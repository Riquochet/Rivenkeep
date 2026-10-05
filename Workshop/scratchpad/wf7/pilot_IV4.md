# PILOT · IV.4 THE GIFT HELD AN HOUR, IN ITS OWN TONGUES (TIER 3)

*wf7 workflow document, 2026-09-27. Not a Book leaf and not a repo doc; nothing here goes into `Docs/`. It answers Jack's note 5 ("I'd like tier 3 on how far to take the translation") for one wood leaf: the whole of IV.4 carved in the grain (Grain Notation v2), with Seren's frame (the title, her headnote and the closing line) in Orrowen, as she writes it in her one ink, the leaf-hand (Garl Flenn).*

**Sources.** The text is `wf6/legends_v12.md` (IV.4, lines 780–824). The grain follows `wf7/grain_v2.md` (with its §21 Additions) and the v1 inventory in `wf6/mystaeri_spec.md` §3; the Orrowen follows `wf7/orrowen_v2.md` and `wf7/lexicon_orrowen.tsv`; the descent of every word is `wf7/ancestor.md`'s. The grain source is `wf7/pilot_IV4/IV-4.gn2` (knowing form); its canonical GN v2 is §4 below.

**Checks, as run.**
- `wf7/grain_validate.py wf7/pilot_IV4/IV-4.gn2`: **0 errors, 0 warnings**; no unknown sign, part, fringe mark, band or ill-formed item.
- `wf7/orr_analyze.py --file wf7/pilot_IV4/headnote.txt`: every word of Seren's frame **OK**; 0 unknown, 0 ill-formed.
- `wf7/grain_validate.py --md wf7/pilot_IV4.md` checks the round block of §4.

**The shape of it.** Myststone ("wood that time has forgotten"), a round pith, 16 rings in three bands (2 / 11 / 3), the band-rules at the Book's two `RING` markers, the seal in the bark. It holds **63 knowings** as written (one or more a sentence): **156 marks** in the rings (the root among them) and 16 more in **8 pockets** (6 said, 2 cut); **110 runners** (4 of them split, 2 hollow), **2 breaks**, **1 bind**, **1 blind**, **2 memory rays**. Packed by §4.3 it is **35 years**; with the cells the girth gives it (`[1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]`, computed by `wf7/pilot_IV4/cells.py`) its radius is about **1,290** units, inside §11.3's estimate for IV.4 (1,200–1,600). No new sign was needed.

---

## 0 · HOW TO READ THIS

- **Seren's frame is Orrowen.** The title, the headnote and the closing "*And no one answered*" are hers, not the wood's, so they are in the stone's tongue, written whole in the leaf-hand, every mortar word and every mutation (orrowen_v2 §8, §9: "if it is written, it is written whole"). Each sentence is given romanised as the Book spells it, then its gloss, then the English. The leaf-hand token string (the form `render_shore.py`, `leafhand.py` and `to_ink.py --tokens` draw) is in §1.4.
- **The wood's telling is the grain.** One ring per paragraph, one or more **knowings** per sentence, written in knowing form (`rK·i`, grain_v2 §21 A8) so each sentence can sit over its own English. Under each paragraph: the Book's English, then a short note on the translator's choices. The packed, canonical round (years and cells by §4.3) is §4.
- **Files are the pronouns** (§6.1). The table in §2.1 says who stands on each file; a runner to `@f` ends in that file's empty cell ("to that one").
- **The literal reading** is the validator's (`grain_validate.py --literal`); it is a gloss, not the telling. Halyna's English is the telling.

---

## 1 · SEREN'S FRAME, IN ORROWEN (THE LEAF-HAND, HER ONE INK)

### 1.1 The title

> **Hebbet sa re yal kethet hos clem**

| Hebbet | sa | re | yal | kethet | hos | clem |
|---|---|---|---|---|---|---|
| gift | REL(+S) | PST(+S) | S·be.PST | held | one | hour |

*The Gift Held an Hour.* (The lexicon's title, O0900: "the gift that was held one hour".)

### 1.2 The headnote

> **Hosen tum Mesk Myst: kethet hy et hebbet sost, et tolm domm sa re rik Brenn hy et tuss, ul Hyll Dhumol; doss o ul lern Yebb et Pard.**

as · remember · Mystwood: held (known) · from · the · gift · itself, the · stone · dark · REL · PST · S·pick-up · Brenn · from · the · dust, in(+N) · Tide · S·Remembering; is · it · in(+N) · face · S·Door · the · Warden.

*As the Mystwood remembers: known from the gift itself, the dark stone that Brenn picked out of the dust, in the Tide of Remembering; it faces the Warden's Door.*

- *kethet*, "held", is the canon's own verb for knowing wood (*keth*: "to know the wood is to hold it"). Seren does not write *sesket* (known as a fact).
- *rik* is *grik* ("pick up") softened after *re*, the *g* dropping before a consonant (§2.5 repair rule).
- *Yebb et Pard* is IV.3's title (*Gebb et Pard*, "the door of the warden") softened as the possessor of *ul lern*, "in the face of" (§3.2, lexicon §5.1): *doss o ul lern Yebb et Pard*, "it stands facing the Warden's Door".

> **Re heth Rhyna o hos clem lo et odh, eth re rarr o uloy niss, hosen nynth um dholm, hy vodh hebb et mesk hemm sost nayalat pynt.**

PST · S·hold · Rhyna · it · one · hour · at · the · hearth, and · PST · S·come · it · in-her · slowly, as · water · over · S·stone, from · what · gives · the · wood · old · very · nothing · quickly.

*Rhyna held it an hour at the hearth, and it came into her slowly, like water over stone, for the eldest wood gives nothing quickly.*

- *re rarr* is *darr* ("come") softened after *re*; *um dholm* is the Cry's own *tolm um dholm* mutation.
- *hy vodh*, "from what", is Orrowen's "for, because" (lexicon §5.2); *mesk hemm sost*, "the eldest wood", is the lexicon's (O1378), with *sost* for the most.

> **Re femm Halvard o nafedh.**

PST · touch · Halvard · it · never.

*Halvard never touched it.*

- The past and the negative particle together are not defined (lexicon §8 item 3), so "never" is the adverb *nafedh*, "no time", after a plain past: "Halvard touched it at no time".

> **Re yal o lo et lodh um et parow, eth re heth o o hosen re heth ey o, eth ew o sa re hadh et tolm hosast ul et brodhol.**

PST · S·be · he · at · the · mortar · across · the · ward, and · PST · S·hold · he · it · as · PST · S·hold · she · it, and · was · he · REL · PST · S·lay · the · stone · first · in · the · telling.

*He was at the mortar across the ward, and he knew it as she knew it, and it was he who began the telling.*

- **"Began" is "laid the first stone"**: *cadh et tolm hosast*. The Shoreland says a tale is laid as a course is laid (*cadh trenn*), so to begin a telling is to lay its first stone. The reserve word *mosk* ("begin") is avoided on purpose: the lexicon's findings flag it as sounding like *bosk* nasalised, the Creed's *nath mosk* (lexicon_orrowen.md §8, item 2). The idiom is added to the lexicon (§5).
- *ew o sa …* is the cleft with the past copula, as *El et tolm sa heth* ("it is the stone that holds") is with the present (§3.1).

> **Ew duss sost brodhol et trenn ul o rask, hy vodh re yal maver o wrodhol um Halyna hosen es gadh et arra o, ul et brodath orrowen sa re yal lo nafedh.**

was · hard · very · telling · the · sentence · in · its · S·end, from · what · PST · S·be · need · its · S·telling · upon · Halyna · as · FUT(+N) · N·lay · the · guest · it, in · the · words · of-the-Shore · REL · PST · S·be · at-him · never.

*The sentence at its end was the hardest to tell, for it had to be told as the Guest would have said it, in words of ours he never had.*

- *brodhol et trenn* is a verbal noun heading a construct, so it takes no article: exactly the rule the Last Carver broke (§11.9).
- "It had to be told" is the "upon" idiom, *doss maver um Y*, "need is upon Y" (O0488), in the past. The pronoun object of the verbal noun is written as its possessor, *o wrodhol*, "its telling", as the construct makes every verbal noun's object its possessor (*tumol ol varn*, "memory of our home"). The spec is silent on pronoun objects of a verbal noun; this is the reading the grammar gives.
- "Would have said" is the future particle in a past frame (*es*, O0549: "would") with *cadh*, "lay", the tongue's own idiom for telling: *es gadh et arra o*, "as the Guest would lay it", as Kael's *es gadhom sy venn* in I.1. Seren does not write *mysk* ("say"), because *es mysk* would read, to the analyzer and to an ear, as the nasalised *bysk*; nor *brodh* ("put into words"), because the nasal would make it *mrodh*, an onset the tongue does not allow (§2.5), which I.1 avoids in the same way.
- "Words of ours" is *et brodath orrowen*, "the words of the Shore": *orrowen*, "of the Shore", is the adjective the tongue's own name is made of. After *ul* (+N) *brodath* would also begin *mr-*; with the article between them nothing mutates, as in I.1's *ul et vess hosast*.
- "He never had" is the "at" idiom for having (§3.7): the words "were at him never", *sa re yal lo nafedh*.
- Revised after the back-translation (the cross-check of 2026-09-28). The line as tested read *… hosen es mrodh et arra o, ul ol mrodath …*, with two *mr-* onsets. The analyzer reads the revised line clean.

> **Re wrodha Halyna o, hos eth ullen, ul ba luth; re hadh Seren o.**

PST · S·tell-3DU · Halyna · it, one · and · other, in · N·two · ink; PST · S·lay · Seren · it.

*Told by Halyna, by turns, in two inks; set down by Seren.*

- **Halyna are two, and take the dual** (*wrodha*, 3DU), as the formal register requires (§3.9, item 1). Their pair-name carries its sealing lintel in the leaf-hand.
- **"By turns" is *hos eth ullen***, "the one and the other": the pair's antiphony in three small words. It is not in the lexicon, and is added as a set phrase (§5).
- *ul ba luth*, "in two inks", is *pa luth* (Seren's own epithet, *Seren Pa Luth*) nasalised after *ul*.
- "Set down" is *cadh*, "lay": Seren lays the telling on the leaf as a mason lays a course. She writes her own name in letters, with no lintel ("one name is a mourning").

> **Amm re yal et mesk cresket, ell re omm et brodhol, doss o rellorat eth nahlennet.**

when · PST · S·be · the · wood · broken, or · PST · fail · the · telling, is · it · marked · and · unmended.

*Where the wood was broken, or the telling failed, it is marked, and not mended.*

- *nahlennet*, "unmended", is the lexicon's (*na-* + softened *clennet*); IV.4 has no such gap, but the headnote's promise stands on every wood leaf.

### 1.3 The closing line

> **Eth re dhess nahos.**

and · PST · S·answer · no-one.

*And no one answered.* (The lexicon's formula, O0563.)

### 1.4 The leaf-hand (what Seren's pen writes)

The course-hand writes the base letter with a bite under it, and the harmonic suffix letters A and O (orrowen_v2 §6.3, §8). As `render_shore.py` / `leafhand.py` tokens (letters by `.`, `^S` and `^N` the bites, `=` the sealing lintel, `,` the wedge, `|` the perpend, `#coping` the close of a tale):

```
h.e.b.b.A.t s.a r.e g^S.a.l k.e.th.A.t h.o.s k.l.e.m
h.o.s.e.n t.u.m m.e.s.k m.y.s.t , k.e.th.A.t h.y e.t h.e.b.b.A.t s.o.s.t , e.t t.o.l.m d.o.m.m s.a r.e g^S.r.i.k b.r.e.n.n h.y e.t t.u.s.s , u.l h.y.l.l t^S.u.m.O.l , d.o.s.s o u.l l.e.r.n g^S.e.b.b e.t p.a.r.d |
r.e k^S.e.th rh.y.n.a o h.o.s k.l.e.m l.o e.t o.dh , e.th r.e d^S.a.r.r o u.l.o.y n.i.s.s , h.o.s.e.n n.y.n.th u.m t^S.o.l.m , h.y v.o.dh h.e.b.b e.t m.e.s.k h.e.m.m s.o.s.t n.a.g^S.a.l.A.t p.y.n.t |
r.e f.e.m.m h.a.l.v.a.r.d o n.a.f.e.dh |
r.e g^S.a.l o l.o e.t l.o.dh u.m e.t p.a.r.o.w , e.th r.e k^S.e.th o o h.o.s.e.n r.e k^S.e.th e.y o , e.th e.w o s.a r.e k^S.a.dh e.t t.o.l.m h.o.s.A.s.t u.l e.t b.r.o.dh.O.l |
e.w d.u.s.s s.o.s.t b.r.o.dh.O.l e.t t.r.e.n.n u.l o d^S.a.s.k , h.y v.o.dh r.e g^S.a.l m.a.v.e.r o b^S.r.o.dh.O.l u.m =h.a.l.y.n.a h.o.s.e.n e.s k^N.a.dh e.t a.r.r.a o , u.l e.t b.r.o.d.A.th o.r.r.o.w.e.n s.a r.e g^S.a.l l.o n.a.f.e.dh |
r.e b^S.r.o.dh.A =h.a.l.y.n.a o , h.o.s e.th u.l.l.e.n , u.l p^N.a l.u.th , r.e k^S.a.dh s.e.r.e.n o |
a.m.m r.e g^S.a.l e.t m.e.s.k k.r.e.s.k.A.t , e.l.l r.e o.m.m e.t b.r.o.dh.O.l , d.o.s.s o r.e.l.l.o.r.A.t e.th n.a.k^S.l.e.n.n.A.t |
e.th r.e t^S.e.s.s n.a.h.o.s #coping
```

Each line was run through `wf7/to_ink.py --tokens` (which parses it with `wf6/render_shore.py`) and draws. The lines are: the title; the headnote's seven sentences; the closing line, ended with the coping (D10: the coping ends a tale). *Halyna* carries its sealing lintel (`=`) both times; *Seren* and every other name has none.

---

## 2 · THE WOOD'S TELLING, IN THE GRAIN

### 2.1 The round and its files

`round IV-4 {wood: stone; pith: round; rings: 16; rules after: [2, 13]}`: the gift itself, Myststone, with a round pith because it is older than the war (mystaeri_spec §4.4). **Root: GIFT** ("We were given once", grain_v2 §11.3). The gift's own sentence keeps its own round (`IV-4-gift`, mystaeri_spec §5.4) and is cited by its root in ring 15.

| File | Referent | Why |
|---|---|---|
| 0 | the root in the heart ring (files 15, 0, 1 are its there); from r3, you: the shore, the shore-men, the men of the house | ahead, toward the shore [v1 bearing] |
| 1 | the Guest (Aelrhen) | a person, placeless |
| 2 | you, in the heart ring only (file 0 is the root's there, A4); from r6 the outermost hold: its doors, its stones, the dust by its wall | a place beside the shore |
| 3 | the rite | placeless |
| 4 | the host, the master of the house | clockwise of the Guest, so the host's right arm meets the Guest's left in the rite (A12) |
| 5 | a child of the long-lived (r2); from r14 a man of the house | persons, placeless |
| 6 | the likenesses, one a ring (leaves on leaves; a child gathering leaves; a shadow on a trunk; a guest under a roof; one lifting a fledgling); from r16 the long road | the grain cuts its likenesses hollow and apart (§10.9) |
| 7 | whoever holds us | placeless |
| 8 | the ages | behind: what lies over us |
| 9 | the chest | placeless |
| 10 | the world | a place |
| 11 | a child (who carried us up) | placeless |
| 12 | **we, the gift** (the teller) | the left hand, by custom (§11.2) |
| 13 | our kin: the wood of the hold | placeless |
| 14 | all that lay at a shore-man's feet and looked like stone; from r14 your mountains | |

**The seal.** "This is held in the grain." and "…and the grain holds it still." are the seal in the bark: `bark 0: HOLD` (§11.1). They are not rings.

### 2.2 Movement I (band I: the heart ring and ring 2)

The heart is plain (§3, A9): ring 1 takes no fringe, pocket, braid, bind or break, one cell to a slot; band I takes no pocket, braid, bind or break and at most two cells. What the opening says with those devices is cut with the plain substitutes.

**Ring 1**

```
  I
    r1·1  0: GIFT*
    r1·2  12: DEEP+WOOD
    r1·3  12: TREE    10: NEW+EARTH    10: EDGE×3
    r1·4  12: FALL    8: TIDE×3+LIE    6: ~LEAF+LIE    6: ~LEAF×3
    r1·5  12: GROW    8: TIDE×3+!HOLD    2: ~SQUARE      band DARK files 12–12
    r1·6  12: !SQUARE    2: STONEFOLK×3+HOLD
    run a1  12.r1·3   →in   10.r1·3        run a6  8.r1·5    →     12.r1·2
    run a2  10.r1·3   →     10.2.r1·3      run a7  12.r1·5   →as   2.r1·5
    run a3  8.r1·4    →in   12.r1·4        run a8  2.r1·6    →     12.r1·6
    run a4  8.r1·4    →as   6.r1·4         run a9  2.r1·6    →as   2.r1·5
    run a5  6.r1·4    →in   6.2.r1·4
```

*We are the eldest wood. We were a tree when the world was green to its edges. We fell, and the ages lay down on us as leaves lie down on leaves, until time forgot us and we grew dark and hard. We are not stone, though you took us for it.*

- **Reads:** Give (the root). We: the old wood; a tree, in the green world, and the world green to its many edges. We fall; many tides lie down in our falling, as seeming leaves lie down in seeming leaves. Many tides do not hold (forget) the old wood; we grow, in the dark, as the seeming stone you saw. We: not stone. The shore-men hold us, not-stone, as that seeming stone.
- "Green to its edges" is a runner from the green world to its edges, not `{all}` (no fringe in the heart). "Though you took us for it" is `HOLD →as` the likeness, not a said-pocket (A9). The one hollow stone on your file serves both "hard" and "took us for": we grew as the stone you saw.
- "Time forgot us" is the ages not holding, `TIDE×3+!HOLD`, run to the old wood itself: the heart ring has one cell to a slot and our file is cut in every year of it, so there is no empty cell for `@12` to end in (A4).
- "You" stand on file 2 in the heart ring only, because files 15, 0 and 1 of ring 1 are the root's (A4); from ring 3 on, "you" are file 0.

**Ring 2**

```
    r2·1  8: TIDE×3+!HOLD    12: WOOD    12: HOLD{still}
    r2·2  12: GIFT{slow}    12: TRUE{only}
    r2·3  5: SAPLING+GIFT{most}    12: WOOD½
    r2·4  12: GIFT#1
    run b1  8.r2·1    →     12.r2·1
    run b2  12.r2·2   →     12.2.r2·2
    run b3  5.r2·3    →     12.r2·3
  ‖
```

*Wood that time has forgotten does not itself forget. It gives slowly, and only what is so. Even a sliver of it is the dearest gift a child of the long-lived can give. We were given once. This is how.*

- **Reads:** The tides do not hold the wood; we hold, still. We give slowly: only what is true. A child gives, the most: a small wood of us. We: a gift, once.
- "Does not itself forget" is `HOLD{still}`: the wood holds still, the same words the seal will close on ("the grain holds it still"). "The dearest gift a child … can give" puts the fringe on the child's giving, `SAPLING+GIFT{most}`, and runs it to the sliver: one mark fewer than cutting "gift" twice (§10.11). "This is how" is Halyna's framing and is not cut (§11.2).

### 2.3 Movement II (band II: rings 3 to 13)

Beyond band-rule 1 every device is allowed, and the rings have two to four cells (§4.4).

**Ring 3**

```
  II
    r3·1  1: US    1: TAKE    1: NAME    1: >GO    pocket P1 said 2–3 { BOND+SQUARE }
    r3·2  1: HEAR    1: DEEP+LIVE    0: STONEFOLK×3    0: TAKE+SAIL:cloth×3    0: SQUARE×3      band MIST files 1–1
    r3·3  1: TAKE#3    0: WORD×3    6: ~SAPLING+TAKE    6: ~FALL+LEAF×3
    run c1  1.2.r3·1  →     {1.3.r3·1, 1.4.r3·1}
    run c2  1.3.r3·1  →that P1
    run c3  1.r3·2    →thru 1.2.r3·2
    run c4  1.r3·2    →     0.r3·2
    run c5  0.r3·2    →in   {0.2.r3·2, 0.3.r3·2}
    run c6  1.r3·3    →     0.r3·3
    run c7  1.r3·3    →as   6.r3·3
    run c8  6.r3·3    →     6.2.r3·3
```

*One of the long-lived took the name Aelrhen when he took his errand, and it means bond-to-stone. Through a long life he listened across the grey to the shore-men at their nets and their walls, and gathered their words as a child gathers fallen leaves, one and one and one.*

- **Reads:** One of us, on the Guest's file, takes (a split runner) the name and the sending; the name says [*Aelrhen*: bond-to-stone]. He hears, in the grey, through a long life, the shore-men, who are among their nets and their walls. He takes thrice your words, as a seeming child takes seeming fallen leaves.
- **One TAKE, two shoots**: "took the name … when he took his errand" is one taking with a forked runner (§6.1, split): one act that took both at once. A split does not order its targets in time (that is a *then* runner's work, §6.5), so "when" is carried only as far as "in the one taking"; the blind back-translation read it "took a name … and an errand" (`backtrans_IV4.md`; grain_v2 §21.8). The name is a said-pocket (a name is said), and its compound, `BOND+SQUARE`, glosses "bond-to-stone" by itself, so "it means" needs no mark.
- "One and one and one" is the count `#3` on the taking: one at a time, thrice.

**Ring 4**

```
    r4·1  1: HOLD{last}    1: TRUE+WORD#3    pocket P2 said 2–4 { STOP  [MIST]  DYING }
    r4·2  0: BOND    0: WORD×3½+!MOUTH    1: !HOLD      band WATER files 0–0
    r4·3  1: !HEAR
    run d1  1.r4·1    →     1.2.r4·1
    run d2  1.r4·1    →that P2
    run d3  1.r4·2    →     0.r4·2
    run d4  0.r4·2    →with 0.2.r4·2
    run d5  1.r4·2    →bc   1.r4·3
    run d6  1.r4·3    →     0.2.r4·2
    mem 1: r4/2 → pith
```

*At the end he had three, and he knew them for the right ones.* Stop. Sky. Dying. *He knew no way to join them, for your tongue joins its words with small words that make no sound across water, and he never heard those.*

- **Reads:** At the last he holds three true words; he holds that: [stop; the grey, the sky; dying]. You bind, on the water, with many small words that do not speak. He does not know your binding, because he does not hear (and the memory ray: never) the small soundless words.
- *Stop. Sky. Dying.* is the said-pocket `{ STOP  [MIST]  DYING }` (A1: the band alone is the sky). "Had" and "knew them for the right ones" are one holding of three true words (`HOLD{last} → TRUE+WORD#3`): in the grain to have a word and to know it are one act.
- "Your tongue joins its words" is cut on your own file, where the doer stands; the file is the pronoun, so "tongue" needs no second sign beside the soundless `!MOUTH` of the small words. "Never" is the mirror and a memory ray (A6).

**Ring 5**

```
    r5·1  1: HOLD
    r5·2  7: HOLD    6: ~TREE:trunk    6: ~GO    7: HOLD{all}      band DARK files 6–6
    r5·3  12: BOND+WORD×3
    r5·4  1: !HOLD    pocket P3 said 2–4 { STONEFOLK{only}  HOLD  CARVE{only} }
    r5·5  12: ~CARVE{all}
    run e1  1.r5·1    →     @12
    run e2  7.r5·2    →     @12
    run e3  7.r5·2    →as   6.2.r5·2
    run e4  6.2.r5·2  →thru 6.r5·2
    run e5  7.r5·2    ⇒     7.2.r5·2
    run e6  1.r5·4    →that P3
    run e7  P3.1      →     P3.2
    run e8  P3.2      →     P3.3
```

*But he had us. Whoever held us while a tree's shadow moves the breadth of its own trunk would know the whole of it. We were the sentence. He did not know that one of you alone holds only the shape of a knowing. The shape would have been enough.*

- **Reads:** He holds us. Whoever holds us, as long as a seeming shadow goes across a seeming trunk, then holds wholly. We: a sentence. He does not know that: [one of you alone holds only the cut]. We: a seeming cut, enough.
- **"Whoever" is a file**: file 7, with no thing-sign on it, is "the one who holds us"; the grain needs no pronoun (§6.3.1). "Would know" is a *then* runner: when this, then that.
- **The shadow is the DARK band** laid on the likeness's file (the register: shadow is the dark), going `→thru` the trunk (`TREE:trunk`, the part device): "the breadth of its own trunk".
- **"The shape" is the cut, `CARVE`**, the shape of a knowing (the register). "One of you alone … only the shape" and "the shape would have been enough" are `CARVE{only}` and the hollow `~CARVE{all}`: a would-have is hollow, shown and not meant (A6), and "enough" is `{all}`.

**Ring 6**

```
    r6·1  1: CHOOSE    2: EDGE{most}+CASTLE
    r6·2  2: DOOR×3    2: SQUARE×3    2: SIT+WOOD×3    13: WOOD
    r6·3  1: TRUE+HOLD    pocket P4 said 3–4 { HOLY+WOOD }
    r6·4  12: HOLD    13: EDGE+BLOOD×3    13: AXE+WOOD    13: SMOOTH
    r6·5  1: HAND    2: DOOR:post    1: MOUTH    13: !MOUTH    13: !LIVE
    run f1  1.r6·1    →     2.r6·1
    run f2  1.r6·1    →bc   13.r6·2
    run f3  13.r6·2   →in   {2.r6·2, 2.2.r6·2, 2.3.r6·2}
    run f4  1.r6·3    →that P4
    run f5  12.r6·4   →     13.r6·4
    run f6  1.r6·5    →     2.r6·5
    run f7  1.2.r6·5  →     13.r6·4
    run f8  13.r6·5   →     1.2.r6·5
    run f9  13.r6·5   →bc   13.2.r6·5
```

*He chose the outermost of your holds, for its doors and walls and benches were of our wood, and he took that for reverence. We knew it for what it was: our kin from the edge, sawn and polished. At the door he laid his hand on the post and greeted them, and they did not answer, for they were dead.*

- **Reads:** He chooses the edge-most castle, because of our kin's wood, which is in its doors, its walls and its benches (one runner, three shoots). He believes that: [holy wood]. We know our kin from the edge: timber, made smooth. He lays a hand on the door-post; he speaks to our kin; they do not speak back to him, because they do not live.
- **"Took that for reverence" is `TRUE+HOLD →that {HOLY+WOOD}`**: to believe is to hold true (§9.1), and the belief is a said-pocket (the register's own recipe).
- **The contrast is a file:** his belief stands on his file; our knowing (`HOLD`) runs from ours to the kin, *timber* (`AXE+WOOD`, "sawn") and *made smooth* (`SMOOTH`, the register's "polished"). The wood does not argue with him; it cuts what it knew.
- "Greeted" is `MOUTH` (the register: greet), "did not answer" is `!MOUTH` with its runner back, and "for they were dead" is `→bc !LIVE`.

**Ring 7**

```
    r7·1  1: KNEEL    2: SQUARE×3    4: DOOR+STONEFOLK
    r7·2  1: GIFT{most}    6: ~US+GO    6: ~HOUSE+OVER
    r7·3  1: MOUTH    1: HULL+BREAK    0: WORD#3    pocket P5 said 9–10 { AELTHAR }
    run g1  1.r7·1    →in   2.r7·1
    run g2  1.r7·1    →     4.r7·1
    run g3  1.r7·2    →     @12
    run g4  1.r7·2    →as   6.r7·2
    run g5  6.r7·2    →in   6.2.r7·2
    run g6  1.r7·3    →that P5
    run g7  1.r7·3    →in   1.2.r7·3
    run g8  1.r7·3    ⇒     0.r7·3
```

*He knelt on the stones before the master of that house and set us down, as one who comes under a roof brings his best, and spoke the name of the rite in the thunder of his own tongue,* Ael'thar, *and after it his three words in yours.*

- **Reads:** He kneels on the stones, to the host. He gives us, his most, as a seeming one of us goes in under a seeming roof. He speaks that: [the Aelthar], in bough-thunder; then three words of yours.
- **The host enters here**, on file 4 (the master of the house is `DOOR+STONEFOLK`, *vethea*, §9.1).
- **"The thunder of his own tongue" is `HULL+BREAK`: *seil·rhass*, Seilrhass itself**, "bough-thunder" (mystaeri_spec §1), built as Seilrhass builds its compounds. It is new to the compound list (§5 below).
- "And after it his three words in yours" is one speaking with a *then* runner to three of your words, on your file: the words were his to say, and yours.

**Ring 8**

```
    r8·1  1: MIND    3: HOLY{most}+AELTHAR    pocket P6 cut 13–14 { KNEEL½ }
    r8·2  3: BOND    3: GIFT    3: BLOOD    3: BLOOD×3    3: BREATH{all}
    r8·3  1: MIND    pocket P7 said 5–9 { RISE  TAKE{gently}  STONEFOLK:stem  US:crown/[STILL]  STONEFOLK:crown\[STILL] }
    run h1  1.r8·1    →that P6
    run h2  1.r8·1    →     3.r8·1
    run h3  3.r8·2    →     {3.2.r8·2, 3.3.r8·2, 3.4.r8·2}
    run h4  3.r8·2    →thru 3.5.r8·2
    run h5  1.r8·3    →that P7
    run h6  P7.1      ⇒     P7.2
    run h7  P7.2      →     P7.3
```

*This was the Aelthar as he meant to make it, the binding of gift and blood and kinship across any divide, the holiest rite of fellowship we have. He would rise and take the back of the host's neck gently in his right hand, where life goes up into thought, and draw their heads together until the foreheads touched in silence.*

- **Reads:** His mind, to the most holy Aelthar: that [the carving whose root is *kneel*, cited]. The rite binds gift, blood and kin, through every gap. His mind: that [rise, then take gently a shore-man's neck; a head and a shore-man's brow leaning to meet, in the stillness].
- **"As he meant to make it" cites the rite's own round** (the Aelthar, mystaeri_spec §5.3, root KNEEL) in a cut-pocket, by its root cut half size; the Book draws that round beside the ring (§8, a whole round cited).
- **"Across any divide" is `→thru BREATH{all}`**: through every gap (the register). "Holiest" is `{most}` on the rite.
- **His plan is a said-pocket of his mind**, so it is cut as thought, not as deed. "Where life goes up into thought" is the neck itself: the part `STONEFOLK:stem` glosses so (§5.2). The foreheads touching are two crowns leaning to meet (v1 lean), each in the STILL band (A1: a band on an item): "in silence".

**Ring 9**

```
    r9·1  1: >WOUND½    4: HAND:stem
    r9·2  1: ~!HOLD    4: STONEFOLK:stem
    r9·3  1: ~>WOUND½    1: HAND:stem
    r9·4  1: MOUTH?{only}    4: BLOOD    1: GIFT+BLOOD
    r9·5  3: BOND+MOUTH
    run i1  1.r9·1    →     4.r9·1
    run i2  1.r9·2    →     4.r9·2
    run i3  1.r9·3    →     1.2.r9·3
    run i4  1.r9·4    →     4.r9·4
    run i5  1.r9·4    →as   1.2.r9·4
    run i6  4.r9·1    →     bind K1 ~
    run i7  1.2.r9·3  →     bind K1 ~
  bind K1 i6 i7 → 3.r9·5
```

*With his left hand he would open a shallow cut on the host's right arm, and let go the neck, and cut his own left arm, for he would ask no blood he did not give. Then the two would press their bleeding arms together, shoulder to shoulder: a promise of united front, that harm to one was harm to both.*

- **Reads:** He wounds, a little, the host's arm. He would let go the host's neck (hollow). He would wound, a little, his own arm (hollow). He asks only the host's blood as he gives blood. The host's arm and his own arm, bound, each only with the other (a seeming bind: the strands hollow), and bound, to the rite: a promise.
- **Truth or nothing, in a would.** Ring 9 is still the rite as meant, but it is cut outside a pocket, in the wood's own voice, so the grain must not cut as done what was never done. **What was made is cut whole** (the shallow cut was opened: ring 10 says so). **What was never made is cut hollow**, "shown, not meant" (A6: *would have*): letting go the neck as a step of the rite, his own cut, and the pressing of the arms, whose two bind strands are hollow runners (§6.1). The bind itself is the rite's meaning, "harm to one is harm to both" (§7.3; Aelthar r6, §17), and its out-runner is the promise (`BOND+MOUTH`).
- **Left and right are placement** (A12): the host on file 4 stands clockwise of the Guest on file 1, so the host's right arm and the Guest's left meet in the bind.
- "He would ask no blood he did not give": `MOUTH?` is to ask; `{only}` with an *as* runner to his own giving of blood is "only as he gives".

**Ring 10**

```
    r10·1  1: KNEEL@1
    r10·2  0: STONEFOLK:foot+STRIKE    2: DUST    2: SQUARE    0: STONEFOLK×3+LAUGH
    r10·3  1: !STOP    3: AELTHAR+!STOP
    r10·4  1: RISE    1: TAKE{gently}    4: STONEFOLK:stem    6: ~SAPLING½    6: ~>RISE
    r10·5  1: US:crown/    4: STONEFOLK:crown\      band STILL files 1–1
    r10·6  1: >WOUND½    4: HAND:stem
    run j1  0.r10·2   →     @12
    run j2  0.r10·2   →in   2.r10·2
    run j3  2.r10·2   →in   2.2.r10·2
    run j4  1.r10·1   ⇒     3.r10·3
    run j5  1.r10·3   →bc   3.r10·3
    run j6  1.2.r10·4 →     4.r10·4
    run j7  1.2.r10·4 →as   6.2.r10·4
    run j8  6.2.r10·4 →     6.r10·4
    run j9  1.r10·6   →     4.r10·6
```

*He made the first step. A foot struck us into the dust by the wall, and the men of the house laughed. He did not stop, for the rite is not stopped once it is begun. He rose and took the neck as gently as one lifts a fledgling, and the foreheads met, and he was silent. Then with his left hand he opened the shallow cut.*

- **Reads:** He kneels, the first. A shore-man's foot strikes us into the dust at the wall; the shore-men laugh. He does not stop, because the Aelthar does not stop, once the first step is made. He rises; he takes gently the host's neck, as a seeming one lifts a seeming small child. His head and the host's brow lean to meet; he, in the stillness. He wounds, a little, the host's arm.
- **"The first step" is `KNEEL@1`**, the ordinal: the kneeling of ring 7 was the first step. "Once it is begun" is a *then* runner from it to the rite's not stopping.
- **A foot, not the host's foot.** The wood does not say whose foot struck it (IV.3 does), so the foot is a shore-man's, on the shore's file.
- "He was silent" is the STILL band over his own file in the year his brow meets the host's.

**Ring 11**

```
    r11·1  4: HAND:stem+TURN
    run k1  4.r11·1   →bc   ∅
```

*And the host drew back. We do not know why. Fear leaves no mark on wood.*

- **Reads:** The host's arm turns aside, and why, the wood does not hold.
- **The blind.** The canon's line is the rule of the script: the grain has no sign for a shore-man's fear, and where it stood the wood cuts only the empty cup (§6.1, §9.2). One mark and one empty cup: the barest ring of the round, as it should be. "Drew back" is the arm turning aside (the register), because it is the arm's moving that the next ring turns on.

**Ring 12**

```
    r12·1  1: AXE+GO½    4: HAND:stem    4: HAND:stem+GO    1: AXE+GO    4: DEEP+WOUND
    r12·2  4: BLOOD+GO    4: CRY    0: STONEFOLK×3+GO
    r12·3  1: HAND+!RISE    1: ~>WOUND½    1: HAND:stem
    r12·4  0: STONEFOLK×3+STRIKE    1: FALL    2: DOOR+SQUARE×3    1: DYING    3: AELTHAR{half}
    r12·5  12: LIE    2: DUST    12: HEAR{all}    0: !TAKE
    run l1  1.r12·1   →     4.r12·1        run l7  1.2.r12·3 →     1.3.r12·3
    run l2  4.2.r12·1 →     1.r12·1        run l8  0.r12·4   →     1.r12·4
    run l3  1.2.r12·1 →bc   4.2.r12·1      run l9  1.r12·4   →in   2.r12·4
    run l4  1.2.r12·1 →     4.3.r12·1      run l10 1.2.r12·4 →with 3.r12·4
    run l5  0.r12·2   →     4.2.r12·2      run l11 12.r12·5  →in   2.r12·5
    run l6  1.r12·3   →     0.r12·2        run l12 0.r12·5   →     12.r12·5
  lap  l2 ⊳ l1
```

*The blade that was meant to go a little way went deep, for the arm was moving. The host's blood came, and he cried out, and his men came. The Guest did not lift his hand against them, and the cut he would have made on his own arm was never made. They struck him down on the stones of the door, and he died there with the rite half made. We lay in the dust and heard all of it, and no one picked us up.*

- **Reads:** The blade goes a little way to the host's arm, and the arm's moving **breaks** it; the blade goes, because the arm moves, to a deep wound. The host's blood flows; he cries out; the shore-men go to his cry. His hand does not rise to them; the cut he would have made, on his own arm (hollow). The shore-men strike him falling on the stones of the door; he dies, with the rite half made. We lie in the dust and hear all of it; you do not take us up.
- **The break** (§7.1) is the ring's centre: the arm's runner crosses the blade's shallow runner square and splinters it, `lap l2 ⊳ l1`. The grain's own grammar says what the English says with "for": the moving arm thwarted the cut meant to be shallow.
- "Half made" is `{half}` on the rite; "heard all of it" is `HEAR{all}`; "no one picked us up" is the shore's file not taking.

**Ring 13**

```
    r13·1  14: ~SQUARE×3{all}    0: STONEFOLK:foot
    r13·2  12: ~MOUTH{only}
    r13·3  0: FIND
    run m1  14.r13·1  →in   0.r13·1
    run m2  12.r13·2  →     @0
    run m3  0.r13·3   →     @12
    run m4  0.r13·3   →with 0.r13·1
  lap  m3 ⊳ m2
    mem 14: r13/1 → pith
  ‖
```

*Of all the things that ever lay at a shore-man's feet and looked like stone, we were the one that could have spoken to him; and it was the one his foot found.*

- **Reads:** All the seeming stones, ever (the memory ray: always), at a shore-man's foot. We alone could have spoken, to him. He finds, with his foot, us; and his finding **breaks** our speaking.
- **"Looked like stone" is the hollow SQUARE**, a seeming stone, and "could have spoken" the hollow MOUTH: both are shown and not meant. "Ever" is a memory ray from an outer ring (v1: *always*).
- **The irony is a break.** The foot's finding runs from the shore's file to ours and crosses our could-have-spoken, which runs from ours to his, and splinters it: the thing that could have spoken was cut off by the one that found it.

### 2.4 Movement III (band III: rings 14 to 16)

**Ring 14**

```
  III
    r14·1  5: STONEFOLK{only}+GO{again}    5: MORNING
    r14·2  5: TAKE    2: DUST
    r14·3  5: _>LIE    5: !HOLD
    r14·4  12: LIE    5: STONEFOLK+LIVE{most}    12: BOND+WORD×3      band DARK files 12–12
    r14·5  12: LIE    9: CHEST    9: SQUARE×3
    r14·6  11: SAPLING+CARRY    11: HAND:stem#2    14: DEEP+SQUARE×3
    r14·7  0: DEEP+HOLD{only}
    r14·8  1: CARRY    2: DOOR
    run n1  5.r14·1   →     @12            run n9  9.r14·5   →in   9.2.r14·5
    run n2  5.r14·2   →     @12            run n10 11.r14·6  →     @12
    run n3  5.r14·2   →thru 2.r14·2        run n11 11.r14·6  →in   14.r14·6
    run n4  5.r14·3   →     @12            run n12 11.r14·6  →with 11.2.r14·6
    run n5  5.2.r14·3 →     @12            run n13 0.r14·7   →     @12
    run n6  12.r14·4  →thru 5.r14·4        run n14 1.r14·8   →     2.r14·8
    run n7  12.r14·4  →with 12.2.r14·4     run n15 1.r14·8   ⇒     12.r15·1
    run n8  12.r14·5  →in   9.r14·5
```

*In the morning a man of the house came back alone and picked us out of the dust, and put us away, and did not hold us. We lay most of his life in the dark with the sentence in us; then in a chest among the mute stones; then we were carried up into your mountains in the arms of a child. No one held us so long, until you. Here is the sentence, as it was brought to the door:*

- **Reads:** A shore-man, alone, goes again to us, in the morning; he takes us, out through the dust; he lays us down unseen; he does not hold us. We lie in the dark, through most of his life, with our sentence. Then we lie in a chest among the stones. A child carries us, with her two arms, into your mountains. Only you held us long. The Guest carried it to the door; then, in ring 15, what we hold.
- **"Came back" is `GO{again} → @12`**: the grain has no *come*, only a going to the one it comes to (§9.2), and "alone" is `{only}` (fix B2).
- **"Put us away" is the causative lying, smoothed** (`_>LIE`): laid down, hidden. "Did not hold us" is exactly that, `!HOLD`: he never knew it, for to know the wood is to hold it.
- **"No one held us so long, until you" is `DEEP+HOLD{only}`** on your file: only you held us long. `DEEP+HOLD` ("hold long", *eir·thein*) is a new compound (§5).
- "Here is the sentence" is a *then* runner into ring 15: the Guest's carrying, and after it, what the wood holds.

**Ring 15**

```
    r15·1  12: HOLD    pocket P8 cut 3–5 { STOP½ }
    run o1  12.r15·1  →that P8
```

*Stop the felling of the pillars at the edge of the grey, for they are not timber. The sky over us is their breath, and ours, and when you cut them it comes open, and our children cannot live in the open sun. We are here, behind the grey, and we have been here always, and we are not your enemies. Stop, for the sky is dying, and we are dying under it.*

- **Reads:** We hold that: [the carving whose root is *stop*, cited by its root].
- **The sentence is cited whole**, as §8 and §11.3 require: a cut-pocket holding the root of its own round, `STOP½`, and the Book draws the sentence's round (`IV-4-gift`, `wf7/grain2_texts/GIFT.gn2`, eleven rings, "the sentence nearest the surface") beside the ring. Its English, "as the Guest would have said it, in words of ours he never had", is Halyna's.

**Ring 16**

```
    r16·1  1: GO    1: MOUTH{only}
    r16·2  12: CARRY    6: DEEP+ROAD
    run p1  1.r16·1   →     @0
    run p2  1.r16·1   →for  1.2.r16·1
    run p3  12.r16·2  →thru 6.r16·2
  bark
    bark 0: HOLD
```

*That is all he came to say. We have carried it a long way, and the grain holds it still.*

- **Reads:** He goes to you, for speaking, only. We carry it through the long road. (The seal: this is held in the grain.)
- "The grain holds it still" is the seal in the bark, not a mark (§11.1). The closing frame, *And no one answered*, is Seren's, in Orrowen (§1.3).

---

## 3 · WHAT THE TRANSLATION DID, AND WHY

**The grain.**

1. **Every sentence is carved, once** (§10.11). One mark to a content word; a referent already cut in a knowing is pointed at, never cut again. **Files are the pronouns**: *we* is file 12, *you* file 0, *the Guest* file 1, and "whoever held us" is simply file 7 with no thing-sign on it (§6.3.1). Thirteen runners end on a file referent (`@12`, `@0`).
2. **The heart stays plain** (§3, A9). Rings 1–2 carry no pocket, braid, bind or break, and ring 1 no fringe: "green to its edges" is a runner to the edges, "though you took us for it" a `HOLD →as` the likeness. The fine work begins outward: the first pocket is in ring 3, the first break in ring 12. Jack's "anchor in the middle … details in the outer rings" holds in this leaf exactly.
3. **Truth or nothing, in the conditional.** IV.4 is full of *would*: the shape *would have been* enough, the Guest *would* rise and cut, *could have* spoken, the cut he *would have* made. The grain has one device for it, the hollow ("shown, not meant", A6), and this leaf uses it strictly: **what was done is cut whole, what was never done is cut hollow**. So ring 9, the rite as he meant it, is a mixture: the host's shallow cut was opened (whole); the letting go of the neck, the Guest's own cut and the pressing of the arms were never made (hollow marks, and **hollow bind strands**). Where the telling gives his intent as thought (ring 8), it is a said-pocket of his mind, which may hold what never happened.
4. **Two breaks, both the leaf's own turning points.** Ring 12, the arm's moving breaks the blade's shallow going: §7.1's own example for IV.4. Ring 13 adds a second that §7.1 did not list: the foot's finding breaks our could-have-spoken, runner across runner, "the one that could have spoken to him; and it was the one his foot found".
5. **The first bind carved in a whole leaf** (IV.6 had none, §12.4). The rite's "harm to one was harm to both" is the two arms' runners hooked through each other, its out-runner the promise (`BOND+MOUTH`), as §17 recommends for the Aelthar's r6. Here its strands are hollow, because the arms were never pressed.
6. **Two rounds cited, not re-carved.** Ring 8 cites the rite as he meant it by the Aelthar's own round (root KNEEL, mystaeri_spec §5.3); ring 15 cites the sentence by its round (root STOP, `IV-4-gift`). Each is a cut-pocket holding the root half size, with the cited round drawn beside (§8). The Book's Original tab should draw the Aelthar beside ring 8's plate and the sentence beside ring 15's.
7. **The blind stands alone in ring 11**: one mark, one empty cup. The barest ring of the round is the one the whole leaf turns on.
8. **The literal reading is rough in places, as it should be**: SMOOTH reads "go veiled" where the register gives it as "made smooth; polished" (ring 6), and `DEEP+WOUND` read "being struck, old" until the compound was added. The telling is Halyna's; the reading is only a gloss (§13.5).

**Findings for the spec and the validator** (none blocks anything).

- **A band's year is the year of its knowing's first mark.** `pack_round` gives a condition band the row where the knowing's *first* mark lands, not the row of the marks on the band's own files. Written in the telling's order, IV.4's "we grew dark" (r1·5, whose first mark was the ages') laid its DARK band on the year of the *tree*, not of the growing (the reading said "We: tree, in the dark"); and under a trial cells list "across water" (r4·2, whose first mark was the Guest's) laid its WATER band over a year with nothing on file 0 (the reading said "The water (the sea) lies over files 0–0", over nothing). The validator raised neither. Both were fixed by writing the band's own mark first. **Proposed:** a note in A8 ("write a band's own mark first in its knowing"), and a validator warning when a band lies over files that hold no mark in its year.
- **Two `@f` terminals may share one empty cell** (ring 5: "he had us" and "whoever held us" both end in file 12's free cell). The validator allows it; §6.1 does not say. It reads right ("to us", twice), and the renderer should keep the two terminals apart in the cell.
- **Ring 2 is one cell wide** by §4.4 (its inner radius, 164, is under the 311 two cells need), so its six marks on our file stack as six years. Legal, and true to the heart's plainness.
- **The blind back-translation** (`wf7/backtrans_IV4.md`) read the leaf back from its GN and Orrowen alone. The grain scored 2 exact, 12 close and 2 drift (ring 5; and ring 15, whose sentence is a cited round). The frame scored 5 exact, 3 close and 1 drift (the headnote's *doss maver um*, "must", read as "wanted"). Its fixes: grain_v2 §21.8 (A15, the register readings a decoder needs; A16, a belonging does not introduce a referent), the validator's reading, the analyzer's set-phrase hints, and *nynth* "water" in the lexicon.

**Orrowen.**

- **"Began" is *cadh et tolm hosast*, "laid the first stone"**, the Shoreland's own metaphor for telling (to tell is to lay a course). The reserve *mosk* ("begin") is avoided: the lexicon's findings flag it as the nasalised *bosk* of the Creed, *nath mosk*. Added as a set phrase.
- **"By turns" is *hos eth ullen***, "the one and the other". Added as a set phrase.
- **The pronoun object of a verbal noun is its possessor**: *maver o wrodhol*, "the need of its telling" (the construct gives every verbal noun's object as its possessor). The spec is silent on pronoun objects; flagged for Jack as a small point of grammar.
- **"Never" after a past is *nafedh*** ("no time"), because the lexicon's pass left the past and the negative together undefined. (A later lexicon row, O2861 *nath re*, now proposes a negative past; *Nath re femm Halvard o* would then also serve. *Re femm Halvard o nafedh* keeps "never", which is what the Book says.)
- ***ul o rask*, not *ul mo rask***: the analyzer treats a possessive pronoun after a nasalising trigger as unmutated; §3.3's letter ("only the word immediately after the trigger mutates", and a vowel takes *m-* or *n-*) would nasalise the pronoun itself. The analyzer's reading is followed; flagged for Jack.
- ***es gadh*, not *es mysk* or *es mrodh***: after *es* (+N), *mysk* "say" is heard as the nasalised *bysk*, and the analyzer glosses it so; *brodh* "put into words" would nasalise to *mrodh*, an onset §2.5 does not allow, which I.1 avoids too. *cadh* "lay" is the tongue's own idiom for telling. *ul et brodath orrowen*, "in the words of the Shore", keeps *brodath* out of the nasal in the same way. (Revised in the cross-check of 2026-09-28; the line as tested had *es mrodh* and *ul ol mrodath*.)
- **Kael's oath-cadence and verse** do not arise in IV.4: it has no oath and no song. The one formula in Seren's frame is the hearth's closing line, kept exactly as the lexicon has it.

**For the builder.** `lexicon_orrowen.tsv` is generated by `wf7/lex/build_lexicon.py`; rows appended by hand (O2858–O2859 here, and the other pilots' rows after them) are lost on a rebuild unless their recipes go into `lex/en_map/` (the set phrases belong in `y_world.txt`). The grain's additions are in the spec itself (`grain_v2.md` §21.7), so they survive.

---

## 4 · THE WHOLE ROUND, CANONICAL GN v2

Printed by `grain_validate.py --canon` from `wf7/pilot_IV4/IV-4.gn2` (years and cells packed by §4.3; runners in §13.4 order), with the two memory rays. This block is what `--md` checks.

```
round IV-4 {wood: stone; pith: round; rings: 16; rules after: [2, 13]; cells: [1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]}
# file 0: the root (in the heart ring files 15, 0 and 1 are the root's)
# file 0 from r3: you (the shore; the shore-men; the men of the house)
# file 1: the Guest (Aelrhen)
# file 2: you (the shore: in the heart ring, where file 0 is the root's)
# file 2 from r6: the outermost hold (its doors, its stones, the dust by its wall)
# file 3: the rite
# file 4: the host (the master of the house)
# file 5: a child of the long-lived
# file 5 from r14: a man of the house
# file 6: a likeness (leaves on leaves)
# file 6 from r3: a likeness (a child gathering leaves)
# file 6 from r5: a likeness (a tree's shadow on its trunk)
# file 6 from r7: a likeness (a guest under a roof)
# file 6 from r10: a likeness (one lifting a fledgling)
# file 6 from r16: the long road
# file 7: whoever holds us
# file 8: the ages (time)
# file 9: the chest
# file 10: the world
# file 11: a child (who carried us)
# file 12: we (the gift)
# file 13: our kin (the wood of the hold)
# file 14: all that looked like stone at a shore-man's feet
# file 14 from r14: your mountains
  I
    r1/1  0: GIFT*    2: ~SQUARE    6: ~LEAF+LIE    8: TIDE×3+LIE    10: NEW+EARTH    12: DEEP+WOOD
    r1/2  2: STONEFOLK×3+HOLD    6: ~LEAF×3    8: TIDE×3+!HOLD    10: EDGE×3    12: TREE
    r1/3  12: FALL
    r1/4  12: GROW      band DARK files 12–12
    r1/5  12: !SQUARE
    r2/1  5: SAPLING+GIFT{most}    8: TIDE×3+!HOLD    12: WOOD
    r2/2  12: HOLD{still}
    r2/3  12: GIFT{slow}
    r2/4  12: TRUE{only}
    r2/5  12: WOOD½
    r2/6  12: GIFT#1
  ‖
  II
    r3/1  0.1: STONEFOLK×3    0.2: TAKE+SAIL:cloth×3    1.1: US    1.2: TAKE    pocket P1 said 2–3 { BOND+SQUARE }    6.1: ~SAPLING+TAKE    6.2: ~FALL+LEAF×3
    r3/2  0.1: SQUARE×3    0.2: WORD×3    1.1: NAME    1.2: >GO
    r3/3  1.1: HEAR    1.2: DEEP+LIVE      band MIST files 1–1
    r3/4  1: TAKE#3
    r4/1  0.1: BOND    0.2: WORD×3½+!MOUTH    1.1: HOLD{last}    1.2: TRUE+WORD#3    1.3: !HOLD    pocket P2 said 2–4 { STOP  [MIST]  DYING }      band WATER files 0–0
    r4/2  1: !HEAR
    r5/1  1.1: HOLD    1.2: !HOLD    pocket P3 said 2–4 { STONEFOLK{only}  HOLD  CARVE{only} }    6.1: ~TREE:trunk    6.2: ~GO    7.1: HOLD    7.2: HOLD{all}    12.1: BOND+WORD×3    12.2: ~CARVE{all}      band DARK files 6–6
    r6/1  1.1: CHOOSE    1.2: TRUE+HOLD    1.3: HAND    1.4: MOUTH    2.1: EDGE{most}+CASTLE    2.2: DOOR×3    2.3: SQUARE×3    2.4: SIT+WOOD×3    pocket P4 said 3–4 { HOLY+WOOD }    12: HOLD    13.1: WOOD    13.2: EDGE+BLOOD×3    13.3: AXE+WOOD    13.4: SMOOTH
    r6/2  2: DOOR:post    13.1: !MOUTH    13.2: !LIVE
    r7/1  0: WORD#3    1.1: KNEEL    1.2: GIFT{most}    1.3: MOUTH    1.4: HULL+BREAK    2: SQUARE×3    4: DOOR+STONEFOLK    6.1: ~US+GO    6.2: ~HOUSE+OVER    pocket P5 said 9–10 { AELTHAR }
    r8/1  1.1: MIND    1.2: MIND    3.1: HOLY{most}+AELTHAR    3.2: BOND    3.3: GIFT    3.4: BLOOD    pocket P7 said 5–9 { RISE  TAKE{gently}  STONEFOLK:stem  US:crown/[STILL]  STONEFOLK:crown\[STILL] }    pocket P6 cut 13–14 { KNEEL½ }
    r8/2  3.1: BLOOD×3    3.2: BREATH{all}
    r9/1  1.1: >WOUND½    1.2: !~HOLD    1.3: ~>WOUND½    1.4: HAND:stem    3: BOND+MOUTH    4.1: HAND:stem    4.2: STONEFOLK:stem    4.3: BLOOD
    r9/2  1.1: MOUTH?{only}    1.2: GIFT+BLOOD
    r10/1 0.1: STONEFOLK:foot+STRIKE    0.2: STONEFOLK×3+LAUGH    1.1: KNEEL@1    1.2: !STOP    1.3: RISE    1.4: TAKE{gently}    2.1: DUST    2.2: SQUARE    3: AELTHAR+!STOP    4.1: STONEFOLK:stem    4.2: STONEFOLK:crown\    4.3: HAND:stem    6.1: ~SAPLING½    6.2: ~>RISE
    r10/2 1.1: US:crown/    1.2: >WOUND½      band STILL files 1–1
    r11/1 4: HAND:stem+TURN
    r12/1 0.1: STONEFOLK×3+GO    0.2: STONEFOLK×3+STRIKE    0.3: !TAKE    1.1: AXE+GO½    1.2: AXE+GO    1.3: HAND+!RISE    1.4: ~>WOUND½    2.1: DOOR+SQUARE×3    2.2: DUST    3: AELTHAR{half}    4.1: HAND:stem    4.2: HAND:stem+GO    4.3: DEEP+WOUND    4.4: BLOOD+GO    12.1: LIE    12.2: HEAR{all}
    r12/2 1.1: HAND:stem    1.2: FALL    1.3: DYING    4: CRY
    r13/1 0.1: STONEFOLK:foot    0.2: FIND    12: ~MOUTH{only}    14: ~SQUARE×3{all}
  ‖
  III
    r14/1 0: DEEP+HOLD{only}    1: CARRY    2.1: DUST    2.2: DOOR    5.1: STONEFOLK{only}+GO{again}    5.2: MORNING    5.3: TAKE    5.4: _>LIE    9.1: CHEST    9.2: SQUARE×3    11.1: SAPLING+CARRY    11.2: HAND:stem#2    12.1: LIE    12.2: BOND+WORD×3    12.3: LIE    14: DEEP+SQUARE×3      band DARK files 12–12
    r14/2 5.1: !HOLD    5.2: STONEFOLK+LIVE{most}
    r15/1 pocket P8 cut 3–5 { STOP½ }    12: HOLD
    r16/1 1.1: GO    1.2: MOUTH{only}    6: DEEP+ROAD    12: CARRY
  bark
    bark 0: HOLD
  runners
    run a5   6.r1/1        →in    6.r1/2
    run a4   8.r1/1        →as    6.r1/1
    run a3   8.r1/1        →in    12.r1/3
    run a2   10.r1/1       →      10.r1/2
    run a9   2.r1/2        →as    2.r1/1
    run a8   2.r1/2        →      12.r1/5
    run a6   8.r1/2        →      12.r1/1
    run a1   12.r1/2       →in    10.r1/1
    run a7   12.r1/4       →as    2.r1/1
    run b3   5.r2/1        →      12.r2/5
    run b1   8.r2/1        →      12.r2/1
    run b2   12.r2/3       →      12.r2/4
    run c5   0.1.r3/1      →in    {0.2.r3/1, 0.1.r3/2}
    run c1   1.2.r3/1      →      {1.1.r3/2, 1.2.r3/2}
    run c8   6.1.r3/1      →      6.2.r3/1
    run c2   1.1.r3/2      →that  P1
    run c4   1.1.r3/3      →      0.1.r3/1
    run c3   1.1.r3/3      →thru  1.2.r3/3
    run c7   1.r3/4        →as    6.1.r3/1
    run c6   1.r3/4        →      0.2.r3/2
    run d4   0.1.r4/1      →with  0.2.r4/1
    run d1   1.1.r4/1      →      1.2.r4/1
    run d2   1.1.r4/1      →that  P2
    run d3   1.3.r4/1      →      0.1.r4/1
    run d5   1.3.r4/1      →bc    1.r4/2
    run d6   1.r4/2        →      0.2.r4/1
    run e1   1.1.r5/1      →      @12
    run e6   1.2.r5/1      →that  P3
    run e7   P3.1          →      P3.2
    run e8   P3.2          →      P3.3
    run e4   6.2.r5/1      →thru  6.1.r5/1
    run e3   7.1.r5/1      →as    6.2.r5/1
    run e5   7.1.r5/1      ⇒      7.2.r5/1
    run e2   7.1.r5/1      →      @12
    run f1   1.1.r6/1      →      2.1.r6/1
    run f2   1.1.r6/1      →bc    13.1.r6/1
    run f4   1.2.r6/1      →that  P4
    run f6   1.3.r6/1      →      2.r6/2
    run f7   1.4.r6/1      →      13.2.r6/1
    run f5   12.r6/1       →      13.2.r6/1
    run f3   13.1.r6/1     →in    {2.2.r6/1, 2.3.r6/1, 2.4.r6/1}
    run f8   13.1.r6/2     →      1.4.r6/1
    run f9   13.1.r6/2     →bc    13.2.r6/2
    run g1   1.1.r7/1      →in    2.r7/1
    run g2   1.1.r7/1      →      4.r7/1
    run g4   1.2.r7/1      →as    6.1.r7/1
    run g3   1.2.r7/1      →      @12
    run g8   1.3.r7/1      ⇒      0.r7/1
    run g7   1.3.r7/1      →in    1.4.r7/1
    run g6   1.3.r7/1      →that  P5
    run g5   6.1.r7/1      →in    6.2.r7/1
    run h2   1.1.r8/1      →      3.1.r8/1
    run h1   1.1.r8/1      →that  P6
    run h5   1.2.r8/1      →that  P7
    run h3   3.2.r8/1      →      {3.3.r8/1, 3.4.r8/1, 3.1.r8/2}
    run h4   3.2.r8/1      →thru  3.2.r8/2
    run h6   P7.1          ⇒      P7.2
    run h7   P7.2          →      P7.3
    run i1   1.1.r9/1      →      4.1.r9/1
    run i2   1.2.r9/1      →      4.2.r9/1
    run i3   1.3.r9/1      →      1.4.r9/1
    run i7   1.4.r9/1      →      bind K1 ~
    run i6   4.1.r9/1      →      bind K1 ~
    run i4   1.1.r9/2      →      4.3.r9/1
    run i5   1.1.r9/2      →as    1.2.r9/2
    run j2   0.1.r10/1     →in    2.1.r10/1
    run j1   0.1.r10/1     →      @12
    run j4   1.1.r10/1     ⇒      3.r10/1
    run j5   1.2.r10/1     →bc    3.r10/1
    run j6   1.4.r10/1     →      4.1.r10/1
    run j7   1.4.r10/1     →as    6.2.r10/1
    run j3   2.1.r10/1     →in    2.2.r10/1
    run j8   6.2.r10/1     →      6.1.r10/1
    run j9   1.2.r10/2     →      4.3.r10/1
    run k1   4.r11/1       →bc    ∅
    run l5   0.1.r12/1     →      4.r12/2
    run l8   0.2.r12/1     →      1.2.r12/2
    run l12  0.3.r12/1     →      12.1.r12/1
    run l1   1.1.r12/1     →      4.1.r12/1
    run l3   1.2.r12/1     →bc    4.2.r12/1
    run l4   1.2.r12/1     →      4.3.r12/1
    run l6   1.3.r12/1     →      0.1.r12/1
    run l7   1.4.r12/1     →      1.1.r12/2
    run l2   4.2.r12/1     →      1.1.r12/1
    run l11  12.1.r12/1    →in    2.2.r12/1
    run l9   1.2.r12/2     →in    2.1.r12/1
    run l10  1.3.r12/2     →with  3.r12/1
    run m4   0.2.r13/1     →with  0.1.r13/1
    run m3   0.2.r13/1     →      @12
    run m2   12.r13/1      →      @0
    run m1   14.r13/1      →in    0.1.r13/1
    run n13  0.r14/1       →      @12
    run n14  1.r14/1       →      2.2.r14/1
    run n15  1.r14/1       ⇒      12.r15/1
    run n1   5.1.r14/1     →      @12
    run n3   5.3.r14/1     →thru  2.1.r14/1
    run n2   5.3.r14/1     →      @12
    run n4   5.4.r14/1     →      @12
    run n9   9.1.r14/1     →in    9.2.r14/1
    run n12  11.1.r14/1    →with  11.2.r14/1
    run n10  11.1.r14/1    →      @12
    run n11  11.1.r14/1    →in    14.r14/1
    run n7   12.1.r14/1    →with  12.2.r14/1
    run n6   12.1.r14/1    →thru  5.2.r14/2
    run n8   12.3.r14/1    →in    9.1.r14/1
    run n5   5.1.r14/2     →      @12
    run o1   12.r15/1      →that  P8
    run p1   1.1.r16/1     →      @0
    run p2   1.1.r16/1     →for   1.2.r16/1
    run p3   12.r16/1      →thru  6.r16/1
  lap  l2 ⊳ l1
  lap  m3 ⊳ m2
  bind K1 i6 i7 → 3.r9/1
  mem 1: r4/2 → pith
  mem 14: r13/1 → pith
```

---

## 5 · LEXICON ADDITIONS

### 5.1 Orrowen (`wf7/lexicon_orrowen.tsv`, appended)

| id | Orrowen | pos | Sense | Derivation (by the lexicon's own rules) | Dry cut |
|---|---|---|---|---|---|
| O2858 | ***hos eth ullen*** | phr, adv | by turns; the one and then the other (two voices, or two inks, taking a telling in turn) | a set phrase of three canon or tier-3 words: *hos* "one" (\*hos-) + *eth* "and" (\*eθ-) + *ullen* "other, of that one" (*ull* + *-en*, \*ull-). The pair's antiphony (orrowen_v2 §3.9, item 5) in three small words | `%h , letters: u.l.l.e.n` (*eth* is mortar: the wedge stands for it, D2) |
| O2859 | ***cadh et tolm hosast*** | phr, v | begin (a work, a tale, a telling): "lay the first stone" | a set phrase: canon *cadh* "lay" (\*kað-) + *et* + canon *tolm* "stone" (\*tolm-) + canon *hosast* "first" (*hos* + *-Ast*). The Shoreland metaphor "to tell a tale is to lay a course" (orrowen_v2 §5, *cadh trenn*). Used where the reserve *mosk* would sound like the Creed's *nath mosk* | `@cadh @tolm @hosast` (TRENN+still 43, TOLM 1, FORE 328) |

Both parse clean in `orr_analyze.py`, and `lex/selfcheck.py` passes over the whole lexicon (every entry, 0 with a problem). No root was coined; every other word of the frame was already in the lexicon (among the tier-3 and reserve words it uses: *hebbet* gift, *grik* pick up, *tuss* dust, *parow* ward, *maver* need, *nynth* water, *niss* slowly, *pynt* quickly, *femm* touch, *nafedh* never, *nayalat* nothing, *rellorat* marked, *nahlennet* unmended, *mesk hemm sost* the eldest wood, *Gebb et Pard* and *Hebbet sa re yal kethet hos clem*, the two titles).

### 5.2 The grain (`wf7/grain_v2.md`, new §21.7, with its `compounds` block for the validator)

| Compound | Means | Soft reading | Derivation | Where in IV.4 |
|---|---|---|---|---|
| `HULL+BREAK` | the thunder-tongue: Seilrhass itself, "bough-thunder" | *seil·rhass* = **Seilrhass** | HULL *seil* "a bough" + BREAK *rhass* "storm; thunder; a crack": the canon's own analysis of the name (mystaeri_spec §1) | ring 7, "in the thunder of his own tongue" |
| `DEEP+WOUND` | a deep wound; a cut that went deep | *eir·thaess* | DEEP *eir* "deep" + WOUND *thaess* "struck; the bark splits" | ring 12, "went deep" |
| `DEEP+HOLD` | hold long; keep long | *eir·thein* | DEEP *eir* "long" + HOLD *thein* "hold; know" | ring 14, "No one held us so long, until you" |

No sign was added. Every other ligature is already in §9.1, §18 or §21.3 (`BOND+SQUARE` Aelrhen, `TAKE+SAIL:cloth` a net, `SIT+WOOD` a bench, `DOOR+STONEFOLK` the host, `HOUSE+OVER` a roof, `BOND+MOUTH` a promise, `BOND+WORD×3` a sentence, `DEEP+LIVE` a long life, `STONEFOLK+LIVE` a shore-man's life, `DEEP+ROAD` the long road, `DEEP+SQUARE` the mountain, `AXE+WOOD` timber, `DEEP+WOOD` the old wood, `TRUE+HOLD` believe) or reads truly part by part (`NEW+EARTH` the green world, `EDGE+BLOOD×3` kin from the edge, `HOLY+WOOD` holy wood, `GIFT+BLOOD` giving blood, `BLOOD+GO` blood flowing).

### 5.3 Files

- `wf7/pilot_IV4.md`: this document.
- `wf7/pilot_IV4/IV-4.gn2`: the leaf in knowing form, with the English of each sentence as a comment (the source).
- `wf7/pilot_IV4/IV-4.canon.gn2`: its canonical GN v2 (§4).
- `wf7/pilot_IV4/headnote.txt`, `headnote.tokens`: Seren's frame, romanised and as leaf-hand tokens.
- `wf7/pilot_IV4/cells.py`: finds the self-consistent cells list of a knowing-form round from the §4.2–4.5 geometry.
- `wf7/pilot_IV4/grain_add.md`: the text appended to `grain_v2.md` as §21.7.
