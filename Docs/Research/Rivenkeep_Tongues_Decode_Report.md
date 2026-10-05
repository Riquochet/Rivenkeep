# Decode test: the course-hand and the grain, read from the pictures alone

> **Imported to `Docs/Research/` on 2026-09-27** as a source behind `Rivenkeep_Tongues.html`, which is canonical where the two differ. Scripts, renderers and file paths mentioned below belong to the design workspace and are deliberately not in the repo, which is documents only.


*wf6, 2026-09-27. A workflow report, scratchpad only.*

## 1 · Method

- **What the decoder was allowed.** Only the two specs, and the pictures.
  - `shoreland_spec.md`: §0–6 and §11, with §7 (the samples) left closed.
  - `mystaeri_spec.md`: §0–4 and §10, with §5 (the samples) left closed.
  - Not opened until the comparison: the renderers, the grain texts, the inventory, `index_*.md`, and every `<title>`.
- **The pictures.** `decode/blind.py` removes `<title>`, `<desc>`, comments, `<text>` and every `aria-*` and `data-*` attribute. It inlines the SVG on a dark page and shoots it with headless Chrome at 3–40×, cropping with CSS. The screenshots are in `decode/shots/`. The SVG source was never read.
- **Not blind from the start.** §0 of each spec already quotes two texts: Seren's line and the Title in the Shoreland spec, and the Aelthar and the sliver in the Mystaeri spec. Those four were decoded anyway, and are marked below.
- **Samples.**
  - Ten course-hand images: `shore_tumar`, `shore_guest`, `shore_cry`, `shore_calls`, `shore_proverb`, `shore_invocation`, `shore_carver`, `shore_stonwryt`, `shore_seren` and `shore_title_coal`.
  - Six grain rounds: `grain_E1-03`, `grain_VI-1`, `grain_E2-01`, `grain_GROW`, `grain_AELTHAR` and `grain_E4-01`.
  - No charts were used for decoding.

## 2 · The course-hand: 10 of 10 exact

Each line below was read letter by letter from the picture, before §7 was opened.

| Image | Read from the picture (hand) | Romanised | English as decoded | Against §7 |
|---|---|---|---|---|
| tumar | `t.u.m.A.r \|` | *Tumar.* | We remember. | exact |
| guest | `h.e.s.s , h.e.l.v , s.e.n.n.O.l` (no end mark) | *Hess, helv, sennyl…* | Stop… sky… dying… | exact |
| cry | `k.a.r.m e.t l.o.dh h.y e.t t.r.u.n \| t.a.l.d.a , s.t.o.n.w.r.y.t.a.n \| k.a.dh.a t.o.l.m u.m t^S.o.l.m \| s.t.o.n.a g.o.r h.a.l.d d.e.m e.t d.a.s.k s.o.s.t , t.a.l.d.a t.a.l.d.a t.a.l.d.a \|` | *Carm et lodh hy et trun. Talda, Stonwrytan. Cadha tolm um dholm. Stona gor hald dem et dask sost, talda talda talda.* | The mortar cries out from the ground. Rise, Stonewrights. Lay stone upon stone. Stand firm, every wall, to the very end; rise, rise, rise. | exact |
| calls | `m.a.r.r th.o t^S.r.u.n \| k.y.l th.o p^S.e.dh \| k.e.th , e.l.l l.u.s.k \|` | *Marr tho dhrun. Kyl tho vedh. Keth, ell lusk.* | Shift your ground. Change your shot. Hold, or let go. | exact |
| proverb | `g.r.e.s.t u.m h.o.s , g.r.e.s.t u.m p^S.a.n.a \|` | *Grest um hos, grest um vana.* | Harm upon one, harm upon both. | exact |
| invocation | `k.e.th e.t t.o.l.m \| k.a.dh e.t t.r.e.n.n \| a.m.m k.a.dh.A.t o , e.s t^N.e.s.s e.t o.dh \|` | *Keth et tolm. Cadh et trenn. Amm cadhat o, es dess et odh.* | Hold the stone. Lay the tale. When it is laid, the hearth will answer. | exact |
| carver | `u.l e.t t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th` | *Ul et dumol ol varn, ol theldeth* | In the memory of our home, our families (open end) | exact. The four tells of §6.13 were all seen: no bed, tapering at both ends, the copied N bite, the open end. *et* was identified as the article wrongly set on a construct's head |
| stonwryt | `e.s s.t.o.n e.t h.a.l.d s.y \| r.e k^S.a.dh.A.n o , e.th t.e.s.s.A.n o , s.o.m.m e.l t.o.l.m t.o.l.m \| s.t.o.n \| ⟨gate⟩` | *Es ston et hald sy. Re hadhan o, eth tessen o, somm el tolm tolm. Ston.* | This wall will stand. We two laid it, and we two stand surety for it, while stone is stone. It stands. | exact. *tess* was glossed "stand surety for", where §7 says "answer for"; both are its lexicon senses |
| seren † | `n.a.b^S.r.o.dh.A.t \| n.a.th d^N.o.s.s t.u.l k.e.th.O.l e.t g.u.n.n s.y l.o =h.a.l.y.n.a \|` | as §0 | as §0 | exact |
| title_coal † | `u.l t^N.u.m.O.l o.l v.a.r.n , … o.l s.o.l.l.a.n \|` (coal: no bed, jittered) | as §0 | as §0 | exact |

† The text was already known from §0.

**No failures, so the renderer was not changed.** Four look-alikes slowed the reading, and §6.12 now names them:
- a word-final *l* or *w*: its free low stone looks like a wedge;
- a middle stone against a top stone on the offset upright, which matters in the coal hand;
- a full *a* against the harmonic *A*: an order to many (*Talda*) against the 3du;
- the Carver's tapered N bite, drawn as a cup of three strokes.

**Two notes for Jack, neither a fault:**
- `shore_stonwryt.svg` has no **HAL | RHYN** signature, although §7.6 says the Captain's Stonwryt is signed.
- The locked leaf's ids begin `sh-serenx-`.

## 3 · The grain: 1 of 6 right first time, 6 of 6 after the fixes

### 3.1 · The blind readings

| Round | Read from the picture | English as decoded | Intended (§5) | Result |
|---|---|---|---|---|
| **E1-03** | `{green; pith war; rings 1} r1 0: LONE*`. The short cut stands clockwise of the long one, and neither has an entry-nick, so it is not BREATH | "One goes ahead of the rest" (the §3.5 meaning) | `r1 0: LONE*` · *Go until struck. Where bark splits, turn aside.* (one word: *go*) | **Structure right, English wrong** |
| **VI-1** † | `{green; round pith; 1 ring}`: HOLD cupped round the pith; HOME leaning clockwise and HOMESTONE counter-clockwise from one foot (the pair); US×3 folded inside HOME's loop | "We hold our home, and yours, the two bound; those of the breath folded in ours" | same structure · *We remember our home too.* | **Structure right, one word wrong**: *hold* for *remember* |
| **E2-01** | `{war; 2 rings}`: WAVE*; a band-rule over included bark; `r2 4: EDGE+BREAKER`; a DREAD shake across files 14/15–1. A tie leaves near the root's head and ends in r2 at about 62°, over file 3, where nothing is cut | "To the shore, all at once; stone-breakers at the edge on the right; the dread across the way" (the tie's target was guessed from proximity) | `tie 0.r1 → 4.r2`, DREAD 15–1 | **Tie misread** (2 → 3); a band edge was ambiguous |
| **GROW** | `{round pith; 2 rings}`: `r1 0: GROW*` stretched to r2 (the span); `r2 2: !MOUTH+SHORE`. The negation was read from the entry-nick on the counter-clockwise side | "Grow until the shore is silent" | same | **Pass**, though `!MOUTH` came by elimination (§5) |
| **AELTHAR** † | `{round pith; 6 rings; rules after 2, 4}`: **`r1 0: AXE*`**; `r2 0: DOOR · 1: GIFT`; `r3 15: US · 1: US`, each leaning toward the other; `r4 15: WOUND · 1: WOUND`; `r5 0: AELTHAR`; `r6 15: WOUND · 0: BOND · 1: WOUND`; `bark 0: HOLD` | "The felling. At the door, a gift. Two of us, turned to each other. A cut on each. Two bloods made one. Bound: a wound on the one and on the other. Held in the grain." | `r1 0: KNEEL*` · *One kneels … two, brow to brow …* | **Root misread** (AXE for KNEEL); the lean had no rule; the rest was right |
| **E4-01** | three square piths, each with WAVE* along the same axis; pith 0 holds E2-01 whole; `r3 0: GO`; `r3 4: GO`; `r4 10: SQUARE+EYE` inside a graft, with a memory ray to the south pith; `bark 0: BOND+TIDE`. **Not read:** r3 file 2 (an "unknown three-armed cut") and the west group, read as one "cut–knot–cut". The hairlines on the left were not sorted into DREAD and ties | "Three roads, all to the shore… the reach, borrowed and remembered…" (incomplete) | `r3 2: BOND`, `12: KNOT^r4`, `r5 12: GO`, DREAD r3 11–13, ties `10.r4 → 0.r4` and `10.r4 → 12.r5` | **Four marks and two ties misread** |

† The text was already known from §0.

### 3.2 · Every mismatch, with its cause and its fix

| # | Mismatch | Cause | Fix (so it cannot recur) |
|---|---|---|---|
| G1 | E1-03 read as LONE's lasting signature, not its young-wood order | **Unlearnable rule.** A root alone in a sapling reads its line's whole order, but those orders lived only in the §5.5 sample table | `mystaeri_spec.md` §3.5: a new table, "A root alone in a sapling", gives the one word and the whole order for all seven roots and *Burn*, and says a sapling is read by it |
| G2 | VI-1's HOLD read as *hold*, not *remember* | **Unlearnable rule, and a contradiction.** §3.5 said *remember* is HOLD with a memory ray, and the sliver has none. "HOLD at the root = remembered" was stated only in §5.1 | §3.7: a new device, **held at the root** (HOLD cupped round the pith, the memory ray's own heart: *ralthein*); §3.5's coverage line points to it |
| G3 | AELTHAR's root read as AXE | **Renderer and sign table.** In a clamped 56-unit heart ring the root is only about 16 units broad, so KNEEL's fold (0.58 B) lay flat against its stem. It looked exactly like AXE's blade, "a solid blade on its clockwise side at the head". §3.12 never overlaid the pair | `grain/signs.json` and §3.5's JSON: the KNEEL fold goes from `(0.66,0)→(0.4,0.58)` to `(0.62,0)→(0.3,0.86)`, which opens a V beside the stem at any breadth. §3.5 now says what tells the two apart: nothing is cut above KNEEL's fold, while AXE's haft runs the whole space under a three-faceted blade. §3.12 adds KNEEL/AXE to the overlay pairs, **at root size**. A widening of every root's breadth was tried and dropped: it redrew every round and did not open the V |
| G4 | AELTHAR r3: two leaning US had no meaning | **Spec ambiguity.** GN had `/` and `\`, but §3.7 defined a lean only as the pair (a shared foot) | §3.7: a new device, **lean**. Two signs in one ring leaning toward each other meet face to face, brow to brow |
| G5 | E2-01's and E4-01's root tie read 2 → 3 instead of 0 → 4 | **Renderer bug.** Tie ends stood 1.15 B/ρ off the file. A mark is about ±0.8 slot broad, so that put each end more than a slot away. Measured over all the samples: **8 of 28 tie ends** (in 4 of 14 ties, in E2-01, E4-01 and STONE) lay over a neighbouring, empty file | `render_grain.py`: every placed mark keeps its own facet polygons. A tie is drawn file to file, sampled one unit apart, and trimmed so that it stops **one knife-width (3 units) from each mark**. A cross-ring tie bends over its first and last thirds so that it leaves just past the source's head and lands just under the target's foot, with no elbow. The **validator now warns** if any tie end is nearer another mark than its own, or stands off its mark and its file. Spec §3.7 gains "How a tie's ends are read" (by the marks they touch; the thick end is the source; an end on an empty file is a bearing); §3.12 step 5 points to it; §10.7 is rewritten |
| G6 | E4-01: BOND on r3 file 2 unread; KNOT^r4 and GO on file 12 merged into one "cut–knot–cut" | **Spec ambiguity.** Nothing said which centre the shared rings of a joined round are measured about. The decoder used the nearest pith, and so read the marks sideways | §3.3: in a joined round, the shared rings are measured about **the round's centre**; the axis runs from it through pith 0, every pith's root points along it, and own-ring marks use their own pith. §3.4's frame and §3.12 step 4 say the same. Checked against the picture: about the centre, BOND's stem points out at 56° (file 2), and the west marks lie on one radius at 282, 330 and 400 units (r3–r4 KNOT, then r5 GO) |
| G7 | E2-01's DREAD read as files 14–1 or 15–1 | **Spec ambiguity** (minor). §3.6 did not say where a band's drawn ends lie | §3.6: a band is drawn to the slot edges, half a file beyond s0 and s1; read the files whose centres it covers, rounding a near-edge end inward |
| G8 | E4-01: DREAD shakes and same-ring ties not told apart | **Spec ambiguity** (minor). Both are hairlines along a ring | §3.12 step 5: the shake is two lines with a knocked-out gap and a bright upper rim; a tie is one tapering line |

**Found by the harness, not by the reading:**

| # | Defect | Cause | Fix |
|---|---|---|---|
| L1 | `data-round="naelear"`, `"aelthar-rite"`, `"IV-4-gift"` sat on every grain SVG, including `--state locked` and the stage-0 Stone. A locked leaf would name its own untold word (§3.11 forbids the leak) | **Renderer bug** | `data-round` is written only in the `whole` state (§3.11 and §10.9 amended) |

### 3.3 · Re-render and re-test

- **Re-render.** `render_grain.py --all` gives no warnings, including the new tie check. Every round is within 60 KB (GIFT is now the largest, at 58.6 KB). Two runs are byte-identical.
  - **Changed:** AELTHAR (KNEEL); E2-01, E4-01, GIFT and STONE (ties; STONE's r8 KNEEL too); STONE stage 0 (no `data-round`); the sign chart.
  - **Byte-identical to before:** everything else, and all the course-hand SVGs.
  - Size tables updated in §10.9 and `svg/index_grain.md`.
- **Re-test.** The fixed rounds were shot again and read by the amended rules.
  - **G1–G2:** E1-03 now reads *Go until struck. Where bark splits, turn aside.* from the sapling table. VI-1 now reads *remembered* from "held at the root".
  - **G3:** AELTHAR's root now shows its stem stopping at the fold, with a dark V between stem and leg and nothing above. Beside an AXE rendered in the same heart ring for comparison (`decode/shots/grain_AXEtest_root.png` against `grain_AELTHAR_root_v4.png`), the two are plainly different.
  - **G4:** the lean now reads *brow to brow*.
  - **G5:** checked mechanically (`decode/tie_check.py`). All 27 tie ends that join a mark read to that mark's own file, 3.0–3.9 units from it and nearer to it than to any other. The 28th (E4-01's reach going east) ends on file 0, which is now read as a bearing. Before the fix, 8 ends read a wrong file.
  - **G6:** measured about the round's centre, E4-01's r3 now reads `0: GO · 2: BOND · 4: GO · 12: KNOT^r4`, then `r5 12: GO`, and the two ties land on the reach and on the GO's foot.
  - **All six rounds now read as §5 gives them.**
- **This second reading was not blind.** §5 had been opened, and no fresh decoder was available to spawn. The honest claim is narrower: each cause above has been removed by a rule or a check, and the tie check is mechanical. A fresh blind decoder on the new files is the real re-test, and is worth running.

## 4 · Near misses and things not tested

- **GROW's `!MOUTH`** (passed, but weakly). As a ligature's modifier it is cut at half length and full breadth, so its arms close into a zig-zag. The suggested fix is to cut ligature parts at 0.7 breadth with the finer knife; it is not made, because it would redraw every ligature (§10.11).
- **E4-01's bark name** is about 7 px across at the intrinsic size. It needs §3.11's tap-to-enlarge.
- **The root is narrower than the marks around it** in any round larger than a sapling (about 16 units, against up to 30), which breaks §3.2's "the root is the largest mark". The KNEEL fix does not depend on it. It is left for Jack, because changing it redraws every round.
- **The prototype drawings** (`svg/E1-01.svg`, `svg/AELTHAR.svg` and the others, made by `grain/grain.py`) were not regenerated. They were already superseded by `render_grain.py`.
- **Not decoded:** the Hal texts (§11g says there is no lexicon for them), the charts, and GIFT, STONE, NAELEAR, E1-01/02/04–07 and BURN. The GN of all of these was seen in §5 before any image of them was read.

## 5 · Files

| File | Change |
|---|---|
| `wf6/render_grain.py` | ties drawn file to file, trimmed to 3 units from their marks and landed on head and foot; each mark keeps its polygons; tie-end validator; `data-round` only when whole |
| `wf6/grain/signs.json` | KNEEL's fold |
| `wf6/mystaeri_spec.md` | §3.3 joined-round frame; §3.4 base; §3.5 sapling table, KNEEL and AXE descriptions, JSON, coverage; §3.6 band ends; §3.7 lean, held at the root, how tie ends are read; §3.11 id leak; §3.12 steps 4–5 and the overlay pairs; §10.1, §10.7, §10.9; new §10.11 (this test) |
| `wf6/shoreland_spec.md` | §6.12 the four look-alikes; new §11h (this test) |
| `wf6/svg/index_grain.md` | checks line, GIFT size |
| `wf6/svg/grain_*.svg` | re-rendered |
| `wf6/decode/` | `blind.py` (strip and shoot), `crop.sh`, `tie_check.py`, `shots/` (every screenshot), `backup/` (the renderers, specs, sign table and SVGs as they were before this test) |
