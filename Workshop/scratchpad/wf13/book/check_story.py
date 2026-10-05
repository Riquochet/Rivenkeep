#!/usr/bin/env python3
"""check_story.py - check the story page (Rivenkeep_Legends.html v3.1.0, wf13) against its three sources, and its
private web copy against the host's page contract.

    python3 check_story.py [OUT_DIR]       (default $RK_OUT or wf13/out: Rivenkeep_Legends.html, web/The_Legends_of_Rivenkeep.html)

  1. word for word, leaf by leaf: every word of each leaf of book_v3.md is in that leaf's The Book pane, in order,
     and every word of plain_v31.md's leaf in its Plain Words pane (builder's markers excepted; the VI.3 token read
     as its text); the title page's line, the Contents, the Book headings and Arguments, from each text
  2. the Original: every leaf's p-orig pane holds every block of panes.json for its anchor, in order (data-k = the
     Book's line), each block's ink text as panes.json gives it, every drawing slot filled; every Book paragraph's
     data-k is one of the Original's (the shared anchors); the inks of Halyna's paragraphs agree between the Book
     pane and the Original, line by line
  3. HTML: tags balanced (non-void), ids unique, every in-page href resolves, every label's 'for' is a radio
  4. ONE SWITCH: three radios name="read" at the very top of the body (read-book checked, read-plain, read-orig),
     fixed and visually hidden; the sticky bar 'The Book · Plain Words · Original' of labels for them under the nav;
     in every leaf the same three labels for the same ids; every switch unit has the three panes; no other radios;
     the CSS sibling selectors that switch every pane and mark the active label
  5. the script: one, inline, small; only keeps the reader's place and the choice; every localStorage access
     inside try/catch; no alert/confirm/prompt/print; no on* handler, no javascript: URL
  6. outside links: Google Fonts only; relative links: the Notes alone; nothing left of the sources' notation
  7. the tale ids of the v2 page all present; the v3 forms: datelines, headnotes, READING blocks (the lines in
     order, the two voices by turns), the seal
  8. the lintel: one span.pair per {{Name}} in each pane; the wood markers applied alike in both texts
  9. no design matter
 10. the web copy: <title>, the Google Fonts <link>, one <style>, and no doctype/html/head/body; every colour a
     token on :root, color-scheme: dark, the body's background a token, no literal colour outside :root; the
     leaf-hand font inline base64; outside loads only Google Fonts; the sticky bar at env(safe-area-inset-top, 0px);
     no link to another file; under 15.5 MB; its body the repo page's but for the colophon's link
 11. (v3.1.0) the interlinear: every line of every romanisation fold in the Original is set word over word, each word
     (its punctuation with it) in an <i> over its English in a <small> hidden from screen readers, the glosses those
     wf13/gloss gives the line, in its order, and once more as one visually hidden list after the line; no letter of a
     line outside a word box; every fold's summary still 'Romanisation ...'; every line wf13/gloss_in asks for is
     there; the CSS that stacks them (inline-flex word boxes, the gloss in the mono face, dimmer, from a token);
     (wf13 reader check) the warden's blotted name in a word's box of its own, upright, glossed '(name blotted out)',
     and said so in the hidden list; every other mark between the words in a span.m that keeps a word's space after it;
     the lines' font-size-adjust none (a wood leaf's .405 had shrunk the mono glosses to about 8px)
 12. (v3.1.0) Plain Words v3.1 complete: the Plain pane is wf13/plain_v31.md (word for word, 1.); every leaf where the
     Book has a dateline has its own Plain 'when' line, set as a dateline (the source's first italic paragraph), the
     headnote after it; the foreword's Plain pane opens with 'A note for new readers', set apart (aside, its label,
     all its paragraphs) before the foreword's dateline; the Book and Plain share the dateline landmark in every leaf
Exit status 1 on any failure.
"""
import difflib
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
S = os.path.dirname(W12)
OUTD = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('RK_OUT', os.path.join(W12, 'out'))
PAGE = os.path.join(OUTD, 'Rivenkeep_Legends.html')
WEB = os.path.join(OUTD, 'web', 'The_Legends_of_Rivenkeep.html')
OLD = '/Users/riquochet/code/Rivenkeep/Docs/Rivenkeep_Legends.html'
SRC = {'book': os.path.join(S, 'wf11', 'book_v3.md'), 'plain': os.path.join(S, 'wf13', 'plain_v31.md')}
PANES = json.load(open(os.path.join(W12, 'orig', 'panes.json'), encoding='utf-8'))
TOKEN = 'Neivaere, in the cellars of Glasspire'
h = open(PAGE, encoding='utf-8').read()
fail = []


def bad(msg):
    fail.append(msg)
    print('   FAIL', msg)


def words(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'…]*", t)


def md_words(md):
    md = re.sub(r'<!--.*?-->', ' ', md, flags=re.S)
    md = re.sub(r'^(> ?)?::: .*$', ' ', md, flags=re.M)
    md = re.sub(r'^(> ?)?:::\s*$', ' ', md, flags=re.M)
    md = re.sub(r'\{\{([A-Za-z]+)\}\}', r'\1', md)
    md = md.replace('{LAST_THRONE_AT_HAVEN}', TOKEN)
    md = re.sub(r'⟦[a-z0-9_]+⟧', ' ', md)
    return words(md)


def html_words(s):
    s = re.sub(r'<svg\b.*?</svg>', ' ', s, flags=re.S)
    s = re.sub(r'<span class="sep"> · </span>', ' ', s)
    s = re.sub(r'<summary>Translation</summary>', ' ', s)          # the fold's own label, not Book text
    s = re.sub(r'</?(?:span|em|strong|a|cite)\b[^>]*>', '', s)     # inline tags join; block tags part
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return words(s)


def same(a, b, where):
    if a == b:
        return True
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            bad('%s: words differ (%s) src %r page %r' % (where, op, ' '.join(a[max(0, i1 - 3):i2 + 3]), ' '.join(b[max(0, j1 - 3):j2 + 3])))
            return False


def element(s, start):
    """the outer HTML of the element whose open tag starts at s[start], by tag counting"""
    tag = re.match(r'<([a-zA-Z][\w-]*)', s[start:]).group(1)
    depth, i = 0, start
    pat = re.compile(r'<(/?)%s\b[^>]*?(/?)>' % tag)
    for m in pat.finditer(s, start):
        if m.group(2):
            continue
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return s[start:m.end()]
    raise SystemExit('unclosed <%s> at %d' % (tag, start))


def panes_of(unit_html):
    """the three panes that are direct children of a switch unit: {key: inner html}"""
    out = {}
    for k in ('book', 'plain', 'orig'):
        m = re.search(r'<div class="pane p-%s"[^>]*>' % k, unit_html)
        if not m:
            continue
        el = element(unit_html, m.start())
        out[k] = el[el.index('>') + 1:-len('</div>')]
    return out

# ---------------------------------------------------------------- the sources, split by leaf
def split_md(path):
    md = open(path, encoding='utf-8').read()
    units = {}
    parts = re.split(r'^(#{2,3} .*|\*\*The Last Note · .*\*\*)$', md, flags=re.M)
    head = None
    for p in parts:
        if re.match(r'^(#{2,3} |\*\*The Last Note)', p or ''):
            head = p
            continue
        if head is None:
            units['__front'] = p
            continue
        units[head] = p
    return units


IDS = {'## OF THIS BOOK': 'foreword', '## THE INVOCATION': 'invocation', '### The Stone out of the Grey': 't-epilogue',
       '### The Book of Knowings': 't-knowings', '**The Last Note · Three Stones over the Hearth**': 't-last-note'}


def unit_id(head):
    if head in IDS:
        return IDS[head]
    m = re.match(r'^### ((?:VI|IV|V|III|II|I)\.\d+) · ', head)
    return 't-' + m.group(1).replace('.', '-') if m else None


src = {k: split_md(v) for k, v in SRC.items()}

# ---------------------------------------------------------------- the page, by switch unit
UNITS = {}
for m in re.finditer(r'<(article|div) class="[^"]*\bsw\b[^"]*"[^>]*>', h):
    el = element(h, m.start())
    idm = re.search(r'\bid="([^"]+)"', m.group(0))
    if idm:
        uid = idm.group(1)
    else:
        # the foreword's and the Invocation's leaf, the title page, the Contents, a Book's Argument: by the section
        sec = re.findall(r'<section id="([^"]+)"', h[:m.start()])[-1]
        uid = sec if 'leaf' in m.group(0) else sec + ':frame'
    UNITS[uid] = {'html': el, 'tag': m.group(0), 'panes': panes_of(el)}
LEAVES = {k: v for k, v in UNITS.items() if not k.endswith(':frame')}
print('0. %d switch units: %d leaves, %d frame units' % (len(UNITS), len(LEAVES), len(UNITS) - len(LEAVES)))

print('1. words, leaf by leaf')
n_ok = 0
n_all = 0
for k in ('book', 'plain'):
    for head, text in src[k].items():
        uid = unit_id(head)
        if not uid:
            continue
        n_all += 1
        if uid not in LEAVES:
            bad('%s: no leaf %s on the page' % (k, uid))
            continue
        if same(md_words(text), html_words(LEAVES[uid]['panes'][k]), '%s %s' % (k, uid)):
            n_ok += 1
print('   leaves word for word: %d of %d' % (n_ok, n_all))
# the frame, each text's own
for k in ('book', 'plain'):
    s = src[k]
    tp = UNITS['front:frame']['panes'][k]
    if not same(md_words('*The Book of the Riven Stone*' + s['## *The Book of the Riven Stone*']), html_words(tp), k + ' title page'):
        pass
    if not same(md_words(s['## CONTENTS']), html_words(UNITS['contents:frame']['panes'][k]), k + ' contents'):
        pass
    for head, text in s.items():
        if head.startswith('## BOOK') or head in ('## EPILOGUE', '## APPENDIX'):
            title = head[3:]
            sid = {'## EPILOGUE': 'epilogue', '## APPENDIX': 'knowings'}.get(head) or 'book-' + str(
                ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX'].index(title.split()[1]) + 1)
            arg = text.split('\n###')[0]
            mh = re.search(r'<section id="%s" class="book">\n<div class="read">\n(<h2.*?</h2>)' % sid, h)
            if not mh or html_words(mh.group(1)) != words(title):
                bad('Book head differs: ' + sid)
            same(md_words(arg), html_words(UNITS[sid + ':frame']['panes'][k]), '%s %s Argument' % (k, sid))
print('   title page, Contents, Book heads and Arguments: each text its own, checked')

# ---------------------------------------------------------------- 2. the Original
print('2. the Original')
n_blocks = n_lines_ok = 0
for anchor, blocks in PANES.items():
    if anchor == 'front':
        uid = 'front:frame'
    elif anchor == 'contents':
        uid = 'contents:frame'
    elif anchor.startswith('book-') or anchor in ('epilogue', 'knowings'):
        uid = anchor + ':frame'
    else:
        uid = anchor
    if uid not in UNITS or 'orig' not in UNITS[uid]['panes']:
        bad('no Original pane for ' + anchor)
        continue
    og = UNITS[uid]['panes']['orig']
    keys = re.findall(r'<[a-z]+\b[^>]*\bdata-k="b(\d+)"', og)
    want = [str(b['line']) for b in blocks]
    n_blocks += len(blocks)
    if keys != want:
        bad('%s: Original blocks by line %s... want %s...' % (anchor, keys[:6], want[:6]))
    else:
        n_lines_ok += 1
    # each block's ink: its words as panes.json gives them (drawings aside)
    if html_words(re.sub(r'<span class="svg-slot"[^>]*></span>', ' ', ''.join(b['html'] for b in blocks))) != html_words(og):
        a = html_words(re.sub(r'<span class="svg-slot"[^>]*></span>', ' ', ''.join(b['html'] for b in blocks)))
        same(a, html_words(og), anchor + ' Original text')
    if 'svg-slot' in og:
        bad(anchor + ': a drawing slot left unfilled')
    # the shared anchors: the Book's lines are the Original's
    if uid in LEAVES:
        bk = set(re.findall(r'\bdata-k="(b\d+)"', LEAVES[uid]['panes']['book']))
        ok = set('b' + w for w in want)
        if bk - ok:
            bad('%s: Book lines with no Original block: %s' % (anchor, sorted(bk - ok)[:6]))
        # Halyna's two inks: the Book pane and the Original agree, line by line
        bv = {}
        for tg in re.findall(r'<p\b[^>]*>', LEAVES[uid]['panes']['book']):
            kk, vv = re.search(r'data-k="b(\d+)"', tg), re.search(r'data-voice="([ab])"', tg)
            if kk and vv:
                bv[kk.group(1)] = vv.group(1)
        ov = {str(b['line']): b['voice'] for b in blocks if b.get('voice') in ('a', 'b')}
        diff = sorted(l for l in set(bv) | set(ov) if bv.get(l) != ov.get(l))
        if diff:
            bad('%s: the two inks differ at Book lines %s (book %s, original %s)' % (
                anchor, diff[:5], [bv.get(l) for l in diff[:5]], [ov.get(l) for l in diff[:5]]))
print('   %d anchors; %d blocks; every block in its place by the Book line: %d of %d; no slot unfilled: %s' % (
    len(PANES), n_blocks, n_lines_ok, len(PANES), 'svg-slot' not in h[h.index('<body>'):]))
nv_b = len(re.findall(r'data-voice="[ab]"', ''.join(u['panes'].get('book', '') for u in LEAVES.values())))
nv_o = sum(1 for bl in PANES.values() for b in bl if b.get('voice') in ('a', 'b'))
print('   Halyna\'s two inks: %d paragraphs in The Book, %d in the Original, line for line' % (nv_b, nv_o))

# ---------------------------------------------------------------- 3. HTML
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}


class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.stack, s.errs, s.ids, s.hrefs, s.labels, s.radios, s.handlers, s.ext, s.tags = [], [], [], [], [], {}, [], [], []
        s.scripts = []
        s.in_script = False

    def handle_starttag(s, tag, a):
        a = dict(a)
        s.tags.append((tag, a))
        if tag not in VOID:
            s.stack.append(tag)
        if 'id' in a:
            s.ids.append(a['id'])
        if 'href' in a and tag not in ('use',):
            s.hrefs.append((tag, a['href']))
        if tag == 'label':
            s.labels.append(a.get('for'))
        if tag == 'input':
            s.radios[a.get('id')] = a
        if tag == 'script':
            s.scripts.append(a)
            s.in_script = True
        if tag in ('iframe', 'object', 'embed'):
            s.handlers.append(('tag', tag))
        for k, v in a.items():
            if k.startswith('on') or (v and 'javascript:' in v.lower()):
                s.handlers.append((tag, k))
        if tag in ('link', 'img', 'script', 'source') and (a.get('href') or a.get('src') or '').startswith('http'):
            s.ext.append(a.get('href') or a.get('src'))

    def handle_startendtag(s, tag, a):
        s.handle_starttag(tag, a)
        if tag not in VOID and s.stack and s.stack[-1] == tag:
            s.stack.pop()

    def handle_endtag(s, tag):
        if tag == 'script':
            s.in_script = False
        if tag in VOID:
            return
        if not s.stack or s.stack[-1] != tag:
            s.errs.append('</%s> at %s, open %s' % (tag, s.getpos(), s.stack[-3:]))
            if tag in s.stack:
                while s.stack and s.stack[-1] != tag:
                    s.stack.pop()
                s.stack.pop()
            return
        s.stack.pop()


p = P()
p.feed(h)
print('3. HTML: %d tags; unbalanced %d; still open %s' % (len(p.tags), len(p.errs), p.stack))
for e in p.errs[:5]:
    print('     ', e)
if p.errs or p.stack:
    bad('tags not balanced')
dups = sorted({i for i in p.ids if p.ids.count(i) > 1})
if dups:
    bad('duplicate ids: %s' % dups[:8])
ids = set(p.ids)
dead = [x for _, x in p.hrefs if x.startswith('#') and x[1:] not in ids]
if dead:
    bad('dead in-page links: %s' % dead[:8])
nolab = [f for f in p.labels if f not in p.radios or p.radios[f].get('type') != 'radio']
if nolab:
    bad('labels without their radio: %s' % nolab[:5])
print('   ids %d unique: %s; in-page links %d, dead %d; labels %d, all for a radio: %s' % (
    len(p.ids), not dups, sum(1 for _, x in p.hrefs if x.startswith('#')), len(dead), len(p.labels), not nolab))
m = re.search(r'<p\b[^>]*>(?:(?!</p>).)*?<(?:div|p|figure|blockquote|h[1-6]|ul|table|details)\b', h, re.S)
if m:
    bad('a block element inside a <p>: ' + m.group(0)[-200:])

# ---------------------------------------------------------------- 4. ONE SWITCH
print('4. one switch for the whole Book')
body = h[h.index('<body>') + 6:]
top = re.match(r'\s*(<input class="rd" type="radio" name="read" id="read-book" checked[^>]*>)\s*'
               r'(<input class="rd" type="radio" name="read" id="read-plain"[^>]*>)\s*'
               r'(<input class="rd" type="radio" name="read" id="read-orig"[^>]*>)', body)
if not top:
    bad('the three radios are not the first thing in the body')
radios = [a for t, a in p.tags if t == 'input']
if len(radios) != 3 or any(a.get('name') != 'read' or a.get('type') != 'radio' for a in radios):
    bad('other inputs on the page: %s' % [(a.get('name'), a.get('id')) for a in radios])
bar = re.search(r'<div class="bars">\s*<nav\b.*?</nav>\s*<div class="readbar"[^>]*>(.*?)</div>\s*</div>', h, re.S)
if not bar:
    bad('no sticky bar under the nav')
else:
    labs = re.findall(r'<label class="l-(\w+)" for="read-(\w+)">([^<]+)</label>', bar.group(1))
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', bar.group(1))).strip()
    if [(a, b, c) for a, b, c in labs] != [('book', 'book', 'The Book'), ('plain', 'plain', 'Plain Words'), ('orig', 'orig', 'Original')] \
            or txt != 'The Book · Plain Words · Original':
        bad('the sticky bar reads %r' % txt)
    print('   the sticky bar: %r, labels for read-book, read-plain, read-orig' % txt)
n_tabs = 0
for uid, u in UNITS.items():
    if set(u['panes']) != {'book', 'plain', 'orig'}:
        bad('%s: panes %s' % (uid, sorted(u['panes'])))
    order = re.findall(r'<div class="pane p-(book|plain|orig)"', u['html'])
    if uid in LEAVES:
        tb = re.search(r'<div class="tabs"[^>]*>(.*?)</div>', u['html'], re.S)
        labs = re.findall(r'<label class="tab l-(\w+)" for="read-(\w+)">([^<]+)</label>', tb.group(1)) if tb else []
        if labs != [('book', 'book', 'The Book'), ('plain', 'plain', 'Plain Words'), ('orig', 'orig', 'Original')]:
            bad('%s: the leaf bar %s' % (uid, labs))
        else:
            n_tabs += 1
        if not u['panes'].get('book', '').strip() or not u['panes'].get('plain', '').strip() or not u['panes'].get('orig', '').strip():
            bad('%s: an empty pane' % uid)
print('   %d leaves each with the same three labels; %d switch units each with The Book, Plain Words and Original' % (n_tabs, len(UNITS)))
css = h[h.index('<style>'):h.index('</style>')]
for need in (r'\.rd\{position:fixed;', r'#read-plain:checked~\.ctn \.p-plain', r'#read-orig:checked~\.ctn \.p-orig',
             r'#read-book:checked~\.ctn \.p-book', r'\.pane\{display:none\}', r'#read-orig:checked~\* \.tabs \.l-orig',
             r'#read-orig:checked~\.bars \.l-orig', r'\.bars\{position:sticky;top:env\(safe-area-inset-top, 0px\)'):
    if not re.search(need, css):
        bad('switch CSS missing: ' + need)
print('   the CSS: radios fixed and hidden; :checked ~ .ctn .p-* switches every pane; the active label marked in every bar')

# ---------------------------------------------------------------- 5. the script
print('5. the script')
scripts = re.findall(r'<script\b([^>]*)>(.*?)</script>', h, re.S)
if len(scripts) != 1 or scripts[0][0].strip():
    bad('scripts: %d (%r)' % (len(scripts), [a for a, _ in scripts]))
js = scripts[0][1] if scripts else ''
uses = [m.start() for m in re.finditer(r'localStorage', js)]
for u in uses:
    before = js[:u]
    if before.rfind('try{') < before.rfind('}catch') or before.rfind('try{') == -1:
        bad('a localStorage access outside try/catch at %d' % u)
for f in ('alert(', 'confirm(', 'prompt(', 'print(', 'eval(', 'Function(', 'innerHTML', 'fetch(', 'XMLHttpRequest'):
    if f in js:
        bad('script uses ' + f)
if p.handlers:
    bad('handlers or embeds: %s' % p.handlers)
print('   one inline script, %d bytes; localStorage %d times, each inside try/catch; no alert/confirm/prompt/print; '
      'no handlers' % (len(js), len(uses)))

# ---------------------------------------------------------------- 6. links, leftovers
outside = [x for _, x in p.hrefs if re.match(r'^[a-z]+:', x)] + p.ext
outside_bad = [x for x in outside if not x.startswith(('https://fonts.googleapis.com', 'https://fonts.gstatic.com'))]
rel = [x for _, x in p.hrefs if not x.startswith('#') and not re.match(r'^[a-z]+:', x)]
print('6. outside links %s; relative links %s' % (sorted(set(outside)), rel))
if outside_bad:
    bad('outside links: %s' % outside_bad)
if rel != ['Rivenkeep_Legends_Notes.html']:
    bad('relative links should be the Notes alone: %s' % rel)
reader = body
for u in UNITS.values():
    if 'orig' in u['panes']:
        reader = reader.replace(u['panes']['orig'], ' ')       # the Original's folds are the grain's notation
body_nosvg = re.sub(r'<svg\b.*?</svg>', '', reader, flags=re.S)
body_nosvg = re.sub(r'<script\b.*?</script>', '', body_nosvg, flags=re.S)
text_only = re.sub(r'<[^>]+>', ' ', body_nosvg)
for pat in (r'\{\{', r'\{[A-Z_]+\}', r':::', r'\*', r'⟦'):
    if re.search(pat, text_only):
        bad('builder notation left on the page: %s' % pat)
if '<!--' in body:
    bad('a comment left in the body')

# ---------------------------------------------------------------- 7. tale ids, v3 forms
old = open(OLD, encoding='utf-8').read()
old_tales = re.findall(r'<article class="tale[^"]*" id="(t-[^"]+)"', old)
new_tales = re.findall(r'<article class="tale[^"]*" id="(t-[^"]+)"', h)
missing = [i for i in old_tales if i not in new_tales]
print('7. tale ids: the v2 page had %d, all present: %s; %d on the page' % (len(old_tales), not missing, len(new_tales)))
if missing:
    bad('tale ids missing: %s' % missing)
for sid in ('front', 'contents', 'foreword', 'invocation', 'book-1', 'book-2', 'book-3', 'book-4', 'book-5', 'book-6', 'epilogue', 'knowings'):
    if sid not in ids:
        bad('section id missing: ' + sid)
dl_src = {str(b['line']): b['book'] for bl in PANES.values() for b in bl if b['kind'] == 'dateline'}
dl_page = dict(re.findall(r'<p class="dateline" data-k="b(\d+)"[^>]*>(.*?)</p>', h))
if set(dl_src) != set(dl_page):
    bad('datelines: page %d, Original %d; differ at %s' % (len(dl_page), len(dl_src), sorted(set(dl_src) ^ set(dl_page))[:5]))
n_hn = {k: sum(len(re.findall(r'<p class="teller"', u['panes'][k])) for u in LEAVES.values()) for k in ('book', 'plain')}
print('   datelines %d (the Original\'s %d, line for line); headnotes: The Book %d, Plain Words %d' % (
    len(dl_page), len(dl_src), n_hn['book'], n_hn['plain']))
n_read = 0
for k in ('book', 'plain'):
    for head, text in src[k].items():
        uid = unit_id(head)
        if not uid or '<!-- READING -->' not in text:
            continue
        lines = re.search(r'<!-- READING -->\s*\n((?:\*— .*\n?)+)', text).group(1).strip().split('\n')
        pane = LEAVES[uid]['panes'][k]
        rd = re.search(r'<div class="reading"[^>]*>(.*?)</div>', pane, re.S)
        if not rd:
            bad('%s %s: no reading' % (k, uid))
            continue
        frs = re.findall(r'<p class="rd-line"[^>]*data-voice="([ab])"[^>]*>(.*?)</p>', rd.group(1))
        if [v for v, _ in frs] != ['ab'[i % 2] for i in range(len(lines))] or \
                [html_words(x) for _, x in frs] != [md_words(l) for l in lines]:
            bad('%s %s: reading lines or voices differ' % (k, uid))
        if 'lead' in rd.group(0) or re.search(r'<(h\d|strong)', rd.group(1)):
            bad('%s %s: a label on the reading' % (k, uid))
        if '<p class="seal"' not in pane:
            bad('%s %s: no seal' % (k, uid))
        n_read += 1
print('   READING blocks: %d (the 8 wood leaves in both texts), each line its own, the voices by turns, no label; the seal set' % n_read)
if n_read != 16:
    bad('READING blocks %d, want 16' % n_read)

# ---------------------------------------------------------------- 8. lintel, wood
n_pairs_src = {k: sum(len(re.findall(r'\{\{[A-Za-z]+\}\}', re.sub(r'<!--.*?-->', '', t, flags=re.S)))
                      for hd, t in src[k].items() if unit_id(hd)) for k in src}
n_pairs_page = {k: sum(len(re.findall(r'<span class="pair">', x['panes'][k])) for x in LEAVES.values()) for k in ('book', 'plain')}
print('8. lintels: source book %d plain %d; page book %d plain %d' % (
    n_pairs_src['book'], n_pairs_src['plain'], n_pairs_page['book'], n_pairs_page['plain']))
if n_pairs_src != n_pairs_page:
    bad('lintel count')
for k in ('book', 'plain'):
    toc_src = len(re.findall(r'\{\{', src[k]['## CONTENTS']))
    toc_page = len(re.findall(r'<span class="pair">', UNITS['contents:frame']['panes'][k]))
    if toc_src != toc_page:
        bad('%s contents lintels %d/%d' % (k, toc_src, toc_page))
wood_b = sum(len(re.findall(r'class="[^"]*\bwood\b', x['panes']['book'])) for x in LEAVES.values())
wood_p = sum(len(re.findall(r'class="[^"]*\bwood\b', x['panes']['plain'])) for x in LEAVES.values())
print('   wood-role passages inside stone leaves: book %d, plain %d' % (wood_b, wood_p))
if wood_b != wood_p:
    bad('wood passages differ between the texts')
ab = re.findall(r'<article class="tale leaf sw (stone|wood)[^"]*" id="([^"]+)"', h)
print('   leaves: %d stone, %d wood' % (sum(1 for r, _ in ab if r == 'stone'), sum(1 for r, _ in ab if r == 'wood')))
if sum(1 for r, _ in ab if r == 'wood') != 8:
    bad('wood leaves')

# ---------------------------------------------------------------- 9. no design matter
txt = re.sub(r'<[^>]+>', ' ', body_nosvg)
for pat in ('unlocked by', 'Version History', 'integrator', "editor's note", 'HOW THE LEGENDS ENTER', 'About this version',
            'delivery map', 'GDD', 'achievement'):
    if pat.lower() in txt.lower():
        bad('design matter on the page: %r' % pat)
print('9. design matter: none' if not [f for f in fail if f.startswith('design')] else '9. design matter found')
# the Original too (fidelity pass, 2026-10-03): its folds are the grain's notation, but not the builder's, the tools'
# or the scratch's; and the warden's blots stand in Seren's ink wherever the Book has them
og_all = ''.join(u['panes'].get('orig', '') for u in UNITS.values())
og_nosvg = re.sub(r'<svg\b.*?</svg>', '', og_all, flags=re.S)
og_txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<pre\b.*?</pre>', ' ', og_nosvg, flags=re.S))
for pat in (r'\{\{', r'\{[A-Z_]+\}', r':::', r'⟦', r'<!--', r'svg3/', r'\.svg\b', r'\.gn2\b', r'\.md\b', r'\.py\b', r'\bwf\d+',
            r'scratchpad', r'/private/', r'validator', r'_spec\b', r'grain_v2', r'§'):
    hit = re.search(pat, og_txt)
    if hit:
        bad('Original: builder, tool or scratch matter on the page: %r near %r' % (pat, og_txt[max(0, hit.start() - 60):hit.end() + 40]))
n_blot_book = sum(u['panes'].get('book', '').count('▒▒▒▒') for u in LEAVES.values())
og_ink = re.sub(r'<details\b.*?</details>', ' ', og_nosvg, flags=re.S)
n_blot_ink = len(re.findall(r'<span class="ink-blot"[^>]*>▒▒▒▒</span>', og_ink))
n_blot_rom = len(re.findall(r'▒▒▒▒', re.sub(r'<span class="ink-blot"[^>]*>▒▒▒▒</span>', '', og_nosvg)))
if not (n_blot_book == n_blot_ink == n_blot_rom):
    bad('the warden\'s blots: The Book %d, the Original\'s ink %d, its romanisation %d' % (n_blot_book, n_blot_ink, n_blot_rom))
print('   the Original: no builder, tool or scratch matter; the warden\'s blots: The Book %d, the ink %d, the romanisation %d'
      % (n_blot_book, n_blot_ink, n_blot_rom))

# ---------------------------------------------------------------- 10. the web copy
print('10. the web copy')
if not os.path.exists(WEB):
    bad('no web copy')
else:
    w = open(WEB, encoding='utf-8').read()
    size = len(w.encode('utf-8'))
    head = re.match(r'<title>The Legends of Rivenkeep</title>\n<link href="(https://fonts\.googleapis\.com/[^"]+)" rel="stylesheet">\n<style>\n(.*?)</style>\n', w, re.S)
    if not head:
        bad('the web copy does not open with <title>, the Google Fonts <link>, one <style>')
    if re.search(r'<(?:!doctype|html|head|body)[\s>]|</(?:html|head|body)>', w, re.I):
        bad('the web copy has a doctype, html, head or body tag')
    n_style = len(re.findall(r'<style\b', w))
    if n_style != 1:
        bad('the web copy has %d <style> elements' % n_style)
    wcss = head.group(2) if head else ''
    # colours: tokens on :root only
    c2 = re.sub(r'url\([^)]*\)|/\*.*?\*/|"[^"]*"|\'[^\']*\'', '', wcss, flags=re.S)
    roots = re.findall(r'(?:^|\})\s*:root\{([^}]*)\}', c2)
    if len(roots) != 1:
        bad('the web copy has %d :root rules' % len(roots))
    rest = re.sub(r'(?:^|(?<=\}))\s*:root\{[^}]*\}', '', c2)
    LITS = re.compile(r'(?<![\w-])#[0-9a-fA-F]{3,8}(?![\w-])|(?<![\w-])(?:rgba?|hsla?)\(|(?<![\w-])(?:transparent|white|black|red|gold|silver|gray|grey)(?![\w(-])')
    lits = [mm.group(0) for mm in LITS.finditer(re.sub(r'^[^{]*\{|\}[^{}]*\{', '{', rest))]
    if lits:
        bad('literal colours outside :root: %s' % sorted(set(lits))[:8])
    if roots and 'color-scheme:dark' not in roots[0].replace(' ', ''):
        bad('no color-scheme: dark on :root')
    if 'prefers-color-scheme' in wcss or '@media print' in wcss:
        bad('a second theme or print rules in the web copy')
    if not re.search(r'(?:^|\})\s*body\{background:var\(--bg\)', rest) and 'html,body{background:var(--bg)' not in rest:
        bad('the body background is not a token')
    if not re.search(r"@font-face\{font-family:'Garl Flenn';src:url\(data:font/woff2;base64,", wcss):
        bad('the leaf-hand font is not inline')
    if not re.search(r'\.bars\{position:sticky;top:env\(safe-area-inset-top, 0px\)', wcss):
        bad('the sticky bar is not at env(safe-area-inset-top, 0px)')
    urls = re.findall(r'(?:href|src)="(https?:[^"]+)"', w) + re.findall(r'url\((https?:[^)]+)\)', wcss) + re.findall(r'@import[^;]+', wcss)
    if [u for u in urls if not u.startswith(('https://fonts.googleapis.com', 'https://fonts.gstatic.com'))]:
        bad('outside loads in the web copy: %s' % urls)
    hrefs = re.findall(r'<a\b[^>]*\bhref="([^"]*)"', w)
    if [x for x in hrefs if not x.startswith('#')]:
        bad('links to other files in the web copy: %s' % [x for x in hrefs if not x.startswith('#')])
    if 'Rivenkeep_Legends_Notes.html' not in re.sub(r'<[^>]+>', ' ', w[w.rfind('<footer'):]):
        bad('the colophon does not name the Notes')
    wjs = re.findall(r'<script>(.*?)</script>', w, re.S)
    if wjs != [js]:
        bad('the web copy\'s script differs')
    for f in ('alert(', 'confirm(', 'prompt(', 'print('):
        if f in w.replace('<script>' + js + '</script>', ''):
            pass
    # the body is the repo page's, but for the colophon
    rb = h[h.index('<body>') + 6:h.index('</body>')].strip()
    wb = w[w.index('</style>\n') + 9:].strip()
    rb2 = re.sub(r'<footer>.*?</footer>', '', rb, flags=re.S)
    wb2 = re.sub(r'<footer>.*?</footer>', '', wb, flags=re.S)
    if rb2 != wb2:
        bad('the web copy\'s body is not the page\'s')
    if size >= 15.5 * 1024 * 1024:
        bad('the web copy is %.2f MB' % (size / 1048576.0))
    print('   opens <title> · Google Fonts <link> · one <style>; no doctype/html/head/body; %d :root rule with '
          'color-scheme dark; literal colours outside :root: %d; font inline; sticky at the safe area; links to files: %d; '
          '%.2f MB (%d bytes)' % (len(roots), len(lits), len([x for x in hrefs if not x.startswith('#')]), size / 1048576.0, size))
print('   the page: %.2f MB (%d bytes)' % (len(h.encode('utf-8')) / 1048576.0, len(h.encode('utf-8'))))

# ---------------------------------------------------------------- 11. the interlinear (v3.1.0)
print('11. the romanisation, word over word')
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(W12, 'orig'))
import build_panes as BPX  # noqa: E402  (its gloss table and its word rule; nothing is built on import)
IL_NEED = set()
for f in sorted(os.listdir(os.path.join(W12, 'gloss_in'))):
    if f.endswith('.json'):
        IL_NEED.update(r['rom'] for r in json.load(open(os.path.join(W12, 'gloss_in', f), encoding='utf-8')))
il = {'folds': 0, 'lines': 0, 'words': 0, 'wordless': 0, 'blots': 0, 'marks': 0}
il_seen, il_bad = set(), []
og_pages = ''.join(u['panes'].get('orig', '') for u in UNITS.values())
for m in re.finditer(r'<details class="tr rom"><summary>(.*?)</summary><div class="tr-body">(.*?)</div></details>', og_pages, re.S):
    il['folds'] += 1
    if not m.group(1).startswith('Romanisation'):
        il_bad.append('a romanisation fold labelled %r' % m.group(1)[:40])
    for para in re.findall(r'<p\b[^>]*>.*?</p>', m.group(2), re.S):
        mm = re.fullmatch(r'<p class="il">(.*)</p>', para, re.S)
        if not mm:
            il_bad.append('a romanised line not word over word: %r' % para[:60])
            continue
        inner = mm.group(1)
        srm = re.search(r' <span class="sr">Word by word: (.*)\.</span>$', inner)
        line = re.sub(r' <span class="sr">.*</span>$', '', inner)
        line_nosvg = re.sub(r'<svg\b.*?</svg>', '', line, flags=re.S)
        ws = re.findall(r'<i>(.*?)<small aria-hidden="true">(.*?)</small></i>', line_nosvg, re.S)
        text = BPX.html_text(re.sub(r'<small aria-hidden="true">.*?</small>', '', line_nosvg)).strip()
        if BPX.WORD_CH.search(BPX.html_text(re.sub(r'<i\b[^>]*>.*?</i>', ' ', line_nosvg, flags=re.S))):
            il_bad.append('letters outside the word boxes: %r' % text[:60])
        # the warden's blotted name: a word's box, upright, glossed '(name blotted out)', never a letter of a name
        blots = re.findall(r'<i class="blot">(.*?)<small aria-hidden="true">(.*?)</small></i>', line_nosvg, re.S)
        for bw, bg in blots:
            il['blots'] += 1
            if BPX.BLOT_CH not in bw or BPX.WORD_CH.search(BPX.html_text(bw)) or BPX.html_text(bg) != BPX.BLOT_GLOSS:
                il_bad.append('a blotted name boxed wrongly: %r' % (bw + ' / ' + bg)[:60])
        if BPX.BLOT_CH in BPX.html_text(re.sub(r'<i class="blot">.*?</i>', ' ', line_nosvg, flags=re.S)):
            il_bad.append('a blotted name outside its box: %r' % text[:60])
        # every other mark between the words in its span.m (a word's space after it)
        for mk in re.findall(r'<span class="m">(.*?)</span>(?= |$)', line_nosvg, re.S):
            il['marks'] += 1
        bare = re.sub(r'<i\b[^>]*>.*?</i>|<span class="m">.*?</span>(?= |$)|<span class="tok"[^>]*>|</span>', ' ', line_nosvg, flags=re.S)
        if BPX.html_text(bare).strip() and ws:
            il_bad.append('a mark between the words left bare: %r' % BPX.html_text(bare).strip()[:40])
        if not ws:
            il['wordless'] += 1
            continue
        g = BPX.GLOSS.get(text)
        if g is None:
            il_bad.append('no gloss for %r' % text[:60])
            continue
        if [BPX.word_core(BPX.html_text(w)) for w, _ in ws] != [w for w, _ in g]:
            il_bad.append('the words differ from the gloss: %r' % text[:60])
        if [BPX.html_text(e) for _, e in ws] != [e for _, e in g]:
            il_bad.append('the glosses differ: %r' % text[:60])
        said, gi = [], iter(e for _, e in g)
        for bm in re.finditer(r'<i( class="blot")?>', line_nosvg):
            said.append(BPX.BLOT_SAID if bm.group(1) else next(gi, '?'))
        if not srm or BPX.html_text(srm.group(1)) != ', '.join(said):
            il_bad.append('the hidden word-by-word list differs: %r' % text[:60])
        il['lines'] += 1
        il['words'] += len(ws)
        il_seen.add(text)
il_miss = IL_NEED - il_seen
for x in il_bad[:8]:
    bad('interlinear: ' + x)
if len(il_bad) > 8:
    bad('interlinear: %d more problems' % (len(il_bad) - 8))
if il_miss:
    bad('interlinear: %d romanised lines of wf13/gloss_in not on the page, glossed: %s' % (len(il_miss), [x[:40] for x in sorted(il_miss)[:4]]))
if 'tr rom' in re.sub(r'<details class="tr rom">', '', og_pages):
    bad('a romanisation fold of another form')
for need in (r'\.il i\{display:inline-flex;flex-direction:column', r'\.il i small\{font-family:\'IBM Plex Mono\',monospace;font-style:normal;[^}]*color:var\(--page-dim\)',
             r'\.il \.sr\{position:absolute;width:1px;height:1px;[^}]*clip-path:inset\(50%\)', r'details\.tr \.tr-body p\.il\{[^}]*font-style:italic',
             r'details\.tr \.tr-body p\.il\{[^}]*font-size-adjust:none', r'\.il \.m\{margin-right:\.36em\}', r'\.il i\.blot\{font-style:normal'):
    if not re.search(need, css):
        bad('interlinear CSS missing: ' + need)
print('   %d romanisation folds; %d lines set word over word (%d distinct, every one of gloss_in\'s %d: %s), %d words glossed, '
      '%d line(s) with no word (a gap); %d blotted names boxed and glossed %s; %d marks between the words spaced; problems %d'
      % (il['folds'], il['lines'], len(il_seen), len(IL_NEED), not il_miss, il['words'], il['wordless'], il['blots'],
         BPX.BLOT_GLOSS, il['marks'], len(il_bad)))

# ---------------------------------------------------------------- 12. Plain Words v3.1
print('12. Plain Words v3.1')
pmd = open(SRC['plain'], encoding='utf-8').read()
if '> **A note for new readers**' not in pmd:
    bad('the Plain source is not v3.1 (no note for new readers)')
n_pdl = 0
for uid, u in LEAVES.items():
    bk, pl = u['panes']['book'], u['panes']['plain']
    b_dl = re.search(r'<p class="dateline"[^>]*>', bk)
    p_dl = re.findall(r'<p class="dateline"([^>]*)>(.*?)</p>', pl, re.S)
    if bool(b_dl) != bool(p_dl) or len(p_dl) > 1:
        bad('%s: the Book has %s dateline, Plain Words %d' % (uid, 'a' if b_dl else 'no', len(p_dl)))
        continue
    if not p_dl:
        continue
    n_pdl += 1
    head = [hh for hh in src['plain'] if unit_id(hh) == uid]
    body = src['plain'][head[0]] if head else ''
    body = re.sub(r'^\s*> \*\*A note for new readers\*\*.*?\n(?!>)', '', body, flags=re.S) if uid == 'foreword' else body
    paras = [x.strip() for x in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', body, flags=re.S)) if x.strip()]
    first = paras[0] if paras else ''
    if not re.match(r'^\*(?!\*)[^*]+\*$', first) or html_words(p_dl[0][1]) != md_words(first):
        bad('%s: the Plain dateline is not the source\'s first italic paragraph' % uid)
    if 'data-m="dl1"' not in p_dl[0][0] or 'data-m="dl1"' not in b_dl.group(0):
        bad('%s: the dateline landmark is not shared' % uid)
    after = re.search(r'<p class="dateline"[^>]*>.*?</p>\s*(<[a-z0-9]+[^>]*>)', pl, re.S)
    if not after or not after.group(1).startswith('<p class="teller"'):
        bad('%s: no headnote after the Plain dateline' % uid)
n_bdl = sum(1 for u in LEAVES.values() if '<p class="dateline"' in u['panes']['book'])
fw = LEAVES['foreword']['panes']['plain']
nr = re.match(r'\s*<aside class="newreaders" aria-labelledby="newreaders-h">\s*<h3 class="nr-h" id="newreaders-h">A note for new readers</h3>(.*?)</aside>\s*<p class="dateline"', fw, re.S)
note_md = re.search(r'^> \*\*A note for new readers\*\*\n((?:>.*\n)+)', pmd, re.M)
if not nr:
    bad('the foreword\'s Plain pane does not open with the note for new readers, set apart, before its dateline')
elif not note_md or html_words(nr.group(1)) != md_words(re.sub(r'^> ?', '', note_md.group(1), flags=re.M)):
    bad('the note for new readers differs from the source')
n_nr = len(re.findall(r'<aside class="newreaders"', h))
if n_nr != 1 or re.search(r'<aside class="newreaders"', ''.join(u['panes']['book'] + u['panes']['orig'] for u in UNITS.values())):
    bad('notes for new readers on the page: %d (want one, in Plain Words)' % n_nr)
if not re.search(r'\.prose aside\.newreaders\{', css):
    bad('no CSS for the note for new readers')
n_hn2 = sum(len(re.findall(r'<p class="teller"', u['panes']['plain'])) for u in LEAVES.values())
print('   the source: %s; Plain datelines %d of the Book\'s %d, each the source\'s first italic paragraph, the dl1 landmark shared, '
      'the headnote after; headnote paragraphs %d; the note for new readers: %s, %d paragraphs' % (
          os.path.basename(SRC['plain']), n_pdl, n_bdl, n_hn2, bool(nr), len(re.findall(r'<p>', nr.group(1))) if nr else 0))
if n_pdl != n_bdl:
    bad('Plain datelines %d, the Book %d' % (n_pdl, n_bdl))

print('FAIL: %d' % len(fail) if fail else 'ALL CHECKS PASS')
sys.exit(1 if fail else 0)
