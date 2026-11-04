# Roadmap

Requirements and design decisions are in the original Astro project:
`../kawser-site/docs/` locally, or the `docs/` folder on the `astro` branch
on GitHub (SRS, pages, design system). This project follows them; only the
technology differs.

## Progress log
| Date | Step | Status | Notes |
|---|---|---|---|
| 2026-11-04 | First build | ✅ done | Flask + Frozen-Flask; Home, About, Research, write-up pages; 4 stubs; screenshots match the Astro build |
| — | CV | next | see `../kawser-site/docs/06-pages.md` § CV |
| — | Journey | | timeline + year grouping; the chip filter needs a little JavaScript |
| — | Notes, Sketch Board | | |
| — | Ship | | GitHub Actions: `pip install` → `python build.py` → deploy `build/` to Pages; 404 page; Open Graph tags; favicon |

## Differences from the Astro site
| Area | Astro site | Here | Why |
|---|---|---|---|
| Images | resized to WebP automatically | served as-is | keeps it simple; resize the portrait by hand if the page feels slow |
| Icons | `@lucide/astro` package | the SVG shapes are copied into `templates/components/icons.html` | no package needed |
| Fonts | Fontsource npm packages, every language subset | Latin `.woff2` files copied into `static/fonts/` | no npm; Latin covers the site's text |
| CSS scoping | automatic per component | prefixed class names + per-page CSS files | plain CSS has no scoping |
| Footer credit | "Built with Astro" | "Built with Flask" | |
| `<link rel="canonical">` | present | not yet | add in the Ship step with the site URL |

## Checks before each step is "done"
- `python build.py` finishes with no errors
- 375px wide: no sideways scrolling
- Keyboard only: every link reachable, focus visible
- Reduced motion on: the quote marquee doesn't move
- No invented facts; placeholders stay `[bracketed]`
