// the sticky bar mid-tale: does the reader keep their place?  env PAGE, W
const R = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/';
const PAGES = { repo: 'file://' + R + 'out/Rivenkeep_Legends.html', web: 'file://' + R + 'tmp/reader/web_wrapped.html' };
const page = process.env.PAGE || 'repo', W = +(process.env.W || 1280), H = W < 500 ? 844 : 900;
const probe = `(function(){var b=document.querySelector('.bars').getBoundingClientRect().bottom+14;var el=null;for(var dy=6;dy<200;dy+=6){var h=document.elementFromPoint(innerWidth/2,b+dy);if(h&&!h.classList.contains('pane')&&!h.classList.contains('sw')&&h.closest('.pane')){el=h;break}}
  var k=el&&el.closest('[data-k],[data-m]');var pane=el&&el.closest('.pane');
  return JSON.stringify({y:Math.round(scrollY),k:k&&((k.getAttribute('data-k')||'')+'/'+(k.getAttribute('data-m')||'')),pane:pane&&pane.className.replace('pane ',''),txt:el&&el.textContent.trim().replace(/\\s+/g,' ').slice(0,50)})})()`;
async function rect(t, sel) { return JSON.parse(await t.ev(`JSON.stringify(document.querySelector(${JSON.stringify(sel)}).getBoundingClientRect())`)); }
async function bar(t, m) { const r = await rect(t, '.readbar .l-' + m); await t.click(r.x + r.width / 2, r.y + r.height / 2); await t.sleep(700); }
export default async function (t) {
  await t.size(W, H, W < 500);
  await t.nav(PAGES[page], 2500); await t.ev(`try{localStorage.clear()}catch(e){}`); await t.nav(PAGES[page], 2500);
  for (const [tale, n] of [['t-V-5', 30], ['t-II-2', 12], ['t-IV-3', 25], ['t-knowings', 8]]) {
    await bar(t, 'book');
    for (let i = 0; i < 4; i++) { await t.ev(`(function(){var e=document.querySelectorAll('#${tale} .p-book [data-k]')[${n}];var b=document.querySelector('.bars').getBoundingClientRect().bottom;window.scrollBy(0,e.getBoundingClientRect().top-b-14)})()`); await t.sleep(250); }
    const seq = [['book', await t.ev(probe)]];
    for (const m of ['plain', 'orig', 'book', 'orig', 'plain', 'book']) { await bar(t, m); seq.push([m, await t.ev(probe)]); }
    console.log(`[${page} ${W}] ${tale}#${n}`); for (const [m, p] of seq) console.log('   ', m.padEnd(5), p);
  }
}
