---
title: CNC Macro Math for Beginners
---

# CNC Macro Math for Beginners

Macros become useful when numbers can describe a family of features. Learn the small amount of mathematics that unlocks patterns, spacing, and safe checks.

[← CNC Macro Programming](../) · [Macro Variables for Beginners](../macro-variables-for-beginners/)

> **Control note:** Arithmetic functions and formatting vary by control. Work from your machine’s official documentation; do calculations on paper or in an approved simulator before they can influence machine motion.

## You Already Know the Most Important Math

Most beginner macros begin with four operations:

| Operation | Meaning | Machining example |
| --- | --- | --- |
| + | Add | Move from one hole to the next spacing |
| - | Subtract | Find remaining stock or distance |
| * | Multiply | Find total pattern length |
| / | Divide | Split a distance into equal sections |

The difficult part is not the arithmetic. It is knowing what each value means, its unit, and its coordinate reference.

## One Pattern, One Formula

Imagine five holes, 20 mm apart, starting at X10. The idea is:

    current position = start position + (counter × spacing)

Write down the result before any programming:

| Hole | Calculation | X position |
| --- | --- | ---: |
| 1 | 10 + (0 × 20) | 10 |
| 2 | 10 + (1 × 20) | 30 |
| 3 | 10 + (2 × 20) | 50 |

If the table surprises you, stop there and check the zero point, unit, and counter definition. This habit catches more mistakes than clever code does.

## Brackets Make Intent Visible

In macro expressions, brackets help show which operation should happen first. They are not decoration. Use them to make the calculation readable to the next person—and to your future self.

Compare the plain-language ideas:

- start + (counter × spacing)
- (start + counter) × spacing

They are different calculations. Brackets make the intended relationship clear.

## The Three Checks Before Any Calculation Drives Motion

1. Are all values using the same unit system?
2. Is the result expressed in the correct coordinate reference?
3. Is the calculated result inside the approved machine and fixture envelope?

## Mini Challenge

A row begins at X5, with 12 mm spacing. On paper, calculate positions for counters 0, 1, 2, and 3. Then change the spacing to 15 mm. You are learning parametric thinking: change one input, predict every result.

## Common Beginner Mistakes

- Mixing diameter and radius values.
- Mixing inches and millimetres.
- Forgetting whether the first counter is 0 or 1.
- Using a calculation result without checking its range.
- Copying an expression without understanding its coordinate reference.

## Next Step

Once you can predict a calculation, combine it with [IF](../if-statement-for-beginners/) for input checks and [WHILE](../while-loop-for-beginners/) for controlled repetition.
