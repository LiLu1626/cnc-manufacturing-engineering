const toolLifeInput = document.querySelector('#toolLife');
const cutTimeInput = document.querySelector('#cutTime');
const quantityInput = document.querySelector('#quantity');
const reserveInput = document.querySelector('#reserve');
const partsPerToolEl = document.querySelector('#partsPerTool');
const toolsRequiredEl = document.querySelector('#toolsRequired');
const detailEl = document.querySelector('#detail');

function calculate() {
  const toolLife = Number(toolLifeInput.value);
  const cutTime = Number(cutTimeInput.value);
  const quantity = Number(quantityInput.value);
  const reserve = Number(reserveInput.value);

  if (toolLife <= 0 || cutTime <= 0 || quantity <= 0) {
    partsPerToolEl.textContent = 'Enter positive values';
    toolsRequiredEl.textContent = '—';
    detailEl.textContent = 'Tool life, cutting time, and quantity must all be greater than zero.';
    return;
  }

  const effectiveLife = toolLife * (1 - reserve / 100);
  const partsPerTool = Math.floor(effectiveLife / cutTime);

  if (partsPerTool < 1) {
    partsPerToolEl.textContent = '0';
    toolsRequiredEl.textContent = '—';
    detailEl.textContent = 'With a ' + reserve + '% reserve, the effective life of ' +
      effectiveLife.toFixed(1) + ' min does not cover one part of ' + cutTime + ' min. ' +
      'Reduce the reserve, extend the assumed tool life, or shorten the cut time.';
    return;
  }

  const toolsRequired = Math.ceil(quantity / partsPerTool);
  const fullTools = Math.floor(quantity / partsPerTool);
  const lastToolParts = quantity - fullTools * partsPerTool;

  let planText = 'Affected life: ' + effectiveLife.toFixed(1) +
    ' min after a ' + reserve + '% reserve. ' +
    partsPerTool + ' parts per tool. ';

  if (lastToolParts > 0) {
    planText += toolsRequired + ' tools planned: ' +
      fullTools + ' full tools and 1 partial tool for ' + lastToolParts + ' parts.';
  } else {
    planText += toolsRequired + ' full tools cover the planned quantity exactly.';
  }

  partsPerToolEl.textContent = partsPerTool;
  toolsRequiredEl.textContent = toolsRequired;
  detailEl.textContent = planText;
}

[toolLifeInput, cutTimeInput, quantityInput, reserveInput].forEach((input) => {
  input.addEventListener('input', calculate);
});

calculate();
