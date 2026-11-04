# Project structure

```
kawser-site-lite/
├─ app.py                    URLs + views (Flask). Start here.
├─ build.py                  Freezes the app into build/ (static HTML)
├─ requirements.txt          Python packages, pinned
│
├─ core/                     Python helpers (no HTML here)
│  ├─ models.py              Pydantic schemas: what valid content looks like
│  ├─ content.py             Reads content/ and data/, answers queries
│  └─ filters.py             Template filters: format_month, bold, ...
│
├─ content/                  ✏️  Markdown: one file = one entry
│  ├─ research/              Research write-ups → /research/<file-name>/
│  ├─ notes/                 Notes (listed on Home; page coming later)
│  └─ paper-notes/           Paper notes (listed on Home)
│
├─ data/                     ✏️  JSON: page copy and small lists
│  ├─ profile.json           Name, tagline, email, links, "Now" section
│  ├─ publications.json      Publications (order = display order)
│  ├─ quotes.json            Favorite quotes (About page)
│  ├─ home.json              All text on the Home page
│  ├─ about.json             All text on the About page
│  └─ research.json          All text on the Research pages
│
├─ templates/
│  ├─ base.html              Page skeleton: <head>, header, main, footer
│  ├─ partials/              header.html, footer.html (included by base)
│  ├─ components/            Reusable macros
│  │  ├─ button.html         button(href, text, variant)
│  │  ├─ icons.html          icon(name, size, stroke, color): inline SVGs
│  │  ├─ status.html         status_badge(...), status_legend(): status labels live here
│  │  ├─ research_card.html  research_card(entry, heading_level)
│  │  ├─ publication_list.html  publication_list(groups, bold_name)
│  │  └─ quote_marquee.html  quote_marquee(quotes, label)
│  └─ pages/                 One template per page
│     ├─ home.html  about.html
│     ├─ research/index.html  research/detail.html
│     ├─ placeholder.html    Shared "coming soon" layout
│     └─ sketch_board.html  notes.html  journey.html  cv.html   (stubs)
│
├─ static/                   Served as-is under /static/
│  ├─ css/                   tokens.css, global.css, components.css, pages/*.css
│  ├─ fonts/                 Newsreader + Lato (.woff2, self-hosted) + licenses
│  └─ img/portrait.jpg       About page photo
│
├─ docs/                     These documents
├─ .venv/                    Virtual environment (not committed)
└─ build/                    Output of build.py (not committed)
```

Rule of thumb: ✏️ `content/` and `data/` are what you edit day to day.
Everything else is code you touch when changing how the site looks or works.

## URL → view → template
| URL | View in `app.py` | Template |
|---|---|---|
| `/` | `home` | `pages/home.html` |
| `/about/` | `about` | `pages/about.html` |
| `/research/` | `research` | `pages/research/index.html` |
| `/research/<slug>/` | `research_detail` | `pages/research/detail.html` |
| `/sketch-board/` | `sketch_board` | `pages/sketch_board.html` (stub) |
| `/notes/` | `notes` | `pages/notes.html` (stub) |
| `/journey/` | `journey` | `pages/journey.html` (stub) |
| `/cv/` | `cv` | `pages/cv.html` (stub) |
