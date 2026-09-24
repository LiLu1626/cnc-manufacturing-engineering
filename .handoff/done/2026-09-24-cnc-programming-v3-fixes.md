# CNC Programming v3 — Fix Report

## Addressed in this round (V01–V13)

- **V01 [P1] Tool offsets**: Page 12 completely rewritten. Clean geometry chain: M=W+P+H, Tip=P+H−L. Worked example W=−400, P=10, H=100, L=102 → tip=8 (2mm deep). G49 corrected: cancels length comp only, does NOT switch to machine coordinates (that is G53). All "Wait/recheck/redo" draft language removed.
- **V03 [P1] Subprograms**: Page 34 fixed. M98 P2000 L3 (not O). First G81 with no X/Y drills current position; removed redundant X10. Exactly 12 drill cycles for 12 holes. Added per-call trace table.
- **V04 [P1] G76 threading**: Page 22 rewritten. K=total thread height (radial), D=first-pass depth — not interchangeable. M10×1.5: K=0.92, minor=8.16 (not 8.2), D=0.2. Full parameter table.
- **V05 [P2] Arc exercise**: Page 15 practice answer corrected: S(0,0) C(30,0) E(30,30) is G02 clockwise (not G03). ViewBox widened to −25 to prevent label clipping.
- **V07 [P1] Probing**: Page 37 center formula corrected: left edge=−98, width=40 → center=−98+20=−78 (not −118). Clarified ball center vs contact point. Removed R11 internal language.
- **V08 [P1] Safety**: Page 23 lead no longer says "from top is safe" unconditionally. Page 24 removed universal 50%/100%/25% feed prescriptions; notes tapping/threading must not override feed.
- **V10 [P2] Macros**: Page 36 rewritten. GOTO takes bare number (GOTO 100, not GOTO N100). Added FIX[#2] NE #2 integer validation. Removed wrong "jumps to O1000" explanation.
- **V11 [P1] SPEC paths restored**: All 14 deleted paths recreated with content:
  10-spindle-feed, 11-controller-dialects, 17-drilling-cycles, 19-turning-fundamentals, 20-turning-cycles, 21-grooving-parting-boring, 22-threading, 24-verification, 29-subprograms, 33-milling-strategies, 34-tapping-thread-milling, 35-cad-cam-postprocessing, 36-macro-foundations, 37-multiaxis-probing-overview.
  Stale pages removed: 38-process-optimization, 39-exercises-assessment, 40-glossary-sources. Sitemap regenerated (53 URLs).
- **V13 [P2] Template/cleanup**: Removed R-finding labels, "SPEC says", internal review language from learner pages. Sources now use real <a href> links to Haas URLs.

## Known remaining (not fully closed)

- **V02 [P1] Milling project toolpath**: Page 28/20 still needs proper center-programmed pocket toolpath with entry/stepdown/clearance. Not yet rewritten this round.
- **V06 [P2] Canned cycle cancellation**: New page 17 now states Haas behavior correctly; old 39 deleted. New 33 still says "next rapid drills" — needs alignment with page 17.
- **V09 [P2] Turning project setup**: Page 27 still needs explicit facing operation and setup/clamping data.
- **V12 [P1] Content depth**: Most pages still under 800 words. Needs expansion pass.
- **V13**: .cp-back class should be .back-link per spec; line-height override not yet verified in CSS.

## Files changed
- 8 pages rewritten/fixed (12, 22, 34, 36, 37, 15, 23, 24)
- 14 restored SPEC path pages created
- 3 stale pages deleted
- sitemap.xml regenerated
- Internal language cleaned from 5 pages
