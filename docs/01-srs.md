# Software Requirements Specification (SRS)
Version 0.1 · 2026-11-03 · Owner: Kawser (PM) · Dev: Claude

Source of truth for *what* we build. Design detail lives in the hand-off
(`../kawser-site-handoff/docs/`); this file does not repeat it.

## 1. Purpose
A static personal research site. Success test: an advisor opening it
from an email understands within seconds what Kawser wants to research
and how he thinks.

## 2. Users
| Priority | User | Needs |
|---|---|---|
| 1 | PhD advisors, admissions committees | Research interests, publications, CV, evidence of thinking (write-ups) |
| 2 | Data-science recruiters (later) | Skills, projects, experience, CV PDF |
| — | Kawser (content author) | Add/edit content by editing Markdown/JSON only |

## 3. Scope
**In (v1):** Home, About, CV, Journey; placeholder pages for Sketch
Board, Research, Notes, Publications; deploy to GitHub Pages.
**Out (v1):** light theme, MDX, D3, three.js, BibTeX, generated OG
images, RSS, analytics, comments, CMS, backend.

## 4. Functional requirements
| ID | Requirement |
|---|---|
| FR-01 | Every page shares a header (wordmark + nav) and footer (copyright, contact links). |
| FR-02 | Nav order: Sketch Board, Research, Notes, Publications, About, Journey, CV. Current page marked with `aria-current="page"` and olive/bold. |
| FR-03 | Home shows hero, status legend, 3 latest research cards, notes + paper notes, publications + "Now", closing CTA. |
| FR-04 | About shows intro + portrait, 3 research-interest cards, path so far, what I'm looking for, quotes marquee. |
| FR-05 | CV shows header with contact + PDF download link, and 8 sections (see pages.md). PDF is a static file, not generated. |
| FR-06 | Journey shows entries grouped by year, newest first, with tag filter chips. All entries visible without JavaScript. |
| FR-07 | Placeholder pages render title, one sentence, "coming soon". No broken nav link. |
| FR-08 | Publications render from one JSON file on both Home and CV; Kawser's name bolded automatically. |
| FR-09 | Profile data (name, email, links, "Now") comes from one file, used everywhere it appears. |
| FR-10 | Invalid content (missing field, wrong tag, bad date) fails the build with a clear message. |
| FR-11 | Each page has its own `<title>`, meta description, Open Graph title/description/image; site has a favicon. |
| FR-12 | Push to `main` builds and deploys automatically. |

## 5. Non-functional requirements
| ID | Category | Requirement | Verified by |
|---|---|---|---|
| NFR-01 | Accessibility | WCAG 2.2 AA contrast; visible focus; labelled icon links; alt text on all photos; pinch-zoom never disabled | axe DevTools + Lighthouse a11y = 100 |
| NFR-02 | Motion | All animation disabled under `prefers-reduced-motion` | OS setting toggle, manual |
| NFR-03 | Responsive | Works at 375px with no horizontal scroll | DevTools device mode |
| NFR-04 | Performance | Zero JS except Journey filter; Lighthouse performance ≥ 95 on mobile | Lighthouse |
| NFR-05 | Maintainability | Content changes never require touching code | Add a Journey entry without editing `src/` outside `content/` |
| NFR-06 | Portability | Static output only; host-agnostic | `astro build` produces plain `dist/` |
| NFR-07 | Integrity | No invented facts; placeholders stay in `[brackets]` | Review before each deploy |

## 6. Constraints
Astro (static), plain `.astro` components, plain CSS with custom
properties, Fontsource fonts, Lucide-style icons, GitHub Pages. New
dependencies need PM approval.

## 7. Acceptance (v1 done when)
All FR/NFR verified on the deployed URL, on a phone and a desktop, with
JavaScript on and off.
