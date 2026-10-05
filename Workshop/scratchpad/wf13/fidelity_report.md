# Fidelity check · Rivenkeep_Legends.html v3.1.0 (wf13)

**Verdict: PASS. Nothing to fix, so the page was not rebuilt.**

- **The Book:** identical to v3.0.0, word for word.
- **Plain Words:** identical to `plain_v31.md`, word for word and paragraph for paragraph.
- **The Original:** unchanged apart from the glosses.
- **The glosses:** every gloss on the page is the one in `gloss/*.json`.
- **The spot-read:** all 30 lines read true.
- **Tale anchors:** unchanged.

Three things changed that are not text. They are listed under "Noted, not changed" below, and none of them changes a word the reader sees.

| | File | md5 |
|---|---|---|
| v3.1.0 (checked) | `wf13/out/Rivenkeep_Legends.html` (13,890,288 B, built 01:16) | a5a5e574507091c4d213792b3da08f1d |
| v3.0.0 (reference) | `wf12/out/Rivenkeep_Legends.html` (12,358,939 B) | 1b98e2f74180106108dcd63e2962d3ba (= `Docs/Rivenkeep_Legends.html`) |
| web copy | `wf13/out/web/The_Legends_of_Rivenkeep.html` | its 123 panes are byte-identical to the page's |

I wrote the checks myself and did not reuse the builder's own checker. The scripts are in `wf13/fid/`: `pg.py`, `orig_cmp.py`, `gloss_cmp.py`, `gloss_sanity.py`, `plain_cmp.py`, `plain_forms.py`, `plain_style.py`, `spot.py` (with its output in `spot_out.txt`) and `sweep.py` (`sweep_out.txt`). I also ran the builder's own `book/check_story.py`, and it reported ALL CHECKS PASS (`fid/check_story_out.txt`).

---

## 1. The Book tab = v3.0.0, word for word: PASS

- **Method.** I split both pages into their 123 panes, in 41 switch units, and compared each of the 41 `p-book` panes as raw HTML. Then I compared the whole page as the Book tab shows it (the Plain and Original panes cut out), from the header to the colophon.
- **Visible text.** The 41 Book panes have the same visible text in both versions: 31,079 words, identical.
- **Bytes.** 11 Book panes are identical byte for byte. The other 30 differ only by an invisible attribute:
  - `data-m="dl1"` on the 29 datelines;
  - `data-m="hn1"` on the Last Note's headnote ("Laid last of all the leaves.").
  These are place-keeping landmarks. The reader's place is held through them when switching between the Book and the new Plain datelines.
- **The rest of the Book view is identical, byte for byte, once those attributes are removed:**
  - the title page, the Contents, the Book heads and the Arguments;
  - the header, the nav and every tale heading.
- **The `<head>`.** Identical apart from three changes:
  - the version string (`--doc-version:"v3.1.0"`);
  - the story.css comment;
  - the new CSS rules: `aside.newreaders`, `.tale p.teller:has(+ p.teller)` and the `.il` interlinear rules.
- **None of the new rules touches a Book element.** The Book panes have no consecutive headnotes, no `aside.newreaders` and no `.il` element.

## 2. The Plain tab = `plain_v31.md`, exactly: PASS

- **Word stream.** The page as Plain Words shows it, from the title `<h1>` to the last pane, against the source with its markup read off:
  - 44,614 words on each side, with **0 differences**;
  - this includes the Contents, the Book heads, the tale headings, the drawings' captions and their Translation folds.
- **No paragraph dropped or doubled.**
  - Every paragraph of four or more words (1,278 of them) occurs on the page exactly as many times as in the source.
  - No source paragraph starts in the middle of a page block, so no two paragraphs were merged.
  - Splits inside a source paragraph on the page are all by design:
    - 55 are the READING fragment lines (each one in its own `<p>`, all 55 checked);
    - 33 are table cells;
    - 10 are drawing captions followed by their folds.
- **The fixed lines (the closes).** They match leaf by leaf.
  - **In the panes:**
    - 74 in the Book panes and 74 in the Plain panes.
    - Every leaf has the same sequence of `seal` / `answer` / `answer silent` / `answer hood` / `laid`.
  - **How the 74 Plain closes are set:**
    - "We remember" ×33.
    - "And no one answered." ×9.
    - The two new Plain hood lines (IV.3, the Epilogue), each set as `answer hood`.
    - The two `laid` forms, ×20 and ×2.
    - "This is held in the grain." ×8.
  - **Other lines that mention a close.** 19 source lines mention a close but are prose. One example is the Knowings fold that begins "This is held in the grain. It is about…". These are correctly set as ordinary text.
- **The redactions (▒▒▒▒).**
  - There are 12 runs, each four blocks long, in the source and in the Plain panes alike.
  - They fall where the Book's do: 1 in IV.1 and 11 in IV.3.
  - Each run sits in the same place in the word stream as in the source.
- **The lintels.**
  - The source has 146 `{{Name}}`: Halyna 99, Idrenna 18, Aldwena 10, Orvenna 8, Wendhessa 7, Enrella 4.
  - The Plain view has 146 `span.pair`, in the **same sequence**.
  - No pair-name is written bare, either in the source or on the page.
- **Italic and bold.**
  - **Italic:** every word's italic matches the source (0 differences).
  - **Bold:** 160 bold words in the source are set by structure, not by `<strong>`, exactly as the Book sets them:
    - the speaker labels (`span.who`, "Rhyna." / "Halvard.");
    - the haven part-heads (`h4.part`);
    - the label of the note for new readers (`h3.nr-h`).
- **The note for new readers and the "when" lines.** `check_story.py` §12 confirms them:
  - there are 29 Plain datelines, one wherever the Book has a dateline;
  - each is the source's first italic paragraph and carries the shared `dl1` landmark;
  - the note for new readers comes before the foreword's dateline, with all 4 of its paragraphs.
- **Provenance (not a page issue).** 63 of the 71 strings in the `_edit/e01–e05` fix pass appear verbatim in `plain_v31.md`. The other 8 were refined later, and their content is present:
  - 6 wood-leaf headnotes say "the two of them" where the edit said "{{Halyna}}, the pair who lead our builders", which avoids repeating the gloss on every wood leaf;
  - one sets "We remember" in quotation marks;
  - one drops "The vow is cut in the Hal, the old writing of the first builders." The drawing's caption directly above it already says this.

  The page matches the source as it stands.

## 3. The Original: text unchanged apart from the glosses: PASS

- **Method.** I turned every interlinear line on the v3.1.0 page back into v3.0.0's form. Each `<p class="il">` became a plain `<p><em>…</em></p>`, with:
  - the `<i>` word boxes removed;
  - the `<small>` glosses removed;
  - the hidden "Word by word" list removed.

  I then compared all 41 `p-orig` panes with v3.0.0 as raw HTML.
- **Result.** 40 panes are identical once the `dl1`/`hn1` landmarks are set aside. The 41st differs by one character of markup (see N2 below), and its visible text is identical.
- **What is unchanged:**
  - Seren's ink, Halyna's two inks and the grain;
  - the rings, the drawings and the Translation folds;
  - all 1,218 fold summaries ("Romanisation …").
- **Fold lines.** There are 1,289 fold lines in both versions, and all 1,289 are now `p.il`:
  - 1,288 are set word over word;
  - 1 holds only a gap ("— [ ]") and has no word to gloss.

## 4. Every gloss on the page = `gloss/*.json`: PASS

- **The JSON.** The 20 files hold 1,196 records for 1,133 distinct lines. No line is given two different glosses.
- **What I read off the page.** For all 1,288 glossed lines (26,532 word boxes), I took:
  - the line as it reads;
  - each box's word (the letters, with the punctuation at either end set aside);
  - each box's `<small>` gloss;
  - the hidden screen-reader list.
- **Results:**
  - Every line has its JSON record.
  - **Every box is the JSON's word and English, in order.** The two lines with a drawn gap mark (IV.2) key as `— Hos, eth — []` and `— eth nath re []`, and both match.
  - Every hidden "Word by word: …" list equals the JSON's English, in order.
  - No letter of any line sits outside a word box.
  - Every JSON line appears on the page.
  - The 2,368 distinct glosses carry no raw analyzer tag (PST, REL, S·, -1SG, ?, …).
  - The conventions are consistent:
    - the past and future particles are glossed "(past)" and "(future)";
    - the verb after the future particle is glossed "will …" (91 of 91);
    - pair-names are glossed "Halyna (the two)" and the like.

## 5. Spot-read: 30 lines against the analyzer: PASS (30 of 30 true)

I took 2 lines from each stone unit (S01–S11) and 1 from each wood unit (W01–W08), drawn at random (seed 20261004) from lines of 5–28 words, 341 words in all. For each word I read three things side by side:

- the page's gloss;
- what `orr_analyze.py --gloss` gives (its gloss, its set phrases and its parse);
- the lexicon row it parsed to.

The full side-by-side table is in `fid/spot_out.txt`.

| # | Unit · leaf | Line (start) | Words |
|---|---|---|---|
| 1 | S01 · foreword | Re lymmym pa yalat dem susk et brunn… | 20 |
| 2 | S01 · foreword | Re rarr nadhumol um ol nedheth… | 21 |
| 3 | S02 · I.2 verse | ketha et hald amm mellorant wemmeth myst, | 7 |
| 4 | S02 · I.3 dateline | Et grem hosast, ul o wress pawast. | 7 |
| 5 | S03 · I.4 | Re yal nindeth nasastat lom hyo. | 6 |
| 6 | S03 · I.4 | Re harm et lunt o: Ketherd… | 16 |
| 7 | S04 · II.1 | Ul et grem sa re nydh nahos… | 19 |
| 8 | S04 · II.3 frame | Olen re hadha sona et hosk umo… | 13 |
| 9 | S05 · III.1 part | Lurrvard, et kethow ul vimm et crisur lurr. | 8 |
| 10 | S05 · III.2 | Doss maver vothol reller um hos. | 6 |
| 11 | S06 · IV.1 | Re stinent o, eth re dhev o… | 17 |
| 12 | S06 · IV.3 | Re visk ▒▒▒▒ o lo sest. | 5 |
| 13 | S07 · V.1 caption | Fodhrellor, hosen re ryt Seren o. | 6 |
| 14 | S07 · IV.5 | Nath re vyskym lo: Hess. | 5 |
| 15 | S08 · V.2 | Re wrodh nahos, eth lo dhrenn fedh sell… | 26 |
| 16 | S08 · V.2 | Orr dem drunn. Ul vodh tresk sast… | 24 |
| 17 | S09 · V.7 | Um wirnenn Halvard re yal et lodh ul rhynyl. | 9 |
| 18 | S09 · V.7 | Vardh, re lodhith pana ul hos… | 12 |
| 19 | S10 · VI.3 | Re heth et mesk o. | 5 |
| 20 | S10 · VI.3 | Dem ull doss orrol lo hos lunt hosel… | 13 |
| 21 | S11 · Contents | Hylleth sa re nydh et Hald · Kael Nydherd… | 14 |
| 22 | S11 · Contents | Hebbet sa re yal kethet hos clem… | 14 |
| 23 | W01 · II.2 reading | — Myst ul molt et gannath. Nel myst… | 10 |
| 24 | W02 · IV.2 reading | — Rellorath lilv, um et galat nawrodh — | 6 |
| 25 | W03 · IV.4 reading | — Garlath, dhaedh, fedh sell. Flenneth… | 14 |
| 26 | W04 · IV.6 reading | — Gannath. Dem neld, dem et lunn, hy — | 7 |
| 27 | W05 · V.3 dateline | Ul nunn et grem sullast. | 5 |
| 28 | W06 · V.4 reading | — Gendeth hosen crisur, feth ul vimm… | 9 |
| 29 | W07 · V.6 reading | — Meskrivullath ul vimm gor yalat, lodhant… | 11 |
| 30 | W08 · VI.2 reading | — Meskrivullath, ul morrol. Tolm, ul dessyl. | 6 |

**Every word reads true to the lexicon.** In several places the page is right where the analyzer's first choice is wrong:

- **The dual ending.** The ending -a after `sona` ("they two") is the third-person dual. The analyzer's first choice reads it as an imperative plural. The page's "they two laid" (*hadha sona*) and "they two breathed" (*hossa sona*) are correct.
- **"Doss maver … um hos".** The page follows the idiom "need is upon someone" (= must), which the analyzer lists among its set phrases. The analyzer's first sense for *maver* is "wish".
- ***dhev*** is "grew" (the lexicon gives "grow, sprout"). The analyzer's first sense is "child".
- ***lo*** at a clause end is the third-person singular "to-him", by orrowen_v2 §3.6 (*lo* / *loy*).
- ***ryt*** is "drew" and ***Hal*** is "old-hand". Both follow the Book's English ("as Seren drew it", "out of the old hand"). The lexicon has *ryt* as "cut letters, write" and only *hal* "bedrock".

**Beyond the 30 lines.** I also swept all 26,072 word glosses in the JSON through the analyzer:

- every line splits into the same number of words in the analyzer as on the page;
- 121 distinct (word, gloss) pairs could not be matched to the lexicon by simple string matching (`fid/sweep_out.txt`);
- **I read all 121.** Every one is an English inflection or irregular form, or a sense the lexicon gives. Examples: answered/*tess*, lay/*firr*, axemen/*gostard*, kindreds/*lonn*.

None is wrong.

## 6. Tale anchors: PASS

- The 29 tale `<article>` ids are the same list in the same order: t-I-1 … t-VI-3, t-epilogue, t-knowings, t-last-note.
- All 41 element ids outside the drawings are kept. The only new one is `newreaders-h`.
- There are 5,736 ids in all, against 5,735 in v3.0.0. The only id lost or gained is that new one.
- The 13,941 in-page hrefs are identical, and every one resolves.

---

## Noted, not changed (no visible text affected)

- **N1. New place-keeping landmarks.**
  - **What changed:** `data-m="dl1"` was added to the 29 datelines and `data-m="hn1"` to the Last Note headnote. It is in the Book and Original panes, matching the new Plain "when" lines.
  - **What it does:** these attributes only let the switch hold the reader's place.
  - **Why it is kept:** the builder's v3.1.0 notes describe it as intended. The Book's words are untouched.
- **N2. The VI.3 token in the romanisation.**
  - **What changed:** the sentence's full stop now sits inside the token span. In v3.0.0 it was `…Sirrvell</span>.` and in v3.1.0 it is `…<i>Sirrvell.<small>Glasspire</small></i></span>`. The ink line keeps `</span>.` as before.
  - **Why the builder did it** (`build_panes.py` `line_items`, logged as "mark moved into the last word of a span"): every word keeps its own punctuation. If the full stop stayed outside the word box, it would stand off by the width of the gloss.
  - **Effect:** the visible text is identical, and nothing on the page swaps the token.
  - **To undo it:** drop the move in `line_items`, at the cost of that gap.
- **N3. New CSS rules.** They are scoped to Plain (`aside.newreaders`, a headnote that runs to two paragraphs) and to the Original (`.il`). As checked in §1, they reach no Book element.

## Files

- `/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/fidelity_report.md` (this report)
- `/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/fid/` (the check scripts and their outputs)
