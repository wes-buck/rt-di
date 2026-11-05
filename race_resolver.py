"""Map DragRaceCentral event names / cities to RT.DI canonical race names.

DRC event strings carry year-to-year sponsors and ordinals, e.g.
"26th annual MOPAR NHRA Las Vegas Nationals powered by Dodge". The canonical
names are the stable labels the site uses, e.g. "Nevada Nationals".

Resolution order (first hit wins):
  1. a distinctive keyword in the event name (most reliable for uniquely named races)
  2. the article city, disambiguated by month where a city hosts two events

Anything unresolved falls back to a cleaned event name and is reported, so data
still flows hands-off while a new/renamed event is easy to pin down in NAME_KEYWORDS
or CITY_RULES below. This file is config: editing these tables is not a per-race
manual edit of story IDs or dates.
"""
import re

# ---- 1. Distinctive event-name keywords -> canonical name --------------------
# Checked against the UPPERCASED event name. Order matters: more specific first.
NAME_KEYWORDS = [
    ("GATORNATIONALS", "Gatornationals"),
    ("WINTERNATIONALS", "Winternationals"),
    ("FALLNATIONALS", "FallNationals"),
    ("FALL NATIONALS", "FallNationals"),
    ("ARIZONA", "Arizona Nationals"),
    ("ROUTE 66", "Route 66"),
    ("SOUTHERN NATIONALS", "Southern Nationals"),
    ("NEW ENGLAND", "New England Nationals"),
    ("THUNDER VALLEY", "Thunder Valley Nationals"),
    ("VIRGINIA", "Virginia Nationals"),
    ("NORTHWEST", "Northwest Nationals"),
    ("SONOMA", "Sonoma Nationals"),
    ("MILE-HIGH", "Mile-High Nationals"),
    ("MILE HIGH", "Mile-High Nationals"),
    ("HEARTLAND", "Heartland Nationals"),
    ("U.S. NATIONALS", "US Nationals"),
    ("US NATIONALS", "US Nationals"),
    ("MIDWEST", "Midwest Nationals"),
    ("GREAT LAKES", "Great Lakes Nationals"),
    ("POTOMAC", "Potomac Nationals"),
    ("SUMMIT", "Summit Racing Nationals"),
    ("NATIONALS AT THE ROCK", "Nationals at The Rock"),
    ("NEVADA NATIONALS", "Nevada Nationals"),
]

# ---- 2. City -> canonical name (month-disambiguated where needed) ------------
# Keys are UPPERCASED cities as they appear at the head of a DRC summary
# ("LAS VEGAS - Summary..." / "GAINESVILLE, Fla. - Summary..."). A value is
# either a plain canonical name, or a list of (months, name) rules tried in order
# (months is a set of two-digit month strings; the last rule may use months=None
# as a catch-all).
CITY_RULES = {
    "GAINESVILLE": "Gatornationals",
    "PHOENIX": "Arizona Nationals",
    "CHANDLER": "Arizona Nationals",
    "POMONA": [({"03", "04", "02"}, "Winternationals"), (None, "Finals")],
    "LAS VEGAS": [({"03", "04", "05"}, "4-Wide Nationals"), (None, "Nevada Nationals")],
    "CHARLOTTE": [({"03", "04", "05"}, "4-Wide Carolina"), (None, "Carolina Nationals")],
    "CONCORD": [({"03", "04", "05"}, "4-Wide Carolina"), (None, "Carolina Nationals")],
    "CHICAGO": "Route 66",
    "JOLIET": "Route 66",
    "EPPING": "New England Nationals",
    "BRISTOL": "Thunder Valley Nationals",
    "RICHMOND": "Virginia Nationals",
    "DINWIDDIE": "Virginia Nationals",
    "NORWALK": "Summit Racing Nationals",
    "DENVER": "Mile-High Nationals",
    "MORRISON": "Mile-High Nationals",
    "SEATTLE": "Northwest Nationals",
    "KENT": "Northwest Nationals",
    "SONOMA": "Sonoma Nationals",
    "TOPEKA": "Heartland Nationals",
    "BRAINERD": "Lucas Oil Nationals",
    "INDIANAPOLIS": "US Nationals",
    "INDY": "US Nationals",
    "CLERMONT": "US Nationals",
    "READING": "Reading Nationals",
    "MOHNTON": "Reading Nationals",
    "ST. LOUIS": "Midwest Nationals",
    "ST LOUIS": "Midwest Nationals",
    "MADISON": "Midwest Nationals",
    "DALLAS": "FallNationals",
    "ENNIS": "FallNationals",
    "VALDOSTA": "Southern Nationals",
    "COMMERCE": "Southern Nationals",
    "BUDDS CREEK": "Potomac Nationals",
    "MARTIN": "Great Lakes Nationals",
    "ROCKINGHAM": "Nationals at The Rock",
}

_ORDINAL = re.compile(r"\b\d{1,3}(ST|ND|RD|TH)\b")
_NOISE = re.compile(
    r"\b(ANNUAL|NHRA|MISSION FOODS|DRAG RACING SERIES|POWERED BY .*|PRESENTED BY .*|"
    r"MOPAR|AMALIE MOTOR OIL|DODGE)\b"
)


def _clean(event_name):
    s = (event_name or "").upper()
    s = _ORDINAL.sub(" ", s)
    s = _NOISE.sub(" ", s)
    s = re.sub(r"[^A-Z0-9 .-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .-")
    return s


def resolve(event_name, city, month):
    """Return (canonical_name, confident). `month` is a '01'..'12' string or ''.
    confident is False when we fell back to a cleaned name (worth reporting)."""
    name_u = (event_name or "").upper()
    for kw, canon in NAME_KEYWORDS:
        if kw in name_u:
            return canon, True

    city_u = (city or "").upper().strip()
    rule = CITY_RULES.get(city_u)
    if rule is None:
        # try a looser city match (strip trailing tokens like "1"/"2")
        base = re.sub(r"\s+\d+$", "", city_u)
        rule = CITY_RULES.get(base)
    if isinstance(rule, str):
        return rule, True
    if isinstance(rule, list):
        for months, canon in rule:
            if months is None or (month and month in months):
                return canon, True

    # Fallback: cleaned event name (Title Case), flagged as not confident.
    cleaned = _clean(event_name)
    if cleaned:
        pretty = " ".join(
            w if re.match(r"^[0-9]", w) else w.capitalize() for w in cleaned.split()
        )
        return pretty, False
    return (city or "Unknown Event").title(), False
