"""Build the RT.DI artifact JSON payload and inject into rt_di_artifact.html.

Run after universal_parser.py has produced master_runs.csv.
"""

import csv
import json
from datetime import date as _date
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).parent
RAW = ROOT / "raw_data"
DEFAULT_VERSION = "v1.7.1"


def _load_discovered():
    """Return (dates, cities): (race,year)->date and (race,year)->DRC city, for
    auto-discovered stories. Hand-built RACE_DATES below take precedence."""
    idx = RAW / "discovered.json"
    dates, cities = {}, {}
    if idx.exists():
        data = json.loads(idx.read_text())
        for meta in data.get("stories", {}).values():
            if meta.get("status") == "ingested" and meta.get("race") and meta.get("year"):
                key = (meta["race"], int(meta["year"]))
                if meta.get("date"):
                    dates[key] = meta["date"]
                if meta.get("city"):
                    cities[key] = meta["city"].title()
    return dates, cities


def _read_version():
    vf = RAW / "version.txt"
    if vf.exists():
        v = vf.read_text().strip()
        if v:
            return v
    return DEFAULT_VERSION


def _fmt_ticker(race, year, iso_date, city):
    """Ticker string in the existing style, e.g.
    'NHRA Nevada Nationals — Las Vegas — 11.01.26'."""
    bits = [f"NHRA {race}"]
    if city:
        bits.append(city)
    if iso_date:
        y, m, d = iso_date.split("-")
        bits.append(f"{m}.{d}.{y[2:]}")
    return " — ".join(bits)

# Canonical race name → date (used for TF/FC/PS/PM and PDRA after normalization)
RACE_DATES = {
    # 2026 PDRA
    ("Carolina Nationals", 2026): "2026-03-28",
    ("East Coast Nationals", 2026): "2026-04-18",
    ("North vs South Shootout", 2026): "2026-06-27",
    ("Thunder Valley Throwdown", 2026): "2026-08-08",
    ("DragWars", 2026): "2026-08-29",
    ("Brian Olson Memorial World Finals", 2026): "2026-09-20",
    # 2025 PDRA (Norwalk cancelled, Pro Stars excluded as specialty event)
    ("East Coast Nationals", 2025): "2025-04-05",
    ("Mid-Atlantic Showdown", 2025): "2025-05-03",
    ("North vs South Shootout", 2025): "2025-06-14",
    ("Northern Nationals", 2025): "2025-08-02",
    ("Thunder Valley Throwdown", 2025): "2025-08-23",
    ("DragWars", 2025): "2025-09-13",
    ("Brian Olson Memorial World Finals", 2025): "2025-10-05",
    # NHRA 2025
    ("Gatornationals", 2025): "2025-03-09",
    ("Arizona Nationals", 2025): "2025-03-23",
    ("Winternationals", 2025): "2025-03-30",
    ("4-Wide Nationals", 2025): "2025-04-13",
    ("4-Wide Carolina", 2025): "2025-04-27",
    ("Route 66", 2025): "2025-05-18",
    ("New England Nationals", 2025): "2025-06-01",
    ("Thunder Valley Nationals", 2025): "2025-06-08",
    ("Virginia Nationals", 2025): "2025-06-22",
    ("Summit Racing Nationals", 2025): "2025-06-29",
    ("Northwest Nationals", 2025): "2025-07-20",
    ("Sonoma Nationals", 2025): "2025-07-27",
    ("Lucas Oil Nationals", 2025): "2025-08-17",
    ("US Nationals", 2025): "2025-09-01",
    ("Reading Nationals", 2025): "2025-09-14",
    ("Carolina 4-Wide Nationals", 2025): "2025-09-21",
    ("Midwest Nationals", 2025): "2025-09-28",
    ("FallNationals", 2025): "2025-10-12",
    ("Nevada Nationals", 2025): "2025-11-02",
    # 2026
    ("Gatornationals", 2026): "2026-03-08",
    ("Arizona Nationals", 2026): "2026-03-22",
    ("Winternationals", 2026): "2026-04-12",
    ("4-Wide Nationals", 2026): "2026-04-26",
    ("Southern Nationals", 2026): "2026-05-03",
    ("Route 66", 2026): "2026-05-17",
    ("Potomac Nationals", 2026): "2026-05-31",
    ("Great Lakes Nationals", 2026): "2026-09-20",
    ("Nationals at The Rock", 2026): "2026-09-27",
    ("Midwest Nationals", 2026): "2026-10-04",
    ("FallNationals", 2026): "2026-10-18",
    ("Nevada Nationals", 2026): "2026-11-01",
    ("New England Nationals", 2026): "2026-06-07",
    ("Thunder Valley Nationals", 2026): "2026-06-14",
    ("Summit Racing Nationals", 2026): "2026-06-28",
    ("Sonoma Nationals", 2026): "2026-07-19",
    ("Northwest Nationals", 2026): "2026-07-26",
    ("Lucas Oil Nationals", 2026): "2026-08-23",
    ("US Nationals", 2026): "2026-09-07",
    ("Midwest Nationals", 2026): "2026-10-04",
    # 2023 NHRA (TF/FC full schedule + PS/PM partial)
    ("Gatornationals", 2023): "2023-03-12",
    ("Arizona Nationals", 2023): "2023-03-26",
    ("Winternationals", 2023): "2023-04-02",
    ("4-Wide Nationals", 2023): "2023-04-16",
    ("4-Wide Carolina", 2023): "2023-04-30",
    ("Route 66", 2023): "2023-05-21",
    ("New England Nationals", 2023): "2023-06-04",
    ("Thunder Valley Nationals", 2023): "2023-06-11",
    ("Summit Racing Nationals", 2023): "2023-06-25",
    ("Mile-High Nationals", 2023): "2023-07-16",
    ("Northwest Nationals", 2023): "2023-07-23",
    ("Sonoma Nationals", 2023): "2023-07-30",
    ("Heartland Nationals", 2023): "2023-08-13",
    ("Lucas Oil Nationals", 2023): "2023-08-20",
    ("US Nationals", 2023): "2023-09-04",
    ("Reading Nationals", 2023): "2023-09-17",
    ("Carolina Nationals", 2023): "2023-09-24",
    ("Midwest Nationals", 2023): "2023-10-01",
    ("FallNationals", 2023): "2023-10-15",
    ("Nevada Nationals", 2023): "2023-10-29",
    ("Finals", 2023): "2023-11-12",
    # 2024 NHRA (TF/FC/PS full schedule + PM partial)
    ("Gatornationals", 2024): "2024-03-10",
    ("Arizona Nationals", 2024): "2024-03-24",
    ("Winternationals", 2024): "2024-04-14",
    ("4-Wide Nationals", 2024): "2024-04-07",
    ("4-Wide Carolina", 2024): "2024-04-28",
    ("Route 66", 2024): "2024-05-19",
    ("New England Nationals", 2024): "2024-06-02",
    ("Thunder Valley Nationals", 2024): "2024-06-09",
    ("Virginia Nationals", 2024): "2024-06-23",
    ("Summit Racing Nationals", 2024): "2024-06-30",
    ("Northwest Nationals", 2024): "2024-07-21",
    ("Sonoma Nationals", 2024): "2024-07-28",
    ("Lucas Oil Nationals", 2024): "2024-08-18",
    ("US Nationals", 2024): "2024-09-02",
    ("Reading Nationals", 2024): "2024-09-15",
    ("Carolina Nationals", 2024): "2024-09-22",
    ("Midwest Nationals", 2024): "2024-09-29",
    ("FallNationals", 2024): "2024-10-13",
    ("Nevada Nationals", 2024): "2024-11-03",
    ("Finals", 2024): "2024-11-17",
}


def main():
    rows = []
    with open(ROOT / "master_runs.csv") as f:
        for r in csv.DictReader(f):
            opps_raw = r.get("opps", "") or ""
            opps = [o for o in opps_raw.split("|") if o]
            rows.append(
                {
                    "c": r["class"],
                    "r": r["race"],
                    "y": int(r["year"]),
                    "rd": int(r["round"]),
                    "d": r["driver"],
                    "rt": float(r["rt"]),
                    "et": float(r["et"]),
                    "m": float(r["mph"]),
                    "w": r["win"] == "True",
                    "o": opps,
                }
            )

    # Append PDRA Pro Nitrous + Pro Boost runs (transcribed via vision OCR)
    try:
        import pdra_data
        for r in pdra_data.RUNS:
            rows.append(
                {
                    "c": r["class"],
                    "r": r["race"],
                    "y": r["year"],
                    "rd": r["round"],
                    "d": r["driver"],
                    "rt": r["rt"],
                    "et": r["et"],
                    "m": r["mph"],
                    "w": r["win"],
                    "o": r["opps"],
                }
            )
        print(f"PDRA rows added: {len(pdra_data.RUNS)}")
    except ImportError:
        print("WARN: pdra_data not loaded")

    # Merge auto-discovered race dates/cities (hand-built RACE_DATES win)
    disc_dates, disc_cities = _load_discovered()
    merged_dates = dict(disc_dates)
    merged_dates.update(RACE_DATES)  # curated values override discovered ones

    # Build races meta — for every (race, year) present in the data
    race_meta = {}
    races_in_data = set((r["r"], r["y"]) for r in rows)
    for (race, year) in races_in_data:
        race_meta[(race, year)] = merged_dates.get((race, year), "")

    # Average field-size per class per year (R1 unique drivers / # races)
    by_class_year = {}
    for r in rows:
        key = (r["c"], r["y"])
        if r["rd"] != 1:
            continue
        by_class_year.setdefault(key, {}).setdefault(r["r"], set()).add(r["d"])

    field_avg = {}
    for key, races in by_class_year.items():
        sizes = [len(d) for d in races.values()]
        field_avg["{}_{}".format(*key)] = round(sum(sizes) / len(sizes), 1) if sizes else 0

    # Latest-dated race drives the ticker (lastRace)
    dated = [(d, r, y) for (r, y), d in race_meta.items() if d]
    if dated:
        last_date, last_race, last_year = max(dated)
        ticker = _fmt_ticker(last_race, last_year, last_date,
                             disc_cities.get((last_race, last_year), ""))
    else:
        ticker = "NHRA RT.DI"

    data = {
        "runs": rows,
        "races": [
            {"race": k[0], "year": k[1], "date": v}
            for k, v in sorted(race_meta.items(), key=lambda kv: (kv[1] or "", kv[0][0]))
        ],
        "fieldAvg": field_avg,
        "version": _read_version(),
        "lastRace": ticker,
    }

    out_json = ROOT / "rt_di_data.json"
    out_json.write_text(json.dumps(data, separators=(",", ":")))

    # Patch HTML
    html_template = (ROOT / "rt_di_artifact.html").read_text()
    # Detect whether the template still has __DATA__ placeholder. If not, find the
    # existing JSON block and replace it.
    if "__DATA__" in html_template:
        new_html = html_template.replace("__DATA__", out_json.read_text().replace("</script>", "<\\/script>"))
    else:
        # Replace existing data block (between <script id="rt-data" ...> and </script>)
        import re
        new_html = re.sub(
            r'(<script id="rt-data"[^>]*>)(.*?)(</script>)',
            lambda m: m.group(1) + out_json.read_text().replace("</script>", "<\\/script>") + m.group(3),
            html_template,
            count=1,
            flags=re.DOTALL,
        )
    (ROOT / "rt_di_artifact.html").write_text(new_html)
    print(f"JSON: {out_json.stat().st_size:,} bytes")
    print(f"HTML: {(ROOT / 'rt_di_artifact.html').stat().st_size:,} bytes")
    print(f"Field-size averages: {field_avg}")


if __name__ == "__main__":
    main()
