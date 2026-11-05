"""
RT.DI Universal Parser
Parses all NHRA elimination summary text files into per-class CSVs
and a master_runs.csv with class column.
"""

import re
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
RAW = ROOT / "raw_data"

# Map (class, year, race_id) -> race name. Race names match the existing TF
# convention (no city qualifier).
RACE_NAMES = {
    # 2025 TF (existing) — these are inferred from the existing 2025_TF_runs.csv,
    # but we re-emit TF rows by ALSO reading the existing CSV directly later.
    # The dict below only needs to cover FC/PS/PM ids we pull from raw txts.

    # 2025 FC
    "405877": "Gatornationals",
    "406214": "Arizona Nationals",
    "406401": "Winternationals",
    "406600": "4-Wide Nationals",
    "407224": "4-Wide Carolina",
    "407557": "Route 66",
    "408179": "New England Nationals",
    "408405": "Thunder Valley Nationals",
    "408742": "Virginia Nationals",
    "409175": "Summit Racing Nationals",
    "409898": "Northwest Nationals",
    "410054": "Sonoma Nationals",
    "410846": "Lucas Oil Nationals",
    "411531": "US Nationals",
    "412097": "Reading Nationals",
    "412542": "Carolina 4-Wide Nationals",
    "412870": "Midwest Nationals",
    "413597": "FallNationals",
    "414398": "Nevada Nationals",
    # 2025 PS
    "405876": "Gatornationals",
    "406213": "Arizona Nationals",
    "406400": "Winternationals",
    "406602": "4-Wide Nationals",
    "407223": "4-Wide Carolina",
    "408178": "New England Nationals",
    "408404": "Thunder Valley Nationals",
    "409174": "Summit Racing Nationals",
    "409895": "Northwest Nationals",
    "410053": "Sonoma Nationals",
    "410844": "Lucas Oil Nationals",
    "411530": "US Nationals",
    "412095": "Reading Nationals",
    "412540": "Carolina 4-Wide Nationals",
    "412871": "Midwest Nationals",
    "413606": "FallNationals",
    "414397": "Nevada Nationals",
    # 2025 PM
    "406156": "Gatornationals",
    "406212": "Arizona Nationals",
    "407214": "4-Wide Carolina",
    "407555": "Route 66",
    "408401": "Thunder Valley Nationals",
    "408740": "Virginia Nationals",
    "411525": "US Nationals",
    "412531": "Carolina 4-Wide Nationals",
    "412863": "Midwest Nationals",
    "414393": "Nevada Nationals",
    # 2026 FC
    "415429": "Gatornationals",
    "416021": "Arizona Nationals",
    "416580": "Winternationals",
    "417089": "4-Wide Nationals",
    "417319": "Southern Nationals",
    "417780": "Route 66",
    "418135": "Potomac Nationals",
    "418327": "New England Nationals",
    "422462": "Great Lakes Nationals",
    "422773": "Nationals at The Rock",
    "423037": "Midwest Nationals",
    "423623": "FallNationals",
    "424123": "Nevada Nationals",
    "418598": "Thunder Valley Nationals",
    "419298": "Summit Racing Nationals",
    "419895": "Sonoma Nationals",
    "420208": "Northwest Nationals",
    "421170": "Lucas Oil Nationals",
    "421918": "US Nationals",
    # 2026 PS
    "415430": "Gatornationals",
    "416020": "Arizona Nationals",
    "416578": "Winternationals",
    "417087": "4-Wide Nationals",
    "417316": "Southern Nationals",
    "417779": "Route 66",
    "418134": "Potomac Nationals",
    "418326": "New England Nationals",
    "422464": "Great Lakes Nationals",
    "422772": "Nationals at The Rock",
    "423036": "Midwest Nationals",
    "423617": "FallNationals",
    "424120": "Nevada Nationals",
    "418593": "Thunder Valley Nationals",
    "419297": "Summit Racing Nationals",
    "419893": "Sonoma Nationals",
    "420192": "Northwest Nationals",
    "421169": "Lucas Oil Nationals",
    "421917": "US Nationals",
    # 2026 PM
    "415420": "Gatornationals",
    "416018": "Arizona Nationals",
    "417080": "4-Wide Nationals",
    "417314": "Southern Nationals",
    "417770": "Route 66",
    "418592": "Thunder Valley Nationals",
    "419294": "Summit Racing Nationals",
    "421913": "US Nationals",
    "422770": "Nationals at The Rock",
    "423034": "Midwest Nationals",
    "424122": "Nevada Nationals",
    # 2025 TF
    "405875": "Gatornationals",
    "406215": "Arizona Nationals",
    "406402": "Winternationals",
    "406601": "4-Wide Nationals",
    "407225": "4-Wide Carolina",
    "407559": "Route 66",
    "408180": "New England Nationals",
    "408406": "Thunder Valley Nationals",
    "408743": "Virginia Nationals",
    "409184": "Summit Racing Nationals",
    "409896": "Northwest Nationals",
    "410055": "Sonoma Nationals",
    "410845": "Lucas Oil Nationals",
    "411533": "US Nationals",
    "412098": "Reading Nationals",
    "412541": "Carolina 4-Wide Nationals",
    "412873": "Midwest Nationals",
    "413596": "FallNationals",
    "414399": "Nevada Nationals",
    # 2026 TF
    "415431": "Gatornationals",
    "416022": "Arizona Nationals",
    "416579": "Winternationals",
    "417090": "4-Wide Nationals",
    "417321": "Southern Nationals",
    "417778": "Route 66",
    "418136": "Potomac Nationals",
    "418328": "New England Nationals",
    "422463": "Great Lakes Nationals",
    "422774": "Nationals at The Rock",
    "423038": "Midwest Nationals",
    "423626": "FallNationals",
    "424121": "Nevada Nationals",
    "418597": "Thunder Valley Nationals",
    "419295": "Summit Racing Nationals",
    "419894": "Sonoma Nationals",
    "420193": "Northwest Nationals",
    "421171": "Lucas Oil Nationals",
    "421919": "US Nationals",
    # 2024 TF
    "396882": "Gatornationals", "397317": "Arizona Nationals", "397599": "Winternationals",
    "397547": "4-Wide Nationals", "398133": "4-Wide Carolina", "398775": "Route 66",
    "399291": "New England Nationals", "399534": "Thunder Valley Nationals",
    "399957": "Virginia Nationals", "400331": "Summit Racing Nationals",
    "401114": "Northwest Nationals", "401415": "Sonoma Nationals",
    "401949": "Lucas Oil Nationals", "402367": "US Nationals",
    "402815": "Reading Nationals", "403284": "Carolina Nationals",
    "403508": "Midwest Nationals", "404189": "FallNationals",
    "404671": "Nevada Nationals", "405009": "Finals",
    # 2024 FC
    "396883": "Gatornationals", "397320": "Arizona Nationals", "397600": "Winternationals",
    "397546": "4-Wide Nationals", "398134": "4-Wide Carolina", "398774": "Route 66",
    "399290": "New England Nationals", "399533": "Thunder Valley Nationals",
    "399958": "Virginia Nationals", "400330": "Summit Racing Nationals",
    "401113": "Northwest Nationals", "401416": "Sonoma Nationals",
    "401948": "Lucas Oil Nationals", "402366": "US Nationals",
    "402814": "Reading Nationals", "403283": "Carolina Nationals",
    "403509": "Midwest Nationals", "404188": "FallNationals",
    "404673": "Nevada Nationals", "405012": "Finals",
    # 2024 PS
    "396880": "Gatornationals", "397315": "Arizona Nationals", "397601": "Winternationals",
    "397544": "4-Wide Nationals", "398131": "4-Wide Carolina", "398773": "Route 66",
    "399289": "New England Nationals", "399532": "Thunder Valley Nationals",
    "399955": "Virginia Nationals", "400329": "Summit Racing Nationals",
    "401112": "Northwest Nationals", "401414": "Sonoma Nationals",
    "401947": "Lucas Oil Nationals", "402365": "US Nationals",
    "402812": "Reading Nationals", "403281": "Carolina Nationals",
    "403506": "Midwest Nationals", "404187": "FallNationals",
    "404670": "Nevada Nationals", "405010": "Finals",
    # 2024 PM
    "396870": "Gatornationals", "397311": "Arizona Nationals", "398772": "Route 66",
    "399292": "New England Nationals", "399526": "Thunder Valley Nationals",
    "399946": "Virginia Nationals", "402354": "US Nationals",
    "403272": "Carolina Nationals", "403500": "Midwest Nationals",
    "404659": "Nevada Nationals",
    # 2023 TF
    "387184": "Gatornationals", "387517": "Arizona Nationals", "387784": "Winternationals",
    "388064": "4-Wide Nationals", "388740": "4-Wide Carolina", "389020": "Route 66",
    "390089": "New England Nationals", "390056": "Thunder Valley Nationals",
    "390457": "Summit Racing Nationals", "391016": "Mile-High Nationals",
    "391329": "Northwest Nationals", "391629": "Sonoma Nationals",
    "392235": "Heartland Nationals", "392460": "Lucas Oil Nationals",
    "393205": "US Nationals", "393750": "Reading Nationals",
    "394084": "Carolina Nationals", "394313": "Midwest Nationals",
    "395028": "FallNationals", "395465": "Nevada Nationals", "395823": "Finals",
    # 2023 FC
    "387185": "Gatornationals", "387516": "Arizona Nationals", "387783": "Winternationals",
    "388063": "4-Wide Nationals", "388739": "4-Wide Carolina", "389019": "Route 66",
    "390088": "New England Nationals", "390067": "Thunder Valley Nationals",
    "390458": "Summit Racing Nationals", "391004": "Mile-High Nationals",
    "391328": "Northwest Nationals", "391628": "Sonoma Nationals",
    "392234": "Heartland Nationals", "392459": "Lucas Oil Nationals",
    "393204": "US Nationals", "393749": "Reading Nationals",
    "394082": "Carolina Nationals", "394312": "Midwest Nationals",
    "395027": "FallNationals", "395464": "Nevada Nationals", "395822": "Finals",
    # 2023 PS
    "387183": "Gatornationals", "387515": "Arizona Nationals", "387782": "Winternationals",
    "388062": "4-Wide Nationals", "388737": "4-Wide Carolina", "389018": "Route 66",
    "390066": "Thunder Valley Nationals", "390455": "Summit Racing Nationals",
    "391014": "Mile-High Nationals", "392233": "Heartland Nationals",
    "392458": "Lucas Oil Nationals", "393203": "US Nationals",
    "393747": "Reading Nationals", "394080": "Carolina Nationals",
    "394311": "Midwest Nationals", "395026": "FallNationals",
    "395463": "Nevada Nationals", "395821": "Finals",
    # 2023 PM
    "387177": "Gatornationals", "388733": "4-Wide Carolina", "389004": "Route 66",
    "390061": "Thunder Valley Nationals", "390086": "New England Nationals",
    "390442": "Summit Racing Nationals", "392446": "Lucas Oil Nationals",
    "393201": "US Nationals", "394307": "Midwest Nationals", "395453": "Nevada Nationals",
}

# Race weekend dates (YYYY-MM-DD) keyed by race_id
RACE_DATES = {
    # 2025 TF (won't be in our parser output - those are read from existing CSV)
    # 2025 FC
    "405877": "2025-03-09", "406214": "2025-03-23", "406401": "2025-03-30",
    "406600": "2025-04-13", "407224": "2025-04-27", "407557": "2025-05-18",
    "408179": "2025-06-01", "408405": "2025-06-08", "408742": "2025-06-22",
    "409175": "2025-06-29", "409898": "2025-07-20", "410054": "2025-07-27",
    "410846": "2025-08-17", "411531": "2025-09-01", "412097": "2025-09-14",
    "412542": "2025-09-21", "412870": "2025-09-28", "413597": "2025-10-12",
    "414398": "2025-11-02",
    # 2025 PS
    "405876": "2025-03-09", "406213": "2025-03-23", "406400": "2025-03-30",
    "406602": "2025-04-13", "407223": "2025-04-27", "408178": "2025-06-01",
    "408404": "2025-06-08", "409174": "2025-06-29", "409895": "2025-07-20",
    "410053": "2025-07-27", "410844": "2025-08-17", "411530": "2025-09-01",
    "412095": "2025-09-14", "412540": "2025-09-21", "412871": "2025-09-28",
    "413606": "2025-10-12", "414397": "2025-11-02",
    # 2025 PM
    "406156": "2025-03-22", "406212": "2025-03-23", "407214": "2025-04-27",
    "407555": "2025-05-18", "408401": "2025-06-08", "408740": "2025-06-22",
    "411525": "2025-09-01", "412531": "2025-09-21", "412863": "2025-09-28",
    "414393": "2025-11-02",
    # 2026 FC
    "415429": "2026-03-08", "416021": "2026-03-22", "416580": "2026-04-12",
    "417089": "2026-04-26", "417319": "2026-05-03", "417780": "2026-05-17",
    "418135": "2026-05-31", "418327": "2026-06-07", "418598": "2026-06-14",
    "419298": "2026-06-28", "419895": "2026-07-19",
    "420208": "2026-07-26", "421170": "2026-08-23", "421918": "2026-09-07",
    "423037": "2026-10-04", "424123": "2026-11-01",
    "422462": "2026-09-20", "422773": "2026-09-27", "423623": "2026-10-18",
    # 2026 PS
    "415430": "2026-03-08", "416020": "2026-03-22", "416578": "2026-04-12",
    "417087": "2026-04-26", "417316": "2026-05-03", "417779": "2026-05-17",
    "418134": "2026-05-31", "418326": "2026-06-07", "418593": "2026-06-14",
    "419297": "2026-06-28", "419893": "2026-07-19",
    "420192": "2026-07-26", "421169": "2026-08-23", "421917": "2026-09-07",
    "423036": "2026-10-04",
    "422464": "2026-09-20", "422772": "2026-09-27", "423617": "2026-10-18", "424120": "2026-11-01",
    # 2026 PM
    "415420": "2026-03-08", "416018": "2026-03-22", "417080": "2026-04-26",
    "417314": "2026-05-03", "417770": "2026-05-17", "418592": "2026-06-14",
    "419294": "2026-06-28", "421913": "2026-09-07",
    "422770": "2026-09-27", "423034": "2026-10-04", "424122": "2026-11-01",
    # 2025 TF
    "405875": "2025-03-09", "406215": "2025-03-23", "406402": "2025-03-30",
    "406601": "2025-04-13", "407225": "2025-04-27", "407559": "2025-05-18",
    "408180": "2025-06-01", "408406": "2025-06-08", "408743": "2025-06-22",
    "409184": "2025-06-29", "409896": "2025-07-20", "410055": "2025-07-27",
    "410845": "2025-08-17", "411533": "2025-09-01", "412098": "2025-09-14",
    "412541": "2025-09-21", "412873": "2025-09-28", "413596": "2025-10-12",
    "414399": "2025-11-02",
    # 2026 TF
    "415431": "2026-03-08", "416022": "2026-03-22", "416579": "2026-04-12",
    "417090": "2026-04-26", "417321": "2026-05-03", "417778": "2026-05-17",
    "418136": "2026-05-31", "418328": "2026-06-07", "418597": "2026-06-14",
    "419295": "2026-06-28", "419894": "2026-07-19",
    "420193": "2026-07-26", "421171": "2026-08-23", "421919": "2026-09-07",
    "423038": "2026-10-04",
    "422463": "2026-09-20", "422774": "2026-09-27", "423626": "2026-10-18", "424121": "2026-11-01",
    # 2024 TF
    "396882": "2024-03-10", "397317": "2024-03-24", "397599": "2024-04-14",
    "397547": "2024-04-07", "398133": "2024-04-28", "398775": "2024-05-19",
    "399291": "2024-06-02", "399534": "2024-06-09", "399957": "2024-06-23",
    "400331": "2024-06-30", "401114": "2024-07-21", "401415": "2024-07-28",
    "401949": "2024-08-18", "402367": "2024-09-02", "402815": "2024-09-15",
    "403284": "2024-09-22", "403508": "2024-09-29", "404189": "2024-10-13",
    "404671": "2024-11-03", "405009": "2024-11-17",
    # 2024 FC
    "396883": "2024-03-10", "397320": "2024-03-24", "397600": "2024-04-14",
    "397546": "2024-04-07", "398134": "2024-04-28", "398774": "2024-05-19",
    "399290": "2024-06-02", "399533": "2024-06-09", "399958": "2024-06-23",
    "400330": "2024-06-30", "401113": "2024-07-21", "401416": "2024-07-28",
    "401948": "2024-08-18", "402366": "2024-09-02", "402814": "2024-09-15",
    "403283": "2024-09-22", "403509": "2024-09-29", "404188": "2024-10-13",
    "404673": "2024-11-03", "405012": "2024-11-17",
    # 2024 PS
    "396880": "2024-03-10", "397315": "2024-03-24", "397601": "2024-04-14",
    "397544": "2024-04-07", "398131": "2024-04-28", "398773": "2024-05-19",
    "399289": "2024-06-02", "399532": "2024-06-09", "399955": "2024-06-23",
    "400329": "2024-06-30", "401112": "2024-07-21", "401414": "2024-07-28",
    "401947": "2024-08-18", "402365": "2024-09-02", "402812": "2024-09-15",
    "403281": "2024-09-22", "403506": "2024-09-29", "404187": "2024-10-13",
    "404670": "2024-11-03", "405010": "2024-11-17",
    # 2024 PM
    "396870": "2024-03-10", "397311": "2024-03-24", "398772": "2024-05-19",
    "399292": "2024-06-02", "399526": "2024-06-09", "399946": "2024-06-23",
    "402354": "2024-09-02", "403272": "2024-09-22", "403500": "2024-09-29",
    "404659": "2024-11-03",
    # 2023 TF
    "387184": "2023-03-12", "387517": "2023-03-26", "387784": "2023-04-02",
    "388064": "2023-04-16", "388740": "2023-04-30", "389020": "2023-05-21",
    "390089": "2023-06-04", "390056": "2023-06-11", "390457": "2023-06-25",
    "391016": "2023-07-16", "391329": "2023-07-23", "391629": "2023-07-30",
    "392235": "2023-08-13", "392460": "2023-08-20", "393205": "2023-09-04",
    "393750": "2023-09-17", "394084": "2023-09-24", "394313": "2023-10-01",
    "395028": "2023-10-15", "395465": "2023-10-29", "395823": "2023-11-12",
    # 2023 FC
    "387185": "2023-03-12", "387516": "2023-03-26", "387783": "2023-04-02",
    "388063": "2023-04-16", "388739": "2023-04-30", "389019": "2023-05-21",
    "390088": "2023-06-04", "390067": "2023-06-11", "390458": "2023-06-25",
    "391004": "2023-07-16", "391328": "2023-07-23", "391628": "2023-07-30",
    "392234": "2023-08-13", "392459": "2023-08-20", "393204": "2023-09-04",
    "393749": "2023-09-17", "394082": "2023-09-24", "394312": "2023-10-01",
    "395027": "2023-10-15", "395464": "2023-10-29", "395822": "2023-11-12",
    # 2023 PS
    "387183": "2023-03-12", "387515": "2023-03-26", "387782": "2023-04-02",
    "388062": "2023-04-16", "388737": "2023-04-30", "389018": "2023-05-21",
    "390066": "2023-06-11", "390455": "2023-06-25", "391014": "2023-07-16",
    "392233": "2023-08-13", "392458": "2023-08-20", "393203": "2023-09-04",
    "393747": "2023-09-17", "394080": "2023-09-24", "394311": "2023-10-01",
    "395026": "2023-10-15", "395463": "2023-10-29", "395821": "2023-11-12",
    # 2023 PM
    "387177": "2023-03-12", "388733": "2023-04-30", "389004": "2023-05-21",
    "390061": "2023-06-11", "390086": "2023-06-04", "390442": "2023-06-25",
    "392446": "2023-08-20", "393201": "2023-09-04", "394307": "2023-10-01",
    "395453": "2023-10-29",
}


def parse_summaries(text):
    """Parse a summary file with multiple ===== RACE_ID=XXXXX ===== blocks.
    Returns a list of dicts: {race_id, round, driver, rt, et, mph, win}.
    """
    rows = []
    blocks = re.split(r"=====\s*RACE_ID=(\d+)\s*=====", text)
    # blocks[0] = preamble, then alternating id, body
    for i in range(1, len(blocks), 2):
        race_id = blocks[i].strip()
        body = blocks[i + 1]
        rows.extend(parse_race_block(race_id, body))
    return rows


# A "result token" looks like (RT) ET MPH e.g. "(0.058) 3.713 338.68"
# RT may be negative like "(-0.046 foul)" or "(0.060)"
# After (RT) we may see ET MPH OR an error/status like "DQ-Centerline", "NT-Broke Before Staging"
RT_RE = re.compile(r"\(\s*(-?\d+\.\d+)(?:\s+\w+)?\s*\)")
TIME_RE = re.compile(r"\(\s*(-?\d+\.\d+)(?:\s+\w+)?\s*\)\s*([0-9.]+|NT-[^,\n]+|DQ-[^,\n]+)\s*([0-9.]+)?")


def _parse_perf_segment(seg):
    """Given a string like '(0.058) 3.713 338.68 def. Tony Stewart, ...'
    or 'Tony Stewart, [origin], [car], Left lane, (0.058) 3.713 338.68'
    Extract RT, ET, MPH from the first time block.
    Returns (rt, et, mph) or None if no valid RT.
    """
    m = TIME_RE.search(seg)
    if not m:
        return None
    rt_str = m.group(1)
    perf = m.group(2).strip()
    speed = m.group(3)
    try:
        rt = float(rt_str)
    except Exception:
        return None
    et = 0.0
    mph = 0.0
    if perf and re.match(r"^[0-9.]+$", perf):
        try:
            et = float(perf)
        except Exception:
            et = 0.0
        if speed:
            try:
                mph = float(speed)
            except Exception:
                mph = 0.0
    return rt, et, mph


# Driver name pattern at start of a winner segment:
#   "John Smith, City ST, '## Car, Left lane, (rt) et mph def. ..."
# Or short form for later rounds:
#   "J Smith, Left lane, (rt) et mph def. ..."
DRIVER_HEAD_RE = re.compile(
    r"^\s*"
    r"(?P<name>[A-Za-z][A-Za-z.\-'\s]+?(?:Jr\.|III|II)?)"
    r"(?:,\s*[A-Za-z][A-Za-z. \-]+\s+[A-Z]{2})?"      # optional City ST
    r"(?:,\s*'\d{2}\s+[\w\- ]+?)?"                       # optional '## Car
    r"(?:,\s*(?:Left lane|Right lane|Lane\s*\d))?"      # optional lane
    r"(?:,\s*)?\("
)


def _parse_driver(seg):
    """Pull driver name from the start of a winner/loser segment.
    Returns name string or None.
    """
    m = DRIVER_HEAD_RE.match(seg)
    if not m:
        # Try a looser match: take everything up to the first '('
        idx = seg.find("(")
        if idx < 0:
            return None
        prefix = seg[:idx]
        # Strip 'Lane X,' or 'Left lane,' or 'Right lane,' etc.
        parts = [p.strip() for p in prefix.split(",")]
        # The first non-lane, non-empty piece is usually the name
        name = parts[0].strip() if parts else None
        if name:
            return name
        return None
    return m.group("name").strip()


def parse_race_block(race_id, body):
    """Parse one race summary into list of run rows.
    Each row also gets an "opps" field — the list of opponent driver names in
    that pair/quad. This makes head-to-head matching trivial later.
    """
    rows = []

    round_chunks = re.split(r"\bRound\s+(\d+)\s*:", body)
    for i in range(1, len(round_chunks), 2):
        rnd = int(round_chunks[i])
        chunk = round_chunks[i + 1]
        chunk = re.split(r"\n\s*Low ET:|\n\s*Top Speed:|Timing data courtesy of", chunk)[0]
        pairings = [p.strip() for p in re.split(r"\n\s*\n|;\s*\n?", chunk) if p.strip()]

        for p in pairings:
            if "def." not in p and "was unopposed" not in p and "def " not in p:
                continue

            if "was unopposed" in p:
                segs = [p.split("was unopposed")[0]]
                pair_rows = _extract_runs(race_id, rnd, segs, [True])
                for r in pair_rows:
                    r["opps"] = []  # solo run, no opponent
                rows.extend(pair_rows)
                continue

            m = re.search(r"\s*def\.\s+", p)
            if not m:
                continue
            wpart = p[: m.start()]
            lpart = p[m.end():]

            win_segs = _split_and_pairs(wpart)
            lose_segs = _split_and_pairs(lpart)

            winners = _extract_runs(race_id, rnd, win_segs, [True] * len(win_segs))
            losers = _extract_runs(race_id, rnd, lose_segs, [False] * len(lose_segs))

            # All drivers in this pairing — every entry knows everyone else they raced.
            all_drivers = [r["driver"] for r in winners + losers]
            for r in winners + losers:
                r["opps"] = [d for d in all_drivers if d != r["driver"]]

            rows.extend(winners)
            rows.extend(losers)

    return rows


# In 4-Wide, two winners are joined by " and " between full driver segments.
# Each driver segment starts with a capitalized name token. To be safe, split on
# " and " ONLY when the following text contains a "(rt) et mph" or "NT-"/"DQ-" performance
# block — that uniquely identifies the start of a new driver segment.
AND_SPLIT_RE = re.compile(r"\s+and\s+(?=[A-Z][A-Za-z'.]*(?:[\s.\-][A-Z][A-Za-z'.]*)*,)")


def _split_and_pairs(segment):
    """Split a possibly-multi-driver segment on ' and ' boundaries.
    Returns list of single-driver sub-segments.
    """
    parts = AND_SPLIT_RE.split(segment)
    return [p.strip() for p in parts if p.strip()]


def _extract_runs(race_id, rnd, segs, wins):
    """For each segment, extract (driver, rt, et, mph) and append to output."""
    out = []
    for seg, win in zip(segs, wins):
        name = _parse_driver(seg)
        perf = _parse_perf_segment(seg)
        if not name or not perf:
            continue
        # Collapse soft-wrap newlines/extra spaces so a driver is not split into
        # two identities ("Mike\n Castellana" vs "Mike Castellana").
        name = re.sub(r"\s+", " ", name).strip()
        rt, et, mph = perf
        out.append(
            {
                "race_id": race_id,
                "round": rnd,
                "driver": name,
                "rt": rt,
                "et": et,
                "mph": mph,
                "win": bool(win),
            }
        )
    return out


# Some drivers appear by initial-only in later rounds (e.g. "J Beckman").
# Resolve to full name using the round-1 mapping (per-race).
def resolve_initials(rows):
    """Map 'X Lastname' shorthand to round-1 full name within the same race."""
    by_race = {}
    for r in rows:
        by_race.setdefault(r["race_id"], []).append(r)
    for race_id, rs in by_race.items():
        # Build {initial+last: full_name} from rows where driver is "Firstname Lastname" form
        full_map = {}
        for r in rs:
            n = r["driver"]
            # If looks like "First Last" or "First M Last" etc.
            if " " in n and len(n.split()[0]) > 1 and not n.startswith("'"):
                last = n.split()[-1].rstrip(",.")
                first = n.split()[0]
                key = f"{first[0]} {last}"
                full_map.setdefault(key, n)
                # Also handle "J.R. Todd"  -> "J Todd"
                # Already covered by first letter of "J.R."
        for r in rs:
            n = r["driver"]
            # Match shorthand "X Lastname" pattern (single letter + space + word, perhaps with periods/dots)
            if re.match(r"^[A-Z]\s+[A-Z]", n) or re.match(r"^[A-Z]\.?[A-Z]?\.?\s+[A-Z]", n):
                key = f"{n[0]} {n.split()[-1].rstrip(',.')}"
                full = full_map.get(key)
                if full:
                    r["driver"] = full
    return rows


def _resolve_opps(runs):
    """Resolve opponent initials ("J Beckman") to full names within each race."""
    by_race = {}
    for r in runs:
        by_race.setdefault(r["race_id"], []).append(r)
    for race_id, rs in by_race.items():
        full_map = {}
        for r in rs:
            n = r["driver"]
            if " " in n and len(n.split()[0]) > 1 and not n.startswith("'"):
                last = n.split()[-1].rstrip(",.")
                first = n.split()[0]
                key = f"{first[0]} {last}"
                full_map.setdefault(key, n)
        for r in rs:
            resolved = []
            for opp in r.get("opps", []):
                if re.match(r"^[A-Z]\s+[A-Z]", opp) or re.match(r"^[A-Z]\.?[A-Z]?\.?\s+[A-Z]", opp):
                    key = f"{opp[0]} {opp.split()[-1].rstrip(',.')}"
                    resolved.append(full_map.get(key, opp))
                else:
                    resolved.append(opp)
            r["opps"] = resolved


def _years_for_class(class_code):
    """Every year with a <year>_<class>_summaries.txt file (generic, no hardcoding)."""
    years = []
    for fp in RAW.glob(f"*_{class_code}_summaries.txt"):
        m = re.match(r"(\d{4})_", fp.name)
        if m:
            years.append(int(m.group(1)))
    return sorted(set(years))


def parse_class_files(class_code):
    """Parse every year's summary file for one class and return run rows with
    year/race/class metadata attached, opponent initials resolved."""
    out = []
    for year in _years_for_class(class_code):
        fpath = RAW / f"{year}_{class_code}_summaries.txt"
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding="utf-8")
        runs = parse_summaries(text)
        runs = resolve_initials(runs)
        _resolve_opps(runs)
        for r in runs:
            race_name = RACE_NAMES.get(r["race_id"], r["race_id"])
            date = RACE_DATES.get(r["race_id"], "")
            out.append(
                {
                    "class": class_code,
                    "race": race_name,
                    "year": year,
                    "round": r["round"],
                    "driver": r["driver"],
                    "rt": r["rt"],
                    "et": r["et"],
                    "mph": r["mph"],
                    "win": r["win"],
                    "race_id": r["race_id"],
                    "date": date,
                    "opps": r.get("opps", []),
                }
            )
    return out


def parse_discovered():
    """Parse auto-discovered stories (raw_data/stories/<id>.txt) using the
    class/race/year/date recorded in raw_data/discovered.json by drc_discover.py.
    Returns run rows in the same shape as parse_class_files. Any (class,race,year)
    already present in the hand-built tables is skipped so history is never
    double-counted."""
    index = RAW / "discovered.json"
    if not index.exists():
        return []
    idx = json.loads(index.read_text())
    # (race_id already in the legacy tables) -> don't re-ingest
    legacy_ids = set(RACE_NAMES) | set(RACE_DATES)
    out = []
    for sid, meta in sorted(idx.get("stories", {}).items()):
        if meta.get("status") != "ingested" or sid in legacy_ids:
            continue
        body_path = RAW / "stories" / f"{sid}.txt"
        if not body_path.exists():
            continue
        wrapped = f"===== RACE_ID={sid} =====\n{body_path.read_text(encoding='utf-8')}\n"
        runs = parse_summaries(wrapped)
        runs = resolve_initials(runs)
        _resolve_opps(runs)
        for r in runs:
            out.append(
                {
                    "class": meta["class"],
                    "race": meta["race"],
                    "year": int(meta["year"]),
                    "round": r["round"],
                    "driver": r["driver"],
                    "rt": r["rt"],
                    "et": r["et"],
                    "mph": r["mph"],
                    "win": r["win"],
                    "race_id": sid,
                    "date": meta.get("date", ""),
                    "opps": r.get("opps", []),
                }
            )
    return out


def write_class_csv(class_code, rows):
    """Write per-class per-year CSVs in the existing TF format
    (race,round,driver,rt,et,mph,win)."""
    for year in sorted({r["year"] for r in rows if r["class"] == class_code}):
        yr_rows = [r for r in rows if r["year"] == year and r["class"] == class_code]
        if not yr_rows:
            continue
        out_path = ROOT / f"{year}_{class_code}_runs.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["race", "round", "driver", "rt", "et", "mph", "win"])
            for r in yr_rows:
                w.writerow([r["race"], r["round"], r["driver"], r["rt"], r["et"], r["mph"], r["win"]])
        print(f"Wrote {out_path} ({len(yr_rows)} runs)")


# Map TF race names from the existing CSV (different conventions used during
# Vol. 1 build) to canonical names that match FC/PS/PM. This is the source of
# the missing Route 66 date.
TF_NAME_TO_CANONICAL = {
    "4-Wide Charlotte": "4-Wide Carolina",
    "4-Wide Vegas": "4-Wide Nationals",
    "Carolina 4-Wide": "Carolina 4-Wide Nationals",
    "Lucas Oil Brainerd": "Lucas Oil Nationals",
    "Midwest": "Midwest Nationals",
    "Nevada": "Nevada Nationals",
    "New England": "New England Nationals",
    "Northwest": "Northwest Nationals",
    "Norwalk": "Summit Racing Nationals",
    "Reading": "Reading Nationals",
    "Route 66 2025": "Route 66",
    "Route 66 Nationals": "Route 66",
    "Sonoma": "Sonoma Nationals",
    "Thunder Valley": "Thunder Valley Nationals",
    "Virginia": "Virginia Nationals",
}


def load_existing_tf_runs():
    """Read existing TF CSVs and return rows in master format.
    Normalizes race names to match FC/PS/PM convention so dates resolve.
    """
    rows = []
    for year in (2023, 2024, 2025, 2026):
        fpath = ROOT / f"{year}_TF_runs.csv"
        if not fpath.exists():
            continue
        with open(fpath, encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                canonical = TF_NAME_TO_CANONICAL.get(row["race"], row["race"])
                rows.append(
                    {
                        "class": "TF",
                        "race": canonical,
                        "year": year,
                        "round": int(row["round"]),
                        "driver": row["driver"],
                        "rt": float(row["rt"]),
                        "et": float(row["et"]),
                        "mph": float(row["mph"]),
                        "win": row["win"].strip().lower() == "true",
                    }
                )
    return rows


def write_master(rows):
    out_path = ROOT / "master_runs.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["class", "race", "year", "round", "driver", "rt", "et", "mph", "win", "opps"])
        for r in rows:
            opps = "|".join(r.get("opps", []))
            w.writerow([
                r["class"], r["race"], r["year"], r["round"], r["driver"],
                r["rt"], r["et"], r["mph"], r["win"], opps,
            ])
    print(f"Wrote {out_path} ({len(rows)} runs total)")


def write_races(rows):
    """Write races.csv lookup table."""
    out_path = ROOT / "races.csv"
    races = {}
    for r in rows:
        if "race_id" not in r:
            continue
        key = r["race_id"]
        if key not in races:
            races[key] = {
                "race_id": key,
                "race_name": r["race"],
                "year": r["year"],
                "date": r.get("date", ""),
                "classes": set(),
            }
        races[key]["classes"].add(r["class"])
    # Also synthesize TF rows from race name → race_id mapping (we don't have race_ids in master TF csv)
    rows_out = []
    for rid, meta in sorted(races.items()):
        rows_out.append({
            "race_id": rid,
            "race_name": meta["race_name"],
            "year": meta["year"],
            "date": meta["date"],
            "classes": "|".join(sorted(meta["classes"])),
        })
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["race_id", "race_name", "year", "date", "classes"])
        for r in rows_out:
            w.writerow([r["race_id"], r["race_name"], r["year"], r["date"], r["classes"]])
    print(f"Wrote {out_path} ({len(rows_out)} races)")


def main():
    tf_rows = parse_class_files("TF")
    fc_rows = parse_class_files("FC")
    ps_rows = parse_class_files("PS")
    pm_rows = parse_class_files("PM")

    all_rows = tf_rows + fc_rows + ps_rows + pm_rows
    # Auto-discovered stories (new races scraped by drc_discover.py)
    discovered = parse_discovered()
    if discovered:
        print(f"Discovered stories added: {len(discovered)} runs")
        all_rows += discovered

    for code in ("TF", "FC", "PS", "PM"):
        write_class_csv(code, all_rows)

    write_master(all_rows)
    write_races(all_rows)

    # Print quick summary
    summary = {}
    for r in all_rows:
        key = (r["class"], r["year"])
        summary[key] = summary.get(key, 0) + 1
    print("\nRun counts by class/year:")
    for k in sorted(summary):
        print(f"  {k[0]} {k[1]}: {summary[k]} runs")
    print(f"\nGrand total: {sum(summary.values())} runs")


if __name__ == "__main__":
    main()
