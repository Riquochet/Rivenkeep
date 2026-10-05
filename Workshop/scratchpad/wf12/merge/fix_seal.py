#!/usr/bin/env python3
"""wf12 merge fix F2: the seal in the house style of W01-W03 (the bark's block over the Book's line) in W04-W08, and
the W04/W06/W08 claims of an italic house style corrected (F1 set their English to the Book)."""
import os
U = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'units')
BLOCK = '```\n  bark\n    bark 0: HOLD\n```\n\nThis is held in the grain.\n\n'
MERGE = ' *Merge (wf12):* set as W01–W03 set it, the bark\'s block over the Book\'s line, so that every wood leaf carries its seal in the house style.'
log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixes.log'), 'a')


def edit(u, old, new, count=1):
    p = os.path.join(U, u + '.md')
    t = open(p, encoding='utf-8').read()
    assert t.count(old) == count, (u, old[:70], t.count(old))
    t = t.replace(old, new)
    open(p, 'w', encoding='utf-8').write(t)
    log.write('F2 %s: %s\n' % (u, old[:80].replace('\n', ' ')))


edit('W04', '**The seal.** "This is held in the grain." and "…and the grain holds it still." are the seal in the bark, `bark 0: HOLD` (§11.1). They are not rings.\n',
     '**The seal**\n\n' + BLOCK + '- The seal in the bark, `bark 0: HOLD` (§11.1), not a ring: "This is held in the grain." opens the story, and "…and the grain holds it still." closes its last paragraph (ring 23).' + MERGE + '\n')
for u, r in (('W05', 20), ('W07', 24)):
    edit(u, '### 1.5 The seal\n\n*This is held in the grain.* (and, in ring %d, *…and the grain holds it still.*) is the seal in the bark, `bark 0: HOLD` (§11.1): the wood\'s, not Seren\'s, and not a ring. It has no Orrowen.\n' % r,
         '### 1.5 The seal\n\n' + BLOCK + '- The seal in the bark, `bark 0: HOLD` (§11.1), and, in ring %d, *…and the grain holds it still.*: the wood\'s, not Seren\'s, and not a ring. It has no Orrowen.%s\n' % (r, MERGE))
edit('W06', '### 3.2 Movement I (band I: rings 1–2)\n',
     '**The seal**\n\n' + BLOCK + '- The seal in the bark, `bark 0: HOLD` (§11.1), not a ring: "This is held in the grain." opens the story, and "…and the grain holds it still." closes its last paragraph (ring 22).' + MERGE + '\n\n### 3.2 Movement I (band I: rings 1–2)\n')
edit('W08', '### 3.2 Movement I (band I: rings 1 to 3, the same in all ten hearts)\n',
     '**The seal**\n\n' + BLOCK + '- The seal in the bark, `bark 0: HOLD` (§11.1), not a ring, the same in all ten hearts: "This is held in the grain." opens the story, and "…and the grain holds it still." closes its last paragraph (the closing ring). Each heart\'s bark holds a second line, that Throne\'s name in the seal\'s cup (A10, §3.4).' + MERGE + '\n\n### 3.2 Movement I (band I: rings 1 to 3, the same in all ten hearts)\n')
edit('W04', 'character for character (in the house style\'s italics).', 'character for character (set to the Book exactly at the merge; the unit had them in italics).')
edit('W06', 'rings carry their paragraph character for character (in the house style\'s italics)', 'rings carry their paragraph character for character (set to the Book exactly at the merge; the unit had them in italics)')
edit('W08', 'character for character (in the house style\'s italics).', 'character for character (set to the Book exactly at the merge; the unit had them in italics).')
edit('W08', 'Under each ring: the Book\'s English (in the house style\'s italics), then', 'Under each ring: the Book\'s English (exactly as the Book has it; set so at the merge), then')
edit('W05', '> **Kaelir sa re vymm dem varn**\n\nThe Wreck That Went Home\n', '> **Kaelir sa re vymm dem varn**\n\n**V.3 · The Wreck That Went Home**\n')
edit('W05', 'the English above is that heading\'s words.', 'the English above is that heading, set in bold as the house style sets a title (merge: the unit had dropped *V.3 ·*).')
print('ok')
