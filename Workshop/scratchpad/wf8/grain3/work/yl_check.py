import sys, os, re, pickle, math
sys.path.insert(0,'work'); sys.path.insert(0,'..')
sys.setrecursionlimit(100000)
import render_grain3 as R, shoot3
name, v2p, v3p, out = sys.argv[1:5]
rd = pickle.load(open('work/%s.pkl' % name,'rb'))
def strip(svg):
    svg = re.sub(r'<title[^>]*>.*?</title>', '', svg, flags=re.S); svg = re.sub(r'<desc[^>]*>.*?</desc>', '', svg, flags=re.S)
    return re.sub(r' aria-labelledby="[^"]*"', '', svg)
S2=strip(open(v2p).read()); S3=strip(open(v3p).read())
p2=re.search(r'id="(g[0-9a-f]+)-', S2).group(1); S2=S2.replace(p2,p2+'v2')
cells=[]; n=0
for key, rec in sorted(rd.recs.items(), key=lambda kv: str(kv[0])):
    if rec.get('kind')!='mark' or rec['mk'].root or rec['y']<2: continue
    n+=1
    if n % 3: continue
    fld=rec['field']; k=rec['k']
    a0=rd.lay.year_r[(k, rec['y'])][0]
    c=fld.pt(fld.yr(k, a0, rec['th']), rec['th']); size=46
    x,y=c[0]-size/2,c[1]-size/2
    cr=lambda s: re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"','viewBox="%g %g %g %g" width="280" height="280"'%(x,y,size,size),s,count=1)
    cells.append('<div style="padding:4px"><div style="display:flex;gap:4px">%s%s</div><div style="font:11px Georgia;color:#b8aa8a">%s %s, year %d: its year-line at the centre</div></div>'%(cr(S2),cr(S3),R.addr_text(key),rec['mk'].lig.text(),rec['y']))
    if len(cells)>=10: break
body='<div style="display:grid;grid-template-columns:repeat(2,580px)">%s</div>'%''.join(cells)
open(out+'.html','w').write(shoot3.page(body)); shoot3.chrome(out+'.html',out,1180,5*310)
