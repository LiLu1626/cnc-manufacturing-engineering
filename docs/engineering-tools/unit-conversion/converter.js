const units = {
  length: {
    mm: ['Millimetre (mm)', 1],
    in: ['Inch (in)', 25.4],
    cm: ['Centimetre (cm)', 10],
    m: ['Metre (m)', 1000],
    ft: ['Foot (ft)', 304.8]
  },
  speed: {
    mmin: ['Metres per minute (m/min)', 1],
    sfm: ['Surface feet per minute (sfm)', 0.3048],
    msec: ['Metres per second (m/s)', 60]
  },
  feed: {
    mmmin: ['Millimetres per minute (mm/min)', 1],
    ipm: ['Inches per minute (ipm)', 25.4],
    mmrev: ['Millimetres per revolution (mm/rev)', 1],
    ipr: ['Inches per revolution (ipr)', 25.4]
  },
  torque: {
    nm: ['Newton metre (N·m)', 1],
    ftlb: ['Foot-pound force (ft·lbf)', 1.3558179483],
    inlb: ['Inch-pound force (in·lbf)', 0.112984829]
  },
  pressure: {
    bar: ['Bar', 1],
    psi: ['Pounds per square inch (psi)', 0.0689475729],
    mpa: ['Megapascal (MPa)', 10],
    kpa: ['Kilopascal (kPa)', 0.01]
  },
  temp: { c: ['Celsius (°C)'], f: ['Fahrenheit (°F)'] }
};

const type = document.querySelector('#type');
const value = document.querySelector('#value');
const from = document.querySelector('#from');
const to = document.querySelector('#to');
const result = document.querySelector('#result');
const detail = document.querySelector('#detail');

function calculate() {
  const input = Number(value.value);
  const group = units[type.value];

  if (!Number.isFinite(input)) {
    result.textContent = 'Enter a valid number';
    return;
  }

  let output;
  if (type.value === 'temp') {
    const celsius = from.value === 'f' ? (input - 32) * 5 / 9 : input;
    output = to.value === 'f' ? celsius * 9 / 5 + 32 : celsius;
  } else {
    output = input * group[from.value][1] / group[to.value][1];
  }

  const formatted = new Intl.NumberFormat(undefined, {
    maximumFractionDigits: 8
  }).format(output);

  result.textContent = formatted + ' ' + group[to.value][0];
  detail.textContent = input + ' ' + group[from.value][0] +
    ' = ' + formatted + ' ' + group[to.value][0];
}

function populateUnits() {
  const group = units[type.value];
  const options = Object.entries(group).map(([key, unit]) =>
    '<option value="' + key + '">' + unit[0] + '</option>'
  ).join('');

  from.innerHTML = options;
  to.innerHTML = options;
  to.selectedIndex = 1;

  if (type.value === 'temp') {
    value.value = 20;
    from.value = 'c';
    to.value = 'f';
  }

  calculate();
}

type.addEventListener('change', populateUnits);
value.addEventListener('input', calculate);
from.addEventListener('change', calculate);
to.addEventListener('change', calculate);
populateUnits();
