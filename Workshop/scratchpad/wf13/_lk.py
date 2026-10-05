import sys,csv
L={}
for row in csv.reader(open('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv'),delimiter='\t'):
    L.setdefault(row[1].lower(),[]).append(row)
for w in sys.argv[1:]:
    rs=L.get(w.lower())
    if not rs: print('---',w,'(none)');continue
    for r in rs: print('---',w,'|',r[0],r[3],'|',r[5][:200])
