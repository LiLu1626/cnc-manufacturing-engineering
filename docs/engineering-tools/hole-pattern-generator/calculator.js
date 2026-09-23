const startXInput = document.getElementById('startX');
const startYInput = document.getElementById('startY');
const colsInput = document.getElementById('cols');
const rowsInput = document.getElementById('rows');
const xSpacingInput = document.getElementById('xSpacing');
const ySpacingInput = document.getElementById('ySpacing');
const orderInput = document.getElementById('order');

const totalResult = document.getElementById('totalResult');
const totalDetail = document.getElementById('totalDetail');
const spanResult = document.getElementById('spanResult');
const spanDetail = document.getElementById('spanDetail');
const tbody = document.querySelector('#coordTable tbody');

function calculate() {
  const sx = parseFloat(startXInput.value) || 0;
  const sy = parseFloat(startYInput.value) || 0;
  const cols = parseInt(colsInput.value) || 0;
  const rows = parseInt(rowsInput.value) || 0;
  const xs = parseFloat(xSpacingInput.value) || 0;
  const ys = parseFloat(ySpacingInput.value) || 0;
  const order = orderInput.value;

  if (cols < 1 || rows < 1) {
    totalResult.textContent = '—';
    totalDetail.textContent = '';
    spanResult.textContent = '—';
    spanDetail.textContent = '';
    tbody.innerHTML = '';
    return;
  }

  const total = cols * rows;
  const spanX = (cols - 1) * xs;
  const spanY = (rows - 1) * ys;

  totalResult.textContent = total + ' holes';
  totalDetail.textContent = cols + ' columns × ' + rows + ' rows';

  spanResult.textContent = spanX.toFixed(2) + ' × ' + spanY.toFixed(2) + ' mm';
  spanDetail.textContent = 'X span = ' + spanX.toFixed(2) + ', Y span = ' + spanY.toFixed(2);

  tbody.innerHTML = '';
  let num = 1;
  const holes = [];

  if (order === 'row') {
    for (let r = 1; r <= rows; r++) {
      for (let c = 1; c <= cols; c++) {
        holes.push({ num: num++, row: r, col: c, x: sx + (c - 1) * xs, y: sy + (r - 1) * ys });
      }
    }
  } else {
    for (let c = 1; c <= cols; c++) {
      for (let r = 1; r <= rows; r++) {
        holes.push({ num: num++, row: r, col: c, x: sx + (c - 1) * xs, y: sy + (r - 1) * ys });
      }
    }
  }

  holes.forEach((h) => {
    const tr = document.createElement('tr');
    const cells = [h.num, h.row, h.col, h.x.toFixed(3), h.y.toFixed(3)];
    cells.forEach((val) => {
      const td = document.createElement('td');
      td.textContent = val;
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
}

[startXInput, startYInput, colsInput, rowsInput, xSpacingInput, ySpacingInput, orderInput].forEach((el) => {
  el.addEventListener('input', calculate);
});

calculate();
