# RIVENKEEP · TIER 3 · THE MERGE: ONE LEXICON, ONE GRAIN, ONE BOOK

*wf8 workflow document, 2026-09-28. Not a Book leaf and not a repo doc; nothing here goes into `Docs/` (nothing was written there). Tier 3 (Jack: "I'd like tier 3 on how far to take the translation"): the whole Book of the Riven Stone in its own tongues, translated in eighteen units at once (S01–S11 the stone leaves, W01–W07 the wood leaves, on the two pilots I.1 and IV.4), each writing its new words and signs to its own additions file. This report merges and harmonises them. The shared `wf7/lexicon_orrowen.tsv`, `wf7/grain_v2.md` and `wf7/coverage/concepts.tsv` were read only; the merged files are new.*

## THE SHORT VERSION

| | Count |
|---|---|
| **Final lexicon** (`wf8/lexicon_orrowen_full.tsv`) | **3,015 entries** = 2,880 shared + **135 new** (O2881–O3015) |
| **Orrowen additions merged** | **180 rows** from 18 additions files (14 with rows): 159 into new entries (24 of them duplicates reached independently, collapsed into 15 entries), 15 as new senses of 10 existing entries, 2 as regular inflections of existing entries, 4 withdrawn for the form another unit or the lexicon already had |
| **Grain additions merged** (`wf8/grain_v2_full.md` §21.9) | **53 compounds** from 56 rows in 8 units (no new sign), **75 decoder readings** (A15), 10 rules and calls (A16b–A25), 15 register corrections |
| **Concept register** (`wf8/concepts_full.tsv`) | **557 rows** = 429 + 53 compounds + 75 readings; 10 rows corrected; 670 of 670 lemmas mapped; 0 rows with an error |
| **Conflicts resolved** | **Lexicon 8**: 4 senses with two forms, 1 form with two senses, 3 near-synonyms kept apart by sense (and 15 independent duplicates harmonised: class, case, formation, cut). **Grain 8** (G1–G8): 3 of substance (the mirror and the hollow; "did not know why"; `!GO → @8`), 5 duplicates. **Cross-unit text: 16 harmonisations** in 15 units (§5) |
| **Units re-validated** | **all 18** (and both pilots): Orrowen 19,281 words in the units' blockquotes, **0 unknown, 0 ill-formed**; the units' own draft files, 19,157 words, 0; analyzer `--test` 87 of 87; grain **79 GN rounds** in the unit files and **30 source files** (84 rounds), **0 errors, 0 warnings**; the coverage corpus ALL OK |
| **Back-translation totals** (all units, blind before, after the units' fixes) | **633 units scored**: before 354 exact, 221 close, 51 drift, 7 wrong; after **368 exact, 259 close, 6 drift, 0 wrong** (the 6 drifts left are 5 reader slips where the text stands and 1 grain collision that is Jack's call) |

---

## 1 · INPUTS

- **Units** (`wf8/units/*.md`): S01 foreword, Invocation, I.2 · S02 I.3, I.4 · S03 I.5, II.1 · S04 II.3, IV.3 · S05 III.1 · S06 IV.1, IV.5 · S07 V.1, V.2 · S08 V.5 · S09 V.7 · S10 VI.1, the Epilogue · S11 the Book of Knowings · W01 II.2 · W02 III.2 · W03 IV.2 · W04 IV.6 · W05 V.3 · W06 V.4 · W07 V.6. With the pilots (I.1, IV.4) that is every leaf of the Book.
- **Additions** (`wf8/additions/`): 18 Orrowen files (`<unit>.tsv`; W04–W07 hold the header only) and 9 grain files (`<unit>_grain.md`: S09, S10, W01–W07).
- **Back-translations** (`wf8/backtrans/*.md`, 17 files; S01's is reported in its unit, §5.5).
- **Specs and tools** (read only): `wf7/ancestor.md`, `wf7/orrowen_v2.md`, `wf7/grain_v2.md`, `wf7/lexicon_orrowen.tsv` + `.md`, `wf7/orr_analyze.py`, `wf7/grain_validate.py`, `wf7/coverage/`, the pilots and their back-translations, `wf6/lang/blacklist.txt`, `wf7/book/legends_v13.md` (the Book v1.3.0) and its builder.

## 2 · THE ORROWEN LEXICON (`wf8/lexicon_orrowen_full.tsv`)

**How it was built** (`wf8/tmp/merge/merge_lex.py`, repeatable). The shared lexicon's 2,880 rows are kept whole (its ids, its canon glosses verbatim). Every addition row was read against it and against the other units' rows, by form (case aside, a leading article aside) and by sense (its English lemmas against the lexicon's `book_lemmas`). The lexicon's own rules decided each case: **one form, one row** (the shared lexicon has no duplicate form but two suffix pairs), so a new sense of an existing form is appended to its `meanings` after the canon sense (lexicon §2, §4.4), never a second row; a phrase takes the class of its last word (the shared lexicon's convention, 243 of its 244 phrase rows) and the formation `phrase`; the new rows keep the 14 columns, `source` `tier3`, and name their units in the derivation. The same 14 columns and escaping mean the analyzer reads the file as it reads the shared one.

### 2.1 Conflicts resolved

| # | Kind | Forms | Chosen, and why | Units updated |
|---|---|---|---|---|
| L1 | one sense, two forms | *trenn um dhrenn* (S02-09) · *trenn eth trenn* (S04-07) | *trenn eth trenn*. "A paragraph each" is distributive, and the distributive is the X *eth* X of pilot I.1's *hos eth hos* (O2862), used by S03, S04, S06, S07, S08 and W02; X *um* X is "X upon X", piling (*bystir um wystir*, *brod um wrod*). S01's third form, *trenn gor hos*, goes the same way (§5) | S02, S01 |
| L2 | one sense, two forms | *hosk et carm* (S01-04) · *cadh et hosk um* (O-S09-01) | *cadh et hosk um*, "lay the lintel upon": the exact counterpart of the pilots' *cadh et tolm hosast*, "begin" (O2859), one verb for both ends. S01's noun use (*hos lo o dholm hosast eth ullen lo o hosk*) was already the pair's | S01 |
| L3 | one sense, two forms (with the shared lexicon) | *kylyl uldath* (S06-08) · *kylyth* (O1134) | *kylyth*: the shared lexicon made it for the Book's own lemma "fickleness", and it keeps the sentence's two abstracts in *-Oth* side by side (*nel hy voduloth, veth hy hylyth uldath*) | S06 |
| L4 | one sense, two forms (with the shared lexicon) | *hinnar Dhavow* (W02-02) · *tavowhinnar* (O2494) | *tavowhinnar*: the shared lexicon's compound for the Book's hyphenated "harbour-city" (lexicon §3.2); a definite construct reads "the city of the harbour", one city. The headnote reads *gor dhavowhinnar Orrow* | W02 |
| L5 | one form, two senses | *meskel* (O1385): "the root-men" and "treelings" | split, as S08 found it must be (V.5: "the wall calls them treelings"): the root-men are *uldath veskrivull*, "the men of the root" (S08-03, O2974); *meskel* keeps "a treeling" | none (S08 already so) |
| L6 | near-synonyms | *ul hos hoss* (S09, W02) · *ul hos fedh* (S05), both glossed "at once" | both kept, glosses narrowed: *ul hos hoss* "in one breath" (quickness, the same instant); *ul hos fedh* "at one time" (things together) | none |
| L7 | near-synonyms | *fedh lyss* (S04) · *fedh* | *fedh lyss* narrowed to "a short while"; *fedh* keeps "a time, a season" | none |
| L8 | near-synonyms | *cadh nycul* (S09) · *nycul* | *cadh nycul* narrowed to "deceive: lay a lie in a mind"; *nycul* keeps "lie, tell a lie" | none |

**Reached independently, merged into one row each (15 entries from 39 rows).** Every group agreed on its form; the merge settled what differed:
- **Lodhan Helv** (O2881: S01, S04): formation → `phrase`
- **tovv um** (O2883: S01, S11)
- **ul so lodh** (O2884: S01, S03)
- **garl venn** (O2885: S01, S04): class B/S → the last word's class
- **garl ullen** (O2886: S01, S04): class B/S → the last word's class
- **Cadhan o hosen re yal cadhat lona** (O2893: S02, S03, S04, S05, S06, S07, S10)
- **arra sa re lumm** (O2925: S04, W01): spelling *arra sa re lumm* / *et arra sa re lumm*
- **pa eth pa** (O2927: S04, S08)
- **Lymmerd Yendeth** (O2943: S05, S10, S11)
- **Meskdhrenn sa Lilv** (O2944: S05, S10, S11): spelling *Meskdhrenn sa Lilv* / *Meskdhrenn sa lilv*
- **Grem Sell** (O2945: S05, S10, S11)
- **Lorr Helv** (O2946: S05, S10, S11)
- **flenn et tolm** (O2961: S06, S08): class B/S → the last word's class
- **flenn et mesk** (O2962: S06, S08)
- **ul hos hoss** (O2985: S09, W02)
- *Cadhan o hosen re yal cadhat lona*, Halyna's close in the dual, was written by seven units in the same words; its logogram and dry cut follow the shared singular and plural rows (O0238, O0234), where four units had cut the person ending.

**New senses of existing forms (15 rows into 10 entries; no new row):** *cadhol* O0237 (S02): (et cadhol) the laying: the hour of the siege day when the Stonewrights raise and mend; *caldol* O0243 (S02): (et caldol) the hauling: the hour of the siege day when the guns are dragged to where the Captain wants them; *kethyl* O1124 (S02): (et kethyl) the holding: the hour of the siege day when the grey sails come in and the wall must stand; *galdat* O0657 (S02): done, made (the participle of gald in its senses 'do, make'); of a rite: done, performed; *ommol* O1869 (S04, S08, S11): (a name, et Ommol) the Fall: the fall of the Shorelands, and of the havens; *vorrol* O2785 (S05, S10, S11): (a name) the Burning: the shore's name for Esthaer, a Throne (the soldiers' Magma Titan); *lennet* O1177 (S05, S10): (a name) the Silvered: the shore's name for Neivaere, a Throne (the soldiers' Crystal Lich); *kylyl* O1133 (S10): (a name, Et Kylyl) The Turn: the subtitle of Book Six; *maveret* O1355 (S11): a prize, a thing coveted ('a thing wanted'); *mellorol* O1364 (S11): reach, range (of guns: as far as their fire comes in).

**Regular inflections (no new row):** *Mymmyleth* is the plural of *mymmyl* (O1453, which already carries "the Homecomings") and *drunnatath* the plural of *drunnat* (O0513, "a drum"); the analyzer parses both, and the units' senses are appended to the two rows.

### 2.2 Screening (`wf8/tmp/merge/screen_lex.py`)

Every new row, and every shared row the merge touched (146 in all), was screened:
- **The analyzer**: every word of every form parses in context (phrases with their mutations) against the merged lexicon: **0 problems**. The whole merged lexicon parses entry by entry as the shared one does (the eight *noss-* forms, said only after *nath* and *es*, set aside as `lex/selfcheck.py` sets them aside); `--test` passes all **87** samples of `orrowen_v2.md`.
- **Originality**: no new word is on the Tolkien and franchise blacklist (`wf6/lang/blacklist.txt`), the reserve screen's rejected forms, or the common-English list; no banned letter (*z, x, q, j*) or ending (*-ion, -iel, -dor*). Only three rows are new single words, all regular derivations of existing roots: *seryl* (*ser* + *-Ol*), *bithlernen* (*bithlern* + *-en*), *desirel* (*desir* + *-el*). None is an English word.
- **The ancestor's uniqueness rules**: no new form equals an existing form or a softened or nasalised one, and none reads as *na-* + another word (lexicon §4.2). **No new root**: every root named by a new row is one the shared lexicon already uses (four written in another notation were normalised: *\*stan-* → *\*ston-*, *\*ol-* → *\*ol*, *\*sa-* → *\*sa*, *\*tunn-* → *\*tann-*), so no wood-only root is revived and the ancestor's 38 kin words stay 38.

### 2.3 Where each addition went

| New id | Form | Units (rows) |
|---|---|---|
| O2881 | *Lodhan Helv* | S01 (S01-01), S04 (S04-06) |
| O2882 | *Hemm eth Hemma* | S01 (S01-02) |
| O2883 | *tovv um* | S01 (S01-03), S11 (O-S11-13) |
| O2884 | *ul so lodh* | S01 (S01-05), S03 (S03-24) |
| O2885 | *garl venn* | S01 (S01-06), S04 (S04-04) |
| O2886 | *garl ullen* | S01 (S01-07), S04 (S04-05) |
| O2887 | *hos ul lern ullen* | S01 (S01-08) |
| O2888 | *cedh ew cedh* | S01 (S01-09) |
| O2889 | *Brodh gor sa heth o* | S01 (S01-10) |
| O2890 | *Hemma Rhyna* | S01 (S01-11) |
| O2891 | *Hemm Halvard* | S01 (S01-12) |
| O2892 | *Gor wramm caldat, trenn nahadhat* | S01 (S01-13) |
| O2893 | *Cadhan o hosen re yal cadhat lona* | S02 (S02-01), S03 (S03-02), S04 (S04-09), S05 (S05-06), S06 (S06-01), S07 (S07-01), S10 (S10-01) |
| O2894 | *Lodhan et Kethow* | S02 (S02-02) |
| O2895 | *Hale Haskard* | S02 (S02-03) |
| O2896 | *Ketherd Hethow Dhresk* | S02 (S02-04) |
| O2897 | *Lo et Crenn, clem sell hosen orl* | S02 (S02-05) |
| O2898 | *bystir um wystir* | S02 (S02-10) |
| O2899 | *hoss kethet* | S02 (S02-11) |
| O2900 | *vess ull* | S02 (S02-12) |
| O2901 | *Crenn Hovv Treskat* | S03 (S03-01) |
| O2902 | *tunn ullen* | S03 (S03-03) |
| O2903 | *tesk eth tesk* | S03 (S03-04) |
| O2904 | *grem eth grem* | S03 (S03-05) |
| O2905 | *hos ul vimm ullen* | S03 (S03-06) |
| O2906 | *hos um ullen* | S03 (S03-07) |
| O2907 | *ganna lodhat* | S03 (S03-08) |
| O2908 | *cadhat ul hos tevow* | S03 (S03-09) |
| O2909 | *serull Stonwryt* | S03 (S03-10) |
| O2910 | *cumm hemm sost* | S03 (S03-11) |
| O2911 | *mest hy* | S03 (S03-12) |
| O2912 | *tragul et prass* | S03 (S03-13) |
| O2913 | *tess tessyl* | S03 (S03-14) |
| O2914 | *keth pawast* | S03 (S03-15) |
| O2915 | *dem dolm eth crest* | S03 (S03-16) |
| O2916 | *voll dem mymmyl* | S03 (S03-17) |
| O2917 | *tolm terril* | S03 (S03-18) |
| O2918 | *um hos lodh gunn* | S03 (S03-19) |
| O2919 | *hy so dhrenn* | S03 (S03-20) |
| O2920 | *hy sona dhrenn* | S03 (S03-21) |
| O2921 | *orrol dem vimm dem et cummath* | S03 (S03-22) |
| O2922 | *orlath desir* | S03 (S03-23) |
| O2923 | *seryl* | S04 (S04-01) |
| O2924 | *Brenn Reldvar* | S04 (S04-02) |
| O2925 | *arra sa re lumm* | S04 (S04-03), W01 (O-W01-01) |
| O2926 | *trenn eth trenn* | S04 (S04-07) |
| O2927 | *pa eth pa* | S04 (S04-08), S08 (S08-08) |
| O2928 | *tev dem susk* | S04 (S04-10) |
| O2929 | *hy volt* | S04 (S04-11) |
| O2930 | *fedh lyss* | S04 (S04-12) |
| O2931 | *ho nath* | S04 (S04-13) |
| O2932 | *drunn hurrol* | S04 (S04-14) |
| O2933 | *Uld sa lumm lo tho yebb, ul vimm tho hrisur* | S04 (S04-16) |
| O2934 | *Besk nasesket. Dask bynden. Hesset. Sceth vorrat eth luskat.* | S04 (S04-17) |
| O2935 | *Amm senn et garl ullen, ho nath senn et garl venn?* | S04 (S04-18) |
| O2936 | *Re lodh tevyl sona; nath re yal sona dhreskol lo sennyl* | S04 (S04-19) |
| O2937 | *Treskol, nath re lusk Mardh o* | S04 (S04-20) |
| O2938 | *doss surr lo* | S04 (S04-21) |
| O2939 | *So Yaldol* | S05 (S05-01) |
| O2940 | *So Ommol* | S05 (S05-02) |
| O2941 | *Saed Hosast* | S05 (S05-03) |
| O2942 | *Saed Pawast* | S05 (S05-04) |
| O2943 | *Lymmerd Yendeth* | S05 (S05-07), S10 (S10-05), S11 (O-S11-02) |
| O2944 | *Meskdhrenn sa Lilv* | S05 (S05-08), S10 (S10-06), S11 (O-S11-04) |
| O2945 | *Grem Sell* | S05 (S05-10), S10 (S10-08), S11 (O-S11-05) |
| O2946 | *Lorr Helv* | S05 (S05-11), S10 (S10-09), S11 (O-S11-01) |
| O2947 | *ryssyth yarl* | S05 (S05-14) |
| O2948 | *Nath gemment et trenneth; re hethym pana* | S05 (S05-15) |
| O2949 | *orrow sa vorr* | S05 (S05-16) |
| O2950 | *wemmeth domm* | S05 (S05-17) |
| O2951 | *scethan stonat* | S05 (S05-18) |
| O2952 | *scethan yorrol* | S05 (S05-19) |
| O2953 | *ammadol pemessen* | S05 (S05-20) |
| O2954 | *ul hos fedh* | S05 (S05-21) |
| O2955 | *lo dhrenn et grem* | S05 (S05-22) |
| O2956 | *farrol orl* | S05 (S05-23) |
| O2957 | *vesk dem neld* | S05 (S05-24) |
| O2958 | *fedh eth fedh* | S06 (S06-02) |
| O2959 | *havul eth havul* | S06 (S06-03) |
| O2960 | *molt syst* | S06 (S06-04) |
| O2961 | *flenn et tolm* | S06 (S06-05), S08 (S08-05) |
| O2962 | *flenn et mesk* | S06 (S06-06), S08 (S08-06) |
| O2963 | *ul neld veskyl* | S06 (S06-07) |
| O2964 | *scaevurel rytow* | S06 (S06-09) |
| O2965 | *gedheth ol nedheth* | S06 (S06-10) |
| O2966 | *Ul vodh naross poduloth, hessyth ol lestir* | S06 (S06-11) |
| O2967 | *Nath noss brodlymmyl lo dholm* | S06 (S06-12) |
| O2968 | *Kesterd Voss* | S06 (S06-13) |
| O2969 | *lo nunthath* | S06 (S06-14) |
| O2970 | *tolmath sa haemerent* | S06 (S06-15) |
| O2971 | *brod um wrod* | S07 (S07-02) |
| O2972 | *bithlernen* | S08 (S08-01) |
| O2973 | *desirel* | S08 (S08-02) |
| O2974 | *uldath veskrivull* | S08 (S08-03) |
| O2975 | *doss flenn et mesk ul o lern* | S08 (S08-07) |
| O2976 | *hos hoss ul lodh* | S08 (S08-09) |
| O2977 | *ul drenn* | S08 (S08-10) |
| O2978 | *el venn o* | S08 (S08-11) |
| O2979 | *Doss vorr et scethan vyssorat* | S08 (S08-12) |
| O2980 | *Naelur et molt sa luskith lont* | S08 (S08-13) |
| O2981 | *keth o dhrenneth* | S08 (S08-14) |
| O2982 | *ho ross* | S08 (S08-15) |
| O2983 | *cadh et hosk um* | S09 (O-S09-01) |
| O2984 | *Re vysk hos, eth re dhunn ullen* | S09 (O-S09-02) |
| O2985 | *ul hos hoss* | S09 (O-S09-03), W02 (W02-05) |
| O2986 | *fedh loskol reller* | S09 (O-S09-04) |
| O2987 | *cadh nycul* | S09 (O-S09-05) |
| O2988 | *hosen re yal kaeveret* | S09 (O-S09-06) |
| O2989 | *Trenn Hosast: Sull Orrol, Hos Clem* | S09 (O-S09-07) |
| O2990 | *Trenn Pawast: Vodh re ammadar lont* | S09 (O-S09-08) |
| O2991 | *Trenn Sullast: Niltenn sa re ryt lernil umo sost* | S09 (O-S09-09) |
| O2992 | *Kethen et tolm olen* | S10 (S10-02) |
| O2993 | *bysket ul lern et trenn hosast* | S10 (S10-04) |
| O2994 | *Lymmerd et Lodh* | S10 (S10-11) |
| O2995 | *lunt et hoss* | S10 (S10-12) |
| O2996 | *Stinel Hosel* | S11 (O-S11-06) |
| O2997 | *Hosk ul Lern* | S11 (O-S11-07) |
| O2998 | *Gemmyorn Nawrodh* | S11 (O-S11-08) |
| O2999 | *Pa Wrodow* | S11 (O-S11-09) |
| O3000 | *Sestow Kylet* | S11 (O-S11-10) |
| O3001 | *Stinel Dasorat* | S11 (O-S11-11) |
| O3002 | *hebb veskyl* | S11 (O-S11-14) |
| O3003 | *lusk ul* | S11 (O-S11-15) |
| O3004 | *sest lo sest* | S11 (O-S11-16) |
| O3005 | *sell tevar* | S11 (O-S11-19) |
| O3006 | *pa sest* | S11 (O-S11-20) |
| O3007 | *Reskowath Strom* | W02 (W02-01) |
| O3008 | *reskow strom eth reskow strom* | W02 (W02-03) |
| O3009 | *hos ul hos cumm* | W02 (W02-04) |
| O3010 | *hy flenn sy dem lern* | W02 (W02-06) |
| O3011 | *ketherdeth strom et scethan strom tunn* | W02 (W02-07) |
| O3012 | *lerneth dasken susk* | W02 (W02-08) |
| O3013 | *Gannath Myst hemm sost* | W02 (W02-09) |
| O3014 | *gannath hossen dasken et hald* | W02 (W02-10) |
| O3015 | *lern hosel* | W03 (W03-01) |

Withdrawn: S01-04 *hosk et carm* (→ O2983), S02-09 *trenn um dhrenn* (→ O2926), S06-08 *kylyl uldath* (→ O1134), W02-02 *hinnar Dhavow* (→ O2494). Into existing rows: S02-06/07/08, S02-13, S04-15, S05-05, S05-09, S05-12, S05-13, S08-04, S10-03, S10-07, S10-10, O-S11-03, O-S11-12, O-S11-17, O-S11-18 (§2.1).

## 3 · THE GRAIN (`wf8/grain_v2_full.md`, `wf8/concepts_full.tsv`)

`wf8/grain_v2_full.md` is `wf7/grain_v2.md` word for word with a new **§21.9** (built by `wf8/tmp/merge/gen_grain_full.py`):
- **§21.9.2 · 53 compounds** from 56 rows (S10, W01–W07), each modifier + head with its computed soft reading, in **one** JSON block the validator reads. `BENEATH+SIT` (W01, W02, W06) and `OVER+HULL×3` (W01, W06) were proposed more than once, always with the same gloss; no compound conflicted with another, with §21.3/§21.7 or with the validator's own table. **No new sign.**
- **§21.9.3 · 75 decoder readings** (A15, continued), merged from the units' 81 rows: one row where two units said one thing ("answer"; "heavy" and "go heavy"; "light" and "go light"; "hasty" and "crude"), and one reading where they differed (below).
- **§21.9.4 · rules and calls**: A16b (referents, completed: W01 with W03, W05 and W06's belongings), **A17** (the mirror and the hollow together), A18 (the untold ring, S09) **[Jack]**, A19 (a memory ray in a celled year), A20 (a band lies over its file's whole year), A21 (A9 completed), A22 (traps the register should name), A23 (*Rhenear* cut small in E5-02), A24 (the Last Tide's root) **[Jack]**, A25 (the v1 STONE sample in the Epilogue) **[Jack]**.
- **§21.9.5 · register corrections** (applied in `wf8/concepts_full.tsv`, 557 rows, which `coverage/check_coverage.py` reads with 670 of 670 lemmas mapped and 0 rows in error), **§21.9.6** ten findings for the shared validator, **§21.9.7** the conflicts settled.

**The grain conflicts** (§21.9.7):

| # | Conflict | Settled | Re-cut |
|---|---|---|---|
| G1 | `!~X`: W01 read it "not mis-X"; W02, W03 and W05 found that no drawing can show whether the mirror or the hollow is outermost | **A17**: the order carries nothing; `!~X` is "a seeming not-X" (as the validator already reads it); *must not be mistaken* is IV.2's `!TURN+HOLD` | W01 r10 `!~HEAR` → `!TURN+HEAR`; W01 r11 `!~HOLD` → `!TURN+HOLD` (the same English as IV.2 r7); W07 r8 `!~GO#2` → `~GO#1{only}` |
| G2 | W03 proposed the canonical order `~!`; the printer writes `!~` | the printer's order stands | none |
| G3 | "did not know why": W03 `!HOLD →in` the act; W04 `!HOLD →` the act, which V.6's *feel* row reads "not feel" | W03's `→in` | W04 r10, runner m8 |
| G4 | `!GO → @8` glossed "will not leave" (W03), "away from home" (W04), "no crown to come home to" (W07) | one reading, *not going to file 8* (behind, home), glossed by its doer | none |
| G5–G8 | duplicate compounds; the pocket-cursor finding (W02, W04); A16's missing belongings (W01, W03, W05, W06); duplicate readings | one entry each | none |

Each re-cut was made in the unit's knowing-form source, its canonical text and its unit file together (`--canon` of the source equals the printed round, comments aside), and all three validate clean.

## 4 · EVERY UNIT RE-VALIDATED

**Orrowen** (`wf8/tmp/merge/validate_units.py`): every blockquote of every unit file (the house style: each paragraph romanised in a blockquote over the Book's English), markdown stripped, against the merged lexicon with a private copy of the analyzer. English verse that a unit quotes in a blockquote is recognised and set aside (listed in `orr_validation.json`); the Last Carver's line, whose error the canon keeps and the analyzer must report, is counted as expected. A second pass reads each unit's own declared analyzer input (`validate_drafts.py`), which also holds lines outside blockquotes (S10's ten token expansions, S11's glosses). **Grain** (`validate_grain.py`): a private copy of the validator whose `wf7/grain_v2.md` is the merged spec checks every GN block of every unit file (`--md`) and every GN source the units name; the coverage corpus (`run_tests.py`: ALL OK) and the IV.4 pilot are re-run to show the merged compounds change no finding.

| Unit | Leaves | Orrowen words (unit file) | Reported | Draft words | Reported | GN rounds (file) | GN sources | Errors / warnings |
|---|---|---|---|---|---|---|---|---|
| S01 | foreword, Invocation, I.2 | 2,235 | 0 | 2,235 | 0 | 0 | 0 | 0 / 0 |
| S02 | I.3, I.4 | 1,741 | 0 | 1,741 | 0 | 0 | 0 | 0 / 0 |
| S03 | I.5, II.1 | 1,600 | 0 | 1,590 | 0 | 0 | 0 | 0 / 0 |
| S04 | II.3, IV.3 | 2,464 | 0 | 2,453 | 0 | 0 | 0 | 0 / 0 |
| S05 | III.1 | 1,399 | 0 | 1,405 | 0 | 0 | 0 | 0 / 0 |
| S06 | IV.1, IV.5 | 1,952 | 0 | 1,952 | 0 | 0 | 0 | 0 / 0 |
| S07 | V.1, V.2 | 1,869 | 0 | 1,869 | 0 | 10 | 1 | 0 / 0 |
| S08 | V.5 | 1,182 | 0 | 1,132 | 0 | 0 | 0 | 0 / 0 |
| S09 | V.7 | 956 | 0 | 956 | 0 | 3 | 3 | 0 / 0 |
| S10 | VI.1, Epilogue | 1,771 | 0 | 1,904 | 0 | 3 | 3 | 0 / 0 |
| S11 | Book of Knowings | 900 | 0 | 943 | 0 | 47 | 1 | 0 / 0 |
| W01 | II.2 | 162 | 0 | 162 | 0 | 1 | 2 | 0 / 0 |
| W02 | III.2 | 235 | 0 | (frame only; in the file) | – | 10 | 10 | 0 / 0 |
| W03 | IV.2 | 194 | 0 | 194 | 0 | 1 | 2 | 0 / 0 |
| W04 | IV.6 | 145 | 0 | 145 | 0 | 1 | 2 | 0 / 0 |
| W05 | V.3 | 147 | 0 | 147 | 0 | 1 | 2 | 0 / 0 |
| W06 | V.4 | 187 | 0 | 187 | 0 | 1 | 2 | 0 / 0 |
| W07 | V.6 | 142 | 0 | 142 | 0 | 1 | 2 | 0 / 0 |
| **all** | | **19,281** | **0** | **19,157** | **0** | **79** | **30** | **0 / 0** |
| pilots | I.1, IV.4 | 1,187 | 0 | | | 2 (IV.4) | | 0 / 0 |

The two word counts differ only where a unit's draft holds more or fewer lines than its blockquotes (S10's nine alternative token names; S11's glosses; the headings and titles S03, S04, S05 and S08 set in blockquotes or leave out), and the units' own claims differ from these by the few words the merge fixes changed (S01 2,235, S02 1,741, S03 1,600, S06 1,952, W02 235, W06 187). No unit reports a word in either pass.

## 5 · CONSISTENCY ACROSS UNITS

### 5.1 The pilots' formulas, everywhere identical

| Formula (pilot) | English | Units |
|---|---|---|
| *Eth re vysk et odh:* **Tumar.** (I.1) | And the hearth said: We remember. | S01–S09 (every stone leaf that closes so); S04, S07 and S09 set as the pilot sets it (merge) |
| *Cadhom o hosen re yal cadhat lom.* (I.1) | This I lay as it was laid for me. | S01, S02 (I.3), S03 (I.5), S06 (IV.5), S07 (V.2), S08 (×6) |
| *Cadhan o hosen re yal cadhat lona.* (the dual, O2893) | This we lay as it was laid for us. | S02 (I.4), S03 (II.1), S04 (II.3, IV.3), S05 (×2), S06 (IV.1), S07 (V.1), S10 (VI.1): every Halyna-told stone leaf |
| *Hosen tum Mesk Myst: kethet hy …* (IV.4) | As the Mystwood remembers: known from … | W01–W07 |
| *Re wrodha Halyna o, hos eth ullen, ul ba luth; re hadh Seren o.* (IV.4) | Told by Halyna, by turns, in two inks; set down by Seren. | W01, W03–W07; W02 with III.2's own "a Throne each" (*reskow strom eth reskow strom*) |
| *Amm re yal et mesk cresket, ell re omm et brodhol, doss o rellorat eth nahlennet.* (IV.4) | Where the wood was broken, or the telling failed, it is marked, and not mended. | W01–W07 (W02, W03, W07 add their leaf's own clause after it) |
| *Eth re dhess nahos.* (IV.4) | And no one answered. | W01–W07, S10 (VI.1) |
| *Re hadh* X … (I.1) | Laid by X … | every stone headnote |
| *doss o ul lern* X (IV.4) | it faces X | W01, W03, W04, W05, W07 |

### 5.2 Recurring English, one rendering (the merge's text fixes)

The Book's recurring phrases were found by their shared five-word runs across leaves and checked paragraph by paragraph (`align.py`). Where units differed, one form was kept (the pilots', else the majority, else the better derivation) and the others changed; each change is marked *Merge fix* in its unit, which also opens with a merge note.

| # | English | The one form | Changed in |
|---|---|---|---|
| 1 | one of them said, and the other finished | *re vysk hos, eth re dhunn ullen* (S03, S07, S09; O2984) | S01 (was *… hos hyonta … ullen o*) |
| 2 | by turns, a paragraph each | *hos eth ullen, trenn eth trenn* (S04, S07) | S01 (*trenn gor hos*), S02 (*trenn um dhrenn*) |
| 3 | one beginning it and the other ending it; gave it its end | *cadh et tolm hosast* / *cadh et hosk um* | S01 (*re hosk o et carm* → *re hadh o et hosk umo*) |
| 4 | It is the stone leaf of X | *El flenn et tolm um et* X (S05, S08) | S03 (*El flenn tolmen et pa varn o*), S06 (*… tolm o, um …*) |
| 5 | the wood's leaf faces it | *doss flenn et mesk ul o lern* (S05, S06, S07, S08) | S04 (*… ul lern flenn sy*) |
| 6 | the (old, new) capstone of the inner gate | *hosk (hemm, clenn) et ganna ulvenn* (S01, S03) | S02 (*hosk Yanna Ulvenn, et hosk clenn*), S10 (*et hosk clenn sa ross um yanna ulvenn*) |
| 7 | the tide took it out | *re lymm et hyll o dem neld* (S06) | S04 (*… o hyo*), S10 (*re rik …*) |
| 8 | what the one knows, the other knows | *galat sa heth hos, keth ullen o* (S01, S07) | S09 (*… sesk hos, sesk ullen o*; its reasoning is kept for Jack, §7) |
| 9 | of the grain we call X | *hy et meskdhrenn sa vollar* X (W03) | W06 (*hy veskdhrenn …*) |
| 10 | the fickleness of men | *kylyth uldath* (the lexicon's *kylyth*) | S06 (L3) |
| 11 | harbour-city | *tavowhinnar* (the lexicon's) | W02 (L4) |
| 12 | we call them Shorelanders … and we call ourselves we | *vollar so: Orrowan … vollar ol sost: ol* (S01) | S03 (punctuation and case) |
| 13 | the Grain That Rots | *Meskdhrenn sa Lilv* (S10, S11) | S05 (case) |
| 14 | must not be mistaken (the grain) | `!TURN+HOLD` (IV.2) | W01 (G1) |
| 15 | did not know why (the grain) | `!HOLD →in` the act (IV.2) | W04 (G3) |
| 16 | the leaf-hand: a lexicalised compound | written as said, no bite inside it (`orrowen_v2` §6.5; W06, and every other unit) | S01 (six words), W03 (three) |

Checked and already one: *Kethen et tolm* (Halyna's "We hold the stone", S02, S04, S07, S10); *galdardath hosast et Kethow* (the first builders); *re rytym ul ba luth* ("I have used two inks"); *vestul sa re lymmym dem susk et brunn* (the chest I carried up the mountain); *Hyll sa re rystull nycul*, *Hyll Dhumol*, *Hyll Lodhat*, *Hyll Pawast* (the Tides); *wemmeth myst* (the grey sails); *vovennerd/movennerd* (Standard-Bearer, mutation aside); *Lodhan et Kethow* (the Bonded of the Keep); *Nath gemment et trenneth … re hethym pana* (the tales do not agree; I have kept both: S01, S05, W03).

### 5.3 Names

Every capitalised word of every unit was parsed and grouped by the lexicon row it reads as (`names_check.py`): each name has one form in all units, mutation aside (*Rhyna / Hyna*, *Kethow / Gethow*, *Tavow / Dhavow / Davow*, *Mardh / Vardh*, *Tarnel / Dharnel*). The epithets agree: *Rhyna Yanna Ulvenn*, *Halvard Tolmvard*, *Kael Nydherd*, *Seren Pa Luth*, *Voss sa re vess*, *Hale Haskard*, *Kesterd Voss*, *Brenn Reldvar*, *Hemma Rhyna*, *Hemm Halvard*, *Lodhan et Kethow*, *et Crenn* (the Captain, never named); the Throne epithets *Lymmerd Yendeth, Meskdhrenn sa Lilv, Vorrol, Grem Sell, Lorr Helv, Lennet* in S05, S10 and S11 alike (S05's case fixed); the grains *Dommwrint*, *Lennsast*; the Mystaeri names as loans. Jack's standing rules hold: *Seren* is "a single sorrow that overcomes" (O2265, canon); *Tumar* "we remember" is the yes of every close; "the Mystlands" is kept (*Mystow*, O1469, in III.1 and IV.5; in the grain, A1's `EARTH[MIST]`, "earth inside the grey"); names are names.

### 5.4 Halyna's alternation

The Legends builder alternates the two inks on every body paragraph of a `<!-- HALYNA -->` leaf, restarting at a part heading and stopping at `HALYNA END`; the laid formula, the hearth's answer, frames and fully italic lines take no ink; II.3 follows the name (`<!-- MARKED -->`). `halyna_check.py` computes the Book's own sequence and compares each unit's Orrowen paragraphs and ink labels:

| Leaf | Unit | Book paragraphs | Unit paragraphs | Voices | Result |
|---|---|---|---|---|---|
| I.4 | S02 | 11 | 11 | abababababa | one paragraph each, in order; labels as the builder sets them |
| II.1 | S03 | 11 | 11 | abababababa | one paragraph each, in order; labels as the builder sets them |
| II.3 | S04 | 12 | 12 | abababababab | the name opens each Orrowen paragraph (Rhyna, Halvard, …), as the Book marks it |
| IV.3 | S04 | 23 | 24 | abababababababababababa | unlabelled by design (S04: "two inks, by turns, unmarked"); the one extra block is the warden's report, a fully italic line that takes no ink |
| III.1 | S05 | 20 | 21 | ababababababaabababa | the one extra block is *Added in Seren's hand …*, a fully italic line in her own ink |
| IV.1 | S06 | 12 | 12 | abababababab | one paragraph each, in order; labels as the builder sets them |
| V.1 | S07 | 11 | 11 | abababababa | one paragraph each, in order; labels as the builder sets them |
| VI.1 | S10 | 17 | 17 | ababababababababa | one paragraph each, in order; labels as the builder sets them |

Fixed at the merge: five units put an ink on the laid formula, and not the same one (S02, S03 and S05 the second ink, S06 the first); it now carries none, as the builder sets it. S07's two halves of V.1's split line were "the one ink" and "the other ink"; they are now *second ink* and *first ink*, the builder's own alternation. On the wood leaves the alternation lives in the English and Plain Words tabs, paragraph by paragraph; the units keep one ring (or knowing) to a paragraph, and the merge changed no ring's place.

## 6 · BACK-TRANSLATION TOTALS

Each unit's native lines were read back blind into English and scored on the pilots' scale (**exact** · **close**: a nuance shifts · **drift**: a proposition lost or changed · **wrong**: contradicted or invented), then fixed and re-read by rule. From `wf8/backtrans/*.md` (S01's from its unit, §5.5):

| Unit | Part | Scored | Before: exact · close · drift · wrong | After: exact · close · drift · wrong |
|---|---|---|---|---|
| S01 | Orrowen | 46 | 28 · 15 · 2 · 1 | 28 · 18 · 0 · 0 |
| S02 | Orrowen | 30 | 13 · 13 · 4 · 0 | 15 · 15 · 0 · 0 |
| S03 | Orrowen | 32 | 23 · 7 · 2 · 0 | 24 · 8 · 0 · 0 |
| S04 | Orrowen | 46 | 33 · 9 · 3 · 1 | 33 · 11 · 2 · 0 |
| S05 | Orrowen | 43 | 33 · 10 · 0 · 0 | 33 · 10 · 0 · 0 |
| S06 | Orrowen | 29 | 14 · 13 · 2 · 0 | 14 · 15 · 0 · 0 |
| S07 | Orrowen | 43 | 24 · 15 · 4 · 0 | 25 · 18 · 0 · 0 |
| S08 | Orrowen | 34 | 25 · 6 · 1 · 2 | 25 · 9 · 0 · 0 |
| S09 | Orrowen | 31 | 24 · 6 · 1 · 0 | 25 · 6 · 0 · 0 |
| S09 | grain | 6 | 0 · 5 · 0 · 1 | 0 · 6 · 0 · 0 |
| S10 | Orrowen + grain | 58 | 30 · 20 · 7 · 1 | 32 · 22 · 4 · 0 |
| S11 | Orrowen | 65 | 46 · 17 · 2 · 0 | 46 · 19 · 0 · 0 |
| W01 | Orrowen | 9 | 6 · 3 · 0 · 0 | 6 · 3 · 0 · 0 |
| W01 | grain | 14 | 1 · 11 · 2 · 0 | 3 · 11 · 0 · 0 |
| W02 | Orrowen | 10 | 8 · 2 · 0 · 0 | 8 · 2 · 0 · 0 |
| W02 | grain | 17 | 1 · 12 · 4 · 0 | 1 · 16 · 0 · 0 |
| W03 | Orrowen | 10 | 8 · 2 · 0 · 0 | 10 · 0 · 0 · 0 |
| W03 | grain | 14 | 2 · 8 · 4 · 0 | 3 · 11 · 0 · 0 |
| W04 | Orrowen | 7 | 6 · 1 · 0 · 0 | 6 · 1 · 0 · 0 |
| W04 | grain | 11 | 1 · 8 · 2 · 0 | 1 · 10 · 0 · 0 |
| W05 | Orrowen | 7 | 5 · 2 · 0 · 0 | 5 · 2 · 0 · 0 |
| W05 | grain | 11 | 1 · 4 · 5 · 1 | 1 · 10 · 0 · 0 |
| W06 | Orrowen + grain | 28 | 12 · 15 · 1 · 0 | 13 · 15 · 0 · 0 |
| W07 | Orrowen | 8 | 7 · 1 · 0 · 0 | 7 · 1 · 0 · 0 |
| W07 | grain | 24 | 3 · 16 · 5 · 0 | 4 · 20 · 0 · 0 |
| **Orrowen (Seren's ink and the tellings)** | | **450** | **303 · 122 · 21 · 4** | **310 · 138 · 2 · 0** |
| **grain (rings, rounds, plates)** | | **97** | **9 · 64 · 22 · 2** | **13 · 84 · 0 · 0** |
| **units scored as one (S10, W06)** | | **86** | **42 · 35 · 8 · 1** | **45 · 37 · 4 · 0** |
| **all units** | | **633** | **354 · 221 · 51 · 7** | **368 · 259 · 6 · 0** |

- **Before**: 575 of 633 units exact or close (91%); **after**: 627 of 633 (99%), with **no wrong** left. The six drifts left are not translation errors: S04's two and three of S10's are reader slips where the text stands, and S10's fourth is the Stone's `DEEP+SQUARE`, a spec collision left to Jack (grain_v2_full A25).
- **Not in the totals**: S11's 47 carvings (identical to their canonical sources, clean, literal readings matching; checked, not scored), W06's twelve leaf-hand lines (decoded 10 · 1 · 1 · 0 before, 12 · 0 · 0 · 0 after), and the pilots' own tests (`wf7/backtrans_I1.md`, `wf7/backtrans_IV4.md`).
- **The merge's own changes were not read blind.** Each adopts a form another unit had already read back (mostly exact), so the risk is small; a fresh reader should still read the changed lines: S01 F.7b, F.8a, C.6c; S02 the I.4 headnote and ¶5; S03 the II.1 headnote and I.5's naming line; S04 the IV.3 headnote and burning; S06 the IV.1 headnote and ¶10; S09 V.7 I ¶1; S10 VI.1 ¶16 and the Epilogue's grave; W02 H2; W06 the headnote; the rings W01 r10–r11, W04 r10, W07 r8.

## 7 · FOR JACK, AND STILL OPEN

1. **"What the one knows, the other knows"** is now *keth* in all three leaves (the Bonded's own verb, "hold; know the wood"). S09 had argued for *sesk*, "know a fact", in V.7, because there the bond shares a mind and no wood is touched. If Jack prefers that distinction, it belongs in all three places (and the foreword's case is wood-knowing), so the choice is one word, made once.
2. **"Part One" (III.1) and "Part I" (V.7)** stay apart: *Saed Hosast*, "the first half", for a catalogue laid in two; *Trenn Hosast*, "the first course", for V.7's three parts, each laid on its own night (*saed* reads "half", which three parts cannot be). The English differs too. Say if one word should serve both.
3. **`!TURN+HOLD` and `!TURN+HEAR`** are legal ligatures that the shared validator reads part by part ("not turning aside, and holding"); a glossed compound could make the reading "a holding not turned". Left for the validator's owner.
4. **The rules marked [proposed] and [Jack] in `grain_v2_full.md` §21.9.4** (A16b referents, A18 the untold ring, A24 the Last Tide's root, A25 the Epilogue's v1 sample) wait on a spec pass; every unit reads right without them, with `# file` comments.
5. **Still owed from before**: the Welsh, Irish and Tolkien dictionary pass on every reserve word the tier-3 text uses (orrowen_v2 §14c), and the lexicon's own findings for Jack (the three *-dor* reserve roots; *mosk*, *heth*, *cald*, *dath*); the units stepped round them throughout, and the merge added nothing that meets them.
6. **Folding the merge into the shared files** (when the concurrency window closes): `lexicon_orrowen_full.tsv` replaces `wf7/lexicon_orrowen.tsv` as is; §21.9 of `grain_v2_full.md` is written to be appended to `wf7/grain_v2.md` as it stands; `concepts_full.tsv` replaces `wf7/coverage/concepts.tsv`; the recipes of the 135 new rows belong in `wf7/lex/en_map/` before any rebuild (pilot I.1's caution).

## 8 · FILES

- **Deliverables** (`wf8/`): `lexicon_orrowen_full.tsv` (3,015 rows), `grain_v2_full.md`, `concepts_full.tsv`, this report.
- **Units** (`wf8/units/`): 15 of the 18 changed as listed (§2, §3, §5), each opening with a merge note; S08, S11 and W05 re-validated and unchanged but for that note. GN sources re-cut in place: `wf8/tmp/W01/II-2(.canon).gn2`, `wf8/tmp/W04/IV-6(.canon).gn2`, `wf8/tmp/W07/V-6(.canon).gn2`; the units' drafts synced with the changed lines. Backups of everything the merge touched: `wf8/tmp/merge/backup_units/`, `backup_src/`, `backup_drafts/`.
- **The merge's tools and logs** (`wf8/tmp/merge/`): `merge_lex.py` (with `load.py`), `screen_lex.py`, `gen_grain_full.py` + `grain_full_tail.md`, `gen_concepts_full.py`, `validate_units.py`, `validate_drafts.py`, `validate_grain.py`, `align.py`, `names_check.py`, `halyna_check.py`, `gen_report.py`; the private analyzer copy `orr_analyze.py`, the private validator root `groot/` (its `wf7/grain_v2.md` links the merged spec), the token tool copy `wf8/tmp/mergetok/`; results `lex_decisions.json`, `screen_report.json`, `orr_validation.json`, `draft_validation.json`, `grain_validation.json`, `halyna_report.json`, `grain_merge_stats.json`, `concepts_stats.json`.
- **Not touched**: `wf7/lexicon_orrowen.tsv`, `wf7/grain_v2.md`, `wf7/coverage/concepts.tsv`, the additions files, the back-translations, and anything in `/Users/riquochet/code/Rivenkeep/Docs`.
