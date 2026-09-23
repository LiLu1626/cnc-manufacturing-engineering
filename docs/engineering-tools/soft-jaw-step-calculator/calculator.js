const partInput = document.getElementById('partD');
const stepInput = document.getElementById('stepH');
const jawInput = document.getElementById('jawCount');
const boreInput = document.getElementById('jawBore');

const boreR = document.getElementById('boreResult');
const stepR = document.getElementById('stepResult');
const radialR = document.getElementById('radialResult');
const contactR = document.getElementById('contactResult');
const boreD = document.getElementById('boreDetail');
const stepD = document.getElementById('stepDetail');
const radialD = document.getElementById('radialDetail');
const contactD = document.getElementById('contactDetail');

function solve() {
  const D = parseFloat(partInput.value);
  const h = parseFloat(stepInput.value);
  const jaws = parseInt(jawInput.value);
  const boreDepth = parseFloat(boreInput.value);

  if (isNaN(D)) {
    boreR.textContent = '—'; boreD.textContent = 'Enter part diameter';
    stepR.textContent = '—'; stepD.textContent = '';
    radialR.textContent = '—'; radialD.textContent = '';
    contactR.textContent = '—'; contactD.textContent = '';
    return;
  }

  const clearance = 0.03; // typical 0.02-0.05
  const mainBore = D + clearance;
  const stepRadial = isNaN(h) ? 1.0 : h;
  const stepDiam = mainBore - 2 * stepRadial;

  // Contact arc per jaw: roughly 360/jaw angle, but effective grip depends on step
  const anglePerJaw = 360 / jaws;
  // Approx contact arc width at the part surface
  const contactWidth = (Math.PI * D * (anglePerJaw - 20)) / 360; // effective ~20° gap per jaw

  boreR.textContent = mainBore.toFixed(3) + ' mm';
  boreD.textContent = 'part + 0.03 clearance';
  stepR.textContent = stepDiam.toFixed(3) + ' mm';
  stepD.textContent = 'back-cut relief diameter';
  radialR.textContent = stepRadial.toFixed(3) + ' mm';
  radialD.textContent = 'radial step per side';
  contactR.textContent = contactWidth.toFixed(2) + ' mm';
  contactD.textContent = 'approx. arc width per jaw';
}

[partInput, stepInput, jawInput, boreInput].forEach((el) => el.addEventListener('input', solve));
solve();
