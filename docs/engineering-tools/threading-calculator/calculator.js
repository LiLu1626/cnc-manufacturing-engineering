const dInput = document.getElementById('workD');
const pInput = document.getElementById('pitchP');
const vcInput = document.getElementById('vcThr');
const modeInput = document.getElementById('mode');

const rpmR = document.getElementById('rpmResult');
const feedR = document.getElementById('feedResult');
const depthR = document.getElementById('depthResult');
const passesR = document.getElementById('passesResult');
const minorR = document.getElementById('minorResult');
const leadR = document.getElementById('leadResult');
const rpmD = document.getElementById('rpmDetail');
const feedD = document.getElementById('feedDetail');
const depthD = document.getElementById('depthDetail');
const passesD = document.getElementById('passesDetail');
const minorD = document.getElementById('minorDetail');
const leadD = document.getElementById('leadDetail');

function solve() {
  const D = parseFloat(dInput.value);
  const P = parseFloat(pInput.value);
  const Vc = parseFloat(vcInput.value);
  const isInternal = modeInput.value === '60int';

  if (isNaN(D) || isNaN(P)) {
    rpmR.textContent = '—'; rpmD.textContent = 'Enter diameter and pitch';
    feedR.textContent = '—'; feedD.textContent = '';
    depthR.textContent = '—'; depthD.textContent = '';
    passesR.textContent = '—'; passesD.textContent = '';
    minorR.textContent = '—'; minorD.textContent = '';
    leadR.textContent = '—'; leadD.textContent = '';
    return;
  }

  const VcUse = isNaN(Vc) ? 60 : Vc;
  const rpm = 1000 * VcUse / (Math.PI * D);
  const feed = rpm * P; // mm/min
  const threadDepth = 0.6134 * P;
  const minorDiam = D - 2 * threadDepth;

  // Approx passes based on total depth
  let passes;
  if (P <= 0.8) passes = 3;
  else if (P <= 1.0) passes = 4;
  else if (P <= 1.5) passes = 6;
  else if (P <= 2.0) passes = 8;
  else if (P <= 2.5) passes = 10;
  else passes = 12;

  rpmR.textContent = Math.round(rpm) + ' RPM';
  rpmD.textContent = 'Vc = ' + VcUse + ' m/min';
  feedR.textContent = feed.toFixed(0) + ' mm/min';
  feedD.textContent = 'F=' + P.toFixed(2) + ' mm/rev';
  depthR.textContent = threadDepth.toFixed(3) + ' mm';
  depthD.textContent = isInternal ? 'internal bore depth' : 'external thread depth';
  passesR.textContent = passes + ' passes';
  passesD.textContent = 'rough estimate (decreasing infeed)';
  minorR.textContent = minorDiam.toFixed(3) + ' mm';
  minorD.textContent = isInternal ? 'tap drill ≈ ' + (D - P).toFixed(2) : 'minor diameter';
  leadR.textContent = P.toFixed(2) + ' mm/rev';
  leadD.textContent = 'single start (lead = pitch)';
}

[dInput, pInput, vcInput, modeInput].forEach((el) => el.addEventListener('input', solve));
solve();
