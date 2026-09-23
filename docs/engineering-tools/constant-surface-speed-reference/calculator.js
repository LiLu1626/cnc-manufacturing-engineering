const dsInput = document.getElementById('dStart');
const deInput = document.getElementById('dEnd');
const vcInput = document.getElementById('vcCss');
const maxInput = document.getElementById('maxRpm');

const rpmSR = document.getElementById('rpmStart');
const rpmIR = document.getElementById('rpmIdealEnd');
const rpmAR = document.getElementById('rpmActualEnd');
const vcER = document.getElementById('vcEnd');
const rpmSD = document.getElementById('rpmStartD');
const rpmID = document.getElementById('rpmIdealEndD');
const rpmAD = document.getElementById('rpmActualEndD');
const vcED = document.getElementById('vcEndD');

function solve() {
  const ds = parseFloat(dsInput.value);
  const de = parseFloat(deInput.value);
  const Vc = parseFloat(vcInput.value);
  const maxRpm = parseFloat(maxInput.value);

  if (isNaN(ds) || isNaN(de) || isNaN(Vc)) {
    rpmSR.textContent = '—'; rpmSD.textContent = 'Enter diameters and Vc';
    rpmIR.textContent = '—'; rpmID.textContent = '';
    rpmAR.textContent = '—'; rpmAD.textContent = '';
    vcER.textContent = '—'; vcED.textContent = '';
    return;
  }

  const rpmStart = 1000 * Vc / (Math.PI * ds);
  const rpmIdealEnd = 1000 * Vc / (Math.PI * de);

  let rpmActualEnd, vcEnd;
  if (!isNaN(maxRpm) && maxRpm > 0) {
    rpmActualEnd = Math.min(rpmIdealEnd, maxRpm);
    vcEnd = Math.PI * de * rpmActualEnd / 1000;
  } else {
    rpmActualEnd = rpmIdealEnd;
    vcEnd = Vc;
  }

  rpmSR.textContent = Math.round(rpmStart) + ' RPM';
  rpmSD.textContent = 'at D=' + ds + ' mm';
  rpmIR.textContent = Math.round(rpmIdealEnd) + ' RPM';
  rpmID.textContent = 'if no RPM limit';
  rpmAR.textContent = Math.round(rpmActualEnd) + ' RPM';
  if (!isNaN(maxRpm) && rpmIdealEnd > maxRpm) {
    rpmAD.textContent = 'capped at G50 limit';
  } else {
    rpmAD.textContent = 'within limit';
  }
  vcER.textContent = vcEnd.toFixed(1) + ' m/min';
  if (vcEnd < Vc - 0.5) {
    vcED.textContent = 'dropped below target (RPM capped)';
  } else {
    vcED.textContent = 'at target Vc';
  }
}

[dsInput, deInput, vcInput, maxInput].forEach((el) => el.addEventListener('input', solve));
solve();
