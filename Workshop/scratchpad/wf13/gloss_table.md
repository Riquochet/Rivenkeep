# The interlinear gloss: shared table (wf13)

Every gloss writer follows this file, so that the same word is glossed the same way on every page.
Authority, in order: the lexicon (`wf12/lexicon_orrowen_full.tsv`), the grammar (`wf7/orrowen_v2.md` §3, §5.10 to §5.12), the analyzer. **The analyzer's draft is only a draft.** Where it is wrong, the lexicon and the sentence decide (§9).

## 1 · The rules

1. **One gloss per word.** Keep the draft's words exactly as they are, in the same order and with the same case. Do not merge words, split them or drop any.
2. **Give the word's true meaning, in the sense the paragraph needs.** Pick among the lexicon's senses: *keth* is 'hold' or 'know', *vesk* is 'see' or 'read', *trenn* is 'course', 'line' or 'tale', *dem* is 'until', 'to' or 'for'. Never give a word a meaning it does not have just to match the English.
3. **Use plain modern English.** Write 'you', not 'thou' or 'ye', and 'said', not 'spake' or 'saith'.
4. **Use lower case**, except where the Book's English uses a capital: names, titles and God (Kael, the Keep, the Captain, the Book, God, Tide of Remembering). Do not capitalise the first word of a sentence.
5. **Gloss literally.** An idiom shows through its own words, and that is the point of the gloss (§7). *ul vimm et hellur* is 'in' 'low' 'the' 'hall', not 'under the hall'. *Doss X lom* is 'is' X 'at-me', not 'I have'.
6. **Do not gloss mutations or constructs.** Drop every `S·` and `N·`, and every `(+S)` and `(+N)`. A softened possessor is glossed as itself, with no 'of' and no possessive -'s added: *odh Halyna* is 'hearth' 'Halyna (the two)', and *nindeth Hyna* is 'fingers' 'Rhyna'.
7. **Use parentheses only for the particles that have no English word:** '(past)', '(future)' and '(question)'. The other place they appear is the pair-name label '(the two)'. They also mark the dual in 'our (two)' and 'their (two)'.
8. **Hyphenate** when a single word needs two English words that should read as one unit. This covers conjugated prepositions ('at-me', 'from-them') and coined compounds ('tide-line', 'Stone-Warden'). A verb's pronoun takes a space instead: 'I see'.
9. **Keep each gloss to a few words.** Never write '?', an empty gloss, or an analyzer tag. The checker rejects PST, REL, NEG, FUT, SG, PL, DU, 1SG, -3PL, IMP, (+N), S· and N·, and also a bare capital M or F.
10. **Gloss identical lines identically.** A line marked `dup` needs only one row.

## 2 · Verbs

**The person ending folds into the verb**, as a pronoun plus the English verb:

| Ending | Gloss | Example |
|---|---|---|
| -Om (1sg) | I … | *veskym* 'I see', *hadhom* 'I laid' |
| -ith (2sg) | you … | *dreskith* 'you part' |
| (none, 3sg) | the bare English 3rd person: 'holds', 'held', 'is'. Do not add a pronoun, because the subject (a noun, or *o*/*ey*) follows the verb | *re heth o* '(past)' 'held' 'he' |
| -An (1du) | we two … | *re hadhan o* '(past)' 'we two laid' 'it' |
| -A (3du) | they two … | *re veske Halyna* '(past)' 'they two read' 'Halyna (the two)' |
| -Ar (1pl) | we … | *resker* 'we sit' |
| -Os (2pl) | you … | *veskys* 'you see' |
| -Ant (3pl) | they … | *re hadhant galdardath* '(past)' 'they laid' 'builders' |

- **A 3sg verb with no subject anywhere in its clause** takes 'it' or 'he', as the English needs. For example, the oath's close *Ston.* is 'it stands'.
- **Tense comes from the particle before the verb, and the verb gloss shows it.** After *re*, the verb is past: '(past)' 'I saw'. After *es*, it is future: '(future)' 'I will see'. With no particle, it is present: 'I see'. After *nath* alone the verb is present (*nath hunnom* 'not' 'I hear'); *nath re* puts it in the past (*nath re vyskym* 'not' '(past)' 'I said'). After *ho*, the verb is present: '(question)' 'you remember'.
- **Imperative.** The bare stem, or stem + *-a* when speaking to many, is the English verb with '!': *Keth* 'hold!', *Vorra* 'burn!', *Orra* 'go!'.
- **-a: 3du or imperative?** A form in *-a* after *re*, *es*, *nath*, *sa* or *ho*, or with a subject, is the 3du 'they two …'. A form in *-a* that opens a command with no subject is the imperative. The analyzer often gets this wrong in both directions.
- **A noun with a person ending is that noun's verb.** *vellent* 'they sang' (*vell* song), *hossant* 'they breathed' or 'they lived', *haemerent* 'they float', *hoska* 'they two sealed', *lodhith* 'you bonded', *runnant* 'they hammered'.
- **Derived forms** are glossed as one English word, using the lexicon's word where it has one:
  - verbal noun *-Ol*: 'holding', 'going', 'telling', 'memory'
  - participle *-At*: 'laid', 'broken', 'riven', 'sealed'
  - agent *-Ard*: 'builder', 'mason', 'runner', 'scribe'
  - abstract *-Oth*: 'wholeness', 'faith', 'husbandhood'
- **The prefix *na-* folds into its word.** *nawrodhat* 'untold', *nadhum* 'forget', *nasell* 'short', *nayalat* 'nothing', *nahos* 'none', *nafedh* 'never'.

**The two verbs 'be'.** Each form is one gloss. Make it agree with its subject:

| Form | Gloss |
|---|---|
| *doss* | 'is', 'are' or 'there is'. With a person ending: *dossom* 'I am', *dossar* 'we are', *dossos* 'you are', *dossant* 'they are' |
| *ross* (*doss* after *sa*/*ho*) | 'is' |
| *re yal* | '(past)' 'was' or 'were'. With a person ending: *yalom* 'I was', *yalan* 'we two were', *yalar* 'we were', *yala* 'they two were', *yalant* 'they were' |
| *noss* | after *nath*: 'is'. After *es*: 'will be' |
| *el* (the copula) | 'is'; 'am' or 'are' to agree with its subject (*El Hemm Halvard en* 'am' 'Elder' 'Halvard' 'I') |
| *ew* | 'was' or 'were' |
| *nel* | 'is not' |
| *new* | 'was not' |

## 3 · The small words

| Word | Gloss | Rule |
|---|---|---|
| **et** | the | always, even where the English drops it |
| **re** | (past) | before a verb |
| **es** | (future) | before a verb |
| **nath** | not | |
| **ho** | (question) | 'whether' in an indirect question ("asked whether") |
| **sa** | that · who · which | the relative: 'who' for a person, 'which' or 'that' for a thing |
| **eth** | and | |
| **ell** | or | |
| **veth** | but | 'rather' when that fits. *nath … veth* = 'not' … 'but' (meaning "only") |
| **amm** | when | 'if' when the English has if |
| **somm** | while | 'as long as' when that fits |
| **tul** | yet | 'still' when that fits. *nath … tul* = 'not' … 'yet' (never "no longer") |
| **sy** | this | after a noun, or standing alone |
| **ull** | that | after a noun, or standing alone (*hy ull* 'from' 'that') |
| **vodh** | what | 'which' when asking |
| **cedh** | who | the question word |
| **gor** | every | 'all', 'each' or 'any' when the English needs it |
| **sost** | very · self | after a quality: 'very' (*hemm sost* 'very'). After a noun or pronoun: 'itself', 'himself', 'herself', 'themselves' or 'own', matching the person (*et wadh sost* 'itself', *voll so sost* 'own'). 'even' when the English has even |
| **hos** | one | 'someone' or 'anyone' when the English needs it. *gor hos* = 'every' 'one' |
| **hosen** | as · like | 'as' before a clause, 'like' before a noun, 'equal' or 'same' when it means that |
| **hosel** | alone | 'only', 'lone' or 'single' by sense (*Stinel Hosel* 'Stroke' 'Lone') |
| **ullen** | other | 'another' or 'the rest' by sense. **Never** 'of rivers' (§9) |
| **galat** | thing | 'anything' or 'something' by sense. *yalat* (softened) is the same word |
| **nayalat** | nothing | |
| **nahos** | none | 'no one' when that fits |
| **nafedh** | never | |
| **fedh** | time | 'ever' as an adverb |
| **pana** | both | |

## 4 · Pronouns

**Where the pronoun stands decides the gloss.** Right **before a noun** (which it mutates), it is the possessive: *o dholm* 'its' 'stone', *ol varn* 'our' 'home'. **Right after a verb**, it is the subject: *re rarr o* '(past)' 'came' 'he'. **After the subject**, or after a verb whose ending already shows the person, it is the object: *Re ryt Seren Pa Luth o* ('(past)' 'wrote' 'Seren' 'Two' 'Inks' 'it'), *Kethym so* 'I hold' 'them'. Where the mutation cannot show (the next word begins with *f v w th dh s h l r n* or a vowel), read the English.

| Word | Subject | Object | Possessive |
|---|---|---|---|
| **en** | I | me | my |
| **tho** | you | you | your |
| **o** | he · it | him · it | his · its |
| **ey** | she | her | her |
| **olna** | we two | us two | our (two) |
| **ol** | we | us | our |
| **va** | you | you | your |
| **sona** | they two | them two | their (two) |
| **so** | they | them | their |

## 5 · Prepositions, and the prepositions with a person ending

| Word | Gloss | Senses to pick from |
|---|---|---|
| **ul** | in | 'into', 'within' |
| **um** | on | 'upon' (always in an oath: *Rytom um* 'I swear' 'upon'), 'over', 'across', 'about' |
| **lo** | at | 'by', 'with', 'to' (for the one who receives: *Hebb et tolm lom* 'give!' 'the' 'stone' 'to-me'). Always 'at' in the "have" and "can" idioms |
| **hy** | from | 'out of', 'off', 'than' (after a comparison) |
| **dem** | until | 'to' or 'as far as' (motion), 'for' (purpose) |

A preposition with a person ending is hyphenated as **preposition-pronoun**, using the sense the preposition has in that sentence:

| Ending | | lo | um | ul | hy | dem |
|---|---|---|---|---|---|---|
| 1sg | me | lom 'at-me' | umom 'on-me' | | | |
| 2sg | you | loth 'at-you' | umoth | | hyoth 'from-you' | |
| 3sg m | him · it | lo 'at-him' (*lo* with no noun after it) | umo 'on-him' | ulo 'in-it' | hyo 'from-it' | demo 'to-it' or 'for-it' |
| 3sg f | her | loy 'at-her' | umoy | uloy 'in-her' | hyoy | demoy |
| 1du | us two | lona 'at-us-two' | umona | | | |
| 1pl | us | lor 'at-us' | umor | | hyor 'from-us' | demor |
| 2pl | you | los 'at-you' | umos | | hyos | demos |
| 3pl | them | lont 'at-them' | umont 'on-them' | ulont | hyont 'from-them' | |
| 3du | them two | lonta 'at-them-two' | umonta | ulonta | hyonta | |

*hyo* after a verb of going, with no "from" sense, is the lexicon's adverb 'out'.

## 6 · Nouns and numbers

- **Plural *-Ath* is the English plural:** 'stones', 'hands', 'men' (*uldath*), 'True Men' (*vennuldath*). Use the irregular plurals the lexicon gives: *tevath* 'children', *tolmath* 'stones' (or 'stonework' where the English says so), *trenneth* 'tales' or 'courses', *flennath* 'Book' (§8).
- **After a numeral, use the English plural**, even though the Orrowen noun stays singular: *pa yarl* 'two' 'hands', *sull brod* 'three' 'words'.
- **Use the lexicon's English word for a compound.** For example, *helvhoss* 'wind', *meskdhrenn* 'grain', *gorndholm* 'cornerstone'. Hyphenate only when English has no single word (*hylldhrenn* 'tide-line').
- **Numbers.** Each numeral is glossed as its own number, so counting in twenties shows:

| Orrowen | Gloss |
|---|---|
| *hos · pa · sull · gemm · lesk* | 'one' · 'two' · 'three' · 'four' · 'five' |
| *vran · dhom · thell · rost · noth* | 'six' · 'seven' · 'eight' · 'nine' · 'ten' |
| *hosnoth · lesknoth* | 'eleven' · 'fifteen' |
| *delv · murr · bost* | 'twelve' · 'twenty' · 'four hundred' |
| *pa vurr* | 'two' 'twenties' |
| *lesk murr* | 'five' 'twenties' |
| *pa relv* | 'two' 'twelves' |

  - **Ordinals:** *hosast* 'first', *pawast* 'second' (or 'again' as an adverb), *sullast* 'third', *vranast* 'sixth', *gemmnothast* 'fourteenth'.
  - ***et Delv*** is 'the' 'Twelve'.

## 7 · Idioms: gloss each word, never the idiom

| Orrowen | Glosses | It means |
|---|---|---|
| *Doss X lom* | 'is' X 'at-me' | I have X |
| *Doss* VN *lom* | 'is' 'holding' 'at-me' | I can hold |
| *Doss X umom* | 'is' X 'on-me' | I feel X |
| *ul vimm X* | 'in' 'low' X | under X (*vimm* is always 'low') |
| *dem vimm* · *dem susk* | 'to' 'low' · 'to' 'high' | down · up |
| *ul sestow* | 'in' 'back' | behind |
| *ul lern* | 'in' 'face' | before, in front |
| *hy vodh* | 'from' 'what' | because, for · why |
| *ul vodh* | 'in' 'what' | where |
| *amm vodh* | 'when' 'what' | when? |
| *hy ull* | 'from' 'that' | then, since |
| *dem sy* | 'until' 'this' | so far |
| *amm sy* | 'when' 'this' | now |
| *vess sy* | 'night' 'this' | tonight |
| *hos um ullen* | 'one' 'on' 'other' | on one another |
| *hy ullen* | 'from' 'other' | apart |
| *hos eth hos* | 'one' 'and' 'one' | one by one |

## 8 · Names

- **A person gets the Book's English name:**
  - *Wik* 'Wick', *Yory* 'Jory', *Merrik* 'Merrick'.
  - Every other name is spelled as written: Seren, Halvard, Rhyna, Kael, Voss, Tarnel, Tarnard, Brenn, Della, Enno…
- **A mutated name** gets its base name: *Hyna* 'Rhyna', *Wrenn* 'Brenn', *Dharnel* 'Tarnel', *Dharnard* 'Tarnard', *Horlen* 'Corlen', *Rella* 'Della'.
- **Pair-names (one name for two)** are 'Halyna (the two)', 'Aldwena (the two)', 'Idrenna (the two)', 'Orvenna (the two)', 'Enrella (the two)' and 'Wendhessa (the two)'. Names that end in *-a* for one woman are not pair-names: Rhyna, Della, Penna, Ebba, Denna, Bena.
- **The hearth's answer:** *Tumar* is always 'we-remember'. It is the hearth's word and Orrowen's "yes". The other persons of *tum* are ordinary verbs: *tumant* 'they remember'.
- **Titles and God:**

| Orrowen | Gloss |
|---|---|
| *Mardh*, *Vardh* | 'God' |
| *Crenn* | 'Captain' for the Captain; 'captain' otherwise |
| *Ketherd* | 'Commander' |
| *Kesterd* | 'Corporal' |
| *Crennel* | 'Sergeant' |
| *Hemm* before a name | 'Elder' |
| *Hemma* | 'Elderess' |
| *Lodhan* | 'Bonded' |
| *Stonwrytan* | 'guild' or 'Stonewrights' (follow the English) |
| *stonwrytel* | 'Stonewright' |
| *Stonwryt* | 'Stonwryt' |
| *Treskan* | 'Rivenmen' |
| *Orrowan* | 'Shorelanders' |
| *Mystaeri* | 'Mystaeri' |
| *Orrow* | 'Shore' (the Shorelands); 'shore' for any coast |
| *orrowen* | 'Shoreland' as an adjective; 'Orrowen' as the tongue's name |
| *flennath* | 'Book' |
| *Tolmvard* | 'Stone-Warden' |
| *Seren Pa Luth* | 'Seren' 'Two' 'Inks' |

- **Places.** A one-word place gets its English name:
  - *Sedhnell* 'Fenholm', *Lurrvard* 'Holtward', *Grullsorth* 'Sandreach', *Frennvar* 'Rimewatch', *Sirrvell* 'Glasspire', *Mystow* 'Mystlands'.
  - A two-word place gets each word's meaning, capitalised, so the English name can be seen in it:

| Orrowen | Gloss | The Book's name |
|---|---|---|
| *Kethow Dhresk* | 'Keep' 'Riven' | Rivenkeep |
| *et Kethow* | 'the' 'Keep' | (*kethow* for any other hold is 'keep' or 'hold') |
| *Tavow Hemm* | 'Harbour' 'Old' | Eldhythe |
| *Tavow Vorr* | 'Harbour' 'Fire' | Emberhythe |
| *Cemm Hyll* | 'Meeting' 'Tide' | Tidesmeet (also *Gemm Hyll* after *ul*/*dem*) |
| *Kethow Stellath* | 'Hold' 'Cairns' | Carnhold |
| *Taldow Helv* | 'Tower' 'Sky' | Highreach (also *Dhaldow Helv*, softened) |

- **Epithets** are glossed by meaning, in lower case: *Corlen Dhavow* 'Corlen' 'harbour'; *Harl Orrow sa Vorr* 'Harl' 'Shore' 'that' 'burns'; *Lanner Gynten* 'Lanner' 'crags'; *Kael Nydherd* 'Kael' 'Counter'.
- **Titles of works and tides** are glossed word by word, capitalised as the English has them: *Hyll Dhumol* 'Tide' 'Remembering', *Odh Sell* 'Hearth' 'Long'.
- **Hal (all-capital) words** do not occur on these pages. If one does, gloss it as its living word.

## 9 · Where the analyzer's draft is wrong

| Draft | Correct gloss |
|---|---|
| ***Kael*** 'tally-notch' | always 'Kael' (the man). Lower-case *kael* = 'notch' |
| ***Hethow*** 'spring-place' (*Ketherd Hethow Dhresk*, *Trenneth Hethow Dhresk*) | 'Keep' (softened *Kethow*) |
| ***Gemm*** 'meet' in *Gemm Hyll* | 'Meeting' (Tidesmeet). *Gemm* as a count, or as a Book number before a title (*Gemm · Hyll Lodhat*), is 'four' |
| ***Hethyleth*** 'spring-…' (*Flennath Hethyleth*) | 'Knowings' |
| ***ullen*** 'of rivers' | 'other' or 'another' |
| ***hummoth*** 'haven-…' | 'husbandhood' |
| ***marrol*** 'guest-…' | 'shifting' or 'trembling' |
| ***mummol*** 'nose-…' | 'smelling' |
| ***yarlelath*** | 'tools' (*garlel*, 'a tool') |
| ***dreskyl*** · ***dreskith*** | 'tearing' · 'you part' |
| ***veskyl*** 'tree-…' | 'sight' |
| ***nafedh*** 'un-time' | 'never' |

**Words with two readings** (pick one by what comes before and by the English):

| Word | Reading 1 | Reading 2 |
|---|---|---|
| *vess* | 'night' | after *re*/*sa*/*ho*: 'asked' or 'ask' |
| *heth* | after *re*/*sa*: 'held' or 'holds' | 'spring' (the season) |
| *hemm* | 'old' · 'Elder' · 'elder' | after *re*: 'met' |
| *dhess* | 'answered' | 'dawn' |
| *hedh* | 'dusk' | 'who' |
| *wemm* | 'lifted' | 'sail' |
| *bynt* | 'narrow' | 'quick' |
| *nend* | 'watch' | 'wild' |
| *vedh* | 'shot' | 'whisper' |
| *nask* | 'eat' | 'end' |
| *ryssyth* | 'breadth' | 'strangeness' |

The 3du or imperative question for *-a* forms is settled in §2.

## 10 · The common content words

Use the first gloss; the others are alternatives for when the English needs them.

| Orrowen | Gloss |
|---|---|
| tolm | stone · letter |
| dholm | stone |
| tolmath | stones · stonework |
| hald | wall |
| lodh | mortar · bond |
| lodhat | bonded |
| hosk | lintel · capstone |
| ganna | gate · pair |
| gannath | posts |
| trenn | course · line · tale |
| dhrenn | course · line · tale |
| ryt | (noun) vow · oath; (verb) cut · wrote · swore |
| rytym | I swear (*Rytom um* …) · I cut · I wrote |
| rytet | carving · written |
| ryterd | scribe · carver |
| rellor | sign · mark |
| flenn | leaf · page |
| luth | ink |
| brod | word |
| brodh · wrodh | tell · speak; after *re*: told · spoke |
| mysk · vysk | say; after *re*: said |
| vesk | see · read |
| veskyl | sight |
| keth · heth | hold · know; after *re*: held |
| kethyl | holding · knowing |
| cadh · hadh · gadh | lay · set; after *re*: laid |
| cadhat | laid |
| orr | go · walk; after *re*: went |
| orrol | going · road · way |
| rarr | came (softened *darr*, after *re*) |
| vellor · mellor | come in · arrive |
| lymm | bring · carry |
| hebb | give |
| rik · grik | catch · take |
| hess | stop |
| ston | stand · stood |
| omm | fall |
| sol | rest · still |
| tum | remember |
| sesk | know (a fact) |
| odh | hearth |
| vorr | fire; (verb) burn |
| greller | lamp |
| varn | home |
| cumm | haven |
| kethow | keep · hold |
| reskow | place · seat |
| mesk | tree · wood |
| meskdhrenn | grain |
| hyll | tide |
| wadh | sea |
| myst | grey · sea-fog · mist |
| helvhoss | wind |
| helv | sky |
| orrow | shore |
| sulter | boat |
| sceth | ship |
| vess | night |
| orl | day |
| ryst | morning |
| hedh | dusk |
| fedh | time |
| surr | year |
| grem | winter |
| syst | summer |
| heth | spring (the season) |
| nynth | spring (of water) · water |
| uld | man |
| uldath | men |
| tev | child |
| tevath | children |
| garl · yarl · narl | hand |
| sest | shoulder |
| sestow | back · stern |
| lern | face · front · shape |
| molt | heart · middle |
| hoss | breath |
| voll | name |
| crenn | captain |
| stinel | stroke |
| saed | half · part |
| nydhyl | count · list |
| hemm | old |
| tevel | young |
| susk | high · tall |
| vimm | low |
| sell | long |
| strom | great |
| lyss | small |
| mest | much · many |
| merr | few |
| niss | slow |
| domm | black · dark |
| venn | true |
| tunn | whole |
| dasken | last · final |
| neld · deld | far |
| virr | near · nearly |
| loskat | filled · enough |
| treskat | riven · torn |

## 11 · Two lines, glossed

*Um et hald veskym et movenn ul memmyl, ul helvhoss sa nath hunnom.*
on · the · wall · I see · the · banner · in · lifting · in · wind · that · not · I hear

*Re ryt Seren Pa Luth o, ryterd et flennath sy, eth sullast odh Halyna.*
(past) · wrote · Seren · Two · Inks · it · scribe · the · Book · this · and · third · hearth · Halyna (the two)
