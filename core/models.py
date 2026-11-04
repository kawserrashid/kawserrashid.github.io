"""
Schemas for every piece of content: the site's "database tables".

Pydantic models work like Django models + forms combined: they describe the
fields and validate the data. If a Markdown file or JSON record has a missing
field or a wrong value, loading it raises a clear error and the build stops.
"""

import datetime
import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

# "[Something]" marks a fact Kawser hasn't supplied yet.
# Fields that normally hold a number, URL or email may hold a placeholder
# instead, so sample content can build without inventing facts.
PLACEHOLDER = re.compile(r"^\[.+\]$")


def is_placeholder(value) -> bool:
    return isinstance(value, str) and bool(PLACEHOLDER.match(value))


# The three status values used by research write-ups and notes.
Status = Literal["planning", "ongoing", "completed"]


# ---------------------------------------------------------------------------
# Markdown collections (content/<folder>/*.md, fields come from front matter)
# ---------------------------------------------------------------------------

class ResearchEntry(BaseModel):
    slug: str  # file name without ".md"; used in the URL /research/<slug>/
    title: str
    summary: str = Field(max_length=160)
    topic: str  # free text, e.g. "Computer Vision"
    status: Status
    date: datetime.date  # used for sorting, not shown yet
    cover: str | None = None  # path under static/, e.g. "img/saliency.jpg"
    cover_alt: str | None = Field(default=None, alias="coverAlt")
    code: str | None = None
    demo: str | None = None
    draft: bool = False
    body_html: str = ""  # Markdown body converted to HTML

    @model_validator(mode="after")
    def cover_needs_alt(self):
        if self.cover and not self.cover_alt:
            raise ValueError("coverAlt is required when cover is set")
        return self


class Note(BaseModel):
    slug: str
    title: str
    status: Status
    date: datetime.date
    draft: bool = False
    body_html: str = ""


class PaperNote(BaseModel):
    slug: str
    paper_title: str = Field(alias="paperTitle")
    venue: str
    year: int | str
    written: datetime.date
    body_html: str = ""

    @field_validator("year")
    @classmethod
    def year_or_placeholder(cls, value):
        if isinstance(value, str) and not is_placeholder(value):
            raise ValueError("year must be a number or a [placeholder]")
        return value


# ---------------------------------------------------------------------------
# JSON data files (data/*.json)
# ---------------------------------------------------------------------------

class Publication(BaseModel):
    id: str
    type: Literal["conference", "manuscript", "thesis"]
    title: str
    authors: list[str] = Field(min_length=1)
    venue: str
    year: int | str
    status: str | None = None  # only for manuscripts
    pdf: str | None = None
    doi: str | None = None

    @model_validator(mode="after")
    def check_status(self):
        if (self.type == "manuscript") != (self.status is not None):
            raise ValueError("status is required for manuscripts and only allowed on manuscripts")
        return self


class Links(BaseModel):
    github: str
    scholar: str
    linkedin: str

    @field_validator("github", "scholar", "linkedin")
    @classmethod
    def url_or_placeholder(cls, value):
        if not (value.startswith("https://") or is_placeholder(value)):
            raise ValueError("must start with https:// or be a [placeholder]")
        return value


class Now(BaseModel):
    text: list[str] = Field(min_length=1)  # one string per paragraph
    updated: str = Field(pattern=r"^\d{4}-(0[1-9]|1[0-2])$")  # YYYY-MM


class Profile(BaseModel):
    name: str
    tagline: str
    email: str
    location: str
    links: Links
    now: Now

    @field_validator("email")
    @classmethod
    def email_or_placeholder(cls, value):
        if "@" not in value and not is_placeholder(value):
            raise ValueError("must be an email address or a [placeholder]")
        return value


class Quote(BaseModel):
    text: str
    author: str
    source: str | None = None

    @field_validator("text")
    @classmethod
    def max_30_words(cls, value):
        if len(value.split()) > 30:
            raise ValueError("quotes must be 30 words or fewer")
        return value
