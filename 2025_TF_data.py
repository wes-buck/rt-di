"""
2025 NHRA Top Fuel — every elimination run, all 19 completed races (Pomona Finals cancelled).
Source: dragracecentral.com 'Summary of Eliminations in Top Fuel' reports.
Race city → Schedule event mapping:
  GAINESVILLE  → Gatornationals (3/6-9)
  PHOENIX      → Arizona Nationals (3/21-23)
  POMONA 1     → Winternationals (3/27-30)
  LAS VEGAS 1  → 4-Wide Nationals (4/11-13)
  CHARLOTTE 1  → 4-Wide Carolina (4/25-27)
  CHICAGO      → Route 66 (5/16-18)
  EPPING       → New England (5/30-6/1)
  BRISTOL      → Thunder Valley (6/6-8)
  RICHMOND     → Virginia Nationals (6/20-22)  [Langdon DQ'd in final, Ashley awarded win]
  NORWALK      → Summit Racing (6/26-29)
  SEATTLE      → Northwest (7/18-20)
  SONOMA       → Sonoma (7/25-27)
  BRAINERD     → Lucas Oil Nationals (8/14-17)
  INDY         → US Nationals (8/27-9/1)
  READING      → Reading (9/11-14)
  CHARLOTTE 2  → Carolina (9/19-21)  [4-wide]
  ST. LOUIS    → Midwest (9/26-28)
  DALLAS       → FallNationals (10/9-12)
  LAS VEGAS 2  → Nevada Nationals (10/30-11/2)
  POMONA 2     → Finals (CANCELLED)
"""

DATA = []
def a(race, rnd, driver, rt, et, mph, win):
    DATA.append({"race": race, "round": rnd, "driver": driver, "rt": rt, "et": et, "mph": mph, "win": win})

# GAINESVILLE (Gatornationals) — Brown won
R = "Gatornationals"
a(R,1,"Clay Millican",0.071,4.365,283.49,True); a(R,1,"Josh Hart",0.069,6.599,94.69,False)
a(R,1,"Tony Stewart",0.075,3.722,329.91,True); a(R,1,"Brittany Force",0.077,8.643,74.73,False)
a(R,1,"Shawn Langdon",0.062,5.020,235.19,True); a(R,1,"Justin Ashley",0.040,5.682,130.61,False)
a(R,1,"Antron Brown",0.060,4.664,253.18,True); a(R,1,"Krista Baldwin",0.088,5.241,183.67,False)
a(R,1,"Doug Kalitta",0.069,5.575,193.13,True); a(R,1,"Ida Zetterstrom",0.092,11.004,74.49,False)
a(R,1,"Dan Mercier",0.077,4.161,308.28,True); a(R,1,"Tripp Tatum",0.031,0,0,False)  # DQ outer boundary
a(R,1,"Steve Torrence",0.076,3.749,335.15,True); a(R,1,"Doug Foley",0.089,3.757,318.47,False)
a(R,1,"Jasmine Salinas",0.105,3.753,330.23,True); a(R,1,"Shawn Reed",0.106,4.100,275.79,False)
a(R,2,"Antron Brown",0.052,3.721,333.25,True); a(R,2,"Clay Millican",0.064,3.772,324.90,False)
a(R,2,"Jasmine Salinas",0.090,3.751,333.99,True); a(R,2,"Dan Mercier",0.081,3.848,310.91,False)
a(R,2,"Steve Torrence",0.070,3.975,278.63,True); a(R,2,"Doug Kalitta",0.049,4.051,281.07,False)
a(R,2,"Shawn Langdon",0.048,3.739,333.82,True); a(R,2,"Tony Stewart",0.076,3.742,331.53,False)
a(R,3,"Shawn Langdon",0.063,3.727,332.84,True); a(R,3,"Jasmine Salinas",0.088,3.777,328.94,False)
a(R,3,"Antron Brown",0.032,3.754,324.36,True); a(R,3,"Steve Torrence",0.044,3.773,329.10,False)
a(R,4,"Antron Brown",0.036,3.673,333.99,True); a(R,4,"Shawn Langdon",0.046,3.684,332.67,False)

# PHOENIX (Arizona) — Langdon won
R = "Arizona Nationals"
a(R,1,"Tony Stewart",0.088,4.940,189.84,True); a(R,1,"Shawn Reed",0.099,7.961,64.16,False)
a(R,1,"Justin Ashley",0.049,3.805,327.19,True); a(R,1,"Ida Zetterstrom",0.100,3.818,324.51,False)
a(R,1,"Brittany Force",0.092,3.779,320.89,True); a(R,1,"Steven Chrisman",0.135,4.089,254.90,False)
a(R,1,"Doug Kalitta",0.082,3.762,325.92,True); a(R,1,"Travis Shumake",0.096,3.829,330.88,False)
a(R,1,"Shawn Langdon",0.066,3.783,323.66,True); a(R,1,"Scott Palmer",0.072,3.918,296.57,False)
a(R,1,"Antron Brown",0.072,3.770,329.34,True); a(R,1,"Josh Hart",0.061,3.810,322.27,False)
a(R,1,"Jasmine Salinas",0.122,3.779,328.70,True); a(R,1,"Clay Millican",0.119,3.815,319.98,False)
a(R,2,"Shawn Langdon",0.054,3.841,311.49,True); a(R,2,"Justin Ashley",0.072,4.124,246.08,False)
a(R,2,"Brittany Force",0.103,3.793,328.38,True); a(R,2,"Tony Stewart",0.090,5.328,135.00,False)
a(R,2,"Jasmine Salinas",0.115,3.821,322.88,True); a(R,2,"Antron Brown",0.085,3.870,314.24,False)
a(R,2,"Doug Kalitta",0.100,3.821,322.27,True)  # unopposed
a(R,3,"Doug Kalitta",0.066,3.767,317.94,True); a(R,3,"Jasmine Salinas",0.111,3.809,320.66,False)
a(R,3,"Shawn Langdon",0.094,3.833,325.37,True)  # opponent broke
a(R,4,"Shawn Langdon",0.050,3.724,330.39,True); a(R,4,"Doug Kalitta",0.076,3.770,325.53,False)

# POMONA 1 (Winternationals) — Millican won
R = "Winternationals"
a(R,1,"Tony Stewart",0.060,3.713,314.68,True); a(R,1,"Antron Brown",0.086,5.253,139.70,False)
a(R,1,"Josh Hart",0.050,3.675,332.67,True); a(R,1,"Justin Ashley",0.040,4.536,184.75,False)
a(R,1,"Brittany Force",0.093,3.700,337.75,True); a(R,1,"Steven Chrisman",0.155,4.048,252.61,False)
a(R,1,"Shawn Langdon",0.059,3.668,331.28,True); a(R,1,"Ida Zetterstrom",0.092,3.806,278.40,False)
a(R,1,"Doug Kalitta",0.080,3.660,338.34,True); a(R,1,"Scott Palmer",0.090,3.852,288.52,False)
a(R,1,"Clay Millican",0.051,3.874,282.54,True); a(R,1,"Shawn Reed",0.058,4.696,238.01,False)
a(R,1,"Jasmine Salinas",0.072,3.716,331.45,True); a(R,1,"Steve Torrence",-0.136,9.274,82.19,False)  # foul
a(R,2,"Clay Millican",0.058,3.717,313.37,True); a(R,2,"Jasmine Salinas",0.082,3.707,331.69,False)
a(R,2,"Brittany Force",0.072,3.693,332.26,True)  # unopposed
a(R,2,"Shawn Langdon",0.041,3.691,334.73,True); a(R,2,"Josh Hart",0.074,11.965,61.44,False)
a(R,2,"Tony Stewart",0.049,3.702,332.92,True); a(R,2,"Doug Kalitta",0.072,4.456,178.26,False)
a(R,3,"Clay Millican",0.051,3.750,324.12,True); a(R,3,"Brittany Force",0.087,3.812,263.92,False)
a(R,3,"Tony Stewart",0.064,3.723,330.07,True); a(R,3,"Shawn Langdon",0.055,3.835,316.01,False)
a(R,4,"Clay Millican",0.038,4.273,189.71,True); a(R,4,"Tony Stewart",0.065,6.187,99.83,False)

# LAS VEGAS 1 (4-Wide Nationals) — Stewart won
R = "4-Wide Vegas"
# R1
a(R,1,"Tony Stewart",0.071,3.864,321.19,True); a(R,1,"Steve Torrence",0.092,3.846,328.94,True)
a(R,1,"Steven Chrisman",0.185,4.097,279.79,False); a(R,1,"Rob Passey",0.132,4.722,185.38,False)
a(R,1,"Antron Brown",0.052,3.779,329.02,True); a(R,1,"Jasmine Salinas",0.040,3.930,290.76,True)
a(R,1,"Scott Palmer",0.071,4.772,141.24,False); a(R,1,"Shawn Langdon",0.054,5.021,151.87,False)
a(R,1,"Shawn Reed",0.121,3.851,321.58,True); a(R,1,"Josh Hart",0.066,4.190,237.75,True)
a(R,1,"Brittany Force",0.051,4.293,285.41,False); a(R,1,"Terry Totten",0.096,5.261,134.36,False)
a(R,1,"Doug Kalitta",0.057,3.774,317.12,True); a(R,1,"Justin Ashley",0.041,4.022,280.08,True)
a(R,1,"Clay Millican",0.063,4.080,230.53,False)
# R2
a(R,2,"Antron Brown",0.080,3.903,313.88,True); a(R,2,"Jasmine Salinas",0.076,3.994,307.23,True)
a(R,2,"Shawn Reed",0.095,4.514,267.85,False); a(R,2,"Josh Hart",0.084,6.319,101.76,False)
a(R,2,"Tony Stewart",0.052,3.943,303.50,True); a(R,2,"Justin Ashley",0.024,4.090,269.94,True)
a(R,2,"Steve Torrence",0.230,3.928,294.82,False); a(R,2,"Doug Kalitta",-0.351,7.089,105.31,False)
# R3 (Final)
a(R,3,"Tony Stewart",0.082,3.870,317.42,True); a(R,3,"Antron Brown",0.058,3.912,302.35,False)
a(R,3,"Justin Ashley",0.049,3.965,304.25,False); a(R,3,"Jasmine Salinas",0.086,4.237,196.67,False)

# CHARLOTTE 1 (4-Wide zMax) — Langdon won
R = "4-Wide Charlotte"
a(R,1,"Doug Foley",0.076,3.775,320.58,True); a(R,1,"Antron Brown",0.049,4.999,207.56,True)
a(R,1,"Shawn Reed",0.086,5.811,113.20,False); a(R,1,"Clay Millican",0.080,0,0,False)  # NT
a(R,1,"Justin Ashley",0.040,3.749,332.02,True); a(R,1,"Brittany Force",0.073,4.044,276.35,True)
a(R,1,"Todd Paton",0.108,4.020,259.41,False); a(R,1,"Spencer Massey",0.055,9.855,78.37,False)
a(R,1,"Shawn Langdon",0.068,3.728,333.25,True); a(R,1,"Josh Hart",0.045,3.755,332.34,True)
a(R,1,"Ida Zetterstrom",0.095,3.753,330.55,False); a(R,1,"Scott Farley",0.151,4.260,192.96,False)
a(R,1,"Steve Torrence",0.070,3.747,335.65,True); a(R,1,"Tony Stewart",0.069,3.774,325.53,True)
a(R,1,"Doug Kalitta",0.100,3.755,328.46,False); a(R,1,"Lex Joon",0.090,8.651,84.90,False)
a(R,2,"Antron Brown",0.056,3.751,334.24,True); a(R,2,"Tony Stewart",0.067,3.760,323.35,True)
a(R,2,"Doug Foley",0.089,3.850,316.38,False); a(R,2,"Steve Torrence",0.071,3.961,311.56,False)
a(R,2,"Shawn Langdon",0.062,3.773,331.45,True); a(R,2,"Justin Ashley",0.055,3.781,328.78,True)
a(R,2,"Brittany Force",0.086,3.834,322.81,False); a(R,2,"Josh Hart",0.097,6.727,94.39,False)
a(R,3,"Shawn Langdon",0.071,3.714,330.63,True); a(R,3,"Justin Ashley",0.031,3.776,329.99,False)
a(R,3,"Tony Stewart",0.078,3.792,309.06,False); a(R,3,"Antron Brown",0.075,5.441,136.39,False)

# CHICAGO (Route 66) — Stewart won (over Ashley in final!)
R = "Route 66 2025"
a(R,1,"Josh Hart",0.066,3.733,330.07,True); a(R,1,"Clay Millican",0.059,3.746,328.70,False)
a(R,1,"Shawn Reed",0.070,3.750,334.40,True); a(R,1,"Dan Mercier",0.101,3.748,329.26,False)
a(R,1,"Antron Brown",0.062,3.689,337.16,True); a(R,1,"T.J. Zizzo",0.045,10.108,80.54,False)
a(R,1,"Tony Stewart",0.071,3.694,329.26,True); a(R,1,"Terry Totten",0.127,4.276,212.43,False)
a(R,1,"Doug Kalitta",0.098,3.724,332.02,True); a(R,1,"Lex Joon",0.092,3.975,255.19,False)
a(R,1,"Shawn Langdon",0.069,3.733,330.88,True); a(R,1,"Kyle Wurtzel",0.102,3.783,316.60,False)
a(R,1,"Justin Ashley",0.018,3.706,336.49,True); a(R,1,"Brittany Force",0.047,5.149,142.84,False)
a(R,1,"Steve Torrence",0.058,3.735,333.08,True); a(R,1,"Spencer Massey",0.047,3.784,324.12,False)
a(R,2,"Steve Torrence",0.076,3.772,331.69,True); a(R,2,"Shawn Langdon",0.051,5.776,150.36,False)
a(R,2,"Doug Kalitta",0.078,3.723,332.43,True); a(R,2,"Josh Hart",0.058,9.266,78.73,False)
a(R,2,"Tony Stewart",0.080,4.539,261.47,True); a(R,2,"Shawn Reed",0.091,5.043,267.11,False)
a(R,2,"Justin Ashley",0.045,4.407,295.53,True); a(R,2,"Antron Brown",0.063,7.178,113.87,False)
a(R,3,"Tony Stewart",0.059,3.762,329.18,True); a(R,3,"Steve Torrence",0.100,4.021,268.28,False)
a(R,3,"Justin Ashley",0.040,3.816,326.87,True); a(R,3,"Doug Kalitta",0.099,4.803,178.42,False)
a(R,4,"Tony Stewart",0.048,3.777,329.10,True); a(R,4,"Justin Ashley",0.042,3.818,324.12,False)

# EPPING (New England) — Force won
R = "New England"
a(R,1,"Ida Zetterstrom",0.121,3.720,332.18,True); a(R,1,"Steve Torrence",0.072,7.295,121.23,False)
a(R,1,"Dan Mercier",0.087,3.738,324.83,True); a(R,1,"Shawn Langdon",0.053,5.199,157.67,False)
a(R,1,"Doug Kalitta",0.088,3.646,338.34,True)  # unopposed
a(R,1,"Tony Stewart",0.087,3.699,331.45,True); a(R,1,"Rit Pustari",0.136,7.738,75.65,False)
a(R,1,"Shawn Reed",0.121,3.724,335.23,True); a(R,1,"Scott Farley",0.134,4.345,189.71,False)
a(R,1,"Brittany Force",0.080,3.692,339.87,True); a(R,1,"Clay Millican",0.054,3.740,333.74,False)
a(R,1,"Justin Ashley",0.042,3.723,338.34,True); a(R,1,"Josh Hart",0.077,7.158,97.47,False)
a(R,1,"Antron Brown",0.066,4.229,259.56,True); a(R,1,"Mike Bucher",0.073,10.285,40.34,False)
a(R,2,"Antron Brown",0.057,4.707,175.64,True); a(R,2,"Dan Mercier",0.084,6.978,88.25,False)
a(R,2,"Tony Stewart",0.064,3.733,330.96,True); a(R,2,"Justin Ashley",0.042,5.893,118.90,False)
a(R,2,"Brittany Force",0.073,3.690,338.26,True); a(R,2,"Shawn Reed",0.097,3.721,334.57,False)
a(R,2,"Doug Kalitta",0.080,3.680,330.31,True); a(R,2,"Ida Zetterstrom",0.087,3.720,330.55,False)
a(R,3,"Tony Stewart",0.054,3.711,332.34,True); a(R,3,"Antron Brown",0.064,3.738,333.66,False)
a(R,3,"Brittany Force",0.099,3.681,341.42,True); a(R,3,"Doug Kalitta",0.057,5.841,157.41,False)
a(R,4,"Brittany Force",0.068,3.694,340.39,True); a(R,4,"Tony Stewart",0.049,3.720,329.91,False)

# BRISTOL (Thunder Valley) — Torrence won
R = "Thunder Valley"
a(R,1,"Brittany Force",0.081,3.811,330.39,True); a(R,1,"Ida Zetterstrom",0.091,6.840,88.90,False)
a(R,1,"Josh Hart",0.071,4.026,311.85,True); a(R,1,"Doug Kalitta",0.075,4.754,224.92,False)
a(R,1,"Justin Ashley",0.040,3.783,328.14,True); a(R,1,"Antron Brown",0.056,4.403,199.11,False)
a(R,1,"Tony Stewart",0.075,3.821,327.27,True); a(R,1,"Cameron Ferre",0.124,8.227,83.57,False)
a(R,1,"Shawn Langdon",0.132,3.922,259.31,True)  # opponent broke
a(R,1,"Clay Millican",0.089,4.119,222.22,True); a(R,1,"Shawn Reed",0.116,8.822,97.27,False)
a(R,1,"Steve Torrence",0.068,3.974,312.93,True); a(R,1,"Dan Mercier",0.102,3.983,307.72,False)
a(R,2,"Steve Torrence",0.076,3.859,328.14,True); a(R,2,"Clay Millican",0.074,6.187,112.38,False)
a(R,2,"Shawn Langdon",0.059,4.460,245.90,True); a(R,2,"Josh Hart",0.071,5.086,266.79,False)
a(R,2,"Tony Stewart",0.070,4.178,212.13,True)  # unopposed
a(R,2,"Justin Ashley",0.036,3.839,329.91,True); a(R,2,"Brittany Force",0.093,4.925,160.40,False)
a(R,3,"Steve Torrence",0.080,3.857,327.27,True); a(R,3,"Tony Stewart",0.078,3.861,326.08,False)
a(R,3,"Justin Ashley",0.040,3.858,326.24,True); a(R,3,"Shawn Langdon",0.056,9.785,74.97,False)
a(R,4,"Steve Torrence",0.060,4.022,325.37,True); a(R,4,"Justin Ashley",0.047,8.600,82.60,False)

# RICHMOND (Virginia) — Ashley awarded WIN after Langdon DQ
R = "Virginia"
a(R,1,"Justin Ashley",0.046,3.934,315.93,True); a(R,1,"Doug Foley",0.074,3.999,259.71,False)
a(R,1,"Shawn Langdon",0.076,3.905,322.11,True); a(R,1,"Cameron Ferre",0.083,4.070,293.09,False)
a(R,1,"Dan Mercier",0.064,3.951,304.12,True); a(R,1,"Shawn Reed",0.123,3.934,321.19,False)
a(R,1,"Tony Stewart",0.065,3.872,318.99,True); a(R,1,"Brittany Force",0.070,3.938,319.14,False)
a(R,1,"Clay Millican",0.978,4.155,224.92,True)  # opponent left before tree
a(R,1,"Steve Torrence",0.103,3.920,321.12,True); a(R,1,"Josh Hart",0.070,4.041,304.94,False)
a(R,1,"Doug Kalitta",0.096,3.877,326.87,True); a(R,1,"Antron Brown",0.072,3.933,302.41,False)
a(R,2,"Justin Ashley",0.058,3.925,317.64,True); a(R,2,"Steve Torrence",0.186,4.568,175.96,False)
a(R,2,"Shawn Langdon",0.080,3.952,319.52,True); a(R,2,"Dan Mercier",0.102,12.443,55.03,False)
a(R,2,"Doug Kalitta",0.078,3.882,326.00,True); a(R,2,"Clay Millican",0.093,4.014,276.46,False)
a(R,2,"Tony Stewart",0.096,11.465,68.75,True)  # unopposed
a(R,3,"Shawn Langdon",0.059,6.350,108.73,True); a(R,3,"Tony Stewart",-0.093,8.267,84.72,False)  # foul
a(R,3,"Justin Ashley",0.046,4.422,266.69,True); a(R,3,"Doug Kalitta",0.079,5.856,143.76,False)
a(R,4,"Justin Ashley",0.055,4.167,227.92,True)  # Langdon DQ-Tech

# NORWALK (Summit) — Ashley WON
R = "Norwalk"
a(R,1,"Clay Millican",0.085,3.817,331.94,True); a(R,1,"Dan Mercier",0.089,4.930,159.87,False)
a(R,1,"Brittany Force",0.071,4.291,292.77,True); a(R,1,"Lex Joon",0.141,4.552,203.28,False)
a(R,1,"Tony Stewart",0.076,3.894,270.70,True); a(R,1,"Kyle Wurtzel",0.103,9.960,88.86,False)
a(R,1,"Doug Kalitta",0.066,3.816,327.43,True); a(R,1,"Antron Brown",0.076,3.903,322.50,False)
a(R,1,"Justin Ashley",0.053,3.880,318.39,True); a(R,1,"Scott Farley",0.119,4.872,190.83,False)
a(R,1,"Shawn Langdon",0.074,3.872,307.09,True); a(R,1,"Doug Foley",0.073,4.721,162.08,False)
a(R,1,"Steve Torrence",0.078,3.939,313.73,True); a(R,1,"Shawn Reed",0.096,4.000,285.77,False)
a(R,1,"Josh Hart",0.074,3.907,323.50,True); a(R,1,"Spencer Massey",0.042,6.803,99.81,False)
a(R,2,"Tony Stewart",0.091,3.908,318.77,True); a(R,2,"Steve Torrence",0.069,5.113,143.89,False)
a(R,2,"Justin Ashley",0.061,3.902,318.47,True); a(R,2,"Josh Hart",0.080,3.976,320.28,False)
a(R,2,"Shawn Langdon",0.069,3.906,312.35,True); a(R,2,"Brittany Force",0.077,3.953,302.41,False)
a(R,2,"Clay Millican",0.100,3.912,314.83,True); a(R,2,"Doug Kalitta",0.119,3.900,324.36,False)
a(R,3,"Clay Millican",0.085,3.958,306.33,True); a(R,3,"Tony Stewart",0.085,3.974,307.72,False)
a(R,3,"Justin Ashley",0.051,3.935,317.57,True); a(R,3,"Shawn Langdon",0.051,4.008,310.41,False)
a(R,4,"Justin Ashley",0.027,3.931,317.34,True); a(R,4,"Clay Millican",0.089,3.922,322.34,False)

# SEATTLE (Northwest) — Langdon won
R = "Northwest"
a(R,1,"Justin Ashley",0.071,11.887,77.15,True)  # opponent no-show
a(R,1,"Tony Stewart",0.073,3.751,328.38,True); a(R,1,"Josh Hart",0.108,3.746,331.12,False)
a(R,1,"Antron Brown",0.064,3.712,335.23,True); a(R,1,"Clay Millican",0.085,3.739,293.09,False)
a(R,1,"Brittany Force",0.070,3.696,340.82,True); a(R,1,"Ida Zetterstrom",0.093,3.752,330.63,False)
a(R,1,"Shawn Langdon",0.066,3.700,335.98,True); a(R,1,"Cameron Ferre",0.106,4.286,275.00,False)
a(R,1,"Doug Kalitta",0.076,3.628,341.34,True)  # unopposed
a(R,2,"Shawn Langdon",0.058,3.685,334.24,True); a(R,2,"Tony Stewart",0.070,4.817,122.53,False)
a(R,2,"Brittany Force",0.070,4.146,202.48,True); a(R,2,"Antron Brown",0.068,5.083,162.35,False)
a(R,2,"Doug Kalitta",0.073,3.676,337.92,True); a(R,2,"Justin Ashley",0.047,3.876,280.78,False)
a(R,3,"Shawn Langdon",0.069,3.651,338.60,True)  # unopposed
a(R,3,"Brittany Force",0.078,3.659,341.85,True); a(R,3,"Doug Kalitta",0.077,3.752,325.22,False)
a(R,4,"Shawn Langdon",0.050,3.662,337.07,True); a(R,4,"Brittany Force",0.086,4.040,215.93,False)

# SONOMA — Kalitta won
R = "Sonoma"
a(R,1,"Josh Hart",0.060,3.746,329.26,True); a(R,1,"Tony Stewart",0.076,10.343,68.96,False)
a(R,1,"Shawn Langdon",0.066,3.688,336.65,True); a(R,1,"Brittany Force",0.074,3.721,289.26,False)
a(R,1,"Antron Brown",0.075,3.718,336.07,True); a(R,1,"Ida Zetterstrom",0.093,3.739,323.12,False)
a(R,1,"Justin Ashley",0.035,3.750,330.55,True); a(R,1,"Clay Millican",0.079,3.718,331.04,False)
a(R,1,"Doug Kalitta",0.093,3.703,332.92,True); a(R,1,"Ron August",0.064,3.826,319.98,False)
a(R,2,"Antron Brown",0.052,3.740,336.15,True); a(R,2,"Justin Ashley",0.066,3.817,322.42,False)
a(R,2,"Shawn Langdon",0.087,8.019,86.37,True)  # unopposed
a(R,2,"Doug Kalitta",0.081,3.719,336.65,True); a(R,2,"Josh Hart",0.054,4.813,153.30,False)
a(R,3,"Antron Brown",0.061,4.195,251.81,True); a(R,3,"Shawn Langdon",0.071,5.322,166.05,False)
a(R,3,"Doug Kalitta",0.084,3.734,335.40,True)  # unopposed
a(R,4,"Doug Kalitta",0.085,3.752,334.57,True); a(R,4,"Antron Brown",0.058,4.067,229.74,False)

# BRAINERD (Lucas Oil) — Kalitta won
R = "Lucas Oil Brainerd"
a(R,1,"Shawn Langdon",0.066,3.683,334.90,True); a(R,1,"Antron Brown",0.052,6.742,93.16,False)
a(R,1,"Clay Millican",0.047,3.693,330.80,True); a(R,1,"Justin Ashley",0.039,3.740,336.57,False)
a(R,1,"Tony Stewart",0.074,3.733,328.54,True); a(R,1,"Josh Hart",0.040,3.788,328.78,False)
a(R,1,"Jordan Vandergriff",0.088,3.778,283.97,True); a(R,1,"Kyle Satenstein",0.054,3.851,316.01,False)
a(R,1,"Doug Kalitta",0.077,3.721,337.50,True); a(R,1,"Terry Totten",0.106,4.269,213.37,False)
a(R,1,"Brittany Force",0.067,3.692,338.77,True); a(R,1,"Will Smith",0.061,4.239,206.20,False)
a(R,1,"Billy Torrence",0.095,3.706,335.73,True); a(R,1,"Ida Zetterstrom",0.100,6.733,89.99,False)
a(R,2,"Doug Kalitta",0.063,3.683,337.50,True)  # unopposed
a(R,2,"Billy Torrence",0.083,3.708,335.73,True); a(R,2,"Tony Stewart",0.064,3.746,328.54,False)
a(R,2,"Clay Millican",0.066,3.715,337.66,True); a(R,2,"Jordan Vandergriff",0.105,3.726,332.18,False)
a(R,2,"Brittany Force",0.074,3.679,341.25,True); a(R,2,"Shawn Langdon",0.044,4.087,219.40,False)
a(R,3,"Doug Kalitta",0.052,3.665,329.83,True); a(R,3,"Billy Torrence",0.094,3.710,335.32,False)
a(R,3,"Clay Millican",0.053,3.715,321.50,True); a(R,3,"Brittany Force",0.059,3.718,337.07,False)
a(R,4,"Doug Kalitta",0.078,3.670,338.77,True); a(R,4,"Clay Millican",0.099,0,0,False)  # NT

# INDY (US Nationals) — ASHLEY WON
R = "US Nationals"
a(R,1,"Clay Millican",0.041,3.749,284.69,True); a(R,1,"Shawn Langdon",0.061,3.767,265.74,False)
a(R,1,"Justin Ashley",0.036,3.721,328.46,True); a(R,1,"Antron Brown",0.062,3.706,333.66,False)
a(R,1,"Kyle Wurtzel",0.094,3.766,321.73,True); a(R,1,"Jordan Vandergriff",0.084,4.385,255.87,False)
a(R,1,"Brittany Force",0.053,3.690,343.51,True); a(R,1,"Ida Zetterstrom",0.060,7.434,79.06,False)
a(R,1,"Jasmine Salinas",0.092,3.759,331.53,True); a(R,1,"T.J. Zizzo",0.117,8.287,80.09,False)
a(R,1,"Doug Kalitta",0.061,3.706,337.41,True); a(R,1,"Tony Schumacher",0.088,3.736,336.49,False)
a(R,1,"Tony Stewart",0.052,3.716,334.65,True); a(R,1,"Steve Torrence",0.082,3.741,331.20,False)
a(R,1,"Tripp Tatum",0.077,3.724,327.74,True); a(R,1,"Josh Hart",0.057,5.610,119.65,False)
a(R,2,"Jasmine Salinas",0.083,3.780,329.10,True); a(R,2,"Clay Millican",0.070,6.095,110.56,False)
a(R,2,"Tony Stewart",0.080,3.802,328.06,True); a(R,2,"Kyle Wurtzel",0.091,4.454,177.65,False)
a(R,2,"Tripp Tatum",0.073,4.603,215.13,True); a(R,2,"Brittany Force",0.063,11.057,45.56,False)
a(R,2,"Justin Ashley",0.035,4.087,293.15,True); a(R,2,"Doug Kalitta",0.075,4.486,234.61,False)
a(R,3,"Justin Ashley",0.034,3.808,327.74,True); a(R,3,"Tripp Tatum",0.081,8.317,86.04,False)
a(R,3,"Tony Stewart",0.060,3.837,325.85,True); a(R,3,"Jasmine Salinas",0.078,10.754,73.87,False)
a(R,4,"Justin Ashley",0.027,3.839,326.16,True); a(R,4,"Tony Stewart",0.053,3.815,321.88,False)

# READING — Reed won
R = "Reading"
a(R,1,"Tony Stewart",0.072,3.808,329.58,True); a(R,1,"Tony Schumacher",0.085,4.261,195.19,False)
a(R,1,"Shawn Langdon",0.067,3.763,335.07,True); a(R,1,"Doug Foley",0.848,3.824,328.70,False)
a(R,1,"Clay Millican",0.223,3.764,333.25,True)  # unopposed
a(R,1,"Justin Ashley",0.029,3.761,330.31,True); a(R,1,"Scott Farley",0.304,6.176,101.06,False)
a(R,1,"Doug Kalitta",0.073,3.779,336.40,True); a(R,1,"Antron Brown",0.060,3.839,299.93,False)
a(R,1,"Shawn Reed",0.087,3.801,328.54,True); a(R,1,"Kyle Satenstein",0.076,4.002,293.73,False)
a(R,1,"Steve Torrence",0.087,3.766,334.15,True); a(R,1,"Josh Hart",0.099,3.804,335.07,False)
a(R,1,"Brittany Force",0.087,3.798,337.41,True); a(R,1,"Dan Mercier",0.112,6.453,94.86,False)
a(R,2,"Doug Kalitta",0.058,3.787,335.73,True); a(R,2,"Tony Stewart",0.087,3.809,326.71,False)
a(R,2,"Clay Millican",0.088,3.866,313.88,True); a(R,2,"Brittany Force",0.076,4.220,237.88,False)
a(R,2,"Shawn Reed",0.104,3.834,326.87,True); a(R,2,"Shawn Langdon",0.049,4.198,247.38,False)
a(R,2,"Steve Torrence",0.045,3.835,331.77,True); a(R,2,"Justin Ashley",0.039,3.994,279.38,False)
a(R,3,"Shawn Reed",0.090,3.833,326.87,True); a(R,3,"Clay Millican",0.093,6.135,102.32,False)
a(R,3,"Doug Kalitta",0.061,3.812,335.23,True); a(R,3,"Steve Torrence",0.071,3.830,330.55,False)
a(R,4,"Shawn Reed",0.074,3.844,326.63,True); a(R,4,"Doug Kalitta",0.072,4.717,202.12,False)

# CHARLOTTE 2 (Carolina, 4-Wide) — Ashley WON!
R = "Carolina 4-Wide"
a(R,1,"Shawn Langdon",0.048,3.792,332.10,True); a(R,1,"Justin Ashley",0.033,3.811,323.81,True)
a(R,1,"Tony Schumacher",0.063,3.865,290.76,False); a(R,1,"Doug Foley",0.069,4.054,217.42,False)
a(R,1,"Steve Torrence",0.064,3.754,331.61,True); a(R,1,"Clay Millican",0.072,3.785,326.56,True)
a(R,1,"Dan Mercier",0.108,3.761,327.66,False)
a(R,1,"Tony Stewart",0.065,3.766,326.79,True); a(R,1,"Brittany Force",0.100,3.758,338.34,True)
a(R,1,"Shawn Reed",0.072,3.787,327.66,False)
a(R,1,"Doug Kalitta",0.058,3.757,327.43,True); a(R,1,"Antron Brown",0.061,3.780,330.31,True)
a(R,1,"Josh Hart",0.038,3.820,331.20,False)
a(R,2,"Justin Ashley",0.036,3.788,326.56,True); a(R,2,"Shawn Langdon",0.068,3.761,333.82,True)
a(R,2,"Brittany Force",0.066,3.773,338.26,False); a(R,2,"Tony Stewart",0.073,3.784,328.62,False)
a(R,2,"Doug Kalitta",0.056,3.797,326.48,True); a(R,2,"Clay Millican",0.083,3.821,327.74,True)
a(R,2,"Antron Brown",0.064,3.844,326.79,False); a(R,2,"Steve Torrence",0.050,4.141,261.67,False)
a(R,3,"Justin Ashley",0.043,3.784,329.83,True); a(R,3,"Doug Kalitta",0.068,3.784,332.84,False)
a(R,3,"Shawn Langdon",0.062,3.814,334.24,False); a(R,3,"Clay Millican",0.081,4.235,195.19,False)

# ST. LOUIS (Midwest) — Kalitta won
R = "Midwest"
a(R,1,"Kyle Wurtzel",0.072,3.789,320.58,True); a(R,1,"Josh Hart",0.061,3.809,330.96,False)
a(R,1,"Justin Ashley",0.036,3.753,331.94,True); a(R,1,"Brittany Force",0.058,5.328,137.90,False)
a(R,1,"Antron Brown",0.051,3.752,333.16,True); a(R,1,"Cameron Ferre",1.257,24.267,52.78,False)
a(R,1,"Doug Kalitta",0.077,3.740,334.82,True); a(R,1,"Will Smith",0.081,10.361,85.16,False)
a(R,1,"Ida Zetterstrom",0.000,3.801,323.66,True); a(R,1,"Tony Stewart",0.026,3.927,298.93,False)
a(R,1,"Tony Schumacher",0.085,3.787,318.47,True); a(R,1,"Clay Millican",0.098,3.850,305.08,False)
a(R,1,"Steve Torrence",0.061,4.426,180.91,True); a(R,1,"T.J. Zizzo",-0.020,3.805,334.32,False)  # foul
a(R,1,"Shawn Langdon",0.062,3.772,336.82,True); a(R,1,"Shawn Reed",0.069,3.788,330.80,False)
a(R,2,"Ida Zetterstrom",0.088,3.802,326.87,True); a(R,2,"Kyle Wurtzel",0.102,3.889,321.04,False)
a(R,2,"Justin Ashley",0.044,3.794,330.55,True); a(R,2,"Shawn Langdon",0.049,3.817,329.42,False)
a(R,2,"Antron Brown",0.076,3.807,331.61,True); a(R,2,"Tony Schumacher",0.065,4.852,151.75,False)
a(R,2,"Doug Kalitta",0.083,3.813,331.94,True); a(R,2,"Steve Torrence",0.077,5.703,119.57,False)
a(R,3,"Ida Zetterstrom",0.069,3.925,292.08,True); a(R,3,"Antron Brown",0.075,5.663,132.41,False)
a(R,3,"Doug Kalitta",0.068,3.805,332.59,True); a(R,3,"Justin Ashley",0.045,3.931,310.41,False)
a(R,4,"Doug Kalitta",0.074,3.796,327.98,True); a(R,4,"Ida Zetterstrom",0.065,4.036,247.79,False)

# DALLAS (FallNationals) — Kalitta won
R = "FallNationals"
a(R,1,"Clay Millican",0.072,3.700,335.32,True); a(R,1,"Tony Stewart",0.090,3.774,321.52,False)
a(R,1,"Brittany Force",0.066,3.729,340.14,True); a(R,1,"Tony Schumacher",0.068,5.441,125.47,False)
a(R,1,"Shawn Reed",0.102,3.717,338.83,True); a(R,1,"Kyle Satenstein",0.069,0,0,False)  # DQ
a(R,1,"Justin Ashley",0.023,3.732,334.25,True); a(R,1,"Doug Foley",0.077,4.857,160.19,False)
a(R,1,"Shawn Langdon",0.082,3.697,336.00,True); a(R,1,"Mitch King",0.102,10.680,79.99,False)
a(R,1,"Ida Zetterstrom",0.077,4.257,206.86,True); a(R,1,"Antron Brown",0.062,5.127,158.61,False)
a(R,1,"Doug Kalitta",0.078,3.751,333.93,True); a(R,1,"Jasmine Salinas",0.074,6.219,99.89,False)
a(R,1,"Steve Torrence",0.087,3.993,264.07,True); a(R,1,"Josh Hart",0.072,4.194,208.21,False)
a(R,2,"Doug Kalitta",0.078,3.757,332.37,True); a(R,2,"Ida Zetterstrom",0.095,3.845,323.37,False)
a(R,2,"Steve Torrence",0.078,3.833,330.37,True); a(R,2,"Shawn Reed",0.060,4.076,257.84,False)
a(R,2,"Brittany Force",0.050,3.828,332.79,True); a(R,2,"Justin Ashley",0.045,3.943,292.85,False)
a(R,2,"Shawn Langdon",0.069,3.790,333.38,True); a(R,2,"Clay Millican",0.075,4.385,187.38,False)
a(R,3,"Steve Torrence",0.123,3.836,328.08,True)  # opponent broke
a(R,3,"Doug Kalitta",0.055,3.805,332.59,True); a(R,3,"Shawn Langdon",0.070,4.545,193.10,False)
a(R,4,"Doug Kalitta",0.079,3.777,333.04,True); a(R,4,"Steve Torrence",0.063,3.874,317.46,False)

# LAS VEGAS 2 (Nevada Nationals) — Force won
R = "Nevada"
a(R,1,"Clay Millican",0.077,3.750,333.74,True); a(R,1,"Antron Brown",0.064,3.791,333.58,False)
a(R,1,"Justin Ashley",0.042,5.667,119.55,True); a(R,1,"Josh Hart",0.069,6.895,94.68,False)
a(R,1,"Tony Schumacher",0.077,3.794,335.32,True); a(R,1,"Shawn Reed",0.109,3.959,240.42,False)
a(R,1,"Brittany Force",0.084,3.758,337.24,True)  # unopposed
a(R,1,"Doug Kalitta",0.080,3.743,338.00,True); a(R,1,"Rob Passey",0.152,4.047,287.29,False)
a(R,1,"Shawn Langdon",0.081,5.183,222.36,True); a(R,1,"Kelly Harper",0.110,6.517,91.14,False)
a(R,1,"Tony Stewart",0.067,3.856,293.22,True); a(R,1,"Dan Mercier",0.099,4.695,163.71,False)
a(R,2,"Shawn Langdon",0.079,3.738,333.33,True); a(R,2,"Justin Ashley",0.041,3.779,332.43,False)
a(R,2,"Tony Stewart",0.069,3.778,328.38,True); a(R,2,"Tony Schumacher",0.065,3.808,319.90,False)
a(R,2,"Brittany Force",0.070,3.764,335.65,True); a(R,2,"Clay Millican",0.097,4.074,225.79,False)
a(R,2,"Doug Kalitta",0.059,3.757,328.54,True)  # unopposed
a(R,3,"Brittany Force",0.095,3.824,323.35,True); a(R,3,"Tony Stewart",0.072,5.015,144.58,False)
a(R,3,"Shawn Langdon",0.083,3.721,334.24,True); a(R,3,"Doug Kalitta",0.068,3.757,336.15,False)
a(R,4,"Brittany Force",0.065,3.704,337.33,True); a(R,4,"Shawn Langdon",0.059,3.727,333.91,False)

# ===== Write CSV =====
import csv
out = "/sessions/great-determined-cannon/mnt/Wes Buck Show Operating Room/RT_Report/2025_TF_runs.csv"
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["race","round","driver","rt","et","mph","win"])
    w.writeheader()
    for row in DATA:
        w.writerow(row)
print(f"Wrote {len(DATA)} 2025 run records.")
