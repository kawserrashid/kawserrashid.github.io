# Editing content

After any edit, refresh the dev server, or run `python build.py`.
If something is wrong, the error names the file and the field.

## Placeholders
Text in `[square brackets]` marks a fact not supplied yet. Fields that
normally need a number, URL, or email (year, links, email) also accept a
`[placeholder]`. Before publishing, search the output:
`grep -rl "\[" build --include=*.html`

## Page text
All visible text on Home, About, and Research lives in `data/home.json`,
`data/about.json`, and `data/research.json`. Edit the values; keep the
keys. Removing or renaming a key makes the page fail on purpose.
In `about.json` → `lookingFor.paragraphs`, `**double asterisks**` make text bold.

## Name, email, links, "Now"
`data/profile.json`. `now.updated` must be `YYYY-MM` (shown as "November 2026").
The first word of `tagline` and of the About headline is highlighted when it
matches your first name.

## Add a research write-up
Create `content/research/<slug>.md`. The file name becomes the URL
(`/research/<slug>/`) and must be lowercase-with-dashes.
```markdown
---
title: "Do saliency maps survive image noise?"
summary: "One sentence, at most 160 characters."
topic: Explainable AI          # free text
status: ongoing                # planning | ongoing | completed
date: 2026-11-03               # sorts newest first (not shown yet)
# optional:
cover: img/saliency.jpg        # file in static/img/
coverAlt: "What the image shows"   # required if cover is set
code: https://github.com/...
demo: https://...
draft: true                    # hides it everywhere, no page
---

## Question
...

## Method
...
```
The body is normal Markdown: headings, lists, `code`, fenced code blocks,
tables, images, quotes.

Home shows the 3 newest; Research shows all.

## Add a note / paper note
`content/notes/<slug>.md`:
```markdown
---
title: "First steps with WebXR"
status: planning
date: 2026-11-02
---
```
`content/paper-notes/<slug>.md`:
```markdown
---
paperTitle: "Grad-CAM: Visual Explanations..."
venue: "ICCV"
year: 2017
written: 2026-11-04
---
```
Home lists the 5 newest of each. Their own page comes with the Notes step.

## Publications
`data/publications.json`, in display order. Conference papers form the
first group; manuscripts and thesis the second; numbering continues.
| Field | Notes |
|---|---|
| `type` | `conference`, `manuscript`, or `thesis` |
| `authors` | your name exactly as in `profile.json` → it's shown bold |
| `status` | manuscripts only: `under-review` or `in-preparation` |
| `pdf`, `doi` | optional; DOI like `10.1234/abcd` |

## Quotes
`data/quotes.json`: `text` (30 words max), `author`, optional `source`.

## Portrait
Replace `static/img/portrait.jpg` (keep the name). A 4:5 photo looks best;
around 720×900 px keeps the page fast.
