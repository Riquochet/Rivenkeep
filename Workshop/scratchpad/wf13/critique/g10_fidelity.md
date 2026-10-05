# Fidelity critique: g10, VI.3 The Knowing of the Green Wood (new Plain Words)

Checked `wf13/plain/g10.md` against Book VI.3 (`wf11/book_v3.md`, lines 2578–2722), the old Plain VI.3 (`wf11/plain_v3.md`, lines 2176–2296), and the primer (H34, §§1–7). I also checked the source tales behind each gloss: V.1, V.2, IV.3, IV.5, VI.1, VI.2 and II.1.

**Verdict.** The leaf is faithful and close to ready. Every beat is there, in the Book's order. The one insertion is the Guest paragraph, which §7 asks for. Every name, number and teller is kept. The fixed lines and echoes are verbatim: *We remember our home too.* · *We remember.* · *Wood that knew the sea…* · *The broken grain met, and held.* · *the lamp burned down a finger's width* · *A net is only knots holding hands.* · *the last of the light caught on their two chisels* · *This is as far as one people can go alone…* / *The rest needs the other.* · *into the wind and against the current* · *the width of one old voice* · the liturgy.

The markup matches the old Plain exactly (checked with the logic of `_markup_cmp.py`). The marker sequence is TOKEN, W, RIPENS, then HALYNA×3 with the native block between the first and second, then `W: line 3 only`. The `::: native legend_stonwryt_halyna chip` block is byte-identical. The pair-names are the same set (`{{Halyna}}`, `{{Orvenna}}`). `{LAST_THRONE_AT_HAVEN}` appears twice, as in the Book and the old Plain. The Two Homes blockquote is byte-identical. Leaving out the closing `---` is fine, because the assembler writes rules from the Book skeleton.

The leaf has no singular *they*, no old words, no semicolons, no Christian terms and no custom of burning. Harl's *Burn it* stays his own word.

Nothing is spoiled. Naelear is new at H34. The Thrones being the eldest pillars was known at H33, the breath of the sleeping trees at H27, Tarnel's death at H16, and the Guest's killing and gift at H16 and H19. Merrick's father was known at H12. The deliberate mysteries are kept: no cause is given for the turn, nothing says where the boat went, *our last mark* stays bare, *the first heart* is left as the caption has it, and the token is never named.

The five fixes below are required. Items 6–8 are smaller, and each is marked optional where it is.

---

## Required fixes

**1. Headnote: restore Seren's full name.** The Book's byline is *Laid by Seren Two-Inks*. The old Plain kept "Seren Two-Inks", and every other new-Plain Seren headnote keeps it (g03, g04, g06, g07, g09). g10 drops "Two-Inks", which loses a name. Change

> `*I, Seren, who write this Book, held the lamp, and I laid this tale.`

to

> `*I, Seren Two-Inks, who write this Book, laid this tale, and I held the lamp that night.`

(If the word count allows, g07's half-clause *for the two inks I write {{Halyna}}'s words in, one for each of them* can follow the name. It isn't required.)

**2. The Thrones' gloss implies the Thrones were cut timber. That is wrong about the lore.** VI.2 says the Thrones were *the eldest of the Naelsaen … the last pillars standing at the edge*. The long-lived *drew [them] out of the earth, and grew [them] into thrones*. They are the pillars that were *not* felled. As written, the appositive *the great trees at the fog's edge that our grandparents' axemen cut for timber* attaches to *the oldest of the black pillars*. A newcomer will read that the Thrones were grown from felled trees. Change

> `The people of the wood behind the fog had grown them from the oldest of the black pillars, the great trees at the fog's edge that our grandparents' axemen cut for timber.`

to

> `The people of the wood behind the fog had grown them out of the oldest of the black pillars, the last of those great trees still standing at the fog's edge after our grandparents' axemen had cut the rest for timber.`

**3. "taller than the harbour-houses on our quays" places the tenth Throne on a quay.** The Book gives only a measure: *higher than a harbour-house*. The haven is the token `{LAST_THRONE_AT_HAVEN}` and may be any of the ten, including Sandreach, which *had no harbour* (III.1), or inland Holtward. *On our quays* says something about the site that the Book leaves open (§4, item 21). Change

> `a hill of timber taller than the harbour-houses on our quays.`

to

> `a hill of timber taller than a harbour-house, one of the big inns where our ship-masters drank.`

(Or just `taller than a harbour-house.`, which also saves words.)

**4. The Stonwryt gloss invents a rule: "always in stone".** The Book says only *Never ere then had a mark of ours gone into wood*, which is a thing that had never happened, not a law. II.1 defines the Stonwryt as *a vow sealed in living rock*, cut by the pair's own hands, and gives no rule against wood. Writing *may cut it, always in stone* turns the moment into a rule being broken. That is new lore (§1.2), and it repeats the next sentence. Change

> `Every bonded pair has its own mark, which the guild calls the Stonwryt, and only the pair's own hands may cut it, always in stone. No mark of ours had ever gone into wood before.`

to

> `Every bonded pair has its own mark, which the guild calls the Stonwryt, and only the pair's own hands may cut it. No mark of ours had ever gone into wood before.`

**5. The coin gloss: "struck under a master pair's mark" is not what II.1 says.** II.1 says *the master-pairs of the havens struck their marks on coin*. The mark is on the coin, not above it. Change

> `struck under a master pair's mark: trust, sealed in stone.`

to

> `struck with the mark of one of our master pairs: trust, sealed in stone.`

---

## Smaller fixes

**6. The Guest paragraph: name who killed him.** `the Guest was killed on that step` is accurate about the place (IV.3: *he went down on his knees again, where he had kneeled with his gift*). But the passive voice leaves a newcomer free to think someone else killed him. The point of our kneeling, and of IV.3's *a killing by our own*, is that it was our people. Change

> `The warden kicked it into the dust, and the Guest was killed on that step.`

to

> `The warden kicked it into the dust, and his men killed the Guest on that step.`

Keep the rest as it is. It is right to give no warden's name, no ▒▒▒▒, no burning boat and no link to the timber-boats.

**7. (Optional, implication made plain) "It wasn't an order, and it wasn't a wound."** A newcomer can't know why a *wound* was expected. The hearth knows. IV.2's heart came to {{Halyna}} *as a wound is, and not as a tale*. V.6 says the carvings were cut *in the wound*. And under the Thrones' judgements *the grain cried out* (VI.2). One clause makes the contrast plain without adding lore. Suggested:

> `It wasn't an order, like the carvings, and it wasn't a wound, like the grief that older wood had given them.`

**8. (Optional, standalone clarity) "the one he taught me on the Road".** *The Road* is never tied to the march glossed two paragraphs earlier. Suggested: `the one he taught me on the Road, that long march over the mountains, a knot for every mile.` If words are tight, change the earlier gloss instead, to `on the Road, our long march over the mountains to this Keep`, so the name and its gloss meet once.

---

## Length (no action required, two optional trims offered)

By my count the leaf runs 1,959 words against the Book's 1,256, which is 156 per cent. That leaves out comment lines and the native block. The writer's own count was 154 per cent. Either way it is a little over the usual ceiling. Fixes 3 and 4 already save about 6 words. Two more trims cost no fidelity:
- `I said the name over three times before I wrote it, to hear whether it would hold, and it held.`: drop `to hear whether it would hold,`. That clause comes from V.1, not from VI.3's Book line, and *it held* already carries it.
- The headnote is about 85 words against the primer's 30–70. With fix 1 applied, the separate `held the lamp` clause can go if the body's *I followed them with the lamp* is thought enough.

Don't cut Merrick's father or the Guest paragraph. §1.2 and §7 ask for both.

---

## The writer's "Unsure" items: rulings

1. **"In six winters no one had ever said *We remember* back to the wood."** **Keep.** The custom that nobody answers a wood tale is the hearth's own, and every wood leaf so far ends *And no one answered.* (primer §1.6, §3.2). The line states a fact the hearth knows on this night. It doesn't borrow the Epilogue's reflection (*A child had answered the green wood, when none of us could*). Without it, a newcomer can't see why the girl's two words matter.
2. **Merrick's father and the burning grey boat, two sentences after the turn.** **Keep.** §1.2 gives this exact gloss as its model of allowed embellishment. No cause is given for either turn, and the Plain never says the burning boat was the Guest's. *At the fog's edge* is close enough to IV.5's *coming home from the edge … out of the grey a boat came at them*.
3. **The girl's lamp.** **Correct as written.** VI.1 says Hesk's own lamp was found burning on the ice, and *a fisher-girl set one there, and lit it*. So *she has kept a lamp burning on our north wall, where Hesk lit his mother's lamp* is exact. Don't call it Hesk's lamp.
4. **"Only {{Halyna}} can know carved wood."** **Keep.** In V.1 Enno and Della lay four hands on the plank and get nothing. In the Epilogue Seren writes *there is none now to know the wood for me* while {{Idrenna}} and {{Orvenna}} still live. The plural-safe *can* is fine.
5. **The when-line's "the year we took back our ten cities".** **Keep.** It matches VI.1's when-line and is true of this night, since the tenth Throne has fallen.

---

## Checked and clean (no change)

- **Beats, in order.** These all match the Book: the Throne all day, then the nine dead hearts, the Captain at evening, dusk inside, the sliver, the lamp brought down, six winters of searching, both hands, the drop that hissed, *Home*, *We remember our home too*, Rhyna weeping, Naelear and Mystaeri, then RIPENS, the iron and the sky, *seed*, the moss and the elbow, the fisher-girl, *Home* and *a boat*, no Stonewright boat, the boatwrights, Tarnard's keel, Harl's plank, the planks speaking for us, the stem keyed (Penna holds, Ormund strikes once), the mark, *The wood took it*, palms and hands, the lashing and the knot, Tarnard's saying, a day's ride, the evening tide, the sliver, coin and chisels, *Let them go*, the kneeling (soldiers, Kael, the Captain last), the Captain's knees *now*, the Guest (inserted), *the gift, and the kneeling*, the wave, Harl walking it out, the fisher-children, the girl foremost, the turn, the ship-masters, *They did not look away*, the liturgy, the silence, Ebba, the girl's *We remember*, the hearth, the song.
- **Names, numbers and tellers.** Seren (except item 1), {{Halyna}}, Halvard, Rhyna, the Captain, Tarnard, Tarnel, Harl, {{Orvenna}} (Ormund, Penna), Kael, Hesk, Merrick, Ebba of Fenholm, Naelear, Mystaeri. The numbers are the tenth Throne, nine hearts, six winters, three times, one hand and two chisels.
- **Glosses checked against their source tales.** The silent plank was *silent for so long* (V.2: it gave nothing until the Night of the Naming). The two planks fit *like the two halves of a split log* (V.2; their meaning is kept dark). The breath is *held up between their crowns* (VI.2). On the Guest's step, the gift went *into the dust* (IV.3). Tarnel *died of the cold beside me* (IV.3). *A knot for every mile* is right.
- **The pair-names** keep plural verbs throughout, and *one beginning and the other finishing* never says which half is whose.
- **The song** keeps the old Plain's verse unchanged. Its meaning is right, its line count is five, and line 3 stays under `W: line 3 only`.
