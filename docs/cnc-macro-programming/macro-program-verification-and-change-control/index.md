---
title: CNC Macro Program Verification and Change Control
---

# CNC Macro Program Verification and Change Control

A disciplined release framework for CNC macros: technical review, controlled prove-out, documented acceptance, and traceable revision.

[← CNC Macro Programming](../) · [← Platform Home](../../)

> **Scope:** A macro program is executable manufacturing logic. A change to its variables, calculations, motion, offsets, coordinate behavior, or calling interface can affect safety, equipment protection, product conformity, and process capability. Apply the organization’s approved change-control and release requirements.

## Verification Is an Engineering Activity

A macro is not proven simply because it runs without an alarm. It is verified when its inputs, calculations, decisions, toolpath, machine state, recovery behavior, and produced result have been evaluated against the intended engineering requirement.

Verification should progress from low-risk review to controlled machine execution. Do not use an unproved machine movement as the first method for discovering a logic defect.

## Change Classification

Classify each change before it is released:

| Change category | Examples | Typical verification consequence |
| --- | --- | --- |
| Documentation-only | Clarified comments or an unchanged reference note | Technical review and revision traceability |
| Parameter update | Approved dimension, limit, or process-window value | Verify the source, range, and affected paths |
| Logic update | Calculation, comparison, loop, branch, or alarm change | Review normal, boundary, and failure paths |
| Motion update | Coordinate, clearance, feed, cycle, or sequence change | Toolpath review, dry run, and controlled prove-out |
| Interface update | New argument, optional mode, shared variable, or caller behavior | Compatibility review across each approved calling program |
| Environment change | Different control version, machine, fixture, tool assembly, or material condition | Reassess the macro within the changed operating context |

The classification determines the required evidence; it does not replace engineering judgment.

## Required Release Record

Each released macro should have a traceable record containing:

- Program identifier and revision.
- Intended machine, control family, and required options.
- Purpose and approved application boundary.
- Linked drawing, setup sheet, process plan, tool list, fixture reference, and inspection requirement.
- Variable map, macro interface, and controlled parameter list.
- Change description, reason, author, reviewer, and approval status.
- Verification plan, actual evidence, acceptance decision, and release date.
- Recovery guidance and any superseded revision.

## Review Before Execution

Perform a structured review before machine prove-out:

1. Check that the revision matches the approved request and intended part/process context.
2. Review variables, units, coordinate references, and allowable ranges.
3. Trace calculations independently for representative normal, boundary, and invalid inputs.
4. Review every conditional branch, loop exit, alarm path, and default behavior.
5. Confirm macro calls, interfaces, shared data, and intended side effects.
6. Inspect motion logic for work offset, plane, compensation, tool, spindle, coolant, approach, retract, and safe-state requirements.
7. Confirm the return condition leaves the machine and caller in a known state.

Peer review is especially valuable for changed coordinate logic, system-variable access, machine state changes, and recovery behavior.

## Layered Verification

### 1. Static Technical Review

Read the macro as an engineering document. Compare its assumptions and calculations with approved process data; inspect interfaces, variable allocation, unit usage, range checks, and comments. Static review catches many defects before any machine activity.

### 2. Independent Calculation and Test Cases

Create an input-and-expected-output matrix. Include nominal, minimum, maximum, boundary, invalid, and omitted-input cases. For each case record calculated positions, branch outcome, expected message/alarm, and required safe state.

### 3. Simulation or Offline Toolpath Review

Where an approved environment is available, review toolpath geometry, axis travel, reachability, interference risk, transformation state, and sequence. Simulation is evidence—not a substitute for machine-specific prove-out.

### 4. Controlled Machine Prove-Out

Use the organization’s approved procedure: correct revision, verified setup, appropriate supervision, dry run, single block, reduced feed where applicable, and safe clearance strategy. Introduce one new risk at a time. Stop and investigate unexpected behavior; do not continue by assumption.

### 5. Product and Process Confirmation

Confirm the actual feature, dimensions, surface condition, cycle time, tool condition, and repeatability against the acceptance criteria. A macro can follow the intended path and still fail the manufacturing objective.

## Acceptance Criteria

Define acceptance before prove-out. It may include:

- Correct feature location and orientation.
- Conformance to drawing and inspection requirements.
- Valid approach, retract, and return-to-safe-state behavior.
- No interference, unexpected alarms, or unauthorized offset/state changes.
- Correct response to defined invalid conditions.
- Repeatable performance over the approved test condition.
- Complete release record and reviewer approval.

## Controlled Prove-Out and Recovery

An operator must know which revision is active, which inputs were used, what the expected motion is, and how to stop safely. If execution is interrupted, inspect the part, tool, fixture, machine state, offset/transformation state, and last completed step before any restart. Do not restart a macro based only on the last displayed block or a stored counter.

## Revision and Configuration Control

Keep released and development revisions distinguishable. A change should have a unique description, be linked to its supporting evidence, and identify the programs or setup documentation affected by it. When an interface or shared variable changes, review every dependent macro and calling program.

Do not overwrite a known-good release without preserving the ability to identify or recover the prior approved revision. GitHub history helps trace publication history, but it does not replace the organization’s production-control procedure.

## Post-Release Monitoring

Early production use is part of verification. Record unexpected alarms, operator feedback, inspection trends, cycle-time variation, tool-life effects, and recovery incidents. Review whether observed conditions expose a missing assumption, insufficient limit, or documentation gap. Feed verified lessons back into the macro, setup procedure, and knowledge base under controlled revision.

## Release Checklist

- Is the macro revision uniquely identified and linked to the correct application?
- Are the inputs, variables, units, references, and limits documented?
- Have all normal, boundary, and invalid paths been reviewed and tested?
- Has geometry and motion been reviewed independently before machine execution?
- Has a controlled prove-out confirmed safe machine behavior?
- Has product/process output met pre-defined acceptance criteria?
- Are change evidence, approvals, recovery instructions, and affected dependencies recorded?
- Has post-release monitoring been planned for the first approved use?

## Related Topics

- Variables and Data Types
- Expressions and Logical Conditions
- Loops, Counters, and Repeated Features
- Macro Arguments and Subprogram Interfaces
- Coordinate Transformations and Safe Geometry
