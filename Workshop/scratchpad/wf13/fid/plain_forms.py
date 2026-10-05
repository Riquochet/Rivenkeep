import sys, re, collections, html as H; sys.path.insert(0,'.')
from pg import *
MD='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/plain_v31.md'
BOOKMD='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf11/book_v3.md'
b=open(V31,encoding='utf-8').read(); a=open(V30,encoding='utf-8').read()
md=open(MD,encoding='utf-8').read(); md_nc=re.sub(r'<!--.*?-->','',md,flags=re.S)
P=panes(b); Pa=panes(a)
units=[]   # per switch unit: (book, plain, orig)
for i in range(0,len(P),3):
    assert [x[0] for x in P[i:i+3]]==['book','plain','orig']
    units.append((P[i][3],P[i+1][3],P[i+2][3]))
def unit_id(i):
    s=P[3*i][1]; m=list(re.finditer(r'<(?:article|section|div)[^>]*\bid="([^"]+)"', b[:s]))
    return m[-1].group(1) if m else '?'
FIX=re.compile(r'<p class="(seal|answer|answer silent|answer hood|laid)"[^>]*>(.*?)</p>', re.S)
print('== fixed lines (the closes), Book pane vs Plain pane, leaf by leaf')
nb=npl=0; mism=[]
for i,(bk,pl,og) in enumerate(units):
    fb=[c for c,_ in FIX.findall(bk)]; fp=[c for c,_ in FIX.findall(pl)]
    nb+=len(fb); npl+=len(fp)
    if fb!=fp: mism.append((unit_id(i),fb,fp))
print('Book fixed lines', nb, ' Plain fixed lines', npl, ' leaves whose sequence differs:', len(mism))
for m in mism: print('   ', m)
# plain texts of the fixed lines
C=collections.Counter()
for bk,pl,og in units:
    for c,t in FIX.findall(pl): C[(c,re.sub(r'<[^>]+>','',t))]+=1
for k,v in sorted(C.items()): print('   %3d  %-14s %s' % (v,k[0],k[1]))
# md paragraphs that look like closes but are not set as one
cand=[l.strip('> ').strip() for l in md_nc.split('\n') if re.search(r'We remember|hood back|laid for (me|us)|held in the grain|no one answered', l)]
rendered=set(H.unescape(re.sub(r'<[^>]+>','',t)) for bk,pl,og in units for c,t in FIX.findall(pl))
print('md lines naming a close:', len(cand))
for c in cand:
    t=re.sub(r'\*','',re.sub(r'\{\{([A-Za-z]+)\}\}',r'\1',c))
    if t not in rendered: print('   NOT set as a close:', c[:160])
# ---- redactions
print('== ▒▒▒▒: md', len(re.findall('▒+',md_nc)), [len(x) for x in re.findall('▒+',md_nc)][:3],
      ' Plain panes', sum(len(re.findall('▒+',pl)) for _,pl,_ in units),
      ' Book panes', sum(len(re.findall('▒+',bk)) for bk,_,_ in units),
      ' Book md', len(re.findall('▒+',re.sub(r'<!--.*?-->','',open(BOOKMD,encoding='utf-8').read(),flags=re.S))))
# redaction per leaf, book vs plain
for i,(bk,pl,og) in enumerate(units):
    x,y=len(re.findall('▒+',bk)),len(re.findall('▒+',pl))
    if x or y: print('    %-14s book %d plain %d %s' % (unit_id(i), x, y, '' if x==y else '<-- differs'))
# ---- lintels
mdn=re.findall(r'\{\{([A-Za-z]+)\}\}', md_nc)
v=strip_panes(b, kinds=('book','orig'))
pgn=re.findall(r'<span class="pair">([A-Za-z]+)</span>', v)
print('== lintels: md {{Name}}', len(mdn), collections.Counter(mdn).most_common(), '\n   Plain view span.pair', len(pgn), collections.Counter(pgn).most_common(), '\n   same sequence:', mdn==pgn)
# a pair name in the Plain panes NOT under a lintel where the md has it bare? (pair names written bare in md)
PAIRS=('Halyna','Aldwena','Idrenna','Orvenna','Enrella','Wendhessa')
bare_md=sum(len(re.findall(r'(?<!\{\{)\b(%s)\b(?!\}\})'%n, md_nc)) for n in PAIRS)
txt_pairs=sum(len(re.findall(r'\b(%s)\b'%n, re.sub(r'<span class="pair">[A-Za-z]+</span>','', re.sub(r'<(svg|script|style)\b.*?</\1>','',v,flags=re.S)))) for n in PAIRS)
print('   pair names written bare (no lintel): md', bare_md, ' Plain view', txt_pairs)
