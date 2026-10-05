#!/usr/bin/env python3
"""wf12 merge fix F6: pair-names in the romanised Orrowen are written under the lintel as the English writes them,
{{Halyna}} (S01, S04, S05, S06, S07, S08 and S11 did; S02, S03, S09, S10, W01, W02 and W08 wrote them bare).  Only
blockquote lines are touched; the braces are transparent to the analyzer and to the token writer (which sets the
lintel '=' on the name either way)."""
import glob, os, re
U = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'units')
NAMES = ('Halyna', 'Idrenna', 'Aldwena', 'Orvenna', 'Enrella', 'Wendhessa')
RX = re.compile(r'(?<!\{\{)\b(%s)\b(?!\}\})' % '|'.join(NAMES))
log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixes.log'), 'a')
for p in sorted(glob.glob(os.path.join(U, '*.md'))):
    L = open(p, encoding='utf-8').read().split('\n')
    n = 0
    fence = False
    for i, l in enumerate(L):
        if l.startswith('```'):
            fence = not fence
        if fence or not l.startswith('>'):
            continue
        if re.search(r'[A-Z]{4,} [A-Z]{3,}', l):      # the Hal Stonwryt, in capitals
            continue
        new, k = RX.subn(r'{{\1}}', l)
        if k:
            L[i] = new
            n += k
    if n:
        open(p, 'w', encoding='utf-8').write('\n'.join(L))
        log.write('F6 %s: %d pair-names set under the lintel ({{…}}) in the romanised Orrowen\n' % (os.path.basename(p)[:-3], n))
        print(os.path.basename(p), n)
