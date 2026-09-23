const radiusInput = document.getElementById('radius');
const angleInput = document.getElementById('angle');
const chordInput = document.getElementById('chord');
const arcInput = document.getElementById('arc');
const sagittaInput = document.getElementById('sagitta');

const rResult = document.getElementById('rResult');
const rDetail = document.getElementById('rDetail');
const angResult = document.getElementById('angResult');
const angDetail = document.getElementById('angDetail');
const cResult = document.getElementById('cResult');
const cDetail = document.getElementById('cDetail');
const lResult = document.getElementById('lResult');
const lDetail = document.getElementById('lDetail');
const hResult = document.getElementById('hResult');
const hDetail = document.getElementById('hDetail');

function solve() {
  const R = parseFloat(radiusInput.value);
  const thetaDeg = parseFloat(angleInput.value);
  const C = parseFloat(chordInput.value);
  const L = parseFloat(arcInput.value);
  const h = parseFloat(sagittaInput.value);

  const known = [];
  if (!isNaN(R)) known.push('R');
  if (!isNaN(thetaDeg)) known.push('ang');
  if (!isNaN(C)) known.push('C');
  if (!isNaN(L)) known.push('L');
  if (!isNaN(h)) known.push('h');

  if (known.length < 2) {
    rResult.textContent = '—'; rDetail.textContent = 'Enter two known values';
    angResult.textContent = '—'; angDetail.textContent = '';
    cResult.textContent = '—'; cDetail.textContent = '';
    lResult.textContent = '—'; lDetail.textContent = '';
    hResult.textContent = '—'; hDetail.textContent = '';
    return;
  }

  let rOut, thetaDegOut, cOut, lOut, hOut;
  let k1 = known[0], k2 = known[1];

  function computeFrom(R, thetaDeg) {
    const rad = thetaDeg * Math.PI / 180;
    cOut = 2 * R * Math.sin(rad / 2);
    lOut = R * rad;
    hOut = R * (1 - Math.cos(rad / 2));
  }

  if (k1 === 'R' && k2 === 'ang') {
    rOut = R; thetaDegOut = thetaDeg;
    computeFrom(R, thetaDeg);
  } else if (k1 === 'R' && k2 === 'C') {
    rOut = R;
    thetaDegOut = 2 * Math.asin(C / (2 * R)) * 180 / Math.PI;
    computeFrom(R, thetaDegOut);
  } else if (k1 === 'R' && k2 === 'L') {
    rOut = R;
    thetaDegOut = (L / R) * 180 / Math.PI;
    computeFrom(R, thetaDegOut);
  } else if (k1 === 'R' && k2 === 'h') {
    rOut = R;
    thetaDegOut = 2 * Math.acos((R - h) / R) * 180 / Math.PI;
    computeFrom(R, thetaDegOut);
  } else if (k1 === 'ang' && k2 === 'C') {
    thetaDegOut = thetaDeg;
    const rad = thetaDeg * Math.PI / 180;
    rOut = C / (2 * Math.sin(rad / 2));
    computeFrom(rOut, thetaDegOut);
  } else if (k1 === 'ang' && k2 === 'L') {
    thetaDegOut = thetaDeg;
    const rad = thetaDeg * Math.PI / 180;
    rOut = L / rad;
    computeFrom(rOut, thetaDegOut);
  } else if (k1 === 'ang' && k2 === 'h') {
    thetaDegOut = thetaDeg;
    const rad = thetaDeg * Math.PI / 180;
    rOut = h / (1 - Math.cos(rad / 2));
    computeFrom(rOut, thetaDegOut);
  } else if (k1 === 'C' && k2 === 'h') {
    rOut = (C * C + 4 * h * h) / (8 * h);
    thetaDegOut = 2 * Math.asin(C / (2 * rOut)) * 180 / Math.PI;
    computeFrom(rOut, thetaDegOut);
  } else {
    // C + L or L + h: iterative solve
    // For C + L: solve C = 2(L/theta) * sin(theta/2) for theta (radians)
    if (k1 === 'C' && k2 === 'L') {
      // Let x = theta (radians). C = 2*(L/x)*sin(x/2) => sin(x/2)/(x/2) = C/L
      const ratio = C / L;
      // Solve sin(x/2)/(x/2) = ratio using Newton
      let x = 1.0;
      for (let i = 0; i < 50; i++) {
        const sx = Math.sin(x / 2) / (x / 2);
        // derivative of sinc(x/2) wrt x
        const dx = 0.0001;
        const sx2 = Math.sin((x + dx) / 2) / ((x + dx) / 2);
        const deriv = (sx2 - sx) / dx;
        x = x - (sx - ratio) / deriv;
        if (x < 0.001) x = 0.001;
      }
      thetaDegOut = x * 180 / Math.PI;
      rOut = L / x;
      computeFrom(rOut, thetaDegOut);
    } else if (k1 === 'L' && k2 === 'h') {
      // L = R*theta, h = R*(1-cos(theta/2))
      // h/L = (1-cos(theta/2))/theta
      const ratio = h / L;
      let x = 1.0;
      for (let i = 0; i < 50; i++) {
        const fx = (1 - Math.cos(x / 2)) / x;
        const dx = 0.0001;
        const fx2 = (1 - Math.cos((x + dx) / 2)) / (x + dx);
        const deriv = (fx2 - fx) / dx;
        x = x - (fx - ratio) / deriv;
        if (x < 0.001) x = 0.001;
      }
      thetaDegOut = x * 180 / Math.PI;
      rOut = L / x;
      computeFrom(rOut, thetaDegOut);
    } else {
      rResult.textContent = 'Invalid';
      rDetail.textContent = 'Cannot solve from these two';
      angResult.textContent = '—'; cResult.textContent = '—';
      lResult.textContent = '—'; hResult.textContent = '—';
      return;
    }
  }

  rResult.textContent = rOut.toFixed(3) + ' mm';
  rDetail.textContent = known.includes('R') ? 'given' : 'calculated';
  angResult.textContent = thetaDegOut.toFixed(2) + '°';
  angDetail.textContent = known.includes('ang') ? 'given' : 'calculated';
  cResult.textContent = cOut.toFixed(3) + ' mm';
  cDetail.textContent = known.includes('C') ? 'given' : 'calculated';
  lResult.textContent = lOut.toFixed(3) + ' mm';
  lDetail.textContent = known.includes('L') ? 'given' : 'calculated';
  hResult.textContent = hOut.toFixed(3) + ' mm';
  hDetail.textContent = known.includes('h') ? 'given' : 'calculated';
}

[radiusInput, angleInput, chordInput, arcInput, sagittaInput].forEach((el) => {
  el.addEventListener('input', solve);
});

solve();
