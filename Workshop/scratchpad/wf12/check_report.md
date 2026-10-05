# The story page, checked as a reader sees it (wf12, 2026-10-03)

Pages: `wf12/out/Rivenkeep_Legends.html` (repo page) and `wf12/out/web/The_Legends_of_Rivenkeep.html` (web copy).
The web copy was viewed the way the host serves it: wrapped in `<!doctype html><html><head>` with charset, viewport
(`viewport-fit=cover`) and the host's reset (light `color-scheme`, safe-area padding on `:root`, zero body margin,
14px system font on an off-white ground), then `<body>…</body>` (`tmp/reader/web_wrapped.html`).
Everything ran in headless Chrome over DevTools (`wf12/book/cdp.mjs`), with real mouse clicks on the labels.
The scripts and every screenshot are in `wf12/tmp/reader/` (`shots/`, montages in `m/`, the Original sweep in `sweep/`).

**Another pass was working at the same time.** The fidelity pass in `tmp/FID` rebuilt `orig/panes.json` and the page
at 08:25 and 08:30. Between those builds it fixed one problem I had seen in the 08:03 build: the IV.2 Romanisation
folds showed the raw builder marker `[⟦legend_iv2_gap1⟧]`. They now show the drawn mark. My rebuilds came after its
last change, so they include its panes. All results below are from the final build (09:17).

## Problems found and fixed at source

1. **Wood leaves set their controls a fifth smaller** (`book/story.css`). The leaf rule `.wood{font-size-adjust:.405}`
   was inherited by every IBM Plex Mono element inside the eight wood leaves. That shrank each leaf's own switch
   (*The Book · Plain Words · Original*), the WOOD LEAF label, the tale number, every Romanisation and Grain Notation
   fold label, and the Grain Notation itself (10.6px set as about 8.3px) to about 78% of the stone-leaf size. It was
   visible in every wood-leaf screenshot. Fix: one rule after `.wood` resets `font-size-adjust` on `.tale-h`, `.tabs`,
   `summary`, `pre`, `code`, `.cont-cap` and `.lit-h` inside `.wood`. The face match is meant for the wood face only;
   captions, the seal and the frames already had the same reset. Re-measured: no mono text in a wood leaf is
   adjusted now, and the wood and stone tab bars are identical at 1280 and 390.
2. **The first switch to Original could throw the reader off the tale they clicked** (the inline script, in
   `book/build_story_html.py`). The browser loads the leaf-hand (Garl Flenn) only when text first needs it. So the
   first switch to Original set the reader's place, then about 40 ms later the font arrived and the whole Original
   reflowed (+14.8k px at 390). Scroll anchoring could not absorb that. The case: fresh load at 390 in Plain Words,
   scroll to the Epilogue, click its own *Original*. The label went from 422px to 1741px, off screen, and the reader
   was left in the end of VI.3 (`shots/fresh_390_plain_orig_t-epilogue.png`, from before the fix). Reload had the
   same flaw: in Original it brought the reader back to I.5 instead of II.1. Fix: the script now starts the leaf-hand
   loading as soon as the page opens (`document.fonts.load`, inside try/catch). After each switch it also sets the
   place again two frames later, at 150 ms, and when the fonts are ready if any face was still loading. Each of these
   re-settings does nothing when nothing has moved. The extra settings also cover the 31px that VI.3's songline carving
   added under the Epilogue's label when content-visibility first laid it out. I tested the re-setting alone, with the
   preload taken out of a temporary copy, and it also holds the Epilogue case to 0px.
3. **The sticky bar drifted on repeated switches** (same script). A switch leaves its anchor on the reading line to a
   fraction of a pixel. On the next switch, an anchor 0.4px below the line was read as the next anchor down. The step
   was then interpolated across the target's whole gap. In the Knowings at 390, Book → Original → Book → Original
   drifted up a paragraph (174px). Fix: an anchor within 2px below the reading line now counts as on it. Retested:
   the cycle holds row 1 every time.

After each fix I rebuilt with `python3 book/build_story_html.py --doc-version "v3.0.0"`.
`python3 book/check_story.py` reports **ALL CHECKS PASS** on the final build: 62 of 62 leaves word for word,
1367 Original blocks in place, ids unique, and the web-copy contract.

## What I saw (screenshots read, 1280 and 390, all three texts)

- **Title page.** The Book and Plain Words each show their own line. In Original, the Book's names and the title-page
  line are in Seren's ink, gold, each with its Romanisation fold, and the title stays in capitals. The Contents is in
  ink. At 390 the title wraps cleanly to two lines.
- **I.1.** The dateline (Book only; Plain Words has none in its source), the headnote, the drop cap, and the story.
  Original: title, dateline and headnote in ink, then every paragraph in the leaf-hand with a closed Romanisation fold.
  The facing leaf (the Stone's rings) is in place.
- **IV.3.** The Book and Plain Words set the warden's blots (▒▒▒▒) as dotted squares, 12 in each text. Wendhessa's seal
  is caption-only, between two short gold rules, in all three texts (owed: see below). The Original has the headnote
  and caption in ink.
- **IV.4, the wood leaf.** The READING: nine em-dash fragment lines in the wood face, the two inks alternating, ending
  in the open gap `[ ]`, the seal *This is held in the grain.* under them, then the story. Plain Words is the same.
  The Original has the nine reading lines in ink with their folds, then the whole round (the gift, Myststone), then
  24 ring plates, rings 1 to 24, each with its Grain Notation fold, plus the cited round in ring 23. All are drawn at
  1280 and at 390 (plates about 350px wide at 390).
- **V.7's carvings.** The Book and Plain Words set them as wood-face inscriptions. The Original draws them as rounds:
  the bearer's plank E4-01 (*Three roads, one hour*), the deceiving hull's plank E5-02, the ring it was cut against
  (E5-02's ring 4), and V7-III (*the end of a whole morrow*). Enrella's mark is caption-only (owed).
- **The Epilogue's stone.** In all three texts: the Last Carver's letters across an unknown grain, with its caption. The
  Book and Plain Words fold the translation. The Original folds the Grain Notation and sets *the words set in* in ink.
- **The Book of Knowings.** The Book and Plain Words: at 1280, a four-column table; at 390, each row a stacked card
  with labelled cells. The Original: each root as a run of carving cards with arrows between them, each card with a
  Romanisation fold and a Grain Notation fold (E1-01 → E2-01 → E4-01 → E5-01, and so on). The Last Note's three
  stones are caption-only (owed).
- **Sweep.** I screenshot the top of every one of the 41 switch units in Original at 390 and read all nine montages.
  Every unit is filled, and nothing is blank, broken or overlapping.

## The one switch, driven as a reader drives it

| check | result |
|---|---|
| Click *Plain Words* in VI.3's own bar, far down (repo and web, 1280 and 390) | all 41 units show Plain Words; the clicked label moved 0–1px (495→496 at 1280; 464→464 at 390); VI.3 stays in view |
| Every leaf really shows Plain Words | I.1, IV.4, the Epilogue, the Knowings, the title page and the Contents each show their Plain text |
| A leaf's own label, all 31 leaves, all 6 directions, in sequence (repo 390, web 1280, web 390) | worst move 0px |
| Fresh load, then a leaf's own label (58 cases at 390: plain→orig and orig→book on 29 tales, plus spot cases on web 390 and 1280) | all within 1px; none out of view |
| Sticky bar mid-tale (V.5, II.2, IV.3, Knowings) | the same paragraph stays on the reading line across Book ↔ Original. Through Plain Words it can land one paragraph off, because Plain Words keeps only landmarks, not line anchors (IV.3 at 390: b1342 → b1344) |
| The choice survives a reload | yes: radio restored before first paint; `localStorage` holds `read-plain`; a real reload lands on the same paragraph in Plain Words and in Original |
| `#t-IV-4` in the URL | lands on IV.4, just under the bars (tale top 78px, bars 65px), in the stored text |
| Script disabled (`Emulation.setScriptExecutionDisabled`) | the CSS switch alone: V.2's own *Original* turns all 41 units to Original; the bar's *Plain Words* turns all 41 back |

## Page-wide checks (final build)

- **No horizontal scroll at 390.** `scrollWidth` equals the viewport on every screenshot, and the audit found no
  element past the viewport in any text, with every fold open (1485 `<details>`). 270 Grain Notation blocks are wider
  than the column, and each scrolls inside its own box. The only element in the 16px gutter is the footer box, whose
  text is padded.
- **Every Original pane is filled.** All 41 units have an Original pane with content. There are no empty ink lines, no
  raw markers (`⟦…⟧`, `{{…}}`, `<!--`), and no placeholder text (*set down anew*, TODO and the like). The 223
  `{again}`/`{all}`-style forms all sit inside Grain Notation `<pre>`, where they are notation.
- **Every drawing is drawn.** 276 drawings show in Original and 10 in The Book and Plain Words. Each has a box, painted
  content (non-empty `getBBox`), and no dead `<use>` reference. All literal SVG colours (1295) are mask luminance
  values inside `<mask>`.
- **The leaf-hand loads.** `document.fonts.check('16px "Garl Flenn"')` is true on both pages, and the ink's computed
  face is Garl Flenn. The font covers every ink character except `[ ]` (the open gap, set in the house face by
  `.ink-gap`) and `▒` (the warden's blots, `.ink-blot`), both on purpose.
- **Web-copy contract.**

  | rule | result |
  |---|---|
  | page skeleton | no doctype, `html`, `head` or `body` tags |
  | first thing in the file | `<title>The Legends of Rivenkeep</title>`, then one Google Fonts `<link>`, then one `<style>` |
  | colour tokens | one `:root` with `color-scheme: dark` (a deliberate single dark theme); body background from a token; no literal colour outside `:root` |
  | leaf-hand font | inline, base64 |
  | outside loads | Google Fonts only |
  | sticky bar | `top: env(safe-area-inset-top, 0px)` |
  | links to other files | none |
  | size | 12,356,546 bytes (11.78 MB), under the 16 MB limit. The repo page is 12,358,939 bytes |

## Left as they are, by rule or as open calls (not faked)

- **Eight native drawings are owed** (six distinct): `legend_stonwryt_aldwena` (I.4), `legend_title_capstone` (I.4),
  `legend_stonwryt_halyna` (II.3, VI.3, the Epilogue), `legend_seal_wendhessa` (IV.3), `legend_stonwryt_enrella`
  (V.7) and `legend_three_stones` (the Last Note). None exists in `wf6/svg`. Under *truth or nothing* (notes_v3 §5.6
  and §5.8), each stands as its caption alone, between two short gold rules, in all three texts. It does not read as
  a broken image. The builders draw each one on their next run once its SVG exists.
- **Eleven drawing captions stay in English in the Original** (the Hal, both coal Titles, the bare rings, Seren's note,
  Aldwena's mark, the capstone Title, Halyna's three marks, the Epilogue's Stone). Six are in ink. This is the merge
  report's open call, §9 item 6: one rule for the Original either way.
- **The warden's blots (▒▒▒▒)** come from the source. The house faces have no such glyph, so the system's fallback draws
  them, as dotted squares on a Mac.
- **Plain Words has no datelines, and no headnote on the Last Note.** Both follow `plain_v3.md`.

## Files changed

- `wf12/book/story.css`: the `font-size-adjust` reset for the furniture inside wood leaves.
- `wf12/book/build_story_html.py`: the inline script (leaf-hand preload, the place set again after a switch, the 2px
  anchor tolerance) and its note in the docstring.
- Rebuilt: `wf12/out/Rivenkeep_Legends.html` and `wf12/out/web/The_Legends_of_Rivenkeep.html`. Nothing in `orig/` needed
  a change.
