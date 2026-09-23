const fitInput = document.getElementById('fitType');
const sizeInput = document.getElementById('sizeRange');

const designR = document.getElementById('designResult');
const typeR = document.getElementById('typeResult');
const appR = document.getElementById('appResult');
const methodR = document.getElementById('methodResult');
const designD = document.getElementById('designDetail');
const typeD = document.getElementById('typeDetail');
const appD = document.getElementById('appDetail');
const methodD = document.getElementById('methodDetail');

const data = {
  clearance: {
    design: 'H7/g6 or H7/h6',
    type: 'Clearance',
    app: 'Sliding bearings, guides, bushings',
    method: 'Hand assembly / soft mallet',
    d1: 'hole H7, shaft g6 or h6',
    d2: 'positive clearance always',
    d3: 'easy disassembly',
    d4: 'lubricate for moving parts'
  },
  transition: {
    design: 'H7/k6 or H7/js6',
    type: 'Transition',
    app: 'Gears, pulleys with key, precision location',
    method: 'Light press / drift',
    d1: 'hole H7, shaft k6 or js6',
    d2: 'tiny clearance or light interference',
    d3: 'requires drift press or soft hammer',
    d4: 'often with key or pin for torque'
  },
  interference: {
    design: 'H7/p6 or H7/s6',
    type: 'Interference',
    app: 'Permanent joints, bearing rings, gears',
    method: 'Press, heat housing, or freeze shaft',
    d1: 'hole H7, shaft p6 / s6',
    d2: 'shaft larger than hole',
    d3: 'hydraulic press or shrink fit',
    d4: 'not intended for disassembly'
  }
};

function solve() {
  const key = fitInput.value;
  const s = data[key];
  designR.textContent = s.design;
  designD.textContent = s.d1;
  typeR.textContent = s.type;
  typeD.textContent = s.d2;
  appR.textContent = s.app;
  appD.textContent = s.d3;
  methodR.textContent = s.method;
  methodD.textContent = s.d4;
}

[fitInput, sizeInput].forEach((el) => el.addEventListener('input', solve));
solve();
