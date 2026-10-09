#!/usr/bin/env python3
"""Strict word counter for the Cutting Tool Technology course.

Teaching interval: from <h2>Concept</h2> up to (but not including) <h2>Practice</h2>.
This deliberately EXCLUDES: breadcrumb/back links, eyebrow, lead, Level/Covers,
learning objectives, all headings, navigation, inline SVG text, <pre>/<code>
formulas, and the Practice/answer and Sources sections.

B-class pages must reach 800 counted words; K-class 2000. Page 35 uses its own
assessment rubric and is excluded from the ordinary interval rule.

Calibration (5 tokenise checks) is printed at the end so a reviewer can confirm
what is being counted:
  1) "n = 1000 vc / (pi D)"          -> 0 words (formula-only line stripped)
  2) "The edge wears."               -> 3 words
  3) "&mdash;" entity                 -> 0 words
  4) "vf = n.zc.fz"                  -> 0 words
  5) heading "<h2>Concept</h2>"       -> 0 words
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTT = os.path.join(ROOT, "docs", "cutting-tool-technology")
B_CLASS = {"01", "08", "11", "13", "20", "24", "30", "31", "36"}


def teaching_interval(html: str) -> str:
    m = re.search(r"<h2>Concept</h2>(.*?)<h2>Practice</h2>", html, re.S)
    return m.group(1) if m else ""


def count_words(text: str) -> int:
    text = re.sub(r"<svg.*?</svg>", " ", text, flags=re.S)
    text = re.sub(r"<pre.*?</pre>", " ", text, flags=re.S)
    text = re.sub(r"<code.*?</code>", " ", text, flags=re.S)
    text = re.sub(r"<h[1-6][^>]*>.*?</h[1-6]>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-z#0-9]+;", " ", text)
    out = []
    for w in text.split():
        w = w.strip(".,;:()[]{}\"'")
        if not w:
            continue
        if "=" in w:            # formula remnant
            continue
        if not re.search(r"[A-Za-z]", w):  # pure numbers / punctuation
            continue
        out.append(w)
    return len(out)


def calibrate():
    samples = [
        ("<code>n = 1000 vc / (pi D)</code>", 0),
        ("<p>The edge wears.</p>", 3),
        ("&mdash;", 0),
        ("<code>vf = n.zc.fz</code>", 0),
        ("<h2>Concept</h2>", 0),
    ]
    ok = True
    print("Calibration (input -> got, expected):")
    for s, exp in samples:
        got = count_words(s)
        flag = "OK" if got == exp else "MISMATCH"
        if got != exp:
            ok = False
        print(f"  {flag:9} {s!r:32} -> {got} (exp {exp})")
    return ok


def main():
    fails = []
    rows = []
    for path in sorted(glob.glob(os.path.join(CTT, "*/index.html"))):
        slug = os.path.basename(os.path.dirname(path))
        num = slug.split("-")[0]
        if num == "35":
            continue
        html = open(path, encoding="utf-8").read()
        words = count_words(teaching_interval(html))
        need = 800 if num in B_CLASS else 2000
        rows.append((slug, words, need))
        if words < need:
            fails.append((slug, words, need))

    print(f"{'page':42} {'words':>6} {'need':>5} {'gap':>5}")
    total_gap = 0
    for slug, w, need in rows:
        gap = max(0, need - w)
        total_gap += gap
        print(f"{slug:42} {w:6d} {need:5d} {gap:5d}")
    print("-" * 60)
    print(f"Total counted gap across short pages: {total_gap} words")
    print()
    if not calibrate():
        print("CALIBRATION FAILED")
        return 1
    if fails:
        print(f"FAIL ({len(fails)} pages short):")
        for slug, w, need in fails:
            print(f"  - {slug}: {w} < {need}")
        return 1
    print("PASS: all ordinary pages meet the teaching-interval word threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
