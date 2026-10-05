# RIVENKEEP · BLIND BACK-TRANSLATION · PILOT I.1 (*COVV TRESKAT*)

*wf7 workflow document, 2026-09-28. Scratch only: it is not a Book leaf or a repo doc. This is a test of `wf7/pilot_I1.md`, the tier-3 Orrowen of I.1: can the Orrowen be read back into the Book's English using only the specs, the lexicon and the tools? Where it could not, this file finds the cause and fixes it if the cause was an error. No canon text was changed.*

**Result.** Of 24 paragraphs, 12 came back **exact**, 6 **close**, 4 with **drift** and 2 **wrong**. All 6 drifts and wrongs trace to 9 clauses. The fixes are:
- **Translation:** 8 clauses corrected in 7 lines of the leaf (the 9th clause is the *Pellow Vell* epithet; see below).
- **Lexicon:** 3 rows mended.
- **Spec:** 4 lines clarified (§3.5, §3.6, §3.8, §5.10).
- **Analyzer:** 2 defects fixed.

After the fixes, `orr_analyze.py` reports 0 unknown and 0 ill-formed words across the leaf (72 lines, 1,020 words), and `--test` still passes all 87 samples. The epithet *Pellow Vell* is a homophone, not an error. It is flagged in the lexicon and the analyzer, and left for Jack.

---

## 1 · Method, and how the test was kept blind

1. **The blind file.** `wf7/blind_I1.txt` holds only the Orrowen and notation lines of the pilot, taken by line number. The 29 blockquoted Orrowen lines are the title, headnote, telling, Title, verse, hearth's answer, facing leaf and Seren's line. The two notation lines are the Title's dry cut (line 150) and Seren's leaf-hand token string (line 265). To choose those lines, only the first 14 characters of each pilot line were looked at. The English, the word-for-word lines and the notes were left out.
2. **The reading.** The blind text was read with only these sources:
   - `orrowen_v2.md` §0–§3 (grammar and stone grammar), §5.10–§5.12 (small words, numbers, affixes);
   - `lexicon_orrowen.tsv`, including its phrase rows;
   - `orr_analyze.py` (check and `--gloss`);
   - `grain_validate.py`.
   
   `grain_validate.py --md pilot_I1.md` finds **no Grain Notation v2 round** in this leaf, and exits 0. The facing leaf is bare rings, as the pilot says. So the only "grain" on I.1 is the course-hand notation: the Title cut dry and Seren's line in the leaf-hand.
3. **Frozen before the look.** The back-translation was written to `wf7/bt/blind_backtrans_I1.md` before the pilot's English was opened (sha1 `fc31ed47…`, 2026-09-27 23:52). It is reproduced unchanged in §2. Only then was `pilot_I1.md` read in full and compared.
4. **Limitation.** Once the English had been seen, no second blind reading was possible. The post-fix readings in §6 are the analyzer's glosses of the fixed lines, with a reading that follows the rules. A fresh blind reader should re-read the seven fixed lines (§7, item 1).

## 2 · The blind back-translation (as frozen, before the English was seen)

*[?] marks the reader's own doubts at the time.*

> **[20]** The Riven Cloak.
>
> **[28]** Laid down by Sergeant Kael, Kael the Counter, oath-keeper of the True Men, on the first night this hearth asked for a tale. He did not let me change a word of it, and I have not changed one.
>
> **[40]** Give me the stone. I will not sit; I will stand. I have sat enough this winter.
>
> **[46]** I swear upon the lintel of the western stair, on which the old wardens cut their names: I will lay this true, because I have no other way of laying it. It stands. I was on the gate that day. I am a counter of things, not a singer; and anything I did not count, I will not lay before you.
>
> **[57]** The column came in at dusk, and I counted it as it came in: old men, and women with packs, and children asleep on their feet, and soldiers of six broken companies who did not yet know [the fate of] their captains [?]. Two thousand and a few hundred. We had walked a month to the keep, and we came in to a heap of rubble. One hinge of the outer gate held. The grass was up to the knee in the courtyard behind. The songs had laid a great hall there, but the roof had fallen, and there was snow on the hearth where you sit now.
>
> **[69]** Some shook. Some wept. Some fell, and did not rise.
>
> **[73]** Then the crying-out rose, and it was not one cry. Some cried: Send to the grey sails and ask for terms! [?] But no one had understood one word the grey sails said. Some cried: To the high passes, and the snow beyond! Some cried: Go down into the cellars of the Keep, and bar the doors, and wait! As if the sea would forget us. I have heard men break, at times. I had never heard a people break. It is a sound like river-ice going out.
>
> **[86]** Now I will tell you what the Captain was, and first what he was not. He was not a general, and the generals had been killed. He was not a politician, and the politicians were forgotten. He was not a lord, and the lords had been thrown down. He was not a Stonewright, and the guild sat in the grass with their chisels in their laps and despaired. He was the captain of a small company, and we were his company. He found us one by one, in companies and on the roads, until there were twelve; and he held us with nothing but trust. We were soldiers who kept our oaths, who built what we promised, who fought alone when the end was sure. That is everything a True Man is. I tell it you so that you know it: it is not much. But it is not small.
>
> **[98]** He did not want to lead. I swear to that a second time. It stands. All through the long retreat he waited for someone to whom the command belonged; and no one took it from him, because the leaders were dead. Do not mistake me. Great men did not come out of him [?]. He was not one. I do not think he ever once breathed like one.
>
> **[108]** The True Men looked to their Captain. The Captain looked at the wall.
>
> **[114]** Then he climbed. He took a coal from the dead hearth as he went through the hall, and I did not know why. He went up the broken face of the inner wall, alone, by the stones that stood out from the mortar; and we stood at its foot and let him go, because he had not said to us: Follow. At the top, where the wall still stood whole, he took off his cloak. It was a proper soldier's cloak, crimson once, and gone to the colour of old brick. He tore it down the back. He took a pike from the rubble, and had it half knotted to it [?]. Then he knelt on the capstones with the coal, and wrote, slowly, as a man writes who has not written much.
>
> **[128]** I was the first to follow him up, and the first to read it. I read it aloud, and my voice did not hold, and I will not lie about it:
>
> **[138]** IN MEMORY OF OUR HOME, OUR FAMILIES, OUR GOD, OUR FREEDOMS, OUR PEACE.
>
> **[150]** *(the Title cut dry)* Memory [of] home · families · God · freedoms · peace.
>
> **[156]** He set the pike in the cleft of the wall and gave it to the wind. That was the last unbroken wall of the Shore, and that was the banner on it.
>
> **[164]** Now hear who answered, and in what order, for I counted. The True Men answered first, and I will name them, because a count is not a count until the naming. Stannard of the Ridge, the quarryman. Corlen of the Harbour. Tamm of the Three Bridges. Marl the Fen-born. Aske of the Forest-Roof. Garvel of the Smithies. Harl of the Shore that Burns. Ulden of the Galleries. Hesk of the Mere. Lanner of the Crags. Pellow of Song [? the lexicon's phrase row says "of the Spire"]. And Kael the Counter, oath-keeper of the True Men: that is I. I have no haven, because he found me on the road. Twelve. I counted us twice, and it did not take long.
>
> **[175]** Then the soldiers of the six companies, who had walked the long retreat at our shoulder; they are our troops now, each True Man one troop, and they trust us as we trust him. Then the people of the column, who had carried their children on their backs through the passes: one voice, and twelve, and then hundreds and hundreds; and then I had no count left, and I gave up trying. It is the only time I have stopped. It was not by order, for he gave none. He wrote only what we still had, and it was enough.
>
> **[185]** That is why the pennant of our keeps is blood-red. It is the colour of that cloak.
>
> **[191]** He is sitting there now, at the end of the bench, with his hood up. He will tell you: it was not like that. It was like that.
>
> **[199]** This I lay as it was laid for me.
>
> **[207]** Then the True Men made it a song, as they still sing it:
> *Gate broken, lords thrown down, / gathering at the shore, the grey sails; / a lone one climbed the loosened stones / and tore the cloak upon his shoulder. / He wrote five things to die for, / and none of us wanted a sixth.*
>
> **[243]** And the hearth said: We remember.
>
> **[251]** On the facing leaf there is only the grain of the wood, and one line:
>
> **[261, 265]** Untold. Halyna cannot yet hold this deep. *(The leaf-hand string, read letter by letter: the same line, with the softening bite on b in* nawrodhat*, the bedding bite on d in* noss*, and the lintel over* Halyna*.)*

## 3 · The comparison, paragraph by paragraph

Scores: **exact**, the same meaning (small word choices aside); **close**, the same meaning with a nuance lost or added, or a difference built in on purpose; **drift**, one clause says something noticeably different; **wrong**, one clause says something else, or the opposite. A paragraph's score is its worst clause.

| ¶ | Pilot line | Score | Where they differ (back-translation → the Book's English) | Cause |
|---|---|---|---|---|
| 1 | 20 title | exact | "The Riven Cloak" → "The Torn Cloak" | *treskat* is both |
| 2 | 28 headnote | exact | "He did not let me" → "He would not let me" | none |
| 3 | 40 | close | "I will not sit" → "No" | by design: Orrowen says no by repeating the verb (§3.4) |
| 4 | 46 | close | "lay this true" → "tell this plain"; "It stands" has no English | *venn* is both true and plain (straight); *cadh* "lay" is the tongue's word for telling. *Ston.* is the pilot's declared liberty (its note 1) |
| 5 | 57 | **drift** | "soldiers … who did not yet know their captains" → "who no longer knew their officers" | **translation error**: *nath … tul* is "not yet" in the canon (Seren's *Nath noss tul kethyl*), and was used here for "no longer". **Spec gap**: the tongue has no "no longer", and nothing said so |
| | | | "One hinge of the outer gate held" → "The outer gate hung from one hinge" | inherent ambiguity: *hos brellir et ganna hyvenn* reads as subject + object, or as a construct. The meaning survives either way; not fixed |
| 6 | 69 | exact | "did not rise" → "would not rise" | none |
| 7 | 73 | close | "no one had understood" → "no one had **ever** understood"; "at times" → "before" | **translation omission**: "ever" had no word (*fedh*); fixed. The pilot's own table accepts *fedheth* for "before" |
| 8 | 86 | **wrong** | "who fought **alone** when the **end was sure**" → "who fought **only** when the **cause was just**" | **translation error**: *hosel* after a verb reads "alone", and so does *dask*. With "alone", "the end" reads as the end of the fight, not its purpose. The True Men's creed came back as a last stand. **Spec gap**: no rule said how to say "only" of a clause |
| | | | "the lords had been thrown down" → "the nobles were scattered" | **lexicon error**: *drig* is "throw; fling; scatter", but its participle row *driget* carried only "thrown" |
| | | | "in companies" → "in garrisons" | *kest* is both; not an error |
| 9 | 98 | **wrong** | "Great men did not come out of him. **He was not one.** I do not think **he ever once breathed like one**" → "It was not that the greater men were gone. There was no greater man. I do not think **his equal** ever lived" | **translation error**, from two ambiguities. (a) *re orrant uldath strom hyo*: after *orr* "go", *hy* reads "from" (*orr hy* "leave"), not "than", so "men greater than he had not gone" read as "great men went from him". (b) *re hoss fedh o hosen*: *h* does not soften, so nothing marks *o* as "his", and it read as "he … like one". The result is nearly the **opposite** of the English. **Spec gaps**: §3.6 never said *hy* is also "than"; §3.5 never said the possessive can be unmarked |
| 10 | 108 | exact | none | |
| 11 | 114 | **drift** | "a **proper** soldier's cloak" → "a **plain** soldier's cloak" (ordinary, not an officer's) | **translation error** from a **lexicon** gloss: *venn* lists "plain" without saying which plain. It is "plain" as in "tell it plain", not as in "ordinary" |
| | | | "had it **half knotted** to it" → "bound **the half of it** there" | **translation error**: *re yal o saed bysket*, meant as "its half was bound". *s* does not soften, so *o* read as "it" and *saed* as "half-(way)". Same §3.5 gap as ¶9 |
| 12 | 128 | close | "my voice did not hold, and I will not lie about it" → "my voice was not steady, and I will not pretend it was" | none |
| 13 | 138 + 150 Title | exact | leaf-hand and dry cut both read the Title exactly | |
| 14 | 156 | exact | "the cleft" → "a crack"; "the Shore" → "the Shorelands" | none |
| 15 | 164 | **drift** | "Pellow **of Song**" → "Pellow **of the spire**" | **homophone**, not an error: the epithet *Vell* is S·*pell* "spire" in the construct, and also the plain word *vell* "song". The analyzer picked "song". The lexicon's phrase row had the right reading, and the reader distrusted it. Flagged (§5); not changed |
| 16 | 175 | close | "twelve" → "a dozen"; "hundreds and hundreds" → "hundreds"; "at our shoulder" → "beside us" | by design (Kael counts); none |
| 17 | 185 | exact | "blood-red" → "crimson"; "pennant of our keeps" → "pennant on every keep of ours" | *lorr* is both; the pilot's own §3 collision note |
| 18 | 191 | exact | none | |
| 19 | 199 | exact | none | |
| 20 | 207 | close | "made it a song" → "sang" | reader's paraphrase |
| 21 | 211–216 verse | **drift** (line 1 only) | "lords **thrown down**" → "lords **scattered**"; "none of us wanted a sixth" → "none of us has needed more" | the *driget* lexicon error (¶8). The sixth is by design (the pilot's verse note) |
| 22 | 243 | exact | none | |
| 23 | 251 | exact | none | |
| 24 | 261 + 265 | exact | Seren's line, and its leaf-hand string, which is identical to `orrowen_v2` §11.4 | |

**Tally:** 12 exact, 6 close, 4 drift (¶5, ¶11, ¶15, ¶21), 2 wrong (¶8, ¶9).

The two wrong paragraphs both hold a statement of character: what the True Men are, and that there was no greater man than the Captain. Both failed on the same weakness: a small word with two readings (*hosel* alone/only, *hy* from/than), in a position where the wrong one is the natural one.

## 4 · The fixes

### 4.1 Translation (`pilot_I1.md` blockquotes, word-for-word lines, notes; `pilot/i1_draft.txt`)

| ¶ | Before | After | Reads |
|---|---|---|---|
| 5 | *sa nath re seskent tul so hrenneth* | ***sa re vammant so hrenneth*** | "who had lost their captains" (*mamm* "lose", S after *re*; *vamm* has no other source, since *b* softens to *w*) |
| 7 | *Veth re hyrril nahos hos brod* | ***Veth re hyrril nahos fedh hos brod*** | "but no one ever understood a word" |
| 8 | *sa re yorrar hosel amm ew venn et dask* | ***sa nath re yorrar veth amm ew venn et dask*** | "who fought not but when the cause was just", which is "only when". It is the leaf's own *lo nayalat veth osk* shape |
| 9 | *Nath re orrant uldath strom hyo. Nath re yal hos.* | ***New hy vodh re yalant et uldath strom sennet. Nath re yal hos strom hyo.*** | "It was not because the great men were dead. There was not one greater than he." Kael still counts and gets none, and *hyo* now stands where only "than" fits |
| 9 | *Nath gaeverym re hoss fedh o hosen.* | ***Nath gaeverym re hoss fedh uld hosen et Crenn.*** | "I do not think a man like the Captain ever breathed." |
| 11 | *Ew covv venn hesperd o* | ***Ew hosel covv hesperd o*** | "It was only a soldier's cloak" (the pattern of the facing leaf's *Doss hosel meskdhrenn*) |
| 11 | *eth re yal o saed bysket umo* | ***eth re yal saed et covv bysket umo*** | "and the half of the cloak was bound upon it" (the possessor as a noun) |

In the pilot, each fix is marked *(Back-translation fix.)* in its paragraph's notes, with the misreading it cures. The word-for-word lines now match the new Orrowen. The pilot's §4 table ("Where the Orrowen is built differently") gains four rows, and its grammar table gains **G8** ("only" = *nath … veth*), **G9** (the possessive before a letter that does not soften) and **G10** (*nath … tul* = "not yet" only). The header counts are updated: 1,020 words, of which 827 are canon, 96 reserve and 97 tier-3. The reserve-root list gains *mamm* (62 roots).

### 4.2 Lexicon (`lexicon_orrowen.tsv`, rows edited in place; no row added or renumbered)

| id | Row | Change |
|---|---|---|
| O0505 | *driget* | "thrown (the participle)" → "thrown, flung; scattered (the participle: all three senses of *drig*)" |
| O2715 | *venn* | "plain" → "plain (straight, honest: 'tell it plain'; NOT 'ordinary': a plain soldier's cloak is *hosel*, 'only a soldier's')" |
| O2880 | *Pellow Vell* | derivation gains "NB homophone: *Vell* also reads as *vell* 'song' … the epithet is the construct, S·*pell*" |

### 4.3 Spec (`orrowen_v2.md`, one clarifying line each, marked "Back-translation of pilot I.1")

- **§3.5, pronouns.** When the mutation cannot show, nothing marks the possessive. This applies before *f, v, w, th, dh, s, h, l, r, n* or a vowel after a softening possessive, and likewise after *en, ol, va*. In that position *o saed* reads "he/it, half", and *o hosen* reads "he … like". So say the possessor as a noun, or recast.
- **§3.6, prepositions.** *Hy* is also "than" (*hos strom hyo*, "one greater than he"). After a verb of going, the "from" reading wins, so a comparison is not set after *orr*.
- **§3.8, negation.** "Only" of a clause is *nath … veth*, "not … but". *Hosel* set after a verb reads "alone". *Nath … tul* is "not yet", never "no longer", and the tongue says "no longer" another way.
- **§5.10, small words.** The *tul* row adds: *nath … tul* is "not yet", never "no longer".

### 4.4 Tools (`orr_analyze.py`)

- **The suppletive past takes person endings only.** In `layer_fits`, *yal*/*gal* no longer take a participle or a noun ending, and the inflected *yala, yalan, yalant, yalar, yalith, yalom, yalos* take no further layer. Before this, *yalatath* ("things", S·*galat*-PL, in *El nydherd yalatath en*, "I am a counter of things") was glossed "was-PTCP-PL" through *yala* + *-At* + *-Ath*. It now reads S·anything-PL. The blind reader had worked around it, so this cost no fidelity, but it is a trap for the next reader.
- **An epithet after a name also shows its construct reading.** In `context_check`, when a capitalised word follows a name and the unmutated reading has won, any softened-possessor reading is added as a note. *Pellow Vell* now glosses "song" with the note "or, as an epithet construct after a name, S·pell 'spire' (§3.10)". In the whole leaf only *Vell* triggers it.

## 5 · What was not fixed, and why

- **The *Pellow Vell* homophone (¶15).** This is the construct doing what §3.10 says. It is the same kind of accident as *vess* "night" / *re vess* "asked", which the pilot keeps. Names are the Book's, so the choice is **[Jack]'s**. If a clear reading is wanted, the grammar offers ***Pellow Pellen*** ("of the spires", an adjective like *Marl Sedhen* and *Lanner Gynten*, which does not mutate). Otherwise the chime stays, now flagged in the lexicon and the analyzer.
- **Subject + object vs construct (¶5, "one hinge").** *Re heth hos brellir et ganna hyvenn* reads as either "one hinge held the outer gate" or "one hinge of the outer gate held". A definite possessor starts with *et*, which never mutates, so no bite tells the two apart. The sense survives either way, so it is noted, not legislated.
- **Differences built in on purpose.** These were scored close, not counted as errors:
  - "No" said as *Nath reskym* (§3.4);
  - the two *Ston.* after Kael's oaths (the pilot's note 1);
  - *fedheth* for "before";
  - "twelve" for "a dozen", and *lesk murr eth lesk murr* for "hundreds";
  - *vranast* "a sixth" for "more";
  - the quoted cries for reported ones.
- **Polysemy that the context carries.** *venn* true/plain in "tell this plain", *kest* company/garrison, and *lorr* blood/crimson each cost at most a nuance.

## 6 · Re-running the tools after the fixes

| Check | Result |
|---|---|
| `python3 orr_analyze.py --file pilot/i1_draft.txt` (the whole leaf; report rewritten to `pilot/i1_report.txt`) | 72 lines, **1,020 words, 0 unknown, 0 ill-formed**, exit 0 |
| the pilot's blockquoted Orrowen re-extracted (`bt/orr_lines_after.txt`) and checked | 29 lines, 0 unknown, 0 ill-formed. Diffed against the blind text, only the seven intended lines changed |
| `python3 orr_analyze.py --test` | **87 samples, 0 with a word reported**, before and after the analyzer and spec edits |
| `python3 grain_validate.py --md pilot_I1.md` | no GN round in the leaf, exit 0; `--selftest` ok (117 signs) |
| Seren's leaf-hand string (pilot line 265) | identical to `orrowen_v2.md` §11.4 |

The analyzer's glosses of the fixed lines (`bt/fixed_sentences.txt`), as a reader now meets them:

```
sa re vammant so hrenneth             REL PST S·lose-3PL their S·captain-PL          -> who had lost their captains
Veth re hyrril nahos fedh hos brod    but PST understand none time one word          -> but no one ever understood a word
et pithulath driget                   the lord-PL thrown (row: thrown, flung; scattered)
sa nath re yorrar veth amm ew venn et dask
                                      REL NEG PST S·fight-1PL but when was true the end
                                                                                     -> who fought only when the cause was true
New hy vodh re yalant et uldath strom sennet. Nath re yal hos strom hyo.
                                      was.not because PST S·be.PST-3PL the man-PL great dead. NEG PST S·be.PST one great from-3SG.M
                                                                                     -> It was not because the great men were dead. There was not one greater than he.
Nath gaeverym re hoss fedh uld hosen et Crenn
                                      NEG N·think-1SG PST breath time man as the captain
                                                                                     -> I do not think a man like the Captain ever lived
Ew hosel covv hesperd o               was alone/only cloak soldier it                -> It was only a soldier's cloak
eth re yal saed et covv bysket umo    and PST S·be.PST half the cloak knot upon-3SG.M -> and the half of the cloak was bound upon it
Pellow Vell                           Pellow song   - or, as an epithet construct after a name, S·pell 'spire'
El nydherd yalatath en                is counter S·anything-PL I                     -> I am a counter of things
```

## 7 · Still owed, and out of scope

1. **A second blind reader** for the seven fixed lines. This reader had seen the English by then, so §6 is a rule-based check, not a blind one.
2. **Rebuild safety.** `lex/build_lexicon.py` regenerates the TSV, so the three row edits above would be lost on a rebuild. To keep them:
   - edit `lex/en_map/m_r.txt` line 146 to `plain | venn | adj | plain (straight, honest: 'tell it plain'; not 'ordinary')`;
   - add the *Pellow Vell* note to the pilot's `@phrase | ~Pellow Vell` recipe line.
   
   *driget* needs more than a recipe line. `systematic()` builds a verb's -At, -Ol and -Ard rows from `en_verbs(e)`, which takes the verb's base sense only, so senses that en_map adds to a reserve verb (*drig*: fling, scatter) never reach its participle. That is a builder defect, and it likely affects other reserve verbs too (*drigyl* is "throwing" only, *drigerd* "one who throws" only). It needs its own fix, which this test did not attempt. Following the pilot's own caution about other pilots writing at the same time, the en_map files were **not** edited here.
3. **Garbled derived glosses in the lexicon.** Seen in passing, not used by I.1: O1656 *naseskerd* "one who nots know or bes ignorant of", and O1658 *naseskyl* "notting know". The builder's agent and verbal-noun templates break on *na-* verbs whose sense starts "not …". This is for the lexicon builder, not this leaf.
4. **Suggestion for `orr_analyze.py --gloss`.** It could print the lexicon's phrase rows where a sequence matches one: *hy ull* "then / so", *hos eth hos* "one by one", *hosen amm* "as if", *nath … veth*. The blind reader looked every one of these up by hand.
5. **Reserve root.** *mamm* "lose" is new to this leaf and joins its list for the Welsh/Irish/Tolkien dictionary pass (`orrowen_v2` §14c item 1). Only its softened form *vammant* appears on the leaf. The bare root does look like Welsh and Irish *mam*, so the pass should look at it.

## 8 · Files

- `wf7/blind_I1.txt`: the blind input (Orrowen and notation lines only, pilot line numbers kept).
- `wf7/bt/blind_backtrans_I1.md`: the back-translation as frozen before the English was seen.
- `wf7/bt/gloss.txt`, `wf7/bt/check.txt`: the analyzer's output on the blind text, before any fix.
- `wf7/bt/gloss_after.txt`, `wf7/bt/check_after.txt`, `wf7/bt/fixed_sentences.txt`: after the fixes.
- Before-copies, for review or rollback:
  - `wf7/bt/pilot_I1.before.md`
  - `wf7/bt/i1_draft.before.txt`
  - `wf7/bt/lexicon_orrowen.before.tsv`
  - `wf7/bt/orrowen_v2.before.md`
  - `wf7/bt/orr_analyze.before.py`
- Changed:
  - `wf7/pilot_I1.md`
  - `wf7/pilot/i1_draft.txt`
  - `wf7/pilot/i1_report.txt`
  - `wf7/lexicon_orrowen.tsv` (rows O0505, O2715, O2880)
  - `wf7/orrowen_v2.md` (§3.5, §3.6, §3.8, §5.10)
  - `wf7/orr_analyze.py` (`layer_fits`, `context_check`)
