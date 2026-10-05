#!/usr/bin/env python3
"""wf12 merge fix F4: the losing units of the lexicon's decisions (merge_lex.py REPLACED) take the chosen forms:
S02 Jory > Yory, Wick > Wik, Merrick > Merrik, hoss vell > hossvell; S07 inthvell > hossvell; S08 garl lo yarl > garl ul
narl; S06 the runners' oath > S02's; S10 Merrick > Merrik; S11 ul reskow > lo reskow.  Blockquotes and the notes that
quote them; each change logged to fixes.log (the units' merge notes are written by merge_notes.py)."""
import os, re
U = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'units')
LOG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixes.log'), 'a')


def sub(u, pairs):
    p = os.path.join(U, u + '.md')
    t = open(p, encoding='utf-8').read()
    for old, new, n in pairs:
        c = t.count(old)
        assert c == n, (u, old, c, n)
        t = t.replace(old, new)
        LOG.write('F4 %s: %r -> %r (%d)\n' % (u, old[:70], new[:70], c))
    open(p, 'w', encoding='utf-8').write(t)


sub('S02', [
    ('> Dasken re ryt Wick o, et tevel sost hyor eth et pynt sost. Nath re vall Wick galat gell hy lymmyl wrod dem et Crenn.',
     '> Dasken re ryt Wik o, et tevel sost hyor eth et pynt sost. Nath re vall Wik galat gell hy lymmyl wrod dem et Crenn.', 1),
    ('Word for word: *Last Wick swore it, the youngest of us and the quickest. Wick did not love',
     'Word for word: *Last Wik swore it, the youngest of us and the quickest. Wik did not love', 1),
    ('- *Wick* is named twice:', '- *Wik* is named twice:', 1),
    ('- *Wick*: addition W12-S02-04; the spelling is the Book\'s **[Jack]** (Notes 3).',
     '- *Wik*: O3024. *Merge (wf12):* the unit had the Book\'s spelling *Wick*; the merge took the romanisation\'s, as S06 and S08 wrote it (§2.4: *k* after *i* at a word\'s end). The English keeps *Wick*. **[Jack]**', 1),
    ('> Amm re dhunnant, re ferr Jory Dhavow Hemm um hosk hald et rerddhald, eth re hoss vell sa dhevirent et higileth hemm. Lo visk et bystir re yal Merrick ul scaevurol wunth, et hemm sost hyont. Re vysk o lo: Hess. Re dhyvull Jory dem vimm umo.',
     '> Amm re dhunnant, re ferr Yory Dhavow Hemm um hosk hald et rerddhald, eth re hossvell et vell sa dhevirent et higileth hemm. Lo visk et bystir re yal Merrik ul scaevurol wunth, et hemm sost hyont. Re vysk o lo: Hess. Re dhyvull Yory dem vimm umo.', 1),
    ('Word for word: *When they had finished, Jory of Eldhythe leaned upon the capstone of the wall of the east, and breathed a song that the old ship-masters hate. At the foot of the stair Merrick was',
     'Word for word: *When they had finished, Jory of Eldhythe leaned upon the capstone of the wall of the east, and whistled the tune that the old ship-masters hate. At the foot of the stair Merrick was', 1),
    ('***Jory Dhavow Hemm*** (W12-S02-07)', '***Yory Dhavow Hemm*** (O3027)', 1),
    ('- **"whistled a tune" is *re hoss vell*, "breathed a song"** (W12-S02-09):',
     '- *Merge (wf12):* **"whistled a tune" is *re hossvell et vell*, "whistled the tune"**, with the Book\'s one word for whistling, *hossvell*, "breath-song" (O3029: S03, S05, S08, S09; the article, as the tune is the one the ship-masters hate, IV.5\'s rhyme), where the unit had *re hoss vell*, "breathed a song" (W12-S02-09, withdrawn). The unit\'s reasoning, kept:', 1),
    ('- *Jory*, *Merrick*: additions W12-S02-05, -06; the spellings are the Book\'s **[Jack]** (Notes 3).',
     '- *Yory*, *Merrik*: O3025, O3026. *Merge (wf12):* the unit had the Book\'s spellings *Jory* and *Merrick*; the merge took the tongue\'s (no *j*, §2.5; *k* after *i*, §2.4), as S03, S07 and S08 wrote them. The English keeps *Jory* and *Merrick*. **[Jack]**', 1),
    ('> Nath re dhyvull Merrick.', '> Nath re dhyvull Merrik.', 1),
])
sub('S10', [
    ('> Lo dhrenn et dhysal re yalant et higileth hemm, eth Merrick hosast.', '> Lo dhrenn et dhysal re yalant et higileth hemm, eth Merrik hosast.', 1),
    ('> Hy ull re orr Merrick dem vimm, niss,', '> Hy ull re orr Merrik dem vimm, niss,', 1),
    ('> Re hadh Merrick garl um sest et sulter.', '> Re hadh Merrik garl um sest et sulter.', 1),
    ('- **Merrick** is romanised as the Book spells him (*-ck*); by §2.4 the Orrowen spelling would be *Merrik*. The letters cut are the same.',
     '- **Merrik** (O3026). *Merge (wf12):* the unit romanised him as the Book spells him (*Merrick*); by §2.4 the Orrowen spelling is *Merrik*, as S07 wrote it, and the merge took it. The English keeps *Merrick*; the letters cut are the same.', 1),
])
sub('S07', [
    ('Um et hald rerddhalden re inthvell Yory.', 'Um et hald rerddhalden re hossvell Yory.', 1),
    ('re inthvell Yory o um et hald rerddhalden', 're hossvell Yory o um et hald rerddhalden', 1),
    ('Niss re inthvell o, hosen re hyl o', 'Niss re hossvell o, hosen re hyl o', 1),
    ('eth re orr o dem susk et dhysal ul ninthvellyl,', 'eth re orr o dem susk et dhysal ul hossvellyl,', 1),
    ('- *inthvell*, "whistle", is this unit\'s one new word (S07-08):',
     '- *Merge (wf12):* "whistle" is *hossvell*, "breath-song" (O3029), the Book\'s one word for it (S03, S05, S08, S09); the unit\'s *inthvell*, "lip-song" (S07-08, withdrawn), is the same thought. The unit\'s note on it, kept: *inthvell*, "whistle", is this unit\'s one new word (S07-08):', 1),
    ('- *ul ninthvellyl*: *inthvellyl* bedded after *ul*,', '- *Merge (wf12):* now *ul hossvellyl* (*h* is unchanged after *ul*), as S03 writes it. The unit\'s note on its own form, kept: *ul ninthvellyl*: *inthvellyl* bedded after *ul*,', 1),
])
sub('S08', [
    ('Enno eth Della, {{Enrella}}, garl lo yarl.', 'Enno eth Della, {{Enrella}}, garl ul narl.', 1),
    ('| hand in hand | ***garl lo yarl*** (S08-07) | II.3, V.1, V.7 |',
     '| hand in hand | ***garl ul narl*** (O3042; *merge (wf12)*: the unit\'s *garl lo yarl*, S08-07, withdrawn for the form of II.3, V.1, V.7 and VI.3) | II.3, V.1, V.7 |', 1),
])
sub('S06', [
    ('en narl ryss um dholm et haskardath: "Lymmym galat sa re veskym. Lymmym nayalat ullen."',
     'en narl ryss um dholm et haskardath: "Galat sa re veskym, lymmym o. Nath lymmym galat ullen. Ston."', 1),
    ('- **The runners\' oath** (fixed matter): *Lymmym galat sa re veskym. Lymmym nayalat ullen.*, "I carry the thing that I saw. I carry nothing other."',
     '- *Merge (wf12):* **the runners\' oath** is one formula in I.3 and IV.3, I.3\'s (O3035): *Galat sa re veskym, lymmym o. Nath lymmym galat ullen. Ston.*, "What I saw, I carry it. I do not carry another thing. It stands.": the English\'s own chiasm (the two *carry* meet across the full stop) and the close of every oath (§3.9). The unit\'s own form, withdrawn (S06-07), and its note, kept: *Lymmym galat sa re veskym. Lymmym nayalat ullen.*, "I carry the thing that I saw. I carry nothing other."', 1),
    ('| What I saw, I carry. I carry nothing else. | *Lymmym galat sa re veskym. Lymmym nayalat ullen.* (S06-07) | I.3 (the runners swear it) |',
     '| What I saw, I carry. I carry nothing else. | *Galat sa re veskym, lymmym o. Nath lymmym galat ullen. Ston.* (O3035, I.3\'s; *merge (wf12)*: the unit\'s S06-07 withdrawn) | I.3 (the runners swear it) |', 1),
])
sub('S11', [
    ('> Mymmyleth · *et vennuldath, cumm gor hos, eth ul reskow et ommatath* · ul lern Reskowath strom sa orrant um wadh',
     '> Mymmyleth · *et vennuldath, cumm gor hos, eth lo reskow et ommatath* · ul lern Reskowath strom sa orrant um wadh', 1),
    ('- "for the fallen" is *ul reskow et ommatath*, "in the place of the fallen": the living speak in the dead men\'s stead (a new sense of *ul reskow*, O-S11-17).',
     '- *Merge (wf12):* "for the fallen" is *lo reskow et ommatath*, "at the seat of the fallen", VI.1\'s own words for the man who speaks for the fallen at his seat (*Voss, lo reskow Horlen*: S09, O3075); the unit\'s *ul reskow* (O-S11-17, withdrawn) is the lexicon\'s "somewhere" (O2636). The living speak in the dead men\'s stead.', 1),
    ('| the fallen; for the fallen | *et ommatath*; *ul reskow et ommatath* (O-S11-17) | VI.1 |',
     '| the fallen; for the fallen | *et ommatath*; *lo reskow et ommatath* (O3075, VI.1\'s; *merge (wf12)*: O-S11-17 withdrawn) | VI.1 |', 1),
])
print('ok')
