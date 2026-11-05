"""DRC recon: prove dragracecentral.com is reachable from GitHub's servers and
dump enough page structure to design auto-discovery + date extraction.

Writes:
  recon_out/<ID>.html         full raw HTML for a few sample stories
  recon_out/findings.txt       human-readable summary (also echoed to the log)

Usage: python3 -I tools/recon_drc.py
"""
import html as htmlmod
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

OUT = Path("recon_out")
OUT.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

# Known story IDs (from the existing story_ids.json) spanning the 4 classes of
# recent race weekends, plus IDs just past the known max to see what a
# not-yet-existing / non-eliminations / other-class story looks like.
KNOWN = {
    "424121": "2026 Nevada Nationals TF (known eliminations)",
    "424120": "2026 Nevada Nationals PS (known eliminations)",
    "424122": "2026 Nevada Nationals PM/Pro Mod (known eliminations)",
    "424123": "2026 Nevada Nationals FC (known eliminations)",
}
# A forward window to characterize the ID space just beyond the known max.
PROBE_RANGE = list(range(424118, 424150))


def fetch(story_id, tries=3):
    url = f"https://www.dragracecentral.com/DRCStory.asp?ID={story_id}"
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return r.getcode(), r.geturl(), raw
        except urllib.error.HTTPError as e:
            return e.code, url, (e.read() or b"")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (attempt + 1))
    return None, url, str(last).encode()


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


DATE_PATTERNS = [
    re.compile(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4}", re.I),
    re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"),
    re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}", re.I),
    re.compile(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*,?\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}", re.I),
]
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL | re.IGNORECASE)
SUMMARY_RE = re.compile(r"Summary of eliminations in ([A-Za-z /]+?) at ", re.IGNORECASE)


def findings_for(story_id, note, code, final_url, raw):
    lines = [f"\n========== ID={story_id}  [{note}] =========="]
    lines.append(f"http_status={code}  bytes={len(raw)}  final_url={final_url}")
    text = to_text(raw)
    mt = TITLE_RE.search(raw.decode("iso-8859-1", "replace"))
    lines.append(f"<title>: {mt.group(1).strip()[:200] if mt else '(none)'}")
    ms = SUMMARY_RE.search(text)
    lines.append(f"eliminations_class: {ms.group(1).strip() if ms else '(not an eliminations story)'}")
    # The whole first content line often carries city + event name
    idx = text.find("Summary of eliminations")
    if idx >= 0:
        ls = text.rfind("\n", 0, idx) + 1
        le = text.find("\n", idx)
        lines.append(f"header_line: {text[ls:le if le > 0 else ls + 300].strip()[:300]}")
    # Date hunting: show every date-like token and a little context
    found_dates = []
    for pat in DATE_PATTERNS:
        for m in pat.finditer(text[:4000]):
            s = max(0, m.start() - 40)
            found_dates.append(text[s:m.end() + 10].replace("\n", " ").strip())
    lines.append("date_candidates (first 4000 chars):")
    for d in found_dates[:12]:
        lines.append(f"    | {d}")
    if not found_dates:
        lines.append("    (none in first 4000 chars)")
    return "\n".join(lines)


def main():
    report = []
    # 1) Known eliminations stories: save full HTML + findings
    for sid, note in KNOWN.items():
        code, final_url, raw = fetch(sid)
        (OUT / f"{sid}.html").write_bytes(raw)
        report.append(findings_for(sid, note, code, final_url, raw))
        # For ONE known story, also dump the first 3500 chars of plain text so we
        # can see exactly where the date sits relative to the body.
        if sid == "424121":
            report.append("---- first 3500 chars of plain text for 424121 ----")
            report.append(to_text(raw)[:3500])
        time.sleep(0.4)

    # 2) Forward probe window: classify the ID space beyond the known max
    report.append("\n\n########## FORWARD PROBE WINDOW ##########")
    for n in PROBE_RANGE:
        sid = str(n)
        code, final_url, raw = fetch(sid)
        text = to_text(raw)
        ms = SUMMARY_RE.search(text)
        cls = ms.group(1).strip() if ms else "-"
        title = TITLE_RE.search(raw.decode("iso-8859-1", "replace"))
        title = title.group(1).strip()[:90] if title else ""
        is_elim = "ELIM" if ms else ""
        # save full HTML for the first non-known eliminations story we find, so a
        # PSM / exhibition / later-posted article can be inspected
        if ms and sid not in KNOWN:
            (OUT / f"{sid}.html").write_bytes(raw)
        report.append(f"ID={sid} status={code} bytes={len(raw):6d} {is_elim:4s} class={cls:28s} title={title}")
        time.sleep(0.3)

    text_report = "\n".join(report)
    (OUT / "findings.txt").write_text(text_report)
    print(text_report)


if __name__ == "__main__":
    main()
