"""
Loads content from disk and answers simple queries.

This is the site's "repository layer" (think of it as the Django ORM for
files): views call these functions instead of reading files themselves.
"""

import json
from functools import cache
from pathlib import Path

import markdown
import yaml

from core.models import Note, PaperNote, Profile, Publication, Quote, ResearchEntry

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
DATA_DIR = BASE_DIR / "data"


# ---------------------------------------------------------------------------
# Low-level readers
# ---------------------------------------------------------------------------

def read_json(name):
    """data/<name>.json -> Python dict or list."""
    with open(DATA_DIR / f"{name}.json", encoding="utf-8") as f:
        return json.load(f)


def read_markdown(path):
    """
    Split a Markdown file into (front matter dict, body HTML).

    A file looks like:
        ---
        title: "Hello"
        ---
        Body text in **Markdown**.
    """
    text = path.read_text(encoding="utf-8")
    _, front_matter, body = text.split("---", 2)
    fields = yaml.safe_load(front_matter) or {}
    body_html = markdown.markdown(body, extensions=["fenced_code", "tables"])
    return fields, body_html


def load_collection(folder, model):
    """Read every .md file in content/<folder>/ and validate it with `model`."""
    items = []
    for path in sorted((CONTENT_DIR / folder).glob("*.md")):
        fields, body_html = read_markdown(path)
        try:
            items.append(model(slug=path.stem, body_html=body_html, **fields))
        except Exception as error:
            # Say which file is broken, not just which field.
            raise ValueError(f"Invalid content in {path}:\n{error}") from error
    return items


# ---------------------------------------------------------------------------
# Queries used by the views
# ---------------------------------------------------------------------------
# @cache: read each file once per run, like a tiny in-memory cache.

@cache
def get_profile():
    return Profile(**read_json("profile"))


@cache
def get_quotes():
    return [Quote(**q) for q in read_json("quotes")]


@cache
def _all_research():
    return load_collection("research", ResearchEntry)


def get_research(limit=None):
    """Published research write-ups, newest first."""
    items = [r for r in _all_research() if not r.draft]
    items.sort(key=lambda r: r.date, reverse=True)
    return items[:limit]


def get_research_entry(slug):
    """One published write-up, or None if it doesn't exist (or is a draft)."""
    for entry in get_research():
        if entry.slug == slug:
            return entry
    return None


@cache
def _all_notes():
    return load_collection("notes", Note)


def get_notes(limit=None):
    """Published notes, newest first."""
    items = [n for n in _all_notes() if not n.draft]
    items.sort(key=lambda n: n.date, reverse=True)
    return items[:limit]


@cache
def _all_paper_notes():
    return load_collection("paper-notes", PaperNote)


def get_paper_notes(limit=None):
    """Paper notes, most recently written first."""
    items = sorted(_all_paper_notes(), key=lambda p: p.written, reverse=True)
    return items[:limit]


@cache
def get_publication_groups():
    """
    Publications split into two display groups, numbered continuously:
    1 = conference paper, 2, 3, ... = manuscripts & thesis.
    Inside a group, the order of publications.json is kept.

    Returns a list like:
        [{"label": "Conference paper", "items": [(1, pub), ...]}, ...]
    """
    publications = [Publication(**p) for p in read_json("publications")]
    conference = [p for p in publications if p.type == "conference"]
    others = [p for p in publications if p.type != "conference"]

    groups = []
    number = 0
    for label, pubs in [("Conference paper", conference), ("Manuscripts & thesis", others)]:
        if not pubs:
            continue
        numbered = []
        for pub in pubs:
            number += 1
            numbered.append((number, pub))
        groups.append({"label": label, "items": numbered})
    return groups
