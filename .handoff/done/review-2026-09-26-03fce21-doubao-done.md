# Doubao Done: S01–S05 (51f0ebb)

## S01 (19)
- Finish code: G00 X39.5 Z2.
- Trace row updated to X39.5.
- Removed duplicate old G21 G97 G99 / T0101 / S1000 startup; one startup block remains.

## S02 (20)
- Main example startup now G21 G18 G97 G99 G40 + G54.
- Shoulder zoom SVG: after-rough shoulder moved to x204 (+Z side of finished at x200), labels added, +Z direction noted.

## S03 (18)
- G80 paragraph replaced: bare XY repeats, explicit G00/G01 exits, G80 doesn't move Z, ends at R2, Z50 not universal.
- Practice 2 answer updated to R2 / verified Z50.
- Tool-change bullet: end pattern explicitly, next tool rebuilds; no "first move always drills".

## S04 (19)
- Z50 vs Z-50: removed "crash into chuck" causal.
- T0102: only wrong unless register calibrated and intentional.
- Facing past center: X-1 is a confirmed classroom assumption.

## S05
- Added normal-vs-interrupted cycle, G98-before-obstacle (18); axial reach vs tool envelope (19); U0.4=0.2 radial, W0.1 shoulder shift, G71 vs G70 F source (20).

Word counts (Doubao strip): 18=2077, 19=2003, 20=1993; each 2 SVGs. Static source review only.
