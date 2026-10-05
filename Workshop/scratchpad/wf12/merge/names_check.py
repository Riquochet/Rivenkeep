#!/usr/bin/env python3
"""Names across units: every capitalised word of every unit's Orrowen (sentence-initial words aside), grouped by the
lexicon row it parses to, with its surface spellings (mutation shown) and the units that use each."""
import collections, glob, os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orr_analyze as oa
from validate_units import orrowen_lines, LEX
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
files = sorted(glob.glob(S + '/wf12/units/*.md'))
by_row = collections.defaultdict(lambda: collections.defaultdict(set))
lower_of_names = collections.defaultdict(lambda: collections.defaultdict(set))
for f in files:
    u = os.path.basename(f)[:-3]
    for ln, t in orrowen_lines(f)[0]:
        if t.isupper():
            continue
        ws = oa.analyse_text(t, LEX)
        prev = '.'
        for w in ws:
            if w.kind == 'punct':
                prev = w.tok
                continue
            row = w.best.row if (w.best is not None and w.best.row is not None) else None
            rid = (row['id'], row['orrowen'], row['pos']) if row else ('?', w.tok, '?')
            initial = prev in ('.', '!', '?', ':', ';') or prev == '.'
            if w.tok[0].isupper() and not initial:
                by_row[rid][w.tok].add(u)
            elif row and 'name' in (row['pos'] or '') and w.tok[0].islower():
                lower_of_names[rid][w.tok].add(u)
            prev = w.tok
out = []
for rid, forms in sorted(by_row.items(), key=lambda x: x[0][1].lower()):
    out.append((rid, {k: sorted(v) for k, v in forms.items()}))
for rid, forms in out:
    print('%s %-18s [%s]  ' % (rid[0], rid[1], rid[2]) + '; '.join('%s (%s)' % (k, ','.join(v)) for k, v in forms.items()))
print('\n# names written lower-case somewhere:')
for rid, forms in lower_of_names.items():
    print('%s %-18s ' % (rid[0], rid[1]) + '; '.join('%s (%s)' % (k, ','.join(sorted(v))) for k, v in forms.items()))
