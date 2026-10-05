import csv,sys
L='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv'
rows=list(csv.DictReader(open(L),delimiter='\t'))
for w in sys.argv[1:]:
    if w.startswith('~'):
        hits=[r for r in rows if w[1:].lower() in r['orrowen'].lower()]
    else:
        hits=[r for r in rows if r['orrowen'].lower()==w.lower()]
    if not hits: print(w,'-- NONE')
    for r in hits[:12]: print(w,'=>',r['orrowen'],'|',r['pos'],'|',r['meanings'][:160])
