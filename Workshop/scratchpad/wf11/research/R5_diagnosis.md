# R5 · Local diagnosis of the style

*Compares the v1.3 Book with the v2.0 Book, and the old Plain Words (Modern v1.2) with the v2.0 Plain Words. Measured with `research/style_metrics.py` (full tables in `style_metrics_out.txt` and `style_metrics.json`). I read I.1, I.2, IV.3, IV.4 and the Green Wood tale (v1.3 VI.1, v2.0 VI.3) in every version.*

---

## 0 · Bottom line

1. **v2.0 is run-on because of how its sentences are joined, not because they are old.** It has twice v1.3's words. Its mean sentence is 21 words against 15. One sentence in eight runs past 45 words (v1.3: one in a hundred). It has 2.7 times the semicolons and 1.5 times the "and"s per sentence, and twenty Homeric "As when…: so" similes of 60 to 76 words each.
2. **Its archaism was costume.** *upon* (261 uses) and *ere* (72) are about 90% of its archaic words, and the grammar is modern. So the difficulty sat in length, and the Plain could only undo it by splitting sentences: "just a change in punctuations".
3. **v1.3 was not archaic either** (0.9 archaic words per 1,000). What Jack liked was its *sentence-craft*. It mixes short and long sentences, uses few semicolons, gives each big moment its own paragraph, and gets *shorter* at the climax. Its voices differ, and it never contracts. The new Book needs v1.3's sentences with real old-English grammar and vocabulary on top. Neither version tried that.
4. **Both versions read like a chronicle, and v2.0 doubled it.** Both give the ending away in the headnote, explain at the peak of a scene, and add records after the end. v2.0 added CAPITALISED datelines, name tags, and an invented custom that "muddies the story".
5. **Neither Plain Words is a real retelling.** Both follow their Book paragraph for paragraph (408/407 and 983/983). Modern v1.2 felt different only because of register. Measured word for word, it was *closer* to its Book than Plain v2.0 is to its own.

---

## 1 · The numbers

Tale bodies only. Headnotes, songs, native blocks and hearth-answer lines are left out. Per-1k means per 1,000 words.

| measure | v1.3 Book | v2.0 Book | Modern v1.2 | Plain v2.0 |
|---|---|---|---|---|
| tales / body words | 25 / 21,132 | 27 / 41,143 | 25 / 21,116 | 27 / 40,831 |
| mean words per tale | 845 | 1,524 | 845 | 1,512 |
| sentence mean / median | 15.2 / 13 | 21.0 / 15 | 13.4 / 12 | 12.3 / 11 |
| 90th percentile / longest | 29 / 75 | 49 / 93 | 25 / 77 | 23 / 44 |
| % sentences > 30 words | 9.1 | **24.1** | 3.6 | 2.0 |
| % sentences > 45 words | 1.0 | **12.3** | 0.1 | 0.0 |
| % sentences < 10 words | 39.3 | 34.7 | 38.4 | **42.9** |
| words per paragraph | 51.8 | 41.9 | 51.9 | 41.5 |
| semicolons per sentence | 0.09 | **0.24** | 0.04 | 0.00 |
| commas per sentence | 1.06 | 1.74 | 0.87 | 0.79 |
| "and" per sentence | 0.69 | **1.04** | 0.50 | 0.34 |
| archaic words per 1k | 0.9 | 9.0 (90% *upon*/*ere*) | 0.0 | 0.1 |
| archaic grammar per 1k (rough) | 0.3 | 1.2 | 0.2 | 0.4 |
| contractions per 1k | 0.0 | 0.1 | 5.3 | 15.5 |
| causal ", for …" per 1k | 3.6 | 4.0 | 0.3 | 0.4 |
| dialogue share of words | 1.2% | 3.1% | 1.2% | 3.1% |
| Flesch-Kincaid grade | 4.3 | 6.5 | 3.8 | 3.4 |
| headnote words, mean | 82 | 132 | 87 | 132 |
| epic similes (count) | 0 | 20 | 0 | 0 (but 19 "Picture a…/Think of…") |
| "the two of them" / "he and she" | 2 / 0 | 40 / 12 | 2 / 0 | 38 / 9 |
| "Hear how…" openings | 7 | 22 | 5 | 14 |
| time-anchor phrases per 1k | 0.6 | 1.6 | 0.6 | 1.7 |
| % of Plain 4-word runs found verbatim in its Book | — | — | **65.8** | **40.3** |
| Plain sentences per Book sentence | — | — | ~1.1 | ~1.7 (1.1–2.5) |

| focus tale | body words v1.3 → v2.0 | headnote | mean sentence | % > 30 words |
|---|---|---|---|---|
| I.1 The Torn Cloak | 957 → 1,521 | 36 → 117 | 11.8 → 20.6 | 4.9 → 25.7 |
| I.2 The Cry of the Bonded | 944 → 1,287 | 43 → 87 | 13.3 → 23.0 | 7.0 → 28.6 |
| IV.3 The Warden's Door | 935 → 2,150 | 86 → 175 | 12.6 → 19.5 | 5.4 → 23.6 |
| IV.4 The Gift Held an Hour | 778 → 890 | 139 → 191 | 15.6 → 13.9 | 12.0 → 0.0 |
| Green Wood (VI.1 → VI.3) | 903 → 2,659 | 39 → 126 | 17.4 → 28.0 | 13.5 → 42.1 |

**Two findings stand out.**

**First, the bloat and the run-ons are in the stone leaves and Seren's leaves.** v2.0's wood leaves stayed near v1.3 in length (IV.4: 890 against 778), with no sentences over 30 words. Their problem is a different one (§6).

**Second, v1.3 changes pace at the crisis and v2.0 doesn't.** Here is the mean sentence length by third of the tale:

- **I.1:** v1.3 runs 12.5 / 13.1 / **9.9**. v2.0 runs 20.8 / 21.6 / 19.2.
- **IV.3:** v1.3 runs 13.7 / **9.5** / 14.8, so the killing goes short and fast. v2.0 runs 19.6 / 16.1 / 22.9.
- **Green Wood:** v1.3 runs 17.8 / 17.3 / 17.0. v2.0 runs 25.3 / **30.2** / 28.5, getting longer at the knowing.

This is the measurable side of "they don't build".

---

## 2 · What Jack liked in v1.3

**Each teller is a person within three sentences.** Kael: *"Give me the stone. No, I will stand. I have sat enough this winter."* v2.0 keeps the first two and then explains the third: *"Fourteen nights I have sat at this fire, and a soldier stands to give his count."* The man has become a note about the man.

**Short sentences carry the weight.** These lines are the spine of v1.3:

- *"Some shook. Some wept. Some fell and would not rise."*
- *"I had heard men break before. I had never heard a people break. It is a sound like ice going out on a river."* Two mirrored sentences, then one picture.
- *"The True Men looked to their Captain. The Captain looked at the wall."*
- *"No one answered him. I remember the wind in the grass."* A silence given by one thing seen.
- *"Old stone does not tremble. I felt it do so under my feet."*

When v1.3 runs long, it is with "and…and" in a list, the King James and Malory habit, not clauses stacked inside clauses. Its causal *for* gives the old cadence without adding length: *"we stood at the foot and let him, for he had not told us to follow."*

**Big moments get their own paragraph.** For example *"We obeyed."*, *"It was green."*, and the turn to the room: *"He is sitting there now, at the end of the bench, with his hood up. He will tell you it was not like that. It was like that."*

**It refuses to explain.** The best line in either IV.4 is a refusal: *"And the host drew back. We do not know why. Fear leaves no mark on wood."* v1.3's burning gives one motive, a weak man's, and it is enough: *"the warden had us lay the body in its boat and set the boat alight, so there would be nothing to show."*

**Its endings are sayings, not records.** *"There is no older law among any people than this: that one who kneels at your door is under your roof. We were a people of doors."* And: *"…we were the one that could have spoken to him; and it was the one his foot found."*

**It never contracts, and it "lays".** The pun on *laid* (stone laid / tale laid) is set up in "Of This Book": *"a tale that is only told is gone by morning, and a tale that is laid is part of the wall."* That is the Seren wordplay Jack means. v1.3 has only a few such turns, but they are the right kind.

**v2.0's best lines are written the v1.3 way.** They are short and balanced, and often stand alone as paragraphs:

- *"▒▒▒▒ kicked it aside."*
- *"I did not say it was so. I said, 'It is written.' For forty years I have weighed that small cleverness."*
- *"I carried the lie in a day and a night. I carried the truth forty years, and gave it to no one."*
- *"On his back is the other half."*
- *"Tarnel did not wake."*
- *"I tied it with Tarnel's knot."*
- *"The wood took it."*
- *"I have counted those stones since: thirty-one there are, and four of them move."*

That last line, with its old word order (*thirty-one there are*), shows the target: hard through inversion, not length. **The v2.0 "elements" Jack likes are mostly these lines.** What he rejects is the text that connects them.

---

## 3 · What made v2.0 "run-on"

1. **Chains of "and", "and", "; and".** I.2's first scene sentence is 78 words: *"It was dusk on the day of the banner, and the last of the light lay thin as ash upon the snow, and the guild sat in the old ward…; and I sat among them, for I was of the guild, though I had no craft yet but the carrying of water."*
2. **v1.3's short pairs were merged.** v1.3's *"I had heard men break before. I had never heard a people break."* became *"I had heard men break on the long retreat; but never till that dusk had I heard a whole people break."* The mirror is gone, and the added qualifiers dull it. In I.1, a 40-word weather sentence now sits in front of *"The True Men looked to their Captain"* and smothers it.
3. **Suspended epic similes.** There are twenty, across fourteen tales. The reader has to hold a whole side picture (a poor man's loaf, an arch's frame struck out, a quarryman's echo, a half-built bridge) before the main clause arrives. They also break the voices. Kael has just said *"Counting is my trade, and not singing"*, and then he sings a 61-word simile. Given to a sergeant, a runner and a scribe alike, they make everyone sound the same.
4. **Tags on every noun.** *"Into the middle of the courtyard he walked, a man not tall, with the coal-black yet on his fingers and the half of a cloak upon his shoulders, and looked at the elders, and past them at the broken gate, and stood."* "The two of them" appears 40 times and "he and she" 12 times. Each one adds a clause and repeats a rule already taught.
5. **A time-stamp before each scene.** "It was dusk on the day of the banner" appears 11 times. Another example: *"In the sixth autumn, when the first frosts lay white of a morning upon the walls we had raised again, the tenth Throne fell…"* These are chronicle openings.
6. **"Measure" took over from voice.** v2.0's "Of This Book" says *"The words are the teller's, and I change not one of them; the measure is mine."* In practice that meant one long rhythm for everyone. Jack's new idea is the reverse: Seren *does* change the words, and the tellers agree hers are better.

---

## 4 · What made v2.0 "clinical", and why it doesn't build

1. **The outcome comes before the scene.** There are 22 "Hear how…" openings, for example *"Hear how the last knowing was done, the one that no one looked for."* Most follow a CAPITALISED contents line that has already summarised the tale, so the reader is told twice before anything happens.
2. **Every beat gets the same weight.** The Green Wood tale tells all of these at one pitch: the knowing, "Home", Seren quoting her own Book, Harl's "Burn it", the keyed stem, the chisel-mark, the knot, the chisels in the bow, the kneeling, Harl carrying the bow, Merrick's simile, and Ebba's great-granddaughter. With twelve climaxes, none of them is the climax.
3. **Explanations that lower the stakes.** Tobe's custom ("What the grey sends, the fire sends back…") moves the guilt from a weak man's order onto tradition: *"We knew the custom, and we were glad of it, for it let us stop thinking."* Every *why* v2.0 added, whether a custom, a lineage or an editorial reason, takes charge out of a deed.
4. **Cross-references at the moment of wonder.** In VI.3: *"I turned back the leaves of this Book, and found therein, in my own hand, three things that the wood had said to us in other years…"*. Three quotations follow, then *"So it was seed."* This is a scholar footnoting her own book: the "history text book".
5. **Too many named people.** Distinct capitalised names and titles (a rough count) went from 13 to 28 in IV.3 and from 19 to 43 in the Green Wood tale. Each arrives with an ID tag (*"Tarnard at their head, the eldest boatwright, of Tidesmeet, where the river meets the tide"*). People are introduced like entries in a register, not met in a scene.

---

## 5 · What reads like an annal in BOTH versions

1. **Headnotes written as catalogue entries.** They give rank, night, contents and custody.
   - v1.3 IV.3 gives the ending away: *"The confession of Brenn of the outpost, the man who picked up the stone…"*, and it says Halyna "laid the closing annal after it".
   - v1.3 IV.4 spends 139 words on how the knowing was done.
   - v2.0 adds a CAPITALISED dateline and contents line (*"…SEVENTY-FIVE YEARS BEFORE THE BANNER, AND OF THE RUN AFTER IT…"*). IV.3 also gets a 175-word chain of custody before Brenn speaks.
2. **The Book calls its own parts annals.** *"So far the words of Brenn. Now hear the annal."* Both versions follow the story with a record: the name cut from the rolls, who sealed the chest, who carried it. v2.0's IV.3 annal is 585 words, 27% of the tale after the story has ended (v1.3: 178 words). The Wendhessa and Tarnel material is moving, but it is told as a record.
3. **A glossary at the climax.** Between *"Then Halyna stood up"* and the cry, I.2 spends **188 words** (v1.3) or **150** (v2.0) on pair-names, "the Bonded", lineages and marriage. That is the exact peak of the tale, and it stops to teach.
4. **Rulebook passages.** I.2's laying / hauling / holding (*"this hearth has names for its hours. There is the laying… There is the hauling… There is the holding…"*) is the game's phase system written as a manual in both versions.
5. **The rite is explained before it is performed.** Both IV.4s spend most of the tale on lore and plans: 540 of 778 words in v1.3, 549 of 890 in v2.0, before "And the host drew back". That includes the rite in the conditional (*"He would rise and take… With his left hand he would open… Then the two would press…"*). Then the rite happens, and the reader gets it twice: first as instructions, then as a replay.
6. **Summary where a scene should be.** v1.3 VI.1 builds the boat in one summary sentence (*"The fisher-folk laid the keel and bent the strakes and caulked the seams…"*) and opens like a report (*"The Captain sent word that Halyna should know its heart…"*). v2.0 swung the other way and staged everything at full length. Neither chose which moment to stage and which to compress.
7. **Editorial notes inside tales.** *"Where Brenn named the warden, I have kept the blots"*. *"The tenth Throne I write here by the name it gave itself…"*. These rules belong in "Of This Book" or the design notes.

---

## 6 · Canon the style carried

- **Brenn takes part in v2.0, and v1.3 is ambiguous.** v2.0 has *"I struck him with the pole… Twice."* and the post dragging the body by the heels. v1.3 has *"We seized him… We obeyed"* and *"the warden had us lay the body"*. Under Jack's note, "we" is the post as a whole. Brenn watched, struck no one, did not stop them, and was a boy among the men. Cut the blows and any line where he handles the body or the fire. **Open for Jack:** *"I laughed"* is a boy laughing along, not a blow. I'd keep it.
- **The custom of burning.** v1.3 already had it right: the warden's order, "so there would be nothing to show". Remove Tobe's line and every echo of it.
- **"He would not let me change a word of it, and I have not."** This is in I.1 in both versions. It contradicts Seren improving every tale with the tellers agreeing. Flip it: Kael grumbles, then gives way.
- **Wood leaves are fluent in both.** IV.4 is polished "we" prose from the wood. Jack wants Halyna in phrases and half-thoughts, and Seren making the story. The seed of that form is already in v2.0 IV.4's coda: *"Then a long jolting in the dark, a day and a night. Then the dark, for half a life, and never a hand… Then small arms, two pairs, going up, in the cold; and then one pair, a long way."* Seren's added note decodes it. Build the form from that: fragments in the two inks, then the told memory.

---

## 7 · Why Plain v2.0 read like re-punctuation, and v1.2 didn't

Measured word for word, Modern v1.2 kept **65.8%** of v1.3's four-word runs, and Plain v2.0 kept only **40.3%** of v2.0's. So the difference Jack felt came from somewhere else:

- **In v1.x the gap was register.** The Book never contracts, keeps *for* as a conjunction (3.6 per 1k against 0.3), and speaks a "laid" voice. The Plain talks (*"No, I'll stand. I've done enough sitting this winter."*), glosses in passing (*"The ward behind it, the open yard inside the walls…"*), and rewrites the songs as plain verse. Switching tabs changed the voice.
- **In v2.0 the Book's difficulty was length.** So the Plain cut at the joints (1.7 sentences per Book sentence), swapped *upon*→*on*, *ere*→*before* and *ward*→*yard*, and added contractions. Compare:
  - Book: *"It was dusk on the day of the banner, and the last of the light lay thin as ash upon the snow, and the guild sat in the old ward where it had gone to grass."*
  - Plain: *"It was dusk on the day of the banner. The last light lay thin as ash on the snow. The guild sat in the old yard, which had gone to grass."*
- **It kept every ornament:** the datelines, the 132-word headnotes, all 20 similes (as "Picture a poor man at his table…"), and the full 40,831 words.
- **Splitting made it choppy, not easy.** 42.9% of its sentences are under 10 words, the most of the four: *"He looked at the elders. He looked past them at the broken gate. He stood there. Then he asked one question."* That reads like a children's primer.

---

## 8 · What the Plain Words must do

1. **Retell, don't convert.** Write each tale fresh from its beats, in the teller's voice as a modern speaker, not from the Book's sentences. Paragraphing and order are its own: start in the scene, and put each fact where a modern reader needs it. *Test:* no more than about 20% of its four-word runs appear in the Book. Against a truly old-English Book, this happens almost by itself.
2. **Easy, not choppy.** Aim for a mean of 11 to 14 words per sentence, under 30% below 10 words, and almost none over 30. Use everyday words, contractions (about 10 to 20 per 1,000), normal word order, and *because/so/but* instead of *for*. Flesch-Kincaid grade 4 or under.
3. **Gloss once, in passing**, the way v1.2 did (*"a course of stone, one layer of the wall"*). Never a glossary paragraph.
4. **No apparatus.** No datelines and no custody. The headnote is one line: who is telling, and when.
5. **Plain speech for ornament.** Say what a turn of phrase means, briefly and vividly. Use at most one short comparison per tale, never "Picture a…".
6. **Shorter than the Book, or no longer.**
7. **Fixed lines stay word for word**: the Title, *"The mortar cries out from the ground…"*, *"Rise! Rise! Rise!"*, *"We remember our home too."* and *"We remember."* Plain-verse songs follow the v1.2/v2.0 practice, with the Book's songs untouched (Jack to confirm).
8. **Voices survive in modern form.** Kael counts, Brenn confesses in short guilty sentences, and Halyna's wood-fragments stay fragments.

---

## 9 · What the new Book should take from this

- **Sentence shape:** go back to v1.3's figures. Mean around 15, median around 13, about 9% over 30 words, about 1% over 45, about 0.1 semicolons and 0.7 "and" per sentence. The crisis third of each tale should be the shortest. Big moments get one-line paragraphs.
- **Length:** about 850 words per tale, with v2.0's best elements kept as single lines rather than paragraphs. At most one short simile per tale, from the teller's own world. No "he and she" or "the two of them" once "Of This Book" has set the rule.
- **Hard through old English, at v1.3 lengths.** That means verb before subject after a fronted adverb, negation without "do", *thou/thee* in close speech, the subjunctive, and older word senses, rather than *upon/ere* swaps. Illustrations only:
  - v1.3 *"I am a counter of things and not a singer, and what I did not count I will not tell you."* → *"A teller am I, and no singer; and what I told not, that will I not tell."* This plays on *tell* = count, which is Seren's sort of turn.
  - v1.3 *"The warden kicked it aside. It went into the dust by the wall. And his men laughed. I laughed."* → *"The warden spurned it from him, and into the dust by the wall it went. Then laughed his men. I laughed."*

  The beats and the short sentences are the same, and both are harder for a first-time reader. A Plain version of the second shows how far apart the two should sit: *"The warden kicked it out of his way, into the dirt by the wall. His men laughed. So did I."*
- **Cut from every tale:** "Hear how…" summaries, explained customs, lineage tags at the climax, the rite told in advance, after-the-end records, and editorial notes. Keep only what fits "Of This Book", the design notes, or one closing saying.
