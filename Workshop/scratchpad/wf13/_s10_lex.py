import sys, json
sys.path.insert(0,'/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/orig')
import orr_analyze as A
lex = A.Lexicon('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv')
d=json.load(open('gloss_in/S10.json'))
common=set(x.strip() for x in open('/dev/null'))
seen={}
for r in d:
    ws=A.analyse_text(r['rom'],lex)
    for w in ws:
        if w.kind=='punct': continue
        k=w.tok.lower()
        if k in seen: continue
        b=w.best
        row=b.row if b else None
        alts=[]
        for p in (w.parses or [])[:4]:
            if p.row: alts.append('%s[%s]%s:%s'%(p.row['orrowen'],'+'.join(p.layers),p.mut or '',(p.row['meanings'] or '')[:70]))
        seen[k]=1
        print('%-14s %-22s| %s'%(w.tok, w.gloss, ' || '.join(alts) if alts else (row['meanings'][:90] if row else '')))
