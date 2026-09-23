const widthInput = document.querySelector('#widthOfCut');
const depthInput = document.querySelector('#depthOfCut');
const feedInput = document.querySelector('#feedRate');
const resultElement = document.querySelector('#result');
const detailElement = document.querySelector('#detail');

function calculateMRR() {
  const width = Number(widthInput.value);
  const depth = Number(depthInput.value);
  const feed = Number(feedInput.value);

  if (width <= 0 || depth <= 0 || feed <= 0) {
    resultElement.textContent = 'Enter positive values';
    detailElement.textContent = 'Width, depth, and feed rate must be greater than zero.';
    return;
  }

  const cubicMillimetresPerMinute = width * depth * feed;
  const cubicCentimetresPerMinute = cubicMillimetresPerMinute / 1000;

  resultElement.textContent =
    cubicMillimetresPerMinute.toLocaleString(undefined, {
      maximumFractionDigits: 1
    }) + ' mm³/min';
  detailElement.textContent =
    cubicCentimetresPerMinute.toFixed(2) + ' cm³/min';
}

[widthInput, depthInput, feedInput].forEach((input) => {
  input.addEventListener('input', calculateMRR);
});

calculateMRR();
