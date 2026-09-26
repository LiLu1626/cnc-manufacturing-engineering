# Doubao Done: 15/16/17 A01-D01 fixes

Commit: 70ce7df

## 16 (A01-A04)
- A01: D offset section rewritten. Formula pocket = 50 - 2d + 2r; table d=4.98/5.00/5.02 -> 50.04/50.00/49.96. First-article stock: d=5.10 (radius) leaves outer oversize/inner undersize. Removed old "reduce D to close pocket".
- A02: Inner pocket direction worked rewritten with 4-edge table using CW order (0,0)->(0,50)->(50,50)->(50,0)->(0,0); bottom edge -X, right side +Y inside = G42.
- A03: D defined as selecting cutter-size register; examples assume Setting 40=RADIUS. Q4 answer lists RADIUS 5->6 and DIAMETER 10->12. Lathe section: D is not nose radius; nose radius/orientation are separate T fields. Limitations Z-offset sentence scoped to G17.
- A04: Lead-in code rewritten to build comp on extension line (-15,-5)->(-5,-5), then tangent to (0,0). Lead-in SVG redrawn: tool center y=150, edge y=180, gap = r. Removed unsupported "0.5 step" and "accept witness mark" advice.

## 17 (B01-B04)
- B01: Why/modal/Common Mistakes now distinguish bare X/Y repeat vs explicit G00 cancel on Haas; still recommend explicit G80.
- B02: Through/blind depth rewritten with h=(D/2)/tan(a/2); 118°=0.3004D, 135°=0.2071D. Practice 1 recalculated: h=3.61, tip to Z-18.61+. Breakthrough.
- B03: G82 dwell no longer "flattens bottom"; flat bottom needs flat-bottom/counterboring tool. Spot drill section same. G85: bore diameter from bar radial set / reamer effective diameter.
- B04: Example reordered: G43 H01 Z50 before XY; G94 added; end split Z50/M09/M05. G84 example S500 pitch 1.25 F625; return feed control-specific. P decimal convention P0.5. Removed duplicate Verification paragraph; restored Common Mistakes h2.

## 15 (C01-C03)
- C01: Plane section lists G17 I/J, G18 I/K, G19 J/K. Lathe section: X20->X30 = 5mm radial, chord sqrt(50)=7.071, not arc radius.
- C02: Wrong I/J section: distances mismatch -> alarm (S(0,0),E(50,0),wrong C(20,0): 20 vs 30). Quarter circle S(0,10)/C(10,10)/E(10,0) = G03 90°. Backwards swap note: other blocks unaffected. R+ now ≤180°.
- C03: Arc feed: F = tool-center feed, vc separate; example inside R20 tool R5 -> center R15, F225, time 0.419 min. Helical fragment declares entry conditions and helix angle 1.82°. Removed duplicate small-radius and full-circle paragraphs.

## D01
- All three pages now have Sources with official Haas links.
- Word counts: 15=2023, 16=2091, 17=2267; each 2 SVGs.

Static source review only.
