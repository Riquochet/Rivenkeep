#!/usr/bin/env python3
"""wf12 merge: Halyna's alternation in the Book v3.0.0 against the units' ink labels.

The Book's rule (notes_v3 §5.5, the two-ink ruling): every split pair in Halyna's mouth is wrapped in <!-- HALYNA --> /
<!-- HALYNA END --> (nineteen blocks); inside a block the paragraphs take the two inks by turns, the first ink first
(IV.3's reading of Brenn alternates by paragraph); under <!-- MARKED --> (II.3) the ink follows the teller's name
(Rhyna the first, Halvard the second), a fully italic line is Seren's own ink, and the oldest saying, said together, and
the laid formula take neither.  On a wood leaf the reading's lines alternate line by line (<!-- READING -->), unnamed.
The unit marks the ink before its blockquote (*(first ink)*, *(second ink)*, a heading '… first ink …', or the name
**Rhyna.** / **Halvard.** opening the Orrowen).  Writes halyna_report.json."""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import coverage as C
BOOK = C.BOOK


def book_blocks():
    L = open(BOOK, encoding='utf-8').read().split('\n')
    out = []
    cur = None
    marked = False
    leaf = None
    reading = None
    infence = False
    for i, l in enumerate(L):
        t = l.strip()
        if l.startswith('### ') or l.startswith('## '):
            leaf = l.lstrip('#').strip()
        if t == '<!-- READING -->':
            reading = dict(kind='reading', leaf=leaf, paras=[])
            out.append(reading)
            continue
        if reading is not None:
            if t.startswith(':::'):
                infence = not infence
                continue
            if infence:
                continue
            if t == 'This is held in the grain.':
                reading = None
            elif t:
                reading['paras'].append(dict(line=i + 1, text=t, want='a' if len(reading['paras']) % 2 == 0 else 'b'))
            continue
        if t == '<!-- HALYNA -->':
            cur = dict(kind='halyna', leaf=leaf, start=i + 1, paras=[])
            marked = False
            n = 0
            continue
        if cur is None:
            continue
        if t.startswith('<!-- HALYNA END'):
            out.append(cur)
            cur = None
            continue
        if t == '<!-- MARKED -->':
            marked = True
            continue
        if not t or t.startswith('<!--') or t.startswith(':::') or (t and L[i - 1].strip().startswith('::: native')):
            continue
        if t in ('This we lay as it was laid for us.', 'This I lay as it was laid for me.'):
            want = '-'
        elif marked:
            m = re.match(r'^\*\*(Rhyna|Halvard)\.\*\*', t)
            if m:
                want = 'a' if m.group(1) == 'Rhyna' else 'b'
            elif re.match(r'^\*[^*].*\*$', t):
                want = 's'
            else:
                want = '-'          # the oldest saying, said together
        else:
            if re.match(r'^\*[^*].*:\*$', t):
                want = 's'          # Seren's frame line inside a block (II.3's opening)
            elif re.match(r'^\*[^*].*\*$', t):
                want = '-'          # a fully italic line takes no ink; the alternation steps over it (IV.3's letter)
            else:
                want = 'a' if n % 2 == 0 else 'b'
                n += 1
        cur['paras'].append(dict(line=i + 1, text=t, want=want))
    return out


LAB = re.compile(r'first ink|second ink|ink I\b|ink II\b|Seren\'s (?:own )?ink|her one ink|no ink|one ink', re.I)


def label_before(unit_lines, bq_line):
    """the ink a unit gives the blockquote starting at bq_line (1-based): the nearest label above it, within the text
    since the previous blockquote or code block; or the name opening the Orrowen."""
    first = unit_lines[bq_line - 1].lstrip('>').strip()
    m = re.match(r'^\*?\*?(\*\*)?(Rhyna|Halvard)\.', re.sub(r'^\*+', '', first))
    if re.match(r'^\**(Rhyna|Halvard)\.\**', first.replace('*', '') + ' ') and re.match(r'^(\*\*)?(Rhyna|Halvard)\.', first.lstrip('*')):
        name = re.match(r'^(Rhyna|Halvard)', first.lstrip('*')).group(1)
        return 'a' if name == 'Rhyna' else 'b'
    j = bq_line - 2
    while j >= 0:
        l = unit_lines[j]
        if l.startswith('>') or l.startswith('```') or l.startswith('## ') or l.strip() == '---':
            return None
        m = LAB.search(l)
        if m and (l.startswith('*') or l.startswith('#') or l.startswith('**')) and not l.startswith('- '):
            s = m.group(0).lower()
            if 'first' in s or s == 'ink i':
                return 'a'
            if 'second' in s or s == 'ink ii':
                return 'b'
            if 'seren' in s or 'her one' in s:
                return 's'
            if 'no ink' in s:
                return '-'
            return None
        j -= 1
    return None


def main(argv):
    cov = json.load(open(os.path.join(HERE, 'coverage2.json')))
    hit = {r['line']: r['hit'] for r in cov['paras']}
    files = {}
    rep = []
    tot = collections.Counter()
    for b in book_blocks():
        seq_want, seq_got, bad = [], [], []
        for p in b['paras']:
            h = hit.get(p['line'])
            if not h:
                seq_want.append(p['want'])
                seq_got.append('?')
                bad.append((p['line'], 'no unit item'))
                continue
            u, ln, kind = h
            if u not in files:
                files[u] = open(os.path.join(C.W12, 'units', u + '.md'), encoding='utf-8').read().split('\n')
            got = label_before(files[u], ln) if kind == 'bq' else None
            seq_want.append(p['want'])
            seq_got.append(got or '·')
            ok = (got == p['want']) or (p['want'] in ('-', 's') and got in (None, '-', 's'))
            if not ok:
                bad.append((p['line'], 'want %s, unit %s (%s L%d)' % (p['want'], got, u, ln)))
        unit = hit.get(b['paras'][0]['line'])[0] if b['paras'] and hit.get(b['paras'][0]['line']) else '?'
        rep.append(dict(kind=b['kind'], leaf=b['leaf'], unit=unit, n=len(b['paras']), want=''.join(seq_want),
                        got=''.join(seq_got), ok=not bad, bad=bad))
        tot[(b['kind'], not bad)] += 1
    json.dump(rep, open(os.path.join(HERE, 'halyna_report.json'), 'w'), indent=1, ensure_ascii=False)
    for r in rep:
        print('%-7s %-34s %-4s %2d  want %-26s unit %-26s %s' % (r['kind'], (r['leaf'] or '')[:34], r['unit'], r['n'],
                                                              r['want'], r['got'], 'OK' if r['ok'] else 'DIFF ' + '; '.join(x[1] for x in r['bad'])[:300]))
    print(dict(tot))


if __name__ == '__main__':
    main(sys.argv[1:])
