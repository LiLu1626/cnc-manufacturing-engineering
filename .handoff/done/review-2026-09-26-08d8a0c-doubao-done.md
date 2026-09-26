# Doubao Done: 18/19/20 second-round fixes (ec03d46)

## 19 (R01/R02)
- Finish pass now writes S1500 and X39.5; rough X41; trace table and feed calc match (15 s rough, 20 s finish at 150 mm/min over 50 mm).
- Startup block: G21 G18 G97 G99 G40, G54, T0101.
- Face retract split: G00 Z1. then G00 X47. (separate blocks); OD retract X47 then Z2.
- Jaw/bar projection stated (jaw ~Z-65, projection to reach Z-50).
- Removed "T0102 always wrong" and "Z+ may crash"; nose-radius and past-center language softened.
- SVG2 arrow text no longer points right.

## 20 (R03/R04/R05)
- Removed wrong pass table (39.5/40.4) and duplicate program template.
- Added contour block trace: (30,2)→(30,0)→(30,-20)→(36,-20)→(36,-40)→(52,-40); explicit Z-then-X at shoulder = step, not taper.
- Added allowance table: O30/O30.4, O36/O36.4, shoulder -20.0/-19.9.
- Main example now has G21 G18 G97 G99 G40, G54.
- Wear example: measured 30.10 vs 30.00 → reduce X wear 0.10 diameter (0.05 radius), sign convention noted.
- Alarm paragraph: identify Type I/II before checking monotonicity; removed "Z in P alarms".
- SVG1: r18.2 y=107.2; Z0 label moved to x355.
- SVG2 replaced with magnified shoulder: red finished, green dashed after-rough, 0.2 radial / 0.1 axial.

## 18 (R06/R07)
- G43 move now G00 G43 H01 Z50.
- Trace table no longer claims XY is on the G81 line; shows pre-position.
- G80 section: bare XY repeats; explicit G00/G01 exits; G80 doesn't move Z; ends at R2.
- Setup checklist separates R entry clearance from inter-hole retract clearance.
- Why text: two-hole hand fragment vs independent four-hole example.
- Practice 2: removed "guaranteed safe".
- "Five steps" renamed to "Basic Cycle Motions and Repeat Control".
- Tapping fragment: states G21/G94, prepared tap drill, S500.

Word counts (Doubao strip): 18=1922, 19=1920, 20=1864; each 2 SVGs. Static source review only.
