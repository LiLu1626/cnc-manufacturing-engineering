# Doubao Done: 12/13/14 v3 (R01-R06)

Commit: 4756aac

## R01 12 old paragraphs synced
- Concept/callout now say "gauge line" throughout, not spindle nose.
- Method table: only the positive-length setter method; other conventions explicitly out of scope.
- Checklist: removed "shorter tools need negative H"; now says H = measured gauge-to-tip length.
- Example walk-through: references Zm = W + Zp + H; missing H leaves G49 state at W+Zp.
- Example code: added G21/G17/G90/G94 G40 G49 G80, G54 on its own block, center-cutting and clearance stated.
- Nose radius: orientation field separated from T word; removed "1-9" and "T-number".
- Removed "leading cause of scrap" ranking.

## R02 12 SVGs
- First SVG redrawn at 1 px/mm: gauge y=50, L=120 tip y=170, L=60 tip y=110 (2:1 ratio).
- Second SVG redrawn at 0.5 px/mm: gauge -130 at y=50, tip -250 at y=110, part top W=-300 at y=135 (50 mm gap visible).

## R03 13 formula figure and wording
- First SVG now: G54 origin (-145,-115) + program point (10,20) = machine point (-135,-95). No "machine zero" box.
- Concept: reference return position; machine point = G54 origin + P.
- Touch wording: "tool tip touches top; gauge-line machine Z reads -180".
- +X: relative to part, per machine axis convention.
- Verification: re-read offsets against setup sheet; do not jog to Z0 on unverified offset.
- Rotary section: three separate concepts (axis zero offset, G68 coordinate rotation, dynamic offset).

## R04 G94 in code
- 13 example code now has G94.
- 12 example code now has G21/G17/G90/G94 G40 G49 G80, G54 standalone.

## R05 14 SVG and old paragraphs
- First SVG viewBox 360x230, start (50,200), end (290,40), rapid corner (290,200); 4 px/mm consistent (ΔX=240px=60mm, ΔY=160px=40mm).
- Duplicate chamfer paragraph rewritten as part-profile (9.5,10)->(10,9.5), not tool center.
- Diameter travel: Δr = (Xend-Xstart)/2, X30->X40 = 5 mm radial; removed "50% off".
- G01 section chip load: nominal fz = F/(n*z), actual depends on engagement.

## R06 Sources
- 12 added Haas Setting 40 S40 and Mill Part Setup.
- 13 added G154 and Mill Part Setup; removed guessed mill-work-offsets URL.
- Removed "second most common scrap" ranking.

Word counts: 12=2435, 13=2329, 14=2195. Each 2 SVGs. Static source review only.
