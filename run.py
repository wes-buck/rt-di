"""RT.DI orchestrator: discover -> parse -> sanity-gate -> build.

Prints exactly one status line the workflow keys off:
  CHANGED <summary>     new/changed data was built and should be published
  UNCHANGED             nothing new; do not publish
  BLOCKED <json>        sanity gate tripped; do not publish, open an issue

Usage:
  python3 -I run.py                 # full run (fetches DRC)
  python3 -I run.py --no-discover   # skip the network fetch (local rebuild/test)
"""
import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
RAW = ROOT / "raw_data"
TRACKED = ("TF", "FC", "PS", "PM")

COUNTS_FILE = RAW / ".last_counts.json"
FP_FILE = RAW / ".fingerprint"
VERSION_FILE = RAW / "version.txt"

# Files whose content, when changed, should also trigger a publish.
CODE_FILES = ["universal_parser.py", "build_artifact.py", "race_resolver.py",
              "drc_discover.py", "run.py", "pdra_data.py"]
# The artifact is both template and output; hash it with its injected data block
# blanked so template/layout edits republish but the injected data never loops.
TEMPLATE_FILE = "rt_di_artifact.html"
_DATA_BLOCK = re.compile(r'(<script id="rt-data"[^>]*>).*?(</script>)', re.DOTALL)


def counts_from_master():
    """Per-(class,year) run counts from master_runs.csv, plus totals."""
    per = defaultdict(int)
    years = defaultdict(set)
    with open(ROOT / "master_runs.csv") as f:
        for r in csv.DictReader(f):
            per[f"{r['class']}_{r['year']}"] += 1
            years[r["class"]].add(int(r["year"]))
    total = sum(per.values())
    return per, years, total


def latest_year(years):
    allyears = set()
    for s in years.values():
        allyears |= s
    return max(allyears) if allyears else None


def sanity_gate(per, years, total):
    """Return (ok, reasons). Blocks if the total drops vs the last published
    counts, or if a tracked class is empty in the latest season."""
    reasons = []
    prev = {}
    if COUNTS_FILE.exists():
        prev = json.loads(COUNTS_FILE.read_text())
    prev_total = prev.get("_total")

    if prev_total is not None and total < prev_total:
        reasons.append(f"total runs dropped: {prev_total} -> {total}")

    ly = latest_year(years)
    if ly is not None:
        for cls in TRACKED:
            if per.get(f"{cls}_{ly}", 0) == 0:
                reasons.append(f"class {cls} is empty for {ly}")

    # Per-class/year regressions (a class-year that had data losing it all)
    for key, pc in prev.items():
        if key.startswith("_"):
            continue
        if pc > 0 and per.get(key, 0) == 0:
            reasons.append(f"{key} went from {pc} runs to 0")

    return (len(reasons) == 0), reasons


def fingerprint(total, per):
    h = hashlib.sha256()
    h.update((ROOT / "master_runs.csv").read_bytes())
    for f in sorted(CODE_FILES):
        p = ROOT / f
        if p.exists():
            h.update(p.read_bytes())
    tpl = ROOT / TEMPLATE_FILE
    if tpl.exists():
        stripped = _DATA_BLOCK.sub(r"\1\2", tpl.read_text())
        h.update(stripped.encode())
    h.update(json.dumps(per, sort_keys=True).encode())
    return h.hexdigest()


def bump_patch(v):
    v = (v or "v1.7.1").strip()
    pre = "v" if v.startswith("v") else ""
    nums = v.lstrip("v").split(".")
    try:
        nums = [int(x) for x in nums]
        nums[-1] += 1
        return pre + ".".join(str(x) for x in nums)
    except ValueError:
        return v


def main():
    do_discover = "--no-discover" not in sys.argv
    discovered_new = 0
    if do_discover:
        try:
            import drc_discover
            drc_discover.main()
        except Exception as e:  # network/parse hiccup: keep going with saved data
            print(f"warn: discovery failed ({e}); using saved raw data")

    # Count how many discovered stories are ingested (for the summary)
    idx = RAW / "discovered.json"
    if idx.exists():
        d = json.loads(idx.read_text())
        discovered_new = sum(1 for m in d.get("stories", {}).values() if m.get("status") == "ingested")

    import universal_parser
    universal_parser.main()

    per, years, total = counts_from_master()
    ok, reasons = sanity_gate(per, years, total)
    if not ok:
        print("BLOCKED " + json.dumps({"reasons": reasons, "total": total, "counts": per}))
        return 2

    fp = fingerprint(total, per)
    prev_fp = FP_FILE.read_text().strip() if FP_FILE.exists() else ""

    if fp == prev_fp:
        print("UNCHANGED")
        return 0

    # Data (or code) changed: bump version, build, record state.
    old_v = VERSION_FILE.read_text().strip() if VERSION_FILE.exists() else "v1.7.1"
    new_v = bump_patch(old_v)
    VERSION_FILE.write_text(new_v + "\n")

    import build_artifact
    build_artifact.main()

    FP_FILE.write_text(fp + "\n")
    snapshot = dict(per)
    snapshot["_total"] = total
    COUNTS_FILE.write_text(json.dumps(snapshot, indent=1, sort_keys=True))

    summary = f"{new_v} (was {old_v}); total {total} runs; ingested stories {discovered_new}"
    print("CHANGED " + summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
