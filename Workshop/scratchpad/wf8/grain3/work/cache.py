"""cache.py - render a round once (routing is the slow part), pickle the renderer after its runners are cut,
then re-paint quickly with the current render_grain3 code (presentation experiments only).
    python3 cache.py build NAME          -> work/NAME.pkl
    python3 cache.py paint NAME OUT.svg  -> repaint from the pickle
"""
import sys, pickle, os, importlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.setrecursionlimit(100000)
import render_grain3 as R
cmd, name = sys.argv[1], sys.argv[2]
pk = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.pkl')
if cmd == 'build':
    md = R.parse_gn(open('texts/%s.gn2' % name, encoding='utf-8').read())
    rd = R.Renderer(md)
    rd.build_marks()
    real = (rd.crossings, rd.cut_runner, rd.pocket_border)
    rd.crossings = lambda: None
    rd.cut_runner = lambda rid: None
    rd.pocket_border = lambda pr: None
    rd.draw_runners()
    del rd.crossings, rd.cut_runner, rd.pocket_border
    pickle.dump(rd, open(pk, 'wb'))
    print('built', pk)
else:
    rd = pickle.load(open(pk, 'rb'))
    # re-cut the runners with the current code (widths, gaps are presentation)
    rd.rcuts = R.Cuts()
    rd.stroke_bins = {}
    if hasattr(rd, '_nbr'):
        del rd._nbr
    big = rd.plate is None and not rd.stage0 and rd.md.K > 2
    rd.pw = max(1.0, min(R.PW_MAX, rd.lay.R[rd.md.K] / R.PW_REF)) if big else 1.0
    rd.pwr = 1.0 + 0.5 * (rd.pw - 1.0)
    pkl = {k: v for k, v in rd.lines.items() if k.startswith('pk:')}
    for k in pkl:
        del rd.lines[k]
    rd.crossings()
    rd.lines.update(pkl)
    rd.ends = []
    for rid in list(rd.lines):
        rd.cut_runner(rid)
    for pr in rd.pockets.values():
        rd.pocket_border(pr)
    rd.add_dips()
    wood = rd.paint_wood()
    svg = rd.assemble(wood)
    open(sys.argv[3], 'w', encoding='utf-8').write(svg)
    print(sys.argv[3], '%.1f KB' % (len(svg.encode()) / 1024))
