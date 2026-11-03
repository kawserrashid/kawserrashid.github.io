# Content schema (the "database")
There is no database. The **filesystem is the data store**, **Zod
schemas in `src/content.config.ts` are the table definitions**, and
**`astro build` is the constraint check** — a bad row fails the build,
like a failed migration.

Notation: `?` = optional. `Status` and `Tag` are shared enums.

## Enums
| Name | Values | Defined in |
|---|---|---|
| `Status` | `planning`, `ongoing`, `completed` | `src/lib/status.ts` (also maps → icon, color, label) |
| `JourneyTag` | `milestone`, `learning`, `teaching`, `life` | `content.config.ts` |
| `PubType` | `conference`, `manuscript`, `thesis` | `content.config.ts` |
| `PubStatus` | `under-review`, `in-preparation` | `content.config.ts` |
| `Topic` | `computer-vision`, `explainable-ai`, `xr`, `data-science` | `content.config.ts` — **proposed**, brief says free text |

## Data files (single-record or list, JSON)
### `profile` — `src/data/profile.json` (one record)
| Field | Type | Rule |
|---|---|---|
| name | string | used for author bolding |
| tagline | string | |
| email | string | valid email |
| location | string | CV header |
| links.github / .scholar / .linkedin | url | |
| now.text | string | |
| now.updated | `YYYY-MM` | |

### `publications` — `src/data/publications.json` (list)
| Field | Type | Rule |
|---|---|---|
| type | PubType | |
| title | string | |
| authors | string[] | ≥1, ordered |
| venue | string | |
| year | int | |
| status? | PubStatus | **required iff** `type = manuscript` |
| pdf? | url | |
| doi? | string | `10.xxxx/…` |

Display order: conference first, then manuscripts & thesis; numbering
continues across groups.

### `quotes` — `src/data/quotes.json` (list)
| Field | Type | Rule |
|---|---|---|
| text | string | ≤ 30 words (enforced) |
| author | string | |
| source? | string | |

## Collections (one Markdown file per record; body = Markdown)
### `research` — `src/content/research/*.md`
| Field | Type | Rule |
|---|---|---|
| title | string | |
| summary | string | ≤ 160 chars |
| topic | Topic | |
| status | Status | |
| date | date | "planted" |
| updated? | date | **proposed** — "last tended", as on maggieappleton.com |
| cover | image | processed by Astro |
| coverAlt | string | **added** — a11y requires alt text |
| code? / demo? | url | |
| draft? | bool | **added** — default false; drafts excluded from build |
Body convention: `## Question`, `## Method`, `## Results`, `## What I learned`.

### `notes` — `src/content/notes/*.md`
title: string · status: Status · date: date · updated?: date (**proposed**) · draft?: bool

### `paperNotes` — `src/content/paper-notes/*.md`
paperTitle: string · venue: string · year: int · written: date

### `journey` — `src/content/journey/<slug>/index.md`
| Field | Type | Rule |
|---|---|---|
| date | date | full date |
| tag | JourneyTag | |
| photo | image | co-located file, resized by Astro |
| alt | string | required, non-empty |
Body: 1–3 sentences.

## Relationships
```
profile.name ──(string match)──► publications.authors[]   bolding
Status ◄── research.status
Status ◄── notes.status
```
No foreign keys beyond these. Sorting and grouping (newest first, by
year) happen in `src/lib/`, not in the data.

## Fields added vs. hand-off (need PM approval)
1. `research.coverAlt` — accessibility rule requires alt text.
2. `draft` on research/notes — lets you commit unfinished work without publishing it.
3. `Topic` as enum instead of free text — keeps labels consistent.
4. `updated` date on research/notes — shows a piece is maintained, not abandoned.

File names (slugs) are stable IDs, so backlinks between write-ups can be added later without a schema change.
