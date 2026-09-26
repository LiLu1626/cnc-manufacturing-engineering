# Doubao Done: 18/19/20 fixes per ca7303c review

## 16
- Removed duplicate second `<h2>Example: Outer CW Profile...` after the code block.

## 18 (A01/A02)
- Modal wording: bare X/Y repeats cycle; explicit G00/G01 also exits but G80 still written.
- First-hole coordinates moved onto the G81 call line; Practice 3 updated to 1 call + 7 more.
- 4-hole block trace table added (cumulative holes, end Z).
- Main example reordered: G43 H01 Z50 → G94 → G00 XY; end split into Z50 / M09 / M05.
- G98 timing rewritten: call G98 on hole 1 so retract already clears before XY move; R-low path requires G80 + re-establish.
- G84 row: synchronous feed in, reverse at bottom, feed out.
- 5th cycle step added; "exact" → "rounded to two decimals".
- Added cycle parameter dialect table, multi-tool reuse, setup checklist.

## 19 (B01/B02)
- G96 direction fixed: n=1000vc/πD; D50→636.6, D25→1273.2, G50 cap.
- Haas lathe G54 work offset vs T geometry/wear; T0102 intentional.
- Z+ away from chuck; removed "toward operator".
- Spindle direction setup-dependent; not derived from front turret.
- Retract code split into X-then-Z blocks; facing retracts +Z first.
- Unified Ø45→Ø41 rough, Ø39.5 finish with classroom assumptions.
- Removed universal X0.5 part-off / X-1 facing advice.
- Nose radius compensation rephrased (corrects contour error, not auto-rounds).
- SVG2 now shows Z0 line, directed feed, chuck-left convention.
- Block trace table added; Sources: G96, lathe G54.

## 20 (C01/C02/C03)
- Type I vs Type II corrected: X-only P = Type I; X+Z = Type II; X increasing allowed; G18.
- Removed "Z in P alarms" / "grooves require G73" generalizations.
- Pass count: 10 mm radial / 2 mm = ~5 passes; D1.0 ≈ 10.
- Cycle time relabeled as straight-cylinder classroom approximation.
- G70 F source: F0.1 on G01 Z0.
- First SVG redrawn as half-section coordinate plot: finished r15/r18, after-rough +0.2 radial, shoulder at -19.9.
- Added step-by-step pass table, U/W sign, first-part wear, alarm reading, rough/finish speeds, program template.
- Sources: G70.

Word counts (Doubao strip method): 18=1921, 19=1919, 20=1808; each 2 SVGs. Static source review only; no controller or runtime verification.
