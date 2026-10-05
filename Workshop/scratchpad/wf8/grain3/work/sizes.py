import re, sys, collections
s=open(sys.argv[1]).read()
tot=len(s)
c=collections.Counter()
c['symbols']=sum(len(m.group(0)) for m in re.finditer(r'<symbol.*?</symbol>', s))
c['uses(transform)']=sum(len(m.group(0)) for m in re.finditer(r'<use href="#[^"]*" transform="[^"]*"/>', s))
c['tone styles']=sum(len(m.group(0)) for m in re.finditer(r'<g style="[^"]*">', s))
s2=re.sub(r'<symbol.*?</symbol>','',s)
for m in re.finditer(r'<path([^>]*?)\sd="([^"]*)"', s2):
    attrs=m.group(1)
    idm=re.search(r'id="[^-]*-([^"]*)"', attrs)
    op=re.search(r'(stroke-opacity|fill-opacity)="([^"]*)"', attrs)
    sw=re.search(r'stroke-width="([^"]*)"', attrs)
    key = ('id:'+re.sub(r'\d+$','#',idm.group(1))) if idm else ('%s %s w%s' % (op.group(1) if op else '', op.group(2) if op else '', sw.group(1) if sw else ''))
    c[key]+=len(m.group(0))
for k,v in c.most_common(30):
    print('%7.1f KB  %s' % (v/1024, k))
print('total %.1f KB' % (tot/1024))
