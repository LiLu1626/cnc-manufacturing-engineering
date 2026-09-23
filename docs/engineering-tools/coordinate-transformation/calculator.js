const tx = document.querySelector('#tx');
const ty = document.querySelector('#ty');
const angle = document.querySelector('#angle');
const mirrorX = document.querySelector('#mirrorX');
const mirrorY = document.querySelector('#mirrorY');
const inputPoints = document.querySelector('#inputPoints');
const resultBody = document.querySelector('#resultBody');

function calculate() {
  const txv = Number(tx.value);
  const tyv = Number(ty.value);
  const rad = Number(angle.value) * Math.PI / 180;
  const mX = Number(mirrorX.value);
  const mY = Number(mirrorY.value);
  const cos = Math.cos(rad);
  const sin = Math.sin(rad);

  const lines = inputPoints.value.trim().split('\n');
  resultBody.innerHTML = '';
  let i = 1;
  for (const line of lines) {
    const parts = line.trim().split(/[,;\s]+/).filter(Boolean);
    if (parts.length < 2) continue;
    let x = Number(parts[0]);
    let y = Number(parts[1]);
    if (isNaN(x) || isNaN(y)) continue;

    // Mirror first
    x *= mY;
    y *= mX;

    // Rotate
    const rx = x * cos - y * sin;
    const ry = x * sin + y * cos;

    // Translate
    const fx = rx + txv;
    const fy = ry + tyv;

    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${i}</td><td>${x.toFixed(3)}</td><td>${y.toFixed(3)}</td><td>${fx.toFixed(3)}</td><td>${fy.toFixed(3)}</td>`;
    resultBody.appendChild(tr);
    i++;
  }
}

[tx, ty, angle, mirrorX, mirrorY, inputPoints].forEach(el => el.addEventListener('input', calculate));
calculate();
