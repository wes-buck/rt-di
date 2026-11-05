"""Probe what DRC returns for real vs out-of-range story IDs, to design a
reliable 'is this a published story' signal. Temporary."""
import html as htmlmod
import re
import urllib.request

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
DATELINE = re.compile(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+\d{1,2}\s+"
                      r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4},\s+\d{1,2}:\d{2}", re.I)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL | re.I)


def text(raw):
    h = raw.decode("iso-8859-1", "replace")
    h = re.sub(r"<script\b[^>]*>.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", htmlmod.unescape(h)).strip()


for sid in [424151, 424155, 424160, 424300, 424908, 425707, 426500, 999999]:
    try:
        req = urllib.request.Request(f"https://www.dragracecentral.com/DRCStory.asp?ID={sid}", headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
        t = text(raw)
        mt = TITLE.search(raw.decode("iso-8859-1", "replace"))
        dl = DATELINE.search(t)
        print(f"ID={sid} bytes={len(raw):6d} title={ (mt.group(1).strip()[:55] if mt else '')!r:57} "
              f"summary={'Y' if 'Summary of eliminations' in t else '-'} "
              f"dateline={'Y' if dl else '-'} first120={t[:120]!r}")
    except Exception as e:
        print(f"ID={sid} ERROR {e}")
