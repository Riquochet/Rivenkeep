# g02 · FIDELITY CRITIQUE

*Scope: `drafts/g02.md`, I.2 The Cry of the Bonded and I.3 The Captain's Long Breath. I checked it against R6a's I.2 and I.3 entries (§0.1–0.8), outline §8 (I.2, I.3), §4 and §10, the reckoning (§2.7, §2.8, §4, §5 A1, B1, B3), `book_v2.md` lines 263–433, voice_v3 (§1.2, §1.6, §1.7, §6, §7) and craft (§3, §4.1, §4.3, §6). I also read the sibling drafts that pay these seeds: g01 (foreword), g04 (II.3), g05 (III.1), g06 (IV.3), g07 (IV.5, V.1), g08 (V.5), g09 (V.7) and g10 (VI.3). Line numbers are those of `drafts/g02.md`.*

**Counts.** I ran `count_v3.py` on each leaf split out alone (`critique/_g02f/I2.md`, `I3.md`).

| Leaf | Tale proper | Ceiling | Headnote | Dateline | Mean sentence | -eth | Contractions |
|---|---|---|---|---|---|---|---|
| I.2 | 973 | 1,000 | 43 / 50 | 7 / 8 | 11.7 | 3 | 0 |
| I.3 | 839 | 850 | 33 / 50 | 7 / 8 | 10.3 | 5 | 0 |

- Both leaves are within every cap, and the writer's figures are correct.
- The fixes below change the totals by about +5 words in I.2 and +1 in I.3. Both stay under the ceiling. The optional items take I.2 to about 984 and I.3 to about 845.

**Verdict.** This is a faithful pair of leaves. Every song and every one of Jack's lines is verbatim, and there is no trace of a custom of burning. The pair grammar is clean, and almost every liked element is kept. The two biggest problems are:
- the plank in I.3 now contradicts V.1 (g07) and the runners' oath;
- the builder can no longer find the two inks on {{Halyna}}'s halves, which matters most at the cry.

Three smaller fidelity fixes follow. None of them costs a beat.

---

## Fixes, most serious first

**1. I.3, line 167: Hale must carry what he *saw*, not the plank.**
- *What:* *I found a plank in the shallows with marks cut in it. Up past the fires I carried it to {{Halyna}}:*. The second *it* can only mean the plank.
- *Why:*
  - **V.1 contradicts it.** In g07's V.1 (lines 117–121, as in v2.0 l.1568–1572), Hale comes up *from the water's edge* and *said it in three words*. Then *at the turn of the tide {{Halyna}} went down*, and *the men hauled one plank up out of the surf*. If Hale has already carried the plank up past the fires, V.1's whole scene on the shingle cannot happen.
  - **The reckoning contradicts it.** Its §2.7 entry for the night of day 24 reads: *Hale sees marks. Halyna go down on the shingle.*
  - **It breaks Hale's own oath**, sworn sixty lines earlier: *What I saw, I carry. I carry nothing else.* A runner carries words. v2.0 has *I carried them… in three words*.
- *Mend (−2 words):* *…I saw marks cut in a plank in the shallows. Up past the fires I carried them to {{Halyna}}:*

**2. I.2, lines 7–11 and 39–45: the two inks on {{Halyna}}'s halves are lost. This is a markup fix.**
- *What:* The builder (`wf10/book/build_story_html.py`, `Pane.para`) inks Halyna's quoted halves only after a cue: a paragraph ending *the other finished:* or *She began it:*, or one beginning *And he …* and ending *:*. Otherwise it needs a `<!-- HALYNA -->` block. The draft has rightly cut the tags (craft rule 19), but it has put nothing in their place:
  - *"Hold the stone." / "Hold it, and it will hold you."* now has no cue at all.
  - *She began the cry:* and *He ended it, his chisel beside hers:* do not match the cue forms.
  
  So the Book's own device, Seren Two-Inks setting Rhyna's half and Halvard's half in two inks, vanishes at Jack's fixed line, the climax of the leaf.
- *Mend:* use the HALYNA block, as `samples/IV3.md` does for *"We two hold the stone," / "but the words…"*.
  - *Hold the stone:* wrap the two lines in the markers, with no word changed:
    ```
    Tonight I was afraid to speak, and {{Halyna}} laid my two hands on the stone.

    <!-- HALYNA -->

    "Hold the stone."

    "Hold it, and it will hold you."

    <!-- HALYNA END -->

    So I hold it.
    ```
  - *The cry (+1 word):* join the two cue lines into one, so that the halves stand together:
    ```
    She began the cry, and he ended it, his chisel beside hers:

    <!-- HALYNA -->

    "The mortar cries out from the ground. Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end."

    "Rise! Rise! Rise!"

    <!-- HALYNA END -->

    Some tell it that she called and he answered, with a silence between.

    There was no silence.
    ```
    This gives the page what the turn claims. Nothing stands between the two halves, and then *Some tell it… There was no silence.* Inside the block the inks alternate a, b. The block also sets `data-told="halyna"`, which `story.css` does not style, so it does no harm.
  - *If the orchestrator would rather not use the marker on a Seren leaf:* use the builder's own cue forms instead, either *The cry came out of them both. She began it:* (+5 words) and *And he ended it, his chisel beside hers:* (+1), or teach the builder *She began the cry:*. The halves of {{Idrenna}} and {{Orvenna}} need nothing, because another pair's halves stay in the leaf's own ink.
  - *The same gap is in g01*, in the foreword's *"A tale told from one side of a wall," / "is half a tale."*. That one is outside this draft; I note it for the orchestrator.

**3. I.3, line 107: name the runners' stone.**
- *What:* *The first week, our hands on a fallen block by the inner gate, we runners sware the old oath of the havens.* The words *runners' stone* are gone. The writer's §7 says *Brenn's runners' stone at Eldhythe needs no further plant.*
- *Why:*
  - g06's IV.3 (line 121, the judged sample's wording) has Brenn *sworn at fifteen with mine hand flat on **the** runners' stone*. The definite article assumes the reader already knows that runners swear on a stone. I.3 is the only leaf that can teach it.
  - Outline §8 I.3, scene 3, asks for *the runners' stone the runners set in the ward the first week*.
  - R6a I.3 (g) says *"as every haven… had its runners' stone" is needed for Brenn's Eldhythe stone, but one clause is enough.*
- *Mend (+2):* *The first week, our hands on a fallen block by the inner gate, our runners' stone, we sware the old oath of the havens:*
- *Optional (+4 more):* add *…our runners' stone, as every haven had one, we sware…*. This makes the Eldhythe stone exact. I.3 has room for it.

**4. I.3, line 143: the halt line must be plain. Restore *The Captain was standing still.***
- *What:* *The Captain standeth still.*
- *Why:*
  - This is the tale's halt. Craft §3 gives the I.3 halt as *the Captain standing still*, and R6a I.3 (c) lists *"The Captain was standing still."* among the liked key lines.
  - Voice §1.6, the hinge rule, says: *At the halt the plainest word wins… No -eth or -est in a strike sentence.* The draft puts its one *-eth* on the very word that should stand plainest.
  - The present-tense slip of the run (*I run… I stop not.*) is good, and it should end as he arrives. The drop back into the past enacts the stillness. v1.3 has *He was standing still. That is what I remember first.*
- *Mend (+1):* *The Captain was standing still.* The paragraph after it stands as written.

**5. I.2, line 37: the chisels must go up *as one*.**
- *What:* *Each lifted a chisel. Their two chisels took the last of the light.*
- *Why:*
  - The ★ image is two people moving as one body. Outline §8 I.2, scene 6, has *Their two chisels go up as one and take the last of the light*. v1.3 has *went up as one*, and v2.0 has *in the one motion*.
  - *Each lifted a chisel*, alone, reads as two separate acts, which is the opposite of the image. The bow carries *in the same breath*, but the chisels have lost it.
  - g10's VI.3 (line 110) pays the next sentence word for word (*their two chisels, that took the last of the light*), so that sentence must not change.
- *Mend (+4):* *Each lifted a chisel, in the one motion. Their two chisels took the last of the light.*

---

## Smaller and optional

**6. I.2, line 15: the bonded pairs a little apart (optional, +6).**
- R6a I.2 (b)2, outline scene 2 and v1.3 all have *the bonded pairs a little apart*. The draft folds it into {{Halyna}}'s *sat apart*. The fold is defensible.
- But the general picture is what makes *look again. Ye will see two* land, and it gives Enno and Della's *sat down together* a ground to stand on.
- If restored: *…some hundreds of us, with our chisels in our laps, and the bonded pairs a little apart.*

**7. Do not take the writer's offered cuts (§1, last bullet).** Every one of them is a liked element, and both leaves are under their ceilings without them:
- *Every joint we broke over the joint below* pays g01's foreword (*as masons set a course, every joint broken over the joint below*) and R6a (b)16.
- *Some tell it…* is the v1.3 order that R6a (c) asks for.
- *Kael was counting under his breath* is in R6a (b)16 and outline scene 9.
- *I have no better way to say it* is v1.3's Hale (R6a §0.8).
- *and in the hauling slower* is in R6a (b)3.

**8. The HEAVY forms in the writer's §4 table are all safe to confirm.**
- None of *hangeth*, *lasteth* or *sloweth* is quoted in any other leaf. I searched v2.0 and every sibling draft, and only I.3 uses them.
- Kael's mend is not Jack's, and it is not on voice §1.7's fixed list. Voice §1.2 therefore requires *sloweth*, although R6a calls the line "verbatim".
- *It is only a rhyme* matches craft rule 18 and g07's IV.5 (line 75). g08's V.5 no longer quotes it (g08 line 355), so nothing else has to change.
- The creed *Build, do not destroy…* may stand as fixed guild matter. It accounts for two of the three *do*-negations voice allows a tale.

**9. Strip the WRITER'S NOTES before assembly.** `split()` adds any `##` heading that is not in `SEC_IDS` to the current unit. As it stands, everything from line 183 down would be built into I.3.

---

## Checked and clean

- **No custom of burning, and no echo of one.**
  - *Ten havens had burned* and the torches are not a custom. Nor is *the first fire* on this hearth.
  - I.3's *up past the fires* is bare. g07's V.1 now gives the fires their plain cause: *for they hated it, and wood was dear on the ridge.*
  - Jory's tune *that the old ship-masters hate* is plain fear, which IV.5 (Daveth) grounds.
- **Brenn** does not appear. **▒▒▒▒** does not appear either. The only *Warden* in the text is Halvard Stone-Warden's epithet.
- **Pair grammar.**
  - Every verb after {{Halyna}}, {{Idrenna}} and {{Orvenna}} is plural or past tense. There is no *he and she* and no *the two of them*.
  - I checked all 13 *they*, 9 *them* and 4 *their*: none is singular.
  - Enno and Della are not yet sealed, so they rightly have no pair-name.
  - {{Halyna}} have no first-person speech here, so *we two* does not arise.
  - *Husband and wife* is said, as outline §4.2 rule 5 requires.
- **Fixed matter.** I checked these against `book_v2.md` by machine:
  - all three songs, verbatim line for line, eleven lines in all: the masons' chant, *Two at the Gate* and the dawn drill;
  - the cry, both halves;
  - the Captain's question;
  - *with the speed and precision that only Aetherbonded pairs could achieve*;
  - *Not the sword, but the stone.* / *Not the killing, but the keeping.*;
  - the runners' oath;
  - *This I lay as it was laid for me.* and *And the hearth said: We remember.*
- **No muddling lore.**
  - Tarnel's knotting is canon: cast.md, and the same habit in g04's II.3 (line 122) and g06's IV.3 annal. It is memory theme 4, lightly done.
  - *The Captain hurried them not* is a plant for I.3, not lore.
  - The arch and the quarry seam are pictures from Seren's trade.
- **The wood rule** does not apply. These are stone leaves.
- **Seeds and payoffs that cross to other tales still hold**, apart from fixes 1 and 3:
  - the two chisels (g10, VI.3);
  - *Two at the Gate* and the first voice (V.7 I, the Epilogue);
  - Enno and Della hand in hand (II.3, V.7);
  - Tarnel unnamed (g04, II.3; g06, the IV.3 annal);
  - *the Captain who will not hurry* (g09, V.7: *He hurried not, as lamplighters hurry not*);
  - the late hull (V.2, *Wait in grey*);
  - one battery at a time by voice (V.5, V.7);
  - *I ran it.* (g08 and g09: *Hale ran it.*);
  - Wick, youngest and longing to carry a word (g08, V.5 III, which now carries the Title-twice habit whole);
  - Hesk's lamp (g05, III.1, which gives it its origin);
  - Pellow's glass (g05, III.1);
  - Jory, Merrick and the tune (g07, IV.5).
- **Elements.** Every beat of R6a (b) for both tales is present, apart from deliberate folds that are held elsewhere:
  - the gateway aside goes to g01's foreword (*{{Halyna}} turned it over on the day of the banner*) and to II.1;
  - *{{Orvenna}} never raise their voices* goes to g01's foreword;
  - Wick's *Title twice* and his place at the front go to V.5 III;
  - the twenty-four-hour arithmetic is dropped, as the outline asks;
  - Kael's routing paragraph is now shown by deed;
  - *a soldier of the east wall* goes to V.1 and V.5;
  - *I could not have told an hour from a morning* is carried by *faster than I could tell them* and the heartbeat.
- **Datelines** agree with the reckoning.
  - I.2: *after the first assault*, laid on night 25 (§2.7, with fix A in §5 A1).
  - I.3: *in its second month*, which matches the outline and v2.0. It also matches §2.8's *at the end of the first winter*, because Cam 2 is the late winter.
  - Both are under 8 words, in plain italic and not capitals, with no event dates.
  - The B1 fixes are in: *Tonight*, and *It is the guild's word now*. So is the B3 fix: *in those weeks*.
- **Ages** agree with the reckoning and the cast: Seren is 12 (B−12), Enno and Della are 15, Hale is 17 (V.1).
- **Markup.**
  - The `### I.n · Title` headings, the italic dateline and headnote, the songs as `>` italic blockquotes with their frame lines, and the Amen are all exact.
  - `book_v2.md` has no `::: native`, PROLOGUE or FACING LEAF markers for I.2 or I.3, so no key is lost. The only markup problem is fix 2.
