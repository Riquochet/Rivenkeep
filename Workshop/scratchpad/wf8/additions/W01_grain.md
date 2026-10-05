# W01 · II.2 Of the Breath of the Wood: grain additions (proposed §21.x of `wf7/grain_v2.md`)

*wf8 unit W01, 2026-09-28. Additions only; the shared `wf7/grain_v2.md` is not edited (concurrency rule). No sign and no rule is added. Each compound below is modifier + head, as Seilrhass builds (mystaeri_spec §2.5), and its soft reading is the compound of the two signs' soft readings (computed, not coined; call §19.8). Seven of them are already named in §18 or the concept register (`coverage/concepts.tsv`) but are missing from the validator's compound table, so the validator read them part by part, in two cases wrongly: `DEEP+TREE×3` ("the deep forest") read as **Yew** (`DEEP+TREE`, a grain-name of the shore), and `BEND+HULL×3` ("the twisted boughs") as "bending host". The ×3 in a key keeps the plural compound apart from the singular one, as `DEEP+PILLAR×3` and `BOND+WORD×3` already do.*

| Compound | Means | Soft reading | Derivation | Where in II.2 | Already named in |
|---|---|---|---|---|---|
| `DEEP+TREE×3` | the deep forest; its depths | *eir·thaelen* | DEEP *eir* "deep" + TREE×3 *thaelen* "trees, a grove" | ring 10, "each deep of the forest" (`DEEP+TREE×3{all}`) | register, *tree, forest*: "the deep forest DEEP+TREE×3" |
| `BEND+HULL×3` | the twisted boughs (the wood's own name for the rite-trees) | *seil·seilen* | BEND *seil* "bend as a bough bends" + HULL×3 *seilen* "boughs" | ring 8, "The twisted boughs we bent in our rites" | §18, "the twisted boughs, our rites" |
| `OVER+HULL×3` | the high boughs | *laes·seilen* | OVER *laes* "over, above; high" + HULL×3 *seilen* | ring 10, "as the storm speaks in the high boughs" | register, *high, tall* |
| `HOLD+EARTH` | anchor: hold (a thing) to the earth | *thein·reth* | HOLD *thein* "hold" + EARTH *reth* "earth, ground" | ring 9, "held the breath to the earth", "the anchors of our sky" | §18, "anchors of our sky"; register, *anchor* |
| `HOLD+PILLAR` | a mist-holder: the shore's name for a black pillar (*Mystholder*), said in its pocket with `[MIST]` | *thein·naelsaen* | HOLD *thein* + PILLAR *naelsaen* | ring 9, "You call them the Mystholders" (`{ HOLD+PILLAR[MIST] }`) | register, *mystholder* |
| `BENEATH+LIE` | lie (flat) beneath; lie aground | *senn·rhir* | BENEATH *senn* "beneath" + LIE *rhir* "lie down; lie; (register) flat, laid along the ground" | ring 3, "Our land lay flat beneath the trees" | §18, *aground* (IV.6) |
| `LIE+TREE×3` | the flat wood: the wood laid along the ground | *rhir·thaelen* | LIE *rhir* ("flat: laid along the ground", register) + TREE×3 *thaelen* | ring 14, "the flat wood under the grey" | register, *flat*: "the flat wood" |
| `BENEATH+SIT` | sit beneath | *senn·rass* | BENEATH *senn* + SIT *rass* "sit; take one's seat" | ring 8, "Under the silver elders the council sat" | new |
| `EDGE+EYE` | watch from the edge | *enth·neas* | EDGE *enth* "an edge; the rim of the grey" + EYE *neas* "an eye; to look" | ring 12, "From the edge we watched your shore" | the II.2 proof ring (`coverage/tests/II-2_proof.gn2`) |
| `LONE+MOUTH` | one's own tongue; its own voice | *ith·renn* | LONE *ith* "one, alone, own" (A6) + MOUTH *renn* "a voice; a tongue" | ring 10, "each deep of the forest speaks it its own way" | A6 (`LONE+X`: own X) |
| `BREAK+MOUTH` | speak in thunder: the storm's speaking, in cracks and breaks | *rhass·renn* | BREAK *rhass* "storm; thunder; a crack" + MOUTH *renn* | ring 10, "as the storm speaks" (the likeness, cut hollow: `~BREAK+MOUTH`) | new (beside §21.7's `HULL+BREAK`, *Seilrhass*) |
| `EDGE+PILLAR×3` | the pillars at the edge (of the world) | *enth·naelsaenen* | EDGE *enth* + PILLAR×3 *naelsaenen* | ring 14, "the black pillars at the edge of the world" | new |
| `TREE×3+LEAF` | a forest-leaf; a fern of the forest floor (cut hollow, the grain's likeness) | *thaelen·lel* | TREE×3 *thaelen* + LEAF *lel* "a leaf" | ring 4, "as it withers a fern of the deep forest" (`~TREE×3+LEAF`) | register, *fern* (`~LEAF`) |

The block the validator reads (a private copy of `grain_v2.md` with this block appended was used for every check of W01):

```json
{"compounds": {
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
 "TREE×3+LEAF": "n:a forest-leaf (a fern of the forest floor)|forest-leaves"
}}
```

**Findings for the validator (not fixed; the validator is shared).**
- `!~X` reads "seem to not X". The register uses it for "not mis-X" (*must not be mistaken* `!~HOLD`; II.2's *no promise misheard* `!~HEAR`). §10.8 says properties combine and gives `~!STRIKE`, "a seeming of not striking"; the order of `!` and `~` is not given a meaning. **Proposed:** A6 gains a row, "not mis-X: `!~X` (the mirror of a seeming)", and the validator reads `!~X` so.
- `>TRUE` ("made sure", register) reads "are true": the causative is dropped from a quality's reading.

---

## Additions from the blind back-translation of W01 (`wf8/backtrans/W01.md`, 2026-09-28)

*The unit's Orrowen and GN were read back into English blind, with the specs, the lexicon, these additions and the tools only, and compared with the Book. Two rings drifted because of the translation (both fixed in the unit: r4, r11). The rest of what the comparison found is a spec gap of the A15 and A16 kind, proposed here for the §21 merge. No sign and no compound is added by the back-translation; one compound gloss is widened (`BENEATH+LIE`, above: "lie (flat) beneath").*

**A15, continued · readings a decoder needs from the register** (II.2). Each is a reading the concept register uses and a decoder given only the spec does not have (A15: "any register reading that is not its sign's own gloss belongs in this table").

| English | Grain | Where in II.2 |
|---|---|---|
| the world; measureless | `EARTH{all}`: all the earth | r3 "measureless, to the far edge of the world"; r7 "old in the world" (`→in @8`, the file where r3 cut it) |
| flat (laid along the ground) | `LIE` as a modifier: `BENEATH+LIE` "lie flat beneath", `LIE+TREE×3` "the flat wood" | r3, r14 |
| answer | `MOUTH` with a runner back to the one who spoke to it | r8 "and they answered" |
| not mis-X (must not be mistaken; no promise misheard) | `!~X`, the mirror of a seeming (the validator still reads "seem to not X"; finding above) | r10 `!~HEAR`, r11 `!~HOLD` |
| make sure (of it) | `>TRUE`, make it true (the validator reads "are true"; finding above) | r13 "We had made sure of it" |
| not leave out; keep (a fault, a debt) | `!LOSE`, not let slip | r13 "the grain will not leave it out" |
| as a branch breaks | `~HULL+BREAK` as a likeness, read by its parts: a bough's break. It is also the name of the thunder-tongue (*seil·rhass*, bough-thunder), which is the pun | r11 |
| for the moment … for always | a count of one on the act (`MOUTH#1`, said once) against a memory ray on what it made (always) | r11 |
| if any … is left, then … | a questioned mark with `{few}` and a *then* runner from it, where no ring is left for a fork (`NEW?{few} ⇒ HOLD`) | r14 |

**A16b · Referents, completed** [proposed; `grain_validate.py`'s reading]. A16 lets a belonging keep a file's referent only where a thing-sign has already introduced one. Read with no `# file` comments, II.2 lost five files that way:
- file 12 (**we**) became "name" from r9 and "shame" from r13: the teller stands on 12 by custom (§11.2) and no thing-sign ever introduces it, so the first belonging did;
- file 11 (**the grey**) became "earth" from r2: the grey has no sign (its band is its thing, A1), and the Mystlands, cut on its file as A9's naming substitute, took its place; ring 3's "the grey lay among the trunks and fed us" then read "earth lies down … feeds us";
- file 0 (**you**) became "the shore-men's three names" from r2: the ligature's head, NAME, is a belonging, and the doer is its modifier;
- file 2 (**your boats**, r12) kept the heart ring's "forebears": the boats are the modifier of their act (`HULL×3+GO½`);
- file 9 (**the water**, r5) read "the one on file 9": its referent is the WATER band alone.

Proposed rules (each is §11.2 read with §10.3 and A1, as A16 is):
- **(a)** A belonging never introduces a referent, whether or not a thing-sign has introduced one before it; the file keeps its bearing, or the teller.
- **(b)** A person's feelings are belongings: `SHAME` (our fault), `GLAD`, `GRIEF`, `ANGER`.
- **(c)** In a telling, file 12 with no thing-sign on it is the teller, *we* (§11.2's custom).
- **(d)** A condition band laid over a file's empty cell is that file's referent, the band as a thing (A1: the grey, the sea, the white), until a thing-sign stands first on the file; a later ring's band over the empty cell replaces an earlier band's.
- **(e)** In the heart ring and band I, a mark that a `NAME` runner from another file points at is the name given (A9's substitute for a naming pocket): a belonging of its file's referent, not a new one.
- **(f)** A thing cut as the modifier of an act, first on its file (`HULL×3+GO½`, the boats go; `STONEFOLK{only}+GO`, a man alone comes), is the act's doer and introduces it, unless the ligature is a named compound or the thing is a belonging.

A private copy of the validator with the six rules (`wf8/backtrans/W01_work/grain_validate_A16b.patch`, against `wf7/grain_validate.py`; about 60 lines in `is_belonging`'s table and `Reader.label`) passes its selftest, gives the same findings on all 13 rounds of `coverage/tests/` and the IV.4 pilot, and reads II.2 with no comments with every one of the five files right: "We (the teller) tend the grey's lying down", "The grey … feeds the trees' many trunks and us", "the trees: root to the water (file 9)", "The host (many hulls) turns aside … why, the wood does not hold". On the IV.4 pilot without comments it changes only likeness files and two outer referents, both for the better ("a shore-man alone" for "the one on file 5"; "a child … with its two arms" for "the one on file 11's two arms"). The shared validator is not edited (concurrency rule).

