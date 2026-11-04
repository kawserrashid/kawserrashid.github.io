"""
Jinja template filters: small display helpers used inside templates.

Like Django's custom template filters: {{ value|format_month }}.
"""

import datetime
import re

from markupsafe import Markup, escape

PUBLICATION_STATUS_LABELS = {
    "under-review": "Under review",
    "in-preparation": "In preparation",
}


def format_month(yyyy_mm):
    """'2026-11' -> 'November 2026'"""
    year, month = (int(part) for part in yyyy_mm.split("-"))
    return datetime.date(year, month, 1).strftime("%B %Y")


def bold(text):
    """'plain **bold** plain' -> 'plain <strong>bold</strong> plain' (HTML-safe)."""
    escaped = str(escape(text))  # escape first, so the text can't inject HTML
    return Markup(re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped))


def highlight_word(text, word):
    """Wrap the first occurrence of `word` in <strong>. Used for the name in headlines."""
    escaped = str(escape(text))
    return Markup(escaped.replace(str(escape(word)), f"<strong>{escape(word)}</strong>", 1))


def publication_status(status):
    """'under-review' -> 'Under review'; placeholders like '[In preparation]' pass through."""
    return PUBLICATION_STATUS_LABELS.get(status, status)


def register(app):
    """Make every filter above available in templates."""
    app.jinja_env.filters["format_month"] = format_month
    app.jinja_env.filters["bold"] = bold
    app.jinja_env.filters["highlight_word"] = highlight_word
    app.jinja_env.filters["publication_status"] = publication_status
