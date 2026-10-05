#!/usr/bin/env python3
"""Secondary check: each unit's own declared analyzer input (its draft text, which also holds lines outside
blockquotes, e.g. S10's alternative token expansions and S11's table glosses), against the merged lexicon."""
import json, os, re, sys
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orr_analyze as oa
from validate_units import EXPECTED, strip_md
LEX = oa.Lexicon(S + '/wf8/lexicon_orrowen_full.tsv')
FILES = dict(S01='S01/draft.txt', S02='S02/draft/s02.txt', S03='S03/draft.txt', S04='S04/ii3_draft.txt S04/iv3_draft.txt',
             S05='S05/draft.txt', S06='S06/s06_text.txt', S07='S07/draft_lines.txt', S08='S08/draft.txt', S09='S09/draft.txt',
             S10='S10/all_orrowen.txt', S11='S11/s11_orrowen.txt', W01='W01/orr/frame.txt', W03='W03/headnote.txt',
             W04='W04/hn_check.txt', W05='W05/headnote.txt', W06='W06/headnote_plain.txt', W07='W07/hn_check.txt')
tot = bad = 0
out = {}
for u, fs in FILES.items():
    w = b = 0
    faults = []
    for f in fs.split():
        for ln in open(S + '/wf8/tmp/' + f, encoding='utf-8'):
            ln = ln.rstrip('\n')
            if not ln.strip():
                continue
            if '\t' in ln:
                ln = ln.split('\t', 1)[1]
            t = strip_md(ln)
            for wd in oa.analyse_text(t, LEX):
                if wd.kind == 'punct':
                    continue
                w += 1
                if wd.status != 'OK' and not any(e.search(t) for e in EXPECTED):
                    b += 1
                    faults.append('%s %s %s | %s' % (wd.tok, wd.status, '; '.join(wd.msgs), t[:100]))
    out[u] = dict(words=w, bad=b, faults=faults)
    tot += w; bad += b
    print('%-4s %-40s words %5d reported %d' % (u, fs, w, b))
    for f in faults[:8]:
        print('     ', f[:200])
print('TOTAL', tot, bad)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'draft_validation.json'), 'w'), indent=1)
