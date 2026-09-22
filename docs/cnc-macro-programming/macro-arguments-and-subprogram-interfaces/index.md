---
title: CNC Macro Arguments and Subprogram Interfaces
---

# CNC Macro Arguments and Subprogram Interfaces

A professional framework for defining how CNC macro programs receive inputs, return control, and remain safe to reuse.

[← CNC Macro Programming](../) · [← Platform Home](../../)

> **Controller dependency:** The calling format, address-to-variable mapping, local-variable behavior, nesting limits, modal effects, and return rules are controller-specific. Confirm the implementation using the applicable control manual and machine-builder documentation.

## Why Interfaces Matter

A reusable macro is a controlled service within a larger program. Its interface defines what a caller must provide, what the macro will do, which conditions it assumes, and how it returns control. Without this contract, a macro call becomes an undocumented dependency that is difficult to review, modify, or recover after an interruption.

A good interface turns a macro from a clever one-time solution into an engineering component with a known purpose and operating boundary.

## Define the Macro Contract

Every reusable macro or subprogram should document these items before release:

| Contract item | Required definition |
| --- | --- |
| Purpose | The machining or inspection function performed |
| Intended environment | Control family, machine type, required options, and process context |
| Required arguments | Name, meaning, unit, reference, valid range, and source |
| Optional arguments | Default behavior and conditions for omission |
| Preconditions | Required tool, offset, plane, work coordinate, modal state, and safe position |
| Outputs and side effects | Motion, offsets, shared-variable changes, messages, counters, or modified modal state |
| Error response | Alarm, message, safe exit, and operator recovery action |
| Revision identity | Program revision and compatible interface version |

## Arguments Are Engineering Inputs

An argument should represent one clearly defined engineering quantity or instruction. Do not overload one input to mean different things in different calls. An input called depth, for example, must specify whether it is an absolute coordinate, an incremental distance, a finished dimension, or a process parameter.

Each argument needs a valid range and a defined response if it is missing or invalid. A macro must not infer safety-critical values from an unknown prior state.

## Required and Optional Inputs

Required inputs are necessary for the macro to perform its intended function. Validate them immediately at macro entry. Optional inputs can improve flexibility, but they should have explicit defaults and should never silently change safety, quality, or coordinate-reference assumptions.

Use optional inputs sparingly. A macro with too many optional behaviors becomes difficult to test because the number of possible operating paths grows rapidly.

## Input Map Example

| Symbolic input | Meaning | Unit / reference | Typical validation |
| --- | --- | --- | --- |
| FEATURE_X | Feature center location | Work coordinate length | Within approved work envelope |
| FEATURE_Y | Feature center location | Work coordinate length | Within approved work envelope |
| CUT_DEPTH | Controlled machining depth | Defined coordinate convention | Compatible with tool and part condition |
| SAFE_Z | Clearance position | Work or machine reference as defined | Clears fixture and clamps |
| FEATURE_MODE | Approved operation selection | Defined code set | Must match documented options |

These symbolic names are documentation names. The actual call syntax and variable mapping must be selected for the specific control.

## Preconditions and Modal Control

A macro must state the machine state it expects on entry. Typical preconditions include unit system, plane, work offset, tool number, compensation state, spindle/coolant condition, safe approach position, and the availability of a required macro option.

Where practical, validate or establish required modal conditions within the macro. Where a condition must remain the caller’s responsibility, make it visible in the call documentation and setup procedure. Hidden modal assumptions are a frequent source of macros that work once and fail later.

## Side Effects Must Be Controlled

A macro can affect more than the intended feature. It may change position, modal state, common variables, offsets, timers, or operator messages. These are side effects and must be documented.

The safest reusable interface minimizes side effects. If the macro changes a condition, decide whether it will restore the prior condition before return, leave a defined new condition, or require the caller to re-establish the state. Do not leave the result ambiguous.

## Nested Calls and Scope

Nested subprogram or macro calls can organize complex work, but they increase dependency and state-management risk. Define which data is local to each level, which data may be shared, and how errors propagate back to the calling level.

Before using nested calls, verify the control’s nesting limits and the behavior of local variables, return paths, and modal state. A subprogram should not unexpectedly overwrite data that belongs to its caller.

## Error Handling and Recovery

A macro interface is incomplete without an error path. When an input or precondition is invalid, the response should identify the issue, prevent unsafe progression, and support a controlled recovery.

Recovery instructions should answer: which parameter or condition requires review, what value or state is expected, whether the tool may be restarted, and whether the part or fixture requires inspection before continuation.

## Verification Strategy

Verify each macro interface independently before integrating it into a larger program:

1. Test every required argument at nominal, minimum, maximum, and invalid values.
2. Test omitted optional arguments and each supported optional mode.
3. Confirm all documented preconditions and side effects.
4. Test error messages, safe exit behavior, and return-to-caller behavior.
5. Test the macro from every approved calling context.
6. Re-verify compatibility when the macro interface or calling program changes.

## Review Checklist

- Does the macro have one clearly defined function?
- Are all inputs named, documented, bounded, and validated?
- Are unit, coordinate reference, and sign conventions explicit?
- Are preconditions and modal assumptions visible?
- Are side effects minimized and documented?
- Is error response safe, understandable, and recoverable?
- Is the interface revision controlled with the calling programs that depend on it?

## Related Topics

- Variables and Data Types
- Expressions and Logical Conditions
- Loops, Counters, and Repeated Features
- Coordinate Transformations and Safe Geometry
- Macro Program Verification and Change Control
