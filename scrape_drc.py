"""Fetch DRC story HTML and extract the eliminations summary body.

Usage:
    python3 scrape_drc.py 2023      # fetch all 2023_* classes from story_ids.json
    python3 scrape_drc.py 2024      # 2024
    python3 scrape_drc.py both      # both years

Writes raw_data/<YEAR>_<CLASS>_summaries.txt files.
"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
RAW = ROOT / "raw_data"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch(story_id):
    url = f"https://www.dragracecentral.com/DRCStory.asp?ID={story_id}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("iso-8859-1")


def extract_body(html):
    """Pull text from <body>, strip tags, find the eliminations summary block."""
    # Naive but effective: strip script/style, drop tags, get text
    html = re.sub(r"<script\b[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style\b[^>]*>.*?</style>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    # Preserve paragraph breaks
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"</p>", "\n\n", html, flags=re.IGNORECASE)
    html = re.sub(r"<[^>]+>", " ", html)
    # Decode HTML entities
    import html as htmlmod
    text = htmlmod.unescape(html)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    idx = text.find(" - Summary of eliminations")
    if idx < 0:
        return None
    line_start = text.rfind("\n", 0, idx) + 1
    end_markers = ["Low ET:", "Timing data", "NHRA: 10 Most"]
    end = len(text)
    for m in end_markers:
        e = text.find(m, idx)
        if 0 < e < end:
            end = e
    block = text[line_start:end].strip()
    # Collapse soft-wrap newlines within pairings — single \n not followed by \n or "Round " becomes space
    block = re.sub(r"([^\n])\n(?!\n|Round |Low ET|Timing|$)", r"\1 ", block)
    return block


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else ["2023"]
    years = []
    for t in targets:
        if t == "both":
            years = [2023, 2024]
            break
        years.append(int(t))

    story_ids = json.loads((RAW / "story_ids.json").read_text())

    for year in years:
        for cls in ("TF", "FC", "PS", "PM"):
            key = f"{cls}_{year}"
            if key not in story_ids:
                print(f"skip {key} (not in story_ids.json)")
                continue
            entries = story_ids[key]
            print(f"\n== {key}: {len(entries)} races ==")
            blocks = []
            for story_id, _venue, _name in entries:
                try:
                    html = fetch(story_id)
                    body = extract_body(html)
                    if not body:
                        print(f"  {story_id}: NO BODY")
                        continue
                    blocks.append(f"===== RACE_ID={story_id} =====\n{body}\n\n")
                    print(f"  {story_id}: {len(body)} chars")
                except Exception as e:
                    print(f"  {story_id}: ERROR {e}")
                time.sleep(0.2)  # be gentle
            out = RAW / f"{year}_{cls}_summaries.txt"
            out.write_text("".join(blocks))
            print(f"  -> wrote {out} ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
