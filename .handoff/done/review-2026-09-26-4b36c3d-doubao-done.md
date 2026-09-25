# Doubao Done: V01–V04

Commit: 4b36c3d

## V01 CSS SVG
- x-axis moved to y=160 (=0 RPM baseline); y-axis bottom also y=160.
- Cap dashed line moved from y=60 to y=50 (=2500 RPM, same mapping as path).
- Circles at crossover (236) and D10 (320) moved from y=60 to y=50.
- In-chart D25/D10/cap text labels removed; values now only in the data table.
- Axis ticks: y=0 at (46,163), y=2500 at (46,53); x ticks D50/D25/D10.
- Table row: ≈22.918 crossover, unconstrained RPM ≈2502 (not 2500).

## V02 11 FANUC=G95
- Table cell now: "FANUC: verify the selected G-code system; Haas lathe: G99".
- FANUC/Haas paragraph: removed "instead of G95"; now states feed-per-rev G-code depends on configured G-code system and must be checked; do not infer G95/G99 from brand name.

## V03 Sources
- 10 Sources: added Sandvik Coromant Formulas and Definitions for Milling PDF link, noting it supports the net-power formula and units; kc=2700 and η=0.8 explicitly labeled classroom assumptions.
- 11 Sources: Siemens and Heidenhain links relabeled as documentation portals / manual search entries, with explicit note that exact version and section are not yet cited line-by-line (honest status, not claimed as verified chapter citations).

## V04 Entry conditions
- 09 example assumptions now also state the selected tool is manufacturer-confirmed to plunge axially at the programmed feed.
- 10 mill snippet prefixed with the same entry assumptions (post-tool-change Z move allowed, H01/G54 calibrated, Z50 clears fixture on XY, Z5 clears work face) and references the confirmed center-plunging tool.
- 11 entry conditions rewritten: after startup block, valid G43 H tool length offset re-established; spindle running in drilling direction/speed; coolant available; clearances verified.

## Word counts
- 09: 1430 (B ≥800)
- 10: 2228 (K ≥2000)
- 11: 934 (B ≥800)

Static source review only; no browser or controller verification.
