# g06 · FIDELITY CRITIQUE · Book Four heading and Argument, IV.1, IV.3

Checked `wf13/plain/g06.md` against `wf11/book_v3.md` (IV.1 lines 1116–1204, IV.3 lines 1286–1416), the old Plain (`wf11/plain_v3.md` 950–1206), `wf13/plain_primer.md` (H11, H16, §1.7, §3, §4, §7), and Jack's verbatim ledger (`Rivenkeep/Docs/Research/Rivenkeep_Legends_Plan.md` §11).

Overall the draft is faithful. Every beat, name, number and teller is there, the markup matches, nothing is told before its night, and every mystery stays dark. The fixes below are for one Jack line that was changed, one wrong lore claim, two places that add meaning the Book leaves to the reader, and some small polish.

## FIXES (most important first)

1. **[MUST] IV.1, line 61: put the Stonewrights' warning back word for word. It is one of Jack's lines.** It is listed in his verbatim ledger (Legends_Plan §11: *"These trees grow in strange soil… let restraint be our guide." | IV.1*). The Book keeps it in its modern wording, even though it puts everything else into old English (like the warden's letter), and the old Plain kept it word for word too. Replace
   `*"These trees grow in strange soil. The carvings we find beside them are in a tongue we cannot read. Where we lack wisdom, let us hold back."*`
   with
   `*"These trees grow in strange soil. The carvings we find beside them bear a tongue we cannot read. Where wisdom is absent, let restraint be our guide."*`
   (Optional, if a reader needs it: start line 63 with one plain sentence in Seren's voice, *It meant: if you don't understand a thing, leave it alone.*, then *But by then trade sat…*)

2. **[MUST] IV.1, line 31: the Highreach clause is wrong about the lore and says too much too early.** *"the cranes of Highreach, which lifted every stone of that tower up its crags"* says the black-wood cranes raised the whole tower. But Highreach was built in the Days of the Havens, centuries before the Harvest (primer §6). Black wood raising *your towers* is also the Throne's own line in VI.2 (Book 2562, *"Our kin… were the cranes that lifted the floating stones"*), so it shouldn't be said here. The Book says only *the cranes of Highreach*. Replace
   `and for the cranes of Highreach, which lifted every stone of that tower up its crags.`
   with
   `and for the cranes of Highreach, the tower on crags so high that every stone had to go up by crane.`

3. **[SHOULD] IV.1, line 71: cut the sentence that introduces the letter.** In the Book, Halvard reads the letter *as he had read the oars*, flat and with no lead-in. That flatness is the point of the moment. The letter is already the one modern-English passage in the Book, so it needs no gloss. *"in four short lines"* is also inaccurate, because it is set as one line. And calling the man *a stranger* in Seren's voice, where the letter says *intruder*, takes his side before she knows anything (*I didn't know what I was holding*). That is part of what the primer says to keep dark at H11 (*what the letter hides*). Replace
   `Halvard read it out the same way he'd read the oars. It was a report, in four short lines, of a stranger and his boat:`
   with
   `Halvard read it out the same way he'd read the oars.`

4. **[SHOULD] IV.3, line 125: put Jack's wording back.** His ledger lists *"words without sentences are only sounds"* (IV.3, mirrored in V.1). The draft adds *a sentence to hold them together*. Replace
   `But words without a sentence to hold them together are only sounds, and sounds were all we heard.`
   with
   `But words without sentences are only sounds, and sounds were all we heard.`

5. **[SHOULD] IV.3, line 221: cut "We built them."** The Book ends on *We were a people of doors.* and lets the reader feel what that means. *We built them.* spells out a meaning the Book leaves open, which breaks primer §1.3 (*don't tell the reader what it means when the Book has chosen to let them find that out*). It also narrows *we* to the builders, when the law that was broken belonged to the whole people. Keep *He is yours to keep from harm.*, because primer §7 asks for that meaning to be made plain. Replace
   `We were a people of doors. We built them.`
   with
   `We were a people of doors.`

6. **[MINOR] IV.1, line 27: two glosses that don't fit the Harvest years.** (a) *"the old captains of the havens' boats"*: the lexicon's *old* describes the ship-masters sitting at today's hearth. In the Harvest they were working captains. (b) *"than their fathers had ever dared"* has no clear owner in the new sentence, which starts *Our ships*. Replace
   `Our ships went farther out than their fathers had ever dared.` → `Our ships went farther out than their crews' fathers had ever dared.`
   `The ship-masters, the old captains of the havens' boats, called them` → `The ship-masters, the captains of the havens' ships, called them`

7. **[MINOR] IV.1, line 59: explain "Stonewrights" the first time the tale uses it.** The headnote says *our builders' guild* but never gives its name (brief rule 3, primer §3.1 house gloss). Replace
   `We Stonewrights did warn the Council.` → `We Stonewrights, the builders' guild, did warn the Council.`

8. **[MINOR] IV.1, line 75: use the Book's word, *blot*.** IV.3 (line 197, *at every one of those blots*) and the lexicon both use *the blot*. The echo between the two tales works only if the word is the same. Replace
   `Rhyna laid her finger on the gap, and took it away.` → `Rhyna laid her finger on the blot, and took it away.`

9. **[MINOR] IV.3, line 115: the Trade Council is a council, not the merchants themselves.** (IV.1 line 29 already has it right.) Replace
   `his father had a seat on the Trade Council, the merchants who ran the trade of our havens, the cities along the coast.`
   with
   `his father had a seat on the Trade Council, the council of merchants who ran the trade of our havens, the cities along the coast.`

## CHECKED AND PASSED (no change)

- **Markup.** All three headings match exactly. The `<!-- HALYNA -->`/`END` pairs are at the same beats (1 in IV.1, 2 in IV.3). The `::: native legend_seal_wendhessa chip` block is identical to the old Plain (checked with diff). The blots are the same as the Book's and the old Plain's: 1 in IV.1 and 11 in IV.3. The pair-name sets are {{Halyna}} in IV.1 and {{Halyna}}/{{Wendhessa}} in IV.3, all with plural verbs. Both liturgy lines and the hearth line are exact. The `---` before BOOK FOUR comes from the assembler's Book skeleton, as it does for g04, g05 and g07. Strip `## WRITER'S NOTES` before assembly, or the assembler will stop on duplicate sections.
- **Fixed lines.** These are all exact: *Stop… Sky… Dying…*, the letter (twice), the runners' oath, *Not as Brenn carried.*, *He had never known battle. He had never known patience.*, *But humility came too late.*, *came no further*, *into the wind and against the current*, *Leave nothing to show.*, *whoever kneels at your door is under your roof*, *Hold the stone, Seren.* and *Stone doesn't translate.* (that last is the primer's Plain form of the echo, and matches g11).
- **No spoilers.** IV.1 explains only what the hearth knows at H11 and earlier. The knowing of wreck-wood (H3) is fine. *The year of the burning boat*, *lost at the edge* and the blot are all left unjoined. IV.3 explains only what it knows at H16 and earlier. The gestures, why he drew back, the boat's turn, *the half of something*, what the gift is, and the two twelves are all kept dark. The stranger is never called *the Guest*.
- **The writer's flags, settled.** (a) *sealed Brenn's words, with his stone*: safe. The foreword confirms it (Book 118: *"It lay in the chest at my feet, under the seal of {{Wendhessa}}"*), and so does lexicon §3.3. (b) *"Is it so?"* is right. (c) *Leave nothing to show*, followed by *He meant: leave nothing that could show what we had done.*: allowed (H16, primer §1.9 and §7). (d) Leaving {{Idrenna}} out (*the oldest pair among us gave leave*) is right and matches the foreword. (e) *Tarnel… shared a cradle* matches II.3 (Book 902, *She lay in one cradle with Tarnel*). (f) *carried the archive chest out of Eldhythe* matches the foreword.
- **Rules.** There is no singular *they* (every *they/their/them* was checked). Nothing is burned by custom: the forges burn it as fuel, and the boat is burned to hide the deed. There are no Christian words. *lord* means a nobleman, as in the Book. The when-lines and headnotes have the right seasons and Tides, with *grandparents' time* and *fathers' fathers*.
- **Length.** IV.1 is 142% of the Book's and IV.3 is 134%, both inside the band.
