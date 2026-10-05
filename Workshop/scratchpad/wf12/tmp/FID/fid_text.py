#!/usr/bin/env python3
"""fid_text.py (wf12 fidelity, scratch): an independent, character-level check of the story page's The Book and
Plain Words panes against wf11/book_v3.md and wf11/plain_v3.md, leaf by leaf, with punctuation, emphasis, the
lintel ({{Name}}), the blots (▒▒▒▒), every song line and every fixed line kept. Written apart from check_story.py
(which compares words only) so that a fault the builder and its own checker share is not missed.

    python3 fid_text.py [PAGE]     -> prints per-leaf results; writes fid_text.json beside itself
"""
import difflib
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
PAGE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(S, 'wf12', 'out', 'Rivenkeep_Legends.html')
SRC = {'book': os.path.join(S, 'wf11', 'book_v3.md'), 'plain': os.path.join(S, 'wf11', 'plain_v3.md')}
TOKEN = 'Neivaere, in the cellars of Glasspire'


# ------------------------------------------------------------------ sources
def leaf_key(head):
    m = re.match(r'^### ((?:VI|IV|V|III|II|I)\.\d+) · (.*)$', head)
    if m:
        return 't-' + m.group(1).replace('.', '-')
    return {'## OF THIS BOOK': 'foreword', '## THE INVOCATION': 'invocation',
            '### The Stone out of the Grey': 't-epilogue', '### The Book of Knowings': 't-knowings',
            '**The Last Note · Three Stones over the Hearth**': 't-last-note'}.get(head)


def split_src(path):
    """{leaf id: (first line, [lines])} in order; the leaf runs to the next heading of level 2 or 3 or the Last Note"""
    ls = open(path, encoding='utf-8').read().split('\n')
    out, order = {}, []
    cur = None
    for n, l in enumerate(ls, 1):
        if re.match(r'^#{2,3} ', l) or l.strip() == '**The Last Note · Three Stones over the Hearth**':
            k = leaf_key(l.strip())
            cur = k
            if k:
                assert k not in out, k
                out[k] = (n, [])
                order.append(k)
            continue
        if cur:
            out[cur][1].append(l)
    return out, order


def norm_src(lines):
    t = '\n'.join(lines)
    t = re.sub(r'<!--.*?-->', '\n', t, flags=re.S)
    o = []
    for l in t.split('\n'):
        l = re.sub(r'^>\s?', '', l)
        l = re.sub(r'^>\s?', '', l)
        s = l.strip()
        if s.startswith(':::') or s == '---' or re.match(r'^\|[\s:|-]+\|$', s):
            continue
        l = re.sub(r'^(- |\d+\. )', '', l)
        o.append(l)
    t = '\n'.join(o)
    t = t.replace('{LAST_THRONE_AT_HAVEN}', TOKEN)
    t = re.sub(r'⟦[a-z0-9_]+⟧', '', t)
    t = t.replace('|', ' ')
    return squash(t)


def squash(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace(' ', ' ')
    t = re.sub(r'\s+', ' ', t)
    return t.strip()


# ------------------------------------------------------------------ page
BLOCK = {'p', 'div', 'li', 'h1', 'h2', 'h3', 'h4', 'td', 'th', 'tr', 'figcaption', 'figure', 'blockquote', 'ul',
         'ol', 'table', 'details', 'section', 'article', 'br'}


class Md(HTMLParser):
    """the pane's text, as the markdown that made it: em -> *, strong -> **, span.pair -> {{X}}, span.who -> **X**,
    h4.part -> **X**; drawings and the fold's label dropped; block tags part the text"""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.o = []
        self.skip = 0
        self.stack = []

    def handle_starttag(self, tag, a):
        a = dict(a)
        cls = (a.get('class') or '').split()
        if self.skip:
            if tag == 'svg' or tag == 'summary':
                self.skip += 1
            return
        if tag == 'svg' or tag == 'summary':
            self.skip = 1
            return
        close = ''
        if tag == 'em':
            self.o.append('*'); close = '*'
        elif tag == 'strong':
            self.o.append('**'); close = '**'
        elif tag == 'span' and 'pair' in cls:
            self.o.append('{{'); close = '}}'
        elif tag == 'span' and 'who' in cls:
            self.o.append('**'); close = '**'
        elif tag == 'h4' and 'part' in cls:
            self.o.append('\n**'); close = '**\n'
        elif tag in BLOCK or (tag == 'span' and ('l' in cls or 'cap' in cls)):
            self.o.append('\n'); close = '\n'
        if tag not in ('br', 'img', 'input', 'meta', 'link', 'hr'):
            self.stack.append((tag, close))

    def handle_startendtag(self, tag, a):
        if not self.skip and tag == 'br':
            self.o.append('\n')

    def handle_endtag(self, tag):
        if self.skip:
            if tag in ('svg', 'summary'):
                self.skip -= 1
            return
        while self.stack:
            t, c = self.stack.pop()
            self.o.append(c)
            if t == tag:
                break

    def handle_data(self, d):
        if not self.skip:
            self.o.append(d)


def md_of(h):
    p = Md()
    p.feed(h)
    t = ''.join(p.o)
    t = re.sub(r'\*\*\*\*\*', '*****', t)
    return t


def element(s, start):
    tag = re.match(r'<([a-zA-Z][\w-]*)', s[start:]).group(1)
    depth = 0
    pat = re.compile(r'<(/?)%s\b[^>]*?(/?)>' % tag)
    for m in pat.finditer(s, start):
        if m.group(2):
            continue
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return s[start:m.end()]
    raise SystemExit('unclosed')


def pane(unit, k):
    m = re.search(r'<div class="pane p-%s"[^>]*>' % k, unit)
    if not m:
        return None
    el = element(unit, m.start())
    return el[el.index('>') + 1:-len('</div>')]


def page_leaves(h):
    out, order = {}, []
    for m in re.finditer(r'<article class="[^"]*\bsw\b[^"]*" id="([^"]+)"', h):
        out[m.group(1)] = element(h, m.start())
        order.append(m.group(1))
    for sid in ('foreword', 'invocation'):
        i = h.index('<section id="%s"' % sid)
        j = h.index('<div class="prose stone sw leaf"', i)
        out[sid] = element(h, j)
        order.insert(0 if sid == 'foreword' else 1, sid)
    return out, order


def diffs(a, b, ctx=40):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    o = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            o.append({'op': op, 'src': a[max(0, i1 - ctx):i2 + ctx], 'page': b[max(0, j1 - ctx):j2 + ctx],
                      'src_bit': a[i1:i2], 'page_bit': b[j1:j2]})
    return o


def main():
    h = open(PAGE, encoding='utf-8').read()
    leaves, porder = page_leaves(h)
    res = {'page_order': porder, 'leaves': {}}
    allok = True
    for k in ('book', 'plain'):
        src, sorder = split_src(SRC[k])
        res[k + '_order'] = sorder
        if sorder != porder:
            print('ORDER differs', k, sorder, porder)
            allok = False
        for lid in sorder:
            a = norm_src(src[lid][1])
            ph = pane(leaves[lid], k)
            b = squash(md_of(ph))
            # the page sets a part's ** on its own lines; the source runs them in the stream the same way
            d = diffs(a, b)
            res['leaves'].setdefault(lid, {})[k] = {'chars_src': len(a), 'chars_page': len(b), 'diffs': d[:20],
                                                    'n_diffs': len(d)}
            if d:
                allok = False
                print('%-12s %-5s %d diffs' % (lid, k, len(d)))
                for x in d[:6]:
                    print('     %s  src=%r  page=%r' % (x['op'], x['src_bit'][:80], x['page_bit'][:80]))
                    print('        ctx src : %r' % x['src'][:200])
                    print('        ctx page: %r' % x['page'][:200])
        # the orig pane must exist and be non-empty for every leaf
    for lid in porder:
        og = pane(leaves[lid], 'orig')
        n = len(re.findall(r'data-k="b\d+"', og or ''))
        res['leaves'].setdefault(lid, {})['orig_blocks'] = n
        if not og or not n:
            print('NO ORIGINAL', lid)
            allok = False
    json.dump(res, open(os.path.join(HERE, 'fid_text.json'), 'w'), indent=1, ensure_ascii=False)
    print('leaves on page:', len(porder), porder)
    print('ALL EXACT' if allok else 'DIFFERENCES FOUND')


if __name__ == '__main__':
    main()
