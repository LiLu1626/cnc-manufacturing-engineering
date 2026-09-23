const lengthInput = document.querySelector('#length');
const diameterInput = document.querySelector('#diameter');
const operationInput = document.querySelector('#operation');
const ratioElement = document.querySelector('#ratio');
const riskElement = document.querySelector('#risk');
const detailElement = document.querySelector('#detail');

function getRecommendation(ratio, operation) {
  const operationNotes = {
    finish: 'Finishing gives more flexibility, but reduce feed when chatter or witness marks appear.',
    general: 'For general milling, use conservative engagement when the ratio rises above 4:1.',
    rough: 'Roughing needs the largest rigidity margin; avoid high ratios or reduce the cutting load substantially.'
  };

  if (ratio <= 3) {
    return ['Low risk', 'A favourable starting ratio. Confirm holder condition and runout, then set parameters from the toolmaker recommendation.'];
  }

  if (ratio <= 4) {
    return ['Moderate risk', 'Usable for many operations. Keep the holder-to-tool interface clean and avoid unnecessary radial engagement.'];
  }

  if (ratio <= 5) {
    return ['Elevated risk', 'Reduce stick-out if possible. Use smaller engagement, observe for chatter, and favour a stable toolpath.'];
  }

  return ['High risk', 'Deflection and vibration are increasingly likely. Shorten the overhang, consider a larger diameter or a more rigid holder, and reduce load before cutting.'];
}

function calculateRisk() {
  const length = Number(lengthInput.value);
  const diameter = Number(diameterInput.value);
  const operation = operationInput.value;

  if (length <= 0 || diameter <= 0) {
    ratioElement.textContent = 'Enter positive values';
    riskElement.textContent = 'Input required';
    detailElement.textContent = 'Unsupported length and tool diameter must both be greater than zero.';
    return;
  }

  const ratio = length / diameter;
  const recommendation = getRecommendation(ratio, operation);

  ratioElement.textContent = ratio.toFixed(2) + ' : 1';
  riskElement.textContent = recommendation[0];
  detailElement.textContent = recommendation[1] + ' ' + operationNotes(operation);
}

function operationNotes(operation) {
  const notes = {
    finish: 'Finishing guidance: verify surface quality with a conservative trial cut.',
    general: 'General milling guidance: reduce engagement before reducing safety margin.',
    rough: 'Roughing guidance: consider a different setup when the ratio is high.'
  };

  return notes[operation];
}

[lengthInput, diameterInput, operationInput].forEach((input) => {
  input.addEventListener('input', calculateRisk);
  input.addEventListener('change', calculateRisk);
});

calculateRisk();
