# RIVENKEEP · THE MYSTAERI TONGUE AND THE GRAIN

*Design spec for wf6, 2026-09-27. Two things are specified here: **Seilrhass**, the spoken thunder-tongue, and **Eilseth**, the grain, the knowing-script carved in living wood. This is a workflow input. It is not a Book leaf and not a repo doc. Its generator prototype lives in `scratchpad/wf6/grain/` and never goes into `Docs/`.*

**Sources used:** `wf6/craft.md` (the originality boundaries), `wf6/inventory.md` (every surface and fixed point), and the canon itself: `wf5/legends_v11_final.md`, `wf5/admiral_v03.md`, `Research/Rivenkeep_Fiction_Hooks.md` and `Research/Rivenkeep_Name_Map.md`. Line refs such as `L1369` point into the Legends markdown; `Ad §9b` points into the Admiral.

**Status key.** **[canon]** means the Book or the Admiral already fixes it. **[rule]** means this spec fixes it. **[call]** means it is Jack's decision (collected in §8).

---

## 0 · THE SHORT ANSWER

1. **Two layers, as the canon says.** The spoken tongue is loud, knocking and dialectal: "we speak as the storm speaks in the high boughs, in cracks and breaks" (II.2). The carved grain has no sound and no words: "what is carved in living wood is not heard. It is known." They are "one word", with "the thunder for the moment, the softness for always". So every grain sign has a **soft reading**, its spoken word with the knock taken out.
2. **Names.** The spoken tongue is ***Seilrhass***, "bough-thunder" (spoken *Seil'rhass*). The grain is ***Eilseth***, "ring-carving" (spoken *Eil'seth*). In ordinary speech the grain is simply *vael*, "grain", which is the word the Book already translates. A knowing is a *theinas*, "a holding". Seren's word "the Knowing" is a calque of it.
3. **Seilrhass is built out of the names Jack already has.**
   - It has seven consonants (*v, th, s, l, r, rh, n*) and no oral stops. Its vowels are front and open: *a, e, i* and *ae, ea, ei*, with no *o* and no *u*.
   - Every word of two or more syllables takes one **knock** after its first syllable. That is the apostrophe of *Ael'thar* and *Ra'lensaen*.
   - Compounds run modifier before head. The language is head-final and verb-last, the opposite of verb-first Shoreland.
   - Every one of the 26 coined Mystaeri names stays valid with its meaning, and each is analysed in §2.7.
   - The lexicon has **215 entries**: 91 roots, 64 compounds, 28 names, 23 small words and 9 affixes.
4. **The hard stops the Rivenmen hear are the knock.** The Story Bible says the spoken tongue has "hard stops (k, t, d)", yet no attested word contains one. The resolution is that the knock is a glottal catch. After it, *th*, *s* and *n* are released hard, and shore ears hear *t*, *ts* and *d*. The deep-forest dialects make the knock velar, and it is heard as *k*. Historically the knock is the ghost of lost stops (§2.3–2.4).
5. **The grain is a cross-section of a trunk.**
   - The pith at the heart is the beginning; the bark is the end.
   - Meaning is carried by marks cut **across** the growth rings.
   - **Ring = when.** One ring is one step, and the same ring is the same hour.
   - **Angle = who or where.** Each mark stands on one of 16 files, read clockwise from the root.
   - The **three bands**, heart, sap and bark, are the three movements. They are parted by doubled rings, which are the Book's own grain-rules.
   - **Line quality classifies.** Closed straight shapes are things of stone; closed curved shapes are things of wood.
   - **Weight carries nothing.**
6. **The ten root signs and *Burn* are drawn exactly as the Book describes them** (§3.5).
   - The Wave is one stroke curling forward. The Lone Stroke is a short cut running ahead of a long one. The Bar Before is a bar laid across a stroke. And so on.
   - *Burn* is a **fire scar**: a charred wedge whose edges the wood has grown over.
   - A Hasty carving is one sign on the heart ring of a sapling. Each later Tide literally contains its parent carving's rings, ring for ring, with the parent's old bark still visible inside as included bark.
   - The Joined Tide grows **several piths inside shared rings**, as stems that grow together really do. It is the dark mirror of the Aetherbond.
7. **The inventory is 70 signs, 6 condition bands and 32 grammar devices.** Each sign is a parametric V-cut mark given as JSON in a local frame, so a program can draw any sentence by rule and read it back by rule. A working prototype draws every sample in this spec (§9).
8. **Nothing is copied from Arrival.** The rings are many and concentric, not one. The cuts are crisp and faceted, not ink or smoke. The marks lie inside the bark, and nothing leaves the rim. The script is directional, heart to bark. Weight means nothing. Rings are time. The full comparison, with the Gallifreyan, Nomai, Elden Ring and Ogham boundaries, is in §3.13. An originality pass against the runes, Cirth, Tengwar, D'ni and the other famous fictional scripts recut nine signs and the root-foot (§3.13, `wf6/originality_report.md`).
9. **The samples are all here** (§5):
   - *We remember our home too*, in the grain and in speech;
   - *Naelear*;
   - the Aelthar, as spoken and as carved;
   - the gift's sentence;
   - the Hasty seven and *Burn*;
   - *Three roads, one hour*, grown from its ancestors;
   - the leaf facing I.1.
10. **The leaf facing I.1** is the grain of the Stone out of the Grey. It is the Last Carver's own knowing, cut in the Myststone under the letters he chiselled.
    - It is the wood's half of *The Torn Cloak*: what the hulls saw on the last whole stone, and what went home through the roots.
    - It holds all five things of the Title, where the letters stop after two, and one more knowing: *they stood for these at the stone, and we stood for the same, on the other side of it.*
    - It uses only signs the player has already met, as the Last Carver used only letters from the Title.
    - Until the Epilogue the leaf shows the Stone's rings with no marks, which is the truthful grain for "nothing is yet given" [call §8.1].

**Fixed points honoured** (each checked against the canon):
- the roots *ael, thar, varen, saen, vael, seth/sethen, thae, lea, ralen, nael, rhen, eir, nei, ress, lenth, -ear*, with their glosses;
- every Tide, Throne and rite name;
- the thunder-break after the first syllable;
- the Law of the Rings (one sign, a phrase, a sentence with a memory, a judgement);
- the root is read by eye, "never more than the root, for the rest the wood gives only to the Bonded, and it must be known, not read" (the Book of Knowings);
- the three movements and two grain-rules of every wood leaf;
- the pale ring closing in a Throne's bark at each groan;
- *Grow until the shore is silent* lying "beneath all the other carvings";
- the two halves of one heart (V.2);
- the dialects that the grain bridges;
- "the wood does not lie";
- *Rhenear* cut small;
- the green sliver's one word, *home*, with *Naelear* folded inside it.

---

## 1 · NAMES

| Thing | In-language name | Spoken | Built from | What the Book calls it |
|---|---|---|---|---|
| The spoken tongue | **Seilrhass** | *Seil'rhass* | *seil* bough + *rhass* storm, crack: "bough-thunder", "the crack of the boughs" | "the thunder-tongue", "their own tongue" |
| The grain, as a written craft | **Eilseth** | *Eil'seth* | *eil* growth ring + *seth* carving: "ring-carving" | "the grain" (*vael*), "the carving" |
| A knowing, the act of knowing wood | **theinas** | *Thei'nas* | *thein* to hold, to know by touch + *-as* | "a knowing"; the Rivenmen's "the Knowing" is its calque |
| A sign's soft reading | **eisranth** | *Eis'ranth* | *eis* name + *ranth* word: "name-word" | "the carved form … whole and soft" |
| The soft letters that spell sound on stone | **rhelranth** | *Rhel'ranth* | *rhel* frost + *ranth* word: "frost-words" | "fine and curling, as beautiful as frost on a window" (IV.1); see Appendix A |

**Checks.** An exact-string web search on 2026-09-27 found no published use of *Seilrhass*, *Eilseth*, *Naelenn*, *Theinas*, *Aelress*, *Rhenseth* or *Eirsethea*. *Ennael*, first drafted for "home", turned out to be a fan-wiki character, so home is ***Naelenn***. Neither *Seilrhass* nor *Eilseth* contains a Tolkien root. *Seil* is a Scottish island and *eil* the German for haste. Both are form-only overlaps that the Name Map's standard allows.

---

## 2 · SEILRHASS, THE THUNDER-TONGUE

### 2.1 · Sounds

Every Mystaeri name the Book prints uses only these sounds, and the list is closed: nothing may be added without a canon reason.

| Letter | Sound (IPA) | Near English | Notes |
|---|---|---|---|
| **v** | [v] | *v*ine | |
| **th** | [θ] | *th*in | never the *th* of *this*, except between vowels in the Grove dialect |
| **s** | [s] | *s*ea | |
| **l** | [l] | *l*eaf | |
| **r** | [r], tapped [ɾ] between vowels | a Scots *r* | |
| **rh** | [r̥], a voiceless trill | the breath of an *r* | only at the start of a syllable |
| **n** | [n] | *n*ight | |
| **ss, nn** (also **ll, rr** where roots meet) | long [sː], [nː] | | written double, held |
| **a** | [a] | f*a*ther | |
| **e** | [ɛ] | b*e*d | |
| **i** | [i] | mach*i*ne | rare in roots; it is the vowel of the small words (*li, ni, thi, si, ri, vi, rhi*) |
| **ae** | [aɛ̯] | "a-eh", between *eye* and *air* | *Nael*, *Aelthar*. English readers who say "nail" are near enough; the Book never depends on it |
| **ea** | [ɛa̯] | *yeah* without the *y* | *Lea*, *-ear*, one syllable |
| **ei** | [ei̯] | v*ei*n | *Eir*, *Nei*, *Seil* |

- **There are no oral stops**: no *p, t, k, b, d, g*.
- **There are also no *m, f, h* (except inside *rh* and *th*), *w* or *y*, and no *o* or *u*.** Those sounds belong to Shoreland.
- **Frequency skew** [rule]:
  - common: *n, l, r, th, s, e, a, ae*;
  - middling: *v, ei, ea*;
  - rare: *rh* and bare *i*.
- **The letters *z*, *x* and *q* never occur**, and nor do the endings *-ion*, *-iel* and *-dor* (FH §9).

### 2.2 · Syllables and words

- **A syllable is (C)V(C).**
  - The onset is any one consonant or none. There are no onset clusters; *rh* and *th* are single sounds.
  - The coda is *l, n, r, s, th, ss, nn* or *nth* (*lenth*, *senth*). The coda *sth* occurs in one root only, *esth* "fire", a worn frequent word.
- **Consonants may meet across syllables,** as in *Es.thaer*, *Rhen.vael*, *Seil.rhass*, *Eir.rhen*, but no more than two consonant sounds in a row. Where a compound would make three, a linking **-e-** goes in.
- **Roots** are mostly one syllable: *ael, thar, seth, nael, rhen*. There are a few old two-syllable roots: *vaere, enna, neira, aven*, and *ralen* and *varen*, which were once compounds.
- **Vowel-final roots take a euphonic -n- before a suffix vowel:** *rei* "go", *rei-n-e* "goes"; *thae* "grow", *thae-n-e* "grows".

### 2.3 · The knock

**The rule** [canon, from every spoken form in the Book]: every word of two or more syllables breaks once, **after its first syllable**, even inside a root: *Ra'lensaen*, *Ra'lenthae*. One-syllable words and the small words never knock.
- A compound is one word and takes one knock: *Nael'saen*.
- A suffixed verb is one word too: *Ral'theine* "remembers".

**What it is:**
- a **glottal catch** [ʔ];
- the syllable before it takes a **high falling pitch**;
- the rest of the word is said level and soft.

Speech therefore comes out in beats of one hard syllable and a soft run, which is why the wall calls the ghost fleet's knocking "the drums". The carved soft reading drops the catch: *Ael'thar* is spoken, and *Aelthar* is carved "whole and soft".

**Why shore ears hear stops.** After the catch, the next consonant is released hard:

| Next sound | Heard as | Example | Rivenman's ear |
|---|---|---|---|
| *th* | [t̪θ] | *Ael'thar* [ˈaɛlʔ.t̪θar] | "Ail-tar" |
| *s* | [ts] | *Nael'saen* [ˈnaɛlʔ.tsaɛn] | "Nail-tsain" |
| *n* | [ⁿd] | *Sen'neir* [ˈsɛnʔ.ⁿdeir] | "Sen-deir" |
| *v, r, rh, l* | a plain catch | *Rhen'vael* | a cough in the word |

**Dialects.** "Each deep of the forest speaks it its own way" [canon]. The grain is the one form they all share, which is why the canon calls it "bridging even the many dialects".
- **Edge speech,** spoken nearest the grey's edge: this is the Guest's dialect, and the one described above.
- **Grove speech,** the council's: the knock is only a pitch-fall, and *th* is voiced between vowels.
- **Deep speech:** the catch is velar, [ʔk], and is heard as a *k*: "*Aelk-thar*".

This is where the Story Bible's "k, t, d" come from. The dialects also differ in a handful of words, but never in the grain.

### 2.4 · History in brief

Seilrhass had an older stage, **the Eldest speech**. It survives in the oldest carved names and in one borrowing. Four changes lead from it to the living tongue, and they account for every irregularity in the canon names.
1. **The old stops were lost.** *\*t* and *\*k* standing after the first syllable became the knock. Elsewhere, *\*t* became *th* and *\*k* became *rh*. The knock is the ghost of a stop, and that is why the drums sound like stone struck.
2. **Final vowels fell after a single consonant** (*\*thaele* > *thael* "tree", *\*senne* > *senn*), but stayed after *r*. So ***vaere*** keeps its *-e*, and so does *Neivaere*.
3. **The collective ending *-aer* was reshaped to *-ear*** by analogy with the singular *-ea* "one of", so that "those of" became "one of" plus *-r*. *Naelear* and *Rhenear* are living forms.
   - ***Esthaer***, the eldest of the Throne-names, was cut before the change and keeps *-aer*.
   - So does the Rivenmen's exonym ***Mystaeri***, an early borrowing that took the old ending and added a Shoreland plural (for the Shoreland designer, §7).
4. **The old agent ending *\*-ane* merged with the plural *-en*.** It survives frozen in ***varen*** "bearer". The living agent ending is ***-ea***.

### 2.5 · Word-building

- **Compounds** are modifier + head, written as one word with one knock:
  - *Nael·saen* "mist-heart", *Rhen·vael* "stone-grain", *Seth·varen* "carving-bearer", *Ael·ralen* "bond-roots": the root-bond, "the bond of roots".
  - The English glosses may run either way; the Seilrhass order never does (inventory §F19).
  - Names may be **who-is compounds**: *Aelrhen*, "bond-stone", is one who binds himself to stone.
- **Suffixes:**

| Suffix | Meaning | Examples |
|---|---|---|
| **-en** (after a vowel **-n**) | plural | *sethen* carvings; *thaelen* trees, a grove; *ennan* children; *thaen* tides |
| **-ea** | one of; one who; on a number, the n-th | *naelea* a Mystaeri; *sethea* a carver; *aelea* a guest; *vannea* the second |
| **-ear** (relic **-aer**) | those of: a whole people or kind | *Naelear*, *Rhenear*, *tharear* kin, *ralear* forebears |
| **-as** | verbal noun: the doing, the thing done | *theinas* a knowing; *rhithas* the felling; *esthas* ash |
| **-eth** (after a vowel **-th**) | causative: make (someone) do | *theineth* teach; *neaseth* show; *reith* send |
| **-e** / **-ne** | verb: it does, it is doing | *raltheine* remembers |
| **-es** / **-nes** | verb: it did | *raltheines* remembered |
| **-ar** | verb: it shall, it is meant to | *reinar* shall go |

- **Zero derivation.** A root is a noun or a verb by its place:
  - *seth*: a carving; to carve;
  - *thae*: a tide; to grow;
  - *thael*: a tree; to rise, to stand;
  - *seil*: a bough; to bend as a bough bends;
  - *nael*: the mist; to veil.

  This is the craft's "lexicon from culture". A tree is a standing, and a bough is a bending.

### 2.6 · Grammar

**Order.** The subject comes first, then the object, then the verb, and nothing follows the verb except the small words that close a clause. Time and place come before the object. Modifiers, possessors and relative clauses come **before** their noun, and postpositions come **after** it.

> *Ve ith naelenn ael raltheine.* · we · own · home · too · remember-PRESENT · "We remember our home too."

**The noun phrase:** *(possessor) (modifier) noun (postposition)*.
- There are **no articles.**
- The demonstrative ***ra*** ("this; the held one") marks a thing that is known or held: *ra vei* "this gift, the gift held out", *ra raltheinas* "the memory". This is the **definite of knowing**. It is why a Mystaeri hand, cutting the Shoreland Title, would supply one word too many: *In **the** memory of…* (Epilogue; for the Shoreland designer, §7).

**Pronouns.** Pronouns are small words and never knock. Seilrhass splits the third person by **animacy**: living things answer; mute things do not.

| | one | more than one |
|---|---|---|
| I / we | *va* | *ve* |
| you | *sa* | *se* |
| he, she, it: a living thing (a person, a tree, a hull) | *la* | *le* |
| it: a mute thing (stone, iron, the dead) | *rha* | *rhe* |
| this, the held one / that | *ra* / *re* | |

- The late, angry wood's contempt is grammatical. It speaks of shore-men with *rhe*, the mute plural.
- The green sliver speaks of them with *le*.
- Possession is a pronoun before its noun: *ve naelenn* "our home". ***Ith*** "own" strengthens it: *ve ith naelenn* "our own home".

**Postpositions** (small words, clitic, all but one on the vowel *i*):

| Word | Meaning | Word | Meaning |
|---|---|---|---|
| *li* | in, at, on | *thi* | through, past |
| *na* | to, toward | *si* | with |
| *rhi* | from, out of | *ri* | against, upon |
| *vi* | for, for the sake of | *vaere* | like, as ("in the face of") |
| *senn* | beneath | *laes* | above, over |

Comparison is reflection: *ral thenn na vaere* means "as a root to water".

**Verbs.**
- **The bare root is the order**, the mood of every carving: *Rei!* "Go!"
- Tense and aspect suffixes follow (§2.5); nothing agrees with the subject.
- **Negation** is the small word ***ni*** before the verb: *ni raltheine* "does not remember".
- **The copula** is ***eiss*** "be so": *Ve se rhesear ni eisse* "We are not your enemies". Existence is *li eisse* "there is".

**Clauses** close with a small word and stand before the main clause:

| Word | Meaning | Example |
|---|---|---|
| *sei* | if | *neas thaesse sei, aven ves thi rei* "if the eye is struck, go by the other road" |
| *anth* | when (literally "at the hour") | *rhen lanthe anth, sae* "when the stone is still, come" |
| *eir* | until (literally "long, to the last") | *rhen aenne eir, thass* "strike until the stone opens" |
| *rhi* | because (literally "from") | *nael vease rhi* "because the sky is dying" |
| *vi* | so that | |

- **Questions** close with ***lae*** (which is also the verb "to ask"): *Rha ressveir eisse lae? Lanthe lae?* "Is it worthless wood? Is it waiting?" This is E3-08's *Is it spent, or waiting?*
- **Relative clauses** use the participle *-ea* before the noun: *renn-ea rhen* "the stone that speaks", which is lexicalised as *rennrhen*, "a gun".

**Adverbs** stand before the verb:
- *ael* together, too, likewise;
- *eir* still, long;
- *eilen* always (literally "all the rings");
- *reil* first;
- *thes* then.

**Numbers** are counted in hands: base five, with *vinn* "hand" meaning five.

| 1 | 2 | 3 | 4 | 5 | 10 | first | second | last | three times |
|---|---|---|---|---|---|---|---|---|---|
| *ith* | *vann* | *raes* | *nal* | *vinn* | *vann vinn* | *reil* (irregular) | *vannea* | *eir* | *raes eil* ("three rings") |

**Irregularity in the frequent words**, each with its history:
- ***varen*** keeps the old agent ending.
- ***reil*** "first" is suppletive; it was once the noun "the fore".
- ***esth*** keeps the only *sth* coda.
- ***Esthaer*** keeps *-aer*.
- ***vaere*** keeps its final *-e*.

### 2.7 · The canon names, analysed

Every coined Mystaeri word in the Book keeps its spelling and its meaning.

| Carved | Spoken | Analysis | Canon gloss | Note |
|---|---|---|---|---|
| **Aelthar** | *Ael'thar* | *ael* bond + *thar* blood | the holiest rite of fellowship | The rite's carved sign is two bloods made one (§5.3) |
| **Aelvaren** | *Ael'varen* | *ael* + *varen* bearer | the Bearer of the Binding | |
| **Aelrhen** | *Ael'rhen* | *ael* + *rhen* stone, a who-is name | bond-to-stone | |
| **Naelear** | *Nael'ear* | *nael* breath + *-ear* those of | those of the breath | |
| **Naelsaen** | *Nael'saen* | *nael* + *saen* heart | mist-hearts | |
| **Rhenear** | *Rhen'ear* | *rhen* + *-ear* | those of stone, who do not hear | In the grain it is cut small (§3.7) |
| **Saenvael** | *Saen'vael* | *saen* + *vael* grain | heart-grain: the Heartwood | |
| **Sethvaren** | *Seth'varen* | *seth* + *varen* | bearer of the carving | |
| **Aelralen** | *Ael'ralen* | *ael* + *ralen* roots | the bond of roots | |
| **sethen** | *Se'then* | *seth* + *-en* | carvings | |
| **Leathae · Vaelthae · Ralenthae · Aelthae · Rhenthae · Eirthae** | *Lea'thae · Vael'thae · Ra'lenthae · Ael'thae · Rhen'thae · Eir'thae* | *lea* green, *vael* grain, *ralen* roots, *ael* bond, *rhen* stone, *eir* deep + *thae* tide | the six Tides | |
| **Thaesaen** | *Thae'saen* | *thae* + *saen* | tide-heart | |
| **Leavaren** | *Lea'varen* | *lea* + *varen* | bearer of new branches | |
| **Vaelress** | *Vael'ress* | *vael* + *ress* rot | the grain that rots | |
| **Ralensaen** | *Ra'lensaen* | *ralen* + *saen* | root-heart | |
| **Rhenvael** | *Rhen'vael* | *rhen* + *vael* | stone-grain | |
| **Esthaer** | *Es'thaer* | *esth* fire + relic *-aer* | "that of fire": the burning | The *-thaer* is the root's *th* plus the old ending, not *thar* "blood" |
| **Senneir** | *Sen'neir* | *senn* beneath + *eir* deep | the deep-beneath | *-neir* is not *nei* "silver" |
| **Eirlenth** | *Eir'lenth* | *eir* + *lenth* winter | the long winter | *Lenth* comes from *lanth* "to wait, a knot", with the vowel of "the season of": winter is the year's waiting. So Eirlenth is "the long wait", the master of the Knot |
| **Naelthar** | *Nael'thar* | *nael* sky + *thar* | blood of the sky | |
| **Neivaere** | *Nei'vaere* | *nei* silver + *vaere* still water, its face | the silvered, the mirror | |
| **Mystaeri** (Shoreland) | — | Shoreland *myst-* + borrowed Eldest *-aer* + Shoreland plural *-i* | "the mist-folk: our word, not theirs" | For the Shoreland designer |

### 2.8 · Phrasebook

| Seilrhass | Spoken | Literally | Use |
|---|---|---|---|
| *Nael si.* | *Nael si.* | with the breath | greeting |
| *Nael si ael.* | | with the breath, you too | answer |
| *Ve raltheine.* | *Ve Ral'theine.* | we remember | the hearth's answer, heard across the water |
| *Vael ra theine.* | *Vael ra Thei'ne.* | the grain holds this | "This is held in the grain." |
| *… ei vael ra eir theine.* | | and the grain still holds the held one | "…and the grain holds it still." |
| *Vael li sethe.* | *Vael li Se'the.* | it is carved in the grain | an oath: anything binding was given to the wood |
| *Veir veir seinne.* | *Veir veir Sein'ne.* | wood heeds wood | "The wood obeys the wood." |
| *Saen leis sethe.* | | the heart carves the morrow | |
| *Seth ra renne, sei ni renne.* | | the carving says "this", it does not say "if" | "The carving says what, and not whether." |
| *Ith li thaess, vann li thaess.* | *Ith li thaess, vann li thaess.* | at one a wound, at two a wound | "Harm to one is harm to both": the Aelthar's promise, and the Stonewright masters' saying, in the other tongue |
| *Rhass anth vi, vael eilen vi.* | *Rhass anth vi, vael Ei'len vi.* | thunder for the hour, the grain for always | II.2's "the thunder is for the moment, the softness for always", as they say it |

### 2.9 · Lexicon (215 entries)

**How to read this.**
- Words marked **canon** are Jack's or the Book's, kept exactly.
- *Sign* names the grain sign that the word reads (§3.5).
- Knock placement follows §2.3 and is not repeated here.

**The canon roots (kept, meanings unchanged)**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *ael* | root | bond, joining; to bind; (adv.) together, too, likewise | **canon**; sign BOND |
| *thar* | root | blood; to bleed | **canon**; sign BLOOD |
| *var* | root | to bear, to carry | **canon** (in varen) |
| *varen* | root | bearer; a laden hull (a Runner) | **canon**; old agent *-ane; sign BEARER |
| *saen* | root | heartwood; the heart of a tree; the middle | **canon**; sign HEART |
| *vael* | root | grain; temper; the carved knowing | **canon** |
| *seth* | root | a carving; an order cut in living wood; to carve | **canon** pl sethen; sign CARVE |
| *thae* | root | tide; a growing; to grow | **canon** pl thaen; sign GROW |
| *lea* | root | green, young; new growth; new | **canon** |
| *ral* | root | a root; a hull sent first (a probe) | **canon** (ralen) |
| *ralen* | root | roots; the root-bond | **canon** = ral + -en |
| *nael* | root | mist, the veil, the breath of the trees, the sky it made; to veil | **canon**; band MIST |
| *rhen* | root | stone, the mute thing; a wall | **canon**; sign STONE (the Mute Square) |
| *eir* | root | deep; old; long; last; (adv.) still; (clause-final) until | **canon** |
| *nei* | root | silver | **canon** |
| *ress* | root | rot, the soft death of wood; to rot | **canon**; sign ROT |
| *lenth* | root | winter; the white season | **canon** |
| *senn* | root | beneath, under; the deep below | **canon** (analysis of Senneir); sign BENEATH |
| *vaere* | root | still water; its face; a reflection; (postp.) like, as | **canon** (analysis of Neivaere); band STILL |
| *esth* | root | fire; to burn | **canon** (analysis of Esthaer); sign BURN |

**Wood, growing, the grove**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *thael* | root | tree; a living trunk; to rise, to stand | thae + old *-l; sign TREE |
| *vath* | root | bark |  |
| *raess* | root | sap |  |
| *eil* | root | a growth ring; a time (once, twice); to count | sign COUNT (bites) |
| *lanth* | root | a knot in the grain; to wait, to hold one's place | sign KNOT (the Knot) |
| *veir* | root | wood, the living stuff |  |
| *lel* | root | leaf |  |
| *veis* | root | seed; the winged seed | sign SEED |
| *seil* | root | bough, branch; a hull; to bend as a bough bends | sign HULL (lens) |
| *rhith* | root | iron; the axe; the felling; to fell | sign AXE |
| *neira* | root | to sing; a song |  |

**Sky, water, world**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *neis* | root | soft light; to shine softly |  |
| *rheis* | root | hard light; the open sun; a flash (of a gun) | sign FLASH (star-notch) |
| *lenn* | root | white; bleached; the white (open sky, snow, blizzard) | band WHITE |
| *veath* | root | night; the dark | band DARK |
| *leis* | root | the morrow; the next coming |  |
| *anth* | root | an hour; (clause-final) when, at the hour that |  |
| *thenn* | root | water; the sea | band WATER |
| *aeth* | root | shore; the edge where water ends | sign SHORE; soft reading of the Wave |
| *reth* | root | ground, earth |  |
| *rhel* | root | frost; to cool | (renamed from leith, a place-name) |
| *reas* | root | wind |  |
| *rhass* | root | storm; thunder; a crack; to crack, to break | sign BREAK |
| *nith* | root | rain |  |
| *enth* | root | edge, rim, margin | sign EDGE |
| *ves* | root | a road; a way over water | sign ROAD |

**Body, person, house**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *vinn* | root | hand; five | sign HAND |
| *lann* | root | arm |  |
| *thal* | root | neck, where life goes up into thought |  |
| *lein* | root | brow, forehead | was *naes*, which is Sindarin for "tooth" (originality pass) |
| *neas* | root | eye; to see, to look | sign EYE |
| *renn* | root | mouth; to speak, to sound aloud | sign MOUTH |
| *eis* | root | name; to name |  |
| *ranth* | root | a word (a spoken thing, which can break) |  |
| *enn* | root | within, inside |  |
| *enna* | root | child | sign SAPLING (children are saplings) |
| *veth* | root | door; the way in | sign DOOR |
| *sath* | root | back, stern; behind |  |
| *reil* | root | fore, front; before; first | soft reading of the Bar Before |
| *aven* | root | other; another |  |
| *ith* | root | one; alone; the same; own | soft reading of the Lone Stroke |

**Acts**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *thein* | root | to hold; to know by touch; a knowing | sign HOLD (the cup) |
| *aenn* | root | open; a gap; between; to open | soft reading of the Breath; sign OPEN |
| *thann* | root | to close; closed | sign CLOSE |
| *rhiss* | root | to take, to seize |  |
| *vei* | root | to give; a gift | sign GIFT |
| *raeth* | root | to kneel | sign KNEEL |
| *rheil* | root | to stop, to cease | sign STOP |
| *veas* | root | to die; dying; death | sign DYING |
| *ilae* | root | to live; to breathe; life | sign LIVE (was thei: clashed with theine "holds") |
| *nenn* | root | to fall, to sink | sign FALL |
| *sae* | root | to come |  |
| *rei* | root | to go | sign GO |
| *neth* | root | to turn, to turn aside | sign TURN-ASIDE |
| *thass* | root | to strike; a blow | sign STRIKE |
| *thaess* | root | to split; a wound; to be struck | sign WOUND (check) |
| *seinn* | root | to hear; to heed |  |
| *veinn* | root | to mend, to make whole | sign MEND |
| *thaval* | root | to hunt, to go for | thavalea a hunter; thavalen the hunters. Was *eneth*, which is Sindarin for "name" (originality pass) |
| *saess* | root | hunger; to hunger | sign HUNGER |
| *rhes* | root | anger; hot |  |
| *senth* | root | dread, fear; the dread | band DREAD |
| *eith* | root | hollow, empty; a seeming | device HOLLOW |
| *iss* | root | thin, slight |  |
| *rhann* | root | heavy, great |  |
| *leas* | root | swift; to run |  |
| *eiss* | root | so; true; what is |  |
| *ilen* | root | to lean, to incline toward |  |

**Numbers (base five, 'hand')**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *vann* | root | two |  |
| *raes* | root | three; (in the grain) many |  |
| *nal* | root | four |  |

**Small words (unknocked clitics)**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *va* | pron | I |  |
| *ve* | pron | we |  |
| *sa* | pron | you (one) |  |
| *se* | pron | you (more than one) |  |
| *la* | pron | he, she; it (a living thing: a person, a tree, a hull) |  |
| *le* | pron | they (living) |  |
| *rha* | pron | it (a mute thing: stone, iron, the dead) |  |
| *rhe* | pron | they (mute) |  |
| *ra* | pron | this; the held one (the definite of a known thing) |  |
| *re* | pron | that; the other one |  |
| *li* | particle | in, at, on (place) |  |
| *na* | particle | to, toward |  |
| *rhi* | particle | from, out of |  |
| *thi* | particle | through, past, by way of |  |
| *laes* | particle | above, over |  |
| *si* | particle | with |  |
| *ri* | particle | against, upon |  |
| *vi* | particle | for, for the sake of; so that |  |
| *ni* | particle | not (before the verb) |  |
| *ei* | particle | and |  |
| *thes* | particle | then, after that |  |
| *sei* | particle | if (closes a clause) |  |
| *lae* | particle | (closes a question); to ask |  |

**Affixes**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *-en* | suffix | plural (after a vowel: -n) | **canon** (sethen) |
| *-ea* | suffix | one of; one who; (on numbers) the n-th |  |
| *-ear* | suffix | those of (a whole people or kind) | **canon**; older -aer |
| *-aer* | suffix | older form of -ear, kept in Esthaer and borrowed in Mystaeri | **canon** relic |
| *-as* | suffix | verbal noun: the doing; the thing done |  |
| *-eth* | suffix | causative: make (someone) do |  |
| *-e* | suffix | verb: it does, it is doing (not past) |  |
| *-es* | suffix | verb: it did (past) |  |
| *-ar* | suffix | verb: it shall, it is meant to |  |

**Names in canon (analysis given; meanings kept)**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *Aelthar* | name | the holiest rite of fellowship: bond-blood | **canon** ael + thar; spoken Ael'thar |
| *Aelvaren* | name | the Bearer of the Binding (the Guest's boat) | **canon** ael + varen |
| *Aelrhen* | name | bond-to-stone (the Guest's errand-name) | **canon** ael + rhen, a 'who-is' name |
| *Naelear* | name | those of the breath (their own name) | **canon** nael + -ear |
| *Naelsaen* | name | mist-hearts: the black pillars; the Thrones' Tide-name | **canon** nael + saen |
| *Rhenear* | name | those of stone, who do not hear: the stone-deaf | **canon** rhen + -ear |
| *Saenvael* | name | heart-grain: the Heartwood | **canon** saen + vael |
| *Sethvaren* | name | carving-bearer: the Standard-Bearer | **canon** seth + varen |
| *Aelralen* | name | the bond of roots: the root-bond | **canon** ael + ralen |
| *Leathae* | name | green tide: the Hasty Tide | **canon** lea + thae |
| *Vaelthae* | name | the tide with grain: the Second Tide | **canon** vael + thae |
| *Ralenthae* | name | root-tide: the Tide of Remembering | **canon** ralen + thae; spoken Ra'lenthae |
| *Aelthae* | name | bond-tide: the Joined Tide | **canon** ael + thae |
| *Rhenthae* | name | stone-tide: the Tide that Learned Deceit | **canon** rhen + thae |
| *Eirthae* | name | deep tide: the Last Tide | **canon** eir + thae |
| *Thaesaen* | name | tide-heart (the Leviathan) | **canon** thae + saen |
| *Leavaren* | name | bearer of new branches (the Hydra) | **canon** lea + varen |
| *Vaelress* | name | the grain that rots (the Plague Herald) | **canon** vael + ress |
| *Ralensaen* | name | root-heart (the Ancient Treant) | **canon** ralen + saen; spoken Ra'lensaen |
| *Rhenvael* | name | stone-grain (the Colossus) | **canon** rhen + vael |
| *Esthaer* | name | the burning, 'that of fire' (the Magma Titan) | **canon** esth + old -aer |
| *Senneir* | name | the deep-beneath (the Sandworm) | **canon** senn + eir |
| *Eirlenth* | name | the long winter (the Frost Wyrm) | **canon** eir + lenth |
| *Naelthar* | name | blood of the sky (the Storm King) | **canon** nael + thar |
| *Neivaere* | name | the silvered, the mirror: silver still-water (the Crystal Lich) | **canon** nei + vaere |
| *sethen* | compound | carvings | **canon** seth + -en |

**New words built by rule**

| Word | Kind | Meaning | Notes |
|---|---|---|---|
| *Seilrhass* | name | 'bough-thunder': the spoken tongue | seil + rhass; spoken Seil'rhass |
| *Eilseth* | name | 'ring-carving': the grain as a written craft | eil + seth; spoken Eil'seth |
| *theinas* | compound | a knowing; the holding | thein + -as |
| *naelenn* | compound | home ('the within of the breath') | nael + enn; spoken Nael'enn |
| *naelea* | compound | one of the long-lived; a Mystaeri | nael + -ea |
| *aethea* | compound | one of the shore; a shore-man (the old, plain word) | aeth + -ea; pl. Aethear |
| *rhenea* | compound | one of stone (a shore-man, in the late and bitter wood) | rhen + -ea |
| *ralthein* | compound | to remember ('to root-hold') | ral + thein; spoken Ral'thein |
| *raltheinas* | compound | a memory | ralthein + -as |
| *aelthein* | compound | to trust ('to hold as bound') | ael + thein |
| *leathein* | compound | to learn ('to hold new') | lea + thein |
| *theineth* | compound | to teach ('to make hold') | thein + -eth |
| *reith* | compound | to send ('to make go') | rei + -eth |
| *neaseth* | compound | to show ('to make see') | neas + -eth |
| *renneth* | compound | to goad ('to make speak') | renn + -eth |
| *rheileth* | compound | to silence ('to make stop') | rheil + -eth |
| *veaseth* | compound | to kill ('to make die') | veas + -eth |
| *aelress* | compound | grief ('the rot of a bond') | ael + ress |
| *rhenseth* | compound | a lie; to mislead ('stone-carving': a cut that carries nothing) | rhen + seth; Rhenthae's coinage |
| *rennrhen* | compound | a gun ('speaking stone') | renn + rhen |
| *rhenneas* | compound | the reach, the watch of a stone ('stone-eye') | rhen + neas |
| *rhenrhass* | compound | a stone-breaker (a Bombard) | rhen + rhass |
| *ennas* | compound | a dwelling; a house ('the within-place') | enn + -as |
| *rhenennas* | compound | a castle ('stone-house') | rhen + ennas |
| *eithseil* | compound | straw; a phantom hull ('hollow bough') | eith + seil |
| *ressveir* | compound | worthless wood; a spent hull | ress + veir |
| *isseil* | compound | thin wood; a cheap hull | iss + seil |
| *rhannseil* | compound | the great hull | rhann + seil |
| *thannvinn* | compound | the kept hand ('closed hand'): the reserve | thann + vinn |
| *issralen* | compound | root-men ('fine roots') | iss + ralen |
| *rhasseil* | compound | the ram ('breaking bough') | rhass + seil |
| *leasen* | compound | the swift (Corsairs) | leas + -en |
| *thavalen* | compound | the hunters (Reavers) | thaval + -en |
| *seilen* | compound | the host (many hulls) | seil + -en |
| *neivath* | compound | silverbark; a silver elder | nei + vath |
| *neivathen* | compound | the council ('the silverbarks') | neivath + -en |
| *thaelen* | compound | a grove | thael + -en |
| *leathael* | compound | a sapling | lea + thael |
| *naelneis* | compound | the between-light | nael + neis |
| *eirrhen* | compound | the mountain ('old stone') | eir + rhen |
| *esthas* | compound | ash ('what is burnt') | esth + -as |
| *rhithveir* | compound | timber ('felled wood') | rhith + veir |
| *rhithas* | compound | the felling | rhith + -as |
| *tharear* | compound | kin ('those of the blood') | thar + -ear |
| *ralear* | compound | forebears; mothers and fathers | ral + -ear |
| *eirea* | compound | an elder | eir + -ea |
| *aelea* | compound | a guest ('one of the bond') | ael + -ea |
| *vethea* | compound | a host, the master of a house ('one of the door') | veth + -ea |
| *rhesea* | compound | an enemy ('one of anger') | rhes + -ea |
| *sethea* | compound | a carver | seth + -ea |
| *Eirsethea* | name | the Last Carver | eir + sethea; spoken Eir'sethea |
| *leisthein* | compound | to hope ('to hold the morrow') | leis + thein |
| *lelneis* | compound | blossom ('leaf-light') | lel + neis |
| *eirveir* | compound | the eldest wood; Myststone ('old wood') | eir + veir |
| *leaveir* | compound | green wood | lea + veir |
| *eilen* | compound | all; the whole; (adv.) always ('all the rings') | eil + -en |
| *rheissae* | compound | east ('sun-coming') | rheis + sae |
| *rheisnenn* | compound | west ('sun-falling') | rheis + nenn |
| *lennves* | compound | north ('the white road') | lenn + ves |
| *rhesves* | compound | south ('the warm road') | rhes + ves |
| *vannrenn* | compound | 'two mouths': a feint | vann + renn; soft reading of the Two Mouths |
| *sathneth* | compound | 'stern-turning': a turning for home | sath + neth; soft reading of the Turned Stern |
| *reaslel* | compound | a sail ('wind-leaf') | reas + lel |
| *naelseth* | compound | 'veiled carving': a hidden thing | nael + seth; soft reading of the Smoothed Cut |
| *eisranth* | compound | a soft reading: the unbroken name of a grain sign ('name-word') | eis + ranth |
| *rhelranth* | compound | the soft letters that spell sound on stone ('frost-words') | rhel + ranth; Appendix A |

### 2.10 · Audit

- **Checked.** The whole lexicon was run through a checker (`wf6/lang/check_lex.py`). It tests three things:
  - phonotactics;
  - duplicate forms;
  - a blacklist of the Tolkien forms named in craft §4d and the Name Map, plus the known franchise and Celtic forms: Witcher Elder Speech, Wheel of Time Old Tongue, Dragon Age Elvish, Warcraft Thalassian, the Aldmeris and Eldar forms, High Valyrian elements, Welsh, Irish and Scots.
- **Changed while designing.** Five draft forms collided and were replaced:
  - *nae* is Scots for "no", so the question word is *lae*;
  - *leith* is a place-name, so frost is *rhel*;
  - *thil* is a Tolkien root ("shine"), so three is *raes*;
  - *thei* "live" collided with *theine* "holds", so live is *ilae*;
  - *Ennael* is a fan character's name, so home is *Naelenn*.
- **Flagged, kept.**
  - ***lanth*** "knot, wait". Sindarin *Lanthir* is from *lamthir* "waterfall", and *lanth* is not a standalone Sindarin word (Eldamo). The overlap is form-only, which the Name Map's own standard allows, as it did for *ael*. Alternative if Jack wants distance: *aneth*.
  - ***nael*** (canon). It sits near Irish *néal* "cloud" in sense, though not in form. It is Jack's word and stays.
- **Still to run before any of this ships.** Two checks remain, as the Name Map did for names:
  - an exact-string web search of every new root of two or more letters against Eldamo, Parf Edhellen, teanglann.ie and the Geiriadur;
  - the same search against the franchise wikis.

  **Only seven headline words were searched in this pass** (§1).

---

## 3 · EILSETH, THE GRAIN

### 3.1 · What it is

- **Semasiographic.** A carving records meaning, not sound, which is why the canon has it "bridging even the many dialects" of the thunder-tongue. The canon already makes the case: "whoever lays a hand on the carving knows what the carver meant, whatever tongue the carver spoke".
- **Taken whole.** The Bonded take a round in at once, as a memory; the reading order in §3.12 exists only for eyes and programs.
- **Grown, not written.**
  - Rings are growings (*thae*), and a later carving contains its earlier forms.
  - The knife-cut is a V with two flat facets, one lit and one in shadow.
  - It is the opposite, visually, of an ink logogram.
- **Every sign has a soft reading** (*eisranth*): the Seilrhass word for its meaning, spoken without the knock. The ten root signs keep Seren's English names as well; she names them by the look of the stroke ("The root, as I name it", the Book of Knowings).
- **Truth or nothing** [rule]. Every round the player sees is a real encoding of a real knowing (craft §7). No round ever carries decorative pseudo-marks. Empty wood is drawn as rings with no marks, which in the grain means exactly "nothing is cut here".

### 3.2 · The round: anatomy and geometry

A carving is laid out as a **round**, the end-face of a trunk cut across. On a plank the same marks run lengthwise "with the grain" (V.1); §3.10 covers planks. All numbers below are in drawing units. The round's drawing box is its own bounding box; §3.11 covers display size.

| Part | Real anatomy | Rule |
|---|---|---|
| **Pith** | the centre of the stem | radius 4.5. **Round** for wood grown in peace. **Square** (side 9, turned to the axis) for every heart and hull grown since the council's vote: this is the **war-pith**, *Grow until the shore is silent* "beneath all the other carvings", which the wood "cannot unlearn" (V.4). A round never has more than one pith, except in the Joined Tide |
| **Heart ring** (ring 1) | juvenile wood: the fast first growth, wide | width 72 in a sapling round. Otherwise clamp(0.22 × the sum of the other ring widths, 56, 96). **The root sign is cut here, from the pith outward, and is the largest mark** |
| **Growth rings** (rings 2…K) | growth rings, each an earlywood/latewood pair | marked ring width 46 × seeded(0.84…1.20); empty ring width 18 × seeded(0.90…1.15). K ≤ 24. V.6, the longest leaf, has 24 paragraphs. Above 13 rings, marked rings shrink toward a minimum width of 26. Each ring is a latewood line (weight 2.2) with a paler earlywood band inside it. Two or three **year-hairlines** per ring (weight 0.5, 35% opacity) show the years and carry nothing |
| **Band-rule** | a false ring: a growth stop in mid-season | the ring line is **doubled** (a second line 5 units outside it). There are two per round, and they part the three bands (§3.3). They are the Book's two `RING` markers made visible |
| **Included bark** | bark overgrown by later wood | a dark, rough line 4.5 wide on a ring. It marks where an older carving ended and a later Tide grew over it (§3.9) |
| **Bark** | the bark | a rough band 12 + 4 × min(K, 6) wide outside ring K. Its outer contour is noise made of harmonics 5, 7, 11, 17, 29 and 41 (amplitudes 1–4). It is crossed by radial fissure hairlines. **No mark ever crosses the outer contour.** Marks in the bark are limited to names, the seal and pale rings (§3.7) |
| **Heartwood / sapwood tint** | the colour of old wood | the rings inside band-rule 1 are tinted heartwood. A sapling (Hasty wood, the green sliver) has no heartwood and is tinted green-wood. Myststone is overlaid in stone-grey |

**Ring shape.** All rings of a round share one shape around the pith, so they never cross:
- r_k(θ) = R_k · f(θ) + j_k(θ).
- f(θ) = 1 + ε·cos(θ − φ) + Σ_{m=2..5} a_m·sin(mθ + ψ_m), with ε ∈ [0.04, 0.09] (the eccentric pith of a leaning trunk) and a_m ∈ [0.010, 0.022]/(m − 1).
- j_k is a small per-ring wobble of about 2% of R_k, always under a fifth of the gap to the next ring.
- A **knot** pushes the ring lines near it outward by A·exp(−(Δθ/σθ)²)·exp(−(Δρ/σρ)²), with A = 0.3 × the smallest ring width, so the grain visibly flows around it.
- Sample each ring at 72–96 points and close it with Catmull-Rom converted to cubic Bézier.

**The seed.** Every free parameter (ε, φ, the harmonics, ring widths, jitter, the bark noise, the ±3° mark jitter and the ±12° axis turn) comes from **mulberry32 seeded with FNV-1a of the round's id** (for example `E1-01`, `IV-4-gift`, `I-1-facing`). The same round is the same drawing for every reader. That is the Book's law of determinism.

### 3.3 · How a round is read

**The axis.** The root sign is cut from the pith outward in the heart ring, and its direction is **the axis**.
- Everything is read relative to it. The page may turn the round; the decoder finds the root first.
- The Book draws the axis near the top, turned by a seeded ±12° so that no two rounds line up mechanically. A sample may fix the turn: the Stone's axis points right, to keep the top clear for its letters (§5.7).

**Files (angle = who and where).** A round has 16 **files**, radii at 22.5° steps clockwise from the axis, numbered 0–15.
- A mark stands on one file, jittered ±3°, where a slot is ±11.25° wide.
- **Everything cut on one file within a band is about one referent**: one hull-group, one road, one stone, one people.
- Across a band-rule a file may be reused, and only a ray says it is still the same one.
- **Even files are bearings**, relative to the carving's main road, facing the shore:

| File | Bearing |
|---|---|
| 0 | ahead, toward the shore on the main road |
| 4 | the right hand |
| 8 | behind: home, the grey, the other side |
| 12 | the left hand |
| 2, 6, 10, 14 | the diagonals |

- **Odd files are placeless**: referents with no road.
- Real compass names (east, north) belong to Halyna's telling. The Knowing generator fills them from the board (Ad: "the bearings are the generator's to fill").
- **In a joined round** (several piths, §3.9 G8) [rule]:
  - files, radii and each mark's local frame in the **shared rings** are taken about **the round's centre**, the point the piths stand around. "Outward" there is away from that centre, not away from the nearest pith;
  - the axis runs from the centre through pith 0, and **every pith's root points along it**, so the roots show the axis even where the shared rings are empty;
  - a mark on a pith's **own** rings takes that pith as its centre instead (GN `pN·`).

  A decoder who measures a shared-ring mark about the nearest pith turns it sideways: E4-01's BOND then reads as an unknown three-armed cut (decode test, §10.11).

**Rings (radius = when).**
- **One ring is one step.**
- **Marks in the same ring happen together, at one hour.** "Three roads, one hour" is three marks in one ring.
- **Outer rings come after inner rings.** A thin **empty ring** means *a morrow passes*: one coming, one sortie.
- **A mark stretched across rings i…j** holds through those steps: "until".

**The three bands (beginning, middle, end).** Band-rule 1 parts band I from band II, and band-rule 2 parts band II from band III. What a band holds depends on the kind of round:

| Band | In an **order** (a *seth*: the 46 carvings, *Burn*, the council's carving) | In a **telling** (a *theinas*: the wood leaves, the gift, the sliver, the Stone) |
|---|---|---|
| **I, the heart** | the root: what kind of order this is (its line), plus any older carving it grew from | the first movement. **One ring per paragraph** |
| **II, the sap** | the parts: who, where, what each group is told, who waits on whom | the second movement, one ring per paragraph |
| **III, the bark rings** | the turnings: *if* and *else*, the home clause, and the aim (*Cut against*) | the third movement, one ring per paragraph |
| **the bark itself** | the name of whoever grew it (a Tide or a Throne) | the **seal**: *This is held in the grain … and the grain holds it still* |

- **A sapling** (Hasty wood, *Burn*, the green sliver) is too young to have heartwood. It is all heart: one ring and no rules.
- **Second-Tide wood** has band-rule 1 (its sapling's overgrown bark) and an empty band III.
- **Each wood leaf's round** has exactly as many rings as the leaf has paragraphs. Its two band-rules fall where the leaf's two `RING` markers fall. The formula paragraph "This is held in the grain" is the seal, not a ring.

### 3.4 · Marks, the local frame and the classifier

**The local frame.** Every sign is defined once, in a frame that is then placed on its file and ring.
- **u** runs 0 → 1 along the file, from the inner edge of the mark's span to its outer edge.
  - The span runs from R_{i−1}(θ) + pad to R_j(θ) − pad, with pad = max(3, 0.09 × ring width).
  - For the root sign, the span starts at the pith.
- **v** runs across the file, in units of **B**, the mark's half-breadth; + is clockwise.
  - B = min(30, 0.8 · ρ_mid · 0.3927) for an ordinary mark.
  - B = min(60, 0.95 · ρ_mid · 0.589) for the root, which owns files 15, 0 and 1 of the heart ring.
- A world point is **P(u, v) = base + u·L·ê_r + v·B·ê_t**, where:
  - base = pith + ρ_in·ê_r(θ) + v_off·B·ê_t(θ) (in a joined round: for a mark on its own pith's rings, that pith; for a mark in the shared rings, the round's centre, §3.3);
  - ê_r = (sin θ, −cos θ) and ê_t = (cos θ, sin θ) in SVG coordinates, with θ clockwise from up;
  - L = ρ_out − ρ_in.
  - A leaning mark (the pair device) rotates ê_r and ê_t about its foot.

**Element types.** A sign is a list of elements drawn in that frame. Lengths of lenses and drops are fractions of L; all other sizes are in B.

| `t` | Parameters | Drawn as |
|---|---|---|
| `cut` | `p` (points), `bend` (sag in B), `curl` {r, sweep°, dir ±1, tail}, `curve` (a smooth curve through three or more points), `straight`, `fill`, `k` (width factor), `hollow`, `smooth` | a V-cut stroke tapered at both ends; a curl continues it along a circular arc (dir +1 = clockwise) |
| `bar` | `u`, `v0`, `v1` | a straight tapered cut across the file |
| `ringarc` | `u`, `v0`, `v1` | a cut that follows the ring (concentric) |
| `star` | `c`, `r` | a star-notch: five tapered V-cuts radiating from one point, one of them on the file |
| `lens` | `c`, `len`, `w`, `rot`, `fill` | a closed curved groove, a pointed vesica: wood-world |
| `drop` | `c`, `len`, `w`, `point` | a closed curved teardrop: wood-world |
| `square` | `c`, `s` | a closed straight groove: stone-world |
| `wedge` / `tri` | `apex`, `base`, `w` / three points | a solid triangle in two facets |
| `check` | `u0` (outer), `u1` (inner), `v`, `w` | a jagged dark split, widest at its outer end (a real check opens toward the bark) |
| `scar` | `apex`, `base`, `w` | a charred wedge plus two callus lips at its base |
| `knot` | `c`, `rx` (B), `ru` (L) | an oval groove with a dark heart; it deflects the rings around it |
| `cup` | `c`, `r`, `form`: hold `( )`, open `) (`, palm `U` | two opposed arcs, or one U |
| `rootfoot` | `c`, `dir`: in / out | three roots of unequal spread and length (−64°, −10°, +38°; 0.40, 0.30, 0.36 B), each bowing outward as real roots flare. Never an even three-tine fork, which is the rune algiz (§3.13) |

**Handedness and the entry-nick.** Negation is the mirror image (§3.7). So every sign must look different from its mirror.
- Signs that are chiral already (the Wave, the Lone Stroke, the Turned Stern, TURN, KNEEL, AXE, LEAN, HOME, SAIL, and TREE, PILLAR and SAPLING with their alternate boughs) need nothing more.
- Every other sign carries the **entry-nick**: a short cut entering beside its head from the clockwise side, at about 50°, length 0.16 B, width 0.55 H.
- The nick is where the knife goes in. Mirrored, it is on the other side.

**The classifier: line quality** [rule]. The line quality of a **closed shape** tells what world a thing belongs to:
- **Straight-edged** (the square and its kin) means **of stone**: the mute thing, the wall, the gun, the house behind the stone, the shore-men's own home, the door.
- **Curved** (lens, drop, loop) means **of wood**: bough, hull, seed, heart, home, one of us.

The same person-figure with a square crown is **one of stone**, and with a lens crown is **one of us**. Open strokes (acts) are not classified.

**Weight carries nothing** [rule]. The stroke half-width H is fixed per round:
- H = 0.14 B for ordinary marks (1.6–6.5);
- H = 0.15 B for the root (3.0–6.5).

A thicker cut never means louder or more urgent. That device belongs to Arrival (craft §2b).

### 3.5 · The sign inventory (70 signs)

**The eleven that open a carving: the ten roots and *Burn*.** Each root keeps Seren's name, and each is drawn from her exact words (Book of Knowings, L1375–1384). As the heart-ring root of a Hasty sapling, the sign alone carries the whole young-wood order: "one word to a hull". Elsewhere, it carries its line's lasting signature (Ad §9a).

| Id | Seren's name | Soft reading | Meaning | What is cut | Entry-nick |
|---|---|---|---|---|---|
| **WAVE** | the Wave | *aeth* | to the shore: all at once, by the straightest water, none waiting on another | a bowed cut from the pith whose head curls clockwise over itself, about 200°, like a crest about to break | no (chiral) |
| **LONE** | the Lone Stroke | *ith* | one goes ahead of the rest | a long cut, a gap, then a short cut beyond it, set a little clockwise: the short one has turned aside | no (chiral) |
| **BARB** | the Bar Before | *reil* | a screen before the bearer | a full cut crossed near its head by a bar that lies along the ring; the cut runs on through the bar | yes |
| **SPARK** | the Spark | *rheis* | where the stone flashed, strike there | a cut ending in a five-point star-notch | yes |
| **SQUARE** | the Mute Square | *rhen* | stone; the wall; the mute thing | a closed square groove, the only closed straight shape among the roots | yes |
| **MOUTHS** | the Two Mouths | *vannrenn* | loud in one place; the landing in another | two parallel full cuts; the counter-clockwise one is cut hollow (outline only) | no (chiral) |
| **STERN** | the Turned Stern | *sathneth* | turn the stern for home | a cut that hooks 180° counter-clockwise and runs back inward beside itself | no (chiral) |
| **BREATH** | the Breath | *aenn* | between their blows: go in the gap | two cuts on one line with an open gap between them | yes |
| **KNOT** | the Knot | *lanth* | wait in the grey; come when the shore is still | a cut that stops in an oval knot; the ring lines bow around the knot, as real grain flows around a branch | yes |
| **SMOOTH** | the Smoothed Cut | *naelseth* | hidden in the grey: go veiled | a bowed cut drawn as two faint edges only, with no facets and no shadow | no (chiral) |
| **BURN** | Burn | *esth* | burn | a fire scar: a charred wedge from the pith, lipped with callus where the wood grew back over it | yes |

**A root alone in a sapling** [rule]. The Meaning column above is the root's lasting signature, which is what it says when it opens an older carving. **Cut alone in green wood, it says its line's whole young-wood order instead**, and that order is read from the sign's own anatomy. A decoder of a Hasty round reads this table, not the one above (§5.5 shows how each stroke carries its clause):

| Root | The one word (K1) | The whole young-wood order (known at Cam 13) |
|---|---|---|
| WAVE | *shore* | *To shore. As root to water, go. Wait on no bough.* |
| SQUARE | *wall* | *Break wall. First stone, only stone. Strike till it opens or wood is ash.* |
| LONE | *go* | *Go until struck. Where bark splits, turn aside.* |
| BARB | *before* | *Before bearer, thin wood. Thin wood falls; bearer keeps pace.* |
| SPARK | *flash* | *Where it flashed, strike. Last flash, only flash.* |
| KNOT | *grey* | *Wait in grey, as seed waits out frost. When stone is still, come.* |
| STERN | *home* | *Home when wounded. One bough falls; all turn, each by its own water.* |
| BURN | — | *Burn.* |

The two are one meaning at two ages: LONE's signature, *one goes ahead of the rest*, is what *go until struck; turn aside* became once the line had grown. The decode test (§10.11) read E1-03 as the signature and missed the order; this table is why that cannot happen again.

**Acts** (open strokes):

| Id | Soft reading | Meaning | What is cut | Entry-nick |
|---|---|---|---|---|
| **GO** | *rei* | go | a plain cut, slightly bowed | no (chiral) |
| **STRIKE** | *thass* | strike | a cut ending in a solid wedge (the blow landing) | yes |
| **BREAK** | *rhass* | break | a cut whose head opens into a split | yes |
| **WOUND** | *thaess* | struck; the bark splits | a check: a jagged split from the ring's outer edge inward | yes |
| **TURN** | *neth* | turn aside | a cut with a sharp kink to the clockwise side | no (chiral) |
| **HOLD** | *thein* | hold; know | two opposed arcs, ( ), cupped around the file | yes |
| **OPEN** | *aenn* | open; come open | two opposed arcs turned outward, ) ( | yes |
| **CLOSE** | *thann* | close | the cup ( ) with a bar across its head | yes |
| **MOUTH** | *renn* | speak aloud; a voice | an open lens: two arcs joined at the foot and parted at the head | yes |
| **FALL** | *nenn* | fall; sink; go down | a cut whose foot droops into a hook (the head points down into the wood) | no (chiral) |
| **RISE** | *thael* | rise; stand | a cut ending in a bud (a small pointed lens) | yes |
| **GROW** | *thae* | grow | a cut with four leaf-strokes springing **alternately**, one side then the other, up its length: a sprig. (Two opposed pairs drew two stacked algiz runes, §3.13) | yes |
| **LIVE** | *ilae* | live; breathe | a cut with one leaf on a short stalk | no (chiral) |
| **DYING** | *veas* | die; dying | a cut that breaks into shorter and shorter pieces toward its head | yes |
| **KNEEL** | *raeth* | kneel | a cut that folds back sharply on itself at its head and **comes to rest on the ground**: the stem stops at seven-tenths of its space, the fold runs back toward the pith on the clockwise side, and the cut then runs on **along the ring**, the shin laid on the ground (one unbroken cut of three strokes). **Nothing is cut above the fold**, which is what tells it from AXE. (The fold alone was the rune laguz, §3.13) | no (chiral) |
| **GIFT** | *vei* | give; a gift laid down | a lens laid on a bar: a thing set down before | yes |
| **BOND** | *ael* | bind; join; together | two cuts that grow together into one (the branches of two trees fused): each **bows in and meets the stem tangentially**, as fused stems do, and their feet are unequal. (Two straight arms drew the inverted Y of Cirth *h*, §3.13) | yes |
| **STOP** | *rheil* | stop; cease | a cut ending against a bar that lies along the ring; nothing beyond the bar | yes |
| **MEND** | *veinn* | mend (with stone) | two cuts on one line with a small stone square set in the gap | yes |
| **ROT** | *ress* | rot | a cut crumbled into five short pieces, offset | yes |
| **AXE** | *rhith* | iron; fell; the felling | a dead-straight haft **running the whole space**, with a solid blade on its clockwise side at the head: a three-faceted triangle hanging from the haft's top, its broad edge parallel to the haft | no (chiral) |
| **CARVE** | *seth* | carve; a carving; marks | two slightly bowed cuts meeting at the foot: the V of a knife-cut | yes |
| **LEAN** | *ilen* | lean toward; lean after | a single cut set obliquely across the ring | no (chiral) |
| **BEND** | *seil* | bend, as a bough bends; give ground in shape | a deeply bowed cut | no (chiral) |
| **BENEATH** | *senn* | beneath; go under | a bar along the ring at the head, and a cut below it that does not reach it | yes |

**Things** (closed shapes classify; `x3` = many; see §3.7):

| Id | Soft reading | Meaning | Line | What is cut | Entry-nick |
|---|---|---|---|---|---|
| **HULL** | *seil* | a bough; a hull | curved (wood) | a lens (a pointed vesica) along the file: a bough, a hull | yes |
| **BEARER** | *varen* | a bearer; a laden hull | curved (wood) | the hull with a cut along its length inside it: laden | yes |
| **THIN** | *isseil* | thin wood; a cheap hull | curved (wood) | a very narrow hull | yes |
| **SPENT** | *ressveir* | worthless wood; a spent hull | curved (wood) | the hull split along its length by a check | yes |
| **GREAT** | *rhannseil* | the great hull | curved (wood) | a broad hull with a rib along the ring across its middle | yes |
| **EYE** | *neas* | an eye (a hull sent to look); to look | curved (wood) | a short lens with tails at both tips | yes |
| **HUNTER** | *thavalea* | a hunter | curved (wood) | a hull with a star-notch at its fore tip | yes |
| **SWIFT** | *leas* | the swift | curved (wood) | a short hull with two wake-lines behind it | yes |
| **BREAKER** | *rhenrhass* | a stone-breaker | curved (wood) | a hull with a small square at its fore tip | yes |
| **RAM** | *rhasseil* | the ram | curved (wood) | a hull with a wedge at its fore tip | yes |
| **ROOT** | *ral* | a root; a hull sent first; (x3) root-men | — | a cut ending in a root-foot at its head, three unequal roots flaring (a root reaching forward); ×3 = root-men | yes |
| **SEED** | *veis* | the winged seed; the sky falling | curved (wood) | a small lens with two swept wings at its foot: the winged seed | yes |
| **TREE** | *thael* | a tree | — | a trunk with two boughs springing from it near the head **at different heights, one to each side**, each bowing upward. (Two boughs from one point drew the rune algiz, §3.13) | no (chiral: the lower bough is on the clockwise side) |
| **PILLAR** | *naelsaen* | a black pillar, a mist-heart | — | the tree with its trunk cut solid (black) | no (chiral, as TREE) |
| **SAPLING** | *leathael* | a sapling; a child | — | a small tree standing in the outer half of its space | no (chiral, as TREE) |
| **HEART** | *saen* | a heart; heartwood | curved (wood) | a small lens cut solid | yes |
| **US** | *naelea* | one of us (the long-lived) | curved (wood) | a root-foot, a stem and a lens crown: one who stands rooted, of wood | yes |
| **STONEFOLK** | *aethea* | one of stone; a shore-man | straight (stone) | a root-foot, a straight stem and a square crown: one who stands rooted, of stone | yes |
| **HOME** | *naelenn* | home (a place loved) | curved (wood) | a cut that hooks back and closes on itself in a round loop: the Turned Stern made whole | no (chiral) |
| **HOMESTONE** | *naelenn* | home (of stone: theirs) | straight (stone) | the same loop drawn straight and square: a home of stone | no (chiral) |
| **SHORE** | *aeth* | a shore | — | a bar along the ring with a small wave curling at its clockwise end | no (chiral) |
| **ROAD** | *ves* | a road; a way over water | — | two close parallel cuts: a lane | yes |
| **EDGE** | *enth* | an edge; the rim (of the dread, of the grey) | — | an arc following the ring at the head of its space | yes |
| **GUN** | *rennrhen* | a speaking stone; a gun | straight (stone) | a square with a star-notch at its head: a speaking stone | yes |
| **CASTLE** | *rhenennas* | the house behind the stone; a castle | straight (stone) | a large square with a small square behind it, joined: the house behind the stone | yes |
| **DOOR** | *veth* | a door | straight (stone) | two straight posts **battered in** toward a bar across their heads, as an old stone doorway's jambs lean. (Upright posts drew Greek Π and Cirth *a*, §3.13) | yes |
| **FLASH** | *rheis* | a flash; hard light; the open sun | — | a five-point star-notch alone | yes |
| **BLOOD** | *thar* | blood | curved (wood) | a drop, point toward the pith | yes |
| **GRIEF** | *aelress* | grief (a wound the wood has grown over) | — | a check whose head the callus has closed over: a wound the wood has grown around | yes |
| **SAIL** | *reaslel* | a sail; a cloth in the wind | — | a mast under one cloth **bellied by the wind**, a curve over its head that hangs lower on the clockwise side: a square sail seen from astern. (A triangle on the mast was the rune thurisaz, §3.13) | no (chiral: the lopsided belly) |
| **HAND** | *vinn* | a hand; (after a thing) five | — | a stem ending in an open palm (a U turned to the bark) | yes |
| **TIDE** | *thae* | a tide; a growing | — | an arc along the ring with a shoot rising from it | yes |
| **DEEP** | *eir* | deep; old; long; last | — | a cut standing on a floor-bar at its foot | yes |
| **AELTHAR** | *aelthar* | the Aelthar: two bloods made one | curved (wood) | two drops at the foot whose stems bow in and grow together into one, as BOND's do but evenly: two bloods made one | yes |

**The inventory as data.** These are the exact parameters drawn by the prototype (`wf6/grain/signs.json`). u and v are in the local frame of §3.4.

```json
{
 "WAVE": {"cls":"root","soft":"aeth","els":[{"t":"cut","p":[[0.04,0],[0.64,0]],"bend":0.05,"curl":{"r":0.42,"sweep":200,"dir":1}}]},
 "LONE": {"cls":"root","soft":"ith","els":[{"t":"cut","p":[[0.04,-0.24],[0.58,-0.24]],"bend":0.04},{"t":"cut","p":[[0.72,0.24],[0.97,0.24]]}]},
 "BARB": {"cls":"root","soft":"reil","nick":true,"els":[{"t":"cut","p":[[0.04,0],[0.97,0]]},{"t":"ringarc","u":0.74,"v0":-0.7,"v1":0.7}]},
 "SPARK": {"cls":"root","soft":"rheis","nick":true,"els":[{"t":"cut","p":[[0.04,0],[0.66,0]]},{"t":"star","c":[0.84,0],"r":0.42}]},
 "SQUARE": {"cls":"root","soft":"rhen","q":"straight","nick":true,"els":[{"t":"square","c":[0.54,0],"s":1.05}]},
 "MOUTHS": {"cls":"root","soft":"vannrenn","els":[{"t":"cut","p":[[0.06,-0.42],[0.94,-0.42]],"hollow":true},{"t":"cut","p":[[0.06,0.42],[0.94,0.42]]}]},
 "STERN": {"cls":"root","soft":"sathneth","els":[{"t":"cut","p":[[0.04,0],[0.8,0]],"curl":{"r":0.42,"sweep":180,"dir":-1,"tail":0.36}}]},
 "BREATH": {"cls":"root","soft":"aenn","nick":true,"els":[{"t":"cut","p":[[0.04,0],[0.4,0]]},{"t":"cut","p":[[0.62,0],[0.97,0]]}]},
 "KNOT": {"cls":"root","soft":"lanth","nick":true,"els":[{"t":"cut","p":[[0.04,0],[0.55,0]]},{"t":"knot","c":[0.74,0],"rx":0.55,"ru":0.13}]},
 "SMOOTH": {"cls":"root","soft":"naelseth","els":[{"t":"cut","p":[[0.04,0],[0.95,0]],"bend":0.34,"smooth":true}]},
 "BURN": {"cls":"root","soft":"esth","nick":true,"els":[{"t":"scar","apex":[0.06,0],"base":0.95,"w":0.8}]},
 "GO": {"cls":"act","soft":"rei","els":[{"t":"cut","p":[[0.08,0],[0.92,0]],"bend":0.1}]},
 "STRIKE": {"cls":"act","soft":"thass","nick":true,"els":[{"t":"cut","p":[[0.08,0],[0.7,0]]},{"t":"wedge","apex":[0.97,0],"base":0.71,"w":0.42}]},
 "BREAK": {"cls":"act","soft":"rhass","nick":true,"els":[{"t":"cut","p":[[0.08,0],[0.64,0]]},{"t":"check","u0":0.98,"u1":0.6,"v":0,"w":0.34}]},
 "WOUND": {"cls":"act","soft":"thaess","nick":true,"els":[{"t":"check","u0":0.98,"u1":0.22,"v":0,"w":0.3}]},
 "TURN": {"cls":"act","soft":"neth","els":[{"t":"cut","p":[[0.08,0],[0.56,0],[0.9,0.78]]}]},
 "HOLD": {"cls":"act","soft":"thein","nick":true,"els":[{"t":"cup","c":[0.54,0],"r":0.56,"form":"hold"}]},
 "OPEN": {"cls":"act","soft":"aenn","nick":true,"els":[{"t":"cup","c":[0.54,0],"r":0.56,"form":"open"}]},
 "CLOSE": {"cls":"act","soft":"thann","nick":true,"els":[{"t":"cup","c":[0.5,0],"r":0.52,"form":"hold"},{"t":"bar","u":0.92,"v0":-0.5,"v1":0.5}]},
 "MOUTH": {"cls":"act","soft":"renn","nick":true,"els":[{"t":"cut","p":[[0.16,0],[0.52,-0.5],[0.86,-0.22]],"bend":0},{"t":"cut","p":[[0.16,0],[0.52,0.5],[0.86,0.22]],"bend":0}]},
 "FALL": {"cls":"act","soft":"nenn","els":[{"t":"cut","p":[[0.94,0],[0.26,0]],"curl":{"r":0.3,"sweep":130,"dir":1}}]},
 "RISE": {"cls":"act","soft":"thael","nick":true,"els":[{"t":"cut","p":[[0.1,0],[0.78,0]]},{"t":"lens","c":[0.89,0],"len":0.16,"w":0.3}]},
 "GROW": {"cls":"act","soft":"thae","nick":true,"els":[{"t":"cut","p":[[0.05,0],[0.95,0]]},{"t":"cut","p":[[0.3,0],[0.45,0.42]]},{"t":"cut","p":[[0.44,0],[0.59,-0.42]]},{"t":"cut","p":[[0.58,0],[0.73,0.42]]},{"t":"cut","p":[[0.72,0],[0.86,-0.38]]}]},
 "LIVE": {"cls":"act","soft":"ilae","els":[{"t":"cut","p":[[0.08,0],[0.92,0]]},{"t":"cut","p":[[0.5,0],[0.6,0.3]]},{"t":"lens","c":[0.72,0.46],"len":0.3,"w":0.2,"rot":-38}]},
 "DYING": {"cls":"act","soft":"veas","nick":true,"els":[{"t":"cut","p":[[0.06,0],[0.4,0]]},{"t":"cut","p":[[0.48,0],[0.65,0]],"k":0.8},{"t":"cut","p":[[0.72,0],[0.81,0]],"k":0.6},{"t":"cut","p":[[0.87,0],[0.91,0]],"k":0.45}]},
 "KNEEL": {"cls":"act","soft":"raeth","els":[{"t":"cut","p":[[0.06,0],[0.7,0],[0.36,0.4],[0.36,1.02]]}]},
 "GIFT": {"cls":"act","soft":"vei","nick":true,"els":[{"t":"bar","u":0.3,"v0":-0.62,"v1":0.62},{"t":"lens","c":[0.64,0],"len":0.44,"w":0.5}]},
 "BOND": {"cls":"act","soft":"ael","nick":true,"els":[{"t":"cut","p":[[0.06,-0.62],[0.52,0]],"bend":0.13},{"t":"cut","p":[[0.18,0.5],[0.52,0]],"bend":-0.1},{"t":"cut","p":[[0.52,0],[0.95,0]]}]},
 "STOP": {"cls":"act","soft":"rheil","nick":true,"els":[{"t":"cut","p":[[0.06,0],[0.7,0]]},{"t":"ringarc","u":0.72,"v0":-0.7,"v1":0.7}]},
 "MEND": {"cls":"act","soft":"veinn","nick":true,"els":[{"t":"cut","p":[[0.04,0],[0.42,0]]},{"t":"square","c":[0.51,0],"s":0.3},{"t":"cut","p":[[0.6,0],[0.96,0]]}]},
 "ROT": {"cls":"act","soft":"ress","nick":true,"els":[{"t":"cut","p":[[0.05,0],[0.19,0]]},{"t":"cut","p":[[0.25,0.1],[0.37,0.1]]},{"t":"cut","p":[[0.43,-0.08],[0.55,-0.08]]},{"t":"cut","p":[[0.61,0.06],[0.73,0.06]]},{"t":"cut","p":[[0.79,-0.1],[0.92,-0.1]]}]},
 "AXE": {"cls":"act","soft":"rhith","q":"straight","els":[{"t":"cut","p":[[0.06,0],[0.94,0]],"straight":true},{"t":"tri","p":[[0.8,0.08],[0.56,0.82],[1.0,0.82]]}]},
 "CARVE": {"cls":"act","soft":"seth","nick":true,"els":[{"t":"cut","p":[[0.9,-0.56],[0.22,0]],"bend":0.12},{"t":"cut","p":[[0.9,0.56],[0.22,0]],"bend":-0.12}]},
 "LEAN": {"cls":"act","soft":"ilen","els":[{"t":"cut","p":[[0.08,-0.52],[0.92,0.52]]}]},
 "BEND": {"cls":"act","soft":"seil","els":[{"t":"cut","p":[[0.06,0],[0.94,0]],"bend":0.72}]},
 "BENEATH": {"cls":"act","soft":"senn","nick":true,"els":[{"t":"ringarc","u":0.92,"v0":-0.72,"v1":0.72},{"t":"cut","p":[[0.08,0],[0.66,0]]}]},
 "HULL": {"cls":"thing","soft":"seil","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.92,"w":0.36}]},
 "BEARER": {"cls":"thing","soft":"varen","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.92,"w":0.36},{"t":"cut","p":[[0.22,0],[0.78,0]]}]},
 "THIN": {"cls":"thing","soft":"isseil","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.94,"w":0.16}]},
 "SPENT": {"cls":"thing","soft":"ressveir","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.92,"w":0.36},{"t":"check","u0":0.9,"u1":0.14,"v":0,"w":0.2}]},
 "GREAT": {"cls":"thing","soft":"rhannseil","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.96,"w":0.66},{"t":"ringarc","u":0.5,"v0":-0.5,"v1":0.5}]},
 "EYE": {"cls":"thing","soft":"neas","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.46,"w":0.32},{"t":"cut","p":[[0.1,0],[0.27,0]]},{"t":"cut","p":[[0.73,0],[0.9,0]]}]},
 "HUNTER": {"cls":"thing","soft":"thavalea","nick":true,"els":[{"t":"lens","c":[0.42,0],"len":0.76,"w":0.34},{"t":"star","c":[0.88,0],"r":0.3}]},
 "SWIFT": {"cls":"thing","soft":"leas","nick":true,"els":[{"t":"lens","c":[0.64,0],"len":0.62,"w":0.32},{"t":"cut","p":[[0.08,-0.26],[0.3,-0.26]]},{"t":"cut","p":[[0.08,0.26],[0.3,0.26]]}]},
 "BREAKER": {"cls":"thing","soft":"rhenrhass","nick":true,"els":[{"t":"lens","c":[0.4,0],"len":0.66,"w":0.34},{"t":"square","c":[0.86,0],"s":0.34}]},
 "RAM": {"cls":"thing","soft":"rhasseil","nick":true,"els":[{"t":"lens","c":[0.38,0],"len":0.66,"w":0.34},{"t":"wedge","apex":[0.97,0],"base":0.72,"w":0.36}]},
 "ROOT": {"cls":"thing","soft":"ral","nick":true,"els":[{"t":"cut","p":[[0.1,0],[0.8,0]]},{"t":"rootfoot","c":[0.8,0],"dir":"out"}]},
 "SEED": {"cls":"thing","soft":"veis","nick":true,"els":[{"t":"lens","c":[0.74,0],"len":0.3,"w":0.3},{"t":"cut","p":[[0.59,0],[0.4,-0.3],[0.24,-0.52]]},{"t":"cut","p":[[0.59,0],[0.4,0.3],[0.24,0.52]]}]},
 "TREE": {"cls":"thing","soft":"thael","els":[{"t":"cut","p":[[0.04,0],[0.95,0]]},{"t":"cut","p":[[0.44,0],[0.74,0.52]],"bend":0.1},{"t":"cut","p":[[0.62,0],[0.9,-0.46]],"bend":-0.08}]},
 "PILLAR": {"cls":"thing","soft":"naelsaen","els":[{"t":"cut","p":[[0.04,0],[0.95,0]],"fill":true},{"t":"cut","p":[[0.44,0],[0.74,0.52]],"bend":0.1},{"t":"cut","p":[[0.62,0],[0.9,-0.46]],"bend":-0.08}]},
 "SAPLING": {"cls":"thing","soft":"leathael","els":[{"t":"cut","p":[[0.34,0],[0.9,0]]},{"t":"cut","p":[[0.58,0],[0.77,0.34]],"bend":0.06},{"t":"cut","p":[[0.7,0],[0.87,-0.3]],"bend":-0.05}]},
 "HEART": {"cls":"thing","soft":"saen","nick":true,"els":[{"t":"lens","c":[0.5,0],"len":0.36,"w":0.42,"fill":true}]},
 "US": {"cls":"thing","soft":"naelea","nick":true,"els":[{"t":"rootfoot","c":[0.12,0],"dir":"in"},{"t":"cut","p":[[0.12,0],[0.7,0]]},{"t":"lens","c":[0.83,0],"len":0.24,"w":0.42}]},
 "STONEFOLK": {"cls":"thing","soft":"aethea","q":"straight","nick":true,"els":[{"t":"rootfoot","c":[0.12,0],"dir":"in"},{"t":"cut","p":[[0.12,0],[0.7,0]],"straight":true},{"t":"square","c":[0.83,0],"s":0.34}]},
 "HOME": {"cls":"thing","soft":"naelenn","els":[{"t":"cut","p":[[0.06,0],[0.6,0]],"curl":{"r":0.4,"sweep":320,"dir":-1}}]},
 "HOMESTONE": {"cls":"thing","soft":"naelenn","q":"straight","els":[{"t":"cut","p":[[0.06,0],[0.62,0],[0.62,-0.62],[0.9,-0.62],[0.9,0],[0.62,0]],"straight":true}]},
 "SHORE": {"cls":"thing","soft":"aeth","els":[{"t":"bar","u":0.56,"v0":-0.85,"v1":0.6},{"t":"cut","p":[[0.56,0.6],[0.56,0.62]],"curl":{"r":0.26,"sweep":200,"dir":-1}}]},
 "ROAD": {"cls":"thing","soft":"ves","nick":true,"els":[{"t":"cut","p":[[0.06,-0.17],[0.94,-0.17]]},{"t":"cut","p":[[0.06,0.17],[0.94,0.17]]}]},
 "EDGE": {"cls":"thing","soft":"enth","nick":true,"els":[{"t":"ringarc","u":0.82,"v0":-0.9,"v1":0.9}]},
 "GUN": {"cls":"thing","soft":"rennrhen","q":"straight","nick":true,"els":[{"t":"square","c":[0.4,0],"s":0.78},{"t":"star","c":[0.84,0],"r":0.3}]},
 "CASTLE": {"cls":"thing","soft":"rhenennas","q":"straight","nick":true,"els":[{"t":"square","c":[0.3,0],"s":0.44},{"t":"cut","p":[[0.4,0],[0.47,0]],"straight":true},{"t":"square","c":[0.72,0],"s":0.62}]},
 "DOOR": {"cls":"thing","soft":"veth","q":"straight","nick":true,"els":[{"t":"cut","p":[[0.14,-0.56],[0.84,-0.36]],"straight":true},{"t":"cut","p":[[0.14,0.56],[0.84,0.36]],"straight":true},{"t":"bar","u":0.86,"v0":-0.54,"v1":0.54}]},
 "FLASH": {"cls":"thing","soft":"rheis","nick":true,"els":[{"t":"star","c":[0.52,0],"r":0.56}]},
 "BLOOD": {"cls":"thing","soft":"thar","nick":true,"els":[{"t":"drop","c":[0.56,0],"len":0.5,"w":0.46,"point":"in"}]},
 "GRIEF": {"cls":"thing","soft":"aelress","nick":true,"els":[{"t":"check","u0":0.86,"u1":0.2,"v":0,"w":0.26},{"t":"cut","p":[[0.97,-0.58],[0.92,-0.2],[0.86,0]]},{"t":"cut","p":[[0.97,0.58],[0.92,0.2],[0.86,0]]}]},
 "SAIL": {"cls":"thing","soft":"reaslel","els":[{"t":"cut","p":[[0.06,0],[0.8,0]],"straight":true},{"t":"cut","p":[[0.64,-0.58],[0.86,-0.32],[0.92,0.1],[0.8,0.52],[0.56,0.8]],"curve":true}]},
 "HAND": {"cls":"thing","soft":"vinn","nick":true,"els":[{"t":"cut","p":[[0.06,0],[0.52,0]]},{"t":"cup","c":[0.74,0],"r":0.44,"form":"palm"}]},
 "TIDE": {"cls":"thing","soft":"thae","nick":true,"els":[{"t":"ringarc","u":0.3,"v0":-0.8,"v1":0.8},{"t":"cut","p":[[0.3,0],[0.9,0]],"bend":0.08}]},
 "DEEP": {"cls":"thing","soft":"eir","nick":true,"els":[{"t":"ringarc","u":0.1,"v0":-0.62,"v1":0.62},{"t":"cut","p":[[0.1,0],[0.94,0]]}]},
 "AELTHAR": {"cls":"ligature","soft":"aelthar","nick":true,"els":[{"t":"drop","c":[0.16,-0.62],"len":0.24,"w":0.3,"point":"in"},{"t":"drop","c":[0.16,0.62],"len":0.24,"w":0.3,"point":"in"},{"t":"cut","p":[[0.28,-0.6],[0.6,0]],"bend":0.13},{"t":"cut","p":[[0.28,0.6],[0.6,0]],"bend":-0.13},{"t":"cut","p":[[0.6,0],[0.95,0]]}]}
}
```

**Coverage.** The inventory covers everything the task and the canon require:
- the ten roots and *Burn*;
- every word in the Admiral's carved vocabulary (§3.9 table);
- every concept the samples need: mist, breath, tree, pillar, child, sky, dying, stop, home, remember, grief, bond, blood, gift, guest, stone, the shore-men, fire, sea, wait, go and strike.

Several of these are conditions or devices rather than signs:
- *remember* is HOLD with a memory ray, or HOLD cupped round the pith itself (§3.7, the memory ray row);
- *sky*, *mist* and *breath* are the MIST band;
- *sea* is the WATER band;
- *guest* is US with GIFT and KNEEL;
- *the shore-men* are STONEFOLK×3.

### 3.6 · Condition bands

A **condition** is not cut across the ring. It lies **along** it, like real ring features (frost rings, ring shakes). It spans files s0…s1 clockwise, or the whole ring, and gives the surroundings of whatever is cut in that ring on those files.

| Band | Soft reading | Meaning | Drawn as (real anatomy) |
|---|---|---|---|
| **MIST** | *nael* | the grey; the breath; the sky it made | a pale band through the middle 56% of the ring, with softly waving edges (a pale, light-starved ring), at 42% opacity |
| **WHITE** | *lenn* | the white: open sky, snow, blizzard, hard light | a **frost ring**: short radial ticks every 4° through the ring's middle half |
| **DREAD** | *senth* | the dread; the fear grid; the burning place of their guns | a **ring shake**: a hairline split along the ring, opening at its middle |
| **WATER** | *thenn* | on the water; the sea | a single waving hairline along the ring's middle |
| **STILL** | *vaere* | still water; silence; the stillness (peace) | two straight concentric hairlines 3 apart |
| **DARK** | *veath* | night; the dark | the ring stained to heartwood tone over those files |

A **gap in a band** is itself meaning. A MIST band with its files 3–5 left open reads "the sky comes open there".

**Where a band ends** [rule]. A band over files s0…s1 is drawn to the slot edges, half a file beyond s0 and s1 (MIST fades to nothing there). Read the files whose centres it passes over; an end that falls near a slot edge is rounded inward.

### 3.7 · Grammar devices

Each device is a way of cutting, not a sign. Together they make up the grammar.

| Device | Written in GN | Drawn as | Means |
|---|---|---|---|
| **file** | `s:` | the radius a mark stands on | who or where. One file is one referent within a band; across bands, a ray carries identity. Even files are bearings |
| **ring** | `rk` | the ring a mark is cut in | when. The same ring is the same hour; outer comes after inner |
| **span** | `^rj` | a mark stretched across rings | through those steps; until step j |
| **empty ring** | `rk ·` | a thin unmarked ring | a morrow passes |
| **ligature** | `A+B` | two signs stacked on one file in one ring, the modifier inward (u 0–0.46) and the head outward (u 0.5–1) | a compound, modifier + head, exactly as in Seilrhass: AXE+PILLAR is "the pillar-felling" |
| **plural** | `×3` | three copies abreast, each at 0.52 breadth, 0.78 B apart | many; those of. The grain counts one, two and many |
| **pair** | `(A=B)` | two signs leaning ±16° from one shared foot, a V | the two, bound; *too*, inside one sign (the sliver) |
| **lean** | `A/` · `A\` | one sign tilted 16° about its own foot, clockwise (`/`) or counter-clockwise (`\`) | turned toward the one on that side. Two signs in one ring leaning toward each other **meet, face to face**: brow to brow (the Aelthar's r3). A lean from a *shared* foot is the pair |
| **twin** | `A … s+8: A` | the same sign on the opposite file in the same ring | *likewise, on the other side*. The other side of the wall |
| **negation** | `!A` | the sign's mirror image across its own file, entry-nick included | not |
| **hollow** | `~A` | the sign cut as an outline, with its floor left standing | shown, not meant: a seeming, a decoy, straw (the Two Mouths is hollow in one mouth) |
| **smoothed** | `_A` | two faint edges, no facets | hidden; felt, not seen (the Smoothed Cut) |
| **count** | `A#n` | 1–4 small bites on the clockwise side of a cut | n of them; on an act, n times |
| **ordinal** | `A@n` | 1–4 bites on the counter-clockwise side | the n-th |
| **five** | `A+HAND` | the hand after a thing | five of them |
| **causative** | `>A` | a small chevron at the mark's foot, pointing inward | make it do; send |
| **half size** | `A½` | the sign cut at half scale | the lesser. Canon uses it once: *Rhenear*, "cut small" (V.7 II) |
| **question** | `A?` | the mark's head runs into the ring line and stops unfinished | is it so? (the canon's "Look, then go") |
| **ray** | `ray s: ri–rj` | a hairline along a file, joining marks | the same one (co-reference, as in UNLWS) |
| **memory ray** | `mem s: rk` | a hairline from a mark inward to the pith, ending in three uneven root-hairs at the pith | remembered; carried back through the roots. From an outer ring, it means *always* |
| **held at the root** | `HOLD+…` at u 0 of a root | HOLD cut small and **cupped round the pith itself**, at the foot of the root | the memory ray's own heart, a ray of length nought: *remembered*, "root-held" (*ralthein*). The sliver's first word (§5.1) |
| **tie, same ring** | `tie a.rk → b.rk` | a hairline running along the ring from one file to the other | this one does it to that one |
| **tie, across rings** | `tie a.ri → b.rj` | a hairline curving outward from one file to another | when (or because) this, then that. From the Second Tide on, this is "one hull waits upon another" |
| **fork** | `A<X|Y>` | a cut splitting in two at its head. The clockwise branch leads to the next ring on the next file clockwise, the other counter-clockwise | if …, else … (the clockwise branch is the *if*) |
| **chain** | `<… root>` | a fork branch that ends in an older line's root sign, cut half size | then do that older carving |
| **band-rule** | `‖` | a doubled ring line | a movement ends |
| **included bark** | `¦` | a dark rough ring line | grown from an older carving, whose bark is here |
| **graft** | `graft(…)` | a V of included bark enclosing marks | borrowed from another line |
| **joined piths** | `pN·` | several piths, each with its own inner rings, inside shared rings | several formations under one order; the Joined Tide |
| **war-pith** | `pith: war` | a square pith | *Grow until the shore is silent* |
| **name place** | `bark 0:` | the bark on file 0 | a name: the Tide or Throne that grew it. A name is "the last thing in a knowing that will go into words" |
| **seal** | `bark 0: HOLD` | HOLD in the bark on file 0. Any name is cut inside its cup | this is held in the grain (tellings only) |
| **aim place** | `III 8:` | band III, file 8, the file facing the root | *Cut against*: the habit the order is aimed at |
| **pale ring** | `pale n` | 1–3 pale rings in the bark | a Throne's groans (T-rule 2) |

**How a tie's ends are read** [rule]. A tie is read by the marks it touches, not by the file its end happens to fall on (a mark is wider than its slot, so a hairline that stopped beside a mark could sit over the next file):
- each end stops **one knife-width (3 units) from the mark it joins**, and nearer to that mark than to any other;
- a tie **across rings** leaves its source's head and lands on its target's foot, each on the mark's own file;
- a tie **within a ring** runs along the ring's middle (or over a mark in its way, near the outer line) from the edge of one mark to the edge of the other;
- the thick end is the source and the fine end the target;
- a tie that ends on a file where nothing is cut in that ring ties to **that file's bearing**, a place (E4-01: the reach goes *to the east*).

### 3.8 · Composition rules

1. **One root per round.** It is cut first, in ring 1, from the pith, along the axis, and it owns files 15, 0 and 1 of ring 1. A telling may cut other marks in ring 1 on other files; an order never does.
2. **At most two signs on one file in one ring**, as a ligature. Everything else about one referent goes to the next ring on the same file, or to another file tied back.
3. **At most eight marked files per ring**, so marks never crowd within a slot. A mark keeps ≥ 3 units from its ring lines and from its neighbours.
4. **Modifier inward, head outward**, in a ligature and in a stack of rings alike. Reading heart to bark is reading left to right in Seilrhass.
5. **Conditions lie along the ring; acts and things cut across it.** A mark cut inside a condition band's files takes that condition ("wait *in the grey*").
6. **Line quality is fixed for closed shapes** (§3.4). An open stroke never classifies.
7. **Rays join only marks on one file. Ties join marks on different files.** A tie within a ring runs along the ring; a tie across rings runs outward, never inward. Only the memory ray runs inward.
8. **The root sets the axis. The seal and the name stay in the bark.** Nothing is ever cut beyond the bark's outer contour.
9. **Negation, hollow, smoothed, count and question** are properties of one mark, and they combine: `~!STRIKE` is "a seeming of not striking".
10. **The canonical order** (§3.12) is:
    - band I, then II, then III, then the bark;
    - within a band, ring by ring, outward;
    - within a ring, file by file clockwise from 0;
    - within a joined round's piths, pith by pith clockwise from the axis;
    - then the bands, rays, memory rays and ties, in that order.

### 3.9 · How a carving grows across the Tides

**The Law of the Rings, made literal** [canon FH §2, V.6 L1133]:

| Wood | Its age | Drawn rings | What it can hold | Where it appears |
|---|---|---|---|---|
| **green** (a sapling) | one season | 1, the heart ring only; no heartwood | **one sign** | the Hasty Tide; *Burn* (the Fall); the green sliver |
| **forty summers** | a generation | 2 marked rings, plus empty rings for time | **a phrase**: the root plus one sign, and one tie ("waits for its brother") | the Second Tide |
| **a shore-man's life** | a long human life | 3–6 | **a sentence, and a memory in it**: memory rays, the first fork | the Tide of Remembering |
| **a long life** | several human lives | 4–9; several piths | **the morrow**: ties between hulls, joined piths, hollow and smoothed marks, forks and chains | the Joined Tide, Deceit, the Last Tide; every Standard-Bearer's heart (*Saenvael*) |
| **the eldest** | ages; the pillars; Myststone | up to 24, plus a full bark | **a judgement**; names; groans | the Thrones; the gift; the Stone out of the Grey |

**The growth rules** [rule]. These realise canon L1369: "each Tide … cut the same root and added to it, as a tree adds a ring, so that the eldest carvings are the youngest ones grown old."
- **G1 · The same root.** Every carving of a line cuts that line's root sign in ring 1, on the axis. This is what Seren reads by eye.
- **G2 · Containment.**
  - A carving that grows from P reproduces **P's rings exactly** as its own innermost rings: the same files, marks, bands and ties.
  - P's bark becomes **included bark** on P's last ring, and the new Tide's rings grow outside it.
  - The inner rings are never re-cut, because the wood "cannot unlearn what is carved in it". Where a child changes what its parent said, it does so with a later mark on the same file. **The outer ring speaks last.**
- **G3 · Rules and old bark.**
  - Band-rule 1 of any grown carving lies on the ring where the root's sapling bark was, so it is drawn as both a double line and included bark.
  - A parent's band III (its turnings) becomes ordinary sap in the child. Its band-rule 2 is overgrown: a single line plus included bark.
  - The child cuts a new band-rule 2 before its own turnings.
- **G4 · Borrowing** (Ad §16c). A primitive borrowed from another line enters as a **graft** (a V of included bark) around the marks that carry it, on the ring where it is used. Real grafting is a thing the long-lived would do; "we guided the wood's growing".
- **G5 · Reach-back.** A carving that reaches back contains the far ancestor's rings, not the middle one's. E5-04 contains E1-06's ring directly.
- **G6 · Dress.** Early forms worn as a disguise are cut **hollow** in band II: E5-02 wears the Wave, the Mute Square, the Lone Stroke and the Bar Before hollow.
- **G7 · Chain.** A hinge branch that carves an older stratagem ends, at the fork's head, in that stratagem's root sign cut half size.
- **G8 · Joined piths.** From the Joined Tide on, each formation of an order has its own pith, with the line's root in its own heart ring. A parent carving, if any, is contained in the **first** pith, on the axis. Shared rings enclose all the piths.
  - Draw shared ring k as the level set smin_i(|x − p_i|) = R_k, with smin(d) = −h·ln Σ exp(−d_i/h) and h = 22.
  - Set pith separation to 1.32 × R_kj from the centroid, so that no inner rings overlap. **The piths' own rings must never intersect.** Overlapping circles would read as interlocking rings (craft §3d).
  - This is exactly how stems that grow together look: separate hearts, then one trunk.
- **G9 · Thrones.** A Throne's Judgement is an order in eldest wood. Its true name is at bark file 0, and during its battle its bark closes one **pale ring** per groan: the in-game hull shows 0–3; the Book draws none. In III.2 the Throne's heart is a **telling**, so the seal's cup holds the name.

**The Tides' growth forms** (what first appears in each):

| Tide | First appears | Its look |
|---|---|---|
| **Leathae** (Hasty) | the root alone | a small green sapling round, one sign from a square pith |
| **Vaelthae** (Second) | band-rule 1 over included bark; one sign in band II; the first **tie** | a round of two rings: a word "that waits for its brother" |
| **Ralenthae** (Remembering) | **memory rays** to the pith; **EYE** and look-signs; the first **fork**; the question device | the first hairlines running inward: "the memory that runs back through the roots" |
| **Aelthae** (Joined) | **joined piths**; ties across files within a ring; BOND between files | several hearts in one trunk: two made one, never explained |
| **Rhenthae** (Deceit) | **hollow** and **smoothed** marks; the **aim place** (band III, file 8) with STONEFOLK; *Rhenear* cut half size | marks that are outlines only, and marks that are felt and not seen |
| **Eirthae** (Last) | **forks** chained through band III; the **home clause** (HOME, or STERN on the fallback branch) | a bark band full of turnings |
| **Naelsaen** (Thrones) | a name in the bark; pale groan-rings | eldest dark heartwood and a heavy bark |

**The carved vocabulary, as signs** (for the Knowing generator; Ad §19 and every carving line):

| The carvings' English | Grain |
|---|---|
| mute stone (a wall) | SQUARE |
| speaking stone (a gun) | GUN |
| the reach (the watch of their stone) | SQUARE+EYE |
| stone-breakers | BREAKER |
| the eye | EYE |
| a sapling sent (a probe) | SAPLING |
| a root sent before | ROOT |
| the bearers | BEARER |
| the hunters | HUNTER |
| the swift | SWIFT |
| the dread | DREAD band |
| worthless wood; the brick | SPENT |
| the morrow | an empty ring |
| root to water; go | GO |
| wait on no bough | the root's single stroke |
| bough (a hull) | HULL |
| thin wood | THIN |
| the great hull | GREAT |
| the kept hand | HAND+CLOSE |
| the hand closes | CLOSE on the HAND file |
| bark splits; struck | WOUND |
| wood is ash | BURN on that file |
| flash, speaks (of a gun) | FLASH (with GUN: the speaking stone speaks) |
| keeps silence (a gun) | !FLASH |
| the grey | MIST band |
| the white | WHITE band |
| the sky falls; open the deck | SEED (×3) |
| straw | ~HULL×3 (hollow hulls) |
| blossom on the bare bough | ~BEARER (a hollow laden hull) |
| the prize | THIN+BEARER |
| hunger; let them hunger | HAND+OPEN |
| the first wood | a mark with an ordinal bite, HULL@1 |
| the ram | RAM |
| the host | HULL×3 |
| crowns, heads | GREAT×3 |
| the mountain | DEEP+SQUARE (*eirrhen*) |
| their hands (the masons) | STONEFOLK+HAND |
| what their hands love (a habit) | a clause on the **aim file** |
| the stone no hand can mend | SQUARE+!MEND |
| the house behind that stone | CASTLE |
| root by root, morrow by morrow | ROOT with empty rings between |
| stand among the stones as a stone | ~SQUARE on the Throne's own file |
| as seed waits out frost | SEED in a WHITE band |
| each by its own water | a plural whose copies take separate files |
| three roads, one hour | three marks in one ring |
| thrice; the fourth time | an act with #3; the next ring @4 |
| east, north, south, west | files (the generator fills the words) |
| cut against: they X | the aim place, band III, file 8: STONEFOLK×3 + the habit |
| *Rhenear* | STONEFOLK×3½ |
| if … if not … | a fork |
| go home | STERN (a real going home); HOME (the place loved) |
| Is it spent, or waiting? | SPENT? and KNOT? on the same file |

### 3.10 · Planks, halves and Seren's drawings

- **A carving is a volume, not a face.** Each mark in a round is the cross-section of a ribbon grown along the trunk's fibres. Any cross-cut shows the same round, and a plank shows its marks "It ran with the grain, fine and shallow" (V.1).
- **Seren draws every knowing as its round**, the end-face, because that shows all of it at once. The Book's drawings are hers.
- **The two halves of one heart** (V.2) [rule, and a gift from the canon].
  - The first plank and "the one plank that had given nothing" are the two halves of **E1-01's sapling round, split along its axis**.
  - The Wave curls **clockwise**, so the whole curl lies on one half. Rhyna's plank showed "one stroke curling forward" and gave a word: *shore*.
  - The other half held only a straight sliver of the stroke's other edge. It was "carved like the rest", and alone it gave nothing, because a Wave without its curl is no sign.
  - Held together from the two ends of the vault, the heart came whole. "The broken grain met, as the halves of a split log meet."
  - The drawing shows the round with a pale split line along its axis. V.1's facing leaf shows **only the clockwise half**: Seren's first drawing, "very small there".
- **A wreck floats only its root** (Ad §9b). The live glyph drawn over a sinking hull is the line's root sign alone, as it would be cut in the heart ring, with no round. It **replaces the Runic placeholder `᛫`** in Admiral §9b.

### 3.11 · Rendering by rule

- **SVG paths, no font, no filters.** Everything is generated, seeded as in §3.2.
- **Each cut is two flat facets.**
  - Build the centre-line, then offset it by ±h(t)·n, with the taper h(t) = H·min(1, t/0.16, (1−t)/0.16)^0.7.
  - Fill the wall whose normal faces the light, L = (−1, −1)/√2 (top-left), with `--cut-lit`, and the other with `--cut-shade`. Add a 0.6 floor line in `--cut-floor`.
  - **Hollow:** the two edges only, weight 1.0, in `--cut-shade`.
  - **Smoothed:** one lit edge (1.1) and one shade edge (0.8 at 55%).
  - **Filled** (the heart, the pillar's trunk): `--cut-floor`.
  - **Scar:** `--char`. **Check:** `--crack`.
- **Tokens.** The page defines these on `:root` and redefines them for dark mode (the Docs' pattern). Stone ink leans yellow and wood ink green (N7). The grain drawing uses only these tokens:

| Token | Light | Dark | | Token | Light | Dark |
|---|---|---|---|---|---|---|
| `--wood` | #e8dcc4 | #3a3226 | | `--cut-lit` | #f7f0e2 | #7d6c50 |
| `--early` | #efe6d2 | #433a2c | | `--cut-shade` | #6b5335 | #16110b |
| `--late` | #9c8660 | #8a7652 | | `--cut-floor` | #4a3822 | #0c0906 |
| `--heartwood` | #cdb68c | #2e271d | | `--char` | #2f2419 | #0a0806 |
| `--green` | #dfe6c6 | #34402c | | `--crack` | #3b2c1c | #0d0a07 |
| `--stone` (Myststone overlay) | #b9b3a8 | #3f3d3a | | `--ray` | #8a7350 | #a08a64 |
| `--bark` | #6f5a42 | #1f1912 | | `--mist` | #f6f2e8 | #5c5446 |
| `--bark-line` | #4c3d2c | #0f0c08 | | `--frost` | #8f8a80 | #9a917f |
| `--bark-in` | #5b4632 | #140f0a | | `--knot` | #5e4830 | #1a140e |
| `--pale` (groan ring) | #d9ceb8 | #5a5040 | | | | |

- **Size.**
  - The `viewBox` is the round's bounding box plus 14. Display it at `width: clamp(40%, R_outer/480 × 100%, 100%)`, so a Hasty sapling is small on the page and a Throne's heart fills it. That is the Law of the Rings, visible.
  - At 340 px, the smallest mark in a 9-ring round is about 10 px. The Book should offer a tap-to-enlarge for each round; this is a builder item.
- **Budget: ≤ 60 KB per round.** The prototype runs 18 KB for a sapling and up to 260 KB for 11 rings, because it keeps every facet segment and ring point. To meet the budget:
  - merge each stroke's facets into two paths;
  - draw rings as Bézier paths from 72 points;
  - draw year-lines from 48 points;
  - round every coordinate to one decimal;
  - put repeated signs in `<defs>` and place them with `<use>`.
- **Accessibility.**
  - Give every round `role="img"`, a `<title>` and a `<desc>`.
  - **Locked:** "A carving in the grain, not yet known". It must not leak the English, and it must not carry the round's id either, because ids name what they tell (`naelear`, `aelthar-rite`).
  - **Fragments:** the root's word only.
  - **Whole:** the telling's first line.
  - Any "rings growing" reveal honours `prefers-reduced-motion`.

### 3.12 · Grain Notation, the canonical reading, and the round trip

**Grain Notation (GN)** is the canonical linear form. It is written like the samples in §5:

```
round <id> {wood: green|forty|life|long|eldest|stone; pith: round|war[ ×n]; rings: K; rules after: [b1, b2]}
  I
    r1     0: WAVE*                  (* = the root)
  II
    r2   p0·4: EDGE+BREAKER          (pN· = on pith N's own rings)
    r3     3: !LIVE+SAPLING×3
  III
    r5    12: GO
  bark
    bark   0: BOND+TIDE              (a name)
    band MIST r4 slots 0–15
    ray  slot 3: r2–r4 · mem slot 8: r8 → pith · tie 0.r5 → 3.r5
```

The **literal reading** replaces each token with its gloss in canonical order (§3.8.10). The **telling** is Halyna's English, which is a translation, not a gloss. Both are given for every sample.

**Decoding by rule** (the round trip):
1. Find the pith or piths (square or round).
2. Trace the ring lines and classify each one: single, doubled (band-rule), dark and rough (included bark), or pale (groan, in the bark).
3. Find the root: the mark that touches the pith in ring 1. Its direction gives θ0.
4. For every mark, take:
   - its angular centroid, giving the file s = round((θ − θ0)/22.5°) mod 16. Angles and "outward" are measured about the mark's own pith, or, in the shared rings of a joined round, about the round's centre (§3.3);
   - its inner and outer radius, giving the ring span;
   - its element signature, giving the sign;
   - its mirror test, giving negation;
   - its bites, hollowness, smoothness and scale, giving the other devices.
5. Classify hairlines: radial between marks is a ray; radial to a pith end of three root-hairs is a memory ray; along a ring is a tie within the ring; curving outward is a tie across rings. Read each tie to the marks its ends touch (§3.7, "How a tie's ends are read"). A hairline along a ring that opens into a knocked-out split with a bright upper rim is the DREAD band, not a tie.
6. Emit GN in the canonical order.

**Validation**, run before any export (the prototype has the pieces):
- encode → draw → decode → compare, for every sample and all 46 carvings plus *Burn*;
- **no two signs share an element signature, and no sign's mirror equals another sign.** Check pairs by overlay: GO against SMOOTH (flag), BARB against STOP (cut passing the bar), BENEATH against STOP (gap), HULL against THIN against EYE (breadth and tails), US against STONEFOLK (crown), **KNEEL against AXE** (KNEEL stops at its fold, and the fold runs on along the ring as a shin; AXE's haft runs the whole space under a solid blade), **TREE against GROW** (two long bowed boughs at two heights; four short straight leaves), **SAIL against STOP** (a bellied, lopsided curve over the mast; a straight bar). Check them **at root size in a 56-unit heart ring** as well as at mark size: a root there is only about 16 units broad, and the old KNEEL closed up into AXE's blade (decode test, §10.11);
- jitter never crosses a quantisation threshold: ±3° against a ±11.25° slot, and pad ≥ 3 units;
- no ring crosses another, and no joined pith's own ring touches another pith's;
- no mark crosses the bark's outer contour;
- the page stays within the size budget.

### 3.13 · Keeping clear of Arrival and the others

| Arrival's logograms | Eilseth |
|---|---|
| one ring per sentence | many concentric growth rings; one ring is one step |
| ink, smoke, soft gradients, blots | crisp V-cut facets on wood, flat fills, no gradients or filters |
| meaning off the rim (tendrils, hooks) | marks cut **inside** the bark and across the rings; **nothing crosses the bark** |
| no start and no end | **directional**: the pith is the beginning, the bark the end, and the root sets the axis |
| stroke weight = tone and urgency | **weight carries nothing** (§3.4) |
| a hook makes a question | a question is an unfinished head at a ring line |
| twelve sectors | sixteen files, set by the root and not by the frame |
| made in one gesture, timeless | **grown over years**; a later carving contains its earlier form |
| black on pale fogged glass | wood tones, bark, growth rings |

- **Gallifreyan.** There are no circles inside circles, no dots on rings, and no anticlockwise reading from the bottom. The only closed curves are lenses, drops and knots, cut across the rings, never concentric "word circles".
- **Nomai.** There are no spirals and no branching vines. Ties are short hairlines along or across one or two rings.
- **Elden Ring.** Nothing interlocks, nothing glows, and no staff line runs through the rings. Joined piths are laid out so their rings **never overlap**.
- **Ogham and runes.** There are no tally strokes on a stem. Counts are at most four small bites, cut into the side of a curved or bowed mark inside a ring.
- **The originality pass (2026-09-27, `wf6/originality_report.md`).** Each sign was set beside the Elder and Younger Futhark, the Anglo-Saxon futhorc, Ogham, Cirth, Tengwar, Arrival's logograms, D'ni (Myst), Aurebesh, Dovahzul, Kryptonian, Klingon pIqaD, the Hylian scripts and the Sheikah script. Nine signs and one element read as copies of a rune or a certh, and were recut:
  - **TREE, PILLAR, SAPLING** were algiz ᛉ (also Younger Futhark *madr* and Cirth *ng*), a rune with a modern extremist use as well. Their boughs now spring alternately and bow.
  - **GROW** was two stacked algiz (the runic *tvimadur*). Its leaves now alternate.
  - **The root-foot** (ROOT, US, STONEFOLK) was an even three-tine fork: algiz at a root's head, its inversion (*yr*, *calc*) at a person's foot. It is now three unequal, flaring roots. The memory ray's pith-end followed it.
  - **KNEEL** was laguz ᛚ. Its fold now comes to rest along the ring.
  - **SAIL** was thurisaz ᚦ (and near wynn ᚹ). It is now a bellied cloth over a mast.
  - **BOND and AELTHAR** were the straight inverted Y of Cirth *h*. Their stems now bow and merge.
  - **DOOR** was Greek Π and Cirth *a*. Its posts are now battered.
  - **Principle, for any sign added later:** the Futhark and Cirth are made of straight staves and branches that meet at a point, so a grain sign that is a stave with straight branches, or two straight strokes meeting, must bow, stagger or break them. The grain is grown wood, and it is allowed curves the runes are not.
- **D'ni (Cyan's *Myst* and *Riven*).** Rivenkeep's *Myst-* and *Riven* already echo Cyan's games, so the grain was checked against D'ni hardest. D'ni letters are brush-written, thick-and-thin, and built on hooked Z- and 2-shaped strokes; its numerals are base 25, drawn inside squares and rotated for the fives. The grain shares none of it: no pen contrast, no boxed or rotated numerals, no count above the four bites and HAND. Keep it so: never give the grain a boxed numeral set, a 25, or a rotation that means a value. Seilrhass counts in fives by hand, which is common among real languages and is not D'ni's system; it is listed for Jack (§8) only because the two sit together. No D'ni word collides with the lexicon (the one form match, D'ni *gor* "time", is a Shoreland word, not a Seilrhass one).
- **Aurebesh, Dovahzul, Kryptonian, Klingon pIqaD, Hylian, Sheikah.** No sign resembles them. The nearest calls are Kryptonian's lozenges beside EYE (a lens with tails) and Dovahzul's wedge-headed claw strokes beside STRIKE and RAM; both are single features, not letters.
- **Heptapod terms.** None are used (not "logogram", not "semagram" as a proper term). *Semasiographic* (§3.1) is a linguist's word, but it is also the one Chiang's Louise Banks gives Heptapod B in "Story of Your Life", the story Arrival was made from. It stays in this design file and must never reach the Book's own text; the Book says "known", "a knowing" and "the grain".
- **Latin-letter likeness.** Some simple signs have Latin-letter or cross-like silhouettes, and most of them are drawn from the canon's own words, so they stay: STOP (a T), BARB (a Latin cross, and Cirth *l*), LONE (an i), STERN (an n), HOME (a 9), HOMESTONE (a square 9), GIFT (a ø) and LIVE (a P). On a round among the rings they read as cuts. The builder should still avoid showing one alone at large size out of its round, and Jack has BARB, STOP and HOME to decide (§8).
- **The look check.** The prototype's drawings were compared by eye with the craft's DO-NOT-COPY list. They read as carved wood cross-sections, and resemble neither ink logograms nor any ring-script above.

### 3.14 · Names in the bark

A name is "the last thing in a knowing that will go into words" (III.2), so it is cut **last**: in the bark, on file 0.
- A name is a ligature of the signs of its compound, modifier inward, exactly as the Seilrhass word is built.
- **The grain itself** (*vael*) is written as a free **grain-arc**: a short hairline along the ring, the same line the rings are drawn with. It is the only hairline that is not a ray or a tie. It occurs only in names.

**The ten Thrones:**

| Name | Built from | In the bark |
|---|---|---|
| **Thaesaen** | tide + heart | TIDE+HEART |
| **Leavaren** | young growth + bearer | SAPLING+BEARER |
| **Vaelress** | grain + rot | grain-arc+ROT |
| **Ralensaen** | roots + heart | ROOT×3+HEART |
| **Rhenvael** | stone + grain | SQUARE+grain-arc |
| **Esthaer** | that of fire | BURN (the old ending is not cut) |
| **Senneir** | beneath + deep | BENEATH+DEEP |
| **Eirlenth** | long + winter (the long wait) | DEEP+KNOT, inside a WHITE band |
| **Naelthar** | sky + blood | BLOOD, inside a MIST band |
| **Neivaere** | silver still-water: the mirror | ~HEART, inside a STILL band: a heart that shows and does not mean |

**The rest:**

| Name | In the bark |
|---|---|
| **Leathae** (Hasty Tide) | SAPLING+TIDE |
| **Vaelthae** (Second Tide) | grain-arc+TIDE |
| **Ralenthae** (Remembering) | ROOT×3+TIDE |
| **Aelthae** (Joined) | BOND+TIDE |
| **Rhenthae** (Deceit) | SQUARE+TIDE |
| **Eirthae** (Last Tide) | DEEP+TIDE |
| **Naelsaen** (the Thrones; the pillars) | HEART, inside a MIST band |
| **Sethvaren** (the Standard-Bearer) | CARVE+BEARER |
| **Saenvael** (the Heartwood) | HEART+grain-arc |
| **Aelvaren** | BOND+BEARER |
| **Aelrhen** | BOND+SQUARE |

**When a round shows a name.** A Throne's name shows glossed only once that Throne has fallen (K7). Before then the name-sign is drawn and unglossed: the name is *untold*, not absent (Ad T-rule 9: "the name stays untold until that haven is retaken").

---

## 4 · HOW THE WOOD IS KNOWN, AND THE LADDER IN THE GRAIN

### 4.1 · Why a knowing cannot be turned

- **There are no words in it to turn.**
  - A spoken sentence can be reordered, misheard or punned on. Its small words can be lost across water, as the Guest lost Shoreland's.
  - A round has no word order and no homophones. It has no small words, and nothing waits on a listener's grammar.
  - Every relation is laid out geometrically:
    - who is the file;
    - when is the ring;
    - "the same one" is a ray;
    - "because" is a tie;
    - "not" is a mirror.
  - One drawing has exactly one reading (§3.12). So "no word could be twisted and no promise misheard" (II.2) is literally true of the grain.
- **Why only the Bonded.** A round is taken in whole, as the carver meant it, in one touch. It is "a forest's thought" (V.1), too large for one shore-mind: Seren "felt something come into her too great to hold, and let go". The Aetherbond's shared mind can hold it, because "what the one knows, the other knows". The grain therefore needs no special mechanism: it is the same act as the knowing of a wall.
- **Where turning comes back in: the telling.** Halyna "set each word down like a marking-stone where the knowing lies". In grain terms, each English word they choose **is a gloss laid on one mark**. That is exactly what the Book shows: the round, with Seren's words set beside the marks they belong to. Fidelity rises because more classes of mark can be glossed (§4.2), not because the wood changes.
- **Deceit without lies.** A Rhenthae carving cuts its decoys **hollow**. Read whole, the round says plainly: *show this; do not mean it*. It is the enemy's eye on the water that is fooled, never the knower of the wood. So Seren's "The wood does not lie. It was told to make us believe a lie, and it obeyed." holds in the grain. The lie is a hollow cut, and the hollowness is itself carved.

### 4.2 · The ladder: what can be told at each band

The ladder follows the Knowing bands of Legends §4 and Admiral §9b exactly. Each band unlocks a **class of marks** for glossing. The Book draws every round in full from the moment it exists, and glosses only what is held.

| Band (campaigns) | What Halyna hold (canon) | What becomes glossable in the grain | What the Book shows |
|---|---|---|---|
| **K1 · one shape** (Hasty, 1–6) | "tell one word of it" | the **root sign**, by one word: *shore, wall, go, before, flash, grey, home* | the round, with the root labelled *…shore…* (Seren's word). Admiral E1: "Untold glyph. One carved sign, drawn" |
| **K2 · two shapes, named** (Second, 7–14) | two signs; a carving named | **things and acts** in band II; the **condition bands** | *Screen … bearer.*: the gap is the unglossed **tie** |
| **Cam 13 · the Night of the Naming** | "every plank gave its whole order" | the **whole young-wood knowing** of each root sign | the seven Hasty rounds glossed whole; the Hasty entries ripen |
| **K3 · sentences, and the memory** (Remembering, 15–22) | "sentences, and the memory in them" | **ties across rings** (Cam 15: the Second-Tide gaps fill); **memory rays**; EYE and the look-signs; the **question**; doubt flags, shown as `[…?]` | *Where the stone fell [silent?], look before you trust.* |
| **K4 · ties** (Joined, 23–26) | "who waited for whom" | **joined piths**; **ties within a ring**; BOND across files; the **pair** | *The west waited for the east to be struck.* |
| **K5 · aim** (Deceit, 27–31) | "what a carving wants" | **hollow**, **smoothed**, the **aim place**, **half size** (*Rhenear*), the **twin** | *Cut against: they hold the north silent.* |
| **K6 · a whole morrow** (Last, 32) | "a whole plan" | **forks**, **chains**, the home clause | *When the bearer falls … go home.* |
| **K7 · true names** (each Throne fallen) | "true names" | the **name place** in the bark | the III.2 entry and the Knowings column |
| **K7★ · all ten** | the sliver | the **sliver's ligature**; the **Naelear** sign | VI.1; II.2's `[ ]` fills with *Naelear* in Seren's hand |
| **After the Epilogue** | no one ("no knowing of Halyna's filled it") | the Stone's telling | §5.7 |

**Seren's brackets, exactly.**
- A mark whose class is not yet held is drawn but not glossed, and its place in the telling prints as `[ ]`. That is "the shape of a knowing before it could be told".
- A mark whose sign is held but which the generator flags as uncertain prints as `[word?]`. These are the Remembering Tide's *[cooled?] [new-laid?] [marked?] [until?] [learn?] [shadow?] [low?] [waiting?]*.
- *[mute thing]* in IV.2 is the Mute Square told only by paraphrase: its shape is known, but not yet as "stone".

### 4.3 · The three states of a wood surface

| State | Canon wording | In the grain |
|---|---|---|
| **Blank** | "Mystwood grain, and the line *Untold…*" | **The leaf's own round, fully and truthfully cut, with no glosses.** Seren's line is in her course-hand (Shoreland spec). The one exception is the leaf facing I.1, which shows rings with no marks (§5.7) |
| **Fragments** | "italic, with the gaps marked [ ] and no small words" | the round with the held marks glossed; the fragment text below it |
| **Whole** | "the full telling … in three movements" | the round kept **above** the telling, with every mark glossed. The fragments stay above that, because the Book only adds |

### 4.4 · The blank wood leaves: what each round is

Every blank facing leaf (inventory D1) shows the round of the wood it will be told from. Its ring count is the leaf's paragraph count, by movement, counted from `legends_v11_final.md`.

| Leaf | The wood | Pith | Rings (I / II / III) |
|---|---|---|---|
| **II.2** Of the Breath of the Wood | the gift, at its deepest holding (Myststone) | round | 4 / 7 / 3 = **14**. Ring 2 carries the Naelear sign, the untold word |
| **III.2** The Thrones That Walk the Sea | each Throne's heart (eldest) | war | **ten small rounds**, one per entry, each with its name held in the seal's cup; the headnote and closing lines are Seren's |
| **IV.2** The Axe in the Grain | a Blackthorn heart grown from a felled pillar's stump | war | 2 / 7 / 4 = **13**. The IV.2 fragments are this round partly glossed |
| **IV.4** The Gift Held an Hour | the gift itself (Myststone) | round | 2 / 11 / 3 = **16**. Its ring 15 cites the sentence, whose own round (§5.4) is drawn inline there |
| **IV.6** The Voyage of the Aelvaren | a Remembering heart | war | 2 / 8 / 1 = **11** |
| **V.3** The Wreck That Went Home | a Remembering hull | war | 2 / 6 / 3 = **11** |
| **V.4** The Council Under the Thin Sky | a Silverbark heart (Joined Tide) | war | 1 / 11 / 3 = **15**. Seren's facing leaf stays empty for ever (D1.9) |
| **V.6** Of the Growing | a Joined Tide heart | war | 4 / 15 / 5 = **24**, the largest round in the Book. The Song of the Years is its ring 23 |

**The gift holds three knowings at three depths** [rule]: the sentence nearest the surface (§5.4), its own story (IV.4), and the home at its "deepest holding" (II.2). Seren draws each as its own round. Eldest wood "gives slowly".

**Composing a wood-leaf round** [rule, for the Legends builder]. For each paragraph, cut into its ring the paragraph's **core knowings** as signs, in the rules of §3.8. Those are its subject, its act, and its condition or bearing. A paragraph needs 1–6 marks. The round is a truthful skeleton of the telling, not a word-for-word copy. The telling is Halyna's; the grain is what they told from. The samples in §5 show the density.

### 4.5 · Achievements that translate (proposal)

Jack asked that the native text be unreadable: "The human can't read it because they have not achieved the ability to yet. Only by unlocking the achievements in the game." The laws allow this only on milestones every player reaches (Legends §1 laws 4–5; inventory §F23). So the **translations ride the Knowing bands**, which are already deterministic and have campaign fallbacks. Each band becomes a named milestone achievement that adds a class of glosses to Seren's sign-list in the codex:

| Achievement (proposed name) | Fires at | Translates |
|---|---|---|
| *The First Glyph* | Cam 1 complete (V.1) | root signs, by one word |
| *The Night of the Naming* | Cam 13 | the young wood whole; things, acts and conditions |
| *A Memory in the Grain* | Cam 16 | ties across rings, memory rays, looks and questions |
| *Two Made One* | Cam 25 (fallback 25) | joined piths, ties within a ring, the pair |
| *What It Wants* | Cam 29 (fallback 29) | hollow, smoothed, the aim, the twin |
| *A Whole Morrow* | Cam 32 | forks and chains |
| *True Names* | each Throne fallen | that Throne's name in the bark |
| *Those of the Breath* | all ten fallen | the sliver's sign and *Naelear* |
| *The Last Carver* | the launch after the Epilogue is laid | the Stone's telling, added under the facing leaf |

- **Skill achievements** (Pacifist and the rest) may add **one gloss line** at most, never a whole leaf. Example: Pacifist could add Seren's soft readings to the sign-list.
- **Names and the codex screen** belong to the GDD owner [call].

### 4.6 · The Book | Modern tab

- **The grain is language-free, so it is identical under both tabs.** Only the glosses change language:
  - the Book tab uses the Book's words (*shore*, *thin wood*, *the dread*);
  - the Modern tab uses plain words (*the coast*, *cheap ships*, *the enemy's range*).
- **A locked leaf shows its native hand under either tab**, because there is nothing yet to translate.
- **The literal reading** (§3.12) may be offered as a third view for decoders: an "Original" facing text [call].

---

## 5 · THE SAMPLES

Each sample gives five things:
- where it lives in the Book;
- its round in Grain Notation (GN);
- a sign-by-sign table;
- the literal reading;
- the English.

Every round here is drawn by the prototype from the same data (`wf6/grain/samples.py`; SVGs in `wf6/svg/`). Files are numbered clockwise from the root's axis.

### 5.1 · *We remember our home too.* (VI.1, the green sliver)

**The wood.**
- It is a living green sliver, grown "in the dark of the dead Throne's heart, out of sight, as a seedling grows in the crack of a wall".
- **Its pith is round.** It is the only living wood in the Book grown after the war with no war in its heart: the council's carving did not reach it.
- It is a sapling round of one ring, so it holds **one sign**: "the green wood holds one word … and the word was *home*". But that one sign is a **ligature**, and the rest of the knowing is folded into it.

```
round VI-1 {wood: green; pith: round; rings: 1; rules after: []}
  I
    r1   0: HOLD+(HOME/ = HOMESTONE\)+[NAELEAR within HOME]*
```

**The one sign, part by part** (`wf6/svg/VI-1.svg`):

| Part | Where | Sign / device | Means |
|---|---|---|---|
| foot | u 0–0.16, cupped round the pith | **HOLD** at the root, the heart form of *ralthein* ("root-hold") | remembered |
| two stems from one foot | leaning ±16° | the **pair** device | the two, bound: *too, likewise* |
| the clockwise stem's head, on the axis | u 0.12–1.0 | **HOME**, the round loop | our home (curved: of wood). The sign's head, and Seren's one word, *home* |
| the counter-clockwise stem's head | u 0.12–0.86 | **HOMESTONE**, the square loop | your home (straight: of stone): "the answer of this hearth" |
| folded inside the round loop | u 0.66–0.86, one-tenth scale | **NAELEAR** (US×3) | "folded in it, as a seed is folded in a fruit, was a name" |

**Literal reading.** *Held at the root: two homes grown from one foot, bound. Ours, of wood; yours, of stone. In ours, folded: those of the breath.*

**The telling** (canon): *We remember our home too.*

**Spoken Seilrhass:**

> ***Ve ith naelenn ael raltheine.***
> *Ve ith Nael'enn ael Ral'theine.*
> ve · ith · naelenn · ael · ralthein-e
> we · own · home · too · remember-PRESENT

The hearth's answer in Seilrhass is ***Ve raltheine***, "We remember". The sliver's sentence **begins and ends as the hearth's does**, *Ve … raltheine*, with *ith naelenn ael*, "our own home, too", folded inside it. The canon says it "did not stop where we stop". In English that is a continuation; in the wood's own tongue it is a folding, as the name is folded in the sign.

**Ladder.** The round is shown from VI.1. The head can be read as *home* by anyone who knows the Turned Stern made whole. The whole comes with *Those of the Breath* (K7★). **It must never appear in store art or screenshots** (Legends §5).

### 5.2 · *Naelear*, the name they give themselves

```
round NAELEAR (a chip) {wood: plain; pith: round; rings: 3}
  I
    r2   0: US×3        band MIST r2 files 15–1
```

| Sign / device | Means |
|---|---|
| **US** | one who stands rooted, crowned with a lens: of wood, one of us |
| **×3** | many; those of |
| **MIST** band over the same files | in the breath of the trees; the grey; the sky it made |

- **Literal reading:** *those of us, in the breath*. **English:** *Naelear, those of the breath.* **Spoken:** *Nael'ear*. **Soft:** *Naelear*.
- **Its opposite, cut small in V.7 II:** *Rhenear* = STONEFOLK×3½, straight crowns at half size, with no band: those of stone, who do not hear.
- **Where it appears:**
  - folded inside the sliver's HOME (§5.1);
  - in ring 2 of the II.2 round;
  - **inline in II.2 ¶2** as the untold word, *We who call ourselves [ ]*. There the `[ ]` is this sign, drawn on a two-ring chip of end-grain at text height. It stays unglossed until K7★, when *Naelear* is added beside it in Seren's hand (the canon's RIPENS). The sign itself is never removed.

### 5.3 · The Aelthar

**(a) The name, carved "whole and soft".** The **AELTHAR** ligature is two drops at the foot, two bloods, whose stems grow together into one: *two bloods made one*.
- **Soft reading:** *Aelthar*. **Spoken:** *Ael'thar*, "with the break in it, as a branch breaks" (II.2).
- On the wall, in the Edge speech, the Rivenmen hear "Ail-tar".

**(b) The rite words, as the rite is spoken.** The Guest spoke only the first line, "the name of the rite in the thunder of his own tongue", and then his three words in Shoreland. The whole rite, as the long-lived say it to one another, runs:

| Step (IV.4) | Seilrhass | Spoken | Word by word | English |
|---|---|---|---|---|
| kneel; name the rite | ***Ael'thar.*** | *Ael'thar* | bond-blood | "Aelthar." |
| at the door | ***Sa veth li va raethe.*** | *Sa veth li va Rae'the* | your · door · at · I · kneel-PRESENT | "At your door I kneel." |
| set down the gift | ***Ra vei sa na.*** | *Ra vei sa na* | this (held) · gift · you · to | "This gift, to you." |
| neck in the right hand; brow to brow | *(silence)* | — | — | the foreheads touch "in silence". Nothing is said; the step is only carved |
| the two cuts | ***Sa thar, va thar.*** | *Sa thar, va thar* | your · blood · my · blood | "Your blood; my blood." |
| the arms pressed together | ***Ith li thaess, vann li thaess.*** | *Ith li thaess, vann li thaess* | one · at · wound · two · at · wound | "Harm to one is harm to both." |

The last line is the Stonewright masters' own saying (II.3) in the other tongue: **one proverb, two peoples** (inventory §C1 #25).

**(c) The rite, as carved.** Rite-wood is a twisted bough, "the twisted boughs we bent in our rites". The rite is older than the war, so its pith is round. The carving is a telling: two rings per movement, and the seal.

```
round AELTHAR {wood: long (rite-wood); pith: round; rings: 6; rules after: [2, 4]}
  I
    r1    0: KNEEL*
    r2    0: DOOR      1: GIFT
  II
    r3   15: US/       1: US\          (leaning together, crown to crown)
    r4   15: WOUND     1: WOUND
  III
    r5    0: AELTHAR
    r6   15: WOUND     0: BOND      1: WOUND
  bark
    bark  0: HOLD                     (the seal)
```

| Ring | Marks | Means |
|---|---|---|
| r1 | KNEEL, the root | one kneels: "the first step … the only step one people can take alone" |
| r2 | DOOR · GIFT | at the door; the gift laid down before |
| r3 | two US, leaning in until their crowns meet | two, brow to brow, at one hour. The host's crown is a lens here, because this is the rite among the long-lived. **Cut for a shore-man, the host's crown is square**: "across any divide" |
| r4 | WOUND · WOUND | a cut on each: "he would ask no blood he did not give" |
| r5 | AELTHAR | two bloods made one |
| r6 | WOUND · BOND · WOUND, in one ring | a wound at one and a wound at the other, bound, at the same hour: harm to one is harm to both |
| bark | HOLD | this is held in the grain |

### 5.4 · The gift's sentence (IV.4)

**The wood.** The gift is eldest wood that "time has forgotten", petrified: Myststone. Its pith is round because it is older than the war. It holds this sentence nearest the surface (§4.4). The round is eleven rings: three for the plea, four for the reason, and four for who they are and the plea again.

**Files:**
- **0** is the hearer: you, the shore-men.
- **3** is the pillars and their breath. It is placeless, an odd file, because the pillars have no road.
- **8** is us, behind the grey.
- **13** is our children, also placeless.

```
round GIFT {wood: eldest (Myststone); pith: round; rings: 11; rules after: [3, 7]}
  I
    r1    0: STOP*
    r2    2: EDGE          3: AXE+PILLAR×3       band MIST r2 files 2–3
    r3    3: LIVE
  II
    r4    8: US×3                                band MIST r4 all files
    r5    0: STONEFOLK×3   3: AXE
    r6    3: OPEN                                band MIST r6 files 5–1 (open at 2–4)
    r7    3: FLASH        13: !LIVE+SAPLING×3
  III
    r8    8: US×3                                band MIST r8 files 7–9
    r9    0: STONEFOLK×3   8: !STRIKE
    r10   3: DYING         8: BENEATH+DYING
    r11   0: STOP
  ray  file 3: r2–r4   ·   ray file 8: r4–r10   ·   mem file 8: r8 → pith
  tie  0.r5 → 3.r5 (does it to)   ·   tie 3.r7 → 13.r7 (does it to)
  tie  8.r9 → 0.r9 (does it to)   ·   tie 3.r10 → 0.r11 (because → then)
```

| Ring | Literal reading | The sentence's words |
|---|---|---|
| r1 | **Stop.** (the root) | *Stop* |
| r2 | the felling of the pillars, at the edge, in the grey | *the felling of the pillars at the edge of the grey,* |
| r3 | they live (the ray says: the same pillars) | *for they are not timber.* |
| r4 | the grey over all; the same pillars' breath; us, within it | *The sky over us is their breath, and ours,* |
| r5 | you, doing it to them: the felling | *and when you cut them* |
| r6 | there, it opens; the grey has a gap | *it comes open,* |
| r7 | hard light, doing it to our children: they do not live | *and our children cannot live in the open sun.* |
| r8 | us, behind the grey; remembered to the heart (always) | *We are here, behind the grey, and we have been here always,* |
| r9 | we do not strike you | *and we are not your enemies.* |
| r10 | the pillars' breath dying; we (the same), beneath, dying | *…for the sky is dying, and we are dying under it.* |
| r11 | **Stop**, because of that (the tie from r10) | *Stop,* |

**The English** (canon, as Halyna told it "in words of ours he never had"):

> *Stop the felling of the pillars at the edge of the grey, for they are not timber. The sky over us is their breath, and ours, and when you cut them it comes open, and our children cannot live in the open sun. We are here, behind the grey, and we have been here always, and we are not your enemies. Stop, for the sky is dying, and we are dying under it.*

**In Seilrhass**, as the Guest would have said it with a common tongue:

> ***Nael enth li naelsaenen rhithas rheil; le rhithveir ni eisse rhi.***
> mist · edge · at · pillars · felling · stop · — · they · timber · not · are · because
>
> ***Ve laes nael le nael ei ve nael eisse; se le rhithe anth, la aenne; ei ve ennan rheis li ni ilaene.***
> us · above · sky · their · breath · and · our · breath · is · — · you · them · fell · when · it · opens · — · and · our · children · hard-light · in · not · live
>
> ***Ve nael sath li ra li eisse, ei eilen eisse; ei ve se rhesear ni eisse.***
> we · mist · behind · at · here · are · and · always · are · — · and · we · your · enemies · not · are
>
> ***Rheil, nael vease rhi, ei ve la senn vease.***
> stop · sky · dies · because · and · we · it · beneath · die

- **Knocks:** *Nael'saenen, Rhi'thas, Rhith'veir, Eis'se, Rhi'the, Aen'ne, En'nan, I'laene, Ei'len, Rhe'sear, Vea'se*.
- **Sky and breath are one word.** In Seilrhass "the sky over us is their breath" is almost *the breath is the breath*: *nael … nael*. They see no metaphor in it. The shore does, and "the shore has no words for a home that is air" (II.2).

### 5.5 · The Hasty seven, and *Burn*

**The wood.**
- Each is a **green sapling round**, one season old. It has one ring, no heartwood, and a **war-pith**, the square.
- The one sign is cut from the pith along the axis, and it is the only mark. A sapling holds one sign.
- **A Hasty sign carries the whole young-wood order in its own anatomy.** That is why Halyna could tell one word at first and the whole order at the Night of the Naming: they learned to hold the rest of the same one sign.

| Carving | Root (Seren) · soft reading | The one word (K1) | How the one sign holds the whole order, stroke by stroke | Known whole at Cam 13 (V.2) |
|---|---|---|---|---|
| **E1-01** *To the shore.* | the Wave · *aeth* | *shore* | the curl breaking forward is *to shore*; the stroke running straight from the pith, as a root runs to water, is *go*; one unbroken stroke, with nothing else cut, is *wait on no bough* | *To shore. As root to water, go. Wait on no bough.* |
| **E1-02** *Break the wall.* | the Mute Square · *rhen* | *wall* | the closed square is stone, the wall, cut as the whole order: the stone *is* the order. One enclosure is *first stone, only stone*. Closed, with nothing after it, is *strike till it opens or wood is ash*: the young wood had no sign for afterwards | *Break wall. First stone, only stone. Strike till it opens or wood is ash.* |
| **E1-03** *Go until struck.* | the Lone Stroke · *ith* | *go* | the short cut running ahead of the long one is one going, alone; the gap between them is where it is struck; the short cut stands to the side of the long one's line, so *turn aside* | *Go until struck. Where bark splits, turn aside.* |
| **E1-04** *Before the bearer.* | the Bar Before · *reil* | *before* | the stroke is the bearer's going; the bar laid across it, ahead, is thin wood across the way; the stroke runs on unbroken through the bar, so *bearer keeps pace* | *Before bearer, thin wood. Thin wood falls; bearer keeps pace.* |
| **E1-05** *Where it flashed.* | the Spark · *rheis* | *flash* | the cut goes to the star-notch and ends there: *where it flashed, strike*. One star, at the head, is *last flash, only flash* | *Where it flashed, strike. Last flash, only flash.* |
| **E1-06** *Wait in the grey.* | the Knot · *lanth* | *grey* | the stroke stops in a knot, a place where the grain waited, *as seed waits out frost*. The rings flow on past the knot while it holds, so *when stone is still, come* | *Wait in grey, as seed waits out frost. When stone is still, come.* |
| **E1-07** *Home when wounded.* | the Turned Stern · *sathneth* | *home* | the stroke goes out and hooks back on itself: *home when wounded*. The return runs beside the outgoing stroke, not on it: *each by its own water* | *Home when wounded. One bough falls; all turn, each by its own water.* |
| ***Burn*** (the Fall; not one of the 46) | *Burn* · *esth* | — | a fire scar at the heart of green wood: the only charred cut in the grain. The callus lips are the wood living on around the burn | *Burn.* |

- **In GN** every one of them is `round E1-0n {wood: green; pith: war; rings: 1}` with `I r1 0: <ROOT>*`. For example, `r1 0: WAVE*` and `r1 0: BURN*`.
- **Two physical marks, neither grammatical:**
  - **E1-01's round is split along its axis** (a pale line): the two planks of V.2 (§3.10).
  - ***Burn*'s plank is charred at one end.** The char is a stain across one side of the bark, which the decoder ignores. The grammatical scar is the one at the heart.
- **Drawings:** `wf6/svg/E1-01.svg` … `E1-07.svg`, `BURN.svg`, and all eight on one sheet in `hasty.svg`.

### 5.6 · A late-Tide carving: *Three roads, one hour* (E4-01), grown from its ancestors

This is the carving of V.7 Part I. It was known from the Standard-Bearer's heart, and it holds its Tide's name. Its growth line is E1-01 → E2-01 → E4-01, plus a graft borrowed from E3-01 (Admiral §16b: "the sounder replaced by memory").

**Its parent, E2-01 *Run the Batteries*** (forty-summer wood, war-pith: a phrase):

```
round E2-01 {wood: forty; pith: war; rings: 2; rules after: [1]}
  I
    r1    0: WAVE*                      (E1-01, whole)
  ‖¦                                    (band-rule 1 on the sapling's overgrown bark)
  II
    r2    4: EDGE+BREAKER               band DREAD r2 files 15–1
  tie  0.r1 → 4.r2  (when → then)
```

- **Literal reading:** *To the shore, all at once, straight: through the burning. Stone-breakers at the edge; they answer to the landing.*
- **Telling** (Admiral): *Through burning, not against. Stone-breakers hold at edge … till bearer touches shore.*
- **The "…" is the unglossed tie.** Ties are not held until Cam 15, when the gap fills.
- **The Law holds:** two signs, one tie.

**E4-01 itself.** It is a long-life heart with **three war-piths inside shared rings**, one per road.
- Pith 0, on the axis, is **the east road**, the main road. **It contains E2-01 whole** (G2, G8).
- Pith 1, clockwise, is **the north**: the right hand, facing the shore from the east.
- Pith 2, counter-clockwise, is **the south**.

```
round E4-01 {wood: long (a Standard-Bearer's heart); pith: war ×3; rings: 5 (2 own + 3 shared); rules after: [2, 4]}
  I
    r1   p0· 0: WAVE*    p1· 0: WAVE*    p2· 0: WAVE*
    r2   p0· 4: EDGE+BREAKER   (with its DREAD band and its tie: E2-01 whole)
  ‖                                     (the piths join: the first shared ring)
  II
    r3     0: GO     2: BOND     4: GO     12: KNOT^r4       band DREAD r3 files 11–13
    r4    10: SQUARE+EYE   graft(E3-01)   mem 10: r4 → pith
  III
    r5    12: GO
  bark
    bark   0: BOND+TIDE                                        (the Tide's name)
  tie 10.r4 → 0.r4 (does it to)   ·   tie 10.r4 → 12.r5 (when → then)
```

| Ring | Literal reading | The telling (V.7 I) |
|---|---|---|
| r1 | three roots of the Wave, on three piths: three roads, each all at once and straight | *Three roads,* |
| r2 | (in the east pith: the older carving, its stone-breakers holding the edge of the burning) | — (the older rings are known, not re-told) |
| r3 | **one ring: one hour.** The east goes and the north goes, bound as one. The south waits, knotted, in the dread's edge, until r4 | *one hour. Let the east and the north go as one. Let the south stand at the edge of the dread* |
| r4 | the south's watching stone (the reach) goes to the east [grafted: remembered, the reach walks when pressed] | *until the reach of the south has walked east;* |
| r5 | when that has happened, the south goes | *then let the south go.* |
| bark | bond-tide | *Aelthae*: "the name the wood gives to that whole Tide" |

- **Why it chilled them.** In the grain, *"let the east and the north go as one"* is **the BOND sign between two files**, the same sign as the Aelthar's joining. "It is how we work a wall."
- **Book of Knowings.** The Wave's growth page draws E1-01 → E2-01 → E4-01 → E5-01 → Thaesaen's Judgement. Each round visibly contains the last.
- **Drawings:** `wf6/svg/E2-01.svg` and `E4-01.svg`. The prototype omits the pith-local band and tie in r2; the GN above is authoritative.

### 5.7 · The untold leaf facing I.1: the Stone out of the Grey

**What the wood holds there.** The Epilogue says:
- the leaf "stood empty until now, with the grain drawn on it and one line";
- "in the end no knowing of Halyna's filled it";
- the Stone "was cut in our own letters, so that anyone might read it, and I did not lay my palms on it".

So **the grain in the Stone was never known by anyone at the hearth.** The Stone is Myststone, "the one stone his people had that would carry a meaning". The Last Carver cut letters for eyes and grain for hands, and only the letters were read.

**Content** [rule; its exact words are Jack's call, §8.2]. The Stone's grain is **the wood's half of *The Torn Cloak***: what every hull saw on the last whole stone, and what went home through the roots to the groves, where "he knew it … as the wood knows a wall". It holds **all five things of the Title**, as the wood names them. The letters stop after two ("In the memory of our home, our families…"); the grain does not stop.

**The round.**
- Eldest wood, petrified; round pith (older than the war); Myststone overlay.
- Nine rings, 4 / 3 / 2 by movement, and the seal.
- **The axis points right** (turn 90°), so the top of the round stays clear for the course of Shoreland letters cut across it (the MIXED surface). Nothing is cut on files 10–14 in rings beyond half the radius.
- **Files.**
  - In band I, 0 is the stone-man.
  - Through bands I–II, 4 is the stone, the sail on it and the marks on the sail, one referent held by the ray r2–r7.
  - 6 is the stone-folk coming; 8 is us, the other side.
  - In band III, files 0–4 are new referents: the five.

```
round STONE (I-1-facing) {wood: eldest (Myststone); pith: round; rings: 9; rules after: [4, 7]; axis 90°}
  I
    r1    0: STONEFOLK*
    r2    0: LONE          4: DEEP+SQUARE
    r3    0: BREAK         4: BLOOD+SAIL
    r4    4: CARVE+HAND    6: STONEFOLK×3
  II
    r5    4: EYE           8: HULL×3
    r6    4: HOLD          8: TREE×3        mem 4: r6 → pith
    r7    4: CARVE         8: US+HOLD
  III
    r8    0: HOMESTONE     1: BLOOD×3       2: KNEEL      3: OPEN+DOOR      band STILL r8 file 4
    r9    0: STONEFOLK×3+RISE               8: US×3+RISE   (the twin)
  bark
    bark  0: HOLD                            (the seal)
  ray  file 4: r2–r7 (the same stone, sail and marks)
  tie  0.r2 → 4.r2 · 0.r3 → 4.r3 · 6.r4 → 4.r4 · 8.r5 → 4.r5 · 8.r6 → 4.r6 · 8.r7 → 4.r7   (all: does it to)
```

| Ring | Literal reading | The telling (the wood's words) |
|---|---|---|
| (seal) | held | *This is held in the grain.* |
| r1 | one of stone (the root) | *It is of one of the stone-folk.* |
| r2 | alone, ahead of the rest, going to the last stone | *He went up alone, ahead of the rest, to the last stone that stood.* |
| r3 | breaking the blood-sail; the same stone | *He tore his sail, the red one, and set it on the stone.* |
| r4 | marks cut on it, a hand of them; stone-folk, many, coming to it | *He cut marks on it, a hand of them; and the stone-folk came to it, one and then many.* |
| r5 | boughs, many, seeing it | *Every bough that came against that stone saw it.* |
| r6 | groves, many, holding it; remembered, to the heart | *What the boughs saw went home through the roots, and the groves held it.* |
| r7 | one of us, holding the marks | *One of us held your marks the longest.* |
| r8 | home (of stone); bloods, many; kneeling; the open door; the stillness | *Home. Kin. The one they kneel to. The open door. The stillness.* |
| r9 | stone-folk standing for these; and the twin: we, standing, on the other side | *They stood for these at the stone. We stood for the same, on the other side of it.* |
| (seal) | held | *…and the grain holds it still.* |

- **The five, clockwise from the axis in the Title's own order:**
  - *our home* is HOMESTONE, their home of stone;
  - *our families* is BLOOD×3, kin;
  - *our God* is KNEEL, "the one they kneel to". It is reverent: kneeling is the Aelthar's first and holiest step. Faith is never the butt of a joke (N18);
  - *our freedoms* is OPEN+DOOR, the open door ("we were a people of doors", IV.3);
  - *our peace* is STILL, still water.
- **The twin is the leaf's meaning.** It carries the foreword's "a tale told from one side of a wall is half a tale", and it completes the first spread.
- **The Last Carver's constraint, mirrored.** He learned our letters only from the Title. The Stone's round uses **only signs and devices the player's sign-list holds by the end of the Finale** (§4.2). The builder's validator must enforce this, so a decoder can read the last leaf by rule, as the Carver read the Title.

**The leaf's three stages:**

| Stage | When | The leaf shows |
|---|---|---|
| **0** | first launch until the Epilogue | the Stone's own rings, seed `I-1-facing`: pith, rings and bark, **no marks**. In the grain an unmarked round has no root and so no axis, and reads truthfully as *nothing is given here*. Under it is Seren's line in her course-hand, replacing the English *Untold. Halyna cannot yet hold this deep.* (Shoreland spec) [call §8.1] |
| **1** | the next launch after the Finale, or the credits: the Epilogue | the **same rings** now carry their marks, and the course of Shoreland letters, *In the memory of our home, our families…*, is cut across the top. Seren's Epilogue is laid beside it. The marks may grow in; reduced motion shows them at once. "The first leaf answered" |
| **2** | *The Last Carver* (§4.5) | the telling above is **added** beneath the round, in the wood's italic, with one line in the Book's own voice: *Known by no one at this hearth. Set down for whoever has learned the grain.* Nothing is removed |

Drawing: `wf6/svg/STONE.svg`. The prototype marks the letters' course only as a reserved band.

### 5.8 · Also: *Grow until the shore is silent* (V.4), the war-pith

The council laid a young silverbark open to the heart while it still stood, and cut the first carving of the war into it.

```
round GROW {wood: green (a young silverbark, standing); pith: round; rings: 2}
  I
    r1    0: GROW^r2*
    r2    2: !MOUTH+SHORE
```

- **Literal reading:** *Grow, until (the span): the shore not speaking.* **English:** *Grow until the shore is silent.*
- **This is the last round pith of the war.** "The wood, which cannot unlearn what is carved in it, grew." Every heart grown under that council since has a **square pith**: the carving closed to a point, "beneath all the other carvings, as the first ring lies beneath all the rings". The square is the Mute Square, "how they cut the word for stone". The war's wood grew the mute thing into its own heart.

---

## 6 · APPENDIX A · THE SOFT LETTERS (*rhelranth*): a sketch

The canon gives the Mystaeri a third writing behaviour: "letters no one could read, fine and curling, as beautiful as frost on a window". It was cut on stone, and "here and there among the letters they had tried to cut our own words by their sound … the sounds were close, and the symbols wrong" (IV.1, IV.2, IV.5; inventory §F1). These letters spell **sound**. Stone carries no knowing, and that is why "stone does not translate": to anyone without Seilrhass they are mute. By the craft's truth rule (§7), anything shown must be a real encoding. This sketch makes the mute stones real [call §8.6].

- **The letters.** There are thirteen, one per sound, plus two marks. Each consonant is a fine **stem with a curled head** (a frost-fern); each vowel is a **hanging drop of rime** under the letter before, as frost beads under a twig. (A three-toed bird's foot was the first sketch; it is the inverted rune algiz, so it was dropped in the originality pass.)

| Consonants: a stem whose head curls | | Vowels: a rime-drop hanging under the letter before |
|---|---|---|
| **v** curl right · **th** curl right + 1 barb · **s** curl right + 2 barbs | | **a** one round drop · **e** a drop drawn out to the right · **i** a bead (a dot) |
| **l** curl left · **r** curl left + 1 barb · **rh** curl left + 2 barbs | | **ae** the drop and a bead beside it · **ea** the drawn drop and a bead · **ei** two beads |
| **n** a double curl, both ways | | **the knock**: a short hook between syllables · **doubling**: a second head on the stem |

- **How it is written.** Lines run left to right along a gentle curve, as on the face of a standing stone. A word ends with a space. Each curl is at most 270°, single and never nested, so the hand stays clear of spirals (Nomai), stem-and-bow letters (Tengwar) and tallies (Ogham). **The strokes are fine and even (monoline), and every stem is upright:** curling letters cut with a thick-and-thin nib and a Z or 2 for a skeleton are what D'ni looks like, and this hand must never look like it (§3.13).
- **Shoreland by sound.** The letters have no stops and no back vowels, so a Shoreland word is spelled with the nearest sounds:
  - *p, b, m, f, w* are written **v**;
  - *t, d* are written **th**;
  - *k, g, h* are written **rh**;
  - *o* is written **a** and *u* is written **e**;
  - a Shoreland *y*-vowel is written **i**.

  The Shoreland designer's words then drop straight in: "the sounds were close, and the symbols wrong".
- **The mute stones' warning** (a proposal, cut in the frost-hand):

  > ***Nael enth li naelsaenen ni rhith. Le rhithveir ni eisse. Ve nael sath li eisse.***
  > *At the edge of the grey, do not fell the pillars. They are not timber. We are behind the grey.*

  The Guest's three Shoreland words are then spelled among the letters by sound.
- **Unlocks.** They never translate by reading, because "stone does not translate". Their meaning is **added beside them** from the wood: at IV.2 (Cam 16), "so we cut our plea on the mute thing", or at IV.4 (Cam 18). The three grey stones of Eldhythe's harbour-house get theirs when Thaesaen falls (inventory D4.4).

---

## 7 · INTERFACES

**For the Shoreland (course-hand) designer:**
- ***Mystaeri*** = the Shoreland root for mist + the borrowed Eldest ending *-aer* + a Shoreland plural in *-i* (§2.4). Supply the root.
- **The Last Carver's "one word too many."** Seilrhass marks any held or remembered thing with ***ra***, "this, the held one". A Mystaeri carver cutting *memory* therefore reaches for a definite word. That word is the Shoreland article or particle, which Shoreland omits in *in memory of*.
- **The Guest's three words** are Shoreland words. In Seilrhass they would be *rheil, nael, vease*.
- **The MIXED surface** (the Stone).
  - The course of letters is cut across the top of the round, above the pith, with the round's axis turned to 90°.
  - The grain keeps files 10–14 clear beyond half the radius (§5.7).
  - Letters are cut with the chisel (stone facets). The grain's rings run under the bed.
- **Seren's untold line** replaces *Untold. Halyna cannot yet hold this deep.* in her course-hand. It sits under an unmarked round on I.1's facing leaf, and under each blank wood leaf's full round. If Jack prefers the wood's hand for it, the Seilrhass is ***Ni theinas. Halyna ra eir ni theine.*** "No knowing. Halyna do not yet hold this."
- **One proverb, two tongues.** *Ith li thaess, vann li thaess* is *Harm to one is harm to both*.
- **Seren.** Nothing here gives Mystaeri any meaning to *Seren*. *Ser-* is not a Seilrhass root.

**For the Legends / tab builder** (the generator stays in `scratchpad/wf6`; only HTML goes to `Docs/`):
- Draw rounds inline as SVG from GN, using the tokens of §3.11.
- Show glosses per mark (hover, tap, or a list under the round), at the band's fidelity (§4.2).
- Replace the blank-leaf line as in §4.3–4.4.
- Draw II.2's `[ ]` as the Naelear chip.
- Keep `role="img"` titles that do not leak.
- Book | Modern changes only the gloss language (§4.6).

**For the fleet design (Admiral doc):**
- **Replace the Runic `᛫` placeholder** in §9b with the root sign drawn alone.
- **The Knowing line** shows the round, glossed at the band's fidelity.
- **The Knowing generator** emits GN from the sim's record, using the vocabulary table in §3.9. It works as follows:
  - the carving's roles become files;
  - its steps become rings;
  - its links become ties;
  - its hinges become forks;
  - its habits go to the aim place.
- **A Throne's groans** are pale rings in its bark.

---

## 8 · FOR JACK

1. **The leaf facing I.1 before the Epilogue.** Recommended: **(a) its rings only**, which is truthful ("nothing is given"), and "stood empty … with the grain drawn on it". The alternative is (b): its marks from the first launch, as a reward for decoders. Then the Epilogue adds only the letters, and a decoder could read the wood's half of the Torn Cloak on minute one (§5.7).
2. **The Stone's telling** (§5.7). The wood names the Title's five things as *home; kin; the one they kneel to; the open door; the stillness*, and closes: *"They stood for these at the stone. We stood for the same, on the other side of it."* Keep, change, or leave the Stone's grain untold for ever?
3. **The names:** ***Seilrhass*** (the spoken tongue, "bough-thunder") and ***Eilseth*** (the grain as a written craft, "ring-carving"). The Book itself can go on saying "the thunder-tongue" and "the grain".
4. ***lanth*** "knot, wait" shares a form with a piece of Sindarin *Lanthir*, but not a word or a meaning. Keep it, or use *aneth*?
5. **Pronunciation.** Should *ae* be the "a-eh" glide given here, or "ay" as most English readers say *Nael*? The design works either way.
6. **The soft letters** (Appendix A). Adopt the sketch so that the mute stones become real? Or keep them as described, never drawn? The truth rule forbids drawing fake letters.
7. **The translation achievements** (§4.5). Their names, and whether they show as achievements or simply as the Knowing bands.
8. **A third, "Original" view** for decoders (the literal reading) beside Book | Modern.
9. **Stage 2 of the facing leaf.** The one-line note in the Book's own voice: *Known by no one at this hearth. Set down for whoever has learned the grain.*
10. **The originality pass** (`wf6/originality_report.md`). Nine signs and the root-foot were recut because they were runes or certhas (§3.13). Three calls are left to you:
    - **BARB, the Bar Before, is a Latin cross.** "A bar laid across a stroke" is the canon's own description, so it was not recut. It also matches Cirth *l*. If a cross on a Mystaeri root reads wrongly in a Book whose other people pray to *Mardh*, the least change is to bow the bar strongly along the ring, so that it reads as a screen or a bow and not a crucifix.
    - **STOP is a T, and HOME and HOMESTONE are a 9 and a square 9** (and turned, the Tengwar *silme nuquerna*). A tail crossing HOME's stem was tried; it read as a Latin *a*, so it was withdrawn. Keep them, since among the rings they read as cuts, or ask for a recut?
    - **The knock's apostrophe.** Every word of two or more syllables prints with an apostrophe after its first syllable (*Nael'enn*, *Seil'rhass*). D'ni names do the same (*Ae'gura*, *Er'cana*, *Ti'ana*), and so does Na'vi (*Na'vi*, *pa'li*), and *Myst-* already points at Cyan. The canon forms (*Ael'thar*, *Ra'lensaen*) stay. Recommended: print the knock only where a Mystaeri is heard speaking, and write every other Seilrhass word soft, as the grain does (*Naelenn*, *Seilrhass*).
    - **Counting in fives** (*vinn*, hand) is ordinary among real languages, but a Myst player may think of D'ni's base 25. Keep it; it is listed only so that no one later builds a boxed or rotated numeral set on it.

---

## 9 · FILES (scratchpad only; nothing here goes into `Docs/`)

**Language:**
- `wf6/lang/lexicon.tsv`: the 215-entry lexicon, as data.
- `wf6/lang/check_lex.py`: the phonotactics, duplicate and blacklist checker, with `blacklist.txt`.

**Grain:**
- `wf6/grain/signs.json`: the 70 signs, as drawn.
- `wf6/grain/grain.py`: the renderer. It has the seed, rings, joined piths, V-cut facets, bands, rays, ties and bark.
- `wf6/grain/samples.py`: every sample round, as data.
- `wf6/grain/gn.py`: the Grain Notation linearizer.
- `wf6/grain/specimen.py`: close-up sign specimens.

**Drawings** (in `wf6/svg/`):
- `E1-01.svg` … `E1-07.svg`, `BURN.svg`;
- `VI-1.svg`, `NAELEAR.svg`, `AELTHAR.svg`, `GIFT.svg`, `E2-01.svg`, `E4-01.svg`, `STONE.svg`, `GROW.svg`;
- sheets: `hasty.svg`, `spec1.svg`, `spec2.svg`; PNG previews alongside.
- *These are the prototype's drawings, superseded by `render_grain.py`'s `grain_*.svg` (§10). They predate the originality pass and still show the old TREE (a rune), SAIL, KNEEL, BOND, DOOR and root-foot, and `grain/grain.py` still draws the old even root-foot. Use only the `grain_*.svg` files.*

**Originality pass:** `wf6/originality_report.md`, and its tools in `wf6/orig/`: `apply_grain.py` (the sign recuts), `apply_mystaeri_spec.py` and `apply_shoreland_spec.py` (the spec amendments), `compare.py`, `compare_shore.py`, `specimen.py` and `snap.py` (the before-and-after sheets, in `wf6/orig/shots/`).

---

## 10 · RENDERER NOTES

*Added 2026-09-27 with `wf6/render_grain.py`, the grain renderer that replaces the prototype `wf6/grain/grain.py` for drawings. Scratchpad only. Where these notes differ from §3.2–3.11, the drawings follow these notes. Each numbered item is marked [rule] (a resolution Jack need not look at) or [call] (worth his eye).*

### 10.1 · What it is

- **One file, standard library only.** It reads the sign table `wf6/grain/signs.json` (the same as §3.5's JSON block, which the decode test, §10.11, and the originality pass, §3.13, have amended), and it takes one *grain text* (§10.2) per round from `wf6/grain_texts/*.json`.
- **Output.** It writes one self-contained SVG per round to `wf6/svg/grain_*.svg`, plus the sign chart and two name-chips. The index is `wf6/svg/index_grain.md`.
- **Commands.**
  - `python3 render_grain.py TEXT.json -o OUT.svg [--state whole|fragments|locked] [--stage0]`
  - `python3 render_grain.py --chart`
  - `python3 render_grain.py --all`
- **Checks.** It checks its own output:
  - no two rings of a field come within 4 units;
  - no joined pith's own rings touch another's;
  - no mark point crosses the bark contour;
  - every round is within the 60 KB budget.
  - It also prints sizes. The last run gave no warnings.
- **Screenshots.** `wf6/shot.py` and `wf6/crop.py` inline the SVGs into a dark page and shoot them with headless Chrome. The PNGs are in `wf6/shots/`.

### 10.2 · The grain text: Grain Notation as JSON [rule]

A round is written the way it is read: bands, then rings, then marks.

| Key | Meaning |
|---|---|
| `id`, `seed` | The seed is `seed` if given, else `id` (§10.4). Examples: `E1-01`, `IV-4-gift`, `I-1-facing` |
| `english`, `literal`, `root_word` | the telling, the literal reading and the root's one word. These feed `<title>` and `<desc>` (§10.9) |
| `wood`, `stone`, `pith` | wood is `green`, `forty`, `long`, `eldest` or `plain`; `stone: true` is Myststone; pith is `round` or `war` |
| `axis` | degrees; omitted means the seeded ±12° turn |
| `bands` | `[{band: "I", rings: [{marks, conditions, included, graft, empty}, …]}, …]`. Ring numbers run on through the bands. The band-rules fall where the band changes (override with `rules`) |
| `bark` | `{marks: ["0: HOLD"], pale: n}` |
| `piths`, `own_rings` | joined piths by file (`[{file: 0}, {file: 5.3}, …]`) and the number of rings each pith owns |
| `rays`, `memory`, `ties` | GN strings: `"3: r2–r4"`, `"8: r8"`, `"p0·0.r1 → 4.r2"` |
| `split`, `char` | E1-01's split along the axis; Burn's charred plank-end |
| `has_stage0`, `stage0_english` | the Stone's unmarked stage |

- **A mark is a GN string:** `"[pN·]file: TOKEN[+TOKEN…]"`.
  - Prefixes: `!` not, `~` hollow, `_` smoothed, `>` causative.
  - Suffixes: `×3`, `½`, `?`, `#n`, `@n`, `^rj`, `*` (the root), and `/` or `\` (lean ±16°).
  - A ligature splits the span into modifier (u 0–0.48) and head (u 0.52–1).
- **An object mark** `{file, root, parts: [...]}` is for composites. Each part takes `u`, `lean`, `scale` and `in_curl` + `size` (folded inside an earlier part's curl). Only VI-1 needs it.

### 10.3 · One ink: currentColor [rule]

- **All paint is `currentColor`** on the root `<svg class="wood-ink">`. The only literal colours in a file are the mask's black and white, which are luminance, not paint.
- **How colour is set.**
  - Inline, the page's `.wood-ink{color:…}` rule or the inherited colour wins.
  - `:root.wood-ink{color:#dcc9a2}` applies only when the SVG is its own document (an `<img>` or an opened file).
- **§3.11's token table becomes opacity tiers of the one ink:**

| Tier | Opacity | Tier | Opacity |
|---|---|---|---|
| wood surface | 7.5% | lit wall | 97% |
| bark band | +8.5% | mid wall | 74% |
| heartwood (inside band-rule 1) | +4.5% | shade wall | 48% |
| year hairline | 13% | flat pocket (HEART, PILLAR's trunk) | 82% |
| latewood band | 34% × 0.62–1.12 per ring | char block | 50% |
| band-rule line | 50% | hairlines (ray, memory, tie) | 62–70% |
| included bark (jagged line) | 48% | mist | 12% |

- **The fresh-cut convention.**
  - On a dark page the cuts are the palest thing in the round, as fresh wood shows pale inside weathered wood.
  - Voids are knocked out to the page. They are the char gaps, the checks, the knot's heart, the split and the dread shake.
  - On a light page the same file reads as an engraving, with the char dark.
- **Colour tints.**
  - Green wood has no tint.
  - Myststone is a fine stipple pattern (dots and a few glints) instead of the stone-grey overlay.
- **The mask.** Every cut, char block and void knocks the wood out beneath it with a 1.7-unit margin. No cut ever sits on a ring line, and a mark stretched across rings visibly parts them.

### 10.4 · The seed, split into streams [rule]

- **Same seeding, named sub-streams.** mulberry32 over FNV-1a, as §3.2, but split into named sub-streams:
  - `id/shape`, `id/widths`, `id/ring/k`, `id/late/k`, `id/bark`, `id/barktex`, `id/plates`, `id/year/…`;
  - `id/mark/<pith>/<ring>/<file>/<index>`, and so on.
- **What follows from it.**
  - Adding or removing a mark never moves a ring.
  - The Stone's stage 0 and stage 1 share every ring and the bark contour exactly (measured difference 0.0).
  - Two full runs are byte-identical.
- **Seeded from the id, not the content.** The task asked for seeding "from the text". The id is the text's own name, so the round is seeded from its id and not from a hash of its content. A content seed would redraw the Stone between its stages and break G2's likeness between a carving and its parent.

### 10.5 · Rings, knots, joined piths, bark [rule]

- **Ring shape.**
  - ε ∈ [0.05, 0.12] and a_m ∈ [0.012, 0.030]/(m − 1) for m = 2, 3, 4, 5, 7. The spec's [0.04, 0.09] and [0.010, 0.022] drew the 11-ring gift as a target.
  - Per-ring wobble uses the whole allowance, min(2.5% R_k, gap/5).
  - A fine wobble (m = 9, 13, 17, ≤ 1.3 units, ∝ R^0.8) is shared by all rings, so it cannot make two cross.
  - Ring widths, heart ring, pad and B are as in the spec.
- **Latewood.** Each ring line is drawn as a latewood band 0.8–3.2 wide, varying round the ring and crisp on its outer edge. Its strength varies from ring to ring. There are 1–2 year hairlines per ring (one when K > 6).
- **Knot deflection.** The formula is r′ = r + s·c·e^(−(d/σ_r)²)·e^(−(Δθ/σ_θ)²), where:
  - c = ru + 6, σ_r = ru + 8 and σ_θ = 1.7·rx/ρ_k;
  - s is the side of the knot the ring lies on at the knot's bearing.
  - Its slope is ≥ 0.14, so the grain flows round a knot and never crosses itself. Year hairlines flow round it too, and that is what makes E1-06 read.
- **Joined piths (G8).**
  - Each pith's own rings are near-circles no larger than R_k, so they can never touch: the centres are 2.29 R_kj apart.
  - The join is the smin level set at R_kj + 6, doubled 5 outside. It is band-rule 1 of a joined round.
  - The first shared ring is widened by 11 to hold it.
  - Shared rings take their shape as an addition to the level value, so the first always encloses the piths.
- **Bark.**
  - Plates bulge between irregular fissures, and each fissure's V-notch runs on inward as a crack, with short laminations on the plates.
  - A sapling's bark (K ≤ 2) is smooth, with fine fibre only.
  - **A name or seal is cut on a sound plate:** no fissure lies within ±0.16 rad of a bark mark's file, at every stage.
  - A bark mark spans r_K + 3.5 to (the lowest point of the contour across the mark's breadth) − 4.5, with B ≤ 0.8 L. Nothing crosses the contour.

### 10.6 · Cuts [rule; the weight change is a call]

- **Weight [call].** H = 0.16 B (1.8–7) for ordinary marks and 0.17 B (3.2–7) for the root. The spec's 0.14 and 0.15 read thin at display size. Weight is still fixed per class and carries nothing.
- **Taper.** Each end tapers over min(0.16 × length, 2.4 H), so long cuts keep crisp ends. **A root's foot is blunt and starts in the pith:** its first point moves to u = 0 and the pith is drawn over it. That is "cut from the pith outward". Burn's wedge starts at the pith too.
- **Three tones.** A wall facing the light (n·L > 0.26) is lit, one facing away is shade, and the rest are mid. A cut that runs with the light shows two mid walls, as it does under raking light.
- **Chip-carved pockets.** Wedges, triangles and count or ordinal bites are three facets meeting at the deepest point.
- **Lenses and drops** pinch their groove at the tips.
- **Checks** (WOUND, BREAK's head, SPENT, GRIEF) are a crack with one lit face and one void face. A V-cut has two walls, so the two are distinct.
- **Burn's char** is broken into charcoal blocks (six rows of 1–3), parted by checks. It is the only such texture in the grain.
- **The entry-nick** starts 0.30 B off the file beside the head and runs at 50° out to 0.64 B. It is attached to the head, not floating.
- **Scaled parts** are cut with a finer knife: H × scale, with a minimum of 0.45. These are VI-1's folded name and `½`.
- **The root-foot** is three roots, each drawn in six steps that turn a little further outward as they go (`ROOTFOOT` in the renderer: −64°, −10°, +38° from the file; 0.40, 0.30, 0.36 B; bowing 16°, 6°, 14°). Under negation the angles mirror with everything else. *Changed by the originality pass.*
- **`curve`** on a cut draws a Catmull-Rom curve through its points, ends clamped. SAIL's cloth uses it. *Added by the originality pass.*
- **Economy.** Arc-length resampling at max(2, 1.15 H) keeps every corner over 20°. Douglas-Peucker at 0.12 units runs on every facet. Cuts are written in tenths; the wood's long curves are written in whole units.

### 10.7 · Devices [rule; the tie is a call]

- **Ties [call].** A tie is a hairline that **tapers from its source (1.9 wide) to its target (0.3)**, as a shoot thins as it reaches. §3.7 gave a tie no direction mark; an arrowhead read as interface, not wood.
  - Same-ring ties run along the ring's middle and always take the short way round. If a mark in that ring is in the way, they pass over it at 0.88 of the ring. A long way round read as a ring shake.
  - Cross-ring ties run from 0.82 of ring i to 0.22 of ring j, then **land on the marks' own files**: the path is bent over its first and last thirds so that it leaves just past the source's head and arrives just under the target's foot, with no elbow.
  - **Each end stops one knife-width (`TIE_GAP`, 3 units) from its mark**: the path is drawn file to file, sampled a unit apart, and trimmed where it first clears its source and where it first comes within 3 units of its target (distances are to the mark's own facet edges, which each placed mark now keeps).
  - *Changed by the decode test (§10.11).* The ties used to stop 1.15 B/ρ off the file. A mark's breadth is about 0.8 of a slot either side, so that offset put the end more than a slot away: 8 of the 28 tie ends in the samples (4 of the 14 ties) sat over a neighbouring, empty file (E2-01's tie read 2 → 3 instead of 0 → 4). Now every end reads to its own mark, at 3.0–3.9 units.
  - **Checked:** for every tie end, its own mark is the nearest mark by at least 2 units, and an end more than 4.5 units from its mark must lie within half a slot of its file (the one tie that ends on an empty file, E4-01's reach going east, does). A failure is a warning.
- **Rays** are straight hairlines along the file, hidden where they pass under the marks they join.
- **Memory rays** run straight from the mark's foot to its pith. In a joined round that is the pith nearest the file's bearing, which is how E4-01's reach remembers the south. They end 9 units from the pith in three root-hairs, uneven on purpose (−38°, −4°, +26°; 6.5, 5.0 and 5.8 units).
- **Included bark** is a jagged hairline (±0.95) over a faint band, 2.6 outside the ring line. It is unlike a ring (smooth) or a band-rule (a clean double).
- **The graft** is the same jagged line as a V, from the ring's inner line out to ±1.25 B.
- **Conditions.**
  - MIST has calm edges and fades at its ends (not smoke).
  - WHITE's frost ticks fall every 4°.
  - DREAD is a shake opening to 2.4 at its middle, knocked out, with a bright upper rim.
  - WATER waves at a 44-unit wavelength.
  - STILL is two hairlines 3 apart.
  - DARK is a 7% stain.
- **The split** (E1-01) is a 2.6-unit gap through wood, bark and cut alike, with two pale split faces. The curl lies on one half.
- **Burn's charred plank-end** darkens the bark there through the mask. It carries nothing.
- **Implemented but unused by any sample:** count, ordinal, causative, question (an open head at the ring line), pale groan-rings, WHITE, WATER and DARK.
- **Not yet drawn:** fork and chain.

### 10.8 · Composites and samples

- **VI-1 [call].**
  - HOLD sits at u 0–0.12 at 0.75 scale.
  - HOME sits at u 0.12–1.0, leaning +16°, at 1.15 scale.
  - HOMESTONE sits at u 0.12–0.84, leaning −26°, at 0.78 scale.
  - US×3 is folded at the centre of HOME's loop, 0.1 L tall at 0.2 scale.
  - At the spec's ±16° and one-tenth scale the two loops collided and the name could not be seen. The name is still tiny, "as a seed is folded in a fruit".
- **AELTHAR r3.** `US/` and `US\` lean ±16° about their own feet, toward each other. Files 15 and 1 are 45° apart, so crowns cannot meet.
- **E4-01.** The GN of §5.6 is followed over G3.
  - Rule 1 is the join after r2.
  - Pith 0's r1 and r2 each carry included bark, from E1-01 and E2-01, as single lines.
  - The pith-local DREAD band and tie are drawn (the prototype left them out).
- **The gift's round** has no bark seal, because its GN gives none. §3.3 would give a telling's bark the seal [call].
- **The Stone.**
  - Its top is left clear and nothing is drawn there. The course of letters belongs to the Shoreland renderer (the MIXED surface); a placeholder band would break truth-or-nothing.
  - Stage 0 has the same seed, rings and bark, but no marks, band-rules, hairlines or conditions. It has no root and so no axis.
- **Chips.** `grain_AELTHAR_name.svg` (§5.3a) and `grain_NAELEAR_chip.svg` (II.2's inline untold word) are annular sectors of a large round, with the sign in the middle ring.

### 10.9 · Accessibility and sizing [rule]

- **Every file** has `role="img"` and `aria-labelledby` pointing at its `<title>` and `<desc>`.
- **States.**
  - `whole` (the default): the title is the English and the desc is the literal reading.
  - `fragments`: the root's word only.
  - `locked`: *A carving in the grain, not yet known*, with no desc (§3.11).
  - Stage 0: *Nothing is given here.*
- **IDs** are prefixed with a hash of text and state, so many rounds can be inlined on one page.
- **`data-round`** carries the round's id only in the `whole` state. Locked, fragmentary and stage-0 files omit it, because the ids name what the rounds tell (`naelear`, `aelthar-rite`, `IV-4-gift`). *Changed by the decode test (§10.11)*, which found it in the stage-0 Stone and in every file drawn with `--state locked`.
- **Intrinsic size** is 0.6 × the viewBox, so the Law of the Rings stays visible: a sapling is about 130 px and the gift about 800 px. Pages size by CSS; `data-r-outer` carries R_outer for the §3.11 rule.
- **Sizes (KB).** Every round meets the 60 KB budget.

| Round | KB | Round | KB | Round | KB |
|---|---|---|---|---|---|
| E1-01…07 | 8.3–9.6 | GIFT | 58.8 | AELTHAR | 31.2 |
| BURN | 9.9 | STONE | 55.5 | NAELEAR | 17.2 |
| E2-01 | 17.0 | STONE stage 0 | 25.7 | GROW | 11.3 |
| E4-01 | 49.7 | VI-1 | 11.4 | chips | 8.5, 10.8 |

*(Sizes after the originality pass's recuts.)* The sign chart is 533 KB. It is a reference sheet, not a round.

### 10.10 · The look check

- **Checked by eye on a dark page at 670–1340 px, with zoomed crops.**
  - The rounds show many irregular concentric rings, an eccentric pith, latewood of varying strength, and plated bark.
  - The cuts are crisp and faceted, and they run in one direction, from pith to bark.
  - The only soft element is the mist, which has calm edges.
  - Nothing crosses the bark, and weight is uniform.
  - They read as wood cross-sections carved with meaning. There is no single ring, ink, smoke or tendril, so they read as nothing like Arrival's logograms.
- **Latin-letter likeness, as §3.13 foresaw:** HOME (a "9"), HOMESTONE, DOOR (a "Π"), SAIL (a "P"), STOP and BARB (a "T" and a dagger). Among the rings they read as cuts. The chart shows them alone and small, not large [call: whether any should be recut].
  - *The originality pass answered part of this call.* SAIL (which was the rune thurisaz rather than a P) and DOOR are recut; HOME, HOMESTONE, STOP and BARB are left for Jack (§8.10).
- **Legibility.** A 9–11-ring round is legible at 900 px or more, and its marks are about one ring tall. §3.11's tap-to-enlarge is needed below that.

### 10.11 · The decode test [rule]

*Run 2026-09-27 (`wf6/decode/`, report in `wf6/decode_report.md`).* Six rounds were decoded from screenshots alone, with `<title>`, `<desc>` and every `data-` attribute stripped, using §0–4 and these notes and nothing else: E1-03, VI-1, E2-01, GROW, AELTHAR and E4-01. Each reading was then compared with §5. What failed, and what now stops it recurring:

| Round | What the decoder read | Intended | Cause | Fix |
|---|---|---|---|---|
| E1-03 | LONE: *one goes ahead of the rest* | *Go until struck. Where bark splits, turn aside.* | spec: the whole young-wood orders lived only in §5.5 | §3.5 now has the sapling table (one word and whole order per root) |
| VI-1 | HOLD: *hold* | *remember* | spec: §3.5 said *remember* is HOLD **with a memory ray**; the sliver's HOLD at the pith has none | §3.7: "held at the root", HOLD cupped round the pith, is the memory ray's own heart |
| AELTHAR r1 | AXE (*the felling*) | KNEEL | renderer + sign table: a root in a 56-unit heart ring is ~16 units broad, and KNEEL's fold (0.58 B) lay against its stem like AXE's blade | KNEEL's fold widened to (0.30, 0.86); §3.5 says what tells the two apart; §3.12 overlays them at root size |
| AELTHAR r3 | two US, each tilted toward the other: no rule | brow to brow, at one hour | spec: GN had `/` and `\`, but §3.7 gave a lean alone no meaning | §3.7: the lean device |
| E2-01, E4-01 | the tie from the root runs 2 → 3, to empty files | 0 → 4 | renderer: ends stood 1.15 B/ρ off the file, more than a slot | ties now land on their marks (§10.7) and the validator checks every end; §3.7 says ties are read by the marks they touch |
| E4-01 II | r3 file 2 an unknown three-armed cut; file 12 a "cut–knot–cut" | BOND; KNOT^r4, then GO in r5 | spec: nothing said that shared rings are measured about the round's centre, so the decoder used the nearest pith and turned the marks sideways | §3.3 and §3.4: the joined-round frame |

**Passed first time:** E1-03's structure (war-pith sapling, LONE on the axis), VI-1's structure (HOLD, the HOME = HOMESTONE pair, US×3 folded inside), E2-01's WAVE, band-rule over included bark, EDGE+BREAKER and DREAD band, all of GROW (`GROW^r2*`, `r2 2: !MOUTH+SHORE`), AELTHAR rings 2–6 and the seal, and E4-01's three piths, contained E2-01, graft, memory ray and bark name.

**Near misses, not failures.**
- **GROW's `!MOUTH`** was read by the entry-nick's side and by elimination. As a ligature's modifier it is cut at half length and full breadth, and its two arms close into a zig-zag. If a later test fails on it, cut ligature parts at 0.7 breadth with the finer knife (§10.6), and re-check every ligature.
- **E4-01's name in the bark** (BOND+TIDE) is about 7 px across at the intrinsic size. It needs §3.11's tap-to-enlarge.
- **DREAD against a same-ring tie:** both are hairlines along a ring. The shake is two lines with a knocked-out gap and a bright upper rim, a tie is one tapering line. §3.12 step 5 now says so.

**Re-test.** After the fixes every round was re-rendered (`--all`: no warnings, all ≤ 60 KB, byte-identical twice) and re-read by the amended rules. All six now read as §5 gives them. That second reading was not blind, because §5 had been opened. The tie check is mechanical (`wf6/decode/tie_check.py`): with the old renderer 8 of the 28 tie ends in the samples (4 of the 14 ties) read to a neighbouring file; now all 27 ends that join a mark lie 3.0–3.9 units from it and nearer to it than to any other, and the 28th (E4-01's reach going east) ends on its file.
