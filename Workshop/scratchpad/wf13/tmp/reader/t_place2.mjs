// t_place.mjs (wf13): the place-keeping script with Plain Words v3.1: put a landmark at the reading line, switch with
// the sticky bar (a real click), and see where its partner lands; then switch back and measure the drift.
const S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13';
const OFF = +(process.env.OFF || -4);
export default async function (t) {
  const W = +(process.env.W || 390), H = +(process.env.H || 844);
  await t.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 700 });
  await t.nav(process.env.PAGEURL || ('file://' + S + '/out/Rivenkeep_Legends.html'), 3000);
  await t.ev(`document.fonts.ready.then(()=>1)`);
  const cases = process.env.CASES ? JSON.parse(process.env.CASES) : [['foreword', 'dl1'], ['t-I-1', 'dl1'], ['t-II-2', 'hn1'], ['t-IV-4', 'rd1'], ['t-V-4', 'dl1'], ['t-epilogue', 'dl1'], ['t-last-note', 'hn1'], ['t-IV-3', 'ans2'], ['t-II-3', 'dl1'], ['t-II-3', 'hn1']];
  async function clickLabel(k) {
    const p = await t.ev(`(()=>{const r=document.querySelector('.readbar label.l-${k}').getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]})()`);
    await t.click(p[0], p[1]); await t.sleep(500);
  }
  for (const [id, m] of cases) {
    await clickLabel('book');
    const pos = await t.ev(`(()=>{const b=document.querySelector('.bars');const rl=b.getBoundingClientRect().bottom+14;
      const e=document.querySelector('#${id} .p-book [data-m="${m}"]');if(!e)return null;
      window.scrollBy(0,e.getBoundingClientRect().top-rl+(${OFF}));return [Math.round(e.getBoundingClientRect().top-rl)]})()`);
    if (!pos) { console.log(id, m, 'no landmark in the Book'); continue; }
    for (let i = 0; i < 4; i++) { await t.sleep(350); pos[0] = await t.ev(`(()=>{const b=document.querySelector('.bars');const rl=b.getBoundingClientRect().bottom+14;
      const e=document.querySelector('#${id} .p-book [data-m="${m}"]');window.scrollBy(0,e.getBoundingClientRect().top-rl+(${OFF}));return Math.round(e.getBoundingClientRect().top-rl)})()`); }
    await t.sleep(300);
    pos[0] = await t.ev(`(()=>{const rl=document.querySelector('.bars').getBoundingClientRect().bottom+14;return Math.round(document.querySelector('#${id} .p-book [data-m="${m}"]').getBoundingClientRect().top-rl)})()`);
    await clickLabel('plain');
    const inPlain = await t.ev(`(()=>{const b=document.querySelector('.bars');const rl=b.getBoundingClientRect().bottom+14;
      const e=document.querySelector('#${id} .p-plain [data-m="${m}"]');return e?Math.round(e.getBoundingClientRect().top-rl):null})()`);
    await clickLabel('book');
    const back = await t.ev(`(()=>{const b=document.querySelector('.bars');const rl=b.getBoundingClientRect().bottom+14;
      const e=document.querySelector('#${id} .p-book [data-m="${m}"]');return Math.round(e.getBoundingClientRect().top-rl)})()`);
    console.log(id, m, 'book', pos[0], '-> plain', inPlain, '-> book', back);
  }
}
