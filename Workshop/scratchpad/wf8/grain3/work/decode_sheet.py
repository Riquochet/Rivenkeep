"""decode_sheet.py - targeted decode crops (titles and descs stripped), v2 | v3 pairs with the model's own label,
laid out as contact sheets to read: every runner role's terminal, every declared break, the braid, the bind,
pockets (mouth and middle), hollow/smoothed runners, file referents, blinds, fringe, year-lines, passes.
    python3 decode_sheet.py NAME V2.svg V3.svg OUTDIR
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
    return re.sub(r' data-round="[^"]*"', '', svg)


S2 = strip(open(v2p, encoding='utf-8').read())
S3 = strip(open(v3p, encoding='utf-8').read())
rd = pickle.load(open(os.path.join(HERE, name + '.pkl'), 'rb'))
rd.pw, rd.pwr = 1.0, 1.0
_pk = {k: v for k, v in rd.lines.items() if k.startswith('pk:')}
for k in _pk:
    del rd.lines[k]
rd.crossings()
rd.lines.update(_pk)
# ids must not clash when two copies of a round sit on one page: prefix v2's
pref2 = re.search(r'id="(g[0-9a-f]+)-', S2).group(1)
S2 = S2.replace(pref2, pref2 + 'v2')


def crop(s, x, y, w, px):
    return re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"', 'viewBox="%g %g %g %g" width="%d" height="%d"' % (x, y, w, w, px, px), s, count=1)


items = []
def add(tag, c, size, label):
    items.append((tag, c, size, label))

by_role = {}
for rid, pts in sorted(rd.lines.items()):
    info = rd.info.get(rid)
    if not info or info[0] is None or rid.startswith('pk:'):
        continue
    rn, end, tr, dirn, tg = info
    role = rn.role + (' hollow' if rn.seeming else '') + (' smoothed' if rn.hidden else '')
    tgt = tg[0] if tg else '?'
    if tgt == 'file':
        role += ' @file'
    if end in ('fork', 'bind', 'stub'):
        continue
    by_role.setdefault(role, []).append((rid, pts, tgt, end))
for role in sorted(by_role):
    lst = by_role[role]
    step = max(1, len(lst) // 3)
    for rid, pts, tgt, end in lst[::step][:3]:
        add('end_' + rid, pts[-1], 60, '%s: %s ends (%s, lands on %s)' % (rid, role, end, tgt))
for o, u, k, p in rd.found:
    if k != 'pass':
        add('x_%s_%s' % (o, u), p, 60, '%s: %s over %s' % (k, o, u))
passes = [f for f in rd.found if f[2] == 'pass']
for o, u, k, p in passes[::max(1, len(passes) // 6)][:6]:
    add('x_%s_%s' % (o, u), p, 60, 'pass: %s over %s (later in canonical order: %s)' % (o, u, o))
for pid, pr in rd.pockets.items():
    mids = pr['mid']
    th, m, hh = mids[len(mids) // 2]
    add('p_' + pid, rd.main.pt(m, th), 110, 'pocket %s (%s): middle' % (pid, pr['pk'].kind))
    add('pm_' + pid, pr['mouth'], 70, 'pocket %s (%s): mouth' % (pid, pr['pk'].kind))
nfr, nyr = 0, 0
for key, rec in sorted(rd.recs.items(), key=lambda kv: str(kv[0])):
    if rec.get('kind') != 'mark' or rec['mk'].root:
        continue
    lig = rec['mk'].lig
    txt = lig.text()
    c = rec['field'].pt(0.5 * (rec['rin'] + rec['rout']), rec['th'])
    if '{' in txt and nfr < 4:
        add('fr_%d' % nfr, c, 60, 'fringe: %s %s' % (R.addr_text(key), txt)); nfr += 1
    elif rec['y'] > 1 and nyr < 3 and '{' not in txt:
        add('yr_%d' % nyr, rec['field'].pt(rec['rin'] - 2.0, rec['th']), 60, 'year-line: %s %s (year %d)' % (R.addr_text(key), txt, rec['y'])); nyr += 1
root = next(r for r in rd.recs.values() if r.get('kind') == 'mark' and r['mk'].root)
add('root', root['field'].pt(0.5 * (root['rin'] + root['rout']), root['th']), 150, 'the heart: root %s' % root['mk'].lig.text())
man = []
PX = 300
per = 12
for si in range(0, len(items), per):
    cells = []
    for tag, c, size, label in items[si:si + per]:
        x, y = c[0] - size / 2.0, c[1] - size / 2.0
        cells.append('<div style="width:%dpx;padding:4px"><div style="display:flex;gap:4px">%s%s</div><div style="font:11px Georgia;color:#b8aa8a;height:28px">%s</div></div>'
                     % (2 * PX + 4, crop(S2, x, y, size, PX), crop(S3, x, y, size, PX), label))
        man.append({'sheet': si // per, 'tag': tag, 'label': label, 'box': [round(x, 1), round(y, 1), size]})
    body = '<div style="display:grid;grid-template-columns:repeat(2,%dpx);gap:6px">%s</div>' % (2 * PX + 12, ''.join(cells))
    out = os.path.join(outdir, '%s_decode_%d.png' % (name, si // per))
    open(out + '.html', 'w', encoding='utf-8').write(shoot3.page(body))
    rows = (len(cells) + 1) // 2
    shoot3.chrome(out + '.html', out, 2 * (2 * PX + 12) + 20, rows * (PX + 44) + 10)
    print(out)
json.dump(man, open(os.path.join(outdir, name + '_decode_manifest.json'), 'w'), indent=1, ensure_ascii=False)
print(len(items), 'crops')
