# Roadmap, definition of done, QA

## Progress log
| Date | Step | Status | Notes |
|---|---|---|---|
| 2026-11-04 | 0 Setup | ✅ done | npm, git multi-account config, GitHub repo, docs pushed |
| 2026-11-04 | 1 Foundation | ✅ done | Astro 6.4 (7.x needs Node ≥ 22.23.4; machine has 22.22.1), Fontsource fonts, tokens, BaseLayout, Header/Nav, Footer, profile.json, temp index |
| 2026-11-04 | 2 Home | ✅ done (pending review) | collections + Zod, status map, Lucide icons, Home sections 1–6, placeholder content from mockup |
| 2026-11-04 | Research page (pulled forward from 6) | ✅ done (pending review) | publications first, then write-ups; nav 6 items |
| 2026-11-04 | Write-up pages (FR-14) | ✅ done (pending review) | `/research/[slug]`, cards link per entry, prose styles, drafts get no page |
| — | 3 About | ⏭ next | awaiting go-ahead |

PM decisions (2026-11-04): `@lucide/astro` approved; schema additions `coverAlt` + `draft` approved, `Topic` enum and `updated` not adopted (topic stays free text).

Write-up pages (2026-11-04): each research write-up gets `/research/<slug>/` in v1 (FR-14); scheduled after step 2's Research page, before step 3. BibTeX: deferred (≈5 entries; JSON is enough), ADR 5 stands.

Structure change (2026-11-04): Publications moved into the Research page as its first section; nav is 6 items; `/publications/` dropped. Home "Full CV →" link unchanged.

Tech debt: `npm audit` flags build-time deps (sharp, esbuild); the fix is Astro 7, which needs a Node upgrade.

## Milestones
Each step ends with: summary of what changed + why → PM review → go-ahead.

| # | Step | Deliverables | You'll learn |
|---|---|---|---|
| 0 | Setup | npm, git repo, GitHub repo, docs committed | — |
| 1 | Foundation | scaffold, tokens.css, fonts, BaseLayout, Header/Nav, Footer, profile.json | Astro project anatomy, components & props, CSS custom properties, file-based routing |
| 2 | Home | hero, legend, research cards, notes, publications, Now, CTA; collections + schemas | content collections, Zod, querying content |
| 3 | About | intro, interest cards, path, looking-for, quote marquee | CSS grid/flex, CSS animation, reduced motion |
| 4 | CV | CV sections, PDF link | semantic HTML for documents |
| 5 | Journey | collection, timeline, year grouping, JS filter | Astro images, progressive enhancement |
| 6 | Research + stubs | Research page (publications, then write-ups); Sketch Board + Notes placeholders | layout reuse, anchors |
| 7 | Ship | Actions deploy, titles, meta, OG, favicon | CI/CD for static sites, SEO basics |

## Definition of done (every step)
- [ ] `npm run build` and `npx astro check` pass with no errors
- [ ] 375px: no sideways scroll
- [ ] Keyboard only: every link reachable, focus visible
- [ ] Lighthouse (mobile): a11y 100, perf ≥ 95
- [ ] axe DevTools: 0 violations
- [ ] Reduced motion on: nothing animates
- [ ] No invented facts; placeholders remain `[bracketed]`
- [ ] Matches mockup look; any deviation listed in the step summary

## Known mockup ↔ brief differences (brief wins)
| Where | Mockup | Brief / decision |
|---|---|---|
| Home hero size | `clamp(38px, 5.4vw, 68px)` | 36–58px, same as other pages |
| Header/footer border | `#16302f` | `#142a2d` (border token) |
| Home hero subline | `#b3c9c5` (off-palette) | `#c3d6d2` (secondary text token) |
| Fonts | Google Fonts link | Fontsource, self-hosted |
| `Home page — dark mode….pdf` (older draft) | nav has The Garden/Now, no Journey/CV; RSS link; Seedling/Budding/Evergreen | brief's nav, no RSS; status vocabulary pending PM decision |

## Takeaways from maggieappleton.com (reference, analysed 2026-11-03)
| Adopt in v1 | Defer | Skip |
|---|---|---|
| Fluid type scale (sizes interpolate between phone and desktop via `clamp()`) | Backlinks between write-ups | Webmentions |
| ~800px prose column on write-up pages | "References & further reading" block on write-ups | RSS (brief) |
| Planted / last tended dates | Subtle title entrance animation (reduced-motion safe) | Light/dark toggle (v1 dark only) |
| Topic tags + status label in post header | Breadcrumb to parent section | |

## Risks
| Risk | Mitigation |
|---|---|
| Placeholder text shipped to advisors | grep for `[` in `dist/` before deploy; a CI check in step 7 |
| Recruiter audience needs a different emphasis later | keep CV data-driven so a recruiter-focused variant is a new page, not a rewrite |
| Content goes stale ("Now" section) | `now.updated` date shown publicly — visible nudge |
