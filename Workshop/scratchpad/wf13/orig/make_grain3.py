#!/usr/bin/env python3
"""make_grain3.py -- the grain drawings of the Original (wf8 scratch, set up for wf12, the Book v3.0.0; never goes into Docs/).

wf12: the rounds are read from wf12/units (W01 II.2, W02 IV.2, W03 IV.4 and its sentence IV-4-gift, W04 IV.6, W05 V.3,
W06 V.4 and its carving V-4-grow, W07 V.6, W08 VI.2's ten hearts; the stone leaves' rounds from S07, S08, S09, S10 and
S11); the renderer is wf8/render_grain3.py, imported read only.

Every round is cut by the NEW renderer, wf8/render_grain3.py (Renderer notes v3: a whole round at page weight;
plates, chips and young wood exactly as v2).  The texts are the merged, validated units' own canonical GN
(wf8/units/*.md, their '## 4' blocks and their inline round blocks), the IV.4 pilot's (wf8/grain3/texts/IV-4.gn2,
= wf7/pilot_IV4/IV-4.canon.gn2), and wf6's AELTHAR (the rite, cited in IV.4).  '# file' legends are dropped (the
renderer reads only '# key: value' front matter); a '# name:' line gives each round its accessible title.

    python3 make_grain3.py [--list] [KEY ...]        -> wf12/orig/svg3/<KEY>.svg, in parallel, cached by text
"""
import hashlib, json, os, re, sys, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
W8 = os.path.dirname(HERE)          # wf12: this folder's parent (the units are wf12's)
S = os.path.dirname(W8)
RENDER = os.path.join(S, 'wf8')     # the renderer stays wf8's, read only
sys.path.insert(0, RENDER)
import render_grain3 as R  # noqa: E402

# ---- two readings of the spec the renderer's parser does not yet take (render-time only; the renderer file is not
# edited, and nothing it draws otherwise changes):
#  * grain_v2 §6.3.2 / A4: a runner to `@f.rK/Y` ends in file f's free cell in ring K, year Y (III.2's c3 and g12);
#    the renderer's `@f` always used the source's own year.
_parse_target = R.parse_target


def _parse_target_year(t):
    m = re.match(r'^@(\d+)\.r(\d+)(?:/(\d+))?$', t.strip())
    if m:
        return ('file', int(m.group(1)), int(m.group(2)), int(m.group(3) or 1))
    return _parse_target(t)


R.parse_target = _parse_target_year
#  * a float raised to a fractional power where the base is -1e-16 comes back complex (imaginary part ~1e-13) and
#    stops the writer (V.6 whole); such a value is its real part.
_q_orig = R._q


def _q_real(v):
    if isinstance(v, complex):
        if abs(v.imag) > 1e-6:
            raise ValueError('a complex coordinate %r' % v)
        v = v.real
    return _q_orig(v)


R._q = _q_real
#  * mystaeri_spec §3.14: the grain itself (vael) is written in names as a free GRAIN-ARC, "a short hairline along
#    the ring, the same line the rings are drawn with" (III.2's Vaelress and Rhenvael in the bark, V.6's Heartwood
#    and Second Tide in pockets, the Knowings' T-02 and T-06); the validator reads it as GRAIN, the renderer's sign
#    table had no drawing for it. It is drawn here as the spec says: one ring-arc, cut at a hairline's weight.
R.SIGNS.setdefault('GRAIN', {"cls": "thing", "soft": "vael", "gloss": "the grain (the grain-arc: in names only)",
                             "els": [{"t": "ringarc", "u": 0.5, "v0": -0.78, "v1": 0.78, "k": 0.45}]})
_target_geo = R.RunnerMixin.target_geo


def _target_geo_year(self, rn, tg, src, dirn):
    if tg[0] == 'file' and len(tg) == 4:
        k, y = tg[2], tg[3]
        if (k, y) in self.lay.year_r and k == src['k']:
            src = dict(src, y=y)
        return _target_geo(self, rn, ('file', tg[1]), src, dirn)
    return _target_geo(self, rn, tg, src, dirn)


R.RunnerMixin.target_geo = _target_geo_year
R.Renderer.target_geo = _target_geo_year

GN = os.path.join(HERE, 'gn')
OUT = os.path.join(HERE, 'svg3')


def unit_blocks(u):
    t = open(os.path.join(W8, 'units', '%s.md' % u), encoding='utf-8').read()
    return [b for b in re.findall(r'```[a-z0-9]*\n(.*?)```', t, re.S) if re.match(r'(?:#[^\n]*\n)*round ', b)]


PK_SPLIT = re.compile(r'^(\s*run\s+)(\S+)(\s+P\w*\.\d+\s+\S+\s+)\{([^}]*)\}\s*$')


def pocket_split(ln):
    """a split runner among a pocket's items (IV.2 ring 13: run m5 P5.1 →in {P5.2, P5.3}), which the renderer's
    pocket runners take one target at a time, is drawn as its shoots, each from the one item (render text only)"""
    m = PK_SPLIT.match(ln)
    if not m:
        return [ln]
    tg = [t.strip() for t in m.group(4).split(',')]
    return ['%s%s%s%s' % (m.group(1), m.group(2) + ('' if i == 0 else chr(ord('a') + i)), m.group(3), t) for i, t in enumerate(tg)]


FORK_RE = re.compile(r'(?<![\w.·])((?:p\d+·)?\d+(?:\.\d)?):\s*([^\s<]+?)<(\S*?)\|(\S*?)>(?=\s|$)')


def forks(lines):
    """grain_v2 §13.7 / mystaeri_spec §3.12: the FORK `A<X|Y>`, "a cut splitting in two at its head; the clockwise
    branch (the if) leads on to the next file clockwise, the other counter-clockwise", its branches ending in their
    signs (a CHAIN's older root half size, `X½`). The renderer does not draw forks yet (grain_v2 §17: "Not yet
    drawn: fork and chain"), so for the drawing only the fork is written with the devices that draw it: A stays;
    X and Y are cut in a new growth of the same ring, on the files either side; one split runner (a cut that forks
    once, §6.1) runs from A's head to them. An empty branch (`…`) is a shoot to that file's empty cell."""
    out = list(lines)
    extra_years, runs = [], []
    n = 0
    for i, ln in enumerate(out):
        m0 = re.match(r'^(\s*)r(\d+)(?:/(\d+))?(\s+)(.*)$', ln)
        if not m0 or '<' not in ln:
            continue
        k = int(m0.group(2))
        y = int(m0.group(3) or 1)
        body = m0.group(5)
        found = list(FORK_RE.finditer(body))
        if not found:
            continue
        for fm in found:
            addr, a, x, yb = fm.group(1), fm.group(2), fm.group(3).strip(), fm.group(4).strip()
            pith = re.match(r'^(p\d+·)', addr)
            f = int(re.sub(r'^p\d+·', '', addr).split('.')[0])
            n += 1
            extra_years.append((k, addr, a, x, yb, f, pith.group(1) if pith else '', y, n))
        body = FORK_RE.sub(lambda fm: '%s: %s' % (fm.group(1), fm.group(2)), body)
        out[i] = '%sr%d/%d%s%s' % (m0.group(1), k, y, m0.group(4), body)
    if not extra_years:
        return out
    # the new growths: after the last year of ring k
    for (k, addr, a, x, yb, f, pp, y, j) in extra_years:
        years = [int(re.match(r'^\s*r\d+/(\d+)', l).group(1)) for l in out
                 if re.match(r'^\s*r%d/(\d+)\b' % k, l)]
        ny = max(years) + 1
        last = max(q for q, l in enumerate(out) if re.match(r'^\s*r%d/\d+\b' % k, l))
        fc, fa = (f + 1) % 16, (f - 1) % 16
        items = []
        tg = []
        for fil, sign in ((fc, x), (fa, yb)):
            if sign and sign != '…':
                items.append('%s%d: %s' % (pp, fil, sign))
                tg.append('%s%d.r%d/%d' % (pp, fil, k, ny))
            else:
                tg.append('@%d.r%d/%d' % (fil, k, ny))
        if not items:
            continue
        out.insert(last + 1, '    r%d/%d  %s' % (k, ny, '    '.join(items)))
        runs.append('    run fk%d  %s.r%d/%d  →  {%s}' % (j, addr, k, y, ', '.join(tg)))
    if not any(l.strip() == 'runners' for l in out):
        out.append('  runners')
    out += runs
    return out


def clean(block, name):
    keep = [ln for ln in block.split('\n') if ln.strip() and not ln.lstrip().startswith('#')]
    keep = [re.sub(r'^(\s*r\d+(?:/\d+)?\s+·)\s*\(.*\)\s*$', r'\1', ln) for ln in keep]   # a ring left untold, with its note
    keep = [x for ln in keep for x in pocket_split(ln)]
    keep = forks(keep)
    # mystaeri_spec §5.1's sliver (VI.1) folds NAELEAR, the name-sign, into HOME; the renderer's sign table writes
    # that name-sign as what it is drawn with, US×3 (as its own text of the same sample, grain3/texts/VI-1.gn2)
    keep = [ln.replace('[NAELEAR within', '[US×3 within') for ln in keep]
    return '\n'.join(['# name: %s' % name] + keep) + '\n'


HEARTS = ['thaesaen', 'leavaren', 'vaelress', 'ralensaen', 'rhenvael', 'esthaer', 'senneir', 'eirlenth', 'naelthar', 'neivaere']
HEART_NAMES = {'thaesaen': 'Thaesaen', 'leavaren': 'Leavaren', 'vaelress': 'Vaelress', 'ralensaen': 'Ralensaen',
               'rhenvael': 'Rhenvael', 'esthaer': 'Esthaer', 'senneir': 'Senneir', 'eirlenth': 'Eirlenth',
               'naelthar': 'Naelthar', 'neivaere': 'Neivaere'}
WOOD = {  # key: (unit, block index, title)   (wf12: the Book v3.0.0's wood units)
    'II-2': ('W01', -1, 'II.2, Of the Breath of the Wood, carved whole in the grain'),
    'IV-2': ('W02', -1, 'IV.2, The Axe in the Grain, carved whole in the grain'),
    'IV-4': ('W03', -1, 'IV.4, The Gift Held an Hour, carved whole in the grain'),
    'IV-6': ('W04', -1, 'IV.6, The Voyage of the Aelvaren, carved whole in the grain'),
    'V-3': ('W05', -1, 'V.3, The Wreck That Went Home, carved whole in the grain'),
    'V-4': ('W06', -1, 'V.4, The Council Under the Thin Sky, carved whole in the grain'),
    'V-6': ('W07', -1, 'V.6, Of the Growing, carved whole in the grain'),
}
CITED = {  # the rounds a wood leaf cites whole (A27): key: (unit, block index, title)
    'GIFT': ('W03', 0, 'IV.4, the Guest\'s sentence (the gift\'s own round, mystaeri_spec §5.4)'),
    'V-4-grow': ('W06', 0, 'V.4, the first carving of the war (mystaeri_spec §5.8)'),
}


def write_texts():
    """the render texts, from the units (idempotent); returns {key: path}"""
    os.makedirs(GN, exist_ok=True)
    out = {}

    def put(key, text):
        p = os.path.join(GN, key + '.gn2')
        if not os.path.exists(p) or open(p, encoding='utf-8').read() != text:
            open(p, 'w', encoding='utf-8').write(text)
        out[key] = p
    for key, (u, i, title) in WOOD.items():
        put(key, clean(unit_blocks(u)[i], title))
    for key, (u, i, title) in CITED.items():
        put(key, clean(unit_blocks(u)[i], title))
    for j, b in enumerate(unit_blocks('W08')):
        rid = re.match(r'(?:#[^\n]*\n)*round (\S+)', b).group(1)
        h = rid.replace('VI-2-', '')
        put(rid, clean(b, 'VI.2, the heart of %s, carved whole in the grain' % HEART_NAMES.get(h, h)))
    # the stone leaves' carvings, and the Book of Knowings: every round block, keyed by unit and round id
    for u in ('S07', 'S08', 'S09', 'S10', 'S11'):
        seen = {}
        for b in unit_blocks(u):
            rid = re.match(r'(?:#[^\n]*\n)*round (\S+)', b).group(1)
            seen[rid] = seen.get(rid, 0) + 1
            key = '%s_%s' % (u, rid) + ('' if seen[rid] == 1 else '_%d' % seen[rid])
            name = re.search(r'^#\s*name\s*:\s*(.+)$', b, re.M)
            put(key, clean(b, name.group(1).strip() if name else rid))
    return out


def jobs_for(texts):
    J = []
    for key in list(WOOD) + ['VI-2-' + h for h in HEARTS]:
        md = R.parse_gn(open(texts[key], encoding='utf-8').read())
        J.append((key, texts[key], 'whole', None))
        for k in range(1, md.K + 1):
            J.append(('%s_r%02d' % (key, k), texts[key], 'plate', k))
    for key, p in texts.items():
        if key[:3] in ('S07', 'S08', 'S09', 'S10', 'S11') or key in CITED:
            J.append((key, p, 'whole', None))
    # I.1's facing leaf: the Stone's own rings, bare (stage 0), from the Epilogue's Stone (S10)
    J.append(('STONE_bare', texts['S10_STONE'], 'stage0', None))
    # IV.4's cited rite (AELTHAR, wf6): v1.3 cited it in ring 8; v3's IV.4 does not (W03 note 13: the rite is told as it
    # happened, its rings 8-9 gone), and its source wf6/grain_texts/AELTHAR.json was lost to the temp cleaner, so it is
    # drawn only if that source returns (wf12 panes). Its sentence (GIFT) is W03's own block, above.
    _ael = os.path.join(S, 'wf6', 'grain_texts', 'AELTHAR.json')
    if os.path.exists(_ael):
        J.append(('AELTHAR', _ael, 'whole', None))
    # V.7 Part II: the line the carving was cut against is E5-02's ring 4, set inline (S09 prints it as a plate)
    J.append(('S09_E5-02_r04', texts['S09_E5-02'], 'plate', 4))
    # IV.2's two drawn marks (v3: W02 §1.4, the Book's legend_iv2_gap1 and legend_iv2_gap2), each as the renderer's
    # strip chip (a mark set in a line of text, as the Book sets its two untold marks)
    for i, (lig, cond, mem, title) in enumerate(IV2_FRAGMENTS, 1):
        J.append(('IV-2_frag%d' % i, None, 'chip', dict(lig=lig, cond=cond, mem=mem, title=title)))
    return J


IV2_FRAGMENTS = [   # wf12, the Book v3.0.0: the reading's two drawn marks (W02 §1.4)
    ('DEEP+PILLAR×3{all}', None, True, 'the pillars, many, with a memory cut through them to the heart: the first drawn mark'),
    ('!MOUTH', None, False, 'the mouth, mirrored, and tied back across the rings to the plea cut on the stone: the second drawn mark'),
]


def digest(path, mode, arg):
    h = hashlib.sha1(open(path, 'rb').read())
    h.update(('%s|%s' % (mode, arg)).encode())
    h.update(open(os.path.join(RENDER, 'render_grain3.py'), 'rb').read())
    return h.hexdigest()[:16]


def job(spec):
    key, path, mode, arg = spec
    out = os.path.join(OUT, key + '.svg')
    if mode == 'chip':
        svg = R.render_chip(arg['lig'], 'chip/IV-2/' + key, arg['title'], cond=arg['cond'], strip=True, mem=arg['mem'])
        open(out, 'w', encoding='utf-8').write(svg)
        return key, len(svg.encode()) / 1024.0, 0.0, ['chip']
    dg = digest(path, mode, arg)
    stamp = out + '.digest'
    if os.path.exists(out) and os.path.exists(stamp) and open(stamp).read() == dg:
        return key, os.path.getsize(out) / 1024.0, 0.0, ['cached']
    t0 = time.time()
    raw = open(path, encoding='utf-8').read()
    chip = re.search(r'^round\s+(\S+)\s*\{[^}]*kind:\s*chip[^}]*\}', raw, re.M)
    if chip:
        # a chip (grain_v2 A10: plain wood, no pith, no ring of its own): the renderer's own chip, one ligature
        lig = re.search(r'^\s*r1(?:/1)?\s+\d+\s*:\s*(.+?)\s*$', raw, re.M).group(1)
        name = re.search(r'^#\s*name\s*:\s*(.+)$', raw, re.M)
        svg = R.render_chip(lig, 'chip/' + chip.group(1), name.group(1) if name else chip.group(1))
        open(out, 'w', encoding='utf-8').write(svg)
        open(stamp, 'w').write(dg)
        return key, len(svg.encode()) / 1024.0, time.time() - t0, ['chip']
    try:
        md = R.load_text(path)
        rd = R.Renderer(md, stage0=(mode == 'stage0'), plate=(arg if mode == 'plate' else None))
        svg = rd.render()
    except Exception as e:  # noqa: BLE001
        return key, 0.0, time.time() - t0, ['FAILED: %r' % e]
    open(out, 'w', encoding='utf-8').write(svg)
    open(stamp, 'w').write(dg)
    warn = [w for w in rd.warnings if 'under 15 degrees' not in w and 'strands are missing' not in w]
    return key, len(svg.encode()) / 1024.0, time.time() - t0, warn


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    texts = write_texts()
    J = jobs_for(texts)
    only = [a for a in sys.argv[1:] if not a.startswith('-')]
    if '--list' in sys.argv:
        for j in J:
            print(j[0], j[2], j[3])
        sys.exit(0)
    if only:
        J = [j for j in J if any(j[0] == o or re.fullmatch(o, j[0]) for o in only)]
    # the big whole rounds first
    J.sort(key=lambda j: (0 if j[2] == 'whole' and '_' not in j[0] else 1))
    log = []
    with Pool(12) as p:
        for key, kb, dt, warn in p.imap_unordered(job, J):
            line = '%-26s %7.1f KB  %6.1fs  %s' % (key, kb, dt, ('; '.join(warn))[:240])
            print(line, flush=True)
            log.append(line)
    open(os.path.join(HERE, 'make_grain3.log'), 'w').write('\n'.join(sorted(log)) + '\n')
