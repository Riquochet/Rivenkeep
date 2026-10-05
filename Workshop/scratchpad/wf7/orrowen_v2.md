# RIVENKEEP · ORROWEN v2: THE SHORELAND TONGUE, ITS STONE AND ITS INK

*wf7 design spec, 2026-09-27. A workflow document, not a Book leaf and not a repo doc. **It supersedes `wf6/shoreland_spec.md`** and keeps everything in it that still works; where a section is carried over unchanged, it says so. It is built on `wf7/ancestor.md` (the First Tongue, its sound laws and its 45 first marks), `wf6/craft.md`, `wf6/inventory.md` and the Book (`wf6/legends_v12.md`). Its tools live in `wf7/orrowen/` and never go into `Docs/`.*

**What this is.** A working language and three working ways of writing it, for the Shorelanders (the Rivenmen): the **dry cut**, which is what the chisel puts in stone; the **leaf-hand**, which is what Seren writes the Book in; and the **Hal**, the first builders' hand. Every sample in §11 was built from the rules and tables here and can be taken apart again by them. The word-sign table (§7) and the leaf-hand table (§8) are precise enough for a program to draw any line, and the leaf-hand table has been built into a working font as a proof (§8.8).

**Jack's notes of 2026-09-27 that this file answers.**

| Note | What Jack said | Where it is answered |
|---|---|---|
| 1 | "Because Orrowen is a chisel language, we need an economy of words … like the reformed Egyptian of the Book of Mormon in its economy. The later written language would have to be able to be written quickly like English if the smaller words were included." | The **dry cut** (§3.11, §7): word-signs for the common words, letters for names, rare words and endings, the small words left out. The **leaf-hand** (§8): the full tongue, small words and all, in a joined running hand. The **Hal** placed as the most economical hand of all (§4.2) |
| 2 | "I like that yes means we remember." | *Tumar* stays the hearth's yes (§3.4, §11.3). In the dry cut it is the Cup and its ending: three signs |
| 4 | "It's not that nothing is traceable to others' works. Just nothing obvious. Nothing we could get sued for." | The originality standard is rewritten to this (§13). Form-only echoes such as *trenn*, *rhass*, *gorn* and *luth* stay |
| 6 | "Sometimes a name is just a name … Seren should mean 'a single sorrow that overcomes'." | *Seren* < \**Swe-reŋ-o-s*, Hal SEREŊOS (§4.6, §5.3). The names the specs gave no meaning keep none (§4.6) |
| 3, 5, 7, 8 | the three tabs; tier 3; the grain's rings; the Latin cross and the one base tongue | §12 (the tabs and tier 3); §7.4 (the Fore, a Latin cross, kept as the word-sign *hosast*); §14 (the kinship with the ancestor). The grain is designed elsewhere |

**What changed from the wf6 spec**, in one table.

| # | Change | Section |
|---|---|---|
| A | The chisel register is now **economical**: 328 word-signs (27 heads, 20 crowns), each a first mark worn straight by the chisel; letters for names, rare words and endings; the small words (the *mortar words*) left out; a telegraphic stone grammar | §3.11, §7 |
| B | The ink hand, *Garl Flenn*, is now a **joined running hand**, every letter one movement of the pen, joined by hairlines on the line; a font-precise table, and a built proof font | §8 |
| C | **The Hal is the most economical hand of all**: word-signs with no endings, no small words, no word-gaps, no bites. A vow alone is cut whole, which is why the tale-stone's Stonwryt reads word for word | §4.2, §6.9, §11.6 |
| D | **Seren** is "a single sorrow that overcomes": \**Swe-reŋ-o-s*, Hal SEREŊOS | §4.6, §5.3 |
| E | ***Tumar*** = "we remember" = yes, unchanged; now also shown cut dry | §3.4, §11.3 |
| F | **The originality standard** is Jack's note 4: nothing obvious, nothing actionable; form-only echoes stay. A look-alike screen against 1463 characters of real scripts was run on every new sign | §13 |
| + | The grammar serves both registers (§3.11); every sample text is shown in both (§11); the lexicon gains a dry-cut column (§5); the ancestor's three Hal emendations are adopted (§4.4) | |

**Confidence and status.** A proposal for Jack; no canon text changes. Items marked **[Jack]** need his call (§15). The 194 word-signs that write reserve words from `ancestor.md` §3.3 inherit that file's caveat: the reserve forms passed the English-dictionary and blacklist screen, but the Welsh, Irish and Tolkien dictionary pass is still owed before any of them ships.

---

## 0 · THE SHORT VERSION

1. **The tongue is *Orrowen*, "[the speech] of the Shore".** Its old register, the first builders' speech, is ***the Hal*** ("the bedrock"). Both descend from the First Tongue, *Tumaʔ* (`ancestor.md`).
2. **The script is *Garl Dhrenn*, "the hand of the course": the course-hand.** It is written three ways, from the most economical to the fullest:

   | Hand | Orrowen | What it writes | Where |
   |---|---|---|---|
   | **the Hal** | *Garl Hal* | word-signs and old letters; no endings, no small words, no word-gaps, no bites; right to left, mirrored | the first builders' stones: the slates of the Rite, the old lintels, the black chest's mark |
   | **the dry cut** | *ryt broc*, "dry cutting" | word-signs for the common words; letters for names, rare words and endings; **the small words left out**, as a dry-stone wall leaves out its mortar | everything cut in stone now: capstones, lintels, works, the Stonwryt coin, the Book when it is cut in the granite of the hall |
   | **the leaf-hand** | *Garl Flenn* | the whole tongue, every small word and every mutation, in letters joined by the pen | ink: the Book, the rolls, every leaf |
   | *(the coal)* | *garl brenth* | the whole tongue in plain unjoined letters | the Captain's Title only, "as a man writes who has not written much" |

   **A vow is always cut whole**, in letters, with every word: "a sign holds what is meant; a vow must hold what was said." That is why the tale-stone's Stonwryt can be read word for word.
3. **The sound of it.** Stops and clusters, rolled *r*, back vowels, a front-rounded *y*, first-syllable stress. The opposite of the thunder-tongue, which has no stops and no *o* or *u*.
4. **The signature grammar** (unchanged): verb first; two initial mutations left by lost endings; conjugated prepositions and no "to have"; two verbs "to be"; verbal nouns for infinitives; a dual for pairs; suffix harmony.
5. **The stone grammar** (new): *the stone is cut; the mortar is the reader's.* The dry cut cuts only the stones of a sentence (its nouns, verbs, qualities and numbers) and leaves out the **mortar words** (articles, most particles, the pronouns, the tense particles, the prepositions). Order carries what they carried. Endings that matter are laid on in letters. Only *not* keeps a mark of its own: the **turned stone**. "Stone has no tense."
6. **The Title in Orrowen:** *Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.* In coal it is 43 letters. Cut dry it is **17 signs**: *memory*, then the five things (home, families, God, freedoms, peace) with the wedge between them.
7. **The hearth's answer, *Tumar*** ("we remember"), is built on the Title's second word, and is also how Orrowen says yes. Cut dry: the Cup, and *-ar*.
8. **Seren's untold line:** *Nawrodhat. Nath noss tul kethyl et gunn sy lo Halyna.* She writes it in the leaf-hand, whole. Cut dry it would be *Not-told. Not yet holding the deep, Halyna.*
9. **The word-signs** are the First Tongue's marks, worn straight by the chisel and stood on the bed: 27 **heads** (a mark alone), each of which may carry one of 20 **crowns** (a second mark cut small and set over it like a capstone). A word-sign stands 4.6 u tall (a letter stands 3) and sits on a **footing**, a second mortar line, so it can never be mistaken for a letter.
10. **The leaf-hand** is the course-hand written: each letter in one movement of the pen, the voicing pin turned into a second leg, the whole hand slanted and joined by hairlines along the line. A line of the Title takes 20 movements of the pen for its 48 letters and marks.
11. **Seren** is ***\*Swe-reŋ-o-s***, "a single sorrow that overcomes": Hal SEREŊOS, with one of the Hal's dead letters in it.

---

## 1 · NAMES

| Thing | In Orrowen | Literally | Notes |
|---|---|---|---|
| the Shoreland tongue | ***Orrowen*** /ˈorouən/ | "of the Shore" (*orrow* shore + *-en*) | What the Rivenmen speak. Formally *brodhen Orrow*, "the speech of the Shore" |
| its old register | ***the Hal*** (*Orrowen Hal*) | "the bedrock [speech]" | The first builders' speech |
| the script | ***Garl Dhrenn*** /ɡarl ðren/ | "the hand of the course" | *garl* hand + *trenn* course, softened in construct. **English: the course-hand.** The family name of all the hands below |
| the chisel register | ***ryt broc*** | "dry cutting" | *ryt* a cutting + *broc* 'dry' (reserve root \**braʔk-*). **English: the dry cut.** The masons also say simply *ryt*, "the cut" |
| the small words it leaves out | ***brodath lodh*** | "the words of mortar" | **English: the mortar words.** "The stone is cut; the mortar is the reader's" |
| a word-sign | ***rellor wrod*** (pl. *rellorath wrod*) | "a sign of a word" | *rellor* 'a sign' (reserve \**reillor-*) + S *brod*. **English: a word-sign** |
| a head · a crown | ***bisk*** · ***hosk*** | "a head" · "a capstone" | The mark a word-sign stands on, and the small mark set over it |
| the footing | ***lodh gunn*** | "the deep mortar" | The second mortar line under every word-sign |
| the NOT mark | ***tolm kylet*** | "the turned stone" | The one mortar word the dry cut keeps as a mark (§7.6) |
| the ink hand | ***Garl Flenn*** | "the leaf-hand" | The scribes' running hand, the one this Book is written in (§8) |
| the Captain's hand | ***garl brenth*** | "the coal hand" | The Title only |
| the first builders' hand | ***Garl Hal*** | "the bedrock hand" | Right to left, mirrored, continuous (§6.9) |
| a letter | ***tolm*** (pl. *tolmath*) | "a stone" | Every letter is a stone; a word, with its bed, is a stone too |
| the mortar line | ***lodh*** | "mortar" | The bed the letters stand on |

The in-world words for writing are the masonry words themselves. A scribe of the guild "lays" a line (*cadh trenn*) as a mason lays a course, and the mortar words are the mortar: a Stonewright cutting a line *dry* is laying it as a dry-stone waller lays a wall, with no mortar, the stones chosen to fit by their shapes alone.

---

## 2 · PHONOLOGY

*Carried over from the wf6 spec unchanged, except the c/k rule, which gains the clause the renderer found missing (wf6 §11b). The First Tongue behind every sound is in `ancestor.md` §2.*

### 2.1 Consonants (living Orrowen)

| | lips | teeth / tongue-tip | back |
|---|---|---|---|
| **stops, voiceless** | p | t | k (written *c* or *k*, §2.4) |
| **stops, voiced** | b | d | g |
| **nasals** | m | n | — |
| **fricatives, voiceless** | f | th /θ/ · s | h |
| **fricatives, voiced** | v | dh /ð/ | — |
| **approximants** | w | l | — |
| **rhotics** | | r (tap or trill) · **rh** /r̥/ ("the rough r") | |

Eighteen consonants. Three more existed in the Hal and have merged (§4): /ŋ/ into *n*, /ʍ/ (*hw*) into *f*, /x/ into *h*. The glide /j/ exists only as the softened form of *g* (written *y* before a vowel).

**Frequency skew.** The common consonants are *l, r, n, t, d, s, th, m*. Rarer are *b, g, dh, v, h*. Rare are *f, rh, w*. *f* is almost confined to old *hw-* words, and *rh* to a handful of old words and names.

### 2.2 Vowels

| | front | front rounded | back |
|---|---|---|---|
| high | i | y /y/ | u |
| mid | e | | o |
| low | | | a |

Plus two long nuclei: **ae** /ɛː/ (only from old long *ē*, as in *Kael*) and **ow** /ou/ (from old long *ū*, and in the place-suffix *-ow*). Unstressed *e* is often /ə/.

**Broad and slender.** *a, o, u, ow* are **broad**. *e, i, y, ae* are **slender**. A word's class is the class of its **last full vowel**, and suffixes follow it (§3.2). This is a harmony of endings. Root vowels are free, so *Corlen* (o…e) and *Pellow* (e…ow) are good words.

### 2.3 Stress and sound

- **Stress falls on the first syllable of every content word.** Particles and pronouns are unstressed and lean on the next word.
- The tongue is musical: long vowels are few, sonorant codas are many (*-rn, -ld, -lm, -rl, -nn, -mm*), and the rolled *r* is frequent.
- Nothing in it has the thunder-break. The drums of the fleet have no counterpart in Orrowen, and to a Shoreland ear the Mystaeri "knock".

### 2.4 Romanisation (the Book's spelling)

The Book spells Orrowen as Seren would hear it, not letter for letter from the course-hand (§6.3 gives the mapping). The rules below keep every existing name valid.

| Spelling | Sound | Rule |
|---|---|---|
| **c / k** | /k/ | *k* before *e, i, y, ae* and at the end of a word after them (*Kael, Aske, Hesk, keth, kyl*); *k* in *-sk* and *-sk-* (*hosk, lusk, Treskan*); *sc-* before any vowel (*sceth*); *c* everywhere else (*Corlen, crenn, covv*) |
| **th, dh** | /θ/, /ð/ | *dh* is never written *dd* |
| **rh** | /r̥/ | word-initial, or at a compound seam |
| **y** | /y/ vowel; /j/ word-initially before a vowel | /j/ occurs only as softened *g* |
| **ae** | /ɛː/ | one long vowel, not *a* + *e*. (In the thunder-tongue the same letters are a diphthong: same spelling, different sound) |
| **ow** | /ou/ | |
| **doubled consonants** | long consonant after a short stressed vowel | *nn, mm, ll, rr, ss*: *Brenn, Tamm, Pellow, carm, Voss* |
| **w** | /w/ | a consonant (*Aldwena*), or the second half of *ow* |
| **wr** | /r/ | the Book keeps the old *w* only in *Stonwryt*, which the guild still spells the old way |

The Book never uses Welsh *ll, dd, ff, ch* or Irish *bh, mh, gc, dt*. Orrowen should not look Welsh or Irish on the page (craft §4d).

### 2.5 Phonotactics

**Syllable shape:** (C)(C)V(C)(C).

| Position | Allowed |
|---|---|
| **Onsets** | any single consonant except /j/ (which comes only from mutation); stop + *r* or *l* (*br, bl, dr, tr, cr, cl, gr, gl, pr, pl*); *s* + stop (*sp, st, sc/sk*); *th* + *r* (rare); *str* only in *Stonwryt*-type compounds |
| **Codas** | any single consonant except *h, w* and /j/; sonorant + stop (*rd, rt, ld, lt, nd, nt, rc*); sonorant + sonorant (*rn, rl, lm, rm*); sonorant + fricative (*rv, lv, rth, rdh*); *st, sk* |
| **Geminates** | only *nn, mm, ll, rr, ss*, and only after a short stressed vowel |

- **Banned everywhere:** *z, x, q, j*, and the Tolkien endings *-ion, -iel, -dor* (the canon rule for both tongues).
- **Repair rules** (they matter when a mutation makes an illegal cluster):
  - A softened *g* before a consonant drops (*g* → *y* → nothing).
  - A softened *rh* after a consonant drops (§3.3).
  - A nasalised *d* before *r* stays *d*.

---

## 3 · GRAMMAR

*§3.1 to §3.10 are the grammar of the whole tongue: what is said, and what the leaf-hand and the coal write. They are carried over from the wf6 spec with two small additions (the yes in §3.4, the vow in §3.9). §3.11 is new: the stone grammar of the dry cut.*

Glosses use: S = softening, N = nasalising, VN = verbal noun, DU = dual, PST = past particle, FUT = future particle, NEG = negative particle, Q = question particle, REL = relative particle. The romanised line shows the mutated sound. The course-hand writes the base letter and a bite (§6.5).

### 3.1 Word order

- **Verb, subject, object, then the rest (VSO).** For example, *Keth et tolm* ("hold the stone"), and *Carm et lodh hy et trun* ("cries the mortar from the ground").
- **The noun comes first in its phrase.** Adjectives, demonstratives and possessors follow it: *et gunn sy* ("the deep this", that is, "this deep"); *hosk et ganna* ("lintel [of] the gate").
- **Numerals come before a singular noun:** *sull carm* ("three call"), *delv vennuld* ("twelve True Man").
- **Particles come before the verb and mutate it:** *re* (PST), *es* (FUT), *nath* (NEG), *ho* (Q), *sa* (REL).
- **Emphasis is a cleft** with the copula: *El et tolm sa heth* ("It is the stone that holds").

### 3.2 Nouns

**No grammatical gender.** Only the pronouns *o* (he, it) and *ey* (she) tell sex. This keeps the soft mutation off the article, which is the Welsh and Sindarin habit craft §4d warns against.

**Number.** Orrowen has three numbers.

| | How it is formed | Example |
|---|---|---|
| singular | the bare stem | *tolm* (a stone) |
| **dual** | *pa* ("two") + S + the singular | *pa yarl* ("two hands", from *garl*); *pa dholm* ("two stones") |
| plural | stem + **-Ath** (*-ath* broad, *-eth* slender) | *tolmath* (stones); *theldeth* (families) |

- **A few old duals are words of their own** ending in *-a*: *ganna* ("gate", literally "the two posts"), *pana* ("both"), and every **pair-name** (§3.10).
- **Collectives and singulatives.** Some nouns name a whole kind, and a single member takes *-el*: *Stonwrytan* ("the guild, the Stonewrights") gives *stonwrytel* ("one Stonewright"); *scethan* ("a fleet") gives *scethel* ("one hull of it").

**Harmony.** A suffix vowel takes the class of the stem's last full vowel. Broad stems (*a, o, u, ow*) take the broad form; slender stems (*e, i, y, ae*) take the slender one.

| Harmonic vowel | broad | slender | In the suffixes |
|---|---|---|---|
| **A** | a | e | plural *-Ath*, agent *-Ard*, participle *-At*, 1du *-An*, 3du *-A*, 1pl *-Ar*, 3pl *-Ant*, ordinal *-Ast* |
| **O** | o | y | verbal noun *-Ol*, abstract *-Oth*, 1sg *-Om*, 2pl *-Os* |

So *tum* ("remember") gives *tumol* ("memory"), and *keth* ("hold") gives *kethyl* ("holding"). The script writes these two vowels with their own **harmonic letters**, so a class is read once per word, from the stem (§6.4).

**Definiteness.** The article is ***et***, the same for every number. It never mutates and never causes a mutation.
- A proper name takes no article, and neither does a noun with a possessive.
- **A noun followed by a definite possessor takes no article (the construct).** *Hosk et ganna* is "the lintel of the gate". *\*Et hosk et ganna* is wrong. Adding an article to the head of a construct is the classic foreigner's error, and it is exactly what the Last Carver did (§11.9).

**Possession between nouns (the construct).** The possessed noun comes first, and the **possessor is softened**:

| Orrowen | Literally | Meaning |
|---|---|---|
| *garl Dhrenn* | hand S-course | the course-hand |
| *lest Vardh* | house S-God | a temple |
| *Kethow Dhresk* | keep S-cleft | Rivenkeep |
| *tumol ol varn* | memory [of] our home | memory of our home |

### 3.3 The two mutations

Both mutations change only the **first consonant of the next word**. The course-hand always writes the base letter, with a bite under it (§6.5), so the dictionary form can always be found. The outcomes and their triggers are Orrowen's own. Neither table is Welsh's or Irish's, though both are the same kind of thing.

**Softening (S, *the wearing*).** In the old tongue these consonants wore soft between vowels. The vowels at the ends of words are gone, but the wearing stayed.

| base | p | b | m | t | d | c/k | g | rh |
|---|---|---|---|---|---|---|---|---|
| **softened** | v | w | v | dh | r | h | y (nothing before a consonant) | h (nothing after a consonant) |

*f, v, w, th, dh, s, h, l, r, n* and all vowels are unchanged.

**Nasalising (N, *the bedding*).** These words once ended in *-n*, and the *n* bedded into the word that followed.

| base | p | t | c/k | b | d | g | vowel |
|---|---|---|---|---|---|---|---|
| **nasalised** | b | d | g | m | n | n | *m-* before a broad vowel, *n-* before a slender one |

*f, v, w, th, dh, s, h, l, r, rh, m, n* are unchanged.

**What triggers which** (each trigger was once a word ending in a vowel or in *-n*; §4.3):

| Softening (S) after | Nasalising (N) after |
|---|---|
| the possessives *tho* (your), *o* (his/its), *olna* (our two), *sona* (their two), *so* (their) | the possessives *en* (my), *ol* (our), *va* (your, pl.) |
| the prepositions *hy* (from), *um* (upon), *lo* (at, by) | the prepositions *ul* (in), *dem* (until, as far as) |
| the particles *re* (PST), *ho* (Q), *sa* (REL), and the prefix *na-* (un-) | the particles *nath* (NEG) and *es* (FUT) |
| the numeral *pa* (two), and *gor* (every) | |
| the possessor in a construct; the second element of a compound; a noun called by name (vocative) | |

- **Only the word immediately after the trigger mutates**, and only once.
- **Adjectives do not mutate**, except after a dual: *pa yarl dhevel* ("two young hands", from *tevel*).

### 3.4 Verbs

A verb is a stem plus a person ending. Tense is carried by a particle before the verb.

| Person | Ending | *tum* "remember" (broad) | *keth* "hold" (slender) |
|---|---|---|---|
| 1sg | -Om | tumom | kethym |
| 2sg | -ith | tumith | kethith |
| 3sg | (none) | tum | keth |
| 1du (we two) | -An | tuman | kethen |
| 3du (they two) | -A | tuma | kethe |
| 1pl | -Ar | **tumar** | kether |
| 2pl | -Os | tumos | kethys |
| 3pl | -Ant | tumant | kethent |

There is no 2nd-person dual. A pair is spoken to as many, and answers as two.

| Form | How it is made | *tum* | *keth* |
|---|---|---|---|
| **present** (also habitual) | the plain forms | *tumar* "we remember" | *keth* "holds" |
| **past** | *re* + S | *re dhumar* | *re heth* |
| **future** | *es* + N | *es dumar* | *es geth* |
| **negative** | *nath* + N | *nath dumar* | *nath geth* |
| **question** | *ho* + S | *ho dhumos?* | *ho heth?* |
| **imperative** | bare stem (to one); stem + *-a* (to many) | *tum!* · *tuma!* | *keth!* · *ketha!* |
| **verbal noun** | -Ol | *tumol* "remembering, memory" | *kethyl* "holding" |
| **participle** | -At | *tumat* "remembered" | *kethet* "held" |
| **agent** | -Ard | *tumard* "one who remembers" | *Ketherd* "holder": the Commander |

- **Yes and no.** Orrowen has no words for "yes" or "no". You answer by repeating the verb: *Ho dhumos?* ("Do you remember?") is answered *Tumar* ("We remember") or *Nath dumar* ("We do not"). **So the hearth's answer is, grammatically, a yes**: every stone leaf asks, and the hearth says yes to it. (Jack, note 2: "I like that yes means we remember.") Cut dry, the yes is the Cup and its ending, [TUM]**A r** (§11.3).
- **The progressive** uses the state verb, *ul* ("in") and a verbal noun: *Doss et hald ul glennol* ("the wall is in mending", that is, "the wall is being mended"; *clenn* "mend" nasalised after *ul*).
- **The imperative plural** in *-a* sounds the same as the 3du of broad verbs (*tuma*). Context settles it, because a dual verb always has a subject.

**The two "be" verbs.** They are the most irregular words in the tongue, as the oldest words usually are.

| | Present | Past | Future | Negative |
|---|---|---|---|---|
| **state verb *doss*** (where, how, whether a thing is) | *doss* (1sg *dossom*, 1pl *dossar*…) | suppletive **re yal-**: *re yal*, *re yalar* (from old *gal-*) | *es noss* | *nath noss* |
| **copula *el*** (what a thing is) | *el* | *ew* | (the tongue uses *doss* instead) | *nel*, past *new* |

- The copula puts the predicate before the subject: *El tolm et hald* ("[It] is stone, the wall").
- *Somm el tolm tolm* means "while stone is stone".

### 3.5 Pronouns and possessives

One set of forms serves as both subject pronoun and possessive. The mutation after it marks the possessive.

| | sg | dual | pl |
|---|---|---|---|
| 1 | **en** (+N) | **olna** (+S) | **ol** (+N) |
| 2 | **tho** (+S) | (use the plural) | **va** (+N) |
| 3 | **o** "he, it" (+S) · **ey** "she" (no mutation) | **sona** (+S) | **so** (+S) |

- The dual pronouns are the plural plus *-na*.
- **Verbs already carry their person**, so a pronoun after the verb is emphatic: *Tumar ol* ("*We* remember").
- **Object pronouns** come after the subject: *Re hadhan o* ("PST-S-laid-1du it", that is, "we two laid it").
- **When the mutation cannot show, nothing marks the possessive.** Before a word the softening leaves unchanged (*f, v, w, th, dh, s, h, l, r, n*, a vowel), *o saed* after a verb reads "he, half" or "it, half", not "its half"; *o hosen* reads "he … like", not "his equal". Say the possessor as a noun (*saed et covv*, "the half of the cloak") or recast (*uld hosen et Crenn*, "a man like the Captain"). The same holds for *en, ol, va* before a letter the bedding leaves unchanged. *(Back-translation of pilot I.1.)*

### 3.6 Prepositions, conjugated

Prepositions take the person endings directly. There is no "to me" or "on him".

| | at, by: ***lo*** (+S) | upon: ***um*** (+S) |
|---|---|---|
| 1sg | lom | umom |
| 2sg | loth | umoth |
| 3sg m / f | lo / loy | umo / umoy |
| 1du | lona | umona |
| 1pl | lor | umor |
| 2pl | los | umos |
| 3pl | lont | umont |
| 3du | lonta | umonta |

The other prepositions follow the same pattern: *ul* (in, +N), *hy* (from, +S), *dem* (until, +N).

***Hy* is also "than"** ("greater from X"): *hos strom hyo*, "one greater than he". After a verb of going the "from" reading wins (*orr hy*, "leave"; *re orrant uldath strom hyo* is heard "great men went from him"), so a comparison is not set after *orr*. *(Back-translation of pilot I.1.)*

### 3.7 Having, being able, feeling: the "at" and "upon" idioms

Orrowen has no verb "to have", no modal "can", and no verb for most feelings.

| Meaning | Pattern | Example | Literally |
|---|---|---|---|
| *Y has X* | *Doss X lo Y* | *Doss tolm lom.* | "Is a stone at me." (I have a stone.) |
| *Y can V* | *Doss* VN *lo Y* | *Doss kethyl et tolm lom.* | "Is holding the stone at me." (I can hold the stone.) |
| *Y cannot V* | *Nath noss* VN *lo Y* | Seren's line (§11.4) | |
| *Y feels X* | *Doss X um Y* | *Doss lomm umom.* | "Is grief upon me." (I grieve.) A feeling is laid on a person, as a course is laid |
| *X knows Y* (by touch) | *keth* "hold" | *Re hethe Halyna et mesk.* | "Halyna (3du) held the wood." The Shoreland word for a knowing is the canon's own verb: to know the wood is to *hold* it |

### 3.8 Negation, questions, relatives

- **Negation:**
  - *nath* + N before a verb: *nath geth* ("does not hold");
  - *nel* for the copula;
  - the prefix *na-* + S for "un-": *nawrodhat* ("untold"), *nadhum* ("forget"), *nayald* ("destroy", un-build), *nalodhat* ("unbonded", un-mortared).
  - **"only" of a clause** is *nath … veth*, "not … but": *sa nath re yorrar veth amm ew venn et dask*, "who fought only when the cause was just", as *re heth o ol lo nayalat veth osk*, "he held us by nothing but trust". *Hosel* "only, alone" set after a verb reads "alone". *(Back-translation of pilot I.1.)*
  - ***nath … tul* is "not yet"** (Seren's line, §11.4), never "no longer"; the tongue has no word for "no longer", and says it another way (*re vammant so hrenneth*, "they had lost their captains"). *(Back-translation of pilot I.1.)*
- **Questions:** *ho* + S for a yes/no question. The question words are *cedh* (who), *vodh* (what), *ul vodh* (where; "in what"), *hy vodh* (why; "from what"), *amm vodh* (when).
- **Relatives:** *sa* + S, with a gap where the shared noun would be: *et tolm sa heth* ("the stone that holds"), *Voss sa re vess* ("Voss who asked", from *pess*).

### 3.9 The formal and oath register

1. **The dual for pairs.** The Bonded speak of themselves as "we two" (1du), and are spoken of by their pair-name with 3du verbs: *Tuma Halyna* ("Halyna remember").
   - Where the Book gives Halyna a plural verb, the Orrowen original is dual.
   - Common speech in the havens had let the dual slip into the plural. The guild never did.
2. **Swearing.** An oath begins *Rytom um …* ("I cut [my word] upon …"), using *ryt*, "cut a vow". Kael's oath opens *Rytom um hosk…* ("I swear upon the lintel…").
3. **Closing an oath.** An oath closes with the one-word vow ***Ston.*** ("It stands."). In writing it is followed by the gate mark (§6.7). Liturgy keeps the Hal form ***Stonos***. **(v2) A vow is cut whole**, in letters, even in stone (§3.11 D9).
4. **Respect.** Elders and bonded pairs are addressed in the 2pl (*va*). The Captain addresses a True Man in the singular (*tho*), as a comrade.
5. **Antiphony.** A line said "one voice to the comma and the other the rest" (the Cry, *Two at the Gate*, the guild's word) is split at the wedge mark (§6.7). In Seren's two inks, one ink runs to the wedge and the other takes the rest.
6. **Old words in liturgy.** The Rite of the Cornerstone is recited in the Hal. The guild pronounces it by the living tongue's rules, as best it can, and knows the words sound wrong (§4.5).

### 3.10 Names

- **Epithets:**
  - *X of the Y* is a construct: *Rhyna Yanna Ulvenn* ("Rhyna of the Inner Gate"; *ganna* softened as possessor).
  - *X the Y* is apposition: *Kael Nydherd* ("Kael the Counter").
  - *X who V* uses the relative: *Voss sa re vess*.
  - A compound epithet is modifier + softened head: *Halvard Tolmvard* ("Halvard Stone-Warden"). His epithet translates his own name (§4.6).
- **The pair-name (*hoskvoll*, "lintel-name").** At the sealing (*hoskol*, "the laying of the lintel") the guild names a pair as a gate is made:

  | Part | What it is | Halyna | Aldwena | Idrenna |
  |---|---|---|---|---|
  | **first post** | the first syllable of his cradle-name | Hal- (Halvard) | Ald- (Aldun) | Id- (Idlan) |
  | **second post** | her cradle-name without its final vowel, **softened** as the second element of a compound | *Rhyn-* → -yn- (rh → h, lost after a consonant) | *Ben-* → -wen- (b → w) | *Denn-* → -renn- (d → r) |
  | **lintel** | the old dual ending *-a*, laid across both | -a | -a | -a |
  | **pair-name** | | ***Halyna*** | ***Aldwena*** | ***Idrenna*** |

  - The three canon pair-names come out of one rule by three different softenings. Every pair-name ends in *-a*, because the lintel is the dual.
  - A pair-name takes a dual verb.
  - In writing, a pair-name carries a **sealing lintel** (§6.8).
- **The unbonded keep one name.** *Seren* has no lintel and never will; "one name is a mourning".

### 3.11 The stone grammar (the dry cut)

**The principle.** *The stone is cut; the mortar is the reader's.* A dry-stone wall stands without mortar, its stones chosen to fit. The dry cut writes a sentence the same way: it cuts its stones (the words that carry the matter) and leaves its mortar (the small words that bind them) for the reader to lay in, as every Rivenman who can read already knows how. It is the economy Jack's note 1 asks for, and the reason is the chisel's: a word cut in granite costs a mason an hour, and a small word costs him as much as a large one.

**D1 · Only the stones are cut.** Nouns, verbs, qualities, numbers, and the few adverbs and conjunctions that carry weight (*tul* "yet", *somm* "while", *amm* "when") are cut. A word with a word-sign (§7.7) is cut as its word-sign; any other word is cut in letters. *(Notation: in this file **[WORD]** is the word-sign that reads *word*, so [THELD] is the sign read *theld*, which is the head ODH under the crown drop; **HEAD+crown** names a sign by its parts; bold lower-case letters after a sign, as [THELD]**A th**, are its complement.)*

**D2 · The mortar words are left out.** They are never cut, except in a vow (D9):

| Left out | The mortar word | How the reader lays it back in |
|---|---|---|
| the article | *et* | always: a stone is "the" stone |
| the copula and the state verb | *el, ew; doss, noss, re yal-* | a line with no verb is a naming (D4); the "at" and "upon" idioms keep their nouns only |
| the conjunctions | *eth* "and", *ell* "or", *veth* "but" | the wedge stands between the things it joins; which of the three is meant is read from the sense |
| the relative and the question | *sa*, *ho* | "a stone does not ask": questions are not cut |
| the tense particles | *re* (past), *es* (future) | **stone has no tense**: a work's inscription speaks of what stands, a memorial of what was, a vow of what shall be. Where the time must be cut, a time is cut (a day, a year, a count of generations) |
| the pronouns and possessives | *en, tho, o, ey, olna, ol, va, sona, so* | the verb's ending, or the order, or the stone itself: an inscription speaks with the voice of those who cut it, so "our" is the wall's own |
| the demonstratives | *sy, ull* | "this" is the stone the words are cut on |
| the prepositions | *ul, hy, um, lo, dem* | from the verb and the order: "cries mortar ground" is read "the mortar cries from the ground", "lay stone stone" as "stone upon stone" |
| the small quantifiers | *gor* "every", *sost* "very" | the plural complement, or nothing |

**D3 · The one mortar word that keeps a mark is *not*.** *Nath*, *nel*, *new* and the prefix *na-* are cut as the **turned stone** (§7.6), set against the stone they turn, on its bed. A thing cut not-so must never be read as so.

**D4 · Order is the order of speech.** The verb comes first, then its subject, then its object, then the rest, exactly as in §3.1. A line that begins with a noun has no verb and is a **naming**: a heading, a memorial, a label, a proverb. Two nouns side by side are a construct, the second the possessor (*hosk ganna*, "the lintel of the gate"), unless the line is a proverb, when they are predicate and subject as the copula would put them.

**D5 · Endings are laid on in letters** (phonetic complements). A word-sign alone is the bare stem: a singular noun, the 3rd-person or imperative singular of a verb, an adjective. An ending that says something the order cannot is cut after it, in letters, on the same bed:

| Ending | Cut as | Example |
|---|---|---|
| plural *-Ath* | **A th** | [THELD]**A th** *theldeth*, families |
| verbal noun *-Ol* | **O l** | [TUM]**O l** *tumol*, memory |
| participle *-At* | **A t** | [BRODH]**A t** *brodhat*, told |
| agent *-Ard* | **A r d** | [VESK]**A r d** *veskerd*, a seer |
| abstract *-Oth* | **O th** | [VENN]**O th** *vennoth*, faith |
| singulative, dear *-el* | **e l** | [TEV]**e l** *tevel*, young |
| collective *-an* | **a n** | [TRESK]**a n** *Treskan*, the Rivenmen |
| belonging *-en* | **e n** | [ORROW]**e n** *Orrowen*, the tongue |
| place *-ow* | **o w** | [MYST]**o w** *Mystow*, the Mystlands |
| ordinal *-Ast* | **A s t** | (with numeral letters) |
| person endings | **O m, i th, A n, A, A r, O s, A n t** | [TUM]**A r** *Tumar*, we remember |
| imperative plural *-a* | **a** (a full vowel) | [TALD]**a** *Talda*, rise |
| the dual, the feminine *-a* | **a** | [ODH]**a** *odha*, a mother |

- The harmonic letters **A** and **O** take their class from the word-sign's own word (its class is listed in §7.7), as they would from the stem's last full vowel in letters.
- **An irregular ending is cut in full vowels**, as a name is: [TEV]**a th** *tevath*, [FLENN]**a th** *flennath*.
- **A person ending is cut only when no subject stone follows.** *Tuma Halyna* is [TUM] =Halyna: the pair-name says who, and the dual is read from the pair-name.

**D6 · No mutations are cut.** The dry cut writes no bites. A mutation belongs to the mortar word that caused it, and the reader lays both back in together. (A construct's softened possessor and a compound's softened second element are read from the order too.)

**D7 · Letters, always:**
- the names of persons, and pair-names with their sealing lintel (a name is said, not meant);
- a word with no word-sign;
- loan words and Mystaeri names, spelled by sound, with the knock as a wedge inside the word;
- numbers, as capped numeral letters (§6.8).

Place-names that are plain words are cut as their words: *Cemm Hyll* (Tidesmeet) is [CEMM] [HYLL].

**D8 · Compounds are their stones, side by side on one bed:** *Stonwryt* is [STON][RYT]; *Stonwrytan* is [STON][RYT]**a n**; *vennuld* is [VENN][ULD]; *gorndholm* is [GORN][TOLM].

**D9 · A vow is cut whole.** A Stonwryt, an oath (*Rytom um …*), the Covenant: every word, every mortar word, every ending and every bite, **in letters**, then the gate. "A sign holds what is meant; a vow must hold what was said", for a vow is sworn aloud, and whoever raises the stone must be able to say it again word for word. When a vow is only **cited** (on the Stonwryt coin, on the lintel of a finished work, in the rolls), it is cut dry, and **the gate alone is read *Ston*** (§11.6).

**D10 · The marks.** The perpend ends a sentence; the wedge is a pause, and stands between the things *eth*, *ell* and *veth* would have joined; the gate ends a vow and is read *Ston*; the coping ends a tale; the foremark (the word-sign *hosast*, "first") may stand at the head of a work. A cry, a question and direct speech are not marked.

**D11 · Beds and lines.** Each word (the turned stone if any, its word-sign or signs, its complement letters; or a word in letters) is one stone on its own bed, parted from the next by a head-joint, and lines break the joint exactly as in §6.8. Every word-sign also stands on its footing. The line pitch is 6.4 u.

**How much the dry cut saves.** Across the eight sample texts of §11 the dry cut uses **117 signs** where the leaf-hand uses **339 letters and marks**: 35 per cent. A granite Book would be about a third as long as the ink one.

---

## 4 · HISTORY: FROM THE FIRST MARKS TO THE LEAF-HAND

### 4.1 Three stages of the tongue, and the surfaces they live on

| Stage | Who wrote it | Where it survives in the Book | How it is written |
|---|---|---|---|
| **The Hal** (the first builders, "in the age before the havens") | the founders of the Keep | the Stonwryt under the old capstone (the tale-stone); the mark on the black chest; the slate leaves of the Rite; the top names on the lintel of the western stair | *Garl Hal*: right to left, mirrored, continuous; word-signs with no endings and no small words, letters for names; three archaic letters. A vow is cut whole |
| **Haven Orrowen** (the twelve generations of the havens) | the rolls, the Council, the clerks | the archive rolls, the Stonewrights' warning, the warden's report, the middle names on the lintel | the rolls in the leaf-hand; stone in the dry cut, with some old spellings kept |
| **Living Orrowen** (the Rivenmen) | Seren, the hearth, the wall | the Book, the Title, every living leaf | the leaf-hand (*Garl Flenn*) for ink; the dry cut for stone; the coal for the Title |

The lintel of the western stair shows the whole history in one column, "one beneath another, for as many generations as the quarry was worked". The top names are Hal, cut right to left. The middle names are haven spellings. Halvard's line is at the foot, in the living hand. Names are always letters (D7), so the column reads by letter, and a player who has earned the old hand can read it downward and watch the tongue change.

### 4.2 The four hands on the economy scale

Writing on the Shore began with meanings and ended with sounds, and every step toward sound was also a step toward ink.

| | **The first marks** | **The Hal** | **The dry cut** | **The leaf-hand** |
|---|---|---|---|---|
| **who** | the First Tongue's one people | the first builders | the living guild | Seren and every scribe |
| **on** | whatever stood: a stone set up, a trunk | stone | stone | a leaf of ink |
| **signs** | 45 marks, each a word and a sound at once | word-signs (the marks, worn straight) and the reform's letters | word-signs, letters, one mark (*not*) | letters only |
| **small words** | none | none (a vow is cut whole) | none but *not* (a vow is cut whole) | all |
| **endings** | none | **none**: the reader supplies the Hal's full endings | laid on in letters where they matter | all, in harmonic letters |
| **mutations** | — | never written | never written | written, as bites |
| **word-gaps** | — | none | head-joints | spaces |
| **the Cry's first sentence** ("The mortar cries out from the ground") | 3 marks | 3 signs, one bed | 4 signs | 18 letters and marks |

**So the Hal is the most economical hand of all** that can still be sounded. The first builders had just made the letters (the reform, `ancestor.md` C6), but they cut with the old marks wherever a mark would do, spelled only names and the words no mark held, and left every ending and every small word to the reader, who spoke the Hal and could not mistake them. The living dry cut is a little fuller: the living tongue has lost the Hal's endings and turned their loss into mutations and harmonic suffixes, so the endings that still carry meaning are laid on in letters. The leaf-hand writes everything.

**This is consistent with `ancestor.md`, and extends it in three places** (§14b lists the emendations):
- The ancestor says the first marks "wrote no small words, as the grain still writes none", and that the first builders' reform was "the 'reformed' hand in your sense: few strokes, laid by rule". Both stand. The reform made the *letters*; it did not stop the builders cutting word-signs.
- The ancestor says "the stone kept the sound, and the wood kept the meaning". This stays true in the sense that matters: a **word-sign is a word, not a meaning**. It is read as one Orrowen word, aloud, and when the word's meaning drifted, the sign followed the word (the Cup is read *tum*, "remember", though the mark meant "hold"). The grain's signs are read as meanings, in no particular words. Neither living hand reads a mark for its first sound any more: that use became the letters (`ancestor.md` §1.1).
- **The tale-stone's Stonwryt is cut in full, in letters, word for word, because it is a vow** (D9). It is the one Hal text anyone can still sound, and the ancestor's derivation of it (§1.6 c) is unchanged.

### 4.3 The sound changes, in order

*Carried over from the wf6 spec. The exact laws, stage by stage from the First Tongue, are in `ancestor.md` §4.1 (O1–O5 to the Hal, H1–H6 to the living tongue), which derives every Orrowen word with no mismatches.*

Each change is regular. Irregular forms today are the ones these changes left behind.

1. **The wearing (softening), inside the Hal.** Between vowels, at compound seams, and after a word ending in a vowel, a single *p b m t d k g hr* was pronounced soft: *v w v dh r h y h*. The Hal hand never wrote this; it was only how the words were said.
2. **The bedding (nasalising).** After a word ending in *-n*, *p t k* were voiced and *b d g* became nasals. A following vowel took the *n*.
3. **The fall of the endings.** Unstressed final syllables were lost:
   - the case and number endings *-os* (broad nouns), *-is* (slender nouns), short *-a, -e, -i, -o*;
   - the *-n* of the particles.

   With the endings gone, the wearing and the bedding were no longer explained by any sound. They became grammar, which is exactly how the Celtic mutations arose (craft §4c).
   - Old *tolmos* > *tolm* (stone); *xaldos* > *hald* (wall); *theldis* > *theld* (family).
   - Old *ulan* 'in' > *ul*, still nasalising.
   - Old *umo* 'upon' > *um*, still softening.
4. **Long vowels shifted:** *ā > o*, *ē > ae*, *ī > i*, *ō > u*, *ū > ow*.
   - Old *kēlos* > *Kael*; old *orrū* 'at the sea's edge' > *orrow* 'shore'; the old locative *-ū* > the place-suffix *-ow*.
   - **Final long *-ā* survived** as *-a*. This is the dual ending, the lintel of every pair-name.
5. **Three mergers:**
   - old /x/ merged into *h*: *xal* > *hal* (bedrock);
   - old /ŋ/ merged into *n*, or assimilated: *soŋmas* > *somm* (while);
   - old /ʍ/ (*hw*) merged into *f*: *hwrennos* > *frenn* (frost), *hwlennā* > *flenn* (leaf).

   The Hal hand has a letter for each of the three lost sounds (§6.9).
6. **Old *wr-* lost its *w*:** *wryta* > *ryt* (a cut vow). The guild still spells its greatest word the old way, ***Stonwryt***, and says it /ˈstonryt/.
7. **Harmony.** Unstressed suffix vowels reduced, then took the colour of the stem. Old *kethola* > *kethyl*, but *tumola* > *tumol*; old plural *-athi* > *-ath* / *-eth*. The Hal spells every suffix vowel in full, and the living hand writes the harmonic letters.

### 4.4 Where each trigger came from

*Carried over, with the ancestor's two emendations of this table adopted: Hal **re** (not *rea*) and Hal **van** (not *vanan*), `ancestor.md` §4.3.*

Every trigger in §3.3 is explained by its old ending. None of them is arbitrary.

| Living | Old (Hal) | Old ending | So today |
|---|---|---|---|
| *ul* in · *dem* until · *es* FUT · *nath* NEG | *ulan · demen · esan · nathan* | *-n* | N |
| *en* my · *ol* our · *va* your (pl) | *enan · olon · van* | *-n* | N |
| *hy* from · *um* upon · *lo* at | *hya · umo · loa* | vowel | S |
| *re* PST · *ho* Q · *sa* REL · *na-* un- | *re · hoa · sae · na-* | vowel | S |
| *tho* your (sg) · *o* his · *so* their | *thoe · oa · soa* | vowel | S |
| *olna* our two · *sona* their two | *olnā · sonā* | long *-ā*, kept | S |
| *pa* two · *gor* every | *pā · gora* | vowel | S |
| *et* the · *ey* her · *eth* and · *el* is | *etas · eyas · ethas · elis* | *-s* | nothing |
| a construct possessor, a compound's second element | once the genitive, and the seam | a vowel before the word | S |

### 4.5 Why a Rivenman cannot read the Hal

He can see every letter of it. What he cannot do is *sound* it, and now, for most of it, he cannot even find the words.

1. **It runs right to left, and every letter faces the way it runs.** The forward-leaning prop of a lip-sound leans leftward in the Hal, so an old *p* looks like a living *k*.
2. **There are no word-gaps.** A Hal line is one unbroken course.
3. **It spells the endings the living tongue has lost**, wherever it spells a word at all (§6.9): *TOLMOS* for *tolm*, *HALDOS* for *hald*.
4. **It writes no bites.** It writes the base letter where the living tongue says the softened sound. So the old pair-name the Rivenmen say *Aldwena* is cut ***ALD·BEN*** under its lintel (§6.8).
5. **Three of its letters stand for sounds no one has said in twelve generations** (*x, ŋ, hw*). It also marks old long vowels.
6. **Some of its words are simply gone.**
7. **(v2) Most of it is not in letters at all.** Outside the one vow, the Hal is cut in word-signs, mirrored, with no endings and no small words. A Rivenman knows perhaps half of those signs from the living dry cut (the same heads and crowns, turned the other way and cut taller), but he cannot supply the Hal's endings or its small words, because he does not speak the Hal. So the Bonded keep the slate leaves of the Rite as a liturgy, learned by heart with their Hal readings, and read the signs as reminders of words they already know.

This is the real reason "the first fathers of the guild had known better, and we had forgotten them": the forgetting is written into the stone. Halyna "read the leaves by lamplight" in I.4 because the Bonded keep the Hal as a liturgy. Earning the old register in play is learning what they already knew.



### 4.6 The Shoreland names

| Name | Old form (Hal) | Sense | Note |
|---|---|---|---|
| **Halvard** | *Xalpardos* | "bedrock-warden": *hal* (living rock) + softened *pard* (warden) | His epithet, *Tolmvard* "Stone-Warden", translates his name. The Old Norse gloss "rock-guardian" becomes a folk comparison **[Jack]** |
| **Rhyna** | *Hriunā* | "she who sets fast", from *rhyn-* (to set, of mortar) + feminine *-ā* | *hr > rh*, *iu > y*. At the root (\**xreun-*) it is the wood's word for stone, *rhen* (`ancestor.md` §1.5) |
| **Halyna** | — | pair-name: Hal- + softened Rhyn- + lintel -a | §3.10 |
| **Aldwena** | *Ald·Ben* (the Hal ligature) | pair-name of the first builders: *Aldun* + *Bena* | |
| **Idrenna** | — | pair-name: *Idlan* + *Denna* | The Theoliths of II.3 |
| **Seren** | ***SEREŊOS*** | ***"a single sorrow that overcomes"***: First Tongue \**Swe-reŋ-o-s*, \**swe-* "one's own; one alone, single" + \**reŋ-* "a sorrow that is carried and does not break the one who carries it" + the nominative \**-o-s* | **Jack's note 6.** \**sw-* > *s-* (O4) gives the Hal SEREŊOS; the ending falls (H2) and *ŋ* > *n* (H4) give living *Seren*. \**reŋ-* survives nowhere else in either tongue; \**swe-* survives in *sost* "self, very". The Hal writes her name with the shore-nasal ŋ, one of the three letters no one has sounded in twelve generations: the sorrow in her name is, in the old hand, a letter no one can say. The same First Tongue word would come out *Seren* in the wood's tongue too (`ancestor.md` §6), the one name in the Book that is the same in both. The guild hears *ser* "go on" in it: a folk etymology, and a true thing about her, but not its source. Welsh *seren* "star" is a coincidence of sound only |
| **Tarnel** | *Tarnelos* | "little net" | A fisher's son of Tidesmeet |
| **Kael** | *Kēlos* | "a tally-notch" | *ē > ae*; he is Kael the Counter |
| **Stannard** | *Stannardos* | "quarrier", from *stann* + *-ard* | "the quarryman" |
| **Garvel** | *Garvelos* | "little smith", from *garv-* (a Hal word lost from the living tongue) + *-el* | |
| **Pellow** | *Pellū* | "of the spire" | |
| **Corlen · Voss · Hale · Brenn · Marl · Tamm · Aske · Harl · Ulden · Hesk · Lanner · Aldun · Bena · Idlan · Denna** | (their Hal forms are in `ancestor.md` §3.2) | **none: names are names** | Jack's note 6. The laws account for their sounds; no meaning is given, and the real-world senses (Estonian *tamm*, Old Norse *askr*, English *marl*, Scots *harl*) are never borrowed. Brenn's First Tongue shape happens to be the word for "mouth"; the Book gives him none |

**In every hand, a name is letters.** The dry cut never writes a name with word-signs, even where a name is made of words (Halvard, Stannard): "a name is said, not meant" (D7).

### 4.7 The Book's translations, and a hybrid exonym

*Carried over from the wf6 spec unchanged.*

The Book is Seren's translation. Where she chose a learned or English word, there is an Orrowen original behind it.

| In the Book | Orrowen | Literally | Why the Book's word |
|---|---|---|---|
| **Stonwryt** | *Stonwryt* (Hal *stonwryta*) | "the standing cutting": *ston* (standing) + *wryt* (a cut vow) | Not translated. It is the guild's own word, kept in its old spelling |
| **the Stonewrights** | *Stonwrytan* | "those of the Stonwryt" | Seren's English echoes the guild's own name, which is why she chose it |
| **the Theoliths** | *Tolmath Vardh* (sg. *Tolm Vardh*) | "stones of God" | theo- = *Mardh*, -lith = *tolm*: a scholar's rendering |
| **the Aetherbond** | *Lodh Helv* | "the mortar of the sky" | aether = *helv*, bond = *lodh* |
| **the Bonded** | *et Lodhan* | "those of the mortar" | |
| **the sealing** | *hoskol* | "the laying of the lintel" | |
| **the Covenant of Completion** | *Ryt Dhunnoth* | "the vow of wholeness" | Its words stay withheld |
| **Rivenkeep** | *Kethow Dhresk* | "the holding-place of the cleft" | |
| **the Rivenmen** | *Treskan* | "the cleft-folk" | |
| **the Torn Cloak** | *Covv Treskat* | "the riven cloak" | **Torn and riven are one word in Orrowen.** The cloak and the Keep share it |
| **the Title** | *et Hosk* | "the lintel" | The words set over a text, as a lintel over a door. The Title of Liberty is *Hosk Lunn*, "the lintel of freedom" |
| **the Shorelands · Shorelanders** | *Orrow · Orrowan* | "the Shore · the shore-folk" | |
| **Mystaeri** | *Mystaeri* | *myst* (Shoreland "sea-fog, the grey") + *-aer* (the thunder-tongue's "those of", heard across the water in its old shape) + the old loan-plural *-i* | A true hybrid, borrowed early, so it kept the Mystaeri ending before that tongue turned *-aer* into *-ear*. The Book keeps it untranslated |
| **Mystwood · Myststone · the Mystlands** | *Mesk Myst · Tolm Myst · Mystow* | "wood of the grey · stone of the grey · the place of the grey" | *Mystow* is the Orrowen behind Jack's "the Mystlands" |
| **Mystholders · Mystarchs** | *Gannath Myst · Crenn Myst* | "the posts of the grey · the captain of the grey" | "as posts hold up a roof" |

**The ten havens.** The English names in the Book are translations, and each haven has an Orrowen original. That settles the originality question for Highreach and Sandreach at the level of the tongue. Whether the English labels stay is still **[Jack]** (Name Map d.2).

| Book | Orrowen | Literally |
|---|---|---|
| Eldhythe | *Tavow Hemm* | the old landing |
| Tidesmeet | *Cemm Hyll* | the meeting of the tide |
| Fenholm | *Sedhnell* | fen-islet |
| Holtward | *Lurrvard* | forest-ward |
| Carnhold | *Kethow Stellath* | the hold of the cairns |
| Emberhythe | *Tavow Vorr* | the landing of fire |
| Sandreach | *Grullsorth* | sand-ridge |
| Rimewatch | *Frennvar* | frost-guard |
| Highreach | *Taldow Helv* | the high place of the sky |
| Glasspire | *Sirrvell* | glass-spire |

---

## 5 · LEXICON

*The wf6 lexicon, every entry kept, with Seren's row made Jack's (note 6) and a new column, **dry cut**, saying how the stone writes each word: its word-sign (**HEAD+crown**, or **HEAD** for a root sign; the number is its row in §7.7), its sign with a complement, or **letters**. A word the dry cut leaves out (D2) says so. The ancestor derives every entry from the First Tongue (`ancestor.md` §4.4). The reserve words that have word-signs are listed with their signs in §7.7 and are not repeated here.*

**How the words were made.** Following Peterson's "lexicon from culture" (craft §4b), the fields are built from the Shorelanders' own metaphors: **to tell a tale is to lay a course** (*cadh trenn*); **a promise is a cut stone** (*ryt*); **a pair is a gate** (*ganna*, the dual of "post"); **to know the wood is to hold it** (*keth*); **freedom is loosing** (*lusk*, *lunn*); and now **the small words are the mortar** (*brodath lodh*). Several English words map to one Orrowen word: *trenn* course, line, tale; *keth* hold, keep, know; *vesk* see, read; *tresk* cleft, riven, torn.

Columns: **Orrowen** (the living form, as the Book spells it) · **Hal** (the old form, where it is known or needed) · **cl.** (harmony class: B broad, S slender) · **sense** · **note** · **dry cut**.

### 5.1 Stone and building

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **tolm** | *tolmos* | B | a stone; a dressed stone of a wall; a letter of the course-hand | S *dholm*, N *dolm* | **TOLM** (1) |
| **hal** | *xalos* | B | bedrock, the living rock of the ridge | in *Halvard* | **TOLM+course** (12) |
| **hald** | *xaldos* | B | a wall | "rock made to stand", from *hal* | **HALD** (21) |
| **lodh** | *lodhos* | B | mortar; the mortar line of a text; the bond | *Lodh Helv*, the Aetherbond | **LODH** (291) |
| **trenn** | *trennos* | S | a course of stones; a line of writing; a tale laid in one night | "a tale that is laid is part of the wall" | **TRENN** (39) |
| **cadh** | — | B | (v.) lay a stone, a course, a tale | *cadhat* laid; *Cadh et trenn* "Lay the tale" | **TRENN+still** (43) |
| **ston** | *stonos* (3sg) | B | (v.) stand (of a wall), make stand, hold firm | ***Ston.*** "It stands": the close of an oath | **TOLM+still** (11) |
| **gald** | — | B | (v.) build, raise a work | S *yald* | **HALD+course** (24) |
| **nayald** | — | B | (v.) destroy | *na-* + S *gald*, "un-build" | NOT + **HALD+course** (24) |
| **clenn** | — | S | (adj.) new; (v.) make new, mend | *ul glennol* "being mended" | **VENN+turn** (266) |
| **stann** | — | B | (v.) quarry, cut stone from the bed | *Stannard*, the quarryman | **TOLM+wedge** (7) |
| **stannow** | — | B | a quarry | place *-ow* | **TOLM+wedge** (7) **o w** |
| **bresk** | *breskis* | S | a chisel |  | **GARL+cut** (219) |
| **drunn** | *drunnos* | B | a mallet, a hammer | *drunnard* a smith; *drunnow* a smithy, a forge | **GARL+wedge** (218) |
| **gann** | *gannos* | B | a post, an upright |  | **GANNA+lone** (285) |
| **ganna** | *gannā* | B | a gate | an old dual, "the two posts". *ganna ulvenn* is the inner gate | **GANNA** (284) |
| **hosk** | *hoskos* | B | a lintel; a capstone; (v.) lay the lintel, seal | *hoskol* the sealing; *et Hosk* the Title | **TOLM+cope** (2) |
| **gorn** | — | B | a corner, a quoin |  | **TOLM+turn** (6) |
| **gorndholm** | — | B | a cornerstone | *gorn* + S *tolm* | **TOLM+turn** (6) + **TOLM** (1) |
| **trenndholm** | — | B | the tale-stone | *trenn* + S *tolm*: "the course-stone" | **TRENN** (39) + **TOLM** (1) |
| **kethow** | *kethū* | B | a keep, a hold | "holding-place", from *keth* | **GARL+cup** (214) **o w** |
| **tresk** | *treskis* | S | a cleft, a split; (v.) cleave, rive, tear | *treskat* riven, torn | **CRESK+gap** (74) |
| **lest** | *lestis* | S | a house | *lest Vardh* a temple | **HALD+door** (22) |
| **taldow** | *taldū* | B | a tower, a high place | from *tald*, rise | **HALD+rim** (26) |
| **cumm** | *cummos* | B | a haven: any walled place of shelter | "not always a harbour for ships" | **HALD+still** (25) |
| **halflenn** | — | S | slate | "rock-leaf" | letters |
| **stell** | *stellis* | S | a cairn |  | **TOLM+three** (5) |
| **pell** | *pellis* | S | a spire, a tall point | in *Pellow* | **TOLM+lone** (4) |
| **ryt** | *wrytis* | S | a cut vow, an oath; an inscription; (v.) cut letters, write, swear | *Rytom um …* "I swear upon …" | **TOLM+cut** (8) |
| **Stonwryt** | *stonwryta* | S | the vow cut under a great work; the Stonwryt coin; trust | "the standing cutting"; said /ˈstonryt/ | **TOLM+still** (11) + **TOLM+cut** (8) (a vow itself is cut whole: D9) |

### 5.2 The guild, the faith, the bond

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **Stonwrytan** | — | B | the guild; the Stonewrights | collective *-an*, "those of the Stonwryt". Vocative in the Cry | **TOLM+still** (11) + **TOLM+cut** (8) **a n** |
| **stonwrytel** | — | S | one Stonewright | singulative *-el* | **TOLM+still** (11) + **TOLM+cut** (8) **e l** |
| **prass** | *prassos* | B | a master of the craft |  | **GARL+cope** (221) |
| **prassel** | — | S | a prentice | "little master" | **GARL+cope** (221) **e l** |
| **Hemm · Hemma** | *hemmos · hemmā* | S · B | Elder · Elderess | "old one"; one rank. Was *Mell*: Sindarin *mell* is "dear", the root of *mellon* (originality pass) | **ULD+notch** (240) · **ULD+notch** (240) **a** |
| **Mardh** | *Mardhos* | B | God | Used of nothing else. It softens in construct (*lest Vardh*) and is never the butt of a jest | **LUMM+cope** (251) |
| **vennoth** | — | B | faith; truth; faithfulness | *venn* + *-Oth* | **VENN** (264) **O th** |
| **ammel** | — | S | (v.) pray |  | **LUMM+zig** (252) |
| **Lodh Helv** | — | S | the Aetherbond | "the mortar of the sky" | **LODH** (291) **ORL+cope** (141) |
| **et Lodhan** | — | B | the Bonded | "those of the mortar" | **LODH** (291) **a n** (the article left out) |
| **lodhat** | — | B | bonded | "mortared" | **LODH** (291) **A t** |
| **nalodhat** | — | B | unbonded |  | NOT + **LODH** (291) **A t** |
| **sullast** | — | B | a third; the unbonded third of a hearth | ordinal of *sull* (three) | numeral letters |
| **veskerd** | — | S | a seer | "one who reads" the cradles | **VESK** (229) **A r d** |
| **tevow** | *tevū* | B | a cradle | "child-place" | **ULD+bough** (239) **o w** |
| **hoskol** | — | B | the sealing (the wedding) | "the laying of the lintel" | **TOLM+cope** (2) **O l** |
| **hoskvoll** | — | B | a pair-name | "lintel-name" | **TOLM+cope** (2) + **BROD+lone** (202) |
| **voll** | *vollos* | B | a name |  | **BROD+lone** (202) |
| **Tolm Vardh** | — | B | a Theolith | "stone of God"; pl. *Tolmath Vardh* | **TOLM** (1) **LUMM+cope** (251) |
| **Ryt Dhunnoth** | — | B | the Covenant of Completion | "the vow of wholeness"; its words are withheld | letters, whole (a vow: D9) |
| **tunn** | — | B | whole, complete | *tunnoth* wholeness | **VENN+cope** (265) |
| **grest** | *grestos* | S | harm, hurt | *Grest um hos, grest um vana* | **CRESK+drop** (75) |
| **pana** | *panā* | B | both | "the two"; S *vana* | letters (p a n a) |
| **par** | — | B | (v.) guard, protect; (n.) a watch |  | **PAR** (92) |
| **pard** | *pardos* | B | a warden, a keeper | S *vard*: *Halvard*, *Lurrvard* | **PAR** (92) **d** |

### 5.3 Hearth, family, people

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **odh** | *odhos* | B | a hearth | *Odh Sell*, the Long Hearth | **ODH** (57) |
| **theld** | *theldis* | S | a family, a household | "hearth-kin"; pl. *theldeth* | **ODH+drop** (59) |
| **varn** | *varnos* | B | home |  | **ODH+still** (58) |
| **tev** | *tevis* | S | a child | pl. *tevath* (irregular, from old *tevāthi*) | **ULD+bough** (239) |
| **gedh** | *gedhis* | S | a father |  | **ULD+course** (238) |
| **odha** | *odhā* | B | a mother | "she of the hearth" | **ODH** (57) **a** |
| **uld** | *uldos* | B | a man; a grown person |  | **ULD** (237) |
| **essa** | *essā* | B | a woman |  | letters |
| **lunt** | *luntos* | B | a people, a nation |  | **ULD+three** (241) |
| **Orrow** | *orrū* | B | the Shore; the Shorelands |  | **WADH+rim** (310) |
| **Orrowan** | — | B | the Shorelanders |  | **WADH+rim** (310) **a n** |
| **Orrowen** | — | S | the Shoreland tongue | "of the Shore" | **WADH+rim** (310) **e n** |
| **brodhen** | — | S | a speech, a tongue | from *brod* word | **BROD+course** (198) **e n** |
| **Treskan** | — | B | the Rivenmen | "the cleft-folk" | **CRESK+gap** (74) **a n** |
| **arra** | *arrā* | B | a guest |  | **ODH+door** (60) |
| **gebb** | *gebbis* | S | a door |  | **HALD+gap** (23) |
| **lumm** | — | B | (v.) kneel |  | **LUMM** (250) |
| **vall** | — | B | (v.) love |  | **MOLT+turn** (108) |
| **osk** | — | B | (v.) trust; (n.) trust |  | **PAR+still** (94) |
| **tesk** | *teskis* | S | a generation | *delv tesk* twelve generations | **TRENN+drop** (45) |
| **Seren** (a cradle-name) | ***SEREŊOS*** | S | ***a single sorrow that overcomes*** (Jack's note 6) | First Tongue \**Swe-reŋ-o-s*: \**swe-* single, one's own (as in *sost*) + \**reŋ-* a sorrow that is carried and does not break the one who carries it (left nowhere else; it would be living *ren*) + the nominative (§4.6). Her meaning is Jack's own; the names given none keep none (§4.6) | letters, as every name: **s e r e n**; in the Hal **S E R E ŋ O S** |

### 5.4 The wall, the war, the Captain

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **Crenn** | *crennos* | S | a captain; *the* Captain | S *Hrenn*, N *Grenn* | **PAR+cope** (93) |
| **Ketherd** | — | S | the Commander | "the holder", from *keth*: the Rite's name for him | **GARL+cup** (214) **A r d** |
| **vennuld** | — | B | a True Man | *venn* + S *uld*; *et Delv*, the Twelve | **VENN** (264) + **ULD** (237) |
| **hesperd** | — | S | a soldier | "sword-one" | **CRESK+cut** (81) **A r d** |
| **hesp** | *hespis* | S | a sword |  | **CRESK+cut** (81) |
| **kest** | *kestis* | S | a company of soldiers |  | **CRESK+three** (82) |
| **bramm** | *brammos* | B | a gun |  | **CRESK+star** (79) |
| **bramman** | — | B | a battery | "the guns of one True Man" | **CRESK+star** (79) **a n** |
| **haskard** | — | B | a runner | from *hask* run | **TRENN+wedge** (42) **A r d** |
| **hask** | — | B | (v.) run |  | **TRENN+wedge** (42) |
| **gomm** | *gommos* | B | a horn |  | **BROD+star** (205) |
| **carm** | — | B | (n.) a call, a cry; (v.) cry out, call | *sull carm* the three calls | **BROD+wedge** (199) |
| **pedh** | *pedhis* | S | a shot: what a gun throws | S *vedh* | **CRESK+lone** (80) |
| **trun** | *trunos* | B | ground; (on the wall) the water a battery watches | S *dhrun* | **LODH+still** (293) |
| **marr** | — | B | (v.) shift, move to another place | *Marr tho dhrun* | **KYL+course** (279) |
| **kyl** | — | S | (v.) change |  | **KYL** (278) |
| **keth** | — | S | (v.) hold, keep; (of the wood) know | VN *kethyl* | **GARL+cup** (214) |
| **lusk** | — | B | (v.) loose, let go, set free |  | **GARL+gap** (216) |
| **bosk** | — | B | (v.) attack | N *mosk* | **CRESK+course** (78) |
| **hurr** | — | B | (v.) kill | VN *hurrol* | **CRESK+fade** (77) |
| **gorr** | — | B | (v.) fight |  | **CRESK+wedge** (76) |
| **covv** | *covvos* | B | a cloak | *Covv Treskat*, the Torn Cloak | **ULD+cope** (242) |
| **Hosk Lunn** | — | B | the Title of Liberty | "the lintel of freedom" | **TOLM+cope** (2) **LUNN** (258) |
| **sceth** | *scethis* | S | a ship, a hull |  | **SCETH** (173) |
| **scethan** | — | B | a fleet | collective; one hull of it is *scethel* | **SCETH** (173) **a n** |
| **wemm** | *wemmis* | S | a sail | *wemmeth myst* the grey sails | **SCETH+zig** (174) |

### 5.5 Sea, land, weather, the grey

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **wadh** | *wadhos* | B | the sea |  | **WADH** (301) |
| **myst** | *mystis* | S | sea-fog; the grey; (adj.) grey | the Shoreland half of *Mystaeri* | **WADH+fade** (302) |
| **Mystow** | — | B | the Mystlands | Jack's word, with its original | **WADH+fade** (302) **o w** |
| **Mystaeri** | — | S | the Mystaeri | hybrid exonym (§4.7) | **WADH+fade** (302) **a e r i** |
| **Mesk Myst · Tolm Myst** | — | S | Mystwood · Myststone | "wood / stone of the grey" | **MESK** (186) **WADH+fade** (302) · **TOLM** (1) **WADH+fade** (302) |
| **Gannath Myst · Crenn Myst** | — | S | the Mystholders · a Mystarch | "posts of the grey · captain of the grey" | **GANNA+lone** (285) **A th** **WADH+fade** (302) · **PAR+cope** (93) **WADH+fade** (302) |
| **mesk** | *meskis* | S | a tree; wood |  | **MESK** (186) |
| **lurr** | *lurros* | B | a forest | *lurrel* green | **MESK+three** (187) |
| **helv** | *helvis* | S | the sky, the upper air | the Guest's second word | **ORL+cope** (141) |
| **hyll** | *hyllis* | S | a tide |  | **WADH+turn** (303) |
| **rhull** | *hrullos* | B | a river |  | **WADH+course** (304) |
| **sedh** | *sedhis* | S | a fen |  | **WADH+still** (305) |
| **nell** | *nellis* | S | an islet |  | **WADH+lone** (306) |
| **tavow** | *tavū* | B | a harbour, a landing | from *tav*, come ashore | **SCETH+turn** (175) **o w** |
| **tav** | — | B | (v.) come ashore, land a boat |  | **SCETH+turn** (175) |
| **sorth** | *sorthos* | B | a ridge |  | **BRUNN+rim** (319) |
| **brunn** | *brunnos* | B | a mountain |  | **BRUNN** (318) |
| **grull** | *grullos* | B | sand |  | **WADH+three** (309) |
| **sirr** | *sirris* | S | glass |  | **TOLM+star** (9) |
| **crest** | *crestis* | S | ice |  | **WADH+cope** (308) |
| **frenn** | *hwrennos* | S | frost, rime | Hal *hw* > *f* | **WADH+pale** (307) |
| **sulv** | *sulvos* | B | snow; (adj.) white |  | **BRUNN+pale** (320) |
| **grem** | *gremis* | S | winter |  | **ORL+pale** (140) |
| **vorr** | *vorros* | B | fire |  | **VORR** (153) |
| **orl** | *orlos* | B | a day |  | **ORL** (136) |
| **vess** | *vessis* | S | a night |  | **ORL+fade** (137) |
| **clem** | *clemis* | S | an hour | *pa relv clem* four-and-twenty hours ("two-twelve hour") | **ORL+notch** (138) |
| **surr** | *surros* | B | a year |  | **ORL+turn** (139) |
| **cemm** | — | S | (v.) meet; (n.) a meeting | *Cemm Hyll*, Tidesmeet | **TRENN+door** (49) |

### 5.6 Body, life, feeling

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **garl** | *garlos* | B | a hand; a hand of writing | *Garl Dhrenn*; dual *pa yarl* | **GARL** (213) |
| **molt** | *moltos* | B | a heart |  | **MOLT** (105) |
| **hoss** | *hossos* | B | breath |  | **MOLT+zig** (106) |
| **lorr** | *lorros* | B | blood; (adj.) crimson | the colour of the cloak and the pennants | **LORR** (130) |
| **senn** | — | S | (v.) die: go out, as a fire in peace | VN *sennyl* dying, death: the Guest's third word | **VORR+fade** (154) |
| **hess** | — | S | (v.) stop | the Guest's first word | **TOVV+cope** (165) |
| **lomm** | *lommos* | B | grief | *Doss lomm umom* "I grieve" | **MOLT+fade** (107) |
| **sollan** | *sollanos* | B | peace | "the rest after the work", from *sol* | **GARL+still** (217) |
| **sol** | — | B | (v.) rest, lie still |  | letters |
| **lunn** | *lunnos* | B | freedom | pl. *lunnath* | **LUNN** (258) |

### 5.7 Speech, writing, memory

| Orrowen | Hal | cl. | sense | note | dry cut |
|---|---|---|---|---|---|
| **tum** | — | B | (v.) remember | ***Tumar.*** "We remember." | **TUM** (120) |
| **tumol** | *tumola* | B | remembering; memory | N *dumol* in the Title | **TUM** (120) **O l** |
| **nadhum** | — | B | (v.) forget | "un-remember" | NOT + **TUM** (120) |
| **brod** | *brodos* | B | a word |  | **BROD** (197) |
| **brodh** | — | B | (v.) put into words, tell, speak | *brodhat* told; ***nawrodhat*** untold | **BROD+course** (198) |
| **vesk** | — | S | (v.) see; read (letters, or a cradle) | Seren "read it with my eyes" | **VESK** (229) |
| **flenn** | *hwlennā* | S | a leaf of a book or of slate; a sheet |  | **TRENN+three** (48) |
| **flennath** | — | S | the Book | "the leaves" | **TRENN+three** (48) **a th** (irregular) |
| **luth** | *luthos* | B | ink | *Seren Pa Luth*, Seren Two-Inks | **TRENN+fade** (47) |
| **brenth** | *brenthis* | S | coal | the Captain's hand is *garl brenth* | **VORR+still** (155) |
| **vell** | *vellis* | S | a song |  | **TRENN+zig** (46) |
| **sesk** | — | S | (v.) know a fact | the wood is not *sesk*'d but *keth*'d | **TUM+cope** (121) |
| **ammad** | — | B | (v.) teach | the Theoliths' work | **BROD+three** (203) |
| **nydh** | — | S | (v.) count | *nydherd* a counter: *Kael Nydherd* | **GARL+notch** (220) |
| **kael** | *kēlos* | S | a tally-notch | the sense of Kael's name | letters |
| **pess** | — | S | (v.) ask | *Voss sa re vess*, Voss who asked | **BROD+gap** (200) |
| **tess** | — | S | (v.) answer; stand surety for | *es dess et odh* "the hearth will answer" | **BROD+turn** (201) |

### 5.8 Other verbs

| Orrowen | cl. | sense | note | dry cut |
|---|---|---|---|---|
| **doss** | B | be (state, place) | irregular; past *re yal-* (§3.4) | left out (D2) |
| **el** · **ew** · **nel** · **new** | S | is · was · is not · was not (the copula) |  | left out; *nel*, *new* as the turned stone |
| **tald** | B | rise, stand up | imperative plural ***Talda!*** | **TOLM+rim** (3) |
| **orr** | B | go, walk |  | **TRENN+course** (40) |
| **darr** | B | come | was *tol*, which is Sindarin *tol-* "to come" (Quenya *tul-*): the same word (originality pass) | **TRENN+turn** (41) |
| **hunn** | B | hear |  | **BROD+cup** (204) |
| **hebb** | S | give |  | **GARL+course** (215) |
| **tovv** | B | wait |  | **TOVV** (164) |
| **omm** | B | fall |  | **KYL+rim** (280) |
| **cresk** | S | break |  | **CRESK** (73) |
| **ser** | S | go on, carry forward | heard in *Seren* (a folk etymology) | letters |
| **rhyn** | S | set fast (of mortar), take hold | in *Rhyna* | **LODH+cope** (292) |

### 5.9 Qualities

| Orrowen | cl. | sense | note | dry cut |
|---|---|---|---|---|
| **hemm** | S | old | *Tavow Hemm*, Eldhythe. Was *mell* (originality pass) | **ULD+notch** (240) |
| **tevel** | S | young |  | **ULD+bough** (239) **e l** |
| **strom** | B | great |  | **VENN+rim** (269) |
| **lyss** | S | small |  | **VENN+lone** (270) |
| **gell** | S | good |  | **VENN+still** (267) |
| **venn** | S | true; plumb; faithful | a true wall is plumb | **VENN** (264) |
| **gunn** | B | deep; (n.) the deep | *et gunn sy* this deep | **LODH+fade** (294) |
| **sell** | S | long |  | **VENN+course** (268) |
| **domm** | B | black |  | **TOLM+fade** (13) |
| **lurrel** | S | green | "forest-coloured" | **MESK+three** (187) **e l** |
| **bell** | S | gold, golden |  | **ORL+drop** (142) |
| **lenn** | S | silver |  | **TOLM+pale** (10) |
| **ulvenn** | S | inner |  | **VENN+cup** (271) |
| **treskat** | B | riven, torn |  | **CRESK+gap** (74) **A t** (wf6 §11b: *tresket* by the rule) |

### 5.10 Small words

| Orrowen | mutation after | sense | dry cut |
|---|---|---|---|
| **et** | none | the (the article; never mutates) | left out |
| **ul** | N | in | left out |
| **hy** | S | from, out of | left out |
| **um** | S | upon, on | left out |
| **lo** | S | at, by, with (having, being able) | left out |
| **dem** | N | until, as far as | left out |
| **eth** | none | and | left out; the wedge |
| **ell** | none | or | left out; the wedge |
| **veth** | none | but, rather | left out; the wedge |
| **nath** | N | not (before a verb) | **the turned stone** |
| **na-** | S | un- (prefix) | **the turned stone** |
| **re** | S | past particle | left out (stone has no tense) |
| **es** | N | future particle | left out (stone has no tense) |
| **ho** | S | question particle | left out (stone does not ask) |
| **sa** | S | who, which, that (relative) | left out |
| **somm** | none | while, as long as | **TOVV+still** (167) |
| **amm** | none | when (conjunction) | **TOVV+notch** (168) |
| **cedh · vodh** | none | who? · what? | left out |
| **sy · ull** | none | this · that (after the noun) | left out |
| **gor** | S | every, all | left out |
| **sost** | none | self, very: *et dask sost* "the very end" | left out |
| **tul** | none | yet, still; *nath … tul* is "not yet" (§3.8), never "no longer" | **TOVV+course** (166) |
| **dask** | — | (n.) the end (a noun, listed here for the Cry) | **TRENN+cope** (44) |
| **en · tho · o · ey · olna · ol · va · sona · so** | see §3.5 | I/my · you/your · he, it/his, its · she/her · we two · we/our · you (pl) · they two · they/their | left out |

### 5.11 Numbers

Speech counts in **twenties**. The guild also counts in **twelves** ("twelvefold, as the old masters counted it"). A numeral stands before a singular noun, and *pa* (two) softens it.

|  | Orrowen |  | Orrowen | dry cut |
|---|---|---|---|---|
| 1 | **hos** | 11 | **hosnoth** (one-ten) | numeral letters, capped |
| 2 | **pa** (+S) | **12** | **delv**: "a course", the guild's twelve. ***et Delv***, the Twelve | numeral letters, capped |
| 3 | **sull** | 13 | **sullnoth** | numeral letters, capped |
| 4 | **gemm** | 20 | **murr** | numeral letters, capped |
| 5 | **lesk** | 24 | ***pa relv*** "two twelves" (guild), or *gemm eth murr* (speech) | numeral letters, capped |
| 6 | **vran** | 40 | ***pa vurr*** "two twenties" | numeral letters, capped |
| 7 | **dhom** | 100 | ***lesk murr*** "five twenties" | numeral letters, capped |
| 8 | **thell** | 400 | **bost** "a score of scores"; 2,000 is *lesk bost* | numeral letters, capped |
| 9 | **rost** | first · second · third | **hosast · pawast · sullast** | numeral letters, capped |
| 10 | **noth** | twelvefold | **delvoth** | numeral letters, capped |

### 5.12 Affixes

| Affix | Meaning | Example | dry cut |
|---|---|---|---|
| **-Ath** | plural | *tolmath, theldeth* | letters, after the sign (D5) |
| **-Ol** | verbal noun | *tumol, kethyl* | letters, after the sign (D5) |
| **-At** | participle (done, made) | *cadhat, treskat, brodhat* | letters, after the sign (D5) |
| **-Ard** | agent, one who does | *Stannard, haskard, Ketherd* | letters, after the sign (D5) |
| **-Oth** | abstract quality | *vennoth, tunnoth* | letters, after the sign (D5) |
| **-el** | singulative; "little, dear" (names) | *stonwrytel, prassel, Tarnel* | letters, after the sign (D5) |
| **-an** | "the folk of", a collective | *Stonwrytan, Treskan, Orrowan, Lodhan* | letters, after the sign (D5) |
| **-en** | "of, belonging to"; an old name-ending | *Orrowen, Seren* | letters, after the sign (D5) |
| **-ow** | place of | *kethow, stannow, tevow, Mystow* | letters, after the sign (D5) |
| **-Ast** | ordinal | *sullast* | letters, after the sign (D5) |
| **-a** | the old dual; feminine names; the pair-name lintel | *ganna, pana, Rhyna, Halyna* | letters, after the sign (D5) |
| **na-** (+S) | un-, not | *nawrodhat, nadhum, nalodhat* | the turned stone |
| **-na** | dual of a pronoun | *olna, sona* | letters, after the sign (D5) |


---

## 6 · THE COURSE-HAND LETTERS (*GARL DHRENN*)

*The letters, their bites, their table, the punctuation, lintels, numerals and the Hal hand, carried over from the wf6 spec. They are unchanged: the dry cut uses them for names, rare words and complements, a vow is cut in them whole, and the leaf-hand is them, written (§8). wf6 called a word with its own bed a "word-stone"; here it is simply **a stone**, and the new logograms are **word-signs**, to keep the two apart. §6.10 is rewritten.*

An alphabet of straight chisel-strokes that stand on a mortar line. It records sound: the stone half of craft's thesis, "stone writes what is said; wood writes what is meant."

### 6.1 The picture in one paragraph

Every letter stands on the **mortar line** (*lodh*), as a stone stands on its bed.
- **Consonants are ashlars** (*tolmath*): tall, joined, cut whole. Each has an **upright** rising from the bed and one or more **laid stones** running to its right.
  - The upright tells *where* the sound is made. It is one of three: the forward-leaning **prop** (lips), the stepped **offset** (tongue-tip), or the back-leaning **shore** (the back of the mouth).
  - The laid stones tell *how* the sound is made.
- **Vowels are pinnings**: small, loose stones set between the ashlars, low on the bed, their parts not touching.
- **A mutation is a bite cut into the mortar** under a letter's foot. The letter itself stays whole, so the dictionary form can always be seen.
- **Each word is a stone with its own bed.** Words are parted by a **head-joint**, and successive lines **break the joint** as a mason staggers courses.
- **A pair-name carries a sealing lintel** laid across it.

### 6.2 Direction, units and the cell

**Direction.** The living hand runs left to right, and lines run top to bottom. The Hal runs right to left (§6.9).

**Units.** 1 u is the base unit. The coordinates have their origin at the letter's left foot on the bed, with **y up**; SVG flips this at draw time.

| Measure | Value |
|---|---|
| **consonant cell** | 4 u wide × 3 u tall |
| **vowel cell** | 2.2 u wide × 2 u tall |
| **letter gap** (inside a word) | 0.55 u |
| **head-joint** (between words) | 2.2 u |
| **bed band** | y ∈ [−0.22, 0]: one band per word, running from 0.3 u before the first letter to the end of the last letter's cell |
| **line pitch** (bed to bed) | 5.2 u |
| **headroom** | 1.2 u above the cell, for lintels and numeral caps at y = 3.75 |
| **minimum joint** | 0.45 u between two strokes of one letter that are not joined |
| **stroke half-width** | 0.19 u (cut form) |

Rendered at 340 px across a phone, a 16-letter line gives about 4.6 px per unit. The smallest mark (a pin, 1.3 u) is then about 6 px tall, which is craft's minimum.

### 6.3 From the tongue to the letters

The course-hand writes the **underlying form**, not the Book's romanisation:
- each base consonant is one letter, with its mutation as a bite;
- each root vowel is a full vowel letter;
- each suffix vowel is a harmonic letter.

| Sound or spelling | Letter(s) |
|---|---|
| *p b m f v w t d n th dh s l r rh k g h* | one letter each (*th, dh, rh* are single letters) |
| *c* and *k* | the one letter **k** (the c/k split is only a Book spelling rule) |
| a softened or nasalised consonant | its **base letter + a bite** (§6.5). *dumol* is written **t**+N · u · m · O · l |
| *y* /j/ (softened *g*) | **g** + S bite |
| *a o u e i y* in a root | the full vowel letter |
| *A*, *O* in a suffix (the harmonic vowels, §3.2) | the harmonic letters **A**, **O** |
| *ae* | **a e** (two pinnings) |
| *ow* | **o w** |
| a doubled consonant | the letter twice (*nn* = n n) |
| a vowel-initial nasalised word (*m-*, *n-*) | an N bite under the first vowel |

This is why the romanisation cannot be turned back into the hand without the lexicon: the Book writes *dumol*, and only the grammar knows it is *tumol* with a nasal bite. Going the other way always works, because the hand shows every base and every mutation.

### 6.4 How a letter is built

**The three uprights (place).** Each is a polyline in cell units, with its foot on the bed.

| Upright | Place | Polyline | Attach x at height y |
|---|---|---|---|
| **prop** | lips (p b m f v w) | (0,0) → (1.2,3), leaning forward | x = 0.4·y |
| **offset** | tongue-tip (t d n th dh s l r rh) | (0,0) → (0,1.5) → (0.9,1.5) → (0.9,3), a stepped wall | x = 0 if y < 1.5; x = 0.9 if y ≥ 1.5 |
| **shore** | back (k g h) | (1.2,0) → (0,3), leaning back | x = 1.2 − 0.4·y |

**The laid stones (manner).**
- Laid stones lie at three heights: top (y = 3), middle (2) and low (1).
- A **joined** stone starts on the upright at its attach point.
- A **free** stone stands apart and does not touch the upright.
- The **pin** is a short second upright: a bedded stroke (3.6,0) → (3.6,1.3).

| Manner | Laid stones | Letters |
|---|---|---|
| **stop** | top, joined, to x = 4 | p · t · k |
| **voiced stop** | top, joined, to 4 + **pin** | b · d · g |
| **nasal** | middle, joined, to 4 | m · n (and Hal ŋ) |
| **fricative** | low, joined, to 4 | f · th · h |
| **voiced fricative** | top, joined, to 2.4 + low, joined, to 4 | v · dh |
| **approximant** | top, joined, to 2.4 + low, **free**, 2.9 → 4 | w · l (and Hal *x*) |
| **sibilant** | top, **free**, 2.9 → 4 + low, joined, to 2.4 | s (and Hal *hw*) |
| **rhotic** | middle, joined, to 2.6 + **pin** | r |
| **rough rhotic** | middle, joined, to 4 + **pin** + top, **free**, 2.9 → 4 | rh |

The families answer the mutations:
- *p b m* share the prop, and the soft forms they wear to, *v w*, share it too.
- *t d n th dh* share the offset.
- *k g h* share the shore.

**Both mutations keep a sound on its own upright**, with two exceptions, and history explains both:
- softened *rh* became *h*, a bare breath (offset to shore);
- nasalised *g* was once /ŋ/, the shore-nasal the Hal still writes, before /ŋ/ merged into *n*.

So the living hand's one empty slot, the shore nasal, is the gap the merger left.

**Vowels (pinnings).** Two or three loose parts that never touch. The broad vowels carry a **capstone** (a laid stone at y = 2) over short pins. The slender vowels carry a tall pin with a low laid stone beside it. *y* is the exception: it is **the leaning pin**, *e*'s tall pin riven from its bed and leaning over its low stone, as the riven ridge leans over the Keep. (Until the originality pass *y* was "the cleft", two strokes whose tops almost met: a Greek Λ, and the Cirth vowel *o*.)

| | Shape | Reads as |
|---|---|---|
| **a** | short pin left, capstone | broad |
| **o** | short pin right, capstone | broad |
| **u** | both short pins, and a short capstone raised between them (the keystone) | broad |
| **e** | tall pin left, low stone right | slender |
| **i** | tall pin right, low stone left | slender |
| **y** | the leaning pin: a tall pin leaning forward, low stone right | slender |
| **A** (harmonic) | as *a*, capstone **broken** in two | *a* in a broad word, *e* in a slender one |
| **O** (harmonic) | as *o*, capstone **broken** in two | *o* in a broad word, *y* in a slender one |

**The harmony mark: once per word.** A harmonic letter has no value of its own. It takes the class of the **nearest full vowel before it** in the same stone. So a word's class is written once, by its stem, and every ending follows. *Theldeth* and *lunnath* end in the same two letters, **A th**, read *-eth* after *e* and *-ath* after *u*. The Title teaches this lesson in its fourth and eighth words.

The derivation of every letter and vowel from the First Tongue's marks (the reform, C6) is `ancestor.md` §5.4.

### 6.5 The bites (mutation marks)

A bite is a notch cut down through the bed band, under the letter's **foot**.

| Bite | Shape (cell units) | Meaning |
|---|---|---|
| **softening** | a V: (fx − 0.45, 0) · (fx, −0.7) · (fx + 0.45, 0) | S |
| **nasalising** | a square: (fx − 0.38, 0) to (fx + 0.38, −0.7) | N |

**The foot, fx, of each letter:**

| Letters | fx |
|---|---|
| prop letters | 0 |
| offset letters | 0 |
| shore letters | 1.2 |
| *a, u, e, A* | 0.25 |
| *o, i, O* | 1.95 |
| *y* | 0.25 (the foot of the leaning pin) |

- **Where a bite goes.** A bite goes under the **first letter of a word**, or under the first letter of a root after the prefix *na-*.
  - A bite is written only where the mutation **changes the sound**: *es ston* has no bite.
  - **Lexicalised compounds and names are spelled as said, with no bite.** These include *Halvard, Lurrvard, gorndholm, vennuld*, and pair-names in running text. The bite marks grammar, not etymology. The Stonwryt ligature is the one place the base forms of a name are shown (§6.8).
- An N bite under a vowel reads *m-* before a broad vowel and *n-* before a slender one.
- **A softened *rh* or *g* that falls silent** (§3.3) still gets its letter and its bite. The hand never drops a letter the tongue has dropped, just as it keeps the *w* of *Stonwryt*.

The dry cut writes no bites (D6); the leaf-hand writes them as small marks under the line (§8.6).

### 6.6 The glyph table

Strokes are polylines in cell units, as `[[x,y],[x,y],…]`. The first stroke of every consonant is its upright.

```json
{
  "metrics": {"cons_cell": [4, 3], "vowel_cell": [2.2, 2], "letter_gap": 0.55,
              "head_joint": 2.2, "bed_band": [-0.22, 0], "line_pitch": 5.2,
              "min_joint": 0.45, "half_width_cut": 0.19, "taper": 0.4},
  "uprights": {"prop": [[0, 0], [1.2, 3]], "offset": [[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], "shore": [[1.2, 0], [0, 3]]},
  "pin": [[3.6, 0], [3.6, 1.3]],
  "foot_x": {"prop": 0, "offset": 0, "shore": 1.2, "a": 0.25, "u": 0.25, "e": 0.25, "A": 0.25, "o": 1.95, "i": 1.95, "O": 1.95, "y": 0.25},
  "consonants": {
    "p": {"place": "prop", "manner": "stop", "strokes": [[[0, 0], [1.2, 3]], [[1.2, 3], [4, 3]]]},
    "b": {"place": "prop", "manner": "vstop", "strokes": [[[0, 0], [1.2, 3]], [[1.2, 3], [4, 3]], [[3.6, 0], [3.6, 1.3]]]},
    "m": {"place": "prop", "manner": "nasal", "strokes": [[[0, 0], [1.2, 3]], [[0.8, 2], [4, 2]]]},
    "f": {"place": "prop", "manner": "fric", "strokes": [[[0, 0], [1.2, 3]], [[0.4, 1], [4, 1]]]},
    "v": {"place": "prop", "manner": "vfric", "strokes": [[[0, 0], [1.2, 3]], [[1.2, 3], [2.4, 3]], [[0.4, 1], [4, 1]]]},
    "w": {"place": "prop", "manner": "approx", "strokes": [[[0, 0], [1.2, 3]], [[1.2, 3], [2.4, 3]], [[2.9, 1], [4, 1]]]},
    "t": {"place": "offset", "manner": "stop", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 3], [4, 3]]]},
    "d": {"place": "offset", "manner": "vstop", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 3], [4, 3]], [[3.6, 0], [3.6, 1.3]]]},
    "n": {"place": "offset", "manner": "nasal", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 2], [4, 2]]]},
    "th": {"place": "offset", "manner": "fric", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0, 1], [4, 1]]]},
    "dh": {"place": "offset", "manner": "vfric", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 3], [2.4, 3]], [[0, 1], [4, 1]]]},
    "s": {"place": "offset", "manner": "sib", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[2.9, 3], [4, 3]], [[0, 1], [2.4, 1]]]},
    "l": {"place": "offset", "manner": "approx", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 3], [2.4, 3]], [[2.9, 1], [4, 1]]]},
    "r": {"place": "offset", "manner": "rhot", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 2], [2.6, 2]], [[3.6, 0], [3.6, 1.3]]]},
    "rh": {"place": "offset", "manner": "rrhot", "strokes": [[[0, 0], [0, 1.5], [0.9, 1.5], [0.9, 3]], [[0.9, 2], [4, 2]], [[3.6, 0], [3.6, 1.3]], [[2.9, 3], [4, 3]]]},
    "k": {"place": "shore", "manner": "stop", "strokes": [[[1.2, 0], [0, 3]], [[0, 3], [4, 3]]]},
    "g": {"place": "shore", "manner": "vstop", "strokes": [[[1.2, 0], [0, 3]], [[0, 3], [4, 3]], [[3.6, 0], [3.6, 1.3]]]},
    "h": {"place": "shore", "manner": "fric", "strokes": [[[1.2, 0], [0, 3]], [[0.8, 1], [4, 1]]]}
  },
  "vowels": {
    "a": {"strokes": [[[0.25, 0], [0.25, 1.25]], [[0, 2], [2.2, 2]]]},
    "o": {"strokes": [[[1.95, 0], [1.95, 1.25]], [[0, 2], [2.2, 2]]]},
    "u": {"strokes": [[[0.25, 0], [0.25, 1.25]], [[1.95, 0], [1.95, 1.25]], [[0.7, 2], [1.5, 2]]]},
    "e": {"strokes": [[[0.25, 0], [0.25, 2]], [[0.75, 1], [2.2, 1]]]},
    "i": {"strokes": [[[1.95, 0], [1.95, 2]], [[0, 1], [1.45, 1]]]},
    "y": {"strokes": [[[0.25, 0], [1.05, 2]], [[1.45, 1], [2.2, 1]]]},
    "A": {"strokes": [[[0.25, 0], [0.25, 1.25]], [[0, 2], [0.85, 2]], [[1.35, 2], [2.2, 2]]]},
    "O": {"strokes": [[[1.95, 0], [1.95, 1.25]], [[0, 2], [0.85, 2]], [[1.35, 2], [2.2, 2]]]}
  },
  "archaic_hal_only": {
    "ŋ": {"place": "shore", "manner": "nasal", "strokes": [[[1.2, 0], [0, 3]], [[0.4, 2], [4, 2]]]},
    "hw": {"place": "prop", "manner": "sib", "strokes": [[[0, 0], [1.2, 3]], [[2.9, 3], [4, 3]], [[0.4, 1], [2.4, 1]]]},
    "x": {"place": "shore", "manner": "approx", "strokes": [[[1.2, 0], [0, 3]], [[0, 3], [2.4, 3]], [[2.9, 1], [4, 1]]]}
  },
  "marks": {
    "perpend": {"width": 0.8, "strokes": [[[0.4, 0], [0.4, 1.6]]]},
    "wedge":   {"width": 1.0, "strokes": [[[0, 1], [1, 1]]]},
    "gate":    {"width": 3.0, "strokes": [[[0.3, 0], [0.3, 2.2]], [[2.7, 0], [2.7, 2.2]], [[0, 3], [3, 3]]]},
    "coping":  {"width": 3.0, "strokes": [[[0.3, 0], [0.3, 2.2]], [[2.7, 0], [2.7, 2.2]], [[0, 3], [3, 3]], [[-0.5, 3.75], [3.5, 3.75]]]},
    "bite_S":  [[-0.45, 0], [0, -0.7], [0.45, 0]],
    "bite_N":  [[-0.38, 0], [-0.38, -0.7], [0.38, -0.7], [0.38, 0]],
    "sealing_lintel": {"y": 3.75, "from": "left edge of the first letter", "to": "right edge of the last letter"},
    "numeral_cap":    {"y": 3.75, "per_letter": [0.2, "cell_width - 0.2"]},
    "long_stone_hal": {"y": 3.25, "over_vowel": [0.3, 1.9]}
  }
}
```

**The end rule, which gives every stroke its "up".** For each stroke end:
1. It is **square** if it lies on the bed (y = 0) or on another stroke of the same letter (a join).
2. Otherwise it **tapers** over 0.4 u, where the chisel lifts.
3. A stroke with no square end at all (a free laid stone, a capstone, a lintel) is **dressed square at both ends**.

The rule is computed, not stored, so the table stays small. The grain's knife-cuts, which taper at both ends, can never be mistaken for it.

### 6.7 Punctuation

All marks are stones set in the line, in their own cells, one letter gap from the word before.

| Mark | Shape | Use |
|---|---|---|
| **perpend** | a short bedded upright, 1.6 u | end of a sentence. The "joint closed" |
| **wedge** | a free laid stone at y = 1 | a pause (comma). In antiphony it is **where the second voice takes the line** |
| **gate** | two posts and a lintel | end of an **oath or vow**. It follows *Ston.* |
| **coping** | the gate with a second, wider stone laid over it | end of a **tale**: "This I lay as it was laid for me." A course is capped |
| (none) | — | questions (the particle *ho* carries them) and cries (the imperative carries them) |

Direct speech is not marked. The Book's quotation marks are Seren's, added in translation.

In the dry cut the gate is also **read**: after a cited vow it says *Ston* (D9).

### 6.8 Stones, lines, lintels, numerals

**Stones.** Each word has its own bed band. At a head-joint the band breaks, so a line looks like a course of stones.
- On cut surfaces, an optional faint **stone outline** may be drawn: a perpend line at each head-joint centre from y = −0.22 to y = 3.8, and a top joint at y = 3.8.
- A word that is too long for its line is **never split**. The line breaks before it.

**Breaking the joint.** For every pair of adjacent lines:
1. If a head-joint centre on the lower line lies within 1.0 u of a head-joint centre on the line above, widen every head-joint on the lower line by 0.25 u.
2. Repeat until no joint is that close, or until the line would overflow the measure.
3. If it would overflow, narrow the joints instead, by 0.2 u steps, down to a floor of 1.4 u.
4. The last line of a paragraph is exempt.

A joint is a word break whatever its width, so reading is untouched. The page looks like a wall.

**The sealing lintel (pair-names).** A pair-name in running text is spelled as it is said (*h a l y n a*), with **one unbroken free laid stone at y = 3.75** over the whole word. That is how a reader knows a pair-name when they see one. It is the gate image of II.3 in the letters.

**The Stonwryt ligature.** Under a capstone, a master-pair's name is cut as a gate:
1. **His post:** the first syllable of his cradle-name, in base letters.
2. A **half head-joint** (1.1 u).
3. **Her post:** her cradle-name stem, in **base letters, with no bite**.
4. **One lintel** over both, on **one shared bed**.

The final *-a* is not cut, because the lintel *is* the *-a*, and the lintel softens the second post. So the Stonwryt of Halyna reads **HAL | RHYN** under one lintel, and the old capstone's reads **ALD | BEN**. A reader who knows the rule says *Halyna* and *Aldwena*. One who does not sees two unknown names.

**Numerals.**
- A number is a run of **numeral letters**, each capped by its own short laid stone at y = 3.75. The caps are broken letter by letter; a sealing lintel is unbroken.
- The numeral letters are the initials of the number words:

  | Letter | h | p | s | g | l | v | dh | th | r | n | d | m | b |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | **Value** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **12** | **20** | **400** |

- Values **add**, except that a unit letter (1–10) standing **directly before d, m or b multiplies it**.

| Number | Written |
|---|---|
| 11 | n h |
| 24 | p d ("two twelves", the guild's way) or m g |
| 40 | p m |
| 2,000 | l b |
| the Twelve | a single capped d |

### 6.9 The first builders' hand (*Garl Hal*)

The same letters, transformed.

| Rule | Detail |
|---|---|
| **1. Mirror** | Every letter is mirrored in its cell: x′ = cell width − x |
| **2. Right to left** | Letters run right to left, facing the way they run. The prop still leans *forward in the direction of writing*, which is leftward. So to a living eye an old *p* has the lean of a living *k*, and an old *a* looks like a living *o* (§6.12) |
| **3. Taller courses** | Consonants are 4 u tall (y × 4/3) and vowels 2.5 u (y × 1.25). Lintels and caps move up to match |
| **4. Scriptio continua** | No head-joints. One unbroken bed runs the whole line |
| **5. No bites** | The old hand writes the base letter where speech already softened it (§4.5) |
| **6. Full endings** | Every Hal ending is spelled out (*TOLMOS, HALDOS*). No harmonic letters: every vowel is full |
| **7. Three archaic letters** | **ŋ** (shore-nasal; merged into *n*), **hw** (merged into *f*), **x** (merged into *h*), from the table above |
| **8. Long vowels** | An old long vowel carries the **long-stone**, a free laid stone at y = 3.25 over it |
| **9. Marks** | Perpend, gate and coping are the same, mirrored. There is no wedge |

The top names on the lintel of the western stair, the slate leaves of the Rite, the mark on the black chest and the old capstone's Stonwryt are all in this hand.

**(v2) The Hal's word-signs.** The Hal cuts the same heads and crowns as the dry cut (§7), under its own rules 1 to 5: mirrored in their cells (x′ = 4.4 − x), cut at 4/3 of their height (a word-sign stands 6.13 u, a letter 4), on the one continuous bed, with no footing (height alone tells a sign from a letter), no complements and no bites. Only names, the words no mark held, and a vow are cut in letters, and the letters carry their full Hal endings (rule 6). §11.7 shows the proverb both ways.

### 6.10 Four ways to make the letters and the signs

| Form | Where it is used | How to draw it |
|---|---|---|
| **The cut** (*garl tolm*): the dry cut, and letters cut whole | capstones, lintels, the tale-stone, works, the coin; the Book "when there is peace enough to cut it"; the Epilogue | V-cut facets (§6.11). The bed band is cut as a shallow channel and the bites go deeper; every word-sign also has its footing (§7.3) |
| **The leaf-hand** (*Garl Flenn*) | Seren's leaves and every scribe's before her; the rolls | **Rewritten in v2 as a joined running hand: §8.** A flat nib 0.30 u at 25°, hairline joins, a slant of 0.18. Halyna's two inks alternate by paragraph; in antiphony the wedge is where the ink changes |
| **The coal hand** (*garl brenth*) | the Title, written by the Captain on the torn cloak and the capstones | Unchanged: blunt strokes 0.5 u wide, square at both ends; each endpoint jittered by up to ±0.12 u and each laid stone tilted by up to ±4°, from a PRNG (mulberry32) seeded by an FNV-1a hash of the text, so the Title is the same drawing for every player; letters at 1.2×; no bed band (cloth has no mortar); bites as short strokes below. **The coal is letters, every word**: the Captain "was no Stonewright" and "wrote, slowly, as a man writes who has not written much" (I.1), so he wrote as he spoke, in the plain letters every child of the Shore learns first, and knew no word-signs |
| **The Hal** (*Garl Hal*) | the first builders' stones | as the cut, mirrored and heightened (§6.9) |

### 6.11 Cut rendering (SVG)

Build each segment of a stroke, from centre-line P to Q with unit normal n, as **two flat facets**:
- facet A = {P, Q′, Q′ + n·w, P + n·w};
- facet B = the mirror on −n;
- w = 0.19 u;
- Q′ is Q, or Q pulled back 0.4 u along the stroke where the end tapers, with the tip closing to the centre line.

**Shading.** Fill the facet whose normal faces the light (from the top left, L = (−0.6, 0.8)) with `--cut-lit`, and the other with `--cut-shade`.
- Overlap joined segments by w so the corners close.
- Square ends on the bed sit **flush with the bed**; they are not extended.

**Theming.** Use no filters and no gradients. Colours come only from CSS tokens (`--cut-lit`, `--cut-shade`, `--bed`, `--bite`), redefined for dark mode. Each letter is a `<symbol>` in `<defs>`, placed with `<use>`. Bites and lintels are drawn inline.

**Budget.** The Title is 43 letters and 5 marks, which is 325 facet polygons: about 27 KB drawn inline, or about 8 KB with each letter as a `<symbol>` reused by `<use>`. A whole leaf of Seren's hand fits well inside the page budget.

### 6.12 Reading it back (the decoder), and the checks to run

**Decoder.** For each stone, read letters left to right (living) or right to left, un-mirroring (Hal).
1. **Classify each letter.**
   - Height 3 or 4 means an ashlar; height 2 or 2.5 means a pinning.
   - An ashlar's first stroke gives the upright: a positive lean is the prop, a step is the offset, a negative lean is the shore (in the Hal, flip the sign).
   - The set of laid stones and pins gives the manner (§6.4).
   - A pinning's parts give the vowel.
2. **Resolve the harmonic letters** from the nearest full vowel before them.
3. **Read any bite under the first letter.** Apply S or N (§3.3) to get the spoken form, and keep the base form for the lexicon.
4. **Read the marks:** perpend is `.`, wedge is `,`, gate is end of oath, coping is end of tale. A sealing lintel means a pair-name. Numeral caps mean the letters are values.
5. **Undo a Stonwryt ligature:** first post + S(second post) + *a*.

**Four look-alikes a decoder must not trip on** (found by the decode test, wf6 §11h; none caused an error, each cost time):
- **A letter's free low stone is not a wedge.** *l* and *w* end in a free stone at y = 1 from x = 2.9 to 4, inside their own cell. A wedge is the same stone in a cell of its own, one letter gap (0.55 u) after the last letter. No letter is an upright with a short top stone and nothing else, so a word that ends *…l* or *…w* never ends in a pause (*sennyl…*, *ell lusk*).
- **A middle stone meets the offset's upper riser partway; a joined top stone leaves from its top corner.** On *n, r, rh* the riser shows above the stone; on *t, d, l, dh* nothing of the riser shows above it. In the coal hand, where jitter moves the stones, read this and not the height.
- **Full *a* against harmonic *A*.** Only the suffixes §3.2 lists are harmonic. The imperative plural *-a* (*Talda*, *Cadha*, *Stona*), the collective *-an* (*Stonwrytan*), the old duals and every pair-name's *-a* are full vowels with an unbroken capstone. The 3du *-A* (*Tuma Halyna*) is broken. The capstone tells an order to many from two who do a thing.
- **The Last Carver's bites** are cut as tapered strokes: his N bite is three short strokes, a cup; an S bite would be two, a V.

**Validation** (run in the scratchpad before any export; craft §6a):
- **Round trip:** encode, draw, then decode each text in §11 and the full lexicon, and require exact equality of the underlying tokens.
- **No two letters share a stroke set within one hand.** This passes for all 26 living letters.
- **Mirror collisions are expected and listed.** Checked by script:
  - No mirrored Hal consonant looks like any living letter, because every mirrored laid stone runs leftward.
  - The mirrored Hal **vowels swap**: an old *a* looks like a living *o*, *e* like *i*, and *A* like *O*; *u* is symmetric. An old *y* mirrors into a shape the living hand does not have (a pin leaning back over a low stone to its left).
  - So a living reader who ignores the direction reads the consonants as nonsense and the vowels wrong. That is the intended misreading. The hand tells him it is the Hal only by its height, its lack of joints and its leftward stones.
- **Minimum joints hold** (0.45 u) in every letter. This passes for the table above (`glyphs.py` check).
- **The coal jitter stays under 0.22 u.**

**(v2) Reading a dry-cut line.** Before step 1, sort each stone's signs: a sign 4.6 u tall on a footing is a **word-sign** (look it up in §7.7 by its head and its crown); a sign 2 u tall standing *before* a word-sign with its one laid stone running left from the head of a pin is the **turned stone** (not); everything else is a letter, read by steps 1 to 5. Letters after a word-sign on its bed are its complement: read the word-sign's word, then add them as its ending, taking **A** and **O** from the word's class. Then lay the mortar back in (§3.11 D2).

### 6.13 The two hands on one surface (the Epilogue)

The Stone out of the Grey is **course-hand letters cut across a petrified round**. The rings of the grain run *under* the bed, and the courses lie straight across them.

It was cut by the Last Carver, who learned the letters only from the Title. That leaves five tells, all true to the rules (the fifth is new in v2):

1. **Every letter in it occurs in the Title.** The one extra word, the article ***et***, is spelled with *e* and *t*, and both are in the Title (*theldeth*, *dumol*).
2. **It has no bed band.** The coal Title he learned from had none, so he never knew letters stand on mortar. Seren, who "knows chisel-work", would see it at once.
3. **Every stroke tapers at both ends**, as a knife-cut in living wood does. He cut stone letters with a carver's hand. The rule that a stroke is squared where it is bedded is the one thing the Title could not teach him.
4. **It stops after *theldeth* with an open joint**: no perpend, no mark, "the chisel's last stroke still sharp at the end of the line".
5. **(v2) He cut the mortar.** Every mortar word of the Title's first line is cut, *ul* and five times *ol*, and one more that the Title never had. No Stonewright cuts a small word in stone, least of all *et*. He cut stone as the Captain wrote on cloth: in letters, every word, as it is said.

He kept the Title's nasal bite under *dumol*, because he copied what he saw. So his error is purely the extra word: *Ul **et** dumol…*, an article on the head of a construct (§3.2). "The right thing, said truly, by one who did not yet know how we say it."


### 6.14 Originality check (craft §8, §9b)

| Risk | Where it would show | Why the course-hand is clear of it |
|---|---|---|
| **Ogham** | strokes on a stem line; vowels as notches; tallies | Letters stand *on one side* of a bed, never across it or either side of it. No letter is a count of parallel strokes. *u*'s two short pins carry a keystone between them, so they read as three stones, not a tally. Bites mark **consonant mutation**, sit *below* the bed and are single, never grouped. No tree names, no *aicmí* |
| **Runes** (Futhark) | angular staves | Horizontals are everywhere, which runes avoid. There are no tall staves with branches. Joined laid stones run only to the right of an upright, never both ways |
| **Cirth** | stem + branches; branch count for voicing; Π and Λ as the vowels *a* and *o* | Voicing is a **separate bedded pin**, not an extra branch. No stems carry side-branches. The old *u* (a detached Π) and *y* (a Λ) matched Cirth's *a* and *o*, both vowels, and were recut in the originality pass |
| **Tengwar** | stem + bow, *tehtar*, series × grade table | No bows or curves. Vowels are full letters, not marks above consonants. It *is* a place × manner featural system, as Tengwar, Cirth and Hangul each are in their own way. But place is shown by the upright's shape and manner by laid stones, which is none of theirs |
| **Latin capitals** | Γ, T, L, E, F, H, Π, Λ | No letter is a Latin capital, upright or italic. The vowels *u* (a detached Π) and *y* (a Λ with its apex open) were the nearest calls, and the originality pass recut them (§6.4). The nearest calls left are the **Hal *k***, which mirrored is a leaning **7** (also Aurebesh *resh*), and the **gate** mark, a Π with its lintel lifted: a door pictograph that both peoples draw, kept because it is punctuation and the II.3 gate image. **[Jack]** |
| **Trunic** | a line through the middle; hexagon edges | The bed is at the foot. No hexagons. The script is not a cipher of English |
| **Dovahzul, Sheikah, Kryptonian, headline scripts** | claw triplets; boxed letters; a shield frame; letters hanging from a top line | No triple slashes, no boxes, no frame. Letters stand; nothing hangs |
| **Aurebesh, Klingon pIqaD, the Hylian scripts** | bold geometric fragments (⊏ ⊐ Γ 7); blade-shaped curves; hooked cursive | Hairline strokes, never filled; every letter has a bedded upright and rightward stones. Γ-like corners (*p*, *t*, *k*) are generic, and none is a letter of these. Aurebesh *resh* (a 7) is the Hal *k*'s near call, above |
| **D'ni** (Cyan's *Myst* and *Riven*) | brush letters with thick and thin, built on hooked Z- and 2-shapes; base-25 numerals in boxes, rotated for fives | Rivenkeep's *Riven* and *Myst-* already echo Cyan, so this was checked hardest. The course-hand is monoline chisel-work, straight and square-footed, with no pen contrast and no hooks; its numerals are capped letters counted in twenties and twelves, never boxed or rotated. No Orrowen word matches a published D'ni word except *gor* (D'ni "time", Orrowen "every"), a form match only |
| **The grain** | knife-cuts, rings | The course-hand is straight, linear and square-footed. The two hands never share a mark, except in the Last Carver's error (§6.13), which is deliberate |

The v2 screen of the word-signs, the turned stone and the leaf-hand is in §13.

### 6.15 Locked and earned leaves (display rules for the builder)

- **A locked Orrowen leaf shows the course-hand only.**
  - Its accessible title is "A leaf in the course-hand, not yet read". The English never leaks into `<title>`, `<desc>` or `alt`.
  - Earning the leaf *adds* the translation beneath the hand. It never replaces it: Law 7, the Book only adds.
- **A Hal surface** (the slates, the tale-stone's Stonwryt, the lintel's top names) needs a later unlock than living Orrowen. The living translation of a Hal text can arrive first, as Halyna's reading, before the player can read the Hal themselves.
- **The three tabs** are *The Book | Plain Words | Original* (Jack's note 3; §10). The hand is shown above the first two; *Original* shows the leaf-hand facing the translation, for decoders.
- **Truth or nothing.** Every course-hand line the player can see, cut, dry or written, must be a true encoding. A leaf without an authored Orrowen text shows its first paragraph in the hand, and the rest folded as ruled empty courses, never faked (craft §7).
- **The surfaces that must stay unreadable:**
  - the warden's name cut from the rolls: its stone is **gouged out**, a rough scar across the bed band, and no letters remain to decode;
  - the three lines lost to the stain;
  - the Covenant of Completion;
  - Seren's empty leaf facing V.4. It **stays empty** of every hand, as she asked.

---

## 7 · THE WORD-SIGNS OF THE DRY CUT (*RELLORATH WROD*)

### 7.1 The picture in one paragraph

A word-sign is **one of the First Tongue's marks, worn straight by the chisel and stood on the bed, and read as one Orrowen word**. 27 marks serve as **heads**: each alone is a **root sign**, read as the word the stone kept for it (the Cup is *tum*, "remember"; the Course is *trenn*; the Door is *ganna*). Any head may carry a **crown**: one of 20 other marks, cut small and set over the head like a capstone on a pillar, which turns it into a neighbouring word (the Hearth under the Still is *varn*, home; the Hearth with the Drop is *theld*, family). The head gives the field and the crown the word. A word-sign stands **4.6 u tall**, half again as tall as a letter, "proud of the course", and it sits on a **footing**, a second mortar line under its own. So a reader always knows a sign from a letter. There are **328** word-signs: 27 roots and 301 crowned signs; 134 of them write words of the wf6 lexicon, and 194 write reserve words from `ancestor.md` §3.3, for the tier-3 translation.

![The heads](orrowen/shots/ws_heads.png)

*`wf7/orrowen/shots/ws_heads.png`: the 27 heads as root signs (drawn by `ws_chart.py` with the course-hand's own renderer).*

![The crowns, on the Stone](orrowen/shots/ws_crowns_on_tolm.png)

*`wf7/orrowen/shots/ws_crowns_on_tolm.png`: the 20 crowns, each set on TOLM, the Stone.*

### 7.2 The laws of the word-signs

The ancestor's laws of form (`ancestor.md` §5.3) made the letters out of the marks. The word-signs are the marks the chisel kept *whole*, and they obey the first two of those laws and five of their own.

| Law | | What happens |
|---|---|---|
| **C1** | The chisel straightens. | Curves become straight strokes or corners; a closed curve opens into strokes or is cut as its outline. (Kept from the ancestor.) |
| **C2** | Everything stands on a bed. | Every word-sign has at least one stroke on the mortar line. (Kept.) |
| **W1** | A word-sign keeps its picture whole. | It is not laid to the right as a letter is; it stands on its own centre, and may have parts on either side. The ancestor's C3 (stones laid to the right) and C4 (three leans) are laws of the *letters*. |
| **W2** | A word-sign stands proud. | 4.6 u tall with its crown, 4.2 u as a root; a letter 3. |
| **W3** | A word-sign has a footing. | A second mortar band, y ∈ [−0.62, −0.44], under the sign's cell, from 0.3 u to 4.1 u. |
| **W4** | A word-sign is a word, not a meaning. | It is read as one Orrowen word, aloud, in one way. When the word's meaning drifted from the mark's, the sign went with the word: the Cup, which meant *hold*, is read *tum*, *remember*; the Split, *crack*, is *cresk*, *break*. It is never read for its first sound (that use became the letters). |
| **W5** | Signs are capped. | A second mark, cut small and set over a head as a capstone is set over a pillar, makes a new word from the head's field. The head is pressed to 0.702 of its height to make room. The crown is always free of the head (a 0.45 u joint). |
| **W6** | Endings are laid on. | The complement letters of §3.11 D5 stand after the sign on its bed. |
| **W7** | Branches are laid flat. | No stroke branches off a stem at a slant as a rune's branch does; a branch is a laid stone, or the stem itself turns. (An originality law, after the runes: §13.) |

### 7.3 The geometry

| Measure | Value |
|---|---|
| **cell** | 4.4 u wide × 4.6 u tall; origin at the left foot on the bed, y up, as for the letters (§6.2) |
| **a root sign** | the head drawn whole, y ∈ [0, 4.2] |
| **a crowned sign** | the head pressed, y′ = 0.7024 y (so its top is at 2.95); the crown's 1.0 u box drawn at 1.2× about (2.2, 3.4), so the crown fills y ∈ [3.4, 4.6] |
| **footing** | a second mortar band y ∈ [−0.62, −0.44], x ∈ [0.3, 4.1] of the cell |
| **minimum joint** | 0.45 u between any two strokes of one sign that do not touch (checked for all 328, root and pressed forms) |
| **stroke** | as the letters: half-width 0.19 u in the cut; the §6.6 end rule (square on the bed and at joins, tapered where the chisel lifts, dressed where no end is square) |
| **letter gap, head-joint** | as the letters: 0.55 u within a stone (word-sign to complement, turned stone to word-sign), 2.2 u between stones |
| **line pitch** | 6.4 u in the dry cut (5.2 in letters) |

A crowned sign's strokes are exactly: *the head's strokes with every y multiplied by 0.7024 (rounded to 4 places)*, then *the crown's strokes with each point (x, y) moved to (2.2 + 1.2 (x − 2.2), 3.4 + 1.2 (y − 3.4))*. Appendix A lists every sign's strokes in full, as computed.

### 7.4 The heads

Each head is one of the ancestor's 45 marks (its number in `ancestor.md` §5.2 is given), and each root sign is read as the Orrowen word the stone kept for it. A **★** marks a head whose reading is the living reflex of the mark's own First Tongue name.

| Head | First mark | Root reading | Sense | The picture |
|---|---|---|---|---|
| **TOLM** | the Stem (\*tolm-) | ***tolm*** ★ | a stone; a letter | a stone set up on its bed, gabled at the head; one foot left open, for a stone is dressed, not closed |
| **HALD** | the Square (\*xreun-) | ***hald*** | a wall | two courses in bond, the upper joint broken over the lower: a wall |
| **TRENN** | the Course (\*trenn-) | ***trenn*** ★ | a course of stones; a line of writing; a tale | the Course itself: a line that runs and steps |
| **ODH** | the Curl (\*oð-) | ***odh*** ★ | a hearth | the Curl worn square: the rim where one comes to rest, wound inward to its fire |
| **CRESK** | the Split (\*krask-) | ***cresk*** ★ | break | one stone split in two, the halves leaning apart at the crack |
| **PAR** | the Bearer (\*par-) | ***par*** ★ | guard, protect; a watch | the Bearer: a prop under its load, the load laid across its head |
| **MOLT** | the Breath Within (\*molt-) | ***molt*** ★ | a heart | the breath within, held between the walls of the body |
| **TUM** | the Cup (\*tum-) | ***tum*** ★ | remember | the Cup, and the one thing it holds: to hold in mind |
| **LORR** | the Drop (\*θar-) | ***lorr*** | blood; crimson | the Drop, point up, on the bed |
| **ORL** | the Star (\*kris-) | ***orl*** | a day | the Star raised on its stand: the light of one day |
| **VORR** | the Scar (\*esθ-) | ***vorr*** | fire | three tongues of fire, uneven, from one bed |
| **TOVV** | the Knot (\*lanθ-) | ***tovv*** | wait | the Knot: a line that holds its place, and goes on again past itself |
| **SCETH** | the Bough (\*sul-) | ***sceth*** | a ship, a hull | the Bough is a hull: seen from the bow, open to the sky |
| **MESK** | the Bough (\*sul-) on the Stem | ***mesk*** | a tree; wood | a tree and its wood: boughs laid in tiers on a trunk |
| **BROD** | the Mouth (\*brenn-) | ***brod*** ★ | a word | the Mouth open, and the word going out of it |
| **GARL** | the Hand (\*wind-) | ***garl*** | a hand; a hand of writing | an arm held out, the hand open and turned up |
| **VESK** | the Eye (\*neʔs-) | ***vesk*** | see; read (letters, or a cradle) | the Eye on its stalk, with its sight in it |
| **ULD** | the Roots, the Stem and the Square (as the grain's STONEFOLK) | ***uld*** | a man; a grown person | one who stands, crowned with a square: one of the stone-folk |
| **LUMM** | the Kneel (\*roθ-) | ***lumm*** | kneel | the fold that comes to rest on the ground |
| **LUNN** | the Gap (\*onn-) | ***lunn*** | freedom | an arch with its keystone out: room to go through |
| **VENN** | the Whole (\*weinn-) | ***venn*** ★ | true; plumb; faithful | a plumb-bob on its line: what is true hangs true |
| **KYL** | the Turn (\*neθ-) | ***kyl*** | change | a line that turns aside and goes on |
| **GANNA** | the Door (\*gann-aʔ), kept whole | ***ganna*** ★ | a gate | the two posts and their lintel: the Door, which both peoples kept whole |
| **LODH** | the Bed (\*loð-) | ***lodh*** ★ | mortar; the mortar line; the bond | a stone set in its wet bed |
| **WADH** | the Course (\*trenn-), running on | ***wadh*** | the sea | the Course running on and on, up and down: the great water |
| **BRUNN** | the Rim (\*enθ-), stood on the bed | ***brunn*** | a mountain | the Rim stood up: peaks against the sky |
| **FORE** | the Fore (\*re-il), kept whole | ***hosast*** | first | the Fore itself, the first builders' mark: first; before all |

**The heads as data** (strokes in cell units, the root form):

```json
{
 "TOLM": [[[1.0,0],[1.0,3.2],[2.2,4.2],[3.4,3.2],[3.4,1.6]]],
 "HALD": [[[0.9,0],[0.9,1.4],[3.5,1.4]],[[0.9,2.8],[3.5,2.8],[3.5,1.4]],[[0.9,2.8],[0.9,4.2]],[[2.2,1.4],[2.2,2.8]]],
 "TRENN": [[[0.9,0],[0.9,2.1],[3.5,2.1],[3.5,4.2]]],
 "ODH": [[[1.0,0],[1.0,4.2],[3.4,4.2],[3.4,1.2],[1.8,1.2],[1.8,3.2],[2.6,3.2],[2.6,2.0]]],
 "CRESK": [[[1.0,0],[1.0,2.2],[2.0,2.8],[1.4,4.2]],[[3.4,0],[3.4,2.0],[2.5,2.6],[3.2,4.2]]],
 "PAR": [[[1.2,0],[2.2,3.2]],[[2.2,3.2],[3.5,3.2]],[[0.9,3.2],[1.7,3.2]],[[2.2,3.2],[2.2,4.2]]],
 "MOLT": [[[1.6,0],[0.9,3.4]],[[2.8,0],[3.5,3.4]],[[1.7,2.0],[1.95,2.7],[2.2,2.0],[2.45,2.7],[2.7,2.0]]],
 "TUM": [[[1.6,0],[0.9,3.4]],[[2.8,0],[3.5,3.4]],[[2.2,1.6],[2.2,2.8]]],
 "LORR": [[[2.2,0],[2.2,0.8]],[[2.2,0.8],[1.2,2.0],[2.2,4.2],[3.2,2.0],[2.2,0.8]]],
 "ORL": [[[1.0,0],[2.2,2.0],[3.4,0]],[[2.2,2.0],[2.2,4.2]],[[1.2,3.6],[3.2,2.6]],[[1.2,2.6],[3.2,3.6]]],
 "VORR": [[[1.2,0],[1.2,1.8],[1.8,3.0]],[[2.2,0],[2.2,2.4],[2.8,4.2]],[[3.2,0],[3.2,1.6]]],
 "TOVV": [[[1.8,0],[1.8,1.4]],[[2.6,2.8],[2.6,4.2]],[[1.8,1.4],[1.2,2.1],[2.6,2.8],[3.2,2.1],[1.8,1.4]]],
 "SCETH": [[[1.7,4.2],[0.9,2.1],[2.2,0],[3.5,2.1],[2.7,4.2]]],
 "MESK": [[[2.2,0],[2.2,2.0]],[[1.0,2.0],[3.4,2.0]],[[1.0,2.0],[1.6,3.2],[2.2,2.0]],[[2.2,2.0],[2.8,3.2],[3.4,2.0]],[[1.6,3.2],[2.2,4.2],[2.8,3.2]]],
 "BROD": [[[2.2,0],[2.2,1.0]],[[3.4,1.5],[2.2,1.0],[1.0,2.4],[2.2,3.8],[3.4,3.3]],[[2.7,2.4],[3.6,2.4]]],
 "GARL": [[[1.0,0],[2.0,2.6],[3.4,2.6],[3.4,3.8]]],
 "VESK": [[[2.2,0],[2.2,1.2]],[[0.9,2.5],[2.2,3.8],[3.5,2.5],[2.2,1.2],[0.9,2.5]],[[2.2,2.1],[2.2,2.9]]],
 "ULD": [[[1.4,0],[2.2,2.6]],[[3.0,0],[2.2,2.6]],[[2.2,2.6],[2.2,3.3]],[[1.6,3.3],[2.8,3.3],[2.8,4.2],[1.6,4.2],[1.6,3.3]]],
 "LUMM": [[[1.2,4.2],[1.2,1.4],[2.4,1.4],[2.4,0],[3.4,0.0]]],
 "LUNN": [[[1.0,0],[1.0,3.4],[1.8,4.2]],[[3.4,0],[3.4,3.4],[2.6,4.2]]],
 "VENN": [[[2.2,4.2],[2.2,2.4]],[[2.2,2.4],[1.5,1.2],[2.2,0],[2.9,1.2],[2.2,2.4]]],
 "KYL": [[[1.2,0],[1.2,2.0],[3.2,3.2],[3.2,4.2]]],
 "GANNA": [[[1.2,0],[1.5,3.6]],[[3.2,0],[2.9,3.6]],[[0.8,3.6],[3.6,3.6]]],
 "LODH": [[[0.9,1.6],[1.6,0.6],[2.8,0.6],[3.5,1.6]],[[2.2,0],[2.2,0.6]],[[1.6,1.6],[1.6,3.0],[2.8,3.0],[2.8,1.8]]],
 "WADH": [[[0.9,0],[0.9,2.2],[1.7,2.2],[1.7,1.0],[2.6,1.0],[2.6,3.4],[3.5,3.4]]],
 "BRUNN": [[[0.9,0],[1.6,1.8],[2.2,1.2],[3.0,3.6],[3.6,2.2]]],
 "FORE": [[[2.2,0],[2.2,4.2]],[[1.2,3.1],[3.2,3.1]]]
}
```

### 7.5 The crowns

| Crown | First mark | Sense it lends | Signs | Examples |
|---|---|---|---|---|
| **cope** | the Bar (\*hosk-) | over; capped; chief; closed and kept | 23 | *hosk* (a lintel), *hellur* (a hall), *dask* (the end), *resk* (sit), *lernil* (a defeat) |
| **rim** | the Rim (\*enθ-) | edge, rim, point, height | 19 | *tald* (rise), *taldow* (a tower), *nesk* (lead), *hedh* (the last light), *sevir* (a volley) |
| **lone** | the Lone Mark (\*itt-) | one, single, alone | 22 | *pell* (a spire), *rivull* (a foundation), *fenn* (follow), *memm* (a friend), *pedh* (a shot: what a gun throws) |
| **three** | the Three (\*ros-) | many; a folk; a heap | 17 | *stell* (a cairn), *hinnar* (a walled town), *flenn* (a leaf of a book or of slate), *lonn* (kin by blood), *kest* (a company of soldiers) |
| **course** | the Course (\*trenn-) | a line; going on; a lineage | 24 | *hal* (bedrock), *gald* (build), *orr* (go), *prenth* (a bench), *bosk* (attack) |
| **turn** | the Turn (\*neθ-) | turning; change; coming back | 14 | *gorn* (a corner), *bystir* (a stair), *darr* (come), *bynd* (a foe), *cald* (drag) |
| **still** | the Still (\*waʔr-) | stillness; rest; at home | 23 | *ston* (stand), *cumm* (a haven: any walled place of shelter), *cadh* (lay), *varn* (home), *gask* (broken) |
| **star** | the Star (\*kris-) | light; a glint; a flash | 17 | *sirr* (glass), *disker* (a window), *lestir* (show the way), *greller* (a lamp), *bramm* (a gun) |
| **fade** | the Fade (\*feʔ-) | going dark; night; death; loss | 19 | *domm* (black), *kaelir* (a ruin), *luth* (ink), *aedh* (sleep), *hurr* (kill) |
| **pale** | the Pale (\*lenn-) | white; frost; cold | 7 | *lenn* (silver), *ludal* (fear), *semm* (a tear), *grem* (winter), *derd* (a bone) |
| **drop** | the Drop (\*θar-) | blood; kin | 10 | *ledal* (a grave), *tesk* (a generation), *theld* (a family), *grest* (harm), *prumul* (sad) |
| **fork** | the Split (\*krask-) | harm; a break; war | 6 | *vathur* (a breach), *bethir* (doubt), *brist* (lightning), *cullar* (a snare), *dath* (evil) |
| **wedge** | the Wedge (\*tass-) | a blow; force | 15 | *stann* (quarry), *kiser* (an assault), *hask* (run), *gorr* (fight), *pemess* (defend) |
| **cut** | the Cut (\*skeθ-) | cutting; a blade; hewing | 9 | *ryt* (a cut vow), *hesp* (a sword), *sulenn* (a scar), *nestull* (an oar), *crynir* (a plank) |
| **gap** | the Gap (\*onn-) | open; between; let go | 14 | *baek* (a lid), *gebb* (a door), *mosk* (begin), *voth* (tend), *tresk* (a cleft) |
| **notch** | the Tally (\*kail-) | a count; a time | 11 | *serull* (a coin), *tynur* (a siege), *haral* (an order), *vadull* (a forebear), *stemir* (a battle) |
| **door** | the Door (\*gann-aʔ) | a gate; a way in; a pair | 7 | *stinal* (a raised stone of offering), *lest* (a house), *cemm* (meet), *arra* (a guest), *peltir* (warn) |
| **bough** | the Bough (\*sul-) | growing; young; of wood | 10 | *saenul* (a pillar of stone), *paltur* (a niche), *tragul* (a promise), *blenth* (bread), *hagess* (a pike) |
| **zig** | the Breath Within (\*molt-) | breath; voice; wind | 15 | *bront* (a boulder), *brellir* (a joint between stones), *vell* (a song), *dhaedh* (warm), *nycul* (a lie) |
| **cup** | the Cup (\*tum-) | held; within | 19 | *tynt* (a pebble), *nelter* (a vault), *mymm* (return), *nunth* (a cup), *heness* (a captive) |

**The crowns as data** (strokes in the crown's 1.0 u box, y ∈ [3.4, 4.4], before the 1.2× setting):

```json
{
 "cope": [[[1.2,3.9],[3.2,3.9]]],
 "rim": [[[1.1,3.5],[2.2,4.4],[3.3,3.5]]],
 "lone": [[[1.9,3.4],[1.9,4.4]],[[2.35,3.75],[2.9,3.75]]],
 "three": [[[1.5,3.4],[1.5,4.1]],[[2.2,3.4],[2.2,4.4]],[[2.9,3.4],[2.9,4.1]]],
 "course": [[[1.2,3.4],[1.2,3.9],[3.2,3.9],[3.2,4.4]]],
 "turn": [[[1.5,3.4],[1.5,3.9],[2.9,4.4]]],
 "still": [[[1.3,3.6],[3.1,3.6]],[[1.3,4.2],[3.1,4.2]]],
 "star": [[[2.2,3.4],[2.2,4.4]],[[1.75,3.62],[2.65,4.18]],[[1.75,4.18],[2.65,3.62]]],
 "fade": [[[1.0,4.3],[1.6,4.3]],[[1.9,3.95],[2.45,3.95]],[[2.75,3.6],[3.15,3.6]]],
 "pale": [[[1.3,3.45],[1.6,4.35]],[[2.05,3.45],[2.35,4.35]],[[2.8,3.45],[3.1,4.35]]],
 "drop": [[[2.2,3.4],[1.85,3.9],[2.2,4.4],[2.55,3.9],[2.2,3.4]]],
 "fork": [[[2.2,3.4],[2.2,3.85],[1.7,4.4]],[[2.62,4.1],[2.9,4.4]]],
 "wedge": [[[1.7,4.4],[2.7,4.4],[2.2,3.4],[1.7,4.4]]],
 "cut": [[[1.7,4.4],[2.2,3.4],[2.7,4.4]]],
 "gap": [[[1.1,3.9],[1.9,3.9]],[[2.5,3.9],[3.3,3.9]]],
 "notch": [[[1.1,4.2],[1.85,4.2],[2.2,3.6],[2.55,4.2],[3.3,4.2]]],
 "door": [[[1.65,3.4],[1.75,3.95]],[[2.75,3.4],[2.65,3.95]],[[1.4,4.4],[3.0,4.4]]],
 "bough": [[[2.0,4.4],[1.7,3.9],[2.2,3.4],[2.7,3.9],[2.4,4.4]]],
 "zig": [[[1.2,3.5],[1.7,4.3],[2.2,3.5],[2.7,4.3],[3.2,3.5]]],
 "cup": [[[1.95,3.4],[1.65,4.4]],[[2.45,3.4],[2.75,4.4]]]
}
```

**Why a crown can stand over any head.** Every crown lies wholly above y = 3.4, and every pressed head wholly below y = 2.95, so a crown can never touch or crowd a head; the check (§7.9) confirms 0.45 u everywhere.

### 7.6 The marks of the dry cut

| Mark | Shape | Reading | From the first marks |
|---|---|---|---|
| **the turned stone** (NOT) | a pin 1.8 u tall with one laid stone running **left** from its head: strokes `[[1.4,0],[1.4,1.8]]`, `[[1.4,1.8],[0.3,1.8]]` in a cell 1.8 u wide | *nath, nel, new*, the prefix *na-*: not | The First Tongue's "not" was a mark turned to face the other way (`ancestor.md` G6). A living letter's stones all run right; this is the one stone in the living hand that is laid the wrong way. It stands before the word it turns, on its bed. (The Hal, which is mirrored, cuts it running right.) |
| **the foremark** | the word-sign FORE (§7.4): a stem crossed near its head | ***hosast***, "first" | The Fore, kept whole by both peoples (`ancestor.md` §5.6). A Latin cross, and "the Latin cross is fine" (note 8). It may stand at the head of a work, on the first stone laid, and on the lid of the black chest |
| **the gate** | §6.7 | after a cited vow, ***Ston*** "it stands" | the Door, kept whole |
| perpend, wedge, coping | §6.7 | as in letters; the wedge also stands for *eth, ell, veth* | the End, the Wedge, the Door and the Bar |

### 7.7 The inventory

**328 word-signs**, grouped by head. Columns: **no.** · **reads** (the word, as the Book would spell it) · **sense** · **sign** (head, and crown if any) · **cl.** (harmony class, for the complements) · **why** (the reading of the picture) · **src** (L the wf6 lexicon; R a reserve root of `ancestor.md` §3.3, which owes the dictionary pass).

**TOLM** (the Stem (\*tolm-); 20 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 1 | ***tolm*** | a stone; a letter | TOLM | B | the root sign | L |
| 2 | ***hosk*** | a lintel, a capstone; (v.) seal | TOLM+cope | B | a stone laid over | L |
| 3 | ***tald*** | rise, stand up | TOLM+rim | B | a stone raised to its height | L |
| 4 | ***pell*** | a spire, a tall point | TOLM+lone | S | one tall stone | L |
| 5 | ***stell*** | a cairn | TOLM+three | S | stones heaped | L |
| 6 | ***gorn*** | a corner, a quoin | TOLM+turn | B | where the stones turn | L |
| 7 | ***stann*** | quarry, cut stone from the bed | TOLM+wedge | B | stone split out with wedges | L |
| 8 | ***ryt*** | a cut vow; an inscription; cut letters, write, swear | TOLM+cut | S | a cut stone | L |
| 9 | ***sirr*** | glass | TOLM+star | S | a stone that the light goes through | L |
| 10 | ***lenn*** | silver | TOLM+pale | S | the pale-bright stone | L |
| 11 | ***ston*** | stand (of a wall), make stand, hold firm | TOLM+still | B | a stone at rest where it was set | L |
| 12 | ***hal*** | bedrock, the living rock | TOLM+course | B | the stone that runs under all | L |
| 13 | ***domm*** | black | TOLM+fade | B | a stone gone dark | L |
| 14 | ***baek*** | a lid, a cover | TOLM+gap | S | the stone lifted off | R |
| 15 | ***ledal*** | a grave | TOLM+drop | B | the stone over the dead of the kin | R |
| 16 | ***bront*** | a boulder | TOLM+zig | B | a stone the ice carried | R |
| 17 | ***serull*** | a coin, a struck piece | TOLM+notch | B | a stone cut to a count | R |
| 18 | ***stinal*** | a raised stone of offering, an altar | TOLM+door | B | a stone at the way in | R |
| 19 | ***saenul*** | a pillar of stone | TOLM+bough | B | a stone that stands as a trunk | R |
| 20 | ***tynt*** | a pebble | TOLM+cup | S | a stone held in the hand | R |

**HALD** (the Square (\*xreun-); 18 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 21 | ***hald*** | a wall | HALD | B | the root sign | L |
| 22 | ***lest*** | a house | HALD+door | S | a wall with a door in it | L |
| 23 | ***gebb*** | a door | HALD+gap | S | the gap in a wall | L |
| 24 | ***gald*** | build, raise a work | HALD+course | B | a wall raised course on course | L |
| 25 | ***cumm*** | a haven: any walled place of shelter | HALD+still | B | the still place inside a wall | L |
| 26 | ***taldow*** | a tower, a high place | HALD+rim | B | a wall to its height | L |
| 27 | ***vathur*** | a breach | HALD+fork | B | a wall broken | R |
| 28 | ***kaelir*** | a ruin, a thing broken down | HALD+fade | S | a wall gone down to dark | R |
| 29 | ***kiser*** | an assault, a rushing-on | HALD+wedge | S | blows against a wall | R |
| 30 | ***tynur*** | a siege, a sitting-down around | HALD+notch | B | a wall counting its days | R |
| 31 | ***hinnar*** | a walled town | HALD+three | B | many walls | R |
| 32 | ***hellur*** | a hall | HALD+cope | B | walls under one roof-stone | R |
| 33 | ***nelter*** | a vault, an arched room below | HALD+cup | S | a wall that holds a room within | R |
| 34 | ***rivull*** | a foundation, the bottom course | HALD+lone | B | the one course under the rest | R |
| 35 | ***bystir*** | a stair; to climb | HALD+turn | S | a wall that turns upward | R |
| 36 | ***paltur*** | a niche, a small hollow in a wall | HALD+bough | B | the hollow in the wall where the old capstone lies | R |
| 37 | ***disker*** | a window, an eye in a wall | HALD+star | S | a wall the light comes through | R |
| 38 | ***brellir*** | a joint between stones | HALD+zig | S | where a wall breathes | R |

**TRENN** (the Course (\*trenn-); 18 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 39 | ***trenn*** | a course of stones; a line of writing; a tale | TRENN | S | the root sign | L |
| 40 | ***orr*** | go, walk | TRENN+course | B | a line going on | L |
| 41 | ***darr*** | come | TRENN+turn | B | a line turning toward | L |
| 42 | ***hask*** | run | TRENN+wedge | B | going with force | L |
| 43 | ***cadh*** | lay (a stone, a course, a tale) | TRENN+still | B | a course set down to rest | L |
| 44 | ***dask*** | the end | TRENN+cope | B | the course capped | L |
| 45 | ***tesk*** | a generation | TRENN+drop | S | a line of blood laid down | L |
| 46 | ***vell*** | a song | TRENN+zig | S | a line with breath in it | L |
| 47 | ***luth*** | ink | TRENN+fade | B | the dark line | L |
| 48 | ***flenn*** | a leaf of a book or of slate | TRENN+three | S | lines laid under lines | L |
| 49 | ***cemm*** | meet; a meeting | TRENN+door | S | lines that come to one gate | L |
| 50 | ***fenn*** | follow | TRENN+lone | S | one line after another | R |
| 51 | ***mymm*** | return, come back | TRENN+cup | S | the line held to its start | R |
| 52 | ***lestir*** | show the way, guide | TRENN+star | S | a line with a light on it | R |
| 53 | ***nesk*** | lead | TRENN+rim | S | the line's front edge | R |
| 54 | ***mosk*** | begin | TRENN+gap | B | the open end of a line | R |
| 55 | ***haral*** | an order; to bid | TRENN+notch | B | a line cut for a count of men | R |
| 56 | ***tragul*** | a promise | TRENN+bough | B | a line that is still growing | R |

**ODH** (the Curl (\*oð-); 16 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 57 | ***odh*** | a hearth | ODH | B | the root sign | L |
| 58 | ***varn*** | home | ODH+still | B | the hearth at rest | L |
| 59 | ***theld*** | a family, a household | ODH+drop | S | the hearth's blood | L |
| 60 | ***arra*** | a guest | ODH+door | B | one at the hearth's door | L |
| 61 | ***greller*** | a lamp | ODH+star | S | the hearth's small light | R |
| 62 | ***prenth*** | a bench | ODH+course | S | the long seat by the hearth | R |
| 63 | ***resk*** | sit | ODH+cope | S | to settle at the hearth | R |
| 64 | ***aedh*** | sleep; to sleep | ODH+fade | S | the hearth gone dark | R |
| 65 | ***vadull*** | a forebear; the old line | ODH+notch | B | the hearth's count of years | R |
| 66 | ***lonn*** | kin by blood | ODH+three | B | the many of one hearth | R |
| 67 | ***memm*** | a friend, one who stands beside | ODH+lone | S | one taken into the hearth | R |
| 68 | ***dhaedh*** | warm | ODH+zig | S | the hearth's breath | R |
| 69 | ***nunth*** | a cup | ODH+cup | B | the hearth's cup | R |
| 70 | ***blenth*** | bread | ODH+bough | S | what grows and is baked at the hearth | R |
| 71 | ***hedh*** | the last light, dusk, evening | ODH+rim | S | the hour the hearth is lit | R |
| 72 | ***voth*** | tend, care for | ODH+gap | B | to open the hearth to another | R |

**CRESK** (the Split (\*krask-); 19 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 73 | ***cresk*** | break | CRESK | S | the root sign | L |
| 74 | ***tresk*** | a cleft, a split; cleave, rive, tear | CRESK+gap | S | a break opened | L |
| 75 | ***grest*** | harm, hurt | CRESK+drop | S | a break that bleeds | L |
| 76 | ***gorr*** | fight | CRESK+wedge | B | a break by blows | L |
| 77 | ***hurr*** | kill | CRESK+fade | B | a break to the dark | L |
| 78 | ***bosk*** | attack | CRESK+course | B | breaking that comes on | L |
| 79 | ***bramm*** | a gun | CRESK+star | B | a break with a flash | L |
| 80 | ***pedh*** | a shot: what a gun throws | CRESK+lone | S | one thrown break | L |
| 81 | ***hesp*** | a sword | CRESK+cut | S | the breaking blade | L |
| 82 | ***kest*** | a company of soldiers | CRESK+three | S | the many who fight together | L |
| 83 | ***nycul*** | a lie; to lie | CRESK+zig | B | breath that breaks | R |
| 84 | ***lernil*** | a defeat | CRESK+cope | S | the breaking that ends it | R |
| 85 | ***stemir*** | a battle | CRESK+notch | S | a breaking counted in hours | R |
| 86 | ***sevir*** | a volley, a shower of shot | CRESK+rim | S | a break along the whole edge | R |
| 87 | ***bynd*** | a foe, one who comes against | CRESK+turn | S | the break turned toward us | R |
| 88 | ***gask*** | broken | CRESK+still | B | a break that stays | R |
| 89 | ***heness*** | a captive | CRESK+cup | S | one held after the breaking | R |
| 90 | ***hagess*** | a pike, a long spear | CRESK+bough | S | the breaking shaft of wood | R |
| 91 | ***peltir*** | warn; a warning | CRESK+door | S | harm at the door | R |

**PAR** (the Bearer (\*par-); 13 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 92 | ***par*** | guard, protect; a watch | PAR | B | the root sign | L |
| 93 | ***crenn*** | a captain; the Captain | PAR+cope | S | the chief of those who bear the weight | L |
| 94 | ***osk*** | trust (v. and n.) | PAR+still | B | to rest one's weight on | L |
| 95 | ***pemess*** | defend, ward off | PAR+wedge | S | to bear the blow | R |
| 96 | ***begorn*** | a watcher on a height, a lookout | PAR+rim | B | the guard on the edge | R |
| 97 | ***cryrull*** | a troop, a band under one leader | PAR+three | B | many under one guard | R |
| 98 | ***lymm*** | bring | PAR+course | S | to bear along | R |
| 99 | ***renn*** | save, bring through | PAR+door | S | to bear through the gate | R |
| 100 | ***havul*** | a pack, a bundle | PAR+cup | B | what is borne and held | R |
| 101 | ***bemm*** | lift | PAR+lone | S | to bear one thing up | R |
| 102 | ***cald*** | drag, haul | PAR+turn | B | to bear a gun to another place | R |
| 103 | ***gesk*** | strong | PAR+star | S | bearing, and shining with it | R |
| 104 | ***hydull*** | patience; to endure | PAR+notch | B | bearing, counted in years | R |

**MOLT** (the Breath Within (\*molt-); 15 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 105 | ***molt*** | a heart | MOLT | B | the root sign | L |
| 106 | ***hoss*** | breath | MOLT+zig | B | the breath going out | L |
| 107 | ***lomm*** | grief | MOLT+fade | B | a heart gone dark | L |
| 108 | ***vall*** | love | MOLT+turn | B | what the heart turns to | L |
| 109 | ***ludal*** | fear | MOLT+pale | B | a heart gone white | R |
| 110 | ***hylenn*** | gladness, joy | MOLT+star | S | a heart with a light in it | R |
| 111 | ***saemal*** | hope | MOLT+bough | B | a heart still growing | R |
| 112 | ***syllorn*** | courage | MOLT+wedge | B | a heart that takes the blow | R |
| 113 | ***teltor*** | mercy | MOLT+gap | B | a heart that opens | R |
| 114 | ***haeril*** | forgive, let a wrong go | MOLT+course | S | a heart that lets it go on | R |
| 115 | ***myrral*** | the self within, a soul | MOLT+lone | B | the one within | R |
| 116 | ***dhyvull*** | laugh | MOLT+three | B | the heart's breath broken into many | R |
| 117 | ***prumul*** | sad, heavy of heart | MOLT+drop | B | a heart that bleeds inward | R |
| 118 | ***hyvul*** | alone, lonely | MOLT+rim | B | a heart at the edge | R |
| 119 | ***ledh*** | feel | MOLT+cup | S | to hold a thing in the heart | R |

**TUM** (the Cup (\*tum-); 10 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 120 | ***tum*** | remember | TUM | B | the root sign: Tumar | L |
| 121 | ***sesk*** | know (a fact) | TUM+cope | S | held, and closed over | L |
| 122 | ***kaever*** | think; a thought | TUM+zig | S | what the mind breathes | R |
| 123 | ***hyrril*** | understand, grasp | TUM+turn | S | to turn a thing till it is held | R |
| 124 | ***daevar*** | believe, hold true | TUM+still | B | held, and at rest | R |
| 125 | ***rystull*** | learn | TUM+course | B | holding, and going on | R |
| 126 | ***prener*** | the mind | TUM+lone | S | the one that holds | R |
| 127 | ***filv*** | a dream | TUM+fade | S | held in the dark | R |
| 128 | ***bethir*** | doubt | TUM+fork | S | a holding that splits | R |
| 129 | ***mamm*** | lose | TUM+gap | B | the cup let go | R |

**LORR** (the Drop (\*θar-); 6 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 130 | ***lorr*** | blood; crimson | LORR | B | the root sign | L |
| 131 | ***unth*** | red | LORR+star | B | the blood's colour, shining | R |
| 132 | ***semm*** | a tear; to weep | LORR+pale | S | a pale drop | R |
| 133 | ***sulenn*** | a scar, a healed cut | LORR+cut | S | the cut the blood closed | R |
| 134 | ***buthar*** | anoint | LORR+cope | B | a drop laid on the head | R |
| 135 | ***lernul*** | oil | LORR+still | B | the still drop | R |

**ORL** (the Star (\*kris-); 17 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 136 | ***orl*** | a day | ORL | B | the root sign | L |
| 137 | ***vess*** | a night | ORL+fade | S | the day gone dark | L |
| 138 | ***clem*** | an hour | ORL+notch | S | a notch of the day | L |
| 139 | ***surr*** | a year | ORL+turn | B | the turn of the days | L |
| 140 | ***grem*** | winter | ORL+pale | S | the white days | L |
| 141 | ***helv*** | the sky, the upper air | ORL+cope | S | the light over all | L |
| 142 | ***bell*** | gold, golden | ORL+drop | S | a drop of the day | L |
| 143 | ***rerd*** | the sun | ORL+lone | S | the one light | R |
| 144 | ***selm*** | the moon; a month | ORL+gap | S | the light with a piece out of it | R |
| 145 | ***elth*** | a star | ORL+three | S | the many small lights | R |
| 146 | ***ryst*** | the morning | ORL+rim | S | the day at its edge | R |
| 147 | ***fedh*** | a time, a season | ORL+course | S | days going on | R |
| 148 | ***dhenn*** | a shadow | ORL+cup | S | what holds the light off | R |
| 149 | ***baeg*** | bright | ORL+star | S | light shining | R |
| 150 | ***heth*** | spring, the lengthening | ORL+bough | S | the growing days | R |
| 151 | ***brist*** | lightning | ORL+fork | S | light that breaks | R |
| 152 | ***dustal*** | dim | ORL+still | B | the light held low | R |

**VORR** (the Scar (\*esθ-); 11 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 153 | ***vorr*** | fire | VORR | B | the root sign | L |
| 154 | ***senn*** | die: go out, as a fire in peace | VORR+fade | S | a fire going out | L |
| 155 | ***brenth*** | coal | VORR+still | S | fire at rest | L |
| 156 | ***vem*** | a flame | VORR+lone | S | one tongue of the fire | R |
| 157 | ***drod*** | a spark | VORR+star | B | the fire's flash | R |
| 158 | ***dhidh*** | smoke | VORR+zig | S | the fire's breath | R |
| 159 | ***syndal*** | kindle | VORR+bough | B | to make a fire grow | R |
| 160 | ***raltar*** | quench, put out | VORR+cope | B | a fire capped | R |
| 161 | ***tymorn*** | a torch | VORR+course | B | a fire carried along | R |
| 162 | ***bith*** | hot | VORR+wedge | S | fire that strikes | R |
| 163 | ***kesk*** | an ember | VORR+cup | S | fire held in the ash | R |

**TOVV** (the Knot (\*lanθ-); 9 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 164 | ***tovv*** | wait | TOVV | B | the root sign | L |
| 165 | ***hess*** | stop | TOVV+cope | S | the knot capped | L |
| 166 | ***tul*** | yet, still | TOVV+course | B | waiting, and going on | L |
| 167 | ***somm*** | while, as long as | TOVV+still | B | held in its place for a length | L |
| 168 | ***amm*** | when (conj.) | TOVV+notch | B | at the notch of the hour | L |
| 169 | ***nend*** | watch, keep watch | TOVV+star | S | waiting with a light | R |
| 170 | ***bysk*** | tie, knot fast | TOVV+cup | S | the knot held | R |
| 171 | ***cullar*** | a snare, a trap | TOVV+fork | B | a knot that harms | R |
| 172 | ***niss*** | slow | TOVV+three | S | waiting many times | R |

**SCETH** (the Bough (\*sul-); 13 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 173 | ***sceth*** | a ship, a hull | SCETH | S | the root sign | L |
| 174 | ***wemm*** | a sail | SCETH+zig | S | the hull's wind | L |
| 175 | ***tav*** | come ashore, land a boat | SCETH+turn | B | a hull turning in | L |
| 176 | ***sulter*** | a small boat | SCETH+lone | S | one small hull | R |
| 177 | ***mivenn*** | a mast | SCETH+rim | S | the hull's tall point | R |
| 178 | ***breller*** | a keel | SCETH+course | S | the line under the hull | R |
| 179 | ***nestull*** | an oar | SCETH+cut | B | the blade that drives the hull | R |
| 180 | ***farr*** | sail (v.) | SCETH+wedge | B | a hull driven | R |
| 181 | ***felm*** | drown | SCETH+fade | S | a hull gone under the dark | R |
| 182 | ***piskur*** | a net | SCETH+three | B | what the hull draws in, many | R |
| 183 | ***pynull*** | a boatwright, a worker of wood | SCETH+cope | B | the master of the hull | R |
| 184 | ***sugorn*** | a fisher | SCETH+drop | B | the hull that feeds the kin | R |
| 185 | ***haemer*** | a raft; to float | SCETH+still | S | a hull at rest on the water | R |

**MESK** (the Bough (\*sul-) on the Stem; 11 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 186 | ***mesk*** | a tree; wood | MESK | S | the root sign | L |
| 187 | ***lurr*** | a forest | MESK+three | B | many trees | L |
| 188 | ***crynir*** | a plank | MESK+cut | S | wood hewn flat | R |
| 189 | ***gost*** | fell a tree | MESK+fade | B | a tree brought down | R |
| 190 | ***brynt*** | a stump | MESK+cope | S | a tree cut and capped | R |
| 191 | ***gend*** | a shoot from a stump | MESK+bough | S | a tree growing again | R |
| 192 | ***sinth*** | a flower | MESK+star | S | the tree's bright thing | R |
| 193 | ***nanth*** | fruit | MESK+drop | B | what drops from the tree | R |
| 194 | ***feth*** | moss | MESK+still | S | what grows on still wood | R |
| 195 | ***brint*** | a thorn | MESK+wedge | S | the tree's point | R |
| 196 | ***linth*** | grass | MESK+course | S | growing things in a line | R |

**BROD** (the Mouth (\*brenn-); 16 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 197 | ***brod*** | a word | BROD | B | the root sign | L |
| 198 | ***brodh*** | put into words, tell, speak | BROD+course | B | words laid in a line | L |
| 199 | ***carm*** | a call, a cry; cry out, call | BROD+wedge | B | a word with force behind it | L |
| 200 | ***pess*** | ask | BROD+gap | S | a word left open | L |
| 201 | ***tess*** | answer; stand surety for | BROD+turn | S | a word coming back | L |
| 202 | ***voll*** | a name | BROD+lone | B | the one word for one | L |
| 203 | ***ammad*** | teach | BROD+three | B | a word to many | L |
| 204 | ***hunn*** | hear | BROD+cup | B | a word held | L |
| 205 | ***gomm*** | a horn | BROD+star | B | the voice that carries | L |
| 206 | ***mysk*** | say | BROD+still | S | a word set down | R |
| 207 | ***dast*** | shout, scream | BROD+zig | B | a word with all the breath | R |
| 208 | ***medh*** | whisper | BROD+fade | S | a word going dark | R |
| 209 | ***rellor*** | a sign, a signal | BROD+notch | B | a word cut as a mark | R |
| 210 | ***niltenn*** | a plan, a counsel | BROD+rim | S | a word set ahead | R |
| 211 | ***stathul*** | praise | BROD+cope | B | a word laid over | R |
| 212 | ***redul*** | a council, those who sit and weigh | BROD+door | B | the many words at one door | R |

**GARL** (the Hand (\*wind-); 16 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 213 | ***garl*** | a hand; a hand of writing | GARL | B | the root sign | L |
| 214 | ***keth*** | hold, keep; (of the wood) know | GARL+cup | S | a hand cupped round | L |
| 215 | ***hebb*** | give | GARL+course | S | a hand held out | L |
| 216 | ***lusk*** | loose, let go, set free | GARL+gap | B | the hand opened | L |
| 217 | ***sollan*** | peace | GARL+still | B | the hands at rest after the work | L |
| 218 | ***drunn*** | a mallet, a hammer | GARL+wedge | B | the hand's blow | L |
| 219 | ***bresk*** | a chisel | GARL+cut | S | the hand's cutting edge | L |
| 220 | ***nydh*** | count | GARL+notch | S | notches under the hand | L |
| 221 | ***prass*** | a master of the craft | GARL+cope | B | the hand that caps the work | L |
| 222 | ***femm*** | touch | GARL+drop | S | the hand laid on | R |
| 223 | ***wesk*** | find | GARL+star | S | the hand that lights on a thing | R |
| 224 | ***birnenn*** | a trowel | GARL+rim | S | the hand's edge in the mortar | R |
| 225 | ***peskul*** | bless | GARL+lone | B | a hand laid on one | R |
| 226 | ***lamm*** | bury, lay in earth | GARL+fade | B | the hand that lays in the dark | R |
| 227 | ***lemm*** | hide | GARL+turn | S | a hand turned over a thing | R |
| 228 | ***bamm*** | pull | GARL+three | B | many hands on the rope | R |

**VESK** (the Eye (\*neʔs-); 8 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 229 | ***vesk*** | see; read (letters, or a cradle) | VESK | S | the root sign | L |
| 230 | ***lern*** | the face | VESK+rim | S | the eye's edge | R |
| 231 | ***stykil*** | wonder | VESK+star | S | a light in the eye | R |
| 232 | ***naelur*** | choose | VESK+lone | B | the eye on one | R |
| 233 | ***raevul*** | seek | VESK+course | B | the eye going on | R |
| 234 | ***virr*** | near | VESK+cup | S | within the eye's hold | R |
| 235 | ***deld*** | far | VESK+fade | S | where sight goes dim | R |
| 236 | ***bisk*** | the head | VESK+cope | S | what the eye is set in | R |

**ULD** (the Roots, the Stem and the Square (as the grain's STONEFOLK); 13 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 237 | ***uld*** | a man; a grown person | ULD | B | the root sign | L |
| 238 | ***gedh*** | a father | ULD+course | S | the one the line runs from | L |
| 239 | ***tev*** | a child | ULD+bough | S | a young growth | L |
| 240 | ***hemm*** | old; (as a title) Elder | ULD+notch | S | one of many years | L |
| 241 | ***lunt*** | a people, a nation | ULD+three | B | many persons | L |
| 242 | ***covv*** | a cloak | ULD+cope | B | what is laid over a man | L |
| 243 | ***hass*** | a son | ULD+lone | B | one of the hearth's own | R |
| 244 | ***besk*** | a stranger, one from beyond | ULD+rim | S | one from past the edge | R |
| 245 | ***saevul*** | one who keeps the rolls, a clerk | ULD+cut | B | the man of the cut letters | R |
| 246 | ***stidor*** | a herald, one who cries news | ULD+zig | B | the man with the voice | R |
| 247 | ***dhaker*** | one bereft: an orphan, a widow | ULD+fade | S | one whose hearth went dark | R |
| 248 | ***misk*** | the foot | ULD+still | S | where a man stands | R |
| 249 | ***derd*** | a bone | ULD+pale | S | the white of a man | R |

**LUMM** (the Kneel (\*roθ-); 8 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 250 | ***lumm*** | kneel | LUMM | B | the root sign | L |
| 251 | ***mardh*** | God (used of nothing else) | LUMM+cope | B | the One over all, knelt to | L |
| 252 | ***ammel*** | pray | LUMM+zig | S | kneeling, with breath | L |
| 253 | ***ternil*** | a rite, a thing done in order | LUMM+course | S | kneeling in order | R |
| 254 | ***peness*** | holy, set apart | LUMM+lone | S | set apart to kneel before | R |
| 255 | ***grumar*** | the high dwelling, heaven | LUMM+rim | B | above the kneeling | R |
| 256 | ***ferr*** | bow, bend low | LUMM+turn | S | a kneeling turn | R |
| 257 | ***nestorn*** | humble, low-set | LUMM+still | B | kneeling at rest | R |

**LUNN** (the Gap (\*onn-); 6 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 258 | ***lunn*** | freedom | LUNN | B | the root sign | L |
| 259 | ***pondul*** | empty | LUNN+gap | B | the arch with nothing in it | R |
| 260 | ***ranner*** | a going-out, a sortie | LUNN+wedge | S | a blow through the gate | R |
| 261 | ***hollar*** | flee | LUNN+course | B | going out through the arch | R |
| 262 | ***villur*** | yield, give oneself up | LUNN+fade | B | freedom gone dark | R |
| 263 | ***haethil*** | a truce, a peace made | LUNN+still | S | the arch at rest | R |

**VENN** (the Whole (\*weinn-); 14 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 264 | ***venn*** | true; plumb; faithful | VENN | S | the root sign | L |
| 265 | ***tunn*** | whole, complete | VENN+cope | B | true and closed over | L |
| 266 | ***clenn*** | new; (v.) make new, mend | VENN+turn | S | made true again | L |
| 267 | ***gell*** | good | VENN+still | S | true at rest | L |
| 268 | ***sell*** | long | VENN+course | S | a line hung long | L |
| 269 | ***strom*** | great | VENN+rim | B | true to the edge | L |
| 270 | ***lyss*** | small | VENN+lone | S | one, and slight | L |
| 271 | ***ulvenn*** | inner | VENN+cup | S | true within | L |
| 272 | ***duss*** | hard | VENN+wedge | B | true under the blow | R |
| 273 | ***gess*** | sure | VENN+star | S | true, and seen | R |
| 274 | ***dath*** | evil, ill | VENN+fork | B | the plumb broken | R |
| 275 | ***saed*** | half | VENN+gap | S | the line with a gap | R |
| 276 | ***mest*** | much, many | VENN+three | S | true many times | R |
| 277 | ***crystil*** | old (of things), worn | VENN+fade | S | the true line worn dim | R |

**KYL** (the Turn (\*neθ-); 6 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 278 | ***kyl*** | change | KYL | S | the root sign | L |
| 279 | ***marr*** | shift, move to another place | KYL+course | B | a change of place | L |
| 280 | ***omm*** | fall | KYL+rim | B | turned over the edge | L |
| 281 | ***drig*** | throw | KYL+wedge | S | a turn with force | R |
| 282 | ***grik*** | catch | KYL+cup | S | a turn that holds | R |
| 283 | ***gyst*** | climb | KYL+lone | S | one turn upward | R |

**GANNA** (the Door (\*gann-aʔ), kept whole; 7 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 284 | ***ganna*** | a gate | GANNA | B | the root sign | L |
| 285 | ***gann*** | a post, an upright | GANNA+lone | B | one post of the two | L |
| 286 | ***vysul*** | a threshold | GANNA+still | B | the still stone under the gate | R |
| 287 | ***crernil*** | an arch | GANNA+rim | S | a gate with a pointed head | R |
| 288 | ***heskal*** | a bridge, a span | GANNA+course | B | a gate laid along | R |
| 289 | ***roskur*** | a key; to lock | GANNA+cup | B | what holds the gate | R |
| 290 | ***vestul*** | a chest | GANNA+cope | B | posts and a lid | R |

**LODH** (the Bed (\*loð-); 10 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 291 | ***lodh*** | mortar; the mortar line; the bond | LODH | B | the root sign | L |
| 292 | ***rhyn*** | set fast (of mortar), take hold | LODH+cope | S | mortar closed and kept | L |
| 293 | ***trun*** | ground | LODH+still | B | the bed at rest | L |
| 294 | ***gunn*** | deep; the deep | LODH+fade | B | the bed going down into the dark | L |
| 295 | ***gaed*** | dry land | LODH+lone | S | one bed out of the water | R |
| 296 | ***tuss*** | dust | LODH+three | B | the bed crumbled | R |
| 297 | ***pask*** | dig | LODH+cut | B | cutting into the bed | R |
| 298 | ***myger*** | a shaft cut down | LODH+course | S | a line cut down through the bed | R |
| 299 | ***demull*** | a low place, a hollow | LODH+cup | B | the bed that holds | R |
| 300 | ***spenn*** | mud | LODH+zig | S | the bed breathing water | R |

**WADH** (the Course (\*trenn-), running on; 17 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 301 | ***wadh*** | the sea | WADH | B | the root sign | L |
| 302 | ***myst*** | sea-fog; the grey; (adj.) grey | WADH+fade | S | the sea gone dim | L |
| 303 | ***hyll*** | a tide | WADH+turn | S | the sea turning | L |
| 304 | ***rhull*** | a river | WADH+course | B | water going on in a line | L |
| 305 | ***sedh*** | a fen | WADH+still | S | still water in the ground | L |
| 306 | ***nell*** | an islet | WADH+lone | S | one land in the water | L |
| 307 | ***frenn*** | frost, rime | WADH+pale | S | water gone white | L |
| 308 | ***crest*** | ice | WADH+cope | S | water capped | L |
| 309 | ***grull*** | sand | WADH+three | B | the sea's many grains | L |
| 310 | ***orrow*** | the Shore; the Shorelands | WADH+rim | B | the sea's edge | L |
| 311 | ***fodh*** | a wave | WADH+zig | B | the sea's breath | R |
| 312 | ***nerdess*** | a storm at sea | WADH+fork | S | the sea breaking | R |
| 313 | ***dhysal*** | shingle, the stony beach | WADH+star | B | the bright stones the sea leaves | R |
| 314 | ***fimm*** | drink | WADH+cup | S | water held | R |
| 315 | ***ridh*** | wash | WADH+gap | S | water through an open hand | R |
| 316 | ***spant*** | surf, breaking water | WADH+wedge | B | the sea's blow | R |
| 317 | ***tant*** | salt | WADH+drop | B | the sea's taste in the blood | R |

**BRUNN** (the Rim (\*enθ-), stood on the bed; 10 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 318 | ***brunn*** | a mountain | BRUNN | B | the root sign | L |
| 319 | ***sorth*** | a ridge | BRUNN+rim | B | the mountain's edge | L |
| 320 | ***sulv*** | snow; (adj.) white | BRUNN+pale | B | the white of the peaks | L |
| 321 | ***hiskenn*** | a pass through mountains | BRUNN+gap | S | the gap between the peaks | R |
| 322 | ***gynt*** | a crag | BRUNN+lone | S | one peak | R |
| 323 | ***gint*** | a cliff | BRUNN+cut | S | the mountain cut sheer | R |
| 324 | ***nenth*** | a valley | BRUNN+cup | S | what the mountains hold | R |
| 325 | ***susk*** | high | BRUNN+cope | B | at the top | R |
| 326 | ***vimm*** | low | BRUNN+still | S | at the foot, at rest | R |
| 327 | ***henth*** | a cloud | BRUNN+zig | S | the breath on the peaks | R |

**FORE** (the Fore (\*re-il), kept whole; 1 signs)

| no. | reads | sense | sign | cl. | why | src |
|---|---|---|---|---|---|---|
| 328 | ***hosast*** | first | FORE | B | the Fore: first; before all | L |


![All the word-signs, 1](orrowen/shots/ws_all_00.png)
![All the word-signs, 2](orrowen/shots/ws_all_01.png)
![All the word-signs, 3](orrowen/shots/ws_all_02.png)
![All the word-signs, 4](orrowen/shots/ws_all_03.png)
![All the word-signs, 5](orrowen/shots/ws_all_04.png)
![All the word-signs, 6](orrowen/shots/ws_all_05.png)

*`wf7/orrowen/shots/ws_all_00.png` to `ws_all_05.png`: every word-sign, in inventory order, drawn in the cut with its footing.*

### 7.8 When a word is written by word-sign, by letters, or by both

| Written | When | Examples |
|---|---|---|
| **by word-sign** | the word is in §7.7 and stands in its bare form (a singular noun; a verb's 3rd-person or imperative singular; an adjective) | [HALD] *hald*; [TOLM] [TOLM] "stone upon stone" |
| **by word-sign and letters** (a complement) | the word is in §7.7 and carries an ending the order cannot supply (§3.11 D5) | [TUM]**A r** *Tumar*; [THELD]**A th** *theldeth*; [TRESK]**a n** *Treskan*; [PAR]**d** *pard* |
| **by letters** | a name of a person or a pair; a word not in §7.7; a loan or a Mystaeri name; a number (capped numeral letters); and **every word of a vow** (D9) | =**h a l y n a**; **p a n a** "both"; the Stonwryt |
| **left out** | a mortar word (§3.11 D2) | *et, eth, ul, lo, re, es, ol …* |
| **by the turned stone** | *nath, nel, new, na-* | [NOT][BRODH]**A t** *nawrodhat*, untold |

**Adding a word-sign later.** A new word-sign is a head and a crown not yet used together, chosen so that the crown's sense (§7.5) turns the head's field (§7.4) toward the word; it is added to §7.7 with its reason, and the checks of §7.9 are re-run. 239 head-and-crown pairs are still free.

### 7.9 The checks

Run by `wf7/orrowen/wordstones.py` and `ws_chart.py` (the results are the ones printed here):

- **Every sign is unique**: no two of the 328 share a head and a crown, and no reading is used twice.
- **Every sign stands on the bed and keeps its joints**: all 328 lie within the 4.4 × 4.6 cell, each has a stroke on y = 0, and no two strokes of one sign that do not touch come closer than 0.45 u, in the root form and in the pressed form of every head.
- **Every reading is a real word of the tongue**: each of the 134 L readings is an entry of the wf6 lexicon, and each of the 194 R readings is a reserve form of `ancestor.md` §3.3, spelled as that file computes it. The harmony class is computed from each word by §2.2.
- **No sign is a letter**: word-signs are 4.2 or 4.6 u tall and stand on a footing; no letter is taller than 3 u.
- **The look-alike screen** (§13.3) was run on every head, every sign and the turned stone.

### 7.10 What the word-signs give the Book

- **Every inscription can now be economical and true.** A lintel, a capstone, a marker, the coin: each can carry a real dry-cut line of a few signs.
- **The Stonwryt coin** gets a legend at last (inventory D4.18 had none): the vow's last clause and its gate, cut dry, round the rim: [SOMM] [TOLM] [TOLM] ⟨gate⟩, "while stone is stone. It stands." **[Jack]**
- **The granite Book** that Halyna mean to cut "when there is peace enough" would be cut dry: a third of the ink.
- **Kinship a decoder can find.** The stone's word-signs are the same first marks as the grain's signs, worn the other way: the dry cut's TUM (the Cup, "remember") is the grain's HOLD; its SCETH (the Bough, "a hull") is the grain's HULL; its LUNN (the Gap) is the grain's BREATH. Nothing in the Book says so (`ancestor.md` §1.7).

---

## 8 · THE LEAF-HAND (*GARL FLENN*): THE RUNNING INK

### 8.1 The picture in one paragraph

The leaf-hand is **the course-hand written, not cut**: the same letters, the same uprights and laid stones, the same pins and pinnings, but each letter made in **one movement of the pen**, the whole hand **slanted** and **joined**. The pen goes up the letter's upright from the line and lays its stones rightward; the voicing pin, which the chisel cut as a separate short post, becomes a **second leg** that brings the pen back to the line; a free stone is a quick **touch** set after; and a **hairline** carries the pen along the line from each letter to the next. A reader of the course-hand can read the leaf-hand at sight: every letter keeps its upright (forward, stepped, back), its stones at their heights, its pin. It writes **the whole tongue**, every mortar word and every mutation, as fast as a hand can move: Jack's "written quickly like English, if the smaller words were included".

![The leaf-hand](orrowen/shots/leaf_sheet.png)

*`wf7/orrowen/shots/leaf_sheet.png`: the leaf-hand's letters (drawn by `leafhand.py`). Rows: p b m f v w · t d n th dh s l r rh · k g h ŋ hw x · a o u e i y A O · perpend, wedge, gate, coping.*

### 8.2 The pen's laws

| Law | | What happens |
|---|---|---|
| **F1** | One movement to a letter. | Each letter begins on the line at its upright's foot, goes up the upright, and lays its joined stones rightward in order. A stone that sits below the top is reached by coming back down the upright (a retrace, which the nib leaves as one thick line). |
| **F2** | The pin becomes a leg. | A voiced letter's last stone turns down at its end (0.12 u on, 0.2 u down) and runs to the line: voiced letters stand on two feet. The ink voices every stop and every breath this one way, so *v* is *f* with a leg and *dh* is *th* with a leg (the reform's short top stone of the cut *v* and *dh* is not written). |
| **F3** | The step is taken at speed. | The offset's step becomes a short jog: (0, 1.35) → (0.5, 1.65). |
| **F4** | The stones are shortened. | An ink letter is the cut letter at 0.55 of its width: a full stone ends at 2.2 u, a short one at 1.32, a free one runs 1.595 → 2.2. |
| **F5** | A free stone is a touch, set after, or the pen travels to it. | The top stones of *s*, *rh* and Hal *hw* are ticks laid after the letter; the low stone of *w*, *l* and Hal *x* is reached by a hairline from the short top stone, and laid thick. |
| **F6** | A pinning is made in one touch. | Each vowel's pin and stone are joined (§8.4); the harmonic letters' broken capstone becomes a **dip** in the capstone. |
| **F7** | The pen runs on. | Every letter leaves the line at its advance, and a hairline takes the pen from its last stroke to that point, so the next letter begins where this one ends. No contextual forms are needed: the joins are in the letters. |
| **F8** | The hand leans. | Every point (x, y) is drawn at (x + 0.18 y, y). The prop then leans hard forward, the offset a little forward with its jog, and the shore a little back, so the three places stay three. |
| **F9** | Corners soften. | Each interior corner of a nib stroke is rounded (radius 0.32 u, or 0.45 of the shorter arm) before the nib is swept along it. |

### 8.3 Metrics

| Measure | Value |
|---|---|
| **pen unit** | 1 u; for a font, **1 u = 180 units at 1000 UPM** |
| **heights** | consonants 3 u; vowels 2 u; the ruled line at 0 |
| **the nib** | a flat nib **0.30 u wide held at 25°**; a nib stroke's area is the union of the nib's sweep along each segment of its rounded centre-line (for each segment, the convex hull of the nib's two ends at both points) |
| **the hairline** | a round pen 0.07 u wide |
| **the slant** | x′ = x + 0.18 y, applied after rounding |
| **bites** | the §6.5 bites, drawn at 0.75 of the nib, hanging under the letter's foot in y ∈ [−1.05, −0.55]; the foot is 0.05 u for prop and offset letters, 1.0 u for shore letters, 0.15 u for vowels |
| **sealing lintel, numeral caps** | a nib stroke at 0.75 at y = 3.45 over the pair-name, or over each numeral letter |
| **word space** | 1.3 u; after a perpend or wedge 0.9 u (the mark is set 0.5 u back into the space) |
| **line pitch** | 5.4 u |
| **ascent, descent (font)** | 820 and −260 units |

### 8.4 The letters, and where each comes from

Each letter is drawn from its cut form in §6.4 by the laws above. The table gives the ink letter's structure; §8.5 gives its exact centre-lines.

| Letter | Upright (F1, F3, F8) | Stones (F1, F4, F5) | Pin (F2) | Leaves the letter by |
|---|---|---|---|---|
| **p · b** | prop, (0,0) → (0.66,3) | top, to 2.2 | b: the leg | p: a hairline falling from the stone's end; b: the leg, then along the line |
| **m** | prop | back to 2, middle, to 2.2 | — | a hairline from the stone |
| **f · v** | prop | back to 1, low, to 2.2 | v: the leg | f: a hairline; v: the leg |
| **w** | prop | top short to 1.32; a hairline to the low stone, 1.595 → 2.2 | — | a hairline from the low stone |
| **t · d** | offset, with its jog | top, to 2.2 | d: the leg | t: a hairline; d: the leg |
| **n** | offset | back to 2, middle, to 2.2 | — | a hairline |
| **th · dh** | offset | back to 1, low, to 2.2 | dh: the leg | th: a hairline; dh: the leg |
| **s** | offset | back to 1, low short to 1.32; the top stone a touch after | — | a hairline, then the touch |
| **l** | offset | as w | — | a hairline |
| **r · rh** | offset | back to 2, middle short to 1.42 | the leg | the leg; rh then the top stone as a touch |
| **k · g** | shore, (1,0) → (0,3), reached along the line | top, to 2.2 | g: the leg | k: a hairline; g: the leg |
| **h** | shore | back to 1, low, to 2.2 | — | a hairline |
| Hal **ŋ · hw · x** | shore · prop · shore | middle · as s · as w | — | as n · s · w (for quoting the Hal in ink) |
| **a** | the pin on the left, up into the capstone | capstone to 1.2 | | a hairline from the capstone |
| **o** | a hairline up to the capstone's left end | capstone, then down the right pin | | along the line |
| **u** | the left pin, up into the keystone | keystone, then down the right pin | | along the line |
| **e** | the tall pin on the left, up to 2 and back to 1 | low stone to 1.2 | | a hairline |
| **i** | a hairline to the low stone | low stone; a hairline up to the tall pin on the right, and down it | | along the line |
| **y** | the leaning pin, up to 2 and back to 1 | low stone to 1.2 | | a hairline |
| **A · O** | as a · as o | the capstone **dipped** 0.45 u where the cut breaks it | | as a · as o |

**Every letter can be told from every other.** Place is the upright's lean (after the slant: hard forward, gently forward with a jog, a little back); manner is the height of the stone and whether it is full, short or a touch; voicing is the second leg. No two letters have the same centre-lines; the closest pairs on the look-alike screen are *a*/*A* and *o*/*O*, told apart by the dip, and *b*/*d*, told apart by the lean and the jog (§13.3).

### 8.5 The table (centre-lines)

Each glyph is `{"adv": advance, "strokes": [{"pen": "nib" | "hair", "pts": [[x, y], ...]}]}` in pen units, **upright** (before F8's slant and F9's rounding, which a font builder applies), with its entry at (0, 0) and its exit at (adv, 0). This is the whole of what a font needs; §8.8 built one from it.

```json
{
 "metrics": {"unit":"u (pen unit)","consonant_height":3,"vowel_height":2,"nib":{"width":0.3,"angle_deg":25.0},"hair":0.07,"round":0.32,"slant":0.18,"lintel_y":3.45,"bite_band":[-1.05,-0.55],"space":1.3,"font_unit":"1 u = 180 at 1000 UPM"},
 "foot_x": {"prop":0.05,"offset":0.05,"shore":1.0,"vowel":0.15},
 "letters": {
  "p": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[2.2,3.0]]},{"pen":"hair","pts":[[2.2,3.0],[2.65,0.0]]}]},
  "b": {"adv":2.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[2.2,3.0],[2.32,2.8],[2.32,0.0]]},{"pen":"hair","pts":[[2.32,0.0],[2.77,0.0]]}]},
  "m": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[0.44,2.0],[2.2,2.0]]},{"pen":"hair","pts":[[2.2,2.0],[2.65,0.0]]}]},
  "f": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[0.22,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "v": {"adv":2.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[0.22,1.0],[2.2,1.0],[2.32,0.8],[2.32,0.0]]},{"pen":"hair","pts":[[2.32,0.0],[2.77,0.0]]}]},
  "w": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[1.32,3.0]]},{"pen":"hair","pts":[[1.32,3.0],[1.595,1.0]]},{"pen":"nib","pts":[[1.595,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "t": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[2.2,3.0]]},{"pen":"hair","pts":[[2.2,3.0],[2.65,0.0]]}]},
  "d": {"adv":2.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[2.2,3.0],[2.32,2.8],[2.32,0.0]]},{"pen":"hair","pts":[[2.32,0.0],[2.77,0.0]]}]},
  "n": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.5,2.0],[2.2,2.0]]},{"pen":"hair","pts":[[2.2,2.0],[2.65,0.0]]}]},
  "th": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.0,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "dh": {"adv":2.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.0,1.0],[2.2,1.0],[2.32,0.8],[2.32,0.0]]},{"pen":"hair","pts":[[2.32,0.0],[2.77,0.0]]}]},
  "s": {"adv":1.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.0,1.0],[1.32,1.0]]},{"pen":"hair","pts":[[1.32,1.0],[1.77,0.0]]},{"pen":"nib","pts":[[1.595,3.0],[2.2,3.0]]}]},
  "l": {"adv":2.65,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[1.32,3.0]]},{"pen":"hair","pts":[[1.32,3.0],[1.595,1.0]]},{"pen":"nib","pts":[[1.595,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "r": {"adv":1.99,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.5,2.0],[1.42,2.0],[1.54,1.8],[1.54,0.0]]},{"pen":"hair","pts":[[1.54,0.0],[1.99,0.0]]}]},
  "rh": {"adv":1.99,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.0,1.35],[0.5,1.65],[0.5,3.0],[0.5,2.0],[1.42,2.0],[1.54,1.8],[1.54,0.0]]},{"pen":"hair","pts":[[1.54,0.0],[1.99,0.0]]},{"pen":"nib","pts":[[1.595,3.0],[2.2,3.0]]}]},
  "k": {"adv":2.65,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[1.0,0.0]]},{"pen":"nib","pts":[[1.0,0.0],[0.0,3.0],[2.2,3.0]]},{"pen":"hair","pts":[[2.2,3.0],[2.65,0.0]]}]},
  "g": {"adv":2.77,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[1.0,0.0]]},{"pen":"nib","pts":[[1.0,0.0],[0.0,3.0],[2.2,3.0],[2.32,2.8],[2.32,0.0]]},{"pen":"hair","pts":[[2.32,0.0],[2.77,0.0]]}]},
  "h": {"adv":2.65,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[1.0,0.0]]},{"pen":"nib","pts":[[1.0,0.0],[0.0,3.0],[0.667,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "ŋ": {"adv":2.65,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[1.0,0.0]]},{"pen":"nib","pts":[[1.0,0.0],[0.0,3.0],[0.333,2.0],[2.2,2.0]]},{"pen":"hair","pts":[[2.2,2.0],[2.65,0.0]]}]},
  "hw": {"adv":1.77,"strokes":[{"pen":"nib","pts":[[0.0,0.0],[0.66,3.0],[0.22,1.0],[1.32,1.0]]},{"pen":"hair","pts":[[1.32,1.0],[1.77,0.0]]},{"pen":"nib","pts":[[1.595,3.0],[2.2,3.0]]}]},
  "x": {"adv":2.65,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[1.0,0.0]]},{"pen":"nib","pts":[[1.0,0.0],[0.0,3.0],[1.32,3.0]]},{"pen":"hair","pts":[[1.32,3.0],[1.595,1.0]]},{"pen":"nib","pts":[[1.595,1.0],[2.2,1.0]]},{"pen":"hair","pts":[[2.2,1.0],[2.65,0.0]]}]},
  "a": {"adv":1.6,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.15,0.0]]},{"pen":"nib","pts":[[0.15,0.0],[0.15,1.6],[0.35,2.0],[1.2,2.0]]},{"pen":"hair","pts":[[1.2,2.0],[1.6,0.0]]}]},
  "o": {"adv":1.5,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.1,2.0]]},{"pen":"nib","pts":[[0.1,2.0],[0.95,2.0],[1.15,1.7],[1.15,0.0]]},{"pen":"hair","pts":[[1.15,0.0],[1.5,0.0]]}]},
  "u": {"adv":1.6,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.1,0.0]]},{"pen":"nib","pts":[[0.1,0.0],[0.1,1.3],[0.45,1.9],[0.9,1.9],[1.25,1.3],[1.25,0.0]]},{"pen":"hair","pts":[[1.25,0.0],[1.6,0.0]]}]},
  "e": {"adv":1.6,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.15,0.0]]},{"pen":"nib","pts":[[0.15,0.0],[0.15,2.0],[0.15,1.0],[1.2,1.0]]},{"pen":"hair","pts":[[1.2,1.0],[1.6,0.0]]}]},
  "i": {"adv":1.45,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.0,1.0]]},{"pen":"nib","pts":[[0.0,1.0],[0.8,1.0]]},{"pen":"hair","pts":[[0.8,1.0],[1.05,2.0]]},{"pen":"nib","pts":[[1.05,2.0],[1.05,0.0]]},{"pen":"hair","pts":[[1.05,0.0],[1.45,0.0]]}]},
  "y": {"adv":1.6,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.1,0.0]]},{"pen":"nib","pts":[[0.1,0.0],[0.6,2.0],[0.35,1.0],[1.2,1.0]]},{"pen":"hair","pts":[[1.2,1.0],[1.6,0.0]]}]},
  "A": {"adv":1.6,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.15,0.0]]},{"pen":"nib","pts":[[0.15,0.0],[0.15,1.6],[0.35,2.0],[0.55,2.0],[0.72,1.55],[0.89,2.0],[1.2,2.0]]},{"pen":"hair","pts":[[1.2,2.0],[1.6,0.0]]}]},
  "O": {"adv":1.5,"strokes":[{"pen":"hair","pts":[[0.0,0.0],[0.1,2.0]]},{"pen":"nib","pts":[[0.1,2.0],[0.37,2.0],[0.54,1.55],[0.71,2.0],[0.95,2.0],[1.15,1.7],[1.15,0.0]]},{"pen":"hair","pts":[[1.15,0.0],[1.5,0.0]]}]}
 },
 "marks": {
  "|": {"adv":0.9,"strokes":[{"pen":"nib","pts":[[0.25,0.0],[0.25,1.6]]}]},
  ",": {"adv":1.05,"strokes":[{"pen":"nib","pts":[[0.15,1.0],[0.8,1.0]]}]},
  "#gate": {"adv":2.0,"strokes":[{"pen":"nib","pts":[[0.2,0.0],[0.2,2.2],[1.6,2.2],[1.6,0.0]]}]},
  "#coping": {"adv":2.0,"strokes":[{"pen":"nib","pts":[[0.2,0.0],[0.2,2.2],[1.6,2.2],[1.6,0.0]]},{"pen":"nib","pts":[[-0.15,2.85],[1.95,2.85]]}]},
  "'": {"adv":0.8,"strokes":[{"pen":"nib","pts":[[0.1,1.0],[0.55,1.0]]}]}
 },
 "bites": {"S":{"scale":0.75,"strokes":[{"pen":"nib","pts":[[-0.2,-0.55],[0.0,-1.05],[0.2,-0.55]]}]},"N":{"scale":0.75,"strokes":[{"pen":"nib","pts":[[-0.2,-0.55],[-0.2,-1.0],[0.2,-1.0],[0.2,-0.55]]}]}}
}
```

### 8.6 Marks, bites, lintels, numerals

- **The perpend** is a short downstroke 1.6 u, **the wedge** a short laid stroke at 1, **the gate** one movement up, across and down, **the coping** the gate with a stroke over it. **The knock** (in a Mystaeri name) is a short stroke at 1 inside the word.
- **The bites** are written as in the cut, small, under the letter's foot: the softening bite a V, the nasalising bite a square cup. In a font they are zero-width marks that follow their letter.
- **The sealing lintel** is a stroke at y = 3.45 over the pair-name; **numeral caps** are one short stroke over each numeral letter, broken between letters (§6.8).
- Numbers are the capped numeral letters of §6.8, written in the running hand.

### 8.7 The two inks

Halyna's tellings alternate their two inks by paragraph (Legends N6). In antiphony (the Cry, the guild's word) the ink changes at the wedge: the renderer's `ink2` option does this. Seren's own notes, and every leaf that is not Halyna's, are in her one ink.

### 8.8 A font, built as a proof

`wf7/orrowen/leafhand.py font` builds **`wf7/fonts/garl_flenn_proof.ttf`** from the table alone, with fontTools (`wf7/venv`): 38 glyphs, each letter's outline the union of its nib and hairline sweeps (convex polygons, clockwise, overlapping, filled non-zero), the bites as zero-width marks. Its letters sit in the Private Use Area (U+E000 on; `leafhand.PUA`). Text set in it in Chrome is **identical to the SVG renderer's drawing** of the same tokens (`wf7/orrowen/shots/font_proof.png`). It is a proof that the table is buildable, not a release font: a release font would merge the overlapping contours, add a GSUB feature mapping the Book's romanisation (with *th*, *dh*, *rh* and the harmonic letters) to the glyphs, and draw the lintel as a contextual mark.

![The proof font beside the renderer](orrowen/shots/font_proof.png)

### 8.9 How fast it is

Speed is how often the pen is lifted. `leafhand.movements()` counts one for every stroke that does not begin where the pen already is, one for every bite, lintel and mark:

| Text | Letters and marks | Pen movements | Letters per movement |
|---|---|---|---|
| The Title of Liberty | 48 | 20 | 2.4 |
| The Cry of the Bonded | 92 | 39 | 2.4 |
| The hearth's answer | 6 | 2 | 3.0 |
| Seren's untold note | 41 | 20 | 2.0 |
| The Captain's three calls | 32 | 17 | 1.9 |
| The Stonwryt | 55 | 36 | 1.5 |
| The saying both peoples share | 23 | 14 | 1.6 |
| The Invocation's close | 42 | 22 | 1.9 |

A word whose letters all end on the line is written without lifting the pen at all: ***Tumar*** is one movement, *t-u-m-A-r*, and the perpend is the second.

---

## 9 · WHERE EACH HAND IS USED

**The rule of choice.** *If it is cut, it is cut dry; if it is written, it is written whole; a vow and a name are always letters.*

| Surface | Hand | Why |
|---|---|---|
| the Book, every leaf, Seren's notes, the Book of Knowings' Shoreland lines | **leaf-hand** | "This Book is ink" (foreword) |
| the archive rolls, the Stonewrights' warning, the warden's report | leaf-hand (haven spellings) | ink |
| the Title of Liberty on the cloak and the capstones | **coal**, letters, every word | the Captain wrote it; he knew no word-signs |
| the tale-stone's Stonwryt; the Captain's Stonwryt under the new capstone | **letters, whole** (the Hal; the living cut) | a vow is cut whole (D9) |
| the slate leaves of the Rite; the old lintels; the top of the lintel column (other than names) | **the Hal's dry cut** | the first builders' economy (§4.2) |
| the names on the lintel of the western stair | letters (Hal, haven, living) | a name is said, not meant |
| the mark on the black chest | the **foremark** (the Fore, in the Hal's cut) | `ancestor.md` §1.7 (1) |
| new capstones, works, markers, a Stonwryt cited on a finished work | **dry cut** | the chisel's economy |
| the Stonwryt coin | dry cut, round the rim (§7.10) | a coin has room for four signs **[Jack]** |
| the Book "cut into the granite of this hall when there is peace enough" | dry cut | the foreword; not a surface of the game |
| the Stone out of the Grey (the Epilogue) | the Last Carver's **letters**, every word, cut | he learned from the coal; his fifth tell (§6.13) |
| the soft letters of the mute stones | the Mystaeri designer's; they spell Orrowen by sound | §14a |

---

## 10 · READING, UNLOCKING, AND THE TABS

- **The leaf-hand is the living course-hand, written.** It needs no rung of its own: the rung that teaches the living letters (*The Mortar Line*, Cam 1 complete, V.1) teaches both, and the Tongues doc should show each letter cut and written side by side. Seren's note, which that rung translates, is now **drawn in the leaf-hand** (she wrote it in ink), and every ink leaf of tier 3 is in it.
- **The dry cut needs the word-sign list.** Proposed: the list of heads and crowns (§7.4, §7.5) enters the codex with *The Mortar Line* too, since the Title's own economy (§11.1) is the first thing a player can compare; each word-sign's reading is added to the codex the first time the player earns a leaf whose translation uses its word. Every dry-cut line is then decodable by rule, as "truth or nothing" requires **[Jack]**.
- **The Hal** stays behind *The Bedrock Hand* (Cam 16), with Halyna's living readings arriving earlier, as before. The Hal's word-signs are the living ones mirrored, so a player who knows the dry cut can recognise them and still cannot sound the Hal.
- **The three tabs (Jack's note 3): The Book | Plain Words | Original.** A locked leaf shows its own hand under all three. An earned leaf adds its translation under The Book and Plain Words; **Original** shows the leaf-hand facing the Book's translation, for decoders, and any inscription the leaf quotes in the dry cut beside its leaf-hand transcription. Nothing is ever removed (law 7).
- **Display rules** are §6.15, unchanged: a locked drawing's accessible title never leaks its English.

---

## 11 · SAMPLE TEXTS, IN BOTH REGISTERS

Each text is given: the Orrowen, as the Book spells it; the interlinear gloss; the translation; **the leaf-hand** (and the coal, for the Title), as a `render_shore.py` token string (letters separated by `.`, `^S`/`^N` bites, `A`/`O` harmonic letters, `,` wedge, `|` perpend, `#gate`, `=` lintel), which `leafhand.py` writes and the cut renderer cuts; and **the dry cut**, as a `drycut.py` token string:

- `@word` is the word-sign whose reading is *word* (§7.7), `@a@b` two word-signs on one bed, `+A.th` its complement letters;
- `!` before a stone is the turned stone (not);
- a word in letters is written as in the leaf-hand tokens, `=` lays the sealing lintel, `%h` is a capped numeral letter;
- `,` `|` `#gate` are the wedge, the perpend and the gate.

The counts are **signs** for the dry cut (word-signs, letters, marks) and **letters and marks** for the leaf-hand, with its **pen movements** (§8.9). All texts are in `wf7/orrowen/samples_v2.py`; the review sheet is below.

![The samples, cut dry and written](orrowen/shots/samples_v2.png)

*`wf7/orrowen/shots/samples_v2.png`: each text cut dry (above) and in the leaf-hand (below).*

### 11.1 The Title of Liberty (*Hosk Lunn*)

Written by the Captain in coal on the torn cloak.

> **Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.**

| Ul | dumol | ol | varn, | ol | theldeth, | ol | Mardh, | ol | lunnath, | ol | sollan. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| in(+N) | N·memory | our(+N) | home | our | family-PL | our | God | our | freedom-PL | our | peace |

*In memory of our home, our families, our God, our freedoms, our peace.*

```
u.l t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th , o.l m.a.r.dh , o.l l.u.n.n.A.th , o.l s.o.l.l.a.n |
```

- ***dumol* has no article.** It is the head of a construct, and its possessors are definite (§3.2). "In memory of" is article-less by grammar, which is what makes the Last Carver's extra word an error (§11.9).
- **The nasal bite under the T** is the Title's only visible mutation. *Ul* ("in") beds the *t* of *tumol* into a *d*.
- ***theldeth* and *lunnath* end in the same two letters**, read two ways (harmony, §6.4).
- **Five possessed nouns, five *ol*:** "five things a man might die for".
- **In the coal hand** (§6.10) the Title has no bed band. It is 43 letters and 5 marks.
- **The Title uses 16 distinct letters:** the 14 full letters *u l t m o v a r n th e d dh s* and the two harmonic letters *A O*, plus the N bite. Everything the Last Carver cut must come from these.

**Written.** The Captain's coal and Seren's leaf-hand write the same token string above, every word: **48 letters and marks**; the leaf-hand joins them in **20 pen movements**. The coal is unjoined, "as a man writes who has not written much".

**Cut dry: 17 signs** (35% of the written line):

```
@tum+O.l @varn , @theld+A.th , @mardh , @lunn+A.th , @sollan |
```

| [TUM] O l | [VARN] , | [THELD] A th , | [MARDH] , | [LUNN] A th , | [SOLLAN] \| |
|---|---|---|---|---|---|
| memory | home | families | God | freedoms | peace |

*Memory: home, families, God, freedoms, peace.* The five things stand; the six mortar words (*ul* and five *ol*) are the reader's. It is how the guild would cut the Title over a gate, and it is the Title's own economy: *memory*, and five stones.

### 11.2 The Cry of the Bonded

Rhyna begins, Halvard ends, "one cry in two throats".

> **Carm et lodh hy et trun. Talda, Stonwrytan! Cadha tolm um dholm. Stona gor hald dem et dask sost,**
> **Talda! Talda! Talda!**

| Carm | et | lodh | hy | et | trun. |
|---|---|---|---|---|---|
| cries | the | mortar | from(+S) | the | ground |

| Talda, | Stonwrytan! |
|---|---|
| rise-IMP.PL | Stonewright-folk (VOC) |

| Cadha | tolm | um | dholm. |
|---|---|---|---|
| lay-IMP.PL | stone | upon(+S) | S·stone |

| Stona | gor | hald | dem | et | dask | sost, |
|---|---|---|---|---|---|---|
| stand-IMP.PL | every(+S) | wall | until(+N) | the | end | self |

| Talda! | Talda! | Talda! |
|---|---|---|
| rise-IMP.PL | rise-IMP.PL | rise-IMP.PL |

*The mortar cries out from the ground. Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end. / Rise! Rise! Rise!*

```
k.a.r.m e.t l.o.dh h.y e.t t.r.u.n | t.a.l.d.a , s.t.o.n.w.r.y.t.a.n |
k.a.dh.a t.o.l.m u.m t^S.o.l.m | s.t.o.n.a g.o.r h.a.l.d d.e.m e.t d.a.s.k s.o.s.t ,
t.a.l.d.a t.a.l.d.a t.a.l.d.a |
```

- **The Cry is laid as one course.** Rhyna's last sentence ends in a **wedge, not a perpend**, and Halvard's three words follow in the other ink. The single perpend comes at the very end. "There was no silence" is written into the punctuation.
- ***tolm um dholm*** is the one mutation in it you can hear. *Um* ("upon") softens the second stone.
- **The rhythm** is first-syllable stress throughout: CARM et LODH hy et TRUN · TAL-da, STON-wry-tan · CA-dha TOLM um DHOLM · STO-na gor HALD dem et DASK SOST · TAL-da TAL-da TAL-da.

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **92 letters and marks, 39 pen movements**.

**Cut dry: 29 signs** (32% of the written line):

```
@carm @lodh @trun | @tald+a , @ston@ryt+a.n | @cadh+a @tolm @tolm | @ston+a @hald @dask , @tald+a @tald+a @tald+a |
```

| [CARM] [LODH] [TRUN] \| | [TALD] a , [STON][RYT] a n \| | [CADH] a [TOLM] [TOLM] \| | [STON] a [HALD] [DASK] , | [TALD] a ×3 \| |
|---|---|---|---|---|
| cries mortar ground | rise-PL, Stonewright-folk | lay-PL stone stone | stand-PL wall end | rise-PL ×3 |

*Cries the mortar [from the] ground. Rise, Stonewrights! Lay stone [upon] stone. Stand [every] wall [to the very] end, rise! rise! rise!* The imperative plural is laid on as **a**; *Stonwrytan* is its two stones and **a n**.

### 11.3 The hearth's answer: *Tumar*, yes

> **Tumar.**

| Tumar. |
|---|
| remember-1PL |

*We remember.*

```
t.u.m.A.r |
```

- **The answer is built on the Title's second word.** *dumol* is *tumol* with a nasal bite, and *Tumar* is the same *T* standing bare. "The answer comes from the first words of the Captain's Title."
- **It is also Orrowen's "yes".** A question is answered by repeating its verb (§3.4). Every stone leaf asks, and the hearth says yes.

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **6 letters and marks, 2 pen movements**.

**Cut dry: 4 signs** (67% of the written line):

```
@tum+A.r |
```

| [TUM] A r \| |
|---|
| remember-1PL |

The hearth's yes, cut: the Cup, which holds, and *-ar*, *we*: three signs, and the perpend.

### 11.4 Seren's untold-leaf note

The line Jack asked for. It is written in Seren's single ink, because she is unbonded and has one hand.

> **Nawrodhat. Nath noss tul kethyl et gunn sy lo Halyna.**

| Nawrodhat. |
|---|
| un-S·tell-PTCP |

| Nath | noss | tul | kethyl | et | gunn | sy | lo | Halyna. |
|---|---|---|---|---|---|---|---|---|
| NEG(+N) | N·is | yet | hold-VN | the | deep | this | at(+S) | Halyna |

Literally: *Untold. Not is yet the holding of this deep at Halyna.*

*Untold. Halyna cannot yet hold this deep.*

```
n.a.b^S.r.o.dh.A.t | n.a.th d^N.o.s.s t.u.l k.e.th.O.l e.t g.u.n.n s.y l.o =h.a.l.y.n.a |
```

- **Two mutations in the first two words:**
  - *na-* softens *brodhat* ("told") into *-wrodhat*;
  - *nath* beds *doss* ("is") into *noss*.
- ***keth* is the canon's own verb.** To know the wood is to hold it. "Cannot" is the "at" idiom: *Doss* VN *lo* Y, negated (§3.7).
- ***Halyna* carries its sealing lintel.** It is the only lintel on the page, so a decoder's first question will be "whose name has a gate over it?"
- **On the leaf:** the grain drawn, and this line beneath it in Seren's **leaf-hand** (v2: she wrote it in ink; §10). The accessible title is "A leaf in the course-hand, not yet read".
- **Unlock.** The line translates when earned: proposal, V.1 (Cam 1 complete), or the first milestone achievement **[Jack]**. The leaf itself stays untold until the Epilogue fills it.

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **41 letters and marks, 20 pen movements**.

**Cut dry: 18 signs** (44% of the written line):

```
!@brodh+A.t | !@tul @keth+O.l @gunn =h.a.l.y.n.a |
```

| NOT [BRODH] A t \| | NOT [TUL] [KETH] O l [GUNN] =h a l y n a \| |
|---|---|
| not-told | not yet holding deep, Halyna |

*Untold. Not yet holding the deep, Halyna.* The turned stone cuts both *na-* and *nath*; *noss*, *et*, *sy* and *lo* are laid back in by the reader. Seren herself writes it whole, in the leaf-hand (§10).

### 11.5 The Captain's three calls

The calls are given by horn, to one battery at a time. The Captain speaks to one True Man, as a comrade, in the singular.

> **Marr tho dhrun.** · **Kyl tho vedh.** · **Keth, ell lusk.**

| Marr | tho | dhrun. |
|---|---|---|
| shift-IMP | your(+S) | S·ground |

| Kyl | tho | vedh. |
|---|---|---|
| change-IMP | your(+S) | S·shot |

| Keth, | ell | lusk. |
|---|---|---|
| hold-IMP | or | loose-IMP |

*Shift your ground. · Change your shot. · Hold, or loose.*

```
m.a.r.r th.o t^S.r.u.n | k.y.l th.o p^S.e.dh | k.e.th , e.l.l l.u.s.k |
```

- ***trun* is the wall's idiom for the water a battery watches**, not the stones it stands on. The canon says so, and so does the word.
- **The third call is a formula for a choice.** On the horn it is sounded as one word, *Keth!* or *Lusk!*. *Lusk* ("loose") is the root of *lunn* ("freedom") in speakers' minds, though not in history, and the hearth plays on it.

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **32 letters and marks, 17 pen movements**.

**Cut dry: 10 signs** (31% of the written line):

```
@marr @trun | @kyl @pedh | @keth , @lusk |
```

| [MARR] [TRUN] \| | [KYL] [PEDH] \| | [KETH] , [LUSK] \| |
|---|---|---|
| shift ground | change shot | hold, loose |

*Shift [your] ground. Change [your] shot. Hold, [or] loose.* The calls are horn and voice, not stone; cut, they would be three short lines on a battery's lintel.

### 11.6 The Stonwryt: the vow under the capstone

The canon gives only its sense, "a master's promise that the wall will hold". Here are its words.

**(a) As the first builders cut it**, under the old capstone that is now the tale-stone. It is in the Hal, and in *Garl Hal*: right to left, mirrored, one unbroken course. It is signed with the ligature of *Aldwena*.

> **ESAN STONOS ETAS XALDOS SIU · RE CADHANA OA ETHAS TESSANA OA SOŊMAS ELIS TOLMOS TOLMOS · STONOS** ⟨gate⟩ ⟨**ALD | BEN** under one lintel⟩

| ESAN | STONOS | ETAS | XALDOS | SIU |
|---|---|---|---|---|
| FUT | stand-3SG | the | wall-NOM | this |

| RE | CADHANA | OA | ETHAS | TESSANA | OA |
|---|---|---|---|---|---|
| PST | lay-1DU | it | and | answer-1DU | it |

| SOŊMAS | ELIS | TOLMOS | TOLMOS | STONOS |
|---|---|---|---|---|
| while | is | stone-NOM | stone-NOM | stand-3SG |

**(b) As Halyna say it now** (living Orrowen):

> **Es ston et hald sy. Re hadhan o, eth tessen o, somm el tolm tolm. Ston.**

| Es | ston | et | hald | sy. |
|---|---|---|---|---|
| FUT(+N) | stand | the | wall | this |

| Re | hadhan | o, |
|---|---|---|
| PST(+S) | S·lay-1DU | it |

| eth | tessen | o, |
|---|---|---|
| and | answer-1DU | it |

| somm | el | tolm | tolm. |
|---|---|---|---|
| while | is | stone | stone |

| Ston. |
|---|
| stands |

*This wall will stand. We two laid it, and we two answer for it, while stone is stone. It stands.*

```
e.s s.t.o.n e.t h.a.l.d s.y | r.e k^S.a.dh.A.n o , e.th t.e.s.s.A.n o , s.o.m.m e.l t.o.l.m t.o.l.m | s.t.o.n | #gate
```

**What changed between (a) and (b), which is the lesson of §4 in one vow:**
- the endings fell (*STONOS* > *ston*, *XALDOS* > *hald*);
- old *x* became *h*;
- old *ŋ* went into *somm*;
- the Hal's unwritten softening of *cadhana* became the written bite of *hadhan*;
- the fixed suffix vowels turned harmonic (*TESSANA* > *tessen*).

The Hal line has two of the three archaic letters in it, *x* and *ŋ*.

**The Captain's Stonwryt (I.4)** is the same vow in the living hand, signed **HAL | RHYN** under one lintel. It is "cut where no eye will see it again unless the wall falls" and should stay hidden unless Jack chooses a reveal (inventory D4.6).

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **55 letters and marks, 36 pen movements**.

**Cut dry: 16 signs** (29% of the written line):

```
@ston @hald | @cadh+A.n , @tess+A.n , @somm @tolm @tolm | #gate
```

| [STON] [HALD] \| | [CADH] A n , [TESS] A n , | [SOMM] [TOLM] [TOLM] \| | ⟨gate⟩ |
|---|---|---|---|
| stands wall | lay-1DU, answer-1DU | while stone stone | *Ston* |

The vow **cited**, as it would be cut on the lintel of a finished work or in the rolls: *[This] wall stands. We two laid [it], we two answer [for it], while stone [is] stone. It stands.* The gate is read *Ston* (D9). As sworn under a capstone it is cut whole, in letters: (a) and (b) above.

**Why (a) and (b) are whole.** A vow is cut whole (D9). That is why the first builders' Stonwryt, alone of all their cuttings, can be read word for word, and why `ancestor.md` §1.6 (c) can say it is "cut in the first tongue itself, word for word". The coin's legend (§7.10) is its last clause, cut dry: `@somm @tolm @tolm #gate`.

### 11.7 The saying shared by both peoples

"Harm to one is harm to both": the old masters' saying, and the meaning of the Aelthar.

> **Grest um hos, grest um vana.** (Hal: *GRESTOS UMO HOSOS GRESTOS UMO PANĀ*, with the long-stone on the last vowel)

| Grest | um | hos, | grest | um | vana. |
|---|---|---|---|---|---|
| harm | upon(+S) | one | harm | upon(+S) | S·both |

*Harm to one is harm to both.* Literally: "Harm upon one, harm upon both."

```
g.r.e.s.t u.m h.o.s , g.r.e.s.t u.m p^S.a.n.a |
```

- **The proverb is verbless**, as Orrowen proverbs are.
- **It is split at the wedge** for two voices.
- **Contact point for the Grain designer:** the Aelthar's carving should gloss to exactly this line (§14).

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **23 letters and marks, 14 pen movements**.

**Cut dry: 9 signs** (39% of the written line):

```
@grest %h , @grest p.a.n.a |
```

| [GREST] %h , | [GREST] p a n a \| |
|---|---|
| harm one | harm both |

*Harm [upon] one, harm [upon] both.* *hos* is the capped numeral **h**; *pana* has no word-sign and is cut in letters.

**The Hal's cut of it** (the most economical hand, §4.2): right to left, mirrored, on one bed, no wedge, the word-signs bare and only *PANĀ* spelled, with its long-stone: `@grest %h @grest p.a.n.a_` in `drycut.py` with `hal=True`: **7 signs**, where the Hal *speech* written in its letters would be 29.

![The proverb in the Hal's cut and the living dry cut](orrowen/shots/dry_proverb_hal.png)

### 11.8 The Guest's three words

> **Hess… Helv… Sennyl…**

| Hess… | Helv… | Sennyl… |
|---|---|---|
| stop-IMP | sky | die-VN |

*Stop… Sky… Dying…*

```
h.e.s.s , h.e.l.v , s.e.n.n.O.l
```

- **Three content words and no small words**, as canon says: "your tongue joins its words with small words that make no sound across water".
- **None of the three needs a stop consonant**, so a mouth that has only the thunder-knock can carry them. That may be why these were the three he learned to say.
- ***Sennyl*'s rounded *y* is the one sound he would miss.** A Mystaeri mouth has no rounded vowel, so he would have said *sennel*. Brenn would not have noticed.

**Not cut.** They were spoken once, at a door, by a Mystaeri mouth; no one would cut them. Cut dry they would be [HESS] , [HELV] , [SENN] **O l**: the three stones exactly, for the Guest had already left out every mortar word ("your tongue joins its words with small words that make no sound across water"). **He spoke the dry cut.**

### 11.9 The Stone out of the Grey (the Last Carver's inscription)

> **Ul et dumol ol varn, ol theldeth…**

| Ul | *et* | dumol | ol | varn, | ol | theldeth… |
|---|---|---|---|---|---|---|
| in | ***the*** | N·memory | our | home | our | family-PL |

*In the memory of our home, our families…*

```
u.l e.t t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th
```

- ***et*** **is the one word too many.** It is an article on the head of a construct. Its two letters are both in the Title, so the inscription uses nothing the Title did not teach.
- **It is drawn with the five tells of §6.13:**
  1. no bed band;
  2. every stroke tapered at both ends;
  3. the Title's nasal bite copied faithfully;
  4. no mark at the end, where the cutting stops.
  5. **(v2)** every mortar word cut, in letters, as the coal Title had them, and one more (§6.13).

### 11.10 The Invocation's last line

> **Keth et tolm. Cadh et trenn. Amm cadhat o, es dess et odh.**

| Keth | et | tolm. |
|---|---|---|
| hold-IMP | the | stone |

| Cadh | et | trenn. |
|---|---|---|
| lay-IMP | the | tale |

| Amm | cadhat | o, | es | dess | et | odh. |
|---|---|---|---|---|---|---|
| when | laid-PTCP | it | FUT(+N) | N·answer | the | hearth |

*Hold the stone. Lay the tale. When it is laid, the hearth will answer.*

```
k.e.th e.t t.o.l.m | k.a.dh e.t t.r.e.n.n | a.m.m k.a.dh.A.t o , e.s t^N.e.s.s e.t o.dh |
```

- ***trenn* is "tale" and "course" at once**: "Lay the course", in the same breath.

**Written in the leaf-hand** (Seren's ink): the token string above, joined as §8 writes it: **42 letters and marks, 22 pen movements**.

**Cut dry: 14 signs** (33% of the written line):

```
@keth @tolm | @cadh @trenn | @amm @cadh+A.t , @tess @odh |
```

| [KETH] [TOLM] \| | [CADH] [TRENN] \| | [AMM] [CADH] A t , [TESS] [ODH] \| |
|---|---|---|
| hold stone | lay tale | when laid, answer hearth |

*Hold the stone. Lay the tale. When [it is] laid, [the] hearth [will] answer.* "Stone has no tense": the future is the reader's.

### 11.11 A small phrasebook

| Orrowen | English | Note |
|---|---|---|
| *Gald; nath nayald. Par; nath mosk.* | Build, do not destroy. Protect, do not attack. | the Creed; *nath* beds *bosk* into *mosk* |
| *Nel et hesp, veth et tolm. Nel et hurrol, veth et kethyl.* | Not the sword, but the stone. Not the killing, but the keeping. | the guild's word; one voice to each wedge |
| *Keth et tolm. Keth o, eth es geth tho.* | Hold the stone. Hold it, and it will hold you. | Halyna to the child Seren |
| *Re yorr et Ketherd.* · *Re yald et Stonwrytan.* | The Commander fought. · The Stonewrights built. | the Naming of the Rivenmen; *re* softens *gorr* and *gald* to *yorr* and *yald* |
| *Ho dhumos?* · *Tumar.* | Do you remember? · We remember. | the question and its echo |
| *Grest um hos, grest um vana.* | Harm to one is harm to both. | §11.7 |
| *Ston.* | It stands. | the close of every oath |

**Cut dry**, as the guild would cut its Creed and its word over the door of its halls:

| Saying | Cut dry | Reads |
|---|---|---|
| *Gald; nath nayald. Par; nath mosk.* | `@gald , !!@gald \| @par , !@bosk \|` | build, not un-build; guard, not attack. *nayald* is the turned stone and [GALD]; *nath* before it is a second turned stone |
| *Nel et hesp, veth et tolm. Nel et hurrol, veth et kethyl.* | `!@hesp , @tolm \| !@hurr+O.l , @keth+O.l \|` | not sword, stone; not killing, keeping. *veth* "but" is the wedge |
| *Ho dhumos?* · *Tumar.* | (not cut: a stone does not ask) · `@tum+A.r \|` | we remember |


---

## 12 · WHAT THIS GIVES THE BOOK

**Authored and ready to draw, in both registers:** the Title (coal, leaf-hand, dry cut); the Cry; the hearth's answer; Seren's untold note; the three calls; the Stonwryt (the Hal, whole; the living, whole; the dry citation; the leaf-hand); the shared proverb (and its Hal cut); the Guest's three words; the Last Carver's inscription; the Invocation's close; the phrasebook; the ten haven originals; every Shoreland name; and now **328 word-signs** and **the leaf-hand's whole alphabet**, with a proof font.

**Tier 3 (Jack's note 5): the whole Book in its own tongues.** For the stone leaves:
- **the text is written in the leaf-hand, whole**, because the Book is Seren's ink; an inscription quoted in a leaf is drawn cut dry beside it;
- the vocabulary is the §5 lexicon plus the reserve roots of `ancestor.md` §3.3 (371, each already derived in both tongues); the 194 reserve words that have word-signs are marked in §7.7;
- every reserve word owes the Welsh, Irish and Tolkien dictionary pass before it ships (`ancestor.md` §4.7); the look-alike screen of §13.3 covers the signs, not the words;
- the translator should keep to three habits of the tongue: verb first; the dual for pairs (Halyna are always two); and the "at" and "upon" idioms for having, being able and feeling.

**The surfaces**, as in the wf6 spec, with two changes: Seren's note is drawn in the leaf-hand, and the black chest's lid carries the foremark.

| Surface | First shown | Translation added | Note |
|---|---|---|---|
| **The Title** | first launch | from the start | Kael reads it out. Coal, letters, as now; the store-art line |
| **I.1's facing leaf** | first launch | Seren's line at V.1 (*The Mortar Line*) **[Jack]** | the Stone's rings, and Seren's line **in the leaf-hand** beneath them |
| **The tale-stone's Stonwryt** | shown from the foreword | Halyna's reading when II.1 is laid (Cam 3) | the Hal, cut whole; the Hal itself at *The Bedrock Hand* (Cam 16) |
| **The slates of the Rite** (I.4, Cam 2) | Cam 2 | Halyna's living reading from Cam 2 | **the Hal's dry cut** (owed) |
| **The lintel column** | — | read downward as the hands are earned | names in letters; the first line older than the Hal, in the first marks (`ancestor.md` §1.7) |
| **The rolls, the warning, the warden's report** | as their tales are laid | readable at once | the leaf-hand, haven spellings |
| **The black chest's lid** | I.4 | *The Bedrock Hand* | the foremark |
| **The Stonwryt coin** | wherever the coin is shown | *The Mortar Line* | the dry cut: [SOMM] [TOLM] [TOLM] ⟨gate⟩ **[Jack]** |

---

## 13 · ORIGINALITY

### 13.1 The standard (Jack's note 4)

> "It's not that nothing is traceable to others' works. Just nothing obvious. Nothing we could get sued for."

So the rule is no longer *nothing that resembles anything*. It is:

| | What | Why |
|---|---|---|
| **Must go** | a trademark, a logo, a franchise's named thing | actionable |
| **Must go** | a letter or sign that is, or is plainly taken from, a letter of a script a player would recognise: Latin, Greek, Cyrillic, Hebrew, the Elder Futhark, the basic CJK characters and the Kangxi radicals, kana, hangul; or of a famous invented script: Tengwar, Cirth, Aurebesh, Dovahzul, D'ni, Kryptonian, Sheikah, the Hylian scripts, Arrival's logograms | obvious |
| **Must go** | a word of a published invented language (Sindarin, Quenya, D'ni, Klingon, Dothraki, Valyrian, Na'vi) with the same or a related meaning; a real-language word with its own meaning (Welsh *seren* "star" is kept only as a coincidence of sound, with its own etymology) | obvious |
| **May stay** | **form-only echoes**: a word whose shape happens to match a word of another tongue, with a different meaning. *trenn, rhass, gorn, luth, tum, el, vess, gor, sell, gell, nell, sirr, hal, varn, mesk, gann, pell, crenn, brod, delv, sull, hebb, neth, lanth, na* and the rest of wf6 §9c's list all stay | not obvious; every language shares shapes |
| **May stay** | the world's commonest strokes, where the design needs them: the Door (Π-like) as the gate and GANNA, both peoples' door; the Fore, a Latin cross, as the Bar Before and the foremark (**"The Latin cross is fine"**, note 8); the Stem, the Bar, the Cut | generic, and kept whole on purpose |
| **May stay** | a resemblance to a letter of an ancient alphabet no player would know (Carian, Lycian, Old Turkic, Old Hungarian, Old Italic, Phoenician) | not obvious |
| **May stay** | an *idea* taken from a real or an invented system: logograms with phonetic complements (Egyptian, Maya, Chinese), a running hand made from an inscriptional one (Roman cursive), the grain's reading of meaning (Arrival, as Jack wants) | ideas are free |

The wf6 near-call list (wf6 §9c) is therefore **closed**: every item on it is a form-only echo and stays. The *trenn* / Sindarin *trenarn* call, which wf6 left for Jack, is resolved by note 4: *trenn* stays.

### 13.2 What the v2 design did to stay clear

- **The word-signs** are the First Tongue's own marks (`ancestor.md` §5), which were screened for runes, Ogham, Cirth, Tengwar and Arrival when they were made. Worn straight, they were screened again (§13.3), and **W7** keeps runes out by law: no branch leaves a stem at a slant.
- **Crowns are free stones, not diacritics.** They are 1.2 u tall and as wide as the head's top, and none is a dot, an acute or a curl, so a crowned sign does not read as a letter with a tehta (Tolkien's vowel marks, craft §8).
- **The leaf-hand** is the course-hand written, with angular turns, a nib, and hairline joins along the line: no loops, no bowls, no stem-and-bow, no headline. It resembles neither Latin cursive nor any of the famous invented hands.
- **The dry cut's economy** is Jack's reformed-Egyptian idea, and nothing in it copies the characters of the Anthon transcript or any Egyptian sign.

### 13.3 The look-alike screen

`wf7/orrowen/lookalike.py` draws each candidate and each reference character (from the system's fonts) into a 64 px box, thins both to one-pixel skeletons, and measures the symmetric mean chamfer distance between the skeletons, in box units (0 is the same shape). Calibration: a plain T scores 0.007 against Latin T; a 土-shaped sign 0.027 against 土. **Below 0.030 against a recognisable script is a copy and must change; 0.030 to 0.045 is looked at by eye.** References: 1463 characters (Latin capitals and small letters, digits, Greek and Cyrillic capitals, the Runic block, Ogham, Tifinagh, Hebrew, the Kangxi radicals and 172 common CJK characters, katakana, hangul jamo, the Canadian syllabics, Cherokee, Old Italic, Old Turkic, Old Hungarian, Phoenician, Carian, Lycian, Gothic, and 52 symbols including the crosses, the swastikas, ⊥, ⊤, Π, ∀ and the planetary signs).

**The results.**

| Signs | Nearest recognisable match | Verdict |
|---|---|---|
| FORE, *hosast* | † 0.005 | **kept by note 8**: it is the Fore, a Latin cross by design |
| GANNA, *ganna* | ⼙ 0.030; Π by eye | kept: the Door, kept whole by both peoples (wf6 §6.14) |
| *villur* | h (Latin small) 0.036 | kept |
| *sinth*, *nanth*, *brint*, *crynir* | ᛄ (Runic) 0.036–0.042 | kept |
| *mesk*, *lern*, *lurr*, *feth*, *linth*, *gend*, *virr* | ☥ (symbols) 0.037–0.045 | kept |
| *besk*, *lunt*, *gedh*, *tev*, *stidor*, *derd*, *misk*, *hass*, *saevul*, *covv*, *uld* | ㅒ (Hangul jamo) 0.037–0.043 | kept |
| *wemm*, *mivenn*, *breller*, *haemer*, *piskur* | 6 (digits) 0.037–0.044 | kept |
| *vestul*, *pynull* | ⼙ (Kangxi radicals) 0.038–0.043 | kept |
| *hoss*, *kaever* | 9 (digits) 0.039–0.042 | kept |
| *sceth* | 0 (digits) 0.039 | kept |
| *heskal*, *crernil* | ᚺ (Runic) 0.039–0.043 | kept |
| *gess*, *duss* | ᛧ (Runic) 0.039–0.044 | kept |
| *ranner*, *bramm*, *grest*, *sirr* | Λ (Greek caps) 0.039–0.044 | kept |
| *dhaedh*, *varn*, *hedh*, *aedh*, *lonn* | ⾷ (Kangxi radicals) 0.039–0.043 | kept |
| *odh* | ⽿ (Kangxi radicals) 0.039 | kept |
| *voth*, *resk* | ⾙ (Kangxi radicals) 0.040 | kept |
| *dath* | ᛌ (Runic) 0.040 | kept |
| *stykil*, *bisk* | ᛰ (Runic) 0.040–0.042 | kept |
| *hyvul*, *ludal*, *haeril* | g (Latin small) 0.041–0.045 | kept |
| *vesk*, *brod* | ♀ (symbols) 0.042–0.043 | kept |
| *heness*, *pedh*, *hagess*, *gorr*, *hesp* | Α (Greek caps) 0.042–0.044 | kept |
| *osk* | チ (Katakana) 0.042 | kept |
| *mest*, *lyss*, *ulvenn* | ‡ (symbols) 0.042–0.045 | kept |
| *vadull*, *greller* | Й (Cyrillic caps) 0.042–0.045 | kept |
| *brynt* | ᛡ (Runic) 0.043 | kept |
| *vysul* | ᚻ (Runic) 0.043 | kept |
| *ryst* | ᛟ (Runic) 0.043 | kept |
| *baeg*, *brist* | ㅔ (Hangul jamo) 0.043–0.045 | kept |
| *prenth* | 乒 (CJK common) 0.044 | kept |
| *tav* | 5 (digits) 0.044 | kept |
| *dhenn* | ᛝ (Runic) 0.044 | kept |
| *roskur* | ♄ (symbols) 0.044 | kept |

Every sign in the rows after the first two scores between 0.030 and 0.045 against a recognisable character, and was looked at by eye beside it. None is a copy: each match is an artefact of the skeleton at 64 px (a lens read as a ring, a tripod or a crowned stalk read as a letter's strokes), and the sign reads, at any size, as a head under a crown. They are kept. No sign scored below 0.030 except the two in the first rows.

**Dropped during design** because the screen or the eye found a copy: a Stem-and-cope sign (丅, T), a Bed sign (⊥, 土, 士), a Still sign (二, 王, =), a Three sign (川, Ш), a Hand sign (Ψ), a Split sign (Y), a Sprout and a Tally sign (runic ᚠ, ᛓ), two tree signs (runic ᛀ, †), a sail sign (P, ᚹ), a mouth sign (K), a wall sign (A), a gate with its capstone (开), a fire sign (a goblet), and a first leaf-hand in which every letter became an arch (it read as Armenian). The leaf-hand's *g*, which read as П when its shore stood upright under the slant, was given a stronger back-lean.

**The leaf-hand's near calls,** looked at by eye and kept: *a* and *A* (Г, 0.037), *o* and *O* (ד, 0.036), *k* (0.034 to a Kangxi radical), the gate (Π, 0.034, the Door). Each is a short stroke-pair that every alphabet has somewhere.

**What the screen cannot do.** It has no fonts for the invented scripts (Tengwar, Cirth, Aurebesh, Dovahzul, D'ni, Kryptonian, Sheikah, Hylian); those were checked by eye against the charts wf6's pass used (`wf6/originality_report.md`), and nothing new resembles them: the word-signs have no bows, no claw-triplets, no boxes, no hooks, and the leaf-hand no brush contrast and no Z- or 2-shapes. Arrival's logograms are ink circles; nothing in the stone is round.

### 13.4 Words

No new root is coined by this file except by the ancestor's laws: every word-sign's reading is a wf6 lexicon word or an ancestor reserve form, and the three new names of things (*ryt broc*, *rellor wrod*, *brodath lodh*) are built from them. *broc* and *rellor* are reserve forms and owe the dictionary pass with the rest.

---

## 14 · CONTACT POINTS

### 14a · With the Mystaeri design (carried over from wf6 §9a)

1. ***Mystaeri* is a Shoreland hybrid.** It is *myst* + *-aer* + the loan-plural *-i*. It needs the thunder-tongue's history to have *-aer* older than *-ear*, which is craft §1a's proposal.
2. **The Aelthar's meaning is the Shoreland proverb.** The carving's gloss should be exactly *Grest um hos, grest um vana* (§11.7), so the two peoples' one proverb is visible.
3. **The mute stones' "soft letters"** spelled Shoreland words "by their sound… the symbols wrong". The words they reached for should be real Orrowen.
   - The obvious plea is ***Hess. Doss et helv ul sennyl.*** ("Stop. The sky is in dying.") It is built from the Guest's three words.
   - A player who has learned Orrowen can then read the sound-spelled words inside the frost-letters, which is inventory D4.3's proposal. The rest of the stone stays mute.
4. **Mystaeri names in the course-hand** are spelled by sound: *Thaesaen* is **th a e s a e n**. The hand has no mark for the thunder-break.
   - **Proposal:** the Rivenmen write the knock as a **wedge inside the word** (*Ael,thar*), a pause mark put to a new use.
   - This is how the stone leaves of the Book already print *Ael'thar*.
5. **The sounds that look alike are different sounds.**

   | Spelling | In Orrowen | In the thunder-tongue |
   |---|---|---|
   | *rh* | /r̥/ | the Mystaeri designer's own value |
   | *ae* | /ɛː/, a monophthong | a diphthong |
   | *-en* | "of" | plural |

   A reader who knows both should hear the difference.
6. **The Epilogue's MIXED surface.** This file gives the letter side (§6.13). The Grain spec gives the rings under it. The courses must lie **straight across** the rings, and the bed is **not cut**.
7. **The green sliver says *home*.** Orrowen *varn* is the Title's third word. If the Grain spec gives the sliver's sign a Shoreland gloss, it should be *varn*.

8. **(v2) The kinship of the signs.** The dry cut's heads and crowns are the same 45 first marks as the grain's signs, worn the other way (§7.10). The Grain designer should keep the grain's forms of those marks as they are; no change is needed, and none should be made to bring the two closer.

### 14b · With `ancestor.md`: the emendations this file proposes

`ancestor.md` is adopted in full: the First Tongue, the laws, the 624 roots, Seren's etymology (§6), and its three small emendations (Hal *re*, Hal *van*, Hal SEREŊOS). This file proposes four small changes to it, none of which changes a form:

| `ancestor.md` | Now says | Proposed |
|---|---|---|
| §1.3, the row "the meaning of the marks", Stone column | "let go: each mark became a letter for one sound" | "kept as *words*, not as meanings: some marks became letters for their first sounds; others stayed word-signs, each read as one Orrowen word, whose meaning drifts with the word (orrowen_v2 §7)" |
| §5.2, the "On stone" column, for the marks used as heads or crowns | "lost" (the Cup, the Drop, the Star, the Knot, the Scar, the Mouth, the Hand, the Eye, the Kneel, the Still, the Fade, the Pale, the Rim, the Whole, the Turn, the Three …) | "lost from the letters; kept as a word-sign head or crown" (§7.4, §7.5 give which) |
| §5.3, the laws C3 and C4 | stated for "stone" | stated for **the letters**; the word-signs obey C1, C2 and W1–W7 |
| §1.7, "A bridge to note 1" | a possibility | done: the dry cut is that bridge, and the ink hand is the later, quicker hand that writes the small words out |

### 14c · The audit still owed

1. **The dictionary pass** (Welsh, Irish, Scottish Gaelic, Breton, Cornish, Manx; Eldamo and Parf Edhellen) on the 194 reserve words that have word-signs, and on every reserve word the tier-3 translation uses (`ancestor.md` §4.7). Under note 4 it is a check for *obvious* matches only: the same word with the same meaning.
2. **An exact-string web search**, as the Name Map did, for the new names: *ryt broc*, *rellor wrod*, *brodath lodh*, *Garl Flenn*.
3. **A look by eye at the leaf-hand at reading size** in the Legends page's own theme (the screen of §13.3 was run on skeletons, and the review sheets on a pale page).

---

## 15 · FOR JACK (decisions only he can make)

1. **The dry cut** as the chisel register: word-signs, letters for names and endings, the mortar words left out, *not* as the turned stone, "stone has no tense". Adopt? Recommended.
2. **Its names:** the dry cut (*ryt broc*), word-signs (*rellor wrod*), the mortar words (*brodath lodh*). Keep, or rename?
3. **The vow rule:** a vow is cut whole, in letters; a cited vow is cut dry and the gate is read *Ston*. Recommended: it is what keeps the tale-stone's Stonwryt readable word for word.
4. **The Hal as the most economical hand** (word-signs with no endings, no small words, no gaps, no bites; a vow whole). Recommended.
5. **The leaf-hand** as drawn in §8 (it replaces wf6's flat-pen leaf-hand, which was never drawn), and **Seren's note redrawn in it**. Recommended.
6. **The Title stays coal and letters, every word**, because the Captain "was no Stonewright" and "wrote as a man writes who has not written much". The dry cut of the Title (§11.1) is how the guild would cut it; say whether it should appear anywhere (over the inner gate? only in the Tongues doc?). Recommended: only in the Tongues doc.
7. **The Last Carver's fifth tell** (he cut the mortar words). It adds nothing to the Book's text; confirm.
8. **Mardh's word-sign**: the Kneel under the capstone, "the One over all, knelt to". An alternative is the Kneel under the Fore. Recommended: the capstone, and the Fore kept for "first".
9. **The Stonwryt coin's legend**: [SOMM] [TOLM] [TOLM] ⟨gate⟩, "while stone is stone. It stands." Adopt, or leave the coin plain?
10. **The word-sign list's unlock** (§10): with *The Mortar Line*, each reading added as its word is earned. Recommended.
11. **The 194 reserve words** given word-signs: adopt the list, or re-draw any? Any reserve word can be swapped without touching the signs.
12. **Carried from wf6, still open:** Halvard's "bedrock-warden" (recommended); when Seren's line translates (V.1 recommended); the old hand's unlock (Cam 16); the Captain's Stonwryt hidden for ever (recommended); the havens' English labels; the dual (confirm); the seven harmony slips, *Covv Treskat* among them (regularise, or declare old broad stems).

---

## 16 · RENDERER NOTES AND FILES

### 16a · The wf6 renderer (still the letters' renderer)

*`wf6/render_shore.py` draws the letters in the cut, the coal, the Carver's hand and the Hal, from the §6.6 table. Its notes, carried over from wf6 §11, still hold for every letter; they are abridged here to the rules a port must keep.*

The page contract for this renderer is stroke-only SVG with rounded caps, coloured `currentColor` under the class `stone-ink`. §6.11 describes filled facet polygons. The two meet as follows:

- **The two facets are two strokes.** Each stroke is drawn once at its full width (0.38 u) as the **shade**, then again at half width, offset a quarter-width towards the light, as the **lit** facet. The lit side is the one whose normal faces L = (−0.6, 0.8), per segment, as §6.11 says. The shade group's opacity is `--cut-shade-alpha` (default .30); the lit facet takes the full ink.
  - The spec's four colour tokens become one colour and three strengths: `--cut-shade-alpha`, `--bed-alpha` (.40) and `--bite-alpha` (.95).
  - Setting `--cut-shade-alpha: 1` gives a solid stroke, which is better in body text.
  - Images 72 px tall or less strengthen their facets to .8 by themselves.
- **Bedded ends are square and flush.** A bedded end is carried 0.4 u down into the mortar, and each line's letters are clipped at the top of the bed. A round cap therefore never shows on the bed. The foot is cut level with it, as §6.6 asks.
- **Joined ends keep their point**, and the round cap closes the corner. Corners inside one polyline (the offset's step, the V of a bite) are mitred (limit 3), which keeps the step crisp.
- **Lifted ends taper** over 0.4 u (at most 0.42 of the segment), drawn as three narrowing sub-strokes at 0.74, 0.50 and 0.30 of the width. The last one's cap ends on the table's point.
- **Dressed stones** (free laid stones, capstones, lintels, caps, long-stones) are pulled back by the half-width, so the round cap ends exactly on the table's end point. The break in a harmonic capstone therefore keeps its full 0.5 u.

- **The mortar** is a 0.22 u stroke on the band's centre line (y = −0.11), one per stone.
- **A bite breaks the mortar.** The notch is drawn from the band's centre line down to y = −0.7, in full ink, 0.26 u wide.
  - Feet at x = 0 put a bite 0.08 to 0.15 u before the band's §6.2 start.
  - So the band is carried back to 0.3 u beyond the notch: a bite is always cut into mortar, never past a stone's end.
- **Marks stand on the bed of the word they follow.** They sit in their own cells, one letter gap after it, and extend its band. The perpend "closes the joint" of its own stone, and the gate stands at the end of the vow's stone.
- **The head-joint centre** used for breaking the joint is the middle of the mortar gap between two stones' bands.
- **Breaking the joint: widening is capped** at 1.25 u over the standard joint (3.45 u). Beyond that, a joint reads as a missing word, not a staggered course. Past the cap, the renderer narrows the joints as §6.8 says. If neither clears 1.0 u, it keeps the best width it tried.
- **The stone outline** (§6.8, optional) is drawn only on surfaces that are cut stone: the cut Title and the Stonwryt. It uses alpha .13. Its top joint rises from y = 3.8 to 4.45 on a line that carries a sealing lintel or numeral caps, which stand at 3.75.
- **Punctuation.** The Book's punctuation maps to the marks as follows:
  - "." "!" "?" become the perpend.
  - "," ";" ":" "—" become the wedge.
  - "…" is a wedge inside a text, and nothing where it ends one: the Guest's words and the Carver's open end.
  - A repeated cry (*Talda! Talda! Talda!*) is laid as one sentence with one perpend, as §11.2's tokens have it.
  - A text whose last sentence is the one word *Ston.* (or *Stonos*) takes the gate after it.
  - In the Hal, "·" is the perpend and there is no wedge.

- **Coal (the Captain's Title, §6.10).** Blunt round caps, never tapered; this is what "square, coal does not taper" asks for.
  - Strokes are 0.5 u wide in cell units, and the whole drawing is 1.2× (applied to the file's width and height).
  - The jitter and the tilt as written can exceed §6.12's 0.22 u limit together: 0.12 u of jitter plus 4° on a 3.1 u stone is 0.34 u.
    - The renderer jitters each distinct point once (dx, dy each ±0.12 u, so joins stay closed).
    - It tilts each horizontal laid stone by up to ±4° about its joined end (about its midpoint if it is free).
    - It then clamps every end's total displacement to 0.215 u (checked: the largest is 0.215 u).
  - **The seed** is FNV-1a-32 of the §11 token string with single spaces, for mulberry32. The Title's seed is `0xee135a92`, and a port must draw in the same order: letters in reading order, points in stroke order, then tilts.
  - Coal bites are short strokes 0.12 u below the absent bed.
- **The Last Carver (§6.13).** No bed band. Every stroke is tapered at both ends, joined and bedded ends included. The bite is copied as tapered strokes, and the end is left open.
- **Garl Hal (§6.9).**
  - Letters are mirrored and heightened *before* the end rule and the lighting, so the light still falls from the top left on the old stone.
  - Consonants and marks are 4/3 tall, vowels 1.25. The lintel sits at 5.0 (3.75 × 4/3). The long-stone stays at the table's 3.25, over a 2.5 u vowel. The line pitch is 6.93 u.
  - Lines are right-aligned, each on one unbroken bed.
  - The Hal *hr* is the rough-r letter.
  - **The ligature** (*ALD | BEN*) is its own stone, after a full head-joint: the only break in a Hal bed, because a signature is cut apart from its vow.

**The slips wf6's analyser found** (wf6 §11b) are carried to §15 item 12 unchanged. **The decode test** (wf6 §11h: ten course-hand images decoded from screenshots alone, all exact) still stands for the letters; the dry cut and the leaf-hand have not yet been decode-tested by a reader who has not seen this file (§14c).

### 16b · The v2 tools (all in `wf7/orrowen/`, scratch only)

| File | What it does |
|---|---|
| `wordstones.py` | the heads, the crowns, the turned stone and the 328-sign inventory; builds every sign's geometry (`wordstones.json`) and runs the checks of §7.9 |
| `ws_chart.py` | the charts of §7 (`heads`, `all`) and the look-alike screen over the whole inventory (`screen`) |
| `drycut.py` | draws a dry-cut token string (§11) in the cut, with beds, footings, complements, the turned stone, lintels and numeral caps; `hal=True` draws the Hal's dry cut, right to left, mirrored, on one bed |
| `leafhand.py` | the leaf-hand: the table (`json` → `leafhand.json`), an SVG renderer with the two inks, the pen-movement count, and the proof font (`font` → `wf7/fonts/garl_flenn_proof.ttf`, run with `wf7/../venv/bin/python`) |
| `lookalike.py` | the look-alike screen (§13.3), in headless Chrome |
| `samples_v2.py` | the §11 texts in both registers, and their review sheet |
| `build_spec.py`, `tpl_a.md`, `tpl_b.md`, `tpl_c.md` | this file, assembled from the templates, the wf6 spec (for the sections carried over) and the tables above |
| `cutlib.py` | shared drawing helpers; uses `wf6/render_shore.py` read-only, so a word-sign is cut exactly as a letter is |
| `proto1.py` … `proto4.py`, `leafhand_proto.py` | the design rounds, kept for the record |

---

## APPENDIX A · EVERY WORD-SIGN'S STROKES

Computed by `wordstones.py` (§7.3): `reading: [[x, y], …]` per stroke, in cell units, y up; the footing is not listed.

```
tolm:     [[[1.0,0],[1.0,3.2],[2.2,4.2],[3.4,3.2],[3.4,1.6]]]
hosk:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.0,4.0],[3.4,4.0]]]
tald:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
pell:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
stell:    [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
gorn:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
stann:    [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
ryt:      [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
sirr:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
lenn:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
ston:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
hal:      [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
domm:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
baek:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
ledal:    [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
bront:    [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
serull:   [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
stinal:   [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
saenul:   [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
tynt:     [[[1.0,0.0],[1.0,2.2476],[2.2,2.95],[3.4,2.2476],[3.4,1.1238]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
hald:     [[[0.9,0],[0.9,1.4],[3.5,1.4]],[[0.9,2.8],[3.5,2.8],[3.5,1.4]],[[0.9,2.8],[0.9,4.2]],[[2.2,1.4],[2.2,2.8]]]
lest:     [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
gebb:     [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
gald:     [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
cumm:     [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
taldow:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
vathur:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
kaelir:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
kiser:    [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
tynur:    [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
hinnar:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
hellur:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.0,4.0],[3.4,4.0]]]
nelter:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
rivull:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
bystir:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
paltur:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
disker:   [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
brellir:  [[[0.9,0.0],[0.9,0.9833],[3.5,0.9833]],[[0.9,1.9667],[3.5,1.9667],[3.5,0.9833]],[[0.9,1.9667],[0.9,2.95]],[[2.2,0.9833],[2.2,1.9667]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
trenn:    [[[0.9,0],[0.9,2.1],[3.5,2.1],[3.5,4.2]]]
orr:      [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
darr:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
hask:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
cadh:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
dask:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.0,4.0],[3.4,4.0]]]
tesk:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
vell:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
luth:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
flenn:    [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
cemm:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
fenn:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
mymm:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
lestir:   [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
nesk:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
mosk:     [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
haral:    [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
tragul:   [[[0.9,0.0],[0.9,1.475],[3.5,1.475],[3.5,2.95]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
odh:      [[[1.0,0],[1.0,4.2],[3.4,4.2],[3.4,1.2],[1.8,1.2],[1.8,3.2],[2.6,3.2],[2.6,2.0]]]
varn:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
theld:    [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
arra:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
greller:  [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
prenth:   [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
resk:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.0,4.0],[3.4,4.0]]]
aedh:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
vadull:   [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
lonn:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
memm:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
dhaedh:   [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
nunth:    [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
blenth:   [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
hedh:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
voth:     [[[1.0,0.0],[1.0,2.95],[3.4,2.95],[3.4,0.8429],[1.8,0.8429],[1.8,2.2476],[2.6,2.2476],[2.6,1.4048]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
cresk:    [[[1.0,0],[1.0,2.2],[2.0,2.8],[1.4,4.2]],[[3.4,0],[3.4,2.0],[2.5,2.6],[3.2,4.2]]]
tresk:    [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
grest:    [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
gorr:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
hurr:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
bosk:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
bramm:    [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
pedh:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
hesp:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
kest:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
nycul:    [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
lernil:   [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.0,4.0],[3.4,4.0]]]
stemir:   [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
sevir:    [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
bynd:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
gask:     [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
heness:   [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
hagess:   [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
peltir:   [[[1.0,0.0],[1.0,1.5452],[2.0,1.9667],[1.4,2.95]],[[3.4,0.0],[3.4,1.4048],[2.5,1.8262],[3.2,2.95]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
par:      [[[1.2,0],[2.2,3.2]],[[2.2,3.2],[3.5,3.2]],[[0.9,3.2],[1.7,3.2]],[[2.2,3.2],[2.2,4.2]]]
crenn:    [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.0,4.0],[3.4,4.0]]]
osk:      [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
pemess:   [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
begorn:   [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
cryrull:  [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
lymm:     [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
renn:     [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
havul:    [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
bemm:     [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
cald:     [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
gesk:     [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
hydull:   [[[1.2,0.0],[2.2,2.2476]],[[2.2,2.2476],[3.5,2.2476]],[[0.9,2.2476],[1.7,2.2476]],[[2.2,2.2476],[2.2,2.95]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
molt:     [[[1.6,0],[0.9,3.4]],[[2.8,0],[3.5,3.4]],[[1.7,2.0],[1.95,2.7],[2.2,2.0],[2.45,2.7],[2.7,2.0]]]
hoss:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
lomm:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
vall:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
ludal:    [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
hylenn:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
saemal:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
syllorn:  [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
teltor:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
haeril:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
myrral:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
dhyvull:  [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
prumul:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
hyvul:    [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
ledh:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[1.7,1.4048],[1.95,1.8964],[2.2,1.4048],[2.45,1.8964],[2.7,1.4048]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
tum:      [[[1.6,0],[0.9,3.4]],[[2.8,0],[3.5,3.4]],[[2.2,1.6],[2.2,2.8]]]
sesk:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.0,4.0],[3.4,4.0]]]
kaever:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
hyrril:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
daevar:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
rystull:  [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
prener:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
filv:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
bethir:   [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
mamm:     [[[1.6,0.0],[0.9,2.3881]],[[2.8,0.0],[3.5,2.3881]],[[2.2,1.1238],[2.2,1.9667]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
lorr:     [[[2.2,0],[2.2,0.8]],[[2.2,0.8],[1.2,2.0],[2.2,4.2],[3.2,2.0],[2.2,0.8]]]
unth:     [[[2.2,0.0],[2.2,0.5619]],[[2.2,0.5619],[1.2,1.4048],[2.2,2.95],[3.2,1.4048],[2.2,0.5619]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
semm:     [[[2.2,0.0],[2.2,0.5619]],[[2.2,0.5619],[1.2,1.4048],[2.2,2.95],[3.2,1.4048],[2.2,0.5619]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
sulenn:   [[[2.2,0.0],[2.2,0.5619]],[[2.2,0.5619],[1.2,1.4048],[2.2,2.95],[3.2,1.4048],[2.2,0.5619]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
buthar:   [[[2.2,0.0],[2.2,0.5619]],[[2.2,0.5619],[1.2,1.4048],[2.2,2.95],[3.2,1.4048],[2.2,0.5619]],[[1.0,4.0],[3.4,4.0]]]
lernul:   [[[2.2,0.0],[2.2,0.5619]],[[2.2,0.5619],[1.2,1.4048],[2.2,2.95],[3.2,1.4048],[2.2,0.5619]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
orl:      [[[1.0,0],[2.2,2.0],[3.4,0]],[[2.2,2.0],[2.2,4.2]],[[1.2,3.6],[3.2,2.6]],[[1.2,2.6],[3.2,3.6]]]
vess:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
clem:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
surr:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
grem:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
helv:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.0,4.0],[3.4,4.0]]]
bell:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
rerd:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
selm:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
elth:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
ryst:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
fedh:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
dhenn:    [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
baeg:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
heth:     [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
brist:    [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
dustal:   [[[1.0,0.0],[2.2,1.4048],[3.4,0.0]],[[2.2,1.4048],[2.2,2.95]],[[1.2,2.5286],[3.2,1.8262]],[[1.2,1.8262],[3.2,2.5286]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
vorr:     [[[1.2,0],[1.2,1.8],[1.8,3.0]],[[2.2,0],[2.2,2.4],[2.8,4.2]],[[3.2,0],[3.2,1.6]]]
senn:     [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
brenth:   [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
vem:      [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
drod:     [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
dhidh:    [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
syndal:   [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
raltar:   [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.0,4.0],[3.4,4.0]]]
tymorn:   [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
bith:     [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
kesk:     [[[1.2,0.0],[1.2,1.2643],[1.8,2.1071]],[[2.2,0.0],[2.2,1.6857],[2.8,2.95]],[[3.2,0.0],[3.2,1.1238]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
tovv:     [[[1.8,0],[1.8,1.4]],[[2.6,2.8],[2.6,4.2]],[[1.8,1.4],[1.2,2.1],[2.6,2.8],[3.2,2.1],[1.8,1.4]]]
hess:     [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[1.0,4.0],[3.4,4.0]]]
tul:      [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
somm:     [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
amm:      [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
nend:     [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
bysk:     [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
cullar:   [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
niss:     [[[1.8,0.0],[1.8,0.9833]],[[2.6,1.9667],[2.6,2.95]],[[1.8,0.9833],[1.2,1.475],[2.6,1.9667],[3.2,1.475],[1.8,0.9833]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
sceth:    [[[1.7,4.2],[0.9,2.1],[2.2,0],[3.5,2.1],[2.7,4.2]]]
wemm:     [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
tav:      [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
sulter:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
mivenn:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
breller:  [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
nestull:  [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
farr:     [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
felm:     [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
piskur:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
pynull:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.0,4.0],[3.4,4.0]]]
sugorn:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
haemer:   [[[1.7,2.95],[0.9,1.475],[2.2,0.0],[3.5,1.475],[2.7,2.95]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
mesk:     [[[2.2,0],[2.2,2.0]],[[1.0,2.0],[3.4,2.0]],[[1.0,2.0],[1.6,3.2],[2.2,2.0]],[[2.2,2.0],[2.8,3.2],[3.4,2.0]],[[1.6,3.2],[2.2,4.2],[2.8,3.2]]]
lurr:     [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
crynir:   [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
gost:     [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
brynt:    [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.0,4.0],[3.4,4.0]]]
gend:     [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
sinth:    [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
nanth:    [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
feth:     [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
brint:    [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
linth:    [[[2.2,0.0],[2.2,1.4048]],[[1.0,1.4048],[3.4,1.4048]],[[1.0,1.4048],[1.6,2.2476],[2.2,1.4048]],[[2.2,1.4048],[2.8,2.2476],[3.4,1.4048]],[[1.6,2.2476],[2.2,2.95],[2.8,2.2476]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
brod:     [[[2.2,0],[2.2,1.0]],[[3.4,1.5],[2.2,1.0],[1.0,2.4],[2.2,3.8],[3.4,3.3]],[[2.7,2.4],[3.6,2.4]]]
brodh:    [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
carm:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
pess:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
tess:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
voll:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
ammad:    [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
hunn:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
gomm:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
mysk:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
dast:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
medh:     [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
rellor:   [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
niltenn:  [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
stathul:  [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.0,4.0],[3.4,4.0]]]
redul:    [[[2.2,0.0],[2.2,0.7024]],[[3.4,1.0536],[2.2,0.7024],[1.0,1.6857],[2.2,2.669],[3.4,2.3179]],[[2.7,1.6857],[3.6,1.6857]],[[1.54,3.4],[1.66,4.06]],[[2.86,3.4],[2.74,4.06]],[[1.24,4.6],[3.16,4.6]]]
garl:     [[[1.0,0],[2.0,2.6],[3.4,2.6],[3.4,3.8]]]
keth:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
hebb:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
lusk:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
sollan:   [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
drunn:    [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
bresk:    [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
nydh:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
prass:    [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.0,4.0],[3.4,4.0]]]
femm:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
wesk:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
birnenn:  [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
peskul:   [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
lamm:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
lemm:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
bamm:     [[[1.0,0.0],[2.0,1.8262],[3.4,1.8262],[3.4,2.669]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
vesk:     [[[2.2,0],[2.2,1.2]],[[0.9,2.5],[2.2,3.8],[3.5,2.5],[2.2,1.2],[0.9,2.5]],[[2.2,2.1],[2.2,2.9]]]
lern:     [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
stykil:   [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
naelur:   [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
raevul:   [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
virr:     [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
deld:     [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
bisk:     [[[2.2,0.0],[2.2,0.8429]],[[0.9,1.756],[2.2,2.669],[3.5,1.756],[2.2,0.8429],[0.9,1.756]],[[2.2,1.475],[2.2,2.0369]],[[1.0,4.0],[3.4,4.0]]]
uld:      [[[1.4,0],[2.2,2.6]],[[3.0,0],[2.2,2.6]],[[2.2,2.6],[2.2,3.3]],[[1.6,3.3],[2.8,3.3],[2.8,4.2],[1.6,4.2],[1.6,3.3]]]
gedh:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
tev:      [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.96,4.6],[1.6,4.0],[2.2,3.4],[2.8,4.0],[2.44,4.6]]]
hemm:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[0.88,4.36],[1.78,4.36],[2.2,3.64],[2.62,4.36],[3.52,4.36]]]
lunt:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
covv:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.0,4.0],[3.4,4.0]]]
hass:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
besk:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
saevul:   [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
stidor:   [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
dhaker:   [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
misk:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
derd:     [[[1.4,0.0],[2.2,1.8262]],[[3.0,0.0],[2.2,1.8262]],[[2.2,1.8262],[2.2,2.3179]],[[1.6,2.3179],[2.8,2.3179],[2.8,2.95],[1.6,2.95],[1.6,2.3179]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
lumm:     [[[1.2,4.2],[1.2,1.4],[2.4,1.4],[2.4,0],[3.4,0.0]]]
mardh:    [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.0,4.0],[3.4,4.0]]]
ammel:    [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
ternil:   [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
peness:   [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
grumar:   [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
ferr:     [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
nestorn:  [[[1.2,2.95],[1.2,0.9833],[2.4,0.9833],[2.4,0.0],[3.4,0.0]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
lunn:     [[[1.0,0],[1.0,3.4],[1.8,4.2]],[[3.4,0],[3.4,3.4],[2.6,4.2]]]
pondul:   [[[1.0,0.0],[1.0,2.3881],[1.8,2.95]],[[3.4,0.0],[3.4,2.3881],[2.6,2.95]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
ranner:   [[[1.0,0.0],[1.0,2.3881],[1.8,2.95]],[[3.4,0.0],[3.4,2.3881],[2.6,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
hollar:   [[[1.0,0.0],[1.0,2.3881],[1.8,2.95]],[[3.4,0.0],[3.4,2.3881],[2.6,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
villur:   [[[1.0,0.0],[1.0,2.3881],[1.8,2.95]],[[3.4,0.0],[3.4,2.3881],[2.6,2.95]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
haethil:  [[[1.0,0.0],[1.0,2.3881],[1.8,2.95]],[[3.4,0.0],[3.4,2.3881],[2.6,2.95]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
venn:     [[[2.2,4.2],[2.2,2.4]],[[2.2,2.4],[1.5,1.2],[2.2,0],[2.9,1.2],[2.2,2.4]]]
tunn:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.0,4.0],[3.4,4.0]]]
clenn:    [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
gell:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
sell:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
strom:    [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
lyss:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
ulvenn:   [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
duss:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
gess:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
dath:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
saed:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
mest:     [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
crystil:  [[[2.2,2.95],[2.2,1.6857]],[[2.2,1.6857],[1.5,0.8429],[2.2,0.0],[2.9,0.8429],[2.2,1.6857]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
kyl:      [[[1.2,0],[1.2,2.0],[3.2,3.2],[3.2,4.2]]]
marr:     [[[1.2,0.0],[1.2,1.4048],[3.2,2.2476],[3.2,2.95]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
omm:      [[[1.2,0.0],[1.2,1.4048],[3.2,2.2476],[3.2,2.95]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
drig:     [[[1.2,0.0],[1.2,1.4048],[3.2,2.2476],[3.2,2.95]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
grik:     [[[1.2,0.0],[1.2,1.4048],[3.2,2.2476],[3.2,2.95]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
gyst:     [[[1.2,0.0],[1.2,1.4048],[3.2,2.2476],[3.2,2.95]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
ganna:    [[[1.2,0],[1.5,3.6]],[[3.2,0],[2.9,3.6]],[[0.8,3.6],[3.6,3.6]]]
gann:     [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
vysul:    [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
crernil:  [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
heskal:   [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
roskur:   [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
vestul:   [[[1.2,0.0],[1.5,2.5286]],[[3.2,0.0],[2.9,2.5286]],[[0.8,2.5286],[3.6,2.5286]],[[1.0,4.0],[3.4,4.0]]]
lodh:     [[[0.9,1.6],[1.6,0.6],[2.8,0.6],[3.5,1.6]],[[2.2,0],[2.2,0.6]],[[1.6,1.6],[1.6,3.0],[2.8,3.0],[2.8,1.8]]]
rhyn:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.0,4.0],[3.4,4.0]]]
trun:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
gunn:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
gaed:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
tuss:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
pask:     [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
myger:    [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
demull:   [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
spenn:    [[[0.9,1.1238],[1.6,0.4214],[2.8,0.4214],[3.5,1.1238]],[[2.2,0.0],[2.2,0.4214]],[[1.6,1.1238],[1.6,2.1071],[2.8,2.1071],[2.8,1.2643]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
wadh:     [[[0.9,0],[0.9,2.2],[1.7,2.2],[1.7,1.0],[2.6,1.0],[2.6,3.4],[3.5,3.4]]]
myst:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[0.76,4.48],[1.48,4.48]],[[1.84,4.06],[2.5,4.06]],[[2.86,3.64],[3.34,3.64]]]
hyll:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.36,3.4],[1.36,4.0],[3.04,4.6]]]
rhull:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.0,3.4],[1.0,4.0],[3.4,4.0],[3.4,4.6]]]
sedh:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
nell:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
frenn:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
crest:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.0,4.0],[3.4,4.0]]]
grull:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.36,3.4],[1.36,4.24]],[[2.2,3.4],[2.2,4.6]],[[3.04,3.4],[3.04,4.24]]]
orrow:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
fodh:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
nerdess:  [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[2.2,3.4],[2.2,3.94],[1.6,4.6]],[[2.704,4.24],[3.04,4.6]]]
dhysal:   [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[2.2,3.4],[2.2,4.6]],[[1.66,3.664],[2.74,4.336]],[[1.66,4.336],[2.74,3.664]]]
fimm:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
ridh:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
spant:    [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[1.6,4.6],[2.8,4.6],[2.2,3.4],[1.6,4.6]]]
tant:     [[[0.9,0.0],[0.9,1.5452],[1.7,1.5452],[1.7,0.7024],[2.6,0.7024],[2.6,2.3881],[3.5,2.3881]],[[2.2,3.4],[1.78,4.0],[2.2,4.6],[2.62,4.0],[2.2,3.4]]]
brunn:    [[[0.9,0],[1.6,1.8],[2.2,1.2],[3.0,3.6],[3.6,2.2]]]
sorth:    [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[0.88,3.52],[2.2,4.6],[3.52,3.52]]]
sulv:     [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.12,3.46],[1.48,4.54]],[[2.02,3.46],[2.38,4.54]],[[2.92,3.46],[3.28,4.54]]]
hiskenn:  [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[0.88,4.0],[1.84,4.0]],[[2.56,4.0],[3.52,4.0]]]
gynt:     [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.84,3.4],[1.84,4.6]],[[2.38,3.82],[3.04,3.82]]]
gint:     [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.6,4.6],[2.2,3.4],[2.8,4.6]]]
nenth:    [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.9,3.4],[1.54,4.6]],[[2.5,3.4],[2.86,4.6]]]
susk:     [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.0,4.0],[3.4,4.0]]]
vimm:     [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.12,3.64],[3.28,3.64]],[[1.12,4.36],[3.28,4.36]]]
henth:    [[[0.9,0.0],[1.6,1.2643],[2.2,0.8429],[3.0,2.5286],[3.6,1.5452]],[[1.0,3.52],[1.6,4.48],[2.2,3.52],[2.8,4.48],[3.4,3.52]]]
hosast:   [[[2.2,0],[2.2,4.2]],[[1.2,3.1],[3.2,3.1]]]
```
