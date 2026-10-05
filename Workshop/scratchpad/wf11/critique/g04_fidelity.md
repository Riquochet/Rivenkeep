# g04 · FIDELITY CRITIQUE · Book Two heading, II.1 Of the Keep That Was Forgotten, II.3 Of the Bonded and the Theoliths

**Checked against:** R6a §0 and its II.1 and II.3 entries · outline §4.2, §5.3, §7.2, §8 (II.1, II.3), §10 · reckoning §2.7 and §2.8 · cast.md · puzzle.md · `wf10/book_v2.md` 667–853 · v1.3 465 · the neighbouring drafts each leaf hands off to or leans on: g01 (the foreword), g02 (I.2), g03 (I.4), g06 (IV.1 and IV.3), g09 (V.7), g10 (VI.3), g11 (the Epilogue), and the IV.3 sample.

**Verdict.** This is a strong, faithful draft. There is no trace of the burning custom. Every one of Jack's lines is word for word. The pair grammar is clean, and the native key and caption are exact. The flaws are of one kind. In several places the writer's notes say a beat lives in another leaf, and it does not. Two handoffs broke between g03 and g04, and one broke between g01 and g04. Three beats that later tales lean on were cut as "doctrine".

**Counts (count_v3.py, re-run on each leaf split out alone; these match the writer's table):**
- **II.1:** 752 words against a ceiling of 800 (6% under) · headnote 37 · dateline 6 · *-eth* 2 · no sentence over 30 words · thirds 14.1 / 10.4 / 10.7.
- **II.3:** 1,140 words against a ceiling of 1,200 (5% under) · headnote 48 · dateline 7 · *-eth* 6 · no sentence over 30 words · thirds 10.8 / 9.7 / 11.4.

**After every fix below** (I applied them to scratch copies in `critique/_g04f/` and counted again):
- II.1 comes to **777** (2.9% under the ceiling) and II.3 to **1,181** (1.6% under). Both ceilings still hold.
- Both leaves now sit inside the 5–10% aim, not under it. That is the cost of putting back beats Jack likes. The ceiling is met.

---

## FIXES, most severe first

**1. II.1 · line 63 · Put back the True Men carrying the old stone into the hall, and "when the Rite was done". At present no leaf in the Book carries this.**
- **What.** Replace *It is in this hall now.* with:
  > *When the Rite was done, the True Men bare it into this hall, and laid it in the niche of the hearth-wall.*

  Then keep *Tonight it is under my two hands. Whoso holdeth it…* as it stands.
- **Why.**
  - The two writers each handed the beat to the other:
    - g04's notes (§2, Folded, and §5) say I.4 (g03) "already tells all of it… the True Men carrying the old stone to the niche".
    - g03's notes (lines 257–261 and 344–345) say the opposite: these beats were "moved to II.1", which "must carry… the old stone carried into the niche".
    - Neither draft has it. `grep niche` finds it only in the foreword, where it has no carriers and no time.
  - **"Other hands act" is a standing rule.** The outline's §5.3 deed table gives "carrying the old stone into the hall" to **the True Men**.
  - **Outline II.1 scene 10** lists it. So does R6a II.1 (b)18.
  - **The reckoning (§2.7, day 14)** dates the stone's setting in the niche to the Rite. The hearth's first tale, I.1, is laid on night 14 or 15 with that stone in hand, so the clause also keeps the clock.
- **Optional.** g03 also handed over *the raising of the new stone, mark down, for the gate is of her line* (outline §5.3: "Halyna set it (the gate is Rhyna's line's)"). I.4 now has only *when the stone was set*. If the words can be spared, add it here: *{{Halyna}} set the new stone in the gate, mark down, for the gate is of Rhyna's line.* That is about 17 more words, and II.1 would still be under 800. Alternatively, the orchestrator gives it back to I.4 as one clause after *cut their mark and their vow under the new stone*.

**2. II.3 · line 96 · Put back the rule that no other pair may cut or break a pair's mark.**
- **What.** After *a name for the mouth, and a mark for the stone.* add:
  > *No hand but theirs may cut it, and no other pair will break it.*
- **Why.**
  - Outline §7.2 makes this a lock: "no pair ever cuts or breaks another pair's mark". R6a II.3 (b)7 lists it.
  - The writer folded it on the grounds that "the ash scene carries the mark's sacredness". But the ash scene says nothing about *other* pairs.
  - Three later leaves lean on the rule:
    - the foreword (g01 line 112): *till {{Idrenna}} gave leave to break it*;
    - IV.3's native caption, *the seal of Brenn's bundle, as it was broken*, which is {{Wendhessa}}'s mark broken by another pair;
    - V.7 (g09 line 39): *Theirs is the only mark in the annals that one hand finished.*
  - Without this sentence, "leave to break" has no law behind it.
  - Cost: 13 words.

**3. II.3 · line 124 · Say outright that every scribe before Seren was of a pair, and that a pair's book went into the vault when the pair went.**
- **What.** Replace *The books of the bonded scribes went into the vault behind them, and a book that none telleth is but ink.* with:
  > *Every scribe before her was of a pair, and when a pair went, their book went into the vault behind them. A book that none telleth is but ink.*
- **Why.**
  - g04's notes (§3, Folded) say "The foreword says both". It does not.
  - The g01 writer folded the line *into the question* and wrote that **"II.3 must say it"** (g01 notes, lines 347 and 392). The foreword now says only *Why the Book is in such a hand, {{Halyna}} tell the children in its place.*
  - So II.3 is the leaf that must answer it.
  - Outline II.3 scene 13 marks the line *keep*, because "it is why an unbonded scribe matters". As the draft stands, *behind them* reads as a place rather than a death.
  - Cost: 7 words.

**4. II.3 · line 88 · Put back the guild's keeping of the faith.**
- **What.** Change *No mother nor father ever refused it.* to:
  > *No mother nor father ever refused it, for the guild kept the faith of the land as it kept its walls.*
- **Why.**
  - Outline II.3 scene 2 lists "the faith kept with the walls". So do R6a II.3 (b)4 and v1.3 465 (*kept the faith of the Shorelands as they kept its walls, and taught it in the temples they raised*).
  - The writer's reason for cutting it ("I.2 carries the creed") does not hold. I.2's creed is *Build, do not destroy*, which is a different element.
  - This clause is what makes two later beats natural:
    - IV.1 (g06 line 95): *The temples were mended, and men climbed the worn steps of our guild-halls again for counsel.*
    - IV.3: Brenn's words were taken down by {{Wendhessa}} *of the guild at Eldhythe*.
  - *Faith* is not a Christian mark (voice §2.4 allows *God*, and this is the land's faith). Cost: 12 words.

**5. II.1 · line 25 · The coin is struck by master-pairs, not by the havens.**
- **What.** Change *The havens struck their coin under such marks: trust, sealed in stone.* to:
  > *The master-pairs of the havens struck coin under their marks: trust, sealed in stone.*
- **Why.**
  - Outline §7.2, the puzzle's *The Havens* row ("Bonded master-pairs mint coin under their marks") and v2.0 all give the coin to the pairs.
  - VI.3 (g10 line 108) lays *a Stonwryt coin, part gold and part black stone* in the boat as the Shore's dearest gift. That works only if the coin is a pair's mark-coin, not a city's.
  - Jack's *trust, sealed in stone* stays word for word.
  - VI.3 carries *part gold and part black stone*, so the writer was right to leave it there.

**6. II.3 · line 122 · Put Seren's lamp into Rhyna's mouth, as the writer's own note says it already is.**
- **What.** Change *Seren, that is writing this down, is our third.* to:
  > *Seren, that held the lamp this morning, and is writing this down, is our third.*
- **Why.**
  - g04's notes (§3, Dropped, and §4) say the lamp stays "in the headnote and in Rhyna's *that held the lamp*". The text has it in the headnote only.
  - R6a II.3 (e) seeds *Seren's lamp at a sealing → the lamp motif*.
  - With the invented custom rightly gone, the bare fact does the work. The unbonded child held the light at a rite she will never have. It also answers the small girl's question at line 86 without a word of explanation.
  - Cost: 6 words.

**7. II.1 · line 31 · Name the black chest, so that II.1 pays I.4.**
- **What.** Change *laid the things of the Keep in order in its deepest vault, the first staff among them* to:
  > *laid the things of the Keep in order in the black chest at the foot of the shaft, the first staff among them*
- **Why.**
  - R6a II.1 (e) and outline II.1 both list *Pays ← I.4 (the founders' annal comes out of the black chest)*.
  - The pay went out with the headnote's chain of custody, which craft §3.2 rightly forbids, and nothing in the body replaced it.
  - The puzzle's First Days row puts the founders' things "in **the black chest** at the foot of the shaft". I.4 (g03) finds them there: the annal, the staff along the floor, and {{Aldwena}}'s mark on the lid.
  - The change also removes a third "vault" from Book Two. II.3 has the scribes' vault, and V.2 has the vault of planks.
  - Cost: 5 words.

**8. II.1 · line 61 · Do not let the cry follow straight on from the turning of the stone.**
- **What (the minimal fix).** Change *Ere the light was off the snow, they rose and cried the guild to its feet.* to:
  > *Ere the light was off the snow, they cried the guild to its feet.*
- **Fuller option.** Put back the element R6a (b)17 lists, at about 11 more words: *They rose, and sat apart in the grass, and spake to no one. Ere the light was off the snow, they cried the guild to its feet.*
- **Why.**
  - *Rose and cried* reads as one movement from the kneel to the cry.
  - But the reckoning (§2.7, day 0) and I.2 (g02) put two things between them:
    - {{Halyna}} sitting apart in the grass, *two elders that sat apart and spake to no one*;
    - the Captain coming down and asking his one question.
  - The writer folded the sitting-apart because "I.2 shows them sitting apart". That fold stands only if II.1 does not then run the two moments together.

**9. II.1 · line 9, the headnote · *of all the words in this Book, those only I have not mended* claims more than the Book allows.**
- **What.** Change it to:
  > *and those I have not dared to mend.*

  This also brings the headnote to 32 words.
- **Why.** The Book holds other unmended words, and later leaves say so:
  - the Captain's Title, of which I.4 says *Neither of them had mended one stroke*;
  - the songs, which are fixed matter;
  - the warden's letter, copied in the roll;
  - the apprentice's hearth-leaf in I.4;
  - Brenn's words, which {{Halyna}} read *as they were written* (IV.3).

  The joke on her mending everyone is worth keeping, but not as a claim that a later leaf breaks.

**10. II.1 · line 47 · Use the cradle-names at the gate, not the pair-name.**
- **What.** Change *At dusk on the day of the banner, {{Halyna}} came under the inner gate* to:
  > *At dusk on the day of the banner, Halvard and Rhyna came under the inner gate*
- **Why.**
  - Outline §4.2 rule 2 says the first mention in every tale must show two people. Rule 7 says that in a scene "the cradle-names and their two hands do the work". This is the leaf body's first mention.
  - The next sentence is *Their names I knew not.* The sealed name {{Halyna}} is exactly what Seren did not know that dusk. v2.0 had *Halvard Stone-Warden and Rhyna of the Inner Gate, he and she together*.
  - The plural *They kneeled…* that follows then has its two.

**11. II.1 · line 37 · Make it clear which word Seren loves, and let using it carry the meaning.**
- **What.** Change *No pair came up to point its mortar. I love that word. The rain found every joint, and after the rain the frost, and after the frost the ice.* to:
  > *No pair came up to* point *its mortar, and the rain found every joint. I love that word. After the rain came the frost, and after the frost the ice.*

  (*point* in italics.)
- **Why.**
  - R6a II.1 (f) calls this "the clearest instance anywhere in Part 1 of what Jack asked for (her love of words), so keep it". That is Jack's note 7.
  - Without the italic, *that word* can be heard as *mortar*.
  - Set beside *point*, the rain clause defines it by use. That is craft §4.2's own model, *No mason came to point its mortar, and the rain found every joint.*, and it is not a lecture.

**12. II.3 · lines 75–82 · The markup: the split opening will not show in two inks.**
- **What.** Move `<!-- MARKED -->` from line 76 to just after the second half:

  ```
  <!-- HALYNA -->
  *With their hands on the stone they began it:*
  "We hold the stone together,"
  "as we hold all things."
  <!-- MARKED -->
  ```

  Or join the halves into one line again, as v2.0 had them.
- **Why.**
  - In the builder (`wf10/book/build_story_html.py`, `Pane.para`), a paragraph inside a MARKED block that has no `**Rhyna.**` or `**Halvard.**` prefix gets no ink.
  - So the writer's "split into two inks" (notes §3) would silently print as two plain lines.
  - Before MARKED, a HALYNA block alternates a/b, as the IV.3 sample's split lines do. The italic cue line is treated as frame and does not use up an ink.
  - The added `<!-- HALYNA END -->` before the Amen does no harm. The builder handles the Amen and *This we lay* by their text, so it may stay.

**13. II.3 · line 71 · The dateline does not name the year.**
- **What.** Change *High summer, the night of {{Enrella}}'s sealing.* to:
  > *The first high summer, {{Enrella}}'s sealing night.*

  That is 7 words. An 8-word alternative is *High summer, the first year, {{Enrella}}'s sealing night.*
- **Why.**
  - The reckoning (§2.8, year 1) lays II.3 in high summer of W1, and it must be year 1: Enrella die in year 4 (V.7).
  - Each model dateline names its year: *The first winter…*, *The third winter…*.
  - Across six winters, *High summer* alone leaves the year open.
  - Note: cast.md lines 79 and 396 say Enrella were sealed "in the first autumn". The reckoning governs, and the draft follows it rightly.

**14. II.1 · line 11 · Put quotation marks round the opening formula.**
- **What.** Write `"Hold the stone, Seren."`
- **Why.** I.4 (g03 line 9) and the Epilogue (g11 line 11) both set it in quotation marks. One formula should have one form across the Book.

**15. II.3 · line 118 · *no sad thing* uses a word on the never-list.**
- **What.** Change *and to us it is no sad thing* to:
  > *and to us it is no grief*

  Or bring back v2.0's beat, *and we two fear it not*.
- **Why.** Voice §2.4 lists *sad* among the false friends (in the old sense it meant *grave* or *steadfast*), unless the sentence fixes the old sense, and this one does not.

**16. Optional, each a few words, each a v2.0 or outline element that is now gone. Take them only if the words are there.**
- **II.3, line 112.** Put back *Two made one.* before *The old masters had a saying for it*. Outline II.3 scene 8 lists it. 3 words.
- **II.1, line 51.** Close the fishers' picture with *and find their fathers' name on her*. That is v2.0's *read upon her bow the name their fathers cut*, and it is what makes *It was their own.* land as a picture. 6 words.
- **II.3, line 88.** *from any hearth* could become *from any hearth, the fishers' huts and the merchants' halls* (R6a (b)4). 7 words.

---

## FOR THE ORCHESTRATOR: claims in the writer's notes that do not hold

**A. "The Epilogue (g11) already matches *beneath the last the stone is smooth*… and *go where we two cannot, alone, and carry this Book on*."**
- Neither is true.
- g11 dropped the lintel line (its notes, line 383) and flags II.1's *beneath the last … smooth* as **an unpaid plant** (g11 §5 item 4).
- g11 has no *where we two cannot*. Its *This is mine.* answers the line lightly.
- Decide one of two things:
  - g11 puts back its 23-word lintel sentence after {{Idrenna}};
  - or II.1's line stands alone as a picture of the forgetting (the quarry no longer worked). It reads that way without a payoff, so no change to II.1 is needed for it.
- The other lines the notes name do match: *till the wall fall*, and *God taketh not the one without leaving the other a work to do* (g11 line 36, word for word).

**B. "I.4 (g03) already tells all of it… the True Men carrying the old stone to the niche."** It does not. See fix 1.

**C. "The foreword says both" (*every scribe before her was one of a pair*; *we two took her to our hearth*).**
- The foreword's own headnote carries the second (*the third of the hearth of {{Halyna}}*).
- It does not carry the first, and g01 asks II.3 to say it. See fix 3.

**D. "Seren's lamp stays… in Rhyna's *that held the lamp*."** It is not in the text. See fix 6.

**E. The semicolon count for II.3 is 2, not 1.**
- One is in the fixed line. The other is at line 92 (*and no more; and no more give we*).
- That is within the cap of two a tale.

**F. *No one living can sound* the old hand.**
- g03 asks II.1 to carry it (g03 notes, line 346).
- Outline II.1 "Must not carry" sends the Hal's reading rules to NOTES, and the draft follows the outline.
- I recommend leaving it out. Puzzle §3 is notes matter.

**G. *a stone that taketh two* (II.1) against the foreword's *It is a stone that two must turn*.** The writer flags these as deliberate variants. Both are fine. Make them one only if you want an exact echo.

**H. The crisis stretch in II.1.**
- In the draft, and after the fixes, the last third (the dusk and the turning) averages slightly longer sentences than the middle third: 10.7 against 10.4 in the draft, 11.5 against 10.5 after the fixes.
- Voice §3.1 wants the crisis stretch to be the shortest.
- The sentences restored in fixes 1 and 8 fall in the last third. Keep them as short as given above. If the writer has a word to spare, the cheapest gain is to split line 55's first sentence at *vow*.

---

## Checked, and holding

- **Burning.** There is no custom of burning and no echo of one in either leaf, nor in the Book heading. The *Fall of the havens* is told without the word *burned*. Every fire in II.3 is the hearth's.
- **Brenn and ▒▒▒▒.** Neither appears, and nothing here leans on either. The quarry-wardens' names cut *into* the lintel (the seed against ▒▒▒▒'s name cut *out*, R6a §0.2) stand at lines 19 and 29.
- **Jack's lines, word for word:**
  - *a vow sealed in living rock, earned by toil and skill* · *trust, sealed in stone* (II.1);
  - *Not all Shorelanders were Stonewrights, yet all Stonewrights were Shorelanders.* · *Separation, God did not permit.* · *When the left hand dies, does not the right one die too?* · *Birth united them; death could not separate them.* (II.3).
- **The founders' vow** is word for word as in the foreword's native block (g01 line 101).
- **The liturgy.** *This I lay…* and *This we lay…* and the Amen are exact. II.3's Captain's hood is rightly dropped (craft §3.6).
- **No songs** belong to these leaves.
- **Pair-names and pronouns:**
  - every pair-name takes a plural or past verb (*{{Idrenna}}, that sit*; *{{Idrenna}} will nod*; *Now are they {{Enrella}}*);
  - {{Halyna}} speak of themselves as *we two* throughout;
  - there is no singular *they*;
  - *husband and wife* is said in II.3 (outline §4.2.5).
- **Forbidden matter.** There is no Christian mark (only *God* and *pray*), no cross-sign, no hint of the tongues' ancestry, no telling of the parting, no contraction and no *Hear how* opening.
- **Seeds that cross to other tales hold:**
  - the jest, the house of one door, and *seldom apart, and never far* (V.7, g09 §5);
  - *a mile apart, and each knew* (D8);
  - the small girl at Della's knee;
  - *some of the old* and *Under one cloak*, against IV.3's annal (*Tarnel did not wake.*);
  - *A net is only knots holding hands* and Tarnel's knot (VI.3, g10 lines 100 and 104);
  - the mark drawn *but once* in the ash, and *A mark is for stone* (VI.3, *the mark that Halvard drew once in the ash*; *The wood took it*);
  - *Harm to one is harm to both*;
  - the Covenant named and no more, paid in the Epilogue;
  - {{Idrenna}} by the door;
  - *It had only been left*, for II.2's home that is air;
  - Seren tracing the mark, for the Epilogue's grave;
  - the chisel-bite, for the Epilogue's *I knew the bite*;
  - *the old hand* the Theoliths taught, which is why {{Halyna}} can read the slates (puzzle §3).
- **Datelines and the reckoning.**
  - II.1's *The first summer of the siege.* agrees with the reckoning.
  - The dusk of the banner, the one column after Glasspire (reckoning B10) and the night of the pass all agree.
  - II.3's season agrees; only the year is missing (fix 13).
- **Markup:**
  - `## BOOK TWO · THE BOOK OF THE BUILDERS` and its italic Argument (*Who we were, and who they were.*) agree with g01's contents and craft §3.5;
  - the `###` titles, the italic datelines and the italic headnotes are in order;
  - `<!-- HALYNA -->` and `<!-- MARKED -->` are present;
  - `::: native legend_stonwryt_halyna chip` has v2.0's caption word for word and no *unlocked by* line;
  - v2.0 has no native block on II.1, and no PROLOGUE or FACING LEAF marker on either leaf, and none is wanted.
- **Invented lore.** The one invented custom, the unbonded holding the lamp at a sealing, is rightly removed. Nothing new has been invented in its place.
- **Halyna discover, Seren writes, other hands act.** {{Halyna}} find the capstone (F1). {{Idrenna}} seal {{Enrella}}. Seren writes. The one deed by other hands that was lost is the True Men's (fix 1).
- **The memory theme** sits lightly:
  - *keeper of the vow… and of the shame* (1);
  - *Forgetting had done what no enemy ever could* (2);
  - *This we lay as it was laid for us* (3);
  - Tarnel's net and his knot before his death (4).
