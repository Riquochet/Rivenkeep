### 21.W04 · Additions by unit W04 (IV.6, The Voyage of the Aelvaren, carved whole: `wf8/units/W04.md`)

*For merging into `wf7/grain_v2.md` §21 by the orchestrator (unit W04 did not edit the shared spec, the lexicon or the concept register). No new sign and no new rule was needed. Three compounds are added, each modifier + head as Seilrhass builds (mystaeri_spec §2.5), its soft reading the compound of the two signs' soft readings (computed, not coined; call §19.8), as §21.3 and §21.7 do. Without them the validator reads these ligatures part by part ("fell with iron and lose", "earth most edge", "a burning wood"), which is legal but misleading.*

| Compound | Means | Soft reading | Derivation | Where in IV.6 |
|---|---|---|---|---|
| `AXE+LOSE` | a blade that slips; the blade let slip | *rhith·naenn* | AXE *rhith* "iron; the blade" + LOSE *naenn* "lose; let slip" (the register's "the blade that slipped" is LOSE with AXE; inside a cut-pocket no runner may join them, so it is the ligature) | ring 9, the keel's cut-pocket: "the blade that slipped" |
| `EARTH+EDGE` | the edge of the world (with `{most}`: its far edge) | *reth·enth* | EARTH *reth* "earth; the world" + EDGE *enth* "edge; end; outer" | ring 11, "to the far edge of the world" (`10: EARTH+EDGE{most}`) |
| `BURN+WOOD` | charred wood: wood the fire has had | *esth·veir* | BURN *esth* "burn; fire; char" + WOOD *veir* "wood" (beside `BURN+TREE`, Ashwood, a name, and `BURN+DUST`, ash) | ring 5, "Even charred … the wood" (`14: BURN+WOOD`) |

```json
{"compounds": {
 "AXE+LOSE": "n:a blade that slips (the blade let slip)|blades that slip",
 "EARTH+EDGE": "n:the edge of the world|the edges of the world",
 "BURN+WOOD": "n:charred wood|"
}}
```

**Readings to add to A15** (register readings that are not their sign's own gloss; IV.6 relies on them):

| English | Grain | Where in IV.6 |
|---|---|---|
| was not there (did not witness it) | `!EYE` on the absent one's file | ring 1, "The hull that brings it to you was not there" |
| light (not heavy) | `THIN` | ring 2, "grey and light" |
| away from (a place) | `!GO →` that place (`@8`, home) | ring 4, "away from home" |
| out into (the open sea) | `→in @f`, where file f's year carries the WATER band | ring 4, "took us out toward the open sea" |
| even (so), conceding | `{still}` on the act that holds in spite of it | ring 5, "Even charred, even dying, the wood knows" (`HOLD{still}`) |
| ourselves (by our own power) | the self (A4): `>GO → @12` from file 12 | ring 5, "we sailed ourselves home" |
| drew back from X | `X ⇒ HAND:stem+TURN`: from the source end, then the arm turns aside | ring 10, "why the host's arm drew back from the blade" |
| it was one (it truly was so) | `TRUE+` the thing | ring 10, "They knew a murder, and it was one" (`TRUE+>DYING`) |
| ignorance | `!HOLD`, not knowing, as the content of a said-pocket | ring 10, "They did not know it was ignorance" |
| their dead | `!LIVE` | ring 11, "as the long-lived lay down their dead" |

**More readings for A15, from the blind back-translation** (`wf8/backtrans/W04.md`). Rings 8 and 10 drifted when IV.6 was read back blind; the first two rows below and the ring-8 recut fix them. The last three are register readings that are not their sign's own gloss (A15's standing rule), whose absence cost ring 2 and ring 3 a nuance.

| English | Grain | Where in IV.6 |
|---|---|---|
| stand (of a tree, a grove); stand down to, reach to (of a place) | `RISE` in ligature with the thing that stands, with a *to* runner to where it reaches: `8: SILVERBARK×3+RISE → @10`, "standing down to the water". A bare *to* runner from a thing that does nothing reads "goes to" (§6.1), which is motion; and a lone `RISE` on the file takes the file's first referent as its doer | ring 8, "a grove of silver elders standing down to the water" |
| the council-grove; the council-hall (the grove the council meets in) | `SILVERBARK×3` on a place's file (home, file 8), beside SAND or ROOT×3. The council as people, the elders of the long-lived, is `DEEP+US×3` on its own file | ring 8, "the council-hall, which is a grove of silver elders"; ring 11, "the roots of the council-grove" |
| did not know why (an act) | `!HOLD →` the act, where the act carries the blind (`→bc ∅`): the act is cut whole, so it is known; what is not held is its cause | ring 10, "why the host's arm drew back from the blade they did not know" |
| the shallows (below a door, a wall) | `BENEATH+DOOR` in the WATER band: the water under the door | ring 2, "waited in the shallows below the door" |
| throw, shove (a body, a hull) | `>GO →` the thing thrown, with `→in` where it goes (B15's two runners) | ring 3, "threw him into us"; ring 4, "shoved us off" |

**A validator finding (for `grain_validate.py`, `pack_round`).** In knowing form a pocket's year is computed from a cursor keyed by the file number alone, while marks keep their cursors under `(pith, file)`. The two never meet: a pocket is always placed in year 1 of its ring (above nothing), and marks written after it on its files are not pushed past it. A pocket on a file that holds a mark in its ring therefore fails K06 (and `@f` terminals on its files fail R16), and a pocket whose files are empty lands in year 1 even when its governing mark stands in year 2. IV.6's P1 (`9.2.r9·2 →that P1`) had to move from the prototype's files 12–1 to 3–8, and the canonical round prints it in r9/1 while its *that* runner leaves r9/2 (legal: inside a ring a runner may run inward). **Proposed:** key the pocket's cursors by `(pith, file)`, as the marks' are, so that "a pocket takes a whole year across its files, above the highest cursor among them" (§4.3) holds.
