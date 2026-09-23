const dInput = document.getElementById('largeD');
const sInput = document.getElementById('smallD');
const lInput = document.getElementById('lengthL');
const aInput = document.getElementById('incAngle');

const dR = document.getElementById('dResult');
const sR = document.getElementById('sResult');
const lR = document.getElementById('lResult');
const aR = document.getElementById('aResult');
const tp100R = document.getElementById('tp100Result');
const halfR = document.getElementById('halfResult');
const dD = document.getElementById('dDetail');
const sD = document.getElementById('sDetail');
const lD = document.getElementById('lDetail');
const aD = document.getElementById('aDetail');
const tp100D = document.getElementById('tp100Detail');
const halfD = document.getElementById('halfDetail');

function solve() {
  const D = parseFloat(dInput.value);
  const d = parseFloat(sInput.value);
  const L = parseFloat(lInput.value);
  const alpha = parseFloat(aInput.value);

  const known = [];
  if (!isNaN(D)) known.push('D');
  if (!isNaN(d)) known.push('d');
  if (!isNaN(L)) known.push('L');
  if (!isNaN(alpha)) known.push('a');

  if (known.length < 3) {
    dR.textContent = '—'; dD.textContent = 'Enter three known values';
    sR.textContent = '—'; sD.textContent = '';
    lR.textContent = '—'; lD.textContent = '';
    aR.textContent = '—'; aD.textContent = '';
    tp100R.textContent = '—'; tp100D.textContent = '';
    halfR.textContent = '—'; halfD.textContent = '';
    return;
  }

  let oD, od, oL, oa;

  if (known.includes('D') && known.includes('d') && known.includes('L')) {
    oD = D; od = d; oL = L;
    oa = 2 * Math.atan((D - d) / (2 * L)) * 180 / Math.PI;
  } else if (known.includes('D') && known.includes('d') && known.includes('a')) {
    oD = D; od = d; oa = alpha;
    oL = (D - d) / (2 * Math.tan(alpha * Math.PI / 360));
  } else if (known.includes('D') && known.includes('L') && known.includes('a')) {
    oD = D; oL = L; oa = alpha;
    od = D - 2 * L * Math.tan(alpha * Math.PI / 360);
  } else if (known.includes('d') && known.includes('L') && known.includes('a')) {
    od = d; oL = L; oa = alpha;
    oD = d + 2 * L * Math.tan(alpha * Math.PI / 360);
  } else {
    dR.textContent = 'Invalid'; dD.textContent = 'Need three of four';
    sR.textContent = '—'; lR.textContent = '—'; aR.textContent = '—';
    tp100R.textContent = '—'; halfR.textContent = '—';
    return;
  }

  const halfAngle = oa / 2;
  const taperPer100 = (oD - od) / oL * 100;

  dR.textContent = oD.toFixed(3) + ' mm';
  dD.textContent = known.includes('D') ? 'given' : 'calculated';
  sR.textContent = od.toFixed(3) + ' mm';
  sD.textContent = known.includes('d') ? 'given' : 'calculated';
  lR.textContent = oL.toFixed(3) + ' mm';
  lD.textContent = known.includes('L') ? 'given' : 'calculated';
  aR.textContent = oa.toFixed(2) + '°';
  aD.textContent = known.includes('a') ? 'given' : 'calculated';
  tp100R.textContent = taperPer100.toFixed(3) + ' mm/100mm';
  tp100D.textContent = 'taper rate';
  halfR.textContent = halfAngle.toFixed(2) + '°';
  halfD.textContent = 'compound rest / program angle';
}

[dInput, sInput, lInput, aInput].forEach((el) => el.addEventListener('input', solve));
solve();
