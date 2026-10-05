# RIVENKEEP · THE GRAIN, VERSION 2

*wf8 merged copy, 2026-09-28 (`wf8/grain_v2_full.md`): `wf7/grain_v2.md` word for word, with the grain additions of every wf8 unit merged and harmonised as §21.9 at the end (one compounds block, the A15 readings, the rules the units proposed, the register corrections and the conflicts settled). Built by `wf8/tmp/merge/gen_grain_full.py`; the shared file is untouched. See `wf8/merge_report.md`.*

*wf7 design spec, 2026-09-27. A workflow document, not a Book leaf and not a repo doc. It answers Jack's notes 7 and 8 of 2026-09-27, and it **supersedes §3 of `wf6/mystaeri_spec.md`** (Eilseth, the grain) together with that spec's §10 (Renderer notes) wherever the two differ. Everything in `mystaeri_spec.md` §§0–2 and §§4–9 (Seilrhass, the ladder, the samples, the interfaces) stands, with the amendments listed in §2.3 below. Nothing here goes into `Docs/`; the prototypes are in `wf7/grain2/`.*

> **Note 7 (Jack, verbatim):** "I like that Seilrhass has an anchor in the middle of the tree and the details are added in the outer rings. This keeps it separate from The Arrival. But the same flavor. I would like to see it more intricate and more intertwined."
>
> **Note 8 (Jack, verbatim):** "The Latin cross is fine. Imagine that all languages come from an ultimate base language."

**Status key** (as in the wf6 specs). **[canon]** the Book or the Admiral fixes it. **[rule]** this spec fixes it. **[call]** Jack's decision (collected in §19). **[v1]** unchanged from `mystaeri_spec.md` §3.

---

## 0 · THE SHORT VERSION

1. **The anchor stays at the heart, and the detail grows outward.** The pith, the root sign cut from it along the axis, the rings as steps, the sixteen files as who-and-where, the three bands as the three movements, the band-rules, the seal in the bark: all of v1 stands. What is new is cut **outside the heart ring**, and it grows denser ring by ring, because each outer ring has more wood in it and older wood holds more (§3, the Law of the Rings made visible).
2. **More intricate: the years of a ring.** A ring is still one paragraph (one step). Inside it, every referent's knowings now stack in **years**, the finer growth lines of the ring. Outer rings split each file's slot into up to four **cells**, as real trees add rays when their girth grows (§4). A whole leaf is carved this way: IV.6 becomes 11 rings in 29 years, holding 100 marks and 64 runners.
3. **More intertwined: runners.** Every relation between signs is now a **runner**, a narrow living cut that springs from the head of the sign that governs and **grows through the wood** to the sign it governs. Runners follow the grain, cross the rings on a drift, wind round the marks, and cross one another (§6). **Its end says its role**: to, then, in, with, for, because, as, through, that, or an empty cup for "the wood does not hold why".
4. **Every crossing means something** (§7).
   - **Pass.** The later knowing lies over the earlier one, and the earlier runs on cleanly beneath.
   - **Break.** The runner over thwarts the one under, whose cut ends are splintered.
   - **Braid.** Two or three runners plait along one cord, and the over-strand at each crossing is whose turn it is. So *abab* reads "by turns, each to the other", and *abab!* ends with the last turn thwarted.
   - **Bind.** Two runners hook through each other in a lock, "each holds only with the other". Harm to one is harm to both.
5. **Finer secondary marks.**
   - The **fringe** is eleven tiny cuts at three stations round a sign: all, few, half; only, more, most; again, still, at last, slowly, gently.
   - The **part** device: a sign with some elements cut whole and the rest hollow names a part, so `US:crown` is the head and `HAND:stem` the arm.
   - The **kind-arc** `‿` marks a whole people.
   - **Pockets** are ring-splits holding a knowing inside a knowing. A smooth one holds words said or believed; a jagged one holds a carving cited whole.
6. **47 new signs**, so the eight wood leaves can be carved whole (note 5). Each grows from the First Tongue's marks by the wood's own laws (note 8, `wf7/ancestor.md` §5). All soft readings are existing Seilrhass words or computed reserve roots (§9).
   - The ten roots, *Burn* and the Bar Before, a Latin cross, are kept exactly: "the Latin cross is fine".
   - Every Admiral carving stays valid, word for word (§17).
7. **How a whole leaf is carved** (§11).
   - **One great round per leaf.** Rings are paragraphs, the band-rules fall at the Book's `RING` markers, and years hold knowings.
   - The blank leaf shows the whole round. Seren's facing page adds **ring plates** at reading size, one per paragraph, and the Original tab reads from them. III.2 is ten Throne hearts.
   - Rejected: one round per movement, because it loses the band-rules and is no more legible; and small rounds inside a leaf-round, because that is Gallifreyan's circles-in-circles.
8. **Grain Notation v2** (§13) is a strict superset of v1. Every v1 text parses and means what it meant. A v1 tie is a v2 runner of role *to* or *then*.
9. **Still decodable by rule** (§14). Trace a runner from its node, through its crossings (the continuous strand is over), to its terminal, and the drawing gives back its GN.
10. **Still not Arrival** (§15). The look is many growth rings with carved threads running along the grain inside the bark, with a plain heart and a busy sapwood. It has no ink ring, no tendrils off a rim, no smoke and no weight-as-tone. The three new near-looks are guarded by rule:
    - Nomai: runners never spiral and never branch into trees;
    - Gallifreyan: no circles within circles;
    - Celtic knot panels: interlace only where a relation crosses, never as a border.
11. **The economy of note 1 was always the grain's.** The grain cuts no small word. In v2 **the runners are where the small words went**: *li, na, rhi, si, vi, thi, ri, sei, ei* become roles, crossings and knots (§6.5).

![IV.6 carved whole, prototype](grain2/figs/v2_iv6_round.png)

*`wf7/grain2/figs/v2_iv6_round.png`: IV.6, The Voyage of the Aelvaren, carved whole by the v2 rules. It is 11 rings, 29 years, 100 marks and 64 runners, drawn by the prototype `wf7/grain2/proto_v3.py` from `wf7/grain2/IV-6.json`. The heart holds only the root. The detail is outward. At page size the round is a texture to take in whole, and the ring plates (§11.5) are for reading.*

![IV.6, a zoom into the sapwood](grain2/figs/v2_iv6_zoom.png)

*`wf7/grain2/figs/v2_iv6_zoom.png`: the left side of the same round at reading scale. Runners run along the grain and drift across it. The braid of ring 7 (the fire and the grey, by turns, until the grey) runs down the middle. Marks stand in cells, the MIST bands are pale, and runners cross over and under.*

---

## 1 · WHAT JACK ASKED, AND WHAT THE PROTOTYPES SHOWED

### 1.1 The ask, as constraints

| Jack's words | As a rule of v2 |
|---|---|
| "an anchor in the middle of the tree" | The pith and the root sign are untouched. The heart ring carries the root and nothing fine: no fringe, no braid, no bind, no pocket (§3) |
| "the details are added in the outer rings" | Intricacy is **gated by age and ring** (§3): the fine devices appear only beyond band-rule 1, and outer rings get more cells (§4.4) |
| "This keeps it separate from The Arrival. But the same flavor" | The flavour kept: a script of meaning, taken whole, in circles. The look refused: one inked ring, tendrils, smoke, weight (§15) |
| "more intricate" | years and cells (§4), the fringe (§5.4), parts and the kind-arc (§5.3), pockets (§8), 47 more signs (§9). The task's "sub-rings and ring-splits for clauses" are the **years** (sub-rings that wedge in where a referent's story grows) and the **pockets** (ring-splits holding a knowing within a knowing) |
| "more intertwined" | runners grown through the wood (§6); passes, breaks, braids and binds (§7) |
| (note 8) "all languages come from an ultimate base language" | every new sign and device is derived from the First Tongue's 45 marks by the laws of form G1–G7 (`ancestor.md` §5.3) |
| (note 5) "tier 3 on how far to take the translation" | a whole wood leaf can be carved: the inventory (§9), the layout (§11) and the worked leaf, IV.6 (§12) |
| (note 4) "Nothing obvious. Nothing we could get sued for." | every new sign was checked against its v1 neighbours and the letter and rune look-alikes, and recut where it read as one (§9.4, §15) |

### 1.2 What the prototypes showed (and one idea that failed)

Two layouts were built and drawn with the whole of IV.6, before this spec was written.

- **Full-circle sub-rings, one per knowing.** They failed. Each sentence became a thin ring right round the round, holding one to three marks. IV.6 became 68 concentric lines with specks on them: a vinyl record, sparse and mechanical. The runners, confined to channels and gates, read as a circuit board.
  - `wf7/grain2/figs/rejected_full_circle_years.png` (drawn by `wf7/grain2/proto_v2.py`).
- **Years packed by referent, cells in outer rings, runners grown through the wood.** This is what the spec adopts. The same leaf is 29 years and 915 units in radius, against about 1,950 for the rejected layout. The marks cluster where the story is, and the runners flow along the grain between them. The heart stays plain.
  - `figs/v2_iv6_round.png`, `figs/v2_iv6_zoom.png`, drawn by `proto_v3.py`.
- **A lattice router alone draws 45° jogs and parallel bundles**, which again read as a circuit board. String-pulling in (θ, ρ) removed the look (§6.2): a straight run in (θ, ρ) is a gentle drift across the grain, never a chord.

![the rejected layout](grain2/figs/rejected_full_circle_years.png)

*The rejected layout, kept as evidence: the same leaf with one full-circle sub-ring per knowing.*

---

## 2 · WHAT STAYS, WHAT CHANGES

### 2.1 Unchanged from v1 [v1]

- **What the grain is** (§3.1): it records meaning, not sound, and is taken whole, grown not written, with a soft reading for every sign. Truth or nothing.
- **The round** (§3.2): the pith (round, or square: the war-pith), the heart ring, growth rings, band-rules, included bark, the bark and its contour, the ring shape, and the seed (mulberry32 over FNV-1a of the id, in named sub-streams).
- **The axis and the files** (§3.3): sixteen files clockwise from the root's axis. Even files are bearings; odd files are placeless. The joined-round frame is kept.
- **Rings** (§3.3):
  - outer comes after inner;
  - an empty ring means *a morrow passes*;
  - a span means *until*;
  - the three bands are the three movements.
- **The local frame** (§3.4): P(u, v) = base + u·L·ê_r + v·B·ê_t. The element types and the entry-nick are kept. So are the classifier (straight means of stone, curved means of wood) and the rule that **weight carries nothing**.
- **The 70 signs, the six condition bands and every v1 device** (§3.5–3.7), with their geometry. This includes the ten roots, *Burn*, and BARB, the Bar Before, which is a Latin cross, kept (note 8).
- **Names in the bark** (§3.14); **planks and halves** (§3.10); **the tie-end reading rule** (§3.7), which now applies to runner ends.

### 2.2 What v2 changes

| v1 (`mystaeri_spec.md`) | v2 | Where |
|---|---|---|
| §3.2 ring widths 46 × seeded; year-hairlines "carry nothing" | a ring is divided into **years** of 32 units. Each year holds one step of each referent's story; the faint year-lines under later knowings now carry that division. A ring of one year keeps v1's width | §4.2 |
| §3.3 "marks in the same ring happen together, at one hour" | still true of the ring. Inside it, marks on one file are ordered outward (years, then cells clockwise). Marks on different files are ordered only by runners | §4.3 |
| §3.3 "Everything cut on one file within a band is about one referent" | in a **telling**, within a **ring**, and a file keeps its referent from ring to ring until a new thing-sign stands first on it; orders keep the band rule | §11.2 |
| §3.4 B = min(30, 0.8·ρ·0.3927) | B = min(24, 0.5·ρ·SLOT/c − 3), so every half-file and half-cell line stays a free gate; the root is now always the largest mark | §4.5 |
| §3.7 ties: flat tapered hairlines, two meanings | **runners**: carved narrow V-cuts with ten roles by terminal; ties are runners | §6 |
| — | laps, braids, binds, pockets, the fringe, the part device, the kind-arc, cells | §5–§8 |
| §3.8 "at most two signs on one file in one ring" | at most one mark (a ligature of at most two signs) **per cell** | §10 |
| §3.8 "at most eight marked files per ring" | withdrawn: the gate rule (§4.5) keeps the air instead | §10 |
| §3.9 the Law of the Rings | kept, and now also sets **which devices** each age of wood may carry | §3 |
| §3.12 Grain Notation | GN v2, a superset | §13 |
| §3.13 "No spirals and no branching vines" (Nomai); "Nothing interlocks" (Elden Ring) | restated precisely: runners that follow the grain are allowed; spirals, conversation-trees, interlocking closed curves and knot panels stay banned | §15 |
| §4.4 "a truthful skeleton … not a word-for-word copy" | for tier 3 (note 5), **every knowing** of a wood leaf is carved | §11 |
| §10.11 "GROW's !MOUTH … cut ligature parts at 0.7 breadth" (a near miss, not fixed in v1, because it would redraw every ligature) | **made**: v2 redraws everything anyway | §4.5 |
| decode report §4, "the root is narrower than the marks around it" (left for Jack) | resolved: mark B ≤ 24 and the root's B up to 56, in a heart ring of at least 72 | §4.5 |

### 2.3 Amendments to `mystaeri_spec.md` outside §3 (for the next spec pass)

- **§2.9 lexicon:** add the reserve roots that the new signs read as. They are listed in §9.2, and all come from `ancestor.md` §3.3, computed and not coined: *ther, rhaenel, seiness, veness, rener, rhaenth, resser, rheth, theiss, res, ath, ses, thaes, thevel, sann, veass, naenn, rass, rhir, nass, vaeth, leser, neiler, rhenn, vesel, eissel*.
- **§3.9's vocabulary table** stands; add the v2 rows of §18.
- **§4.2 ladder:** add the v2 device column of §16.
- **§4.4 blank wood leaves:** the round of each leaf becomes the whole v2 carving (§11). The ring counts stand; III.2 is re-specified (§11.4).
- **§5 samples:** each sample keeps its GN. Its drawing becomes the v2 rendering (§17).

---

## 3 · THE LAW OF THE RINGS, MADE VISIBLE: INTRICACY GROWS OUTWARD AND WITH AGE

The canon's law is that "a hull of one season holds one sign; of forty summers, a phrase; of a shore-man's life, a sentence, and a memory in it. The eldest pillars hold a judgement". v1 made it literal in ring counts. **v2 makes it literal in the knife as well.** Each age of wood may carry only the devices it has grown into, and within any round the heart is plain and the fine work is outward. This is Jack's "anchor in the middle … details added in the outer rings", enforced by rule [rule].

| Wood (v1 §3.9) | Rings | Years per ring | Devices it may carry (cumulative) |
|---|---|---|---|
| **green** (a sapling) | 1 | 1 | one sign, from the pith. No runner, no fringe. *The Hasty seven, Burn and the green sliver are drawn exactly as v1* |
| **forty summers** | 2 + empty | 1 | + **one runner** (*then*, or *to*): "a word, and waits for its brother" |
| **a shore-man's life** | 3–6 | ≤ 2 | + memory rays, forks, the question, **cut-pockets** (an older carving cited), fringe of count and time (#, @, again, still, at last), the blind |
| **a long life** | 4–9, several piths | ≤ 4 | + **every runner role**, file referents (@), passes and **breaks**, **braids**, **binds**, hollow and smoothed marks and runners, the part device, the kind-arc, cells |
| **the eldest**; Myststone; every **telling** | up to 24 | any | + **said-pockets**, the whole fringe, names, pale rings |

**Where in the round** [rule]:
- **Ring 1 (the heart ring)** holds the root and, in a telling, the first knowings on files 2–14. It takes no fringe, braid, bind or pocket, and it has one cell per slot.
- **Band I** takes runners and the fringe, and at most two cells.
- **Beyond band-rule 1** everything is allowed, and cells grow with the girth (§4.4).

So the carving is quiet at the heart and busy in the sapwood, as a real tree's figure is.

---

## 4 · THE ROUND v2: YEARS, CELLS AND THE GRAIN'S FLOW

### 4.1 Levels

| Level | In a telling (a wood leaf) | In an order (an Admiral carving) | Drawn as |
|---|---|---|---|
| the round | the whole telling (*theinas*) | the carving (*seth*) | one heart [v1] |
| band | a movement | root · parts · turnings [v1] | parted by band-rules [v1] |
| ring | a paragraph: one step | one step [v1] | a ring line with its latewood [v1] |
| **year** | one step in each referent's story, within the paragraph | usually one per ring | a row inside the ring, 32 units deep; a faint **year-line** under each mark that is not in the ring's first year |
| **cell** | a place for one mark within a file's slot | usually one per slot | up to four side by side in a slot, in outer rings |
| **knowing** | the marks one runner-system joins: a clause, or a sentence | the order in that ring | the marks plus the runners between them |
| sign | a content word | [v1] | a V-cut mark [v1] |

**A knowing, defined** [rule]. A knowing is the set of marks in one ring that its runners join: a connected component of the runner graph, or a single mark with no runner. The grain has no sentence boundaries of its own. A knowing is what one touch holds together.

### 4.2 Years

- **A ring of a telling is cut in years** [rule].
  - Each year is 32 × seeded(0.94–1.08) units deep. The stream is `id/years`.
  - A year holding a pocket is 8 units deeper.
  - In a round of more than 36 years, the pitch shrinks as 32 × 36 / Y, but never below 26.
- **A ring of one year** (every Admiral order, every v1 sample) keeps v1's width, 46 × seeded(0.84–1.20). That keeps the look and the G2 containment of E1-01 → E2-01 → E4-01.
- **The mark band of a year** runs from the year's floor + 3 up to the year's top − 5.5.
  - The top 5.5 units are **runner room**.
  - A mark with foot-fringe (§5.4) starts 4.5 higher.
- **The heart ring** is at least 72 units, spread over its years. The root spans the whole heart ring, from the pith to the ring line − 4.
- **After a band-rule**, the next ring's first year starts 5 units above the doubled line [v1].
- **Year-lines** [rule].
  - Under every mark that is **not** in its ring's first year, the grain shows a faint year-line. It is a hairline 0.7 wide at 20–24% opacity, at that year's floor radius, spanning the mark's cell (± 0.62 of a cell).
  - These are real wood's **wedging (partial) rings**: a year that grew only where something grew in it.
  - They are wood anatomy and are never cut, but they carry the division. A decoder counts years by them and by the mark feet.
  - Years are **not** drawn as full circles: that was the rejected vinyl look (§1.2).

### 4.3 How knowings fill the years: the packing rule [rule]

Knowings are placed in the order the telling gives them.
- **Each mark takes the next free cell of its own file**: cell by cell clockwise across the slot, then the next year outward.
- **A pocket** takes a whole year across its files, above the highest cursor among them.
- **The ring's depth** is its deepest file.

So:
- **Within a referent, later is outward** (and, within a year, clockwise). This is v1's "one file is one referent" and "outer comes after inner", carried inside the ring.
- **Across referents in one ring, the grain does not order**, and knowings about different referents may sit side by side. v1 already said as much: "Marks in the same ring happen together, at one hour". Where order across referents matters, a *then* runner says so.
- It is exactly how a real ring grows: each part of the girth lays down its own wood, and the year-lines wedge in only where the growth was.
- **The packing depends on the marks and pockets only.** Adding or removing a runner never moves a mark (v1's "adding a mark never moves a ring", extended).

### 4.4 Cells: more rays as the girth grows [rule]

- **The number of cells per slot** in ring k is c_k = clamp(⌊(r_k·SLOT − 6) / 58⌋, 1, 4), where r_k is the ring's inner radius. Ring 1 always has c = 1: the root owns files 15, 0 and 1 of every year of the heart ring [v1].
- **A cell's centre angle:** θ = θ₀ + (s + (j − (c_k − 1)/2) / c_k)·SLOT + jitter, where s is the file and j = 0…c_k − 1 the cell. The jitter is seeded ±2°/c_k (`id/mark/…`).
- **Reading.** The file is still round((θ − θ₀)/SLOT) mod 16, because every cell lies inside its slot: a cell never changes the referent. Cells in one year of one file are read clockwise.
- **Real anatomy.** Trees add new rays as the circumference grows, and a cross-section's outer wood carries more rays than its heart. The cells are that.
- **Measured on IV.6.** Cells (1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4 by ring) cut the leaf from 53 years to 29.

### 4.5 Breadth, gates and room [rule]

- **The breadth of a mark:** B = max(7, min(24, 0.5·ρ_mid·SLOT / c_k − 3)).
  - A ×3 mark takes B / 1.3, so its outer copies stay in the cell.
  - H = 0.16·B, clamped to 1.8–6.5.
  - **Ligature parts** are cut at 0.7 breadth with the finer knife, H × 0.8 (the decode report's GROW `!MOUTH` fix, §2.2).
- **The root:** B = min(56, 0.95·ρ_mid·0.589), with H = 0.17·B clamped to 3.2–7.
  - With the heart ring at least 72 wide, **the root is always the largest mark** (v1's intent, §3.2).
- **Gates.**
  - Every half-file line and every half-cell line has at least 3 units clear either side, inside every year.
  - The top 5.5 units of every year are free.
  - Runners use this room, and all the empty wood besides (§6.2).
- **Joined rounds** [v1]:
  - shared-ring marks are measured about the round's centre;
  - own-ring marks are measured about their pith;
  - cells and years apply in both.

### 4.6 The grain's flow: the wood yields round what is cut in it [rule, wood anatomy, carries nothing]

- **Round every mark,** the nearest ring lines bow away from it by up to 1.2 units. The profile is Gaussian: σ along the ring is 0.9·B, and σ across is half the mark's height + 6.
- **Where a runner crosses a ring line,** the line dips 1.3 units over ±3.6 units: the grain yields as it does round a passing root.
- **The KNOT sign's larger deflection** is unchanged [v1].
- **Checks:**
  - no deflection may bring two lines within 4 units [v1];
  - no line may move a mark's pad below 3.

---

## 5 · MARKS v2: ELEMENTS, PARTS, THE KIND-ARC AND THE FRINGE

### 5.1 New element types (added to §3.4's table) [rule]

| `t` | Parameters | Drawn as |
|---|---|---|
| `punch` | `c`, `r` (in B) | a tiny three-faceted chip: a grain of sand or dust, a thought in the mind, a thing found in the eye. It is the only point-like element, and it never sits on a line (§15) |
| `lens` + `across: true` | `c`, `len` (half-length **along the ring**, in B), `w` (half-width **along the file**, in L) | a lens lying across the file: a load on a pole, a bone's knob, a head laid along the ground |

`cut` gains no new options. The `curve` option (Catmull-Rom, from the originality pass) is used by the new signs as in v1 §10.6.

### 5.2 The part device, `SIGN:part` [rule]

**A sign cut with some of its elements whole and the rest hollow names that part of the thing.**
- The whole elements are cut as usual. The others are cut as outlines, as §3.7's hollow is.
- It is v1's *hollow* ("shown, not meant") turned to use: the rest of the thing is *shown* so that the part is *meant*.
- It gives the body and the made thing their parts without new signs.

| Part token | Elements cut whole | Means |
|---|---|---|
| `US:crown` · `STONEFOLK:crown` | the crown | a head; a brow; a face (*viss*, *lein*, *leir*) |
| `US:stem` · `STONEFOLK:stem` | the stem | the neck, "where life goes up into thought" (*thal*, from \*tal-, rise) |
| `US:foot` · `STONEFOLK:foot` | the root-foot | a foot (*niss*) |
| `HAND:stem` | the stem | an arm (*lann*) |
| `HAND:palm` | the palm | a palm |
| `TREE:trunk` · `TREE:boughs` | trunk · boughs | a trunk · a crown of boughs ("crown-hulls") |
| `SAIL:mast` · `SAIL:cloth` | mast · cloth | a mast · a sail's cloth |
| `BEARER:keel` · `BEARER:hull` | the inner cut · the lens | a keel · a hull's shell |
| `NEW:stump` · `NEW:shoot` | stump and its bar · the shoot and its bud | a stump · a shoot from a stump |
| `DOOR:post` | the first post | a door-post; a post |

- **Decoding.** A sign whose full element signature is present, with some elements hollow and some whole, is that sign's part. All hollow is v1's *hollow*. All whole is the sign itself.
- **The one mixed v1 sign.** MOUTHS (two cuts, one hollow) is not a part: its element set, two full cuts at ±0.42, matches no other sign [v1]. The validator keeps it so.

### 5.3 The kind-arc, `‿` [rule]

- **What it is.** After ×3, the kind-arc is a fine ring-arc cut 2.5 units under the three feet, spanning ±1.2 B. It means **those of that kind: a whole people** (Seilrhass *-ear*), where ×3 alone is a plural (*-en*).
- **Examples:**
  - `STONEFOLK×3‿` is *Rhenear* or *Aethear*, the shore-folk as a people;
  - `ROOT×3‿` is *ralear*, forebears, "mothers and fathers";
  - `US×3‿` is *Naelear*.
- **v1 GN without it** stays valid: `×3` alone reads either way, as it did. The Book's NAELEAR chip is redrawn with it.
- **Descent.** It comes from the Bed (\*loð-): those set in one bed.

### 5.4 The fringe: finer secondary marks round a sign [rule]

The fringe is written `SIGN{f,f,…}` in GN. It has three stations in the sign's own frame; all fringe cuts use the knife at 0.55 H, and punches are 0.1–0.11 B.

| Station | Where | Mark | Means | Form |
|---|---|---|---|---|
| **clockwise flank** (how many) | v = +1.16 … +1.22 | `all` | all, every, the whole | a fine cut along the whole flank, u 0.12–0.88 |
| | | `few` | few | one punch at u 0.5 |
| | | `half` | half | a fine cut along the lower flank, u 0.12–0.46 |
| | | `#n` [v1] | n of them; n times | 1–4 bites on the cut's clockwise side |
| **counter-clockwise flank** (which, how much) | v = −1.14 … −1.40 | `only` | only; alone | a short fine cut at u 0.36–0.64 |
| | | `more` | more (than: with an *as* runner) | two punches stepped outward |
| | | `most` | most; the -est | three punches stepped outward |
| | | `@n` [v1] | the n-th | 1–4 bites on the counter-clockwise side |
| **under the foot** (how it went) | 2–4.5 units under the mark's lowest point | `again` | again; once more | two tiny ring-arcs, ±0.28 B |
| | | `still` | still; yet (*eir*) | one tiny ring-arc |
| | | `last` | at the last | one punch |
| | | `slow` | slowly | a tiny S along the ring, ±0.3 B |
| | | `gently` | gently | a tiny cup opening outward, ±0.3 B |
| | | `>` [v1] | make it do; send | the chevron at the foot pointing in |

- **At most one mark per station**, so at most three fringe marks on a sign. Count and ordinal bites are on the cut itself and do not use a station.
- **Descent.** The fringe is the Tally (\*kail-, notches cut to keep a count) grown round the sign:
  - *only* is the Lone Mark small;
  - *still* is the Bed small;
  - *at last* is the End, reduced to its point;
  - *gently* is the Cup;
  - *slowly* is the Curl drawn out.
- **Not Ogham** (§15). The fringe sits beside or under one sign, never along a stem-line, and never as a run of parallel strokes: *all* is a single line, and counts stop at four [v1].

![the devices on chips](grain2/figs/v2_devices.png)

*`wf7/grain2/figs/v2_devices.png` (`specimens.py`): each v2 device alone on a chip of end-grain. It shows the runner roles by their ends, pass and break, three braids, the bind, both pockets, years and cells, five parts, the kind-arc and the eleven fringe marks. The chips are drawn at the same scale as the sign chart, where terminals are small; the ring plates of §11.5 are the reading size.*

---

## 6 · RUNNERS: THE LIVING BRANCH-LINES

### 6.1 What a runner is, and how its ends are read [rule]

- **A runner is a narrow living cut** that springs from the **head** of the sign that governs, and grows through the wood to the sign, file or pocket it governs.
- **It is the Course** (\*trenn-, "a running line"), grown from a Stem's head by G4. Like the wood's roots, it runs with the grain and crosses the rings where it must: the Aelralen, "the bond of roots", made small.
- **It is cut, not drawn.**
  - It is a V-cut with two facets, like every mark (§3.11).
  - Its half-width is 1.35 units at its node, tapering to 0.45 at its terminal.
  - At the node it swells to 1.9 over the first 2.2 units: a small bud where it springs.
- **The thick end is the source** [v1, for ties]. The taper gives the direction; it is not weight, which still carries nothing.
- **Hidden and seeming.** A runner may be cut *smoothed* (`_`: a hidden relation, felt and not seen) or *hollow* (`~`: a seeming relation, shown and not meant), exactly as a mark may.

**The ten roles.** Each role is read by its **terminal** (the shape of the end), and confirmed by **where it lands**. Terminal sizes are in units, about three runner-widths, so that they read at the plate scale (§11.5).

| Role | GN | Means (Seilrhass small word it replaces) | Lands on | Terminal | From the first mark |
|---|---|---|---|---|---|
| **to** | `→` | does it to; goes to (the done-to, the goal: *na*) | the target's **head**, stopping a knife-width short | plain taper | the Stem |
| **then** | `⇒` | when this, then that; from this (*thes*; v1's cross-ring tie) | the target's **foot** | plain taper, arriving from below | the Stem |
| **in** | `→in` | in, at, on, among (*li*) | the head | a **cup**, radius 5.2, opening toward the target | the Cup (\*tum-) |
| **with** | `→with` | with; by means of; together with (*si*) | the target's **flank**, which it grows into and touches | **merge**: the only runner that touches its target | the Bond (\*ol) |
| **for** | `→for` | for, so that, for the sake of (*vi*) | the head | a **bud**: a pointed lens 10 × 4.6 | the Bough, the Sprout |
| **because** | `→bc` | because of; for this reason: that (*rhi*) | the head | **root-hairs**: three uneven hairs, 6.6 / 5.0 / 6.0 at −40°, −4°, +28° | the Roots (\*ral-) |
| **as** | `→as` | as, like; than (with *more*: *vaere*) | the head | **two level bars** across the end, 8.4 wide, 3.4 apart | the Still (\*waʔr-): still water, a reflection |
| **through** | `→thru` | through, past, by way of (*thi*) | straddles the head | **two tines** 7.2 long at ±30°, one either side of the target | the Split (\*krask-) |
| **that** | `→that` | the content of saying, knowing, carving, believing | a **pocket's mouth** (§8) | none: it ends a unit inside the mouth | the Gap (\*onn-) |
| **blind** | `→bc ∅` | there was a cause, and the wood does not hold it: "we do not know why" | nothing: **empty wood** at least 6 units from any mark | an **empty cup** | the Cup, empty |

- **The file referent.** A runner of role *to* (or *in*) whose target is written `@f` ends in the empty cell of file f, in its own year: "to that file's one". This is v1's rule that "a tie that ends on a file where nothing is cut ties to that file's bearing", extended from places to all referents. **The file is the pronoun.** The grain needs no sign for *us* in every knowing; it points at file 12.
- **Split runners.** A runner may fork **once**, at one point, into two or three shoots of the same role, going to several targets: "what one pillar felt, all the ranks felt". A shoot never forks again (§15, Nomai).
- **The blind is what "Fear leaves no mark on wood" means.** The canon's own line becomes a rule: **the grain has no sign for a shore-man's fear**. Where the host's fear stood, the wood cuts only the empty cup. Halyna's telling glosses it: "We do not know why. Fear leaves no mark on wood."
- **v1 hairlines stay hairlines.** The ray (the same one), the memory ray (remembered, to the pith) and the grain-arc (in names) are unchanged. They pass *under* runners (§7.1).

### 6.2 How a runner is grown (the router) [rule]

The route is the renderer's, fixed by the seed. **The meaning is in the endpoints, the terminal and the crossings, never in the path's shape.** A decoder never reads a route for meaning; it only traces it. The rule below makes every route deterministic, grain-following and clear of the marks.

1. **Order.**
   - Runners are grown in canonical order (§13.4).
   - Exceptions: a runner that a declared break will cross is grown **before** its breaker, and the second strand of a braid is not grown at all (§7.2).
2. **Ends.**
   - The start is 3 units above the source's head, offset 0.25·B toward the target's side.
   - The goal is the landing point of the role (§6.1): the head + 3, the foot − 3.4, or the flank + 3.5.
3. **Lattice.**
   - An A* search runs on a polar lattice of 1.6-unit cells, inside a window.
   - The window is the arc between the ends ± 90 units, and the radii between them ± 70.
   - A runner may only enter the rings between its source's and its target's.
4. **Walls.**
   - A cell is closed if it lies within **3.2 units of any mark's ink** (its own two marks excepted), within 18 units of the bark's inner line, or within 12 of the pith.
   - **No step may cross a ring line inward.** Only memory runs inward [v1]; inside one ring, a runner may go either way.
5. **Cost.** Each step costs its length × (1 + 0.7 × its radial fraction), so across the grain costs 1.7 times along it. On top of that:
   - +5 for each ring line crossed;
   - +3 within 2.6 units of another runner, and +0.6 within 5.2, so runners keep apart, and cross when they must, instead of running in bundles;
   - +0.35 for each change of direction.
6. **String-pulling.** From the lattice path, keep a point only where the run from the last kept point would come within 3.2 of a mark or cross a ring line inward. The run is straight **in (θ, ρ)**, checked every 1.5 units.
   - A straight run in (θ, ρ) is a gentle **drift across the grain**, like a root that climbs the rings as it goes. It is never a chord, and never a 45° jog (§1.2).
7. **Curve.**
   - Fit a Catmull-Rom curve in (θ, ρ) through the kept points, then smooth it with one Chaikin pass.
   - Add a seeded **meander**: amplitude 0.55 across the line, wavelength 26–38 units, tapering to nothing over 6 units at each end. The stream is `id/runner/<rid>/meander`.
8. **Failure.** If no way is found, the validator fails the round, and the GN or the files must change. (The prototype still fails 3 of IV.6's 64 runners, in the crowded ring 7. A production router must widen its window before giving up.)

**Why these numbers.**
- With GRAIN = 1.7, a runner takes a long way round along a ring before a short climb across it. That is the look of roots in layered soil, and of figure in wood.
- The 3-unit runner repulsion breaks the bundles that read as circuit traces.
- The window stops a runner wandering the round.

### 6.3 Composition rules for runners [rule]

1. **Prefer the file referent** (`@f`) to a runner that crosses years to reach a repeated sign. The grain has no pronouns, and it needs none: the file is the pronoun.
2. **A runner stays within its ring when it can.** Across rings it runs only outward, as *then* (or *to* into a later ring's knowing).
3. **Two runners of the same role, from one mark to one target, are one runner.** A mark may send any number of runners of different roles.
4. **Runners never pass through a pocket.** A pocket closes its gates in its year (§8).
5. **A runner has at most one fork, at most three shoots**, and at most 300° of total turning. It has no loop.

### 6.4 Rays, memory and ties, in v2 [v1, restated]

| v1 | v2 |
|---|---|
| `tie a.rk → b.rk` (within a ring: this one does it to that one) | `run … → …`, role **to** |
| `tie a.ri → b.rj`, i < j (when or because this, then that) | `run … ⇒ …`, role **then** |
| a tie ending on an empty file (a bearing, a place) | `→ @f` (a file referent, place or person) |
| `ray s: ri–rj` (the same one) | unchanged; a hairline that passes under runners |
| `mem s: rk → pith` | unchanged |

### 6.5 Where the small words went (note 1)

Seilrhass joins its words with small words, and the grain never cut one. v1 had only two relation-lines. v2's runners, crossings and knots give the grain its whole grammar of relation, as the chisel's economy asks, without a single small word:

| Seilrhass | What it does | In the grain v2 |
|---|---|---|
| *na* to · *li* in, at · *si* with · *vi* for · *thi* through · *rhi* from, because | case and relation | runner roles (§6.1). "From" is simply the source end |
| *thes* then · *anth* when (clause-final) · *eir* until | time between clauses | *then* runners; the span `^` [v1] |
| *sei* if | condition | the fork [v1] |
| *ei* and | joining | nothing: marks in one ring are together [v1]. For *both, bound*: the bind (§7.3) |
| *vaere* like, as | likeness | the *as* runner, to a hollow likeness (§10) |
| *ni* not · *lae* (question) | negation, asking | the mirror and the unfinished head [v1] |
| *ra* this (the held one) · *re* that | pointing | the file referent (@) and the ray |
| the knock | — | nothing: the grain is soft |

---

## 7 · CROSSINGS: PASS, BREAK, BRAID, BIND

At every crossing of two runners, one is cut through (**over**) and the other is broken on both sides (**under**). The gap in the under-strand is the over-strand's half-width + 1.5 on each side, and the under-strand's cut ends are blunted to 0.55 of its width. **Every crossing means something.** Its kind is read from the under-strand's ends and from what the strands are doing.

This is the Upon (\*um-, "upon; seen from below, beneath"), the one first mark that was already about over and under. The wood kept it as BENEATH (senn), and v2 makes it the grammar of every crossing.

### 7.1 Pass and break [rule]

| Kind | Drawn | Means | Over is |
|---|---|---|---|
| **pass** | clean ends | the two relations both hold. The later lies upon the earlier, as later growth lies upon earlier wood: "the outer ring speaks last" [v1 G2] | the runner **later in canonical order**: its source's ring, then year, then file clockwise, then cell, then GN order. A decoder can check it, and must |
| **break** | each cut end of the under-strand **splinters** into two tines, 2.8 long at −40° and +36° | the over-strand **thwarts** the under-strand: prevails over it, cuts it off, turns it back | the thwarting runner, earlier or later |

- **A break is declared** in GN: `lap e1 ⊳ f1`.
- **The router makes it happen** (§6.2). The thwarted runner is grown first. The thwarting runner is then grown through two points 6 units either side of the thwarted runner's midpoint, so that it **crosses square, exactly once**.
- **A pass is never declared.** It happens wherever two routes cross, and it carries its fixed reading.
- **Crossing angles.** Every crossing is at 15° or more. The router's repulsion and the square rule make shallow crossings rare, and the validator rejects any below 15°.
- **Hairlines.** Runners cross over rays and memory rays, with a gap in the hairline. That is always a pass: the same one, or the memory, still holds beneath.

**In the tellings.**
- IV.6, ring 5: "We turned against the current" is `lap e1 ⊳ f1`. Our turning, going home, breaks the current's taking.
- V.4: "the vote was carried by the weight of anger and grief" is the young's runner breaking the elders' plea.
- IV.4: "the host drew back … the blade … went deep" is the drawing back breaking the rite's shallow cut.

### 7.2 Braids [rule]

- **What a braid is.** Two or three runners that share a stretch of one cord and **plait along it**, crossing at a steady pitch.
- **What it means.** One relation held **by turns**: each to the other, or all three holding one another. The over-strand at each crossing is **whose turn it is**, read in order along the cord from the first strand's source.

| Pattern | Means | In the tellings |
|---|---|---|
| `abab…` (2 strands, alternating) | by turns; each to the other; the one and then the other | II.2: "we tended the wood, and the wood kept us"; IV.2: "The iron came back for the young ones. We put up more. It came again." |
| `aaaa…` | the one prevails at every turn | V.4: the elders' counsel of patience against the young's grief, turn after turn ("and counselled patience still"), until the young break it |
| `abcabc…` (3 strands, the standard plait) | these three, each holding the others | II.2: "The wood needed the breath, the breath needed the wood, and we needed both" |
| `…!` | the **last** crossing is a break: at the last turn, the one over thwarts the other | IV.6: "the fire went out of us slowly as the grey closed over" is `abab!`: fire and grey by turns, until the grey. IV.2: "At the last the stumps put up nothing" |

**Geometry.**
- **The first strand is grown** (§6.2). The second (and third) take its line as a **cord**.
- **The braid's stretch** is (N + 1) × 12 units, centred on the cord's middle, where N is the number of crossings, the pattern's length.
- **Two strands.**
  - Outside the stretch, they run ±2.2 either side of the cord.
  - Inside it, they lie at ±2.9 × sin(π(N + 1)q), blended over 10% at each end.
  - That gives **exactly N crossings**, at q = m/(N + 1), m = 1…N.
- **Three strands** (the plait).
  - Outside the stretch, they run in three lanes, at −2.6, 0 and +2.6.
  - At each of the N steps (one every 12 units), an outer strand crosses into the middle lane and the middle strand moves out to that side, alternately from the counter-clockwise and the clockwise side, with the moves eased over the step.
  - **Each step is one crossing**, so there are again exactly N.
- **Each strand ends on its own target.** The second strand of a mutual braid runs the cord backward, so "each to the other" lands both ways.
- **Room.** The cord needs 5 units clear either side along its stretch. The router gives a braid's first strand that room (+5 on the clearance).
- **Validator.** The braid has exactly N crossings in its stretch, and the over-strands match the pattern.

### 7.3 Binds (knots where meanings bind) [rule]

- **What a bind is.** Two runners meet head-on, and **each hooks through the other**.
- **What it means.** The two relations are **bound into one**: each holds only with the other.
  - "Harm to one is harm to both."
  - "One life, in two kinds."
  - A promise; a rite's joining.
- **Out-runner.** A bind may send out **one** runner, of role *then* or *to*: what the bound pair together does or leads to. The Aelthar rite's r6 in v2 (§17): the two WOUND runners bound, and the bind's out-runner to BOND.
- **Three strands.** x and y lock, then the lock's out-strand locks with z. This is never a three-fold rotational figure (§15).

**Geometry.** In the site's local frame, x runs along the ring and y outward.
- **The site** is a free point between the two sources, at their mean angle, in the outer source's year. The strands arrive **from opposite sides** along the ring.
- **Strand x** comes in along y = −4 to x = +4, hooks round (radius 3) to y = +2, and goes back to x = −9.
- **Strand y** comes in along y = +4 to x = −4, hooks round to y = −2, and goes back to x = +9.
- **The two hooks cross twice**: x is over where x's hook crosses y's arm (x > 0), and y is over where y's hook crosses x's arm (x < 0). Each is through the other, and **the eye** is the small closed space between them.
- **The out-runner** leaves from (0, +8.5).
- **Room.** A year holding a bind is 5 units deeper.

**Distinct from the signs.**
- **BOND** (*ael*, "bind; join; together") is a *sign*, two cuts that grow into one: the word.
- **AELTHAR** is the rite's name-sign.
- **The bind** is grammar: two relations bound.
- A bind is never a sign, and a sign is never drawn as a lock.

---

## 8 · POCKETS: A KNOWING INSIDE A KNOWING (THE RING-SPLIT) [rule]

A **pocket** is a lens-shaped hollow in a year, whose lines part round it, holding a knowing that another knowing *contains*. It is real anatomy: a **resin pocket** or a **bark pocket** between the rings, round which the grain splits and rejoins.

| Kind | GN | Border | Holds | In the tellings |
|---|---|---|---|---|
| **said** (resin pocket) | `pocket P said s0–s1 { … }` | a smooth **double** line: 0.9 wide at 62%, and 0.7 at 34% set 1.25 inside it | words said, sung, asked, believed, named: the content of MOUTH, HEAR, SING, NAME, HOLD, TRUE+HOLD (believe) | V.4: the elders' "Send another. Learn their words." and the young's answer; IV.4: *Stop. Sky. Dying.*; II.2: "You called it the fog…"; V.6: the Song of the Years |
| **cut** (bark pocket) | `pocket P cut s0–s1 { … }` | a **jagged** line (±0.9), included bark's own texture [v1] | a carving: an order, a judgement, an older knowing, cited whole, or by its root cut half size (v1's chain) | III.2: each Throne's "Our judgement was …"; V.3: "Then an older carving woke in us … *Home when wounded*" is `{ STERN½ }`; V.4: "*Grow until the shore is silent*"; IV.6: what the keel held of IV.4 |

- **Its place.**
  - A pocket spans files s0 to s1 clockwise, at most six. Its tips lie on the half-file lines s0 − ½ and s1 + ½.
  - It takes its year's whole mark band (§4.3), and its thickness goes as sin(πq).
  - Its year is 8 units deeper.
  - **The year's lines bow away from it**, 2.2 inward and 1.6 outward: the ring-split.
- **The mouth.** A 3.2-unit gap in the border at the tip facing its governing runner. The *that* runner ends one unit inside it. A pocket has exactly one *that* runner.
- **Its contents.**
  - Up to eight items, laid clockwise along its midline at equal spacing: the pocket's own reading order.
  - They are cut with the finer knife (H × 0.62), at B = min(16, 0.36 × the pocket's arc / n, 0.9 × its half-thickness).
  - They may carry runners among themselves, at the same scale, inside the pocket.
  - A pocket may hold one pocket: depth 2 at most.
- **A whole round cited.** When the cited knowing is itself a whole round (IV.4's ring 15 cites the gift's sentence, `mystaeri_spec.md` §5.4), the cut-pocket holds that round's **root, half size**, and the Book draws the cited round beside it, as v1 already does.
- **Pockets close their gates.** No runner passes through one (§6.3).
- **Descent.** From the Gap (\*onn-, the between) and the Mouth (the said pocket's mouth). The jagged border is included bark [v1].

---

## 9 · THE INVENTORY v2: 70 + 47 SIGNS

### 9.1 How the new signs were made [rule]

- **Only where needed.** A new sign was added only where a concept of the eight wood leaves needed a Seilrhass **root**. Everything else is a **ligature**, exactly as Seilrhass builds its compounds (§18):
  - *timber* is AXE+WOOD (*rhithveir*);
  - *the council* is SILVERBARK×3 (*neivathen*);
  - *to learn* is NEW+HOLD (*leathein*);
  - *to believe* is TRUE+HOLD ("hold true");
  - *to hope* is MORROW+HOLD (*leisthein*);
  - *a guest* is BOND+US (*aelea*);
  - *a host* is DOOR+STONEFOLK (*vethea*);
  - *a lie* is SQUARE+CARVE (*rhenseth*, "a cut that carries nothing");
  - *war* is STRIKE×3.
  Parts come from the part device (§5.2), not from new signs.
- **Every new sign grows from the First Tongue's marks** by the wood's laws (`ancestor.md` §5.3): G1 (on a file), G2 (the knife bows and tapers), G4 (signs grow new signs), G7 (straight for stone, curved for wood). Most belong to a **family** grown from a v1 sign, so a reader who knows the head of the family can guess its members:
  - the MOUTH family: MOUTH, HEAR, SING, CRY, LAUGH, EAT;
  - the EYE family: EYE, WEEP, FIND;
  - the HAND family: HAND, TAKE, LOSE;
  - the Cup family: HOLD, NAME, TEND, HOLY, CLOSE, OPEN;
  - the HEART family: HEART, ANGER, SHAME, GLAD;
  - the Bed family: DEEP, EARTH, SAND, MOSS;
  - the Star family: FLASH, SOFTLIGHT, MORNING, DUSK, SUMMER.
- **Every soft reading is a Seilrhass word that already exists.** 21 are in the lexicon (`wf6/lang/lexicon.tsv`). 26 are reserve roots whose forms `ancestor.md` §3.3 computed by the sound laws; none is coined here. Two reserve homophones are allowed by that table's own rule:
  - *rhaenel* is both "shame" and "weave"; the grain signs only shame;
  - *rhenn* "follow" sits beside *rhen* "stone" and *renn* "mouth", with different consonants.
- **The originality principle of v1 §3.13 was applied to every one** ("a stave with straight branches, or two straight strokes meeting, must bow, stagger or break them"). So was a new check against Latin letters, digits, Hebrew and Greek letters, and interface icons (§9.4).

### 9.2 The 47 new signs

`L` means in the lexicon; `R` means a reserve root (`ancestor.md` §3.3). The **Chiral** column says whether the sign already differs from its mirror; a sign that does not carries the entry-nick [v1 §3.4].

**The ground, the growing and the weather** (the Bed, the Bough, the Drop, the Stem)

| Id | Soft reading | Means | From the first marks · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **WOOD** | *veir* L | wood, the living stuff; boards; (with AXE) timber | a length of the Bough sawn at both ends by the Bar: a billet · G4 | a lens with a short ring-arc across each tip | nick |
| **BARK** | *vath* L | bark; a skin | the Bar (a smooth cambium line) and the Split laid along it (rough plates) · G1 G4 | a ring-arc, and above it a jagged cut along the ring | nick |
| **LEAF** | *lel* L | a leaf | the Bough on the Stem: stalk and midrib · G4 | a lens with a cut running from below it up through its middle | nick |
| **SAP** | *raess* L | sap; what the wood lives by | the Stem and the Drop, thrice, alternating · G4 | a fine cut with three small drops beside it, alternately, points outward | nick |
| **EARTH** | *reth* L | earth, ground, the land | the Bed and the Roots hanging from it · G4 | a ring-arc with three uneven root-hairs hanging inward from it | nick |
| **SAND** | *resser* R | sand; a waste of sand; (with SHORE) the shingle | the Bed and grains · G4 | a low ring-arc with five punches above it | nick |
| **DUST** | *theiss* R | dust | the Fade crumbled to grains, with no bed · G2 | seven punches in a loose lens-shaped cloud | nick |
| **MOSS** | *rheth* R | moss; the forest floor | the Bed and four small Boughs: soft cushions · G4 | a low ring-arc with four small lenses on it | nick |
| **RAIN** | *nith* L | rain | the Drop, thrice, falling · G1 | three small drops on a slant, points outward | nick |
| **WIND** | *reas* L | wind | the Bough bent as air bends it: a gust and its eddy · G2 | a long S-bowed cut, and a short bowed cut beside its middle bowing the other way | yes |
| **SILVERBARK** | *neivath* L (compound) | a silverbark; a silver elder; (×3) the council | TREE and the Star at each bough's tip · G4 | the v1 TREE, its two boughs ending in small star-notches | yes |

**Light and time** (the Star, the Rim, the Sprout)

| Id | Soft reading | Means | From · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **SOFTLIGHT** | *neis* L | soft light; (inside the MIST band) the between-light (*naelneis*) | the Star held in a Bough: light within the breath · G4 | a broad lens with a star-notch at its centre | nick |
| **MORNING** | *res* R | morning; dawn | the Rim with the Star beyond it: light over the rim · G4 | a ring-arc low in the space, a star-notch above it | nick |
| **DUSK** | *ath* R | dusk; evening | the Rim with the Star within it: light under the rim · G4 | a ring-arc high in the space, a star-notch below it | nick |
| **SUMMER** | *ses* R | summer; (#1) one season | TIDE and the Star: the sun's growing · G4 | TIDE's arc and shoot, the shoot ending in a star-notch | nick |
| **MORROW** | *leis* L | the morrow; the next coming (HOPE is MORROW+HOLD) | an empty ring cut small: a piece of the next ring, closed and empty · G5 | a closed rounded band lying along the ring, empty | nick |

**The mouth, the eye, the hand and the cup** (families of v1 signs, G4)

| Id | Soft reading | Means | From · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **HEAR** | *seinn* L | hear; heed; obey; listen | MOUTH turned toward the heart: a mouth that takes in · G4 | MOUTH's open lens joined at the **head** and parted at the foot | nick |
| **SING** | *neira* L | sing; a song | MOUTH and the Curl rising out of it · G4 | a short MOUTH, and from its opening a cut that rises and curls 160° | nick |
| **CRY** | *thaes* R | cry out; scream; groan | MOUTH torn wide, and the Split below it · G4 | a wide MOUTH, and a check running inward from its foot | nick |
| **LAUGH** | *thevel* R | laugh | MOUTH with its lips broken, again and again · G4 | MOUTH's two arms, each cut in two pieces with a gap | nick |
| **EAT** | *nass* R | eat; drink; feed on; (causative `>EAT`) feed | MOUTH with a morsel in it · G4 | MOUTH, with a small solid lens inside its opening | nick |
| **WEEP** | *sann* R | weep; a tear | EYE and the Drop falling from it · G4 | EYE, with a small drop below its foot on the clockwise side, point in | nick |
| **FIND** | *veass* R | find; come upon | EYE with a grain in it: a thing seen and had · G4 | EYE, with a punch in the lens | nick |
| **TAKE** | *rhiss* L | take; seize; (#, ×3) gather | HAND whose clockwise finger closes over a thing held · G4 | HAND's stem; the palm's clockwise arm curls over a small solid lens | yes |
| **LOSE** | *naenn* R | lose; let slip | HAND with its clockwise finger gone, and what it held fallen beside it · G4 | HAND's stem and one arm; a small solid lens beside it on the open side | yes |
| **NAME** | *eis* L | a name; to name, to call | the Cup holding a Bough: what the seal holds · G4 | HOLD's cup ( ) with a lens groove inside it | nick |
| **TEND** | *vaeth* R | tend; care for | the Cup round a Sprout · G4 | HOLD's cup with a small shoot and one leaf inside it | nick |
| **HOLY** | *veness* R | holy; set apart; sacred | the Cup round the heart: the heart held apart · G4 | HOLD's cup with HEART (a solid lens) inside it | nick |

**The heart** (feelings, from v1 HEART, the small solid lens; G4)

| Id | Soft reading | Means | What is cut | Chiral |
|---|---|---|---|---|
| **ANGER** | *rhes* L | anger; hot | HEART with a star-notch above it: a heart that flashes | nick |
| **SHAME** | *rhaenel* R | shame; our fault | HEART under a laid ring-arc: a heart covered | nick |
| **GLAD** | *seiness* R | gladness; glad, content | HEART putting up a bowed shoot | nick |

There is **no sign for fear**. The wood holds the dread, the DREAD band, "the place where wood dies", but it never held a shore-man's fear: "fear leaves no mark on wood". Where the telling says it, the grain cuts the blind (§6.1).

**The body, the beast, the mind and the word**

| Id | Soft reading | Means | From · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **BONE** | *ther* R | a bone; (×3, of a hull) its ribs | the Stem knobbed at both ends · G4 | a short straight cut with two small lenses at each end | nick |
| **BEAST** | *rhaenth* R | a beast (and the shore's beast-names for the Thrones) | a Bough with a toothed side: a thing with teeth · G4 | a half-lens closed by a zigzag edge on its clockwise side | nick |
| **MIND** | *rener* R | the mind; thought; to think | a Bough holding seeds: a pod of thoughts · G4 | a lens with three punches in it | nick |
| **WORD** | *ranth* L | a word: "a spoken thing, which can break" | a small Bough broken across by the Split · G4 | a lens crossed at its middle by a zigzag crack | nick |

**Acts of the body** (the Stem and its folds)

| Id | Soft reading | Means | From · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **CARRY** | *var* L (canon, in *varen*) | carry; bear (the act of BEARER) | the Bearer: a leaning prop under a load laid across its head · G4 | a bowed cut leaning across the file, and a lens lying along the ring on its head | nick |
| **SIT** | *rass* R | sit; take one's seat | the Stem folded at the hip onto a seat, above the ground · G2 | a stem folding at 0.62 into a seat along the ring, then down; a short ring-arc (the ground) below the shin | yes |
| **LIE** | *rhir* R | lie down; lie; sleep; (`>LIE`) lay down | US laid along the ground · G1 | a ring-arc low in the space, with a lens lying across at its clockwise end | nick |
| **GUIDE** | *leser* R | guide; lead; show the way | TURN, and a second stroke turning with it · G4 | two kinked cuts, the shorter inside the longer, turning together | yes |
| **CHOOSE** | *neiler* R | choose; (of a council) vote | RISE, with the one not chosen set apart · G4 | a cut ending in a lens, and a small lens apart on the counter-clockwise side | yes |
| **FOLLOW** | *rhenn* R | follow; come after; (with SWIFT) chase | the Lone Mark turned end for end: the short cut behind and beside the long one · G4 | a short cut low on the clockwise side, and a long cut above it, overlapping it a little | yes |
| **OVER** | *laes* L | over, above; high: "the Upon read from above" | the Upon (\*um-) · G1 G3 | a floor-bar at the foot, and a cut above it that does not touch it: BENEATH turned end for end | nick |

**Made things** (straight means of stone, G7)

| Id | Soft reading | Means | What is cut | Chiral |
|---|---|---|---|---|
| **HOUSE** | *ennas* L (compound) | a house; a dwelling; (GREAT+) a hall | a straight square opened by a doorway in its head side | nick |
| **CHEST** | *vesel* R | a chest; a box of stone (the Stonewrights' chest) | a straight square, with a laid bar above it: the lid | nick |
| **BRIDGE** | *eissel* R | a bridge; a span; a beam laid across | a bowed span over a low ring-arc; open strokes, so not classified | nick |

**Qualities**

| Id | Soft reading | Means | From · law | What is cut | Chiral |
|---|---|---|---|---|---|
| **NEW** | *lea* L (canon) | new; young; green. Parts: `NEW:stump` a stump, `NEW:shoot` a shoot (*rheann*) | the Sprout rising from a cut stump · G4: the Blackthorn's own heart, "the last shoot of a stump" | a short thick stump capped by a bar, and a thin curved shoot rising from beside its top, with a bud | yes |
| **TRUE** | *eiss* L | true; so; what is; straight, as a plumb | the Stem standing true between a bed and a small stone: a plumb-line · G7 | a straight cut from a small floor-bar up to a small square | nick |

**Withdrawn in the look check: COME.** Every drawing of COME ("a way that enters its file from the side") read as the **mirror of FALL**. Mirror is the grain's *not*, so a reader would have seen "not falling". The grain therefore has no *come*: it cuts **GO toward the one it comes to**, `GO → @f`. "The iron came" is AXE+GO → @12; "it came again" is GO{again} → @12. Seilrhass *sae* stays a spoken word only.

### 9.3 The inventory as data (the exact parameters the prototype drew)

Local frame as §3.4 [v1]. `punch` and `lens.across` are §5.1's new elements.

```json
{
 "WOOD": {"cls":"thing","soft":"veir","nick":true,"els":[{"t":"lens","c":[0.52,0],"len":0.76,"w":0.34},{"t":"ringarc","u":0.24,"v0":-0.46,"v1":0.46},{"t":"ringarc","u":0.8,"v0":-0.46,"v1":0.46}]},
 "BARK": {"cls":"thing","soft":"vath","nick":true,"els":[{"t":"ringarc","u":0.34,"v0":-0.72,"v1":0.72},{"t":"cut","p":[[0.58,-0.8],[0.72,-0.6],[0.62,-0.34],[0.66,-0.1],[0.56,0.06],[0.74,0.3],[0.6,0.5],[0.66,0.8]],"straight":true}]},
 "LEAF": {"cls":"thing","soft":"lel","nick":true,"els":[{"t":"lens","c":[0.6,0],"len":0.64,"w":0.36},{"t":"cut","p":[[0.1,0],[0.8,0]]}]},
 "SAP": {"cls":"thing","soft":"raess","nick":true,"els":[{"t":"cut","p":[[0.06,0],[0.94,0]],"k":0.8},{"t":"drop","c":[0.3,0.36],"len":0.16,"w":0.16,"point":"out"},{"t":"drop","c":[0.52,-0.36],"len":0.16,"w":0.16,"point":"out"},{"t":"drop","c":[0.74,0.36],"len":0.16,"w":0.16,"point":"out"}]},
 "EARTH": {"cls":"thing","soft":"reth","nick":true,"els":[{"t":"ringarc","u":0.5,"v0":-0.86,"v1":0.86},{"t":"cut","p":[[0.5,-0.46],[0.34,-0.74],[0.18,-0.96]],"curve":true,"k":0.6},{"t":"cut","p":[[0.5,0.06],[0.36,0.1],[0.3,0.04]],"curve":true,"k":0.6},{"t":"cut","p":[[0.5,0.44],[0.34,0.52],[0.2,0.76]],"curve":true,"k":0.6}]},
 "SAND": {"cls":"thing","soft":"resser","nick":true,"els":[{"t":"ringarc","u":0.28,"v0":-0.82,"v1":0.82},{"t":"punch","c":[0.48,-0.56],"r":0.1},{"t":"punch","c":[0.62,-0.18],"r":0.1},{"t":"punch","c":[0.46,0.16],"r":0.1},{"t":"punch","c":[0.66,0.5],"r":0.1},{"t":"punch","c":[0.82,0.02],"r":0.1}]},
 "DUST": {"cls":"thing","soft":"theiss","nick":true,"els":[{"t":"punch","c":[0.3,-0.2],"r":0.08},{"t":"punch","c":[0.42,0.3],"r":0.08},{"t":"punch","c":[0.52,-0.42],"r":0.08},{"t":"punch","c":[0.58,0.06],"r":0.08},{"t":"punch","c":[0.7,0.42],"r":0.08},{"t":"punch","c":[0.76,-0.2],"r":0.08},{"t":"punch","c":[0.88,0.14],"r":0.08}]},
 "MOSS": {"cls":"thing","soft":"rheth","nick":true,"els":[{"t":"ringarc","u":0.3,"v0":-0.84,"v1":0.84},{"t":"lens","c":[0.46,-0.56],"len":0.2,"w":0.17},{"t":"lens","c":[0.5,-0.16],"len":0.26,"w":0.17},{"t":"lens","c":[0.47,0.24],"len":0.22,"w":0.17},{"t":"lens","c":[0.45,0.6],"len":0.18,"w":0.16}]},
 "RAIN": {"cls":"thing","soft":"nith","nick":true,"els":[{"t":"drop","c":[0.76,-0.5],"len":0.2,"w":0.17,"point":"out"},{"t":"drop","c":[0.52,0.02],"len":0.2,"w":0.17,"point":"out"},{"t":"drop","c":[0.28,0.52],"len":0.2,"w":0.17,"point":"out"}]},
 "WIND": {"cls":"thing","soft":"reas","els":[{"t":"cut","p":[[0.06,-0.1],[0.36,-0.46],[0.7,-0.36],[0.94,0.1]],"curve":true},{"t":"cut","p":[[0.34,0.3],[0.56,0.12],[0.8,0.34]],"curve":true,"k":0.8}]},
 "SOFTLIGHT": {"cls":"thing","soft":"neis","nick":true,"els":[{"t":"lens","c":[0.52,0],"len":0.7,"w":0.5},{"t":"star","c":[0.52,0],"r":0.26}]},
 "MORNING": {"cls":"thing","soft":"res","nick":true,"els":[{"t":"ringarc","u":0.36,"v0":-0.86,"v1":0.86},{"t":"star","c":[0.7,0],"r":0.3}]},
 "DUSK": {"cls":"thing","soft":"ath","nick":true,"els":[{"t":"ringarc","u":0.7,"v0":-0.86,"v1":0.86},{"t":"star","c":[0.36,0],"r":0.3}]},
 "SUMMER": {"cls":"thing","soft":"ses","nick":true,"els":[{"t":"ringarc","u":0.24,"v0":-0.8,"v1":0.8},{"t":"cut","p":[[0.24,0],[0.66,0]],"bend":0.06},{"t":"star","c":[0.84,0],"r":0.26}]},
 "MORROW": {"cls":"thing","soft":"leis","nick":true,"els":[{"t":"cut","p":[[0.3,-0.56],[0.3,0.56],[0.5,0.72],[0.72,0.56],[0.72,-0.56],[0.5,-0.72],[0.3,-0.56]],"curve":true}]},
 "SILVERBARK": {"cls":"thing","soft":"neivath","els":[{"t":"cut","p":[[0.04,0],[0.95,0]]},{"t":"cut","p":[[0.44,0],[0.7,0.46]],"bend":0.1},{"t":"cut","p":[[0.62,0],[0.84,-0.4]],"bend":-0.08},{"t":"star","c":[0.76,0.54],"r":0.16},{"t":"star","c":[0.9,-0.47],"r":0.16}]},
 "BEAST": {"cls":"thing","soft":"rhaenth","nick":true,"els":[{"t":"cut","p":[[0.18,0],[0.44,-0.46],[0.74,-0.4],[0.88,0]],"curve":true},{"t":"cut","p":[[0.88,0],[0.78,0.24],[0.7,0.1],[0.6,0.32],[0.5,0.14],[0.4,0.34],[0.3,0.12],[0.18,0]],"straight":true}]},
 "BONE": {"cls":"thing","soft":"ther","nick":true,"els":[{"t":"cut","p":[[0.26,0],[0.74,0]],"straight":true},{"t":"lens","c":[0.17,-0.18],"len":0.14,"w":0.18},{"t":"lens","c":[0.17,0.18],"len":0.14,"w":0.18},{"t":"lens","c":[0.83,-0.18],"len":0.14,"w":0.18},{"t":"lens","c":[0.83,0.18],"len":0.14,"w":0.18}]},
 "NAME": {"cls":"thing","soft":"eis","nick":true,"els":[{"t":"cup","c":[0.54,0],"r":0.58,"form":"hold"},{"t":"lens","c":[0.54,0],"len":0.3,"w":0.24}]},
 "WORD": {"cls":"thing","soft":"ranth","nick":true,"els":[{"t":"lens","c":[0.52,0],"len":0.52,"w":0.34},{"t":"cut","p":[[0.49,-0.52],[0.55,-0.16],[0.47,0.14],[0.53,0.5]],"straight":true,"k":0.7}]},
 "HEAR": {"cls":"act","soft":"seinn","nick":true,"els":[{"t":"cut","p":[[0.84,0],[0.48,-0.5],[0.14,-0.22]]},{"t":"cut","p":[[0.84,0],[0.48,0.5],[0.14,0.22]]}]},
 "MIND": {"cls":"thing","soft":"rener","nick":true,"els":[{"t":"lens","c":[0.55,0],"len":0.52,"w":0.44},{"t":"punch","c":[0.46,-0.12],"r":0.08},{"t":"punch","c":[0.58,0.14],"r":0.08},{"t":"punch","c":[0.66,-0.1],"r":0.08}]},
 "TAKE": {"cls":"act","soft":"rhiss","nick":false,"els":[{"t":"cut","p":[[0.06,0],[0.54,0]]},{"t":"cut","p":[[0.54,0],[0.64,-0.5],[0.8,-0.62]],"curve":true},{"t":"cut","p":[[0.54,0],[0.66,0.36],[0.84,0.5],[0.9,0.3]],"curve":true},{"t":"lens","c":[0.74,0.28],"len":0.12,"w":0.13,"fill":true}]},
 "CARRY": {"cls":"act","soft":"var","nick":true,"els":[{"t":"cut","p":[[0.06,-0.5],[0.76,0.18]],"bend":0.1},{"t":"lens","c":[0.86,0.26],"len":0.58,"w":0.08,"across":true}]},
 "SING": {"cls":"act","soft":"neira","nick":true,"els":[{"t":"cut","p":[[0.12,0],[0.44,-0.48],[0.74,-0.26]]},{"t":"cut","p":[[0.12,0],[0.44,0.48],[0.74,0.26]]},{"t":"cut","p":[[0.5,0],[0.86,0.04]],"curl":{"r":0.18,"sweep":160,"dir":-1}}]},
 "CRY": {"cls":"act","soft":"thaes","nick":true,"els":[{"t":"cut","p":[[0.26,0],[0.6,-0.74],[0.94,-0.62]]},{"t":"cut","p":[[0.26,0],[0.6,0.74],[0.94,0.62]]},{"t":"check","u0":0.26,"u1":0.04,"v":0,"w":0.2}]},
 "LAUGH": {"cls":"act","soft":"thevel","nick":true,"els":[{"t":"cut","p":[[0.16,0],[0.36,-0.36]]},{"t":"cut","p":[[0.46,-0.46],[0.86,-0.24]]},{"t":"cut","p":[[0.16,0],[0.36,0.36]]},{"t":"cut","p":[[0.46,0.46],[0.86,0.24]]}]},
 "WEEP": {"cls":"act","soft":"sann","nick":true,"els":[{"t":"lens","c":[0.6,0],"len":0.42,"w":0.3},{"t":"cut","p":[[0.3,0],[0.39,0]]},{"t":"cut","p":[[0.81,0],[0.92,0]]},{"t":"drop","c":[0.26,0.4],"len":0.18,"w":0.14,"point":"in"}]},
 "FIND": {"cls":"act","soft":"veass","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.46,"w":0.32},{"t":"cut","p":[[0.1,0],[0.27,0]]},{"t":"cut","p":[[0.73,0],[0.9,0]]},{"t":"punch","c":[0.5,0],"r":0.1}]},
 "LOSE": {"cls":"act","soft":"naenn","nick":false,"els":[{"t":"cut","p":[[0.06,0],[0.54,0]]},{"t":"cut","p":[[0.54,0],[0.66,-0.36],[0.86,-0.44]],"curve":true},{"t":"lens","c":[0.5,0.62],"len":0.14,"w":0.14,"fill":true}]},
 "SIT": {"cls":"act","soft":"rass","els":[{"t":"cut","p":[[0.06,0],[0.62,0],[0.62,0.46],[0.34,0.58]],"straight":true},{"t":"ringarc","u":0.26,"v0":0.22,"v1":0.9}]},
 "LIE": {"cls":"act","soft":"rhir","nick":true,"els":[{"t":"ringarc","u":0.4,"v0":-0.84,"v1":0.5},{"t":"lens","c":[0.46,0.74],"len":0.44,"w":0.1,"across":true}]},
 "EAT": {"cls":"act","soft":"nass","nick":true,"els":[{"t":"cut","p":[[0.16,0],[0.52,-0.5],[0.86,-0.22]]},{"t":"cut","p":[[0.16,0],[0.52,0.5],[0.86,0.22]]},{"t":"lens","c":[0.56,0],"len":0.16,"w":0.14,"fill":true}]},
 "TEND": {"cls":"act","soft":"vaeth","nick":true,"els":[{"t":"cup","c":[0.54,0],"r":0.58,"form":"hold"},{"t":"cut","p":[[0.26,0],[0.72,0]],"k":0.8},{"t":"cut","p":[[0.56,0],[0.68,0.18]],"k":0.6}]},
 "GUIDE": {"cls":"act","soft":"leser","els":[{"t":"cut","p":[[0.06,-0.1],[0.56,-0.1],[0.9,0.62]]},{"t":"cut","p":[[0.3,-0.46],[0.64,-0.46],[0.86,0.02]],"k":0.8}]},
 "CHOOSE": {"cls":"act","soft":"neiler","els":[{"t":"cut","p":[[0.06,0],[0.62,0]]},{"t":"lens","c":[0.77,0],"len":0.28,"w":0.28},{"t":"lens","c":[0.72,-0.72],"len":0.18,"w":0.17}]},
 "FOLLOW": {"cls":"act","soft":"rhenn","els":[{"t":"cut","p":[[0.04,0.56],[0.32,0.56]],"k":0.9},{"t":"cut","p":[[0.26,-0.14],[0.96,-0.14]],"bend":0.06}]},
 "HOUSE": {"cls":"thing","soft":"ennas","q":"straight","nick":true,"els":[{"t":"cut","p":[[0.78,-0.12],[0.78,-0.38],[0.3,-0.38],[0.3,0.38],[0.78,0.38],[0.78,0.12]],"straight":true}]},
 "CHEST": {"cls":"thing","soft":"vesel","q":"straight","nick":true,"els":[{"t":"square","c":[0.46,0],"s":0.72},{"t":"bar","u":0.9,"v0":-0.5,"v1":0.5}]},
 "BRIDGE": {"cls":"thing","soft":"eissel","nick":true,"els":[{"t":"cut","p":[[0.42,-0.86],[0.6,-0.5],[0.66,0.0],[0.6,0.5],[0.42,0.86]],"curve":true},{"t":"ringarc","u":0.2,"v0":-0.6,"v1":0.6}]},
 "OVER": {"cls":"act","soft":"laes","nick":true,"els":[{"t":"ringarc","u":0.1,"v0":-0.72,"v1":0.72},{"t":"cut","p":[[0.34,0],[0.92,0]]}]},
 "NEW": {"cls":"quality","soft":"lea","els":[{"t":"cut","p":[[0.06,-0.12],[0.4,-0.12]],"k":1.0},{"t":"cut","p":[[0.06,0.12],[0.4,0.12]],"k":1.0},{"t":"bar","u":0.42,"v0":-0.36,"v1":0.36},{"t":"cut","p":[[0.42,0.38],[0.62,0.46],[0.9,0.2]],"curve":true,"k":0.85},{"t":"lens","c":[0.93,0.16],"len":0.12,"w":0.16}]},
 "TRUE": {"cls":"quality","soft":"eiss","nick":true,"els":[{"t":"cut","p":[[0.06,0],[0.66,0]],"straight":true},{"t":"square","c":[0.82,0],"s":0.34},{"t":"ringarc","u":0.06,"v0":-0.34,"v1":0.34}]},
 "ANGER": {"cls":"thing","soft":"rhes","nick":true,"els":[{"t":"lens","c":[0.42,0],"len":0.34,"w":0.4,"fill":true},{"t":"star","c":[0.8,0],"r":0.26}]},
 "SHAME": {"cls":"thing","soft":"rhaenel","nick":true,"els":[{"t":"lens","c":[0.4,0],"len":0.34,"w":0.4,"fill":true},{"t":"ringarc","u":0.74,"v0":-0.62,"v1":0.62}]},
 "GLAD": {"cls":"thing","soft":"seiness","nick":true,"els":[{"t":"lens","c":[0.34,0],"len":0.34,"w":0.4,"fill":true},{"t":"cut","p":[[0.52,0],[0.92,0.14]],"bend":0.08,"k":0.8}]},
 "HOLY": {"cls":"thing","soft":"veness","nick":true,"els":[{"t":"cup","c":[0.54,0],"r":0.58,"form":"hold"},{"t":"lens","c":[0.54,0],"len":0.28,"w":0.3,"fill":true}]}
}
```

### 9.4 The look check of the new signs

![the new signs on chips](grain2/figs/v2_new_signs.png)

*`wf7/grain2/figs/v2_new_signs.png` (`proto_signs.py`): the 47 new signs alone on chips of end-grain.*

![the new signs beside their nearest v1 signs](grain2/figs/v2_neighbours.png)

*`wf7/grain2/figs/v2_neighbours.png` (`compare.py`): each new sign beside the v1 signs it is nearest to.*

**Recut during this pass**, each because a first drawing read as something else:

| Sign | First drawing read as | Recut to |
|---|---|---|
| WOOD | a Latin **E** (a stem with three arcs off it) | a billet: a lens sawn at both tips |
| FOLLOW, TRUE | **!** and **¡**: two colinear cuts, or a drop under a stem | FOLLOW: the short cut set well aside. TRUE: a plumb between a floor-bar and a small square |
| MORROW | Hebrew **kaf/bet**, katakana **コ** (a square C) | a closed rounded band along the ring |
| HEAR | first a Latin **C**, then a **?** (a stem with a sideways hook) | MOUTH turned toward the heart |
| BRIDGE | Greek **Ω** (an arch on out-turned feet) | a shallow span over a low arc, with no feet |
| CARRY | a **T** (a stem under a crosswise lens) | the stem leans, as the Bearer's prop leans |
| LOSE | an **emoticon**, "( :" | HAND with one finger gone, the thing fallen beside it |
| TAKE | Greek **Ψ**, then a yen sign | an asymmetric grasp: only the clockwise finger closes |
| BEAST | the same silhouette as EARTH (a bar on legs) | a thing with teeth: a half-lens with a toothed edge |
| WIND | a nested crescent, **☽** | an S-gust and its eddy |
| EARTH | a comb, or a table on legs | three uneven, splayed root-hairs |
| COME | the **mirror of FALL** | withdrawn (§9.2) |

**Left, and watched.**
- LEAF and BEARER are near **φ/Φ** (a lens with a line through it). The stalk below LEAF separates them from each other; among the rings they read as cuts.
- CHEST is near **ō** (a square with a macron).
- CHOOSE is near a lollipop or **♀** without its cross. The detached lens separates it from RISE.
- As in v1 §3.13: never show one of these alone at large size out of its round.

**Pairs that must never collapse**, added to v1 §3.12's overlay list, and checked at mark size and at 0.6 scale (pockets):

| Pair | What tells them apart |
|---|---|
| OVER / DEEP / BENEATH | the gap: OVER's cut does not touch its floor-bar; DEEP's does; BENEATH's bar is at the head |
| HEAR / MOUTH / CARVE | which end is joined: the head (HEAR) or the foot (MOUTH). HEAR and MOUTH are bulging lenses; CARVE is a straight V |
| NAME / HOLY / TEND / HOLD | what the cup holds: a groove lens, a solid lens, a shoot, or nothing |
| FIND / WEEP / EYE | a punch in the lens; a drop below the foot; nothing |
| MORNING / DUSK / SHORE / EDGE | the star beyond the arc; within it; a curl at the bar's end; the arc alone |
| SUMMER / TIDE / SPARK | TIDE with a star; TIDE; a star with no arc |
| LIE / SHORE | a lens at the arc's end; a curl |
| CARRY / STOP / KNOT | a leaning bowed stem and a pointed lens; a straight stem against a bar; a round knot with a dark heart that the rings bow round |
| TAKE / LOSE / HAND | a finger closed over a solid lens; one finger gone with the lens outside; the open palm |
| SILVERBARK / TREE | the star-notches at the bough tips |
| BONE / EYE | knobs at the ends of a cut; tails at the ends of a lens |

---

## 10 · COMPOSITION RULES v2 (replacing v1 §3.8)

1. **One root per round** [v1].
   - It is cut first, from the pith, along the axis, and it spans the whole heart ring. It owns files 15, 0 and 1 of every year of ring 1.
   - **In a telling, the root names what the telling is of.** Examples: v1's STONE root is STONEFOLK, "it is of one of the stone-folk", and GIFT's is STOP, the plea. The eight wood leaves' roots are in §11.3.
2. **One mark per cell**, and a mark is one sign or a ligature of two [v1, per cell]. Modifier inward, head outward [v1]. Ligature parts are cut at 0.7 breadth with the finer knife (§4.5).
3. **Where things stand.**
   - An act is cut on the file of its **doer**. A thing is cut on the file of the one it is, or belongs to.
   - A runner goes **from** the act to what it governs.
   - (v1's GIFT r5, with the felling cut on the pillars' file and a tie from the doer, stays valid: it reads "they do it to that".)
4. **Conditions** lie along the ring over files, in one year [v1, per year]. A mark inside a condition's files and year takes the condition [v1].
5. **Line quality classifies closed shapes only** [v1]. Runners, fringe marks and terminals never classify.
6. **Runners** follow §6.3. Crossings follow §7. A break must be declared. A pass is never declared.
7. **The root sets the axis. The seal and names stay in the bark** [v1]. No runner enters the bark band. Nothing crosses the bark's contour [v1].
8. **Properties of one mark combine** [v1]. These are negation, hollow, smoothed, count, ordinal, question, half, span, part and the fringe: `~!STRIKE`, `WOOD+!SMOOTH{all}`, `BEARER:keel{only}`.
9. **Likeness.** An *as* runner goes to its likeness. If the likeness is only an image, not present in the knowing, it is cut **hollow**, "shown, not meant" [v1 hollow]. Examples:
   - "the trees breathed out the grey **as sleepers breathe**" is `TREE×3+LIVE →as ~LIE`;
   - "as a mast holds up a sail" is `→as ~SAIL:mast`;
   - where the likeness is the custom itself, it is cut whole: IV.6's "as the long-lived lay down their dead" is `→as US×3+>LIE`.
10. **No small words are cut** (§6.5). No sign exists for *come*: it is GO → @f (§9.2).
11. **Economy for tier 3** [rule]. Every knowing of a wood leaf is carved, but only once:
    - one mark per content word;
    - a referent repeated in a knowing is pointed at (@f), not re-cut;
    - a clause shared by two knowings is carved in the first and reached from the second by a runner.
12. **Age gating** (§3) and the **canonical order** (§13.4) bind every round.

---

## 11 · CARVING A WHOLE WOOD LEAF: THE LAYOUT

### 11.1 The answer: one great round per leaf [rule; call §19.1]

**A wood leaf is one telling, known from one heart, so it is one round.** Its parts:
- the **three movements** are its three bands, parted by the two band-rules that stand where the Book's two `RING` markers stand [v1 §3.3];
- its **paragraphs** are its rings, as in v1's §4.4, whose ring counts stand;
- inside each ring, the paragraph's **knowings** fill the **years and cells** by the packing rule (§4.3–4.4), and **runners** knit them together;
- the formula paragraph "This is held in the grain" is the **seal** in the bark, not a ring [v1].

The alternatives the task asked about, and why they lose:

| Layout | Why not |
|---|---|
| **one great round per movement** (three rounds a leaf) | A movement is not a heart. It would lose the band-rules, which are the Book's own `RING` markers made visible, and the heartwood inside band-rule 1. It is **no more legible**: V.6's second movement alone is 42 sentences. The legibility problem is solved by plates (§11.5), not by cutting the heart in three |
| **one small round per knowing, arranged inside a leaf-round** | That is circles within a circle: Circular Gallifreyan's signature (§15), and exactly what v1 §3.13 forbids. Several piths in one round already *means* something in the grain: the Joined Tide, "several formations under one order" [v1 G8] |
| **full-circle sub-rings, one per knowing** | tried, and rejected on the evidence (§1.2): sparse, mechanical, a vinyl record |

### 11.2 From a leaf's text to its round [rule, for the Legends builder and the Knowing generator]

1. **Bands and rings.** Split the leaf at its two `RING` markers into three movements. Each movement is a band; each paragraph of it is a ring. The leading "This is held in the grain." and the closing "…and the grain holds it still." are the seal.
2. **Referents to files.**
   - List the leaf's referents.
   - **Places and bearings take even files** relative to the telling's road [v1]: the shore ahead (0), home and the grey behind (8), the right hand (4) and the left hand (12).
   - **Persons and things with no road take odd files.**
   - The teller ("we") takes the file of its bearing, or 12 by custom, as IV.6's Aelvaren does.
   - **Within a ring, one file is one referent.** v1 said "within a band"; a telling is too long for sixteen files to hold a band's referents, so for tellings v2 narrows it to the ring.
   - **From ring to ring**, a file keeps its referent until a new thing-sign stands first on it, which introduces the new referent there.
   - A ray says that marks in different rings are the same one [v1]. Orders keep v1's band rule.
3. **Knowings.** For each sentence, cut its content words as marks (one mark per content word; ligatures for compounds), on their referents' files. Then join them with runners by role. The sentence's framing is Halyna's, and not the wood's; it is carved only where it is the wood's own knowing. For example, "We do not know why" is the blind; "for fear leaves no mark on wood" is its gloss.
4. **Packing.** Place the knowings by §4.3.
5. **Crossings.** Declare the breaks, braids and binds the knowings mean (§7). Let passes fall where they fall.
6. **Check.** Run the validator (§14.2). A router failure means the GN must change, never the rule.

### 11.3 The eight wood leaves, planned

Sentence counts come from `wf6/legends_v12.md` (`wf7/grain2/count_leaves.py`). The estimates scale from IV.6, the leaf carved whole here, where 28 sentences gave 68 knowings, 100 marks, 64 runners, 29 years and a radius of 915. They assume about 3.6 marks and 1.0–1.2 years per sentence, and apply §4.2's pitch rule: 32 units a year up to 36 years, shrinking to 26 above 44.

| Leaf | Wood (v1 §4.4) | Pith | Rings I / II / III | Sentences | Est. marks | Est. years | Est. radius | Root (§10.1) |
|---|---|---|---|---|---|---|---|---|
| **II.2** Of the Breath of the Wood | the gift at its deepest holding: Myststone | round | 4 / 7 / 3 = 14 | 48 | ≈ 170 | 45–58 | 1,200–1,500 | **HOME** ("This is our home"; the gift's deepest holding is the home) |
| **III.2** The Thrones That Walk the Sea | each Throne's heart (eldest) | war | ten rounds, 6 / 1 / 1 each (§11.4) | 52 | ≈ 70 per heart | ≈ 20 per heart | ≈ 650 each | **that Throne's line root** (Seren's Book of Knowings: Thaesaen the Wave, Leavaren the Bar Before …) |
| **IV.2** The Axe in the Grain | a Blackthorn heart from a felled pillar's stump | war | 2 / 7 / 4 = 13 | 40 | ≈ 145 | 36–48 | 1,150–1,250 | **AXE** |
| **IV.4** The Gift Held an Hour | the gift itself: Myststone | round | 2 / 11 / 3 = 16 | 52 | ≈ 190 | 47–62 | 1,200–1,600 | **GIFT** ("We were given once") |
| **IV.6** The Voyage of the Aelvaren | a Remembering heart | war | 2 / 8 / 1 = 11 | 28 | **100** (carved) | **29** (carved) | **915** (carved) | **HOLD** ("not in this grain only"; held at the root) |
| **V.3** The Wreck That Went Home | a Remembering hull | war | 2 / 6 / 3 = 11 | 31 | ≈ 110 | 28–37 | 900–1,150 | **STERN** ("Home when wounded" woke in it) |
| **V.4** The Council Under the Thin Sky | a Silverbark heart, Joined Tide | war | 1 / 11 / 3 = 15 | 38 | ≈ 135 | 34–46 | 1,100–1,200 | **SILVERBARK** ("We are a cutting of those elders") |
| **V.6** Of the Growing | a Joined Tide heart | war | 4 / 15 / 5 = 24 | 58 | ≈ 210 | 52–70 | 1,350–1,800 | **GROW** ("We were grown, not built") |

- **The IV.4 gift sentence** keeps its own round (`mystaeri_spec.md` §5.4). IV.4's ring 15 cites it as a cut-pocket holding STOP½ (§8).
- **V.6's Song of the Years** (its ring 23) is one **said-pocket** per line of the song, in successive years, sung by the groves (SILVERBARK×3 or TREE×3 + SING →that). Seven lines is seven pockets.

### 11.4 III.2: ten hearts [rule; the closing is a call, §19.3]

III.2 is "known from the hearts of the Mystarchs … each in its own haven", and "the headnote and the opening knowings … come with the first". So:

- **Each Throne's heart is one round.** Its pith is war, and its root is its line's root (Seren's table).
  - **Band I** (6 rings) is the six opening knowings: "We came late … at the third cry it was cut, and it fell". It is **identical in all ten hearts**, because every heart holds it. The Book draws it truthfully in every round, and it is glossable from the first Throne on.
  - **Band II** (1 ring) is that Throne's own entry: its name, "whom you named …" as a said-pocket (NAME → pocket{BEAST+…}), its haven, the kin in the haven's walls, and its judgement as a **cut-pocket**.
  - **The bark** holds the seal, and in the seal's cup the Throne's name [v1 §3.14], untold until it falls.
  - **Band III** (1 ring) is the closing, "These were the ten … the sky over the groves is thin". **Recommended:** each heart's band III is **its own fall**, cut by the wood as it fell: FALL, the haven yours again (`CASTLE → @0`), the thin sky. A Throne's bark already closes a pale ring at each groan in real time [v1 G9], so the wood does record what happens to it. Halyna's closing paragraph is the ten band-IIIs told together, and so it is glossable only when all ten have fallen, as the Book's comment already says.
- **The Book draws the ten rounds** in the order of the havens, each at about 650 units, with its entry's ring plate.

### 11.5 Showing it in the Book: the whole round and the ring plates [rule; the Legends builder]

- **The blank leaf** (v1 §4.3) shows **the whole v2 round**, fully and truthfully cut, with no glosses.
  - At page width it is a texture to take in whole, "known in a breath": the plain heart, and the intertwined sapwood.
  - Its marks are about 8–12 px tall at 900 px, so a decoder zooms.
  - The Stone's facing leaf, before the Epilogue, still shows rings only [v1 §5.7].
- **Ring plates: Seren's reading of the round**, set on the facing page, one per paragraph (ring).
  - A plate is **that ring alone**, re-laid at reading scale, with its inner radius normalised to 240 units. It is the same GN, the same seeds, and the same years and cells.
  - It is drawn as an **annulus with no pith**. An annulus without a pith is never a round, so it cannot be mistaken for "nothing is given here".
  - **Runners to or from other rings** are drawn to the plate's edge, as stubs cut off by the plate's own outline. Beside each stub, the Book's margin carries a small pencil tag, "→ r8" or "from r4". **The tags are Seren's apparatus, not the grain**, in her course-hand numerals (the shoreland spec).
  - At 600 px a plate's marks are 18–26 px: legible.
  - `figs/v2_iv6_plate9.png` and `figs/v2_iv6_plate5.png` are IV.6's rings 9 and 5 as plates.
- **Glossing.** The whole round and the plates are glossed together, mark by mark, at the ladder's fidelity (§16). Seren's brackets are as in v1 §4.2.
- **The three tabs** (Jack: "I like that there are 3 tabs for the book"). The grain is language-free, so it is identical under all three [v1 §4.6]:
  - **The Book** shows Halyna's telling, the Book's words;
  - **Plain Words** shows the modern English, and its glosses use plain words;
  - **Original** shows the native hand: the whole round, then the ring plates in order, each with the **literal reading** (§13.5) set under it once the ladder allows.
- **Motion.** Any growing-in of rings or runners honours `prefers-reduced-motion` [v1].

### 11.6 Sizes and budgets [rule]

| Drawing | Prototype (no optimisation) | Budget | How |
|---|---|---|---|
| a whole-leaf round (IV.6) | 510 KB | **≤ 350 KB** | merge each cut's facets into two paths; one decimal; `<defs>`/`<use>` for repeated signs at their cell size; above 150 marks, the whole round uses **one silhouette per cut** (lit tone only), and facets are kept for the plates |
| a ring plate | 42–52 KB | **≤ 60 KB** | as v1 §3.11 |
| a Throne heart (III.2) | — | ≤ 120 KB | each heart cuts band I in its own wood (its own seed), so nothing is shared between the ten |
| all eight leaves, whole + plates | — | ≈ 3.5 MB | the builder should lazy-load a leaf's round and plates when the leaf opens |

---

## 12 · THE WORKED LEAF: IV.6, THE VOYAGE OF THE AELVAREN, CARVED WHOLE

The leaf is 11 rings (2 / 8 / 1), 28 sentences, 68 knowings, 100 marks and 64 runners. It has one break, one braid, two pockets and two blinds. It was written as a grain text (`wf7/grain2/IV-6.json`) and drawn by the prototype (`proto_v3.py`). Its canonical GN v2, below, was printed from the same data by `gn2.py`; nothing in it is typed by hand.

### 12.1 Its files

| File | Referent | Why this file |
|---|---|---|
| 0 | the shore; the house at its edge; its host and men; "you" | ahead, toward the shore [v1 bearing] |
| 1 | the Guest (BOND+US, *aelea*) | placeless |
| 2 | the door and the shallows below it | a place beside the shore |
| 3 | the rite (AELTHAR) | placeless |
| 4 | the open sea | the right hand |
| 5 | the current (ring 5); the shore-men's hulls (ring 6, introduced by STONEFOLK+HULL×3) | placeless |
| 6 | the road home ("that road", "the way home") | the right-behind diagonal |
| 7 | every hull (rings 1, 11) | placeless |
| 8 | home: the council-grove, the pale sand, the roots | behind [v1 bearing] |
| 9 | the council of the long-lived | placeless |
| 10 | the old channels, the secret waters | the left-behind diagonal |
| 11 | the grey (rings 2, 6, 7); the rain (ring 11) | placeless |
| 12 | **we, the Aelvaren** (the teller); our keel | the left hand |
| 13 | the fire | placeless |
| 14 | this hull, the one that brings it (ring 1); wood in general (rings 4, 5, 9) | the left-ahead diagonal |
| 15 | every grove, and the young trees in them (ring 11) | placeless (ring 1's file 15 belongs to the root) |

### 12.2 Its Grain Notation v2 (canonical, printed by `gn2.py`)

```
round IV-6-aelvaren {wood: life; pith: war; rings: 11; rules after: [2, 10]; cells: [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4]}
  I
    r1/1  0: HOLD*    7: HULL×3{all}    12: BOND+BEARER    14: HULL+CARRY
    r1/2  14: !EYE
    r1/3  14: HOLD
    r2/1  1: BOND+US    2: BENEATH+DOOR    3: AELTHAR    11: THIN    12: BOND+BEARER
    r2/2  12: NAME+GLAD
    r2/3  12: DEEP+HULL½      band MIST files 12–12
    r2/4  12: CARRY      band MIST files 10–11
    r2/5  12: KNOT      band WATER files 2–3
    r2/6  12: CARRY
  ‖
  II
    r3/1  0: STONEFOLK×3+>GO    1: !LIVE    12: BOND+BEARER
    r3/2  1: BLOOD    12: WOOD
    r3/3  1: HOLD{last}    12: WOOD+EAT
    r3/4  12: HOLD{all}
    r4/1  0.1: >BURN    0.2: >GO    4: TAKE    12.1: DEEP+WOOD    12.2: GRIEF+ANGER    14: WOOD+CRY      band WATER files 4–6
    r4/2  12.1: BURN{more}    12.2: CRY
    r5/1  4: !HOLD    5: TAKE    6: ROAD    8: HOME    12.1: BURN+TURN    12.2: BEARER:keel    12.3: HOLD    14.1: DYING+WOOD    14.2: HOLD      band WATER files 4–5
    r5/2  12: GO
    r6/1  5.1: STONEFOLK+HULL×3    5.2: GO#2    5.3: TURN    11: EDGE    12: BOND+BEARER      band MIST files 10–11
    r6/2  5: SWIFT+GO
    r7/1  0: !GO    1: BONE×3    10.1: _DEEP+ROAD    10.2: ROOT×3    11.1: THIN{most}    11.2: CLOSE    12.1: FIND    12.2: BURN{all}    12.3: BEARER:keel{only}    12.4: BONE×3{few}    13: !BURN{slow}      band MIST files 11–12  band WATER files 10–10
    r8/1  8.1: SAND    8.2: SILVERBARK×3    12.1: RISE½    12.2: BENEATH+LIE      band DARK files 12–12  band WATER files 7–7  band STILL files 12–12
    r9/1  9.1: US×3    9.2: GO    9.3: HOLD    9.4: >GO    12.1: BOND+BEARER    12.2: BEARER:keel
    r9/2  9.1: BOND+HAND×3    9.2: HOLD{all}    pocket P1 cut 11–2 { GIFT  US:foot+DUST  US:stem  US:crown/  AXE+TURN  STRIKE+FALL  BURN  >GO }
    r9/3  14: WOOD+!SMOOTH{all}
    r10/1  0.1: MOUTH    0.2: HAND:stem+TURN    0.3: STRIKE×3    1.1: >DYING    1.2: TRUE    3: HOLY+AELTHAR    pocket P2 said 5–7 { !HOLD }    9.1: EYE    9.2: HOLD    9.3: !HOLD    9.4: !MOUTH?    13: BURN
    r10/2  9: EYE{only}
  ‖
  III
    r11/1  0: SQUARE    1: BONE×3{still}    7.1: HULL    7.2: HULL×3{all}    7.3: CARRY    8.1: ROOT×3    8.2: ROOT×3+EAT    8.3: SILVERBARK×3    9.1: >LIE    9.2: US×3+>LIE    11: RAIN    12.1: BEARER:keel    12.2: GRIEF    15.1: TREE×3{all}    15.2: SAPLING×3{all}    15.3: EAT
  bark
    bark 0: HOLD
  runners
    run a1   0.r1/1       →in    7.r1/1
    run a2   14.r1/1      →      @0
    run a3   12.r1/1      ⇒      14.r1/3
    run b1   12.r2/4      →      1.r2/1
    run b2   12.r2/4      →thru  11.r2/1
    run b3   12.r2/5      →in    2.r2/1
    run b4   12.r2/5      →for   12.r2/6
    run b5   12.r2/6      →      @1
    run b6   12.r2/6      →with  3.r2/1
    run c2   0.r3/1       →      @1
    run c1   1.r3/1       →      12.r3/1
    run c3   1.r3/2       →in    12.r3/2
    run c4   1.r3/3       →in    12.r3/3
    run c5   1.r3/3       →with  1.r3/2
    run c6   12.r3/4      →bc    12.r3/3
    run d1   0.1.r4/1     →      12.1.r4/1
    run d4   0.2.r4/1     →      @12
    run d5   4.r4/1       →      @12
    run d2   12.1.r4/2    →as    0.1.r4/1
    run d3   12.2.r4/2    →bc    14.r4/1
    run g1   4.r5/1       →      12.2.r5/1
    run f1   5.r5/1       →      12.1.r5/1
    run g6   6.r5/1       →      8.r5/1
    run e1   12.1.r5/1    →      8.r5/1
    run g2   12.3.r5/1    →      6.r5/1
    run g3   12.1.r5/1    →bc    4.r5/1
    run g5   14.2.r5/1    →      6.r5/1
    run g4   12.r5/2      →      8.r5/1
    run h1   5.2.r6/1     →thru  12.r6/1
    run h3   5.3.r6/1     →bc    ∅
    run h2   12.r6/1      ⇒      5.3.r6/1
    run i3   0.r7/1       →      10.2.r7/1
    run i5   1.r7/1       →in    12.4.r7/1
    run j1   10.1.r7/1    ⇒      12.1.r8/1
    run q    11.2.r7/1    →      13.r7/1
    run i1   12.1.r7/1    →      10.1.r7/1
    run i2   12.1.r7/1    →in    11.1.r7/1
    run p    13.r7/1      →      11.2.r7/1
    run j2   12.1.r8/1    →      8.1.r8/1
    run j3   12.2.r8/1    →in    8.2.r8/1
    run k1   9.2.r9/1     →      @12
    run k2   9.3.r9/1     →      @12
    run k3   9.3.r9/1     →bc    9.4.r9/1
    run k4   9.4.r9/1     →      @12
    run k5   9.1.r9/2     →      12.2.r9/1
    run k6   9.2.r9/2     →that  P1
    run l2   0.1.r10/1    →      3.r10/1
    run l3   0.1.r10/1    →with  1.1.r10/1
    run l4   0.1.r10/1    →with  13.r10/1
    run l6   0.2.r10/1    →bc    ∅
    run l1   9.1.r10/1    →      3.r10/1
    run l5   9.2.r10/1    →      1.1.r10/1
    run l7   9.3.r10/1    →that  P2
    run l8   9.r10/2      →      0.3.r10/1
    run m3   1.r11/1      →in    12.1.r11/1
    run m10  7.3.r11/1    →      12.2.r11/1
    run m9   7.2.r11/1    →      0.r11/1
    run m5   8.1.r11/1    ⇒      8.2.r11/1
    run m6   8.3.r11/1    →      15.1.r11/1
    run m1   9.1.r11/1    →      12.1.r11/1
    run m4   9.1.r11/1    →as    9.2.r11/1
    run m2   12.1.r11/1   →in    8.1.r11/1
    run m7   15.2.r11/1   →for   7.1.r11/1
    run m8   15.3.r11/1   →with  11.r11/1
  lap  e1 ⊳ f1
  braid B1 p q : abab!
```

### 12.3 Three rings, read by rule

**Ring 5.**
- *Literal reading* (§13.5):
  - On the water's file (4): not holding. On the current's (5): taking. On the road's (6): the road. On home's (8): home.
  - On ours (12), in cells clockwise: burning, turning; the keel; holding. On the wood's (14): the dying wood; holding.
  - The current's taking goes to us (f1). Our turning goes to home (e1), and **breaks** the current's taking (`lap e1 ⊳ f1`). We turn because (g3) the water does not hold (g1) the keel.
  - We hold, to the road (g2). The road, to home (g6). The dying wood holds, to the road (g5).
  - In our next year we go, to home (g4).
- *The telling* (canon): *We turned against the current, burning, for no water holds a keel that knows its way; and we sailed ourselves home. Even charred, even dying, the wood knows the way home.*

**Ring 7.**
- *Literal reading:*
  - We, in cells clockwise: find (i1, to the old hidden ways, 10.1) in the thinnest grey (i2); burning, all; the keel, only; bones, few.
  - The old ways are among roots (10.2). To them the shore does not go (i3).
  - The fire (13), not burning, slowly, and the grey (11.2), closing, are **braided** `abab!`: by turns, and at the last the grey thwarts the fire.
  - The Guest's bones (1) are in ours (i5).
- *The telling:* *Under the thinnest of the grey we found the old channels, the secret waters that run among the roots where no shore-man's keel has gone. All that way we burned, and the fire went out of us slowly as the grey closed over, until nothing was left of us but the keel, a few ribs, and the Guest's bones in them.*

**Ring 9.**
- *Literal reading:*
  - The council (9), in cells: those of us; going, to us (k1); holding, to us (k2), because (k3) sending, to us (k4).
  - In its next year: joined hands, to our keel (k5); holding all, **that** (k6): *[cut pocket P1: the gift; the foot, and dust; the neck; the brow leaning; the axe turning; struck and falling; burning; the sending]*.
  - Then, on the wood's file: wood, not hiding, at all.
- *The telling:* *The council of the long-lived came down to us, and knew us, for they had sent us. They laid their hands on our keel, many hands together, and knew the whole of it: the gift set down, and the foot that put it in the dust; the neck held gently, the foreheads meeting, the blade that slipped; the Guest struck down, the fire, the shove into the current. Wood can hide nothing.*

![IV.6 ring 9 as a plate](grain2/figs/v2_iv6_plate9.png)

*`figs/v2_iv6_plate9.png`: ring 9 as a ring plate. Its cut-pocket, with the eight things the keel held, lies across the top.*

### 12.4 What the prototype still does badly (for the production renderer)

- **Routing failures.** Three runners of ring 7 (i1, i3, i5) found no way, and are not drawn. The crowded ring needs a wider search window before failing (§6.2.8).
- **Double crossing.** The declared break e1 ⊳ f1 crosses twice. The square-crossing rule must also forbid the breaker from re-crossing its target (§14.2).
- **Weight.** Runners that run far along the grain, near the bark, read at page size almost as extra rings. Two remedies [call §19.2]:
  - cut runners in the **mid** tone only (74%), rather than lit;
  - raise the ring-line crossing cost, so they climb sooner.
- **No bind in IV.6.** The leaf has no bind, so the bind was proved only on its specimen chip.

---

## 13 · GRAIN NOTATION v2 (replacing v1 §3.12's notation; the round trip is §14)

### 13.1 What it is

**GN v2** is the canonical linear form of a round. It is written in the order a round is read (§13.4), and it is a **strict superset of v1**:
- every v1 text is a v2 text with the same meaning (§13.7);
- one drawing has exactly one canonical GN v2, and that GN draws that drawing (up to seeded noise).

### 13.2 Grammar (EBNF)

```ebnf
round      = header, NL, { band | rule_line }, [ bark ], [ devices ] ;
header     = "round ", id, " {", attr, { "; ", attr }, "}" ;
attr       = "wood: ", ( "green" | "forty" | "life" | "long" | "eldest" | "stone" | "plain" )
           | "pith: ", ( "round" | "war" ), [ " ×", int ]
           | "rings: ", int
           | "rules after: [", [ int, { ", ", int } ], "]"
           | "cells: [", int, { ", ", int }, "]"            (* derived; printed for the reader *)
           | "axis ", deg ;
band       = INDENT, ( "I" | "II" | "III" ), NL, { yearline } ;
rule_line  = INDENT, ( "‖" | "‖¦" ), NL ;                    (* a band-rule; ¦ = over included bark *)
yearline   = INDENT2, "r", int, "/", int, { SEP, ( mark | pocket ) }, { SEP, cond }, NL ;
                                                              (* r<ring>/<year>, years from 1 *)
mark       = [ pith_pfx ], file, [ ".", cell ], ": ", ligature ;
ligature   = token, [ "+", token ] ;
token      = { "!" | "~" | "_" | ">" }, SIGN, [ ":", PART ], { suffix }, [ fringe ] ;
suffix     = "×3" | "‿" | "½" | "?" | "*" | "/" | "\"
           | "#", digit1to4 | "@", digit1to4
           | "^r", int, [ "/", int ] ;                         (* span: until ring/year *)
fringe     = "{", FR, { ",", FR }, "}" ;
FR         = "all" | "few" | "half" | "only" | "more" | "most"
           | "again" | "still" | "last" | "slow" | "gently" ;
pocket     = "pocket ", pid, " ", ( "said" | "cut" ), " ", file, "–", file,
             " { ", item, { "  ", item }, " }" ;
item       = ligature | pocket ;                               (* depth ≤ 2 *)
cond       = "band ", BAND, " files ", file, "–", file ;       (* in that year *)
bark       = INDENT, "bark", NL, { INDENT2, "bark ", file, ": ", ligature, NL }, [ INDENT2, "pale ", int, NL ] ;
devices    = { runner | lap | braid | bind | ray | mem | split } ;
runner     = INDENT, "run ", rid, " ", addr, " ", arrow, " ", target, [ " _" | " ~" ], NL ;
arrow      = "→" | "⇒" | "→in" | "→with" | "→for" | "→bc" | "→as" | "→thru" | "→that" ;
target     = addr | "@", file | pid | "∅" | "bind ", kid ;
split      = INDENT, "run ", rid, " ", addr, " ", arrow, " {", target, { ", ", target }, "}", NL ;   (* ≤ 3 shoots *)
lap        = INDENT, "lap ", rid, " ⊳ ", rid, NL ;             (* a break: the first thwarts the second *)
braid      = INDENT, "braid ", bid, " ", rid, " ", rid, [ " ", rid ], " : ", PATTERN, NL ;
PATTERN    = ( "a" | "b" | "c" ), { "a" | "b" | "c" }, [ "!" ] ;   (* one letter per crossing, length ≤ 9 *)
bind       = INDENT, "bind ", kid, " ", rid, " ", rid, [ " ", rid ], [ " ", ( "→" | "⇒" ), " ", addr ], NL ;
ray        = INDENT, "ray ", file, ": r", int, [ "/", int ], "–r", int, [ "/", int ], NL ;      (* v1, years optional *)
mem        = INDENT, "mem ", file, ": r", int, [ "/", int ], " → pith", NL ;                   (* v1 *)
addr       = [ pith_pfx ], file, [ ".", cell ], ".r", int, "/", int ;
pith_pfx   = "p", int, "·" ;
file       = "0" … "15" ;   cell = "1" … "4" ;
```

**Conventions.**
- The **cell** is written only when a file holds more than one mark in that year: `12.2: BEARER:keel`, `12.2.r5/1`.
- The **year** is written only when a ring has more than one: `r5/2`. `r5` alone is `r5/1`.
- `rid`, `bid`, `kid` and `pid` are free identifiers. Only their order carries meaning (§13.4).

### 13.3 Tokens, at a glance

| Written | Is | § |
|---|---|---|
| `SIGN` | one of the 117 signs | §9, [v1 §3.5] |
| `!` `~` `_` `>` | not (the mirror) · hollow (a seeming) · smoothed (hidden) · causative | [v1] |
| `:part` | the part device | §5.2 |
| `×3` `‿` | many; and a whole kind | [v1], §5.3 |
| `½` `?` `#n` `@n` `^r…` `*` `/` `\` | half size; question; count; ordinal; span; the root; lean | [v1] |
| `{…}` | the fringe | §5.4 |
| `run …` | a runner, by role | §6 |
| `@f` | a file referent | §6.1 |
| `∅` | the blind | §6.1 |
| `lap a ⊳ b` | a break | §7.1 |
| `braid … : abab!` | a braid | §7.2 |
| `bind …` | a bind | §7.3 |
| `pocket P said\|cut s0–s1 {…}` | a pocket | §8 |

### 13.4 The canonical order [rule; replaces v1 §3.8.10]

1. The header.
2. Band by band. Within a band, ring by ring outward. Within a ring, year by year outward. Within a year, **file by file clockwise from 0**, then **cell by cell clockwise**.
   - In a joined round: shared rings about the centre, own rings pith by pith clockwise from the axis [v1].
   - Pockets stand in their year at their first file. Their items keep their own clockwise order.
3. The band-rule lines, between rings.
4. The bark: names, the seal, pale rings.
5. **Runners**, sorted by source address (ring, year, file, cell), then by target address, then by id.
6. Laps. 7. Braids. 8. Binds. 9. Bands spanning rings, if any [v1]. 10. Rays [v1]. 11. Memory rays [v1].

The same order decides **which strand lies over** in a pass (§7.1).

### 13.5 The literal reading [rule]

**Ring by ring**, and within a ring, **referent by referent** (file order), read each file's marks in their year and cell order. Then read its runners as `A —role→ B`, using the role's gloss:

| Role | Read as |
|---|---|
| → | to |
| ⇒ | then / from this |
| →in | in |
| →with | with |
| →for | for, so that |
| →bc | because |
| →as | as |
| →thru | through |
| →that | "that: […]" |
| ∅ | "why, the wood does not hold" |

- A **pass** adds nothing to the reading. A **break** reads "and [A] broke [B]".
- A **braid** reads "by turns" (2 strands) or "each holding the others" (3), plus the turn sequence, and "until at the last [x]" for `!`.
- A **bind** reads "bound: each only with the other", plus its out-runner.
- **Pockets** are read in brackets.

§12.3 shows three rings read this way. The literal reading is a gloss. **The telling** is Halyna's English, a translation, as in v1.

### 13.6 The grain text v2 (JSON, for the renderer)

An illustration of the keys, drawn from IV.6's text; the full leaf is `wf7/grain2/IV-6.json`.

```json
{
 "id": "example", "seed": "example", "wood": "life", "pith": "war", "axis": 0, "rules": [2, 10],
 "english": "…", "literal": "…", "root_word": "held",
 "rings": [
  {"band": "I", "knowings": [
    {"marks": ["0: HOLD*", "7: HULL×3{all}"]},
    {"marks": ["14: HULL+CARRY"]},
    {"marks": ["9: HOLD{all}"], "conds": [{"band": "MIST", "files": [11, 12]}],
     "pockets": [{"id": "P1", "kind": "cut", "files": [11, 2], "contents": ["GIFT", "US:foot+DUST"]}]}
  ]}
 ],
 "runners": [
  {"id": "a1", "from": "0.r1·1", "to": "7.r1·1", "role": "in"},
  {"id": "a2", "from": "14.r1·2", "to": "@0", "role": "to"},
  {"id": "h3", "from": "5.r6·3", "to": "∅", "role": "blind", "blind_file": 7},
  {"id": "k6", "from": "9.r9·6", "to": "P1", "role": "that"},
  {"id": "x",  "from": "15.r2·1", "to": "bind:K1", "role": "to", "hidden": false, "seeming": false}
 ],
 "laps":   [{"over": "e1", "under": "f1"}],
 "braids": [{"id": "B1", "strands": ["p", "q"], "pattern": "abab!"}],
 "binds":  [{"id": "K1", "strands": ["x", "y"], "site_file": 0, "out": {"to": "0.r2·2", "role": "then"}}],
 "bark": {"marks": ["0: HOLD"], "pale": 0},
 "rays": [], "memory": []
}
```

- **Knowings are listed in the telling's order.** An address in JSON is `file.r<ring>·<knowing>`: the knowing's number, not its year.
- **The renderer packs** the knowings into years and cells (§4.3) and prints the canonical GN with years and cells (`gn2.py`).
- The prototype still writes `@f` as `"bearing f"`. v1's JSON keys (`bands`, `rings`, `marks`, `ties`, `rays`, `memory`, …, v1 §10.2) are read as a one-knowing-per-ring v2 text.

### 13.7 v1 compatibility [rule]

| v1 GN | reads in v2 as |
|---|---|
| `r5   12: GO` | `r5/1  12: GO` |
| `tie 0.r1 → 4.r2` | `run t 0.r1/1 ⇒ 4.r2/1` (rings differ: *then*) |
| `tie 10.r4 → 0.r4` | `run t 10.r4/1 → 0.r4/1` (same ring: *to*) |
| a tie to an empty file | `→ @f` |
| `ray`, `mem`, `band`, `‖`, `¦`, `graft(…)`, `pN·`, `pith: war`, `bark`, `pale` | unchanged |
| fork `A<X\|Y>`, chain `<… root>` | unchanged [v1]. v2's renderer draws them, where v1's did not: the fork is a cut splitting at its head, its clockwise branch the *if* |

So every one of the 46 carvings, *Burn* and every v1 sample (`mystaeri_spec.md` §5) is a valid v2 text, with its meaning unchanged.

---

## 14 · DECODING BY RULE, AND THE ROUND TRIP (replacing v1 §3.12's decode)

### 14.1 Decoding a v2 drawing

1. **The pith or piths**, and **the root**: the mark that touches the pith. Its direction gives θ₀ [v1].
2. **Lines.** Classify every line that runs with the rings:
   - a ring line (latewood, crisp outside);
   - a band-rule (doubled);
   - included bark (a dark jagged line);
   - a pale ring (in the bark);
   - a **year-line** (a faint short arc under one mark, at a year's floor);
   - a **pocket border** (a lens: smooth and doubled means *said*, jagged means *cut*);
   - a condition band [v1].
3. **Years and cells.** In each ring, cluster the marks' foot radii into years; the year-lines confirm them. Within a slot, count the marks side by side. The ring's cell count is the most any slot holds, and the header prints it.
4. **Marks.** For each mark, read:
   - its file: round((θ − θ₀)/SLOT) mod 16, measured about its pith or the joined round's centre [v1];
   - its cell, by its offset within the slot;
   - its ring and year;
   - its **sign**, by element signature, including the part device (which elements are hollow) and ligature halves;
   - negation, by the mirror test [v1];
   - its **fringe**, by station and form;
   - its other devices: ×3, ‿, ½, ?, #, @, span, lean [v1].
5. **Pockets.** Read each pocket's kind, files, mouth and items (clockwise), then any pocket inside it.
6. **Runners.** Find every narrow faceted cut that is not part of a sign.
   - Start at its **node**: the small swelling at a mark's head.
   - **Trace it**: along the grain, across the rings, through crossings. At a crossing, the **continuous strand is the one over**, so tracing never changes strand there.
   - Stop at its **terminal**. Read its role from the terminal and its landing (§6.1): head, foot, flank, a cell with nothing in it (`@f`), a pocket mouth, or empty wood (∅).
7. **Crossings.**
   - At each crossing of two runners: clean under-ends are a **pass**; splintered ends are a **break** (`lap over ⊳ under`).
   - Where two or three strands weave along one cord, it is a **braid**. Read its over-strands in order along the cord from the first strand's source: that is the pattern, with `!` if its last crossing is splintered.
   - Where two strands hook through each other, it is a **bind**. Read its out-runner, if any.
8. **Hairlines** [v1]: rays (along a file), memory rays (to the pith, ending in root-hairs), and the grain-arc in names.
9. **Knowings.** Group each ring's marks by runner-connectivity (§4.1).
10. **Emit** the canonical GN v2 (§13.4).

### 14.2 Validation, run before any export [rule]

Everything in v1's list (§3.12) stands:
- encode → draw → decode → compare, for every round;
- no two signs share an element signature, and no sign's mirror is another sign;
- jitter never crosses a quantisation threshold;
- no ring crosses another;
- nothing crosses the bark contour;
- the size budget holds.

Add:

1. **Round trip** for every leaf round, every Throne heart, every plate, the 46 carvings, *Burn* and every v1 sample: the decoded GN v2 **equals** the source's canonical GN v2.
2. **Signatures.** The 117 signs, their parts, and their mirrors are pairwise distinct, at mark size, at root size in a 56-unit heart ring (v1), and at pocket scale (0.6). The new must-not-collapse pairs of §9.4 are overlaid.
3. **Gates.** No mark comes within 3 units of a half-file or half-cell line, and every year's top 5.5 units are free.
4. **Runners.** Each runner has one node, at its source's head, and one terminal of its role. It keeps 3.2 units from every mark but its own two, and it never crosses a ring line inward. It has at most 300° of turning, no loop and at most one fork.
5. **Crossings.** Every crossing is at 15° or more.
   - Every pass has, as its over-strand, the later runner in canonical order.
   - Every declared break is **exactly one** crossing, square, splintered.
   - Every braid has exactly its pattern's number of crossings in its stretch, and the over-strands match.
   - Every bind has exactly two lock crossings (x over, then y over) and at most one out-runner.
6. **Pockets.** Each has one mouth and exactly one *that* runner, at most eight items, at most one pocket inside it, and no runner through it.
7. **Packing.** Years and cells are reproduced from the marks alone (§4.3). Adding or removing a runner moves no mark.
8. **Age gating** (§3): no device in wood too young for it. The heart ring carries no fringe, braid, bind or pocket.
9. **Determinism.** Two runs are byte-identical [v1].

### 14.3 The decode test to run (a builder item)

The wf6 decode test (`wf6/decode_report.md`) took the grain from 1 of 6 rounds right first time to 6 of 6 after fixes. v2 needs the same test, **blind**, by a fresh decoder given only §§3–8, 13 and 14 of this spec and the pictures. Test on:
- IV.6's ring plates 5 (the break), 7 (the braid) and 9 (the pocket);
- a plate with a bind: the Aelthar's r6 in v2, §17;
- E4-01 in its v2 drawing;
- the whole IV.6 round at 1,100 px, **for structure only**: the root, the bands, the ring count, and which files carry the story.

---

## 15 · KEEPING CLEAR OF ARRIVAL AND THE OTHERS (replacing v1 §3.13's table; its text stands)

v2 asked for more intertwining. That moves the grain toward three looks v1 had banned outright: branching vines, interlocking, and knots. The boundaries are therefore restated **by their signatures**, not by broad words, so v2 can be intricate without borrowing anyone's look.

| Look to avoid | Its signature | Where v2 stands |
|---|---|---|
| **Arrival** (the heptapods' logograms, in the film) | one inked ring per sentence; tendrils and hooks off the rim; smoke and blots; thicker means more urgent; no start and no end; made in one gesture | Many growth rings, with runners **inside** them and nothing off the rim [v1]. Every cut is faceted, with no smoke. A runner's taper gives its **direction**, not its tone; weight carries nothing [v1]. The round reads heart to bark, and a later ring grows over an earlier one [v1]. Jack's "same flavour" is kept as an idea: a writing of meaning, taken whole, in circles |
| **Nomai** (*Outer Wilds*) | text written *along* a spiral; each spiral is one speaker; replies branch off as new spirals, and a conversation is a tree of spirals on a wall | Runners carry **no text along them**: the signs stand apart, and the runners only join them. Runners follow the grain and **never spiral**: at most 300° of turning, no curl tighter than 5 units (terminals and locks apart), no loop. They **fork once at most**, and a shoot never forks. Everything is enclosed in growth rings |
| **Circular Gallifreyan** | word-circles inside a sentence-circle; dots and arcs on the circles; straight lines joining circles; read anticlockwise from the bottom | No circle anywhere but the growth rings. Year-lines are **partial** arcs, never closed. No dot sits on a line: punches are inside signs. Runners join signs, never circles, and they drift; they are never chords. No small rounds inside a leaf-round (§11.1). The grain reads clockwise from the root [v1] |
| **The Elden Ring emblem** | overlapping, interlocking ring arcs; a golden glow; a staff line through the rings | Rings **never** interlock. Only runners, which are open cuts, cross, and a bind is two open hooks, never two closed curves linked. No glow. No straight staff: the only straight radial line is a ray, within one file [v1] |
| **Celtic and Norse interlace**: knot panels and borders, the triquetra, the triskele, Solomon's knot, the endless knot, Borromean rings, and **the valknut**, which has a modern extremist use as well | interlace as *ornament*: closed, symmetric, periodic panels; rotational three-fold knots | Interlace appears **only where two relations cross**, and every crossing is read (§7). No closed knot, panel or border. A braid is short, open at both ends, and runs along one ring. A bind is a two-strand lock; three strands chain as two locks, **never a three-fold rotational figure**, and never interlocked triangles |
| **Runes, Cirth, Tengwar** | staves with straight branches meeting at a point; stem-and-bow letters | v1's principle, applied to all 47 new signs (§9.1): bow, stagger or break. The fringe never runs along a stem-line (not Ogham) |
| **Letters, punctuation, icons**: Latin, Greek, Hebrew; ! ? ¡; emoticons; ¥; the ankh; ☽ ♀; Wi-Fi arcs | one small glyph that is already something | the recut list (§9.4). Never show one sign alone at large size out of its round [v1] |
| **Circuit boards and transit maps** | parallel traces with 45° jogs; orthogonal routing | the string-pulled, grain-following router (§6.2), and the runner repulsion that breaks bundles (§1.2) |
| **Tree-carving traditions**: the Moriori *rākau momori* of Rēkohu (the Chatham Islands), carved in living kōpi trees; the Basque shepherds' aspen carvings | figures cut into the **bark of standing trees** | The grain is cut across the **end-grain** of a heart, never on standing bark, and it carves no human figures in the bark. Named here with respect, so that no later sign drifts toward them |
| **Avatar** (the forest's root network that holds the ancestors) | a living link between trees that holds memory | Runners are **cuts inside one heart**, not links between trees. "What went home through the roots" is carved: the memory ray and the file referent. Never a glowing or living network [wf6 originality report §D] |
| **D'ni** (*Myst*, *Riven*) | brush strokes, thick and thin, hooked Z- and 2-shaped; boxed base-25 numerals | unchanged [v1]: no pen contrast, no boxed numerals, no count above four bites and HAND |

**The look check.** Done by eye on the prototype's drawings (`figs/v2_iv6_round.png`, `v2_iv6_zoom.png`, `v2_devices.png`, `v2_new_signs.png`), on a dark page at 1,100 px and in zoomed crops.
- The round reads as a **carved cross-section of wood**: a plain heart, and carved threads running along the grain between clusters of marks, crossing over and under. It resembles no ink logogram and no ring-script above.
- **Two watch items.**
  - Long runners near the bark can read, at page size, as extra rings [call §19.2].
  - The chips' terminals are small at chart scale. They are sized for the plates (§11.5), and the plates are where roles are read.
- **Not yet done** (a builder item before anything ships): an originality pass by a fresh eye on the v2 renders, as `wf6/originality_report.md` did for v1, including a web image search for "tree ring script", "carved wood interlace glyph" and "dendroglyph writing".

---

## 16 · THE LADDER v2, AND THE THREE TABS

Each v2 device becomes glossable at one of the canon's Knowing bands (v1 §4.2). The Book draws every round whole from the start, and glosses only what is held [v1].

| Band (campaigns) | What becomes glossable in v2 (in addition to v1's column) |
|---|---|
| **K1** · one shape (1–6) | the root, by one word [v1] |
| **K2** · two shapes (7–14; the Night of the Naming, 13) | every sign, including the 47 new ones; the part device; the kind-arc; conditions; the quantity fringe (all, few, half; count) |
| **K3** · sentences and the memory (15–22) | **then** runners (v1's cross-ring ties); memory; the question; the ordinal; **cut-pockets** ("an older carving woke in us"); the time fringe (again, still, at last); **the blind**, printed as Seren's `[ ]` until K3 and then as *we do not know why* |
| **K4** · ties (23–26) | the other runner roles (to, in, with, for, because, as, through); file referents; joined piths [v1]; **braids**; **binds**; passes |
| **K5** · aim (27–31) | hollow and smoothed marks and **runners**; **breaks** ("The wood … was told to make us believe a lie, and it obeyed": a thwarting is a kind of aim); the aim place, half size and the twin [v1] |
| **K6** · a whole morrow (32) | forks and chains [v1]; **said-pockets** (a plan's words, a council's words); the manner and degree fringe (slowly, gently; only, more, most) |
| **K7** · true names (each Throne) | names in the bark [v1] |
| **K7★** · all ten | the sliver [v1]; III.2's closing ring (§11.4) |

- **Tier 3.** By the Finale every device is glossable, so every wood leaf reads whole under **Original** (§11.5), with its literal reading. The translation achievements of v1 §4.5 are unchanged: they ride these bands.
- **The three tabs** (Jack's note 3):
  - **The Book** is Halyna's telling with Seren's words as glosses;
  - **Plain Words** is the modern telling with plain glosses;
  - **Original** is the grain itself: the whole round, then the ring plates, each with the literal reading under it.
  - The grain drawing is the same in all three [v1 §4.6].

---

## 17 · THE ADMIRAL CARVINGS AND THE v1 SAMPLES IN v2

**Every one of the 46 carvings and *Burn* keeps its GN, and its meaning, exactly** (§13.7). What changes is only the drawing:

1. **Ties become carved runners** of role *to* or *then*, grown by §6.2. They are still one knife-width short of the target, and they land on its head or foot [v1 §3.7].
2. **Breadth** follows §4.5. Marks in inner rings are narrower than v1's, and the root is always the largest mark.
3. **The grain's flow** (§4.6): the ring lines yield a little round every mark.
4. **Year-hairlines** in one-year rings are no longer drawn. They were meaningless in v1, and in v2 a year-line always means a year. Empty rings and unmarked rounds keep none.
5. **Hasty saplings** are unchanged apart from the flow: one sign, from the pith, and nothing else (§3).

**Example: E2-01**, *Run the Batteries* (forty summers: "a word, and waits for its brother", one runner).

```
round E2-01 {wood: forty; pith: war; rings: 2; rules after: [1]}
  I
    r1/1  0: WAVE*
  ‖¦
  II
    r2/1  4: EDGE+BREAKER      band DREAD files 15–1
  runners
    run t1  0.r1/1   ⇒  4.r2/1
```

**Example: E4-01**, *Three roads, one hour*, with its v1 ties as v2 runners.

```
round E4-01 {wood: long; pith: war ×3; rings: 5; rules after: [2, 4]}
  I
    r1/1  p0·0: WAVE*    p1·0: WAVE*    p2·0: WAVE*
    r2/1  p0·4: EDGE+BREAKER      band DREAD files 15–1
  ‖
  II
    r3/1  0: GO    2: BOND    4: GO    12: KNOT^r4      band DREAD files 11–13
    r4/1  10: SQUARE+EYE    graft(E3-01)
  III
    r5/1  12: GO
  bark
    bark 0: BOND+TIDE
  runners
    run t0  p0·0.r1/1  ⇒  p0·4.r2/1
    run t1  10.r4/1    →  @0
    run t2  10.r4/1    ⇒  12.r5/1
    mem 10: r4 → pith
```

**The later Tides may be carved richer** [call §19.6]. The canon says what each Tide first learned (v1 §3.9); v2 gives some of those lessons their own devices. If Jack wants it, the Knowing generator may cut them where the sim's record has them:
- **the Joined Tide** (K4): its "one hull waits upon another" as *then* runners with **binds** ("the east and the north go as one");
- **Deceit** (K5): its decoys as hollow marks **and hollow runners**, and its aim as a **break** over the habit it is cut against;
- **the Last Tide** (K6): its forks drawn, and its "when the second falls, go home" as a fork with a *then* runner.

Recommended: no. The carvings' GN is settled, and v2's richer drawing alone already shows the Tides' growth.

**The v1 samples** keep their GN; their drawings become v2 renderings:
- VI-1, the sliver: unchanged but for the flow.
- NAELEAR: its ×3 takes the kind-arc.
- GIFT: its four ties become runners; §5.4's sentence stays eleven rings.
- AELTHAR: the same, plus one optional enrichment [call §19.6]. Its r6, "harm to one is harm to both", may cut its two WOUND runners as a **bind** with its out-runner to BOND:
  ```
      r6/1  15: WOUND    0: BOND    1: WOUND
    runners
      run w1  15.r6/1  →  bind K1
      run w2  1.r6/1   →  bind K1
    bind K1 w1 w2 → 0.r6/1
  ```
- STONE: its six ties become runners, and its twin stays [v1].
- GROW: unchanged; it is green wood.

---

## 18 · COVERAGE: THE EIGHT WOOD LEAVES IN THE GRAIN

Every content word of the eight leaves has a grain form. The table lists every concept that needed thought: the new signs where they are first needed, the compounds built as Seilrhass builds them, and the devices that carry what English says with small words. (Signs already in v1, such as SQUARE for wall and stone, AXE for iron and the felling, and MIST for the grey, sky and breath, are not repeated.) Leaves: A = II.2, T = III.2, X = IV.2, G = IV.4, V = IV.6, W = V.3, C = V.4, S = V.6.

| English (leaf) | Grain | Kind |
|---|---|---|
| your fathers; forebears; mothers and fathers (A, C) | `ROOT×3‿` (*ralear*) on the hearers' file | kind-arc |
| call; name; you named us (A, T) | NAME; `STONEFOLK×3+NAME →that pocket{said: …}` | new · pocket |
| lived in the wood, and the wood in us (A) | `US×3+LIVE →in TREE×3` and `TREE×3 →in @8` (the wood in us, on our file), braided `abab` | braid |
| between us was the breath (A) | the MIST band over the files between the two | [v1] |
| the Mystlands (A, the shore's word) | EARTH cut inside the MIST band, in a said-pocket of the shore-folk (a band is laid on a sign, never ligatured to it: v1's *Naelsaen* is HEART inside MIST) | new · pocket |
| air we breathed; the trees breathed out the grey (A, S) | LIVE, or TREE×3+LIVE, cut inside the MIST band: a mark in a condition's files takes the condition | [v1] |
| as sleepers breathe (A) | `→as ~LIE` (a likeness, hollow) | §10.9 |
| lay down; laid down; lay (A, G, V, S) | LIE; `>LIE` | new |
| fed; drank; the roots drank (A, V, S) | EAT; `>EAT`; `ROOT×3+EAT` | new |
| tend; as you tend a hearth (A) | TEND; hearth is BURN+HOMESTONE | new · ligature |
| softened; a gentler radiance; the between-light (A) | SOFTLIGHT; the between-light (*naelneis*) is SOFTLIGHT inside the MIST band | new |
| the open sun; hard light (A, T, X) | FLASH [v1]; the WHITE band [v1] | [v1] |
| day nor dusk; evening; at dusk (A) | FLASH; DUSK | new |
| wither; the desert (A) | DYING; SAND (*resser*, a waste of sand) | new |
| a fern of the deep forest (A) | `~LEAF` with DEEP+TREE×3: the grain's likeness | §10.9 |
| guided; led its roots to the water (A, S) | GUIDE `→` ROOT, and ROOT `→ @f`, where file f's year carries the WATER band | new |
| pruned; sang to it (A, S) | CARVE+GROW ("a cut for growing"); SING | ligature · new |
| one life, in two kinds (A, S) | LIVE, **bound**: `bind` of the two tendings | bind |
| needed; without the breath the wood sickens (A) | HAND+OPEN (need, hunger) [v1]; a year whose MIST band has a gap over the wood's file (v1: a gap in a band is meaning), with TREE×3+ROT in it | [v1] |
| the wood needed the breath … and we needed both (A) | a three-strand **braid** `abc` | braid |
| twice as long as you and half again (A) | LIVE+DEEP#2 `→as` STONEFOLK's LIVE, with `{half}` | fringe |
| the twisted boughs, our rites (A) | BEND+HULL×3; HOLY+KNEEL (rite) | ligature |
| a choir; singing at evening (A) | SING×3 in the DUSK year | [v1] ×3 |
| the silver elders; the council (A, V, C) | SILVERBARK×3; the council is SILVERBARK×3 (*neivathen*), or US×3 on its own file | new |
| no one lies under a silverbark (A) | `!` … `SQUARE+CARVE` (a lie) BENEATH SILVERBARK | ligature |
| sea; a mast holds up a sail (A) | the WATER band [v1]; `→as ~SAIL:mast` | part |
| mist-hearts; anchors of our sky (A) | HEART in MIST (*Naelsaen*) [v1]; HOLD+EARTH | ligature |
| a tongue of truth (A) | TRUE+MOUTH | new · ligature |
| storm; cracks and breaks (A) | BREAK (*rhass*) [v1] | [v1] |
| is not heard; misheard; listened (A, G, C) | `!HEAR`; `~HEAR`; HEAR | new |
| lay a hand on the carving (A) | HAND `→` CARVE | runner |
| no word could be twisted; no promise misheard (A) | `!TURN → WORD`; promise is BOND+MOUTH | new · ligature |
| sacred; binding (A) | HOLY; BOND [v1] | new |
| believed (A, X) | TRUE+HOLD ("hold true") | ligature |
| havens raised; lamps at dusk (A) | SHORE+CASTLE; `SQUARE+RISE` (build); SOFTLIGHT½×3 in the DUSK year | ligature |
| white faces; turned their faces (A, X) | `US:crown` / `STONEFOLK:crown` with the WHITE band; TURN | part |
| we did not know why (A, V, W) | the blind `→bc ∅` | blind |
| our fault (A) | SHAME | new |
| we wove the breath thicker and hid (A) | the MIST band laid over more files in the later year, with `US×3+TEND{more}` inside it; hiding is `_US×3` (smoothed) | fringe · [v1] |
| glad (A) | GLAD | new |
| came late (T) | GO `→ @0` with `{last}` | §9.2 |
| one sign to a hull (T, S) | CARVE#1 | [v1] |
| cut judgements into us slowly (T) | DEEP+CARVE (a judgement) `{slow}` | fringe |
| drew us up out of the earth (T) | EARTH `⇒ >RISE` | new |
| grew us into thrones (T) | GROW `→for` PILLAR+HULL (a throne) | ligature |
| the children lay down and could not breathe (T) | SAPLING×3+LIE; `!LIVE` | new |
| the timber of our kin in walls, beams and bridges (T) | AXE+WOOD (timber) `→in` SQUARE, BRIDGE | new |
| as mourners sit by a grave (T) | `→as ~US×3+SIT` by `~LIE+EARTH` | new · §10.9 |
| you named us for beasts; the Leviathan … the Lich (T) | NAME `→that` pocket{said: BEAST + its kind: WATER (Leviathan), HEAD×3 = `US:crown×3` (Hydra), ROT+MOUTH (Plague Herald), DEEP+TREE (Treant), GREAT+STONEFOLK (Colossus), BURN+GREAT (Magma Titan), SAND (Sandworm), WHITE band (Frost Wyrm), BREAK (Storm King), STILL (Crystal Lich)} | new · pocket |
| of the grain you call Heartoak … Silverbark (T, S) | the grain-arc [v1] + said-pocket of the shore-folk: HEART+TREE, AXE+BARK (Ironbark), DEEP+TREE (Yew), NEW:stump in the DARK band (Blackthorn), TURN+HULL (Twistbough), BEND+TREE (Willow), BURN+TREE (Ashwood), SILVERBARK | ligature · pocket |
| trade-tables, priced (T) | GIFT+TAKE (trade) | new · ligature |
| give them the middle; take the sides; close the hand (T) | a cut-pocket: `{ GIFT → HEART (the middle)  TAKE → @4 @12  CLOSE+HAND }` | pocket |
| strike one head; two will answer (T) | `STRIKE → US:crown#1`; `MOUTH#2` (answer: a runner back) | part |
| the cairn-mountain (T) | DEEP+SQUARE (*eirrhen*) [v1]; SQUARE×3 | [v1] |
| forges; black dust; iron hot (T) | BURN+HOUSE; DUST in the DARK band; AXE+ANGER (*rhes*: hot) | new |
| chase the fire; you followed (T) | SWIFT+FOLLOW; FOLLOW | new |
| galleries; the canyon; the rock over their heads (T) | ROAD+BENEATH; BENEATH+SQUARE; `OVER → STONEFOLK:crown×3` | new · part |
| hall on the frozen mere; feasted; warm (T) | GREAT+HOUSE; the mere is the STILL and WATER bands under a WHITE band on the haven's file; EAT×3; ANGER (hot) | new |
| cranes lifted the floating stones; lighter than iron (T) | `>RISE`+WOOD; SQUARE cut inside the MIST band (stones in the sky); THIN `→as` AXE `{more}` | runner |
| towers; the spire (T) | SQUARE+PILLAR | ligature |
| the great glass; cellars; one shard among a thousand (T) | GREAT+SQUARE in the STILL band (glass is still water in stone); BENEATH+HOUSE; LONE among ×3 | ligature |
| show them themselves (T) | `>EYE → @0` from file 0 (a runner that returns to its own file is *self*) | runner |
| tall and dark of bark (X) | OVER+PILLAR; BARK in the DARK band | new |
| as roots hold a bank (X) | `→as ~ROOT+HOLD` | §10.9 |
| did not think of it (X) | `!MIND` | new |
| every hull that came near, we marked (X) | HULL{all} `→ @8`; CARVE | fringe |
| each brush was a cut; the wood keeps every count (X) | HAND:palm `⇒` CARVE; HOLD+CARVE#… `{all}` | part · fringe |
| boats with many oars; waded up out of the surf (X) | HULL×3 `→with` HAND×3; STONEFOLK×3+GO cut inside the WATER band | runner |
| what one pillar felt, all the ranks felt, root to root (X) | `PILLAR@1+HOLD → {PILLAR×3{all}}` (a split runner) along ROOT×3 | split |
| summer after summer (X, T) | SUMMER{again} | new · fringe |
| pale; then pale and hard; then pale and hard and wide (X) | three years: the WHITE band over one file; WHITE and FLASH; WHITE and FLASH over five files | [v1] geometry |
| did not know why they wept (X) | WEEP `→bc ∅` | new · blind |
| the stumps put up shoots, straight and black (X) | `NEW:stump`; `NEW:shoot` TRUE in the DARK band | part |
| it came again; we put up more (X) | a **braid** `abab…!`: AXE+GO{again} and GROW{more}, until "at the last the stumps put up nothing" | braid |
| we cut our plea on the mute thing (X) | CARVE `→that` pocket{said: the plea}, and CARVE `→in` SQUARE (see the note below the table) | pocket |
| our soft letters; as near its sound (X) | WORD×3 in our own; `→as` MOUTH `{more}` | new |
| we believed every made thing speaks. A child's belief (X) | TRUE+HOLD `→that` pocket{said: CARVE{all}+MOUTH}; SAPLING+TRUE+HOLD | pocket |
| stone has no intelligence; it did not answer (X) | SQUARE+!MIND; `!MOUTH →` back to the plea | new |
| held our sap and waited (X) | HOLD `→` SAP; KNOT | new |
| the last shoot of a stump cut low (X) | `NEW:shoot{last}` from `NEW:stump`+BENEATH | part · fringe |
| the council chose us, for the axe in our rings (X) | CHOOSE; `→bc` AXE with a memory ray | new |
| as the tongue goes to a broken tooth (X) | the grain's own likeness: `→as ~HAND+GO → ~WOUND` (as a hurt hand goes to its hurt) | §10.9 |
| the world green to its edges (G) | NEW over EARTH{all}, to EDGE | new |
| the ages lay down on us as leaves lie down on leaves (G) | TIDE×3+LIE `→as ~LEAF+LIE` | new |
| grew dark and hard; not stone, though you took us for it (G) | GROW in the DARK band, `→as SQUARE` (hard as stone); `!SQUARE`; the shore's HOLD `→that` pocket{said: SQUARE} (took us for stone) | runner · pocket |
| gives slowly, and only what is so (G) | GIFT{slow}; TRUE{only} | fringe |
| a sliver; the dearest gift; given once (G) | WOOD½; GIFT{most}; GIFT#1 | fringe |
| took the name Aelrhen; his errand (G) | TAKE → NAME (BOND+SQUARE in a pocket); `>GO` | new · pocket |
| gathered their words as a child gathers fallen leaves, one and one and one (G) | TAKE#3 `→` WORD `→as ~SAPLING+TAKE → ~LEAF+FALL` | new · §10.9 |
| Stop. Sky. Dying. (G) | a said-pocket of three items: STOP; a cell with nothing cut but the MIST band laid on it (the sky); DYING | pocket |
| small words that make no sound across water (G) | WORD½×3+!MOUTH, cut inside the WATER band | new |
| while a tree's shadow moves the breadth of its own trunk (G) | HOLD over one year, `→as ~TREE:trunk`: the grain's likeness | part |
| benches, doors and walls of our wood (G) | SIT+WOOD; DOOR [v1]; SQUARE | new |
| sawn and polished (G) | AXE; SMOOTH [v1] (made smooth) | [v1] |
| laid his hand on the post and greeted them (G) | `HAND →` DOOR:… (DOOR's post: its first element, `DOOR:post`); MOUTH | part (DOOR gains `post`) |
| as one who comes under a roof brings his best (G) | `→as ~US+GO → ~BENEATH+HOUSE` with `CARRY+GIFT{most}` | new |
| take the back of the host's neck gently in his right hand (G) | `TAKE{gently} → STONEFOLK:stem` on file 4 (the right hand) | part · fringe |
| the foreheads touched in silence (G) | `US:crown/` and `STONEFOLK:crown\` leaning to meet [v1 lean] in the STILL band | part |
| a shallow cut on the host's right arm (G) | WOUND½ `→in HAND:stem` on file 4 | part |
| shoulder to shoulder; harm to one was harm to both (G) | the two ARM runners **bound** | bind |
| a foot struck us into the dust; the men laughed (G) | `STONEFOLK:foot+STRIKE →in DUST`; LAUGH | new |
| as gently as one lifts a fledgling (G) | `>RISE{gently} →as ~SAPLING½` | fringe |
| the blade went deep, for the arm was moving (G) | AXE+GO `→` DEEP, **breaking** the rite's shallow-cut runner | break |
| cried out; his men came (G) | CRY; STONEFOLK×3+GO `→ @0` | new |
| the rite half made (G) | AELTHAR{half} | fringe |
| in the morning a man came back alone (G) | MORNING; STONEFOLK+LONE+GO{again} | new |
| a chest among the mute stones (G) | CHEST among SQUARE×3 | new |
| carried up into your mountains in the arms of a child (G) | CARRY; DEEP+SQUARE×3; `→in HAND:stem×3` of SAPLING | new · part |
| proud of the name (V) | NAME+GLAD | ligature |
| a small boat of the old wood, grey and light (V) | DEEP+HULL½ in MIST | [v1] |
| threw him into us; his blood ran into our boards (V) | `>GO → @1 →in @12`; `BLOOD →in WOOD` | new |
| the old wood raged in its grief (V) | GRIEF+ANGER | ligature |
| burned higher than any fire of theirs (V) | BURN{more} `→as` their `>BURN` | fringe |
| screamed, for wood can (V) | CRY `→bc` WOOD+CRY | new |
| we turned against the current (V) | `lap e1 ⊳ f1` | break |
| the fire went out slowly as the grey closed over (V) | **braid** `abab!` | braid |
| a keel, a few ribs, the Guest's bones (V) | `BEARER:keel{only}`; BONE×3{few}; BONE×3 on the Guest's file | part · new |
| pale sand before the council-hall (V) | SAND in the WHITE band; SILVERBARK×3 | new |
| ran aground beneath the silverbarks, and were still (V) | BENEATH+LIE; the STILL band | new |
| wood can hide nothing (V) | `WOOD+!SMOOTH{all}` | fringe |
| their holiest peace answered with murder and flame (V) | HOLY+AELTHAR; `MOUTH →with >DYING`, `→with BURN` | new |
| fear leaves no mark on wood (V, G) | the blind; no sign for fear (§9.2) | blind |
| an act of war (V) | STRIKE×3 | [v1] |
| every young tree that was to be a hull drank it with the rain (V) | `SAPLING×3{all} →for HULL`; EAT `→with` RAIN | new |
| a memory, and a caution (W) | HOLD with memory ray; `EYE ⇒ BOND+HOLD` (look, then trust) | [v1] |
| where a stone flashes, a gun is (W) | a cut-pocket `{ SQUARE+FLASH ⇒ GUN }` | pocket |
| home when wounded (W) | a cut-pocket `{ STERN½ }`: the chain | pocket |
| as you two feel each other's hurt across a city (W) | `→as` a likeness: two hollow `~STONEFOLK` on two files, whose HOLD runners to each other's WOUND are **braided** `abab`, across a hollow `~CASTLE` | braid · §10.9 |
| slowly, as sap goes (W) | GO{slow} `→as ~SAP` | new |
| look before you trust (W) | a cut-pocket `{ EYE ⇒ BOND+HOLD }` | pocket |
| yesterday, today, the next coming (W) | rings and years; MORROW | new |
| lay in the cold (W) | LIE in the WHITE band | new |
| the hand behind the wall (W) | HAND on the file behind the wall's (the wall on 0, the hand on 8: v1's *behind* bearing) | [v1] |
| a hull which turns and runs draws iron after it (W) | `HULL+TURN ⇒ AXE+FOLLOW` | new |
| no roof but the boughs, no floor but the moss (C) | `!HOUSE`; HULL×3{only} OVER; MOSS{only} | new |
| like teeth from a jaw (C) | `→as ~BREATH×3` (gaps: the grain's likeness of gaps) | §10.9 |
| newborns frailer every spring; some did not wake (C) | SAPLING½×3, THIN{more}, NEW+SUMMER (spring); wake is EYE+OPEN (the eye opening), so *did not wake* is EYE+!OPEN | ligature |
| strength going out like water from a cracked jar (C) | `→as` a likeness: `~BREAK+HOLD` (a cracked cup) `⇒ ~GO` in the WATER band | §10.9 |
| counselled patience (C) | MOUTH `→that` pocket{said: KNOT …} | pocket |
| the elders rose and pleaded: Send another. Learn their words… (C) | RISE; `MOUTH? →that` pocket{said: `>GO` US@2, NEW+HOLD → WORD×3, …} | pocket |
| the young answered … (C) | MOUTH `→that` pocket{said: HEAR+LIVE#3, NEW+HOLD+WORD#3, `!HEAR`}, **breaking** the elders' plea | pocket · break |
| the vote was carried by the weight of anger and grief (C) | CHOOSE; GREAT+ANGER, GRIEF, **braided** `ab` and **breaking** the plea | braid · break |
| laid it open to the heart while it still stood (C) | OPEN `→` HEART; RISE{still} | fringe |
| *Grow until the shore is silent* (C, and every heart since) | a cut-pocket `{ GROW^…  !MOUTH+SHORE }`; the war-pith [v1] | pocket |
| went down into the moss one by one (C) | `FALL →in MOSS`, #1 … | new |
| grown, not built (S) | GROW, `!SQUARE+RISE` | ligature |
| masts from saplings trained by decades of windsong (S) | `SAIL:mast` from SAPLING; `>HOLD` (train, teach); WIND+SING | part · new |
| a leash (S) | CLOSE+BOND: a bond that closes | ligature |
| as a hand obeys the mind (S) | `→as ~HAND+HEAR → ~MIND` | new |
| balk at burning water; savage where it bled (S) | `!GO →` BURN in the WATER band; ANGER `→in` BLOOD's file | new |
| crawl on roots over sand and rock; swim burning rock in a skin of wet bark; go white in the snow (S) | GO `→with` ROOT over SAND, SQUARE; GO `→in` BURN+SQUARE `→with` BARK in the WATER band; GO in the WHITE band | new |
| four to a knot, a knot strikes as four (S) | KNOT (*lanth*) #4 `→as` STRIKE#4 | [v1] |
| bind the others' hurts with sap (S) | `BOND → WOUND →with SAP` | new |
| the winged seed ripens; the wind chooses the keep; husks (S) | SEED+GROW; `WIND+CHOOSE → CASTLE`; `~SEED×3` (hollow: husks) | new |
| hung from its own bladder (S) | SEED `→with ~HULL½` (a hollow little hull: the bladder) | §10.9 |
| no voice among us can call us home (S) | `!MOUTH → HOME` | [v1] |
| the Song of the Years (S) | seven said-pockets, SILVERBARK×3+SING `→that`, one a year | pocket |

**Two gaps closed by the table.**
- `DOOR:post` joins §5.2's parts table (the first element of DOOR: a post).
- "a plea" is `MOUTH?` (asking) with a *for* runner to what is asked. The mute stones' plea is cut as CARVE `→that` pocket{said: …}. No sign for "plea" is needed.

---

## 19 · FOR JACK (decisions only he can make)

1. **The layout of a whole leaf** (§11). Recommended: one great round per leaf, with years packed by referent, cells in the outer rings, and runners grown through the wood. The blank leaf shows the whole carving; the facing page and the Original tab give Seren's ring plates for reading.
   - The alternative: keep v1's skeleton round on the blank leaf, and show the whole carving only under Original. Not recommended. The truth rule wants the leaf's own round, and the whole round is the intricate one you asked to see.
2. **Runners' prominence** [§12.4, §15]. At page size, long runners near the bark can read as extra rings.
   - (a) Cut them in the mid tone (74%), so the marks stay the brightest thing in the round. Recommended.
   - (b) Keep them lit (97%), as every other cut.
3. **III.2's closing ring** (§11.4).
   - (a) Each Throne's heart carves its own fall as its band III; Halyna's closing is the ten told together. Recommended.
   - (b) The closing is Halyna's words with no grain under it, marked as such.
   - (c) Only the last Throne's heart holds it.
4. **The ladder** (§16). Where the new devices unlock: breaks at K5 (Deceit), said-pockets and the manner fringe at K6, braids and binds at K4. Keep, or move?
5. **"Come" has no sign** (§9.2). Every drawn COME was the mirror of FALL, which reads "not falling". The grain says *go to the one it comes to*. Keep? The alternative is a sign built on a different first mark, which would need a new drawing pass.
6. **Richer carvings for the later Tides** (§17). Recommended: no; their GN is settled. **The Aelthar's r6** as a bind: recommended yes. It is the Book's own sample, and "harm to one is harm to both" is exactly what a bind means.
7. **No sign for fear** (§9.2, §6.1). The canon's "fear leaves no mark on wood" becomes a rule of the script: the grain has the dread, but no fear. Keep?
8. **The 26 reserve roots** that the new signs read as (§9.2) enter the Seilrhass lexicon. `ancestor.md` §7, item 7, asked whether its reserve list could be adopted as it is. These are the first to be used.
9. **The kind-arc** (§5.3). *Naelear* and *Rhenear* redrawn with it. Recommended.
10. **Weight on the page** (§11.6). About 3.5 MB of grain for all eight leaves whole. The builder should load a leaf's round when the leaf opens.

---

## 20 · FILES (scratchpad only; nothing here goes into `Docs/`)

All in `wf7/grain2/`:

**Signs.**
- `signs_new.json`: the 47 new signs as data, with glosses and descent notes.
- `signs_new_compact.txt`: the JSON block of §9.3.
- `proto_signs.py`: extends wf6's sign table, read-only, with the new signs and the `punch` and `lens.across` elements, and draws the chart `chart_new.svg`.
- `compare.py`: the neighbour sheet, `chart_pairs.svg`.

**Layout and routing.**
- `proto_v2.py`: the first prototype, with full-circle sub-rings and a channel-and-gate router. It was **rejected** (§1.2). It is kept for its runner cutting, terminals, pockets and fringe, which `proto_v3.py` reuses.
- `proto_v3.py`: **the adopted layout**. It does the packing into years and cells (§4.3–4.4), the grain-following A* router with string-pulling (§6.2), passes, declared breaks crossed square, braids and binds.
  - `python3 proto_v3.py TEXT.json [-o OUT.svg] [--plate K]`
- `specimens.py`: the device specimen sheet, `specimens_v2.svg`.
- `gn2.py`: prints canonical GN v2 from a grain text (§13), with years and cells computed.

**Texts.**
- `IV-6.json`: IV.6 whole, as a v2 grain text (§12).
- `IV-6.gn2.txt`: its canonical GN v2.
- `test_devices.json`, `devices_v3.json`: device tests.
- `count_leaves.py`, `leaf_counts.json`: paragraphs, sentences and words per movement for the eight wood leaves (§11.3).

**Figures** (`figs/`):
- `v2_iv6_round.png`, `v2_iv6_zoom.png`, `v2_iv6_plate9.png`, `v2_iv6_plate5.png`;
- `v2_devices.png`, `v2_new_signs.png`, `v2_neighbours.png`;
- `rejected_full_circle_years.png`;
- `v1_gift_stone.png` (v1, for comparison).

**Shots.** `shots/` holds every intermediate screenshot. `shoot.py` and `crop.py` are the headless-Chrome helpers.

**What a production renderer must add** beyond the prototype:
- routing that never fails (§12.4);
- the one-crossing rule for breaks;
- the size optimisations (§11.6);
- `<title>` and `<desc>` states (locked, fragments, whole) [v1 §10.9];
- the plate stubs and margin tags (§11.5);
- the whole of §14.2's validator.

---

## 21 · ADDITIONS (the tier-3 coverage pass, 2026-09-27)

*The coverage pass asked by note 5 ("tier 3 on how far to take the translation"): every concept of the eight wood leaves and of every carving in the Book of Knowings, checked against the sign table and the composition rules, with a validator to keep it so. The full report is `wf7/grain_coverage.md`; the tools and the test corpus are in `wf7/coverage/`; the validator is `wf7/grain_validate.py`. Nothing here goes into `Docs/`.*

### 21.1 What was checked, and what it found

- **Words.** The eight wood leaves (II.2, III.2, IV.2, IV.4, IV.6, V.3, V.4, V.6) and the 47 carvings of the Book of Knowings (the 46 and *Burn*) hold **670 content lemmas** once the small words are set aside (`coverage/words.py`). Every one is mapped to a grain form in the concept register, `coverage/concepts.tsv` (429 rows), and every grain form there passes the validator's sign and ligature checks (`coverage/check_coverage.py`).
- **§18.** Each of its 157 rows was run through the validator. Five break the notation as written (three ligatures of three signs, two prose tokens). A reading of the rest found ten more that break a composition rule: a braid or a break across rings, runners inside a cut-pocket, a span inside a pocket, a file used as a body's hand. It found six more whose devices fall in the heart ring or band I. The ten are fixed in §21.4, and the six are answered by A9.
- **Whole rounds.** Proof rings of the seven uncarved leaves were written in GN v2 at their true ring positions, with Thaesaen's whole heart for III.2. So were all 47 carvings of the Book of Knowings, as orders in wood of their own Tide's age (E4-01 from the specs' own GN), and the Aelthar with its bind (`coverage/tests/`). All pass clean. The IV-6 GN of §12.2 raises three errors and eight order warnings; `coverage/tests/IV-6_fixed.gn2` is the corrected text (§21.4, B16).
- **No new sign was needed.** §9.1's principle held: a new sign only where a Seilrhass root is needed, and none was. The 117 signs, with 26 new compounds (§21.3) and the notation rules below, carry every concept of the eight leaves and the forty-seven carvings.
- **The one real tension** is between tier 3 and §3's plain heart: the opening paragraphs of seven leaves want the fringe, a pocket or a braid in the heart ring or band I, which §3 forbids there. It resolves without moving a word: the heart takes plain substitutes, and the fine devices stay outward (A9). This keeps Jack's "anchor in the middle … details in the outer rings" exactly.

### 21.2 Additions to the rules and the notation [rule, unless marked call]

**A1 · A band on an item, and a band alone.** Inside a pocket, and in a name in the bark, an item may carry its own condition: `EARTH[MIST]` (the Mystlands: earth inside the grey), `GREAT+BEAST[WATER]` (the Leviathan), `~HEART[STILL]` (Neivaere). A band alone, `[MIST]`, is the band laid on an empty cell, **the band as a thing**: the sky, the sea, the white. In a year, bands are still written `band X files a–b`.
- Needed by: *Stop. Sky. Dying.* (IV.4) is `pocket said { STOP  [MIST]  DYING }`; the names of v1 §3.14 that were always "inside a band" (Eirlenth, Naelthar, Neivaere, Naelsaen) had no GN until now; the fear-names and the grains in III.2's said-pockets.
- Grammar: `item = ligature, [ "[", BAND, "]" ] | "[", BAND, "]" | pocket ;` and a `bark` line takes an item.

**A2 · Inside a pocket.** A pocket has no files, so it has its own addresses and its own grammar.
- **Items are addressed `P.n`**, counted clockwise from 1: `run d3 P3.3 → P3.4`. Runners among items stay inside their pocket; nothing crosses its border (§6.3.4). No `@f` inside a pocket.
- **The doer.** Outside, an act is cut on its doer's file. Inside, a runner from a thing-item to an act-item makes the thing its doer: `{ NEW+WOOD  HOLD  WORD#1 }` with `P.1 → P.2`, `P.2 → P.3` is "the green wood holds one word".
- **Items** are separated by two spaces or a `;`. Grammar: `addr = … | pid, ".", int ;`

**A3 · Numbers above five.** v1 counts one to four in bites, and five as `X+HAND`. Ten is two hands, `X+HAND#2`; fifteen and twenty are `#3` and `#4`; beyond, many (`×3`). "The ten" of III.2's closing and V.4's "the ten havens" are `PILLAR+HAND#2` and `CASTLE+HAND#2`. Bites still stop at four, so nothing drifts toward D'ni's numerals (v1 §3.13).

**A4 · The file referent, with a ring; and the self.**
- `@f.rK/Y` ends in file f's free cell in ring K, year Y; plain `@f` means the source's own year. A to-runner may so point into a later ring (§6.3.2).
- **Files 15, 0 and 1 of the heart ring are the root's**, so no terminal may stand there (IV-6's a2 did). Point at the file in a later ring instead.
- **Where the referent is cut in that year and its cells are full, run to the mark**, not to `@f`: the terminal has no free cell to stand in (IV-6's c2, d4, d5).
- **The self.** A runner to `@f` of its own file reads *itself, themselves*: T-08's head, "Show them themselves", is `0: >EYE` with `run t 0.r3/1 → @0` (§18 used it; now it is a rule).

**A5 · The blind of place** [call §21.6]. `→ ∅`, a to-runner with a plain taper ending in empty wood at least 6 units from any mark, reads "whither, the wood does not hold". IV.2's "the shore-men took the stones away …, and we did not know where they went" is `0: CARRY` with `run e7 0.2.r8/1 → ∅`. It is told from the blind (`→bc ∅`, an empty cup) by its terminal, and glosses with it at K3.

**A6 · Idioms of the mirror, the fringe and the hollow.**

| English | Grain |
|---|---|
| never | the mirror and a memory ray: `!HEAR` + `mem` ("not, always") |
| not once | `!X#1` |
| least | `!X{most}` ("bends least": `!BEND{most}`) |
| some | `{few}` |
| own; only (in the heart) | `LONE+X` (*ith*: one, alone, own): `LONE+NAME` "our own names" |
| would have, could have, if it had | hollow: shown, not meant (`~WOUND½`, the cut he would have made) |
| either … or, and we do not know which | two questioned marks on one file, as v1's "spent, or waiting?": `GUN×3+>GO?` and `GUN×3+!EYE?` (V.3) |
| more than (in the heart) | `×3` ("more than a word was cut in us": `CARVE+WORD×3`) |

**A7 · The canonical order, completed** (§13.4 left three things open).
- **Targets that are not marks** sort thus: `@f` at file f in the source's ring and year, after that file's cells; a pocket at its first file; `∅` last in its year; `bind K` after everything in the ring.
- **Runners among a pocket's items** follow the marks of the pocket's year.
- **Token suffixes** stand in one order: `×3 ‿ ½ #n @n ^r ? / \`, then the fringe, a fork, a fold, and the root's `*` last. (§18 wrote `WORD½×3`; canonical is `WORD×3½`.)
- `gn2.py` sorts runners by (ring, knowing, file, id). It omits the cell and the target, and so prints eight of IV-6's 64 runners out of order. Since a pass reads its over-strand by this order, the printer must follow §13.4.

**A8 · Knowing form, for authors.** A leaf may be written knowing by knowing, in the telling's order, and packed by rule: `rK·i` lines (the i-th knowing of ring K) and `file[.n].rK·i` addresses (the n-th mark on that file in that knowing). `grain_validate.py --canon` lays it out by §4.3 (the same rule as `proto_v3.py`: next free cell of the file, then the next year; a pocket takes a whole year above the highest cursor among its files) and prints the canonical GN. All the proof rings in `coverage/tests/` are written so.

**A9 · The heart stays plain: substitutes** [rule; call §21.6]. §3 stands: ring 1 takes no fringe, pocket, braid, bind or break, and band I of a telling takes no pocket, braid, bind or break and at most two cells. Where a leaf's opening knowings say what those devices say, the heart cuts it plainly instead:

| In the sapwood | In the heart ring and band I |
|---|---|
| `{all}` | `×3` (many), or the band over the whole |
| `{only}` | `LONE+X` |
| `{last}` ("came late") | `DEEP+X` (*eir*: deep; old; long; **last**) |
| `{more}` ("more than a word") | `×3` |
| a said-pocket of naming ("You called it …") | a `NAME` runner to the named mark, cut on the named one's file |
| a said-pocket of taking-for ("though you took us for it") | `HOLD →as` the likeness |
| a braid of mutual acts ("in the wood, and the wood in us") | two plain runners, one each way |
| a bind ("one life, in two kinds") | two with-runners to one `LIVE#1` |
| a cut-pocket (V.3's "a caution") | the plain sign (`EYE`); the carving itself is cut whole outward |

Seven leaves need a substitute in rings 1–2: II.2 (braid; naming pocket), III.2 (`{last}`), IV.2 (`{only}`, `{all}`), IV.4 (`{all}`; the taking-for pocket), IV.6 (`{all}`), V.3 (`{more}`; the caution), V.4 (`{all}`, `{only}`). V.6's "one life, in two kinds" falls in ring 2 (band I): two with-runners. Every one is written and validated in `coverage/tests/`.

**A10 · The kind of round, and names.**
- The header may say `kind: telling | order | chip`. Otherwise:
  - a seal in the bark (`bark 0: HOLD`) makes it a telling;
  - a root among the ten line roots and *Burn* makes it an order;
  - any other root makes it a telling (GIFT, the sliver, the council's GROW);
  - no root, or `wood: plain`, makes it a chip.
- **A Throne's heart** (III.2) writes its name in the seal's cup as a second `bark 0:` line: `bark 0: HOLD` then `bark 0: TIDE+HEART`.
- **Names in an order's bark** are allowed from a long life. §3 lists names under the eldest, but E4-01, a long life, carries *Aelthae*.

**A11 · `DOOR:post`** joins §5.2's parts table, as §18 said. The validator knows it.

**A12 · Body sides are placement, never files** [call §21.6].
- **Files are the road's bearings.** File 4 is the road's right hand, never a body's, so §18's "on file 4 (the right hand)" is withdrawn.
- **Where a telling needs a body's right or left**, the placement carries it: of two people facing each other in one ring, the one on the clockwise file is on the right, as a person facing the bark stands.
- **IV.4's rite** cuts the host (file 4) clockwise of the Guest (file 1), as v1's AELTHAR r6 cuts its two wounds either side of the bond. So the host's right arm and the Guest's left meet in the bind.

**A13 · Young wood's substitutes** (orders). A Remembering carving, a shore-man's life, may not carry a long life's devices (§3), and none of its words needs them:

| Its words need | It cuts instead |
|---|---|
| *most* (E3-02 "the stone that has taken most") | the four bites, `#4` |
| *into* (E3-04 "goes into the fire") | a to-runner |
| a likeness (E3-03 "as the bough bends") | the sign that already holds it: `BEND` |
| *as though it mattered* (E3-06) | the Two Mouths' own hollow mouth, its root's signature |
| *the hidden* (E3-06) | the `DARK` band over them |
| *with all our wood* (E3-05) | the host as doer, `HULL×3+>STOP` |
| *so that* (E3-05) | a then-runner |

**A14 · "Remember" inside a pocket.** No memory ray can run from inside a pocket to the pith, so *remembered* there is `ROOT+HOLD` (*ralthein*, "root-hold", already in the lexicon). The Song's "a wall remembered in it" is `ROOT+HOLD → SQUARE`.

### 21.3 Compounds added

Each is modifier + head, as Seilrhass builds (mystaeri_spec §2.5). The soft reading is the lexicon's word where one exists, and otherwise the compound of the two soft readings by that rule (computed, not coined; call §19.8).

| Compound | Means | Soft reading | Where |
|---|---|---|---|
| `HEART+HOLD` | love; the thing loved | *saen·thein* | IV.2 "the thing it loves"; T-08 "what their hands love" |
| `TRUE+CARVE` | a law | *eiss·seth* | V.6 "the law of the years" |
| `HOUSE+OVER` | a roof | *ennas·laes* | III.2 "roofed with our kin"; V.4 "no roof but the boughs" |
| `EARTH+RISE` | a hill | *reth·thael* | E3-06 "the hill's shadow" |
| `EARTH+OPEN` | dig; the ground gives | *reth·aenn* | V.6 "walk, dig"; T-03 "when the ground gives" |
| `BURN+DUST` | ash | (*esthas*) | V.4 "come home in ashes" |
| `CARVE+US` | a carver | *sethea* | III.2, V.6 "the carvers" |
| `DEEP+US` | an elder of the long-lived | *eirea* | V.4 "the elders" (of the council, not the trees) |
| `ANGER+STONEFOLK` | an enemy (of the shore) | (*rhesea*) | V.6 "the foe" |
| `BLOOD+SQUARE` | a sister stone | *thar·rhen* | E3-02 "go to its sister" |
| `SHORE+HOUSE` | a harbour-house | *aeth·ennas* | III.2 Thaesaen |
| `TAKE+SAIL:cloth` | a net | *rhiss·reaslel* | IV.4 "at their nets" |
| `AXE+TREE:trunk` | a pole | *rhith·thael* | IV.2 "too thin to make a pole" |
| `BREAK+SAIL:cloth` | a rent in a sail | *rhass·reaslel* | IV.2 |
| `BOND+WORD×3` | a sentence | *ael·ranthen* | IV.4, V.6, III.2 |
| `DEEP+ROAD` | the long road: the far road; the old way | *eir·ves* | E4-05 "the far road"; smoothed, IV-6's hidden channels (`_DEEP+ROAD`) |
| `DEEP+PILLAR×3` | the long ranks | *eir·naelsaenen* | IV.2 |
| `OVER+SEED` | the seed aloft | *laes·veis* | V.6 |
| `THIN+MIND` | the short-minded | *iss·rener* | V.4 |
| `THIN+MOUTH` | a faint voice | *iss·renn* | V.4 |
| `THIN+ROOT×3` | the fine roots: the root-men | *issralen* | V.6 |
| `THIN{most}+SQUARE` | the weakest stone | *iss·rhen* | V.6 |
| `HAND+GIFT` | help | *vinn·vei* | IV.2, V.4 "could not help them" |
| `BARK+GO` | coming bark-first | *vath·rei* | V.6 |
| `ROOT×3+BOND` | a crowd of root-men | *ralen·ael* | V.6 "where they crowd they knot" |
| `SQUARE+WOUND{few}` | a wall left chequered | *rhen·thaess* | V.6 |
| `ROOT+HOLD` | remember (in a pocket, A14) | *ralthein* | V.6's Song |
| `LONE+X` | only X; one's own X (A6, A9) | *ith·…* | the heart rings |

The validator reads these from the block below. Compounds the validator already glosses are not repeated.

```json
{"compounds": {
 "HEART+HOLD": "v:love|loving|", "TRUE+CARVE": "n:a law|laws", "HOUSE+OVER": "n:a roof|roofs", "EARTH+RISE": "n:a hill|hills",
 "EARTH+OPEN": "v:dig|digging|", "BURN+DUST": "n:ash|", "CARVE+US": "n:a carver|carvers", "DEEP+US": "n:an elder|elders",
 "ANGER+STONEFOLK": "n:an enemy|enemies", "BLOOD+SQUARE": "n:a sister stone|sister stones", "SHORE+HOUSE": "n:a harbour-house|harbour-houses",
 "TAKE+SAIL:cloth": "n:a net|nets", "AXE+TREE:trunk": "n:a pole|poles", "BREAK+SAIL:cloth": "n:a rent in a sail|",
 "BOND+WORD×3": "n:a sentence|sentences", "DEEP+ROAD": "n:the long road (far, or old)|long roads", "DEEP+PILLAR×3": "n:the long ranks|",
 "OVER+SEED": "n:the seed aloft|", "THIN+MIND": "n:the short-minded|", "THIN+MOUTH": "n:a faint voice|faint voices",
 "THIN+ROOT×3": "n:the fine roots (the root-men)|", "THIN+SQUARE": "n:the weakest stone|", "HAND+GIFT": "v:help|helping|",
 "BARK+GO": "v:come bark-first|coming bark-first|", "ROOT×3+BOND": "n:a crowd of root-men|", "SQUARE+WOUND": "n:a wall left chequered|",
 "ROOT+HOLD": "v:remember|remembering|"
}}
```

### 21.4 Fixes (each found by the validator or by reading the spec against it)

| # | Where | Was | Now |
|---|---|---|---|
| B1 | §18, IV.2 "a child's belief" | `SAPLING+TRUE+HOLD`: three signs | `TRUE+HOLD →as ~SAPLING+HOLD` |
| B2 | §18, IV.4 "a man came back alone" | `STONEFOLK+LONE+GO{again}`: three signs | `STONEFOLK{only}+GO{again}` |
| B3 | §18, V.4 "learned three words" | `NEW+HOLD+WORD#3`: three signs | pocket items `NEW+HOLD  WORD#3`, `P.3 → P.4` (A2) |
| B4 | §18, V.4 "we listened three of their lives" | `HEAR+LIVE#3` reads "hear and live, thrice" | `HEAR →thru STONEFOLK+LIVE#3` |
| B5 | §18, II.2 "twice as long as you and half again" | `LIVE+DEEP#2`: modifier and head reversed | `DEEP+LIVE#2{half} →as STONEFOLK+LIVE` |
| B6 | §18, III.2 and IV.4 | prose tokens `HEAD×3`, "the two ARM runners" | `US:crown×3`, the two `HAND:stem` runners |
| B7 | §18, III.2 "you named us for beasts" | the fear-names as a phrase | two-sign names in a said-pocket: `GREAT+BEAST[WATER]` Leviathan, `US:crown×3+BEAST` Hydra, `ROT+MOUTH` Plague Herald, `TREE+BEAST` Ancient Treant, `GREAT+STONEFOLK` Colossus, `BURN+GREAT` Magma Titan, `SAND+BEAST` Sandworm, `BEAST[WHITE]` Frost Wyrm, `BREAK+GREAT` Storm King, `DYING+HEART[STILL]` Crystal Lich |
| B8 | §18 | the Ancient Treant and Yew were both `DEEP+TREE` | Treant `TREE+BEAST`; Yew keeps `DEEP+TREE` |
| B9 | §18, IV.4 "in his right hand … on file 4" | a bearing used as a body's hand | A12: sides by placement |
| B10 | §18, IV.4 "Stop. Sky. Dying." | "a cell with nothing cut but the MIST band": no GN | `pocket said { STOP  [MIST]  DYING }` (A1) |
| B11 | §18, V.4 "*Grow until the shore is silent*" | `{ GROW^…  !MOUTH+SHORE }`: a span has no rings inside a pocket | `pocket cut { GROW½ }`, the council's round drawn beside (§8's rule for a whole round cited) |
| B12 | §18 and §7.2, IV.2 and V.4 | braids and a break spanning rings: IV.2's `abab…!` ending at "At the last" three rings out; V.4's `aaaa` counsel "until the young break it"; "the young answered …, breaking the elders' plea" | a braid runs along one ring, and a break needs two runners that meet: IV.2 ring 6 `abab`, ring 9 `!GROW{last}`; V.4 ring 4 `MOUTH{still}`, and ring 12 cuts the elders' plea again (`6: MOUTH?{still}`) so the vote can break it (`lap w3 ⊳ w4`) |
| B13 | §18, V.3 "the hand behind the wall … the wall on 0, the hand on 8" | file 8 is home, not the far side of their wall | `STONEFOLK+HAND` on the wall's own file |
| B14 | §18, III.2 "give them the middle; take the sides; close the hand" | runners and `@4 @12` inside a cut-pocket | the Judgement cited by its root, `{ WAVE½ }`, and E5-01's round drawn beside |
| B15 | §18, IV.6 "threw him into us" | `>GO → @1 →in @12`: two roles on one runner | two runners from the one mark: `→` the dead Guest, `→in` us |
| B16 | §12.2, IV-6 | `r1/1 7: HULL×3{all}` (fringe in the heart ring); `pocket P1 cut 11–2` (eight files; at most six); `run a2 … → @0` (ends in the root's cell); c2, d4, d5 `→ @f` where the referent is cut and its cells are full; eight runners out of canonical order | `7: HULL×3‿`; `P1 cut 12–1`; `a2 → @0.r2/1`; c2 `→ 1.r3/1`, d4 and d5 `→ 12.1.r4/1`; runners reordered. The corrected text is `coverage/tests/IV-6_fixed.gn2`, and §12.2 should be reprinted from it |
| B17 | §17, E4-01 | no band-rule line after ring 4 | add `‖` before `III` |
| B18 | mystaeri_spec §5.3, AELTHAR | file 15 written before file 1 | canonical order is clockwise from 0: `1: US\    15: US/` |

### 21.5 The validator, `wf7/grain_validate.py`

Standard library only. It reads the sign table from the specs' own JSON blocks: mystaeri_spec §3.5 (70 signs), §9.3 above (47), and any `signs` or `compounds` block in this section.
- **What it does.** It parses GN v2, with every v1 form of §13.7 (ties, `slot`, the pair, the fold, the fork, trailing comments). It then checks the round and prints a reading.
- **What it checks**, by code:
  - **P** parse;
  - **H** header;
  - **S** structure and bands;
  - **M** signs, parts, fringe, ligatures of two, files, cells, packing (§4.3), the root;
  - **K** pockets;
  - **R** runners: roles against targets, direction, duplicates, `@f`;
  - **X** laps, braids and binds;
  - **A** age and place (§3, A9, A13);
  - **C** canonical order (§13.4, A7);
  - **D** the v1 devices.
- **What it leaves to the renderer's validator** (§14.2, items 3–5 and 9): gates, routes, crossing angles and the round trip through a drawing. These need geometry.
- **The readings.**
  - The plain one (default) tells the round ring by ring, as a shore-mind would tell it. A comment `# file 12: we (the Aelvaren)` names a file's referent.
  - `--literal` gives §13.5's literal reading.
  - `--canon` prints the canonical GN, packing a knowing-form text first (A8).
- **Other modes.** `--expr` checks a grain fragment, as the concept register uses. `--md` checks every GN block in a markdown file. `--selftest` and `coverage/run_tests.py` run the corpus.

### 21.6 For Jack (added to §19)

11. **A plain heart** (A9). Keep §3's rule, that no fine device stands in the heart ring or band I, by cutting the opening knowings plainly? Recommended yes. It is exactly "an anchor in the middle … details in the outer rings", and it costs no words. The alternative is to let tellings carry the fringe in band I's heart ring, which makes the heart busy.
12. **Body sides by placement** (A12)? Recommended yes. The alternative is a new device for *right* and *left*, which the grain has never needed elsewhere.
13. **The blind of place** (A5): `→ ∅` for "we did not know where". Recommended yes. The alternative is to leave "where they went" to Halyna's words, uncarved.
14. **The file referent for other roles.** §6.1 lets `@f` take only *to* and *in*. III.2's "pleaded for us" wanted `→for @12`. Recommended: keep the rule, and run to one of our marks instead, as the proof ring does.
15. **The pocket's six files.** IV-6's cited carving spans eight. Recommended: keep six and recut P1 to `12–1` (B16). Eight items fit six files at ring 9's girth.

### 21.7 Compounds added by the IV.4 pilot (the whole leaf in the grain, `wf7/pilot_IV4.md`)

*IV.4, The Gift Held an Hour, carved whole (16 rings) for tier 3. No new sign and no new rule was needed. Three compounds the leaf needs are added below, each modifier + head as Seilrhass builds (mystaeri_spec §2.5), its soft reading the compound of the two soft readings (computed, not coined; call §19.8). Without them the validator reads the ligatures part by part ("hull breaking", "being struck, old", "hold, old"), which is legal but misleading.*

| Compound | Means | Soft reading | Derivation | Where |
|---|---|---|---|---|
| `HULL+BREAK` | the thunder-tongue: Seilrhass itself, "bough-thunder" | *seil·rhass* = **Seilrhass** | HULL *seil* "a bough" + BREAK *rhass* "storm; thunder; a crack": the canon's own analysis of the name (mystaeri_spec §1, §2.9 *Seilrhass*: seil + rhass) | IV.4 ring 7, "in the thunder of his own tongue" |
| `DEEP+WOUND` | a deep wound; a cut that went deep | *eir·thaess* | DEEP *eir* "deep; old; long" + WOUND *thaess* "struck; the bark splits" | IV.4 ring 12, "went deep" (the proof ring's `4: DEEP+WOUND`) |
| `DEEP+HOLD` | hold long; keep long | *eir·thein* | DEEP *eir* "long" + HOLD *thein* "hold; know" (beside ROOT+HOLD *ralthein*, remember) | IV.4 ring 14, "No one held us so long, until you" (`0: DEEP+HOLD{only}`: only you held us long) |

```json
{"compounds": {
 "HULL+BREAK": "n:the thunder-tongue (Seilrhass, bough-thunder)|",
 "DEEP+WOUND": "n:a deep wound|deep wounds",
 "DEEP+HOLD": "v:hold long|holding long|"
}}
```

### 21.8 Additions from the IV.4 blind back-translation (`wf7/backtrans_IV4.md`)

*IV.4's round (§21.7) was read back into English blind, from its GN alone, with this spec, the validator and the Orrowen tools, and then compared with the Book. Of its sixteen rings, two kept every proposition, twelve came back close, and two drifted. Ring 5 drifted because two of its readings live only in the concept register. Ring 15 drifted by design: its sentence is a cited round that was not part of the test. The register gap was the spec's, and so was a clash between §10.3 and §11.2 that made the validator's reading lose track of who stands on a file. Both are fixed here.*

**A15 · Readings a decoder needs from the register.** The concept register (`coverage/concepts.tsv`, shown as `coverage/register.md`) maps every lemma of the leaves to a grain form, and most of its readings are simply a sign's own gloss. The readings below are not. A decoder given only this spec, as §14.3's blind decoder is, reads them wrongly, so they continue A6 here.

| English | Grain | Where |
|---|---|---|
| forget; be forgotten | `!HOLD`: to know is to hold, so to forget is to hold no longer | IV.4 r1, "until time forgot us" (`TIDE×3+!HOLD →` us) |
| not forget; still know | `HOLD{still}` | IV.4 r2, "does not itself forget" |
| let go (of what is held) | `!HOLD →` the thing held; hollow, `~!HOLD`, when the letting go was only meant | IV.4 r9, "and let go the neck" |
| enough | `{all}`: all that was needed. On a hollow mark it reads "would have been enough" | IV.4 r5, "the shape would have been enough" (`~CARVE{all}`) |
| the shape of a knowing (what one touch takes of it, without its words) | `CARVE`: the cut | IV.4 r5, "one of you alone holds only the shape" (`CARVE{only}`) |
| polished; made smooth | `SMOOTH`, as a mark in a telling (as a line root it still reads "go veiled") | IV.4 r6, "sawn and polished" |
| greet | `MOUTH`, to the one greeted | IV.4 r6 |
| draw back | `HAND:stem+TURN`: the arm turning aside | IV.4 r11 |

Any register reading that is not its sign's own gloss belongs in this table. The register is the builder's tool; this spec is what the reader has.

**A16 · A belonging does not introduce a referent** [rule; §11.2 read with §10.3]. §11.2 says that a new thing-sign standing first on a file introduces a new referent there. §10.3 says that a thing is cut on the file of the one it belongs to. When the first thing on a file in a ring is a **belonging** of the referent already there, §10.3 wins and the referent stands. The belongings are:
- a part (`SIGN:part`: a brow, a neck, a foot, an arm), unless the ligature is a named compound (`TAKE+SAIL:cloth`, a net);
- a person's mind, word or words, name, breath, hand, eye, bones and blood: `MIND`, `WORD` and every compound headed by it (a true word, `TRUE+WORD`; a sentence, `BOND+WORD×3`), `NAME`, `BREATH`, `HAND`, `EYE`, `BONE`, `BLOOD` (but `BLOOD×3`, kin, is a referent of its own);
- the dust at a place, `DUST`;
- a built place's doors and stones: `DOOR` and `SQUARE` on the file of a `CASTLE` or a `HOUSE`.

Read by §11.2 alone, IV.4's files lost their referents:
- file 12 (we) became "a sentence" from ring 5;
- the Guest's file became "mind" from ring 8;
- the shore's file became "three words", then "a shore-man's foot";
- the host's file became "an arm" and "a shore-man's neck";
- the hold's file became "dust".

The validator's reading now follows A16 (`is_belonging`). A round with no `# file` comments keeps the Guest, the host, the hold and the teller on their files through the whole leaf. A `# file` comment still names a referent the wood cannot show: like the plates' tags, it is Seren's apparatus (§11.5).

**A split runner is not "when."** A split (§6.1) says that one act reached several things at once: one taking of the name and of the errand. It does not order them in time. Time between clauses is carried by *then* runners and the span (§6.5). IV.4's ring-3 note said otherwise, and has been corrected.

### 21.9 Additions from the wf8 units, merged (tier 3, the whole Book; 2026-09-28)

*The wf8 workflow carved every wood leaf whole (II.2, III.2, IV.2, IV.6, V.3, V.4, V.6: units W01–W07; IV.4 is the pilot, §21.7) and the grain inside the stone leaves (V.7: S09; VI.1 and the Epilogue: S10; the 47 carvings of the Book of Knowings: S11), each unit writing its grain additions to its own file under the concurrency rule (`wf8/additions/*_grain.md`). This section merges them, harmonised: one compounds table and **one** compounds block for the validator, one table of decoder readings, the rules the units proposed, and the corrections and findings. Where two units said different things of one form, one is chosen here and the unit that used the other was re-cut (§21.9.7). The unit files stay as the record of each unit's reasoning. Nothing here goes into `Docs/`.*

#### 21.9.1 What was merged

- **No new sign.** No unit needed one; §9.1's principle held for the whole Book.
- **53 compounds** from 8 units (S10, W01, W02, W03, W04, W05, W06, W07), 56 rows as written: 2 were proposed by more than one unit, always with the same gloss (`BENEATH+SIT` by W01, W02 and W06; `OVER+HULL×3` by W01 and W06), so no compound conflict had to be settled. None repeats a compound the validator already glosses or §21.3/§21.7 add.
- **75 decoder readings** (A15, continued, §21.9.3), merged from the units' tables: rows that said one thing twice are one row; three pairs that said different things of one form are settled in A17 and §21.9.7.
- **Rules proposed** by the units are gathered in §21.9.4, marked *[proposed]* where the validator does not yet read them, and **[Jack]** where they are calls.

#### 21.9.2 Compounds added by the wf8 units

Each is modifier + head, as Seilrhass builds (mystaeri_spec §2.5); its soft reading is the compound of the two soft readings (computed, not coined; call §19.8). Keys follow the validator's `lig_key` (every decoration but a part and ×3 is ignored).

| Compound | Means | Soft reading | Derivation | Where | Unit |
|---|---|---|---|---|---|
| `THIN+LIVE` | breathe thin; the breath grown thin | *iss·ilae* | THIN *isseil* "thin wood; thin" (as modifier *iss-*) + LIVE *ilae* "live; breathe" | VI.1, *The Two Homes* line 3 (the chip `VI-1-twohomes`, r2): "and the breath grew thin", cut inside the MIST band on the trees' file | S10 |
| `DEEP+TREE×3` | the deep forest; its depths | *eir·thaelen* | DEEP *eir* "deep" + TREE×3 *thaelen* "trees, a grove" | II.2 ring 10, "each deep of the forest" (`DEEP+TREE×3{all}`) | W01 |
| `BEND+HULL×3` | the twisted boughs (the wood's own name for the rite-trees) | *seil·seilen* | BEND *seil* "bend as a bough bends" + HULL×3 *seilen* "boughs" | II.2 ring 8, "The twisted boughs we bent in our rites" | W01 |
| `OVER+HULL×3` | the high boughs | *laes·seilen* | OVER *laes* "over, above; high" + HULL×3 *seilen* | II.2 ring 10, "as the storm speaks in the high boughs"; V.4 ring 1, "no roof but the boughs" | W01, W06 |
| `HOLD+EARTH` | anchor: hold (a thing) to the earth | *thein·reth* | HOLD *thein* "hold" + EARTH *reth* "earth, ground" | II.2 ring 9, "held the breath to the earth", "the anchors of our sky" | W01 |
| `HOLD+PILLAR` | a mist-holder: the shore's name for a black pillar (*Mystholder*), said in its pocket with `[MIST]` | *thein·naelsaen* | HOLD *thein* + PILLAR *naelsaen* | II.2 ring 9, "You call them the Mystholders" (`{ HOLD+PILLAR[MIST] }`) | W01 |
| `BENEATH+LIE` | lie (flat) beneath; lie aground | *senn·rhir* | BENEATH *senn* "beneath" + LIE *rhir* "lie down; lie; (register) flat, laid along the ground" | II.2 ring 3, "Our land lay flat beneath the trees" | W01 |
| `LIE+TREE×3` | the flat wood: the wood laid along the ground | *rhir·thaelen* | LIE *rhir* ("flat: laid along the ground", register) + TREE×3 *thaelen* | II.2 ring 14, "the flat wood under the grey" | W01 |
| `BENEATH+SIT` | sit beneath | *senn·rass* | BENEATH *senn* + SIT *rass* "sit; take one's seat" | II.2 ring 8, "Under the silver elders the council sat"; III.2 Thaesaen, "We sat beneath Eldhythe's harbour"; Leavaren, "beneath the three spans"; V.4 ring 1, "Our council sat under the silver elders" | W01, W02, W06 |
| `EDGE+EYE` | watch from the edge | *enth·neas* | EDGE *enth* "an edge; the rim of the grey" + EYE *neas* "an eye; to look" | II.2 ring 12, "From the edge we watched your shore" | W01 |
| `LONE+MOUTH` | one's own tongue; its own voice | *ith·renn* | LONE *ith* "one, alone, own" (A6) + MOUTH *renn* "a voice; a tongue" | II.2 ring 10, "each deep of the forest speaks it its own way" | W01 |
| `BREAK+MOUTH` | speak in thunder: the storm's speaking, in cracks and breaks | *rhass·renn* | BREAK *rhass* "storm; thunder; a crack" + MOUTH *renn* | II.2 ring 10, "as the storm speaks" (the likeness, cut hollow: `~BREAK+MOUTH`) | W01 |
| `EDGE+PILLAR×3` | the pillars at the edge (of the world) | *enth·naelsaenen* | EDGE *enth* + PILLAR×3 *naelsaenen* | II.2 ring 14, "the black pillars at the edge of the world" | W01 |
| `TREE×3+LEAF` | a forest-leaf; a fern of the forest floor (cut hollow, the grain's likeness) | *thaelen·lel* | TREE×3 *thaelen* + LEAF *lel* "a leaf" | II.2 ring 4, "as it withers a fern of the deep forest" (`~TREE×3+LEAF`) | W01 |
| `DEEP+GO` | come late; go at the last; go long after | *eir·rei* | DEEP *eir* "deep; old; long; **last**" + GO *rei* "go". It is A9's own substitute for `GO{last}` ("came late", §18) in band I, given its reading | III.2 band I ring 1, "We came late"; Neivaere's ring 7, "We came long after" | W02 |
| `BENEATH+RISE` | come up from beneath | *senn·thael* | BENEATH *senn* + RISE *thael* "rise, stand" | III.2 Senneir, "We came up beneath" (its Judgement T-04 cuts `BENEATH+GO` and `RISE` apart) | W02 |
| `CARVE+SQUARE` | a carved stone: a stone that bears a carving | *seth·rhen* | CARVE *seth* "a cut, a carving" + SQUARE *rhen* "stone". Not the lie, `SQUARE+CARVE` (*rhen·seth*, "a cut that carries nothing"): the order is the meaning, modifier inward | III.2 Thaesaen, "the stones that pleaded for us" (the plea the wood cut in the mute stones, IV.2) | W02 |
| `RISE+WOOD` | a crane: a lifting-wood | *thael·veir* | RISE *thael* (with the causative, `>RISE`, "raise") + WOOD *veir*. §18 already gives it ("cranes … `>RISE`+WOOD"); only its reading is added | III.2 Naelthar, "the cranes that lifted the floating stones" | W02 |
| `BREAK+SQUARE` | a shard; a broken stone (in the STILL band, a shard of glass) | *rhass·rhen* | BREAK *rhass* "break; a crack" + SQUARE *rhen* "stone". Replaces the register's `SQUARE½{only}[STILL]` for a shard: outside a pocket a half-size line root reads as a **cited carving** (§8), so `SQUARE½` is the Mute Square cited, not a small stone | III.2 Neivaere, "among the broken glass, one shard among a thousand" | W02 |
| `THIN+NEW` | a thin green thing; a thin young shoot | *iss·lea* | THIN *isseil* "thin wood" (compound form *iss-*) + NEW *lea* "new; young; green" | IV.2 ring 10, "a thin green thing with the whole of the axe in its rings" | W03 |
| `BENEATH+NEW:stump` | a stump cut low | *senn·lea* | BENEATH *senn* "beneath; low" + NEW:stump (the part: a stump; NEW *lea*), as BENEATH+HOUSE is a cellar and BENEATH+SQUARE a canyon | IV.2 ring 10, "the last shoot of a stump cut low where the iron first went in" (corrects §18's `NEW:stump+BENEATH`, which puts the head inward: modifier inward, head outward, §10.2) | W03 |
| `AXE+LOSE` | a blade that slips; the blade let slip | *rhith·naenn* | AXE *rhith* "iron; the blade" + LOSE *naenn* "lose; let slip" (the register's "the blade that slipped" is LOSE with AXE; inside a cut-pocket no runner may join them, so it is the ligature) | IV.6 ring 9, the keel's cut-pocket: "the blade that slipped" | W04 |
| `EARTH+EDGE` | the edge of the world (with `{most}`: its far edge) | *reth·enth* | EARTH *reth* "earth; the world" + EDGE *enth* "edge; end; outer" | IV.6 ring 11, "to the far edge of the world" (`10: EARTH+EDGE{most}`) | W04 |
| `BURN+WOOD` | charred wood: wood the fire has had | *esth·veir* | BURN *esth* "burn; fire; char" + WOOD *veir* "wood" (beside `BURN+TREE`, Ashwood, a name, and `BURN+DUST`, ash) | IV.6 ring 5, "Even charred … the wood" (`14: BURN+WOOD`) | W04 |
| `LONE+BEARER` | the bearer ahead; the bearer going before the rest | *ith·varen* | LONE *ith* "one goes ahead of the rest" (its line-root gloss) + BEARER *varen* "a bearer; a laden hull" | V.3 ring 1, "and the bearer ahead" | W05 |
| `LONE+GO` | go ahead; go out in front of the rest | *ith·rei* | LONE *ith* "one goes ahead of the rest" + GO *rei* "go": the Lone Stroke's own act (*Go until struck*; *One goes; the rest follow the quiet*) | V.3 ring 7, "we went out in front" | W05 |
| `BENEATH+WOUND` | a low wound; struck low, under the water-line | *senn·thaess* | BENEATH *senn* "beneath; low" + WOUND *thaess* "struck; the bark splits" (as DEEP+WOUND *eir·thaess*, §21.7) | V.3 ring 2, "the iron went into us low and through" | W05 |
| `SQUARE+BENEATH` | the lee of a stone; the low, sheltered side of a wall | *rhen·senn* | SQUARE *rhen* "stone; the wall" + BENEATH *senn* "beneath; low; the lee" (the register's own reading of BENEATH for "in the lee of that stone"). Distinct from BENEATH+SQUARE (the canyon, head and modifier the other way) | V.3 ring 8, "we went down in the lee of that stone" | W05 |
| `MORROW+HULL×3` | the next hulls: the hulls of the next coming | *leis·seilen* | MORROW *leis* "the morrow; the next coming" + HULL×3 *seilen* "hulls" | V.3 ring 9, "the groves where the next hulls stood growing" | W05 |
| `BEARER+HEART` | the bearer's heart (a heart as a referent of its own, the bearer's) | *varen·saen* | BEARER *varen* "a bearer; a laden hull" + HEART *saen* "a heart; heartwood". Added after the blind back-translation (`wf8/backtrans/W05.md`): a plain `HEART` standing first on the bearer's file introduces "a heart" there by §11.2 (A16 does not list the heart as a belonging), so the bearer was lost from rings 6–7 | V.3 ring 6, "quickest to the heart of the bearer, and from the heart to all" | W05 |
| `BREAK+HOLD` | a cracked cup; a cracked jar | *rhass·thein* | BREAK *rhass* "break; crack" + HOLD *thein*, whose sign is the Cup (§9.1, the Cup family). §18 already gives the jar as "`~BREAK+HOLD` (a cracked cup)", and the concept register has it (*jar*), but the validator had no gloss | V.4 ring 3, "like water from a cracked jar" (`6: ~BREAK+HOLD ⇒ 6: ~GO` in the WATER band, hollow: a likeness) | W06 |
| `LIVE+GO` | life going out; strength ebbing | *ilae·rei* | LIVE *ilae* "to live; to breathe; life" + GO *rei* "go": the thing that goes, then the going, as `BLOOD+GO` (blood flowing, IV.4). The register's own reading of *strength* ("their strength going out of them": life going out) | V.4 ring 3, "their strength going out of them" | W06 |
| `AXE+GO` | the iron coming; the felling going on | *rhith·rei* | AXE *rhith* "iron; the felling" + GO *rei*. The grain has no *come* (§9.2): the iron's coming is its going. IV.4's `AXE+GO` ("the blade goes") reads the same | V.4 ring 4, the counsel: "The iron comes seldom now" (`AXE+GO{few}`) | W06 |
| `AXE+STOP` | the iron stopping; the felling ended | *rhith·rheil* | AXE *rhith* + STOP *rheil* "stop" | V.4 ring 4, the counsel: "when the iron stops"; ring 14, "the iron stopped coming to the edge" (the counsel's own words come true, one mark for both) | W06 |
| `LONE+MOSS` | only the moss; the moss alone | *ith·rheth* | LONE *ith* "one, alone; only" + MOSS *rheth*. A9's heart substitute for §18's `MOSS{only}` (the heart ring takes no fringe), after `LONE+X` (§21.3) | V.4 ring 1, "and no floor but the moss" | W06 |
| `OPEN+HAND×3` | open hands; hands held out, hiding nothing | *aenn·vinnen* | OPEN *aenn* "open" + HAND×3 *vinnen* "hands". Modifier OPEN, head HAND, so it is told from the v1 `HAND+OPEN` (need, hunger: a hand that opens to take) | V.4 ring 9, "went down to the shore with our hands open" | W06 |
| `STRIKE×3+CARVE` | a carving of war; a war-carving | *thassen·seth* | STRIKE×3 *thassen* "blows: war" (v1 table) + CARVE *seth* "a carving". Read as a thing, so a file on which it stands first holds the carving | V.4 ring 13, "the first carving of the war" (`STRIKE×3+CARVE@1`); ring 15, "The carving did not go down with them" | W06 |
| `NEW+SILVERBARK` | a young silverbark | *lea·neivath* | NEW *lea* "new; young; green" + SILVERBARK *neivath* | V.4 ring 13, "the straightest of the young silverbarks" | W06 |
| `ANGER+SAPLING×3` | the angry young | *rhes·leathaelen* | ANGER *rhes* "anger; hot" + SAPLING×3 *leathaelen* "saplings; children; the young". The head is the young, so the mark keeps the young on their file (§11.2), as `THIN+MIND` names the short-minded by their head. It is told from `ANGER+STONEFOLK` (*rhesea*, an enemy, §21.3), whose head is the shore-man. *Back-translation fix (`wf8/backtrans/W06.md`):* the leaf first cut a lone `ANGER` here, which by §11.2 names anger itself as file 5's referent, because A16 lists no feeling among the belongings. So the blind reading lost the young | V.4 ring 11, "But war is for the short-minded and the angry young" | W06 |
| `DEEP+HULL×3` | the deep hulls: the deep-laden hulls that carry the root-men | *eir·seilen* | DEEP *eir* "deep" + HULL×3 *seilen* "hulls" (beside IV.6's `DEEP+HULL½`, a small boat of the old wood, which stays as it is) | V.6 ring 14, "They ride in the deep hulls" | W07 |
| `GREAT+HULL` | a broad hull (a crown-hull); the broad hulls | *rhann·seil*; *rhann·seilen* | GREAT *rhannseil* "the great hull" (*rhann* + *seil*) + HULL *seil*: the ligature spells GREAT's own word out as a broad hull, *rhannseil* | V.6 rings 17–19, "The broad hulls hang back" | W07 |
| `GREAT+HULL×3` | a broad hull (a crown-hull); the broad hulls | *rhann·seil*; *rhann·seilen* | GREAT *rhannseil* "the great hull" (*rhann* + *seil*) + HULL *seil*: the ligature spells GREAT's own word out as a broad hull, *rhannseil* | V.6 rings 17–19, "The broad hulls hang back" | W07 |
| `SUMMER+HULL` | a hull of one season (with `#1`); a hull of summers | *ses·seil* | SUMMER *ses* "summer; (#1) one season" + HULL *seil* | V.6 ring 9, "a hull of one season holds one sign" (`SUMMER#1+HULL`) | W07 |
| `SUMMER×3+HULL` | a hull of many summers (of forty summers) | *sesen·seil* | SUMMER×3 *sesen* + HULL *seil*, beside the validator's `SUMMER×3+WOOD` | V.6 ring 9, "of forty summers, a phrase" | W07 |
| `NEW+HULL×3` | green hulls: the crude, young-wood hulls (with `{most}`, the crudest) | *lea·seilen* | NEW *lea* "new; young; green; crude" + HULL×3 | V.6 ring 9, "So the crudest came first" | W07 |
| `GREAT+GO` | go heavy; the heavy going | *rhann·rei* | GREAT "great; heavy" (the register's *heavy*) + GO *rei* | V.6 ring 8, Ironbark "comes again heavier" (`GREAT{more}+GO{again}`); ring 14, "the heavy slowly" (`GREAT+GO{slow}`) | W07 |
| `THIN+GO` | go light; the light going | *iss·rei* | THIN *isseil* "thin; light, not heavy" (W04's A15 reading) + GO | V.6 ring 14, "the light pouring" (`THIN+GO{all}`: all going at once) | W07 |
| `SWIFT+GROW` | grow quickly (with `{most}`, quickest) | *leas·thae* | SWIFT *leas* "swift; quick; soon" + GROW *thae* | V.6 ring 10, "young wood grows quickest" | W07 |
| `OVER+GO` | go over; go high (the seed over the walls, the seed in the high air) | *laes·rei* | OVER *laes* "over, above; high" + GO | V.6 ring 17, "over your walls"; ring 19, "It rides the high air" | W07 |
| `OVER+ANGER` | the heat above; a hot sky | *laes·rhes* | OVER *laes* + ANGER *rhes* "anger; hot" | V.6 ring 17, "the hot sky over your guns" | W07 |
| `LONE+LIVE` | its own life; one's own life | *ith·ilae* | LONE *ith* "one, alone, own" (A6) + LIVE *ilae* | V.6 ring 18, "The seed is the hull's own life" (the bind's out-runner) | W07 |
| `LONE+CARVE` | its own grain; its own carving | *ith·seth* | LONE *ith* "own" + CARVE *seth* (the register's *grain*, outside names) | V.6 ring 7, "Each hull keeps its own grain" | W07 |
| `ROOT+BOND` | a knot of root-men (with `#4`, a knot of four) | *ral·ael* | ROOT *ral* + BOND *ael*, beside §21.3's `ROOT×3+BOND`, a crowd | V.6 ring 15, "four to a knot" (`ROOT#4+BOND`) | W07 |

The validator reads these from the one block below.

```json
{"compounds": {
 "THIN+LIVE": "v:breathe thin (the breath grown thin)|breathing thin|",
 "DEEP+TREE×3": "n:the deep forest (its depths)|",
 "BEND+HULL×3": "n:the twisted boughs|",
 "OVER+HULL×3": "n:the high boughs|",
 "HOLD+EARTH": "v:anchor (hold to the earth)|anchoring|",
 "HOLD+PILLAR": "n:a mist-holder (the shore's Mystholder)|mist-holders",
 "BENEATH+LIE": "v:lie (flat) beneath|lying (flat) beneath|",
 "LIE+TREE×3": "n:the flat wood (laid along the ground)|",
 "BENEATH+SIT": "v:sit beneath|sitting beneath|",
 "EDGE+EYE": "v:watch from the edge|watching from the edge|",
 "LONE+MOUTH": "n:its own tongue (voice)|own tongues",
 "BREAK+MOUTH": "v:speak in thunder (the storm's voice)|speaking in thunder|",
 "EDGE+PILLAR×3": "n:the pillars at the edge (of the world)|",
 "TREE×3+LEAF": "n:a forest-leaf (a fern of the forest floor)|forest-leaves",
 "DEEP+GO": "v:come late (go at the last, or long after)|coming late|",
 "BENEATH+RISE": "v:come up from beneath|coming up from beneath|",
 "CARVE+SQUARE": "n:a carved stone (a stone that bears a carving)|carved stones",
 "RISE+WOOD": "n:a crane (a lifting-wood)|cranes",
 "BREAK+SQUARE": "n:a shard (a broken stone)|shards (broken stones)",
 "THIN+NEW": "n:a thin green thing (a thin young shoot)|thin green things",
 "BENEATH+NEW:stump": "n:a stump cut low|stumps cut low",
 "AXE+LOSE": "n:a blade that slips (the blade let slip)|blades that slip",
 "EARTH+EDGE": "n:the edge of the world|the edges of the world",
 "BURN+WOOD": "n:charred wood|",
 "LONE+BEARER": "n:the bearer ahead (going before the rest)|bearers ahead",
 "LONE+GO": "v:go ahead (out in front of the rest)|going ahead|send ahead",
 "BENEATH+WOUND": "n:a low wound (struck low, under the water-line)|low wounds",
 "SQUARE+BENEATH": "n:the lee of a stone (its low side)|the lees of stones",
 "MORROW+HULL×3": "n:the next hulls (of the next coming)|",
 "BEARER+HEART": "n:the bearer's heart|",
 "BREAK+HOLD": "n:a cracked cup (a jar)|cracked cups",
 "LIVE+GO": "n:life going out (strength ebbing)|",
 "AXE+GO": "n:the iron's coming (the felling going on)|",
 "AXE+STOP": "n:the iron's stopping (the felling ended)|",
 "LONE+MOSS": "n:only the moss (the moss alone)|",
 "OPEN+HAND×3": "n:open hands (held out)|",
 "STRIKE×3+CARVE": "n:a carving of war|carvings of war",
 "NEW+SILVERBARK": "n:a young silverbark|young silverbarks",
 "ANGER+SAPLING×3": "n:the angry young|",
 "DEEP+HULL×3": "n:the deep hulls (deep-laden, that carry the root-men)|",
 "GREAT+HULL": "n:a broad hull (a crown-hull)|broad hulls",
 "GREAT+HULL×3": "n:the broad hulls (the crown-hulls)|",
 "SUMMER+HULL": "n:a hull of summers (with one: of one season)|hulls of summers",
 "SUMMER×3+HULL": "n:a hull of many summers (of forty summers)|",
 "NEW+HULL×3": "n:green hulls (crude, of the young wood)|",
 "GREAT+GO": "v:go heavy|going heavy|",
 "THIN+GO": "v:go light|going light|",
 "SWIFT+GROW": "v:grow quickly|growing quickly|",
 "OVER+GO": "v:go over (go high)|going over|",
 "OVER+ANGER": "n:the heat above (a hot sky)|",
 "LONE+LIVE": "n:its own life|own lives",
 "LONE+CARVE": "n:its own grain (its own carving)|own grains",
 "ROOT+BOND": "n:a knot of root-men|knots of root-men"
}}
```

#### 21.9.3 A15, continued: readings a decoder needs from the register

A15's standing rule: any register reading that is not its sign's own gloss belongs in this table. These are the readings the whole-leaf carvings rely on, merged from the units' tables (W01–W07, S09) and harmonised; the Where column names the leaf and ring.

| English | Grain | Where |
|---|---|---|
| answer; did not answer | `MOUTH` / `!MOUTH` with a runner back to the one who spoke or cut | II.2 r8 "and they answered"; IV.2 r8 "It did not answer" |
| the world; measureless | `EARTH{all}`: all the earth | II.2 r3, r7 |
| the edge of the world (with `{most}`: its far edge) | `EARTH+EDGE` (compound, §21.9.2); "measureless, to the far edge of the world" is `EARTH{all}` with it | IV.6 r11; II.2 r3 |
| flat (laid along the ground) | `LIE` as a modifier: `BENEATH+LIE`, `LIE+TREE×3` | II.2 r3, r14; III.2 Leavaren ("laid flat") |
| must not be mistaken; a knowing that cannot be turned | `!TURN+HOLD`, "a holding not turned" (§18's "no word could be twisted" is `!TURN →` WORD). **Not** `!~HOLD`: see A17 | IV.2 r7; II.2 r11 |
| not mishear (no promise misheard) | `!TURN+HEAR`, "a hearing not turned", the same shape as `!TURN+HOLD`. **Not** `!~HEAR`: see A17 | II.2 r10 |
| make sure (of it) | `>TRUE`, make it true (the validator reads "are true": §21.9.6) | II.2 r13 |
| not leave out; keep (a fault, a debt) | `!LOSE`, not let slip | II.2 r13 |
| as a branch breaks | `~HULL+BREAK` as a likeness, read by its parts: a bough's break; it is also the name of the thunder-tongue (*seil·rhass*), which is the pun | II.2 r11 |
| for the moment … for always | a count of one on the act (`MOUTH#1`, said once) against a memory ray on what it made (always) | II.2 r11 |
| if any … is left, then … | a questioned mark with `{few}` and a *then* runner from it, where no ring is left for a fork (`NEW?{few} ⇒ HOLD`) | II.2 r14 |
| heavy (to carry); go heavy | `GREAT` on the carried thing's file (the validator glosses GREAT "great hull", its v1 hull sense); of a going, `GREAT+GO` | III.2 band I r6; V.6 r8, r14 |
| light (not heavy); go light | `THIN`; of a going, `THIN+GO` | IV.6 r2; V.6 r14 |
| close the hand (a Judgement's own act, E5-01) | `HAND+CLOSE`, which the validator glosses "the kept hand" (E4-03's sense) | III.2 Thaesaen |
| what was seen, the wood does not hold | `EYE → ∅`: A5's blind of place read by its role ("whither" for a going, "what" for a seeing) | III.2 Neivaere |
| put beneath; drive down (piles) | `>BENEATH` (the validator's causative gloss); the register's `>FALL` reads "fell" | III.2 Vaelress |
| once there were no tricks | `DEEP+WOOD` with `TRUE{all}`: the old wood, wholly true | III.2 Esthaer |
| a trick; never the same trick twice | a hollow going, `~GO` (shown, not meant); "never plays one trick twice" is `~GO#1{only}` with a memory ray (always): one trick, once only. **Not** `!~GO#2`: see A17 | III.2 Esthaer (`~BURN`); V.6 r8 (Twistbough) |
| wait for, hope for (what has not come) | the *for* runner to the awaited thing, **cut hollow** (A6): `KNOT →for ~X`. A *for* target cut whole reads as a thing that happened | III.2 band I r2 |
| hard to look upon (too bright to face) | `FLASH`, hard light, on the one looked upon; `FLASH →as` another's FLASH is "and so were we" | III.2 Neivaere |
| hasty; crude, crudest | `NEW` (*lea*: green, young; the Hasty Tide's own syllable); `NEW{most}`, the crudest | III.2 band I r1; V.6 r9 |
| wrong, harm ("most wronged") | `STRIKE`, with the fringe for degree: `STRIKE{most}` | III.2 band I r5 |
| go home; go away (behind); leave | `GO → @8`: file 8 is behind, home, the other side (the register's *away*, *leave*) | IV.2 r13; V.7 III r4 (`HULL×3+GO →` HOME on file 8) |
| not go home; not go away, will not leave | `!GO → @8`. Its gloss follows the doer: the axe in our grain "will not leave it" (IV.2 r13); the hull carried out to sea does not go home, "away from home" (IV.6 r4); the felled hull's seed has "no crown to come home to" (V.6 r18). One reading, not going to file 8 | IV.2 r13; IV.6 r4; V.6 r18 |
| cannot help it (a thing done by the grain, not by choice) | `!STOP →bc` its cause | IV.2 r12 |
| as near as could be to (a likeness) | `→as` the hollow likeness with `{most}`: `→as ~MOUTH{most}` | IV.2 r8 |
| were grey (grew old) | `DEEP+LIVE`, a long life, after a *then* runner | IV.2 r4 |
| until it is taken (a loss with no taker named) | `~LOSE` (or `LOSE`) on the loser's own file, after a *then* runner. Not TAKE there: an act stands on its doer's file (§10.3) | IV.2 r1 |
| did not know why (another did not know the cause of an act) | `!HOLD →in` the act, the act cut whole beside its blind `→bc ∅`: the act is known; what is not held is *in* it, its cause. The blind alone is the wood's not-knowing, never another's (§6.1). **Not** `!HOLD →` the act, which is *not feel* (below) | IV.2 r5; IV.6 r10 |
| feel (of wood, of a hull); not feel a happening | `HOLD`, to know by touch; `!HOLD →` an **act** is *not feel* it (A15's *let go* is `!HOLD →` a **thing** held) | V.6 r18 |
| was not there (did not witness it) | `!EYE` on the absent one's file | IV.6 r1 |
| out into (the open sea) | `→in @f`, where file f's year carries the WATER band | IV.6 r4 |
| even (so), conceding | `{still}` on the act that holds in spite of it | IV.6 r5 |
| ourselves, itself (by one's own power) | the self (A4): a runner to `@f` of its own file: `>GO → @12` from file 12, "we sailed ourselves home"; `HEAR → @13` from file 13, "the wood obeys the wood" | IV.6 r5; V.6 r6 |
| drew back from X | `X ⇒ HAND:stem+TURN`: from the source end, then the arm turns aside | IV.6 r10 |
| it was one (it truly was so) | `TRUE+` the thing (`TRUE+>DYING`, a true killing) | IV.6 r10 |
| ignorance | `!HOLD`, not knowing, as the content of a said-pocket | IV.6 r10 |
| their dead | `!LIVE` | IV.6 r3, r11 |
| stand (of a tree, a grove); reach to (of a place) | `RISE` in ligature with the thing that stands, with a *to* runner to where it reaches (`8: SILVERBARK×3+RISE → @10`). A bare *to* runner from a thing that does nothing reads "goes to" | IV.6 r8 |
| the council-grove; the council-hall | `SILVERBARK×3` on a place's file (home, file 8). The council as people is `DEEP+US×3` on its own file | IV.6 r8, r11 |
| the shallows (below a door, a wall) | `BENEATH+DOOR` in the WATER band | IV.6 r2 |
| throw, shove (a body, a hull); send; set in motion | `>GO →` the thing thrown or sent, with `→in` where it goes (B15's two runners). `>GO` is *make go*, never *let go* (which is `!HOLD →`) | IV.6 r3, r4; V.3 r4–6; V.6 r21 |
| go out of (us) into … | `>GO` on the source's file ("we sent it"), `→` the thing, `→in` where it goes. Not `GO` on our file, which is our own going (§10.3) | V.3 r4–6 |
| not empty (of a silent stone): not spent | `!SPENT`, as E3-08 asks of a silent stone "Is it spent, or waiting?" | V.3 r10 |
| know rightly; hold (it) true | `TRUE+HOLD` cut on the file where the telling's *you* stands, with no runner (the reading needs the file named) | V.3 r10 |
| the bearer (of a standard), and the standard it bears | `BEARER` on its own file, with `CARVE` after it on the same file: *Seth·varen* (`CARVE+BEARER`) said apart | V.7 III r3 |
| the second (in succession) | `HULL@2`, the second hull | V.7 III r3 |
| when X, then Y (a turning with no *else*) | a *then* runner (`⇒`) from X's act to Y's act; a fork needs an *else* branch | V.7 III r3–r4 |
| grown, not built | `GROW` and `!SQUARE+RISE` on one file (build is `SQUARE+RISE`) | V.6 r1 |
| the sky they lived by | `LIVE →with` the wood's `LIVE` in the MIST band | V.6 r2 |
| ask (a thing of someone) | `MOUTH?`, with a *for* runner to what is asked and a *to* runner to the one asked | V.6 r3 |
| sail | `GO` in the WATER band | V.6 r4 |
| crewed by | `HULL(×3) →with` the crew | V.6 r4, r21 |
| command (a hull with no one aboard); obey | `HEAR?` on the hull `→with CARVE` (does it obey? by a carving); obey is `HEAR` to the carving obeyed | V.6 r5, r6 |
| says what, and not whether | `MOUTH` and `!MOUTH?` on the carving's file | V.6 r7 |
| balk at | `!GO? →` the thing (the question: *may*) | V.6 r7 |
| fail; a failure (of a blow) | `!STRIKE`; "where it failed" a runner `→in` it; "the first failure" `!STRIKE@1` | V.6 r8 |
| temper (of a grain); grain (in a hull) | `HEART`: a grain's temper is its heart; "no temper yet" `!HEART{still}` | V.6 r8, r12 |
| serve (your names will serve) | `TAKE →` the thing: we take it up and use it | V.6 r8 |
| the swell | `RISE` in the WATER band | V.6 r13 |
| generations | `LIVE×3`: many lives | V.6 r11 |
| spare (none to spare) | `!GIFT →` them | V.6 r14 |
| pour | `GO{all}`: all going at once | V.6 r14 |
| ripen; ready | `GROW{all}`: grown full | V.6 r12, r17 |
| hang back | `KNOT` (wait) on file 8, the file behind | V.6 r17 |
| soon | `SWIFT`, as a modifier | V.6 r10 |
| touch | `HAND →` the thing touched | V.6 r16 |
| your children had children | two `SAPLING×3` on your file, the first `⇒` the second | V.6 r10 |
| fewer | `{few,more}` on one sign | V.6 r20 |
| a people who had never known they were the foe | `STONEFOLK×3‿`, `!HOLD →that {ANGER+STONEFOLK}` with a memory ray (never) | V.6 r21 |
| a doom (the whole fleet) | `DEEP+CARVE` cut on our own file: we are the doom | V.6 r21 |
| the shot meant for it (taken by the husks) | the shot `STRIKE →` the seed, **broken** by the husks' `TAKE →` the shot (`lap`) | V.6 r18 |
| hard to bring down | `>FALL{slow}` from the shore | V.6 r19 |
| the seed is the hull's own life | a **bind** of the hull and the seed, its out-runner to `LONE+LIVE` on the hull's file | V.6 r18 |
| you (in the heart ring) | files 15, 0 and 1 are the root's (A4), so the shore-men are **named** on another file, `STONEFOLK×3` standing first on it | V.6 r1; IV.4 r1 |

#### 21.9.4 Rules the units proposed [rule, where the validator already reads it; *[proposed]* otherwise; **[Jack]** for calls]

**A16b · Referents, completed** *[proposed]* (W01, with W03, W05 and W06's cases). A16 lets a belonging keep a file's referent only where a thing-sign has introduced one. Read with no `# file` comments, the whole-leaf carvings lost referents in five ways. Each rule below is §11.2 read with §10.3 and A1, as A16 is:
- **(a)** A belonging never introduces a referent, whether or not a thing-sign has introduced one before it; the file keeps its bearing, or the teller.
- **(b)** A person's (or a hull's) **heart and feelings** are belongings: `HEART`, `SHAME`, `GLAD`, `GRIEF`, `ANGER` (W01, W05 #9, W06 #9). A tree's `BARK` is its skin, a belonging (W03). A stone's or a gun's `FLASH` on the file of a `SQUARE` or `GUN` is a belonging (W05 #9). An `EDGE` cut on the file of a place already standing there is that place's edge (W06 #10), as `DOOR` and `SQUARE` are a built place's.
- **(c)** In a telling, file 12 with no thing-sign on it is the teller, *we* (§11.2's custom).
- **(d)** A condition band laid over a file's empty cell is that file's referent, the band as a thing (A1: the grey, the sea, the white), until a thing-sign stands first on the file; a later ring's band over the empty cell replaces an earlier one's. In a year, `→ @f` to such a file goes to the band as a thing (W03's note for A1).
- **(e)** In the heart ring and band I, a mark that a `NAME` runner from another file points at is the name given (A9's naming substitute): a belonging, not a new referent.
- **(f)** A thing cut as the modifier of an act, first on its file (`HULL×3+GO½`, `STONEFOLK{only}+GO`), is the act's doer and introduces it, unless the ligature is a named compound or the thing is a belonging.
- **(g)** A mirrored thing-sign (`!PILLAR`, "not a pillar") is said of the referent and never introduces one (W03). A hollow mark (shown, not meant) introduces its referent for its own knowing only, since a likeness is "not present in the knowing" (§10.9; W05 #10).

W01 tried (a)–(f) on a private copy of the validator (`wf8/backtrans/W01_work/grain_validate_A16b.patch`): its selftest passes, the 13 rounds of `coverage/tests/` and the IV.4 pilot keep their findings, and II.2 read with no comments keeps every file right. Until the shared validator takes it, every whole-leaf round carries `# file` comments, and the leaves that the back-translations found fragile were re-cut so that they read right under either rule (V.3's `BEARER+HEART`, V.4's `ANGER+SAPLING×3`).

**A17 · The mirror and the hollow together** [rule; settles W01 against W02, W03 and W05]. `!` and `~` on one sign draw **one** mark, a mirrored outline, so the order they are written in carries nothing. The canonical order is the printer's, `!~X` (A7's token order; every canonical round the units printed writes it so, e.g. III.2 Leavaren's `!~AXE`), and `~!X` is accepted and printed `!~X`. It reads **"a seeming not-X"**: the hollow of a not-doing (III.2's "if the axe had not felled them", A6's *would have*). It never reads "not mis-X": no drawing can show whether the mirror or the hollow is outermost. So:
- *must not be mistaken* is `!TURN+HOLD`, "a holding not turned", and *not misheard* `!TURN+HEAR` (A15 above);
- *not empty* (of a silent stone) is `!SPENT` (V.3);
- *no more tricks* is said straight (`DEEP+WOOD` with `TRUE{all}`, III.2), and *never the same trick twice* is `~GO#1{only}` with a memory ray (V.6).
W01's proposal (`!~X` = "not mis-X") and W03's (canonical `~!`) are withdrawn in favour of this rule; the register rows that used `!~` are corrected (§21.9.5).

**A18 · The untold ring** *[proposed]* **[Jack]** (S09). `rK …` (an ellipsis where the empty ring has its dot) means "the wood holds a knowing here that the telling does not give". It is never drawn: a round with an untold ring is shown only as the plates of its told rings. It is never read "a morrow passes". It counts toward `rings:` and the band-rules as an empty ring does, and takes no marks, runners or rays. It serves every carving the Book cites only in part: V.7 III's Last Tide plan, and the parent rings E5-02's coverage text elides. Until the validator reads it, S09 writes the stand-in `r2 ·  (untold: …)`, a trailing comment the validator accepts.

**A19 · A memory ray in a year of several cells** *[proposed]* (W03). `mem f: rK/Y → pith` names a file and a year, not a cell. Where the file holds more than one mark in that year, the ray leaves **the first cell's mark** (the first written in that knowing); an author writes the remembered mark first. Without the rule two drawings share one canonical GN.

**A20 · A band lies over its file's whole year** [rule; a validator note *[proposed]*] (W03 #6, W05 #12, W06 #2). A band is written with a knowing, but §3.6 and §4.3 lay it over its file's whole year, and in a celled ring the knowings on one file share a year, so the band covers every mark in that year. Where that is false of a mark, lay the band on a file between (IV.2 lays the WATER band on file 13 alone), or keep the knowings in separate years. In a one-cell ring (rings 2 and 3 of most rounds) every mark on the file is a year of its own and needs its own `band` line. *Proposed:* a validator note when a band covers a mark of another knowing.

**A21 · A9, completed** [rule]. A9's V.3 entry gains ring 2's "where a stone flashes, a gun is", which §18 gives as a cut-pocket and band I cuts plainly (`0: FLASH ⇒ 0: GUN` on the wall's file, W05 #1). In A9's own substitute "two with-runners to one `LIVE#1`", the `#1` is "one", not "once" (W07): the validator reads a count on an act as "n times" (v1 §3.7), so the reading is to be taken from the two with-runners.

**A22 · Traps the register should name** [rule] (W05 #3, W07, W02).
- `X+HAND` is **five** (v1 §3.7), so "angry hands" is `HAND×3+ANGER` (the hand the modifier), never `ANGER+HAND×3`; "the wood's hands" is the wood's knowing `→with HAND`.
- `DEEP+KNOT` is **Eirlenth's name** (with the WHITE band): "how long it waits" is `KNOT?`, not `DEEP+KNOT?`.
- A half-size **line root** outside a pocket reads as a **cited carving** (§8): `SQUARE½` is the Mute Square cited, not a small stone. A shard is `BREAK+SQUARE` (§21.9.2).
- `NEW+HAND` with a runner reads *touch*; B13's `STONEFOLK+HAND` reads "five shore-men": the plain `HAND` on the wall's own file is the wall's hand (W05 #11).
- In a round whose root is a place (`HOME`), runners in outer rings point at the place's bearing (`@8`), not at `@0`, which beyond ring 1 reads as its bearing, "ahead (the shore)" (S10).
- "Cannot hold (it)" is a **break**, not the mirror: the holding cut whole, `HOLD →` it, thwarted by what breaks it (`lap`, §7.1). `!HOLD` is *forget; let go* (A15), which would say the opposite (S10, *The Two Homes*).

**A23 · *Rhenear* cut small** [rule] (S09). E5-02's aim (ring 4, file 8) cuts *Rhenear* once, alone, half size with the kind-arc, `STONEFOLK×3‿½`, as mystaeri_spec §3.9 and the Deceit Tide's first-appearance row say, and the habits after it as acts: `8.1: STONEFOLK×3‿½    8.2: DEEP+STRIKE@1    8.3: >GO`. The Book of Knowings' own round of E5-02 takes the same ring 4.

**A24 · The Last Tide's root** **[Jack]** (S09). V.7 III's round is an order and must cut a line root in its heart. Proposed: `STERN`, the Turned Stern (heart: the young wood's *home when wounded*; last ring: the *home* wanted); the alternative is `BARB`, the Bar Before. No name in its bark: V.7 III does not say the heart held one.

**A25 · The v1 STONE sample in the Epilogue** **[Jack]** (S10). The Epilogue's round keeps every mark, file, ring and ray of mystaeri_spec §5.7 and adds five tier-3 marks on files 0, 4, 6 and 8 (never on 10–14, which the letters' course keeps clear). §17 says the v1 samples keep their GN: strip the five and the round is the v1 sample exactly. The blind back-translation also read the Stone's r2 `DEEP+SQUARE` as "the mountain" (the compound table's *eirrhen*), where §5.7 glosses "the last stone": either cut `SQUARE{last}` there (a v1 mark changes), or add a reading rule that a lexical compound yields to its parts on a file a ray holds as one stone.

#### 21.9.5 Corrections to the concept register (`coverage/concepts.tsv`; applied in `wf8/concepts_full.tsv`)

| Lemma | Was | Now | Found by |
|---|---|---|---|
| mistake, "must not be mistaken" | `!~HOLD` | `!TURN+HOLD` (A17); *mistake* itself stays `~HOLD` | W03 #7, A17 |
| misheard, "no promise misheard" | `!~HEAR` | `!TURN+HEAR` (A17) | A17 (II.2 r10) |
| trick, "never plays one trick twice" | `!~GO#2` | `~GO#1{only}` with a memory ray (A17) | A17 (V.6 r8) |
| empty, "silent and not empty" | `!~` | `SQUARE+!MOUTH →with !SPENT` | W05 #2 |
| shard | `SQUARE½{only}[STILL]` | `BREAK+SQUARE{only}` in the STILL band (A22) | W02 |
| jar | `~BREAK+HOLD` (cmp, no gloss) | the compound `BREAK+HOLD`, a cracked cup, cut hollow as a likeness | W06 |
| strength, "going out of them" | `LIVE` | `LIVE+GO`, life going out | W06 |
| bank, "as roots hold a bank" | `→as ~ROOT+HOLD → ~EARTH` (reads "seem to remember") | `HOLD →as ~ROOT`, `~ROOT → ~EARTH` | W03 #1 |
| stump, "a stump cut low" | `NEW:stump+BENEATH` (head inward) | `BENEATH+NEW:stump` | W03 #2 |
| grain (the kind of a heart's wood) | `CARVE` | `WOOD` on the teller's file, NAME to it and to the said-pocket of the grain's name; `CARVE` stays for "the shape of a knowing" (A15) | W03 #5 |
| away, leave | `GO → @8` | unchanged; `!GO → @8` "not go home; will not leave" added (A15) | W03, W04, W07 |
| (IV.2, ring 6) "it came again; we put up more" | braid `abab` | `aba`: one letter per crossing (§7.2) | W03 #3 |
| (IV.2) "tall and dark of bark" | band year unset | write `BARK` first in its knowing, so the DARK band's year is the bark's | W03 #4 |
| (V.3 proof ring r10) | `!NEW+HOLD` (mirror on the modifier) | `NEW+!HOLD` (the head mirrored) | W05 #4 |
| (V.4 proof rings) | elders on file 6, silver elders on 10 | elders on 7 (a person, an odd file), the grove on 8 (home) | W06 #3 |

Every new compound of §21.9.2 and every reading of §21.9.3 has its row in `wf8/concepts_full.tsv` (kind `add`).

#### 21.9.6 Findings for the validator (not fixed: `grain_validate.py` is shared; none blocks a unit)

1. **Pockets and the packing** (W02 and W04, found separately). `pack_round` keys the marks' cursors by `(pith, file)` and the pockets' by the bare file, so a pocket never sees the marks already cut on its files: it lands in its ring's first year, and marks after it are not pushed past it (K06, R16). *Proposed:* key the pocket's cursors by `(pith, file)`, so that "a pocket takes a whole year across its files, above the highest cursor among them" (§4.3) holds. Every unit placed its pockets on files that hold no mark in their ring.
2. **`>TRUE`** reads "are true": the causative is dropped from a quality's reading (W01).
3. **`--canon` drops a v1 graft** (`graft(E3-01)` after E4-01's r4 marks); the printer should keep it (S09).
4. **The kind-arc with half size** (`STONEFOLK×3‿½`) reads "the small shore-folk as a people (Aethear)"; it should gloss *Rhenear*, "the stone-deaf" (S09).
5. **A split runner inside a pocket** is read by its first shoot only (W06 #4); units write pocket runners singly.
6. **A lone mark that governs nothing** takes a verb-first gloss ("seem to speak" for a hollow jaw); a noun-first gloss would help a blind decoder (W06 #5).
7. **§13.4 does not order rays among themselves**; units write them by file (W06 #6).
8. **`LIVE#1`** in A9's substitute reads "living once" (A21; W07).
9. **The untold ring** `rK …` is not yet read (A18; S09).
10. **Referents without `# file` comments** (A16b): the validator's reading follows A16 only.

#### 21.9.7 Conflicts between units, and how each was settled

| # | Units | The conflict | Settled | Units re-cut |
|---|---|---|---|---|
| G1 | W01 against W02, W03, W05 | `!~X`: W01 read it "not mis-X"; W02, W03 and W05 found that the drawing cannot show the order of `!` and `~` | A17: the order carries nothing; `!~X` is "a seeming not-X" | W01 r10 (`!~HEAR` → `!TURN+HEAR`), W01 r11 (`!~HOLD` → `!TURN+HOLD`, the same English as IV.2 r7's "must not be mistaken"), W07 r8 (`!~GO#2` → `~GO#1{only}`) |
| G2 | W03 against the printer | W03 proposed the canonical order `~!` | the printer's `!~` stands (A17) | none (a knowing-form `~!` is accepted) |
| G3 | W03 against W04 (and W07) | "did not know why": W03 `!HOLD →in` the act; W04 `!HOLD →` the act, which W07's *feel* row reads "not feel" | W03's `→in` (A15) | W04 r10 (runner m8 `→` → `→in`) |
| G4 | W03, W04, W07 | `!GO → @8` glossed "will not leave", "away from home", "no crown to come home to" | one reading (not going to file 8: behind, home), glossed by its doer (A15) | none |
| G5 | W01, W02, W06 | `BENEATH+SIT` proposed three times; `OVER+HULL×3` twice | one entry each, same gloss | none |
| G6 | W02, W04 | the pocket-cursor finding, reported twice | one finding (§21.9.6 item 1) | none |
| G7 | W01, W03, W05, W06 | A16's missing belongings, proposed separately | one list, A16b | none |
| G8 | W01, W03; W02, W07; W04, W07 | "answer" twice; "heavy" and "go heavy"; "light" and "go light"; "hasty" and "crude" | one row each (A15) | none |
