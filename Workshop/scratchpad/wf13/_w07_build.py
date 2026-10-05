import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
src=json.load(open(S+'/gloss_in/W07.json'))
G={
'Tevyl':['Growing'],
'Et heth gemmest.':['the','spring','fourth'],
'Re lymm Halvard':['(past)','carried','Halvard','the','heart','this','to','high','on','the','shoulder',
 'and','when','(past)','was','it','on-him','still','(past)','came','it','into-them-two','both','though','Rhyna','at','the','hearth',
 'was','great','it','than-them-two','and','(past)','rested','it','in','the','vault','until','spring',
 '(past)','I laid','song','the','heart','in','verse','near','as','(future)','will go','the','ink'],
'— Vellyl.':['singing','time','long','singing','bending','to-it'],
'— Gann,':['trunk','and','root','and','sapling','led','led','to','far'],
'— Sceth.':['hull','no one','in-it','no one','very'],
'— Meskrivullath':['roots','in','low','every','thing','they bind','kin','and','kin','and','kin'],
'— Et vellyl':['the','singing'],
'— hess.':['stops','blade','in','the','heart'],
'— Stinet':['cut','into-us','in','the','stroke'],
'Eth re dhess nahos.':['and','(past)','answered','no one'],
}
out=[];seen=set()
for r in src:
    if r['rom'] in seen: continue
    seen.add(r['rom'])
    k=[k for k in G if r['rom'].startswith(k)]
    assert len(k)==1,(r['rom'],k)
    g=G[k[0]]; words=[w for w,_ in r['draft']]
    assert len(g)==len(words),(r['rom'][:30],len(g),len(words))
    out.append({'rom':r['rom'],'gloss':[[w,e] for w,e in zip(words,g)]})
json.dump(out,open(S+'/gloss/W07.json','w'),ensure_ascii=False,indent=1)
for o in out: print(' · '.join(f'{w}={e}' for w,e in o['gloss']))
