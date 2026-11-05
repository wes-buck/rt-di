"""Structural accuracy audit of master_runs.csv.

Catches the kinds of errors a scrape/parse can introduce without any external
source: broken opponent links, losers that reappear in a later round, a driver
listed twice in one round, implausible timing numbers, and garbage names.

Exit code is non-zero if any ERROR-level issue is found. WARN-level issues are
printed but do not fail. Run: python3 -I validate_data.py
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent

# Loose plausibility bounds per class (full pulls; broken runs can be slow, so
# upper bounds are generous -- we only flag the physically impossible).
ET_BOUNDS = {"TF": (3.5, 20), "FC": (3.5, 20), "PS": (6.0, 20), "PM": (5.2, 20)}
MPH_MAX = 345.0
RT_BOUNDS = (-0.5, 2.0)
NAME_RE = re.compile(r"^[A-Za-z][A-Za-z.'\- ]{1,40}$")


def load():
    rows = []
    with open(ROOT / "master_runs.csv") as f:
        for r in csv.DictReader(f):
            r["year"] = int(r["year"]); r["round"] = int(r["round"])
            r["rt"] = float(r["rt"]); r["et"] = float(r["et"]); r["mph"] = float(r["mph"])
            r["win"] = r["win"] == "True"
            r["opps"] = [o for o in (r.get("opps", "") or "").split("|") if o]
            rows.append(r)
    return rows


def main():
    rows = load()
    errors, warns = [], []

    # Index by event and by (event, round)
    by_event = defaultdict(list)
    for r in rows:
        by_event[(r["class"], r["race"], r["year"])].append(r)

    # 1) Value ranges + name sanity
    for r in rows:
        tag = f"{r['class']} {r['race']} {r['year']} R{r['round']} {r['driver']}"
        lo, hi = ET_BOUNDS.get(r["class"], (3.0, 25))
        if r["et"] and not (lo <= r["et"] <= hi):
            warns.append(f"ET out of range ({r['et']}): {tag}")
        if r["mph"] and r["mph"] > MPH_MAX:
            errors.append(f"MPH impossible ({r['mph']}): {tag}")
        if not (RT_BOUNDS[0] <= r["rt"] <= RT_BOUNDS[1]):
            warns.append(f"RT out of range ({r['rt']}): {tag}")
        if not NAME_RE.match(r["driver"]):
            errors.append(f"suspect driver name {r['driver']!r}: {tag}")

    # 2) Opponent symmetry within an event+round
    for key, ev in by_event.items():
        by_round = defaultdict(list)
        for r in ev:
            by_round[r["round"]].append(r)
        for rnd, rs in by_round.items():
            names = [r["driver"] for r in rs]
            # duplicate driver in a single round
            dupes = {n for n in names if names.count(n) > 1}
            for d in dupes:
                errors.append(f"driver appears {names.count(d)}x in one round: {d} - {key} R{rnd}")
            present = set(names)
            for r in rs:
                for opp in r["opps"]:
                    if opp not in present:
                        warns.append(f"opponent {opp!r} not found in same round as {r['driver']}: {key} R{rnd}")

    # 3) Advancement: round N+1 field should be winners of round N (allow byes)
    for key, ev in by_event.items():
        by_round = defaultdict(list)
        for r in ev:
            by_round[r["round"]].append(r)
        rounds = sorted(by_round)
        for i in range(len(rounds) - 1):
            rn, rn1 = rounds[i], rounds[i + 1]
            winners = {r["driver"] for r in by_round[rn] if r["win"]}
            nextfield = {r["driver"] for r in by_round[rn1]}
            intruders = nextfield - winners
            # A bye runner can advance without a logged win; tolerate a couple.
            if len(intruders) > 2:
                errors.append(f"{len(intruders)} drivers in R{rn1} did not win R{rn}: "
                              f"{key} -> {sorted(intruders)[:6]}")
            elif intruders:
                warns.append(f"R{rn1} entrants not among R{rn} winners (byes?): {key} {sorted(intruders)}")

    # 4) Each event should have a single champion (one winner in its last round)
    for key, ev in by_event.items():
        last = max(r["round"] for r in ev)
        champs = [r["driver"] for r in ev if r["round"] == last and r["win"]]
        if len(champs) == 0:
            warns.append(f"no winner recorded in final round: {key}")
        elif len(champs) > 1:
            warns.append(f"{len(champs)} winners in final round: {key} {champs}")

    # Report
    print(f"Audited {len(rows)} runs across {len(by_event)} events.\n")
    print(f"ERRORS: {len(errors)}")
    for e in errors[:60]:
        print(f"  [ERR] {e}")
    print(f"\nWARNINGS: {len(warns)}")
    for w in warns[:40]:
        print(f"  [warn] {w}")
    if len(warns) > 40:
        print(f"  ... and {len(warns) - 40} more warnings")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
