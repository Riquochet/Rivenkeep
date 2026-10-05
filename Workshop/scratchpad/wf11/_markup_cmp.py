#!/usr/bin/env python3
"""Compare book_v3.md and plain_v3.md section by section: skeleton, comment markers, ::: blocks, inline tokens."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _assemble_plain_v3 import cut, STRUCT  # noqa

WF = os.path.dirname(os.path.abspath(__file__))
book = open(os.path.join(WF, 'book_v3.md'), encoding='utf-8').read()
plain = open(os.path.join(WF, 'plain_v3.md'), encoding='utf-8').read()

bs, ps = cut(book), cut(plain)
bk = [k for k, _ in bs]
pk = [k for k, _ in ps]
print('skeleton identical:', bk == pk, len(bk), len(pk))
if bk != pk:
    for i, (a, b) in enumerate(zip(bk, pk)):
        if a != b:
            print('  first diff at', i, repr(a), repr(b))
            break

COMMENT = re.compile(r'<!--.*?-->')
BLOCK = re.compile(r'^(?:> ?)*:::.*$')
CHIP = re.compile(r'\[⟦[^⟧]*⟧\]|⟦[^⟧]*⟧')
PAIR = re.compile(r'\{\{[^}]*\}\}')
TOKEN = re.compile(r'\{[A-Z_]+\}')


def marks(body):
    out = []
    for ln in body:
        s = ln.strip()
        if BLOCK.match(s):
            out.append(re.sub(r'^(?:> ?)+', '> ', s))
        for c in COMMENT.findall(ln):
            out.append(c)
        for c in CHIP.findall(ln):
            out.append(c)
    return out


def bag(rx, body):
    return collections.Counter(x for ln in body for x in rx.findall(ln))


bad = 0
for (k, bb), (_, pb) in zip(bs, ps):
    if k == '---':
        continue
    mb, mp = marks(bb), marks(pb)
    if mb != mp:
        bad += 1
        print('\n##', k)
        import difflib
        for d in difflib.unified_diff(mb, mp, 'book', 'plain', lineterm='', n=0):
            print('   ', d)
    pb_, pp_ = set(bag(PAIR, bb)), set(bag(PAIR, pb))
    if pb_ != pp_:
        print('\n##', k, 'pair-names book-only:', pb_ - pp_, 'plain-only:', pp_ - pb_)
    tb, tp = bag(TOKEN, bb), bag(TOKEN, pb)
    if tb != tp:
        print('\n##', k, 'tokens', dict(tb), dict(tp))
print('\nsections with markup differences:', bad)
