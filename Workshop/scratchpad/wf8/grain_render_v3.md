# THE GRAIN · RENDERER NOTES v3 (presentation only)

*wf8 workflow document, 2026-09-28. Not a Book leaf and not a repo doc; nothing here goes into `Docs/`. It answers Jack's note of 2026-09-27: "I like that Seilrhass has an anchor in the middle of the tree and the details are added in the outer rings... I would like to see it more intricate and more intertwined." It changes **only how a whole round is cut for the page**. The meaning of Grain Notation, and every rule of `wf7/grain_v2.md` (§§3–15 and §21), is untouched.*

**Before/after sheet:** `wf8/grain_v2_v3.png`. **Renderer:** `wf8/render_grain3.py`, a copy of `wf7/render_grain2.py`. Its data are copies in `wf8/grain3/`:
- `data/`: the signs, and IV-6.json;
- `texts/`: the Book's `.gn2` texts, and IV-4 from `wf7/pilot_IV4.md` §4 (identical to `pilot_IV4/IV-4.canon.gn2`, with the `# file` legend dropped as `wf7/orig/make_grain.py` does).

---

## Renderer notes v3

### v3.0 What was wrong

At page size (about 700 px wide) a whole leaf read as **sparse and faint**: small scattered marks and pale lines, not a carving.

The v2 renderer cut every round with one knife, sized for reading scale. On IV.6 (radius about 1,000 units) one unit is about 0.35 px on the page, and on IV.4 (about 1,280 units) about 0.27 px. So the v2 runner, 2.7 units at its node, becomes a sub-pixel hairline, and its crossings (gaps of about 3 units) disappear.

The structure (runners, braids, binds, years, cells) was all there; it was simply drawn too finely to see.

### v3.1 The page weight [rule]

- A **whole round** is cut at a page weight **pw = clamp(R_K / 400, 1, 2.8)**, where R_K is the nominal radius of its outermost ring.
  - IV.6: pw = 2.34.
  - IV.4: pw = 2.80.
  - The gift's sentence: pw = 1.46.
- Every v3 device scales with pw. At **pw = 1** nothing in v3 applies.
- **Byte-identical to v2** (checked): the Hasty seven, *Burn*, VI.1, *Naelear*, E4-01 (pw 1), the chip, and every **ring plate** (IV.6 plates 5, 7 and 9, IV.4 plates 5 and 12, the gift's plate 2).
  - The plates are the reading surface (grain_v2 §11.5), so they keep v2's exact cut.
- Rounds of three rings or fewer, stage-0 rounds and plates are never page-weighted. Young carvings stay simple.

### v3.2 The Law of the Rings, carried into the figure [rule]

Each ring k gets a **figure strength** tex(k), which sets how much of v3's secondary texture it shows:

| Where | tex(k) |
|---|---|
| the heart ring, or a joined round's own pith rings | 0 |
| band I | 0.45 |
| band II | 0.80 |
| band III | 1.0 |
| a round of six rings or fewer | the band's value × 0.6 |

So **the anchor stays plain and the detail is outward**, as Jack asked. The heart ring gets:
- no figure, wake, knot-eye or ring-split;
- runners at **v2's own knife**. A runner is kept at v2 width wherever it runs inside the heart ring.
- The one v3 change the heart shares with the rest of the round is the wider dark knock-out margin round every cut, the root's included (v3.4). It adds no ink.

### v3.3 Runners: bolder, and visibly over and under

1. **The knife.** A runner is cut at pwr = 1 + 0.5 (pw − 1) of its v2 width at the node and along its body (IV.6 ×1.67, IV.4 ×1.90).
   - Its **terminal point stays v2's 0.45**, so it still stops a knife-width short of the head it lands on (§6.1).
   - The bud keeps v2's node-to-body ratio.
   - A braid's strands take half the extra weight, which keeps the plait open.
   - A pocket's runners keep the pocket's finer knife.
2. **Clearance caps.** The heavier knife narrows wherever it would crowd something (legibility fixes 1 and 3, below):
   - it keeps **1.9 units** from any other mark's ink, as v2's cut did;
   - it keeps **1.0 unit** from its own two marks' ink, as v2's bud did;
   - a runner running within 25° of another takes **at most half the wood between them, less a dark margin**, so two runners never merge;
   - it keeps **8.3 units** from another runner's end, which is the reach of a terminal (cup, tines, root-hairs, bars, bud).
   - Narrowings are held over ±8 units and eased at 0.12 per unit. They are never thinner than v2's own cut.
3. **Stroked, in steps of the taper.** On a heavy round (more than 40,000 units of runner, the same test as v2's silhouette mode), the runners are drawn as stroked centre-lines:
   - one path per width step, five steps along the taper;
   - round joins, and a **square end at the node**;
   - bud, terminals and splinters are cut as before.
   - This is more compact than v2's silhouettes, and the wake (v3.5) reuses the same paths.
4. **Tone.** Runners are one tone at 0.88. The marks stay the brightest thing in the round at 0.97, which keeps the intent of call §19.2(a).
5. **The groove.** The wood's knock-out margin round a runner widens from 2.2 to 2.2 + 3 (pw − 1): IV.6 6.2, IV.4 7.6. Each runner lies in a **dark groove**, so where two cross the over-strand is visibly lifted.
6. **The gap.** The under-strand's gap at a crossing widens to:
   - H_RUN·pwr + 1.5·(1 + 0.9 (pw − 1)) each side;
   - at half that extra for a braid's or a bind's close strands.
   The under-strand's cut ends are round (**clean**: a pass). A break's ends still **splinter** (two tines, 2.8 × (1 + 0.5 (pwr − 1)) long, at −40° and +36°), so pass and break read at page size.

### v3.4 Round every mark: the knot-eye and the yield

- **Knot-eye.** Round every mark outside the heart ring, the wood's mask knocks out a lens at 62%, pointed along the grain.
  - It reaches 3 + 2.2 (pw − 1) along the ring and 2 + 1.2 (pw − 1) across it, both scaled by 0.6 + 0.4·tex.
  - It is a knot's darker wood. It adds no ink, so it can never be a band, a pocket or a sign.
  - The knock-out margin round every sign widens from 3.4 to 3.4 + 2.4 (pw − 1).
- **Yield.** The ring lines' yield round a mark (grain_v2 §4.6) deepens to 1.2 × (1 + 2.5 (pw − 1)) outside the heart ring.
  - The §4.6 check (no two lines within 4 units) still passes on both rounds.
- **Latewood.** Latewood bands are up to 1 + 0.6 (pw − 1) wider, and 1 + 0.1 (pw − 1) stronger, outside the heart ring.

### v3.5 Where runners pass: the bark-flow

- **The dip.** Where a runner crosses a ring line, the line dips further and wider:
  - 1.3 + 3.5 (pw − 1)·t over 3.6 + 6 (pw − 1)·t units, where t = min(1, tex / 0.45);
  - the grain is dragged along a passing root.
- **The wake.** Six faint contour lines lie at even, widening distances from every runner's course:
  - opacity 0.28 falling to 0.07, line width 0.55 pw^1.5;
  - where runners lie close their wakes merge, and where they cross the wakes turn with them;
  - the grain swirls round the runners, which is the "intertwined" look at page size;
  - drawn as the runners' own stroke paths in a mask, and gated by tex band by band.
- **Where the wake is never drawn:**
  - in the heart ring;
  - in a pocket (± 4 units) or a lined condition band (STILL, WATER, WHITE, DREAD);
  - within 2.5 + 0.75 (pw − 1) units of a year-line.

### v3.6 Ring-splits

- Where the carving disturbs a ring line (a mark's yield, or a runner's dip), the line's latewood **splits into 1 to 3 finer strands** on its inner side. They follow its bow and rejoin it in open wood, like the grain crowding round a knot.
- The number of strands grows with tex: 1 in band I, 2 in band II, 3 beyond.
- **Guards**, so a split never reads as a line that carries meaning:
  - pieces are at most 150 units, so never a whole ring and never a band-rule;
  - opacity 0.30 / 0.24 / 0.18, width 0.6 (1 + 0.55 (pw − 1));
  - a split is always **attached to a ring line at both ends**, whereas a pocket border is a closed lens with tips on half-file lines, a mouth and items (see v3.9).

### v3.7 The figure

- Seeded grain lines run between the ring lines at spacing (9.5 − 3.5·tex)(1 + 0.3 (pw − 1)). They are broken into runs of 90 to 320 units, each flecked by one of three seeded dash patterns (5 to 20 units on, 9 to 34 off, × pw^0.6).
- **Knot-halo.** Each line parts round every mark: above a mark's head it crowds over, below its foot it crowds under, and beside the mark it rejoins. The line drops out where it would cross the mark.
- **Bark-flow.** Each line is dragged along every runner that crosses it.
- **Guards:**
  - never within 4 units of a year's floor, where year-lines are read;
  - never in a pocket or a lined condition band;
  - opacity 0.15 to 0.29 in four tiers, width 0.6 pw^1.3.
- A figure line is always fainter than a year-line or a pocket border, and it is **flecked, never a full circle**. Drawn as continuous lines, the figure read as the rejected vinyl look (grain_v2 §1.2).

### v3.8 Year-lines

- At page weight a year-line is cut as what it is: a **wedging ring**. It is a sliver that swells in its middle and pinches out at both ends, 0.8 (1 + 0.9 (pw − 1)) wide at 40%.
- It is laid **above** the wood's knock-out, so a mark's wider margin never eats the year-line under its foot (legibility fix 5, below).
- It spans exactly the v2 year-line's arc (±0.62 of a cell), at the year's floor.

### v3.9 Legibility regressions found by the decode check, and fixed

1. **Heavy strokes crowded other marks and terminals.**
   - What happened: IV.4's c7 ran over c3's through-tines, and a4's *as*-runner bled onto the heads beside it.
   - Fix: the clearance caps of v3.3 (2).
2. **The node's round cap read as a bud-knot or a cup.**
   - What happened: IV.6's a2 at its source looked like a terminal.
   - Fix: the run from the node is cut **square**, and the bud keeps v2's shape.
3. **Width steps, cut square, made ladder-notches that read as crossing gaps.**
   - Fix: round joins, width hysteresis, and eased plateaus.
4. **The wake had seams.** Butt joins in its mask left light squares at every width step.
   - Fix: round caps and group opacity.
5. **Year-lines were eaten** by the wider knock-out margins.
   - Fix: the slivers of v3.8, drawn above the mask, with the wake and the figure kept clear of them.
6. **The anchor was no longer plain.** Runners inside the heart ring were cut heavy.
   - Fix: they keep v2's knife.
7. **Wood figure could rival the read lines.** Wake lines at 0.34 and ring-splits at 0.40, some 1.7 units wide, could be mistaken for pocket borders (said: 0.62 and 0.34).
   - Fix: the wake is capped at 0.28 and ring-splits at 0.30, and the splits are finer.

### v3.10 Not Arrival, and the other near-looks (grain_v2 §15), re-checked

- Nothing leaves the rim: the wake, figure and splits are masked to rings 2 to K.
- There is no ink blot and no smoke. The knot-eye is a knock-out: darker wood, not ink.
- There are no tendrils and no single brushed ring. The wake follows the runners along the grain, and the figure follows the rings.
- There is no spiral, no closed circle besides the growth rings, and no interlace off a crossing.
- Colour is currentColor under `class="wood-ink"`. The masks use luminance only.

### v3.11 What v3 does not change (checked by `wf8/grain3/work/equiv.py`)

On IV.6, IV.4, the gift's sentence and E4-01, the v2 and v3 renders have **identical**:
- marks (placement, span and breadth);
- runner courses;
- crossings (over, under, kind): IV.6 has 109 passes, 1 break, 3 braid crossings and 1 braid-break; IV.4 has 231 passes, 9 break crossings and 2 bind locks;
- runner ends;
- validator warnings.

The router, the packing and the signs are not touched. The whole-round `--check` is deterministic (two runs byte-identical).

### v3.12 Size

| Round | v2 | v3 | Budget (grain_v2 §11.6) |
|---|---|---|---|
| IV.6 whole | 306.8 KB | **344.7 KB** | 350 KB (within) |
| IV.4 whole | 429.1 KB | **479.2 KB** | 350 KB (v2 was already over) |
| the gift's sentence | 74.8 KB | 113.6 KB | — |

- Everything is still symbol-based: every sign is one `<symbol>` placed with `<use>`.
- The new cost is:
  - the figure, in four opacity tiers × three dash patterns, each one path, at whole-unit precision;
  - the stroked runner steps, which the wake reuses;
  - the knot-eyes, one path;
  - the year-line slivers, one path.
- IV.4's size is mostly v2's own: 145 KB of symbols and 46 KB of placements.

---

## The mini decode check (2026-09-28)

**Method.**
- Both whole rounds were re-rendered by v3: IV.6 from `wf7/grain2/`'s text (`grain2_texts/IV-6.gn2`, the same GN as `grain2/IV-6.json`), and IV.4 from `wf7/pilot_IV4.md` §4.
- `<title>`, `<desc>` and the aria labels were stripped.
- The rounds were cut into v2 | v3 crop pairs at reading scale:
  - IV.6: 51 crops, in `grain3/decode/IV-6_decode_0–4.png`;
  - IV.4: 70 crops, in `grain3/decode/IV-4_decode_0–5.png`;
  - plus year-line crops for both, in `*_yearlines.png`.
- Each crop was read by eye by grain_v2 §14.1 and compared with the model's own list of what it holds (`*_decode_manifest.json`).

**IV.6** (pw 2.34).
- **Roles.** Every runner role reads by its terminal and landing: *to*, *then* (arriving at the foot), *in* (cup), *with* (merge at the flank), *for* (bud), *because* (root-hairs), *as* (two bars), *through* (two tines), *that* (ending in a pocket's mouth), *blind* (an empty cup in empty wood), and *to @file* (ending in an empty cell).
- **The break** e1 ⊳ f1 crosses square, once, with splintered ends.
- **The braid** *abab!* has 4 crossings; the over-strands read p, q, p, q, and the last crossing is splintered.
- **Passes.** Six of the 109 passes were sampled. In each, the continuous strand is the later one in canonical order.
- **Pockets.** P1 (cut, jagged border) and P2 (said, doubled border): mouths and items read.
- **Fringe:** *more*, *most*, *still*, *last*, *all*.
- **Year-lines, and the heart.** The year-lines read, and the heart holds only the root HOLD, plain.

**IV.4** (pw 2.80).
- **Roles.** The same eleven runner roles and landings read.
- **The bind** K1 reads: two lock crossings, the eye, and one out-runner.
- **Breaks.** l2 ⊳ l1 and m3 ⊳ m2 are splintered.
- **Passes.** Six of the 231 passes were sampled.
- **Pockets.** 6 said and 2 cut: borders and mouths read.
- **Fringe:** *only*, *last*.
- **Year-lines, and the heart.** The year-lines read, and the root GIFT* is plain.

**Still open, from v2, not caused by v3.**
- IV.4's two declared breaks cross 4 and 5 times, not once. The v2 router reports "break m3 ⊳ m2: its legs found no way", and the v2 validator already warns.
- IV.6's P1 spans 8 files (the rule is at most 6).
- IV.4 rings 12–13 have long parallel runner bundles. They are the §15 "circuit board" watch item, and they belong to the router.
- IV.4's canonical GN does not reprint byte-for-byte: it differs by whitespace and the place of one pocket runner line (`run e7 P3.1 → P3.2`). v2 behaves the same.
- At page size IV.4's middle rings on the lower half stay open wood, because the telling carves little on those files. v3 adds texture there, not marks.

## Files

- `wf8/render_grain3.py`: the v3 renderer.
  - `python3 render_grain3.py TEXT -o OUT.svg`
  - `--all` / `--check` write `wf8/grain3/svg/grain3_*.svg`
- `wf8/grain3/svg/grain3_IV-6.svg`, `grain3_IV-4.svg`: the two whole rounds, v3.
- `wf8/grain3/v2out/`: the same rounds by v2, for comparison.
- `wf8/grain_v2_v3.png`: the before/after sheet, built by `wf8/grain3/work/sheet_v2_v3.py`.
- Helpers in `wf8/grain3/work/`:

| Helper | What it does |
|---|---|
| `shoot3.py` | headless Chrome shots |
| `cache.py` | repaints from a pickled route, for quick presentation passes; checked byte-identical to a full render |
| `equiv.py` | the v2 = v3 structural check |
| `decode_sheet.py`, `yl_check.py` | the decode crops |
| `sizes.py` | the SVG size breakdown |
| `render_grain2_ref.py` | v2, pointed at the copied data |
