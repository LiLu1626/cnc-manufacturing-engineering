const dInput = document.getElementById('workD');
const vcInput = document.getElementById('vc');
const fInput = document.getElementById('frev');
const apInput = document.getElementById('depth');

const rpmR = document.getElementById('rpmResult');
const feedR = document.getElementById('feedResult');
const vcR = document.getElementById('vcResult');
const mrrR = document.getElementById('mrrResult');
const rpmD = document.getElementById('rpmDetail');
const feedD = document.getElementById('feedDetail');
const vcD = document.getElementById('vcDetail');
const mrrD = document.getElementById('mrrDetail');

function solve() {
  const D = parseFloat(dInput.value);
  const Vc = parseFloat(vcInput.value);
  const f = parseFloat(fInput.value);
  const ap = parseFloat(apInput.value);

  if (isNaN(D) || isNaN(Vc) || isNaN(f)) {
    rpmR.textContent = '—'; rpmD.textContent = 'Enter diameter, Vc, and feed';
    feedR.textContent = '—'; feedD.textContent = '';
    vcR.textContent = '—'; vcD.textContent = '';
    mrrR.textContent = '—'; mrrD.textContent = '';
    return;
  }

  const rpm = 1000 * Vc / (Math.PI * D);
  const feed = rpm * f;
  const actualVc = Math.PI * D * rpm / 1000;

  rpmR.textContent = Math.round(rpm) + ' RPM';
  rpmD.textContent = 'target spindle speed';
  feedR.textContent = feed.toFixed(0) + ' mm/min';
  feedD.textContent = 'RPM × feed/rev';
  vcR.textContent = actualVc.toFixed(1) + ' m/min';
  vcD.textContent = 'surface speed at this RPM';

  if (!isNaN(ap) && ap > 0) {
    // Q in cm^3/min = feed(mm/min) * ap(mm) * f(mm/rev) / 1000
    const mrr = feed * ap * f / 1000;
    mrrR.textContent = mrr.toFixed(1) + ' cm³/min';
    mrrD.textContent = 'needs ap = ' + ap + ' mm';
  } else {
    mrrR.textContent = '—';
    mrrD.textContent = 'enter depth of cut for MRR';
  }
}

[dInput, vcInput, fInput, apInput].forEach((el) => el.addEventListener('input', solve));
solve();
