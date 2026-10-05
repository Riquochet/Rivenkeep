import csv,sys
rows=list(csv.DictReader(open('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv'),delimiter='\t'))
for w in sys.argv[1:]:
    hits=[r for r in rows if r['orrowen'].lower().startswith(w.lower())]
    for r in hits[:8]:
        print('%s [%s] %s'%(r['orrowen'],r['pos'],r['meanings'][:150]))
    if not hits: print(w,'-- NONE')
    print('-')
