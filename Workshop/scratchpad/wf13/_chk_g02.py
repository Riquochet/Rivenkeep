import re,sys
SP='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/'
new=open(SP+'wf13/plain/g02.md').read().split('## WRITER')[0]
old=open(SP+'wf11/plain_v3.md').read()
book=open(SP+'wf11/book_v3.md').read()
def sect(txt,h,nxt):
    a=txt.index(h); b=txt.index(nxt,a+1) if nxt in txt[a+1:] else len(txt)
    return txt[a:b]
for h,n in [('### I.2','### I.3'),('### I.3','### I.4')]:
    nn=sect(new+'### I.4',h,n); oo=sect(old,h,n); bb=sect(book,h,n)
    rx=re.compile(r'<!--.*?-->|^(?:> ?)*:::.*$|\{\{[^}]*\}\}|\[⟦[^⟧]*⟧\]|▒+|^#+ .*$|^\*.*:\*$|^> ',re.M)
    mn=[m.group(0) for m in rx.finditer(nn)]; mo=[m.group(0) for m in rx.finditer(oo)]
    # compare comment markers and headings only, and pair-name sets
    cm=lambda L:[x for x in L if x.startswith('<!--') or x.startswith('#') or x.startswith(':::')]
    print(h,'markers same:',cm(mn)==cm(mo), cm(mn))
    print('  pairs new',sorted(set(x for x in mn if x.startswith('{{'))),'old',sorted(set(x for x in mo if x.startswith('{{'))))
    print('  blockquote lines new',sum(1 for x in mn if x=='> '),'old',sum(1 for x in mo if x=='> '))
    wn=len(nn.split()); wb=len(bb.split())
    print('  words new',wn,'book',wb,'pct',round(100*wn/wb))
    old_words=r'\b(ere|naught|aught|wist|ye|thee|thou|thy|spake|bade|sware|bare|nigh|whither|thither|whoso|lest|forgat|wherefore|hath|doth)\b|\w+eth\b|\w+est\b'
    print('  oldwords:',sorted(set(m.group(0) for m in re.finditer(old_words,nn,re.I))))
    print('  semicolons:',nn.count(';'))
    # sentence stats
    body=re.sub(r'<!--.*?-->|^#.*$','',nn,flags=re.M)
    sents=[s for s in re.split(r'(?<=[.!?])["”]?\s+',body) if s.strip()]
    lens=[len(s.split()) for s in sents]
    print('  sentences',len(sents),'mean',round(sum(lens)/len(lens),1),'max',max(lens))
    long=[s.strip()[:120] for s in sents if len(s.split())>30]
    for s in long: print('   LONG:',s)
