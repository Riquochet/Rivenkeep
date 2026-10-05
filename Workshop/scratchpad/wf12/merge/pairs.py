#!/usr/bin/env python3
"""wf12 merge: every unit's items in the house style -- a blockquote (romanised Orrowen) or a code block (a ring),
paired with the Book's English that follows it.  Writes pairs.json; `pairs.py grep REGEX` searches the Orrowen,
`pairs.py en PHRASE` the English (both case-insensitive)."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
UNITS = sorted(glob.glob(os.path.join(W12, 'units', '*.md')))
LABEL = re.compile(r'^\*\((first|second|seren|the other|one)[^)]*\)\*$|^\*\*¶\s*\d+[^*]*\*\*(\s*\*\([^)]*\)\*)?$|^\*\*(Rhyna|Halvard)\.\*\*$', re.I)
STOP = ('Word for word', '(Word for word', '- ', '* ', '|', '#', '```', 'Literal', '**Ring', '---', '**Reads', '*Word for word')


def blocks(path):
    """the md as a stream of (kind, text, line): bq, code, head, text"""
    L = open(path, encoding='utf-8').read().split('\n')
    out, i = [], 0
    while i < len(L):
        ln = L[i]
        if ln.startswith('```'):
            j = i + 1
            while j < len(L) and not L[j].startswith('```'):
                j += 1
            out.append(('code', '\n'.join(L[i + 1:j]), i + 1))
            i = j + 1
            continue
        if ln.startswith('>'):
            j = i
            cur, start = [], i
            while j < len(L) and L[j].startswith('>'):
                t = L[j][1:].strip()
                if not t:
                    if cur:
                        out.append(('bq', '\n'.join(cur), start + 1))
                    cur = []
                    start = j + 1
                else:
                    cur.append(L[j][1:].lstrip(' ') if L[j].startswith('> ') else L[j][1:])
                j += 1
            if cur:
                out.append(('bq', '\n'.join(cur), start + 1))
            i = j
            continue
        if ln.startswith('#'):
            out.append(('head', ln, i + 1))
            i += 1
            continue
        if not ln.strip():
            i += 1
            continue
        j, buf = i, []
        while j < len(L) and L[j].strip() and not L[j].startswith(('>', '#', '```')):
            buf.append(L[j])
            j += 1
        out.append(('text', '\n'.join(buf), i + 1))
        i = j
    return out


if __name__ == '__main__':
    pass


EN_WORDS = set('''the and of to in is was it that he she they we i his her their our for with as not but on at by from this be had
have were you my me all no what when who which there them him would could will an are its one said did do does has
into out up so if then than these those your us been more some any other only very just like after before ye thee thou hath
naught ere wist'''.split())


def is_english(t):
    toks = re.findall(r"[A-Za-z']+", re.sub(r'\{\{[^}]*\}\}', ' ', t))
    if not toks:
        return False
    hits = sum(1 for x in toks if x.lower() in EN_WORDS)
    return hits >= 2 and hits >= 0.2 * len(toks)


def is_label(t):
    t = t.strip()
    return len(t) < 200 and bool(LABEL.match(t) or re.match(r'^\*\((first|second)[^)]*\)\*', t, re.I)
                                 or re.match(r'^\((first|second|the other|one) ink[^)]*\)$', t, re.I))


def items(path):
    """[{'kind': 'bq'|'ring', 'orr': text, 'eng': text, 'engs': [text, ...], 'line': n, 'eline': n}] : an Orrowen
    blockquote (or a ring's code block) and the English paragraphs after it (labels skipped; the first is 'eng')."""
    B = blocks(path)
    out = []
    for i, (k, v, ln) in enumerate(B):
        if k == 'bq' and not is_english(v):
            kind = 'bq'
        elif k == 'code' and (re.search(r'^\s*r\d+[·/]\d+\s', v, re.M) or re.search(r'^\s*bark\b', v, re.M)):
            kind = 'ring'
        else:
            continue
        j = i + 1
        while j < len(B) and B[j][0] == 'text' and is_label(B[j][1]):
            j += 1
        engs, elines = [], []
        while j < len(B):
            k2, v2, ln2 = B[j]
            if k2 == 'bq' and is_english(v2):
                engs.append(v2); elines.append(ln2); j += 1; continue
            if k2 == 'head' and not engs:
                engs.append(v2); elines.append(ln2); j += 1; break
            if k2 == 'text' and not is_label(v2):
                if v2.lstrip().startswith(STOP) and not (v2.lstrip().startswith('**') and not v2.lstrip().startswith('**Reads')):
                    break
                engs.append(v2); elines.append(ln2); j += 1; continue
            break
        out.append(dict(kind=kind, orr=v, eng=engs[0] if engs else '', engs=engs, line=ln, eline=elines[0] if elines else 0))
    return out


def all_items():
    res = {}
    for p in UNITS:
        res[os.path.basename(p)[:-3]] = items(p)
    return res


def main(argv):
    res = all_items()
    json.dump(res, open(os.path.join(HERE, 'pairs.json'), 'w'), indent=1, ensure_ascii=False)
    if len(argv) >= 2 and argv[0] in ('grep', 'en'):
        rx = re.compile(argv[1], re.I)
        for u, its in res.items():
            for it in its:
                hay = it['orr'] if argv[0] == 'grep' else it['eng']
                if rx.search(hay):
                    print('[%s L%d %s] %s\n      EN: %s' % (u, it['line'], it['kind'], it['orr'].replace('\n', ' / ')[:700], it['eng'].replace('\n', ' / ')[:300]))
    else:
        for u, its in res.items():
            print(u, len(its), 'items', sum(1 for x in its if x['eng']), 'with English')


if __name__ == '__main__':
    main(sys.argv[1:])
