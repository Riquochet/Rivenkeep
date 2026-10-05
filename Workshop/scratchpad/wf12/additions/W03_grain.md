# wf12 · W03 · GRAIN ADDITIONS (IV.4, The Gift Held an Hour, in the Book v3.0.0)

*For §21 of `grain_v2_full.md`, at the merge. No new sign and no new rule. Revised after the blind back-translation (`wf12/backtrans/W03.md`; the unit's BACK-TRANSLATION): rings 15, 16 and 17 re-cut, three decoder readings and findings 8–9 added, the compounds unchanged. Four compounds, each modifier + head as Seilrhass builds (mystaeri_spec §2.5), its soft reading the compound of the two soft readings (computed, not coined; call §19.8); eight decoder readings (A15, continued); and findings for the spec, the register and the validator. The unit is `wf12/units/W03.md`; its round is `wf12/tmp/W03/IV-4.gn2` (knowing form) and `IV-4.canon.full.gn2` (canonical).*

## 1 · Compounds

| Compound | Means | Soft reading | Derivation | Where in IV.4 |
|---|---|---|---|---|
| `DEEP+HEAR` | listen long; a long listening | *eir·seinn* | DEEP *eir* "deep; old; long" + HEAR *seinn* "hear; heed; listen", beside §21.7's `DEEP+HOLD` *eir·thein* "hold long" | ring 14, "with it came all of him: his long listening, and his last hour" |
| `DEEP+CARRY` | carry long; bear a long while | *eir·var* | DEEP *eir* "long" + CARRY *var* "carry; bear" | ring 20, "Then old arms, two pairs, slow, a long while" (`15: DEEP+CARRY{slow}`) |
| `LEAN+BURN` | a near fire; fire at hand | *ilen·esth* | LEAN *ilen* "lean toward" (the register's *near*) + BURN *esth* "burn; fire" | ring 20, "and fire, near and far" |
| `EDGE+BURN` | a far fire; fire at the edge (with `{most}` on the edge: the farthest) | *enth·esth* | EDGE *enth* "an edge; the rim" (the register's *far*, `EDGE{most}`) + BURN *esth* | ring 20, "and fire, near and far" (`10: EDGE{most}+BURN`) |

Without them the validator reads the ligatures part by part ("hear, old", "carry slowly, old", "lean toward and burn", "burn: most edge"), which is legal and misleading: DEEP as a modifier reads *old*, where these mean *long* and *far*.

```json
{"compounds": {
 "DEEP+HEAR": "v:listen long|listening long|",
 "DEEP+CARRY": "v:carry long|carrying long|",
 "LEAN+BURN": "n:a near fire (fire at hand)|near fires",
 "EDGE+BURN": "n:a far fire (fire at the edge)|far fires"
}}
```

## 2 · A15, continued: readings a decoder needs

| English | Grain | Where |
|---|---|---|
| a jolting (being carried, struck again and again) | `STRIKE½{again}`, small blows, again, on a placeless file, `→` us | IV.4 r20 |
| a day (a length of time) | `FLASH#1`, one day (the register's *day*), the target of a *through* runner | IV.4 r20 |
| half a life (a length of time) | `LIVE{half}`, the target of a *through* runner | IV.4 r20 |
| two pairs (of arms); one pair | `HAND:stem#4`; `HAND:stem#2`: four arms, two arms | IV.4 r20, r21 |
| never a hand | `!HAND` on the file of *whoever holds us*, with a memory ray (never, A6) | IV.4 r20 |
| the whole of him (what came with his blood) | `MIND{all}`, his whole mind (a belonging, A16) | IV.4 r14 |
| his last hour | `TIDE{last}`: a ring is an hour of the wood (the register's *hour*), its tide the growth of it | IV.4 r14 |
| set the blade to (a body) | `AXE →` the part, on the doer's file (the validator reads the act, "fell with iron") | IV.4 r11 |
| would ask no X that one gave not (no asking without the giving) | a **bind** whose strands are the asking and the giving: `MOUTH? →for` X, `MOUTH? →` bind, `GIFT+X →` bind; the bind's out-runner `⇒` the deed (*he gave it all*). Not `MOUTH?{only} →as GIFT+X`, which a blind reader hears as "asked only for X" | IV.4 r15 |
| never joined (a joining meant and not done) | the joined marks cut hollow **and** the bind's strands hollow: `~HAND:stem →` bind `~`, "a seeming arm (shown, not meant)", so the seeming shows in the readings (finding 8) | IV.4 r16 |
| of all X, the one that could have (we alone) | the hollow act with `{only}`, `→in` the company it is one of: `~MOUTH{only} →in ~SQUARE×3{all}`. With no company to range over, `{only}` is heard on the act's other runner ("only to you") | IV.4 r17 |

## 3 · Findings (none blocks anything)

1. **Twenty-four rings, and a leaf of twenty-five paragraphs.** v3's IV.4 has 25 paragraphs between the seals; a telling may have at most 24 rings (§3; validator H05). The twenty-fourth paragraph is the italic sentence, which is the gift's own round (mystaeri_spec §5.4) and is cited by ring 23 (§8, a whole round cited), so it needs no ring of IV-4. **Proposed** for §11.2 item 1: *a paragraph that is a cited round is drawn as that round, beside the ring that cites it, and takes no ring of its own.* The Legends builder should pair that paragraph with the cited round, not with a ring.
2. **`AXE+GO` now reads as W06's compound** ("the iron's coming (the felling going on)", §21.9.2), and so does every ligature keyed `AXE+GO`, including the pilot's `AXE+GO½` ("the blade goes a little way"). IV.4 r13 was re-cut around it (the rite's own `>WOUND½`, and `DEEP+WOUND`); a compound that reads a felling should not catch a blade's going. **Proposed:** gloss `AXE+GO` "the iron goes (comes; the felling goes on)", which serves both.
3. **A sign of the act class alone, used as a thing.** `AXE` stands for *iron, blade, axe, saw* in the register, but alone it reads only as the act ("fell with iron"); IV.4 r11's "the blade" is carried by the reading of the whole knowing. A noun reading for `AXE` with no runner from it (the iron, the blade) would help a decoder, as `DOER_NOUN` already gives *the iron* for AXE as a ligature's first part.
4. **The v1 sample's "all files".** `wf8/grain3/texts/GIFT.gn2` writes v1's *band MIST r4 all files* as `band MIST files all`, which the validator cannot read (P02, and a stray D02 after it). Written `files 0–15` it is clean. **Proposed:** either the validator reads `files all`, or the v2 text of every v1 sample writes `0–15` (§13.7).
5. **A band, a celled year, and a silence.** IV.4 r10's *he was silent* could not be the STILL band (A20: the meeting crown shares its year with the rising and the taking), so it is `!MOUTH`; r20 gives each of its five *Then*s files of its own so that its two DARK and two WHITE bands each lie over one year of one file. A20 is doing its work; the register's *silence, silent* row (`!MOUTH ; >STOP ; [STILL]`) might say which to prefer in a celled ring.
6. **The pilot's second break could not stand.** "And we were the one his foot found" is its own paragraph in v3, so the finding (ring 18) cannot cross and break the could-have-spoken (ring 17) (B12: a break needs two runners in one ring). It is a then-runner across the ring-line instead. If Jack wants the break back, rings 17 and 18 would have to be one paragraph.
7. **Pockets and the packing** (§21.9.6 item 1) held: every pocket of IV.4 stands on files with no mark in its ring (P1 2–3, P2 3–4, P3 9–10, P4 2–4, P5 3–5).
8. **The validator's readings drop a hollow runner's `~` on a bind's strand** (for §21.9.6; the validator is shared and is not changed here). `run p1 … → bind K1 ~` is read "an arm — a strand of the bind K1" (plain) and "[an arm] —to→ [the bind K1]" (`--literal`), with no "(a seeming)": the plain reading's strand branch returns before the hollow and smoothed flags are added, and `--literal` prints no runner's flag at all (a test round in `wf12/tmp/W03fix/t/h.gn2` shows both). IV.4's blind reader, working from those readings, gave ring 16's never-pressed arms as "bound". The unit now cuts the arms hollow as well, so the seeming shows in the marks; the readings should print the flag on every runner, a strand included.
9. **The gift's v1 round, read under v2's ring rule** [Jack]. In IV-4-gift (mystaeri_spec §5.4; kept whole by §17, "every v1 sample keeps its GN, and its meaning, exactly") `FLASH` stands first on file 3 in ring 7, so §11.2's ring rule makes the hard light file 3's referent, and the validator reads ring 10's `DYING` "Flash (hard light) dies", where the canon reads "the pillars' breath dying" (*for the sky is dying*). The blind reader followed the rule. The Book prints the round with Seren's `# file` lines, which hold file 3; the blind GN has none. **Proposed** for §17: a v1 sample's referents are read by v1's band rule, or its `# file` lines count as part of its GN; else, A16's belongings take in a thing's own light (`FLASH` on a file whose referent is already there). Not re-cut here. The same reader also missed what the round does carry (its memory ray, *always*, read "remember"; ray 3, the pillars' breath as the grey over us), which is the reader's slip, not the round's.
