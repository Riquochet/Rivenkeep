#!/usr/bin/env python3
"""Compare the markup of plain_v31_draft.md with wf11/plain_v3.md, marker for marker, and its headings with book_v3.md.

Checked, whole file and section by section:
  1. the skeleton: the sequence of '#', '##', '###' headings and top-level '---' rules (against the Book and plain_v3);
  2. HTML comments <!-- ... --> in order;
  3. ':::' fence lines in order (blockquote prefix normalised), and the native-block keys in order;
  4. {{...}} pair-names: the sequence, the per-name counts, and the set (the set is the standard wf11 used);
  5. ▒▒▒▒ redaction runs: count and run length;
  6. ⟦...⟧ chips and {TOKEN}s, which wf11's _markup_cmp.py also compared.
Also: native-block bodies byte for byte, and leftovers that must not be in the draft.
Prints a report; exits 1 if any check other than the pair-name sequence/counts fails.
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _assemble_plain_v31 import cut  # noqa

WF13 = os.path.dirname(os.path.abspath(__file__))
WF11 = os.path.join(os.path.dirname(WF13), 'wf11')
book = open(os.path.join(WF11, 'book_v3.md'), encoding='utf-8').read()
old = open(os.path.join(WF11, 'plain_v3.md'), encoding='utf-8').read()
new = open(os.path.join(WF13, 'plain_v31_draft.md'), encoding='utf-8').read()

COMMENT = re.compile(r'<!--.*?-->', re.S)
FENCE = re.compile(r'^(?:> ?)*:::.*$')
NATIVE = re.compile(r'^(?:> ?)*:::\s*native\s+(\S+)')
PAIR = re.compile(r'\{\{([^}]*)\}\}')
REDACT = re.compile(r'▒+')
CHIP = re.compile(r'\[⟦[^⟧]*⟧\]|⟦[^⟧]*⟧')
TOKEN = re.compile(r'(?<!\{)\{[A-Z_]+\}(?!\})')


def extract(lines):
    text = '\n'.join(lines)
    fences = [re.sub(r'^(?:> ?)+', '> ', ln.strip()) for ln in lines if FENCE.match(ln.strip())]
    return {
        'comments': COMMENT.findall(text),
        'fences': fences,
        'native keys': [m.group(1) for ln in lines for m in [NATIVE.match(ln.strip())] if m],
        'pair-name sequence': PAIR.findall(text),
        'redaction runs': REDACT.findall(text),
        'chips': CHIP.findall(text),
        'tokens': TOKEN.findall(text),
    }


def native_bodies(text):
    out, cur = [], None
    for ln in text.split('\n'):
        s = re.sub(r'^(?:> ?)+', '', ln.strip()).strip()
        if cur is None and NATIVE.match(ln.strip()):
            cur = [ln.strip()]
        elif cur is not None:
            cur.append(ln.rstrip())
            if s == ':::':
                out.append(cur)
                cur = None
    return out


fail = 0
bs, os_, ns = cut(book), cut(old), cut(new)
bk, ok_, nk = [k for k, _ in bs], [k for k, _ in os_], [k for k, _ in ns]
print('== 1. Skeleton (headings and rules)')
print(f'   Book {len(bk)} · plain_v3 {len(ok_)} · v3.1 draft {len(nk)}')
print('   identical to the Book:', nk == bk, '· identical to plain_v3:', nk == ok_)
if nk != bk:
    fail += 1
    for d in difflib.unified_diff(bk, nk, 'book', 'v31', lineterm='', n=0):
        print('     ', d)
b3 = [k for k in bk if k and k.startswith('### ')]
n3 = [k for k in nk if k and k.startswith('### ')]
print(f"   '###' headings: Book {len(b3)} · draft {len(n3)} · identical, byte for byte: {b3 == n3}")
if b3 != n3:
    fail += 1

print('\n== 2-6. Markup, whole file (plain_v3 -> v3.1 draft)')
eo, en = extract(old.split('\n')), extract(new.split('\n'))
for name in eo:
    same = eo[name] == en[name]
    extra = ''
    if name == 'pair-name sequence':
        extra = f'   counts {dict(collections.Counter(eo[name]))} -> {dict(collections.Counter(en[name]))}'
    elif name == 'redaction runs':
        extra = f'   lengths {sorted(set(map(len, eo[name])))} -> {sorted(set(map(len, en[name])))}'
    print(f'   {name:20} {len(eo[name]):3} -> {len(en[name]):3}  identical sequence: {same}{extra}')

print('\n== Section by section')
oS, nS = dict(os_), dict(ns)
rows = []
for k in [k for k in nk if k and k != '---']:
    a, b = extract(oS.get(k, [])), extract(nS.get(k, []))
    bad = []
    for name in ['comments', 'fences', 'native keys', 'redaction runs', 'chips', 'tokens']:
        if a[name] != b[name]:
            bad.append(name)
    pa, pb = a['pair-name sequence'], b['pair-name sequence']
    pair_set = set(pa) == set(pb)
    pair_seq = pa == pb
    if not pair_set:
        bad.append('pair-name set')
    rows.append((k, a, b, bad, pair_set, pair_seq))
    if bad:
        fail += 1

hdr = f"   {'section':45} {'cmt':>7} {'fence':>7} {'native':>7} {'▒▒▒▒':>7} {'{{}}':>7}  set seq  result"
print(hdr)
for k, a, b, bad, pset, pseq in rows:
    def c(n):
        return f"{len(a[n])}/{len(b[n])}"
    res = 'OK' if not bad else 'DIFF: ' + ', '.join(bad)
    print(f"   {k[:45]:45} {c('comments'):>7} {c('fences'):>7} {c('native keys'):>7} {c('redaction runs'):>7}"
          f" {c('pair-name sequence'):>7}  {'=' if pset else 'X':>3} {'=' if pseq else '~':>3}  {res}")
for k, a, b, bad, pset, pseq in rows:
    if bad:
        print('\n   ##', k)
        for name in ['comments', 'fences', 'native keys', 'redaction runs', 'chips', 'tokens', 'pair-name sequence']:
            if a[name] != b[name] and (name != 'pair-name sequence' or not pset):
                for d in difflib.unified_diff(a[name], b[name], 'plain_v3', 'v31', lineterm='', n=0):
                    print('     ', name, d)

print('\n== Native blocks, bodies byte for byte')
ob, nb = native_bodies(old), native_bodies(new)
print(f'   plain_v3 {len(ob)} · draft {len(nb)} · all identical: {ob == nb}')
for x, y in zip(ob, nb):
    if x != y:
        print('   differs:', x[0])

print('\n== Leftovers')
for label, rx in [("'## WRITER'S NOTES'", r"^## WRITER'S NOTES"), ('PLAIN WORDS header', r'<!-- PLAIN WORDS'),
                  ("'#### ' heading", r'^#### ')]:
    n = len(re.findall(rx, new, re.M))
    print(f'   {label}: {n}')
    if n:
        fail += 1

print('\nsections with markup differences (pair-name set counted, sequence not):', sum(1 for r in rows if r[3]))
print('sections whose pair-name sequence differs from plain_v3:', sum(1 for r in rows if not r[5]))
sys.exit(1 if fail else 0)
