# Doubao Done: S01-S05 (12/13)

## S01 (12 line 115)
Replaced "If H01 were missing...G49 state" with explicit conditional fault calculation: compensation explicitly inactive, no auto tool-change reactivation; gauge at W+Zp=-250, tip -370. Stated that omitting H01 alone does not establish this fault.

## S02 (12 lines 87, 155)
- Body: H selects length register; D selects cutter-size register, radius/diameter per control config; check Setting 40.
- Common mistake: replaced "H is length; D is radius" with "Confusing H and D...verify register number and radius/diameter convention".

## S03 (13 touch table)
Z row now: "Tool tip touches part top; gauge-line machine Z reads -180. With L=120: W=-300. Enter W=-300 into G54 Z."

## S04 (12 line 35, 13 lead/concept)
- 12 concept: Zm is machine-coordinate position of gauge reference; machine origin and reference-return identified from machine docs.
- 13 lead: reference-return defined by machine, need not coincide with machine coordinate origin.
- 13 concept: machine coordinate system provides reference; follow machine's referencing procedure; P maps to G54_origin+P in unrotated XY; Z uses tool-length chain.

## S05 (13 rotary section)
- Rotary zero offset: sets angular datum, does not define physical rotary center.
- Dynamic work offset: Haas G254 MRZP example; probing that writes G54 is not itself DWO.
- Sources added G254 link.

Static source review only; no browser/controller verification.
