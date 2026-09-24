# v9 Fix Report — B01–B08 Engineering Fixes

Commit: `bd39617`

## Fixed in this round

### B01 (P1) — Milling project drilling cycle
- Replaced G81 with G83 peck drilling (Q3)
- Added explicit `G00 X10. Y10.` before cycle start
- Removed G00 between holes (was canceling cycle mode)
- Added `G00 Z2.` before first Z plunge to match text
- Updated source reference from G81 to G83

### B02 (P1) — Cutter compensation direction
- Rewrote page 16 with verified coordinate table: (0,0)→(0,50)→(50,50)→(50,0)→(0,0)
- CW outer profile + G41 keeps tool outside (X=-5, Y=55, X=55, Y=-5 midpoints)
- Practice Q1 answer corrected to G41 with full trace
- Added lead-in/out code example

### B03 (P1) — Subprograms drift
- Rewrote with absolute coordinates only (no G91 in subprogram)
- O2000 is now a real subprogram identifier
- Main program restores G90 before each call
- Subprogram exits at G90 G00 Z50. before M99
- Corrected G80 explanation: cancels mode, does not retract

### B04 (P1) — Arc direction
- Removed "Wait... Let's redo... but wait" draft text
- S(0,0)/C(25,0)/E(50,0): G02 lower semicircle, G03 upper semicircle
- Practice Q1: S(0,0)/C(30,0)/E(30,30) short 90° arc = G02 (47.124 mm)
- Added regression example: S(0,0)/C(0,20)/E(20,20) G03 short arc 31.416 mm

### B05 (P1) — CSS paths and compat pages
- 34 pages: all `../assets/css/` → `/cnc-manufacturing-engineering/assets/css/`
- 15 compat redirect pages: all links now absolute paths, no auto-refresh
- All compat pages have proper site-nav and canonical

### B06 (P2) — Navigation order
- 37 main chain pages: bottom nav regenerated from correct course order
- Page 39: added canonical, description, bottom nav
- 6 pages (08,09,10,11,23,32): `cp-back` → `back-link`
- Service pages 30, 40: nav corrected

### B08 (P2) — Threading semantics
- "Why It Matters": changed from "feed per rev changes" to encoder synchronization explanation
- G96 issue: RPM change breaks sync between passes, not the feed math
- Common mistakes updated accordingly

## Remaining: B07 (content expansion)
- B-type pages need 800+ words (currently 216–664)
- K-type pages need 2000+ words (currently 219–901)
- All 40 pages need embedded SVG diagrams
- Page 39 needs 20 practice questions + code review + project assessment
- This is the largest remaining task and has not been started in this round
