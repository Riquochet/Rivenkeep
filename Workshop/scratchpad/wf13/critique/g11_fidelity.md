# FIDELITY CRITIQUE · g11 · Epilogue (The Stone out of the Grey) and Appendix (The Book of Knowings, with the Last Note)

Checked `wf13/plain/g11.md` against `wf11/book_v3.md` (lines 2724–2898), the primer `wf13/plain_primer.md` (§1.7 echoes, §2 H35/H36, §3, §4, §5, §7) and the old Plain `wf11/plain_v3.md`. Where it bears on an echo, I also checked the sibling leaves (`g02.md` I.2, `g03.md` I.4, `g06.md` IV.1, `g10.md` VI.3).

## Verdict

The leaf is faithful and close to done. Every beat of the Book's Epilogue (40 beats), Appendix and Last Note is present, in order, with every name and number. Nothing in it is a spoiler, because H35/H36 is the end of the hearth's clock. Every gloss draws on an earlier step: the Guest's killing (H16), the green sliver (H34), the fisher-girl as Ebba's great-granddaughter (H34), the Judgements (H33), Myststone (H35), the staff's history (H5) and the second hood (H16). The deliberate mysteries are kept:
- The Stone's grain is not retold.
- The Last Carver's fate is never given.
- Why the cutting stops is not said.
- The extra *the* is not explained.
- The staff is given only as Seren's belief.
- What we send back stays open.
- Seren knows no carving.
- The meaning of the raw edges is not explained. The stem uses VI.3's own words, *the two halves of the first heart*.

I found two actual errors (fixes 2 and 3), one broken echo (fix 1), one misleading when-line (fix 4), and one place where Seren's guess is stated as fact (fix 5). The rest are smaller.

**Verified clean, so no change is needed:**
- **Markup.** Checked by script against `plain_v3.md`. The `##` and `###` headings, the `---` rules, the bold head `**The Last Note · Three Stones over the Hearth**`, all three `::: native` blocks, the `<!-- MIXED … -->` comment, the carving line `*In the memory of our home, our families...*` and the whole Knowings table are byte-identical.
- **Pair-names and blots.** The Epilogue has {{Halyna}}, {{Idrenna}} and {{Orvenna}}, and the Appendix has {{Halyna}} only, all with plural verbs. There is no ▒▒▒▒, as in the old Plain.
- **Fixed lines, verbatim.** The Title; *We remember our home too.*; *We remember.*; *Stop… Sky… Dying…*; *"Hold the stone." / "Hold it, and it will hold you."*; *God does not take the one without leaving the other a work to do.*; *If you doubt the tale, go and look at the dust.* (as the Book has it in the Epilogue); *the stair that goes no more* (matches g03); *the lamp burned down a finger's width*; *Stone doesn't translate.* (twice); *The sea hasn't finished.*; *came no further*; *no child laughed*; the liturgy.
- **Counts.** The counts 7 / 8 / 8 / 8 / 7, plus 8 Judgements, come to 46, and they match the table.
- **Banned things.** There is no singular *they*, no custom of burning, no Christian vocabulary, no old word (the only uses of *yet* mean "so far"), and no semicolon in the prose.

---

## Fixes, most important first

**1. Two at the Gate, line 3: restore the comma, so the verse matches I.2 and "up to the comma" works.** In `g02.md`, I.2 explains the song as *In every line, one of them sang up to the comma, and the other sang the rest*, and it gives line 3 a comma for that reason. In g11, line 3 has no comma, so *Ormund up to the comma and Penna the rest* can't be followed in that line, and the echo with I.2 no longer matches word for word.
- Old: `> *Two at the gate when the grey sails gather.*  `
- New: `> *Two at the gate, when the grey sails gather.*  `
- Optional, to match g02's naming: in the line before the verse, change *sang the old gate-song of the havens in its two voices* to *sang the havens' old gate-song, *Two at the Gate*, in its two voices*.

**2. Remove the gloss "our banner" on the torn cloak over the grave. It commits to a reading the Book doesn't make, and probably the wrong one.** The Book says only *Over the one grave the torn cloak flieth yet.* The grave is under the inner gate's capstone. The beat just before says the Captain bound *the last of his half* *on a pike over the gate* (Book 2751), so the nearest reading is that last strip. The banner, which is the written half, was set *in a cleft of the wall* (I.1, Book 237), and the Book never places it over the inner gate.
- Old: `Over their one grave the torn cloak, our banner, still flies.`
- New: `Over their one grave the torn cloak still flies.`

**3. Merrick: "all his life" contradicts the Book.** VI.3 says *Six winters had they turned their faces from the sea when a hull burned* (Book 2697). That means the six winters of war, not his whole life.
- Old: `He's the eldest of the old ship-masters, and all his life he had turned his face away from every ship that burned.`
- New: `He's the eldest of the old ship-masters, and through all six winters of the war he had turned his face away from every ship that burned.`
- If you take fix 8, use its wording for this sentence instead.

**4. The Epilogue's when-line reads wrongly on a first pass.** Because the appositive comes right after it, *the fourth year after the homecomings, the year we took back our ten cities* reads as if the fourth year were the year of the homecomings. *After that year* can then be taken as the year of writing. In fact the events (the seventh winter and spring) follow the homecoming year straight away, and the writing comes four years later.
- Old: `*Written in the fourth year after the homecomings, the year we took back our ten cities on the coast. It tells of the winter and spring after that year.*`
- New: `*Written four years after we took back our ten cities on the coast, in the year we call the homecomings. It tells of the winter and spring that came right after the homecoming year.*`

**5. The Last Carver: keep the whole sentence as Seren's guess (primer §4.4: "Give only Seren's guesses").** As written, *It was a hand from behind the fog* is stated as fact, and *I think* covers only his age. The Book only implies where he came from (*their reckoning*, *he never sailed*). Moving *I think* to the front keeps the useful gloss and makes it hers. (The writer flagged this as note 2.)
- Old: `It was a hand from behind the fog, young by their count, I think, and seasoned by ours, because they live far longer than we do.`
- New: `I think it was a hand from behind the fog, young by their count and seasoned by ours, because they live far longer than we do.`

**6. "Carved stone never gave Halyna anything" overstates the lore.** {{Halyna}} *read* the founders' slates in I.4. What gave them nothing was the *touch* of the mute stones (Book 1178: *have laid their four hands on them, and been given naught*). g06's IV.1 says it the same way: *These stones give them nothing.*
- Old: `Stone doesn't translate: carved stone never gave {{Halyna}} anything.`
- New: `Stone doesn't translate: when {{Halyna}} laid their hands on the carved stones from the fog's edge, they were given nothing.`

**7. Seren as "third": she wasn't "raised" in Halyna's household.** Tarnel died on the night of the pass, a month before the banner, when Seren was twelve. The Book says {{Halyna}} *took me into their hearth as its third* (Book 136), and II.3 says an unbonded child *is given to a bonded hearth as its third*. Since {{Halyna}} are dead, *was* also reads better here than *am*.
- Old: `I'm their third, an unbonded child of the guild raised in their household, because Tarnel, who shared my cradle, died before we could be sealed as a pair.`
- New: `I was their third, the unbonded child of the guild they took into their household, because Tarnel, who shared my cradle, died before we could be sealed as a pair.`

**8. Recommended: make the shingle beat's meaning plain (brief rule 5, and primer §1.2, which gives this very example).** A newcomer isn't told why the old ship-masters stop at the top of the beach, or why Merrick's hand on the boat matters. The Book's reader knows both: the ship-masters' dread of the grey-boat rhyme (H0), and that Merrick's father came home on the spar after the burning boat struck the timber-boats (H12). Each needs only one clause. This joins no puzzle lock: *came no further* stays unjoined to the warden, and no cause is given for the boat's turning.
- Old: `The old ship-masters, the captains of our cities' boats, stood at the top of the beach and came no further.`
- New: `The old ship-masters, the captains of our cities' boats, who have always dreaded the old harbour rhyme of a grey boat, stood at the top of the beach and came no further.`
- Old (after fix 3): `He's the eldest of the old ship-masters, and through all six winters of the war he had turned his face away from every ship that burned.`
- New: `He's the eldest of the old ship-masters. His father was one of the three axemen who came home clinging to a spar, long ago, when a burning boat out of the grey struck their timber-boats. Through all six winters of the war, Merrick had turned his face away from every ship that burned.`
- On length: the Epilogue is already at 171% of the Book's prose. To pay for these clauses, you could cut *So I'm bound to no one.*, which is embellishment, and the Appendix headnote's *one carving at a time*, which repeats the when-line.

**9. Small fidelity trims: new pictures the Book doesn't have.**
- (a) Old: `The children ran down in a crowd,` · New: `The children went down in a crowd,`. The Book says *went down*.
- (b) Old: `Halvard went before the lamp burned out,` · New: `Halvard went before the lamp went out,`. The Book says *ere the lamp was out*, and *burned out* adds that the lamp was left to burn down.
- (c) Old: `*And the Captain, who always keeps his hood up, put it back for only the second time.*` · New: `*And the Captain, who keeps his hood up at this hearth, put it back. It was only the second time.*`. *Always* clashes with *the second time*, because he put it back once before, after IV.3.

**10. Last Note: undo the Book's inversion (primer §1.4).**
- Old: `a child at the front asked what they say, the three grey stones that hang over this hearth.`
- New: `a child at the front asked what the three grey stones that hang over this hearth say.`

**11. Optional, for the newcomer and not for fidelity.**
- (a) The Book's own picture of *these* three stones is *letters fine as the tracks of birds on wet sand* (IV.5, Book 1508). The *frost on a window* picture belongs to the mute stones in general. Either is true, because the grey stones are mute stones, but the IV.5 picture is closer.
- (b) One clause could say how the stones came to the hearth: *until Voss carried them up from his grandmother's harbour-house in the year of the homecomings* (VI.1, H33).
- (c) *the silent plank* could take a half-clause: *the one plank that had at first given {{Halyna}} nothing* (V.2).
- (d) *Corlen of the harbour* could take *one of the Captain's Twelve, who died on the wall* (H15).

---

## For the orchestrator, with no change to g11

- **The native caption of `legend_three_stones`.** g11 rightly copies the old Plain's *the curling letters along its edge*. The Book has *the curling letters of the edge*, which more likely means the writing of the fog's edge than a border around the stone. If that's a mistranslation, it belongs to whoever owns the native blocks in `plain_v3.md`. (The writer flagged this as note 7.)
- **The `## WRITER'S NOTES` section and the top `<!-- PLAIN WORDS … -->` comment.** The assembler must strip both. Every g-file carries them, so confirm the assembler drops them before the Plain is published.
