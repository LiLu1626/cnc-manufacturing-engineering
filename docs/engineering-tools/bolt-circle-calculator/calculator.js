const centerXInput = document.getElementById('centerX');
const centerYInput = document.getElementById('centerY');
const pcdInput = document.getElementById('pcd');
const holeCountInput = document.getElementById('holeCount');
const startAngleInput = document.getElementById('startAngle');
const directionInput = document.getElementById('direction');

const radiusResult = document.getElementById('radiusResult');
const radiusDetail = document.getElementById('radiusDetail');
const spacingResult = document.getElementById('spacingResult');
const spacingDetail = document.getElementById('spacingDetail');
const tbody = document.querySelector('#coordTable tbody');

function calculate() {
  const cx = parseFloat(centerXInput.value) || 0;
  const cy = parseFloat(centerYInput.value) || 0;
  const pcd = parseFloat(pcdInput.value) || 0;
  const n = parseInt(holeCountInput.value) || 0;
  const start = parseFloat(startAngleInput.value) || 0;
  const dir = directionInput.value;

  if (pcd <= 0 || n < 2) {
    radiusResult.textContent = '—';
    radiusDetail.textContent = '';
    spacingResult.textContent = '—';
    spacingDetail.textContent = '';
    tbody.innerHTML = '';
    return;
  }

  const R = pcd / 2;
  const spacing = 360 / n;
  const sign = dir === 'cw' ? -1 : 1;

  radiusResult.textContent = R.toFixed(3) + ' mm';
  radiusDetail.textContent = 'R = PCD / 2 = ' + pcd.toFixed(2) + ' / 2';

  spacingResult.textContent = spacing.toFixed(3) + '°';
  spacingDetail.textContent = '360° / ' + n + ' holes' + (dir === 'cw' ? ' (clockwise)' : ' (counter-clockwise)');

  tbody.innerHTML = '';
  for (let i = 0; i < n; i++) {
    const angle = start + sign * i * spacing;
    const rad = angle * Math.PI / 180;
    const x = cx + R * Math.cos(rad);
    const y = cy + R * Math.sin(rad);

    const tr = document.createElement('tr');
    const tdNum = document.createElement('td');
    tdNum.textContent = (i + 1);
    const tdAngle = document.createElement('td');
    tdAngle.textContent = angle.toFixed(3) + '°';
    const tdX = document.createElement('td');
    tdX.textContent = x.toFixed(3);
    const tdY = document.createElement('td');
    tdY.textContent = y.toFixed(3);
    tr.appendChild(tdNum);
    tr.appendChild(tdAngle);
    tr.appendChild(tdX);
    tr.appendChild(tdY);
    tbody.appendChild(tr);
  }
}

[centerXInput, centerYInput, pcdInput, holeCountInput, startAngleInput, directionInput].forEach((el) => {
  el.addEventListener('input', calculate);
});

calculate();
