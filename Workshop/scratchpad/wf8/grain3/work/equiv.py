"""equiv.py - v2 and v3 must agree on everything that is read: identical plates and young rounds (byte for
byte), and on the whole rounds the same marks, runner courses, crossings (over, under, kind) and runner ends."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import render_grain2_ref as V2
import render_grain3 as V3
os.chdir(os.path.dirname(HERE))
res = {}
same = []
for name in ['E1-01', 'E1-02', 'E1-03', 'E1-04', 'E1-05', 'E1-06', 'E1-07', 'BURN', 'VI-1', 'NAELEAR']:
    raw = open('texts/%s.gn2' % name, encoding='utf-8').read()
    a = V2.Renderer(V2.parse_gn(raw)).render()
    b = V3.Renderer(V3.parse_gn(raw)).render()
    same.append((name, a == b))
for name, plates in (('IV-6', [5, 7, 9]), ('GIFT', [2])):
    raw = open('texts/%s.gn2' % name, encoding='utf-8').read()
    for k in plates:
        a = V2.Renderer(V2.parse_gn(raw), plate=k).render()
        b = V3.Renderer(V3.parse_gn(raw), plate=k).render()
        same.append(('%s plate %d' % (name, k), a == b))
print('byte-identical to v2:', ', '.join('%s %s' % (n, 'yes' if ok else 'NO') for n, ok in same))
for name in sys.argv[1:]:
    raw = open('texts/%s.gn2' % name, encoding='utf-8').read()
    r2 = V2.Renderer(V2.parse_gn(raw)); r2.render()
    r3 = V3.Renderer(V3.parse_gn(raw)); r3.render()
    marks2 = sorted((str(k), round(v['th'], 6), round(v['rin'], 3), round(v['rout'], 3)) for k, v in r2.recs.items())
    marks3 = sorted((str(k), round(v['th'], 6), round(v['rin'], 3), round(v['rout'], 3)) for k, v in r3.recs.items())
    lines_same = sorted(r2.lines) == sorted(r3.lines) and all(
        len(r2.lines[k]) == len(r3.lines[k]) and all(abs(p[0] - q[0]) < 1e-9 and abs(p[1] - q[1]) < 1e-9 for p, q in zip(r2.lines[k], r3.lines[k])) for k in r2.lines)
    f2 = sorted((o, u, k, round(x[0], 3), round(x[1], 3)) for o, u, k, x in r2.found)
    f3 = sorted((o, u, k, round(x[0], 3), round(x[1], 3)) for o, u, k, x in r3.found)
    e2 = sorted((rid, rn.role, tuple(round(v, 3) for v in a), tuple(round(v, 3) for v in b)) for rid, rn, a, b, tr in r2.ends)
    e3 = sorted((rid, rn.role, tuple(round(v, 3) for v in a), tuple(round(v, 3) for v in b)) for rid, rn, a, b, tr in r3.ends)
    w2, w3 = sorted(set(r2.warnings)), sorted(set(r3.warnings))
    kinds = {}
    for o, u, k, x in r3.found:
        kinds[k] = kinds.get(k, 0) + 1
    print('%s: marks %s (%d), runner courses %s (%d), crossings %s (%s), runner ends %s (%d), warnings %s (%d); pw %.2f'
          % (name, 'same' if marks2 == marks3 else 'DIFFER', len(marks3), 'same' if lines_same else 'DIFFER', len(r3.lines),
             'same' if f2 == f3 else 'DIFFER', ', '.join('%s %d' % kv for kv in sorted(kinds.items())),
             'same' if e2 == e3 else 'DIFFER', len(e3), 'same' if w2 == w3 else 'DIFFER', len(w3), r3.pw))
    if w2 != w3:
        print('  only v2:', [w for w in w2 if w not in w3]); print('  only v3:', [w for w in w3 if w not in w2])
