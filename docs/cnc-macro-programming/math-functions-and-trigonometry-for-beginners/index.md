---
title: CNC Macro Math Functions and Trigonometry for Beginners
---

# CNC Macro Math Functions and Trigonometry for Beginners

A practical beginner reference for the calculations behind patterns, angles, arcs, coordinates, and safe macro decisions.

[← CNC Macro Programming](../) · [Macro Math for Beginners](../macro-math-for-beginners/)

> **Controller boundary:** Function names, bracket rules, angle units, return values, and permitted variable ranges differ among FANUC, Haas, Siemens, Heidenhain, and machine-builder implementations. The examples here use familiar FANUC/Haas-style teaching notation. Treat every line as a learning example—not machine-ready production code—and verify your own control manual before use.

## Why Math Matters in Macro Programming

Macro programming does not require advanced mathematics. It requires a clear connection between a number and a physical feature. A formula can describe hole spacing, a point on a bolt circle, a taper, an angle, or a safe limit.

The most valuable habit is this: calculate first, predict the answer, then decide whether the result makes engineering sense.

## Before Every Calculation: The Four-Part Check

1. **Meaning** — What does each value represent?
2. **Unit** — Is it millimetres, inches, degrees, radians, diameter, or radius?
3. **Reference** — Which work offset, origin, plane, or datum is used?
4. **Limit** — Is the result inside the approved machine, fixture, tooling, and part envelope?

A correct formula with the wrong unit or reference is still a dangerous result.

## Basic Arithmetic Operators

| Operation | Usual meaning | Simple machining use |
| --- | --- | --- |
| + | Addition | Move to the next equally spaced feature |
| - | Subtraction | Find remaining stock or a distance from a datum |
| * | Multiplication | Find total length from count and spacing |
| / | Division | Divide a distance into equal intervals |
| [ ] | Grouping | Make the intended calculation order clear |

Example idea: starting X plus counter times spacing.

    #10 = #1 + [#2 * #3]

Read it before using it: result equals start position plus counter multiplied by spacing.

## Useful Math Functions at a Glance

| Function | Plain-language meaning | Typical beginner use |
| --- | --- | --- |
| ABS[value] | Absolute value; remove the sign | Compare distance regardless of direction |
| SQRT[value] | Square root | Geometry and distance calculation |
| FIX[value] | Round down toward the lower integer | Create a whole-number index, control-specific behavior must be checked |
| FUP[value] | Round up toward the higher integer | Determine required number of passes |
| ROUND[value] | Round to the nearest integer | Convert a value to a nearest whole count |
| SIN[angle] | Sine of an angle | Y offset on a circle, depending on chosen convention |
| COS[angle] | Cosine of an angle | X offset on a circle, depending on chosen convention |
| TAN[angle] | Tangent of an angle | Calculate offset from a known angle and length |
| ATAN[...] | Inverse tangent; derive an angle from a ratio | Determine an angle from X/Y change; syntax varies greatly |

Always check your controller manual for availability and exact behavior, especially for rounding and inverse trigonometry.

## ABS: Distance Without Direction

ABS returns the positive size of a value. For example, a deviation of -0.20 mm and +0.20 mm are both 0.20 mm away from target.

    #20 = ABS[#10 - #11]

Plain English: calculate the difference between actual and target, then ignore whether it is above or below.

Use it for a tolerance comparison only after the target, actual value, unit, and approved limit are understood.

## SQRT: The Diagonal-Distance Tool

The square root function is useful when a calculation produces a squared distance. A classic geometry relationship is:

    distance = SQRT[(delta X * delta X) + (delta Y * delta Y)]

This describes the straight-line distance between two points in a plane. It is a calculation concept, not an instruction to move a machine.

## Rounding Functions: Converting a Value to a Whole Count

Macros frequently need a whole number of holes, passes, or steps. Rounding functions can help, but their behavior must be confirmed on the control.

Imagine 47 mm of length with a maximum allowed step of 10 mm. The minimum pass count is usually five, because four passes would cover only 40 mm. A round-up function may support this reasoning.

Never hide a rounding decision. Document whether the process intends to round down, round up, or select the nearest whole value—and explain why.

## Trigonometry Without Fear

A right triangle has an angle and two sides. Sine, cosine, and tangent describe the relationship between them.

| Function | Relationship | Beginner memory aid |
| --- | --- | --- |
| SIN | opposite / hypotenuse | Gives the vertical-style component in a chosen convention |
| COS | adjacent / hypotenuse | Gives the horizontal-style component in a chosen convention |
| TAN | opposite / adjacent | Converts an angle and a horizontal-style distance into an offset |

You do not need to memorize a diagram immediately. Start by calculating one point, checking it on paper, and drawing what the answer means.

## SIN and COS: Finding a Point on a Circle

A bolt circle is the most familiar macro example. If the center is Xc, Yc and the radius is R, a common coordinate convention is:

    X = Xc + [R * COS[angle]]
    Y = Yc + [R * SIN[angle]]

At an angle of 0 degrees, this convention produces a point to the right of the center: X increases by R and Y does not change. At 90 degrees, Y increases by R and X does not change.

Example: center X100 Y50, radius 25, angle 0 degrees.

| Item | Calculation | Result |
| --- | --- | ---: |
| X | 100 + 25 × COS[0] | 125 |
| Y | 50 + 25 × SIN[0] | 50 |

Now test 90 degrees on paper. You should expect X100 Y75. If your result does not match the sketch, stop and check the angle mode, function convention, and coordinate reference.

## A Four-Hole Bolt Circle: The Thinking Sequence

For four equally spaced holes, use angles 0, 90, 180, and 270 degrees. For each angle:

1. Calculate X and Y on paper.
2. Plot or sketch the point.
3. Check that every point lies 25 units from the center.
4. Check the sequence is clear of clamps, workholding, and travel limits.
5. Only then consider an approved simulation or controlled prove-out procedure.

The macro lesson is not “make the machine move in a circle.” The lesson is “use a stable formula to describe a known pattern.”

## TAN: Turning an Angle Into an Offset

Tangent is often useful for slopes, tapers, and angled features. In a right triangle:

    offset = length * TAN[angle]

Example: if a feature rises by the tangent relationship over a 40 mm horizontal distance, calculate the offset on paper first. Be extremely careful about whether the drawing angle is from the horizontal, from the vertical, or is an included angle. These are different engineering definitions.

## ATAN: Finding an Angle From Two Changes

Inverse tangent works in the opposite direction: it derives an angle from X and Y differences. Controllers vary substantially in their ATAN syntax and in how they determine the correct quadrant. Treat inverse trigonometry as an advanced topic until you can confidently verify signs, quadrants, and angle units on your control.

## Degrees, Radians, and the Most Expensive Assumption

Many CNC macro environments use degrees for trigonometric functions, but do not assume. Software, calculators, and some controls may use radians. Entering 90 when a system expects radians does not mean 90 degrees.

Before testing any angular formula, confirm:

- Whether the function expects degrees or radians.
- Where zero degrees lies in the active coordinate system.
- Which direction is positive rotation.
- Whether a rotation or transformation is already active.

## A Safe Expression-Building Workflow

1. Write the formula in words.
2. Draw a quick sketch of the geometry.
3. Substitute one known input set on paper.
4. Calculate the expected result independently.
5. Test boundary cases: zero, minimum, maximum, and negative values where allowed.
6. Compare the result with the machine envelope and process intent.
7. Only then translate the approved expression into controller syntax.

## Common Newcomer Errors

- Mixing radius and diameter.
- Calculating in millimetres while the active program assumes inches.
- Using an angle from the wrong datum direction.
- Forgetting that trigonometric signs change by quadrant.
- Putting a formula directly into motion without testing the calculated value.
- Assuming a calculator’s angle mode matches the CNC control.
- Rounding a value without documenting why the direction of rounding is safe.

## Practice Set: No Machine Required

1. A circle center is X0 Y0, radius 10. Calculate points at 0, 90, 180, and 270 degrees.
2. A hole pattern starts at X20 with 15 mm spacing. Calculate positions for counters 0 through 4.
3. A result differs from target by -0.35. What does ABS make it?
4. A length is 47 mm and the maximum step is 10 mm. Explain why rounding up produces five passes.
5. Sketch a 30-degree slope over a 40 mm horizontal distance. Which function connects angle, length, and offset?

## What to Learn Next

- [IF Statement for Beginners](../if-statement-for-beginners/) — validate inputs before using a calculation.
- [WHILE Loops for Beginners](../while-loop-for-beginners/) — repeat a pattern with a controlled exit.
- [Coordinate Transformations and Safe Geometry](../coordinate-transformations-and-safe-geometry/) — move from basic formulas to controlled production geometry.
- [Macro Program Verification and Change Control](../macro-program-verification-and-change-control/) — learn how to prove and release a macro responsibly.
