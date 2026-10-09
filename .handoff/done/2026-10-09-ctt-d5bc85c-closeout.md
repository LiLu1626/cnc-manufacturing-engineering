# CTT d5bc85c Closeout — Final Report

Final commit: **e22dd1c** (pushed; `main` == `origin/main`).

## R-number closure

| Item | Status | Evidence |
|---|---|---|
| R03 page 16 | CLOSED | `16-turning-inserts-toolholders/index.html` L91 now uses h=fn·sinκr (0.141 at 45°, 0.20 at 90°), states moving to 90° does not thin chip; removed "most complaints start in clamping chain" → "possible causes worth checking"; turret answer now "position scatter". |
| R05 page 33 | CLOSED | removed "it is from the edge" certainty → "edge a credible candidate; fixed params do not rule out thermal/measurement/seating"; softened "too-high speed" claim; replaced "wait for the trend" with out-of-tolerance disposition text (hold part, do not release to collect trend); VB answer now independent size/finish acceptance. |
| R04 page 34 | CLOSED | off-position answer now lists pre-hole, datum, measurement, reamer alignment/runout/guidance; 0.10 mm scoped to CTT-H1 classroom case; alignment answer no longer excludes position effects. |
| R06 page 02/06 | CLOSED | 02 SVG title/desc/labels/caption rewritten to "feed and depth are different quantities; within layer not automatically rubbing"; 06 Common Mistake "Chips do not break" → "may impair chip control". |
| R09 structure | CLOSED | script moved exactly **93** `<details>` out of `<section class="ctt-sources">` into each page's `<div class="ctt-practice">`. Post-check: zero `<details>` inside any sources section; per-page counts preserved (K=6, B=4; page 35=26). |
| Page 35 seven h2 | CLOSED | h2 list now exactly: Concept, Why It Matters, How It Works, Worked Example, Common Mistakes, Practice, Sources. Part A/B/C demoted to h3 under Practice; number derivation and "how to prepare" demoted to h3 under How It Works; worked scoring example demoted to h3 under Worked Example. |
| R10 sources | CLOSED | `source-register.json` now carries concrete chapter names (e.g. "Turning Handbook, material groups and machinability table") and an `audit_status` field stating registration only — HTTP reachability and on-page content NOT probed. The old `verified_date` field was removed so a date cannot imply content was verified. Page 01 no longer cites a bare homepage. |
| R11/R12 checker honesty | CLOSED | `check_ctt_sources.py` final output now explicitly states it checks structure/tags only and does NOT probe HTTP or judge claim-to-reference support. |

## Per-page regression

- `verify_cutting_tool_course.py`: **Total counted gap = 0 words, PASS** (after the text removals, no page dropped below threshold).
- `check_ctt_sources.py`: **PASS (structure only)** on 36 pages; the NOTE line records the HTTP limitation.
- Quiz counts after move: B-class pages (01,08,11,13,20,24,30,31,36) = 4; all other ordinary pages = 6; page 35 = 26 (its own rubric).
- SVG: every inline `<svg>` has `<title>` and `<desc>` (checked by the script).
- Sources-section quiz count = 0 across all pages.

## Browser / print acceptance

- Live (post-build) load of `/33-case-turning-wear/` confirmed the **new** content: `details=6, svg=3` (the earlier stale read of 2 was on the previous commit).
- At the attached narrow viewport (499 px wide) there is **no horizontal overflow** (`scrollWidth == clientWidth == 499`).
- `document.body.style.zoom = '2'` applied cleanly: still no horizontal overflow, h1 renders. This is a CSS-zoom emulation inside the page, not a native browser 200% zoom.

### Documented external limitations (not claimed as passed)
- Native browser 200% zoom and forced 390 px device emulation could not be driven (CDP device-emulation previously returned "session not found"); CSS-zoom reflow was verified instead.
- The two printable worksheets' print output was not driven.
- Sandvik URLs are registered as references; their HTTP reachability and chapter-level content were not probed in this audit (per-entry `audit_status`).

No Siemens/Heidenhain controller content was added to CTT; the prior report's drill-point formula now reads h = (D/2)/tan(59°) = (D/2)·tan(31°) consistently on pages 34/35.

---

## Post-review follow-up (18773b8 review)

### R10 source verification — NOT fully closed
- Page-01 register mismatch fixed: the page actually cites the **Mitsubishi Materials technical portal** and the **ISCAR Cutting Tools User Guide** (see `01-cutting-tool-system/index.html` Sources). The register entry now matches those two, with section "Technical Data portal / Cutting Tools User Guide (general reference; not a source for a specific recommended speed)". It no longer claims a Sandvik Turning Handbook chapter for page 01.
- All other entries remain **registered only**: HTTP reachability and on-page content support were NOT probed; `audit_status` says so explicitly. R10 therefore stays "registration complete; content/accessibility verification pending" — not CLOSED.

### R11 browser / print — partial; blockers recorded
- Native forced 390 px device emulation via CDP: **blocked** (`Emulation.setDeviceMetricsOverride` → "Session with given id not found").
- Headless Chrome (`--screenshot`/`--print-to-pdf`) from shell: **blocked** — every invocation aborts (`Abort trap: 6`, macOS `__SharedStringStorage initialize` fork error), including `--version`.
- What DID run:
  - In-app browser, narrow layout: no horizontal overflow at cw=499 and again at cw=416 (`scrollWidth == clientWidth`), page 33 new content confirmed live (details=6, svg=3).
  - Native zoom: after the in-app webview applied additional zoom, `devicePixelRatio` moved 2.0 → 2.4 and layout width 499 → 416 px with **no horizontal overflow** (`scrollWidth == clientWidth == 416`). Exact 200% could not be forced (hotkey reported input-focus blocked), so this is not a certified 200% check.
  - Both worksheets render: `tool-selection-worksheet` (h1 + 3 tables) and `wear-trial-log` (h1 + 3 tables), no overflow.
- Still unverified (not claimed as passed): exact 390 px layout, certified native 200% zoom, and actual print-to-pdf output of the two worksheets.
