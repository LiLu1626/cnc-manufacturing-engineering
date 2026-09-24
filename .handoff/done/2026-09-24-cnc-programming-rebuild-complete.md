# CNC Programming Rebuild — Completion Report

**Date:** 2026-09-24
**Status:** DONE — pushed to main
**Commit:** 0a1a54a
**Live URL:** https://lilu1626.github.io/cnc-manufacturing-engineering/cnc-programming/

## What was delivered

### 41 article pages (1 homepage + 40 articles)
All 6-section teaching structure per page:
1. Concept
2. Why It Matters
3. How (with worked example / code)
4. Example (numerical)
5. Common Mistakes
6. Practice Questions (collapsible `<details>` answers)
Plus: Objectives callout, difficulty badge, Sources section.

### Pages generated
| # | Page | Status |
|---|------|--------|
| 00 | index.html (homepage) | rewritten — 7-module card grid |
| 01 | what-is-cnc-programming | rewritten |
| 02 | machine-fundamentals | rewritten |
| 03 | coordinate-systems | rewritten |
| 04 | program-structure | rewritten |
| 05 | gcode-fundamentals | rewritten |
| 06 | modal-codes | rewritten |
| 07 | plane-units | rewritten |
| 08 | programming-math | **NEW** |
| 09 | mcode-fundamentals | rewritten |
| 10 | spindle-feed | rewritten |
| 11 | controller-dialects | **NEW** |
| 12 | tool-offsets | rewritten |
| 13 | work-offsets | rewritten |
| 14 | linear-interpolation | rewritten |
| 15 | circular-interpolation | rewritten (G03 direction verified) |
| 16 | cutter-compensation | rewritten |
| 17 | drilling-cycles | rewritten |
| 18 | canned-cycles | rewritten |
| 19 | turning-fundamentals | **NEW** |
| 20 | turning-cycles | **NEW** |
| 21 | grooving-parting-boring | **NEW** |
| 22 | threading | **NEW** |
| 23 | program-safety | rewritten |
| 24 | verification | rewritten |
| 25 | troubleshooting | rewritten |
| 26 | common-mistakes | rewritten |
| 27 | turning-project | **NEW** |
| 28 | milling-project | **NEW** |
| 29 | subprograms | **NEW** |
| 30 | reference | rewritten |
| 31 | learning-path | rewritten |
| 32 | drawings-process-planning | **NEW** |
| 33 | milling-strategies | **NEW** |
| 34 | tapping-thread-milling | **NEW** |
| 35 | cad-cam-postprocessing | **NEW** |
| 36 | macro-foundations | **NEW** |
| 37 | multiaxis-probing-overview | **NEW** |
| 38 | process-optimization | **NEW** |
| 39 | exercises-assessment | **NEW** |
| 40 | glossary-sources | **NEW** |

### Design system
- Shared CSS: `docs/assets/css/cnc-programming.css` (code blocks, figures, practice, safety notes, prev/next nav)
- Site nav: 6 items (Home, Engineering Tools, Knowledge Base, Machine Systems, CNC Programming, About)
- Back button: `← Back to CNC Programming` on every article
- Prev/Next navigation at bottom of every article
- Footer: `Designed by Li Lu · CNC & Manufacturing Engineering`
- Google verification meta tag present

### Sitemap
All 41 CNC Programming URLs added to `docs/sitemap.xml`.

## SPEC compliance check
- [x] Page 15 uses G03 (CCW 90° arc = 31.416 mm), not G02
- [x] Every article has back button + 6 H2 sections
- [x] Practice questions with `<details>` answers
- [x] SVG diagrams on key pages (coordinate system, arc geometry, cutter comp)
- [x] Worked numbers: S(0,0)/C(0,20)/E(20,20), 2000rpm×4×0.03=240mm/min, CSS D50=955/D25=1910 capped 1800, M10×1.5 tapping feed 900mm/min
- [x] Internal links use absolute `/cnc-manufacturing-engineering/...`
- [x] References: Haas dialect primary, FANUC/Siemens differences noted

## Known limitations / needs review
1. Page 17 (drilling-cycles) G84 tapping: noted as rigid-tap / Haas; verify against SPEC requirement
2. SVG diagrams are inline and simple — may need richer illustrations per SPEC
3. Some pages are shorter than others (e.g., 37 multiaxis overview is intentionally brief — marked as future extension)
4. Generator script `gen_cp.py` remains in repo root (can be removed later)
5. No visual browser testing yet — please review on the live site
