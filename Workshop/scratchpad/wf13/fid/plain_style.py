"""italic / bold of every word: plain_v31.md vs the page's Plain view"""
import sys, re, collections, html as H; sys.path.insert(0,'.')
from pg import *
import importlib.util
MD='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/plain_v31.md'
TOKEN='Neivaere, in the cellars of Glasspire'
WRE=re.compile(r"▒+|[A-Za-z0-9À-ž][A-Za-z0-9À-ž'’…]*")
def norm(w): return w.replace('’',"'")
md=open(MD,encoding='utf-8').read()
# md: walk, skipping comments, fences, rules, table separators, heading/list/quote markers
out=[]
for l in md.split('\n'):
    s=re.sub(r'^(> ?)+','',l)
    if re.match(r'^\s*<!--.*-->\s*$',s) or re.match(r'^:::',s) or s.strip()=='---' or re.match(r'^\|[-| :]+\|$',s.strip()): continue
    s=re.sub(r'<!--.*?-->',' ',s)
    s=re.sub(r'^(#+ |- )','',s)
    s=re.sub(r'\{\{([A-Za-z]+)\}\}',r'\1',s).replace('{LAST_THRONE_AT_HAVEN}',TOKEN)
    s=re.sub(r'⟦[a-z0-9_]+⟧',' ',s)
    it=bd=False; i=0
    while i<len(s):
        if s.startswith('**',i): bd=not bd; i+=2; continue
        if s[i]=='*': it=not it; i+=1; continue
        m=WRE.match(s,i)
        if m: out.append((norm(m.group(0)),it,bd)); i=m.end(); continue
        i+=1
b=open(V31,encoding='utf-8').read()
v=strip_panes(b, kinds=('book','orig'))
body=v[v.find('<h1'):v.rfind('<!--PANE orig-->')]
body=re.sub(r'<(script|style)\b.*?</\1>',' ',body,flags=re.S)
body=re.sub(r'<svg\b.*?</svg>',' ',body,flags=re.S)
body=re.sub(r'<label\b.*?</label>',' ',body,flags=re.S)
body=re.sub(r'<summary>.*?</summary>',' ',body,flags=re.S)
body=re.sub(r'<span class="kind">.*?</span>',' ',body,flags=re.S)
pg=[]; st=[]
for part in re.split(r'(<[^>]+>)', body):
    if part.startswith('<'):
        m=re.match(r'<(/?)(em|strong|i|b)\b',part)
        if m:
            if m.group(1): 
                if st and st[-1]==m.group(2): st.pop()
            else: st.append(m.group(2))
        continue
    t=H.unescape(part)
    for m in WRE.finditer(t):
        pg.append((norm(m.group(0)),('em' in st or 'i' in st),('strong' in st or 'b' in st)))
# glue split words (Halyna</span>'s) : re-tokenise page words by joining adjacent fragments is complex; align with difflib on words
import difflib
mw=[w for w,_,_ in out]; pw=[w for w,_,_ in pg]
sm=difflib.SequenceMatcher(None,mw,pw,autojunk=False)
diffs=[o for o in sm.get_opcodes() if o[0]!='equal']
print('words md', len(mw), 'page', len(pw), 'non-equal chunks', len(diffs), [ (mw[i1:i2],pw[j1:j2]) for _,i1,i2,j1,j2 in diffs][:12])
C=collections.Counter(); ex=collections.defaultdict(list)
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op!='equal': continue
    for k in range(i2-i1):
        a=out[i1+k]; c=pg[j1+k]
        if a[1:]!=c[1:]:
            key=('md it=%d bd=%d' % a[1:], 'page it=%d bd=%d' % c[1:])
            C[key]+=1; ex[key].append(i1+k)
print('style mismatches:', dict(C))
for key,idx in ex.items():
    # group consecutive runs
    runs=[]; 
    for i in idx:
        if runs and i==runs[-1][1]+1: runs[-1][1]=i
        else: runs.append([i,i])
    print(key, len(runs), 'runs')
    for r0,r1 in runs[:25]: print('    ', ' '.join(mw[max(0,r0-4):r0]), '[[', ' '.join(mw[r0:r1+1])[:120], ']]', ' '.join(mw[r1+1:r1+4]))
