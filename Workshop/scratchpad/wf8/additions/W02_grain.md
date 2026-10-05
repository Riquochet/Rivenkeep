### 21.W02 · Compounds added by the III.2 unit (W02: *The Thrones That Walk the Sea*, the ten hearts)

*wf8 unit W02, 2026-09-28. For `wf7/grain_v2.md` §21, to be merged by the builder (units may not edit the shared spec). III.2 carved whole as ten Throne hearts (§11.4): no new sign and no new rule. The six compounds below are modifier + head, as Seilrhass builds (mystaeri_spec §2.5); each soft reading is the compound of the two soft readings (computed, not coined; call §19.8). Without them the validator reads the ligatures part by part ("go beneath and sit", "breaking only stone", "raising many woods"), which is legal but misleading.*

| Compound | Means | Soft reading | Derivation | Where in III.2 |
|---|---|---|---|---|
| `DEEP+GO` | come late; go at the last; go long after | *eir·rei* | DEEP *eir* "deep; old; long; **last**" + GO *rei* "go". It is A9's own substitute for `GO{last}` ("came late", §18) in band I, given its reading | band I ring 1, "We came late"; Neivaere's ring 7, "We came long after" |
| `BENEATH+SIT` | sit beneath; take one's seat under | *senn·rass* | BENEATH *senn* "beneath" + SIT *rass* "sit; take one's seat" | Thaesaen, "We sat beneath Eldhythe's harbour"; Leavaren, "beneath the three spans" |
| `BENEATH+RISE` | come up from beneath | *senn·thael* | BENEATH *senn* + RISE *thael* "rise, stand" | Senneir, "We came up beneath" (its Judgement T-04 cuts `BENEATH+GO` and `RISE` apart) |
| `CARVE+SQUARE` | a carved stone: a stone that bears a carving | *seth·rhen* | CARVE *seth* "a cut, a carving" + SQUARE *rhen* "stone". Not the lie, `SQUARE+CARVE` (*rhen·seth*, "a cut that carries nothing"): the order is the meaning, modifier inward | Thaesaen, "the stones that pleaded for us" (the plea the wood cut in the mute stones, IV.2) |
| `RISE+WOOD` | a crane: a lifting-wood | *thael·veir* | RISE *thael* (with the causative, `>RISE`, "raise") + WOOD *veir*. §18 already gives it ("cranes … `>RISE`+WOOD"); only its reading is added | Naelthar, "the cranes that lifted the floating stones" |
| `BREAK+SQUARE` | a shard; a broken stone (in the STILL band, a shard of glass) | *rhass·rhen* | BREAK *rhass* "break; a crack" + SQUARE *rhen* "stone". Replaces the register's `SQUARE½{only}[STILL]` for a shard: outside a pocket a half-size line root reads as a **cited carving** (§8), so `SQUARE½` is the Mute Square cited, not a small stone | Neivaere, "among the broken glass, one shard among a thousand" |

```json
{"compounds": {
 "DEEP+GO": "v:come late (go at the last, or long after)|coming late|",
 "BENEATH+SIT": "v:sit beneath|sitting beneath|",
 "BENEATH+RISE": "v:come up from beneath|coming up from beneath|",
 "CARVE+SQUARE": "n:a carved stone (a stone that bears a carving)|carved stones",
 "RISE+WOOD": "n:a crane (a lifting-wood)|cranes",
 "BREAK+SQUARE": "n:a shard (a broken stone)|shards (broken stones)"
}}
```

**Readings a decoder needs (continuing A15),** for the builder to add to §21.8's table:

| English | Grain | Where |
|---|---|---|
| heavy (to carry) | `GREAT` on the carried thing's file (the validator glosses GREAT "great hull", its v1 hull sense) | band I ring 6, "a judgement is heavy to carry" |
| close the hand (a Judgement's own act, E5-01) | `HAND+CLOSE`, which the validator glosses "the kept hand" (E4-03's sense) | Thaesaen, "We closed it" |
| what was seen, the wood does not hold | `EYE → ∅`: A5's blind of place read by its role, the done-to not held ("whither" for a going, "what" for a seeing) | Neivaere, "what you saw in the grey, the grain does not hold" |
| put beneath; drive down (piles) | `>BENEATH` (the validator's own causative gloss, "put beneath"); the register's `>FALL` reads "fell" | Vaelress, "driven into the fen" |
| once there were no tricks | `DEEP+WOOD` with `TRUE{all}`: the old wood, wholly true (a trick is a hollow cut; `!~CARVE` cannot show whether the mirror or the hollow is outermost) | Esthaer |
| wait for, hope for (what has not come) | the *for* runner to the awaited thing, **cut hollow** (A6: shown, not yet so): `KNOT →for ~X`. A *for* target cut whole reads as a thing that happened | band I ring 2, "We were waiting for the sky to come again" (`12: KNOT →for 11: ~GO{again}`) |
| hard to look upon (too bright to face) | `FLASH`, hard light, on the one looked upon; `FLASH →as` another's FLASH is "and so were we" | Neivaere, "you were hard to look upon; and so were we" |
| hasty (the young wood of the Hasty Tide) | `NEW` (*lea*: green, young; the Hasty Tide's own syllable) | band I ring 1, "the young wood, green and hasty" |
| wrong, harm ("most wronged") | `STRIKE`, with the fringe for degree: `STRIKE{most}`, struck the most, wronged the most | band I ring 5, "where that haven had most wronged the wood" |

*The last four rows were added by the blind back-translation of this unit (`wf8/backtrans/W02.md`). Read without the first two, ring 2 came back "the sky came again to us" and Neivaere's close "our light was as your light" (both drifts, now fixed). Without the last two, "hasty" and "wronged" came back only as "young" and "struck" (nuance only; A15's standing rule still puts them here).*

**Two findings for the validator** (not rules; nothing here changes the spec):
- `pack_round` keeps the marks' cursors under the key `(pith, file)` and the pockets' under the bare file, so a pocket never sees the marks already cut on its files: a pocket laid across a file that holds marks in that ring lands in year 1 and raises K06 against later marks. Every pocket of the ten hearts stands on files that hold no mark in its ring, as the pilots' do.
- A half-size **line root** outside a pocket (`SQUARE½`, `SQUARE×3½`) reads as a cited carving. The register's shard (`SQUARE½{only}[STILL]`) should become `BREAK+SQUARE{only}` in the STILL band (above).
