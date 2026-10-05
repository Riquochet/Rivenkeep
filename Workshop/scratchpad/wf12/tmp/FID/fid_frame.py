#!/usr/bin/env python3
"""fid_frame.py: the frame (title page, Contents, Book heads, Arguments, tale heads) of the page, char by char"""
import re, sys
sys.argv=[sys.argv[0]]
import fid_text as F
S=F.S
h=open(F.PAGE,encoding='utf-8').read()
bad=0
for k in ('book','plain'):
    ls=open(F.SRC[k],encoding='utf-8').read().split('\n')
    # title page: lines 3..8; contents 9..84 (book). find by headings
    def block(start_pat,end_pat):
        i=next(n for n,l in enumerate(ls) if re.match(start_pat,l))
        j=next(n for n,l in enumerate(ls) if n>i and re.match(end_pat,l))
        return ls[i+1:j]
    tp=block(r'^## \*The Book of the Riven Stone\*',r'^## CONTENTS')
    ct=block(r'^## CONTENTS',r'^## OF THIS BOOK')
    sw=re.findall(r'<div class="sw tp-sw">.*?</div>\n</div>',h,flags=re.S)
    i=h.index('<div class="sw tp-sw">'); el=F.element(h,i)
    a=F.squash('*The Book of the Riven Stone* '+F.norm_src(tp)); b=F.squash(F.md_of(F.pane(el,k)))
    if a!=b: bad+=1; print(k,'TITLE PAGE',F.diffs(a,b)[:3])
    i=h.index('<div class="sw toc-sw">'); el=F.element(h,i)
    a=F.norm_src(ct); b=F.squash(F.md_of(F.pane(el,k)))
    # the Contents: the page sets the tale number in span.tn and drops the list dash; compare without * (links carry strong)
    if a!=b:
        d=F.diffs(a,b)
        print(k,'CONTENTS',len(d)); [print('   ',x['op'],repr(x['src_bit']),repr(x['page_bit']),'|',repr(x['src'][:120])) for x in d[:8]]
        bad+=1
    # Book heads and Arguments
    for m in re.finditer(r'^## (BOOK .*|EPILOGUE|APPENDIX)$',open(F.SRC[k],encoding='utf-8').read(),flags=re.M):
        title=m.group(1)
        n=next(i for i,l in enumerate(ls) if l=='## '+title)
        j=n+1
        while not ls[j].strip(): j+=1
        arg=[]
        while ls[j].strip(): arg.append(ls[j]); j+=1
        sid={'EPILOGUE':'epilogue','APPENDIX':'knowings'}.get(title) or 'book-'+str(['ONE','TWO','THREE','FOUR','FIVE','SIX'].index(title.split()[1])+1)
        i=h.index('<section id="%s"'%sid)
        hh=re.search(r'<h2 class="book-h">(.*?)</h2>',h[i:]).group(1)
        if F.squash(F.md_of(hh))!=title: bad+=1; print('HEAD',sid,repr(F.md_of(hh)),title)
        el=F.element(h,h.index('<div class="sw arg-sw">',i))
        a=F.norm_src(arg); b=F.squash(F.md_of(F.pane(el,k)))
        if a!=b: bad+=1; print(k,'ARG',sid,F.diffs(a,b)[:2])
    # tale heads
    for m in re.finditer(r'^### (.*)$',open(F.SRC[k],encoding='utf-8').read(),flags=re.M):
        lid=F.leaf_key('### '+m.group(1))
        i=h.index('id="%s"'%lid)
        hh=re.search(r'<h3 class="tale-h">(.*?)</h3>',h[i:i+3000]).group(1)
        hh=re.sub(r'<span class="kind">.*?</span>','',hh)
        if F.squash(F.md_of(hh)).replace(' · ',' · ')!=m.group(1): bad+=1; print('TALE HEAD',lid,repr(F.squash(F.md_of(hh))),repr(m.group(1)))
print('frame differences:',bad)
