const raUmInput = document.getElementById('raUm');
const raUinInput = document.getElementById('raUin');
const rzInput = document.getElementById('rzUm');
const rmsInput = document.getElementById('rmsUm');

const raR = document.getElementById('raResult');
const rzR = document.getElementById('rzResult');
const rmsR = document.getElementById('rmsResult');
const gradeR = document.getElementById('gradeResult');
const raD = document.getElementById('raDetail');
const rzD = document.getElementById('rzDetail');
const rmsD = document.getElementById('rmsDetail');
const gradeD = document.getElementById('gradeDetail');

const grades = [
  { n: 'N1', ra: 0.025, proc: 'Lapping / honing' },
  { n: 'N2', ra: 0.05, proc: 'Superfinishing' },
  { n: 'N3', ra: 0.10, proc: 'Grinding' },
  { n: 'N4', ra: 0.20, proc: 'Fine grinding' },
  { n: 'N5', ra: 0.40, proc: 'Finish turning' },
  { n: 'N6', ra: 0.80, proc: 'Finish milling' },
  { n: 'N7', ra: 1.60, proc: 'General machining' },
  { n: 'N8', ra: 3.20, proc: 'Rough milling' },
  { n: 'N9', ra: 6.30, proc: 'Roughing' },
  { n: 'N10', ra: 12.50, proc: 'Heavy roughing' },
  { n: 'N11', ra: 25.00, proc: 'Flame cut / as-forged' },
];

function solve() {
  const raUm = parseFloat(raUmInput.value);
  const raUin = parseFloat(raUinInput.value);
  const rz = parseFloat(rzInput.value);
  const rms = parseFloat(rmsInput.value);

  let ra = NaN;

  if (!isNaN(raUm)) ra = raUm;
  else if (!isNaN(raUin)) ra = raUin / 39.37;
  else if (!isNaN(rz)) ra = rz / 4;
  else if (!isNaN(rms)) ra = rms / 1.11;

  if (isNaN(ra)) {
    raR.textContent = '—'; raD.textContent = 'Enter any one value';
    rzR.textContent = '—'; rzD.textContent = '';
    rmsR.textContent = '—'; rmsD.textContent = '';
    gradeR.textContent = '—'; gradeD.textContent = '';
    return;
  }

  const rzCalc = ra * 4;
  const rmsCalc = ra * 1.11;
  const raUinCalc = ra * 39.37;

  // Find closest grade
  let closest = grades[0];
  let minDiff = Math.abs(Math.log(ra / closest.ra));
  for (const g of grades) {
    const diff = Math.abs(Math.log(ra / g.ra));
    if (diff < minDiff) { minDiff = diff; closest = g; }
  }

  raR.textContent = ra.toFixed(3) + ' µm / ' + raUinCalc.toFixed(1) + ' µin';
  raD.textContent = 'Ra (arithmetic avg)';
  rzR.textContent = rzCalc.toFixed(2) + ' µm';
  rzD.textContent = '≈ 4 × Ra (approx)';
  rmsR.textContent = rmsCalc.toFixed(3) + ' µm';
  rmsD.textContent = '≈ 1.11 × Ra (approx)';
  gradeR.textContent = closest.n;
  gradeD.textContent = closest.proc;
}

[raUmInput, raUinInput, rzInput, rmsInput].forEach((el) => el.addEventListener('input', solve));
solve();
