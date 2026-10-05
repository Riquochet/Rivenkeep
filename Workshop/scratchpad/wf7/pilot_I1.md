# RIVENKEEP · PILOT I.1 · *COVV TRESKAT*, THE TORN CLOAK, IN ORROWEN

*wf7 workflow document, 2026-09-27. Not a Book leaf and not a repo doc. The first stone leaf of tier 3 (Jack's note 5, "the WHOLE Book in its own tongues"): I.1 whole, as Seren writes it in her ink. Built on `wf7/orrowen_v2.md` (grammar §3, the stone grammar §3.11, samples §11), `wf7/lexicon_orrowen.tsv`, `wf7/ancestor.md` and the Book (`wf6/legends_v12.md`, lines 154–225). A proposal for Jack; no canon text changes.*

**What is here.**
- **The whole leaf in the leaf-hand register** (*Garl Flenn*, the ink hand): Seren's headnote, Kael's telling, the Title, the True Men's verse, the hearth's answer and the facing leaf. The ink writes the whole tongue: every mortar word, every ending, every mutation (Jack's note 1: "the later written language would have to be able to be written quickly like English if the smaller words were included").
- **The Title three ways:** in coal (the Captain's letters, every word), in Seren's leaf-hand, and **cut dry** (the chisel register: 17 signs, the mortar words left out).
- **21 lexicon additions**, each derived by the lexicon's own rules, appended to `lexicon_orrowen.tsv` (list at the end).
- **The check.** `python3 orr_analyze.py --file pilot/i1_draft.txt` reads every line of the leaf (72 lines, 1,020 words after the back-translation fixes) and reports **0 unknown and 0 ill-formed** words (exit status 0). `--test` still passes all 87 samples of `orrowen_v2.md` with the additions in place. The romanised text is kept line by line in `wf7/pilot/i1_draft.txt`; the analyzer's full report is `wf7/pilot/i1_report.txt`.
- **The back-translation.** A blind back-translation (`wf7/backtrans_I1.md`) read the Orrowen back into English without the English; seven lines were corrected where the Orrowen said something else (marked *Back-translation fix* below), three lexicon rows were mended, and §3.5, §3.6, §3.8 and §5.10 of `orrowen_v2.md` gained a clarifying line each.
- **The length.** 1,020 words of Orrowen (1,012 before the fixes) against about 1,080 in the Book's English for the same text: written whole, small words and all, the ink runs about as long as English, which is what note 1 asks of the later hand. Of the 1,020, 827 land on canon words, 96 on reserve roots, 97 on tier-3 words.

**How to read the blocks.** Each paragraph is given as the Book spells Orrowen (romanised; the leaf-hand writes this, bites and harmonic letters included), then **the Book's English exactly as it stands** (Seren's translation, unchanged), then a *word-for-word* line where the Orrowen is built differently from the English. Canon Orrowen (the Title, *Tumar*, Seren's line, *Covv Treskat*, *Kael Nydherd*, *Rytom um …*, *Ston.*) is used exactly as `orrowen_v2.md` gives it.

---

## THE LEAF

### Title

> ## *Covv Treskat*

**I.1 · The Torn Cloak**

*The riven cloak.* (*treskat* is canon: one word for torn, riven, cleft; the canon keeps its broad ending.)

### Seren's headnote

> *Re hadh Crennel Kael, Kael Nydherd, rytvard et vennuldath, ul et vess hosast sa re vess et odh sy trenn. Nath re lusk o lom kylyl wrod hyo, eth nath re hylym.*

*Laid by Sergeant Kael, Kael the Counter, oath-keeper of the True Men, on the first night this hearth asked for a tale. He would not let me change a word of it, and I have not.*

Word for word: *Laid Sergeant Kael, Kael the Counter, oath-keeper of the True Men, on the first night that this hearth asked a tale. He did not allow me a changing of a word of it, and I did not change.*

- The headnote is active (*Re hadh Crennel Kael*, "Sergeant Kael laid"): *cadhat lo X* would mean "laid **for** X", as in the lexicon's *cadhat lom*, "laid for me".
- ***vess … vess***: "night" and "asked" (*re* + S *pess*) sound the same, the canon's own homophony (lexicon §8.2). Seren lets it stand.
- *and I have not* is Orrowen's yes-and-no rule: the verb is said again, *nath re hylym*, "I did not change".

### Kael's telling

> Hebb et tolm lom. Nath reskym; es stonom. Re reskym loskat grem sy.

Give me the stone. No, I will stand. I have sat enough this winter.

Word for word: *Give the stone at me. I do not sit; I will stand. I sat enough this winter.* Orrowen has no "no": a man offered a seat refuses it by saying the verb back, *Nath reskym*.

> Rytom um hosk et bystir rerdsennen, sa re rytent et pardath hemm so vollath umo: es gadhom sy venn, hy vodh nath noss cadhol ullen lom. Ston. Re yalom um et ganna orl ull. El nydherd yalatath en, nel vellerd; eth galat sa nath re nydhym, nath gadhom o los.

I swear on the lintel of the western stair, where the old wardens cut their names, that I will tell this plain, for I have no other way of telling. I was on the gate that day. I am a counter of things and not a singer, and what I did not count I will not tell you.

Word for word: *I cut [my word] upon the lintel of the western stair, that the old wardens cut their names upon it: I will lay this plumb, for no other laying is at me. It stands. I was on the gate that day. A counter of things am I; not a singer; and a thing that I did not count, I do not lay it for you.*

- **The oath is the canon's:** *Rytom um hosk…* (`orrowen_v2` §3.9 gives this very opening as Kael's), and it closes with ***Ston.***, "It stands", as every oath does. This is the one word of the leaf that Seren's English does not carry: English "I swear … that" renders the whole frame. **[Jack]**, see note 1 below.
- ***es gadhom sy venn***, "I will lay this plumb". To tell a tale is to lay a course, and *venn* is "true, plumb, plain": a plain telling is a true course. *Cadh* is used here, not *brodh*, because the future's bedding would turn *brodh* into *mrodh*, an onset the tongue does not allow.
- ***rytent … ryt***: the wardens *cut* their names, Kael *cuts* his oath: one verb.
- ***nath gadhom o los***, "I do not tell it you": Kael's rule, said as a habit, not a promise.

> Re vellor et trenn ul hedh, eth re nydhym o somm re vellor o: uldath hemm, eth essath lo havulath, eth tevath ul naedh um so visketh, eth hesperdeth vran kest cresket, sa re vammant so hrenneth. Lesk bost eth merr lesk murr. Re orrar bress dem gethow, eth re vellorar tolmstell. Re heth hos brellir et ganna hyvenn. Re yal linth dem et gerd ul et parow ul sestow. Re hadhant et velleth hellur strom lo ull, veth re yal crisur ommat, eth sulv um et odh sa reskys lo amm sy.

The column came in at dusk, and I counted it as it came: old men, and women with bundles, and children asleep on their feet, and soldiers of six broken companies who no longer knew their officers. Two thousand and some hundreds. We had walked a month to reach a castle, and we reached a heap of stones. The outer gate hung from one hinge. The ward behind it was grass to the knee. Where the songs had put a great hall there was a roof fallen in, and snow on the hearth where you sit now.

Word for word: *The column came in at dusk, and I counted it while it came in: … soldiers of six broken companies, who had lost their captains. Five four-hundreds and some five-twenties. We walked a month to a keep, and we came in to a heap of stones. One hinge held the outer gate. There was grass to the knee in the ward behind. The songs had laid a great hall there, but there was a roof fallen, and snow on the hearth that you sit at now.*

- ***trenn*** is the column, and the course, and the tale: the people come in as a course is laid.
- ***mellor*** "come in, reach" carries both ends of the march: *re vellor et trenn* … *re vellorar tolmstell*.
- **Two thousand** is *lesk bost*, "five four-hundreds": the Shore counts in twenties, and Kael counts in the Shore's way.
- ***Re heth hos brellir et ganna hyvenn***, "one hinge held the outer gate": the gate is kept (*keth*) by one hinge. *brellir* is "a joint between stones; a hinge".
- ***Re hadhant et velleth***, "the songs had laid": the songs, too, lay stones.
- ***sa re vammant so hrenneth***, "who had lost their captains" (*mamm* "lose", softened after *re*). *(Back-translation fix.)* The first draft said *nath re seskent tul*, meant as "knew no longer"; but *nath … tul* is "not yet" (Seren's own line, *Nath noss tul kethyl*), and a blind reader heard "who did not yet know their captains".

> Re varrant merr. Re semment merr. Re ommant merr, eth nath re dhaldant.

Some shook. Some wept. Some fell and would not rise.

> Hy ull re dhald et carmol, eth new hos carm. Re harmant merr: Luska dem wemmeth myst, eth pessa haethil! Veth re hyrril nahos fedh hos brod sa re vyskent et wemmeth myst. Re harmant merr: Dem et hiskenneth susk, eth et sulv ul neld! Re harmant merr: Orra dem vimm ul nyrulath et Kethow, eth hoska et gebbeth, eth tovva! Hosen amm es nadhum et wadh ol. Re hunnom uldath ul greskyl, fedheth. Nath re hunnom fedh lunt ul greskyl. El hunnat hosen crest hull ul morrol.

Then the crying began, and it was not one cry. Some cried that we should send to the grey sails and beg for terms, though no one had ever understood a word the grey sails said. Some cried for the high passes and the snow beyond them. Some cried that we should go down into the cellars of the Keep and bar the doors and wait, as if the sea would forget us. I had heard men break before. I had never heard a people break. It is a sound like ice going out on a river.

Word for word: *Then the crying rose, and it was not one cry. Some cried: Send to the grey sails, and beg terms! But no one ever understood one word that the grey sails said. Some cried: To the high passes, and the snow beyond! Some cried: Go down into the cellars of the Keep, and lintel the doors, and wait! As if the sea would forget us. I had heard men in breaking, at times. I had not ever heard a people in breaking. It is a sound like river-ice in going.*

- **The cries are quoted, not reported.** Orrowen has no word for "that" before a clause; a crowd's cries are given as they were cried, in the imperative plural (*Luska*, *pessa*, *Orra*, *hoska*, *tovva*).
- ***hoska et gebbeth***, "lintel the doors": to bar a door is to lay its lintel, *hosk*, the same word as the Title (*et Hosk*).
- ***hosen amm***, "as when", is "as if" (an addition).
- ***re hyrril nahos fedh***, "no one ever understood": *fedh* "ever" carries the English "ever" (back-translation fix: without it the line said only that no one understood them that day).
- ***uldath ul greskyl***, "men in breaking", is the progressive of §3.4 (*ul* + a verbal noun), as *Doss et hald ul glennol*.
- ***crest hull***, "the ice of a river" (*rhull*, softened as possessor), *ul morrol*, "in going" (*orrol*, nasalised after *ul*).
- *The crying began* is *re dhald et carmol*, "the crying rose": the reserve *mosk* "begin" is the known trap of lexicon §8.2 (it sounds like the Creed's *mosk*).

> Amm sy myskym los vodh ew et Crenn, eth hosast vodh new o. New crenn hesteth o, eth re yalant et crenneth hesteth hurrat. New redulard o, eth re yalant et redulardath nadhumat. New pithul o, eth re yalant et pithulath driget. New stonwrytel o, eth re resk et Stonwrytan ul linth, eth so wresketh ul so simmeth, eth re nasaemal. Ew crenn hest lyss o, eth ew o hest ol. Re wesk o ol hos eth hos, ul gesteth eth um orrolath, dem nelv; eth re heth o ol lo nayalat veth osk. Ew hesperdeth ol, sa re hether ol ryteth, sa re yaldar galat sa re dhragular, sa nath re yorrar veth amm ew venn et dask. El gor yalat vennuld ull. Myskym o dem va seskyl: nel mest o. Veth nel lyss o.

Now I will tell you what the Captain was, and first what he was not. He was no general, and the generals were slain. He was no politician, and the politicians were forgotten. He was no nobleman, and the nobles were scattered. He was no Stonewright, and the Stonewrights sat in the grass with their chisels in their laps and despaired. He was the captain of a small company, and we were his company. He had found us one by one, in garrisons and on roads, twelve of us in all, and bound us by nothing but trust. We were soldiers who kept our oaths, who built what we promised, who fought only when the cause was just. That is all a True Man is. I say it so you will know it is not much. It is not little, either.

Word for word: *Now I tell you what the Captain was, and first what he was not. He was not a captain of companies, and the captains of companies were slain. He was not a councilman, and the councilmen were forgotten. He was not a lord, and the lords were flung apart. He was not a Stonewright, and the Stonewrights sat in the grass, and their chisels in their laps, and un-hoped. He was the captain of a small company, and his company were we. He found us one and one, in garrisons and on roads, up to twelve; and he held us by nothing but trust. Soldiers were we, who kept our oaths, who built the thing we promised, who did not fight but when the cause was true. That is the whole of a True Man. I say it for your knowing: it is not much. But it is not small.*

- **Three blows in one shape**, *New X o, eth re yalant et Xath Y-at*: the copula's past negative (*new*) against the state verb's past (*re yal-*), what he was not and what became of those who were. The fourth breaks the shape, as the Stonewrights broke: *eth re resk et Stonwrytan ul linth*.
- ***eth so wresketh ul so simmeth***, "and their chisels in their laps": the clause with no verb, laid beside the other with *eth*.
- ***hos eth hos … dem nelv***, "one and one … up to twelve": the counter's arithmetic for "one by one … twelve of us in all" (*dem* beds *delv* into *nelv*).
- ***re heth o ol lo nayalat veth osk***, "he held us by nothing but trust". *Keth* "hold, keep" is the Rite's own name for him (*Ketherd*, "the holder"); it is also the verb of *sa re hether ol ryteth*, "who kept our oaths". The reserve *bysk* "bind" would have been heard as *re vysk*, "said".
- ***El gor yalat vennuld ull***: "that is the whole of a True Man".
- ***sa nath re yorrar veth amm ew venn et dask***, "who did not fight but when the cause was true": Orrowen says "only" of a clause as *nath … veth*, "not … but", as in *lo nayalat veth osk*. *(Back-translation fix.)* The first draft had *sa re yorrar hosel amm…*, and *hosel* after a verb reads "alone": a blind reader heard "who fought alone when the end was sure", the True Men's creed turned into a last stand.
- ***pithulath driget***: *driget* is "thrown, flung, scattered" (the lexicon row now carries all three senses of *drig*; it had only "thrown", and "the nobles were scattered" came back as "the lords were thrown down").

> Nath re vaver o neskyl. Rytom um ull pawast. Ston. Gor orl et hollarol sell re dhovv o dem hos sa re yal et neskyl lo; eth re rik nahos o, hy vodh re yalant et neskerdeth sennet. Nath hyrrila en navenn. New hy vodh re yalant et uldath strom sennet. Nath re yal hos strom hyo. Nath gaeverym re hoss fedh uld hosen et Crenn.

He did not want to lead. I swear to that as well. All through the long retreat he waited for someone whose place it was to lead to take it up, and none did, for the leaders were dead. Do not mistake me. It was not that the greater men were gone. There was no greater man. I do not think his equal ever lived.

Word for word: *He did not want leading. I cut [my word] upon that a second time. It stands. Every day of the long retreat he waited for one that the leading was at him; and no one took it, for the leaders were dead. Do not understand me false. It was not because the great men were dead. There was not one greater than he. I do not think a man like the Captain ever breathed.*

- ***Rytom um ull pawast. Ston.*** "I swear upon that again. It stands." Kael swears twice in his telling, and both oaths close as oaths do.
- **"It was not that the greater men were gone. There was no greater man. I do not think his equal ever lived."** is ***New hy vodh re yalant et uldath strom sennet. Nath re yal hos strom hyo. Nath gaeverym re hoss fedh uld hosen et Crenn.***, "It was not because the great men were dead. There was not one greater than he (*hy* 'than'). I do not think a man like the Captain ever breathed." The counter still counts the greater men, and gets none. *(Back-translation fix.)* The first draft, *Nath re orrant uldath strom hyo. Nath re yal hos. Nath gaeverym re hoss fedh o hosen.*, came back blind as "Great men did not come out of him. He was not one. I do not think he ever once breathed like one": *orr … hy* is "leave, go from", so *hyo* read "from him", not "than he"; and *o hosen* read "he … like one", because *h* does not soften and nothing marked *o* as "his".
- ***sennet***, "dead", is *senn* "go out, as a fire in peace", the same word as the dead hearth below.

> Re veskent et vennuldath dem so Hrenn. Re vesk et Crenn um et hald.

The True Men looked to their Captain. The Captain looked at the wall.

- *so Hrenn*: the canon's own softening of *Crenn* (`orrowen_v2` §5.4, "S *Hrenn*").

> Hy ull re yyst o. Re rik brenth hy et odh sennet somm re orr o lo dhrenn et hellur, eth nath re seskym hy vodh. Re orr o dem susk um lern gask et hald ulvenn, hosel, lo dhrenn et tolmath sa re dhaldant hy et lodh; eth re stonar lo visk, eth re luskar o, hy vodh nath re vysk o lor: Fenna. Lo wisk, ul vodh re ston et hald tunn tul, re nahovv o hovv. Ew hosel covv hesperd o, lorr hos fedh, eth kylet ul vesket vorrdholm hemm. Re dhresk o lo dhrenn o sestow. Re rik o hagess hy et gask, eth re yal saed et covv bysket umo. Hy ull re lumm o um et hoskath lo et brenth, eth re ryt, niss, hosen ryt uld sa nath re ryt mest.

Then he climbed it. He had taken a coal from the dead hearth as he came through the hall, and I did not know why. He went up the broken face of the inner wall alone, by the stones that stood proud of the mortar, and we stood at the foot and let him, for he had not told us to follow. At the top, where the wall still stood whole, he took off his cloak. It was a plain soldier's cloak, crimson once and gone to the colour of old brick. He tore it down the back. He took a pike out of the rubble and bound the half of it there. Then he knelt on the capstones with the coal, and wrote, slowly, as a man writes who has not written much.

Word for word: *Then he climbed it. He took a coal from the gone-out hearth while he went through the hall, and I did not know why. He went up the broken face of the inner wall, alone, by the stones that rose out of the mortar; and we stood at the foot, and let him go, for he had not said to us: Follow. At the top, where the wall still stood whole, he un-cloaked his cloak. It was only a soldier's cloak, crimson once, and changed into the colour of old brick. He rived it along its back. He took a pike from the rubble, and the half of the cloak was bound upon it. Then he knelt upon the capstones with the coal, and wrote, slowly, as writes a man who has not written much.*

- ***re yyst o***: *gyst* "climb", softened after *re*: the *g* becomes the glide *y* before the vowel *y*, /jyst/, exactly by §3.3.
- ***et odh sennet***, "the gone-out hearth": *senn* is to go out as a fire goes out in peace.
- ***sa re dhaldant hy et lodh***, "that rose out of the mortar": a mason's "stood proud".
- ***eth re luskar o***, "and we let him go": *lusk*, "loose", the Captain's own third call.
- ***re nahovv o hovv***, "he un-cloaked his cloak": *na-* + *covv* "wear", the reversative (an addition), as *nahadh* "unlay".
- ***Re dhresk o***, "he rived it": the verb of *Covv Treskat* and of *Kethow Dhresk*.
- ***eth re yal saed et covv bysket umo***, "and the half of the cloak was bound upon it". The active *re vysk* "bound" would sound as *re vysk* "said"; the passive keeps it clear. *(Back-translation fix.)* The first draft had *re yal o saed bysket*, "its half"; but *s* does not soften, so nothing marks *o* as "its", and it read "it was half-knotted". The possessor is now a noun.
- ***Ew hosel covv hesperd o***, "it was only a soldier's cloak", for the English "a plain soldier's cloak" (ordinary, not an officer's). *(Back-translation fix.)* The first draft had *covv venn hesperd*, and *venn* is "plain" only as in "tell it plain": it read "a true soldier's cloak".

> Hosast re fennym o dem susk, eth hosast re veskym o. Re veskym o ul garm, eth nath re ston en garm, eth nath nyculom umo:

I was the first up after him, and the first to read it. I read it out, and my voice was not steady, and I will not pretend it was:

Word for word: *First I followed him up, and first I read it. I read it aloud, and my voice did not stand, and I do not lie about it:*

- ***nath re ston en garm***, "my voice did not stand": *ston*, the word of every oath's close, and of the wall.

**The Title.** *Written in coal by the Captain on the capstones; drawn in the Book as he wrote it (the `legend_title_coal` surface), and written by Seren in the same words.*

> **Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.**

**IN MEMORY OF OUR HOME, OUR FAMILIES, OUR GOD, OUR FREEDOMS, OUR PEACE.**

| Hand | What it writes | Token string | Count |
|---|---|---|---|
| **the coal** (*garl brenth*), the Captain's | the whole tongue, unjoined letters, no bed band | `u.l t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th , o.l m.a.r.dh , o.l l.u.n.n.A.th , o.l s.o.l.l.a.n \|` | 43 letters, 5 marks |
| **the leaf-hand** (*Garl Flenn*), Seren's ink | the same string, joined | the same | 48 letters and marks, 20 pen movements |
| **the dry cut** (*ryt broc*), the chisel | the stones only; the six mortar words (*ul*, five *ol*) left out | `@tum+O.l @varn , @theld+A.th , @mardh , @lunn+A.th , @sollan \|` | **17 signs** (checked with `drycut.py`) |

**The Title cut dry, sign by sign** (`orrowen_v2` §7.7):

| [TUM] (120) **O l** | [VARN] ODH+still (58) | wedge | [THELD] ODH+drop (59) **A th** | wedge | [MARDH] LUMM+cope (251) | wedge | [LUNN] (258) **A th** | wedge | [SOLLAN] GARL+still (217) | perpend |
|---|---|---|---|---|---|---|---|---|---|---|
| memory | home | · | families | · | God | · | freedoms | · | peace | · |

*Memory: home, families, God, freedoms, peace.* The five things stand; the reader lays the mortar in. The Title is not cut in the Book (the Captain "was no Stonewright", and wrote in coal); this is how the guild would cut it over a gate, and where it is shown is **[Jack]** (`orrowen_v2` §15 item 6 recommends the Tongues doc only).

> Re hadh o et hagess ul dresk et hald, eth re hebb o lo et helvhoss. Ew ull hald nahresket dasken Orrow, eth ew ull et movenn umo.

He set the pike in a crack of the wall and gave it to the wind. That was the last unbroken wall of the Shorelands, and that was the banner above it.

Word for word: *He laid the pike in a cleft of the wall, and gave it to the wind. That was the last unbroken wall of the Shore, and that was the banner upon it.*

- ***ul dresk et hald***, "in a cleft of the wall": the crack is *tresk*, the word in *Kethow Dhresk*, "the keep of the cleft". The Keep's name and the cloak's are one word, and here is where the pike stood.

> Amm sy hunna cedh re dhess, eth ul drenn vodh, hy vodh re nydhym. Re dhessent et vennuldath hosast, eth es vollom so, hy vodh nel nydhyl nydhyl dem vollol. Stannard Sorth, et stannard. Corlen Dhavow. Tamm Sull Heskal. Marl Sedhen. Aske Hrisur Lurr. Garvel Runnowath. Harl Orrow sa Vorr. Ulden Salereth. Hesk Lynth. Lanner Gynten. Pellow Vell. Eth Kael Nydherd, rytvard et vennuldath: el en ull. Nath noss cumm lom, hy vodh re wesk o en lo orrol. Delv. Re nydhym ol pa fedh, eth new sell.

Now hear who answered, and in what order, for I counted. The True Men answered first, and I will name them, for a count is not a count until it is named. Stannard of the ridge, the quarryman. Corlen of the harbour. Tamm of the three spans. Marl the fen-born. Aske of the canopy. Garvel of the smithies. Harl of the burning shore. Ulden of the galleries. Hesk of the mere. Lanner of the crags. Pellow of the spire. And Kael the Counter, oath-keeper of the True Men; that is me, of no haven, for he found me on a road. Twelve. I counted us twice, and it did not take long.

Word for word: *Now hear who answered, and in what course, for I counted. The True Men answered first, and I will name them, for a count is not a count until the naming. … And Kael the Counter, oath-keeper of the True Men: that is I. No haven is at me, for he found me by a road. Twelve. I counted us twice, and it was not long.*

- ***nel nydhyl nydhyl dem vollol***, "a count is not a count until the naming", is built as the Stonwryt's *somm el tolm tolm*, "while stone is stone": Kael's creed in the shape of the guild's vow.
- **The Twelve's epithets** are the tongue's own constructs, the place softened as possessor as in *Rhyna Yanna Ulvenn* (*Corlen Dhavow* < *tavow*; *Pellow Vell* < *pell*; *Garvel Runnowath* < *drunnowath*; *Aske Hrisur Lurr* < *crisur lurr*, "the roof of the forest"). *Marl Sedhen* and *Lanner Gynten* are adjectives ("fen-born", "crag-born"), which do not mutate. *Harl Orrow sa Vorr* is "of the shore that burns", as *Sulter sa vorr* is the Burning Boat. **Names are names**: the epithets are places; the names keep no meaning.
- ***Stannard Sorth, et stannard***: Stannard's name is the word for a quarrier, so "the quarryman" is his own name said again as a word. A Rivenman hears the chime; the English cannot.
- ***ul drenn vodh***, "in what course": the order of a line of men, as of a course of stones (an addition).

> Hy ull hesperdeth et vran kest, sa re orrant et hollarol sell lo ol sest; el ol gryrullath so amm sy, gor vennuld hos cryrull, eth oskant ol hosen oskar o. Hy ull lunt et trenn, sa re lymm so dhevath um so sestowath lo dhrenn et hiskenneth: hos carm, eth delv, eth hy ull lesk murr eth lesk murr; eth amm ull nath re yal nydhyl lom, eth re hessym raevulol. El et fedh hosel sa re hessym. New hy haral, hy vodh re hebb o nahos. Re ryt o hosel galat sa re yal lor tul, eth re yal loskat.

Then the soldiers of the six companies, who had walked the long retreat beside us; they are our troops now, a troop to each True Man, and they trust us as we trust him. Then the people of the column, who had carried their children on their backs through the passes: one voice, and a dozen, and then hundreds, until I could not count, and I stopped trying. It is the only time I ever stopped. It was not by command, for he gave none. He had only written down what we had left, and it was enough.

Word for word: *Then the soldiers of the six companies, who had walked the long retreat at our shoulder; our troops are they now, every True Man one troop, and they trust us as we trust him. Then the people of the column, who had carried their children upon their backs through the passes: one voice, and twelve, and then a hundred and a hundred; and then counting was not at me, and I stopped trying. It is the only time that I stopped. It was not from a command, for he gave none. He wrote only the thing that was still at us, and it was enough.*

- ***lesk murr eth lesk murr***, "a hundred and a hundred": Orrowen's hundred is a phrase ("five twenties") and takes no plural, so "hundreds" is counted on until the counter gives up, which is the point.
- ***nath re yal nydhyl lom***, "counting was not at me": "I could not count", the "at" idiom of §3.7 in the past.
- ***oskant ol hosen oskar o***, "they trust us as we trust him": *osk* is "rest one's weight on".

> Hy ull el lorr gever ol gethowath. El vesket et covv ull.

That is why the pennant on every keep of ours is crimson. It is the colour of that cloak.

Word for word: *That is why the pennant of our keeps is crimson. It is the colour of that cloak.* *Lorr* is "blood" and "crimson" at once.

> Doss o ul reskyl lo ull amm sy, lo rask et prenth, eth o wiskhovv dem susk. Mysk o los: new hosen ull. Ew hosen ull.

He is sitting there now, at the end of the bench, with his hood up. He will tell you it was not like that. It was like that.

Word for word: *He is in sitting there now, at the end of the bench, and his hood up. He tells you: it was not like that. It was like that.*

- ***New hosen ull. Ew hosen ull.*** The Captain's denial and Kael's answer are the same three words, with the copula turned: *new*, "was not", *ew*, "was". Orrowen's yes and no are the verb said back.

> Cadhom o hosen re yal cadhat lom.

This I lay as it was laid for me.

(The hearth formula as the lexicon gives it: *I lay it as it was laid at me.*)

### The True Men's verse

> *Hy ull re vellent et vennuldath, hosen vellent o tul:*

*Then the True Men sang, as they sing it still:*

> *Ganna cresket, pithulath driget,*
> *ul gemmyl lo orrow, wemmeth myst;*
> *re yyst hosel um dholmath luskat,*
> *eth re dhresk et covv um o sest.*
> *Re ryt o lesk galat dem sennyl,*
> *eth re vaver nahos hyor vranast.*

> *The gate was broken, the lords were scattered,*
> *the grey sails gathered along the shore;*
> *one man climbed where the stones lay loosened*
> *and tore the cloak his shoulders wore.*
> *He wrote five things a man might die for,*
> *and none of us has needed more.*

Word for word:

> *Gate broken, lords flung apart,*
> *a-gathering by the shore, the grey sails;*
> *a lone one climbed upon the loosened stones,*
> *and rived the cloak upon his shoulder.*
> *He wrote five things for dying,*
> *and none of us has wanted a sixth.*

**The form.** First-syllable stress, as the tongue has it. The first, third and fifth lines have four beats and fall away on a two-syllable ending (*DRI-get*, *LUS-kat*, *SEN-nyl*, with *CRES-ket* chiming inside the first). The second, fourth and sixth lines close on **the same consonants, not the same vowels**: *myst · sest · vranast*. A rhyme of the ear that a mason would call a true joint; the English rhymes *shore · wore · more* by vowels, and Seren rhymed it her own way. **[Jack]** if the song should rhyme by vowels too.

- **The opening is verbless** (*Ganna cresket, pithulath driget*), as the tongue's proverbs are: a song remembers states, and the verbs begin when the one man moves.
- ***re yyst hosel***, "a lone one climbed": *hosel* is "one, alone, single", the *one* man against the scattered lords.
- ***luskat***, "loosened", is *lusk*, which the hearth hears in *lunn*, freedom (`orrowen_v2` §11.5).
- ***nahos hyor vranast***, "none of us … a sixth": the Title's five, and no one needing a sixth. The English "needed more" is the same thing said without counting; the True Men count.

### The hearth's answer

> *Eth re vysk et odh:* **Tumar.**

*And the hearth said: We remember.*

*Tumar* is canon and unchanged: "we remember", and Orrowen's yes (Jack's note 2). It is built on the Title's second word. The frame *Eth re vysk et odh* is the lexicon's formula.

### The facing leaf (the wood's, not yet known)

> *Doss hosel meskdhrenn um et flenn ul lern, eth hos trenn:*

*The facing leaf shows only the grain of the wood, and one line:*

Word for word: *There is only the grain upon the leaf in front, and one line.* (*meskdhrenn*, "the wood's course", is the grain.)

**The grain.** The leaf itself is the Stone's own rings, with **no mark cut in them** until the Epilogue (Book, `legend_stone_rings`; `grain_v2.md`: "the Stone's facing leaf, before the Epilogue, still shows rings only"). There is nothing to write in Grain Notation: the round is bare. When the Epilogue is laid, the same rings carry the Last Carver's marks; that is the Epilogue's pilot, not this one.

**Seren's line**, in her single ink (canon, `orrowen_v2` §11.4, unchanged):

> **Nawrodhat. Nath noss tul kethyl et gunn sy lo Halyna.**

*Untold. Halyna cannot yet hold this deep.*

`n.a.b^S.r.o.dh.A.t | n.a.th d^N.o.s.s t.u.l k.e.th.O.l e.t g.u.n.n s.y l.o =h.a.l.y.n.a |` (41 letters and marks, 20 pen movements). *Halyna* carries the sealing lintel, the only lintel on the leaf.

---

## NOTES FOR JACK AND FOR THE NEXT TRANSLATORS

### 1. The one liberty: *Ston.* after Kael's two oaths [Jack]

`orrowen_v2` §3.9: "An oath closes with the one-word vow *Ston.*" Kael swears twice (*Rytom um hosk…*, *Rytom um ull pawast*), and in Orrowen an oath without its close is not finished; he is the oath-keeper, and would not leave one open. So both close with *Ston.*, and this is the only place the Orrowen has a word the English lacks. The reading offered: Seren's "I swear … that …" renders the whole formula, as an English oath has no closing word. Seren says she did not change a word of Kael's; she translated them. If Jack would rather the Orrowen carry nothing the English does not, delete the two *Ston.* and nothing else moves.

### 2. Grammar this leaf had to settle (proposals, each reversible)

| # | Point | What the leaf does | Why |
|---|---|---|---|
| G1 | **The negative past** (lexicon §8.3 left it open) | ***nath re*** + S: *nath re yal*, *nath re hylym*, *nath re vysk* | *nath* beds the next word, which is *re* and cannot change; *re* softens the verb. The tense particle sits next to the verb, as in the canon's *sa re vess*. Added to the lexicon as a phrase row |
| G2 | **Verb agreement** | a plural noun subject takes the plural ending (*re yalant et crenneth*, *re veskent et vennuldath*); a collective takes the 3sg (*re resk et Stonwrytan*, *sa re lymm* of *lunt*); the existential *doss* stays 3sg | the canon's *Tuma Halyna* agrees with its noun subject; the canon's *Re yald et Stonwrytan* is 3sg with a collective |
| G3 | **The object of a verbal noun** | a possessor, softened: *kylyl wrod* "changing a word" | a verbal noun is a noun; the canon's *rellor wrod* has the same shape |
| G4 | **"where" as a relative** | *ul vodh* (*Lo wisk, ul vodh re ston et hald*) | the lexicon already gives *ul vodh* for "where"; the question word serves as the relative, as in many tongues |
| G5 | **Relatives with a preposition** | the conjugated preposition stays behind: *sa re rytent … umo* "on which they cut", *sa reskys lo* "that you sit at", *sa re yal et neskyl lo* "whose was the leading" | the Celtic-type resumptive, which §3.6's conjugated prepositions make natural |
| G6 | **A fronted object** | left out and taken up again: *galat sa nath re nydhym, nath gadhom o los* | Orrowen is verb-first; a thing brought forward is picked up by *o* |
| G7 | **The softened *cr-*** | *hr-*: *so Hrenn*, *so hrenneth*, *Aske Hrisur Lurr* | the canon gives *Crenn*, S *Hrenn* (§5.4), so the onset is the canon's own |
| G8 | **"Only" of a clause** (back-translation) | *nath … veth*, "not … but": *sa nath re yorrar veth amm ew venn et dask* | *hosel* after a verb reads "alone"; *nath … veth* is already the leaf's *lo nayalat veth osk* |
| G9 | **A possessive before a letter that does not soften** (back-translation) | the possessor said as a noun (*saed et covv*), or the sentence recast (*uld hosen et Crenn*) | after a verb, *o* + a word in *h, s, l, r, n, f, v, w, th, dh* or a vowel shows no bite, so it reads as the subject "he" (`orrowen_v2` §3.5, clarified) |
| G10 | **"Not yet" and "no longer"** (back-translation) | *nath … tul* is "not yet" only; "no longer" is said another way (*re vammant*, "had lost") | the canon's *Nath noss tul kethyl* fixes *nath … tul* (`orrowen_v2` §5.10, clarified) |

### 3. Collisions the leaf steps around

- **N + *br-* gives *mr-***, an onset §2.5 does not allow: no nasalised *brodh* anywhere (Kael's *tell* after *es* and *nath* is *cadh*, "lay", which is the tongue's own idiom for telling).
- ***mysk* "say" after a nasalising word reads as N·*bysk* "tie"**: the analyzer takes *nath myskym* as "I do not tie". The leaf never puts *mysk* after *es* or *nath* (*Amm sy myskym los*, *Mysk o los*: the present, which is also the habitual).
- ***re vysk*** is both "said" and "bound": "bound" is given as the participle (*bysket*); "said" keeps *re vysk*, as the canon formula has it.
- ***darr* "come" softens to *rarr***: *mellor* "come in" is used instead.
- ***dem amm* "until when" nasalises to *dem mamm***, which is a reserve word: avoided (the paragraph runs on with *eth amm ull*, "and then").
- **A mutating trigger before *gor***: *lo gor vennuld* would leave *gor* either unmutated or as *yor*, which the grammar does not settle; the leaf says *gor vennuld hos cryrull* ("every True Man one troop"), and "every keep of ours" is *ol gethowath*, "our keeps".
- **The construct of *gynteth*** would give *Yynteth*: Lanner takes the adjective *Gynten*.
- ***hethow*** (S·*kethow*) reads as *heth* "spring" + *-ow* in the analyzer (lexicon §8.2): "to a castle" is *dem gethow*, where the nasal makes it plain.

### 4. Where the Orrowen is built differently from the English

For Jack's eye; none changes the sense.

| English | Orrowen | Why |
|---|---|---|
| Some cried that we should send… | the cries quoted: *Luska… pessa…!* | no "that" before a clause |
| The crying began | *re dhald et carmol*, the crying rose | *mosk* "begin" is the Creed trap; the lexicon's newer *cadh et tolm hosast*, "lay the first stone", is for beginning a work, not a crying |
| The outer gate hung from one hinge | *Re heth hos brellir et ganna hyvenn*, one hinge held it | the tongue's verb is *keth* |
| The ward behind it was grass to the knee | there was grass to the knee in the ward behind | the state verb |
| I had heard men break before | *…fedheth*, at times | the lexicon's *tevar* is "early, before the time", not "previously"; *fedheth* "times" does it |
| twelve of us in all | *dem nelv*, up to twelve | the counter's sum after *hos eth hos* |
| bound us by nothing but trust | *re heth o ol*, held us | see §3 |
| It was not that the greater men were gone. There was no greater man. | *New hy vodh re yalant et uldath strom sennet. Nath re yal hos strom hyo.* It was not because the great men were dead. There was not one greater than he. | Kael counts (revised after the back-translation) |
| who no longer knew their officers | *sa re vammant so hrenneth*, who had lost their captains | *nath … tul* is "not yet"; the tongue has no "no longer" |
| who fought only when the cause was just | *sa nath re yorrar veth amm…*, who did not fight but when… | "only" of a clause is *nath … veth* |
| a plain soldier's cloak | *hosel covv hesperd*, only a soldier's cloak | *venn* "plain" is "straight", not "ordinary" |
| I do not think his equal ever lived | *…uld hosen et Crenn*, a man like the Captain | *o hosen* read "he … like one" |
| he took off his cloak | *re nahovv o hovv*, un-cloaked his cloak | the reversative |
| and hundreds | *lesk murr eth lesk murr* | a hundred has no plural |
| every keep of ours | *ol gethowath*, our keeps | see §3 |
| He will tell you | *Mysk o los*, he tells you | see §3 |
| one man climbed | *re yyst hosel*, a lone one climbed | the verse's metre |
| and none of us has needed more | *…nahos hyor vranast*, none of us a sixth | the True Men count to five |

### 5. The hands

- **Ink (this leaf).** Everything above is what the leaf-hand writes: the mortar words, the endings, every mutation as a bite under its base letter. `to_ink.py` turns romanised Orrowen into the Garl Flenn font's markup, but it reads the wf6 lexicon through `render_shore.py` and does not yet know the tier-3 words (tried on the headnote, it gets the bites right, *k^sadh*, *p^sess*, and spells *Crennel* and *rytvard* by sound, with no harmonic letters). **Before the leaf is drawn, `to_ink.py` should read `lexicon_orrowen.tsv`**, or the token strings should be made from `orr_analyze.py`'s parses (base letter, bite, harmonic letter), which already hold everything needed.
- **Chisel.** Only the Title is cut on this leaf, above. If the Book is ever "cut into the granite of this hall", Kael's telling cut dry would keep its stones and lose its mortar words; *Rytom um … Ston.*, being an oath, would be cut **whole**, in letters (D9).

---

## LEXICON ADDITIONS

Appended to `wf7/lexicon_orrowen.tsv` by `wf7/pilot/add_i1.py` (idempotent), source `tier3`, each derivation ending "pilot I.1", as rows O2860 to O2880 (O2858 and O2859, *hos eth ullen* and *cadh et tolm hosast*, were appended by another pilot in between). No new root; every row is built from existing entries by the lexicon's rules (§4 of `lexicon_orrowen.md`).

| id | Orrowen | pos | cl. | sense | derivation | dry cut |
|---|---|---|---|---|---|---|
| O2860 | **nahovv** | v | B | take off (a cloak, a garment); unwear | *na-* 'un-' (+S) + *covv* 'a cloak; wear' (c > h): the reversative, as *nahadh*, *nawysk* | `!@covv` |
| O2861 | **nath re** | part | B | did not, had not: the negative past | *nath* NEG(+N) + *re* PST(+S) (G1; a grammar proposal) | `!` |
| O2862 | **hos eth hos** | adv | B | one by one ("one and one") | *hos* + *eth* + *hos* | `%h , %h` |
| O2863 | **hosen amm** | conj | B | as if, as though ("as when") | *hosen* as + *amm* when | `letters: h.o.s.e.n @amm` |
| O2864 | **ul drenn vodh** | adv | B | in what order ("in the course of what") | *ul* (+N) + N·*trenn* + *vodh* | `@trenn` |
| O2865 | **orl ull** | adv | B | that day | *orl* + *ull*, as *vess sy* | `@orl` |
| O2866 | **grem sy** | adv | S | this winter | *grem* + *sy*, as *vess sy* | `@grem` |
| O2867 | **gor orl** | adv | B | every day; all through a span of days | *gor* (+S) + *orl* | `@orl` |
| O2868 | **crest hull** | n | B | river-ice | *crest* + S·*rhull* (rh > h), the construct | `@crest @rhull` |
| O2869 | **rytvard et vennuldath** | n | B | the oath-keeper of the True Men (Kael's office) | *rytvard* + *et* + *vennuldath* | `letters: r.y.t.v.a.r.d @venn@uld+A.th` |
| O2870 | **Stannard Sorth** | name | B | Stannard of the Ridge | the epithet construct, *sorth* (s unchanged) | `s.t.a.n.n.a.r.d @sorth` |
| O2871 | **Corlen Dhavow** | name | B | Corlen of the Harbour | S·*tavow* (t > dh) | `k.o.r.l.e.n letters: t.a.v.o.w` |
| O2872 | **Tamm Sull Heskal** | name | B | Tamm of the Three Spans | *sull* + *heskal* (numeral before a singular) | `t.a.m.m %s @heskal` |
| O2873 | **Marl Sedhen** | name | S | Marl the Fen-born | apposition, *sedhen* "of the fen" | `m.a.r.l @sedh+e.n` |
| O2874 | **Aske Hrisur Lurr** | name | B | Aske of the Canopy | S·*crisur lurr* (c > h, as *Hrenn*) | `a.s.k.e letters: k.r.i.s.u.r @lurr` |
| O2875 | **Garvel Runnowath** | name | B | Garvel of the Smithies | S·*drunnowath* (dr- > r-, lexicon §4.3) | `g.a.r.v.e.l @drunn+o.w.A.th` |
| O2876 | **Harl Orrow sa Vorr** | name | B | Harl of the Burning Shore | *Orrow* + *sa* + *vorr*, as *Sulter sa vorr* | `h.a.r.l @orrow @vorr` |
| O2877 | **Ulden Salereth** | name | S | Ulden of the Galleries | *saler*-PL (s unchanged) | `u.l.d.e.n letters: s.a.l.e.r.A.th` |
| O2878 | **Hesk Lynth** | name | S | Hesk of the Mere | *lynth* (l unchanged) | `h.e.s.k letters: l.y.n.th` |
| O2879 | **Lanner Gynten** | name | S | Lanner of the Crags | apposition, *gynten* "of crags" | `l.a.n.n.e.r @gynt+e.n` |
| O2880 | **Pellow Vell** | name | S | Pellow of the Spire | S·*pell* (p > v) | `p.e.l.l.o.w @pell` |

**Before any rebuild.** `lex/build_lexicon.py` regenerates the TSV from `lex/en_map/*.txt`, so appended rows would be lost. To keep them, add these recipe lines (the files' own format) first:

```
lex/en_map/y_world.txt:
- | na-covv | v | take off (a cloak, a garment); unwear
did not | ~nath re | part | did not, had not: the negative past (nath + re, +S)
one by one | ~hos eth hos | adv | one by one ('one and one')
as if | ~hosen amm | conj | as if, as though ('as when')
- | ~ul drenn vodh | adv | in what order ('in the course of what')
that day | ~orl ull | adv | that day
this winter | ~grem sy | adv | this winter
every day | ~gor orl | adv | every day; all through a span of days
river-ice | ~crest hull | n | river-ice ('the ice of a river')
lex/en_map/names_terms.txt:
@phrase | ~rytvard et vennuldath | n | the oath-keeper of the True Men
@phrase | ~Stannard Sorth | name | Stannard of the Ridge
@phrase | ~Corlen Dhavow | name | Corlen of the Harbour
@phrase | ~Tamm Sull Heskal | name | Tamm of the Three Spans
@phrase | ~Marl Sedhen | name | Marl the Fen-born
@phrase | ~Aske Hrisur Lurr | name | Aske of the Canopy
@phrase | ~Garvel Runnowath | name | Garvel of the Smithies
@phrase | ~Harl Orrow sa Vorr | name | Harl of the Burning Shore
@phrase | ~Ulden Salereth | name | Ulden of the Galleries
@phrase | ~Hesk Lynth | name | Hesk of the Mere
@phrase | ~Lanner Gynten | name | Lanner of the Crags
@phrase | ~Pellow Vell | name | Pellow of the Spire
```

(Not added to those files here: other pilots may be appending to the lexicon at the same time, and a rebuild would renumber every row under them.)

**Still owed**, as for all tier-3 text: the Welsh, Irish and Tolkien dictionary pass on the reserve words this leaf uses (`orrowen_v2` §14c item 1). The leaf rests on 62 reserve roots (as words, or under a tier-3 derivation; *mamm* 'lose' came in with the back-translation fixes): *aedh, bisk, brellir, bress, bysk, bystir, crisur, cryrull, deld, drig, fedh, fenn, gask, gerd, gever, grik, gynt, gyst, haethil, hagess, haral, havul, hedh, hellur, heskal, hiskenn, hollar, hyrril, kaever, lern, linth, losk, lymm, lynth, mamm, maver, mellor, merr, mest, misk, movenn, mysk, nesk, niss, nycul, nyrul, pithul, prenth, raevul, redul, rerd, resk, saed, saemal, saler, semm, sest, simm, susk, tragul, vimm, wesk*.
