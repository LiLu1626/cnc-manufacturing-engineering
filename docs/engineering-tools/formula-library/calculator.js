const formulas = [
  { cat: 'Speeds & Feeds', name: 'Spindle speed (milling/turning)', formula: 'RPM = 1000 × Vc / (π × D)', tool: 'spindle-speed-calculator', toolName: 'Spindle Speed Calculator' },
  { cat: 'Speeds & Feeds', name: 'Feed rate (per tooth)', formula: 'Vf = RPM × fz × z', tool: 'feed-rate-calculator', toolName: 'Feed Rate Calculator' },
  { cat: 'Speeds & Feeds', name: 'Feed per revolution (turning)', formula: 'Vf = RPM × f', tool: 'turning-speed-feed-calculator', toolName: 'Turning Speed & Feed' },
  { cat: 'Speeds & Feeds', name: 'Cutting speed (reverse)', formula: 'Vc = π × D × RPM / 1000', tool: 'cutting-speed-calculator', toolName: 'Cutting Speed Calculator' },
  { cat: 'Speeds & Feeds', name: 'Metal removal rate', formula: 'Q = Vf × ap × ae / 1000 (cm³/min)', tool: 'material-removal-rate-calculator', toolName: 'MRR Calculator' },
  { cat: 'Drilling', name: 'Drill RPM', formula: 'RPM = 1000 × Vc / (π × D_drill)', tool: 'drilling-parameter-assistant', toolName: 'Drilling Parameter Assistant' },
  { cat: 'Drilling', name: 'Drill feed rate', formula: 'Vf = RPM × fn', tool: 'drilling-parameter-assistant', toolName: 'Drilling Parameter Assistant' },
  { cat: 'Drilling', name: 'L/D ratio', formula: 'L/D = hole_depth / drill_diameter', tool: 'drilling-parameter-assistant', toolName: 'Drilling Parameter Assistant' },
  { cat: 'Tapping', name: 'Tap RPM', formula: 'RPM = 1000 × Vc / (π × D_tap)', tool: 'tapping-parameter-assistant', toolName: 'Tapping Parameter Assistant' },
  { cat: 'Tapping', name: 'Tapping feed', formula: 'Vf = RPM × pitch', tool: 'tapping-parameter-assistant', toolName: 'Tapping Parameter Assistant' },
  { cat: 'Tapping', name: 'Tap drill size (metric)', formula: 'D_tap = nominal − pitch', tool: 'tapping-parameter-assistant', toolName: 'Tapping Parameter Assistant' },
  { cat: 'Threads', name: 'Thread depth (60°)', formula: 'depth = 0.6134 × P', tool: 'threading-calculator', toolName: 'Threading Calculator' },
  { cat: 'Threads', name: 'Minor diameter (external)', formula: 'd_minor = D − 1.2268 × P', tool: 'threading-calculator', toolName: 'Threading Calculator' },
  { cat: 'Threads', name: 'Thread feed', formula: 'F = P (mm/rev)', tool: 'threading-calculator', toolName: 'Threading Calculator' },
  { cat: 'Geometry', name: 'Right triangle: Pythagoras', formula: 'c = √(a² + b²)', tool: 'right-triangle-calculator', toolName: 'Right-Triangle Calculator' },
  { cat: 'Geometry', name: 'Right triangle: angle', formula: 'tan(A) = a / b', tool: 'right-triangle-calculator', toolName: 'Right-Triangle Calculator' },
  { cat: 'Geometry', name: 'Chord length', formula: 'C = 2R × sin(θ/2)', tool: 'arc-and-chord-calculator', toolName: 'Arc and Chord Calculator' },
  { cat: 'Geometry', name: 'Arc length', formula: 'L = R × θ (radians)', tool: 'arc-and-chord-calculator', toolName: 'Arc and Chord Calculator' },
  { cat: 'Geometry', name: 'Sagitta (bow height)', formula: 'h = R × (1 − cos(θ/2))', tool: 'arc-and-chord-calculator', toolName: 'Arc and Chord Calculator' },
  { cat: 'Taper', name: 'Taper angle', formula: 'α = 2 × atan((D−d) / (2L))', tool: 'taper-angle-calculator', toolName: 'Taper and Angle Calculator' },
  { cat: 'Taper', name: 'Taper per 100 mm', formula: '= (D − d) / L × 100', tool: 'taper-angle-calculator', toolName: 'Taper and Angle Calculator' },
  { cat: 'Bolt circles', name: 'Bolt circle hole X', formula: 'X = R × cos(angle)', tool: 'bolt-circle-calculator', toolName: 'Bolt Circle Calculator' },
  { cat: 'Bolt circles', name: 'Bolt circle hole Y', formula: 'Y = R × sin(angle)', tool: 'bolt-circle-calculator', toolName: 'Bolt Circle Calculator' },
  { cat: 'CSS', name: 'CSS crossover', formula: 'D_cross = 1000 × Vc / (π × RPM_max)', tool: 'constant-surface-speed-reference', toolName: 'CSS Reference' },
  { cat: 'Surface finish', name: 'Ra to Rz', formula: 'Rz ≈ 4 × Ra', tool: 'surface-finish-conversion', toolName: 'Surface Finish Conversion' },
  { cat: 'Surface finish', name: 'µm to µin', formula: 'µin = µm × 39.37', tool: 'surface-finish-conversion', toolName: 'Surface Finish Conversion' },
];

const listEl = document.getElementById('formulaList');
const searchEl = document.getElementById('searchBox');

function render(list) {
  listEl.innerHTML = '';
  if (list.length === 0) {
    listEl.innerHTML = '<p style="color:var(--muted);">No formulas match your search.</p>';
    return;
  }
  let currentCat = '';
  for (const f of list) {
    if (f.cat !== currentCat) {
      currentCat = f.cat;
      const h = document.createElement('h3');
      h.style.cssText = 'color:var(--accent-dark); margin:1rem 0 0.5rem; font-size:1rem;';
      h.textContent = f.cat;
      listEl.appendChild(h);
    }
    const card = document.createElement('div');
    card.style.cssText = 'border:1px solid var(--border); border-radius:8px; padding:0.75rem 1rem; margin-bottom:0.5rem;';
    card.innerHTML = '<strong>' + f.name + '</strong><br>' +
      '<code style="color:var(--accent);">' + f.formula + '</code><br>' +
      '<a href="' + f.tool + '/" style="color:var(--accent); font-size:0.85rem;">Open ' + f.toolName + ' →</a>';
    listEl.appendChild(card);
  }
}

searchEl.addEventListener('input', () => {
  const q = searchEl.value.toLowerCase().trim();
  if (!q) { render(formulas); return; }
  const filtered = formulas.filter((f) =>
    f.name.toLowerCase().includes(q) ||
    f.formula.toLowerCase().includes(q) ||
    f.cat.toLowerCase().includes(q)
  );
  render(filtered);
});

render(formulas);
