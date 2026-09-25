# Doubao Done: U01–U06 fixes

Commit: 38e5bb3

## U01 Program order
- 09: example now `G54 G90` → `G00 G43 H01 Z50.` → `S1500 M03` → `G00 X0. Y0.` → `M08` → `G00 Z5.`. Assumptions listed (Z50 clears fixture, H01/G54 calibrated, Z5 clears work face, tool can plunge).
- 10: mill snippet same order (G43 H01 Z50 before X0 Y0), S2000 M03.
- 11: drilling snippet now starts `G90 G54 G00 Z50.` before `G00 X10. Y10.`; entry conditions explicitly stated; G98 returns to the cycle initial plane, not an implicit Z50.

## U02 09 ending contradictions
- Removed "Forgetting M09 leaves coolant running at shutdown"; replaced with statement that Haas M30 ends spindle/coolant and explicit M09/M05 documents order.
- Direction wording now uses Haas "forward/reverse" (M03 forward / M04 reverse); removed "tool-change end looking toward machine" and "inserts expect M03".
- Coolant end sequence unified: retract to verified clearance first, then M09/M05/M30; no universal Z5 claim.

## U03 10 power calculation
- Replaced erroneous `28.8 × 4.5 = 1296 W` with specific-cutting-force model:
  - MRR = 28.8 cm³/min.
  - kc = 2700 N/mm² (classroom assumption).
  - Pc = ae·ap·vf·kc/(60×10⁶) = 1.296 kW.
  - η = 0.8 → input ≈ 1.62 kW.
  - Compare against actual machine power curve at 2500 RPM, not nameplate.
  - Doubling ap doubles Pc to ≈2.592 kW; still needs curve check.
- Added Sandvik milling formulas PDF link to Sources.

## U04 10 CSS SVG
- Redrawn to exact mapping: x=60…320 for D=50…10, x=60+(50−D)×6.5; y=160−RPM×0.044.
- Sampled D = 50,45,40,35,30,25,22.9,20,15,10.
- Cap line at y=60 (2500 RPM); cap point starts at D≈22.9 (x=236).
- Data labels inside plot short; full values moved to a 5-row table (D, unconstrained RPM, actual RPM, actual Vc).
- "G50 cap" label anchored end at right boundary; no overflow.

## U05 10 threading / plunge / feed advice
- Threading: phase sync is done by the cycle and spindle position feedback; G97 is used per cycle requirement. Removed "fixed RPM starts at same spindle angle" claim.
- G76/G92 no longer grouped as "defines all passes"; now "specific cycle, consult its manual".
- Plunge: example uses a manufacturer-confirmed center-plunging tool; removed "standard end mill can plunge".
- Wear advice: now identifies wear mode first, checks material/tool/catalog; only adjusts feed if confirmed too light and permitted.
- Table: G95 labeled "ISO/FANUC lathe where configured"; G99 explicitly Haas lathe; text says do not treat them as interchangeable.

## U06 11 sources
- Added actual Siemens SINUMERIK support portal link and Heidenhain TNC 640/iTNC 530 online manual link.
- Added Haas G98/G99 retract explainer link.
- Softened "G17/G18/G19 universal" to: geometric plane concept transfers; specific plane G-codes and cycle syntax must be checked.

## Word counts (excluding pre/svg/nav/footer/section)
- 09: 1415 (B ≥800)
- 10: 2180 (K ≥2000)
- 11: 889 (B ≥800)

SVGs: 09=2, 10=2 (CSS chart + startup/coolant), 11=1.

Static source review only; no browser or controller verification.
