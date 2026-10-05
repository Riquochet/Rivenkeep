"""sheet_v2_v3.py - the before/after sheet of the grain renderers: wf7 render_grain2.py (v2) beside
wf8 render_grain3.py (v3 presentation). -> wf8/grain_v2_v3.png"""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
G3 = os.path.dirname(HERE)
WF8 = os.path.dirname(G3)
TMP = os.path.join(G3, 'sheet')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
V2, V3 = os.path.join(G3, 'v2out'), os.path.join(G3, 'svg')
os.makedirs(TMP, exist_ok=True)


def crop(src, dst, x, y, w, h=None):
    h = h or w
    s = open(src, encoding='utf-8').read()
    s = re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"', 'viewBox="%g %g %g %g" width="%d" height="%d"' % (x, y, w, h, w, h), s, count=1)
    p = os.path.join(TMP, dst)
    open(p, 'w', encoding='utf-8').write(s)
    return p


_n = [0]


def img(path, w, h=None):
    """inline the SVG (sharper than <img> at page size), its ids made unique on this page"""
    _n[0] += 1
    s = open(path, encoding='utf-8').read()
    for pref in set(re.findall(r'id="([gk][0-9a-f]{7})-', s)):
        s = s.replace(pref, '%sx%d' % (pref, _n[0]))
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', s)
    vw, vh = float(m.group(3)), float(m.group(4))
    W = w if vw >= vh else int(round((h or w) * vw / vh))
    H = int(round(W * vh / vw))
    s = re.sub(r'(<svg [^>]*?) width="\d+" height="\d+"', r'\1 width="%d" height="%d" style="display:block"' % (W, H), s, count=1)
    return s


def pair(title, a, b, w, note=''):
    return ('<div class="pair"><div class="t">%s</div><div class="row">'
            '<div><span class="v">v2</span>%s</div><div><span class="v">v3</span>%s</div></div>%s</div>'
            % (title, img(a, w), img(b, w), ('<div class="l">%s</div>' % note) if note else ''))


css = ('body{margin:0;background:#15120e;color:#cbbd9f;font:14px/1.38 Georgia,serif}'
       '.wrap{padding:24px 30px;width:1500px}h1{font-weight:normal;font-size:27px;margin:0 0 4px}'
       'h2{font-weight:normal;font-size:16px;letter-spacing:.12em;text-transform:uppercase;margin:24px 0 4px;color:#e0d2b2}'
       'p.s{margin:0 0 10px;color:#8f846d;font-style:italic;max-width:1480px}'
       '.row{display:flex;gap:14px;align-items:flex-start;flex-wrap:wrap}'
       '.pair{display:flex;flex-direction:column}.pair .t{font-size:13px;color:#cbbd9f;margin-bottom:3px}'
       '.pair .l{font-size:12px;color:#8f846d;margin-top:3px;max-width:760px}'
       '.v{font-size:11px;letter-spacing:.1em;color:#6f6552;display:block}'
       'table{border-collapse:collapse;font-size:13px;margin-top:6px}td,th{border-bottom:1px solid #2e2820;padding:3px 10px;text-align:left;vertical-align:top}'
       'th{color:#e0d2b2;font-weight:normal}td.ok{color:#b9c79a}')
h = ['<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><div class="wrap">' % css]
h.append('<h1>Eilseth, the grain &middot; v2 &rarr; v3 presentation</h1>')
h.append('<p class="s">Left: wf7 render_grain2.py (v2). Right: wf8 render_grain3.py (v3), the same Grain Notation, the same '
         'packing, routes and crossings (checked equal), only the cut changed. A whole round is cut at a page weight '
         'pw = R/400 (IV.6 2.34, IV.4 2.80): heavier runners in dark grooves, wider over/under gaps, a knot-eye round every '
         'mark, ring lines yielding further, a wake of grain along every runner, ring-splits where the carving disturbs a '
         'line, and a flecked figure; all by the Law of the Rings: nothing in the heart ring, little in band I, most outward. '
         'Shown at page size, 720 px wide.</p>')
h.append('<h2>IV.6 &middot; the Voyage of the Aelvaren, carved whole</h2><div class="row">')
h.append(pair('', os.path.join(V2, 'IV-6.svg'), os.path.join(V3, 'grain3_IV-6.svg'), 720))
h.append('</div><h2>IV.4 &middot; the Gift Held an Hour, carved whole</h2><div class="row">')
h.append(pair('', os.path.join(V2, 'IV-4.svg'), os.path.join(V3, 'grain3_IV-4.svg'), 720))
h.append('</div>')
h.append('<h2>At reading scale (the same crops)</h2><div class="row">')
d = []
d.append(('IV.4, rings 9&ndash;15, files 12&ndash;3: the busy sapwood', crop(os.path.join(V2, 'IV-4.svg'), 'a2.svg', 0, -1000, 700),
          crop(os.path.join(V3, 'grain3_IV-4.svg'), 'a3.svg', 0, -1000, 700), 360))
d.append(('IV.6 ring 7: the braid <i>abab!</i> (fire and grey, by turns, until the grey)', crop(os.path.join(V2, 'IV-6.svg'), 'b2.svg', -706, -58, 76),
          crop(os.path.join(V3, 'grain3_IV-6.svg'), 'b3.svg', -706, -58, 76), 360))
h.append(''.join(pair(t, a, b, s) for t, a, b, s in d))
h.append('</div><div class="row" style="margin-top:12px">')
d = []
d.append(('IV.6 ring 5: our turning <i>breaks</i> the current (e1 &#8883; f1)', crop(os.path.join(V2, 'IV-6.svg'), 'c2.svg', -100, 455, 60),
          crop(os.path.join(V3, 'grain3_IV-6.svg'), 'c3.svg', -100, 455, 60), 360))
d.append(('IV.4: the bind K1 (i6 and i7 hooked through each other) and its out-runner', crop(os.path.join(V2, 'IV-4.svg'), 'd2.svg', 572, -476, 50),
          crop(os.path.join(V3, 'grain3_IV-4.svg'), 'd3.svg', 572, -476, 50), 360))
h.append(''.join(pair(t, a, b, s) for t, a, b, s in d))
h.append('</div>')
h.append('<h2>What does not change</h2><p class="s">The heart stays a plain anchor (the heart ring takes no figure, wake, knot-eye or ring-split, and a runner '
         'there keeps v2\'s knife; only the dark margin round each cut is wider); young and small carvings, the ring plates and the chips render byte-identical to v2.</p><div class="row">')
h.append(pair('IV.6: the heart ring (the root HOLD)', crop(os.path.join(V2, 'IV-6.svg'), 'e2.svg', -110, -165, 220),
              crop(os.path.join(V3, 'grain3_IV-6.svg'), 'e3.svg', -110, -165, 220), 250))
for n, t in (('E1-01', 'E1-01 (green)'), ('BURN', '<i>Burn</i>'), ('E4-01', 'E4-01 (pw 1)'), ('NAELEAR', '<i>Naelear</i>')):
    h.append('<div class="pair"><div class="t">%s</div>%s<div class="l">v2 = v3, byte for byte</div></div>'
             % (t, img(os.path.join(V3, 'grain3_%s.svg' % n), 190)))
h.append('</div>')
h.append(open(os.path.join(TMP, 'decode_table.html'), encoding='utf-8').read() if os.path.exists(os.path.join(TMP, 'decode_table.html')) else '')
h.append('</div></body></html>')
html = os.path.join(TMP, 'grain_v2_v3.html')
open(html, 'w', encoding='utf-8').write(''.join(h))
png = os.path.join(WF8, 'grain_v2_v3.png')
H = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--screenshot=' + png,
                '--window-size=1560,%d' % H, 'file://' + html], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
print(png)
