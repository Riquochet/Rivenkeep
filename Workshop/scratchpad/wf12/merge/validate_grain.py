#!/usr/bin/env python3
"""(wf12 copy of wf8/tmp/merge/validate_grain.py) Re-validate every wf12 unit's grain against the merged spec
(wf12/grain_v2_full.md), with a private copy of the validator whose root (wf12/merge/groot) links wf7/grain_v2.md to the
merged spec:
  1. every GN block of every unit file (`--md`), which is what the unit prints (the builder reads these);
  2. the units' GN sources as they stand after their fixes (knowing form and canonical), in wf12/tmp/<unit>[fix]/;
  3. the blind rounds (wf12/blind/*_grain.gn2, the rounds with no `# file` comments);
  4. with --corpus, the coverage corpus (wf7/coverage/tests/*.gn2) and the IV.4 pilot, to show the merged compounds
     change no finding."""
import glob, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
S = os.path.dirname(W12)
V = os.path.join(HERE, 'groot', 'wf7', 'grain_validate.py')
T = os.path.join(W12, 'tmp') + '/'
SOURCES = {
    'S08': ['S08/S08.gn2'],
    'S09': ['S09fix/e4-01.gn2', 'S09fix/e5-02.gn2', 'S09fix/v7-iii.gn2'],
    'S10': ['S10/stone.gn2', 'S10/song.gn2', 'S10/sliver.gn2'],
    'S11': ['S11/s11_carvings.gn2'],
    'W01': ['W01fix/II-2.gn2', 'W01fix/II-2.canon.gn2'],
    'W02': ['W02fix/IV-2.gn2', 'W02fix/IV-2.canon.gn2'],
    'W03': ['W03fix/IV-4.gn2', 'W03fix/IV-4.canon.full.gn2', 'W03fix/GIFT.unit.gn2'],
    'W04': ['W04/IV-6.gn2'],
    'W05': ['W05/V-3.gn2', 'W05/V-3.canon.gn2'],
    'W06': ['W06/V-4.gn2', 'W06/V-4.canon.gn2', 'W06/GROW.unit.gn2'],
    'W07': ['W07fix/V-6.gn2', 'W07fix/V-6.canon.gn2'],
    'W08': sorted(os.path.relpath(p, T) for p in glob.glob(T + 'W08/hearts/*.gn2')),
}
HEAD = re.compile(r'^== (\S+).*?(\d+) errors, (\d+) warnings')


def run(args):
    p = subprocess.run([sys.executable, V, '--check-only', '--no-notes'] + args, capture_output=True, text=True)
    rounds, errs, warns, detail = 0, 0, 0, []
    for ln in p.stdout.splitlines():
        m = HEAD.match(ln)
        if m:
            rounds += 1
            errs += int(m.group(2))
            warns += int(m.group(3))
        elif ln.strip().startswith(('ERROR', 'WARN')) or ' ERROR ' in ln or ' WARN ' in ln:
            detail.append(ln.strip())
    return dict(rounds=rounds, errors=errs, warnings=warns, detail=detail, rc=p.returncode, stderr=p.stderr[-500:])


def main(argv):
    out = {}
    units = [a for a in argv if not a.startswith('-')] or sorted(os.path.basename(p)[:-3] for p in glob.glob(W12 + '/units/*.md'))
    tot = dict(md_rounds=0, md_err=0, md_warn=0, src_files=0, src_rounds=0, src_err=0, src_warn=0, blind_rounds=0, blind_err=0, blind_warn=0)
    for u in units:
        md = W12 + '/units/%s.md' % u
        r = run(['--md', md])
        src = [run([T + f]) for f in SOURCES.get(u, [])]
        bl = W12 + '/blind/%s_grain.gn2' % u
        b = run([bl]) if os.path.exists(bl) else None
        out[u] = dict(md=r, sources=dict(zip(SOURCES.get(u, []), src)), blind=b)
        tot['md_rounds'] += r['rounds']; tot['md_err'] += r['errors']; tot['md_warn'] += r['warnings']
        for s in src:
            tot['src_files'] += 1; tot['src_rounds'] += s['rounds']; tot['src_err'] += s['errors']; tot['src_warn'] += s['warnings']
        if b:
            tot['blind_rounds'] += b['rounds']; tot['blind_err'] += b['errors']; tot['blind_warn'] += b['warnings']
        print('%-4s md: %2d rounds, %d errors, %d warnings | sources %d files: %d rounds, %d/%d | blind: %s' % (
            u, r['rounds'], r['errors'], r['warnings'], len(src), sum(s['rounds'] for s in src),
            sum(s['errors'] for s in src), sum(s['warnings'] for s in src),
            ('%d rounds, %d/%d' % (b['rounds'], b['errors'], b['warnings'])) if b else '-'))
        if '-v' in argv:
            for d in r['detail'] + sum((s['detail'] for s in src), []) + (b['detail'] if b else []):
                print('      ', d[:220])
    if '--corpus' in argv:
        files = sorted(glob.glob(S + '/wf7/coverage/tests/*.gn2'))
        c = run(files)
        print('corpus (wf7/coverage/tests, %d files): %d rounds, %d errors, %d warnings' % (len(files), c['rounds'], c['errors'], c['warnings']))
        out['_corpus'] = c
        pil = glob.glob(S + '/wf7/pilot_IV4/*.gn2')
        if pil:
            c = run(pil)
            print('IV.4 pilot: %d rounds, %d errors, %d warnings' % (c['rounds'], c['errors'], c['warnings']))
            out['_pilot'] = c
    out['_total'] = tot
    print('TOTAL', tot)
    json.dump(out, open(os.path.join(HERE, 'grain_validation.json'), 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1:])
