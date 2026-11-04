# How it works

## The one-sentence version
A small Flask app renders pages from templates and content files; a build
script visits every page once and saves the HTML, so the live site is just
files: no Python server runs on GitHub Pages.

## Two ways to run the same code
```
                 ┌──────────── dev:  flask run ─────────────►  browser (live reload)
content/*.md  ┐  │
data/*.json   ├─►  app.py (routes/views) ─► templates/*.html
static/       ┘  │
                 └──────────── build: python build.py ──────►  build/*.html ─► GitHub Pages
```
- **Dev** (`flask --app app run --debug`): a normal web server. Edit a
  file, refresh the browser, see the change.
- **Build** (`python build.py`): Frozen-Flask requests every URL and saves
  each response: `/about/` becomes `build/about/index.html`. Static files
  are copied to `build/static/`.

## Django → this project
| Django | Here | Where |
|---|---|---|
| `urls.py` + views | `@app.route("/about/")` above a function | `app.py` |
| `render(request, "x.html", ctx)` | `render_template("x.html", **ctx)` | `app.py` |
| Models | Pydantic models (fields + validation) | `core/models.py` |
| ORM queries / managers | plain functions: `get_research(limit=3)` | `core/content.py` |
| Database rows | Markdown files and JSON files | `content/`, `data/` |
| Templates (`{% extends %}`, `{% block %}`, `{{ }}`) | Jinja2: almost the same syntax | `templates/` |
| `base.html` | `base.html` | `templates/base.html` |
| `{% include %}` | `{% include %}` | header/footer partials |
| Inclusion tags | Jinja **macros**: functions that return HTML | `templates/components/` |
| Custom template filters | `core/filters.py` → `{{ x\|format_month }}` | |
| Context processors | `@app.context_processor` | `app.py` (`profile`, nav) |
| `{% url "about" %}` | `{{ url_for('about') }}` | everywhere |
| `{% static "x" %}` | `{{ url_for('static', filename='x') }}` | everywhere |
| `collectstatic` + deploy | `python build.py` | `build.py` |

Jinja differences that will trip you up:
- Calling methods needs parentheses: `profile.name.split()[0]`.
- `{% set x = ... %}` creates variables in templates.
- A dict key named `items` must be written `obj["items"]` (because
  `obj.items` is the dict's `.items()` method).
- Macros only see what you pass in; they don't see the page's variables.

## Where safety checks happen
The Astro site failed the build when content was wrong. This one does too:
1. **Pydantic** (`core/models.py`) checks every Markdown file, publication,
   quote, and `profile.json`. A missing title or a status like `"done"`
   raises an error naming the file and field.
2. **StrictUndefined** (in `app.py`) makes a template crash on a missing
   value instead of printing nothing. That's how a missing key in
   `home.json`/`about.json`/`research.json` gets caught.
3. **Escaping**: Jinja escapes text automatically (like Django). The only
   `|safe` is for the HTML made from your own Markdown files.

So: if `python build.py` finishes, the content is valid.

## Life of a request (dev server)
1. Browser asks for `/research/saliency-noise/`.
2. Flask matches `@app.route("/research/<slug>/")` → `research_detail(slug)`.
3. The view calls `content.get_research_entry(slug)`, which reads
   `content/research/saliency-noise.md`, validates it with `ResearchEntry`,
   and converts the Markdown body to HTML.
4. `render_template("pages/research/detail.html", entry=...)`.
5. The template extends `base.html`, which includes the header and footer.

During the build, step 1 is done by Frozen-Flask instead of a browser.

## Styling
Plain CSS, no build step.
- `static/css/tokens.css`: every color, font, and size as a variable
  (`--color-teal`). Change a value once, the whole site changes.
- `global.css`: fonts, reset, base styles. `components.css`: header,
  footer, buttons, cards, etc. Both load on every page.
- `static/css/pages/<page>.css`: loaded only by that page (via the
  `page_css` block), so page class names like `.stack` can't clash.
- Astro scoped CSS automatically. Plain CSS doesn't, so component classes
  carry a prefix: `.research-card-title`, `.quote-card`, `.nav-links`.

There is no JavaScript on the site. The quote marquee is pure CSS.
