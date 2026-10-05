# THE LEGENDS v3 · THE ORIGINAL TAB'S PANES, AS DATA FOR THE PAGE BUILDER

*wf12 workflow document, 2026-10-03. Not a Book leaf and not a repo doc; nothing here goes into `Docs/`. Jack wants the original back in every tale: "This should be the full document with all the tree and stone writings." This is everything the story page's **Original** tab needs, built from the merged units (`wf12/units/*.md`) against THE LEGENDS OF RIVENKEEP, Book v3.0.0 (`wf11/book_v3.md`), with the markup and classes of the old Original page Jack saw and liked (`wf8/out/Rivenkeep_Legends_Original.html`, built by `build_original.py`).*

## THE SHORT VERSION

| | |
|---|---|
| **`panes.json`** | `{tale_anchor: [{para_index, html, kind, ...}]}`: **41 leaves, 1,367 blocks**, one block per Book paragraph, in the Book's order |
| **Coverage** | **every** paragraph of the Book has its block (title page and Contents included). From OF THIS BOOK on, **1,300 of 1,300** text paragraphs are set from exactly the unit item the merge paired them with (`merge/coverage2.json`); the 29 lines of the `::: native` / `::: note` fences are 17 drawing blocks; **0 blocks without Orrowen** |
| **The hands** | **1,216** paragraphs in Seren's ink, the leaf-hand Garl Flenn (`ink.py`), each with a quiet no-script `<details>` giving its romanisation. **155** in Halyna's two inks (77 split halves, 14 of II.3's marked tellers, 64 reading lines), **155 of 155** as the Book's two-ink rule sets them. One analyzer report: the Last Carver's *et dumol*, the error the canon keeps |
| **The grain** | the 8 wood leaves' whole rounds at their seals; **187 ring plates**, one to a story paragraph (A26's two shared rings as 2 continuation blocks, the two cited rounds as their own blocks: 191 of 191 story paragraphs); every carving of V.1, V.2, V.7, VI.3, the Epilogue's Stone and the Book of Knowings (47) as its round |
| **Drawings rendered** | `make_grain3.py`, cached: **391 jobs** (84 whole rounds, 305 ring plates, 2 chips, the bare Stone): **390 drawn** (326 cut in this run, 64 from the cache), **1 failure** that does not matter (below). `svg3/` holds those 390 and 3 recovered from the wf8 build; **266 distinct drawings** are set in the panes (11.4 MB as rendered) |
| **Font** | `GarlFlenn.woff2` embedded once, base64, in **`panes.css`** (30.8 KB with the ink and grain rules) |
| **Checks** | `check_panes.py`: **0 failures** (the Book cut, the merge's pairing, every slot resolves to this run's render, every block's HTML balances, the inks); a test page of the whole pane (`shots/panes_preview_all.html`, 11.1 MB, 274 drawings) and headless-Chrome shots of the foreword, II.2, V.2, V.6, VI.2, VI.3, the Epilogue and the Knowings, at desk and phone width |

---

## 1 · THE FILES

All in `wf12/orig/`:

- **`panes.json`**: the data. **`panes.css`**: the Original's styles (the old page's `EXTRA_CSS`, its selectors moved from `.tale` / `.prose` to `.pane`, v3's new classes, the grain renderer's shared rules once, and the font).
- **`panes_lib.py`**: for the page builder. `PL.load()`; `F = PL.Filler()` once per page; `F.fill(block['html'])` fills every drawing slot; `F.defs()` once after `<body>` (the shared `<symbol>`s); `PL.css()`. `Filler(mode='img')` sets the grain as `<img loading="lazy" src="svg3/KEY.svg">` instead (each svg3 file carries its own style, so it draws alone).
- **`build_panes.py`**: builds `panes.json` and `panes.css` (+ `panes_build.log`, `panes_stats.json`). **`check_panes.py`**: the checks (`panes_check.json`). **`preview_panes.py`**: the test page (`shots/`), with `--from= --to=` for a slice of one leaf. **`shoot.sh`**: a headless shot of a slice.
- **`svg3/`**: the drawings. **`make_grain3.py`**: the renderer's driver (one change, §3). **`make_grain3.log`** / **`make_grain3.run3.log`**: this run.

## 2 · THE CONTRACT (`panes.json`)

**The anchors** are the story builder's (`wf10/book/build_story_html.py`'s split, which keeps v1.3's anchors): `front` (the title page), `contents`, `foreword`, `invocation`, `book-1` … `book-6`, `epilogue`, `knowings` (each Book's heading and Argument, outside its tales), `t-I-1` … `t-VI-3`, `t-epilogue`, `t-knowings`, `t-last-note`. The builder puts the tabs on the leaves; the Books' heads, the title page and the Contents are offered for its use (it sets them outside the tabs today).

| Anchor | Blocks | From | Book lines | Most |
|---|---|---|---|---|
| `front` | 3 | S11 | L1–5 | front-title 1, front-sub 1, front-line 1 |
| `contents` | 47 | S11 | L9–81 | list-item 28, contents-line 10, contents-arg 8, book-head 1 |
| `foreword` | 31 | S01 | L85–152 | para 25, halyna 2, book-head 1, dateline 1 |
| `invocation` | 10 | S01 | L156–177 | para 5, book-head 1, headnote 1, native 1 |
| `book-1` | 2 | S11 | L181–183 | book-head 1, book-arg 1 |
| `t-I-1` | 43 | S01 | L185–285 | para 31, native 3, frame 2, title 1 |
| `t-I-2` | 46 | S02 | L289–393 | para 33, halyna 4, frame 2, verse 2 |
| `t-I-3` | 40 | S02 | L395–475 | para 33 |
| `t-I-4` | 57 | S03 | L477–609 | para 42, halyna 6, native 2 |
| `t-I-5` | 43 | S03 | L611–695 | para 37 |
| `book-2` | 2 | S11 | L699–701 | |
| `t-II-1` | 33 | S04 | L703–767 | para 28 |
| `t-II-2` | 38 | W01 | L769–844 | ring 23, reading 9 |
| `t-II-3` | 32 | S04 | L846–916 | marked 14, inscr 7, frame 2, halyna 2 |
| `book-3` | 2 | S11 | L920–922 | |
| `t-III-1` | 41 | S05 | L924–1004 | para 22, part 10 |
| `t-III-2` | 52 | S05 | L1006–1108 | para 32, part 10 |
| `book-4` | 2 | S11 | L1112–1114 | |
| `t-IV-1` | 43 | S06 | L1116–1204 | para 32 |
| `t-IV-2` | 39 | W02 | L1206–1284 | ring 24 (+1 cont), reading 8 |
| `t-IV-3` | 61 | S06 | L1286–1416 | halyna 43, para 8 |
| `t-IV-4` | 39 | W03 | L1418–1492 | ring 24, cited 1, reading 9 |
| `t-IV-5` | 43 | S07 | L1494–1584 | para 35, verse 2 |
| `t-IV-6` | 36 | W04 | L1586–1655 | ring 23, reading 8 |
| `book-5` | 2 | S11 | L1659–1661 | |
| `t-V-1` | 32 | S07 | L1663–1732 | para 23, halyna 2 |
| `t-V-2` | 39 | S08 | L1734–1812 | para 26, carving 7 |
| `t-V-3` | 33 | W05 | L1814–1877 | ring 20, reading 8 |
| `t-V-4` | 38 | W06 | L1879–1952 | ring 22, cited 1, reading 8 |
| `t-V-5` | 75 | S08 | L1954–2106 | para 61, part 6 |
| `t-V-6` | 37 | W07 | L2108–2186 | ring 24 (+1 cont), reading 7 |
| `t-V-7` | 75 | S09 | L2188–2358 | para 50, halyna 8, carving 4, part 3 |
| `book-6` | 2 | S11 | L2362–2364 | |
| `t-VI-1` | 67 | S09 | L2366–2498 | para 29, answer 11, part 10, who-line 10 |
| `t-VI-2` | 39 | W08 | L2500–2576 | ring 27, reading 7 |
| `t-VI-3` | 60 | S10 | L2578–2720 | para 44, halyna 6 |
| `epilogue` | 2 | S11 | L2724–2726 | |
| `t-epilogue` | 44 | S10 | L2728–2827 | para 33, native 2 |
| `knowings` | 2 | S11 | L2831–2833 | |
| `t-knowings` | 22 | S11 | L2835–2868 | table-row 10, para 7 |
| `t-last-note` | 13 | S11 | L2870–2896 | para 7, native 1 |

**A block** always has `para_index` (0 … n-1 in the leaf), `kind`, `html`, `line` and `end_line` (its lines in `book_v3.md`), `book` (the Book's text of the paragraph, character for character; for a drawing, its whole `:::` fence) and, when it comes from a unit, `src` (`UNIT:line`). The builder can match by `para_index` over the same cut, or by `line`, which is the safer: **the cut** is the merge's (`merge/coverage.py`'s `book_paras`): a heading, a paragraph, each Book blockquote's paragraph, a verse (one block, its lines inside), each reading line, the seal, each story paragraph, each row of the Knowings' table; and one `::: native` or `::: note` fence is one block (caption and fold together, as the Book draws one figure). Optional fields: `voice` (`a` | `b`, Halyna's two inks), `role` (`wood`, `wood: line 3`, `mixed`), `wrap` + `wrap_id` (consecutive blocks with one `wrap_id` sit in one Book blockquote: `invocation` → `blockquote.invocation`, `facing` → `blockquote.grain`, `quote` → `blockquote.grain` (II.1's founders' leaf), `knowings` → `div.knowings`), `ring` and `svg3` (a plate's ring and key), `nid` and `owed` (a native drawing, and whether it is still owed), `token_forms` (VI.3), `markers` (the builder's markers just above the paragraph: `RING` is the grain-rule the Original also draws there, `<div class="ring" aria-hidden="true"></div>`; `HALYNA`, `READING`, `W…`, `MIXED`, `TOKEN`, `RIPENS`, `PROLOGUE EXCERPT`) and `markers_after` (I.1's `FACING LEAF`).

**The kinds**: `title` (a leaf's title in ink, `p.ink.ink-name`), `book-head`, `book-arg`, `front-title`, `front-sub`, `front-line`, `contents-line`, `contents-arg`, `list-item`, `dateline` (`ink-dateline`; the first fully italic line of nine words or fewer under a title), `headnote` (`ink-teller`), `para`, `halyna` (a split half, `data-voice`), `marked` (II.3's tellers), `frame`, `added` (V.5's and VI.1's *Added in Seren's hand*), `inscr`, `who-line`, `part` (`h4.part.ink`), `verse`, `laid`, `answer` / `silent` / `hood` (the closes, with the coping), `title-line` (the Title in ink, `ink-title`), `reading`, `seal`, `ring`, `ring-cont`, `cited`, `carving`, `native`, `note`, `table-head`, `table-row`.

**Drawings are slots**, never inlined in the JSON: `<span class="svg-slot" data-svg3="KEY" data-title="…"></span>` (the grain, `svg3/KEY.svg`) or `data-native="ID"` (the Book's own drawing, `wf6/svg/ID.svg`, the one the Book tab draws). `panes_lib` fills them so that every inclusion gets unique ids on the page (one Book drawing is set in both the Book and the Original tabs).

## 3 · WHAT IS SET, LEAF BY LEAF

**Stone leaves** (S01–S11): every paragraph in Seren's ink, in its underlying form (each mutation as its base letter with its bite, the harmonic letters, the sealing lintel over every pair-name, the coping after the laying and the closes). The ink has no sign for the em-dash, the gap, the middle dot or a builder token, so the line breaks there: the dash and the dot stand in the house face (`span.ink-p`), the gap as `[ ]` (`span.ink-gap`, never mended), a token as `span.tok`. The romanisation fold shows the pair-names under their lintel (`span.pair`). The wood's role inside a stone leaf is the wood ink on the words the Book marks (`<!-- W -->`: the whole line; *the italic carvings only* / *the italic line only*: the italic run; VI.3's song: line 3); the Epilogue's Last Carver's letters are `ink-mixed`.

- **The foreword**: the Stonwryt drawn (the Book's Hal), its fold the Hal romanised and the line as {{Halyna}} say it in Seren's ink; then the Stonwryt cut dry, as the old page set it.
- **The Invocation and I.1**: the coal Title drawn (the Book's), its fold the Title romanised; the bold Title line in Seren's ink, then the Title cut dry. **I.4**'s Title under the new capstone stands in ink only: S03 says it is cut in the Captain's own coal letters, not dry.
- **I.1's facing leaf**: its frame line in ink; the Stone's own rings, bare (`STONE_bare`, the old page's choice for this leaf); Seren's untold line drawn in the course-hand (the Book's drawing) with her line in her ink under it.
- **V.1's facing leaf**: the Wave as a chip of the grain (`S07_V1-face`) with Seren's caption in her ink, as the old page set it.
- **V.2**: each carving paragraph with its plank's round first (E1-01 to E1-07, BURN, from S08), the wood's words and the literal reading in the fold, then Seren's paragraph.
- **V.7**: the three carvings as their rounds (E4-01, E5-02, V7-III), the leaf's excerpt and reading in the fold; Part II's *Under it was cut:* in ink, then E5-02's ring 4 as an inline plate.
- **VI.3**: the green sliver's round after *We remember our home too.*; *The Two Homes* in ink with line 3 in the wood's ink, then its chip; the tenth Throne's token **filled with the story builder's one state of the game, Glasspire** (*Neivaere o, ul nyrulath Sirrvell*), in `span.tok[data-token="LAST_THRONE_AT_HAVEN"][data-haven]`; `token_forms` gives all ten (S10 §3: the Book's text, the Orrowen, the ink) for the game to swap.
- **The Epilogue**: the Book's Stone drawn; its fold the grain on the Stone (`S10_STONE`), its canonical GN, the wood's words, and the Book's own line in Seren's ink, as the old page set it.
- **The Book of Knowings**: the column heads in ink; each of the ten roots one block (`div.k-root`: the root and its look in ink; each carving a card with its round, its head and Tide in ink, its GN and *the whole carved line* in the fold; the Throne in ink, and its Judgement as a card where it has one: 46 cards in all); *Burn* after the paragraph that names it, with Seren's head *Vorr.* in ink (47 rounds).

**Wood leaves** (W01–W08): the title, dateline and headnote in Seren's ink; the READING line by line in Halyna's two inks (IV.2's two drawn marks as the grain's own chips inline, `IV-2_frag1`, `IV-2_frag2`); **the seal is the whole round** (`figure.native.round.whole`, its fold the header, the file legend and the bark, and the note that the seal is the bark's, not a ring); every story paragraph its ring plate (`figure.native.plate`), its fold the unit's knowing-form ring and its literal reading (the unit's prose *Reads*, and the validator's printout where the unit gives one); the close in ink. II.2's and IV.2's `::: note` are Seren's in ink, with the Naelear chip (II.2) and the two marks (IV.2). V.4's facing leaf (*Here there is no tale of ours …*) is wrapped `facing`.

- **The cited rounds** (A27): IV.4's sentence is the gift's own round (`GIFT`), V.4's *Grow until the shore is silent.* the war's first carving (`V-4-grow`), each a block of its own (`kind: cited`).
- **A26, two paragraphs in one ring**: IV.2's ¶24–25 (ring 24, in two code blocks) and V.6's paragraph and *The Song of the Years* (ring 23): the plate stands at the first; the second is `kind: ring-cont`, a short line (*Ring 24 holds this paragraph too*) and its own GN fold (IV.2: ring 24's last knowings; V.6: ring 23's seven said-pockets).
- **VI.2, ten hearts**: the seal sets **Thaesaen's heart whole**, as the old page set the first heart; rings 1–11 and the two closing rings are Thaesaen's plates (the same ring in all ten but for the root and the haven); each Throne's entry is that Throne's own ring from **its own heart** (Eirlenth's and Neivaere's three each). The other nine hearts are rendered whole (`svg3/VI-2-<name>.svg`), and are not set (see §5, call 4).

## 4 · THE DRAWINGS (`svg3/`, `make_grain3.py`)

**This run** (`make_grain3.run3.log`): 391 jobs from the merged units: the 8 wood leaves' whole rounds (II-2, IV-2, IV-4, IV-6, V-3, V-4, V-6 and the ten VI-2 hearts) and every ring plate of each (305), the two cited rounds (GIFT, V-4-grow), every round of S07–S11 (V.1's Wave, V.2's eight planks, V.7's three, VI.3's sliver and chip, the Epilogue's Stone, the Knowings' 47, and the units' canonical duplicates), the Stone bare, E5-02's ring 4, and IV.2's two marks as chips. **326 cut, 64 found in the cache, 1 failed**; 89 drawings carry the renderer's usual notes (a runner drawn straight, little room), none an error. Every key a block sets was rendered or found fresh in this run (the checker refuses any other).

- **The one failure**: `S10_VI-1-twohomes`, the chip's **knowing-form** copy (S10 §1.3, `r1·1` lines), which the renderer does not read; its canonical copy in S10 §4, `S10_VI-1-twohomes_2`, is the same round and is drawn and set (its fold shows the knowing form, as the unit sets it).
- **AELTHAR**: v1.3's IV.4 cited the Aelthar's rite in ring 8; v3's does not (W03, note 13), and its source, `wf6/grain_texts/AELTHAR.json`, was lost to the temp cleaner. `make_grain3.py` now draws it only if that source returns (the one change to the file; nothing else it draws changes).
- **Recovered from the wf8 build, not re-rendered**: `CHISEL_title` and `CHISEL_stonwryt`, the dry cuts (their renderer, `wf7/render_chisel.py`, was lost to the temp cleaner; the canon lines they cut are unchanged in v3, so the wf8 page's drawings are taken out of it whole, self-contained), and `NAELEAR_chip` (`wf8/grain3/svg/grain3_NAELEAR_chip.svg`, the untold name's sign, unchanged).
- **Set aside**: the 106 drawings `svg3/` held from the wf8 copy (v1.3's III-2 hearts, AELTHAR, the old keys, and the failed key's old file) moved to `svg3/_wf8_stale/`, not deleted, so `svg3/` holds exactly this run's 390 and the 3 recovered.
- **Rendered and not set**: 127: the nine other VI.2 hearts whole and their 117 plates that no entry uses, and S10's canonical duplicate of the sliver.
- **Weight**: the 266 drawings set are 11.4 MB as rendered; filled through `svgpool` (the renderer's style once in `panes.css`, every sign once as a shared `<symbol>`) they are 8.1 MB, and the whole Original pane as a test page is **11.1 MB**. With the Book and Plain Words tabs the story page will be about 12 MB inline. `Filler(mode='img')` keeps the Original pane near 0.9 MB of HTML, the grain loading lazily from `svg3/` published beside it (the native drawings stay inline: they take the page's classes).

## 5 · GAPS, AND CALLS FOR JACK OR THE BUILDER

1. **Eight native drawings are still owed** (no drawing in `wf6/svg`): the pair-marks `legend_stonwryt_aldwena` (I.4), `legend_stonwryt_halyna` (II.3, VI.3, the Epilogue), `legend_seal_wendhessa` (IV.3), `legend_stonwryt_enrella` (V.7), the capstone Title `legend_title_capstone` (I.4) and `legend_three_stones` (the Last Note). Truth or nothing (notes_v3 §5.6): each block stands as its caption alone (`figure.native.unset`, `owed: true`), the capstone Title with its romanised Title in the fold. When a drawing lands in `wf6/svg`, `build_panes.py` draws it on the next run.
2. **Native captions in English**: 11 drawing captions stand in the Book's English as the reader's furniture, as the old Original set them (the Hal, both coal Titles, the bare rings, Seren's note, Aldwena's mark, the capstone Title, Halyna's three marks, the Epilogue's Stone); 6 are in Seren's ink because their units give them (II.2's and IV.2's notes, Wendhessa's seal, the Wave, Enrella's mark, the three stones). This is the merge's open call (merge report §9, item 6): one rule for the Original either way.
3. **A26, the ring cap**: two `ring-cont` blocks stand for it; raising the cap would make them plates.
4. **VI.2's other nine whole hearts** are drawn and not set, as the old page set only the first; any can be set beside its Throne's entry with one slot each (about 0.3 MB each).
5. **Datelines**: the builder must read v3's dateline (notes_v3 §5.13); these panes call the first fully italic line of nine words or fewer under a title the dateline and the next italic paragraph the headnote (29 and 31). The Last Note's *Laid last of all the leaves.* is set as its headnote.
6. **The token**: VI.3's block carries the Glasspire state, the story builder's; the ten forms are in `token_forms`.
7. **Nothing in the panes translates**: every fold is a romanisation or Grain Notation, as the old page's were (the designers' folds; the game's Original tab shows the hands alone, notes_v3 §5.8). The English that stands is the drawings' captions (call 2) and the dry cuts' explanatory folds, the old page's.

## 6 · HOW IT WAS CHECKED

- `check_panes.py` (exit 0): the 41 anchors are the Book's leaves; each leaf's blocks are its paragraphs by line, in order, `para_index` 0 … n-1, each `book` the Book's text; **1,300 of 1,300** text paragraphs set from the merge's own item (`coverage2.json`, `src` = its unit and line); 0 blocks without Orrowen; every slot resolves to a drawing of this run (or the 3 recovered) and every native slot to `wf6/svg`; every block's HTML balances; **155 of 155** ink-marked paragraphs carry the Book's ink; no plate set twice; the eight wood leaves' rings, cited rounds, wholes and readings counted (`panes_check.json`).
- The ink: `ink.py` on every line, through the private analyzer on the merged lexicon: one report, the Last Carver's error, expected.
- Seen: `preview_panes.py` filled the whole pane (274 drawings, every slot filled) in the house shell (`Docs/Rivenkeep_Legends.html`'s style) with `panes.css`; headless Chrome shots of the foreword's opening (title, dateline, headnote, the Stonwryt and its dry cut), II.2 (the reading's two inks, the gap, the whole round, ring 1), V.2 (the planks before their paragraphs, the italic carvings in the leaf-hand), V.6 (ring 23 and its continuation), VI.2 (Thaesaen's ring 11 and the entries from their own hearts), VI.3 (the song and its chip), the Epilogue (the Stone, the Last Carver's letters) and the Knowings (the heads, the root rows, the cards), and II.2 at phone width (headless Chrome lays out at 500 px at the least: no block overflows it).
