#!/usr/bin/env python3
"""wf12 merge: the Book v3.0.0 paragraph by paragraph against its owner unit, in order.  Each leaf (or Book heading) has
one owner unit; the owner's items are walked in order and each Book paragraph takes the next item whose English is that
paragraph exactly (headings may be bold).  Reports: missing (no item), and, across ALL units, any other item whose
English is a Book paragraph of a leaf it does not own (a double).  Native-block captions and bodies are the reader's
furniture (the old units' practice) and are reported apart."""
import bisect, collections, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import coverage as C

OWN = [(85, 'S01'), (156, 'S01'), (181, 'S11'), (185, 'S01'), (289, 'S02'), (395, 'S02'), (477, 'S03'), (611, 'S03'),
       (699, 'S11'), (703, 'S04'), (769, 'W01'), (846, 'S04'), (920, 'S11'), (924, 'S05'), (1006, 'S05'),
       (1112, 'S11'), (1116, 'S06'), (1206, 'W02'), (1286, 'S06'), (1418, 'W03'), (1494, 'S07'), (1586, 'W04'),
       (1659, 'S11'), (1663, 'S07'), (1734, 'S08'), (1814, 'W05'), (1879, 'W06'), (1954, 'S08'), (2108, 'W07'),
       (2188, 'S09'), (2362, 'S11'), (2366, 'S09'), (2500, 'W08'), (2578, 'S10'), (2724, 'S11'), (2728, 'S10'),
       (2831, 'S11')]
START = {'S11': 355}     # S11's Contents (§2) stand before OF THIS BOOK; its body headings begin at §3
FURN = ('native-cap', 'native-body')


def owner(line):
    i = bisect.bisect_right([a for a, _ in OWN], line) - 1
    return OWN[i][1]


def main(argv):
    bp = C.book_paras()
    ue = C.unit_english()
    byu = collections.defaultdict(list)
    for x in ue:
        byu[x['unit']].append(x)
    for u in byu:
        byu[u].sort(key=lambda x: x['line'])
    ptr = collections.defaultdict(int)
    used = set()
    res = []
    for p in bp:
        u = owner(p['line'])
        its = byu[u]
        j = ptr[u]
        while j < len(its) and its[j]['line'] < START.get(u, 0):
            j += 1
        key = C.norm(p['text'])
        keyh = C.norm_head(p['text'])
        hit = None
        for k in range(j, len(its)):
            e = its[k]['eng']
            if (C.norm(e) == key) or (p['kind'] == 'head' and C.norm_head(e) == keyh):
                hit = k
                break
        ooo = False
        if hit is None:          # out of the unit's order (a wood leaf's close set with its frame): any unused item
            for k in range(0, len(its)):
                if (u, its[k]['line'], its[k].get('nth', 0)) in used or its[k]['line'] < START.get(u, 0):
                    continue
                e = its[k]['eng']
                if (C.norm(e) == key) or (p['kind'] == 'head' and C.norm_head(e) == keyh):
                    hit, ooo = k, True
                    break
        if hit is not None:
            if not ooo:
                ptr[u] = hit + 1
            used.add((u, its[hit]['line'], its[hit].get('nth', 0)))
            used.add((u, its[hit]['line']))
            res.append(dict(p, owner=u, hit=(u, its[hit]['line'], its[hit]['kind']), out_of_order=ooo))
        else:
            res.append(dict(p, owner=u, hit=None))
    # the Book of Knowings' table is set out by S11 root by root (the builder's knowings_roots reads it so): its head row
    # is S11's table head (Orrowen over English), each root row a '#### n · ' section whose blockquote is the root and its
    # look, over the row's first two cells
    s11 = open(os.path.join(C.W12, 'units', 'S11.md'), encoding='utf-8').read()
    for r in res:
        if r['kind'] != 'table' or r['hit'] is not None:
            continue
        cells = [x.strip() for x in r['text'].strip('|').split('|')]
        if cells[0] == 'The root, as I name it':
            ok = ('| *Et meskrivull' in s11) and (r['text'] in s11)
        else:
            ok = ('\n%s · %s\n' % (cells[0], cells[1])) in s11
        if ok:
            r['hit'] = ('S11', 0, 'table')
            r['note'] = 'set out root by root (S11 §4, the table)'
    # doubles: an item, not used, whose English is a Book paragraph (in the range), in any unit
    book_keys = collections.defaultdict(list)
    for r in res:
        book_keys[C.norm(r['text'])].append(r)
        if r['kind'] == 'head':
            book_keys[C.norm_head(r['text'])].append(r)
    doubles = []
    for x in ue:
        if (x['unit'], x['line'], x.get('nth', 0)) in used:
            continue
        k1, k2 = C.norm(x['eng']), C.norm_head(x['eng'])
        if k1 in book_keys or k2 in book_keys:
            if x['unit'] == 'S11' and x['line'] < START['S11']:
                continue            # the Contents, before OF THIS BOOK
            doubles.append(x)
    json.dump(dict(paras=res, doubles=doubles), open(os.path.join(HERE, 'coverage2.json'), 'w'), indent=1, ensure_ascii=False)
    cnt = collections.Counter((r['kind'] in FURN and 'furniture' or 'text', r['hit'] is not None) for r in res)
    print('Book paragraphs from OF THIS BOOK: %d (%d text, %d native furniture)' % (
        len(res), sum(1 for r in res if r['kind'] not in FURN), sum(1 for r in res if r['kind'] in FURN)))
    print('text paragraphs matched %d, missing %d; furniture matched %d, not given %d' % (
        cnt[('text', True)], cnt[('text', False)], cnt[('furniture', True)], cnt[('furniture', False)]))
    print('doubles (an unused item whose English is a Book paragraph): %d' % len(doubles))
    if '-q' in argv:
        return
    for r in res:
        if r['hit'] is None and (r['kind'] not in FURN or '-f' in argv):
            print('MISSING %-11s L%-5d %s %s | %s' % (r['kind'], r['line'], r['owner'], (r['leaf'] or '')[:14], r['text'][:120].replace('\n', ' / ')))
    for x in doubles:
        print('DOUBLE  %s L%d (%s) | %s' % (x['unit'], x['line'], x['kind'], x['eng'][:100].replace('\n', ' / ')))


if __name__ == '__main__':
    main(sys.argv[1:])
