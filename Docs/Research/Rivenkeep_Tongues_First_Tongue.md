# RIVENKEEP · THE FIRST TONGUE

> **Imported to `Docs/Research/` on 2026-09-28** as a source behind `Rivenkeep_Tongues.html` and `Rivenkeep_Legends_Original.html`, which are canonical where they differ. Scripts, renderers and paths mentioned below belong to the design workspace and are deliberately not in the repo, which is documents only.


*wf7 design spec, 2026-09-27. A workflow document, not a Book leaf and not a repo doc. It answers Jack's note 8 of 2026-09-27: "The Latin cross is fine. Imagine that all languages come from an ultimate base language." It is built on `wf6/shoreland_spec.md` (Orrowen and the course-hand), `wf6/mystaeri_spec.md` (Seilrhass and the grain) and the Book (`wf6/legends_v12.md`).*

**What this is.** The one tongue that Orrowen and Seilrhass both come from, reverse-engineered as Tolkien built his primitive roots under Quenya and Sindarin. It gives a sound system, 624 roots, the ordered sound laws that turn them into both living tongues, and the sign-set from which the course-hand's letters and the grain's signs both descend.

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
4. **38 words are one word in both tongues** (§1.5). They fall where the Book already cares most:
   - the hearth's yes, *Tumar* "we remember", is the first tongue's "we hold". The Knowing, *theinas*, is the same holding;
   - the Title's *ol* "our", said five times, is the Aelthar's *ael* "together", and the green sliver's "too";
   - the proverb ends on one word in both tongues: O *vana*, S *vann*, "both";
   - the Riven Stone and the Torn Cloak (O *tresk*) are the wound in the Seilrhass proverb (S *thaess*);
   - *myst*, the Rivenmen's grey (in *Mystaeri* and the Mystlands), is the wood's between-light (S *neis*);
   - the Title's "home" (O *varn*) is the Stone's "peace", still water (S *vaere*).
5. **The sound laws are few and regular.**
   - To Orrowen, five laws make the Hal (the catch doubles a consonant or lengthens a vowel; the old diphthongs close; the i-colouring makes the slender class; *f* and *w* become *v*; three like consonants keep two). The spec's own laws, made exact, then make the living tongue.
   - To Seilrhass, five laws make the Eldest speech (the catch breaks the vowel; the brightening fronts every back vowel; the later vowels thin; lips and throat go soft; clusters simplify). The spec's own three then make the living tongue.
   - **Every existing word of both tongues falls out**: 310 of 310 Orrowen lexicon entries and 215 of 215 Seilrhass entries are accounted for, with **0 mismatches in 356 derivations**, and a short list of named irregularities (§4.3).
6. **The first marks are 45 signs** (§5).
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

| First tongue | Orrowen | Seilrhass | Where it touches the Book |
|---|---|---|---|
| *\*tol- / tal-* rise, stand up tall | *tolm* a stone · *tald* rise, stand up (v.) · *taldow* a tower, a high place | *thael* a tree · *thal* the neck, where life goes up into… | The one word for the standing thing split between the peoples: the stone-folk kept it for stone, the wood-folk for the tree. The mystaeri spec's analysis of thael as thae + \*-l is replaced. |
| *\*xreun-* set hard, harden | *rhyn* set fast (of mortar), take hold · *Rhyna* 'she who sets fast' | *rhen* stone, the mute thing | Rhyna's name and the wood's word for stone are one. The Guest's errand-name Aelrhen, 'bond-to-stone', is at the root \*ol-xreun: 'together, set fast'. |
| *\*tum-* hold, keep (in the hand and in the mind) | *tum* remember · *tumol* remembering | *thein* to hold | The hearth's yes, Tumar 'we remember', is in the first tongue 'we hold'. The Knowing (theinas) is the same holding. |
| *\*ol* together, one with another | *ol* we · *olna* we two (+S) | *ael* bond, joining | The Title says ol five times ('our home, our families...'); the Aelthar and the sliver's 'too' are the same word. |
| *\*pa-* two | *pa* two (+S) · *pana* both | *vann* two | The proverb's last word is this root in both tongues: grest um vana / vann li thaess. |
| *\*trosk-* split, cleave | *tresk* a cleft, a split | *thaess* to split | The Riven Stone and the Torn Cloak (O tresk) and the wound of the proverb (S thaess) are one word. |
| *\*krask-* crack, break | *cresk* break | *rhass* storm | Seilrhass, 'bough-thunder', is at the root 'the breaking of the boughs'. |
| *\*ston-* stand firm, hold one's place | *ston* stand (of a wall), make stand, hold firm | *saen* heartwood | The Stonwryt ('the standing cutting') and the Saenvael ('heart-grain') are one word at the root: the vow at the core of a wall, the order at the core of a hull. |
| *\*skeθ-* hew, cut into wood | *sceth* a ship, a hull (a trunk hewn out) | *seth* a carving | The stone-folk's word for a ship is the wood-folk's word for a carving: the Sethvaren is, at the root, 'the hull that bears the hewing'. |
| *\*molt-* the breath within | *molt* a heart | *nael* mist | What the stone-folk call the heart, the wood-folk call the breath. Naelear, 'those of the breath', is in the first tongue 'those of the heart'. |
| *\*mus-* the dim light | *myst* sea-fog | *neis* soft light | The Rivenmen's grey (myst, in Mystaeri and the Mystlands) is the wood's between-light. |
| *\*waʔr-* stillness | *varn* home | *vaere* still water | The Title's 'home' and the Stone's 'peace' (STILL) are one word in the first tongue. |
| *\*waʔl-* the inward bent of a thing: its grain… | *vall* love | *vael* grain | Love is the heart's grain. |
| *\*senn-* down, below | *senn* die: go out, as a fire in peace | *senn* beneath, under |  |
| *\*feʔ-* fade, go dark | *vess* a night | *veas* to die · *veath* night | Chiasmus with SENN: the stone's night is the wood's dying, and the stone's dying is the wood's 'beneath'. |
| *\*par-* bear up, hold up | *par* guard, protect · *pard* a warden, a keeper · *Halvard* 'bedrock-warden' | *var* to bear, to carry · *varen* a bearer | Halvard's -vard and the Aelvaren's -varen are one root. |
| *\*oð-* the rim where one stops and gathers… | *odh* a hearth · *odha* a mother ('she of the hearth') | *aeth* a shore | The first word the wood ever gave Halyna, shore, is the hearth's own word in the first tongue. |
| *\*trenn-* a running line: a course of stones… | *trenn* a course of stones | *thenn* water | A course of stone and a course of water: the stone-folk laid tales in it, the wood-folk heard the sea in it. |
| *\*lenn-* pale-bright | *lenn* silver | *lenn* white |  |
| *\*weinn-* sound, whole, true (as a plumb wall) | *venn* true | *veinn* to mend, to make whole | A True Man (vennuld) is, at the root, a whole man; the grain's MEND is 'make true'. |
| *\*kul-* leave off | *kyl* change | *rheil* to stop, to cease | The Captain's 'Change your shot' and the Guest's plea 'Stop' are one verb. |
| *\*grest-* a burning smart, a hurt | *grest* harm, hurt | *rhes* anger | Harm (the stone's word) and anger (the wood's) are the same heat. |
| *\*krenn- / krann-* weighty | *crenn* a captain | *rhann* heavy, great |  |
| *\*taw-* sprout, grow | *tev* a child | *thae* tide | A child is a sprouting; a Tide is a growing. tevow (Hal tevū) and tevel are built in the Hal on tev-, after the i-colouring. |
| *\*et- / itt-* this very one, the same | *et* the (the article) | *ith* one | The stone's article and the wood's 'one' are one word: 'the' is 'that one'. |
| *\*re* yonder, that | *re* past particle (+S) | *re* that · *reil* fore, front | A 'that' became the stone's past ('then') and the wood's fore ('the one before'). |
| *\*es* at another time, not now | *es* future particle (+N) | *es* -es, the past of a verb… | The stone looked forward with it and the wood looked back. |
| *\*xui* out of, from | *hy* from, out of (+S) | *rhi* from, out of |  |
| *\*na- / ni* not | *na* un- (prefix, +S) · *nath* not (before a verb, +N) | *ni* not (before the verb) |  |
| *\*aŋ-* at the hour | *amm* when (conj.) | *anth* an hour |  |
| *\*ros-* three | *rost* nine ('thrice three') | *raes* three | The stone kept the old three only in nine; its living three, sull, is new. |
| *\*xwre-* rime, frost | *frenn* frost, rime | *rhel* frost | A root of the cold. The stone built it with \*-n-, the wood with \*-l-. |
| *\*xwle-* a thin sheet: a leaf | *flenn* a leaf of a book or of slate | *lel* a leaf |  |
| *\*bro- / bra- / bre-* utter | *brod* a word · *brodh* put into words, tell, speak · *Brenn* Brenn: a name. Names are names | *ranth* a word (a spoken thing, which can break) · *renn* a mouth |  |
| *\*tann- / tunn-* shut in | *tunn* whole, complete | *thann* to close |  |
| *\*lo- / li-* at, by | *lo* at, by, with (+S) | *li* in, at, on (place) |  |
| *\*sa / se* that one, the one by you | *sa* who, which, that (relative, +S) | *sa* you (one) · *se* you (more than one) |  |
| *\*-en* belonging to | *-en* 'of, belonging to' | *-en* plural |  |

**Two crossings worth seeing.** Death and night trade places across the two tongues. The stone says "die" with *\*senn-* "go down" (O *senn*, "go out, as a fire in peace"); the wood kept *\*senn-* for "beneath". The wood says "die" with *\*feʔ-* "fade" (S *veas*); the stone kept *\*feʔ-* for "night" (O *vess*). In the same way, the stone's word for stone is the wood's word for the tree, and the wood's word for stone is the stone's word for mortar setting fast.

### 1.6 Four sayings, back to the first tongue

Each word of each line below is derived by the engine; the build fails if any does not come out.

**(a) The Title, and the green sliver's answer.**

*The Title: Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.*

| First tongue | Hal | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*ul-an* | ULAN | ul | **Ul** | in (+N) |
| *\*tum-ol-a* | TUMOLA | tumol | **dumol (N after ul)** | memory |
| *\*ol-on* | OLON | ol | **ol** | our (+N) |
| *\*waʔr-n-o-s* | VARNOS | varn | **varn** | home |
| *\*ol-on* | OLON | ol | **ol** | our |
| *\*thald-athi* | THALDATHI | thaldath | **theldeth (rebuilt on theld-)** | families |
| *\*ol-on* | OLON | ol | **ol** | our |
| *\*mardh-o-s* | MARDHOS | mardh | **Mardh** | God |
| *\*ol-on* | OLON | ol | **ol** | our |
| *\*lunn-athi* | LUNNATHI | lunnath | **lunnath** | freedoms |
| *\*ol-on* | OLON | ol | **ol** | our |
| *\*soʔl-an-o-s* | SOLLANOS | sollan | **sollan** | peace |

*The hearth's answer: Tumar.*

| First tongue | Hal | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*tum-ar* | TUMAR | tumar | **Tumar** | hold-1PL: we remember |

*The sliver: Ve ith naelenn ael raltheine.*

| First tongue | Eldest | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*be* | ve | ve | **Ve** | we |
| *\*itt-o* | ite | ith | **ith** | own |
| *\*molt-o* | naele | nael | **naelenn (nael + enn)** | breath (+ enn: home) |
| *\*enn-o* | enne | enn | **(in naelenn)** | within |
| *\*ol* | ael | ael | **ael** | too, together |
| *\*ral-o* | rale | ral | **raltheine (ral + thein + -e)** | root (+ thein: remember) |
| *\*tum-i* | teine | thein | **(in raltheine)** | hold |
| *\*e* | e | e | **(-e)** | now: the present |

The Title opens *Ul dumol ol varn*, "In memory of our home". At the end of the war the green sliver says *Ve ith naelenn ael raltheine*, "We remember our home too". Under both lie the same two first-tongue words, *\*tum-* "hold" and *\*ol* "together". The hearth's answer, *Tumar*, is *\*tum-ar*, "we hold". The canon says the sliver "gave them the answer of this hearth … and it did not stop where we stop". In the first tongue it is the same answer.

**(b) The proverb both peoples share.**

*Orrowen: Grest um hos, grest um vana. (Hal GRESTOS UMO HOSOS GRESTOS UMO PANĀ, exactly.)*

| First tongue | Hal | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*grest-o-s* | GRESTOS | grest | **Grest** | harm |
| *\*um-o* | UMO | um | **um** | upon (+S) |
| *\*hos-o-s* | HOSOS | hos | **hos** | one |
| *\*grest-o-s* | GRESTOS | grest | **grest** | harm |
| *\*um-o* | UMO | um | **um** | upon (+S) |
| *\*pa-naʔ* | PANĀ | pana | **vana (S after um)** | both |

*Seilrhass: Ith li thaess, vann li thaess.*

| First tongue | Eldest | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*itt-o* | ite | ith | **Ith** | one |
| *\*li* | li | li | **li** | at |
| *\*trosk-i* | taesse | thaess | **thaess** | a wound (O tresk, riven) |
| *\*pann-i* | vanne | vann | **vann** | two (O pana, both) |
| *\*li* | li | li | **li** | at |
| *\*trosk-i* | taesse | thaess | **thaess** | a wound |

The saying is older than the parting. The wood's wording is the older one: its words are the first tongue's own. The stone rebuilt all of it except the last word, and that word is still one word in both tongues: *vana*, *vann*, "both".

**(c) The Stonwryt under the old capstone.**

*ESAN STONOS ETAS XALDOS SIU · RE CADHANA OA ETHAS TESSANA OA SOŊMAS ELIS TOLMOS TOLMOS · STONOS: each Hal word is also the first tongue's*

| First tongue | Hal | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*es-an* | ESAN | es | **Es** | FUT (+N) |
| *\*ston-o-s* | STONOS | ston | **ston** | stand-3SG |
| *\*et-as* | ETAS | et | **et** | the |
| *\*xal-d-o-s* | XALDOS | hald | **hald** | wall |
| *\*siu* | SIU | sy | **sy** | this |
| *\*re* | RE | re | **Re** | PST (+S) |
| *\*kadh-ana* | CADHANA | cadhan | **hadhan (S after re)** | lay-1DU |
| *\*o-a* | OA | o | **o** | it |
| *\*eth-as* | ETHAS | eth | **eth** | and |
| *\*tess-ana* | TESSANA | tessen | **tessen** | answer-1DU |
| *\*o-a* | OA | o | **o** | it |
| *\*soŋ-ma-s* | SOŊMAS | somm | **somm** | while |
| *\*el-i-s* | ELIS | el | **el** | is |
| *\*tolm-o-s* | TOLMOS | tolm | **tolm** | stone |
| *\*tolm-o-s* | TOLMOS | tolm | **tolm** | stone |
| *\*ston-o-s* | STONOS | ston | **Ston.** | it stands |

None of the Stonwryt's words met a law between the first tongue and the Hal. **The vow under the tale-stone is cut in the first tongue itself, word for word**: it is the oldest sentence anyone can still see. The Rivenmen cannot sound it, and the Mystaeri would not know one word of it.

**(d) The Guest's three words.**

*What he said, in the shore's tongue: Hess… Helv… Sennyl…*

| First tongue | Hal | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*hess-i-s* | HESSIS | hess | **Hess…** | stop |
| *\*half-i-s* | HELVIS | helv | **Helv…** | the upper air, sky |
| *\*senn-i-s* | SENNIS | senn | **Sennyl…** | go down: die (+ -Ol, dying) |

*What his own tongue says for the same, and the word at the end of the gift's sentence*

| First tongue | Eldest | living | as the line says it | gloss |
|---|---|---|---|---|
| *\*kul-i* | keile | rheil | **rheil** | stop (O kyl, change) |
| *\*molt-o* | naele | nael | **nael** | sky, breath (O molt, heart) |
| *\*feʔs-i* | vease | veas | **vease** | die (O vess, night) |
| *\*senn-i* | senne | senn | **senn** | beneath (O senn, die) |

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

## 3 · THE ROOTS (624)

### 3.1 How to read the tables

- **253 inherited roots** (§3.2) are the roots behind every existing word of both tongues, together with their small words, affixes and names.
- **371 reserve roots** (§3.3) are first-tongue words that neither living tongue has used yet. Each gives its regular reflex in both tongues, ready for the tier-3 translation of the whole Book (note 5): stone leaves in Orrowen, wood leaves in the grain's soft readings.
- **Columns.**
  - *Orrowen*: the living form, with the Hal form after it.
  - *Seilrhass*: the living form, with the Eldest-speech form after it.
  - Where a tongue did not keep the root, the cell gives the form it *would* have, in italics after "would be". It says "falls together with" where that form is already another word, and "a lift" where the form is on the originality blacklist and must not be used.
- **★** marks a root that both tongues kept: a cognate set (§1.5).
- The reserve roots were drawn from the first tongue's own sound pattern (seeded, so the list can be re-made exactly). Each was then screened: no clash with any existing word, no form on the originality blacklist, and no form, in either tongue, that is an English word (the whole system dictionary of about 236,000 words). The Orrowen form is always unique. A Seilrhass form is shared by at most two roots, of different fields, as a tongue of seven consonants must share some.

### 3.2 The inherited roots

**Stone, wood and building** (22)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| ★ *\*tol- / tal-* | rise, stand up tall; (o-grade) a standing thing, a stone set up or a trunk | **tolm** 'a stone' (Hal *tolmos*) · **tald** 'rise, stand up (v.)' (Hal *taldos*) · **taldow** 'a tower, a high place' (Hal *taldū*) | **thael** 'a tree' (Eldest *taele*) · **thal** 'the neck, where life goes up into thought' (Eldest *tale*) |
| *\*xal-* | the living rock, what lies under everything | **hal** 'bedrock, the living rock of the ridge' (Hal *xalos*) · **hald** 'a wall ('rock made to stand')' (Hal *xaldos*) | *would be* rhal |
| *\*loð-* | set in a wet bed; bind (as mortar binds) | **lodh** 'mortar' (Hal *lodhos*) | *would be* laeth: a lift (on the blacklist), not usable |
| ★ *\*trenn-* | a running line: a course of stones, a line of writing, a stream | **trenn** 'a course of stones' (Hal *trennos*) | **thenn** 'water' (Eldest *tenne*) |
| *\*kað-* | set down in its place, lay | **cadh** 'lay (a stone, a course, a tale)' (Hal *cadhos*) | *would be* rhath |
| ★ *\*ston-* | stand firm, hold one's place; the standing core of a thing | **ston** 'stand (of a wall), make stand, hold firm' (Hal *stonos*) | **saen** 'heartwood' (Eldest *saene*) |
| *\*gal-* | set up, raise; (of a thing) stand made, be | **gald** 'build, raise a work' (Hal *galdos*) · **gal** '(old) was: the suppletive past of doss, re yal-' (Hal *galos*) | *would be* rhal |
| *\*klenn-* | fresh, not yet worn | **clenn** 'new' (Hal *clennis*) | *would be* lenn: falls together with lenn 'white' |
| *\*stann-* | cut out of its bed | **stann** 'quarry, cut stone from the bed' (Hal *stannos*) · **Stannard** 'quarrier' (Hal *stannardos*) | *would be* sann |
| *\*brask-* | a biting edge | **bresk** 'a chisel' (Hal *breskis*) | *would be* rass |
| *\*drunn-* | a heavy blow | **drunn** 'a mallet, a hammer' (Hal *drunnos*) | *would be* thinn |
| *\*gann-* | a post, an upright; (dual) the two posts | **gann** 'a post, an upright' (Hal *gannos*) · **ganna** 'a gate ('the two posts')' (Hal *gannā*) | *would be* rhann: falls together with rhann 'heavy, great' |
| *\*hosk-* | a stone laid across; to cap | **hosk** 'a lintel' (Hal *hoskos*) | *would be* aess |
| *\*gorn-* | a turn of a wall, a corner | **gorn** 'a corner, a quoin' (Hal *gornos*) | *would be* rhear |
| *\*keθ-* | hold in the hand, keep | **keth** 'hold, keep' (Hal *kethis*) · **kethow** 'a keep, a hold' (Hal *kethū*) | *would be* rheth |
| ★ *\*trosk-* | split, cleave; a split | **tresk** 'a cleft, a split' (Hal *treskis*) | **thaess** 'to split' (Eldest *taesse*) |
| *\*last-* | a roofed room | **lest** 'a house' (Hal *lestis*) | *would be* las: a lift (on the blacklist), not usable |
| *\*kumm-* | a sheltered hollow | **cumm** 'a haven: any walled place of shelter' (Hal *cummos*) | *would be* rhinn |
| *\*stell-* | a heap of stones | **stell** 'a cairn' (Hal *stellis*) | *would be* sel |
| *\*pell-* | a tall point | **pell** 'a spire, a tall point' (Hal *pellis*) · **Pellow** 'of the spire' (Hal *pellū*) | *would be* vel |
| *\*wrut-* | cut into; a cut made to last | **ryt** 'a cut vow, an oath' (Hal *wrytis*) | *would be* reith |
| *\*prass-* | one who knows the work through | **prass** 'a master of the craft' (Hal *prassos*) | *would be* rass |

**Faith, bond and kin** (25)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*hemm-* | old, of many years | **hemm** 'old' (Hal *hemmos*) · **hemma** 'Elderess' (Hal *hemmā*) | *would be* enn: falls together with enn 'within, inside' |
| *\*marð-* | the Maker; the one who is knelt to | **mardh** 'God (used of nothing else)' (Hal *mardhos*) | *would be* nar: a lift (on the blacklist), not usable |
| *\*amm-* | lift the voice to one above: to call upon, to teach | **ammel** 'pray' (Hal *ammelis*) · **ammad** 'teach' (Hal *ammados*) | *would be* ann |
| ★ *\*taw-* | sprout, grow | **tev** 'a child' (Hal *tevis*) | **thae** 'tide' (Eldest *taee*) |
| *\*woll-* | a calling, a name | **voll** 'a name' (Hal *vollos*) | *would be* vael: falls together with vael 'grain' |
| ★ *\*tann- / tunn-* | shut in; (u-grade) shut round, whole | **tunn** 'whole, complete' (Hal *tunnos*) | **thann** 'to close' (Eldest *tanne*) |
| ★ *\*grest-* | a burning smart, a hurt | **grest** 'harm, hurt' (Hal *grestos*) | **rhes** 'anger' (Eldest *kese*) |
| ★ *\*par-* | bear up, hold up; keep safe | **par** 'guard, protect' (Hal *paros*) · **pard** 'a warden, a keeper' (Hal *pardos*) · **Halvard** 'bedrock-warden' (Hal *xalpardos*) | **var** 'to bear, to carry' (Eldest *var*) · **varen** 'a bearer' (Eldest *varene*) |
| ★ *\*oð-* | the rim where one stops and gathers: the fireside, the waterside | **odh** 'a hearth' (Hal *odhos*) · **odha** 'a mother ('she of the hearth')' (Hal *odhā*) | **aeth** 'a shore' (Eldest *aethe*) |
| *\*θald-* | those of one hearth | **theld** 'a family, a household' (Hal *theldis*) | *would be* thal: falls together with thal 'the neck, where life goes up…' |
| ★ *\*waʔr-* | stillness; a still place | **varn** 'home' (Hal *varnos*) | **vaere** 'still water' (Eldest *vaere*) |
| *\*gað-* | a father | **gedh** 'a father' (Hal *gedhis*) | *would be* rhath |
| *\*uld-* | grown | **uld** 'a man' (Hal *uldos*) | *would be* il |
| *\*ess-* | a woman | **essa** 'a woman' (Hal *essā*) | *would be* essae |
| *\*lunt-* | those of one speech | **lunt** 'a people, a nation' (Hal *luntos*) | *would be* linth |
| *\*orr-* | go along; the edge one goes along | **orr** 'go, walk' (Hal *orros*) · **orrow** 'the Shore' (Hal *orrū*) | *would be* ear |
| *\*arr-aʔ* | (dual) the two at a threshold, the guest and the host | **arra** 'a guest' (Hal *arrā*) | *would be* arae |
| *\*gebb-* | a leaf that swings; a door | **gebb** 'a door' (Hal *gebbis*) | *would be* rhe: falls together with rhe 'they (mute)' |
| *\*lumm-* | bow down | **lumm** 'kneel' (Hal *lummos*) | *would be* linn: a lift (on the blacklist), not usable |
| ★ *\*waʔl-* | the inward bent of a thing: its grain, what it leans to | **vall** 'love' (Hal *vallos*) | **vael** 'grain' (Eldest *vaele*) |
| *\*osk-* | rest one's weight on | **osk** 'trust (v. and n.)' (Hal *oskos*) | *would be* aess |
| *\*tesk-* | a layer, a laying-down | **tesk** 'a generation' (Hal *teskis*) | *would be* thess: a lift (on the blacklist), not usable |
| *\*swe- / swo-* | one's own; one alone, single | **sost** 'self, very' (Hal *sostos*) · **Seren** 'a single sorrow that overcomes' (Hal *sereŋos*) | *would be* se: falls together with se 'you (more than one)' |
| *\*reŋ-* | a sorrow that is carried and does not break the one who carries it; a grief that overcomes | *would be* ren (Hal *reŋos*) | *would be* ren: a lift (on the blacklist), not usable |
| *\*gweθ-* | a way in | *would be* weth (Hal *wethos*) | **veth** 'door' (Eldest *vethe*) |

**The wall, the war, the sea-road** (19)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| ★ *\*krenn- / krann-* | weighty; the one who bears the weight, the head | **crenn** 'a captain' (Hal *crennos*) | **rhann** 'heavy, great' (Eldest *kanne*) |
| *\*hesp-* | a long blade | **hesp** 'a sword' (Hal *hespis*) | *would be* es: falls together with es '-es, the past of a verb…' |
| *\*kest-* | a band that goes together | **kest** 'a company of soldiers' (Hal *kestis*) | *would be* rhes: falls together with rhes 'anger' |
| *\*bramm-* | a roar; to roar | **bramm** 'a gun ('the roarer')' (Hal *brammos*) | *would be* rann |
| *\*hask-* | run | **hask** 'run' (Hal *haskos*) | *would be* ass |
| *\*gomm-* | a horn | **gomm** 'a horn' (Hal *gommos*) | *would be* rhaenn |
| *\*karm-* | cry out | **carm** 'a call, a cry' (Hal *carmos*) | *would be* rhar |
| *\*peð-* | a thing thrown | **pedh** 'a shot: what a gun throws' (Hal *pedhis*) | *would be* veth: falls together with veth 'door' |
| *\*trun-* | the ground under one | **trun** 'ground' (Hal *trunos*) | *would be* thein: falls together with thein 'to hold' |
| *\*marr-* | shift over | **marr** 'shift, move to another place' (Hal *marros*) | *would be* nar: a lift (on the blacklist), not usable |
| ★ *\*kul-* | leave off; turn from one thing | **kyl** 'change' (Hal *kylis*) | **rheil** 'to stop, to cease' (Eldest *keile*) |
| *\*lusk-* | let go | **lusk** 'loose, let go, set free' (Hal *luskos*) | *would be* liss |
| *\*bosk-* | fall upon | **bosk** 'attack' (Hal *boskos*) | *would be* vaess |
| *\*hurr-* | strike down | **hurr** 'kill' (Hal *hurros*) | *would be* ir: a lift (on the blacklist), not usable |
| *\*gorr-* | fight | **gorr** 'fight' (Hal *gorros*) | *would be* rhear |
| *\*koff-* | a wrap | **covv** 'a cloak' (Hal *covvos*) | *would be* rhae: a lift (on the blacklist), not usable |
| ★ *\*skeθ-* | hew, cut into wood | **sceth** 'a ship, a hull (a trunk hewn out)' (Hal *scethis*) | **seth** 'a carving' (Eldest *sethe*) |
| *\*gwemm-* | a cloth that fills | **wemm** 'a sail' (Hal *wemmis*) | *would be* venn |
| *\*kriθθ-* | a hard cutting edge; (later) iron, the axe | *would be* crith (Hal *crithis*) | **rhith** 'iron' (Eldest *kithe*) |

**Sea, land and growing things** (25)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*gwað-* | the great water | **wadh** 'the sea' (Hal *wadhos*) | *would be* vath: falls together with vath 'bark' |
| ★ *\*mus-* | the dim light; fog-light | **myst** 'sea-fog' (Hal *mystis*) | **neis** 'soft light' (Eldest *neise*) |
| *\*mosk-* | a tree and its wood | **mesk** 'a tree' (Hal *meskis*) | *would be* naess |
| *\*lurr-* | thick-grown | **lurr** 'a forest' (Hal *lurros*) | *would be* lir: a lift (on the blacklist), not usable |
| *\*hull-* | a swelling of water | **hyll** 'a tide' (Hal *hyllis*) | *would be* il |
| *\*xrull-* | a rushing water | **rhull** 'a river' (Hal *hrullos*) | *would be* rhil |
| *\*seð-* | soft wet ground | **sedh** 'a fen' (Hal *sedhis*) | *would be* seth: falls together with seth 'a carving' |
| *\*nall-* | a small land in water | **nell** 'an islet' (Hal *nellis*) | *would be* nal: falls together with nal 'four' |
| *\*taf-* | come to land | **tav** 'come ashore, land a boat' (Hal *tavos*) · **tavow** 'a harbour, a landing' (Hal *tavū*) | *would be* tha |
| *\*sorθ-* | a back of land | **sorth** 'a ridge' (Hal *sorthos*) | *would be* sear |
| *\*brunn-* | a great height of land | **brunn** 'a mountain' (Hal *brunnos*) | *would be* rinn: a lift (on the blacklist), not usable |
| *\*grull-* | grit | **grull** 'sand' (Hal *grullos*) | *would be* rhil |
| *\*sirr-* | a clear hard thing | **sirr** 'glass' (Hal *sirris*) | *would be* sir: a lift (on the blacklist), not usable |
| *\*krest-* | hard water, ice | **crest** 'ice' (Hal *crestis*) | *would be* rhes: falls together with rhes 'anger' |
| *\*lew-* | green, fresh | *would be* lev (Hal *levis*) | **lea** 'green, young' (Eldest *leae*) |
| *\*ral-* | a root | *would be* ral (Hal *ralos*) | **ral** 'a root' (Eldest *rale*) |
| *\*waθ-* | an outer skin | *would be* vath (Hal *vathos*) | **vath** 'bark' (Eldest *vathe*) |
| *\*ross-* | a slow inner flowing | *would be* ress (Hal *ressis*) | **raess** 'sap' (Eldest *raesse*) |
| *\*il-* | a round, a going-round | *would be* il (Hal *ilos*) | **eil** 'a growth ring' (Eldest *eile*) |
| *\*wur-* | living wood | *would be* vyr (Hal *vyris*) | **veir** 'wood, the living stuff' (Eldest *veire*) |
| *\*wus-* | a seed | *would be* vys (Hal *vysis*) | **veis** 'seed' (Eldest *veise*) |
| *\*sul-* | a bough; to bend | *would be* syl (Hal *sylis*) | **seil** 'bough, branch' (Eldest *seile*) |
| *\*reθ-* | the earth underfoot | *would be* reth (Hal *rethos*) | **reth** 'ground, earth' (Eldest *rethe*) |
| *\*enθ-* | a rim, an edge | *would be* enth (Hal *enthos*) | **enth** 'edge, rim, margin' (Eldest *enthe*) |
| *\*gwes-* | a way | *would be* wes (Hal *wesos*) | **ves** 'a road' (Eldest *vese*) |

**Sky, weather, fire and time** (15)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*half-* | the upper air | **helv** 'the sky, the upper air' (Hal *helvis*) | *would be* al |
| ★ *\*xwre-* | rime, frost | **frenn** 'frost, rime' (Hal *hwrennos*) | **rhel** 'frost' (Eldest *kele*) |
| *\*sulf-* | snow | **sulv** 'snow' (Hal *sulvos*) | *would be* sil: a lift (on the blacklist), not usable |
| *\*grem-* | the hard season | **grem** 'winter' (Hal *gremis*) | *would be* rhen: falls together with rhen 'stone, the mute thing' |
| *\*forr-* | fire | **vorr** 'fire' (Hal *vorros*) | *would be* vear |
| *\*orl-* | the light of one day | **orl** 'a day' (Hal *orlos*) | *would be* ear |
| ★ *\*feʔ-* | fade, go dark | **vess** 'a night' (Hal *vessis*) | **veas** 'to die' (Eldest *vease*) · **veath** 'night' (Eldest *veathe*) |
| *\*klem-* | a stroke of time | **clem** 'an hour' (Hal *clemis*) | *would be* len |
| *\*surr-* | a turn of the seasons | **surr** 'a year' (Hal *surros*) | *would be* sir: a lift (on the blacklist), not usable |
| *\*kamm-* | come together | **cemm** 'meet' (Hal *cemmis*) | *would be* rhann: falls together with rhann 'heavy, great' |
| *\*esθ-* | burn | *would be* esth (Hal *esthos*) | **esth** 'fire' (Eldest *esthe*) · **Esthaer** 'that of fire' (Eldest *esthaer*) |
| *\*kris-* | a hard glint | *would be* cris (Hal *crisis*) | **rheis** 'hard light' (Eldest *keise*) |
| *\*lis-* | what comes next | *would be* lis (Hal *lisis*) | **leis** 'the morrow' (Eldest *leise*) |
| *\*reʔs-* | moving air | *would be* ress (Hal *ressos*) | **reas** 'wind' (Eldest *rease*) |
| *\*niθθ-* | falling water | *would be* nith (Hal *nithis*) | **nith** 'rain' (Eldest *nithe*) |

**Body, life and feeling** (15)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*garl-* | a hand | **garl** 'a hand' (Hal *garlos*) | *would be* rhar |
| ★ *\*molt-* | the breath within; the living middle | **molt** 'a heart' (Hal *moltos*) | **nael** 'mist' (Eldest *naele*) |
| *\*hoss-* | breath going out | **hoss** 'breath' (Hal *hossos*) | *would be* aess |
| *\*lorr-* | red blood | **lorr** 'blood' (Hal *lorros*) | *would be* lear |
| ★ *\*senn-* | down, below; go down (as a fire in peace, as the sun) | **senn** 'die: go out, as a fire in peace' (Hal *sennis*) | **senn** 'beneath, under' (Eldest *senne*) |
| *\*hess-* | halt, stay | **hess** 'stop' (Hal *hessis*) | *would be* ess: a lift (on the blacklist), not usable |
| *\*lomm-* | the weight of a loss | **lomm** 'grief' (Hal *lommos*) | *would be* laenn |
| *\*sol- / soʔl-* | lie still; (catch-grade) the deep rest | **sol** 'rest, lie still' (Hal *solos*) · **sollan** 'peace ('the rest after the work')' (Hal *sollanos*) | *would be* sael: a lift (on the blacklist), not usable |
| *\*lunn-* | an open space, room to move | **lunn** 'freedom' (Hal *lunnos*) | *would be* linn: a lift (on the blacklist), not usable |
| *\*θar-* | blood | *would be* thar (Hal *tharos*) | **thar** 'blood' (Eldest *thare*) |
| *\*lann-* | an arm | *would be* lann (Hal *lannos*) | **lann** 'arm' (Eldest *lanne*) |
| *\*lin-* | the brow | *would be* lin (Hal *linos*) | **lein** 'brow, forehead' (Eldest *leine*) |
| *\*neʔs-* | the eye; to look | *would be* ness (Hal *nessos*) | **neas** 'eye' (Eldest *nease*) |
| *\*enn-* | within; the one from within | *would be* enn (Hal *ennos*) | **enn** 'within, inside' (Eldest *enne*) · **enna** 'a child' (Eldest *enna*) |
| *\*saθ-* | the back | *would be* sath (Hal *sathos*) | **sath** 'back, stern' (Eldest *sathe*) |

**Speech, writing and mind** (14)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| ★ *\*tum-* | hold, keep (in the hand and in the mind) | **tum** 'remember' (Hal *tumos*) · **tumol** 'remembering' (Hal *tumola*) | **thein** 'to hold' (Eldest *teine*) |
| ★ *\*bro- / bra- / bre-* | utter | **brod** 'a word' (Hal *brodos*) · **brodh** 'put into words, tell, speak' (Hal *brodhos*) · **Brenn** 'Brenn: a name. Names are names' (Hal *brennos*) | **ranth** 'a word (a spoken thing, which can break)' (Eldest *ranthe*) · **renn** 'a mouth' (Eldest *renne*) |
| *\*wesk-* | look at closely | **vesk** 'see' (Hal *veskis*) | *would be* vess: a lift (on the blacklist), not usable |
| ★ *\*xwle-* | a thin sheet: a leaf | **flenn** 'a leaf of a book or of slate' (Hal *hwlennā*) | **lel** 'a leaf' (Eldest *lele*) |
| *\*luθ-* | a dark wetness | **luth** 'ink' (Hal *luthos*) | *would be* leith: a lift (on the blacklist), not usable |
| *\*branθ-* | an ember | **brenth** 'coal' (Hal *brenthis*) | *would be* ranth: falls together with ranth 'a word (a spoken thing…)' |
| *\*fell-* | a song | **vell** 'a song' (Hal *vellis*) | *would be* vel |
| *\*sesk-* | know (a thing that is so) | **sesk** 'know a fact' (Hal *seskis*) | *would be* sess |
| *\*nuð-* | count | **nydh** 'count' (Hal *nydhis*) | *would be* neith |
| *\*kail-* | a notch cut to keep a count | **kael** 'a tally-notch' (Hal *kēlos*) | *would be* rhael |
| *\*pess-* | ask | **pess** 'ask' (Hal *pessis*) | *would be* vess: a lift (on the blacklist), not usable |
| *\*tess-* | give back an answer; stand for | **tess** 'answer' (Hal *tessis*) · **tessen** 'we two answer (1du)' (Hal *tessana*) | *would be* thess: a lift (on the blacklist), not usable |
| *\*nir-* | sing | *would be* nir (Hal *nira*) | **neira** 'to sing' (Eldest *neira*) |
| *\*is-* | a name, a calling-out | *would be* is (Hal *isos*) | **eis** 'name' (Eldest *eise*) |

**Other acts** (24)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*doss-* | be (in a place, in a state) | **doss** 'be (state, place)' (Hal *dossos*) | *would be* thaess: falls together with thaess 'to split' |
| *\*el- / egw-* | be such; (egw-) was | **el** 'is (the copula)' (Hal *elis*) · **ew** 'was' (Hal *ewas*) | *would be* el: a lift (on the blacklist), not usable |
| *\*darr-* | come near | **darr** 'come' (Hal *darros*) | *would be* thar: falls together with thar 'blood' |
| *\*hunn-* | hear | **hunn** 'hear' (Hal *hunnos*) | *would be* inn |
| *\*habb-* | hold out, give | **hebb** 'give' (Hal *hebbis*) | *would be* a |
| *\*toff-* | stay where one is | **tovv** 'wait' (Hal *tovvos*) | *would be* thae: falls together with thae 'tide' |
| *\*omm-* | drop | **omm** 'fall' (Hal *ommos*) | *would be* aenn: falls together with aenn 'open' |
| ★ *\*krask-* | crack, break | **cresk** 'break' (Hal *creskis*) | **rhass** 'storm' (Eldest *kasse*) |
| *\*ser-* | go on, carry forward | **ser** 'go on, carry forward' (Hal *seris*) | *would be* ser |
| ★ *\*xreun-* | set hard, harden; the hard thing | **rhyn** 'set fast (of mortar), take hold' (Hal *hriunis*) · **Rhyna** 'she who sets fast' (Hal *hriunā*) | **rhen** 'stone, the mute thing' (Eldest *kene*) |
| *\*ress-* | go soft, rot | *would be* ress (Hal *ressis*) | **ress** 'rot, the soft death of wood' (Eldest *resse*) |
| *\*lanθ- / lenθ-* | hold one's place, wait; (e-grade) the season of waiting | *would be* lenth (Hal *lenthis*) | **lanth** 'a knot in the grain' (Eldest *lanthe*) · **lenth** 'winter' (Eldest *lenthe*) |
| *\*onn-* | a gap, the between | *would be* onn (Hal *onnos*) | **aenn** 'open' (Eldest *aenne*) |
| *\*griss-* | seize | *would be* griss (Hal *grissis*) | **rhiss** 'to take, to seize' (Eldest *kisse*) |
| *\*roθ-* | fold the knee | *would be* reth (Hal *rethis*) | **raeth** 'to kneel' (Eldest *raethe*) |
| *\*iʔl-* | breathe, live | *would be* illa (Hal *illā*) | **ilae** 'to live' (Eldest *ilae*) · **ilen** 'to lean, to incline toward…' (Eldest *ilene*) |
| *\*nenn-* | sink | *would be* nenn (Hal *nennos*) | **nenn** 'to fall, to sink' (Eldest *nenne*) |
| *\*soʔ* | come | *would be* su (Hal *sō*) | **sae** 'to come' (Eldest *sae*) |
| *\*neθ-* | turn aside | *would be* neth (Hal *nethis*) | **neth** 'to turn, to turn aside' (Eldest *nethe*) |
| *\*tass-* | strike | *would be* tass (Hal *tassos*) | **thass** 'to strike' (Eldest *tasse*) |
| *\*seinn-* | listen, heed | *would be* senn: falls together with senn 'die: go out, as a fire in…' | **seinn** 'to hear' (Eldest *seinne*) |
| *\*tafall-* | go after | *would be* tavall (Hal *tavallos*) | **thaval** 'to hunt, to go for' (Eldest *tavale*) |
| *\*soss-* | hunger | *would be* sess (Hal *sessis*) | **saess** 'hunger' (Eldest *saesse*) |
| *\*senθ-* | dread | *would be* senth (Hal *senthos*) | **senth** 'dread, fear' (Eldest *senthe*) |

**Qualities** (16)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*strom-* | wide, great | **strom** 'great' (Hal *stromos*) | *would be* saen: falls together with saen 'heartwood' |
| *\*luss-* | small | **lyss** 'small' (Hal *lyssis*) | *would be* liss |
| *\*gell-* | fitting, good | **gell** 'good' (Hal *gellis*) | *would be* rhel: falls together with rhel 'frost' |
| ★ *\*weinn-* | sound, whole, true (as a plumb wall) | **venn** 'true' (Hal *vennis*) | **veinn** 'to mend, to make whole' (Eldest *veinne*) |
| *\*gunn-* | deep | **gunn** 'deep' (Hal *gunnos*) | *would be* rhinn |
| *\*sell-* | long | **sell** 'long' (Hal *sellis*) | *would be* sel |
| *\*domm-* | black | **domm** 'black' (Hal *dommos*) | *would be* thaenn |
| *\*bell-* | golden | **bell** 'gold, golden' (Hal *bellis*) | *would be* vel |
| ★ *\*lenn-* | pale-bright | **lenn** 'silver' (Hal *lennis*) | **lenn** 'white' (Eldest *lenne*) |
| *\*ir-* | far down, far back | *would be* ir (Hal *iris*) | **eir** 'deep' (Eldest *eire*) |
| *\*niw-* | the gleam of a still surface | *would be* niv (Hal *nivis*) | **nei** 'silver' (Eldest *neie*) |
| *\*afen-* | the other | *would be* aven (Hal *avenos*) | **aven** 'other' (Eldest *avene*) |
| *\*iθ-* | hollow, a seeming | *would be* ith (Hal *ithos*) | **eith** 'hollow, empty' (Eldest *eithe*) |
| *\*iss-* | thin | *would be* iss (Hal *issos*) | **iss** 'thin, slight' (Eldest *isse*) |
| *\*leʔs-* | swift | *would be* less (Hal *lessos*) | **leas** 'swift' (Eldest *lease*) |
| *\*eiss-* | so, as it is | *would be* ess (Hal *essos*) | **eiss** 'so' (Eldest *eisse*) |

**Numbers** (15)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*hos-* | one | **hos** 'one' (Hal *hosos*) | *would be* aes: a lift (on the blacklist), not usable |
| ★ *\*pa-* | two | **pa** 'two (+S)' (Hal *pā*) · **pana** 'both' (Hal *panā*) | **vann** 'two' (Eldest *vanne*) |
| ★ *\*ros-* | three | **rost** 'nine ('thrice three')' (Hal *rostos*) | **raes** 'three' (Eldest *raese*) |
| *\*sull-* | a set of three | **sull** 'three' (Hal *sullos*) | *would be* sil: a lift (on the blacklist), not usable |
| *\*gemm-* | four | **gemm** 'four' (Hal *gemmis*) | *would be* rhenn |
| *\*nal-* | the four fingers, a hand without its thumb | *would be* nal (Hal *nalos*) | **nal** 'four' (Eldest *nale*) |
| *\*lesk-* | five | **lesk** 'five' (Hal *leskis*) | *would be* less |
| *\*wind-* | the whole hand | *would be* vind (Hal *vindos*) | **vinn** 'hand' (Eldest *vinne*) |
| *\*fran-* | six | **vran** 'six' (Hal *vranos*) | *would be* ran |
| *\*ðom-* | seven | **dhom** 'seven' (Hal *dhomos*) | *would be* thaen |
| *\*θell-* | eight | **thell** 'eight' (Hal *thellis*) | *would be* thel: a lift (on the blacklist), not usable |
| *\*noθ-* | ten | **noth** 'ten' (Hal *nothos*) | *would be* naeth: a lift (on the blacklist), not usable |
| *\*delf-* | a full course | **delv** 'twelve' (Hal *delvis*) | *would be* thel: a lift (on the blacklist), not usable |
| *\*murr-* | a score | **murr** 'twenty' (Hal *murros*) | *would be* nir |
| *\*bost-* | a great heap | **bost** 'four hundred' (Hal *bostos*) | *would be* vaes |

**Small words** (42)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| ★ *\*et- / itt-* | this very one, the same | **et** 'the (the article)' (Hal *etas*) | **ith** 'one' (Eldest *ite*) |
| *\*ul-* | in, within | **ul** 'in (+N)' (Hal *ulan*) | *would be* ul |
| ★ *\*xui* | out of, from | **hy** 'from, out of (+S)' (Hal *hya*) | **rhi** 'from, out of' (Eldest *ki*) |
| *\*um-* | upon | **um** 'upon, on (+S)' (Hal *umo*) | *would be* un |
| ★ *\*lo- / li-* | at, by | **lo** 'at, by, with (+S)' (Hal *loa*) | **li** 'in, at, on (place)' (Eldest *li*) |
| *\*dem-* | up to, as far as | **dem** 'until, as far as (+N)' (Hal *demen*) | *would be* then |
| *\*eθ-* | and, also | **eth** 'and' (Hal *ethas*) | *would be* eth |
| *\*ell-* | or, else | **ell** 'or' (Hal *ello*) | *would be* el: a lift (on the blacklist), not usable |
| *\*weθ-* | on the other side, rather | **veth** 'but, rather' (Hal *vetho*) | *would be* veth: falls together with veth 'door' |
| ★ *\*na- / ni* | not | **na** 'un- (prefix, +S)' · **nath** 'not (before a verb, +N)' (Hal *nathan*) | **ni** 'not (before the verb)' (Eldest *ni*) |
| ★ *\*re* | yonder, that; then, at that time | **re** 'past particle (+S)' | **re** 'that' (Eldest *re*) · **reil** 'fore, front' (Eldest *reil*) |
| ★ *\*es* | at another time, not now | **es** 'future particle (+N)' (Hal *esan*) | **es** '-es, the past of a verb (a particle fused after…)' (Eldest *es*) |
| *\*ho-* | is it? | **ho** 'question particle (+S)' (Hal *hoa*) | *would be* o |
| ★ *\*sa / se* | that one, the one by you | **sa** 'who, which, that (relative, +S)' (Hal *sae*) | **sa** 'you (one)' (Eldest *sa*) · **se** 'you (more than one)' (Eldest *se*) |
| *\*soŋ-* | the length of a thing | **somm** 'while, as long as' (Hal *soŋmas*) | *would be* son |
| ★ *\*aŋ-* | at the hour | **amm** 'when (conj.)' (Hal *aŋma*) | **anth** 'an hour' (Eldest *anthe*) |
| *\*ka-, wo- + -ð-* | which one? (ka- of a person, wo- of a thing, with the asking suffix \*-ð-) | **cedh** 'who?' (Hal *cedhi*) · **vodh** 'what?' (Hal *vodho*) | *would be* rhath |
| *\*siu* | this, here | **sy** 'this (after the noun)' (Hal *siu*) | *would be* si: falls together with si 'with' |
| *\*ull-* | that, there | **ull** 'that (after the noun)' (Hal *ullo*) | *would be* ul |
| *\*gor-* | all, each one | **gor** 'every, all (+S)' (Hal *gora*) | *would be* rhor |
| *\*tul-* | still, as yet | **tul** 'yet, still' (Hal *tulo*) | *would be* thul |
| *\*dask-* | the last of a thing | **dask** 'the end' (Hal *daskos*) | *would be* thass: falls together with thass 'to strike' |
| *\*en-* | I, this one here | **en** 'I' (Hal *enan*) | *would be* en |
| *\*θo-* | you (one) | **tho** 'you' (Hal *thoe*) | *would be* tho |
| *\*o-* | he, it | **o** 'he, it' (Hal *oa*) | *would be* o |
| *\*ey-* | she | **ey** 'she' (Hal *eyas*) | *would be* e |
| ★ *\*ol* | together, one with another; we (all) | **ol** 'we' (Hal *olon*) · **olna** 'we two (+S)' (Hal *olnā*) | **ael** 'bond, joining' (Eldest *ael*) |
| *\*wa-* | you (many) | **va** 'you' (Hal *van*) | *would be* va: falls together with va 'I' |
| *\*so-* | they | **so** 'they' (Hal *soa*) · **sona** 'they two (+S)' (Hal *sonā*) | *would be* so |
| *\*ba / be* | I / we (the speaker's side) | *would be* ba (Hal *ba*) | **va** 'I' (Eldest *va*) · **ve** 'we' (Eldest *ve*) |
| *\*la / le* | he, she (a living thing) / they | *would be* la (Hal *la*) | **la** 'he, she' (Eldest *la*) · **le** 'they (living)' (Eldest *le*) |
| *\*xa / xe* | it (a thing that does not answer) / they | *would be* ha (Hal *xa*) | **rha** 'it (a mute thing: stone, iron, the dead)' (Eldest *ka*) · **rhe** 'they (mute)' (Eldest *ke*) |
| *\*ra* | this, the one in hand | *would be* ra (Hal *ra*) | **ra** 'this' (Eldest *ra*) |
| *\*ŋa* | toward | *would be* na: falls together with na 'un- (prefix, +S)' | **na** 'to, toward' (Eldest *na*) |
| *\*ti* | through, past | *would be* ti (Hal *ti*) | **thi** 'through, past, by way of' (Eldest *ti*) |
| *\*loʔs* | above | *would be* loss (Hal *loss*) | **laes** 'above, over' (Eldest *laes*) |
| *\*si* | with; given that | *would be* si (Hal *si*) | **si** 'with' (Eldest *si*) · **sei** 'if (closes a clause)' (Eldest *sei*) |
| *\*ri* | go toward; against | *would be* ri (Hal *ri*) | **ri** 'against, upon' (Eldest *ri*) · **rei** 'to go' (Eldest *rei*) |
| *\*wi* | give; for (the sake of) | *would be* vi (Hal *vi*) | **vi** 'for, for the sake of' (Eldest *vi*) · **vei** 'to give' (Eldest *vei*) |
| *\*ei* | and, and also | *would be* ae (Hal *ē*) | **ei** 'and' (Eldest *ei*) |
| *\*tes-* | after that | *would be* tes (Hal *tes*) | **thes** 'then, after that' (Eldest *tes*) |
| *\*loʔ* | is it so? ask | *would be* lu (Hal *lō*) | **lae** '(closes a question)' (Eldest *lae*) |

**Affixes** (20)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| *\*-aθi* | many (the plural) | **-ath** 'plural -Ath' (Hal *-athi*) | — |
| *\*-ol-a* | the doing (a verbal noun) | **-ol** 'verbal noun -Ol' (Hal *-ola*) | — |
| *\*-at* | done, made | **-at** 'participle -At' | — |
| *\*-ard* | one who does | **-ard** 'agent -Ard' | — |
| *\*-oθ* | the quality of | **-oth** 'abstract -Oth' | — |
| *\*-el* | one, a small one | **-el** 'singulative' | — |
| *\*-an* | the folk of | **-an** 'collective 'the folk of'' | — |
| *\*-en* | belonging to; (as a noun) those belonging | **-en** 'of, belonging to' | **-en** 'plural' (Eldest *-en*) |
| *\*-uʔ* | at, the place of | **-ow** 'place of -ow' (Hal *-ū*) | — |
| *\*-ast* | the n-th | **-ast** 'ordinal -Ast' | — |
| *\*-aʔ* | the pair; she | **-a** 'the old dual' (Hal *-ā*) | — |
| *\*-naʔ* | the two of | **-na** 'dual of a pronoun' (Hal *-nā*) | — |
| *\*-eʔ* | one of, one who | — | **-ea** 'one of' (Eldest *-ea*) |
| *\*-aʔr* | all of a kind, those of | — | **-ear** 'those of (a whole people or kind)' (Eldest *-aer*) · **-aer** 'the relic, kept in Esthaer and borrowed in…' (Eldest *-aer*) |
| *\*-as* | the doing, the thing done | — | **-as** 'verbal noun' (Eldest *-as*) |
| *\*-eθ* | make (one) do | — | **-eth** 'causative' (Eldest *-eth*) |
| *\*e* | now, here (a particle) | — | **-e** 'verb: it does, it is doing (fused late)' (Eldest *-e*) |
| *\*ar* | toward (a goal) | — | **-ar** 'verb: it shall, it is meant to (fused late)' (Eldest *-ar*) |
| *\*-ane* | one who bears or does (old) | — | **-en** 'the old agent, merged with the plural' (Eldest *-ene*) |
| *\*-om, -ith, -os, -ana, -aʔ, -ar, -us, -ant* | the person endings of the verb | **-om** '1sg -Om' · **-ith** '2sg -ith' · **-an** '1du -An (Hal -ana)' (Hal *-ana*) · **-a** '3du -A' (Hal *-ā*) · **-ar** '1pl -Ar: tum-ar 'we remember' < \*tum-ar 'we…' · **-us** '2pl -Os (Hal -us, reduced to the harmonic O)' · **-ant** '3pl -Ant' | — |

**Names** (1)

| First tongue | Meaning | Orrowen | Seilrhass |
|---|---|---|---|
| — | Shoreland cradle-names (names are names) | **Tarnel** 'little net' (Hal *tarnelos*) · **Garvel** 'little smith' (Hal *garvelos*) · **Corlen** 'Corlen (a cradle-name)' (Hal *corlenos*) · **Voss** 'Voss' (Hal *vossos*) · **Hale** 'Hale' (Hal *xalea*) · **Marl** 'Marl' (Hal *marlos*) · **Tamm** 'Tamm' (Hal *tammos*) · **Aske** 'Aske' (Hal *askea*) · **Harl** 'Harl' (Hal *xarlos*) · **Ulden** 'Ulden' (Hal *uldenos*) · **Hesk** 'Hesk' (Hal *heskos*) · **Lanner** 'Lanner' (Hal *lanneros*) · **Aldun** 'Aldun (the first builder of Aldwena)' (Hal *aldunos*) · **Bena** 'Bena (the first builder of Aldwena)' (Hal *benā*) · **Idlan** 'Idlan (of Idrenna)' (Hal *idlanos*) · **Denna** 'Denna (of Idrenna)' (Hal *dennā*) | — |


### 3.3 The reserve roots

**Stone, wood and building** (40)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*buʔnth-* | a rope | bunth (*bunthos*) | veinth |
| *\*festul-* | a chest | vestul (*vestulis*) | vesel (ve'sel); also 'a threshold' |
| *\*beʔk-* | a lid, a cover | baek (*bēkis*) | vea |
| *\*roskur-* | a key; to lock | roskur (*roskuris*) | raesser (raes'ser) |
| *\*greller-* | a lamp | greller (*grelleros*) | rheler (rhe'ler); also 'a market' |
| *\*teumorn-* | a torch | tymorn (*tiumornos*) | thener (the'ner); also 'a siege, a sitting-down around' |
| *\*heilleinn-* | a flask | hellenn (*hellennos*) | eilenn (ei'lenn) |
| *\*swaiwar-* | a cart | saevar (*sēvaros*) | saever (sae'ver); also 'a volley, a shower of shot' |
| *\*skeiwur-* | a wheel | scaevur (*scēvuris*) | seiver (sei'ver); also 'a spear' |
| *\*dufeir-* | an adze | duver (*duvēros*) | theiver (thei'ver) |
| *\*birneinn-* | a trowel | birnenn (*birnennos*) | virenn (vi'renn) |
| *\*xulteir-* | a staff, a rod | hulter (*xultēros*) | rhiler (rhi'ler); also 'a snare, a trap' |
| *\*serull-* | a coin, a struck piece | serull (*serullos*) | serel (se'rel) |
| *\*stufil-* | gold, the metal | styvil (*styvilos*) | seivel (sei'vel) |
| *\*keuwil-* | granite, the grained stone | kyvil (*kiuvilis*) | rhevel (rhe'vel); also 'alone, lonely' |
| *\*heiskal-* | a bridge, a span | heskal (*heskalis*) | eissel (eis'sel) |
| *\*beustir-* | a stair; to climb | bystir (*biustiris*) | veser (ve'ser) |
| *\*lusul-* | a step | lusul (*lusulos*) | leisel (lei'sel) |
| *\*neilteir-* | a vault, an arched room below | nelter (*neltēros*) | neiler (nei'ler); also 'choose' |
| *\*neurul-* | a cellar | nyrul (*niurulis*) | nerel (ne'rel); also 'the self within, a soul' |
| *\*meuger-* | a shaft cut down | myger (*miugeros*) | nerher (ne'rher); also 'a pipe' |
| *\*prassir-* | a floor | pressir (*pressiros*) | rasser (ras'ser) |
| *\*krisur-* | a roof | crisur (*crisuros*) | rheiser (rhei'ser); also 'an assault, a rushing-on' |
| *\*stomorn-* | a beam | stomorn (*stomornos*) | saener (sae'ner); also 'a battle' |
| *\*sweinul-* | a pillar of stone | saenul (*sēnulos*) | seinel (sei'nel); also 'a raised stone of offering' |
| *\*xomar-* | a buttress, a propping wall | homar (*xomaris*) | rhaener (rhae'ner) |
| *\*krarnil-* | an arch | crernil (*crernilos*) | rharel (rha'rel) |
| *\*saler-* | a gallery, a way cut in rock | saler (*saleros*) | saler (sa'ler) |
| *\*xeillur-* | a hall | hellur (*xelluris*) | rheiler (rhei'ler); also 'a ruin, a thing broken down' |
| *\*sweuther-* | a room | syther (*siutheros*) | sether (se'ther) |
| *\*disker-* | a window, an eye in a wall | disker (*diskeris*) | thisser (this'ser) |
| *\*sannorn-* | a drain | sannorn (*sannornos*) | sanner (san'ner) |
| *\*stendor-* | a crane, a lifting-beam | stendor (*stendoris*) | senner (sen'ner) |
| *\*preunur-* | a scaffold | prynur (*priunuros*) | rener (re'ner); also 'the mind' |
| *\*paltur-* | a niche, a small hollow in a wall | paltur (*palturis*) | valer (va'ler); also 'warn' |
| *\*xinnar-* | a walled town | hinnar (*hinnaros*) | rhinner (rhin'ner); also 'skip, leap' |
| *\*brallir-* | a joint between stones | brellir (*brelliros*) | raler (ra'ler); also 'quench, put out' |
| *\*rifull-* | a foundation, the bottom course | rivull (*rivullos*) | reivel (rei'vel); also 'seek' |
| *\*wundor-* | measure | vundor (*vundoros*) | vinner (vin'ner) |
| *\*dasor-* | polish, rub smooth | dasor (*dasoris*) | thaser (tha'ser); also 'late, after the time' |

**Faith, bond and kin** (24)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*lernul-* | oil | lernul (*lernulos*) | lerel (le'rel) |
| *\*mareiss-* | cedar | maress (*maressos*) | naress (na'ress) |
| *\*steuweiss-* | myrrh | styvess (*stiuvessis*) | sevess (se'vess); also 'lie in wait' |
| *\*weusul-* | a threshold | vysul (*viusulos*) | vesel (ve'sel); also 'a chest' |
| *\*ledal-* | a grave | ledal (*ledalos*) | lethel (le'thel) |
| *\*peness-* | holy, set apart | peness (*penessis*) | veness (ve'ness); also 'defend, ward off' |
| *\*stinal-* | a raised stone of offering | stinal (*stinalos*) | seinel (sei'nel); also 'a pillar of stone' |
| *\*daifar-* | believe, hold true | daevar (*dēvaros*) | thaever (thae'ver) |
| *\*saimal-* | hope | saemal (*sēmalos*) | saenel (sae'nel) |
| *\*kaimul-* | shame | kaemul (*kēmulos*) | rhaenel (rhae'nel); also 'weave' |
| *\*leurneiss-* | pride | lyrness (*liurnessos*) | leress (le'ress) |
| *\*xeuleinn-* | gladness, joy | hylenn (*hiulennos*) | rhelenn (rhe'lenn) |
| *\*teiltor-* | mercy | teltor (*teltoris*) | theiler (thei'ler) |
| *\*xeiril-* | forgive, let a wrong go | haeril (*xērilos*) | rheirel (rhei'rel) |
| *\*paiskul-* | bless | peskul (*peskulos*) | vaessel (vaes'sel) |
| *\*xeudull-* | patience; to endure | hydull (*hiudullos*) | rhethel (rhe'thel) |
| *\*tafir-* | hatred; to hate | tevir (*teviros*) | thaver (tha'ver) |
| *\*sweullorn-* | courage | syllorn (*siullornos*) | seler (se'ler) |
| *\*meurral-* | the self within, a soul | myrral (*miurralos*) | nerel (ne'rel); also 'a cellar' |
| *\*grumar-* | the high dwelling, heaven | grumar (*grumaros*) | rheiner (rhei'ner) |
| *\*ternil-* | a rite, a thing done in order | ternil (*ternilis*) | therel (the'rel) |
| *\*buthar-* | anoint | buthar (*butharis*) | veither (vei'ther) |
| *\*stathul-* | praise | stathul (*stathulos*) | sathel (sa'thel) |
| *\*pussal-* | a lot cast; one's lot | pussal (*pussalos*) | vissel (vis'sel) |

**Hearth and people** (38)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*haʔss-* | a son | hass (*hassos*) | aess |
| *\*heʔnn-* | a daughter | henn (*hennis*) | eann |
| *\*huʔmm-* | a husband, the man of a hearth | humm (*hummos*) | einn |
| *\*faʔrr-* | a wife, the woman of a hearth | verr (*verris*) | vear |
| *\*foʔst-* | a brother | vost (*vostos*) | vaes |
| *\*laʔlf-* | a sister | lalva (*lalvā*) | laelvae (lael'vae) |
| *\*skeilur-* | a grandmother, an old mother of the hearth | scaelur (*scēluris*) | seiler (sei'ler) |
| *\*wadull-* | a forebear; the old line | vadull (*vadullos*) | vathel (va'thel) |
| *\*loʔn-* | kin by blood | lonn (*lonnos*) | laen |
| *\*maʔm-* | a friend, one who stands beside | memm (*memmis*) | naen |
| *\*bask-* | a stranger, one from beyond | besk (*beskis*) | vass |
| *\*pithul-* | a lord, one who holds land | pithul (*pithulos*) | veithel (vei'thel) |
| *\*faskorn-* | a trader, one who carries goods | vaskorn (*vaskornis*) | vasser (vas'ser) |
| *\*raʔl-* | a youth, one not yet grown | rall (*rallos*) | rael |
| *\*reʔm-* | a newborn | remm (*remmos*) | rean |
| *\*dhakeir-* | one bereft: an orphan, a widow | dhaker (*dhakēros*) | tharher (tha'rher); also 'gentle' |
| *\*redul-* | a council, those who sit and weigh | redul (*redulis*) | rethel (re'thel) |
| *\*luʔld-* | a boy | luld (*luldos*) | leil |
| *\*neʔm-* | a girl | nemm (*nemmis*) | nean |
| *\*nuʔnth-* | a cup | nunth (*nunthos*) | neinth |
| *\*bleʔnth-* | bread | blenth (*blenthos*) | leanth |
| *\*braimur-* | ale | braemur (*brēmuros*) | raener (rae'ner); also 'a bow for shooting' |
| *\*lodull-* | a bed | lodull (*lodullis*) | laethel (lae'thel) |
| *\*geinth-* | a table | genth (*genthos*) | rheinth |
| *\*kleinth-* | a seat, a chair | clenth (*clenthos*) | leinth |
| *\*preinth-* | a bench | prenth (*prenthis*) | reinth |
| *\*nuleiss-* | a die for casting lots | nuless (*nulessos*) | neiless (nei'less) |
| *\*meugur-* | a pipe | mygur (*miuguris*) | nerher (ne'rher); also 'a shaft cut down' |
| *\*neifal-* | a blanket, a wool cloth | naeval (*nēvalos*) | neivel (nei'vel) |
| *\*xaful-* | a pack, a bundle | havul (*xavulos*) | rhavel (rha'vel) |
| *\*rofal-* | cloth | roval (*rovalis*) | raevel (rae'vel) |
| *\*prelor-* | a thread | prelor (*preloris*) | reler (re'ler); also 'a keel' |
| *\*xasker-* | a needle | hasker (*xaskeris*) | rhasser (rhas'ser) |
| *\*geulorn-* | a market | gylorn (*giulornos*) | rheler (rhe'ler); also 'a lamp' |
| *\*lenull-* | buy, trade for | lenull (*lenullos*) | lenel (le'nel) |
| *\*heunal-* | sell | hynal (*hiunalis*) | enel (e'nel) |
| *\*nethil-* | pay; a payment | nethil (*nethilos*) | nethel (ne'thel) |
| *\*swairdul-* | trade, exchange goods | serdul (*serdulos*) | saerel (sae'rel) |

**The wall, the war, the sea-road** (32)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*beund-* | a foe, one who comes against | bynd (*biundos*) | venn |
| *\*fairnul-* | one who shuts in, a gaoler | vernul (*vernulos*) | vaerel (vae'rel) |
| *\*begorn-* | a watcher on a height | begorn (*begornos*) | verher (ve'rher) |
| *\*kreurull-* | a troop, a band under one leader | cryrull (*criurullos*) | rherel (rhe'rel); also 'understand, grasp' |
| *\*hageiss-* | a pike, a long spear | hagess (*hagessis*) | arhess (a'rhess) |
| *\*mofenn-* | a banner, a sign flown | movenn (*movennos*) | naevenn (nae'venn) |
| *\*gefer-* | a pennant | gever (*geveros*) | rhever (rhe'ver) |
| *\*goful-* | powder | govul (*govulos*) | rhaevel (rhae'vel) |
| *\*preiller-* | a knife, a short blade | preller (*prelleris*) | reiler (rei'ler); also 'a sign, a signal' |
| *\*swifur-* | a spear | sivur (*sivuris*) | seiver (sei'ver); also 'a wheel' |
| *\*rainorn-* | a bow for shooting | raenorn (*rēnornos*) | raener (rae'ner); also 'ale' |
| *\*keilir-* | a ruin, a thing broken down | kaelir (*kēliros*) | rheiler (rhei'ler); also 'a hall' |
| *\*teunur-* | a siege, a sitting-down around | tynur (*tiunuros*) | thener (the'ner); also 'a torch' |
| *\*kiser-* | an assault, a rushing-on | kiser (*kiseros*) | rheiser (rhei'ser); also 'a roof' |
| *\*stomir-* | a battle | stemir (*stemiris*) | saener (sae'ner); also 'a beam' |
| *\*ranner-* | a going-out, a sortie | ranner (*ranneros*) | ranner (ran'ner) |
| *\*fathur-* | a breach | vathur (*vathuros*) | vather (va'ther); also 'doubt' |
| *\*sofir-* | a volley, a shower of shot | sevir (*seviros*) | saever (sae'ver); also 'a cart' |
| *\*xollar-* | flee | hollar (*xollaros*) | rhaeler (rhae'ler) |
| *\*ganur-* | chase, drive before one | ganur (*ganuros*) | rhaner (rha'ner) |
| *\*swefeiss-* | lie in wait | sevess (*sevessos*) | sevess (se'vess); also 'myrrh' |
| *\*kullar-* | a snare, a trap | cullar (*cullaris*) | rhiler (rhi'ler); also 'a staff, a rod' |
| *\*haral-* | an order; to bid | haral (*haralis*) | arel (a'rel) |
| *\*leunir-* | obey, heed an order | lynir (*liuniris*) | lener (le'ner) |
| *\*swannal-* | a victory | sannal (*sannalis*) | sannel (san'nel) |
| *\*larnil-* | a defeat | lernil (*lernilos*) | larel (la'rel) |
| *\*fillur-* | yield, give oneself up | villur (*villuris*) | viler (vi'ler) |
| *\*haithil-* | a truce, a peace made | haethil (*hēthilos*) | aethel (ae'thel) |
| *\*xeness-* | a captive | heness (*xenessos*) | rheness (rhe'ness) |
| *\*pemess-* | defend, ward off | pemess (*pemessis*) | veness (ve'ness); also 'holy, set apart' |
| *\*neʔsk-* | lead | nesk (*neskos*) | neass |
| *\*xwenn-* | follow | fenn (*hwennos*) | rhenn |

**Sea, land and growing things** (51)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*swugorn-* | a fisher | sugorn (*sugornis*) | seirher (sei'rher) |
| *\*higil-* | one who knows the water, a ship-master | higil (*higilos*) | eirhel (ei'rhel) |
| *\*peunull-* | a worker of wood, a boatwright | pynull (*piunullis*) | venel (ve'nel) |
| *\*xweth-* | moss | feth (*hwethos*) | rheth |
| *\*stunnil-* | a fern | stynnil (*stynnilos*) | sinnel (sin'nel) |
| *\*liʔnth-* | grass | linth (*linthos*) | linth |
| *\*siʔnth-* | a flower | sinth (*sinthos*) | sinth |
| *\*nanth-* | fruit | nanth (*nanthos*) | nanth |
| *\*breunt-* | a stump | brynt (*briuntos*) | renth |
| *\*geʔnd-* | a shoot from a stump | gend (*gendos*) | rheann |
| *\*brint-* | a thorn | brint (*brintos*) | rinth |
| *\*guʔnd-* | a hole, a cave | gund (*gundos*) | rheinn |
| *\*geunt-* | a crag | gynt (*giuntos*) | rhenth |
| *\*gint-* | a cliff | gint (*gintis*) | rhinth |
| *\*hiskeinn-* | a pass through mountains | hiskenn (*hiskennos*) | issenn (is'senn) |
| *\*nenth-* | a valley | nenth (*nenthos*) | nenth |
| *\*theukir-* | a gorge, a canyon | thykir (*thiukiros*) | therher (the'rher) |
| *\*tunt-* | a pebble | tynt (*tyntis*) | thinth |
| *\*dheusal-* | shingle, the stony beach | dhysal (*dhiusalis*) | thesel (the'sel) |
| *\*spant-* | surf, breaking water | spant (*spantos*) | santh |
| *\*xwaʔdh-* | a wave | fodh (*hwādhos*) | rhaeth |
| *\*xwidh-* | foam | fidh (*hwidhos*) | rheith |
| *\*keʔss-* | a current in the sea | kess (*kessos*) | rheass |
| *\*praifar-* | a channel | praevar (*prēvaros*) | raever (rae'ver) |
| *\*feʔnth-* | shallow water | venth (*venthis*) | veanth |
| *\*kleʔss-* | a bank, a raised edge | cless (*clessos*) | leass |
| *\*theʔnn-* | a bay, a bend of the shore | thenn (*thennis*) | theann |
| *\*launth-* | a lake, a mere | lynth (*lynthis*) | laenth |
| *\*saʔnth-* | a pool | santh (*santhos*) | saenth |
| *\*naunth-* | a spring, a well | nynth (*nynthis*) | naenth |
| *\*speʔnn-* | mud | spenn (*spennos*) | seann |
| *\*tant-* | salt | tant (*tantos*) | thanth |
| *\*ressur-* | a waste of sand | ressur (*ressuros*) | resser (res'ser) |
| *\*sas-* | a fish | ses (*sesis*) | sas |
| *\*kaunt-* | a beast | kynt (*kyntis*) | rhaenth |
| *\*broʔnt-* | a boulder | bront (*brontos*) | raenth |
| *\*demull-* | a low place, a hollow | demull (*demullis*) | thenel (the'nel) |
| *\*geʔd-* | dry land | gaed (*gēdis*) | rheath |
| *\*nestull-* | an oar | nestull (*nestullos*) | nesel (ne'sel) |
| *\*brelleir-* | a keel | breller (*brellēris*) | reler (re'ler); also 'a thread' |
| *\*krestal-* | a rib of a hull or a body | crestal (*crestalis*) | rhesel (rhe'sel) |
| *\*kreunir-* | a plank | crynir (*criuniros*) | rhener (rhe'ner) |
| *\*mifeinn-* | a mast | mivenn (*mivennos*) | neivenn (nei'venn) |
| *\*taleiss-* | a strake, a line of planking | taless (*talessis*) | thaless (tha'less) |
| *\*troful-* | a seam | trovul (*trovulis*) | thaevel (thae'vel) |
| *\*piskur-* | a net | piskur (*piskuros*) | visser (vis'ser) |
| *\*sulter-* | a small boat | sulter (*sulteros*) | siler (si'ler) |
| *\*heimeir-* | a raft; to float | haemer (*hēmēros*) | einer (ei'ner) |
| *\*xwaʔr-* | sail (v.) | farr (*hwarros*) | rhear |
| *\*luʔss-* | row | luss (*lussos*) | leiss |
| *\*xweʔlm-* | drown | felm (*hwelmos*) | rheal |

**Sky, weather, fire and time** (33)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*rerd-* | the sun | rerd (*rerdos*) | rer |
| *\*selm-* | the moon; a month | selm (*selmos*) | sel |
| *\*eʔlth-* | a star | elth (*elthis*) | eal |
| *\*heʔnth-* | a cloud | henth (*henthos*) | eanth |
| *\*dheʔn-* | a shadow | dhenn (*dhennos*) | thean |
| *\*dheʔs-* | the first light, dawn | dhess (*dhessos*) | theas |
| *\*hadh-* | the last light, dusk, evening | hedh (*hedhis*) | ath |
| *\*sorenn-* | the middle of the day, noon | sorenn (*sorennis*) | saerenn (sae'renn) |
| *\*reust-* | the morning | ryst (*riustos*) | res |
| *\*heth-* | spring, the lengthening | heth (*hethis*) | eth |
| *\*seust-* | summer | syst (*siustos*) | ses |
| *\*breʔmm-* | autumn, the gathering-in | bremm (*bremmos*) | reann |
| *\*breʔss-* | a month, a moon's turn | bress (*bressis*) | reass |
| *\*duʔnd-* | a week, a turn of days | dynd (*dyndis*) | theinn |
| *\*tefar-* | early, before the time | tevar (*tevaros*) | thever (the'ver) |
| *\*dasir-* | late, after the time | desir (*desiris*) | thaser (tha'ser); also 'polish, rub smooth' |
| *\*begess-* | an age, a long time | begess (*begessos*) | verhess (ve'rhess) |
| *\*gordal-* | yesterday | gordal (*gordalos*) | rhaerel (rhae'rel) |
| *\*xwadh-* | a time, a season | fedh (*hwedhis*) | rhath |
| *\*dhiʔdh-* | smoke | dhidh (*dhīdhos*) | thith |
| *\*tuʔss-* | dust | tuss (*tussos*) | theiss |
| *\*keisk-* | an ember | kesk (*keskis*) | rheiss |
| *\*fem-* | a flame | vem (*vemos*) | ven |
| *\*draʔd-* | a spark | drod (*drādos*) | thaeth |
| *\*drid-* | hail | drid (*dridos*) | theith |
| *\*brist-* | lightning | brist (*bristis*) | ris |
| *\*nerdeiss-* | a storm at sea | nerdess (*nerdessos*) | neress (ne'ress) |
| *\*fonul-* | a calm, windless water | vonul (*vonulos*) | vaenel (vae'nel) |
| *\*nas-* | a bird | nas (*nasos*) | nas |
| *\*rothor-* | a fledgling | rothor (*rothoris*) | raether (rae'ther) |
| *\*dhenth-* | a feather; a wing | dhenth (*dhenthis*) | thenth |
| *\*krant-* | cold; to freeze | crent (*crentis*) | rhanth |
| *\*dheʔdh-* | warm | dhaedh (*dhēdhos*) | theath |

**Body, life and feeling** (27)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*bisk-* | the head | bisk (*biskos*) | viss |
| *\*leirn-* | the face | lern (*lernis*) | leir |
| *\*meirn-* | hair | mern (*mernos*) | neir |
| *\*reirn-* | an ear; to listen | rern (*rernos*) | reir |
| *\*muʔm-* | the nose; to smell | mumm (*mummos*) | nein |
| *\*seirr-* | the tongue | serr (*serros*) | seir |
| *\*dast-* | a tooth | dest (*destis*) | thas |
| *\*iʔnth-* | a lip | inth (*inthis*) | inth |
| *\*saʔst-* | skin, a hide | sast (*sastos*) | saes |
| *\*derd-* | a bone | derd (*derdos*) | ther |
| *\*seʔst-* | the shoulder | sest (*sestos*) | seas |
| *\*gard-* | the knee | gerd (*gerdis*) | rhar |
| *\*miʔsk-* | the foot | misk (*miskos*) | niss |
| *\*niʔnd-* | a finger | nind (*nindis*) | ninn |
| *\*siʔmm-* | the belly, the womb | simm (*simmos*) | sinn |
| *\*mann-* | the breast | menn (*mennis*) | nann |
| *\*samm-* | a tear; to weep | semm (*semmis*) | sann |
| *\*eʔdh-* | sleep; to sleep | aedh (*ēdhos*) | eath |
| *\*gern-* | wake, be awake | gern (*gernis*) | rher |
| *\*xwiʔlf-* | a dream | filv (*hwilvos*) | rhil |
| *\*swureiss-* | a fever, a burning of the body | suress (*suressis*) | seiress (sei'ress) |
| *\*kathal-* | sickness | cathal (*cathalis*) | rhathel (rha'thel) |
| *\*meulenn-* | strength | mylenn (*miulennos*) | nelenn (ne'lenn) |
| *\*sulenn-* | a scar, a healed cut | sulenn (*sulennos*) | seilenn (sei'lenn) |
| *\*nask-* | eat | nask (*naskos*) | nass |
| *\*xwiʔm-* | drink | fimm (*hwimmis*) | rhin |
| *\*peuskorn-* | sweat, toil | pyskorn (*piuskornis*) | vesser (ves'ser); also 'spend' |

**Speech, writing and mind** (17)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*saiful-* | one who keeps the rolls, a clerk | saevul (*sēvulis*) | saevel (sae'vel) |
| *\*stidor-* | one who cries news | stidor (*stidoros*) | seither (sei'ther) |
| *\*neukul-* | a lie; to lie | nycul (*niuculos*) | nerhel (ne'rhel) |
| *\*niltenn-* | a plan, a counsel | niltenn (*niltennis*) | nilenn (ni'lenn) |
| *\*reillor-* | a sign, a signal | rellor (*relloros*) | reiler (rei'ler); also 'a knife, a short blade' |
| *\*keiwer-* | think; a thought | kaever (*kēveros*) | rheiver (rhei'ver) |
| *\*xeurril-* | understand, grasp | hyrril (*hiurrilos*) | rherel (rhe'rel); also 'a troop, a band under one…' |
| *\*bathir-* | doubt | bethir (*bethiros*) | vather (va'ther); also 'a breach' |
| *\*reustull-* | learn | rystull (*riustullis*) | resel (re'sel) |
| *\*stukil-* | wonder | stykil (*stykilos*) | seirhel (sei'rhel) |
| *\*preneir-* | the mind | prener (*prenēros*) | rener (re'ner); also 'a scaffold' |
| *\*muʔsk-* | say | mysk (*myskis*) | neiss |
| *\*daʔst-* | shout, scream | dast (*dastos*) | thaes |
| *\*madh-* | whisper | medh (*medhis*) | nath |
| *\*tragul-* | promise; a promise | tragul (*tragulis*) | tharhel (tha'rhel) |
| *\*skeundal-* | a scream | scyndal (*sciundalis*) | sennel (sen'nel); also 'kindle' |
| *\*paltir-* | warn; a warning | peltir (*peltiros*) | valer (va'ler); also 'a niche, a small hollow in a…' |

**Other acts** (53)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*ludal-* | fear | ludal (*ludalos*) | leithel (lei'thel) |
| *\*dheuwull-* | laugh | dhyvull (*dhiuvullos*) | thevel (the'vel) |
| *\*mafer-* | wish, want | maver (*maveros*) | naver (na'ver) |
| *\*neilur-* | choose | naelur (*nēluris*) | neiler (nei'ler); also 'a vault, an arched room below' |
| *\*reiful-* | seek | raevul (*rēvulos*) | reivel (rei'vel); also 'a foundation, the bottom…' |
| *\*rask-* | sit | resk (*reskis*) | rass |
| *\*xwiʔr-* | lie down | firr (*hwirris*) | rhir |
| *\*gust-* | climb | gyst (*gystis*) | rhis |
| *\*kald-* | drag, haul | cald (*caldos*) | rhal |
| *\*baʔmm-* | pull | bamm (*bammos*) | vaenn |
| *\*xast-* | push | hast (*xastos*) | rhas |
| *\*beʔmm-* | lift | bemm (*bemmos*) | veann |
| *\*aʔnth-* | lower | anth (*anthos*) | aenth |
| *\*drig-* | throw | drig (*drigis*) | thei |
| *\*grik-* | catch | grik (*gricos*) | rhei |
| *\*buʔsk-* | tie, knot fast | bysk (*byskis*) | veiss |
| *\*komull-* | weave | comull (*comullis*) | rhaenel (rhae'nel); also 'shame' |
| *\*leurnenn-* | sew | lyrnenn (*liurnennis*) | lerenn (le'renn) |
| *\*paʔsk-* | dig | pask (*paskos*) | vaess |
| *\*laʔmm-* | bury, lay in earth | lamm (*lammos*) | laenn |
| *\*eʔsk-* | cover | esk (*eskos*) | eass |
| *\*leʔmm-* | hide | lemm (*lemmos*) | leann |
| *\*gweʔsk-* | find | wesk (*weskis*) | veass |
| *\*maʔmm-* | lose | mamm (*mammos*) | naenn |
| *\*luʔmm-* | bring | lymm (*lymmis*) | leinn |
| *\*raʔnn-* | save, bring through | renn (*rennis*) | raenn |
| *\*saʔnn-* | spare | sann (*sannos*) | saenn |
| *\*weussor-* | spend | vyssor (*viussoros*) | vesser (ves'ser); also 'sweat, toil' |
| *\*stin-* | cut | stin (*stinos*) | sein |
| *\*daʔn-* | hew | dann (*dannos*) | thaen |
| *\*fiʔdh-* | pour | vidh (*vīdhos*) | vith |
| *\*loʔsk-* | fill; full | losk (*loskos*) | laess |
| *\*sweundal-* | kindle | syndal (*siundalos*) | sennel (sen'nel); also 'a scream' |
| *\*raltar-* | quench, put out | raltar (*raltaros*) | raler (ra'ler); also 'a joint between stones' |
| *\*riʔdh-* | wash | ridh (*rīdhos*) | rith |
| *\*xwaʔlf-* | swim | felv (*hwelvis*) | rhael |
| *\*moʔsk-* | begin | mosk (*moskos*) | naess |
| *\*muʔmm-* | return, come back | mymm (*mymmis*) | neinn |
| *\*neʔnd-* | watch, keep watch | nend (*nendos*) | neann |
| *\*xweʔm-* | touch | femm (*hwemmos*) | rhean |
| *\*ledh-* | feel | ledh (*ledhis*) | leth |
| *\*xweirr-* | bow, bend low | ferr (*hwerros*) | rheir |
| *\*xwuimm-* | sow seed | fymm (*hwymmos*) | rhinn |
| *\*daʔr-* | reap, gather in | derr (*derris*) | thear |
| *\*faʔth-* | tend, care for | voth (*vāthis*) | vaeth |
| *\*neussir-* | prune, cut back to help grow | nyssir (*niussiris*) | nesser (nes'ser) |
| *\*lestir-* | show the way, guide | lestir (*lestiros*) | leser (le'ser) |
| *\*goʔst-* | fell a tree | gost (*gostos*) | rhaes |
| *\*maillor-* | come in, arrive | mellor (*melloros*) | naeler (nae'ler) |
| *\*ruʔnn-* | wake up, rise from sleep | rynn (*rynnis*) | reinn |
| *\*saʔdh-* | play; a game | sodh (*sādhos*) | saeth |
| *\*fiʔlf-* | dance | vilv (*vilvis*) | vil |
| *\*xunneir-* | skip, leap | hunner (*xunnēris*) | rhinner (rhin'ner); also 'a walled town' |

**Qualities** (56)

| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |
|---|---|---|---|
| *\*braʔk-* | dry | broc (*brākis*) | rae |
| *\*thaʔnth-* | wet | thenth (*thenthis*) | thaenth |
| *\*baig-* | bright | baeg (*bēgis*) | vae |
| *\*dustal-* | dim | dustal (*dustalis*) | thisel (thi'sel) |
| *\*stakorn-* | pale | stacorn (*stacornis*) | sarher (sa'rher) |
| *\*weinal-* | brown | vaenal (*vēnalis*) | veinel (vei'nel) |
| *\*podul-* | wise | podul (*podulis*) | vaethel (vae'thel) |
| *\*gennar-* | foolish; a fool | gennar (*gennaros*) | rhenner (rhen'ner) |
| *\*dagorn-* | gentle | dagorn (*dagornis*) | tharher (tha'rher); also 'one bereft: an orphan, a widow' |
| *\*ruthar-* | cruel, hard of heart | ruthar (*rutharis*) | reither (rei'ther) |
| *\*preussal-* | kind | pryssal (*priussalis*) | ressel (res'sel) |
| *\*sumeiss-* | glad, content | sumess (*sumessis*) | seiness (sei'ness) |
| *\*prumul-* | sad, heavy of heart | prumul (*prumulos*) | reinel (rei'nel) |
| *\*xeuwul-* | alone, lonely | hyvul (*hiuvulos*) | rhevel (rhe'vel); also 'granite, the grained stone' |
| *\*pondul-* | empty | pondul (*pondulos*) | vaennel (vaen'nel) |
| *\*suʔsk-* | high | susk (*suskos*) | seiss |
| *\*fiʔm-* | low | vimm (*vimmos*) | vin |
| *\*ruʔss-* | wide | ryss (*ryssis*) | reiss |
| *\*beunt-* | narrow | bynt (*biuntos*) | venth |
| *\*fiʔr-* | near | virr (*virros*) | vir |
| *\*deʔld-* | far | deld (*deldis*) | theal |
| *\*dind-* | thick | dind (*dindis*) | thinn |
| *\*liʔlf-* | soft | lilv (*lilvos*) | lil |
| *\*duss-* | hard | duss (*dussos*) | thiss |
| *\*gesk-* | strong | gesk (*geskos*) | rhess |
| *\*miʔr-* | weak | mirr (*mirros*) | nir |
| *\*niʔs-* | slow | niss (*nissos*) | nis |
| *\*punt-* | quick | pynt (*pyntis*) | vinth |
| *\*bith-* | hot | bith (*bithis*) | veith |
| *\*brid-* | cold | brid (*bridos*) | reith |
| *\*uʔnth-* | red | unth (*unthos*) | einth |
| *\*tairril-* | grey (as ash) | terril (*terrilos*) | thaerel (thae'rel) |
| *\*riʔm-* | sweet | rimm (*rimmos*) | rin |
| *\*skid-* | bitter | scid (*scidis*) | seith |
| *\*duʔl-* | rich | dyll (*dyllis*) | theil |
| *\*riʔrn-* | poor | rirn (*rirnos*) | rir |
| *\*naistorn-* | humble, low-set | nestorn (*nestornos*) | naeser (nae'ser) |
| *\*berd-* | brave, bold | berd (*berdos*) | ver |
| *\*midh-* | clean | midh (*midhis*) | neith |
| *\*felf-* | quiet | velv (*velvis*) | vel |
| *\*boʔnt-* | loud | bont (*bontos*) | vaenth |
| *\*daʔnd-* | wild | dend (*dendis*) | thaenn |
| *\*duʔs-* | strange | dyss (*dyssis*) | theis |
| *\*geʔs-* | sure | gess (*gessis*) | rheas |
| *\*gaʔnd-* | sharp | gand (*gandos*) | rhaenn |
| *\*reʔt-* | blunt, dull | raet (*rētos*) | reath |
| *\*lalf-* | light (not heavy) | lelv (*lelvis*) | lal |
| *\*gaʔsk-* | broken | gask (*gaskos*) | rhaess |
| *\*seʔd-* | half | saed (*sēdos*) | seath |
| *\*merr-* | few | merr (*merros*) | ner |
| *\*mest-* | much, many | mest (*mestos*) | nes |
| *\*krustil-* | old (of things), worn | crystil (*crystilos*) | rhisel (rhi'sel) |
| *\*beikar-* | well made, well done | baecar (*bēcaros*) | veirher (vei'rher) |
| *\*dath-* | evil, ill | dath (*dathos*) | thath |
| *\*deth-* | proud | deth (*dethos*) | theth |
| *\*rarr-* | fair, lovely to see | rerr (*rerris*) | rar |


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

| Orrowen | Sense | How it falls out |
|---|---|---|
| **tolm** | a stone | *\*tolm-o-s* = Hal *tolmos* (unchanged) >H2 *tolm* |
| **tald** | rise, stand up (v.) | *\*tal-d-o-s* = Hal *taldos* (unchanged) >H2 *tald* |
| **taldow** | a tower, a high place | *\*tal-d-uʔ* >O1 *taldū* = Hal *taldū* >H3 *taldow* |
| **hal** | bedrock, the living rock of the ridge | *\*xal-o-s* = Hal *xalos* (unchanged) >H2 *xal* >H4 *hal* |
| **hald** | a wall ('rock made to stand') | *\*xal-d-o-s* = Hal *xaldos* (unchanged) >H2 *xald* >H4 *hald* |
| **lodh** | mortar | *\*lodh-o-s* = Hal *lodhos* (unchanged) >H2 *lodh* |
| **trenn** | a course of stones | *\*trenn-o-s* = Hal *trennos* (unchanged) >H2 *trenn* |
| **cadh** | lay (a stone, a course, a tale) | *\*kadh-o-s* = Hal *cadhos* (unchanged) >H2 *cadh* |
| **ston** | stand (of a wall), make stand, hold firm | *\*ston-o-s* = Hal *stonos* (unchanged) >H2 *ston* |
| **gald** | build, raise a work | *\*gal-d-o-s* = Hal *galdos* (unchanged) >H2 *gald* |
| **gal** | (old) was: the suppletive past of doss, re yal- | *\*gal-o-s* = Hal *galos* (unchanged) >H2 *gal* |
| **clenn** | new | *\*klenn-i-s* = Hal *clennis* (unchanged) >H2 *clenn* |
| **stann** | quarry, cut stone from the bed | *\*stann-o-s* = Hal *stannos* (unchanged) >H2 *stann* |
| **Stannard** | 'quarrier' | *\*stann-ard-o-s* = Hal *stannardos* (unchanged) >H2 *stannard* |
| **bresk** | a chisel | *\*brask-i-s* >O3 *breskis* = Hal *breskis* >H2 *bresk* |
| **drunn** | a mallet, a hammer | *\*drunn-o-s* = Hal *drunnos* (unchanged) >H2 *drunn* |
| **gann** | a post, an upright | *\*gann-o-s* = Hal *gannos* (unchanged) >H2 *gann* |
| **ganna** | a gate ('the two posts') | *\*gann-aʔ* >O1 *gannā* = Hal *gannā* >H3 *ganna* |
| **hosk** | a lintel | *\*hosk-o-s* = Hal *hoskos* (unchanged) >H2 *hosk* |
| **gorn** | a corner, a quoin | *\*gorn-o-s* = Hal *gornos* (unchanged) >H2 *gorn* |
| **keth** | hold, keep | *\*keth-i-s* = Hal *kethis* (unchanged) >H2 *keth* |
| **kethow** | a keep, a hold | *\*keth-uʔ* >O1 *kethū* = Hal *kethū* >H3 *kethow* |
| **tresk** | a cleft, a split | *\*trosk-i-s* >O3 *treskis* = Hal *treskis* >H2 *tresk* |
| **lest** | a house | *\*last-i-s* >O3 *lestis* = Hal *lestis* >H2 *lest* |
| **cumm** | a haven: any walled place of shelter | *\*kumm-o-s* = Hal *cummos* (unchanged) >H2 *cumm* |
| **stell** | a cairn | *\*stell-i-s* = Hal *stellis* (unchanged) >H2 *stell* |
| **pell** | a spire, a tall point | *\*pell-i-s* = Hal *pellis* (unchanged) >H2 *pell* |
| **Pellow** | 'of the spire' | *\*pell-uʔ* >O1 *pellū* = Hal *pellū* >H3 *pellow* |
| **ryt** | a cut vow, an oath | *\*wrut-i-s* >O3 *wrytis* = Hal *wrytis* >H2 *wryt* >H4 *ryt* |
| **prass** | a master of the craft | *\*prass-o-s* = Hal *prassos* (unchanged) >H2 *prass* |
| **hemm** | old | *\*hemm-o-s* = Hal *hemmos* (unchanged) >H2 *hemm* |
| **hemma** | Elderess | *\*hemm-aʔ* >O1 *hemmā* = Hal *hemmā* >H3 *hemma* |
| **mardh** | God (used of nothing else) | *\*mardh-o-s* = Hal *mardhos* (unchanged) >H2 *mardh* |
| **ammel** | pray | *\*amm-el-i-s* = Hal *ammelis* (unchanged) >H2 *ammel* |
| **ammad** | teach | *\*amm-ad-o-s* = Hal *ammados* (unchanged) >H2 *ammad* |
| **tev** | a child | *\*taw-i-s* >O3 *tewis* >O4 *tevis* = Hal *tevis* >H2 *tev* |
| **voll** | a name | *\*woll-o-s* >O4 *vollos* = Hal *vollos* >H2 *voll* |
| **tunn** | whole, complete | *\*tunn-o-s* = Hal *tunnos* (unchanged) >H2 *tunn* |
| **grest** | harm, hurt | *\*grest-o-s* = Hal *grestos* (unchanged) >H2 *grest* |
| **par** | guard, protect | *\*par-o-s* = Hal *paros* (unchanged) >H2 *par* |
| **pard** | a warden, a keeper | *\*par-d-o-s* = Hal *pardos* (unchanged) >H2 *pard* |
| **Halvard** | 'bedrock-warden' | *\*xal+par-d-o-s* = Hal *xalpardos* (unchanged) >H2 *xalpard* >H4 *halpard* >H5 *halvard* |
| **odh** | a hearth | *\*odh-o-s* = Hal *odhos* (unchanged) >H2 *odh* |
| **odha** | a mother ('she of the hearth') | *\*odh-aʔ* >O1 *odhā* = Hal *odhā* >H3 *odha* |
| **theld** | a family, a household | *\*thald-i-s* >O3 *theldis* = Hal *theldis* >H2 *theld* |
| **varn** | home | *\*waʔr-n-o-s* >O1 *warrnos* >O4 *varrnos* >O5 *varnos* = Hal *varnos* >H2 *varn* |
| **gedh** | a father | *\*gadh-i-s* >O3 *gedhis* = Hal *gedhis* >H2 *gedh* |
| **uld** | a man | *\*uld-o-s* = Hal *uldos* (unchanged) >H2 *uld* |
| **essa** | a woman | *\*ess-aʔ* >O1 *essā* = Hal *essā* >H3 *essa* |
| **lunt** | a people, a nation | *\*lunt-o-s* = Hal *luntos* (unchanged) >H2 *lunt* |
| **orr** | go, walk | *\*orr-o-s* = Hal *orros* (unchanged) >H2 *orr* |
| **orrow** | the Shore | *\*orr-uʔ* >O1 *orrū* = Hal *orrū* >H3 *orrow* |
| **arra** | a guest | *\*arr-aʔ* >O1 *arrā* = Hal *arrā* >H3 *arra*. *keeps the dual -a: a guest is half of a pair* |
| **gebb** | a door | *\*gebb-i-s* = Hal *gebbis* (unchanged) >H2 *gebb* |
| **lumm** | kneel | *\*lumm-o-s* = Hal *lummos* (unchanged) >H2 *lumm* |
| **vall** | love | *\*waʔl-o-s* >O1 *wallos* >O4 *vallos* = Hal *vallos* >H2 *vall* |
| **osk** | trust (v. and n.) | *\*osk-o-s* = Hal *oskos* (unchanged) >H2 *osk* |
| **tesk** | a generation | *\*tesk-i-s* = Hal *teskis* (unchanged) >H2 *tesk* |
| **sost** | self, very | *\*swo-st-o-s* >O4 *sostos* = Hal *sostos* >H2 *sost* |
| **Seren** | 'a single sorrow that overcomes' | *\*swe-reŋ-o-s* >O4 *sereŋos* = Hal *sereŋos* >H2 *sereŋ* >H4 *seren* |
| **crenn** | a captain | *\*krenn-o-s* = Hal *crennos* (unchanged) >H2 *crenn* |
| **hesp** | a sword | *\*hesp-i-s* = Hal *hespis* (unchanged) >H2 *hesp* |
| **kest** | a company of soldiers | *\*kest-i-s* = Hal *kestis* (unchanged) >H2 *kest* |
| **bramm** | a gun ('the roarer') | *\*bramm-o-s* = Hal *brammos* (unchanged) >H2 *bramm* |
| **hask** | run | *\*hask-o-s* = Hal *haskos* (unchanged) >H2 *hask* |
| **gomm** | a horn | *\*gomm-o-s* = Hal *gommos* (unchanged) >H2 *gomm* |
| **carm** | a call, a cry | *\*karm-o-s* = Hal *carmos* (unchanged) >H2 *carm* |
| **pedh** | a shot: what a gun throws | *\*pedh-i-s* = Hal *pedhis* (unchanged) >H2 *pedh* |
| **trun** | ground | *\*trun-o-s* = Hal *trunos* (unchanged) >H2 *trun* |
| **marr** | shift, move to another place | *\*marr-o-s* = Hal *marros* (unchanged) >H2 *marr* |
| **kyl** | change | *\*kul-i-s* >O3 *kylis* = Hal *kylis* >H2 *kyl* |
| **lusk** | loose, let go, set free | *\*lusk-o-s* = Hal *luskos* (unchanged) >H2 *lusk* |
| **bosk** | attack | *\*bosk-o-s* = Hal *boskos* (unchanged) >H2 *bosk* |
| **hurr** | kill | *\*hurr-o-s* = Hal *hurros* (unchanged) >H2 *hurr* |
| **gorr** | fight | *\*gorr-o-s* = Hal *gorros* (unchanged) >H2 *gorr* |
| **covv** | a cloak | *\*koff-o-s* >O4 *covvos* = Hal *covvos* >H2 *covv* |
| **sceth** | a ship, a hull (a trunk hewn out) | *\*sketh-i-s* = Hal *scethis* (unchanged) >H2 *sceth* |
| **wemm** | a sail | *\*gwemm-i-s* >O4 *wemmis* = Hal *wemmis* >H2 *wemm* |
| **wadh** | the sea | *\*gwadh-o-s* >O4 *wadhos* = Hal *wadhos* >H2 *wadh* |
| **myst** | sea-fog | *\*mus-t-i-s* >O3 *mystis* = Hal *mystis* >H2 *myst* |
| **mesk** | a tree | *\*mosk-i-s* >O3 *meskis* = Hal *meskis* >H2 *mesk* |
| **lurr** | a forest | *\*lurr-o-s* = Hal *lurros* (unchanged) >H2 *lurr* |
| **helv** | the sky, the upper air | *\*half-i-s* >O3 *helfis* >O4 *helvis* = Hal *helvis* >H2 *helv* |
| **hyll** | a tide | *\*hull-i-s* >O3 *hyllis* = Hal *hyllis* >H2 *hyll* |
| **rhull** | a river | *\*xrull-o-s* >O4 *hrullos* = Hal *hrullos* >H2 *hrull* >H4 *rhull* |
| **sedh** | a fen | *\*sedh-i-s* = Hal *sedhis* (unchanged) >H2 *sedh* |
| **nell** | an islet | *\*nall-i-s* >O3 *nellis* = Hal *nellis* >H2 *nell* |
| **tav** | come ashore, land a boat | *\*taf-o-s* >O4 *tavos* = Hal *tavos* >H2 *tav* |
| **tavow** | a harbour, a landing | *\*taf-uʔ* >O1 *tafū* >O4 *tavū* = Hal *tavū* >H3 *tavow* |
| **sorth** | a ridge | *\*sorth-o-s* = Hal *sorthos* (unchanged) >H2 *sorth* |
| **brunn** | a mountain | *\*brunn-o-s* = Hal *brunnos* (unchanged) >H2 *brunn* |
| **grull** | sand | *\*grull-o-s* = Hal *grullos* (unchanged) >H2 *grull* |
| **sirr** | glass | *\*sirr-i-s* = Hal *sirris* (unchanged) >H2 *sirr* |
| **crest** | ice | *\*krest-i-s* = Hal *crestis* (unchanged) >H2 *crest* |
| **frenn** | frost, rime | *\*xwren-n-o-s* >O4 *hwrennos* = Hal *hwrennos* >H2 *hwrenn* >H4 *frenn* |
| **sulv** | snow | *\*sulf-o-s* >O4 *sulvos* = Hal *sulvos* >H2 *sulv* |
| **grem** | winter | *\*grem-i-s* = Hal *gremis* (unchanged) >H2 *grem* |
| **vorr** | fire | *\*forr-o-s* >O4 *vorros* = Hal *vorros* >H2 *vorr* |
| **orl** | a day | *\*orl-o-s* = Hal *orlos* (unchanged) >H2 *orl* |
| **vess** | a night | *\*feʔs-i-s* >O1 *fessis* >O4 *vessis* = Hal *vessis* >H2 *vess* |
| **clem** | an hour | *\*klem-i-s* = Hal *clemis* (unchanged) >H2 *clem* |
| **surr** | a year | *\*surr-o-s* = Hal *surros* (unchanged) >H2 *surr* |
| **cemm** | meet | *\*kamm-i-s* >O3 *cemmis* = Hal *cemmis* >H2 *cemm* |
| **garl** | a hand | *\*garl-o-s* = Hal *garlos* (unchanged) >H2 *garl* |
| **molt** | a heart | *\*molt-o-s* = Hal *moltos* (unchanged) >H2 *molt* |
| **hoss** | breath | *\*hoss-o-s* = Hal *hossos* (unchanged) >H2 *hoss* |
| **lorr** | blood | *\*lorr-o-s* = Hal *lorros* (unchanged) >H2 *lorr* |
| **senn** | die: go out, as a fire in peace | *\*senn-i-s* = Hal *sennis* (unchanged) >H2 *senn* |
| **hess** | stop | *\*hess-i-s* = Hal *hessis* (unchanged) >H2 *hess* |
| **lomm** | grief | *\*lomm-o-s* = Hal *lommos* (unchanged) >H2 *lomm* |
| **sol** | rest, lie still | *\*sol-o-s* = Hal *solos* (unchanged) >H2 *sol* |
| **sollan** | peace ('the rest after the work') | *\*soʔl-an-o-s* >O1 *sollanos* = Hal *sollanos* >H2 *sollan* |
| **lunn** | freedom | *\*lunn-o-s* = Hal *lunnos* (unchanged) >H2 *lunn* |
| **tum** | remember | *\*tum-o-s* = Hal *tumos* (unchanged) >H2 *tum* |
| **tumol** | remembering | *\*tum-ol-a* = Hal *tumola* (unchanged) >H2 *tumol* |
| **brod** | a word | *\*brod-o-s* = Hal *brodos* (unchanged) >H2 *brod* |
| **brodh** | put into words, tell, speak | *\*brodh-o-s* = Hal *brodhos* (unchanged) >H2 *brodh* |
| **Brenn** | Brenn: a name. Names are names | *\*brenn-o-s* = Hal *brennos* (unchanged) >H2 *brenn* |
| **vesk** | see | *\*wesk-i-s* >O4 *veskis* = Hal *veskis* >H2 *vesk* |
| **flenn** | a leaf of a book or of slate | *\*xwlen-naʔ* >O1 *xwlennā* >O4 *hwlennā* = Hal *hwlennā* >H2 *hwlenn* >H4 *flenn*. *the -ā fell, because it was not the dual or the feminine but a stem vowel* |
| **luth** | ink | *\*luth-o-s* = Hal *luthos* (unchanged) >H2 *luth* |
| **brenth** | coal | *\*branth-i-s* >O3 *brenthis* = Hal *brenthis* >H2 *brenth* |
| **vell** | a song | *\*fell-i-s* >O4 *vellis* = Hal *vellis* >H2 *vell* |
| **sesk** | know a fact | *\*sesk-i-s* = Hal *seskis* (unchanged) >H2 *sesk* |
| **nydh** | count | *\*nudh-i-s* >O3 *nydhis* = Hal *nydhis* >H2 *nydh* |
| **kael** | a tally-notch | *\*kail-o-s* >O2 *kēlos* = Hal *kēlos* >H2 *kēl* >H3 *kael* |
| **pess** | ask | *\*pess-i-s* = Hal *pessis* (unchanged) >H2 *pess* |
| **tess** | answer | *\*tess-i-s* = Hal *tessis* (unchanged) >H2 *tess* |
| **tessen** | we two answer (1du) | *\*tess-ana* = Hal *tessana* (unchanged) >H2 *tessan* >H6 *tessen* |
| **doss** | be (state, place) | *\*doss-o-s* = Hal *dossos* (unchanged) >H2 *doss* |
| **el** | is (the copula) | *\*el-i-s* = Hal *elis* (unchanged) >H2 *el* |
| **ew** | was | *\*egw-as* >O4 *ewas* = Hal *ewas* >H2 *ew* |
| **darr** | come | *\*darr-o-s* = Hal *darros* (unchanged) >H2 *darr* |
| **hunn** | hear | *\*hunn-o-s* = Hal *hunnos* (unchanged) >H2 *hunn* |
| **hebb** | give | *\*habb-i-s* >O3 *hebbis* = Hal *hebbis* >H2 *hebb* |
| **tovv** | wait | *\*toff-o-s* >O4 *tovvos* = Hal *tovvos* >H2 *tovv* |
| **omm** | fall | *\*omm-o-s* = Hal *ommos* (unchanged) >H2 *omm* |
| **cresk** | break | *\*krask-i-s* >O3 *creskis* = Hal *creskis* >H2 *cresk* |
| **ser** | go on, carry forward | *\*ser-i-s* = Hal *seris* (unchanged) >H2 *ser* |
| **rhyn** | set fast (of mortar), take hold | *\*xreun-i-s* >O2 *xriunis* >O4 *hriunis* = Hal *hriunis* >H2 *hriun* >H4 *rhyn* |
| **Rhyna** | 'she who sets fast' | *\*xreun-aʔ* >O1 *xreunā* >O2 *xriunā* >O4 *hriunā* = Hal *hriunā* >H3 *hriuna* >H4 *rhyna* |
| **strom** | great | *\*strom-o-s* = Hal *stromos* (unchanged) >H2 *strom* |
| **lyss** | small | *\*luss-i-s* >O3 *lyssis* = Hal *lyssis* >H2 *lyss* |
| **gell** | good | *\*gell-i-s* = Hal *gellis* (unchanged) >H2 *gell* |
| **venn** | true | *\*weinn-i-s* >O2 *wēnnis* >O2 *wennis* >O4 *vennis* = Hal *vennis* >H2 *venn* |
| **gunn** | deep | *\*gunn-o-s* = Hal *gunnos* (unchanged) >H2 *gunn* |
| **sell** | long | *\*sell-i-s* = Hal *sellis* (unchanged) >H2 *sell* |
| **domm** | black | *\*domm-o-s* = Hal *dommos* (unchanged) >H2 *domm* |
| **bell** | gold, golden | *\*bell-i-s* = Hal *bellis* (unchanged) >H2 *bell* |
| **lenn** | silver | *\*lenn-i-s* = Hal *lennis* (unchanged) >H2 *lenn* |
| **et** | the (the article) | *\*et-as* = Hal *etas* (unchanged) >H2 *et* |
| **ul** | in (+N) | *\*ul-an* = Hal *ulan* (unchanged) >H1 *ula* >H2 *ul* |
| **hy** | from, out of (+S) | *\*xui-a* >O2 *xya* >O4 *hya* = Hal *hya* >H2 *hy* |
| **um** | upon, on (+S) | *\*um-o* = Hal *umo* (unchanged) >H2 *um* |
| **lo** | at, by, with (+S) | *\*lo-a* = Hal *loa* (unchanged) >H2 *lo* |
| **dem** | until, as far as (+N) | *\*dem-en* = Hal *demen* (unchanged) >H1 *deme* >H2 *dem* |
| **eth** | and | *\*eth-as* = Hal *ethas* (unchanged) >H2 *eth* |
| **ell** | or | *\*ell-o* = Hal *ello* (unchanged) >H2 *ell* |
| **veth** | but, rather | *\*weth-o* >O4 *vetho* = Hal *vetho* >H2 *veth* |
| **na** | un- (prefix, +S) | *\*na* = Hal *na* (unchanged) |
| **nath** | not (before a verb, +N) | *\*nath-an* = Hal *nathan* (unchanged) >H1 *natha* >H2 *nath* |
| **re** | past particle (+S) | *\*re* = Hal *re* (unchanged). *the spec's §4.3 gives Hal rea; the Stonwryt itself cuts RE, and RE is right: a vowel-final word, so it softens* |
| **es** | future particle (+N) | *\*es-an* = Hal *esan* (unchanged) >H1 *esa* >H2 *es* |
| **ho** | question particle (+S) | *\*ho-a* = Hal *hoa* (unchanged) >H2 *ho* |
| **sa** | who, which, that (relative, +S) | *\*sa-e* = Hal *sae* (unchanged) >H2 *sa* |
| **somm** | while, as long as | *\*soŋ-ma-s* = Hal *soŋmas* (unchanged) >H2 *soŋm* >H4 *somm* |
| **amm** | when (conj.) | *\*aŋ-ma* = Hal *aŋma* (unchanged) >H2 *aŋm* >H4 *amm* |
| **cedh** | who? | *\*ka-dh-i* >O3 *cedhi* = Hal *cedhi* >H2 *cedh* |
| **vodh** | what? | *\*wo-dh-o* >O4 *vodho* = Hal *vodho* >H2 *vodh* |
| **sy** | this (after the noun) | *\*siu* = Hal *siu* (unchanged) >H4 *sy* |
| **ull** | that (after the noun) | *\*ull-o* = Hal *ullo* (unchanged) >H2 *ull* |
| **gor** | every, all (+S) | *\*gor-a* = Hal *gora* (unchanged) >H2 *gor* |
| **tul** | yet, still | *\*tul-o* = Hal *tulo* (unchanged) >H2 *tul* |
| **dask** | the end | *\*dask-o-s* = Hal *daskos* (unchanged) >H2 *dask* |
| **en** | I | *\*en-an* = Hal *enan* (unchanged) >H1 *ena* >H2 *en* |
| **tho** | you | *\*tho-e* = Hal *thoe* (unchanged) >H2 *tho* |
| **o** | he, it | *\*o-a* = Hal *oa* (unchanged) >H2 *o* |
| **ey** | she | *\*ey-as* = Hal *eyas* (unchanged) >H2 *ey* |
| **ol** | we | *\*ol-on* = Hal *olon* (unchanged) >H1 *olo* >H2 *ol* |
| **olna** | we two (+S) | *\*ol-naʔ* >O1 *olnā* = Hal *olnā* >H3 *olna* |
| **va** | you | *\*wa-n* >O4 *van* = Hal *van* >H1 *va*. *the spec's Hal vanan is emended to van: vanan would give \*van* |
| **so** | they | *\*so-a* = Hal *soa* (unchanged) >H2 *so* |
| **sona** | they two (+S) | *\*so-naʔ* >O1 *sonā* = Hal *sonā* >H3 *sona* |
| **hos** | one | *\*hos-o-s* = Hal *hosos* (unchanged) >H2 *hos* |
| **pa** | two (+S) | *\*paʔ* >O1 *pā* = Hal *pā* >H3 *pa* |
| **pana** | both | *\*pa-naʔ* >O1 *panā* = Hal *panā* >H3 *pana* |
| **rost** | nine ('thrice three') | *\*ros-t-o-s* = Hal *rostos* (unchanged) >H2 *rost* |
| **sull** | three | *\*sull-o-s* = Hal *sullos* (unchanged) >H2 *sull* |
| **gemm** | four | *\*gemm-i-s* = Hal *gemmis* (unchanged) >H2 *gemm* |
| **lesk** | five | *\*lesk-i-s* = Hal *leskis* (unchanged) >H2 *lesk* |
| **vran** | six | *\*fran-o-s* >O4 *vranos* = Hal *vranos* >H2 *vran* |
| **dhom** | seven | *\*dhom-o-s* = Hal *dhomos* (unchanged) >H2 *dhom* |
| **thell** | eight | *\*thell-i-s* = Hal *thellis* (unchanged) >H2 *thell* |
| **noth** | ten | *\*noth-o-s* = Hal *nothos* (unchanged) >H2 *noth* |
| **delv** | twelve | *\*delf-i-s* >O4 *delvis* = Hal *delvis* >H2 *delv* |
| **murr** | twenty | *\*murr-o-s* = Hal *murros* (unchanged) >H2 *murr* |
| **bost** | four hundred | *\*bost-o-s* = Hal *bostos* (unchanged) >H2 *bost* |
| **-ath** | plural -Ath | *\*-athi* = Hal *-athi* (unchanged) >H2 *ath* |
| **-ol** | verbal noun -Ol | *\*-ola* = Hal *-ola* (unchanged) >H2 *ol* |
| **-at** | participle -At | *\*-at* = Hal *-at* (unchanged) |
| **-ard** | agent -Ard | *\*-ard* = Hal *-ard* (unchanged) |
| **-oth** | abstract -Oth | *\*-oth* = Hal *-oth* (unchanged) |
| **-el** | singulative | *\*-el* = Hal *-el* (unchanged) |
| **-an** | collective 'the folk of' | *\*-an* = Hal *-an* (unchanged) |
| **-en** | 'of, belonging to' | *\*-en* = Hal *-en* (unchanged) |
| **-ow** | place of -ow | *\*-uʔ* >O1 *ū* = Hal *-ū* >H3 *ow* |
| **-ast** | ordinal -Ast | *\*-ast* = Hal *-ast* (unchanged) |
| **-a** | the old dual | *\*-aʔ* >O1 *ā* = Hal *-ā* >H3 *a* |
| **-na** | dual of a pronoun | *\*-naʔ* >O1 *nā* = Hal *-nā* >H3 *na* |
| **-om** | 1sg -Om | *\*-om* = Hal *-om* (unchanged) |
| **-ith** | 2sg -ith | *\*-ith* = Hal *-ith* (unchanged) |
| **-an** | 1du -An (Hal -ana) | *\*-ana* = Hal *-ana* (unchanged) >H2 *an* |
| **-a** | 3du -A | *\*-aʔ* >O1 *ā* = Hal *-ā* >H3 *a* |
| **-ar** | 1pl -Ar: tum-ar 'we remember' < \*tum-ar 'we hold' | *\*-ar* = Hal *-ar* (unchanged) |
| **-us** | 2pl -Os (Hal -us, reduced to the harmonic O) | *\*-us* = Hal *-us* (unchanged) |
| **-ant** | 3pl -Ant | *\*-ant* = Hal *-ant* (unchanged) |
| **Tarnel** | 'little net' | *\*tarn-el-o-s* = Hal *tarnelos* (unchanged) >H2 *tarnel* |
| **Garvel** | 'little smith' | *\*garf-el-o-s* >O4 *garvelos* = Hal *garvelos* >H2 *garvel* |
| **Corlen** | Corlen (a cradle-name) | *\*korlen-o-s* = Hal *corlenos* (unchanged) >H2 *corlen* |
| **Voss** | Voss | *\*woss-o-s* >O4 *vossos* = Hal *vossos* >H2 *voss* |
| **Hale** | Hale | *\*xaleʔa* >O1 *xalea* = Hal *xalea* >H2 *xale* >H4 *hale* |
| **Marl** | Marl | *\*marl-o-s* = Hal *marlos* (unchanged) >H2 *marl* |
| **Tamm** | Tamm | *\*tamm-o-s* = Hal *tammos* (unchanged) >H2 *tamm* |
| **Aske** | Aske | *\*askeʔa* >O1 *askea* = Hal *askea* >H2 *aske* |
| **Harl** | Harl | *\*xarl-o-s* = Hal *xarlos* (unchanged) >H2 *xarl* >H4 *harl* |
| **Ulden** | Ulden | *\*uld-en-o-s* = Hal *uldenos* (unchanged) >H2 *ulden* |
| **Hesk** | Hesk | *\*hesk-o-s* = Hal *heskos* (unchanged) >H2 *hesk* |
| **Lanner** | Lanner | *\*lann-er-o-s* = Hal *lanneros* (unchanged) >H2 *lanner* |
| **Aldun** | Aldun (the first builder of Aldwena) | *\*ald-un-o-s* = Hal *aldunos* (unchanged) >H2 *aldun* |
| **Bena** | Bena (the first builder of Aldwena) | *\*ben-aʔ* >O1 *benā* = Hal *benā* >H3 *bena* |
| **Idlan** | Idlan (of Idrenna) | *\*id-lan-o-s* = Hal *idlanos* (unchanged) >H2 *idlan* |
| **Denna** | Denna (of Idrenna) | *\*denn-aʔ* >O1 *dennā* = Hal *dennā* >H3 *denna* |

**Words Orrowen built for itself** (compounds, suffixes, mutations: the daughter's grammar, not sound change). Every part is an inherited word above.

| Word | Built from | How |
|---|---|---|
| **nayald** | na- + gald | na- + S gald (g > y) |
| **stannow** | stann + -ow | place -ow |
| **gorndholm** | gorn + tolm | compound: second element softened (t > dh) |
| **trenndholm** | trenn + tolm | compound, softened |
| **halflenn** | hal + flenn | compound 'rock-leaf' |
| **stonwryt** | ston + ryt | Hal compound stonwryta, built on the Hal stems ston- and wryt- (hence its y); the guild keeps the w in spelling |
| **stonwrytan** | stonwryt + -an | collective |
| **stonwrytel** | stonwryt + -el | singulative |
| **prassel** | prass + -el | 'little master' |
| **vennoth** | venn + -oth | abstract (the spec's slip: by harmony vennyth) |
| **lodhat** | lodh + -at | participle |
| **nalodhat** | na- + lodhat | un- |
| **lodhan** | lodh + -an | collective: et Lodhan, the Bonded |
| **sullast** | sull + -ast | ordinal |
| **hosast** | hos + -ast | ordinal |
| **pawast** | pa + -ast | ordinal (w between the vowels) |
| **veskerd** | vesk + -ard | agent, slender |
| **tevow** | tev + -ow | Hal tevū, built on tev- after the i-colouring |
| **tevath** | tev + -ath | Hal tevāthi: the broad plural of an old ā-plural |
| **tevel** | tev + -el | 'young' |
| **hoskol** | hosk + -ol | the sealing |
| **hoskvoll** | hosk + voll | compound, softened |
| **tolm vardh** | tolm + mardh | construct, possessor softened (m > v) |
| **tolmath vardh** | tolm + -ath + mardh | plural |
| **tunnoth** | tunn + -oth | wholeness |
| **ryt dhunnoth** | ryt + tunnoth | construct, softened (t > dh) |
| **lodh helv** | lodh + helv | construct |
| **odh sell** | odh + sell | the Long Hearth |
| **orrowan** | orrow + -an | the shore-folk |
| **orrowen** | orrow + -en | 'of the Shore' |
| **brodhen** | brodh + -en | a speech, a tongue |
| **treskan** | tresk + -an | the cleft-folk (broad: the spec keeps tresk's old broad suffixes, as in treskat) |
| **ketherd** | keth + -ard | the holder: the Commander |
| **vennuld** | venn + uld | compound: a True Man |
| **hesperd** | hesp + -ard | 'sword-one' |
| **bramman** | bramm + -an | a battery |
| **haskard** | hask + -ard | a runner |
| **drunnard** | drunn + -ard | a smith |
| **drunnow** | drunn + -ow | a smithy |
| **hosk lunn** | hosk + lunn | the Title of Liberty |
| **scethan** | sceth + -an | a fleet |
| **scethel** | sceth + -el | one hull of it |
| **treskat** | tresk + -at | riven, torn (an old broad suffix: see §11b of the spec) |
| **covv treskat** | covv + treskat | the Torn Cloak |
| **mystow** | myst + -ow | the Mystlands |
| **mystaeri** | myst + -aer + -i | hybrid: Orrowen myst + the Eldest Seilrhass -aer (before -aer > -ear) + an Orrowen loan-plural -i |
| **mesk myst** | mesk + myst | Mystwood |
| **tolm myst** | tolm + myst | Myststone |
| **gannath myst** | gann + -ath + myst | the Mystholders |
| **crenn myst** | crenn + myst | a Mystarch |
| **lurrel** | lurr + -el | green, 'forest-coloured' |
| **tumol** | tum + -ol | memory (also inherited whole: \*tum-ol-a) |
| **nadhum** | na- + tum | forget, un-remember (t > dh) |
| **flennath** | flenn + -ath | the Book: broad, as an old ā-stem (see tevath) |
| **nydherd** | nydh + -ard | a counter: Kael Nydherd |
| **brodhat** | brodh + -at | told |
| **nawrodhat** | na- + brodhat | untold (b > w) |
| **kethyl** | keth + -ol | holding (slender -yl) |
| **sennyl** | senn + -ol | dying, death |
| **tumar** | tum + -ar | we remember: the hearth's answer, and Orrowen's 'yes' |
| **ulvenn** | ul + venn | inner: 'true-in' |
| **tolmvard** | tolm + pard | Stone-Warden, Halvard's epithet |
| **cadhat** | cadh + -at | laid |
| **halyna** | hal + rhyna + -a | pair-name: Hal- + softened Rhyn- (rh > h, lost after a consonant) + the lintel -a |
| **aldwena** | aldun + bena + -a | pair-name: Ald- + softened Ben- (b > w) + -a |
| **idrenna** | idlan + denna + -a | pair-name: Id- + softened Denn- (d > r) + -a |
| **kael nydherd** | kael + nydherd | Kael the Counter |
| **tavow hemm** | tavow + hemm | Eldhythe |
| **cemm hyll** | cemm + hyll | Tidesmeet |
| **sedhnell** | sedh + nell | Fenholm |
| **lurrvard** | lurr + pard | Holtward (p > v) |
| **kethow stellath** | kethow + stell + -ath | Carnhold (the spec's broad -ath) |
| **tavow vorr** | tavow + vorr | Emberhythe |
| **grullsorth** | grull + sorth | Sandreach |
| **frennvar** | frenn + par | Rimewatch (p > v) |
| **taldow helv** | taldow + helv | Highreach |
| **sirrvell** | sirr + pell | Glasspire (p > v) |
| **kethow dhresk** | kethow + tresk | Rivenkeep (t > dh) |
| **et hosk** | et + hosk | the Title |
| **hosnoth** | hos + noth | eleven |
| **sullnoth** | sull + noth | thirteen |
| **pa relv** | pa + delv | twenty-four, 'two twelves' (d > r) |
| **pa vurr** | pa + murr | forty (m > v) |
| **lesk murr** | lesk + murr | a hundred |
| **delvoth** | delv + -oth | twelvefold |
| **et delv** | et + delv | the Twelve |
| **nel** | na + el | is not: the Hal's contraction |
| **new** | na + ew | was not |
| **yal** | gal | was: re + S gal (g > y) |

### 4.5 Every Seilrhass word, derived

**Inherited words.** From the first-tongue stem, through the Eldest speech (the stage with the stops *t* and *k*), to the living word, with the spoken form's knock.

| Seilrhass | Spoken | Sense | How it falls out |
|---|---|---|---|
| **thael** | thael | a tree | *\*tolm-i* >S2 *taelmi* >S3 *taelme* >S4 *taelne* >S5 *taele* = Eldest *taele* >S6 *thaele* >S7 *thael* |
| **thal** | thal | the neck, where life goes up into thought | *\*tal-o* >S3 *tale* = Eldest *tale* >S6 *thale* >S7 *thal* |
| **thenn** | thenn | water | *\*trenn-o* >S3 *trenne* >S5 *tenne* = Eldest *tenne* >S6 *thenne* >S7 *thenn* |
| **saen** | saen | heartwood | *\*ston-i* >S2 *staeni* >S3 *staene* >S5 *saene* = Eldest *saene* >S7 *saen* |
| **thaess** | thaess | to split | *\*trosk-i* >S2 *traeski* >S3 *traeske* >S5 *taesse* = Eldest *taesse* >S6 *thaesse* >S7 *thaess* |
| **thae** | thae | tide | *\*taw-i* >S1 *taei* >S3 *taee* = Eldest *taee* >S6 *thaee* >S7 *thae* |
| **thann** | thann | to close | *\*tann-i* >S3 *tanne* = Eldest *tanne* >S6 *thanne* >S7 *thann* |
| **rhes** | rhes | anger | *\*grest-i* >S3 *greste* >S4 *kreste* >S5 *kese* = Eldest *kese* >S6 *rhese* >S7 *rhes* |
| **var** | var | to bear, to carry | *\*par* >S4 *var* = Eldest *var* |
| **varen** | va'ren | a bearer | *\*par-ane* >S3 *parene* >S4 *varene* = Eldest *varene* >S7 *varen*. *keeps the old agent ending \*-ane* |
| **aeth** | aeth | a shore | *\*odh-i* >S2 *aedhi* >S3 *aedhe* >S4 *aethe* = Eldest *aethe* >S7 *aeth* |
| **vaere** | vae're | still water | *\*waʔr-ai* >S1 *waere* >S4 *vaere* = Eldest *vaere*. *the final -e is the long e of the old \*-ai, which did not fall* |
| **vael** | vael | grain | *\*waʔl-i* >S1 *waeli* >S3 *waele* >S4 *vaele* = Eldest *vaele* >S7 *vael* |
| **rhann** | rhann | heavy, great | *\*krann-i* >S3 *kranne* >S5 *kanne* = Eldest *kanne* >S6 *rhanne* >S7 *rhann* |
| **rheil** | rheil | to stop, to cease | *\*kul-i* >S2 *keili* >S3 *keile* = Eldest *keile* >S6 *rheile* >S7 *rheil* |
| **seth** | seth | a carving | *\*sketh-i* >S3 *skethe* >S5 *sethe* = Eldest *sethe* >S7 *seth* |
| **neis** | neis | soft light | *\*mus-i* >S2 *meisi* >S3 *meise* >S4 *neise* = Eldest *neise* >S7 *neis* |
| **rhel** | rhel | frost | *\*xwrel-i* >S3 *xwrele* >S4 *kvrele* >S5 *kele* = Eldest *kele* >S6 *rhele* >S7 *rhel* |
| **veas** | veas | to die | *\*feʔs-i* >S1 *feasi* >S3 *fease* >S4 *vease* = Eldest *vease* >S7 *veas* |
| **veath** | veath | night | *\*feʔth-i* >S1 *feathi* >S3 *feathe* >S4 *veathe* = Eldest *veathe* >S7 *veath* |
| **nael** | nael | mist | *\*molt-o* >S2 *maelto* >S3 *maelte* >S4 *naelte* >S5 *naele* = Eldest *naele* >S7 *nael* |
| **senn** | senn | beneath, under | *\*senn-i* >S3 *senne* = Eldest *senne* >S7 *senn* |
| **thein** | thein | to hold | *\*tum-i* >S2 *teimi* >S3 *teime* >S4 *teine* = Eldest *teine* >S6 *theine* >S7 *thein* |
| **ranth** | ranth | a word (a spoken thing, which can break) | *\*brant-i* >S3 *brante* >S4 *vrante* >S5 *ranthe* = Eldest *ranthe* >S7 *ranth* |
| **renn** | renn | a mouth | *\*brenn-i* >S3 *brenne* >S4 *vrenne* >S5 *renne* = Eldest *renne* >S7 *renn* |
| **lel** | lel | a leaf | *\*xwlel-i* >S3 *xwlele* >S4 *kvlele* >S5 *lele* = Eldest *lele* >S7 *lel* |
| **rhass** | rhass | storm | *\*krask-i* >S3 *kraske* >S5 *kasse* = Eldest *kasse* >S6 *rhasse* >S7 *rhass* |
| **rhen** | rhen | stone, the mute thing | *\*xreun-i* >S1 *xreni* >S3 *xrene* >S4 *krene* >S5 *kene* = Eldest *kene* >S6 *rhene* >S7 *rhen* |
| **veinn** | veinn | to mend, to make whole | *\*weinn-i* >S1 *weinni* >S3 *weinne* >S4 *veinne* = Eldest *veinne* >S7 *veinn* |
| **lenn** | lenn | white | *\*lenn-i* >S3 *lenne* = Eldest *lenne* >S7 *lenn* |
| **ith** | ith | one | *\*itt-o* >S3 *itte* >S5 *ite* = Eldest *ite* >S6 *ithe* >S7 *ith* |
| **rhi** | rhi | from, out of | *\*xui* >S1 *xi* >S4 *ki* = Eldest *ki* >S6 *rhi* |
| **li** | li | in, at, on (place) | *\*li* = Eldest *li* |
| **ni** | ni | not (before the verb) | *\*ni* = Eldest *ni* |
| **re** | re | that | *\*re* = Eldest *re* |
| **reil** | reil | fore, front | *\*re-il* >S1 *reil* = Eldest *reil*. *soft reading of the Bar Before* |
| **es** | es | -es, the past of a verb (a particle fused after the final…) | *\*es* = Eldest *es* |
| **sa** | sa | you (one) | *\*sa* = Eldest *sa* |
| **se** | se | you (more than one) | *\*se* = Eldest *se* |
| **anth** | anth | an hour | *\*aŋ-thi* >S3 *aŋthe* >S4 *anthe* = Eldest *anthe* >S7 *anth* |
| **ael** | ael | bond, joining | *\*ol* >S2 *ael* = Eldest *ael* |
| **va** | va | I | *\*ba* >S4 *va* = Eldest *va* |
| **ve** | ve | we | *\*be* >S4 *ve* = Eldest *ve* |
| **la** | la | he, she | *\*la* = Eldest *la* |
| **le** | le | they (living) | *\*le* = Eldest *le* |
| **rha** | rha | it (a mute thing: stone, iron, the dead) | *\*xa* >S4 *ka* = Eldest *ka* >S6 *rha* |
| **rhe** | rhe | they (mute) | *\*xe* >S4 *ke* = Eldest *ke* >S6 *rhe* |
| **ra** | ra | this | *\*ra* = Eldest *ra* |
| **na** | na | to, toward | *\*ŋa* >S4 *na* = Eldest *na* |
| **thi** | thi | through, past, by way of | *\*ti* = Eldest *ti* >S6 *thi* |
| **laes** | laes | above, over | *\*loʔs* >S1 *laes* = Eldest *laes* |
| **si** | si | with | *\*si* = Eldest *si* |
| **sei** | sei | if (closes a clause) | *\*si* >S2 *sei* = Eldest *sei*. *the stressed twin of si: a clause-final word took the knock's stress* |
| **ri** | ri | against, upon | *\*ri* = Eldest *ri* |
| **rei** | rei | to go | *\*ri* >S2 *rei* = Eldest *rei*. *the stressed twin: the verb* |
| **vi** | vi | for, for the sake of | *\*wi* >S4 *vi* = Eldest *vi* |
| **vei** | vei | to give | *\*wi* >S2 *wei* >S4 *vei* = Eldest *vei*. *the stressed twin: the verb* |
| **ei** | ei | and | *\*ei* >S1 *ei* = Eldest *ei* |
| **thes** | thes | then, after that | *\*tes* = Eldest *tes* >S6 *thes* |
| **lae** | lae | (closes a question) | *\*loʔ* >S1 *lae* = Eldest *lae* |
| **vann** | vann | two | *\*pann-i* >S3 *panne* >S4 *vanne* = Eldest *vanne* >S7 *vann* |
| **raes** | raes | three | *\*ros-i* >S2 *raesi* >S3 *raese* = Eldest *raese* >S7 *raes* |
| **nal** | nal | four | *\*nal-o* >S3 *nale* = Eldest *nale* >S7 *nal* |
| **vinn** | vinn | hand | *\*wind-o* >S3 *winde* >S4 *vinne* = Eldest *vinne* >S7 *vinn* |
| **-en** | -en | plural | *\*-en* = Eldest *-en* |
| **-ea** | -ea | one of | *\*-eʔ* >S1 *ea* = Eldest *-ea* |
| **-ear** | -ear | those of (a whole people or kind) | *\*-aʔr* >S1 *aer* = Eldest *-aer* >S8 *ear* |
| **-aer** | -aer | the relic, kept in Esthaer and borrowed in Mystaeri | *\*-aʔr* >S1 *aer* = Eldest *-aer* |
| **-as** | -as | verbal noun | *\*-as* = Eldest *-as* |
| **-eth** | -eth | causative | *\*-eth* = Eldest *-eth* |
| **-e** | -e | verb: it does, it is doing (fused late) | *\*e* = Eldest *-e* |
| **-ar** | -ar | verb: it shall, it is meant to (fused late) | *\*ar* = Eldest *-ar* |
| **-en** | -en | the old agent, merged with the plural | *\*-ane* >S3 *ene* = Eldest *-ene* >S7 *en* |
| **thar** | thar | blood | *\*thar-o* >S3 *thare* = Eldest *thare* >S7 *thar* |
| **lea** | lea | green, young | *\*lew-i* >S1 *leai* >S3 *leae* = Eldest *leae* >S7 *lea* |
| **ral** | ral | a root | *\*ral-o* >S3 *rale* = Eldest *rale* >S7 *ral* |
| **eir** | eir | deep | *\*ir-i* >S2 *eiri* >S3 *eire* = Eldest *eire* >S7 *eir* |
| **nei** | nei | silver | *\*niw-i* >S1 *neii* >S3 *neie* = Eldest *neie* >S7 *nei* |
| **ress** | ress | rot, the soft death of wood | *\*ress-i* >S3 *resse* = Eldest *resse* >S7 *ress* |
| **lanth** | lanth | a knot in the grain | *\*lanth-i* >S3 *lanthe* = Eldest *lanthe* >S7 *lanth* |
| **lenth** | lenth | winter | *\*lenth-i* >S3 *lenthe* = Eldest *lenthe* >S7 *lenth*. *the e-grade, 'the season of': the spec's own analysis* |
| **esth** | esth | fire | *\*esth-o* >S3 *esthe* = Eldest *esthe* >S7 *esth* |
| **Esthaer** | Esthaer | 'that of fire' | *\*esth-aʔr* >S1 *esthaer* = Eldest *esthaer* |
| **vath** | vath | bark | *\*wath-o* >S3 *wathe* >S4 *vathe* = Eldest *vathe* >S7 *vath* |
| **raess** | raess | sap | *\*ross-i* >S2 *raessi* >S3 *raesse* = Eldest *raesse* >S7 *raess* |
| **eil** | eil | a growth ring | *\*il-o* >S2 *eilo* >S3 *eile* = Eldest *eile* >S7 *eil* |
| **veir** | veir | wood, the living stuff | *\*wur-i* >S2 *weiri* >S3 *weire* >S4 *veire* = Eldest *veire* >S7 *veir* |
| **veis** | veis | seed | *\*wus-i* >S2 *weisi* >S3 *weise* >S4 *veise* = Eldest *veise* >S7 *veis* |
| **seil** | seil | bough, branch | *\*sul-i* >S2 *seili* >S3 *seile* = Eldest *seile* >S7 *seil* |
| **rhith** | rhith | iron | *\*kriththi* >S3 *kriththe* >S5 *kithe* = Eldest *kithe* >S6 *rhithe* >S7 *rhith* |
| **neira** | nei'ra | to sing | *\*nir-a* >S2 *neira* = Eldest *neira* |
| **rheis** | rheis | hard light | *\*kris-i* >S2 *kreisi* >S3 *kreise* >S5 *keise* = Eldest *keise* >S6 *rheise* >S7 *rheis* |
| **leis** | leis | the morrow | *\*lis-i* >S2 *leisi* >S3 *leise* = Eldest *leise* >S7 *leis* |
| **reth** | reth | ground, earth | *\*reth-o* >S3 *rethe* = Eldest *rethe* >S7 *reth* |
| **reas** | reas | wind | *\*reʔs-o* >S1 *reaso* >S3 *rease* = Eldest *rease* >S7 *reas* |
| **nith** | nith | rain | *\*niththi* >S3 *niththe* >S5 *nithe* = Eldest *nithe* >S7 *nith* |
| **enth** | enth | edge, rim, margin | *\*enth-o* >S3 *enthe* = Eldest *enthe* >S7 *enth* |
| **ves** | ves | a road | *\*gwes-o* >S3 *gwese* >S4 *vese* = Eldest *vese* >S7 *ves* |
| **lann** | lann | arm | *\*lann-o* >S3 *lanne* = Eldest *lanne* >S7 *lann* |
| **lein** | lein | brow, forehead | *\*lin-o* >S2 *leino* >S3 *leine* = Eldest *leine* >S7 *lein* |
| **neas** | neas | eye | *\*neʔs-o* >S1 *neaso* >S3 *nease* = Eldest *nease* >S7 *neas* |
| **eis** | eis | name | *\*is-o* >S2 *eiso* >S3 *eise* = Eldest *eise* >S7 *eis* |
| **enn** | enn | within, inside | *\*enn-o* >S3 *enne* = Eldest *enne* >S7 *enn* |
| **enna** | en'na | a child | *\*enn-a* = Eldest *enna* |
| **veth** | veth | door | *\*gweth-o* >S3 *gwethe* >S4 *vethe* = Eldest *vethe* >S7 *veth* |
| **sath** | sath | back, stern | *\*sath-o* >S3 *sathe* = Eldest *sathe* >S7 *sath* |
| **aven** | a'ven | other | *\*afen-o* >S3 *afene* >S4 *avene* = Eldest *avene* >S7 *aven* |
| **aenn** | aenn | open | *\*onn-o* >S2 *aenno* >S3 *aenne* = Eldest *aenne* >S7 *aenn* |
| **rhiss** | rhiss | to take, to seize | *\*griss-i* >S3 *grisse* >S4 *krisse* >S5 *kisse* = Eldest *kisse* >S6 *rhisse* >S7 *rhiss* |
| **raeth** | raeth | to kneel | *\*roth-i* >S2 *raethi* >S3 *raethe* = Eldest *raethe* >S7 *raeth* |
| **ilae** | i'lae | to live | *\*iʔl-aʔ* >S1 *ilae* = Eldest *ilae* |
| **ilen** | i'len | to lean, to incline toward (as one leans to breathe) | *\*iʔl-en-o* >S1 *ileno* >S3 *ilene* = Eldest *ilene* >S7 *ilen* |
| **nenn** | nenn | to fall, to sink | *\*nenn-o* >S3 *nenne* = Eldest *nenne* >S7 *nenn* |
| **sae** | sae | to come | *\*soʔ* >S1 *sae* = Eldest *sae* |
| **neth** | neth | to turn, to turn aside | *\*neth-i* >S3 *nethe* = Eldest *nethe* >S7 *neth* |
| **thass** | thass | to strike | *\*tass-o* >S3 *tasse* = Eldest *tasse* >S6 *thasse* >S7 *thass* |
| **seinn** | seinn | to hear | *\*seinn-i* >S1 *seinni* >S3 *seinne* = Eldest *seinne* >S7 *seinn* |
| **thaval** | tha'val | to hunt, to go for | *\*tafall-o* >S3 *tafalle* >S4 *tavalle* >S5 *tavale* = Eldest *tavale* >S6 *thavale* >S7 *thaval* |
| **saess** | saess | hunger | *\*soss-i* >S2 *saessi* >S3 *saesse* = Eldest *saesse* >S7 *saess* |
| **senth** | senth | dread, fear | *\*senth-o* >S3 *senthe* = Eldest *senthe* >S7 *senth* |
| **eith** | eith | hollow, empty | *\*ith-o* >S2 *eitho* >S3 *eithe* = Eldest *eithe* >S7 *eith* |
| **iss** | iss | thin, slight | *\*iss-o* >S3 *isse* = Eldest *isse* >S7 *iss* |
| **leas** | leas | swift | *\*leʔs-o* >S1 *leaso* >S3 *lease* = Eldest *lease* >S7 *leas* |
| **eiss** | eiss | so | *\*eiss-o* >S1 *eisso* >S3 *eisse* = Eldest *eisse* >S7 *eiss* |

**Words Seilrhass built for itself.** Every part is an inherited word above.

| Word | Built from | How |
|---|---|---|
| **ralen** | ral + -en | roots; the root-bond |
| **sethen** | seth + -en | carvings |
| **thaen** | thae + -en | tides (after a vowel -n) |
| **ennan** | enna + -en | children (-n after a vowel) |
| **aelthar** | ael + thar | bond-blood: the rite |
| **aelvaren** | ael + varen | the Bearer of the Binding |
| **aelrhen** | ael + rhen | bond-to-stone, a who-is name |
| **naelear** | nael + -ear | those of the breath |
| **naelsaen** | nael + saen | mist-hearts |
| **rhenear** | rhen + -ear | those of stone |
| **saenvael** | saen + vael | heart-grain: the Heartwood |
| **sethvaren** | seth + varen | the Standard-Bearer |
| **aelralen** | ael + ralen | the root-bond |
| **leathae** | lea + thae | the Hasty Tide |
| **vaelthae** | vael + thae | the Second Tide |
| **ralenthae** | ralen + thae | the Tide of Remembering |
| **aelthae** | ael + thae | the Joined Tide |
| **rhenthae** | rhen + thae | the Tide that Learned Deceit |
| **eirthae** | eir + thae | the Last Tide |
| **thaesaen** | thae + saen | tide-heart |
| **leavaren** | lea + varen | bearer of new branches |
| **vaelress** | vael + ress | the grain that rots |
| **ralensaen** | ralen + saen | root-heart |
| **rhenvael** | rhen + vael | stone-grain |
| **senneir** | senn + eir | the deep-beneath |
| **eirlenth** | eir + lenth | the long winter |
| **naelthar** | nael + thar | blood of the sky |
| **neivaere** | nei + vaere | the silvered |
| **seilrhass** | seil + rhass | bough-thunder: the spoken tongue |
| **eilseth** | eil + seth | ring-carving: the grain |
| **theinas** | thein + -as | a knowing |
| **naelenn** | nael + enn | home |
| **naelea** | nael + -ea | a Mystaeri |
| **aethea** | aeth + -ea | a shore-man |
| **aethear** | aeth + -ear | the shore-men |
| **rhenea** | rhen + -ea | one of stone |
| **ralthein** | ral + thein | to remember, 'root-hold' |
| **raltheinas** | ralthein + -as | a memory |
| **aelthein** | ael + thein | to trust |
| **leathein** | lea + thein | to learn |
| **theineth** | thein + -eth | to teach |
| **reith** | rei + -eth | to send |
| **neaseth** | neas + -eth | to show |
| **renneth** | renn + -eth | to goad |
| **rheileth** | rheil + -eth | to silence |
| **veaseth** | veas + -eth | to kill |
| **aelress** | ael + ress | grief |
| **rhenseth** | rhen + seth | a lie |
| **rennrhen** | renn + rhen | a gun |
| **rhenneas** | rhen + neas | the reach |
| **rhenrhass** | rhen + rhass | a stone-breaker |
| **ennas** | enn + -as | a dwelling |
| **rhenennas** | rhen + ennas | a castle |
| **eithseil** | eith + seil | straw |
| **ressveir** | ress + veir | worthless wood |
| **isseil** | iss + seil | thin wood |
| **rhannseil** | rhann + seil | the great hull |
| **thannvinn** | thann + vinn | the kept hand |
| **issralen** | iss + ralen | root-men |
| **rhasseil** | rhass + seil | the ram |
| **leasen** | leas + -en | the swift |
| **thavalen** | thaval + -en | the hunters |
| **thavalea** | thaval + -ea | a hunter |
| **seilen** | seil + -en | the host |
| **neivath** | nei + vath | silverbark |
| **neivathen** | neivath + -en | the council |
| **thaelen** | thael + -en | a grove |
| **leathael** | lea + thael | a sapling |
| **naelneis** | nael + neis | the between-light |
| **eirrhen** | eir + rhen | the mountain |
| **esthas** | esth + -as | ash |
| **rhithveir** | rhith + veir | timber |
| **rhithas** | rhith + -as | the felling |
| **tharear** | thar + -ear | kin |
| **ralear** | ral + -ear | forebears |
| **eirea** | eir + -ea | an elder |
| **aelea** | ael + -ea | a guest |
| **vethea** | veth + -ea | a host |
| **rhesea** | rhes + -ea | an enemy |
| **rhesear** | rhes + -ear | enemies |
| **sethea** | seth + -ea | a carver |
| **eirsethea** | eir + sethea | the Last Carver |
| **leisthein** | leis + thein | to hope |
| **lelneis** | lel + neis | blossom |
| **eirveir** | eir + veir | Myststone |
| **leaveir** | lea + veir | green wood |
| **eilen** | eil + -en | all; always |
| **rheissae** | rheis + sae | east |
| **rheisnenn** | rheis + nenn | west |
| **lennves** | lenn + ves | north |
| **rhesves** | rhes + ves | south |
| **vannrenn** | vann + renn | a feint |
| **sathneth** | sath + neth | a turning for home |
| **reaslel** | reas + lel | a sail |
| **naelseth** | nael + seth | a hidden thing |
| **eisranth** | eis + ranth | a soft reading |
| **rhelranth** | rhel + ranth | the soft letters |
| **vannea** | vann + -ea | the second |
| **naelsaenen** | naelsaen + -en | the pillars |
| **raltheine** | ralthein + -e | remembers: Ve raltheine, 'we remember' |
| **eisse** | eiss + -e | is (so) |

### 4.6 What the reserve roots give

The reserve roots of §3.3 derive by the same laws; their forms in that table are computed, not chosen. Two things follow for the tier-3 translation.
- **A reserve word enters as a Hal word.** When a stone leaf needs one, its Hal form is known (for the old register and the lintel's names), and so are its mutations.
- **In Seilrhass a reserve word is a root like any other.** It takes *-en, -ea, -ear, -as, -eth* and compounds by the spec's rules, and the soft reading of any new grain sign is its living form.

### 4.7 The check

- **356 derivations** from **253 inherited roots**, run by `check.py`: **0 mismatches**. Every Hal form the shoreland spec gives comes out exactly (three are emended first, §4.3), and so does every Eldest form the mystaeri spec gives (*\*thaele* as a stage of *thael*, *\*senne*).
- **Coverage:** 310 of 310 Orrowen lexicon entries (every entry of shoreland spec §4.5, §4.6 and §5, split at its ·) and 215 of 215 Seilrhass entries (all of `wf6/lang/lexicon.tsv`) are derived, directly or as a formation whose every part is derived.
- **The canon Hal texts** (the Stonwryt, the proverb) are reproduced word for word (§1.6), and so are the Title, the hearth's answer, the sliver's sentence and the Guest's words.
- **Reserve:** 371 roots; every one derives in both tongues by the same laws, and none collides with an existing word.
- **What the check cannot do:** it cannot judge beauty or originality. The reserve forms were screened against the Tolkien and franchise blacklist, the spec's rejected forms and the whole English dictionary (about 236,000 words), but a dictionary pass against Welsh, Irish and the Tolkien lexicons (shoreland spec §9c) is still owed for any reserve word before it ships.

---

## 5 · THE FIRST MARKS

### 5.1 The picture in one paragraph

The first tongue wrote with 45 marks, cut on whatever stood. Each was a small picture, and each was named by a first-tongue word. Stone took the marks to the chisel: they were worn straight and set on a bed, and then read for the first sounds of their names. A reform of the first builders then laid them out as a system of uprights and laid stones, and that system is the course-hand. Wood took the same marks into the growing tree: they were set on files and bowed by the knife, read for what they mean, and grown into new signs. That is the grain. Two marks were kept whole by both peoples: **the Fore** (a stroke crossed near its head: the Latin cross, the Bar Before) and **the Door** (two posts and a lintel: the gate mark, and DOOR).

![The first marks](ancestor/first_marks.png)

*`wf7/ancestor/first_marks.svg` (drawn by `first_marks.py`). The first hand is drawn in neither people's style: one even stroke with round ends, no chisel-foot and no knife-taper.*

![The descent of the marks](ancestor/descent.png)

*`wf7/ancestor/descent.html` (drawn by `descent.py`, using the Book's own two renderers): each first mark, then what the chisel made of it, then what the wood made of it.*

### 5.2 The marks

| # | Mark | First-tongue word | Meaning | On stone | In wood |
|---|---|---|---|---|---|
| 1 | **the Stem** | *\*tolm-* | a standing thing: a stone set up, a trunk | every consonant's upright; a letter is still called a tolm | the cut itself: GO; the trunk of TREE and RISE (thael) |
| 2 | **the Bar** | *\*hosk-* | a stone laid across; a cap | the laid stones; the sealing lintel; the long-stone | the bar and the ring-arc that lie along a ring |
| 3 | **the Fore** | *\*re-il* | the one before; first | kept whole as the foremark (proposed: the mark on the black chest, the head of the lintel column); its right arm and foot give r | kept whole: the Bar Before (reil) |
| 4 | **the End** | *\*kul-* | leave off; stop | the perpend (the stopping bar stood on the bed) | STOP (rheil); laid along the whole ring, the band-rule |
| 5 | **the Post** | *\*gann-* | a post, an upright | the pin of b d g r rh (a letter 'with its post') | the posts of DOOR |
| 6 | **the Door** | *\*gann-aʔ* | the two posts; a gate | kept whole: the gate mark (end of an oath); capped, the coping (end of a tale) | kept whole: DOOR (veth) |
| 7 | **the Curl** | *\*oð-* | the rim where one comes to rest | the broad vowels a and o (the curl laid over a short pin as a capstone) | the Wave (aeth); SHORE, the Turned Stern, HOME, FALL |
| 8 | **the Lone Mark** | *\*itt-* | this very one; one | the slender vowels i and e (a tall pin and a low stone) | the Lone Stroke (ith) |
| 9 | **the Upon** | *\*um-* | upon; (seen from below) beneath | the vowel u (two pins and a keystone raised clear) | BENEATH (senn): the two strokes grown into one |
| 10 | **the Split** | *\*krask-* | crack, break | the shore (the back-leaning upright of k g h); k | BREAK (rhass); the check of WOUND, SPENT, GRIEF; the fork (if, if not) |
| 11 | **the Course** | *\*trenn-* | a running line: a course, a stream | the offset (the stepped upright of t d n th dh s l r rh); t; the hand's own name, Garl Dhrenn | the WATER band; ROAD (two running lines); the ray |
| 12 | **the Bearer** | *\*par-* | bear up, hold up | the prop (the forward-leaning upright of p b m f v w); p | BEARER (varen): the load grown round the stroke into a laden hull |
| 13 | **the Bough** | *\*sul-* | a bough; to bend | the sibilant stones of s (the lens cut straight: one stone free above, one joined below) | HULL and BEND (seil); every curved closed shape (of wood) |
| 14 | **the Square** | *\*xreun-* | the hard thing, the set-fast; stone | rh (Hal hr): the square stood on its bed and opened | the Mute Square (rhen); every straight closed shape (of stone); the war-pith |
| 15 | **the Breath Within** | *\*molt-* | the living middle; the heart's breath | the nasal stone (the middle stone of m n ŋ) | the MIST band (a pale band through the middle of the ring) |
| 16 | **the Breathing** | *\*hoss-* | breath going out | the fricative stone (the low stone of f th h) | LIVE (ilae): a leaf on a short stalk |
| 17 | **the Sail** | *\*gwemm-* | a cloth that fills | the approximant stones of w and l (a short top stone and a free low one) | SAIL (reaslel) |
| 18 | **the Bed** | *\*loð-* | the wet bed a thing is set in | the mortar line under every word (lodh) | DEEP (eir): a cut standing on a floor-bar |
| 19 | **the Roots** | *\*ral-* | a root; what feeds from below | lost: the chisel set every mark on its bed instead | ROOT, the feet of US and STONEFOLK, the memory ray's root-hairs |
| 20 | **the Gap** | *\*onn-* | the between | the head-joint: the break in the bed between two word-stones | the Breath (aenn) |
| 21 | **the Cup** | *\*tum-* | hold, keep | lost: the stone kept the word (tum, remember) and let the mark go | HOLD (thein), OPEN, CLOSE, the palm of HAND; the seal in the bark |
| 22 | **the Drop** | *\*θar-* | blood | lost | BLOOD (thar); the Aelthar's two drops |
| 23 | **the Star** | *\*kris-* | a hard glint | lost | FLASH (rheis); the star of SPARK, HUNTER and GUN |
| 24 | **the Wedge** | *\*tass-* | a blow | the wedge mark (a pause: the blow's base kept as a free laid stone) | STRIKE (thass); the wedge of RAM; the causative chevron |
| 25 | **the Knot** | *\*lanθ-* | hold one's place, wait | lost | the Knot (lanth) |
| 26 | **the Scar** | *\*esθ-* | burn | lost | BURN (esth): a fire scar |
| 27 | **the Cut** | *\*skeθ-* | hew, cut into wood | late: the V of the softening bite | CARVE (seth); the Smoothed Cut |
| 28 | **the Lean** | *\*iʔl-en-* | lean toward | the vowel y (e's pin set leaning) | LEAN (ilen); the lean and the pair |
| 29 | **the Mouth** | *\*brenn-* | a mouth; to speak | lost | MOUTH (renn); the Two Mouths |
| 30 | **the Hand** | *\*wind-* | the whole hand | lost | HAND (vinn); five |
| 31 | **the Eye** | *\*neʔs-* | the eye; to look | lost | EYE (neas) |
| 32 | **the Seed** | *\*wus-* | a seed | lost | SEED (veis) |
| 33 | **the Sprout** | *\*taw-* | sprout, grow | lost (the stone kept the word, tev, a child) | GROW and TIDE (thae); SAPLING |
| 34 | **the Kneel** | *\*roθ-* | fold the knee | lost | KNEEL (raeth); in the Stone, 'the one they kneel to' |
| 35 | **the Bond** | *\*ol* | together, one with another | lost (the stone binds with mortar: lodh) | BOND (ael); the Aelthar's joined stems; the tie |
| 36 | **the Still** | *\*waʔr-* | stillness | lost | the STILL band (vaere) |
| 37 | **the Fade** | *\*feʔ-* | fade, go dark | lost | DYING (veas); crumbled, ROT; laid along the ring, the DARK band |
| 38 | **the Pale** | *\*lenn-* | pale-bright | lost | the WHITE band (a frost ring of short ticks) |
| 39 | **the Rim** | *\*enθ-* | a rim, an edge | lost | EDGE (enth); the ring-arc under TIDE |
| 40 | **the Tally** | *\*kail-* | a notch cut to keep a count | the numeral cap; and Kael's name | the count and ordinal bites |
| 41 | **the Gift** | *\*wi* | give; a thing set down before | lost | GIFT (vei) |
| 42 | **the Whole** | *\*weinn-* | sound, true, made whole | lost (the stone kept the word, venn, true, plumb) | MEND (veinn) |
| 43 | **the Turn** | *\*neθ-* | turn aside | lost | TURN (neth) |
| 44 | **the Blade** | *\*kriθθ-* | a hard cutting edge | lost | AXE (rhith) |
| 45 | **the Three** | *\*ros-* | three; many | lost (the stone counts with letters) | the plural: three copies abreast |

### 5.3 The laws of form

**On stone: the chisel, the first sound, and the reform.**

| Law | | What happens |
|---|---|---|
| **C1** | The chisel straightens. | A curve becomes a straight stroke or a corner; a closed curve opens into strokes; a solid is cut as its outline's base. |
| **C2** | Everything stands on a bed. | A mark is stood on the mortar line; its roots are replaced by the bed; a mark that hung or floated is set down. |
| **C3** | Stones are laid to the right. | An arm on the left of a stem is cut away; what is kept runs to the right, as a mason lays each stone against the last. |
| **C4** | Three leans. | Every upright leans forward, steps, or leans back, and nothing else. |
| **C5** | The first sound. | A mark is read for the first sound of its name (acrophony). Stone writes what is said. |
| **C6** | The laying of the letters (the reform). | The first builders' scribes made the letter of each sound out of two parts: the upright of its place, taken from the three oldest letters p, t and k; and the laid stones of its manner, taken from the mark whose name began with that kind of sound. Everything else about the old marks was let go. Like the reformed Egyptian that note 1 names, it is an economy: few strokes, laid by rule. |
| **C7** | Small marks become pinnings. | The marks read for a vowel become small loose stones set low between the ashlars, in mirrored pairs. |
| **C8** | Marks of ending and binding stay marks. | What closed or bound a line in the old hand stays outside the alphabet as punctuation: the end, the door, the bar, the tally. |

**In wood: the file, the knife, and the meaning.**

| Law | | What happens |
|---|---|---|
| **G1** | The mark goes on a file. | Its stem runs from the heart outward; whatever lay across the stem now lies along the ring; a line laid along the whole ring is a condition or a rule. |
| **G2** | The knife and the growing. | Strokes bow and taper at both ends; corners round; a closed shape stays straight only when it names a thing of stone. |
| **G3** | Meaning, not sound. | A mark is known by what it means. Its soft reading is the living word for that meaning, not the mark's old name. Wood writes what is meant. |
| **G4** | Signs grow new signs. | Marks join on one file (modifier inward) and grow parts: a lens for a thing of wood, a square for a thing of stone, a star for a flash, a wedge for a blow, a check for a hurt. |
| **G5** | Time and place. | What comes first is cut nearer the heart (a ring is an hour); who and where are files; a pause is an empty ring. |
| **G6** | The mirror. | The first tongue's 'not' was a mark turned to face the other way. The grain kept it as negation, and gave every symmetrical sign the entry-nick so that it has a mirror. |
| **G7** | The two line-qualities. | The Square and the Bough became the classifier: straight for what is of stone, curved for what is of wood. |

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

| Letter | Upright (place) | Laid stones (manner) | Note |
|---|---|---|---|
| **p** | the prop (from the Bearer, *\*par-*) | a top stone: the old letter's own laid stone | the Bearer itself: a prop under its load (\*par-, 'bear up') |
| **b** | the prop (from the Bearer, *\*par-*) | the stop + the pin (from the Post, *\*gann-*) |  |
| **m** | the prop (from the Bearer, *\*par-*) | the middle stone (from the Breath Within, *\*molt-*) | \*molt-: the Breath Within gives the nasal stone, and m is its own first sound |
| **f** | the prop (from the Bearer, *\*par-*) | the low stone (from the Breathing, *\*hoss-*) | made when Hal hw became f: hw without its free top stone |
| **v** | the prop (from the Bearer, *\*par-*) | the stop's top stone, shortened, + the fricative's low stone (built by the reform) |  |
| **w** | the prop (from the Bearer, *\*par-*) | a short top stone + a free low stone (from the Sail, *\*gwemm-*) | \*gwemm-: the Sail gives the approximant stones, and w is its own first sound |
| **t** | the offset (from the Course, *\*trenn-*) | a top stone: the old letter's own laid stone | the Course itself: a line that runs and steps (\*trenn-); the hand is named for it, Garl Dhrenn |
| **d** | the offset (from the Course, *\*trenn-*) | the stop + the pin (from the Post, *\*gann-*) |  |
| **n** | the offset (from the Course, *\*trenn-*) | the middle stone (from the Breath Within, *\*molt-*) |  |
| **th** | the offset (from the Course, *\*trenn-*) | the low stone (from the Breathing, *\*hoss-*) |  |
| **dh** | the offset (from the Course, *\*trenn-*) | the stop's top stone, shortened, + the fricative's low stone (built by the reform) |  |
| **s** | the offset (from the Course, *\*trenn-*) | a free top stone + a joined low stone (from the Bough, *\*sul-*) | \*sul-: the Bough gives the sibilant stones, and s is its own first sound |
| **l** | the offset (from the Course, *\*trenn-*) | a short top stone + a free low stone (from the Sail, *\*gwemm-*) | l shares its stones with w (both let the breath past) |
| **r** | the offset (from the Course, *\*trenn-*) | a short middle stone + the pin (from the Fore, *\*re-il*) | \*re-il: the Fore's right arm and foot; r is its first sound. The Fore itself stays whole outside the alphabet |
| **rh** | the offset (from the Course, *\*trenn-*) | the middle stone + the pin + a free top stone (from the Square, *\*xreun-*) | \*xreun-: the Square opened; Hal hr, its first sound (Rhyna's own root) |
| **k** | the shore (from the Split, *\*krask-*) | a top stone: the old letter's own laid stone | the Split itself (\*krask-, 'crack') |
| **g** | the shore (from the Split, *\*krask-*) | the stop + the pin (from the Post, *\*gann-*) | \*gann-: the Post gives the pin, and g is its own first sound |
| **h** | the shore (from the Split, *\*krask-*) | the low stone (from the Breathing, *\*hoss-*) | \*hoss-: the Breathing gives the low stone, and h is its own first sound |
| **ŋ (Hal)** | the shore (from the Split, *\*krask-*) | the middle stone (from the Breath Within, *\*molt-*) | the shore nasal; its letter died with the sound, and Seren's name keeps it (Hal SEREŊOS) |
| **hw (Hal)** | the prop (from the Bearer, *\*par-*) | a free top stone + a joined low stone (from the Bough, *\*sul-*) | the lip-sibilant; living f |
| **x (Hal)** | the shore (from the Split, *\*krask-*) | a short top stone + a free low stone (from the Sail, *\*gwemm-*) | the back approximant; living h |

**The vowels (C7).**

| Vowel | From | How |
|---|---|---|
| **a** | the Curl (*\*oð-*) | the Curl's head laid flat as a capstone over a short pin on the left (C1, C7) |
| **o** | the Curl (*\*oð-*) | the same, pin on the right: the Curl's own first sound, \*oð- |
| **u** | the Upon (*\*um-*) | two short pins and a keystone raised clear of them: the Upon, \*um-, its first sound |
| **e** | the Lone Mark (*\*itt-*) | a tall pin on the left and a low stone: the Lone Mark mirrored by the reform |
| **i** | the Lone Mark (*\*itt-*) | a tall pin on the right and a low stone: the Lone Mark, \*itt-, its first sound |
| **y** | the Lean (*\*iʔl-en-*) | e's pin set leaning: made by the reform when the i-colouring gave the Hal its y |
| **A · O** | the Curl (*\*oð-*) | a and o with the capstone broken: the reform's empty vowel, which takes the colour of its stem |

**The marks, bites, lintels and numerals (C8).**

| Mark | From | How |
|---|---|---|
| **perpend** | the End | the End's stopping bar stood on the bed (C2) |
| **wedge (pause)** | the Wedge | the blow's base kept as a free laid stone (C1) |
| **gate (end of an oath)** | the Door | kept whole (C8) |
| **coping (end of a tale)** | the Door + the Bar | the gate capped: a course laid over it |
| **sealing lintel** | the Bar | \*hosk-, the lintel: a pair-name under one laid stone |
| **long-stone (Hal)** | the Bar | a short laid stone over an old long vowel |
| **numeral cap** | the Tally | the tally-notch set over the letter it counts (C2, C8) |
| **the bed band** | the Bed | \*loð-, the mortar line: the stone-folk's roots |
| **the head-joint** | the Gap | the break in the bed between two word-stones |
| **softening bite (V)** | the Cut | late: the living hand's own, the V of a cut |
| **nasalising bite (square)** | the Square | late: a socket cut into the bed |
| **the foremark (proposed)** | the Fore | kept whole: the first builders' mark |

### 5.5 Every grain sign, from the marks

**The seventy signs.**

| Sign | Soft reading | From the first marks | Laws | How |
|---|---|---|---|---|
| **WAVE** | *aeth* | the Curl | G1 G2 | the Curl on its file; its head bows over and breaks forward, as a crest |
| **LONE** | *ith* | the Lone Mark | G1 G2 | kept: a long cut and a short one set aside |
| **BARB** | *reil* | the Fore | G1 | kept whole: the Fore, its bar laid along the ring |
| **SPARK** | *rheis* | the Stem + the Star | G4 | a cut that ends in the Star |
| **SQUARE** | *rhen* | the Square | G7 | kept whole; the one straight closed shape among the roots |
| **MOUTHS** | *vannrenn* | the Mouth + the Mouth | G2 G4 · hollow | two mouths grown to two parallel cuts, one cut hollow: one voice is a seeming |
| **STERN** | *sathneth* | the Curl | G4 | the Curl hooked back on itself and run home beside its own stroke |
| **BREATH** | *aenn* | the Gap | G1 | the Gap on its file: two cuts and the between |
| **KNOT** | *lanth* | the Knot | G1 G2 | kept; the rings bow round it as grain flows round a branch |
| **SMOOTH** | *naelseth* | the Cut | G2 · smoothed | a bowed cut filled and smoothed: felt, not seen |
| **BURN** | *esth* | the Scar | G2 | the Scar as a charred wedge, lipped with callus where the wood grew back |
| **GO** | *rei* | the Stem | G1 G3 | the Stem on a file: a cut from the heart outward is a going |
| **STRIKE** | *thass* | the Stem + the Wedge | G4 | a cut ending in the Wedge: the blow landing |
| **BREAK** | *rhass* | the Split | G2 | the Split: the head opens |
| **WOUND** | *thaess* | the Split | G2 | the Split grown as a check, widest toward the bark |
| **TURN** | *neth* | the Turn | G2 | kept: a cut with a kink |
| **HOLD** | *thein* | the Cup | G1 | kept: the Cup cupped round the file |
| **OPEN** | *aenn* | the Cup | G4 | the Cup turned outward |
| **CLOSE** | *thann* | the Cup + the Bar | G4 | the Cup with a bar across its head |
| **MOUTH** | *renn* | the Mouth | G2 | kept: an open lens, joined at the foot |
| **FALL** | *nenn* | the Curl | G4 | the Curl at the foot: the head points down into the wood |
| **RISE** | *thael* | the Stem + the Bough | G4 | a cut ending in a bud (a small Bough) |
| **GROW** | *thae* | the Sprout | G2 | kept: leaves springing alternately up the stem |
| **LIVE** | *ilae* | the Breathing | G2 G3 | the Breathing: one leaf on a short stalk; breath is life |
| **DYING** | *veas* | the Fade | G2 | kept: a cut breaking into shorter and shorter pieces |
| **KNEEL** | *raeth* | the Kneel | G2 | kept: the fold that comes to rest on the ground |
| **GIFT** | *vei* | the Gift | G1 | kept: a lens set down on a bar |
| **BOND** | *ael* | the Bond | G2 | kept: two cuts that bow in and grow into one |
| **STOP** | *rheil* | the End | G1 | the End: a cut against a bar that lies along the ring |
| **MEND** | *veinn* | the Whole | G1 | kept: a line made whole with a small stone in its gap |
| **ROT** | *ress* | the Fade | G4 | the Fade crumbled into five pieces, offset |
| **AXE** | *rhith* | the Blade | G2 | the Blade: a haft running the whole space, the blade on its clockwise side |
| **CARVE** | *seth* | the Cut | G1 G2 | kept: the V of a knife-cut |
| **LEAN** | *ilen* | the Lean | G1 | kept: one cut set obliquely across the ring |
| **BEND** | *seil* | the Bough | G2 | the Bough as a single stroke, deeply bowed: bending as a bough bends |
| **BENEATH** | *senn* | the Upon | G2 G3 | the Upon read from below: a bar at the head, a cut under it that does not reach it |
| **HULL** | *seil* | the Bough | G1 | kept: the Bough is a hull |
| **BEARER** | *varen* | the Bearer + the Bough | G2 G4 | the Bearer's load grown round the bearing stroke: a hull with a cut inside |
| **THIN** | *isseil* | the Bough | G4 | a narrow Bough |
| **SPENT** | *ressveir* | the Bough + the Split | G4 | a Bough split by a check |
| **GREAT** | *rhannseil* | the Bough + the Bar | G4 | a broad Bough with a rib across it |
| **EYE** | *neas* | the Eye | G1 | kept: a short lens with tails |
| **HUNTER** | *thavalea* | the Bough + the Star | G4 | a Bough with a star at its fore tip |
| **SWIFT** | *leas* | the Bough + the Course + the Course | G4 | a short Bough with two running lines behind it: the wake |
| **BREAKER** | *rhenrhass* | the Bough + the Square | G4 | a Bough with a small Square at its fore tip |
| **RAM** | *rhasseil* | the Bough + the Wedge | G4 | a Bough with a Wedge at its fore tip |
| **ROOT** | *ral* | the Stem + the Roots | G4 | a cut ending in the Roots, reaching forward |
| **SEED** | *veis* | the Seed | G2 | kept: a small lens with two swept wings |
| **TREE** | *thael* | the Stem + the Bough + the Bough | G4 | the Stem with two boughs at two heights: \*tolm-, the standing thing, is thael, the tree |
| **PILLAR** | *naelsaen* | the Stem + the Bough + the Bough | G4 | the tree with its trunk cut solid |
| **SAPLING** | *leathael* | the Stem + the Bough + the Bough | G4 | a small tree in the outer half of its space |
| **HEART** | *saen* | the Bough | G4 | a small Bough cut solid |
| **US** | *naelea* | the Roots + the Stem + the Bough | G4 G7 | one who stands rooted, crowned with a Bough: of wood |
| **STONEFOLK** | *aethea* | the Roots + the Stem + the Square | G4 G7 | one who stands rooted, crowned with a Square: of stone |
| **HOME** | *naelenn* | the Curl | G4 | the Curl closed round on itself: the Turned Stern made whole |
| **HOMESTONE** | *naelenn* | the Curl + the Square | G4 G7 | Home drawn straight and square: a home of stone |
| **SHORE** | *aeth* | the Bar + the Curl | G1 G4 | a bar along the ring with a small Curl at its end |
| **ROAD** | *ves* | the Course + the Course | G1 G4 | two running lines: a lane |
| **EDGE** | *enth* | the Rim | G1 | the Rim, its arc following the ring at the head of its space |
| **GUN** | *rennrhen* | the Square + the Star | G4 | a Square with a Star at its head: a speaking stone |
| **CASTLE** | *rhenennas* | the Square + the Square | G4 | a large Square with a small one behind it, joined |
| **DOOR** | *veth* | the Door | G2 | kept whole; its posts battered in as old jambs lean |
| **FLASH** | *rheis* | the Star | G1 | kept: the Star alone |
| **BLOOD** | *thar* | the Drop | G1 | kept: a drop, point toward the heart |
| **GRIEF** | *aelress* | the Split | G4 | the Split as a check, its head closed over by callus: a wound the wood has grown around |
| **SAIL** | *reaslel* | the Sail | G2 | kept: a mast under a cloth bellied by the wind |
| **HAND** | *vinn* | the Hand | G1 | kept: a stem ending in an open palm |
| **TIDE** | *thae* | the Rim + the Sprout | G4 | an arc along the ring with a shoot rising from it |
| **DEEP** | *eir* | the Bed | G1 | the Bed: a cut standing on a floor-bar |
| **AELTHAR** | *aelthar* | the Drop + the Drop + the Bond | G4 | two Drops whose stems grow together: two bloods made one |

**The six condition bands** (G1: a mark laid along the whole ring).

| Band | From | How |
|---|---|---|
| **MIST** | the Breath Within | the Breath Within laid along the ring: a pale band through its middle |
| **WHITE** | the Pale | the Pale laid along the ring: a frost ring of short ticks |
| **DREAD** | the Split | the Split laid along the ring: a ring shake |
| **WATER** | the Course | the Course laid along the ring: a single waving hairline |
| **STILL** | the Still | kept: two level lines, concentric |
| **DARK** | the Fade | the Fade laid along the ring: a stain |

**The devices.**

| Device | Where it comes from | Laws |
|---|---|---|
| **file** | the first hand cut its marks round a standing thing (\*tolm-); where a mark stood round the trunk said who and where | G1 G5 |
| **ring** | the tree grew over the marks: what was cut first lies nearest the heart; a ring is an hour | G5 |
| **span** | a Stem stretched across rings: until | G5 |
| **empty ring** | a pause in the telling became a pause in time: a morrow passes | G5 |
| **ligature** | two marks on one file, modifier inward, as in the first tongue's own compounds | G4 |
| **plural ×3** | the Three: three copies abreast | G4 |
| **pair** | the Bond: two from one foot | G4 |
| **lean** | the Lean | G1 |
| **twin** | the same mark on the opposite file: likewise, on the other side | G5 |
| **negation** | the first tongue's 'not' was a mark turned to face the other way | G6 |
| **entry-nick** | added so that every symmetrical sign has a mirror | G6 |
| **hollow** | the first tongue's 'seeming' was a mark cut in outline only (\*iθ-, eith) | — |
| **smoothed** | the Cut filled and smoothed | G2 |
| **count, ordinal** | the Tally: notches on one side count, on the other side order | G4 |
| **five** | the Hand after a thing | G4 |
| **causative** | a small Wedge at the foot: the push that makes it do | G4 |
| **half size** | a mark cut small: the lesser | G4 |
| **question** | the first tongue's asking mark was a stroke left unfinished; it runs into the ring line and stops | G2 |
| **ray** | the Course along one file: the same one | G1 |
| **memory ray** | the Course running back to the heart and ending in the Roots: carried back through the roots | G4 G5 |
| **held at the root** | the Cup cupped round the pith itself | G4 |
| **ties** | the Bond thinned to a hairline: this one to that one; when this, then that | G4 |
| **fork** | the Split: if, and if not | G4 |
| **chain** | a fork ending in an older root, cut small | G4 |
| **band-rule** | the End laid along the whole ring: a movement ends | G1 |
| **war-pith** | the Square at the heart: the council's carving | G7 |
| **seal** | the Cup (HOLD) in the bark: this is held in the grain | G4 |
| **grain-arc** | the grain line itself, \*waʔl- (vael): a short hairline along the ring, in names only | G1 |
| **included bark, graft, joined piths, pale ring** | not marks but growth: what a tree does, which the grain reads | — |

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

| Stage | Form | Law |
|---|---|---|
| the first tongue | *\*swe-reŋ-o-s* | single + a sorrow that overcomes + the nominative |
| the Hal | *sereŋos* | *sw-* > *s-* (O4): the Hal's **SEREŊOS** |
| living Orrowen | *sereŋ* | the ending falls (H2) |
| living Orrowen | *seren* | *ŋ* > *n* (H4): living **Seren** |
| (in the wood's tongue) | *seren* | from the bare stem *\*swe-reŋ-o*: S3 *-o* > *-e*, S4 *ŋ* > *n*, S5 *sw-* > *s-*, S7 the final *-e* falls; spoken *se'ren* |

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
- `roots_core.py`: the 253 inherited roots, each with its Orrowen and Seilrhass words.
- `formations.py`: the names, and the words each tongue built for itself.
- `gen_reserve.py`, `gen_reserve2.py`, `reserve.json`: the 371 reserve roots, with the screens that drew them (seeded and deterministic).
- `extract.py`, `o_lex_raw.json`, `s_lex_raw.json`: both published lexicons, as data.
- `check.py`: derives everything and compares it with both lexicons (`python3 check.py`).
- `predict.py`: the would-be reflexes, with their clashes.
- `first_marks.py`, `first_marks.svg/.png/.json`: the 45 marks, the laws of form, and the letter and sign derivations.
- `descent.py`, `descent.html/.png`: the descent figure, drawn with wf6's renderers (read-only).
- `build_md.py`, `ancestor_template.md`: this file, rebuilt from the engine (`python3 build_md.py`).
