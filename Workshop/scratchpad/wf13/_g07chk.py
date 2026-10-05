import re,collections
new=open('wf13/plain/g07.md',encoding='utf-8').read()
new=new.split('## WRITER')[0]
old=open('wf11/plain_v3.md',encoding='utf-8').read().split('\n')
book=open('wf11/book_v3.md',encoding='utf-8').read().split('\n')
def sl(lines,a,b): return '\n'.join(lines[a-1:b])
oldsec={'IV.5':sl(old,1270,1347),'BK5':sl(old,1409,1412),'V.1':sl(old,1413,1471)}
booksec={'IV.5':sl(book,1494,1585),'BK5':sl(book,1659,1662),'V.1':sl(book,1663,1733)}
# split new
parts=re.split(r'(?m)^(?=### |## BOOK)',new)
newsec={}
for p in parts:
    if p.startswith('### IV.5'): newsec['IV.5']=p
    elif p.startswith('## BOOK FIVE'): newsec['BK5']=p
    elif p.startswith('### V.1'): newsec['V.1']=p
COMMENT=re.compile(r'<!--.*?-->'); BLOCK=re.compile(r'^(?:> ?)*:::.*$'); PAIR=re.compile(r'\{\{[^}]*\}\}')
def marks(t):
    out=[]
    for ln in t.split('\n'):
        s=ln.strip()
        if s.startswith('#'): out.append(s)
        if BLOCK.match(s): out.append(re.sub(r'^(?:> ?)+','> ',s))
        out+=COMMENT.findall(ln)
    return out
def blocks(t):
    return re.findall(r'(?ms)^(?:> )?::: .*?^(?:> )?:::$',t)
for k in ['IV.5','BK5','V.1']:
    n,o,b=newsec[k],oldsec[k],booksec[k]
    print(k,'marks equal:',marks(n)==marks(o), marks(n) if marks(n)!=marks(o) else '')
    if marks(n)!=marks(o): print('  old:',marks(o))
    print('  native blocks identical:',blocks(n)==blocks(o))
    print('  pairs new',dict(collections.Counter(PAIR.findall(n))),'old',dict(collections.Counter(PAIR.findall(o))))
    wn,wb=len(n.split()),len(b.split())
    print('  words new %d book %d -> %.0f%%'%(wn,wb,100*wn/wb))
    print('  semicolons:',n.count(';'))
    sents=[s for s in re.split(r'(?<=[.!?])\s+',re.sub(r'[*>#]','',n)) if len(s.split())>2]
    words=re.findall(r"[A-Za-z']+",re.sub(r'<!--.*?-->|\{\{|\}\}','',n))
    def syl(w):
        w=w.lower(); v=re.findall(r'[aeiouy]+',w); c=len(v)
        if w.endswith('e') and c>1: c-=1
        return max(c,1)
    S=sum(syl(w) for w in words)
    print('  mean sentence %.1f, FK %.1f'%(len(words)/len(sents), 0.39*len(words)/len(sents)+11.8*S/len(words)-15.59))
OLD=r"\b(ere|naught|aught|wist|ye|thee|thou|thy|spake|bade|sware|nigh|whither|thither|whoso|lest|forgat|wherefore|hath|doth|sitteth|cometh|mine own)\b"
print('old words:',re.findall(OLD,new,re.I))
print('they-check lines:',[l[:80] for l in new.split('\n') if re.search(r'\bthey\b',l) and 'Halyna' not in l][:0])
