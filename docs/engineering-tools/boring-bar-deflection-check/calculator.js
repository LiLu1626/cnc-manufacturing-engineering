const barD = document.querySelector('#barD');
const overhang = document.querySelector('#overhang');
const barMaterial = document.querySelector('#barMaterial');
const workMaterial = document.querySelector('#workMaterial');
const ap = document.querySelector('#ap');
const f = document.querySelector('#f');

function calculate() {
  const d = Number(barD.value);
  const L = Number(overhang.value);
  const E = Number(barMaterial.value);
  const kc = Number(workMaterial.value);
  const depth = Number(ap.value);
  const feed = Number(f.value);

  if (d <= 0 || L <= 0 || depth <= 0 || feed <= 0) {
    document.querySelector('#ldResult').textContent = '—';
    document.querySelector('#deflectResult').textContent = '—';
    document.querySelector('#forceResult').textContent = '—';
    document.querySelector('#riskResult').textContent = '—';
    return;
  }

  // L/D ratio
  const ld = L / d;

  // Moment of inertia: I = pi*d^4/64
  const I = Math.PI * Math.pow(d, 4) / 64;

  // Cutting force: Fc = ap * f * kc
  const Fc = depth * feed * kc;

  // Radial force estimate: Fr = 0.4 * Fc
  const Fr = Fc * 0.4;

  // Deflection: delta = Fr * L^3 / (3 * E * I)
  const delta = (Fr * Math.pow(L, 3)) / (3 * E * I);

  document.querySelector('#ldResult').textContent = ld.toFixed(1) + ' : 1';
  document.querySelector('#deflectResult').textContent = (delta * 1000).toFixed(3) + ' µm';
  document.querySelector('#forceResult').textContent = Math.round(Fc) + ' N';

  // Risk assessment
  let risk, riskText;
  if (ld <= 4 && delta < 0.01) {
    risk = 'Safe';
    riskText = 'Stable setup. Good surface finish expected. No chatter risk at these parameters.';
  } else if (ld <= 6 && delta < 0.02) {
    risk = 'Watch';
    riskText = 'Marginal. Monitor finish and listen for chatter. Consider reducing ap or using sharper inserts.';
  } else if (ld <= 8) {
    risk = 'Risky';
    riskText = 'High deflection/chatter risk. Reduce overhang, increase bar diameter, or switch to carbide shank. Reduce feed by 20–30%.';
  } else {
    risk = 'Danger';
    riskText = 'Very high risk. Deflection will cause visible finish errors and likely chatter. Use a damped boring bar, reduce L, or re-design the setup.';
  }

  document.querySelector('#riskResult').textContent = risk;
  document.querySelector('#riskDetail').textContent = riskText;

  // L/D detail
  if (ld <= 4) {
    document.querySelector('#ldDetail').textContent = 'Short overhang — rigid setup';
  } else if (ld <= 6) {
    document.querySelector('#ldDetail').textContent = 'Moderate overhang — acceptable for carbide';
  } else if (ld <= 8) {
    document.querySelector('#ldDetail').textContent = 'Long overhang — near limit';
  } else {
    document.querySelector('#ldDetail').textContent = 'Very long — requires damped bar';
  }

  document.querySelector('#deflectDetail').textContent = 'δ = Fr·L³ / (3EI). Smaller is better; target < 0.01–0.02 mm.';
}

[barD, overhang, barMaterial, workMaterial, ap, f].forEach(el => {
  el.addEventListener('input', calculate);
});
calculate();
