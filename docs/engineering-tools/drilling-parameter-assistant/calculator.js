const diameterInput = document.querySelector('#diameter');
const vcInput = document.querySelector('#vc');
const feedRevInput = document.querySelector('#feedRev');
const holeDepthInput = document.querySelector('#holeDepth');
const maxRpmInput = document.querySelector('#maxRpm');
const rpmResultEl = document.querySelector('#rpmResult');
const feedResultEl = document.querySelector('#feedResult');
const feedDetailEl = document.querySelector('#feedDetail');
const ldResultEl = document.querySelector('#ldResult');
const ldDetailEl = document.querySelector('#ldDetail');
const strategyDetailEl = document.querySelector('#strategyDetail');

function calculate() {
  const D = Number(diameterInput.value);
  const Vc = Number(vcInput.value);
  const f = Number(feedRevInput.value);
  const depth = Number(holeDepthInput.value);
  const maxRpm = Number(maxRpmInput.value);

  if (D <= 0 || Vc <= 0 || f <= 0) {
    rpmResultEl.textContent = 'Enter positive values';
    feedResultEl.textContent = '—';
    feedDetailEl.textContent = '';
    ldResultEl.textContent = '—';
    ldDetailEl.textContent = '';
    strategyDetailEl.textContent = 'Diameter, cutting speed, and feed must all be greater than zero.';
    return;
  }

  const idealRpm = (1000 * Vc) / (Math.PI * D);
  let rpm = idealRpm;
  let capped = false;

  if (maxRpm > 0 && idealRpm > maxRpm) {
    rpm = maxRpm;
    capped = true;
  }

  const feedRate = f * rpm;
  const ld = depth / D;

  rpmResultEl.textContent = Math.round(rpm).toLocaleString();
  feedResultEl.textContent = feedRate.toFixed(1) + ' mm/min';

  if (capped) {
    const actualVc = (Math.PI * D * rpm) / 1000;
    feedDetailEl.textContent = 'RPM capped by machine limit. Actual Vc = ' + actualVc.toFixed(1) + ' m/min instead of ' + Vc.toFixed(1) + '.';
  } else {
    feedDetailEl.textContent = '';
  }

  ldResultEl.textContent = ld.toFixed(1);

  let risk, strategy;
  if (ld <= 3) {
    risk = 'Short hole';
    strategy = 'Standard drilling. No peck needed unless chips pack. Use through-hole or spot drill to start.';
  } else if (ld <= 6) {
    risk = 'Moderate depth';
    strategy = 'Standard drilling with periodic peck (Q 2–3×D). Ensure through-spindle coolant or air blast.';
  } else if (ld <= 10) {
    risk = 'Deep hole';
    strategy = 'Peck drilling every 2–3×D. Use through-tool coolant. Reduce feed by 20–30% in the first engagement and final breakthrough.';
  } else {
    risk = 'Very deep hole';
    strategy = 'Deep-hole strategy: peck every 1.5–2×D, full retract to clear chips. Consider internal-coolant drill or gun-drill process. Watch for wander and hole straightness.';
  }

  ldDetailEl.textContent = risk;
  strategyDetailEl.textContent = strategy;
}

[diameterInput, vcInput, feedRevInput, holeDepthInput, maxRpmInput].forEach((input) => {
  input.addEventListener('input', calculate);
});

calculate();

