# Architecture
How the site is built, and why. Backend analogy where it helps.

## 1. Build pipeline
```
Markdown / JSON  ──►  Zod schemas  ──►  .astro pages/components  ──►  static HTML+CSS  ──►  GitHub Pages
 (content)          (validation)        (templates, run at build)       (dist/)              (CDN)
```
Astro is a **static site generator**: all code runs once, at build time,
on your machine or in CI. The visitor's browser receives finished HTML.
Think of it as a Python script that renders Jinja templates to files —
there is no server at request time.

## 2. Folder layout
```
kawser-site/
├─ .github/workflows/deploy.yml   CI: build + deploy on push to main
├─ docs/                          these documents
├─ public/                        copied as-is: favicon.svg, cv.pdf, og.png
├─ src/
│  ├─ content.config.ts           collection schemas (the "DB schema")
│  ├─ content/                    one folder per collection
│  │  ├─ research/  notes/  paper-notes/
│  │  └─ journey/2026-xx-gre/     index.md + photo.jpg (co-located)
│  ├─ data/                       profile.json, publications.json, quotes.json
│  ├─ lib/                        pure TS helpers: status map, author bolding, grouping
│  ├─ components/                 reusable UI pieces
│  ├─ layouts/BaseLayout.astro    <head>, header, footer, meta tags
│  ├─ styles/                     tokens.css (design tokens), global.css (reset + base)
│  ├─ assets/                     portrait, images processed by Astro
│  └─ pages/                      one file = one URL (file-based routing)
├─ astro.config.mjs
├─ package.json
└─ tsconfig.json
```
Rule of thumb: `content/` + `data/` = what you edit; everything else =
code you rarely touch.

## 3. Component inventory
| Component | Used on | Notes |
|---|---|---|
| `BaseLayout` | all | props: `title`, `description`, `ogImage?` |
| `Header` / `Nav` | all | reads current URL to set `aria-current` |
| `Footer` | all | links from `profile.json` |
| `Icon` | many | one wrapper so stroke width stays consistent |
| `Button` | many | `variant: primary \| outline`, min 44px tall |
| `SectionHeading` | many | label + title pattern |
| `StatusBadge` / `StatusLegend` | Home, Notes | icon + word, never color alone |
| `ResearchCard` | Home, Research | whole card is one `<a>` |
| `PublicationList` | Home, CV | groups, continuous numbering, bolds name |
| `QuoteMarquee` | About | CSS-only animation, duplicate list `aria-hidden` |
| `TimelineEntry` | Journey | date · dot · card |
| `CvSection` | CV | olive title left, entries right |
| `PlaceholderPage` | 4 stubs | title + sentence + "coming soon" |

Components are like classes with a constructor (props) and a render
method (the template). Each owns its scoped CSS.

## 4. Styling
- `tokens.css`: every color, font, size, radius as a CSS custom property
  (`--color-teal`, `--radius-card`). Components reference tokens, never
  raw hex. Changing a token changes the whole site — like a config file.
- Astro scopes a component's `<style>` to that component automatically,
  so class names don't collide.
- Mobile first: base styles target phones; `@media (min-width: …)`
  adds desktop layout.

## 5. JavaScript budget
| Page | JS | Why |
|---|---|---|
| Journey | ~1 KB inline | chip filter; progressive enhancement, all entries render server-side |
| All others | 0 | marquee and hover states are pure CSS |

## 6. Decision records (ADR, short form)
| # | Decision | Why | Rejected |
|---|---|---|---|
| 1 | Astro, static | content site; zero JS by default; Markdown native | Next.js (React + runtime overhead), Hugo (Go templates, weaker typing) |
| 2 | Content collections + Zod | build-time validation = schema enforcement without a DB | loose frontmatter |
| 3 | Plain CSS + tokens | small site, full control, nothing to learn twice | Tailwind |
| 4 | Fontsource | self-hosted: faster, no Google tracking, works offline | Google Fonts `<link>` |
| 5 | JSON publications | 4 entries; trivial to edit | BibTeX (revisit at ~10) |
| 6 | GitHub Pages + Actions | free, official Astro action, deploy on push | Netlify/Vercel (fine, but extra account) |
| 7 | Manual minimal scaffold | no template cruft; you see every file and why it exists | `npm create astro` starter |
