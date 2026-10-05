# The Epilogue, the Book of Knowings and the Last Note: read with Jack's eye

*A critique of `wf11/drafts/g11.md`, set against `voice_v3.md` §10, `craft.md` §8, the model leaves (`samples/I1.md`, `IV3.md`, `IV4.md`, `I1_plain.md`), `memory_theme.md`, R6b's Epilogue and Knowings entries, and the sibling drafts these leaves pay (g01, g02, g03, g04, g07, g09, g10). Line numbers refer to g11.md. Scratch counts and the sketch are in `critique/_g11j/`.*

---

## 0 · Verdict

**The Last Note is nearly done.** It is the quietest leaf in the Book, as R6b asked. The lamp burns down a finger's width, the three words land plain, and *I think I have read them. I say I think.* closes it. *I said not so. I said that I knew not.* quietly mirrors Brenn's *I said not that it was so.* That is Seren's play at its best. Two faults remain: it opens on a résumé, and its sub-dateline gives the ending away (§1.6).

**The Book of Knowings is nearly done.** The prose is in Seren's voice: the wet stone, ring on ring, the mallet-haft, and *Every one have I set down, and not one of them did I know.* The table is verbatim and the arithmetic is right (7 + 8 + 8 + 8 + 7 + 8 = 46). It needs three small mends and one move (§2, items 14–17).

**The Epilogue is not done, and Jack would send it back.** Its bones are right, and some of them are better than v2.0's:
- The leaf's question is planted in its first sentence, *there is none now to know the wood for me*, and paid by *It was cut so that one could read it alone.*
- *out of the grey came a small grey boat* rings IV.3's first sentence of story.
- *If ye doubt the tale, go and look at the dust* turns I.4's refrain.
- *stoppeth … stopped* plays as the guide asks.
- The *Burn it* refrain turns: the warden's order was obeyed, Harl's temper was not, and this brand is quenched.

But the leaf is delivered as a roll of payoffs. The writer's own note says so: *about thirty-five of v2.0's elements … Each one now gets a single line.* That is the fault g10's critic named in VI.3 ("a ledger of payoffs in white space"), and it is worse here because this is the ending of the whole Book. On top of it sit five more faults:
- the custom's ghost is still on the shingle;
- the climax is a document rather than a deed, and the facing leaf does not face I.1;
- three explanations stop the scene at its moments of wonder;
- the tail stacks four endings;
- one sentence carries two *-eth* forms.

Every fix below uses the draft's own words, or words already in the Book. The sketch in §6 applies all of §1 and counts **898** words of tale proper (ceiling 900).

| Measure (count_v3.py on the split leaves) | Epilogue as handed in | Sketch (§6) | Models |
|---|---|---|---|
| Tale proper | 891 | 898 | I.1 1,075 · IV.4 868 |
| Paragraphs in the tale proper | 47 (19 words each) | 42 | I.1 36 (30 words each) · IV.4 28 (31 each) |
| **Narrative paragraphs that are one sentence** (speech, songs and liturgy left out) | **22 of 39 (56%)** | 12 of 31 (39%) | I.1 10% · IV.3 24% · IV.4 33% |
| Mean sentence / under 10 words / over 30 | 11.7 / 42% / 0 | 11.2 / 45% / 0 | 9.9–11.3 / 43–55% |
| *-eth* forms | 6 (two in one sentence, line 114) | 5 (none doubled) | 1–7 |
| Words after the half-Title, through the last line before the liturgy | 223, in 9 paragraphs (four of them closes) | 221, in 7 paragraphs (two closes); every beat there is must-survive, so the gain is in shape, not length | `craft.md` §2.1: turn and cost about 100, close under 50 |

Knowings (prose and table, without the Last Note): 890. Last Note: 260 as handed in, 252 in the §1.6 rewrite. The two together sit well under the 1,200 ceiling.

---

## 1 · The worst problems, with rewrites

### 1.1 The Epilogue is a roll of payoffs, not a tale (lines 13–116)

**What is wrong.** Read it aloud and it sounds like a drumbeat of single lines: *{{Halyna}} are gone.* / *It was the last of his half.* / *Into that winter went he in a plain grey cloak.* / *This is mine.* / *It was the same child.* / *Merrick laid his hand on its gunwale.* / *No one took the fire…* / *Last went I down…* / *By its stem I knew the boat…* / *It had gone home…* / *I knew the bite.* / *Twice had I held the lamp…* / *There the cutting broke off…* / *I have not gone down to look.* / *Grief is an inheritance…* / *Over the one grave…*

The guide allows four to eight great lines alone on their paragraphs in a tale (voice §3.4). This leaf has twenty-two narrative paragraphs of one sentence. When every line stands alone, none of them is great. The hearer cannot tell the strike from the inventory. This is Jack's "clinical" and "doesn't build" in a new form: the v2.0 run-on chain has been replaced by a chain of white space. It reads like an index to the Book's last pages.

The proportions are wrong too. The approach and the halt (lines 48–98) are told at roughly the same pace as the grief litany before them and the tail after them. Nothing slows down. There is no held moment. The draft cut the two that v2.0 had on the shingle:
- the soldier standing *a while in the rain with the brand in his hand*;
- Seren reading the stone *out to them* on the shingle.

**The fix.**
1. **Let about eight lines stand alone as great lines:** *{{Halyna}} are gone.* · *This is mine.* · *It was the same child.* · *Merrick laid his hand on its gunwale.* (paired with the line before it, as *His men obeyed.* / *We obeyed.* are paired) · *I knew the bite.* · the half-Title · *I have not gone down to look.* · *What we will send back…*
   - A few other one-sentence paragraphs may stay where they sit against speech, or serve as the aftermath of a strike. Examples are *There is none now to finish it…* after the two inks' lines, and *Twice had I held the lamp…* after the bite.
   - The sketch keeps twelve one-sentence paragraphs (39%). That is still above the models' 10–33%, and it should not go higher.
2. **Fold the rest into breaths**, two to five sentences each, the way a speaker says them:
   - *It was the last of his half. Into that winter went he in a plain grey cloak.*
   - *It had gone home, and it had come home. In its bow…*
   - *There the cutting broke off, and its last stroke is sharp yet. Our cloak he never saw…*
   - the mason's knowledge of the hand joins the stone paragraph.
3. **Give back the held moments, and slow down at the halt:**

> *No man took the brand from the soldier. A while he stood in the rain with it, and then he quenched it in the sea.*

That replaces line 62. It costs nine words, and it gives the leaf its weather: thin rain → *stood in the rain with it* → *The rain had stopped*. That is the breath before the bite. Now the one object in the scene (the brand) has a moment of its own before it goes out. Then the reading aloud (§1.3).

### 1.2 The custom's ghost is still on the shingle (line 50)

> *The old ship-masters would not go down, for their fathers had told them of the boat that cometh for you. "Burn it," said one, and his voice shook. A soldier ran for fire.*

The orchestrator allowed rumour-born fear, so this is not a breach of the letter. It does keep the shape of the thing Jack struck out:
- a *for* of motive at the crisis, which `craft.md` §8 Q5 says to cut;
- a handed-down belief about grey boats (*their fathers had told them*);
- a call to burn that follows from it.

Put those three together and a reader hears a custom by another name. It is the "invented lore that explains a deed" which Jack said makes a scene "less impactful, not better". IV.5 already gives the whole reason the masters fear a grey boat: Daveth on the spar, two boats grown to twenty, *the boat that cometh for you when ye die*. The Epilogue does not need to say it again. Let the body show the fear, and leave the why dark.

**Rewrite:**

> *The old ship-masters stood at the head of the shingle, and came no further. "Burn it," said one. His voice shook. A soldier ran for fire.*

*Came no further* is the warden's posture at his own door (*▒▒▒▒ stood within, and came no further*), set down with no comment. That is Seren's mirror: frightened men at a threshold, and this time children walk past them. Merrick's deed then breaks the posture (§1.4). Keep option (i), the fire and the quenched brand. The three *Burn it*s now turn as a refrain should: the warden's was obeyed, Harl's was answered, and this one is put out in the sea. Option (ii), no fire at all, would lose that.

### 1.3 The climax is a document, not a deed, and the facing leaf does not face (lines 74–98)

The half-Title is the climax of the whole Book. In the draft it arrives with no human act around it:
- the stone is described;
- the hand is described;
- the bite is known;
- the letters are read *with mine eyes*;
- then a native block, an HTML marker and an italic line.

No one does anything. v2.0 had *There upon the shingle, with the children close about me, I read it out to them*. That beat was cut, and it is the one that makes this a scene.

Restore it. It also does the work this leaf exists for. The Epilogue is bound facing I.1, and the reader will see the two leaves side by side. In I.1 Kael *turned to the ward and read it out*, after *No man in the ward spake*. Let Seren's climax rhyme with Kael's across the spread, without a word of comment:

> *No one on the shingle spake. The rain had stopped, and the tide drew back with a long sound.*
>
> *I knew the bite.*
>
> *Twice had I held the lamp to that chisel: under the new capstone, and across this stem.*
>
> *It was cut in our own letters. I laid not my palms on it. I read it with mine eyes. It was cut so that one could read it alone. There on the shingle I read it out to the children.*

Four further mends make *I knew the bite* land as the moment where the two climbs meet. That is the moment the reader learns the Last Carver cut our Title with {{Halyna}}'s own chisel, the winter they died.

- **Plant the chisels in the bow-line (line 74).** VI.3 laid them there (*Last they laid by it their two chisels*), but the Epilogue never mentions them. Without them, *I knew the bite* is a riddle for anyone who does not hold VI.3's last page in mind. Write: *In its bow, where we laid the green sliver and their chisels, lay a stone.* That is three words, and then the reader puts it together alone.
- **Fix the antecedent (line 84).** *Twice had I held the lamp to it* reads as "to the stone". Write *to that chisel*. The Plain twin already has it right: *I'd held the lamp for that chisel twice*.
- **Drop the maxim before the moment (line 78).** *No two chisels leave the same bite.* explains the recognition just before it happens. That is the "rite told before it is done" fault, in small. II.1 has already taught *bite*, with Halvard's thumb in his fathers' bite. Cut the maxim.
- **Give back *set before memory* (line 104).** v2.0 had *the word* the, *set before* memory. The draft has only *the*. The Last Carver's one wrong word sits on *memory*: the enemy, cutting our Title, put an extra word before *memory*. That is the memory theme felt at the Book's peak, without a word of preaching. Write: *One word is in it that our Title never had:* the, *set before* memory.

### 1.4 Explanation at the moment of wonder (lines 36, 58, 102)

Each of these stops the tale to tell the reader something.

**Line 102, the Last Carver.** The draft has:

> *Our cloak he never saw, for he never sailed, but what the hulls saw went home through the roots, and there he learned our letters.*

That is a *for … but … and* chain of 24 words, set straight after the climax, which is the place the sentences should be shortest. It also decodes the facing native leaf. The native English, two inches above it, already says *What the boughs saw went home through the roots, and the groves held it*. Voice §5 says neither leaf may explain the other, and the gap belongs to the reader. Keep Seren's guess, and leave the how dark:

> *There the cutting broke off, and its last stroke is sharp yet. Our cloak he never saw, for he never sailed. Yet our letters he learned. The Last Carver I call him, for I think that when he cut this there was no other.*

**Line 36, the Covenant.** The draft has:

> *Now I know the Covenant of Completion: God taketh not the one…*

A doctrine named, a colon, and its definition: that is the history-book voice in one stroke. II.3 (g04) planted the withholding: *Ye will understand it when it is yours to understand.* Pay that instead, and let the old saying arrive as her own understanding:

> *I went not with {{Halyna}}. Alone, they said once, I could go where they could not, and carry this Book on. I understand the Covenant now, as they said I would. God taketh not the one without leaving the other a work to do.*
>
> *This is mine.*

Two smaller mends in the same passage:
- *{{Halyna}}* replaces *them*. *I went not with them* comes straight after the Captain's paragraph, and the first reading of *them* is uncertain.
- *This is mine.* now carries three senses at once: the work, the understanding, and the Book.

**Line 58, Merrick.** The draft has:

> *Then down came Merrick, slowly. His father came home on a spar.*

The second sentence is a register entry: a fact, bolted on. The plant that pays here is a deed. In IV.5 (g07) Merrick turns his face from the sea when a hull burns, and does so first. VI.3 (g10) repeats it: *Six winters had he turned his face from the sea, each time a hull burned.* The man who always turned away now lays his hand on the boat. Use the deed:

> *Then down came Merrick, slowly, that had turned his face from every hull that burned.*
>
> *Merrick laid his hand on its gunwale.*

With that, *Never had a ship-master laid a hand on a grey boat* (line 58) can go, because the deed says it. That saves the words for §1.1's brand.

### 1.5 The tail stacks four endings, and one sentence carries two *-eth* forms (lines 102–116)

After the half-Title, the draft ends four times:
1. *I have not gone down to look.*
2. *Grief is an inheritance, and it is paid out to the children.*
3. *Over the one grave the torn cloak flieth yet, and the sea hath not finished.*
4. *What we will send back, I know not. I know only that it must be sent kneeling.*

That is the "stacked endings" fault on the never-list (`craft.md` §6). Every one of these lines is must-survive, so none can be cut. The fix is to stop giving each its own close. Fold the inheritance, the cloak and the sea into one paragraph that ends on a picture, then give the saying the last word, as `craft.md` §2.1 asks (a picture, then the teller's close).

Line 114 also has *flieth* and *hath* in one sentence, which breaks the cap in voice §1.5: one *-eth* form to a sentence. Splitting the sentence fixes both problems:

> *Ere that spring was out the staff was gone from the gatehouse. Where it leaned there is a clean stroke in the dust of seven winters. If ye doubt the tale, go and look at the dust. I know* the stair that goes no more.
>
> *I have not gone down to look.*
>
> *Grief is an inheritance, and it is paid out to the children. Over the one grave the torn cloak flieth yet. Below the wall the sea hath not finished.*
>
> *What we will send back, I know not. I know only that it must be sent kneeling.*

*I know the stair* (line 108) is orphaned now that the law of the staff is cut. Five words give it its key with no gloss: *the stair that goes no more*. That phrase is I.4's cradle-rhyme (g03, line 16), quoted in italic, so its *goes* stays outside the dial. The rhyme was handed down to the children, and now it points the way to the Captain's laid-down staff. That is memory theme 3, felt.

### 1.6 The Last Note opens on a résumé, and its sub-dateline gives the ending away (lines 167–175, 187)

- ***Laid last, the night after the reading.*** tells the hearer, before the leaf begins, that the stones were read. *I think I have read them* then lands as something already known. A headnote "never holds the ending" (voice §6). Write: ***Laid last of all the leaves.***
- **The first sentence of story is the stones' provenance:** *cut at the feet of the black pillars, and carried off with the timber, and sold. Three generations they hung…* Voice §3.5 says never to open on a résumé. The question of this leaf (will anyone ever read them?) is the child's, so open on the child.
- **The provenance belongs after the strike.** There it becomes Seren's litany that ends on the wrong thing, and memory theme 2 (forgetting brings ruin) is felt at the exact moment the plea is finally read. It is never said.
- **Line 187:** *the quay laughed* drops the echo. IV.3 and IV.5 both say *the shore laughed*. Keep their word.

**Rewrite** (252 words of tale proper, against 260):

> ***Laid last of all the leaves.***
>
> *"Hold the stone, Seren."*
>
> *On the first night of this winter a child at the front asked what they say, the three grey stones over this hearth. In the havens the answer was ever that they said naught, and so was I answered when I was small. I said not so. I said that I knew not.*
>
> *Every night since, when the hall was empty, I have held the lamp to the lowest stone.* [the draft's paragraph, unchanged, through *And three words of ours I had from Brenn.*]
>
> *Last night the hall was empty…* [unchanged] / *Then I had them…* [unchanged] / [the native block] / ***Stop… Sky… Dying…***
>
> *At the feet of the black pillars they were cut, and carried off with the timber, and sold. Three generations they hung over a harbour-house fire at Eldhythe. Under them the shore laughed at three axemen, home on a spar. On the lowest the ship-masters knocked out their pipes. And no one read them.*
>
> *Here no pipe is knocked on them. I think I have read them. I say I think.*

*Voss who asked carried them up the mountain* can go, because VI.1 packs them. *Here no pipe is knocked on them* now stands as the mirror of the litany (there, pipes and no reader; here, no pipe and a reading), right before the close.

**Optional, sharper:** *Under them a girl laughed at her own brother, home on a spar.* That is IV.5's Elspet and Daveth (*She said it of her brother*). It is more particular than *three axemen*, but it leans harder on IV.5.

---

## 2 · The rest, numbered

**The Epilogue**

1. **Change the Argument (line 3)** to ***What the grey sent back.*** g01's Contents already prints it, and g01's notes say *g11 line 3 must change to match*. *The tellers dead, one scribe left* gives away *{{Halyna}} are gone.* before the leaf opens. `craft.md` §3.5 says the Arguments spoil nothing.
2. **Match the kindness to I.2 word for word (line 40).** g02 has *Tonight I was afraid to speak, and {{Halyna}} laid my two hands on the stone.* The Epilogue's *put my hands* loses both the fear the kindness answered and the *laid* of the Book's *lay / laid* pun. Write: *My first night at this hearth I was afraid to speak, and {{Halyna}} laid my two hands on the stone.* This is memory theme 4: the good of the dead, remembered at their death, in their own gesture.
3. **{{Idrenna}}'s prayer** is on R6b's fixed list for this leaf, and it was cut on the ground that V.7 tells it whole. That ground does not hold. The ledger in `craft.md` §2.2 forbids telling a death twice, not saying a prayer twice. Liturgy is the one thing in the Book that repeats. Here it would turn hard: *one stone of us; and thou wilt not part them*, said over a pair that died in one night and lies under one stone. If the budget allows, put it in front of the outliving line, as one sentence: *{{Idrenna}} prayed over them as over {{Enrella}}: "One cradle they had of thee, and one stone of us; and thou wilt not part them." Old they were when {{Halyna}} were young, and they have outlived them both.* Added to the §6 sketch, it counts 923 (`_g11j/epi_final_prayer.md`). To get under 900 with the prayer, cut *Alone, they said once…* and *A child had answered the green wood…*: that gives 895 (`_g11j/epi_final_prayer_lean.md`). Cutting the I.1 breath mirror as well gives 889. Otherwise leave the prayer in V.7. Orchestrator's call; I lean to the prayer.
4. **The slate-coloured sea** is on R6b's must-survive list and was cut (writer's note, *Small pictures cut*). If the I.1 mirror in §1.3 is not wanted, let the slate take its place in the breath: *The rain had stopped. Grey as slate lay the sea, and the tide drew back with a long sound.* Do not put it in the arrival sentence, where it would crowd the IV.3 echo.
5. **Line 54, *A child had answered the green wood, when none of us could: old Ebba's great-granddaughter.*** The colon-appositive is a register entry, and it sits right in front of the punch, *It was the same child.* Drop the appositive, because VI.3 has just said *Old Ebba was her great-grandmother*. Keep the bridge in eleven words. The bolder choice is to cut the bridge altogether and trust *The first laid both her hands flat on the bow* to recall VI.3's *the girl that went first into the sea*. That saves eleven more words, but risks the first-time reader.
6. **Corlen's refrain needs one Book-wide form.** g05 keeps *"Wait. The sea has not finished."* (*has*, as voice §4 prints it). g08 and g11 write *hath*. The Epilogue's echo only lands if the reader hears the same words. Orchestrator to rule. If *has* wins, line 114 becomes *Below the wall the sea has not finished*, written as a quotation.
7. **The register is thinner here than in the models.** There is no strong past anywhere in the leaf (no *spake*, *wist*, *bare*, *bade*, *sware*), and only a few stock words (*ere* three times, *yet* three times, no *naught*). Most of its archaism is inversion. Seren goes plain at the grave, which is right, but the leaf should not be easier than Brenn's. The §1.3 breath gives back one *spake*. Two other natural slots: *Down came the soldier and bare the brand* (if §1.1's line is recast), and *naught* in the Last Carver passage. Do not force more than that.
8. **The foreword's chest is unpaid.** g01 says *This Book is ink. {{Halyna}} would have it cut in the granite of this hall … when peace is come. Till then it lieth in that chest.* The draft dropped the chest for the budget, and flagged it. At 898 there is no room. If the orchestrator wants it paid, the one line that would earn it, placed before *Grief is an inheritance*, is: *This Book lieth yet in the chest, with the gift and this Stone. Peace is not come.* That gives *inheritance* its object. Pay for it with the prayer (item 3), not alongside it.
9. **The north-lamp child** is dropped here because VI.1 pays it. That is acceptable, but note it for the fidelity pass: R6b lists *the lamp* as must-survive.
10. **Headnote (line 9):** keep. *In the end no knowing of {{Halyna}}'s filled it* is a doom-line, which voice allows. Once the Argument stops saying the same thing (item 1), it no longer spoils.
11. **Fixed matter checked and clean:**
    - *Two at the Gate* is word for word.
    - Both native keys (`legend_stonwryt_halyna`, `legend_stone_epilogue`) are present, with v2.0's English verbatim and no unlock line.
    - The MIXED marker is kept.
    - The half-Title is exact, with its one extra word.
    - *Stone does not translate.* keeps the fixed *-s* form, as g06 does.
    - The liturgy is exact, and the hood comes once, after the Amen, as `craft.md` §3.6 allows.
    - There is no singular *they*, no Christian mark and no contraction.
12. **Seren's own turn (voice §10.8).** Nearly every turn in the draft is inherited from v1.3 or v2.0. They are good turns, but there is none of her own. The §1 fixes give her three, all of them mirrors across the Book with no comment: the masters *came no further*; *No one on the shingle spake*; and *I read it out to the children*.
13. **Strip the WRITER'S NOTES (lines 197–293) before assembly**, as g01 does with its own.

**The Book of Knowings**

14. **Line 142, *I could tell a root from the wall*,** reads as "tell a root apart from the wall". v2.0's commas made *from the wall* a place. Write: *From the wall, in the late Tides, I could tell a root in the time a wreck takes to roll over.* Keep *tell*: it is Kael's pun, and here it means *make out*.
15. **Line 138: put the place back.** *Their shapes I learned by eye,* at the tide-line and in the vault, *long ere I could make out aught else in the grain.* These four words are the only physical place in the Knowings' prose. Without them it reads as a method note.
16. **Line 159: put the *turning for home* back.** *The Last Tide carved no new head, but whole morrows out of heads already cut,* and at the end of each a turning for home. That is eight words, and it is the one touch of the wood's own want in the ledger. It rings VI.3's *"Home."* from the other side, without a word of explanation.
17. **Move the *Burn* paragraph (line 163) to just after the table**, and change its last clause to *I count it not among these.* The main body then closes on its human line, *Every one have I set down, and not one of them did I know.*, instead of on a technical aside about a mason's pack. Then the Last Note follows.
18. **Line 138, *Each I said three times ere I wrote it, and they held*:** *each … they*. Write *and each held*, or keep *they* and change *Each* to *Every name*. This is minor.

**The Last Note**

19. **Line 175, *Since the third winter we have known that…*,** is exposition, but the leaf needs it, and g06 left the sound-writing here on purpose. Leave it.

---

## 3 · The memory theme, as it stands after the fixes

All four items are light, and none is preached.

- **Item 4, the good of the dead:** *I was afraid to speak, and {{Halyna}} laid my two hands on the stone* (item 2); *for he knew*; the dry inks; and their chisel's bite in the enemy's answer.
- **Item 3, the hand-down:**
  - Seren reads the stone out to the children (§1.3);
  - *the stair that goes no more* is a children's rhyme, and it points the way (§1.5);
  - *Grief is an inheritance, and it is paid out to the children*;
  - *This I lay as it was laid for me*, laid by the last one left.
- **Item 2, forgetting brings ruin:** the Last Note's closing litany, set straight after the plea is read (§1.6), together with *so was I answered when I was small*. It is not said anywhere. It is only shown.
- **The peak of the Book:** *the, set before memory* (§1.3). Their one wrong word sits on our word for remembering. Say nothing more about it.

Do not add anything beyond these.

---

## 4 · What must survive the revision

The writer should not lose these while fixing the rest:
- **the spine:** *none now to know the wood for me* paid by *so that one could read it alone*;
- *out of the grey came a small grey boat*;
- *Dry on my table stand their two inks.*;
- *till the wall fall*;
- *Into that winter went he in a plain grey cloak.*;
- *I say both halves alone*;
- *the children parted before me, as water before a keel*;
- *It had gone home, and it had come home.*;
- *the right thing said truly by one that knew not yet how we say it*;
- *stoppeth there because his hand stopped*;
- *We have not yet earned a guest.*;
- the dust refrain turned.

In the Last Note: *I said not so. I said that I knew not.*, the finger's width, and the close.

---

## 5 · The Plain Words companion (`drafts/g11_plain.md`), briefly

`plain_check.py` passes the Plain Epilogue on every row: 85.0%, 13.4% overlap, FK 3.5. Once the Book changes, retell the changed beats again; do not patch them. Carry over:
- the masters who come no further;
- the brand held in the rain;
- the reading aloud to the children;
- the chisels in the bow;
- *the* set before *memory*;
- the folded tail.

Faults of its own:
- **Line 32:** *He wore a plain grey cloak that winter. I didn't go with them.* puts the Captain and Seren in one paragraph, so *them* reads as the Captain. Split them, and name {{Halyna}}.
- **Line 32:** *when God takes one, he leaves the other work to do* reads as "other work" (different work). Write *he leaves the other one a job to do.* Also drop the colon-definition, as in §1.4.
- **Line 44:** *because their fathers had warned them about the boat that comes for you* is the same ghost as §1.2. Cut it.
- **Knowings, line 120:** *known, never read* will stop a twelve-year-old.
- **Knowings, line 137:** *The Last Tide only made plans from old heads* uses *heads* without a gloss. *I've written down all forty-six and didn't know one* mixes its tenses: write *and I didn't know a single one*. *and I leave it out* is vague: write *and I haven't counted it with the rest*.
- **Last Note, line 147:** *In the havens we all heard "nothing"* is muddled. Write *In the havens, any child who asked was told they said nothing. I was told the same.*

---

## 6 · The sketch: the Epilogue with every fix in §1 applied (898 words of tale proper)

*Not canon. It shows that the fixes fit the budget, and how the leaf sounds when it breathes. The dateline and headnote are unchanged. Native blocks are marked in brackets and unchanged. The full counted file is `critique/_g11j/epi_final.md`.*

"Hold the stone, Seren."

I write this alone, in one ink, for there is none now to know the wood for me. Dry on my table stand their two inks.

{{Halyna}} are gone.

In the seventh winter they went in one night, as the Bonded go: Rhyna first, in her sleep, and Halvard ere the lamp was out, for he knew. They lie under the new capstone of the inner gate, in one grave, with one stone, and one name on it. Face down above them are their mark and the Title, where no eye will see them again till the wall fall.

*At the grave sang {{Orvenna}}, Ormund to the comma and Penna the rest:*

> *Stone upon stone, and the stone keeps faith;*  
> *hand over hand, and the hand holds true;*  
> *two at the gate when the grey sails gather,*  
> *two at the gate, and the gate stands through.*

{{Idrenna}}, that were old when {{Halyna}} were young, have outlived them both. Beneath Halvard's name in the lintel of the western stair the stone is smooth.

That night the Captain cut a hand's breadth from his half of the cloak, and bound it over the gate.

It was the last of his half. Into that winter went he in a plain grey cloak.

I went not with {{Halyna}}. Alone, they said once, I could go where they could not, and carry this Book on. I understand the Covenant now, as they said I would. God taketh not the one without leaving the other a work to do.

This is mine.

My first night at this hearth I was afraid to speak, and {{Halyna}} laid my two hands on the stone.

"Hold the stone."

"Hold it, and it will hold you."

There is none now to finish it, and I say both halves alone.

In the seventh spring, on a morning of thin rain, out of the grey came a small grey boat. It ran itself up the shingle, and no one was in it.

The old ship-masters stood at the head of the shingle, and came no further. "Burn it," said one. His voice shook. A soldier ran for fire.

Ere the fire came, the children went down in a crowd. The first laid both her hands flat on the bow. A child had answered the green wood, when none of us could.

It was the same child.

Then down came Merrick, slowly, that had turned his face from every hull that burned.

Merrick laid his hand on its gunwale.

No man took the brand from the soldier. A while he stood in the rain with it, and then he quenched it in the sea.

Last went I down, and the children parted before me, as water before a keel. By its stem I knew the boat: the two halves of the first heart, keyed, and {{Halyna}}'s mark across the join.

[`::: native legend_stonwryt_halyna chip`, unchanged]

It had gone home, and it had come home. In its bow, where we laid the green sliver and their chisels, lay a stone. It was not stone. Or it was stone that had been wood, with the grain yet in it, like the Guest's gift. Myststone the Rivenmen call it, and say it remembereth all. Stone does not translate. But this was never only stone. It had been cut by a hand that learned the chisel late, and learned it well: young by their reckoning, I think, and seasoned by ours.

No one on the shingle spake. The rain had stopped, and the tide drew back with a long sound.

I knew the bite.

Twice had I held the lamp to that chisel: under the new capstone, and across this stem.

It was cut in our own letters. I laid not my palms on it. I read it with mine eyes. It was cut so that one could read it alone. There on the shingle I read it out to the children.

[`::: native legend_stone_epilogue stone`, unchanged]

[`<!-- MIXED … -->`, unchanged]
*In the memory of our home, our families...*

There the cutting broke off, and its last stroke is sharp yet. Our cloak he never saw, for he never sailed. Yet our letters he learned. The Last Carver I call him, for I think that when he cut this there was no other.

One word is in it that our Title never had: *the*, set before *memory*. It is like the Guest's three words, the right thing said truly by one that knew not yet how we say it. I have wondered whether it stoppeth there because his hand stopped.

No one came with it, and perhaps that is wise. We have not yet earned a guest. Yet every night is the inner gate left open, as a guest would find it.

Ere that spring was out the staff was gone from the gatehouse. Where it leaned there is a clean stroke in the dust of seven winters. If ye doubt the tale, go and look at the dust. I know *the stair that goes no more*.

I have not gone down to look.

Grief is an inheritance, and it is paid out to the children. Over the one grave the torn cloak flieth yet. Below the wall the sea hath not finished.

What we will send back, I know not. I know only that it must be sent kneeling.

This I lay as it was laid for me.

*And the hearth said: We remember.*

*And the Captain put his hood back.*
