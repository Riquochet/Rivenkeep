import sys, re, json, os, collections, html as H; sys.path.insert(0,'.')
from pg import *
GD='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/gloss'
b=open(V31,encoding='utf-8').read()
# all gloss records, by file
recs={}; perfile=collections.Counter(); conflicts=[]
src=collections.defaultdict(list)
for f in sorted(os.listdir(GD)):
    if not f.endswith('.json'): continue
    for r in json.load(open(os.path.join(GD,f),encoding='utf-8')):
        perfile[f]+=1
        k=r['rom']; src[k].append(f)
        g=[tuple(x) for x in r['gloss']]
        if k in recs and recs[k]!=g: conflicts.append((k,f))
        recs.setdefault(k,g)
print('json records', sum(perfile.values()), 'distinct lines', len(recs), 'conflicting duplicates', len(conflicts))
for c in conflicts[:10]: print('  CONFLICT', c)
# the page's interlinear lines
def tx(h): return H.unescape(re.sub(r'<[^>]+>','',h))
lines=[]
for m in re.finditer(r'<p class="il">(.*?)</p>', b, re.S):
    inner=m.group(1)
    srm=re.search(r' <span class="sr">Word by word: (.*?)\.</span>$', inner, re.S)
    body=inner[:srm.start()] if srm else inner
    boxes=re.findall(r'<i>(.*?)<small aria-hidden="true">(.*?)</small></i>', body, re.S)
    key=tx(re.sub(r'<small aria-hidden="true">.*?</small>','',body)).strip()
    pairs=[(re.sub(r"^[^\w']+|[^\w']+$",'',tx(w)), H.unescape(g)) for w,g in boxes]
    sr=H.unescape(srm.group(1)) if srm else None
    lines.append((m.start(), key, pairs, sr, body))
print('page il lines', len(lines), 'with boxes', sum(1 for l in lines if l[2]))
bad=collections.Counter(); used=set(); ex=collections.defaultdict(list)
for pos,key,pairs,sr,body in lines:
    if not pairs:
        bad['line without boxes']+=1; ex['line without boxes'].append(key); continue
    g=recs.get(key)
    if g is None: bad['no json record for the line']+=1; ex['nojson'].append(key); continue
    used.add(key)
    if pairs!=list(g): bad['boxes != json']+=1; ex['boxes'].append((key,pairs,g))
    if sr != ', '.join(e for _,e in g): bad['sr list != json']+=1; ex['sr'].append((key,sr))
    # no letter outside a box
    outside=tx(re.sub(r'<i>.*?</i>','',body,flags=re.S))
    if re.search(r'[A-Za-zÀ-ž]', outside): bad['letters outside a box']+=1; ex['out'].append((key,outside))
print('problems:', dict(bad) or 'none')
for k,v in ex.items(): print(k, v[:5])
unused=[k for k in recs if k not in used]
print('json lines not on the page:', len(unused))
for k in unused[:40]: print('   ', src[k], repr(k[:100]))
print('page lines (distinct):', len(set(l[1] for l in lines)), ' total boxes:', sum(len(l[2]) for l in lines))
# where are il lines: all inside orig panes?
op=[(s,e) for k,s,e,_ in panes(b) if k=='orig']
outside_orig=[l for l in lines if not any(s<=l[0]<e for s,e in op)]
print('il lines outside orig panes:', len(outside_orig), [l[1][:40] for l in outside_orig[:5]])
print('--- the gap lines')
for pos,key,pairs,sr,body in lines:
    if key not in recs:
        k2=re.sub(r'\[[^\]]*\]','[]',key)
        g=recs.get(k2)
        print(repr(key), '->', repr(k2), 'json found:', g is not None, '; boxes == json:', g is not None and pairs==list(g), '; sr ok:', g is not None and sr==', '.join(e for _,e in g))
        print('    ', pairs)
        print('    body:', body[:600])
    if not pairs:
        print('no-box line body:', body[:600])
