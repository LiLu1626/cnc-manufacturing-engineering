# Cutting Tool Technology — Article Template

Every numbered article under `docs/cutting-tool-technology/NN-*/index.html` follows this
seven-section skeleton. Teaching word count is measured from **Concept** to the end of
**Common Mistakes** only (excludes lead, objectives, nav, SVG text, code/formulas,
Practice and Sources).

B-class pages: >= 800 counted words, >= 4 quiz items.
K-class pages: >= 2000 counted words, >= 6 quiz items.
Every teaching SVG needs `<title>` and `<desc>`.

```html
<main>
  <h1><!-- Page title --></h1>
  <p class="ctt-lead"><!-- 2-3 sentence lead; NOT counted --></p>
  <p class="ctt-level"><!-- Level / estimated time --></p>

  <h2>Concept</h2>
  <p><!-- what it is --></p>

  <h2>Why it matters</h2>
  <p><!-- why the learner cares --></p>

  <h2>How it works</h2>
  <p><!-- mechanism, geometry, rules --></p>
  <figure class="ctt-figure">
    <svg role="img" aria-label="...">
      <title><!-- figure title --></title>
      <desc><!-- figure description --></desc>
      <!-- geometry consistent with the locked baselines -->
    </svg>
    <figcaption><!-- non-ratio note if needed --></figcaption>
  </figure>

  <h2>Worked Example</h2>
  <p><!-- numeric example; use example-data.json baselines --></p>

  <h2>Common Mistakes</h2>
  <ul><li><strong>...</strong> ...</li></ul>

  <h2>Practice</h2>
  <details><summary>Q.</summary><p>Answer with reasoning.</p></details>

  <h2>Sources</h2>
  <ul><li><!-- per-page reference, see source-register.json --></li></ul>
</main>
```

Locked numeric baselines live in `docs/cutting-tool-technology/example-data.json` and
must not drift between text, figures and answers.
