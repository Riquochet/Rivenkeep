# g11 · The Epilogue and the Book of Knowings · fidelity critique

*What I checked it against:*
- R6b's Epilogue and Knowings entries (a)–(h), §0, §0.1 and its five open questions;
- R6a's Part 1 seeds that pay in these leaves;
- outline §8 (the Epilogue and the Appendix) and §10;
- the reckoning (§2.9, B9, C7, C8, the datelines table);
- `book_v2.md` lines 2700–2930;
- voice_v3 (§1.5, §1.7, §6, §7) and craft (§2.2, §2.3, §3.5, §3.6, §6);
- the builder, `wf10/book/build_story_html.py`;
- the sibling drafts as they stand now: g01 (Contents, the foreword, I.1 and the facing leaf), g02 (I.2), g03 (I.4), g04 (II.1, II.3), g05 (III.2), g06 (IV.3), g07 (IV.5), g08 (V.2, V.5), g09 (V.7, VI.1), g10 (VI.3) and w01 (IV.6).

I also read the sibling critiques' asks of g11. I ran `count_v3.py` on each leaf split out (`critique/_g11f/epi.md`, `kno.md`), and `plain_check.py` on the Epilogue twin. Line numbers are g11.md's.

**Verdict.**
- These leaves are clean on most locks:
  - every song and fixed line is verbatim;
  - all three native blocks match v2.0 byte for byte, keys included;
  - the table is identical to v2.0's;
  - pair-names take plural verbs, and there is no singular *they*;
  - no ▒▒▒▒ is needed, and Brenn appears only as the source of the three sounds;
  - the datelines fit the reckoning;
  - both leaves are under their ceilings.
- **One fix touches the custom (fix 1).** A ship-master's *"Burn it"* now repeats the warden's own order from g06. With the soldier running for fire, the coast still burns a grey boat by reflex. That is the custom by another road.
- **Four lost elements break locks that other leaves plant (fixes 2–5):**
  - the staff loses both who took it and the law that gives *I know the stair* its meaning;
  - the archive chest, which the foreword plants, is never paid;
  - the Argument no longer matches g01's Contents;
  - the lintel loses *none of his line is left*.
- **Fix 6 is a factual slip against I.1 and I.2.** *My first night at this hearth* is wrong: Seren wrote down Kael's tale the night before.
- Fixes 7–12 are smaller restorations and one density-cap breach. Fixes 13–20 are optional, or calls for the orchestrator.

The budget ledger at the end shows that fixes 1–9 fit only if fix 1 takes option A.

---

## Fixes, most important first

### 1. L50, L52, L62: the fire beat still has the shape of the custom. Drop it (R6b option ii).
- **What (option A, recommended):**
  - L50: keep the first sentence (*The old ship-masters would not go down, for their fathers had told them of the boat that cometh for you.*). Cut *"Burn it," said one, and his voice shook. A soldier ran for fire.*
  - L52: cut *Ere the fire came,*, so it reads *The children went down in a crowd.*
  - L62: cut the whole line.
  - Net −32 words.
- **Why:**
  - **The words are now the warden's.** g06 IV.3 l.155 has ▒▒▒▒'s order: *"Burn it," said he, "and shove it off, and give it the tide. Leave naught to show."* The writer's note (§2) calls the echo deliberate. Jack's fix is that the burning was one weak man's cruelty, done to hide a deed, and *no custom*. Put the same order in an old ship-master's mouth over a beached grey boat, have a soldier run at once to carry it out, and the reader learns that this is what the coast does with grey boats. That is the custom again, given as fear (Jack: it "muddies the story… make it less impactful").
  - **The beat was there only to break the custom.** In v2.0 it was born of *By the old way of the coast it should have been burned*. The outline's "custom broken" frame has been retired for VI.3 (g10 notes §3; R6b's index). Keeping the frame here keeps the custom's shape.
  - **VI.3 already plays the same beat.** In g10, Harl says *"Burn it."*, a palm is laid on the wood, and *None brought fire to the shingle.* The Epilogue would repeat it step for step: *Burn it*, a hand on the bow, no fire. Craft §2.2 says to tell a beat whole once. It would also add a fourth *"Burn it"* to IV.3's, V.1's and VI.3's, beside III.2's and VI.1's *burn it*.
  - **The masters' fear already stands without it,** in *would not go down* and *Never had a ship-master laid a hand on a grey boat* (L58). That is what makes Merrick's hand land. Fear alone was the brief's mend: "use plain fear of grey boats spread by the survivors' rumours, or drop the beat".
  - **R6b's must-survive "the brand quenched in the sea" yields here** to Jack's fix and to direction (6). R6b itself offers this option as (ii) and leaves the choice open (open question 2).
- **Option B, if the orchestrator keeps the brand:**
  - take the warden's words out of the master's mouth: *One cried out for fire, and his voice shook. A soldier ran for it.*;
  - keep L52 and L62;
  - make the same change in `g11_plain.md`.

### 2. L108: the staff has lost who took it and why the stair matters.
- **What:** *Ere that spring was out the staff was gone from the gatehouse, **and no one saw the Captain take it**. Where it leaned there is a clean stroke in the dust of seven winters. If ye doubt the tale, go and look at the dust. **The work is done.** I know the stair.*
  - +12 words.
  - Fuller form (+19): instead of *The work is done.*, use g03's law in its own words, *When the work is done, it is laid down in it.*
- **Why:**
  - **The Captain is never named in the passage.** Without him, *I know the stair* is a riddle with no subject. The point of v2.0 (*no one saw the Captain take it*) and of outline scene 13 ([should]) is that he laid down his staff in the chest at the foot of the shaft, because his work is done.
  - **The law is the seed being paid.** R6a I.4 (e) seeds *the law of the staff → III.2 → the Epilogue*. g03 l.40 plants it (*When the work is done, it is laid down in it*), and g05 III.2 l.183 echoes it (*A staff is cut for its work, and leaveth it not*). g05's notes (l.320) say *The Epilogue keeps "when the work is done"*, and g03's fidelity critique says that "without it, the reader cannot see that the war's end is the work's end".
  - **Its last statement comes 25 leaves after the plant.** Four words of it, turned (*The work is done.*), are a refrain, not a cross-reference, so craft §2.3's cut does not apply.

### 3. Closing inventory (after L110): the archive chest is never paid. Restore it in one line.
- **What:** one sentence before *Grief is an inheritance*, for example ***This Book lieth now in that chest, among the mute stones, with the gift from the dust and the Stone out of the Grey.*** That is +24 words (minimal form +13: *This Book lieth now in that chest, with the gift and the Stone.*). The extra *-eth* is fine: the leaf would have 7 in about 900 words.
- **Why:**
  - The foreword (g01 l.146) ends *This Book is ink. … Till then it lieth in that chest, among the mute stones.* The chest also runs through IV.1 (*the chest at my knee*) and IV.3's annal (g06: Wendhessa's hands, frost on both handles, *Tarnel and me*).
  - R6a's foreword (e) seeds *the chest … → the Epilogue*. R6b (e) lists *the foreword (the archive chest)* among *the Book's last locks*. Outline scene 15 says the chest *now holds the Book, the gift and the Stone… side by side*.
  - The writer's notes (§5, last row) flag the chest as unpaid. A seed planted in the first leaf of the Book and never paid is a lock broken, not a fold.
  - It also lets the gift kicked into the dust come to rest beside the Book: memory theme 4 felt, with no new lore.
  - *Lieth … in that chest, among the mute stones* turns the foreword's own words.
- *Optional, R6a [may]:* the granite (*{{Halyna}} would have it cut in the granite… when peace is come*). Leave it unsaid. The chest line already answers it.

### 4. L3: the Epilogue's Argument must match the Contents.
- **What:** change *The tellers dead, one scribe left, and a grey boat come back.* to ***What the grey sent back.***
- **Why:**
  - g01's Contents (l.73) already print *What the grey sent back.* under EPILOGUE. g01's notes (item 4) say *g11 line 3 must change to match*.
  - The writer's own flag (§3, last bullet) is right that the old line gives away *{{Halyna}} are gone* before the leaf opens (craft §3.5: the Arguments spoil nothing).
  - The Arguments sit outside the tale proper, so this costs nothing in the count.
  - The Appendix's Argument already matches g01 (l.77).

### 5. L28: the lintel must say that the line ends.
- **What:** *Beneath Halvard's name in the lintel of the western stair the stone is smooth, **and none of his line is left to cut it**.* That is +9 (minimal +6: *and none is left to cut it*).
- **Why:**
  - g04 II.1 plants the smooth stone as a waiting stone. The founders' leaf (l.19) says *the first of them cut his name in the lintel of the western stair, and left the stone below it for his sons*, and l.29 says *beneath the last the stone is smooth*.
  - Bare, the Epilogue's *the stone is smooth* reads the same as II.1. The payoff is that it will now stay smooth. R6a II.1 (e) seeds exactly this (*Halvard's name the last on the lintel, "no one of his line is left to cut it"*), and outline scene 2 has it as [may]: *there will be none under it*.
  - The writer's note (*The smooth stone says it*) is true only for a reader who remembers II.1's *for his sons*.

### 6. L40: Seren's first night at the hearth was the night of Kael's tale, not her own.
- **What:** ***The night I laid my first tale, {{Halyna}} laid my two hands on the stone.*** (+2)
- **Why:**
  - I.1's headnote (g01 l.183) has Seren at the hearth on *the first night this hearth asked a tale*, writing down Kael's.
  - I.2's headnote (g02) says her own tale came second: *this hearth had heard but one before it*. Its first line is *Tonight I was afraid to speak, and {{Halyna}} laid my two hands on the stone.*
  - v2.0 has *On the night I laid my first tale at this hearth*.
  - Taking I.2's *laid my two hands* also makes this a true echo of I.2, which suits the memory-theme kindness the writer placed here.
  - The Plain twin has the same slip (*My first night here*). Mend it there too.

### 7. L19: the vow has dropped out from under the capstone.
- **What:** *Face down above them are their mark, **their vow** and the Title, cut on the night of the Rite…* (+2)
- **Why:**
  - g03 I.4 l.82 has *I held the lamp while {{Halyna}} cut their mark and their vow under the new stone … Beside the vow they cut words that are not a vow*.
  - The founders' leaf (g04 l.21) cut *our mark, and our vow beside it*.
  - Outline scene 2 ([new]) and R6b beat 4 both name *the mark and the vow*.

### 8. L30: keep the strip's formula.
- **What:** *…and bound it **on a pike** over the gate.* (+3)
- **Why:**
  - The strip is a refrain that counts down (craft §3.6). Its words are fixed by V.5 Count I (g08 l.104, *…and bound it on the pike over the cairn*) and V.7 (g09, *bound a strip of his cloak on a pike over them*).
  - v2.0 has *on a pike over the gate*.
  - The last strip should be bound in the same words as the first.

### 9. L48: the slate-coloured sea is on R6b's must-survive list.
- **What:** *In the seventh spring, on a morning of thin rain, **when the sea lay like slate**, out of the grey came a small grey boat.* (+6)
- **Why:** R6b (c) lists *slate-coloured sea* among the Epilogue's must-survive elements. The writer's notes (§3) cut it as a "small picture". Jack: "I like all of the elements." It is one clause, and craft allows one painted picture to a movement. This movement has none until the children *parted … as water before a keel*.

### 10. L114: two archaic verbs in one sentence.
- **What:** split it: *Over the one grave the torn cloak flieth yet. The sea hath not finished.* (±0)
- **Why:**
  - voice §1.5 caps *-eth* and *hath* at one to a sentence. L114 carries both.
  - Splitting also lets the sea line stand alone as the echo of Corlen's *"Wait. The sea has not finished."* (g05 III.2).
  - *Orchestrator's call:* g05 keeps Corlen's *has* as a saying outside the dial, as g06 keeps *Stone does not translate*. If Seren's echo should quote him, write ***The sea has not finished.*** as its own sentence.

### 11. Closing inventory: Hesk's line belongs here (craft ledger).
- **What:** one line in the closing inventory, for example ***At every dusk the same child lighteth the north lamp.*** (+10). Match VI.1's final wording: g09's fidelity fix 6 may make it *a lamp on the north wall*.
- **Why:**
  - craft §2.2's ledger, which is binding, gives Hesk's death its *Elsewhere, a line only* in **the Epilogue**.
  - R6b (c) lists *the lamp* as must-survive.
  - The writer dropped it because VI.1 pays the first lighting. But VI.1 pays one night. The Epilogue pays the rite going on (memory theme 3), with Hesk's *Someone has to keep a light* now a child's nightly task.

### 12. L84 depends on g10. Lock it there.
- *Twice had I held the lamp to it, under the new capstone and across this stem* holds for the capstone (g03 l.82, *I held the lamp while…*).
- It does not yet hold for the stem. g10 l.84 still reads *The lamp burned down a finger's width.*, which puts no lamp in Seren's hand.
- g10's fidelity fix 3 (*I held the lamp, and it burned down a finger's width.*) must land. If it does not, change L84 to *Twice had I seen it cut, under the new capstone and across this stem.*

### 13. L144: the parts note (outline "keep it whole"; R6b: one line).
- **What:** after *Here are but the heads…*, add one line: ***The parts, who waited on whom and when the heart meant to turn, stand in their places in this Book.*** (+20; the Knowings has 35 words of room)
- **Why:**
  - Outline §8 Appendix: *Keep it whole: Seren's note on the roots and the parts.*
  - R6b (g) asks for one line, not none.
  - Without it, a reader who meets *Here are but the heads* cannot tell where the rest went. The table's whole morrows (*whole morrows out of heads already cut*) lean on it.

### 14. L36–38: the first scribe to outlive the tellers (optional; outline "keep").
- **What:** after *This is mine.*, add ***I am the first scribe to outlive the tellers.*** (+9)
- **Why:**
  - Outline scene 3 marks the line "keep". It pays g04 II.3's *This Book must outlive its tellers. That is why it is Seren that writeth it.*, which L36 now leaves unpaid. L36 pays only II.3's *go where we two cannot*.
  - The foreword's *Every scribe before me was one of a pair. I write alone.* (g01 l.132) is already answered by L13, *I write this alone*.
  - Take it only if the budget allows after fixes 1–11.

### 15. L28: {{Idrenna}}'s bench (optional; outline [should]).
- **What:** before the outliving line, ***All the next day {{Idrenna}} sat on one bench by the gate, and prayed in two halves.*** (+17). No prayer text: V.7 tells it whole (g09 l.49–51), and the writer's fold of the words is sound.
- **Why:** R6a II.3 (e) seeds *Idrenna's seat → V.7 I (the prayer) → the Epilogue*. The seat runs through II.3 (*that sit by the door tonight*) and V.7. Only the image is lost, not the words.

### 16. L114: the wind that speaks the Title (optional; outline scene 16 "keep").
- **What:** if words allow, end L114 with *… and the old ones say the wind speaketh the Title.* Watch the cap in fix 10: give it its own sentence.
- **Why:** outline scene 16 keeps it and R6b beat 27 lists it. It is a folk saying, not lore that explains a deed. Dropping it is a fold the outline did not ask for. Lowest priority. If nothing else fits, accept the fold and say so in the notes.

### 17. L173: *I said not so* can be misread.
- **What:** ***I told her not so.***, or *I said it not.* (±0)
- **Why:** in HEAVY word order, *I said not so* can read as Seren answering *"Not so"*, which would contradict the havens: she claims the stones say something before she knows it. v2.0 is *I did not tell her so*, and R6b (c) wants the answer to be *I did not know*, set against *they said nothing*. The mirror of Brenn's *I said not that it was so* (g06) survives either way.

### 18. L11 and L169: one form for Seren's opener.
- g04, g06, g07, g08, g09 and g10 print *Hold the stone, Seren.* bare. g03 and g11 put it in quotation marks.
- g10's Jack-eye item 14 asks for one form for the whole Book. The bare form is the majority.
- This is the orchestrator's ruling, and it costs no words.

### 19. L167: the Last Note's one italic line (markup).
- v2.0 gave the Last Note a dateline and a headnote. The draft has one line, *Laid last, the night after the reading.*
- The builder (`split()`, `LAST_NOTE`) opens the unit on the exact bold head, which matches. Its dateline test needs a fully italic, all-capital line with ` · `, which no v3 dateline is, so this line will be set as the teller line.
- That is acceptable. But the builder's dateline rule must change Book-wide for the short v3 datelines, and the Last Note should be checked when it does.

### 20. Before assembly (markup).
- Strip `---` and the whole `## WRITER'S NOTES` block (L195–293).
- The builder takes a `##` line as a Book heading. A `### 1 · Counts…` line would hit `UNIT_IDS[b[2]]` and raise a KeyError.
- Carry fixes 1, 2, 3, 5, 6, 7, 8, 9 and 11 into `g11_plain.md`. Its Epilogue twin passes `plain_check.py` today: 85.0% of the Book, FK 3.5, overlap 13.4%, every row ok. It must move with the Book.

---

## Budget ledger

`count_v3.py` on each leaf split out:

| Leaf | Tale proper (ceiling) | Headnote | Dateline | Sentences | *-eth* |
|---|---|---|---|---|---|
| Epilogue | **891** (900), 1.0% under | 46 / 50 | 6 / 8 | 73 · mean 11.7 · <10w 42% · >30w 0 (max 28) | 6, 1 in 149: within the cap, but L114 holds two (fix 10) |
| Knowings with the Last Note | **1,165** (1,200), 2.9% under | 44 / 50 | 8 / 8; the Last Note's line is 7 | 94 · mean 12.4 · one sentence over 30 (37), which is the table's header row | 2 |

- **Both ceilings are met.** Neither leaf reaches voice §7's 5–10% margin, which is an aim, not a cap.
- **The Epilogue's arithmetic with these fixes:**
  - fix 1A: −32;
  - fixes 2 (+12), 3 (+13 minimal), 4 (0), 5 (+6 minimal), 6 (+2), 7 (+2), 8 (+3), 9 (+6), 10 (0), 11 (+10): together +54;
  - that comes to about **913**, so about 13 words must come out of the joints;
  - one candidate is L54's *when none of us could* (−5), since VI.3 shows that silence; the writer should find the rest in the same way.
- **If fix 1 takes option B,** fixes 2–11 cannot all fit. Then the order of sacrifice is 9, 8 and 11, before 2, 3, 5, 6 or 7.
- Fixes 14–16 fit only if the joints give more.
- **The Knowings:** fix 13 (+20) brings it to about 1,185 of 1,200.

---

## Checked and clean

**The custom, apart from fix 1:**
- no *custom*, *old way* or saying anywhere in either leaf;
- *the boat that cometh for you* is IV.5's rumour, in IV.5's own grammar (g07 l.47; g07's fidelity item 14 locks it);
- the Knowings never leaned on the custom;
- *Burn* in the table and in the mason's note is the Emberhythe plank's order and Esthaer's Judgement, and nothing more.

**Brenn:** named only as the source of the three sounds (L175).

**Songs and fixed matter, all verbatim:**
- *Two at the Gate*, diffed against v2.0, split *Ormund to the comma and Penna the rest*, which answers V.7's silent first voice;
- the half-Title *In the memory of our home, our families...*, with its one wrong word;
- *Stone does not translate.*, in the leaf and echoed in the Last Note;
- *Hold it, and it will hold you.*;
- *Stop… Sky… Dying…*;
- *We remember.*, in the hearth's answer;
- *This I lay as it was laid for me.*;
- *God taketh not the one without leaving the other a work to do.*, word for word as g04 l.120.

**Native blocks:** the three blocks (`legend_stonwryt_halyna` chip, `legend_stone_epilogue` stone, `legend_three_stones` chip) are byte-identical to v2.0. The `<!-- MIXED -->` marker is kept. No FACING LEAF or PROLOGUE marker belongs here; v2.0 keeps both in I.1, and g01 l.281 carries `<!-- FACING LEAF: filled by the Epilogue -->`. The table is identical to v2.0, all twelve rows. The count works out: 7 + 8 + 8 + 8 + 7 = 38, plus 8 Judgements, is 46, and two Thrones carried an older carving whole.

**Pairs and pronouns:**
- *{{Halyna}} are gone* · *cannot yet hold* · *{{Idrenna}} … were … have outlived* · *{{Orvenna}} sang*;
- every *they* is the pair, the stones or the Mystaeri, so there is no singular *they*;
- Halyna speak only in the remembered split line, so no *we two* is needed.

**The wood's side:**
- Seren's Last Carver lines are her own inference, from IV.6's root-to-root knowing (w01: *every hull that came against your wall bare our grief in it*);
- the grain itself is the fixed native English;
- *It was cut so that one could read it alone* answers *Rhenear* without saying so.

**Datelines against the reckoning:**
- *The fourth year after the homecomings* (C8);
- the seventh winter for {{Halyna}} and the seventh spring for the boat (§2.9);
- *the dust of seven winters*, which runs from the Rite in W1 to the seventh spring;
- the Knowings, *through the war, and closed four years after*, is the same year as the Epilogue;
- the Last Note's *this winter* falls in that year.

**Crossing seeds that hold:**
- *till the wall fall* (g04 II.1 and II.3);
- *go where we two cannot, alone, and carry this Book on* (g04);
- the Covenant, named and withheld in II.3 (*Ye will understand it when it is yours to understand*) and paid at L36;
- the stem keyed, the mark across the join, the sliver on its moss and the chisels in the bow (g10);
- *It was the same child.*, Ebba's great-granddaughter (g10);
- Merrick, Daveth's son, home on a spar (g07, g10);
- *It had gone home, and it had come home.*, against IV.6's *the wood knoweth the way home*;
- the Guest's three words, *the right thing said truly*, against g06 l.119 (*They were the right words, and truly spoken*);
- *a people of doors* → the open gate;
- the Last Note's road for the stones: IV.1's pillars, IV.5's harbour-house and pipes, VI.1's pack;
- *the quay laughed at three axemen home on a spar* (g06 l.181);
- *So was I answered, when I was small* (memory theme 2; g06 notes);
- the sound-writing, which g06 left to the Last Note on purpose;
- the soldiers' Hasty names in the table, against V.2's wood forms (g08).

**Memory theme:**
- item 4 at the death: {{Halyna}}'s hands on Seren's on the stone (fix 6 sharpens it);
- item 3: *Grief is an inheritance…*, the last one left laying *This I lay…*, and *both halves alone*;
- item 2, in the Last Note: felt, not said.

Each is light, and none adds lore.
