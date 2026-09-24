# CNC Programming v4 — Fix Report (addressing W01–W08)

## W01 [P1] sitemap double-prefix + lost sections — FIXED
- Regenerated sitemap by scanning all `docs/` subdirectories for index.html.
- Result: 158 URLs, all correct single-prefix paths.
- Verified: 0 URLs contain `cnc-programming/cnc-programming`.
- All other sections (engineering-tools, knowledge-base, machine-systems, about) included.

## W02 [P1] Subprogram G80 retract semantics — FIXED
- Subprogram code now explicitly adds `G00 Z50.` after `G80` before Y traversal.
- Comment corrected: G80 cancels cycle mode; tool remains at R plane Z2 until explicit Z retract.
- Practice corrected: explicit G00 also cancels cycle on Haas; the risk is low Z during traversal, not drilling.
- Arithmetic corrected: extra X10 line = 15 cycles (not 13) for 12 unique points.

## W03 [P2] Arc practice answer still G03 — FIXED
- Directly edited `15-circular-interpolation/index.html` line 52.
- Answer now: CW 90° (G02): G02 X30 Y30 I30 J0.
- Added vector explanation: start relative to center (-30,0) at 180°, end (0,30) at 90° → clockwise.
- Verified by reading the actual file bytes (UTF-8 chars, not HTML entities).

## W04 [P1] Probing offset conversion — FIXED
- Added explicit explanation: #5061 records position in current work coordinates, not machine coordinates.
- Worked example: old G54 X = -300, measured center = -78 → machine center = -378 → new G54 X = -378.
- Warns that entering -78 directly is wrong unless old G54 X = 0.
- G31 does not automatically write G54 (already correct, preserved).

## W05 [P1] Missing SPEC paths 38/39/40 — FIXED
- Restored 38-process-optimization/ with new content (cycle time, tool wear table, surface finish, chatter).
- Restored 39-exercises-assessment/ with knowledge check, code reading, find-the-error, write-the-program.
- Restored 40-glossary-sources/ with glossary terms and real Haas source links.
- Fixed broken link in 19-turning-fundamentals: `/machine-systems/horizontal-cnc-lathes/` → `/machine-systems/03-horizontal-lathes/lathe-fundamentals/`.

## W06 [P2] G71 Type I vs Type II — FIXED
- 20-turning-cycles now distinguishes:
  - Type I: both X and Z must be monotonic.
  - Type II (Haas/FANUC option): Z monotonic, X may reverse for simple recesses.
- Removed unsupported claim that missing depth = single pass.

## W07 [P2] Threading parameter sourcing — PARTIALLY ADDRESSED
- K/D and 8.16 arithmetic already correct from v3.
- Remaining: "D0.2 typical for steel" needs source caveat; 0.613×pitch needs tolerance note. Not yet expanded this round.

## W08 [P1/P2] Remaining gaps
- V02 milling project toolpath: not yet redesigned.
- V09 turning project facing/setup: not yet expanded.
- V12 content depth: most pages still under 800 words. Needs full expansion pass.
- V13 template: .cp-back → .back-link, line-height, bare markdown links — partially cleaned.

## Verification
- Sitemap: 158 URLs, 0 double-prefix, all sections present.
- Direct file reads confirmed W02/W03/W04/W06 edits are in the HTML (not just claimed).
- All restored pages use the correct nav, back-link, and CSS includes.
