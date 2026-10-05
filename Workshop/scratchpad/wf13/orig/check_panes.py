#!/usr/bin/env python3
"""check_panes.py (wf13 scratch, v3.1.0) -- panes.json against the Book v3.0.0 and the merge: every Book paragraph has
exactly one block, in order, with the Book's text and the unit item the merge paired it with; every drawing slot resolves
to a drawing rendered in make_grain3.py's last run; the HTML of every block balances; Halyna's inks are the Book's; and
(v3.1.0) every romanised line of every romanisation fold is set word over word, glossed from wf13/gloss.
Writes panes_check.json; prints a summary (exit 1 on any failure)."""
import collections
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import build_panes as BPX  # noqa: E402  (its Book cut, its pairing, the fresh keys; nothing is built on import)

VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'wbr', 'source'}


class Bal(HTMLParser):
    def __init__(self):
        super().__init__()
        self.st, self.err = [], []

    def handle_starttag(self, t, a):
        if t not in VOID:
            self.st.append(t)

    def handle_endtag(self, t):
        if t in VOID:
            return
        if not self.st or self.st[-1] != t:
            self.err.append(t)
        else:
            self.st.pop()


def main():
    panes = json.load(open(os.path.join(HERE, 'panes.json'), encoding='utf-8'))
    fails = []
    res = collections.OrderedDict()
    # 1. the Book cut, leaf by leaf
    lv = BPX.leaves()
    if list(lv) != list(panes):
        fails.append('anchors differ: %s' % (set(lv) ^ set(panes)))
    nb = 0
    for a, paras in lv.items():
        bl = panes.get(a, [])
        if [p['line'] for p in paras] != [b['line'] for b in bl]:
            fails.append('%s: block lines differ from the Book cut' % a)
        if [b['para_index'] for b in bl] != list(range(len(bl))):
            fails.append('%s: para_index not 0..n-1' % a)
        for p, b in zip(paras, bl):
            if p['text'] != b['book']:
                fails.append('%s L%d: book text differs' % (a, p['line']))
        nb += len(bl)
    res['leaves'] = len(panes)
    res['blocks'] = nb
    allb = [b for bl in panes.values() for b in bl]
    res['missing'] = [(b['line'], b['book'][:60]) for b in allb if b['kind'] == 'missing']
    if res['missing']:
        fails.append('%d blocks without Orrowen' % len(res['missing']))
    # 2. the merge's pairing (coverage2.json): every matched Book paragraph from OF THIS BOOK on is set from its item
    cov = json.load(open(os.path.join(BPX.MERGE, 'coverage2.json'), encoding='utf-8'))
    byline = {b['line']: b for b in allb}
    cnt = collections.Counter()
    for r in cov['paras']:
        k = r['kind']
        if k in ('native-cap', 'native-body'):
            cnt['furniture'] += 1
            continue
        cnt['text'] += 1
        b = byline.get(r['line'])
        if b is None:
            fails.append('coverage L%d: no block' % r['line'])
            continue
        if r['hit'] is None:
            fails.append('coverage L%d: the merge had no item' % r['line'])
            continue
        u, ln, kind = r['hit']
        if u == 'S11' and kind == 'table':
            ok = b['kind'] in ('table-head', 'table-row')
        else:
            ok = b.get('src') in ('%s:%d' % (u, ln),) or (b['kind'] in ('carving',) and b.get('src', '').startswith(u))
        cnt['same item' if ok else 'other item'] += 1
        if not ok:
            fails.append('coverage L%d: block src %s, merge item %s:%d' % (r['line'], b.get('src'), u, ln))
    res['coverage2'] = dict(cnt)
    # 3. the drawings
    slots = []
    for b in allb:
        for m in re.finditer(r'data-(svg3|native)="([^"]+)"', b['html']):
            slots.append((m.group(1), m.group(2)))
    bad = []
    for kind, key in slots:
        if kind == 'svg3':
            if not os.path.exists(os.path.join(BPX.SVG3, key + '.svg')) or (key not in BPX.FRESH and key not in BPX.EXTRA_SVG3):
                bad.append(key)
        elif not os.path.exists(os.path.join(BPX.NATIVE_DIR, key + '.svg')):
            bad.append('native:' + key)
    if bad:
        fails.append('slots that do not resolve: %s' % bad)
    s3 = [k for t, k in slots if t == 'svg3']
    res['slots'] = {'svg3': len(s3), 'svg3 distinct': len(set(s3)), 'native': len([1 for t, _ in slots if t == 'native'])}
    res['svg3_bytes'] = sum(os.path.getsize(os.path.join(BPX.SVG3, k + '.svg')) for k in set(s3))
    # every render of the last make_grain3 run, set or not
    jobs = [ln.split()[0] for ln in open(os.path.join(HERE, 'make_grain3.log'), encoding='utf-8') if ln.strip()]
    res['renders'] = {'jobs': len(jobs), 'failed': sorted(BPX.FAILED), 'set': len([k for k in set(s3) if k in jobs]),
                      'not set': sorted(k for k in jobs if k not in set(s3) and k not in BPX.FAILED)}
    # 4. the HTML
    unb = []
    for b in allb:
        p = Bal()
        p.feed(b['html'])
        p.close()
        if p.err or p.st:
            unb.append(b['line'])
    if unb:
        fails.append('unbalanced HTML at %s' % unb[:10])
    res['unbalanced'] = unb
    # 5. Halyna's inks: the Book's rule (halyna_check.book_blocks)
    vc = collections.Counter()
    for b in allb:
        want = BPX.VOICE.get(b['line'])
        if want in ('a', 'b'):
            vc['ok' if b.get('voice') == want else 'wrong'] += 1
            if b.get('voice') != want:
                fails.append('L%d: ink %s, the Book %s' % (b['line'], b.get('voice'), want))
        elif b.get('voice'):
            vc['voice outside a block'] += 1
            fails.append('L%d: an ink outside a HALYNA block or a reading' % b['line'])
    res['inks'] = dict(vc)
    # 6. the wood: every ring of every round set once, by leaf
    wood = {}
    for a, bl in panes.items():
        rk = [b['svg3'] for b in bl if b['kind'] == 'ring']
        if rk:
            dup = [k for k, n in collections.Counter(rk).items() if n > 1]
            if dup:
                fails.append('%s: a plate set twice: %s' % (a, dup))
            wood[a] = {'rings': len(rk), 'ring-cont': sum(1 for b in bl if b['kind'] == 'ring-cont'),
                       'cited': [b['svg3'] for b in bl if b['kind'] == 'cited'],
                       'whole': [b['svg3'] for b in bl if b['kind'] == 'seal'], 'readings': sum(1 for b in bl if b['kind'] == 'reading')}
    res['wood'] = wood
    res['kinds'] = dict(collections.Counter(b['kind'] for b in allb))
    res['natives'] = [{'line': b['line'], 'nid': b.get('nid'), 'kind': b['kind'], 'drawn': ('svg-slot' in b['html']),
                       'caption': 'Orrowen' if re.search(r'<figcaption><div class="ip">|class="native-note', b['html']) else 'English',
                       'owed': bool(b.get('owed'))} for b in allb if b['kind'] in ('native', 'note')]
    # 7. the interlinear (v3.1.0): every line of every romanisation fold set word over word, each word (its punctuation
    #    kept with it) over the English that wf13/gloss gives that line (keyed by the line as the fold shows it), the
    #    words in the gloss's order, every gloss readable, and once more as the visually hidden list after the line; no
    #    letter of the line outside a word box; the fold's summary still 'Romanisation ...'; and every line
    #    wf13/gloss_in asks for (wf13/extract_rom.py's harvest of the v3.0.0 folds) is on the page, glossed
    il_need = set()
    gin = os.path.join(os.path.dirname(HERE), 'gloss_in')
    for f in sorted(os.listdir(gin)):
        if f.endswith('.json'):
            il_need.update(r['rom'] for r in json.load(open(os.path.join(gin, f), encoding='utf-8')))
    RAW = re.compile(r'\((\+[NS])\)|\b(PST|PRS|FUT|REL|NEG|IMP|SG|PL|DU|1SG|2SG|3SG|1PL|2PL|3PL|GEN|DAT|ACC|NOM)\b|[NS]·')
    il = collections.Counter()
    il_seen = set()
    il_fail = []
    for b in allb:
        for m in re.finditer(r'<details class="tr rom"><summary>(.*?)</summary><div class="tr-body">(.*?)</div></details>', b['html'], re.S):
            if not m.group(1).startswith('Romanisation'):
                il_fail.append('L%d: a romanisation fold labelled %r' % (b['line'], m.group(1)[:40]))
            for p in re.findall(r'<p\b[^>]*>.*?</p>', m.group(2), re.S):
                mm = re.fullmatch(r'<p class="il">(.*)</p>', p, re.S)
                if not mm:
                    il_fail.append('L%d: a romanised line not set word over word: %r' % (b['line'], p[:60]))
                    continue
                inner = mm.group(1)
                srm = re.search(r' <span class="sr">Word by word: (.*)\.</span>$', inner)
                line = re.sub(r' <span class="sr">.*</span>$', '', inner)
                ws = re.findall(r'<i>(.*?)<small aria-hidden="true">(.*?)</small></i>', line)
                text = BPX.html_text(re.sub(r'<small aria-hidden="true">.*?</small>', '', line)).strip()
                outside = BPX.html_text(re.sub(r'<i\b[^>]*>.*?</i>', ' ', line))
                if BPX.WORD_CH.search(outside):
                    il_fail.append('L%d: letters outside the word boxes: %r' % (b['line'], outside[:60]))
                # (wf13 reader check) the warden's blotted name in a word's box, glossed '(name blotted out)'; every
                # other mark between the words in a span.m
                for bw, bg in re.findall(r'<i class="blot">(.*?)<small aria-hidden="true">(.*?)</small></i>', line):
                    il['blotted names boxed'] += 1
                    if BPX.BLOT_CH not in bw or BPX.html_text(bg) != BPX.BLOT_GLOSS:
                        il_fail.append('L%d: a blotted name boxed wrongly: %r' % (b['line'], bw + ' / ' + bg))
                if BPX.BLOT_CH in BPX.html_text(re.sub(r'<i class="blot">.*?</i>', ' ', line)):
                    il_fail.append('L%d: a blotted name outside its box: %r' % (b['line'], text[:60]))
                il['marks between the words'] += len(re.findall(r'<span class="m">', line))
                if not ws:
                    il['lines without a word'] += 1
                    continue
                g = BPX.GLOSS.get(text)
                if g is None:
                    il_fail.append('L%d: no gloss for %r' % (b['line'], text[:60]))
                    continue
                if [BPX.word_core(BPX.html_text(w)) for w, _ in ws] != [w for w, _ in g]:
                    il_fail.append('L%d: the words differ from the gloss: %r' % (b['line'], text[:60]))
                if [BPX.html_text(e) for _, e in ws] != [e for _, e in g]:
                    il_fail.append('L%d: the glosses differ from wf13/gloss: %r' % (b['line'], text[:60]))
                gi = iter(e for _, e in g)
                said = [BPX.BLOT_SAID if bm.group(1) else next(gi, '?') for bm in re.finditer(r'<i( class="blot")?>', line)]
                if not srm or BPX.html_text(srm.group(1)) != ', '.join(said):
                    il_fail.append('L%d: the hidden word-by-word list differs: %r' % (b['line'], text[:60]))
                bad_g = [e for _, e in g if not e.strip() or e.strip() == '?' or RAW.search(e)]
                if bad_g:
                    il_fail.append('L%d: unreadable glosses %s' % (b['line'], bad_g[:4]))
                il['lines'] += 1
                il['words'] += len(ws)
                il_seen.add(text)
    miss = sorted(il_need - il_seen)
    if miss:
        il_fail.append('%d romanised lines of gloss_in not on the page glossed: %s' % (len(miss), [x[:40] for x in miss[:4]]))
    fails.extend(il_fail)
    res['interlinear'] = dict(il, distinct_lines=len(il_seen), gloss_in_lines=len(il_need), gloss_in_missing=len(miss),
                              problems=len(il_fail))
    res['fails'] = fails
    json.dump(res, open(os.path.join(HERE, 'panes_check.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k not in ('natives', 'wood')}, ensure_ascii=False, indent=1)[:4000])
    print('FAILS:', len(fails))
    for f in fails[:30]:
        print('  ', f)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
