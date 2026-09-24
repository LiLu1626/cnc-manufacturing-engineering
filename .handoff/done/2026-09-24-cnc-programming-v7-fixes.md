# CNC Programming v7 — Fix Report (Z01, Z02, thread gauge terms)

## Z01 [P1] G41 outer profile overcut — FIXED
- The corrected program path was counter-clockwise with G41, pushing tool center inside the block.
- Reversed to clockwise: up left edge → across top → down right → along bottom.
- With G41 (left of travel), tool center now sits outside on every side:
  - Up left edge (+Y): left = -X = outside ✓
  - Across top (+X): left = +Y = outside ✓
  - Down right edge (-Y): left = +X = outside ✓
  - Along bottom (-X): left = -Y = outside ✓
- Added explanation of why clockwise + G41 = outer profile.

## Z02 [P2] Startup assumptions incomplete — FIXED
- Added G21 G17 G94 G40 G80 G49 to startup block.
- Reordered: G43 H01 Z50 BEFORE first G00 X-10 Y-10 (Z established before XY rapid).
- Added M08 coolant, M09 M05 at end.
- Stated assumptions explicitly: D05=5.0mm radius, H01 tool length, G21 metric, G94 mm/min.

## Thread gauge terminology — FIXED
- External thread: 6g tolerance class, verified with thread ring gauge (go/no-go).
- Internal thread: 6H tolerance class, verified with thread plug gauge.
- No longer conflates the two.

## Still remaining
- V02 milling pocket toolpath
- V09 turning facing + setup
- V12 content depth
- X04 homepage integration
