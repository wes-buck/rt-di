"""PDRA Pro Nitrous & Pro Boost — manually transcribed via vision OCR from
racepdra.com elimination images. Two formats observed:
  - "summary" tabular results (Benson East Coast Nationals 2026): full data
  - "bracket" images (Darlington Carolina Nationals 2026): R1+R2 only, no R3/Final

Sources:
  pdra660.com/results/2026/darlington-carolina-nationals
  pdra660.com/results/2026/benson-east-coast-nationals

Each run row has:
  class, race, year, round, driver, rt, et, mph, win, opps[list]

Notes:
  - 'Single' runs (e.g. Salemi Benson R1) have empty opps list.
  - Driver names with leading initial in source (e.g. 'John Doc', 'Ed Marx')
    are best-guess transcriptions — please verify.
  - Darlington PN R3+Final not in source image: Tommy Franklin won the event
    but per-round data after R2 isn't captured.
  - Darlington PB R3+Final also not in source image.
"""

RUNS = []


def add(cls, race, year, rnd, driver, rt, et, mph, win, opps):
    RUNS.append({
        "class": cls, "race": race, "year": year, "round": rnd,
        "driver": driver, "rt": rt, "et": et, "mph": mph, "win": win,
        "opps": list(opps),
    })


# =================================================================
# 2026 DARLINGTON — PDRA Carolina Nationals, March 25-28, 2026
# Bracket image; only R1 and R2 data available
# =================================================================
R = "Carolina Nationals"
Y = 2026

# PRO NITROUS — Darlington
# Round 1 (8 pairs)
add("PN", R, Y, 1, "Tommy Franklin",  0.015, 3.665, 206.71, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",   -0.007, 4.005, 185.64, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Buddy Perkinson", 0.012, 3.673, 207.09, True,  ["Cam Clark"])
add("PN", R, Y, 1, "Cam Clark",       0.004, 4.261, 136.74, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Fredy Scriba",    0.086, 3.692, 205.57, True,  ["Amber Denton"])
add("PN", R, Y, 1, "Amber Denton",    0.042, 3.907, 195.91, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Rickie Smith",    0.031, 3.679, 206.33, True,  ["Corey Smith"])
add("PN", R, Y, 1, "Corey Smith",     0.005, 3.745, 199.47, False, ["Rickie Smith"])
add("PN", R, Y, 1, "Mike Achenbach",  0.024, 3.664, 206.80, True,  ["Dale Brinsfield"])
add("PN", R, Y, 1, "Dale Brinsfield", 0.013, 5.004, 101.31, False, ["Mike Achenbach"])
add("PN", R, Y, 1, "Chris Rini",      0.041, 3.939, 195.31, True,  ["Ed Wilson"])
add("PN", R, Y, 1, "Ed Wilson",       0.352, 3.696, 187.19, False, ["Chris Rini"])
add("PN", R, Y, 1, "Marcus Butner",   0.032, 3.641, 207.85, True,  ["Tim Molnar"])
add("PN", R, Y, 1, "Tim Molnar",      0.026, 5.851,  73.19, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Brian Shrader",   0.020, 3.789, 200.62, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",    0.089, 5.384,  90.84, False, ["Brian Shrader"])
# Round 2 (4 pairs)
add("PN", R, Y, 2, "Tommy Franklin",  0.034, 3.632, 207.28, True,  ["Buddy Perkinson"])
add("PN", R, Y, 2, "Buddy Perkinson",-0.001, 3.654, 205.86, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Fredy Scriba",    0.012, 3.644, 206.71, True,  ["Rickie Smith"])
add("PN", R, Y, 2, "Rickie Smith",    0.014, 5.013,  99.73, False, ["Fredy Scriba"])
add("PN", R, Y, 2, "Mike Achenbach",  0.033, 3.661, 207.56, True,  ["Chris Rini"])
add("PN", R, Y, 2, "Chris Rini",      0.018, 3.902, 197.11, False, ["Mike Achenbach"])
add("PN", R, Y, 2, "Marcus Butner",   0.040, 3.617, 209.01, True,  ["Brian Shrader"])
add("PN", R, Y, 2, "Brian Shrader",   0.054, 3.726, 202.98, False, ["Marcus Butner"])

# PRO BOOST — Darlington
# Round 1 (8 pairs)
add("PB", R, Y, 1, "Joel Wensley",    0.007, 3.646, 212.77, True,  ["Randy Weatherford"])
add("PB", R, Y, 1, "Randy Weatherford",-0.011,3.562, 213.07, False, ["Joel Wensley"])
add("PB", R, Y, 1, "Melanie Salemi",  0.023, 3.598, 211.27, True,  ["Ethan Steding"])
add("PB", R, Y, 1, "Ethan Steding",   0.024, 6.000,  89.90, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Johnny Camp",     0.027, 3.563, 213.57, True,  ["John Doc"])
add("PB", R, Y, 1, "John Doc",         -0.010, 3.606, 210.97, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Raymond Matos",   0.012, 3.583, 212.26, True,  ["Ned Dunphy"])
add("PB", R, Y, 1, "Ned Dunphy",      0.037, 3.578, 212.67, False, ["Raymond Matos"])
add("PB", R, Y, 1, "Jason Harris",    0.026, 3.590, 210.97, True,  ["Travis Harvey"])
add("PB", R, Y, 1, "Travis Harvey",   0.045, 3.589, 212.36, False, ["Jason Harris"])
add("PB", R, Y, 1, "Ty Tutterow",     0.000, 3.693, 209.50, True,  ["Jay Cox"])
add("PB", R, Y, 1, "Jay Cox",         0.022, 3.694, 207.18, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Lyle Barnett",    0.002, 3.642, 210.18, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",    0.116, 5.262,  90.74, False, ["Lyle Barnett"])
add("PB", R, Y, 1, "Steve King",      0.008, 5.008,  97.02, True,  ["Ed Marx"])
add("PB", R, Y, 1, "Ed Marx",        -0.016, 3.600, 207.18, False, ["Steve King"])
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Melanie Salemi",  0.049, 3.561, 212.36, True,  ["Joel Wensley"])
add("PB", R, Y, 2, "Joel Wensley",   -0.004, 3.648, 212.87, False, ["Melanie Salemi"])
add("PB", R, Y, 2, "Johnny Camp",     0.038, 3.542, 213.88, True,  ["Raymond Matos"])
add("PB", R, Y, 2, "Raymond Matos",   0.014, 3.577, 212.46, False, ["Johnny Camp"])
add("PB", R, Y, 2, "Ty Tutterow",     0.025, 3.575, 213.47, True,  ["Jason Harris"])
add("PB", R, Y, 2, "Jason Harris",    0.005, 4.236, 123.46, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Lyle Barnett",    0.005, 3.549, 213.68, True,  ["Steve King"])
add("PB", R, Y, 2, "Steve King",     -0.003, 3.587, 202.52, False, ["Lyle Barnett"])

# =================================================================
# 2026 BENSON — PDRA East Coast Nationals, April 16-18, 2026
# Summary image; complete data (R1, R2, R3, Finals)
# =================================================================
R = "East Coast Nationals"
Y = 2026

# PRO NITROUS — Benson
# Round 1 (8 pairs — Smith vs Denton: Denton broke, no time)
add("PN", R, Y, 1, "Tim Molnar",      0.017, 3.747, 203.89, True,  ["Fredy Scriba"])
add("PN", R, Y, 1, "Fredy Scriba",    0.086, 3.705, 204.63, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Buddy Perkinson", 0.069, 3.717, 204.42, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",    0.041, 3.750, 199.11, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Keith Haney",     0.031, 3.714, 206.35, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",    0.054, 3.747, 205.01, False, ["Keith Haney"])
add("PN", R, Y, 1, "Rickie Smith",    0.074, 3.744, 204.85, True,  ["Amber Denton"])
# Amber Denton "BROKE" — no RT/ET captured
add("PN", R, Y, 1, "Tommy Franklin",  0.018, 3.714, 205.10, True,  ["Chris Rini"])
add("PN", R, Y, 1, "Chris Rini",      0.033, 3.774, 203.86, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Mike Achenbach",  0.026, 3.710, 207.21, True,  ["Cam Clark"])
add("PN", R, Y, 1, "Cam Clark",       0.044, 3.790, 199.32, False, ["Mike Achenbach"])
add("PN", R, Y, 1, "Tim Paap",        0.051, 3.720, 203.31, True,  ["Dane Wood"])
add("PN", R, Y, 1, "Dane Wood",       0.013, 5.457,  89.23, False, ["Tim Paap"])
add("PN", R, Y, 1, "Marcus Butner",   0.050, 3.704, 205.07, True,  ["Brian Shrader"])
add("PN", R, Y, 1, "Brian Shrader",   0.055, 3.741, 203.92, False, ["Marcus Butner"])
# Round 2 (only 3 of 4 pairs in source image — Perkinson def. Paap missing)
add("PN", R, Y, 2, "Tommy Franklin",  0.023, 3.711, 205.29, True,  ["Rickie Smith"])
add("PN", R, Y, 2, "Rickie Smith",    0.034, 3.750, 204.05, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Keith Haney",     0.033, 3.755, 195.19, True,  ["Mike Achenbach"])
add("PN", R, Y, 2, "Mike Achenbach", -0.011, 4.586, 115.53, False, ["Keith Haney"])
add("PN", R, Y, 2, "Tim Molnar",      0.018, 3.767, 203.68, True,  ["Marcus Butner"])
add("PN", R, Y, 2, "Marcus Butner",   0.056, 4.372, 126.76, False, ["Tim Molnar"])
# Note: 4th R2 pair (Perkinson def. Paap) not in source image; R3 confirms Perkinson advanced
# Round 3 (2 pairs)
add("PN", R, Y, 3, "Keith Haney",     0.053, 3.664, 206.48, True,  ["Buddy Perkinson"])
add("PN", R, Y, 3, "Buddy Perkinson", 0.100, 3.691, 204.79, False, ["Keith Haney"])
add("PN", R, Y, 3, "Tommy Franklin",  0.016, 3.669, 205.60, True,  ["Tim Molnar"])
add("PN", R, Y, 3, "Tim Molnar",      0.022, 3.707, 204.98, False, ["Tommy Franklin"])
# Finals
add("PN", R, Y, 4, "Tommy Franklin",  0.089, 3.676, 206.64, True,  ["Keith Haney"])
add("PN", R, Y, 4, "Keith Haney",     0.007, 3.966, 148.01, False, ["Tommy Franklin"])

# PRO BOOST — Benson
# Round 1 (Salemi was Single — no opponent)
add("PB", R, Y, 1, "Travis Harvey",   0.004, 3.626, 208.20, True,  ["Ned Dunphy"])
add("PB", R, Y, 1, "Ned Dunphy",      0.001, 3.637, 207.34, False, ["Travis Harvey"])
add("PB", R, Y, 1, "Ethan Steding",   0.067, 3.652, 207.43, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",    0.025, 6.205,  74.07, False, ["Ethan Steding"])
add("PB", R, Y, 1, "Steve King",      0.039, 3.640, 205.29, True,  ["Randy Weatherford"])
add("PB", R, Y, 1, "Randy Weatherford",0.043,3.681, 209.43, False, ["Steve King"])
add("PB", R, Y, 1, "Jay Cox",         0.068, 3.631, 208.20, True,  ["Gabriel Andino"])
add("PB", R, Y, 1, "Gabriel Andino",  0.028, 3.689, 205.63, False, ["Jay Cox"])
add("PB", R, Y, 1, "Ty Tutterow",     0.035, 3.650, 208.46, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",  -0.004, 3.723, 208.23, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Johnny Camp",     0.032, 3.650, 209.85, True,  ["Chris Cline"])
add("PB", R, Y, 1, "Chris Cline",     0.035, 3.751, 211.16, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Jason Harris",    0.010, 3.637, 210.37, True,  ["Joel Wensley"])
add("PB", R, Y, 1, "Joel Wensley",    0.046, 6.068,  77.48, False, ["Jason Harris"])
add("PB", R, Y, 1, "Melanie Salemi",  0.010, 3.615, 208.39, True,  [])  # SINGLE
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Johnny Camp",     0.030, 3.653, 209.56, True,  ["Steve King"])
add("PB", R, Y, 2, "Steve King",      0.017, 4.441, 122.97, False, ["Johnny Camp"])
add("PB", R, Y, 2, "Jason Harris",    0.016, 3.639, 209.62, True,  ["Ethan Steding"])
add("PB", R, Y, 2, "Ethan Steding",   0.025, 3.647, 207.37, False, ["Jason Harris"])
add("PB", R, Y, 2, "Jay Cox",         0.035, 3.830, 155.10, True,  ["Ty Tutterow"])
# Tutterow "BROKE" in R2 — no time captured
add("PB", R, Y, 2, "Melanie Salemi",  0.044, 3.643, 207.02, True,  ["Travis Harvey"])
add("PB", R, Y, 2, "Travis Harvey",   0.022, 4.436, 118.96, False, ["Melanie Salemi"])
# Round 3 (2 pairs)
add("PB", R, Y, 3, "Melanie Salemi",  0.010, 3.626, 206.95, True,  ["Jay Cox"])
add("PB", R, Y, 3, "Jay Cox",         0.038, 3.630, 207.66, False, ["Melanie Salemi"])
add("PB", R, Y, 3, "Jason Harris",    0.004, 3.612, 209.20, True,  ["Johnny Camp"])
add("PB", R, Y, 3, "Johnny Camp",     0.067, 3.627, 208.88, False, ["Jason Harris"])
# Finals
add("PB", R, Y, 4, "Jason Harris",    0.021, 3.643, 200.47, True,  ["Melanie Salemi"])
add("PB", R, Y, 4, "Melanie Salemi",  0.043, 3.723, 168.53, False, ["Jason Harris"])


# =================================================================
# 2025 PDRA SEASON — full 7-race schedule (Norwalk cancelled)
# Each race has complete data (R1, R2, R3, Finals) sourced from
# racepdra.com elimination summary images.
# =================================================================

# -----------------------------------------------------------------
# 2025 East Coast Nationals — GALOT, April 5, 2025
# PN winner: Tim Paap   /   PB winner: Melanie Salemi
# -----------------------------------------------------------------
R, Y = "East Coast Nationals", 2025

# PRO NITROUS
add("PN", R, Y, 1, "Tim Molnar",       0.010, 3.741, 202.12, True,  ["Matthew Deitsch"])
add("PN", R, Y, 1, "Matthew Deitsch",  0.031, 5.047,  98.53, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Marcus Butner",    0.031, 3.718, 204.39, True,  ["Buddy Perkinson"])
add("PN", R, Y, 1, "Buddy Perkinson", -0.003, 3.728, 202.79, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Jackie Slone Jr",  0.253, 3.733, 203.16, True,  ["John Vergotz"])
# John Vergotz BROKE; no RT/ET
add("PN", R, Y, 1, "Tony Wilson",      0.033, 3.766, 201.25, True,  ["Fredy Scriba"])
add("PN", R, Y, 1, "Fredy Scriba",    -0.006, 6.857,  65.82, False, ["Tony Wilson"])
add("PN", R, Y, 1, "Dane Wood",        0.036, 3.728, 200.26, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",     0.045, 3.721, 205.32, False, ["Dane Wood"])
add("PN", R, Y, 1, "Amber Denton",     0.045, 3.694, 203.61, True,  ["Corey Smith"])
add("PN", R, Y, 1, "Corey Smith",      0.035, 3.760, 198.70, False, ["Amber Denton"])
add("PN", R, Y, 1, "Tommy Franklin",   0.028, 3.695, 204.51, True,  ["Tommy Mauney"])
add("PN", R, Y, 1, "Tommy Mauney",     0.064, 5.625,  85.96, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Tim Paap",         0.017, 3.699, 203.95, True,  ["Edward Wilson"])
add("PN", R, Y, 1, "Edward Wilson",    0.085, 10.550, 38.36, False, ["Tim Paap"])

add("PN", R, Y, 2, "Tony Wilson",      0.008, 3.748, 202.61, True,  ["Dane Wood"])
add("PN", R, Y, 2, "Dane Wood",        0.038, 4.306, 128.26, False, ["Tony Wilson"])
add("PN", R, Y, 2, "Tim Paap",         0.005, 3.679, 201.67, True,  ["Tim Molnar"])
add("PN", R, Y, 2, "Tim Molnar",       0.028, 3.732, 204.08, False, ["Tim Paap"])
add("PN", R, Y, 2, "Tommy Franklin",   0.016, 3.678, 205.07, True,  ["Marcus Butner"])
add("PN", R, Y, 2, "Marcus Butner",    0.014, 3.698, 206.29, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Jackie Slone Jr",  0.023, 3.720, 203.77, True,  ["Amber Denton"])
add("PN", R, Y, 2, "Amber Denton",     0.097, 3.719, 203.40, False, ["Jackie Slone Jr"])

add("PN", R, Y, 3, "Tim Paap",         0.043, 3.688, 203.80, True,  ["Tony Wilson"])
add("PN", R, Y, 3, "Tony Wilson",      0.025, 3.736, 202.82, False, ["Tim Paap"])
add("PN", R, Y, 3, "Tommy Franklin",   0.026, 3.666, 205.47, True,  ["Jackie Slone Jr"])
add("PN", R, Y, 3, "Jackie Slone Jr",  0.024, 4.742, 108.80, False, ["Tommy Franklin"])

add("PN", R, Y, 4, "Tim Paap",         0.019, 3.651, 205.26, True,  ["Tommy Franklin"])
add("PN", R, Y, 4, "Tommy Franklin",   0.036, 3.652, 205.66, False, ["Tim Paap"])

# PRO BOOST
add("PB", R, Y, 1, "Preston Tanner",   0.014, 3.670, 204.91, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",    -0.018, 3.681, 204.23, False, ["Preston Tanner"])
add("PB", R, Y, 1, "Ty Tutterow",      0.031, 3.701, 193.43, True,  ["David Monday"])
add("PB", R, Y, 1, "David Monday",     0.237, 3.695, 203.52, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Scott Lang",       0.036, 3.692, 210.87, True,  ["Jay Cox"])
add("PB", R, Y, 1, "Jay Cox",          0.011, 3.720, 215.65, False, ["Scott Lang"])
add("PB", R, Y, 1, "Steve King",       0.083, 3.646, 204.23, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",   -0.007, 3.769, 200.56, False, ["Steve King"])
add("PB", R, Y, 1, "Travis Harvey",    0.010, 6.567,  92.86, True,  ["Tim Dutton"])
add("PB", R, Y, 1, "Tim Dutton",      -0.003, 3.691, 204.32, False, ["Travis Harvey"])
add("PB", R, Y, 1, "Johnny Camp",      0.014, 3.653, 204.51, True,  ["Randy Weatherford"])
add("PB", R, Y, 1, "Randy Weatherford",-0.001,3.655, 205.60, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Jason Harris",     0.027, 3.661, 206.04, True,  ["Tom Blincoe"])
add("PB", R, Y, 1, "Tom Blincoe",      0.023, 5.590,  83.53, False, ["Jason Harris"])
add("PB", R, Y, 1, "Melanie Salemi",   0.016, 3.639, 205.41, True,  ["Lyle Barnett"])
add("PB", R, Y, 1, "Lyle Barnett",     0.025, 4.653, 109.74, False, ["Melanie Salemi"])

add("PB", R, Y, 2, "Ty Tutterow",      0.006, 3.769, 174.53, True,  ["Jason Harris"])
add("PB", R, Y, 2, "Jason Harris",     0.015, 3.782, 192.82, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Johnny Camp",      0.029, 3.644, 205.04, True,  ["Scott Lang"])
add("PB", R, Y, 2, "Scott Lang",       0.013, 3.708, 204.73, False, ["Johnny Camp"])
add("PB", R, Y, 2, "Steve King",       0.006, 3.635, 204.88, True,  ["Travis Harvey"])
add("PB", R, Y, 2, "Travis Harvey",    0.026, 3.642, 207.78, False, ["Steve King"])
add("PB", R, Y, 2, "Melanie Salemi",   0.027, 3.625, 206.29, True,  ["Preston Tanner"])
add("PB", R, Y, 2, "Preston Tanner",   0.014, 3.651, 205.41, False, ["Melanie Salemi"])

add("PB", R, Y, 3, "Johnny Camp",      0.022, 3.631, 205.04, True,  ["Ty Tutterow"])
add("PB", R, Y, 3, "Ty Tutterow",      0.011, 3.683, 204.35, False, ["Johnny Camp"])
add("PB", R, Y, 3, "Melanie Salemi",   0.016, 3.617, 206.61, True,  ["Steve King"])
add("PB", R, Y, 3, "Steve King",       0.062, 3.640, 205.66, False, ["Melanie Salemi"])

add("PB", R, Y, 4, "Melanie Salemi",   0.001, 3.622, 206.29, True,  ["Johnny Camp"])
add("PB", R, Y, 4, "Johnny Camp",      0.018, 3.628, 205.13, False, ["Melanie Salemi"])

# -----------------------------------------------------------------
# 2025 Mid-Atlantic Showdown — VMP, May 4, 2025
# PN winner: Marcus Butner   /   PB winner: Kurt Steding
# -----------------------------------------------------------------
R, Y = "Mid-Atlantic Showdown", 2025

add("PN", R, Y, 1, "Tim Molnar",       0.000, 3.715, 204.82, True,  ["Steve Jackson"])
add("PN", R, Y, 1, "Steve Jackson",    0.015, 3.732, 203.28, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Brian Shrader",    0.012, 3.701, 205.38, True,  ["Dane Wood"])
add("PN", R, Y, 1, "Dane Wood",       -0.020, 3.755, 201.97, False, ["Brian Shrader"])
add("PN", R, Y, 1, "Buddy Perkinson",  0.013, 3.747, 202.06, True,  ["Matthew Deitsch"])
add("PN", R, Y, 1, "Matthew Deitsch",  0.042, 4.251, 130.89, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Corey Smith",      0.031, 3.731, 199.88, True,  ["Jackie Slone Jr"])
add("PN", R, Y, 1, "Jackie Slone Jr",  0.021, 3.761, 203.37, False, ["Corey Smith"])
add("PN", R, Y, 1, "Amber Denton",     0.048, 4.379, 136.97, True,  ["Jim Widener"])
add("PN", R, Y, 1, "Jim Widener",      0.014, 5.081,  93.02, False, ["Amber Denton"])
add("PN", R, Y, 1, "Billy Albert",     0.009, 3.697, 206.57, True,  ["Fredy Scriba"])
add("PN", R, Y, 1, "Fredy Scriba",     0.028, 4.652, 111.12, False, ["Billy Albert"])
add("PN", R, Y, 1, "Marcus Butner",    0.066, 3.706, 205.79, True,  ["Cam Clark"])
add("PN", R, Y, 1, "Cam Clark",        0.047, 3.750, 199.64, False, ["Marcus Butner"])
add("PN", R, Y, 1, "John Vergotz",     0.058, 3.737, 201.13, True,  ["Tommy Franklin"])
add("PN", R, Y, 1, "Tommy Franklin",   0.011, 3.944, 169.59, False, ["John Vergotz"])

add("PN", R, Y, 2, "Amber Denton",     0.067, 3.675, 198.70, True,  ["Corey Smith"])
add("PN", R, Y, 2, "Corey Smith",     -0.005, 3.729, 200.83, False, ["Amber Denton"])
add("PN", R, Y, 2, "John Vergotz",     0.065, 3.914, 176.35, True,  ["Tim Molnar"])
add("PN", R, Y, 2, "Tim Molnar",       0.013, 4.752, 110.31, False, ["John Vergotz"])
add("PN", R, Y, 2, "Marcus Butner",    0.040, 3.689, 207.78, True,  ["Brian Shrader"])
add("PN", R, Y, 2, "Brian Shrader",    0.025, 3.707, 201.19, False, ["Marcus Butner"])
add("PN", R, Y, 2, "Buddy Perkinson",  0.012, 3.798, 175.00, True,  ["Billy Albert"])
add("PN", R, Y, 2, "Billy Albert",    -0.001, 3.724, 205.85, False, ["Buddy Perkinson"])

add("PN", R, Y, 3, "Marcus Butner",    0.039, 3.637, 208.62, True,  ["Buddy Perkinson"])
add("PN", R, Y, 3, "Buddy Perkinson",  0.010, 3.681, 204.63, False, ["Marcus Butner"])
add("PN", R, Y, 3, "Amber Denton",     0.035, 3.659, 206.92, True,  ["John Vergotz"])
add("PN", R, Y, 3, "John Vergotz",     0.069, 4.173, 150.63, False, ["Amber Denton"])

add("PN", R, Y, 4, "Marcus Butner",    0.021, 3.639, 208.55, True,  ["Amber Denton"])
add("PN", R, Y, 4, "Amber Denton",     0.042, 3.772, 189.95, False, ["Marcus Butner"])

add("PB", R, Y, 1, "Randy Weatherford",0.043, 3.689, 206.10, True,  ["Steve King"])
add("PB", R, Y, 1, "Steve King",       0.011, 3.911, 195.73, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Kurt Steding",     0.011, 3.685, 205.88, True,  ["James Beadling"])
add("PB", R, Y, 1, "James Beadling",   0.016, 3.728, 204.88, False, ["Kurt Steding"])
add("PB", R, Y, 1, "Melanie Salemi",   0.023, 3.688, 205.10, True,  ["Chuck Ulsch"])
add("PB", R, Y, 1, "Chuck Ulsch",      0.144, 4.462, 119.52, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Ed Marx",          0.034, 3.706, 205.01, True,  ["Tommy Gray"])
add("PB", R, Y, 1, "Tommy Gray",       0.082, 3.674, 205.32, False, ["Ed Marx"])
add("PB", R, Y, 1, "Johnny Camp",      0.034, 3.666, 205.69, True,  ["Jason Lee"])
add("PB", R, Y, 1, "Jason Lee",        0.034, 3.695, 202.82, False, ["Johnny Camp"])
add("PB", R, Y, 1, "John Doc",         0.020, 3.714, 201.19, True,  ["Preston Tanner"])
add("PB", R, Y, 1, "Preston Tanner",   0.066, 3.672, 204.88, False, ["John Doc"])
add("PB", R, Y, 1, "Gabriel Andino",   0.027, 3.704, 202.61, True,  ["Ed Burnley"])
add("PB", R, Y, 1, "Ed Burnley",       0.108, 3.673, 204.70, False, ["Gabriel Andino"])
add("PB", R, Y, 1, "Jason Harris",     0.027, 3.654, 206.80, True,  ["Scott Lang"])
add("PB", R, Y, 1, "Scott Lang",      -0.016, 3.679, 204.88, False, ["Jason Harris"])

add("PB", R, Y, 2, "John Doc",         0.094, 3.716, 201.19, True,  ["Melanie Salemi"])
add("PB", R, Y, 2, "Melanie Salemi",   0.019, 3.940, 170.99, False, ["John Doc"])
add("PB", R, Y, 2, "Kurt Steding",     0.000, 3.687, 206.54, True,  ["Gabriel Andino"])
add("PB", R, Y, 2, "Gabriel Andino",   0.029, 3.717, 202.39, False, ["Kurt Steding"])
add("PB", R, Y, 2, "Ed Marx",          0.081, 3.670, 207.66, True,  ["Johnny Camp"])
add("PB", R, Y, 2, "Johnny Camp",     -0.015, 3.650, 206.54, False, ["Ed Marx"])
add("PB", R, Y, 2, "Jason Harris",     0.033, 3.661, 206.35, True,  ["Randy Weatherford"])
add("PB", R, Y, 2, "Randy Weatherford",0.109, 3.670, 206.73, False, ["Jason Harris"])

add("PB", R, Y, 3, "Kurt Steding",     0.059, 3.653, 206.86, True,  ["John Doc"])
add("PB", R, Y, 3, "John Doc",         0.001, 3.724, 201.46, False, ["Kurt Steding"])
add("PB", R, Y, 3, "Jason Harris",     0.020, 3.640, 206.92, True,  ["Ed Marx"])
add("PB", R, Y, 3, "Ed Marx",         -0.009, 3.636, 208.62, False, ["Jason Harris"])

add("PB", R, Y, 4, "Kurt Steding",     0.007, 3.615, 208.97, True,  ["Jason Harris"])
add("PB", R, Y, 4, "Jason Harris",    -0.123, 3.637, 207.15, False, ["Kurt Steding"])

# -----------------------------------------------------------------
# 2025 North vs South Shootout — MIR, June 14, 2025
# PN: 12-car field. Winner: Fredy Scriba   /   PB winner: Ty Tutterow
# -----------------------------------------------------------------
R, Y = "North vs South Shootout", 2025

add("PN", R, Y, 1, "Fredy Scriba",     0.029, 3.711, 206.57, True,  ["Brian Shrader"])
add("PN", R, Y, 1, "Brian Shrader",    0.008, 3.755, 192.71, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Billy Albert",     0.030, 3.719, 206.20, True,  ["Tony Wilson"])
add("PN", R, Y, 1, "Tony Wilson",      0.026, 3.748, 205.32, False, ["Billy Albert"])
add("PN", R, Y, 1, "Buddy Perkinson",  0.001, 3.689, 205.38, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",     0.080, 3.729, 202.24, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Amber Denton",     0.091, 3.695, 205.51, True,  ["Tim Molnar"])
add("PN", R, Y, 1, "Tim Molnar",      -0.024, 3.715, 205.47, False, ["Amber Denton"])
add("PN", R, Y, 1, "Dane Wood",        0.038, 3.697, 204.66, True,  ["Tim Paap"])
add("PN", R, Y, 1, "Tim Paap",         0.071, 3.693, 203.06, False, ["Dane Wood"])
add("PN", R, Y, 1, "Tommy Franklin",   0.006, 3.673, 207.24, True,  ["Marcus Butner"])
add("PN", R, Y, 1, "Marcus Butner",    0.063, 3.693, 206.61, False, ["Tommy Franklin"])

add("PN", R, Y, 2, "Billy Albert",     0.025, 3.733, 206.10, True,  ["Dane Wood"])
add("PN", R, Y, 2, "Dane Wood",        0.009, 3.889, 204.39, False, ["Billy Albert"])
add("PN", R, Y, 2, "Buddy Perkinson",  0.014, 3.731, 204.01, True,  ["Amber Denton"])
# Denton BROKE; no times
add("PN", R, Y, 2, "Fredy Scriba",     0.007, 3.720, 207.82, True,  ["Tommy Franklin"])
add("PN", R, Y, 2, "Tommy Franklin",   0.092, 4.095, 140.77, False, ["Fredy Scriba"])

add("PN", R, Y, 3, "Billy Albert",     0.019, 3.741, 206.32, True,  ["Buddy Perkinson"])
add("PN", R, Y, 3, "Buddy Perkinson",  0.035, 3.733, 204.01, False, ["Billy Albert"])
add("PN", R, Y, 3, "Fredy Scriba",     0.039, 3.738, 206.07, True,  [])  # SINGLE

add("PN", R, Y, 4, "Fredy Scriba",     0.011, 3.712, 206.29, True,  ["Billy Albert"])
add("PN", R, Y, 4, "Billy Albert",     0.025, 3.727, 206.42, False, ["Fredy Scriba"])

add("PB", R, Y, 1, "Randy Weatherford",0.028, 3.684, 206.39, True,  ["Travis Harvey"])
add("PB", R, Y, 1, "Travis Harvey",    0.034, 3.733, 190.30, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Chuck Ulsch",      0.006, 3.675, 205.51, True,  ["Tommy Gray"])
add("PB", R, Y, 1, "Tommy Gray",       0.048, 3.664, 206.54, False, ["Chuck Ulsch"])
add("PB", R, Y, 1, "Ty Tutterow",      0.021, 3.703, 207.50, True,  ["Ed Burnley"])
add("PB", R, Y, 1, "Ed Burnley",       0.059, 3.695, 201.58, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "John Doc",         0.008, 3.694, 204.73, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",     0.089, 3.713, 205.19, False, ["John Doc"])
add("PB", R, Y, 1, "Melanie Salemi",   0.023, 3.620, 208.26, True,  ["Preston Tanner"])
add("PB", R, Y, 1, "Preston Tanner",  -0.149, 3.655, 205.94, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Jason Harris",     0.009, 3.664, 205.94, True,  ["Jason Lee"])
add("PB", R, Y, 1, "Jason Lee",        0.035, 6.760,  67.31, False, ["Jason Harris"])
add("PB", R, Y, 1, "Johnny Camp",      0.004, 3.650, 205.94, True,  ["Scott Lang"])
add("PB", R, Y, 1, "Scott Lang",       0.011, 3.695, 205.41, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Steve King",       0.046, 3.653, 206.67, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",   -0.012, 3.704, 203.19, False, ["Steve King"])

add("PB", R, Y, 2, "Ty Tutterow",      0.002, 3.685, 206.95, True,  ["Jason Harris"])
add("PB", R, Y, 2, "Jason Harris",     0.015, 7.134,  62.75, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Steve King",       0.038, 3.698, 207.69, True,  ["Randy Weatherford"])
add("PB", R, Y, 2, "Randy Weatherford",0.031, 5.232, 111.00, False, ["Steve King"])
add("PB", R, Y, 2, "Johnny Camp",      0.037, 3.697, 205.07, True,  ["Chuck Ulsch"])
add("PB", R, Y, 2, "Chuck Ulsch",      0.026, 5.076,  97.36, False, ["Johnny Camp"])
add("PB", R, Y, 2, "John Doc",        -0.014, 3.712, 203.52, True,  ["Melanie Salemi"])
add("PB", R, Y, 2, "Melanie Salemi",  -0.079, 5.165,  94.86, False, ["John Doc"])

add("PB", R, Y, 3, "Steve King",       0.044, 3.701, 205.22, True,  ["John Doc"])
add("PB", R, Y, 3, "John Doc",        -0.191, 3.719, 202.00, False, ["Steve King"])
add("PB", R, Y, 3, "Ty Tutterow",      0.026, 3.693, 205.98, True,  ["Johnny Camp"])
add("PB", R, Y, 3, "Johnny Camp",      0.035, 3.705, 205.47, False, ["Ty Tutterow"])

add("PB", R, Y, 4, "Ty Tutterow",      0.024, 3.667, 206.54, True,  ["Steve King"])
add("PB", R, Y, 4, "Steve King",       0.042, 3.680, 205.35, False, ["Ty Tutterow"])

# -----------------------------------------------------------------
# 2025 Northern Nationals — US 131 Motorsports Park, August 3, 2025
# PN: 12-car field. Winner: Amber Denton   /   PB winner: Randy Weatherford
# -----------------------------------------------------------------
R, Y = "Northern Nationals", 2025

add("PN", R, Y, 1, "Buddy Perkinson",  0.012, 3.687, 202.98, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",     0.036, 3.706, 201.43, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Fredy Scriba",     0.003, 3.687, 203.71, True,  ["Tim Molnar"])
add("PN", R, Y, 1, "Tim Molnar",       0.020, 3.684, 205.39, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Tommy Franklin",   0.014, 3.714, 187.50, True,  ["Tony Wilson"])
# Tony Wilson DQ-LB3A; no clean RT/ET
add("PN", R, Y, 1, "Marcus Butner",    0.012, 3.661, 207.18, True,  ["Corey Smith"])
add("PN", R, Y, 1, "Corey Smith",      0.036, 3.715, 201.61, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Billy Albert",     0.026, 3.670, 205.67, True,  ["Dane Wood"])
add("PN", R, Y, 1, "Dane Wood",        0.011, 6.487,  70.52, False, ["Billy Albert"])
add("PN", R, Y, 1, "Amber Denton",     0.055, 3.666, 206.42, True,  ["Jackie Slone Jr"])
add("PN", R, Y, 1, "Jackie Slone Jr",  0.010, 3.772, 203.62, False, ["Amber Denton"])
add("PN", R, Y, 1, "Tim Paap",         0.058, 3.656, 206.23, True,  [])  # SINGLE

add("PN", R, Y, 2, "Billy Albert",     0.014, 3.694, 204.64, True,  ["Fredy Scriba"])
add("PN", R, Y, 2, "Fredy Scriba",     0.010, 3.706, 205.95, False, ["Billy Albert"])
add("PN", R, Y, 2, "Amber Denton",     0.052, 3.692, 205.76, True,  [])  # SINGLE
add("PN", R, Y, 2, "Tommy Franklin",   0.025, 4.636, 113.58, True,  ["Marcus Butner"])
add("PN", R, Y, 2, "Marcus Butner",   -0.007, 3.776, 173.64, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Tim Paap",         0.012, 3.667, 206.52, True,  ["Buddy Perkinson"])
add("PN", R, Y, 2, "Buddy Perkinson",  0.024, 3.712, 205.76, False, ["Tim Paap"])

add("PN", R, Y, 3, "Amber Denton",     0.029, 3.662, 195.23, True,  ["Billy Albert"])
add("PN", R, Y, 3, "Billy Albert",     0.081, 3.642, 208.14, False, ["Amber Denton"])
add("PN", R, Y, 3, "Tommy Franklin",   0.053, 3.723, 176.40, True,  ["Tim Paap"])
# Tim Paap DQ-LB3A in R3; no RT

add("PN", R, Y, 4, "Amber Denton",     0.200, 5.441, 147.49, True,  ["Tommy Franklin"])
add("PN", R, Y, 4, "Tommy Franklin",   0.178, 5.469, 149.01, False, ["Amber Denton"])

add("PB", R, Y, 1, "Steve King",       0.014, 3.619, 206.52, True,  ["Cameron Hensley"])
add("PB", R, Y, 1, "Cameron Hensley",  0.045, 3.645, 205.10, False, ["Steve King"])
add("PB", R, Y, 1, "Preston Tanner",   0.031, 3.599, 207.66, True,  ["Jason Lee"])
# Jason Lee DQ-LB3A in R1
add("PB", R, Y, 1, "Johnny Camp",      0.003, 3.651, 206.14, True,  ["John Doc"])
add("PB", R, Y, 1, "John Doc",         0.044, 3.657, 204.17, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Melanie Salemi",   0.006, 3.641, 207.73, True,  ["Jay Cox"])
add("PB", R, Y, 1, "Jay Cox",          0.038, 3.674, 217.29, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Jason Harris",     0.075, 3.610, 208.91, True,  ["James Beadling"])
add("PB", R, Y, 1, "James Beadling",  -0.001, 3.667, 206.80, False, ["Jason Harris"])
add("PB", R, Y, 1, "Ty Tutterow",      0.023, 3.612, 209.40, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",    0.001, 3.931, 151.77, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Kurt Steding",     0.017, 3.639, 209.40, True,  ["Joel Wensley Sr"])
add("PB", R, Y, 1, "Joel Wensley Sr",  0.177, 7.119,  64.73, False, ["Kurt Steding"])
add("PB", R, Y, 1, "Randy Weatherford",0.173, 4.171, 128.87, True,  [])  # SINGLE

add("PB", R, Y, 2, "Randy Weatherford",0.016, 3.604, 211.37, True,  ["Steve King"])
add("PB", R, Y, 2, "Steve King",       0.000, 4.992,  99.54, False, ["Randy Weatherford"])
add("PB", R, Y, 2, "Ty Tutterow",      0.036, 3.626, 208.04, True,  ["Johnny Camp"])
add("PB", R, Y, 2, "Johnny Camp",      0.010, 3.659, 206.71, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Jason Harris",     0.062, 3.648, 203.16, True,  ["Melanie Salemi"])
add("PB", R, Y, 2, "Melanie Salemi",   0.060, 7.094,  62.99, False, ["Jason Harris"])
add("PB", R, Y, 2, "Preston Tanner",   0.045, 3.631, 206.80, True,  ["Kurt Steding"])
add("PB", R, Y, 2, "Kurt Steding",    -0.004, 3.637, 209.21, False, ["Preston Tanner"])

add("PB", R, Y, 3, "Ty Tutterow",      0.028, 3.592, 208.24, True,  ["Preston Tanner"])
add("PB", R, Y, 3, "Preston Tanner",   0.018, 3.620, 206.90, False, ["Ty Tutterow"])
add("PB", R, Y, 3, "Randy Weatherford",0.005, 3.580, 211.37, True,  ["Jason Harris"])
add("PB", R, Y, 3, "Jason Harris",     0.041, 3.595, 209.01, False, ["Randy Weatherford"])

add("PB", R, Y, 4, "Randy Weatherford",0.042, 3.579, 211.07, True,  ["Ty Tutterow"])
add("PB", R, Y, 4, "Ty Tutterow",     -0.017, 3.576, 209.40, False, ["Randy Weatherford"])

# -----------------------------------------------------------------
# 2025 Thunder Valley Throwdown — Bristol, August 22, 2025
# PN: 12-car field. Winner: Tommy Franklin   /   PB winner: Ty Tutterow
# -----------------------------------------------------------------
R, Y = "Thunder Valley Throwdown", 2025

add("PN", R, Y, 1, "Brian Shrader",    0.025, 3.968, 194.30, True,  ["Tim Paap"])
add("PN", R, Y, 1, "Tim Paap",        -0.003, 5.524,  87.32, False, ["Brian Shrader"])
add("PN", R, Y, 1, "Tim Molnar",       0.062, 3.825, 199.76, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",    -0.094, 5.502,  88.11, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Cam Clark",        0.067, 3.826, 197.33, True,  ["Amber Denton"])
add("PN", R, Y, 1, "Amber Denton",     0.022, 4.208, 185.08, False, ["Cam Clark"])
add("PN", R, Y, 1, "Marcus Butner",    0.047, 3.806, 203.43, True,  ["Fredy Scriba"])
add("PN", R, Y, 1, "Fredy Scriba",     0.077, 3.779, 201.94, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Dane Wood",        0.050, 3.761, 199.82, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",     0.071, 3.760, 201.52, False, ["Dane Wood"])
add("PN", R, Y, 1, "Tommy Franklin",   0.066, 3.907, 162.65, True,  [])  # SINGLE

add("PN", R, Y, 2, "Tommy Franklin",   0.020, 3.660, 206.80, True,  ["Brian Shrader"])
add("PN", R, Y, 2, "Brian Shrader",    0.032, 3.689, 202.97, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Marcus Butner",    0.023, 3.628, 209.10, True,  ["Cam Clark"])
add("PN", R, Y, 2, "Cam Clark",        0.067, 3.781, 183.89, False, ["Marcus Butner"])
add("PN", R, Y, 2, "Tim Molnar",       0.015, 3.702, 204.48, True,  ["Dane Wood"])
add("PN", R, Y, 2, "Dane Wood",       -0.347, 4.593, 131.84, False, ["Tim Molnar"])

add("PN", R, Y, 3, "Tim Molnar",       0.022, 3.811, 162.61, True,  [])  # SINGLE
add("PN", R, Y, 3, "Tommy Franklin",   0.076, 3.623, 207.43, True,  ["Marcus Butner"])
add("PN", R, Y, 3, "Marcus Butner",    0.071, 3.628, 209.10, False, ["Tommy Franklin"])

add("PN", R, Y, 4, "Tommy Franklin",   0.045, 3.626, 207.08, True,  ["Tim Molnar"])
add("PN", R, Y, 4, "Tim Molnar",       0.030, 3.681, 205.98, False, ["Tommy Franklin"])

add("PB", R, Y, 1, "Ed Marx",          0.004, 3.715, 204.26, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",     0.034, 3.727, 203.25, False, ["Ed Marx"])
add("PB", R, Y, 1, "Steve King",       0.047, 3.732, 202.06, True,  ["Frank Falter IV"])
add("PB", R, Y, 1, "Frank Falter IV",  0.063, 3.803, 196.33, False, ["Steve King"])
add("PB", R, Y, 1, "Ty Tutterow",      0.051, 3.734, 203.31, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",   -0.004, 32.000, 0.00,  False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Melanie Salemi",   0.025, 3.709, 200.98, True,  ["Cameron Hensley"])
add("PB", R, Y, 1, "Cameron Hensley",  0.030, 4.550, 115.73, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "David Monday",     0.025, 5.202, 107.46, True,  ["Johnny Camp"])
add("PB", R, Y, 1, "Johnny Camp",     -0.045, 3.714, 202.97, False, ["David Monday"])
add("PB", R, Y, 1, "Randy Weatherford",0.028, 3.714, 207.56, True,  ["John Doc"])
add("PB", R, Y, 1, "John Doc",         0.028, 3.722, 201.49, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Jason Harris",     0.085, 3.686, 205.51, True,  ["Dan Tolley"])
add("PB", R, Y, 1, "Dan Tolley",      -0.171, 5.928,  73.17, False, ["Jason Harris"])
add("PB", R, Y, 1, "Preston Tanner",   0.053, 3.688, 203.19, True,  ["Bubba Greene"])
add("PB", R, Y, 1, "Bubba Greene",     0.014, 5.269,  95.58, False, ["Preston Tanner"])

add("PB", R, Y, 2, "Ty Tutterow",      0.013, 3.589, 208.75, True,  ["Randy Weatherford"])
add("PB", R, Y, 2, "Randy Weatherford",0.031, 3.593, 209.39, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Melanie Salemi",   0.027, 3.615, 206.20, True,  ["David Monday"])
# David Monday BROKE; no times
add("PB", R, Y, 2, "Ed Marx",          0.032, 5.180,  92.55, True,  ["Preston Tanner"])
# Preston Tanner BROKE; no times
add("PB", R, Y, 2, "Jason Harris",     0.014, 3.572, 208.26, True,  ["Steve King"])
add("PB", R, Y, 2, "Steve King",       0.023, 3.640, 204.60, False, ["Jason Harris"])

add("PB", R, Y, 3, "Melanie Salemi",   0.029, 3.599, 206.89, True,  ["Ed Marx"])
add("PB", R, Y, 3, "Ed Marx",          0.057, 4.579, 111.78, False, ["Melanie Salemi"])
add("PB", R, Y, 3, "Ty Tutterow",      0.014, 3.577, 209.95, True,  ["Jason Harris"])
add("PB", R, Y, 3, "Jason Harris",    -0.004, 3.562, 208.23, False, ["Ty Tutterow"])

add("PB", R, Y, 4, "Ty Tutterow",      0.031, 3.580, 209.52, True,  ["Melanie Salemi"])
add("PB", R, Y, 4, "Melanie Salemi",   0.035, 3.588, 206.92, False, ["Ty Tutterow"])

# -----------------------------------------------------------------
# 2025 Drag Wars — GALOT, September 13, 2025
# PN: 12-car field. Winner: Marcus Butner   /   PB winner: Ty Tutterow
# -----------------------------------------------------------------
R, Y = "DragWars", 2025

add("PN", R, Y, 1, "Fredy Scriba",     0.015, 4.274, 127.70, True,  ["Amber Denton"])
add("PN", R, Y, 1, "Amber Denton",    -0.024, 3.687, 206.51, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Tim Molnar",       0.027, 3.689, 205.32, True,  ["Brian Shrader"])
add("PN", R, Y, 1, "Brian Shrader",    0.022, 3.700, 203.40, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Dane Wood",        0.031, 3.703, 202.64, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",    -0.119, 3.681, 207.11, False, ["Dane Wood"])
add("PN", R, Y, 1, "Chris Rini",       1.270, 3.724, 202.24, True,  ["Tim Paap"])
# Tim Paap BROKE; no times
add("PN", R, Y, 1, "Marcus Butner",    0.043, 3.666, 206.99, True,  ["Cam Clark"])
add("PN", R, Y, 1, "Cam Clark",        0.033, 3.742, 199.40, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Tommy Franklin",   0.013, 4.871, 103.37, True,  ["Edward Wilson"])
add("PN", R, Y, 1, "Edward Wilson",    0.114, 5.993,  76.76, False, ["Tommy Franklin"])

add("PN", R, Y, 2, "Tommy Franklin",   0.023, 3.679, 205.38, True,  ["Fredy Scriba"])
add("PN", R, Y, 2, "Fredy Scriba",     0.020, 3.709, 204.73, False, ["Tommy Franklin"])
add("PN", R, Y, 2, "Dane Wood",        0.017, 3.725, 202.24, True,  ["Chris Rini"])
# Chris Rini BROKE; no times
add("PN", R, Y, 2, "Marcus Butner",    0.030, 3.684, 207.08, True,  ["Tim Molnar"])
add("PN", R, Y, 2, "Tim Molnar",       0.031, 3.688, 204.70, False, ["Marcus Butner"])

add("PN", R, Y, 3, "Marcus Butner",    0.013, 3.640, 207.50, True,  ["Dane Wood"])
add("PN", R, Y, 3, "Dane Wood",        0.002, 3.711, 201.40, False, ["Marcus Butner"])
add("PN", R, Y, 3, "Tommy Franklin",   0.186, 5.016,  98.98, True,  [])  # SINGLE

add("PN", R, Y, 4, "Marcus Butner",    0.107, 3.634, 207.78, True,  ["Tommy Franklin"])
add("PN", R, Y, 4, "Tommy Franklin",   0.086, 3.666, 203.71, False, ["Marcus Butner"])

add("PB", R, Y, 1, "Jason Lee",        0.012, 3.672, 206.10, True,  ["John Doc"])
add("PB", R, Y, 1, "John Doc",        -0.003, 3.638, 208.39, False, ["Jason Lee"])
add("PB", R, Y, 1, "Ed Marx",          0.025, 3.612, 209.69, True,  ["Scott Lang"])
add("PB", R, Y, 1, "Scott Lang",      -0.026, 3.634, 201.25, False, ["Ed Marx"])
add("PB", R, Y, 1, "Melanie Salemi",   0.041, 3.586, 207.46, True,  ["Steve King"])
add("PB", R, Y, 1, "Steve King",       0.015, 3.638, 201.79, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Randy Weatherford",0.037, 3.611, 209.52, True,  ["Cameron Hensley"])
add("PB", R, Y, 1, "Cameron Hensley",  0.031, 3.645, 205.98, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Raymond Matos",    0.012, 3.644, 206.23, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",    -0.009, 3.622, 207.59, False, ["Raymond Matos"])
add("PB", R, Y, 1, "Johnny Camp",      0.034, 3.612, 207.18, True,  ["Frank Falter IV"])
add("PB", R, Y, 1, "Frank Falter IV", -0.015, 3.686, 201.49, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Jason Harris",     0.051, 3.610, 208.65, True,  ["Dan Tolley"])
add("PB", R, Y, 1, "Dan Tolley",       0.051, 3.743, 201.31, False, ["Jason Harris"])
add("PB", R, Y, 1, "Ty Tutterow",      0.017, 3.608, 208.88, True,  ["Bubba Greene"])
add("PB", R, Y, 1, "Bubba Greene",     0.028, 3.751, 199.76, False, ["Ty Tutterow"])

add("PB", R, Y, 2, "Randy Weatherford",0.017, 3.631, 208.94, True,  ["Raymond Matos"])
add("PB", R, Y, 2, "Raymond Matos",    0.013, 3.729, 203.12, False, ["Randy Weatherford"])
add("PB", R, Y, 2, "Ed Marx",          0.003, 3.627, 205.44, True,  ["Jason Harris"])
add("PB", R, Y, 2, "Jason Harris",     0.041, 3.590, 209.14, False, ["Ed Marx"])
add("PB", R, Y, 2, "Ty Tutterow",      0.020, 3.590, 207.72, True,  ["Jason Lee"])
add("PB", R, Y, 2, "Jason Lee",        0.038, 4.590, 112.05, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Melanie Salemi",   0.040, 3.617, 193.24, True,  ["Johnny Camp"])
add("PB", R, Y, 2, "Johnny Camp",      0.019, 3.708, 178.68, False, ["Melanie Salemi"])

add("PB", R, Y, 3, "Melanie Salemi",   0.031, 3.583, 207.88, True,  ["Ed Marx"])
add("PB", R, Y, 3, "Ed Marx",          0.053, 4.579, 111.78, False, ["Melanie Salemi"])
add("PB", R, Y, 3, "Ty Tutterow",      0.024, 3.568, 209.49, True,  ["Randy Weatherford"])
add("PB", R, Y, 3, "Randy Weatherford",-0.001,3.601, 209.30, False, ["Ty Tutterow"])

add("PB", R, Y, 4, "Ty Tutterow",      0.011, 3.561, 209.95, True,  ["Melanie Salemi"])
add("PB", R, Y, 4, "Melanie Salemi",   0.009, 11.113, 37.29, False, ["Ty Tutterow"])

# -----------------------------------------------------------------
# 2025 Brian Olson Memorial World Finals — VMP, October 5, 2025
# PN: 14-car field. Winner: Marcus Butner   /   PB winner: Jason Harris
# -----------------------------------------------------------------
R, Y = "Brian Olson Memorial World Finals", 2025

add("PN", R, Y, 1, "Buddy Perkinson",  0.007, 3.641, 206.86, True,  ["Tim Molnar"])
add("PN", R, Y, 1, "Tim Molnar",       0.028, 3.681, 204.85, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Marcus Butner",    0.048, 3.603, 209.98, True,  ["Chris Rini"])
add("PN", R, Y, 1, "Chris Rini",       0.043, 3.674, 205.63, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Billy Albert",     0.028, 3.654, 208.10, True,  ["Matthew Deitsch"])
add("PN", R, Y, 1, "Matthew Deitsch",  0.049, 3.694, 205.01, False, ["Billy Albert"])
add("PN", R, Y, 1, "Amber Denton",     0.048, 3.615, 208.65, True,  ["Dane Wood"])
add("PN", R, Y, 1, "Dane Wood",        0.017, 3.690, 202.03, False, ["Amber Denton"])
add("PN", R, Y, 1, "Tommy Franklin",   0.023, 3.611, 209.17, True,  ["Brian Shrader"])
add("PN", R, Y, 1, "Brian Shrader",   -0.018, 4.038, 145.25, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Cam Clark",        0.052, 3.700, 201.58, True,  ["Tim Paap"])
add("PN", R, Y, 1, "Tim Paap",         0.087, 4.485, 115.85, False, ["Cam Clark"])
add("PN", R, Y, 1, "Fredy Scriba",     0.047, 3.633, 207.62, True,  [])  # SINGLE

add("PN", R, Y, 2, "Cam Clark",        0.046, 4.444, 119.26, True,  [])  # SINGLE
add("PN", R, Y, 2, "Buddy Perkinson",  0.016, 3.704, 204.32, True,  ["Fredy Scriba"])
add("PN", R, Y, 2, "Fredy Scriba",     0.014, 6.573,  69.87, False, ["Buddy Perkinson"])
add("PN", R, Y, 2, "Billy Albert",     0.062, 4.219, 148.74, True,  ["Amber Denton"])
add("PN", R, Y, 2, "Amber Denton",     0.057, 6.594,  69.15, False, ["Billy Albert"])
add("PN", R, Y, 2, "Marcus Butner",    0.042, 3.671, 208.10, True,  ["Tommy Franklin"])
add("PN", R, Y, 2, "Tommy Franklin",   0.044, 3.681, 206.57, False, ["Marcus Butner"])

add("PN", R, Y, 3, "Buddy Perkinson",  0.063, 3.679, 205.82, True,  ["Billy Albert"])
add("PN", R, Y, 3, "Billy Albert",     0.025, 3.719, 206.83, False, ["Buddy Perkinson"])
add("PN", R, Y, 3, "Marcus Butner",    0.029, 3.688, 206.86, True,  ["Cam Clark"])
add("PN", R, Y, 3, "Cam Clark",        0.047, 3.723, 200.44, False, ["Marcus Butner"])

add("PN", R, Y, 4, "Marcus Butner",    0.009, 3.647, 207.53, True,  ["Buddy Perkinson"])
add("PN", R, Y, 4, "Buddy Perkinson",  0.009, 3.660, 205.91, False, ["Marcus Butner"])

add("PB", R, Y, 1, "Ed Burnley",       0.007, 3.612, 205.98, True,  ["Cameron Hensley"])
add("PB", R, Y, 1, "Cameron Hensley",  0.052, 3.599, 209.14, False, ["Ed Burnley"])
add("PB", R, Y, 1, "Kurt Steding",     0.106, 3.600, 209.36, True,  ["Jay Cox"])
add("PB", R, Y, 1, "Jay Cox",          0.044, 3.971, 140.34, False, ["Kurt Steding"])
add("PB", R, Y, 1, "John Doc",         0.029, 3.671, 181.30, True,  ["Jason Lee"])
add("PB", R, Y, 1, "Jason Lee",       -0.079, 3.686, 184.85, False, ["John Doc"])
add("PB", R, Y, 1, "Ty Tutterow",      0.010, 3.567, 210.97, True,  ["Johnny Camp"])
add("PB", R, Y, 1, "Johnny Camp",      0.032, 3.574, 208.26, False, ["Ty Tutterow"])
add("PB", R, Y, 1, "Melanie Salemi",   0.057, 3.574, 208.62, True,  ["Scott Lang"])
add("PB", R, Y, 1, "Scott Lang",       0.057, 3.601, 205.82, False, ["Melanie Salemi"])
add("PB", R, Y, 1, "Jason Harris",     0.015, 3.564, 210.08, True,  ["Frank Falter IV"])
add("PB", R, Y, 1, "Frank Falter IV",  0.050, 3.613, 206.61, False, ["Jason Harris"])
add("PB", R, Y, 1, "Steve King",       0.130, 3.586, 218.55, True,  ["Joel Wensley"])
# Joel Wensley BROKE; no times
add("PB", R, Y, 1, "Randy Weatherford",0.023, 3.556, 212.69, True,  ["Chuck Ulsch"])
add("PB", R, Y, 1, "Chuck Ulsch",      0.069, 3.626, 209.72, False, ["Randy Weatherford"])

add("PB", R, Y, 2, "Kurt Steding",     0.006, 3.661, 207.11, True,  ["Steve King"])
add("PB", R, Y, 2, "Steve King",       0.014, 5.202,  93.97, False, ["Kurt Steding"])
add("PB", R, Y, 2, "Ty Tutterow",      0.033, 3.706, 206.20, True,  ["Melanie Salemi"])
add("PB", R, Y, 2, "Melanie Salemi",   0.026, 4.195, 139.17, False, ["Ty Tutterow"])
add("PB", R, Y, 2, "Jason Harris",     0.034, 3.601, 208.71, True,  ["John Doc"])
add("PB", R, Y, 2, "John Doc",         0.030, 3.646, 208.01, False, ["Jason Harris"])
add("PB", R, Y, 2, "Randy Weatherford",0.089, 3.615, 210.80, True,  ["Ed Burnley"])
add("PB", R, Y, 2, "Ed Burnley",       0.094, 4.818, 102.04, False, ["Randy Weatherford"])

add("PB", R, Y, 3, "Jason Harris",     0.021, 3.651, 186.46, True,  ["Kurt Steding"])
# Kurt Steding BROKE in R3; no times
add("PB", R, Y, 3, "Ty Tutterow",      0.009, 3.601, 209.65, True,  ["Randy Weatherford"])
add("PB", R, Y, 3, "Randy Weatherford",0.045, 8.868,  35.56, False, ["Ty Tutterow"])

add("PB", R, Y, 4, "Jason Harris",     0.020, 3.586, 209.20, True,  ["Ty Tutterow"])
add("PB", R, Y, 4, "Ty Tutterow",     -0.041, 3.588, 209.46, False, ["Jason Harris"])

# ============================================================================
# 2026 MIR — PDRA North vs. South Shootout, June 25-27, 2026, Budds Creek, MD
# Source: CompuLink StarTrak elimination PNGs, 27/JUN/2026
# ============================================================================
R, Y = "North vs South Shootout", 2026

# --- PRO NITROUS ---
# Round 1 (6 pairs)
add("PN", R, Y, 1, "Fredy Scriba",     0.015, 3.652, 206.48, True,  ["Rickie Smith"])
add("PN", R, Y, 1, "Rickie Smith",     0.008, 3.699, 205.26, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Tommy Franklin",   0.019, 3.650, 206.83, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",     0.024, 3.684, 206.04, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Buddy Perkinson",  0.007, 3.652, 205.85, True,  ["Chris Rini"])
add("PN", R, Y, 1, "Chris Rini",       0.035, 10.502, 39.72, False, ["Buddy Perkinson"])
add("PN", R, Y, 1, "Marcus Butner",    0.044, 3.693, 205.76, True,  ["Mike Achenbach"])
add("PN", R, Y, 1, "Mike Achenbach",   0.086, 3.694, 205.44, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Dane Wood",        0.009, 3.701, 205.22, True,  ["Amber Denton"])
add("PN", R, Y, 1, "Amber Denton",     0.075, 3.656, 207.24, False, ["Dane Wood"])
add("PN", R, Y, 1, "Tim Paap",         0.076, 3.670, 204.94, True,  ["Dale Brinsfield"])
add("PN", R, Y, 1, "Dale Brinsfield",  0.015, 3.741, 202.45, False, ["Tim Paap"])
# Round 2 (3 pairs)
add("PN", R, Y, 2, "Buddy Perkinson",  0.009, 3.691, 204.45, True,  ["Marcus Butner"])
add("PN", R, Y, 2, "Marcus Butner",    0.039, 3.699, 206.54, False, ["Buddy Perkinson"])
add("PN", R, Y, 2, "Fredy Scriba",     0.020, 3.661, 206.54, True,  ["Tim Paap"])
add("PN", R, Y, 2, "Tim Paap",         0.049, 3.659, 205.76, False, ["Fredy Scriba"])
add("PN", R, Y, 2, "Dane Wood",        0.010, 3.684, 206.45, True,  ["Tommy Franklin"])
add("PN", R, Y, 2, "Tommy Franklin",   0.042, 3.680, 206.39, False, ["Dane Wood"])
# Round 3 (Semis — 1 pair + 1 single)
add("PN", R, Y, 3, "Buddy Perkinson",  0.036, 3.657, 205.88, True,  ["Dane Wood"])
add("PN", R, Y, 3, "Dane Wood",       -0.014, 3.667, 206.86, False, ["Buddy Perkinson"])
add("PN", R, Y, 3, "Fredy Scriba",     1.228, 9.311,  93.78, True,  [])  # Single
# Finals
add("PN", R, Y, 4, "Fredy Scriba",     0.024, 3.653, 207.72, True,  ["Buddy Perkinson"])
add("PN", R, Y, 4, "Buddy Perkinson", -0.011, 3.656, 206.73, False, ["Fredy Scriba"])

# --- PRO BOOST ---
# Round 1 (8 pairs)
add("PB", R, Y, 1, "Derek Ward",       0.024, 3.644, 208.55, True,  ["Gabriel Andino"])
add("PB", R, Y, 1, "Gabriel Andino",   0.030, 3.657, 204.73, False, ["Derek Ward"])
add("PB", R, Y, 1, "Mike Decker III",  0.037, 3.649, 205.91, True,  ["Ethan Steding"])
add("PB", R, Y, 1, "Ethan Steding",    0.053, 5.444,  87.66, False, ["Mike Decker III"])
add("PB", R, Y, 1, "Mike Decker Jr.",  0.063, 3.657, 204.91, True,  ["Ed Burnley"])
add("PB", R, Y, 1, "Ed Burnley",       0.067, 3.749, 170.06, False, ["Mike Decker Jr."])
add("PB", R, Y, 1, "Fletcher Cox",     0.012, 3.627, 207.75, True,  ["Frank Falter IV"])
add("PB", R, Y, 1, "Frank Falter IV",  0.032, 3.693, 204.98, False, ["Fletcher Cox"])
add("PB", R, Y, 1, "Raymond Matos",    0.160, 3.622, 209.62, True,  ["Don Tolley"])
add("PB", R, Y, 1, "Don Tolley",       0.029, 3.770, 202.09, False, ["Raymond Matos"])
add("PB", R, Y, 1, "Travis Harvey",    0.055, 3.610, 208.84, True,  ["Joel Wensley"])
add("PB", R, Y, 1, "Joel Wensley",     0.056, 3.668, 208.10, False, ["Travis Harvey"])
add("PB", R, Y, 1, "Jason Harris",     0.107, 3.605, 210.87, True,  ["Andy Jensen"])
add("PB", R, Y, 1, "Andy Jensen",      0.031, 3.967, 194.72, False, ["Jason Harris"])
add("PB", R, Y, 1, "Ty Tutterow",      0.035, 3.588, 207.94, True,  ["Dwayne Wolfe"])
add("PB", R, Y, 1, "Dwayne Wolfe",     0.077, 3.892, 168.81, False, ["Ty Tutterow"])
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Travis Harvey",    0.012, 3.616, 208.81, True,  ["Mike Decker Jr."])
add("PB", R, Y, 2, "Mike Decker Jr.",  0.045, 3.751, 200.26, False, ["Travis Harvey"])
add("PB", R, Y, 2, "Raymond Matos",    0.079, 3.642, 208.94, True,  ["Fletcher Cox"])
add("PB", R, Y, 2, "Fletcher Cox",    -0.001, 0.000,   0.00, False, ["Raymond Matos"])  # foul + broke
add("PB", R, Y, 2, "Jason Harris",     0.029, 3.623, 208.59, True,  ["Mike Decker III"])
add("PB", R, Y, 2, "Mike Decker III",  0.212, 6.802,  65.86, False, ["Jason Harris"])
add("PB", R, Y, 2, "Derek Ward",       0.024, 3.648, 208.52, True,  ["Ty Tutterow"])
add("PB", R, Y, 2, "Ty Tutterow",      0.166, 3.589, 208.62, False, ["Derek Ward"])
# Round 3 (Semis)
add("PB", R, Y, 3, "Travis Harvey",    0.022, 3.610, 208.46, True,  ["Jason Harris"])
add("PB", R, Y, 3, "Jason Harris",     0.043, 3.603, 210.97, False, ["Travis Harvey"])
add("PB", R, Y, 3, "Derek Ward",       0.036, 3.633, 208.52, True,  ["Raymond Matos"])
add("PB", R, Y, 3, "Raymond Matos",    0.021, 5.731,  73.66, False, ["Derek Ward"])
# Finals
add("PB", R, Y, 4, "Travis Harvey",    0.023, 3.595, 209.36, True,  ["Derek Ward"])
add("PB", R, Y, 4, "Derek Ward",       0.043, 3.624, 207.75, False, ["Travis Harvey"])

# ============================================================================
# 2026 BRISTOL — PDRA Thunder Valley Throwdown, August 6-8, 2026
# Source: CompuLink StarTrak elimination PNGs, 8/AUG/2026
# ============================================================================
R, Y = "Thunder Valley Throwdown", 2026

# --- PRO NITROUS ---
# Round 1 (6 pairs + 1 single)
add("PN", R, Y, 1, "Amber Denton",     0.008, 3.703, 205.22, True,  ["Buddy Perkinson"])
add("PN", R, Y, 1, "Buddy Perkinson",  0.034, 3.704, 203.80, False, ["Amber Denton"])
add("PN", R, Y, 1, "Dane Wood",        0.028, 3.739, 200.00, True,  ["Fredy Scriba"])
add("PN", R, Y, 1, "Fredy Scriba",     0.026, 5.384,  90.67, False, ["Dane Wood"])
add("PN", R, Y, 1, "Tim Paap",         0.028, 3.705, 202.48, True,  ["Edward Wilson"])
add("PN", R, Y, 1, "Edward Wilson",    0.028, 3.784, 196.99, False, ["Tim Paap"])
add("PN", R, Y, 1, "Billy Albert",     0.037, 4.167, 167.80, True,  ["Brian Teachman"])
add("PN", R, Y, 1, "Brian Teachman",   0.052, 6.191,  76.10, False, ["Billy Albert"])
add("PN", R, Y, 1, "Dale Brinsfield",  0.062, 3.767, 200.89, True,  ["Rickie Smith"])
add("PN", R, Y, 1, "Rickie Smith",     0.040, 3.984, 188.46, False, ["Dale Brinsfield"])
add("PN", R, Y, 1, "Tommy Franklin",   0.072, 4.071, 146.59, True,  ["Jimmy Cowan"])
add("PN", R, Y, 1, "Jimmy Cowan",      0.452, 7.540, 108.06, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Marcus Butner",    0.059, 3.696, 204.76, True,  [])  # Single
# Round 2 (3 pairs + 1 single)
add("PN", R, Y, 2, "Tommy Franklin",   0.091, 4.483, 116.65, True,  [])  # Single
add("PN", R, Y, 2, "Dane Wood",        0.020, 3.716, 204.75, True,  ["Dale Brinsfield"])
add("PN", R, Y, 2, "Dale Brinsfield",  0.031, 4.129, 140.85, False, ["Dane Wood"])
add("PN", R, Y, 2, "Tim Paap",         0.066, 3.667, 203.89, True,  ["Billy Albert"])
add("PN", R, Y, 2, "Billy Albert",     0.037, 3.700, 201.64, False, ["Tim Paap"])
add("PN", R, Y, 2, "Marcus Butner",    0.043, 3.695, 204.91, True,  ["Amber Denton"])
add("PN", R, Y, 2, "Amber Denton",    -0.060, 6.022,  81.10, False, ["Marcus Butner"])
# Round 3 (Semis)
add("PN", R, Y, 3, "Tommy Franklin",   0.048, 3.646, 206.99, True,  ["Dane Wood"])
add("PN", R, Y, 3, "Dane Wood",        0.097, 3.708, 204.54, False, ["Tommy Franklin"])
add("PN", R, Y, 3, "Marcus Butner",    0.020, 3.635, 205.61, True,  ["Tim Paap"])
add("PN", R, Y, 3, "Tim Paap",         0.096, 4.702, 108.36, False, ["Marcus Butner"])
# Finals
add("PN", R, Y, 4, "Marcus Butner",    0.025, 3.688, 204.32, True,  ["Tommy Franklin"])
add("PN", R, Y, 4, "Tommy Franklin",   0.061, 3.655, 205.98, False, ["Marcus Butner"])

# --- PRO BOOST ---
# Round 1 (8 pairs)
add("PB", R, Y, 1, "Lyle Barnett",     0.004, 3.669, 207.53, True,  ["Randy Weatherford"])
add("PB", R, Y, 1, "Randy Weatherford",-0.033, 3.665, 207.66, False, ["Lyle Barnett"])
add("PB", R, Y, 1, "Johnny Camp",      0.027, 3.655, 206.23, True,  ["Ethan Steding"])
add("PB", R, Y, 1, "Ethan Steding",    0.035, 3.676, 204.01, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Ned Dunphy",       0.034, 3.641, 206.51, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",    0.044, 3.676, 207.50, False, ["Ned Dunphy"])
add("PB", R, Y, 1, "Jason Harris",     0.019, 3.639, 209.01, True,  ["Melanie Salemi"])
add("PB", R, Y, 1, "Melanie Salemi",   0.029, 3.685, 185.87, False, ["Jason Harris"])
add("PB", R, Y, 1, "John Doc",         0.091, 3.643, 206.70, True,  ["Joel Wensley"])
add("PB", R, Y, 1, "Joel Wensley",    -0.104, 3.680, 205.66, False, ["John Doc"])
add("PB", R, Y, 1, "Paul Gargus",      0.043, 3.640, 208.26, True,  ["Carson Perry"])
add("PB", R, Y, 1, "Carson Perry",     0.018, 3.668, 206.04, False, ["Paul Gargus"])
add("PB", R, Y, 1, "Fletcher Cox",     0.027, 3.648, 206.76, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",     0.004, 3.691, 203.40, False, ["Fletcher Cox"])
add("PB", R, Y, 1, "Ty Tutterow",      0.026, 3.628, 207.05, True,  ["Travis Harvey"])
add("PB", R, Y, 1, "Travis Harvey",    0.015, 3.661, 206.04, False, ["Ty Tutterow"])
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Fletcher Cox",     0.016, 3.626, 206.95, True,  ["Johnny Camp"])
add("PB", R, Y, 2, "Johnny Camp",      0.032, 3.645, 206.04, False, ["Fletcher Cox"])
add("PB", R, Y, 2, "Ned Dunphy",       0.000, 3.636, 206.26, True,  ["Paul Gargus"])
add("PB", R, Y, 2, "Paul Gargus",      0.015, 3.625, 207.53, False, ["Ned Dunphy"])
add("PB", R, Y, 2, "Jason Harris",     0.007, 3.626, 209.07, True,  ["John Doc"])
add("PB", R, Y, 2, "John Doc",         0.003, 3.657, 206.89, False, ["Jason Harris"])
add("PB", R, Y, 2, "Lyle Barnett",     0.001, 3.619, 208.91, True,  ["Ty Tutterow"])
add("PB", R, Y, 2, "Ty Tutterow",      0.026, 3.615, 207.11, False, ["Lyle Barnett"])
# Round 3 (Semis)
add("PB", R, Y, 3, "Ned Dunphy",       0.035, 3.636, 206.64, True,  ["Fletcher Cox"])
add("PB", R, Y, 3, "Fletcher Cox",    -0.021, 3.620, 207.72, False, ["Ned Dunphy"])
add("PB", R, Y, 3, "Lyle Barnett",     0.031, 3.613, 209.01, True,  ["Jason Harris"])
add("PB", R, Y, 3, "Jason Harris",     0.026, 3.627, 209.20, False, ["Lyle Barnett"])
# Finals
add("PB", R, Y, 4, "Ned Dunphy",       0.013, 3.632, 207.08, True,  ["Lyle Barnett"])
add("PB", R, Y, 4, "Lyle Barnett",     0.029, 3.627, 208.42, False, ["Ned Dunphy"])

# ============================================================================
# 2026 BENSON — PDRA Drag Wars, August 27-29, 2026, GALOT Motorsports Park
# Source: CompuLink StarTrak elimination PNGs, 29/AUG/2026
# ============================================================================
R, Y = "DragWars", 2026

# --- PRO NITROUS ---
# Round 1 (7 pairs + 1 single)
add("PN", R, Y, 1, "Amber Denton",     0.025, 3.663, 205.63, True,  ["Chris Rini"])
add("PN", R, Y, 1, "Chris Rini",       0.082, 3.696, 205.60, False, ["Amber Denton"])
add("PN", R, Y, 1, "Tim Paap",         0.042, 3.661, 204.73, True,  ["Dale Brinsfield"])
add("PN", R, Y, 1, "Dale Brinsfield",  0.055, 4.667, 112.50, False, ["Tim Paap"])
add("PN", R, Y, 1, "Brian Shrader",    0.023, 3.678, 205.38, True,  ["Buddy Perkinson"])
add("PN", R, Y, 1, "Buddy Perkinson", -0.010, 3.661, 206.20, False, ["Brian Shrader"])
add("PN", R, Y, 1, "Tim Molnar",       0.036, 3.677, 206.10, True,  ["Edward Wilson"])
add("PN", R, Y, 1, "Edward Wilson",    0.364, 3.857, 164.23, False, ["Tim Molnar"])
add("PN", R, Y, 1, "Dane Wood",        0.005, 3.684, 204.60, True,  ["Tommy Franklin"])
add("PN", R, Y, 1, "Tommy Franklin",   0.036, 3.658, 207.21, False, ["Dane Wood"])
add("PN", R, Y, 1, "Fredy Scriba",     0.017, 3.659, 207.50, True,  ["Billy Albert"])
add("PN", R, Y, 1, "Billy Albert",     0.044, 3.677, 205.91, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Marcus Butner",    0.042, 3.708, 184.85, True,  ["Brian Teachman"])
add("PN", R, Y, 1, "Brian Teachman",   0.021, 5.812,  81.86, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Ryan Bush",        0.018, 3.652, 206.95, True,  [])  # Single
# Round 2 (4 pairs)
add("PN", R, Y, 2, "Dane Wood",        0.025, 5.942,  79.10, True,  ["Tim Molnar"])
add("PN", R, Y, 2, "Tim Molnar",      -0.002, 3.748, 203.46, False, ["Dane Wood"])
add("PN", R, Y, 2, "Marcus Butner",    0.051, 3.670, 207.46, True,  ["Tim Paap"])
add("PN", R, Y, 2, "Tim Paap",         0.083, 3.931, 152.95, False, ["Marcus Butner"])
add("PN", R, Y, 2, "Brian Shrader",    0.006, 3.732, 204.01, True,  ["Fredy Scriba"])
add("PN", R, Y, 2, "Fredy Scriba",     0.028, 3.716, 205.47, False, ["Brian Shrader"])
add("PN", R, Y, 2, "Amber Denton",     0.036, 3.689, 205.41, True,  ["Ryan Bush"])
add("PN", R, Y, 2, "Ryan Bush",        0.044, 3.868, 169.91, False, ["Amber Denton"])
# Round 3 (Semis)
add("PN", R, Y, 3, "Amber Denton",     0.050, 3.656, 206.61, True,  ["Dane Wood"])
add("PN", R, Y, 3, "Dane Wood",        0.025, 3.690, 204.51, False, ["Amber Denton"])
add("PN", R, Y, 3, "Marcus Butner",    0.047, 3.641, 208.55, True,  ["Brian Shrader"])
add("PN", R, Y, 3, "Brian Shrader",    0.055, 3.692, 204.42, False, ["Marcus Butner"])
# Finals
add("PN", R, Y, 4, "Marcus Butner",    0.021, 3.628, 209.20, True,  ["Amber Denton"])
add("PN", R, Y, 4, "Amber Denton",     0.034, 3.643, 207.46, False, ["Marcus Butner"])

# --- PRO BOOST ---
# Round 1 (8 pairs)
add("PB", R, Y, 1, "Randy Weatherford",0.018, 3.582, 210.08, True,  ["Ned Dunphy"])
add("PB", R, Y, 1, "Ned Dunphy",       0.025, 3.588, 209.26, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Jason Harris",     0.009, 3.594, 210.57, True,  ["Brylon Holder"])
add("PB", R, Y, 1, "Brylon Holder",    0.016, 3.601, 209.20, False, ["Jason Harris"])
add("PB", R, Y, 1, "Travis Harvey",    0.078, 3.596, 210.57, True,  ["Jeff Rudolf"])
add("PB", R, Y, 1, "Jeff Rudolf",      0.053, 5.008, 101.42, False, ["Travis Harvey"])
add("PB", R, Y, 1, "Ethan Steding",    0.018, 3.599, 206.70, True,  ["John Doc"])
add("PB", R, Y, 1, "John Doc",         0.061, 3.587, 209.46, False, ["Ethan Steding"])
add("PB", R, Y, 1, "Eric Dillard",     0.025, 3.579, 209.75, True,  ["Kurt Steding"])
add("PB", R, Y, 1, "Kurt Steding",     0.028, 3.967, 143.83, False, ["Eric Dillard"])
add("PB", R, Y, 1, "Carson Perry",     0.039, 3.580, 210.64, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",   -0.018, 3.608, 209.49, False, ["Carson Perry"])
add("PB", R, Y, 1, "Johnny Camp",      0.031, 3.584, 210.50, True,  ["Joel Wensley"])
add("PB", R, Y, 1, "Joel Wensley",     0.026, 3.636, 209.14, False, ["Johnny Camp"])
add("PB", R, Y, 1, "Jay Santos",      -0.186, 4.943, 107.20, True,  ["Ty Tutterow"])
add("PB", R, Y, 1, "Ty Tutterow",     -0.001, 0.000,   0.00, False, ["Jay Santos"])  # foul + broke
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Johnny Camp",      0.010, 3.602, 210.41, True,  ["Jason Harris"])
add("PB", R, Y, 2, "Jason Harris",     0.011, 4.843,  94.18, False, ["Johnny Camp"])
add("PB", R, Y, 2, "Randy Weatherford",0.023, 3.623, 209.52, True,  ["Jay Santos"])
add("PB", R, Y, 2, "Jay Santos",       0.050, 6.967,  63.98, False, ["Randy Weatherford"])
add("PB", R, Y, 2, "Carson Perry",     0.027, 4.937,  99.61, True,  ["Travis Harvey"])
add("PB", R, Y, 2, "Travis Harvey",   -0.001, 0.000,   0.00, False, ["Carson Perry"])  # foul + broke
add("PB", R, Y, 2, "Ethan Steding",    0.045, 3.607, 206.89, True,  ["Eric Dillard"])
add("PB", R, Y, 2, "Eric Dillard",     0.015, 4.236, 140.99, False, ["Ethan Steding"])
# Round 3 (Semis)
add("PB", R, Y, 3, "Randy Weatherford",0.003, 3.596, 209.79, True,  ["Ethan Steding"])
add("PB", R, Y, 3, "Ethan Steding",    0.021, 5.575,  83.78, False, ["Randy Weatherford"])
add("PB", R, Y, 3, "Johnny Camp",      0.025, 3.603, 210.50, True,  ["Carson Perry"])
add("PB", R, Y, 3, "Carson Perry",     0.043, 3.650, 180.02, False, ["Johnny Camp"])
# Finals
add("PB", R, Y, 4, "Johnny Camp",      0.024, 3.594, 210.44, True,  ["Randy Weatherford"])
add("PB", R, Y, 4, "Randy Weatherford",-0.004, 3.578, 210.11, False, ["Johnny Camp"])

# ============================================================================
# 2026 DINWIDDIE — PDRA Brian Olson Memorial World Finals, Sept 18-20, 2026
# Source: CompuLink StarTrak elimination PNGs, 20/SEP/2026
# ============================================================================
R, Y = "Brian Olson Memorial World Finals", 2026

# --- PRO NITROUS ---
# Round 1 (8 pairs)
add("PN", R, Y, 1, "Tim Molnar",       0.045, 3.713, 199.82, True,  ["Edward Wilson"])
add("PN", R, Y, 1, "Edward Wilson",   -0.001, 0.000,   0.00, False, ["Tim Molnar"])  # foul + broke
add("PN", R, Y, 1, "Fredy Scriba",     0.038, 3.647, 204.82, True,  ["Dane Wood"])
add("PN", R, Y, 1, "Dane Wood",        0.035, 5.667,  84.53, False, ["Fredy Scriba"])
add("PN", R, Y, 1, "Marcus Butner",    0.040, 3.655, 205.32, True,  ["Chris Rini"])
add("PN", R, Y, 1, "Chris Rini",       0.189, 3.681, 205.26, False, ["Marcus Butner"])
add("PN", R, Y, 1, "Dale Brinsfield",  0.032, 3.668, 205.01, True,  ["Buddy Perkinson"])
add("PN", R, Y, 1, "Buddy Perkinson",  0.036, 3.731, 198.67, False, ["Dale Brinsfield"])
add("PN", R, Y, 1, "Tommy Franklin",   0.065, 3.628, 207.98, True,  ["John Vergotz"])
add("PN", R, Y, 1, "John Vergotz",     0.037, 3.730, 200.29, False, ["Tommy Franklin"])
add("PN", R, Y, 1, "Billy Albert",     0.071, 3.646, 207.75, True,  ["Brian Teachman"])
add("PN", R, Y, 1, "Brian Teachman",   0.422, 9.086,  78.52, False, ["Billy Albert"])
add("PN", R, Y, 1, "John Vergotz Jr.", 0.032, 4.349, 163.99, True,  ["Amber Denton"])
add("PN", R, Y, 1, "Amber Denton",     0.030, 4.526, 115.40, False, ["John Vergotz Jr."])
add("PN", R, Y, 1, "Tim Paap",         0.032, 3.638, 207.50, True,  ["Tony Wilson"])
add("PN", R, Y, 1, "Tony Wilson",      0.001, 4.989, 100.20, False, ["Tim Paap"])
# Round 2 (4 pairs)
add("PN", R, Y, 2, "John Vergotz Jr.", 0.005, 3.812, 196.04, True,  ["Fredy Scriba"])
add("PN", R, Y, 2, "Fredy Scriba",     0.048, 4.008, 193.38, False, ["John Vergotz Jr."])
add("PN", R, Y, 2, "Billy Albert",     0.028, 3.702, 206.13, True,  ["Marcus Butner"])
add("PN", R, Y, 2, "Marcus Butner",    0.059, 3.714, 205.91, False, ["Billy Albert"])
add("PN", R, Y, 2, "Tim Paap",         0.059, 3.690, 205.63, True,  ["Tim Molnar"])
add("PN", R, Y, 2, "Tim Molnar",       0.032, 3.760, 203.16, False, ["Tim Paap"])
add("PN", R, Y, 2, "Dale Brinsfield",  0.035, 3.746, 202.70, True,  ["Tommy Franklin"])
add("PN", R, Y, 2, "Tommy Franklin",   0.108, 3.701, 210.28, False, ["Dale Brinsfield"])
# Round 3 (Semis)
add("PN", R, Y, 3, "Billy Albert",     0.133, 3.706, 205.41, True,  ["John Vergotz Jr."])
add("PN", R, Y, 3, "John Vergotz Jr.", 0.051, 4.036, 185.87, False, ["Billy Albert"])
add("PN", R, Y, 3, "Tim Paap",         0.043, 4.018, 146.07, True,  ["Dale Brinsfield"])
add("PN", R, Y, 3, "Dale Brinsfield", -0.001, 0.000,   0.00, False, ["Tim Paap"])  # foul + broke
# Finals
add("PN", R, Y, 4, "Billy Albert",     0.040, 3.679, 207.08, True,  ["Tim Paap"])
add("PN", R, Y, 4, "Tim Paap",         0.048, 3.687, 206.16, False, ["Billy Albert"])

# --- PRO BOOST ---
# Round 1 (8 pairs)
add("PB", R, Y, 1, "Mike Decker III",  0.029, 3.614, 208.91, True,  ["Greg Blevins Jr."])
add("PB", R, Y, 1, "Greg Blevins Jr.",-0.004, 3.610, 208.78, False, ["Mike Decker III"])
add("PB", R, Y, 1, "Joel Wensley",     0.057, 3.586, 212.06, True,  ["Brylon Holder"])
add("PB", R, Y, 1, "Brylon Holder",   -0.006, 3.574, 220.04, False, ["Joel Wensley"])
add("PB", R, Y, 1, "Travis Harvey",    0.040, 3.557, 211.33, True,  ["Blake Housley"])
add("PB", R, Y, 1, "Blake Housley",    0.041, 3.625, 208.78, False, ["Travis Harvey"])
add("PB", R, Y, 1, "Jason Harris",     0.001, 3.573, 211.46, True,  ["Ethan Steding"])
add("PB", R, Y, 1, "Ethan Steding",   -0.023, 3.584, 210.54, False, ["Jason Harris"])
add("PB", R, Y, 1, "Carson Perry",     0.030, 3.599, 208.39, True,  ["Johnny Camp"])
add("PB", R, Y, 1, "Johnny Camp",      0.028, 4.512, 109.72, False, ["Carson Perry"])
add("PB", R, Y, 1, "Fletcher Cox",     0.034, 3.565, 212.23, True,  ["Scott Lang"])
add("PB", R, Y, 1, "Scott Lang",       0.056, 3.630, 211.23, False, ["Fletcher Cox"])
add("PB", R, Y, 1, "Randy Weatherford",0.043, 3.576, 210.54, True,  ["Raymond Matos"])
add("PB", R, Y, 1, "Raymond Matos",    0.055, 3.608, 210.97, False, ["Randy Weatherford"])
add("PB", R, Y, 1, "Ty Tutterow",      0.056, 3.561, 210.44, True,  ["Mike Decker Jr."])
add("PB", R, Y, 1, "Mike Decker Jr.", -0.131, 3.600, 209.30, False, ["Ty Tutterow"])
# Round 2 (4 pairs)
add("PB", R, Y, 2, "Joel Wensley",     0.033, 3.634, 209.36, True,  ["Randy Weatherford"])
add("PB", R, Y, 2, "Randy Weatherford",0.048, 3.624, 208.65, False, ["Joel Wensley"])
add("PB", R, Y, 2, "Jason Harris",     0.036, 3.605, 211.36, True,  ["Carson Perry"])
add("PB", R, Y, 2, "Carson Perry",     0.059, 3.643, 208.10, False, ["Jason Harris"])
add("PB", R, Y, 2, "Mike Decker III",  0.027, 4.754, 107.10, True,  ["Ty Tutterow"])
add("PB", R, Y, 2, "Ty Tutterow",     -0.008, 3.606, 208.01, False, ["Mike Decker III"])
add("PB", R, Y, 2, "Fletcher Cox",     0.050, 3.605, 210.41, True,  ["Travis Harvey"])
add("PB", R, Y, 2, "Travis Harvey",    0.037, 3.946, 147.49, False, ["Fletcher Cox"])
# Round 3 (Semis)
add("PB", R, Y, 3, "Joel Wensley",    -0.006, 3.633, 209.59, True,  ["Fletcher Cox"])
add("PB", R, Y, 3, "Fletcher Cox",    -0.018, 3.607, 213.91, False, ["Joel Wensley"])
add("PB", R, Y, 3, "Jason Harris",     0.036, 3.617, 210.90, True,  ["Mike Decker III"])
add("PB", R, Y, 3, "Mike Decker III",  0.036, 3.641, 206.45, False, ["Jason Harris"])
# Finals
add("PB", R, Y, 4, "Jason Harris",     0.027, 3.601, 211.16, True,  ["Joel Wensley"])
add("PB", R, Y, 4, "Joel Wensley",     0.163, 3.619, 209.26, False, ["Jason Harris"])


if __name__ == "__main__":
    print(f"PDRA runs: {len(RUNS)}")
    from collections import Counter
    c = Counter((r["class"], r["race"], r["year"]) for r in RUNS)
    for k, v in sorted(c.items()):
        print(f"  {k}: {v} runs")
