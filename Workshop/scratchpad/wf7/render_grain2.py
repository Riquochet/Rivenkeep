#!/usr/bin/env python3
"""render_grain2.py - the Eilseth v2 renderer for Rivenkeep (the grain, version 2). Python 3 standard
library only. Scratchpad tool: it never goes into Docs/.

Grain Notation v2 in (wf7/grain_v2.md section 13), compact deterministic SVG out:

  * the round as wf6's v1 renderer drew it (pith, heart ring, growth rings with latewood, band-rules,
    included bark, conditions, rays and memory rays, bark with its plates, the seal and names), now cut
    in YEARS and CELLS (v2 4), with the grain yielding round every mark and every runner (v2 4.6);
  * every sign defined ONCE as a <symbol> and placed with <use> (v2 11.6). A cut's two facets are
    bucketed by the way they face (eight buckets of 45 degrees), and each placement sets eight CSS
    custom properties that give every bucket its tone under the one light (top-left), so a symbol
    turned to any file is still lit truly, and the same symbol, unlit, knocks the wood out in the mask;
  * RUNNERS (v2 6): narrow living V-cuts grown by a grain-following A* router on a ring-aligned
    lattice (its rows follow each ring's own shape), string-pulled and smoothed in (theta, ring), with
    a seeded slow drift across the grain and the spec's meander, a bud at the node and the role's
    terminal at the end; PASSES and BREAKS (7.1: a declared break crosses square, exactly once),
    BRAIDS (7.2), BINDS (7.3), POCKETS (8), the FRINGE, PARTS and the KIND-ARC (5); split runners;
    ring PLATES with stubs and Seren's margin tags (11.5); CHIPS for the Book's inline drawings;
  * paint in currentColor under class "wood-ink"; an accessible <title> and <desc>; seeded,
    repeatable irregularity (mulberry32 over FNV-1a of the round's id, in named sub-streams).

  * (2026-09-28, for the Original's IV.4) grain_v2 21 A1 and A2: a band on a pocket item, X[STILL], and a band
    alone, [MIST], drawn in the item's own slot; runners among a pocket's items, P3.1 -> P3.2, cut with the
    pocket's finer knife and never leaving it. A ring plate's inner ring lines are now scaled under the plate,
    so the router finds the plate's ring (before, a plate's runners ran off it). Whole rounds are unchanged
    (the Book's thirteen rounds render byte-identical).

    python3 render_grain2.py TEXT [-o OUT.svg] [--state whole|fragments|locked] [--plate K] [--facets]
    python3 render_grain2.py TEXT --gn              # print its canonical Grain Notation v2
    python3 render_grain2.py --all                  # the Book's rounds -> wf7/svg/grain2_*.svg
    python3 render_grain2.py --check                # round trip, validator and determinism

TEXT is Grain Notation v2 (*.gn2: section 13's grammar, with '# key: value' front matter for the
title and desc), or a grain text in JSON (v1 wf6/grain_texts/*.json, read as v2 by section 13.7; or v2
with knowings, packed into years and cells by section 4.3).
"""
import argparse
import heapq
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.dirname(HERE)
SIGNS_V1 = os.path.join(SCRATCH, 'wf6', 'grain', 'signs.json')
SIGNS_V2 = os.path.join(HERE, 'grain2', 'signs_new.json')
TEXTS_DIR = os.path.join(HERE, 'grain2_texts')
OUT_DIR = os.path.join(HERE, 'svg')

SLOT = math.radians(22.5)
LIGHT = (-math.sqrt(0.5), -math.sqrt(0.5))     # toward the light: top-left (v1 3.11)
PITH_R = 4.5
ROOTFOOT = ((-64, 0.40, -16), (-10, 0.30, -6), (38, 0.36, 14))   # v1 10.6 (the originality pass)
MEMORY_TINES = ((-38, 6.5), (-4, 5.0), (26, 5.8))
INK_FALLBACK = '#dcc9a2'

# one ink, opacity tiers (v1 10.3), with v2's additions
OP = {
    'disc': .075, 'barkband': .085, 'heart': .045, 'stipple': .30,
    'late': .34, 'rule': .50, 'inc': .48, 'incband': .09,
    'fiss': .20, 'cambium': .45, 'plate': .30, 'pith': .62, 'hair': .62,
    'lit': .97, 'mid': .74, 'shade': .48, 'flat': .82,
    'rim': .78, 'edge': .78, 'smooth_lit': .62, 'smooth_shade': .30,
    'char': .50, 'mist': .12, 'frost': .48, 'water': .60, 'still': .55, 'dark': .07,
    'year': .22,                                   # v2 4.2: a year-line, 20-24%
    'pocket_said': .62, 'pocket_said_in': .34, 'pocket_cut': .55,
}
# runners: v2 19.2 (a) is recommended: cut them in the mid tone, so the marks stay the brightest thing
RUN_TONE = {'mid': {'lit': .74, 'mid': .60, 'shade': .42}, 'lit': {'lit': .97, 'mid': .74, 'shade': .48}}

H_MARK = 0.16
H_ROOT = 0.17
YEAR = 32.0
H_RUN = 1.35          # a runner's half-width at its node (v2 6.1); 0.45 at its terminal
BUD = 1.9             # the swelling where it springs
GAP_EXTRA = 1.5       # an under-strand's gap: the over-strand's half-width + this, each side
CLEAR = 3.2           # a runner keeps this far from every mark but its own two
RUN_CLEAR = 2.6
GRAIN = 1.7
CELLSTEP = 1.6


# ------------------------------------------------------------------------------------------ PRNG
def fnv1a(s):
    h = 0x811c9dc5
    for ch in s.encode('utf-8'):
        h ^= ch
        h = (h * 0x01000193) & 0xffffffff
    return h


class Rng:
    """mulberry32 over FNV-1a (v1 3.2). One stream per named purpose."""
    def __init__(self, seed):
        self.a = fnv1a(seed)

    def next(self):
        self.a = (self.a + 0x6D2B79F5) & 0xffffffff
        t = self.a
        t = ((t ^ (t >> 15)) * (t | 1)) & 0xffffffff
        t ^= (t + (((t ^ (t >> 7)) * (t | 61)) & 0xffffffff)) & 0xffffffff
        return ((t ^ (t >> 14)) & 0xffffffff) / 4294967296.0

    def uni(self, a, b):
        return a + (b - a) * self.next()


# -------------------------------------------------------------------------------------- vectors
def er(th):
    return (math.sin(th), -math.cos(th))


def et(th):
    return (math.cos(th), math.sin(th))


def add(a, b, k=1.0):
    return (a[0] + k * b[0], a[1] + k * b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def unit(a):
    l = math.hypot(a[0], a[1]) or 1e-9
    return (a[0] / l, a[1] / l)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def rot(v, ang):
    c, s = math.cos(ang), math.sin(ang)
    return (v[0] * c - v[1] * s, v[0] * s + v[1] * c)


def wrap(a):
    return math.atan2(math.sin(a), math.cos(a))


def polar_of(p, O=(0.0, 0.0)):
    """(theta, rho) of a point about O: theta clockwise from up (v1 3.4)."""
    dx, dy = p[0] - O[0], p[1] - O[1]
    return math.atan2(dx, -dy), math.hypot(dx, dy)


def arclen(pts):
    s = [0.0]
    for i in range(1, len(pts)):
        s.append(s[-1] + math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]))
    return s


def seg_dist(p, a, b):
    ab = sub(b, a)
    l2 = ab[0] * ab[0] + ab[1] * ab[1]
    t = 0.0 if l2 < 1e-12 else max(0.0, min(1.0, ((p[0] - a[0]) * ab[0] + (p[1] - a[1]) * ab[1]) / l2))
    q = add(a, ab, t)
    return math.hypot(p[0] - q[0], p[1] - q[1])


def poly_dist(p, polys):
    best = 1e9
    for pts, closed in polys:
        n = len(pts)
        if n == 1:
            best = min(best, math.hypot(p[0] - pts[0][0], p[1] - pts[0][1]))
        for i in range(n - (0 if closed else 1)):
            best = min(best, seg_dist(p, pts[i], pts[(i + 1) % n]))
    return best


def resample(pts, step):
    """Even arc-length resampling that keeps every corner sharper than 20 deg."""
    if len(pts) < 3:
        return pts
    keep = [0]
    for i in range(1, len(pts) - 1):
        a, b = sub(pts[i], pts[i - 1]), sub(pts[i + 1], pts[i])
        la, lb = math.hypot(*a), math.hypot(*b)
        if la > 1e-9 and lb > 1e-9 and dot(a, b) / (la * lb) < math.cos(math.radians(20)):
            keep.append(i)
    keep.append(len(pts) - 1)
    out = [pts[0]]
    for q in range(len(keep) - 1):
        seg = pts[keep[q]:keep[q + 1] + 1]
        s = arclen(seg)
        tot = s[-1]
        n = max(2, int(math.ceil(tot / step)))
        j = 0
        for i in range(1, n + 1):
            d = tot * i / n
            while j < len(seg) - 2 and s[j + 1] < d:
                j += 1
            span = (s[j + 1] - s[j]) or 1e-9
            out.append(lerp(seg[j], seg[j + 1], (d - s[j]) / span))
    return out


def resample_even(pts, step):
    if len(pts) < 2:
        return pts
    s = arclen(pts)
    tot = s[-1]
    n = max(2, int(math.ceil(tot / step)))
    out, j = [], 0
    for i in range(n + 1):
        d = tot * i / n
        while j < len(pts) - 2 and s[j + 1] < d:
            j += 1
        span = (s[j + 1] - s[j]) or 1e-9
        out.append(lerp(pts[j], pts[j + 1], min(1.0, (d - s[j]) / span)))
    return out


def dedupe(pts, eps=0.05):
    out = [pts[0]]
    for p in pts[1:]:
        if math.hypot(p[0] - out[-1][0], p[1] - out[-1][1]) > eps:
            out.append(p)
    return out


def chaikin(pts, n=1):
    for _ in range(n):
        if len(pts) < 3:
            return pts
        out = [pts[0]]
        for i in range(len(pts) - 1):
            a, b = pts[i], pts[i + 1]
            out.append(lerp(a, b, 0.25))
            out.append(lerp(a, b, 0.75))
        out.append(pts[-1])
        pts = out
    return pts


def edges_of(pts, hw):
    L, R = [], []
    n = len(pts)
    for i in range(n):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, n - 1)]
        d = unit(sub(b, a))
        nn = (-d[1], d[0])
        L.append(add(pts[i], nn, hw[i]))
        R.append(add(pts[i], nn, -hw[i]))
    return L, R


def offset_line(run, d):
    out = []
    n = len(run)
    for i in range(n):
        a, b = run[max(i - 1, 0)], run[min(i + 1, n - 1)]
        dd = unit(sub(b, a))
        out.append(add(run[i], (-dd[1], dd[0]), d))
    return out


# ------------------------------------------------------------------------------ path encoding
PREC = [10]          # 10 = tenths (cuts); 1 = whole units (the wood's long curves)


def _q(v):
    return int(round(v * PREC[0]))


def _num(t):
    p = PREC[0]
    if p == 1:
        return str(t)
    if t == 0:
        return '0'
    neg = t < 0
    t = abs(t)
    if p == 10:
        s = str(t // 10) if t % 10 == 0 else ('%d.%d' % (t // 10, t % 10))
    else:
        s = ('%.3f' % (t / float(p))).rstrip('0').rstrip('.')
    if s.startswith('0.'):
        s = s[1:]
    return ('-' + s) if neg else s


def _nums(vals):
    """Numbers joined as SVG allows: a space unless the next one starts with '-'."""
    out = ''
    for v in vals:
        s = _num(v)
        out += s if (not out or s[0] == '-') else ' ' + s
    return out


class prec:
    def __init__(self, p):
        self.p = p

    def __enter__(self):
        PREC.insert(0, self.p)

    def __exit__(self, *a):
        PREC.pop(0)


def poly_d(pts, closed=True):
    if len(pts) < 2:
        return ''
    q = [(_q(x), _q(y)) for x, y in pts]
    d = 'M' + _nums(q[0])
    rel = []
    for i in range(1, len(q)):
        rel += [q[i][0] - q[i - 1][0], q[i][1] - q[i - 1][1]]
    d += 'l' + _nums(rel)
    return d + ('z' if closed else '')


def smooth_d(pts, closed=True):
    """Catmull-Rom through pts as cubic Beziers (c then s), relative, exact at the precision."""
    n = len(pts)
    if n < 3:
        return poly_d(pts, closed)
    P = pts
    idx = (lambda i: P[i % n]) if closed else (lambda i: P[min(max(i, 0), n - 1)])

    def c_out(i):
        a, b, c = idx(i - 1), idx(i), idx(i + 1)
        return (b[0] + (c[0] - a[0]) / 6, b[1] + (c[1] - a[1]) / 6)

    def c_in(i):
        a, b, c = idx(i - 1), idx(i), idx(i + 1)
        return (b[0] - (c[0] - a[0]) / 6, b[1] - (c[1] - a[1]) / 6)

    Q = lambda p: (_q(p[0]), _q(p[1]))
    cur = Q(idx(0))
    d = 'M' + _nums(cur)
    last = n if closed else n - 1
    for i in range(1, last + 1):
        c2, p = Q(c_in(i)), Q(idx(i))
        if i == 1:
            c1 = Q(c_out(0))
            d += 'c' + _nums([c1[0] - cur[0], c1[1] - cur[1], c2[0] - cur[0], c2[1] - cur[1], p[0] - cur[0], p[1] - cur[1]])
        else:
            d += 's' + _nums([c2[0] - cur[0], c2[1] - cur[1], p[0] - cur[0], p[1] - cur[1]])
        cur = p
    return d + ('z' if closed else '')


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def simplify(poly, tol=0.12):
    if len(poly) < 5:
        return poly
    p0 = poly[0]
    f = max(range(len(poly)), key=lambda i: (poly[i][0] - p0[0]) ** 2 + (poly[i][1] - p0[1]) ** 2)
    if f == 0:
        return poly
    a = _dp(poly[:f + 1], tol)
    b = _dp(poly[f:] + [p0], tol)
    return a + b[1:-1]


def _dp(pts, tol):
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        pa, pb = pts[a], pts[b]
        dx, dy = pb[0] - pa[0], pb[1] - pa[1]
        ln = math.hypot(dx, dy) or 1e-9
        best, bi = -1.0, -1
        for i in range(a + 1, b):
            d = abs((pts[i][0] - pa[0]) * dy - (pts[i][1] - pa[1]) * dx) / ln
            if d > best:
                best, bi = d, i
        if best > tol:
            keep[bi] = True
            stack.append((a, bi))
            stack.append((bi, b))
    return [p for p, k in zip(pts, keep) if k]


def quant(b):
    return 'lit' if b > 0.26 else ('shade' if b < -0.26 else 'mid')


# ----------------------------------------------------------------------------------- the signs
def load_signs():
    out = {}
    for path in (SIGNS_V1, SIGNS_V2):
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        for k, v in d.items():
            if not k.startswith('_'):
                out[k] = v
    return out


SIGNS = load_signs()
# v2 5.2: which elements of a sign are cut whole for each part; the rest are cut hollow
PARTS = {
    'US': {'foot': [0], 'stem': [1], 'crown': [2]},
    'STONEFOLK': {'foot': [0], 'stem': [1], 'crown': [2]},
    'HAND': {'stem': [0], 'palm': [1]},
    'TREE': {'trunk': [0], 'boughs': [1, 2]},
    'SAIL': {'mast': [0], 'cloth': [1]},
    'BEARER': {'hull': [0], 'keel': [1]},
    'NEW': {'stump': [0, 1, 2], 'shoot': [3, 4]},
    'DOOR': {'post': [0]},
}
CONDITIONS = {
    'MIST': ('nael', 'the grey; the breath; the sky it made'),
    'WHITE': ('lenn', 'the white: open sky, snow, hard light'),
    'DREAD': ('senth', 'the dread; the burning place of their guns'),
    'WATER': ('thenn', 'on the water; the sea'),
    'STILL': ('vaere', 'still water; silence; the stillness'),
    'DARK': ('veath', 'night; the dark'),
}
FRINGE_WORDS = ('all', 'few', 'half', 'only', 'more', 'most', 'again', 'still', 'last', 'slow', 'gently')
FOOT_FRINGE = ('again', 'still', 'last', 'slow', 'gently')
ROLES = {'→': 'to', '->': 'to', '⇒': 'then', '=>': 'then', '→in': 'in', '→with': 'with', '→for': 'for',
         '→bc': 'bc', '→as': 'as', '→thru': 'thru', '→that': 'that'}
ARROW = {'to': '→', 'then': '⇒', 'in': '→in', 'with': '→with', 'for': '→for', 'bc': '→bc', 'as': '→as',
         'thru': '→thru', 'that': '→that', 'blind': '→bc'}
GLOSS_ROLE = {'to': 'to', 'then': 'then', 'in': 'in', 'with': 'with', 'for': 'for', 'bc': 'because',
              'as': 'as', 'thru': 'through', 'that': 'that', 'blind': 'why, the wood does not hold'}


def umax(sg):
    um = 0.0
    for el in sg['els']:
        t = el['t']
        if t == 'cut':
            um = max(um, max(p[0] for p in el['p']))
        if 'c' in el:
            if el.get('across'):
                um = max(um, el['c'][0] + el.get('w', 0.1))
            else:
                um = max(um, el['c'][0] + el.get('len', 0.2) / 2)
        if t in ('bar', 'ringarc'):
            um = max(um, el['u'])
        if t == 'scar':
            um = max(um, el['base'])
        if t == 'wedge':
            um = max(um, el['apex'][0])
        if t == 'check':
            um = max(um, el['u0'])
        if t == 'tri':
            um = max(um, max(p[0] for p in el['p']))
    return min(um, 0.97)


# =================================================================================================
#  GRAIN NOTATION v2: the model, the parser, the JSON readers and the canonical printer (v2 13)
# =================================================================================================
class GNError(ValueError):
    pass


class Token:
    """One sign in a ligature: prefixes, SIGN, :part, suffixes, {fringe} (v2 13.2)."""
    __slots__ = ('sign', 'part', 'not_', 'hollow', 'smooth', 'caus', 'x3', 'kind', 'half', 'q', 'root',
                 'lean', 'count', 'ord', 'span', 'fringe')

    def __init__(self, sign):
        self.sign = sign
        self.part = None
        self.not_ = self.hollow = self.smooth = self.caus = False
        self.x3 = self.kind = self.half = self.q = self.root = False
        self.lean = 0.0
        self.count = self.ord = 0
        self.span = None
        self.fringe = []

    def text(self):
        s = ('!' if self.not_ else '') + ('~' if self.hollow else '') + ('_' if self.smooth else '') + ('>' if self.caus else '')
        s += self.sign + ((':' + self.part) if self.part else '')
        if self.x3:
            s += '×3'
        if self.kind:
            s += '‿'
        if self.half:
            s += '½'
        if self.q:
            s += '?'
        if self.count:
            s += '#%d' % self.count
        if self.ord:
            s += '@%d' % self.ord
        if self.span:
            s += '^r%d' % self.span[0] + (('/%d' % self.span[1]) if self.span[1] and self.span[1] != 1 else '')
        if self.lean > 0:
            s += '/'
        elif self.lean < 0:
            s += '\\'
        if self.root:
            s += '*'
        if self.fringe:
            s += '{' + ','.join(self.fringe) + '}'
        return s


TOK_RE = re.compile(r'^([!~_>]*)([A-Z]+)(?::([a-z]+))?(.*)$')


def parse_token(txt):
    txt = txt.strip()
    m = TOK_RE.match(txt)
    if not m:
        raise GNError('bad grain token: %r' % txt)
    pre, name, part, suf = m.groups()
    if name not in SIGNS:
        raise GNError('unknown sign: %s' % name)
    t = Token(name)
    t.part = part
    if part and (name not in PARTS or part not in PARTS[name]):
        raise GNError('unknown part %s:%s' % (name, part))
    for ch in pre:
        if ch == '!':
            t.not_ = True
        elif ch == '~':
            t.hollow = True
        elif ch == '_':
            t.smooth = True
        elif ch == '>':
            t.caus = True
    fm = re.search(r'\{([a-z,\s]*)\}\s*$', suf)
    if fm:
        t.fringe = [x.strip() for x in fm.group(1).split(',') if x.strip()]
        for f in t.fringe:
            if f not in FRINGE_WORDS:
                raise GNError('unknown fringe mark %r' % f)
        suf = suf[:fm.start()]
    while suf:
        mm = re.match(r'^(×3|x3|X3)', suf)
        if mm:
            t.x3 = True
            suf = suf[mm.end():]
            continue
        mm = re.match(r'^\^r(\d+)(?:/(\d+))?', suf)
        if mm:
            t.span = (int(mm.group(1)), int(mm.group(2) or 1))
            suf = suf[mm.end():]
            continue
        mm = re.match(r'^([#@])([1-4])', suf)
        if mm:
            if mm.group(1) == '#':
                t.count = int(mm.group(2))
            else:
                t.ord = int(mm.group(2))
            suf = suf[mm.end():]
            continue
        c = suf[0]
        suf = suf[1:]
        if c == '‿':
            t.kind = True
        elif c == '½':
            t.half = True
        elif c == '?':
            t.q = True
        elif c == '*':
            t.root = True
        elif c == '/':
            t.lean = 16.0
        elif c == '\\':
            t.lean = -16.0
        elif c.isspace():
            pass
        else:
            raise GNError('bad suffix %r in %r' % (c, txt))
    return t


ITEM_BAND_RE = re.compile(r'^(.*?)\[(MIST|WHITE|DREAD|WATER|STILL|DARK)\]$')


def split_top(s, sep='+'):
    out, depth, cur = [], 0, ''
    for ch in s:
        if ch in '([{':
            depth += 1
        elif ch in ')]}':
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ''
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out]


class Lig:
    """A ligature (modifier + head), or v1's composite root (the sliver: HOLD+(A = B)+[X within A])."""
    def __init__(self, text):
        self.raw = text.strip()
        self.toks = []
        self.composite = None
        self.band = None          # grain_v2 21 A1: a band on an item, X[MIST]; or a band alone, [MIST]
        body = self.raw
        root = False
        bm = ITEM_BAND_RE.match(body)
        if bm:
            self.band = bm.group(2)
            body = bm.group(1).strip()
            if not body:
                self.root = False
                return
        if '(' in body or '[' in body:
            if body.endswith('*'):
                root = True
                body = body[:-1]
            parts = []
            for piece in split_top(body):
                if piece.startswith('('):
                    a, b = [x.strip() for x in piece.strip('()').split('=')]
                    parts.append({'kind': 'pair', 'a': parse_token(a), 'b': parse_token(b)})
                elif piece.startswith('['):
                    inner = piece.strip('[]')
                    x, host = [y.strip() for y in inner.split(' within ')]
                    parts.append({'kind': 'within', 'tok': parse_token(x), 'host': host})
                else:
                    parts.append({'kind': 'tok', 'tok': parse_token(piece)})
            self.composite = parts
            self.root = root
            return
        for piece in split_top(body):
            self.toks.append(parse_token(piece))
        if len(self.toks) > 2:
            raise GNError('a ligature holds at most two signs: %r' % text)
        self.root = any(t.root for t in self.toks)

    def text(self):
        if self.composite:
            out = []
            for p in self.composite:
                if p['kind'] == 'tok':
                    out.append(p['tok'].text())
                elif p['kind'] == 'pair':
                    out.append('(%s = %s)' % (p['a'].text(), p['b'].text()))
                else:
                    out.append('[%s within %s]' % (p['tok'].text(), p['host']))
            return '+'.join(out) + ('*' if self.root else '')
        return '+'.join(t.text() for t in self.toks) + (('[%s]' % self.band) if self.band else '')

    def span(self):
        for t in self.toks:
            if t.span:
                return t.span
        return None

    def fringe(self):
        out = []
        for t in self.toks:
            out += t.fringe
        return out


class Mark:
    def __init__(self, file_, lig, pith=None, cell=None):
        self.file = file_
        self.lig = lig
        self.pith = pith
        self.cell = cell          # 1-based, or None when the file holds one mark in that year
        self.ring = self.year = None
        self.graft = None
        self.key = None           # (knowing index, order) for JSON-packed texts

    @property
    def root(self):
        return self.lig.root


class Pocket:
    def __init__(self, pid, kind, s0, s1, items):
        self.pid, self.kind, self.s0, self.s1, self.items = pid, kind, s0, s1, items
        self.ring = self.year = None

    @property
    def file(self):
        return self.s0

    def text(self):
        inner = '  '.join(it.text() for it in self.items)
        return 'pocket %s %s %s–%s { %s }' % (self.pid, self.kind, fstr(self.s0), fstr(self.s1), inner)


class Cond:
    def __init__(self, band, s0, s1, pith=None):
        self.band, self.s0, self.s1, self.pith = band, s0, s1, pith

    @property
    def full(self):
        return self.s0 is None

    def text(self):
        if self.full:
            return 'band %s files all' % self.band
        pp = ('p%d·' % self.pith) if self.pith is not None else ''
        return 'band %s files %s%s–%s' % (self.band, pp, fstr(self.s0), fstr(self.s1))


class Year:
    def __init__(self, y):
        self.y = y
        self.items = []
        self.conds = []


class Ring:
    def __init__(self, k, band):
        self.k, self.band = k, band
        self.years = []
        self.inc = []             # included bark on this ring's line: pith indices, or [None] (the round)
        self.empty = False

    def year(self, y):
        while len(self.years) < y:
            self.years.append(Year(len(self.years) + 1))
        return self.years[y - 1]

    @property
    def marks(self):
        return [it for yr in self.years for it in yr.items if isinstance(it, Mark)]


class Runner:
    def __init__(self, rid, src, role, tgts, hidden=False, seeming=False):
        self.rid, self.src, self.role, self.tgts = rid, src, role, tgts
        self.hidden, self.seeming = hidden, seeming
        self.split = len(tgts) > 1


def fstr(f):
    return ('%g' % f) if f is not None else ''


def addr_text(a):
    pith, f, cell, k, y = a
    return '%s%s%s.r%d/%d' % (('p%d·' % pith) if pith is not None else '', fstr(f), ('.%d' % cell) if cell else '', k, y)


def tgt_text(t):
    if t[0] == 'mark':
        return addr_text(t[1])
    if t[0] == 'file':
        return '@%s' % fstr(t[1])
    if t[0] == 'pocket':
        return t[1]
    if t[0] == 'blind':
        return '∅'
    if t[0] == 'bind':
        return 'bind %s' % t[1]
    raise GNError('bad target %r' % (t,))


ADDR_RE = re.compile(r'^(?:p(\d+)[·.])?(-?\d+(?:\.\d+)?)\.r(\d+)(?:/(\d+))?$')


def parse_addr(s):
    s = s.strip()
    # a cell is written file.cell: 12.2.r5/1 ; a plain file is 12.r5/1
    m = re.match(r'^(?:p(\d+)[·.])?(\d+)(?:\.(\d))?\.r(\d+)(?:/(\d+))?$', s)
    if not m:
        raise GNError('bad address %r' % s)
    p, f, c, k, y = m.groups()
    return (int(p) if p is not None else None, int(f), int(c) if c else None, int(k), int(y or 1))


class Model:
    """A round in Grain Notation v2, with its front matter."""
    def __init__(self):
        self.id = None
        self.meta = {}
        self.wood = 'plain'
        self.pith = 'round'
        self.npith = 1
        self.axis = None
        self.K = 0
        self.rules = []
        self.cells = None
        self.rings = []           # Ring 1..K at index 0..K-1
        self.bark = []            # [(file, Lig)]
        self.pale = 0
        self.runners = []
        self.laps = []            # (over, under)
        self.braids = []          # (bid, [strands], pattern)
        self.binds = []           # (kid, [strands], out role or None, out addr or None)
        self.rays = []            # (pith, file, (k0, y0), (k1, y1))
        self.mems = []            # (pith, file, (k, y))
        self.pk_runs = []         # runners among a pocket's items (v2 21 A2): (rid, pid, i, role, j)

    @property
    def seed(self):
        return self.meta.get('seed', self.id)

    def ring(self, k):
        while len(self.rings) < k:
            self.rings.append(Ring(len(self.rings) + 1, 'I'))
        return self.rings[k - 1]

    def all_marks(self):
        return [m for r in self.rings for m in r.marks]

    def mark_at(self, a):
        pith, f, cell, k, y = a
        if k < 1 or k > len(self.rings):
            return None
        best = None
        for yr in self.rings[k - 1].years:
            for it in yr.items:
                if isinstance(it, Mark) and it.file == f and it.pith == pith and yr.y == y:
                    if cell is None or it.cell == cell or (it.cell is None and cell == 1):
                        return it
        # a span (^r) holds the mark through later rings
        for r in self.rings[:k]:
            for yr in r.years:
                for it in yr.items:
                    if isinstance(it, Mark) and it.file == f and it.pith == pith and it.lig.span():
                        sk, sy = it.lig.span()
                        if r.k <= k <= sk:
                            best = it
        return best

    def pocket(self, pid):
        for r in self.rings:
            for yr in r.years:
                for it in yr.items:
                    if isinstance(it, Pocket) and it.pid == pid:
                        return it
        return None

    def has_years(self):
        return any(len(r.years) > 1 for r in self.rings) or any(
            it.cell for r in self.rings for yr in r.years for it in yr.items if isinstance(it, Mark))


# ------------------------------------------------------------------------------------ parser
FRONT_RE = re.compile(r'^#\s*([A-Za-z_]+)\s*:\s*(.*)$')
PK_RUN_RE = re.compile(r'^run\s+(\S+)\s+(P\w*)\.(\d+)\s+(\S+)\s+(P\w*)\.(\d+)$')


def parse_gn(text):
    md = Model()
    band = 'I'
    section = 'rings'
    last_ring = 0
    last_mark = None
    for ln in text.split('\n'):
        raw = ln.rstrip()
        s = raw.strip()
        if not s:
            continue
        fm = FRONT_RE.match(s)
        if fm:
            key, val = fm.group(1).lower(), fm.group(2).strip()
            if val.lower() in ('true', 'yes'):
                val = True
            elif val.lower() in ('false', 'no'):
                val = False
            md.meta[key] = val
            continue
        if s.startswith('round '):
            m = re.match(r'^round\s+(\S+)\s*\{(.*)\}\s*$', s)
            if not m:
                raise GNError('bad header: %r' % s)
            md.id = m.group(1)
            for attr in [a.strip() for a in m.group(2).split(';') if a.strip()]:
                if attr.startswith('wood:'):
                    md.wood = attr.split(':', 1)[1].strip()
                elif attr.startswith('pith:'):
                    v = attr.split(':', 1)[1].strip()
                    mm = re.match(r'^(round|war)(?:\s*×\s*(\d+))?$', v)
                    if not mm:
                        raise GNError('bad pith %r' % v)
                    md.pith, md.npith = mm.group(1), int(mm.group(2) or 1)
                elif attr.startswith('rings:'):
                    md.K = int(attr.split(':', 1)[1])
                elif attr.startswith('rules after:'):
                    v = attr.split(':', 1)[1].strip().strip('[]')
                    md.rules = [int(x) for x in v.split(',') if x.strip()]
                elif attr.startswith('cells:'):
                    v = attr.split(':', 1)[1].strip().strip('[]')
                    md.cells = [int(x) for x in v.split(',') if x.strip()]
                elif attr.startswith('axis'):
                    md.axis = float(re.sub(r'[^0-9.\-]', '', attr[4:]))
                else:
                    raise GNError('unknown header attribute %r' % attr)
            continue
        if s in ('I', 'II', 'III'):
            band = s
            section = 'rings'
            continue
        if s.startswith('‖') or s.startswith('¦'):
            m = re.match(r'^(‖?)(¦?)\s*(.*)$', s)
            rl, inc, rest = m.groups()
            if inc:
                piths = [int(x) for x in re.findall(r'p(\d+)', rest)] or [None]
                md.ring(last_ring).inc = sorted(set(md.ring(last_ring).inc + piths), key=lambda v: -1 if v is None else v)
            continue
        if s == 'bark':
            section = 'bark'
            continue
        if s == 'runners':
            section = 'devices'
            continue
        m = re.match(r'^r(\d+)(?:/(\d+))?(?:\s+(.*))?$', s)
        if m and section in ('rings',):
            k, y, rest = int(m.group(1)), int(m.group(2) or 1), m.group(3) or ''
            ring = md.ring(k)
            ring.band = band
            last_ring = k
            yr = ring.year(y)
            last_mark = parse_items(rest, ring, yr, md)
            continue
        if s.startswith('bark ') and section == 'bark':
            m = re.match(r'^bark\s+(\d+)\s*:\s*(.+)$', s)
            md.bark.append((int(m.group(1)), Lig(m.group(2))))
            continue
        if s.startswith('pale '):
            md.pale = int(s.split()[1])
            continue
        pm = PK_RUN_RE.match(s)
        if pm:
            # a runner among a pocket's items (v2 21 A2): P3.1 → P3.2; it never leaves its pocket
            role = ROLES.get(pm.group(4))
            if role is None or pm.group(2) != pm.group(5):
                raise GNError('bad pocket runner %r' % s)
            md.pk_runs.append((pm.group(1), pm.group(2), int(pm.group(3)), role, int(pm.group(6))))
            section = 'devices'
            continue
        if s.startswith('run ') or s.startswith('tie '):
            md.runners.append(parse_run(s))
            section = 'devices'
            continue
        if s.startswith('lap '):
            m = re.match(r'^lap\s+(\S+)\s*⊳\s*(\S+)$', s)
            md.laps.append((m.group(1), m.group(2)))
            continue
        if s.startswith('braid '):
            m = re.match(r'^braid\s+(\S+)\s+(.+?)\s*:\s*([abc]+!?)$', s)
            md.braids.append((m.group(1), m.group(2).split(), m.group(3)))
            continue
        if s.startswith('bind '):
            m = re.match(r'^bind\s+(\S+)\s+(.+?)(?:\s+(→|⇒)\s+(\S+))?$', s)
            strands = m.group(2).split()
            out = (('then' if m.group(3) == '⇒' else 'to'), parse_addr(m.group(4))) if m.group(3) else None
            md.binds.append((m.group(1), strands, out))
            continue
        if s.startswith('ray '):
            m = re.match(r'^ray\s+(?:p(\d+)·)?(\d+)\s*:\s*r(\d+)(?:/(\d+))?\s*[–-]\s*r(\d+)(?:/(\d+))?$', s)
            if not m:
                raise GNError('bad ray %r' % s)
            g = m.groups()
            md.rays.append((int(g[0]) if g[0] else None, int(g[1]), (int(g[2]), int(g[3] or 1)), (int(g[4]), int(g[5] or 1))))
            continue
        if s.startswith('mem '):
            m = re.match(r'^mem\s+(?:p(\d+)·)?(\d+)\s*:\s*r(\d+)(?:/(\d+))?\s*→\s*pith$', s)
            if not m:
                raise GNError('bad memory ray %r' % s)
            g = m.groups()
            md.mems.append((int(g[0]) if g[0] else None, int(g[1]), (int(g[2]), int(g[3] or 1))))
            continue
        raise GNError('cannot read line: %r' % s)
    if md.id is None:
        raise GNError('no header')
    if md.K and len(md.rings) < md.K:
        md.ring(md.K)
    md.K = len(md.rings)
    for r in md.rings:
        if not r.years:
            r.year(1)
            r.empty = True
        elif not any(yr.items for yr in r.years):
            r.empty = r.empty or False
    return md


def parse_items(rest, ring, yr, md):
    """Marks, pockets, conditions and grafts on one year line."""
    i = 0
    s = rest
    last = None
    while i < len(s):
        while i < len(s) and s[i].isspace():
            i += 1
        if i >= len(s):
            break
        if s.startswith('pocket ', i):
            pk, i = parse_pocket(s, i)
            pk.ring, pk.year = ring.k, yr.y
            yr.items.append(pk)
            continue
        if s.startswith('band ', i):
            m = re.compile(r'band\s+([A-Z]+)\s+files\s+(all|(?:p(\d+)·)?(\d+)\s*[–-]\s*(\d+))').match(s, i)
            if not m:
                raise GNError('bad band in %r' % s)
            if m.group(2) == 'all':
                yr.conds.append(Cond(m.group(1), None, None))
            else:
                yr.conds.append(Cond(m.group(1), int(m.group(4)), int(m.group(5)), int(m.group(3)) if m.group(3) else None))
            i = m.end()
            continue
        if s.startswith('graft(', i):
            j = s.index(')', i)
            if last is None:
                raise GNError('a graft needs a mark before it')
            last.graft = s[i + 6:j]
            i = j + 1
            continue
        if s[i] == '·':
            ring.empty = True
            i += 1
            continue
        m = re.compile(r'(?:p(\d+)·)?(\d+)(?:\.(\d))?:\s+').match(s, i)
        if not m:
            raise GNError('cannot read %r' % s[i:])
        j = m.end()
        depth = 0
        k = j
        while k < len(s):
            ch = s[k]
            if ch in '([{':
                depth += 1
            elif ch in ')]}':
                depth -= 1
            elif ch.isspace() and depth == 0:
                break
            k += 1
        mk = Mark(int(m.group(2)), Lig(s[j:k]), int(m.group(1)) if m.group(1) else None, int(m.group(3)) if m.group(3) else None)
        mk.ring, mk.year = ring.k, yr.y
        yr.items.append(mk)
        last = mk
        i = k
    return last


def parse_pocket(s, i):
    m = re.compile(r'pocket\s+(\S+)\s+(said|cut)\s+(\d+)\s*[–-]\s*(\d+)\s*\{').match(s, i)
    if not m:
        raise GNError('bad pocket in %r' % s[i:])
    j = m.end()
    depth = 1
    k = j
    while k < len(s) and depth:
        if s[k] == '{':
            depth += 1
        elif s[k] == '}':
            depth -= 1
        k += 1
    inner = s[j:k - 1]
    items = []
    q = 0
    while q < len(inner):
        while q < len(inner) and inner[q].isspace():
            q += 1
        if q >= len(inner):
            break
        if inner.startswith('pocket ', q):
            pk, q = parse_pocket(inner, q)
            items.append(pk)
            continue
        e = q
        depth = 0
        while e < len(inner):
            ch = inner[e]
            if ch in '([{':
                depth += 1
            elif ch in ')]}':
                depth -= 1
            elif ch.isspace() and depth == 0:
                break
            e += 1
        items.append(Lig(inner[q:e]))
        q = e
    if len(items) > 8:
        raise GNError('a pocket holds at most eight items')
    return Pocket(m.group(1), m.group(2), int(m.group(3)), int(m.group(4)), items), k


def parse_target(t):
    t = t.strip()
    if t == '∅':
        return ('blind',)
    if t.startswith('@'):
        return ('file', int(t[1:]))
    if t.startswith('bind'):
        return ('bind', t.split()[1])
    if re.match(r'^P\w*$', t) and '.r' not in t:
        return ('pocket', t)
    return ('mark', parse_addr(t))


def parse_run(s):
    if s.startswith('tie '):
        m = re.match(r'^tie\s+(\S+)\s*(?:→|->)\s*(\S+)$', s)
        a, b = parse_addr(m.group(1)), parse_addr(m.group(2))
        return Runner('t%d' % (fnv1a(s) % 1000), a, 'to' if a[3] == b[3] else 'then', [('mark', b)])
    m = re.match(r'^run\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+?)(\s+[_~]+)?$', s)
    if not m:
        raise GNError('bad runner %r' % s)
    rid, src, arrow, tgt, fl = m.groups()
    role = ROLES.get(arrow)
    if role is None:
        raise GNError('unknown arrow %r' % arrow)
    fl = (fl or '').strip()
    if tgt.startswith('{'):
        tg = [parse_target(x) for x in tgt.strip('{}').split(',')]
        if len(tg) > 3:
            raise GNError('a runner forks into three shoots at most')
    else:
        tg = [parse_target(tgt)]
    if tg[0][0] == 'blind':
        role = 'blind'
    return Runner(rid, parse_addr(src), role, tg, hidden='_' in fl, seeming='~' in fl)


# ------------------------------------------------------------------------------ JSON readers
def read_json(doc):
    """A v1 grain text (bands/rings/marks, wf6 10.2) or a v2 one (rings/knowings, v2 13.6)."""
    if 'bands' in doc:
        return read_v1(doc)
    return read_v2(doc)


def _meta_from(doc, md):
    for key in ('english', 'literal', 'root_word', 'name', 'kind', 'split', 'char', 'stage0_english', 'stage0_desc',
                'has_stage0', 'file', 'title', 'desc', 'seed'):
        if key in doc:
            md.meta[key] = doc[key]


def read_v1(doc):
    md = Model()
    md.id = doc['id']
    _meta_from(doc, md)
    md.wood = 'stone' if doc.get('stone') else doc.get('wood', 'plain')
    md.pith = doc.get('pith', 'round')
    md.axis = doc.get('axis')
    if doc.get('piths'):
        md.npith = len(doc['piths'])
    k = 0
    bands_of = []
    for b in doc['bands']:
        for r in b['rings']:
            k += 1
            ring = md.ring(k)
            ring.band = b.get('band', 'I')
            bands_of.append(ring.band)
            yr = ring.year(1)
            if r.get('empty') or not r.get('marks'):
                ring.empty = not r.get('marks')
            for m in r.get('marks', []):
                if isinstance(m, dict):
                    lig = Lig(composite_text(m))
                    mk = Mark(int(m.get('file', 0)), lig, m.get('pith'))
                else:
                    mm = re.match(r'^\s*(?:p(\d+)\s*[·.]\s*)?(\d+)\s*:\s*(.+?)\s*$', m)
                    mk = Mark(int(mm.group(2)), Lig(mm.group(3)), int(mm.group(1)) if mm.group(1) else None)
                mk.ring, mk.year = k, 1
                yr.items.append(mk)
            for c in r.get('conditions', []):
                files = c.get('files', 'all')
                if files == 'all' or files is None:
                    yr.conds.append(Cond(c['c'].upper(), None, None))
                else:
                    yr.conds.append(Cond(c['c'].upper(), int(files[0]), int(files[1]), c.get('pith')))
            inc = r.get('included')
            if inc:
                ring.inc = [None] if inc is True else list(inc)
            for gr in r.get('graft', []):
                for it in yr.items:
                    if isinstance(it, Mark) and it.file == int(gr['file']):
                        it.graft = gr['from']
    md.K = k
    rules = doc.get('rules')
    if rules is None:
        rules = [i + 1 for i in range(len(bands_of) - 1) if bands_of[i] != bands_of[i + 1]]
    md.rules = list(rules)
    for bm in (doc.get('bark') or {}).get('marks', []):
        mm = re.match(r'^\s*(\d+)\s*:\s*(.+?)\s*$', bm)
        md.bark.append((int(mm.group(1)), Lig(mm.group(2))))
    md.pale = int((doc.get('bark') or {}).get('pale', 0))
    for i, t in enumerate(doc.get('ties', [])):
        mm = re.match(r'^\s*(?:p(\d+)\s*[·.]\s*)?(\d+)\.r(\d+)\s*(?:→|->)\s*(\d+)\.r(\d+)\s*$', t)
        p, a, ra, b, rb = mm.groups()
        pith = int(p) if p is not None else None
        src = (pith, int(a), None, int(ra), 1)
        tgt_mark = md.mark_at((pith, int(b), None, int(rb), 1))
        tgt = ('mark', (pith, int(b), None, int(rb), 1)) if tgt_mark else ('file', int(b))
        md.runners.append(Runner('t%d' % (i + 1), src, 'to' if ra == rb else 'then', [tgt]))
    for r in doc.get('rays', []):
        mm = re.match(r'^\s*(?:p(\d+)\s*[·.]\s*)?(\d+)\s*:\s*r(\d+)\s*[–-]\s*r(\d+)\s*$', r)
        g = mm.groups()
        md.rays.append((int(g[0]) if g[0] else None, int(g[1]), (int(g[2]), 1), (int(g[3]), 1)))
    for r in doc.get('memory', []):
        mm = re.match(r'^\s*(?:p(\d+)\s*[·.]\s*)?(\d+)\s*:\s*r(\d+)\s*$', r)
        g = mm.groups()
        md.mems.append((int(g[0]) if g[0] else None, int(g[1]), (int(g[2]), 1)))
    return md


def composite_text(m):
    """v1's object mark (VI-1) as the GN composite HOLD+(HOME/ = HOMESTONE\\)+[US×3 within HOME]*."""
    parts = m['parts']
    out = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if p.get('lean') and i + 1 < len(parts) and parts[i + 1].get('lean') and not parts[i + 1].get('in_curl'):
            a, b = p, parts[i + 1]
            out.append('(%s%s = %s%s)' % (a['sign'], '/' if a['lean'] > 0 else '\\', b['sign'], '/' if b['lean'] > 0 else '\\'))
            i += 2
            continue
        if p.get('in_curl'):
            host = [q for q in parts if q.get('lean')][p['in_curl'] - 1]['sign']
            out.append('[%s%s within %s]' % (p['sign'], '×3' if p.get('x3') else '', host))
            i += 1
            continue
        out.append(p['sign'])
        i += 1
    return '+'.join(out) + ('*' if m.get('root') else '')


def read_v2(doc):
    """A v2 grain text: knowings listed in the telling's order. They are packed into years and cells
    later (pack_model), because the cells a ring may hold depend on its radius (v2 4.4)."""
    md = Model()
    md.id = doc['id']
    _meta_from(doc, md)
    md.wood = doc.get('wood', 'plain')
    md.pith = doc.get('pith', 'round')
    md.axis = doc.get('axis')
    md.rules = list(doc.get('rules', []))
    md.knowings = []
    for k, ring in enumerate(doc['rings'], start=1):
        r = md.ring(k)
        r.band = ring.get('band', 'I')
        kns = ring.get('knowings', ring.get('lamellae', []))
        lst = []
        for i, kn in enumerate(kns, start=1):
            marks = []
            for ms in kn.get('marks', []):
                mm = re.match(r'^\s*(?:p(\d+)\s*[·.]\s*)?(\d+)\s*:\s*(.+?)\s*$', ms)
                mk = Mark(int(mm.group(2)), Lig(mm.group(3)), int(mm.group(1)) if mm.group(1) else None)
                mk.key = (i, len(marks))
                marks.append(mk)
            pockets = []
            for pk in kn.get('pockets', []):
                pockets.append(Pocket(pk['id'], pk['kind'], int(pk['files'][0]), int(pk['files'][1]),
                                      [Lig(x) for x in pk.get('contents', [])]))
            conds = [Cond(c['band'], int(c['files'][0]), int(c['files'][1])) for c in kn.get('conds', [])]
            lst.append({'marks': marks, 'pockets': pockets, 'conds': conds, 'bind_room': False})
        md.knowings.append(lst)
    md.K = len(md.rings)
    for bm in (doc.get('bark') or {}).get('marks', []):
        mm = re.match(r'^\s*(\d+)\s*:\s*(.+?)\s*$', bm)
        md.bark.append((int(mm.group(1)), Lig(mm.group(2))))
    md.pale = int((doc.get('bark') or {}).get('pale', 0))
    md.json_runners = doc.get('runners', [])
    md.laps = [(l['over'], l['under']) for l in doc.get('laps', [])]
    md.braids = [(b['id'], list(b['strands']), b['pattern']) for b in doc.get('braids', [])]
    md.json_binds = doc.get('binds', [])
    md.rays, md.mems = [], []
    return md


def json_addr(md, s):
    """'12.r5·3' (file, ring, knowing) -> the packed address; 'bearing f' -> a file referent."""
    s = s.strip()
    m = re.match(r'^bearing\s+(\d+)$', s)
    if m:
        return ('file', int(m.group(1)))
    if s == '∅':
        return ('blind',)
    if s.startswith('bind:'):
        return ('bind', s[5:])
    if re.match(r'^P\w*$', s):
        return ('pocket', s)
    m = re.match(r'^(?:p(\d+)·)?(\d+)\.r(\d+)(?:[·.](\d+))?$', s)
    if not m:
        raise GNError('bad JSON address %r' % s)
    pith = int(m.group(1)) if m.group(1) else None
    f, k, i = int(m.group(2)), int(m.group(3)), int(m.group(4) or 1)
    kn = md.knowings[k - 1][i - 1]
    for mk in kn['marks']:
        if mk.file == f and mk.pith == pith:
            return ('mark', (pith, f, mk.cell, k, mk.year))
    raise GNError('no mark at %s' % s)


# ------------------------------------------------------------------------- canonical printer
def canon_key_addr(md, a):
    pith, f, cell, k, y = a
    return (k, y, pith if pith is not None else -1, f % 16, cell or 0)


def print_gn(md, cells=None, front=True):
    """The canonical Grain Notation v2 of a round (v2 13.4)."""
    out = []
    if front:
        for key in ('name', 'english', 'literal', 'root_word', 'split', 'char', 'stage0_english', 'title', 'desc', 'seed'):
            if key in md.meta and md.meta[key] not in (None, ''):
                v = md.meta[key]
                if v is True:
                    v = 'true'
                out.append('# %s: %s' % (key, v))
    attrs = ['wood: %s' % md.wood, 'pith: %s%s' % (md.pith, (' ×%d' % md.npith) if md.npith > 1 else ''),
             'rings: %d' % len(md.rings), 'rules after: [%s]' % ', '.join(str(r) for r in md.rules)]
    if cells and md.has_years():
        attrs.append('cells: [%s]' % ', '.join(str(c) for c in cells))
    if md.axis is not None:
        attrs.append('axis %g°' % md.axis)
    out.append('round %s {%s}' % (md.id, '; '.join(attrs)))
    cur = None
    for ring in md.rings:
        if ring.band != cur:
            out.append('  ' + ring.band)
            cur = ring.band
        for yr in ring.years:
            items = sorted(yr.items, key=lambda it: ((it.pith if isinstance(it, Mark) and it.pith is not None else -1),
                                                    it.file % 16, (it.cell or 0) if isinstance(it, Mark) else 0))
            cells_txt = []
            for it in items:
                if isinstance(it, Mark):
                    t = '%s%s%s: %s' % (('p%d·' % it.pith) if it.pith is not None else '', fstr(it.file),
                                        ('.%d' % it.cell) if it.cell else '', it.lig.text())
                    if it.graft:
                        t += '    graft(%s)' % it.graft
                    cells_txt.append(t)
                else:
                    cells_txt.append(it.text())
            line = '    r%-3s' % ('%d/%d' % (ring.k, yr.y))
            if not items and ring.empty and len(ring.years) == 1:
                line += '  ·'
            line += '  ' + '    '.join(cells_txt)
            if yr.conds:
                line += '      ' + '  '.join(c.text() for c in yr.conds)
            out.append(line.rstrip())
        if ring.inc:
            out.append('  ¦' + ((' ' + ','.join('p%d' % p for p in ring.inc if p is not None)) if any(p is not None for p in ring.inc) else ''))
        if ring.k in md.rules:
            out.append('  ‖')
    if md.bark or md.pale:
        out.append('  bark')
        for f, lig in sorted(md.bark, key=lambda b: b[0]):
            out.append('    bark %s: %s' % (fstr(f), lig.text()))
        if md.pale:
            out.append('    pale %d' % md.pale)
    if md.runners or md.mems or md.rays or md.pk_runs:
        out.append('  runners')
    for rn in sorted(md.runners, key=lambda r: runner_key(md, r)):
        tg = tgt_text(rn.tgts[0]) if len(rn.tgts) == 1 else '{%s}' % ', '.join(tgt_text(t) for t in rn.tgts)
        fl = (' _' if rn.hidden else '') + (' ~' if rn.seeming else '')
        out.append('    run %-4s %-12s %-6s %s%s' % (rn.rid, addr_text(rn.src), ARROW[rn.role], tg, fl))
    for rid, pid, i, role, j in md.pk_runs:
        out.append('    run %-4s %-12s %-6s %s' % (rid, '%s.%d' % (pid, i), ARROW[role], '%s.%d' % (pid, j)))
    for a, b in md.laps:
        out.append('  lap  %s ⊳ %s' % (a, b))
    for bid, strands, pat in md.braids:
        out.append('  braid %s %s : %s' % (bid, ' '.join(strands), pat))
    for kid, strands, o in md.binds:
        out.append('  bind %s %s%s' % (kid, ' '.join(strands), (' %s %s' % ('⇒' if o[0] == 'then' else '→', addr_text(o[1]))) if o else ''))
    for pith, f, a, b in md.rays:
        out.append('    ray %s%s: r%d/%d–r%d/%d' % (('p%d·' % pith) if pith is not None else '', fstr(f), a[0], a[1], b[0], b[1]))
    for pith, f, a in md.mems:
        out.append('    mem %s%s: r%d/%d → pith' % (('p%d·' % pith) if pith is not None else '', fstr(f), a[0], a[1]))
    return '\n'.join(out) + '\n'


def runner_key(md, rn):
    t = rn.tgts[0]
    tk = canon_key_addr(md, t[1]) if t[0] == 'mark' else (99, 0, 0, 0, 0)
    return (canon_key_addr(md, rn.src), tk, rn.rid)


# =================================================================================================
#  THE ROUND'S GEOMETRY: rings, years and cells (v2 4), and the fields the lines are drawn in
# =================================================================================================
JOIN_GAP = 6.0


class Knot:
    def __init__(self, th, rho, ru, rx):
        self.th, self.rho = th, rho
        self.c = ru + 6.0
        self.st = max(0.08, 1.7 * rx / max(rho, 1.0))
        self.sr = ru + 8.0


class Field:
    """Ring lines about one centre. base(k, th) is ring k's undeflected line; line(k, th) adds the
    grain's flow: knots (v1), the yield round every mark and the dip where a runner crosses (v2 4.6)."""
    def __init__(self, lay, O):
        self.lay = lay
        self.O = O
        self.knots = []
        self.bumps = {}          # k -> [(th, amp, width, kind)]

    def pt(self, rho, th):
        return (self.O[0] + rho * math.sin(th), self.O[1] - rho * math.cos(th))

    def polar(self, p):
        return polar_of(p, self.O)

    def deflect(self, rho, th, ref):
        for kn in self.knots:
            dth = wrap(th - kn.th)
            g = math.exp(-(dth / kn.st) ** 2)
            if g < 1e-4:
                continue
            s = 1.0 if ref >= kn.rho else -1.0
            rho += s * kn.c * math.exp(-((rho - kn.rho) / kn.sr) ** 2) * g
        return rho

    def line(self, k, th, flow=True):
        """Ring line k as drawn."""
        b = self.base(k, th)
        if self.knots:
            b = self.deflect(b, th, self.base(k, self.knots[0].th))
        if flow:
            for tc, amp, wdt, kind in self.bumps.get(k, ()):
                d = wrap(th - tc) * b
                if kind == 'g':
                    if abs(d) < 3 * wdt:
                        b += amp * math.exp(-(d / wdt) ** 2)
                elif abs(d) < wdt:
                    b += amp * 0.5 * (1 + math.cos(math.pi * d / wdt))
        return b

    def yr(self, k, rho0, th, deflect=True):
        """A nominal radius rho0 inside ring k carried round the ring's shape (years follow the ring)."""
        lay = self.lay
        a0, b0 = lay.R[k - 1], lay.R[k]
        fr = (rho0 - a0) / max(b0 - a0, 1e-6)
        a, b = self.base(k - 1, th), self.base(k, th)
        rho = a + fr * (b - a)
        if deflect and self.knots:
            ra = self.base(k - 1, self.knots[0].th)
            rb = self.base(k, self.knots[0].th)
            rho = self.deflect(rho, th, ra + fr * (rb - ra))
        return rho

    def samples(self, k, n, t0=0.0, t1=2 * math.pi, closed=True):
        """Angles for drawing ring line k: n even steps plus fine steps wherever the grain yields."""
        ths = [t0 + (t1 - t0) * i / n for i in range(n + (0 if closed else 1))]
        extra = []
        rho = self.lay.R[min(k, len(self.lay.R) - 1)] if k >= 0 else 50.0
        for tc, amp, wdt, kind in self.bumps.get(k, ()):
            span = (2.2 * wdt if kind == 'g' else wdt) / max(rho, 1.0)
            for q in range(-2, 3):
                extra.append(tc + span * q / 2.0)
        for kn in self.knots:
            for q in range(-6, 7):
                extra.append(kn.th + kn.st * q / 3.0)
        if not extra:
            return ths
        allt = []
        for t in ths + extra:
            if closed:
                t = t % (2 * math.pi)
            elif not (t0 <= t <= t1):
                tt = t0 + ((t - t0) % (2 * math.pi))
                if not (t0 <= tt <= t1):
                    continue
                t = tt
            allt.append(t)
        allt.sort()
        out = [allt[0]]
        for t in allt[1:]:
            if t - out[-1] > 0.35 / max(rho, 1.0):
                out.append(t)
        return out


class SimpleField(Field):
    def base(self, k, th):
        if k <= 0:
            return PITH_R
        g = self.lay
        return g.R[k] * g.f(th) + g.jitter(k, th) + g.fine_term(th) * (g.R[k] / g.R[-1]) ** 0.8


class LocalField(Field):
    """A joined round's own pith rings: near-circles never larger than R_k (they cannot touch)."""
    def __init__(self, lay, O, idx):
        Field.__init__(self, lay, O)
        r = Rng(lay.seed + '/pith/%d' % idx)
        self.h = [(m, r.uni(0, 6.283)) for m in (2, 3, 5)]
        self.idx = idx

    def base(self, k, th):
        if k <= 0:
            return PITH_R
        v = sum(math.sin(m * th + p) for m, p in self.h) / 3.0
        return self.lay.R[k] * (0.975 + 0.025 * v)


class SharedField(Field):
    """Shared rings of joined piths: level sets of smin(|x - p_i|), h = 22 (v1 G8)."""
    def __init__(self, lay, O, piths):
        Field.__init__(self, lay, O)
        self.piths = piths
        self.cache = {}

    def smin(self, x):
        h = 22.0
        return -h * math.log(sum(math.exp(-math.hypot(x[0] - p[0], x[1] - p[1]) / h) for p in self.piths))

    def level(self, val, th):
        key = (round(val, 3), round(th, 6))
        if key in self.cache:
            return self.cache[key]
        e = er(th)
        lo, hi = 0.0, 4000.0
        for _ in range(44):
            mid = 0.5 * (lo + hi)
            if self.smin((self.O[0] + e[0] * mid, self.O[1] + e[1] * mid)) < val:
                lo = mid
            else:
                hi = mid
        self.cache[key] = lo
        return lo

    def base(self, k, th):
        g = self.lay
        if k <= g.kj:
            val = g.R[g.kj] + JOIN_GAP
        else:
            val = g.R[k] + 0.35 * g.R[k] * (g.f(th) - 1) + g.jitter(k, th) * 0.6
        return self.level(val, th)


class Layout:
    """Ring widths, years and cells of a round (v2 4.2-4.5), from its model and its seed."""
    def __init__(self, md, plate=None):
        self.md = md
        self.seed = seed = md.seed
        K = self.K = md.K
        rings = md.rings
        empty = set(r.k for r in rings if r.empty)
        rw = Rng(seed + '/widths')
        w = [0.0] * (K + 1)
        for k in range(2, K + 1):
            w[k] = 18.0 * rw.uni(0.90, 1.15) if k in empty else 46.0 * rw.uni(0.84, 1.20)
            if K > 13 and k not in empty:
                w[k] = max(26.0, w[k] * 13.0 / K)
        self.joined = md.npith > 1
        self.kj = (md.rules[0] if md.rules else 1) if self.joined else 0
        # the extra room a year needs: a pocket (v2 8) or a bind (v2 7.3)
        room = {}
        for r in rings:
            for yr in r.years:
                if any(isinstance(it, Pocket) for it in yr.items):
                    room[(r.k, yr.y)] = room.get((r.k, yr.y), 0.0) + 8.0
        for kid, strands, out in md.binds:
            site = bind_site_year(md, kid, strands)
            if site:
                room[site] = room.get(site, 0.0) + 5.0
        # a braid's cord needs 5 units clear either side (v2 7.2): the year it springs in grows 8
        # units of runner room above its marks
        self.top_room = {}
        for bid, strands, pat in md.braids:
            src = next((rn.src for rn in md.runners if rn.rid == strands[0]), None)
            if src:
                key = (src[3], src[4])
                room[key] = room.get(key, 0.0) + 8.0
                self.top_room[key] = self.top_room.get(key, 0.0) + 8.0
        self.room = room
        # the floor offset of a ring: 5 above a band-rule, 3.5 above included bark (v1)
        off = [0.0] * (K + 1)
        for k in range(2, K + 1):
            if (k - 1) in md.rules and not (self.joined and k - 1 == self.kj):
                off[k] += 5.0
            if rings[k - 2].inc:
                off[k] += 3.5
        if self.joined and self.kj < K:
            off[self.kj + 1] += 5.0
        self.off = off
        ytot = sum(len(r.years) for r in rings if len(r.years) > 1)
        pitch = YEAR if ytot <= 36 else max(26.0, YEAR * 36.0 / ytot)
        ry = Rng(seed + '/years')
        depth = {}
        for r in rings:
            k = r.k
            Y = len(r.years)
            if Y > 1:
                ds = [pitch * ry.uni(0.94, 1.08) / YEAR * YEAR for _ in range(Y)]
                for y in range(Y):
                    ds[y] += room.get((k, y + 1), 0.0)
                if k == 1 and sum(ds) < 72.0:
                    s = 72.0 / sum(ds)
                    ds = [d * s for d in ds]
                depth[k] = ds
                w[k] = off[k] + sum(ds) + (2.0 if k == 1 else 0.0)
            else:
                if room.get((k, 1)):
                    w[k] += room[(k, 1)]
        if len(rings[0].years) == 1:
            w[1] = 72.0 if K == 1 else max(56.0, min(96.0, 0.22 * sum(w[2:])))
            if any(m.root for m in rings[0].marks):
                w[1] = max(72.0, w[1])
        if self.joined and self.kj < K:
            w[self.kj + 1] += JOIN_GAP + 5.0
        self.w = w
        self.R = [PITH_R]
        for k in range(1, K + 1):
            self.R.append(self.R[-1] + w[k])
        # years: (k, y) -> (floor, top), nominal radii
        self.year_r = {}
        for r in rings:
            k = r.k
            a = self.R[k - 1] + off[k]
            if self.joined and k == self.kj + 1:
                a += JOIN_GAP
            if k in depth:
                for y, d in enumerate(depth[k], start=1):
                    self.year_r[(k, y)] = (a, a + d)
                    a += d
            else:
                self.year_r[(k, 1)] = (a, self.R[k])
        # cells per slot (v2 4.4): more rays as the girth grows
        self.cells = [None]
        for r in rings:
            k = r.k
            if md.cells and k - 1 < len(md.cells):
                c = md.cells[k - 1]
            else:
                c = 1 if k == 1 else max(1, min(4, int((self.R[k - 1] * SLOT - 6.0) / 58.0)))
            used = max([it.cell or 1 for yr in r.years for it in yr.items if isinstance(it, Mark)] + [1])
            self.cells.append(max(c, used))
        # the shape (v1 10.5)
        rs = Rng(seed + '/shape')
        self.eps = rs.uni(0.05, 0.12)
        self.phi = rs.uni(0, 2 * math.pi)
        self.harm = [(m, rs.uni(0.012, 0.030) / (m - 1), rs.uni(0, 2 * math.pi)) for m in (2, 3, 4, 5, 7)]
        self.fine = [(m, rs.uni(0.5, 1.3), rs.uni(0, 2 * math.pi)) for m in (9, 13, 17)]
        if plate:
            self.eps *= 0.2
            self.harm = [(m, a * 0.3, p) for m, a, p in self.harm]
        self.jit = [None]
        for k in range(1, K + 1):
            rj = Rng(seed + '/ring/%d' % k)
            gap = min(w[k], w[k + 1] if k < K else w[k])
            amp = min(0.025 * self.R[k], gap / 5.0, 6.0)
            hs = [(m, rj.uni(0.4, 1.0) * (1 if rj.next() < 0.5 else -1), rj.uni(0, 2 * math.pi)) for m in (2, 3, 5)]
            norm_ = sum(abs(c) for _, c, _ in hs)
            self.jit.append((amp, [(m, c / norm_, p) for m, c, p in hs]))
        rl = Rng(seed + '/latestrength')
        self.late = [None] + [[(m, Rng(seed + '/late/%d' % k).uni(0, 6.283)) for m in (2, 3, 5)] for k in range(1, K + 1)]
        self.late_op = [None] + [rl.uni(0.62, 1.12) for k in range(1, K + 1)]
        rb = Rng(seed + '/bark')
        self.bark_w = 12.0 + 4.0 * min(K, 6)
        amps = {5: 2.6, 7: 2.0, 11: 1.4, 17: 0.9, 29: 0.4, 41: 0.25}
        self.bark_n = [(m, amps[m] * rb.uni(0.55, 1.25), rb.uni(0, 2 * math.pi)) for m in (5, 7, 11, 17, 29, 41)]
        self.young = K <= 2
        nn = 0 if K == 1 else (3 + 2 * min(K, 6))
        base_t = sorted(rb.uni(0, 2 * math.pi) for _ in range(nn))
        self.notches = [(t, rb.uni(0.010, 0.030), rb.uni(0.22, 0.60) * (0.6 if self.young else 1.0)) for t in base_t]
        self.make_plates()
        self.axis_seeded = math.radians(Rng(seed + '/axis').uni(-12, 12))
        self.plate = plate
        if plate:
            # a ring plate (v2 11.5): the one ring re-laid at reading scale, its inner line at 240,
            # with the same years and cells
            off = 240.0 - self.R[plate - 1]
            inner = self.R[plate - 1]
            # the lines inside the plate are drawn nowhere, but the router finds a point's ring by
            # walking them outward, so they must stay inside it: scaled under its inner line (without
            # this a plate's runners were routed in the wrong ring and ran off the plate)
            self.R = [r + off if i >= plate - 1 else r * 240.0 / max(inner, 1.0) for i, r in enumerate(self.R)]
            for key, (a, b) in list(self.year_r.items()):
                if key[0] >= plate:
                    self.year_r[key] = (a + off, b + off)
            self.jit = [None] + [(0.0, j[1]) for j in self.jit[1:]]
            self.fine = [(m, a * 0.3, p) for m, a, p in self.fine]

    def make_plates(self):
        rp = Rng(self.seed + '/plates')
        self.plates = []
        nn = len(self.notches)
        for i, (t, wdt, dp) in enumerate(self.notches):
            t2 = self.notches[(i + 1) % nn][0]
            self.plates.append((t, (t2 - t) % (2 * math.pi) or 2 * math.pi, rp.uni(0.04, 0.11)))

    def f(self, th):
        v = 1 + self.eps * math.cos(th - self.phi)
        for m, a, ps in self.harm:
            v += a * math.sin(m * th + ps)
        return v

    def fine_term(self, th):
        return sum(a * math.sin(m * th + p) for m, a, p in self.fine)

    def jitter(self, k, th):
        amp, hs = self.jit[k]
        return amp * sum(c * math.sin(m * th + p) for m, c, p in hs)

    def late_w(self, k, th):
        n = sum(math.sin(m * th + p) for m, p in self.late[k]) / 3.0
        return max(0.8, min(3.2, 0.046 * max(min(self.w[k], 60.0), 30) * (1 + 0.6 * n)))

    def nyears(self, k):
        return len(self.md.rings[k - 1].years)


def bind_site_year(md, kid, strands):
    srcs = [rn.src for rn in md.runners if rn.rid in strands]
    if not srcs:
        return None
    s = max(srcs, key=lambda a: (a[3], a[4]))
    return (s[3], s[4])


# ------------------------------------------------------------------------------------- packing
def pack_model(md):
    """v2 4.3: knowings are placed in the telling's order; each mark takes the next free cell of its
    own file (cell by cell clockwise across the slot, then the next year outward); a pocket takes a
    whole year across its files, above the highest cursor among them. The cells a ring may hold come
    from its radius (4.4), which depends on the rings inside it, so the packing is iterated to rest."""
    if not hasattr(md, 'knowings'):
        return md
    cells = None
    used = None
    for _ in range(6):
        used = cells
        md.cells = None
        for r in md.rings:
            r.years = []
        for k, kns in enumerate(md.knowings, start=1):
            ring = md.ring(k)
            c = 1 if k == 1 else (cells[k] if cells else 1)
            cursor = {}
            for kn in kns:
                kn.pop('year', None)
                pk_files = []
                for pk in kn['pockets']:
                    n = int((pk.s1 - pk.s0) % 16)
                    pk_files += [(None, (pk.s0 + d) % 16) for d in range(n + 1)]
                if pk_files:
                    row = max([cursor.get(f, (0, 0))[0] + (1 if cursor.get(f, (0, 0))[1] else 0) for f in pk_files] + [0])
                    for f in pk_files:
                        cursor[f] = (row + 1, 0)
                    for pk in kn['pockets']:
                        pk.ring, pk.year = k, row + 1
                        ring.year(row + 1).items.append(pk)
                    kn['year'] = row + 1
                for mk in kn['marks']:
                    key = (mk.pith, mk.file % 16)
                    if mk.root:
                        mk.ring, mk.year, mk.cell = k, 1, None
                        ring.year(1).items.append(mk)
                        continue
                    rw_, cl = cursor.get(key, (0, 0))
                    mk.ring, mk.year, mk.cell = k, rw_ + 1, cl + 1
                    ring.year(rw_ + 1).items.append(mk)
                    cl += 1
                    if cl >= c:
                        rw_, cl = rw_ + 1, 0
                    cursor[key] = (rw_, cl)
                if 'year' not in kn:
                    kn['year'] = kn['marks'][0].year if kn['marks'] else 1
                for cd in kn['conds']:
                    # a condition lies in the year of the marks it holds (a mark inside a condition's
                    # files and year takes the condition, v1 3.8.5)
                    y_ = kn['year']
                    for mk in kn['marks']:
                        fs = [(cd.s0 + d) % 16 for d in range(int((cd.s1 - cd.s0) % 16) + 1)] if not cd.full else range(16)
                        if mk.file % 16 in fs:
                            y_ = mk.year
                            break
                    ring.year(y_).conds.append(cd)
            if not ring.years:
                ring.year(1)
                ring.empty = True
        # a cell is written only where a file holds more than one mark in a year (v2 13.2)
        for r in md.rings:
            for yr in r.years:
                count = {}
                for it in yr.items:
                    if isinstance(it, Mark):
                        count[(it.pith, it.file % 16)] = count.get((it.pith, it.file % 16), 0) + 1
                for it in yr.items:
                    if isinstance(it, Mark) and count[(it.pith, it.file % 16)] == 1:
                        it.cell = None
        # runners, laps, braids and binds of the JSON text, now with packed addresses
        md.runners = []
        for rn in md.json_runners:
            src = json_addr(md, rn['from'])[1]
            tg = json_addr(md, rn['to'])
            role = rn.get('role', 'to')
            if role == 'blind':
                tg = ('blind',)
            md.runners.append(Runner(rn['id'], src, role, [tg], hidden=bool(rn.get('hidden')), seeming=bool(rn.get('seeming'))))
        md.binds = []
        for bd in md.json_binds:
            out = None
            if bd.get('out'):
                out = (bd['out'].get('role', 'to'), json_addr(md, bd['out']['to'])[1])
            md.binds.append((bd['id'], list(bd['strands']), out))
        lay = Layout(md)
        new = [None] + [1 if k == 1 else max(1, min(4, int((lay.R[k - 1] * SLOT - 6.0) / 58.0))) for k in range(1, md.K + 1)]
        if used is not None and new == used:
            break
        cells = new
    md.cells = [max([1] + [it.cell or 1 for yr in r.years for it in yr.items if isinstance(it, Mark)] + [used[r.k] if used else 1])
                for r in md.rings]
    return md


# =================================================================================================
#  CUTS: facet geometry that remembers which way each wall faces, so it can be lit in any placement
# =================================================================================================
NBUCKET = 8
BUCKET_CLS = 'abcdefgh'
LINE_CLS = {            # line class -> (opacity, width) in the visible layer (v1 10.3 tiers)
    'e0': (OP['edge'], 1.0),              # hollow edges
    'e1': (OP['rim'] * 0.75, 0.7),        # a check's rim
    'e2': (OP['rim'], 0.8),               # a scar's rims
    'e3': (OP['rim'] * 0.7, 0.7),         # a knot's heart
}


def taper_w(s, tot, H, k=1.0, head=True, foot=None):
    e = min(0.16 * tot, 2.4 * H)
    ef = e if foot is None else foot
    a = 1.0 if ef <= 0 else s / ef
    b = (tot - s) / e if head else 1.0
    m = max(0.0, min(1.0, a, b))
    return k * H * m ** 0.7


class Cuts:
    """The cuts of one sign (in its local frame) or of the round's direct ink (in world frame)."""
    def __init__(self):
        self.vcuts = []          # (P, Lp, Rp, segn)
        self.chips = []          # (triangle, facing)
        self.flat, self.char, self.voids = [], [], []
        self.lines = []          # (pts, cls, closed)
        self.knots = []          # (centre, ru, rx)
        self.curls = []

    def vcut(self, pts, hw, closed=False):
        if len(pts) < 2:
            return
        P = list(pts) + ([pts[0]] if closed else [])
        Hh = list(hw) + ([hw[0]] if closed else [])
        m = len(P)
        segn = []
        for i in range(m - 1):
            d = unit(sub(P[i + 1], P[i]))
            segn.append((-d[1], d[0]))
        ns = len(segn)
        if ns == 0:
            return
        Lp, Rp = [], []
        for i in range(m):
            if closed:
                a, b = segn[(i - 1) % ns], segn[i % ns]
            else:
                a, b = segn[max(i - 1, 0)], segn[min(i, ns - 1)]
            s = (a[0] + b[0], a[1] + b[1])
            l = math.hypot(*s)
            if l < 1e-6:
                nn, k = b, 1.0
            else:
                nn = (s[0] / l, s[1] / l)
                k = min(2.0, 1.0 / max(0.5, dot(nn, b)))
            Lp.append(add(P[i], nn, Hh[i] * k))
            Rp.append(add(P[i], nn, -Hh[i] * k))
        if max(Hh) > 0.05:
            self.vcuts.append((P, Lp, Rp, segn, Hh))

    def chip(self, poly):
        c = (sum(p[0] for p in poly) / len(poly), sum(p[1] for p in poly) / len(poly))
        n = len(poly)
        for i in range(n):
            a, b = poly[i], poly[(i + 1) % n]
            mid = lerp(a, b, 0.5)
            self.chips.append(([a, b, c], unit(sub(c, mid))))

    def line(self, pts, cls, closed=False):
        self.lines.append((list(pts), cls, closed))

    def facets(self, keyfn):
        """Facet polygons grouped in runs by keyfn(facing): [(key, polygon)]."""
        out = []
        for P, Lp, Rp, segn, Hh in self.vcuts:
            ns = len(segn)
            for side, sgn in ((Lp, -1.0), (Rp, 1.0)):
                keys = [keyfn((sgn * n[0], sgn * n[1])) for n in segn]
                s = 0
                while s < ns:
                    e = s
                    while e + 1 < ns and keys[e + 1] == keys[s]:
                        e += 1
                    if max(Hh[s:e + 2]) > 0.05:
                        out.append((keys[s], P[s:e + 2] + list(reversed(side[s:e + 2]))))
                    s = e + 1
        for tri, f in self.chips:
            out.append((keyfn(f), tri))
        return out

    def outlines(self):
        """Every outline, for clearance tests: (points, closed)."""
        out = []
        for P, Lp, Rp, segn, Hh in self.vcuts:
            out.append((Lp + list(reversed(Rp)), True))
        out += [(t, True) for t, f in self.chips]
        out += [(p, True) for p in self.flat + self.char + self.voids]
        out += [(p, c) for p, cls, c in self.lines]
        return out

    def transformed(self, A, t):
        """A copy of these cuts under x -> A x + t (A = [[a, c], [b, d]] as SVG's matrix)."""
        a, b, c, d = A
        T = lambda p: (a * p[0] + c * p[1] + t[0], b * p[0] + d * p[1] + t[1])
        V = lambda v: unit((a * v[0] + c * v[1], b * v[0] + d * v[1]))
        o = Cuts()
        # a mirrored transform turns the walls' handedness: normals follow the linear part
        for P, Lp, Rp, segn, Hh in self.vcuts:
            o.vcuts.append(([T(p) for p in P], [T(p) for p in Lp], [T(p) for p in Rp], [V(n) for n in segn], Hh))
        o.chips = [([T(p) for p in tri], V(f)) for tri, f in self.chips]
        o.flat = [[T(p) for p in q] for q in self.flat]
        o.char = [[T(p) for p in q] for q in self.char]
        o.voids = [[T(p) for p in q] for q in self.voids]
        o.lines = [([T(p) for p in q], cls, c) for q, cls, c in self.lines]
        o.knots = [(T(c), ru, rx) for c, ru, rx in self.knots]
        o.curls = [T(c) for c in self.curls]
        return o

    def extend(self, other):
        self.vcuts += other.vcuts
        self.chips += other.chips
        self.flat += other.flat
        self.char += other.char
        self.voids += other.voids
        self.lines += other.lines


def bucket_of(f):
    a = math.atan2(f[1], f[0])
    return int(round(a / (2 * math.pi / NBUCKET))) % NBUCKET


def tone_of(f):
    return quant(dot(unit(f), LIGHT))


# ------------------------------------------------------------------------------ the local frame
class LFrame:
    """A sign's local frame (v1 3.4): x = u L outward along the file, y = v B clockwise across it.
    The round's centre lies at (-rin, 0), so a ring-arc curves about it."""
    def __init__(self, L, B, H, rin, mir=1.0):
        self.L, self.B, self.H, self.rin, self.mir = L, B, H, rin, mir
        self.er, self.et = (1.0, 0.0), (0.0, 1.0)

    def P(self, u, v):
        return (u * self.L, v * self.mir * self.B)

    def arc(self, rho, phi):
        return (-self.rin + rho * math.cos(phi), rho * math.sin(phi))


class SignMaker:
    """Cuts one sign into a Cuts in its local frame (v1 MarkMaker, with v2's punch, lens across,
    parts, the fringe and the kind-arc)."""
    def __init__(self, cuts, rng, open_head=False, root_foot=False):
        self.ink = cuts
        self.rng = rng
        self.open_head = open_head
        self.root_foot = root_foot

    def stroke(self, F, pts, flags, k=1.0, fill=False, head=True, foot=None):
        pts = resample(pts, max(2.0, 1.15 * F.H))
        s = arclen(pts)
        tot = s[-1] or 1e-9
        hw = [taper_w(si, tot, F.H, k, head=head, foot=foot) for si in s]
        if foot is not None:
            hw[0] = max(hw[0], 0.55 * F.H * k)
        if flags.get('hollow'):
            L, R = edges_of(pts, [h * 1.2 for h in hw])
            self.ink.line(L, 'e0')
            self.ink.line(R, 'e0')
            return
        if flags.get('smooth'):
            L, R = edges_of(pts, [h * 1.1 for h in hw])
            self.ink.line(L, 'sL')
            self.ink.line(R, 'sR')
            return
        if fill:
            L, R = edges_of(pts, [h * 1.35 for h in hw])
            self.ink.flat.append(L + list(reversed(R)))
            return
        self.ink.vcut(pts, hw)

    def groove(self, F, pts, flags, pinch=None, fill=False):
        n = len(pts)
        hw = [F.H * 0.78] * n
        if pinch:
            hw = [min(h, pinch[i]) for i, h in enumerate(hw)]
        if flags.get('hollow') or flags.get('smooth'):
            L, R = edges_of(pts + [pts[0]], hw + [hw[0]])
            if flags.get('hollow'):
                self.ink.line(L, 'e0', closed=True)
                self.ink.line(R, 'e0', closed=True)
            else:
                self.ink.line(L, 'sL', closed=True)
                self.ink.line(R, 'sR', closed=True)
            return
        if fill:
            self.ink.flat.append(list(pts))
        self.ink.vcut(pts, hw, closed=True)

    def cut_pts(self, F, el):
        p = el['p']
        if self.root_foot and p[0][0] <= 0.08:
            p = [[0.0, p[0][1]]] + [list(q) for q in p[1:]]
        pts = []
        if len(p) == 2 and el.get('bend', 0):
            a, b = p
            for i in range(17):
                t = i / 16.0
                pts.append(F.P(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t + el['bend'] * 4 * t * (1 - t)))
        elif el.get('curve') and len(p) > 2:
            ext = [p[0]] + [list(q) for q in p] + [p[-1]]
            for q in range(1, len(ext) - 2):
                p0, p1, p2, p3 = ext[q - 1], ext[q], ext[q + 1], ext[q + 2]
                for i in range(12):
                    t = i / 12.0
                    t2, t3 = t * t, t * t * t
                    uu = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
                    vv = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
                    pts.append(F.P(uu, vv))
            pts.append(F.P(*p[-1]))
        else:
            for q in range(len(p) - 1):
                a, b = p[q], p[q + 1]
                for i in range(12):
                    t = i / 12.0
                    pts.append(F.P(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
            pts.append(F.P(*p[-1]))
        if 'curl' in el:
            cu = el['curl']
            end = pts[-1]
            d = unit(sub(pts[-1], pts[-2]))
            n = (-d[1], d[0])
            dirn = cu['dir'] * F.mir
            rw = cu['r'] * F.B
            c = add(end, n, dirn * rw)
            self.ink.curls.append(c)
            ph0 = math.atan2(end[1] - c[1], end[0] - c[0])
            sw = math.radians(cu['sweep'])
            steps = max(10, int(cu['sweep'] / 11))
            for i in range(1, steps + 1):
                ph = ph0 + dirn * sw * i / steps
                pts.append((c[0] + rw * math.cos(ph), c[1] + rw * math.sin(ph)))
            if cu.get('tail'):
                d2 = unit(sub(pts[-1], pts[-2]))
                last = pts[-1]
                for i in range(1, 9):
                    pts.append(add(last, d2, cu['tail'] * F.L * i / 8))
        return pts

    def element(self, F, el, flags):
        t = el['t']
        fl = dict(flags)
        for f in ('hollow', 'smooth'):
            if el.get(f):
                fl[f] = True
        if t == 'cut':
            pts = self.cut_pts(F, el)
            head = not (self.open_head and el['p'][-1][0] >= 0.85 and 'curl' not in el)
            foot = 0.5 * F.H if (self.root_foot and el['p'][0][0] <= 0.08) else None
            self.stroke(F, pts, fl, el.get('k', 1.0), fill=el.get('fill', False), head=head, foot=foot)
        elif t == 'bar':
            self.stroke(F, [F.P(el['u'], el['v0'] + (el['v1'] - el['v0']) * i / 12.0) for i in range(13)], fl, el.get('k', 1.0))
        elif t == 'ringarc':
            rho = F.rin + el['u'] * F.L
            pts = [F.arc(rho, (el['v0'] + (el['v1'] - el['v0']) * i / 16.0) * F.mir * F.B / max(rho, 1.0)) for i in range(17)]
            self.stroke(F, pts, fl, el.get('k', 1.0))
        elif t == 'star':
            c = F.P(*el['c'])
            for q in range(5):
                d = rot(F.er, q * 2 * math.pi / 5)
                pts = [add(c, d, el['r'] * F.B * i / 8.0) for i in range(9)]
                hw = [F.H * 1.15 * (1 - i / 8.0) ** 0.8 for i in range(9)]
                if fl.get('hollow'):
                    L, R = edges_of(pts, hw)
                    self.ink.line(L + list(reversed(R)), 'e0')
                else:
                    self.ink.vcut(pts, hw)
        elif t == 'lens':
            c = F.P(*el['c'])
            if el.get('across'):
                L2 = el['len'] * F.B
                W = el['w'] * F.L
            else:
                L2 = el['len'] * F.L / 2
                W = el['w'] * F.B
            ro = math.radians(el.get('rot', 0)) * F.mir
            pts, pinch = [], []
            n = 20
            for i in range(n):
                a = 2 * math.pi * i / n
                x = math.cos(a) * L2
                y = math.sin(a) * W * abs(math.sin(a)) ** 0.25 * (1 - 0.35 * abs(math.cos(a)) ** 3)
                pinch.append(max(0.35, 0.42 * abs(y)))
                if el.get('across'):
                    pts.append((c[0] + y, c[1] + x * F.mir))
                else:
                    x, y = x * math.cos(ro) - y * math.sin(ro), x * math.sin(ro) + y * math.cos(ro)
                    pts.append((c[0] + x, c[1] + y * F.mir))
            self.groove(F, pts, fl, pinch=pinch, fill=el.get('fill', False))
        elif t == 'drop':
            c = F.P(*el['c'])
            L2 = el['len'] * F.L / 2
            W = el['w'] * F.B
            sgn = -1 if el.get('point', 'in') == 'in' else 1
            pts, pinch = [], []
            for i in range(20):
                a = 2 * math.pi * i / 20
                x = math.cos(a)
                y = math.sin(a) * (0.5 * (1 - sgn * x)) ** 0.9 * W
                pinch.append(max(0.35, 0.45 * abs(y)))
                pts.append((c[0] + x * L2, c[1] + y * F.mir))
            self.groove(F, pts, fl, pinch=pinch)
        elif t == 'square':
            c = F.P(*el['c'])
            h = el['s'] * F.B / 2
            corners = [(-h, -h), (h, -h), (h, h), (-h, h)]
            pts = []
            for q in range(4):
                a, b = corners[q], corners[(q + 1) % 4]
                for i in range(4):
                    pts.append((c[0] + a[0] + (b[0] - a[0]) * i / 4.0, c[1] + a[1] + (b[1] - a[1]) * i / 4.0))
            self.groove(F, pts, fl)
        elif t in ('wedge', 'tri'):
            tri = [F.P(*el['apex']), F.P(el['base'], -el['w']), F.P(el['base'], el['w'])] if t == 'wedge' else [F.P(*p) for p in el['p']]
            if fl.get('hollow'):
                self.ink.line(tri + [tri[0]], 'e0')
            else:
                self.ink.chip(tri)
        elif t == 'punch':
            c = F.P(*el['c'])
            r = max(0.9, el.get('r', 0.08) * F.B)
            tri = [add(c, (r * math.cos(a), r * math.sin(a) * F.mir)) for a in (math.pi / 2, math.pi / 2 + 2.094, math.pi / 2 + 4.189)]
            if fl.get('hollow'):
                self.ink.line(tri + [tri[0]], 'e0')
            else:
                self.ink.chip(tri)
        elif t == 'check':
            self.check(F, el)
        elif t == 'scar':
            self.scar(F, el)
        elif t == 'knot':
            self.knot(F, el, fl)
        elif t == 'cup':
            self.cup(F, el, fl)
        elif t == 'rootfoot':
            c = F.P(*el['c'])
            base = F.er if el['dir'] == 'out' else (-F.er[0], -F.er[1])
            for ang, ln, bow in ROOTFOOT:
                a0 = math.radians(ang) * F.mir
                pts, cur = [c], c
                for i in range(1, 7):
                    d = rot(base, a0 + math.radians(bow) * F.mir * i / 6.0)
                    cur = add(cur, d, ln * F.B / 6.0)
                    pts.append(cur)
                self.stroke(F, pts, fl, 0.6)
        else:
            raise GNError('unknown element type %r' % t)

    def check(self, F, el):
        n = 9
        left, right, mid = [], [], []
        for q in range(n + 1):
            u = el['u0'] + (el['u1'] - el['u0']) * q / n
            wv = el['w'] * (1 - q / float(n)) ** 0.9
            jv = self.rng.uni(-0.09, 0.09) if 0 < q < n else 0.0
            left.append(F.P(u, el['v'] - wv / 2 + jv))
            right.append(F.P(u, el['v'] + wv / 2 + jv))
            mid.append(F.P(u, el['v'] + jv + wv * 0.08))
        # both faces of the crack: whichever faces the light is lit where the sign is placed
        self.ink.voids.append(left + list(reversed(right)))
        d = unit(sub(left[-1], left[0]))
        nrm = (-d[1], d[0])
        self.ink.chips.append((mid + list(reversed(right)), (-nrm[0], -nrm[1])))
        self.ink.chips.append((mid + list(reversed(left)), nrm))
        self.ink.line(left, 'e1')

    def scar(self, F, el):
        u0, u1, w = (0.0 if self.root_foot else el['apex'][0]), el['base'], el['w']
        vv = lambda u: w * max(0.0, (u - u0) / (u1 - u0)) ** 0.85
        rows = 6
        us = [u0 + (u1 - u0) * (i / float(rows)) ** 0.8 for i in range(rows + 1)]
        L = [F.P(u0 + (u1 - u0) * i / 10.0, -vv(u0 + (u1 - u0) * i / 10.0)) for i in range(11)]
        R = [F.P(u0 + (u1 - u0) * i / 10.0, vv(u0 + (u1 - u0) * i / 10.0)) for i in range(11)]
        self.ink.voids.append(L + list(reversed(R)))
        self.ink.line(L, 'e2')
        self.ink.line(R, 'e2')
        for r_ in range(rows):
            ua, ub = us[r_], us[r_ + 1]
            ncell = 1 if r_ < 1 else (2 if r_ < 3 else 3)
            cuts = [0.0] + sorted(min(0.9, max(0.1, (c + 1) / float(ncell) + self.rng.uni(-0.12, 0.12))) for c in range(ncell - 1)) + [1.0]
            for c in range(ncell):
                f0, f1 = cuts[c], cuts[c + 1]
                va = lambda u, f: -vv(u) + 2 * vv(u) * f
                cell = [F.P(ua, va(ua, f0)), F.P(ub, va(ub, f0)), F.P(ub, va(ub, f1)), F.P(ua, va(ua, f1))]
                cx = sum(p[0] for p in cell) / 4.0
                cy = sum(p[1] for p in cell) / 4.0
                cell = [add(p, unit(sub((cx, cy), p)), 1.25) for p in cell]
                self.ink.char.append(cell)
        for sgn in (-1, 1):
            pts = [F.P(u1 - 0.1 + 0.12 * math.sin(a * math.pi / 2), sgn * (w + 0.1 - 0.42 * a)) for a in [i / 10.0 for i in range(11)]]
            self.stroke(F, pts, {}, 0.9)

    def knot(self, F, el, fl):
        c = F.P(*el['c'])
        rx = el['rx'] * F.B
        ru = el['ru'] * F.L
        pts, inner = [], []
        for i in range(20):
            a = 2 * math.pi * i / 20
            pts.append((c[0] + ru * math.cos(a), c[1] + rx * math.sin(a)))
            inner.append((c[0] + 0.42 * ru * math.cos(a), c[1] + 0.5 * rx * math.sin(a)))
        self.ink.knots.append((c, ru, rx))
        self.groove(F, pts, fl)
        self.ink.voids.append(inner)
        self.ink.line(inner, 'e3', closed=True)

    def cup(self, F, el, fl):
        c = F.P(*el['c'])
        r = el['r'] * F.B
        form = el.get('form', 'hold')
        if form == 'palm':
            pts = [add(add(c, F.et, r * math.sin(math.radians(-80 + 160 * i / 16.0)) * F.mir), F.er, -r * math.cos(math.radians(-80 + 160 * i / 16.0)) * 0.8) for i in range(17)]
            self.stroke(F, pts, fl)
            return
        for sgn in (-1, 1):
            pts = []
            for i in range(15):
                a = math.radians(-55 + 110 * i / 14.0)
                x = sgn * (r * math.cos(a) - 0.25 * r) if form == 'hold' else sgn * (1.25 * r - r * math.cos(a))
                pts.append(add(add(c, F.et, x), F.er, r * math.sin(a) * 0.9))
            self.stroke(F, pts, fl)

    def sign(self, F, tok, whole=None, fringe=(), kind_arc=None):
        """One copy of one token: its elements (hollow where a part leaves them), the entry-nick,
        bites, the causative chevron, and, on the copy that carries them, the fringe and kind-arc."""
        sg = SIGNS[tok.sign]
        base = {'hollow': tok.hollow, 'smooth': tok.smooth}
        for i, el in enumerate(sg['els']):
            fl = dict(base)
            if whole is not None and i not in whole:
                fl['hollow'] = True
            self.element(F, el, fl)
        um = umax(sg)
        if sg.get('nick'):
            a = F.P(um - 0.02, 0.30)
            b = F.P(um - 0.02 + 0.27 * F.B / max(F.L, 1), 0.64)
            self.stroke(F, [lerp(a, b, i / 4.0) for i in range(5)], base, 0.6)
        for q in range(min(tok.count, 4)):
            u = um - 0.08 - 0.14 * q
            self.ink.chip([F.P(u - 0.045, 0.30), F.P(u, 0.10), F.P(u + 0.045, 0.30)])
        for q in range(min(tok.ord, 4)):
            u = um - 0.08 - 0.14 * q
            self.ink.chip([F.P(u - 0.045, -0.30), F.P(u, -0.10), F.P(u + 0.045, -0.30)])
        if tok.caus:
            self.stroke(F, [F.P(0.12, -0.3), F.P(0.03, 0), F.P(0.12, 0.3)], {}, 0.6)
        if fringe:
            self.fringe(F, fringe)
        if kind_arc:
            rho = F.rin - 2.5
            span = kind_arc / max(rho, 1.0)
            pts = [F.arc(rho, -span + 2 * span * i / 16.0) for i in range(17)]
            self.stroke(F, pts, {}, 0.55)

    def fringe(self, F, fr):
        """v2 5.4: three stations round the sign, cut with the knife at 0.55 H."""
        k = 0.55
        hu = 1.0 / max(F.L, 1.0)
        pr = lambda u, v, r: self.punch(F.P(u, v), r * F.B)
        for f in fr:
            if f == 'all':
                self.stroke(F, [F.P(0.12 + 0.76 * i / 8.0, 1.19) for i in range(9)], {}, k)
            elif f == 'half':
                self.stroke(F, [F.P(0.12 + 0.34 * i / 6.0, 1.19) for i in range(7)], {}, k)
            elif f == 'few':
                pr(0.5, 1.22, 0.11)
            elif f == 'only':
                self.stroke(F, [F.P(0.36 + 0.28 * i / 5.0, -1.18) for i in range(6)], {}, k)
            elif f == 'more':
                for u, v in ((0.42, -1.16), (0.6, -1.32)):
                    pr(u, v, 0.1)
            elif f == 'most':
                for u, v in ((0.32, -1.14), (0.5, -1.27), (0.68, -1.4)):
                    pr(u, v, 0.1)
            elif f in ('again', 'still'):
                for du in ((-2.2, -4.2) if f == 'again' else (-3.0,)):
                    rho = F.rin + du
                    span = 0.28 * F.B / max(rho, 1.0)
                    self.stroke(F, [F.arc(rho, -span + 2 * span * i / 6.0) for i in range(7)], {}, k)
            elif f == 'last':
                self.punch(F.P(-3.4 * hu, 0), 0.11 * F.B)
            elif f == 'slow':
                pts = [F.P((-3.0 + 1.1 * math.sin(i / 10.0 * 2 * math.pi)) * hu, -0.3 + 0.6 * i / 10.0) for i in range(11)]
                self.stroke(F, pts, {}, k)
            elif f == 'gently':
                pts = [F.P((-1.6 - 2.4 * math.sin(math.pi * i / 10.0)) * hu, -0.3 + 0.6 * i / 10.0) for i in range(11)]
                self.stroke(F, pts, {}, k)

    def punch(self, c, r):
        r = max(r, 1.1)
        tri = [(c[0] + r * math.cos(a), c[1] + r * math.sin(a)) for a in (-math.pi / 2, math.pi / 6, 5 * math.pi / 6)]
        self.ink.chip(tri)


# ------------------------------------------------------------------------------------ symbols
def q_(v, step):
    return round(v / step) * step


class SymbolBook:
    """Every sign cut once, as a <symbol>, and placed with <use> (v2 11.6). A symbol is keyed by what
    changes its cut: the token, its part, its devices, and its size in its frame."""
    def __init__(self, pref):
        self.pref = pref
        self.syms = {}           # key -> (sid, Cuts)
        self.order = []
        self.used = set()

    def get(self, tok, L, B, H, rin, root_foot=False, fringe=(), kind_arc=None, whole=None):
        # sizes on a coarse grid (a sign is cut the same wherever it is the same size), the length
        # rounded down so it never outgrows its span; the ring's curvature matters only to a
        # sign with a ring-arc in it
        L = max(4.0, math.floor(L / 2.0) * 2.0) if L >= 8.0 else q_(L, 1.0)
        B, H = q_(B, 1.0), q_(H, 0.2)
        curved = kind_arc or any(el['t'] == 'ringarc' for el in SIGNS[tok.sign]['els']) or any(f in ('again', 'still') for f in fringe)
        rin_q = round(math.log(max(rin, 4.0)) / 0.06) if curved else 0
        rin = math.exp(rin_q * 0.06) if curved else 1e4
        key = (tok.sign, tok.part, tok.hollow, tok.smooth, tok.caus, tok.count, tok.ord, tok.q, root_foot,
               tuple(fringe), q_(kind_arc, 0.5) if kind_arc else 0, tuple(whole) if whole is not None else None,
               L, B, H, rin_q)
        if key in self.syms:
            return self.syms[key]
        cuts = Cuts()
        mk = SignMaker(cuts, Rng('sign/%s/%s' % (tok.sign, tok.part)), open_head=tok.q, root_foot=root_foot)
        F = LFrame(L, B, H, rin)
        mk.sign(F, tok, whole=whole, fringe=fringe, kind_arc=kind_arc)
        sid = '%s-s%d' % (self.pref, len(self.order))
        self.syms[key] = (sid, cuts)
        self.order.append(key)
        return self.syms[key]

    def svg(self):
        out = []
        for key in self.order:
            sid, cuts = self.syms[key]
            if sid in self.used:
                out.append(symbol_svg(sid, cuts))
        return ''.join(out)


def symbol_svg(sid, cuts):
    groups = {}
    for b, poly in cuts.facets(bucket_of):
        poly = simplify(poly, 0.18)
        if len(poly) >= 3:
            groups.setdefault(b, []).append(poly)
    body = []
    for b in sorted(groups):
        body.append('<path class="g2%s" d="%s"/>' % (BUCKET_CLS[b], ''.join(poly_d(p) for p in groups[b])))
    if cuts.flat:
        body.append('<path class="g2f" d="%s"/>' % ''.join(poly_d(p) for p in cuts.flat))
    if cuts.char:
        body.append('<path class="g2c" d="%s"/>' % ''.join(poly_d(p) for p in cuts.char))
    if cuts.voids:
        body.append('<path class="g2v" d="%s"/>' % ''.join(poly_d(p) for p in cuts.voids))
    lines = {}
    for pts, cls, closed in cuts.lines:
        lines.setdefault(cls, []).append(poly_d(pts, closed))
    for cls in sorted(lines):
        body.append('<path class="g2%s" fill="none" d="%s"/>' % (cls, ''.join(lines[cls])))
    return '<symbol id="%s" overflow="visible">%s</symbol>' % (sid, ''.join(body))


def tone_vars(A, tones=None):
    """The twelve bucket tones of one placement: each bucket's facing, turned by A, under the light."""
    a, b, c, d = A
    tones = tones or {'lit': '.97', 'mid': '.74', 'shade': '.48'}
    out = []
    for i in range(NBUCKET):
        ang = 2 * math.pi * i / NBUCKET
        f = (math.cos(ang), math.sin(ang))
        w = (a * f[0] + c * f[1], b * f[0] + d * f[1])
        out.append('--%s:%s' % (BUCKET_CLS[i], tones[tone_of(w)]))
    return ';'.join(out)


def mat_txt(A, t):
    a, b, c, d = A
    f4 = lambda v: ('%.4f' % v).rstrip('0').rstrip('.').replace('-0.', '-.').replace('0.', '.', 1) if abs(v) >= 1e-5 else '0'
    f1 = lambda v: ('%.2f' % v).rstrip('0').rstrip('.') if abs(v) >= 0.005 else '0'
    return 'matrix(%s %s %s %s %s %s)' % (f4(a), f4(b), f4(c), f4(d), f1(t[0]), f1(t[1]))


# =================================================================================================
#  A ROUND: marks placed as symbols, pockets, bark
# =================================================================================================
def expand_lig(lig):
    """A ligature's parts, each with its span along the file (modifier inward, head outward), its
    scale, lean and whether it is a ligature part (0.7 breadth, finer knife: v2 4.5)."""
    if lig.composite:
        # v1 10.8, the pair at the root (the sliver): HOLD cupped at the foot; the pair from one foot,
        # the round loop leaning clockwise and larger, the square loop leaning further away; the
        # name folded in the round loop's curl, as a seed is folded in a fruit
        out = []
        for p in lig.composite:
            if p['kind'] == 'tok':
                out.append({'tok': p['tok'], 'u': (0.0, 0.12), 'scale': 0.75, 'lean': 0.0, 'lig': False})
            elif p['kind'] == 'pair':
                out.append({'tok': p['a'], 'u': (0.12, 1.0), 'scale': 1.15, 'lean': 16.0 if p['a'].lean >= 0 else -16.0, 'lig': False, 'host': p['a'].sign})
                out.append({'tok': p['b'], 'u': (0.12, 0.84), 'scale': 0.78, 'lean': -26.0 if p['b'].lean <= 0 else 26.0, 'lig': False, 'host': p['b'].sign})
            else:
                out.append({'tok': p['tok'], 'u': None, 'scale': 0.2, 'lean': 0.0, 'lig': False, 'within': p['host'], 'size': 0.1})
        return out
    n = len(lig.toks)
    if n == 1:
        return [{'tok': lig.toks[0], 'u': (0.0, 1.0), 'scale': 1.0, 'lean': lig.toks[0].lean, 'lig': False}]
    return [{'tok': lig.toks[0], 'u': (0.0, 0.48), 'scale': 1.0, 'lean': lig.toks[0].lean, 'lig': True},
            {'tok': lig.toks[1], 'u': (0.52, 1.0), 'scale': 1.0, 'lean': lig.toks[1].lean, 'lig': True}]


class Round:
    def __init__(self, md, state='whole', stage0=False, plate=None, run_tone='mid'):
        self.md = md
        self.state = state
        self.stage0 = stage0
        self.plate = plate
        self.run_tone = run_tone
        self.lay = lay = Layout(md, plate)
        self.K = md.K
        self.seed = md.seed
        self.axis = math.radians(md.axis) if md.axis is not None else lay.axis_seeded
        self.war = md.pith == 'war'
        self.wood = md.wood
        self.stone = md.wood == 'stone'
        if lay.joined:
            sep = 1.32 * lay.R[lay.kj]
            n = md.npith
            self.piths = [add((0.0, 0.0), er(self.axis + (16.0 * i / n) * SLOT), sep) for i in range(n)]
            self.locals = [LocalField(lay, p, i) for i, p in enumerate(self.piths)]
            self.main = SharedField(lay, (0.0, 0.0), self.piths)
        else:
            self.piths = [(0.0, 0.0)]
            self.locals = []
            self.main = SimpleField(lay, (0.0, 0.0))
        self.pref = 'g%07x' % (fnv1a(print_gn(md) + state + str(stage0) + str(plate)) & 0xfffffff)
        self.book = SymbolBook(self.pref)
        self.places = []          # [(group of (sid, A, t)), A for its tones, what]
        self.direct = Cuts()      # world cuts drawn directly: smoothed marks
        self.rcuts = Cuts()       # the runners, cut in their own tone
        self.recs = {}            # (pith, file, cell, ring, year) -> mark record
        self.pockets = {}
        self.warnings = []
        self.hair = []            # hairline paths (rays, memory), world points
        self.ends = []            # runner ends, for the decode checks

    # ---------------------------------------------------------------- helpers
    def field_for(self, pith, ring):
        if self.locals and pith is not None and ring <= self.lay.kj:
            return self.locals[pith]
        return self.main

    def th_file(self, f):
        return self.axis + f * SLOT

    def visible(self, k):
        return self.plate is None or k == self.plate

    def band(self, fld, k, y, th, lo=3.0, hi=5.5):
        a, b = self.lay.year_r[(k, y)]
        hi += self.lay.top_room.get((k, y), 0.0)
        return fld.yr(k, a + lo, th), fld.yr(k, b - hi, th)

    def outer(self, th):
        """The bark's outer contour. No mark may cross it."""
        g = self.lay
        v = self.main.base(self.K, th) + g.bark_w
        v += sum(a * math.sin(m * th + p) for m, a, p in g.bark_n)
        for c, wdt, depth in g.notches:
            d = wrap(th - c)
            if abs(d) < wdt:
                v -= depth * g.bark_w * (1 - abs(d) / wdt) ** 1.4
        for c, span, bulge in g.plates:
            d = (th - c) % (2 * math.pi)
            if d < span:
                v += bulge * g.bark_w * math.sin(math.pi * d / span) ** 0.6
        return v

    # ---------------------------------------------------------------- marks
    def build_marks(self):
        md = self.md
        if self.stage0:
            return
        order = []
        for r in md.rings:
            for yr in r.years:
                for it in sorted(yr.items, key=lambda it: ((it.pith if isinstance(it, Mark) and it.pith is not None else -1), it.file % 16, (it.cell or 0) if isinstance(it, Mark) else 0)):
                    order.append(it)
        idx = 0
        for it in order:
            if isinstance(it, Mark):
                if self.plate is None or it.ring == self.plate:
                    self.place_mark(it, idx)
                idx += 1
        for it in order:
            if isinstance(it, Pocket) and (self.plate is None or it.ring == self.plate):
                self.place_pocket(it)
        if self.bark_ok():
            # a name or seal is cut on a sound plate of bark: no fissure under it (v1 10.5)
            g = self.lay
            if md.bark:
                g.notches = [(c, w_, dp) for (c, w_, dp) in g.notches
                             if all(abs(wrap(c - self.th_file(f))) > 0.16 for f, _ in md.bark)]
                g.make_plates()
            for i, (f, lig) in enumerate(md.bark):
                self.place_bark(f, lig, i)

    def bark_ok(self):
        return self.plate is None

    def slot_count(self, mk):
        yr = self.md.rings[mk.ring - 1].years[mk.year - 1]
        return sum(1 for it in yr.items if isinstance(it, Mark) and it.file % 16 == mk.file % 16 and it.pith == mk.pith)

    def place_mark(self, mk, idx):
        lay = self.lay
        k, y = mk.ring, mk.year
        fld = self.field_for(mk.pith, k)
        c = 1 if mk.root else lay.cells[k]
        n_here = self.slot_count(mk)
        j = (mk.cell or 1) - 1
        off = 0.0 if n_here <= 1 else (j - (n_here - 1) / 2.0) / c
        rng = Rng(self.seed + '/mark/%s/%d/%g/%d' % (mk.pith, k, mk.file, idx))
        th = self.th_file(mk.file + off)
        if not mk.root:
            th += math.radians(rng.uni(-2.0, 2.0) / c)
        toks = mk.lig.toks or [p['tok'] if 'tok' in p else p['a'] for p in mk.lig.composite]
        foot_fr = any(f in FOOT_FRINGE for t in toks for f in t.fringe)
        kind = any(t.kind for t in toks)
        if mk.root:
            rin = PITH_R * 0.55
            rout = fld.base(1, th) - 4.0
        else:
            rin, rout = self.band(fld, k, y, th, 3.0 + (4.5 if foot_fr else 0.0) + (3.0 if kind else 0.0), 5.5)
            sp = mk.lig.span()
            if sp:
                ks, ys = sp
                ys = min(ys, lay.nyears(ks)) if ks <= self.K else 1
                if ks <= self.K:
                    rout = self.band(fld, ks, ys, th)[1]
            if any(t.q for t in toks):
                a, b = lay.year_r[(k, y)]
                rout = fld.yr(k, b - 0.5, th)
        mid = 0.5 * (rin + rout)
        if mk.root:
            B0 = min(56.0, 0.95 * mid * 0.589)
            H0 = max(3.2, min(7.0, H_ROOT * B0))
        else:
            B0 = max(7.0, min(24.0, 0.5 * mid * SLOT / c - 3.0))
            H0 = max(1.8, min(6.5, H_MARK * B0))
        rec = {'mk': mk, 'th': th, 'rin': rin, 'rout': rout, 'B': B0, 'field': fld, 'k': k, 'y': y,
               'polys': [], 'kind': 'mark'}
        self.recs[(mk.pith, mk.file, mk.cell, k, y)] = rec
        self.cut_lig(rec, mk.lig, fld, th, rin, rout, B0, H0, root=mk.root, rng=rng)
        head_tok = toks[-1]
        # a plural's head is three heads abreast: a runner springs from, or lands on, the one on
        # its own side (v2 6.1), never hooking over its neighbour
        rec['x3off'] = 0.78 * B0 / 1.3 * (0.7 if len(toks) > 1 else 1.0) if head_tok.x3 else 0.0
        self.head_foot(rec)
        # the grain yields round the mark (v2 4.6): the ring lines either side bow away from it
        h = 0.5 * (rout - rin)
        for kk, sgn, ref in ((k - 1, -1.0, rin), (k, 1.0, rout)):
            if kk < 0 or (kk == 0 and not mk.root and False):
                continue
            if kk == 0:
                continue
            lineb = fld.base(kk, th)
            D = max(0.0, abs(lineb - ref))
            amp = sgn * 1.2 * math.exp(-(D / (h + 6.0)) ** 2)
            if abs(amp) > 0.05:
                fld.bumps.setdefault(kk, []).append((th, amp, 0.9 * B0, 'g'))
        return rec

    def cut_lig(self, rec, lig, fld, th, rin, rout, B0, H0, root=False, rng=None, knife=1.0, visible=True):
        """Cut a ligature's parts on one file: symbols placed with <use>, or cut directly when smoothed."""
        curls = []
        parts = expand_lig(lig)
        polys = []
        placed = []
        for pi, p in enumerate(parts):
            tok = p['tok']
            sc = p['scale']
            if p.get('within'):
                host = next((q for q in placed if q['sign'] == p['within']), None)
                if not host or not host['curls']:
                    continue
                cw = host['curls'][0]
                thc, rho = fld.polar(cw)
                span = p['size'] * (rout - rin)
                pa, pb = rho - span / 2, rho + span / 2
                th_use = thc
                lean = 0.0
            else:
                a, b = p['u']
                if tok.half:
                    a, b = a + 0.25 * (b - a), a + 0.75 * (b - a)
                pa, pb = rin + a * (rout - rin), rin + b * (rout - rin)
                th_use = th
                lean = p['lean']
            if tok.half:
                sc *= 0.5
            B = B0 * sc * (0.7 if p['lig'] else 1.0) / (1.3 if tok.x3 else 1.0)
            H = H0 * (0.8 if p['lig'] else 1.0) * knife
            if sc < 1:
                H = max(0.45 if sc < 0.5 else 1.0, H * sc)
            mir = -1.0 if tok.not_ else 1.0
            copies = [(0.0, 1.0)] if not tok.x3 else [(-0.78, 0.52), (0.0, 0.52), (0.78, 0.52)]
            whole = PARTS[tok.sign][tok.part] if tok.part else None
            lr = math.radians(lean)
            e_r, e_t = rot(er(th_use), lr), rot(et(th_use), lr)
            A = (e_r[0], e_r[1], mir * e_t[0], mir * e_t[1])
            group = []
            pc = {'sign': tok.sign, 'curls': []}
            # the gate rule (v2 4.5): nothing of a sign stands above its span, so the year's top 5.5
            # units stay free for the runners; a sign whose star, cup or nick would reach past its
            # head is cut a little shorter along the file
            L = pb - pa
            if not root:
                bs_m = copies[len(copies) // 2][1]
                Bm = B * bs_m
                Hm = max(0.4 if sc < 0.5 else 1.6, H * bs_m) if bs_m < 1 else H
                for _ in range(4):
                    _, cm = self.book.get(tok, L, Bm, Hm, pa, root_foot=root, fringe=tuple(tok.fringe),
                                          kind_arc=1.2 * B if tok.kind else None, whole=whole)
                    hi = max(pt[0] for pts, c_ in cm.outlines() for pt in pts)
                    over = hi - (pb - pa)
                    if over <= 0.3 or L < 6.0:
                        break
                    L = max(6.0, L - over - 0.2)
            for ci, (voff, bs) in enumerate(copies):
                Bc = B * bs
                Hc = max(0.4 if sc < 0.5 else 1.6, H * bs) if bs < 1 else H
                middle = (ci == len(copies) // 2)
                fr = tuple(tok.fringe) if middle else ()
                ka = 1.2 * B if (middle and tok.kind) else None
                sid, cuts = self.book.get(tok, L, Bc, Hc, pa, root_foot=root, fringe=fr, kind_arc=ka, whole=whole)
                if visible:
                    self.book.used.add(sid)
                base = add(fld.pt(pa, th_use), et(th_use), voff * B)
                wc = cuts.transformed(A, base)
                polys += wc.outlines()
                for c_, ru, rx in wc.knots:
                    kth, krho = fld.polar(c_)
                    fld.knots.append(Knot(kth, krho, ru, rx))
                pc['curls'] += wc.curls
                if any(cls in ('sL', 'sR') for _, cls, _ in cuts.lines):
                    self.direct.extend(wc)
                    self.smooth_lines(wc)
                else:
                    group.append((sid, A, base))
            placed.append(pc)
            if group and visible:
                self.places.append((group, A))
        rec['polys'] += polys
        return polys

    def smooth_lines(self, wc):
        """A smoothed cut: one lit edge and one shade edge, by how it lies to the light (v1 3.11)."""
        ls = [l for l in wc.lines if l[1] in ('sL', 'sR')]
        self.direct.lines = [l for l in self.direct.lines if l[1] not in ('sL', 'sR')]
        for i in range(0, len(ls) - 1, 2):
            L, R = ls[i][0], ls[i + 1][0]
            lit_first = dot(unit(sub(L[len(L) // 2], R[len(R) // 2])), LIGHT) < 0
            a, b = (L, R) if lit_first else (R, L)
            self.direct.lines.append((a, 'smL', ls[i][2]))
            self.direct.lines.append((b, 'smS', ls[i][2]))

    def place_bark(self, f, lig, idx):
        th = self.th_file(f)
        rin = self.main.base(self.K, th) + 3.5
        ext = 1.45 * 30.0 / max(rin, 1.0)
        lo = min(self.outer(th + ext * (i / 6.0 - 1)) for i in range(13))
        rout = lo - 4.5
        mid = 0.5 * (rin + rout)
        B0 = min(24.0, 0.8 * mid * SLOT, 0.8 * (rout - rin))
        H0 = max(1.8, min(6.5, H_MARK * B0))
        rec = {'mk': None, 'th': th, 'rin': rin, 'rout': rout, 'B': B0, 'field': self.main, 'k': self.K + 1,
               'y': 1, 'polys': [], 'kind': 'bark'}
        self.recs[('bark', f, None, self.K + 1, 1)] = rec
        self.cut_lig(rec, lig, self.main, th, rin, rout, B0, H0, rng=Rng(self.seed + '/bark/%d' % idx))

    # ---------------------------------------------------------------- pockets (v2 8)
    def place_pocket(self, pk):
        k, y = pk.ring, pk.year
        fld = self.main
        s0, s1 = pk.s0, pk.s1
        n = int((s1 - s0) % 16)
        if n + 1 > 6:
            self.warnings.append('pocket %s spans %d files (at most six, v2 8)' % (pk.pid, n + 1))
        t0 = self.th_file(s0 - 0.5)
        t1 = t0 + (n + 1) * SLOT
        a, b = self.lay.year_r[(k, y)]
        rec = {'pk': pk, 'k': k, 'y': y, 't0': t0, 't1': t1, 'items': [], 'polys': []}
        self.pockets[pk.pid] = rec
        N = 72
        up, lo, mids = [], [], []
        for i in range(N + 1):
            q = i / float(N)
            th = t0 + (t1 - t0) * q
            ra, rb = fld.yr(k, a + 3.0, th), fld.yr(k, b - 5.5 + 3.0, th)
            m = 0.5 * (ra + rb)
            h = 0.5 * (rb - ra) * math.sin(math.pi * q) ** 0.85
            up.append((th, m + h))
            lo.append((th, m - h))
            mids.append((th, m, 0.5 * (rb - ra)))
        rec['up'], rec['lo'], rec['mid'] = up, lo, mids
        rec['outline'] = [fld.pt(r_, t_) for t_, r_ in up] + [fld.pt(r_, t_) for t_, r_ in reversed(lo)]
        rec['polys'] = [(rec['outline'], True)]
        # its contents, cut with the finer knife, clockwise along the midline (v2 8)
        items = pk.items
        nC = max(1, len(items))
        for j, it in enumerate(items):
            q = (j + 0.5) / nC
            th = t0 + (t1 - t0) * q
            _, m, hh = mids[int(round(q * N))]
            h = hh * math.sin(math.pi * q) ** 0.85
            arc = (t1 - t0) / nC * m
            B = max(4.0, min(16.0, 0.36 * arc, 0.9 * h))
            rin, rout = m - 0.72 * h, m + 0.72 * h
            if isinstance(it, Pocket):
                continue
            H = max(0.9, 0.62 * H_MARK * B * 1.6)
            irec = {'th': th, 'rin': rin, 'rout': rout, 'B': B, 'polys': [], 'q': q, 'n': j + 1, 'm': m, 'h': h}
            if getattr(it, 'band', None):
                # v2 21 A1: a band on an item, or a band alone (the band as a thing: the sky, the sea)
                rec.setdefault('bands', []).append((it.band, j / float(nC), (j + 1) / float(nC), bool(it.toks)))
            if it.toks or it.composite:
                self.cut_lig(irec, it, fld, th, rin, rout, B, H, knife=1.0, visible=self.visible(k))
            rec['items'].append(irec)
            rec['polys'] += irec['polys']
        return rec

    def pocket_bands(self, pr):
        """The bands of a pocket's items (v2 21 A1), drawn in the item's own slot of the pocket: a band
        on an item lies behind its sign; a band alone fills the slot, the band as a thing."""
        out = []
        if not pr.get('bands') or not self.visible(pr['k']):
            return out
        fld = self.main
        mids = pr['mid']
        N = len(mids) - 1
        for name, qa, qb, on_item in pr['bands']:
            n = 18
            qs = [qa + (qb - qa) * (0.08 + 0.84 * i / n) for i in range(n + 1)]
            geo = []
            for q in qs:
                th, m, hh = mids[int(round(q * N))]
                h = hh * math.sin(math.pi * q) ** 0.85
                fade = math.sin(math.pi * (q - qa) / (qb - qa)) ** 0.5
                geo.append((th, m, h, fade))
            if name == 'MIST':
                top = [fld.pt(m + 0.62 * h * f, th) for th, m, h, f in geo]
                bot = [fld.pt(m - 0.62 * h * f, th) for th, m, h, f in geo]
                with prec(2):
                    out.append('<path fill-opacity="%s" d="%s"/>' % (OP['mist'] * (1.0 if on_item else 1.6), smooth_d(top + bot[::-1])))
            elif name == 'STILL':
                ds = ''.join(smooth_d([fld.pt(m + off * (0.5 * h if on_item else 1.0), th) for th, m, h, f in geo], closed=False)
                             for off in (-1.5, 1.5))
                with prec(2):
                    out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".7" d="%s"/>' % (OP['still'], ds))
            elif name == 'WATER':
                pts = [fld.pt(m + 0.3 * h * math.sin(2 * math.pi * i / 6.0) * f, th) for i, (th, m, h, f) in enumerate(geo)]
                with prec(2):
                    out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".9" d="%s"/>' % (OP['water'], smooth_d(pts, closed=False)))
            elif name == 'WHITE':
                pts = [fld.pt(m, th) for th, m, h, f in geo]
                with prec(2):
                    out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="%s" stroke-dasharray=".8 2.2" d="%s"/>'
                               % (OP['frost'], _num(_q(max(1.0, 0.9 * geo[len(geo) // 2][2]))), smooth_d(pts, closed=False)))
            elif name == 'DARK':
                top = [fld.pt(m + 0.9 * h, th) for th, m, h, f in geo]
                bot = [fld.pt(m - 0.9 * h, th) for th, m, h, f in geo]
                with prec(2):
                    out.append('<path fill-opacity="%s" d="%s"/>' % (OP['dark'] * 1.6, smooth_d(top + bot[::-1])))
            else:   # DREAD: a scorched slit along the slot
                top = [fld.pt(m + 0.25 * h * f, th) for th, m, h, f in geo]
                bot = [fld.pt(m - 0.25 * h * f, th) for th, m, h, f in geo]
                self.direct.voids.append(top + bot[::-1])
                self.direct.lines.append((top, 'dT', False))
                self.direct.lines.append((bot, 'dB', False))
        return out

    def pocket_runs(self):
        """Runners among a pocket's items (v2 21 A2), cut with the pocket's finer knife: from the one
        item's head across the gap to the next item, a to-runner landing by its head and a then-runner
        by its foot. Nothing crosses the pocket's border."""
        md = self.md
        for rid, pid, i, role, j in md.pk_runs:
            pr = self.pockets.get(pid)
            if pr is None or not self.visible(pr['k']):
                continue
            its = pr['items']
            if not (1 <= i <= len(its) and 1 <= j <= len(its)) or i == j:
                self.warnings.append('pocket runner %s: no item %s.%d or %s.%d' % (rid, pid, i, pid, j))
                continue
            a, b = its[i - 1], its[j - 1]
            fld = self.main
            mids = pr['mid']
            N = len(mids) - 1
            dq = 1.0 if b['q'] > a['q'] else -1.0
            qa = a['q'] + dq * (0.5 * a['B'] + 1.2) / max(1.0, (pr['t1'] - pr['t0']) * a['m'])
            qb = b['q'] - dq * (0.5 * b['B'] + 2.2) / max(1.0, (pr['t1'] - pr['t0']) * b['m'])
            fa, fb = 0.16, (0.16 if role != 'then' else -0.3)
            pts = []
            n = 14
            for s_ in range(n + 1):
                u = s_ / float(n)
                q = qa + (qb - qa) * u
                th, m, hh = mids[int(round(min(1.0, max(0.0, q)) * N))]
                h = hh * math.sin(math.pi * min(1.0, max(0.0, q))) ** 0.85
                fr = fa + (fb - fa) * (3 * u * u - 2 * u * u * u) + 0.1 * math.sin(math.pi * u)
                pts.append(fld.pt(m + fr * h, th))
            key = 'pk:' + rid
            self.lines[key] = dedupe(pts, 0.3)
            self.info[key] = (Runner(rid, None, role, [('pocket-item', pid, j)]), 'pk', None, dq, None)
            self.fine.add(key)


# =================================================================================================
#  RUNNERS (v2 6-7): grown through the wood, crossing over and under
# =================================================================================================
class Obstacles:
    """A spatial hash of every mark's ink (and every pocket), for clearance tests."""
    H = 6.0

    def __init__(self):
        self.segs = {}

    def add_poly(self, pts, closed, owner):
        n = len(pts)
        m = n if closed else n - 1
        for i in range(m):
            a, b = pts[i], pts[(i + 1) % n]
            self.add_seg(a, b, owner)
        if n == 1:
            self.add_seg(pts[0], pts[0], owner)

    def add_seg(self, a, b, owner):
        H = self.H
        x0, x1 = int(math.floor(min(a[0], b[0]) / H)), int(math.floor(max(a[0], b[0]) / H))
        y0, y1 = int(math.floor(min(a[1], b[1]) / H)), int(math.floor(max(a[1], b[1]) / H))
        for cx in range(x0, x1 + 1):
            for cy in range(y0, y1 + 1):
                self.segs.setdefault((cx, cy), []).append((a, b, owner))

    def dist(self, p, allow=None, reach=1):
        H = self.H
        cx, cy = int(math.floor(p[0] / H)), int(math.floor(p[1] / H))
        best = 1e9
        for dx in range(-reach, reach + 1):
            for dy in range(-reach, reach + 1):
                for a, b, owner in self.segs.get((cx + dx, cy + dy), ()):
                    if allow and owner in allow:
                        c, r = allow[owner]
                        if math.hypot(p[0] - c[0], p[1] - c[1]) < r:
                            continue
                    d = seg_dist(p, a, b)
                    if d < best:
                        best = d
        return best


class RunnerLines:
    """The points of the runners grown so far: runners keep apart and cross when they must."""
    H = 4.0

    def __init__(self):
        self.pts = {}

    def add(self, pts, rid):
        for p in resample_even(pts, 1.2):
            self.pts.setdefault((int(p[0] // self.H), int(p[1] // self.H)), []).append((p, rid))

    def near(self, p, skip=()):
        cx, cy = int(p[0] // self.H), int(p[1] // self.H)
        best = 1e9
        for dx in (-1, 0, 1, 2, -2):
            for dy in (-1, 0, 1, 2, -2):
                for q, rid in self.pts.get((cx + dx, cy + dy), ()):
                    if rid in skip:
                        continue
                    d = math.hypot(p[0] - q[0], p[1] - q[1])
                    if d < best:
                        best = d
        return best


TRIM = {'in': 4.6, 'for': 10.2, 'bc': 5.6, 'as': 4.4}


def side_of(curve, p):
    """Which side of a line a point lies on: the sign of the turn from the line's tangent at its
    nearest point to the point."""
    i = min(range(len(curve)), key=lambda q: (curve[q][0] - p[0]) ** 2 + (curve[q][1] - p[1]) ** 2)
    a, b = curve[max(i - 1, 0)], curve[min(i + 1, len(curve) - 1)]
    t = sub(b, a)
    v = sub(p, curve[i])
    return 1 if t[0] * v[1] - t[1] * v[0] >= 0 else -1


def trim_by(pts, length):
    """Cut a line back by an arc length from its end (the terminal is grown in that room)."""
    s = arclen(pts)
    keep = s[-1] - length
    if keep < 6.0:
        return pts
    out = [p for p, si in zip(pts, s) if si <= keep]
    i = len(out)
    if i < len(pts):
        a, b = pts[i - 1], pts[i]
        out.append(lerp(a, b, (keep - s[i - 1]) / max(s[i] - s[i - 1], 1e-9)))
    return out


def gauss_smooth(pts, sigma, ramp=None):
    """Smooth an evenly sampled line (1 unit apart) with a Gaussian of sigma units, ends held. With
    ramp, sigma grows from 1.5 at each end by ramp per unit, so a runner threads its marks closely
    and flows freely between them."""
    n = len(pts)
    if n < 5:
        return pts
    out = []
    cache = {}
    for i in range(n):
        sg = sigma if ramp is None else min(sigma, 1.5 + ramp * min(i, n - 1 - i))
        sg = max(0.5, sg)
        r = min(int(3 * sg), i, n - 1 - i)       # the window shrinks at the ends, so they stay put
        key = (round(sg, 1), r)
        w = cache.get(key)
        if w is None:
            w = [math.exp(-0.5 * (k / sg) ** 2) for k in range(-r, r + 1)]
            cache[key] = w
        sx = sy = sw = 0.0
        for k in range(-r, r + 1):
            ww = w[k + r]
            sx += ww * pts[i + k][0]
            sy += ww * pts[i + k][1]
            sw += ww
        out.append((sx / sw, sy / sw))
    return out


def meander(pts, seed, amp=0.55):
    """A runner is grown, not ruled: a slight seeded wander across its line (carries nothing)."""
    if len(pts) < 4:
        return pts
    s = arclen(pts)
    r = Rng(seed)
    ph, lam = r.uni(0, 6.283), r.uni(26, 38)
    out = []
    n = len(pts)
    for i in range(n):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, n - 1)]
        d = unit(sub(b, a))
        nn = (-d[1], d[0])
        env = min(1.0, s[i] / 6.0, (s[-1] - s[i]) / 6.0)
        out.append(add(pts[i], nn, amp * env * math.sin(2 * math.pi * s[i] / lam + ph)))
    return out


def intersections(A, B):
    """Every proper crossing of two polylines: (point, arc length on A, on B, sin of the angle)."""
    if len(A) < 2 or len(B) < 2:
        return []
    ax = [p[0] for p in A]; ay = [p[1] for p in A]
    bx = [p[0] for p in B]; by = [p[1] for p in B]
    if max(ax) < min(bx) or max(bx) < min(ax) or max(ay) < min(by) or max(by) < min(ay):
        return []
    sa, sb = arclen(A), arclen(B)
    res = []

    def blocks(P, n=8):
        out = []
        for i in range(0, len(P) - 1, n):
            seg = P[i:i + n + 1]
            xs = [p[0] for p in seg]
            ys = [p[1] for p in seg]
            out.append((i, min(len(P) - 1, i + n), min(xs), max(xs), min(ys), max(ys)))
        return out
    for (i0, i1, x0, x1, y0, y1) in blocks(A):
        for (j0, j1, u0, u1, v0, v1) in blocks(B):
            if x1 < u0 or u1 < x0 or y1 < v0 or v1 < y0:
                continue
            for i in range(i0, i1):
                p, p2 = A[i], A[i + 1]
                r_ = sub(p2, p)
                la = math.hypot(*r_)
                if la < 1e-9:
                    continue
                for j in range(j0, j1):
                    q, q2 = B[j], B[j + 1]
                    s_ = sub(q2, q)
                    lb = math.hypot(*s_)
                    den = r_[0] * s_[1] - r_[1] * s_[0]
                    if lb < 1e-9 or abs(den) < 1e-12:
                        continue
                    t = ((q[0] - p[0]) * s_[1] - (q[1] - p[1]) * s_[0]) / den
                    u = ((q[0] - p[0]) * r_[1] - (q[1] - p[1]) * r_[0]) / den
                    if 0 <= t < 1 and 0 <= u < 1:
                        x = add(p, r_, t)
                        ta = sa[i] + t * (sa[i + 1] - sa[i])
                        tb = sb[j] + u * (sb[j + 1] - sb[j])
                        if any(math.hypot(x[0] - r0[0][0], x[1] - r0[0][1]) < 1.2 for r0 in res):
                            continue
                        res.append((x, ta, tb, abs(den) / (la * lb)))
    return res


class RunnerMixin:
    # ---------------------------------------------------------------- ends
    def find_rec(self, a):
        pith, f, cell, k, y = a
        rec = self.recs.get((pith, f, cell, k, y))
        if rec:
            return rec
        for key, r in self.recs.items():
            if key[0] == pith and key[1] == f and key[3] == k and key[4] == y and (cell is None or key[2] in (None, cell)):
                return r
        mk = self.md.mark_at(a)
        if mk is not None:
            return self.recs.get((mk.pith, mk.file, mk.cell, mk.ring, mk.year))
        return None

    def head_foot(self, rec):
        """Where the cut really ends: its head and its foot along its file (a half-size, fitted or
        leaning sign is shorter than its span)."""
        fld, th, B = rec['field'], rec['th'], rec['B']
        top, bot = rec['rin'], rec['rout']
        for pts, closed in rec['polys']:
            for p in pts:
                t_, r_ = fld.polar(p)
                if abs(wrap(t_ - th)) * r_ <= 1.2 * B + 2.0:
                    top = max(top, r_)
                    bot = min(bot, r_)
        rec['head'] = min(top, rec['rout'] + 1.0)
        rec['foot'] = bot

    def head_pt(self, rec, dirn, lift=3.0, side=0.25):
        fld = rec['field']
        hd = rec.get('head', rec['rout'])
        off = rec.get('x3off', 0.0) + side * rec['B'] * (0.52 if rec.get('x3off') else 1.0)
        th = rec['th'] + dirn * off / max(hd, 1.0)
        return fld.pt(hd + lift, th)

    def target_geo(self, rn, tg, src, dirn):
        """Where a runner lands, by its role (v2 6.1): (goal point, approach point or None, end kind,
        owner key, the mark record or None)."""
        role = rn.role
        if tg[0] == 'mark':
            tr = self.find_rec(tg[1])
            if tr is None:
                raise GNError('runner %s: no mark at %s' % (rn.rid, addr_text(tg[1])))
            fld = tr['field']
            key = self.rec_key(tr)
            th = tr['th']
            if role == 'then':
                ft = tr.get('foot', tr['rin'])
                g = fld.pt(ft - 3.4, th)
                return g, fld.pt(ft - 9.0, th - dirn * 2.0 / max(ft, 1)), 'foot', key, tr
            if role == 'with':
                side = -dirn
                midr = 0.5 * (tr['rin'] + tr['rout'])
                g = fld.pt(midr, th + side * (tr['B'] + 3.5) / max(midr, 1.0))
                return g, None, 'flank', key, tr
            # every other role lands on the head, a knife-width short; its terminal is grown back along
            # the runner's last stretch (TRIM), so the end never stands on the mark
            hd = tr.get('head', tr['rout'])
            thh = th - dirn * (tr.get('x3off', 0.0) + 0.08 * tr['B']) / max(hd, 1.0)
            g = fld.pt(hd + 3.0, thh)
            return g, None, 'head', key, tr
        if tg[0] == 'file':
            fld = src['field']
            k, y = src['k'], src['y']
            th = self.th_file(tg[1])
            a, b = self.lay.year_r[(k, y)]
            rho = fld.yr(k, 0.5 * (a + 3.0 + b - 5.5), th)
            return fld.pt(rho, th), fld.pt(rho + 6.0, th - dirn * 5.0 / max(rho, 1.0)), 'place', None, None
        if tg[0] == 'pocket':
            pr = self.pockets.get(tg[1])
            if pr is None:
                raise GNError('runner %s: no pocket %s' % (rn.rid, tg[1]))
            return pr['mouth_in'], pr['mouth_out'], 'pocket', ('P', tg[1]), None
        if tg[0] == 'blind':
            return self.blind_spot(src, dirn) + (None,)
        raise GNError('runner %s: bad target' % rn.rid)

    def rec_key(self, rec):
        for key, r in self.recs.items():
            if r is rec:
                return key
        return None

    def blind_spot(self, src, dirn):
        """The blind lands on nothing: empty wood at least 6 units from any mark, in the source's own
        year, on the nearest file clockwise (then counter-clockwise) where the empty cup fits."""
        fld = src['field']
        k, y = src['k'], src['y']
        a, b = self.lay.year_r[(k, y)]
        base_f = (src['mk'].file if src.get('mk') else 0)
        for dd in (1, -1, 2, -2, 3, -3, 4, -4):
            th = self.th_file(base_f + dd)
            rho = fld.yr(k, 0.5 * (a + b), th)
            p = fld.pt(rho, th)
            if self.obst.dist(p, reach=2) > 12.0 and self.rl.near(p) > 6.0:
                return p, fld.pt(rho + 3.0, th - (1 if dd > 0 else -1) * 6.0 / rho), 'blind', None
        th = self.th_file(base_f + 1.5)
        rho = fld.yr(k, 0.5 * (a + b), th)
        self.warnings.append('a blind runner found no empty wood 6 units clear')
        return fld.pt(rho, th), None, 'blind', None

    # ---------------------------------------------------------------- the router
    # The lattice is ring-aligned: its rows are fractions across each ring, so a row follows the
    # ring's own shape (a round is eccentric, and its lines are not circles), and a runner's room
    # above the heads is a row or two all the way along.
    def qpos(self, fld, p):
        """(theta, q) of a point: q = k - 1 + its fraction across ring k."""
        th, rho = fld.polar(p)
        k = 1
        while k < self.K and rho > fld.base(k, th):
            k += 1
        a, b = fld.base(k - 1, th), fld.base(k, th)
        return th, (k - 1) + (rho - a) / max(b - a, 1e-6)

    def qpt(self, fld, th, q):
        k = min(self.K, max(1, int(math.floor(q)) + 1))
        fr = q - (k - 1)
        a, b = fld.base(k - 1, th), fld.base(k, th)
        return fld.pt(a + fr * (b - a), th)

    def astar(self, fld, start, goal, klo, khi, allow, clear=CLEAR, grow=1.0, skip_runners=(), avoid=None):
        """Grow a runner from start to goal through the empty wood (v2 6.2): along the grain is cheap,
        across it dear; marks are walls; other runners are dear to run beside and cheap to cross; no
        step crosses a ring line inward; only the rings between the ends may be entered."""
        lay = self.lay
        th0, q0 = self.qpos(fld, start)
        th1, q1 = self.qpos(fld, goal)
        r0, r1 = fld.polar(start)[1], fld.polar(goal)[1]
        dth = wrap(th1 - th0)
        if abs(abs(dth) - math.pi) < 1e-6:
            dth = math.pi
        rref = max(30.0, 0.5 * (r0 + r1))
        self._rref = rref
        dt = CELLSTEP / rref
        sgn = 1.0 if dth >= 0 else -1.0
        nth = int(abs(dth) / dt) + 1
        pad_i = int(90.0 * grow / CELLSTEP)
        lo_i, hi_i = -pad_i, nth + pad_i
        if (hi_i - lo_i) * dt > 2 * math.pi - 0.05:
            extra = int((2 * math.pi - 0.05) / dt) - nth
            lo_i, hi_i = -extra // 2, nth + extra // 2
        rows = []
        for k in range(max(1, klo), min(khi, self.K) + 1):
            n = max(3, int(round((lay.R[k] - lay.R[k - 1]) / CELLSTEP)))
            for r_ in range(n):
                rows.append((k, (r_ + 0.5) / n))
        nr = len(rows)
        first_row = {}
        for j, (k, fr) in enumerate(rows):
            first_row.setdefault(k, (j, sum(1 for kk, _ in rows if kk == k)))
        bounds_cache = {}
        node = {}
        piths = self.piths if fld is self.main else [fld.O]
        lam, ph, amp = self._drift
        rules = self.md.rules

        def bounds(i):
            b_ = bounds_cache.get(i)
            if b_ is None:
                th = th0 + sgn * i * dt
                b_ = [fld.base(k, th) for k in range(0, self.K + 1)]
                bounds_cache[i] = b_
            return b_

        def info(i, j):
            key = (i, j)
            v = node.get(key)
            if v is not None:
                return v
            th = th0 + sgn * i * dt
            k, fr = rows[j]
            bb = bounds(i)
            a, b = bb[k - 1], bb[k]
            rho = a + fr * (b - a)
            p = fld.pt(rho, th)
            ok = True
            if any(math.hypot(p[0] - q[0], p[1] - q[1]) < 12.0 for q in piths):
                ok = False
            if ok and k == self.K and rho > b - 3.0:
                ok = False
            if ok and self.locals and fld is self.main and k == lay.kj + 1 and rho < a + 3.0:
                ok = False
            cost = 0.0
            if ok:
                wid = max(b - a, 1.0)
                dl = min(fr, 1.0 - fr) * wid
                if k - 1 in rules:
                    dl = min(dl, abs(rho - a - 5.0))
                # a runner keeps off the ring lines, so that it never reads as another ring (v2 12.4)
                if dl < 7.0:
                    cost += 1.6 * (1.0 - dl / 7.0) ** 2
                # and it wanders, as a root does: a seeded slow drift across the grain within its ring
                pref = 0.5 + amp * math.sin(2 * math.pi * i * CELLSTEP / lam + ph)
                cost += 0.8 * ((fr - pref) / 0.5) ** 2
                if self.obst.dist(p, allow) <= clear:
                    ok = False
                elif avoid is not None and avoid.near(p) < 3.0 and min(math.hypot(p[0] - start[0], p[1] - start[1]), math.hypot(p[0] - goal[0], p[1] - goal[1])) > 10.0:
                    ok = False
            nrun = 0.0
            if ok and self.rl.pts:
                nr_ = self.rl.near(p, skip_runners)
                nrun = 6.0 if nr_ < RUN_CLEAR else (1.5 if nr_ < 6.0 else 0.0)
            v = (ok, k, p, rho, cost, nrun)
            node[key] = v
            return v

        def cell(th, q):
            i = int(round(wrap(th - th0) * sgn / dt))
            k = min(max(int(math.floor(q)) + 1, max(1, klo)), min(khi, self.K))
            j0, n = first_row[k]
            fr = q - (k - 1)
            return i, j0 + min(n - 1, max(0, int(fr * n)))

        si, sj = cell(th0, q0)
        gi, gj = cell(th1, q1)
        if abs(dth) >= math.pi - 1e-6:
            gi = int(round(abs(dth) / dt))
        gpt = goal
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        openq = [(0.0, 0.0, si, sj, -1)]
        best = {(si, sj): 0.0}
        came = {}
        found = None
        steps = 0
        while openq:
            f, gc, i, j, mv = heapq.heappop(openq)
            if gc > best.get((i, j), 1e18) + 1e-9:
                continue
            if abs(i - gi) <= 1 and abs(j - gj) <= 1:
                found = (i, j)
                break
            steps += 1
            if steps > 400000:
                break
            ok0, k0, p0, rho0, c0, _ = info(i, j)
            for mi, (di, dj) in enumerate(moves):
                ni, nj = i + di, j + dj
                if ni < lo_i or ni > hi_i or nj < 0 or nj >= nr:
                    continue
                ok, kk, p, rho, cst, nrun = info(ni, nj)
                if not ok:
                    near_end = (abs(ni - gi) <= 2 and abs(nj - gj) <= 2) or (abs(ni - si) <= 2 and abs(nj - sj) <= 2)
                    if not near_end:
                        continue
                if kk < k0:
                    continue            # never inward across a ring line
                step = math.hypot(p[0] - p0[0], p[1] - p0[1]) or 1e-6
                cost = step * (1.0 + (GRAIN - 1.0) * min(1.0, abs(rho - rho0) / step) + cst) + nrun
                if kk != k0:
                    cost += 5.0
                if mv >= 0 and mi != mv:
                    cost += 0.35
                ng = gc + cost
                if ng < best.get((ni, nj), 1e18):
                    best[(ni, nj)] = ng
                    came[(ni, nj)] = (i, j, mi)
                    h = math.hypot(p[0] - gpt[0], p[1] - gpt[1])
                    heapq.heappush(openq, (ng + 1.1 * h, ng, ni, nj, mi))
        if not found:
            return None
        path = [found]
        while path[-1] in came:
            i, j, _ = came[path[-1]]
            path.append((i, j))
        path.reverse()
        pol = []
        for i, j in path:
            k, fr = rows[j]
            pol.append((th0 + sgn * i * dt, (k - 1) + fr))
        pol[0] = (th0, q0)
        pol[-1] = (th1, q1)
        return pol, (lambda th, q: self._free(fld, th, q, allow, clear, klo, khi, avoid, (start, goal)))

    def _free(self, fld, th, q, allow, clear, klo, khi, avoid, ends=()):
        k = min(self.K, max(1, int(math.floor(q)) + 1))
        if not (klo <= k <= khi):
            return False, k
        p = self.qpt(fld, th, q)
        if self.obst.dist(p, allow) <= clear:
            return False, k
        if avoid is not None and avoid.near(p) < 3.0 and all(math.hypot(p[0] - e[0], p[1] - e[1]) > 10.0 for e in ends):
            return False, k
        return True, k

    def pull(self, fld, pol, free):
        """String-pulling in (theta, q) (v2 6.2 step 6), keeping the shape the cost gave (its drift
        and its distance from the lines) but not the lattice's steps: a point goes only where the
        run without it stays within 1.8 units of the path, clear of the marks, never inward."""
        if len(pol) < 3:
            return pol
        rref = 300.0
        wq = 40.0

        def clear_run(a, b):
            L = math.hypot(wrap(b[0] - a[0]) * rref, (b[1] - a[1]) * wq)
            n = max(2, int(L / 1.5))
            k_prev = None
            for s_ in range(0, n + 1):
                t = s_ / float(n)
                th = a[0] + wrap(b[0] - a[0]) * t
                q = a[1] + (b[1] - a[1]) * t
                ok, k = free(th, q)
                if not ok and 0 < s_ < n:
                    return False
                if k_prev is not None and k < k_prev:
                    return False
                k_prev = k
            return True
        th_un = [pol[0][0]]
        for t, q in pol[1:]:
            th_un.append(th_un[-1] + wrap(t - th_un[-1]))
        XY = [(t * rref, q * wq) for t, (_, q) in zip(th_un, pol)]

        def dev(i, j, q):
            (ax, ay), (bx, by), (px, py) = XY[i], XY[j], XY[q]
            dx, dy = bx - ax, by - ay
            L = math.hypot(dx, dy) or 1e-9
            return abs((px - ax) * dy - (py - ay) * dx) / L
        keepi = {0, len(pol) - 1}
        stack = [(0, len(pol) - 1)]
        while stack:
            i, j = stack.pop()
            if j - i < 2:
                continue
            q, dmax = max(((q, dev(i, j, q)) for q in range(i + 1, j)), key=lambda t: t[1])
            if dmax > 1.8 or not clear_run(pol[i], pol[j]):
                if dmax <= 1.8:
                    q = (i + j) // 2
                keepi.add(q)
                stack.append((i, q))
                stack.append((q, j))
        return [pol[i] for i in sorted(keepi)]

    def smooth_route(self, fld, base_q, allow, cl, klo, khi, rid):
        """Smooth the lattice path hard where the wood is open and gently where it threads between
        marks: a Gaussian in (theta, q), blended back toward the lattice path wherever it would come
        too near a mark or leave its rings."""
        n = len(base_q)
        S = gauss_smooth(base_q, 18.0, 0.45)
        w = [1.0] * n

        def bad_at(qs):
            pts = [self.qpt(fld, x / self.q_rref, y / self.q_w) for x, y in qs]
            s_ = arclen(pts)
            bad = []
            kprev = 0
            for i, p in enumerate(pts):
                if s_[i] < 5 or s_[-1] - s_[i] < 5:
                    continue
                th, rho = fld.polar(p)
                k = 1
                while k <= self.K and rho > fld.base(k, th):
                    k += 1
                if self.obst.dist(p, allow) < cl - 0.6 or k < kprev or not (klo <= k <= khi):
                    bad.append(i)
                kprev = max(kprev, k)
            return pts, bad
        for it in range(7):
            ws = gauss_smooth([(float(i), wi) for i, wi in enumerate(w)], 5.0)
            wv = [max(0.0, min(1.0, v)) for _, v in ws] if it else w
            qs = [(b[0] + wv[i] * (S[i][0] - b[0]), b[1] + wv[i] * (S[i][1] - b[1])) for i, b in enumerate(base_q)]
            pts, bad = bad_at(qs)
            if not bad:
                pts = resample_even(pts, 1.4)
                return meander(pts, self.seed + '/runner/%s/meander' % rid)
            for i in bad:
                for j in range(max(0, i - 10 - 3 * it), min(n, i + 11 + 3 * it)):
                    w[j] = 0.0
        return None

    def q_curve(self, pol):
        """The lattice path in (theta, q) as an evenly sampled line in units (arc along, ring-width
        across), ready to be smoothed there: a Gaussian in (theta, q) keeps the drift and loses
        the lattice's steps, and never cuts a chord (v2 6.2)."""
        rref = self.q_rref = max(30.0, getattr(self, '_rref', 300.0))
        self.q_w = 40.0
        th_un = [pol[0][0]]
        for t, q in pol[1:]:
            th_un.append(th_un[-1] + wrap(t - th_un[-1]))
        XY = [(t * rref, q * self.q_w) for t, (_, q) in zip(th_un, pol)]
        return resample_even(dedupe(XY, 0.05), 1.0)

    def polar_line(self, fld, keep, step=1.0):
        """The kept points joined by straight runs in (theta, q): each a gentle drift across the
        grain, following the rings' own shape, never a chord (v2 6.2); a Gaussian then rounds it."""
        out = []
        for (t0, q0), (t1, q1) in zip(keep, keep[1:]):
            dt_ = wrap(t1 - t0)
            a, b = self.qpt(fld, t0, q0), self.qpt(fld, t1, q1)
            L = max(math.hypot(b[0] - a[0], b[1] - a[1]), abs(dt_) * fld.polar(a)[1])
            n = max(1, int(L / step))
            for s_ in range(n):
                f = s_ / float(n)
                out.append(self.qpt(fld, t0 + dt_ * f, q0 + (q1 - q0) * f))
        out.append(self.qpt(fld, keep[-1][0], keep[-1][1]))
        return out

    def route(self, fld, a, b, klo, khi, allow, clear=CLEAR, rid='', skip=(), avoid=None):
        """A* then string-pulling then the curve; wider windows and then less room before giving up."""
        rd_ = Rng(self.seed + '/runner/%s/drift' % rid)
        self._drift = (rd_.uni(70.0, 130.0), rd_.uni(0, 2 * math.pi), rd_.uni(0.26, 0.36))
        for grow, cl in ((1.0, clear), (2.2, clear), (4.0, clear), (4.0, max(2.6, clear - 0.6)), (6.0, 2.2)):
            res = self.astar(fld, a, b, klo, khi, allow, cl, grow, skip, avoid)
            if res is None:
                continue
            pol, free = res
            base_q = self.q_curve(pol)
            pts = self.smooth_route(fld, base_q, allow, cl, klo, khi, rid)
            if pts is not None:
                if cl < clear:
                    self.warnings.append('runner %s: grown with only %.1f units of room' % (rid, cl))
                return pts
            # the string-pulled path is clear by construction: drift-straight runs between kept points
            keep = self.pull(fld, pol, free)
            pts = resample_even(dedupe(self.polar_line(fld, keep), 0.2), 1.0)
            return meander(resample_even(gauss_smooth(pts, 1.5), 1.4), self.seed + '/runner/%s/meander' % rid, 0.3)
        return None

    # ---------------------------------------------------------------- growing them all
    def draw_runners(self):
        md = self.md
        self.obst = Obstacles()
        for key, rec in self.recs.items():
            for pts, closed in rec['polys']:
                self.obst.add_poly(pts, closed, key)
        for pid, pr in self.pockets.items():
            self.obst.add_poly(pr['outline'], True, ('P', pid))
        self.rl = RunnerLines()
        self.lines = {}
        self.info = {}
        if not md.runners:
            return
        order = sorted(md.runners, key=lambda r: runner_key(md, r))
        self.canon = {rn.rid: i for i, rn in enumerate(order)}
        laps = {o: u for o, u in md.laps}
        braid_of = {}
        for bid, strands, pat in md.braids:
            for j, s in enumerate(strands):
                braid_of[s] = (bid, j, strands, pat)
        seq = list(order)
        for ov, un in md.laps:
            io = next((i for i, r in enumerate(seq) if r.rid == ov), None)
            iu = next((i for i, r in enumerate(seq) if r.rid == un), None)
            if io is not None and iu is not None and iu > io:
                seq.insert(io, seq.pop(iu))
        # pockets decide their mouths from the runner that governs them
        for rn in md.runners:
            for tg in rn.tgts:
                if tg[0] == 'pocket' and tg[1] in self.pockets:
                    src = self.find_rec(rn.src)
                    self.pocket_mouth(self.pockets[tg[1]], src)
        for pid, pr in self.pockets.items():
            if 'mouth_in' not in pr:
                self.pocket_mouth(pr, None)
        self.stubs = {}
        self.tags = []
        for rn in seq:
            if self.plate is not None:
                ks, kt = rn.src[3], self.target_ring(rn)
                if ks != self.plate and kt != self.plate:
                    continue
                if ks != self.plate or kt != self.plate:
                    try:
                        self.stub(rn, ks, kt)
                    except GNError as e:
                        self.warnings.append(str(e))
                    continue
            if rn.rid in braid_of and braid_of[rn.rid][1] > 0:
                continue
            if any(t[0] == 'bind' for t in rn.tgts):
                continue
            try:
                self.grow(rn, laps.get(rn.rid), braid_of.get(rn.rid))
            except GNError as e:
                self.warnings.append(str(e))
        for bid, strands, pat in md.braids:
            if strands[0] in self.lines:
                self.braid(bid, strands, pat)
        for kid, strands, out in md.binds:
            self.bind(kid, strands, out)
        self.crossings()
        self.fine = set()
        if md.pk_runs:
            self.pocket_runs()
        total = sum(arclen(p)[-1] for p in self.lines.values())
        self.runner_silhouette = self.plate is None and not getattr(self, 'facets', False) and total > 40000.0
        for rid in self.lines:
            self.cut_runner(rid)
        for pr in self.pockets.values():
            self.pocket_border(pr)

    def target_ring(self, rn):
        tg = rn.tgts[0]
        if tg[0] == 'mark':
            return tg[1][3]
        if tg[0] == 'pocket':
            pk = self.md.pocket(tg[1])
            return pk.ring if pk else rn.src[3]
        if tg[0] == 'bind':
            site = bind_site_year(self.md, tg[1], next((st for kid, st, o in self.md.binds if kid == tg[1]), []))
            return site[0] if site else rn.src[3]
        return rn.src[3]

    def stub(self, rn, ks, kt):
        """On a ring plate, a runner to or from another ring is drawn to the plate's edge, a stub cut
        off by the plate's own outline; Seren's margin carries its tag (v2 11.5)."""
        K = self.plate
        fld = self.main
        tg = rn.tgts[0]
        if ks == K:
            src = self.find_rec(rn.src)
            if src is None:
                return
            th_t = self.th_file(tg[1][1] if tg[0] == 'mark' else src['mk'].file)
            dirn = 1.0 if wrap(th_t - src['th']) >= 0 else -1.0
            node = self.head_pt(src, dirn, lift=-0.6, side=0.06)
            start = self.head_pt(src, dirn, lift=3.0)
            edge = self.qpt(fld, th_t, K - 1 + 0.9)
            allow = {self.rec_key(src): (node, 14.0)}
            path = self.route(fld, start, edge, K, K, allow, CLEAR, rn.rid) or [start, edge]
            ext = [fld.pt(fld.base(K, th_t) + d, th_t) for d in (1.5, 5.0, 9.0, 13.5)]
            self.lines[rn.rid] = dedupe([node] + path + ext, 0.3)
            self.info[rn.rid] = (rn, 'stub', None, dirn, tg)
            self.stubs[rn.rid] = 'out'
            self.tags.append((fld.pt(fld.base(K, th_t) + 22.0, th_t), '→ r%d' % kt))
        else:
            th_s = self.th_file(rn.src[1])
            dummy = {'k': K, 'y': 1, 'th': th_s, 'field': fld, 'mk': None, 'B': 10.0, 'rin': fld.base(K - 1, th_s),
                     'rout': fld.base(K - 1, th_s)}
            tr = self.find_rec(tg[1]) if tg[0] == 'mark' else None
            dirn = 1.0 if (tr is None or wrap(tr['th'] - th_s) >= 0) else -1.0
            goal, approach, end, tkey, tr = self.target_geo(rn, tg, dummy, dirn)
            s0 = fld.pt(fld.base(K - 1, th_s) - 13.5, th_s)
            s1 = fld.pt(fld.base(K - 1, th_s) + 3.0, th_s)
            allow = {tkey: (goal, 16.0)} if tkey else {}
            path = self.route(fld, s1, approach or goal, K, K, allow, CLEAR, rn.rid) or [s1, goal]
            if approach is not None:
                path = path + [lerp(approach, goal, q / 4.0) for q in range(1, 5)]
            full = [s0, lerp(s0, s1, 0.33), lerp(s0, s1, 0.66)] + path
            if end == 'head' and TRIM.get(rn.role):
                full = trim_by(full, TRIM[rn.role])
            self.lines[rn.rid] = dedupe(full, 0.3)
            self.info[rn.rid] = (rn, end, tr, dirn, tg)
            self.stubs[rn.rid] = 'in'
            self.tags.append((fld.pt(fld.base(K - 1, th_s) - 22.0, th_s), 'from r%d' % ks))
        self.rl.add(self.lines[rn.rid], rn.rid)

    def grow(self, rn, thwarts=None, braid=None):
        src = self.find_rec(rn.src)
        if src is None:
            raise GNError('runner %s: no mark at %s' % (rn.rid, addr_text(rn.src)))
        fld = src['field']
        tg0 = rn.tgts[0]
        # which way it runs: the short way to its target
        if tg0[0] == 'mark':
            tr = self.find_rec(tg0[1])
            tth = tr['th'] if tr else src['th']
        elif tg0[0] == 'file':
            tth = self.th_file(tg0[1])
        elif tg0[0] == 'pocket':
            tth = self.pockets[tg0[1]]['tip']
        else:
            tth = src['th'] + 0.1
        d = wrap(tth - src['th'])
        dirn = 1.0 if d >= -1e-9 else -1.0
        node = self.head_pt(src, dirn, lift=-0.6, side=0.06)
        start = self.head_pt(src, dirn, lift=3.0)
        skey = self.rec_key(src)
        paths = []
        shoot_from = None
        for ti, tg in enumerate(rn.tgts):
            goal, approach, end, tkey, tr = self.target_geo(rn, tg, src, dirn)
            klo = src['k']
            khi = max(src['k'], tr['k'] if tr else src['k'])
            if tg[0] == 'pocket':
                khi = max(khi, self.pockets[tg[1]]['k'])
            if khi < klo:
                self.warnings.append('runner %s runs inward, to an earlier ring' % rn.rid)
                klo, khi = khi, klo
            allow = {}
            if skey:
                allow[skey] = (node, 14.0)
            if tkey:
                allow[tkey] = (goal, 16.0)
            clear = CLEAR + (5.0 if braid else 0.0)
            a = start if shoot_from is None else shoot_from
            b = approach or goal
            if thwarts and thwarts in self.lines:
                # a declared break crosses square, exactly once, near the thwarted runner's middle
                # (v2 7.1): the nearest point to the middle with free wood 6 units either side
                un = self.lines[thwarts]
                s = arclen(un)
                cands = sorted(range(len(un)), key=lambda q: abs(s[q] - 0.5 * s[-1]))
                sides = None
                for i in cands:
                    if not (0.2 * s[-1] < s[i] < 0.8 * s[-1]):
                        continue
                    wp = un[i]
                    dd = unit(sub(un[min(i + 3, len(un) - 1)], un[max(i - 3, 0)]))
                    nn = (-dd[1], dd[0])
                    ok = True
                    pair = []
                    for sg in (6.0, -6.0):
                        w_ = add(wp, nn, sg)
                        k_ = self.qpos(fld, w_)
                        kk = int(math.floor(k_[1])) + 1
                        if not (klo <= kk <= khi) or self.obst.dist(w_, allow) <= CLEAR + 0.4:
                            ok = False
                            break
                        pair.append(w_)
                    if ok:
                        # cross once: approach from the side away from the target, and leave on the
                        # target's side of the thwarted line
                        sb = side_of(un, b)
                        sides = pair if side_of(un, pair[1]) == sb else [pair[1], pair[0]]
                        break
                if sides is None:
                    self.warnings.append('break %s ⊳ %s: no room to cross square' % (rn.rid, thwarts))
                    i = cands[0]
                    wp = un[i]
                    dd = unit(sub(un[min(i + 3, len(un) - 1)], un[max(i - 3, 0)]))
                    nn = (-dd[1], dd[0])
                    sides = sorted([add(wp, nn, 6.0), add(wp, nn, -6.0)], key=lambda q: math.hypot(q[0] - a[0], q[1] - a[1]))
                av = RunnerLines()
                av.add(un, thwarts)
                l1 = self.route(fld, a, sides[0], klo, khi, allow, clear, rn.rid + 'a', avoid=av)
                l2 = self.route(fld, sides[1], b, klo, khi, allow, clear, rn.rid + 'b', avoid=av)
                if l1 and l2:
                    path = l1 + [lerp(sides[0], sides[1], q / 6.0) for q in range(1, 6)] + l2
                else:
                    self.warnings.append('break %s ⊳ %s: its legs found no way' % (rn.rid, thwarts))
                    path = self.route(fld, a, b, klo, khi, allow, clear, rn.rid)
            else:
                path = self.route(fld, a, b, klo, khi, allow, clear, rn.rid)
                if path is None and braid:
                    path = self.route(fld, a, b, klo, khi, allow, CLEAR, rn.rid)
            if path is None:
                self.warnings.append('runner %s: no way through the wood; drawn straight' % rn.rid)
                path = [a, b]
            if approach is not None:
                path = path + [lerp(approach, goal, q / 4.0) for q in range(1, 5)]
            full = dedupe(([node] if shoot_from is None else [shoot_from]) + path, 0.3)
            if end == 'head' and TRIM.get(rn.role):
                full = trim_by(full, TRIM[rn.role])
            key = rn.rid + ('' if ti == 0 else ':%d' % ti)
            self.lines[key] = full
            self.info[key] = (rn, end, tr, dirn, tg)
            self.rl.add(full, rn.rid)
            if ti == 0 and len(rn.tgts) > 1:
                # a split runner forks once (v2 6.1): the other shoots spring from one point of the first
                sl = arclen(full)
                q = min(range(len(full)), key=lambda q: abs(sl[q] - 0.45 * sl[-1]))
                shoot_from = full[q]
                start = shoot_from

    # ---------------------------------------------------------------- braids (v2 7.2)
    def braid(self, bid, strands, pat):
        md = self.md
        rns = {r.rid: r for r in md.runners}
        a = strands[0]
        cord = self.lines[a]
        N = len(pat.rstrip('!'))
        s = arclen(cord)
        tot = s[-1]
        pitch = 12.0
        L = (N + 1) * pitch
        if L > tot - 12.0:
            pitch = max(5.0, (tot - 12.0) / (N + 1))
            L = (N + 1) * pitch
            self.warnings.append('braid %s: its cord is short; pitch %.1f' % (bid, pitch))
        s0 = 0.5 * tot - 0.5 * L
        s1 = s0 + L
        n = len(cord)
        normals = []
        for i in range(n):
            q0, q1 = cord[max(i - 1, 0)], cord[min(i + 1, n - 1)]
            d = unit(sub(q1, q0))
            normals.append((-d[1], d[0]))
        ns = len(strands)
        offs = [[] for _ in strands]
        cross_s = []
        if ns == 2:
            for i in range(n):
                if s0 <= s[i] <= s1:
                    q = (s[i] - s0) / L
                    env = min(1.0, q / 0.1, (1 - q) / 0.1)
                    w = 2.2 * (1 - env) + env * 2.9 * math.sin(math.pi * (N + 1) * q)
                else:
                    w = 2.2
                offs[0].append(w)
                offs[1].append(-w)
            cross_s = [s0 + L * m / (N + 1.0) for m in range(1, N + 1)]
            pairs = [(0, 1)] * N
        else:
            lane = [-2.6, 0.0, 2.6]
            pos = [0, 1, 2]            # strand j's lane index
            steps = []
            for m in range(N):
                side = 0 if m % 2 == 0 else 2
                x = pos.index(side)
                y = pos.index(1)
                steps.append((x, y))
                pos[x], pos[y] = 1, side
            pairs = steps
            for i in range(n):
                cur = [0, 1, 2]
                val = [lane[c] for c in cur]
                if s[i] >= s0:
                    m = int((s[i] - s0) // pitch)
                    t = ((s[i] - s0) % pitch) / pitch
                    cur = [0, 1, 2]
                    for mm in range(min(m, N)):
                        x, y = steps[mm]
                        cur[x], cur[y] = cur[y], cur[x]
                    val = [lane[c] for c in cur]
                    if m < N:
                        x, y = steps[m]
                        e = t * t * (3 - 2 * t)
                        val[x] = lane[cur[x]] + (lane[cur[y]] - lane[cur[x]]) * e
                        val[y] = lane[cur[y]] + (lane[cur[x]] - lane[cur[y]]) * e
                for j in range(3):
                    offs[j].append(val[j])
            cross_s = [s0 + pitch * (m + 0.5) for m in range(N)]
        new = {}
        for j, sid in enumerate(strands):
            pts = [add(cord[i], normals[i], offs[j][i]) for i in range(n)]
            if j == 0:
                new[sid] = pts
                continue
            rn = rns[sid]
            ra = rns[a]
            mutual = (rn.src == (ra.tgts[0][1] if ra.tgts[0][0] == 'mark' else None)) and rn.tgts[0][0] == 'mark' and rn.tgts[0][1] == ra.src
            if mutual or ns == 2:
                new[sid] = list(reversed(pts)) if mutual else pts
                src = self.find_rec(rn.src)
                tg = rn.tgts[0]
                tr = self.find_rec(tg[1]) if tg[0] == 'mark' else None
                self.info[sid] = (rn, 'head', tr, 1.0, tg)
            else:
                new[sid] = pts
                self.info[sid] = (rn, 'head', self.find_rec(rn.tgts[0][1]) if rn.tgts[0][0] == 'mark' else None, 1.0, rn.tgts[0])
        for sid, pts in new.items():
            # an end that would stand on its mark stops a knife-width short of it
            self.lines[sid] = self.trim_end(pts, sid)
            self.rl.add(self.lines[sid], sid)
        self.braids_geo = getattr(self, 'braids_geo', {})
        self.braids_geo[bid] = {'strands': strands, 'pat': pat, 'cord': cord, 's': cross_s, 'pairs': pairs, 'N': N}

    def trim_end(self, pts, rid):
        rn, end, tr, dirn, tg = self.info.get(rid, (None, None, None, None, None))
        if tr is None:
            return pts
        polys = tr['polys']
        i = len(pts) - 1
        while i > 4 and poly_dist(pts[i], polys) < 3.0:
            i -= 1
        return pts[:i + 1]

    # ---------------------------------------------------------------- binds (v2 7.3)
    def bind(self, kid, strands, out):
        md = self.md
        rns = {r.rid: r for r in md.runners}
        srcs = [self.find_rec(rns[s].src) for s in strands if s in rns]
        if len(srcs) < 2 or any(s is None for s in srcs):
            self.warnings.append('bind %s: its strands are missing' % kid)
            return
        fld = srcs[0]['field']
        th_site = math.atan2(sum(math.sin(s['th']) for s in srcs), sum(math.cos(s['th']) for s in srcs))
        outer = max(srcs, key=lambda s: (s['k'], s['y']))
        k, y = outer['k'], outer['y']
        a, b = self.lay.year_r[(k, y)]
        rho = fld.yr(k, 0.5 * (a + b), th_site)
        best = None
        for dd in [0, 1, -1, 2, -2, 3, -3, 4, -4, 6, -6, 8, -8]:
            th = th_site + dd * 4.0 / rho
            p = fld.pt(rho, th)
            if self.obst.dist(p, reach=2) > 13.0:
                best = th
                break
        if best is None:
            best = th_site
            self.warnings.append('bind %s: no free site' % kid)
        th_site = best
        site = fld.pt(rho, th_site)
        ex, ey = et(th_site), er(th_site)
        W = lambda x, y_: add(add(site, ex, x), ey, y_)
        order = sorted(range(len(strands)), key=lambda i: wrap(srcs[i]['th'] - th_site))
        xs, ys = strands[order[0]], strands[order[-1]]
        geo = {'site': site, 'ex': ex, 'ey': ey, 'x': xs, 'y': ys}
        for sid, sgn in ((xs, 1.0), (ys, -1.0)):
            rn = rns[sid]
            src = self.find_rec(rn.src)
            dirn = 1.0 if wrap(th_site - src['th']) >= 0 else -1.0
            node = self.head_pt(src, dirn, lift=-0.6)
            start = self.head_pt(src, dirn, lift=3.0)
            entry = W(-sgn * 13.0, -sgn * 4.0)
            allow = {self.rec_key(src): (node, 14.0)}
            path = self.route(fld, start, entry, src['k'], k, allow, CLEAR, rn.rid) or [start, entry]
            lock = []
            for i in range(1, 11):
                lock.append(W(-sgn * 13.0 + sgn * 17.0 * i / 10.0, -sgn * 4.0))
            for i in range(1, 13):
                ph = -math.pi / 2 + math.pi * i / 12.0
                lock.append(W(sgn * (4.0 + 3.0 * math.cos(ph)), sgn * (-1.0 + 3.0 * math.sin(ph))))
            for i in range(1, 12):
                lock.append(W(sgn * (4.0 - 13.0 * i / 11.0), sgn * 2.0))
            self.lines[sid] = dedupe([node] + path + lock, 0.3)
            self.info[sid] = (rn, 'bind', None, dirn, ('bind', kid))
            self.rl.add(self.lines[sid], sid)
        if out:
            role, addr = out
            tr = self.find_rec(addr)
            if tr:
                oid = kid + ':out'
                start = W(0.0, 8.5)
                orn = Runner(oid, None, role, [('mark', addr)])
                goal, approach, end, tkey, _ = self.target_geo(orn, ('mark', addr), outer, 1.0 if wrap(tr['th'] - th_site) >= 0 else -1.0)
                allow = {tkey: (goal, 16.0)} if tkey else {}
                path = self.route(fld, start, approach or goal, k, max(k, tr['k']), allow, CLEAR, oid) or [start, goal]
                if approach is not None:
                    path = path + [lerp(approach, goal, q / 4.0) for q in range(1, 5)]
                self.lines[oid] = [W(0.0, 5.2)] + path
                self.info[oid] = (orn, end, tr, 1.0, ('mark', addr))
                self.canon[oid] = len(self.canon) + 1
        self.binds_geo = getattr(self, 'binds_geo', {})
        self.binds_geo[kid] = geo

    # ---------------------------------------------------------------- pockets' mouths and borders
    def pocket_mouth(self, pr, src):
        k, y = pr['k'], pr['y']
        fld = self.main
        a, b = self.lay.year_r[(k, y)]
        tc = 0.5 * (pr['t0'] + pr['t1'])
        tip = pr['t0'] if (src is None or wrap(src['th'] - tc) < 0) else pr['t1']
        inward = 1.0 if tip == pr['t0'] else -1.0
        mid = pr['mid'][0 if tip == pr['t0'] else -1][1]
        pr['tip'] = tip
        pr['mouth'] = fld.pt(mid, tip)
        pr['mouth_in'] = fld.pt(mid, tip + inward * 1.0 / mid)
        pr['mouth_out'] = fld.pt(mid, tip - inward * 5.0 / mid)

    def pocket_border(self, pr):
        pk = pr['pk']
        fld = self.main
        pts = pr['outline']
        tip = pr['mouth']
        runs, cur = [], []
        for p in pts + [pts[0]]:
            if math.hypot(p[0] - tip[0], p[1] - tip[1]) > 3.2:
                cur.append(p)
            elif cur:
                runs.append(cur)
                cur = []
        if cur:
            runs.append(cur)
        if len(runs) > 1 and math.hypot(runs[0][0][0] - runs[-1][-1][0], runs[0][0][1] - runs[-1][-1][1]) < 2.0:
            runs = [runs[-1] + runs[0]] + runs[1:-1]
        if not self.visible(pr['k']):
            return
        if pk.kind == 'said':
            for run in runs:
                self.direct.lines.append((run, 'pS', False))
                self.direct.lines.append((offset_line(run, 1.25), 'pSi', False))
        else:
            rj = Rng(self.seed + '/pocket/' + pk.pid)
            for run in runs:
                jag = []
                for i, p in enumerate(run):
                    if 0 < i < len(run) - 1:
                        th, rho = fld.polar(p)
                        jag.append(fld.pt(rho + rj.uni(-0.9, 0.9), th))
                    else:
                        jag.append(p)
                self.direct.lines.append((jag, 'pC', False))

    # ---------------------------------------------------------------- crossings (v2 7)
    def crossings(self):
        ids = sorted(self.lines)
        self.cuts_at = {rid: [] for rid in ids}
        self.found = []
        braid_pairs = {}
        for bid, g in getattr(self, 'braids_geo', {}).items():
            for s in g['strands']:
                braid_pairs.setdefault(s, set()).update(g['strands'])
        bind_pairs = {}
        for kid, g in getattr(self, 'binds_geo', {}).items():
            bind_pairs[(g['x'], g['y'])] = g
            bind_pairs[(g['y'], g['x'])] = g
        laps = set(self.md.laps)
        braid_x = {}
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                a, b = ids[i], ids[j]
                ra, rb = a.split(':')[0], b.split(':')[0]
                if ra == rb:
                    continue
                if self.same_node(a, b):
                    continue
                shared = self.shared_ends(a, b)
                for x, sa, sb, sn in intersections(self.lines[a], self.lines[b]):
                    la, lb = arclen(self.lines[a])[-1], arclen(self.lines[b])[-1]
                    if sa < 2.0 or sb < 2.0 or sa > la - 1.0 or sb > lb - 1.0:
                        continue
                    # two runners that meet at one mark (the target of one, the source of the
                    # other) touch there; that is a meeting, not a crossing
                    if any(math.hypot(x[0] - e[0], x[1] - e[1]) < 12.0 for e in shared):
                        continue
                    if sn < 0.2588 and not (b in braid_pairs.get(a, ())):
                        self.warnings.append('runners %s and %s cross at under 15 degrees' % (a, b))
                    if b in braid_pairs.get(a, ()):
                        braid_x.setdefault(frozenset((a, b)), []).append((x, sa, sb, a, b))
                        continue
                    if (a, b) in bind_pairs:
                        g = bind_pairs[(a, b)]
                        lx = dot(sub(x, g['site']), g['ex'])
                        over = g['x'] if lx > 0 else g['y']
                        kind = 'bind'
                    elif (a, b) in laps or (b, a) in laps:
                        over = a if (a, b) in laps else b
                        kind = 'break'
                    else:
                        ca, cb = self.canon.get(ra, 0), self.canon.get(rb, 0)
                        over = a if ca > cb else b
                        kind = 'pass'
                    under = b if over == a else a
                    su = sb if under == b else sa
                    self.cuts_at[under].append((su, H_RUN + GAP_EXTRA, kind == 'break'))
                    self.found.append((over, under, kind, x))
        for bid, g in getattr(self, 'braids_geo', {}).items():
            xs = []
            for key, lst in braid_x.items():
                if set(key) <= set(g['strands']):
                    xs += lst
            a0 = g['strands'][0]
            cord_s = arclen(g['cord'])
            def along(item):
                x = item[0]
                i = min(range(len(g['cord'])), key=lambda q: math.hypot(g['cord'][q][0] - x[0], g['cord'][q][1] - x[1]))
                return cord_s[i]
            xs.sort(key=along)
            N = g['N']
            pat = g['pat']
            if len(xs) != N:
                self.warnings.append('braid %s: %d crossings for %d turns' % (bid, len(xs), N))
            for m, (x, sa, sb, a, b) in enumerate(xs):
                who = pat[m] if m < N else 'a'
                ov = g['strands'][ord(who) - ord('a')]
                if ov not in (a, b):
                    ov = a
                un = b if ov == a else a
                su = sb if un == b else sa
                brk = pat.endswith('!') and m == N - 1
                self.cuts_at[un].append((su, H_RUN + GAP_EXTRA - 0.3, brk))
                self.found.append((ov, un, 'braid-break' if brk else 'braid', x))

    def shared_ends(self, a, b):
        out = []
        for u, v in ((a, b), (b, a)):
            iu, iv = self.info.get(u), self.info.get(v)
            if not iu or not iv or iu[0] is None or iv[0] is None or iv[0].src is None:
                continue
            tg = iu[4]
            if tg is not None and tg[0] == 'mark' and tg[1] == iv[0].src:
                out.append(self.lines[u][-1])
                out.append(self.lines[v][0])
        return out

    def same_node(self, a, b):
        ia, ib = self.info.get(a), self.info.get(b)
        if not ia or not ib or ia[0] is None or ib[0] is None:
            return False
        if ia[0].src is None or ib[0].src is None:
            return False
        return ia[0].src == ib[0].src and not (a in getattr(self, 'lap_ids', ()) )

    # ---------------------------------------------------------------- cutting a runner
    def cut_runner(self, rid):
        pts = self.lines[rid]
        if len(pts) < 2:
            return
        pts = resample_even(pts, 3.0)
        self.lines[rid] = pts
        rn, end, tr, dirn, tg = self.info.get(rid, (None, 'head', None, 1.0, None))
        if tg is not None and tg[0] == 'pocket':
            pass
        vis = True
        if self.plate is not None:
            vis = True
        s = arclen(pts)
        tot = s[-1] or 1.0
        stub = getattr(self, 'stubs', {}).get(rid)
        trunk_child = (':' in rid and not rid.endswith(':out') and not rid.endswith(':trunk')) or stub == 'in'
        h0 = 0.95 if trunk_child else H_RUN

        fine = 0.72 if rid in getattr(self, 'fine', ()) else 1.0     # a pocket's finer knife (v2 8)

        def hw_at(si):
            h = h0 - (h0 - 0.45) * (si / tot)
            if stub == 'out':
                h = h0 - (h0 - 0.8) * (si / tot)       # cut off by the plate's edge, not tapered
            if si < 2.2 and not trunk_child and not rid.endswith(':out'):
                h = max(h, BUD - 0.25 * si)
            return h * fine
        keep = [True] * len(pts)
        for su, gap, brk in self.cuts_at.get(rid, ()):
            for i, si in enumerate(s):
                if abs(si - su) < gap:
                    keep[i] = False
        pieces, cur = [], []
        for i in range(len(pts)):
            if keep[i]:
                cur.append(i)
            elif cur:
                pieces.append(cur)
                cur = []
        if cur:
            pieces.append(cur)
        hidden = rn is not None and rn.hidden
        seeming = rn is not None and rn.seeming
        for pc in pieces:
            if len(pc) < 2:
                continue
            P = [pts[i] for i in pc]
            H = [hw_at(s[i]) for i in pc]
            if pc[0] != 0:
                H[0] *= 0.55
            if pc[-1] != len(pts) - 1:
                H[-1] *= 0.55
            if hidden or seeming:
                L_, R_ = edges_of(P, H)
                if seeming:
                    self.rcuts.line(L_, 'e0')
                    self.rcuts.line(R_, 'e0')
                else:
                    lit_first = dot(unit(sub(L_[len(L_) // 2], R_[len(R_) // 2])), LIGHT) < 0
                    self.rcuts.line(L_ if lit_first else R_, 'smL')
                    self.rcuts.line(R_ if lit_first else L_, 'smS')
            elif self.runner_silhouette:
                # a whole round heavy with runners cuts them as silhouettes, one tone; their facets
                # are kept for the ring plates (v2 11.6)
                L_, R_ = edges_of(P, H)
                self.rcuts.flat.append(L_ + list(reversed(R_)))
            else:
                self.rcuts.vcut(P, H)
        # a thwarted strand is splintered where it breaks (v2 7.1)
        for su, gap, brk in self.cuts_at.get(rid, ()):
            if not brk:
                continue
            for sg in (-1, 1):
                se = su + sg * gap
                i = min(range(len(s)), key=lambda q: abs(s[q] - se))
                if 0 < i < len(pts) - 1:
                    d = unit(sub(pts[min(i + 1, len(pts) - 1)], pts[max(i - 1, 0)]))
                    d = d if sg < 0 else (-d[0], -d[1])
                    d = (-d[0], -d[1])
                    for ang in (-40, 36):
                        e = add(pts[i], rot(d, math.radians(ang)), 2.8)
                        self.rcuts.vcut([pts[i], lerp(pts[i], e, 0.5), e], [0.55, 0.42, 0.14])
        if rn is not None and end not in ('fork', 'bind', 'stub'):
            self.terminal(pts, rn.role, end)
            if stub != 'in':
                self.ends.append((rid, rn, pts[0], pts[-1], tr))

    def terminal(self, pts, role, end):
        """The end says the role (v2 6.1). Sizes in units: about three runner-widths."""
        E = pts[-1]
        back = pts[-5] if len(pts) > 5 else pts[0]
        d = unit(sub(E, back))
        n = (-d[1], d[0])
        cut = self.rcuts.vcut
        if role in ('in', 'blind'):
            r = 5.2
            c = add(E, d, r)
            base = math.atan2(-d[1], -d[0])
            arc = []
            for i in range(13):
                a = base - math.radians(80) + math.radians(160) * i / 12.0
                arc.append((c[0] + r * math.cos(a), c[1] + r * math.sin(a)))
            cut(arc, [0.45 + 0.3 * math.sin(math.pi * i / 12.0) for i in range(13)])
        elif role == 'for':
            c = add(E, d, 5.0)
            lens = []
            for i in range(18):
                a = 2 * math.pi * i / 18
                x = math.cos(a) * 5.0
                y = math.sin(a) * 2.3 * abs(math.sin(a)) ** 0.2
                lens.append(add(add(c, d, x), n, y))
            cut(lens, [0.45] * 18, closed=True)
        elif role == 'bc':
            for ang, ln in ((-40, 6.6), (-4, 5.0), (28, 6.0)):
                e = add(E, rot(d, math.radians(ang)), ln)
                cut([E, lerp(E, e, 0.5), e], [0.6, 0.45, 0.14])
        elif role == 'as':
            for off in (0.8, 4.2):
                c = add(E, d, off)
                a, b = add(c, n, 4.2), add(c, n, -4.2)
                cut([a, lerp(a, b, 0.5), b], [0.35, 0.6, 0.35])
        elif role == 'thru':
            for ang in (-30, 30):
                e = add(E, rot(d, math.radians(ang)), 7.2)
                cut([E, lerp(E, e, 0.5), e], [0.6, 0.45, 0.14])
        elif role == 'with':
            e = add(E, d, 4.6)
            cut([E, lerp(E, e, 0.5), e], [0.6, 0.95, 0.85])

    def add_dips(self):
        """Where a runner crosses a ring line, the line dips 1.3 over +-3.6 units (v2 4.6)."""
        for rid, pts in self.lines.items():
            rn, end, tr, dirn, tg = self.info.get(rid, (None, None, None, None, None))
            fld = self.main
            if rn is not None and rn.src is not None:
                src = self.find_rec(rn.src)
                if src:
                    fld = src['field']
            prev = None
            for p in pts[::2]:
                th, rho = fld.polar(p)
                if prev is not None:
                    pth, prho = prev
                    for k in range(1, self.K + 1):
                        lb = fld.base(k, th)
                        if (prho - lb) * (rho - lb) < 0:
                            fld.bumps.setdefault(k, []).append((th, 1.3 if rho > prho else -1.3, 3.6, 'c'))
                prev = (th, rho)


# =================================================================================================
#  THE WOOD, THE CHECKS AND THE SVG
# =================================================================================================
class WoodMixin:
    def ring_sets(self):
        if self.locals:
            sets = [(lf, list(range(1, self.lay.kj + 1))) for lf in self.locals]
            sets.append((self.main, list(range(self.lay.kj + 1, self.K + 1))))
            return sets
        return [(self.main, list(range(1, self.K + 1)))]

    def nsamp(self, fld, k):
        rho = self.lay.R[k] if k < len(self.lay.R) else self.lay.R[-1]
        return max(60, min(120, int(2 * math.pi * rho / 24.0)))

    def ring_pts(self, fld, k, off=0.0, flow=True):
        ths = fld.samples(k, self.nsamp(fld, k)) if flow else [2 * math.pi * i / self.nsamp(fld, k) for i in range(self.nsamp(fld, k))]
        return [fld.pt(fld.line(k, t, flow) + off, t) for t in ths], ths

    def paint_wood(self):
        with prec(1):
            if self.plate:
                return self._paint_plate()
            return self._paint_wood()

    def _paint_plate(self):
        """A ring plate: the ring alone, an annulus with no pith (never a round, so never 'nothing is
        given here'), at reading scale (v2 11.5)."""
        K = self.plate
        lay = self.lay
        fld = self.main
        P = self.pref
        wood = []
        N = 240
        ths = [2 * math.pi * i / N for i in range(N)]
        inner_r = lambda t: (fld.base(K - 1, t) if K > 1 else PITH_R + 20.0) - 14.0
        outer = [fld.pt(fld.base(K, t) + 14.0, t) for t in ths]
        inner = [fld.pt(inner_r(t), t) for t in ths]
        self.bbox_pts = outer
        self.outer_d = smooth_d(outer) + smooth_d(inner[::-1])
        wood.append('<use href="#%s-o" fill-opacity="%s"/>' % (P, OP['disc']))
        if self.stone:
            wood.append('<use href="#%s-o" fill="url(#%s-st)"/>' % (P, P))
        for yr in self.md.rings[K - 1].years:
            for c in yr.conds:
                wood += self.condition(K, yr.y, c)
        for pid, pr in self.pockets.items():
            wood += self.pocket_bands(pr)
        yl = []
        for key, rec in self.recs.items():
            if rec.get('kind') != 'mark' or rec['y'] <= 1 or rec['mk'].root:
                continue
            c = lay.cells[rec['k']]
            half = 0.62 / c
            t0, t1 = rec['th'] - half * SLOT, rec['th'] + half * SLOT
            a0 = lay.year_r[(rec['k'], rec['y'])][0]
            yl.append(smooth_d([fld.pt(fld.yr(K, a0, t0 + (t1 - t0) * q / 16.0), t0 + (t1 - t0) * q / 16.0) for q in range(17)], False))
        for pid, pr in self.pockets.items():
            a, b = lay.year_r[(K, pr['y'])]
            t0, t1 = pr['t0'] - 0.35 * SLOT, pr['t1'] + 0.35 * SLOT
            for base_r, amp in ((a, -2.2), (b, 1.6)):
                pts = []
                for q in range(41):
                    t = t0 + (t1 - t0) * q / 40.0
                    qq = (t - pr['t0']) / (pr['t1'] - pr['t0'])
                    bow = amp * (math.sin(math.pi * qq) ** 0.8 if 0 <= qq <= 1 else 0.0)
                    pts.append(fld.pt(fld.yr(K, base_r, t) + bow, t))
                yl.append(smooth_d(pts, False))
        if yl:
            with prec(2):
                wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".7" stroke-linecap="round" d="%s"/>' % (OP['year'], ''.join(yl)))
        with prec(2):
            for k in [kk for kk in (K - 1, K) if kk >= 1]:
                o, ths_ = self.ring_pts(fld, k)
                ti = [2 * math.pi * (1 - i / 96.0) for i in range(96)]
                i_ = [fld.pt(fld.line(k, t, False) - lay.late_w(k, t), t) for t in ti]
                wood.append('<path fill-opacity="%.2f" d="%s%s"/>' % (OP['late'] * lay.late_op[k], smooth_d(o), smooth_d(i_)))
            rl = ''.join(smooth_d(self.ring_pts(fld, k, 5.0)[0]) for k in (K - 1, K) if k >= 1 and k in self.md.rules)
            if rl:
                wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1.1" d="%s"/>' % (OP['rule'], rl))
        hair = []
        for h in self.hairlines():
            seg = [p for p in h if inner_r(fld.polar(p)[0]) + 1 < fld.polar(p)[1] < fld.base(K, fld.polar(p)[0]) + 13]
            if len(seg) >= 2:
                hair.append(seg)
        if hair:
            with prec(10):
                wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".95" stroke-linecap="round" d="%s"/>' % (OP['hair'], ''.join(poly_d(h, False) for h in hair)))
        wood.append('<use href="#%s-o" fill="none" stroke="currentColor" stroke-opacity=".34" stroke-width=".8"/>' % P)
        self.pith_svg = ''
        self.inc_jag = []
        return wood

    def _paint_wood(self):
        lay = self.lay
        K = self.K
        wood = []
        NB = 300
        bths = [2 * math.pi * i / NB for i in range(NB)]
        outer_pts = [self.main.pt(self.outer(t), t) for t in bths]
        ringK, _ = self.ring_pts(self.main, K)
        self.bbox_pts = outer_pts
        self.outer_d = poly_d(outer_pts)
        P = self.pref
        wood.append('<use href="#%s-o" fill-opacity="%s"/>' % (P, OP['disc']))
        wood.append('<path fill-opacity="%s" fill-rule="evenodd" d="%s%s"/>' % (OP['barkband'], self.outer_d, smooth_d(ringK)))
        if self.md.meta.get('char'):
            c0 = self.axis + math.radians(200)
            span = math.radians(70)
            a_pts = [self.main.pt(self.outer(c0 + span * (i / 30.0 - 0.5)) + 3, c0 + span * (i / 30.0 - 0.5)) for i in range(31)]
            b_pts = [self.main.pt(self.main.base(K, c0 + span * (0.5 - i / 30.0)) - 3.0, c0 + span * (0.5 - i / 30.0)) for i in range(31)]
            self.char_d = poly_d(a_pts + b_pts)
        rules = self.md.rules if not self.stage0 else []
        if not self.locals and rules and self.wood not in ('green',):
            hp, _ = self.ring_pts(self.main, rules[0])
            wood.append('<path fill-opacity="%s" d="%s"/>' % (OP['heart'], smooth_d(hp)))
        if self.locals and self.wood not in ('green',):
            for lf in self.locals:
                hp, _ = self.ring_pts(lf, lay.kj)
                wood.append('<path fill-opacity="%s" d="%s"/>' % (OP['heart'], smooth_d(hp)))
        if self.stone:
            wood.append('<path fill="url(#%s-st)" d="%s"/>' % (P, smooth_d(ringK)))
        if not self.stage0:
            for r in self.md.rings:
                for yr in r.years:
                    for c in yr.conds:
                        wood += self.condition(r.k, yr.y, c)
            for pid, pr in self.pockets.items():
                wood += self.pocket_bands(pr)
        # year-lines: a faint arc under every mark that is not in its ring's first year (v2 4.2),
        # the wedging rings of real wood; and round every pocket, the year's lines part (v2 8)
        yl = []
        if not self.stage0:
            for key, rec in self.recs.items():
                if rec.get('kind') != 'mark' or rec['y'] <= 1 or rec['mk'].root:
                    continue
                fld = rec['field']
                c = lay.cells[rec['k']]
                half = 0.62 / c
                t0, t1 = rec['th'] - half * SLOT, rec['th'] + half * SLOT
                a0 = lay.year_r[(rec['k'], rec['y'])][0]
                yl.append(smooth_d([fld.pt(fld.yr(rec['k'], a0, t0 + (t1 - t0) * q / 16.0), t0 + (t1 - t0) * q / 16.0) for q in range(17)], False))
            for pid, pr in self.pockets.items():
                k, y = pr['k'], pr['y']
                a, b = lay.year_r[(k, y)]
                t0, t1 = pr['t0'] - 0.35 * SLOT, pr['t1'] + 0.35 * SLOT
                for base_r, amp in ((a, -2.2), (b, 1.6)):
                    pts = []
                    for q in range(41):
                        t = t0 + (t1 - t0) * q / 40.0
                        qq = (t - pr['t0']) / (pr['t1'] - pr['t0'])
                        bow = amp * (math.sin(math.pi * qq) ** 0.8 if 0 <= qq <= 1 else 0.0)
                        pts.append(self.main.pt(self.main.yr(k, base_r, t) + bow, t))
                    yl.append(smooth_d(pts, False))
        if yl:
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".7" stroke-linecap="round" d="%s"/>' % (OP['year'], ''.join(yl)))
        PREC.insert(0, 2)
        # latewood: each ring line a latewood band, crisp outside, yielding round the cuts (v2 4.6)
        with prec(2):
            for fld, ks in self.ring_sets():
                for k in ks:
                    o, ths = self.ring_pts(fld, k)
                    ti = [2 * math.pi * (1 - i / 48.0) for i in range(48)]
                    i_ = [fld.pt(fld.line(k, t, False) - lay.late_w(k, t), t) for t in ti]
                    op = OP['late'] * (lay.late_op[k] if not (k == K and fld is self.main) else 1.25)
                    with prec(1):
                        inner = smooth_d(i_)
                    wood.append('<path fill-opacity="%.2f" d="%s%s"/>' % (op, smooth_d(o), inner))
        if self.locals:
            o, ths = self.ring_pts(self.main, lay.kj)
            i_ = [self.main.pt(self.main.line(lay.kj, t) - 1.3, t) for t in ths[::-1]]
            wood.append('<path fill-opacity="%s" d="%s%s"/>' % (OP['late'], smooth_d(o), smooth_d(i_)))
        PREC.pop(0)
        rl = []
        for k in rules:
            pts, _ = self.ring_pts(self.main, k, 5.0)
            with prec(2):
                rl.append(smooth_d(pts))
        if rl:
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1.1" d="%s"/>' % (OP['rule'], ''.join(rl)))
        inc, self.inc_jag = [], []
        if not self.stage0:
            for r in self.md.rings:
                if not r.inc:
                    continue
                k = r.k
                flds = [self.main] if (not self.locals or k > lay.kj) else [self.locals[i] for i in (r.inc if r.inc != [None] else range(len(self.locals))) if i is not None and i < len(self.locals)]
                for fld in flds:
                    inc.append(smooth_d([fld.pt(fld.line(k, t, False) + 2.6, t) for t in [2 * math.pi * i / 96 for i in range(96)]]))
                    rj = Rng(self.seed + '/inc/%d/%d' % (k, 99 if fld is self.main else self.locals.index(fld)))
                    rho0 = fld.base(k, 0)
                    nj = max(60, int(2 * math.pi * rho0 / 3.2))
                    jag = [fld.pt(fld.line(k, 2 * math.pi * i / nj, False) + 2.6 + rj.uni(-0.95, 0.95), 2 * math.pi * i / nj) for i in range(nj)]
                    with prec(10):
                        self.inc_jag.append(poly_d(jag))
            for key, rec in self.recs.items():
                if rec.get('kind') == 'mark' and rec['mk'].graft:
                    inc.append(self.graft_d(rec))
        if inc:
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="3.4" d="%s"/>' % (OP['incband'], ''.join(inc)))
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1.05" stroke-linejoin="bevel" d="%s"/>' % (OP['inc'], ''.join(self.inc_jag)))
        for q in range(self.md.pale if not self.stage0 else 0):
            pts = [self.main.pt(self.main.base(K, t) + 6 + 7 * q, t) for t in bths[::2]]
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity=".55" stroke-width="2.2" d="%s"/>' % smooth_d(pts))
        wood += self.bark_texture()
        self.pith_svg = ''
        with prec(10):
            for p in self.piths:
                if self.war:
                    h = PITH_R
                    pts = [add(add(p, er(self.axis), x), et(self.axis), y) for x, y in ((-h, -h), (h, -h), (h, h), (-h, h))]
                    self.pith_svg += '<path fill-opacity="%s" d="%s"/>' % (OP['pith'], poly_d(pts))
                else:
                    self.pith_svg += '<circle fill-opacity="%s" cx="%s" cy="%s" r="%s"/>' % (OP['pith'], _num(_q(p[0])), _num(_q(p[1])), PITH_R)
        if not self.stage0:
            hair = self.hairlines()
            if hair:
                with prec(10):
                    wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".95" stroke-linecap="round" stroke-linejoin="round" d="%s"/>' % (OP['hair'], ''.join(poly_d(h, False) for h in hair)))
        return wood

    def bark_texture(self):
        g = self.lay
        K = self.K
        out = []
        skips = []
        for key, rec in self.recs.items():
            if rec.get('kind') == 'bark':
                skips.append((rec['th'], 1.35 * rec['B'] / max(rec['rin'], 1) + 0.02))
        skip = lambda t: any(abs(wrap(t - c)) < h for c, h in skips)
        rK = lambda t: self.main.base(K, t)
        depth = lambda t, f: rK(t) + f * (self.outer(t) - rK(t))
        rb = Rng(self.seed + '/barktex')
        fis, lam = [], []
        notches = sorted(g.notches)
        for i, (c, wdt, dp) in enumerate(notches):
            if skip(c) or g.young:
                continue
            f_end = rb.uni(0.12, 0.42)
            f_top = 1 - dp + 0.02
            pts = [self.main.pt(depth(c + rb.uni(-0.004, 0.004), f_top + (f_end - f_top) * q / 4.0), c + 0.006 * math.sin(q)) for q in range(5)]
            fis.append(poly_d(pts, closed=False))
            c2 = notches[(i + 1) % len(notches)][0]
            span = (c2 - c) % (2 * math.pi)
            for f in (rb.uni(0.30, 0.42), rb.uni(0.58, 0.72)):
                a0, a1 = c + span * rb.uni(0.12, 0.3), c + span * rb.uni(0.65, 0.9)
                n = max(3, int((a1 - a0) / 0.03))
                arc = [t for t in [(a0 + (a1 - a0) * q / n) for q in range(n + 1)] if not skip(t)]
                if len(arc) > 2:
                    lam.append(smooth_d([self.main.pt(depth(t, f), t) for t in arc], closed=False))
        if fis:
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".8" stroke-linecap="round" d="%s"/>' % (OP['plate'], ''.join(fis)))
        if lam:
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".6" stroke-linecap="round" d="%s"/>' % (OP['plate'] * 0.6, ''.join(lam)))

        def arcs(frac_fn, n=200):
            segs, cur = [], []
            for i in range(n + 1):
                t = 2 * math.pi * i / n
                if skip(t):
                    if len(cur) > 1:
                        segs.append(cur)
                    cur = []
                    continue
                cur.append(self.main.pt(frac_fn(t), t))
            if len(cur) > 1:
                segs.append(cur)
            return ''.join(poly_d(s_, closed=False) for s_ in segs)
        bw = g.bark_w
        if g.young:
            out.append('<g clip-path="url(#%s-bk)">' % self.pref)
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="%s" stroke-dasharray=".5 2.6 .4 3.9 .6 2.2 .45 4.4" d="%s"/>'
                       % (OP['fiss'] * 0.75, _num(_q(0.42 * bw)), arcs(lambda t: depth(t, 0.62))))
            out.append('</g>')
        out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".6" d="%s"/>'
                   % (OP['cambium'] * 0.55, arcs(lambda t: rK(t) + 2.2, 150)))
        out.append('<use href="#%s-o" fill="none" stroke="currentColor" stroke-opacity=".34" stroke-width=".8" stroke-linejoin="round"/>' % self.pref)
        return out

    def graft_d(self, rec):
        fld = rec['field']
        k = rec['k']
        th = rec['th']
        B = rec['B']
        r0 = fld.base(k - 1, th) + 2.0
        r1 = fld.base(k, th) - 1.0
        hw = 1.25 * B / r1
        ap = fld.pt(r0, th)
        a = [lerp(ap, fld.pt(r1, th - hw), i / 10.0) for i in range(11)]
        b = [lerp(ap, fld.pt(r1, th + hw), i / 10.0) for i in range(11)]
        rj = Rng(self.seed + '/graft/%d' % k)
        jag = [add(p, (rj.uni(-1.2, 1.2), rj.uni(-1.2, 1.2))) for p in list(reversed(a)) + b[1:]]
        with prec(10):
            self.inc_jag.append(poly_d(jag, closed=False))
        return poly_d(list(reversed(a)) + b[1:], closed=False)

    def condition(self, k, y, c):
        name = c.band.upper()
        fld = self.field_for(c.pith, k)
        full = c.full
        if not full:
            s0, s1 = c.s0, c.s1
            if s1 < s0:
                s1 += 16
            th0 = self.axis + (s0 - 0.5) * SLOT
            th1 = self.axis + (s1 + 0.5) * SLOT
        else:
            th0, th1 = self.axis, self.axis + 2 * math.pi
        rho_m = fld.yr(k, 0.5 * sum(self.lay.year_r[(k, y)]), 0.5 * (th0 + th1))
        n = max(12, int(abs(th1 - th0) * rho_m / (4.0 if name in ('DREAD', 'WHITE', 'WATER') else 11.0)))
        a, b = self.lay.year_r[(k, y)]
        rr = lambda t, fr: fld.yr(k, a + fr * (b - a), t)
        out = []
        tt = [th0 + (th1 - th0) * i / n for i in range(n + 1)]
        if full:
            tt = tt[:-1]
        end_fade = (lambda i: 1.0) if full else (lambda i: min(1.0, 4.0 * i / n, 4.0 * (n - i) / n) ** 0.6)
        if name == 'MIST':
            top, bot = [], []
            for i, t in enumerate(tt):
                wv = 0.022 * math.sin(i * 0.33) + 0.012 * math.sin(i * 0.9)
                f = end_fade(i)
                top.append(fld.pt(rr(t, 0.5 + (0.28 + wv) * f), t))
                bot.append(fld.pt(rr(t, 0.5 - (0.28 - wv) * f), t))
            if full:
                out.append('<path fill-opacity="%s" fill-rule="evenodd" d="%s%s"/>' % (OP['mist'], smooth_d(top), smooth_d(bot[::-1])))
            else:
                out.append('<path fill-opacity="%s" d="%s"/>' % (OP['mist'], smooth_d(top + bot[::-1])))
        elif name == 'WHITE':
            pts = [fld.pt(rr(t, 0.5), t) for t in tt]
            step = rho_m * math.radians(4)
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="%s" stroke-dasharray=".9 %s" d="%s"/>'
                       % (OP['frost'], _num(_q(0.5 * (b - a))), _num(_q(step - 0.9)), smooth_d(pts, closed=full)))
        elif name == 'DREAD':
            top, bot = [], []
            rd_ = Rng(self.seed + '/dread/%d/%d' % (k, y))
            for i, t in enumerate(tt):
                gp = (2.4 * math.sin(math.pi * i / n) ** 0.8 + 0.3) if not full else 1.6 + 0.6 * math.sin(i * 0.3)
                j = rd_.uni(-0.5, 0.5)
                top.append(fld.pt(rr(t, 0.5) + gp + j, t))
                bot.append(fld.pt(rr(t, 0.5) - gp + j, t))
            self.direct.voids.append(top + bot[::-1])
            self.direct.lines.append((top + ([top[0]] if full else []), 'dT', False))
            self.direct.lines.append((bot + ([bot[0]] if full else []), 'dB', False))
        elif name == 'WATER':
            m = int(n * 1.6)
            pts = []
            for i in range(m + 1 - (1 if full else 0)):
                t = th0 + (th1 - th0) * i / m
                pts.append(fld.pt(rr(t, 0.5 + 0.14 * math.sin(2 * math.pi * rho_m * (t - th0) / 44.0)), t))
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1.1" d="%s"/>' % (OP['water'], smooth_d(pts, closed=full)))
        elif name == 'STILL':
            ds = ''.join(smooth_d([fld.pt(rr(t, 0.5) + off, t) for t in tt], closed=full) for off in (-1.5, 1.5))
            out.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".8" d="%s"/>' % (OP['still'], ds))
        elif name == 'DARK':
            top = [fld.pt(rr(t, 1.0), t) for t in tt]
            bot = [fld.pt(rr(t, 0.0), t) for t in tt]
            out.append('<path fill-opacity="%s" d="%s"/>' % (OP['dark'], smooth_d(top + bot[::-1])))
        else:
            raise GNError('unknown condition %s' % name)
        return out

    def hairlines(self):
        d = []
        md = self.md
        for pith, f, a, b in md.rays:
            fld = self.field_for(pith, a[0])
            pl = self.find_rec((pith, f, None, a[0], a[1]))
            th = pl['th'] if pl else self.th_file(f)
            r0 = fld.yr(a[0], self.lay.year_r[(a[0], a[1])][0], th) + 6
            r1 = fld.yr(b[0], self.lay.year_r[(b[0], b[1])][1], th) - 6
            d.append([fld.pt(r0 + (r1 - r0) * i / 8.0, th) for i in range(9)])
        for pith, f, a in md.mems:
            fld = self.field_for(pith, a[0])
            pl = self.find_rec((pith, f, None, a[0], a[1]))
            th = pl['th'] if pl else self.th_file(f)
            start = fld.pt((pl['rin'] if pl else fld.base(a[0] - 1, th)) - 1.0, th)
            if self.locals and fld is self.main:
                pp = min(self.piths, key=lambda p: abs(wrap(math.atan2(p[0], -p[1]) - th)) if (p[0] or p[1]) else 9)
            else:
                pp = fld.O
            u = unit(sub(pp, start))
            end = add(pp, u, -(PITH_R + 9.0))
            d.append([start, end])
            for ang, ln in MEMORY_TINES:
                d.append([end, add(end, rot(u, math.radians(ang)), ln)])
        return d

    # ---------------------------------------------------------------- checks (v2 14.2)
    def validate(self):
        lay = self.lay
        W = self.warnings
        for fld, ks in self.ring_sets():
            if self.plate:
                ks = [k for k in ks if k >= self.plate - 1][:2]
            for k in ks[:-1]:
                for i in range(0, 360, 3):
                    t = math.radians(i)
                    if fld.line(k + 1, t) - fld.line(k, t) < 4.0:
                        W.append('rings %d/%d come within 4 units at %d°' % (k, k + 1, i))
                        break
        if self.locals:
            for i, p in enumerate(self.piths):
                for j, q in enumerate(self.piths):
                    if i < j and math.hypot(p[0] - q[0], p[1] - q[1]) < 2 * lay.R[lay.kj] + 4:
                        W.append('joined piths %d and %d: own rings touch' % (i, j))
        for key, rec in self.recs.items():
            if self.plate:
                break
            for pts, closed in rec['polys']:
                for p in pts[::3]:
                    th, rho = polar_of(p)
                    if rho > self.outer(th) - 1.0:
                        W.append('a mark crosses the bark contour at %.0f°' % math.degrees(th))
                        break
        # the runner ends read to their own marks (v1 3.7, v2 14.1 step 6)
        for rid, rn, a, b, tr in self.ends:
            src = self.find_rec(rn.src) if rn.src else None
            for end, own, what in ((a, src, 'node'), (b, tr, 'terminal')):
                if own is None:
                    continue
                d_own = poly_dist(end, own['polys'])
                for key, rec in self.recs.items():
                    if rec is own or rec.get('kind') == 'bark':
                        continue
                    if poly_dist(end, rec['polys']) < d_own + 0.4:
                        W.append('runner %s: its %s is as near %s as its own mark' % (rid, what, addr_text(key) if key[0] != 'bark' else 'the bark'))
                        break
        # clearance and ring lines
        for rid, pts in self.lines.items():
            if rid in getattr(self, 'fine', ()):
                continue                               # inside its pocket, among the pocket's items
            rn = self.info.get(rid, (None,))[0]
            s = arclen(pts)
            own = set()
            if rn is not None and rn.src is not None:
                src = self.find_rec(rn.src)
                own.add(self.rec_key(src))
            tr = self.info.get(rid, (None, None, None))[2]
            if tr is not None:
                own.add(self.rec_key(tr))
            worst = 99.0
            for i, p in enumerate(pts):
                if s[i] < 8 or s[-1] - s[i] < 12:
                    continue
                allow = {o: (p, 99.0) for o in own if o}
                worst = min(worst, self.obst.dist(p, allow))
            if worst < 2.0:
                W.append('runner %s comes within %.1f of a mark' % (rid, worst))
        # declared breaks cross once; binds lock twice
        for ov, un in self.md.laps:
            if ov not in self.lines or un not in self.lines:
                continue
            n = sum(1 for o, u, k, x in self.found if o == ov and u == un and k == 'break')
            if n != 1:
                W.append('break %s ⊳ %s: %d crossings (must be exactly one)' % (ov, un, n))
        for kid, g in getattr(self, 'binds_geo', {}).items():
            n = sum(1 for o, u, k, x in self.found if k == 'bind' and {o, u} == {g['x'], g['y']})
            if n != 2:
                W.append('bind %s: %d lock crossings (must be two)' % (kid, n))
        for pid, pr in self.pockets.items():
            n = sum(1 for rn in self.md.runners for t in rn.tgts if t == ('pocket', pid))
            if n != 1:
                W.append('pocket %s: %d that-runners (must be exactly one)' % (pid, n))
        # age gating (v2 3): no device in wood too young for it
        wood = self.md.wood
        nrun = len(self.md.runners)
        if wood == 'green' and (nrun or any(t.fringe for m in self.md.all_marks() for t in (m.lig.toks or []))):
            W.append('green wood carries one sign, no runner and no fringe')
        if wood == 'forty' and nrun > 1:
            W.append('forty-summer wood carries one runner')
        for r in self.md.rings[:1]:
            for yr in r.years:
                for it in yr.items:
                    if isinstance(it, Pocket):
                        W.append('the heart ring carries no pocket')
                    elif any(t.fringe for t in (it.lig.toks or [])):
                        W.append('the heart ring carries no fringe')

    # ---------------------------------------------------------------- output
    def title_desc(self):
        md = self.md
        if self.state == 'locked':
            return 'A carving in the grain, not yet known', ''
        if self.stage0:
            return md.meta.get('stage0_english', 'Nothing is given here.'), md.meta.get('stage0_desc', '')
        if self.state == 'fragments':
            return md.meta.get('root_word') or 'A carving in the grain', ''
        if self.plate:
            return ('Ring %d of %s' % (self.plate, md.meta.get('name') or md.meta.get('english') or 'a carving in the grain'),
                    'A ring plate: the one ring re-laid at reading scale, as Seren reads the round; runners to other rings end at its edge.')
        return md.meta.get('english') or md.meta.get('name') or 'A carving in the grain', md.meta.get('literal', '')

    def render(self):
        self.build_marks()
        if not self.stage0:
            self.draw_runners()
            self.add_dips()
        wood = self.paint_wood()
        if not self.stage0:
            self.validate()
        return self.assemble(wood)

    def assemble(self, wood):
        P = self.pref
        xs = [p[0] for p in self.bbox_pts]
        ys = [p[1] for p in self.bbox_pts]
        pad = 14
        x0, y0 = math.floor(min(xs) - pad), math.floor(min(ys) - pad)
        w, h = math.ceil(max(xs) + pad) - x0, math.ceil(max(ys) + pad) - y0
        title, desc = self.title_desc()
        defs = ['<path id="%s-o"%s d="%s"/>' % (P, ' fill-rule="evenodd" clip-rule="evenodd"' if self.plate else '', self.outer_d)]
        defs.append(self.book.svg())
        # direct cuts (smoothed marks, the dread's shake, pocket borders) and the runners, by tone
        vis, msk = [], []
        for name, cuts, tones in (('d', self.direct, {'lit': OP['lit'], 'mid': OP['mid'], 'shade': OP['shade']}),
                                  ('r', self.rcuts, RUN_TONE[self.run_tone])):
            groups = {}
            for tone, poly in cuts.facets(tone_of):
                poly = simplify(poly, 0.3 if name == 'r' else 0.15)
                if len(poly) >= 3:
                    groups.setdefault(tone, []).append(poly)
            for tone in ('lit', 'mid', 'shade'):
                if tone in groups:
                    pid = '%s-%s%s' % (P, name, tone[0])
                    with prec(5 if name == 'r' else 10):
                        defs.append('<path id="%s" d="%s"/>' % (pid, ''.join(poly_d(p) for p in groups[tone])))
                    vis.append('<use href="#%s" fill-opacity="%s"/>' % (pid, tones[tone]))
                    # a runner is a fine cut: the wood yields a thinner margin round it than a mark's
                    msk.append('<use href="#%s"%s/>' % (pid, ' stroke-width="2.2"' if name == 'r' else ''))
            if cuts.flat:
                pid = '%s-%sf' % (P, name)
                with prec(5 if name == 'r' else 10):
                    defs.append('<path id="%s" d="%s"/>' % (pid, ''.join(poly_d(simplify(p, 0.3) if name == 'r' else p) for p in cuts.flat)))
                vis.append('<use href="#%s" fill-opacity="%s"/>' % (pid, tones['lit'] if name == 'r' else OP['flat']))
                msk.append('<use href="#%s"%s/>' % (pid, ' stroke-width="2.2"' if name == 'r' else ''))
        voids = self.direct.voids + self.rcuts.voids
        if voids:
            defs.append('<path id="%s-v" d="%s"/>' % (P, ''.join(poly_d(p) for p in voids)))
        LOP = {'e0': (OP['edge'], 1.0), 'smL': (OP['smooth_lit'], 1.1), 'smS': (OP['smooth_shade'], 0.8),
               'dT': (OP['rim'], 0.9), 'dB': (OP['rim'] * 0.62, 0.75),
               'pS': (OP['pocket_said'], 0.9), 'pSi': (OP['pocket_said_in'], 0.7), 'pC': (OP['pocket_cut'], 1.05)}
        lines = {}
        for cuts in (self.direct, self.rcuts):
            for pts, cls, closed in cuts.lines:
                lines.setdefault(cls, []).append(poly_d(pts, closed))
        line_uses, line_mask = [], []
        for cls in sorted(lines):
            lid = '%s-l%s' % (P, cls)
            defs.append('<path id="%s" d="%s"/>' % (lid, ''.join(lines[cls])))
            op, lw = LOP.get(cls, (OP['edge'], 1.0))
            line_uses.append('<use href="#%s" fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/>' % (lid, op, lw))
            line_mask.append('<use href="#%s"/>' % lid)
        if self.stone:
            defs.append(stipple_pattern(P + '-st', Rng(self.seed + '/stone')))
        defs.append('<clipPath id="%s-bk"><use href="#%s-o"/></clipPath>' % (P, P))
        # symbol placements: in the mask unlit, in the cuts lit by their twelve bucket tones
        place_vis, place_msk = [], []
        for group, A in self.places:
            uses = ''.join('<use href="#%s" transform="%s"/>' % (sid, mat_txt(Aa, t)) for sid, Aa, t in group)
            place_msk.append(uses)
            place_vis.append('<g style="%s">%s</g>' % (tone_vars(A), uses))
        mk = ['<mask id="%s-m" maskUnits="userSpaceOnUse" x="%d" y="%d" width="%d" height="%d">' % (P, x0, y0, w, h),
              '<rect x="%d" y="%d" width="%d" height="%d" fill="#fff"/>' % (x0, y0, w, h),
              '<g fill="#000" stroke="#000" stroke-width="3.4" stroke-linejoin="round">']
        mk += msk + place_msk
        if voids:
            mk.append('<use href="#%s-v" stroke-width="1"/>' % P)
        mk.append('</g><g fill="none" stroke="#000" stroke-width="3.6" stroke-linecap="round">')
        mk += line_mask
        mk.append('</g>')
        split_d = ''
        if self.md.meta.get('split') and not self.stage0:
            a = self.main.pt(self.outer(self.axis) + 20, self.axis)
            b = self.main.pt(self.outer(self.axis + math.pi) + 20, self.axis + math.pi)
            split_d = poly_d([a, b], closed=False)
            mk.append('<path stroke="#000" stroke-width="2.6" d="%s"/>' % split_d)
        if self.md.meta.get('char') and not self.stage0:
            mk.append('<path fill="#000" fill-opacity=".6" d="%s"/>' % self.char_d)
        mk.append('</mask>')
        defs.append(''.join(mk))
        body = ['<g mask="url(#%s-m)">' % P] + wood + ['</g>']
        lv = ';'.join('--o%s:%s;--w%s:%s' % (c[1:], LINE_CLS[c][0], c[1:], LINE_CLS[c][1]) for c in sorted(LINE_CLS))
        cuts = ['<g stroke="none" style="--f:%s;--c:%s;--v:0;--k:currentColor;%s">' % (OP['flat'], OP['char'], lv)]
        cuts += place_vis + vis + line_uses
        cuts.append(self.pith_svg)
        cuts.append('</g>')
        if getattr(self, 'tags', None):
            # Seren's pencil tags in the margin: her apparatus, not the grain (v2 11.5)
            tg = ['<g class="seren-tags" data-apparatus="seren" font-family="Georgia, serif" font-size="12" font-style="italic" fill-opacity=".6" text-anchor="middle">']
            for p, txt in self.tags:
                tg.append('<text x="%.1f" y="%.1f">%s</text>' % (p[0], p[1] + 4, esc(txt)))
            tg.append('</g>')
            cuts += tg
        if split_d:
            defs.append('<mask id="%s-sp" maskUnits="userSpaceOnUse" x="%d" y="%d" width="%d" height="%d"><rect x="%d" y="%d" width="%d" height="%d" fill="#fff"/><path stroke="#000" stroke-width="2.6" d="%s"/></mask>'
                        % (P, x0, y0, w, h, x0, y0, w, h, split_d))
            cuts = ['<g mask="url(#%s-sp)">' % P] + cuts + ['</g>']
            nrm = et(self.axis)
            faces = ''
            for off in (-1.9, 1.9):
                a = add(self.main.pt(self.outer(self.axis) + 20, self.axis), nrm, off)
                b = add(self.main.pt(self.outer(self.axis + math.pi) + 20, self.axis + math.pi), nrm, off)
                faces += poly_d([a, b], closed=False)
            cuts.append('<g clip-path="url(#%s-bk)"><path fill="none" stroke="currentColor" stroke-opacity=".5" stroke-width=".7" d="%s"/></g>' % (P, faces))
        rid = (' data-round="%s"' % esc(self.md.id)) if (self.state == 'whole' and not self.stage0) else ''
        head = ('<svg xmlns="http://www.w3.org/2000/svg" class="wood-ink" viewBox="%d %d %d %d" width="%d" height="%d" '
                'role="img" aria-labelledby="%s-t%s"%s data-r-outer="%d">'
                % (x0, y0, w, h, round(w * 0.6), round(h * 0.6), P, (' %s-d' % P) if desc else '', rid,
                   round(max(math.hypot(p[0], p[1]) for p in self.bbox_pts))))
        parts = [head, '<title id="%s-t">%s</title>' % (P, esc(title))]
        if desc:
            parts.append('<desc id="%s-d">%s</desc>' % (P, esc(desc)))
        parts.append('<style>%s</style>' % STYLE)
        parts.append('<defs>%s</defs>' % ''.join(defs))
        parts.append('<g fill="currentColor">')
        parts += body + cuts
        parts.append('</g></svg>')
        return ''.join(parts)


STYLE = (':root.wood-ink{color:%s}' % INK_FALLBACK
         + ''.join('.g2%s{fill-opacity:var(--%s,1)}' % (c, c) for c in BUCKET_CLS)
         + '.g2f{fill-opacity:var(--f,1)}.g2c{fill-opacity:var(--c,1)}.g2v{fill-opacity:var(--v,1);stroke-width:1}'
         + ''.join('.g2%s{stroke:var(--k,#000);stroke-opacity:var(--o%s,1);stroke-width:var(--w%s,3.6)}' % (c, c[1:], c[1:]) for c in sorted(LINE_CLS)))


def stipple_pattern(pid, rng):
    """Myststone: the wood turned to stone, a fine mineral stipple over the rings (v1 10.3)."""
    dots, big = [], []
    for i in range(34):
        x, y = rng.uni(0, 60), rng.uni(0, 60)
        (big if rng.next() < 0.3 else dots).append('M%s %sh0' % (_num(_q(x)), _num(_q(y))))
    glints = []
    for _ in range(6):
        x, y, a = rng.uni(0, 60), rng.uni(0, 60), rng.uni(0, math.pi)
        dx, dy = 1.8 * math.cos(a), 1.8 * math.sin(a)
        glints.append(poly_d([(x - dx, y - dy), (x + dx, y + dy)], closed=False))
    return ('<pattern id="%s" patternUnits="userSpaceOnUse" width="60" height="60">'
            '<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".9" stroke-linecap="round" d="%s"/>'
            '<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1.5" stroke-linecap="round" d="%s"/>'
            '<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width=".6" d="%s"/></pattern>'
            % (pid, OP['stipple'], ''.join(dots), OP['stipple'] * 0.8, ''.join(big), OP['stipple'] * 0.7, ''.join(glints)))


class Renderer(RunnerMixin, WoodMixin, Round):
    pass


# =================================================================================================
#  A CHIP: one sign alone on a chip of end-grain (the Book's inline drawings, v1 10.8)
# =================================================================================================
def render_chip(lig_text, seed, title, desc=None, cond=None, strip=False, mem=False):
    """One ligature on an annular sector of a large round, pith far below; the sign in the middle
    ring, cut as a symbol and lit where it stands. strip=True cuts the chip down to the band the mark
    stands in, for a drawing set in a line of text."""
    R = [PITH_R, 256.0, 296.0, 356.0, 394.0]
    r = Rng(seed + '/chip')
    h = [(m, r.uni(-1, 1), r.uni(0, 6.283)) for m in (9, 17, 29)]
    hk = [None] + [(r.uni(-1, 1), r.uni(0, 6.283)) for _ in range(6)]
    base = lambda k, t: R[k] + sum(a * math.sin(m * t + q) for m, a, q in h) * 1.1 + 1.6 * hk[k][0] * math.sin(21 * t + hk[k][1])
    pt = lambda rho, t: (rho * math.sin(t), -rho * math.cos(t))
    alpha = math.radians(9.0)
    P = 'k%07x' % (fnv1a(seed + lig_text) & 0xfffffff)
    book = SymbolBook(P)
    lig = Lig(lig_text)
    rin, rout = base(2, 0.0) + 5.4, base(3, 0.0) - 5.4
    B0, H0 = 24.0, max(1.8, min(6.5, H_MARK * 24.0))
    places, polys = [], []
    for p in expand_lig(lig):
        tok = p['tok']
        a, b = p['u']
        pa, pb = rin + a * (rout - rin), rin + b * (rout - rin)
        if tok.kind:
            pa += 3.0
        B = B0 * (0.7 if p['lig'] else 1.0) / (1.3 if tok.x3 else 1.0)
        H = H0 * (0.8 if p['lig'] else 1.0)
        mir = -1.0 if tok.not_ else 1.0
        e_r, e_t = rot(er(0.0), math.radians(tok.lean)), rot(et(0.0), math.radians(tok.lean))
        A = (e_r[0], e_r[1], mir * e_t[0], mir * e_t[1])
        copies = [(0.0, 1.0)] if not tok.x3 else [(-0.78, 0.52), (0.0, 0.52), (0.78, 0.52)]
        whole = PARTS[tok.sign][tok.part] if tok.part else None
        group = []
        for ci, (voff, bs) in enumerate(copies):
            mid = ci == len(copies) // 2
            sid, cuts = book.get(tok, pb - pa, B * bs, max(1.6, H * bs) if bs < 1 else H, pa,
                                 fringe=tuple(tok.fringe) if mid else (), kind_arc=1.2 * B if (mid and tok.kind) else None, whole=whole)
            book.used.add(sid)
            bpt = add(pt(pa, 0.0), et(0.0), voff * B)
            group.append((sid, A, bpt))
            polys += cuts.transformed(A, bpt).outlines()
        places.append((group, A))
    # the chip's outline: split along two rays, broken along two rings
    r2 = Rng(seed + '/edge')
    inner_r, outer_r = 268.0, 386.0
    outline = []
    n = 26
    for i in range(n + 1):
        t = -alpha + 2 * alpha * i / n
        outline.append(pt(outer_r + r2.uni(-0.6, 0.6) + 1.3 * math.sin(i * 0.7), t))
    for i in range(12):
        outline.append(pt(outer_r - (outer_r - inner_r) * i / 11.0, alpha + r2.uni(-0.004, 0.004) + 0.003 * math.sin(i * 2.1)))
    for i in range(n + 1):
        t = alpha - 2 * alpha * i / n
        outline.append(pt(inner_r + r2.uni(-0.6, 0.6) + 1.1 * math.sin(i * 0.9), t))
    for i in range(12):
        outline.append(pt(inner_r + (outer_r - inner_r) * i / 11.0, -alpha + r2.uni(-0.004, 0.004) + 0.003 * math.sin(i * 1.9)))
    xs = [q[0] for q in outline]
    ys = [q[1] for q in outline]
    x0, y0, x1, y1 = math.floor(min(xs) - 4), math.floor(min(ys) - 4), math.ceil(max(xs) + 4), math.ceil(max(ys) + 4)
    if strip:
        hh = y1 - y0
        y0, y1 = y0 + round(0.21 * hh), y0 + round(0.81 * hh)
        x0, x1 = x0 + 6, x1 - 6
    ths = [-alpha * 1.2 + 2.4 * alpha * i / 40 for i in range(41)]
    wood = []
    with prec(1):
        wood.append('<path fill-opacity="%s" d="%s"/>' % (OP['disc'] * 1.2, poly_d(outline)))
        late = []
        for k in (1, 2, 3):
            o = [pt(base(k, t), t) for t in ths]
            wv = [max(0.9, min(3.4, 2.1 + 1.0 * math.sin(1.4 * t / alpha + k * 2.1))) for t in ths]
            i_ = [pt(base(k, t) - wv[j], t) for j, t in enumerate(ths)][::-1]
            with prec(2):
                late.append(smooth_d(o, closed=False) + 'L' + smooth_d(i_, closed=False)[1:] + 'z')
        wood.append('<path fill-opacity="%s" d="%s"/>' % (OP['late'], ''.join(late)))
        if cond == 'MIST':
            tt = [-alpha * 0.98 + 1.96 * alpha * i / 30 for i in range(31)]
            rr = lambda t, f: base(2, t) + f * (base(3, t) - base(2, t))
            top = [pt(rr(t, 0.78 + 0.03 * math.sin(2 * math.pi * 326 * t / 90)), t) for t in tt]
            bot = [pt(rr(t, 0.22 - 0.03 * math.sin(2 * math.pi * 326 * t / 90 + 1)), t) for t in tt]
            with prec(2):
                wood.append('<path fill-opacity="%s" d="%s"/>' % (OP['mist'] * 1.3, smooth_d(top + bot[::-1])))
        if mem:
            wood.append('<path fill="none" stroke="currentColor" stroke-opacity="%s" stroke-width="1" d="%s"/>'
                        % (OP['hair'], poly_d([pt(rin - 1, 0.0), pt(inner_r - 6, 0.0)], False)))
    uses_m = ''.join(''.join('<use href="#%s" transform="%s"/>' % (sid, mat_txt(Aa, t)) for sid, Aa, t in g) for g, A in places)
    uses_v = ''.join('<g style="%s">%s</g>' % (tone_vars(A), ''.join('<use href="#%s" transform="%s"/>' % (sid, mat_txt(Aa, t)) for sid, Aa, t in g)) for g, A in places)
    lv = ';'.join('--o%s:%s;--w%s:%s' % (c[1:], LINE_CLS[c][0], c[1:], LINE_CLS[c][1]) for c in sorted(LINE_CLS))
    with prec(1):
        od = poly_d(outline)
    defs = (book.svg() + '<clipPath id="%s-c"><path d="%s"/></clipPath>' % (P, od)
            + '<mask id="%s-m" maskUnits="userSpaceOnUse" x="%d" y="%d" width="%d" height="%d"><rect x="%d" y="%d" width="%d" height="%d" fill="#fff"/>'
              '<g fill="#000" stroke="#000" stroke-width="3.4" stroke-linejoin="round">%s</g></mask>'
            % (P, x0, y0, x1 - x0, y1 - y0, x0, y0, x1 - x0, y1 - y0, uses_m))
    lab = '%s-t' % P + ((' %s-d' % P) if desc else '')
    head = ('<svg xmlns="http://www.w3.org/2000/svg" class="wood-ink" viewBox="%d %d %d %d" width="%d" height="%d" role="img" aria-labelledby="%s">'
            % (x0, y0, x1 - x0, y1 - y0, round((x1 - x0) * .75), round((y1 - y0) * .75), lab))
    td = '<title id="%s-t">%s</title>' % (P, esc(title)) + (('<desc id="%s-d">%s</desc>' % (P, esc(desc))) if desc else '')
    body = ('<g clip-path="url(#%s-c)"><g mask="url(#%s-m)">%s</g></g>' % (P, P, ''.join(wood))
            + '<path fill="none" stroke="currentColor" stroke-opacity=".38" stroke-width=".9" stroke-linejoin="round" d="%s"/>' % od
            + '<g stroke="none" style="--f:%s;--c:%s;--v:0;--k:currentColor;%s">%s</g>' % (OP['flat'], OP['char'], lv, uses_v))
    return head + td + '<style>%s</style>' % STYLE + '<defs>' + defs + '</defs><g fill="currentColor">' + body + '</g></svg>'


# =================================================================================================
#  READING TEXTS, AND THE COMMAND LINE
# =================================================================================================
def load_text(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    if path.endswith('.json'):
        md = read_json(json.loads(raw))
        return pack_model(md)
    return parse_gn(raw)


def render_model(md, state='whole', stage0=False, plate=None, run_tone='mid'):
    rd = Renderer(md, state=state, stage0=stage0, plate=plate, run_tone=run_tone)
    return rd.render(), rd


def canonical(md):
    lay = Layout(md)
    return print_gn(md, lay.cells[1:])


# the Book's rounds (the task of wf7): v1 grain texts read as v2 (13.7), with the v2 amendments of 17
BOOK = ['E1-01', 'E1-02', 'E1-03', 'E1-04', 'E1-05', 'E1-06', 'E1-07', 'BURN', 'E4-01', 'VI-1', 'NAELEAR', 'GIFT']


def make_texts():
    """Write the Book's rounds as Grain Notation v2 into wf7/grain2_texts/ (from wf6's v1 texts, read
    by v2 13.7; NAELEAR's x3 takes the kind-arc, v2 5.3 and 17), and IV.6 whole from its v2 text."""
    os.makedirs(TEXTS_DIR, exist_ok=True)
    src = os.path.join(SCRATCH, 'wf6', 'grain_texts')
    out = []
    for name in BOOK:
        with open(os.path.join(src, name + '.json'), encoding='utf-8') as f:
            doc = json.load(f)
        md = read_json(doc)
        if name == 'NAELEAR':
            for m in md.all_marks():
                for t in m.lig.toks:
                    if t.x3 and t.sign == 'US':
                        t.kind = True
            md.meta['literal'] = ('Those of us, a whole people, in the breath: US three times over, crowned with lenses '
                                  '(of wood), with the kind-arc under their feet, inside a MIST band on the same files.')
        text = canonical(md)
        p = os.path.join(TEXTS_DIR, name + '.gn2')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        out.append(p)
    iv6 = os.path.join(HERE, 'grain2', 'IV-6.json')
    if os.path.exists(iv6):
        md = load_text(iv6)
        md.meta.setdefault('english', 'The Voyage of the Aelvaren (IV.6), carved whole.')
        text = canonical(md)
        p = os.path.join(TEXTS_DIR, 'IV-6.gn2')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        out.append(p)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('text', nargs='?')
    ap.add_argument('-o', '--out')
    ap.add_argument('--state', default='whole', choices=['whole', 'fragments', 'locked'])
    ap.add_argument('--stage0', action='store_true')
    ap.add_argument('--plate', type=int)
    ap.add_argument('--gn', action='store_true', help='print the canonical Grain Notation v2')
    ap.add_argument('--run-tone', default='mid', choices=['mid', 'lit'], help='v2 19.2: (a) mid, recommended; (b) lit')
    ap.add_argument('--facets', action='store_true', help='cut the runners of a heavy whole round with facets, not as silhouettes')
    ap.add_argument('--make-texts', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    if a.make_texts:
        for p in make_texts():
            print(p)
        return 0
    if a.all or a.check:
        return run_all(check=a.check, run_tone=a.run_tone)
    if not a.text:
        ap.error('give a text, --all, --check or --make-texts')
    md = load_text(a.text)
    if a.gn:
        sys.stdout.write(canonical(md))
        return 0
    rd = Renderer(md, state=a.state, stage0=a.stage0, plate=a.plate, run_tone=a.run_tone)
    rd.facets = a.facets
    svg = rd.render()
    for w in rd.warnings:
        print('warning:', w, file=sys.stderr)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(svg)
        print('%s  %.1f KB' % (a.out, len(svg.encode('utf-8')) / 1024.0))
    else:
        sys.stdout.write(svg)
    return 0


def run_all(check=False, run_tone='mid'):
    os.makedirs(OUT_DIR, exist_ok=True)
    names = [n for n in BOOK] + ['IV-6']
    ok = True
    for name in names:
        p = os.path.join(TEXTS_DIR, name + '.gn2')
        if not os.path.exists(p):
            print('missing', p)
            ok = False
            continue
        with open(p, encoding='utf-8') as f:
            raw = f.read()
        md = parse_gn(raw)
        svg, rd = render_model(md, run_tone=run_tone)
        out = os.path.join(OUT_DIR, 'grain2_%s.svg' % name)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(svg)
        kb = len(svg.encode('utf-8')) / 1024.0
        budget = 350 if name == 'IV-6' else 60
        print('%-24s %7.1f KB  rings %2d  symbols %3d  placements %3d  runners %2d%s'
              % (os.path.basename(out), kb, md.K, len(rd.book.used), len(rd.places), len(md.runners),
                 '' if kb <= budget else '  OVER %d KB' % budget))
        for w in rd.warnings:
            print('   warning:', w)
        if check:
            # the round trip: the text's canonical GN parses back to itself (v2 14.2.1)
            again = canonical(parse_gn(raw))
            if again.strip() != raw.strip():
                ok = False
                print('   ROUND TRIP DIFFERS')
            svg2, _ = render_model(parse_gn(raw), run_tone=run_tone)
            if svg2 != svg:
                ok = False
                print('   NOT DETERMINISTIC')
    chip = render_chip('US×3‿', 'chip/NAELEAR_chip', 'Naelear, those of the breath.',
                       'US three times over, crowned with lenses (of wood), with the kind-arc under their feet: those of us, '
                       'a whole people, inside a MIST band on the same files. Drawn inline in II.2 as the untold word.', cond='MIST')
    with open(os.path.join(OUT_DIR, 'grain2_NAELEAR_chip.svg'), 'w', encoding='utf-8') as f:
        f.write(chip)
    print('%-24s %7.1f KB  chip' % ('grain2_NAELEAR_chip.svg', len(chip.encode('utf-8')) / 1024.0))
    if name == 'IV-6' and check:
        md = load_text(os.path.join(HERE, 'grain2', 'IV-6.json'))
        if canonical(md).split('\n', 1)[1] != open(os.path.join(TEXTS_DIR, 'IV-6.gn2'), encoding='utf-8').read().split('\n', 1)[1]:
            print('   IV-6: JSON and GN disagree')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
