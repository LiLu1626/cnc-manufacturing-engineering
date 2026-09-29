#!/usr/bin/env python3
"""Generate a CTT article page from content fields. Used to avoid hand-writing boilerplate 36 times."""
import os, html, json, sys

ROOT = "/Users/lilu/Doubao/chats/2026-09-23/new-chat/cnc-manufacturing-engineering/docs/cutting-tool-technology"

NAV = '''<nav class="site-nav">
  <div class="site-nav-inner">
    <div class="site-nav-brand">Li Lu <span>&middot;</span> CNC Eng</div>
    <ul class="site-nav-links">
      <li><a href="/cnc-manufacturing-engineering/">Home</a></li>
      <li><a href="/cnc-manufacturing-engineering/engineering-tools/">Engineering Tools</a></li>
      <li><a href="/cnc-manufacturing-engineering/knowledge-base/">Knowledge Base</a></li>
      <li><a href="/cnc-manufacturing-engineering/machine-systems/">Machine Systems</a></li>
      <li><a href="/cnc-manufacturing-engineering/cnc-programming/">CNC Programming</a></li>
      <li><a href="/cnc-manufacturing-engineering/cutting-tool-technology/" class="active">Cutting Tools</a></li>
      <li><a href="/cnc-manufacturing-engineering/about/">About</a></li>
    </ul>
  </div>
</nav>'''

FOOT = '<footer class="site-footer">Designed by Li Lu &middot; CNC &amp; Manufacturing Engineering</footer>'

def page(*, slug, title, description, level, prereq_html, objectives, h2s, prev=None, nxt=None):
    """h2s: list of (h2_title, inner_html). inner already contains h3/table/svg markup."""
    canon = f"https://lilu1626.github.io/cnc-manufacturing-engineering/cutting-tool-technology/{slug}/"
    body = []
    body.append(f'<a href="/cnc-manufacturing-engineering/cutting-tool-technology/" class="ctt-back">&larr; Back to Cutting Tool Technology</a>')
    body.append(f'<span class="ctt-eyebrow">Cutting Tool Technology &middot; Level {level}</span>')
    body.append(f'<h1>{html.escape(title)}</h1>')
    body.append(f'<p class="lead">{description}</p>')
    body.append(f'<div class="ctt-meta"><span><strong>Level:</strong> {level}</span>{prereq_html}</div>')
    obj_li = "".join(f"<li>{o}</li>" for o in objectives)
    body.append(f'<div class="ctt-objectives"><strong>After this lesson, you can:</strong><ul>{obj_li}</ul></div>')
    toc = "".join(f"<li><a href='#h2-{i+1}'>{html.escape(t)}</a></li>" for i,(t,_) in enumerate(h2s))
    body.append(f'<div class="ctt-toc"><strong>On this page</strong><ol>{toc}</ol></div>')
    for i,(t, inner) in enumerate(h2s):
        body.append(f'<h2 id="h2-{i+1}">{html.escape(t)}</h2>')
        body.append(inner)
    nav = []
    if prev:
        nav.append(f'<a href="{prev[1]}">&larr; Previous: {prev[0]}</a>')
    else:
        nav.append('<a href="/cnc-manufacturing-engineering/cutting-tool-technology/">&uarr; Course home</a>')
    if nxt:
        nav.append(f'<a href="{nxt[1]}">Next: {nxt[0]} &rarr;</a>')
    else:
        nav.append('<a href="/cnc-manufacturing-engineering/cutting-tool-technology/">&uarr; Course home</a>')
    body.append('<nav class="ctt-nav-bottom" aria-label="Lesson navigation">' + "".join(nav) + '</nav>')
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{html.escape(title)} — CNC &amp; Manufacturing Engineering</title>
<meta name="description" content="{html.escape(description[:150])}">
<link rel="canonical" href="{canon}">
<link rel="stylesheet" href="/cnc-manufacturing-engineering/assets/css/site.css">
<link rel="stylesheet" href="/cnc-manufacturing-engineering/assets/css/article.css">
<link rel="stylesheet" href="/cnc-manufacturing-engineering/assets/css/cutting-tool-technology.css?v=wp0">
</head>
<body class="cutting-tool-technology">
{NAV}
<main class="article ctt-article">
{chr(10).join(body)}
</main>
{FOOT}
</body>
</html>'''
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(doc)
    print("wrote", slug, len(doc), "bytes")

if __name__ == "__main__":
    print("generator ready")
