---
title: CNC Macro WHILE Loop for Beginners
---

# CNC Macro WHILE Loop for Beginners

Learn how a macro repeats a task with purpose—without losing control of the loop.

[← CNC Macro Programming](../) · [IF Statement for Beginners](../if-statement-for-beginners/)

> **Important:** Syntax varies by control. This is a Fanuc-style learning model, not production-ready code. Verify behavior away from the machine and use only your approved procedures.

## Why Beginners Like WHILE

A WHILE loop answers a practical question:

> “Keep doing this task while this rule remains true.”

This is ideal for a repeated feature such as a row of holes. Instead of copying the same blocks many times, a macro can repeat an approved sequence and calculate the next position.

## The Mental Model

Every healthy loop needs four things:

1. A **starting value** — usually a counter.
2. A **condition** — the rule that permits another repetition.
3. A **body** — the approved work repeated each time.
4. An **update** — a change that moves the counter toward the exit.

If the counter never changes, the loop may never end. In CNC, an endless loop is not a small error; it can become a serious machine-control problem.

## A Simple Teaching Pattern

    #1 = 1 (START COUNTER)
    WHILE [#1 LE 5] DO1
      (APPROVED REPEATED ACTION GOES HERE)
      #1 = #1 + 1
    END1

Read it in normal language: start at 1; while the counter is 5 or less, perform the task; then add one. After the fifth repetition, the condition is no longer true and the loop ends.

## Visualize It First

For the example above, predict the counter values before writing any motion:

| Pass | Counter at start | Another pass allowed? |
| --- | ---: | --- |
| 1 | 1 | Yes |
| 2 | 2 | Yes |
| 3 | 3 | Yes |
| 4 | 4 | Yes |
| 5 | 5 | Yes |
| 6 | 6 | No — exit |

If you cannot make this table, you are not ready to put the loop into an actual machining sequence.

## The Most Important Rule: Always Know the Exit

Before running a loop, point to the exact line that changes the condition. Ask: “What guarantees that this becomes false?”

Good practice includes a defined maximum quantity, a clearly initialized counter, and input checks before the loop begins.

## Common WHILE Mistakes

- Forgetting to initialize the counter.
- Forgetting to update the counter.
- Using the wrong comparison direction, such as LT instead of LE.
- Allowing a user input to define an unlimited number of repetitions.
- Putting a risky motion inside the loop before proving the loop logic.
- Restarting after an interruption without knowing the actual part, tool, and machine state.

## A Practice Exercise

Plan a loop for three inspection points. Do not write CNC motion. On paper, list the counter values, the expected point number, and the exit point. Then deliberately change the limit to 0 and to 4. Can you predict every result?

## Next Step

[Learn GOTO for Beginners](../goto-for-beginners/) to understand another way programs jump between sections—and why structured loops are usually easier to read and verify.
