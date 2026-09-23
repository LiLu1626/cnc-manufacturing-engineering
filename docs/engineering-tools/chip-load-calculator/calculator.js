const feedInput = document.querySelector('#feed');
const rpmInput = document.querySelector('#rpm');
const flutesInput = document.querySelector('#flutes');
const resultElement = document.querySelector('#result');
const detailElement = document.querySelector('#detail');

function calculateChipLoad() {
  const feed = Number(feedInput.value);
  const rpm = Number(rpmInput.value);
  const flutes = Number(flutesInput.value);

  if (feed <= 0 || rpm <= 0 || flutes <= 0) {
    resultElement.textContent = 'Enter positive values';
    detailElement.textContent = 'Feed rate, spindle speed, and active cutting edges must all be greater than zero.';
    return;
  }

  const chipLoad = feed / (rpm * flutes);

  resultElement.textContent = chipLoad.toFixed(3) + ' mm/tooth';
  detailElement.textContent = 'Feed rate ' + feed + ' mm/min ÷ (' + rpm + ' RPM × ' + flutes + ' edges).';
}

[feedInput, rpmInput, flutesInput].forEach((input) => {
  input.addEventListener('input', calculateChipLoad);
});

calculateChipLoad();
