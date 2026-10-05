# IV.4 · BLIND BACK-TRANSLATION TEST (the grain and Seren's Orrowen frame)

*wf7 workflow document, 2026-09-28. Scratch only; nothing here goes into `Docs/`. It tests `wf7/pilot_IV4.md` (IV.4, The Gift Held an Hour, at tier 3). The pilot's Orrowen and Grain Notation were read back into English using only the specs, the lexicon and the tools. The result was then compared with the pilot's English, paragraph by paragraph. Causes that were errors in the translation, the lexicon, the specs or the tools were fixed, and the tools were re-run.*

## 0 · The result in brief

| | Units | Exact | Close | Drift | Wrong |
|---|---|---|---|---|---|
| **Seren's frame** (Orrowen: the title, 7 headnote sentences, the closing line) | 9 | 5 | 3 | 1 | 0 |
| **The wood's telling** (the grain: 16 rings) | 16 | 2 | 12 | 2 | 0 |

- **One sentence was wrong** inside a drifting ring: ring 5's "The shape would have been enough" came back as "all our carving would seem not to be there".
- **The two drifting rings** are ring 5 and ring 15.
  - Ring 5 uses two readings that exist only in the concept register (CARVE for "the shape of a knowing", `{all}` for "enough").
  - Ring 15 is a cited round (`STOP½`) whose sentence lives in another round, which was not part of the test.
- **The drifting frame sentence** is headnote 5. The idiom *doss maver um*, "must", came back as "wanted". The lexicon has the idiom, but the analyzer's gloss never showed it.

**Five causes were fixed:**
1. The lexicon's *nynth* lacked "water", because of a sense-dedup bug in the builder.
2. The analyzer's `--gloss` hid set phrases.
3. The spec lacked the register-only readings (now A15).
4. The spec's §11.2 clashed with §10.3, so the validator's reading lost the file referents (now A16, and the validator follows it).
5. The pilot claimed that a split runner says "when".

After the fixes, every tool passes: the validator's tests are ALL OK, the analyzer's `--test` reports 0, and the lexicon self-check reports 0 problems. §6 re-reads the drifted units.

---

## 1 · How blind it was (read this before the scores)

**The procedure.**
1. I mapped `pilot_IV4.md` by line type and length without printing its text. I checked candidate lines for English stop-words by count, still without printing them.
2. A script then copied only these lines into `wf7/blind_IV4.txt` (369 lines):
   - the nine blockquoted Orrowen lines (§1.1–1.3);
   - the leaf-hand letter block (§1.4);
   - the sixteen knowing-form GN blocks (§2.2–2.4);
   - the canonical GN of §4, with its `#` comment lines stripped.
3. I read those lines with only `orrowen_v2.md`, `grain_v2.md`, `lexicon_orrowen.tsv`, `orr_analyze.py --gloss` and `grain_validate.py` (plain and `--literal`).
4. I wrote the whole back-translation to `wf7/bt_IV4/blind_draft.md` (23:57:45) **before** I opened the English. `blind_IV4.txt` is timestamped 23:50:34.

**Two leaks, both reported honestly.**
- **The pilot's file legend (contamination).** Before the copy, a `grep '^#'` I ran to find the section headings also printed three things:
  - the pilot's title line ("THE GIFT HELD AN HOUR");
  - the movement headings;
  - the **24 `# file` legend comments** of §4's canonical GN, which give every file's English referent ("file 7: whoever holds us", "file 12: we (the gift)", and so on).

  They were stripped from the blind copy, but I had seen them. **So the referents in my back-translation are not a blind result.** The uncontaminated baseline for referents is the validator's reading of the comment-free GN (`wf7/bt_IV4/plain.txt`), and it lost them (§4, C4).
- **The spec itself (allowed material).** `grain_v2.md` quotes about 35 fragments of IV.4's English:
  - §7.1, §8 and §11.3;
  - the "G" rows of §18;
  - §21.4 (B2, B6, B9, B10) and §21.7.

  IV.6's ring 9 telling (§12.3) also summarises IV.4's plot from the other side. The test is therefore blind to the pilot, not to the spec. Where a sign choice has a §18 row, my reading of it benefited. The Orrowen frame was not exposed this way: the spec quotes none of it, and the lexicon holds only its title (O0900).

## 2 · The back-translation (as fixed in the draft, before comparison)

### 2.1 Seren's frame (Orrowen)

| # | Orrowen | Back-translation |
|---|---|---|
| T | *Hebbet sa re yal kethet hos clem* | The Gift That Was Held an Hour. |
| H1 | *Hosen tum Mesk Myst: kethet hy et hebbet sost, et tolm domm sa re rik Brenn hy et tuss, ul Hyll Dhumol; doss o ul lern Yebb et Pard.* | As the Mystwood remembers it: known from the gift itself, the black stone that Brenn picked up out of the dust, in the Tide of Remembering. It stands before *The Warden's Door* (or: facing it). |
| H2 | *Re heth Rhyna o hos clem lo et odh, eth re rarr o uloy niss, hosen nynth um dholm, hy vodh hebb et mesk hemm sost nayalat pynt.* | Rhyna held it for an hour at the hearth, and it came into her slowly, like a spring through stone, because the eldest wood gives nothing quickly. |
| H3 | *Re femm Halvard o nafedh.* | Halvard never touched it. |
| H4 | *Re yal o lo et lodh um et parow, eth re heth o o hosen re heth ey o, eth ew o sa re hadh et tolm hosast ul et brodhol.* | He was at the mortar in the courtyard, and he held (knew) it as she held it; and it was he who laid the first stone of the telling. |
| H5 | *Ew duss sost brodhol et trenn ul o rask, hy vodh re yal maver o wrodhol um Halyna hosen es mrodh et arra o, ul ol mrodath sa re yal lo nafedh.* | The telling of the tale was hardest at its end, because Halyna wanted to tell it as the Guest would have told it, in our words, which he never had. |
| H6 | *Re wrodha Halyna o, hos eth ullen, ul ba luth; re hadh Seren o.* | Halyna told it, the one and then the other, in two inks; Seren set it down. |
| H7 | *Amm re yal et mesk cresket, ell re omm et brodhol, doss o rellorat eth nahlennet.* | Where the wood was broken, or the telling failed, it is marked and left unmended. |
| C | *Eth re dhess nahos.* (then the coping) | And no one answered. (The end of a tale.) |

The leaf-hand block matches the romanised lines letter for letter, bites and lintels included, so it added nothing to read.

### 2.2 The wood's telling (the grain)

- **r1.** Given [the root]. We are the old wood. We were a tree in a green world, green to its edges. We fell, and the ages lay down on us as leaves lie down on leaves. The ages did not hold us; we grew dark, as hard as stone. We are not stone, though you held us for stone.
- **r2.** The ages do not hold this wood; it holds still. It gives slowly, and only what is so. A sliver of it is the dearest gift of a child [of the long-lived] (or: the dearest gift a child is given). It is given once.
- **r3.** One of the long-lived took a name, *Aelrhen*, "bond-to-stone", and an errand. Hidden in the grey, through a long life, he listened to you, the shore-men, at your nets and your walls. He gathered your words, one and one and one, as a child gathers fallen leaves.
- **r4.** At the last he knew three true words: *Stop. Sky. Dying.* He did not know how you bind words together with small words that make no sound across the water, because he never heard them.
- **r5.** He held us. Whoever holds us for as long as a tree's shadow takes to move across its own trunk knows all of us. We are a sentence. He did not know that a shore-man holds only what is carved; to you, all our carving would seem not to be there.
- **r6.** He chose the outermost hold, because of the wood: there was wood in its doors, its walls and its benches. He believed that the wood there was held holy. We knew them: our kin at the edge, felled for timber, smoothed. He laid his hand on the door-post and spoke to them; they did not answer him, because they did not live.
- **r7.** He knelt on the stones before the host, the master of the house. He gave us, his dearest gift, as one who comes in under a roof gives. He named the Aelthar in the thunder of his own tongue, and then said three of your words.
- **r8.** He had in mind the Aelthar, the holiest rite (the old carving "Kneel"), which binds gift, blood and kin across every gap between. He meant to rise, take the shore-man's neck gently, and lean brow to brow in stillness.
- **r9.** He would make a small cut in the host's arm, [hold the host's neck without gripping it?], and make a small cut in his own arm. He would ask only for the host's blood, as a gift of blood for blood. The two arms, bound each only to the other, would make the promise.
- **r10.** He knelt first, and from then the Aelthar does not stop. A shore-man's foot kicked us into the dust by the wall, and the shore-men laughed. He did not stop, because the Aelthar does not stop. He rose and took the host's neck gently, as one lifts a small child. His brow leaned to the host's brow, in stillness. He made a small cut in the host's arm.
- **r11.** The host's arm turned aside. Why, the wood does not hold.
- **r12.** His blade went lightly to the arm; the arm moved into it and broke the light cut; because the arm was moving, the blade went deep. Blood ran; the host cried out, and his men came. He did not raise his hand against them, and never made the small cut in his own arm. They struck him down; he fell at the door among the stones and died, the rite half made. We lay in the dust and heard all of it. No one took us up.
- **r13.** Of everything at your feet that looked like stone (always), only we would have spoken to you; a foot found us, and cut that off.
- **r14.** In the morning a shore-man came back to us, alone. He took us up out of the dust. He laid us away hidden; he did not know us. We lay in the dark, with our sentence, through most of a man's life. We lay in a chest among the stones. A child carried us in its two arms into the mountains. No one but you held us long. He [the Guest] carried us to your door, and from that we hold:
- **r15.** the old carving, "Stop" (the gift's own sentence, cited by its root).
- **r16.** He came to you only to speak. We have carried it the whole long road. *(Seal: this is held in the grain.)*

---

## 3 · Comparison, paragraph by paragraph

**Scores.**
- **Exact:** every proposition and relation comes back; only the wording differs.
- **Close:** every main proposition comes back; a nuance, image or modality shifts.
- **Drift:** a proposition is lost or changed.
- **Wrong:** a proposition is contradicted or invented.

### 3.1 The frame

| # | Original (pilot) | Score | Where it differs, and the cause |
|---|---|---|---|
| T | *The Gift Held an Hour.* | exact | none |
| H1 | *…the dark stone that Brenn picked out of the dust, in the Tide of Remembering; it faces the Warden's Door.* | close | *ul lern* is "before; in front of; in the face of". I led with "before", which in English can mean page order, and gave "facing" second. *domm* lists both "black" and "dark". **Reader choice; no fix.** |
| H2 | *…like water over stone, for the eldest wood gives nothing quickly.* | close | "a spring" for "water". The lexicon's *nynth* read only "a spring, a well", although its compounds *helvnynth* "sky-water" and *tantnynth* "salt-water" use it as water, and its Book lemma is "water". **Lexicon error (C1), fixed.** |
| H3 | *Halvard never touched it.* | exact | none |
| H4 | *He was at the mortar across the ward, and he knew it as she knew it, and it was he who began the telling.* | close | *um* lists "upon; … across, over". I took "upon" and lost that he was across the ward, away from the hearth. "Laid the first stone" is the set phrase O2859, "begin", which the analyzer did not show (C2). **Reader choice, and a tool gap (fixed).** |
| H5 | *The sentence at its end was the hardest to tell, for it had to be told as the Guest would have said it, in words of ours he never had.* | **drift** | "Halyna **wanted** to tell it" for "it **had to** be told". *re yal maver o wrodhol um Halyna* is the lexicon's idiom *doss maver um* (O0488, "must: need is upon Y"), past tense, with its slots filled. `--gloss` shows single words only, so *maver* read "wish, want", its first sense. **Tool gap (C2), fixed.** "Tale" for "sentence" is *trenn*'s polysemy, and ring 15 disambiguates it. |
| H6 | *Told by Halyna, by turns, in two inks; set down by Seren.* | exact | none |
| H7 | *Where the wood was broken, or the telling failed, it is marked, and not mended.* | exact | none |
| C | *And no one answered.* | exact | none |

### 3.2 The grain

| Ring | Original (pilot's English) | Score | Where it differs, and the cause |
|---|---|---|---|
| r1 | *We are the eldest wood. … until time forgot us and we grew dark and hard. We are not stone, though you took us for it.* | close | "The ages did not hold us" for "time forgot us". That `!HOLD` means *forget* lives only in the concept register. **Spec gap (C3), fixed by A15.** "Until" is not carried, because a6 is a *to* runner. That is stylistic, and the heart takes no span. |
| r2 | *Wood that time has forgotten does not itself forget. … Even a sliver of it is the dearest gift a child of the long-lived can give. We were given once. This is how.* | close | The first sentence drifted to "the ages do not hold this wood; it holds still" (C3 again: `HOLD{still}` is "does not forget"). The gift sentence came back close ("the dearest gift of a child"; "even" is lost). "This is how" is Halyna's framing and is not cut, by design (§11.2). |
| r3 | *…took the name Aelrhen when he took his errand, and it means bond-to-stone. Through a long life he listened across the grey…* | close | "Took a name … and an errand" has no "when". The pilot's note said a split runner is "how the grain says when"; §6.1 does not allow that. **Translation-doc error (C5), fixed.** "Hidden in the grey" for "across the grey" is my over-reading of the MIST band. |
| r4 | *At the end he had three, and he knew them for the right ones. Stop. Sky. Dying. He knew no way to join them…* | close | "Knew three true words" for "had three and knew them for the right ones". "Did not know how you bind words" for "knew no way to join them". Meaning kept. |
| r5 | *But he had us. Whoever held us while a tree's shadow moves the breadth of its own trunk would know the whole of it. We were the sentence. He did not know that one of you alone holds only the shape of a knowing. The shape would have been enough.* | **drift** | Sentence 4 drifted: "a shore-man holds only what is carved". Sentence 5 was **wrong**: "all our carving would seem not to be there". CARVE as "the shape of a knowing", and `{all}` as "enough", are register-only readings (C3). With A15, `CARVE{only}` and `~CARVE{all}` read by rule. **Spec gap, fixed.** |
| r6 | *He chose the outermost of your holds … he took that for reverence. We knew it for what it was: our kin from the edge, sawn and polished. … greeted them … they were dead.* | close | "Believed the wood there was held holy" for "took that for reverence"; "spoke to" for "greeted"; "smoothed" for "polished". All kept; A15 now lists greet and polished. |
| r7 | *He knelt on the stones before the master of that house and set us down, as one who comes under a roof brings his best, and spoke the name of the rite … and after it his three words in yours.* | close | "Gave us, his dearest gift" for "set us down … brings his best"; "three of your words" for "his three words in yours". |
| r8 | *This was the Aelthar as he meant to make it … the holiest rite of fellowship we have. He would rise and take the back of the host's neck gently in his right hand, where life goes up into thought, and draw their heads together until the foreheads touched in silence.* | close | Lost: "right hand" (A12 carries it by placement only), "where life goes up into thought" (the part's own gloss, §5.2, which I did not use), and "fellowship". |
| r9 | *…open a shallow cut on the host's right arm, and let go the neck, and cut his own left arm, for he would ask no blood he did not give. Then the two would press their bleeding arms together … harm to one was harm to both.* | close | `~!HOLD` came back "hold without gripping?" instead of "let go". That was mostly my misreading (hollow + mirror = "would not hold"), and A15 now lists "let go". The bind came back as "bound each only to the other" (§7.3's gloss). |
| r10 | *He made the first step. A foot struck us into the dust by the wall … He rose and took the neck as gently as one lifts a fledgling…* | close | "Knelt first" for "made the first step"; "a small child" for "a fledgling". The grain cuts the fledgling as `~SAPLING½`, by design (§18). |
| r11 | *And the host drew back. We do not know why. Fear leaves no mark on wood.* | close | "The arm turned aside" for "drew back" (A15 now lists it). The blind is exact. "Fear leaves no mark" is Halyna's gloss, by design. |
| r12 | *The blade that was meant to go a little way went deep, for the arm was moving. … struck him down on the stones of the door … no one picked us up.* | exact | The break (`lap l2 ⊳ l1`) carried "was meant to … for the arm was moving" in full. |
| r13 | *Of all the things that ever lay at a shore-man's feet and looked like stone, we were the one that could have spoken to him; and it was the one his foot found.* | close | "To you" for "to him" (file 0 is the shore). The irony is carried by the break. |
| r14 | *In the morning a man of the house came back alone … No one held us so long, until you. Here is the sentence, as it was brought to the door:* | close | "A shore-man" for "a man of the house"; "he [the Guest] carried us to your door, and from that we hold" for "as it was brought to the door". |
| r15 | *Stop the felling of the pillars at the edge of the grey … Stop, for the sky is dying, and we are dying under it.* | **drift** (by design) | The ring holds only `12: HOLD →that pocket cut { STOP½ }`. The sentence is its own round (`IV-4-gift`), drawn beside the ring, and it was outside this test's allowed files. **No fix; test it separately (§7).** |
| r16 | *That is all he came to say. We have carried it a long way, and the grain holds it still.* | exact | none |

---

## 4 · Causes and fixes

| # | Cause | Kind | Fix | Files |
|---|---|---|---|---|
| **C1** | *nynth* read "a spring, a well" and never "water". The builder's `add_sense` dropped the en_map recipe `water \| nynth` because "water" is a **substring** of "a spring (of water)". The same test also dropped "cap" (inside "capstone") and "lone" (inside "alone"). | lexicon error (builder bug) | `add_sense` now treats a sense as already said only when its words stand **whole and outside brackets** in a sense the entry has. A bracketed variant of a sense already present still counts as said. A dry rebuild in an isolated copy (`bt_IV4/lexdry/`) changed exactly 4 rows: O1839 *nynth* +"water", O0990 *hosel* +"lone", O0994 *hosk* +"cap", and O2174 *sa* drops a repeated "which (relative)". Those 4 rows were hand-applied to the live TSV. The live lexicon was **not** rebuilt, because a rebuild loses the pilots' appended rows O2858–O2880. | `wf7/lex/build_lexicon.py`, `wf7/lexicon_orrowen.tsv` |
| **C2** | `orr_analyze.py --gloss` printed single-word glosses only. The lexicon's set phrases never showed, whether contiguous (*cadh et tolm hosast* "begin", *hos eth ullen* "by turns", *ul lern*, *hy vodh*) or with slots (*doss maver um* "must"). | tool gap | New `phrase_hints()`, run in `--gloss` only. It prints `= phrase: meanings` for every multi-word lexicon entry found in the line. A two-word phrase must stand together; a longer one may have up to two words in each gap; nothing runs across punctuation; *doss* also matches its past *yal*/*gal*. On IV.4's frame it finds 13, all right. `--test` is unchanged (87 samples, 0 reported). | `wf7/orr_analyze.py` |
| **C3** | The readings `!HOLD` = forget, `HOLD{still}` = does not forget, `!HOLD` = let go, `{all}` = enough, CARVE = the shape of a knowing, SMOOTH = polished, MOUTH = greet, and HAND:stem+TURN = draw back live only in the concept register (`coverage/concepts.tsv`). A decoder given only the spec cannot recover them. | spec gap | **A15** in the new **§21.8**, continuing A6's idiom table, with a standing rule: any register reading that is not its sign's own gloss belongs there. | `wf7/grain_v2.md` §21.8 |
| **C4** | §11.2 ("a new thing-sign standing first on a file introduces a new referent") clashes with §10.3 ("a thing is cut on the file of the one it belongs to"). The validator applies §11.2 alone. Without the `# file` comments, its reading renamed file 12 (we) "a sentence" from r5, the Guest's file "mind" from r8, the shore's "three words" and "a shore-man's foot", the host's "an arm" and "a shore-man's neck", and the hold's "dust". A reader without the legend is misled the same way. | spec error (conflict) | **A16** in §21.8: a **belonging** never introduces a referent. Belongings are parts (unless the ligature is a named compound); MIND, WORD and its compounds, NAME, BREATH, HAND, EYE, BONE and BLOOD (not BLOOD×3, kin); DUST; and a CASTLE's or HOUSE's DOOR and SQUARE. The validator's `Reader.label` follows it through a new `is_belonging`. This affects the reading only, never the findings; `coverage/run_tests.py` is ALL OK and `--selftest` is ok. | `wf7/grain_v2.md` §21.8, `wf7/grain_validate.py` |
| **C5** | The pilot's ring-3 note said a split runner is "how the grain says 'when'". §6.1 makes a split one act reaching several things; time is carried by *then* runners and the span (§6.5). | translation-doc error | The note is corrected. §21.8 states the rule. The pilot's §3 findings gain a line pointing here. | `wf7/pilot_IV4.md`, `wf7/grain_v2.md` §21.8 |

**Not fixed, because they are stylistic, reader choices or by design:**
- *um* "upon" against "across" (H4);
- *ul lern* "before" against "facing" (H1);
- *domm* black/dark;
- *trenn* tale/sentence (H5);
- "until" in r1;
- "fledgling" as a small sapling (§18's own choice);
- "right/left" carried only by placement (A12);
- Halyna's framing ("This is how", "Fear leaves no mark on wood"), uncut by §11.2;
- r15's cited round.

**The comment-free reading, before and after C4** (ring 12, from `bt_IV4/plain.txt` and `bt_IV4/plain_after.txt`):

| Before | After |
|---|---|
| The shore-men go to an arm's crying out. | The shore-men go to the host's crying out. |
| The shore-men strike mind's falling. | The shore-men strike one of us' falling. |
| Three words do not take a sentence's lying down. | The shore-men do not take wood's lying down. |
| The iron goes to an arm's deep wound. | The iron goes to the host's deep wound. |
| A sentence lies down, in door many stones' dust. | Wood lies down, in most edge house behind the stone's dust. |

## 5 · Re-runs after the fixes

| Tool | Result |
|---|---|
| `grain_validate.py pilot_IV4/IV-4.gn2` | 0 errors, 0 warnings |
| `grain_validate.py --md pilot_IV4.md` | IV-4: 0 errors, 0 warnings |
| `grain_validate.py --md grain_v2.md` | as before: IV-6 as printed, 3 errors (the known K03, R19, A02); E2-01 clean; E4-01's one known warning (B17) |
| `grain_validate.py --selftest` | ok (117 signs) |
| `coverage/run_tests.py` | ALL OK |
| `grain_validate.py bt_IV4/IV-4.blind.gn2` (comment-free) | 0 errors, 0 warnings; referents now kept (above) |
| `orr_analyze.py --file pilot_IV4/headnote.txt` | every word OK |
| `orr_analyze.py --test` | 87 samples, 0 with a word reported |
| `orr_analyze.py --gloss --file bt_IV4/orr_lines.txt` | the same gloss, plus 13 set-phrase lines (*doss maver um*: must, among them) |
| `lex/selfcheck.py` | 2880 entries, 0 with a problem |

## 6 · The drifted units, re-read with the fixes (not blind: I had seen the English by then)

- **H5.** With `= doss maver um: must` shown: "The telling was hardest at its end, because it fell to Halyna to tell it as the Guest would have told it, in our words, which he never had." Now **close**; "tale" against "sentence" remains.
  - *After this test* (the cross-check of 2026-09-28): the line's two nasalised forms, *es mrodh* and *ul ol mrodath*, begin *mr-*, an onset `orrowen_v2.md` §2.5 does not allow and the I.1 pilot avoids. The clause now reads *hosen es gadh et arra o, ul et brodath orrowen sa re yal lo nafedh* ("as the Guest would lay it, in the words of the Shore, which he never had"); `orr_analyze.py` reads it clean. The tables above keep the line as it was tested.
- **r5.** With A15: "He had us. Whoever holds us while a tree's shadow crosses its own trunk would know the whole. We are the sentence. He did not know that one of you alone holds only the shape of a knowing. The shape would have been enough." Now **close to exact**.
- **r1, r2.** "…until the ages forgot us, and we grew dark as stone"; "Time forgets this wood; it does not itself forget." Now **close**.
- **r9.** "…and would let go the neck…" Now **close**.
- **r15** stays a drift until the cited round is tested.

Expected after the fixes: the frame 5 exact / 4 close; the grain 2–3 exact / 12–13 close / 1 drift (r15, by design).

## 7 · Open items

1. **Test the cited round.** Ring 15's whole meaning is the `IV-4-gift` round (`wf7/grain2_texts/GIFT.gn2`, mystaeri_spec §5.4). It needs its own blind read, given that file.
2. **A16 is a list, not a theory.** A character who is a belonging-sign (a "Hand" as a person, say) would need a person-sign first on the file, or a `# file` comment. Other place-parts (a SHORE's sand, a TREE's boughs) may want the same treatment as CASTLE's doors when a leaf needs it.
3. **SMOOTH's validator gloss** still reads "go veiled". A15 documents the telling's "made smooth", but changing the gloss would change the orders' readings, so it was left for the builder. The validator's "most edge house behind the stone" (for `EDGE{most}+CASTLE`) is also clumsy, though only in the reading.
4. **The phrase hints** allow two-word gaps inside 3+-word phrases. No false hit arose on IV.4, but watch the other pilots.
5. **The builder fix** will reproduce the 4 changed rows on any rebuild. A rebuild still drops hand-appended rows unless their recipes go into `lex/en_map/` (the pilot's standing note).
6. **The legend leak.** A cleaner future run should build the blind copy from the knowing-form file with a parser that drops comments before anything is printed, rather than grepping the pilot for headings.

## 8 · Files

**Written by this test:**
- `wf7/blind_IV4.txt`: the blind copy (Orrowen, leaf-hand letters, GN in knowing and canonical form; no English, no comments).
- `wf7/backtrans_IV4.md`: this report.
- `wf7/bt_IV4/`, the working set:
  - `blind_draft.md`: the back-translation, fixed before comparison;
  - `orr_lines.txt`, `gloss.txt` and `check.txt`, with `gloss_after.txt` after the fixes;
  - `IV-4.blind.gn2`: the comment-free canonical GN;
  - `plain.txt` and `literal.txt`, with `plain_after.txt` and `literal_after.txt` after the fixes;
  - `lk.py`: a lexicon lookup helper;
  - `lexdry/`: the isolated dry rebuild of the lexicon;
  - backups: `build_lexicon.py.bak`, `lexicon_orrowen.tsv.bak`, `orr_analyze.py.bak`.

**Changed:**
- `wf7/grain_v2.md`: new §21.8 (A15, A16, the split-runner note).
- `wf7/grain_validate.py`: `BELONGINGS`, `PLACE_PARTS`, `is_belonging`, and `Reader.label`.
- `wf7/orr_analyze.py`: `phrase_hints`, printed in `--gloss`.
- `wf7/lex/build_lexicon.py`: `add_sense`.
- `wf7/lexicon_orrowen.tsv`: rows O0990, O0994, O1839 and O2174.
- `wf7/pilot_IV4.md`: the ring-3 note, and one line in §3's findings.
