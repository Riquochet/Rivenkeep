#!/usr/bin/env python3
"""wf12 merge: build wf12/grain_v2_full.md = wf12/base/grain_v2_full.md (word for word) + a new §21.10, the grain
additions of the wf12 units (the Book v3.0.0) merged: one compounds table and ONE compounds block for the validator, one
table of decoder readings (A15, continued), the rules and calls the units proposed, the findings for the validator, and
the conflicts settled.  No new sign.  Also writes wf12/concepts_full.tsv (the base register + a row for every new
compound and every reading with a checkable fragment) and grain_merge_stats.json."""
import collections, importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
BASE = os.path.join(W12, 'base', 'grain_v2_full.md')
OUT = os.path.join(W12, 'grain_v2_full.md')
CBASE = os.path.join(W12, 'base', 'concepts_full.tsv')
COUT = os.path.join(W12, 'concepts_full.tsv')
ADD = os.path.join(W12, 'additions')

# ---- the compounds, merged (unit order); the gloss is the validator's "cls:reading|ing|plural-or-past" string
COMPOUNDS = collections.OrderedDict([
    ('DEEP+LIE', dict(units=['W01', 'W05'], gloss='v:lie long (sleep long; a long sleep)|lying long|lay long', soft='eir·rhir',
                      means='lie long; sleep long, a long sleep', der='DEEP *eir* "deep; old; long" + LIE *rhir* "lie down; lie; sleep", as §21.7\'s `DEEP+HOLD` *eir·thein* "hold long"',
                      where='II.2 r3, the trees\' long sleep (W01); V.3 r18, "Long we lay in the cold" (W05)')),
    ('NEW+TREE×3', dict(units=['W01'], gloss='n:young trees (saplings)|', soft='lea·thaelen', means='young trees: saplings (of trees, never children)',
                        der='NEW *lea* "new; young; green" + TREE×3 *thaelen* "trees, a grove": SAPLING×3\'s soft reading laid out in its two parts, so that a leaf that has both keeps `SAPLING` for the children',
                        where='II.2 r5, r22, the pale saplings that answer the singing')),
    ('DEEP+HEAR', dict(units=['W03', 'W06'], gloss='v:listen long (hear long)|listening long|', soft='eir·seinn', means='listen long; a long listening',
                       der='DEEP *eir* "long" + HEAR *seinn* "hear; heed; listen"', where='IV.4 r14, "his long listening" (W03); V.4 r13, "Long we listened from behind the breath" (W06)')),
    ('DEEP+CARRY', dict(units=['W03'], gloss='v:carry long|carrying long|', soft='eir·var', means='carry long; bear a long while',
                        der='DEEP *eir* "long" + CARRY *var* "carry; bear"', where='IV.4 r20, "old arms, two pairs, slow, a long while"')),
    ('LEAN+BURN', dict(units=['W03'], gloss='n:a near fire (fire at hand)|near fires', soft='ilen·esth', means='a near fire; fire at hand',
                       der='LEAN *ilen* "lean toward" (the register\'s *near*) + BURN *esth* "burn; fire"', where='IV.4 r20, "and fire, near and far"')),
    ('EDGE+BURN', dict(units=['W03'], gloss='n:a far fire (fire at the edge)|far fires', soft='enth·esth', means='a far fire; fire at the edge (with `{most}` on the edge: the farthest)',
                       der='EDGE *enth* "an edge; the rim" (the register\'s *far*) + BURN *esth*', where='IV.4 r20 (`EDGE{most}+BURN`)')),
    ('BENEATH+GO', dict(units=['W04', 'W08'], gloss='v:go low (go under, go in under; beneath the water-line)|going low|', soft='senn·rei',
                        means='go low; go under, go in under (beneath the water-line)', der='BENEATH *senn* "beneath; low; go under" + GO *rei* "go", as `BENEATH+WOUND` and `BENEATH+RISE` (§21.9.2)',
                        where='IV.6 r12, "We went into them burning, low" (W04); VI.2 Ralensaen r12, "Root by root we went under" (W08)')),
    ('BREAK+WOOD', dict(units=['W05'], gloss='n:broken wood (wreck-wood)|broken boards', soft='rhass·veir', means='broken wood; wreck-wood',
                        der='BREAK *rhass* "break; a crack" + WOOD *veir* "wood; boards", as `BREAK+HOLD` and `BREAK+SQUARE` (§21.9.2)', where='V.3 r1, "Now are we broken wood"')),
    ('BURN+GO', dict(units=['W05'], gloss="v:go as fire (the fire's going: a shot of fire)|going as fire|throw fire", soft='esth·rei',
                     means="the fire's going: a shot of fire; with the causative, throw fire", der='BURN *esth* + GO *rei*, as `AXE+GO` (§21.9.2) is the iron\'s coming',
                     where='V.3 r11, "We threw one fire at the stone that had spoken" (`BURN#1+>GO`)')),
    ('BURN+FIND', dict(units=['W05'], gloss="v:find by fire (the fire's finding)|finding by fire|", soft='esth·veass', means="the fire's finding: what a shot of fire finds",
                       der='BURN *esth* + FIND *veass* "find; come upon", beside `AXE+FIND`', where='V.3 r11, "Of what our fire found there, the grain hath naught" (`→ ∅`)')),
    ('FALL+LEAF×3', dict(units=['W07'], gloss='n:the falling leaves (the leaf-fall: autumn)|', soft='nenn·lelen', means='the falling leaves: the leaf-fall, autumn',
                         der='FALL *nenn* "fall" + LEAF×3 *lelen* "leaves": the head a thing, so the mark names its own file (§11.2); beside §18\'s likeness `~LEAF+FALL`',
                         where='V.6 r20, "at the leaf-fall, when its ring was laid"')),
    ('NEW+DYING', dict(units=['W07'], gloss="v:die young (before one's years)|dying young|", soft='lea·veas', means="die young; die before one's years",
                       der='NEW *lea* "new; young; green" + DYING *veas* "die"', where='V.6 r21, "They that cried for war died ere their years"')),
    ('ROOT×3+GO', dict(units=['W08'], gloss='v:walk on roots (as a pillar walks)|walking on roots|', soft='ralen·rei', means="walk on roots (as a pillar walks; a tree's walking)",
                       der='ROOT×3 *ralen* "roots" + GO *rei* "go": the thing, then the act, as `BLOOD+GO` and `LIVE+GO`; part by part it reads "the root-men going"',
                       where='VI.2 Ralensaen r12, "but walked, as a pillar would walk home"; the reading\'s *Roots, walking*')),
])
CONFLICTS = [
    ('G9', 'W01, W05', '`DEEP+LIE` glossed "sleep long (a long sleep)" (W01, the trees\' sleep) and "lie long" (W05, the wreck in the cold)',
     'one entry: "lie long (sleep long; a long sleep)": LIE\'s own reading is "lie down; lie; sleep", so both senses are the sign\'s', 'none (the units\' literal readings now print the merged gloss)'),
    ('G10', 'W03, W06', '`DEEP+HEAR` proposed twice: "listen long" (W03) and "listen long (hear long)" (W06)', 'one entry, W06\'s gloss (it holds W03\'s)', 'none'),
    ('G11', 'W04, W08', '`BENEATH+GO` proposed twice: "go low (go in under; beneath the water-line)" (W04) and "go under (go low, go in under)" (W08)',
     'one entry: "go low (go under, go in under; beneath the water-line)"', 'none (the readings print the merged gloss)'),
    ('G12', 'W04, W05', '"in the night": the DARK band on an empty cell with an *in* runner to it (W04) and the DARK band over the doer\'s year (W05)',
     'both stand, by what the night does in the knowing: a night *in* which a thing happens is the band as a thing, reached by `→in`; a night the doer is *in* is the band over its year (A20)', 'none'),
    ('G13', 'W04, W06', '"our kin": `BLOOD×3` (W04) and `BLOOD×3 → @12` (W06)', 'one row: `BLOOD×3`, kin, a referent of its own, with a runner to us where the kin is a tree\'s', 'none'),
]


LEAF = {'W01': 'II.2', 'W02': 'IV.2', 'W03': 'IV.4', 'W04': 'IV.6', 'W05': 'V.3', 'W06': 'V.4', 'W07': 'V.6', 'W08': 'VI.2'}


def a15_rows():
    rows = []
    for f in sorted(os.listdir(ADD)):
        if not f.endswith('_grain.md'):
            continue
        u = f.split('_')[0]
        L = open(os.path.join(ADD, f), encoding='utf-8').read().split('\n')
        i = 0
        while i < len(L):
            if re.match(r'^\|\s*English\s*\|\s*Grain\s*\|', L[i]):
                i += 2
                while i < len(L) and L[i].startswith('|'):
                    cells = [c.strip() for c in L[i].strip().strip('|').split(' | ')]
                    if len(cells) >= 3:
                        where = ' | '.join(cells[2:])
                        if not re.search(r'\b[IV]+\.\d', where):
                            where = LEAF[u] + ' ' + where
                        rows.append(dict(unit=u, en=cells[0], grain=cells[1], where=where))
                    i += 1
                continue
            i += 1
    # one row where units said one thing: same English (case, emphasis and brackets aside)
    def k(e):
        return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', re.sub(r'\([^)]*\)', '', e))).strip().lower()
    merged = collections.OrderedDict()
    for r in rows:
        merged.setdefault(k(r['en']), []).append(r)
    out = []
    for key, rs in merged.items():
        if len(rs) == 1:
            r = rs[0]
            out.append(dict(en=r['en'], grain=r['grain'], where=r['where'], units=[r['unit']]))
        else:
            out.append(dict(en=rs[0]['en'], grain=' **Or** '.join(dict.fromkeys(r['grain'] for r in rs)) if len(set(r['grain'] for r in rs)) > 1 else rs[0]['grain'],
                            where='; '.join('%s (%s)' % (r['where'], r['unit']) for r in rs), units=[r['unit'] for r in rs]))
    return rows, out


RULES = r'''
#### 21.10.4 Rules and calls the units proposed [rule, where the validator already reads it; *[proposed]* otherwise; **[Jack]** for calls]

**A26 · The ring cap and the v3 leaves** **[Jack]** (W02, W03, W07). v1 §3.2 caps a telling at 24 rings ("V.6, the longest leaf, has 24 paragraphs"), and the validator's H05 errs above 24. v3's IV.2, IV.4 and V.6 have **25** story paragraphs. The units kept the cap: IV.2 lays its ¶24 and ¶25 in ring 24 (two blocks over their own English); IV.4's twenty-fourth paragraph is the Guest's sentence, its own cited round (A27); V.6's ring 23 holds the groves' paragraph and the Song its colon opens. The cap was a measurement of v1.3, not a law of the wood: if it is raised to 25, IV.2 re-cuts as 3 / 17 / 5 and V.6's Song takes its own ring under our HOLD, with no other change.

**A27 · A paragraph that is a cited round is that round, not a ring** *[proposed]* (W03 #1, W06 #1). A fully italic paragraph of a wood leaf's story that is a carving or a sentence cited whole (IV.4's *Stop the felling …*, the gift's own round, mystaeri_spec §5.4; V.4's *Grow until the shore is silent.*, §5.8) is drawn as its own round beside the ring that cites it by its root (§8), and takes no ring of its own. For §11.2 item 1; the Legends builder pairs such a paragraph with the cited round (the Legends builder's `p.inscr`).

**A28 · The causative counts with the foot station** *[proposed]* (W05 #1, W06). §5.4 puts `>` (the chevron at the foot) in the "under the foot" station with *again, still, last, slow, gently*, one mark per station; the validator's M04 counts only the fringe, so `>GO{again}` passes. The units step round it: a sending counted is `>GO@1 … @4`, "another" `>GO@2`, slowness set on the likeness. For M04.

**A29 · A cut-pocket's reading** *[proposed]* (W05 #2, W06 #3). Every cut-pocket reads "an older carving, cited", even a carving cut whole that is new where it stands (V.3 r9; V.4 r17) or a lesson given (V.3 r3). Proposed: "a carving: […]", keeping "an older carving, cited" for a pocket that holds a half-size line root with an ordinal or a ray to an earlier carving.

**A30 · One questioned mark to a file** [rule] (W05). Possibilities in a row that do not rule each other out (*may …; may …*) take one questioned mark to a file; two questioned marks on one file are always A6's "either … or, and we do not know which".

**A31 · A ray joins its two ends only** *[proposed]* (W05 #8). A ray (`ray f: rI/Y–rJ/Y`) makes its two ends the same one; the marks it passes on its file between them are not made the same. For §3.7.

**A32 · A band may wrap** [rule; the renderer] (W07 #2). A band laid clockwise across the axis (`band DARK files 12–0`) is one band: the validator reads it so (`conds_at`) and §13.2's grammar allows it; §3.6 and the renderer should draw it as one.

**A33 · A telling's rings follow the telling, not its wood** *[proposed]* (W06 #2). mystaeri_spec §5.8's GROW round, in GN v2, is a telling of two rings on green wood, which §3's table gives one; the validator reads it as a telling (A10). A line in A10 would settle it.

**A34 · A v1 sample's referents** **[Jack]** (W03 #9). In IV-4-gift (mystaeri_spec §5.4, kept whole by §17) `FLASH` stands first on file 3 in ring 7, so §11.2's ring rule makes the hard light file 3's referent, and the validator reads ring 10's `DYING` "Flash (hard light) dies" where the canon reads the pillars' breath dying. Proposed for §17: a v1 sample's referents are read by v1's band rule, or its `# file` lines count as part of its GN; else A16's belongings take in a thing's own light. Not re-cut.

**A35 · `files all` in the v1 samples** *[proposed]* (W03 #4). v1's *band MIST r4 all files* was written `band MIST files all` in `wf8/grain3/texts/GIFT.gn2`, which the validator cannot read (P02); written `files 0–15` it is clean, and the units write it so. Either the validator reads `files all`, or every v1 sample's v2 text writes `0–15` (§13.7).

**A36 · `AXE+GO`'s gloss** *[proposed]* (W03 #2). §21.9.2's `AXE+GO` ("the iron's coming (the felling going on)", W06 wf8) catches every ligature keyed `AXE+GO`, including the pilot's `AXE+GO½` ("the blade goes a little way"); IV.4 r13 was re-cut round it. Proposed: "the iron goes (comes; the felling goes on)", which serves both. **Not applied here**: IV.2 (W02) reads r21 by the present gloss.

**A22, continued · Traps the register should name** [rule] (W02 §3, W06, W07, W08).
- `ROOT×3+!HOLD` is not "the roots let go": the ligature is `ROOT+HOLD` (*ralthein*, remember, A14) mirrored, *forget*. Cut `!HOLD →` the thing let go, `→with ROOT×3`.
- A modifier is read as the doer: `MORROW+GROW` reads "the morrow grows"; the future is a `→in MORROW` runner.
- A file of the grey takes act heads only: a thing-sign first on it (`FLASH`, `THIN`) becomes its referent for the rest of the round; `FLASH+OPEN` and `THIN+LIVE` keep the grey.
- `SQUARE` on a `CASTLE` file is a belonging (the havens' stone): give a stone its own file.
- A ligature whose head is an act names no referent (`TREE×3+KNOT`, `TIDE@1+BENEATH`): name the thing first and cut the act after it (W06 #5).
- `!HOLD →` an act reads *not feel* it (A15, V.6 r18): "let us go" is `!HOLD? →` us, the thing held (W05 #6); *forget (a people)* is `!ROOT+HOLD →` them (W07).
- `{only}` bounds the mark it stands on (W05 #7): "for naught else" stands on the looking, not the sending.
- `BURN½` outside a pocket is a cited carving (A22): a small fire is `BURN{few}` (W08).
- `!HOUSE+OVER` on the unroofed one's own file reads "we: no roof"; cut it on a placeless file with `OVER → @f` (W08).
'''

FINDINGS = r'''
#### 21.10.6 Findings for the validator (not fixed: `grain_validate.py` is shared; none blocks a unit)

1. **A hollow runner's `~` on a bind's strand is dropped from the readings** (W03 #8): the plain reading's strand branch returns before the hollow and smoothed flags are added, and `--literal` prints no runner's flag. IV.4 r16 now cuts the arms hollow as well.
2. **A band over a celled year** (A20, again: W03 #5, W04 #1, W05 #4, W07 #6): in a celled year a band covers every mark on its file. True in every place the units used it; a band that could name its cells would part them.
3. **`→ ∅` from a thing** is printed by `--literal` as "—to→ []" (W04 #2); a reading rule "what became of it, the wood does not hold" would serve.
4. **Fringe readings that want the register's word**: `GIFT{most}` "give, the most" for §18's *the dearest gift*; `GREAT{most}` "most great hull" for A15's *heavy* (W04 #3); `BURN{few,last}` "burn, few at the last" for *a little fire, at the last* (W08 #3).
5. **The plain reading without `# file` comments** follows A16 only; A16b (§21.9.4) would keep the referents every unit's blind round lost (W01 notes 5–6, W02, W04 #4, W06 #9).
6. **A band-only file is left out of `--literal`** (W08 #1): the harbour, the sea, the nights appear only as a runner's target. Proposed: print a band-only file in its ring, "file f: the water (the sea), the band as a thing".
7. **`>EYE` reads "the making of eye"** (W08 #2): the causative of a thing-class sign is read as a noun; a decoder wants "show" (A15's *show them themselves*).
8. **A lone `AXE` reads "fell with iron"** (W03 #3, W06 #6): a noun reading for a mark that governs nothing (the iron, the blade) would help, as `DOER_NOUN` gives it in a ligature.
9. **`ROOT×3` reads "the root-men (roots)"** (W06 #7): in a grove's file it is the roots.
10. **The literal reading drops the plural under an ordinal and doubles a part's** (`TREE×3@1` "the first tree"; `TREE:boughs×3` "many crown of boughss", W07 #3). Glosses only.
11. **Compounds still gloss the dropped names** (`BOND+ROOT×3` "(Aelralen)", `CARVE+BEARER` "(Sethvaren)", W07 #4): v3 took the names out of the Book (notes_v3 §1.14); a reading for the Original tab should drop the brackets, or Jack may keep them as the wood's own words **[Jack]**.
12. **The blind of place reads "whither" for every to-runner** (W07 #5); A15 says "what" for a seeing, and a carving's blind would want "what" too.
13. **The self-runner** (`→ @f` to its own file and year) is exempt from R15 (W07 #7); the renderer must place its terminal beside its source when the year's cells are full.
14. **§18's `!MOUTH → HOME`** ("no voice among us can call us home") is read *do not speak to home* without §18's row (W07 #8): A15 could carry it, *call (one) home* is MOUTH `→` HOME.
15. **The blind inputs carry the Book** (W01 note 7, W05 #9): the "Where" columns of §21.9 and of these tables quote the Book's English; a blind reader should be given the `json` block and the *Grain* column only.
'''


def main():
    base = open(BASE, encoding='utf-8').read()
    rows, a15 = a15_rows()
    units_c = sorted(set(u for c in COMPOUNDS.values() for u in c['units']))
    rows_c = sum(len(c['units']) for c in COMPOUNDS.values())
    L = []
    L.append('\n### 21.10 Additions from the wf12 units, merged (tier 3 on the Book v3.0.0; 2026-10-03)\n')
    L.append('*The wf12 workflow carved every wood leaf of the Book v3.0.0 whole (II.2, IV.2, IV.4, IV.6, V.3, V.4, V.6 and VI.2: units W01–W08; IV.4 re-cut from the pilot on the v3 English, VI.2 the ten hearts of v1.3\'s III.2 moved and re-cut), and the grain inside the stone leaves (V.2: S08; V.7 and VI.1: S09; VI.3 and the Epilogue: S10; the 47 carvings of the Book of Knowings: S11), each unit writing its grain additions to its own file under the concurrency rule (`wf12/additions/*_grain.md`). This section merges them as §21.9 merged the wf8 units\': one compounds table and **one** compounds block for the validator, one table of decoder readings, the rules and calls the units proposed, the findings, and the conflicts settled. The unit files stay as the record of each unit\'s reasoning. Nothing here goes into `Docs/`.*\n')
    L.append('#### 21.10.1 What was merged\n')
    L.append('- **No new sign.** No unit needed one; §9.1\'s principle held for the whole v3 Book. The stone units (S08–S11) added nothing to the grain; their rounds are v1.3\'s or §21.9\'s, re-validated.')
    L.append('- **%d compounds** from %d rows in %d units (%s), each modifier + head as Seilrhass builds (mystaeri_spec §2.5), its soft reading the compound of the two soft readings (computed, not coined; call §19.8). Three were proposed by two units each (`DEEP+LIE`, `DEEP+HEAR`, `BENEATH+GO`), with glosses that differed in wording; each is one entry (§21.10.7). None repeats a compound of §21.3, §21.7, §21.9.2 or the validator\'s table.' % (len(COMPOUNDS), rows_c, len(units_c), ', '.join(units_c)))
    L.append('- **%d decoder readings** (A15, continued, §21.10.3), merged from the units\' %d rows: rows that said one thing twice are one row, and where two units gave one English two cuts, both are kept as one row (§21.10.7).' % (len(a15), len(rows)))
    L.append('- **Rules and calls** in §21.10.4 (A26–A36, and A22 continued), marked *[proposed]* where the validator does not read them yet and **[Jack]** where they are calls; **findings** for the validator in §21.10.6.\n')
    L.append('#### 21.10.2 Compounds added by the wf12 units\n')
    L.append('Keys follow the validator\'s `lig_key` (every decoration but a part and ×3 is ignored).\n')
    L.append('| Compound | Means | Soft reading | Derivation | Where | Unit |')
    L.append('|---|---|---|---|---|---|')
    for k, c in COMPOUNDS.items():
        L.append('| `%s` | %s | *%s* | %s | %s | %s |' % (k, c['means'], c['soft'], c['der'], c['where'], ', '.join(c['units'])))
    L.append('\nThe one block the validator reads (it takes every `json` block of §21; this one adds the thirteen):\n')
    L.append('```json')
    L.append('{"compounds": {')
    L.append(',\n'.join(' %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(c['gloss'], ensure_ascii=False)) for k, c in COMPOUNDS.items()))
    L.append('}}')
    L.append('```\n')
    L.append('#### 21.10.3 A15, continued: readings a decoder needs from the register\n')
    L.append('A15\'s standing rule: any register reading that is not its sign\'s own gloss belongs in the table. These are the readings the v3 whole-leaf carvings rely on, merged from the units\' tables (W01–W08), in unit order; "Where" names the v3 leaf and ring (the shared rings of VI.2 are the heart\'s own numbers).\n')
    L.append('| English | Grain | Where | Unit |')
    L.append('|---|---|---|---|')
    for r in a15:
        L.append('| %s | %s | %s | %s |' % (r['en'], r['grain'], r['where'], ', '.join(dict.fromkeys(r['units']))))
    L.append(RULES)
    L.append('#### 21.10.5 Corrections to the concept register (applied in `wf12/concepts_full.tsv`)\n')
    L.append('No row of the base register is changed: the units found no register reading that is wrong, only readings it lacked. Every compound of §21.10.2 and every reading of §21.10.3 with a fragment the validator can check has its row in `wf12/concepts_full.tsv` (kind `add`, note `wf12 §21.10`); a reading whose cut is prose only is in the table above and not in the register.\n')
    L.append(FINDINGS)
    L.append('#### 21.10.7 Conflicts between units, and how each was settled\n')
    L.append('| # | Units | The conflict | Settled | Units re-cut |')
    L.append('|---|---|---|---|---|')
    for c in CONFLICTS:
        L.append('| %s | %s | %s | %s | %s |' % c)
    L.append('')
    tail = '\n'.join(L) + '\n'
    open(OUT, 'w', encoding='utf-8').write(base.rstrip('\n') + '\n' + tail)

    # ---- the concept register
    spec = importlib.util.spec_from_file_location('gv', os.path.join(HERE, 'groot', 'wf7', 'grain_validate.py'))
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)

    def frag_ok(fr):
        F = g.Findings()
        try:
            g.check_fragment(fr, F, 'x')
        except Exception:
            return False
        return not [x for x in F.items if x['level'] == 'ERROR']

    out = open(CBASE, encoding='utf-8').read().rstrip('\n').split('\n')
    out.append('# ---- wf12 merge, 2026-10-03: the compounds of grain_v2_full.md §21.10.2 and the readings of §21.10.3 ----')
    n_c = n_r = n_skip = 0
    for k, c in COMPOUNDS.items():
        eng = c['gloss'].split(':', 1)[1].split('|')[0]
        lem = re.sub(r'\s*\(.*?\)', '', eng).strip()
        out.append('\t'.join([lem, k, 'add', 'wf12 %s; §21.10.2; %s' % (', '.join(c['units']), eng)]))
        n_c += 1
    for r in a15:
        frags = [f for f in re.findall(r'`([^`]+)`', r['grain']) if frag_ok(f)]
        if not frags:
            n_skip += 1
            continue
        lem = re.sub(r'\s*\(.*?\)', '', r['en']).replace('*', '').strip()
        out.append('\t'.join([lem, ' ; '.join(dict.fromkeys(frags)), 'add', 'wf12 §21.10.3 (A15); %s; %s' % (
            re.sub(r'\s+', ' ', r['where'].replace('|', '/'))[:200], re.sub(r'\s+', ' ', r['grain'].replace('|', '/'))[:400])]))
        n_r += 1
    open(COUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    stats = dict(compounds=len(COMPOUNDS), compound_rows=rows_c, readings=len(a15), reading_rows=len(rows),
                 concept_rows_added=n_c + n_r, concept_compounds=n_c, concept_readings=n_r, readings_without_fragment=n_skip)
    json.dump(stats, open(os.path.join(HERE, 'grain_merge_stats.json'), 'w'), indent=1)
    print(stats)


if __name__ == '__main__':
    main()
