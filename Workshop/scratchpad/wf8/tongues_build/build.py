"""Build Docs-ready Rivenkeep_Tongues.html v0.2.0 from the wf6 and wf7 specs, SVGs and hand-written templates.
Scratchpad only: this script never goes into Docs/. Output: wf7/out/Rivenkeep_Tongues.html

    python3 build.py [--doc-version v0.2.0]
"""
import base64
import csv
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mdlib import W, W7, load, inline, table, tables_after, find, render, strip_refs, fixall, post  # noqa: E402

sys.path.insert(0, W7)
import render_chisel as RC  # noqa: E402  (read-only use of the dry-cut renderer)
import to_ink as TI  # noqa: E402  (read-only: token string -> Garl Flenn markup)

DOCVER = 'v0.2.0'
if '--doc-version' in sys.argv:
    DOCVER = sys.argv[sys.argv.index('--doc-version') + 1]
DOCS = '/Users/riquochet/code/Rivenkeep/Docs'
OUT = W7 + '/out/Rivenkeep_Tongues.html'

S = load('w7:orrowen_v2.md')        # Orrowen v2: supersedes the wf6 shoreland spec
S0 = load('shoreland_spec.md')       # wf6, for the originality lists v2 closed
M = load('mystaeri_spec.md')         # Seilrhass, and the grain v1 (which stands)
A = load('w7:ancestor.md')           # the First Tongue
G = load('w7:grain_v2.md')           # the grain v2
LX = load('w7:lexicon_orrowen.md')   # the tier-3 lexicon summary
P1 = load('w7:pilot_I1.md')
P4 = load('w7:pilot_IV4.md')
B1 = load('w7:backtrans_I1.md')
B4 = load('w7:backtrans_IV4.md')
O = load('originality_report.md')
SRAW = '\n'.join(S)
MRAW = '\n'.join(M)
GRAW = '\n'.join(G)

# ---------------------------------------------------------------- head and house style
fight = open(DOCS + '/Rivenkeep_Fight.html', encoding='utf-8').read()
style = re.search(r'<style>\n(.*?)</style>', fight, re.S).group(1)
style = re.sub(r'--doc-version:"v[\d.]+"', '--doc-version:"%s"' % DOCVER, style)
assert ('--doc-version:"%s"' % DOCVER) in style

EXTRA_CSS = open(os.path.join(HERE, 'extra.css'), encoding='utf-8').read()
FONT_B64 = base64.b64encode(open(W7 + '/fonts/GarlFlenn.woff2', 'rb').read()).decode('ascii')
FONT_CSS = ("@font-face{font-family:'Garl Flenn';src:url(data:font/woff2;base64,%s) format('woff2');"
            "font-display:block}\n" % FONT_B64)

HEAD = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>Rivenkeep — The Tongues</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&amp;family=Crimson+Pro:ital,wght@0,300..600;1,300..600&amp;family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=Source+Sans+3:wght@300;400;600;700&amp;display=swap" rel="stylesheet">\n'
        '<style>\n' + style + '\n' + FONT_CSS + EXTRA_CSS + '</style>\n</head>\n')

# ---------------------------------------------------------------- SVG embedding
SVGDIRS = {'svg': W + '/svg', 'svg6': W + '/svg', 'svg7': W7 + '/svg', 'svgo': W7 + '/orig/svg'}
USED = []


def fix_mask_ids(s):
    # Renderer defect (wf6): a grain round's mid-wall facet path and its mask share the id "<p>-m".
    for mid in re.findall(r'<mask id="([^"]+)"', s):
        if len(re.findall(r'\bid="%s"' % re.escape(mid), s)) > 1:
            s = s.replace('<mask id="%s"' % mid, '<mask id="%sk"' % mid)
            s = s.replace('url(#%s)' % mid, 'url(#%sk)' % mid)
    return s


def uniq_ids(s, pfx):
    """Prefix every id in one SVG (and every reference to it) so any number can share a page."""
    ids = sorted(set(re.findall(r'\bid="([^"]+)"', s)), key=len, reverse=True)
    for i in ids:
        s = re.sub(r'\bid="%s"' % re.escape(i), 'id="%s%s"' % (pfx, i), s)
        s = s.replace('href="#%s"' % i, 'href="#%s%s"' % (pfx, i))
        s = s.replace('url(#%s)' % i, 'url(#%s%s)' % (pfx, i))
        s = re.sub(r'(aria-labelledby="[^"]*)\b%s\b' % re.escape(i), r'\g<1>%s%s' % (pfx, i), s)
    return s


def svg(kind, name, suffix=None):
    s = open(os.path.join(SVGDIRS[kind], name + '.svg'), encoding='utf-8').read().strip()
    assert s.startswith('<svg'), name
    s = fix_mask_ids(s)
    if suffix:
        s = uniq_ids(s, suffix + '-')
    USED.append(kind + ':' + name + (':' + suffix if suffix else ''))
    return s


def set_title(s, title, desc=None):
    s = re.sub(r'(<title[^>]*>)(.*?)(</title>)', lambda m: m.group(1) + html.escape(title, quote=False) + m.group(3), s, 1, re.S)
    if desc is not None and '<desc' in s:
        s = re.sub(r'(<desc[^>]*>)(.*?)(</desc>)', lambda m: m.group(1) + html.escape(desc, quote=False) + m.group(3), s, 1, re.S)
    return s


# ---------------------------------------------------------------- figures from the wf7 sheets
def svgs_in(path):
    s = open(path, encoding='utf-8').read()
    return re.findall(r'<svg.*?</svg>', s, re.S)


def fig_first_marks():
    s = open(W7 + '/ancestor/first_marks.svg', encoding='utf-8').read().strip()
    s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)   # its own :root colours and svg background would leak
    s = s.replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" class="fm" role="img" aria-labelledby="fm-t"', 1)
    s = re.sub(r'(<svg[^>]*>)', r'\1<title id="fm-t">The first marks: the 45 signs of the First Tongue, drawn in neither people’s hand.</title>', s, 1)
    s = re.sub(r' width="\d+" height="\d+"', '', s, 1)
    USED.append('fig:first_marks')
    return s


def fig_descent():
    s = open(W7 + '/ancestor/descent.html', encoding='utf-8').read()
    t = re.search(r'<table>.*?</table>', s, re.S).group(0)
    k = [0]

    def plain(m):
        sv = m.group(0)
        k[0] += 1
        if '<defs>' in sv or 'id="' in sv:
            return uniq_ids(fix_mask_ids(sv), 'ds%d-' % k[0])
        if 'class="stone-ink"' in sv:
            return sv
        k[0] += 1
        return sv.replace('<svg ', '<svg aria-hidden="true" ', 1)
    t = re.sub(r'<svg.*?</svg>', plain, t, flags=re.S)
    t = t.replace('<table>', '<table class="descent">', 1)
    USED.append('fig:descent')
    return '<div class="tw descent-w">' + t + '</div>'


def fig_ws(which):
    if which == 'heads':
        sv = svgs_in(W7 + '/orrowen/shots/ws_heads.html')[0]
        sv = uniq_ids(sv, 'wsh-')
        sv = set_title(sv, 'The 27 heads of the dry cut, each as its root sign, cut on its bed and footing.')
    elif which == 'crowns':
        sv = svgs_in(W7 + '/orrowen/shots/ws_crowns_on_tolm.html')[0]
        sv = uniq_ids(sv, 'wsc-')
        sv = set_title(sv, 'The 20 crowns, each set over TOLM, the Stone.')
    elif which == 'prov_hal':
        sv = svgs_in(W7 + '/orrowen/shots/dry_proverb_hal.html')[0]
        sv = set_title(sv, 'The saying both peoples share, in the Hal’s cut: right to left, mirrored, one bed, seven signs.')
    elif which == 'prov_live':
        sv = svgs_in(W7 + '/orrowen/shots/dry_proverb_hal.html')[1]
        sv = set_title(sv, 'The saying both peoples share, in the living dry cut: nine signs.')
    USED.append('ws:' + which)
    return sv


# ---------------------------------------------------------------- the dry cut, rendered by rule
DRY = {
    'title': ('@tum+O.l @varn , @theld+A.th , @mardh , @lunn+A.th , @sollan |', 80.0,
              'The Title of Liberty, cut dry: Memory: home, families, God, freedoms, peace.'),
    'cry': ('@carm @lodh @trun | @tald+a , @ston@ryt+a.n | @cadh+a @tolm @tolm | @ston+a @hald @dask , @tald+a @tald+a @tald+a |', 68.0,
            'The Cry of the Bonded, cut dry: Cries the mortar ground. Rise, Stonewrights! Lay stone stone. Stand wall end, rise! rise! rise!'),
    'tumar': ('@tum+A.r |', 40.0, 'The hearth’s answer, cut dry: We remember. (Yes.)'),
    'seren': ('!@brodh+A.t | !@tul @keth+O.l @gunn =h.a.l.y.n.a |', 80.0,
              'Seren’s untold note, cut dry: Untold. Not yet holding the deep, Halyna.'),
    'calls': ('@marr @trun | @kyl @pedh | @keth , @lusk |', 80.0,
              'The Captain’s three calls, cut dry: Shift ground. Change shot. Hold, loose.'),
    'stonwryt': ('@ston @hald | @cadh+A.n , @tess+A.n , @somm @tolm @tolm | #gate', 80.0,
                 'The Stonwryt, cited dry: Wall stands. We two laid, we two answer, while stone stone. It stands.'),
    'proverb': ('@grest %h , @grest p.a.n.a |', 80.0, 'The saying both peoples share, cut dry: Harm one, harm both.'),
    'invocation': ('@keth @tolm | @cadh @trenn | @amm @cadh+A.t , @tess @odh |', 80.0,
                   'The Invocation’s close, cut dry: Hold stone. Lay tale. When laid, answer hearth.'),
    'creed': ('@gald , !!@gald | @par , !@bosk |', 80.0, 'The Creed, cut dry: Build, not un-build. Guard, not attack.'),
    'word': ('!@hesp , @tolm | !@hurr+O.l , @keth+O.l |', 80.0, 'The guild’s word, cut dry: Not sword, stone. Not killing, keeping.'),
    'coin': ('@somm @tolm @tolm #gate', 40.0, 'The Stonwryt coin’s legend, cut dry: while stone stone. It stands.'),
    'guest': ('@hess , @helv , @senn+O.l', 60.0, 'The Guest’s three words, as they would be cut dry: Stop, sky, dying.'),
    'untold': ('!@brodh+A.t |', 40.0, 'Untold, cut dry: the turned stone and the sign read brodh, with its ending.'),
}
DRYSTATS = {}


DRYN = [0]


def dry(key):
    tok, measure, title = DRY[key]
    DRYN[0] += 1
    s, st = RC.render(tok, measure=measure, title=title, desc='Dry cut tokens: ' + tok, pfx='d%d%s' % (DRYN[0], key[:3]))
    back = RC.read_back(s)
    assert back == ' '.join(tok.split()), (key, back)
    DRYSTATS[key] = st
    USED.append('dry:' + key)
    return s


# ---------------------------------------------------------------- the leaf-hand, set in the Garl Flenn font
INK = {
    'title': 'u.l t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th , o.l m.a.r.dh , o.l l.u.n.n.A.th , o.l s.o.l.l.a.n |',
    'cry1': 'k.a.r.m e.t l.o.dh h.y e.t t.r.u.n | t.a.l.d.a , s.t.o.n.w.r.y.t.a.n | k.a.dh.a t.o.l.m u.m t^S.o.l.m | s.t.o.n.a g.o.r h.a.l.d d.e.m e.t d.a.s.k s.o.s.t ,',
    'cry2': 't.a.l.d.a t.a.l.d.a t.a.l.d.a |',
    'tumar': 't.u.m.A.r |',
    'seren': 'n.a.b^S.r.o.dh.A.t | n.a.th d^N.o.s.s t.u.l k.e.th.O.l e.t g.u.n.n s.y l.o =h.a.l.y.n.a |',
    'calls': 'm.a.r.r th.o t^S.r.u.n | k.y.l th.o p^S.e.dh | k.e.th , e.l.l l.u.s.k |',
    'stonwryt': 'e.s s.t.o.n e.t h.a.l.d s.y | r.e k^S.a.dh.A.n o , e.th t.e.s.s.A.n o , s.o.m.m e.l t.o.l.m t.o.l.m | s.t.o.n | #gate',
    'proverb': 'g.r.e.s.t u.m h.o.s , g.r.e.s.t u.m p^S.a.n.a |',
    'guest': 'h.e.s.s , h.e.l.v , s.e.n.n.O.l',
    'invocation': 'k.e.th e.t t.o.l.m | k.a.dh e.t t.r.e.n.n | a.m.m k.a.dh.A.t o , e.s t^N.e.s.s e.t o.dh |',
    'carver': 'u.l e.t t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th',
}


def ink_markup(tok):
    return TI.tokens_to_markup(tok)


def ink(key, cls='', label=None, tok=None):
    t = tok if tok is not None else INK[key]
    mk = ink_markup(t)
    lab = (' aria-label="%s"' % html.escape(label)) if label else ''
    return '<span class="gf%s" lang="x-orrowen"%s>%s</span>' % ((' ' + cls) if cls else '', lab, html.escape(mk, quote=False))


# the pilots' own token strings: IV.4's frame (its §1.4 block) and I.1's leaf (the Original's tier-3 parse)
def code_block_after(lines, pat):
    i = find(lines, pat)
    j = find(lines, r'^```', i)
    k = find(lines, r'^```', j + 1)
    return lines[j + 1:k]


P4_TOKENS = [l for l in code_block_after(P4, r'^### 1\.4 The leaf-hand') if l.strip()]
I1_PAIRS = []
_rom = None
for l in open(W7 + '/orig/i1_tokens.txt', encoding='utf-8').read().split('\n'):
    if l.startswith('ROM: '):
        _rom = l[5:]
    elif l.startswith('TOK: ') and _rom is not None:
        I1_PAIRS.append((_rom, l[5:]))
        _rom = None


# ---------------------------------------------------------------- tables
SPEC_WORDS = [
    ('the word is in §7.7', 'the word is in the inventory'),
    ('the First Tongue spec §3.2 and §4.4', 'the First Tongue’s roots and derivations'),
    ('their Hal forms are in the First Tongue spec §3.2', 'their Hal forms are in the First Tongue’s roots'),
    ('the First Tongue spec §1.7 (1)', 'the lore call-out, item 1'),
    ('ancestor.md` §1.7 (1)', 'the lore call-out, item 1'),
    ('§14a', ''),
    ('A15 in the new §21.8', 'A15, a new rule'),
    ('A16 in §21.8', 'A16, a new rule'),
    ('§21.8', 'the rules'),
    ('see §3', 'see the collisions above'),
    ('the First Tongue spec §3.3', 'the First Tongue’s reserve'),
    ('the Orrowen spec §5.12', 'the Orrowen suffixes'),
    ('the Orrowen spec §11.4', 'the spec'),
    ('Rewritten in v2 as a joined running hand: §8.', 'Rewritten in v2 as a joined running hand.'),
    ('(An originality law, after the runes: §13.)', '(An originality law, after the runes.)'),
    ('a word not in §7.7', 'a word not in the inventory'),
    ('the §6.6 end rule', 'the end rule'),
    ('the §6.5 bites', 'the bites'),
    ('wf6 §9c\'s list', 'v0.1’s near-call list'),
    ("wf6 §9c's list", 'v0.1’s near-call list'),
    ('(wf6 §11b: tresket by the rule)', '(by the rule, tresket)'),
    ("the spec's §4.3 gives Hal rea", 'v0.1 gave Hal rea'),
    ('(lexicon §8.3 left it open)', '(the lexicon left it open)'),
    (', lexicon §4.3)', ', the lexicon’s seam rule)'),
    ("which §3.6's conjugated prepositions make natural", 'which the conjugated prepositions make natural'),
    ('§3.6 never said', 'the spec never said'),
    ('§3.5 never said', 'the spec never said'),
    ('Same §3.5 gap', 'The same gap'),
    ("the pilot's own §3 collision note", "the pilot's own collision note"),
    ('§6.1 does not allow that', 'the runner rules do not allow that'),
    ("(the part's own gloss, §5.2, which I did not use)", "(the part's own gloss, which I did not use)"),
    ("(§7.3's gloss)", "(the bind's gloss)"),
    ('§11.2 ("a new thing-sign', 'The layout rule ("a new thing-sign'),
    ('clashes with §10.3 ("a thing', 'clashes with the composition rule ("a thing'),
    ('The validator applies §11.2 alone.', 'The validator applied the first alone.'),
    ('§6.1 makes a split one act', 'The runner rules make a split one act'),
    ('§21.8 states the rule', 'The additions state the rule'),
    ("The pilot's §3 findings", "The pilot's findings"),
    ('decode report §4', 'the decode report'),
    ('new · §10.9', 'new · a likeness'),
    ('§10.9', 'a likeness'),
    ('§11.7', 'the saying both peoples share'),
    (' [wf6 originality report §D]', ''),
    ('[wf6 originality report §D]', ''),
    ('The task\'s "sub-rings and ring-splits for clauses" are the', 'The "sub-rings and ring-splits for clauses" are the'),
    ("The task's \"sub-rings and ring-splits for clauses\" are the", 'The "sub-rings and ring-splits for clauses" are the'),
]


def spec_words(s):
    for a, b in SPEC_WORDS:
        s = s.replace(a, b)
    s = re.sub(r'\((?:wf6 )?§[\d.]+[a-z]?: ', '(', s)
    return s


def fixS(s):
    s = spec_words(s)
    s = re.sub(r'\(?§3\.11 (D\d+)\)?', lambda m: ('(' if m.group(0).startswith('(') else '') + m.group(1) + (')' if m.group(0).endswith(')') else ''), s)
    s = re.sub(r'^§6\.7$', 'the punctuation', s)
    s = re.sub(r'\(§[\d.]+: ', '(', s)
    s = strip_refs(s)
    s = s.replace('see §3.5', 'see the pronoun table')
    s = re.sub(r'^§3\.10$', 'the pair-name rule', s)
    s = re.sub(r'^§7\.7$', 'the saying both peoples share; not in the drawing above, it is drawn in §6.7', s)
    s = re.sub(r'\s*\(the number is its row in §7\.7\)', '', s)
    s = spec_words(fixall(s))
    return s


def T(lines, pat, n=0, **kw):
    kw.setdefault('fix', fixS)
    return table(lines, pat, n, **kw)


TABS = {}
# Orrowen v2 (the grammar carried over from wf6, plus the stone grammar)
TABS['s_notes'] = T(S, r'^\*\*Jack.s notes of 2026-09-27', 0)
TABS['s_changed'] = T(S, r'^\*\*What changed from the wf6 spec', 0)
TABS['s_names'] = T(S, r'^## 1 · NAMES', 0)
TABS['s_cons'] = T(S, r'^### 2\.1 Consonants', 0)
TABS['s_vow'] = T(S, r'^### 2\.2 Vowels', 0)
TABS['s_rom'] = T(S, r'^### 2\.4 Romanisation', 0, cols=[0, 1, 2])
TABS['s_phon'] = T(S, r'^### 2\.5 Phonotactics', 0)
TABS['s_num'] = T(S, r'^### 3\.2 Nouns', 0)
TABS['s_harm'] = T(S, r'^### 3\.2 Nouns', 1)
TABS['s_constr'] = T(S, r'^### 3\.2 Nouns', 2)
TABS['s_soft'] = T(S, r'^### 3\.3 The two mutations', 0)
TABS['s_nasal'] = T(S, r'^### 3\.3 The two mutations', 1)
TABS['s_trig'] = T(S, r'^### 3\.3 The two mutations', 2)
TABS['s_pers'] = T(S, r'^### 3\.4 Verbs', 0)
TABS['s_forms'] = T(S, r'^### 3\.4 Verbs', 1)
TABS['s_be'] = T(S, r'^### 3\.4 Verbs', 2)
TABS['s_pron'] = T(S, r'^### 3\.5 Pronouns', 0)
TABS['s_prep'] = T(S, r'^### 3\.6 Prepositions', 0)
TABS['s_idiom'] = T(S, r'^### 3\.7 Having', 0)
TABS['s_pair'] = T(S, r'^### 3\.10 Names', 0)
TABS['s_d2'] = T(S, r'^### 3\.11 The stone grammar', 0)
TABS['s_d5'] = T(S, r'^### 3\.11 The stone grammar', 1)
TABS['s_stages'] = T(S, r'^### 4\.1 Three stages', 0)
TABS['s_economy'] = T(S, r'^### 4\.2 The four hands on the economy', 0)
TABS['s_origin'] = T(S, r'^### 4\.\d Where each trigger', 0)
TABS['s_pnames'] = T(S, r'^### 4\.\d The Shoreland names', 0)
TABS['s_trans'] = T(S, r"^### 4\.\d The Book's translations", 0)
TABS['s_havens'] = T(S, r"^### 4\.\d The Book's translations", 1)
TABS['s_hands'] = T(S, r'^## 0 · THE SHORT VERSION', 0)
TABS['s_upr'] = T(S, r'^### 6\.4 How a letter', 0)
TABS['s_manner'] = T(S, r'^### 6\.4 How a letter', 1)
TABS['s_vowels'] = T(S, r'^### 6\.4 How a letter', 2)
TABS['s_bites'] = T(S, r'^### 6\.5 The bites', 0)
TABS['s_feet'] = T(S, r'^### 6\.5 The bites', 1)
TABS['s_punct'] = T(S, r'^### 6\.7 Punctuation', 0)
TABS['s_numerals'] = T(S, r'^### 6\.8 Stones, lines', 0)
TABS['s_numex'] = T(S, r'^### 6\.8 Stones, lines', 1)
TABS['s_hal'] = T(S, r'^### 6\.9 The first builders', 0)
TABS['s_forms4'] = T(S, r'^### 6\.10 Four ways', 0)
TABS['s_metrics'] = T(S, r'^### 6\.2 Direction', 0)
TABS['s_phrase'] = T(S, r'^### 11\.11 A small phrasebook', 0)
TABS['s_phrase_dry'] = T(S, r'^### 11\.11 A small phrasebook', 1)
TABS['s_nearcall'] = T(S0, r'^### 9c · The audit', 0)
TABS['s_rejected'] = T(S0, r'^### 9b · The originality pass', 0)
# the dry cut
TABS['s_wslaws'] = T(S, r'^### 7\.2 The laws of the word-signs', 0)
TABS['s_wsgeo'] = T(S, r'^### 7\.3 The geometry', 0)
TABS['s_heads'] = T(S, r'^### 7\.4 The heads', 0)
TABS['s_crowns'] = T(S, r'^### 7\.5 The crowns', 0)
TABS['s_wsmarks'] = T(S, r'^### 7\.6 The marks of the dry cut', 0)
TABS['s_when'] = T(S, r'^### 7\.8 When a word is written', 0)
TABS['s_uses'] = T(S, r'^## 9 · WHERE EACH HAND IS USED', 0)
TABS['s_surfaces'] = T(S, r'^## 12 · WHAT THIS GIVES THE BOOK', 0)
# the leaf-hand
TABS['s_pen'] = T(S, r"^### 8\.2 The pen's laws", 0)
TABS['s_lmetrics'] = T(S, r'^### 8\.3 Metrics', 0)
TABS['s_lletters'] = T(S, r'^### 8\.4 The letters, and where', 0)
TABS['s_speed'] = T(S, r'^### 8\.9 How fast it is', 0)
# originality v2
TABS['s_standard'] = T(S, r'^### 13\.1 The standard', 0)
TABS['s_lookalike'] = T(S, r'^### 13\.3 The look-alike screen', 0)
TABS['s_emend'] = T(S, r'^### 14b · With `ancestor\.md`', 0)


def fixM(s):
    s = strip_refs(s)
    s = s.replace(' [canon]', '').replace(' [rule]', '')
    s = re.sub(r'\s*\(Ad §[^)]*\)', '', s)
    s = re.sub(r'\s*\(L\d+[^)]*\)', '', s)
    s = s.replace('Book of Knowings, L1375–1384', 'the Book of Knowings')
    s = re.sub(r'^§5\.7$', 'the Stone out of the Grey', s)
    s = s.replace("(the renderer notes' §10.10 call stands)", "(the renderer's call stands)")
    s = s.replace(' (Mystaeri §3.1)', '')
    s = s.replace(' (now said in §3.13)', '')
    s = s.replace('(already §8.4)', '(already flagged)')
    s = s.replace(' (Shoreland spec)', '')
    s = s.replace(' (D1.9)', '')
    s = s.replace("(T-rule 2)", "(the Admiral's Throne rules)")
    s = s.replace(' (`grain_GIFT.svg`)', ' (the gift, §6.14)')
    s = s.replace('For the Shoreland designer', "A Shoreland word: its Orrowen parts are in the Book's translations (§2.5)")
    return spec_words(fixall(s))


def TM(pat, n=0, **kw):
    kw.setdefault('fix', fixM)
    return table(M, pat, n, **kw)


TABS['m_names'] = TM(r'^## 1 · NAMES', 0)
TABS['m_sounds'] = TM(r'^### 2.1 · Sounds', 0)
TABS['m_knock'] = TM(r'^### 2.3 · The knock', 0)
TABS['m_suff'] = TM(r'^### 2.5 · Word-building', 0)
TABS['m_pron'] = TM(r'^### 2.6 · Grammar', 0)
TABS['m_post'] = TM(r'^### 2.6 · Grammar', 1)
TABS['m_clause'] = TM(r'^### 2.6 · Grammar', 2)
TABS['m_numbers'] = TM(r'^### 2.6 · Grammar', 3)
TABS['m_canon'] = TM(r'^### 2.7 · The canon names', 0)
TABS['m_phrase'] = TM(r'^### 2.8 · Phrasebook', 0)
TABS['m_anat'] = TM(r'^### 3.2 · The round', 0)
TABS['m_files'] = TM(r'^### 3.3 · How a round', 0)
TABS['m_bands'] = TM(r'^### 3.3 · How a round', 1)
TABS['m_roots'] = TM(r'^### 3.5 · The sign inventory', 0, cols=[0, 1, 2, 3, 4])
TABS['m_sapling'] = TM(r'^### 3.5 · The sign inventory', 1)
TABS['m_acts'] = TM(r'^### 3.5 · The sign inventory', 2, cols=[0, 1, 2, 3])
TABS['m_things'] = TM(r'^### 3.5 · The sign inventory', 3, cols=[0, 1, 2, 3, 4])
TABS['m_cond'] = TM(r'^### 3.6 · Condition bands', 0)
TABS['m_dev'] = TM(r'^### 3.7 · Grammar devices', 0)
TABS['m_law'] = TM(r'^### 3.9 · How a carving grows', 0)
TABS['m_tides'] = TM(r'^### 3.9 · How a carving grows', 1)
TABS['m_vocab'] = TM(r'^### 3.9 · How a carving grows', 2)
TABS['m_arrival'] = TM(r'^### 3.13 · Keeping clear', 0)
TABS['m_thrones'] = TM(r'^### 3.14 · Names in the bark', 0)
TABS['m_rest'] = TM(r'^### 3.14 · Names in the bark', 1)
TABS['m_ladder'] = TM(r'^### 4.2 · The ladder', 0)
TABS['m_states'] = TM(r'^### 4.3 · The three states', 0)
TABS['m_blank'] = TM(r'^### 4.4 · The blank wood', 0)
TABS['m_softletters'] = TM(r'^## 6 · APPENDIX A', 0)
TABS['m_rite'] = TM(r'^### 5.3 · The Aelthar', 0)
TABS['m_aelthar_rings'] = TM(r'^### 5.3 · The Aelthar', 1)
TABS['m_sliver'] = TM(r'^### 5.1 · \*We remember', 0)
TABS['m_naelear'] = TM(r'^### 5.2 · \*Naelear\*', 0)
TABS['m_gift'] = TM(r'^### 5.4 · The gift', 0)
TABS['m_hasty'] = TM(r'^### 5.5 · The Hasty seven', 0, cols=[0, 1, 2, 3, 4])
TABS['m_e4'] = TM(r'^### 5.6 · A late-Tide', 0)
TABS['m_stone'] = TM(r'^### 5.7 · The untold leaf', 0)
TABS['m_stages'] = TM(r'^### 5.7 · The untold leaf', 1)

# originality report (wf6) tables
TABS['o_grain'] = table(O, r'^### A1 · The grain', 0, fix=fixM)
TABS['o_shore'] = table(O, r'^### A2 · The course-hand', 0, fix=fixM)
TABS['o_words'] = table(O, r'^### A3 · Words', 0, fix=fixM)
TABS['o_near'] = table(O, r'^## B · Near-calls', 0, fix=fixM)
TABS['o_form'] = table(O, r'^## B · Near-calls', 1, fix=fixM)
TABS['o_clear'] = table(O, r'^## C · Checked and clear', 0, fix=fixM)


# ---- the First Tongue
def fixA(s):
    s = spec_words(s)
    s = strip_refs(s)
    s = s.replace("The mystaeri spec's analysis of thael as thae + \\*-l is replaced.",
                  "The earlier analysis of <em>thael</em> as <em>thae</em> + an old <em>-l</em> is replaced.")
    s = s.replace('(mystaeri spec §2.3)', '')
    s = s.replace('(shoreland spec §4.4)', '')
    return spec_words(fixall(s))


def TA(pat, n=0, **kw):
    kw.setdefault('fix', fixA)
    return table(A, pat, n, **kw)


TABS['a_kept'] = TA(r'^### 1\.3 What each people kept', 0)
TABS['a_kin'] = TA(r'^### 1\.5 The kinship', 0)
for k, n in (('a_title', 0), ('a_tumar', 1), ('a_sliver', 2), ('a_prov_o', 3), ('a_prov_s', 4),
             ('a_stonwryt', 5), ('a_guest_o', 6), ('a_guest_s', 7)):
    TABS[k] = TA(r'^### 1\.6 Four sayings', n)
TABS['a_cons'] = TA(r'^### 2\.1 Consonants', 0)
TABS['a_catch'] = TA(r'^### 2\.3 The catch', 0)
TABS['a_lawO1'] = TA(r'^### 4\.1 From the first tongue to Orrowen', 0)
TABS['a_lawO2'] = TA(r'^### 4\.1 From the first tongue to Orrowen', 1)
TABS['a_lawS1'] = TA(r'^### 4\.2 From the first tongue to Seilrhass', 0)
TABS['a_lawS2'] = TA(r'^### 4\.2 From the first tongue to Seilrhass', 1)
TABS['a_irreg'] = TA(r'^### 4\.3 The principled irregularities', 0)
TABS['a_marks'] = TA(r'^### 5\.2 The marks', 0)
TABS['a_formC'] = TA(r'^### 5\.3 The laws of form', 0)
TABS['a_formG'] = TA(r'^### 5\.3 The laws of form', 1)
TABS['a_letters'] = TA(r'^### 5\.4 Every course-hand letter', 0)
TABS['a_lvowels'] = TA(r'^### 5\.4 Every course-hand letter', 1)
TABS['a_lmarks'] = TA(r'^### 5\.4 Every course-hand letter', 2)
TABS['a_gsigns'] = TA(r'^### 5\.5 Every grain sign', 0)
TABS['a_gbands'] = TA(r'^### 5\.5 Every grain sign', 1)
TABS['a_gdev'] = TA(r'^### 5\.5 Every grain sign', 2)
TABS['a_seren_parts'] = TA(r'^## 6 · SEREN', 0)
TABS['a_seren_der'] = TA(r'^## 6 · SEREN', 1)


def labelled_tables(lines, start_pat, end_pat, fix, open_first=False, cls=None):
    """Each table between two headings, in a <details>, labelled by the bold line above it."""
    i = find(lines, start_pat)
    end = find(lines, end_pat, i + 1)
    out, k, total = [], 0, 0
    for h, rows, idx in tables_after(lines, i):
        if idx > end:
            break
        j = idx - 1
        while j > i and not lines[j].strip():
            j -= 1
        lab = lines[j].strip()
        m = re.match(r'^\*\*(.+?)\*\*(.*)$', lab)
        lab = (m.group(1) + (m.group(2).split('.')[0] if m and len(m.group(2)) < 30 else '')) if m else lab
        lab = re.sub(r'\s*\(\d+\)\s*$', '', lab).strip().rstrip('.')
        total += len(rows)
        out.append('<details class="lex"%s><summary>%s <span class="n">%d</span></summary>%s</details>'
                   % (' open' if (k == 0 and open_first) else '', inline(fix(lab)), len(rows),
                      render(h, rows, fix=fix, cls=cls)))
        k += 1
    return '\n'.join(out), total


ROOTS_INH, N_ROOTS_INH = labelled_tables(A, r'^### 3\.2 The inherited roots', r'^### 3\.3', fixA)
ROOTS_RES, N_ROOTS_RES = labelled_tables(A, r'^### 3\.3 The reserve roots', r'^## 4 ·', fixA)
DER_O, N_DER_O = labelled_tables(A, r'^### 4\.4 Every Orrowen word', r'^### 4\.5', fixA)
DER_S, N_DER_S = labelled_tables(A, r'^### 4\.5 Every Seilrhass word', r'^### 4\.6', fixA)


# ---- the grain v2
def fixG(s):
    s = spec_words(s)
    s = re.sub(r'^§[\d.]+\s+', '', s)
    s = re.sub(r'^§10\.9$', 'a likeness', s)
    s = re.sub(r'^§9\.2$', 'no new sign', s)
    s = re.sub(r'^§[\d.]+$', '', s)
    s = strip_refs(s)
    s = s.replace('(`grain_GIFT.svg`)', '')
    s = re.sub(r'\s*\(v1 §[\d.]+[^)]*\)', ' [v1]', s)
    s = re.sub(r'v1 §[\d.]+', 'v1', s)
    return spec_words(fixall(s))


def TG(pat, n=0, **kw):
    kw.setdefault('fix', fixG)
    return table(G, pat, n, **kw)


TABS['g_ask'] = TG(r'^### 1\.1 The ask, as constraints', 0)
TABS['g_changes'] = TG(r'^### 2\.2 What v2 changes', 0, cols=[0, 1])
TABS['g_law'] = TG(r'^## 3 · THE LAW OF THE RINGS', 0)
TABS['g_levels'] = TG(r'^### 4\.1 Levels', 0)
TABS['g_elems'] = TG(r'^### 5\.1 New element types', 0)
TABS['g_parts'] = TG(r'^### 5\.2 The part device', 0)
TABS['g_fringe'] = TG(r'^### 5\.4 The fringe', 0)
TABS['g_roles'] = TG(r'^### 6\.1 What a runner is', 0)
TABS['g_rays'] = TG(r'^### 6\.4 Rays, memory and ties', 0)
TABS['g_small'] = TG(r'^### 6\.5 Where the small words went', 0)
TABS['g_pass'] = TG(r'^### 7\.1 Pass and break', 0)
TABS['g_braid'] = TG(r'^### 7\.2 Braids', 0)
TABS['g_pockets'] = TG(r'^## 8 · POCKETS', 0)
TABS['g_recut'] = TG(r'^### 9\.4 The look check', 0)
TABS['g_pairs'] = TG(r'^### 9\.4 The look check', 1)
TABS['g_layouts'] = TG(r'^### 11\.1 The answer', 0)
TABS['g_leaves'] = TG(r'^### 11\.3 The eight wood leaves', 0)
TABS['g_sizes'] = TG(r'^### 11\.6 Sizes and budgets', 0)
TABS['g_iv6files'] = TG(r'^### 12\.1 Its files', 0)
TABS['g_tokens'] = TG(r'^### 13\.3 Tokens, at a glance', 0, cols=[0, 1])
TABS['g_arrival'] = TG(r'^## 15 · KEEPING CLEAR', 0)
TABS['g_ladder'] = TG(r'^## 16 · THE LADDER v2', 0)
TABS['g_compounds'] = TG(r'^### 21\.7 Compounds added by the IV\.4 pilot', 0, cols=[0, 1, 2, 4])
TABS['g_a15'] = TG(r'^### 21\.8 Additions from the IV\.4 blind', 0)
G_NEW, N_G_NEW = labelled_tables(G, r'^### 9\.2 The 47 new signs', r'^### 9\.3', fixG, open_first=True)
G_COV = render(*tables_after(G, find(G, r'^## 18 · COVERAGE'))[0][:2], fix=fixG)
N_G_COV = len(tables_after(G, find(G, r'^## 18 · COVERAGE'))[0][1])


def gn_block(lines, pat):
    return '\n'.join(code_block_after(lines, pat))


GN_IV6 = gn_block(G, r'^### 12\.2 Its Grain Notation v2')
GN_E401_V2 = code_block_after(G, r'^\*\*Example: E4-01\*\*')
GN_E401_V2 = '\n'.join(GN_E401_V2)
GN_AELTHAR_BIND = None
_i = find(G, r'^- AELTHAR: the same, plus one optional enrichment')
_j = find(G, r'```', _i)
_k = find(G, r'```', _j + 1)
GN_AELTHAR_BIND = '\n'.join(l[4:] if l.startswith('    ') else l for l in G[_j + 1:_k])


# ---- the tier-3 lexicon summary, the pilots, the back-translations
def fixL(s):
    s = spec_words(s)
    s = re.sub(r'^§[\d.]+$', '', s)
    s = strip_refs(s)
    s = s.replace('(orrowen_v2 §3.11 (D1–D11) and §7.8)', '')
    return spec_words(fixall(s))


def TL(lines, pat, n=0, **kw):
    kw.setdefault('fix', fixL)
    return table(lines, pat, n, **kw)


TABS['l_land'] = TL(LX, r'^### 3\.2 Where the Book', 0)
TABS['l_kinds'] = TL(LX, r'^### 4\.1 From the roots only', 0)
TABS['l_patterns'] = TL(LX, r'^### 4\.2 The derivational patterns', 0)
TABS['l_place'] = TL(LX, r'^### 5\.1 Prepositions and adverbs', 0)
TABS['l_time'] = TL(LX, r'^### 5\.2 Time, manner, quantity', 0)
TABS['l_grammar'] = TL(LX, r'^### 5\.3 What the grammar carries', 0)
TABS['l_chisel'] = TL(LX, r'^## 6 · THE CHISEL REGISTER', 0)
TABS['l_traps'] = TL(LX, r'^## 8 · FINDINGS FOR JACK', 0)
TABS['p1_grammar'] = TL(P1, r'^### 2\. Grammar this leaf had to settle', 0)
TABS['p1_diff'] = TL(P1, r'^### 4\. Where the Orrowen is built differently', 0)
TABS['p1_adds'] = TL(P1, r'^## LEXICON ADDITIONS', 0, cols=[1, 2, 4, 5, 6])
TABS['b1_compare'] = TL(B1, r'^## 3 · The comparison', 0, cols=[0, 2, 3, 4])
TABS['b1_fixes'] = TL(B1, r'^### 4\.1 Translation', 0)
TABS['p4_files'] = TL(P4, r'^### 2\.1 The round and its files', 0)
TABS['b4_brief'] = TL(B4, r'^## 0 · The result in brief', 0)
TABS['b4_frame'] = TL(B4, r'^### 3\.1 The frame', 0)
TABS['b4_grain'] = TL(B4, r'^### 3\.2 The grain', 0)
TABS['b4_causes'] = TL(B4, r'^## 4 · Causes and fixes', 0, cols=[0, 1, 2, 3])


def ring_block(pat):
    return '\n'.join(code_block_after(P4, pat))


P4_R1 = ring_block(r'^\*\*Ring 1\*\*')
P4_R9 = ring_block(r'^\*\*Ring 9\*\*')
P4_R12 = ring_block(r'^\*\*Ring 12\*\*')


# ---------------------------------------------------------------- lexicons (the canon ones, as in v0.1)
def lex_shore():
    out = []
    i = find(S, r'^## 5 · LEXICON')
    heads = [j for j in range(i, find(S, r'^## 6 · THE COURSE-HAND')) if S[j].startswith('### 5.')]
    for k, j in enumerate(heads):
        title = re.sub(r'^### 5\.\d+\s*', '', S[j])
        h, rows, _ = tables_after(S, j)[0]
        out.append('<details class="lex"%s><summary>%s <span class="n">%d</span></summary>%s</details>'
                   % (' open' if k == 0 else '', inline(title), len(rows), render(h, rows, fix=fixS)))
    return '\n'.join(out)


def lex_myst():
    out = []
    i = find(M, r'^### 2.9 · Lexicon')
    end = find(M, r'^### 2.10 · Audit')
    k = 0
    for h, rows, idx in tables_after(M, i):
        if idx > end:
            break
        lab = M[idx - 2].strip().strip('*')
        out.append('<details class="lex"%s><summary>%s <span class="n">%d</span></summary>%s</details>'
                   % (' open' if k == 0 else '', inline(lab), len(rows), render(h, rows, fix=fixM)))
        k += 1
    return '\n'.join(out)


def count_lex():
    n1 = 0
    i = find(S, r'^## 5 · LEXICON')
    for j in range(i, find(S, r'^## 6 · THE COURSE-HAND')):
        if S[j].startswith('### 5.'):
            n1 += len(tables_after(S, j)[0][1])
    n2 = 0
    i = find(M, r'^### 2.9 · Lexicon')
    end = find(M, r'^### 2.10 · Audit')
    for h, rows, idx in tables_after(M, i):
        if idx < end:
            n2 += len(rows)
    return n1, n2


# ---------------------------------------------------------------- the tier-3 lexicon, whole, grouped by field
sys.path.insert(0, W7 + '/ancestor')
import roots_core as RCORE  # noqa: E402

FIELDS = [('stone', 'Stone, wood and building'), ('bond', 'Faith, bond and kin'), ('hearth', 'Hearth and people'),
          ('war', 'The wall, the war, the sea-road'), ('sea', 'Sea, land and growing things'),
          ('sky', 'Sky, weather, fire and time'), ('body', 'Body, life and feeling'),
          ('speech', 'Speech, writing and mind'), ('acts', 'Other acts'), ('quality', 'Qualities'),
          ('number', 'Numbers'), ('small', 'Small words and set phrases'), ('affix', 'Affixes'),
          ('names', 'Names, places and loans')]
SRCMARK = {'canon': ('C', 'canon'), 'reserve': ('R', 'a reserve root of the First Tongue'),
           'tier3': ('T', 'made for the Book'), 'tier3-sys': ('·', 'made by rule')}


def olex():
    F = {}
    for r in RCORE.ROOTS:
        for part in r['root'].split('/'):
            F[part.strip().strip('*').strip()] = r['field']
        F[r['root']] = r['field']
    for r in json.load(open(W7 + '/ancestor/reserve.json', encoding='utf-8')):
        F[r['root'].strip('*')] = r['field']
    rows = list(csv.DictReader(open(W7 + '/lexicon_orrowen.tsv', encoding='utf-8'), delimiter='\t'))
    byword = {}
    groups = {k: [] for k, _ in FIELDS}
    counts = {'src': {}, 'logo': 0, 'n': len(rows)}

    def field_of(r):
        pos = r['pos']
        if 'name' in pos or 'loan' in pos or r['root'].startswith('(Seilrhass)'):
            return 'names'
        if pos.startswith('suf') or pos == 'pref':
            return 'affix'
        if pos.split(',')[0] == 'num':
            return 'number'
        roots = [x.strip().lstrip('*') for x in r['root'].split(',') if x.strip()]
        fs = [F.get(x) for x in roots]
        if '^' in r['formation'] and len(fs) >= 2 and fs[-1]:
            return fs[-1]
        good = [f for f in fs if f and f not in ('small', 'affix')]
        if good:
            return good[0]
        if fs and fs[0]:
            return fs[0]
        base = re.split(r'[+^ ]', r['formation'])[0].strip('-') if r['formation'] else ''
        return byword.get(base, 'small')
    for r in rows:
        f = field_of(r)
        if f == 'affix' and not r['pos'].startswith('suf'):
            f = 'small'
        byword.setdefault(r['orrowen'], f)
        groups.setdefault(f, []).append(r)
        counts['src'][r['source']] = counts['src'].get(r['source'], 0) + 1
        if r['logogram']:
            counts['logo'] += 1

    def cell_from(r):
        d = r['derivation']
        if r['source'] == 'tier3-sys':
            d = re.sub(r" '[^']*'", '', d)
            d = re.sub(r" \(('[^)]*'|[^)]*)\)$", '', d)
        d = re.sub(r'\s*\(reserve, ancestor §3\.3\)', ' (reserve)', d)
        d = fixall(d)
        d = re.sub(r',?\s*§[\d.]+[a-z]?', '', d)
        d = re.sub(r'\(\s*\)', '', d)
        d = re.sub(r'\s*\(?(?:ancestor|orrowen_v2|lexicon_orrowen)[^;)]*§[\d.]+\)?', '', d)
        d = d.replace('; pilot I.1', '').replace('pilot I.1', 'I.1 pilot')
        return d
    out = []
    for k, lab in FIELDS:
        rs = groups.get(k, [])
        if not rs:
            continue
        body = ['<div class="tw"><table class="olex"><tr><th>Orrowen</th><th>Hal</th><th>pos · cl.</th><th>Sense</th>'
                '<th>From</th><th>Dry cut</th><th></th></tr>']
        for r in rs:
            mark, why = SRCMARK.get(r['source'], ('', ''))
            hal = ('<i>%s</i>' % html.escape(r['hal'])) if r['hal'] else ''
            logo = html.escape(r['logogram']) if r['logogram'] else ('<span class="dim">%s</span>' % html.escape(
                'left out' if r['dry_cut'] == 'left out' else 'letters'))
            body.append('<tr%s><td><b>%s</b></td><td>%s</td><td>%s · %s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                        % (' class="cn"' if r['source'] == 'canon' else '', html.escape(r['orrowen']), hal,
                           html.escape(r['pos']), html.escape(r['class']), inline(re.sub(r'\s*\(§[\d.]+\)', '', r['meanings'])),
                           inline(cell_from(r)), logo, mark))
        body.append('</table></div>')
        out.append('<details class="lex"><summary>%s <span class="n">%d</span></summary>%s</details>'
                   % (html.escape(lab), len(rs), '\n'.join(body)))
    return '\n'.join(out), counts


OLEX, OLEX_COUNTS = olex()


# ---------------------------------------------------------------- the 328 word-signs, as centre-lines
WS = json.load(open(W7 + '/orrowen/wordstones.json', encoding='utf-8'))
HEAD_ORDER = []
for v in WS.values():
    if v['head'] not in HEAD_ORDER:
        HEAD_ORDER.append(v['head'])


def ws_glyph(key, v, big=False):
    d = []
    for st in v['strokes']:
        d.append('M' + ' '.join('%s %s' % (('%g' % round(x, 2)), ('%g' % round(-y, 2))) for x, y in st))
    d = re.sub(r'(?<=[ M])(-?)0\.', r'\1.', ''.join(d))
    lab = ('role="img" aria-label="the word-sign read %s"' % html.escape(key)) if big else 'aria-hidden="true"'
    return ('<svg class="wsg%s" viewBox="-.1 -4.95 4.6 5.75" %s><path class="ft" d="M.3 .11H4.1M.3 .53H4.1"/><path d="%s"/></svg>'
            % (' big' if big else '', lab, d))


def ws_inventory():
    out = []
    heads_meta = {}
    i = find(S, r'^### 7\.7 The inventory')
    for j in range(i, find(S, r'^### 7\.8')):
        m = re.match(r'^\*\*([A-Z]+)\*\* \((.*); (\d+) signs?\)$', S[j])
        if m:
            heads_meta[m.group(1)] = (m.group(2), int(m.group(3)))
    for h in HEAD_ORDER:
        items = sorted([(k, v) for k, v in WS.items() if v['head'] == h], key=lambda kv: kv[1]['n'])
        mark, n = heads_meta.get(h, ('', len(items)))
        assert n == len(items), (h, n, len(items))
        rows = ['<div class="tw"><table class="wsinv"><tr><th>no.</th><th>sign</th><th>reads</th><th>sense</th>'
                '<th>parts</th><th>cl.</th><th>why</th><th>src</th></tr>']
        for k, v in items:
            parts = v['head'] + ('+' + v['crown'] if v['crown'] else '')
            rows.append('<tr><td>%d</td><td>%s</td><td><b class="orr">%s</b></td><td>%s</td><td><code>%s</code></td>'
                        '<td>%s</td><td>%s</td><td>%s</td></tr>'
                        % (v['n'], ws_glyph(k, v), html.escape(k), inline(v['gloss']), parts, v['cls'],
                           inline(v['why']), v['src']))
        rows.append('</table></div>')
        out.append('<details class="lex"><summary>%s <span class="n">%s · %d</span></summary>%s</details>'
                   % (h, inline(fixall(mark)), len(items), '\n'.join(rows)))
    return '\n'.join(out)


WSINV = ws_inventory()
assert len(WS) == 328


# ---------------------------------------------------------------- the font specimen
LETTER_ROWS = [('the lips: the prop, leaning forward', 'p b m f v w'),
               ('the tongue-tip: the offset, stepped', 't d n th dh s l r rh'),
               ('the back: the shore, leaning back', 'k g h'),
               ('the vowels, and the two harmonic letters', 'a o u e i y A O')]


def font_letters():
    out = []
    for lab, letters in LETTER_ROWS:
        cells = []
        for L in letters.split():
            tok = L
            mk = ink_markup(tok)
            cells.append('<div class="gcell"><span class="gf" lang="x-orrowen">%s</span><small>%s</small></div>'
                         % (html.escape(mk, quote=False), html.escape(L)))
        out.append('<div class="gfam">%s</div><div class="ggrid">%s</div>' % (html.escape(lab), ''.join(cells)))
    return '\n'.join(out)


# ---------------------------------------------------------------- geometry tables (as v0.1)
def fmt(p):
    return '(%s,%s)' % tuple(('%g' % v) for v in p)


def geo_shore():
    d = json.loads(re.search(r'```json\n(\{\n  "metrics".*?)\n```', SRAW, re.S).group(1))
    rows = []
    for k, v in d['consonants'].items():
        rows.append([k, v['place'], v['manner'], ' · '.join('–'.join(fmt(p) for p in st) for st in v['strokes'])])
    for k, v in d['vowels'].items():
        rows.append([k, 'vowel', 'harmonic' if k in 'AO' else ('broad' if k in 'aou' else 'slender'),
                     ' · '.join('–'.join(fmt(p) for p in st) for st in v['strokes'])])
    for k, v in d['archaic_hal_only'].items():
        rows.append([k + ' (Hal)', v['place'], v['manner'], ' · '.join('–'.join(fmt(p) for p in st) for st in v['strokes'])])
    for k in ('perpend', 'wedge', 'gate', 'coping'):
        v = d['marks'][k]
        rows.append([k, 'mark', 'width %g u' % v['width'], ' · '.join('–'.join(fmt(p) for p in st) for st in v['strokes'])])
    rows.append(['S bite', 'bite', 'under the foot', '–'.join(fmt(p) for p in d['marks']['bite_S']) + ' (x from the foot)'])
    rows.append(['N bite', 'bite', 'under the foot', '–'.join(fmt(p) for p in d['marks']['bite_N']) + ' (x from the foot)'])
    h = ['Letter', 'Place / kind', 'Manner / class', 'Strokes (cell units, y up, from the left foot on the bed)']
    esc = [[c.replace('<', '&lt;') for c in r] for r in rows]
    out = ['<div class="tw"><table class="geo"><tr>' + ''.join('<th>%s</th>' % c for c in h) + '</tr>']
    for r in esc:
        out.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td class="mono">%s</td></tr>' % tuple(r))
    out.append('</table></div>')
    return '\n'.join(out)


def el_text(e):
    t = e['t']
    if t == 'cut':
        s = 'cut ' + '→'.join(fmt(p) for p in e['p'])
        for k in ('bend', 'k'):
            if k in e:
                s += ' %s %g' % (k, e[k])
        if 'curl' in e:
            c = e['curl']
            s += ' curl r %g, %g° %s%s' % (c['r'], c['sweep'], 'cw' if c['dir'] > 0 else 'ccw',
                                           (', tail %g' % c['tail']) if 'tail' in c else '')
        for k in ('straight', 'fill', 'hollow', 'smooth', 'curve'):
            if e.get(k):
                s += ' ' + {'fill': 'solid', 'curve': 'smooth curve'}.get(k, k)
        return s
    if t == 'bar':
        return 'bar across at u %g, v %g…%g' % (e['u'], e['v0'], e['v1'])
    if t == 'ringarc':
        return 'ring-arc at u %g, v %g…%g' % (e['u'], e['v0'], e['v1'])
    if t == 'star':
        return 'star-notch at %s, r %g' % (fmt(e['c']), e['r'])
    if t == 'lens':
        s = 'lens at %s, length %g, width %g' % (fmt(e['c']), e['len'], e['w'])
        if 'rot' in e:
            s += ', turned %g°' % e['rot']
        if e.get('across'):
            s += ', across the file'
        if e.get('fill'):
            s += ', solid'
        return s
    if t == 'drop':
        return 'drop at %s, length %g, width %g, point %s' % (fmt(e['c']), e['len'], e['w'], e['point'])
    if t == 'square':
        return 'square at %s, side %g' % (fmt(e['c']), e['s'])
    if t == 'wedge':
        return 'wedge, apex %s, base u %g, width %g' % (fmt(e['apex']), e['base'], e['w'])
    if t == 'tri':
        return 'triangle ' + ' '.join(fmt(p) for p in e['p'])
    if t == 'check':
        return 'check u %g→%g at v %g, width %g' % (e['u0'], e['u1'], e['v'], e['w'])
    if t == 'scar':
        return 'fire scar, apex %s, base u %g, width %g' % (fmt(e['apex']), e['base'], e['w'])
    if t == 'knot':
        return 'knot at %s, rx %g B, ru %g L' % (fmt(e['c']), e['rx'], e['ru'])
    if t == 'cup':
        return 'cup at %s, r %g, form %s' % (fmt(e['c']), e['r'], e['form'])
    if t == 'rootfoot':
        return 'root-foot at %s, %s' % (fmt(e['c']), 'outward' if e['dir'] == 'out' else 'at the foot')
    if t == 'punch':
        return 'punch at %s, r %g' % (fmt(e['c']), e['r'])
    raise ValueError(t)


def geo_table(d):
    h = ['Sign', 'Class', 'Soft reading', 'Elements (u along the file 0→1, v across it in B, + clockwise)', 'Nick']
    out = ['<div class="tw"><table class="geo"><tr>' + ''.join('<th>%s</th>' % c for c in h) + '</tr>']
    for k, v in d.items():
        cls = v['cls'] + ((' · ' + v['q']) if 'q' in v else '')
        out.append('<tr><td><strong>%s</strong></td><td>%s</td><td><em>%s</em></td><td class="mono">%s</td><td>%s</td></tr>'
                   % (k, cls, v['soft'], ' · '.join(el_text(e) for e in v['els']), 'yes' if v.get('nick') else '—'))
    out.append('</table></div>')
    return '\n'.join(out), len(d)


GEO_GRAIN, NSIGNS = geo_table(json.loads(re.search(r'```json\n(\{\n "WAVE".*?)\n```', MRAW, re.S).group(1)))
assert NSIGNS == 70
GEO_GRAIN2, NSIGNS2 = geo_table(json.loads(re.search(r'```json\n(\{\n "WOOD".*?)\n```', GRAW, re.S).group(1)))
assert NSIGNS2 == 47, NSIGNS2

NLEX_S, NLEX_M = count_lex()
N = {'lex_s': NLEX_S, 'lex_m': NLEX_M, 'olex': OLEX_COUNTS['n'], 'olex_logo': OLEX_COUNTS['logo'],
     'olex_canon': OLEX_COUNTS['src'].get('canon', 0), 'olex_reserve': OLEX_COUNTS['src'].get('reserve', 0),
     'olex_t3': OLEX_COUNTS['src'].get('tier3', 0), 'olex_sys': OLEX_COUNTS['src'].get('tier3-sys', 0),
     'roots_inh': N_ROOTS_INH, 'roots_res': N_ROOTS_RES, 'der_o': N_DER_O, 'der_s': N_DER_S,
     'g_new': N_G_NEW, 'g_cov': N_G_COV}


# ---------------------------------------------------------------- assemble
def sub(m):
    kind, arg = m.group(1), (m.group(2) or '').strip()
    if kind in SVGDIRS:
        a = arg.split()
        return svg(kind, a[0], suffix=a[2] if len(a) > 2 and a[1] == 'as' else None)
    if kind == 'tab':
        return TABS[arg]
    if kind == 'lex':
        return lex_shore() if arg == 'shore' else lex_myst()
    if kind == 'geo':
        return {'shore': geo_shore, 'grain': lambda: GEO_GRAIN, 'grain2': lambda: GEO_GRAIN2}[arg]()
    if kind == 'n':
        return '{:,}'.format(N[arg]) if N[arg] >= 1000 else str(N[arg])
    if kind == 'dry':
        return dry(arg)
    if kind == 'ink':
        a = arg.split(None, 1)
        return ink(a[0], cls=a[1] if len(a) > 1 else '')
    if kind == 'inkp4':
        return ink(None, tok=P4_TOKENS[int(arg)])
    if kind == 'inki1':
        return ink(None, tok=I1_PAIRS[int(arg)][1])
    if kind == 'romi1':
        return html.escape(I1_PAIRS[int(arg)][0])
    if kind == 'fig':
        return {'first_marks': fig_first_marks, 'descent': fig_descent}[arg]() if arg in ('first_marks', 'descent') else fig_ws(arg)
    if kind == 'wsinv':
        return WSINV
    if kind == 'wsg':
        return ws_glyph(arg, WS[arg], big=True)
    if kind == 'olex':
        return OLEX
    if kind == 'block':
        return {'roots_inh': ROOTS_INH, 'roots_res': ROOTS_RES, 'der_o': DER_O, 'der_s': DER_S,
                'g_new': G_NEW, 'g_cov': G_COV, 'font_letters': font_letters()}[arg]
    if kind == 'gn':
        return html.escape({'iv6': GN_IV6, 'e401v2': GN_E401_V2, 'aelthar_bind': GN_AELTHAR_BIND,
                            'p4r1': P4_R1, 'p4r9': P4_R9, 'p4r12': P4_R12}[arg], quote=False)
    raise KeyError(kind)


# ---------------------------------------------------------------- section numbers on internal links
def number_ids(b):
    """Map every id to the number of the heading it sits under (h2 'N', h3 'N.M')."""
    heads = []
    for m in re.finditer(r'<h2[^>]*>\s*<span class="n">(\d+)</span>', b):
        heads.append((m.start(), 2, m.group(1)))
    for m in re.finditer(r'<h3[^>]*>\s*(\d+\.\d+) ·', b):
        heads.append((m.start(), 3, m.group(1)))
    for m in re.finditer(r'<h3[^>]*>(?!\s*\d+\.\d+ ·)', b):
        heads.append((m.start(), 3, None))
    heads.sort()
    nums = {}
    for m in re.finditer(r'<(\w+)[^>]*\bid="([^"]+)"', b):
        tag, i, p = m.group(1), m.group(2), m.start()
        if tag in ('section', 'article'):
            nxt = [h for h in heads if h[0] > p and h[1] == (2 if tag == 'section' else 3)]
            nums[i] = nxt[0][2] if nxt else None
            continue
        cur2 = cur3 = None
        for hp, lv, n in heads:
            if hp > p:
                break
            if lv == 2:
                cur2, cur3 = n, None
            else:
                cur3 = n
        nums[i] = cur3 or cur2
    return nums


def check_numbering(b):
    """h3 numbers must run 1, 2, 3 … inside each h2, and each h2 number must follow the last."""
    errs = []
    last2, last3 = 0, 0
    for m in re.finditer(r'<h2[^>]*>\s*<span class="n">(\d+)</span>|<h3[^>]*>\s*(\d+)\.(\d+) ·', b):
        if m.group(1):
            n = int(m.group(1))
            if n != last2 + 1:
                errs.append('h2 %d after %d' % (n, last2))
            last2, last3 = n, 0
        else:
            a, c = int(m.group(2)), int(m.group(3))
            if a != last2 or c != last3 + 1:
                errs.append('h3 %d.%d (in %d, after .%d)' % (a, c, last2, last3))
            last3 = c
    return errs


def fix_refs(b):
    nums = number_ids(b)
    changed = []

    def rep(m):
        i, text = m.group(1), m.group(2)
        n = nums.get(i)
        if n is None:
            return m.group(0)
        new = '§' + n
        if new != text:
            changed.append((i, text, new))
        return '<a href="#%s">%s</a>' % (i, new)
    b = re.sub(r'<a href="#([^"]+)">(§[\d.]+)</a>', rep, b)
    return b, changed, nums


PARTS = ('p0.html', 'p_anc.html', 'p1.html', 'p_dry.html', 'p2.html', 'p_g2.html', 'p3.html', 'p_t3.html', 'p4.html')
body = ''
for part in PARTS:
    body += open(os.path.join(HERE, part), encoding='utf-8').read()

body = re.sub(r'\{\{(\w+)\s+([^}]*)\}\}|\{\{(\w+)\}\}',
              lambda m: sub(m) if m.group(1) else sub(re.match(r'(\w+)()', m.group(3))), body)
errs = check_numbering(body)
assert not errs, errs
body, CHANGED, NUMS = fix_refs(body)
for c in CHANGED:
    print('ref fixed', c)
assert '{{' not in body, re.findall(r'\{\{[^}]*\}\}', body)[:5]

html_out = HEAD + '<body>\n' + body + '</body>\n</html>\n'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html_out)
print('wrote', OUT, len(html_out) // 1024, 'KB;', len(USED), 'drawings;', 'lexicons', NLEX_S, NLEX_M, OLEX_COUNTS)
print('dry-cut stats', {k: (v['signs'], v['bytes']) for k, v in DRYSTATS.items()})
