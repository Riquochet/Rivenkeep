import sys, re, difflib, collections; sys.path.insert(0,'.')
from pg import *
a=open(V30,encoding='utf-8').read(); b=open(V31,encoding='utf-8').read()
oa=[p for p in panes(a) if p[0]=='orig']; ob=[p for p in panes(b) if p[0]=='orig']
IL=re.compile(r'<p class="il">(.*?)</p>', re.S)
def un_il(m):
    x=m.group(1)
    x=re.sub(r' ?<span class="sr">Word by word: .*?</span>$', '', x, flags=re.S)
    x=re.sub(r'<small aria-hidden="true">.*?</small>', '', x)
    x=x.replace('<i>','').replace('</i>','')
    return '<p><em>%s</em></p>' % x
def norm(h, landmarks=True):
    h=IL.sub(un_il, h)
    if landmarks: h=re.sub(r' data-m="(dl1|hn1)"','',h)
    return h
C=collections.Counter(); nd=0
for i,(x,y) in enumerate(zip(oa,ob)):
    yy=norm(y[3]); xx=re.sub(r' data-m="(dl1|hn1)"','',x[3])
    if yy!=xx:
        nd+=1
        sm=difflib.SequenceMatcher(None,xx,yy,autojunk=False)
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op!='equal': C[(op,xx[max(0,i1-90):i2+40],yy[max(0,j1-90):j2+40])]+=1
print('orig panes', len(oa), len(ob), '; differing after un-glossing:', nd)
for k,v in C.most_common(40): print(v,k[0]); print('   OLD',repr(k[1])); print('   NEW',repr(k[2]))
# landmark attrs on orig
print('v3.0 orig dl1/hn1:', sum(len(re.findall(r'data-m="(?:dl1|hn1)"',p[3])) for p in oa), ' v3.1:', sum(len(re.findall(r'data-m="(?:dl1|hn1)"',p[3])) for p in ob))
