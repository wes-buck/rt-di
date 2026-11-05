"""
2026 NHRA Top Fuel — full eliminations dataset across all 6 races run through May 17, 2026.
Source: dragracecentral.com 'Summary of Eliminations' reports.
"""

# Each run is a dict: {race, round, driver, rt, et, mph, win}
# rt < 0 = redlight foul. NT entries (broke/no-show) excluded from RT averages but kept in dataset.

DATA = []

def add(race, rnd, driver, rt, et, mph, win):
    DATA.append({"race": race, "round": rnd, "driver": driver, "rt": rt, "et": et, "mph": mph, "win": win})

# ============================================================
# RACE 1: GATORNATIONALS (Gainesville) - Mar 5-8 - Hart won
# ============================================================
R = "Gatornationals"
# Round 1
add(R, 1, "Tony Stewart",       0.058, 3.713, 338.68, True)
add(R, 1, "Clay Millican",      0.081, 7.811, 80.19,  False)
add(R, 1, "Leah Pruett",        0.089, 3.713, 333.41, True)
add(R, 1, "Jasmine Salinas",    0.098, 8.765, 77.77,  False)
add(R, 1, "Maddi Gordon",       0.094, 3.762, 334.48, True)
add(R, 1, "Shawn Langdon",      0.065, 4.494, 190.81, False)
add(R, 1, "Josh Hart",          0.087, 3.751, 335.65, True)
add(R, 1, "Dan Mercier",        0.110, 5.107, 143.08, False)
add(R, 1, "Antron Brown",       0.054, 3.764, 331.20, True)
add(R, 1, "Gary Pritchett",     0.059, 5.778, 111.73, False)
add(R, 1, "Doug Kalitta",       0.056, 4.338, 237.96, True)
add(R, 1, "Justin Ashley",      0.026, 4.586, 221.27, False)
add(R, 1, "Tony Schumacher",    0.096, 4.182, 260.86, True)
add(R, 1, "Shawn Reed",         0.073, 4.684, 158.99, False)
add(R, 1, "Tripp Tatum",        0.034, 4.563, 234.33, True)
add(R, 1, "Billy Torrence",     0.107, 4.603, 197.39, False)
# Round 2
add(R, 2, "Maddi Gordon",       0.107, 3.783, 331.53, True)
add(R, 2, "Tony Schumacher",    0.077, 3.863, 298.87, False)
add(R, 2, "Antron Brown",       0.041, 3.821, 327.82, True)
add(R, 2, "Tony Stewart",       0.056, 3.813, 332.10, False)
add(R, 2, "Doug Kalitta",       0.062, 3.764, 332.34, True)
add(R, 2, "Leah Pruett",        0.093, 3.871, 318.47, False)
add(R, 2, "Josh Hart",          0.081, 3.845, 334.57, True)
add(R, 2, "Tripp Tatum",       -0.098, 3.796, 323.27, False)   # redlight foul
# Round 3
add(R, 3, "Josh Hart",          0.095, 4.488, 289.51, True)
add(R, 3, "Antron Brown",       0.053, 4.552, 246.93, False)
add(R, 3, "Doug Kalitta",       0.052, 3.754, 333.91, True)
add(R, 3, "Maddi Gordon",       0.118, 4.630, 165.07, False)
# Round 4 (Final)
add(R, 4, "Josh Hart",          0.072, 3.733, 337.83, True)
add(R, 4, "Doug Kalitta",       0.065, 3.877, 319.60, False)

# ============================================================
# RACE 2: ARIZONA NATIONALS (Chandler) - Mar 20-22 - Langdon won
# ============================================================
R = "Arizona Nationals"
# Round 1
add(R, 1, "Tony Stewart",       0.062, 3.823, 329.99, True)
add(R, 1, "Shawn Reed",         0.066, 3.932, 316.38, False)
add(R, 1, "Maddi Gordon",       0.085, 3.852, 324.98, True)
add(R, 1, "Jaren Mott",         0.119, 3.962, 281.07, False)
add(R, 1, "Leah Pruett",        0.119, 3.827, 327.74, True)
add(R, 1, "Cameron Ferre",      0.062, 4.670, 178.47, False)
add(R, 1, "Shawn Langdon",      0.056, 3.832, 331.04, True)  # unopposed
add(R, 1, "Doug Kalitta",       0.095, 3.791, 331.94, True)
add(R, 1, "Will Smith",         0.068, 3.852, 320.97, False)
add(R, 1, "Billy Torrence",     0.091, 3.844, 329.10, True)
add(R, 1, "Antron Brown",       0.059, 4.109, 250.13, False)
add(R, 1, "Josh Hart",          0.056, 4.000, 280.02, True)
add(R, 1, "Justin Ashley",      0.035, 4.115, 269.03, False)
add(R, 1, "Tony Schumacher",    0.108, 4.329, 239.82, True)
add(R, 1, "Clay Millican",      0.100, 4.595, 170.13, False)
# Round 2
add(R, 2, "Shawn Langdon",      0.067, 3.859, 329.02, True)
add(R, 2, "Tony Schumacher",    0.093, 3.987, 282.24, False)
add(R, 2, "Leah Pruett",        0.098, 3.887, 319.52, True)
add(R, 2, "Josh Hart",          0.075, 4.081, 275.62, False)
add(R, 2, "Maddi Gordon",       0.095, 3.851, 324.83, True)
add(R, 2, "Tony Stewart",       0.079, 3.950, 311.13, False)
add(R, 2, "Doug Kalitta",       0.080, 3.874, 327.59, True)
add(R, 2, "Billy Torrence",     0.131, 3.953, 321.96, False)
# Round 3
add(R, 3, "Leah Pruett",        0.093, 3.887, 316.52, True)
add(R, 3, "Doug Kalitta",       0.055, 3.926, 314.75, False)
add(R, 3, "Shawn Langdon",      0.067, 3.979, 297.68, True)
add(R, 3, "Maddi Gordon",       0.087, 4.396, 187.31, False)
# Round 4 (Final)
add(R, 4, "Shawn Langdon",      0.079, 3.877, 325.45, True)
add(R, 4, "Leah Pruett",        0.080, 3.930, 317.57, False)

# ============================================================
# RACE 3: WINTERNATIONALS (Pomona) - Apr 9-12 - Stewart won
# ============================================================
R = "Winternationals"
# Round 1 (Ferre broke before staging, August no-show; both excluded from RT pool)
add(R, 1, "Justin Ashley",      0.025, 3.714, 332.43, True)
add(R, 1, "Maddi Gordon",       0.091, 3.744, 334.15, False)
add(R, 1, "Tony Stewart",       0.055, 3.726, 327.11, True)
add(R, 1, "Will Smith",         0.029, 4.209, 224.14, False)
add(R, 1, "Clay Millican",      0.080, 3.758, 318.47, True)
add(R, 1, "Shawn Reed",         0.091, 4.327, 193.10, False)
add(R, 1, "Josh Hart",          0.160, 3.698, 336.91, True)   # Ferre broke
add(R, 1, "Leah Pruett",        0.105, 6.721, 99.54,  True)   # unopposed
add(R, 1, "Shawn Langdon",      0.059, 4.003, 252.99, True)
add(R, 1, "Tony Schumacher",    0.089, 4.454, 169.59, False)
add(R, 1, "Doug Kalitta",       0.071, 3.719, 339.79, True)   # August no-show
add(R, 1, "Billy Torrence",     0.075, 3.746, 336.91, True)
add(R, 1, "Antron Brown",       0.058, 6.064, 112.45, False)
# Round 2
add(R, 2, "Shawn Langdon",      0.067, 3.689, 336.74, True)
add(R, 2, "Billy Torrence",     0.059, 3.713, 335.15, False)
add(R, 2, "Doug Kalitta",       0.042, 3.694, 339.36, True)
add(R, 2, "Clay Millican",      0.086, 8.570, 78.34,  False)
add(R, 2, "Tony Stewart",       0.058, 3.715, 337.92, True)
add(R, 2, "Josh Hart",          0.065, 3.968, 236.46, False)
add(R, 2, "Justin Ashley",      0.025, 3.720, 336.07, True)
add(R, 2, "Leah Pruett",        0.064, 3.703, 334.73, False)
# Round 3
add(R, 3, "Justin Ashley",      0.025, 3.705, 326.24, True)
add(R, 3, "Doug Kalitta",       0.034, 3.705, 340.56, False)
add(R, 3, "Tony Stewart",       0.042, 3.701, 334.98, True)
add(R, 3, "Shawn Langdon",      0.048, 3.718, 339.53, False)
# Round 4 (Final)
add(R, 4, "Tony Stewart",       0.047, 3.683, 332.51, True)
add(R, 4, "Justin Ashley",      0.036, 3.714, 328.54, False)

# ============================================================
# RACE 4: 4-WIDE NATIONALS (Concord) - Apr 23-26 - Kalitta won
# 4-wide format. Note: Schumacher broke before staging in R1 (no RT recorded).
# ============================================================
R = "4-Wide Nationals"
# Round 1
add(R, 1, "Tony Stewart",       0.054, 3.727, 331.36, True)
add(R, 1, "Billy Torrence",     0.063, 3.731, 335.98, True)
add(R, 1, "Josh Hart",          0.087, 3.753, 333.16, False)
# (Schumacher NT - omitted)
add(R, 1, "Doug Kalitta",       0.055, 3.686, 337.33, True)
add(R, 1, "Maddi Gordon",       0.082, 3.777, 332.51, True)
add(R, 1, "Clay Millican",      0.059, 3.911, 266.69, False)
add(R, 1, "Antron Brown",       0.059, 4.267, 193.02, False)
add(R, 1, "Justin Ashley",      0.032, 3.699, 336.74, True)
add(R, 1, "Leah Pruett",        0.094, 3.673, 333.16, True)
add(R, 1, "Will Smith",         0.033, 3.748, 330.47, False)
add(R, 1, "Ida Zetterstrom",    0.188, 3.803, 334.90, False)
add(R, 1, "Shawn Langdon",      0.075, 3.673, 330.15, True)
add(R, 1, "Spencer Massey",     0.050, 3.822, 325.30, True)
add(R, 1, "Dan Mercier",        0.090, 3.800, 326.32, False)
add(R, 1, "Jasmine Salinas",    0.080, 4.561, 142.61, False)
# Round 2
add(R, 2, "Shawn Langdon",      0.038, 3.748, 329.02, True)
add(R, 2, "Tony Stewart",       0.064, 3.776, 328.22, True)
add(R, 2, "Spencer Massey",     0.047, 3.798, 326.56, False)
add(R, 2, "Billy Torrence",     0.084, 3.785, 324.44, False)
add(R, 2, "Doug Kalitta",       0.059, 3.707, 339.02, True)
add(R, 2, "Leah Pruett",        0.056, 3.749, 333.66, True)
add(R, 2, "Justin Ashley",      0.036, 3.774, 331.61, False)
add(R, 2, "Maddi Gordon",       0.060, 3.767, 333.16, False)
# Round 3 (semifinal, 4-wide - top 1 advances per quad in some quads; this one was Kalitta advancing)
add(R, 3, "Doug Kalitta",       0.073, 3.692, 342.98, True)
add(R, 3, "Shawn Langdon",      0.052, 3.727, 338.51, False)
add(R, 3, "Leah Pruett",        0.095, 3.724, 329.42, False)
add(R, 3, "Tony Stewart",       0.057, 10.663, 66.89, False)

# ============================================================
# RACE 5: SOUTHERN NATIONALS (Adel) - May 1-3 - Langdon won
# ============================================================
R = "Southern Nationals"
# Round 1
add(R, 1, "Antron Brown",       0.062, 3.746, 331.94, True)
add(R, 1, "Shawn Reed",         0.090, 3.727, 333.58, False)
add(R, 1, "Clay Millican",      0.098, 3.812, 327.74, True)
add(R, 1, "Tony Schumacher",    0.049, 8.933, 83.50,  False)
add(R, 1, "Justin Ashley",      0.041, 4.073, 254.81, True)
add(R, 1, "Tony Stewart",       0.075, 10.598, 66.69, False)
add(R, 1, "Maddi Gordon",       0.079, 3.728, 340.22, True)
add(R, 1, "Will Smith",         0.042, 4.056, 258.12, False)
add(R, 1, "Doug Kalitta",       0.058, 3.732, 338.94, True)  # unopposed
add(R, 1, "Shawn Langdon",      0.105, 4.151, 249.72, True)
add(R, 1, "Cameron Ferre",      0.087, 6.650, 103.35, False)
add(R, 1, "Billy Torrence",     0.105, 3.742, 335.82, True)
add(R, 1, "Dan Mercier",        0.092, 9.198, 88.29,  False)
add(R, 1, "Leah Pruett",        0.094, 3.996, 287.78, True)
add(R, 1, "Josh Hart",          0.077, 7.296, 77.48,  False)
# Round 2
add(R, 2, "Shawn Langdon",      0.089, 3.812, 332.59, True)
add(R, 2, "Antron Brown",       0.064, 13.197, 38.36, False)
add(R, 2, "Clay Millican",      0.107, 5.026, 147.91, True)
add(R, 2, "Billy Torrence",     0.088, 7.136, 142.97, False)
add(R, 2, "Justin Ashley",      0.056, 4.035, 246.35, True)
add(R, 2, "Maddi Gordon",       0.067, 10.440, 80.96, False)
add(R, 2, "Doug Kalitta",       0.062, 3.798, 333.00, True)
add(R, 2, "Leah Pruett",        0.027, 3.864, 322.96, False)
# Round 3
add(R, 3, "Shawn Langdon",      0.058, 3.898, 316.90, True)
add(R, 3, "Clay Millican",      0.090, 7.214, 82.81,  False)
add(R, 3, "Doug Kalitta",       0.074, 5.190, 288.58, True)
add(R, 3, "Justin Ashley",      0.056, 5.450, 183.57, False)
# Round 4 (Final)
add(R, 4, "Shawn Langdon",      0.070, 3.808, 333.16, True)
add(R, 4, "Doug Kalitta",       0.074, 3.954, 314.61, False)

# ============================================================
# RACE 6: ROUTE 66 NATIONALS (Joliet) - May 14-17 - Langdon won
# ============================================================
R = "Route 66 Nationals"
# Round 1
add(R, 1, "Antron Brown",       0.049, 3.777, 329.18, True)
add(R, 1, "T.J. Zizzo",         0.084, 3.796, 329.99, False)
add(R, 1, "Tony Stewart",       0.065, 3.742, 334.48, True)
add(R, 1, "Tony Schumacher",    0.063, 3.785, 333.82, False)
add(R, 1, "Josh Hart",          0.035, 3.790, 338.26, True)
add(R, 1, "Justin Ashley",      0.044, 3.785, 322.11, False)
add(R, 1, "Maddi Gordon",       0.072, 3.813, 329.58, True)
add(R, 1, "Krista Baldwin",     0.091, 4.347, 192.96, False)
add(R, 1, "Doug Kalitta",       0.061, 3.736, 327.98, True)  # unopposed
add(R, 1, "Will Smith",         0.049, 3.776, 331.45, True)
add(R, 1, "Billy Torrence",     0.085, 3.795, 332.92, False)
add(R, 1, "Leah Pruett",        0.076, 3.739, 326.16, True)
add(R, 1, "Clay Millican",      0.093, 3.868, 272.61, False)
add(R, 1, "Shawn Langdon",      0.068, 3.739, 338.68, True)
add(R, 1, "Shawn Reed",         0.061, 3.886, 296.11, False)
# Round 2
add(R, 2, "Antron Brown",       0.061, 3.774, 332.18, True)
add(R, 2, "Maddi Gordon",       0.066, 3.804, 333.82, False)
add(R, 2, "Josh Hart",          0.067, 3.782, 330.63, True)
add(R, 2, "Tony Stewart",       0.061, 6.384, 95.98,  False)
add(R, 2, "Leah Pruett",        0.072, 4.201, 205.16, True)
add(R, 2, "Will Smith",         0.046, 0.000, 0.0,    False)  # NT-Broke After Staging
add(R, 2, "Shawn Langdon",      0.073, 3.789, 333.49, True)
add(R, 2, "Doug Kalitta",       0.059, 4.408, 220.84, False)
# Round 3
add(R, 3, "Shawn Langdon",      0.068, 3.790, 332.10, True)
add(R, 3, "Josh Hart",          0.047, 3.823, 333.16, False)
add(R, 3, "Antron Brown",       0.059, 3.809, 328.38, True)
add(R, 3, "Leah Pruett",        0.065, 5.810, 119.90, False)
# Round 4 (Final)
add(R, 4, "Shawn Langdon",      0.068, 3.775, 335.90, True)
add(R, 4, "Antron Brown",       0.053, 4.225, 206.48, False)

# ============================================================
# WRITE TO CSV
# ============================================================
import csv, os
out = "/sessions/great-determined-cannon/mnt/Wes Buck Show Operating Room/RT_Report/2026_TF_runs.csv"
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["race","round","driver","rt","et","mph","win"])
    w.writeheader()
    for row in DATA:
        w.writerow(row)
print(f"Wrote {len(DATA)} run records to:")
print(out)
