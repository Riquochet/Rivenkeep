import sys, time, math
sys.path.insert(0, sys.argv[1])
import importlib
R = importlib.import_module(sys.argv[2])
for n in sys.argv[3:]:
    t=time.time()
    md = R.parse_gn(open('texts/%s.gn2' % n, encoding='utf-8').read())
    rd = R.Renderer(md)
    svg = rd.render()
    kinds = {}
    for o,u,k,x in rd.found:
        kinds[k] = kinds.get(k,0)+1
    xs=[p[0] for p in rd.bbox_pts]; ys=[p[1] for p in rd.bbox_pts]
    L = sum(R.arclen(p)[-1] for p in rd.lines.values())
    print(n, 'time %.1fs' % (time.time()-t), 'KB %.0f' % (len(svg)/1024), 'diam %.0f x %.0f' % (max(xs)-min(xs), max(ys)-min(ys)), 'runners', len(rd.lines), 'len %.0f' % L, 'crossings', kinds, 'silh', rd.runner_silhouette, 'R', [round(r) for r in rd.lay.R])
