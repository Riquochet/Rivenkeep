#!/usr/bin/env python3
"""(wf12 copy) Re-validate every wf12 unit's Orrowen against the merged lexicon (wf12/lexicon_orrowen_full.tsv).

The Orrowen of a unit is every blockquote line of its markdown outside code fences (the house style of both pilots:
each paragraph is given romanised in a blockquote, then the Book's English, then notes). Markdown emphasis, headings and
the inline-drawing marks (⟦…⟧) are stripped. A blockquote line in English (the pilots quote English verse in
blockquotes) is recognised by its English function words and set aside, and listed, so nothing is skipped silently.
Usage: validate_units.py [UNIT ...]   (default: every wf8/units/*.md; also the two pilots with --pilots)"""
import glob, json, os, re, sys
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
W = S + '/wf12'
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import orr_analyze as oa

LEX = oa.Lexicon(W + '/lexicon_orrowen_full.tsv')
EN = set("""gate lords flung apart broken grey sails shore stone stones the and of to in is was it that he she they we i his her their our for with as not but on at by from this be had
have were you my me all no what when who which there them him would could will an are its one said did do does has
into out up so if then than these those your us been more some any other only very just like after before""".split())
EN -= set(k.lower() for k in LEX.by_key)  # a word the tongue also has is no evidence of English


def strip_md(s):
    s = re.sub(r'⟦[^⟧]*⟧', ' ', s)
    s = re.sub(r'⟨[^⟩]*⟩', ' ', s)          # an editor's label on a drawn surface
    s = re.sub(r'\{[A-Z_]+\}', ' ', s)      # a builder's template token ({LAST_THRONE_AT_HAVEN})
    s = re.sub(r'`[^`]*`', ' ', s)
    s = re.sub(r'^#+\s*', '', s)
    s = s.replace('**', '').replace('*', '').replace('_', ' ')
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\[(\w)\]', ' ', s)
    return s.strip()


def is_english(s):
    toks = re.findall(r"[A-Za-z']+", s)
    if not toks:
        return False
    hits = sum(1 for t in toks if t.lower() in EN)
    return hits >= 2 and hits >= 0.2 * len(toks)


def orrowen_lines(path):
    out, eng = [], []
    fence = False
    for i, ln in enumerate(open(path, encoding='utf-8'), 1):
        if ln.startswith('```'):
            fence = not fence
            continue
        if fence or not ln.startswith('>'):
            continue
        t = strip_md(ln.lstrip('>').strip())
        if not t or not re.search(r'[A-Za-z]', t):
            continue
        if is_english(t):
            eng.append((i, t))
            continue
        out.append((i, t))
    return out, eng


# faults the canon keeps on purpose: the Last Carver's line (orrowen_v2 §11.9), whose article on a construct's head
# the analyzer must report ("it reports both of his tells, as it should")
EXPECTED = [re.compile(r'Ul et dumol ol varn')]


def check(path):
    lines, eng = orrowen_lines(path)
    words = bad = 0
    faults = []
    expected = []
    for i, t in lines:
        ws = oa.analyse_text(t, LEX)
        for w in ws:
            if w.kind == 'punct':
                continue
            words += 1
            if w.status != 'OK':
                if any(e.search(t) for e in EXPECTED):
                    expected.append(dict(line=i, tok=w.tok, status=w.status, text=t))
                    continue
                bad += 1
                faults.append(dict(line=i, tok=w.tok, status=w.status, msgs=w.msgs, sugg=w.sugg, text=t))
    return dict(unit=os.path.basename(path)[:-3], lines=len(lines), words=words, bad=bad, faults=faults, expected=expected,
                english_lines=[dict(line=i, text=t[:90]) for i, t in eng])


def main(argv):
    paths = []
    names = [a for a in argv if not a.startswith('-')]
    if names:
        paths = [W + '/units/%s.md' % n for n in names]
    else:
        paths = sorted(glob.glob(W + '/units/*.md'))
    if '--pilots' in argv:
        paths += [S + '/wf7/pilot_I1.md', S + '/wf7/pilot_IV4.md']
    res = [check(p) for p in paths]
    tot_w = sum(r['words'] for r in res)
    tot_b = sum(r['bad'] for r in res)
    for r in res:
        print('%-10s lines %4d  words %6d  reported %3d  (english blockquote lines set aside: %d)' % (
            r['unit'], r['lines'], r['words'], r['bad'], len(r['english_lines'])))
        if '-v' in argv:
            for f in r['faults']:
                print('    L%d %s %s %s %s' % (f['line'], f['tok'], f['status'], '; '.join(f['msgs']),
                                             ('suggest ' + ', '.join(f['sugg'])) if f['sugg'] else ''))
            for e in r['english_lines']:
                print('    [en] L%d %s' % (e['line'], e['text']))
    print('TOTAL words %d, reported %d' % (tot_w, tot_b))
    json.dump(res, open(os.path.join(HERE, 'orr_validation.json'), 'w'), indent=1, ensure_ascii=False)
    return 1 if tot_b else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
