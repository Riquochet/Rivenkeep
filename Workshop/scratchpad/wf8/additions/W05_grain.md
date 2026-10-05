# W05 · V.3 The Wreck That Went Home · grain additions (proposed; not yet in grain_v2.md)

*wf8 unit W05. Compounds and one register reading that V.3's whole carving uses. Each compound is modifier + head, as Seilrhass builds (mystaeri_spec §2.5); its soft reading is the compound of the two soft readings (computed, not coined; call §19.8). No new sign and no new rule of the notation was needed. Without these glosses the validator reads the ligatures part by part ("an own bearer", "going beneath and being struck", "stone goes beneath"), which is legal but misleading. To be merged into grain_v2.md §21 (a new §21.x "Compounds added by V.3") by whoever owns the shared spec.*

## Compounds

| Compound | Means | Soft reading | Derivation | Where in V.3 |
|---|---|---|---|---|
| `LONE+BEARER` | the bearer ahead; the bearer going before the rest | *ith·varen* | LONE *ith* "one goes ahead of the rest" (its line-root gloss) + BEARER *varen* "a bearer; a laden hull" | ring 1, "and the bearer ahead" |
| `LONE+GO` | go ahead; go out in front of the rest | *ith·rei* | LONE *ith* "one goes ahead of the rest" + GO *rei* "go": the Lone Stroke's own act (*Go until struck*; *One goes; the rest follow the quiet*) | ring 7, "we went out in front" |
| `BENEATH+WOUND` | a low wound; struck low, under the water-line | *senn·thaess* | BENEATH *senn* "beneath; low" + WOUND *thaess* "struck; the bark splits" (as DEEP+WOUND *eir·thaess*, §21.7) | ring 2, "the iron went into us low and through" |
| `SQUARE+BENEATH` | the lee of a stone; the low, sheltered side of a wall | *rhen·senn* | SQUARE *rhen* "stone; the wall" + BENEATH *senn* "beneath; low; the lee" (the register's own reading of BENEATH for "in the lee of that stone"). Distinct from BENEATH+SQUARE (the canyon, head and modifier the other way) | ring 8, "we went down in the lee of that stone" |
| `MORROW+HULL×3` | the next hulls: the hulls of the next coming | *leis·seilen* | MORROW *leis* "the morrow; the next coming" + HULL×3 *seilen* "hulls" | ring 9, "the groves where the next hulls stood growing" |
| `BEARER+HEART` | the bearer's heart (a heart as a referent of its own, the bearer's) | *varen·saen* | BEARER *varen* "a bearer; a laden hull" + HEART *saen* "a heart; heartwood". Added after the blind back-translation (`wf8/backtrans/W05.md`): a plain `HEART` standing first on the bearer's file introduces "a heart" there by §11.2 (A16 does not list the heart as a belonging), so the bearer was lost from rings 6–7 | ring 6, "quickest to the heart of the bearer, and from the heart to all" |

```json
{"compounds": {
 "LONE+BEARER": "n:the bearer ahead (going before the rest)|bearers ahead",
 "LONE+GO": "v:go ahead (out in front of the rest)|going ahead|send ahead",
 "BENEATH+WOUND": "n:a low wound (struck low, under the water-line)|low wounds",
 "SQUARE+BENEATH": "n:the lee of a stone (its low side)|the lees of stones",
 "MORROW+HULL×3": "n:the next hulls (of the next coming)|",
 "BEARER+HEART": "n:the bearer's heart|"
}}
```

## A register reading to add to A15 (grain_v2 §21.8)

| English | Grain | Where |
|---|---|---|
| not empty (of a silent stone): not spent | `!SPENT`: SPENT "a spent hull; worthless" mirrored, as the Tide of Remembering's own carving asks of a silent stone "Is it spent, or waiting?" (E3-08, `SPENT?` and `KNOT?`) | V.3 r10, the groves' lesson "a stone may be silent and not empty" (`SQUARE+!MOUTH →with !SPENT`) |
| know rightly; hold (it) true | `TRUE+HOLD` cut **on your file** (file 0, where the telling's "you" stands by Seren's file tag), with no runner: the compound's literal "hold true", which as a telling's injunction is "know this rightly", not "believe". Without the tag, file 0 is the wall, and the mark reads "the wall holds true": the reading needs the tag | V.3 r10, "Know this rightly." |

## Findings (for the spec's owner; none blocks)

1. **A9's list misses one V.3 heart item.** A9 lists V.3's band-I substitutes as `{more}` and the caution. Ring 2 (band I) also holds a knowing that §18 gives as a cut-pocket, "where a stone flashes, a gun is" (`{ SQUARE+FLASH ⇒ GUN }`). Band I takes no pocket, so it is cut plainly: `0: FLASH ⇒ 0: GUN` on the wall's file, with the young wood's learning and the roots' carrying run to the FLASH. Propose adding it to A9's V.3 entry.
2. **The concept register's `!~` ("silent and not empty") reads backwards in the validator** ("a seeming no stone"). V.3 uses `!SPENT` instead (row above), from the carvings' own vocabulary. Either the register row or the validator's reading of `!~X` wants a fix.
3. **`DEEP+KNOT` is Eirlenth's name** (with the WHITE band). V.3's "how long it waits" is therefore cut `KNOT?` (the wait, in question), not `DEEP+KNOT?`, so no reader sees a Throne's name in the hand's waiting.
4. **The proof rings' `!NEW+HOLD`** (coverage/tests/V-3_proof.gn2, r10) puts the mirror on the modifier ("old-hold"); the leaf cuts `NEW+!HOLD` (the head mirrored), as every negated ligature of IV.4 does (`TIDE×3+!HOLD`, `HAND+!RISE`).
5. **The proof's `→in @11` "into the grey"** made file 11 (our kin) stand for the grey through a band alone, which §11.2 does not allow (a band is not a thing-sign). The leaf cuts "back into the grey" as the MIST band over our own going and a runner to `@8` (behind: home and the grey).

## Findings from the blind back-translation (`wf8/backtrans/W05.md`, 2026-09-28)

The unit was read back blind from its native lines alone (no `# file` tags, as IV.4's test was). Six errors were found and mended in `wf8/units/W05.md` (§2, §4); the spec-level causes are below, for the spec's owner. None changes a sign; none needs a new rule of the notation.

6. **An act is its file's referent's act, so "X went out of us" is not `GO` on our file.** Rings 4–6 cut "the flash … went out of us into the roots", "where we were struck went out of us too" and "the dread went out of us … it went to every hull" as `12: GO`, which reads (§10.3) "*we* went into the roots / back to our kin / to every hull". Mended as the causative on our file, `12: >GO` ("we sent it"), with `→` the thing sent and `→in` the goal (`→in @5` into the roots, `→in @11` among our kin, `→in 7` among every hull). Proposed for A15: *go out of (us) into …*: `>GO` on the source's file, `→` the knowing, `→in` where it goes.
7. **`>GO` is "make go; send", never "let go".** "The guns let us go" was `GUN×3+>GO?`, read blind as "did the guns fire after us?", the reverse. A15 already gives *let go* as `!HOLD →`; mended to `GUN×3+!HOLD?`.
8. **A condition band is a surrounding, not an event.** "And the sea came in" (r2) and "with the sea in us already" (r8) were carried by the WATER band on our own file, which reads only "on the water": true of every hull, and silent about the sea coming in. Mended by carving the sea as a doer: `4: TIDE  4: GO →in` the low wound (r2), and in r8 `4: TIDE  4: GO{still}` with our `!TURN@2 →bc` it, the two tides joined by `ray 4: r2/1–r8/1` (the same sea, still coming in).
9. **A16 misses the heart; §11.2 then lets a belonging take a file.** A plain `HEART` first on the bearer's file (r6) made "a heart" the referent (read blind as the host's heart; the validator reads "heart"). A16 lists mind, word, name, breath, hand, eye, bones and blood, but not `HEART`. Proposed: add `HEART` (a person's or a hull's heart) to A16's belongings. The leaf now cuts `BEARER+HEART` (compound above), which reads right under either rule. Likewise **a stone's `FLASH`**: `0: FLASH{still}` first on the wall's file in r8 made "the flash" file 0's referent through rings 8 and 10 ("the flash believes", "the flash's hand"); the leaf now cuts `0: SQUARE  0: FLASH{still}`, and A16 might list FLASH on the file of a SQUARE or GUN as a belonging.
10. **A hollow likeness keeps its file.** Ring 5's likeness puts a hollow `~STONEFOLK` first on file 3; by §11.2 file 3 is then "a seeming shore-man" until a new thing-sign stands first, so ring 8's surf (`3: BREAK  3: CARRY`, acts) read "a seeming shore-man breaks, carries". Mended by cutting the surf on file 15, which no referent holds after the heart ring. Proposed for §11.2 or A16: a hollow mark (shown, not meant) introduces its referent for its own knowing only, since a likeness is "not present in the knowing" (§10.9).
11. **A quality on a file is its referent's.** "The hand behind your wall is new to each of them" was `0: NEW`, which reads "[the wall / you] is new to every fleet", against the knowing before it ("every fleet … holds your wall"). Mended to `0: HAND+NEW` ("the wall's hand, new to every fleet"). Note: `NEW+HAND` with a runner reads as *touch* ("lays a hand on"), the register's `HAND →`; and B13's `STONEFOLK+HAND` reads "five shore-men" (v1's X+HAND is *five*), so the plain `HAND` on the wall's file stays the leaf's hand.
12. **Bands spread across cells when a ring is packed** (an observation; nothing in V.3 needed mending). A band is written for one knowing, but §3.6 and §4.3 lay it over a file's whole *year*. In a celled ring, knowings on one file share a year, so the band covers every mark in that year. In V.3's ring 8, the cold (WHITE) written for "we lay" also lies over our turning, our wound and our going down: true here, but a leaf where it is false would need the band to be per cell, or the knowings kept in separate years.
