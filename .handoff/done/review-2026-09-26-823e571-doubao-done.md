# Doubao Done: 12/13/14 v2 fixes

Commit: 823e571

## A: 12 unified gauge-line teaching model
- Adopted model: L = H = +120 (gauge line to tip), W = -300 (part top machine Z), Zp = 50.
  Gauge stops at Zm = W + Zp + L = -130; tip at Zm - L = -250 = W + Zp.
  With G49: gauge at W + Zp = -250; tip at -370 = W - 70 (120 mm too low; crash not assumed).
- Rewrote G43 block, second SVG, "forget G43" section, Q1 (now asks for W and H), and the sign-on-H mistake.
- Lathe X wear: states diameter-field vs radius-field units explicitly; removed "entering radius halves diameter" claim.
- Lathe Z correction: removed +0.015; now -0.03 on linear Z (no factor).
- H/D: states Haas Setting 40 RADIUS/DIAMETER; D entry is 6 or 12 accordingly.
- Q4: reframed as "why explicit G43 after T01 M06" with auto-recall caveat.
- First SVG: now shows shared gauge line, long vs short tip; no undefined Z80/Z110.

## B: 13 same coordinate chain
- Edge finder: "radius = half diameter"; mechanical vs calibrated probe radius not added twice.
- Z touch: gauge touches top at -180, L=120, W = -300 (not copying -180 into G54).
- Removed master equation "machine zero + work + tool = tip"; replaced with program-point wording.
- Position vs size: width errors are NOT fixed by translating G54.
- G54.1: replaced with Haas G154 P1-P99 plus FANUC G54.1 note.
- Removed "first piece thermal negligible", "fixture broken if datum shift every run".
- G54->G55: Z and other axes also shift; envelope planning.
- Forget G54: may inherit G55 etc.; G53 non-modal; not guaranteed crash.
- Example: G21/G17/G90/G94, center-cutting plunge assumption, fixture clearance.

## C: 14 code/geometry
- Program snippet: G43 Z50 before XY; added G21/G17/G90/G94; center-cutting tool stated.
- Chamfer: explicit lathe endpoints (X38,Z0)->(X40,Z-1), C1; mill (9.5,10)->(10,9.5); no "+X1." incremental confusion.
- X40 radial: stated current diameter 30 -> 5 mm radial move.
- Facing: part X0..50, Y-5..5, Oslash;16 cutter (r=8), center at Y0; overhang 10 > r=8; Y coverage Y+/-8 covers Y+/-5. SVG redrawn to 4px/mm scale with cutter circles.
- Three sides: now bottom Y=0, right X=40, top Y=20; missing left X=0; not called open pocket.
- G00 SVG: explicit two-block G00 X60 then Y40; 4px/mm scale.
- Removed "25/50% guarantees feed hold", "crash waiting to happen", block-skip "first half" claim.
- 5-axis: notes kinematics/TCP caveat.
- Diagonal chip load: nominal fz = F/(n*z); actual thickness depends on engagement.

Word counts (excluding pre/svg/nav/footer/section): 12=2295, 13=2279, 14=2194. Each page still has 2 SVGs.

Static source review only; no browser or controller verification.
