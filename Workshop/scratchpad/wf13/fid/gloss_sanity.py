import sys, re, json, os, collections, html as H; sys.path.insert(0,'.')
from pg import *
b=open(V31,encoding='utf-8').read()
# every rom fold line is il
n=0; nonil=[]
for m in re.finditer(r'<details class="tr rom"><summary>(.*?)</summary><div class="tr-body">(.*?)</div></details>', b, re.S):
    for p in re.finditer(r'<p\b([^>]*)>', m.group(2)):
        n+=1
        if p.group(1)!=' class="il"': nonil.append((m.group(1), m.group(2)[:100]))
print('rom fold <p>:', n, 'not il:', len(nonil), nonil[:3])
summ=collections.Counter(re.sub(r' ·.*','',s) for s in re.findall(r'<details class="tr rom"><summary>(.*?)</summary>', b))
print('rom fold summaries:', dict(summ))
# glosses: suspicious notation
G=collections.Counter(H.unescape(g) for g in re.findall(r'<small aria-hidden="true">(.*?)</small>', b))
sus=[g for g in G if re.search(r'[?{}+·_]|\b(PST|PL|SG|REL|GEN|NEG|1SG|2SG|3SG|1PL|2PL|3PL|S·|N·)\b|^\s*$', g)]
print('distinct glosses', len(G), 'total', sum(G.values()))
print('suspicious-looking glosses:', [(g,G[g]) for g in sus][:60])
print('parenthesised glosses:', sorted([(g,G[g]) for g in G if '(' in g], key=lambda x:-x[1])[:40])
