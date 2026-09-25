# Completion Report — 0538c5d four-batch fixes

Commit: 08d1e44 (on top of 0538c5d). Static source review only; no browser verification, no controller simulation, no machine test.

## Batch 1 — 03 Coordinate Systems
- Deleted paragraph claiming +Z uniquely predicts +X on any machine.
- Mill X/Y bullets rewritten as tool-relative-to-workpiece displacement.
- Lathe X restricted to "this page's diameter mode"; cross-center/rear-turret noted as exceptions.
- Rotary direction rule rewritten: thumb along +linear axis, curled fingers = positive rotation.
- Machine zero/home/reference no longer conflated; builder-defined relationship noted.
- Work offset formula simplified to XY translation: machine = G54 origin + programmed coord; Z separated as H-offset chain.
- Z touch-off rewritten: H offset set first, then workpiece Z datum; no direct spindle-nose write.
- Edge finder example: outer edge contacts left edge, spindle center at -203; omit +3 = 3 mm error, wrong sign = 6 mm.
- Error list: "lathe X always diameter" and "full tip diameter" corrected; G28 bullet changed to "misreading G90/G91 state."

## Batch 2 — 06 Modal Codes
- G81/G00 rule: explicit Haas statement — Group 09 vs Group 01, but G00/G01 still cancels; G80 is explicit.
- Q5 answer: G00 executed cancels cycle on Haas; units/plane/compensation still inherited.
- Two-branch explanation: (A) G00 Z50 after G81 cancels; (B) bare XY after G81 repeats drill.
- F200 wording: G90/G01 are different G groups; F200 is a held numeric value, not a third group.
- First-cut feed: restated with G94 F200 → G00 → G01 F200 trace.

## Batch 3 — 08 Programming Math
- Lathe X error list restricted to diameter-mode.
- atan bullet rewritten: atan(y/x) cannot distinguish opposite-direction vectors; references (-40,-20) atan2 example.
- Rounding statement: independent absolute holes do not accumulate by count; incremental chains do.
- SVG angle arc endpoint corrected to (272.761, 147.428), on a R30 circle centered at (300,160).
- I/J/R section names Haas mill G17 as the selected controller/plane.
- Sources: added Haas G02/G03 link.
- Expanded chord/arc/sagitta explanation ~200 words; clarifies none of the three numbers are interchangeable.

## Batch 4 — Six-section restructure
All three pages now have Concept → Why It Matters → How It Works → Example → Common Mistakes → Practice → Sources. Sub-topics demoted to h3.

## Counts (same method)
| Page | Words | SVGs |
|---|---:|---:|
| 03 | 2202 | 3 |
| 06 | 2065 | 2 |
| 08 | 2399 | 2 |

## Residual
- CSS/template/visual acceptance still on the fixed checklist, not done.
- All teaching values are classroom assumptions, not tooling recommendations.
