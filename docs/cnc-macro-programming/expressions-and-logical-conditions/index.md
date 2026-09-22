---
title: CNC Macro Expressions and Logical Conditions
---

# CNC Macro Expressions and Logical Conditions

A controller-aware guide to calculations, comparisons, and decision logic in CNC macro programs.

[← CNC Macro Programming](../) · [← Platform Home](../../)

> **Controller dependency:** Operator names, precedence, function availability, comparison syntax, alarm behavior, and branching rules differ by control. Confirm every implementation against the applicable control and machine-builder documentation.

## Purpose

Expressions transform inputs into calculated engineering values. Logical conditions decide whether a program may proceed, select a controlled path, repeat a feature, issue a message, or stop safely. In manufacturing, these are not abstract programming features: they define how the machine responds to actual dimensions, offsets, workholding conditions, and process limits.

A strong macro separates three questions: what value is calculated, what condition is evaluated, and what motion or action is permitted as a result.

## Expression Design

An expression may combine variables, constants, arithmetic operators, geometric functions, and controller functions. Before writing it, state the engineering relationship in plain language and identify the unit and reference for each term.

A calculated feature position, for example, should be traceable to a defined datum, nominal pitch, index number, and approved compensation. If the relationship cannot be explained in words and checked independently, it is not ready to control machine motion.

## Order of Evaluation

Controls apply their own evaluation and precedence rules. Use explicit grouping where the intended calculation could be misread. Grouping is valuable not only for correct execution but also for reviewability.

Avoid long expressions that combine geometry, compensation, conditions, and modal assumptions in one line. Break them into documented intermediate values so each result can be inspected during prove-out.

## Units, References, and Sign Conventions

Every calculation should answer:

- What unit system applies at this point in the program?
- Which datum or coordinate reference does the result use?
- Does positive represent an axis direction, stock condition, diameter/radius convention, or logical state?
- Has the active plane or relevant modal condition been confirmed?
- Is the final value physically plausible for the machine, tool, and fixture?

Unit mismatch and reference mismatch are common sources of macros that calculate correctly but move incorrectly.

## Comparison Conditions

Logical conditions compare values and determine which path is permitted. Typical applications include input-range checks, feature-count validation, clearance protection, process-window evaluation, and controlled recovery logic.

A condition should state a measurable engineering rule. If the calculated clearance is below the approved minimum for the active fixture, for example, the macro should prevent the approach motion and provide a controlled response.

| Condition element | Required definition |
| --- | --- |
| Value | Source, unit, reference, and update point |
| Threshold | Approved limit, tolerance, or controlled parameter |
| Comparison direction | Greater than, less than, within a band, or outside a range |
| Response | Continue, alternate path, alarm, message, or safe exit |
| Recovery | Required check before restart |

## Equality and Tolerance Bands

Decimal calculations may be affected by rounding and control precision. Do not assume exact equality is reliable after several calculations unless the control documentation supports that assumption.

Where appropriate, evaluate whether a value falls within a defined tolerance band rather than relying on one exact comparison. The band must be linked to the protected function: a probing decision may require different limits from a roughing stock calculation.

## Decision Architecture

A maintainable macro uses a visible decision structure:

1. Validate required data and machine context.
2. Calculate intermediate and final engineering values.
3. Check values against approved limits.
4. Select the permitted action path.
5. Provide a visible, recoverable response when a path is rejected.

Do not bury a critical safety or quality condition inside a complex motion statement. Put it in a dedicated decision section where it can be tested independently.

## Fail-Safe Logic

When a condition is uncertain, missing, or outside its approved range, the macro should default to a safe, operator-visible state rather than improvising a motion path. The exact response depends on the control and application, but the intent should be clear: stop unsafe progression, identify the condition, and preserve a recoverable machine state.

Alarm or message text should state the engineering issue and the required check, not merely that a number is wrong. Identify the affected parameter, expected range, and reference document or setup step to review.

## Testing Expressions and Logic

Test calculations and decisions separately before testing motion. Use representative normal, boundary, invalid, and missing-input cases. For each case, record inputs, expected calculated result, expected branch, observed result, and recovery behavior.

Boundary testing is essential: test values just inside and just outside every critical limit. A macro that works only for nominal values has not demonstrated reliable decision behavior.

## Review Checklist

- Is every expression traceable to a drawing, process plan, or defined engineering relationship?
- Are units, coordinate references, and sign conventions explicit?
- Are complex calculations divided into inspectable intermediate results?
- Is each condition linked to an approved limit and defined response?
- Does invalid or uncertain data produce a safe, visible outcome?
- Has the logic been tested at normal, boundary, and failure conditions?
- Are controller-specific assumptions recorded in the release record?

## Related Topics

- Variables and Data Types
- Macro Arguments and Subprogram Interfaces
- Loops, Counters, and Repeated Features
- Coordinate Transformations and Safe Geometry
- Macro Program Verification and Change Control
