const sideAInput = document.getElementById('sideA');
const sideBInput = document.getElementById('sideB');
const hypCInput = document.getElementById('hypC');
const angleAInput = document.getElementById('angleA');

const aResult = document.getElementById('aResult');
const aDetail = document.getElementById('aDetail');
const bResult = document.getElementById('bResult');
const bDetail = document.getElementById('bDetail');
const cResult = document.getElementById('cResult');
const cDetail = document.getElementById('cDetail');
const angResult = document.getElementById('angResult');
const angDetail = document.getElementById('angDetail');

function solve() {
  const a = parseFloat(sideAInput.value);
  const b = parseFloat(sideBInput.value);
  const c = parseFloat(hypCInput.value);
  const angleA = parseFloat(angleAInput.value);

  // Count known values
  const known = [];
  if (!isNaN(a)) known.push('a');
  if (!isNaN(b)) known.push('b');
  if (!isNaN(c)) known.push('c');
  if (!isNaN(angleA)) known.push('A');

  if (known.length < 2) {
    aResult.textContent = '—';
    aDetail.textContent = 'Enter two known values';
    bResult.textContent = '—';
    bDetail.textContent = '';
    cResult.textContent = '—';
    cDetail.textContent = '';
    angResult.textContent = '—';
    angDetail.textContent = '';
    return;
  }

  let sa, sb, sc, sA;

  // Determine which two knowns to use
  const k1 = known[0];
  const k2 = known[1];

  if (k1 === 'a' && k2 === 'b') {
    sa = a; sb = b;
    sc = Math.sqrt(a*a + b*b);
    sA = Math.atan(a/b) * 180 / Math.PI;
  } else if (k1 === 'a' && k2 === 'c') {
    sa = a; sc = c;
    sb = Math.sqrt(c*c - a*a);
    sA = Math.asin(a/c) * 180 / Math.PI;
  } else if (k1 === 'b' && k2 === 'c') {
    sb = b; sc = c;
    sa = Math.sqrt(c*c - b*b);
    sA = Math.acos(b/c) * 180 / Math.PI;
  } else if (k1 === 'a' && k2 === 'A') {
    sa = a; sA = angleA;
    const rad = angleA * Math.PI / 180;
    sb = a / Math.tan(rad);
    sc = a / Math.sin(rad);
  } else if (k1 === 'b' && k2 === 'A') {
    sb = b; sA = angleA;
    const rad = angleA * Math.PI / 180;
    sa = b * Math.tan(rad);
    sc = b / Math.cos(rad);
  } else if (k1 === 'c' && k2 === 'A') {
    sc = c; sA = angleA;
    const rad = angleA * Math.PI / 180;
    sa = c * Math.sin(rad);
    sb = c * Math.cos(rad);
  } else {
    aResult.textContent = 'Invalid';
    aDetail.textContent = 'Cannot solve from these two';
    bResult.textContent = '—';
    cResult.textContent = '—';
    angResult.textContent = '—';
    angDetail.textContent = 'Need 2 sides or 1 side + 1 angle';
    return;
  }

  const sB = 90 - sA;

  aResult.textContent = sa.toFixed(3) + ' mm';
  aDetail.textContent = known.includes('a') ? 'given' : 'calculated';
  bResult.textContent = sb.toFixed(3) + ' mm';
  bDetail.textContent = known.includes('b') ? 'given' : 'calculated';
  cResult.textContent = sc.toFixed(3) + ' mm';
  cDetail.textContent = known.includes('c') ? 'given' : 'calculated';
  angResult.textContent = sA.toFixed(2) + '° / ' + sB.toFixed(2) + '°';
  angDetail.textContent = 'A / B (C = 90°)';
}

[sideAInput, sideBInput, hypCInput, angleAInput].forEach((el) => {
  el.addEventListener('input', solve);
});

solve();
