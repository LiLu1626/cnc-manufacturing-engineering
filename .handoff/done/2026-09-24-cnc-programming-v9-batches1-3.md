# v9 Progress Report — Batches 1–3 Complete

## Batch 1A: Exercise page (39-exercises-assessment)
- Entry conditions: verified setup position, clear Z path, tool loaded, G54/H01 confirmed, Setting 40=radius
- G43 line now explicitly G00 G43 H01 Z50
- Diagnosis no longer claims "tool is cutting at depth" (stock boundary undefined)
- Title: "one fully defined replacement example"
- Notes static geometry != controller simulation

## Batch 1B: Threading (22-threading) rewritten
- Merged G76 content from 22-lathe-threading
- H = 0.8660254 P, h3 = 0.6134347 P (Hexagon Infoletter No.37 source cited)
- M10x1.5: H=1.299, h3=0.920, d3=8.160 mm
- 6g/ring gauge external, 6H/plug gauge internal — stated as example choice, follow drawing
- 3 practice problems with full solutions
- Sources section with Haas G76 link

## Batch 2: Milling project (28-milling-project) rewritten
- Fixed data: 100x80x12 faced plate, pocket X30-70/Y25-55, Z-4, R5
- O10 end mill, center-programmed (G40), center boundary X35-65/Y30-50
- Two layers Z-2/Z-4, ramp entry 30mm/1mm drop
- Full 17-point raster listed for BOTH layers (no "repeat above")
- Drill tip h=3/tan59=1.803mm, target Z-14.5, extra breakthrough 0.697
- G98 drilling retract
- Complete program, setup table, corner geometry explanation, coverage math
- 3 practice problems

## Batch 3: Turning project (27-turning-project) rewritten
- Fixed data: O40x100 bar, jaw front Z-55, grip 44mm, projection 55mm
- Two facing passes (0.5mm each) from Z+1 to Z0
- Haas single-line G71: P10 Q20 D1.0 U0.4 W0.1 F0.20
- G70 finish at S1200 F0.10
- r0.4 nose radius explained at shoulder root
- X100/Z100 retract, toolholder envelope 8mm -> 7mm gap
- Complete program, setup table, 3 practice problems

## Remaining
- Batch 4: homepage nav, 15 compat pages, sitemap, CSS
- Batch 5: expand 40 pages to 800-2400 words
- Batch 6: final verification report
