# CNC Programming v6 — Fix Report (Y01–Y04)

## Y01 [P2] Rmax arithmetic 10x too large — FIXED
- 38-process-optimization: corrected Rmax = 0.2²/(8×0.4) = 0.04/3.2 = 0.0125 mm = 12.5 µm (not 125).
- Removed unsupported "Ra = Rmax/4 to Rmax/10" claim.
- Added back-calculation example: for Rmax=1.6 µm, f = √(8×0.4×0.0016) = 0.072 mm/rev.
- Showed all calculation steps.

## Y02 [P2] Thread profile explanation wrong — FIXED
- 22-lathe-threading: corrected that 0.613×pitch is NOT the sharp V height.
- Sharp 60° triangle H = (√3/2)×P ≈ 0.866P = 1.30 mm for P=1.5.
- The 0.613P is the truncated basic external thread profile per ISO 68-1.
- Noted it differs for internal threads and other forms (UN, trapezoidal).
- D0.2 now labeled "teaching assumption" not "for carbide in steel".

## Y03 [P2] G98/G99 not declared — FIXED
- 34-subprograms: startup block now explicitly includes G99.
- Added explanation: G99 retracts to R plane between same-row holes (efficient); G98 would retract to Z50 after every hole (for tall fixtures).
- Subprogram explicitly raises to Z50 before Y row advance.

## Y04 [P2] G41 answer incomplete — FIXED
- 39-exercises-assessment: now gives complete corrected program with assumptions (10mm end mill, D05=5mm radius, 50×50 part).
- Full lead-in from (-10,-10) to (0,0) = 14.1mm diagonal, then contour, then lead-out to (-10,-10) with G40.
- Code reading trace now states "assuming machine starts at safe Z" premise.

## Still remaining (honest gaps)
- V02 milling project pocket toolpath
- V09 turning project facing + setup data
- V12 content depth (most pages under 800 words)
- X04 new pages not integrated into homepage; template inconsistency
