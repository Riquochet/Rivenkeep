"""The whole Book (tier 3, done) for Rivenkeep_Tongues.html v0.3.0: sections built from wf8/merge_report.md
(read-only). Scratch only; never goes into Docs/."""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mdlib import load, tables_after, find, inline, post, fixall  # noqa: E402

WF8 = os.path.dirname(HERE)
R = load(WF8 + '/merge_report.md')
ORIG = 'Rivenkeep_Legends_Original.html'


def tbl(pat, n=0):
    return tables_after(R, find(R, pat))[n]


def cell(s):
    s = s.replace('`wf8/lexicon_orrowen_full.tsv`', 'the merged lexicon')
    s = re.sub(r'`wf8/[^`]*`', '', s)
    s = s.replace('grain_v2_full', 'the merged grain spec').replace('grain_v2 §', 'the grain spec §')
    s = fixall(s)
    s = s.replace('as the builder sets them', 'as the Book sets them')
    s = re.sub(r'\b(?:O-)?([SW]\d\d)-\d\d\b', r'\1', s)
    s = re.sub(r'\s*\((?:grain_v2|orrowen_v2|lexicon)[^)]*§[^)]*\)', '', s)
    s = re.sub(r'\s*§[\d.]+(?:/§[\d.]+)?', '', s)
    s = re.sub(r'\(\s*\)', '', s)
    assert 'wf8' not in s and 'wf7' not in s, s
    return post(inline(s))


def render(head, rows, cols=None, cls=None):
    if cols is not None:
        head = [head[c] for c in cols]
        rows = [[r[c] for c in cols] for r in rows]
    out = ['<div class="tw"><table%s>' % (' class="%s"' % cls if cls else '')]
    out.append('<tr>' + ''.join('<th>%s</th>' % cell(h) for h in head) + '</tr>')
    for r in rows:
        out.append('<tr>' + ''.join('<td>%s</td>' % cell(c) for c in r) + '</tr>')
    out.append('</table></div>')
    return '\n'.join(out)


# ---------------------------------------------------------------- the leaves, and where they are in the Original
TITLES = {
    'foreword': ('Of This Book', 'foreword'), 'Invocation': ('The Invocation', 'invocation'),
    'I.1': ('The Torn Cloak', 't-I-1'), 'I.2': ('The Cry of the Bonded', 't-I-2'),
    'I.3': ('The Captain’s Long Breath', 't-I-3'), 'I.4': ('The Rite of the Cornerstone', 't-I-4'),
    'I.5': ('The Naming of the Rivenmen', 't-I-5'), 'II.1': ('Of the Keep That Was Forgotten', 't-II-1'),
    'II.2': ('Of the Breath of the Wood', 't-II-2'), 'II.3': ('Of the Bonded and the Theoliths', 't-II-3'),
    'III.1': ('The Book of the Havens', 't-III-1'), 'III.2': ('The Thrones That Walk the Sea', 't-III-2'),
    'IV.1': ('Of the Felling of the Black Pillars', 't-IV-1'), 'IV.2': ('The Axe in the Grain', 't-IV-2'),
    'IV.3': ('The Warden’s Door', 't-IV-3'), 'IV.4': ('The Gift Held an Hour', 't-IV-4'),
    'IV.5': ('The Burning Boat', 't-IV-5'), 'IV.6': ('The Voyage of the Aelvaren', 't-IV-6'),
    'V.1': ('The First Glyph', 't-V-1'), 'V.2': ('The Night of the Naming', 't-V-2'),
    'V.3': ('The Wreck That Went Home', 't-V-3'), 'V.4': ('The Council Under the Thin Sky', 't-V-4'),
    'V.5': ('The Tides, as the Wall Counted Them', 't-V-5'), 'V.6': ('Of the Growing', 't-V-6'),
    'V.7': ('The Mirror in the Grain', 't-V-7'), 'VI.1': ('The Knowing of the Green Wood', 't-VI-1'),
    'Epilogue': ('The Stone out of the Grey', 't-epilogue'), 'Knowings': ('The Book of Knowings', 'knowings'),
}
UNITS = [('S01', ['foreword', 'Invocation', 'I.2']), ('S02', ['I.3', 'I.4']), ('S03', ['I.5', 'II.1']),
         ('S04', ['II.3', 'IV.3']), ('S05', ['III.1']), ('S06', ['IV.1', 'IV.5']), ('S07', ['V.1', 'V.2']),
         ('S08', ['V.5']), ('S09', ['V.7']), ('S10', ['VI.1', 'Epilogue']), ('S11', ['Knowings']),
         ('W01', ['II.2']), ('W02', ['III.2']), ('W03', ['IV.2']), ('W04', ['IV.6']), ('W05', ['V.3']),
         ('W06', ['V.4']), ('W07', ['V.6'])]


def leaf_link(k):
    t, a = TITLES[k]
    if k in ('foreword', 'Invocation', 'Knowings', 'Epilogue'):
        lab = {'foreword': 'the foreword', 'Invocation': 'the Invocation', 'Knowings': 'the Book of Knowings',
               'Epilogue': 'the Epilogue'}[k]
        return '<a href="%s#%s">%s</a>' % (ORIG, a, lab)
    return '<a href="%s#%s">%s</a> <em>%s</em>' % (ORIG, a, k, html.escape(t, quote=False))


def n(s):
    return int(s.replace(',', '').strip('*').strip() or 0)


def quad(s):
    return [int(x) for x in re.findall(r'\d+', s)]


# ---------------------------------------------------------------- the numbers, from the report's tables
VH, VROWS, _ = tbl(r'^## 4 ')
VAL = {r[0]: r for r in VROWS}
BH, BROWS, _ = tbl(r'^## 6 ')
BT = {}
for r in BROWS:
    u = r[0].strip('*').strip()
    if not re.match(r'^[SW]\d\d$', u):
        continue
    sc, b, a = n(r[2]), quad(r[3]), quad(r[4])
    t = BT.setdefault(u, [0, [0] * 4, [0] * 4, []])
    t[0] += sc
    t[1] = [x + y for x, y in zip(t[1], b)]
    t[2] = [x + y for x, y in zip(t[2], a)]
    t[3].append(r[1])
TOT = [0, [0] * 4, [0] * 4]
for u, t in BT.items():
    TOT[0] += t[0]
    TOT[1] = [x + y for x, y in zip(TOT[1], t[1])]
    TOT[2] = [x + y for x, y in zip(TOT[2], t[2])]
assert TOT == [633, [354, 221, 51, 7], [368, 259, 6, 0]], TOT
ORR_WORDS = sum(n(VAL[u][2]) for u, _ in UNITS)
GN_ROUNDS = sum(n(VAL[u][6]) for u, _ in UNITS)
GN_SRC = sum(n(VAL[u][7]) for u, _ in UNITS)
assert (ORR_WORDS, GN_ROUNDS, GN_SRC) == (19281, 79, 30), (ORR_WORDS, GN_ROUNDS, GN_SRC)
AGG = {}
for r in BROWS:
    if r[0].startswith('**') and not re.match(r'^\*\*[SW]\d\d', r[0]):
        AGG[r[0].strip('*').strip()] = (n(r[2]), quad(r[3]), quad(r[4]))


def fq(q):
    return ' · '.join(str(x) for x in q)


# ---------------------------------------------------------------- 11.4 the whole Book
def book_html():
    rows = []
    for u, leaves in UNITS:
        hand = 'Orrowen' if u.startswith('S') else 'the grain; Seren’s frame in Orrowen'
        if u in ('S07', 'S09', 'S10', 'S11'):
            hand = 'Orrowen; its carvings in the grain'
        t = BT[u]
        rows.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                    % (u, ' · '.join(leaf_link(k) for k in leaves), hand, '{:,}'.format(n(VAL[u][2])),
                       VAL[u][6] if n(VAL[u][6]) else '–', t[0], fq(t[2])))
    rows.append('<tr><td><strong>pilots</strong></td><td>%s · %s</td><td>Orrowen · the grain</td><td>1,187</td>'
                '<td>2 (IV.4)</td><td colspan="2">read back on their own (<a href="#t3-bt1">§11.8</a>, '
                '<a href="#t3-bt4">§11.10</a>)</td></tr>' % (leaf_link('I.1'), leaf_link('IV.4')))
    rows.append('<tr><td><strong>all</strong></td><td>28 pieces: the foreword, the Invocation, 24 tales, the Epilogue and the '
                'Book of Knowings</td><td></td><td><strong>{:,}</strong> + 1,187</td><td><strong>{}</strong> + 2</td>'
                '<td><strong>{}</strong></td><td><strong>{}</strong></td></tr>'.format(ORR_WORDS, GN_ROUNDS, TOT[0], fq(TOT[2])))
    table = ('<div class="tw"><table><tr><th>Unit</th><th>Leaves (each opens in the Original)</th><th>Written in</th>'
             '<th>Orrowen words</th><th>Grain rounds</th><th>Read back</th><th>After the fixes: exact · close · drift · wrong</th></tr>\n'
             + '\n'.join(rows) + '\n</table></div>')
    return '''<h3 id="t3-book">11.4 · The whole Book</h3>
<p class="lead" style="font-size:1rem">Tier 3 is done. <strong>Every leaf of the Book is in its own tongue.</strong> The stone leaves, the Rivenmen’s tellings, are written whole in Orrowen, in the leaf-hand, small words and all, as Seren writes the Book in ink; so are Seren’s headnotes, the foreword, the Invocation and the Epilogue. The wood leaves, the Mystwood’s knowings, are carved whole in the grain, one round to a leaf, with Seren’s frame (her title, her headnote and her closing line) in Orrowen. The whole of it, leaf by leaf and facing the Book’s English, is <a href="{orig}">The Legends, in Their Own Hands</a>.</p>
<p>It was made in <strong>eighteen units at once</strong>: S01–S11 the stone leaves, W01–W07 the wood leaves. Every unit built on the two pilots (<a href="#t3-i1">§11.7</a>, <a href="#t3-iv4">§11.9</a>) and reused their formulas word for word. Each unit put every word and sign it needed into its own additions, derived from the First Tongue’s roots by the lexicon’s own rules, and had its leaves read back blind. A merge then made the eighteen into one Book: one lexicon, one grain and one rendering of every line the Book repeats (<a href="#t3-merge">§11.6</a>).</p>
{table}
<ul>
<li><strong>Orrowen: {words} words</strong> in the units’ leaves, and 1,187 in the pilots. The analyzer read every word against the merged lexicon and found <strong>0 unknown and 0 ill-formed</strong>. A second pass over each unit’s own draft (19,157 words) also found 0. The analyzer’s own test still passes all 87 samples of the spec. The Last Carver’s line keeps its canon error, and the analyzer still reports it, as it must.</li>
<li><strong>The lexicon: 135 new entries</strong>, almost all set phrases: the Book’s names, epithets, titles and formulas. Only three are new single words, and all three are regular derivations. No new root and no new word-sign (<a href="#t3-findings">§11.2</a>).</li>
<li><strong>The grain: {gn} rounds</strong> in the units’ files, and 30 source files (84 rounds). The validator reports <strong>0 errors and 0 warnings</strong>, and the coverage corpus passes. <strong>No new sign.</strong> The merge adds 53 compounds, 75 decoder readings, ten rules and calls (A16b–A25) and 15 corrections to the concept register, which now has 557 rows and maps all 670 lemmas of the wood leaves.</li>
<li><strong>Jack’s standing rules hold throughout.</strong> <span class="orr">Seren</span> is “a single sorrow that overcomes”. <span class="orr">Tumar</span>, “we remember”, is the yes of every close. “The Mystlands” is kept: <span class="orr">Mystow</span> in III.1 and IV.5, and in the grain <code>EARTH[MIST]</code>, “earth inside the grey”. Names are names.</li>
</ul>
'''.format(orig=ORIG, table=table, words='{:,}'.format(ORR_WORDS), gn=GN_ROUNDS)


# ---------------------------------------------------------------- 11.5 the scores
def scores_html():
    rows = []
    for u, _ in UNITS:
        t = BT[u]
        parts = ' and '.join(dict.fromkeys(p.replace('Orrowen + grain', 'Orrowen and grain') for p in t[3]))
        rows.append('<tr><td><strong>%s</strong></td><td>%s</td><td>%d</td><td>%s</td><td>%s</td></tr>'
                    % (u, parts, t[0], fq(t[1]), fq(t[2])))
    for lab, key in (('Orrowen (Seren’s ink and the tellings)', 'Orrowen (Seren\'s ink and the tellings)'),
                     ('the grain (rings, rounds, plates)', 'grain (rings, rounds, plates)'),
                     ('units scored as one (S10, W06)', 'units scored as one (S10, W06)'),
                     ('all units', 'all units')):
        sc, b, a = AGG[key]
        rows.append('<tr><td colspan="2"><strong>%s</strong></td><td><strong>%d</strong></td><td><strong>%s</strong></td>'
                    '<td><strong>%s</strong></td></tr>' % (lab, sc, fq(b), fq(a)))
    table = ('<div class="tw"><table><tr><th>Unit</th><th>Read</th><th>Scored</th><th>Before: exact · close · drift · wrong</th>'
             '<th>After: exact · close · drift · wrong</th></tr>\n' + '\n'.join(rows) + '\n</table></div>')
    b, a = TOT[1], TOT[2]
    pb, pa = b[0] + b[1], a[0] + a[1]
    return '''<h3 id="t3-scores">11.5 · The whole Book read back blind</h3>
<p>Every unit’s native lines were read back into English <strong>blind</strong>, by the pilots’ method (<a href="#t3-bt1">§11.8</a>): the reader had the Orrowen or the Grain Notation, the specs, the lexicon and the tools, and no English. Each line was scored on the pilots’ scale: <strong>exact</strong>; <strong>close</strong>, where a nuance shifts; <strong>drift</strong>, where a proposition is lost or changed; <strong>wrong</strong>, where something is contradicted or invented. Each unit then fixed what the reading found and re-read the fixed lines by rule.</p>
<div class="s pillar"><div class="ct">The result: {tot} units scored. Before: {pb} exact or close ({pbp}%), {b2} drift, {b3} wrong. After: {pa} exact or close ({pap}%), {a2} drift, no wrong.</div>
<p>The six drifts left are not translation errors. Five are reader slips where the text stands: two in S04 and three in S10. The sixth is the Stone’s <code>DEEP+SQUARE</code> in the Epilogue, a collision in the grain spec, left open for Jack’s call <span class="kv jack">Jack</span>.</p></div>
{table}
<ul>
<li><strong>The stone and the wood fail differently, as the pilots found.</strong> Orrowen came back exact 303 times in 450 before any fix, and its 25 drifts and wrongs were mostly small words and homophones. The grain came back close far more often than exact (64 of 97): a round keeps the proposition and loses the English nuance. Its 24 drifts and wrongs were mostly spec gaps, readings a decoder could not get from the spec alone, with some translation errors; the units wrote the missing readings as decoder readings, and the merge gathered them (75).</li>
<li><strong>Not in the totals:</strong> the Book of Knowings’ 47 carvings (identical to their sources and clean, with their literal readings matching; checked, not scored); W06’s twelve leaf-hand lines (10 · 1 · 1 · 0 before, 12 · 0 · 0 · 0 after); and the pilots’ own tests (<a href="#t3-bt1">§11.8</a>, <a href="#t3-bt4">§11.10</a>).</li>
<li><strong>Still owed: a fresh blind reader for the lines the merge changed.</strong> Each change adopts a form another unit had already read back, mostly exactly, so the risk is small. The lines are the merge’s one-rendering fixes (<a href="#t3-merge">§11.6</a>) in S01, S02, S03, S04, S06, S09, S10, W02 and W06, and the rings it re-cut: W01 r10–r11, W04 r10 and W07 r8.</li>
</ul>
'''.format(tot=TOT[0], pb=pb, pbp=round(100 * pb / TOT[0]), b2=b[2], b3=b[3], pa=pa, pap=round(100 * pa / TOT[0]),
           a2=a[2], table=table)


# ---------------------------------------------------------------- 11.6 one voice
def merge_html():
    fh, frows, _ = tbl(r'^### 5\.1')
    eh, erows, _ = tbl(r'^### 5\.2')
    hh, hrows, _ = tbl(r'^### 5\.4')
    gh, grows, _ = tbl(r'^## 3 ')
    return '''<h3 id="t3-merge">11.6 · One Book, one voice: the merge</h3>
<p>Eighteen translators working at once will render one English line eighteen ways. The merge read the units against each other and made the Book say each thing once. It found the Book’s recurring phrases by their shared five-word runs across leaves, and checked them paragraph by paragraph. Where units differed, <strong>one form was kept</strong>: the pilots’ form if there was one, else the majority’s, else the better derivation. The others were changed, and each change is marked in its unit.</p>
<h4>The pilots’ formulas, identical everywhere</h4>
{ftab}
<h4>Recurring English, one rendering</h4>
{etab}
<p>Already one before the merge: <em>Kethen et tolm</em> (Halyna’s “We hold the stone”), the first builders, <em>re rytym ul ba luth</em> (“I have used two inks”), the chest carried up the mountain, the Tides’ names, the grey sails, the Standard-Bearer, <em>Lodhan et Kethow</em> (the Bonded of the Keep), and <em>Nath gemment et trenneth … re hethym pana</em> (the tales do not agree; I have kept both).</p>
<h4>Names</h4>
<p>Every capitalised word of every unit was parsed and grouped by the lexicon row it reads as. <strong>Each name has one form in every unit</strong>, mutation aside (<em>Rhyna / Hyna</em>, <em>Kethow / Gethow</em>, <em>Tavow / Dhavow / Davow</em>, <em>Mardh / Vardh</em>, <em>Tarnel / Dharnel</em>). The epithets agree: <em>Rhyna Yanna Ulvenn</em>, <em>Halvard Tolmvard</em>, <em>Kael Nydherd</em>, <em>Seren Pa Luth</em>, <em>Hale Haskard</em>, <em>Kesterd Voss</em>, <em>Brenn Reldvar</em>, <em>et Crenn</em> (the Captain, never named). The Thrones’ shore-names, <em>Lymmerd Yendeth, Meskdhrenn sa Lilv, Vorrol, Grem Sell, Lorr Helv, Lennet</em>, are the same in III.1, VI.1 and the Book of Knowings. The Mystaeri names are loans.</p>
<h4>Halyna’s two inks</h4>
<p>The Book alternates Halyna’s two inks on every body paragraph of a leaf they tell. The formula they lay, the hearth’s answer, the frames and the fully italic lines take no ink. The merge computed the Book’s own sequence and checked every unit’s Orrowen against it. Five units had put an ink on the laid formula, and not all the same one; it now carries none, as the Book sets it.</p>
{htab}
<h4>The grain, merged</h4>
<p>The merge adds to the grain spec <strong>53 compounds</strong> (modifier + head, each with its computed soft reading; none conflicts with another or with the spec), <strong>75 decoder readings</strong>, and ten rules and calls. Among them are <strong>A17</strong>: the mirror and the hollow together carry no order, so <code>!~X</code> is “a seeming not-X”; A18, the untold ring <span class="kv jack">Jack</span>; A24, the Last Tide’s root <span class="kv jack">Jack</span>; and A25, the v1 Stone sample in the Epilogue <span class="kv jack">Jack</span>. <strong>No new sign.</strong> Each re-cut ring was changed in its source, its canonical text and its unit together, and all three validate clean.</p>
{gtab}
'''.format(ftab=render(fh, frows), etab=render(eh, erows), htab=render(hh, hrows, cols=[0, 1, 2, 3, 5]),
           gtab=render(gh, grows))


# ---------------------------------------------------------------- 11.2: the lexicon at the merge
def lexmerge_html():
    lh, lrows, _ = tbl(r'^### 2\.1')
    return '''<h4 id="t3-lexmerge">At the merge: the lexicon of the whole Book</h4>
<p>The eighteen units wrote <strong>180 rows</strong> of additions. The merge read each one against the lexicon and against the other units’ rows, by form and by sense, and let the lexicon’s own rules decide. <strong>One form, one row</strong>: a new sense of an existing word goes into that word’s meanings, after its canon sense, never into a second row. A phrase takes the class of its last word. Of the 180 rows:</p>
<ul>
<li><strong>159 became 135 new entries</strong>, O2881–O3015. Of those 159 rows, 39 had been reached independently by two to seven units, and they agreed on their form; they collapsed into 15 entries. Halyna’s close in the dual, <span class="orr">Cadhan o hosen re yal cadhat lona</span>, “This we lay as it was laid for us”, was written by seven units in the same words.</li>
<li><strong>15 are new senses of 10 existing words.</strong> The siege day’s hours are among them: <span class="orr">et cadhol</span> the laying, <span class="orr">et caldol</span> the hauling, <span class="orr">et kethyl</span> the holding. So are the Fall, <span class="orr">Ommol</span>, and the shore’s names for two Thrones, <span class="orr">Vorrol</span> the Burning and <span class="orr">Lennet</span> the Silvered.</li>
<li><strong>2 are regular plurals</strong> the analyzer already parses (<span class="orr">Mymmyleth</span> the Homecomings, <span class="orr">drunnatath</span> drums).</li>
<li><strong>4 were withdrawn</strong> for a form that another unit, or the lexicon, already had.</li>
</ul>
{ltab}
<p><strong>Screened.</strong> Every new row, and every old row the merge touched (146 in all), parses word by word in context against the merged lexicon, with 0 problems; the whole lexicon parses entry by entry as before, and the analyzer’s test passes all 87 samples. No new word is on the Tolkien and franchise blacklist, the reserve screen’s rejected forms or the common-English list. None uses a banned letter (<em>z, x, q, j</em>) or ending (<em>-ion, -iel, -dor</em>). None equals an existing form or its softened or nasalised form, and none reads as <em>na-</em> + another word. <strong>No new root</strong>: every root a new row names is one the lexicon already used, so no root that only the wood kept is revived, and the kin words stay 38. The three new single words are regular derivations of existing roots: <span class="orr">seryl</span>, carrying on (<em>ser</em> + <em>-Ol</em>); <span class="orr">bithlernen</span>, southern (<em>bithlern</em> + <em>-en</em>); and <span class="orr">desirel</span>, latish (<em>desir</em> + <em>-el</em>).</p>
'''.format(ltab=render(lh, lrows, cols=[0, 1, 2, 3]))


# ---------------------------------------------------------------- 11.11: still open
def open_html():
    return '''<h4 id="t3-open">Still open, for Jack</h4>
<ol>
<li><strong>“What the one knows, the other knows”</strong> is now <span class="orr">keth</span> in all three leaves: the Bonded’s own verb, “hold; know the wood”. S09 had argued for <span class="orr">sesk</span>, “know a fact”, in V.7, where the bond shares a mind and no wood is touched. If that distinction is wanted, it belongs in all three places, so it is one word, chosen once <span class="kv jack">Jack</span>.</li>
<li><strong>“Part One” (III.1) and “Part I” (V.7)</strong> stay different. <span class="orr">Saed Hosast</span>, “the first half”, is for a catalogue laid in two. <span class="orr">Trenn Hosast</span>, “the first course”, is for V.7’s three parts, each laid on its own night: <em>saed</em> means “half”, and three parts cannot be halves. The English differs too. Say if one word should serve both <span class="kv jack">Jack</span>.</li>
<li><strong><code>!TURN+HOLD</code> and <code>!TURN+HEAR</code></strong> are legal ligatures that the validator reads part by part (“not turning aside, and holding”). A glossed compound could make the reading “a holding not turned”. This is left to the validator.</li>
<li><strong>The grain rules marked proposed or for Jack</strong> (A16b referents, A18 the untold ring, A24 the Last Tide’s root, A25 the Epilogue’s v1 sample) wait on a spec pass. Every unit reads right without them <span class="kv jack">Jack</span>.</li>
<li><strong>Owed from before:</strong> the Welsh, Irish and Tolkien dictionary pass on every reserve word the text uses (<a href="#o-owed">§13.8</a>), and the lexicon’s own findings (the three <em>-dor</em> reserve roots; <em>mosk</em>, <em>heth</em>, <em>cald</em>, <em>dath</em>: <a href="#t3-findings">§11.2</a>). The units stepped round them throughout, and the merge added nothing that meets them.</li>
<li><strong>For the builder:</strong> the merged lexicon, grain spec and concept register replace the shared ones as they stand, and the recipes of the 135 new rows go into the lexicon builder’s sources before any rebuild, or a rebuild loses them.</li>
</ol>
'''


if __name__ == '__main__':
    for f in (book_html, scores_html, merge_html, lexmerge_html, open_html):
        h = f()
        print(f.__name__, len(h))
    print(BT['S10'], BT['W06'], AGG)
    print(merge_html()[:3000])
