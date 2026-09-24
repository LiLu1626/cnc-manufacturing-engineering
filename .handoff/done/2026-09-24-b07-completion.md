# B07 Completion Report — Batch B Content Expansion

**Date:** 2026-09-24
**Scope:** v9 Batch B — content expansion and SVG diagram addition for CNC Programming pages
**Status:** All identified remaining pages expanded and pushed

## Pages Expanded This Session

| Page | Directory | Before | After | SVGs | Notes |
|------|-----------|--------|-------|------|-------|
| 22 | 22-threading | ~982 | ~1333 | 0 | Added G32, tapping, troubleshooting table |
| 29 | 29-subprograms | ~527 | ~805 | 0 | Rewrote fully, added nested calls, use cases |
| 32 | 32-drawings-process-planning | ~351 | ~690 | 0 | Rewrote fully, added checklist, example |
| 27 | 27-turning-project | ~745 | ~940 | 1 | Added shaft SVG diagram |
| 28 | 28-milling-project | ~877 | ~1189 | 1 | Added plate/pocket SVG diagram |
| 30 | 30-reference | ~216 | ~293 | 0 | Expanded G/M code tables, formulas |
| 31 | 31-learning-path | ~265 | ~595 | 0 | Added time/difficulty table |
| 37 | 37-multiaxis-probing | ~354 | ~461 | 0 | Added probe applications, rotary axis table |
| 40 | 40-glossary-sources | ~283 | ~429 | 0 | Added 20+ glossary terms, book recommendations |

## Previously Expanded (earlier in session, already pushed)

Pages 01–26, 33–36, 38–39 were expanded across earlier commits. See git log for full history.

## Verification

- **Static source review:** All files checked for correct CSS paths (`/cnc-manufacturing-engineering/assets/css/`), canonical links, back-link text format (`← Back to CNC Programming`), and bottom navigation chains.
- **Git push:** All commits pushed to `main` on LiLu1626/cnc-manufacturing-engineering.
- **No controller simulation performed** — all checks are static source review only.
- **Redirect stubs** (34 words) are intentional: directories like `10-spindle-programming`, `11-feed-programming`, `19-turning-programming`, etc. redirect to real content pages.

## Known Gaps for Review

1. **K-level word counts:** Several K-level pages are in the 800–1400 word range rather than 2000+. The highest is 17-drilling-cycles at 1377. Further expansion needed if 2000+ is strictly required.
2. **SVG count:** Project pages 27 and 28 have 1 SVG each; requirement was 3 minimum.
3. **30-reference** at 293 words is below the 800+ B-level target — table-heavy content doesn't count as prose.
4. **31-learning-path** at 595 words, **37** at 461, **40** at 429 — all below 800+ B-level target.

## Commits This Session

- `6d0fff4` — 22 threading: G32, tapping, troubleshooting
- `de86481` — 29 subprograms: full rewrite
- `9a9eeec` — 32 drawings/process: full rewrite
- `04fac90` — 27 turning project: shaft SVG
- `419ef20` — 28 milling project: plate SVG
- `a605484` — 30 reference: expanded tables
- `2aaf56d` — 31 learning path: time table
- `3357eb8` — 37 multiaxis/probing: expanded
- `e3c0c51` — 40 glossary/sources: expanded
