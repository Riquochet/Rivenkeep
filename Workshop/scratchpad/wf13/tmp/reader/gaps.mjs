// gaps.mjs (wf13 check): the space between neighbours on a romanised line (word boxes, marks), by kind, every fold
// open; and close shots of a blotted name, a dash in the reading, and the VI.3 token.   env PAGE, W
import fs from 'node:fs';
const R = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/';
const PAGES = { repo: 'file://' + R + 'out/Rivenkeep_Legends.html', web: 'file://' + R + 'tmp/reader/web_wrapped.html' };
const T = R + 'tmp/reader/shots/';
const page = process.env.PAGE || 'repo', W = +(process.env.W || 1280), H = W < 500 ? 844 : 900;
export default async function (t) {
  await t.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 500 });
  await t.nav(PAGES[page], 3000);
  await t.ev(`document.fonts.ready.then(()=>1)`);
  await t.ev(`document.getElementById('read-orig').click(); document.querySelectorAll('.p-orig details.tr.rom').forEach(d=>d.open=true); 1`);
  await t.sleep(900);
  const r = JSON.parse(await t.ev(`(function(){var st={},tok=[];
    function box(e){if(e.tagName==='I'){var s=e.querySelector('small');var rg=document.createRange();rg.setStartBefore(e.firstChild);rg.setEndBefore(s);var a=rg.getBoundingClientRect();return {l:a.left,r:a.right,t:a.top}}
      var b=e.getBoundingClientRect();return {l:b.left,r:b.right,t:b.top}}
    function kind(e){return e.tagName==='I'?(e.classList.contains('blot')?'blot':'word'):'mark'}
    document.querySelectorAll('.p-orig p.il').forEach(function(p){
      var els=[...p.querySelectorAll('i, span.m')].filter(e=>!e.closest('small'));
      for(var k=1;k<els.length;k++){var a=box(els[k-1]),b=box(els[k]);if(Math.abs(a.t-b.t)>12)continue;
        var key=kind(els[k-1])+'>'+kind(els[k]);var g=Math.round(b.l-a.r);var s=st[key]||(st[key]={n:0,min:1e9,max:-1e9,sum:0});s.n++;s.min=Math.min(s.min,g);s.max=Math.max(s.max,g);s.sum+=g}
      p.querySelectorAll('.tok i').forEach(function(i){var q=i.getBoundingClientRect(),pr=p.getBoundingClientRect();tok.push([i.textContent,Math.round(q.left),Math.round(q.right),Math.round(pr.right)])});
    });
    Object.values(st).forEach(s=>{s.avg=+(s.sum/s.n).toFixed(1);delete s.sum});
    var b=document.querySelector('.p-orig p.il i.blot');var bb=b.getBoundingClientRect();
    var d=[...document.querySelectorAll('#t-IV-4 .p-orig .reading p.il span.m')][2];var dd=d.getBoundingClientRect();
    var tk=document.querySelector('.p-orig p.il .tok');var tt=tk.closest('p.il').getBoundingClientRect();
    return JSON.stringify({gaps:st,tok:tok,blot:[bb.left,bb.top+scrollY,bb.width,bb.height],dash:[dd.left,dd.top+scrollY],tokp:[tt.left,tt.top+scrollY,tt.width,tt.height]})})()`));
  console.log(`[${page} ${W}] gaps`, JSON.stringify(r.gaps));
  console.log(`[${page} ${W}] token words`, JSON.stringify(r.tok));
  let n = 0;
  for (const [x, y, w, h, nm] of [[r.blot[0] - 140, r.blot[1] - 16, 440, 60, 'blot'], [r.dash[0] - 160, r.dash[1] - 16, 440, 60, 'dash'], [r.tokp[0], r.tokp[1] - 6, Math.min(r.tokp[2], W - r.tokp[0]), Math.min(r.tokp[3] + 12, 400), 'tok']]) {
    await t.ev(`window.scrollTo(0, ${Math.round(y - 300)})`); await t.sleep(400);
    const sh = await t.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0, x), y, width: Math.min(w, W - Math.max(0, x)), height: h, scale: nm === 'tok' ? 2 : 3 }, captureBeyondViewport: true });
    fs.writeFileSync(`${T}z_${nm}_${page}_${W}.png`, Buffer.from(sh.data, 'base64'));
  }
}
