# -*- coding: utf-8 -*-
"""One-off edits to p1.html (Orrowen v2 and the course-hand). Scratch only."""
import os
import re
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, 'p1.html')
s = open(p, encoding='utf-8').read()


def R(a, b):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b, 1)


R('It is also built to be the opposite of the thunder-tongue in every way a listener would notice.</p>',
  'It is also built to be the opposite of the thunder-tongue in every way a listener would notice, and yet it descends from the same First Tongue (<a href="#first-tongue">§2</a>): every word in it is derived by the sound laws, with no mismatches. <strong>Version 2</strong> keeps the whole grammar of v0.1 and adds what Jack’s notes asked for: a stone grammar for the economical chisel register (<a href="#dry-cut">§5</a>), a running ink hand for the whole tongue (<a href="#leaf-hand">§6</a>), the Hal placed as the most economical hand of all (<a href="#o-history">§3.4</a>), and Seren’s name given its meaning (<a href="#o-seren">§3.6</a>). The script, <span class="orr">Garl Dhrenn</span>, is written three ways, from the most economical to the fullest:</p>\n'
  '{{tab s_hands}}\n'
  '<p><strong>A vow is always cut whole</strong>, in letters, with every word: “a sign holds what is meant; a vow must hold what was said.” That is why the tale-stone’s Stonwryt can be read word for word.</p>')

R('<p>The names were chosen so that the words for writing are the words for masonry. A scribe of the guild <em>lays</em> a line (<span class="orr">cadh trenn</span>) as a mason lays a course, and a letter is a stone.</p>',
  '<p>The names were chosen so that the words for writing are the words for masonry. A scribe of the guild <em>lays</em> a line (<span class="orr">cadh trenn</span>) as a mason lays a course, and a letter is a stone. A Stonewright cutting a line <em>dry</em> lays it as a dry-stone waller lays a wall: no mortar, the stones chosen to fit by their shapes alone, and the small words, the <strong>mortar words</strong>, left for the reader to lay back in.</p>')

R('<p>Prepositions take the person endings directly; there is no “to me” or “on him”.',
  '<p><strong>When the mutation cannot show, nothing marks the possessive.</strong> Before a word the softening leaves unchanged (<em>f, v, w, th, dh, s, h, l, r, n</em>, a vowel), <span class="orr">o saed</span> after a verb reads “he, half”, not “its half”, and <span class="orr">o hosen</span> reads “he … like”, not “his equal”. Say the possessor as a noun (<span class="orr">saed et covv</span>, “the half of the cloak”) or recast (<span class="orr">uld hosen et Crenn</span>, “a man like the Captain”). The same holds for <em>en, ol, va</em> before a letter the bedding leaves unchanged. <span class="kv">back-translation</span></p>\n<p>Prepositions take the person endings directly; there is no “to me” or “on him”.')
R('{{tab s_prep}}',
  '{{tab s_prep}}\n<p><strong><span class="orr">Hy</span> is also “than”</strong> (“greater from X”): <span class="orr">hos strom hyo</span>, “one greater than he”. After a verb of going the “from” reading wins (<span class="orr">orr hy</span>, “leave”), so a comparison is not set after <em>orr</em>. The most is <span class="orr">sost</span>, “self, very”: <span class="orr">et strom sost</span>, the greatest. An adverb is the bare quality after the verb. <span class="kv">back-translation</span></p>')
R('<li><strong>Questions:</strong> <span class="orr">ho</span> + S.',
  '<li><strong>“Only” of a clause</strong> is <span class="orr">nath … veth</span>, “not … but”: <span class="orr">sa nath re yorrar veth amm ew venn et dask</span>, “who fought only when the cause was just”. <span class="orr">Hosel</span> “only, alone” set after a verb reads “alone”. <strong><span class="orr">Nath … tul</span> is “not yet”</strong> (Seren’s own line), never “no longer”; the tongue has no “no longer”, and says it another way (<span class="orr">re vammant so hrenneth</span>, “they had lost their captains”). The negative past is <span class="orr">nath re</span> + S (<span class="orr">nath re yal</span>, “was not”). <span class="kv">back-translation</span></li>\n<li><strong>Questions:</strong> <span class="orr">ho</span> + S.')
R('Liturgy keeps the Hal form <span class="orr">Stonos</span>.</li>',
  'Liturgy keeps the Hal form <span class="orr">Stonos</span>. <strong>A vow is cut whole</strong>, in letters, even in stone (<a href="#dry-rules">§5.2</a>).</li>')

# ---- history
R('<h3 id="o-history">3.4 · History: from the Hal to the living tongue</h3>\n{{tab s_stages}}',
  '<h3 id="o-history">3.4 · History: from the first marks to the leaf-hand</h3>\n{{tab s_stages}}')
R('A player who has earned the old hand can read the column downward and watch the tongue change (<a href="#ladder">§7.2</a>, <span class="ach">Read Down the Lintel</span>).</p>',
  'Names are always letters, so the column reads by letter, and a player who has earned the old hand can read it downward and watch the tongue change (<a href="#ladder">§12.2</a>, <span class="ach">Read Down the Lintel</span>).</p>\n'
  '<h4>The four hands on the economy scale</h4>\n'
  '<p>Writing on the Shore began with meanings and ended with sounds, and every step toward sound was also a step toward ink.</p>\n'
  '{{tab s_economy}}\n'
  '<p><strong>So the Hal is the most economical hand of all</strong> that can still be sounded. The first builders had just made the letters (the reform, <a href="#a-marks">§2.6</a>), but they cut with the old marks wherever a mark would do, spelled only names and the words no mark held, and left every ending and every small word to the reader, who spoke the Hal and could not mistake them. The living dry cut is a little fuller: the living tongue has lost the Hal’s endings and turned their loss into mutations and harmonic suffixes, so the endings that still carry meaning are laid on in letters. The leaf-hand writes everything. Two things keep this true to the First Tongue: <strong>a word-sign is a word, not a meaning</strong> (it is read as one Orrowen word, aloud, and when the word’s meaning drifted, the sign followed the word: the Cup is read <em>tum</em>, “remember”, though the mark meant “hold”), and <strong>the tale-stone’s Stonwryt is cut in full, in letters, word for word, because it is a vow</strong>. It is the one Hal text anyone can still sound.</p>')
R('<h4>The sound changes, in order</h4>\n<ol>',
  '<h4>The sound changes, in order</h4>\n<p>The exact laws, stage by stage from the First Tongue, are in <a href="#a-laws">§2.3</a>, and they derive every Orrowen word with no mismatches. In brief, from the Hal to the living tongue:</p>\n<ol>')
R('<h4>Where each trigger came from</h4>\n{{tab s_origin}}',
  '<h4>Where each trigger came from</h4>\n<p>Every trigger is explained by its old ending, which the First Tongue explains in turn: the particles were fixed before the word, and their final <em>-n</em> and final vowels froze into the mutations (<a href="#a-sound">§2.2</a>). Two rows are emended from v0.1: Hal <em>re</em> (not <em>rea</em>), and Hal <em>van</em> (not <em>vanan</em>).</p>\n{{tab s_origin}}')
R('Halyna read the slate leaves by lamplight because the Bonded keep the Hal as a liturgy; earning the old hand is learning what they already knew.</p>',
  'Halyna read the slate leaves by lamplight because the Bonded keep the Hal as a liturgy; earning the old hand is learning what they already knew.</p>\n'
  '<p><strong>And most of it is not in letters at all.</strong> Outside the one vow, the Hal is cut in word-signs, mirrored, with no endings and no small words. A Rivenman knows perhaps half of those signs from the living dry cut (the same heads and crowns, turned the other way and cut taller), but he cannot supply the Hal’s endings or its small words, because he does not speak the Hal. So the Bonded keep the slate leaves of the Rite as a liturgy, learned by heart with their Hal readings, and read the signs as reminders of words they already know.</p>')

# ---- names, and Seren
R('<h3 id="o-names2">3.5 · The Shoreland names, and the Book’s translations</h3>\n{{tab s_pnames}}',
  '<h3 id="o-names2">3.5 · The Shoreland names, and the Book’s translations</h3>\n{{tab s_pnames}}\n<p><strong>In every hand, a name is letters.</strong> The dry cut never writes a name with word-signs, even where a name is made of words (Halvard, Stannard): “a name is said, not meant”.</p>')
R('<h3 id="o-lexicon">3.6 · The lexicon ({{n lex_s}} entries)</h3>',
  '<h3 id="o-seren">3.6 · Seren: “a single sorrow that overcomes”</h3>\n'
  '<p>Jack’s note 6: <em>“Sometimes a name is just a name. Having a meaning isn’t always necessary. Seren should mean ‘a single sorrow that overcomes’.”</em> Her name is the First Tongue’s <strong><em>*Swe-reŋ-o-s</em></strong>.</p>\n'
  '{{tab a_seren_parts}}\n{{tab a_seren_der}}\n'
  '<ul>\n'
  '<li><strong>Stress</strong> is on the first syllable: SE-ren. Both vowels are slender, so her name takes slender suffixes.</li>\n'
  '<li><strong>In the course-hand.</strong> The living hand writes <strong>s e r e n</strong>, spelled as said, with no lintel: “one name is a mourning”, and her one name <em>is</em> a single sorrow. The Hal writes <strong>SEREŊOS</strong>, with the long ending and the shore-nasal <em>ŋ</em>, one of the three letters for sounds no one has said in twelve generations. <strong>The sorrow in her name is, in the old hand, a letter no one can sound.</strong></li>\n'
  '<li><strong>In the wood’s tongue</strong> the same First Tongue word would also come out <em>Seren</em> (spoken <span class="sei">Se’ren</span>). It is the one name in the Book that is the same in both tongues: fitting for the one who writes both halves of the Book.</li>\n'
  '<li><strong>The guild’s own reading.</strong> The Rivenmen hear <span class="orr">ser</span>, “go on, carry forward”, in her name. That is a folk etymology and a true thing about her (“she can go where we cannot, alone, and carry this Book on after us”, II.3), but it is not where the name comes from; <em>ser</em> stays a verb of its own. Welsh <em>seren</em> “star” remains a coincidence of sound only.</li>\n'
  '<li><strong>Names are names.</strong> The names given no meaning keep none (Corlen, Voss, Hale, Marl, Tamm, Aske, Harl, Ulden, Hesk, Lanner, Aldun, Bena, Idlan, Denna). The laws account for their sounds; the real-world senses (Estonian <em>tamm</em>, Old Norse <em>askr</em>, English <em>marl</em>, Scots <em>harl</em>) are never borrowed.</li>\n'
  '</ul>\n\n'
  '<h3 id="o-lexicon">3.7 · The canon lexicon ({{n lex_s}} entries)</h3>')
R('Columns: the living form; the Hal form where it is known (most nouns are the stem + <em>-os</em> broad or <em>-is</em> slender); the harmony class (B broad, S slender); the sense; notes. Nouns take the plural <em>-Ath</em> unless marked.</p>',
  'Columns: the living form; the Hal form where it is known (most nouns are the stem + <em>-os</em> broad or <em>-is</em> slender); the harmony class (B broad, S slender); the sense; notes; and, new in v2, <strong>how the dry cut writes it</strong>: its word-sign (HEAD+crown, with its number in the inventory, <a href="#dry-inventory">§5.6</a>), its sign with a complement, or letters. The First Tongue derives every entry (<a href="#a-derived">§2.4</a>). This is the canon; the whole tier-3 lexicon of {{n olex}} entries, which contains it, is in <a href="#t3-lexicon">§11.3</a>.</p>')
R('<div class="s warn"><div class="ct">Seven forms break the harmony rule <span class="kv jack">Jack</span></div>',
  '<div class="s warn"><div class="ct">Seven forms break the harmony rule <span class="kv jack">Jack</span></div>\n<p><strong>Still open from v0.1</strong>, with one new fact: the First Tongue shows that <em>flennath</em> and <em>tevath</em> are old <em>ā</em>-stems, so their broad endings are right; the tier-3 lexicon keeps the canon’s three old broad stems (<em>tresk, flenn, tev</em>) broad.</p>')

# ---- the course-hand
R('<p class="lead">An alphabet of straight chisel strokes that stand on a mortar line. It records sound, and it is cut in stone, so it has no curves. It is Ogham-like in spirit (strokes set on a line, made to be cut) and its own in every shape and rule: its letters stand on one side of the line only, and their shapes say how the sound is made.</p>',
  '<p class="lead">An alphabet of straight chisel strokes that stand on a mortar line. It records sound, and it is cut in stone, so it has no curves. It is Ogham-like in spirit (strokes set on a line, made to be cut) and its own in every shape and rule: its letters stand on one side of the line only, and their shapes say how the sound is made. <strong>The letters are unchanged in v2.</strong> The dry cut uses them for names, rare words and complements (<a href="#dry-cut">§5</a>); a vow is cut in them whole; and the leaf-hand is them, written (<a href="#leaf-hand">§6</a>). Every letter descends from a first mark by the first builders’ reform (<a href="#a-marks">§2.6</a>).</p>')
R('<h3 id="ch-marks">4.4 · Bites, word-stones, marks, lintels</h3>', '<h3 id="ch-marks">4.4 · Bites, stones, marks, lintels</h3>')
R('<p><strong>Word-stones.</strong> Each word has its own bed band', '<p><strong>Stones.</strong> (v0.1 called a word with its own bed a “word-stone”; v2 calls it simply a <em>stone</em>, to keep it apart from the dry cut’s word-signs.) Each word has its own bed band')
R('It takes the class of the <strong>nearest full vowel before it</strong> in the same word-stone.', 'It takes the class of the <strong>nearest full vowel before it</strong> in the same stone.')
R('<p>For each word-stone, read the letters left to right', '<p>For each stone, read the letters left to right')
R('The Hal texts and the charts were not part of that test.</p></div>',
  'The Hal texts and the charts were not part of that test.</p></div>\n<p><strong>Reading a dry-cut line</strong> adds one step before step 1: sort each stone’s signs. A sign 4.6 u tall on a footing is a word-sign (look it up by its head and its crown, <a href="#dry-inventory">§5.6</a>); a sign 2 u tall standing before a word-sign, with its one laid stone running left from the head of a pin, is the turned stone (not); everything else is a letter. Letters after a word-sign on its bed are its complement. Then lay the mortar back in (<a href="#dry-rules">§5.2</a>).</p>')
R('<h3 id="ch-forms">4.7 · Three ways to make the letters</h3>\n{{tab s_forms3}}', '<h3 id="ch-forms">4.7 · Four ways to make the letters and the signs</h3>\n{{tab s_forms4}}')
R('The Title is 43 letters and five marks; a whole leaf of Seren’s hand fits well inside a page. The leaf-hand’s flat nib is specified but not yet drawn.</p>',
  'The Title is 43 letters and five marks; a whole leaf of Seren’s hand fits well inside a page. The leaf-hand is no longer a flat-pen sketch: it is drawn, and built as a font (<a href="#leaf-hand">§6</a>).</p>')
R('He copied the Title’s nasal bite faithfully. So his only error of language is the extra word (<a href="#x-stone">§6.19</a>).</p>',
  'He copied the Title’s nasal bite faithfully. So his only error of language is the extra word (<a href="#x-stone">§10.19</a>). <strong>And a fifth tell, new in v2: he cut the mortar.</strong> Every mortar word of the Title’s first line is cut, <em>ul</em> and five times <em>ol</em>, and one more the Title never had. No Stonewright cuts a small word in stone, least of all <em>et</em>. He cut stone as the Captain wrote on cloth: in letters, every word, as it is said.</p>')
R('<p>The same letters, transformed. The top names on the lintel of the western stair, the slate leaves of the Rite, the mark on the black chest and the old capstone’s Stonwryt are all in this hand.</p>',
  '<p>The same letters, transformed, and the same word-signs. The top names on the lintel of the western stair, the slate leaves of the Rite, the mark on the black chest and the old capstone’s Stonwryt are all in this hand.</p>')
R('Its living form is in <a href="#x-proverb">§6.7</a>.</figcaption>\n</figure>',
  'This is the Hal’s <em>speech</em> spelled out in its letters, 29 signs; the Hal itself would cut it in seven (below). Its living form is in <a href="#x-proverb">§10.7</a>.</figcaption>\n</figure>\n'
  '<p><strong>The Hal’s word-signs.</strong> The Hal cuts the same heads and crowns as the dry cut (<a href="#dry-cut">§5</a>), under its own rules 1 to 5: mirrored in their cells, cut at 4/3 of their height (a word-sign stands 6.13 u, a letter 4), on the one continuous bed, with no footing (height alone tells a sign from a letter), no complements and no bites. Only names, the words no mark held, and a vow are cut in letters, and the letters carry their full Hal endings. So the proverb, which the Hal <em>speech</em> spells in 29 letters, the Hal <em>hand</em> cuts in seven signs:</p>\n'
  '<figure class="leaf stone">\n{{fig prov_hal}}\n<div style="margin-top:12px">{{fig prov_live}}</div>\n'
  '<figcaption>Above: the Hal’s cut of <span class="orr">GRESTOS UMO HOSOS GRESTOS UMO PANĀ</span>: right to left, mirrored, one bed, no wedge, the word-signs bare and only <em>PANĀ</em> spelled, with its long-stone. Seven signs. Below: the living dry cut of the same saying, nine signs, with its footings and head-joints, and <em>hos</em> “one” as the capped numeral <strong>h</strong>.</figcaption>\n</figure>')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
