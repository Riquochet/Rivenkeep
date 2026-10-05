"""panes_lib.py (wf12 scratch) -- for the page builder: fill the drawing slots of panes.json.

    import panes_lib as PL
    panes = PL.load()                         # {tale_anchor: [{para_index, line, end_line, kind, html, book, ...}]}
    F = PL.Filler()                           # one per page
    html = F.fill(block['html'])              # every slot replaced by its drawing, inline, ids unique on the page
    page_head_css = PL.css()                  # panes.css: the leaf-hand font (base64, once), the ink and grain rules
    body_start = F.defs()                     # the shared <symbol>s, once, right after <body> (after every fill)

A slot is  <span class="svg-slot" data-svg3="KEY" data-title="..."></span>  (wf12/orig/svg3/KEY.svg, the grain, by
make_grain3.py) or  <span class="svg-slot" data-native="ID" data-title="..."></span>  (wf6/svg/ID.svg, the Book's own
drawing, the same one the Book tab draws).  The grain goes through svgpool (the renderer's shared style dropped, since
panes.css carries it once; every sign drawn once as a shared <symbol>); a native drawing is inlined with its ids
prefixed, as build_story_html.py's Inliner does.  Filler(mode='img') sets the grain as <img loading="lazy"> instead
(each svg3 file carries its own style, so it draws alone; the native drawings stay inline, for they take the page's
classes).
"""
import html as H
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(os.path.dirname(HERE))
SVG3 = os.path.join(HERE, 'svg3')
NATIVE = os.path.join(S, 'wf6', 'svg')
sys.path.insert(0, HERE)
import svgpool  # noqa: E402

SLOT_RE = re.compile(r'<span class="svg-slot" data-(svg3|native)="([^"]+)"(?: data-title="([^"]*)")?></span>')


def load():
    return json.load(open(os.path.join(HERE, 'panes.json'), encoding='utf-8'))


def css():
    return open(os.path.join(HERE, 'panes.css'), encoding='utf-8').read()


class Filler:
    def __init__(self, mode='inline', img_base='svg3/'):
        self.pool = svgpool.Pool()
        self.mode = mode
        self.img_base = img_base
        self.n = 0
        self.keys = []

    def native(self, nid, title=None):
        s = open(os.path.join(NATIVE, nid + '.svg'), encoding='utf-8').read().strip()
        s = re.sub(r'^<\?xml[^>]*\?>\s*', '', s)
        self.n += 1
        u = 'nv%d' % self.n
        s = re.sub(r'<style>.*?</style>', '', s, flags=re.S)
        s = re.sub(r'\bid="([^"]+)"', lambda m: 'id="%s-%s"' % (u, m.group(1)), s)
        s = re.sub(r'\bhref="#([^"]+)"', lambda m: 'href="#%s-%s"' % (u, m.group(1)), s)
        s = re.sub(r'url\(#([^)]+)\)', lambda m: 'url(#%s-%s)' % (u, m.group(1)), s)
        s = re.sub(r'aria-labelledby="([^"]+)"',
                   lambda m: 'aria-labelledby="%s"' % ' '.join('%s-%s' % (u, x) for x in m.group(1).split()), s)
        if title:
            s = re.sub(r'(<title[^>]*>)[^<]*(</title>)', lambda q: q.group(1) + svgpool.esc(title) + q.group(2), s, count=1)
        return s

    def _one(self, m):
        kind, key, title = m.group(1), m.group(2), H.unescape(m.group(3)) if m.group(3) else None
        self.keys.append((kind, key))
        if kind == 'native':
            return self.native(key, title)
        if self.mode == 'img':
            return '<img src="%s%s.svg" alt="%s" loading="lazy" decoding="async">' % (self.img_base, key, H.escape(title or key))
        return self.pool.take(os.path.join(SVG3, key + '.svg'), title=title)

    def fill(self, html):
        return SLOT_RE.sub(self._one, html)

    def defs(self):
        return self.pool.defs()
