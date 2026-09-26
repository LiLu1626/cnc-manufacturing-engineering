# Doubao Done: 15/16/17 K-class expansion

Commit: ff86318 (+ follow-up for 16)

## 15 Circular Interpolation (was 782 -> 2018 words, 2 SVGs kept)
Added: plane selection G17/G18/G19, arc feed and surface speed, quarter circles and corner rounds, wrong I/J consequences, R vs I/J preference, arc length/cycle time, lead-in/lead-out on arcs, lathe G18 arcs, verification before cutting, full circles R limitation, inside vs outside arc feed, small-radius feed. Existing G02/G03 math preserved (upper semicircle through (25,+25), lower through (25,-25), 78.540 mm; 90° arc through C(0,20), 31.416 mm).

## 16 Cutter Compensation (was 801/0 SVG -> ~2000 words, 2 SVGs added)
Added: D offset units / Setting 40, wear adjustment through D, lead-in/out geometry, compensation on arcs, forgetting G40, tool changes, limitations, first-article check, inner pocket direction worked example, when not to use compensation, Z vs XY offset separation, lathe nose radius, common overcut failure. Existing G41 direction table for CW outer rectangle preserved (tool center at X=-5/Y=25, X=25/Y=55, X=55/Y=25, X=25/Y=-5). Two new SVGs: outer profile G41 offset diagram, inner pocket G42 diagram, lead-in ramp diagram.

## 17 Drilling Cycles (was 1319 -> 2073 words, 2 SVGs kept)
Added: G84 tapping, G73 vs G83, multiple tools/hole patterns, G98 vs G99 selection, coolant/chip evacuation, through vs blind depth, spot vs center drilling, cycle modal state/G80, drill surface speed formula, verification. Existing R plane SVG and drill-point 0.3D SVG preserved.

Static source review only; no browser/controller verification.
