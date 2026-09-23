const dims = document.querySelector('#dims');
const method = document.querySelector('#method');

function calculate() {
  const lines = dims.value.trim().split('\n');
  let nominal = 0;
  let sumTol = 0;
  let sumTolSq = 0;
  let count = 0;

  for (const line of lines) {
    const m = line.trim().match(/(-?[\d.]+)\s*±\s*([\d.]+)/);
    if (!m) continue;
    nominal += Number(m[1]);
    const t = Number(m[2]);
    sumTol += t;
    sumTolSq += t * t;
    count++;
  }

  if (count === 0) {
    document.querySelector('#nomResult').textContent = '—';
    document.querySelector('#tolResult').textContent = '—';
    document.querySelector('#rangeResult').textContent = '—';
    document.querySelector('#assessResult').textContent = '—';
    return;
  }

  let totalTol;
  if (method.value === 'worst') {
    totalTol = sumTol;
    document.querySelector('#tolDetail').textContent = `Worst-case: sum of ${count} tolerances`;
  } else {
    totalTol = Math.sqrt(sumTolSq);
    document.querySelector('#tolDetail').textContent = `RSS: √(Σtol²) of ${count} tolerances`;
  }

  document.querySelector('#nomResult').textContent = nominal.toFixed(3);
  document.querySelector('#tolResult').textContent = '±' + totalTol.toFixed(3);
  document.querySelector('#rangeResult').textContent = (nominal - totalTol).toFixed(3) + ' to ' + (nominal + totalTol).toFixed(3);

  let assess, detail;
  if (totalTol < 0.05) {
    assess = 'Very tight';
    detail = 'Difficult to hold economically. Consider design for manufacturing (DFM) review.';
  } else if (totalTol < 0.15) {
    assess = 'Tight';
    detail = 'Requires careful machining and CMM inspection. Feasible on good equipment.';
  } else if (totalTol < 0.5) {
    assess = 'Moderate';
    detail = 'Standard machining tolerance. No special process needed.';
  } else {
    assess = 'Loose';
    detail = 'Easy to hold. May indicate over-toleranced drawing.';
  }
  document.querySelector('#assessResult').textContent = assess;
  document.querySelector('#assessDetail').textContent = detail;
}

[dims, method].forEach(el => el.addEventListener('input', calculate));
calculate();
