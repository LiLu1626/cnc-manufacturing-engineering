# Doubao Done: 15/16/17 R01-R08

## 16
- R01: d=4.98 center nearer wall cuts more -> 50.04; d=5.02 farther cuts less -> 49.96. Table Effect column aligned. First-article d=5.10 note kept.
- R02: Lead-in rebuilt per skeleton: G40 (0,-20); G41 to (0,-10) on +Y extension, center X=-5; to (0,0); contour; extend to (-10,0); G40 to (-20,0). Trace table included.
- R03: Lead-in SVG redrawn 5px/mm: edge y180, center y155, circle r=25 touching edge. Inner pocket SVG now has CW arrows on all four sides and coordinates.

## 17
- R04: Old 0.3D/nub paragraph replaced with h=(D/2)/tan(a/2). Tip Z = -(D_full+h); example Ø10/118°, D_full=12, h=3.004, tip -15.004. Drill-point SVG rebuilt at 5px/mm (plate y30-90, shoulder y90, tip y105). R-plane figcaption marked schematic/not to scale.
- R05: Q=G73/G83 not exclusive; P=cycles with dwell, P0.5; F=G21/G94 mm/min, fn for mm/rev. Removed "R2-3 always safe", "G98 to Z50", "G83 safe choice", ">3D must G83". Center drill vs spot drill separated.

## 15
- R06: Modal G02/G03 inheritance stated; after swapping a direction word, check all following blocks omitting motion code.
- R07: Inside/outside feed merged into R20/r5/F225 example. I/J start-offset limited to Haas. Viewing directions explicit: G17 +Z, G18 +Y, G19 +X. Removed "10-second check" and CAM generalization.
- R08: Helical demoted h3; Example h2 added to 16; Inner vs Outer demoted h3.

Word counts: 15=2037, 16=2209, 17=2343; 2 SVGs each. Static source review only.
