# RT.DI

Round-by-round NHRA pro eliminations history (Top Fuel, Funny Car, Pro Stock,
Pro Modified) plus PDRA Pro Nitrous / Pro Boost, rendered as one self-contained
page and published to GitHub Pages at **rt.dragillustrated.com**.

Modeled on DI Incrementals: a scheduled GitHub Actions workflow, raw data kept
forever, a build step that injects data into one HTML artifact, published to the
`gh-pages` branch.

## Hands-off: nothing to edit each weekend

New DragRaceCentral "Summary of Eliminations" articles are discovered
automatically. There are **no manual story-ID or date edits**. Each run:

1. **Discover** (`drc_discover.py`) walks DRC story IDs forward from a saved
   frontier and captures every Top Fuel / Funny Car / Pro Stock / Pro Modified
   eliminations summary. It skips Pro Stock Motorcycle, Top Alcohol and other
   sportsman/exhibition classes, empty articles, and duplicate re-posts of a
   race already captured. Each race's name is mapped to our canonical name and
   the date is taken from the article. Raw bodies are saved under
   `raw_data/stories/<id>.txt` and indexed in `raw_data/discovered.json`.
2. **Parse** (`universal_parser.py`) turns every summary into run rows and
   writes `master_runs.csv` and the per-class CSVs.
3. **Sanity gate** (`run.py`) refuses to publish if the total run count drops or
   a class that had data comes back empty; instead it opens a GitHub issue
   (label `sanity-gate`) and leaves the last good build live.
4. **Build** (`build_artifact.py`) injects the data into `rt_di_artifact.html`,
   bumps the version string, and updates the ticker from the latest race.
5. **Publish**: when the data changes, the workflow commits the raw data back
   and publishes the artifact as `index.html` on `gh-pages` (with `CNAME` and
   `.nojekyll`).

`run.py` prints `CHANGED`, `UNCHANGED`, or `BLOCKED` so the workflow knows
whether to publish.

## Schedule

`.github/workflows/rtdi.yml` runs on cron from **Sunday night through Tuesday**
(US Central), when DRC posts the weekend's summaries. It commits only when the
data changes, so extra runs are free. Trigger a run by hand from the Actions tab
(`force_publish: true` republishes even with no change).

## Files

- `drc_discover.py` - DRC article discovery and classification
- `race_resolver.py` - DRC event name / city -> canonical race name (config)
- `universal_parser.py` - summaries -> run rows, CSVs
- `build_artifact.py` - data -> `rt_di_artifact.html`, version + ticker
- `run.py` - orchestrator: discover -> parse -> gate -> build
- `.github/workflows/rtdi.yml` - the schedule and publish
- `raw_data/` - raw story bodies, discovered index, scan frontier, state (kept forever)
- `CNAME` - `rt.dragillustrated.com`

## One-time setup

1. **Merge this branch to `main`.** GitHub only runs scheduled workflows from the
   default branch, so the cron activates once `rtdi.yml` is on `main`.
2. **Turn on GitHub Pages** (needs repo admin; the API is blocked from the build
   environment, so do it in the browser): repo **Settings > Pages**, set
   **Source: Deploy from a branch**, **Branch: `gh-pages` / `(root)`**, Save. The
   `CNAME` file already sets the custom domain to `rt.dragillustrated.com`.
3. **DNS** (Kyle King): add a `CNAME` record `rt` -> `wes-buck.github.io`.
4. Once DNS resolves, tick **Enforce HTTPS** in Settings > Pages.

## Run locally

    python3 run.py                 # discover (fetches DRC), parse, gate, build
    python3 run.py --no-discover   # rebuild from saved raw data, no network

## Notes

- The date shown for a race is the DRC article's publication date. NHRA posts
  the summary the night of / morning after finals, so it is the finals day or
  the day after. Historical races keep their curated dates in `build_artifact.py`;
  that table takes precedence over discovered dates.
- If `race_resolver.py` cannot confidently map a new event, it falls back to a
  cleaned name and flags it in the run log (`UNCONFIRMED NAME`) so a one-line
  entry can be added to `race_resolver.py` if desired. Data still flows.
