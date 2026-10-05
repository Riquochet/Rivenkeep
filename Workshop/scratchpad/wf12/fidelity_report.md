# THE LEGENDS OF RIVENKEEP v3.0.0 · Fidelity of the three texts on the story page

*wf12 workflow document, 2026-10-03. It is not a Book leaf or a repo doc. It checks the story page `wf12/out/Rivenkeep_Legends.html` (and its web copy `wf12/out/web/The_Legends_of_Rivenkeep.html`) against `wf11/book_v3.md`, `wf11/plain_v3.md` and the merged units `wf12/units/*.md`.*

## Verdict

**The Book and Plain Words panes are faithful to their sources, character for character.** All 31 leaves are present in all three tabs, in the Book's order. Every paragraph, song line, fixed line, ▒▒▒▒ blot and lintel is there, emphasis included, with nothing dropped or doubled.

**The Original had seven faults, all in the Original pane.** Each one is fixed at its source, and the page has been rebuilt. The worst fault: **the warden's ▒▒▒▒ was missing from Seren's ink in all 12 lines where the Book has it.** The romanisation kept the blots, but the leaf-hand line dropped them, so a line such as *"▒▒▒▒ held his arm"* read *"held his arm"*. The other six were notation, tool notes and a scratch path that had leaked into the folds.

**The Original is aligned to the right Book paragraphs.** Mechanically, all 1,300 text blocks were checked. By reading, 31 paragraphs across 20 leaves were checked with the analyzer's `--gloss`.

There is no custom of burning in any of the three texts. Every tale anchor of v2 is unchanged, and **no inbound link in Docs breaks**.

After the fixes, `check_story.py` (now stricter), `check_panes.py` and the three independent checkers written for this pass all pass.

---

## 1 · What was checked, and how

The builder's own checker, `check_story.py`, compares **words only**, and it exempts the Original pane from its leftover-notation scan. So this pass wrote its own checkers, apart from the builder. They live in `wf12/tmp/FID/`:

| Tool | What it does |
|---|---|
| `fid_text.py` | For every leaf, the Book and Plain Words panes are turned back into markdown: `em` becomes `*`, `strong` becomes `**`, `span.pair` becomes `{{X}}`, `span.who` and `h4.part` become `**X**`, and drawings are dropped. The result is compared **character by character** with the leaf's source, keeping punctuation, ▒▒▒▒, `{{lintels}}` and every `*`. It also checks the leaf order of each source against the page. It was proved on a fault-injected copy: it caught a dropped paragraph, a doubled paragraph, a lost `<em>` and a lost blot. |
| `fid_frame.py` | Checks the title page, the Contents, the Book headings, the Arguments and every tale heading, character by character. |
| `fid_orig.py` | Checks the Original pane in four ways: **A**, every Book paragraph (`data-k`) has its Original block, in the Book's order; **B**, each block's own copy of the Book text matches the Book at that line; **C**, the unit item each block came from (`src`) is re-read from the unit file, and its English is checked against that Book paragraph; **D**, the page's romanisation fold matches the unit's Orrowen. |
| `spot.py LEAF LINE…` | Prints, for one paragraph: the Book's English, the fold's romanisation, the ink, the unit's word-for-word or literal reading, and `orr_analyze.py --gloss`. It runs on a private copy of the analyzer and the merged lexicon. |

---

## 2 · Results, item by item

| Check | Result |
|---|---|
| **Every tale in all three tabs, in order** | 31 leaves (the foreword, the Invocation, 29 tales, the Book of Knowings and the Last Note) plus 10 frame units. The leaf order is the same in `book_v3.md`, `plain_v3.md` and the page. Every leaf has The Book, Plain Words and Original. Each Original pane opens with the right tale's title block. |
| **The Book pane matches `book_v3.md`** | **Character-exact in all 31 leaves.** No paragraph is dropped or doubled. Every song (the verse blocks), fixed line (*We remember*, the laying formula, *And no one answered.*, the hood, the seal), ▒▒▒▒ (12 of 12) and lintel (113 of 113) is in place. |
| **The Plain Words pane matches `plain_v3.md`** | **Character-exact in all 31 leaves.** The lintels are 112 of 112 and the blots 12 of 12. Plain Words has no datelines because its source has none. |
| **The frame** | The title page, the Book headings, the Arguments and the tale headings are exact in both texts. In the Contents, the only difference is that a tale's number sits in its own styled `span.tn`, without the source's `·` after it. That is the v2 page's own setting, kept on purpose. |
| **The Original, mechanically** | A: in 31 of 31 leaves, every Book paragraph has its block, in order. B: all 1,300 block copies of the Book text match the Book. C: 1,277 unit items have English that is the Book paragraph exactly. The other cases were confirmed by hand: V.6's song is held by ring 23's pockets (a ring continuation), V.7's carving English follows its code block, and the Knowings' table rows are Seren's table. D: 1,061 folds match the unit's Orrowen; the rest are the faults fixed below. The fixed formulas are identical everywhere (table below). Halyna's two inks agree with the Book's in 155 of 155 paragraphs. Every pair-name in the romanisation carries its lintel in the ink. |
| **The Original, by reading** | 31 paragraphs from 20 leaves, all on the right Book paragraph (§4). |
| **No design notes on the story page** | Four faults were found in the Original and fixed: faults 4 to 7 in §3. The Book and Plain Words panes hold none. |
| **No scratch paths** | One was found and fixed: the `svg3/VI-2-<name>.svg` reference (fault 6). One stylesheet comment named the workflow (`wf12 panes`) and is gone. Neither copy of the page now holds `/private/`, `scratchpad`, `wf…`, `.gn2`, `.md` or `.py`. |
| **No custom of burning** | None in the English. Notes §1.8 lists seven mends, and all of them hold in the Book and Plain Words. The Orrowen was read, by gloss, wherever a custom once stood: IV.3 ×4, IV.5, V.1, V.2, VI.3 ×4, the Epilogue and IV.6's ring 4. In every case the burning is the warden's order, plain fear, want of wood or Harl's temper, and nothing is said over a fire. The four uses of *custom* on the page are IV.4's file notes in the Grain Notation, *(guests: the custom itself)* and *(trees that know the iron: the custom itself)*. They name the Guest's kneeling rite, not burning. |
| **Tale anchors unchanged from v2** | All 41 section and article ids of the v2 page (`contents`, `foreword`, `invocation`, `book-1` to `book-6`, `epilogue`, `knowings`, `t-I-1` to `t-VI-3`, `t-epilogue`, `t-knowings`, `t-last-note`) are on v3, **in the same order**. The ids v2 drops are only its 93 per-leaf radio inputs (`t-I-1--book` and the like), and nothing links to them. |

**The fixed formulas in the Original** (from the units, as the Tier 3 report §5 sets them):

| The Book's line | The Original | Times |
|---|---|---|
| *And the hearth said: We remember.* | *Eth re vysk et odh: Tumar.* | 33 |
| This I lay as it was laid for me. | *Cadhom o hosen re yal cadhat lom.* | 20 |
| This we lay as it was laid for us. | *Cadhan o hosen re yal cadhat lona.* | 2 |
| *And no one answered.* | *Eth re dhess nahos.* | 9 |
| **IN MEMORY OF OUR HOME…** (the Title) | *Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.* | 3 |
| *And the Captain put his hood back.* | *Eth re hadh et Crenn et biskhovv dem sestow.* | 2 |
| "We remember." | *Tumar.* | 1 |
| This is held in the grain. | the bark seal, `bark 0: HOLD`, on the whole round; not a ring | 8 |

---

## 3 · The faults, and how each was fixed at its source

All seven were in the Original pane. Every fix was made in `wf12/orig/build_panes.py` or in a unit, and then `panes.json` and `panes.css` were rebuilt and the page with them. Exactly 41 blocks of `panes.json` changed: the 18 below, plus II.2's 23 ring folds, where only a label changed (fault 7). No block moved, and no `src` changed.

| # | Fault | Where | The source | The fix |
|---|---|---|---|---|
| **1** | **The warden's ▒▒▒▒ was missing from Seren's ink.** The romanisation kept the blots, but the ink line lost them, because the leaf-hand's tokenizer drops anything that is not a letter. *"Re heth ▒▒▒▒ o sestyarl"* (▒▒▒▒ held his arm) was inked as *"re k̬eth o sestyarl"*. | 12 lines: IV.1 b1184; IV.3 b1304, 1308, 1318, 1322, 1326, 1332, 1336, 1348, 1358, 1364, 1378 | `build_panes.py`, `ink_line()` and `SEG_RE` | ▒+ is now a segment of its own, set as `<span class="ink-blot" role="img" aria-label="a name blotted out">▒▒▒▒</span>` in the house face (the leaf-hand has no sign for it), the same way the dash and the gap are set. A new `.ink-blot` rule went into the generated `panes.css`. The punctuation around the blot is right: IV.1 now reads *…stinAt, ▒▒▒▒. re k̬adh rhyna…*. A screenshot confirms it renders like the Book's own blots. |
| **2** | **Builder notation in a fold.** IV.2's two reading lines showed `[⟦legend_iv2_gap1⟧]` and `[⟦legend_iv2_gap2⟧]` as raw text. | IV.2 b1216, b1221 | `build_panes.py`, `rom_html()` | A `⟦id⟧` mark in a romanisation is now the Book's own drawing, set inline at text height (`span.glyph` around a native slot), as the Book pane sets it. The fold now reads *— Hos, eth — [drawn mark]*. |
| **3** | **Builder notation in a fold.** VI.3's tenth Throne showed *"Ew {LAST_THRONE_AT_HAVEN}."* | VI.3 b2588 | `build_panes.py`, `rom_html()` | The token is now romanised as the Book's one state (Glasspire, from S10's table of ten): *Ew* `<span class="tok" data-token="LAST_THRONE_AT_HAVEN" data-haven="Glasspire">`*Neivaere o, ul nyrulath Sirrvell*`</span>`. It sits in the same swappable span the ink line uses. |
| **4** | **A tool note in a literal reading.** It read: *(The validator prints "the small shore-folk as a people (Aethear)": grain_v2_full §21.9.6 finding 4.)* … *(`DEEP` is* eir*…; the validator prints "old".)* | V.7 b2297, the plate of what the carving was cut against | `units/S09.md` l.536–538 | The two notes were moved out of the numbered reading and into the **Reads** heading's parenthesis, so the unit keeps them. The page now reads *Rhenear, cut small. They strike, the first time, and far. They send (make go) the guns found.* The unit's line count is unchanged. |
| **5** | **A spec reference in a literal reading:** *(mystaeri_spec §5.1 adds the fold: …)* | VI.3 b2617, the green sliver's round | `units/S10.md` l.248–249 | The reading now ends *…bound.* The fold: *In ours, folded: those of the breath*, `[NAELEAR within HOME]`. The source note moved to the next bullet of the unit. The line count is unchanged. |
| **6** | **A scratch path and a false claim.** It read: *"The other nine hearts are drawn whole as well (svg3/VI-2-<name>.svg)."* The nine hearts are not on the page; they were rendered but never set. | VI.2 b2516, the whole round at the seal | `build_panes.py`, `render_seal()` | The sentence is cut. The note's true parts stay: the ten hearts, the shared bands, each Throne's entry drawn below, and the name in the bark. |
| **7** | **The toolchain on the page.** 23 printouts were labelled *"The validator's reading"*. | II.2, all 23 ring plates | `build_panes.py`, `gn_details()` | The label is now *File by file*, which is what the printout is: the round's literal reading, file by file. It sits under the prose *Literal reading*. |

**The checker now catches all of these.** `wf12/book/check_story.py` §9 checks the Original pane's text outside the Grain Notation for builder, tool or scratch matter: `{{`, `{TOKEN}`, `:::`, `⟦`, `<!--`, `svg3/`, `.svg`, `.gn2`, `.md`, `.py`, `wf\d`, `scratchpad`, `/private/`, `validator`, `_spec`, `grain_v2` and `§`. It also requires the warden's blots to agree three ways (The Book 12, the ink 12, the romanisation 12). Run on the page as it stood before this pass, it reports all of faults 1 to 7. That run gave 14 FAILs: 9 for the faults, and 5 more because the old page no longer matches the rebuilt `panes.json`. Run on the rebuilt page, it passes.

---

## 4 · Reading the Original against the English (31 paragraphs, 20 leaves)

Each paragraph's romanisation was glossed with `orr_analyze.py --gloss`, on a private copy with the merged lexicon. The gloss was read against the Book's paragraph at the same `data-k`. Every one is the right paragraph, and its meaning is the Book's. The tales where a custom was mended (marked †) were read for it on purpose.

| Leaf · line | Kind | The Book (short) | The Orrowen (short) and its gloss | Verdict |
|---|---|---|---|---|
| I.1 · b193 | stone | By the lintel of the western stair I swear it… A teller am I, and no singer | *Rytom um hosk et bystir rerdsennen … Ston. El nydherd en, nel vellerd*: "I swear upon the lintel of the western stair… a counter am I, not a singer" | ✓ the canon's oath |
| I.2 · b331 | stone | Their two chisels took the last of the light. | *Re rike et pa wresk et baegyth dasken*: "the two chisels caught (3DU) the last light" | ✓ |
| I.4 · b538 | stone | Bloom the masons call the pale crust… | *Sinth, vollant et tolmardath et sast stacorn…*: "Bloom, the masons name the pale skin…" | ✓ |
| II.3 · b868 | marked, Rhyna | We hold that God made each pair one… the Aetherbond | *Rhyna. Kethen: re lodh Mardh gor yanna ul hos…*: "we two hold: God mortared every pair into one…" | ✓ the dual throughout |
| III.1 · b974 † | stone | Harl… the grey I will burn, and the sea too | *…es vorrom et myst, eth et wadh sost, amm grik o vorr. Ston.*: "I will burn the grey, and the sea itself, if it catch fire" | ✓ his temper, no custom |
| III.2 · b1056 † | stone | I told him to burn it. | *Re vyskym lo: Vorr o.* | ✓ |
| IV.1 · b1184 | stone | At its foot a name is cut out: ▒▒▒▒. | *Lo o visk doss voll stinet: ▒▒▒▒.* | ✓ (fault 1, fixed) |
| IV.3 · b1348 † | Halyna, b | ▒▒▒▒ held his arm, and looked not at the boat. | *Re heth ▒▒▒▒ o sestyarl, eth nath re vesk o et sulter.* | ✓ (fault 1, fixed) |
| IV.3 · b1350 † | Halyna, a | "Burn it," said he… Leave naught to show. | *Vorra o, re vysk o, eth hasta o dem neld … Luska nayalat sa hebb veskyl.* | ✓ the warden's own order |
| IV.3 · b1354 † | Halyna, b | Old Tobe… washed the poles. | *Re orr Tobe hemm ul et wadh dem o yerdeth, eth re ridh o et gannath.* | ✓ Tobe says nothing |
| IV.3 · b1356 † | Halyna, a | Into the wind it went… into the grey, burning. | *Re orr o ul lern et helvhoss … ul et myst, ul vorr.* | ✓ |
| IV.5 · b1538 † | stone | It is the boat that cometh for you when ye die. | *El et sulter o sa rarr demos amm sennys.* | ✓ a sailor's tale, not a belief |
| V.1 · b1675 † | stone | …made their fires of it… for wood was dear… "Burn it," said Harl | *…re hadhant vorrath hyo … hy vodh ew merr et mesk um et sorth. Vorra o, re vysk Harl…* | ✓ fear, want of wood, temper |
| V.2 · b1746 † | stone | The soldiers' fires had the rest, and the tide. | *Re yal et ullen lo vorrath et hesperdeth, eth lo et hyll.* | ✓ |
| V.5 · b2006 | stone | He died at the parapet… the Captain cut the second strip. | *Re senn o lo et hosk hald … re dhresk et Crenn et saedel pawast.* | ✓ |
| VI.1 · b2434 † | stone | I did not burn it. | *Nath re vorrom o.* | ✓ |
| VI.3 · b2643 † | stone | *Burn it*, he had said of every plank… set down at Tarnard's feet | *Gor hrynir et gorrol, re vysk o: Vorra o. Re hadh o et crynir sy lo visketh Dharnard…* | ✓ |
| VI.3 · b2695 † | stone | Into the wind it went… and into the grey. | *Re orr o ul lern et helvhoss, eth ul lern et kess, eth ul et myst.* | ✓ no last word, as v3 has it |
| VI.3 · b2697 † | stone | Six winters had they turned their faces… when a hull burned. | *Vran grem re hylent so lerneth hy et wadh, amm re vorr sceth.* | ✓ |
| VI.3 · b2699 † | stone | They did not look away. | *Nath re veskent dem neld.* | ✓ |
| Epilogue · b2767 † | stone | The old ship-masters stood at the head of the shingle, and came no further. | *Re yalant et higileth hemm lo wisk et dhysal, eth nath re rarrant mest virr.* | ✓ no fire beat |
| Last Note · b2882 | stone | …the sounds close and the symbols wrong. | *…et hunnatath virr, eth et rellorath navenn.* | ✓ |
| Foreword · b130 | Halyna, b | "is half a tale." | *saed trenn.* | ✓ |
| II.2 · b777 | reading, a | *— Old. Ere stone. Ere any stone was cut.* | *— Hemm. Tevar hy dholm. Tevar hy et tolm hosast stannat.* | ✓ echoes ring 1 (a1) |
| II.2 · b778 | reading, b | *— Grey among the trunks. Not fog. There is no word —* | *— Myst ul molt et gannath. Nel myst. Nath noss brod —* | ✓ |
| IV.2 · b1256 | ring 13 | The young of the long-lived turned their faces from the open sky… | `9: NEW+US×3  9: US:crown×3+TURN  11: OPEN`…; literal: "turn aside: many heads; weep; not hold" | ✓ |
| IV.4 · b1464 | ring 13 | The blade that was to go a little way went deep… The host cried out | `1: >WOUND½ … 4: DEEP+WOUND … 4: CRY  0: STONEFOLK×3+GO`; "a deep wound —because→ an arm going" | ✓ |
| IV.6 · b1613 † | ring 4 | Into us they cast him, as men cast a torn net. | literal: "as a seeming one sends a seeming net, and a seeming breaking is on it" | ✓ no intent to burn |
| V.3 · b1855 | ring 11 | We threw one fire at the stone… the grain hath naught. | literal: "We throw fire, once, at your stone… what, the wood does not hold [ ]" | ✓ |
| V.6 · b2152 | ring 13 | Some wait, and burn, and wait again… | literal: "Some wait; then burn; then wait again. Some send all, once." | ✓ |
| VI.2 · b2546 | ring 12, Vaelress | We are **Vaelress**, the grain that rots… | literal: "wood that alone does not rot… You put our kin beneath, into the fen… then our rotting. (In the bark: Vaelress…)" | ✓ |

---

## 5 · Inbound links in Docs

**No tale or section link breaks.** All 1,491 anchored links into `Rivenkeep_Legends.html` from Docs (the four pages named, plus `Rivenkeep_GDD_Removed.html` and the `Archive/` pages) resolve on v3. So do all 1,883 from the new Notes (`wf12/out/Rivenkeep_Legends_Notes.html`).

| Page | Links into the Legends | On v3 |
|---|---|---|
| `Rivenkeep_Tongues.html` | 5, to the page only | ✓ |
| `Rivenkeep_Admiral.html` | 31 anchored (11 distinct: t-I-1, t-I-3, t-IV-2, t-V-1, t-V-2, t-V-3, t-V-5, t-V-6, t-V-7, t-VI-2, t-VI-3) and 1 to the page | ✓ all |
| `Rivenkeep_GDD.html` | 2, to the page only | ✓ |
| `Rivenkeep_Legends_Notes.html` (v1.0.0) | 1,404 anchored (33 distinct: every tale, foreword, invocation, knowings, book-3, book-5, book-6) and 5 to the page | ✓ all |

**Outside this page's scope, but it will break when Notes v1.1.0 replaces v1.0.0 in Docs.** v1.1.0 adds a new §1 and renumbers the old sections: the old §1.5 is now §2.4, and the old §4 is now §5. Docs links into the *Notes* will then point to the wrong section, or to none:

| Link | In | v1.0.0 section | In v1.1.0 |
|---|---|---|---|
| `Notes#s4-8` | Tongues | 4.8 The reader: three tabs | **gone** (now `s5-8`) |
| `Notes#s4-9` | GDD | 4.9 The Whispers and the hearth-lines | **gone** (now `s5-9`) |
| `Notes#s4-10` | GDD | 4.10 Battle messages | **gone** (now `s5-10`) |
| `Notes#s4-1`, `#s4-3`, `#s4-5`, `#s4-6` | Tongues (all four), Admiral (s4-3, s4-5) | 4.1 standing laws, 4.3 tales by campaign, 4.5 the Knowing, 4.6 the native hands | resolve, but to **different** sections (now `s5-1`, `s5-3`, `s5-5`, `s5-6`) |
| `Notes#s1-5` | Admiral | 1.5 What moved out of the Book | resolves, but to 1.5 *The wood-leaf form* (now `s2-4`) |
| `Notes#names`, `Notes#game` | Admiral, GDD | | ✓ unchanged |

---

## 6 · Kept as they are (judgement calls, for Jack)

- **The carvings' design ids in Original captions.** Captions such as *E1-02, as the wood cut it*, *The bearer's plank, E4-01* and *Grain Notation · E5-02* carry these ids. They are also the rounds' names inside the Grain Notation (`round E1-02 {…}`). The Original page Jack saw and liked, `Archive/Rivenkeep_Legends_Original_v1.0.html`, set them the same way, so they stay. If the story page should carry no game ids at all, they would go in `build_panes.py`'s captions and in the rounds' names.
- **The whole-round notes at each seal.** One example: *"…it is not a ring. 23 rings in three movements (7 / 6 / 10): 142 marks, 102 runners, 2 pockets. Packed by years and cells, the round is 37 years, about 1,302 units in radius."* The v1.0 Original set these word for word, so they stay.
- **"openning".** It appears 5 times in IV.2's *File by file* printouts (b1246, 1248, 1250, 1256, 1282). It is the grain validator's own generated English (a gerund rule), pasted into `units/W02.md` as the tool printed it. The fix belongs in the shared `grain_validate.py`, not in the unit, so the printout and the tool stay in step.
- **The Contents' tale numbers.** Each sits in `span.tn` without its `·`. This is v2's setting, and the words are otherwise exact.

---

## 7 · Files

**Changed (sources).** Backups of every changed file and of both pages as they stood are in `wf12/tmp/FID/backup/`.

- `wf12/orig/build_panes.py`: the blot segment (`SEG_RE`, `BLOT`, `ink_line`); `rom_html()` gains the inline drawn mark and the romanised token (`token_rom`); the label *File by file*; the VI.2 sentence cut; the stylesheet comment without `wf12`; the new `.ink-blot` rule.
- `wf12/units/S09.md` and `wf12/units/S10.md`: each Reads line now holds the reading alone, and the tool or source notes moved within the same unit. The line counts are unchanged. `validate_units.py S09 S10` reports 0, and `grain_validate.py --md` gives 0 errors.
- `wf12/book/check_story.py`: the new Original checks (§3).

**Rebuilt:**

- `wf12/orig/panes.json`, `panes.css`, `panes_build.log`, `panes_stats.json` and `panes_check.json`. `check_panes.py` gives FAILS: 0.
- `wf12/out/Rivenkeep_Legends.html` (12,358,282 bytes) and `wf12/out/web/The_Legends_of_Rivenkeep.html` (12,356,121 bytes). `check_story.py` gives ALL CHECKS PASS.

**This pass's tools:** `wf12/tmp/FID/fid_text.py`, `fid_frame.py`, `fid_orig.py` and `spot.py`, with screenshots of the fixed blocks in `wf12/tmp/FID/shots/`. To re-run them all:

```
cd wf12/orig && python3 build_panes.py && python3 check_panes.py
cd ../book && python3 build_story_html.py --doc-version v3.0.0 && python3 check_story.py
cd ../tmp/FID && python3 fid_text.py && python3 fid_frame.py && python3 fid_orig.py
```
