import sys, json, os, random, re, collections
sys.path.insert(0,'/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/orig')
import orr_analyze as OA
W13='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
lex=OA.Lexicon(OA.LEX)
leaf={}
for f in sorted(os.listdir(W13+'/gloss_in')):
    for r in json.load(open(W13+'/gloss_in/'+f)):
        leaf.setdefault(r['rom'],(r['leaf'],r['label'],r['english']))
seen=collections.Counter()
for f in sorted(os.listdir(W13+'/gloss')):
    for r in json.load(open(W13+'/gloss/'+f)): seen[r['rom']]+=1
rnd=random.Random(20261004)
picks=[]
for f in sorted(os.listdir(W13+'/gloss')):
    if f=='S03x.json': continue
    d=[r for r in json.load(open(W13+'/gloss/'+f)) if seen[r['rom']]==1 and 5<=len(r['gloss'])<=28]
    n=2 if f.startswith('S') else 1
    for r in rnd.sample(d, n): picks.append((f[:-5], r))
print(len(picks),'lines')
for u,r in picks:
    lf,lab,en=leaf.get(r['rom'],('?','?','?'))
    words=OA.analyse_text(r['rom'], lex)
    ws=[w for w in words if w.kind!='punct']
    print('='*100); print('%s · %s · %s' % (u, lf, lab)); print('ROM :', r['rom']); print('ENG :', en[:600])
    hints=OA.phrase_hints(words, lex)
    for form,mean in hints: print('  phrase = %s: %s' % (form, mean))
    if len(ws)!=len(r['gloss']):
        print('  !! token count differs: analyzer %d, page %d' % (len(ws), len(r['gloss'])))
    for i,(w,g) in enumerate(zip(ws, r['gloss'])):
        row=w.best.row if (w.best is not None and w.best.row is not None) else None
        mean=(row.get('meanings') or row.get('english') or '')[:70] if row else ''
        flag='' if w.status=='OK' else ' {%s}'%w.status
        print('  %-14s | page: %-22s | analyzer: %-24s%s | lex: %s' % (w.tok, g[1], w.gloss, flag, mean))
