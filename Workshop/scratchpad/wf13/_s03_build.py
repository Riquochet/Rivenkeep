import json,re
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
d=json.load(open(S+'/gloss_in/S03.json'))
G={}
for line in open(S+'/_s03_glosses.txt'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    i,rest=line.split(':',1)
    G[int(i)]=[g.strip() for g in rest.split('|')]
out=[];seen={};bad=0
for i,r in enumerate(d):
    words=[w for w,_ in r['draft']]
    g=G.get(i)
    if g is None or len(g)!=len(words):
        bad+=1
        print('COUNT', i, len(words), None if g is None else len(g))
        if g:
            for k,(w,x) in enumerate(zip(words,g)): print('   ',k,w,x)
        continue
    row={'rom':r['rom'],'gloss':[[w,x] for w,x in zip(words,g)]}
    if r['rom'] in seen:
        if seen[r['rom']]!=row['gloss']: print('DUP MISMATCH',i)
        continue
    seen[r['rom']]=row['gloss']
    out.append(row)
if not bad:
    json.dump(out,open(S+'/gloss/S03.json','w'),ensure_ascii=False,indent=1)
    print('wrote',len(out))
