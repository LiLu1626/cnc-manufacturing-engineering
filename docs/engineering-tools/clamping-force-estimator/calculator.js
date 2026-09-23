const method = document.querySelector('#method');
const torque = document.querySelector('#torque');
const thread = document.querySelector('#thread');
const efficiency = document.querySelector('#efficiency');
const pressure = document.querySelector('#pressure');
const area = document.querySelector('#area');
const torqueField = document.querySelector('#torqueField');
const threadField = document.querySelector('#threadField');
const effField = document.querySelector('#effField');
const pressureField = document.querySelector('#pressureField');
const areaField = document.querySelector('#areaField');

// Bolt diameters by thread
const boltD = { '1.5': 8, '1.25': 10, '1.75': 12, '2.0': 16 };

function calculate() {
  if (method.value === 'screw') {
    torqueField.style.display = '';
    threadField.style.display = '';
    effField.style.display = '';
    pressureField.style.display = 'none';
    areaField.style.display = 'none';

    const T = Number(torque.value);
    const d = boltD[thread.value];
    const mu = Number(efficiency.value);
    // Approximate: F = (2*T) / (d/2 * (mu + ... )) — shop approximation
    // F ≈ T * 2*pi / (p / (2*pi) + mu * r_m)
    // Simplified: F ≈ (1.5 * T * 1000) / d  (rough estimate, corrected by friction)
    const pitch = Number(thread.value);
    const rm = d / 2; // mean radius approx
    const leadAngle = Math.atan(pitch / (2 * Math.PI * rm));
    const F = (2 * T) / ((pitch / (2 * Math.PI)) + mu * rm) * Math.cos(leadAngle) / 1000; // kN

    document.querySelector('#forceResult').textContent = F.toFixed(1) + ' kN';
    document.querySelector('#forceDetail').textContent = `M${d} bolt, pitch ${pitch} mm, μ=${mu}`;

    // Safety: compare to typical cutting forces
    let safety, detail;
    if (F > 15) {
      safety = 'Strong';
      detail = 'High clamping force. Suitable for heavy cuts. Watch for part deformation on thin walls.';
    } else if (F > 6) {
      safety = 'Good';
      detail = 'Adequate for most milling/turning. Ensure force is applied directly over support.';
    } else {
      safety = 'Light';
      detail = 'May not hold under heavy cuts. Increase torque, use more clamps, or check for slip.';
    }
    document.querySelector('#safetyResult').textContent = safety;
    document.querySelector('#safetyDetail').textContent = detail;
  } else {
    torqueField.style.display = 'none';
    threadField.style.display = 'none';
    effField.style.display = 'none';
    pressureField.style.display = '';
    areaField.style.display = '';

    const P = Number(pressure.value) * 0.1; // bar to N/mm²
    const A = Number(area.value) * 100; // cm² to mm²
    const F = P * A / 1000; // kN

    document.querySelector('#forceResult').textContent = F.toFixed(1) + ' kN';
    document.querySelector('#forceDetail').textContent = `${pressure.value} bar × ${area.value} cm² piston`;
    document.querySelector('#safetyResult').textContent = 'Hydraulic';
    document.querySelector('#safetyDetail').textContent = 'Consistent force. Check pressure gauge and cylinder condition regularly.';
  }
}

[method, torque, thread, efficiency, pressure, area].forEach(el => el.addEventListener('input', calculate));
calculate();
