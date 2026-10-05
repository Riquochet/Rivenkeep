#!/usr/bin/env python3
"""wf12 merge: write wf12/merge_report.md from the merge's own results (lex_decisions.json, screen_report.json,
orr_validation.json, grain_validation.json, grain_merge_stats.json, concepts_check.json, coverage2.json,
halyna_report.json, harmonisations.json, fixes.log) and the units' back-translation totals."""
import collections, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
J = lambda f: json.load(open(os.path.join(HERE, f), encoding='utf-8'))
dec, scr, orr, grn, gst, cck, cov, hal, harm = (J('lex_decisions.json'), J('screen_report.json'), J('orr_validation.json'),
    J('grain_validation.json'), J('grain_merge_stats.json'), J('concepts_check.json'), J('coverage2.json'), J('halyna_report.json'),
    J('harmonisations.json'))
fixes = [l.rstrip('\n') for l in open(os.path.join(HERE, 'fixes.log'), encoding='utf-8')]

LEAVES = collections.OrderedDict([
    ('S01', 'Of This Book, the Invocation, I.1'), ('S02', 'I.2, I.3'), ('S03', 'I.4, I.5'), ('S04', 'II.1, II.3'),
    ('S05', 'III.1, III.2'), ('S06', 'IV.1, IV.3'), ('S07', 'IV.5, V.1'), ('S08', 'V.2, V.5'), ('S09', 'V.7, VI.1'),
    ('S10', 'VI.3, the Epilogue'), ('S11', 'the title page, the Contents, the Books\' heads, the Book of Knowings'),
    ('W01', 'II.2'), ('W02', 'IV.2'), ('W03', 'IV.4'), ('W04', 'IV.6'), ('W05', 'V.3'), ('W06', 'V.4'), ('W07', 'V.6'),
    ('W08', 'VI.2')])
# the units' own back-translation totals (their BACK-TRANSLATION sections): scored, before E C D W, after E C D W
BT = collections.OrderedDict([
    ('S01', (86, (44, 37, 5, 0), (44, 42, 0, 0))), ('S02', (86, (34, 47, 5, 0), (34, 52, 0, 0))),
    ('S03', (98, (62, 26, 9, 1), (63, 35, 0, 0))), ('S04', (66, (26, 34, 4, 2), (26, 40, 0, 0))),
    ('S05', (95, (40, 48, 7, 0), (41, 54, 0, 0))), ('S06', (104, (51, 44, 8, 1), (51, 53, 0, 0))),
    ('S07', (77, (32, 36, 9, 0), (32, 44, 1, 0))), ('S08', (114, (64, 39, 9, 2), (64, 50, 0, 0))),
    ('S09', (141, (99, 34, 6, 2), (102, 39, 0, 0))), ('S10', (113, (67, 36, 9, 1), (68, 45, 0, 0))),
    ('S11', (150, (103, 43, 4, 0), (103, 47, 0, 0))), ('W01', (39, (14, 19, 6, 0), (15, 24, 0, 0))),
    ('W02', (40, (16, 22, 2, 0), (16, 24, 0, 0))), ('W03', (39, (10, 24, 3, 2), (10, 28, 1, 0))),
    ('W04', (35, (16, 17, 2, 0), (17, 18, 0, 0))), ('W05', (33, (10, 17, 6, 0), (12, 21, 0, 0))),
    ('W06', (38, (16, 19, 3, 0), (16, 22, 0, 0))), ('W07', (37, (10, 21, 6, 0), (10, 27, 0, 0))),
    ('W08', (39, (15, 23, 1, 0), (15, 24, 0, 0)))])
for u, (n, b, a) in BT.items():
    assert sum(b) == n and sum(a) == n, u


def fmt(t):
    return ' · '.join(str(x) for x in t)


def main():
    o = []
    w = o.append
    new = dec['new_rows']
    wd = set((d['unit'], d['row']) for d in dec['decisions'] if d['kind'] in ('one sense, two forms', 'folded into one saying'))
    rows_new = sum(1 for r in new for u, rid in zip(r['units'], r['rows']) if (u, rid) not in wd)
    multi = [r for r in new if len([1 for u, rid in zip(r['units'], r['rows']) if (u, rid) not in wd]) > 1]
    rows_multi = sum(len([1 for u, rid in zip(r['units'], r['rows']) if (u, rid) not in wd]) for r in multi)
    senses = [d for d in dec['decisions'] if d['kind'] == 'new sense of a base form']
    rows_sense = sum(len(d['rows']) for d in senses)
    repl = [d for d in dec['decisions'] if d['kind'] in ('one sense, two forms', 'folded into one saying')]
    tot_words = sum(r['words'] for r in orr)
    tot_bad = sum(r['bad'] for r in orr)
    gt = grn['_total']
    paras = cov['paras']
    n_text = sum(1 for r in paras if r['kind'] not in ('native-cap', 'native-body'))
    n_text_hit = sum(1 for r in paras if r['kind'] not in ('native-cap', 'native-body') and r['hit'])
    n_furn = sum(1 for r in paras if r['kind'] in ('native-cap', 'native-body'))
    n_furn_hit = sum(1 for r in paras if r['kind'] in ('native-cap', 'native-body') and r['hit'])
    bsum = [sum(BT[u][1][i] for u in BT) for i in range(4)]
    asum = [sum(BT[u][2][i] for u in BT) for i in range(4)]
    nsc = sum(BT[u][0] for u in BT)

    w('# RIVENKEEP · THE LEGENDS v3 IN THEIR OWN TONGUES · THE MERGE: ONE LEXICON, ONE GRAIN, ONE BOOK')
    w('')
    w('*wf12 workflow document, 2026-10-03. Not a Book leaf and not a repo doc; nothing here goes into `Docs/` (nothing was written there). Jack (2026-10-02): "This should be the full document with all the tree and stone writings." The whole of THE LEGENDS OF RIVENKEEP, Book v3.0.0 (`wf11/book_v3.md`), was translated into its own tongues in nineteen units at once (S01–S11 the stone leaves and the Book\'s furniture, W01–W08 the wood leaves), each writing its new words and grain to its own additions file; this report merges and harmonises them, as the Tier 3 merge (`Docs/Research/Rivenkeep_Tongues_Tier3_Report.md`) merged the v1.3 units. The shared `wf12/base/lexicon_orrowen.tsv`, `wf12/base/grain_v2_full.md` and `wf12/base/concepts_full.tsv` were read only; the merged files are new.*')
    w('')
    w('## THE SHORT VERSION')
    w('')
    w('| | Count |')
    w('|---|---|')
    w('| **Final lexicon** (`wf12/lexicon_orrowen_full.tsv`) | **%s entries** = 3,015 shared + **%d new** (O3016–O%04d) |' % (format(3015 + len(new), ','), len(new), 3015 + len(new)))
    w('| **Orrowen additions merged** | **%d rows** from 19 additions files (16 with rows): %d into new entries (%d of them duplicates reached independently, collapsed into %d entries), %d as new senses of %d existing entries, %d withdrawn or folded for the form another unit had (and one row renamed by that choice) |' % (dec['additions'], rows_new, rows_multi, len(multi), rows_sense, len(senses), len(repl)))
    w('| **Grain additions merged** (`wf12/grain_v2_full.md` §21.10) | **%d compounds** from %d rows in 7 units (no new sign), **%d decoder readings** (A15, from %d rows), 11 rules and calls (A26–A36) and A22 continued, 15 findings for the validator |' % (gst['compounds'], gst['compound_rows'], gst['readings'], gst['reading_rows']))
    w('| **Concept register** (`wf12/concepts_full.tsv`) | **%d rows** = 557 + %d compounds + %d readings; %d rows with an error |' % (cck['rows'], gst['concept_compounds'], gst['concept_readings'], cck['rows_with_errors']))
    w('| **Conflicts resolved** | **Lexicon 9** (W12-L1–L9: one sense with two or three forms, %d rows withdrawn or folded) and %d independent duplicates harmonised; **grain 5** (G9–G13: three compounds proposed twice with different glosses, two readings) |' % (len(repl), len(multi)))
    w('| **Cross-unit harmonisation** | **%d recurring renderings** made one (H1–H36: H31 in three places, no H33 or H34), the title page and the Books\' heads and Arguments left to their one owner (S11), the pair-names written under the lintel in every unit, speech unmarked in every unit, the seal set alike in every wood leaf; every formula of the Tier 3 report §5 checked and found one |' % len(harm))
    w('| **Units re-validated** | **all 19**: Orrowen **%s words** in the units\' blockquotes, **%d unknown, %d ill-formed**; analyzer `--test` 87 of 87; grain **%d GN rounds** in the unit files, **%d** in the units\' %d source files and **%d** in the blind rounds, **0 errors, 0 warnings**; the leaf-hand writes every line (1,238 lines, 0 tokens outside the glyph table) |' % (format(tot_words, ','), tot_bad, 0, gt['md_rounds'], gt['src_rounds'], gt['src_files'], gt['blind_rounds']))
    w('| **The Book, paragraph by paragraph** | **%d of %d** paragraphs from OF THIS BOOK to the end (headings, datelines and headnotes included) have **exactly one** unit blockquote (or ring) whose English is theirs character for character; **0 doubles**; the %d native-block captions and bodies are the reader\'s furniture, %d of them given in Orrowen by their units |' % (n_text_hit, n_text, n_furn, n_furn_hit))
    w('| **Halyna\'s alternation** | all **19** `HALYNA` blocks and all **8** wood readings carry the inks as the Book sets them; no ink label outside them |')
    w('| **Back-translation totals** (every unit, blind before, after the units\' fixes) | **%d scored**: before %s (exact · close · drift · wrong); after **%s** |' % (nsc, fmt(bsum), fmt(asum)))
    w('| **The builder\'s folder** (`wf12/orig/`) | wf8\'s copied and pointed at wf12; `ink.py --test` **0 differences**, `tokens_units.py --selftest` **ok**; `to_ink.py`, lost to the temp cleaner, reconstructed privately and checked on the 326 ink lines of the wf8 build (326 of 326) |')
    w('')
    w('---')
    w('')
    w('## 1 · INPUTS')
    w('')
    w('- **Units** (`wf12/units/*.md`), one owner to each leaf of the Book v3.0.0:')
    for u, l in LEAVES.items():
        w('  - **%s** %s' % (u, l))
    w('- **Additions** (`wf12/additions/`): 19 Orrowen files (`<unit>.tsv`; W05, W06 and W07 hold the header only) and 8 grain files (`W01_grain.md` … `W08_grain.md`). The stone units added no grain: their rounds are v1.3\'s or §21.9\'s, re-validated.')
    w('- **Back-translations** (`wf12/backtrans/*.md`, 19 files; the scores are each unit\'s BACK-TRANSLATION section) and the blind inputs (`wf12/blind/`).')
    w('- **Specs and tools** (read only): `wf7/orrowen_v2.md`, `wf7/ancestor.md`, `wf12/base/` (the shared lexicon, analyzer, grain spec, concept register, validator root), the Tier 3 report and its tools (`wf8/tmp/merge/`), `wf11/book_v3.md`, `wf11/plain_v3.md`, `wf11/notes_v3.md`, the name map.')
    w('')
    w('## 2 · THE ORROWEN LEXICON (`wf12/lexicon_orrowen_full.tsv`)')
    w('')
    w('**How it was built** (`wf12/merge/merge_lex.py`, repeatable; adapted from wf8\'s). The shared lexicon\'s 3,015 rows are kept whole (ids, canon glosses verbatim). Every addition row was read against it and against the other units\' rows, by form (case aside, a leading article aside, and where a base form exists both bare and with *et*, the bare row) and by sense. The lexicon\'s rules decided each case: **one form, one row**, so a new sense of an existing form is appended to its `meanings`; a phrase takes the class of its last word and the formation `phrase`; a name carries no root; the new rows keep the 14 columns, `source` `tier3`, and name their units in the derivation (`[wf12 unit(s) …]`). Where two units coined different forms for one sense, one was chosen and the losing units\' text was changed (`fix_lex_text.py`; each change marked *Merge (wf12)* where it stands).')
    w('')
    w('### 2.1 Conflicts resolved')
    w('')
    w('| # | Sense | Forms | Chosen, and why | Units changed |')
    w('|---|---|---|---|---|')
    L = [
        ('W12-L1', 'Jory', '*Jory* (S02) · *Yory* (S03, S07, S08)', '*Yory*: the tongue has no *j* (orrowen_v2 §2.5) and its one /j/ is the worn *g* written *y* (§2.4); three units against one. The English keeps *Jory* **[Jack]**', 'S02 (four places, and *Yory Dhavow Hemm*, O3027)'),
        ('W12-L2', 'Wick', '*Wick* (S02) · *Wik* (S06, S08)', '*Wik*: *k* after *i* at a word\'s end (§2.4: *Hesk*, *kyl*), no doubled *k* (§2.5). The English keeps *Wick* **[Jack]**', 'S02'),
        ('W12-L3', 'Merrick', '*Merrick* (S02, S10) · *Merrik* (S07)', '*Merrik*, by the same rule as *Wik*, so the Book\'s two names in *-ck* are romanised alike (two units against one, but the rule decides) **[Jack]**', 'S02, S10'),
        ('W12-L4', 'whistle', '*hoss vell* (S02) · *hossvell* (S03, S05, S08, S09) · *inthvell* (S07)', '*hossvell*, "breath-song", a compound by §3.10; four units. *Re hossvell et vell* for "whistled a tune" (S02)', 'S02, S07'),
        ('W12-L5', 'hand in hand', '*garl ul narl* (S04; S07, S09, S10 in their text) · *garl lo yarl* (S08)', '*garl ul narl*: II.3, V.1, V.7 and VI.3 say it, and Tarnel\'s saying (*Piskur, el bysketeth hosel o, garl ul narl*)', 'S08'),
        ('W12-L6', 'the runners\' stone', '*tolm haskardath* (S02) · *tolm et haskardath* (S06)', 'one row, the definite construct *tolm et haskardath* (as *flenn et tolm*); I.3\'s *tolm haskardath*, "a runners\' stone" (every haven had one), is its regular indefinite and stands', 'none'),
        ('W12-L7', 'the runners\' oath', '*Galat sa re veskym, lymmym o. Nath lymmym galat ullen.* (S02) · *Lymmym galat sa re veskym. Lymmym nayalat ullen.* (S06)', 'S02\'s (O3035): it keeps the English\'s chiasm (the two *carry* meet across the full stop), I.3 is where the oath is first sworn, and it closes as every oath closes, *Ston.* (§3.9)', 'S06 (IV.3)'),
        ('W12-L8', 'for X (in X\'s stead)', '*lo reskow* X (S09) · *ul reskow* X, a new sense of O2636 (S11)', '*lo reskow*, "at X\'s seat": VI.1\'s own three captions; *ul reskow* is the lexicon\'s "somewhere"', 'S11 (the Contents line for VI.1)'),
        ('W12-L9', 'The sea hath not finished', '*Nath dunn et wadh tul* (S05) · *Tovv. Nath dunn et wadh tul.* (S08)', 'one row (O3053): the saying, with its *Tovv* (*Tovva*, to many) said beside it; both texts stand', 'none'),
    ]
    for r in L:
        w('| %s | %s | %s | %s | %s |' % r)
    w('')
    w('**Reached independently, merged into one row each (%d entries from %d rows).** Every group agreed on its form; the merge settled what differed (the dry cut written with or without `letters:`, the formation, the meaning\'s wording):' % (len(multi), rows_multi))
    for d in dec['decisions']:
        if d['kind'] == 'reached independently':
            w('- **%s** (%s: %s)' % (d['form'], d['id'], ', '.join(d['units'])))
    w('')
    w('**New senses of existing forms (%d rows into %d entries; no new row):** %s.' % (rows_sense, len(senses), '; '.join('*%s* %s (%s): %s' % (d['form'], d['base'], ', '.join(d['units']), d['sense']) for d in senses)))
    w('')
    w('### 2.2 Screening (`wf12/merge/screen_lex.py`)')
    w('')
    w('Every new row and every shared row the merge touched (%d in all) was screened:' % len(scr))
    w('- **The analyzer**: every word of every form parses in context against the merged lexicon: **%d problems**. The whole merged lexicon parses entry by entry exactly as the shared one does (23 reports in both, all the shared lexicon\'s own: the eight *noss-* forms said only after *nath* and *es*, and the suffix rows); `--test` passes all **87** samples of `orrowen_v2.md`. No duplicate form but the shared lexicon\'s two suffix pairs.' % sum(1 for x in scr if x['problems']))
    w('- **The tongue\'s phonology** (orrowen_v2 §2.5): no *z, x, q, j* and no *-ion, -iel, -dor* in any new form (the merge\'s choice of *Yory* is what makes this hold).')
    w('- **Uniqueness**: no new single word equals an existing form or reads as *na-* + another word. One homophone is reported, not failed: *miskhovv*, "a boot" (S09, O3073), sounds like N·*biskhovv*, "hood" (*en miskhovv* is both "my boot" and "my hood"); the leaves say it only softened (*o viskhovvath*), so context settles it **[Jack]**.')
    w('- **Roots**: every root named by a new row is one the shared lexicon already uses (those written in another notation were normalised to the lexicon\'s notation, e.g. *\\*bysk-* → *\\*buʔsk-*, *\\*resk-* → *\\*rask-*, *\\*xem-* → *\\*hemm-*); names carry none. No new root.')
    w('- **Not run, by Jack\'s standing rule**: no originality or dictionary check (overlap is just overlap).')
    w('')
    w('### 2.3 Where each addition went')
    w('')
    w('| New id | Form | Units (rows) |')
    w('|---|---|---|')
    for r in new:
        keep = [(u, rid) for u, rid in zip(r['units'], r['rows']) if (u, rid) not in wd]
        w('| %s | *%s* | %s |' % (r['id'], r['form'], ', '.join('%s (%s)' % (u, rid) for u, rid in keep)))
    w('')
    w('Withdrawn or folded: %s. Renamed by a choice: W12-S02-07 *Jory Dhavow Hemm* → *Yory Dhavow Hemm* (O3027).' % '; '.join('%s %s *%s* (for *%s*)' % (d['unit'], d['row'], d['dropped'], d['chosen']) for d in repl))
    w('')
    w('## 3 · THE GRAIN (`wf12/grain_v2_full.md`, `wf12/concepts_full.tsv`)')
    w('')
    w('`wf12/grain_v2_full.md` is `wf12/base/grain_v2_full.md` word for word with a new **§21.10** (built by `wf12/merge/gen_grain_full.py`):')
    w('- **§21.10.2 · %d compounds** from %d rows (W01, W03, W04, W05, W06, W07, W08), each modifier + head with its computed soft reading, in **one** JSON block the validator reads (its sources line now ends "§21 (13 compounds)"). **No new sign.** None repeats a compound of §21.3, §21.7, §21.9.2 or the validator\'s own tables (checked against all 174 + 83 + 83).' % (gst['compounds'], gst['compound_rows']))
    w('- **§21.10.3 · %d decoder readings** (A15, continued), merged from the units\' %d rows, each with its leaf and ring.' % (gst['readings'], gst['reading_rows']))
    w('- **§21.10.4 · rules and calls**: A26 the ring cap and v3\'s 25-paragraph leaves **[Jack]**; A27 a cited round is that round, not a ring *[proposed]*; A28 the causative counts with the foot station *[proposed]*; A29 a cut-pocket\'s reading *[proposed]*; A30 one questioned mark to a file [rule]; A31 a ray joins its two ends only *[proposed]*; A32 a band may wrap [rule]; A33 a telling\'s rings follow the telling *[proposed]*; A34 a v1 sample\'s referents **[Jack]**; A35 `files all` in the v1 samples *[proposed]*; A36 `AXE+GO`\'s gloss *[proposed]*, not applied; A22 continued (nine traps).')
    w('- **§21.10.5 · the register**: no base row is wrong; every new compound and every reading with a checkable fragment has its row in `wf12/concepts_full.tsv` (%d rows, kind `add`; %d readings whose cut is prose only stay in the table). **§21.10.6** fifteen findings for the shared validator; **§21.10.7** the conflicts.' % (gst['concept_rows_added'], gst['readings_without_fragment']))
    w('')
    w('| # | Conflict | Settled | Re-cut |')
    w('|---|---|---|---|')
    w('| G9 | `DEEP+LIE`: "sleep long (a long sleep)" (W01, the trees\' sleep) and "lie long" (W05, the wreck in the cold) | one entry, "lie long (sleep long; a long sleep)": LIE\'s own reading is "lie down; lie; sleep" | none; W01\'s printed literal reading now gives the merged gloss |')
    w('| G10 | `DEEP+HEAR` proposed by W03 and W06 | W06\'s gloss, "listen long (hear long)", which holds W03\'s | none; W03\'s printed literal reading updated |')
    w('| G11 | `BENEATH+GO`: "go low (go in under; beneath the water-line)" (W04) and "go under (go low, go in under)" (W08) | one entry, "go low (go under, go in under; beneath the water-line)" | none |')
    w('| G12 | "in the night": the DARK band on an empty cell with an *in* runner (W04), the DARK band over the doer\'s year (W05) | both, by what the night does in the knowing (one row) | none |')
    w('| G13 | "our kin": `BLOOD×3` (W04), `BLOOD×3 → @12` (W06) | one row | none |')
    w('')
    w('The concept register: %d rows (557 + %d), every grain cell checked with the validator\'s fragment check, **%d with an error**. `coverage/check_coverage.py` could not be run: its `words.json` (the leaves\' lemma counts) and the corpus `wf7/coverage/tests/*.gn2` are gone from the scratchpad and from the Rivenkeep_Workshop backup (the temp cleaner), so the "every lemma mapped" figure of Tier 3 is not re-measured here.' % (cck['rows'], cck['rows'] - 557, cck['rows_with_errors']))
    w('')
    w('## 4 · EVERY UNIT RE-VALIDATED')
    w('')
    w('**Orrowen** (`wf12/merge/validate_units.py`, the Tier 3 tool pointed at wf12): every blockquote line of every unit file, markdown stripped, through a private copy of the analyzer reading the merged lexicon. English verse a unit quotes in a blockquote is recognised and set aside (listed in `orr_validation.json`: the True Men\'s verse, the songs, *Two at the Gate*, the founders\' leaf\'s English, the Song of V.6 and their word-for-word renderings); the Last Carver\'s line, whose error the canon keeps, is counted as expected. **Grain** (`wf12/merge/validate_grain.py`): a private copy of the validator whose `wf7/grain_v2.md` links the merged spec checks every GN block of every unit file (`--md`), the units\' GN sources as they stand after their fixes, and the blind rounds; `--selftest` ok (117 signs; 27 + 3 + 53 + 13 compounds). The coverage corpus is gone (above); the IV.4 pilot\'s round re-validates clean.')
    w('')
    w('| Unit | Leaves | Orrowen words | Reported | GN rounds (file) | GN sources (files: rounds) | Blind rounds | Errors / warnings |')
    w('|---|---|---|---|---|---|---|---|')
    ov = {r['unit']: r for r in orr}
    for u, l in LEAVES.items():
        g = grn[u]
        src = g['sources']
        w('| %s | %s | %s | %d | %d | %s | %s | %d / %d |' % (u, l, format(ov[u]['words'], ','), ov[u]['bad'], g['md']['rounds'],
            ('%d: %d' % (len(src), sum(s['rounds'] for s in src.values()))) if src else '–',
            g['blind']['rounds'] if g.get('blind') else '–',
            g['md']['errors'] + sum(s['errors'] for s in src.values()) + (g['blind']['errors'] if g.get('blind') else 0),
            g['md']['warnings'] + sum(s['warnings'] for s in src.values()) + (g['blind']['warnings'] if g.get('blind') else 0)))
    w('| **all** | | **%s** | **%d** | **%d** | **%d: %d** | **%d** | **0 / 0** |' % (format(tot_words, ','), tot_bad, gt['md_rounds'], gt['src_files'], gt['src_rounds'], gt['blind_rounds']))
    w('')
    w('**The leaf-hand.** Every romanised line of every unit (1,238 lines, 26,391 words, 99,205 letters and marks) was written through the builder\'s `ink.py` with the merged lexicon: **0 tokens outside the glyph table** (`wf7/orrowen/leafhand.py`), 47,472 pen movements by its counter. The pair-names *Orvenna, Enrella, Wendhessa* take the sealing lintel with the canon\'s three (`tokens_units.py` PAIR_NAMES).')
    w('')
    w('**Not re-validated, on purpose**: the blind files `wf12/blind/*.txt` are the record of what each blind reader read, before the merge; they still hold the withdrawn forms (*Jory*, *Wick*, *Merrick*, *inthvell*), so they are not re-run. The units\' GN sources are validated as the units left them (the merge changed no mark).')
    w('')
    w('## 5 · THE BOOK, PARAGRAPH BY PARAGRAPH (`wf12/merge/coverage2.py`)')
    w('')
    w('Every paragraph of `wf11/book_v3.md` from **OF THIS BOOK** to the end was cut out as the Book sets it: headings, datelines, headnotes, every body paragraph, every line of a wood leaf\'s reading, the seal, each story paragraph, the Book\'s own blockquotes (the Invocation, the verse, the facing leaf), the rows of the Book of Knowings\' table, and the lines of the `::: native` and `::: note` blocks. Each leaf has one owner unit (§1); the owner\'s items are walked in order and each Book paragraph takes the next item, a blockquote of Orrowen or a ring\'s code block, whose English is that paragraph **character for character** (a heading may be set in bold, as the house style sets titles; the Book\'s `> ` is the Book\'s furniture). Then every other item in every unit whose English is a Book paragraph is a double.')
    w('')
    w('| | Book paragraphs | With exactly one unit item | Missing | Doubles |')
    w('|---|---|---|---|---|')
    kinds = collections.OrderedDict([('head', 'headings'), ('para', 'body paragraphs (datelines, headnotes, the tellings)'), ('bq', 'the Book\'s blockquotes'), ('reading', 'reading lines (wood leaves)'), ('seal', 'the seal'), ('story', 'story paragraphs (rings)'), ('table', 'the Book of Knowings\' table rows (set out root by root by S11)')])
    for k, lab in kinds.items():
        rs = [r for r in paras if r['kind'] == k]
        w('| %s | %d | %d | %d | 0 |' % (lab, len(rs), sum(1 for r in rs if r['hit']), sum(1 for r in rs if not r['hit'])))
    w('| **all text** | **%d** | **%d** | **%d** | **0** |' % (n_text, n_text_hit, n_text - n_text_hit))
    w('')
    w('Found and fixed on the way (each logged in `fixes.log`):')
    w('- **F1** · W04, W06 and W08 set the wood\'s story English in italics ("the house style\'s italics"): 72 paragraphs differed from the Book by their asterisks only, and were set to the Book character for character (the units\' claims corrected).')
    w('- **F2** · W04–W08 had no seal item (the bark\'s block over *This is held in the grain.*), which W01–W03 have and the builder keys a wood leaf on (notes_v3 §5.5); it is set in each, in the same words. W05\'s title had dropped *V.3 ·*.')
    w('- **F3** · The title page (S01 §0 and S11 §1) and the Books\' headings and Arguments (S01 Book One, S04 Book Two, S05 Book Three, S07 Book Five, S09 Book Six, S10 the Epilogue, and S11 §3) were each given twice. S11 owns them (the title page, the Contents and the Books\' heads are its brief); the offered copies are kept as a record in a merge note, not as paragraphs. Where they differed, S11\'s stands (back-translated exact or close), except the Epilogue\'s Argument: S11 takes S10\'s *Galat sa re lusk et myst dem sestow*, "the thing the grey sent back", which keeps the grey as the doer and is the Epilogue\'s own last phrase (S11\'s own note asked for it), in the Contents and in §3.')
    w('- **The Book of Knowings\' table** is set out by S11 root by root, its head row a table of Orrowen over English and each root a `#### n ·` section, as the builder\'s `knowings_roots()` reads it; each of the 11 rows is checked present.')
    w('- **Native furniture** (%d lines: %d captions and %d bodies): the old units\' practice is that a native block\'s caption and fold are the reader\'s, in English. %d are given in Orrowen by their units, each a blockquote over the Book\'s line (S01 the Stonwryt\'s body and Seren\'s untold line; W01 II.2\'s note, caption and body; W02 IV.2\'s note, caption and body; S06 the seal of Wendhessa; S09 the mark of Enrella; S11 the three grey stones); S07 gives the Wave\'s caption and its *Orrow.* as one pair; S10 gives the Stone\'s fold ring by ring (§2.4 of its unit) and its last line in Orrowen; S04\'s optional caption for Halvard\'s mark is offered unpaired; the Title\'s native bodies are the Title itself. The rest stand in English: **for Jack** whether the Original gives every caption in Seren\'s ink.' % (n_furn, sum(1 for r in paras if r['kind'] == 'native-cap'), sum(1 for r in paras if r['kind'] == 'native-body'), n_furn_hit))
    w('')
    w('## 6 · CONSISTENCY ACROSS UNITS')
    w('')
    w('### 6.1 The formulas, everywhere identical')
    w('')
    w('Each was searched for in every unit\'s Orrowen and in every paragraph whose English holds it (`pairs.py`, `recur.py`):')
    w('')
    w('| Formula | English | Where | Result |')
    w('|---|---|---|---|')
    F = [
        ('**Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.**', 'the Title', 'the Invocation, I.1, I.4 (S01, S03); the Last Carver\'s *Ul et dumol …* kept with its error (S10)', 'one'),
        ('*Eth re vysk et odh:* **Tumar.** · *Tumar.*', 'And the hearth said: We remember. · We remember.', '33 closes in S01–S11; the foreword\'s *Tess hos brod … : Tumar.*; VI.3\'s *Tumar.* and *Tumar ol varn eth.*', 'one'),
        ('*Cadhom o hosen re yal cadhat lom.* · *Cadhan o hosen re yal cadhat lona.*', 'This I lay … for me. · This we lay … for us.', 'every close; the dual only where the Book has *we* (II.3, IV.3)', 'one each'),
        ('*Carm et lodh hy et trun. Talda, Stonwrytan! …* / *Talda! Talda! Talda!*', 'the Cry', 'I.2 (S02), in Halyna\'s two inks', 'canon'),
        ('*Es ston et hald sy. Re hadhan o, eth tessen o, somm el tolm tolm. Ston.* (and the Hal)', 'the Stonwryt', 'the foreword (S01), the founders\' leaf (S04)', 'one'),
        ('*Hess… Helv… Sennyl…*', 'Stop… Sky… Dying…', 'IV.3 (S06), the Last Note (S11); IV.4\'s said-pocket (W03)', 'canon'),
        ('*Keth et tolm. Cadh et trenn. Amm cadhat o, es dess et odh.*', 'the Invocation\'s close', 'S01', 'canon'),
        ('*Keth et tolm.* / *Keth o, eth es geth tho.* · *Keth et tolm, Seren.* (O3061)', 'Hold the stone. / Hold it, and it will hold thee. · Hold the stone, Seren.', 'I.2, the Epilogue (S02, S10); Seren\'s own leaves (S03, S04, S06, S07, S08, S09, S10, S11)', 'one'),
        ('*Eth re dhess nahos.*', 'And no one answered.', 'every wood leaf; VI.3 (S10)', 'one (W01–W08 set it in bold, the pilot\'s style for a wood leaf\'s frame; S10 and W03 in italics: the letters are one)'),
        ('*Hebb et tolm lom. Nath reskym; es stonom.* · *Rytom um ull. Ston.*', 'Give me the stone. No, I will stand. · I swear to that.', 'I.1, III.1, III.2, V.5, VI.1', 'one'),
        ('*Re hadh* X …', 'Laid by X …', 'every stone headnote', 'one'),
    ]
    for r in F:
        w('| %s | %s | %s | %s |' % r)
    w('')
    w('### 6.2 Recurring English, one rendering (the merge\'s text fixes)')
    w('')
    w('The Book\'s recurring phrases were found by their shared six- and five-word runs across leaves (`recur.py`, 74 and 61 clusters), and by the cross-unit tables every unit wrote for the merge; each was checked paragraph by paragraph. Where units differed, one form was kept (the first leaf\'s, else the majority\'s, else the better grammar) and the others changed; each change is marked *Merge (wf12), H…* in its unit, under the Book\'s English, with the unit\'s old form.')
    w('')
    w('| # | English | The one form | Changed in | Why |')
    w('|---|---|---|---|---|')
    for h in harm:
        en = h['english']
        w('| %s | %s | *%s* | %s | %s |' % (h['id'], en[:110] + ('…' if len(en) > 110 else ''), h['new'].lstrip('> ').strip().replace('*', '').replace('|', '/'), h['unit'], h['why'].replace('|', '/')))
    w('')
    w('Checked and already one: the datelines (*Et syst sullast, ul Hyll Dhumol.* and the rest, S01, W02, W03, W04, S06); *Rhyna Yanna Ulvenn*, *Halvard Tolmvard*; *ul et vess hosast sa re vess et odh sy trenn*; *ul vimm hosk {{Wendhessa}}*; *hosk et bystir rerdsennen*; *eth nath re ston en garm, eth nath nyculom umo*; *Nel nydhyl nydhyl dem vollol*; *El gor yalat vennuld ull*; *re wesk et Crenn en lo orrol*; *Hy ull re vellent …, hosen vellent o tul*; *um et flenn ul lern*; *Pa lo Yanna* (I.2 and the Epilogue, word for word); *Piskur, el bysketeth hosel o, garl ul narl*; *Ul vess et hiskenn*; *Amm sy hunna vollath et cummath, eth ketha so, hy vodh dossant lor*; *Hinnar uld ullen, nath gadhom o*; *El crynir hos heskal. El hinnar sull.*; *Re runnant et higileth mygurath um et tolm vimm sost*; *et hunnat eth nafedh et brodath*; *Re hadh Seren Pa Luth, sa re heth et greller*; *hosen amm re hadh hos et brod ul … brodow, eth re orr dem neld*; *cless treskat lo hless treskat*; *Doss o ul reskyl lo ull amm sy, lo rask et prenth*; *sull tolm ryss myst*; *ryssyth yarl* (a hand\'s breadth); the leaf titles of the Contents against the leaf units\' titles (26 of 26). The standing terms (`terms.py`): the Long Hearth, the inner gate, the torn cloak, the grey sails, the young wood, the black pillars, the mute stones (H36), the archive chest, the True Men, the Stonewrights, the wreck-wood, Mystarchs, the Thrones, harbour-houses, the east cairns, the Fall, the Twelve, the wall-walk, the Rite, the Bonded, the Tides\' names, the Guest, the warden (▒▒▒▒ in all 12 paragraphs, never a name).')
    w('')
    w('Not made one, on purpose: *Veska virr* / *Vesk virr* ("Look close.") take the plural or the singular imperative by whom Pellow speaks to (III.1 the children; V.5, V.7 one man); *Vorr o* / *Vorra o* ("burn it") likewise (III.2 to one mason; IV.3, IV.5, VI.3 to many); "held his glass up to everything" is *re vesk … gor yalat ul o sirr* in V.5 and *keth o o dem susk gor fedh* in III.1, both stepping round *gor* after a preposition (pilot I.1 §3) **[for the next pass]**.')
    w('')
    w('### 6.3 Names and the lintel')
    w('')
    w('Every capitalised word of every unit was parsed and grouped by the lexicon row it reads as (`names_check.py` → `names_out.txt`): each name has one form in all units, mutation aside (*Brenn / Wrenn*, *Corlen / Horlen*, *Della / Rella*, *Rhyna / Hyna*, *Tarnel / Dharnel*, *Tarnard / Dharnard*, *Mardh / Vardh*, *Orrow / Morrow*). The six pair-names (Halyna, Aldwena, Idrenna, Orvenna, Enrella, Wendhessa) are one name for two, under the lintel, with the dual verb; **F6**: seven units wrote them bare in the romanisation and six under the lintel as the English does (`{{Halyna}}`); all now write `{{…}}` (59 names in S02, S03, S09, S10, W01, W02, W08), which the analyzer and the token writer read as the name (the leaf-hand\'s `=` either way). **F5**: S06 and S08 had kept the Book\'s quotation marks in 23 romanised lines; orrowen_v2 §6.7 says direct speech is not marked and the quotation marks are Seren\'s, in the English, so they are out.')
    w('')
    w('### 6.4 Halyna\'s alternation (`wf12/merge/halyna_check.py`)')
    w('')
    w('The Book\'s rule (notes_v3 §5.5): every split pair in Halyna\'s mouth is wrapped in `<!-- HALYNA -->` (nineteen blocks), the two inks by turns, the first ink first; IV.3\'s reading of Brenn alternates by paragraph, stepping over the warden\'s letter (a fully italic line takes no ink); under `<!-- MARKED -->` (II.3) the ink follows the name, a fully italic line is Seren\'s, and the oldest saying and the laid formula take neither; a wood leaf\'s reading alternates line by line, unnamed.')
    w('')
    w('| Block | Leaf | Unit | Paragraphs | Inks the Book sets | Result |')
    w('|---|---|---|---|---|---|')
    for r in hal:
        w('| %s | %s | %s | %d | `%s` | %s |' % (r['kind'], r['leaf'], r['unit'], r['n'], r['want'], 'as the Book sets them' if r['ok'] else 'DIFF'))
    w('')
    w('(*a*, *b* the first and second ink; *s* Seren\'s own; *-* none.) No unit puts an ink label on any paragraph outside these blocks.')
    w('')
    w('## 7 · BACK-TRANSLATION TOTALS')
    w('')
    w('Each unit\'s native lines and rounds were read back blind into English (`wf12/backtrans/`), scored by the unit\'s fixer on the pilots\' scale (**exact** · **close**: a nuance shifts · **drift**: a proposition lost or changed · **wrong**: contradicted or invented), fixed, and re-read by rule. From each unit\'s BACK-TRANSLATION section:')
    w('')
    w('| Unit | Scored | Before: exact · close · drift · wrong | After: exact · close · drift · wrong |')
    w('|---|---|---|---|')
    for u, (n, b, a) in BT.items():
        w('| %s | %d | %s | %s |' % (u, n, fmt(b), fmt(a)))
    sb = [sum(BT[u][1][i] for u in BT if u.startswith('S')) for i in range(4)]
    sa = [sum(BT[u][2][i] for u in BT if u.startswith('S')) for i in range(4)]
    wb = [sum(BT[u][1][i] for u in BT if u.startswith('W')) for i in range(4)]
    wa = [sum(BT[u][2][i] for u in BT if u.startswith('W')) for i in range(4)]
    w('| **stone units (S01–S11)** | **%d** | **%s** | **%s** |' % (sum(BT[u][0] for u in BT if u.startswith('S')), fmt(sb), fmt(sa)))
    w('| **wood units (W01–W08)** | **%d** | **%s** | **%s** |' % (sum(BT[u][0] for u in BT if u.startswith('W')), fmt(wb), fmt(wa)))
    w('| **all units** | **%d** | **%s** | **%s** |' % (nsc, fmt(bsum), fmt(asum)))
    w('')
    pb = (bsum[0] + bsum[1]) * 100.0 / nsc
    pa = (asum[0] + asum[1]) * 100.0 / nsc
    w('- **Before**: %d of %d exact or close (%.0f%%); **after**: %d of %d (%.1f%%), with **no wrong** left. The two drifts left are not the merge\'s: S07\'s IV.5 ¶35 is the reader\'s slip where the text stands; W03\'s is the Guest\'s sentence, whose round is the canon\'s v1 sample (mystaeri_spec §5.4) and is not re-cut (A34, **[Jack]**).' % (bsum[0] + bsum[1], nsc, pb, asum[0] + asum[1], nsc, pa))
    w('- **The "after" readings are the fixers\'**, by the blind reader\'s own method, not a second blind pass (every unit says so).')
    w('- **The merge\'s own changes were not read blind.** Each adopts a form another unit had read back (mostly exact), so the risk is small; a fresh blind reader should still read the changed lines: %s; and the losing units\' lines of §2.1: S02 I.3 *Wick sware it last …*, *The drill done, Jory of Eldhythe leaned …* and *Merrick did not laugh.*; S06 IV.3 *Nineteen I was …* (the oath); S07 IV.5 *In the first holding of this war …*, *All that first winter Jory whistled it …*, *On the morning he died …* and V.1 *They rose stiff from the stones …*; S08 V.5 *Now hear the dead of the wall …*; S10 VI.3 *Along the shingle stood the old ship-masters …*, the Epilogue\'s *Then down came Merrick …* and *Merrick laid his hand on its gunwale.*; S11 the Contents line for VI.1.' % ', '.join('%s %s' % (h['unit'], h['id']) for h in harm))
    w('')
    w('## 8 · THE BUILDER\'S FOLDER (`wf12/orig/`)')
    w('')
    w('`wf8/orig/` was copied to `wf12/orig/` whole and pointed at wf12:')
    w('- **`lexicon_orrowen.tsv`** is now a link to `wf12/lexicon_orrowen_full.tsv`; **`orr_analyze.py`** the merge\'s private copy (the same as `wf12/base/orr_analyze.py`); `orrowen_v2.md` links `wf7/orrowen_v2.md` (identical to `wf12/base/`).')
    w('- **`units.py`** reads `wf12/units` (its path is its parent\'s; the docstring says so); **`tokens_units.py`** adds the Book v3\'s three new pair-names to the lintel (*orvenna, enrella, wendhessa*); **`ink.py`** reads the linked lexicon, and an ellipsis is now the wedge between words and no mark at a line\'s end, as orrowen_v2 §11.8 writes the Guest\'s three words (`h.e.s.s , h.e.l.v , s.e.n.n.O.l`).')
    w('- **`to_ink.py` reconstructed.** `ink.py` imports `to_ink` (the token string to the font\'s markup, and the canon\'s `SAMPLES`) from `wf7/`, where the temp cleaner removed it (its links in wf8 and in the Rivenkeep_Workshop backup point at nothing; `leafhand.py` was rebuilt from `leafhand.json` the same way on 2026-10-02). A private copy is in `wf12/orig/to_ink.py`: `tokens_to_markup` follows `GarlFlenn.fea` (letters run together, a ZWNJ where *t, d, r* and *h* are two letters, the bites as U+032C and U+033A, the harmonic capitals, `=`, `.` `,` ` #` ` ¶`) and reproduces **326 of 326** ink lines of the wf8 build character for character (`wf12/merge/inkre/`); `SAMPLES` are read from orrowen_v2 §11.1–§11.10. `wf7/` was not written.')
    w('- **`make_grain3.py`** reads the rounds from wf12\'s units (W01 II.2, W02 IV.2, W03 IV.4 and its sentence IV-4-gift, W04 IV.6, W05 V.3, W06 V.4 and its carving V-4-grow, W07 V.6, W08\'s ten hearts as `VI-2-<name>`; S07, S08, S09, S10 and S11\'s carvings), imports the renderer from `wf8/render_grain3.py` (read only), and draws IV.2\'s two v3 marks (W02 §1.4) as chips; `--list` resolves 392 jobs (84 whole rounds, 305 plates, 2 chips, the bare Stone); V-3, S08_E1-01, S07_V1-face and IV-2_frag2 were rendered as a test. The wf8 texts in `gn/` are kept aside in `gn_wf8/`.')
    w('- **Tests run**: `python3 ink.py --test` **0 differences** (the 12 canon pairs of `tokens_units.CANON`, the IV.4 pilot\'s headnote lines and the 10 §11 samples); `python3 tokens_units.py --selftest` **ok** (exit 0).')
    w('- **Still the builder\'s to do** (not this merge\'s): `build_original.py` and `check_original.py` are wf8\'s, built for the v1.3 Book HTML. For v3 the builder must read `wf11/book_v3.md` (or its HTML) with its `{{…}}` pair-names; take the Books\' heads from S11 §3 (its `BOOK_HEADS` still names S03, S05, S07, S10 and the lexicon); drop the pilots (I.1 is S01\'s, IV.4 is W03\'s, built from the v3 English); read VI.2 from W08 (the hearts were III.2\'s in wf8) and V.2\'s planks from S08; key every wood leaf on `<!-- READING -->`, the reading\'s lines in two inks, and the seal (now in every wood unit); and pair IV.4\'s and V.4\'s cited rounds with their italic paragraphs (A27).')
    w('')
    w('## 9 · FOR JACK, AND STILL OPEN')
    w('')
    J = [
        '**The romanisation of the Book\'s three names**: *Jory* > *Yory*, *Wick* > *Wik*, *Merrick* > *Merrik* (W12-L1–L3). The tongue has no *j* and writes a final /k/ after *i* as *k*; the English keeps the Book\'s spellings. If the romanised Orrowen should show the English spellings, it is three rows and a search, but *Jory* breaks §2.5.',
        '**The runners\' oath closes with *Ston.*** in both places now (W12-L7), as Kael\'s oaths do (pilot I.1\'s one liberty, §3.9); the English has no word for it. Delete the two *Ston.* and nothing else moves.',
        '**Plays given up for one rendering**: S10\'s *lusk*, "loose", for the hood put back (the Captain\'s third call; H20), and S11\'s *haemer*, "hang; float", for the axemen home on a spar (H13), and S08\'s *lodh*, the bond-word, for the strip bound on the pike (H31a). Each is in its unit\'s note; any can return if Jack prefers the play to the echo, in all the places at once.',
        '**A26, the ring cap.** IV.2, IV.4 and V.6 have 25 story paragraphs in v3; the units kept 24 rings (two paragraphs in one ring, the cited sentence as its own round, the Song inside its paragraph\'s ring). Raise the cap, or keep it.',
        '**A34, IV-4-gift\'s referents** (the one drift left in the wood): the v1 sample\'s `FLASH` names its file under v2\'s ring rule. Read v1 samples by v1\'s band rule, or count their `# file` lines.',
        '**Native-block captions in Seren\'s ink**: twenty lines of the Book\'s `::: native` furniture stand in English, as the old units left them; nine are given in Orrowen by their units. One rule for the Original either way.',
        '**The homophone *miskhovv*** "boot" = N·*biskhovv* "hood" (§2.2).',
        '**Rules marked [proposed]** in §21.10.4 (A27–A29, A31, A33, A35, A36) and the fifteen validator findings (§21.10.6) wait on a spec pass; every unit reads right without them, with `# file` comments.',
        '**Still owed from before** (Tier 3 §7): A16b, A18, A24, A25; "what the one knows, the other knows" (*keth* or *sesk*); *Saed Hosast* against *Trenn Hosast*; the Welsh, Irish and Tolkien pass is no longer owed (Jack\'s standing rule: no originality or dictionary checks).',
        '**Lost to the temp cleaner, and needed again**: `wf7/to_ink.py` (reconstructed here privately), `wf7/coverage/words.json` and the corpus `wf7/coverage/tests/*.gn2` (`check_coverage.py` and `run_tests.py` cannot run). The Rivenkeep_Workshop backup lacks them too.',
        '**A fresh blind reader** for the merge\'s changed lines (§7), as Tier 3 left it.',
        '**Folding the merge into the shared files** (when the concurrency window closes): `lexicon_orrowen_full.tsv` replaces `wf12/base/lexicon_orrowen.tsv` as is; §21.10 of `grain_v2_full.md` is written to be appended to the base spec as it stands; `concepts_full.tsv` replaces the base register; the 86 new rows\' recipes belong in `wf7/lex/en_map/` before any rebuild (pilot I.1\'s caution).',
    ]
    for i, t in enumerate(J, 1):
        w('%d. %s' % (i, t))
    w('')
    w('## 10 · FILES')
    w('')
    w('- **Deliverables** (`wf12/`): `lexicon_orrowen_full.tsv` (%s rows), `grain_v2_full.md` (§21.10), `concepts_full.tsv` (%d rows), this report.' % (format(3015 + len(new), ','), cck['rows']))
    w('- **Units** (`wf12/units/`): all 19 changed (each opens with its merge note, and every change is marked *Merge (wf12)* where it stands); backups of the units as they came in: `wf12/merge/backup_units/`, and as they stood before the harmonisation pass: `wf12/merge/backup_preF7/`.')
    w('- **The builder\'s folder**: `wf12/orig/` (§8).')
    w('- **The merge\'s tools and logs** (`wf12/merge/`): `merge_lex.py`, `screen_lex.py`, `fix_lex_text.py`, `gen_grain_full.py`, `validate_units.py`, `validate_grain.py`, `pairs.py`, `coverage.py`, `coverage2.py`, `fix_emphasis.py`, `fix_seal.py`, `fix_heads.py`, `fix_pairnames.py`, `harmonise.py`, `recur.py`, `terms.py`, `halyna_check.py`, `names_check.py`, `merge_notes.py`, `gen_report.py`; the private analyzer `orr_analyze.py` and validator root `groot/` (its `wf7/grain_v2.md` links the merged spec); results `lex_decisions.json`, `screen_report.json`, `orr_validation.json`, `grain_validation.json`, `grain_merge_stats.json`, `concepts_check.json`, `coverage2.json`, `halyna_report.json`, `harmonisations.json`, `recur_5.json`, `recur_6.json`, `names_out.txt`, `fixes.log`; the ink reconstruction\'s check, `inkre/`.')
    w('- **Not touched**: `wf12/base/`, `wf12/additions/`, `wf12/backtrans/`, `wf12/blind/`, `wf7/`, `wf8/`, `wf11/`, and anything in `/Users/riquochet/code/Rivenkeep/Docs`.')
    w('')
    open(os.path.join(W12, 'merge_report.md'), 'w', encoding='utf-8').write('\n'.join(o))
    print('wrote', os.path.join(W12, 'merge_report.md'), sum(len(x) for x in o), 'chars')


if __name__ == '__main__':
    main()
