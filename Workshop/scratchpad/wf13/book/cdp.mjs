// cdp.mjs - drive headless Chrome over the DevTools protocol (wf12 scratch, wf13's copy; never in Docs/).
//   node cdp.mjs SCRIPT.mjs   -- SCRIPT exports default async function(t) using t.ev, t.shot, t.nav, t.size, t.click, t.wait
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
const CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = 9300 + Math.floor(Math.random() * 500);
const udd = fs.mkdtempSync('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/tmp/cdp-');
const proc = spawn(CH, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--remote-debugging-port=' + port,
  '--user-data-dir=' + udd, '--allow-file-access-from-files', '--no-first-run', '--window-size=1280,900', 'about:blank'],
  { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ws, id = 0; const pending = new Map(); const events = [];
async function connect() {
  for (let i = 0; i < 100; i++) {
    try { const r = await fetch(`http://127.0.0.1:${port}/json/list`); const j = await r.json();
      const pg = j.find(x => x.type === 'page'); if (pg) return pg.webSocketDebuggerUrl; } catch (e) {}
    await sleep(150);
  }
  throw new Error('no chrome');
}
function send(method, params = {}) {
  return new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
}
const url = await connect();
ws = new WebSocket(url);
await new Promise(r => ws.addEventListener('open', r));
ws.addEventListener('message', m => { const d = JSON.parse(m.data);
  if (d.id && pending.has(d.id)) { const p = pending.get(d.id); pending.delete(d.id); d.error ? p.rej(new Error(JSON.stringify(d.error))) : p.res(d.result); }
  else if (d.method) events.push(d); });
await send('Page.enable'); await send('Runtime.enable');
const t = {
  send,
  async ev(expr) { const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
    if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 600)); return r.result.value; },
  async size(w, h, mobile = false) { await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile }); },
  async nav(u, ms = 2500) { events.length = 0; await send('Page.navigate', { url: u });
    for (let i = 0; i < 400; i++) { if (events.find(e => e.method === 'Page.loadEventFired')) break; await sleep(50); } await sleep(ms); },
  async shot(file, clip) { const r = await send('Page.captureScreenshot', clip ? { format: 'png', clip: { ...clip, scale: 1 } } : { format: 'png' });
    fs.writeFileSync(file, Buffer.from(r.data, 'base64')); },
  async click(x, y) { for (const type of ['mouseMoved', 'mousePressed', 'mouseReleased'])
    await send('Input.dispatchMouseEvent', { type, x, y, button: 'left', clickCount: 1 }); },
  async key(k, code, kc) { await send('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code, windowsVirtualKeyCode: kc });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code, windowsVirtualKeyCode: kc }); },
  sleep,
};
const mod = await import(path.resolve(process.argv[2]));
try { await mod.default(t); } catch (e) { console.error('ERROR', e.message); process.exitCode = 1; }
ws.close(); proc.kill(); await sleep(400); try { fs.rmSync(udd, { recursive: true, force: true }); } catch (e) {}
