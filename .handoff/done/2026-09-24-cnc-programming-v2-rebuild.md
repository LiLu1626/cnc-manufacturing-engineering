# CNC Programming v2 Rebuild — Completion Report

## What was done
Rebuilt all 40 CNC Programming pages per ChatGPT SPEC and 14-point review.

## R-findings addressed
- R01: Page 23 teaches proper restart procedure (rebuild modal state, not jump-to-line).
- R02: Page 28/20 uses SPEC dimensions: 100×80×12 plate, pocket X30-70/Y25-55, R5, holes at corners, Z-13.8.
- R03: Pages 10/22 use Haas G99 (not G95) for feed/rev; Haas G76 K/D format (not FANUC two-line).
- R04: Page 12 signed geometry chain: longer tool with under-stored H cuts DEEPER.
- R05: Page 24 states dry run at raised Z does NOT prove no collision.
- R06: Page 27 turning project has monotonic Z contour, no parting off.
- R07: Page 34 subprograms build a real 4×3 grid with X reset and Y advance.
- R08: Page 36 macros use N labels, input validation, divide-by-zero protection.
- R09: Page 15 SVG arc corrected (A 20 20 0 0 1 20 20, center at 0,20).
- R10: Page 39 notes G00 cancels canned cycle on Haas.
- R11: Page 37 G31 records positions, does not auto-update offsets.
- R12: All pages expanded with lead/objectives/examples/practice/sources.
- R13: Prev/next nav follows SPEC module order; homepage groups by level.
- R14: Template uses body.cnc-programming, main.article, class="active" nav.

## Files
- 40 content pages in docs/cnc-programming/
- Homepage rewritten with level-grouped lesson list
- Old v1 directories removed
- Generator: gen_cp2.py

## Known gaps
- Word count: many pages are 500-800 words vs SPEC 800-3000 target. Further expansion needed in review pass.
- SVG diagrams: only page 15 has an SVG; other pages need more visuals.
- Controller-specific pages (38) are brief.
