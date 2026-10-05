#!/usr/bin/env python3
"""Build THE LEGENDS OF RIVENKEEP, the story page (Rivenkeep_Legends.html, v3.1.0; wf13, 2026-10-04).

    python3 build_story_html.py --doc-version "v3.1.0" [--out DIR]
        -> DIR/Rivenkeep_Legends.html            (the page for Docs/, beside Rivenkeep_Legends_Notes.html)
        -> DIR/web/The_Legends_of_Rivenkeep.html (the private web copy for claude.ai, the host's page contract)
    (DIR defaults to $RK_OUT, else wf13/out)

Sources, three texts of one Book:
  * The Book:     wf11/book_v3.md   (THE LEGENDS OF RIVENKEEP, Book v3.0.0, the final English; unchanged)
  * Plain Words:  wf13/plain_v31.md (Plain Words v3.1: every paragraph rewritten whole for a reader new to the lore)
  * Original:     wf13/orig/panes.json (one block per Book paragraph, in Seren's ink and the grain; filled by
                  wf13/orig/panes_lib.py, styled by wf13/orig/panes.css, which carries the leaf-hand font; v3.1.0:
                  every romanised line in its fold set word over word, each word over its English)

Changes from v3.0.0 (wf12/book/build_story_html.py), after Jack's notes of 2026-10-03:
  * Plain Words is v3.1 (wf13/plain_v31.md). Its leaves have their own italic 'when' line under the title, a
    sentence or two: set as the Book's dateline is set (p.dateline, the same landmark dl1) wherever the Book's leaf
    has a dateline, the headnote after it as before. The foreword's Plain pane opens with 'A note for new readers',
    set apart, quietly (aside.newreaders, a small mono label over its paragraphs, between two hairlines), before the
    foreword's own dateline and headnote; it carries no landmark, for the Book has no such note.
  * the Original's romanisation folds are interlinear (build_panes.py rom_p): the one switch, the place-keeping
    script, the Book and the rest of the Original are as they were.
The house look is read from Docs/Rivenkeep_Legends.html (its base rules) and this folder's story.css (the reading
face: the fonts, the stone and wood faces and their tints, Halyna's two inks, the lintel over pair-names); the
drawings are wf6/svg's.

The page holds only the story: the title page, the Contents, the foreword, the Invocation, the six Books with their
Arguments, every tale, the Epilogue, the Book of Knowings and its Last Note, and a one-line colophon naming the Notes.

Changes from the v2.0.0 builder (wf10/book/build_story_html.py):
  * ONE SWITCH FOR THE WHOLE BOOK: three radio inputs at the very top of the body (name="read"; read-book checked,
    read-plain, read-orig), visually hidden and position:fixed (focusing one never scrolls); a slim sticky bar under
    the nav, 'The Book · Plain Words · Original', of <label for> those ids; and in every leaf the same three labels,
    for the same ids. CSS sibling selectors (#read-plain:checked ~ .ctn .p-book ...) show the chosen text in every leaf
    and mark the active label everywhere, with no script. The title page's line, the Contents and each Book's Argument
    switch too (Plain Words has its own; the Original sets them in Seren's ink).
  * the Original pane is the full original: every stone paragraph in Seren's ink, every wood leaf's reading in
    Halyna's two inks and its grain, round and rings (panes.json, matched to the Book by its line numbers)
  * v3's short datelines (the first italic line under a title, nine words or fewer, with the italic headnote after it)
    and its one- or two-sentence headnotes (p.teller)
  * the <!-- READING --> block of a wood leaf: the em-dash fragment lines, set apart, in the wood face, a little
    smaller, the two voices alternating in Halyna's two inks, no label; the seal under it (This is held in the grain.)
    set as the bark's, not a story paragraph
  * a small inline script only keeps the reader's place: on a switch it holds the clicked label (a leaf's own bar) or
    the paragraph at the reading line (the sticky bar) where it was, through the anchors the three texts share (the
    Book's line numbers, which the Original's blocks carry, and the landmarks Plain Words keeps: the rings, the parts,
    the drawings, the closes); it remembers the choice in localStorage (inside try/catch) and restores it on load; a
    #tale-anchor in the URL still lands on its tale. Tale anchors stay as they were (t-I-1 ...). It starts the
    leaf-hand (Garl Flenn) loading at once, for a browser fetches a face only when text first needs it: left to the
    first switch to Original, the font arrived after the place was set and the whole Original reflowed under the
    reader (15k px at phone width; the Epilogue's own label was thrown 1,300 px out of view). And it sets the place
    again two frames after a switch and at 150 ms (a drawing that content-visibility had skipped is laid out only
    then, and VI.3's songline, just above the Epilogue, grew 31 px under its label), and once more when the fonts are
    ready if any face was still loading. Each setting is idempotent: when nothing moved, nothing scrolls. An anchor
    within 2 px below the reading line counts as at it: a switch leaves its anchor on the line to a fraction of a
    pixel, and read as the next anchor down it stretched the step across the target's whole gap (the Knowings at
    phone width: Book, Original, Book, Original drifted a paragraph up, 174 px).
"""
import argparse
import html as HTML
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
S = os.path.dirname(W12)
ORIG = os.path.join(W12, 'orig')
SRC = {'book': os.path.join(S, 'wf11', 'book_v3.md'), 'plain': os.path.join(S, 'wf13', 'plain_v31.md')}
HOUSE = '/Users/riquochet/code/Rivenkeep/Docs/Rivenkeep_Legends.html'
SVG_DIR = os.path.join(S, 'wf6', 'svg')
NOTES_HREF = 'Rivenkeep_Legends_Notes.html'
STORE_KEY = 'rk-legends-read'
# the VI.3 token, read as one true state of the game: the Book's own order lays Glasspire last (VI.1)
TOKEN_TEXT = {'LAST_THRONE_AT_HAVEN': 'Neivaere, in the cellars of Glasspire'}
PAIRS = ('Halyna', 'Aldwena', 'Idrenna', 'Orvenna', 'Enrella', 'Wendhessa')
FONTS = ('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700'
         '&family=Crimson+Pro:ital,wght@0,300..600;1,300..600'
         '&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500'
         '&family=IBM+Plex+Mono:wght@400;500&family=Source+Sans+3:wght@300;400;600;700&display=swap')

ap = argparse.ArgumentParser()
ap.add_argument('--doc-version', default='v3.1.0')
ap.add_argument('--out', default=os.environ.get('RK_OUT', os.path.join(W12, 'out')))
ARGS = ap.parse_args()
VERSION = ARGS.doc_version
OUT = os.path.join(ARGS.out, 'Rivenkeep_Legends.html')
OUT_WEB = os.path.join(ARGS.out, 'web', 'The_Legends_of_Rivenkeep.html')

sys.path.insert(0, ORIG)
import panes_lib as PL  # noqa: E402

# ------------------------------------------------------------------ the drawings
class Inliner:
    """every Book/Plain drawing inlined whole, its ids prefixed so that any number can sit on one page (all three
    texts can carry the same drawing), its own <style> dropped (the page carries those rules once)"""
    def __init__(self):
        self.n = 0
        self.drawn = []
        self.owed = []

    @staticmethod
    def exists(name):
        return os.path.exists(os.path.join(SVG_DIR, name + '.svg'))

    @staticmethod
    def fix_mask_ids(s):
        ids = re.findall(r'\bid="([^"]+)"', s)
        for d in sorted({i for i in ids if ids.count(i) > 1}):
            assert len(re.findall(r'<mask id="%s"' % re.escape(d), s)) == 1 and ids.count(d) == 2, d
            s = s.replace('<mask id="%s"' % d, '<mask id="%s-mask"' % d)
            s = s.replace('mask="url(#%s)"' % d, 'mask="url(#%s-mask)"' % d)
        return s

    def svg(self, name):
        s = open(os.path.join(SVG_DIR, name + '.svg'), encoding='utf-8').read().strip()
        s = re.sub(r'^<\?xml[^>]*\?>\s*', '', s)
        s = balance_svg(s, name)
        self.n += 1
        u = 'd%d' % self.n
        self.drawn.append(name)
        s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)
        s = self.fix_mask_ids(s)
        s = re.sub(r'\bid="([^"]+)"', lambda m: 'id="%s-%s"' % (u, m.group(1)), s)
        s = re.sub(r'\bhref="#([^"]+)"', lambda m: 'href="#%s-%s"' % (u, m.group(1)), s)
        s = re.sub(r'url\(#([^)]+)\)', lambda m: 'url(#%s-%s)' % (u, m.group(1)), s)
        s = re.sub(r'aria-labelledby="([^"]+)"',
                   lambda m: 'aria-labelledby="%s"' % ' '.join('%s-%s' % (u, x) for x in m.group(1).split()), s)
        s = re.sub(r'(<use\b[^>]*?)\shref="', r'\1 xlink:href="', s)
        s = re.sub(r'\sdata-[a-z-]+="[^"]*"', '', s)
        if 'focusable=' not in s[:300]:
            s = s.replace('<svg ', '<svg focusable="false" ', 1)
        return s


INL = Inliner()
_native = PL.Filler.native
PL.Filler.native = lambda self, nid, title=None: balance_svg(_native(self, nid, title), nid)
FILL = PL.Filler()          # the Original's drawings: the grain through svgpool, the native ones inline
GLYPH_RE = re.compile(r'⟦([a-z0-9_]+)⟧')

# ------------------------------------------------------------------ inline
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def smart(t):
    out = []
    n = len(t)
    for i, c in enumerate(t):
        if c == '"':
            prev = t[i - 1] if i > 0 else ' '
            nxt = t[i + 1] if i + 1 < n else ' '
            if i == 0 or prev.isspace() or prev in '([{—–\x00':
                out.append('“')
            elif prev == '*' and (nxt.isalnum() or nxt == '…'):
                out.append('“')
            else:
                out.append('”')
        elif c == "'":
            out.append('’')
        else:
            out.append(c)
    return ''.join(out)


def pair(name):
    return '<span class="pair">%s</span>' % name


def inl(t):
    ph = []

    def keep(s):
        ph.append(s)
        return '\x01%d\x01' % (len(ph) - 1)
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)          # builder's markers never reach the page
    t = GLYPH_RE.sub(lambda m: keep('<span class="glyph">%s</span>' % INL.svg(m.group(1))), t)
    t = re.sub(r'\{\{([A-Za-z]+)\}\}', lambda m: keep(pair(m.group(1))), t)
    t = re.sub(r'\{([A-Z_]+)\}', lambda m: keep('<span class="token" data-token="%s">%s</span>'
                                                % (m.group(1), esc(TOKEN_TEXT[m.group(1)]))), t)
    assert '{' not in t and '}' not in t, t[:120]
    t = esc(t)
    t = smart(t)
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\*\w])\*(?=\S)(.+?)(?<=\S)\*(?![\*\w])', r'<em>\1</em>', t)
    if '*' in t:
        raise SystemExit('stray asterisk: ' + t[:200])
    for _ in range(3):
        t = re.sub(r'\x01(\d+)\x01', lambda m: ph[int(m.group(1))], t)
    return t


def put_attrs(h, **kw):
    """add attributes at the end of the first opening tag of an HTML fragment"""
    extra = ''.join(' %s="%s"' % (k.replace('_', '-'), v) for k, v in kw.items() if v)
    if not extra:
        return h
    out, n = re.subn(r'^(\s*<[a-zA-Z][\w-]*\b[^>]*?)(\s*/?>)', lambda m: m.group(1) + extra + m.group(2), h, count=1)
    assert n == 1, h[:80]
    return out


REPAIRED = []


def balance_svg(s, name):
    """close a drawing whose file lost its last </svg> (wf6's legend_stone_epilogue.svg ends one short)"""
    opens = len(re.findall(r'<svg\b[^>]*?(?<!/)>', s))
    closes = s.count('</svg>')
    if opens > closes:
        s += '</svg>' * (opens - closes)
        REPAIRED.append(name)
    return s


def uniq_svg_ids(page):
    """every id on the page once: an inline drawing whose ids another drawing already holds (the dry cuts, set more
    than once, keep their own symbol ids) gets them prefixed anew, with every reference inside it"""
    out, pos, n_fixed = [], 0, 0
    seen = set()
    tag = re.compile(r'<(/?)svg\b[^>]*?(/?)>')
    depth, start = 0, None
    for m in tag.finditer(page):
        if m.group(2):
            continue
        if not m.group(1):
            if depth == 0:
                start = m.start()
            depth += 1
            continue
        depth -= 1
        if depth:
            continue
        seg = page[start:m.end()]
        ids = re.findall(r'\bid="([^"]+)"', seg)
        if any(i in seen for i in ids):
            n_fixed += 1
            u = 'u%d-' % n_fixed
            idset = set(ids)
            seg = re.sub(r'\bid="([^"]+)"', lambda q: 'id="%s%s"' % (u, q.group(1)), seg)
            seg = re.sub(r'(\bhref=")#([^"]+)"', lambda q: '%s#%s%s"' % (q.group(1), u if q.group(2) in idset else '', q.group(2)), seg)
            seg = re.sub(r'url\(#([^)]+)\)', lambda q: 'url(#%s%s)' % (u if q.group(1) in idset else '', q.group(1)), seg)
            seg = re.sub(r'aria-labelledby="([^"]+)"', lambda q: 'aria-labelledby="%s"' % ' '.join(
                (u + x if x in idset else x) for x in q.group(1).split()), seg)
            ids = re.findall(r'\bid="([^"]+)"', seg)
        seen.update(ids)
        out.append(page[pos:start])
        out.append(seg)
        pos = m.end()
    out.append(page[pos:])
    return ''.join(out), n_fixed

# ------------------------------------------------------------------ blocks (each with its first source line, 1-based)
LIST_RE = re.compile(r'^(- |\d+\. )')


def collect(ls, i, base):
    """ls[i] opens a ::: block (v3: a caption line, then the English, paragraphs split by blank lines)"""
    parts = ls[i].strip()[4:].split()
    if parts[0] == 'native':
        assert len(parts) == 3 and parts[2] in ('round', 'line', 'chip', 'stone'), ls[i]
        head = {'kind': 'native', 'name': parts[1], 'size': parts[2]}
    else:
        assert parts == ['note'], ls[i]
        head = {'kind': 'note'}
    j = i + 1
    inner = []
    while ls[j].strip() != ':::':
        assert not ls[j].strip().startswith('::: '), 'nested ::: at %d' % j
        inner.append(ls[j])
        j += 1
    while inner and not inner[0].strip():
        inner.pop(0)
    head['caption'] = inner[0].strip()
    paras, buf = [], []
    for x in inner[1:]:
        if x.strip():
            buf.append(x.strip())
        elif buf:
            paras.append(' '.join(buf))
            buf = []
    if buf:
        paras.append(' '.join(buf))
    head['body'] = paras
    return {'t': 'native', 'head': head, 'line': base + i}, j + 1


def parse_blocks(ls, base=1):
    """ls: the lines; base: the source line number of ls[0]"""
    blocks = []
    i = 0
    N = len(ls)
    while i < N:
        l = ls[i]
        s = l.strip()
        if not s:
            i += 1
            continue
        if s.startswith('::: '):
            b, i = collect(ls, i, base)
            blocks.append(b)
            continue
        if s.startswith('<!--'):
            buf = [l]
            at = i
            while '-->' not in ls[i]:
                i += 1
                buf.append(ls[i])
            blocks.append({'t': 'comment', 'text': '\n'.join(buf), 'line': base + at})
            i += 1
            continue
        m = re.match(r'^(#{1,6}) (.*)$', l)
        if m:
            blocks.append({'t': 'h', 'level': len(m.group(1)), 'text': m.group(2).strip(), 'line': base + i})
            i += 1
            continue
        if s == '---':
            blocks.append({'t': 'hr', 'line': base + i})
            i += 1
            continue
        if l.startswith('|'):
            rows, at = [], i
            while i < N and ls[i].startswith('|'):
                rows.append(ls[i])
                i += 1
            blocks.append({'t': 'table', 'rows': rows, 'line': base + at})
            continue
        if l.startswith('>'):
            buf, at = [], i
            while i < N and ls[i].startswith('>'):
                buf.append(re.sub(r'^> ?', '', ls[i]))
                i += 1
            blocks.append({'t': 'quote', 'buf': buf, 'line': base + at})
            continue
        if LIST_RE.match(l):
            items, at = [], i
            while i < N and LIST_RE.match(ls[i]):
                items.append(LIST_RE.sub('', ls[i], count=1))
                i += 1
            blocks.append({'t': 'list', 'items': items, 'line': base + at})
            continue
        if re.match(r'^\s{2,}\S', l):
            raise SystemExit('stray indented line %d: %r' % (base + i, l[:80]))
        buf, at = [], i
        while i < N:
            x = ls[i]
            if not x.strip() or x.startswith(('#', '|', '>', '<!--', ':::')) or LIST_RE.match(x) or x.strip() == '---':
                break
            buf.append(x)
            i += 1
        blocks.append({'t': 'p', 'buf': buf, 'line': base + at})
    return blocks


def ptext(b):
    return ' '.join(x.strip() for x in b['buf'])

# ------------------------------------------------------------------ helpers
ANSWERS = ('*And the hearth said: We remember.*', '*And everyone at the hearth said: We remember.*')
SILENT = ('*And no one answered.*',)
HOOD = ('*And the Captain put his hood back.*', '*And the Captain pushed his hood back.*',
        # Plain Words v3.1 says who the Captain is as it closes IV.3 and the Epilogue
        '*And the Captain, who leads us and had kept his hood up through every tale before, put his hood back.*',
        '*And the Captain, who keeps his hood up at this hearth, put it back. It was only the second time.*')
LAID = ('This I lay as it was laid for me.', 'This we lay as it was laid for us.',
        'I have laid this tale the way it was laid for me.', 'We have laid this tale the way it was laid for us.')
SEAL = 'This is held in the grain.'
MARK_NAMES = {'Rhyna': 'a', 'Halvard': 'b'}
OTHER_PAIRS = [p for p in PAIRS if p != 'Halyna']


def fully_italic(t):
    return bool(re.match(r'^\*(?!\*)[^*]+\*$', t))


def bold_only(t):
    return bool(re.match(r'^\*\*[^*]+\*\*$', t))


def n_words(t):
    return len(re.findall(r"[A-Za-z{}][A-Za-z'{}-]*", t))


def tale_id(num):
    return 't-' + num.replace('.', '-')


def attrs(cls=None, **kw):
    o = ''
    if cls:
        o += ' class="%s"' % ' '.join(cls)
    for k, v in kw.items():
        if v is not None:
            o += ' %s="%s"' % (k.replace('_', '-'), v)
    return o


def is_verse(buf):
    ls = [x.rstrip() for x in buf]
    return len(ls) >= 2 and all(x and x.startswith('*') and x.endswith('*') for x in ls)


def verse_html(buf, wood_lines=(), cls=None):
    o = ['<div class="verse%s">' % (' ' + cls if cls else '')]
    for n, x in enumerate(buf, 1):
        o.append('<span class="l%s">%s</span>' % (' wood' if n in wood_lines else '', inl(x.rstrip())))
    o.append('</div>')
    return '\n'.join(o)


def table_html(rows, wood_col, line, key=None):
    """key(line) -> the data-k of a row (the Book's line), or None"""
    def cells(r):
        r = r.strip()
        if r.startswith('|'):
            r = r[1:]
        if r.endswith('|'):
            r = r[:-1]
        return [c.strip() for c in r.split('|')]
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    o = ['<div class="tw wide"><table>']
    o.append('<thead><tr%s>' % attrs(data_k=key(line) if key else None)
             + ''.join('<th scope="col">%s</th>' % inl(c) for c in head) + '</tr></thead><tbody>')
    labels = [re.sub(r'<[^>]+>', '', inl(c)).replace('"', '&quot;') for c in head]
    for n, r in enumerate(body):
        # data-label: the column's head, shown above each cell when a phone stacks the row
        o.append('<tr%s>' % attrs(data_k=key(line + 2 + n) if key else None, data_m='row%d' % (n + 1))
                 + ''.join('<td%s data-label="%s">%s</td>' % (' class="wood"' if j == wood_col else '', labels[j], inl(c))
                           for j, c in enumerate(r)) + '</tr>')
    o.append('</tbody></table></div>')
    return '\n'.join(o)


def native_html(head):
    """a drawing (if it has been drawn), its quiet caption, and the English in a plain <details> fold"""
    cap = '<span class="cap">%s</span>' % inl(head['caption'])
    fold = ''
    if head['body']:
        fold = ('<details class="tr"><summary>Translation</summary><div class="tr-body">%s</div></details>'
                % ''.join('<p>%s</p>' % inl(p) for p in head['body']))
    if head['kind'] == 'note':
        return '<div class="native-note">%s%s</div>' % (cap, fold)
    if Inliner.exists(head['name']):
        return ('<figure class="native %s"><div class="art">%s</div><figcaption>%s%s</figcaption></figure>'
                % (head['size'], INL.svg(head['name']), cap, fold))
    INL.owed.append(head['name'])
    return ('<figure class="native %s unset"><figcaption>%s%s</figcaption></figure>' % (head['size'], cap, fold))

NEWREADERS = '**A note for new readers**'


def is_newreaders(b):
    """Plain Words v3.1: the foreword opens with a note for new readers (a blockquote whose first line is its title)"""
    return b['t'] == 'quote' and bool(b['buf']) and b['buf'][0].strip() == NEWREADERS


def newreaders_html(b):
    """the note for new readers, set apart, quietly: its quiet label, then its paragraphs; no landmark (the Book has
    no such note), no drop cap, and the leaf's head (its dateline, its headnote) still to come after it"""
    inner = parse_blocks(b['buf'], b['line'])
    assert inner and inner[0]['t'] == 'p' and ptext(inner[0]) == NEWREADERS, inner[:1]
    assert all(x['t'] == 'p' for x in inner[1:]), [x['t'] for x in inner]
    label = re.sub(r'^\*\*|\*\*$', '', NEWREADERS)
    return ('<aside class="newreaders" aria-labelledby="newreaders-h">\n<h3 class="nr-h" id="newreaders-h">%s</h3>\n%s\n</aside>'
            % (label, '\n'.join('<p>%s</p>' % inl(ptext(x)) for x in inner[1:])))

# ------------------------------------------------------------------ one text of one leaf
class Pane:
    """one text (The Book or Plain Words) of one leaf. Every element it sets from a source paragraph carries that
    paragraph's line (data-k="b<line>", the Book only: the Original's blocks carry the same) and, where it is a
    landmark both texts keep, data-m (the ring, the part, the drawing, the close, counted in the leaf)"""
    def __init__(self, unit_kind, keyed):
        self.out = []
        self.unit_kind = unit_kind     # 'tale' | 'prose' | 'invocation' | 'knowings'
        self.keyed = keyed             # the Book: data-k on every element
        self.head = True               # before the headnote
        self.dated = False
        self.dateline_line = None
        self.first_done = False
        self.ink = []
        self.halyna = False
        self.told_halyna = False
        self.marked = False
        self.voice = 'a'
        self.after_part = False
        self.w_block = False
        self.w_lead = None             # 'W: the italic carvings only': leading italics of the next run
        self.w_words = []
        self.w_em = False
        self.w_inscr = 0
        self.w_lines = set()
        self.mixed = False
        self.reading = False
        self.hal_new = False
        self.w_new = False
        self.count = {}
        self.line_m = {}               # the Book's line -> its landmark
        self.n_voiced = 0
        self.book_dated = False        # Plain Words v3.1: the Book's leaf has a dateline, so this text's 'when' line is one
        self.more_notes = False        # Plain Words v3.1: a headnote may run to a second italic paragraph (II.2, IV.4)
        self.n_note = 0
        self.n_more_notes = 0

    def mark(self, kind):
        self.count[kind] = self.count.get(kind, 0) + 1
        return '%s%d' % (kind, self.count[kind])

    def key(self, line):
        return 'b%d' % line if (self.keyed and line) else None

    def emit(self, s, line=None, m=None):
        if line and m:
            self.line_m.setdefault(line, m)
        self.out.append(put_attrs(s, data_k=self.key(line), data_m=m))

    def check(self, where):
        left = [n for n, v in (('W', self.w_block), ('W em', self.w_em), ('W inscr', self.w_inscr),
                               ('W words', self.w_words), ('W lines', self.w_lines), ('MIXED', self.mixed),
                               ('READING', self.reading)) if v]
        if left or self.w_lead:
            raise SystemExit('unconsumed markers %s at %s' % (left or ['W lead'], where))

    def comment(self, text):
        body = text[4:-3].strip()
        if body == 'HALYNA':
            # the halves a cue promised are this stretch's own (Plain Words v3.1 says 'one of them began and the other
            # finished:' before IV.1's HALYNA lines): the cue's inks must not run on past it
            self.ink = []
            self.halyna = self.told_halyna = True
            self.voice = 'a'
            self.hal_new = True
        elif body == 'HALYNA END':
            assert self.halyna
            self.halyna = self.marked = False
        elif body == 'MARKED':
            assert self.halyna
            self.marked = True
        elif body == 'READING':
            self.reading = True
            self.told_halyna = True
        elif body == 'RING':
            self.emit('<div class="ring" aria-hidden="true"></div>', m=self.mark('ring'))
        elif body == 'W':
            self.w_block = True
            self.w_new = True
        elif body == 'W: the italic carvings only':
            self.w_lead = 'armed'
            self.w_words = ['Burn']
            self.w_new = True
        elif body == 'W: the italic line only':
            self.w_em = True
            self.w_new = True
        elif body == 'W: the three italic lines only':
            self.w_inscr = 3
            self.w_new = True
        elif body == 'W: line 3 only':
            self.w_lines = {3}
            self.w_new = True
        elif body.startswith('MIXED'):
            self.mixed = True
        elif re.match(r'^(PROLOGUE EXCERPT (BEGIN|END)|FACING LEAF|RIPENS|TOKEN)', body):
            pass
        else:
            raise SystemExit('unknown marker: ' + body[:80])

    def landmark(self, default):
        """the landmark of the element about to be set: a HALYNA stretch's or a W passage's first, else default"""
        if self.hal_new:
            self.hal_new = False
            return self.mark('hal')
        if self.w_new:
            self.w_new = False
            return self.mark('w')
        return self.mark(default) if default else None

    def role_cls(self):
        if self.w_block:
            self.w_block = False
            return ['wood']
        if self.mixed:
            self.mixed = False
            return ['mixed']
        return []

    def inline_wood(self, h):
        if self.w_em:
            assert '<em>' in h, 'W italic line: no italic in ' + h[:80]
            h = h.replace('<em>', '<em class="wood">')
            self.w_em = False
        if self.w_lead:
            if h.startswith('<em>'):
                h = h.replace('<em>', '<em class="wood">', 1)
                self.w_lead = 'run'
            elif self.w_lead == 'run':
                self.w_lead = None
        for w in list(self.w_words):
            if '<em>%s</em>' % w in h and not self.w_lead:
                h = h.replace('<em>%s</em>' % w, '<em class="wood">%s</em>' % w, 1)
                self.w_words.remove(w)
        return h

    def reading_html(self, b):
        """the fragments {{Halyna}} spoke as the wood gave the memory up: one line each, the two voices by turns"""
        self.reading = False
        lines = [x.rstrip() for x in b['buf']]
        assert lines and all(x.strip().startswith('*—') and x.strip().endswith('*') for x in lines), lines[:2]
        self.emit('<div class="reading">', m=self.landmark('rd'))
        voice = 'a'
        for n, x in enumerate(lines):
            self.line_m.setdefault(b['line'] + n, 'frag%d' % (n + 1))
            self.out.append('<p class="rd-line"%s>%s</p>' % (
                attrs(data_k=self.key(b['line'] + n), data_m='frag%d' % (n + 1), data_voice=voice), inl(x.strip())))
            self.n_voiced += 1
            voice = 'b' if voice == 'a' else 'a'
        self.out.append('</div>')

    def para(self, b):
        t = ptext(b)
        line = b['line']
        after_part, self.after_part = self.after_part, False
        if self.reading:
            return self.reading_html(b)
        if line == self.dateline_line:
            self.dated = True
            self.emit('<p class="dateline">%s</p>' % inl(t), line, self.mark('dl'))
            return
        if self.head:
            self.head = False
            if t.startswith('*'):
                self.emit('<p class="teller">%s</p>' % inl(t), line, self.mark('hn'))
                self.more_notes = not self.keyed
                return
        if self.more_notes:
            # Plain Words v3.1: the headnote's second italic paragraph, straight after the first, is the headnote still
            # (no landmark of its own: the Book's headnote is one paragraph)
            if fully_italic(t) and t not in ANSWERS + SILENT + HOOD + LAID:
                self.out.append('<p class="teller">%s</p>' % inl(t))
                self.n_more_notes += 1
                return
            self.more_notes = False
        role = self.role_cls()
        if t == SEAL:
            self.emit('<p class="seal">%s</p>' % inl(t), line, self.landmark('seal')); return
        if t in ANSWERS:
            self.emit('<p class="answer">%s</p>' % inl(t), line, self.landmark('ans')); return
        if t in SILENT:
            self.emit('<p class="answer silent">%s</p>' % inl(t), line, self.landmark('ans')); return
        if t in HOOD:
            self.emit('<p class="answer hood">%s</p>' % inl(t), line, self.landmark('ans')); return
        if t in LAID:
            self.emit('<p class="laid">%s</p>' % inl(t), line, self.landmark('laid')); return
        if bold_only(t):
            if t.startswith('**IN MEMORY'):
                self.emit('<p class="title-line">%s</p>' % inl(t), line, self.landmark('tl'))
            else:
                self.emit('<h4 class="part">%s</h4>' % inl(t[2:-2]), line, self.landmark('part'))
                self.voice = 'a'
                self.after_part = True
            return
        if t.startswith('***Added'):
            self.emit('<p class="frame added">%s</p>' % inl(t), line, self.landmark('add')); return
        if t.startswith('*') and (t.endswith(':') or t.endswith(':*')):
            self.emit('<p class="frame">%s</p>' % inl(t), line, self.landmark('fr')); return
        if fully_italic(t):
            if after_part:
                self.emit('<p class="frame who-line">%s</p>' % inl(t), line, self.landmark('who')); return
            cls = ['inscr'] + role
            if self.w_inscr:
                cls.append('wood')
                self.w_inscr -= 1
            self.emit('<p%s>%s</p>' % (attrs(cls), self.inline_wood(inl(t))), line, self.landmark(None)); return
        cls = list(role)
        voice = teller = None
        h = inl(t)
        if self.halyna:
            if self.marked:
                m = re.match(r'^<strong>(Rhyna|Halvard)\.</strong> ', h)
                if m:
                    teller = m.group(1)
                    voice = MARK_NAMES[teller]
                    h = '<span class="who">%s.</span> ' % teller + h[m.end():]
                    cls.append('marked')
            else:
                voice = self.voice
                self.voice = 'b' if voice == 'a' else 'a'
        elif self.ink:
            voice = self.ink.pop(0)
        if voice:
            self.n_voiced += 1
        if not self.first_done:
            cls.append('first')
            self.first_done = True
        h = self.inline_wood(h)
        self.emit('<p%s>%s</p>' % (attrs(cls, data_voice=voice, data_teller=teller), h), line, self.landmark(None))
        if not self.halyna:
            halyna_said = not any('{{%s}}' % p in t for p in OTHER_PAIRS)
            # a cue: the next paragraph(s) are the halves, his and hers
            if t.endswith('the other finished:') and halyna_said:
                self.ink = ['a', 'b']
            elif t.endswith('She began it:'):
                self.ink = ['a']
            elif t.startswith('And he ') and t.endswith(':') and len(t) < 80:
                self.ink = ['b']

    def quote(self, b):
        buf = b['buf']
        if is_newreaders(b):
            self.out.append(newreaders_html(b))
            self.n_note += 1
            return
        if is_verse(buf):
            role = self.role_cls()
            self.emit(verse_html(buf, self.w_lines, ' '.join(role) or None), b['line'], self.landmark('verse'))
            self.w_lines = set()
            self.ink = []
            return
        inner = parse_blocks(buf, b['line'])
        if self.unit_kind == 'invocation':
            self.emit('<blockquote class="invocation">', m=self.landmark('q'))
            for x in inner:
                if x['t'] == 'native':
                    self.emit(native_html(x['head']), x['line'], self.mark('nat'))
                    continue
                t = ptext(x)
                if bold_only(t):
                    self.emit('<p class="title-line">%s</p>' % inl(t), x['line'], self.mark('tl'))
                elif t in ANSWERS:
                    self.emit('<p class="answer">%s</p>' % inl(t), x['line'], self.mark('ans'))
                else:
                    self.emit('<p>%s</p>' % inl(t), x['line'])
            self.out.append('</blockquote>')
            return
        # a facing leaf (or II.1's founders' leaf): the wood's leaf, set inside the stone leaf
        self.emit('<blockquote class="grain">', m=self.landmark('q'))
        for x in inner:
            if x['t'] == 'native':
                self.emit(native_html(x['head']), x['line'], self.mark('nat'))
                continue
            self.emit('<p>%s</p>' % inl(ptext(x)), x['line'])
        self.out.append('</blockquote>')

    def block(self, b):
        k = b['t']
        if k != 'p':
            self.more_notes = False
        if k == 'p':
            self.para(b)
        elif k == 'quote':
            if self.head and not is_newreaders(b):
                self.head = False
            self.quote(b)
        elif k == 'comment':
            self.comment(b['text'])
        elif k == 'native':
            self.emit(native_html(b['head']), b['line'], self.landmark('nat'))
        elif k == 'table':
            self.emit(table_html(b['rows'], 2, b['line'], self.key if self.keyed else None), m=self.mark('tbl'))
            for n in range(len(b['rows']) - 2):
                self.line_m.setdefault(b['line'] + 2 + n, 'row%d' % (n + 1))
        elif k == 'hr':
            pass
        else:
            raise SystemExit('unexpected block: %r' % (b,))

    def render(self, blocks, where):
        # the dateline: the first paragraph, fully italic and nine words or fewer, with the italic headnote after it
        ps = [b for b in blocks if b['t'] != 'comment' and not is_newreaders(b)]
        if self.keyed and len(ps) >= 2 and ps[0]['t'] == 'p' and ps[1]['t'] == 'p':
            t0, t1 = ptext(ps[0]), ptext(ps[1])
            if fully_italic(t0) and n_words(t0) <= 9 and t1.startswith('*'):
                self.dateline_line = ps[0]['line']
        # Plain Words v3.1: its own 'when' line, the first paragraph, fully italic (a sentence or two, longer than the
        # Book's), set as the Book's dateline is set wherever the Book's leaf has one
        if not self.keyed and self.book_dated:
            if not (ps and ps[0]['t'] == 'p' and fully_italic(ptext(ps[0]))):
                raise SystemExit('%s: the Book has a dateline, Plain Words no italic when-line first' % where)
            self.dateline_line = ps[0]['line']
        for b in blocks:
            self.block(b)
        self.check(where)
        return '\n'.join(self.out)

# ------------------------------------------------------------------ split a source into its units
SEC_IDS = {
    'CONTENTS': 'contents', 'OF THIS BOOK': 'foreword', 'THE INVOCATION': 'invocation',
    'BOOK ONE · THE BOOK OF THE WALL': 'book-1', 'BOOK TWO · THE BOOK OF THE BUILDERS': 'book-2',
    'BOOK THREE · THE BOOK OF THE HAVENS': 'book-3', 'BOOK FOUR · THE BOOK OF THE WOUND': 'book-4',
    'BOOK FIVE · THE BOOK OF THE TIDES': 'book-5', 'BOOK SIX · THE BOOK OF THE HOMECOMINGS': 'book-6',
    'EPILOGUE': 'epilogue', 'APPENDIX': 'knowings',
}
UNIT_IDS = {'The Stone out of the Grey': 't-epilogue', 'The Book of Knowings': 't-knowings'}
LAST_NOTE = '**The Last Note · Three Stones over the Hearth**'


def split(path):
    blocks = parse_blocks(open(path, encoding='utf-8').read().split('\n'))
    assert blocks[0]['t'] == 'h' and blocks[0]['text'] == 'THE LEGENDS OF RIVENKEEP', blocks[0]
    front, sections = [], []
    cur = None
    unit = None
    for b in blocks[1:]:
        if b['t'] == 'h' and b['level'] == 2 and b['text'] in SEC_IDS:
            cur = {'id': SEC_IDS[b['text']], 'title': b['text'], 'arg': None, 'pre': [], 'units': [], 'line': b['line']}
            sections.append(cur)
            unit = None
            continue
        if cur is None:
            front.append(b)
            continue
        if b['t'] == 'h' and b['level'] == 3:
            m = re.match(r'^((?:VI|IV|V|III|II|I)\.\d+) · (.+)$', b['text'])
            if m:
                unit = {'id': tale_id(m.group(1)), 'num': m.group(1), 'title': m.group(2), 'blocks': [], 'line': b['line']}
            else:
                unit = {'id': UNIT_IDS[b['text']], 'num': None, 'title': b['text'], 'blocks': [], 'line': b['line']}
            cur['units'].append(unit)
            continue
        if b['t'] == 'p' and ptext(b) == LAST_NOTE:
            m = re.match(r'^\*\*(.+) · (.+)\*\*$', LAST_NOTE)
            unit = {'id': 't-last-note', 'num': None, 'kick': m.group(1), 'title': m.group(2), 'blocks': [], 'line': b['line']}
            cur['units'].append(unit)
            continue
        if b['t'] == 'hr':
            continue
        if unit is not None:
            unit['blocks'].append(b)
        elif cur['id'].startswith('book-') or cur['id'] in ('epilogue', 'knowings'):
            assert cur['arg'] is None and b['t'] == 'p', (cur['id'], b)
            cur['arg'] = ptext(b)
            cur['arg_line'] = b['line']
        else:
            cur['pre'].append(b)
    return front, sections


SRCS = {k: split(v) for k, v in SRC.items()}
FRONT, SECS = SRCS['book']
PFRONT, PSECS = SRCS['plain']
assert [s['id'] for s in SECS] == [s['id'] for s in PSECS]
PLAIN = {}
for s in PSECS:
    PLAIN[s['id']] = s
    for u in s['units']:
        PLAIN[u['id']] = u
for s in SECS:
    assert [u['id'] for u in s['units']] == [u['id'] for u in PLAIN[s['id']]['units']], s['id']
    for u in s['units']:
        assert u['title'] == PLAIN[u['id']]['title'], (u['id'], u['title'], PLAIN[u['id']]['title'])

PANES = PL.load()

# ------------------------------------------------------------------ the three texts, and the one switch
TABS = (('book', 'The Book'), ('plain', 'Plain Words'), ('orig', 'Original'))
WRAP_OPEN = {'invocation': ('blockquote', 'invocation'), 'facing': ('blockquote', 'grain'),
             'quote': ('blockquote', 'grain'), 'knowings': ('div', 'knowings')}
STATS = {'orig_blocks': 0, 'orig_keyed': 0, 'shared_m': 0, 'dropped_m': {}, 'plain_datelines': 0, 'plain_notes': 0, 'plain_headnote_2nd': 0}


def leaf_tabs():
    """the leaf's own bar: the same three labels as the sticky bar, for the same three radios"""
    return ('<div class="tabs" role="group" aria-label="Read this in">%s</div>'
            % ''.join('<label class="tab l-%s" for="read-%s">%s</label>' % (k, k, name) for k, name in TABS))


def strip_m(h, keep):
    """drop the landmarks the other text does not keep in the same number"""
    def one(m):
        kind = re.match(r'[a-z]+', m.group(1)).group(0)
        return m.group(0) if kind in keep else ''
    return re.sub(r' data-m="([a-z]+\d+)"', one, h)


def agree(pb, pp, where):
    keep = {k for k in set(pb.count) | set(pp.count) if pb.count.get(k) == pp.count.get(k)}
    keep.update(('frag', 'row'))
    for k in set(pb.count) | set(pp.count):
        if k not in keep:
            STATS['dropped_m'].setdefault(where, []).append('%s %s/%s' % (k, pb.count.get(k, 0), pp.count.get(k, 0)))
    return keep


def orig_pane(anchor, line_m=None, keep=None, toc_href=None):
    """the Original's blocks of one leaf, filled: one per Book paragraph, each with the Book's line (data-k) and the
    Book's landmark there (data-m), so the reader's place can be kept across the switch"""
    out = []
    cur = curw = None
    rings = 0
    in_reading = False
    for b in PANES[anchor]:
        # the wood leaf's READING lines, set apart together as the Book sets them
        if (b['kind'] == 'reading') != in_reading:
            out.append('<div class="reading">' if not in_reading else '</div>')
            in_reading = not in_reading
        w = b.get('wrap_id')
        if w != cur:
            if cur:
                out.append('</%s>' % WRAP_OPEN[curw][0])
            if w:
                curw = b['wrap']
                out.append('<%s class="%s">' % WRAP_OPEN[curw])
            cur = w
        if 'RING' in (b.get('markers') or []):
            rings += 1
            m = 'ring%d' % rings
            out.append('<div class="ring" aria-hidden="true"%s></div>' % (' data-m="%s"' % m if (keep and 'ring' in keep) else ''))
        h = FILL.fill(b['html'])
        if toc_href and b['line'] in toc_href:
            # the Original's Contents: the ink line itself is the link to its leaf
            h, n = re.subn(r'(<p class="ink[^"]*"[^>]*>)(.*?)(</p>)',
                           lambda q: '%s<a class="ink-a" href="#%s">%s</a>%s' % (q.group(1), toc_href[b['line']], q.group(2), q.group(3)),
                           h, count=1, flags=re.S)
            assert n == 1, b['line']
        m = (line_m or {}).get(b['line'])
        if m and keep is not None and re.match(r'[a-z]+', m).group(0) not in keep:
            m = None
        h = put_attrs(h, data_k='b%d' % b['line'], data_m=m)
        STATS['orig_blocks'] += 1
        out.append(h)
    if in_reading:
        out.append('</div>')
    if cur:
        out.append('</%s>' % WRAP_OPEN[curw][0])
    return '\n'.join(out)


def panes3(book_html, plain_html, orig_html):
    return ('<div class="pane p-book" lang="en">\n%s\n</div>\n<div class="pane p-plain" lang="en">\n%s\n</div>\n'
            '<div class="pane p-orig">\n%s\n</div>' % (book_html, plain_html, orig_html))


def leaf_kind(unit):
    if unit['id'] == 't-epilogue':
        return 'seren'
    for b in unit['blocks']:
        if b['t'] == 'comment' and b['text'][4:-3].strip() == 'READING':
            return 'wood'
    return 'stone'


KIND_LABEL = {'stone': 'Stone leaf', 'wood': 'Wood leaf', 'seren': 'The leaf facing I.1'}


def render_leaf(uid, book_blocks, plain_blocks, kind):
    pb = Pane(kind, True)
    pp = Pane(kind, False)
    bh = pb.render(book_blocks, uid + ' book')
    pp.book_dated = pb.dateline_line is not None
    ph = pp.render(plain_blocks, uid + ' plain')
    STATS['plain_datelines'] += 1 if pp.dated else 0
    STATS['plain_notes'] += pp.n_note
    STATS['plain_headnote_2nd'] += pp.n_more_notes
    keep = agree(pb, pp, uid)
    bh, ph = strip_m(bh, keep), strip_m(ph, keep)
    STATS['shared_m'] += len(re.findall(r' data-m=', ph))
    oh = orig_pane(uid, pb.line_m, keep)
    return pb, pp, panes3(bh, ph, oh)

# ------------------------------------------------------------------ the frame: title page, Contents, Book heads
def toc_html(pre, href_of_line=None):
    o = ['<div class="toc">']
    n = 0
    for b in pre:
        if b['t'] == 'p':
            for k, ln in enumerate(b['buf']):
                ln = ln.strip()
                n += 1
                mm = re.match(r'^\*\*(.+?)\*\*(.*)$', ln)
                key = 'b%d' % (b['line'] + k) if href_of_line is not None else None
                if mm:
                    href = TOC_LINKS[mm.group(1)]
                    if href_of_line is not None:
                        href_of_line[b['line'] + k] = href
                    cls = 'toc-front' if mm.group(1) in ('Of This Book', 'The Invocation') else 'toc-book'
                    o.append('<p%s><a href="#%s"><strong>%s</strong></a>%s</p>'
                             % (attrs([cls], data_k=key, data_m='c%d' % n), href, inl(mm.group(1)), inl(mm.group(2))))
                else:
                    assert fully_italic(ln), ln
                    o.append('<p%s>%s</p>' % (attrs(['toc-arg'], data_k=key, data_m='c%d' % n), inl(ln)))
        elif b['t'] == 'list':
            o.append('<ul class="toc-tales">')
            for k, text in enumerate(b['items']):
                n += 1
                key = 'b%d' % (b['line'] + k) if href_of_line is not None else None
                mm = re.match(r'^((VI|IV|V|III|II|I)\.\d+) · (.+?)( · .*)$', text)
                if mm:
                    href = tale_id(mm.group(1))
                    o.append('<li%s><a href="#%s"><span class="tn">%s</span> %s</a>%s</li>'
                             % (attrs(data_k=key, data_m='c%d' % n), href, mm.group(1), inl(mm.group(3)), inl(mm.group(4))))
                else:
                    mm = re.match(r'^(.+?)( · .*)$', text)
                    href = TOC_TALE[mm.group(1)]
                    o.append('<li%s><a href="#%s">%s</a>%s</li>' % (attrs(data_k=key, data_m='c%d' % n), href, inl(mm.group(1)), inl(mm.group(2))))
                if href_of_line is not None:
                    href_of_line[b['line'] + k] = href
            o.append('</ul>')
        else:
            raise SystemExit('contents block %r' % (b,))
    o.append('</div>')
    return '\n'.join(o)


TOC_LINKS = {'Of This Book': 'foreword', 'The Invocation': 'invocation', 'EPILOGUE': 'epilogue', 'APPENDIX': 'knowings'}
for s in SECS:
    if s['id'].startswith('book-'):
        TOC_LINKS[s['title']] = s['id']
TOC_TALE = {'The Stone out of the Grey': 't-epilogue', 'The Book of Knowings': 't-knowings'}

body = []
all_ids = []
leaf_meta = {}
# --- the title page: the Book's name stands over all three; under it, the line each text gives
assert FRONT[0]['t'] == 'h' and FRONT[0]['text'] == '*The Book of the Riven Stone*', FRONT[0]
assert FRONT[1]['t'] == 'p' and PFRONT[1]['t'] == 'p'
assert PFRONT[0]['text'] == FRONT[0]['text']


def tp_text(front, keyed):
    sub = '<p class="tp-sub"%s>%s</p>' % (attrs(data_k='b%d' % front[0]['line'] if keyed else None, data_m='tp1'),
                                         inl(front[0]['text']))
    line = '<p class="tp-line"%s>%s</p>' % (attrs(data_k='b%d' % front[1]['line'] if keyed else None, data_m='tp2'),
                                           inl(ptext(front[1])))
    return '%s\n<div class="tp-orn" aria-hidden="true"></div>\n%s' % (sub, line)


fo = PANES['front']
assert [b['kind'] for b in fo] == ['front-title', 'front-sub', 'front-line'], [b['kind'] for b in fo]
orig_tp = ('%s\n%s\n<div class="tp-orn" aria-hidden="true"></div>\n%s' % (
    put_attrs(FILL.fill(fo[0]['html']), data_k='b%d' % fo[0]['line']),
    put_attrs(FILL.fill(fo[1]['html']), data_k='b%d' % fo[1]['line'], data_m='tp1'),
    put_attrs(FILL.fill(fo[2]['html']), data_k='b%d' % fo[2]['line'], data_m='tp2')))
STATS['orig_blocks'] += 3
body.append('<section id="front" class="front">\n<div class="read">')
body.append('<div class="titlepage">')
body.append('<h1 class="tp-title">THE LEGENDS OF RIVENKEEP</h1>')
body.append('<div class="sw tp-sw">\n%s\n</div>' % panes3(tp_text(FRONT, True), tp_text(PFRONT, False), orig_tp))
body.append('</div>')
body.append('</div>\n</section>')

for s in SECS:
    sid = s['id']
    ps = PLAIN[sid]
    if sid == 'contents':
        body.append('<section id="contents" class="book">\n<div class="read">')
        body.append('<h2 class="book-h">CONTENTS</h2>')
        hrefs = {}
        bk = toc_html(s['pre'], hrefs)
        pl = toc_html(ps['pre'])
        # the Original's Contents: its lines carry the Book's lines, and the c<n> landmarks by their order
        cm = {}
        n = 0
        for b in PANES['contents']:
            if b['kind'] != 'book-head':
                n += 1
                cm[b['line']] = 'c%d' % n
        og = orig_pane('contents', cm, None, hrefs)
        body.append('<div class="sw toc-sw">\n%s\n</div>' % panes3(bk, pl, '<div class="toc toc-ink">\n%s\n</div>' % og))
        body.append('</div>\n</section>')
        continue
    if sid in ('foreword', 'invocation'):
        body.append('<section id="%s" class="book prose-sec">\n<div class="read">' % sid)
        body.append('<h2 class="book-h">%s</h2>' % s['title'])
        kind = 'invocation' if sid == 'invocation' else 'prose'
        pb, pp, three = render_leaf(sid, s['pre'], ps['pre'], kind)
        body.append('<div class="prose stone sw leaf"%s>' % (' data-told="halyna"' if pb.told_halyna else ''))
        body.append(leaf_tabs())
        body.append(three)
        body.append('</div>')
        body.append('</div>\n</section>')
        all_ids.append(sid)
        leaf_meta[sid] = (pb, pp)
        continue
    # a Book, the Epilogue, the Appendix: the heading stands over all three; its Argument is each text's own
    title = s['title']
    body.append('<section id="%s" class="book">\n<div class="read">' % sid)
    if ' · ' in title:
        kick, rest = title.split(' · ', 1)
        body.append('<h2 class="book-h"><span class="kick">%s</span><span class="sep"> · </span>%s</h2>' % (kick, rest))
    else:
        body.append('<h2 class="book-h">%s</h2>' % title)
    og = PANES[sid]
    assert [b['kind'] for b in og] == ['book-head', 'book-arg'], (sid, [b['kind'] for b in og])
    orig_arg = '\n'.join(put_attrs(FILL.fill(b['html']), data_k='b%d' % b['line'], data_m='arg1' if b['kind'] == 'book-arg' else None)
                         for b in og)
    STATS['orig_blocks'] += 2
    body.append('<div class="sw arg-sw">\n%s\n</div>' % panes3(
        '<p class="book-sub" data-k="b%d" data-m="arg1">%s</p>' % (s['arg_line'], inl(s['arg'])),
        '<p class="book-sub" data-m="arg1">%s</p>' % inl(ps['arg']),
        '<div class="book-sub-ink">\n%s\n</div>' % orig_arg))
    for u in s['units']:
        kind = leaf_kind(u)
        role = 'wood' if kind == 'wood' else 'stone'
        uk = 'knowings' if u['id'] == 't-knowings' else 'tale'
        pb, pp, three = render_leaf(u['id'], u['blocks'], PLAIN[u['id']]['blocks'], uk)
        told = ' data-told="halyna"' if pb.told_halyna else ''
        cls = 'tale leaf sw %s%s' % (role, ' seren' if kind == 'seren' else '')
        if u['num']:
            kick = '<span class="tn">%s</span><span class="sep"> · </span>' % u['num']
        elif u.get('kick'):
            kick = '<span class="tn">%s</span><span class="sep"> · </span>' % u['kick']
        else:
            kick = ''
        label = '' if uk == 'knowings' else '<span class="kind">%s</span>' % KIND_LABEL[kind]
        body.append('<article class="%s" id="%s"%s>' % (cls, u['id'], told))
        body.append('<h3 class="tale-h">%s<span class="tt">%s</span>%s</h3>' % (kick, inl(u['title']), label))
        body.append(leaf_tabs())
        body.append(three)
        body.append('</article>')
        all_ids.append(u['id'])
        leaf_meta[u['id']] = (pb, pp)
    body.append('</div>\n</section>')

missing = [a for a in PANES if a not in all_ids + ['front', 'contents'] and not a.startswith('book-') and a not in ('epilogue', 'knowings')]
assert not missing, missing
body_html = '\n'.join(body)
# an inline drawing's own <style> (the dry cuts carry one) never reaches the page: its rules are the page's already
body_html, n_svg_styles = re.subn(r'(<svg\b[^>]*>(?:(?!</svg>).)*?)<style>.*?</style>', r'\1', body_html, flags=re.S)
assert '<style' not in body_html
body_html, n_reprefixed = uniq_svg_ids(body_html)

# ------------------------------------------------------------------ head / style
house = open(HOUSE, encoding='utf-8').read()
m = (re.search(r'<style>\n(.*?)/\* ---- The Legends of Rivenkeep, the story alone', house, re.S)
     or re.search(r'<style>\n(.*?)/\* ---- The Legends: the reading face ---- \*/', house, re.S))
style = m.group(1)
style = re.sub(r'#history\{.*\n', '', style)
# every sticky bar sits under the safe area (the nav is held inside .bars, which is the sticky one)
style, n = re.subn(r'nav\{position:sticky;top:0;', 'nav{position:sticky;top:env(safe-area-inset-top, 0px);', style, count=1)
# (v3.1.0: the house page is now v3.0.0's own build, whose nav already sits under the safe area)
assert n == 1 or (n == 0 and style.count('nav{position:sticky;top:env(safe-area-inset-top, 0px);') == 1)
style, n = re.subn(r'--doc-version:"v[\d.]+"', '--doc-version:"%s"' % VERSION, style, count=1)
assert n == 1
extra = open(os.path.join(HERE, 'story.css'), encoding='utf-8').read()
panes_css = PL.css()

header = '''<header>
<div class="h1">Rivenkeep — The Legends</div>
<div class="sub">The Book of the Riven Stone</div>
<div class="meta"><span class="ver"></span></div>
</header>'''

radios = '\n'.join('<input class="rd" type="radio" name="read" id="read-%s"%s aria-label="%s">'
                   % (k, ' checked' if k == 'book' else '', name) for k, name in TABS)

bars = '''<div class="bars">
<nav aria-label="The Book">
<a href="#contents">Contents</a>
<a href="#foreword">Of This Book</a>
<a href="#invocation">Invocation</a>
<a href="#book-1">I · The Wall</a>
<a href="#book-2">II · The Builders</a>
<a href="#book-3">III · The Havens</a>
<a href="#book-4">IV · The Wound</a>
<a href="#book-5">V · The Tides</a>
<a href="#book-6">VI · The Homecomings</a>
<a href="#epilogue">Epilogue</a>
<a href="#knowings">Knowings</a>
</nav>
<div class="readbar" role="group" aria-label="Read the whole Book in">%s</div>
</div>''' % '<span class="dot" aria-hidden="true"> · </span>'.join(
    '<label class="l-%s" for="read-%s">%s</label>' % (k, k, name) for k, name in TABS)

SCRIPT = r'''(function(){
var K='%s',d=document,w=window,snap=null;
try{var v=w.localStorage.getItem(K);if(v==='read-book'||v==='read-plain'||v==='read-orig'){var r0=d.getElementById(v);if(r0)r0.checked=true}}catch(e){}
try{if(d.fonts&&d.fonts.load)d.fonts.load('1em "Garl Flenn"').catch(function(){})}catch(e){}
function rl(){var b=d.querySelector('.bars');return (b?Math.max(0,b.getBoundingClientRect().bottom):0)+14}
function shown(e){return !!(e&&e.getClientRects().length)}
function pane(sw){for(var c=sw.firstElementChild;c;c=c.nextElementSibling){if(c.classList.contains('pane')&&shown(c))return c}return null}
function anchors(p){var a=p.querySelectorAll('[data-k],[data-m]'),o=[];for(var i=0;i<a.length;i++){var r=a[i].getBoundingClientRect();if(!r.width&&!r.height)continue;var k=[],x=a[i].getAttribute('data-k'),y=a[i].getAttribute('data-m');if(x)k.push(x);if(y)k.push(y);o.push({t:r.top,k:k})}return o}
function take(lab){
 var y=rl(),el=lab||null;
 if(!el){var x=Math.round(d.documentElement.clientWidth/2);for(var dy=0;dy<96&&!el;dy+=12){var h=d.elementFromPoint(x,y+dy);if(h&&h!==d.body&&h!==d.documentElement&&!h.closest('.bars'))el=h}}
 if(!el)return null;
 var p=el.closest('.pane');
 if(!p)return{fix:el,top:el.getBoundingClientRect().top,at:Date.now()};
 var r=p.getBoundingClientRect();
 return{sw:p.parentNode,y:y,src:anchors(p),t0:r.top,t1:r.bottom,at:Date.now()};
}
function put(s){
 if(!s||Date.now()-s.at>4000)return;
 if(s.fix){var dt=s.fix.getBoundingClientRect().top-s.top;if(dt)w.scrollBy(0,dt);return}
 var p=pane(s.sw);if(!p)return;
 var tl=anchors(p),at={},i,j;
 for(i=0;i<tl.length;i++)for(j=0;j<tl[i].k.length;j++)if(!(tl[i].k[j] in at))at[tl[i].k[j]]=tl[i].t;
 var r=p.getBoundingClientRect(),Sp=s.t0,Tp=r.top,Sn=s.t1,Tn=r.bottom;
 for(i=0;i<s.src.length;i++){var a=s.src[i],t=null;for(j=0;j<a.k.length;j++)if(a.k[j] in at){t=at[a.k[j]];break}
  if(t===null)continue;if(a.t<=s.y+2){Sp=a.t;Tp=t}else{Sn=a.t;Tn=t;break}}
 var ty=(Sn>Sp&&Tn>=Tp)?Tp+(s.y-Sp)*(Tn-Tp)/(Sn-Sp):Tp+(s.y-Sp);
 if(Math.abs(ty-s.y)>1)w.scrollBy(0,ty-s.y);
}
d.addEventListener('click',function(e){var t=e.target,l=t&&t.closest?t.closest('label[for^="read-"]'):null;if(!l)return;var r=d.getElementById(l.htmlFor);if(!r||r.checked){snap=null;return}snap=take(l.closest('.readbar')?null:l)},true);
d.addEventListener('keydown',function(e){var t=e.target;if(t&&t.name==='read')snap=take(null)},true);
d.addEventListener('change',function(e){var t=e.target;if(!t||t.name!=='read')return;try{w.localStorage.setItem(K,t.id)}catch(x){}var s=snap;snap=null;put(s);if(!s)return;var again=function(){put(s)};
 try{w.requestAnimationFrame(function(){w.requestAnimationFrame(again)});w.setTimeout(again,150);if(d.fonts&&d.fonts.status==='loading')d.fonts.ready.then(again)}catch(x){}});
})();''' % STORE_KEY

footer_repo = ('<footer>The Legends of Rivenkeep · The Book of the Riven Stone · <span class="ver"></span> · '
               'how the Book was made, and how it enters the game: <a href="%s">The Legends: Notes</a></footer>' % NOTES_HREF)
footer_web = ('<footer>The Legends of Rivenkeep · The Book of the Riven Stone · <span class="ver"></span> · '
              'how the Book was made, and how it enters the game: <cite>The Legends: Notes</cite> (Rivenkeep_Legends_Notes.html)</footer>')

defs = FILL.defs()
inner = '''%s
<script>
%s
</script>
%s
%s
%s
<main class="ctn">

%s

</main>
@@FOOTER@@
''' % (radios, SCRIPT, defs, header, bars, body_html)

doc = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rivenkeep — The Legends</title>
<meta name="description" content="The Book of the Riven Stone: the tales laid at the Long Hearth of Rivenkeep, as Seren Two-Inks set them down, in the Book's own English, in plain words, and in the original hands, stone and wood.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="%s" rel="stylesheet">
<style>
%s%s
%s</style>
</head>
<body>
%s</body>
</html>
''' % (FONTS.replace('&', '&amp;'), style, extra, panes_css, inner.replace('@@FOOTER@@', footer_repo))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(doc)

# ------------------------------------------------------------------ the private web copy (the host's page contract)
sys.path.insert(0, HERE)
import web_copy  # noqa: E402
web = web_copy.make(style + extra + '\n' + panes_css, inner.replace('@@FOOTER@@', footer_web), FONTS, VERSION)
os.makedirs(os.path.dirname(OUT_WEB), exist_ok=True)
open(OUT_WEB, 'w', encoding='utf-8').write(web)

mb = lambda s: len(s.encode('utf-8')) / 1048576.0
print('wrote %s  %.2f MB (%d bytes)' % (OUT, mb(doc), len(doc.encode('utf-8'))))
print('wrote %s  %.2f MB (%d bytes)' % (OUT_WEB, mb(web), len(web.encode('utf-8'))))
print('%d switchable leaves; Book/Plain drawings inlined %d times; owed (caption only): %s' % (
    len(all_ids), len(INL.drawn), sorted(set(INL.owed))))
print('Original: %d blocks set, %d drawings filled (%d distinct), %d shared symbols; svg <style> dropped: %d' % (
    STATS['orig_blocks'], len(FILL.keys), len(set(FILL.keys)), len(FILL.pool.syms), n_svg_styles))
print('drawings re-prefixed for unique ids: %d; drawings closed that their file left open: %s' % (n_reprefixed, sorted(set(REPAIRED))))
print('landmarks Plain Words shares: %d; dropped where the counts differ: %s' % (STATS['shared_m'], STATS['dropped_m']))
print('Plain Words v3.1: datelines %d; second headnote paragraphs %d; notes for new readers %d' % (
    STATS['plain_datelines'], STATS['plain_headnote_2nd'], STATS['plain_notes']))
