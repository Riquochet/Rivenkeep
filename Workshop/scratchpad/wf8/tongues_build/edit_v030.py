"""Rivenkeep_Tongues.html v0.2.0 -> v0.3.0 (scratch only; never goes into Docs/, never writes there).

Starts from the published v0.2.0 (a copy: published_v020.html) and makes only these changes:
  1. the lexicon (§11.2, §11.3, and the count in §3.7) reflects the merged lexicon, wf8/lexicon_orrowen_full.tsv;
     §11.3 gives the counts by field, a selection, and the 158 entries added in translation, whole (the whole
     lexicon would take the page past ~4 MB beside the grain's v3 drawings); the full TSV's home is named;
  2. the grain section shows the v3 page cut: the §9 hero becomes the v3 IV.6; new §9.18 with v2 beside v3,
     IV.4 whole in v3, the reading-scale crops, the decode check and the Renderer notes v3;
  3. the pilot section becomes the whole Book: new §11.4-11.6 (the units, the back-translation totals, the merge),
     the pilots kept after them as §11.7-11.10, the lessons as §11.11 with what is still open;
  4. the version (v0.3.0) and a version-history row (2026-09-28).
Every internal link's section number is recomputed, as build.py did.

    python3 edit_v030.py  ->  wf8/out/Rivenkeep_Tongues.html
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v030_lex as LX  # noqa: E402
import v030_book as BK  # noqa: E402
import v030_grain as GR  # noqa: E402

WF8 = os.path.dirname(HERE)
SRC = HERE + '/published_v020.html'
OUT = WF8 + '/out/Rivenkeep_Tongues.html'
DOCS = '/Users/riquochet/code/Rivenkeep/Docs'
assert not OUT.startswith(DOCS)

s = open(SRC, encoding='utf-8').read()
assert open(DOCS + '/Rivenkeep_Tongues.html', encoding='utf-8').read() == s, 'published v0.2.0 changed since the copy'


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:120])
    s = s.replace(old, new)


def smart(h):
    """Curly apostrophes and quotes in text (never inside tags or <code>)."""
    parts = re.split(r'(<code>.*?</code>|<[^>]+>)', h, flags=re.S)
    for i in range(0, len(parts), 2):
        t = parts[i]
        t = re.sub(r"(\w)'(\w)", r'\1’\2', t)
        t = re.sub(r"(\w)'(?=[\s.,;:)!?]|$)", r'\1’', t)
        t = re.sub(r'"([^"]+)"', r'“\1”', t)
        t = re.sub(r"(?<![\w’])'([^'\n]+?)'(?![\w])", r'‘\1’', t)
        parts[i] = t
    return ''.join(parts)


# ---------------------------------------------------------------- 0. version and CSS
rep('--doc-version:"v0.2.0"', '--doc-version:"v0.3.0"')
rep('.rounds.pair>div{flex:1 1 280px;max-width:calc(50% - 10px)}',
    '.rounds.pair>div{flex:1 1 280px;max-width:calc(50% - 10px)}' + GR.CSS.rstrip('\n'))

# ---------------------------------------------------------------- 2. the grain: the hero, and §9.18
a = s.index('<figure class="leaf wood g2hero" id="fig-iv6">')
i = s.index('<svg', a)
j = s.index('</svg>', i) + len('</svg>')
V2_HERO = s[i:j]
assert V2_HERO == open(WF8 + '/grain3/v2out/IV-6.svg', encoding='utf-8').read().strip()
s = s[:i] + GR.hero_v3() + s[j:]
rep('<figcaption><strong>IV.6, <em>The Voyage of the Aelvaren</em>, carved whole by the v2 rules</strong>: ',
    '<figcaption><strong>IV.6, <em>The Voyage of the Aelvaren</em>, carved whole by the v2 rules</strong>, and cut for the page by the v3 renderer (<a href="#g2-v3">§9.18</a>): ')
rep('Its files and three of its rings, read by rule, are in <a href="#g2-iv6">§9.12</a>.</figcaption>',
    'Its files and three of its rings, read by rule, are in <a href="#g2-iv6">§9.12</a>; the same round as v2 cut it is beside it in <a href="#g2-v3">§9.18</a>.</figcaption>')

a = s.index('<h3 id="g2-jack">')
b = s.index('</section>', a)
s = s[:b] + smart(GR.section_html(V2_HERO)) + '\n' + s[b:]

# ---------------------------------------------------------------- 1. the lexicon
rep('the whole tier-3 lexicon of 2,880 entries, which contains it, is in <a href="#t3-lexicon">§11.3</a>.</p>',
    'the whole tier-3 lexicon of 3,015 entries, which contains it, is summarised in <a href="#t3-lexicon">§11.3</a>.</p>')

# the section's lead
rep('This section gives the vocabulary that makes it possible, a lexicon of <strong>2,880 entries</strong> covering every word of the Book’s stone text, and two whole leaves done as pilots, one of each kind, each read back into English <strong>blind</strong> to test whether the tongue says what the Book says.',
    'This section gives the vocabulary that makes it possible, a lexicon now of <strong>3,015 entries</strong>; <strong>the whole Book, done</strong> (<a href="#t3-book">§11.4</a>), read back into English <strong>blind</strong> to test whether the tongues say what the Book says (<a href="#t3-scores">§11.5</a>), and made one voice by the merge (<a href="#t3-merge">§11.6</a>); and the two pilots, one leaf of each kind, that set the house style and the formulas every leaf reuses (<a href="#t3-i1">§11.7</a>, <a href="#t3-iv4">§11.9</a>).')

# §11.2
rep('<p><strong>2,880 entries</strong>, every one resting on',
    '<p><strong>{:,} entries</strong> (2,880 when the pilots were done; translating the whole Book added 135, <a href="#t3-lexmerge">below</a>), every one resting on'.format(LX.N))
rep('<li><strong>The canon survives whole.</strong>',
    '<li><strong>The whole Book is written in it.</strong> Every word of the translation, {:,} in the eighteen units and 1,187 in the pilots, parses against the merged lexicon, with 0 unknown and 0 ill-formed (<a href="#t3-book">§11.4</a>).</li>\n<li><strong>The canon survives whole.</strong>'.format(BK.ORR_WORDS))
assert LX.LOGO == 1892
rep('<li><strong>1,767 entries carry a dry-cut word-sign</strong>: 328 are the word-signs themselves, about 1,030 are a word-sign with its complement letters, 197 are compounds cut as two signs, and the rest are phrases whose stones have signs.',
    '<li><strong>{:,} entries carry a dry-cut word-sign</strong> (1,767 before the merge): 328 are the word-signs themselves, about 1,030 are a word-sign with its complement letters, 198 are compounds cut as two signs, and the rest are phrases whose stones have signs.'.format(LX.LOGO))
K = LX.KINDS
for name, old in (('suffixed', '1,548'), ('<em>na-</em>', '178'), ('compound', '219'), ('construct or set phrase', '225')):
    key = {'<em>na-</em>': 'na-'}.get(name, name)
    rep('<tr><td>%s</td><td>%s</td>' % (name, old), '<tr><td>%s</td><td>%s</td>' % (name, '{:,}'.format(K[key])))
rep('<tr><th>Kind</th><th>Entries</th><th>Rule</th></tr>', '<tr><th>Kind</th><th>Entries (%s)</th><th>Rule</th></tr>' % '{:,}'.format(LX.N))
# the derivational patterns: the three new single words and the phrases
rep('<td>207</td><td><em>galdol</em> building', '<td>208</td><td><em>galdol</em> building')
rep('<td>238</td><td><em>lestel</em> a hut', '<td>239</td><td><em>lestel</em> a hut')
rep('<td>178 (all na-)</td>', '<td>179 (all na-)</td>')
rep('<td>219 (and 41 canon)</td>', '<td>220 (and 41 canon)</td>')
rep('<td>head + softened possessor; particle + noun</td><td>225</td>', '<td>head + softened possessor; particle + noun</td><td>{:,}</td>'.format(K['construct or set phrase']))
D = LX.ADDED_DRY
assert D == {'numeral letters': 5, 'stones': 119, 'one sign': 20, 'turned stone': 2, 'letters': 10, 'not cut': 2}, D
a = s.index('<h4>The chisel register</h4>')
b = s.index('</table></div>', a) + len('</table></div>')
s = s[:b] + ('\n<p>Counted over the 2,857 entries the lexicon builder made. The 158 added in translation (the pilots’ 23 and the '
             'merge’s 135) are cut by the same rules: {stones} by their stones, the mortar words left out and a signless word in '
             'letters; {one} by a single sign; {letters} in letters (names, and words with no sign); {nums} in numeral letters '
             '(<em>hos</em>, <em>pa</em>); {turned} by the turned stone alone (<span class="orr">nath re</span>, '
             '<span class="orr">ho nath</span>); and {nc} not at all, because a stone does not ask.</p>'
             .format(stones=D['stones'], one=D['one sign'], letters=D['letters'], nums=D['numeral letters'],
                     turned=D['turned stone'], nc=D['not cut'])) + s[b:]
rep('<h4>Findings for Jack</h4>', smart(BK.lexmerge_html()) + '<h4>Findings for Jack</h4>')
rep('<li><strong>The size.</strong> The brief asked for about 3,000; the lexicon has 2,880. It could reach 3,000 by deriving every suffix onto every root, but the extra words would be ones a speaker would not use (<em>a little dusk</em>, <em>a place of noons</em>).</li>',
    '<li><strong>The size.</strong> The brief asked for about 3,000. The lexicon had 2,880 when the pilots were done, and the whole Book’s translation took it to {:,} with words the Book itself needed. It did not get there by deriving every suffix onto every root, which would make words a speaker would not use (<em>a little dusk</em>, <em>a place of noons</em>).</li>'.format(LX.N))

# §11.3, replaced
a = s.index('<h3 id="t3-lexicon">')
b = s.index('<h3 id="t3-i1">')
C = LX.SRC
new113 = '''<h3 id="t3-lexicon">11.3 · The lexicon: {n} entries by field, and a selection</h3>
<p>Grouped by the field of the First Tongue root each entry rests on: a compound goes with its head, and names, places, the Book’s terms and the Mystaeri loans go together at the end. Canon {canon} · reserve {reserve} · made for the Book {t3} · made by rule {sys}. <strong>The whole lexicon</strong>, {n} rows in 14 tab-separated columns (an id, the form, its Hal, part of speech, class, senses, canon gloss, derivation, root, formation, word-sign, dry cut, source and the Book’s English lemmas it renders), lives beside this doc at <a href="Research/Rivenkeep_Orrowen_Lexicon.tsv"><code>Docs/Research/Rivenkeep_Orrowen_Lexicon.tsv</code></a>. Printed whole here it would take this page past about 4 MB, beside the grain’s drawings, so each field below is <strong>a selection</strong>: about one entry in twelve, and at least twelve a field, spread evenly through the alphabet and across the four sources, with words the Book uses chosen first among the made ones. <strong>Every entry added in translation</strong>, the pilots’ 23 and the merge’s 135, is given whole at the end.</p>
{ftab}
<p>Columns: the living form; its <strong>Hal</strong>, where the Hal is known; part of speech and harmony class; the senses, canon first; <strong>from</strong>, how it comes from the First Tongue or from other words (an entry added in translation names the units that made it, <a href="#t3-book">§11.4</a>); <strong>dry cut</strong>, its word-sign with its number, and any complement letters, or <em>letters</em>, or <em>left out</em> (a mortar word); and its source: <strong>C</strong> canon (<span class="cnkey">highlighted</span>), <strong>R</strong> a reserve root, <strong>T</strong> made for a word of the Book, <strong>·</strong> made by the systematic derivations.</p>
{sel}
{added}
'''.format(n='{:,}'.format(LX.N), canon=C['canon'], reserve=C['reserve'], t3=C['tier3'], sys='{:,}'.format(C['tier3-sys']),
           ftab=LX.field_table(), sel=LX.selection_html(), added=LX.added_html())
s = s[:a] + new113 + '\n' + smart(BK.book_html()) + '\n' + smart(BK.scores_html()) + '\n' + smart(BK.merge_html()) + '\n' + s[b:]

# ---------------------------------------------------------------- 3. the pilots, renumbered; the lessons and what is open
rep('<h3 id="t3-i1">11.4 · ', '<h3 id="t3-i1">11.7 · ')
rep('<h3 id="t3-bt1">11.5 · ', '<h3 id="t3-bt1">11.8 · ')
rep('<h3 id="t3-iv4">11.6 · ', '<h3 id="t3-iv4">11.9 · ')
rep('<h3 id="t3-bt4">11.7 · ', '<h3 id="t3-bt4">11.10 · ')
rep('<h3 id="t3-lessons">11.8 · What the pilots teach the next translators</h3>',
    '<h3 id="t3-lessons">11.11 · What the pilots and the whole Book teach, and what is still open</h3>')
rep('<p>The first stone leaf of tier 3: I.1 whole, as Seren writes it in her ink.',
    '<p>The first stone leaf of tier 3, and the first of the two pilots on which the eighteen units built: I.1 whole, as Seren writes it in her ink.')
a = s.index('<h3 id="t3-lessons">')
b = s.index('</section>', a)
s = s[:b] + smart(BK.open_html()) + s[b:]
# the I.1 pilot's leaf-hand, as the whole Book (the Original) writes it: v0.2.0 printed the pilot writer's tokens, which
# the back-translations then fixed (merge_report §5.2 #16; wf8/orig/ink.py): treskat, an old broad stem, keeps its full
# vowel (a harmonic A on the slender tresk would read tresket, as §11.2 and the pilot's own note say), and yalom and
# yalatath take the harmonic letters of their endings like every other ending in the leaf (nydhOm, kadhOm, galAt).
rep('<span class="gf" lang="x-orrowen">kovv treskAt</span>', '<span class="gf" lang="x-orrowen">kovv treskat</span>')
rep('ston. # re g̬alom um et ganna orl ull. el nydhArd g̬alatAth en,', 'ston. # re g̬alOm um et ganna orl ull. el nydhArd g̬alAtAth en,')

# ---------------------------------------------------------------- 4. version history
rep('<tr><td><strong>v0.2.0</strong></td>',
    '<tr><td><strong>v0.3.0</strong></td><td>2026-09-28 · Tier 3 done (Jack: “I’d like tier 3 on how far to take the translation”): '
    '<strong>the whole Book in its own tongues</strong>. <strong>The whole Book</strong> (new <a href="#t3-book">§11.4</a>–<a href="#t3-merge">§11.6</a>): '
    'the stone leaves, Seren’s headnotes, the foreword, the Invocation and the Epilogue in Orrowen, in the leaf-hand; the wood leaves carved '
    'whole in the grain, with Seren’s frame in Orrowen; eighteen units on the two pilots, {w} words of Orrowen and {g} grain rounds, '
    '0 unknown and 0 errors; read back blind, {sc} units scored, {ok} exact or close after the fixes and none wrong; the merge that '
    'made them one voice (the formulas, the recurring English, the names, Halyna’s two inks, the grain’s conflicts); still open for Jack. '
    '<strong>The lexicon</strong> at {n} entries (135 new, all phrases but three regular derivations; no new root or word-sign; '
    'the merge’s conflicts and new senses), given by field as counts and a selection, with the 158 entries added in translation whole; '
    'the whole in <code>Docs/Research/Rivenkeep_Orrowen_Lexicon.tsv</code>. <strong>The grain’s page cut, v3</strong> (new <a href="#g2-v3">§9.18</a>): '
    'a whole round cut at a page weight, heavier runners in grooves, the wake, the knot-eyes, the ring-splits and the figure, all by '
    'the Law of the Rings, with the notation, marks, runners and crossings unchanged; IV.6 at the head of <a href="#grain2">§9</a> now in v3, '
    'beside its v2; IV.4 carved whole, printed for the first time; the crops at reading scale, the decode check and the Renderer notes v3. '
    'The pilots are now <a href="#t3-i1">§11.7</a>–<a href="#t3-lessons">§11.11</a>, and I.1’s leaf-hand is written as the '
    'Original writes it (<em>treskat</em> keeps its full vowel; <em>yalom</em> and <em>yalatath</em> take their endings’ '
    'harmonic letters).</td></tr>\n<tr><td><strong>v0.2.0</strong></td>'
    .format(w='{:,}'.format(BK.ORR_WORDS), g=BK.GN_ROUNDS, sc=BK.TOT[0], ok=BK.TOT[2][0] + BK.TOT[2][1], n='{:,}'.format(LX.N)))


# ---------------------------------------------------------------- section numbers on internal links (build.py's own)
def number_ids(b):
    heads = []
    for m in re.finditer(r'<h2[^>]*>\s*<span class="n">(\d+)</span>', b):
        heads.append((m.start(), 2, m.group(1)))
    for m in re.finditer(r'<h3[^>]*>\s*(\d+\.\d+) ·', b):
        heads.append((m.start(), 3, m.group(1)))
    for m in re.finditer(r'<h3[^>]*>(?!\s*\d+\.\d+ ·)', b):
        heads.append((m.start(), 3, None))
    heads.sort()
    nums = {}
    for m in re.finditer(r'<(\w+)[^>]*\bid="([^"]+)"', b):
        tag, i, p = m.group(1), m.group(2), m.start()
        if tag in ('section', 'article'):
            nxt = [h for h in heads if h[0] > p and h[1] == (2 if tag == 'section' else 3)]
            nums[i] = nxt[0][2] if nxt else None
            continue
        cur2 = cur3 = None
        for hp, lv, n in heads:
            if hp > p:
                break
            if lv == 2:
                cur2, cur3 = n, None
            else:
                cur3 = n
        nums[i] = cur3 or cur2
    return nums


def check_numbering(b):
    errs = []
    last2, last3 = 0, 0
    for m in re.finditer(r'<h2[^>]*>\s*<span class="n">(\d+)</span>|<h3[^>]*>\s*(\d+)\.(\d+) ·', b):
        if m.group(1):
            n = int(m.group(1))
            if n != last2 + 1:
                errs.append('h2 %d after %d' % (n, last2))
            last2, last3 = n, 0
        else:
            a_, c = int(m.group(2)), int(m.group(3))
            if a_ != last2 or c != last3 + 1:
                errs.append('h3 %d.%d (in %d, after .%d)' % (a_, c, last2, last3))
            last3 = c
    return errs


a = s.index('<body>')
body = s[a:]
errs = check_numbering(body)
assert not errs, errs
# only ids outside the drawings matter to the numbering; drop the SVGs while computing it (speed)
light = re.sub(r'<svg\b.*?</svg>', lambda m: '<svg>' + ''.join(re.findall(r'<\w+[^>]*\bid="(?:g2-|t3-|fig-)[^"]*"[^>]*>', m.group(0))) + '</svg>', body, flags=re.S)
nums = number_ids(light)
changed = []


def fix(m):
    i, text = m.group(1), m.group(2)
    n = nums.get(i)
    if n is None:
        return m.group(0)
    new = '§' + n
    if new != text:
        changed.append((i, text, new))
    return '<a href="#%s">%s</a>' % (i, new)


body = re.sub(r'<a href="#([^"]+)">(§[\d.]+)</a>', fix, body)
s = s[:a] + body
for c in changed:
    print('ref renumbered', c)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(s)
print('wrote', OUT, len(s.encode('utf-8')), 'bytes')
