---
title: Macro Logic for Beginners
---

# Macro Logic for Beginners

Understand how a CNC macro makes a simple decision—and why safe decisions must be explicit before machine motion begins.

[← CNC Macro Programming](../) · [Macro Variables for Beginners](../macro-variables-for-beginners/)

> **Safety note:** The exact syntax for comparisons, branches, messages, and alarms differs by control. This lesson explains the reasoning model, not controller-ready production code.

## What Is Logic in a Macro?

Logic is the part of a macro that asks a question and follows a defined answer.

For example:

> Is the requested hole quantity at least 1?

If yes, the macro may continue to the next approved check. If no, it should stop before any related motion occurs.

This is called a **condition**: a statement that is either true or false.

## The Basic Pattern

Every safe decision has three parts:

1. **Input** — the value being checked.
2. **Rule** — the allowed condition or limit.
3. **Response** — what the macro does when the rule is true or false.

| Example | Input | Rule | Safe response |
| --- | --- | --- | --- |
| Hole quantity | Quantity | Must be 1 or greater | Stop if quantity is zero or negative |
| Hole spacing | Spacing | Must be within the approved range | Stop and request correction if outside the range |
| Feature depth | Depth | Must not exceed an approved limit | Do not begin the cycle if the limit is exceeded |

The important point is that the response is planned—not guessed after an unexpected movement.

## Comparisons in Plain Language

Most macro logic uses familiar comparisons:

| Comparison | Meaning |
| --- | --- |
| Equal to | Is this value exactly the required value? |
| Not equal to | Is this value different from the required value? |
| Greater than | Is this value above the permitted limit? |
| Less than | Is this value below the permitted limit? |
| Greater than or equal to | Has the minimum requirement been met? |
| Less than or equal to | Is the maximum limit respected? |

A control manual shows how these comparisons are written. Before learning syntax, make sure you can state the engineering rule in plain language.

## Validate Before Motion

A beginner-friendly rule is:

> Check information before it is used to create movement.

For a drilling pattern, verify the quantity, spacing, start point, and approved limits before the first position is calculated. Do not discover a bad value after the tool has already entered the work area.

## Use Clear Boundaries

A value near a limit deserves deliberate attention. If spacing is allowed from 10.0 to 50.0 mm, test the reasoning for:

- 10.0 mm — minimum allowed
- 50.0 mm — maximum allowed
- 9.9 mm — just below the allowed range
- 50.1 mm — just above the allowed range

Boundary checks reveal misunderstandings that a “typical” input may hide.

## Decision Paths Must Be Easy to Read

A macro should not make people guess what happens next. Good beginner logic has:

- One clear reason for each check.
- A message or controlled stop when an input is unacceptable.
- A normal path that is easy to trace.
- No hidden changes to offsets, coordinate systems, or machine states.
- A known condition when the macro returns to its caller.

## A Safe Example in Words

Here is a simple decision sequence, written without control-specific syntax:

1. Receive the requested hole quantity.
2. If the quantity is not a whole number, stop and explain why.
3. If the quantity is less than 1, stop and explain why.
4. If the quantity is greater than the approved maximum, stop and explain why.
5. Only after all checks pass, allow the routine to calculate the pattern.

Notice that the macro does not “try it and see.” It either has acceptable information or it stops in a controlled way.

## Common Logic Mistakes

- Checking a value after it has already affected motion.
- Using a vague limit with no units or source.
- Forgetting what happens when a condition is false.
- Allowing a loop or branch to continue without a clear exit.
- Assuming an alarm means the machine is automatically in a safe state.
- Testing only typical values and never testing the boundary.

## Practice Away From the Machine

Choose a simple rule, such as “quantity must be from 1 to 10.” Write down the expected result for 0, 1, 5, 10, and 11. This develops the habit of predicting program behavior before execution.

## Next Steps

Once you can describe variables and simple decisions clearly, move to controlled repetition and calculations. The advanced references explain controller-specific implementation, interfaces, coordinate safety, and verification requirements.
