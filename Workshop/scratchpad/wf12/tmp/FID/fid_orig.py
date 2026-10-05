#!/usr/bin/env python3
"""fid_orig.py (wf12 fidelity, scratch): the Original pane, block by block, against the Book and the units.

  A. every Book paragraph of every leaf (data-k in its The Book pane) has its Original block (same data-k), and every
     Original block's data-k is a Book paragraph's first line; the blocks run in the Book's order
  B. each panes.json block's own copy of the Book text ('book') is the Book's paragraph at its line, exactly
  C. each block's unit item (src = UNIT:line): the unit's Orrowen there, followed by English that is the Book's
     paragraph exactly (the pairing the merge made, re-read from the unit file itself)
  D. the romanisation the page's fold gives is the unit's Orrowen (markdown and markers aside)
"""
import collections
import html
import json
import os
import re
import sys

sys.argv = sys.argv[:1]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fid_text as F  # noqa: E402

S = F.S
W12 = os.path.join(S, 'wf12')
PANES = json.load(open(os.path.join(W12, 'orig', 'panes.json'), encoding='utf-8'))
BOOKL = open(F.SRC['book'], encoding='utf-8').read().split('\n')
UNITS = {}


def unit(name):
    if name not in UNITS:
        UNITS[name] = open(os.path.join(W12, 'units', name + '.md'), encoding='utf-8').read().split('\n')
    return UNITS[name]


def unq(l):
    return re.sub(r'^>\s?', '', re.sub(r'^>\s?', '', l))


def book_para(line, end):
    t = F.squash(' '.join(unq(x).rstrip() for x in BOOKL[line - 1:end]))
    return re.sub(r'^#{1,6} ', '', t)


def norm(t):
    t = re.sub(r'<!--.*?-->', '', t)
    return F.squash(t.replace('  \n', '\n'))


def unit_item(src):
    """(orrowen lines, english lines) of the unit item that begins at src"""
    u, ln = src.split(':')
    if not ln.isdigit():
        return None, None
    ls = unit(u)
    i = int(ln) - 1
    orr = []
    if ls[i].startswith('```'):
        j = i + 1
        while not ls[j].startswith('```'):
            orr.append(ls[j])
            j += 1
        j += 1
    elif ls[i].startswith('>'):
        j = i
        while j < len(ls) and ls[j].startswith('>'):
            orr.append(unq(ls[j]))
            j += 1
    else:
        return [ls[i]], None
    while j < len(ls) and not ls[j].strip():
        j += 1
    eng = []
    while j < len(ls) and ls[j].strip():
        eng.append(ls[j])
        j += 1
    return orr, eng


def main():
    h = open(F.PAGE, encoding='utf-8').read()
    leaves, order = F.page_leaves(h)
    R = collections.OrderedDict()
    probs = []
    nA = nB = nC = nD = 0
    for lid in order:
        bk = F.pane(leaves[lid], 'book')
        og = F.pane(leaves[lid], 'orig')
        bks = re.findall(r'\bdata-k="b(\d+)"', bk)
        ogs = re.findall(r'<[a-z]+\b[^>]*\bdata-k="b(\d+)"', og)
        blocks = PANES[lid]
        want = [str(b['line']) for b in blocks]
        if ogs != want:
            probs.append((lid, 'A', 'page Original data-k order differs from panes.json'))
        miss = [k for k in dict.fromkeys(bks) if k not in set(ogs)]
        extra = [k for k in ogs if k not in set(bks)]
        if miss:
            probs.append((lid, 'A', 'Book paragraphs with no Original block: %s' % miss))
        # the Original's blocks in Book order
        if [int(x) for x in ogs] != sorted(int(x) for x in ogs):
            probs.append((lid, 'A', 'Original blocks out of Book order'))
        nA += 1
        R[lid] = {'book_keys': len(set(bks)), 'orig_blocks': len(ogs), 'orig_only_keys': extra}
        for b in blocks:
            # B
            bp = book_para(b['line'], b.get('end_line') or b['line'])
            mine = norm(re.sub(r'^\s*>\s?', '', b['book'], flags=re.M))
            if b['kind'] in ('native', 'note', 'table-head', 'table-row'):
                mine2 = F.squash(re.sub(r'^>\s?', '', b['book'], flags=re.M))
                ok = mine2.replace(' ', '') == bp.replace(' ', '') or mine2 in bp or bp in mine2
            else:
                ok = mine == bp
            if not ok:
                probs.append((lid, 'B', 'line %d: panes.book %r != Book %r' % (b['line'], mine[:90], bp[:90])))
            else:
                nB += 1
            # C
            src = b.get('src')
            if not src or ':' not in src or not src.split(':')[1].isdigit():
                continue
            orr, eng = unit_item(src)
            if eng is None:
                if b['kind'] not in ('native', 'note'):
                    probs.append((lid, 'C', 'line %d: src %s is not an Orrowen item: %r' % (b['line'], src, orr[0][:80])))
                continue
            e = F.squash(' '.join(unq(x).rstrip() for x in eng))
            e = re.sub(r'^#{1,6} ', '', e)
            if e.startswith('**') and e.endswith('**') and b['kind'] in ('book-head', 'title'):
                e = e[2:-2]
            if b['kind'] in ('native', 'note', 'title', 'table-row', 'table-head'):
                ok = True     # captions and heads: their English is set otherwise in the unit
            else:
                ok = e == bp
            if not ok:
                probs.append((lid, 'C', 'line %d (%s, %s): unit English %r != Book %r' % (b['line'], b['kind'], src, e[:100], bp[:100])))
            else:
                nC += 1
            # D: the fold's romanisation vs the unit's Orrowen (blockquote items only)
            if b['kind'] in ('ring', 'seal', 'ring-cont', 'native', 'note', 'cited', 'carving', 'table-row', 'table-head'):
                continue
            m = re.search(r'<details class="tr rom">.*?<div class="tr-body">(.*?)</div></details>', b['html'], flags=re.S)
            if not m:
                continue
            fold = html.unescape(re.sub(r'<[^>]+>', '', m.group(1).replace('</p><p>', ' ')))
            uo = ' '.join(orr)
            uo = re.sub(r'<!--.*?-->', '', uo)
            uo = re.sub(r'^#+\s*', '', uo).replace('**', '').replace('*', '')
            uo = re.sub(r'⟦[a-z0-9_]+⟧', '', uo)
            uo = re.sub(r'\{\{([A-Za-z]+)\}\}', r'\1', uo)
            a1 = re.sub(r'[\s\[\]]+', ' ', F.squash(uo)).strip()
            b1 = re.sub(r'[\s\[\]]+', ' ', F.squash(fold)).strip()
            if a1 != b1:
                probs.append((lid, 'D', 'line %d (%s): fold %r != unit %r' % (b['line'], src, b1[:100], a1[:100])))
            else:
                nD += 1
    print('A leaves', nA, '; B blocks ok', nB, '; C items ok', nC, '; D folds ok', nD)
    byk = collections.Counter(p[1] for p in probs)
    print('problems', dict(byk))
    for p in probs[:80]:
        print('  ', p)
    json.dump({'leaves': R, 'problems': probs}, open(os.path.join(HERE, 'fid_orig.json'), 'w'), indent=1, ensure_ascii=False)


main()
