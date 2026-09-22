---
title: CNC Macro Loops, Counters, and Repeated Features
---

# CNC Macro Loops, Counters, and Repeated Features

A disciplined approach to repeated-feature machining with controlled iteration, geometry generation, limits, and verification.

[← CNC Macro Programming](../) · [← Platform Home](../../)

> **Controller dependency:** Loop syntax, branching behavior, maximum nesting, available functions, and alarm handling vary by control and machine builder. Treat this page as an engineering framework, then implement and verify against the applicable documentation.

## Why Use a Macro Loop

Repeated holes, pockets, slots, bolt-circle positions, patterned faces, and multi-station operations are common in CNC work. A macro loop can reduce duplicated code and make the relationship between feature count, spacing, and geometry explicit.

The benefit is not fewer lines alone. The benefit is one controlled method that can be reviewed, tested, and reused when the part family changes within an approved range.

## The Loop Contract

Before writing loop logic, define its contract:

| Element | Required definition |
| --- | --- |
| Feature purpose | What identical or patterned feature is being machined? |
| Count | How many features are required, and what is the permitted range? |
| Start condition | What datum, index, or first position establishes the pattern? |
| Increment | How does each subsequent position change? |
| End condition | What specifically ends the loop? |
| Safe state | What must be true before and after every iteration? |
| Recovery | How is the current index identified after a controlled interruption? |

A loop without an explicit end condition or a bounded count is not ready for a machine tool.

## Counter Design

A counter represents the current iteration. It should be initialized deliberately at macro entry and updated at one clearly identifiable point in each cycle. Use a local counter where possible so that another program cannot alter the loop state.

The counter should have a defined meaning: it may represent the completed feature number, the next feature number, or a zero-based internal index. Do not mix these conventions. Document which one applies and how it maps to drawing feature identification.

## Geometry Generation

Repeated-feature geometry should be calculated from an approved reference, not accumulated blindly from prior machine position. A robust design identifies the datum, nominal location, pitch or angular increment, index, and any approved compensation.

For linear patterns, verify the direction and sign of the increment. For circular patterns, verify center reference, radius, angular convention, plane, and index-to-angle relationship. For nonuniform patterns, use a documented data table or controlled lookup method rather than assuming equal spacing.

## Pre-Loop Validation

Validate all inputs before the first feature is machined:

1. Confirm the required count is present, integral where required, and within the approved maximum.
2. Confirm start geometry, pitch or angular increment, and clearances are plausible for the drawing and fixture.
3. Confirm active units, plane, work offset, tool, and required modal conditions.
4. Confirm the toolpath envelope remains within machine travel and clear of clamps, jaws, and protected zones.
5. Define the response if any validation condition fails.

Do not wait until the loop is in motion to discover that a count, pitch, or reference is invalid.

## Per-Iteration Safety

Each iteration should follow a repeatable structure:

1. Calculate the current feature location from the approved reference and counter.
2. Check the calculated location against any required limit or protected zone.
3. Move through an approved approach and clearance sequence.
4. Execute the feature operation using the controlled cycle or subroutine.
5. Retract to a defined safe position.
6. Update the counter and evaluate the end condition.

Separating these steps makes the macro easier to inspect in single block and easier to diagnose after an interruption.

## Avoiding Infinite and Runaway Loops

An infinite loop can create repeated unexpected motion, wasted time, tool damage, or collision risk. Prevent it with independent safeguards:

- Validate the requested count against an approved upper limit.
- Update the counter exactly once per completed iteration.
- Test the end condition using the documented counter convention.
- Avoid modifying the counter from more than one hidden location.
- Add a secondary exit or controlled alarm if the iteration exceeds the expected maximum.

The upper limit should be a real engineering limit, not an arbitrarily large number.

## Interruptions and Recovery

A repeated-feature macro should be designed for the reality of production interruptions. Determine whether the operation can safely restart at the beginning, whether it needs a verified current-feature index, and what inspection is required before resuming.

Never assume a stored counter alone proves that a feature was completed correctly. A recovery decision may also require checking spindle state, tool condition, position, work offset, fixture security, and the last completed operation.

## Verification Strategy

Verify the loop in layers:

1. Review the count, start geometry, increment, and generated positions without machine motion where possible.
2. Test normal, minimum, maximum, and invalid counts.
3. Test the first, middle, and final feature positions independently.
4. Dry run and single-block the initial prove-out with safe clearances.
5. Confirm actual positions and feature results through approved inspection.
6. Test the controlled response to an invalid input and an interrupted cycle.

For a pattern, checking only the first feature is insufficient. The last feature often reveals errors in count, index convention, cumulative logic, or coordinate reference.

## Review Checklist

- Is the feature count bounded, validated, and traceable to an approved source?
- Is the counter convention documented and initialized at entry?
- Are positions calculated from a stable datum and controlled geometry relationship?
- Is every iteration protected by a repeatable approach, operation, and retract sequence?
- Are machine travel, fixture clearance, and protected zones checked?
- Does the loop have a visible, reliable end condition and secondary protection against runaway iteration?
- Is recovery after interruption defined and verified?

## Related Topics

- Variables and Data Types
- Expressions and Logical Conditions
- Macro Arguments and Subprogram Interfaces
- Coordinate Transformations and Safe Geometry
- Macro Program Verification and Change Control
