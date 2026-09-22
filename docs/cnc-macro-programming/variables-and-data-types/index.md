---
title: CNC Macro Variables and Data Types
---

# CNC Macro Variables and Data Types

A controller-aware reference to variable-based CNC macro programming, focused on data lifetime, intent, validation, and safe reuse.

[← CNC Macro Programming](../) · [← Platform Home](../../)

> **Controller dependency:** Variable ranges, persistence, system-variable access, precision, syntax, and option availability differ by control model and machine-builder implementation. Use the applicable control manual as the authority.

## Why Variables Matter

A conventional CNC program describes a fixed sequence for a fixed part condition. A macro program introduces data into that sequence: dimensions, offsets, counters, status flags, feature counts, probing results, and decision thresholds. It can make a proven program structure reusable across controlled variations, but it also creates failure modes when data is assigned, retained, or interpreted incorrectly.

The engineering objective is to make program inputs, calculations, decision logic, and outputs understandable and verifiable during setup, production, recovery, and future revision.

## Variable Categories by Lifetime

### Local Variables

Local variables exist only while a macro or subprogram call is active. Use them for temporary calculations, local loop indexes, calculated coordinates, and call-specific parameters. Keeping internal working values local reduces unintended interaction with other programs.

### Common or Shared Variables

Common variables can be accessed by more than one program or macro. Some controls clear them at reset or power-off while others retain them. Define ownership: which program may write a value, which programs may read it, what value means not initialized, and when it must be reset.

### Persistent Variables

Persistent variables retain values across reset or power cycles when supported. They may hold durable, controlled information such as an approved calibration reference, a managed setup parameter, or a completed-part counter. Persistence is not validation: confirm the value remains correct for the active part, revision, machine, and setup before use.

### System Variables

System variables expose control state, offsets, positions, timers, modal conditions, and other machine information. Some are read-only; others can change offsets or operating state. Treat write access as an engineering change: confirm the variable definition, units, reset behavior, access restrictions, machine-builder logic, and recovery method before prove-out.

## Data Is More Than a Number

Most macro environments represent values numerically; the programmer supplies the meaning. Define these attributes for every important value:

| Attribute | Question to answer |
| --- | --- |
| Meaning | Is it a finished diameter, clearance, tool-life count, or status flag? |
| Unit | Is it in the active unit system or a fixed unit convention? |
| Reference | Is it machine, work, tool, or local geometry referenced? |
| Sign convention | What does positive and negative mean physically? |
| Valid range | What values are process-wise and physically acceptable? |
| Lifetime | Is it local, shared, persistent, or read from the control? |
| Owner | Which controlled procedure may change it? |

A calculation can be mathematically valid and still command an unsafe or incorrect result if these attributes are undefined.

## Naming and Documentation

Variable numbers are constrained by the control, but their purpose should never be anonymous. Maintain a variable map in the program header, setup documentation, or an approved reference sheet.

| Symbolic name | Purpose | Expected convention | Verification |
| --- | --- | --- | --- |
| FEATURE_COUNT | Number of repeated features | Integer, greater than zero | Compare with drawing or setup sheet |
| PITCH_DISTANCE | Increment between feature centers | Positive length | Verify datum direction and drawing value |
| SAFE_CLEARANCE | Retract clearance | Positive length | Check clamps, jaws, and machine limits |
| CURRENT_INDEX | Internal loop position | Local integer | Reset at macro entry |
| STATUS_FLAG | Macro state | Defined code set | Record meanings in the header |

These symbolic names are documentation names, not universal CNC syntax. Map them to the correct controller variables only after review.

## Initialization and Validity Checks

Every input needs a known source and state before use. A safe macro normally performs these checks near entry:

1. Confirm required inputs have been supplied or initialized.
2. Verify each value’s range, sign, and expected type.
3. Confirm the required modal state, work offset, tool, and plane.
4. Reject impossible combinations before any calculated motion.
5. Use a controlled alarm, message, or safe exit when a condition is not met.

A zero feature count, negative retract clearance, or pitch directed into a fixture should never be silently accepted merely because it is numerically valid.

## Precision, Rounding, and Comparison

Macro calculations often use decimal values. Control precision, rounding behavior, and comparison rules determine whether two apparently equal values are considered equal. Avoid depending on exact equality after multiple calculations unless the control documentation supports it. Where appropriate, compare within a defined engineering tolerance band and keep unit and rounding conventions consistent.

## Indirect Addressing and Bounds Checking

Some macro systems support indexed or indirect variable selection. This handles repeated feature data efficiently but requires bounds checking. Verify the index is an integer within documented limits, and prevent indexed storage from overlapping another macro’s allocation. An out-of-range index can select wrong geometry, wrong offsets, or unintended motion.

## Engineering Rules for Reusable Macros

- Prefer local variables for internal calculations.
- Allocate shared and persistent values through a documented, non-overlapping map.
- Set a defined state at macro entry; do not depend on temporary data from an earlier program.
- Validate units, ranges, signs, and control state before calculated motion.
- Keep calculation, decision, and motion sections separate.
- Record the intended control family, required macro options, and program revision.
- Provide an operator-visible response for invalid input; never allow an unsafe default.

## Verification and Release

Verify the macro first through approved simulation or offline review where available, then dry run, single block, reduced feed, and controlled prove-out using safe geometry and approved tooling and workholding. The release record should identify the program revision, machine/control, macro option status, input values, expected and actual results, reviewer, and recovery procedure.

Re-verify when variables, calculations, control software, machine configuration, or intended use changes.

## Related Topics

- Expressions and Logical Conditions
- Macro Arguments and Subprogram Interfaces
- Loops, Counters, and Repeated Features
- Coordinate Transformations and Safe Geometry
- Probing Data and Offset Management
- Macro Program Verification and Change Control
