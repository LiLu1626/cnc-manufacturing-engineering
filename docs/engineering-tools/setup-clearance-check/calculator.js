const holderType = document.querySelector('#holderType');
const holderD = document.querySelector('#holderD');
const toolLength = document.querySelector('#toolLength');
const fixtureHeight = document.querySelector('#fixtureHeight');
const partHeight = document.querySelector('#partHeight');
const workZ = document.querySelector('#workZ');

function calculate() {
  const holderOverhang = Number(holderType.value);
  const hD = Number(holderD.value);
  const protrusion = Number(toolLength.value);
  const fixH = Number(fixtureHeight.value);
  const partH = Number(partHeight.value);
  const wZ = Number(workZ.value);

  const totalReach = holderOverhang + protrusion;
  // Holder flange position above table = workZ - holderOverhang
  const flangeHeight = wZ - holderOverhang;
  // Tallest obstruction = fixture + part
  const obstacleTop = fixH + partH;
  const clearance = flangeHeight - obstacleTop;

  document.querySelector('#reachResult').textContent = totalReach + ' mm';
  document.querySelector('#reachDetail').textContent = `Holder ${holderOverhang} mm + tool ${protrusion} mm`;

  document.querySelector('#clearResult').textContent = clearance.toFixed(1) + ' mm';

  if (clearance < 0) {
    document.querySelector('#clearDetail').textContent = 'DANGER: Holder flange is below the part/fixture top. Crash risk! Shorten tool or raise work offset.';
  } else if (clearance < 5) {
    document.querySelector('#clearDetail').textContent = 'Tight clearance. Manually verify with dry run. Reduce protrusion if possible.';
  } else if (clearance < 15) {
    document.querySelector('#clearDetail').textContent = 'Acceptable clearance. Double-check corners and fixture posts.';
  } else {
    document.querySelector('#clearDetail').textContent = 'Good clearance. Safe for tool changes and moves.';
  }
}

[holderType, holderD, toolLength, fixtureHeight, partHeight, workZ].forEach(el => el.addEventListener('input', calculate));
calculate();
