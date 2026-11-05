"""Apply v1.5 branding to rt_di_artifact.html — embed DI logos, add favicon,
add loading splash, add stat-card watermarks, add GA4 placeholder.

Reads logo data URIs from logo_data_uris.json. Idempotent — running twice
produces the same result.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
HTML = ROOT / "rt_di_artifact.html"

uris = json.loads((ROOT / "logo_data_uris.json").read_text())
WORDMARK = uris["header wordmark"]
SPLASH = uris["loading splash"]
WATERMARK = uris["stat-card watermark"]
FAVICON = uris["browser favicon"]

# GA4 measurement ID — placeholder until Wes provides the real one
GA4_ID = "G-PLACEHOLDER"  # Replace with actual ID later

html = HTML.read_text()

# --- 1. Add favicon to <head> ---
if 'rel="icon"' not in html:
    html = html.replace(
        '<title>RT.DI — DI Reaction Time Report</title>',
        f'<title>RT.DI — DI Reaction Time Report</title>\n<link rel="icon" type="image/png" href="{FAVICON}">'
    )

# --- 2. Add CSS for logo header, loading splash, watermarks, footer mark ---
NEW_CSS = """
  /* === DI BRANDING (v1.5) === */
  .di-header-lockup {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 6px;
  }
  .di-header-lockup img {
    height: 64px;
    width: auto;
    filter: drop-shadow(0 0 12px rgba(0,212,255,0.35));
  }
  .di-header-text { display: flex; flex-direction: column; }

  /* Loading splash — covers the screen until DATA is hydrated */
  .di-splash {
    position: fixed; inset: 0;
    z-index: 9999;
    background: #0a0a0a;
    display: flex; align-items: center; justify-content: center;
    flex-direction: column;
    gap: 24px;
    transition: opacity 0.4s ease;
  }
  .di-splash img {
    width: 240px; height: auto;
    filter: drop-shadow(0 0 32px rgba(0,212,255,0.6));
    animation: di-pulse 1.6s ease-in-out infinite;
  }
  .di-splash-text {
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 12px;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    opacity: 0.7;
  }
  @keyframes di-pulse {
    0%, 100% { opacity: 0.55; transform: scale(0.97); }
    50% { opacity: 1.0; transform: scale(1.03); }
  }
  .di-splash.hidden { opacity: 0; pointer-events: none; }

  /* Stat-card watermark — subtle DI mark in the corner */
  .stat-card { position: relative; overflow: hidden; }
  .stat-card::after {
    content: '';
    position: absolute;
    right: 10px; bottom: 8px;
    width: 44px; height: 34px;
    background-image: url("__WATERMARK__");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: bottom right;
    opacity: 0.10;
    pointer-events: none;
  }

  /* Footer mark */
  .di-footer-mark {
    height: 18px; width: auto;
    vertical-align: middle;
    margin: 0 4px -3px;
    opacity: 0.75;
  }
""".replace("__WATERMARK__", WATERMARK)

# Insert before closing </style>
if "/* === DI BRANDING (v1.5) === */" not in html:
    html = html.replace("</style>\n</head>", NEW_CSS + "\n</style>\n</head>")

# --- 3. Replace header HTML with DI lockup ---
OLD_HEADER = '''  <div class="header">
    <h1 class="wordmark">RT.DI</h1>
    <div class="subtitle">DRAG ILLUSTRATED REACTION TIME REPORT</div>
  </div>'''
NEW_HEADER = f'''  <div class="header">
    <div class="di-header-lockup">
      <img src="{WORDMARK}" alt="Drag Illustrated">
      <div class="di-header-text">
        <h1 class="wordmark">RT.DI</h1>
        <div class="subtitle">REACTION TIME REPORT</div>
      </div>
    </div>
  </div>'''
html = html.replace(OLD_HEADER, NEW_HEADER)

# --- 4. Add loading splash right after <body> ---
SPLASH_HTML = f'''<div id="di-splash" class="di-splash">
  <img src="{SPLASH}" alt="Drag Illustrated">
  <div class="di-splash-text">RT.DI // INITIALIZING</div>
</div>
'''
if 'id="di-splash"' not in html:
    html = html.replace('<body>\n<div class="wrap">', f'<body>\n{SPLASH_HTML}<div class="wrap">')

# --- 5. Splash dismissal script — fade out 500ms after data renders ---
SPLASH_SCRIPT = """
  // Dismiss the DI splash once the artifact has rendered
  setTimeout(() => {
    const s = document.getElementById('di-splash');
    if (s) {
      s.classList.add('hidden');
      setTimeout(() => s.remove(), 500);
    }
  }, 700);
"""
# Append to end of the main script. Find the last </script> before </body>.
# We'll inject just before </body> as a new script tag for safety.
if "Dismiss the DI splash" not in html:
    html = html.replace("</body>", f"<script>{SPLASH_SCRIPT}</script>\n</body>")

# --- 6. Update footer to include DI mark next to copyright ---
# Find "© DRAG ILLUSTRATED 2026" and prepend the mark
FOOTER_OLD = "© DRAG ILLUSTRATED 2026"
FOOTER_NEW = f'<img class="di-footer-mark" src="{WATERMARK}" alt="DI"> © DRAG ILLUSTRATED 2026'
if "di-footer-mark" not in html:
    html = html.replace(FOOTER_OLD, FOOTER_NEW)

# --- 7. Bump version strings to v1.5 ---
html = html.replace("RT.DI v1.4.1", "RT.DI v1.5")
html = html.replace("v1.4.1</b>", "v1.5</b>")

# --- 8. GA4 placeholder (commented — Wes will fill in his real ID) ---
GA4_BLOCK = f"""
<!-- Google Analytics 4 — replace G-PLACEHOLDER with your actual Measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}', {{
    'page_title': 'RT.DI Reaction Time Report',
    'send_page_view': true
  }});
  // Custom event helper — wired up to class switches, season changes, H2H, etc.
  window.rtTrack = function(name, params) {{
    if (typeof gtag === 'function') gtag('event', name, params || {{}});
  }};
</script>
"""
if "Google Analytics 4" not in html:
    html = html.replace("</head>", f"{GA4_BLOCK}\n</head>")

HTML.write_text(html)
print(f"v1.5 branding applied. HTML now {HTML.stat().st_size:,} bytes.")
