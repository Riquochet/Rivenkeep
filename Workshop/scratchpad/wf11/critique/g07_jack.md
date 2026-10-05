# g07 · Jack's Eye: IV.5 The Burning Boat, BOOK FIVE's heading and Argument, V.1 The First Glyph

*Critic: I read this as Jack would, against voice_v3 §10, craft §8, the three model leaves and memory_theme. The source is `wf11/drafts/g07.md`. My trial rewrites, used only for counting, are in `wf11/critique/_g07j/` (`IV5_rw.md`, `V1_rw2.md`).*

## The verdict

**IV.5 has dropped the custom cleanly. It keeps every element R6b lists, and both songs are word for word. But it does not build.** It is a string of v2.0's best single lines, each set down on its own, and almost none of them is a scene. The tale exists to deliver Jory's death, yet Jory first appears at word 613 of 962 and is dead about 290 words later. His last morning, the halt, gets 74 words, which is 8% of the tale. Craft §2.1 says the halt is the longest stretch. Between the opening and Jory, the middle reads like a file on how the rumour spread: who swore to it, who wrote it down, who sang it. Voss's sentences are as clipped as Kael's, and his second-hand voice (*So she told it me*) is missing. Jack would call the middle "blah" and say the whole "doesn't build", and he would be right about both.

**V.1 is the nearer of the two to shipping, and Seren's play is real in it:**
- *they had but the shore's*
- *one word was all they could tell*
- *It held.*
- *a river in flood, and I a girl with a cup*
- *Halvard put the lamp back in my hand.*

**But the mend of the custom is the weakest sentence in the draft.** *"Burn it," said Harl…, of every plank.* has the same shape as the cut line *they said the old words over it*: a formula spoken over each grey plank as it goes on the fire. It also puts the warden's own order from IV.3 into a True Man's mouth. Beside it, *for they hated it, and wood was dear on the ridge* explains the deed, and its second half contradicts the deed, since scarce wood is being burned on a beach.

V.1 has two further faults:
- The question arrives at word 176.
- The turn (*I let go.*) comes at word 555, and 265 words follow it. Jory and Enno with Della trail in after the turn as afterthoughts, when they could be the second step of a build by three.

**The Book Five Argument** carries no custom; the writer is right about that. But at 34 words, with a colon and a semicolon, it is two to five times the length of the other five Arguments in the drafts, which run 6 to 17 words.

**Measured** (count_v3.py, each leaf counted on its own):

| | Tale proper (ceiling) | Headnote | Real *-eth* | Question / Jory at word | Halt | Words after the turn |
|---|---|---|---|---|---|---|
| IV.5 as drafted | 962 (1,000) | 48 | 4: *cometh*, *laugheth*, *argueth* (three of them inside five sentences), *sitteth* | Jory @ 613 | 74 | — |
| IV.5 with the rewrites below | **972** | 48 | 2: *cometh*, *sitteth* | Jory @ **66** | 83 | — |
| V.1 as drafted | 813 (850) | 29 | 3: *hath*, *burneth* (at the hinge), *sitteth* | question @ 176 | 218 | 265 |
| V.1 with the rewrites below | **826** | 23 | 2: *hath*, *sitteth* | question @ **38** | 295 (now with the build by three) | **182** |

Both rewrites keep every element. No sentence runs over 30 words, there are no contractions, and the crisis third is the shortest in both.

---

## The worst problems, with rewrites

### 1 · IV.5: Jory comes in too late for his death to land

The tale's real question is the one a child at the front would ask: *will Jory stop whistling before the rhyme comes true?* It is never raised, because the hearth does not meet Jory until the rope, two-thirds of the way in. Every good line in the middle presses on nothing:
- the ship-masters' sayings;
- the couplet's *the one it comes for will not come home again*;
- Merrick's *"Not that one."*

Put Jory in the opening, as a deed, and the whole tale leans on him.

The opening also has a logic stumble, and it is the wrong kind of hard: *Wherefore would a ship-master not hear that tale?* Nothing in the first 70 words is a tale. There is a hull, a scream and a rhyme. A first-time reader stops on the sense, not on the grammar.

**Draft (lines 9–13):**
> In the first holding of this war, on the shingle, I heard one of their hulls burn. It screamed. Along the wall the old sailors turned their faces from the sea, and Merrick first.
>
> A rhyme went round in me like a skipping-rope. At seven I had skipped to it. At forty I understood it.
>
> Wherefore would a ship-master not hear that tale? My grandmother answered me with the tale. Ye may weigh it.

**Rewrite:**
> In the first holding of this war, on the shingle, I heard one of their hulls burn. It screamed. Along the wall the old sailors turned their faces from the sea, and Merrick first. Up on the east wall Jory whistled.
>
> A rhyme went round in me like a skipping-rope. At seven I had skipped to it. At forty I understood it.
>
> A boy at her table, I asked my grandmother wherefore the ship-masters would not hear it. She answered me with a tale. Ye may weigh it.

The rewrite does five things:
- Everyone turns away and one man whistles. That is the tale's dread in one sentence.
- A reader who has read I.3 and I.5 knows who Jory is, and knows he dies.
- The asking is now Voss's own deed, as his epithet promises.
- *Wherefore* still asks *why*, its only allowed sense.
- It ties the leaves together, at no cost. I.3 makes the first holding the day of the first assault, and V.1 is *the night the first assault was broken*. IV.5's whistling Jory is the same Jory who goes up V.1's shingle whistling that night.

Then **pay the kindness at the death.** The draft plants a lovely line, *for the least of them Jory turned it slower yet*, and never uses it again. Memory theme 4 asks for the good of the dead at the death. Give it one clause in the halt, with no gloss.

**Draft (line 77):**
> On the morning he died I was at his side, and the tune went before him along the wall-walk. Then the rhyme stood up hard in me, like a mooring-line when the flood is come under the hull. I heard the two lines we never sang.

**Rewrite:**
> On the morning he died I was at his side, and the tune went before him along the wall-walk. Slow he whistled it, as he had turned the rope for the least of us. Then the rhyme stood up hard in me, as a mooring-line at the flood. I heard the two lines we never sang.

The mooring-line keeps Voss's rope, his own trade-picture, but loses its scaffold, because at the death the tale should be colder (craft rule 12). With Jory carried from word 66, the halt can stay short. Its problem was never only its length. Nothing pressed on it.

### 2 · V.1: the burning is still a rite in all but name

**Draft (line 115):**
> The soldiers dragged it up and burned it on the tide-line, for they hated it, and wood was dear on the ridge. "Burn it," said Harl of the burning shore, of every plank. One by one the fires went up, as lamps go up along a quay at dusk. The Captain let them burn the most of it, and stood among them, still.

The draft has three faults here:
1. ***"Burn it,"… of every plank*** is a phrase said over each grey plank as it is burned. That is exactly the shape of v2.0's *they said the old words over it*, which Jack's fix removed. The reader also heard ▒▒▒▒ say *"Burn it"* two leaves ago, so a True Man saying the same words over a grey boat teaches the reader that this is what the coast does.
2. ***for they hated it*** gives a motive with *for*, which craft §8 Q5 says to cut. The deed can show the hatred.
3. ***and wood was dear on the ridge*** contradicts the deed. If wood is dear, why burn it on the beach? The sentence explains, and its own explanation does not hold.

Harl's temper is already planted in III.1 (g05: *Aske may lay his hand on the planks. I say burn them.*), so V.1 does not need his words. A deed pays III.1 and still roots VI.3. The fear should be the plain fear the orchestrator asked for, the survivors' rumour. IV.5 has just shown it on this very day: *the old sailors turned their faces from the sea.*

**Rewrite:**
> The old sailors on the wall would not go down to it. The soldiers went, and dragged it up the stones, and fired it along the tide-line. Harl of the burning shore broke a rib of it across his knee, and fed it in. One by one the fires went up, as lamps go up along a quay at dusk. The Captain let them burn the most of it, and stood among them, still.

The rewrite shows fear and hatred as deeds. It has no *for*, no formula and no custom, and the quay-lamps and the still Captain are kept.

**For the orchestrator, Book-wide.** Read across the drafts, a grey plank or boat nearly always draws a call for fire:

| Leaf (draft) | Who | What is said or done |
|---|---|---|
| IV.3 (g06) | ▒▒▒▒ | *"Burn it"* |
| V.1 (g07) | Harl | *"Burn it," of every plank* |
| VI.3 (g10) | Harl | *what he had said of every plank of the war: "Burn it."* |
| Epilogue (g11) | the ship-masters | *"Burn it," said one of them*, with a soldier running for fire; *Their fathers had told them…*; *No ship-master… had ever laid a hand on a grey boat* |

No single leaf names a custom, but together they teach one. I recommend:
- V.1 as above;
- in VI.3, Harl's *"Burn it."* said once, without *every plank of the war*;
- in the Epilogue, R6b's option (ii) (no fire is sent for), or the ship-master's cry kept without *Their fathers had told them*.

### 3 · V.1: the question arrives late, and the turn is buried

The plank's promise (*Marks on the wood.*) comes at word 176, and nothing before it says what the Keep lacks. The want is set out only at word 265, as an inventory (*Of things that might speak…*), and it rests on a "saying" of the axemen. A saying is the very form of the lore that was cut. Then the turn, *I let go.*, comes before Jory and Enno with Della, so both trail after it.

The fix comes in three parts. Raise the want in one line at the top. Turn the saying into rumour, the same rumour the shore laughed at in IV.5. Then move the others before Seren, so that the touching builds by three (craft rule 8):
- {{Halyna}} get one word;
- the others get nothing (*Wet planks*; cold and not cold);
- Seren gets too much, and lets go.

**Rewrite (the opening, after *As it began, so it hath gone on.*):**
> Nigh a month had the grey sails lain off this wall, and what they were, none of us wist. The night the first assault was broken, the tide brought their wreck in under the wall: …

**Rewrite (the want):**
> Of things that might speak, we had the mute stones in my chest, and a bundle under the seal of {{Wendhessa}} that no pair would break. Now we had this. Axemen of the felling had sworn in their cups that the black wood would put a thought into a man's hand, if he rested it there long enough. The shore had laughed at them. Naught else was left us to try.

**Rewrite (after *one word was all they could tell.*):**
> They rose stiff from the stones, and others came down to try it. First came Jory of Eldhythe, that sitteth tonight at the back of this hall, beside Voss. He laid his hand on it, laughing. "Wet planks," said he, and went up the shingle whistling, the tune and never the words.
>
> Then came Enno and Della, that walked up the mountain hand in hand. Their four hands they laid on the plank together. He said the wood was cold, and she said it was not, and both were right.
>
> When they too had gone up, I sat where Rhyna had sat. Alone I laid mine own palm on the grain. Something came up into it out of the wood, too great to hold. It was a river in flood, and I a girl with a cup.
>
> I let go.
>
> Halvard put the lamp back in my hand.

After this come the leaf, *It held.*, the ink that would not dry, *The word looked very small on its leaf.*, and the gate. The turn moves to word 643 of 826, with 182 words after it (the leaf, the gate and the close), and nothing is lost. Jory alive and laughing, on the leaf after the reader watched him die, is memory theme 4 at its lightest: the good of him, kept. Two small mends ride in this passage:
- the misplaced relative (*Jory of Eldhythe came first, that sitteth…*);
- the refrain, which must change (craft rule 22). V.1 repeated I.3's *a tune the old ship-masters hate* after IV.5 had already named the tune, so it becomes *the tune and never the words*, which pays IV.5.

### 4 · IV.5: the endings stack into pastiche at the ship-masters

The leaf as a whole is under the cap, but *cometh* (line 47), *laugheth* (49) and *argueth* (51) fall within five sentences. That is the 14-in-830 fault the judges named, in miniature. Keep *cometh*, because the Epilogue quotes the saying. Recast the other two, by voice §1.5's own methods: the imperative and the modal.

**Draft:**
> Then said one, "The shore laugheth, for the shore will never have to meet it." … And who argueth with writing?

**Rewrite:**
> Then said one, "Let the shore laugh, for the shore will never have to meet it." … And who will argue with writing?

*Let the shore laugh* is also bitterer in a ship-master's mouth. Then fold the saying into the paragraph of the other three. It is the fourth cup set down, not a great line of its own.

### 5 · IV.5: the middle is a file on the rumour, and Voss has lost his second-hand voice

Voice §4 gives Voss *So my grandmother told it me* and forbids him certainty. The ramming paragraph (lines 25–29) is told as plain fact, from no one's eyes, in Seren's epic cadence. A man clinging to a spar could not have seen *where the load rode heaviest*. That image is IV.6's, the facing leaf's: *low, where they were heaviest*. Leave it to the wood. Mark the hearsay once, and cut the turn that is made twice. *Wherefore told she me that tale above all? For her brother was in it.* repeats *She said it of her brother.* with no new fact.

**Rewrite (lines 25–31):**
> Out of the grey a boat came at them, burning, into the wind and against the current. Screaming it came, as gulls come at boys that rob a nest. Low it struck them both, and the black wood in their holds took its fire. After came the rain, on the heads of two crews.
>
> Three came home.
>
> Daveth came home on a spar, with the sea running out of his coat onto the floor my grandmother had swept. So she told it me. All that autumn the three told it, and never again set foot in a boat.
>
> After them the outpost men sware in their cups to a boat shoved off burning, with a dead man in it, that turned. Three words of ours, they sware, the grey man spake; but which three, no two agreed.

Then let *Daveth drank on his tale, and the harbour drowned him a stone's throw from his mother's house.* stand alone and cold, with no question after it.

*Two crews* also removes a muddle. The draft's *more than twenty men*, a few lines before *Now the ship-masters say twenty* (meaning boats), makes the reader count the wrong thing.

---

## The rest, numbered

1. **V.1, the headnote.** *and I have mended it not* is bad grammar: with an auxiliary, *not* follows the auxiliary, so the line reads as Yoda order. It also collides with II.1's headnote (g04: *of all the words in this Book, those only I have not mended*), and its sign sentence repeats the tale's *On the facing leaf I drew the sign.* Every other leaf of Seren's opens *Laid by Seren Two-Inks.* **Rewrite (23 words):** *Laid by Seren Two-Inks. I was twelve, and of all on that shingle the lamp was the one thing given me to hold.* This gives one human touch and plays on *hold*. She was twelve at the banner (I.2), and this is a month later.
2. **V.1, the hinge.** *not as fire burneth* puts an *-eth* on the first instant of a knowing, which voice §0.4 and §1.6 forbid. Write *It burned, she said, not as fire, but as cold iron in the deep of winter.*
3. **V.1, the pictures.** There are eight in 813 words:
   - the sea turning each piece;
   - the quay lamps;
   - the mason's scoring;
   - the mother by a sick child;
   - cold iron;
   - the wave;
   - the river and the cup;
   - the dressed stone.

   Cut the mother. It sits at the halt, where the plainest words win, and it is the Guest's own image (IV.3's one simile; g10 cut Tarnard's for the same reason). Write *So Rhyna sat down by the plank, and laid her palms flat on the grain.* The rest are short, from a trade, and earn their place.
4. **V.1, Hale.** *He said it in three words, as runners do:* glosses I.3's law, and the line already shows its own three words. *He had run his first holding that morning.* retells I.3. Cut both, so the line follows straight on: *Past the fires he went, and past the Captain, to {{Halyna}}.* / *"Marks on the wood."*
5. **IV.5, Merrick's evening.** The draft reads *Two lines more we sang not on the quay, lest a ship-master hear.* / *One evening Merrick heard them, eldest of the ship-masters.* Heard what, if no one sang them? And the appositive lands on *them*. Write *Two lines more there were, and those we sang not on the quay, lest a ship-master hear.* After the couplet, write *Once a child began them, and Merrick heard, eldest of the ship-masters.* This keeps *the two lines we never sang* true at the halt.
6. **IV.5, the dangling modifier.** In *he was coming home…, low with black wood*, it is the man who is laden. Write *his boat low with black wood, and a second in his wake.*
7. **IV.5, one-line paragraphs.** There are 16 of 38, and voice §3.4 expects four to eight great lines to stand alone. When everything stands alone, nothing does. Make these joins:
   - the pipes go into the stones paragraph (as v1.3 had them);
   - *Then said one…* goes into the sayings.

   Keep these alone: *She said it of her brother.* · *Three came home.* · the pair *There were two boats.* / *Now the ship-masters say twenty.* · *At night she did not laugh.* · *His father was Daveth.* · the pair *Merrick told him to stop.* / *I did not tell him to stop.* · *The tune stopped.* · the cairn · the cold hearth.
8. **IV.5, the frame line.** *Thus the children sang it, and sing it still:* is fine. Do not let anyone put *Then* back, for the writer's reason.
9. **Cross-leaf: the ship-masters' saying.** IV.5 has *the boat that cometh for you when ye die*. g11's Epilogue has *…when you die*. They must match, and *ye* (subject) is the Book's grammar. Tell g11. On the writer's question 1: the sayings are not in voice §1.7's fixed list, so archaize them, but by one *-eth* only (problem 4).
10. **The BOOK FIVE Argument.** Drop the tail and the semicolon. Write *The war: a doom set in motion by the dead, crewed by the living, against a people who had never known they were the foe.* (23 words; Jack's line word for word). *How each side learned the other at the wall* is V.7's turn, and the Argument should not spend it.
11. **The writer's question 2, Harl's plant.** Take neither the words nor *every plank*. Use the deed in problem 2. III.1 already roots his temper.
12. **Locks: all hold.**
    - {{Halyna}} take plural verbs throughout, with no tag.
    - There is no singular *they*.
    - ▒▒▒▒ appears only inside the song, word for word.
    - There is no holy mark, the Captain is unnamed, and no one is aboard the grey fleet. The rewrite's *what they were, none of us wist* keeps that dark.
    - Both songs and Jack's *We forget… But Mystwood remembers.* are word for word.
    - The hood after IV.5 is rightly gone.
13. **The memory theme is light and right.** *What they said, none knew, nor asked.* stands against *We forget.* with no comment. Add nothing more. Jory's slow rope at the death (problem 1) is the only addition it needs.

## Keep, whatever else changes

- **IV.5:**
  - *the sea laughed not*;
  - *She said it of her brother.*;
  - the fingers and the flat hand;
  - the double *for* (*for we were the biggest… and for the least of them*), which is Seren's play at its quietest;
  - *He is not gone out.*, paying the master who went into the rain;
  - *I did not tell him to stop.*, which echoes Brenn's *I did not stop them* without a word said;
  - *under no roof but the rain*.
- **V.1:**
  - the sea turning each piece to see its underside;
  - *the light was mine to carry*;
  - *they had but the shore's*;
  - *It held.*;
  - the river and the cup;
  - *I let go.* / *Halvard put the lamp back in my hand.*;
  - *The word looked very small on its leaf.*
