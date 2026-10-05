#!/usr/bin/env python3
"""Pair each unit's Orrowen paragraph (a blockquote) with the Book's English that follows it (the house style: the
Orrowen, then the English exactly as it stands). Used for the cross-unit consistency checks: find every paragraph whose
English holds a recurring phrase and print its Orrowen side by side.
    align.py "phrase" ["phrase" ...]        (case-insensitive; also searches the pilots)"""
import glob, os, re, sys
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
FILES = sorted(glob.glob(S + '/wf8/units/*.md')) + [S + '/wf7/pilot_I1.md', S + '/wf7/pilot_IV4.md']


def pairs(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    i = 0
    fence = False
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            fence = not fence
        if not fence and l.startswith('>'):
            j = i
            orr = []
            while j < len(lines) and lines[j].startswith('>'):
                orr.append(lines[j].lstrip('>').strip())
                j += 1
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            eng = lines[k] if k < len(lines) else ''
            if eng.startswith(('Word for word', '-', '>', '#', '```', '|')):
                eng = ''
            out.append((i + 1, ' '.join(orr), eng))
            i = j
            continue
        i += 1
    return out


def norm(s):
    return re.sub(r"[^a-z' ]", ' ', s.lower().replace('’', "'")).split()


def find(phrase):
    ph = ' '.join(norm(phrase))
    res = []
    for f in FILES:
        for ln, orr, eng in pairs(f):
            if ph in ' '.join(norm(eng)):
                res.append((os.path.basename(f)[:-3], ln, orr, eng))
    return res


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('=== %s' % p)
        for u, ln, orr, eng in find(p):
            print('  [%s L%d] %s' % (u, ln, orr[:600]))
