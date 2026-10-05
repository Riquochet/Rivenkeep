import csv,sys
L='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv'
rows=list(csv.DictReader(open(L),delimiter='\t'))
for w in sys.argv[1:]:
    hits=[r for r in rows if r['orrowen'].lower()==w.lower()]
    if not hits: print('%-14s --'%w)
    for r in hits: print('%-14s %-6s %s'%(w,r['pos'],r['meanings'][:220]))
