# -*- coding: utf-8 -*-
"""Checks for Rivenkeep_Tongues.html v0.3.0 (scratch only): well-formed, unique ids, every anchor resolves,
no scripts, no external refs but the house fonts, no leftover placeholders, the doc version."""
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

W7 = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf7'
W8 = W7[:-1] + '8'
F = W8 + '/out/Rivenkeep_Tongues.html'
DOCS = '/Users/riquochet/code/Rivenkeep/Docs/'
s = open(F, encoding='utf-8').read()
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
# elements whose end tag HTML lets you omit are not used here; SVG children are all explicitly closed or self-closed
bad = 0


class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.stack, s.err, s.ids = [], [], []

    def handle_starttag(s, tag, attrs):
        d = dict(attrs)
        if 'id' in d:
            s.ids.append(d['id'])
        if tag in VOID:
            return
        s.stack.append((tag, s.getpos()))

    def handle_startendtag(s, tag, attrs):
        d = dict(attrs)
        if 'id' in d:
            s.ids.append(d['id'])

    def handle_endtag(s, tag):
        if tag in VOID:
            return
        if not s.stack:
            s.err.append(('extra close', tag, s.getpos()))
            return
        t, pos = s.stack.pop()
        if t != tag:
            s.err.append(('mismatch open', t, pos, 'close', tag, s.getpos()))


p = P()
p.feed(s)
p.close()
print('unclosed:', p.stack[:5])
print('errors:', p.err[:10])
bad += len(p.stack) + len(p.err)
c = Counter(p.ids)
d = [k for k, v in c.items() if v > 1]
print('ids', len(c), 'dups', d[:10])
bad += len(d)
ids = set(c)
unres = sorted(set(h for h in re.findall(r'href="#([^"]+)"', s) if h not in ids))
print('unresolved internal hrefs:', unres[:20])
bad += len(unres)
badu = [h for h in re.findall(r'url\(#([^)]+)\)', s) if h not in ids]
print('unresolved url():', len(badu), badu[:5])
bad += len(badu)
lab = [h for m in re.findall(r'aria-labelledby="([^"]+)"', s) for h in m.split() if h not in ids]
print('unresolved aria-labelledby:', len(lab), lab[:5])
bad += len(lab)
lf = [h for h in re.findall(r'<label for="([^"]+)"', s) if h not in ids]
print('unresolved label for:', lf)
bad += len(lf)
for doc, anc in sorted(set(re.findall(r'href="(Rivenkeep_[A-Za-z_]+\.html)(?:#([^"]*))?"', s))):
    path = W8 + '/out/' + doc
    where = 'wf8/out (to be deployed with this doc)'
    if not os.path.exists(path):
        path = DOCS + doc
        where = 'Docs'
    if not os.path.exists(path):
        print('MISSING cross doc', doc)
        bad += 1
        continue
    t = open(path, encoding='utf-8').read()
    if anc and ('id="%s"' % anc) not in t:
        print('BAD cross anchor', doc, anc)
        bad += 1
    elif doc == 'Rivenkeep_Legends_Original.html':
        print('cross link ok via', where, doc, anc)
print('cross-doc links:', sorted(set(re.findall(r'href="(Rivenkeep_[^"]+)"', s))))
nscript = len(re.findall(r'<script', s, re.I))
non = len(re.findall(r'\son[a-z]+=', s))
print('script tags:', nscript, 'on* attrs:', non)
bad += nscript + non
ext = sorted(set(re.findall(r'(?:src|href)="(https?://[^"]+)"', s)))
print('external refs:', ext)
bad += len([e for e in ext if not e.startswith('https://fonts.googleapis.com/')])
print('placeholders left:', re.findall(r'\{\{[^}]*\}\}', s)[:5])
bad += len(re.findall(r'\{\{[^}]*\}\}', s))
ver = re.findall(r'--doc-version:"([^"]+)"', s)
print('doc version:', ver)
bad += (ver != ['v0.3.0'])
print('history rows v0.3.0, v0.2.0:', '<td><strong>v0.3.0</strong></td><td>2026-09-28' in s, '<td><strong>v0.2.0</strong></td>' in s)
bad += '<td><strong>v0.3.0</strong></td><td>2026-09-28' not in s
# the one allowed path: where the full lexicon lives (named on purpose), and its relative link
s_scan = s.replace('Docs/Research/Rivenkeep_Orrowen_Lexicon.tsv', '').replace('Research/Rivenkeep_Orrowen_Lexicon.tsv', '')
# stray section signs in text outside links (from the specs' own numbering)
txt = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
txt = re.sub(r'<style>.*?</style>', '', txt, flags=re.S)
txt = re.sub(r'<a [^>]*>[^<]*</a>', '', txt)
plain = re.sub(r'<[^>]+>', ' ', txt)
st = Counter(re.findall(r'(?:[A-Za-z]+ )?§[\d]+[\w.]*', plain))
print('unlinked §:', st.most_common(40))
# scratch paths must not leak into the doc
leak = re.findall(r'(?:wf[678]/?|scratchpad|\.py\b|\.tsv\b|/private/tmp)', re.sub(r'base64,[A-Za-z0-9+/=]+', '', s_scan))
print('scratch leaks:', Counter(leak).most_common(10))
bad += len(leak)
print('size KB:', len(s.encode()) // 1024)
print('RESULT', 'OK' if not bad else 'PROBLEMS: %d' % bad)
sys.exit(1 if bad else 0)
