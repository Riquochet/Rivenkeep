#!/usr/bin/env python3
"""wf12 merge fix F3: one rendering of the title page and of the Books' headings and Arguments, S11's (§1, §3), which
own them; the offered copies in S01 (§0, §3), S04, S05, S07, S09 and S10 (the Epilogue's head and Argument) are turned
into a merge note (the offered Orrowen kept as a record, in code spans, not as paragraphs), so that each Book paragraph
has exactly one unit blockquote.  The Epilogue's Argument takes S10's words (S11's own note asks for it): S11's Contents
and §3 are changed."""
import os, re
U = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'units')
log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixes.log'), 'a')


def rd(u):
    return open(os.path.join(U, u + '.md'), encoding='utf-8').read()


def wr(u, t):
    open(os.path.join(U, u + '.md'), 'w', encoding='utf-8').write(t)


def demote(u, start_marker, end_marker, label):
    t = rd(u)
    a = t.index(start_marker)
    b = t.index(end_marker, a)
    sec = t[a:b]
    rec = re.findall(r'^> (.*)$', sec, re.M)
    rec = [re.sub(r'^#+\s*', '', x).strip() for x in rec]
    note = ('*Merge (wf12): %s is S11\'s (the unit of the title page, the Contents and the Books\' headings and '
            'Arguments, §1 and §3), one rendering for the Book, so that each paragraph has one blockquote. This unit\'s '
            'offered Orrowen is kept here as a record only:* %s\n\n' % (label, ' · '.join('`%s`' % x for x in rec)))
    t = t[:a] + note + t[b:]
    wr(u, t)
    log.write('F3 %s: %s demoted to a note (%s)\n' % (u, label, ' · '.join(rec)))


# S01 §0 and §3
t = rd('S01')
a = t.index('### The Book\'s name and subtitle\n')
demote('S01', '### The Book\'s name and subtitle\n', '---\n\n## 1 · OF THIS BOOK', 'the title page')
demote('S01', '> ## *Flennath et Hald*\n', '---\n\n## 4 · I.1 THE TORN CLOAK', 'Book One\'s heading and its Argument')
demote('S04', '*II.1 opens Book Two, so its heading is given here', '---\n\n## II.1 · *KETHOW SA RE YAL NADHUMAT*', 'Book Two\'s heading and its Argument')
demote('S05', '*Book Three has no unit of its own and holds only these two tales', '---\n\n## III.1 · OF THEIR RAISING', 'Book Three\'s heading and its Argument')
demote('S07', '**Book title** · `S07-B5-01`', '---\n\n## 3 · V.1 · THE FIRST GLYPH', 'Book Five\'s heading and its Argument')
demote('S09', '> **Flennath et Mymmyl**\n', '### Title\n\n> ## *Mymmyleth*', 'Book Six\'s heading and its Argument')
demote('S10', '**¶1** · `S10-EP-01`', '**¶3** · `S10-EP-03`', 'the Epilogue\'s heading and its Argument (here ¶1 and ¶2; S11 takes this unit\'s Argument, *Galat sa re lusk et myst dem sestow*)')
# S11 takes S10's Argument for the Epilogue (Contents and §3)
t = rd('S11')
n = t.count('> *Vodh re vymm hy et myst.*')
assert n == 2, n
t = t.replace('> *Vodh re vymm hy et myst.*', '> *Galat sa re lusk et myst dem sestow.*')
wr('S11', t)
log.write('F3 S11: the Epilogue\'s Argument (Contents and §3) is S10\'s, Galat sa re lusk et myst dem sestow. (was Vodh re vymm hy et myst.)\n')
print('ok')
