"""svgpool.py -- inline SVGs for the Original (wf8 scratch; never goes into Docs/).

Every drawing is set inline once per place it stands, with its ids made unique for the page (a new prefix per
inclusion), its copy of the renderer's shared <style> dropped (the page carries it once), and every <symbol> whose
body stands alone moved to one hidden <defs> at the top of the page, shared by every round that cuts the same
sign at the same size (the renderer draws each sign once as a <symbol> placed with <use>; this carries that one
step further, across rounds)."""
import hashlib
import os
import re

COMMON_STYLE = None
SHARED_CSS = ''


class Pool:
    def __init__(self):
        self.n = 0
        self.syms = {}           # hash -> (gid, xml)
        self.order = []
        self.raw_bytes = 0       # the SVGs as the renderer wrote them
        self.out_bytes = 0       # as set in the page
        self.count = 0
        self.styles_dropped = 0

    def take(self, src, title=None, desc=None):
        """src: a path, or SVG text. Returns the SVG ready to set inline."""
        global COMMON_STYLE, SHARED_CSS
        s = open(src, encoding='utf-8').read() if (len(src) < 400 and os.path.exists(src)) else src
        s = re.sub(r'^<\?xml[^>]*>\s*', '', s.strip())
        self.raw_bytes += len(s.encode('utf-8'))
        self.count += 1
        m = re.search(r'\bid="([A-Za-z][0-9A-Za-z]*)-', s)
        self.n += 1
        new = 'r%d' % self.n
        if m:
            pre = m.group(1)
            s = re.sub(r'(?<![0-9A-Za-z_-])%s-' % re.escape(pre), new + '-', s)
        # the renderer's style, once for the page
        st = re.search(r'<style>(.*?)</style>', s, re.S)
        if st:
            body = st.group(1)
            if COMMON_STYLE is None and body.startswith(':root.wood-ink{'):
                COMMON_STYLE = body
                SHARED_CSS = re.sub(r'^:root\.wood-ink\{[^}]*\}', '', body)
            if body == COMMON_STYLE:
                s = s.replace(st.group(0), '', 1)
                self.styles_dropped += 1
        # symbols shared across the page
        for sm in list(re.finditer(r'<symbol id="(%s-[^"]+)"([^>]*)>(.*?)</symbol>' % new, s, re.S)):
            sid, attrs, body = sm.group(1), sm.group(2), sm.group(3)
            if (new + '-') in body or 'url(#' in body:
                continue
            h = hashlib.sha1((attrs + '>' + body).encode('utf-8')).hexdigest()
            if h not in self.syms:
                gid = 'gs%d' % len(self.syms)
                self.syms[h] = (gid, '<symbol id="%s"%s>%s</symbol>' % (gid, attrs, body))
                self.order.append(h)
            gid = self.syms[h][0]
            s = s.replace(sm.group(0), '', 1)
            s = s.replace('href="#%s"' % sid, 'href="#%s"' % gid)
        s = s.replace('<defs></defs>', '')
        if title is not None:
            s = re.sub(r'(<title[^>]*>)[^<]*(</title>)', lambda q: q.group(1) + esc(title) + q.group(2), s, count=1)
        if desc is not None:
            s = re.sub(r'(<desc[^>]*>)[^<]*(</desc>)', lambda q: q.group(1) + esc(desc) + q.group(2), s, count=1)
        if 'focusable=' not in s[:300]:
            s = s.replace('<svg ', '<svg focusable="false" ', 1)
        self.out_bytes += len(s.encode('utf-8'))
        return s

    def defs(self):
        body = ''.join(self.syms[h][1] for h in self.order)
        self.out_bytes += len(body)
        return ('<svg class="gdefs" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" '
                'width="0" height="0"><defs>%s</defs></svg>' % body)


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def r_outer(svg):
    m = re.search(r'data-r-outer="(\d+)"', svg)
    return int(m.group(1)) if m else None
