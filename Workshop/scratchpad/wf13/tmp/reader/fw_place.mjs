// fw_place.mjs (wf13 check): the foreword's place through Book -> Plain -> Book with the sticky bar (real clicks).
// env W, OFF (the Book's dateline this far below the reading line), PAGEF
const R = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/';
const W = +(process.env.W || 1280), H = W < 500 ? 844 : 900, OFF = +(process.env.OFF || 4);
const T = R + 'tmp/reader/shots/';
export default async function (t) {
  await t.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 500 });
  const U = 'file://' + R + (process.env.PAGEF || 'out/Rivenkeep_Legends.html');
  await t.nav(U, 3000); await t.ev(`try{localStorage.clear()}catch(e){}`); await t.nav(U, 3000);
  await t.ev(`document.fonts.ready.then(()=>1)`);
  async function bar(k) { const p = await t.ev(`(()=>{const r=document.querySelector('.readbar label.l-${k}').getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]})()`); await t.click(p[0], p[1]); await t.sleep(700); }
  const where = `(()=>{const rl=document.querySelector('.bars').getBoundingClientRect().bottom+14;const f=document.getElementById('foreword');
    const o={scrollY:Math.round(scrollY),rl:Math.round(rl),leafTop:Math.round(f.getBoundingClientRect().top-rl)};
    ['book','plain'].forEach(k=>{const p=f.querySelector('.p-'+k);const r=p.getBoundingClientRect();o[k]={vis:!!p.getClientRects().length,paneTop:Math.round(r.top-rl)};
      const d=p.querySelector('[data-m="dl1"]');if(d)o[k].dl1=Math.round(d.getBoundingClientRect().top-rl);const n=p.querySelector('aside.newreaders');if(n)o[k].note=[Math.round(n.getBoundingClientRect().top-rl),Math.round(n.getBoundingClientRect().bottom-rl)]});
    const kids=[...f.children].map(c=>c.tagName+'.'+c.className+' '+Math.round(c.getBoundingClientRect().top-rl));o.kids=kids.slice(0,8);return JSON.stringify(o)})()`;
  await bar('book');
  for (let i = 0; i < 5; i++) { await t.ev(`(()=>{const rl=document.querySelector('.bars').getBoundingClientRect().bottom+14;const e=document.querySelector('#foreword .p-book [data-m="dl1"]');window.scrollBy(0,e.getBoundingClientRect().top-rl-(${OFF}));return 1})()`);
  await t.sleep(400); }
  console.log('book  ', await t.ev(where)); await t.shot(`${T}fw_place_${W}_${OFF}_1book.png`);
  await bar('plain');
  console.log('plain ', await t.ev(where)); await t.shot(`${T}fw_place_${W}_${OFF}_2plain.png`);
  await bar('book');
  console.log('book  ', await t.ev(where)); await t.shot(`${T}fw_place_${W}_${OFF}_3book.png`);
}
