#!/usr/bin/env python3
"""wf12 merge: the Book's recurring English (a run of N or more words shared by paragraphs of different leaves, or of
one leaf far apart), with each paragraph's Orrowen from its unit, for the harmonisation pass.  recur.py [N]"""
import json, re, sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import coverage as C, pairs as P
N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
cov = json.load(open(os.path.join(HERE, 'coverage2.json')))
items = {u: {it['line']: it for it in its} for u, its in P.all_items().items()}
paras = [r for r in cov['paras'] if r['hit'] and r['hit'][2] in ('bq',) and r['kind'] not in ('head',)]
def toks(s):
    s = re.sub(r'\{\{([^}]*)\}\}', r'\1', s)
    return re.findall(r"[a-z0-9']+", s.lower().replace('’', "'"))
SKIP = {'and the hearth said we remember', 'this i lay as it was laid for me', 'this we lay as it was laid for us', 'and no one answered'}
grams = collections.defaultdict(set)
for i, r in enumerate(paras):
    t = toks(r['text'])
    for k in range(len(t) - N + 1):
        grams[tuple(t[k:k + N])].add(i)
clusters = collections.defaultdict(set)
for g, ids in grams.items():
    if len(ids) < 2:
        continue
    ids = sorted(ids)
    leaves = set(paras[i]['leaf'] for i in ids)
    if len(leaves) < 2 and max(paras[i]['line'] for i in ids) - min(paras[i]['line'] for i in ids) < 40:
        continue
    if ' '.join(g) in ' '.join(SKIP):
        continue
    clusters[tuple(ids)].add(g)
out = []
for ids, gs in sorted(clusters.items(), key=lambda x: paras[x[0][0]]['line']):
    # the longest shared run, as text
    best = max(gs, key=len)
    out.append(dict(phrase=' '.join(best), paras=[dict(line=paras[i]['line'], leaf=paras[i]['leaf'], unit=paras[i]['hit'][0],
                     uline=paras[i]['hit'][1], en=paras[i]['text'], orr=items[paras[i]['hit'][0]][paras[i]['hit'][1]]['orr']) for i in ids]))
json.dump(out, open(os.path.join(HERE, 'recur_%d.json' % N), 'w'), indent=1, ensure_ascii=False)
print(len(out), 'clusters')
for c in out:
    print('=== %s' % c['phrase'])
    for p in c['paras']:
        print('   [%s L%d · %s] %s' % (p['unit'], p['uline'], (p['leaf'] or '')[:6], p['orr'].replace('\n', ' / ')[:420]))
        print('        EN: %s' % p['en'][:200].replace('\n', ' / '))
