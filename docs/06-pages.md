<!-- Imported from the design hand-off, 2026-11-04. This file is now the source of truth. -->
# Pages (v1: Home, Research, About, CV, Journey)
Visual reference: original hand-off mockups (not in repo).


## Home
1. Hero
   - One sentence leading with the research interest, currently:
     "Kawser explores how people can understand and trust what vision
     models see." (Kawser may revise it.)
   - A short supporting line: research areas, current role, MS degree.
   - Two buttons: read the research (primary), CV and publications
     (outline).
2. My Sketch Board
   - Section title, one-sentence explanation, and the status legend
     (Planning, Ongoing, Completed).
3. Research write-ups
   - Three most recent cards from the research collection.
   - Short note under the heading: question, method, results, what I
     learned.
4. Notes and Paper notes, side by side
   - Notes: title plus status, newest first.
   - Paper notes: paper title plus venue and year.
5. Publications and Now (on a surface band)
   - Publications: the conference paper on its own under a "Conference
     paper" label, then "Manuscripts & thesis" continuing the numbering.
     Kawser's name bold in every author list. Link to the full CV.
   - Now: what Kawser is working on this month, with an "updated" date.
6. Closing call to action: reach out about PhD opportunities and
   collaborations, then the footer.

## About
1. Intro
   - Small "About" label.
   - Headline, currently: "I'm Kawser, an engineer, teacher, and
     researcher asking why AI and computer vision systems make their
     decisions, and whether we can trust them." Use the mockup text as
     the source, but fix the doubled period at its end.
   - Two short paragraphs: personal background and motivation, then
     current work.
   - Portrait slot beside the text, stacking below on phones.
2. What I want to research
   - Three cards: Computer Vision (teal camera icon), Trustworthy &
     Explainable AI (olive question icon), Extended Reality (sand
     headset icon). Each with a one-line reason it matters to Kawser.
3. Two columns
   - The path so far: a short timeline of roles and degrees (years on
     the left, role and one line on the right).
   - What I'm looking for: PhD start term, kinds of labs, buttons to get
     in touch and view the CV, and a small "Outside work" box.
4. Favorite quotes marquee
   - Label "Favorite quotes", heading "Words I keep coming back to".

## CV
- Header: "Curriculum Vitae" label, full name, location, contact links,
  a Download PDF button and a "last updated" note.
- The PDF is a file Kawser drops into the public folder; the page links
  to it. Do not generate the PDF.
- Sections, each with an olive title on the left and entries on the
  right, a date column for each entry, stacking on phones:
  - Research interests
  - Education (MS in Computer Science, Data Science focus, East West
    University, with thesis title and advisor placeholders)
  - Publications (conference paper; then two manuscripts and the MS
    thesis)
  - Research projects
  - Experience
  - Teaching & training
  - Skills (list only what Kawser has actually used)
  - Writing samples (placeholder, coming soon)

## Journey
- Header: "Journey" label, headline "Small steps, written down as they
  happen.", one intro sentence.
- Filter chips: All, Milestone, Learning, Teaching, Life. Filtering is
  a small enhancement; without JavaScript, all entries show.
- Timeline grouped by year, newest first.
- Seed entry: "Took the GRE today. Riding on the high point of a
  month-long effort." (Milestone; date is a placeholder.)

## Research
Publications live here as a section; there is no separate Publications
page (PM decision 2026-11-04).
1. Page title and a one-sentence intro.
2. Publications (`id="publications"`, first on the page)
   - Same grouped, numbered list as Home and CV (`PublicationList`).
3. Write-ups
   - Every published research write-up as a card, newest first, with
     status badge and topic. Drafts excluded.

## Placeholder pages
- Sketch Board, Notes: title, one sentence,
  "coming soon". They exist so navigation never leads to a missing page.

## Site-wide
- Each page gets its own title and meta description.
- Open Graph title, description and image for link previews.
- A simple favicon.
