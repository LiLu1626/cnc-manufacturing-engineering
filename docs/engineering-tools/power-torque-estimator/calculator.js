const mrrInput = document.querySelector('#mrr');
const energyInput = document.querySelector('#specificEnergy');
const rpmInput = document.querySelector('#rpm');
const powerResult = document.querySelector('#powerResult');
const torqueResult = document.querySelector('#torqueResult');

function calculatePowerAndTorque() {
  const mrr = Number(mrrInput.value);
  const specificEnergy = Number(energyInput.value);
  const rpm = Number(rpmInput.value);

  if (mrr <= 0 || specificEnergy <= 0 || rpm <= 0) {
    powerResult.textContent = 'Enter positive values';
    torqueResult.textContent = 'MRR, specific energy, and RPM must be greater than zero.';
    return;
  }

  const powerKilowatts = (mrr * specificEnergy) / 60;
  const torqueNewtonMetres = (9549 * powerKilowatts) / rpm;

  powerResult.textContent = powerKilowatts.toFixed(2) + ' kW';
  torqueResult.textContent = 'Estimated spindle torque: ' + torqueNewtonMetres.toFixed(2) + ' N·m';
}

[mrrInput, energyInput, rpmInput].forEach((input) => {
  input.addEventListener('input', calculatePowerAndTorque);
});

calculatePowerAndTorque();
