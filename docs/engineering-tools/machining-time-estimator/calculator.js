const cuttingLengthInput = document.querySelector('#length');
const feedRateInput = document.querySelector('#feedRate');
const additionalTimeInput = document.querySelector('#allowance');
const resultElement = document.querySelector('#result');
const detailElement = document.querySelector('#detail');

function formatDuration(totalSeconds) {
  const roundedSeconds = Math.round(totalSeconds);
  const minutes = Math.floor(roundedSeconds / 60);
  const seconds = roundedSeconds % 60;

  if (minutes === 0) {
    return seconds + ' s';
  }

  return minutes + ' min ' + seconds + ' s';
}

function calculateMachiningTime() {
  const cuttingLength = Number(cuttingLengthInput.value);
  const feedRate = Number(feedRateInput.value);
  const additionalTime = Number(additionalTimeInput.value);

  if (cuttingLength <= 0 || feedRate <= 0 || additionalTime < 0) {
    resultElement.textContent = 'Enter valid positive values';
    detailElement.textContent = 'Cutting length and feed rate must be greater than zero.';
    return;
  }

  const cuttingTimeSeconds = (cuttingLength / feedRate) * 60;
  const estimatedCycleTimeSeconds = cuttingTimeSeconds + additionalTime;

  resultElement.textContent = formatDuration(estimatedCycleTimeSeconds);
  detailElement.textContent =
    'Cutting time: ' + cuttingTimeSeconds.toFixed(1) +
    ' s + additional time: ' + additionalTime.toFixed(1) + ' s.';
}

const inputs = [
  cuttingLengthInput,
  feedRateInput,
  additionalTimeInput
];

inputs.forEach((input) => {
  input.addEventListener('input', calculateMachiningTime);
});

calculateMachiningTime();
