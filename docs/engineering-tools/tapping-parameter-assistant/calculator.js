const diameterInput = document.getElementById('diameter');
const pitchInput = document.getElementById('pitch');
const vcInput = document.getElementById('vc');
const maxRpmInput = document.getElementById('maxRpm');

const rpmResult = document.getElementById('rpmResult');
const rpmDetail = document.getElementById('rpmDetail');
const feedResult = document.getElementById('feedResult');
const drillResult = document.getElementById('drillResult');
const drillDetail = document.getElementById('drillDetail');
const strategyDetail = document.getElementById('strategyDetail');

function calculate() {
  const D = parseFloat(diameterInput.value) || 0;
  const pitch = parseFloat(pitchInput.value) || 0;
  const vc = parseFloat(vcInput.value) || 0;
  const maxRpm = parseFloat(maxRpmInput.value) || 0;

  if (D <= 0 || pitch <= 0 || vc <= 0) {
    rpmResult.textContent = '—';
    rpmDetail.textContent = '';
    feedResult.textContent = '—';
    drillResult.textContent = '—';
    drillDetail.textContent = '';
    strategyDetail.textContent = '';
    return;
  }

  const idealRpm = (1000 * vc) / (Math.PI * D);
  let rpm = idealRpm;
  let capped = false;
  if (maxRpm > 0 && rpm > maxRpm) {
    rpm = maxRpm;
    capped = true;
  }

  const feed = rpm * pitch;
  const minorDiameter = D - pitch * 1.08256;

  rpmResult.textContent = Math.round(rpm).toLocaleString();
  if (capped) {
    const actualVc = (Math.PI * D * rpm) / 1000;
    rpmDetail.textContent = 'Capped by machine limit. Actual Vc = ' + actualVc.toFixed(1) + ' m/min (target ' + vc.toFixed(1) + ').';
  } else {
    rpmDetail.textContent = 'Ideal Vc = ' + vc.toFixed(1) + ' m/min';
  }

  feedResult.textContent = feed.toFixed(1) + ' mm/min';

  drillResult.textContent = minorDiameter.toFixed(2) + ' mm';
  drillDetail.textContent = 'Tap drill ~ ' + minorDiameter.toFixed(2) + ' mm (≈ ' + (minorDiameter * 0.03937).toFixed(3) + ' in)';

  let strategy = '';
  if (capped) {
    strategy += 'RPM is limited by the machine. ';
  }
  if (pitch >= 1.75) {
    strategy += 'Coarse thread — use spiral-flute or spiral-point tap for chip evacuation. Reduce Vc by 20–30% on blind holes. ';
  } else {
    strategy += 'Fine thread — straight-flute tap is fine for through holes. Use spiral point for through holes to push chips forward. ';
  }
  strategy += 'In rigid tapping (G84), feed is automatically synchronized to pitch. Never override feed on rigid cycles. Use tapping fluid and confirm bottom clearance for blind holes.';

  strategyDetail.textContent = strategy;
}

[diameterInput, pitchInput, vcInput, maxRpmInput].forEach((el) => {
  el.addEventListener('input', calculate);
});

calculate();
