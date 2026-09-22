---
title: CNC Macro IF Statement for Beginners
---

# CNC Macro IF Statement for Beginners

The first instruction that makes a macro feel intelligent: **IF** lets your program check a value before it continues.

[← CNC Macro Programming](../) · [Beginner Learning Path](../macro-programming-for-beginners/)

> **Important:** Macro syntax differs by control. The examples below use a familiar Fanuc-style teaching format. Check your own control manual and follow approved training before using any macro on a machine.

## Why IF Is So Powerful

An IF statement asks one clear question: “Is this condition true?” If yes, the program performs the defined action. If no, it moves on or follows another approved path.

That single idea lets a macro protect itself from bad inputs, choose an option, or stop before an unsafe calculation becomes motion.

## The Shape of an IF Statement

A beginner-friendly pattern is: IF [condition] THEN action.

Read it aloud: **IF** this rule is true, **THEN** do this action.

For example, imagine that #1 holds the number of holes requested:

    IF [#1 LT 1] THEN #3000 = 1 (HOLE QUANTITY MUST BE 1 OR MORE)

In plain English: if the requested quantity is less than one, stop and show a useful message.

The purpose is not to memorize the line. The purpose is to understand the protective thinking behind it.

## Comparison Words You Will See

Many Fanuc-style macro examples use these abbreviations:

| Word | Meaning | Everyday question |
| --- | --- | --- |
| EQ | Equal to | Is it exactly this value? |
| NE | Not equal to | Is it different? |
| GT | Greater than | Is it above the limit? |
| GE | Greater than or equal to | Has it reached the minimum? |
| LT | Less than | Is it below the limit? |
| LE | Less than or equal to | Is it within the maximum? |

Always translate the line into normal language before trusting it.

## One Useful Example: Checking a Range

Suppose an approved routine accepts a quantity from 1 to 10:

    IF [#1 LT 1] THEN #3000 = 1 (QUANTITY TOO SMALL)
    IF [#1 GT 10] THEN #3000 = 2 (QUANTITY TOO LARGE)

This makes the expected range visible and stops before the value can create an unintended pattern.

## Think Before You Write

For every IF statement, write these three sentences first:

1. What value am I checking? Example: hole quantity.
2. What is the approved rule? Example: it must be from 1 to 10.
3. What should happen if the rule fails? Example: stop with a clear message before motion.

If you cannot answer all three, do not write the line yet.

## A Mini Challenge

Without writing CNC code, decide what should happen for this rule: a drilling depth must be greater than 0 and no deeper than the approved maximum. Test 0, 5, the maximum, and one value beyond it on paper. What message should appear in each failed case?

That is real macro-programming practice: predicting behavior before execution.

## Common IF Mistakes

- Checking the value after it has already affected motion.
- Using a limit with no unit, source, or engineering reason.
- Writing a condition that is correct mathematically but wrong for the intended coordinate system.
- Showing an unclear alarm message such as ERROR.
- Testing only one normal value instead of the boundary values too.

## Where to Go Next

After IF, learn [WHILE Loops for Beginners](../while-loop-for-beginners/) to repeat a task in a controlled way. Then read [GOTO for Beginners](../goto-for-beginners/) to understand a powerful—but easy-to-misuse—branching instruction.
