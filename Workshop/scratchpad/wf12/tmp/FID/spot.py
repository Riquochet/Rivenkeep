#!/usr/bin/env python3
"""spot.py LEAF LINE [LINE...]: the Book's English, the unit's Orrowen (as the page's fold gives it), the unit's own
word-for-word, and the analyzer's --gloss of the Orrowen, for a reader to judge the alignment"""
import json, os, re, subprocess, sys, html
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
P=json.load(open(S+'/wf12/orig/panes.json'))
B=open(S+'/wf11/book_v3.md',encoding='utf-8').read().split('\n')
HERE=os.path.dirname(os.path.abspath(__file__))
leaf=sys.argv[1]
for ln in map(int,sys.argv[2:]):
    b=next(x for x in P[leaf] if x['line']==ln)
    print('='*100)
    print('%s b%d  [%s]  src %s' % (leaf, ln, b['kind'], b.get('src')))
    print('BOOK :', ' '.join(B[ln-1:(b.get('end_line') or ln)]))
    m=re.search(r'<details class="tr rom">.*?<div class="tr-body">(.*?)</div></details>',b['html'],flags=re.S)
    rom=html.unescape(re.sub(r'<[^>]+>','',m.group(1).replace('</p><p>',' / '))) if m else None
    ink=html.unescape(re.sub(r'<[^>]+>','',re.search(r'<(?:p|h4|div) class="(?:ink|verse ink|part ink)[^"]*"[^>]*>(.*?)</(?:p|h4|div)>',b['html'],flags=re.S).group(1))) if re.search(r'class="(?:ink|verse ink|part ink)',b['html']) else None
    print('ORIG :', rom)
    print('INK  :', ink)
    u,l=b['src'].split(':')
    U=open(S+'/wf12/units/%s.md'%u,encoding='utf-8').read().split('\n')
    i=int(l)
    k=i
    while k<len(U) and (U[k-1].startswith('>') or U[k-1].startswith('```') or not U[k-1].strip() or k==i):
        k+=1
    seen=0
    for k2 in range(k, min(k+30,len(U))):
        if U[k2].startswith('>') or U[k2].startswith('**Ring') or U[k2].startswith('#'):
            break
        if 'Word for word' in U[k2][:20] or U[k2].startswith('- *Gloss') or U[k2].startswith('- **Reads') or U[k2].startswith('- *Word for word'):
            print('UNIT :', U[k2][:700])
    for lit in re.findall(r'<p class="lit"><span class="lit-h">Literal reading</span>(.*?)</p>',b['html'],flags=re.S):
        print('LIT  :', html.unescape(re.sub(r'<[^>]+>','',lit)).strip()[:900])
    g=re.search(r'<pre class="gn">(.*?)</pre>',b['html'],flags=re.S)
    if g and b['kind'] in ('ring','ring-cont'):
        print('GN   :', html.unescape(g.group(1)).replace('\n','\n       ')[:1200])
    if rom:
        r=re.sub(r'\[|\]','',rom).replace(' / ',' ')
        out=subprocess.run(['python3',HERE+'/orr_analyze.py','--gloss',r],capture_output=True,text=True,cwd=HERE).stdout
        print('GLOSS:'); print('   '+out.strip().replace('\n','\n   ')[:3000])
