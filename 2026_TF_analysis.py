"""
2026 Top Fuel Reaction Time Analysis — six races, March-May 2026.
"""
import csv
from collections import defaultdict

CSV_PATH = "/sessions/great-determined-cannon/mnt/Wes Buck Show Operating Room/RT_Report/2026_TF_runs.csv"

runs = []
with open(CSV_PATH) as f:
    for r in csv.DictReader(f):
        r["rt"] = float(r["rt"])
        r["et"] = float(r["et"])
        r["mph"] = float(r["mph"])
        r["round"] = int(r["round"])
        r["win"] = r["win"] == "True"
        runs.append(r)

# Valid RTs: positive (no redlights or NT placeholders), and we'll keep redlights as a separate count
valid_rts = [r["rt"] for r in runs if r["rt"] > 0 and not (r["et"] == 0.0 and r["mph"] == 0.0)]
redlights = [r for r in runs if r["rt"] < 0]
nt_runs   = [r for r in runs if r["et"] == 0.0 and r["mph"] == 0.0]

print("="*70)
print("  2026 NHRA TOP FUEL — SEASON RT ANALYSIS (First 6 races)")
print("="*70)
print(f"Total run records:     {len(runs)}")
print(f"Valid RTs in pool:     {len(valid_rts)}")
print(f"Redlight fouls:        {len(redlights)}")
print(f"NT (broke/no-show):    {len(nt_runs)}")
print()
print(f"SEASON FIELD AVG RT:   {sum(valid_rts)/len(valid_rts):.4f}")
print(f"Best light:            {min(valid_rts):.3f}")
print(f"Worst light:           {max(valid_rts):.3f}")
print()

# Per-race summary
print("="*70)
print("  RACE-BY-RACE")
print("="*70)
race_order = ["Gatornationals","Arizona Nationals","Winternationals",
              "4-Wide Nationals","Southern Nationals","Route 66 Nationals"]
header = f"{'Race':<22} {'n':>4} {'avg':>7} {'best':>6} {'worst':>6}  Winner"
print(header); print("-"*70)
for race in race_order:
    race_rts = [r["rt"] for r in runs if r["race"]==race and r["rt"]>0 and not (r["et"]==0 and r["mph"]==0)]
    winners_in_round4 = [r["driver"] for r in runs if r["race"]==race and r["round"]==4 and r["win"]]
    winner = winners_in_round4[0] if winners_in_round4 else "(4-wide)"
    avg = sum(race_rts)/len(race_rts)
    print(f"{race:<22} {len(race_rts):>4d} {avg:>7.4f} {min(race_rts):>6.3f} {max(race_rts):>6.3f}  {winner}")

# Driver leaderboards
print()
print("="*70)
print("  DRIVER SEASON AVERAGES (min 4 runs)")
print("="*70)
driver_rts = defaultdict(list)
for r in runs:
    if r["rt"] > 0 and not (r["et"]==0 and r["mph"]==0):
        driver_rts[r["driver"]].append(r["rt"])

leaderboard = []
for driver, rts in driver_rts.items():
    if len(rts) >= 4:
        leaderboard.append((driver, len(rts), sum(rts)/len(rts), min(rts), max(rts)))

print(f"{'Driver':<22} {'n':>4} {'avg':>7} {'best':>6} {'worst':>6}")
print("-"*52)
for d, n, avg, lo, hi in sorted(leaderboard, key=lambda x: x[2]):
    print(f"{d:<22} {n:>4d} {avg:>7.4f} {lo:>6.3f} {hi:>6.3f}")

# Win-correlation: do better-reacting drivers actually win?
print()
print("="*70)
print("  WIN CORRELATION — head-to-head RT comparison")
print("="*70)
# Group by race+round+et-pair (proxy for pairing). Use simpler approach:
# For each round in each race, sort runs by win, but in 4-wide it's messy.
# Easier: in 2-wide races, pair up by adjacency in source order.
pairs = []
for race in race_order:
    if race == "4-Wide Nationals":  # skip 4-wide for clean head-to-head
        continue
    race_runs = [r for r in runs if r["race"]==race]
    # group by round
    by_round = defaultdict(list)
    for r in race_runs:
        by_round[r["round"]].append(r)
    for rnd, lst in by_round.items():
        # Walk through pairs in source order (winner first, loser second per DRC summary structure)
        # Filter unopposed runs (single winner with no opponent record); pairs are consecutive
        i = 0
        while i < len(lst):
            if i+1 < len(lst) and lst[i]["win"] and not lst[i+1]["win"]:
                pairs.append((lst[i], lst[i+1]))
                i += 2
            else:
                # likely unopposed
                i += 1

# Filter pairs where both have valid RTs
clean = [(a,b) for a,b in pairs if a["rt"]>0 and b["rt"]>0 and not (b["et"]==0 and b["mph"]==0)]
better_rt_won = sum(1 for a,b in clean if a["rt"] < b["rt"])
worse_rt_won  = sum(1 for a,b in clean if a["rt"] > b["rt"])
tie           = sum(1 for a,b in clean if a["rt"] == b["rt"])

print(f"Clean pairs analyzed:  {len(clean)} (excludes 4-Wide + unopposed + NT)")
print(f"Better-RT driver won:  {better_rt_won}  ({100*better_rt_won/len(clean):.1f}%)")
print(f"Worse-RT driver won:   {worse_rt_won}  ({100*worse_rt_won/len(clean):.1f}%)")
print(f"Tied:                  {tie}")
print()
print("Translation: in 2026 Top Fuel head-to-head, the driver with the")
print("better light won only %d%% of the time. The car wins races." % (100*better_rt_won/len(clean)))
print()

# Top-5 best lights of the season
print("="*70)
print("  TOP 10 BEST LIGHTS OF THE SEASON")
print("="*70)
valid_runs = [r for r in runs if r["rt"] > 0 and not (r["et"]==0 and r["mph"]==0)]
for r in sorted(valid_runs, key=lambda x: x["rt"])[:10]:
    print(f"  .{int(r['rt']*1000):03d}  {r['driver']:<22} {r['race']:<22} R{r['round']}  {'W' if r['win'] else 'L'}")

print()
print("="*70)
print("  REDLIGHT FOULS")
print("="*70)
for r in redlights:
    print(f"  {r['rt']:+.3f}  {r['driver']:<22} {r['race']:<22} R{r['round']}")
