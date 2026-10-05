#!/usr/bin/env python3
"""wf12 merge: build wf12/lexicon_orrowen_full.tsv = wf12/base/lexicon_orrowen.tsv + every wf12/additions/*.tsv, harmonised.

Private merge tool (scratch; adapted from wf8/tmp/merge/merge_lex.py). Reads the shared lexicon and the unit additions
read-only; writes only wf12/lexicon_orrowen_full.tsv and wf12/merge/lex_decisions.json.

Rules (lexicon_orrowen.md, as the Tier 3 merge applied them):
  * one form = one row; a new sense of an existing form is appended to its `meanings` (canon sense first), never a
    second row (lexicon §4.4);
  * a phrase's class is the class of its last word; a single word's class is its harmony class; a phrase's formation
    is `phrase`;
  * where two units coined different forms for one sense, one is chosen (REPLACED below, each with its reason) and the
    losing units' text is changed (fix_lex_text.py);
  * new rows take ids after the last shared id (O3015), in unit order.
"""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import orr_analyze as oa  # private copy (wf12/merge/orr_analyze.py)

BASE = os.path.join(W12, 'base', 'lexicon_orrowen.tsv')
OUT = os.path.join(W12, 'lexicon_orrowen_full.tsv')
COLS = ['id', 'orrowen', 'hal', 'pos', 'class', 'meanings', 'canon_sense', 'derivation', 'root', 'formation',
        'logogram', 'dry_cut', 'source', 'book_lemmas']


def read(p):
    lines = open(p, encoding='utf-8').read().split('\n')
    hdr = lines[0].split('\t')
    assert hdr == COLS, (p, hdr)
    rows = []
    for ln in lines[1:]:
        if not ln.strip():
            continue
        parts = ln.split('\t')
        assert len(parts) == len(COLS), (p, ln[:80], len(parts))
        rows.append(dict(zip(COLS, parts)))
    return rows


def key(form):
    f = form.strip().lower()
    return f[3:] if f.startswith('et ') else f


def lemmas_union(*lists):
    out, seen = [], set()
    for l in lists:
        for x in re.split(r'[;,]\s*', l or ''):
            x = x.strip()
            if x and x.lower() not in seen:
                seen.add(x.lower())
                out.append(x)
    return ', '.join(out)


def phrase_class(form):
    ws = re.findall(r"[A-Za-z']+", form)
    return oa.word_class(ws[-1]) if ws else 'B'


def strip_prov(d):
    d = re.sub(r'\s*\[wf12 unit[^\]]*\]\s*$', '', d)
    d = re.sub(r';?\s*unit [SW]\d\d \([^)]*\)\s*$', '', d)
    d = re.sub(r';?\s*unit [SW]\d\d\s*(\(wf12\))?\s*$', '', d)
    d = re.sub(r'\.?\s*Unit W0\d \(wf12\)[^.]*\.?[^.]*$', '', d) if 'Unit W01 (wf12)' in d else d
    return d.rstrip('; .') + ('' if d.rstrip().endswith(')') else '')


# ---------------------------------------------------------------------------------------------
# The decisions (each recorded, with its reason, in lex_decisions.json and the merge report)
# ---------------------------------------------------------------------------------------------

# (a) one sense, two (or three) forms: the dropped row, the chosen form, why, and the units whose text changes
REPLACED = {
    ('S02', 'W12-S02-05'): dict(chosen='Yory', why="the tongue has no j (orrowen_v2 §2.5; the banned letters) and its one /j/ is the "
        "worn g written y (§2.4): Yory is the Book's Jory in the ink, as S03, S07 and S08 wrote it (three units against one). "
        "The English keeps Jory. S02's text changed (Jory > Yory, four places)", text='S02'),
    ('S02', 'W12-S02-04'): dict(chosen='Wik', why="the romanisation writes /k/ as k at the end of a word after i (orrowen_v2 §2.4: "
        "Hesk, kyl), and a doubled k is no geminate of the tongue (§2.5): Wik, as S06 and S08 wrote it. The English keeps Wick. "
        "S02's text changed", text='S02'),
    ('S02', 'W12-S02-06'): dict(chosen='Merrik', why="the same rule as Wik (orrowen_v2 §2.4): Merrik, as S07 wrote it, so that the "
        "Book's two names in -ck are romanised alike; the English keeps Merrick. S02's and S10's text changed", text='S02'),
    ('S10', 'S10-05'): dict(chosen='Merrik', why="as W12-S02-06", text='S10'),
    ('S02', 'W12-S02-09'): dict(chosen='hossvell', why="'whistle' is the compound hossvell, 'breath-song' (hoss + S·vell, the head "
        "softened, §3.10), as S03, S05, S08 and S09 made it (four units against two); S02's hoss vell ('breathe a song') and S07's "
        "inthvell ('lip-song') are the same thought. S02's and S07's text changed", text='S02'),
    ('S07', 'S07-08'): dict(chosen='hossvell', why="as W12-S02-09", text='S07'),
    ('S08', 'S08-07'): dict(chosen='garl ul narl', why="'hand in hand' is garl ul narl (ul + N·garl) in II.3, V.1, V.7 and VI.3 "
        "(S04, S07, S09, S10, and Tarnel's saying in II.3 and VI.3); S08's garl lo yarl (V.5, Count VI) is the only other. S08's "
        "text changed", text='S08'),
    ('S02', 'W12-S02-14'): dict(chosen='tolm et haskardath', why="one row for 'the runners' stone': the definite construct, as flenn et "
        "tolm (O2961), which IV.3 uses (S06); I.3's tolm haskardath ('a runners' stone', every haven had one) is the same construct "
        "with an indefinite possessor, regular, and stands in S02's text; the row says so", text=None),
    ('S06', 'S06-07'): dict(chosen='Galat sa re veskym, lymmym o. Nath lymmym galat ullen.', why="the runners' oath is one formula "
        "in I.3 and IV.3. S02's keeps the English's own chiasm (what I saw, I carry. / I carry nothing else: the two 'carry' meet "
        "across the full stop, lymmym o. Nath lymmym) and closes as every oath closes, Ston. (orrowen_v2 §3.9); S06's "
        "Lymmym galat sa re veskym. Lymmym nayalat ullen. opens both lines on the verb. I.3 is where the oath is first sworn. "
        "S06's text changed (IV.3)", text='S06'),
    ('S11', 'O-S11-17'): dict(chosen='lo reskow', why="'for X (in X's stead)' is lo reskow X, 'at X's seat', as VI.1's three captions "
        "say it (Voss, lo reskow Horlen; S09-16); ul reskow is the lexicon's 'somewhere' (O2636), which S09 steps round. S11's "
        "Contents line for VI.1 changed (eth lo reskow et ommatath)", text='S11'),
}
# (b) a row whose form is renamed by a decision above (the row stays)
RENAME = {
    ('S02', 'W12-S02-07'): dict(orrowen='Yory Dhavow Hemm', dry_cut='y.o.r.y letters: t.a.v.o.w @hemm',
                                meanings='Jory of Eldhythe (the Book\'s English Jory; Yory in the ink)'),
}
# (c) a row folded into another new row (one saying, said with and without its first word)
INTO = {
    ('S08', 'S08-08'): 'nath dunn et wadh tul',
}
# (d) the same form already in the base, with a new sense (appended to the base row)
SENSE_NOTE = {
    'dhenth': "(of a scribe) a quill, a pen: a feather cut for the ink (Seren's pen, II.3)",
    'flenn': "a leaf of a tree, of a bough (pl. flenneth, leaves: the slender regular plural, beside the Book's lexicalised "
             "flennath); a letter: a written sheet sent (the warden's letter, IV.1, IV.3)",
    'nasow': "a nest: one bird's place",
    'trenndholm': "a course-stone: a stone of a house's last course, kept when the house is lost (Ebba's, out of Fenholm, III.1); "
                  "the plain sense of 'the tale-stone'",
    'lunn': "(lunn X hy Y) clear a place of a thing, sweep clear",
    'orrol': "(a name, et Orrol) the Road: the column's march up the mountain after the Fall",
    'luth': "a blot: the place on a leaf where a name has been cut out, written ▒▒▒▒ (IV.1, IV.3); luth eth luth, at every blot",
    'hosk': "a seal: the lintel laid across a bundle or a chest, the mark of those who sealed it (IV.3)",
    'derryl': "(a name, et Derryl) the Harvest: the felling of the black pillars, two generations long (IV.1)",
    'kylyl': "(of an answer) a turning aside, a small cleverness (IV.3)",
    'bynt': "(v.) thin, grow thin: of mist and the grey (IV.1: re wynt et myst); the Thin Sky's word",
    'dhyvullat': "a jest ('a laughed thing'), the participle used as a noun, as drunnat 'a drum' (V.7)",
    'tesset': "a doom: a judgement laid on a people, loosed and not called back (Book Five's Argument)",
    'demo': "for him, for it; for its sake (dem in its second sense, conjugated: Tevath, galdat demo. Demo hosel., II.2)",
}
# (e) harmonised meanings for forms reached independently by several units (or merged by a decision)
MERGED_MEANING = {
    'orvenna': "Orvenna: the pair-name of Ormund and Penna, the wall-masters of the Keep; one name for two, with a dual verb",
    'enrella': "Enrella: the pair-name of Enno and Della, the youngest pair of the guild, sealed at the Keep in the first high "
               "summer (II.3); one name for two, with a dual verb",
    'wendhessa': "Wendhessa: the pair-name of the archivists of Eldhythe (Wendel and Tessa, cradle-names of the notes only), whose "
                 "seal is on Brenn's bundle (the foreword, IV.3, V.1); one name for two, with a dual verb",
    'ebba': "Ebba (a cradle-name; names are names): old Ebba of Fenholm, Marl's grandmother, who first said the hearth's answer",
    'enno': "Enno (a cradle-name; names are names): the first post of Enrella",
    'della': "Della (a cradle-name; names are names): the second post of Enrella",
    'ormund': "Ormund (a cradle-name; names are names): the first post of Orvenna, the wall-masters",
    'penna': "Penna (a cradle-name; names are names): the second post of Orvenna, the wall-masters",
    'yory': "Yory (a cradle-name; names are names): the Book's Jory, of Eldhythe, who whistled on the east wall (I.3, I.5, IV.5, "
            "V.1, V.5); the tongue has no j, and its one /j/ is the worn g written y",
    'wik': "Wik (a cradle-name; names are names): the Book's Wick, the youngest and swiftest of the runners (I.3, IV.3, V.5)",
    'merrik': "Merrik (a cradle-name; names are names): the Book's Merrick, eldest of the old ship-masters, Daveth's son (I.3, IV.5, "
              "the Epilogue)",
    'hossvell': "a whistle, a tune whistled, a song with no words ('breath-song'); (v.) whistle; VN hossvellyl, whistling; "
                "hossvell X dem susk, whistle X up (a wind); re hossvellym dem et helvhoss, I whistled for the wind",
    'sirr dem neld': "a far-glass, a spyglass ('a glass to far off'); pl. sirreth dem neld",
    'nind strom': "the thumb ('the great finger')",
    'drunndholm': "an anvil ('hammer-stone', the stone the smith strikes on); pl. drunndholmath",
    'keth et tolm, seren': "Hold the stone, Seren: Seren's opening of a telling of her own, her word to herself (the canon Keth et "
                           "tolm, Halyna's to the child Seren, with her name called)",
    'flennath et mymmyl': "Book Six: the Book of the Homecomings ('the Book of the Homecoming', the generic singular of every "
                          "Book's name); in v3 it replaces O0624 Flennath et Mesk Lurrel as Book Six's name",
    'nath dunn et wadh tul': "The sea hath not finished ('the sea does not finish yet'): Corlen's saying before every holding, "
                             "after Tovv (Tovva, to many), 'Wait': Tovv. Nath dunn et wadh tul. (V.5; III.1, the Epilogue); in a "
                             "past telling eth nath re dhunn et wadh tul, 'and the sea had not finished' (III.2)",
    'tolm et haskardath': "the runners' stone: the stone a haven's runners swear their oath on, the hand flat upon it ('the stone of "
                          "the runners'; IV.3: en narl ryss um dholm et haskardath); with an indefinite possessor tolm haskardath, "
                          "'a runners' stone' (I.3: Re yal tolm haskardath lo et cummath, cumm eth cumm, every haven had one)",
    'garl ul narl': "hand in hand ('hand in hand': the second softened by ul, N): of Enno and Della (I.2, II.3, V.1, V.5, V.7), "
                    "and of the knots of Tarnel's net (Piskur, el bysketeth hosel o, garl ul narl, II.3, VI.3)",
    'lo reskow': "at the seat of; for, in the stead of (of one who speaks for the fallen at his seat by the fire): lo reskow "
                 "Horlen 'for Corlen' ('at Corlen's seat', VI.1); eth lo reskow et ommatath, 'and for the fallen' (the Contents)",
    'galat sa re veskym, lymmym o. nath lymmym galat ullen.': "What I saw, I carry. I carry nothing else: the runners' oath, sworn "
        "with the hand flat on the runners' stone (I.3; sworn again in IV.3); as an oath it closes with Ston.",
}
# where units differed in a dry cut or a formation of the same form: the one kept
CANON_CUT = {
    'orvenna': ('', '=o.r.v.e.n.n.a'), 'enrella': ('', '=e.n.r.e.l.l.a'), 'wendhessa': ('', '=w.e.n.dh.e.s.s.a'),
    'ebba': ('', 'e.b.b.a'), 'enno': ('', 'e.n.n.o'), 'della': ('', 'd.e.l.l.a'), 'yory': ('', 'y.o.r.y'), 'wik': ('', 'w.i.k'),
    'merrik': ('', 'm.e.r.r.i.k'), 'ormund': ('', 'o.r.m.u.n.d'), 'penna': ('', 'p.e.n.n.a'),
    'hossvell': ('MOLT+zig (106) · TRENN+zig (46)', '@hoss@vell'),
    'drunndholm': ('GARL+wedge (218) · TOLM (1)', '@drunn@tolm'),
    'tolm et haskardath': ('TOLM (1) · TRENN+wedge (42) + A r d A th', '@tolm @hask+A.r.d+A.th'),
}
FORMATION = {'orvenna': 'ormund+penna+-a (pair-name)', 'enrella': 'enno+della+-a (pair-name)',
             'wendhessa': 'wendel+tessa+-a (pair-name)', 'ebba': 'name', 'enno': 'name', 'della': 'name', 'yory': 'name',
             'wik': 'name', 'merrik': 'name', 'ormund': 'name', 'penna': 'name', 'hossvell': 'hoss+vell', 'drunndholm': 'drunn+tolm',
             'tobe': 'name', 'ruan': 'name', 'tarnard': 'name'}
CANON_FORM = {'galat sa re veskym, lymmym o. nath lymmym galat ullen.': 'Galat sa re veskym, lymmym o. Nath lymmym galat ullen.'}
# root notation as the lexicon writes it
ROOT_FIX = {'*xoss-': '*hoss-', '*wel-': '*fell-', '*stan-': '*ston-', '*tunn-': '*tann-', '*ulan': '*ul-', '*umo': '*um-',
            '*or-': '*orr-', '*dos-': '*doss-', '*wryt-': '*wrut-', '*keθ-': '*keθ-', '*bysk-': '*buʔsk-', '*es-': '*es',
            '*maver-': '*mafer-', '*prenθ-': '*preinth-', '*resk-': '*rask-', '*sa-': '*sa', '*sast-': '*saʔst-',
            '*soŋm-': '*soŋ-', '*xem-': '*hemm-', '*ebb-ā': ''}


def main():
    base = read(BASE)
    by_key = collections.defaultdict(list)
    for r in base:
        by_key[key(r['orrowen'])].append(r)
    last = max(int(r['id'][1:]) for r in base)
    base_roots = set()
    for r in base:
        for x in re.split(r',\s*', r['root']):
            if x.strip():
                base_roots.add(x.strip())

    adds = []
    for p in sorted(glob.glob(os.path.join(W12, 'additions', '*.tsv'))):
        for r in read(p):
            r['_unit'] = os.path.basename(p)[:-4]
            adds.append(r)

    decisions = []
    groups = collections.OrderedDict()
    for r in adds:
        uid = (r['_unit'], r['id'])
        if uid in REPLACED:
            d = REPLACED[uid]
            decisions.append(dict(kind='one sense, two forms', dropped=r['orrowen'], unit=r['_unit'], row=r['id'],
                                  chosen=d['chosen'], why=d['why'], text_changed=d['text']))
            # its lemmas go to the chosen form's group
            groups.setdefault(key(d['chosen']), []).append(dict(r, _lemmas_only=True))
            continue
        if uid in RENAME:
            r = dict(r, **RENAME[uid])
            decisions.append(dict(kind='renamed by a decision', unit=r['_unit'], row=r['id'], form=r['orrowen']))
        if uid in INTO:
            decisions.append(dict(kind='folded into one saying', dropped=r['orrowen'], unit=r['_unit'], row=r['id'],
                                  chosen=INTO[uid]))
            groups.setdefault(INTO[uid], []).append(dict(r, _lemmas_only=True))
            continue
        groups.setdefault(key(r['orrowen']), []).append(r)

    new_rows = []
    for k, rs in groups.items():
        full = [r for r in rs if not r.get('_lemmas_only')]
        units = [r['_unit'] for r in rs]
        if k in by_key:  # a new sense of an existing form (the row of that very form, where 'X' and 'et X' both exist)
            exact = [x for x in by_key[k] if x['orrowen'].strip().lower() == k]
            b = (exact or by_key[k])[0]
            note = SENSE_NOTE.get(k)
            if note is None and k == 'ul reskow':
                continue
            assert note, ('no sense note for', k)
            if note not in b['meanings']:
                b['meanings'] = b['meanings'] + '; ' + note
            b['book_lemmas'] = lemmas_union(b['book_lemmas'], *[r['book_lemmas'] for r in rs])
            b['derivation'] = b['derivation'] + " [wf12: the sense '%s' added by unit%s %s]" % (
                note.split(':')[0].split(' (')[0], 's' if len(set(units)) > 1 else '', ', '.join(sorted(set(units))))
            decisions.append(dict(kind='new sense of a base form', form=b['orrowen'], base=b['id'], units=sorted(set(units)),
                                  rows=[r['id'] for r in rs], sense=note))
            continue
        assert full, ('group with no full row', k)
        r0 = dict(full[0])
        form = CANON_FORM.get(k, r0['orrowen'])
        if form.lower().startswith('et ') and ' ' in form[3:]:
            pass
        r0['orrowen'] = form
        single = ' ' not in form
        if k in FORMATION:
            r0['formation'] = FORMATION[k]
        elif not single:
            r0['formation'] = 'phrase'
        r0['class'] = oa.word_class(form) if single else phrase_class(form)
        if k in MERGED_MEANING:
            r0['meanings'] = MERGED_MEANING[k]
        if k in CANON_CUT:
            lg, dc = CANON_CUT[k]
            if lg:
                r0['logogram'] = lg
            r0['dry_cut'] = dc
        if k in ('yory', 'wik', 'merrik', 'ebba', 'enno', 'della', 'ormund', 'penna'):
            r0['pos'] = 'name'
        r0['book_lemmas'] = lemmas_union(*[r['book_lemmas'] for r in rs])
        der = strip_prov(r0['derivation'])
        prov = 'wf12 unit%s %s' % ('s' if len(set(units)) > 1 else '', ', '.join(sorted(set(units), key=units.index)))
        r0['derivation'] = der + ' [%s]' % prov
        r0['source'] = 'tier3'
        roots = []
        for r in full:
            for x in re.split(r',\s*', r['root']):
                x = ROOT_FIX.get(x.strip(), x.strip())
                if x and x not in roots:
                    roots.append(x)
        r0['root'] = '' if r0['pos'] == 'name' and single else ', '.join(roots)   # a name carries no root
        last += 1
        r0['id'] = 'O%04d' % last
        r0['_units'] = units
        r0['_rows'] = [r['id'] for r in rs]
        new_rows.append(r0)
        if len(full) > 1:
            diffs = sorted(set((r['class'], r['formation'], r['orrowen'], r['dry_cut']) for r in full))
            decisions.append(dict(kind='reached independently', form=form, id=r0['id'], units=[r['_unit'] for r in full],
                                  rows=[r['id'] for r in full], variants=[list(d) for d in diffs]))

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('\t'.join(COLS) + '\n')
        for r in base + new_rows:
            f.write('\t'.join(r[c].replace('\t', ' ').replace('\n', ' ') for c in COLS) + '\n')
    json.dump(dict(base=len(base), new=len(new_rows), additions=len(adds), decisions=decisions,
                   new_rows=[dict(id=r['id'], form=r['orrowen'], units=r['_units'], rows=r['_rows']) for r in new_rows]),
              open(os.path.join(HERE, 'lex_decisions.json'), 'w'), indent=1, ensure_ascii=False)
    print('base %d + new %d = %d rows; %d addition rows read; %d decisions' % (
        len(base), len(new_rows), len(base) + len(new_rows), len(adds), len(decisions)))
    bad_roots = sorted(set(x for r in new_rows for x in re.split(r',\s*', r['root']) if x and x not in base_roots))
    print('roots not among the base roots:', bad_roots)


if __name__ == '__main__':
    main()
