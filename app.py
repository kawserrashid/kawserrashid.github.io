"""
The web app: URLs and views in one file.

Django mapping:
    @app.route("/about/")   ~  path("about/", views.about)  in urls.py
    def about(): ...        ~  a function-based view
    render_template(...)    ~  render(request, ...)

Run the dev server:   flask --app app run --debug
Build static files:   python build.py
"""

import datetime

from flask import Flask, abort, render_template, request
from jinja2 import StrictUndefined

from core import content, filters

app = Flask(__name__)

# A typo like {{ page.heor.title }} raises an error instead of printing nothing.
# This is how missing fields in data/*.json get caught.
app.jinja_env.undefined = StrictUndefined
filters.register(app)

# Main navigation, in display order.
NAV_ITEMS = [
    {"label": "Sketch Board", "endpoint": "sketch_board"},
    {"label": "Research", "endpoint": "research"},
    {"label": "Notes", "endpoint": "notes"},
    {"label": "About", "endpoint": "about"},
    {"label": "Journey", "endpoint": "journey"},
    {"label": "CV", "endpoint": "cv"},
]


@app.context_processor
def site_context():
    """Variables available in every template (like a Django context processor)."""
    return {
        "profile": content.get_profile(),
        "nav_items": NAV_ITEMS,
        "current_year": datetime.date.today().year,
    }


@app.template_global()
def is_current(endpoint):
    """True if `endpoint` is the page being shown, or its parent (Research for a write-up)."""
    if request.endpoint == endpoint:
        return True
    return endpoint == "research" and request.endpoint == "research_detail"


# ---------------------------------------------------------------------------
# Built pages
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template(
        "pages/home.html",
        page=content.read_json("home"),
        research=content.get_research(limit=3),
        notes=content.get_notes(limit=5),
        paper_notes=content.get_paper_notes(limit=5),
        publication_groups=content.get_publication_groups(),
    )


@app.route("/about/")
def about():
    return render_template(
        "pages/about.html",
        page=content.read_json("about"),
        quotes=content.get_quotes(),
    )


@app.route("/research/")
def research():
    return render_template(
        "pages/research/index.html",
        page=content.read_json("research"),
        writeups=content.get_research(),
        publication_groups=content.get_publication_groups(),
    )


@app.route("/research/<slug>/")
def research_detail(slug):
    entry = content.get_research_entry(slug)
    if entry is None:
        abort(404)
    return render_template(
        "pages/research/detail.html",
        page=content.read_json("research"),
        entry=entry,
    )


# ---------------------------------------------------------------------------
# Placeholder pages ("coming soon"), so the nav never leads to a missing page
# ---------------------------------------------------------------------------

@app.route("/sketch-board/")
def sketch_board():
    return render_template("pages/sketch_board.html")


@app.route("/notes/")
def notes():
    return render_template("pages/notes.html")


@app.route("/journey/")
def journey():
    return render_template("pages/journey.html")


@app.route("/cv/")
def cv():
    return render_template("pages/cv.html")
