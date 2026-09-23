const chipLoad = document.querySelector('#chipLoad');
const teeth = document.querySelector('#teeth');
const rpm = document.querySelector('#rpm');
const result = document.querySelector('#result');
const detail = document.querySelector('#detail');

function calculateFeedRate() {
  const load = Number(chipLoad.value);
  const toothCount = Number(teeth.value);
  const spindleSpeed = Number(rpm.value);

  if (load <= 0 || toothCount <= 0 || spindleSpeed <= 0) {
    result.textContent = 'Enter positive values';
    detail.textContent = '';
    return;
  }

  const feedRate = load * toothCount * spindleSpeed;

  result.textContent = feedRate.toLocaleString() + ' mm/min';
  detail.textContent =
    load + ' mm/tooth × ' + toothCount + ' teeth × ' +
    spindleSpeed.toLocaleString() + ' RPM';
}

chipLoad.addEventListener('input', calculateFeedRate);
teeth.addEventListener('input', calculateFeedRate);
rpm.addEventListener('input', calculateFeedRate);

calculateFeedRate();
