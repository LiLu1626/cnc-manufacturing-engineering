#!/usr/bin/env python3
"""Generate all CNC Programming article pages."""
import os, re

BASE = "/Users/lilu/Doubao/chats/2026-09-23/new-chat/cnc-manufacturing-engineering/docs/cnc-programming"
S = "/cnc-manufacturing-engineering"

NAV = f'''<nav class="site-nav"><div class="site-nav-inner">
<div class="site-nav-brand">Li Lu <span>&middot;</span> CNC Eng</div>
<ul class="site-nav-links">
<li><a href="{S}/">Home</a></li>
<li><a href="{S}/engineering-tools/">Engineering Tools</a></li>
<li><a href="{S}/knowledge-base/">Knowledge Base</a></li>
<li><a href="{S}/machine-systems/">Machine Systems</a></li>
<li><a href="{S}/cnc-programming/" aria-current="page">CNC Programming</a></li>
<li><a href="{S}/about/">About</a></li>
</ul></div></nav>'''
FOOT = '<footer class="site-footer">Designed by Li Lu · CNC &amp; Manufacturing Engineering</footer>'

def pg(sub, title, desc, body, prev=None, nxt=None):
    """sub = path relative to cnc-programming/ e.g. '03-coordinate-systems'"""
    folder = os.path.join(BASE, sub)
    os.makedirs(folder, exist_ok=True)
    cp = f"https://lilu1626.github.io{S}/cnc-programming/{sub}/"
    nb = ""
    if prev or nxt:
        p = f'<a href="{S}/cnc-programming/{prev[0]}/">&larr; {prev[1]}</a>' if prev else "<span></span>"
        n = f'<a href="{S}/cnc-programming/{nxt[0]}/">{nxt[1]} &rarr;</a>' if nxt else "<span></span>"
        nb = f'<div class="cp-nav-bottom">{p}{n}</div>'
    h = f'''<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — CNC &amp; Manufacturing Engineering</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{cp}">
<link rel="stylesheet" href="{S}/assets/css/site.css">
<link rel="stylesheet" href="{S}/assets/css/article.css">
<link rel="stylesheet" href="{S}/assets/css/cnc-programming.css">
</head><body>
{NAV}
<main class="cp-article">
<a class="back-link" href="{S}/cnc-programming/">&larr; Back to CNC Programming</a>
{body}
{nb}
</main>{FOOT}</body></html>'''
    with open(os.path.join(folder, 'index.html'), 'w') as f:
        f.write(h)
    print(f"  {sub}")

def m(level, machine):
    return f'<div class="cp-meta"><span><strong>Level:</strong> {level}</span><span><strong>Machine:</strong> {machine}</span></div>'
def obj(items):
    return f'<div class="cp-objectives"><strong>What you will learn:</strong><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
def prac(qs):
    out = '<div class="cp-practice"><h3>Practice</h3>'
    for i,(q,a) in enumerate(qs,1):
        out += f'<p><strong>{i}.</strong> {q}</p><details><summary>Show answer</summary><p>{a}</p></details>'
    return out + '</div>'
def src(items):
    return f'<h2>Sources and Applicability</h2><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>'
def code(block):
    return f'<pre class="cp-code"><code>{block}</code></pre>'

# SVG fragments
SVG_AXES = '''<svg viewBox="0 0 300 220" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="190" x2="280" y2="190" stroke="#17242f" stroke-width="1.5" marker-end="url(#ax)"/>
<line x1="50" y1="210" x2="50" y2="20" stroke="#17242f" stroke-width="1.5" marker-end="url(#ay)"/>
<defs><marker id="ax" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#17242f"/></marker>
<marker id="ay" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#17242f"/></marker></defs>
<text x="275" y="205" font-size="13" fill="#17242f">X+</text><text x="35" y="25" font-size="13" fill="#17242f">Y+</text>
<circle cx="150" cy="100" r="4" fill="#0b766e"/><text x="160" y="95" font-size="12" fill="#07574f">Work zero</text>
<circle cx="220" cy="140" r="4" fill="#e07a3f"/><text x="225" y="155" font-size="11" fill="#e07a3f">P(40,30)</text>
</svg>'''

SVG_ARC = '''<svg viewBox="0 0 260 220" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="180" x2="240" y2="180" stroke="#17242f"/><line x1="40" y1="200" x2="40" y2="20" stroke="#17242f"/>
<text x="230" y="195" font-size="11">X</text><text x="25" y="25" font-size="11">Y</text>
<circle cx="40" cy="100" r="80" fill="none" stroke="#cfdbd8" stroke-dasharray="3"/>
<path d="M 40 180 A 80 80 0 0 1 120 100" fill="none" stroke="#0b766e" stroke-width="2.5"/>
<circle cx="40" cy="180" r="4" fill="#0b766e"/><text x="10" y="195" font-size="11" fill="#0b766e">S(0,0)</text>
<circle cx="120" cy="100" r="4" fill="#e07a3f"/><text x="125" y="95" font-size="11" fill="#e07a3f">E(20,20)</text>
<circle cx="40" cy="100" r="3" fill="#17242f"/><text x="5" y="95" font-size="11" fill="#17242f">C(0,20)</text>
<text x="60" y="160" font-size="10" fill="#0b766e">G03 90&deg;</text></svg>'''

SVG_COMP = '''<svg viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg">
<rect x="60" y="40" width="120" height="120" fill="none" stroke="#17242f" stroke-width="2"/>
<circle cx="120" cy="100" r="30" fill="none" stroke="#0b766e" stroke-width="2" stroke-dasharray="5"/>
<circle cx="120" cy="100" r="3" fill="#0b766e"/>
<text x="190" y="60" font-size="11" fill="#17242f">Part contour</text>
<text x="190" y="80" font-size="11" fill="#0b766e">Tool center path</text>
<line x1="60" y1="40" x2="120" y2="100" stroke="#cfdbd8" stroke-dasharray="3"/>
<text x="70" y="125" font-size="10" fill="#5c6872">tool radius offset</text></svg>'''

SVG_FLOW = '''<svg viewBox="0 0 300 140" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="f" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L5,3 L0,6 Z" fill="#0b766e"/></marker></defs>'''
steps = ["Drawing","Plan","Setup","Code","Verify","Part"]
for i,s in enumerate(steps):
    x = 5+i*49
    SVG_FLOW += f'<rect x="{x}" y="80" width="46" height="28" rx="4" fill="#e6f4f2" stroke="#0b766e"/>'
    SVG_FLOW += f'<text x="{x+23}" y="97" font-size="8" text-anchor="middle" fill="#07574f">{s}</text>'
    if i<5: SVG_FLOW += f'<line x1="{x+46}" y1="94" x2="{x+49}" y2="94" stroke="#0b766e" marker-end="url(#f)"/>'
SVG_FLOW += '</svg>'

print("Generating...")

# 01
pg('01-getting-started/what-is-cnc-programming', "What Is CNC Programming?",
   "Understand what CNC programming is, how a drawing becomes machined part coordinates, and the difference between manual and CAM.",
   f'''<h1>What Is CNC Programming?</h1>
<p class="cp-lead">CNC programming is the bridge between an engineering drawing and a moving machine tool.</p>
{m("Beginner","Mill & Lathe concept")}
{obj(["What a CNC program controls","The drawing-to-part workflow","Manual vs CAM programming","Why coordinates matter first"])}
<figure class="cp-figure">{SVG_FLOW}<figcaption>From drawing to part. Schematic.</figcaption></figure>
<h2>Concept</h2>
<p>A CNC program is a text file of instructions telling the machine where to move, how fast to spin, and how fast to feed. The controller reads each line and commands the servos. It does not think — it executes. The NC file is not the same as a CAM project file: the CAM file holds the model and toolpaths; the exported G-code is what the machine runs.</p>
<h2>Why It Matters</h2>
<p>A 60&times;40 mm plate with holes at (10,10) and (50,30). On a manual mill you crank dials. In CNC you write coordinates — and the machine repeats them exactly. If coordinates are wrong, every hole is wrong, consistently. That is why coordinates come before code.</p>
<h2>How: The Workflow</h2>
<ol><li><strong>Drawing</strong> — dimensions, tolerances, material.</li>
<li><strong>Process plan</strong> — rough/finish, tools, setup.</li>
<li><strong>Workholding</strong> — vise, chuck, fixtures.</li>
<li><strong>Program</strong> — coordinates, speeds, feeds, cycles.</li>
<li><strong>Verify</strong> — backplot, dry run, single block.</li>
<li><strong>First part</strong> — inspect, adjust offsets.</li></ol>
<p><strong>Manual programming</strong> suits simple geometry: straight turns, rectangular pockets, hole patterns. <strong>CAM</strong> suits 3D surfaces, molds, complex parts. Even with CAM you must read the output to catch post errors.</p>
<h2>Example</h2>
{code('G00 X10. Y10.        <span class="cp-comment">(over hole A)</span>\nG81 Z-15. R5. F100. <span class="cp-comment">(drill)</span>\nG00 X50. Y30.       <span class="cp-comment">(hole B, cycle stays)</span>\nG80')}
<p>X50 Y30 is a destination (G90 absolute), not a distance. S2000 is RPM, not surface speed. F200 is mm/min under G94.</p>
<h2>Common Mistakes</h2>
<ul><li>Treating coordinates as distances (G90 vs G91).</li><li>Confusing RPM with cutting speed.</li><li>Assuming CAM output needs no review — wrong posts and unmodeled fixtures crash machines.</li></ul>
{prac([
("Holes A(10,10) and B(50,30). Delta X and Y?", "ΔX = 40, ΔY = 20. Diagonal = √(1600+400) = √2000 ≈ 44.7 mm."),
("Stepped shaft vs turbine blade — hand code or CAM?", "Stepped shaft: hand code. Turbine blade: CAM for 3D surfaces."),
("Why verify CAM output?", "Post-processors output wrong G-codes per machine; CAM simulation omits vise/fixture. Review actual NC code.")])}
{src(["Haas Mill Operator's Manual — G-Codes, haascnc.com.","Sandvik Coromant, Milling Formulas.","Teaching values; not cutting recommendations."])}''',
   nxt=("02-machine-fundamentals","Machine Fundamentals"))

# 02
pg('02-machine-fundamentals', "Machine Fundamentals for Programmers",
   "Learn axes, spindle, tool changer, and coordinate basics every CNC programmer must know.",
   f'''<h1>Machine Fundamentals for Programmers</h1>
<p class="cp-lead">You do not need to be a machinist, but you must know which way axes point and what the spindle spins.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Identify X/Y/Z on mill and lathe","Machine home vs work zero","Why X means diameter on a lathe","Tool changer vs turret"])}
<h2>Concept</h2>
<p>A vertical machining center spins the tool; the table moves X/Y and the spindle moves Z. A CNC lathe spins the workpiece in a chuck; a turret holds tools moving in X (radial) and Z (along the part). The <strong>machine home</strong> is a fixed physical reference found on startup. The <strong>work zero</strong> (G54) is where you tell the controller your drawing origin sits.</p>
<figure class="cp-figure">{SVG_AXES}<figcaption>Work coordinate system. Schematic, not to scale.</figcaption></figure>
<h2>Why It Matters</h2>
<p>X30 means different things: on a mill it is a table position. On a lathe in diameter mode it means a 30 mm diameter — 15 mm from center. Mixing these crashes tools or cuts wrong diameters.</p>
<h2>How</h2>
<p><strong>Mill (G17 XY):</strong> X = table left-right, Y = front-back, Z = spindle up-down. Tool spins; workpiece does not.</p>
<p><strong>Lathe (G18 XZ):</strong> Z = along spindle (away from chuck is negative), X = radial. In <strong>diameter programming</strong>, X values are the full diameter, not radius. Workpiece spins; tool does not.</p>
<p>Mills use a <strong>tool magazine + ATC</strong>; lathes use a <strong>turret</strong> indexing stations.</p>
<h2>Example</h2>
<p>Lathe bar Ø40. Command X30. Tool tip moves to 30 mm diameter = 15 mm from center. Radial depth = (40−30)/2 = 5 mm, not 10.</p>
<h2>Common Mistakes</h2>
<ul><li>Confusing machine home with part zero.</li><li>Treating lathe X as radius.</li><li>Ignoring that tool holder, turret, chuck bodies can collide even if tip path looks clear.</li></ul>
{prac([
("Lathe: X moves 50→46. Radial depth?", "Diameter drops 4 mm; radial depth = 2 mm."),
("Why does a safe-looking tip path still crash?", "Coordinates define the tip point only. Holder, turret, vise occupy physical space. Know the machine envelope.")])}
{src(["Haas Mill and Lathe Operator's Manuals.","Axis direction and stroke vary by builder — verify on your machine."])}''',
   prev=("01-getting-started/what-is-cnc-programming","What Is CNC Programming"),
   nxt=("03-coordinate-systems","Coordinate Systems"))

# 03 Coordinate Systems
pg('03-coordinate-systems', "CNC Coordinate Systems",
   "Master machine vs work coordinates, G54-G59 work offsets, and absolute vs incremental programming.",
   f'''<h1>CNC Coordinate Systems</h1>
<p class="cp-lead">The single most important chapter. Coordinates are the language of CNC; get this wrong and nothing else matters.</p>
{m("Key","Mill & Lathe")}
{obj(["Machine coordinate system and home position","Work coordinate system and G54–G59","Absolute (G90) vs incremental (G91)","How offsets chain: machine + work + tool = actual position"])}
<h2>Concept</h2>
<p>There are three nested coordinate systems. The <strong>machine coordinate system</strong> is fixed to the machine — its origin is the machine home. The <strong>work coordinate system</strong> (WCS) is where you place your part origin via a G54–G59 offset. The <strong>program</strong> uses WCS coordinates; it never sees machine coordinates.</p>
<p>The chain is: <em>machine position + work offset + tool offset = actual tool–workpiece relationship.</em> The controller does this math every block. You only program in work coordinates.</p>
<h2>Why It Matters</h2>
<p>If your G54 X/Y is off by 2 mm, every feature programs to the wrong place by 2 mm — but the program itself is "correct." This is why setup verification matters more than code review. Absolute vs incremental errors are the #1 beginner crash cause.</p>
<h2>How</h2>
<p><strong>G90 (absolute):</strong> every X/Y/Z word is a destination in work coordinates. <strong>G91 (incremental):</strong> every word is a distance moved from the current position.</p>
<p>Start at X0 Y0. To reach (50,20):</p>
<ul><li>Absolute: <code>G90 G01 X50. Y20. F200</code> — go to the point (50,20).</li>
<li>Incremental: <code>G91 G01 X50. Y20. F200</code> — move 50 in X and 20 in Y from wherever you are.</li></ul>
<p>If you were at (100,50), G91 X50 Y20 lands at (150,70) — not (50,20). That is the difference.</p>
<figure class="cp-figure">{SVG_AXES}<figcaption>Work coordinates: X right, Y up, origin at your chosen part zero.</figcaption></figure>
<p><strong>G54–G59</strong> are six stored work offsets. Use G54 for setup 1, G55 for setup 2, etc. — useful when machining multiple parts on a tombstone or running two setups on one program.</p>
<h2>Example</h2>
<p>Programmed point X100 Y50. G54 work offset is X0.000 Y0.000. Machine axis target = machine_home + G54 + (100,50). If you measured the edge wrong and G54 should be X0.5, the part is off by 0.5 mm in X — consistently on every feature.</p>
<p>Compare: G90 G01 X30 F150 (go to X=30) vs G91 G01 X30 F150 (move 30 mm away). Same numbers, completely different motion.</p>
<h2>Common Mistakes</h2>
<ul><li>Switching G90/G91 mid-program and forgetting — subsequent moves accumulate wrong.</li>
<li>Using G54 for every setup even when a second offset would avoid re-fixturing.</li>
<li>Assuming work zero is always on the part corner — choose it by datum, not by convenience.</li>
<li>Mixing G90 and G91 in the same block without understanding the state.</li></ul>
{prac([
("In G90 at X20 Y10, you command G91 X30 Y10. Where is the tool now?", "X50 Y20 (20+30, 10+10). Incremental adds to current position."),
("You want the tool to go from (20,20) to (60,45). Write it in G91.", "G91 G01 X40. Y25. (60−20=40, 45−20=25)."),
("Why is G54 called an offset, not a zero?", "It shifts the work origin relative to machine home. The machine never moves the part; it just adds a stored number to every programmed coordinate.")])}
{src(["Haas Mill Operator's Manual — Work Offsets, G54–G59.","HEIDENHAIN and Siemens manuals use equivalent datum plane / zero offset concepts.","Always confirm offset behavior on your controller."])}''',
   prev=("02-machine-fundamentals","Machine Fundamentals"),
   nxt=("04-program-structure","Program Structure"))

# 04 Program Structure
pg('04-program-structure', "CNC Program Structure",
   "Anatomy of a real CNC program: program number, blocks, addresses, start and end, line by line.",
   f'''<h1>CNC Program Structure</h1>
<p class="cp-lead">Before you write G00, understand what each part of a program is for.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Program number and file boundaries","Blocks, sequence numbers, words","Addresses: N/G/X/Y/Z/S/T/H/F/M","Startup and end blocks"])}
<h2>Concept</h2>
<p>A program is a text file. Lines are called <strong>blocks</strong>. Each block contains <strong>words</strong> like <code>G01</code>, <code>X50.</code>, <code>F200.</code>. A word = letter (address) + number. Blocks are separated by newlines. The controller executes them in order unless a jump or loop redirects it.</p>
<h2>Why It Matters</h2>
<p>Reading a program is like reading a sentence: you parse words left to right. Knowing that <code>N10</code> is just a label, <code>G01</code> is the action, and <code>X100.</code> is the target lets you read any program quickly.</p>
<h2>How</h2>
{code('%             <span class="cp-comment">(file start, often required on FANUC)</span>\nO1001         <span class="cp-comment">(program number)</span>\nG21 G17 G90 G40 G49 G80  <span class="cp-comment">(known state)</span>\nT01 M06       <span class="cp-comment">(call tool 1, change)</span>\nG54 G00 X0 Y0 <span class="cp-comment">(work offset, position)</span>\nS2000 M03     <span class="cp-comment)">spindle on, CW</span>\nG43 H01 Z50.  <span class="cp-comment">(tool length offset)</span>\nM08           <span class="cp-comment">(coolant on)</span>\n...\nM09           <span class="cp-comment">(coolant off)</span>\nM05           <span class="cp-comment">(spindle stop)</span>\nG91 G28 Z0    <span class="cp-comment">(Z to home)</span>\nM30           <span class="cp-comment">(end, reset to start)</span>\n%')}
<p>Breakdown of <code>N10 G01 X100.0 Y50.0 F300.</code>:</p>
<ul><li><code>N10</code> — sequence number (label, does not execute).</li>
<li><code>G01</code> — linear interpolation mode.</li>
<li><code>X100.0</code> — X destination.</li>
<li><code>Y50.0</code> — Y destination.</li>
<li><code>F300.</code> — feed rate 300 mm/min.</li></ul>
<h2>Example</h2>
<p><code>O1001</code> names the program. <code>T01 M06</code> selects and changes to tool 1. <code>G54</code> activates work offset 1. <code>S2000 M03</code> starts spindle clockwise at 2000 RPM. <code>G43 H01</code> applies tool length offset #1. <code>M30</code> ends and rewinds.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting <code>%</code> start/end on FANUC-controlled machines.</li><li>Using duplicate O-numbers in memory.</li><li>Missing M30 — program runs off the end.</li><li>Putting comments in ways the controller does not accept (use parentheses).</li></ul>
{prac([
("What does O1001 do?", "It names/identifies the program. It does not move anything."),
("Which word sets feed rate?", "The F word (e.g. F200). It is modal."),
("Why G43 H01 before cutting?", "It applies the stored tool length offset so the Z position reflects the actual tool length, not just the machine's Z zero.")])}
{src(["Haas Mill Operator's Manual — Program Structure.","FANUC Series Manual — program number and block format."])}''',
   prev=("03-coordinate-systems","Coordinate Systems"),
   nxt=("05-gcode-fundamentals","G-Code Fundamentals"))

# 05 G-Code Fundamentals
pg('05-gcode-fundamentals', "G-Code Fundamentals",
   "G-codes grouped by function: motion, setup, cycles, compensation — not just a lookup table.",
   f'''<h1>G-Code Fundamentals</h1>
<p class="cp-lead">G-codes are not random magic letters. They are grouped by function, and understanding the groups prevents confusion.</p>
{m("Beginner","Mill & Lathe")}
{obj(["How G-codes are organized into modal groups","The four motion codes you must know","Setup, offset, and cycle group codes","Why group membership matters"])}
<h2>Concept</h2>
<p>G-codes are <strong>preparatory functions</strong> — they prepare the controller for a type of motion. They fall into <strong>modal groups</strong>: only one code in a group can be active at a time. Choosing a new one cancels the old. The most important group is <strong>motion</strong>: G00, G01, G02, G03.</p>
<h2>Why It Matters</h2>
<p>If you understand groups, you know that writing G81 then G83 automatically cancels G81 (same cycle group). But writing G43 does not cancel G01 (different groups). This is how you avoid "why is my machine doing X?" surprises.</p>
<h2>How</h2>
<div class="cp-table-wrap"><table>
<tr><th>Group</th><th>Codes</th><th>What they do</th></tr>
<tr><td>Motion</td><td>G00, G01, G02, G03</td><td>Rapid, linear, CW arc, CCW arc</td></tr>
<tr><td>Plane</td><td>G17, G18, G19</td><td>XY / XZ / YZ plane for arcs</td></tr>
<tr><td>Units</td><td>G20, G21</td><td>Inch / mm</td></tr>
<tr><td>Offset</td><td>G54–G59</td><td>Work coordinate systems</td></tr>
<tr><td>Cycle</td><td>G80, G81, G82, G83, G84, G85</td><td>Cancel / drilling / boring cycles</td></tr>
<tr><td>Compensation</td><td>G40, G41, G42</td><td>Cutter radius comp off / left / right</td></tr>
<tr><td>Tool length</td><td>G43, G49</td><td>Apply length offset / cancel</td></tr>
<tr><td>Mode</td><td>G90, G91</td><td>Absolute / incremental</td></tr>
</table></div>
<h2>Example</h2>
<p><code>G01 X50 F200</code> — linear feed. Then <code>X100</code> — still G01 (modal), now at X100. Then <code>G00 X0</code> — G00 replaces G01; rapid back to X0. Then <code>G81 Z-10 R5 F100</code> — G81 cancels G00 in the motion group? No: cycles are their own group. G81 activates a canned drill cycle; once drilling completes, motion returns to rapid positioning.</p>
<h2>Common Mistakes</h2>
<ul><li>Assuming every G-code is modal — some (like G28) are one-shot.</li><li>Forgetting to cancel a cycle with G80 before another motion.</li><li>Mixing up which group cancels which code.</li></ul>
{prac([
("After G01 X50, you write X80. What happens?", "Linear feed to X80 — G01 is modal, still active."),
("Which code cancels a drilling cycle?", "G80."),
("Can G43 and G01 be active at once?", "Yes — different modal groups. Tool length offset applies to whatever motion mode is active.")])}
{src(["Haas Mill Operator's Manual — modal groups table.","FANUC G-code lists differ by option; verify on your machine."])}''',
   prev=("04-program-structure","Program Structure"),
   nxt=("06-modal-codes","Modal Codes"))

print("Pages 01-05 done.")

# 06 Modal Codes
pg('06-modal-codes', "Modal vs Non-Modal Codes",
   "Understand modal state: why G01 persists, what cancels it, and how to track active modes.",
   f'''<h1>Modal vs Non-Modal Codes</h1>
<p class="cp-lead">Modal state is the hidden context that makes CNC programs look terse.</p>
{m("Key","Mill & Lathe")}
{obj(["What modal means","Modal groups and one-shot codes","Why cleanup blocks exist"])}
<h2>Concept</h2>
<p>A <strong>modal</strong> code stays active until canceled or replaced in the same group. A <strong>one-shot</strong> code works only on that block. G01 is modal; G28 is one-shot.</p>
<h2>Why It Matters</h2>
<p><code>G01 X50 F200</code> then <code>X100</code> then <code>X150</code> — all three move linearly at F200. If you forget this, you think X100 is rapid — it is not.</p>
<h2>How</h2>
<p>Only one code per modal group active. Motion (G00/G01/G02/G03), feed (G94/G95), comp (G40/G41/G42), cycles (G80–G89). G28 and G04 are one-shot.</p>
<h2>Example</h2>
{code('G01 X50. F200.\nX100.\nX150.\nG00 X0')}
<p>Startup block <code>G21 G17 G90 G40 G49 G80</code> resets every modal group.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting F persists.</li><li>Leaving G81 active — next X/Y drills unexpectedly.</li></ul>
{prac([
("After G81 Z-10 R5 F100, write X50 Y50. What happens?", "Cycle executes at X50 Y50. Need G80 to cancel."),
("Is G28 modal?", "No — one-shot.")])}
{src(["Haas Mill Operator Manual — modal groups."])}''',
   prev=("05-gcode-fundamentals","G-Code Fundamentals"),
   nxt=("07-plane-units","Planes & Units"))

# 07
pg('07-plane-units', "Planes, Units, and Conventions",
   "G17/G18/G19, G20/G21, and why a units error scrapes a part.",
   f'''<h1>Planes, Units, and Conventions</h1>
<p class="cp-lead">Trivial until a 25.4 mm error appears.</p>
{m("Beginner","Mill & Lathe")}
{obj(["G17/G18/G19 plane","G20/G21 units","Number formatting"])}
<h2>Concept</h2>
<p><strong>G17</strong> = XY (mill), <strong>G18</strong> = XZ (lathe), <strong>G19</strong> = YZ. Plane determines arc interpretation. <strong>G20</strong> = inch, <strong>G21</strong> = mm.</p>
<h2>Why It Matters</h2>
<p>Program says X100 in mm but machine is G20: it moves 100 inches. Crash. Always set units explicitly.</p>
<h2>How</h2>
<p>Always write decimal point: X50. = 50.0. X50 without decimal may be 0.05 on some controls.</p>
<h2>Example</h2>
<p>G17 G02 X50 Y50 I25 J0 — CW arc in XY. G18 active would interpret XZ (lathe).</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting G21.</li><li>No decimal point.</li></ul>
{prac([
("Why X50. not X50?", "Decimal point forces 50.0."),
("Lathe plane?", "G18 (XZ).")])}
{src(["Haas Operator Manual."])}''',
   prev=("06-modal-codes","Modal Codes"),
   nxt=("08-programming-math","Programming Math"))

# 08
pg('08-programming-math', "Practical Math for CNC",
   "Right triangles, sine/cosine, bolt circle coordinates, chamfer and radius.",
   f'''<h1>Practical Math for CNC</h1>
<p class="cp-lead">No calculus — triangles, circles, and converting drawings to coordinates.</p>
{m("Key","Mill & Lathe")}
{obj(["Pythagorean theorem","Bolt circle coordinates","Chamfer calculation"])}
<h2>Concept</h2>
<p>Every coordinate is either directly dimensioned or derived. Bolt circle at angle θ: X = R·cos(θ), Y = R·sin(θ). Verify CAM output yourself.</p>
<h2>Why It Matters</h2>
<p>CAM says hole at (86.6, 50) on R=100 at 30°. Check: 100·cos30=86.6, 100·sin30=50.0. If you cannot check, you cannot catch CAM errors.</p>
<h2>How</h2>
<p><strong>Distance:</strong> (10,20)→(50,50): √(40²+30²)=50 mm. <strong>Chamfer:</strong> 1×45° removes 1 mm in both axes.</p>
<h2>Example</h2>
<p>4 holes on 100 mm bolt circle (R=50): 0°=(50,0), 90°=(0,50), 180°=(-50,0), 270°=(0,-50).</p>
<h2>Common Mistakes</h2>
<ul><li>Using diameter as radius on bolt circles.</li></ul>
{prac([
("Hole on R=60 at 45°. X,Y?", "42.43, 42.43."),
("Distance (0,0)→(30,40)?", "50 mm.")])}
{src(["Sandvik Coromant — Machining Math."])}''',
   prev=("07-plane-units","Planes & Units"),
   nxt=("09-mcode-fundamentals","M-Codes"))

# 09
pg('09-mcode-fundamentals', "M-Codes and Machine Functions",
   "M00/M03/M05/M06/M08/M30 — what each does and why M-codes are machine-specific.",
   f'''<h1>M-Codes and Machine Functions</h1>
<p class="cp-lead">G-codes control motion; M-codes control the machine itself.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Stop/end codes","Spindle direction","Coolant and tool change","Why M-codes vary"])}
<h2>Concept</h2>
<p>M-codes are hardware functions. Near-standard but machine-specific. Verify on your machine.</p>
<h2>How</h2>
<div class="cp-table-wrap"><table>
<tr><th>Code</th><th>Function</th></tr>
<tr><td>M00</td><td>Program stop (always)</td></tr>
<tr><td>M01</td><td>Optional stop (switch ON)</td></tr>
<tr><td>M03</td><td>Spindle CW</td></tr>
<tr><td>M05</td><td>Spindle stop</td></tr>
<tr><td>M06</td><td>Tool change</td></tr>
<tr><td>M08/M09</td><td>Coolant on/off</td></tr>
<tr><td>M30</td><td>End and rewind</td></tr>
</table></div>
<h2>Example</h2>
{code('S2000 M03\nG43 H01 Z50.\nM08\n... cut ...\nM09 M05\nG91 G28 Z0\nM30')}
<h2>Common Mistakes</h2>
<ul><li>M00 vs M01 confusion.</li></ul>
{prac([("M00 vs M01?", "M00 always stops; M01 only if switch ON.")])}
{src(["Haas Operator Manual — M-Codes."])}''',
   prev=("08-programming-math","Programming Math"),
   nxt=("10-spindle-feed","Spindle & Feed"))

# 10
pg('10-spindle-feed', "Spindle and Feed Programming",
   "S command, RPM vs CSS, G96/G97, G94/G95, and cutting speed vs tool life.",
   f'''<h1>Spindle and Feed Programming</h1>
<p class="cp-lead">Speed and feed decide whether the tool cuts or burns.</p>
{m("Key","Mill & Lathe")}
{obj(["S and RPM","V = πDN/1000","G96 CSS vs G97","G94 mm/min vs G95 mm/rev"])}
<h2>Concept</h2>
<p><strong>S</strong> sets RPM. V = π·D·N/1000. On a lathe facing OD→center, G96 CSS holds surface speed by adjusting RPM as D changes.</p>
<h2>Why It Matters</h2>
<p>Too fast = burned tool. Too slow = rub and work-hardening. G97 S800 leaves the tool rubbing at center. G96 S200 adjusts RPM — but must be capped.</p>
<h2>How</h2>
<p><strong>Mill:</strong> N = 1000·V/(π·D). <strong>Lathe G97:</strong> constant RPM. <strong>G96:</strong> CSS + G50 S1800 cap. <strong>Feed:</strong> G94 mm/min (mill), G95 mm/rev (lathe). Feed = N × teeth × fz.</p>
<h2>Example</h2>
<p>D=50, V=200: N=1273. At D=25, G96 would give 2546 RPM — capped at 1800. 2000 RPM × 4 teeth × 0.03 = 240 mm/min.</p>
<h2>Common Mistakes</h2>
<ul><li>G96 without RPM cap.</li><li>G95 on a mill.</li></ul>
{prac([
("D=10, V=100. RPM?", "3183."),
("2000×4×0.03. Feed?", "240 mm/min."),
("Why cap G96?", "As D→0, RPM→∞.")])}
{src(["Sandvik Coromant formulas.","Haas Lathe Manual — G96/G97/G50."])}''',
   prev=("09-mcode-fundamentals","M-Codes"),
   nxt=("11-controller-dialects","Controller Dialects"))

# 11
pg('11-controller-dialects', "Controller Dialects",
   "Why Haas, FANUC, Siemens, HEIDENHAIN differ — read the manual.",
   f'''<h1>Controller Dialects</h1>
<p class="cp-lead">G-code is not one language. UK vs US vs Australian English — close, but details bite.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Why G-codes differ","FANUC/Haas vs Siemens/HEIDENHAIN","Post-processors"])}
<h2>Concept</h2>
<p>FANUC defined much of G-code; Haas follows FANUC. Siemens uses its own cycles. HEIDENHAIN uses conversational input. The <strong>post-processor</strong> translates CAM to machine-specific code.</p>
<h2>Why It Matters</h2>
<p>G84 on FANUC may be rigid tapping; on older machines it expects a floating tap. Copying code across machines without checking causes errors.</p>
<h2>How</h2>
<p>Learn the family: FANUC-style (Haas, Doosan, Hyundai) shares core codes. Siemens/HEIDENHAIN are different. Read the manual's G-code appendix.</p>
<h2>Common Mistakes</h2>
<ul><li>Assuming G84 is always rigid tapping.</li><li>Running CAM output without verifying post.</li></ul>
{prac([("What is a post-processor?", "Translates CAM toolpath into machine-specific G-code.")])}
{src(["Builder manuals."])}''',
   prev=("10-spindle-feed","Spindle & Feed"),
   nxt=("12-tool-offsets","Tool Offsets"))

print("Pages 06-11 done.")

# 12 Tool Offsets
pg('12-tool-offsets', "Tool Offsets",
   "Tool length H, geometry vs wear, tool nose radius — why machine position is not tool tip position.",
   f'''<h1>Tool Offsets</h1>
<p class="cp-lead">The machine knows where its spindle is, but it does not know how long your tool is. Tool offsets teach it.</p>
{m("Key","Mill & Lathe")}
{obj(["Why machine position ≠ tool tip position","Tool length offset G43 H","Geometry vs wear offset","Lathe tool nose radius and orientation"])}
<h2>Concept</h2>
<p>When you load a 100 mm end mill into the spindle, the machine's Z axis knows where the spindle face is — but not where the tip is. The <strong>tool length offset</strong> (G43 Hxx) stores that difference. The machine adds the offset to the programmed Z position so the tool tip actually reaches Z-5.</p>
<h2>Why It Matters</h2>
<p>If H01 says the tool is 100 mm long but it is actually 102 mm, every Z cut is 2 mm too shallow. The program is correct; the offset is wrong. This is why setup measurement and offset verification matter.</p>
<h2>How</h2>
<p><strong>Mill:</strong> G43 H01 applies length offset #1. G49 cancels. H values are measured at setup (tool setter or manual).</p>
<p><strong>Geometry vs wear:</strong> geometry offset = full tool length from setter. Wear offset = small correction (±0.01 mm) for dimensional tweaks without re-measuring.</p>
<p><strong>Lathe:</strong> geometry offset stores X and Z tool position relative to turret. Nose radius (R) and tool orientation (T-number, 0-9) are stored for radius compensation on turned contours.</p>
<h2>Example</h2>
<p>Program: G43 H01 Z50. G01 Z-5. F100. The machine moves Z to machine_home + H01 + (-5). If H01 = 150.000, the tool tip reaches Z=-5 in work coordinates. If H01 were 0, the spindle nose would crash into the part.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting G43 — spindle moves without length offset.</li><li>Confusing H number with T number (T01 may use H01, but not always).</li><li>Not updating wear offset after tool changes.</li><li>Ignoring tool nose radius on lathe profile work.</li></ul>
{prac([
("G43 H01 means?", "Apply tool length offset #1. The controller adds stored H01 value to every Z move."),
("Geometry vs wear offset?", "Geometry = measured tool length. Wear = small correction for dimensional adjustment.")])}
{src(["Haas Mill and Lathe Operator Manuals — Tool Offsets.","Tool setter and presetter documentation."])}''',
   prev=("11-controller-dialects","Controller Dialects"),
   nxt=("13-work-offsets","Work Offsets"))

# 13 Work Offsets
pg('13-work-offsets', "Work Offsets (G54–G59)",
   "Set part zero, multiple work offsets, datums, and why machine zero + work offset + tool offset = actual position.",
   f'''<h1>Work Offsets (G54–G59)</h1>
<p class="cp-lead">Work offsets tell the machine where your part sits. Get them wrong and every feature shifts by the same error.</p>
{m("Key","Mill & Lathe")}
{obj(["G54–G59 work coordinate systems","Edge finder and indicator setup","Multiple work offsets for setups","Datum strategy and why it matters"])}
<h2>Concept</h2>
<p><strong>G54–G59</strong> are six stored work offsets. Each offset stores X, Y, Z (and sometimes rotation) that tell the controller: "part zero is here relative to machine home." The program always uses work coordinates; the controller adds the G54 value to every move.</p>
<h2>Why It Matters</h2>
<p>If G54 X is off by 0.5 mm, every feature on the part is off by 0.5 mm — consistently. The program itself is perfect. This is why first-article inspection checks datum-to-feature relationships, not just individual dimensions.</p>
<h2>How</h2>
<p><strong>Mill setup:</strong> edge finder or indicator touches the part edge. X=0 on left edge, Y=0 on front edge. Z=0 on top surface. Values entered into G54.</p>
<p><strong>Multiple offsets:</strong> G54 for part 1, G55 for part 2 on a tombstone. One program machines both by switching G54↔G55.</p>
<p>The chain: <strong>machine position + work offset + tool offset = actual tool–workpiece relationship.</strong></p>
<h2>Example</h2>
<p>G54 X0.000 Y0.000 Z0.000. Program moves G00 X50 Y30. The machine goes to machine_home + G54 + (50,30). If you touched the wrong edge and G54 should be X-0.1, the hole is 0.1 mm off in X on every feature.</p>
<h2>Common Mistakes</h2>
<ul><li>Setting work zero on a feature that is not the drawing datum.</li><li>Using G54 for everything even when a second offset would avoid re-fixturing.</li><li>Forgetting to update G54 after moving the part.</li><li>Confusing tool length offset with work offset (Z work offset is part top; H is tool length).</li></ul>
{prac([
("If G54 X should be 0.000 but you entered 0.200, what happens?", "Every X coordinate shifts +0.2 mm. All features consistently wrong by 0.2 mm."),
("Why use G55 instead of G54?", "For a second part on the same tombstone or a second setup on the same program.")])}
{src(["Haas Operator Manual — Work Offsets.","Edge finder and indicator setup procedure."])}''',
   prev=("12-tool-offsets","Tool Offsets"),
   nxt=("14-linear-interpolation","Linear Interpolation"))

# 14 Linear Interpolation
pg('14-linear-interpolation', "Rapid and Linear Motion (G00/G01)",
   "G00 rapid vs G01 linear feed, safe approach and retract, envelope awareness.",
   f'''<h1>Rapid and Linear Motion (G00/G01)</h1>
<p class="cp-lead">The two most-used motion codes. G00 gets you there fast; G01 cuts at controlled feed.</p>
{m("Key","Mill & Lathe")}
{obj(["G00 rapid positioning vs G01 linear feed","Safe approach and retract paths","Multi-axis diagonal moves","Why rapid is not always diagonal"])}
<h2>Concept</h2>
<p><strong>G00</strong> = rapid positioning. The machine moves at its fastest traverse (often 15-30 m/min), but the path may not be straight — each axis moves independently and may stop at different times. Never assume G00 takes a diagonal line.</p>
<p><strong>G01</strong> = linear interpolation. The axes move simultaneously at a coordinated feed rate (F), cutting a straight line at exactly the programmed feed.</p>
<h2>Why It Matters</h2>
<p>A common crash: rapid to X50 Y30 Z-5 assuming a diagonal path. The machine may move Z first (into the vise), then X/Y. Use safe approach: rapid X/Y above the part, then Z down. Never rapid into cut material.</p>
<h2>How</h2>
{code('G00 X0 Y0        <span class="cp-comment">(rapid to XY position)</span>\nG00 Z5.         <span class="cp-comment">(rapid Z to 5 mm above part)</span>\nG01 Z-2. F100.  <span class="cp-comment">(feed down 2 mm deep)</span>\nG01 X100. F300. <span class="cp-comment">(cut straight line at 300 mm/min)</span>\nG00 Z5.         <span class="cp-comment">(rapid retract)</span>')}
<p>Approach: XY first, then Z down. Retract: Z up first, then XY. This avoids crashing into fixtures.</p>
<h2>Example</h2>
<p>G01 Z-2 F100 plunges at 100 mm/min (plunge feed). Then G01 X100 F300 cuts at 300 mm/min. Feed change on the fly is fine — F is modal.</p>
<h2>Common Mistakes</h2>
<ul><li>Rapiding Z into the part instead of above it.</li><li>Assuming G00 takes a straight diagonal.</li><li>Not specifying F on the first G01 block — F is modal but may be unset.</li></ul>
{prac([
("Why G00 not safe for cutting?", "It moves at maximum traverse with no controlled feed; it would break the tool."),
("Correct approach order?", "Rapid XY above part → rapid Z to clearance → feed Z down → cut.")])}
{src(["Haas Operator Manual — G00/G01.","Machine traverse speed specifications."])}''',
   prev=("13-work-offsets","Work Offsets"),
   nxt=("15-circular-interpolation","Circular Interpolation"))

# 15 Circular Interpolation
pg('15-circular-interpolation', "Circular Interpolation (G02/G03)",
   "G02 clockwise vs G03 counterclockwise, I/J arc center, R radius, direction from the correct plane.",
   f'''<h1>Circular Interpolation (G02/G03)</h1>
<p class="cp-lead">The hardest motion code to read. Get the direction right and arcs stop being a mystery.</p>
{m("Key","Mill & Lathe")}
{obj(["G02 CW vs G03 CCW — viewed from positive axis","I/J arc center vs R radius method","Start → Center → End → Direction","Why direction depends on the plane"])}
<h2>Concept</h2>
<p><strong>G02</strong> = clockwise arc. <strong>G03</strong> = counterclockwise arc. Direction is viewed looking from the positive axis of the current plane back toward the origin. In G17 (XY plane), you look down +Z. The arc is defined by start point (current position), end point (X/Y), and either center (I/J) or radius (R).</p>
<figure class="cp-figure"><svg viewBox="0 0 260 220" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="180" x2="240" y2="180" stroke="#17242f"/><line x1="40" y1="200" x2="40" y2="20" stroke="#17242f"/>
<text x="230" y="195" font-size="11">X</text><text x="25" y="25" font-size="11">Y</text>
<circle cx="40" cy="100" r="80" fill="none" stroke="#cfdbd8" stroke-dasharray="3"/>
<path d="M 40 180 A 80 80 0 0 1 120 100" fill="none" stroke="#0b766e" stroke-width="2.5"/>
<circle cx="40" cy="180" r="4" fill="#0b766e"/><text x="10" y="195" font-size="11" fill="#0b766e">S(0,0)</text>
<circle cx="120" cy="100" r="4" fill="#e07a3f"/><text x="125" y="95" font-size="11" fill="#e07a3f">E(20,20)</text>
<circle cx="40" cy="100" r="3" fill="#17242f"/><text x="5" y="95" font-size="11" fill="#17242f">C(0,20)</text>
<text x="55" y="160" font-size="10" fill="#0b766e">G03 90&deg;</text></svg>
<figcaption>Arc from S(0,0) to E(20,20), center C(0,20). This is G03 (CCW), 90° short arc. Not G02.</figcaption></figure>
<h2>Why It Matters</h2>
<p>The most common arc error: calling G02 when it should be G03. On a 90° corner, G02 cuts the 270° long way around (94.2 mm of arc instead of 31.4 mm). The machine does not alarm — it just cuts the wrong arc.</p>
<h2>How</h2>
<p><strong>I/J method:</strong> I = center X relative to start. J = center Y relative to start. These are <em>incremental from start point</em>, not absolute center coordinates.</p>
<p><strong>R method:</strong> R positive = arc ≤ 180° (short way). R negative = arc > 180° (long way).</p>
<h2>Example</h2>
<p>Start S(0,0), end E(20,20), center C(0,20). Radius = 20 mm. I = Cx − Sx = 0−0 = 0. J = Cy − Sy = 20−0 = 20.</p>
{code('G17 G90 G03 X20. Y20. I0 J20. F200.')}
<p>Arc length = 90° = &frac14; × 2π × 20 = 31.416 mm. If you used G02 instead, the machine would take the 270° long way = &frac34; × 2π × 20 = 94.248 mm — wrong arc.</p>
<p><strong>Check direction:</strong> looking down +Z, from S(0,0) to E(20,20) around center (0,20), the motion goes right and up — counterclockwise. That is G03.</p>
<h2>Common Mistakes</h2>
<ul><li>Using absolute center coordinates for I/J instead of incremental from start.</li><li>G02/G03 reversed because plane was wrong (G18 vs G17).</li><li>R positive when the arc should be >180°.</li><li>Forgetting that direction flips when you view from the other axis (lathe G18).</li></ul>
{prac([
("S(0,0), E(20,20), C(0,20). G02 or G03?", "G03 — counterclockwise 90° arc. G02 would be the 270° long way."),
("I and J are what kind of coordinate?", "Incremental: center minus start point. Not absolute."),
("Arc length for R=20, 90°?", "¼ × 2π × 20 = 31.416 mm.")])}
{src(["Haas Operator Manual — Circular Interpolation.","FANUC G-code programming guide — I/J vs R."])}''',
   prev=("14-linear-interpolation","Linear Interpolation"),
   nxt=("16-cutter-compensation","Cutter Compensation"))

# 16 Cutter Compensation
pg('16-cutter-compensation', "Cutter Radius Compensation (G41/G42)",
   "Program the part contour, not the tool center. Left/right comp, lead-in/out, and why G40 cleanup matters.",
   f'''<h1>Cutter Radius Compensation (G41/G42)</h1>
<p class="cp-lead">Instead of calculating tool center offsets for every contour, let the controller do it.</p>
{m("Key","Mill & Lathe")}
{obj(["What cutter comp does and why use it","G41 left vs G42 right","Lead-in and lead-out moves","G40 cancellation and common errors"])}
<h2>Concept</h2>
<p>When you mill a 50 mm square, you cannot program the part edges directly — the tool has a radius. Without comp, you must offset every coordinate by the tool radius yourself. <strong>Cutter radius compensation</strong> lets you program the part contour; the controller shifts the tool center path left or right by the stored tool radius (D offset).</p>
<figure class="cp-figure"><svg viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg">
<rect x="60" y="40" width="120" height="120" fill="none" stroke="#17242f" stroke-width="2"/>
<circle cx="120" cy="100" r="30" fill="none" stroke="#0b766e" stroke-width="2" stroke-dasharray="5"/>
<circle cx="120" cy="100" r="3" fill="#0b766e"/>
<text x="190" y="60" font-size="11" fill="#17242f">Part contour</text>
<text x="190" y="80" font-size="11" fill="#0b766e">Tool center path</text></svg>
<figcaption>Program the contour; the controller offsets the tool center path by radius.</figcaption></figure>
<h2>Why It Matters</h2>
<p>With comp, you can switch from a 10 mm end mill to an 8 mm end mill by changing the D offset — no program changes. Without comp, every coordinate must be recalculated. This is why cutter comp is essential for production.</p>
<h2>How</h2>
<p><strong>G41</strong> = left compensation (tool left of directed path). <strong>G42</strong> = right compensation. <strong>G40</strong> = cancel.</p>
<p>You must <strong>lead in</strong> on a linear move (G00/G01) at a distance greater than the tool radius — never engage comp on an arc. Cancel (G40) on a linear move away from the part.</p>
{code('G00 X0 Y0\nG41 X10. Y10. D01  <span class="cp-comment">(lead in, left comp)</span>\nG01 X50. F200.    <span class="cp-comment">(mill contour)</span>\n...\nG40 X0 Y0         <span class="cp-comment">(cancel on linear move)</span>')}
<h2>Example</h2>
<p>Program a 50×50 mm square contour. D01 stores 5.000 (10 mm tool radius). The controller offsets the tool center 5 mm outside the programmed contour. Switch to an 8 mm tool: change D01 to 4.000. Program unchanged.</p>
<h2>Common Mistakes</h2>
<ul><li>Engaging G41/G42 on an arc — causes alarm.</li><li>Forgetting G40 before the next operation — comp stays active.</li><li>Lead-in shorter than tool radius — tool gouges the corner.</li><li>Using G41 vs G42 backwards (climb vs conventional).</li></ul>
{prac([
("G41 vs G42?", "G41 = tool left of directed path. G42 = tool right."),
("Why must lead-in be linear?", "Comp engages on a straight move; arcs require comp already active.")])}
{src(["Haas Operator Manual — Cutter Compensation.","D offset = tool radius, not diameter."])}''',
   prev=("15-circular-interpolation","Circular Interpolation"),
   nxt=("17-drilling-cycles","Drilling Cycles"))

# 17 Drilling Cycles
pg('17-drilling-cycles', "Drilling and Boring Cycles",
   "G81 drilling, G82 dwell, G83 peck, G85 boring — purpose, parameters, and tool path.",
   f'''<h1>Drilling and Boring Cycles</h1>
<p class="cp-lead">Instead of writing 5 lines per hole, one G81 block repeats the whole drill-retract sequence.</p>
{m("Key","Mill")}
{obj(["G81 simple drill vs G82 dwell vs G83 peck","G85 boring feed-in/feed-out","Cycle parameters: R plane, Z depth","G80 cancel"])}
<h2>Concept</h2>
<p>A <strong>canned drilling cycle</strong> packages rapid to position → rapid to R plane → feed to depth → retract into one block. It stays modal: move to the next X/Y and the cycle repeats. G80 cancels.</p>
<h2>Why It Matters</h2>
<p>Drilling 20 holes without cycles means 100+ lines. With G81, it is 20 lines — one per hole. Peck drilling (G83) retracts between pecks to clear chips, essential for deep holes.</p>
<h2>How</h2>
<div class="cp-table-wrap"><table>
<tr><th>Cycle</th><th>Purpose</th><th>Retract</th></tr>
<tr><td>G81</td><td>Simple drill</td><td>Rapid out</td></tr>
<tr><td>G82</td><td>Drill + dwell (better finish at bottom)</td><td>Rapid out</td></tr>
<tr><td>G83</td><td>Peck drill (chip evacuation)</td><td>Rapid out each peck</td></tr>
<tr><td>G85</td><td>Bore (feed in, feed out)</td><td>Feed out</td></tr>
</table></div>
<p><strong>R plane</strong> (R) = safe retract height above part (typically 2-5 mm). <strong>Z depth</strong> = final drill depth.</p>
{code('G81 G99 X10. Y10. Z-15. R5. F100.  <span class="cp-comment">(hole A)</span>\nX50. Y30.                    <span class="cp-comment">(hole B, repeats)</span>\nG80                           <span class="cp-comment">(cancel)</span>')}
<h2>Example</h2>
<p>G83 for a 20 mm deep hole in steel: Z-20, R5. The drill pecks down in steps (e.g. 5 mm), retracts fully to clear chips, then continues. F100 feed. Without peck, the drill rubs and work-hardens the bottom.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting G80 — next X/Y move drills unexpectedly.</li><li>Using G81 for deep holes (chip packing) — use G83.</li><li>R plane too close to the part — rapid retract crashes into clamps.</li><li>Confusing G84 tapping (see Tapping page) with rigid tapping availability.</li></ul>
{prac([
("G81 vs G83?", "G81 is simple drill. G83 pecks and retracts to clear chips for deep holes."),
("What does R5 mean?", "R plane at Z=5 mm above the part — safe rapid height.")])}
{src(["Haas Mill Operator Manual — Drilling Cycles.","Sandvik Coromant — drill point geometry and peck depth."])}''',
   prev=("16-cutter-compensation","Cutter Compensation"),
   nxt=("18-canned-cycles","Canned Cycles"))

# 18 Canned Cycles
pg('18-canned-cycles', "Canned Cycles Reference",
   "G98/G99 retract mode, R plane, cycle repetition, G80 cancel, and how cycles chain.",
   f'''<h1>Canned Cycles Reference</h1>
<p class="cp-lead">One block repeats a multi-step operation at every hole position. This page explains the cycle structure itself.</p>
{m("Key","Mill")}
{obj(["Anatomy of a canned cycle","G98 retract to initial plane vs G99 to R plane","Repetition with L/K","G80 cancel and cycle state"])}
<h2>Concept</h2>
<p>Every canned cycle follows the same 5-step sequence: (1) rapid to X/Y position, (2) rapid to R plane, (3) feed to Z depth, (4) dwell or optional actions, (5) retract — either to R plane (G99) or to the initial Z height (G98).</p>
<h2>Why It Matters</h2>
<p>G99 retracts to R plane between holes — faster when no obstacles. G98 retracts to the initial Z height — needed when crossing a clamp or boss. Choosing wrong means crashing the drill head into a fixture.</p>
<h2>How</h2>
<p><strong>G99</strong>: retract to R plane (stay low, faster). Use when holes are in a clear pattern.</p>
<p><strong>G98</strong>: retract to initial plane (go high). Use when crossing over a fixture, wall, or clamp.</p>
<p><strong>L/K repetition</strong> (controller-dependent): repeat the cycle at incremental positions for a row of holes.</p>
{code('G90 G00 X0 Y0 Z50.     <span class="cp-comment">(initial plane Z50)</span>\nG99 G81 X10. Y10. Z-15. R5. F100.  <span class="cp-comment">(retract to R=5)</span>\nX50. Y30.              <span class="cp-comment">(next hole, retract to R=5)</span>\nG98 X80. Y10.          <span class="cp-comment">(retract to Z50, crossing a boss)</span>\nG80')}
<h2>Example</h2>
<p>4 holes in a row at X10, X30, X50, X70, Y20. With G99, each hole retracts only to R5 between them — efficient. If a clamp sits between hole 2 and 3, switch to G98 for that move so the drill lifts over the clamp.</p>
<h2>Common Mistakes</h2>
<ul><li>Using G99 when a fixture stands between holes.</li><li>Forgetting G80 — cycle stays active after all holes.</li><li>Confusing R plane with initial plane.</li><li>Changing Z depth mid-cycle without resetting the cycle.</li></ul>
{prac([
("G98 vs G99?", "G98 retracts to initial Z height. G99 retracts only to R plane."),
("When must you use G98?", "When the drill must clear an obstacle between hole positions.")])}
{src(["Haas Mill Operator Manual — G98/G99.","FANUC canned cycle programming guide."])}''',
   prev=("17-drilling-cycles","Drilling Cycles"),
   nxt=("19-turning-fundamentals","Turning Fundamentals"))

print("Pages 12-18 done.")

# 19 Turning Fundamentals
pg('19-turning-fundamentals', "Turning Coordinates and Setup",
   "Lathe coordinate system, diameter programming, X/Z, tool nose, and G18 plane.",
   f'''<h1>Turning Coordinates and Setup</h1>
<p class="cp-lead">The lathe looks like a different world because X means diameter, not position.</p>
{m("Key","Lathe")}
{obj(["Lathe X/Z axes and diameter programming","Tool post orientation and turret","G18 XZ plane","Work offset setup on a chuck"])}
<h2>Concept</h2>
<p>On a lathe, <strong>Z</strong> runs along the spindle axis (away from chuck is negative). <strong>X</strong> is radial, but in <strong>diameter programming</strong> — the standard — X values are the full diameter, not the radius. The workpiece spins; the tool feeds in X and Z.</p>
<h2>Why It Matters</h2>
<p>Commanding X30 on a lathe means the tool tip sits at a 30 mm diameter = 15 mm from center. If you think radius, you double-cut depth. This is the #1 lathe beginner mistake.</p>
<h2>How</h2>
<p>Work zero is on the face center (Z=0 at the part face, X=0 at spindle center). Z negative cuts into the part. X increases outward. G18 selects the XZ plane for arcs.</p>
<p>Tool tip geometry: insert has a nose radius (e.g. 0.4 mm). Tool nose radius compensation (G41/G42 in G18) adjusts for this on profiled work.</p>
<h2>Example</h2>
<p>Bar stock &Oslash;50. Face the part: G01 X0 Z0 F0.2. Then turn OD to &Oslash;40: G01 X40 Z-20. The tool moves from X50 to X40 (diameter), cutting 5 mm radial depth (10 mm diameter reduction over the pass).</p>
<h2>Common Mistakes</h2>
<ul><li>Programming X as radius instead of diameter.</li><li>Z positive direction confusion (away from chuck = negative on most lathes).</li><li>Forgetting G18 when programming arcs.</li></ul>
{prac([
("Bar &Oslash;50, command X46. Radial depth?", "Diameter drop 4 mm; radial depth = 2 mm."),
("Where is work zero on a lathe?", "Typically on the face center: X0 at spindle center, Z0 at the part face.")])}
{src(["Haas Lathe Operator Manual — Coordinates and Diameter Programming."])}''',
   prev=("18-canned-cycles","Canned Cycles"),
   nxt=("20-turning-cycles","Turning Cycles"))

# 20 Turning Cycles
pg('20-turning-cycles', "Roughing and Finishing Cycles (G71/G70)",
   "G71 stock removal, G70 finish pass, profile definition with P/Q, and stock allowance.",
   f'''<h1>Roughing and Finishing Cycles (G71/G70)</h1>
<p class="cp-lead">Instead of writing every roughing pass, G71 automatically steps over the entire profile.</p>
{m("Key","Lathe")}
{obj(["G71 roughing cycle mechanics","P/Q profile definition blocks","U/W stock allowance","G70 finish pass"])}
<h2>Concept</h2>
<p><strong>G71</strong> (stock removal turning) automatically cuts multiple roughing passes along a defined profile. You define the final shape between P (start) and Q (end) blocks, set depth of cut and stock allowance, and the machine does the rest. <strong>G70</strong> then takes the finish pass.</p>
<h2>Why It Matters</h2>
<p>Without G71, roughing a 5-step shaft means writing 15+ passes by hand. G71 does it in one cycle call, recalculating each pass automatically. This is why lathe programming relies on cycles.</p>
<h2>How</h2>
{code('G71 U2. R1.       <span class="cp-comment">(depth of cut 2mm, retract 1mm)</span>\nG71 P10 Q20 U0.2 W0.1 F200.  <span class="cp-comment">(stock: X0.2, Z0.1)</span>\nN10 G00 X20.      <span class="cp-comment">(profile start)</span>\nG01 Z0 F100.\nX40. Z-20.\nZ-40.\nN20 X50.          <span class="cp-comment">(profile end)</span>\nG70 P10 Q20       <span class="cp-comment">(finish pass)</span>')}
<p>U2 = depth of cut per pass. R1 = retract distance. U0.2 = finishing stock in X (diameter). W0.1 = finishing stock in Z.</p>
<h2>Example</h2>
<p>&Oslash;50 bar turned to a profile: &Oslash;40 for 20 mm, &Oslash;30 for 20 mm, with a chamfer. G71 roughs in 2 mm passes leaving 0.2 mm diameter stock. G70 then takes a single finish pass at full feed to size.</p>
<h2>Common Mistakes</h2>
<ul><li>Profile start/end blocks (P/Q) not properly defined.</li><li>Stock allowance U0.2 too large or zero.</li><li>Changing feed inside the profile — G71 overrides with its own F.</li></ul>
{prac([
("G71 U2 R1 means?", "2 mm depth of cut per roughing pass, 1 mm retract between passes."),
("What does G70 do?", "Takes the finishing pass along the same P/Q profile at finish feed/speed.")])}
{src(["Haas Lathe Operator Manual — G71/G70.","FANUC lathe cycle programming guide."])}''',
   prev=("19-turning-fundamentals","Turning Coordinates"),
   nxt=("21-grooving-parting-boring","Grooving, Parting, Boring"))

# 21 Grooving, Parting, Boring
pg('21-grooving-parting-boring', "Grooving, Parting, and Boring",
   "Groove tool reference edges, parting cut with bar pullout, and boring bar setup.",
   f'''<h1>Grooving, Parting, and Boring</h1>
<p class="cp-lead">These operations look simple but have specific tool geometry and feed considerations.</p>
{m("Key","Lathe")}
{obj(["Groove tool reference edge (left/right)","Parting cut safety and pullout","Boring bar setup and depth limit","Internal vs external tooling"])}
<h2>Concept</h2>
<p>A grooving/parting tool is a narrow insert. Its <strong>reference edge</strong> is either the left or right corner — this determines which X coordinate you program. Boring bars cut internal diameters; they must be rigid enough to avoid chatter.</p>
<h2>Why It Matters</h2>
<p>Groove tools have width (e.g. 3 mm). If you program the left edge at X30, the right edge is at X33. Parting off at the wrong X leaves a nub or cuts too early. Boring bars deflect if too long — causing taper and chatter.</p>
<h2>How</h2>
<p><strong>Grooving:</strong> position at groove X, feed in at reduced feed. Use G01 with dwell (G04) at the bottom for a clean finish. <strong>Parting:</strong> feed to X near center, then stop and break off — never feed to X0 (tool binds). <strong>Boring:</strong> bore bar enters from the right, feeds left into the part; internal X coordinates increase outward from center.</p>
<h2>Example</h2>
<p>Part off &Oslash;40 bar: G01 X1 F0.05. Feed slowly to X1 (1 mm diameter remaining). M05, then part off manually. Feeding to X0 would jam the tool and break the insert.</p>
<h2>Common Mistakes</h2>
<ul><li>Parting to X0 — tool binds and breaks.</li><li>Not accounting for groove tool width in coordinates.</li><li>Boring bar too long for the hole depth — chatter and taper.</li></ul>
{prac([
("Why not part to X0?", "The tool binds against the center nub. Leave 1-2 mm and break off manually."),
("Boring bar rule of thumb?", "Boring bar length-to-diameter ratio should be under 4:1 to avoid deflection.")])}
{src(["Sandvik Coromant — Grooving and Parting Tooling.","Haas Lathe Manual."])}''',
   prev=("20-turning-cycles","Turning Cycles"),
   nxt=("22-threading","Threading"))

# 22 Threading
pg('22-threading', "Single-Point Threading (G76)",
   "Pitch, lead, thread depth, G76 threading cycle, and infeed/outfeed strategy.",
   f'''<h1>Single-Point Threading (G76)</h1>
<p class="cp-lead">Threads require multiple passes with decreasing depth — G76 automates this.</p>
{m("Key","Lathe")}
{obj(["Pitch vs lead, major/minor diameter","G76 threading cycle parameters","Multiple passes and infeed angle","Thread depth calculation"])}
<h2>Concept</h2>
<p>A thread is a helical groove. On a lathe, the spindle synchronizes with the Z feed so each pass follows the helix. <strong>Pitch</strong> = distance between threads (mm). <strong>Lead</strong> = distance per revolution (= pitch for single-start). G76 automates multiple passes with decreasing depth.</p>
<h2>Why It Matters</h2>
<p>Cutting a thread in one pass would break the tool. Each pass cuts a shallow depth (chip load), and the infeed angle controls how the insert engages. Wrong pitch = scrap thread. Wrong depth = loose or tight fit.</p>
<h2>How</h2>
{code('G76 P010060 Q0.1 R0.05\nG76 X28. Z-20. P1.08 Q0.3 F1.5')}
<p>F1.5 = pitch 1.5 mm. P1.08 = thread depth (mm, radial). Q0.3 = first pass depth. X28 = minor diameter. The machine makes multiple passes automatically.</p>
<p>Thread depth for 60° metric: depth ≈ 0.613 × pitch. For M30×1.5: depth ≈ 0.92 mm. Minor diameter ≈ 30 − 2×0.92 = 28.16 mm.</p>
<h2>Example</h2>
<p>M30×1.5 external thread on &Oslash;30 bar. Major dia = 30. Minor dia ≈ 28.16. Z length = 20 mm. G76 cuts ~5-6 passes at decreasing depth. Feed = pitch = 1.5 mm/rev (G95 mode).</p>
<h2>Common Mistakes</h2>
<ul><li>Wrong F value — F must equal pitch in mm/rev (G95).</li><li>Not leaving enough clearance at thread start (lead-in distance).</li><li>Too-deep first pass — tool breaks.</li><li>Confusing pitch with feed rate.</li></ul>
{prac([
("M20×1.5 thread. Feed rate in G95?", "F1.5 — feed per revolution equals pitch."),
("Approx thread depth for M30×1.5?", "0.613 × 1.5 ≈ 0.92 mm radial.")])}
{src(["Sandvik Coromant — Threading Formulas.","Haas Lathe Manual — G76."])}''',
   prev=("21-grooving-parting-boring","Grooving, Parting, Boring"),
   nxt=("23-program-safety","Program Safety"))

# 23 Program Safety
pg('23-program-safety', "Safe Program Start and Restart",
   "Why G21 G17 G90 G40 G49 G80 exists, known machine state, safe approach, and restart procedure.",
   f'''<h1>Safe Program Start and Restart</h1>
<p class="cp-lead">The startup block is not superstition — it resets the machine to a known state.</p>
{m("Key","Mill & Lathe")}
{obj(["Why every program starts with known-state codes","Safe approach and clearance plane","Program restart after tool breakage","Checklists before cycle start"])}
<h2>Concept</h2>
<p>At the top of every program: <code>G21 G17 G90 G40 G49 G80</code>. This explicitly sets: mm units, XY plane, absolute mode, cutter comp off, tool length comp off, canned cycles off. It wipes any leftover modal state from the previous job.</p>
<h2>Why It Matters</h2>
<p>If the previous program left G41 active and your new program does not cancel it, the machine silently offsets the tool path. The startup block prevents this. Safe approach means never moving Z below the part until X/Y is positioned above it.</p>
<h2>How</h2>
<p><strong>Before cycle start:</strong> check tool number, work offset, spindle direction, coolant. <strong>Safe approach:</strong> rapid XY to position, then Z down. <strong>Restart:</strong> after a tool break, find the line number, position the tool manually, and restart from that block — never from the top.</p>
<div class="cp-safety-note"><strong>Safety:</strong> Always run the first part in single block with feed hold ready. Never assume the program is safe because it backplots correctly.</div>
<h2>Example</h2>
<p>Startup block: G21 (mm), G17 (XY plane), G90 (absolute), G40 (comp off), G49 (length off), G80 (cycles off). Then T01 M06, G54, S2000 M03, G43 H01 Z50, M08.</p>
<h2>Common Mistakes</h2>
<ul><li>Skipping the startup block to "save lines."</li><li>Rapiding Z into the part before XY is clear.</li><li>Restarting from program top after a mid-program tool break — re-cuts already-machined geometry.</li></ul>
{prac([
("Why G40 G49 G80 at startup?", "Cancels any leftover cutter comp, tool length comp, or drill cycles from the previous job."),
("After a tool breaks at line N80, what do you do?", "Replace tool, position manually near N80, restart from that block — not from the top.")])}
{src(["Haas Operator Manual — Program Restart.","Shop safety practices; always follow your machine's lockout/tagout procedures."])}''',
   prev=("22-threading","Threading"),
   nxt=("24-verification","Verification"))

# 24 Verification
pg('24-verification', "Program Verification and First Article",
   "Code review, backplot simulation, dry run, single block, and first-article inspection.",
   f'''<h1>Program Verification and First Article</h1>
<p class="cp-lead">Writing the program is half the job. Proving it is safe before cutting metal is the other half.</p>
{m("Key","Mill & Lathe")}
{obj(["Code review checklist","Backplot vs actual machine","Dry run and single block","First-article inspection"])}
<h2>Concept</h2>
<p>Verification is a staged process: read the code → backplot on screen → dry run at height → single block → reduced feed → first part. Each stage catches a different class of error. Never skip to full-speed cutting.</p>
<h2>Why It Matters</h2>
<p>Simulation shows tool motion but does not know about your vise, clamps, or tool holder. Dry run at Z=50 (above part) catches gross coordinate errors. Single block lets you stop between moves. The first part proves everything.</p>
<div class="cp-safety-note"><strong>Important:</strong> Backplot simulation is not a substitute for dry run. It cannot detect missing fixture geometry, incorrect offsets, or machine envelope violations.</div>
<h2>How</h2>
<ol><li><strong>Code review:</strong> check units, G90/G91, work offset, tool number, spindle direction, Z approach.</li>
<li><strong>Backplot:</strong> trace the tool path on screen — look for unexpected moves.</li>
<li><strong>Dry run:</strong> Z at +50, program runs, no cutting.</li>
<li><strong>Single block:</strong> one block at a time, feed hold ready.</li>
<li><strong>Reduced feed:</strong> 25% feed override, first cut.</li>
<li><strong>First article:</strong> measure critical dimensions against drawing.</li></ol>
<h2>Example</h2>
<p>Program mills a pocket. Backplot shows the tool path inside the pocket — looks fine. Dry run reveals the tool holder would hit the vise because the pocket is deeper than expected. Single block confirms the approach is safe. First part measured: pocket depth 10.02 vs drawing 10.00 — adjust wear offset by -0.02.</p>
<h2>Common Mistakes</h2>
<ul><li>Trusting backplot over dry run.</li><li>Running full feed on the first part.</li><li>Measuring only one dimension on first article.</li></ul>
{prac([
("Why can't simulation replace dry run?", "Simulation does not model your actual vise, clamps, or tool holder. Dry run on the real machine catches those."),
("What does first-article inspection check?", "Every critical dimension: datum location, hole positions, depths, tolerances, surface finish.")])}
{src(["AS9102 First Article Inspection requirements (aerospace).","Shop verification best practices."])}''',
   prev=("23-program-safety","Program Safety"),
   nxt=("25-troubleshooting","Troubleshooting"))

# 25 Troubleshooting
pg('25-troubleshooting', "CNC Programming Troubleshooting",
   "Alarms, unexpected motion, wrong geometry, offset errors — diagnose methodically.",
   f'''<h1>CNC Programming Troubleshooting</h1>
<p class="cp-lead">When the machine does something unexpected, work the problem systematically — do not guess.</p>
{m("Key","Mill & Lathe")}
{obj(["Alarm diagnosis approach","Geometry errors: offset vs program","Unexpected motion: modal state","Wrong direction: G90/G91 or plane"])}
<h2>Concept</h2>
<p>Every problem has a symptom. Method: note the symptom → check the machine state (modal codes active) → review the relevant block → check offsets → test one change at a time. Never change multiple things at once.</p>
<h2>Why It Matters</h2>
<p>A part cuts 0.5 mm off in X. Is the program wrong, the G54 offset wrong, or the tool wear offset wrong? Change one, test, measure. Change all three at once and you learn nothing.</p>
<h2>How</h2>
<div class="cp-table-wrap"><table>
<tr><th>Symptom</th><th>Check</th></tr>
<tr><td>Tool moves wrong direction</td><td>G90 vs G91, G54 offset sign</td></tr>
<tr><td>Dimension consistently off</td><td>Work offset or wear offset</td></tr>
<tr><td>Dimension varies per feature</td><td>Program coordinate error</td></tr>
<tr><td>Unexpected drill move</td><td>G80 missing; cycle still active</td></tr>
<tr><td>Arc cuts wrong way</td><td>G02/G03 reversed or wrong plane</td></tr>
<tr><td>Cutter comp alarm</td><td>Lead-in on arc or comp not engaged</td></tr>
</table></div>
<h2>Example</h2>
<p>All holes are 0.3 mm too far right. The program coordinates are correct (you checked). G54 X should be 0.000 but was entered as 0.300. Fix G54, rerun — holes correct. If only one hole is wrong, the program coordinate for that hole has a typo.</p>
<h2>Common Mistakes</h2>
<ul><li>Changing the program before checking offsets.</li><li>Changing multiple offsets at once.</li><li>Ignoring the alarm code — read it, look it up, do not just press reset.</li></ul>
{prac([
("All features off by 0.2 mm in X. First thing to check?", "G54 work offset X value. Consistent offset error = work offset issue."),
("Only one hole is at the wrong position. Check?", "Program coordinate for that specific hole. Per-feature error = program typo.")])}
{src(["Haas Alarm Code List.","FANUC Programmer's Guide."])}''',
   prev=("24-verification","Verification"),
   nxt=("26-common-mistakes","Common Mistakes"))

# 26 Common Mistakes
pg('26-common-mistakes', "Common Beginner Mistakes",
   "The 15 mistakes every new CNC programmer makes — and how to catch them before they crash.",
   f'''<h1>Common Beginner Mistakes</h1>
<p class="cp-lead">Every programmer makes these. The professionals catch them on paper before they reach the machine.</p>
{m("Beginner","Mill & Lathe")}
{obj(["The most frequent beginner errors","How to catch each on paper","Building personal checklists"])}
<h2>The 15 Mistakes</h2>
<ol>
<li><strong>Wrong work offset</strong> — G54 X/Y set on the wrong edge. Check: touch off on the drawing datum.</li>
<li><strong>Wrong tool offset</strong> — H number mismatched to tool. Check: T01 uses H01? Verify.</li>
<li><strong>Wrong units</strong> — G20 vs G21. 25.4 mm error. Always set G21 explicitly.</li>
<li><strong>Wrong plane</strong> — G17 vs G18. Arcs cut wrong. Confirm before arcs.</li>
<li><strong>G90/G91 mix-up</strong> — incremental after absolute. Check mode before coordinate moves.</li>
<li><strong>G41/G42 reversed</strong> — tool cuts the wrong side. Visualize climb vs conventional.</li>
<li><strong>Missing G40</strong> — comp stays active. Always cancel before new operation.</li>
<li><strong>Missing G80</strong> — cycle drills unexpectedly. Cancel after hole patterns.</li>
<li><strong>Wrong Z direction</strong> — Z up = positive on mill. Plunge negative. Confirm.</li>
<li><strong>Wrong spindle direction</strong> — M03 vs M04. Right-hand tools cut CW (M03).</li>
<li><strong>Unsafe rapid</strong> — G00 Z into the part. Always Z-up first.</li>
<li><strong>Wrong tool number</strong> — T02 M06 loads the wrong tool. Verify holder at spindle.</li>
<li><strong>Wrong arc center</strong> — I/J absolute instead of incremental. Recalculate.</li>
<li><strong>Copy-paste code</strong> — coordinates not changed. Read every block.</li>
<li><strong>No decimal point</strong> — X50 vs X50. Write X50. always.</li>
</ol>
<h2>How to Catch Them</h2>
<p>Build a personal checklist. Before cycle start: units, plane, mode (G90), work offset, tool number, spindle direction, Z approach, comp canceled, cycles canceled. Run through it every time.</p>
{prac([
("You milled a pocket 0.5 mm too deep. What to check first?", "Z work offset (part top) and H tool length offset. Consistent depth error = offset, not program."),
("Why write X50. not X50?", "Decimal point avoids controller ambiguity — some controls treat X50 as 0.05.")])}
{src(["Compiled from common shop-floor errors.","Build your own checklist."])}''',
   prev=("25-troubleshooting","Troubleshooting"),
   nxt=("27-turning-project","Turning Project"))

print("Pages 19-26 done.")

# 27 Turning Project
pg('27-turning-project', 'Project: Stepped Shaft',
   'Complete worked example: raw bar to finished stepped shaft with process plan, coordinates, and full program.',
   f'''<h1>Project: Stepped Shaft</h1>
<p class="cp-lead">Put it all together: a &Oslash;40 bar turned to a two-step shaft with chamfer, faced, and parted off.</p>
{m("Key","Lathe")}
{obj(["Read a simple shaft drawing","Plan operations and tools","Calculate coordinates","Write a complete turning program"])}
<h2>Concept</h2>
<p><strong>Part:</strong> &Oslash;40 bar stock. Turn to &Oslash;30 for 15 mm, then &Oslash;20 for 20 mm, with 1&times;45&deg; chamfers. Face, rough, finish, part off. Material: free-machining steel.</p>
<h2>Process Plan</h2>
<ol><li>Face part (T01).</li><li>Rough OD turns (T02, G71).</li><li>Finish OD turns (T02, G70).</li><li>Chamfer.</li><li>Part off (T03).</li></ol>
<h2>How: The Program</h2>
{code('O2701\nG21 G97 G99\nT0101 M03 S1500  <span class="cp-comment">(facing tool)</span>\nG00 X42. Z0.1\nG01 Z0 F0.2\nX-1. F0.15\nG00 X42. Z2.\nT0202 M03 S2000  <span class="cp-comment">(OD turn tool)</span>\nG71 U2. R1.\nG71 P10 Q20 U0.2 W0.1 F0.25\nN10 G00 X18.\nG01 Z0 F0.1\nX20. Z-1.  <span class="cp-comment">(chamfer)</span>\nZ-20.       <span class="cp-comment">(Ø20 step)</span>\nX30. Z-20.\nZ-35.       <span class="cp-comment">(Ø30 step)</span>\nX40.\nN20 G00 Z2.\nG70 P10 Q20\nG00 X100. Z100.\nT0303 M03 S1200  <span class="cp-comment">(part-off tool)</span>\nG00 X42. Z-36.\nG01 X1. F0.08\nG00 X45.\nM05\nM30')}
<h2>Verification</h2>
<p>Backplot the profile. Confirm: facing cuts from center outward, G71 leaves 0.2 mm stock, G70 finishes, part-off at Z-36 leaves the part length. Check G54 on face center. Single block first pass.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting the chamfer block in N10–N20.</li><li>Part-off too early (part too short).</li><li>G71 stock U0.2 not set — finish pass has no stock.</li></ul>
{prac([
("Why G99 (feed/rev)?", "Lathe standard: feed per revolution. F0.25 = 0.25 mm per revolution."),
("Part-off at Z-36 gives what part length?", "From face Z0 to Z-36 = 36 mm long part (plus parting tool width).")])}
{src(["Worked example; adjust speeds/feeds for your material and tooling."])}''',
   prev=("26-common-mistakes","Common Mistakes"),
   nxt=("28-milling-project","Milling Project"))

# 28 Milling Project
pg('28-milling-project', 'Project: Mounting Plate',
   'Complete worked example: 100x80x12 mm plate — face, pocket, 4 holes, chamfer.',
   f'''<h1>Project: Mounting Plate</h1>
<p class="cp-lead">A complete mill program: rectangular block, face mill, pocket, bolt holes, and chamfer.</p>
{m("Key","Mill")}
{obj(["Read a simple plate drawing","Plan mill operations","Write a complete mill program","Verify approach and retract"])}
<h2>Concept</h2>
<p><strong>Part:</strong> 100&times;80&times;12 mm aluminum plate. Mill 60&times;40&times;5 mm pocket centered, drill 4 &Oslash;8 holes at corners (10 mm in from edges), face top.</p>
<h2>Process Plan</h2>
<ol><li>Face top (T01, &Oslash;63 face mill).</li><li>Rough/finish pocket (T02, &Oslash;10 end mill).</li><li>Drill 4 holes (T03, &Oslash;8 drill).</li><li>Chamfer holes (T04).</li></ol>
<h2>How: The Program</h2>
{code('O2801\nG21 G17 G90 G40 G49 G80\nT01 M06          <span class="cp-comment">(face mill)</span>\nG54 G00 X-40 Y0 S2000 M03\nG43 H01 Z50. M08\nG00 Z2.\nG01 Z0. F300.\nX140. F400.      <span class="cp-comment">(face pass)</span>\nG00 Z50.\nT02 M06          <span class="cp-comment">(end mill)</span>\nG54 G00 X-30 Y-20 S2500 M03\nG43 H02 Z50.\nG00 Z2.\nG01 Z-5. F150.   <span class="cp-comment">(pocket depth)</span>\nG41 X0 Y0 D02 F300.\nY20. X60. Y-20. X0.  <span class="cp-comment">(pocket contour)</span>\nG40 X-30 Y-20.\nG00 Z50.\nT03 M06          <span class="cp-comment">(drill)</span>\nG54 G00 X10 Y10 S1500 M03\nG43 H03 Z50.\nG99 G81 Z-15. R5. F120.\nX90. Y10.\nX90. Y70.\nX10. Y70.\nG80\nG00 Z50. M09\nM05\nG91 G28 Z0\nM30')}
<h2>Verification</h2>
<p>Check: face mill starts off the left edge, pocket lead-in with G41, holes at (10,10)/(90,10)/(90,70)/(10,70), G80 after drilling. Single block: confirm Z approach, pocket depth, hole positions.</p>
<h2>Common Mistakes</h2>
<ul><li>Pocket lead-in on an arc (must be linear).</li><li>Forgetting G80 after holes.</li><li>Face mill starting on the part (must start off-edge).</li></ul>
{prac([
("Holes at corners 10 mm in from edges on 100x80 plate. Coordinates?", "(10,10), (90,10), (90,70), (10,70)."),
("Why G41 lead-in at X-30 Y-20?", "Start outside the pocket, ramp in with cutter comp engaged, then cut contour.")])}
{src(["Worked example; adjust speeds/feeds for aluminum."])}''',
   prev=("27-turning-project","Turning Project"),
   nxt=("29-subprograms","Subprograms"))

# 29 Subprograms
pg('29-subprograms', "Subprograms (M98/M99)",
   'Main program calls a repeating subprogram — hole patterns, repeated features, and code reuse.',
   f'''<h1>Subprograms (M98/M99)</h1>
<p class="cp-lead">Repeat a hole pattern 10 times without writing it 10 times. Subprograms are your first step toward automation.</p>
{m("Key","Mill & Lathe")}
{obj(["Main program vs subprogram","M98 call and M99 return","State contracts when calling subs","Repeat counters"])}
<h2>Concept</h2>
<p>A <strong>subprogram</strong> is a separate O-number program called from the main program with M98 Pxxxx. It executes, then M99 returns to the caller. Use it for repeated features: hole patterns, pocket milling, drilling rows.</p>
<h2>Why It Matters</h2>
<p>Drilling a 4×3 hole grid: without subs, 12 coordinate blocks. With a sub that drills one hole pattern and returns, the main program calls it 4 times — changing Y each row. If the hole spacing changes, you edit one place.</p>
<h2>How</h2>
{code('<span class="cp-comment">(Main O2901)</span>\nG90 G54 G00 X0 Y0 S1500 M03\nG43 H01 Z50.\nM98 P0201 L4   <span class="cp-comment">(call sub 4 times)</span>\nG80 Z50.\nM30\n\n<span class="cp-comment">(Sub O0201 — one row of 3 holes)</span>\nG91 G81 X20. Y0 Z-15. R5. F100. L3\nG80\nG90\nM99')}
<p>The sub moves X+20 three times (row), then returns. Main calls it 4 times — each call moves to the next Y row. G90/G91 inside the sub is explicit and safe.</p>
<h2>Common Mistakes</h2>
<ul><li>Modal state leaking between main and sub — always set G90/G91 explicitly in both.</li><li>Sub not returning to start position — next call starts from wrong place.</li><li>Forgetting G80 in the sub.</li></ul>
{prac([
("What does M98 P0201 L4 do?", "Calls subprogram O0201 four times. Each call returns with M99."),
("Why set G91 in the sub?", "The sub moves incrementally (X+20 per hole) regardless of main program G90/G91 state.")])}
{src(["Haas Operator Manual — Subprograms.","M98/M99 are near-universal FANUC-style."])}''',
   prev=("28-milling-project","Milling Project"),
   nxt=("30-reference","Quick Reference"))

# 30 Reference
pg('30-reference', "CNC Programming Quick Reference",
   "One-page lookup: common G-codes, M-codes, addresses, and modal groups.",
   f'''<h1>CNC Programming Quick Reference</h1>
<p class="cp-lead">Fast lookup when you are at the machine and need to confirm a code.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Common G-codes by function","Common M-codes","Addresses and their meaning","Modal groups at a glance"])}
<h2>G-Codes</h2>
<div class="cp-table-wrap"><table>
<tr><th>Code</th><th>Function</th><th>Modal?</th></tr>
<tr><td>G00</td><td>Rapid positioning</td><td>Yes</td></tr>
<tr><td>G01</td><td>Linear feed</td><td>Yes</td></tr>
<tr><td>G02</td><td>CW arc</td><td>Yes</td></tr>
<tr><td>G03</td><td>CCW arc</td><td>Yes</td></tr>
<tr><td>G04</td><td>Dwell</td><td>No</td></tr>
<tr><td>G17/G18/G19</td><td>XY / XZ / YZ plane</td><td>Yes</td></tr>
<tr><td>G20/G21</td><td>Inch / mm</td><td>Yes</td></tr>
<tr><td>G28</td><td>Return home</td><td>No</td></tr>
<tr><td>G40</td><td>Cutter comp off</td><td>Yes</td></tr>
<tr><td>G41/G42</td><td>Cutter comp left/right</td><td>Yes</td></tr>
<tr><td>G43/G49</td><td>Tool length on/off</td><td>Yes</td></tr>
<tr><td>G54–G59</td><td>Work offsets</td><td>Yes</td></tr>
<tr><td>G70</td><td>Finish pass (lathe)</td><td>—</td></tr>
<tr><td>G71</td><td>Stock removal (lathe)</td><td>—</td></tr>
<tr><td>G76</td><td>Threading cycle (lathe)</td><td>—</td></tr>
<tr><td>G80</td><td>Cancel drill cycle</td><td>Yes</td></tr>
<tr><td>G81</td><td>Drill</td><td>Yes</td></tr>
<tr><td>G82</td><td>Drill + dwell</td><td>Yes</td></tr>
<tr><td>G83</td><td>Peck drill</td><td>Yes</td></tr>
<tr><td>G84</td><td>Tapping</td><td>Yes</td></tr>
<tr><td>G85</td><td>Bore</td><td>Yes</td></tr>
<tr><td>G90/G91</td><td>Absolute / incremental</td><td>Yes</td></tr>
<tr><td>G94/G95</td><td>Feed/min / feed/rev</td><td>Yes</td></tr>
<tr><td>G96/G97</td><td>CSS / constant RPM (lathe)</td><td>Yes</td></tr>
<tr><td>G98/G99</td><td>Retract to init / R plane</td><td>Yes</td></tr>
</table></div>
<h2>M-Codes</h2>
<div class="cp-table-wrap"><table>
<tr><th>Code</th><th>Function</th></tr>
<tr><td>M00</td><td>Program stop</td></tr>
<tr><td>M01</td><td>Optional stop</td></tr>
<tr><td>M03/M04</td><td>Spindle CW / CCW</td></tr>
<tr><td>M05</td><td>Spindle stop</td></tr>
<tr><td>M06</td><td>Tool change</td></tr>
<tr><td>M08/M09</td><td>Coolant on/off</td></tr>
<tr><td>M30</td><td>Program end</td></tr>
<tr><td>M98/M99</td><td>Call sub / return</td></tr>
</table></div>
<h2>Addresses</h2>
<div class="cp-table-wrap"><table>
<tr><th>Addr</th><th>Meaning</th></tr>
<tr><td>O</td><td>Program number</td></tr>
<tr><td>N</td><td>Block sequence number</td></tr>
<tr><td>X/Y/Z</td><td>Coordinates</td></tr>
<tr><td>I/J/K</td><td>Arc center (incremental)</td></tr>
<tr><td>R</td><td>Radius or R-plane</td></tr>
<tr><td>S</td><td>Spindle RPM</td></tr>
<tr><td>T</td><td>Tool number</td></tr>
<tr><td>H/D</td><td>Tool length / radius offset number</td></tr>
<tr><td>F</td><td>Feed rate</td></tr>
<tr><td>P/Q</td><td>Subprogram number / profile blocks</td></tr>
</table></div>
{src(["Verify against your machine manual.","Haas, FANUC, Siemens documentation."])}''',
   prev=("29-subprograms","Subprograms"),
   nxt=("31-learning-path","Learning Path"))

# 31 Learning Path
pg('31-learning-path', "CNC Programming Learning Path",
   "Recommended order from zero to capable: foundations, motion, offsets, applications, projects.",
   f'''<h1>CNC Programming Learning Path</h1>
<p class="cp-lead">Follow this order. Do not skip ahead — each chapter builds on the previous one.</p>
{m("Beginner","Mill & Lathe")}
<h2>Stage 1: Foundations</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/01-getting-started/what-is-cnc-programming/">What Is CNC Programming?</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/02-machine-fundamentals/">Machine Fundamentals</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/03-coordinate-systems/">Coordinate Systems</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/08-programming-math/">Practical Math</a></li></ol>
<h2>Stage 2: Language</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/04-program-structure/">Program Structure</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/05-gcode-fundamentals/">G-Code Fundamentals</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/06-modal-codes/">Modal Codes</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/07-plane-units/">Planes &amp; Units</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/09-mcode-fundamentals/">M-Codes</a></li></ol>
<h2>Stage 3: Motion &amp; Setup</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/10-spindle-feed/">Spindle &amp; Feed</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/13-work-offsets/">Work Offsets</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/12-tool-offsets/">Tool Offsets</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/14-linear-interpolation/">Rapid &amp; Linear</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/15-circular-interpolation/">Circular Interpolation</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/16-cutter-compensation/">Cutter Compensation</a></li></ol>
<h2>Stage 4: Applications</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/17-drilling-cycles/">Drilling Cycles</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/18-canned-cycles/">Canned Cycles</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/19-turning-fundamentals/">Turning Coordinates</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/20-turning-cycles/">Turning Cycles</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/22-threading/">Threading</a></li></ol>
<h2>Stage 5: Projects &amp; Safety</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/23-program-safety/">Program Safety</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/24-verification/">Verification</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/28-milling-project/">Milling Project</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/27-turning-project/">Turning Project</a></li></ol>
<h2>Stage 6: Beyond Hand Coding</h2>
<ol><li><a href="/cnc-manufacturing-engineering/cnc-programming/35-cad-cam-postprocessing/">CAD/CAM &amp; Post</a></li>
<li><a href="/cnc-manufacturing-engineering/cnc-programming/36-macro-foundations/">Macro Foundations</a></li></ol>
{prac([
("Where should a complete beginner start?", "01 What Is CNC Programming, then follow Stage 1 through 5 in order."),
("I already know G00/G01. Where to jump?", "Stage 3: offsets and motion. Review Stage 2 quickly.")])}
{src(["Learning path designed for first-time CNC programmers."])}''',
   prev=("30-reference","Quick Reference"),
   nxt=("32-drawings-process-planning","Drawings & Planning"))

print("Pages 27-31 done.")

# 32 Drawings & Process Planning
pg('32-drawings-process-planning', 'From Drawing to Process Plan',
   'Read the drawing, choose datums, sequence operations, select tools — before writing a single line of code.',
   f'''<h1>From Drawing to Process Plan</h1>
<p class="cp-lead">Programming starts on paper, not at the keyboard. A good process plan prevents most mistakes.</p>
{m("Key","Mill & Lathe")}
{obj(["Reading a machined drawing","Choosing datum strategy","Sequencing rough → finish → holes","Selecting tools and setups"])}
<h2>Concept</h2>
<p>Before coding, answer: what does the part look like? What are the critical datums? Which faces get machined first? Roughing removes most material; finishing holds tolerance. Holes come after milling (they reference milled faces). Setups must minimize re-fixturing.</p>
<h2>Why It Matters</h2>
<p>A part machined from the wrong datum will fail inspection even if every coordinate is correct. Drilling before milling means holes reference raw stock, not finished faces. Process planning is where dimensional control is won or lost.</p>
<h2>How</h2>
<ol><li><strong>Read the drawing:</strong> identify datums, critical dimensions, tolerances, surface finish.</li>
<li><strong>Choose datum:</strong> machine the reference faces first; set work zero on the datum.</li>
<li><strong>Sequence:</strong> face → rough profile → finish profile → drill/tap → deburr.</li>
<li><strong>Tools:</strong> pick insert grade for material, tool diameter for corner radius, number of teeth for MRR.</li>
<li><strong>Setups:</strong> can it be done in one vise? Do you need a second operation?</li></ol>
<h2>Example</h2>
<p>An aluminum bracket: mill the back face (datum A), flip and machine the front profile and holes. Holes reference the milled face, not the raw stock. This ensures hole-to-face relationship within tolerance.</p>
<h2>Common Mistakes</h2>
<ul><li>Drilling before milling — holes reference raw stock.</li><li>Choosing work zero on a non-datum edge.</li><li>Squeezing a second setup's features into setup 1 without checking tool access.</li></ul>
{prac([
("Why face the part first?", "The face becomes the Z datum. All other Z dimensions reference this flat surface."),
("Roughing before finishing — why?", "Roughing removes bulk stock fast. Finishing takes light cuts at better surface speed to hold tolerance.")])}
{src(["Machinery's Handbook — Process Planning.","Shop process planning practice."])}''',
   prev=("31-learning-path","Learning Path"),
   nxt=("33-milling-strategies","Milling Strategies"))

# 33 Milling Strategies
pg('33-milling-strategies', 'Facing, Slots, and Pockets',
   'Climb vs conventional milling, stepover, lead-in/out, and chip evacuation strategy.',
   f'''<h1>Facing, Slots, and Pockets</h1>
<p class="cp-lead">Tool path strategy affects tool life, surface finish, and cycle time as much as speeds and feeds.</p>
{m("Key","Mill")}
{obj(["Climb vs conventional milling","Radial stepover and axial depth","Lead-in/out for contour cuts","Chip evacuation in slots and pockets"])}
<h2>Concept</h2>
<p><strong>Climb (up) milling:</strong> the cutter feeds in the same direction as spindle rotation. Chip starts thick, ends thin — better finish, less rubbing, preferred on modern machines.</p>
<p><strong>Conventional (down) milling:</strong> cutter feeds against rotation. Chip starts thin, ends thick — work hardening, tool wear. Old machines with backlash require it; modern CNCs do not.</p>
<h2>Why It Matters</h2>
<p>Climb milling in aluminum doubles tool life and improves finish. Conventional milling on a worn machine causes chatter and work-hardening. Stepover (radial engagement) affects MRR: 50% stepover balances load vs time.</p>
<h2>How</h2>
<p><strong>Facing:</strong> start off the edge, feed across, overlap 5-10 mm past the far side. <strong>Slots:</strong> plunge feed (slow) then lateral feed. <strong>Pockets:</strong> start center, spiral outward, climb mill the walls.</p>
<p><strong>Lead-in/out:</strong> approach the contour on a straight or arc lead-in greater than tool radius. Never start cutting on the part edge directly — marks the surface.</p>
<h2>Example</h2>
<p>10 mm end mill, 50% radial stepover = 5 mm per pass. For a 60 mm pocket, 12 passes. Climb direction: watch which way the spindle spins and feed accordingly.</p>
<h2>Common Mistakes</h2>
<ul><li>Using conventional milling when the machine can climb.</li><li>100% stepover — overloading the tool.</li><li>No lead-in — tool marks at the contour start.</li></ul>
{prac([
("Climb vs conventional — which to use?", "Climb on modern CNC. Conventional only if the machine has significant backlash."),
("Typical radial stepover for end mill?", "30-70% of cutter diameter. 50% is a balanced starting point.")])}
{src(["Sandvik Coromant — Milling Strategies."])}''',
   prev=("32-drawings-process-planning","Drawings & Planning"),
   nxt=("34-tapping-thread-milling","Tapping & Thread Milling"))

# 34 Tapping & Thread Milling
pg('34-tapping-thread-milling', 'Tapping and Thread Milling',
   'G84 tapping cycle, tap drill size, pitch/lead, and when to thread-mill instead of tap.',
   f'''<h1>Tapping and Thread Milling</h1>
<p class="cp-lead">Tapping is the highest-stakes hole operation — a broken tap in a finished part is scrap.</p>
{m("Key","Mill")}
{obj(["G84 rigid tapping cycle","Tap drill size and pitch","Rigid tap vs floating tap holder","Thread milling basics"])}
<h2>Concept</h2>
<p><strong>Tapping</strong> cuts internal threads with a tap. G84 synchronizes spindle RPM with feed so the tap advances exactly one pitch per revolution. <strong>Rigid tapping</strong> uses spindle encoder sync (no floating holder). <strong>Thread milling</strong> uses a helical-interpolating cutter for large or hard-to-reach threads.</p>
<h2>Why It Matters</h2>
<p>Feed must equal pitch × RPM. For M10×1.5 at 500 RPM: feed = 1.5 × 500 = 750 mm/min. Wrong feed = stripped threads or broken tap. Tap drill size = major diameter − pitch (approximate): M10×1.5 → 8.5 mm drill.</p>
<h2>How</h2>
{code('G84 X50. Y30. Z-25. R5. F750.  <span class="cp-comment">(M10×1.5, 500 rpm, F=750)</span>')}
<p>On rigid-tap machines, G84 reverses the spindle and retracts. On non-rigid machines, use a floating tap holder and confirm the feed sync.</p>
<h2>Example</h2>
<p>M8×1.25 through hole in steel: tap drill = 6.8 mm. RPM = 600. Feed = 1.25 × 600 = 750 mm/min. G84 at Z-20, R5.</p>
<h2>Common Mistakes</h2>
<ul><li>Feed wrong — F must equal pitch × RPM in mm/min.</li><li>Not using rigid tapping when available — floating holder chatter.</li><li>Forgetting that G84 is modal — next X/Y taps too.</li><li>Drilling tap drill too small — tap binds and breaks.</li></ul>
{prac([
("M10×1.5 at 600 RPM. Feed?", "1.5 × 600 = 900 mm/min."),
("M10×1.5 tap drill size?", "Approx 8.5 mm (major − pitch).")])}
{src(["Sandvik Coromant — Tapping.","Haas Manual — G84."])}''',
   prev=("33-milling-strategies","Milling Strategies"),
   nxt=("35-cad-cam-postprocessing","CAD/CAM & Post"))

# 35 CAD/CAM & Post
pg('35-cad-cam-postprocessing', 'CAD/CAM and Post-Processing',
   'From 3D model to NC code: CAM toolpaths, post-processors, and why you still verify the output.',
   f'''<h1>CAD/CAM and Post-Processing</h1>
<p class="cp-lead">CAM handles complex geometry — but the post-processor is where machine-specific safety lives.</p>
{m("Key","Mill & Lathe")}
{obj(["CAD model → CAM toolpath → NC code","Post-processor role","Why verify post output","Simulation limitations"])}
<h2>Concept</h2>
<p><strong>CAM</strong> (Computer-Aided Manufacturing) software takes a 3D model and generates toolpaths: pocketing, contouring, drilling. The <strong>post-processor</strong> translates generic toolpath data into machine-specific G-code for your controller (Haas, FANUC, Siemens).</p>
<h2>Why It Matters</h2>
<p>A generic post may output G-code that looks correct but uses the wrong cycle format, missing safe Z retracts, or incorrect tool change syntax on your machine. CAM simulation shows the tool path in the abstract; it does not know your vise, tool holder, or machine envelope. You must verify the actual NC code.</p>
<h2>How</h2>
<ol><li>Import the CAD model.</li><li>Define stock, fixtures, tools.</li><li>Generate toolpaths (roughing, finishing, drilling).</li><li>Post-process with the correct post for your machine.</li><li>Review the G-code — check startup block, tool changes, Z heights, cycles.</li><li>Dry run on the machine before cutting.</li></ol>
<h2>Example</h2>
<p>Part imported into CAM. Roughing toolpath generated. Post for Haas VF-2 outputs G21 G17 G90 ... T01 M06 ... G54 ... But the post forgets G43 Hxx on some tools. Review catches it — add H number manually or fix the post.</p>
<h2>Common Mistakes</h2>
<ul><li>Using the wrong post (generic instead of machine-specific).</li><li>Trusting CAM simulation over machine dry run.</li><li>Not checking that tool numbers match the physical turret/magazine.</li></ul>
{prac([
("What does a post-processor do?", "Translates generic CAM toolpath into machine-specific G-code syntax for your controller."),
("Why review CAM output?", "Posts make mistakes; CAM simulation omits real fixtures. Read the actual G-code.")])}
{src(["Mastercam, Fusion 360, ESPRIT documentation.","Post-processor verification is a shop-floor best practice."])}''',
   prev=("34-tapping-thread-milling","Tapping & Thread Milling"),
   nxt=("36-macro-foundations","Macro Foundations"))

# 36 Macro Foundations
pg('36-macro-foundations', 'Macro Programming Foundations',
   'Variables, logic, and loops — parameterize holes, bolt circles, and repeated features.',
   f'''<h1>Macro Programming Foundations</h1>
<p class="cp-lead">Macros let the controller do math and make decisions — no CAM needed for parametric parts.</p>
{m("Key","Mill & Lathe")}
{obj(["What macros add to G-code","Variables (#1–#33 local, #100+ common)","IF/GOTO and WHILE loops","Bolt circle example"])}
<h2>Concept</h2>
<p><strong>Macros</strong> (parametric programming) use variables, arithmetic, and logic inside G-code. Instead of hardcoding 12 bolt circle holes, write a loop that calculates each one. Change the radius or hole count — the program recalculates.</p>
<h2>Why It Matters</h2>
<p>A bolt circle with N holes at radius R: without macro, trig per hole. With macro: initialize angle, loop N times, increment angle. One program handles any hole count. This is powerful for families of parts.</p>
<h2>How</h2>
{code('#1=50.          <span class="cp-comment">(bolt circle radius)</span>\n#2=6            <span class="cp-comment">(number of holes)</span>\n#3=0            <span class="cp-comment">(angle counter)</span>\n#4=360/#2       <span class="cp-comment">(angle step)</span>\nO1000\n#5=#1*COS[#3]\n#6=#1*SIN[#3]\nG81 X#5 Y#6 Z-15. R5. F100.\n#3=#3+#4\nIF[#3 LT 360] GOTO1000\nG80')}
<p>#5 and #6 recalculate each iteration. The loop runs until angle reaches 360°. Controller syntax varies (FANUC uses #, Siemens uses R parameters).</p>
<h2>Common Mistakes</h2>
<ul><li>Infinite loop (forgot to increment the counter).</li><li>Using degrees vs radians incorrectly (most controllers use degrees).</li><li>Not understanding controller-specific variable ranges.</li></ul>
{prac([
("6 holes on R=50. First hole angle 0°, next angle?", "60° (360/6). X=50, Y=0, then X=25, Y=43.3.")])}
{src(["FANUC Macro B Guide.","Haas Macro documentation."])}''',
   prev=("35-cad-cam-postprocessing","CAD/CAM & Post"),
   nxt=("37-multiaxis-probing-overview","Multi-axis & Probing"))

# 37 Multi-axis & Probing
pg('37-multiaxis-probing-overview', 'Rotary Axes and Touch Probes',
   '4th axis, 3+2 positioning, and touch probing — an overview of what comes after 3-axis.',
   f'''<h1>Rotary Axes and Touch Probes</h1>
<p class="cp-lead">Beyond 3-axis: rotary axes position parts for side features, and probes automate setup and inspection.</p>
{m("Beginner","Mill")}
{obj(["A/B/C rotary axes and 4th axis","3+2 positioning vs simultaneous 5-axis","Touch probe basics","Probe cycles for setup"])}
<h2>Concept</h2>
<p>A <strong>4th axis</strong> (rotary A or C) indexes the part to machine side faces without re-fixturing. <strong>3+2</strong> locks two rotary axes to position the part at an angle, then mills in 3 axes. <strong>Simultaneous 5-axis</strong> moves all axes together for complex surfaces.</p>
<p>A <strong>touch probe</strong> is a precision sensor that touches the part and records positions — automating edge finding, bore location, and in-cycle inspection.</p>
<h2>Why It Matters</h2>
<p>4th axis eliminates a second setup for side holes. Probing cuts setup time and catches offset errors automatically. Both are intermediate topics — master 3-axis first.</p>
<h2>How</h2>
<p>4th axis: G00 A90. rotates the part 90°. Probe: M06 probe, G38.2 touch cycle records surface position into work offset.</p>
<h2>Common Mistakes</h2>
<ul><li>Not accounting for rotary center in work offsets.</li><li>Probing without a probe calibration routine.</li></ul>
{prac([
("3+2 vs simultaneous 5-axis?", "3+2 locks angles and mills in 3 axes. Simultaneous interpolates all 5 axes during cut.")])}
{src(["Haas 4th Axis Manual.","Renishaw probing documentation."])}''',
   prev=("36-macro-foundations","Macro Foundations"),
   nxt=("38-process-optimization","Process Optimization"))

# 38 Process Optimization
pg('38-process-optimization', 'Cycle Time and Quality',
   'Where cycle time goes, how to improve it without wrecking parts, and process capability basics.',
   f'''<h1>Cycle Time and Quality</h1>
<p class="cp-lead">A correct program is the start. A fast, repeatable program is the goal.</p>
{m("Key","Mill & Lathe")}
{obj(["Where time goes in a cycle","Rapid vs cutting time","Tool change and pallet time","Process capability Cp/Ck concept"])}
<h2>Concept</h2>
<p>Cycle time = rapid moves + cutting feeds + tool changes + spindle acceleration + probing. Reducing air cuts (rapid repositioning) often saves more than speeding feeds. A good program balances: safe approach, minimal air cuts, optimized chip load, and repeatable offsets.</p>
<h2>Why It Matters</h2>
<p>Running 20% faster may break tools or ruin finish. Cutting air 20% shorter is free. Tool changes and spindle accel/decel are often 30%+ of cycle time on small parts.</p>
<h2>How</h2>
<ul><li>Minimize R plane height — just enough clearance.</li><li>Use G99 (retract to R) between holes, not G98.</li><li>Combine operations where possible.</li><li>Optimize tool paths for climb milling (better tool life = less downtime).</li><li>Stable offsets = fewer inspection stops.</li></ul>
<h2>Common Mistakes</h2>
<ul><li>Cranking feed too high to save seconds — tool wears faster, net time worse.</li><li>Ignoring tool change time on multiple-tool programs.</li></ul>
{prac([
("Where is cycle time on a 4-hole drill program?", "Mostly rapid repositioning between holes. G99 saves time vs G98."),
("Why does climb milling reduce total cost?", "Longer tool life = less tool change and insert cost, despite similar cutting time.")])}
{src(["Sandvik Coromant — Productivity.","Process capability: Cp/Cpk references in Manufacturing Quality."])}''',
   prev=("37-multiaxis-probing-overview","Multi-axis & Probing"),
   nxt=("39-exercises-assessment","Exercises"))

# 39 Exercises & Assessment
pg('39-exercises-assessment', 'Practice Exercises and Self-Assessment',
   'Test your CNC programming knowledge: code reading, error finding, and written programs.',
   f'''<h1>Practice Exercises and Self-Assessment</h1>
<p class="cp-lead">Reading about CNC is not enough. These exercises check whether you can actually do it.</p>
{m("Key","Mill & Lathe")}
{obj(["Code reading comprehension","Finding intentional errors","Writing simple programs","Self-assessment checklist"])}
<h2>Code Reading</h2>
<p>Read this block and answer:</p>
{code('G90 G54 G00 X20. Y20.\nG01 Z-2. F100.\nG01 X80. F300.\nG00 Z5.')}
<p><strong>Q:</strong> What does the tool do?<br>
<strong>A:</strong> Rapid to X20 Y20 above part → feed down to Z-2 at 100 mm/min → feed to X80 at 300 mm/min → rapid up to Z5.</p>
<h2>Find the Error</h2>
<p>This program has a bug. What is it?</p>
{code('G81 G99 X10. Y10. Z-10. R5. F100.\nX50. Y30.\nG00 X0 Y0\nG00 Z50.')}
<p><strong>A:</strong> Missing G80 before G00 X0 Y0. The drilling cycle is still active — the G00 X0 Y0 will execute a drill at X0 Y0. Insert G80 after the last hole.</p>
<h2>Write the Program</h2>
<p>Drill 3 holes at (10,10), (30,10), (50,10) through a 10 mm plate. R plane 5 mm, Z depth -12. Feed 100. Show the G-code.</p>
<details><summary>Sample answer</summary>
{code('G90 G54 G00 X10. Y10. S1500 M03\nG43 H01 Z50. M08\nG99 G81 Z-12. R5. F100.\nX30. Y10.\nX50. Y10.\nG80\nG00 Z50. M09\nM05\nM30')}
</details>
<h2>Self-Assessment Checklist</h2>
<p>Before calling yourself competent:</p>
<ul><li>I can read a G-code block and predict tool motion.</li>
<li>I know G90 vs G91 without looking it up.</li>
<li>I know why G40 G49 G80 are in startup blocks.</li>
<li>I can set up G54 work offset and H tool offset.</li>
<li>I can write a simple drilling program from a drawing.</li>
<li>I know when to use G98 vs G99.</li>
<li>I verify programs with dry run, not just backplot.</li></ul>
{src(["Exercises are self-paced. Verify answers against your machine's manual."])}''',
   prev=("38-process-optimization","Process Optimization"),
   nxt=("40-glossary-sources","Glossary & Sources"))

# 40 Glossary & Sources
pg('40-glossary-sources', 'Glossary and Sources',
   'Key CNC terms defined, and the authoritative references this course relies on.',
   f'''<h1>Glossary and Sources</h1>
<p class="cp-lead">Definitions you will encounter on the shop floor, and where to verify facts yourself.</p>
{m("Beginner","Mill & Lathe")}
<h2>Glossary</h2>
<div class="cp-table-wrap"><table>
<tr><th>Term</th><th>Definition</th></tr>
<tr><td>CNC</td><td>Computer Numerical Control</td></tr>
<tr><td>G-code</td><td>Preparatory function codes that control motion</td></tr>
<tr><td>M-code</td><td>Miscellaneous functions: spindle, coolant, stop</td></tr>
<tr><td>RPM</td><td>Revolutions per minute (spindle speed)</td></tr>
<tr><td>SFM / m/min</td><td>Surface cutting speed</td></tr>
<tr><td>Feed rate</td><td>Tool travel speed (mm/min or mm/rev)</td></tr>
<tr><td>Work offset</td><td>G54–G59: part position relative to machine home</td></tr>
<tr><td>Tool length offset</td><td>G43 H: stored tool length applied to Z moves</td></tr>
<tr><td>Cutter comp</td><td>G41/G42: automatic radius offset from programmed contour</td></tr>
<tr><td>Canned cycle</td><td>G80–G89: pre-programmed drill/bore sequences</td></tr>
<tr><td>Modal</td><td>A code that stays active until canceled</td></tr>
<tr><td>Peck drilling</td><td>G83: intermittent feed with retract for chip clearing</td></tr>
<tr><td>CSS</td><td>Constant Surface Speed (G96 on lathe)</td></tr>
<tr><td>MRR</td><td>Material Removal Rate (mm&sup3;/min)</td></tr>
<tr><td>Setup</td><td>Fixturing, offsets, and tooling before running</td></tr>
<tr><td>First article</td><td>First produced part, fully inspected</td></tr>
</table></div>
<h2>Sources</h2>
<p>This course draws on:</p>
<ul><li><strong>Haas Automation</strong> — Mill and Lathe Operator's Manuals (haascnc.com)</li>
<li><strong>Sandvik Coromant</strong> — Machining knowledge and cutting parameter guides</li>
<li><strong>FANUC</strong> — Series Programming Manuals</li>
<li><strong>Machinery's Handbook</strong> — process planning and threading references</li>
<li>Shop-floor practice and hands-on training</li></ul>
<p>Always verify G-code behavior, cycle definitions, and parameter values against your specific machine manual. This site teaches concepts; your machine is the authority.</p>
{src(["All G-code examples are illustrative. Verify on your machine before production.","Speeds and feeds are starting points, not recommendations."])}''',
   prev=("39-exercises-assessment","Exercises"),
   nxt=None)

print("Pages 32-40 done. ALL PAGES COMPLETE.")
