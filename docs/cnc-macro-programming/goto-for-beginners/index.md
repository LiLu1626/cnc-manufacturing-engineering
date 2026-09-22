---
title: CNC Macro GOTO for Beginners
---

# CNC Macro GOTO for Beginners

GOTO tells a program to jump to a labeled section. It is useful to understand—and important to use with restraint.

[← CNC Macro Programming](../) · [WHILE Loops for Beginners](../while-loop-for-beginners/)

> **Important:** This article uses a common Fanuc-style teaching format. Control syntax differs. Do not copy this into production code without approved documentation, review, and prove-out.

## What Does GOTO Do?

A program normally reads from top to bottom. GOTO changes that path: “Continue at the section carrying this label.”

A simplified teaching example:

    IF [#1 EQ 0] GOTO 100
    (NORMAL PATH)
    N100 (ALTERNATE OR EXIT PATH)

If the condition is true, the program skips directly to label N100.

## Why Learn It?

GOTO appears in many older programs and in examples you may encounter at work. Understanding it helps you read a macro safely, trace why a sequence was skipped, and recognize when a program might return to an unexpected point.

## The Risk: Hidden Paths

GOTO can make a short program harder to follow because the next executed line may be far away. Several jumps can create paths that are difficult to review—especially when machine state, offsets, or motion are involved.

For a beginner, treat every GOTO as a signpost you must trace carefully.

## A Reading Method That Works

When you see GOTO:

1. Circle the condition that triggers it.
2. Find the destination label.
3. Read every line between the destination and the next normal exit.
4. Write down what machine or program state may be different after the jump.
5. Check whether the program can ever jump backward and repeat unexpectedly.

This turns a confusing jump into a visible route through the program.

## GOTO vs WHILE

| Question | WHILE loop | GOTO |
| --- | --- | --- |
| Main purpose | Repeat an operation while a rule is true | Jump to a named location |
| Easy to understand? | Usually, when structured well | Often less so in longer programs |
| Best beginner use | Controlled repeated patterns | Reading existing code and simple exit paths |
| Main risk | Loop never exits | Hidden, confusing, or unintended paths |

For repeated tasks, a structured WHILE loop is often easier to read, test, and maintain. GOTO still has a place where it makes an approved exit or error path clearer.

## A Good Beginner Rule

Before writing GOTO yourself, become comfortable with IF and WHILE. When reading GOTO, always draw the path on paper. If you cannot explain where the program goes next, do not let it control a machining sequence.

## Mini Challenge

Imagine a macro checks an input. If it is invalid, it jumps to a labeled section that displays a message and ends. Draw two paths: one for valid input and one for invalid input. Which path reaches motion? Which path must leave the machine in a known state?

## Next Lesson

Return to [CNC Macro Programming](../) and continue through the beginner path. When you are ready, the professional references explain how logic, loops, interfaces, and verification are managed in production-quality macros.
