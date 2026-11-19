# RT.DI — Project State & Session Context

> **Read this file first.** It is the single source of truth for anyone (human or Claude) picking up work on RT.DI. Every session should update it on the way out so the next one starts caught up.

Last updated: 2026-11-19 · v1.7.6 · Updated by: Claude session (porting UI changes)

---

## What RT.DI is

RT.DI = Drag Illustrated Reaction Time Engine. Live interactive database of every elimination round from every NHRA + PDRA pro class since 2023. Hosted at **https://rt.dragillustrated.com**. Validated by Brian Lohnes (NHRA on FOX), who uses it on-air every weekend.

- GitHub repo: **github.com/wes-buck/rt-di** (public)
- Live URL: **rt.dragillustrated.com** (served by GitHub Pages from the `gh-pages` branch)
- Local working copy: `/Users/wesbuck/Documents/Claude/Projects/Wes Buck Show Operating Room/RT_Report/`

## Current state (as of 2026-11-19)

- **Version:** v1.7.6
- **Total runs:** 8,673 (7,964 NHRA + 709 PDRA)
- **Last NHRA race:** Finals — Pomona, CA — 11.15.26
- **Last PDRA race:** Brian Olson Memorial World Finals — VMP — 09.20.26
- **2026 NHRA season:** COMPLETE through Finals.
- **2026 PDRA season:** COMPLETE through World Finals.

**Pomona Finals winners:** Doug Kalitta (TF), J.R. Todd (FC), Dallas Glenn (PS). No Pro Mod ran at Pomona.

## Automation (this is fully hands-off)

A GitHub Actions workflow at `.github/workflows/rtdi.yml` runs on a cron:
- Sun 23:00 UTC
- Mon & Tue every 2h UTC
- Wed 1:00, 3:00, 5:00 UTC

Each run:
1. Executes `python3 run.py` which calls `drc_discover.py` to check DragRaceCentral for new NHRA "Summary of Eliminations" stories
2. `race_resolver.py` auto-identifies venue + canonical race name + date from story content
3. Appends new story IDs to `raw_data/story_ids.json` and bumps per-class `RACE_NAMES`/`RACE_DATES` entries in `universal_parser.py`
4. Runs `universal_parser.py` -> `master_runs.csv` + per-class CSVs
5. Runs `build_artifact.py` -> `rt_di_data.json` + injects it into `rt_di_artifact.html`
6. Sanity gate validates run counts didn't drop vs. baseline
7. Commits CHANGED/UNCHANGED/BLOCKED and pushes. On CHANGED, deploys to `gh-pages` branch.
8. If BLOCKED, opens/comments a GitHub Issue with label `sanity-gate`.

PDRA is NOT auto-discovered (sheets are PNG images, not text). Wes drops PN + PB printouts into chat for OCR, and a Claude session transcribes to `pdra_data.py`.

## Key file map

| File | Purpose |
|---|---|
| `run.py` | Pipeline entrypoint — called by GitHub Actions |
| `drc_discover.py` | Scrape new DRC story IDs |
| `race_resolver.py` | Auto-name & auto-date new races |
| `universal_parser.py` | Parse DRC text summaries -> CSVs. Holds `RACE_NAMES`/`RACE_DATES`. |
| `build_artifact.py` | Assemble `rt_di_data.json` + inject into HTML template. Reads `raw_data/version.txt`. |
| `pdra_data.py` | Hand-transcribed PDRA PN + PB runs (one `add()` per row). |
| `rt_di_artifact.html` | Template + rendered site. Contains all CSS + JS + injected data. |
| `raw_data/version.txt` | Current semver (e.g. `v1.7.6`). Pipeline bumps patch on CHANGED. |
| `raw_data/story_ids.json` | Map of `CLASS_YEAR` -> list of `[story_id, venue, race_name]` entries. |
| `raw_data/stories/*.txt` | Raw story bodies cached by discovery. |
| `raw_data/.fingerprint` | Hash of code files + template (data block blanked). Changes trigger republish. |
| `raw_data/.last_counts.json` | Baseline run counts for sanity gate. |
| `CNAME` | `rt.dragillustrated.com` (GitHub Pages custom domain). |

## Local vs. repo gotcha (IMPORTANT)

The local folder `/Users/wesbuck/Documents/Claude/Projects/Wes Buck Show Operating Room/RT_Report/` is **not a git clone** — it's the working copy Wes opens in Finder. The actual repo lives at `github.com/wes-buck/rt-di`. When a Claude session edits local files, those changes do NOT reach the live site unless they're committed into the repo and pushed.

**Rule for every Claude session:** clone the repo to `/tmp/rt-di`, make changes there, commit + push. Then also mirror edits back to the local working folder so Wes's `rt_di_artifact.html` is in sync if he opens it locally.

## Push mechanics (what this session's Claude needs)

Claude Code sandbox has `git` but no GitHub credentials. Two ways to push:

1. **Fine-grained Personal Access Token** — Wes pastes a PAT with `Contents: Read & Write` scope on `rt-di`. Claude uses `GITHUB_TOKEN=... git push https://wes-buck:$GITHUB_TOKEN@github.com/wes-buck/rt-di.git`.
2. **Have Wes push manually** — Claude writes a `.push.sh` in the clone, Wes runs it in Terminal.

Option 1 is faster and lets Claude close the loop. Option 2 keeps the token off any external surface.

## What's in flight RIGHT NOW (2026-11-19 session)

1. **Port LEAVES FIRST stat & RT cap filter to the repo HTML.** These were made locally in a prior session but never committed. Done this session in `/tmp/rt-di/rt_di_artifact.html`:
   - `RT_MAX = 0.300` in JS
   - `isRatedRT(r)` filter: positive RT <= .300 AND had an opponent
   - Every RT stat (leaderboard, stat cards, feed, H2H, race detail) now filters through `isRatedRT`
   - "% BEST IN ROUND" column replaced with "% LEAVES FIRST" (pair-wise, not round-wise)
2. **Version bumped** `raw_data/version.txt` -> `v1.7.6`.
3. **Scheduled task** needs updating — the old one still says "upload to WordPress ?v=N." It should instead push to GitHub (no-op since Actions handles it) or just verify the Action ran.

## For the next Claude session (after this one)

Before touching anything else:
1. **Read this file.**
2. `cd /tmp && rm -rf rt-di && git clone https://github.com/wes-buck/rt-di.git` to get the latest truth.
3. Check `raw_data/version.txt` to know current version.
4. Check the latest commits (`git log --oneline -10`) to see what the bot has been doing.
5. If Wes is asking for a change, make it IN THE CLONE and push from there.
6. Update this file on the way out with: what you changed, what's next, any gotchas you ran into.

## Known quirks

- `build_artifact.py` is the canonical file in the repo (uses `_read_version()`). Do not replace it with an older local copy that hardcodes the version.
- `pdra_data.py` entries use `add(cls, race, year, round, driver, rt, et, mph, win, opps)`. Fouls use negative `rt`. Broken runs use `rt=-0.001, et=0, mph=0` to flag as foul without polluting averages.
- The sanity gate in `run.py` blocks publish if run counts drop vs `.last_counts.json`. If a legitimate schedule change drops counts (unlikely), bypass by editing that file and committing.
- The HTML `<script id="rt-data">` block is overwritten on every build. Any custom JS or CSS changes to the template must live OUTSIDE that block.

## Contact / context

- Owner: Wes Buck (wes@dragillustrated.com), publisher of Drag Illustrated.
- Validator: Brian Lohnes (NHRA on FOX booth).
- The tool is already public, already live, already branded with DI logo lockup, already has GA4 analytics firing (`G-LEFMXG2GNT`).
- There is no Nevada Nationals or Pomona Finals left to ingest for 2026. NHRA season is complete. Next NHRA is Gatornationals 2027 (March).
- PDRA 2027 opens with East Coast Nationals (typically early April).

---

**End of state. Update this file when you ship.**
