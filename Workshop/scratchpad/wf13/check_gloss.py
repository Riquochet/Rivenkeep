"""check_gloss.py (wf13) -- every romanised line on the page has a complete, readable word-by-word English gloss.

    python3 check_gloss.py [UNIT ...]     (default: every gloss_in/<UNIT>.json)

For each line of gloss_in/<UNIT>.json, gloss/<UNIT>.json must hold a row with the identical 'rom' string, whose 'gloss'
is a list of [word, english] pairs with exactly the analyzer's words in order (the 'draft' words), and every english
gloss readable: not empty, not '?', and free of the analyzer's raw tags (PST, REL, NEG, -1SG, (+N), N·, S·, -PL ...)."""
import json, re, sys, os, glob
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
RAW = re.compile(r'\((\+[NS])\)|\b(PST|PRS|FUT|REL|NEG|IMP|SG|PL|DU|1SG|2SG|3SG|1PL|2PL|3PL|GEN|DAT|ACC|NOM|M|F)\b|[NS]·|-\d?(SG|PL)\b|\bPL\b')
units = sys.argv[1:] or sorted(os.path.basename(p)[:-5] for p in glob.glob(S + '/gloss_in/*.json'))
total = bad_all = 0
for u in units:
    need = json.load(open('%s/gloss_in/%s.json' % (S, u)))
    path = '%s/gloss/%s.json' % (S, u)
    if not os.path.exists(path):
        print('%-5s MISSING %s' % (u, path)); bad_all += len(need); continue
    have = {}
    for r in json.load(open(path)):
        have.setdefault(r['rom'], r)
    bad = []
    for r in need:
        g = have.get(r['rom'])
        words = [w for w, _ in r['draft']]
        if not g:
            bad.append(('no row', r['rom'][:60])); continue
        gw = [w for w, _ in g['gloss']]
        if gw != words:
            bad.append(('words differ', r['rom'][:60], len(gw), len(words))); continue
        for w, e in g['gloss']:
            if not e or not e.strip() or e.strip() == '?' or RAW.search(e):
                bad.append(('gloss', w, e))
    total += len(need); bad_all += len(bad)
    print('%-5s lines %4d  problems %d' % (u, len(need), len(bad)))
    for b in bad[:8]:
        print('      ', b)
print('ALL: %d lines, %d problems' % (total, bad_all))
sys.exit(1 if bad_all else 0)
