"""Plain Words on the page vs wf13/plain_v31.md: word stream diff, paragraph presence/duplication, redactions, lintels"""
import sys, re, difflib, collections, html as H; sys.path.insert(0,'.')
from pg import *
MD='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/plain_v31.md'
TOKEN='Neivaere, in the cellars of Glasspire'
b=open(V31,encoding='utf-8').read()
md=open(MD,encoding='utf-8').read()

def words(t):
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.findall(r"▒+|[A-Za-z0-9À-ž][A-Za-z0-9À-ž'…]*", t)

# ---- md -> paragraphs of visible text
def md_inline(t):
    t=re.sub(r'<!--.*?-->',' ',t)
    t=re.sub(r'\{\{([A-Za-z]+)\}\}',r'\1',t)
    t=t.replace('{LAST_THRONE_AT_HAVEN}',TOKEN)
    t=re.sub(r'⟦[a-z0-9_]+⟧',' ',t)
    return t
md_nc=re.sub(r'<!--.*?-->','',md,flags=re.S)
paras=[]   # (line, text)
cur=[]; start=None
lines=md.split('\n')
def flush():
    global cur,start
    if cur:
        paras.append((start,' '.join(cur)))
    cur=[]; start=None
for i,l in enumerate(lines,1):
    s=l
    s=re.sub(r'^(> ?)+','',s)
    if re.match(r'^\s*<!--.*-->\s*$',s): flush(); continue
    if re.match(r'^:::',s): flush(); continue
    if not s.strip() or s.strip()=='---' or re.match(r'^\|[-| :]+\|$',s.strip()): flush(); continue
    if re.match(r'^(- |\d+\. |#+ |\|)',s): flush()
    s=re.sub(r'^(#+ |- )','',s)
    if start is None: start=i
    cur.append(md_inline(s))
    if re.match(r'^(#+ |\|)', l.lstrip('> ')): flush()
flush()
P=[(ln,tuple(words(t))) for ln,t in paras if words(t)]
mdw=[w for _,p in P for w in p]

# ---- the page as Plain Words shows it
v=strip_panes(b, kinds=('book','orig'))
body=v[v.find('<body'):]
body=re.sub(r'<(script|style)\b.*?</\1>',' ',body,flags=re.S)
body=re.sub(r'<svg\b.*?</svg>',' ',body,flags=re.S)
body=re.sub(r'<label\b.*?</label>',' ',body,flags=re.S)      # the switch's labels
body=re.sub(r'<summary>.*?</summary>',' ',body,flags=re.S)   # fold labels
body=re.sub(r'<span class="kind">.*?</span>',' ',body,flags=re.S)
# start at the first pane, end after the last
fp=body.find('<h1'); lp=body.rfind('<!--PANE orig-->')
head_part=body[:fp]; tail_part=body[lp:]
mid=body[fp:lp]
mid=re.sub(r'</?(span|em|strong|i|b|a|small|sup|sub|code)\b[^>]*>','',mid)
pw=words(H.unescape(re.sub(r'<[^>]+>',' ',mid)))
print('md words', len(mdw), ' page Plain-view words (first pane .. last pane)', len(pw))
sm=difflib.SequenceMatcher(None,mdw,pw,autojunk=False)
ops=[o for o in sm.get_opcodes() if o[0]!='equal']
print('diff chunks:', len(ops))
# map md word index -> md line
idx2line=[]
for ln,p in P: idx2line+= [ln]*len(p)
for op,i1,i2,j1,j2 in ops:
    ln=idx2line[min(i1,len(idx2line)-1)]
    print('  %-7s md line %5d  md[%d:%d] %r  ->  page %r' % (op, ln, i1,i2, ' '.join(mdw[i1:i2])[:160], ' '.join(pw[j1:j2])[:160]))
print('words before the first pane on the page:', ' '.join(words(H.unescape(re.sub(r'<[^>]+>',' ',head_part))))[:600])
print('words after the last pane on the page:', ' '.join(words(H.unescape(re.sub(r'<[^>]+>',' ',tail_part))))[:600])

# ---- paragraphs: each md paragraph present as often as the md has it
J='\x01'
pstream=J+J.join(pw)+J
mstream=J+J.join(mdw)+J
bad=[]
for ln,p in P:
    if len(p)<4: continue
    k=J+J.join(p)+J
    a=mstream.count(k); c=pstream.count(k)
    if a!=c: bad.append((ln,a,c,' '.join(p)[:120]))
print('paragraphs (>=4 words):', sum(1 for _,p in P if len(p)>=4), ' present a different number of times on the page:', len(bad))
for x in bad[:40]: print('   md line %d: md x%d, page x%d: %s' % x)

# ---- block boundaries: md paragraph starts vs the page's block starts
BLK=re.compile(r'<(p|li|h[1-6]|tr|td|th|div|blockquote|figcaption|aside|details|figure|span class="l[^"]*"|span class="cap"|br)\b[^>]*>')
mid2=body[fp:lp]
tag_at=[]   # (word index, tag)
pos=0; widx=0; out=[]
for m in BLK.finditer(mid2):
    seg=mid2[pos:m.start()]
    seg=re.sub(r'</?(span|em|strong|i|b|a|small|sup|sub|code)\b[^>]*>','',seg)
    widx+=len(words(H.unescape(re.sub(r'<[^>]+>',' ',seg))))
    tag_at.append((widx, m.group(1).split()[0] if not m.group(1).startswith('span') else m.group(1)))
    pos=m.end()
pb=collections.defaultdict(set)
for w,t in tag_at: pb[w].add(t)
starts=[]; acc=0
for ln,p in P:
    starts.append((acc,ln)); acc+=len(p)
mds=set(s for s,_ in starts)
merged=[(ln,s) for s,ln in starts if s not in pb]
print('md paragraph starts not at a page block start (merged paragraphs):', len(merged), merged[:20])
extra=collections.Counter(); ex=collections.defaultdict(list)
for w,ts in pb.items():
    if w in mds or w>=len(pw): continue
    k=tuple(sorted(ts)); extra[k]+=1; ex[k].append(' '.join(pw[max(0,w-6):w])+' | '+' '.join(pw[w:w+6]))
print('page block starts inside an md paragraph, by tag:')
for k,v in extra.most_common(): print('   ',v,k, ex[k][:3])
# line-level starts in md (same word stream as P)
line_start={}; acc=0
for ln,t in paras:
    pass
# recompute: walk md lines in the same way as the paragraph parser, counting words per line
acc=0
for i,l in enumerate(lines,1):
    s=re.sub(r'^(> ?)+','',l)
    if re.match(r'^\s*<!--.*-->\s*$',s) or re.match(r'^:::',s) or not s.strip() or s.strip()=='---' or re.match(r'^\|[-| :]+\|$',s.strip()): continue
    s2=re.sub(r'^(#+ |- )','',s)
    n=len(words(md_inline(s2)))
    if n: line_start.setdefault(acc,(i,s.strip()))
    acc+=n
kinds=collections.Counter(); odd=[]
for w,ts in pb.items():
    if w in mds or w>=len(pw) or ts!={'p'}: continue
    ln,s=line_start.get(w,(None,''))
    k='reading fragment line' if re.match(r'^\*?—',s) else 'other'
    kinds[k]+=1
    if k=='other': odd.append((ln,s[:100]))
print('the in-paragraph <p> starts:', dict(kinds)); [print('   ',o) for o in odd]
