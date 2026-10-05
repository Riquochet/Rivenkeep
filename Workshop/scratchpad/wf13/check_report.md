# v3.1.0 reader check: The Legends of Rivenkeep (wf13, 2026-10-04)

I checked the page as a reader sees it, in headless Chrome (/Applications/Google Chrome.app). I checked the Docs page `out/Rivenkeep_Legends.html` and the web copy `out/web/The_Legends_of_Rivenkeep.html`. The web copy was wrapped the way the host wraps it, in a minimal doctype/head/body page whose body is 14px system-ui on a light ground (`tmp/reader/web_wrapped.html`). The wf12 reader tools were copied to `wf13/tmp/reader/` and pointed at wf13. New scripts in the same folder are `il.mjs`, `plain.mjs`, `gaps.mjs`, `blot.mjs`, `fw_place.mjs`, `t_place2.mjs` and `zoomshot.mjs`. The static checks are `tmp/chk/gloss_static.py` and `tmp/chk/web_contract.py`.

**Result.** I found three problems, all in the interlinear romanisation, the Plain note and the web copy, and fixed each at its source. I rebuilt and checked everything again. `book/check_story.py` reports ALL CHECKS PASS and `orig/check_panes.py` reports FAILS 0.

## Problems found and fixed

1. **Marks between the words read as glued to the next word.** A dash, middle dot or gap bracket in a romanised line was bare text with only a space after it. That gave 3 px against the 9 px between words. In IV.4's reading it showed as `Tolm —nel.`, `No —brodath` and `Ol —lonn`.
   - **Fix** (in `orig/build_panes.py`, function `rom_p`, plus its CSS): each mark between words now goes in `span.m` with `margin-right:.36em`, the same space a word box leaves after it. This covers 180 marks.
   - **Measured after the fix:** mark-to-word gap is 9 px at both widths (minimum and maximum), the same as word-to-word.
2. **The warden's blotted name ran into the next word and had no gloss.** The 12 blots (`▒▒▒▒`) in IV.1 and IV.3 were bare, italic-slanted text in a fallback face. They touched the next word (`▒▒▒▒et`) and sat over an empty gloss slot that read as a missing gloss.
   - **Fix** (in `rom_p`): each blot gets its own word box `<i class="blot">`, upright as the ink sets it, glossed **(name blotted out)**. The gloss is set like the grammar glosses, `(past)` and `(future)`. The hidden word-by-word list says "a name blotted out" at that point. No name is given.
   - Constants: `BLOT_CH`, `BLOT_GLOSS`, `BLOT_SAID`.
3. **The glosses in wood leaves were smaller.** A wood leaf's `.wood{font-size-adjust:.405}` was inherited by the romanisation lines. That shrank the IBM Plex Mono glosses from 10.2 px to about 8 px in 96 of the 1,288 lines. Those lines were in the eight wood leaves (II.2, IV.2, IV.4, IV.6, V.3, V.4, V.6 and VI.2), including all of IV.4's reading.
   - **Fix** (in the `details.tr .tr-body p.il` rule built by `orig/build_panes.py`): added `font-size-adjust:none`, since these lines are set in the stone face everywhere.
   - **Measured after the fix:** all 1,288 lines and their glosses have `font-size-adjust:none`. Gloss size is 10.19 px everywhere.
4. **Web copy only: the note for new readers was narrower.** `aside.newreaders{max-width:34em}` took its em from the host's 14px body. On desktop the note stood 476 px wide against 544 px on the Docs page, and 106 px taller.
   - **Fix** (in `book/story.css`): `aside.newreaders` now has its own `font-size:1rem`.
   - **Measured after the fix:** at 1280 px the note spans 4 to 737 px in both copies. At 390 px nothing changed.

I also updated the two checkers so they know the new forms and guard them:

- `book/check_story.py` section 11 now checks:
  - the blot boxes and their gloss,
  - that no blot or mark is left bare,
  - the hidden list with the blot in its place,
  - the new CSS: `font-size-adjust:none`, `.il .m` and `.il i.blot`.
- `orig/check_panes.py` section 7 has the same checks.

Rebuilt files:

- `orig/panes.json`, `panes.css`, `panes_build.log`, `panes_stats.json` and `panes_check.json`, from `python3 build_panes.py`
- both pages, from `python3 build_story_html.py --doc-version "v3.1.0"`

Docs page: 13,896,188 bytes. Web copy: 13,892,692 bytes.

## Screenshots read, 1280 px and 390 px (`tmp/reader/shots/`)

**Original, with romanisation folds opened by clicking their summaries** (`o_*_{repo,web}_{1280,390}.png`; before-fix copies are in `shots/before/`):

- I.1: Seren's headnote fold (45 words) and the first story fold
- IV.3: two of Halyna's long voiced folds, one holding a blotted name
- IV.4: all 9 folds of the wood leaf's reading

What I saw after the fix:

- Each word sits over its English, left-aligned with it.
- Rows wrap cleanly. The longest gloss ("they two will answer", 124 px) never overruns a line.
- Dashes sit on the word baseline with a word's space on both sides.
- The blot reads `▒▒▒▒.` over "(name blotted out)".
- The VI.3 token's five words stay boxed inside their swap span (`z_tok_*`).

**Plain Words, switched with a real click on the sticky bar** (`p_{fw_note,I1,II3,IV4}_*_{repo,web}_{1280,390}.png`):

- The foreword's "A note for new readers" sits quietly between two hairlines, a little smaller and dimmer, then the foreword's dateline.
- I.1, II.3 and IV.4 open with their italic "when" line, then the headnote, then the story.
- Pair-names keep their lintel. Speaker labels (Rhyna., Halvard.) sit in the margin at 1280 px and above the paragraph at 390 px.
- IV.4's reading lines alternate voices, then "This is held in the grain."
- The text reads as plain modern English with lore terms explained as they come.

## Confirmations

**The one switch changes every leaf.** I tested both copies at both widths:

- The sticky bar's labels, clicked for real, give 41 of 41 switch units in the chosen text: 31 leaves and 10 frame units, in all three texts.
- A leaf's own label far down the page (VI.3) stays under the pointer: 495 to 495 px at 1280, 464 to 464 px at 390.
- The choice survives a reload.
- `#t-IV-4` lands on its tale.
- With scripting off, the CSS switch alone still changes all 41 units.

**The switch keeps the place.**

- Book, Plain, Book through shared landmarks (`t_place2.mjs`), with a landmark 4 px below the reading line and with one 30 px into the block, across 10 cases:
  - Foreword, I.1, II.2, II.3 (two cases), IV.3, IV.4's reading, V.4, the Epilogue and the Last Note.
  - Every case returns to exactly the starting offset, at both widths and in both copies.
  - The foreword case from the top of its pane lands on the top of the Plain pane, which is the note, since the note comes before the dateline.
- The sequences through all three texts (`place.mjs`: V.5, II.2, IV.3, Knowings) behave as v3.0.0 did.
- An earlier run seemed to lose 1,123 px at the foreword. That came from my test scrolling only once right after load: content-visibility re-sized the page above before the click. With the scroll settled, the foreword round trip is exact (`fw_place.mjs`).

**No horizontal scroll at 390 px with every fold open.** I opened every `<details>` and turned content-visibility off, in all three texts and both copies.

- `scrollWidth` is 390 for both the document and the body, and nothing pokes past the viewport.
- Across all 1,289 romanised lines:
  - no word box goes past its line or within 16 px of the screen edge,
  - no box overlaps its neighbour and no rows collide,
  - no gloss is clipped and every gloss sits under its word.

The same holds at 1280 px. Grain Notation `pre` blocks scroll inside their own box, by design; the page does not scroll.

**Every romanised word has its gloss.** Static check over both copies:

- 1,289 lines in 1,218 romanisation folds.
- 26,532 words, each with a non-empty gloss.
- 12 blotted names glossed.
- No letter outside a word box.
- Every hidden word-by-word list matches its line.
- The only line without a word is the last fragment of II.2's reading, `— [ ]`: a dash and a gap left open, with nothing to gloss.

**The web copy keeps the host's contract** (`web_contract.py` and check_story section 10):

- It opens with `<title>The Legends of Rivenkeep</title>`, then the Google Fonts `<link>`, then one `<style>`.
- No doctype, html, head or body tag.
- One `:root` rule holding 52 tokens, with `color-scheme:dark`.
- The body background comes from a token (`var(--bg)`).
- No literal colour in the CSS outside `:root`, and none in any of the 4,181 `style=""` attributes.
- Outside loads: Google Fonts only. One inline script. The leaf-hand font is inline base64.
- The sticky bars sit at `env(safe-area-inset-top, 0px)`.
- No links to other files.
- 13,892,692 bytes, which is 13.25 MiB, under 15.5 MB.

## Seen and left as they are (no change from v3.0.0)

- **SVG mask colours.** 1,295 `fill`/`stroke` values of `#fff`/`#000` sit in SVG attributes, every one inside a `<mask>`. They are mask luminance, not painted colour, and they are identical in the v3.0.0 web copy.
- **Plain to Original slips one paragraph at 390 px.** In IV.3 at 390 px, going Plain then Original moves one paragraph down (b1342 to b1344). Plain paragraphs carry only the shared landmarks, not Book line numbers. The v3.0.0 run shows the same slip, and the round trip returns to b1342.
- **Audit false positive.** The audit flags `{all}`, `{most}` and `{again}` in the Original. These are Grain Notation quantifiers, unchanged from v3.0.0.
- **Romanised words in the dry-cut folds.** The three dry-cut folds explain the chisel register in prose, and they are not romanisation folds. One quotes the Hal's mortar sentence, which is glossed word by word in the fold just above it. The other two name the mortar words *ul* and *ol* and give their English in the same sentence.
