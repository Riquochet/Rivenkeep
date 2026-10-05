import sys, json, collections
sys.path.insert(0,'/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/orig')
import orr_analyze as A
lex=A.Lexicon()
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
out=json.load(open(S+'/gloss/S01.json'))
small=set(A.__dict__.get('FUNCTION',{}) or [])
pairs=collections.OrderedDict()
for r in out:
    for w,g in r['gloss']:
        pairs.setdefault(w.lower(),collections.Counter())[g]+=1
skip={'et','re','es','nath','ho','sa','eth','ell','veth','amm','somm','tul','sy','ull','vodh','cedh','gor','sost','hos','o','en','ey','ol','va','sona','so','el','ew','nel','new','doss','lo','um','ul','hy','dem','pa','lom','lor','los'}
for w,c in pairs.items():
    if w in skip: continue
    ps=A.analyse_word(w,lex)
    if ps:
        p=ps[0]; m=p.row['meanings'][:110]; st=p.row['orrowen']+' '+'+'.join(p.layers)+(' '+p.mut if p.mut else '')
    else: m='(no parse)'; st=''
    print(f"{w:16} {dict(c)!s:40} || {st:22} {m}")
