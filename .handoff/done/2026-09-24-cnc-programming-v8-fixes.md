# CNC Programming v8 — Fix Report (A01–A03)

## A01 [P2] Entry state assumptions — FIXED
- Added: tool already loaded, G54/H01 verified, Z50 above all fixturing, Setting 40 = radius mode.
- No longer implies safe Z movement from arbitrary initial position.

## A02 [P2] Thread tolerance as universal rule — FIXED
- 6g now stated as "in this example we assume", not as universal external thread class.
- Added "always follow the tolerance class on your drawing".
- 8.16 mm now described as "theoretical minor diameter estimate used as X endpoint in this G76 example", not "starting diameter".
- Ring gauge confirms functional acceptance, not every drawing dimension.

## A03 [P3] Answer references imaginary closed square — FIXED
- Rewrote diagnosis to match the ACTUAL buggy program (X0Y0→X50→X80Y30):
  1. G41 mid-cut at Z-5
  2. No G40 at end
  3. No startup block
  4. Path is not a defined part geometry
- Removed the "counter-clockwise closed square" narrative that didn't match the problem.
- Corrected outer-profile program kept as a proper-worked example, clearly labeled.

## Still remaining
- V02/V09 projects, V12 depth, X04 integration, source citations for 0.613
