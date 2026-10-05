import sys, math, json
sys.path.insert(0, sys.argv[1]); import importlib
R = importlib.import_module(sys.argv[2])
md = R.parse_gn(open('texts/%s.gn2' % sys.argv[3], encoding='utf-8').read())
rd = R.Renderer(md); svg = rd.render()
out = []
for o,u,k,x in rd.found:
    # crossing angle
    def dirat(rid, x):
        pts = rd.lines[rid]
        i = min(range(len(pts)), key=lambda q: math.hypot(pts[q][0]-x[0], pts[q][1]-x[1]))
        a, b = pts[max(i-1,0)], pts[min(i+1,len(pts)-1)]
        return R.unit(R.sub(b,a))
    da, db = dirat(o,x), dirat(u,x)
    ang = math.degrees(math.acos(min(1,abs(R.dot(da,db)))))
    out.append((o,u,k,round(x[0],1),round(x[1],1),round(ang)))
json.dump(out, open('work/%s_found.json' % sys.argv[3],'w'))
import collections
print(len(out), collections.Counter(int(a/15)*15 for *_,a in out))
