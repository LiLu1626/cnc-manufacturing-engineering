---
title: Macro Variables for Beginners
---

# Macro Variables for Beginners

Learn how a macro stores and uses information before you write calculations or motion logic.

[← CNC Macro Programming](../) · [Beginner Introduction](../macro-programming-for-beginners/)

> **Safety note:** Variable numbers, permitted ranges, and persistence rules vary by CNC control and workplace. Do not write to system, offset, or shared variables unless their purpose and consequences are approved and understood.

## The Core Idea

A macro variable is a place where the CNC control stores a number. A program can later read that number, use it in a calculation, compare it with a limit, or pass it to another approved macro.

For a beginner, treat a variable like a labeled container:

| Label | Example value | Possible meaning |
| --- | ---: | --- |
| Hole quantity | 6 | Six holes are required |
| Hole spacing | 25.0 | Holes are 25 mm apart |
| Counter | 3 | The third repetition is running |

The actual variable syntax depends on the control. Learn the concept first, then follow the official manual for your machine’s exact format.

## Why Variables Matter

Without variables, a CNC program is mostly fixed. With variables, a controlled routine can adapt to approved input values. For example, the same hole-pattern routine may be used for 4, 6, or 8 holes—provided its inputs and limits are checked.

Variables make a macro flexible, but flexibility increases the need for clear documentation and verification.

## Three Questions for Every Variable

Before using any variable, answer these questions:

1. **What does it represent?** Write a plain-language description such as “hole spacing in millimetres.”
2. **Where does its value come from?** It may be an argument, an approved parameter, a calculation result, or a counter.
3. **What values are allowed?** State the unit, minimum, maximum, and any special condition such as “must be a whole number.”

If any answer is unclear, the macro is not ready for use.

## Local, Shared, and Persistent Values

Controls use different names for variable ranges, but the underlying idea is common:

- **Local value:** used temporarily inside one macro call. It should not be relied on after the macro finishes.
- **Shared value:** available to more than one program. It requires careful ownership and naming because another program may read or change it.
- **Persistent value:** remains stored after a program ends or the machine is powered down, depending on the control. It must have a defined owner and an approved reset method.

Beginners should start with temporary values in examples approved for their control. Persistent and shared values require stronger change control.

## A Simple Mental Exercise

Suppose a routine needs to drill five holes, starting at X = 10.0 with a 20.0 spacing.

The routine may conceptually store:

- Starting X position = 10.0
- Spacing = 20.0
- Quantity = 5
- Counter = 0

Each repetition uses the counter to calculate the next position. The calculation is only reliable when every value uses the intended units and coordinate reference.

## Common Beginner Mistakes

- Using a variable without knowing whether it already has a value.
- Mixing millimetres and inches.
- Treating a diameter as if it were a radius.
- Reusing one variable for unrelated meanings.
- Forgetting to reset or initialize a counter.
- Changing a shared or persistent variable without knowing who else uses it.
- Assuming a value is safe because the program does not alarm.

## Good Habits From the First Day

- Use a small variable map beside your practice code.
- Give each value one clear purpose.
- State units in comments and documentation.
- Initialize temporary values intentionally.
- Check input ranges before using them in motion.
- Test calculations on paper with a few expected results.
- Keep learning examples separate from released production programs.

## Quick Self-Check

Before continuing, you should be able to explain:

- What value each variable represents.
- Whether it is an input, a result, or a counter.
- What units it uses.
- Which range is allowed.
- Whether it is local, shared, or persistent on your control.

## Next Lesson

[Macro Logic: Making Simple Decisions Safely](../macro-logic-for-beginners/) explains how a macro uses a value to make a safe, understandable yes-or-no decision.
