# g03 · I.4 The Rite of the Cornerstone and I.5 The Naming of the Rivenmen · fidelity critique

*Checked against R6a §I.4 and §I.5 (a)–(h) and §0.1–0.6; R6b's Epilogue and V.5 entries, which pay I.4; outline §7.5, §8 I.4 and I.5, and §10; the reckoning §2.7, §2.8 and its datelines table; v2.0 ll. 435–663; voice_v3 §1.7, §4, §6 and §7; craft rules 5, 18, 19 and 22, §3.5, §3.6 and §4.1; the v2 builder (`wf10/book/build_story_html.py`, which decides where the two inks fall); and the neighbouring drafts as they stand now: the foreword and I.1 in `g01`, I.2 and I.3 in `g02`, II.1 and II.3 in `g04`, III.1 and III.2 in `g05`, IV.5 in `g07`, V.5 in `g08`, VI.1 in `g09`, VI.3 in `g10`, and the Epilogue in `g11`. Line numbers below are g03.md's.*

**Counts.** `count_v3.py` was run on each leaf split out on its own, and it agrees with the writer.
- I.4: tale proper **1,178** against a ceiling of 1,200, with 22 words free. Headnote 30, dateline 6.
- I.5: tale proper **829** against a ceiling of 850, with 21 words free. Headnote 30, dateline 8.

Both are under their ceilings. Neither is 5–10% under, which voice §7 asks for, and so every word put back below has to be paid for. The arithmetic is at the end.

**Verdict.**
- These things are clean:
  - no custom of burning and no echo of one;
  - no Brenn, no warden and no wood leaf;
  - pair grammar;
  - every song and fixed line (one exception, fix 3);
  - both native blocks;
  - both datelines;
  - every R6a (c) picture in both tales.
- These things are wrong:
  - **One element has fallen between this draft and g04 (fix 1).** I.4 sends the setting of the new capstone (*mark down*) and the carrying of the old stone to the niche to II.1. g04 cut its own version of the same paragraph, on the belief that g03 kept it. As things stand, no leaf tells either deed, and the Epilogue's *Face down above them* has nothing planted under it.
  - **One markup loss (fix 2).** Two readings by turns have lost the two inks.
  - **One fixed line archaized (fix 3).**
- The other fixes put back elements of the outline that were cut with no reason given or for a weak one. Most cost three to ten words.

---

## Fixes, most important first

1. **I.4, after L93 (or in L99): the new stone set mark down. MUST.**
   - *What:* put the setting back. There are two ways, depending on the budget.
     - **Preferred (10 words).** Add a paragraph after L93 *Neither of them had mended one stroke.*: **The True Men raised it into the gate, mark down.** If there is room, add the v2.0 reason as well (7 words): *, for that gate is of Rhyna's line.*
     - **Minimal (2 words).** In L99, change *when the stone was set and the tools were cleaned* to **when the stone was set mark down and the tools were cleaned.** This keeps the echo of the founders' leaf (L105), slightly bent.
   - *Why:*
     - Outline §8 I.4, scene 9, and reckoning §2.7 day 14 put the stone's raising in I.4.
     - R6b's Epilogue (e) lists *I.4 (the staff; the mark under the gate)* among the Book's last locks. g11 (l.19) pays it: *Face down above them are their mark and the Title, cut on the night of the Rite.* At present nothing in the Book says the mark was turned down.
     - The writer's notes (L257–261 and L344–345) send this to II.1. But g04 §2 (l.180) says "I.4 (g03) already tells all of it… and the True Men carrying the old stone to the niche", and g04 §5 (l.246–254) ends "g03 does all of these". Neither leaf tells it. Correct the writer's notes to match whichever leaf carries it.
   - *The old stone to the niche.* This is the other half of the same lost paragraph, and it matters less. The foreword (g01 l.97, *Beside me in its niche is the stone, the old capstone*) and II.1 (g04 l.63, *It is in this hall now*) already say where the stone lies. Only the deed is lost: the True Men carried it in on the night of the Rite. If it is wanted, II.1 has 48 words free. Change g04 l.63 to *On the night of the Rite the True Men bare it in. It is in this hall now.* (+10). That is cheaper than putting it in I.4.

2. **I.4, L36–38 and L105–107: two readings by turns with no second ink. MUST (0 words).**
   - *What:* wrap each pair of paragraphs in the reading-by-turns markers:
     ```
     <!-- HALYNA -->

     "This is the Rite of the Cornerstone,"

     "by which a keeper is set over a great work, to raise it and to keep it, till it stand."

     <!-- HALYNA END -->
     ```
     Do the same around *"When the stone is set…"* / *"As a course is laid…"*.
   - *Why:*
     - The draft has rightly cut v2.0's tag *one of them said, and the other finished* (craft rule 19, voice §4: "Never: a tag on every line").
     - Craft rule 19's *After* is "two lines, in two inks, with no tag". The builder gives Halyna's halves the second ink in only two cases: inside `<!-- HALYNA -->` (build_story_html.py l.363–365 and l.469–472), or after a cue paragraph that ends *the other finished:* (l.483–484). v2.0 used the cue. The draft has neither, so both pairs would print in one ink as two quotations with no speakers. That loses the two-voice device that the slate's first line and the founders' leaf are built on.
     - Voice §6 lists `<!-- HALYNA -->` / `<!-- HALYNA END -->` "for a reading by turns", and IV.3 (the sample, and g06) uses it in a stone leaf.

3. **I.4, L97: Jack's dust line, archaized. MUST (0 words).**
   - *What:* **If you doubt the tale, go and look at the dust on it.** Restore *you* for *ye*. *No one hath moved the staff.* before it may stay in HEAVY.
   - *Why:*
     - Outline §10.2 lists *the dust (I.4)* among "Jack's other lines the Book keeps, verbatim". R6a I.4 (d) marks it "Fixed / Jack's, verbatim".
     - Voice principle 7 and §1.7: "Jack's lines … are never archaized." The draft keeps every other §10.2 line of these leaves unarchaized, including the *do*-negations in *He did not like it.* and *We do not fight…*. The dust line is the one exception, and the writer flagged it himself.
     - The Epilogue's *If ye doubt the tale, go and look at the dust.* (g11 l.108) is the refrain turned (craft rule 22). It can keep its *ye*, because it is the turning, not the line.

4. **I.4, L95: why the staff leans in the gatehouse. SHOULD (+6).**
   - *What:* give the law its application. For example: **The staff the Captain leaned that night in the corner of the gatehouse, for his work was the wall and the war.** Then make *He went back to it with his half of a cloak on his back* its own sentence, so that nothing runs past 30 words.
   - *Why:*
     - Outline §7.5 ("The work is the wall and the war, and the gatehouse is the work's heart … Law and humility are both true") and §8 I.4 scene 10 both give the reason. v2.0 had *for a staff does not leave its work, and his work was the wall and the war.*
     - The draft states the law at L40 but never ties it to the corner. A reader sees humility only.
     - The Epilogue's payoff needs the tie: the staff gone from the gatehouse, and *When the work is done, the staff is laid down in it, and I know the stair* (g11 l.108). Without it, the reader cannot see that the war's end is the work's end.

5. **I.4, before L72: {{Idrenna}}'s halves at the anointing. SHOULD (+10).**
   - *What:* put back one short cue before the fixed line: **The one named each oil, and the other its meaning:** Leave the fixed line untouched below it.
   - *Why:*
     - Outline §8 I.4 scene 8 [O]: "One named the oil and the other its meaning". R6a I.4 (b)17 lists it among the beats.
     - Craft rule 19 forbids a tag on *every* line, not one cue at the Rite. The builder keeps another pair's halves in the leaf's own ink (l.25), so for {{Idrenna}} the cue is the only way the reader can know that two voices speak the line.
     - It is also the pair's whole character in this tale, as their *prayer for the dead in two halves* is in I.5 (L177).

6. **I.4, L22: the shaft is never named. SHOULD (+3).**
   - *What:* **At the foot of the shaft, as they told it me, stood a chest of black stone…**
   - *Why:*
     - The word *shaft* is nowhere in I.4. *Halvard went down. She paid out the rope.* and *At the foot* have no stated referent. Only the rhyme's *down where the rope let the first stone go* hints at one.
     - Outline scene 2 has the lip of the shaft where the first builders let their stone down on ropes, and R6a (e) seeds *the shaft and the stair → the Epilogue*. g11's notes (l.438) assume "Seren knows the shaft stair".
     - L99's *sent me down alone* also leans on it.

7. **I.4, L34: no one living can sound the old hand. MAY (+6).**
   - *What:* **At the fire {{Halyna}} read the slates for their meaning, for none living can sound them, a line and a breath and a line…** (or split the sentence).
   - *Why:*
     - Outline §8 I.4 scene 4: "Halyna can read the old hand for its meaning but cannot sound it." That is a story fact (memory theme 2, a thing forgotten), not Hal grammar, which goes to NOTES.
     - The writer's notes (L237) send it to "II.1's headnote and NOTES". g04's II.1 headnote says only *read it me out of the old hand*, and no other draft says it. It is lost Book-wide.
     - It also sets up the Last Note's opposite case, *No meaning sought I there, but the sounds only* (g11 l.280).
     - If I.4 has no room, the II.1 headnote can take *out of the old hand, that none living can sound* (headnotes are outside the budget, and g04's is 37 of 50 words).

8. **I.4, L82: the Title cut under a capstone for the first time. MAY (+7).**
   - *What:* **Beside the vow, for the first time under any capstone, they cut words that are not a vow, copied that afternoon from the cloak, stroke for stroke.**
   - *Why:*
     - Outline §8 I.4 scene 9: "for the first time under any capstone". v2.0 has it.
     - It makes the deed unprecedented, and the Last Carver's copied half-Title in the Epilogue leans on that.
     - The writer's notes do not list it as cut.

9. **I.4, L13: the rhyme's line, back to {{Aldwena}}. MAY (0 words).**
   - *What:* **the rhyme of {{Aldwena}}'s line** in place of *the rhyme of her line*.
   - *Why:*
     - R6a (b)5: "sung over every cradle back to Aldwena". v2.0 has *a rhyme of her line, which runs back to {{Aldwena}}*.
     - In Book order the reader has not yet learnt (g04 l.29) that Rhyna is of {{Aldwena}}'s line. Without it, *the first two keep what the first two know* is not yet a set of directions to Aldwena's chest, and *It was the mark of {{Aldwena}}* (L24) lands as a fact rather than a fulfilment.

10. **I.5, L147: the guild answers *in one voice*. SHOULD (+3).**
    - *What:* **And the whole guild ended it, in one voice, from {{Idrenna}} down to the least child that carried its water:**
    - *Why:* outline §8 I.5 scene 3 ("the whole guild answered in one voice") and R6a (b)7. It is the hinge of the half-and-half motif (§7.1): two lines, two peoples, one voice. L151's *We were one* leans on it.

11. **I.5, L189: the keeps that were raised in this war. SHOULD (+4 to +5).**
    - *What:* for example, **From the east tower ye may see the keeps we raised in this war, along the coast like posts along a quay, a crimson pennant on every one.**
    - *Why:*
      - Outline §8 I.5 scene 8 ("raised in this war and still standing") and R6a (b)18.
      - Nothing else in Book One says these keeps exist. The havens fell, and the Keep stood alone (reckoning §2.8, Year 1). Without the clause, *our keeps along the coast* comes from nowhere, and *a place to go out from* loses what it stands against.
      - The writer's list of cuts drops it as *raised in this war… each still stands*, with no reason given beyond economy.

12. **I.5, L177: the strip comes from the half-cloak. MAY (+1).**
    - *What:* **The Captain bound a strip of his half-cloak on a pike above her.**
    - *Why:* the strip is the refrain that grows (craft rule 22 and §3.6), and what it shortens is *his half*. V.5 Count I (g08 l.104) has *a hand's breadth from his half of the cloak*, and the Epilogue pays *It was the last of his half.* *a strip of his cloak* blurs the object the refrain counts down.

13. **I.5, L141: the Captain at the Naming without the staff. MAY (+12).**
    - *What:* the outline marks v2.0's *The Captain of the Torn Cloak had held the staff for a day, and set it down, as you know.* as "(keep)". The writer cut it as a cross-reference. Craft §4.1 rule 5 supports cutting *as ye know*, but the beat can be shown instead of referred to. For example, after *and Jory at my shoulder.*: **The Captain stood with the companies, and the staff in its corner.**
    - *Why:*
      - R6a (b)6, and R6a (e) *Pays ← I.4 (… the staff set down)*.
      - It also puts the Commander bare-handed among soldiers at his own naming, which is the humility that I.4 closes on.
    - Take this only if fixes 10 and 11 leave room (see the arithmetic).

14. **I.4, L9: the opening formula's quotation marks. LOW (0 words).**
    - *What:* drop the quotation marks: **Hold the stone, Seren. I tell myself so every time.**
    - *Why:* every other Seren leaf now opens on the formula with no quotation marks (g04 l.11, g06 l.11, g07 l.109, g08 l.9, g09 l.9), as the sample's *Give me the stone.* does. I.5's L125 already matches them. The formula is said to oneself, not spoken aloud.

15. **I.4, L40: the law of the staff, said one way Book-wide. LOW, for the orchestrator.**
    - I.4 has *A staff is cut for its work, and leaveth it not. When the work is done, it is laid down in it.*
    - III.2 (g05 l.177) has *A staff leaveth not its work.* and asks I.4, II.1 and the Epilogue to match (g05 l.327 and l.348).
    - The Epilogue (g11 l.108) has *When the work is done, the staff is laid down in it.*
    - The slate's fuller form in I.4 is fine as the source. Either let III.2 quote I.4's clause exactly (*and leaveth it not*), or set I.4 as *A staff is cut for its work. A staff leaveth not its work.* (+3). Choose one form.

16. **Assembly: the line-1 comment and the writer's notes. LOW.**
    - L1's comment (`<!-- g03 · Book One … -->`) and everything from L203 (`---` and WRITER'S NOTES) must be stripped before the leaves are joined.
    - The builder stops on any comment it does not know (`raise SystemExit('unknown marker: …')`, l.390).
    - At the same time, correct the notes at L257–261 and L341–346, which say II.1 carries the setting and the niche (fix 1).

---

## Lost or thinned with no listed reason, and judged acceptable (no fix)

- **I.4:**
  - the guild asleep under the broken beams with the stars between them;
  - Seren watching without calling out;
  - *On the fourth morning*;
  - *for weather* and *and was proud* in the twelve generations;
  - *of the guild* in *The first fathers had known better* (the outline marks the sentence "keep", and its sense survives);
  - *They knew whose chest it was ere ever they opened it* (listed as cut; the native caption carries the identity);
  - *nor wore he the oils past that day* and the mortar on his hands (listed);
  - *the same face* for the new stone's quarry.
- **I.5:**
  - *A people was remade in that ward* (outline "keep"; folded into *neither half would have stood without the other*; acceptable, though if fix 13 is not taken, these 7 words are the next most-wanted);
  - *the people of the riven stone*;
  - *men still say back to me*;
  - *a Mystarch sits, and waits* (the hulls *sat down in the havens* carry it);
  - Ebba's age and biography (III.1 and III.2 in g05, and VI.1 in g09, carry them).
- **The hood after I.5's Amen** is cut correctly (craft §3.6 and voice §6).
- **Stannard's** *It is not the ice I fight for.* is craft rule 18's own *After*, so it is sanctioned.
- **Ebba's** *shall stand … lie broken* is not a fixed line, and it is correct HEAVY.

## Checked and clean

- **The custom of burning.**
  - None in either leaf, and no echo. The only fire is the hearth's (L173).
  - *as men make fast their ropes on the quay at evening* is a picture, not a custom of the coast (voice §4: Voss never gives one).
  - The grandmother's slow-tide saying is given at second hand as a homely saying, with no *old way*.
  - The writer also kept the word *custom* out of both leaves. That goes beyond what Jack's fix asks, since the hearth's tale-laying is approved lore, not the banned kind. But *We made it not* (L109) and *In that ward it began* (L155) keep the sense, so no change is needed.
- **Brenn, ▒▒▒▒, the cross-sign, the tongues' ancestry, the parting of the peoples.** None of them is touched.
- **Pair grammar.**
  - Every {{Halyna}}, {{Idrenna}}, {{Orvenna}} and {{Aldwena}} is written in braces.
  - The verbs are plural or past: *their laps*, *their four old hands*, *their mark*, *the one … the other*.
  - No *he and she*, no *the two of them*, and no singular *they*. *they trusted me* (L7) is the guild. *None of us have* (L179) is plural.
- **Songs and fixed lines, verbatim:**
  - the cradle-rhyme (L15–18);
  - the slate's first line;
  - *I know which of these will hold.*;
  - *He did not like it. He stood there.*;
  - the oils;
  - the staff's description, with *This was the first of them*;
  - *Four hands laid it in two.*;
  - the Title, in its native block and in bold;
  - *The people called him Commander. In his own heart he was still only the Captain.*;
  - *The Commander fought.* / *The Stonewrights built.*;
  - *Not one stone that was not ours. But every one that was.*;
  - *We do not fight because we are right. We fight because our children are behind these walls.*;
  - *Tomorrow we go down to the havens.*;
  - the liturgy;
  - *The hearth waited a breath for Ebba.*

  The dust line is the one exception (fix 3).
- **Native blocks.** `legend_stonwryt_aldwena chip` and `legend_title_capstone line` are v2.0's keys. Their captions and their English are identical to v2.0, with no *unlocked by* line. v2.0 has no PROLOGUE or FACING LEAF markers in these tales, and none were needed.
- **Datelines and the reckoning.**
  - *The first spring of the siege.* agrees with the reckoning: I.4 was laid in the first spring.
  - *The sixth winter, the eve of the going-down.* agrees too: I.5 was laid on the eve of the going-down, at the end of the sixth winter.
  - The days inside the tales match §2.7:
    - the third night after the cry;
    - the fourteenth day, with the first thin sun;
    - Kael's first tale *the next night*, which fits I.1's *the night after the Rite*;
    - the Naming *the week after the Rite*, on day 21;
    - Jory's cairn *near the end of the first winter*;
    - the hulls sat down *this winter*, so that *the last Mystarch* is sayable now and not before (reckoning §2.9).
- **Seeds and payoffs that cross to other leaves:**
  - *Kael stood, for he would not sit* pays I.1's *No, I will stand.*
  - Jory's whistle and the rope on the quay agree with I.3 (g02 l.125–127) and IV.5 (g07 l.75 and l.186).
  - The battle-slates and the outward breach are paid by V.5 Count I (g08 l.98).
  - The myrrh of the road's dead is paid by II.3's Tarnel (g04 l.122) and IV.3's {{Wendhessa}}.
  - Ebba's *a breath before the rest* agrees with the foreword (g01 l.108), III.1 (g05 l.83), V.5 (g08 l.232), VI.1 (g09 l.211) and VI.3 (g10 l.152).
  - *Perhaps* is paid in VI.1 (g09 l.207), and *Every haven is Rivenkeep* in VI.1 (g09 l.281).
  - The strip at Ebba is a clause after Jory's whole first strip (g08 l.106), which is craft's order in the hearth's time.
  - The lamp held at the cutting is what makes the Epilogue's *Twice had I held the lamp to it* true.
  - Two things are open, and fixes 1 and 4 close them: the mark down for *Face down above them*, and the gatehouse corner for *When the work is done…*.
- **The memory theme, lightly:**
  - the rhyme nobody asked about;
  - *we had forgotten them*;
  - the hearth forgotten and found;
  - Ebba remembered by her habit at her grave, and Jory by the rope (themes 2, 3 and 4).
  
  None of it is lectured.
- **The wood.** There is no wood leaf in this group. Nothing in either tale is told from the grain.

## Budget arithmetic, if the fixes are taken

- **I.4 (1,178 of 1,200).**
  - Fix 1 minimal +2, fix 4 +6, fix 5 +10 and fix 6 +3 give **1,199**.
  - With fix 1 preferred (+10) in place of minimal, the total is 1,207. Then find 7 words in the joins. Three trims below give 4 of them, and the writer finds the other 3:
    - *and stood still in the noise of it* → *and stood still in the noise* (L80, −2);
    - *So Stannard knocked* → *Stannard knocked* (L46, −1);
    - *On those slates the walls* → *On them the walls* (L42, −1).

    Fix 9 costs nothing. Fixes 7 and 8 (+6 and +7) go in only if more joins give.
- **I.5 (829 of 850).**
  - Fixes 10, 11 and 12 give **838**.
  - Adding fix 13 (+12) gives 850, which is the ceiling exactly. Take fix 13 only if the writer finds a few words to spare elsewhere in the leaf.

**Plain Words.** Neither twin is in this draft, and the draft says so. That is outside this check, but the leaves cannot be built with the three tabs until the twins exist.
