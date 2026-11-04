# kawser-site-lite

The personal research site from `../kawser-site`, rebuilt in Python.
Flask + Jinja templates, built to plain HTML for GitHub Pages.

**Status (2026-11-04):** Home, About, Research, and the research write-up
pages are built and match the Astro site. Sketch Board, Notes, Journey, and
CV exist as "coming soon" pages.

## Quick start
```bash
cd ~/Personal/kawser-site-lite
python3 -m venv .venv                 # once
.venv/bin/pip install -r requirements.txt   # once

.venv/bin/flask --app app run --debug # dev server → http://127.0.0.1:5000
.venv/bin/python build.py             # static site → build/
```
Stop the dev server with **Ctrl+C** (not Ctrl+Z, which only pauses it).

To preview the built files:
`.venv/bin/python -m http.server 8000 --directory build` → http://localhost:8000

## Read next
| Doc | What it covers |
|---|---|
| [docs/01-how-it-works.md](docs/01-how-it-works.md) | The big picture, mapped to Django |
| [docs/02-project-structure.md](docs/02-project-structure.md) | Every folder and file, and what it's for |
| [docs/03-editing-content.md](docs/03-editing-content.md) | Changing text, adding write-ups, publications, quotes |
| [docs/04-adding-a-page.md](docs/04-adding-a-page.md) | Turning a "coming soon" page into a real one |
| [docs/05-roadmap.md](docs/05-roadmap.md) | What's done, what's next, differences from the Astro site |
