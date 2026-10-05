#!/usr/bin/env python3
"""wf12 merge fix F1: a unit's English that differs from its Book paragraph only by emphasis marks (W04, W06, W08 set
the wood's story in italics) is replaced by the Book's paragraph, character for character.  Logged to fixes.log."""
import json, re, collections, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import coverage as C
res = json.load(open(os.path.join(HERE, 'coverage2.json')))
miss = [r for r in res['paras'] if r['hit'] is None and r['kind'] not in ('native-cap', 'native-body', 'table')]
ue = C.unit_english()
strip = lambda s: re.sub(r'[*_]', '', C.norm(s))
by = collections.defaultdict(list)
for x in ue:
    by[(x['unit'], strip(x['eng']))].append(x)
edits = collections.defaultdict(list)
for r in miss:
    c = by.get((r['owner'], strip(r['text'])), [])
    if len(c) == 1:
        edits[r['owner']].append((c[0]['eng'], r['text'], r['line']))
log = open(os.path.join(HERE, 'fixes.log'), 'a')
for u, es in edits.items():
    p = os.path.join(C.W12, 'units', u + '.md')
    t = open(p, encoding='utf-8').read()
    n = 0
    for old, new, bl in es:
        k = t.count('\n' + old + '\n')
        assert k == 1, (u, old[:60], k)
        t = t.replace('\n' + old + '\n', '\n' + new + '\n')
        n += 1
        log.write('F1 %s: English set to the Book (line %d), emphasis only: %s\n' % (u, bl, new[:70]))
    open(p, 'w', encoding='utf-8').write(t)
    print(u, n, 'paragraphs set to the Book')
