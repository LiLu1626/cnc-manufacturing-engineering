# Batch A Completion Report

Commit: `b73d866`

## A1 — Arc page (15)
- Corrected: G02 clockwise from 180°→90°→0° passes through (25,+25) = **upper** semicircle
- Corrected: G03 counterclockwise from 180°→270°→360° passes through (25,−25) = **lower** semicircle
- Fixed arc length formula: L = 2πr×θ/360 (was missing factor of 2)
- Semicircle: 2π×25×180/360 = 78.540 mm ✓
- 90° short arc: 2π×20×90/360 = 31.416 mm ✓
- Practice Q1: 2π×30×90/360 = 47.124 mm ✓
- Added 2 inline SVG diagrams: upper/lower semicircle comparison, 90° short arc
- Code blocks now labeled as independent examples (not consecutive code)
- Removed the "short vs long arc on opposite endpoints" mistake (both are 180°, it's CW/CCW)

## A2 — Subprograms (29) and Threading (22)
- Page 29 Common Mistakes: G80 explanation replaced with Haas-accurate wording
- Page 22 "Why It Matters": replaced absolute "always G97 never G96" with bounded teaching example language
- Page 22 Common Mistakes: replaced with "using a spindle mode not verified for this cycle"
- Page 22: removed UN/trapezoidal/buttress parenthetical generalization

## A3 — Navigation and template
- Chain rebuilt: 01→02→**23**→08→32→... (page 23 now in main chain)
- 38 pages bottom nav regenerated
- 31 pages upgraded from flat nav to structured site-nav-inner

## Remaining (not done in this batch)
- Homepage (cnc-programming/index.html): 7 module entries and old anchors
- Learning path page (31): restructure to 7 modules
- Sitemap: remove 15 alias URLs, keep 41 main + 102 other = 143
- Pages 10, 11, 39: six-section structure
- B07: all 40 pages to word-count minimums (B=800, K=2000) with SVGs
- No controller simulation performed; all checks are static source review
