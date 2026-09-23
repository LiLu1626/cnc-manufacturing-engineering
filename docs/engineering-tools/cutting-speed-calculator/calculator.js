const diameterInput = document.querySelector('#diameter');
const rpmInput = document.querySelector('#rpm');
const resultElement = document.querySelector('#result');
const detailElement = document.querySelector('#detail');

function calculateCuttingSpeed() {
  const diameter = Number(diameterInput.value);
  const rpm = Number(rpmInput.value);

  if (diameter <= 0 || rpm <= 0) {
    resultElement.textContent = 'Enter positive values';
    detailElement.textContent = 'Tool diameter and spindle speed must be greater than zero.';
    return;
  }

  const cuttingSpeed = (Math.PI * diameter * rpm) / 1000;

  resultElement.textContent = cuttingSpeed.toFixed(1) + ' m/min';
  detailElement.textContent = 'Calculated from a ' + diameter + ' mm tool at ' + rpm + ' RPM.';
}

[diameterInput, rpmInput].forEach((input) => {
  input.addEventListener('input', calculateCuttingSpeed);
});

calculateCuttingSpeed();
