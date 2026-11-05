"""Auto-discover new DragRaceCentral "Summary of Eliminations" articles.

No manual story-ID or date edits: this walks DRC's sequential story IDs forward
from where it last stopped, and for every Top Fuel / Funny Car / Pro Stock /
Pro Modified eliminations summary it finds, it saves the article body and records
its class, canonical race name (via race_resolver) and date (taken from the
article). It skips Pro Stock Motorcycle, exhibition/specialty classes, empty
articles, and duplicates of a race already captured.

State and raw data (both committed, kept forever):
  raw_data/discovered.json        index: frontier id + per-story metadata
  raw_data/stories/<id>.txt        the raw eliminations body for each story

Run:  python3 -I drc_discover.py           # scan from the saved frontier
      python3 -I drc_discover.py --from N   # force a start id (re-scan)
Env:  RTDI_SCAN_MAX_FETCH (default 800), RTDI_SCAN_GAP (40), RTDI_SCAN_OVERLAP (15)
"""
import html as htmlmod
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))  # work even under `python -I` (isolated mode)

import race_resolver  # noqa: E402
RAW = ROOT / "raw_data"
# Index/stories locations can be redirected (CI dry-runs) so a validation scan
# never touches the committed state.
STORIES = Path(os.environ.get("RTDI_STORIES", str(RAW / "stories")))
INDEX = Path(os.environ.get("RTDI_INDEX", str(RAW / "discovered.json")))

# First id to scan on a cold start: one past the last hand-curated story
# (424123 Funny Car Las Vegas 2026; 424124 is the Comp exhibition). Everything
# at or below this is already in the hand-built RACE_NAMES/RACE_DATES tables.
SEED_FRONTIER = 424124

GAP = int(os.environ.get("RTDI_SCAN_GAP", "40"))          # stop this far past the last live page
OVERLAP = int(os.environ.get("RTDI_SCAN_OVERLAP", "15"))  # re-check this many ids below the frontier
MAX_FETCH = int(os.environ.get("RTDI_SCAN_MAX_FETCH", "800"))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

MONTHS = {m: f"{i:02d}" for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL | re.IGNORECASE)
DATELINE_RE = re.compile(
    r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+(\d{1,2})\s+"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4}),\s+\d{1,2}:\d{2}",
    re.IGNORECASE)
CLASS_RE = re.compile(r"Summary of eliminations in\s+(.+?)\s+at the", re.IGNORECASE)
EVENT_RE = re.compile(r"Summary of eliminations in\s+.+?\s+at the\s+(.+?):", re.IGNORECASE | re.DOTALL)
CITY_RE = re.compile(r"([A-Z][A-Za-z.\- ]+?)(?:,\s*[A-Za-z.]+)?\s*-\s*Summary of eliminations", re.IGNORECASE)


def fetch(story_id, tries=4):
    url = f"https://www.dragracecentral.com/DRCStory.asp?ID={story_id}"
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.getcode(), r.read()
        except urllib.error.HTTPError as e:
            # 5xx are transient (DRC flakes) -> retry; 4xx (404/410) are final.
            if e.code >= 500 and attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            return e.code, (e.read() or b"")
        except Exception:
            if attempt == tries - 1:
                return None, b""
            time.sleep(2 * (attempt + 1))


def to_text(raw):
    h = raw.decode("iso-8859-1", "replace")
    h = re.sub(r"<script\b[^>]*>.*?</script>", " ", h, flags=re.DOTALL | re.IGNORECASE)
    h = re.sub(r"<style\b[^>]*>.*?</style>", " ", h, flags=re.DOTALL | re.IGNORECASE)
    h = re.sub(r"<br\s*/?>", "\n", h, flags=re.IGNORECASE)
    h = re.sub(r"</p>", "\n\n", h, flags=re.IGNORECASE)
    h = re.sub(r"<[^>]+>", " ", h)
    t = htmlmod.unescape(h)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t


def extract_body(text):
    """The eliminations block only (same shape the parser already consumes)."""
    idx = text.find(" - Summary of eliminations")
    if idx < 0:
        idx = text.find("Summary of eliminations")
    if idx < 0:
        return None
    line_start = text.rfind("\n", 0, idx) + 1
    end = len(text)
    for m in ("Low ET:", "Timing data", "NHRA: 10 Most", "NHRA: 10"):
        e = text.find(m, idx)
        if 0 < e < end:
            end = e
    block = text[line_start:end].strip()
    block = re.sub(r"([^\n])\n(?!\n|Round |Low ET|Timing|$)", r"\1 ", block)
    return block


def classify(class_name):
    """DRC class label -> our code, or None to skip.

    Match the professional class name EXACTLY (after normalizing whitespace/case).
    This is deliberately strict: DRC also runs 'Top Alcohol Funny Car', 'Top
    Alcohol Dragster', 'Pro Stock Motorcycle', etc. A loose substring test would
    map 'Top Alcohol Funny Car' to Funny Car -- exactly the bug that injected
    sportsman runs into a nitro class. Only the four pro classes we track pass."""
    n = re.sub(r"\s+", " ", (class_name or "").strip().lower())
    return {
        "top fuel": "TF",
        "funny car": "FC",
        "pro stock": "PS",
        "pro modified": "PM",
        "pro mod": "PM",
    }.get(n)


def parse_date(text):
    m = DATELINE_RE.search(text)
    if not m:
        return None
    day, mon, year = m.group(1), m.group(2).title(), m.group(3)
    return f"{year}-{MONTHS[mon]}-{int(day):02d}"


def has_runs(body):
    return bool(body) and "Round 1" in body and (" def." in body or " def " in body)


def load_index():
    if INDEX.exists():
        d = json.loads(INDEX.read_text())
        d.setdefault("stories", {})
        d.setdefault("frontier", SEED_FRONTIER)
        return d
    return {"frontier": SEED_FRONTIER, "stories": {}}


def save_index(idx):
    STORIES.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(idx, indent=1, sort_keys=True))


def ingested_triples(idx):
    out = {}
    for sid, m in idx["stories"].items():
        if m.get("status") == "ingested":
            out[(m["class"], m["race"], m["year"])] = sid
    return out


def existing_coverage():
    """(class, race, year) triples already present in the committed data
    (hand-built history below the scan seed, plus everything published so far).
    Seeding dedup with these stops a late/duplicate re-post of a race we already
    have from being ingested a second time."""
    import csv as _csv
    cov = {}
    mf = ROOT / "master_runs.csv"
    if mf.exists():
        with open(mf) as f:
            for r in _csv.DictReader(f):
                try:
                    cov[(r["class"], r["race"], int(r["year"]))] = "committed"
                except (KeyError, ValueError):
                    continue
    return cov


def main():
    start_override = None
    if "--from" in sys.argv:
        start_override = int(sys.argv[sys.argv.index("--from") + 1])

    idx = load_index()
    frontier = idx["frontier"]
    start = start_override if start_override is not None else max(SEED_FRONTIER, frontier - OVERLAP)
    # Dedup against both previously ingested stories and races already in the
    # committed baseline data (so a duplicate re-post of a historical race is skipped).
    triples = existing_coverage()
    triples.update(ingested_triples(idx))

    print(f"scan start={start} frontier={frontier} gap={GAP} max_fetch={MAX_FETCH}")
    sid = start
    fetched = 0
    last_live = frontier
    new_articles, skipped = [], []
    while fetched < MAX_FETCH:
        if sid > last_live + GAP:
            break
        code, raw = fetch(sid)
        fetched += 1
        text = to_text(raw)
        # A real published story is HTTP 200 and carries a publication dateline.
        # Out-of-range ids return 410/500 (or tiny stubs) and must NOT advance the
        # frontier, or the scan runs away past where real stories will appear.
        is_story = (code == 200) and bool(parse_date(text))
        if is_story:
            last_live = max(last_live, sid)

        if code == 200 and "Summary of eliminations" in text:
            cm = CLASS_RE.search(text)
            class_name = cm.group(1).strip() if cm else ""
            code = classify(class_name)
            em = EVENT_RE.search(text)
            event = (em.group(1).strip() if em else "")
            if "Series," in event:
                event = event.split("Series,")[-1].strip()
            event = re.sub(r"\s+", " ", event)
            cym = CITY_RE.search(text)
            city = (cym.group(1).strip() if cym else "")
            date = parse_date(text)
            year = int(date[:4]) if date else None
            month = date[5:7] if date else ""
            sids = str(sid)

            if code is None:
                skipped.append((sids, f"class '{class_name}' not tracked"))
                idx["stories"][sids] = {"status": "skipped", "reason": f"class '{class_name}' not tracked",
                                        "city": city, "event": event}
            elif date is None:
                skipped.append((sids, "no date line"))
                idx["stories"][sids] = {"status": "skipped", "reason": "no date line",
                                        "class": code, "event": event, "city": city}
            else:
                body = extract_body(text)
                race, confident = race_resolver.resolve(event, city, month)
                if not has_runs(body):
                    skipped.append((sids, f"empty ({code} {race} {year})"))
                    idx["stories"][sids] = {"status": "skipped", "reason": "empty article",
                                            "class": code, "race": race, "year": year,
                                            "date": date, "city": city, "event": event}
                elif (code, race, year) in triples and triples[(code, race, year)] != sids:
                    skipped.append((sids, f"duplicate of {triples[(code, race, year)]} ({code} {race} {year})"))
                    idx["stories"][sids] = {"status": "skipped", "reason": "duplicate",
                                            "class": code, "race": race, "year": year,
                                            "date": date, "city": city, "event": event,
                                            "duplicate_of": triples[(code, race, year)]}
                else:
                    STORIES.mkdir(parents=True, exist_ok=True)
                    (STORIES / f"{sid}.txt").write_text(body, encoding="utf-8")
                    idx["stories"][sids] = {"status": "ingested", "class": code, "race": race,
                                            "year": year, "date": date, "city": city,
                                            "event": event, "confident": confident}
                    triples[(code, race, year)] = sids
                    new_articles.append((sids, code, race, year, date, confident))
                    flag = "" if confident else "  [UNCONFIRMED NAME - check race_resolver]"
                    print(f"  + {sid} {code} {race} {year} {date}{flag}")

        sid += 1

    idx["frontier"] = max(frontier, last_live)
    save_index(idx)

    print(f"\ndone: fetched={fetched} new={len(new_articles)} skipped_this_run={len(skipped)} "
          f"frontier->{idx['frontier']}")
    for s, why in skipped[:25]:
        print(f"  - {s}: {why}")
    # machine-readable summary line for the orchestrator / CI
    unconfident = [a[0] for a in new_articles if not a[5]]
    print("DISCOVER_RESULT " + json.dumps({
        "new": len(new_articles),
        "new_ids": [a[0] for a in new_articles],
        "unconfident_ids": unconfident,
        "frontier": idx["frontier"],
        "capped": fetched >= MAX_FETCH,
    }))


if __name__ == "__main__":
    main()
