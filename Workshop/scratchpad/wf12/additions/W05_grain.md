# W05 · grain additions (wf12, Book v3.0.0: V.3 The Wreck That Went Home)

*wf12 unit W05. Additions to `wf12/base/grain_v2_full.md` for the v3 round of V.3 (`wf12/units/W05.md` §4). No new sign and no new rule. Four compounds, each modifier + head as Seilrhass builds (mystaeri_spec §2.5), the soft reading the compound of the two soft readings (computed, not coined; call §19.8); eleven decoder readings for A15 (nine in §2, two more in §4 after the blind back-translation); and the findings for the validator and the spec. The private validator copy (`wf12/tmp/W05/groot/wf7/grain_v2.md`, not linked) carries the block below as its §21.10.*

## 1 · Compounds

| Compound | Means | Soft reading | Derivation | Where in V.3 (v3) |
|---|---|---|---|---|
| `BREAK+WOOD` | broken wood; wreck-wood | *rhass·veir* | BREAK *rhass* "break; a crack" + WOOD *veir* "wood; boards". Beside `BREAK+HOLD` (a cracked cup, §21.9.2) and `BREAK+SQUARE` (a shard): BREAK as modifier is "broken". Without it the validator reads "breaking wood" | ring 1, "Now are we broken wood" |
| `DEEP+LIE` | lie long | *eir·rhir* | DEEP *eir* "deep; old; long" + LIE *rhir* "lie down; lie". The exact counterpart of IV.4's `DEEP+HOLD` (*eir·thein*, "hold long", §21.7). Without it the validator reads "lie down, old" | ring 18, "Long we lay in the cold" |
| `BURN+GO` | the fire's going: a shot of fire; with the causative, throw fire | *esth·rei* | BURN *esth* "burn; fire" + GO *rei* "go". The hull's fire thrown, as `AXE+GO` (§21.9.2) is the shore's iron coming: the two weapons of the leaf, each the thing that goes. `BURN#1+>GO` reads "throw fire, once" | ring 11, "We threw one fire at the stone that had spoken" |
| `BURN+FIND` | the fire's finding: what a shot of fire finds | *esth·veass* | BURN *esth* + FIND *veass* "find; come upon", beside `AXE+FIND`, which the validator already reads "find: the iron" (ring 15) | ring 11, "Of what our fire found there, the grain hath naught" (`→ ∅`) |

The validator reads these from the one block below.

```json
{"compounds": {
 "BREAK+WOOD": "n:broken wood (wreck-wood)|broken boards",
 "DEEP+LIE": "v:lie long|lying long|lay long",
 "BURN+GO": "v:go as fire (the fire's going: a shot of fire)|going as fire|throw fire",
 "BURN+FIND": "v:find by fire (the fire's finding)|finding by fire|"
}}
```

## 2 · A15, continued: readings a decoder needs

| English | Grain | Where |
|---|---|---|
| salt (the sea's salt in wood) | `DUST` cut inside the WATER band: the water's dust. The grain has no sign for salt and needs none; DUST is a belonging (A16), so it keeps its file's referent | V.3 r1, "the salt is in every board" (`12: DUST →in 12: WOOD×3`) |
| every board (in the heart) | `WOOD×3`: A9's `×3` for `{all}` in the heart ring | V.3 r1 |
| one cold season | `SUMMER#1` (one season) in the WHITE band | V.3 r2 |
| first … then … then … last (of acts in a row) | ordinals on the acts, `@1 … @4`; `{last}` is a foot-station mark and cannot stand with the causative's chevron (`>X{last}`, §5.4: one mark per station) | V.3 r7–r8, the four sendings |
| the same one, through a whole leaf (the stone that had spoken) | a chain of rays on one file (`ray 0: r3/1–r4/1`, `r4/1–r11/1`, `r11/1–r14/1`); a stone on another file with no ray is another stone | V.3 r3, r4, r11, r14 |
| along (a wall) | a stone on a file beside the wall's, with `→in @0`: a stone in your wall | V.3 r14, "a stone along the wall" |
| stand off behind, hang back (of persons) | `KNOT →in @8`: wait, in the behind (A15's *hang back* puts KNOT on file 8; here the waiters keep their own file) | V.3 r12, "Behind us our kin stood off" |
| flat (of water); calm | `LIE` on the sea's file in the STILL band: the sea lies still | V.3 r12, "Flat lay the water" |
| in the night | the DARK band over the doer's year | V.3 r9, "In the night the heart carved" |

## 3 · Findings (for the validator and the spec; none blocks the unit)

1. **The causative and the foot station.** §5.4 puts `>` (the chevron at the foot) in the "under the foot" station with *again, still, last, slow, gently*, and allows one mark per station; the validator's M04 counts only the fringe, so `>GO{again}` and `>GO{slow}` pass (the wf8 V.3 round carried both, rings 5–6). This round avoids them: the sendings are counted (`>GO@1`–`@4`), and "slow as sap" puts the slowness on the likeness (`~SAP+GO{slow}`). *Proposed:* M04 counts `>` with the foot station.
2. **Every cut-pocket reads "an older carving, cited"**, even a carving cut whole that is new where it stands (ring 9's *Look before you trust*, which the heart carves that night) or a lesson given (ring 3's *Where a stone flasheth, there the iron is*). *Proposed:* "a carving: […]", keeping "an older carving, cited" for a pocket that holds a half-size root (`STERN½@1`, ring 6).
3. **TIDE for the sea** (as the wf8 round): the validator glosses TIDE "tide (a growing)". The Book's own word in ring 18 is *the tide*; elsewhere the reading needs the `# file` comment. A1's band as a thing (`[WATER]`) cannot stand where the sea acts, because an act needs its mark.
4. **Rays in celled years** (as before): `ray 0: r4/1–r11/1` names a year whose file holds two or three marks; the renderer should run the ray SQUARE to SQUARE.
5. **§11.3's plan for V.3** (2 / 6 / 3 = 11 rings, ≈110 marks, radius 900–1,150) was the v1.3 leaf. The v3 leaf is 20 paragraphs: 2 / 14 / 4 = 20 rings, 118 marks (114 before the back-translation's mends), 31 years, radius about 1,254 (cells `[1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]`).

## 4 · After the blind back-translation (the fixer, 2026-10-03)

The blind reader (`wf12/backtrans/W05.md`) drifted on five rings and one line of the reading; the mends are in the unit's § BACK-TRANSLATION. No compound was added or changed, so the `json` block above stands as it is. Two readings a decoder needs, and one use of an A15 reading:

| English | Grain | Where |
|---|---|---|
| *may … ; may …* (possibilities in a row, that do not rule each other out) | **one questioned mark to a file**: a second thing on a file of its own carries the second *may*. Two questioned marks on one file are always A6's "either … or, and we do not know which" | V.3 r9: `0: SQUARE  0: MOUTH  0: !MOUTH?` (a stone spoke; then, may it not speak?) and `3: SQUARE  3: !MOUTH  3: KNOT?` (a silent stone: may it wait?) |
| *that place; it* (a thing cut in an earlier ring, named again) | the thing **re-cut on its file and rayed** to where it was first cut, and the runner run to the re-cut mark; a runner cannot reach back into an earlier ring, and `@f` names the file's referent, not its belonging | V.3 r10: `4: WOOD+DYING` with `ray 4: r8/1–r10/1`, "we knew that place"; r16: `12: WOUND` with `ray 12: r15/1–r16/1`, "our kin felt it" |
| *let us go* (a use of A15) | `!HOLD? →` **us**, the thing held (`@12`, or `@12.rK/Y` where file 12 is full in the source's year, A4). `!HOLD →` an act reads *not feel* it (A15, V.6 r18) | V.3 r6, `f4  0.r6·4 → @12.r6/2` |

**Findings.**

6. **`!HOLD →` an act.** The wf8 V.3 round's "let us go" was `!HOLD? →` our going; under the merged A15 it reads *not feel our going*, and the blind reader read it so. Units that copied it should run it to the thing held.
7. **`{only}` bounds the mark it stands on.** On the sending (`>GO{only}`) the blind reader read "sent us alone"; "for naught else" bounds the purpose, so it stands on the looking (`EYE{only}`), which the validator reads "only eye".
8. **A ray names its two ends only.** The blind reader asked whether `ray 0: r4/1–r11/1` makes ring 9's file-0 stone, which it passes, the same stone. This round reads it as not (a ray joins its two ends; ring 9's stone is any stone of the wall, and ring 13's is the wall), but the spec does not say. *Proposed:* §3.7 says that a ray joins its two ends only, and the marks it passes on its file are not made the same.
9. **The blind inputs carry the Book.** §1's "Where in V.3 (v3)" column and §2's "Where" column quote the leaf's English, as the shared spec's §21.9.2–3 quote the wf8 round. A blind reader should be given the `json` block and the *Grain* column only.
