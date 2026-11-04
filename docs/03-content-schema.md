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

## Fields added vs. hand-off (PM decision 2026-11-04: 1 + 2 approved, 3 + 4 not adopted)
1. `research.coverAlt` — accessibility rule requires alt text.
2. `draft` on research/notes — lets you commit unfinished work without publishing it.
3. `Topic` as enum instead of free text — keeps labels consistent.
4. `updated` date on research/notes — shows a piece is maintained, not abandoned.

File names (slugs) are stable IDs, so backlinks between write-ups can be added later without a schema change.

## Implementation notes (step 2, 2026-11-04)
- **Placeholders:** fields typed as number/enum/url/email also accept a
  `[bracketed]` string (`orPlaceholder` in `src/lib/schema.ts`), so sample
  content builds without inventing facts. Replace them as facts arrive.
- `research.cover` is **optional** until real images exist; the card shows
  an `[Illustration or demo GIF]` slot. `coverAlt` is required whenever
  `cover` is set.
- `publications.json` entries carry an `id` (required by Astro's `file()` loader).
- `profile.now.text` is a **list of paragraphs**, not one string.
- `profile.json` is validated by `src/lib/profile.ts` (not a collection).
- v1 has no individual write-up pages, so Home cards link to `/research/`
  and notes link to `/notes/`.
- `src/data/home.json` holds all fixed Home page copy (hero line, section
  titles and hints, CTA, button labels); validated by `src/lib/home.ts`.
  Links (URLs) stay in code. Other pages will follow the same pattern.
- `src/data/research.json` holds the Research page copy; validated by `src/lib/research.ts`.
- `src/data/about.json` holds About page copy (intro, interests with
  `icon: camera | question | headset`, path, looking-for); `**text**` marks
  bold. `src/data/quotes.json` holds the quotes (≤ 30 words each, enforced).
  Both validated by `src/lib/about.ts`.
- Portrait: put `src/assets/portrait.jpg` (or .png/.webp) in place and it
  appears automatically; alt text is `intro.portraitAlt` in about.json.
- About's "path so far" duplicates CV roles/degrees for now; step 4 moves
  them to one shared file (PM decision 2026-11-04, option A).
