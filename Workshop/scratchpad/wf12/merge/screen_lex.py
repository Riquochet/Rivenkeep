#!/usr/bin/env python3
"""(wf12 copy of wf8/tmp/merge/screen_lex.py) Screen every wf12 addition in wf12/lexicon_orrowen_full.tsv (the rows after
O3015, and the base rows the merge touched) against: the analyzer (every word of the form parses, in context); the
tongue's phonology (orrowen_v2 §2.5: no z, x, q, j; no -ion, -iel, -dor); uniqueness (a new single word may not be an
existing form, nor read as na- + another word; a homophone of a mutated form is reported, not failed, lexicon §4.2);
and the roots (no root outside those the lexicon already uses, ancestor §1.5).  Jack's standing rule: no originality or
dictionary checks (overlap is just overlap), so the blacklist, common-English and dictionary screens are not run."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import orr_analyze as oa
FULL = os.path.join(W12, 'lexicon_orrowen_full.tsv')
lex = oa.Lexicon(FULL)
rows = lex.rows
dec = json.load(open(os.path.join(HERE, 'lex_decisions.json')))
new_ids = set(x['id'] for x in dec['new_rows'])
touched = set(d['base'] for d in dec['decisions'] if 'base' in d)
base_rows = [r for r in rows if r['id'] not in new_ids]
base_forms = set(oa.nk(r['orrowen']) for r in base_rows if ' ' not in r['orrowen'])
base_roots = set(x.strip() for r in base_rows for x in re.split(r',\s*', r['root']) if x.strip())
report, fail = [], 0
for r in rows:
    if r['id'] not in new_ids and r['id'] not in touched:
        continue
    form = r['orrowen']
    probs, notes = [], []
    for w in oa.analyse_text(form, lex):
        if w.kind == 'punct':
            continue
        if w.status != 'OK':
            probs.append('analyzer: %s %s %s' % (w.tok, w.status, '; '.join(w.msgs)))
    for w in re.findall(r"[A-Za-z']+", form):
        lw = w.lower()
        if re.search(r'[zxqj]', lw):
            probs.append('banned letter in %s (§2.5)' % w)
        if re.search(r'(ion|iel|dor)$', lw):
            probs.append('banned ending in %s (§2.5)' % w)
    if ' ' not in form and r['id'] in new_ids and r['pos'] not in ('name', 'loan'):
        if oa.nk(form) in base_forms:
            probs.append('collides with an existing form')
        if form.lower().startswith('na') and oa.nk(form[2:]) in base_forms:
            probs.append('reads as na- + %s' % form[2:])
        for b in base_rows:
            bf = b['orrowen']
            if ' ' in bf or bf.startswith('-'):
                continue
            if oa.nk(oa.soften(bf)) == oa.nk(form) or oa.nk(oa.nasalise(bf)) == oa.nk(form):
                notes.append('sounds like a mutated %s (%s): homophony, settled by context' % (bf, b['id']))
    for x in re.split(r',\s*', r['root']):
        x = x.strip()
        if x and x not in base_roots and not x.startswith('('):
            probs.append('root %s not among the lexicon roots' % x)
    if probs:
        fail += 1
    report.append(dict(id=r['id'], form=form, problems=probs, notes=notes))
json.dump(report, open(os.path.join(HERE, 'screen_report.json'), 'w'), indent=1, ensure_ascii=False)
print('screened %d rows (%d new, %d touched base rows); %d with a problem' % (len(report), len(new_ids), len(touched), fail))
for x in report:
    if x['problems'] or x['notes']:
        print(x['id'], x['form'], '|', '; '.join(x['problems']), '|', '; '.join(x['notes']))
