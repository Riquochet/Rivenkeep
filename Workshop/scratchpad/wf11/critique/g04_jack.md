# g04 · Jack's Eye: BOOK TWO's heading and Argument, II.1 and II.3

*Critic: I read this as Jack would, against voice_v3 §10, craft §8, the three model leaves and memory_theme. The source is `wf11/drafts/g04.md`. My trial rewrites, used only for counting, are in `wf11/critique/_g04j/` (`II1_trial.md`, `II3_trial.md`; the drafts split out as `II1.md`, `II3.md`).*

## The verdict

**The heading and Argument ship as they are.** *Who we were, and who they were.* is v1.3's tag. It spoils nothing and it matches the contents page.

**II.1 has a fine back half and a front half that reads like a textbook.** From *Behind the last of them* to *It was their own*, this is Seren at her best:
- the gate that no one kept;
- *It had never fallen. It had only been left.*;
- *No one heard it fall.* turned straight into *The Fall of the havens the whole coast heard.*;
- the sleeve, the bloom, the four hands;
- *Neither spake.*

The run before it is the trouble. Lines 25–31 go definition, then a register of names, then *Then… Then…* chronicle. That is the annal voice Jack named ("like you are writing history text book"). The leaf's one human moment, Seren tracing the mark alone in the dark, is buried between a gloss and a genealogy. II.1 is also the **lightest-register leaf handed in so far**, so a first-time reader goes through its front half without stopping. Its close gives up the *hold/hold* play and ends on a clerk's noun where there should be a picture.

**II.3 builds, and its instincts are right.** These are all real craft:
- the small girl's second question, put to Seren, raises the tale's other half early;
- *Halvard leaned to the hearth, and the children leaned with him.*;
- the coal settling at the halt;
- *Ash is for the wind. A mark is for stone, and stone will hold.*;
- {{Idrenna}} not nodding, then nodding;
- Seren's pen as the thread.

The faults are at the hottest point:
- At Tarnel's death a pronoun points the wrong way.
- The pen beat's *It* reads as "the Book".
- Halvard's last speech squeezes two of its lines until they mean nothing.

Four doctrine lines read as a rulebook, and one liked line that plays on the word was cut.

**No run-on chains anywhere.** The longest sentence is 28 words in II.1 and 26 in II.3, and none is a chain. The v1.3 sentence-craft holds.

**Measured** (count_v3.py, each tale split out):

| | Tale proper (ceiling) | Headnote | -eth | Mean / <10w | Thirds | Old-form tokens per 100 words* |
|---|---|---|---|---|---|---|
| II.1 as drafted | 752 (800) | 37 | 2 | 11.7 / 51% | 14.1 / 10.4 / 10.7 | **3.1** |
| II.1 with the rewrites below | **763** | 37 | 1 | 11.5 / 51% | 14.1 / 10.0 / 10.3 | 3.2, plus five new inversions the count misses |
| II.3 as drafted | 1,140 (1,200) | 48 | 6 | 10.7 / 51% | 10.8 / 9.7 / 11.4 | 3.8 |
| II.3 with the rewrites below | **1,154** | 48 | 6 | 10.8 / 52% | 12.1 / **9.3** / 10.9 | 3.7 |
| *Models: I.1 · IV.3 · IV.4* | | | | | | *4.8 · 4.2 · 4.2* |

\*A crude count of stock words, *-eth*, *ye*, *not*-negation, *that* and *yet*. It does not count inversions. Read it as a comparison only.

---

## The worst problems, with rewrites

### 1 · II.1's middle is the history-textbook stretch, and it buries the leaf's heart

Lines 25–31 come between the founders' vow (*It stands.*) and the leaving. They run in this order:
1. a definition (*That mark is the Stonwryt.*);
2. the human moment, which is the best thing in the paragraph;
3. a register entry (*Of that line is Halvard… and Rhyna… is of {{Aldwena}}'s*);
4. a chronicle (*Then the folk went down… Then they raised Eldhythe*), with a clerk's phrase in it (*laid the things of the Keep in order*).

That is craft §6.2 and §6.3, the annal voice and the glossary. R6a II.1 (g) flagged the Stonwryt gloss as "definition, not scene", and the draft only shortened it.

The draft also leaves unused the one fact that would make this stretch a story. The stone takes two to turn, and Seren is one. She has to reach under it.

**Draft (lines 25–31):**
> That mark is the Stonwryt. Cut under a wall, it is a vow sealed in living rock, earned by toil and skill, and it cannot be bought. The havens struck their coin under such marks: trust, sealed in stone.
>
> The unbonded have no mark, and I shall never cut one. Late, when none is at the fire, I have put my hand under this stone, and traced theirs with one finger.
>
> Under the first warden's name his sons cut theirs, one beneath another, and beneath the last the stone is smooth. Of that line is Halvard Stone-Warden, and Rhyna of the Inner Gate is of {{Aldwena}}'s. Two lines were one, long ere those two lay in their one cradle.
>
> Then the folk went down to the warm harbours, and the guild after them. Ere they went, the founders laid the things of the Keep in order in its deepest vault, the first staff among them. Then they raised Eldhythe, that men call the Eldest. It is the eldest only of the havens.

**Rewrite:**
> That mark and that vow are on this stone, face down. Turn it I cannot, for it is a stone that taketh two. Late, when none is at the fire, I have put my hand under it, and traced their mark with one finger.
>
> The Stonwryt it is: a vow sealed in living rock, earned by toil and skill. No gold can buy it, though the havens struck their coin under such marks: trust, sealed in stone. The unbonded have no mark. Never shall I cut one.
>
> Under the first warden's name his sons cut theirs, one beneath another, and beneath the last the stone is smooth. Of that line is Halvard Stone-Warden, and Rhyna of the Inner Gate is of {{Aldwena}}'s. Two lines were one, long ere those two lay in their one cradle.
>
> Then went the folk down to the warm harbours, and the guild after them. Ere they went, the founders laid the Keep's slates and its first staff in the deepest vault, as masons lay by their tools at dusk. Then they raised Eldhythe, that men call the Eldest. It is the eldest only of the havens.

**And at the halt (line 51):**
> ~~They kneeled down in the snow, for it is a stone that taketh two. They set their four hands under it and turned it, as fishers…~~
> They kneeled down in the snow and set their four hands under it. They turned it as fishers of Tidesmeet turn a boat long given up for lost.

Why this works:
- **The definition hangs on a deed.** The gloss now follows Seren's finger in the dark, and the paragraph ends on her loss (*Never shall I cut one.*), not on a coin.
- ***A stone that taketh two* leaves the halt.** At the halt it was an explaining *for*, and it repeated the foreword's *It is a stone that two must turn*. Now it belongs to Seren's solitude, which turns the refrain.
- **The halt now carries one finger against four hands.** Halvard's *a stone that one cannot lift* in II.3 then pays it across Book Two without a word.
- ***As masons lay by their tools at dusk*** is a seven-word picture from her own world. It says they meant to come back without saying so, so *the gate that no one kept* stings harder two lines later. *The Keep's slates* is accurate to what I.4 (g03) finds in the chest. *The things of the Keep in order* was a clerk's phrase.
- **No gold can buy it** keeps *it cannot be bought* and plays against a coin that is part gold. It is modal, so it needs no *-eth*. *Gold buys it not* would be wrong under voice §1.2.
- **Jack's two phrases stay word for word:** *a vow sealed in living rock, earned by toil and skill* and *trust, sealed in stone*.
- **The register entry stays.** Both epithets *are* the lineage, so this is where they bite. It is now framed by the lintel picture and the cradle line, not by chronicle.
- **Length:** 4 words fewer across the four paragraphs and the halt together.

### 2 · II.1 is too easy to read: the front half is modern English with old words dropped in

By the token count above, II.1 has about two-thirds of the models' density. Read by sentence, the stretches of plain modern grammar are these:
- the four sentences from *That mark is the Stonwryt* to *I shall never cut one*;
- *Then the folk went down…*;
- *It is in this hall now. Tonight it is under my two hands.*

A first reader goes straight through them, which is judge B's "cosmetic" fault (voice §0). The hinge lines (*It was their own.* · *It was whole.* · the fingers and the thumb) are rightly plain. The fault is the narration *around* them. Voice §1.5 leaves room: II.1 has two *-eth* in 752 words, where the cap is about one in 100–150. These conversions cost no words:

| Draft | HEAVY | Rule |
|---|---|---|
| *That mark is the Stonwryt.* | *The Stonwryt it is:* | complement first (§1.4) |
| *and I shall never cut one.* | *Never shall I cut one.* | verb before subject after a fronted word |
| *(new)* | *Turn it I cannot* | object first |
| *Then the folk went down* | *Then went the folk down* | *Then laughed his men* |
| *Their names I knew not.* | *Their names I wist not.* | §1.3: *wist* is for knowing a fact. A name is a fact, and *wist* comes back from I.1. |
| *the column was coming in yet, and their feet* | *the folk of the column came in yet, and their feet* | mends the number clash between *column* and *their*, and keeps *yet* |

Leave the liked plain lines alone: *It had never fallen…*, *No one heard it fall.*, *What man could not destroy…*, *Forgetting had done…* and *The stone kept its vow…*. They gain from standing plain among old sentences, as the Guest's sentence does in IV.4.

### 3 · II.1's close gives up its play, and ends on a noun instead of a picture

**Draft:**
> It is in this hall now. Tonight it is under my two hands. Whoso holdeth it is keeper of the vow of the first builders, and of the shame of their children.

- The writer had a good reason: two *-eth* in one sentence is barred, so *Whoso holdeth it holdeth* was out.
- But the cure lost the *hold/hold* turn that craft §2.3 names as the close.
- *Is keeper of… and of the shame* is an abstract noun in a clerk's construction, and nobody keeps a shame.
- The *keep* chain does not need paying again here, because *The stone kept its vow. It was we who did not keep ours.* paid it four lines earlier.
- Craft rule 14 says to end on a picture, and the picture (her two hands) is buried in the middle.

**Rewrite:**
> It is in this hall now. They that hold it hold the vow of the first builders, and the shame of their children. Tonight it is under my two hands.

Why this works:
- **The plural is voice §1.5's own method** (*They that come under a roof bring their best*). It gives back the word-for-word play with no *-eth*.
- ***They that hold it*** still rings the Invocation's *Whoso holdeth it now is the teller*, and it turns that line.
- **The leaf ends on Seren's two hands under the stone.** The founders had four hands and {{Halyna}} four in the snow. The unbonded keeper of the Book now carries the children's shame alone, in her own hands, and no word says so. That is memory theme 1 (remembering is chosen and carried), felt and not stated.
- **If the orchestrator would rather end on *shame*,** keep the draft's order and still use the plural sentence.

### 4 · II.3, the hottest point: two pointing words misfire at the death and at the pen

**(a) The death line.**
> On the night of the pass the cold took many of the children, and some of the old. Under one cloak they lay down together. She woke beside him.

By grammar, *they* is "many of the children, and some of the old". At the one line in the tale where the reader must not stumble, the reader stumbles.

**Rewrite:**
> On the night of the pass the cold took many of the children, and some of the old. Tarnel and she lay down under one cloak. She woke beside him.

It also mirrors IV.3's annal exactly (*{{Wendhessa}} lay down under one cloak*), so the two deaths on that night rhyme. That is the ledger's intent.

**(b) The pen.**
> *It had stopped at the cloak, and I set it going again. By the door, {{Idrenna}} nodded.*

The sentence just before it is *That is why it is Seren that writeth it.*, where *it* is the Book. So *It had stopped* reads as "the Book had stopped". The idea is the best new thing in the leaf: Halvard says kindly that her pen is not stopped, and Seren's own ink admits it was. It must read at once. *Set it going* is also a clock's phrase, not a pen's.

**Rewrite:**
> *My pen had stopped at the cloak. I dipped it, and wrote on. By the door, {{Idrenna}} nodded.*

Why this works:
- ***And wrote on*** rings the tale's first pen beat, *I had no answer, and wrote on.*
- **The pen now builds by three, and the third breaks:**
  1. Seren writes on with no answer.
  2. Halvard says *Look, her pen is not stopped.*
  3. Seren admits it had stopped, and writes on.
- **This is craft rule 13's sideways understatement at the hottest point,** and now it lands.

### 5 · II.3: Halvard's last speech squeezes two lines until they mean nothing

This paragraph carries Jack's note 7 (the tellers agree that Seren's version is best) and the Epilogue's plant. Two of its sentences are now unclear:

| Draft | The problem | Rewrite |
|---|---|---|
| *Yet hers is the writing, and truer than ours.* | Truer than *our* what? {{Halyna}} do not write the Book. v2.0's *she writes it truer than we two could* was the craft §4.4 beat, and it has been blurred. | *Yet she can write it truer than we two can tell it.* (*write* against *tell*; modal, so no *-eth*) |
| *The books of the bonded scribes went into the vault behind them, and a book that none telleth is but ink.* | The cause has fallen out. Bonded scribes die together, so no one is left to carry their book. *Behind them* can read as "behind the books". | *When a pair of scribes went, their book went into the vault behind them. A book that none telleth is but ink.* (*went… went*: they died, and the book followed) |

These cost 4 words in all. The rest of the paragraph is right, and it is the one long speech the teaching tale has earned. In particular, keep *a stone that one cannot lift*: it puns on *she is one* and pays II.1.

### 6 · II.3's doctrine slips into a rulebook in four places, and one liked line that plays on the word was cut

R6a advises taking the economy from the doctrine paragraphs, and the writer did. But what is left still has rulebook lines in it, and Jack will hear them as "clinical". The craft says this tale teaches *through the children* and through what the pair did, not through rules.

| Draft | Rewrite | Why |
|---|---|---|
| *The seers that go among the cradles with the lamp make no pair. They read what was written ere ever we were born. They choose not. This is the Aetherbond. So were we two read, and laid in one cradle,* | *The seers go among the cradles with a lamp, and bend low, and read what was written ere ever we were born. They choose not. This is the Aetherbond. Over his cradle and mine a seer bent so, and from that night we lay in one,* | It brings back R6a's element, the seer *bending low* with the lamp, and makes the doctrine their own night in the cradle. The seer's lamp quietly answers Seren's lamp at this morning's sealing (headnote). |
| *Elder and Elderess are one rank. So I am Elder Halvard and she is Elderess Rhyna, and neither is the elder of the other.* | *Elder Halvard am I, and she is Elderess Rhyna, and neither is the elder of the other.* | The rank is implied by the play. 6 words saved, and an inversion gained. |
| *The old masters had a saying for it, that ye will hear again. Harm to one is harm to both.* | *The old masters had a saying for it. Harm to one is harm to both.* | This is a cross-reference signpost (craft §4.1, step 5). *Mark this, for ye will need it* and *Ye will understand it when it is yours to understand* already give the pair two forward-pointings, which is plenty. |
| *No mother nor father ever refused it.* | ***The guild kept the faith of the land as it kept its walls,*** *and no mother nor father ever refused it.* | **Restore it.** It is an R6a (b)4 element ("Jack likes all the elements"), and it is the kind of play Jack asked for. Its *kept… kept* rings II.1's *The stone kept its vow. It was we who did not keep ours.*, so Book Two keeps faith, walls and vows in one word. The draft's reason, that I.2 carries the creed, holds for the creed, not for this line. +12 words. |

---

## Across the leaves: one plant the draft's notes say is paid, and is not

The writer's notes (§5) say the Epilogue "already matches… *beneath the last the stone is smooth*". It does not. g11's own notes (§3, and its §5 item 4) say the lintel line was **dropped** for its budget, and they flag II.1's line as now unpaid. Since Jack likes every element, this is a choice for the orchestrator:
- **Recommended:** restore g11's 23-word lintel sentence. v2.0 has *the last name is Halvard's, which he cut there with his own hand in the year the havens came home… and no one of his line is left to cut it.* It is the cheapest payoff in the Book, and it turns the doom of the pair into stone.
- **Do not** fix it from II.1's side by writing that the last name is Halvard's. In v2.0 he cuts it only *in the year the havens came home*, long after II.1 was laid in the first summer.

---

## The rest

1. **II.1, the founders' leaf, *The wardens of the quarry cut it*.** *It* can be the hold. Write *cut the stone* (v2.0's word).
2. **II.1, *till the wall fall*.** The subjunctive is correct, and the irony works: the stone fell, and eyes saw the vow. It rings in II.3 and the Epilogue. Keep it.
3. **II.1, *I love that word*.** Keep it. It works because *The rain found every joint* teaches *point* by use the very next instant. Do not let a later pass add a gloss.
4. **II.1, the stacked sayings.** *What man could not destroy, time had withered.* / *Forgetting had done what no enemy ever could.* Both are liked and both stay. But the Invocation (g01) already says *Our fathers forgat a keep, and it crumbled* every night. II.1 must add no further statement of the moral, and it does not. Hold that line in later passes, so that memory theme 2 stays felt.
5. **II.1, *We found a shadow*.** It is clear from *the one place the songs said would hold* just before it. Keep it.
6. **II.1's headnote** (37 words) is good. *Of all the words in this Book, those only I have not mended* is the tellers-agree device turned on the founders, and it is a dry joke on herself. Keep it.
7. **II.1, *as rivers gather their streams*.** The plural is the correct thinning (it avoids *gathereth*). Keep it.
8. **II.3, *No child breathed.*** This is a stock phrase, and Seren is concrete elsewhere. Write ***No child stirred.***, and keep *In the fire a coal settled.*
9. **II.3, *each knew that the other was going*.** A *that*-fact takes *wist* (voice §1.3; *We wist not that it is but how they speak*). Write ***each wist that the other was going***. It is not Jack's fixed line, so it may change.
10. **II.3, Jack's *When the left hand dies…*** is now placed at the end of Rhyna's paragraph. This is right: it becomes the question that Halvard's *Now the last thing… and the other lived* and Seren's story answer with "not always". Give it no gloss.
11. **II.3, the Enrella tag (*said Enno, and Della ended it*).** This is the one tag craft rule 19 can bear here, because the foreword planted *the one cannot begin a jest but the other will end it*. Keep it.
12. **II.3, *we two*.** It comes eight times in 1,140 words, which is at the edge. One can go without loss: *They taught us two to cut* can become *They taught us to cut*, since the Theoliths taught pairs. The rest are where the pair is the point.
13. **II.3's budget after these rewrites is 1,154,** which is 3.8% under the ceiling against the 5–10% aim. If the orchestrator wants the margin, cut the gloss *the old master-pairs that teach*, giving *Our Theoliths were {{Idrenna}}, that sit by the door tonight.* (−7). The next sentence (*They taught us two to cut and lay and set*) teaches the word.
14. **II.3, the stretch after the halt** (the work of twelve, the cut hand, never broken) is about 110 words, and the trims above bring it down to about 95. Do not move it before the ash. *So the Bonded die together* hangs on *Separation, God did not permit*.
15. **Writer's notes, a correction.** §3 says Seren's lamp is kept "in Rhyna's *that held the lamp*". The text has no such words. The lamp is in the headnote only, which is enough for the motif. Fix the note, not the tale.
16. **The markup is right.**
    - `<!-- HALYNA -->` and `<!-- MARKED -->` are kept.
    - `legend_stonwryt_halyna chip` is unchanged.
    - `<!-- HALYNA END -->` before the Amen is new against v2.0 but matches the IV.3 model.
    - II.1 has no native block and no facing marker, as in v2.0.
    - The datelines are 6 and 7 words, and the headnotes 37 and 48.
17. **The locks hold in both leaves.**
    - The pair-names take plural verbs (*{{Idrenna}}, that sit* · *They nodded not* · *Now are they {{Enrella}}*).
    - There is no singular *they*.
    - *God* appears and no other holy mark.
    - There are no native words in the prose and no contractions.
    - There is no custom of any kind: the lamp custom is rightly cut.
    - There is no burning trace and no Captain's hood after the Amen.
18. **N/A for g04:** a wood-leaf READING, a Plain Words twin, and songs.

**Keep untouched, whatever else changes:**
- *Here is the annal of the Keep, as the founders kept it, and as we kept it not.*
- *In some winter that none told*
- *No one heard it fall.* / *The Fall of the havens the whole coast heard.*
- *Close behind came I with the water-skin.*
- *They turned it as fishers of Tidesmeet turn a boat long given up for lost.* / *It was their own.*
- *Neither spake.*
- *kneel down two and rise up one*
- *no more; and no more give we*
- *saith aloud what the cradle said first*
- *Halvard leaned to the hearth, and the children leaned with him.*
- *Ash is for the wind. A mark is for stone, and stone will hold.*
- *Now the last thing, and then to bed.*
- *She woke beside him.*
- *a stone that one cannot lift*
- *Birth united them; death could not separate them.*, which closes on the pang it does not say: for Seren, death did.
