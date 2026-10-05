# Originality check: the course-hand, the grain, Orrowen and Seilrhass

> **Imported to `Docs/Research/` on 2026-09-27** as a source behind `Rivenkeep_Tongues.html`, which is canonical where the two differ. Scripts, renderers and file paths mentioned below belong to the design workspace and are deliberately not in the repo, which is documents only.


*wf6 workflow report, 2026-09-27. Scratchpad only. It covers the two scripts (the Shoreland course-hand, `shoreland_spec.md` §6, and the Mystaeri grain, `mystaeri_spec.md` §3) and the two languages (Orrowen and Seilrhass), checked against the famous fictional scripts and conlangs. The fixes are already applied to both specs and both renderers, and every drawing has been re-rendered.*

## The short version

- **Twelve shapes read as copies, and all twelve are recut.**
  - **Nine grain signs and the grain's root-foot** were runes, Tolkien certhas (letters of his Cirth) or Greek Π.
  - **The course-hand's vowels *u* and *y*** were Greek Π and Λ, which are also two Cirth vowels.
  - The worst was **TREE**, which was the rune *algiz* ᛉ exactly. *Algiz* also has a modern extremist use, and the old root-foot put it, or its inversion, on every ROOT, US and STONEFOLK sign.
- **Four words were real Tolkien words**: one with the same meaning (*tol*), one a body part for a body part (*naes*), and two famous forms (*mell*, *eneth*). All four are replaced.
  - Orrowen *tol* "come" is Sindarin *tol-* "to come". It is now *darr*.
  - Orrowen *mell* "old" (the title *Mell*, "Elder") is Sindarin *mell* "dear", the root of *mellon*. It is now *hemm*.
  - Seilrhass *eneth* "hunt" is Sindarin *eneth* "name". It is now *thaval*.
  - Seilrhass *naes* "brow" is Sindarin *naes* "tooth". It is now *lein*.
- **D'ni (Cyan's *Myst* and *Riven*) was checked hardest, and neither script copies it.**
  - The letters are nothing alike: D'ni is brush-written with hooked Z- and 2-shaped strokes; the course-hand is straight chisel-work and the grain is carved.
  - The numerals are nothing alike: D'ni counts in base 25 inside boxes; the course-hand caps letters and counts in twenties and twelves; the grain has no numerals beyond four count-bites.
  - The vocabulary does not collide. The one form match is Orrowen *gor* "every" against D'ni *gor* "time".
  - Two things sit close: the apostrophe after the first syllable of Seilrhass words (*Nael'enn*, as in D'ni *Ae'gura*), and counting in fives. Both are listed for Jack in §B.
- **Arrival stays an influence, as Jack wants, not a copy.** The grain shares Heptapod B's idea (a writing of meaning, taken in whole, drawn in circles). It shares none of its look: ink, smoke, one ring, tendrils, stroke weight.
- **Left for Jack** (§B): four Latin look-alikes (the Bar Before, drawn as the canon describes it, is a Latin cross; STOP is a T; HOME and HOMESTONE are a 9 and a square 9), the Hal *k* (a mirrored 7), the gate mark (a Π with a lifted lintel), the knock's apostrophe, and a short list of form-only word matches.

---

## How the check was done

- **Our drawings.** Every `wf6/svg/shore_*.svg` and `grain_*.svg` was shot in headless Chrome on a pale page, whole and in zoomed crops, and read by eye. The sign chart was also shot sign by sign on chips (`wf6/orig/specimen.py`, `snap.py`).
- **The other scripts**, viewed as charts. Omniglot's charts were opened in the built-in browser for:
  - D'ni (letters, numerals and a text sample);
  - Aurebesh, Dovahzul, Kryptonian and Klingon pIqaD;
  - the Sheikah script, the Hylian alphabet, Cirth (Angerthas Daeron) and Tengwar (the Quenya mode).

  The Elder and Younger Futhark and the Anglo-Saxon futhorc were set in the system's Unicode Runic font beside our signs (`wf6/orig/compare.py`). Ogham was checked from its rules; its strokes are simple enough not to need a picture. Arrival's logograms were compared from knowledge of the film's designs, as the spec's §3.13 already does; no Arrival image was opened in this pass.
- **Words.**
  - **Tolkien.** About twenty suspect words were looked up on Parf Edhellen (elfdict.com): the four new coinages, roots chosen by their shape and meaning (body, nature and motion words first), and some of the spec's own near-call list. Every other root was screened from memory of the Sindarin and Quenya lexicons, which is not a full dictionary pass.
  - **D'ni.** The full published dictionary (Kh'reestrefah's *Dictionary of the Language of D'ni*) was matched by script against both lexicons: exact and one-letter matches, after normalising D'ni *ah, eh, ee, oo* to *a, e, i, u*.
  - **Dothraki, High Valyrian, Na'vi and Klingon** were checked from their best-known published vocabularies, with spot web searches for the new words.
- **Limits.**
  - No full dictionary pass was done for Dothraki, Valyrian, Na'vi or Klingon. The Welsh and Irish pass the Shoreland spec owes (§9c) was not done here either.
  - Ancient Hylian and the Twilight Princess variant were not opened. The Hylian script that was opened is cursive and hooked, like neither of ours.

---

## A · What read as a copy, and what was done

### A1 · The grain (Mystaeri)

![before, the look-alike, after](orig/shots/compare_grain.png)

`wf6/orig/shots/compare_grain.png` shows each sign as it was, the letter it read as, and the recut.

| Sign | Read as | The recut | Why it keeps its meaning |
|---|---|---|---|
| **TREE** | Elder Futhark *algiz* ᛉ exactly (and Younger Futhark *madr* ᛘ, Cirth *ng*). *Algiz* is also a modern extremist symbol | The two boughs spring at **different heights, one to each side**, and bow upward. Now chiral (the lower bough is clockwise), so it drops the entry-nick | still "a trunk with two boughs near the head", and more like a real tree |
| **PILLAR** | *algiz* with a solid stem | as TREE, trunk still cut solid | as TREE |
| **SAPLING** | a small *algiz* | as TREE, small, in the outer half | as TREE |
| **GROW** | two *algiz* stacked (the runic *tvimadur* ᛯ) | four leaf-strokes **alternating** up the stem | still a sprig |
| **The root-foot** (ROOT, US, STONEFOLK) | an even three-tine fork at −58°, 0°, +58°: *algiz* at ROOT's head, and its inversion (Younger Futhark *yr*, futhorc *calc* ᛣ) at the foot of every person-figure | **three unequal, flaring roots** (−64°, −10°, +38°; 0.40, 0.30, 0.36 B; each bowing outward). The memory ray's pith-end follows it (−38°, −4°, +26°) | still "one who stands rooted"; a real root-flare is never even |
| **KNEEL** | *laguz* ᛚ (a stave with one branch down from its top) | the fold comes down and **runs on along the ring**: the shin laid on the ground. One unbroken cut | still "folds back sharply on itself at its head". It stays clear of AXE, as the decode test (§10.11) needs: nothing is cut above the fold, and AXE's haft runs the whole space |
| **SAIL** | *thurisaz* ᚦ (a stave with a triangle on its side), near *wynn* ᚹ | a mast under **one cloth bellied lopsided by the wind**, a square sail seen from astern. The lopsided belly makes it chiral | still "a sail; a cloth in the wind". Three other forms were tried and dropped: a streamer read as Λ; a leaf-sail and a bellied pennant read as P and *wynn* ƿ |
| **BOND** | the straight inverted Y of Cirth *h* (also λ, and the CJK 人) | both stems **bow in and meet the trunk tangentially**, as fused stems do, and the feet are unequal | still "the branches of two trees fused" |
| **AELTHAR** | the same inverted Y, with two drops | the same bowed merge, kept symmetrical: two equal bloods | still the canon's "two bloods made one" |
| **DOOR** | Greek Π and Cirth *a* | the posts are **battered**: they lean in toward the lintel, as an old stone doorway's jambs do | still "two straight posts and a bar across their heads"; still straight, so still of stone |

**One rule for any sign added later** (now in `mystaeri_spec.md` §3.13): the runes and the Cirth are made of straight staves and branches that meet at a point. A grain sign that is a stave with straight branches, or two straight strokes meeting, must bow, stagger or break them. The grain is grown wood, so it can use curves the runes cannot.

**The soft letters (Appendix A, not yet drawn)** had vowels drawn as "a three-toed foot, a bird's track". That is the inverted *algiz* again. The vowels are now **hanging rime-drops** under the letter before: a drop, a drawn-out drop, a bead, and pairs of these for the long vowels. The appendix also gains a guard against D'ni: the frost-hand is monoline and upright, never thick-and-thin, and never built on a Z or a 2.

### A2 · The course-hand (Shoreland)

![u and y, before and after](orig/shots/compare_shore.png)

| Letter | Read as | The recut |
|---|---|---|
| ***u*** | a detached Π: Greek *pi*, and **Cirth *a***, a vowel there too | two short pins with a **short capstone raised between them, the keystone**. It stays broad (a capstone), and it no longer reads as a gate or a tally |
| ***y*** | a Λ with its apex open: Greek *lambda*, **Cirth *o*** (a vowel), Aurebesh *nern* | **the leaning pin**: *e*'s tall pin, riven from its bed and leaning over its low stone, as the riven ridge leans over the Keep. It stays slender (pin and low stone) |

**What follows in the rules.**
- *y*'s foot (for a bite) is now 0.25, the leaning pin's foot.
- A mirrored Hal *y* is now a shape the living hand does not have, so §6.12 lists *u* as the only symmetric vowel.
- `render_shore.py --selftest` checks both, and passes:
  - all 26 living letters are still distinct;
  - the minimum joint holds at 0.50 u;
  - the mirror swaps are as stated;
  - the §7 token blocks are unchanged, because the letters, not the texts, changed;
  - all 286 lexicon words round-trip.

### A3 · Words

| Tongue | Was | Is a real word in | Now | Where it is used |
|---|---|---|---|---|
| Orrowen | *tol* "come" | Sindarin *tol-* "to come" (and Quenya *tul-*, as in *utúlien*) | ***darr*** (B) | lexicon only |
| Orrowen | *mell* "old"; *Mell · Mella* "Elder · Elderess" | Sindarin *mell* "dear, beloved", the root of *mellon* (the Moria password) | ***hemm***; ***Hemm · Hemma*** (Hal *hemmos · hemmā*) | lexicon; the Eldhythe original becomes ***Tavow Hemm*** |
| Seilrhass | *eneth* "to hunt" | Sindarin *eneth* "name" (as in *Man eneth lín?*) | ***thaval*** (*thavalea* a hunter, *thavalen* the hunters, the Reavers) | lexicon; HUNTER's soft reading |
| Seilrhass | *naes* "brow" | Sindarin *naes* "tooth", another body part | ***lein*** | lexicon only |

**Checks on the new words.**
- *darr* and *hemm* pass the Shoreland round trip.
- *thaval* and *lein* pass `lang/check_lex.py`: they obey the phonotactics, are not duplicates, are not English and are not on the blacklist.
- *thaval* is at least two edits from every Seilrhass root. *lein* is one edit from *lenn* and *leis*, as 158 other root pairs in the lexicon already are.
- Parf Edhellen has no *thaval*, *darr* or *hemm*. *lein* matches only the Sindarin possessive suffix *-lein* "your", which is a form match.
- None of the four is in the D'ni dictionary, and spot searches found none of them in Dothraki, Valyrian, Na'vi or Klingon.
- *thaval* is close to Tamil *tāval* "distress", and *darr* to Hindi *ḍar* "fear". These are natural-language form matches, which the Name Map's standard allows.

---

## B · Near-calls left for Jack (not changed)

| Item | What it resembles | Why it was left | Proposal |
|---|---|---|---|
| **BARB, the Bar Before** (a Hasty root) | a **Latin cross**, and Cirth *l*. In a Book whose other people pray to *Mardh*, a cross on a Mystaeri root can read as a crucifix | "a bar laid across a stroke" is the canon's own description (Seren's words) | if it reads wrongly in play, bow the bar strongly along the ring so it reads as a screen or a bow, not a cross |
| **STOP** | a Latin **T**, and it is the gift's root and last mark, so it is large twice (`grain_GIFT.svg`) | generic. Every alternative considered turns it into an arrow (the rune *tiwaz*), a Γ, or a dome, which is now SAIL's | keep |
| **HOME, HOMESTONE** | a **9** and a square 9; turned in a round, Tengwar *silme* / *silme nuquerna* | a tail crossing the stem was tried, and it read as a Latin *a*, so it was withdrawn. VI.1's sliver is built on HOME | keep (the renderer notes' §10.10 call stands) |
| LONE, STERN, GIFT, LIVE | *i*, *n*, *ø*, *P* | canon-described or generic; among the rings they read as cuts | keep; never show one alone at large size |
| **Hal *k*** (and *g*) | mirrored, a leaning **7**, which is also Aurebesh *resh* and near Cirth *th*/*kh* | the mirror is the Hal's defining rule, and only a few Hal surfaces exist | keep, or give the Hal's shore upright a short bedded toe so the 7 is broken |
| **the gate mark** (end of an oath) | a Π with its lintel lifted | punctuation, not a letter; it is the II.3 gate image | keep |
| **The knock's apostrophe** | every Seilrhass word of two or more syllables prints as *X'yz* (*Nael'enn*, *Seil'rhass*, *Eir'sethea*). D'ni names do the same (*Ae'gura*, *Er'cana*, *Ti'ana*, *K'veer*), and so does Na'vi (*Na'vi*, *pa'li*) | the canon forms (*Ael'thar*, *Ra'lensaen*) are fixed | print the knock only where a Mystaeri is heard speaking, and write every other word soft, as the grain does (*Naelenn*, *Seilrhass*) |
| **Counting in fives** (*vinn*, "hand") | a Myst player may think of D'ni's base 25 | counting in fives is common in real languages, and the grain has no numerals | keep; never give the grain a boxed or rotated numeral set, or a 25 |
| ***semasiographic*** (Mystaeri §3.1) | Louise Banks's word for Heptapod B in Chiang's story | it is a real linguist's term | keep it in the design files, and out of the Book (now said in §3.13) |

**Word matches in form only, kept** (a different meaning; the Name Map's standard allows them; all are now listed in the specs):

| Tongue | Word, meaning | Resembles |
|---|---|---|
| Orrowen | *trenn*, course; tale | Sindarin *trenarn* "account, tale" (*tre-* + *narn*). This one is the same field. It was kept because *trenn* is the script's own name (*Garl Dhrenn*) and its core sense is a course of stones. **Jack should see it** |
| Orrowen | *tum*, remember | Sindarin *tum* "valley" |
| Orrowen | *gorn*, corner | Sindarin *gorn* "valour", as in *Aragorn* |
| Orrowen | *luth*, ink | Sindarin *lûth* "spell", as in *Lúthien* |
| Orrowen | *sell*, long | Sindarin *sell* "daughter" |
| Orrowen | *el*, is | Sindarin *el* "star" |
| Orrowen | *vess*, night | Sindarin *vess* (the mutated *bess*) "wife" |
| Orrowen | *gor*, every | D'ni *gor* "time", and Sindarin *gor* "horror" |
| Seilrhass | *rhass*, storm, crack (in *Seilrhass*) | Sindarin *rhass* "precipice" |
| Seilrhass | *neth*, turn aside | Sindarin *neth* "young; girl" |
| Seilrhass | *lanth*, knot, wait | part of Sindarin *Lanthir* (already §8.4) |
| Seilrhass | *na*, to, toward | Sindarin *na* "to, at". A two-letter particle, as in Slavic *na*. Unavoidable |

---

## C · Checked and clear, script by script

| Script or language | The risk | Finding |
|---|---|---|
| **Arrival** (Heptapod B) | circles; meaning, not sound; taken whole | The grain keeps Arrival's *ideas*, as Jack asked. It has none of its *look*: many growth rings, not one ink ring; crisp facets, not smoke; nothing off the rim; weight carries nothing; it reads in a direction, from pith to bark. The one shared term, *semasiographic*, is kept out of the Book |
| **Ogham** | strokes on a stem line; tallies | Course-hand letters stand on one side of the bed. Recut *u*'s two pins carry a keystone between them, so they read as three stones, not a tally. GROW's alternating leaves are no Ogham letter, since Ogham groups its strokes on one side or across the line |
| **Elder and Younger Futhark, futhorc** | staves with branches | Six grain signs and the root-foot were runes, and BOND and AELTHAR were near the futhorc's *calc*; all are recut (A1). The course-hand is full of horizontals, which runes avoid. Clear |
| **Cirth** | straight stems and branches; Π and Λ vowels | Cirth *h*, *l*, *a*, *o* and *ng* were matched (BOND, BARB, DOOR, the course-hand's *u* and *y*, TREE). All are recut except BARB (§B) |
| **Tengwar** | stem and bow; a series-by-grade table | The course-hand has no bows. Its place-by-manner table is its own: the upright's shape and the laid stones. The grain's HOME, turned, is near *silme* (§B). The soft letters are now barred from stem-and-bow shapes |
| **D'ni** | letters, numerals, apostrophes, words | Letters: brush-written, hooked, Z- and 2-shaped, sharing nothing with either hand. Numerals: base 25 in boxes; ours are capped letters, or none. Words: no collision except *gor*, a form match. The apostrophe and counting in fives are in §B. Canon-level echoes are in §D |
| **Aurebesh** | bold geometric fragments | No letter matches. Aurebesh *resh* (a 7) is the Hal *k*'s near-call (§B) |
| **Dovahzul** | claw strokes with wedge heads | Only single features are shared (STRIKE's and RAM's wedges); no letter matches |
| **Kryptonian** | lozenges, circles, dots and bars | EYE (a lens with two tails) is the nearest feature; no letter matches |
| **Klingon pIqaD** | blade-shaped curved glyphs; Γ | Only generic Γ-corners are shared (course-hand *p*, *t*, *k*) |
| **Hylian** (the alphabet), **Sheikah** | hooked cursive; bold rounded squares | Nothing shared. The grain's squares are thin outlines, never filled rounded blocks |
| **Quenya and Sindarin** | vocabulary | Four real words replaced (A3); the form-only matches are in §B |
| **Dothraki, High Valyrian** | vocabulary; the *ae* and *rh* look of Targaryen names | No word collides. Seilrhass's density of *ae* and *rh* (*Rhenear*, *Naelthar*) has a Valyrian ring, but the canon names are Jack's, and the tongue has no *o*, *u* or stops, where Valyrian is full of them |
| **Na'vi** | vocabulary; apostrophes | No word collides. The apostrophe is in §B |
| **Klingon** | vocabulary | No collision: Seilrhass has no stops, and Orrowen shares only chance forms such as *hos* and *HoS* |

---

## D · Outside the scripts, noticed in passing (canon, for Jack's awareness only)

- **Myst's Ages.** *Myststone* and *Mystwood* sit near Myst's *Stoneship* and *Channelwood* Ages (a forest of tree-houses on water). The Book's *Riven* and *Myst-* already make the echo. Nothing in either script adds to it.
- **Avatar.** The canon's "the memory that runs back through the roots" (Ralenthae) and the Stone's "what the boughs saw went home through the roots, and the groves held it" are close to Avatar's premise, the forest's root network holding the ancestors' memories. The grain carves memory as a ray cut into wood, never as a living link, and should stay that way.
- ***It is known.*** The canon line "what is carved in living wood is not heard. It is known" ends on the phrase that Game of Thrones fans know as a Dothraki catchphrase. It is ordinary English and canon. It is noted only because readers may smile at it.

---

## E · What changed, file by file, and how it was confirmed

**Grain.**
- `wf6/grain/signs.json`:
  - TREE, PILLAR, SAPLING, GROW, KNEEL, SAIL, BOND, AELTHAR and DOOR are recut;
  - HUNTER's soft reading is now *thavalea*.
  - The patch is `wf6/orig/apply_grain.py`. It is idempotent, and it records the reason for each change.
- `wf6/render_grain.py`:
  - `ROOTFOOT` and `MEMORY_TINES` are new constants, the uneven roots;
  - the root-foot element now draws bowed, unequal roots;
  - cuts take a new `curve` option (a Catmull-Rom curve through the points), which SAIL uses.
- `wf6/mystaeri_spec.md`:
  - §0: a pointer to this pass.
  - §2.9: *lein*, *thaval*, *thavalen*.
  - §3.4: the `curve` option, the root-foot, and the chiral list.
  - §3.5: nine rows and the matching JSON lines, checked equal to `signs.json`.
  - §3.7 and §3.12: the memory ray's pith-end, and new overlay pairs (TREE with GROW, SAIL with STOP).
  - §3.13: the pass, the rule for later signs, D'ni and the rest, and the Latin look-alikes.
  - Appendix A: the vowels and the monoline rule.
  - §8.10: Jack's calls.
  - §9: the prototype drawings marked as superseded.
  - §10.1, §10.6, §10.7, §10.9 (sizes) and §10.10.
  - Applied by `wf6/orig/apply_mystaeri_spec.py`, plus two hand edits.
- `wf6/lang/lexicon.tsv`: the three rows.
- `wf6/svg/index_grain.md`: the size line.

**Course-hand.**
- `wf6/shoreland_spec.md`:
  - §6.6 JSON: *u*, *y*, and *y*'s foot;
  - §4.5: *Tavow Hemm*;
  - §5.2, §5.8, §5.9: *Hemm*, *darr*, *hemm*;
  - §6.4 and §6.5: the new vowels and *y*'s foot;
  - §6.12: the mirror note;
  - §6.14: Cirth, Latin, and new rows for Aurebesh, Klingon, Hylian and D'ni;
  - §9c: the dictionary pass, the near-call table, and the overlay done;
  - §10.7: Jack's calls;
  - §11a.
  - Applied by `wf6/orig/apply_shoreland_spec.py`, plus the §6.6 patch and one hand edit.
- `wf6/render_shore.py`: the embedded §6.6 table (the selftest checks it equals the spec's), and the selftest's mirror-swap expectation.
- `wf6/course/final_glyphs.py`: the reference table.

**Re-rendered.**
- `render_grain.py --all`:
  - no warnings;
  - every round ≤ 60 KB (the largest is GIFT, 58.8 KB);
  - two runs are byte-identical.
- `render_shore.py --all` and `--selftest`: all checks pass, and two runs are byte-identical.
- The decode test's tie check (`wf6/decode/tie_check.py`) still passes. Every tie end reads to its own mark and file, as before.

**Confirmation images** (all in `wf6/orig/shots/`):
- `compare_grain.png`: before, the look-alike, and after, for every grain recut (the root-foot shown on ROOT and US);
- `compare_shore.png`: *u*, *y*, *Tumar*, *Halyna* and Seren's line, before and after;
- `spec_final.png`: the recut signs on chips, beside HOME and BARB;
- `new_signs_1.png` to `new_signs_3.png`: the re-rendered chart;
- `new_vowels.png`, `new_seren.png`, `new_hal.png`: the course-hand;
- `r_stone.png`, `r_stone_trees.png`, `r_gift.png`, `r_e4.png`, `r_aelthar_c.png`: rounds that carry the recut signs.

**Not touched.**
- The prototype renderer `wf6/grain/grain.py` and its old drawings (`wf6/svg/E1-01.svg` … `signs.svg`, `spec1.svg`, `spec2.svg`, `hasty.svg`) still show the old forms. `mystaeri_spec.md` §9 now marks them superseded; use only `grain_*.svg`.
- No file in `Docs/` was touched.

---

## Sources

- [Omniglot: D'ni alphabet and numerals](https://www.omniglot.com/conscripts/dni.htm)
- [Guild of Archivists: D'ni numerals](https://archive.guildofarchivists.org/wiki/D'ni_numerals)
- [Kh'reestrefah, *A Dictionary of the Language of D'ni*](http://www.eldalamberon.com/dni_dict.htm)
- [Omniglot: Aurebesh](https://www.omniglot.com/conscripts/aurekbesh.htm)
- [Omniglot: Dovahzul](https://www.omniglot.com/conscripts/dovahzul.htm)
- [Omniglot: Kryptonian](https://www.omniglot.com/conscripts/kryptonian.php)
- [Omniglot: Klingon](https://www.omniglot.com/conscripts/klingon.htm)
- [Omniglot: Sheikah](https://www.omniglot.com/conscripts/sheikah.htm)
- [Omniglot: Hylian alphabet](https://www.omniglot.com/conscripts/hylian3.htm)
- [Omniglot: Cirth](https://www.omniglot.com/conscripts/cirth.htm)
- [Omniglot: Quenya and the Tengwar](https://www.omniglot.com/conscripts/tengwar.htm)
- Parf Edhellen, via elfdict.com:
  - [*eneth*](https://www.elfdict.com/w/eneth)
  - [*naes*](https://www.elfdict.com/w/naes)
  - [*tol*](https://www.elfdict.com/w/tol)
  - [*mell*](https://www.elfdict.com/w/mell)
  - [*tum*](https://www.elfdict.com/w/tum)
  - [*rhass*](https://www.elfdict.com/w/rhass)
  - [*neth*](https://www.elfdict.com/w/neth)
  - [*trenarn*](https://www.elfdict.com/w/trenarn)
  - [*gorn*](https://www.elfdict.com/w/gorn)
  - [*sell*](https://www.elfdict.com/w/sell)
  - [*lein*](https://www.elfdict.com/w/lein)
- [Wikipedia: Heptapod languages](https://en.wikipedia.org/wiki/Heptapod_languages)
- [Wikipedia: Story of Your Life](https://en.wikipedia.org/wiki/Story_of_Your_Life) (*semasiographic*)
