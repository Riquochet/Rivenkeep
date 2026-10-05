# g06 · Fidelity critique: the Book Four heading, IV.1 and IV.3

Checked against R6b (IV.1, IV.3, §0.1, §0.2), R6a §0, outline §8 (IV.1, IV.3), §7.6, §7.8, §7.10, §7.11, §10, reckoning, cast, puzzle, `wf10/book_v2.md`, v1.3 (`wf7/book/legends_v13.md`), voice_v3, craft, and the current drafts that share seeds with these tales (g01, g02, g04, g05, g07, g08/V5, g10, g11, w01, w02).

**Verdict.** The draft is faithful. No custom of burning, no echo of one, Brenn never strikes, ▒▒▒▒ throughout, no holy mark, every fixed line verbatim, the markup exact, and the datelines agree with the reckoning. One budget breaks: the IV.3 annal is at 159 against a cap of 150. Below that, the fixes are small restorations of liked wording and one pronoun lock.

---

## Counts (`count_v3.py`, each tale split out)

| Leaf | Draft | Cap | With fixes 1–6 applied, and 9 for IV.1 (tested on a scratch copy) |
|---|---|---|---|
| Book Four Argument | one line, 9 words, no spoiler | one line | same. It also matches g01's contents |
| IV.1 dateline · headnote | 7 · 38 | 8 · 50 | 7 · 34 |
| IV.1 tale proper | 965 | 1,000 | 970. Longest sentence 28, mean 10.9, 55% under 10 words. Prose without the litany averages 12.1, inside Seren's band |
| IV.3 dateline · headnote | 8 · 36 | 8 · 50 | unchanged |
| IV.3 tale proper | 1,289 | 1,300 | 1,284. Crisis third still the shortest (10.3 / 8.8 / 10.1) |
| **IV.3 annal** | **159 ✗** | **150** | **150** |
| *-eth* forms | IV.1: 2 · IV.3: 7 | one per sentence | unchanged; never two in one sentence |

---

## Fixes, most severe first

### Must

**1. IV.3 annal: 159 words against the cap of 150.**
- **Why:** voice_v3 §7 and craft §3.5 set the cap, and the new memory-theme line (*The Council kept the letter, and forgat the Guest.*) put the annal over it.
- **What:** keep the line where the writer put it. It is the place memory theme item 2 names, and it reads cold. Then take the nine words out of the joints, not the elements. I tested this; it comes to exactly 150.
  - `At every blot {{Halyna}} stopped, and ye heard a silence in the place of the name.` → `At every blot {{Halyna}} stopped. Ye heard a silence where the name was.` (−3; the blot-silence stays.)
  - `Brenn died within the year, as a man setteth down a load.` → `Brenn died, as a man setteth down a load.` (−3. *Within the year* is a v2.0 time-stamp. The token, *as a man setteth down a load*, is what craft §2.2's ledger keeps.)
  - `When the havens fell they bare the chest out` → `At the Fall they bare the chest out` (−1. g05 and g11 already use *the Fall*.)
  - `his hand on one handle and hers on the other` → `his hand on one handle, hers on the other` (−1.)
  - `At morning frost lay on both handles, and neither rose.` → `At morning frost lay on both handles. Neither rose.` (−1. It is colder, and it sets up *Tarnel did not wake.*)
- **Do not** take the writer's option (c), *to Tarnel and me*. It loses *the youngest*, which v1.3, the outline (§7.8) and cast all keep: the worthless chest went to the least.
- **Do not** cut *So far the words of Brenn.* (it is v1.3's) or *with his free hand* (voice_v3 §4 quotes it as the model kindness of the dead).

### Should

**2. IV.1, Halyna's opening line: they must say *we two*.**
- **Where:** `"We lived it not,"`
- **What:** `"We two lived it not,"`
- **Why:**
  - Outline §4.3 [must] says that when Halyna speak of themselves, they say *we two*.
  - The reckoning (l.171) reads this line as their own lineage: born about B−60, so their fathers' fathers did the felling.
  - IV.3 opens their speech the same way (*We two hold the stone,*).
  - IV.1 is the reader's first Book Four meeting with the pair, so the device should show here.

**3. IV.1 headnote: cut *in the old archive-hand*.**
- **What:** `{{Halyna}} read them me by night, and I copied after them so fast that my letters leaned like reeds in a wind.` (34 words)
- **Why:**
  - It is reading-lore (R6a (g)), and g05 cut the same phrase from III.1 for that reason.
  - g04 already uses *the old hand* for the founders' Hal (II.1, II.3). A second "old hand" muddies the two.
  - Nothing in IV.1 needs it. {{Halyna}} read and Seren copies, so Rhyna's finger finding the line while Seren bends the lamp stands without a gloss.
  - It also removes the writer's §5 request for a plant in the foreword.

**4. IV.1, the bed: restore *single*.**
- **What:** `a merchant of Tidesmeet had one pillar hewn into a single bed.`
- **Why:** this is the outline's kept line (scene 4 ★) and the wording of v1.3 and v2.0. A whole pillar for one sleeper is the vanity the litany climbs to. Without *single*, the bed is just furniture.

**5. IV.1, the clerk's line: restore *to it*, and end the lead-in with a full stop.**
- **What:** `A clerk had written one line more, so small that twice I bent the lamp to it ere she could read it.` Then the italic line follows as its own paragraph.
- **Why:**
  - *Twice I bent the lamp to it* is an R6b (c) must-survive and craft's own wording (§2.3, §6.5). *Bent the lamp* alone is unclear.
  - A full stop matches how the letter's lead-in sits (*…with the same care.* then the letter).
  - It also stops the counter reading the lead-in and the fixed line as one false 31-word sentence.

**6. IV.3, the warden: restore *on the Trade Council*.**
- **What:** `He held the post by his father's name on the Trade Council, and was scarce older than his runner.` (+4)
- **Why:**
  - It is in v1.3, v2.0 and outline IV.3 scene 2. The calibration sample dropped it, and nothing logs the drop.
  - It ties the weak man to IV.1's Council, the one that sent the axes, shelved the warning, and asks *Is it so?*
  - It makes the new annal line bite: the Council kept its own man's son's lie.
  - It adds no lore.
- **Approval:** this touches the calibrated sample, so it needs the orchestrator's yes.

**7. Writer's notes §5: withdraw the request that IV.2 and V.4 keep the clerk's line "word for word".**
- **Why:** those are wood leaves. They may hold only what the wood knows (voice_v3 §5; outline §9), and quoting a Shore roll would make one leaf explain the other.
- w01's IV.2 already has it right in the wood's own words: *At the last, along the whole edge, the stumps put up nothing.*
- Only VI.3, which is Seren's, may quote the roll verbatim.

**8. Writer's notes §5: a ruling on *Stone does not translate.***
- Keep it exactly as written, with *does*. It is one of Jack's lines kept verbatim (outline §10.2: IV.1 and the Epilogue), and fixed matter sits outside the dial.
- g11's Last Note echo (*for stone does not translate*) stays as it is.
- Do not change it to *doth*.

### Could (each is a few words; the budget allows all of them)

**9. IV.1: restore *reduced to ornament*.**
- **What:** `Others hung in the harbour-houses, reduced to ornament.` (+1)
- **Why:** R6b (c) lists *reduced to ornament* as a must-survive. Craft §6.6 objects only to *holy pleas reduced to ornament*, and the *holy pleas* half is gone.
- **Leave it as is if:** *reduced* is ruled a verdict.

**10. IV.1: the one call allowed at the head of a catalogue.**
- **What:** after *The rolls keep the count, cargo by cargo.*, add `Hear it now, and hold it, for it is ours.` (+10)
- **Why:**
  - R6b §0.7 counts *Hear now… and hold it* among the rites that stay.
  - Craft §3.5 allows it once a leaf, at the head of a catalogue, when it names no outcome. g05 uses it so in III.1.
  - v2.0's *Hear now what the rolls keep… and hold it, for it is ours* is not in the writer's list of drops; only *Hear it as I copied it* is.
- **If not restored:** log it as dropped.

**11. IV.1 close: keep v1.3's ★ pair together.**
- **The problem:** outline scene 13 keeps *But humility came too late. / The first dark sails were already on the sea.* as one unit. The draft now sets the guild's share paragraph between the two lines.
- **What:** move *In our archives the stones lay yet… We will not lay it all on the Council.* up, to follow *Glad were we, as men are glad that mend a sea-wall in the calm.* Then *But humility came too late.* comes next, and the sails close the tale.
- This still ends on the guild's share and then the sails, as craft §2.3 asks. The gladness also sits against the locked stones.
- This is a matter of taste: the draft's order is also within the rules.

**12. IV.3: plant Tobe in one clause.**
- **What:** after the oath paragraph, add `Old Tobe, eldest of us, had fished the edge thirty years.` (+11; the tale proper would be 1,295)
- **Why:**
  - Outline IV.3 names Tobe among the people *we come to love*. R6b (g) keeps him for exactly this clause and the washing.
  - In the draft he arrives cold at the washing of the poles.
  - This is a sample-level change, so it needs the orchestrator's call.

---

## For the orchestrator (not g06's to fix)

**13. Strip the notes before assembly.** The `---` and the `## WRITER'S NOTES` block must be removed. The builder reads `## ` lines as Book headings.

**14. The builder gives split pairs outside `<!-- HALYNA -->` only one ink.**
- Two pairs are affected: IV.1's opening split line, and IV.3's *She carried it every step,* / *and after the passes…*. The second comes from the sample.
- They have no cue paragraph. `wf10/book/build_legends_html.py` gives two inks only after a paragraph ending *the other finished:* (or the SPEECH_CUES), so both halves will set in one ink.
- **Rule once for the whole Book:** either the builder learns the v3 split pair (two consecutive quoted paragraphs, the first ending in a comma), or the pairs need a marker. Do not wrap them in HALYNA. That would tag a Seren leaf as Halyna-told.

**15. The second half of Seren's refrain belongs to no leaf yet.** *I tell myself so every time* is said nowhere: g01, g02, g04, g06, g07, g10 and g11 all use only *Hold the stone, Seren.* Craft §3.6 wants it once, then turned in the Epilogue. Assign it, probably to I.2, the first of Seren's own leaves.

**16. One seed is now carried by no leaf: why {{Halyna}} asked leave.**
- The outline and puzzle (knot 2) had it: IV.2's shape (*we cut on [mute thing]… it did not [answer]*) showed them what the mute stones beside the sealed bundle were. Puzzle calls this "the hinge between IV.1 and IV.3".
- g01 carries {{Idrenna}}'s leave but not the reason, and w01's IV.2 headnote does not carry it either. IV.3's headnote must not (craft §3.2).
- If it is wanted, the place is one clause in IV.2's headnote. Otherwise, accept the loss.

**17. Brenn's laughter (voice_v3 §9.1) still needs Jack's word.** Either way, V.5 (g08) *We laughed. God forgive us, we laughed.* holds, as the wall's own laughter.

**18. The Plain Words twins for IV.1 and IV.3 are still owed.** The IV.3 twin inside `samples/IV3.md` fails §11.

---

## Checked and holding

**IV.1 elements: all present, or folded with a logged reason.**
- the opening's *never read what they had written*;
- the blackish veil and the night-watch question;
- *The answer, when it came, was not written in our hand.*;
- the Mystholders: plumb-line, oak, iron, rot;
- the full litany: need → vanity → the stain → the bed, then *He slept in it, and was proud.*;
- Halvard turning the leaf;
- the regrowth bought for scaffold, and the triple *They cut it…*;
- the clerk's line, staged;
- *like a dying enchantment*, *fortune*, and the mortar picture;
- the warning, read once and shelved;
- frost on a window, and *Stone does not translate.*;
- the archives and the harbour-houses, with *Men drank under them, and did their reckoning*;
- the letter between poles and oars, and the blot;
- *lost at the edge*;
- *What I held, I knew not.*;
- *not by wisdom, but by the fickleness of men*;
- the plain-fear root, *no crew would row within sight of the grey*, which is clean;
- *No one decided it.*;
- the forgetting, the children, and the aside;
- the late turning, with the sea-wall picture shrunk to a clause;
- *it was we who turned the key* (planted, then paid) and the guild's share;
- the dark sails.

The two *Added in Seren's hand* lines are cut, as craft §3.5 requires. Their content survives elsewhere:
- the pleas are in w01's IV.2 (*So on the mute thing we cut our plea*);
- the sound-writing is in g11's Last Note (*cut our words among their letters by the sound*).

Silent losses I accept as economy, with no fix needed:
- v2.0's *in the flat hand of clerks whom nothing moved*;
- *Mute and beautiful, the stones came down… among the timber*. IV.2's question, *whither they went*, is still answered by the archives and the harbour-houses.

**IV.3 elements.** These are the sample's, plus one line.
- Every R6b (c) must-survive is present.
- Folds I accept:
  - *we could hear it on the water…* goes into *would not look, and looked*;
  - *I saw it when it was done* goes into *The blows I counted*;
  - Hale and Wick are dropped from the close. g08's V.5 pays the oath: *Wick, the youngest yet, sware it loudest.*
- The seal and {{Idrenna}}'s leave have moved to g01's foreword.

**The custom of burning.**
- None in either tale.
- The burning is ▒▒▒▒'s order: *Leave naught to show.*
- Tobe only washes the poles.
- No cursed-blade scream, no *as every man on that coast*.
- *fit for nothing now but the fire* is gone.
- IV.1's *the year of the burning boat* is plain fear.

**Brenn.**
- *They* seized, broke, drew, cast, set alight and shoved.
- *One of them took up my pole*; *The blows I counted*.
- *I say* we *… No hand laid I on him. I did not stop them. A boy was I among the men.*
- His hands touch only the stone.

**Fixed lines, checked against v2.0 character for character:**
- the letter (twice);
- *Stop… Sky… Dying…*;
- the warning;
- *Stone does not translate.*;
- the runners' oath, and *Not as Brenn carried.*;
- the stain line;
- the clerk's line;
- *There was no wind, and the boat came anyway.*;
- *We were a people of doors.*;
- *He slept in it, and was proud.*;
- *No one decided it.*;
- *But humility came too late.*;
- *The first dark sails were already on the sea.*;
- the Amen, twice.

There are no songs in these tales.

**▒▒▒▒.** Every blot is four glyphs. The warden is never named, and *the warden* appears only as a title.

**Pairs.**
- Plural verbs throughout: *{{Halyna}} have laid their four hands*, *laid theirs*, *Neither of them spake*.
- No *he and she*, no tag lines.
- No singular *they*. *We wist not that it is but how they speak* is plural, his people.
- *whoso kneeleth*.
- The one gap is fix 2.

**No holy marks.** Only *God*. *The half of something, cut off in the middle* is kept, and *a holy thing* is cut.

**The wood's side.** Neither stone leaf decodes its facing wood leaf.
- Brenn sees the blade *turned to his own arm* and does not understand it.
- The wood-scream is reached by weighing facts.
- In the second spring, IV.1 knows only what the rolls show (*been given naught*).

**Seeds and payoffs, checked against the current drafts:**
- the report → g07's IV.5 (*who argueth with writing?*) → IV.3, where Brenn ran it;
- *lost at the edge* → IV.5's Daveth, and IV.6;
- the harbour-house stones and *those children* → IV.5 and g11's Last Note (*So was I answered, when I was small*);
- the litany → w02's VI.2: the spans, Holtward's roofs, the hall on the ice, the cranes;
- the blot → the guild cut the name (the IV.3 annal);
- *the chest I carried up the mountain* → the IV.3 annal and g01;
- the warden's words → *The Grey Boat* (*Burn it and shove it and give it the tide*);
- the stone *picked out of the dust*, *not once held*, and *a day and a night* → w01's IV.4 (*a hand took us out of the dust… held us not*; *a jolting in the dark, a day and a night*);
- *Between their hands he went down on his knees again* → IV.4, word for word;
- the three axemen → IV.5;
- *under one cloak* → g04's II.3 (*She woke beside him.*);
- Tarnel's knot → g10's VI.3;
- twelve → I.1;
- the oath → g02's I.3;
- *the Guest*, first named in the annal → IV.4's headnote (*what the Guest had given*).

**Datelines.**
- IV.1: *The second spring, in the Second Tide.* That is Cam 10.
- IV.3: *The third winter, in the Tide of Remembering.* That is Cam 15.
- Both agree with reckoning §3 and the outline. Neither carries an event date.
- Inside IV.1, *A year had we read* fits the reckoning: the chest was opened in the first winter, and the Harvest rolls lay at the bottom.

**Markup.**
- These match v2.0 exactly: `## BOOK FOUR · THE BOOK OF THE WOUND`, the italic Argument, `### IV.1 · …`, `### IV.3 · …`, `::: native legend_seal_wendhessa chip` with its caption only, `<!-- HALYNA -->` and `<!-- HALYNA END -->`.
- v2.0 has no `::: native`, FACING LEAF or PROLOGUE marker for IV.1, and none is needed.
