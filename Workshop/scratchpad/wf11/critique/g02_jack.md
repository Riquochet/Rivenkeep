# g02 · Jack's Eye: I.2 The Cry of the Bonded and I.3 The Captain's Long Breath

*Critic: I read this as Jack would, checking it against voice_v3 §1, §3, §4 and §10, craft §2 and §8, the three model leaves, `I1_plain.md` and memory_theme. The source is `wf11/drafts/g02.md`. Trial rewrites, used for counting only, are in `wf11/critique/_g02j/` (`I2_rw.md`, `I3_rw.md`). I checked continuity against the foreword draft (`drafts/g01.md`) and the V.1 / IV.5 draft (`drafts/g07.md`).*

---

## The verdict

**I.2's middle is the best stretch in Book One after the torn cloak. Its two ends are where Jack's "history text book" lives.** From *Then came the Captain down from the wall* to *Under my feet I felt it tremble*, the tale builds and lands:
- the question;
- the wind in the grass;
- *Then {{Halyna}} stood up.*;
- the two chisels in the last of the light;
- the cry;
- *There was no silence*;
- the arch;
- old stone trembling.

Keep it almost word for word. Around that middle, though:
- **The opening** puts the guild's creed, its statistics and a thesis sentence ahead of the person telling the tale. That is the I.1 fault that calibration fixed (voice §3.5, §9.6). It then parades three introductions in a row (the boy, Enno and Della, {{Halyna}}'s pedigree) before the Captain comes down.
- **After the turn** come 401 words (41% of the tale) of founding acts: the fire, the terms, the day split, a chant, an aside, the course, a second song and the sleep. Seren, the girl who *came into that courtyard alone*, has vanished from them until the last paragraph.
- **The register.** Seren's own tale, which should show off her tongue, is the lightest in Book One. Of its first fifteen sentences of story, five carry any old form and none carries an old verb. In Kael's I.1, eleven of the first fifteen carry one.

**I.3's run and stretched hour is the best Hale in any version.** Do not touch:
- *I run. Under the smoke, head down…*;
- *The Captain standeth still.*;
- the cart and the log-rings;
- *The gulls hung. The smoke stood. On he walked.*;
- the three *I had time…*;
- *Hold.* … *Loose.*

The faults are elsewhere:
- **The hull threatens nothing we can see**, so *Hold* costs nothing. The tale's whole point is a man who will not hurry, and it never shows us what hurrying would have saved.
- **The setup.** The first 43% (360 words) parades plants: oath, Wick, Kael's mind, Kael's law, the drill, Jory, the hours. The question (*will the word reach him?*) is not raised until the hull appears at word ~340.
- **A contradiction.** Hale carries the *plank* up to {{Halyna}}. That contradicts V.1 and quietly breaks his own oath.

**Measured** (count_v3.py, each tale split out):

| | Tale proper (ceiling) | Headnote | Mean / <10 words | Thirds | *-eth* | *and* per sentence | Where the build sits |
|---|---|---|---|---|---|---|---|
| I.2 as drafted | 973 (1,000) | 43 | 11.7 / 50% | 12.4 / **8.3** / 14.2 | 3 | 0.49 | Seren becomes a person at word 168; the Captain arrives at 315; 401 words follow the turn |
| I.2 with the rewrites below | **977** | 35 | 11.4 / 50% | 11.7 / **8.5** / 14.0 | 2 | 0.47 | the question is seeded at 67; Seren becomes a person at 82; the Captain arrives at 322; the after-stretch keeps every beat, now with Seren in it |
| I.3 as drafted | 839 (850) | 33 | 10.3 / 57% | 12.9 / **7.7** / 10.4 | 5 | 0.25 | the distance is first given at 339; the run starts at 360; no stake |
| I.3 with the rewrites below | **842** | 33 | 10.3 / 57% | 12.7 / **7.7** / 10.6 | 5 | 0.28 | the distance is given at 108; the run starts at 351; the masons on the breach at the *Hold* |

Both tales stay under their ceilings, but each sits within 3% of it, as the calibration leaves did. Optional cuts toward a 5% margin are in the list below (items 19 and 20).

---

## The worst problems, with rewrites

### 1 · I.2 opens on creed, statistics and a cast list, and its question is a thesis, not a scene

**What's wrong.** The first story sentence is good: dusk, the grass, the chisels in their laps, ash light on the snow. Then come four sentences of backstory:
- *Ten havens had burned behind us in twenty months*;
- the creed;
- *twelve generations*;
- *Every elder, I think, was turning over the same hard thing… that walls raised for peace must at the last be held with blood.*

That last sentence is the tale's thesis, stated. Seren does not step into her own story until word 168. Then the leaf introduces people one after another, as entries in a register:
- a boy;
- two children;
- {{Halyna}}, with a semicolon pedigree (*She was Rhyna of the Inner Gate, of the line that laid it; he was Halvard Stone-Warden, of the line that cut it…*).

The foreword (g01) has already named {{Halyna}} as *Halvard Stone-Warden and Rhyna of the Inner Gate*, so the pedigree is told twice. Voice §3.5 says never to open on a creed. That is exactly why the True Men's creed went down to the roll in I.1.

The fix costs almost nothing:
- **Reorder.** Put Seren's loss right after the image. Keep the draft's best move, *I came into that courtyard alone.* followed straight by the two children with their hands joined.
- **Seed the question in the scene**, with the element the writer dropped: v1.3 and v2.0's *heard the soldiers shout*. The soldiers shout for the banner, and the guild in the grass says naught. That raises *will the guild rise?* by word 70. It also sets up a ring the reader feels without being told: at the end, *the soldiers on the wall took it from us*.
- **Turn the pedigree into a picture.** {{Halyna}} sit under the broken inner gate their own lines laid and cut. Now *Your walls are falling* is aimed at them. The first course *in the gap of the inner gate* pays it without a word, and II.1's capstone (*It was their own*) is left untouched.
- **Start a silence that builds by three:** *we said naught* · *No one answered him* · *There was no silence.*

**Draft (lines 15–27):**
> At dusk on the day of the banner the guild sat in the grass of the old ward, some hundreds of us, with our chisels in our laps. On the snow the last light lay thin as ash.
>
> Ten havens had burned behind us in twenty months. We watched every one die, and walked away from each with our chisels in our packs. Our creed forbade us to lift a hand: *Build, do not destroy. Protect, do not attack.* Mortar and chisel were our only arms, and they had not been enough.
>
> The faith of twelve generations sat on us yet, like a wet cloak. Every elder, I think, was turning over the same hard thing, unspoken: that walls raised for peace must at the last be held with blood. And if that were so, whose blood? Whose hands?
>
> I sat among them with no craft yet but the carrying of water. Over the high passes I had walked beside a boy of the guild, that knotted a net as he went. At night I slept at his side.
>
> I came into that courtyard alone.
>
> A little after me came two children with their hands joined… In the grass they sat down together, and held on.
>
> {{Halyna}} I knew not then, save as two elders that sat apart and spake to no one, for they had no need. She was Rhyna of the Inner Gate, of the line that laid it; he was Halvard Stone-Warden, of the line that cut it from the mountain. Husband and wife they were, and one since the cradle.

**Rewrite:**
> At dusk on the day of the banner the guild sat in the grass of the old ward, some hundreds of us, with our chisels in our laps. Thin as ash lay the last light on the snow. On the wall the soldiers shouted for the banner. In the grass we said naught.
>
> There sat I, that had no craft yet but the carrying of water. Over the high passes I had walked beside a boy of the guild, that knotted a net as he went. At night I slept at his side.
>
> I came into that courtyard alone.
>
> A little after me came two children with their hands joined, Enno and Della, of fifteen winters. Of all the pairs among the children, none came up the mountain whole save those two. In the grass they sat down together, and held on.
>
> Ten havens had we watched die in twenty months. From each we walked away with our chisels in our packs. Not one of us had lifted a hand, for our creed forbade it: *Build, do not destroy. Protect, do not attack.* Mortar and chisel were our only arms, and they had not been enough.
>
> The faith of twelve generations sat on us yet, like a wet cloak. Every elder there turned over the same hard thing, unspoken: that walls raised for peace must at the last be held with blood. And if that were so, whose blood? Whose hands?
>
> {{Halyna}} I knew not then, save as two elders that sat apart under the broken inner gate, and spake to no one, for they had no need. Her line had laid that gate. His had cut its stone out of the mountain. Husband and wife they were, and one since the cradle.

**What the rewrite does:**
- *Whose hands?* now falls straight onto {{Halyna}}, and their four hands answer it twenty lines later.
- The draft's own turn of phrase is kept: *watched die* still plants the Captain's *watch and die*.
- *Husband and wife* is kept (outline §5, item 5).

### 2 · After the turn, I.2 becomes the founding charter, and Seren leaves her own tale

**What's wrong.** Every beat after *There was no silence* is an element Jack likes (R6a I.2 (b) items 12–17), so none can go. But the joints between them are all *and then*:
- the fire;
- the terms;
- the day split;
- the chant;
- the aside;
- the course;
- the song;
- the sleep.

They are told in treaty voice: *The Stonewrights would bear no arms… But they would build between the volleys…* Two register appositions repeat what the foreword already taught: *{{Idrenna}}, the eldest pair, Idlan and Denna* and *{{Orvenna}}, the wall-masters, Ormund and Penna*. The never-list (craft §6.2) calls that "names arriving like entries in a register". One sentence explains the song's pedigree. *Spake* comes four times in 300 words, once of guns.

Above all, the girl who came in alone does nothing between word 258 and word 912 but carry water. So the close (Enno and Della asleep with their hands joined, Seren *a little way off, by the water-pails*) arrives cold. It should be the tale's cost.

**What to do** is give the stretch a pulse rather than cut it:
- Drop the epithets, which the foreword gave. If Idlan, Denna, Ormund and Penna must be named in Book One, name them where a deed first needs one, never in apposition.
- Fold the gate-song's pedigree into {{Orvenna}}'s ask.
- Frame {{Orvenna}}'s halves without a fourth *spake*.
- Give Seren one line of her own, built from the song's own device. Everyone sings it "the one to the comma and the other the rest". The orphan sings both halves. Seren states no feeling and adds no lore. The hall works it out, and the close then lands as the third and quietest blow of *alone*.

**Draft (lines 57–58, 67, 82, and after the song):**
> That night this hearth had its first fire in more years than any knew. By it {{Idrenna}}, the eldest pair, Idlan and Denna, made the terms with the Captain, and I carried in the water. …
>
> Ere that fire burned down, {{Orvenna}}, the wall-masters, Ormund and Penna, split the siege day in three, as quarrymen split a block along its own seam. Then they spake to the Captain:
>
> … Every joint we broke over the joint below. For such work the guild hath the old gate-song of the havens. {{Orvenna}} asked for the clearest voices. Up stood Enno and Della…
>
> *[song]*
>
> When the torches were burned to their stubs…

**Rewrite:**
> That night this hearth had its first fire in more years than any could tell. By it {{Idrenna}} made the terms with the Captain, and I carried in the water. Slow they spake, as the old speak, and the Captain hurried them not.
>
> The Stonewrights would bear no arms, and he asked it not. But they would build between the volleys, and mend a breach under the guns, with the speed and precision that only Aetherbonded pairs could achieve. …
>
> Ere that fire burned down, {{Orvenna}} split the siege day in three, as quarrymen split a block along its own seam. To the Captain they said:
>
> … Every joint we broke over the joint below. For the old gate-song of the havens {{Orvenna}} asked the clearest voices. Up stood Enno and Della, and took the first voice between them, the one to the comma and the other the rest.
>
> *[song]*
>
> I sang to the comma, and then I sang the rest.
>
> When the torches were burned to their stubs…

**What else changed:**
- *More years than any could tell* replaces *any knew*. Knowing a count is a fact, so the knew is a §1.3 slip, and *tell* gives Seren the Book's count/recount play, which Kael taught in I.1.
- *Under the guns* replaces *while the guns yet spake*, which removes one of the four *spake*s.
- Keep *Every joint we broke over the joint below.* The writer offered to cut it. It is the foreword's own image (*as masons set a course, every joint broken over the joint below*) made literal at the first course, and that is the Book's economy at its best.

### 3 · I.3: the late hull threatens nothing, so *Hold* costs nothing

**What's wrong.** A tale about a man who will not hurry needs the hearer to *want* him to hurry. The draft never shows what is at risk:
- v1.3's *when the rest were spent* is gone;
- the masons appear only as scenery in the run (*past the masons*);
- at *Hold* the hull simply comes on.

The payoff (*where it could hurt no one*) names a danger the tale never planted. Everything needed is already in the Book. Jack's terms in I.2 have the guild *mend a breach under the guns*, and the masons are on the wall in the run. Put them in the hull's path at the moment the holding seems over. *Two and two* answers I.2's *look again. Ye will see two.* with no gloss. The cause stays dark: *I know not what the Captain thought.*

**Draft (lines 133 and 159):**
> One battery had we in those weeks, and it was Kael's. Late in the holding his lookout saw, in a far-glass of Pellow's grinding, a hull that had hung back in the grey, where none had hung before. Now it came in, late and alone.
>
> …
>
> The battery held. The late hull came on through the smoke, and on, till I could see the wet on its timbers.

**Rewrite:**
> Late in the holding, when the rest were spent and the masons were come out on the breach, Kael's lookout saw a hull in a far-glass of Pellow's grinding. It had hung back in the grey, where none had hung before. Now it came in, late and alone.
>
> …
>
> The battery held. Below us the masons laid on, two and two, and looked not up. The late hull came on through the smoke, and on, till I could see the wet on its timbers.

This adds 22 words, and they buy the whole tale its stake. *Were come out* is the be-perfect for motion (§1.4). *Looked not up* is negation without *do*. The one-battery fact moves into the dawn sentence (see 4).

### 4 · I.3's setup is a parade of plants, and the question arrives at word ~340

**What's wrong.** These are craft §2.3's plants, and each is a single line, as the note asks. But no line presses on the next, and the reader learns that distance is the problem only at *At the far end of the wall, above the gate, stood the Captain* (word 339). Kael's law then gets glossed twice: Kael says it, and Hale restates it (*So what I see, I carry to him, and to no man on the way*). Meanwhile the oath is sworn on *a fallen block* that is never called the runners' stone, which IV.3's Brenn (*mine hand flat on the runners' stone*) needs.

**What to do:**
- Show the Captain walking away to the far end at dawn. That gives the question (*a man can stand but in one place*, and his place is the whole wall away) by word 110.
- Cut Hale's restatement. The run's *To no man speak I* carries it.
- Name the stone. It also lets the hall feel the oath as a rite handed on (memory theme 3) without a word added.

**Draft (lines 107, 113–117):**
> The first week, our hands on a fallen block by the inner gate, we runners sware the old oath of the havens:
>
> …
>
> At the grey of the morning of the first assault I stood by Kael's guns. Ere he went on, the Captain gave Kael his mind: where to watch, what shot to lay, and when to hold. Kael laid his hand on my shoulder.
>
> "Naught may change that mind but his own voice at my side, lad, and a man can stand but in one place."
>
> So what I see, I carry to him, and to no man on the way. We runners are his eyes, where the smoke lieth between him and the water.

**Rewrite:**
> The first week we made a fallen block by the inner gate our runners' stone, and sware on it the old oath of the havens:
>
> …
>
> At the grey of the morning of the first assault I stood by Kael's guns, that were all the guns we had. The Captain gave Kael his mind: where to watch, what shot to lay, and when to hold. Then went he on, to the far end of the wall. Kael laid his hand on my shoulder.
>
> "Naught may change that mind but his own voice at my side, lad, and a man can stand but in one place."
>
> So we runners are his eyes, where the smoke lieth between him and the water.

Then line 135 shrinks to *Between the Captain and that hull lay the smoke.* The reader already knows where he stands.

### 5 · Hale carries the plank. That breaks V.1 and his own oath

**What's wrong.** Line 167 reads *I found a plank in the shallows with marks cut in it. Up past the fires I carried it to {{Halyna}}*. In the V.1 draft (g07), Hale comes up *from the water's edge* and says the three words. {{Halyna}} then go down with Seren's lamp, and *the men hauled one plank up out of the surf*. v2.0 likewise had him carry the marks *in three words*. A runner carries *what he saw, and nothing else*, so he carries the word, not the wood.

g07's notes also count on I.3 to plant *as we runners do after every holding*. Keep it. *Past the fires* can stay too: V.1 now gives the fires their plain cause (*for they hated it, and wood was dear on the ridge*), so no custom is implied.

**Rewrite:**
> That evening I walked the tide-line, as we runners do after every holding. In the shallows I saw marks cut in a plank, and carried them up past the fires to {{Halyna}}:

### 6 · The old English slips in the leaf that should show it off

These matter more in I.2 than anywhere else, because Seren is the register's own voice.

| Line | Fault | Fix |
|---|---|---|
| *I had seen the cloak go up, and **knew** not what it was to us.* | knowing a fact takes *wist* (§1.3; the foreword and I.1 both use *wist*) | *and wist not what it was to us.* |
| *in more years than any **knew*** | the same | *than any could tell* (see 2) |
| *So I **knew** the north was awake.* (I.3) | the same | *By it I wist the north was awake.* |
| *"Hold it, and it will hold **you**."* | {{Halyna}} speak to one frightened child. R3 H1 and voice §1.1 give *thou/thee* to "one near hearer (kin, friend, comrade, child)"; *you* is the plural or the honour form | *"Hold it, and it will hold thee."* It is warmer, too. **Book-wide:** the Epilogue draft (`_g11/epi_final.md` l. 40) must match. If the orchestrator rules the line fixed, keep *you* in both. |
| *Not tall was he. Coal-black were his fingers yet. Half a cloak hung on his back.* | two inversions in a row, then three short sentences with no weight: Yoda order turning into a primer (§1.5, §3.1) | craft §4.1's own worked cut: *Not tall was he. The coal-black was yet on his fingers, and the half of a cloak on his back.* |
| ***Looking up** at the torn cloak, they bowed to it in the same breath.* | a modern participle opening at the hinge's breath-before | *To the torn cloak they looked up, and bowed to it in the same breath.* |
| *Every elder, I think, **was turning over**…* | a modern progressive in a sentence of thought; with *I think* it reads as a lecture | *Every elder there turned over the same hard thing, unspoken:* |
| *spake* ×4 in lines 27–67 (*spake to no one* · *Slow they spake* · *the guns yet spake* · *Then they spake*) | a stock word worn out in one page, and once on guns | keep the first two and cut the others (see 2) |
| *They say it of him **as of a gift of the Rite**.* (I.3) | it stumbles, and the *of* carries no sense | *They say it as though the Rite had given it him.* (old dative, as in *gave it him*) |
| *Ere he went on, the Captain gave Kael his mind* (I.3) | once 4 adds *Then went he on*, the *Ere* doubles it | *The Captain gave Kael his mind…* |

---

## The rest

1. **I.2, *There was no silence.*** The writer says this line works twice: no silence between the halves, and none left in the ward. But the next two sentences explain the first sense and close off the second. Move *One cry it was, in two throats. Hers came first for no cause but that a cry must begin somewhere.* in front of *Some tell it…*. Then *There was no silence.* stands last, opens straight onto *Then stood the guild*, and is the third of the silences (see 1). This is in `I2_rw.md`.
2. **I.2, the bow and the chisels.** Give the ★ line its own paragraph: *Their two chisels took the last of the light.* It is a great line (voice §3.4), and the cry follows it.
3. **I.2, the aside** *look again. Ye will see two.* falls in the middle of the after-stretch, not at the turn or the close (voice §3.5). Leave it there. It is the tale's only aside, and it answers *Whose hands?*. Do **not** move it next to *I sang to the comma…*. Three blows of *alone* in a row would turn the nuance into a plea.
4. **I.2 headnote.** *and I sat in the grass with the rest* repeats the first sentence of the story. Cut it: *On the day I tell of I was twelve winters old, and a child of the guild.* (35 words).
5. **I.2 dateline.** Use the canon phrase: *The first winter, the night after the first assault.* (8 words).
6. ***with the speed and precision that only Aetherbonded pairs could achieve.*** R6a marks it as Jack's, but voice §1.7 does not list it. *Precision* and *achieve* are the most modern words in Book One outside the warden's letter, which voice §1.7 calls "the only modern register in the Book". **Orchestrator to confirm.** If it is Jack's, keep it word for word and keep its frame old, as the rewrite does (*mend a breach under the guns*). If it is not, consider *as swift and true as only the Bonded build*.
7. **I.2, the creed** *Build, do not destroy. Protect, do not attack.* I agree with the writer: keep it word for word. An imperative *do not* is good 1611 usage, and it is quoted guild lore.
8. **I.2, the cuts the writer offered.** Refuse both. *Every joint we broke over the joint below.* pays the foreword (see 2). *Some tell it…* is what *There was no silence.* stands on.
9. **I.2, what to keep exactly.** *Tonight I was afraid to speak* (the B1 fix holds). *So I hold it.* *We watched every one die* planting *watch and die*, a real Seren turn. *Slow they spake… and the Captain hurried them not*, which plants I.3's *will not hurry* with no gloss. *I stood with them, and remember not the standing.* The arch with its frame struck. *I lay down… This I lay*.
10. **I.3, the cuts the writer offered.** Refuse all three:
    - *Kael was counting under his breath* is the Counter at the moment of the *Hold*, and it quietly pays I.1's *tell*;
    - *I have no better way to say it* is v1.3's Hale (R6a §0.8);
    - *and in the hauling slower* is the middle of the triple.
11. **I.3, the headnote** (*He told it standing, and as fast as ever he ran; I have set it down slower.*) is the best headnote touch since I.1's. It is Seren's joke on a tale about not hurrying, and it implies no teller's verdict. Keep it.
12. **I.3, *faster than I could tell them*** against *I am not a teller* is exactly the play Jack asked for. Keep it.
13. **I.3, the *-eth* forms.**
    - I agree with writer §4 on *Hull hangeth back*, *lasteth* and *It is only a rhyme*: §1.2 forbids *-s* and *-eth* in one mouth.
    - *It is not the world that sloweth, lad* closes the tale, and Jack loved it in v1.3 as *slows*. **Orchestrator's call.** If *sloweth* stays, every later quotation of the mend and of the saying (V.5 and the Epilogue, if they quote it) must use the same forms.
14. **I.3, no cost.** Craft lists none for I.3, and the tale pays one inward: *Then I had time to be ashamed of it.* Do not add another.
15. **I.3, Jory's place.** IV.5 (g07) puts Jory *on the east wall* all that winter. I.3 has him leaning on the parapet within earshot of Kael's battery after the drill. If Kael's guns are not on the east wall, add one clause (*Jory of Eldhythe, come along from the east wall,*) or let IV.5's *east wall* stand as his post and not his place that morning. This is minor, and the orchestrator should look at it once.
16. **I.3, *One battery had we in those weeks, and it was Kael's.*** It reads like an annal entry between two scenes. It is folded into the dawn sentence in 4 (*Kael's guns, that were all the guns we had*). The plant for V.5 II and IV, and V.7 II, survives.
17. **Memory theme.** It is light, right and felt, and none of it is preached:
    - Tarnel remembered by his knots and never by his death;
    - the old oath and the old gate-song of the havens, handed on at a new stone and a new course;
    - Hesk's *mother's* lamp;
    - the hearth's first fire.

    The rewrites add only the runners' stone and *I sang to the comma…*. Add nothing more.
18. **Locks.** All of these hold:
    - pair-names take plural verbs, and there is no tag on pair-speech;
    - no singular *they*;
    - no *he and she* used as a tag;
    - no Christian mark;
    - the Captain is unnamed and speaks only the question and the calls;
    - {{Halyna}} discover and cry, and the other hands act;
    - no custom, since the *fires* get their plain cause in V.1;
    - the songs and the cry are word for word.
19. **Optional cuts for a margin in I.2** (the rewrite is 977; 5% under would be 950). These cost nothing liked, and together they save 11:
    - *Of all the pairs among the children, none came up the mountain whole save those two.* becomes *Of the children's pairs, none came up whole save those two.* (saves 5);
    - *He looked at the elders, and past them at the broken gate, and asked one question.* becomes *He looked past the elders at the broken gate, and asked one question.* (saves 3);
    - *When the torches were burned to their stubs,* becomes *When the torches were stubs,* (saves 3).

    That brings I.2 to 966. Getting further down would mean cutting a liked line. Do not.
20. **Optional cuts in I.3** (the rewrite is 842; 5% under would be 808):
    - *Jory laughed down at him.* becomes *Jory laughed.* (saves 3);
    - *That is what I remember first.* (saves 6). This one costs a v1.3 line, so cut it only if needed.

    Better to stay near 840 than to lose Hale's voice.
21. **Plain Words.** The draft has no Plain twin for either tale. Both are still owed under §11, with these points:
    - I.2's solo line becomes *I sang the first half, and then I sang the other half too.* The meaning stays and the shape goes (§11.3).
    - I.3's masons become *the masons kept working below us, in pairs, and didn't look up.*
22. **For other tales.** If the rewrites are taken:
    - the Epilogue's *Hold it, and it will hold you* must change with I.2 (see 6);
    - V.1 already has Hale carry words, not wood, so it needs nothing;
    - II.1 gains a quiet plant, {{Halyna}} sitting under the inner gate their lines laid. *It was their own* now pays twice.
