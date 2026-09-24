# CNC Programming v5 — Fix Report (addressing X01–X03, W06/W07)

## X01 [P1] Subprogram G00 Z50 missing — FIXED (verified in file)
- O2000 code now explicitly has `G00 Z50.` after G80, before Y traversal.
- Comment corrected: G80 cancels cycle mode; tool stays at R plane Z2.
- Practice answer corrected: G80 does NOT raise the tool; explicit G00 also cancels on Haas but doesn't guarantee safe height.
- Arithmetic: redundant X10 = 15 cycles (not 13), updated in both body and practice.
- Verified by reading actual file: G00 Z50 line is present in O2000 code block.

## X02 [P2] Ra formula mislabeled — FIXED
- 38-process-optimization: f²/(8r) now correctly labeled Rmax (peak-to-valley), not Ra.
- Example recalculated: f=0.2, r=0.4 → Rmax=125 µm (not 12.5 µm).
- Added caveat: Ra is roughly Rmax/4 to Rmax/10; actual depends on tool wear, vibration, material.
- Removed contradictory "r=0.8 gives Ra 1.6" claim.

## X03 [P2] G41 exercise answer wrong — FIXED
- 39-exercises-assessment: answer now explains G41 needs an XY lead-in move from outside the part, not just "move to Z50".
- Corrected advice: position outside part at Z50, feed to depth, then G01 G41 lead-in, contour, lead-out with G40.
- Added "always end with G40 before retracting Z".

## W06 [P2] G71 Type I/II consistency — FIXED
- 20-turning-cycles common mistakes: no longer says all X reversal is forbidden; now distinguishes Type I vs Type II.
- Practice answer: Z always monotonic; Type I X monotonic, Type II allows X reversal.
- Removed unsupported "missing depth = single cut" claim.

## W07 [P2] Threading parameter sourcing — FIXED
- 22-lathe-threading: 0.613×pitch now labeled as geometric ideal for sharp 60° V-thread; actual minor depends on tolerance class (6g/6H), tool nose radius, chamfer.
- D0.2 now labeled "teaching starting point for carbide in steel"; real values depend on insert grade, material, coolant, machine rigidity.
- Added "consult tool manufacturer" recommendation.

## Still remaining (honest gaps)
- V02 milling project toolpath (pocket center-programmed, entry, stepdown, cleanup corners)
- V09 turning project facing operation + setup/clamping data
- V12 content depth (most pages under 800 words; K-class needs 2000+)
- V13 template (38/39/40 pages use simple nav not full site-nav-inner; missing canonical/description on some)
- X04 (new pages not integrated into homepage nav; two competing numbering schemes)
