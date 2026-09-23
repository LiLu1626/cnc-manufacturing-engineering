const cuttingSpeed = document.querySelector('#cuttingSpeed');
const diameter = document.querySelector('#diameter');
const maxRpm = document.querySelector('#maxRpm');
const result = document.querySelector('#result');
const detail = document.querySelector('#detail');

function calculateRpm() {
  const speed = Number(cuttingSpeed.value);
  const toolDiameter = Number(diameter.value);
  const machineLimit = Number(maxRpm.value);

  if (speed <= 0 || toolDiameter <= 0) {
    result.textContent = 'Enter positive values';
    detail.textContent = '';
    return;
  }

  const calculatedRpm = (1000 * speed) / (Math.PI * toolDiameter);
  const limited = machineLimit > 0 && calculatedRpm > machineLimit;
  const output = limited ? machineLimit : calculatedRpm;

  result.textContent = Math.round(output).toLocaleString() + ' RPM';
  detail.textContent = limited
    ? 'Limited by the specified machine maximum RPM.'
    : 'Calculated from cutting speed and effective diameter.';
}

cuttingSpeed.addEventListener('input', calculateRpm);
diameter.addEventListener('input', calculateRpm);
maxRpm.addEventListener('input', calculateRpm);
calculateRpm();
