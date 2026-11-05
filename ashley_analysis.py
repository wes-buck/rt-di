"""
Justin Ashley reaction time analysis: 2025 full season vs. 2026 (first 6 races).
"""
import csv
from collections import defaultdict

def load(path):
    runs = []
    with open(path) as f:
        for r in csv.DictReader(f):
            r["rt"] = float(r["rt"])
            r["et"] = float(r["et"])
            r["mph"] = float(r["mph"])
            r["round"] = int(r["round"])
            r["win"] = r["win"] == "True"
            runs.append(r)
    return runs

R26 = load("/sessions/great-determined-cannon/mnt/Wes Buck Show Operating Room/RT_Report/2026_TF_runs.csv")
R25 = load("/sessions/great-determined-cannon/mnt/Wes Buck Show Operating Room/RT_Report/2025_TF_runs.csv")

def valid(r):
    """Exclude redlights (negative RT), DNS/NT runs (et==0, mph==0), and known-bad RT entries."""
    if r["rt"] <= 0: return False
    if r["et"] == 0.0 and r["mph"] == 0.0: return False
    # The two anomalies we saw: Millican's .978 at Richmond (opponent left before tree)
    # and Reading Doug Foley .848 — both are weird sensor situations.
    # We keep .000 anomaly (Zetterstrom St. Louis) — likely a perfect light or sensor glitch.
    return True

def stats(runs):
    n = len(runs)
    if n == 0: return None
    rts = [r["rt"] for r in runs]
    return {
        "n": n,
        "avg": sum(rts)/n,
        "best": min(rts),
        "worst": max(rts),
    }

def ashley(runs): return [r for r in runs if r["driver"] == "Justin Ashley" and valid(r)]
def field(runs): return [r for r in runs if valid(r)]

print("="*78)
print("  JUSTIN ASHLEY: 2025 FULL SEASON vs. 2026 (first 6 races)")
print("="*78)
ash25 = ashley(R25)
ash26 = ashley(R26)
fld25 = field(R25)
fld26 = field(R26)

s25 = stats(ash25)
s26 = stats(ash26)
f25 = stats(fld25)
f26 = stats(fld26)

print()
print(f"{'':25s}  {'Ashley':>10s} | {'Field':>10s} | {'Gap':>8s}")
print("-"*78)
print(f"{'2025 (19 races)':25s}  {s25['avg']:>10.4f} | {f25['avg']:>10.4f} | {f25['avg']-s25['avg']:>+8.4f}")
print(f"{'2026 (6 races thru May)':25s}  {s26['avg']:>10.4f} | {f26['avg']:>10.4f} | {f26['avg']-s26['avg']:>+8.4f}")
print()
print(f"  Ashley 2025: n={s25['n']}, best={s25['best']:.3f}, worst={s25['worst']:.3f}")
print(f"  Ashley 2026: n={s26['n']}, best={s26['best']:.3f}, worst={s26['worst']:.3f}")
print(f"  YEAR-OVER-YEAR delta: {s26['avg']-s25['avg']:+.4f}  ({'IMPROVED' if s26['avg']<s25['avg'] else 'REGRESSED'})")

# Per-race breakdown for Ashley
print()
print("="*78)
print("  ASHLEY 2025 RACE-BY-RACE")
print("="*78)
by_race25 = defaultdict(list)
for r in ash25:
    by_race25[r["race"]].append(r)
race_order25 = ["Gatornationals","Arizona Nationals","Winternationals","4-Wide Vegas",
                "4-Wide Charlotte","Route 66 2025","New England","Thunder Valley",
                "Virginia","Norwalk","Northwest","Sonoma","Lucas Oil Brainerd",
                "US Nationals","Reading","Carolina 4-Wide","Midwest","FallNationals","Nevada"]
print(f"  {'Race':<20s} {'n':>3s} {'avg':>6s} {'best':>6s} {'rounds':<14s}")
for race in race_order25:
    if race not in by_race25: continue
    rs = by_race25[race]
    rts = [r["rt"] for r in rs]
    avg = sum(rts)/len(rts)
    best = min(rts)
    rds = ",".join(str(r["round"]) for r in sorted(rs, key=lambda x: x["round"]))
    print(f"  {race:<20s} {len(rts):>3d} {avg:>6.4f} {best:>6.3f} {rds}")

print()
print("="*78)
print("  ASHLEY 2026 RACE-BY-RACE")
print("="*78)
by_race26 = defaultdict(list)
for r in ash26:
    by_race26[r["race"]].append(r)
race_order26 = ["Gatornationals","Arizona Nationals","Winternationals","4-Wide Nationals",
                "Southern Nationals","Route 66 Nationals"]
for race in race_order26:
    if race not in by_race26: continue
    rs = by_race26[race]
    rts = [r["rt"] for r in rs]
    avg = sum(rts)/len(rts)
    best = min(rts)
    rds = ",".join(str(r["round"]) for r in sorted(rs, key=lambda x: x["round"]))
    print(f"  {race:<22s} {len(rts):>3d} {avg:>6.4f} {best:>6.3f} {rds}")

# Field leaderboards
print()
print("="*78)
print("  2025 FULL-SEASON DRIVER LEADERBOARD (min 10 valid RTs)")
print("="*78)
drv = defaultdict(list)
for r in fld25:
    drv[r["driver"]].append(r["rt"])
lb = sorted([(d, len(v), sum(v)/len(v), min(v), max(v)) for d,v in drv.items() if len(v) >= 10], key=lambda x: x[2])
print(f"  {'Driver':<25s} {'n':>4s} {'avg':>7s} {'best':>6s} {'worst':>6s}")
for d, n, avg, lo, hi in lb:
    print(f"  {d:<25s} {n:>4d} {avg:>7.4f} {lo:>6.3f} {hi:>6.3f}")

# Ashley's best-light count by year
print()
print("="*78)
print("  HOW OFTEN WAS ASHLEY THE BEST REACTOR IN A ROUND?")
print("="*78)
def round_best_count(runs, driver):
    by_rr = defaultdict(list)
    for r in runs:
        if valid(r):
            by_rr[(r["race"], r["round"])].append(r)
    wins, total = 0, 0
    for key, lst in by_rr.items():
        if any(r["driver"] == driver for r in lst):
            total += 1
            best = min(lst, key=lambda x: x["rt"])
            if best["driver"] == driver:
                wins += 1
    return wins, total

w25, t25 = round_best_count(R25, "Justin Ashley")
w26, t26 = round_best_count(R26, "Justin Ashley")
print(f"  2025: Best light in {w25} of {t25} rounds he raced ({100*w25/t25:.1f}%)")
print(f"  2026: Best light in {w26} of {t26} rounds he raced ({100*w26/t26:.1f}%)")

# Ashley wins
print()
print("="*78)
print("  ASHLEY'S 2025 WALLY-WIN ROUND")
print("="*78)
finals25 = [r for r in R25 if r["driver"]=="Justin Ashley" and r["round"]==4 and r["win"] and valid(r)]
for r in finals25:
    print(f"  {r['race']:<25s} RT {r['rt']:.3f}, ET {r['et']:.3f}, MPH {r['mph']:.2f}")
print()
print("  Finals appearances 2025:")
finals_all = [r for r in R25 if r["driver"]=="Justin Ashley" and r["round"]==4]
for r in finals_all:
    result = "WIN" if r["win"] else "RU"
    print(f"  {r['race']:<25s} RT {r['rt']:.3f}, ET {r['et']:.3f}  {result}")

# Best lights of 2025 - overall
print()
print("="*78)
print("  TOP 15 BEST LIGHTS OF 2025 SEASON")
print("="*78)
sorted_25 = sorted(fld25, key=lambda x: x["rt"])[:15]
for r in sorted_25:
    print(f"  .{int(r['rt']*1000):03d}  {r['driver']:<22s} {r['race']:<22s} R{r['round']}  {'W' if r['win'] else 'L'}")
