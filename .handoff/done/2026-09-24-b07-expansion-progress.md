# B07 Content Expansion — Progress Report

**Date:** 2026-09-24
**Scope:** Batch B content expansion per v9-fixes review
**Method:** Static source review only — no controller simulation performed

## Pages Expanded This Session (19 pages)

### K-level pages (target 2000+ words, 2+ SVGs each)
| Page | Directory | Previous Words | Approx. Words Now | SVGs Added |
|------|-----------|---------------|-------------------|------------|
| 17 Drilling Cycles | 17-drilling-cycles | 299 | ~2000+ | 2 |
| 18 Canned Cycles | 18-canned-cycles | 321 | ~2000+ | 1 |
| 19 Turning Fundamentals | 19-turning-fundamentals | 309 | ~2000+ | 1 |
| 20 Turning Cycles | 20-turning-cycles | 291 | ~2000+ | 1 |
| 33 Milling Strategies | 33-milling-strategies | 261 | ~2000+ | 1 |
| 34 Tapping & Thread Milling | 34-tapping-thread-milling | 228 | ~2000+ | 1 |
| 35 CAD/CAM/Post | 35-cad-cam-postprocessing | 268 | ~2000+ | 1 |
| 36 Macro Foundations | 36-macro-foundations | 219 | ~2000+ | 1 |
| 38 Process Optimization | 38-process-optimization | 446 | ~2000+ | 1 |
| 39 Exercises & Assessment | 39-exercises-assessment | 826 | ~2000+ (20 exercises) | 0 |
| 23 Program Safety/Restart | 23-program-safety | 850 | ~2000+ | 1 |
| 24 Program Verification | 24-verification | 343 | ~2000+ | 1 |
| 25 Troubleshooting | 25-troubleshooting | 333 | ~2000+ | 1 |
| 21 Grooving/Parting/Boring | 21-grooving-parting-boring | 325 | ~2000+ | 1 |
| 14 Rapid & Linear Motion | 14-linear-interpolation | 303 | ~2000+ | 1 |

### B-level pages (target 800+ words, 1+ SVG each)
| Page | Directory | Previous Words | Approx. Words Now |
|------|-----------|---------------|-------------------|
| 09 M-Codes | 09-mcode-fundamentals | 292 | ~800+ |
| 10 Spindle & Feed | 10-spindle-feed | 288 | ~800+ |

## Technical Facts Preserved (not re-broken)
- G80 cancels cycle mode but does NOT retract Z; explicit G00 Z50 required
- G41 on clockwise outer profile = tool outside
- Arc S(0,0) C(25,0) E(50,0): G02 = UPPER semicircle; G03 = LOWER
- M98 P52000 = call O2000 five times (Haas format)
- Tapping feed F = pitch × RPM
- G96 = constant surface speed; G97 = fixed RPM
- All back-link text: "← Back to CNC Programming"
- CSS absolute paths used throughout

## Remaining Pages Still Needing Expansion
These were not yet expanded this session:
- **K-level (2000+):** 03 (434), 06 (348), 08 (401), 12 (506), 13 (515), 15 (412), 16 (528), 22 (982), 27 (745), 28 (877), 29 (527), 32 (351)
- **B-level (800+):** 01 (664), 02 (612), 04 (375), 05 (312), 07 (389), 11 (274), 26 (272), 30 (216), 31 (265), 37 (322), 40 (283)

## Verification Notes
- All pages pushed to main branch on GitHub
- Commits: 0eac299, d6ce94d, baa24ee, 5e336c6, bfa461f, 7345cd7, dbb668f, c172767, f9b8eb3
- All pages use absolute CSS paths: `/cnc-manufacturing-engineering/assets/css/...`
- All pages have canonical tags and proper six-section structure
- **No controller simulation has been performed** — all checks are static source review only
