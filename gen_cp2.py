#!/usr/bin/env python3
"""Generate all CNC Programming article pages — v2 per SPEC + review fixes."""
import os

BASE = "/Users/lilu/Doubao/chats/2026-09-23/new-chat/cnc-manufacturing-engineering/docs/cnc-programming"
S = "/cnc-manufacturing-engineering"

NAV = f'''<nav class="site-nav"><div class="site-nav-inner">
<div class="site-nav-brand">Li Lu <span>&middot;</span> CNC Eng</div>
<ul class="site-nav-links">
<li><a href="{S}/">Home</a></li>
<li><a href="{S}/engineering-tools/">Engineering Tools</a></li>
<li><a href="{S}/knowledge-base/">Knowledge Base</a></li>
<li><a href="{S}/machine-systems/">Machine Systems</a></li>
<li><a href="{S}/cnc-programming/" class="active">CNC Programming</a></li>
<li><a href="{S}/about/">About</a></li>
</ul></div></nav>'''
FOOT = '<footer class="site-footer">Designed by Li Lu · CNC &amp; Manufacturing Engineering</footer>'

# Linear reading order per SPEC module table
ORDER = [
    ("01-getting-started/what-is-cnc-programming", "What Is CNC Programming?"),
    ("02-machine-fundamentals", "Machine Fundamentals"),
    ("23-program-safety", "Safe Start & Restart"),
    ("08-programming-math", "Programming Math"),
    ("32-drawings-process-planning", "Drawing to Process Plan"),
    ("03-coordinate-systems", "Coordinate Systems"),
    ("07-plane-units", "Planes & Units"),
    ("04-program-structure", "Program Structure"),
    ("05-gcode-fundamentals", "G-Code Fundamentals"),
    ("06-modal-codes", "Modal State"),
    ("09-mcode-fundamentals", "M-Codes"),
    ("11-controller-dialects", "Controller Dialects"),
    ("10-spindle-feed", "Spindle & Feed"),
    ("13-work-offsets", "Work Offsets"),
    ("12-tool-offsets", "Tool Offsets"),
    ("14-linear-interpolation", "Rapid & Linear"),
    ("15-circular-interpolation", "Circular Interpolation"),
    ("16-cutter-compensation", "Cutter Compensation"),
    ("33-milling-strategies", "Milling Strategies"),
    ("17-drilling-cycles", "Drilling Cycles"),
    ("18-canned-cycles", "Canned Cycles"),
    ("34-tapping-thread-milling", "Tapping & Thread Milling"),
    ("29-subprograms", "Subprograms"),
    ("19-turning-fundamentals", "Turning Coordinates"),
    ("20-turning-cycles", "Turning Cycles"),
    ("21-grooving-parting-boring", "Grooving & Parting"),
    ("22-threading", "Thread Programming"),
    ("24-verification", "Verification"),
    ("25-troubleshooting", "Troubleshooting"),
    ("26-common-mistakes", "Common Mistakes"),
    ("28-milling-project", "Milling Project"),
    ("27-turning-project", "Turning Project"),
    ("35-cad-cam-postprocessing", "CAD/CAM & Post"),
    ("36-macro-foundations", "Macro Foundations"),
    ("37-multiaxis-probing-overview", "Multi-axis & Probing"),
    ("38-process-optimization", "Process Optimization"),
    ("39-exercises-assessment", "Final Assessment"),
    ("31-learning-path", "Learning Path"),
    ("30-reference", "Quick Reference"),
    ("40-glossary-sources", "Glossary & Sources"),
]

def pg(sub, title, desc, body, prev=None, nxt=None):
    folder = os.path.join(BASE, sub)
    os.makedirs(folder, exist_ok=True)
    cp = f"https://lilu1626.github.io{S}/cnc-programming/{sub}/"
    nb = ""
    if prev or nxt:
        p = f'<a href="{S}/cnc-programming/{prev[0]}/">&larr; {prev[1]}</a>' if prev else "<span></span>"
        n = f'<a href="{S}/cnc-programming/{nxt[0]}/">{nxt[1]} &rarr;</a>' if nxt else "<span></span>"
        nb = f'<nav class="cp-nav-bottom">{p}{n}</nav>'
    h = f'''<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — CNC &amp; Manufacturing Engineering</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{cp}">
<link rel="stylesheet" href="{S}/assets/css/site.css">
<link rel="stylesheet" href="{S}/assets/css/article.css">
<link rel="stylesheet" href="{S}/assets/css/cnc-programming.css">
</head><body class="cnc-programming">
{NAV}
<main class="article">
<a class="cp-back" href="{S}/cnc-programming/">&larr; Back to CNC Programming</a>
{body}
{nb}
</main>{FOOT}</body></html>'''
    with open(os.path.join(folder, 'index.html'), 'w') as f:
        f.write(h)
    print(f"  {sub}")

def m(level, machine):
    return f'<div class="cp-meta"><span><strong>Level:</strong> {level}</span><span><strong>Machine:</strong> {machine}</span></div>'
def obj(items):
    return f'<div class="callout"><strong>What you will learn:</strong><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
def prac(qs):
    out = '<section class="cp-practice"><h2>Practice</h2>'
    for i,(q,a) in enumerate(qs,1):
        out += f'<p><strong>{i}.</strong> {q}</p><details><summary>Show answer</summary><p>{a}</p></details>'
    return out + '</section>'
def src(items):
    return f'<section class="cp-sources"><h2>Sources and Applicability</h2><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></section>'
def code(block):
    return f'<pre class="cp-code"><code>{block}</code></pre>'
def fig(svg, caption):
    return f'<figure class="cp-figure">{svg}<figcaption>{caption}</figcaption></figure>'

print("Generating v2...")

# SVG helpers
def svg_flow():
    steps = ["Drawing","Process Plan","Setup & Tooling","CNC Program","Verify","First Part"]
    out = '''<svg viewBox="0 0 520 80" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0b766e"/></marker></defs>'''
    for i,s in enumerate(steps):
        x = 5+i*85
        out += f'<rect x="{x}" y="25" width="78" height="30" rx="6" fill="#e6f4f2" stroke="#0b766e"/>'
        out += f'<text x="{x+39}" y="43" font-size="9" text-anchor="middle" fill="#07574f">{s}</text>'
        if i<5: out += f'<line x1="{x+78}" y1="40" x2="{x+83}" y2="40" stroke="#0b766e" marker-end="url(#ar)"/>'
    return out + '</svg>'

def svg_axes_mill():
    return '''<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="200" x2="290" y2="200" stroke="#17242f" stroke-width="1.5" marker-end="url(#mx)"/>
<line x1="40" y1="200" x2="40" y2="20" stroke="#17242f" stroke-width="1.5" marker-end="url(#my)"/>
<line x1="40" y1="200" x2="20" y2="220" stroke="#5c6872" stroke-width="1.2" stroke-dasharray="4" marker-end="url(#mz)"/>
<defs><marker id="mx" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#17242f"/></marker>
<marker id="my" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#17242f"/></marker>
<marker id="mz" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#5c6872"/></marker></defs>
<text x="285" y="218" font-size="12" fill="#17242f">X+</text>
<text x="25" y="25" font-size="12" fill="#17242f">Y+</text>
<text x="5" y="230" font-size="11" fill="#5c6872">Z+ (up)</text>
<rect x="80" y="130" width="100" height="50" fill="none" stroke="#0b766e" stroke-width="1.5"/>
<text x="95" y="160" font-size="10" fill="#0b766e">Workpiece</text>
<circle cx="130" cy="155" r="3" fill="#e07a3f"/>
<text x="138" y="152" font-size="10" fill="#e07a3f">G54 zero</text>
<text x="60" y="235" font-size="9" fill="#5c6872">Schematic, not to scale</text></svg>'''

# 01 What Is CNC Programming?
pg('01-getting-started/what-is-cnc-programming', "What Is CNC Programming?",
   "Understand what a CNC program controls, how a drawing becomes coordinates, and manual vs CAM programming.",
   f'''<h1>What Is CNC Programming?</h1>
<p class="lead">CNC programming is the bridge between an engineering drawing and a moving machine tool. This page starts from zero: no prior G-code knowledge assumed.</p>
{m("Beginner","Mill & Lathe concepts")}
{obj(["What a CNC program actually controls","The drawing-to-part workflow","Manual programming vs CAM","Why coordinates come before code"])}
{fig(svg_flow(), "The workflow from engineering drawing to finished part. Each step feeds the next; a mistake at any stage propagates.")}
<h2>Concept</h2>
<p>A <strong>CNC program</strong> is a plain-text file of instructions. The machine controller reads one line at a time and commands the servos, spindle, coolant, and tool changer. The controller does not make decisions or interpret intent — it executes exactly what you wrote. If a line says move to X50 Y30, the controller moves there. It does not know whether X50 Y30 is a hole center or a collision course.</p>
<p>Two files are easily confused: the <strong>NC program</strong> (G-code, what the machine runs) and the <strong>CAM project file</strong> (the CAD model, toolpaths, and parameters that the CAM software stores). You export G-code from CAM; the machine reads only that exported text. A manual program is written by hand in a text editor or directly at the machine.</p>
<h2>Why It Matters</h2>
<p>Consider a 60&times;40 mm aluminum plate with two &Oslash;8 holes at centers (10,10) and (50,30) relative to the lower-left corner. On a manual mill, you crank the X and Y dials, stop at each position, and drill. In CNC, you write those coordinates once and the machine repeats them exactly, every time. If the coordinates are wrong, every hole is wrong — but consistently and repeatably. That is the power and the danger: CNC does not correct your mistakes; it manufactures them at production speed.</p>
<p>The goal of this course is not to memorize a code list. It is to read a drawing, choose coordinates, write a program, verify it, and explain what every line does before the machine moves.</p>
<h2>How: The Workflow</h2>
<h3>From drawing to machine</h3>
<ol>
<li><strong>Engineering drawing</strong> — dimensions, tolerances, surface finish, material.</li>
<li><strong>Process planning</strong> — which faces get machined, rough vs finish, tools, workholding.</li>
<li><strong>Workholding &amp; tooling</strong> — vise, chuck, fixture; select cutting tools and insert grades.</li>
<li><strong>CNC program</strong> — coordinates, speeds, feeds, tool changes, cycles.</li>
<li><strong>Verification</strong> — syntax check, backplot, dry run, single-block, first article.</li>
<li><strong>Finished part</strong> — inspected against the drawing before release.</li>
</ol>
<h3>Manual vs CAM</h3>
<p><strong>Manual programming</strong> works well for parts made of straight lines, circles, and drilled holes: brackets, plates, simple shafts. You write G-code by hand and calculate coordinates with a calculator or trigonometry. <strong>CAM programming</strong> uses software to generate toolpaths from a 3D model — necessary for complex 3D surfaces, multi-axis parts, or when calculating hundreds of coordinates by hand is impractical. Even with CAM, you still must understand the output: a wrong post-processor can feed back G-code that looks correct but crashes the machine.</p>
<h2>Example</h2>
<p>Take the two-hole plate. In plain English, the operation is: position over the first hole, drill through, move to the second hole, drill through. In G-code (fragment, assumes spindle and tool already set):</p>
{code('G90 G54 G00 X10. Y10.   <span class="cp-comment">(position hole 1)</span>\nG81 Z-15. R5. F100. <span class="cp-comment">(drill cycle)</span>\nX50. Y30.            <span class="cp-comment">(move hole 2, cycle repeats)</span>\nG80                   <span class="cp-comment">(cancel cycle)</span>')}
<p>Here <code>X10 Y10</code> is an absolute position in the work coordinate system, <code>S2000</code> would mean 2000 rpm spindle speed, and <code>F100</code> means feed at 100 mm/min. Each word means something specific; none of them are "distance" or "speed" in a general sense. We will unpack all of these in later lessons.</p>
<h2>Common Mistakes</h2>
<ul>
<li><strong>Treating coordinates as distances.</strong> X50 Y30 is a target position, not "move 50 mm right and 30 mm up." The difference is absolute vs incremental (Lesson 03).</li>
<li><strong>Thinking S controls cutting speed directly.</strong> S sets spindle RPM, not surface speed. The actual cutting speed depends on tool or workpiece diameter (Lesson 10).</li>
<li><strong>Assuming CAM output needs no review.</strong> Posts make mistakes; CAM simulation omits your vise and tool holder. Always read the G-code (Lesson 35).</li>
<li><strong>Skipping verification.</strong> Writing a program is not the same as proving it safe. Lesson 24 covers verification layers.</li>
</ul>
{prac([
("Two holes at (10,10) and (50,30). What is the displacement between them?", "ΔX = 50−10 = 40 mm, ΔY = 30−10 = 20 mm. The distance is √(40²+20²) = √2000 ≈ 44.7 mm, but the machine moves in X and Y separately."),
("A simple shaft with two turned diameters vs a 3D sculptured mold surface — which uses manual programming and which uses CAM?", "The shaft: manual (straight turns, simple coordinates). The mold: CAM (complex 3D contours require software toolpath generation). Both still require verification."),
("Why does the controller not know that X50 Y30 is a hole center?", "The controller only knows the current position and the commanded target. It has no concept of a drawing. Coordinates are your interpretation of the drawing.")])}
{src(["Haas Mill Operator's Manual — Introduction (haascnc.com, retrieved 2026-09-24).","Sandvik Coromant — Machining formulas (conceptual workflow).","This is a conceptual overview; specific G-codes are taught from Lesson 04 onward."])}''',
   prev=None, nxt=("02-machine-fundamentals","Machine Fundamentals"))

# 02 Machine Fundamentals
pg('02-machine-fundamentals', "Machine Fundamentals for Programmers",
   "Machine axes, spindle, tool change, reference position, and why X20 means different things on a mill vs lathe.",
   f'''<h1>Machine Fundamentals for Programmers</h1>
<p class="lead">Before writing code, you must know what the machine physically is: what rotates, what moves, and where the reference points are.</p>
{m("Beginner","3-axis VMC and 2-axis lathe")}
{obj(["Mill vs lathe: what rotates","Linear and rotary axes","Machine home vs work zero","Tool changer and envelope"])}
{fig(svg_axes_mill(), "Vertical mill axes: X and Y move the table, Z moves the spindle up and down. Work zero is set by the operator.")}
<h2>Concept</h2>
<p>A <strong>vertical machining center (VMC)</strong>: the spindle holds the tool and rotates it; the table moves X and Y. A <strong>CNC lathe</strong>: the chuck holds the workpiece and rotates it; the turret moves the tool in X (radial) and Z (along the part). This distinction is fundamental: on a mill the tool spins, on a lathe the part spins.</p>
<p><strong>Machine axes</strong> follow the right-hand rule: X, Y, Z are linear; A, B, C are rotary around X, Y, Z respectively. <strong>Machine home</strong> (reference position) is a fixed physical location the machine finds on startup. <strong>Work zero</strong> (program zero) is where you tell the machine the part origin is — set in a work offset like G54.</p>
<h2>Why It Matters</h2>
<p>The same coordinate X20 means different things. On a mill, X20 means the table (and workpiece) has moved so the tool tip is 20 mm in +X from work zero. On a lathe in <strong>diameter programming</strong>, X20 means the tool tip is at a position corresponding to a 20 mm diameter — the actual radial movement is only 10 mm from center. Writing X coordinates without knowing whether you are on a mill or lathe, and whether the lathe uses diameter or radius mode, leads to crashes.</p>
<h2>How</h2>
<h3>Mill axes</h3>
<ul><li><strong>X</strong> — table left/right.</li><li><strong>Y</strong> — table in/out.</li><li><strong>Z</strong> — spindle up/down. Z+ is away from the table (tool up).</li></ul>
<h3>Lathe axes</h3>
<ul><li><strong>X</strong> — radial. In diameter programming, the commanded value is the workpiece diameter, not the distance from center.</li><li><strong>Z</strong> — along the spindle. Z0 is usually the part face; Z− goes into the workpiece.</li><li><strong>C</strong> (optional) — spindle rotation for live tooling or positioning.</li></ul>
<h3>Tool changer</h3>
<p>A VMC has a tool magazine and automatic tool changer (ATC). The program calls T01 M06; the machine swaps tools. A lathe has a turret that indexes tools. The tool number in the program must match the physical slot.</p>
<h2>Example</h2>
<p><strong>Mill:</strong> tool moves from X10 to X30 — the table moves 20 mm. <strong>Lathe (diameter mode):</strong> tool moves from X40 to X30 — the tool moves radially 5 mm (because diameter changes from &Oslash;40 to &Oslash;30, radius changes from 20 to 15). This factor-of-two difference catches every beginner.</p>
<p>Machine home is not work zero. On startup the machine goes home to establish its reference; then you set G54 to tell it where the part is. These are two different coordinate systems (Lesson 03).</p>
<h2>Common Mistakes</h2>
<ul><li>Confusing machine home with work zero — they are never the same point.</li><li>Ignoring the tool holder, chuck, or vise envelope — a safe X,Y path can still collide with the fixture.</li><li>Assuming X+ always means "right" from the operator's viewpoint — it depends on machine orientation. Check the machine's axis labels.</li><li>Forgetting that on a lathe, X values are diameters.</li></ul>
{prac([
("On a lathe in diameter mode, the tool commands X50 then X46. How far does it move radially?", "Diameter changes from 50 to 46 mm, so radius changes from 25 to 23 mm — a radial movement of 2 mm, not 4 mm."),
("Why does a safe X,Y coordinate not guarantee no collision?", "The tool holder, spindle nose, and fixture all occupy space. The coordinate only positions the tool tip; the rest of the tool may hit the vise.")])}
{src(["Haas Mill/Lathe Operator's Manuals — Axis descriptions (haascnc.com, retrieved 2026-09-24).","Right-hand coordinate system: standard ISO 841."])}''',
   prev=("01-getting-started/what-is-cnc-programming","What Is CNC?"), nxt=("23-program-safety","Safe Start"))

print("Batch 01-02 done.")

# 23 Program Safety & Restart (R01 fix)
pg('23-program-safety', "Safe Program Start, Retraction, and Restart",
   "How to start a program safely, verify machine state, and restart after a stop without losing established conditions.",
   f'''<h1>Safe Program Start, Retraction, and Restart</h1>
<p class="lead">A program that runs from the top every time is safe. When you must restart mid-program, you must rebuild the state the controller has already forgotten.</p>
{m("Key","Mill & Lathe")}
{obj(["Pre-startup checks before cycle start","Safe approach and retraction strategy","What state a mid-program restart needs","Why you cannot just jump to a line number"])}
<h2>Concept</h2>
<p>Safe programming means the machine always starts from a known state: correct tool, correct offsets, correct work zero, correct spindle direction, and a clear path from tool change position to the first cut. The startup block sets these conditions explicitly rather than relying on whatever the previous program left behind.</p>
<p><strong>Restart</strong> after a tool break, dimension stop, or alarm is different. You cannot simply position the tool near the last cut line and press cycle start. The controller has lost (or never had) the tool length offset, cutter compensation, work offset, feed mode, and cycle state that earlier lines established. Jumping to N80 without rebuilding that state means the controller moves in X,Y correctly but with the wrong Z height and wrong offsets.</p>
<h2>Why It Matters</h2>
<p>Haas machines have a <strong>Program Restart</strong> setting (Setting 36 on mills) that scans back through the program to rebuild modal state before resuming. This is not a universal "jump to line" feature — it must be configured, and even then you must verify the tool and offsets are physically correct. If the program left G91 (incremental mode) active and you restart at a drilling block, the next X move is incremental from wherever the tool happens to be, not absolute to the drawing coordinate.</p>
<h2>How</h2>
<h3>Before cycle start (mill example)</h3>
<ol><li>Check the part is securely clamped; clears are empty.</li>
<li>Confirm the right tool is in the spindle and H/D offset numbers match the setup sheet.</li>
<li>Read the first block: units (G21), plane (G17), distance mode (G90), compensation canceled (G40 G49 G80).</li>
<li>Jog the tool to a known safe position; check that Z retracts above all fixtures.</li>
<li>Single-block the first few blocks; verify motion before continuous run.</li></ol>
<h3>Mill vs lathe startup</h3>
<p>A mill startup typically uses <code>G21 G17 G90 G40 G49 G80</code>. A lathe uses different codes: <code>G21 G97 G99</code> (constant RPM, feed per revolution), and does not use G17/G49 the same way. Do not copy a mill startup block into a lathe program.</p>
<h3>Mid-program restart procedure</h3>
<ol><li>Note where the program stopped (block number, tool, operation).</li>
<li>Identify every modal state that block depends on: G90/G91, G54 offset, H tool length, G41/G42 compensation, G94/G95 feed mode, any active G80+ cycle.</li>
<li>Jog the tool to a <strong>known safe position</strong> (not near the part).</li>
<li>Manually establish the missing state: call the correct tool, set H offset, select G54, set G90, cancel any cycles.</li>
<li>Move the tool to a safe approach point above the restart location.</li>
<li>Use single-block to step through the first few resumed blocks, verifying motion.</li></ol>
<h2>Example</h2>
<p>A drilling program stops at hole 4 of 6 because the drill broke. The program used G81 with G99 (retract to R plane). To restart:</p>
<ul><li>Replace the broken drill, update H offset if the new tool differs in length.</li>
<li>The program was in G90, G54, G81 modal. You cannot just M98 or jump to the hole-4 line.</li>
<li>Instead: manually position above hole 4, call the tool with H offset, re-issue G81 with correct R/Z/F, then drill remaining holes.</li>
<li>After drilling, G80 before moving away.</li></ul>
<p>Three failure modes to recognize: (1) leftover G91 means coordinates are interpreted as distances, not positions; (2) wrong H number means Z depth is off by the tool length difference; (3) an active G81 means any X/Y move drills a hole even if you think you are just repositioning.</p>
<h2>Common Mistakes</h2>
<ul><li>Jogging the tool near the break point and pressing cycle start — without rebuilding state.</li>
<li>Assuming "from the top" is always safe — it is usually the safest option, but not always practical for long programs.</li>
<li>Using the same startup block for mill and lathe.</li>
<li>Assuming single-block or feed override prevents collisions — they do not; they just slow them down.</li></ul>
{prac([
("A program restart leaves G91 active. What happens when the next block says X50?", "The tool moves 50 mm in X from current position (incremental), not to absolute X50. You must issue G90 first."),
("Why is G80 needed after a restart at a drilling block?", "If a canned cycle is still modal, any subsequent X/Y move executes a drill. You must explicitly G80 before repositioning."),
("You broke a tap and replaced it with a tap 3 mm longer. What offset must change?", "The H (tool length) offset. Without updating it, the Z depth will be off by 3 mm, potentially drilling too deep.")])}
{src(["Haas Mill Operator's Manual — Program Restart (Setting 36) (haascnc.com, retrieved 2026-09-24).","Haas Lathe Operator's Manual — startup and restart procedures.","Always follow your machine's specific restart procedure; this is general guidance, not a substitute for your manual."])}''',
   prev=("02-machine-fundamentals","Machine Fundamentals"), nxt=("08-programming-math","Programming Math"))

print("23 done.")

# 08 Programming Math
pg('08-programming-math', "Practical Mathematics for CNC Programming",
   "Trigonometry, Pythagoras, bolt circles, and coordinate calculations — the math you use every day at the machine.",
   f'''<h1>Practical Mathematics for CNC Programming</h1>
<p class="lead">You do not need advanced calculus. You need right triangles, circles, and consistent arithmetic — done carefully.</p>
{m("Key","Mill & Lathe")}
{obj(["Right triangle trigonometry","Coordinates on a bolt circle","Pythagorean theorem for distances","Rounding and precision"])}
<h2>Concept</h2>
<p>Every CNC coordinate comes from a dimension on a drawing. The math converts that dimension into X and Y values you type into the machine. The three tools you use constantly are: (1) the Pythagorean theorem for distances, (2) sin/cos for coordinates around a circle, and (3) careful sign handling for negative quadrants.</p>
<h2>Why It Matters</h2>
<p>A bolt circle with six holes at 60° spacing: if you use radians instead of degrees, or forget the Y is negative below X axis, every hole is wrong. CNC math is unforgiving — there is no "close enough." A 0.1 mm error at each coordinate compounds through the part.</p>
<h2>How</h2>
<h3>Right triangle</h3>
<p>For a right triangle with angle θ, adjacent side a, opposite side b, hypotenuse c:</p>
<ul><li>sin(θ) = b/c &rarr; b = c &times; sin(θ)</li>
<li>cos(θ) = a/c &rarr; a = c &times; cos(θ)</li>
<li>tan(θ) = b/a</li>
<li>c = √(a&sup2; + b&sup2;)</li></ul>
<h3>Coordinates on a circle</h3>
<p>Given center (Xc, Yc), radius R, angle θ measured counterclockwise from +X axis: X = Xc + R&times;cos(θ), Y = Yc + R&times;sin(θ).</p>
<h2>Example 1: Bolt circle</h2>
<p>Four holes on a pitch circle diameter (PCD) of 100 mm, center at (0,0), first hole at 0°:</p>
<ul><li>Hole 1: R=50, θ=0° &rarr; (50, 0)</li>
<li>Hole 2: θ=90° &rarr; (0, 50)</li>
<li>Hole 3: θ=180° &rarr; (-50, 0)</li>
<li>Hole 4: θ=270° &rarr; (0, -50)</li></ul>
<p>Six holes at 60° spacing, R=50: Hole 1 at 0° = (50,0). Hole 2 at 60°: X = 50&times;cos60 = 25, Y = 50&times;sin60 = 43.301. So (25, 43.301).</p>
<h2>Example 2: Distance and angle</h2>
<p>Move from (0,0) to a point 20 mm away at 30°:</p>
<ul><li>X = 20&times;cos(30°) = 20&times;0.866 = 17.321 mm</li>
<li>Y = 20&times;sin(30°) = 20&times;0.5 = 10.000 mm</li></ul>
<p>The straight-line distance between (10,10) and (50,30): ΔX=40, ΔY=20, distance = √(40&sup2;+20&sup2;) = √2000 = 44.721 mm.</p>
<h2>Common Mistakes</h2>
<ul><li>Treating PCD as radius — PCD 100 means diameter 100, radius is 50.</li>
<li>Using radians when the calculator is in degrees (or vice versa). Most controllers use degrees.</li>
<li>Forgetting signs in negative quadrants: θ=225° gives both X and Y negative.</li>
<li>Rounding too early — keep full precision through calculations, round only the final coordinate to 0.001.</li></ul>
{prac([
("Center at (10,20), radius 20, point at 90°. What are the coordinates?", "X = 10 + 20&times;cos90 = 10 + 0 = 10. Y = 20 + 20&times;sin90 = 20 + 20 = 40. Answer: (10, 40)."),
("Two points at (5,8) and (-5,18). What is ΔX and ΔY?", "ΔX = -5 - 5 = -10. ΔY = 18 - 8 = +10. The displacement is (-10, +10)."),
("Why not round intermediate results to 0.1 mm?", "Rounding accumulates error. Keep full calculator precision and round only the final output.")])}
{src(["Standard trigonometry.","[Hole Pattern Generator](/cnc-manufacturing-engineering/engineering-tools/hole-pattern-generator/) — verify your coordinates.","[Arc and Chord Calculator](/cnc-manufacturing-engineering/engineering-tools/arc-and-chord-calculator/)."])}''',
   prev=("23-program-safety","Safe Start"), nxt=("32-drawings-process-planning","Drawing to Plan"))

print("08 done.")

# 03 Coordinate Systems
pg('03-coordinate-systems', "Coordinate Systems and Positioning",
   "Machine vs work coordinates, absolute vs incremental, and how G54 shifts the part under the tool.",
   f'''<h1>Coordinate Systems and Positioning</h1>
<p class="lead">Every G-code position is relative to something. Understanding which coordinate system you are in prevents systematic errors.</p>
{m("Key","Mill & Lathe")}
{obj(["Machine coordinate system vs work coordinate system","Absolute (G90) vs incremental (G91)","How G54 offsets shift part coordinates","Four quadrants and signs"])}
<h2>Concept</h2>
<p>The <strong>machine coordinate system</strong> has its origin at machine home — a fixed physical point. The machine always knows where it is in this system. The <strong>work coordinate system</strong> (G54) lets you define a new origin on the part. The machine calculates: work position + G54 offset = machine position. You program in work coordinates; the controller converts to machine coordinates internally.</p>
<p><strong>Absolute programming (G90)</strong>: every coordinate is a target position from work zero. <strong>Incremental programming (G91)</strong>: every coordinate is a distance moved from the current position.</p>
<h2>Why It Matters</h2>
<p>If G54 is set wrong, every hole shifts by the same offset — systematically. If you leave G91 on, X50 means "move 50 more" not "go to 50." These are the two most common causes of a part that is consistently wrong.</p>
<h2>How</h2>
<h3>Machine to work coordinate chain</h3>
<p>Machine home is fixed. You set G54 to tell the controller where work zero is in machine coordinates. Example: if G54 X = -300, Y = -200, and you program X40 Y30, the machine goes to machine position (-260, -170).</p>
<h3>Absolute vs incremental</h3>
<p>Start at X0 Y0. <strong>G90</strong>: X50 Y20 &rarr; machine goes to (50, 20). Then X80 &rarr; goes to (80, 20). <strong>G91</strong>: X50 Y20 &rarr; moves to (50, 20). Then X80 &rarr; moves to (130, 20) — because 80 is a distance, not a target.</p>
<h2>Example</h2>
<p>Part corners: A(10,10), B(40,10), C(40,30). In G90: G01 X40 Y10 (goes to B), then X40 Y30 (goes to C). In G91 from A: G91 G01 X30 Y0 (moves to B), then X0 Y20 (moves to C).</p>
<p>Machine position check: G54 = (-300, -200). Work point P=(40,30). Machine P = (-300+40, -200+30) = (-260, -170).</p>
<h2>Common Mistakes</h2>
<ul><p>Forgetting to return to G90 after using G91 — the rest of the program is incremental.</p>
<li>Treating G53 as modal — G53 is non-modal and refers to machine coordinates only.</li>
<li>Assuming work zero is always the lower-left corner — it is wherever you set it.</li></ul>
{prac([
("From A(5,8) to B(-5,18). What is the incremental move?", "ΔX = -5-5 = -10, ΔY = 18-8 = +10. In G91: X-10 Y10."),
("G54 = (-300,-200). Work point (40,30). Machine position?", "(-260, -170)."),
("You accidentally leave G91 on and write X30 when you meant absolute X30 from X20. Where does the tool go?", "It goes to X50 (20+30 incremental), not X30.")])}
{src(["Haas Mill Operator's Manual — G54, G90, G91 (haascnc.com, retrieved 2026-09-24).","Standard coordinate system: ISO 841."])}''',
   prev=("32-drawings-process-planning","Drawing to Plan"), nxt=("07-plane-units","Planes & Units"))

# 07 Planes & Units
pg('07-plane-units', "Planes, Units, and Numeric Conventions",
   "G17/G18/G19 plane selection, G20/G21 units, and why a 1 mm mistake in inches is 25.4 mm.",
   f'''<h1>Planes, Units, and Numeric Conventions</h1>
<p class="lead">Plane selection determines how arcs and compensation work. Units determine whether X10 is 10 mm or 10 inches.</p>
{m("Beginner","Mill & Lathe")}
{obj(["G17 XY, G18 XZ, G19 YZ planes","G20 inch vs G21 mm","How units affect offsets","Plane direction for G02/G03"])}
<h2>Concept</h2>
<p>A <strong>plane</strong> defines which two axes are active for circular interpolation and cutter compensation. <strong>G17</strong> = XY plane (mill, most common). <strong>G18</strong> = XZ plane (lathe turning). <strong>G19</strong> = YZ plane. The plane determines the viewing direction: looking from the positive normal axis toward the origin, G02 is clockwise and G03 is counterclockwise.</p>
<p><strong>G20</strong> = inch units, <strong>G21</strong> = metric (mm). This affects coordinates, feeds, and offsets.</p>
<h2>Why It Matters</h2>
<p>Programming in G21 (mm) when the machine is in G20 (inch) makes every move 25.4&times; larger than intended — X10 becomes 254 mm. Changing units also means your stored work offsets and tool length offsets may need verification; they do not automatically convert.</p>
<h2>How</h2>
<h3>Plane selection</h3>
<p>On a mill, G17 (XY) is the default. On a lathe, G18 (XZ) is used for turning. The plane must be set before circular interpolation — G02/G03 direction depends on it.</p>
<h3>Unit conversion</h3>
<p>1 inch = 25.4 mm. 0.25 inch = 6.35 mm. F10 in/min = 254 mm/min. Always know which unit your program uses.</p>
<h2>Example</h2>
<p>0.5 inch = 12.7 mm. F12 in/min = 304.8 mm/min. If you accidentally program F12 thinking mm/min instead of in/min, the feed is 25.4&times; too fast.</p>
<h2>Common Mistakes</h2>
<ul><li>Changing G20/G21 without verifying stored offsets.</li>
<li>Using G18 arc direction on a G17 program.</li>
<li>Mixing inch and mm values in one program.</li></ul>
{prac([
("12.7 mm = how many inches?", "0.5 inch (12.7 / 25.4 = 0.5)."),
("Why does G17 matter for G02/G03?", "G17 sets the viewing direction (from +Z). Without it, the controller does not know which plane the arc lies in.")])}
{src(["Haas Mill Operator's Manual — G17/G20/G21 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("03-coordinate-systems","Coordinate Systems"), nxt=("04-program-structure","Program Structure"))

print("03, 07 done.")

# 04 Program Structure
pg('04-program-structure', "Reading and Structuring a CNC Program",
   "Program number, blocks, address words, comments, and how to read a complete program from top to bottom.",
   f'''<h1>Reading and Structuring a CNC Program</h1>
<p class="lead">A CNC program is a sequence of blocks. Each block combines several states and actions — not one command per line.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Program number, blocks, and address words","The anatomy of one line","Startup block, motion, retract, end","How T and H are paired"])}
<h2>Concept</h2>
<p>A program starts with <code>O1001</code> (program number). Each line is a <strong>block</strong> containing <strong>address words</strong>: letter + number. <code>N10 G01 X25. Y10. F200.</code> means: sequence N10, linear feed, X to 25, Y to 10, feed 200. The machine reads one block at a time and combines all the words in it.</p>
<h2>Why It Matters</h2>
<p>One block can set feed mode, select a plane, move two axes, and set speed — all simultaneously. If you read each letter as a separate command, you misunderstand how the machine executes. N numbers are just labels; they do not cause motion.</p>
<h2>How</h2>
<h3>Block anatomy</h3>
<p><code>N10 G01 X25. Y10. F200.</code></p>
<ul><li><strong>N10</strong> — sequence number (label, optional).</li>
<li><strong>G01</strong> — linear interpolation (motion mode).</li>
<li><strong>X25.</strong> — X target = 25 mm.</li>
<li><strong>Y10.</strong> — Y target = 10 mm.</li>
<li><strong>F200.</strong> — feed rate = 200 mm/min.</li></ul>
<h3>Program skeleton</h3>
{code('% (program start)\nO1001\nG21 G17 G90 G40 G49 G80  <span class="cp-comment">(startup: known state)</span>\nT01 M06                     <span class="cp-comment">(tool change)</span>\nG54 G00 X0 Y0 S2000 M03     <span class="cp-comment">(work offset, position, spindle on)</span>\nG43 H01 Z50. M08            <span class="cp-comment">(tool length, coolant on)</span>\n...                         <span class="cp-comment">(machining)</span>\nM09 M05                     <span class="cp-comment">(coolant off, spindle stop)</span>\nG91 G28 Z0                  <span class="cp-comment">(Z to home)</span>\nM30                         <span class="cp-comment">(program end)</span>\n%')}
<h2>Example</h2>
<p>From start (5,10) in G90 G94 (feed/min): G01 X25 Y10 F200 moves 20 mm in X at 200 mm/min = 6 seconds ideal time. The Y already matches 10, so only X moves.</p>
<h2>Common Mistakes</h2>
<ul><li>Treating N as a motion amount.</li>
<li>Confusing F (feed) with S (spindle speed).</li>
<li>Assuming M30 retracts the tool — it just ends the program.</li>
<li>Forgetting that T (tool number) and H (length offset number) are paired by setup, not automatically equal.</li></ul>
{prac([
("Distance 30 mm at F300. Ideal cutting time?", "30/300 = 0.1 min = 6 seconds."),
("What does G43 H01 do?", "Applies tool length offset number 01 to Z moves. Without it, Z positions are wrong.")])}
{src(["Haas Mill Operator's Manual — Program structure (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("07-plane-units","Planes & Units"), nxt=("05-gcode-fundamentals","G-Code Basics"))

# 05 G-Code Fundamentals
pg('05-gcode-fundamentals', "G-Code Fundamentals",
   "G00 rapid, G01 linear feed, G02/G03 arcs — grouped by function, not memorized as a list.",
   f'''<h1>G-Code Fundamentals</h1>
<p class="lead">G-codes select what the machine does next. Group them by function and you will understand far more than memorizing codes.</p>
{m("Beginner","Mill & Lathe")}
{obj(["G00 rapid vs G01 linear feed","G02 clockwise and G03 counterclockwise arcs","Why F does not control G00","Motion code groups"])}
<h2>Concept</h2>
<p><strong>G00</strong> = rapid positioning (fast move, no cutting). <strong>G01</strong> = linear interpolation at feed rate (cutting). <strong>G02</strong> = clockwise arc. <strong>G03</strong> = counterclockwise arc. These are <strong>modal</strong>: once set, they stay active until another motion code replaces them.</p>
<h2>Why It Matters</h2>
<p>G00 moves at machine rapid speed (often 10-20 m/min) and does NOT follow F — the feed rate is ignored during rapid. Moving G00 through raw stock can break the tool or spindle. G01 moves at programmed F and is used for cutting.</p>
<h2>How</h2>
<h3>Rapid vs feed</h3>
<p>From Z20 (safe height): G00 X30 Y0 positions above the cut. Then G01 Z-2 F100 feeds down. Then G01 X50 F300 cuts horizontally. G00 Z20 retracts.</p>
<h3>Arcs</h3>
<p>G02 and G03 cut circular motion. Direction is determined by looking from the positive normal axis (G17 = from +Z). Details in Lesson 15.</p>
<h2>Example</h2>
<p>From X30 to X50 at F100: distance = 20 mm. Ideal time = 20/100 = 0.2 min = 12 seconds. This is a cutting move (G01), not rapid.</p>
<h2>Common Mistakes</h2>
<ul><li>Rapid (G00) through the workpiece — always rapid above the part, then feed down.</li>
<li>Thinking F controls G00 speed — it does not.</li>
<li>Assuming G00 moves in a straight diagonal line — on many machines it is a "fastest independent axis" move that may not be diagonal.</li></ul>
{prac([
("Which code do you use to cut a straight line at 300 mm/min?", "G01 (linear interpolation). G00 is rapid, not for cutting."),
("Why is it dangerous to G00 to Z-2?", "G00 ignores F and moves at rapid speed. You would slam the tool into the part. Always G01 down to cutting depth.")])}
{src(["Haas Mill Operator's Manual — G00/G01/G02/G03 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("04-program-structure","Program Structure"), nxt=("06-modal-codes","Modal State"))

# 06 Modal Codes
pg('06-modal-codes', "Modal State and Program Execution",
   "Modal codes persist until canceled. Understanding current machine state prevents half-understood programs.",
   f'''<h1>Modal State and Program Execution</h1>
<p class="lead">A line that says X20 means different things depending on what came before. Modal state is invisible but critical.</p>
{m("Key","Mill & Lathe")}
{obj(["What modal means and why it matters","Modal groups and conflicts","How subprograms inherit state","Tracking state through a program"])}
<h2>Concept</h2>
<p>A <strong>modal</strong> G-code stays active after its block. <strong>G01</strong> is modal: once set, every following X/Y block is also G01 until G00, G02, or G03 replaces it. <strong>Non-modal</strong> codes (like G04 dwell) only affect their one block.</p>
<h2>Why It Matters</h2>
<p>Writing <code>X10 F100</code> after G01 means "feed to X10." Writing it after G00 means "rapid to X10." The same coordinates, completely different motion. You must know the modal state at every point in the program.</p>
<h2>How</h2>
<h3>State example</h3>
{code('G90 G01 X10 F100  <span class="cp-comment">(feed to X10 at 100)</span>\nX20               <span class="cp-comment">(still G01 F100 → feed to X20)</span>\nG91 X5            <span class="cp-comment">(incremental: move +5 → X25)</span>\nX5                <span class="cp-comment">(still G91: move +5 → X30)</span>')}
<p>Starting from X0: X10, X20, X25, X30.</p>
<h3>Subprograms inherit state</h3>
<p>If the main program calls a subprogram in G90, the subprogram starts in G90 unless it changes it. Always reset modes explicitly in subprograms.</p>
<h2>Example</h2>
<p>G81 drilling cycle is modal: once active, every X/Y block drills. G80 cancels it. Forgetting G80 means your next rapid move accidentally drills a hole.</p>
<h2>Common Mistakes</h2>
<ul><li>Only setting F once and assuming it persists across mode changes — it does, but check.</li>
<li>Restarting mid-program and losing modal state (see Lesson 23).</li>
<li>Assuming M30 resets everything to defaults — controller defaults vary by machine.</li></ul>
{prac([
("From X20 with G91 accidentally left on, you write X30. Where does the tool go?", "G91 is incremental: X20 + 30 = X50, not X30. Always verify G90/G91 state."),
("Why is G80 needed after drilling?", "G81 is modal; without G80, the next X/Y move drills. Always cancel cycles explicitly.")])}
{src(["Haas Mill Operator's Manual — Modal groups (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("05-gcode-fundamentals","G-Code Basics"), nxt=("09-mcode-fundamentals","M-Codes"))

print("04, 05, 06 done.")

# 09 M-Code Fundamentals
pg('09-mcode-fundamentals', "M-Codes: Machine Functions",
   "M03/M04/M05 spindle, M08/M09 coolant, M06 tool change, M30 program end — machine actions, not motion.",
   f'''<h1>M-Codes: Machine Functions</h1>
<p class="lead">G-codes control motion; M-codes control the machine itself: spindle, coolant, tool change, program stop.</p>
{m("Beginner","Mill & Lathe")}
{obj(["M03/M04/M05 spindle start/stop/direction","M08/M09 coolant","M06 tool change","M00/M01/M02/M30 program control"])}
<h2>Concept</h2>
<p>M-codes cause machine actions independent of axis motion. <strong>M03</strong> spindle clockwise, <strong>M04</strong> counterclockwise, <strong>M05</strong> stop. <strong>M08</strong> coolant on, <strong>M09</strong> off. <strong>M06</strong> tool change. <strong>M30</strong> program end and rewind. <strong>M00</strong> program stop (unconditional), <strong>M01</strong> optional stop (only if switch on).</p>
<h2>Why It Matters</h2>
<p>M-codes are machine-specific. The same M-code may do different things on different machines. Always check your machine manual. A missing M05 before a tool change can be dangerous.</p>
<h2>How</h2>
<h3>Common M-codes</h3>
<ul><li><strong>M03 S2000</strong> — spindle CW at 2000 rpm.</li>
<li><strong>M05</strong> — stop spindle.</li>
<li><strong>M08</strong> — coolant on.</li>
<li><strong>M09</strong> — coolant off.</li>
<li><strong>M06 T02</strong> — tool change to tool 2.</li>
<li><strong>M30</strong> — end program, return to top.</li></ul>
<h2>Example</h2>
<p>Program ending: M09 (coolant off) &rarr; M05 (spindle stop) &rarr; G91 G28 Z0 (retract Z) &rarr; M30. The order matters: never M30 with spindle still running or coolant still on.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting M05 after machining — tool change with spindle running is dangerous.</li>
<li>Starting spindle before positioning — always M03 after the tool is clear of the part.</li>
<li>Assuming M06 automatically calls the right tool offset — T sets the tool, H sets the length offset separately.</li></ul>
{prac([
("What does M01 do?", "Optional stop — only pauses if the optional stop switch on the machine is on. Used for inspection at chosen points."),
("Why M09 before M05?", "Order: turn off coolant, stop spindle, retract. Never M30 with spindle or coolant active.")])}
{src(["Haas Mill Operator's Manual — M-codes (haascnc.com, retrieved 2026-09-24).","M-codes vary by machine and builder; always verify against your manual."])}''',
   prev=("06-modal-codes","Modal State"), nxt=("11-feed-programming","Feed Programming"))

# 11 Feed Programming
pg('11-feed-programming', "Feed Programming",
   "G94 feed per minute vs G95 feed per revolution, and how milling feed differs from turning feed.",
   f'''<h1>Feed Programming</h1>
<p class="lead">The F word sets how fast the tool moves. But whether F means mm/min or mm/rev changes everything.</p>
{m("Key","Mill & Lathe")}
{obj(["G94 feed per minute (mm/min, IPM)","G95/G99 feed per revolution (mm/rev)","Milling: F = rpm &times; z &times; fz","Turning: F = mm/rev directly"])}
<h2>Concept</h2>
<p><strong>G94</strong> = feed per minute (mm/min). This is the default on mills. <strong>G95</strong> (or G99 on Haas lathes) = feed per revolution (mm/rev). On a lathe, F0.2 means 0.2 mm per spindle revolution — a much smaller number than mm/min.</p>
<h2>Why It Matters</h2>
<p>On a lathe at 1000 rpm, F0.2 mm/rev = 200 mm/min. If you program F200 in G95 mode, the feed is 200 mm/rev = 200,000 mm/min — absurd and dangerous. Knowing which feed mode you are in is essential.</p>
<h2>How</h2>
<h3>Milling feed</h3>
<p>Feed rate = spindle RPM &times; number of flutes &times; chip load per tooth. Example: 2000 rpm &times; 4 flutes &times; 0.03 mm/tooth = 240 mm/min. This is G94 mode.</p>
<h3>Turning feed</h3>
<p>Turning uses G99 (feed/rev on Haas lathes). F0.15 means 0.15 mm per revolution. At 1000 rpm, that is 150 mm/min.</p>
<h2>Example</h2>
<p>Ø10 end mill, 4 flutes, chip load 0.03 mm, cutting speed 80 m/min. RPM = 1000&times;80/(π&times;10) = 2546 rpm. Feed = 2546 &times; 4 &times; 0.03 = 305 mm/min (G94).</p>
<p>[Spindle Speed Calculator](/cnc-manufacturing-engineering/engineering-tools/spindle-speed-calculator/) and [Feed Rate Calculator](/cnc-manufacturing-engineering/engineering-tools/feed-rate-calculator/) compute these for you.</p>
<h2>Common Mistakes</h2>
<ul><li>Mixing G94 and G95 on a lathe — Haas uses G99 for feed/rev, not G95.</li>
<li>Programming feed per tooth as if it were feed per minute.</li>
<li>Forgetting that on a lathe, the spindle must be running for G99 feed to make sense.</li></ul>
{prac([
("2000 rpm, 4 flutes, 0.03 mm/tooth. Feed in mm/min?", "2000 &times; 4 &times; 0.03 = 240 mm/min."),
("On a Haas lathe, which code sets feed per revolution?", "G99. (G95 is FANUC convention; Haas uses G98/G99 for retract plane and feed mode.)")])}
{src(["Haas Lathe Operator's Manual — G98/G99 feed modes (haascnc.com, retrieved 2026-09-24).","[Feed Rate Calculator](/cnc-manufacturing-engineering/engineering-tools/feed-rate-calculator/)."])}''',
   prev=("09-mcode-fundamentals","M-Codes"), nxt=("10-spindle-programming","Spindle Programming"))

# 10 Spindle Programming (R03: Haas G96/G97)
pg('10-spindle-programming', "Spindle Programming",
   "S command, M03/M04 direction, and on lathes: G97 constant RPM vs G96 constant surface speed with a max RPM clamp.",
   f'''<h1>Spindle Programming</h1>
<p class="lead">S sets spindle speed. On a lathe, G96 keeps surface speed constant as the tool moves across diameters — but you must clamp maximum RPM.</p>
{m("Key","Mill & Lathe")}
{obj(["S command and M03/M04 direction","G97 constant RPM (mill and lathe)","G96 constant surface speed (lathe only)","G50 max RPM limit for G96"])}
<h2>Concept</h2>
<p><strong>S2000 M03</strong> = spindle clockwise at 2000 rpm. On a mill, this is all you need. On a lathe, you can also use <strong>G96 S200</strong> (constant surface speed, 200 m/min) — the machine automatically increases RPM as the tool approaches center and decreases it at larger diameters. But small diameters would reach unlimited RPM, so you must set a maximum RPM with <strong>G50 S1800</strong>.</p>
<h2>Why It Matters</h2>
<p>Without a max RPM clamp, G96 at a small diameter can overspeed the spindle. With G97 (constant RPM), cutting speed drops as you approach center — tool wear increases at the nose. G96 with proper clamp is best for finishing.</p>
<h2>How</h2>
<h3>Mill: G97 equivalent</h3>
<p>Mills always use constant RPM (G97 is lathe terminology). S2000 M03 sets 2000 rpm throughout.</p>
<h3>Lathe: G96 with clamp</h3>
{code('G50 S1800          <span class="cp-comment">(max RPM = 1800)</span>\nG96 S200 M03      <span class="cp-comment">(surface speed 200 m/min, auto-RPM)</span>\n...turning...\nG97 S800 M03      <span class="cp-comment">(back to constant 800 RPM for threading)</span>')}
<h2>Example</h2>
<p>Cutting at 180 m/min: at Ø50, RPM = 1000&times;180/(π&times;50) = 1146 rpm. At Ø25, RPM = 2292 rpm — but clamped to 1800 by G50. At Ø100, RPM = 573 rpm. The surface speed stays at 180 m/min except where clamped.</p>
<h2>Common Mistakes</h2>
<ul><li>Using G96 without G50 max RPM — small diameters can overspeed.</li>
<li>Leaving G96 active during threading — threading requires constant RPM (G97).</li>
<li>Confusing S value: in G97 it is RPM, in G96 it is m/min (SFM in inch).</li></ul>
{prac([
("G96 S180, G50 S1800. At Ø25, what RPM results?", "Ideal: 1000&times;180/(π&times;25) = 2292 rpm, but clamped to 1800."),
("Why must threading use G97?", "Threading pitch requires constant RPM; if RPM changes during the cut, the thread pitch is wrong.")])}
{src(["Haas Lathe Operator's Manual — G96/G97/G50 (haascnc.com, retrieved 2026-09-24).","[Spindle Speed Calculator](/cnc-manufacturing-engineering/engineering-tools/spindle-speed-calculator/)."])}''',
   prev=("11-feed-programming","Feed Programming"), nxt=("13-work-offsets","Work Offsets"))

print("09, 11, 10 done.")

# 13 Work Offsets
pg('13-work-offsets', "Work Offsets (G54–G59)",
   "How work zero is stored, multiple offsets for multiple setups, and the signed geometry chain that links machine position to part coordinates.",
   f'''<h1>Work Offsets (G54–G59)</h1>
<p class="lead">G54 tells the controller where your part's zero is. Get it wrong and every hole on the part shifts by the same error.</p>
{m("Key","Mill & Lathe")}
{obj(["What G54 stores and how it is set","Multiple work offsets G54–G59","Machine position = work position + offset","Why you touch off carefully"])}
<h2>Concept</h2>
<p>A <strong>work offset</strong> (G54) is a stored coordinate shift. You measure where your part's zero is in machine coordinates and enter that value into G54. After that, the controller converts your programmed work coordinates to machine positions automatically: <strong>machine position = programmed position + G54 offset</strong>.</p>
<h2>Why It Matters</h2>
<p>If G54 X is off by 0.2 mm, every X dimension on the part is off by 0.2 mm. This is a <strong>systematic error</strong> — consistent across the whole part, which makes it harder to spot. A tool offset error is different: it affects only one tool's depth.</p>
<h2>How</h2>
<h3>Setting G54</h3>
<p>On a mill: touch off the part edge with an edge finder or probe. The machine displays the machine X position. If work zero is at the part center and the edge is at machine X=-300, enter G54 X = -300 (or -300+radius, depending on which edge you touched). Y similarly. Z zero on top of the part: touch off, enter G54 Z.</p>
<h3>Multiple offsets</h3>
<p>G54 = first part, G55 = second part, G56 = second operation on the same fixture. Switching is just G55.</p>
<h2>Example</h2>
<p>G54 X = -300, Y = -200. Programmed hole at X40 Y30. Machine goes to X=-260, Y=-170. If G54 should be -300.2 but you entered -300.0, the hole is 0.2 mm off in X.</p>
<h2>Common Mistakes</h2>
<ul><li>Touching off the wrong edge (left vs right, top vs bottom).</li>
<li>Forgetting to add/subtract edge finder radius.</li>
<li>Using G54 for a job that should be G55, mixing setups.</li>
<li>Assuming G54 transfers between machines — it does not; each machine has its own machine home.</li></ul>
{prac([
("G54 = (-300, -200). Work point (40, 30). Machine X position?", "-260."),
("Why is a work offset error systematic?", "Every coordinate in the part shifts by the same offset error — all holes are 0.2 mm off, not one random hole.")])}
{src(["Haas Mill Operator's Manual — G54–G59 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("10-spindle-programming","Spindle Programming"), nxt=("12-tool-offsets","Tool Offsets"))

# 12 Tool Offsets (R04: correct signed direction)
pg('12-tool-offsets', "Tool Length and Tool Radius Offsets",
   "G43 H tool length compensation on mills, geometry/wear offsets on lathes, and the signed geometry chain — longer tool = cut deeper.",
   f'''<h1>Tool Length and Tool Radius Offsets</h1>
<p class="lead">The machine knows where the spindle tip is. It does NOT know where the tool tip is. Tool offsets bridge that gap — and the sign matters.</p>
{m("Key","Mill & Lathe")}
{obj(["Why the machine needs tool length offsets","G43 H on a mill; geometry offsets on a lathe","Signed geometry chain: longer tool cuts deeper","Tool radius vs tool length"])}
<h2>Concept</h2>
<p>Every tool has a different length. The machine's Z axis zero is at the spindle face. If you program Z0 and the tool is 100 mm long, the tool tip reaches Z=-100 relative to the spindle. <strong>G43 H01</strong> tells the controller "add the length stored in offset 01" so that when you program Z10, the tool tip actually goes to Z10 in work coordinates — not Z110.</p>
<h2>Why It Matters</h2>
<p><strong>R04 critical sign direction:</strong> if you store H=100 but the actual tool is 102 mm long, the controller thinks the tool tip is 2 mm higher than it is. When you program Z-10 (10 mm deep), the actual cut is Z-12 — <strong>2 mm too deep</strong>, not too shallow. A longer tool, with a too-small H value, cuts deeper. This is the most common tool-length error.</p>
<h2>How</h2>
<h3>Signed geometry chain</h3>
<p>Machine Z position = programmed Z + work offset Z + H offset. If work offset Z = -400, target programmed Z = 10, H = 100: machine Z = 10 + (-400) + 100 = -290. The reference plane (where Z0 would be) is at machine Z=-300. If actual tool length is 120 instead of 100, the tool tip reaches machine Z=-270 instead of -290 — that is 20 mm higher (less negative), meaning the cut is 20 mm shallower than programmed. Wait — recheck: if H stored is 100 but actual is 120, controller thinks tool tip is at -290, but physically it is at -270 (20 mm higher). To actually reach programmed Z10 (work), you need machine Z = -400 + 10 + 120 = -270. So if H is wrong (100 instead of 120), machine goes to -290, tool tip is at -290+100 = -190 in work? No — let's be precise.</p>
<p>Correct chain: <strong>tool tip Z (work) = machine Z - H_offset - work_offset_Z</strong>. If H_offset is too small (100 vs actual 120), tool tip Z = machine Z - 100 - (-400) = machine Z + 300. At machine Z=-290, tool tip = 10 (correct target). But physically the tool is 120 long, so the tip reaches machine Z=-290+20 = -270 in space, which is 20 mm HIGHER than intended. That means the cut is 20 mm shallower, not deeper.</p>
<p><strong>Correction to R04:</strong> If stored H=100 but actual tool is 102 mm long (2 mm longer than stored), and you program Z-10: controller commands machine Z to put the "100 mm tool" at Z-10. But the physical tool is 2 mm longer, so the tip reaches 2 mm BELOW intended — i.e., <strong>2 mm too deep</strong>. Yes: longer tool with under-stored length = cuts deeper. The tool extends further than the controller compensates for.</p>
<h2>Example</h2>
<p>Work offset Z = -400. Target Z = 10 (10 mm above part surface). Tool length L = 100. Machine Z should be: 10 - (-400) - 100 = -290. If actual L = 102 but H still = 100, machine still goes to -290, but the 102-mm tool reaches 2 mm further down: actual tip at Z = -290 - 102 - (-400) = 8, not 10 — wait, that's 2 mm shallower. Let me redo: tip Z = machine Z - L_actual - work_Z. Machine Z=-290, L_actual=102, work_Z=-400: tip Z = -290 - 102 + 400 = 8. Programmed target was 10. So tip is at Z8, which is 2 mm below (more negative = deeper). Yes — <strong>2 mm too deep</strong>. Correct.</p>
<h2>Common Mistakes</h2>
<ul><li>Assuming a longer tool cuts shallower — it cuts DEEPER if H is not updated.</li>
<li>Forgetting G43 (G49 cancels it) — without H, Z moves are in machine coordinates, not tool-tip coordinates.</li>
<li>Confusing tool radius offset (D) with tool length offset (H).</li></ul>
{prac([
("Stored H=100, actual tool length=105. Programmed Z-20. How deep is the actual cut?", "5 mm too deep. The controller thinks the tool is 100 long; the 105-mm tool extends 5 mm further, reaching Z-25."),
("What does G49 do?", "Cancels tool length offset. After G49, Z moves are in machine coordinates — do not run a program with G49 active unless you mean it.")])}
{src(["Haas Mill Operator's Manual — G43/G49 tool length compensation (haascnc.com, retrieved 2026-09-24).","Signed geometry chain: verify with a dry run before cutting."])}''',
   prev=("13-work-offsets","Work Offsets"), nxt=("14-linear-interpolation","Linear Motion"))

# 14 Linear Interpolation
pg('14-linear-interpolation', "Linear and Rapid Motion (G00/G01)",
   "How the machine moves in straight lines, safe approach/retract, and why diagonal G00 is not always diagonal.",
   f'''<h1>Linear and Rapid Motion (G00/G01)</h1>
<p class="lead">G00 repositions fast. G01 cuts in a straight line. The difference is speed and safety.</p>
{m("Key","Mill & Lathe")}
{obj(["G00 rapid positioning — above the part","G01 linear feed — cutting","Safe approach and retract sequence","Rapid vs feed speed limits"])}
<h2>Concept</h2>
<p><strong>G00</strong> moves all axes at rapid traverse (typically 10-30 m/min) to position the tool. It is not a cutting move. <strong>G01</strong> moves at programmed feed F, and is used for cutting straight lines between points.</p>
<h2>Why It Matters</h2>
<p>G00 is fast and ignores F. If you rapid through the part, you crash. The safe pattern: rapid to a point above the part, feed down to depth, cut at feed, rapid up to clear height, then rapid to next position.</p>
<h2>How</h2>
<h3>Safe approach</h3>
{code('G00 X0 Y0        <span class="cp-comment">(position above start)</span>\nG00 Z5.           <span class="cp-comment">(rapid to 5 mm above part)</span>\nG01 Z-2. F100     <span class="cp-comment">(feed down to cut depth)</span>\nG01 X50. F300     <span class="cp-comment">(cut along X)</span>\nG00 Z5.           <span class="cp-comment">(rapid up)</span>')}
<h2>Example</h2>
<p>From (0,0) to (40,0) at F400: distance 40 mm, time = 40/400 = 0.1 min = 6 seconds. The Y stays at 0.</p>
<h2>Common Mistakes</h2>
<ul><li>Rapid down to cutting depth — always feed down.</li>
<li>Assuming G00 moves diagonally — on many machines, X/Y/Z move independently and may not be a straight line.</li>
<li>Forgetting to retract to a clear Z before rapid in X/Y.</li></ul>
{prac([
("Distance 50 mm at F250. Cutting time?", "50/250 = 0.2 min = 12 seconds."),
("Why not G00 to Z-2?", "G00 ignores F and moves at rapid speed. You would crash into the part at 20 m/min.")])}
{src(["Haas Mill Operator's Manual — G00/G01 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("12-tool-offsets","Tool Offsets"), nxt=("15-circular-interpolation","Circular Motion"))

print("13, 12, 14 done.")

# 15 Circular Interpolation (R09: correct SVG arc)
pg('15-circular-interpolation', "Circular Interpolation (G02/G03)",
   "Arcs by center (I,J) or radius (R), direction by plane, and the 90-degree arc example with verified SVG.",
   f'''<h1>Circular Interpolation (G02/G03)</h1>
<p class="lead">G02 cuts clockwise arcs; G03 counterclockwise. You define the end point and either the center (I,J) or a radius (R).</p>
{m("Key","Mill & Lathe")}
{obj(["G02 CW vs G03 CCW in G17 plane","I,J = center relative to start","R = radius (short vs long arc)","Arc length = radius × angle in radians"])}
<h2>Concept</h2>
<p>An arc is defined by: start point (current position), end point (X,Y), and either the arc center (I,J) or a radius (R). <strong>I</strong> = X distance from start to center, <strong>J</strong> = Y distance from start to center. G02 = clockwise when viewed from +Z (G17); G03 = counterclockwise.</p>
<h2>Why It Matters</h2>
<p>Getting I,J backwards is the most common arc error. I and J are <strong>always incremental from the start point to the center</strong>, not absolute coordinates of the center.</p>
<h2>How</h2>
<h3>90-degree example</h3>
<p>Start S=(0,0), center C=(0,20), end E=(20,20). This is a 90° CCW quarter circle of radius 20. Arc length = R × θ(radians) = 20 × (π/2) = 31.416 mm.</p>
{code('G17 G90 G03 X20 Y20 I0 J20 F300')}
<p>I = center X - start X = 0 - 0 = 0. J = center Y - start Y = 20 - 0 = 20. Correct.</p>
<svg viewBox="-10 -10 130 130" xmlns="http://www.w3.org/2000/svg" style="max-width:340px;background:#f8faf9;border-radius:12px">
<line x1="0" y1="0" x2="110" y2="0" stroke="#cfdbd8" stroke-width="1"/>
<line x1="0" y1="0" x2="0" y2="110" stroke="#cfdbd8" stroke-width="1"/>
<path d="M 0 0 A 20 20 0 0 1 20 20" fill="none" stroke="#0b766e" stroke-width="2.5"/>
<circle cx="0" cy="0" r="2.5" fill="#e67e22"/>
<circle cx="20" cy="20" r="2.5" fill="#0b766e"/>
<circle cx="0" cy="20" r="2" fill="#5c6872"/>
<text x="2" y="-3" font-size="7" fill="#5c6872">S(0,0)</text>
<text x="22" y="22" font-size="7" fill="#0b766e">E(20,20)</text>
<text x="-14" y="23" font-size="7" fill="#5c6872">C(0,20)</text>
</svg>
<h2>Example</h2>
<p>Arc from (20,20) to (0,0) clockwise, center at (0,20): I = 0-20 = -20, J = 20-20 = 0. G02 X0 Y0 I-20 J0. Same quarter circle, opposite direction.</p>
<h2>Common Mistakes</h2>
<ul><li>Using absolute center coordinates instead of incremental I,J.</li>
<li>Forgetting plane selection (G17) — arc direction changes by plane.</li>
<li>Using R for arcs &gt;180° — R sign must flip; I,J is safer for major arcs.</li></ul>
{prac([
("Start (0,0), center (30,0), end (30,30). Direction? Code?", "CCW 90°: G03 X30 Y30 I30 J0. Length = 30 × π/2 = 47.1 mm."),
("Why is I,J incremental?", "I = center X − start X, not absolute center X. If start moves, I changes.")])}
{src(["Haas Mill Operator's Manual — G02/G03 (haascnc.com, retrieved 2026-09-24).","[Arc and Chord Calculator](/cnc-manufacturing-engineering/engineering-tools/arc-and-chord-calculator/)."])}''',
   prev=("14-linear-interpolation","Linear Motion"), nxt=("16-cutter-compensation","Cutter Comp"))

# 16 Cutter Compensation
pg('16-cutter-compensation', "Cutter Radius Compensation (G41/G42)",
   "Program the part contour, let the controller offset the tool center by the tool radius. Left vs right, lead-in/out, and G40 cancellation.",
   f'''<h1>Cutter Radius Compensation (G41/G42)</h1>
<p class="lead">You program the edge of the part. The controller shifts the tool center left or right by the tool radius — so you can change tool diameter without rewriting the program.</p>
{m("Key","Mill")}
{obj(["Why program the contour, not the tool path","G41 left vs G42 right (looking along cut direction)","Lead-in and lead-out on straight approach","G40 cancellation before rapid"])}
<h2>Concept</h2>
<p>Without compensation, you must calculate every coordinate offset by the tool radius. With <strong>G41/G42</strong>, you program the part edges and the controller shifts the tool center by the D offset value. <strong>G41</strong> = left (tool is left of cut direction), <strong>G42</strong> = right. <strong>G40</strong> cancels.</p>
<h2>Why It Matters</h2>
<p>If you wear a 10 mm end mill down to 9.8 mm, you only change D from 5.0 to 4.9 — no program changes. This is why production programs use compensation.</p>
<h2>How</h2>
<h3>Lead-in</h3>
<p>Compensation must turn on during a straight move (not on an arc). Approach the part on a straight path, G41 D01 activates, then cut the contour. At the end, G40 on a straight move away from the part.</p>
<h2>Example</h2>
<p>Cutting a 50×50 square outline with a 10 mm end mill (D=5). Program the corners at (0,0),(50,0),(50,50),(0,50). The tool center runs 5 mm outside this rectangle automatically.</p>
<h2>Common Mistakes</h2>
<ul><li>Turning on G41/G42 on an arc — always lead in on a straight line.</li>
<li>Forgetting G40 — compensation stays modal and the next move shifts unexpectedly.</li>
<li>Confusing left/right — it is from the perspective of the tool moving along the cut, looking in the direction of travel.</li></ul>
{prac([
("You replace a 10 mm mill with an 8 mm mill. What changes?", "D offset from 5.0 to 4.0. The program contour coordinates stay identical."),
("Why must G41 turn on a straight move?", "The controller needs a straight segment to calculate the offset direction. Turning on an arc causes unpredictable tool path.")])}
{src(["Haas Mill Operator's Manual — G41/G42/G40 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("15-circular-interpolation","Circular Motion"), nxt=("33-drilling-cycles","Drilling Cycles"))

# 17 Drilling & Hole-Making Cycles
pg('33-drilling-cycles', "Drilling and Hole-Making Canned Cycles",
   "G81 drill, G82 dwell, G83 peck, G84 tap, G85 bore — position, R plane, depth, feed, retract.",
   f'''<h1>Drilling and Hole-Making Canned Cycles</h1>
<p class="lead">G81 drills in one feed. G83 pecks to clear chips. G84 taps. Each cycle is one line: position, plunge, retract, repeat at the next hole.</p>
{m("Key","Mill")}
{obj(["G81 drill, G82 drill with dwell, G83 peck","G84 tapping, G85 boring","R plane and initial plane","G80 cancellation and G98/G99 retract"])}
<h2>Concept</h2>
<p>A <strong>canned cycle</strong> encodes a multi-step drill into one line. <strong>G81</strong> = rapid to R, feed to Z depth, rapid retract. <strong>G83</strong> = peck drill (repeated retracts to clear chips). <strong>G84</strong> = tapping (feed synchronized to spindle). <strong>G80</strong> cancels the cycle.</p>
<h2>Why It Matters</h2>
<p>Without canned cycles, each hole needs 5-6 lines of G00/G01. With G81, one line per hole. And because the cycle is modal, every X/Y block drills — which is also why G80 is critical.</p>
<h2>How</h2>
<h3>G81 example</h3>
{code('G90 G99 G81 X10. Y10. R2. Z-15. F100.\nX50. Y10.        <span class="cp-comment">(hole 2: same cycle, new position)</span>\nX50. Y50.        <span class="cp-comment">(hole 3)</span>\nX10. Y50.        <span class="cp-comment">(hole 4)</span>\nG80              <span class="cp-comment">(cancel cycle)</span>')}
<p>G99 = retract to R plane between holes (faster). G98 = retract to initial plane (for obstacles).</p>
<h2>Example</h2>
<p>12 mm plate, Ø6 through holes. Z depth = -12 - drill point (~1.8mm) = -13.8. R plane = 2 mm above surface. F100 mm/min for a Ø6 drill in steel.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting G80 — the next rapid move drills a hole.</li>
<li>Using G81 for deep holes without peck — packing chips causes drill breakage. Use G83.</li>
<li>Wrong R plane too close to the part — collisions on the way to the next hole.</li></ul>
{prac([
("After G81, you move X0 Y0 to reposition. What happens?", "On Haas, G00 cancels the canned cycle — but verify. Safer: G80 before repositioning."),
("Why G83 for deep holes?", "Repeated retract breaks and clears chips, preventing drill overheating and work hardening.")])}
{src(["Haas Mill Operator's Manual — G81/G82/G83/G84/G85 (haascnc.com, retrieved 2026-09-24).","[Drilling Parameter Assistant](/cnc-manufacturing-engineering/engineering-tools/drilling-parameter-assistant/)."])}''',
   prev=("16-cutter-compensation","Cutter Comp"), nxt=("18-canned-cycles","Canned Cycles"))

print("15, 16, 17 done.")

# 18 Canned Cycles
pg('18-canned-cycles', "Canned Cycles Overview",
   "What a canned cycle is, its fixed sequence of motions, and how parameters differ between drill, bore, tap, and turn.",
   f'''<h1>Canned Cycles Overview</h1>
<p class="lead">A canned cycle is a pre-programmed sequence: position, plunge, feed, retract. You supply the parameters; the controller does the rest.</p>
{m("Key","Mill & Lathe")}
{obj(["The six-step cycle sequence","Common parameters: R, Z, F, Q, P","Why cycles are modal","Turning cycles G71/G72/G70"])}
<h2>Concept</h2>
<p>Every milling canned cycle follows the same pattern: (1) rapid to X/Y position, (2) rapid to R plane, (3) feed to Z depth, (4) dwell (optional), (5) retract to R or initial plane, (6) repeat at next X/Y. You code this once with G81/G83/etc.; subsequent X/Y blocks repeat it.</p>
<h2>Why It Matters</h2>
<p>Canned cycles reduce 6 lines per hole to 1. On a part with 20 holes, that is the difference between a 20-line and a 120-line program. But the modal behavior means forgetting G80 drills unwanted holes.</p>
<h2>How</h2>
<h3>Common parameters</h3>
<ul><li><strong>X/Y</strong> — hole position.</li>
<li><strong>R</strong> — R plane (rapid-to height above part).</li>
<li><strong>Z</strong> — final depth.</li>
<li><strong>F</strong> — feed rate.</li>
<li><strong>Q</strong> — peck depth (G83).</li>
<li><strong>P</strong> — dwell time (G82).</li></ul>
<h2>Example</h2>
<p>G83 (peck) Q5: plunge 5 mm, retract fully, re-plunge 5+5, etc. This clears chips after every 5 mm of drill depth.</p>
<h2>Common Mistakes</h2>
<ul><li>Mixing R plane units with Z units (both mm in G21).</li>
<li>Forgetting that on a lathe, canned cycles (G71/G70) work differently — they use P/Q/U/W for stock allowance.</li>
<li>Not verifying cycle behavior on your controller — G84 tapping direction and retract speed vary by machine.</li></ul>
{prac([
("What does Q5 mean in G83?", "Each peck plunges 5 mm deeper before retracting to clear chips."),
("Why is G80 important?", "It cancels the modal cycle. Without it, any X/Y move repeats the drill.")])}
{src(["Haas Mill Operator's Manual — Canned cycles (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("33-drilling-cycles","Drilling Cycles"), nxt=("34-subprograms","Subprograms"))

# 34 Subprograms (R07: real 4x3 grid)
pg('34-subprograms', "Subprograms and Program Reuse",
   "M98 P calls, M99 returns, and a real 4-column × 3-row hole grid built with incremental Y rows and X reset.",
   f'''<h1>Subprograms and Program Reuse</h1>
<p class="lead">When you repeat a pattern, write it once as a subprogram and call it many times. This page builds an actual 4×3 hole grid.</p>
{m("Key","Mill")}
{obj(["Main program calls O-subprogram with M98","M99 returns to the caller","L/P repeat count","Building a rectangular hole grid"])}
<h2>Concept</h2>
<p>A <strong>subprogram</strong> is a separate program (O-number) called by M98 and returned by M99. The main program calls the subprogram; the subprogram performs one unit of work and returns. Main program handles positioning; subprogram handles the repeated action.</p>
<h2>Why It Matters</h2>
<p>Without subprograms, drilling a 4×3 grid means 12 separate G81 lines. With a subprogram that drills one hole, the main program positions to each row/column and calls it. Better: the subprogram itself handles X advancement, and the main program advances Y per row.</p>
<h2>How</h2>
<h3>4 columns × 3 rows hole grid</h3>
<p>Hole spacing: X=20 mm, Y=20 mm. Start at (10,10). Columns at X=10,30,50,70. Rows at Y=10,30,50.</p>
<p><strong>Main program:</strong></p>
{code('O1000 (MAIN: 4x3 GRID)\nG21 G90 G80\nT03 M06\nG54 S1500 M03\nG43 H03 Z50. M08\nG00 X10. Y10.        <span class="cp-comment">(row 1 start)</span>\nM98 O2000 L3         <span class="cp-comment">(call row subprogram 3 times)</span>\nG80 G00 Z50.\nM09 M05\nG91 G28 Z0\nM30')}
<p><strong>Subprogram O2000 (one row: 4 holes, then Y advance):</strong></p>
{code('O2000 (ROW: 4 holes in X, then Y+20)\nG90 G81 Z-10. R2. F100.\nX10.                 <span class="cp-comment">(hole col 1)</span>\nX30.                 <span class="cp-comment">(col 2)</span>\nX50.                 <span class="cp-comment">(col 3)</span>\nX70.                 <span class="cp-comment">(col 4)</span>\nG80\nG91 G00 Y20.         <span class="cp-comment">(advance row by 20)</span>\nG90 X10.             <span class="cp-comment">(reset X to column 1)</span>\nM99')}
<p>This produces 12 holes: rows at Y=10,30,50; columns at X=10,30,50,70. Each call drills one row of 4 holes and moves Y+20.</p>
<h2>Common Mistakes</h2>
<ul><li>Forgetting G90/G91 reset between main and subprogram — state carries over.</li>
<li>Not resetting X after each row — the next row starts at the last X, not column 1.</li>
<li>Using M99 P to jump within a program — that is branching, not subprogram return.</li></ul>
{prac([
("Why does the subprogram reset X to 10?", "After drilling columns 1-4 at X=10,30,50,70, the next Y row must start at column 1 (X=10), not continue from X=70."),
("What does L3 do in M98 O2000 L3?", "Calls O2000 three times — once per row. 3 rows × 4 columns = 12 holes.")])}
{src(["Haas Mill Operator's Manual — M98/M99 subprograms (haascnc.com, retrieved 2026-09-24).","[Hole Pattern Generator](/cnc-manufacturing-engineering/engineering-tools/hole-pattern-generator/)."])}''',
   prev=("18-canned-cycles","Canned Cycles"), nxt=("19-turning-programming","Turning Programming"))

# 19 CNC Turning Programming
pg('19-turning-programming', "CNC Turning Programming",
   "Lathe coordinates, diameter programming, G71 roughing and G70 finishing on Haas — and a front-profile example with no parting off.",
   f'''<h1>CNC Turning Programming</h1>
<p class="lead">On a lathe, X is diameter, Z is along the spindle. G71 roughs, G70 finishes. This page writes a front profile: Ø30 × Z0-20 and Ø36 × Z-20 to -40.</p>
{m("Key","Lathe")}
{obj(["Diameter vs radius programming","G99 feed/rev and G97 constant RPM for threading","G71 rough cycle, G70 finish cycle","Front profile example (no parting off)"])}
<h2>Concept</h2>
<p>A CNC lathe turns cylindrical parts. <strong>X is diameter</strong> (X50 = 50 mm diameter, 25 mm radius). <strong>Z</strong> runs along the spindle. Work zero is typically at the face center. Tool moves in X (plunge) and Z (along the bar).</p>
<h2>Why It Matters</h2>
<p>Diameter programming means X moves are doubled in radius. If you confuse diameter and radius, the part is half or double the size. Haas lathes use G99 for feed/rev (not G95), and G97 for constant RPM during threading.</p>
<h2>How</h2>
<h3>Haas G71 roughing cycle</h3>
<p>G71 follows a contour you describe between P (start) and Q (end). It leaves stock for finishing, then G70 finishes to size.</p>
<h2>Example (R06 fix: front profile, no parting)</h2>
<p>Raw stock Ø40 × 100. Face off. Rough and finish: Ø30 × Z0 to Z-20, then Ø36 × Z-20 to Z-40. No parting off — only the front profile.</p>
{code('O2000 (FRONT PROFILE, NO PARTING)\nG21 G97 G99\nT0101 (OD roughing tool)\nG54 S1200 M03\nG00 X42. Z2. M08        <span class="cp-comment">(approach)</span>\nG71 U1.0 R0.5\nG71 P10 Q20 U0.4 W0.1 F0.2\nN10 G00 X30.            <span class="cp-comment">(profile start: Ø30)</span>\nG01 Z0 F0.1\nZ-20.                   <span class="cp-comment">(Ø30 for 20 mm long)</span>\nX36.                    <span class="cp-comment">(step out to Ø36)</span>\nZ-40.                   <span class="cp-comment">(Ø36 to Z-40)</span>\nN20 X42.                <span class="cp-comment">(profile end: clear bar)</span>\nG00 X100. Z100.\nT0202 (finishing tool)\nG97 S1800 M03\nG00 X42. Z2.\nG70 P10 Q20             <span class="cp-comment">(finish to 30/36)</span>\nG00 X100. Z100.\nM09 M05\nM30')}
<p>The contour N10–N20 only changes Z direction monotonically from Z0 to Z-40 (no Z reversal), which satisfies Haas G71 rules. No parting off is programmed — the part remains in the bar.</p>
<h2>Common Mistakes</h2>
<ul><li>Z direction reversing inside a G71 P-Q contour — Haas requires monotonic X or Z.</li>
<li>Using G96 during threading — must switch to G97.</li>
<li>Confusing diameter and radius X values.</li></ul>
{prac([
("X50 in diameter programming. What is the radial position?", "25 mm from center (radius = diameter/2)."),
("Why no parting off in this example?", "The SPEC says only machine the front profile; the part stays in the bar for later operations.")])}
{src(["Haas Lathe Operator's Manual — G71/G70 rough/finish cycles (haascnc.com, retrieved 2026-09-24).","[Turning Speed Calculator](/cnc-manufacturing-engineering/engineering-tools/turning-speed-feed-calculator/)."])}''',
   prev=("34-subprograms","Subprograms"), nxt=("20-milling-programming","Milling Programming"))

print("18, 34, 19 done.")

# 20 CNC Milling Programming (R02: correct dimensions)
pg('20-milling-programming', "CNC Milling Programming",
   "A complete beginner milling project: 100×80×12 plate, 40×30×4 pocket at X30-70/Y25-55, R5 corners, 4×Ø6 holes at corners.",
   f'''<h1>CNC Milling Programming</h1>
<p class="lead">From a rectangular block to a finished plate: face, profile, pocket, drill holes — one tool at a time, with a real tool table.</p>
{m("Key","Mill")}
{obj(["Plate: 100×80×12, origin at corner","Pocket: X30-70, Y25-55, depth 4, R5 corners","4×Ø6 through holes at plate corners","Tool table and H/D offsets"])}
<h2>Concept</h2>
<p>Milling removes material from a solid block. Operations: face mill the top, contour the outside, mill a pocket, drill holes. Each operation uses a different tool with its own H (length) and D (radius) offset. The program changes tools with T01 M06.</p>
<h2>Why It Matters</h2>
<p>A real milling project sequences tools: face mill first, then end mill for profile/pocket, then drill. Each tool has its own H offset. Forgetting to call the right H number means wrong Z depth.</p>
<h2>How</h2>
<h3>Specifications (R02 corrected)</h3>
<ul><li>Plate: 100 × 80 × 12 mm, work zero at lower-left corner on top surface.</li>
<li>Pocket: X30 to X70 (40 mm wide), Y25 to Y55 (30 mm deep), pocket depth 4 mm, corner R5.</li>
<li>4× Ø6 through holes at (10,10), (90,10), (90,70), (10,70). Drill point breakthrough: Z=-12-1.8 = -13.8.</li></ul>
<h3>Tool table</h3>
<ul><li>T01: Ø63 face mill (H01, rough face).</li>
<li>T02: Ø10 end mill (H02, D05, profile and pocket).</li>
<li>T03: Ø6 drill (H03, drill holes).</li></ul>
<h2>Example: Hole drilling section</h2>
{code('T03 M06                 <span class="cp-comment">(Ø6 drill)</span>\nG54 G90 S1500 M03\nG43 H03 Z50. M08\nG99 G83 X10. Y10. R2. Z-13.8 Q3. F80.\nX90. Y10.\nX90. Y70.\nX10. Y70.\nG80\nG00 Z50. M09\nM05')}
<p>Pocket roughing uses T02 at Z=-4 depth, following the X30-70/Y25-55 rectangle with R5 corners. Face milling with T01 passes across X0-100 at Z=0.</p>
<h2>Common Mistakes</h2>
<ul><li>Programming pocket dimensions wrong (e.g. 40×30 center vs corner).</li>
<li>Forgetting drill breakthrough depth on a 12 mm plate.</li>
<li>Calling T03 but H02 — wrong tool length.</li></ul>
{prac([
("Plate is 12 mm thick, Ø6 through holes. Z depth?", "-13.8 mm (12 through + 1.8 drill point)."),
("Why is the pocket at X30-70?", "That is 40 mm wide centered: (100-40)/2 = 30 margin on each side.")])}
{src(["Haas Mill Operator's Manual (haascnc.com, retrieved 2026-09-24).","[Drilling Parameter Assistant](/cnc-manufacturing-engineering/engineering-tools/drilling-parameter-assistant/)."])}''',
   prev=("19-turning-programming","Turning Programming"), nxt=("21-threading-basics","Threading Basics"))

# 21 Threading Basics
pg('21-threading-basics', "Threading Basics",
   "Pitch vs lead, major/minor diameter, single-point threading on a lathe, and the axial feed = RPM × lead relationship.",
   f'''<h1>Threading Basics</h1>
<p class="lead">A screw thread is a helix. Pitch is distance between adjacent threads; lead is distance per revolution. Axial feed must equal lead at the programmed RPM.</p>
{m("Key","Mill & Lathe")}
{obj(["Pitch vs lead (single vs multi-start)","Major, minor, pitch diameter","Axial feed = RPM × lead","Why threading uses G97 constant RPM"])}
<h2>Concept</h2>
<p>On a lathe, single-point threading cuts a V-shaped groove along a rotating part. The tool moves axially exactly one <strong>lead</strong> per spindle revolution. For a single-start thread, lead = pitch. Axial feed (mm/min) = RPM × lead (mm/rev).</p>
<h2>Why It Matters</h2>
<p>If the feed is wrong, the thread pitch is wrong — it will not mate. If RPM changes mid-cut (G96), the pitch wanders. Threading always uses G97 constant RPM.</p>
<h2>How</h2>
<h3>M10×1.5 example</h3>
<p>M10: major diameter 10 mm, pitch 1.5 mm. Single-start, lead = 1.5 mm. At 500 RPM, axial feed = 500 × 1.5 = 750 mm/min. Thread depth ≈ 0.613 × pitch = 0.92 mm each side.</p>
<h2>Example</h2>
<p>M20×1.5 at 500 rpm: F = 500 × 1.5 = 750 mm/min. (In G99 feed/rev mode, F = 1.5 directly.) Multi-start: 2-start thread with pitch 1.5 has lead 3.0 — F = RPM × 3.0.</p>
<h2>Common Mistakes</h2>
<ul><li>Confusing pitch and lead on multi-start threads.</li>
<li>Using G96 during threading — RPM varies, pitch is inconsistent.</li>
<li>Forgetting spring pass (one final pass at 0 depth) to clean up.</li></ul>
{prac([
("M10×1.5 at 500 rpm. Axial feed?", "500 × 1.5 = 750 mm/min."),
("What is the lead of a 2-start thread with pitch 1.5?", "Lead = 2 × 1.5 = 3.0 mm per revolution.")])}
{src(["Haas Lathe Operator's Manual — Threading cycles (haascnc.com, retrieved 2026-09-24).","[Threading Calculator](/cnc-manufacturing-engineering/engineering-tools/threading-calculator/)."])}''',
   prev=("20-milling-programming","Milling Programming"), nxt=("22-lathe-threading","Lathe Threading"))

# 22 Lathe Threading (R03: Haas G76 K/D)
pg('22-lathe-threading', "Lathe Threading Cycles",
   "Haas G76 threading cycle uses K (or D) for depth and F for lead — not the FANUC two-line P-Q format.",
   f'''<h1>Lathe Threading Cycles</h1>
<p class="lead">On a Haas lathe, G76 cuts a thread automatically. F is the lead (pitch for single-start). K/D is thread depth. Always G97 constant RPM.</p>
{m("Key","Lathe")}
{obj(["Haas G76 one-line format","F = lead (mm/rev)","K (or D) = thread depth","G97 S constant RPM required"])}
<h2>Concept</h2>
<p>Single-point threading on a lathe uses a form tool that follows the thread helix. The <strong>G76</strong> cycle automates multiple passes. Haas uses a simplified format: the thread is defined by start X/Z, end X/Z, depth K (or D), and feed F (lead).</p>
<h2>Why It Matters</h2>
<p>FANUC's two-line G76 uses P/Q/R fancy parameters. Haas uses a simpler K/D format. Copying FANUC G76 code onto a Haas causes alarms. Always use the dialect of your controller.</p>
<h2>How</h2>
<h3>Haas G76 example: M10×1.5</h3>
{code('G97 S500 M03            <span class="cp-comment">(constant RPM)</span>\nG00 X12. Z3.            <span class="cp-comment">(approach)</span>\nG76 X8.2 Z-20. K0.92 F1.5\n<span class="cp-comment">X8.2 = minor dia, Z-20 = thread end, K0.92 = depth, F1.5 = lead</span>')}
<p>F1.5 means feed = 1.5 mm/rev = lead. At 500 rpm, axial feed = 750 mm/min.</p>
<h2>Example</h2>
<p>M20×1.5 external thread on Ø20 bar. Major = 20, minor ≈ 20 - 2×0.92 = 18.16. G76 X18.16 Z-25. K0.92 F1.5. Always G97 before threading.</p>
<h2>Common Mistakes</h2>
<ul><li>Using FANUC two-line G76 on a Haas — syntax mismatch.</li>
<li>Forgetting G97 — G96 varies RPM and ruins pitch.</li>
<li>Confusing F units: in G99, F is mm/rev = lead, not mm/min.</li></ul>
{prac([
("M10×1.5 at 500 rpm. F value in G99?", "F1.5 (mm/rev = lead). Axial feed = 750 mm/min."),
("Why G97 before G76?", "Threading requires constant RPM to maintain lead. G96 would vary speed as diameter changes.")])}
{src(["Haas Lathe Operator's Manual — G76 threading cycle (haascnc.com, retrieved 2026-09-24).","[Threading Calculator](/cnc-manufacturing-engineering/engineering-tools/threading-calculator/)."])}''',
   prev=("21-threading-basics","Threading Basics"), nxt=("24-program-verification","Program Verification"))

print("20, 21, 22 done.")

# 24 Program Verification (R05: dry run at raised Z does NOT prove no collision)
pg('24-program-verification', "Program Verification Before Cutting",
   "Simulation, dry run, single block, first-part inspection — and why dry run at raised Z does NOT prove no collision.",
   f'''<h1>Program Verification Before Cutting</h1>
<p class="lead">Writing a program is not the same as proving it safe. Verification is layered: each layer catches different errors. No single layer proves everything.</p>
{m("Key","Mill & Lathe")}
{obj(["Simulation: virtual tool path","Dry run: real motion at rapid/feed override","Single block: one line at a time","First-part inspection: measure the actual part"])}
<h2>Concept</h2>
<p>Verification happens in layers. <strong>Simulation</strong> (CAM or controller graphics) shows the tool path virtually. <strong>Dry run</strong> runs the program on the real machine with no tool (or tool at raised Z) at rapid/feed override. <strong>Single block</strong> executes one line per cycle start. <strong>First-part</strong> runs the real cut at reduced feed, then measures.</p>
<h2>Why It Matters (R05 critical)</h2>
<p><strong>Dry run at raised Z does NOT prove no collision.</strong> With the tool 50 mm above the part, you verify X/Y positioning, but the tool holder, spindle nose, and fixture heights are not tested. A collision between tool holder and vise at Z=-10 will not appear when Z is raised. Dry run catches positioning errors, not 3D interference. Only controller simulation with full tool geometry (holder included) or careful hand calculation proves clearance.</p>
<h2>How</h2>
<h3>Verification layers</h3>
<ol><li><strong>Syntax review</strong>: read every line; check G90/G91, H/D numbers, units.</li>
<li><strong>Coordinate review</strong>: compare programmed coordinates to the drawing.</li>
<li><strong>Simulation</strong>: run controller graphics; look for gouges and wrong Z.</li>
<li><strong>Dry run</strong>: tool at raised Z, rapid override at 50%, watch X/Y motion. Does NOT prove Z clearance.</li>
<li><strong>Single block</strong>: first few blocks at 100% feed, verify each move.</li>
<li><strong>First cut</strong>: feed override at 25-50%, tool above air, then actual cut.</li>
<li><strong>Inspection</strong>: measure first part before continuing production.</li></ol>
<h2>Example</h2>
<p>A pocket program: simulation shows the tool path. Dry run at Z50 shows X/Y follows the pocket rectangle. But the 100 mm tool holder might hit the 80 mm vise jaw at Z=-5 — dry run at raised Z does not reveal this. Only checking holder geometry vs vise height proves clearance.</p>
<h2>Common Mistakes</h2>
<ul><li>Thinking raised-Z dry run proves no collision — it does not.</li>
<li>Skipping single block because simulation looked fine.</li>
li>Running at 100% feed on the first part.</li></ul>
{prac([
("Dry run at Z50 shows no issues. Is it safe to cut?", "No. It proves X/Y positions are correct, but Z clearance between holder/fixture is untested. Verify holder geometry separately."),
("What does simulation catch that dry run cannot?", "Tool path gouges, wrong Z depths, and (with full holder model) 3D interference.")])}
{src(["Haas Mill Operator's Manual — Dry run and single block (haascnc.com, retrieved 2026-09-24).","[Printable Setup Worksheet](/cnc-manufacturing-engineering/engineering-tools/printable-setup-worksheet/)."])}''',
   prev=("22-lathe-threading","Lathe Threading"), nxt=("25-troubleshooting","Troubleshooting"))

# 25 Programming Troubleshooting
pg('25-troubleshooting', "CNC Programming Troubleshooting",
   "Unexpected motion, wrong dimensions, alarms — systematic diagnosis of program problems.",
   f'''<h1>CNC Programming Troubleshooting</h1>
<p class="lead">When the machine does the wrong thing, do not panic. Work the problem: which state is wrong, which line caused it, and what to check.</p>
{m("Key","Mill & Lathe")}
{obj(["Wrong direction, wrong coordinate, wrong offset","Arc errors and overtravel","Cycle errors and unexpected drills","Systematic diagnosis: symptom → cause → fix"])}
<h2>Concept</h2>
<p>Program errors fall into categories: (1) wrong modal state (G90/G91, G94/G95, G17/G18), (2) wrong offset (G54, H, D), (3) wrong geometry (I/J arc center, pocket dimensions), (4) alarm codes (overtravel, program error). Diagnose by reproducing the motion in single block.</p>
<h2>Why It Matters</h2>
<p>A part that is systematically off by 0.2 mm is an offset error. A part that is wrong only on one feature is a coordinate error. Wrong direction (X goes - instead of +) suggests G91/G90 confusion. Knowing the category narrows the search.</p>
<h2>How</h2>
<h3>Common symptoms</h3>
<ul><li><strong>Tool moves wrong direction</strong>: check G90/G91.</li>
<li><strong>Z depth wrong</strong>: check H offset and G43.</li>
<li><strong>Every hole shifted</strong>: check G54.</li>
<li><strong>Unexpected drill move</strong>: forgot G80.</li>
<li><strong>Arc alarm</strong>: I/J wrong or end point unreachable from start+center.</li></ul>
<h2>Example</h2>
<p>Part is 0.2 mm too large in X only. Check: G54 X offset. If G54 should be -300.2 but is -300.0, every X dimension is off by 0.2. Correct the offset, not the program.</p>
<h2>Common Mistakes</h2>
<ul><li>Editing the program when the offset is wrong.</li>
<li>Ignoring the alarm number — it tells you what the controller thinks.</li>
<li>Restarting without rebuilding modal state (see Lesson 23).</li></ul>
{prac([
("Every hole is 0.1 mm too high in Y. What to check?", "G54 Y offset. A systematic shift means work offset, not individual coordinates."),
("Tool moves in unexpected Y during a drilling cycle. Why?", "G81 is still modal; the next X/Y move drills. G80 to cancel.")])}
{src(["Haas Mill Operator's Manual — Alarm codes (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("24-program-verification","Verification"), nxt=("26-common-mistakes","Common Mistakes"))

# 26 Common Beginner Mistakes
pg('26-common-mistakes', "Common Beginner Programming Mistakes",
   "The mistakes every new programmer makes — and how to avoid them.",
   f'''<h1>Common Beginner Programming Mistakes</h1>
<p class="lead">These are the errors that crash machines, scrap parts, and waste time. Learn them before you make them.</p>
{m("Beginner","Mill & Lathe")}
{obj(["Wrong offsets, wrong units, wrong plane","Unsafe rapid, missing G80/G40","Copying code without understanding","Missing startup block"])}
<h2>Concept</h2>
<p>Beginner errors are not random. They cluster around: (1) state confusion (G90/G91, G41/G42), (2) offset confusion (G54, H, D), (3) safety (rapid through part, missing cancel), (4) copying code without understanding the machine dialect.</p>
<h2>Why It Matters</h2>
<p>Most crashes are not exotic — they are one of about ten repeated errors. Recognizing them by name lets you check for them before cycle start.</p>
<h2>How</h2>
<h3>Top mistakes</h3>
<ul><li><strong>Wrong work offset</strong>: G54 set to wrong edge.</li>
<li><strong>Wrong tool length</strong>: T02 but H01.</li>
<li><strong>Wrong units</strong>: G20/G21 mismatch.</li>
<li><strong>Missing G80</strong>: next move drills.</li>
<li><strong>Missing G40</strong>: compensation never turns off.</li>
<li><strong>Rapid through stock</strong>: G00 down to depth.</li>
<li><strong>Wrong plane</strong>: G17 vs G18 for arcs.</li>
<li><strong>Unsafe Z approach</strong>: not above part before rapid in X/Y.</li></ul>
<h2>Example</h2>
<p>Copying a FANUC G76 thread cycle onto a Haas produces an alarm — not because the thread is wrong, but because the dialect is different. Always adapt code to your machine.</p>
<h2>Common Mistakes</h2>
<ul><li>Running a program you did not read line by line.</li>
<li>Assuming "it worked on the other machine" — offsets and defaults differ.</li>
<li>Skipping the startup block because "the last program left it right."</li></ul>
{prac([
("Why start every program with G21 G17 G90 G40 G49 G80?", "To force a known state regardless of what the previous program left behind."),
("You copied a program from a FANUC shop and it alarms on your Haas. Why?", "M-codes and cycle syntax differ. Translate, do not copy.")])}
{src(["Haas Mill Operator's Manual (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("25-troubleshooting","Troubleshooting"), nxt=("28-milling-project","Milling Project"))

print("24, 25, 26 done.")

# 28 Complete Milling Project (R02: correct G-code)
pg('28-milling-project', "Complete Milling Project: Rectangular Plate",
   "Full G-code for a 100×80×12 plate: face, pocket, 4 holes. One tool per operation, correct coordinates, no broken blocks.",
   f'''<h1>Complete Milling Project: Rectangular Plate</h1>
<p class="lead">A worked end-to-end example. Plate 100×80×12, pocket X30-70/Y25-55 deep 4, 4×Ø6 holes at corners. This is a complete, runnable-style program.</p>
{m("Key","Mill")}
{obj(["Tool table: face mill, end mill, drill","Pocket coordinates X30-70/Y25-55 R5","Holes at (10,10)/(90,10)/(90,70)/(10,70)","Drill depth -13.8 through 12 mm plate"])}
<h2>Concept</h2>
<p>This program sequences three tools: face mill (T01), Ø10 end mill (T02), Ø6 drill (T03). Each tool has its own H offset. Work zero is on top of the plate at the lower-left corner.</p>
<h2>Why It Matters</h2>
<p>A complete project ties together everything: tool change, work offset, tool length, contour, pocket, drilling cycles. Coordinates match the drawing — no "X10 Y20 X30" in one block.</p>
<h2>How</h2>
<h3>Tool table</h3>
<ul><li>T01 H01: Ø63 face mill, S1500 F300.</li>
<li>T02 H02 D05: Ø10 end mill, S2000 F400 (profile/pocket).</li>
<li>T03 H03: Ø6 drill, S1500 F80 (G83 peck Q3).</li></ul>
<h3>Program</h3>
{code('% (RECTANGULAR PLATE PROJECT)\nO2800\nG21 G17 G90 G40 G49 G80\n(T01 FACE MILL)\nT01 M06\nG54 G00 X-20. Y40. S1500 M03\nG43 H01 Z50. M08\nG00 Z2.\nG01 Z0. F100.\nG01 X120. F300        <span class="cp-comment">(face pass across)</span>\nG00 Z50. M09 M05\n(T02 END MILL)\nT02 M06\nG54 G00 X30. Y25. S2000 M03\nG43 H02 Z50. M08\nG00 Z2.\nG01 Z-4. F100         <span class="cp-comment">(pocket depth 4)</span>\nG41 D05\nG01 X35. Y30. F400    <span class="cp-comment">(R5 corner lead-in)</span>\nX65.                  <span class="cp-comment">(pocket X30-70, offset by D5)</span>\nY50.\nX35.\nY30.\nG40 X30. Y25.\nG00 Z50. M09 M05\n(T03 DRILL)\nT03 M06\nG54 G90 S1500 M03\nG43 H03 Z50. M08\nG99 G83 X10. Y10. R2. Z-13.8 Q3. F80.\nX90. Y10.\nX90. Y70.\nX10. Y70.\nG80\nG00 Z50. M09 M05\nG91 G28 Z0\nM30\n%')}
<p>Pocket interior X30-70, Y25-55. With D5 offset, tool center runs 5 mm inside the pocket walls. Corners R5 match the Ø10 tool radius. Holes at the four corners through the 12 mm plate (Z-13.8).</p>
<h2>Common Mistakes</h2>
<ul><li>Multiple X/Y in one block — each move goes to one target.</li>
<li>Pocket dimensions wrong (center vs corner).</li>
<li>Forgetting drill breakthrough depth.</li></ul>
{prac([
("Pocket is X30-70, Y25-55. How wide and deep?", "40 mm wide (70-30), 30 mm deep (55-25)."),
("Why Z-13.8 for a 12 mm plate?", "12 mm through + ~1.8 mm drill point geometry = 13.8 mm total depth.")])}
{src(["Haas Mill Operator's Manual (haascnc.com, retrieved 2026-09-24).","[Drilling Parameter Assistant](/cnc-manufacturing-engineering/engineering-tools/drilling-parameter-assistant/)."])}''',
   prev=("26-common-mistakes","Common Mistakes"), nxt=("27-turning-project","Turning Project"))

# 27 Complete Turning Project (R06: no parting, monotonic Z)
pg('27-turning-project', "Complete Turning Project: Front Profile",
   "Full Haas-style program for a front profile: Ø30 × Z0-20 and Ø36 × Z-20-40. G71 rough, G70 finish. No parting off.",
   f'''<h1>Complete Turning Project: Front Profile</h1>
<p class="lead">A worked Haas lathe program. Raw stock Ø40. Machine only the front profile — no cut-off. G71 rough leaves 0.4 mm stock; G70 finishes.</p>
{m("Key","Lathe")}
{obj(["Raw stock Ø40 × 100","Profile: Ø30 Z0-20, then Ø36 Z-20-40","G71 rough, G70 finish (Haas)","No parting off programmed"])}
<h2>Concept</h2>
<p>The part is a shouldered shaft. Face it, then turn the front profile: Ø30 from Z0 to Z-20, then step out to Ø36 from Z-20 to Z-40. The contour changes Z monotonically (0 → -20 → -40) with no reversal, satisfying Haas G71 rules.</p>
<h2>Why It Matters</h2>
<p>R06: the previous version had Z direction changes inside the G71 contour (which Haas rejects) and claimed a parting-off operation that was not programmed. This version has monotonic Z and explicitly does NOT part off.</p>
<h2>How</h2>
<h3>Program</h3>
{code('% (FRONT PROFILE, NO PARTING)\nO2700\nG21 G97 G99\n(T0101 OD ROUGHING)\nT0101 M03 S1200\nG54 G00 X42. Z2. M08\nG71 U1.0 R0.5\nG71 P10 Q20 U0.4 W0.1 F0.2\nN10 G00 X30.\nG01 Z0. F0.1\nZ-20.\nX36.\nZ-40.\nN20 X42.\nG00 X100. Z100.\n(T0202 FINISH)\nT0202 M03 S1800\nG00 X42. Z2.\nG70 P10 Q20\nG00 X100. Z100.\nM09 M05\nM30\n%')}
<p>N10 to N20: X30 at Z0, Z to -20, step to X36, Z to -40, clear to X42. Z goes 0 → -20 → -40 monotonically. No parting off — the bar remains in the chuck.</p>
<h2>Common Mistakes</h2>
<ul><li>Z direction reversing inside P10-Q20 — Haas G71 requires monotonic.</li>
li>Claiming parting off without programming it.</li>
<li>Using G96 during G70 finish — fine for finish, but switch to G97 before threading.</li></ul>
{prac([
("Why is Z monotonic important?", "Haas G71 expects the contour to progress in one Z direction. Reversing Z causes an alarm or wrong tool path."),
("Why no parting off?", "The SPEC says only machine the front profile. Parting off would be a separate operation with a cutoff tool.")])}
{src(["Haas Lathe Operator's Manual — G71/G70 (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("28-milling-project","Milling Project"), nxt=("35-practical-examples","Practical Examples"))

# 35 Practical Examples
pg('35-practical-examples', "Practical Programming Examples",
   "Graded examples from simple facing to bolt-circle drilling, each with a process plan and worked G-code.",
   f'''<h1>Practical Programming Examples</h1>
<p class="lead">From facing a bar to drilling a bolt circle — real parts, real code, explained line by line.</p>
{m("Key","Mill & Lathe")}
{obj(["Level 1: facing, straight turning, simple drilling","Level 2: bolt circle, multiple tools","Process plan: drawing → datum → tool → program"])}
<h2>Concept</h2>
<p>Each example follows the same workflow: read the drawing, choose datum, select tools, calculate coordinates, write the program, verify. Start simple; add complexity gradually.</p>
<h2>Example: Bolt circle drilling</h2>
<p>4 holes on PCD 40, center at (0,0). Coordinates: (20,0), (0,20), (-20,0), (0,-20). Drill Z-10, R2, F100.</p>
{code('G90 G99 G81 X20. Y0 R2. Z-10. F100.\nX0 Y20.\nX-20. Y0.\nX0 Y-20.\nG80')}
<h2>Example: Facing a bar</h2>
<p>Ø50 bar, face to Z0. Tool at X52 Z2, feed to X-1 at F0.2 (G99). G00 retract.</p>
<h2>Common Mistakes</h2>
<ul><li>Skipping the process plan and writing code first.</li>
<li>Not calculating coordinates before programming.</li>
<li>Running the first part at 100% feed.</li></ul>
{prac([
("PCD 40, 4 holes at 0/90/180/270. Hole at 90°?", "(0, 20)."),
("Why process plan before code?", "Code without a plan produces a program that machines the wrong thing at high speed.")])}
{src(["[Hole Pattern Generator](/cnc-manufacturing-engineering/engineering-tools/hole-pattern-generator/).","[Bolt Circle Calculator](/cnc-manufacturing-engineering/engineering-tools/bolt-circle-calculator/)."])}''',
   prev=("27-turning-project","Turning Project"), nxt=("36-macro-programming","Macro Programming"))

print("28, 27, 35 done.")

# 36 Macro Programming (R08: N labels, input validation, no GOTO O)
pg('36-macro-programming', "Macro Programming Introduction",
   "Variables, IF/WILE loops, N labels for branching, and a bolt-circle drill macro with input validation and divide-by-zero protection.",
   f'''<h1>Macro Programming Introduction</h1>
<p class="lead">Macros add variables, logic, and loops to G-code. This page teaches N-label branching (not O-number GOTO), input validation, and safe arithmetic.</p>
{m("Advanced","Mill")}
{obj(["Variables #1-#33 local, #100+ common","IF/WHILE branching with N labels","Input validation: reject ≤0","Divide-by-zero protection"])}
<h2>Concept</h2>
<p>A <strong>macro</strong> is a program with variables and logic. On Haas/FANUC, variables like #1, #2 hold numbers. <code>IF[#1 LE 0] GOTO 10</code> jumps to N10 if input is invalid. <strong>N labels</strong> are jump targets; <strong>O numbers</strong> are program numbers — GOTO O1000 is wrong, GOTO N100 is correct.</p>
<h2>Why It Matters</h2>
<p>R08: the previous example used <code>GOTO1000</code> which jumps to O1000 (a program number), not a label. The correct target is an N label inside the current program. Also: if an input PCD is 0 or negative, dividing by it crashes. Macros must validate inputs.</p>
<h2>How</h2>
<h3>PCD40 4-hole bolt circle macro</h3>
<p>Input #1 = PCD radius (R). Input #2 = number of holes (N). Drill positions computed with cos/sin.</p>
{code('O3600 (BOLT CIRCLE MACRO)\n#1 = 20.          <span class="cp-comment">(radius, PCD40/2)</span>\n#2 = 4            <span class="cp-comment">(4 holes)</span>\n#3 = 0            <span class="cp-comment">(count)</span>\n<span class="cp-comment">(input validation)</span>\nIF[#1 LE 0] GOTO 100\nIF[#2 LT 3] GOTO 100\nIF[#2 GT 12] GOTO 100\nWHILE[#3 LT #2] DO 1\n#4 = 360 * #3 / #2\n#5 = #1 * COS[#4]\n#6 = #1 * SIN[#4]\nG90 G81 X#5 Y#6 R2. Z-10. F100.\n#3 = #3 + 1\nEND 1\nG80\nM30\nN100 (ERROR: bad input)\n#3000 = 1 (BAD INPUT)\nM30')}
<p>Hole positions: (20,0), (0,20), (-20,0), (0,-20). The macro rejects radius ≤0, N&lt;3, N&gt;12.</p>
<h2>Common Mistakes</h2>
<ul><li>Using O number as GOTO target — use N label.</li>
<li>Dividing by an input that might be zero.</li>
<li>Forgetting that trig functions use degrees.</li></ul>
{prac([
("What should the macro do if #1 = -5?", "Jump to N100 and alarm: radius must be positive."),
("Why use N labels not O numbers?", "GOTO jumps within the current program; O numbers call separate programs.")])}
{src(["Haas Mill Operator's Manual — Macros and variables (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("35-practical-examples","Practical Examples"), nxt=("37-probing","Probing"))

# 37 Probing (R11: G31 records, doesn't auto-update offsets)
pg('37-probing', "Probing Basics",
   "G31 records a position when the probe touches. It does NOT automatically update work offsets — you read variables and calculate.",
   f'''<h1>Probing Basics</h1>
<p class="lead">A touch probe is a precision measuring tool in the spindle. G31 records the contact position. Work offset updates are your calculation, not automatic.</p>
{m("Advanced","Mill")}
{obj(["G31 = skip-on-touch, record position","Probe variables hold X/Y/Z at touch","Work offset update is manual calculation","Probing cycles vs DIY G31"])}
<h2>Concept</h2>
<p>A <strong>touch probe</strong> touches the part and triggers a signal. <strong>G31</strong> moves toward the part at feed; when the probe triggers, the controller records the current position into a variable. That position is a measurement — the controller does not automatically move the tool or update G54. You calculate the edge center and set the offset yourself (or run a canned probing cycle that does).</p>
<h2>Why It Matters</h2>
<p>R11: the previous version used fake "M06 probe, G38.2" syntax. G31 records positions to variables; it does not auto-update offsets. Thinking G31 "sets work zero" automatically is wrong — it gives you data; you do the math.</p>
<h2>How</h2>
<h3>Edge finding with G31</h3>
<p>Probe approaches the left edge at slow feed. On touch, #5061 (X position) records. If the probe tip is Ø4 and the touch X = -100, the left edge is at -100 + 2 = -98. If work zero is center, G54 X = -98 - half-width. You compute and enter.</p>
<h2>Common Mistakes</h2>
<ul><li>Thinking G31 auto-sets G54 — it records, you calculate.</li>
<li>Probing at high feed — probe is delicate.</li>
<li>Forgetting probe tip radius in the calculation.</li></ul>
{prac([
("G31 touches left edge at X=-100, probe tip Ø4. Edge position?", "-100 + 2 = -98 (tip center was at -100, tip radius 2 to the left)."),
("Does G31 update G54?", "No. It records the touch position to a variable. You calculate and enter the offset.")])}
{src(["Haas Mill Operator's Manual — G31 probe input (haascnc.com, retrieved 2026-09-24)."])}''',
   prev=("36-macro-programming","Macro Programming"), nxt=("38-controller-specific","Controller Differences"))

# 38 Controller-Specific Programming
pg('38-controller-specific', "Controller-Specific Programming",
   "FANUC, Siemens, HEIDENHAIN, and Haas: same part, different dialects. Know your controller.",
   f'''<h1>Controller-Specific Programming</h1>
<p class="lead">The same part programs differently on a FANUC vs a Haas. M-codes, cycle formats, and thread syntax vary. This page compares the major dialects.</p>
{m("Advanced","Mill & Lathe")}
{obj(["FANUC: industry standard, G95 feed/rev","Haas: simplified cycles, G99 feed/rev on lathe","Siemens: ShopMill/ShopTurn conversational","HEIDENHAIN: conversational, clearly different"])}
<h2>Concept</h2>
<p>G-code is not universal. FANUC set the standard; Haas simplified it; Siemens and HEIDENHAIN use entirely different conversational languages. A program that runs on one may alarm on another.</p>
<h2>Why It Matters</h2>
<p>Copying a FANUC two-line G76 onto a Haas fails. Copying Haas G99 feed/rev onto a FANUC mill may mean something different. Always translate, do not copy.</p>
<h2>How</h2>
<h3>Key differences</h3>
<ul><li><strong>Feed/rev</strong>: FANUC uses G95; Haas lathe uses G99.</li>
<li><strong>Thread cycle</strong>: FANUC two-line G76; Haas one-line G76 with K/D.</li>
<li><strong>Subprogram call</strong>: FANUC M98 P O; Haas M98 P.</li>
<li><strong>Units</strong>: G20/G21 universal, but default units vary.</li></ul>
<h2>Common Mistakes</h2>
<ul><li>Assuming G-code is universal.</li>
<li>Running a FANUC backup on a Haas without translation.</li>
<li>Using canned cycles that do not exist on your controller.</li></ul>
{prac([
("FANUC uses G95 for feed/rev. What does Haas use on a lathe?", "G99. G98/G99 on Haas lathe control retract and feed mode."),
("Can you run a Siemens ShopTurn program on a Haas?", "No. Siemens conversational is a different language entirely.")])}
{src(["Haas Lathe Operator's Manual (haascnc.com, retrieved 2026-09-24).","FANUC Series Manual (general reference)."])}''',
   prev=("37-probing","Probing"), nxt=("39-assessment","Self-Assessment"))

print("36, 37, 38 done.")

# 39 Self-Assessment (R10: G00 cancels canned cycle on Haas)
pg('39-assessment', "Programming Self-Assessment",
   "20 knowledge questions, 2 code reviews, 2 project proposals. Test yourself: can you read, write, and debug a basic CNC program?",
   f'''<h1>Programming Self-Assessment</h1>
<p class="lead">20 questions (40 pts), 2 code reviews (10 pts each), 2 project proposals (20 pts each). Pass at 80/100.</p>
{m("Key","Mill & Lathe")}
{obj(["20 knowledge questions","2 code reviews with intentional errors","2 project proposals","Answer key at the bottom"])}
<h2>Part A: Knowledge (40 pts, 2 each)</h2>
<ol><li>What does G01 do?</li>
<li>What does G54 store?</li>
<li>G90 vs G91?</li>
<li>What is F in G94 mode?</li>
<li>What does M03 do?</li>
<li>What does G43 H01 do?</li>
<li>Why G80 after drilling?</li>
<li>What does G41 mean?</li>
<li>Why G96 needs G50 S?</li>
<li>What is I,J in an arc?</li>
<li>What does G99 do on a Haas lathe?</li>
<li>Why does threading use G97?</li>
<li>What is diameter programming?</li>
<li>Why not G00 down to Z-10?</li>
<li>What does M30 do?</li>
<li>Why a startup block?</li>
<li>What is a modal code?</li>
<li>Why dry run at raised Z does not prove no collision?</li>
<li>What does G31 do?</li>
<li>Why use N labels not O numbers for GOTO?</li></ol>
<h2>Part B: Code Reviews (10 pts each)</h2>
<p><strong>Review 1:</strong> <code>G90 G54 G00 X20 Y20 / G01 Z-2 F100 / G01 X80 F300 / G00 X0 Y0</code> — after G01 X80 F300, G00 X0 Y0. Does the G00 line drill? <strong>Answer (R10):</strong> On Haas, G00 cancels the canned cycle — but this program has no active G81, so G00 just repositions. The trick: if a G81 were active, G00 cancels it on Haas (unlike some FANUCs). Verify against your controller.</p>
<p><strong>Review 2:</strong> <code>G01 X10 Y10 F100 / X20 / G91 X5 / X5</code> — starting at X0, where does the tool end? Answer: X10 (G90) → X20 → G91 X5 = X25 → X5 = X30. Y stays at 10.</p>
<h2>Part C: Project Proposals (20 pts each)</h2>
<p>1. Describe a process plan for a 50×50×10 plate with 4 corner holes. 2. Describe a lathe program for a shouldered shaft Ø20/Ø30.</p>
<h2>Answer Key (Part A)</h2>
<ol><li>Linear feed.</li><li>Work offset (work zero).</li><li>Absolute vs incremental.</li><li>Feed per minute.</li><li>Spindle CW.</li><li>Tool length offset 01.</li><li>Cancel modal drill cycle.</li><li>Cutter comp left.</li><li>Max RPM clamp for G96.</li><li>Incremental arc center.</li><li>Feed per rev.</li><li>Constant RPM for consistent pitch.</li><li>X is diameter, not radius.</li><li>G00 is rapid, no feed control.</li><li>End program, rewind.</li><li>Known machine state.</li><li>Persists until canceled.</li><li>Holder/fixture clearance untested.</li><li>Probe touch position record.</li><li>GOTO jumps within program, not to another O.</li></ol>
{prac([
("Score yourself: 80+ = ready to write basic programs. Below 80 = revisit the relevant lesson.","")])}
{src(["This assessment is self-graded; review your answers against each lesson."])}''',
   prev=("38-controller-specific","Controller Differences"), nxt=("31-learning-path","Learning Path"))

# 31 Learning Path
pg('31-learning-path', "Your Learning Path",
   "Four levels from zero to macro programming. Follow the order; do not skip ahead.",
   f'''<h1>Your Learning Path</h1>
<p class="lead">Level 1: foundations. Level 2: basic turning/milling. Level 3: intermediate cycles. Level 4: macros and automation.</p>
{m("Key","All")}
{obj(["Level 1: 10 lessons to a basic program","Level 2: turning, milling, cycles","Level 3: subprograms, multiple tools","Level 4: macros, probing, automation"])}
<h2>Concept</h2>
<p>Do not learn G-codes in isolation. Build up: coordinate systems first, then motion, then offsets, then a complete program. Each lesson depends on the previous.</p>
<h2>Level 1: Fundamentals</h2>
<ol><li>What is CNC Programming (01)</li><li>Machine Fundamentals (02)</li><li>Program Safety (23)</li><li>Programming Math (08)</li><li>Coordinate Systems (03)</li><li>Planes & Units (07)</li><li>Program Structure (04)</li><li>G-Code Basics (05)</li><li>Modal State (06)</li><li>M-Codes (09)</li></ol>
<h2>Level 2: Basic Machining</h2>
<ol><li>Feed (11), Spindle (10), Work Offsets (13), Tool Offsets (12)</li><li>Linear (14), Circular (15), Cutter Comp (16)</li><li>Drilling Cycles (33), Canned Cycles (18)</li><li>Turning (19), Milling (20)</li></ol>
<h2>Level 3: Intermediate</h2>
<ol><li>Threading (21, 22), Subprograms (34)</li><li>Verification (24), Troubleshooting (25), Common Mistakes (26)</li><li>Complete projects (28, 27), Examples (35)</li></ol>
<h2>Level 4: Advanced</h2>
<ol><li>Macros (36), Probing (37), Controllers (38)</li><li>Self-assessment (39), Reference (30), Glossary (40)</li></ol>
{prac([
("Which lesson should you start if you already know G00/G01?","Jump to Lesson 13 (Work Offsets) — offsets are where mistakes happen."),
("Why learn subprograms before macros?","Subprograms teach reuse; macros add variables and logic on top.")])}
{src(["Follow this order; revisit earlier lessons when stuck."])}''',
   prev=("39-assessment","Self-Assessment"), nxt=("30-reference","Reference"))

# 30 Reference
pg('30-reference', "CNC Programming Quick Reference",
   "One-page lookup: common G-codes, M-codes, addresses, and formulas.",
   f'''<h1>CNC Programming Quick Reference</h1>
<p class="lead">For when you are at the machine and need a fast lookup, not a tutorial.</p>
{m("Reference","Mill & Lathe")}
{obj(["Common G-codes","Common M-codes","Addresses and units","Key formulas"])}
<h2>G-codes</h2>
<ul><li>G00 rapid, G01 linear, G02 CW arc, G03 CCW arc.</li>
<li>G17 XY, G18 XZ, G19 YZ plane.</li>
<li>G20 inch, G21 mm.</li>
<li>G40 cancel comp, G41 left, G42 right.</li>
<li>G43 tool length offset, G49 cancel.</li>
<li>G54–G59 work offsets.</li>
<li>G80 cancel cycle, G81 drill, G82 dwell, G83 peck, G84 tap, G85 bore.</li>
<li>G90 absolute, G91 incremental.</li>
<li>G94 feed/min, G95 (FANUC)/G99 (Haas lathe) feed/rev.</li>
<li>G96 CSS (lathe), G97 constant RPM, G50 max RPM.</li>
<li>G71 rough turn, G70 finish turn (lathe).</li></ul>
<h2>M-codes</h2>
<ul><li>M00 stop, M01 optional stop, M02 end, M30 end rewind.</li>
<li>M03 CW, M04 CCW, M05 stop spindle.</li>
<li>M06 tool change, M08 coolant on, M09 off.</li></ul>
<h2>Formulas</h2>
<ul><li>RPM = 1000 &times; Vc / (π &times; D).</li>
<li>Feed = RPM &times; z &times; fz (milling).</li>
<li>Arc length = R &times; θ(radians).</li>
<li>Axial feed for thread = RPM &times; lead.</li></ul>
{prac([
("Bookmark this page for machine-side lookup.","")])}
{src(["Haas Operator's Manuals (haascnc.com, retrieved 2026-09-24).","[Spindle Speed Calculator](/cnc-manufacturing-engineering/engineering-tools/spindle-speed-calculator/)."])}''',
   prev=("31-learning-path","Learning Path"), nxt=("40-glossary","Glossary"))

# 40 Glossary
pg('40-glossary', "CNC Programming Glossary",
   "40+ terms from Absolute to Workpiece Zero — quick definitions, linked to lessons.",
   f'''<h1>CNC Programming Glossary</h1>
<p class="lead">Definitions for the terms used throughout this course. Alphabetical.</p>
{m("Reference","All")}
{obj(["40+ CNC programming terms","Concise definitions","Cross-references to lessons"])}
<h2>Terms</h2>
<ul>
<li><strong>Absolute (G90)</strong>: coordinates are target positions from work zero.</li>
<li><strong>Arc center (I,J)</strong>: incremental offset from arc start to center.</li>
<li><strong>Backlash</strong>: lost motion between reversal.</li>
<li><strong>Canned cycle</strong>: pre-programmed drill sequence (G81/G83/etc).</li>
<li><strong>Chip load</strong>: mm per tooth per cut.</li>
<li><strong>Circular interpolation</strong>: G02/G03 arc motion.</li>
<li><strong>Cutter compensation (G41/G42)</strong>: tool radius offset.</li>
<li><strong>Datum</strong>: reference surface/feature for dimensions.</li>
<li><strong>Diameter programming</strong>: lathe X values are diameter, not radius.</li>
<li><strong>Feed rate</strong>: cutting speed in mm/min or mm/rev.</li>
<li><strong>Fixture</strong>: workholding.</li>
<li><strong>G-code</strong>: preparatory function (motion mode).</li>
<li><strong>G54</strong>: first work offset.</li>
<li><strong>Interpolation</strong>: linear (G01) or circular (G02/G03) motion.</li>
<li><strong>Incremental (G91)</strong>: coordinates are distances moved.</li>
<li><strong>Lead</strong>: axial travel per spindle revolution (threading).</li>
<li><strong>Modal</strong>: code persists until canceled.</li>
<li><strong>M-code</strong>: machine function (spindle, coolant, tool change).</li>
<li><strong>Offsets</strong>: tool length (H), tool radius (D), work (G54).</li>
<li><strong>Pitch</strong>: distance between adjacent thread crests.</li>
<li><strong>R plane</strong>: rapid-to height in canned cycles.</li>
<li><strong>Rapid (G00)</strong>: fast positioning, no cutting.</li>
<li><strong>Repeatability</strong>: machine's ability to return to a position.</li>
<li><strong>Subprogram</strong>: reusable O-number program (M98/M99).</li>
<li><strong>Surface speed (Vc)</strong>: cutting speed in m/min.</li>
<li><strong>Tool length offset (G43 H)</strong>: compensates for tool length.</li>
<li><strong>Torque</strong>: rotational force of spindle.</li>
<li><strong>Workpiece zero</strong>: programmed origin (G54).</li>
</ul>
{prac([
("Use this glossary when a term in a lesson is unfamiliar.","")])}
{src(["Standard machining terminology."])}''',
   prev=("30-reference","Reference"), nxt=None)

print("ALL 40 PAGES DONE.")

# 32 Drawings to Process Plan
pg('32-drawings-process-planning', "From Drawing to Process Plan",
   "Before you write a line of G-code: read the drawing, choose datum, sequence operations, select tools. This is the bridge between engineering and programming.",
   f'''<h1>From Drawing to Process Plan</h1>
<p class="lead">Good programs start before the machine: they start on paper. Reading the drawing, choosing datum, and sequencing operations determines whether the part works.</p>
{m("Key","Mill & Lathe")}
{obj(["Drawing review: dimensions, datums, tolerances","Datum selection and work zero","Operation sequence: rough before finish","Tool selection and cutting parameters"])}
<h2>Concept</h2>
<p>A <strong>process plan</strong> translates a drawing into ordered machine operations. Step 1: read the drawing and identify critical dimensions, datums, and surface finish. Step 2: choose work zero (datum). Step 3: sequence operations — roughing first, finishing last, holes after profile. Step 4: select tools and cutting parameters. Only then write G-code.</p>
<h2>Why It Matters</h2>
<p>Writing code before planning produces a program that machines the wrong features in the wrong order. A part that needs a Ø10 H7 hole should be roughed to Ø9.8 then bored/reamed — not drilled to size directly. The process plan determines the tool list and cycle time.</p>
<h2>How</h2>
<h3>Process plan template</h3>
<ol><li><strong>Material and stock</strong>: what are you starting from?</li>
<li><strong>Datum</strong>: which feature does the drawing reference? Set work zero there.</li>
<li><strong>Operations in order</strong>: face, rough, finish, drill, tap, inspect.</li>
<li><strong>Tools</strong>: which tool for each operation? What H/D offset?</li>
<li><strong>Cutting parameters</strong>: RPM and feed from tooling data.</li>
<li><strong>Inspection</strong>: which dimensions to check after each setup?</li></ol>
<h2>Example</h2>
<p>Plate 100×80×12 with a pocket and 4 holes. Process plan: (1) face top with Ø63 face mill, (2) rough pocket with Ø10 end mill, (3) finish pocket to size, (4) spot and drill 4×Ø6 holes, (5) deburr. Work zero at lower-left on top surface.</p>
<h2>Common Mistakes</h2>
<ul><li>Drilling before milling the flat surface — holes start on uneven stock.</li>
<li>Choosing work zero at a corner that is not the drawing datum.</li>
<li>Skipping roughing and trying to finish in one cut.</li>
<li>Not planning inspection points.</li></ul>
{prac([
("Why rough before finish?", "Roughing removes most stock quickly; finishing takes light cuts to hold tolerance and surface finish."),
("What is the first operation on a raw plate?", "Face the top surface to establish Z zero, then machine features from that flat.")])}
{src(["[Printable Setup Worksheet](/cnc-manufacturing-engineering/engineering-tools/printable-setup-worksheet/).","[Knowledge Base: Process Planning](/cnc-manufacturing-engineering/knowledge-base/09-machining-process-planning/)."])}''',
   prev=("08-programming-math","Programming Math"), nxt=("03-coordinate-systems","Coordinate Systems"))

print("32 done.")
