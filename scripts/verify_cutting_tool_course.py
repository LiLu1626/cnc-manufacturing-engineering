#!/usr/bin/env python3
"""Static verification for the Cutting Tool Technology course.

Usage: python3 scripts/verify_cutting_tool_course.py

Checks, per article under docs/cutting-tool-technology/:
  * strict English word count (body between <main> and the Sources section,
    excluding <nav>, inline <svg>, the Practice section, and headings)
  * inline SVG count and that every <svg> has a <title>
  * presence of a canonical link
  * presence of the 7 expected <h2> sections (assessment page 35 exempt)

B-class pages must reach 800 words; K-class pages 2000.
This script is a diagnostic counter shipped with the course; it is not the
only acceptance gate. Report any FAIL for human review.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTT = os.path.join(ROOT, "docs", "cutting-tool-technology")

B_CLASS = {"01", "08", "11", "13", "20", "24", "30", "31", "36"}
EXPECTED_H2 = ["Concept", "Why It Matters", "How It Works", "Worked Example",
               "Common Mistakes", "Practice", "Sources"]


def strict_words(html: str) -> int:
    m = re.search(r"<main[^>]*>(.*?)(<section class=\"ctt-sources\">)", html, re.S)
    body = m.group(1) if m else html
    body = re.sub(r"<nav.*?</nav>", " ", body, flags=re.S)
    body = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
    body = re.sub(r"<h2>Practice</h2>.*", " ", body, flags=re.S)
    body = re.sub(r"<h[1-6][^>]*>.*?</h[1-6]>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"&[a-z#0-9]+;", " ", body)
    # keep only tokens that contain at least one ASCII letter
    return sum(1 for w in body.split() if re.search(r"[A-Za-z]", w))


def main() -> int:
    fails = []
    rows = []
    for path in sorted(glob.glob(os.path.join(CTT, "*/index.html"))):
        slug = os.path.basename(os.path.dirname(path))
        num = slug.split("-")[0]
        html = open(path, encoding="utf-8").read()
        words = strict_words(html)
        svgs = len(re.findall(r"<svg", html))
        titled = len(re.findall(r"<svg[^>]*>.*?<title>", html, flags=re.S))
        canon = 'rel="canonical"' in html
        h2 = re.findall(r"<h2>([^<]*)", html)
        need = 800 if num in B_CLASS else 2000
        rows.append((slug, words, need, svgs, titled, canon))
        if words < need:
            fails.append(f"{slug}: words {words} < {need}")
        if titled < svgs:
            fails.append(f"{slug}: {svgs-titled} svg(s) missing <title>")
        if not canon:
            fails.append(f"{slug}: missing canonical")
        if num != "35" and h2 != EXPECTED_H2:
            fails.append(f"{slug}: h2 mismatch -> {h2}")

    print(f"{'page':42} {'words':>6} {'need':>5} {'svg':>3} {'titled':>6} canon")
    for slug, w, need, sv, ti, canon in rows:
        print(f"{slug:42} {w:6d} {need:5d} {sv:3d} {ti:6d} {'Y' if canon else 'N'}")
    print("-" * 70)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print("  -", f)
        return 1
    print("PASS: all checks satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
