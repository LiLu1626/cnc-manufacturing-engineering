# Doubao Done: 09/10/11 fixes per review 8f6591c

Commit: 1a93e54

## Fixes applied

### 09 M-code (B class)
- M30 now correctly described as ending program and stopping spindle/coolant; explicit M09/M05 documented as teaching order, not required because M30 would otherwise leave them on.
- M06 now described as automatically stopping spindle/coolant and moving to tool-change position; M05 explicit is teaching habit, not required.
- Removed "cannot cancel M03 with another M-code"; replaced with separate state tracking (spindle/coolant/program).
- Coolant timing: M08 on its own block at clearance, not on first plunge line; SVG redrawn as three boxes (safe position → M08 → cut).
- M-codes execute at end of block; order expressed by separate blocks, not word order.
- Example labeled "teaching snippet"; added G94, G43 H01 at Z50 before XY; assumptions listed.
- TSC on Haas is M88/M89; M07 not universal.
- M03 direction clarified (tool-change end looking toward machine); lathe direction to be verified.
- Sources: M30 link corrected to type=mcode; added M06 and Haas M-codes manual links.

### 10 Spindle/Feed (K class, ≥2000)
- CSS direction corrected: as diameter shrinks, RPM RISES until G50 cap, then holds; Vc drops below cap. SVG redrawn with real numbers (Vc=180, cap 2500; D50→1146, D25→2292, D20→2500 capped, D10→Vc~78.5).
- Q2 answer: CSS holds surface speed; chip load/feed set separately.
- Code blocks split line-by-line; mill example has full startup G21/G17/G90/G94/G40/G49/G80, G43 at Z50, M08 separate.
- Haas lathe example uses G99 (not G95); labeled as status-setting snippet with assumptions.
- Feed override: 60mm at F300 = 12s, at 50% = 24s; whole cycle not necessarily doubled.
- Threading: fixed RPM follows spindle angle; lead = pitch (single start); multi-start lead = starts × pitch.
- Removed "G97 only for threading"; removed 70%/80%/50%/blue chips/continuous chips/7.5kW universal rules; replaced with catalog-based guidance.
- Feed hold/single block behavior noted as control/cycle dependent.

### 11 Controller Dialects (B class, ≥800)
- CYCLE82 SVG replaced with three-column concept mapping (no fake executable Siemens code).
- Removed "UP 1.0 / CALL LBL" Siemens claim; replaced with "procedure/label call per Siemens manual".
- Corrected: Siemens can use G17/G54/M30; not removed.
- Removed "Haas programs run on FANUC unchanged", "Haas VF and Mazak both FANUC", "020 OVER TRAVEL" alarm.
- Heidenhain described as Klartext conversational text blocks, not touch-probe.
- Removed "one week, one month" filler.
- Sources now reference specific manuals (Haas G-code, G99, Siemens SINUMERIK, Heidenhain TNC).

## Word counts (excluding pre/svg/nav/footer/section)
- 09: ~1400 (B class ≥800)
- 10: 2016 (K class ≥2000)
- 11: ~900 (B class ≥800)

SVGs: 09=2, 10=2, 11=1.

Static source review only; no browser or controller verification.
