// plain.mjs (wf13 check): Plain Words as a reader sees it.  node cdp.mjs plain.mjs   env PAGE=repo|web, W, SCREENS
// A real click on the sticky bar's 'Plain Words'; then viewport shots (the bars included) of the foreword's note for
// new readers and the openings of I.1, II.3 and IV.4, SCREENS screens each; and the note's and the leaves' text.
import fs from 'node:fs';
const R = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/';
const PAGES = { repo: 'file://' + R + 'out/Rivenkeep_Legends.html', web: 'file://' + R + 'tmp/reader/web_wrapped.html' };
const T = R + 'tmp/reader/shots/';
const page = process.env.PAGE || 'repo', W = +(process.env.W || 1280), H = W < 500 ? 844 : 900;
const DPR = W < 500 ? 2 : 1, SCREENS = +(process.env.SCREENS || 2);
async function rect(t, sel) { return JSON.parse(await t.ev(`JSON.stringify(document.querySelector(${JSON.stringify(sel)}).getBoundingClientRect())`)); }
async function under(t, sel, extra = 0) {
  for (let i = 0; i < 4; i++) {
    const d = await t.ev(`(function(){var e=document.querySelector(${JSON.stringify(sel)});var b=document.querySelector('.bars').getBoundingClientRect().bottom;
      var dy=e.getBoundingClientRect().top-b-12+(${extra});if(Math.abs(dy)>1)window.scrollBy(0,dy);return Math.round(dy)})()`);
    await t.sleep(250); if (Math.abs(d) <= 1) break;
  }
}
export default async function (t) {
  await t.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: DPR, mobile: W < 500 });
  await t.nav(PAGES[page], 3000); await t.ev(`try{localStorage.clear()}catch(e){}`); await t.nav(PAGES[page], 3000);
  await t.ev(`document.fonts.ready.then(()=>1)`);
  const r = await rect(t, '.readbar .l-plain'); await t.click(r.x + r.width / 2, r.y + r.height / 2); await t.sleep(600);
  console.log('mode', await t.ev(`document.querySelector('input[name=read]:checked').id`));
  const text = {};
  for (const [name, sel] of [['fw_note', '#foreword .p-plain aside.newreaders'], ['I1', '#t-I-1 .p-plain'], ['II3', '#t-II-3 .p-plain'], ['IV4', '#t-IV-4 .p-plain']]) {
    await under(t, sel, name === 'fw_note' ? -40 : 0);
    for (let k = 0; k < SCREENS; k++) {
      if (k) await t.ev(`window.scrollBy(0, ${Math.round((H - 120) * 0.92)})`);
      await t.sleep(300);
      await t.shot(`${T}p_${name}_${k}_${page}_${W}.png`);
    }
    text[name] = await t.ev(`(function(){var e=document.querySelector(${JSON.stringify(sel)});return [...e.querySelectorAll('h2,h3,h4,p,li,figcaption,.verse')].filter(x=>x.getClientRects().length).map(x=>x.tagName+'.'+x.className+': '+x.textContent.trim().replace(/\\s+/g,' ')).join('\\n')})()`);
  }
  fs.writeFileSync(`${T}p_text_${page}_${W}.txt`, Object.entries(text).map(([k, v]) => '## ' + k + '\n' + v).join('\n\n'));
  console.log(await t.ev(`JSON.stringify({docSW:document.documentElement.scrollWidth,vw:document.documentElement.clientWidth})`));
}
