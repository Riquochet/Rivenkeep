# RIVENKEEP · THE FIRST TONGUE

*wf7 design spec, 2026-09-27. A workflow document, not a Book leaf and not a repo doc. It answers Jack's note 8 of 2026-09-27: "The Latin cross is fine. Imagine that all languages come from an ultimate base language." It is built on `wf6/shoreland_spec.md` (Orrowen and the course-hand), `wf6/mystaeri_spec.md` (Seilrhass and the grain) and the Book (`wf6/legends_v12.md`).*

**What this is.** The one tongue that Orrowen and Seilrhass both come from, reverse-engineered as Tolkien built his primitive roots under Quenya and Sindarin. It gives a sound system, {{N_ROOTS}} roots, the ordered sound laws that turn them into both living tongues, and the sign-set from which the course-hand's letters and the grain's signs both descend.

**How it was made, and how it is checked.** Every form in the tables below is computed by a sound-law engine (`wf7/ancestor/laws.py`) from the ancestral form, and compared with both published lexicons. Nothing in a table of forms is typed by hand. The check result is in §4.7.

**Status.** A proposal. No canon text changes. Items marked **[Jack]** need his decision (§7). Where the ancestor exposes a slip in the spec files, a small emendation is proposed (§4.3).

**Notation.** An asterisk marks a first-tongue form: *\*tolm-*. In ancestral forms, *th* is /θ/, *dh* is /ð/, *x* is /x/ (as in Scots *loch*), *ŋ* is the *ng* of *sing*, and ***ʔ* is the catch**, a stop in the throat, the grandfather of the Mystaeri knock. A hyphen marks a suffix seam and *+* a compound seam. "O" is Orrowen, "S" is Seilrhass.

---

## 0 · THE SHORT VERSION

1. **Its name is *Tumaʔ*, "what is held in common"**: *\*tum-* "hold, keep" + *\*-aʔ* "a whole of two or more". In English it is **the First Tongue**.
   - Its Orrowen reflex is *Tuma*. In the living tongue that is also the verb the Bonded use of themselves: "they two remember" (*Tuma Halyna*).
   - Its Seilrhass reflex is *Theinae*, built on *thein*, the Knowing's own root.
   - **[Jack]** the name.
2. **One people spoke it, and cut one hand of marks on whatever stood.** A stone set on end and a living trunk were one word to them, *\*tolm-* "a standing thing". When the people parted, the stone-folk kept that word for stone (O *tolm*: a stone, and a letter) and the wood-folk kept it for the tree (S *thael*).
3. **The stone kept the sound, and the wood kept the meaning.**
   - The chisel wore the first marks into letters read for their first sounds.
   - The growing wood took the same marks into its rings as signs read for what they mean.
   - So **the Knowing is the nearest living survivor of the first tongue**. Sound changes, and words can be turned; a meaning cut in wood cannot. The nearest survivor in *sound* is the Hal, which no one alive can sound rightly.
4. **{{N_COG}} words are one word in both tongues** (§1.5). They fall where the Book already cares most:
   - the hearth's yes, *Tumar* "we remember", is the first tongue's "we hold". The Knowing, *theinas*, is the same holding;
   - the Title's *ol* "our", said five times, is the Aelthar's *ael* "together", and the green sliver's "too";
   - the proverb ends on one word in both tongues: O *vana*, S *vann*, "both";
   - the Riven Stone and the Torn Cloak (O *tresk*) are the wound in the Seilrhass proverb (S *thaess*);
   - *myst*, the Rivenmen's grey (in *Mystaeri* and the Mystlands), is the wood's between-light (S *neis*);
   - the Title's "home" (O *varn*) is the Stone's "peace", still water (S *vaere*).
5. **The sound laws are few and regular.**
   - To Orrowen, five laws make the Hal (the catch doubles a consonant or lengthens a vowel; the old diphthongs close; the i-colouring makes the slender class; *f* and *w* become *v*; three like consonants keep two). The spec's own laws, made exact, then make the living tongue.
   - To Seilrhass, five laws make the Eldest speech (the catch breaks the vowel; the brightening fronts every back vowel; the later vowels thin; lips and throat go soft; clusters simplify). The spec's own three then make the living tongue.
   - **Every existing word of both tongues falls out**: {{COV_O}} Orrowen lexicon entries and {{COV_S}} Seilrhass entries are accounted for, with **{{N_BAD}} mismatches in {{N_DERIV}} derivations**, and a short list of named irregularities (§4.3).
6. **The first marks are {{N_MARKS}} signs** (§5).
   - **Stone.** Three of them gave the course-hand its three uprights: the Bearer, the Course and the Split, the old letters for *p*, *t* and *k*. Seven more gave the manner-stones, each from the mark whose own name began with that kind of sound. Four gave the vowels: the Curl, the Lone Mark, the Upon and the Lean.
   - **Wood.** Every one of the 70 grain signs, the six condition bands and the devices grows from them.
   - **The Fore, a stroke crossed near its head (the Latin cross), is kept whole by both**: it is the wood's Bar Before, and the first builders' mark on stone.
7. **Seren** is *\*Swe-reŋ-o-s*, **"a single sorrow that overcomes"**: Hal SEREŊOS, living *Seren*. Her name keeps one of the Hal's three dead letters, and the same first-tongue word would come out *Seren* in the wood's tongue too (§6).

---

## 1 · PREMISE AND LORE

### 1.1 What the first tongue was

- **One people, one tongue, one hand.** Before there was a grey or a wall, one people spoke Tumaʔ. They cut their marks on whatever stood: a stone set on end, or the trunk of a living tree. Their word for both was *\*tolm-*.
- **A mark was a word and a sound at once.** Each of the first marks stood for a thing, and it could also be read for the first sound of its name. A line of marks said what was meant and how it was said, both at once. Neither living hand can do that.
- **A word held.** The first tongue's name for itself, *Tumaʔ*, "what is held in common", comes from *\*tum-*, "hold, keep, in the hand and in the mind".
  - In Orrowen the root means "remember" (*tum*).
  - In Seilrhass it means "hold, know by touch" (*thein*).
  - So the hearth's yes and the wood's Knowing are one verb.

### 1.2 The parting

- **No tale tells it**, and nothing here needs one. **[Jack]** Why they parted can stay unknown for ever.
- **The Book fixes only the two ends.** The Mystaeri "were old" before the Shorelanders cut their first stone (II.2), and the first Stonewrights "came up onto the high ridges" in the age before the havens (II.1). The parting lies before both.
- **The two kinds of standing thing became the two peoples' matter.**
  - *Those who stayed with the trees* became long-lived with the wood. Their marks, cut into living wood, were carried outward by every ring the tree grew. What grows keeps its meaning and loses its sound.
  - *Those who went up to the rock* cut their marks in stone, which does not grow. The chisel wore the marks straight, and the builders read them for their sounds.
- **The tongues drifted, as tongues do.** The wood's speech lost every stop and every back vowel, and its catch became the knock. The stone's speech kept its stops, lost its endings, and turned the lost endings into mutations. By the time the grey sails came, no word of one could be heard in the other.

### 1.3 What each people kept

| | Stone: the Shorelanders | Wood: the Mystaeri |
|---|---|---|
| **the sound** | kept longest. The Hal still has its endings and three sounds that have since merged | worn down to seven consonants and a knock |
| **the meaning of the marks** | let go: each mark became a letter for one sound | kept: each mark is still read for what it means |
| **the shapes** | worn straight, stood on a bed, arms kept only to the right (§5.3) | set along a file, bowed and tapered, grown in rings (§5.3) |
| **kept whole by both** | the Fore (the cross) and the Door (the gate); the word for "both"; the proverb | the same |

**Why the Knowing is the nearest survivor.** Only the wood kept what the first marks *meant*, and "a knowing cannot be turned" (the foreword). The stone kept how the first tongue *sounded*, and sound is what time changes: the Rivenmen cannot sound their own Hal. So the one part of the first tongue anyone alive can still take in whole is the wood's.

### 1.4 Why no one knows

- The Hal is unreadable even to the Rivenmen (shoreland spec §4.4).
- The Mystaeri "never once went down to the shore with our hands open, save once" (V.4).
- The grain has no sound. The one hand that kept the first tongue's meanings cannot tell anyone how it sounded.
- **The kin words look nothing alike**: *tresk* and *thaess*, *tolm* and *thael*, *ol* and *ael*, *molt* and *nael*. Only the laws show that they are one word.

### 1.5 The kinship: the words that are one word in both tongues

★ in §3 marks the same sets. The meaning in the first tongue is the one both senses grew from.

{{T_COGNATES}}

**Two crossings worth seeing.** Death and night trade places across the two tongues. The stone says "die" with *\*senn-* "go down" (O *senn*, "go out, as a fire in peace"); the wood kept *\*senn-* for "beneath". The wood says "die" with *\*feʔ-* "fade" (S *veas*); the stone kept *\*feʔ-* for "night" (O *vess*). In the same way, the stone's word for stone is the wood's word for the tree, and the wood's word for stone is the stone's word for mortar setting fast.

### 1.6 Four sayings, back to the first tongue

Each word of each line below is derived by the engine; the build fails if any does not come out.

**(a) The Title, and the green sliver's answer.**

{{T_TITLE}}

The Title opens *Ul dumol ol varn*, "In memory of our home". At the end of the war the green sliver says *Ve ith naelenn ael raltheine*, "We remember our home too". Under both lie the same two first-tongue words, *\*tum-* "hold" and *\*ol* "together". The hearth's answer, *Tumar*, is *\*tum-ar*, "we hold". The canon says the sliver "gave them the answer of this hearth … and it did not stop where we stop". In the first tongue it is the same answer.

**(b) The proverb both peoples share.**

{{T_PROVERB}}

The saying is older than the parting. The wood's wording is the older one: its words are the first tongue's own. The stone rebuilt all of it except the last word, and that word is still one word in both tongues: *vana*, *vann*, "both".

**(c) The Stonwryt under the old capstone.**

{{T_STONWRYT}}

None of the Stonwryt's words met a law between the first tongue and the Hal. **The vow under the tale-stone is cut in the first tongue itself, word for word**: it is the oldest sentence anyone can still see. The Rivenmen cannot sound it, and the Mystaeri would not know one word of it.

**(d) The Guest's three words.**

{{T_GUEST}}

The Guest reached for "stop, sky, dying" in the shore's tongue. His third word, *Sennyl*, is at the root *\*senn-*, "going down". His own people kept that root as *senn*, "beneath", and the gift's sentence ends with it: *ei ve la **senn** vease*, "and we are dying **under** it". The last word he said at the door and the last clause of the gift he brought are one word, split by the parting.

### 1.7 CALL-OUT · For Jack: letting the kinship show, without editing a tale

> The Book should never say that the two tongues are kin. No one at the hearth knows it. It can let the player find it, in the places the Book already keeps for native hands and their translations (Legends, "How the Legends Enter the Game", §4.1–4.2).
>
> 1. **The mark on the black chest (I.4) is the Fore.** The tale says only "a chest of black stone, with the mark of the first builders cut in its lid", and that surface is still owed (Legends §4.1). Draw it as the Fore in the Hal's cut style: a stroke crossed near its head, square-footed on its bed. From *One Word* (Cam 1) the player has the Bar Before in Seren's sign-list, so the two are the same sign, and nothing in the Book says so. Its Translation fold, at *The Bedrock Hand* (Cam 16): *The first builders' mark: "first; before all".*
> 2. **The head of the lintel column** (owed; *Read Down the Lintel*, Cam 32). Above the topmost Hal name there is one line older than the Hal, cut in the first marks. It stays untranslated until item 4.
> 3. **Seren's last line in the Book of Knowings** (optional: it adds to the appendix, not to a tale). It is added with item 4: *The Bar Before is the mark on the lid of the chest I carried. I looked at it every night of the war, and did not see it.*
> 4. **A last achievement, *The First Tongue* (native *Tuma*)**, at the launch after *The Last Carver*, when nothing else is left to earn. It changes no word; it adds three Translation-fold lines:
>    - under the lintel's first line: *What is held in common.*
>    - under the proverb, wherever it is shown in both tongues: *In both tongues the last word is one word: both.*
>    - under the Stone out of the Grey: *Stone writes what is said, and wood what is meant. Here, for the first time since the first tongue, both are cut on one face.*
>
>    It keeps the Legends' laws: it is cosmetic, reached by every player, after and never before, and it only adds.
> 5. **"The Knowing is the nearest survivor" needs no new line.** The foreword already says "Words can be turned, and a knowing cannot." The Tongues doc can give the reason (§1.3).
> 6. **Echoes the tales already hold** (nothing to add; for the Tongues doc, and for players who dig):
>    - *Tumar* is "we hold";
>    - the Guest's last word and the gift's last clause are one root (§1.6 d);
>    - Rhyna's name is the wood's word for stone, and the Guest's errand-name *Aelrhen*, "bond-to-stone", is at the root "together, set fast";
>    - Halvard's *-vard* is the Aelvaren's *-varen*;
>    - Brenn, the man who at last confessed, carries by accident the first tongue's word for "mouth". Names are names, and the Book gives his none.
> 7. **Never:** in a tale, in store art, before the Finale, or as a mechanic.
>
> **Faith, reverently.** If note 8's "ultimate base language" is, for you, the one tongue before the scattering, the design leaves exactly that room and never claims it. The Book names no cause for the parting. The first tongue's word for God, *\*marð-* "the Maker, the one knelt to", survives only in stone (*Mardh*); the wood kept no name for Him, only the kneeling. The Stone's grain says "our God" as *the one they kneel to*.
>
> **[Jack]** Adopt 1–4? Recommended: 1 and 4 (the drawing, and one late achievement), with 3 if you want the Book itself to notice at the very end.

**A bridge to note 1 (the chisel's economy).** The first marks were word-signs and wrote no small words, as the grain still writes none. The first builders' reform (C6, §5.3) is the "reformed" hand in your sense: few strokes, laid by rule, one letter to a sound. If note 1 leads to a cut register that leaves out the small words and keeps a few old word-signs (for example the Fore for "first", the Door for an oath, the Tally for numbers), that is the first hand's economy surviving on stone. The ink hand, *Garl Flenn*, is then the later and quicker hand that writes the small words out. Nothing here depends on that choice.

---

## 2 · PHONOLOGY, AND THE GRAMMAR IN BRIEF

### 2.1 Consonants

| | lips | tongue-tip | back | throat |
|---|---|---|---|---|
| **stops** | p · b | t · d | k · g | **ʔ** (the catch) |
| **nasals** | m | n | ŋ | |
| **fricatives** | f | th /θ/ · dh /ð/ · s | x | h |
| **approximants** | w | l · r | y | |

- **Clusters.** At the start of a word: stop + *r* or *l* (*tr, kr, gr, br, pr, dr, kl, gl, pl*); *s* + stop (*st, sk, sp*); *xr, xw, xwr, xwl, gw, sw*. After a vowel, most sonorant + consonant pairs, *st, sk*, and doubled *ll, nn, mm, rr, ss*.
- **Frequency.** Common: *t, k, s, n, l, r, m*. Middling: *p, d, g, th, dh, w, f, x*. Rarer: *b, ŋ, h, y*. The catch stands in about one root in eight.

### 2.2 Vowels

- Five short vowels: *a, e, i, o, u*. The back vowels *o* and *u* are frequent, and the wood lost both.
- Diphthongs: *ai, ei, oi, au, eu, ui*.
- **There are no long vowels.** Length in the Hal comes from the catch (§2.3).

### 2.3 The catch, *ʔ*, and its three fates

The catch is the first tongue's own colour, and it is where the knock began.

| Where it stands | In Orrowen (O1) | In Seilrhass (S1) |
|---|---|---|
| after a vowel, before *l r m n s* | doubles the consonant: *\*waʔl-* > *vall* | breaks the vowel: *aʔ* > *ae*, *eʔ* > *ea*, *oʔ* > *ae*, *iʔ* > *i*, *uʔ* > *ei*: *\*waʔl-* > *vael* |
| after a vowel, before any other consonant, or at the end | lengthens the vowel: *\*gann-aʔ* > Hal *gannā*, *\*feʔth-* > Hal *vēth-* | breaks the vowel, as above |
| between vowels, or at the start | lost | lost |

- **Its ghost in the knock.** In the wood's speech a stop at the head of the second syllable left a catch before it, and the catch then spread to every word of two syllables or more (S6). The Mystaeri knock is the first tongue's catch, moved.
- **The catch-grade.** A root with the catch after its vowel is often the intensive or the solemn form of a plainer root: *\*sol-* "lie still" beside *\*soʔl-* "the deep rest" (O *sollan*, peace). *\*waʔr-* "the still place", *\*waʔl-* "a thing's inward bent" and *\*feʔ-* "fade" are catch-grade roots.

### 2.4 Syllables and stress

- **A syllable is (C)(C)(C)V(C)(C).**
- **Stress falls on the first syllable**, as in both daughters. A catch carries a falling pitch on its syllable, and that pitch survives in the knock's "high falling pitch" (mystaeri spec §2.3).

### 2.5 Roots and ablaut

- **Most roots are one syllable**, CVC or CVCC: *\*tolm-, \*krask-, \*senn-*. A few are two: *\*afen-, \*tafall-*.
- **Ablaut.** A root may show *e*, *a* or *o* (and sometimes *u* or *i*) in different words:
  - *\*tol-/\*tal-*: tolm, a stone; tald, rise; thal, the neck;
  - *\*krenn-/\*krann-*: crenn, a captain; rhann, heavy;
  - *\*lanθ-/\*lenθ-*: lanth, wait; lenth, winter;
  - *\*bro-/\*bra-/\*bre-*: brod, a word; ranth, a word; renn, a mouth;
  - *\*et-/\*itt-*: et, the; ith, one;
  - *\*tann-/\*tunn-*: thann, close; tunn, whole.
- **Extensions** make new stems: *\*-d-* "made, brought to" (*\*tal-d-* rise up; *\*gal-d-* build; *\*xal-d-* a wall), *\*-t-* (*\*mus-t-* the grey; *\*ros-t-* thrice three), *\*-n-* and *\*-l-* (*\*xwre-n-* frost in stone, *\*xwre-l-* frost in wood).

### 2.6 The grammar in brief (what the daughters inherited)

- **Nouns** end in a thematic vowel: *\*-o-* (broad) or *\*-i-* (slender).
  - The nominative adds *\*-s*: *\*tolm-o-s*. Orrowen built on this form, which is why the Hal ends in *-os* and *-is*.
  - The bare stem was used for calling and naming: *\*tolm-o*. Seilrhass built on this form, which is why it has no case endings.
- **Other endings:** *\*-aʔ* "a whole of two or more" (O dual *-a*, and the feminine); *\*-uʔ* "at, the place of" (O *-ow*); *\*-aθi* plural (O *-Ath*); *\*-en* "belonging to" (O *-en*; S plural *-en*); *\*-eʔ* "one of" (S *-ea*); *\*-aʔr* "all of a kind" (S *-aer*, later *-ear*); *\*-el* "one, a small one" (O *-el*).
- **Verbs** take the person endings *\*-om, -iθ, -os, -ana, -aʔ, -ar, -us, -ant*. Orrowen kept them. The 3sg *\*-os* fell with the other endings, which is why the living 3sg is the bare stem (Hal STONOS > *ston*). *Tumar*, "we remember", is *\*tum-ar*, "we hold".
- **Particles** could stand before or after the word they governed:
  - *\*re* "that, then"; *\*es(an)* "at another time, not now"; *\*na/\*ni* "not"; *\*ho* "is it?"; *\*loʔ* "is it so?";
  - *\*ul(an)* "in"; *\*um(o)* "upon"; *\*lo* "at"; *\*li* "at"; *\*xui* "from"; *\*si* "with"; *\*ri* "toward"; *\*wi* "for"; *\*ti* "through"; *\*ŋa* "toward"; *\*dem(en)* "up to".
  - Orrowen, which put its verb first, fixed its particles *before* the word. That froze their final *-n* and final vowels into the mutations.
  - Seilrhass, which put its verb last, fixed its particles *after* the word. Its verb suffixes *-e*, *-es* and *-ar* are the particles *\*e* "now", *\*es* "at another time" and *\*ar* "toward", fused to the verb after the final vowels had fallen, which is why they did not fall. So *\*es* became a future in the stone and a past in the wood: the stone looked forward with it, and the wood looked back.
- **Pronouns and pointing words** were many, and each tongue kept a different set: *\*en* "this one here, I"; *\*θo* "you"; *\*o* "he, it"; *\*ey* "she"; *\*ol* "together, we"; *\*wa* "you (many)"; *\*so* "they"; *\*ba/\*be* "my side"; *\*sa/\*se* "that one by you"; *\*la/\*le* "that living one"; *\*xa/\*xe* "that mute thing"; *\*ra* "this"; *\*re* "that".

### 2.7 How the first tongue sounds

Stops and back vowels, like the stone's tongue, with the wood's breathy clusters (*xw-, xr-*) and a catch in one root in eight. It sounds heavier than Seilrhass and less worn than Orrowen: *\*trosk-i*, *\*xreun-aʔ*, *\*waʔr-ai*, *\*swe-reŋ-o-s*.

---

## 3 · THE ROOTS ({{N_ROOTS}})

### 3.1 How to read the tables

- **{{N_CORE}} inherited roots** (§3.2) are the roots behind every existing word of both tongues, together with their small words, affixes and names.
- **{{N_RESERVE}} reserve roots** (§3.3) are first-tongue words that neither living tongue has used yet. Each gives its regular reflex in both tongues, ready for the tier-3 translation of the whole Book (note 5): stone leaves in Orrowen, wood leaves in the grain's soft readings.
- **Columns.**
  - *Orrowen*: the living form, with the Hal form after it.
  - *Seilrhass*: the living form, with the Eldest-speech form after it.
  - Where a tongue did not keep the root, the cell gives the form it *would* have, in italics after "would be". It says "falls together with" where that form is already another word, and "a lift" where the form is on the originality blacklist and must not be used.
- **★** marks a root that both tongues kept: a cognate set (§1.5).
- The reserve roots were drawn from the first tongue's own sound pattern (seeded, so the list can be re-made exactly). Each was then screened: no clash with any existing word, no form on the originality blacklist, and no form, in either tongue, that is an English word (the whole system dictionary of about 236,000 words). The Orrowen form is always unique. A Seilrhass form is shared by at most two roots, of different fields, as a tongue of seven consonants must share some.

### 3.2 The inherited roots

{{T_CORE}}

### 3.3 The reserve roots

{{T_RESERVE}}

---

## 4 · THE SOUND LAWS

### 4.1 From the first tongue to Orrowen

**Stage 1: the first tongue to the Hal** (the first builders' speech). These laws are new.

| Law | What happens | Examples |
|---|---|---|
| **O1 · The catch** | Before *l r m n s* it doubles the consonant; before any other consonant, or at the end of a word, it lengthens the vowel; between vowels or at the start it is lost | *\*waʔl-o-s* > *wallos* (> Hal *vallos*); *\*soʔl-an-o-s* > Hal *sollanos*; *\*gann-aʔ* > Hal *gannā*; *\*tal-d-uʔ* > Hal *taldū*; *\*feʔth-i-s* > *fēthis* |
| **O2 · The old diphthongs close** | *ai, ei, oi* > *ē*; *au, ou* > *ū*; *eu* > *iu*; *ui* > *y*. A long vowel before two consonants is shortened | *\*kail-o-s* > Hal *kēlos* (Kael); *\*xreun-aʔ* > *xriunā* (> Hal *Hriunā*); *\*xui-a* > *xya* (> Hal *hya*); *\*weinn-i-s* > *wēnnis* > *wennis* (> Hal *vennis*) |
| **O3 · The i-colouring** | A stressed *a* or *o* becomes *e*, and *u* becomes *y*, when the next syllable holds *i*. **This is the birth of the slender class**: every Hal noun in *-is* has *e, i* or *y*, and that is why the living tongue's harmony follows the stem | *\*trosk-i-s* > *treskis*; *\*krask-i-s* > *creskis*; *\*taw-i-s* > *tevis*; *\*kul-i-s* > *kylis*; *\*mus-t-i-s* > *mystis* |
| **O4 · Lips and throat** | *f* > *v* everywhere; *w* > *v* before a vowel (not in *wr-*); *gw* > the new *w*; *sw-* > *s-*; *x* > *h* before *r*, *w* and a front vowel (the Hal's *hr*, *hw*, and the *h* of *hya*) | *\*forr-o-s* > Hal *vorros*; *\*woll-o-s* > Hal *vollos*; *\*gwadh-o-s* > Hal *wadhos*; *\*swe-reŋ-o-s* > Hal *sereŋos*; *\*xwren-n-o-s* > Hal *hwrennos* |
| **O5 · Three like consonants keep two** | *lld* > *ld*, *rrn* > *rn*, *θθ* > *θ*; a doubled consonant before another consonant is single | *\*waʔr-n-o-s* > *warrnos* > *varrnos* > Hal *varnos*; *\*kriθθ-i-s* > *crithis* |

**Stage 2: the Hal to living Orrowen.** These are the spec's own laws (shoreland spec §4.2), made exact.

| Law | What happens | Examples |
|---|---|---|
| **H1 · The small words' -n** | a small word's final *-n* falls, leaving its nasalising | *ulan* > *ul(a)*; *enan* > *en(a)*; *van* > *va* |
| **H2 · The fall of the endings** | final *-os, -is, -as* after a consonant, and any final short vowel, are lost in words of two syllables or more. A final long *-ā* survives as *-a* where it is still a living ending (the dual, the feminine) | *tolmos* > *tolm*; *tumola* > *tumol*; *umo* > *um*; *hoa* > *ho*; *gannā* > *ganna* |
| **H3 · The long vowels shift** | *ā* > *o*, *ē* > *ae*, *ī* > *i*, *ō* > *u*, *ū* > *ow*; a final *-ā* > *-a*; an unstressed long vowel inside a word is first shortened | *kēlos* > *Kael*; *orrū* > *Orrow*; *tevāthi* > *tevath* |
| **H4 · The mergers** | *x* > *h*; *ŋm* > *mm*, other *ŋ* > *n*; *hw* > *f*; *hr* > *rh*; *wr-* > *r-* (the guild keeps *Stonwryt*); *iu* > *y* | *xaldos* > *hald*; *soŋmas* > *somm*; *hwrennos* > *frenn*; *Hriunā* > *Rhyna*; *wrytis* > *ryt* |
| **H5 · The wearing at a seam** | in a compound spelled as said, the second element's first consonant softens: *p b m t d k g* > *v w v dh r h y* | *Xalpardos* > *Halvard* |
| **H6 · Harmony** | a suffix *a* or *o* after a slender stem becomes *e* or *y* | *tessana* > *tessen*; *kethola* > *kethyl* |

### 4.2 From the first tongue to Seilrhass

**Stage 1: the parting** (the first tongue to the Eldest speech). These laws are new. Seilrhass is built on the ancestral *stem*, without the case ending (§2.6).

| Law | What happens | Examples |
|---|---|---|
| **S1 · The catch breaks the vowel** | In the first syllable: *aʔ, oʔ, ai, oi, au* > *ae*; *eʔ* > *ea*; *iʔ* > *i*; *uʔ, ei* > *ei*; *eu* > *e*; *ui* > *i*. A *w* after the first vowel and before another vowel melts into it (*aw* > *ae*, *ew* > *ea*, *iw* > *ei*). In later syllables *aʔ* > *ae*, *eʔ* > *ea*, and *ai, ei* > a long *e* that will not fall; the catch is otherwise lost | *\*waʔl-i* > *waeli* (> *vael*); *\*feʔs-i* > *feasi* (> *veas*); *\*xreun-i* > *xreni* (> *rhen*); *\*taw-i* > *taei* (> *thae*); *\*lew-i* > *leai* (> *lea*); *\*waʔr-ai* > *waere* (> *vaere*) |
| **S2 · The brightening** | In the first syllable *o* > *ae*; *i* and *u* > *ei* in an open syllable, and > *i* in a closed one; *a* and *e* stay. **This is why the wood has no *o* or *u*** | *\*ol* > *ael*; *\*ston-i* > *staeni* (> *saen*); *\*tum-i* > *teimi* (> *thein*); *\*kul-i* > *keili* (> *rheil*); *\*kriθθ-i* keeps its *i* (> *rhith*) |
| **S3 · The thinning** | In later syllables *o, u, i* > *e*; *a* > *e* in an open syllable that is not the last | *\*par-ane* > *parene* (> *varen*); *\*pann-i* > *panne* (> *vann*) |
| **S4 · Lips and throat go soft** | *p b f w* > *v*; *m ŋ* > *n*; *h y* > nothing; *d* > *t*, *g x* > *k*; *nd mb* > *nn*; *gw-* > *w-*. The Eldest speech has only two stops, *t* and *k* | *panne* > *vanne*; *maelte* > *naelte* (> *nael*); *\*gwes-o* > *gwese* > *vese* (> *ves*); *\*wind-o* > *vinne* (> *vinn*) |
| **S5 · The clusters** | At the start: *tr-* > *t-*; *kr- gr- xr- xwr-* > *k-*; *pr- br- fr- wr- mr-* > *r-*; stop or fricative + *l* > *l-*; *st- sk- sp- sw-* > *s-*. After a vowel: *sk* > *ss*; *st* > *s*; *s + th* > *sth*; *nt, n + th* > *nth*; *lt, ld* > *l*; *rt, rd, rn, rm* > *r*; *lm* > *l*; *rs, ls, ns* > *ss*; *kt, pt* > *t*; *tt* > *t*; *ll* > *l*; *rr* > *r*; a final *k* or *v* is lost | *traeske* > *taesse* (> *thaess*); *vrante* > *ranthe* (> *ranth*); *staene* > *saene* (> *saen*); *taelne* > *taele* (> *thael*); *\*esθ-o* > *esthe* (> *esth*) |

**Stage 2: the Eldest speech to living Seilrhass.** These are the spec's own laws (mystaeri spec §2.4), made exact.

| Law | What happens | Examples |
|---|---|---|
| **S6 · The old stops are lost** | *t* > *th*, *k* > *rh*. A stop at the head of the second syllable first left a catch before it, and the catch spread to every word of two syllables or more: **the knock** | *taele* > *thaele*; *kene* > *rhene*; *Aeltar* > *Ael'thar* |
| **S7 · The final vowels fall** | A final *-e* falls in a word of two syllables or more (after a consonant, or merging into a vowel before it). It does not fall when it is the long *e* of an old diphthong, and a final *-a* or *-ae* stays. A pair of consonants left at the end keeps its first | *thaele* > *thael*; *senne* > *senn*; *thae-e* > *thae*; but *vaere*, *neira*, *ilae* |
| **S8 · -aer > -ear** | By analogy with *-ea* "one of". It does not happen in *Esthaer*, or in the borrowed *Mystaeri* | *\*molt-aʔr* > *Naelaer* > *Naelear* |

### 4.3 The principled irregularities, three emendations and one re-analysis

| Word | What is irregular | Why |
|---|---|---|
| **flenn** (Hal *hwlennā*) | the final *-ā* fell | H2 keeps *-ā* only where it is still a living ending, the dual or the feminine. In *\*xwlen-naʔ* it was a stem vowel. Its broad plural *flennath* keeps the old *ā*-stem's class, as *tevath* does |
| **arra** (Hal *arrā*) | keeps *-ā*, though "a guest" is neither dual nor feminine | it *is* an old dual: *\*arr-aʔ*, "the two at a threshold, guest and host". A guest is half of a pair |
| **vaere** | keeps its final *-e* | the *-e* is the long *e* of the old *\*-ai* (S1), which S7 does not drop. The spec's "final vowels stayed after *r*" is replaced by this: *eir* (from *\*ir-i*) loses its *-e* |
| **varen** | keeps the old agent *\*-ane* | as the spec says; S3 makes it *-en* |
| **Esthaer**, **Mystaeri** | keep *-aer* | as the spec says: cut, or borrowed, before S8 |
| **sei, rei, vei** beside **si, ri, vi** | one first-tongue word gives two | the stressed twins. *\*si*, *\*ri*, *\*wi* stayed *i* as unstressed small words and became *ei* where they carried stress (S2): "if", "to go", "to give" beside "with", "against", "for" |
| **cedh, cemm** | spelled with *c* before *e* | a spelling rule, not a sound. The Book writes *c* before an *e* that the i-colouring made out of *a* (*\*ka-ð-i*, *\*kamm-i-s*), and *k* before an old *e* (*keth*, *kest*) |
| **theldeth** | not the regular Hal *\*thaldathi* | the plural was rebuilt on the singular *theld-* after the i-colouring (analogy) |
| **nel, new** | not *\*nael*, *\*naew* | the Hal's own contractions of *na + el*, *na + ew* |
| **-Os**, 2pl (Hal *-us*) | living *-os* / *-ys*, not the *-us* the tables give | the harmony law of the Orrowen spec: an unstressed suffix vowel was reduced, then took the stem's colour, as Hal *-ola* became *-ol* / *-yl*. The engine runs the colouring (H6) but not the reduction, so the tables give the Hal's *-us*; the living 2pl is the harmonic *-Os* (*tumos*, *kethys*) |
| **Seren** (was Hal *Serenos*) | **emendation**: Hal SEREŊOS | the name now carries *\*reŋ-* (§6). The Hal writes it with the dead letter ŋ |
| **re** (was Hal *rea*, shoreland §4.3) | **emendation**: Hal *re* | the Stonwryt itself cuts RE, and *re* softens because it ends in a vowel |
| **va** (was Hal *vanan*, shoreland §4.3) | **emendation**: Hal *van* | *vanan* would give *\*van* by H1–H2; *\*wa-n* gives Hal *van*, living *va* |
| **thael** | **re-analysis** (not a form change) | the mystaeri spec's "thae + old *-l*" becomes *\*tolm-i*, the standing thing (§1.1) |

The spec's harmony slips (shoreland §11b: *vennoth, delvoth, flennath, Kethow Stellath, treskat, ul glennol, Rytom*) are untouched by the ancestor. It only shows that *flennath* and *tevath* are old *ā*-stems, so the broad suffix is right for those two.

### 4.4 Every Orrowen word, derived

**Inherited words.** Each row runs from the first-tongue form, through each law that changes it, to the living word. A form marked (Hal) is the first builders' form; the spec's Hal forms are all reproduced exactly.

{{T_ODERIV}}

**Words Orrowen built for itself** (compounds, suffixes, mutations: the daughter's grammar, not sound change). Every part is an inherited word above.

{{T_OFORM}}

### 4.5 Every Seilrhass word, derived

**Inherited words.** From the first-tongue stem, through the Eldest speech (the stage with the stops *t* and *k*), to the living word, with the spoken form's knock.

{{T_SDERIV}}

**Words Seilrhass built for itself.** Every part is an inherited word above.

{{T_SFORM}}

### 4.6 What the reserve roots give

The reserve roots of §3.3 derive by the same laws; their forms in that table are computed, not chosen. Two things follow for the tier-3 translation.
- **A reserve word enters as a Hal word.** When a stone leaf needs one, its Hal form is known (for the old register and the lintel's names), and so are its mutations.
- **In Seilrhass a reserve word is a root like any other.** It takes *-en, -ea, -ear, -as, -eth* and compounds by the spec's rules, and the soft reading of any new grain sign is its living form.

### 4.7 The check

{{CHECK}}

---

## 5 · THE FIRST MARKS

### 5.1 The picture in one paragraph

The first tongue wrote with {{N_MARKS}} marks, cut on whatever stood. Each was a small picture, and each was named by a first-tongue word. Stone took the marks to the chisel: they were worn straight and set on a bed, and then read for the first sounds of their names. A reform of the first builders then laid them out as a system of uprights and laid stones, and that system is the course-hand. Wood took the same marks into the growing tree: they were set on files and bowed by the knife, read for what they mean, and grown into new signs. That is the grain. Two marks were kept whole by both peoples: **the Fore** (a stroke crossed near its head: the Latin cross, the Bar Before) and **the Door** (two posts and a lintel: the gate mark, and DOOR).

![The first marks](ancestor/first_marks.png)

*`wf7/ancestor/first_marks.svg` (drawn by `first_marks.py`). The first hand is drawn in neither people's style: one even stroke with round ends, no chisel-foot and no knife-taper.*

![The descent of the marks](ancestor/descent.png)

*`wf7/ancestor/descent.html` (drawn by `descent.py`, using the Book's own two renderers): each first mark, then what the chisel made of it, then what the wood made of it.*

### 5.2 The marks

{{T_MARKS}}

### 5.3 The laws of form

**On stone: the chisel, the first sound, and the reform.**

{{T_STONELAWS}}

**In wood: the file, the knife, and the meaning.**

{{T_WOODLAWS}}

### 5.4 Every course-hand letter, from the marks

**The reform's rule (C6).** A letter is *the upright of its place* + *the laid stones of its manner*.
- The three uprights come from the three oldest letters: the **Bearer** for the lips (*p*), the **Course** for the tongue-tip (*t*) and the **Split** for the back of the mouth (*k*).
- Each manner's stones come from **the mark whose own name began with that kind of sound**:
  - the voicing pin from the Post, *\*gann-* (g);
  - the nasal's middle stone from the Breath Within, *\*molt-* (m);
  - the fricative's low stone from the Breathing, *\*hoss-* (h);
  - the approximant's stones from the Sail, *\*gwemm-* (w);
  - the sibilant's stones from the Bough, *\*sul-* (s);
  - the rhotic's stones from the Fore, *\*re-il* (r);
  - the rough rhotic's from the Square, *\*xreun-* (hr).

So the reform is itself an act of reading by first sound: it asked what each mark *sounded*, and kept only the strokes that told it.

{{T_LETTERS}}

**The vowels (C7).**

{{T_VOWELS}}

**The marks, bites, lintels and numerals (C8).**

{{T_STONEMARKS}}

### 5.5 Every grain sign, from the marks

**The seventy signs.**

{{T_GRAIN}}

**The six condition bands** (G1: a mark laid along the whole ring).

{{T_BANDS}}

**The devices.**

{{T_DEVICES}}

### 5.6 The two marks kept whole

- **The Fore** (*\*re-il*, "the one before; first").
  - **Wood:** the Bar Before, the root of the Screen line. Its soft reading, *reil*, is the Fore's own name, worn by S1–S2.
  - **Stone:** the first builders' mark: first, before all. It is proposed for the black chest's lid, the head of the lintel column and the first stone of a work (§1.7). Its right arm and its foot also gave the letter *r* (C6).
  - It is a Latin cross, and that is fine (note 8): it is older than both peoples, and each kept it for "first".
  - **[Jack]** Should the Shorelanders keep it as a holy sign as well? The design does not require it; the Book's faith needs no emblem.
- **The Door** (*\*gann-aʔ*, "the two posts").
  - **Stone:** the gate mark that closes an oath, capped as the coping that closes a tale. It is also the word *ganna* and the pair-name custom: "a pair is a gate".
  - **Wood:** DOOR, its posts battered in.
  - "We were a people of doors" (IV.3). So, it turns out, were both.

### 5.7 Originality of the first marks

- **Primitive shapes, unavoidably.** The first marks are proto-writing, so some are the world's commonest strokes: the Stem (|), the Bar (—), the Fore (+, by design), the End (T), the Door (Π), the Cut (V), the Three (|||), the Split and the Bond (Y-like, with the Split's tine broken and the Bond's arms uneven, after the originality pass's rule for the grain).
- **They are no one's alphabet.** None of them is a Futhark rune (no stave with straight branches; the Roots' three feet are uneven). None is an Ogham letter: no strokes across or beside a stem-line, since the Tally cuts notches, not strokes, and the Pale is loose ticks, not a line. None is a Cirth letter, a Tengwa, or an Arrival logogram.
- **They are shown only in the Tongues doc and at the head of the lintel column**, never alone in store art.

---

## 6 · SEREN: "A SINGLE SORROW THAT OVERCOMES"

Jack (note 6): "Sometimes a name is just a name. Having a meaning isn't always necessary. Seren should mean 'a single sorrow that overcomes'."

**The first-tongue name.** *\*Swe-reŋ-o-s*:

| Part | Form | Meaning | Where else it lives |
|---|---|---|---|
| **single** | *\*swe-* | one's own; one alone, single | O *sost* "self, very" (*\*swo-st-o-s*) |
| **a sorrow that overcomes** | *\*reŋ-* | a sorrow that is carried and does not break the one who carries it; a grief that overcomes | nowhere else: Seren's name is the only word left of it in either tongue |
| (the ending) | *\*-o-s* | the nominative | every Hal noun |

**The derivation.**

{{T_SEREN}}

- **Stress** is on the first syllable: SE-ren. Both vowels are slender, so her name takes slender suffixes.
- **In the course-hand.** The living hand writes **s·e·r·e·n**, spelled as said, with no lintel: "one name is a mourning", and her one name *is* a single sorrow. The Hal writes **SEREŊOS**, with the long ending and the shore-nasal ŋ, one of the three letters for sounds that no one has said in twelve generations. The sorrow in her name is, in the old hand, a letter no one can sound.
- **In the wood's tongue** the same first-tongue word would also come out *Seren* (spoken *Se'ren*: the wood builds on the bare stem *\*swe-reŋ-o*, and S3 *-o* > *-e*, S4 *ŋ* > *n*, S5 *sw-* > *s-*, S7 the final *-e* falls). It is the one name in the Book that is the same in both tongues: fitting for the one who writes both halves of the Book.
- **The guild's own reading.** The Rivenmen hear *ser*, "go on, carry forward", in her name. That is a folk etymology and a true thing about her ("she can go where we cannot, alone, and carry this Book on after us", II.3), but it is not where the name comes from. *Ser* stays in the lexicon as a verb of its own (*\*ser-*).
- **Welsh *seren* "star"** remains a coincidence of sound only.
- **Spec changes** (shoreland spec):
  - §4.5, the Seren row: *Serenos* > Hal *Sereŋos*; the sense becomes "a single sorrow that overcomes".
  - §5.8, *ser*: "in *Seren*" becomes "heard in *Seren* (a folk etymology)".
  - §6.15 and the course-hand token for the Hal name: `S.E.R.E.ŋ.O.S`.

**Names are names.** The cradle-names the specs gave no sense keep none (Corlen, Voss, Hale, Marl, Tamm, Aske, Harl, Ulden, Hesk, Lanner, Aldun, Bena, Idlan, Denna). Each has a regular first-tongue shape in §4.4, so the laws account for their sounds, but no meaning is given. Brenn's first-tongue shape happens to be the word for "mouth"; the Book gives him no meaning, and nothing needs to.

---

## 7 · FOR JACK (decisions only he can make)

1. **The name.** *Tumaʔ*, "what is held in common" (English: the First Tongue; O *Tuma*, S *Theinae*)? Recommended.
2. **The kinship in the Book** (§1.7): adopt the chest's mark as the Fore (1), the late achievement *The First Tongue* (4), and optionally Seren's last line in the Book of Knowings (3)? Recommended: 1 and 4.
3. **The parting.** Leave its cause untold for ever (recommended), or give it a tale?
4. **The Fore on the Shoreland side.** The first builders' mark only (recommended), or also a holy sign of the faith?
5. **Seren** = *\*Swe-reŋ-o-s* (§6), with its Hal emended to SEREŊOS? Recommended.
6. **The three small emendations and one re-analysis** (§4.3): Hal *re* for *rea*; Hal *van* for *vanan*; Seren's Hal SEREŊOS; and *thael* re-analysed as *\*tolm-i*. Recommended; none changes a living word.
7. **The reserve roots** (§3.3) as the tier-3 translation's source: adopt the list as it is, or have particular words re-drawn? Any reserve word can be swapped for another draw without touching the laws.
8. **The Knowing as the survivor** stated in the Tongues doc (§1.3), not in the Book. Recommended.

---

## 8 · FILES (scratchpad only; nothing here goes into `Docs/`)

All in `wf7/ancestor/`:
- `laws.py`: the sound-law engine (O1–O5, H1–H6; S1–S8), with stage-by-stage traces.
- `roots_core.py`: the {{N_CORE}} inherited roots, each with its Orrowen and Seilrhass words.
- `formations.py`: the names, and the words each tongue built for itself.
- `gen_reserve.py`, `gen_reserve2.py`, `reserve.json`: the {{N_RESERVE}} reserve roots, with the screens that drew them (seeded and deterministic).
- `extract.py`, `o_lex_raw.json`, `s_lex_raw.json`: both published lexicons, as data.
- `check.py`: derives everything and compares it with both lexicons (`python3 check.py`).
- `predict.py`: the would-be reflexes, with their clashes.
- `first_marks.py`, `first_marks.svg/.png/.json`: the {{N_MARKS}} marks, the laws of form, and the letter and sign derivations.
- `descent.py`, `descent.html/.png`: the descent figure, drawn with wf6's renderers (read-only).
- `build_md.py`, `ancestor_template.md`: this file, rebuilt from the engine (`python3 build_md.py`).
