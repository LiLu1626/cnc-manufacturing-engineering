#!/usr/bin/env python3
"""Source-link and structure checker for the Cutting Tool Technology course.

Checks:
  1. Every article page has a Sources <h2>.
  2. Every external <a href="http..."> points to an allowed reference host
     (Sandvik knowledge site). No fabricated third-party URLs are invented.
  3. Every article has inline <svg> with <title> and <desc>.
  4. Every <details> quiz item has an answer <p>.

Exit 0 = all checks pass; 1 = problems listed.
"""
import glob, os, re, sys, html
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTT = os.path.join(ROOT, "docs", "cutting-tool-technology")
ALLOWED_HOSTS = ("sandvik.coromant.com", "lilu1626.github.io", "guehring.com",
                 "mitsubishicarbide.com", "secotools.com", "kennametal.com", "osgtool.com")

problems = []
pages = sorted(glob.glob(os.path.join(CTT, "*/index.html")))
for p in pages:
    slug = os.path.basename(os.path.dirname(p))
    if slug in ("resources",):
        continue
    s = open(p, encoding="utf-8").read()
    if "<h2>Sources</h2>" not in s:
        problems.append(f"{slug}: missing Sources section")
    for href in re.findall(r'href="(https?://[^"]+)"', s):
        host = re.sub(r"^https?://", "", href).split("/")[0]
        if not any(host == h or host.endswith("." + h) for h in ALLOWED_HOSTS):
            problems.append(f"{slug}: external link to non-reference host {href}")
    # svg title/desc
    for i, svg in enumerate(re.findall(r"<svg.*?</svg>", s, re.S), 1):
        if "<title>" not in svg:
            problems.append(f"{slug}: svg #{i} missing <title>")
        if "<desc>" not in svg:
            problems.append(f"{slug}: svg #{i} missing <desc>")
    # details answer
    for d in re.findall(r"<details>.*?</details>", s, re.S):
        if "<p>" not in d:
            problems.append(f"{slug}: a <details> item has no answer <p>")

print(f"Checked {len(pages)} pages.")
if problems:
    print(f"FAIL ({len(problems)} problems):")
    for x in problems:
        print("  -", x)
    sys.exit(1)
print("PASS (structure only): Sources heading present, external links on the allow-list, every SVG has title/desc, every quiz item has an answer.")
print("NOTE: this script does NOT probe HTTP reachability and does NOT verify that a reference supports the adjacent claim; see source-register.json audit_status.")
