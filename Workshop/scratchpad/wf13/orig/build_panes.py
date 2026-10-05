#!/usr/bin/env python3
"""build_panes.py (wf12 scratch; never goes into Docs/) -- the story page's ORIGINAL tab, as data for the page builder.

    python3 build_panes.py            -> wf12/orig/panes.json, panes.css, panes_report.md (+ panes_build.log)

For every leaf of THE LEGENDS OF RIVENKEEP, Book v3.0.0 (wf11/book_v3.md), in the Book's order, the Original pane as a
list of blocks ALIGNED to the Book's paragraphs: one block per Book paragraph, each carrying its Book line numbers and
its Book text so the page builder can match it to its own block.  The Orrowen comes from the merged, validated units
(wf12/units/*.md), each Book paragraph paired with its one unit item exactly as the merge's coverage pass pairs them
(wf12/merge/coverage2.py: an Orrowen blockquote, or a ring's code block, whose English is that paragraph character for
character).  The markup and its classes are the old Original page's (wf8/out/Rivenkeep_Legends_Original.html, built by
build_original.py, which Jack saw and liked):

  * a stone paragraph in Seren's ink, the leaf-hand Garl Flenn (ink.py markup), with a quiet no-script <details> fold
    giving its romanisation (div.ip > p.ink + details.tr.rom);
  * Halyna's paragraphs and the wood leaves' READING lines in their two inks (data-voice="a" | "b"), as the Book sets
    them (wf12/merge/halyna_check.py's reading of the Book's markers, which the merge found the units carry);
  * a wood story paragraph as its ring plate (the ring drawn alone, figure.native.plate) with its Grain Notation fold
    (the unit's knowing-form ring) and its literal reading;
  * the whole round at the seal (This is held in the grain.), where the old Original set it; the seal is the bark's,
    not a ring, and the round's fold says so;
  * the carvings the stone leaves hold (V.1, V.2, V.7, VI.3, the Epilogue's Stone, the Book of Knowings) as their own
    rounds; the Title and the Stonwryt also cut dry (the old page's dry cuts, re-used: the canon lines are unchanged);
  * native drawings as in the Book (wf6/svg), at their places.

Drawings are NOT inlined in panes.json: each stands as an empty slot,
    <span class="svg-slot" data-svg3="KEY" data-title="..."></span>      (wf12/orig/svg3/KEY.svg, by make_grain3.py)
    <span class="svg-slot" data-native="ID" data-title="..."></span>     (wf6/svg/ID.svg, the Book's own drawing)
and panes_lib.py fills them (inline, with svgpool's shared symbols, or as <img>), so one drawing set inline once per
place keeps unique ids on the page.  The leaf-hand font is embedded once, base64, in panes.css.
"""
import base64
import collections
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(os.path.dirname(HERE))
W12 = os.path.join(S, 'wf12')          # wf13: the merge and the units are wf12's, read only (v3.0.0 stays untouched)
sys.dont_write_bytecode = True
MERGE = os.path.join(W12, 'merge')
UNITS = os.path.join(W12, 'units')
BOOK = os.path.join(S, 'wf11', 'book_v3.md')
SVG3 = os.path.join(HERE, 'svg3')
NATIVE_DIR = os.path.join(S, 'wf6', 'svg')
FONT = os.path.join(S, 'wf7', 'fonts', 'GarlFlenn.woff2')
OUT_JSON = os.path.join(HERE, 'panes.json')
OUT_CSS = os.path.join(HERE, 'panes.css')
OUT_LOG = os.path.join(HERE, 'panes_build.log')

sys.path.insert(0, HERE)
import ink                  # noqa: E402  (wf12/orig, the merged lexicon)
import svgpool              # noqa: E402
sys.path.append(MERGE)
import coverage as C        # noqa: E402  (the merge's Book cut and unit English)
import coverage2 as C2      # noqa: E402  (the leaves' owners)
import pairs as P           # noqa: E402  (the units' items)
import halyna_check as HC   # noqa: E402  (the Book's two-ink rule)

E = lambda s: html.escape(s, quote=False)   # noqa: E731
A = lambda s: html.escape(s, quote=True)    # noqa: E731
LOG = []
FLAGS = []
STATS = collections.Counter()


def log(*a):
    LOG.append(' '.join(str(x) for x in a))


# ============================================================================ the drawings (slots)
def fresh_keys():
    """the keys make_grain3.py rendered (or found cached) in its last full run, and the render failures"""
    ok, bad = set(), set()
    for ln in open(os.path.join(HERE, 'make_grain3.log'), encoding='utf-8'):
        k = ln.split()[0] if ln.strip() else None
        if not k:
            continue
        (bad if 'FAILED' in ln else ok).add(k)
    return ok, bad


FRESH, FAILED = fresh_keys()
EXTRA_SVG3 = {'CHISEL_title', 'CHISEL_stonwryt', 'NAELEAR_chip'}    # recovered from the wf8 build (see the report)
USED = collections.OrderedDict()      # key -> where (for the report)


def slot3(key, title=None, where=''):
    assert os.path.exists(os.path.join(SVG3, key + '.svg')), key
    if key not in FRESH and key not in EXTRA_SVG3:
        raise SystemExit('svg3 key %s was not rendered by the last make_grain3.py run' % key)
    USED.setdefault(key, where)
    STATS['svg3'] += 1
    return '<span class="svg-slot" data-svg3="%s"%s></span>' % (A(key), (' data-title="%s"' % A(title)) if title else '')


def native_exists(nid):
    return os.path.exists(os.path.join(NATIVE_DIR, nid + '.svg'))


def slot_native(nid, title=None):
    STATS['native-drawn'] += 1
    USED.setdefault('native:' + nid, 'the Book\'s drawing')
    return '<span class="svg-slot" data-native="%s"%s></span>' % (A(nid), (' data-title="%s"' % A(title)) if title else '')


# ============================================================================ the ink
def strip_md(s):
    return s.replace('**', '').replace('*', '')


def clean_rom(s):
    s = s.strip()
    s = re.sub(r'^#+\s*', '', s)
    s = re.sub(r'⟨[^⟩]*⟩', ' ', s)
    s = re.sub(r'<!--.*?-->', '', s)
    s = s.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', s).strip()


def ink_markup(rom, end=None):
    rep = []
    mk, tok = ink.markup(rom, end, rep)
    for r in rep:
        FLAGS.append((rom[:60],) + tuple(r))
    return mk


PAIR_RE = re.compile(r'\{\{([A-Za-z]+)\}\}')


GLYPH_INLINE_RE = re.compile(r'⟦([a-z0-9_]+)⟧')
TOKEN_RE = re.compile(r'\{([A-Z_]+)\}')


def rom_html(r):
    """a romanised line for the fold: the pair-names under their lintel (span.pair, as the Book draws them); a drawn
    mark the line carries (IV.2's reading: ⟦legend_iv2_gap1⟧) set as the Book sets it, the Book's own drawing inline at
    text height; the VI.3 token as the romanised form of the Book's one state (fidelity pass, 2026-10-03: the fold had
    shown the builder's notation itself)"""
    s = PAIR_RE.sub(lambda m: '<span class="pair">%s</span>' % m.group(1), E(r))
    s = GLYPH_INLINE_RE.sub(lambda m: '<span class="glyph">%s</span>' % slot_native(m.group(1)), s)
    s = TOKEN_RE.sub(lambda m: token_rom(m.group(1)), s)
    return s


def token_rom(key):
    """{LAST_THRONE_AT_HAVEN} in a romanisation: the Book's one state (Glasspire), romanised, in the span the game swaps"""
    assert key == 'LAST_THRONE_AT_HAVEN', key
    rows = {}
    for ln in unit('S10').L:
        m = re.match(r'^\| (\w+) \| \*([^*]+)\* \| \*([^*]+)\* \|', ln)
        if m:
            rows[m.group(1)] = m.group(3)
    assert len(rows) == 10, rows
    return ('<span class="tok" data-token="LAST_THRONE_AT_HAVEN" data-haven="%s">%s</span>'
            % (TOKEN_DEFAULT, E(rows[TOKEN_DEFAULT])))


# ============================================================================ the interlinear (wf13, v3.1.0)
# Jack, 2026-10-03: "It would be cool if the romanization include what english translated word each was."  Every
# romanised line in a fold is set word by word, each word over its English (wf13/gloss/<UNIT>.json, keyed by the
# exact romanised line as the fold shows it; wf13/check_gloss.py proves every line is covered):
#     <p class="il"><i>Hos,<small aria-hidden="true">one</small></i> <i>eth<small aria-hidden="true">and</small></i>
#     <span class="sr">Word by word: one, and.</span></p>
# (the <i> is HTML's own element for a transliteration, a word of another tongue in our letters, and the shortest)
# The word keeps its punctuation; the line stays inline text (real spaces between the words, so it wraps where a line
# of words wraps, and a screen reader reads the romanised line once, as a line); each gloss is hidden from the screen
# reader and given again, once, after the line, as a visually hidden list.  Marks that are not words (a dash, a gap
# with its drawn mark, a middle dot) stand between the words unglossed, each in a span.m that keeps a word's space
# after it (wf13 reader check, 2026-10-04: left as bare text they had only the space, 3 px against the words' 9, and
# read as glued to the next word: 'Tolm —nel.', 'No —brodath').  The warden's blotted name (the four blots, as the
# Book sets them, never a name) stands where a word stands, so it gets a word's box and a gloss that says what it is,
# '(name blotted out)', set upright as the ink sets it (the same check: bare, it ran into the next word, '▒▒▒▒et',
# over an empty gloss slot that read as a missing gloss).  The VI.3 token's span, which holds five words, stays one
# span around their five word boxes (the game swaps it whole).
GLOSS_DIR = os.path.join(os.path.dirname(HERE), 'gloss')
INTERLINEAR = collections.Counter()


def load_gloss():
    g = {}
    for f in sorted(os.listdir(GLOSS_DIR)):
        if f.endswith('.json'):
            for r in json.load(open(os.path.join(GLOSS_DIR, f), encoding='utf-8')):
                if r['rom'] in g:
                    assert g[r['rom']] == r['gloss'], ('two glosses for one line', r['rom'][:60])
                g.setdefault(r['rom'], r['gloss'])
    return g


GLOSS = load_gloss()
TAG_SPLIT = re.compile(r'(<[^>]+>)')
WORD_CH = re.compile(r"[A-Za-zÀ-ž']")
BLOT_CH = '▒'                       # the warden's name, blotted out (four of them)
BLOT_GLOSS = '(name blotted out)'        # its gloss, as the grammar's glosses are set: '(past)', '(future)'
BLOT_SAID = 'a name blotted out'         # in the hidden word-by-word list, as the ink's blot is labelled


def html_text(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h))


def word_core(t):
    """a word as the gloss keys it: its letters, the punctuation at either end left off (wf13/extract_rom.py's rule)"""
    return re.sub(r"^[^\w']+|[^\w']+$", '', t)


def line_items(inner):
    """a romanised line's HTML -> [('w', html) a whitespace-separated run | ('s', ' ') | ('o'|'c', tag) the open or
    close of a span that holds several words (the VI.3 token)]; any other element (a pair-name's lintel, a drawn mark)
    stays inside its run"""
    items, cur, stack = [], [], []

    def flush():
        if cur:
            items.append(('w', ''.join(cur)))
            del cur[:]
    for part in TAG_SPLIT.split(inner):
        if not part:
            continue
        if part.startswith('</'):
            if stack.pop():
                flush()
                items.append(('c', part))
            else:
                cur.append(part)
        elif part.startswith('<'):
            wrap = 'class="tok"' in part
            if not part.endswith('/>'):
                stack.append(wrap)
            if wrap:
                flush()
                items.append(('o', part))
            else:
                cur.append(part)
        else:
            for chunk in re.split(r'(\s+)', part):
                if not chunk:
                    continue
                if chunk.isspace():
                    assert all(stack), ('a space inside an element of the line', inner[:80])
                    flush()
                    if items and items[-1][0] != 's':
                        items.append(('s', ' '))
                else:
                    cur.append(chunk)
    flush()
    while items and items[-1][0] == 's':
        items.pop()
    assert not stack, inner[:80]
    # a mark straight after the close of a span that holds words (VI.3: the token, then its sentence's full stop) goes
    # into the last word's box, as every word keeps its own punctuation: left after the box, it stood off by the width
    # of the box's gloss ('Sirrvell   .')
    out = []
    for k, x in items:
        if k == 'w' and not WORD_CH.search(html_text(x)) and len(out) >= 2 and out[-1][0] == 'c' and out[-2][0] == 'w':
            out[-2] = ('w', out[-2][1] + x)
            INTERLINEAR['marks moved into the last word of a span'] += 1
            continue
        out.append((k, x))
    return out


def rom_p(r):
    """one romanised line for a fold, word over word: the romanisation's italic word, its English beneath"""
    inner = rom_html(r)
    key = html_text(inner).strip()
    items = line_items(inner)
    words = [x for k, x in items if k == 'w' and WORD_CH.search(html_text(x))]
    if not words:
        INTERLINEAR['lines without a word'] += 1
        return '<p class="il">%s</p>' % inner
    g = GLOSS.get(key)
    if g is None:
        raise SystemExit('no gloss for the romanised line %r' % key[:80])
    cores = [word_core(html_text(x)) for x in words]
    if cores != [w for w, _ in g]:
        raise SystemExit('the gloss of %r has the words %s, the line %s' % (key[:60], [w for w, _ in g][:8], cores[:8]))
    out, n, said = [], 0, []
    for k, x in items:
        t = html_text(x)
        if k == 'w' and WORD_CH.search(t):
            out.append('<i>%s<small aria-hidden="true">%s</small></i>' % (x, E(g[n][1])))
            said.append(g[n][1])
            n += 1
        elif k == 'w' and BLOT_CH in t:
            out.append('<i class="blot">%s<small aria-hidden="true">%s</small></i>' % (x, E(BLOT_GLOSS)))
            said.append(BLOT_SAID)
            INTERLINEAR['blotted names glossed'] += 1
        elif k == 'w':
            out.append('<span class="m">%s</span>' % x)
            INTERLINEAR['marks between the words'] += 1
        else:
            out.append(x)
    INTERLINEAR['lines'] += 1
    INTERLINEAR['words'] += n
    sr = '<span class="sr">Word by word: %s.</span>' % ', '.join(E(e) for e in said)
    return '<p class="il">%s %s</p>' % (''.join(out), sr)


def rom_details(rom, label='Romanisation', extra=''):
    body = ''.join(rom_p(r) for r in (rom if isinstance(rom, list) else [rom]))
    return '<details class="tr rom"><summary>%s</summary><div class="tr-body">%s%s</div></details>' % (label, body, extra)


DASH = '<span class="ink-p" aria-hidden="true">&#8212;</span>'
GAP = '<span class="ink-gap" role="img" aria-label="a gap, left open">[&#8195;]</span>'
SEG_RE = re.compile(r'(⟦[a-z0-9_]+⟧|\[\s*⟦[a-z0-9_]+⟧\s*\]|\[\s*\]|—|·|\{[A-Z_]+\}|▒+)')
MIDDOT = '<span class="ink-p sep" aria-hidden="true">&#183;</span>'
# the warden's name, blotted out: four blots in Seren's ink as in the Book (never a name). The leaf-hand has no sign
# for it, so the blots stand in the house face, as the dash and the gap do (fidelity pass, 2026-10-03: the ink had
# dropped them, so twelve lines read as if no one were named there)
BLOT = '<span class="ink-blot" role="img" aria-label="a name blotted out">%s</span>'


def ink_line(rom, end=None, chips=None, tokens=None, wood_italics=False):
    """romanised Orrowen (markdown kept, for the wood role's italics) -> ink HTML.  Breaks the line where the ink has
    no sign: an em-dash (a broken-off word: the house face's dash), a gap [ ] (left open, never mended), an inline
    drawing ⟦id⟧ (a chip slot), a builder token {X} (span.tok, filled with the Book's one state of the game)."""
    rom = re.sub(r'<!--.*?-->', '', rom)
    parts = SEG_RE.split(rom)
    out = []
    textparts = [i for i, p in enumerate(parts) if p and not SEG_RE.fullmatch(p) and clean_rom(p)]
    last_text = textparts[-1] if textparts else -1
    for i, p in enumerate(parts):
        if not p:
            continue
        if SEG_RE.fullmatch(p):
            if p == '—':
                out.append(DASH)
            elif p == '·':
                out.append(MIDDOT)
            elif re.fullmatch(r'\[\s*\]', p):
                out.append(GAP)
            elif p.startswith('▒'):
                out.append(BLOT % p)
            elif p.startswith('{'):
                key = p[1:-1]
                tk = (tokens or {}).get(key)
                if tk:
                    out.append(tk)
                else:
                    out.append('<span class="tok">%s</span>' % E(p))
            else:
                gid = re.search(r'⟦([a-z0-9_]+)⟧', p).group(1)
                ch = (chips or {}).get(gid)
                out.append(ch if ch else '<span class="tok">%s</span>' % E(p))
            continue
        if not clean_rom(p):
            continue
        lead = re.match(r'^\s*([.,;:!?]+)\s*(.*)$', p, re.S)
        if out and lead:
            # a mark right after a token or a chip sits on it, as on a word (the perpend, or the wedge)
            out[-1] = out[-1] + ('.' if re.search(r'[.!?]', lead.group(1)) else ',')
            p = lead.group(2)
            if not clean_rom(p):
                continue
        piece = ink_segments(p, end if i == last_text else None, wood_italics)
        if out and piece and not re.search(r'[A-Za-zÀ-ÿ]', clean_rom(p)):
            out[-1] = out[-1] + piece          # a mark left after a token or a chip sits on it, as on a word
            continue
        out.append(piece)
    return ' '.join(x for x in out if x)


def ink_segments(p, end, wood_italics):
    if not wood_italics or '*' not in p.replace('**', ''):
        return E(ink_markup(clean_rom(p), end))
    # the wood's role on its italic words only (V.2's carvings, V.7's line): each run inked on its own
    q = p.replace('**', '')
    segs = []
    for j, s in enumerate(q.split('*')):
        if not s.strip():
            continue
        it = (j % 2 == 1)
        if segs and not re.search(r'[A-Za-zÀ-ÿ]', s):
            segs[-1] = (segs[-1][0] + s, segs[-1][1])
            continue
        segs.append((s, it))
    out = []
    for k, (s, it) in enumerate(segs):
        mk = E(ink_markup(clean_rom(s), end if k == len(segs) - 1 else None))
        out.append('<span class="ink-wood">%s</span>' % mk if it else mk)
    return ' '.join(out)


def ink_para(rom_md, cls='', end=None, label='Romanisation', first=False, voice=None, chips=None, tokens=None,
             wood_italics=False, extra='', tag='p', ipcls='', rom_lines=None):
    """one paragraph in Seren's ink (or Halyna's), its romanisation folded under it"""
    STATS['ink'] += 1
    c = 'ink' + ((' ' + cls) if cls else '')
    va = (' data-voice="%s"' % voice) if voice else ''
    rom = rom_lines if rom_lines is not None else clean_rom(rom_md)
    return ('<div class="ip%s%s"><%s class="%s" lang="x-orrowen"%s>%s</%s>%s</div>'
            % (' first' if first else '', (' ' + ipcls) if ipcls else '', tag, c, va,
               ink_line(rom_md, end, chips, tokens, wood_italics), tag, rom_details(rom, label, extra)))


def ink_verse(lines_md, label='Romanisation · the verse', cls='', wood_lines=()):
    STATS['ink'] += 1
    spans = []
    for n, l in enumerate(lines_md, 1):
        spans.append('<span class="l%s">%s</span>' % (' ink-wood' if n in wood_lines else '', ink_line(l)))
    return ('<div class="ip verse-ink%s"><div class="verse ink" lang="x-orrowen">%s</div>%s</div>'
            % ((' ' + cls) if cls else '', ''.join(spans), rom_details([clean_rom(l) for l in lines_md], label)))


def fig(art, cls, cap, details=''):
    return ('<figure class="native %s"><div class="art">%s</div><figcaption>%s%s</figcaption></figure>'
            % (cls, art, cap, details))


def capspan(s):
    return '<span class="cap">%s</span>' % s


def md_inline(s):
    s = E(s)
    s = PAIR_RE.sub(lambda m: '<span class="pair">%s</span>' % m.group(1), s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def gn_details(lines, label, reads=None, note=None, lit_label='Literal reading', lit_pre=None, lit_pre_label=None):
    body = '<pre class="gn">%s</pre>' % E('\n'.join(lines).strip('\n'))
    if reads:
        body += '<p class="lit"><span class="lit-h">%s</span> %s</p>' % (lit_label, md_inline(reads))
    if lit_pre:
        body += ('<p class="lit"><span class="lit-h">%s</span></p><pre class="gn lit-gn">%s</pre>'
                 % (lit_pre_label or ('File by file' if reads else lit_label), E(lit_pre.strip('\n'))))
    if note:
        body += '<p class="lit">%s</p>' % note
    return '<details class="tr gn-fold"><summary>%s</summary><div class="tr-body">%s</div></details>' % (label, body)


def ring_gn(lines):
    """a knowing-form ring as the fold prints it: the movement marks are the page's (the rules between plates)"""
    keep = [ln for ln in lines if ln.strip() not in ('I', 'II', 'III', '‖', '‖¦', '¦') and not re.match(r'^\s*‖', ln)]
    while keep and not keep[0].strip():
        keep.pop(0)
    base = min((len(x) - len(x.lstrip()) for x in keep if x.strip()), default=0)
    return [x[base:] if len(x) >= base else x for x in keep]


# ============================================================================ the units
class UnitFile:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(UNITS, name + '.md')
        self.text = open(self.path, encoding='utf-8').read()
        self.L = self.text.split('\n')
        self.items = P.items(self.path)
        self.by_line = {it['line']: it for it in self.items}
        self.item_lines = sorted(self.by_line)
        # every fenced code block: (start line of the fence, 1-based, the line after ```), (end line), text
        self.codes = []
        i = 0
        while i < len(self.L):
            if self.L[i].startswith('```'):
                j = i + 1
                while j < len(self.L) and not self.L[j].startswith('```'):
                    j += 1
                self.codes.append({'open': i + 1, 'first': i + 2, 'close': j + 1, 'text': '\n'.join(self.L[i + 1:j]),
                                   'lang': self.L[i][3:].strip()})
                i = j + 1
                continue
            i += 1
        # the make_grain3 keys of the stone units' rounds (the same count: blocks that start with 'round ')
        self.round_key = {}
        seen = collections.Counter()
        for cb in self.codes:
            if cb['lang'] == '' and re.match(r'(?:#[^\n]*\n)*round ', cb['text'] + '\n'):
                rid = re.match(r'(?:#[^\n]*\n)*round (\S+)', cb['text']).group(1)
                seen[rid] += 1
                self.round_key[cb['first']] = '%s_%s' % (name, rid) + ('' if seen[rid] == 1 else '_%d' % seen[rid])
        self.headings = [i + 1 for i, l in enumerate(self.L) if l.startswith('## ')]
        round_opens = {cb['open'] for cb in self.codes if cb['first'] in self.round_key}
        self.nonround_items = [l for l in self.item_lines if l not in round_opens]
        self.after_table = next((i + 1 for i, l in enumerate(self.L) if l.startswith('### After the table')), 10 ** 6)

    def code_at(self, line):
        """the code block whose first content line is `line` (pairs.items counts a code item from that line)"""
        for cb in self.codes:
            if cb['first'] == line or cb['open'] == line:
                return cb
        raise KeyError('%s: no code block at %d' % (self.name, line))

    def next_item_after(self, line):
        for l in self.item_lines:
            if l > line:
                return l
        return len(self.L) + 1

    def next_heading_after(self, line):
        for l in self.headings:
            if l > line:
                return l
        return len(self.L) + 1


UF = {}


def unit(name):
    if name not in UF:
        UF[name] = UnitFile(name)
    return UF[name]


# ============================================================================ the Book
SEC_IDS = {
    'CONTENTS': 'contents', 'OF THIS BOOK': 'foreword', 'THE INVOCATION': 'invocation',
    'BOOK ONE · THE BOOK OF THE WALL': 'book-1', 'BOOK TWO · THE BOOK OF THE BUILDERS': 'book-2',
    'BOOK THREE · THE BOOK OF THE HAVENS': 'book-3', 'BOOK FOUR · THE BOOK OF THE WOUND': 'book-4',
    'BOOK FIVE · THE BOOK OF THE TIDES': 'book-5', 'BOOK SIX · THE BOOK OF THE HOMECOMINGS': 'book-6',
    'EPILOGUE': 'epilogue', 'APPENDIX': 'knowings',
}
UNIT_IDS = {'The Stone out of the Grey': 't-epilogue', 'The Book of Knowings': 't-knowings'}
LAST_NOTE = '**The Last Note · Three Stones over the Hearth**'
WOOD_UNITS = {'W01': 'II-2', 'W02': 'IV-2', 'W03': 'IV-4', 'W04': 'IV-6', 'W05': 'V-3', 'W06': 'V-4', 'W07': 'V-6', 'W08': 'VI-2'}
ANSWERS = ('*And the hearth said: We remember.*', '*And everyone at the hearth said: We remember.*')
SILENT = ('*And no one answered.*',)
HOOD = ('*And the Captain put his hood back.*', '*And the Captain pushed his hood back.*')
LAID = ('This I lay as it was laid for me.', 'This we lay as it was laid for us.')
TOKEN_DEFAULT = 'Glasspire'     # the story builder's one true state: the Book's own order lays Glasspire last (VI.1)


def tale_id(num):
    return 't-' + num.replace('.', '-')


def fully_italic(t):
    return bool(re.match(r'^\*(?!\*)[^*]+\*$', t))


def bold_only(t):
    return bool(re.match(r'^\*\*[^*]+\*\*$', t))


def book_lines():
    return open(BOOK, encoding='utf-8').read().split('\n')


BL = book_lines()


def front_paras():
    """the title page and the Contents (before OF THIS BOOK), cut as the body is: a heading, a paragraph, a list item"""
    out = []
    end = next(i for i, l in enumerate(BL) if l.strip() == '## OF THIS BOOK')
    leaf = None
    for i in range(0, end):
        l = BL[i]
        s = l.strip()
        if not s or s == '---':
            continue
        if l.startswith('#'):
            h = l.lstrip('#').strip()
            leaf = h if l.startswith('## ') and h == 'CONTENTS' else (leaf or h)
            out.append(dict(line=i + 1, kind='head', text=h, leaf=leaf, level=len(l) - len(l.lstrip('#'))))
            continue
        if l.startswith('- '):
            out.append(dict(line=i + 1, kind='list', text=l[2:].strip(), leaf=leaf))
            continue
        out.append(dict(line=i + 1, kind='para', text=s, leaf=leaf))
    return out


def body_paras():
    """C.book_paras(), with the native fences' caption and body lines made one 'native' item (one drawing, one block)
    and every item given its end line, its fence head and its blockquote"""
    bp = C.book_paras()
    out = []
    i = 0
    while i < len(bp):
        p = dict(bp[i])
        if p['kind'] in ('native-cap',):
            j = i + 1
            group = [p]
            while j < len(bp) and bp[j]['kind'] == 'native-body':
                group.append(bp[j])
                j += 1
            head_line = p['line'] - 1
            while not re.sub(r'^>\s?', '', BL[head_line - 1]).strip().startswith(':::'):
                head_line -= 1
            fh = re.sub(r'^>\s?', '', BL[head_line - 1]).strip().split()
            nat = dict(line=head_line, kind='native', leaf=p['leaf'], cap=p['text'], body=[g['text'] for g in group[1:]],
                       body_lines=[g['line'] for g in group[1:]], cap_line=p['line'],
                       fence=fh[1], nid=fh[2] if fh[1] == 'native' else None, size=fh[3] if len(fh) > 3 else None,
                       inbq=BL[head_line - 1].startswith('>'))
            close = group[-1]['line'] + 1
            while re.sub(r'^>\s?', '', BL[close - 1]).strip() != ':::':
                close += 1
            nat['end'] = close
            nat['text'] = '\n'.join(BL[head_line - 1:close])
            out.append(nat)
            i = j
            continue
        p['end'] = p['line'] + p['text'].count('\n')
        out.append(p)
        i += 1
    return out


def bq_block_of(line):
    """the Book blockquote (contiguous '>' lines) holding a line: (first, last, lines)"""
    a = line
    while a > 1 and BL[a - 2].startswith('>'):
        a -= 1
    b = line
    while b < len(BL) and BL[b].startswith('>'):
        b += 1
    return a, b, [re.sub(r'^> ?', '', x) for x in BL[a - 1:b]]


def markers_before(line, prev_end):
    """the builder's markers (whole-line HTML comments) between the previous paragraph and this one"""
    out = []
    for k in range(prev_end, line - 1):
        s = BL[k].strip()
        s = re.sub(r'^>\s?', '', s)
        if s.startswith('<!--') and s.endswith('-->'):
            out.append(s[4:-3].strip())
    return out


def leaves():
    """[(anchor, [paras])] in the Book's order (the story builder's split: the title page, the Contents, the
    foreword and the Invocation; each Book's heading and Argument under the Book's id; each tale; the Last Note)"""
    allp = front_paras() + body_paras()
    res = collections.OrderedDict()
    cur = None
    sec = None
    for p in allp:
        if p['kind'] == 'head' and BL[p['line'] - 1].startswith('# '):
            cur = 'front'
        elif p['kind'] == 'head' and BL[p['line'] - 1].startswith('## '):
            h = p['text']
            if h in SEC_IDS:
                sec = SEC_IDS[h]
                cur = sec
            else:
                cur = 'front'
        elif p['kind'] == 'head' and BL[p['line'] - 1].startswith('### '):
            m = re.match(r'^((?:VI|IV|V|III|II|I)\.\d+) · (.+)$', p['text'])
            cur = tale_id(m.group(1)) if m else UNIT_IDS[p['text']]
        elif p['kind'] == 'para' and p['text'] == LAST_NOTE:
            cur = 't-last-note'
        res.setdefault(cur, []).append(p)
    return res


# ============================================================================ the pairing (coverage2's walk, kept with nth)
def pair_book():
    bp = C.book_paras()
    ue = C.unit_english()
    byu = collections.defaultdict(list)
    for x in ue:
        byu[x['unit']].append(x)
    for u in byu:
        byu[u].sort(key=lambda x: (x['line'], x.get('nth', 0)))
    ptr = collections.defaultdict(int)
    used = set()
    hits = {}
    for p in bp:
        u = C2.owner(p['line'])
        its = byu[u]
        j = ptr[u]
        while j < len(its) and its[j]['line'] < C2.START.get(u, 0):
            j += 1
        key = C.norm(p['text'])
        keyh = C.norm_head(p['text'])
        hit = None
        for k in range(j, len(its)):
            e = its[k]['eng']
            if (C.norm(e) == key) or (p['kind'] == 'head' and C.norm_head(e) == keyh):
                hit = k
                break
        ooo = False
        if hit is None:
            for k in range(0, len(its)):
                if (u, its[k]['line'], its[k].get('nth', 0)) in used or its[k]['line'] < C2.START.get(u, 0):
                    continue
                e = its[k]['eng']
                if (C.norm(e) == key) or (p['kind'] == 'head' and C.norm_head(e) == keyh):
                    hit, ooo = k, True
                    break
        if hit is not None:
            if not ooo:
                ptr[u] = hit + 1
            used.add((u, its[hit]['line'], its[hit].get('nth', 0)))
            hits[p['line']] = (u, its[hit]['line'], its[hit]['kind'], its[hit].get('nth', 0))
    return hits, used, byu


def pair_front(paras):
    """the title page and the Contents are S11's (§1, §2): each Book line to the S11 item whose English it is"""
    s11 = unit('S11')
    its = [it for it in s11.items if it['line'] < C2.START['S11']]
    out = {}
    k = 0
    for p in paras:
        key, keyh = C.norm(p['text']), C.norm_head(p['text'])
        for q in range(k, len(its)):
            e = '\n'.join(x[1:].lstrip(' ') if x.startswith('>') else x for x in its[q]['eng'].split('\n'))
            if C.norm(e) == key or C.norm_head(e) == keyh:
                out[p['line']] = ('S11', its[q]['line'], its[q]['kind'], 0)
                k = q + 1
                break
    return out


# ============================================================================ what a unit says around an item
def region_after(u, line):
    """the unit's lines after an item, up to the next item or the next '## ' section"""
    return line, min(u.next_item_after(line), u.next_heading_after(line))


def rounds_in(u, a, b):
    """the rounds a stone unit sets between two of its lines; not those a native block draws (V.1's Wave)"""
    return [cb for cb in u.codes if a < cb['first'] < b and cb['first'] in u.round_key
            and u.round_key[cb['first']] not in NATIVE_GRAIN.values()]


def carving_reads(u, cb, stop):
    """what a unit says a round reads: '*The plank's carving … Literal reading:* "…"', '- **Reads** …: …',
    '*The grain holds the whole carved line* …: …', or a line of its own after a 'Literal reading' label"""
    words = reads = None
    for i in range(cb['close'], min(stop, len(u.L))):
        ln = u.L[i].strip()
        m = re.match(r'^\*The plank.s carving.*Literal reading:\*\s*"(.+)"\s*$', ln)
        if m and not words:
            words = m.group(1)
        m = re.match(r'^-?\s*\*\*Reads\*\*[^:]*:\s*(.+)$', ln) or re.match(r'^-?\s*\*\*Reads:\*\*\s*(.+)$', ln)
        if m and not reads:
            reads = m.group(1)
        m = re.match(r'^-\s*\*\*Literal reading:\*\*\s*(.+)$', ln)
        if m and not reads:
            reads = m.group(1)
        m = re.match(r'^Literal reading \(of [^)]*\):\s*(.+)$', ln)
        if m and not reads:
            reads = m.group(1)
    return words, reads


# ============================================================================ the blocks
class Ctx:
    """the state of one leaf as its paragraphs are walked"""

    def __init__(self, anchor, paras):
        self.anchor = anchor
        self.paras = paras
        self.head = True          # before the teller line
        self.first_done = False
        self.after_part = False
        self.w_lead = None
        self.w_words = []
        self.prev_end = paras[0]['line'] - 1 if paras else 0
        self.ring_prev = None
        self.story = False


def leaf_unit(anchor, paras):
    owners = [C2.owner(p['line']) for p in paras if p['line'] >= 85]
    return collections.Counter(owners).most_common(1)[0][0] if owners else 'S11'


def classify(ctx, p, markers):
    """the Book paragraph's role, as the story builder reads it"""
    t = p['text']
    k = p['kind']
    if k == 'head' or t == LAST_NOTE:
        return 'title'
    if k in ('reading',):
        return 'reading'
    if k == 'seal':
        return 'seal'
    if k == 'story':
        return 'ring'
    if k == 'native':
        return 'native' if p['fence'] == 'native' else 'note'
    if k == 'table':
        return 'table-head' if t.startswith('| The root') else 'table-row'
    if k == 'list':
        return 'list-item'
    if k == 'bq' and '\n' in t and all(x.strip().startswith('*') and x.strip().endswith('*') for x in t.split('\n')):
        return 'verse'
    if t in ANSWERS:
        return 'answer'
    if t in SILENT:
        return 'silent'
    if t in HOOD:
        return 'hood'
    if t in LAID:
        return 'laid'
    if bold_only(t):
        return 'title-line' if t.startswith('**IN MEMORY') else 'part'
    if t.startswith('***Added'):
        return 'added'
    return 'para'


def voice_map():
    """Book line -> 'a' | 'b' | 's' | '-' for every paragraph inside a HALYNA block or a READING (halyna_check's rule)"""
    vm = {}
    for b in HC.book_blocks():
        for q in b['paras']:
            vm[q['line']] = q['want']
    return vm


VOICE = voice_map()


def label_of(kind):
    return {'title': 'Romanisation · the title', 'dateline': 'Romanisation · the dateline',
            'headnote': 'Romanisation · Seren’s headnote', 'laid': 'Romanisation · the laying',
            'frame': 'Romanisation · the frame', 'inscr': 'Romanisation · the words set in',
            'answer': 'Romanisation · the hearth’s answer', 'silent': 'Romanisation · Seren’s closing line',
            'hood': 'Romanisation · the Captain’s answer', 'who-line': 'Romanisation · the frame',
            'added': 'Romanisation · added in Seren’s hand', 'book-head': 'Romanisation · the heading',
            'book-arg': 'Romanisation · the line under it', 'reading': 'Romanisation · the reading',
            'list-item': 'Romanisation · the Contents', 'contents-line': 'Romanisation · the Contents',
            'front-line': 'Romanisation · the title page'}.get(kind, 'Romanisation')


INK_CLS = {'title': 'ink-name', 'book-head': 'ink-book', 'book-arg': 'ink-booksub', 'dateline': 'ink-dateline',
           'headnote': 'ink-teller', 'laid': 'ink-laid', 'frame': 'ink-frame', 'who-line': 'ink-frame ink-who',
           'added': 'ink-frame ink-added', 'inscr': 'ink-inscr', 'answer': 'ink-answer',
           'silent': 'ink-answer ink-silent', 'hood': 'ink-answer ink-hood', 'reading': 'ink-reading',
           'front-title': 'ink-book', 'front-sub': 'ink-booksub', 'front-line': 'ink-booksub',
           'contents-line': 'ink-toc', 'list-item': 'ink-toc-tale'}


def item_rom(u, it):
    """an item's Orrowen, markdown kept (one string; a verse keeps its lines)"""
    return it['orr']


def build_leaf(anchor, paras, hits):
    ctx = Ctx(anchor, paras)
    blocks = []
    wood = any(C2.owner(p['line']).startswith('W') for p in paras if p['line'] >= 85 and p['kind'] in ('story', 'seal'))
    for idx, p in enumerate(paras):
        markers = markers_before(p['line'], ctx.prev_end)
        ctx.prev_end = p.get('end', p['line'])
        try:
            b = render(ctx, idx, p, markers, hits, wood)
        except Exception as e:   # noqa: BLE001
            log('  !! %s L%d: %r' % (anchor, p['line'], e))
            raise
        b.update(para_index=idx, line=p['line'], end_line=p.get('end', p['line']), book=p['text'])
        if markers:
            b['markers'] = markers          # the builder's markers just above this paragraph (RING: the grain-rule)
        blocks.append(b)
    return blocks


# ---------------------------------------------------------------------------- one paragraph
def render(ctx, idx, p, markers, hits, wood):
    k = classify(ctx, p, markers)
    t = p['text']
    hit = hits.get(p['line'])
    a = ctx.anchor
    # the builder's markers
    wood_role = 'W' in markers
    if 'W: the italic carvings only' in markers:
        ctx.w_lead = 'armed'
        ctx.w_words = ['Burn']
    w_em = 'W: the italic line only' in markers
    w_line3 = 'W: line 3 only' in markers
    mixed = any(m.startswith('MIXED') for m in markers)
    if 'RING' in markers:
        pass
    # the head of a leaf: its title, then (italic) the dateline and the headnote
    if k == 'title':
        ctx.head = True
        return render_title(ctx, p, hit)
    if a == 'front' and p['kind'] == 'para':
        return render_simple(p, hit, 'front-line', 'front-line')
    if a == 'contents':
        return render_contents(p, hit)
    if a.startswith('book-') or a in ('epilogue', 'knowings'):
        # a Book's Argument (the line under its heading)
        return render_simple(p, hit, 'book-arg', 'book-arg')
    if k == 'para' and ctx.head and t.startswith('*'):
        words = len(re.findall(r"[A-Za-z']+", t))
        if fully_italic(t) and words <= 9 and ctx.anchor != 't-last-note' and not getattr(ctx, 'dated', False):
            ctx.dated = True
            return render_simple(p, hit, 'dateline', 'dateline')
        ctx.head = False
        return render_simple(p, hit, 'headnote', 'headnote')
    if k not in ('title',):
        ctx.head = False
    if k == 'part':
        ctx.after_part = True
        return render_part(p, hit)
    after_part, ctx.after_part = ctx.after_part, False
    if k == 'reading':
        return render_reading(ctx, p, hit)
    if k == 'seal':
        return render_seal(ctx, p, hit)
    if k == 'ring':
        return render_ring(ctx, p, hit)
    if k in ('native', 'note'):
        return render_native(ctx, p, hits)
    if k in ('table-head', 'table-row'):
        return render_table_row(ctx, p, k)
    if k == 'verse':
        return render_verse(ctx, p, hit, w_line3, wood_role)
    if k == 'title-line':
        return render_title_line(ctx, p, hit)
    if hit is None:
        log('  !! %s L%d: no unit item for a %s paragraph: %s' % (a, p['line'], k, t[:80]))
        return dict(kind='missing', html='<!-- no Orrowen for this paragraph -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    if hit[2] == 'ring':
        # a stone leaf's carving given as a ring excerpt (V.7) or a round
        return render_stone_ring(ctx, p, u, it)
    rom = item_rom(u, it)
    # the role and its ink
    kind = k
    if k == 'para':
        if t.startswith('*') and (t.endswith(':') or t.endswith(':*')):
            kind = 'frame'
        elif fully_italic(t):
            kind = 'who-line' if after_part else 'inscr'
            if kind == 'inscr' and (wrap_of(ctx, p) or {}).get('wrap') == 'facing':
                kind = 'frame'          # the line over a facing leaf (V.1's), as I.1's is
    if k == 'added':
        kind = 'added'
    cls = INK_CLS.get(kind, '')
    end = 'coping' if kind in ('answer', 'silent', 'hood') else None
    voice = None
    v = VOICE.get(p['line'])
    teller = None
    if v in ('a', 'b'):
        voice = v
        kind = 'halyna' if kind == 'para' else kind
        m = re.match(r'^\*\*(Rhyna|Halvard)\.\*\*', t)
        if m:
            teller = m.group(1)
            kind = 'marked'
            cls = (cls + ' ink-marked').strip()
    if p['kind'] == 'reading':
        kind = 'reading'
    first = False
    if kind in ('para', 'halyna', 'marked') and not ctx.first_done:
        first = True
        ctx.first_done = True
    # the wood's role inside a stone leaf
    wood_italics = False
    if wood_role:
        cls = (cls + ' ink-wood').strip()
    if w_em:
        wood_italics = True
    if ctx.w_lead:
        if t.startswith('*'):
            wood_italics = True
            ctx.w_lead = 'run'
        elif ctx.w_lead == 'run':
            ctx.w_lead = None
    if ctx.w_words and not ctx.w_lead:
        for w in list(ctx.w_words):
            if '*%s*' % w in t:
                wood_italics = True
                ctx.w_words.remove(w)
    if mixed:
        cls = (cls + ' ink-mixed').strip()
    tokens = None
    tok_forms = None
    if '{LAST_THRONE_AT_HAVEN}' in rom:
        tokens, tok_forms = token_vi3(rom)
    lab = label_of(kind)
    if teller:
        lab = 'Romanisation · %s' % teller
    body = ink_para(rom, cls, end, lab, first=first, voice=voice, tokens=tokens, wood_italics=wood_italics)
    # a carving the unit sets with this paragraph (V.2's planks before; VI.3's sliver and the Knowings' Burn after)
    before, after = attached_rounds(u, it)
    out = body
    if before or after:
        out = '<div class="carved-para">%s%s%s</div>' % (''.join(before), body, ''.join(after))
        kind = 'carving' if kind == 'para' else kind
    b = dict(kind=kind, html=out, src='%s:%d' % (u.name, it['line']))
    if voice:
        b['voice'] = voice
    if wood_role or wood_italics:
        b['role'] = 'wood'
    if mixed:
        b['role'] = 'mixed'
    if tok_forms:
        b['token_forms'] = tok_forms
    wrap = wrap_of(ctx, p)
    if wrap:
        b.update(wrap)
    return b


def wrap_of(ctx, p):
    if not BL[p['line'] - 1].startswith('>'):
        return None
    a, z, lines = bq_block_of(p['line'])
    before = next((BL[i].strip() for i in range(a - 2, 0, -1) if BL[i].strip()), '')
    facing = any('faceth' in x for x in lines) or 'facing leaf' in before.lower()
    cls = 'invocation' if ctx.anchor == 'invocation' else ('facing' if facing else 'quote')
    return {'wrap': cls, 'wrap_id': 'bq%d' % a}


def render_simple(p, hit, kind, ink_kind):
    if hit is None:
        log('  !! L%d: no unit item for a %s: %s' % (p['line'], kind, p['text'][:80]))
        return dict(kind='missing', html='<!-- no Orrowen for this paragraph -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    h = ink_para(item_rom(u, it), INK_CLS.get(ink_kind, ''), None, label_of(ink_kind))
    return dict(kind=kind, html=h, src='%s:%d' % (u.name, it['line']))


def render_title(ctx, p, hit):
    lvl = 1 if BL[p['line'] - 1].startswith('# ') else (2 if BL[p['line'] - 1].startswith('## ') else 3)
    kind = 'title' if lvl == 3 else 'book-head'
    if ctx.anchor == 'front':
        kind = 'front-title' if lvl == 1 else 'front-sub'
    if hit is None:
        log('  !! %s L%d: no Orrowen for the heading %s' % (ctx.anchor, p['line'], p['text']))
        return dict(kind='missing', html='<!-- no Orrowen for this heading -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    cls = INK_CLS[kind]
    lab = 'Romanisation · the title' if kind == 'title' else ('Romanisation · the Book’s name' if ctx.anchor == 'front' else 'Romanisation · the heading')
    return dict(kind=kind, html=ink_para(item_rom(u, it), cls, None, lab), src='%s:%d' % (u.name, it['line']))


def render_contents(p, hit):
    kind = 'list-item' if p['kind'] == 'list' else ('contents-line' if not fully_italic(p['text']) else 'contents-arg')
    if hit is None:
        log('  !! contents L%d: no Orrowen: %s' % (p['line'], p['text'][:80]))
        return dict(kind='missing', html='<!-- no Orrowen for this line -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    cls = {'list-item': 'ink-toc-tale', 'contents-line': 'ink-toc', 'contents-arg': 'ink-toc-arg'}[kind]
    return dict(kind=kind, html=ink_para(item_rom(u, it), cls, None, 'Romanisation · the Contents'),
                src='%s:%d' % (u.name, it['line']))


def render_part(p, hit):
    if hit is None:
        log('  !! L%d: no Orrowen for a part head: %s' % (p['line'], p['text']))
        return dict(kind='missing', html='<!-- no Orrowen for this part head -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    STATS['ink'] += 1
    h = ('<div class="ip part-ink"><h4 class="part ink" lang="x-orrowen">%s</h4>%s</div>'
         % (ink_line(it['orr']), rom_details(clean_rom(it['orr']), 'Romanisation · the part')))
    return dict(kind='part', html=h, src='%s:%d' % (u.name, it['line']))


def render_verse(ctx, p, hit, w_line3, wood_role):
    if hit is None:
        log('  !! %s L%d: no Orrowen for a verse' % (ctx.anchor, p['line']))
        return dict(kind='missing', html='<!-- no Orrowen for this verse -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    lines = [x.rstrip() for x in it['orr'].split('\n') if x.strip()]
    wl = {3} if w_line3 else set()
    h = ink_verse(lines, 'Romanisation · the verse', '', wood_lines=wl)
    if wood_role:
        h = h.replace('class="verse ink"', 'class="verse ink ink-wood"', 1)
    before, after = attached_rounds(u, it)
    kind = 'verse'
    if before or after:
        h = '<div class="carved-para">%s%s%s</div>' % (''.join(before), h, ''.join(after))
    b = dict(kind=kind, html=h, src='%s:%d' % (u.name, it['line']))
    if wl:
        b['role'] = 'wood: line 3'
    w = wrap_of(ctx, p)
    if w and w['wrap'] != 'quote':
        b.update(w)
    return b


# ---------------------------------------------------------------------------- the Title, and its dry cut
DRY_TITLE = ('<details class="tr"><summary>The dry cut · <em>ryt broc</em></summary><div class="tr-body">'
             '<p>The chisel register cuts the stones only: five word-signs on their footings, each with its ending laid on in letters, parted by wedges and closed by the perpend. The six mortar words (<em>ul</em>, and <em>ol</em> five times) are left for the reader to lay in: <em>Memory: home, families, God, freedoms, peace.</em> Seventeen signs, where the ink writes forty-eight letters and marks.</p>'
             '<p class="tok-line"><code>@tum+O.l @varn , @theld+A.th , @mardh , @lunn+A.th , @sollan |</code></p>'
             '<p>%s This is how the guild would cut it over a gate.</p></div></details>')
TITLE_WHERE = {'invocation': 'The Captain wrote it in coal on the torn cloak, every word (the Book draws that).',
               't-I-1': 'The Captain did not cut it: he wrote it in coal on the torn cloak, every word (the Book draws that).'}


def render_title_line(ctx, p, hit):
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    rom = it['orr']
    STATS['ink'] += 1
    out = ['<div class="ip title-ink"><p class="ink ink-title" lang="x-orrowen">%s</p>%s</div>'
           % (ink_line(rom), rom_details(clean_rom(rom), 'Romanisation · the Title'))]
    if ctx.anchor in ('invocation', 't-I-1'):
        # the old Original's pair: the Title in Seren's ink, and cut dry as the guild would cut it over a gate. I.4's
        # Title under the new capstone is cut in the Captain's own coal letters, not dry (S03), so it stands alone.
        out.append(fig(slot3('CHISEL_title', 'The Title of Liberty, cut dry', 'the Title cut dry'), 'line chisel stone-ink',
                       capspan('The Title cut dry, as the guild would cut it over a gate'), DRY_TITLE % TITLE_WHERE[ctx.anchor]))
        STATS['chisel'] += 1
    b = dict(kind='title-line', html='\n'.join(out), src='%s:%d' % (u.name, it['line']))
    w = wrap_of(ctx, p)
    if w:
        b.update(w)
    return b


# ---------------------------------------------------------------------------- the token (VI.3)
def token_vi3(rom):
    """{LAST_THRONE_AT_HAVEN}: the sentence 'Ew {X}.' filled with the Book's one state (Glasspire), in a span the game
    swaps; and the ten forms of the sentence in ink (S10 §3)"""
    L = unit('S10').L
    rows = {}
    for ln in L:
        m = re.match(r'^\| (\w+) \| \*([^*]+)\* \| \*([^*]+)\* \|', ln)
        if m:
            rows[m.group(1)] = (m.group(2), m.group(3))
    assert len(rows) == 10, rows
    forms = {}
    for haven, (eng, orr) in rows.items():
        forms[haven] = {'book': eng, 'orrowen': orr, 'ink': E(ink_markup(orr))}
    d = rows[TOKEN_DEFAULT][1]
    span = ('<span class="tok" data-token="LAST_THRONE_AT_HAVEN" data-haven="%s">%s</span>'
            % (TOKEN_DEFAULT, E(ink_markup(d))))
    return {'LAST_THRONE_AT_HAVEN': span}, forms


# ---------------------------------------------------------------------------- the wood leaves: the reading
def frag_chips():
    return {'legend_iv2_gap1': '<span class="frag untold">%s</span>' % slot3('IV-2_frag1', 'the first drawn mark: the pillars, many, with a memory cut through them to the heart', 'IV.2 reading'),
            'legend_iv2_gap2': '<span class="frag untold">%s</span>' % slot3('IV-2_frag2', 'the second drawn mark: the mouth, mirrored, tied back to the plea cut on the stone', 'IV.2 reading')}


def render_reading(ctx, p, hit):
    if hit is None:
        log('  !! %s L%d: no Orrowen for a reading line' % (ctx.anchor, p['line']))
        return dict(kind='missing', html='<!-- no Orrowen for this line -->')
    u = unit(hit[0])
    it = u.by_line[hit[1]]
    v = VOICE.get(p['line'])
    voice = v if v in ('a', 'b') else None
    chips = frag_chips() if '⟦legend_iv2' in it['orr'] else None
    lab = 'Romanisation · the reading, %s ink' % ('first' if voice == 'a' else 'second') if voice else 'Romanisation · the reading'
    h = ink_para(it['orr'], 'ink-reading', None, lab, voice=voice, chips=chips)
    b = dict(kind='reading', html=h, src='%s:%d' % (u.name, it['line']))
    if voice:
        b['voice'] = voice
    return b


# ---------------------------------------------------------------------------- the wood leaves: the seal, the rings
def wood_key(u, line):
    """the round a wood unit's ring belongs to, and the ring's number in it"""
    base = WOOD_UNITS[u.name]
    if u.name != 'W08':
        return base, None
    for j in range(line - 1, 0, -1):
        m = re.match(r'^\*\*([A-Z][a-z]+) · Ring (\d+)\*\*', u.L[j - 1])
        if m:
            return 'VI-2-' + m.group(1).lower(), int(m.group(2))
        m = re.match(r'^\*\*Ring (\d+)\*\*', u.L[j - 1])
        if m:
            return 'VI-2-thaesaen', int(m.group(1))
    raise KeyError(line)


def whole_note(key, canon):
    L = canon.split('\n')
    header = next(ln for ln in L if ln.startswith('round '))
    legend = [ln for ln in L if ln.startswith('# file')]
    bark, sec = [], None
    for ln in L:
        s = ln.strip()
        if s in ('bark', 'runners'):
            sec = s
            continue
        if sec == 'bark' and s.startswith('bark '):
            bark.append(s)
    rings = [ln for ln in L if re.match(r'^\s*r\d+', ln)]
    K = max(int(re.match(r'^\s*r(\d+)', ln).group(1)) for ln in rings)
    marks = 0
    for ln in rings:
        body = re.sub(r'pocket\s+P\w+\s+\w+\s+[\d–-]+\s*\{[^}]*\}', ' ', ln)
        body = re.sub(r'band\s+\w+\s+files\s+[\d–-]+', ' ', body)
        marks += len(re.findall(r'(?:^|\s)(?:p\d+·)?\d+(?:\.\d)?:\s', body))
    pockets = sum(len(re.findall(r'pocket\s+P', ln)) for ln in rings)
    runners = len([ln for ln in L if re.match(r'^\s*run\s', ln)])
    rl = [int(x) for x in re.search(r'rules after:\s*\[([^\]]*)\]', header).group(1).split(',') if x.strip()]
    bands, prev = [], 0
    for r in rl + [K]:
        bands.append(r - prev)
        prev = r
    svg = open(os.path.join(SVG3, key + '.svg'), encoding='utf-8').read()
    rad = svgpool.r_outer(svg)
    lines = [header] + legend + ['  bark'] + ['    ' + x for x in bark]
    note = ('The seal in the bark, <code>bark 0: HOLD</code>, is &ldquo;This is held in the grain&rdquo; and &ldquo;the grain '
            'holds it still&rdquo;: it is not a ring. %d rings in three movements (%s): %d marks, %d runners%s. Packed by years '
            'and cells, the round is %d years, about %s units in radius.'
            % (K, ' / '.join(str(b) for b in bands), marks, runners,
               (', %d pocket%s' % (pockets, '' if pockets == 1 else 's')) if pockets else '', len(rings),
               '{:,}'.format(rad) if rad else '?'))
    return lines, note, K


WHOLE_CAP = {
    'W01': 'The whole round, as the wood holds it: the gift of the Guest at its deepest holding, Myststone',
    'W02': 'The whole round, as the wood holds it: a Blackthorn heart, grown from the last shoot of a felled pillar&rsquo;s stump',
    'W03': 'The whole round, as the wood holds it: the gift itself, Myststone',
    'W04': 'The whole round, as the wood holds it: the heart of a Standard-Bearer of the Tide of Remembering',
    'W05': 'The whole round, as the wood holds it: a hull of the Tide of Remembering',
    'W06': 'The whole round, as the wood holds it: the heart of a Standard-Bearer of the Joined Tide, of Silverbark',
    'W07': 'The whole round, as the wood holds it: the heart of a Standard-Bearer of the Joined Tide',
    'W08': 'The first of the ten hearts, whole, as the wood holds it: Thaesaen&rsquo;s, the eldest wood',
}


def round_title(u):
    m = re.search(r"^#\s*name\s*:\s*(.+)$", open(os.path.join(HERE, 'gn', WOOD_UNITS[u.name] + ('-thaesaen' if u.name == 'W08' else '') + '.gn2'), encoding='utf-8').read(), re.M)
    return m.group(1) if m else None


def render_seal(ctx, p, hit):
    u = unit(hit[0])
    if u.name == 'W08':
        key = 'VI-2-thaesaen'
        canon = [cb for cb in u.codes if cb['text'].lstrip().startswith('round VI-2-thaesaen')][-1]['text']
        extra = (' VI.2 is known from ten hearts, one to each Throne: band I (rings 1 to 3) and the shared rings of band II '
                 '(4 to 11) are the same in all ten but for the root, each Throne&rsquo;s own line; each Throne&rsquo;s entry '
                 '(ring 12, and in Eirlenth&rsquo;s and Neivaere&rsquo;s hearts rings 12 to 14) is drawn below from its own heart; '
                 'the closing rings are the same in every heart but for its haven; and in the bark, in the seal&rsquo;s cup, '
                 'stands the Throne&rsquo;s name.')
    else:
        key = WOOD_UNITS[u.name]
        canon = [cb for cb in u.codes if re.match(r'(?:#[^\n]*\n)*round ', cb['text'] + '\n')][-1]['text']
        extra = ''
    lines, note, K = whole_note(key, canon)
    title = round_title(u)
    h = fig(slot3(key, title, 'whole round'), 'round whole wood-ink', capspan(WHOLE_CAP[u.name]),
            gn_details(lines, 'Grain Notation · the round, its files and its seal', note=note + extra))
    STATS['rounds'] += 1
    ctx.story = True
    return dict(kind='seal', html=h, src='%s:%d' % (u.name, hit[1]), svg3=key)


RING_STOP = re.compile(r'^\*\*(?:[A-Z][a-z]+ · )?Ring \d+\*\*|^#{2,4} |^<!-- RING -->|^\*\*The (?:carving|sentence)')


def ring_extras(u, cb):
    """after a ring's code block, up to the next ring: its literal reading (prose, '- **Reads:**') and the validator's
    printout (a code block after a 'Literal reading' or '**Reads**' label, or a ```text block)"""
    reads, lit = None, None
    i = cb['close']
    while i < len(u.L):
        ln = u.L[i]
        if RING_STOP.match(ln):
            break
        if ln.startswith('```'):
            j = i + 1
            while j < len(u.L) and not u.L[j].startswith('```'):
                j += 1
            prev = ' '.join(u.L[max(cb['close'], i - 3):i])
            if ln.startswith('```text') or 'Literal reading' in prev or '**Reads**' in prev:
                if lit is None:
                    lit = '\n'.join(u.L[i + 1:j])
                i = j + 1
                continue
            break           # the next ring's code (IV.2's ring 24 in two blocks)
        m = re.match(r'^-\s*\*\*Reads:?\*\*:?\s*(.+)$', ln)
        if m and not reads:
            reads = m.group(1).strip()
        i += 1
    return reads, lit


def render_ring(ctx, p, hit):
    if hit is None:
        log('  !! %s L%d: no ring for a story paragraph' % (ctx.anchor, p['line']))
        return dict(kind='missing', html='<!-- no ring for this paragraph -->')
    u = unit(hit[0])
    cb = u.code_at(hit[1])
    code = cb['text']
    m = re.match(r'(?:#[^\n]*\n)*round (\S+)', code + '\n')
    if m:
        return render_cited(ctx, p, u, cb, m.group(1))
    rk = re.search(r'^\s*r(\d+)[·/]', code, re.M)
    key, k_label = wood_key(u, hit[1])
    k = k_label or int(rk.group(1))
    pk = '%s_r%02d' % (key, k)
    reads, lit = ring_extras(u, cb)
    lines = ring_gn([ln for ln in code.split('\n') if not ln.lstrip().startswith('#')])
    nth = hit[3]
    if ctx.ring_prev == (key, k):
        # the second paragraph a ring holds (A26: IV.2's ring 24; V.6's Song inside ring 23)
        if nth == 0:
            fold = gn_details(lines, 'Grain Notation · ring %d, its last knowings' % k, reads=reads, lit_pre=lit)
        else:
            pk_lines = [ln for ln in lines if 'pocket' in ln]
            fold = gn_details(pk_lines, 'Grain Notation · ring %d, what the groves sang (its said-pockets)' % k) if pk_lines else ''
        h = ('<div class="plate-cont wood-ink"><p class="cont-cap">Ring %d holds this paragraph too</p>%s</div>' % (k, fold))
        b = dict(kind='ring-cont', html=h, src='%s:%d' % (u.name, hit[1]), ring=k, svg3=pk)
        STATS['ring-cont'] += 1
        return b
    ctx.ring_prev = (key, k)
    cap = 'Ring %d' % k
    if u.name == 'W08' and 12 <= k and (key != 'VI-2-thaesaen' or (k_label and 'entry' == ring_part(u, hit[1]))):
        cap = 'Ring %d of the heart of %s' % (k, key.split('-')[-1].title())
    elif u.name == 'W08' and k >= 13:
        cap = 'Ring %d: each heart&rsquo;s own fall (Thaesaen&rsquo;s drawn; the same in all ten but for the haven)' % k
    elif u.name == 'W08' and k <= 11:
        cap = 'Ring %d (Thaesaen&rsquo;s heart; the same ring in all ten)' % k
    label = 'Grain Notation · ring %d' % k
    if u.name == 'W08' and (key != 'VI-2-thaesaen' or ring_part(u, hit[1]) == 'entry'):
        label = 'Grain Notation · %s, ring %d' % (key.split('-')[-1].title(), k)
    h = fig(slot3(pk, '%s, ring %d' % (key, k), 'plate'), 'plate wood-ink', capspan(cap),
            gn_details(lines, label, reads=reads, lit_pre=lit))
    STATS['plates'] += 1
    return dict(kind='ring', html=h, src='%s:%d' % (u.name, hit[1]), ring=k, svg3=pk)


def ring_part(u, line):
    """VI.2: is this ring a Throne's own entry ('**Name · Ring k**') or a shared ring ('**Ring k**')?"""
    for j in range(line - 1, 0, -1):
        if re.match(r'^\*\*[A-Z][a-z]+ · Ring \d+\*\*', u.L[j - 1]):
            return 'entry'
        if re.match(r'^\*\*Ring \d+\*\*', u.L[j - 1]):
            return 'shared'
    return None


CITED_KEY = {('W03', 'IV-4-gift'): 'GIFT', ('W06', 'V-4-grow'): 'V-4-grow'}
CITED_CAP = {'GIFT': 'The sentence&rsquo;s own round, cited in ring 23: the gift&rsquo;s carving, its root <em>stop</em>',
             'V-4-grow': 'The carving&rsquo;s own round, cited in ring 17: the first carving of the war, its root <em>grow</em>'}


def render_cited(ctx, p, u, cb, rid):
    key = CITED_KEY[(u.name, rid)]
    stop = next((i for i in range(cb['close'], len(u.L)) if RING_STOP.match(u.L[i])), len(u.L))
    words, reads = carving_reads(u, cb, stop)
    lit = None
    # W03 prints the gift's literal reading as a block after 'Literal reading (of IV-4-gift):'
    for i in range(cb['close'], min(len(u.L), cb['close'] + 40)):
        if u.L[i].startswith('Literal reading (of') and u.L[i].strip().endswith(':'):
            j = i + 1
            while j < len(u.L) and not u.L[j].startswith('```'):
                j += 1
            q = j + 1
            while q < len(u.L) and not u.L[q].startswith('```'):
                q += 1
            lit = '\n'.join(u.L[j + 1:q])
            break
    lines = [ln for ln in cb['text'].split('\n')]
    h = fig(slot3(key, CITED_CAP[key], 'cited round'), 'round cited wood-ink', capspan(CITED_CAP[key]),
            gn_details(lines, 'Grain Notation · %s, the cited round' % rid, reads=reads, lit_pre=lit))
    STATS['rounds'] += 1
    return dict(kind='cited', html=h, src='%s:%d' % (u.name, cb['open']), svg3=key)


# ---------------------------------------------------------------------------- the stone leaves' carvings
def attached_rounds(u, it):
    """the rounds a stone unit sets with a paragraph: before it (V.2's planks: the round, then the paragraph) and
    after it (VI.3's sliver, the Two Homes' chip, the Knowings' Burn), each drawn as its own round"""
    if u.name.startswith('W'):
        return [], []
    if u.name == 'S11' and it['line'] < u.after_table:
        return [], []
    line = it['line']
    nonround = u.nonround_items
    prev = max([l for l in nonround if l < line] or [0])
    before = []
    for cb in rounds_in(u, prev, line):
        if not any(cb['close'] < l < line for l in nonround) and round_owner(u, cb, prev, line) == 'next':
            before.append(carving_fig(u, cb, line))
    a = it['eline'] or line
    b = min(min([l for l in nonround if l > a] or [len(u.L) + 1]), u.next_heading_after(a))
    after = []
    for cb in rounds_in(u, a, b):
        if round_owner(u, cb, a, b) == 'prev':
            after.append(carving_fig(u, cb, b))
    return before, after


PARA_LABEL = re.compile(r'^\*\*¶\s*\d+')


def round_owner(u, cb, a, b):
    """a round set between two items belongs to the next one when the next one's paragraph label (**¶n**) stands
    before the round (V.2: '**¶18** · E1-02, and Seren's gloss', the round, then the paragraph); else to the one before
    (VI.3's sliver after ¶19, the Two Homes' chip after the song, the Knowings' Burn)"""
    after_lab = any(PARA_LABEL.match(u.L[i]) for i in range(cb['close'], min(b - 1, len(u.L))))
    before_lab = any(PARA_LABEL.match(u.L[i]) for i in range(max(a, 0), cb['open'] - 1))
    if before_lab and not after_lab:
        return 'next'
    return 'prev'


CARVE_CAP = {
    'E1-01': 'E1-01, the first plank&rsquo;s order, as the wood cut it',
    'BURN': '<em>Burn</em>, cut in the Fall: the one sign more',
    'VI-1': 'The green sliver&rsquo;s round: its one sign, with the rest folded into it',
    'VI-1-twohomes': 'The song&rsquo;s third line, the wood&rsquo;s own, cut on a chip of end-grain',
}


def carving_fig(u, cb, stop):
    key = u.round_key[cb['first']]
    rid = re.match(r'(?:#[^\n]*\n)*round (\S+)', cb['text']).group(1)
    draw = key
    if key in FAILED or key not in FRESH:
        # the knowing-form copy the renderer cannot read: draw the unit's canonical copy of the same round
        alts = [k for k in u.round_key.values() if k != key and re.sub(r'_\d+$', '', k) == re.sub(r'_\d+$', '', key) and k in FRESH]
        assert alts, key
        draw = alts[0]
        log('  .. %s drawn from %s (the knowing form does not render)' % (key, draw))
    words, reads = carving_reads(u, cb, stop)
    cap = CARVE_CAP.get(rid) or ('%s, as the wood cut it' % rid)
    lines = cb['text'].split('\n')
    lab = 'Grain Notation · %s' % rid
    if words:
        body = gn_details(lines, lab, reads=words, lit_label='The wood&rsquo;s words')
        if reads:
            body = body.replace('</div></details>', '<p class="lit"><span class="lit-h">Literal reading</span> %s</p></div></details>' % md_inline(reads))
    else:
        body = gn_details(lines, lab, reads=reads)
    # the head the unit gives the round in Seren's ink, when an item stands right under it with no English of the
    # Book's (the Knowings' *Vorr.* for Burn)
    head = ''
    nxt = min([l for l in u.nonround_items if l > cb['close']] or [len(u.L) + 1])
    if nxt <= stop and nxt in u.by_line and not any(cb2['first'] in u.round_key and cb['close'] < cb2['first'] < nxt for cb2 in u.codes):
        it2 = u.by_line[nxt]
        if it2['eng'] and C.norm(it2['eng']) not in BOOK_NORMS:
            head = ink_para(it2['orr'], 'ink-cap', None, 'Romanisation · Seren&rsquo;s head for it')
    STATS['carvings'] += 1
    cls = 'carving' + (' songline' if 'twohomes' in rid else (' inscr' if rid.startswith('VI-1') else ''))
    return fig(slot3(draw, cap.replace('&rsquo;', '’').replace('<em>', '').replace('</em>', ''), 'carving'), 'round %s wood-ink' % cls,
               capspan(cap) + head, body)


BOOK_NORMS = set()


def mark_tokens(code):
    toks = []
    for ln in code.split('\n'):
        m = re.match(r'^\s*r\d+[/·]\d+\s+(.*)$', ln)
        if m:
            toks += [x.strip() for x in re.split(r'\s{2,}', m.group(1)) if ':' in x]
    return toks


def render_stone_ring(ctx, p, u, it):
    """a carved line a stone leaf quotes, given by its unit as the ring(s) it reads from (V.7: the bearer's planks):
    the round drawn whole, its excerpt in the fold; a single ring set inside a line of Seren's (V.7 Part II: *Under it
    was cut:* ⟦grain⟧) is that ring's plate, inline, between her words"""
    cb = u.code_at(it['line'])
    code = cb['text']
    toks = mark_tokens(code)
    best, key = 0, None
    for k2 in sorted(set(u.round_key.values())):
        g = os.path.join(HERE, 'gn', k2 + '.gn2')
        if not (os.path.exists(g) and k2 in FRESH):
            continue
        gt = open(g, encoding='utf-8').read()
        sc = sum(1 for t in toks if t.split(':', 1)[1].strip().split('<')[0] in gt)
        if sc > best:
            best, key = sc, k2
    assert key, (u.name, it['line'])
    rings = sorted({int(x) for x in re.findall(r'^\s*r(\d+)[/·]', code, re.M)})
    reads = None
    lit = []
    for i in range(cb['close'], min(len(u.L), cb['close'] + 30)):
        ln = u.L[i]
        if ln.startswith('```') or ln.startswith('> ') or ln.startswith('#'):
            break
        m = re.match(r'^(\d+)\.\s+(.+)$', ln)
        if m:
            lit.append(m.group(2))
    if lit:
        reads = ' '.join(lit)
    lines = ring_gn(code.split('\n'))
    # the inline case: Seren's line around the carving
    pre = next((x for x in u.items if x['kind'] == 'bq' and 0 < it['line'] - x['line'] <= 8 and '⟦grain⟧' in x['orr']), None)
    if pre is not None and len(rings) == 1:
        pk = '%s_r%02d' % (key, rings[0])
        words = re.search(r'\*([^*]+)\*', p['text'])
        words = words.group(1) if words else ''
        f = fig(slot3(pk, 'Ring %d of %s: the thing it had been cut against' % (rings[0], key.split('_', 1)[1]), 'inline plate'),
                'plate inline wood-ink', capspan('What the carving was cut against: %s&rsquo;s ring %d' % (key.split('_', 1)[1], rings[0])),
                gn_details(lines, 'Grain Notation · %s, ring %d' % (key.split('_', 1)[1], rings[0]), reads=words,
                           lit_label='The wood&rsquo;s words') .replace('</div></details>', ('<p class="lit"><span class="lit-h">Literal reading</span> %s</p></div></details>' % md_inline(reads)) if reads else '</div></details>'))
        STATS['plates'] += 1
        full = ' '.join(x.strip() for x in pre['orr'].split('\n'))
        a1, a2 = full.split('⟦grain⟧', 1)
        parts = [ink_para(a1, '', None, 'Romanisation · to the carving', wood_italics=True)]
        parts.append(f)
        if clean_rom(a2):
            parts.append(ink_para(a2, 'ink-wood', None, 'Romanisation · after the carving'))
        return dict(kind='carving', html='\n'.join(parts), src='%s:%d' % (u.name, pre['line']), role='wood', svg3=pk)
    cap = {'S09_E4-01': 'The bearer&rsquo;s plank, E4-01: three roads, one hour',
           'S09_E5-02': 'The deceiving hull&rsquo;s plank, E5-02: come as the young wood came',
           'S09_V7-III': 'The end of a whole morrow, from a bearer&rsquo;s heart'}.get(key, 'The carving')
    words = clean_rom(p['text'])
    body = gn_details(code.split('\n'), 'Grain Notation · %s, as the leaf cites it' % key.split('_', 1)[1], reads=words,
                      lit_label='The wood&rsquo;s words')
    if reads:
        body = body.replace('</div></details>', '<p class="lit"><span class="lit-h">Literal reading</span> %s</p></div></details>' % md_inline(reads))
    STATS['carvings'] += 1
    h = fig(slot3(key, cap.replace('&rsquo;', '’'), 'carving'), 'round carving inscr wood-ink', capspan(cap), body)
    return dict(kind='carving', html=h, src='%s:%d' % (u.name, it['line']), role='wood', svg3=key)


# ---------------------------------------------------------------------------- native drawings
NATIVE_GRAIN = {'legend_wave_chip': 'S07_V1-face', 'legend_stone_rings': 'STONE_bare'}


def find_caption_item(u, texts, used_lines):
    keys = [C.norm(t) for t in texts]
    for it in u.items:
        if it['line'] in used_lines:
            continue
        for e in it['engs'] or []:
            e2 = '\n'.join(x[1:].lstrip(' ') if x.startswith('>') else x for x in e.split('\n'))
            if C.norm(e2) in keys or C.norm(e2.split('\n')[0]) == keys[0]:
                return it
    return None


def render_native(ctx, p, hits):
    nid = p['nid']
    owner = C2.owner(p['line'])
    u = unit(owner)
    used = {h[1] for h in HITS_ALL.values() if h[0] == owner}
    cap_hit = hits.get(p['cap_line'])
    body_hits = [hits.get(l) for l in p['body_lines']]
    cap_it = u.by_line[cap_hit[1]] if cap_hit else find_caption_item(u, [p['cap'], p['cap'] + '\n' + '\n'.join(p['body'])], used)
    cap_two = bool(cap_it and len([x for x in cap_it['orr'].split('\n') if x.strip()]) >= 2 and not cap_hit and p['body'])
    w = wrap_of(ctx, p)
    # the caption: in Seren's ink where her unit gives it; else the Book's English, the plate's quiet title
    if cap_it:
        if cap_two:
            lines = [x for x in cap_it['orr'].split('\n') if x.strip()]
            cap = ink_para(lines[0], 'ink-cap', None, 'Romanisation · Seren’s caption',
                           extra=''.join(rom_p(clean_rom(x)) for x in lines[1:]))
            cap += ''.join('<div class="ip"><p class="ink ink-cap" lang="x-orrowen">%s</p></div>' % ink_line(x) for x in lines[1:])
        else:
            cap = ink_para(cap_it['orr'], 'ink-cap', None, 'Romanisation · Seren’s caption')
        cap_src = '%s:%d' % (u.name, cap_it['line'])
    else:
        cap = capspan(md_inline(p['cap']))
        cap_src = None
        STATS['caption-english'] += 1
    # the body (the fold): Orrowen where given
    body_inks = []
    for bl, bh, btxt in zip(p['body_lines'], body_hits, p['body']):
        if bh:
            it = u.by_line[bh[1]]
            body_inks.append((btxt, it))
    kind = 'native' if p['fence'] == 'native' else 'note'
    b = dict(kind=kind, nid=nid, src=cap_src)
    if w:
        b.update(w)
    special = NATIVE_SPECIAL.get(nid)
    if special:
        b['html'] = special(ctx, p, u, cap, body_inks, cap_it)
        if ' unset"' in b['html'].split('>')[0]:
            b['owed'] = True
        return b
    if kind == 'note':
        chips = ''
        if ctx.anchor == 't-II-2':
            chips = '<div class="note-chip">%s</div>' % slot3('NAELEAR_chip', 'Naelear, those of the breath', 'II.2 note')
        elif ctx.anchor == 't-IV-2':
            chips = '<div class="note-chip">%s%s</div>' % (frag_chips()['legend_iv2_gap1'], frag_chips()['legend_iv2_gap2'])
        nlab = 'Romanisation · Seren’s gloss, when the name is told' if ctx.anchor == 't-II-2' else 'Romanisation · Seren’s note'
        inks = ''.join(ink_para(it['orr'], 'ink-cap', None, nlab) for _, it in body_inks)
        b['html'] = '<div class="native-note ink-note">%s%s%s</div>' % (chips, cap, inks)
        return b
    det = ''
    if body_inks:
        det = ('<details class="tr"><summary>In Seren&rsquo;s ink</summary><div class="tr-body">%s</div></details>'
               % ''.join(ink_para(it['orr'], 'ink-cap', None, 'Romanisation') for _, it in body_inks))
    if nid in NATIVE_GRAIN:
        art = slot3(NATIVE_GRAIN[nid], strip_md(p['cap']), 'native (grain)')
        cls = '%s wood-ink' % (p['size'] or 'chip')
    elif native_exists(nid):
        art = slot_native(nid, strip_md(p['cap']))
        cls = p['size'] or 'line'
    else:
        STATS['native-owed'] += 1
        b['owed'] = True
        b['html'] = '<figure class="native %s unset"><figcaption>%s%s</figcaption></figure>' % (p['size'] or 'chip', cap, det)
        return b
    b['html'] = fig(art, cls, cap, det)
    return b


def nat_stonwryt_hal(ctx, p, u, cap, body_inks, cap_it):
    """the foreword's Stonwryt: the Book's drawing; the Hal and Halyna's reading in the fold; and cut dry"""
    hal = clean_rom(body_inks[0][1]['orr']) if body_inks else ''
    living = next((it for it in u.items if clean_rom(it['orr']).startswith('Es ston et hald sy')), None)
    lv = clean_rom(living['orr']) if living else ''
    det = ('<details class="tr"><summary>The Hal, and {{Halyna}}&rsquo;s reading</summary><div class="tr-body">'
           '<p><em>%s</em> &middot; the gate &middot; signed <em>ALD | BEN</em> under one lintel, the pair-name of <span class="pair">Aldwena</span>, who laid the capstone.</p>'
           '%s</div></details>' % (E(re.sub(r'\s*⟨.*$', '', hal)), ink_para(lv, 'ink-cap', None, 'Romanisation · as {{Halyna}} say it in the living tongue') if lv else ''))
    det = det.replace('{{Halyna}}', '<span class="pair">Halyna</span>')
    out = [fig(slot_native('legend_stonwryt_hal', strip_md(p['cap'])), 'line stone-ink', cap, det)]
    out.append(fig(slot3('CHISEL_stonwryt', 'The Stonwryt, cited dry', 'dry cut'), 'line chisel stone-ink',
                   capspan('The Stonwryt cited dry, in the living tongue, as the guild cuts a stone today'),
                   '<details class="tr"><summary>The dry cut · <em>ryt broc</em></summary><div class="tr-body">'
                   '<p class="tok-line"><code>@ston @hald | @cadh+A.n , @tess+A.n , @somm @tolm @tolm | #gate</code></p>'
                   '<p>The stones only; the mortar words are the reader&rsquo;s: <em>%s</em></p></div></details>' % E(lv)))
    STATS['chisel'] += 1
    return '\n'.join(out)


TITLE_ROM = 'Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.'


def nat_title(ctx, p, u, cap, body_inks, cap_it):
    """the Title drawn in the Captain's coal (or under the capstone): the Book's drawing; its words in the fold"""
    det = ('<details class="tr rom"><summary>Romanisation · the Title</summary><div class="tr-body">%s'
           '</div></details>' % rom_p(TITLE_ROM))
    nid = p['nid']
    if native_exists(nid):
        return fig(slot_native(nid, strip_md(p['cap'])), p['size'] or 'line', cap, det)
    STATS['native-owed'] += 1
    return '<figure class="native %s unset"><figcaption>%s%s</figcaption></figure>' % (p['size'] or 'line', cap, det)


def nat_stone_rings(ctx, p, u, cap, body_inks, cap_it):
    fdet = ('<details class="tr"><summary>The facing leaf</summary><div class="tr-body"><p>The Stone&rsquo;s own rings, '
            'with no mark cut in them: no knowing of <span class="pair">Halyna</span>&rsquo;s filled this leaf. When the Epilogue is laid, the same '
            'rings carry the Last Carver&rsquo;s marks, and that is the Epilogue&rsquo;s own leaf. There is no Grain Notation '
            'to give: the round is bare.</p></div></details>')
    STATS['rounds'] += 1
    return fig(slot3('STONE_bare', 'The Stone’s own rings, with no mark cut in them', 'facing leaf'), 'round wood-ink', cap, fdet)


def nat_seren_note(ctx, p, u, cap, body_inks, cap_it):
    """I.1's facing leaf: Seren's one line, drawn in the course-hand (the Book's drawing) and in her ink"""
    line = ink_para(body_inks[0][1]['orr'], 'ink-seren', None, 'Romanisation · Seren’s line') if body_inks else ''
    art = slot_native('legend_seren_note', strip_md(p['cap'])) if native_exists('legend_seren_note') else ''
    return ('<figure class="native line seren-note">%s<figcaption>%s%s</figcaption></figure>'
            % (('<div class="art">%s</div>' % art) if art else '', cap, line))


def nat_wave(ctx, p, u, cap, body_inks, cap_it):
    """V.1's facing leaf: the Wave as Seren drew it, the sign (a chip of the grain), her caption in her ink"""
    STATS['carvings'] += 1
    return ('<figure class="native chip wood-ink"><div class="art">%s</div><figcaption>%s%s</figcaption></figure>'
            % (slot3('S07_V1-face', 'The Wave, as Seren drew it', 'V.1 facing leaf'), cap,
               gn_details(['round V1-face {wood: plain; kind: chip; rings: 1; rules after: []}', '  I', '    r1/1  0: WAVE'],
                          'Grain Notation · the sign', reads='The Wave: ahead (the shore) goes to the shore, all at once (a chip: plain wood, no pith, no ring of its own).')))


def nat_stone_epilogue(ctx, p, u, cap, body_inks, cap_it):
    """the Epilogue's Stone: the Book's drawing (the Last Carver's letters across the grain); in the fold the grain on
    the Stone as the wood holds it (its round), and the Book's own line in Seren's ink"""
    blk = [cb for cb in u.codes if cb['text'].lstrip().startswith('round STONE')][-1]
    words = clean_rom(p['body'][1]) if len(p['body']) > 1 else ''
    line = ink_para(body_inks[-1][1]['orr'], 'ink-frame', None, 'Romanisation · the Book’s own line') if body_inks else ''
    STATS['rounds'] += 1
    inner = ('<p>The letters are read at once, above, with the eyes. The grain under them was known by no one at this hearth: '
             'this is it, as the wood holds it.</p>'
             '<figure class="native round wood-ink"><div class="art">%s</div></figure>'
             '<pre class="gn">%s</pre><p class="lit"><span class="lit-h">The wood&rsquo;s words</span> <em>%s</em></p>'
             % (slot3('S10_STONE', 'The grain on the Stone, as the wood holds it', 'Epilogue'), E(blk['text'].strip('\n')), E(words)))
    inner += '<p>And one line in the Book&rsquo;s own voice, in Seren&rsquo;s ink:</p>' + line
    det = '<details class="tr gn-fold"><summary>The grain on the Stone · Grain Notation</summary><div class="tr-body">%s</div></details>' % inner
    art = slot_native('legend_stone_epilogue', strip_md(p['cap'])) if native_exists('legend_stone_epilogue') else ''
    return fig(art, 'stone', cap, det)


NATIVE_SPECIAL = {'legend_stonwryt_hal': nat_stonwryt_hal, 'legend_title_coal': nat_title, 'legend_title_capstone': nat_title,
                  'legend_stone_rings': nat_stone_rings, 'legend_seren_note': nat_seren_note, 'legend_wave_chip': nat_wave,
                  'legend_stone_epilogue': nat_stone_epilogue}


# ---------------------------------------------------------------------------- the Book of Knowings' table
def knowings_roots():
    """S11's table: its four column heads, and each root's section: name and look, carvings, the Throne"""
    L = unit('S11').L
    heads = None
    for ln in L:
        if ln.startswith('| *Et meskrivull'):
            heads = [clean_rom(x) for x in ln.strip('|').split('|')]
            break
    starts = [i for i, ln in enumerate(L) if re.match(r'^#### \d+ · ', ln)]
    end_all = next(i for i, ln in enumerate(L) if ln.startswith('### After the table'))
    roots = []
    for n, i in enumerate(starts):
        j = starts[n + 1] if n + 1 < len(starts) else end_all
        sec = L[i:j]
        r = {'title': sec[0][5:], 'look': None, 'carvings': [], 'throne': None, 'judgement': None, 'line': i + 1}
        q = 0
        mode = None
        while q < len(sec):
            ln = sec[q]
            if ln.startswith('> ') and r['look'] is None:
                r['look'] = ln[2:]
            m = re.match(r'^\*\*((?:E\d|T)-\d+)\*\* · (.*)$', ln)
            if m:
                cid = m.group(1)
                tide = re.search(r'\*([^*]+)\*', m.group(2))
                c = {'id': cid, 'tide': tide.group(1) if tide else '', 'code': '', 'head': '', 'head_en': '', 'whole': ''}
                a = next(x for x in range(q, len(sec)) if sec[x].startswith('```'))
                b = next(x for x in range(a + 1, len(sec)) if sec[x].startswith('```'))
                c['code'] = '\n'.join(sec[a + 1:b])
                x = b + 1
                while x < len(sec) and not re.match(r'^\*\*((E\d|T)-\d+|Whose)', sec[x]) and not sec[x].startswith('---'):
                    s = sec[x]
                    if s.startswith('> ') and not c['head']:
                        c['head'] = s[2:]
                    elif s.startswith('*') and not s.startswith('**') and c['head'] and not c['head_en']:
                        c['head_en'] = s.strip()
                    if 'The grain holds the whole carved line' in s:
                        c['whole'] = s.split(':', 1)[1].strip() if ':' in s else ''
                    x += 1
                if mode == 'throne':
                    r['judgement'] = c
                else:
                    r['carvings'].append(c)
                q = x
                continue
            if ln.startswith('**Whose it was at the last**'):
                mode = 'throne'
                y = next(x for x in range(q, len(sec)) if sec[x].startswith('> '))
                r['throne'] = sec[y][2:]
                q = y + 1
                continue
            q += 1
        roots.append(r)
    return heads, roots


KN = None


def render_table_row(ctx, p, k):
    global KN
    if KN is None:
        KN = knowings_roots()
    heads, roots = KN
    if k == 'table-head':
        STATS['ink'] += 1
        h = ('<div class="k-heads"><div class="ip verse-ink k-cols"><div class="verse ink" lang="x-orrowen">%s</div>%s</div></div>'
             % (''.join('<span class="l">%s</span>' % ink_line(x) for x in heads),
                rom_details(heads, 'Romanisation · the four columns of Seren’s table')))
        return dict(kind='table-head', html=h, src='S11:table', wrap='knowings', wrap_id='knowings-table')
    cells = [x.strip() for x in p['text'].strip('|').split('|')]
    name = strip_md(cells[0])
    r = next(x for x in roots if x['title'].split(', ')[-1].strip() == name or x['title'].endswith(name))
    out = ['<div class="k-root" role="group" aria-label="%s">' % A(re.sub(r'[*_]', '', r['title']))]
    out.append('<div class="k-look">%s</div>' % ink_para(r['look'], 'ink-root', None, 'Romanisation · the root, and what it looks like'))
    cards = []
    for c in r['carvings']:
        heng = re.sub(r'[*]', '', c['head_en'])
        sl = slot3('S11_%s' % c['id'], '%s: %s' % (c['id'], heng), 'Knowings')
        STATS['carvings'] += 1
        words = re.sub(r'\*', '', c['whole']).strip() or heng
        fold = gn_details(c['code'].split('\n'), 'Grain Notation · %s' % c['id'], reads=words, lit_label='The whole carved line')
        cards.append('<figure class="native k-card wood-ink"><div class="art">%s</div><figcaption>%s%s</figcaption></figure>'
                     % (sl, ink_verse([c['head'], c['tide']], 'Romanisation', 'k-head'), fold))
    out.append('<div class="k-carvings">%s</div>' % '<span class="k-arrow" aria-hidden="true">&rarr;</span>'.join(cards))
    th = [ink_para(r['throne'], 'ink-throne', None, 'Romanisation · whose it was at the last')]
    if r['judgement']:
        c = r['judgement']
        sl = slot3('S11_%s' % c['id'], '%s: the Judgement' % c['id'], 'Knowings')
        STATS['carvings'] += 1
        words = re.sub(r'\*', '', c['whole']).strip()
        th.append('<figure class="native k-card judgement wood-ink"><div class="art">%s</div><figcaption>%s%s</figcaption></figure>'
                  % (sl, ink_verse([c['head'] or c['tide'], c['tide']] if c['head'] else [c['tide']], 'Romanisation', 'k-head'),
                     gn_details(c['code'].split('\n'), 'Grain Notation · %s' % c['id'], reads=words or None, lit_label='The whole carved line')))
    out.append('<div class="k-last">%s</div>' % ''.join(th))
    out.append('</div>')
    return dict(kind='table-row', html='\n'.join(out), src='S11:%d' % r['line'], wrap='knowings', wrap_id='knowings-table',
                svg3=['S11_%s' % c['id'] for c in r['carvings']] + (['S11_%s' % r['judgement']['id']] if r['judgement'] else []))


# ============================================================================ the CSS (the old Original's, and v3's)
EXTRA_CSS = r"""
/* ---- The Legends, Original tab: the leaf-hand typed in Garl Flenn, the grain drawn ---- */
@font-face{font-family:'Garl Flenn';src:url(data:font/woff2;base64,@@FONT@@) format('woff2');font-display:block}
.p-orig{--face-ink:'Garl Flenn',var(--face-stone)}
.ink{font-family:'Garl Flenn',var(--face-stone);font-weight:400;font-style:normal;letter-spacing:normal;word-spacing:.12em;font-size-adjust:none;font-synthesis:none;font-variant-ligatures:normal;color:var(--stone-ink);overflow-wrap:break-word}
.tale .ink,.prose .ink,.tp-ink .ink,blockquote .ink,.read .ink,.pane .ink{font-family:'Garl Flenn',var(--face-stone);font-weight:400;font-style:normal;letter-spacing:normal;font-size-adjust:none}
.pane p.ink[data-voice="a"]{color:var(--ink)}
.pane p.ink[data-voice="b"],.tale p.ink[data-voice="b"],.prose p.ink[data-voice="b"]{color:var(--ink-b)}
.ink .ink-wood,.ink.ink-wood,.verse.ink .l.ink-wood{color:var(--wood-ink)}
.ink.ink-mixed{color:var(--wood-ink)}
.ink .tok{border-bottom:1px dotted currentColor}
.ink-p{font-family:var(--face-stone);opacity:.7;margin:0 .08em}
.ink-gap{font-family:var(--face-stone);opacity:.6;letter-spacing:.1em}
.ink-blot{font-family:var(--face-stone);letter-spacing:0;margin:0 .06em;white-space:nowrap}
.pane p.ink.ink-name,.pane p.ink.ink-answer,.pane p.ink.ink-title,.pane p.ink.ink-seren,.tp-ink p.ink,p.ink.ink-book,p.ink.ink-booksub{text-wrap:balance}
.ip{margin:0 0 1.15em}
.pane p.ink{font-size:calc(1.46rem * var(--fit,1));line-height:1.78;margin:0}
.ip.first p.ink::first-letter{color:inherit;font-size:inherit;float:none;margin:0;padding:0;line-height:inherit;font-family:inherit}
.ip details.tr{margin:.25em 0 0;max-width:none}
.ip details.tr summary{text-align:left;padding:1px 0}
.ip details.tr .tr-body{margin-top:.35em}
.pane .ip details.tr .tr-body p{font-size:.98rem}
.pane p.ink.ink-name{text-align:center;color:var(--gold-m);font-size:1.7rem;line-height:1.5;margin:0}
.ip:has(> p.ink.ink-name){margin:-4px 0 1.3em}
.ip:has(> p.ink.ink-name) details.tr summary,.ip:has(> p.ink.ink-book) details.tr summary,.ip:has(> p.ink.ink-booksub) details.tr summary,.ip:has(> p.ink.ink-dateline) details.tr summary{text-align:center}
.pane p.ink.ink-book{text-align:center;color:var(--gold-m);font-size:1.62rem;line-height:1.5;margin:0}
.pane p.ink.ink-booksub{text-align:center;color:var(--page-dim);font-size:1.2rem;line-height:1.6;margin:0}
.pane p.ink.ink-dateline{text-align:center;color:var(--page-dim);font-size:1.12rem;line-height:1.6;margin:0}
.pane p.ink.ink-teller{color:var(--page-dim);font-size:1.22rem;line-height:1.75}
.pane p.ink.ink-laid{color:var(--page-dim);font-size:1.3rem}
.pane p.ink.ink-frame{color:var(--page-dim);font-size:1.26rem}
.pane p.ink.ink-inscr{margin-left:1.2em;font-size:1.34rem}
.pane p.ink.ink-answer{text-align:center;color:var(--gold-m);font-size:1.42rem}
.pane p.ink.ink-answer.ink-silent,.pane p.ink.ink-answer.ink-hood{color:var(--page-dim)}
.ip:has(> p.ink.ink-answer) details.tr summary{text-align:center}
.pane p.ink.ink-title{text-align:center;color:var(--gold-m);font-size:1.55rem;line-height:1.7}
.ip.title-ink{margin:1.3em 0 .4em}
.ip.title-ink details.tr summary{text-align:center}
.pane p.ink.ink-seren{text-align:center;font-size:1.3rem}
.ip:has(> p.ink.ink-seren) details.tr summary{text-align:center}
.pane p.ink.ink-marked{margin-top:.2em}
.pane p.ink.ink-reading{font-size:1.36rem;line-height:1.7;margin-left:1.2em}
.pane .ip:has(> p.ink.ink-reading){margin-bottom:.55em}
.pane p.ink.ink-toc,.pane p.ink.ink-toc-tale,.pane p.ink.ink-toc-arg{font-size:1.18rem;line-height:1.6}
.pane p.ink.ink-toc-arg{color:var(--page-dim)}
.verse.ink{font-size:calc(1.36rem * var(--fit,1));line-height:1.72;margin:.6em 0 .2em 2.2em}
.verse.ink .l{display:block}
.ip.verse-ink{margin-bottom:1.3em}
.ip.part-ink{margin:1.7em 0 .9em;text-align:center}
.ip.part-ink h4.part.ink{font-family:'Garl Flenn',var(--face-stone);font-variant:normal;letter-spacing:normal;font-size:1.5rem;color:var(--gold-m);margin:0;text-transform:none}
.ip.part-ink details.tr summary{text-align:center}
p.ink.ink-cap{font-size:1.15rem;color:var(--page-dim);text-align:center;line-height:1.6}
figure.native .svg-slot,figure.native .art > svg,figure.native .art > img{display:block;margin:0 auto}
figure.native.chisel .art svg{width:min(560px,100%)}
figure.native.plate{margin:1.4em auto 1.5em}
figure.native.plate .art svg{width:min(600px,100%)}
figure.native.plate figcaption .cap,figure.native.carving figcaption .cap{font-family:'IBM Plex Mono',monospace;font-style:normal;font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--grain)}
figure.native.whole{width:min(900px,calc(100vw - 80px));margin-left:50%;transform:translateX(-50%)}
figure.native.whole .art svg{width:100%}
figure.native.whole details.tr{max-width:40rem;margin-left:auto;margin-right:auto}
figure.native.cited{margin:1.2em auto 1.4em}
figure.native.cited .art svg{width:min(320px,80%)}
figure.native.carving .art svg{width:min(260px,70%)}
figure.native.carving.inscr .art svg{width:min(340px,86%)}
figure.native.carving.songline .art svg{width:min(300px,80%)}
figure.native.chip .art svg{width:104px}
figure.native.seren-note .art svg{width:min(420px,90%)}
figure.native.unset{min-height:0}
.carved-para{margin:0 0 .4em}
.carved-para figure.native.carving{margin:1.2em auto .5em}
.plate-cont{margin:-.6em auto 1.4em;max-width:600px;text-align:center}
.plate-cont .cont-cap{font-family:'IBM Plex Mono',monospace;font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--grain);margin:0 0 .2em}
.frag{display:inline-block;vertical-align:middle}
.frag svg{display:inline-block;height:2.2em;width:auto;margin:0 .15em}
.frag.untold svg{outline:1px dashed rgba(159,176,138,.45);outline-offset:2px;border-radius:2px}
.native-note.ink-note{margin:.2em auto 1.4em;max-width:32rem}
.native-note.ink-note .note-chip{display:flex;justify-content:center;gap:10px}
.native-note.ink-note .note-chip svg{display:block;margin:0 auto .3em;height:2.4em;width:auto}
.native-note.ink-note .ip{margin-bottom:.5em}
pre.gn{font-family:'IBM Plex Mono',monospace;font-size:.66rem;line-height:1.55;color:#c3ccb4;white-space:pre;overflow-x:auto;margin:0 0 .6em;padding:0 0 4px;tab-size:4;text-align:left}
pre.gn.lit-gn{color:var(--page-dim)}
details.tr .tr-body p.lit{font-family:var(--face-stone);font-size:.98rem;line-height:1.5;color:var(--page-dim);margin:.3em 0 0;text-align:left}
.lit-h{font-family:'IBM Plex Mono',monospace;font-size:.58rem;letter-spacing:1.4px;text-transform:uppercase;color:var(--grain);margin-right:.5em}
details.tr .tr-body code{font-size:.74em}
details.gn-fold .tr-body figure.native{margin:.6em auto}
p.tok-line{overflow-x:auto;white-space:nowrap}
/* the romanisation, word over word (v3.1.0): each word in the romanisation's italic, its English beneath it, small,
   in the mono face, dimmer; the words stay inline text, so the line wraps as words wrap. font-size-adjust:none, for
   the stone face sets these lines everywhere: inside a wood leaf they took the leaf's adjust (.405), and the mono
   glosses fell from 10.2px to about 8px (wf13 reader check). A mark between the words (span.m) keeps a word's space
   after it; the blotted name's box is upright, as the ink sets the blots. */
details.tr .tr-body p.il{font-family:var(--face-stone);font-style:italic;font-weight:400;font-size-adjust:none;line-height:1.35;color:var(--page);text-align:left;margin:0 0 .35em}
details.tr .tr-body p.il:last-child{margin-bottom:0}
.il i{display:inline-flex;flex-direction:column;align-items:flex-start;vertical-align:baseline;font-style:italic;margin:0 .36em .5em 0}
.il i small{font-family:'IBM Plex Mono',monospace;font-style:normal;font-weight:400;font-size:.65em;letter-spacing:.01em;line-height:1.25;color:var(--page-dim);margin-top:.15em;-webkit-user-select:none;user-select:none}
.il i.blot{font-style:normal;letter-spacing:0}
.il .m{margin-right:.36em}
.il .sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;border:0;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap;-webkit-user-select:none;user-select:none}
/* the Book of Knowings: Seren's table, a root to a row, each carving drawn */
.k-heads{border-bottom:1px solid var(--border);padding-bottom:.4em;margin-bottom:.4em}
.k-heads .ip{margin:0}
.ip.k-cols .verse.ink{margin:.2em 0;font-size:1.1rem;line-height:1.6;color:var(--gold-m);columns:2 16rem;column-gap:24px}
.ip.k-cols .verse.ink .l{break-inside:avoid}
.k-root{border-bottom:1px solid var(--border);padding:.9em 0 1em}
.k-look p.ink.ink-root{font-size:1.32rem;color:var(--gold-m);text-align:left}
.k-carvings{display:flex;flex-wrap:wrap;align-items:flex-start;gap:6px 4px;margin:.5em 0}
.k-arrow{align-self:center;color:var(--page-dim);font-size:1.2rem;padding:0 2px}
figure.native.k-card{margin:0;flex:0 1 148px;min-width:128px}
figure.native.k-card .art svg{width:min(140px,100%)}
figure.native.k-card .ip{margin:.2em 0 .1em}
figure.native.k-card .ip.verse-ink{margin:.2em 0 .1em}
figure.native.k-card .verse.ink{margin:0;font-size:1.06rem;line-height:1.45;text-align:center}
figure.native.k-card .verse.ink .l{padding-left:0;text-indent:0}
figure.native.k-card .verse.ink .l+.l{font-size:.86em;color:var(--page-dim)}
figure.native.k-card details.tr summary{text-align:center;font-size:.72rem}
.k-last{display:flex;flex-wrap:wrap;align-items:center;gap:6px 16px;margin-top:.3em}
.k-last .ip{flex:1 1 280px;margin:0}
.k-last p.ink.ink-throne{font-size:1.18rem;color:var(--page-dim)}
figure.native.k-card.judgement{flex:0 1 160px}
svg.gdefs{position:absolute;width:0;height:0;overflow:hidden}
/* a drawing is laid out only when it nears the screen (the pane holds some four hundred of them) */
figure.native.plate,figure.native.whole,figure.native.carving,figure.native.k-card,figure.native.stone,figure.native.cited{content-visibility:auto}
figure.native.plate{contain-intrinsic-size:auto 640px}
figure.native.whole{contain-intrinsic-size:auto 900px}
figure.native.carving{contain-intrinsic-size:auto 320px}
figure.native.k-card{contain-intrinsic-size:auto 260px}
@SHARED@
@media(max-width:768px){
 .pane p.ink{font-size:calc(1.26rem * var(--fit,1));line-height:1.74}
 .pane p.ink.ink-name{font-size:1.4rem}
 .pane p.ink.ink-book{font-size:1.36rem}
 .pane p.ink.ink-title{font-size:1.28rem}
 .pane p.ink.ink-teller{font-size:1.1rem}
 .pane p.ink.ink-reading{margin-left:.4em;font-size:1.18rem}
 .verse.ink{margin-left:.6em;font-size:1.16rem}
 figure.native.whole{width:100%;margin-left:0;transform:none}
 figure.native.k-card{flex:1 1 140px;min-width:130px}
 figure.native.plate{contain-intrinsic-size:auto 400px}
 figure.native.whole{contain-intrinsic-size:auto 420px}
}
"""


def shared_css():
    """the renderer's shared <style> (the same in every drawing), once for the page: read from one rendered round"""
    s = open(os.path.join(SVG3, 'II-2_r01.svg'), encoding='utf-8').read()
    st = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    assert st.startswith(':root.wood-ink{'), st[:40]
    return st, re.sub(r'^:root\.wood-ink\{[^}]*\}', '', st)


# ============================================================================ main
HITS_ALL = {}


def main():
    global HITS_ALL
    hits, used, byu = pair_book()
    lv = leaves()
    hits.update(pair_front(lv['front'] + lv.get('contents', [])))
    HITS_ALL = hits
    for p in C.book_paras():
        BOOK_NORMS.add(C.norm(p['text']))
    out = collections.OrderedDict()
    for anchor, paras in lv.items():
        log('== %s (%d paragraphs)' % (anchor, len(paras)))
        out[anchor] = build_leaf(anchor, paras, hits)
    # a marker after a leaf's last paragraph (I.1's FACING LEAF) rides on that block
    keys = list(out)
    for i, a in enumerate(keys):
        last = out[a][-1]
        nxt = out[keys[i + 1]][0]['line'] if i + 1 < len(keys) else len(BL) + 1
        tail = markers_before(nxt, last['end_line'])
        if tail:
            last['markers_after'] = tail
    # the interlinear (v3.1.0): every line of every romanisation fold is set word over word
    n_p = n_il = 0
    for bl in out.values():
        for b in bl:
            for m in re.finditer(r'<details class="tr rom"><summary>.*?</summary><div class="tr-body">(.*?)</div></details>', b['html'], re.S):
                ps = re.findall(r'<p\b[^>]*>', m.group(1))
                n_p += len(ps)
                n_il += sum(1 for x in ps if x == '<p class="il">')
    if n_p != n_il:
        raise SystemExit('romanisation lines not set word over word: %d of %d' % (n_p - n_il, n_p))
    STATS['interlinear-lines'] = INTERLINEAR['lines']
    STATS['interlinear-words'] = INTERLINEAR['words']
    log('interlinear: %d fold lines, %d set word over word (%d words glossed), %d without a word; %d mark(s) after a '
        'span of words moved into its last word; %d mark(s) between the words spaced as words; %d blotted name(s) '
        'boxed and glossed %s' % (n_p, INTERLINEAR['lines'], INTERLINEAR['words'],
                                  INTERLINEAR['lines without a word'], INTERLINEAR['marks moved into the last word of a span'],
                                  INTERLINEAR['marks between the words'], INTERLINEAR['blotted names glossed'], BLOT_GLOSS))
    json.dump(out, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    font = base64.b64encode(open(FONT, 'rb').read()).decode('ascii')
    full, shared = shared_css()
    css = EXTRA_CSS.replace('@@FONT@@', font).replace('@SHARED@', "/* the grain renderer's shared rules, once for the page */\n" + shared)
    open(OUT_CSS, 'w', encoding='utf-8').write(css)
    n = sum(len(v) for v in out.values())
    kinds = collections.Counter(b['kind'] for v in out.values() for b in v)
    lines = ['panes: %d leaves, %d blocks' % (len(out), n), 'kinds: %s' % dict(kinds), 'stats: %s' % dict(STATS),
             'flags (%d): %s' % (len(FLAGS), FLAGS[:20]), 'svg3 keys used: %d' % len([k for k in USED if not k.startswith('native:')])]
    open(OUT_LOG, 'w', encoding='utf-8').write('\n'.join(lines + LOG) + '\n')
    json.dump({'used': USED, 'stats': STATS, 'flags': FLAGS, 'kinds': kinds}, open(os.path.join(HERE, 'panes_stats.json'), 'w'), indent=1, ensure_ascii=False)
    print('\n'.join(lines))
    print('problems:', sum(1 for r in LOG if '!!' in r))


if __name__ == '__main__':
    main()
