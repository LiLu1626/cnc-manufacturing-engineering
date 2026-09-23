const insertWidth = document.querySelector('#insertWidth');
const vc = document.querySelector('#vc');
const workD = document.querySelector('#workD');
const depth = document.querySelector('#depth');
const feedRev = document.querySelector('#feedRev');

function calculate() {
  const w = Number(insertWidth.value);
  const V = Number(vc.value);
  const D = Number(workD.value);
  const dep = Number(depth.value);
  const f = Number(feedRev.value);

  if (w <= 0 || V <= 0 || D <= 0 || dep <= 0 || f <= 0) {
    document.querySelector('#rpmResult').textContent = '—';
    document.querySelector('#feedResult').textContent = '—';
    document.querySelector('#chipResult').textContent = '—';
    document.querySelector('#dwResult').textContent = '—';
    return;
  }

  const rpm = (1000 * V) / (Math.PI * D);
  const feedRate = f * rpm;
  const chipArea = w * f; // approx: width × feed (grooving cut is full width)
  const dw = dep / w;

  document.querySelector('#rpmResult').textContent = Math.round(rpm).toLocaleString();
  document.querySelector('#feedResult').textContent = feedRate.toFixed(1) + ' mm/min';
  document.querySelector('#chipResult').textContent = chipArea.toFixed(3) + ' mm²';
  document.querySelector('#dwResult').textContent = dw.toFixed(2) + ' : 1';

  let dwText;
  if (dw <= 1.5) {
    dwText = 'Within single-pass depth. Good chip evacuation expected.';
  } else if (dw <= 2.5) {
    dwText = 'Deeper groove. Use peck cycle with 0.5–1 mm retracts.';
  } else {
    dwText = 'Very deep. Requires multiple passes: plunge partially, retract, shift 0.2–0.5 mm axially, repeat.';
  }
  document.querySelector('#dwDetail').textContent = dwText;
}

[insertWidth, vc, workD, depth, feedRev].forEach(el => el.addEventListener('input', calculate));
calculate();
