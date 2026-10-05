#!/usr/bin/env python3
"""wf12 merge: every paragraph of the Book v3.0.0 (wf11/book_v3.md, from OF THIS BOOK to the end, headings, datelines and
headnotes included) against the units: exactly one unit item (an Orrowen blockquote, or a ring's code block for a wood
leaf's story) whose English is that paragraph, character for character (headings may be set in bold; a Book blockquote's
'> ' is the Book's furniture).  Writes coverage.json; prints the misses and the doubles."""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pairs as P
W12 = os.path.dirname(HERE)
S = os.path.dirname(W12)
BOOK = os.path.join(S, 'wf11', 'book_v3.md')


def book_paras():
    L = open(BOOK, encoding='utf-8').read().split('\n')
    start = next(i for i, l in enumerate(L) if l.strip() == '## OF THIS BOOK')
    out = []
    fence = None      # None, or [kind, nlines]
    reading = False
    story = False
    leaf = None
    buf, bstart, bkind = [], None, None

    def flush():
        nonlocal buf, bstart, bkind
        if buf:
            out.append(dict(line=bstart + 1, kind=bkind, text='\n'.join(buf), leaf=leaf))
        buf, bstart, bkind = [], None, None

    for i in range(start, len(L)):
        raw = L[i]
        inbq = raw.startswith('>')
        t = raw[1:] if inbq else raw
        if t.startswith(' '):
            t = t[1:]
        s = t.strip()
        if raw.startswith('#'):
            flush()
            h = raw.lstrip('#').strip()
            if raw.startswith('### '):
                leaf = h
                story = reading = False
            elif raw.startswith('## '):
                leaf = h
                story = reading = False
            out.append(dict(line=i + 1, kind='head', text=h, leaf=leaf))
            continue
        if s.startswith(':::'):
            flush()
            if fence is None:
                fence = [s.split()[1] if len(s.split()) > 1 else 'fence', 0]
            else:
                fence = None
            continue
        if s.startswith('<!--') and s.endswith('-->'):
            flush()
            if 'READING' in s:
                reading = True
            continue
        if not s or s == '---':
            flush()
            continue
        if fence is not None:
            flush()
            fence[1] += 1
            out.append(dict(line=i + 1, kind='native-cap' if fence[1] == 1 else 'native-body', text=s, leaf=leaf, fence=fence[0]))
            continue
        if reading:
            if s == 'This is held in the grain.':
                flush()
                reading = False
                story = True
                out.append(dict(line=i + 1, kind='seal', text=s, leaf=leaf))
                continue
            flush()
            out.append(dict(line=i + 1, kind='reading', text=t.rstrip(), leaf=leaf))
            continue
        if story and s == '*And no one answered.*':
            flush()
            story = False
            out.append(dict(line=i + 1, kind='para', text=t.rstrip(), leaf=leaf))
            continue
        if s.startswith('|'):
            flush()
            if not re.match(r'^\|[-\s|:]+\|$', s):
                out.append(dict(line=i + 1, kind='table', text=s, leaf=leaf))
            continue
        kind = 'story' if story else ('bq' if inbq else 'para')
        if bkind is not None and bkind != kind:
            flush()
        if bstart is None:
            bstart, bkind = i, kind
        buf.append(t.rstrip() if t.rstrip().endswith('  ') is False else t.rstrip())
        # keep verse lines (two trailing spaces) together
    flush()
    return out


def norm(s):
    s = s.replace(' ', ' ')
    s = '\n'.join(x.rstrip() for x in s.split('\n'))
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s


def norm_head(s):
    s = norm(s)
    s = re.sub(r'^#+\s*', '', s)
    if s.startswith('**') and s.endswith('**'):
        s = s[2:-2]
    return s.strip()


def unit_english():
    """every English the units pair with an item: unit, line, kind, text"""
    res = P.all_items()
    out = []
    for u, its in res.items():
        for it in its:
            for n, e in enumerate(it.get('engs') or []):
                e = '\n'.join(x[1:].lstrip(' ') if x.startswith('>') else x for x in e.split('\n'))
                out.append(dict(unit=u, line=it['line'], eline=it['eline'], kind=it['kind'], eng=e, orr=it['orr'], nth=n))
    return out


def main(argv):
    bp = book_paras()
    ue = unit_english()
    idx = collections.defaultdict(list)
    for x in ue:
        idx[norm(x['eng'])].append(x)
        idx[norm_head(x['eng'])].append(x)
    res = []
    for p in bp:
        key = norm(p['text'])
        hits = idx.get(key, [])
        if p['kind'] == 'head':
            hits = hits + [x for x in idx.get(norm_head(p['text']), []) if x not in hits]
        hits = list({(h['unit'], h['line']): h for h in hits}.values())
        res.append(dict(p, n=len(hits), hits=[(h['unit'], h['line'], h['kind']) for h in hits]))
    json.dump(res, open(os.path.join(HERE, 'coverage.json'), 'w'), indent=1, ensure_ascii=False)
    cnt = collections.Counter()
    for r in res:
        cnt[(r['kind'], 'ok' if r['n'] == 1 else ('missing' if r['n'] == 0 else 'double'))] += 1
    for k in sorted(cnt):
        print(k, cnt[k])
    show = set(argv) or {'para', 'story', 'reading', 'head', 'bq', 'seal'}
    for r in res:
        if r['n'] != 1 and r['kind'] in show:
            print('%-7s L%-5d %-7s n=%d %s | %s' % (r['kind'], r['line'], (r['leaf'] or '')[:12], r['n'], r['hits'], r['text'][:110].replace('\n', ' / ')))


if __name__ == '__main__':
    main(sys.argv[1:])
