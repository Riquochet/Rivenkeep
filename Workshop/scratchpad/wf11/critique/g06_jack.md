# g06 · Jack's Eye: BOOK FOUR's heading and Argument, IV.1 and IV.3

*Critic: read as Jack would, against voice_v3 §10, craft §8, the three model leaves and memory_theme. The source is `wf11/drafts/g06.md`. Trial rewrites (used for counting only) are in `wf11/critique/_g06tmp/`.*

## The verdict

**IV.3 is the calibration leaf with one sentence added, and that sentence is the only thing wrong with it.** Cut it, mend two small things, and IV.3 ships.

**IV.1 starts as a story and ends as a history text book.** The first half builds well:
- the rotten cord;
- {{Halyna}} refusing to read on until Seren writes their line down;
- the litany climbing to the bed;
- *Halvard turned the leaf*;
- the clerk's line, with the lamp bent to it twice;
- *I would have kept his name.*

Then the reading scene goes dark. Across the last ~500 words, the only moment set in the room where they are reading is *I copied it as he had*. The turn arrives with no one's hand on it, and after it come 203 words of chronicle (eras, causes, a moral), which break v1.3's one-two close. Jack would say "it doesn't build" about the back half, and he'd be right.

**Measured** (count_v3.py, each tale split out):

| | Tale proper (ceiling) | Headnote | Inside cap | Notes |
|---|---|---|---|---|
| IV.1 as drafted | 965 (1,000) | 38 | — | thirds 12.0 / 11.1 / 9.8; 203 words after the turn (craft §2.1 allows about 100 for turn and cost, plus under 50 for the close) |
| IV.1 with the rewrites below | **954** | 38 | — | thirds 12.9 / 11.9 / 9.8; **153** after the turn; one *-eth*; longest sentence 29 words |
| IV.3 as drafted | 1,289 (1,300) | 36 | annal **159 (cap 150)** | a diff against `samples/IV3.md` shows one added sentence and nothing else |
| IV.3 with the fixes below | **1,285** | 36 | annal **150** | thirds 10.3 / 8.7 / 10.6 |

---

## The worst problems, with rewrites

### 1 · IV.1 dies after its turn, and its close is broken in two

*What I held, I knew not.* is a real turn. After it, four paragraphs (203 words) narrate the era:
- the end of the Harvest;
- *three generations long*;
- *the wheel of pride turned*;
- *Glad were we*;
- *But humility came too late*.

Then the guild's share comes **after** *humility came too late*, followed by the sails. That splits v1.3's couplet, the best close in Book Four:

> *But humility came too late. The first dark sails were already on the sea.*

Four sentences now stand between the moral and the picture that should answer it. The share is also *stated* (*That is our share of it. We will not lay it all on the Council.*) when it could be *done*. And *In our archives the stones lay yet* contradicts *Stones like them* earlier (see 3).

**Draft (lines 93–99):**
> Then the havens forgat, three generations long. The stones hung on over the ale and the dice. The children grew up under them, and asked what they said, and were told they said naught. Some of you that sit at this fire were those children.
>
> Late, very late, the wheel of pride turned. The temples were mended, and men climbed the worn steps of our guild-halls again for counsel. Glad were we, as men are glad that mend a sea-wall in the calm. But humility came too late.
>
> In our archives the stones lay yet, where we had locked them. It was we who turned the key. That is our share of it. We will not lay it all on the Council.
>
> The first dark sails were already on the sea.

**Rewrite:**
> Then the havens forgat. Over the ale and the dice the stones hung on, and children asked what they said, and were told naught. Some of you that sit at this fire were those children.
>
> Late, very late, the wheel of pride turned. The temples were mended, and men climbed our worn steps again for counsel, glad as men that mend a sea-wall in the calm. Of the stones none asked, and we said naught. It was we who turned the key.
>
> But humility came too late.
>
> The first dark sails were already on the sea.

Why this works:
- **The share becomes a deed.** The guild had its chance when the havens came back for counsel, and said nothing. That is memory theme 2, shown and not told, and it sets the guild beside Brenn without a word of comparison.
- ***Turned* now works twice.** The wheel of pride turned, and it was we who turned the key.
- **The couplet is whole again**, ending on a picture.
- **Every beat stays:** the forgetting, the children, the aside to the hall, the temples, the sea-wall, the key, the humility and the sails. *That is our share of it.* may go back in after *the key* (+6 words) if the orchestrator holds that line as locked. Drop *We will not lay it all on the Council*: it argues, where the deed has already said it.
- **The Harvest-ending paragraph above it stays as drafted.** It is good, and *No one decided it.* is Seren at her driest.

### 2 · The turn is the least staged moment in the tale

R6b (f) calls the letter "the second blow", but it gets less staging than the first. The clerk's line gets Rhyna's finger and the lamp bent twice. The letter, the Book's first sight of the lie and the one modern register in it, simply appears: *Among the counts… a clerk had copied a letter.* Nobody reads it aloud, nobody's voice is heard, nobody's hand is on it.

Stage it as a build by three, where the third breaks. Three people handle the lie as cargo: the clerk, Halvard and Seren. Then Seren's own line breaks the pattern.

**Draft (lines 79–89):**
> Among the counts of one late summer a clerk had copied a letter from the outermost post. He set it between a count of poles and a count of oars, with the same care.
> …
> At its foot a name is cut out: ▒▒▒▒.

**Rewrite:**
> Among the counts of one late summer Halvard came on a letter from the outermost post. A clerk had copied it between a count of poles and a count of oars, with the same care. Halvard read it as he had read the oars.
>
> *Unknown intruder. Hostile intent. Neutralized. Vessel burned and released.*
>
> At its foot a name is cut out: ▒▒▒▒. Rhyna laid her finger on the blot, and took it away.
>
> *(lost at the edge, then* I copied it as he had, between the poles and the oars. *then* What I held, I knew not. *, all as drafted)*

What this adds:
- {{Halyna}} discover and Seren writes.
- The reader hears what Halvard did not: the dead modern words read in a voice meant for oars.
- Rhyna's finger on the blot plants IV.3's blots and explains nothing (*took it away* stays dark).
- The headnote's *letters leaned like reeds* now pays quietly: she copied too fast to know what she held.
- The finger is optional (+10 words). The Halvard sentence is not.

### 3 · In the middle, the frame vanishes and the leaf turns into chronicle

Lines 67–77 run 202 words of pure summary:
- the grey thins;
- the Stonewrights warn;
- the warning is shelved;
- the carvings are found, hung and locked.

In all of it there is no lamp, no leaf, no hand, no chest. This is the textbook Jack named. Two touches from the room bring it back, and one of them also clears up a muddle. As drafted, the stones are *Stones like them* in the chest, yet *the stones lay yet* in the archives. Which is it? Per the outline (§7.11, the mute stones of the archive), the guild's locked stones **are** the ones in the archive chest. Say so, and put the chest in the room.

**a) The warning:**
> *It is in our own hand:* → **It is in our own hand, on a leaf that no thumb had darkened:**

This is a scribe's picture from her own trade. Nobody re-read the guild's own warning. It is the guild's share again, as a thing seen.

**b) The carvings** (reordered so that the locked stones lead into the room):
> For there were carvings. At the feet of the pillars the axemen found stones set upright, cut with curling letters, as beautiful as frost on a window. No man could read them. Some hung for ornament in the harbour-houses, and men drank under them, and did their reckoning. The rest the guild locked in its archives, and its own warning with them. Some of those lie in the chest at my knee, that I carried up the mountain. {{Halyna}} have laid their four hands on them, and been given naught. Stone does not translate.

*The chest at my knee* puts the stones in the room where the reading happens, at the bottom of the same chest the tale opened on, and *that I carried up the mountain* still plants IV.3. That makes the close (*It was we who turned the key*) a key to something the hearth could reach out and touch.

**c) The fortune line is garbled**, and it is the one place in the leaf where the archaism slips:
> *That word will not hold under my tongue, but giveth, as mortar that is gone to sand.*

The problems:
- the modal *will not hold* is yoked to an indicative *giveth*;
- *giveth* with no object reads as "gives something", not "gives way";
- the *-eth* is spent where nothing plays on it.

**Rewrite:** *I tried that word under my tongue, and it gave, like mortar gone to sand.* (14 words against 18.) It keeps the picture and gives a passing nod to her habit of saying a word over, which craft §3.6 rations to V.1, VI.3 and the Knowings. Nothing more is needed.

### 4 · IV.3: cut the added line *The Council kept the letter, and forgat the Guest.*

It is the only change from the calibration leaf, and it does four kinds of harm:
1. **It is false.** The Council never had the Guest to forget. It had *Unknown intruder*. The truth went into Brenn's pack, *and gave it to no one*. The line throws away the very point Brenn's mirror makes: the Council did not forget the truth, it never received it.
2. **It preaches.** The Invocation (g01) already says outright *Their fathers forgat a wrong, and it came back to us under grey sails.* I.4 says *We forgat it*, IV.5 says *We forget*, and IV.1 shows it (*Then the havens forgat*). This would be the fourth statement of one moral. memory_theme asks for the reader to "feel it without being told".
3. **It breaks the annal's cold chain.** As written, the annal pairs the mark on the warden's flesh with the name cut from the rolls. A verdict about the Council lands between the two and turns the annal toward a summing-up.
4. **It breaks the 150 cap** (159).

**The theme is already felt here, without the line.** Brenn *gave it to no one*; ten lines later {{Wendhessa}} *sealed his words, and told no one*; and then the masons call the chest *naught of worth*. The truth is nearly forgotten twice more, and children carry it up the mountain. That is item 2, shown three times. **Revert the annal to the sample, word for word.**

### 5 · IV.1's litany is set out as a ledger, not a chant

There are fifteen one-line paragraphs in the count: ten lines of *Black wood, for…* (eight of them for the needful uses before the vanity begins), plus the Carnhold line, the hinge, the stain, the bed and *proud*. On the page it reads as an inventory, the "clinical" Jack named. It also blows through voice §3.4, which expects four to eight one-line paragraphs in a whole tale, and IV.1 has twenty-three.

The climb (need, then vanity, then the bed) only bites if the needful run goes *fast* and the vanity goes *slow*. Keep every haven, because VI.2 hangs its Thrones on them, but run them as one paragraph of anaphora. Then let the vanities stand alone.

**Rewrite:**
> Black wood, for buttresses and bridges. Black wood, for the three spans at Tidesmeet, and the pilings of Fenholm. Black wood, for the roof-trees of Holtward, and the cranes of Highreach. Black wood, for the galleries of Sandreach, and the hall on the ice at Rimewatch. Black wood, burned slow in the forges of Emberhythe. And at Carnhold the axes were beaten out, and went back to the edge for more.
>
> Then the things that needed naught of the kind.
>
> Black wood, to floor the dancing-hall of a lord of Eldhythe.
>
> Black wood, for the trade-tables of the harbour-houses, and their dice-boards.
>
> *[Here the roll is stained, and three lines are lost.]*
>
> Last of all, a merchant of Tidesmeet had one pillar hewn into a bed.
>
> He slept in it, and was proud.

It is the same words, chanted instead of filed. The Carnhold line now closes the first run as its sting: the wood's own fire forged the axes that went back for more.

---

## The rest

1. **IV.3: Brenn's second silence has dropped out.** R6b beat 20 says that at the axemen in Eldhythe he did not laugh, *but said nothing*. The draft goes straight from *I laughed not, for I had seen it turn.* to *The Council had it in writing.* A first reader will not see that Brenn had a second chance to tell the truth, and let it go. Rewrite: *I laughed not, for I had seen it turn. Yet I said naught. The Council had it in writing.* (+4 words; the trial lands at 1,285.)
2. **IV.3: *Never had he had a wound.*** The double *had* stumbles one sentence before the blood. Rewrite: ***Never in his life had he bled.*** It is plain at the hinge, the same length, and it sets up *and the blood came*.
3. **IV.1: *In the oldest the grey is but…*** The elliptical *the oldest* (what?) trips a first reader on the leaf's first fact. Rewrite: ***In the oldest roll** the grey is but a blackish veil…*
4. **IV.1: the time-stamps.** *three generations long* is the annal voice that craft §6.2 cuts. It goes in rewrite 1. *Two generations the Trade Council sent out the axes* may stay, because it is the roll's own count and Seren is reading it.
5. ***Stone does not translate.*** This is a *do*-negation on a 20th-century sense of *translate* ("this joke doesn't translate"): a modern word in plain clothes. It is an outline lock, echoed in g11, and it lands as the leaf's one plain saying, so keep it as written. **Never** use the writer's fallback *Stone doth not translate*: that is costume on a modern verb, which is exactly what §2.4 forbids. The orchestrator should rule once, for both leaves.
6. **IV.3: the laugh** (voice §9.1) still needs Jack's word. My read as Jack: *I stood among them, and I hear that laughter yet* is truer to "only observe", and it is the stronger line. With it, *I laughed not, for I had seen it turn* now answers the shore's laughter rather than his own, which still works. Keep the flag open, and change nothing until he rules.
7. **IV.3's coda after the Amen** has three frame lines: Ebba and the slow following, the hood, and the runners. Voice §6 allows exactly these, but it is the Book's longest coda, so add nothing to it, and let no other leaf copy it.
8. **The Book Four Argument** (*The wrong, told from both sides of the grey.*) is safe and spoils nothing, but it is the barest of the six. Book One's now has a picture (*How we came to a heap of stones, and stood.*), and Book Three's has a shape (*Ten havens, and ten men to tell them…*). An optional version that still spoils nothing: *What was felled at the edge, and who came to the door: the wrong, told from both sides of the grey.* If it is kept as drafted, nothing is wrong.
9. **IV.1: *Of those stones, some the guild locked in its archives, and its own warning with them.*** As drafted, the warning has two fates in four sentences (the Council's shelf, then the guild's archive), and *Of those stones, some…* is a clumsy inversion. Rewrite 3b fixes both: the Council's copy is shelved, and the guild's copy is locked with the stones.
10. **Keep these exactly. They are the leaf's best, and they are Seren's own:**
    - *No line of it would {{Halyna}} read me till I had written this*;
    - *They cut it, and it grew. They cut it, and it grew. They cut it.*;
    - *Halvard turned the leaf. Neither of them spake.*;
    - *Whose hand it was, the roll saith not. I would have kept his name.* (memory theme 1, chosen and unspoken, set against the name cut out);
    - *I copied it as he had, between the poles and the oars.*;
    - *trade sat in the high seat*;
    - *laid on a shelf* (against the hearth's *lay*, unsaid);
    - *No one decided it.*;
    - the thread *pride… proud… the wheel of pride*.
11. **The writer's asks of other leaves are already met. Strike them from the notes:**
    - g03's I.4 opens with the whole refrain, *Hold the stone, Seren. I tell myself so every time.*;
    - g04's II.1 headnote shows that {{Halyna}} read *the old hand*.
12. **The annal options in writer's note §2** fall away once the line is cut. Nothing in the annal needs trimming.
13. **The Plain Words are still owed for both tales.** The twin inside `samples/IV3.md` fails §11 (it runs at 100% of the Book and follows it paragraph by paragraph), so it must be retold from the beats. IV.1's Plain must keep the litany as a list but drop the anaphora's grandeur. Plain does not chant.
14. **Locks, all holding:**
    - no custom: IV.1's *After the year of the burning boat no crew would row…* is plain fear, and IV.3's burning is ▒▒▒▒'s *Leave naught to show.*;
    - Brenn's hands touch nothing;
    - the blots are kept;
    - pair-names take plural verbs, with no singular *they*;
    - there is no holy mark, and the cross-sign is *the half of something*;
    - the letter, the warning, the oath, *Stop… Sky… Dying…* and the clerk's line are all verbatim;
    - IV.3 keeps the `legend_seal_wendhessa chip` block and its HALYNA markers exactly as v2.0 and the sample have them;
    - IV.1 needs no native block, because v2.0 has none for it.
