// il.mjs (wf13 check): the interlinear romanisation as a reader sees it.  node cdp.mjs il.mjs   env PAGE=repo|web, W
//  1. a real click on the sticky bar's 'Original'; real clicks on the summaries of the folds to be shown
//  2. screenshots (what the reader sees: viewport shots, the bars included) of I.1's headnote and first story fold,
//     IV.3's first two voiced folds, and IV.4's reading with every fold open
//  3. then every fold on the page open: the geometry of every word box (gloss under its word, left-aligned with it,
//     no overlap with its neighbour, nothing past the line's right edge or the viewport, rows not colliding)
const R = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/';
const PAGES = { repo: 'file://' + R + 'out/Rivenkeep_Legends.html', web: 'file://' + R + 'tmp/reader/web_wrapped.html' };
const T = R + 'tmp/reader/shots/';
const page = process.env.PAGE || 'repo', W = +(process.env.W || 1280), H = W < 500 ? 844 : 900;
const DPR = W < 500 ? 2 : 1;
async function rect(t, sel) { return JSON.parse(await t.ev(`JSON.stringify(document.querySelector(${JSON.stringify(sel)}).getBoundingClientRect())`)); }
async function clickSel(t, sel) { const r = await rect(t, sel); await t.click(r.x + Math.min(r.width / 2, 60), r.y + r.height / 2); await t.sleep(350); }
async function under(t, sel, extra = 0) {   // put sel's top just under the sticky bars
  for (let i = 0; i < 4; i++) {
    const d = await t.ev(`(function(){var e=document.querySelector(${JSON.stringify(sel)});var b=document.querySelector('.bars').getBoundingClientRect().bottom;
      var dy=e.getBoundingClientRect().top-b-12+(${extra});if(Math.abs(dy)>1)window.scrollBy(0,dy);return Math.round(dy)})()`);
    await t.sleep(250); if (Math.abs(d) <= 1) break;
  }
}
async function shot(t, name) { await t.sleep(250); await t.shot(`${T}${name}_${page}_${W}.png`); }
export default async function (t) {
  await t.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: DPR, mobile: W < 500 });
  await t.nav(PAGES[page], 3000); await t.ev(`try{localStorage.clear()}catch(e){}`); await t.nav(PAGES[page], 3000);
  await t.ev(`document.fonts.ready.then(()=>1)`);
  await clickSel(t, '.readbar .l-orig');
  console.log('mode', await t.ev(`document.querySelector('input[name=read]:checked').id`));
  // ---- I.1: the headnote's fold and the first story paragraph's fold, opened by clicking their summaries
  for (const k of ['b189', 'b193']) {
    await under(t, `#t-I-1 .p-orig [data-k="${k}"] summary`, -H * 0.25);
    await clickSel(t, `#t-I-1 .p-orig [data-k="${k}"] summary`);
  }
  await under(t, '#t-I-1 .p-orig [data-k="b189"]');
  await shot(t, 'o_I1_a');
  await under(t, '#t-I-1 .p-orig [data-k="b193"]');
  await shot(t, 'o_I1_b');
  // ---- IV.3: Halyna's leaf, the first two long voiced folds
  for (const k of ['b1302', 'b1304']) {
    await under(t, `#t-IV-3 .p-orig [data-k="${k}"] summary`, -H * 0.25);
    await clickSel(t, `#t-IV-3 .p-orig [data-k="${k}"] summary`);
  }
  await under(t, '#t-IV-3 .p-orig [data-k="b1302"]');
  await shot(t, 'o_IV3_a');
  await under(t, '#t-IV-3 .p-orig [data-k="b1302"] details .tr-body', 0);
  await t.ev(`window.scrollBy(0, ${Math.round(H * 0.55)})`);
  await shot(t, 'o_IV3_b');
  // ---- IV.4: the wood leaf's reading, every fold in it open (clicked)
  const nr = await t.ev(`document.querySelectorAll('#t-IV-4 .p-orig .reading details.tr.rom').length`);
  for (let i = 0; i < nr; i++) {
    const sel = `#t-IV-4 .p-orig .reading .ip:nth-of-type(${i + 1}) summary`;
    const ok = await t.ev(`!!document.querySelector(${JSON.stringify(sel)})`);
    if (!ok) { console.log('no', sel); continue; }
    await under(t, sel, -H * 0.3);
    await clickSel(t, sel);
  }
  console.log('IV.4 reading folds', nr, 'open', await t.ev(`[...document.querySelectorAll('#t-IV-4 .p-orig .reading details.tr.rom')].filter(d=>d.open).length`));
  await under(t, '#t-IV-4 .p-orig .reading');
  await shot(t, 'o_IV4_a');
  for (let k = 1; k <= 4; k++) {
    const more = await t.ev(`(function(){var r=document.querySelector('#t-IV-4 .p-orig .reading').getBoundingClientRect();return r.bottom>${H}})()`);
    if (!more) break;
    await t.ev(`window.scrollBy(0, ${Math.round(H * 0.8)})`);
    await shot(t, 'o_IV4_' + 'bcde'[k - 1]);
  }
  // ---- every fold on the page open: the geometry of every word box
  await t.ev(`document.querySelectorAll('details').forEach(x=>x.open=true); 1`);
  await t.ev(`(function(){var st=document.createElement('style');st.id='__cv';st.textContent='*{content-visibility:visible!important}';document.head.appendChild(st);return 1})()`);
  await t.sleep(1500);
  const g = await t.ev(`(function(){
    var de=document.documentElement,Wv=de.clientWidth,o={vw:Wv,docSW:de.scrollWidth,bodySW:document.body.scrollWidth,lines:0,words:0,wrapped:0,maxRows:0,
      notUnder:[],notLeft:[],overlap:[],pastLine:[],pastView:[],clipped:[],rowsCollide:[],dashOff:[],widest:0,widestGap:0,glossWider:0};
    document.querySelectorAll('.p-orig p.il').forEach(function(p){
      var pr=p.getBoundingClientRect();if(!pr.width)return;o.lines++;
      var leaf=(p.closest('section[id],.leaf[id],[id^=t-]')||{}).id;
      var is=[...p.querySelectorAll(':scope > i')];var rows=[];
      is.forEach(function(i,n){o.words++;var q=i.getBoundingClientRect(),s=i.querySelector('small'),sr=s.getBoundingClientRect();
        // the word's own text: a range over the i's nodes before the small
        var rg=document.createRange();rg.setStartBefore(i.firstChild);rg.setEndBefore(s);var wr=rg.getBoundingClientRect();
        if(sr.top<wr.bottom-2&&o.notUnder.length<8)o.notUnder.push([leaf,i.textContent,Math.round(sr.top-wr.bottom)]);
        if(Math.abs(sr.left-wr.left)>1.5&&o.notLeft.length<8)o.notLeft.push([leaf,i.textContent,Math.round(sr.left-wr.left)]);
        if(sr.width>wr.width+1)o.glossWider++;
        if(q.right>pr.right+1&&o.pastLine.length<8)o.pastLine.push([leaf,i.textContent,Math.round(q.right-pr.right)]);
        if((q.right>Wv-15.5||q.left<15.5)&&o.pastView.length<8)o.pastView.push([leaf,i.textContent,Math.round(q.left),Math.round(q.right)]);
        if(s.scrollWidth>s.clientWidth+1&&o.clipped.length<8)o.clipped.push([leaf,i.textContent]);
        o.widest=Math.max(o.widest,Math.round(q.width));
        var top=Math.round(q.top);var row=rows.find(r=>Math.abs(r.top-top)<3);if(!row){row={top:top,bottom:q.bottom,items:[]};rows.push(row)}row.bottom=Math.max(row.bottom,q.bottom);row.items.push(q);
      });
      rows.sort((a,b)=>a.top-b.top);
      rows.forEach(function(r,n){r.items.sort((a,b)=>a.left-b.left);for(var k=1;k<r.items.length;k++){var gap=r.items[k].left-r.items[k-1].right;
          if(gap<1&&o.overlap.length<8)o.overlap.push([leaf,Math.round(gap)]);}
        if(n&&r.top<rows[n-1].bottom-0.5&&o.rowsCollide.length<8)o.rowsCollide.push([leaf,Math.round(r.top-rows[n-1].bottom)])});
      if(rows.length>1)o.wrapped++;o.maxRows=Math.max(o.maxRows,rows.length);
      // loose marks between words (a dash, a gap): on the words' baseline row, not floating
      [...p.childNodes].forEach(function(nd){if(nd.nodeType===3&&nd.textContent.trim()){var rg=document.createRange();rg.selectNodeContents(nd);var rr=rg.getClientRects();
        [...rr].forEach(function(b){if(!b.width)return;var row=rows.find(r=>b.top>=r.top-4&&b.top<=r.bottom);if(!row&&o.dashOff.length<8)o.dashOff.push([leaf,nd.textContent.trim().slice(0,10)]);});}});
    });
    return JSON.stringify(o)})()`);
  console.log(`[${page} ${W}] geometry`, g);
  // the type sizes a reader gets: the word, the gloss, the ink line above
  console.log(`[${page} ${W}] sizes`, await t.ev(`(function(){var i=document.querySelector('#t-I-1 .p-orig p.il i'),s=i.querySelector('small'),ink=document.querySelector('#t-I-1 .p-orig [data-k=b193] p.ink');
    var ci=getComputedStyle(i),cs=getComputedStyle(s),ck=getComputedStyle(ink),cp=getComputedStyle(i.parentElement);
    return JSON.stringify({word:[ci.fontFamily,ci.fontSize,ci.fontStyle,ci.color],gloss:[cs.fontFamily,cs.fontSize,cs.color],line:[cp.lineHeight],ink:[ck.fontFamily,ck.fontSize]})})()`));
}
