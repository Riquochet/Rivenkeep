"""decode_crops.py - the mini decode check's pictures: a whole round, titles and descs stripped, cut into zoom
crops at reading scale; v2 left, v3 right, the same viewBox. A manifest (from the renderer's own model) lists
what each crop holds, to check the reading against.
    python3 decode_crops.py NAME V2.svg V3.svg OUTDIR
"""
import sys, os, re, pickle, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
sys.setrecursionlimit(100000)
import render_grain3 as R
import shoot3

name, v2p, v3p, outdir = sys.argv[1:5]
os.makedirs(outdir, exist_ok=True)


def strip(svg):
    svg = re.sub(r'<title[^>]*>.*?</title>', '', svg, flags=re.S)
    svg = re.sub(r'<desc[^>]*>.*?</desc>', '', svg, flags=re.S)
    svg = re.sub(r' aria-labelledby="[^"]*"', '', svg)
    svg = re.sub(r' data-round="[^"]*"', '', svg)
    return svg


S2 = strip(open(v2p, encoding='utf-8').read())
S3 = strip(open(v3p, encoding='utf-8').read())
open(os.path.join(outdir, name + '_v3_stripped.svg'), 'w', encoding='utf-8').write(S3)
open(os.path.join(outdir, name + '_v2_stripped.svg'), 'w', encoding='utf-8').write(S2)
rd = pickle.load(open(os.path.join(HERE, name + '.pkl'), 'rb'))
rd.pw, rd.pwr = 1.0, 1.0
_pk = {k: v for k, v in rd.lines.items() if k.startswith('pk:')}
for k in _pk:
    del rd.lines[k]
rd.crossings()
rd.lines.update(_pk)


def crop_svg(s, x, y, w, h, px):
    return re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"', 'viewBox="%g %g %g %g" width="%d" height="%d"' % (x, y, w, h, px, int(px * h / w)), s, count=1)


def pair(tag, cx, cy, size, px=640, note=''):
    x, y = cx - size / 2.0, cy - size / 2.0
    a, b = crop_svg(S2, x, y, size, size, px), crop_svg(S3, x, y, size, size, px)
    body = ('<div style="display:flex;gap:8px;padding:6px"><div>%s<div style="color:#8a7f6a;font:12px Georgia">v2</div></div>'
            '<div>%s<div style="color:#8a7f6a;font:12px Georgia">v3</div></div></div>' % (a, b))
    out = os.path.join(outdir, '%s_%s.png' % (name, tag))
    open(out + '.html', 'w', encoding='utf-8').write(shoot3.page(body))
    shoot3.chrome(out + '.html', out, 2 * px + 30, px + 40)
    # manifest: marks, runner ends and crossings inside the box
    inside = lambda p: x <= p[0] <= x + size and y <= p[1] <= y + size
    ms = []
    for key, rec in rd.recs.items():
        if rec.get('kind') != 'mark':
            continue
        c = rec['field'].pt(0.5 * (rec['rin'] + rec['rout']), rec['th'])
        if inside(c):
            ms.append('%s %s' % (R.addr_text(key), rec['mk'].lig.text()))
    rs = []
    for rid, pts in rd.lines.items():
        info = rd.info.get(rid)
        if not info or info[0] is None:
            continue
        rn, end = info[0], info[1]
        if inside(pts[-1]):
            rs.append('%s ends (%s, %s)' % (rid, rn.role + ('~' if rn.seeming else '') + ('_' if rn.hidden else ''), end))
        if inside(pts[0]):
            rs.append('%s springs' % rid)
    xs = ['%s over %s (%s)' % (o, u, k) for o, u, k, p in rd.found if inside(p)]
    return {'crop': os.path.basename(out), 'box': [round(x), round(y), size], 'note': note, 'marks': ms, 'runners': rs, 'crossings': xs}


man = []
# 1) tiles over the whole round (content tiles only)
vb = [float(v) for v in re.search(r'viewBox="([^"]*)"', S3).group(1).split()]
T = float(sys.argv[5]) if len(sys.argv) > 5 else 420.0
x0, y0 = vb[0], vb[1]
nx, ny = int(math.ceil(vb[2] / T)), int(math.ceil(vb[3] / T))
for i in range(nx):
    for j in range(ny):
        cx, cy = x0 + (i + 0.5) * T, y0 + (j + 0.5) * T
        box = lambda p: abs(p[0] - cx) <= T / 2 and abs(p[1] - cy) <= T / 2
        n = sum(1 for rec in rd.recs.values() if rec.get('kind') == 'mark' and box(rec['field'].pt(rec['rin'], rec['th'])))
        n += sum(1 for pts in rd.lines.values() if any(box(p) for p in pts[::10]))
        if n:
            man.append(pair('t%d%d' % (i, j), cx, cy, T, note='tile'))
# 2) the devices
for o, u, k, p in rd.found:
    if k in ('break', 'braid-break', 'bind'):
        man.append(pair('x_%s_%s' % (o.replace(':', '-'), u.replace(':', '-')), p[0], p[1], 110, note='%s: %s over %s' % (k, o, u)))
for pid, pr in rd.pockets.items():
    c = R.lerp(pr['outline'][0], pr['outline'][len(pr['outline']) // 2], 0.5)
    tt = 0.5 * (pr['t0'] + pr['t1'])
    c = rd.main.pt(pr['mid'][len(pr['mid']) // 2][1], tt)
    span = (pr['t1'] - pr['t0']) * pr['mid'][len(pr['mid']) // 2][1]
    man.append(pair('p_%s' % pid, c[0], c[1], max(120, 1.15 * span), note='pocket %s (%s)' % (pid, pr['pk'].kind)))
json.dump(man, open(os.path.join(outdir, name + '_manifest.json'), 'w'), indent=1, ensure_ascii=False)
print(len(man), 'crops')
