<!-- Imported from the design hand-off, 2026-11-04. This file is now the source of truth. -->
# Design system

## Mood
Calm, editorial, research-first. Near-black ocean background, serif
reading text, olive and teal as identity colors. No browns anywhere.

## Color palette (dark theme)
Turn these into named design tokens. Hex values are the approved colors.

Surfaces, darkest to lightest:
- Page background: #060f11 (near-black with a teal tint)
- Surface (header, footer, bands, cards): #0a1a1d
- Raised/inset surface (image placeholders): #0f2326
- Border (dividers, card edges): #142a2d
- Strong border (outline buttons, chips): #2c5154

Text, strongest to softest:
- Headings and emphasis: #f2f7f5
- Body: #e6efec
- Long-form paragraphs: #d3e2df
- Secondary copy, inactive nav: #c3d6d2
- Labels, dates, captions: #a1bbb6

Accents:
- Teal #7fd6cb, hover #b4ece4: links and primary buttons
- Olive #a3b26a: identity (Kawser's name, section titles, current page)
- Light olive #b5c27a: "Planning" status, Learning tag
- Sand #e3c77f: "Ongoing" status, Teaching tag

Color roles:
- Teal means "clickable". Don't use it for decoration.
- Olive is a signature. Use it in a few places per page, not everywhere.
- Primary buttons: teal fill with near-black text.
- Never convey meaning by color alone; pair it with an icon or a word.

## Typography
- Reading and headings: Newsreader (serif), regular, medium, semibold,
  plus italic.
- Interface text (nav, labels, buttons, captions, dates): Lato,
  regular and bold.
- Body around 19px with relaxed line spacing (about 1.65).
- Hero headlines scale fluidly with screen width, roughly 36px on
  phones to 58px on desktop, regular weight, Kawser's name semibold
  in olive.
- Section headings around 32px, medium weight.
- Small labels: Lato bold, uppercase, slightly letter-spaced, in the
  label text color.

## Layout
- Main content width up to about 1120px; the Journey page is narrower
  (about 880px) for a reading-column feel.
- Separate sections with thin border lines or a change to the surface
  color, not with heavy boxes or shadows.
- Rounded corners: about 12px on cards, fully rounded pill buttons.
- Buttons and tappable links at least 44px tall.
- Grids collapse to a single column on phones.

## Components
Header and navigation
- Surface-colored bar with a thin bottom border.
- "Kawser" wordmark in the serif on the left, links on the right,
  wrapping on narrow screens.
- Current page in olive and bold.

Footer
- Surface-colored bar with a thin top border.
- Left: copyright line with Kawser's name and "Built with Astro".
- Right: Email, GitHub, Google Scholar, LinkedIn.

Status badge (research write-ups and notes)
- Three states, always icon plus label:
  - Planning: lightbulb icon, light olive
  - Ongoing: loading/spinner icon, sand
  - Completed: double-tick icon, teal
- A legend explaining the three states sits at the top of the Sketch
  Board section on Home.

Research card
- Large image or demo slot on top, then status and topic, title, and a
  one-line summary. Whole card is one link.

Favorite-quotes marquee (bottom of About)
- A single row of quote cards drifting slowly right to left in an
  endless loop (about a minute per cycle).
- Seamless loop: render the list twice and hide the second copy from
  screen readers.
- Pauses on hover and on keyboard focus.
- With reduced motion turned on: no animation; the row becomes
  swipeable/scrollable instead.
- Edges fade softly instead of cutting cards off.
- Cards: olive opening quote mark, italic serif quote, author in small
  label text. Quotes should stay under about 30 words.

Journey timeline entry
- Three columns: date (right-aligned), the timeline line with a ringed
  dot colored by tag, then the entry card.
- Card: tag label, one to three sentences in larger text, one 3:2 photo
  with rounded corners and a capped width.
- Entries grouped under olive year headings, newest first.
