// blot.mjs (wf13 check): the blotted name inside an interlinear line: its box, the gap to the next word, a close shot
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
  await t.sleep(800);
  const r = JSON.parse(await t.ev(`(function(){var out=[];
    document.querySelectorAll('.p-orig p.il').forEach(function(p){[...p.childNodes].forEach(function(nd){
      if(nd.nodeType!==3||!/[\\u2592\\[\\u2014]/.test(nd.textContent))return;var rg=document.createRange();rg.selectNodeContents(nd);
      var t=nd.textContent;var m=t.search(/\\S/);var e=t.length-t.slice().split('').reverse().join('').search(/\\S/);
      var rg2=document.createRange();rg2.setStart(nd,m);rg2.setEnd(nd,e);var b=rg2.getBoundingClientRect();
      var nx=nd.nextElementSibling&&nd.nextSibling.nextSibling;var nb=nd.nextElementSibling?nd.nextElementSibling.getBoundingClientRect():null;
      var pv=nd.previousElementSibling?nd.previousElementSibling.getBoundingClientRect():null;
      var fam=getComputedStyle(p).fontFamily;
      out.push({leaf:(p.closest('[id^=t-]')||{}).id,txt:t.trim(),w:Math.round(b.width),gapNext:nb&&Math.abs(nb.top-b.top)<30?Math.round(nb.left-b.right):null,gapPrev:pv&&Math.abs(pv.top-b.top)<30?Math.round(b.left-pv.right):null,x:Math.round(b.left),y:Math.round(b.top+scrollY),h:Math.round(b.height)})})});
    return JSON.stringify(out)})()`));
  const blots = r.filter(x => x.txt.includes('▒'));
  console.log('loose marks', r.length, 'blots', blots.length);
  for (const x of r.slice(0, 60)) console.log(JSON.stringify(x));
  // a close shot of the first two blots
  let n = 0;
  for (const b of blots.slice(0, 2)) {
    await t.ev(`window.scrollTo(0, ${b.y - 300})`); await t.sleep(400);
    const sy = await t.ev('scrollY');
    const sh = await t.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0, b.x - 120), y: b.y - 20, width: Math.min(W - Math.max(0, b.x - 120), 420), height: 70, scale: 3 }, captureBeyondViewport: true });
    fs.writeFileSync(`${T}z_blot_${page}_${W}_${n++}.png`, Buffer.from(sh.data, 'base64'));
  }
}
