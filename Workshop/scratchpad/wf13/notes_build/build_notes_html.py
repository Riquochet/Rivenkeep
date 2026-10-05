#!/usr/bin/env python3
"""build_notes_html.py - builds Rivenkeep_Legends_Notes.html, Notes v1.2.0, from wf11/notes_v3.md (wf13 scratch;
never in Docs/).

    python3 build_notes_html.py --doc-version "v1.2.0"
        -> wf13/out/Rivenkeep_Legends_Notes.html (+ notes_build/notes_v3_composed.md)

Changes from the wf12 builder (Notes v1.1.0, with section 1.15), for the Book's page v3.1.0 (2026-10-03):
  * a second section is spliced in after 1.15: 1.16 Plain Words for newcomers, and the word-by-word romanisation
    (v3.1.0) (notes_build/sec_1_16.md: Jack's notes of 2026-10-03 verbatim, the new Plain's rules and numbers, and the
    interlinear gloss of the Original's romanisation folds, how it was made and its counts); Jack's notes stand in a
    gold box like his notes of 2026-10-02;
  * pointers to it (EDITS): the contents, the front matter and its references note, 0, 1.10, 1.11, 5.8, 5.14 and
    7.2; and the Original recorded as on the story page, which it has been since v3.0.0, wherever these Notes still
    called it owed (1.1's K2, 1.11, 5.8, 7.2 by EDITS; 1.15's two sentences by POST_EDITS, after the splice, so
    sec_1_15.md stays as wf12 made it);
  * the version history gets the row Book v3.1.0 / Notes v1.2.0 (2026-10-03) and a NOTES v1.2.0 sources paragraph;
  * --doc-version sets the house sheet's version (default v1.2.0); the meta line reads Notes v1.2.0 for the Book
    v3.1.0, 2026-10-03.

House style: the head and <style> of Docs/Rivenkeep_Fight.html, copied verbatim, with --doc-version set to v1.2.0
and a short block of additions appended (tables that scroll on a phone, h4 sub-heads, ordered lists, block quotes,
the quiet tale-link, pills, the contents grid, Jack's quoted notes).  No script.  Links into the story page use its
tale anchors (t-I-1 ... t-VI-3, t-epilogue, t-last-note, foreword, invocation, knowings, book-1 ... book-6), the
anchors the v3 story builder keeps (wf12/orig/panes.json is keyed on the same set).

Changes from the wf10 builder (Notes v1.0.0 for the Book v2.0.0):
  * the source is wf11/notes_v3.md, with nine sections (0 to 8): a new section 1 (What v3 changed), the old 1 as 2,
    and every later section one up.  Section ids stay by name; sub-section ids are by number (s5-3 is section 5.3);
  * one section is added, 1.15 The Original, translated from v3 (notes_build/sec_1_15.md, from the wf12 merge
    report), and five short pointers to it (EDITS).  The composed markdown is written beside this script, for the
    checker's word count;
  * Jack's notes of 2026-10-02 (K1 to K9) get boxes and ids like the notes of 2026-09-30 (J1 to J26); section 7.2's
    calls are boxes with ids call-1 to call-24; the deaths table rows are d1 to d12;
  * markdown links may be relative (the Research docs, by path from Docs/); block quotes render; a list item may
    carry indented paragraphs and quotes after a blank line (5.11);
  * the v1.3 pages Plain Words and the Original link to their archived copies in Docs/Archive/;
  * section references that name another document's sections (voice, craft, R6b, the outline, a file in code) are
    never linked as this document's.
"""
import argparse
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(HERE)                          # wf13
SCRATCH = os.path.dirname(W)
SRC = os.path.join(SCRATCH, 'wf11', 'notes_v3.md')
ADDED = [os.path.join(HERE, 'sec_1_15.md'), os.path.join(HERE, 'sec_1_16.md')]   # spliced in this order
COMPOSED = os.path.join(HERE, 'notes_v3_composed.md')
OUT = os.path.join(W, 'out', 'Rivenkeep_Legends_Notes.html')
HOUSE = '/Users/riquochet/code/Rivenkeep/Docs/Rivenkeep_Fight.html'
BOOK = 'Rivenkeep_Legends.html'
ORIGINAL_V1 = 'Archive/Rivenkeep_Legends_Original_v1.0.html'
MODERN_V12 = 'Archive/Rivenkeep_Legends_Modern_v1.2.html'
_ap = argparse.ArgumentParser()
_ap.add_argument('--doc-version', default='v1.2.0')
VERSION = _ap.parse_args().doc_version
BOOK_VERSION = 'v3.1.0'
DATE = '2026-10-03'

SEC_IDS = {'0': 'glance', '1': 'changed-v3', '2': 'changed-v2', '3': 'reckoning', '4': 'puzzle', '5': 'game',
           '6': 'names', '7': 'calls', '8': 'history'}
NAV = [('about', 'This Document'), ('glance', 'At a Glance'), ('changed-v3', 'What v3 Changed'),
       ('changed-v2', 'What v2 Changed'), ('reckoning', 'Reckoning &amp; Cast'), ('puzzle', 'Puzzle Pieces'),
       ('game', 'Into the Game'), ('names', 'The Names'), ('calls', 'Open Calls'), ('history', 'Version History')]

# The tales of the Book v3.0.0 and how many each Book holds (the same as v2.0's).
TALES = {'I': 5, 'II': 3, 'III': 2, 'IV': 6, 'V': 7, 'VI': 3}
BOOKNUM = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6}

# Section 8 for v1.2.0: the new row and its sources paragraph.
HISTORY_ROW = (
    "| **Book v3.1.0 · Notes v1.2.0** | 2026-10-03 | Jack's notes of 2026-10-03 applied (§1.16). The Book's English, "
    "v3.0.0, unchanged. Plain Words v3.1: every paragraph rewritten whole for a modern reader who knows nothing of the "
    "lore, by thirteen groups from one primer, each group read by a newcomer and checked for fidelity, then the whole "
    "read by a newcomer and edited; the lore explained as the tale meets it, never before the hearth knows it and "
    "never where the Book keeps it dark; a plain *when* line in place of each of the 29 datelines; a note for new "
    "readers before the foreword; 44,895 words against the Book's 31,567 (142%); the markup as v3.0's Plain, section "
    "by section. The Original's romanisation folds set word over word, each Orrowen word over its English: the "
    "analyzer's drafts, one shared table, twenty units glossed and verified, 1,288 lines and 26,532 words, 0 problems. "
    "Notes: §1.16 added, with pointers in the front matter, §0, §1.10, §1.11, §5.8, §5.14 and §7.2; the *Original* "
    "recorded as on the story page where these Notes still called it owed (§1.1, §1.11, §1.15, §5.8, §7.2) |")
NOTES_V120 = (
    "**NOTES v1.2.0 (2026-10-03).** Made for the Book v3.1.0 from Notes v1.1.0; from Jack's notes of 2026-10-03 and "
    "the orchestrator's reading of them (`wf13/jack_2026-10-03.md`); from the Plain's primer "
    "(`wf13/plain_primer.md`), its critiques (`wf13/critique/`) and its writers' and editor's notes "
    "(`wf13/plain_notes.md`); from the gloss's shared table (`wf13/gloss_table.md`), drafts (`wf13/gloss_in/`), "
    "units (`wf13/gloss/`) and checker (`wf13/check_gloss.py`); and from the story page's build "
    "(`wf13/book/build_story_html.py`, `wf13/orig/panes_build.log`).")

# The added sections 1.15 and 1.16 and their pointers.  Each 'old' must stand in the source exactly once.
EDITS = [
    ('   - 1.14 What left the Book in v3, for Jack\'s eye\n',
     '   - 1.14 What left the Book in v3, for Jack\'s eye\n   - 1.15 The Original, translated from v3\n'
     '   - 1.16 Plain Words for newcomers, and the word-by-word romanisation (v3.1.0)\n'),
    # the meta line, the references note and the front's lead (v1.2.0)
    ('*Notes v1.1.0 · for the Book v3.0.0 · 2026-10-02*', '*Notes v1.2.0 · for the Book v3.1.0 · 2026-10-03*'),
    ('"v3" is this Book, v3.0.0.',
     '"v3" is this Book, v3.0.0. "v3.1.0" is its page with Plain Words rewritten for newcomers and the '
     'romanisation glossed word by word (§1.16).'),
    ('so this document can be read on its own.*',
     'so this document can be read on its own. Notes v1.2.0 (2026-10-03) adds §1.16, for the Book\'s page v3.1.0: '
     'Plain Words rewritten for newcomers, and the romanisation glossed word by word.*'),
    # section 0
    ('reads at about grade 3, and keeps its own paragraphs (K4; §1.10).',
     'reads at about grade 3, and keeps its own paragraphs (K4; §1.10). In v3.1.0 every paragraph was rewritten '
     'again, whole, for a reader new to the lore (§1.16).'),
    ('The Original must come back in every section, set down anew from v3 (K2).',
     'The Original must come back in every section, set down anew from v3 (K2), and it has (§1.15); from v3.1.0 '
     'its romanisation is glossed word by word (§1.16).'),
    # 1.10 and 1.11
    ('### 1.10 Plain Words, a true retelling\n\n',
     '### 1.10 Plain Words, a true retelling\n\n*This is v3.0\'s Plain. Jack found it still too hard for a reader '
     'new to the lore (2026-10-03), and v3.1.0 rewrote every paragraph whole for that reader (§1.16).*\n\n'),
    ("That is the Tongues team's pass and is owed.",
     "That is the Tongues team's pass. It is made and merged (§1.15), and the tab built from it is on the story "
     "page (§1.16)."),
    ('Until it lands, every native drawing the Book carries (the Title',
     'Every native drawing the Book carries (the Title'),
    ('shows under *Original* at its place (§1.11, §5.8, §7.2 call 2).',
     'shows under *Original* at its place (§1.11, §5.8, §7.2 call 2). It has since landed, and the tab is on the '
     'story page (§1.15, §1.16).'),
    # 5.8's table, 5.14, and 7.2 call 2
    ("| **owed** (K2): to be set down from v3 by the Tongues team. Until then every native drawing the Book carries "
     "shows here at its place, and the leaf's prose is not faked. *Being set down anew in its own hands.* does not "
     "ship (§1.11) |",
     "| **translated, merged and on the story page** (K2; §1.15, §1.16): set down from v3 by the Tongues team; on "
     "the page every line of a *Romanisation* fold stands word over word, each word over its English (v3.1.0). "
     "*Being set down anew in its own hands.* does not ship (§1.11) |"),
    ('; no datelines | done (`wf11/plain_v3.md`, checked leaf by leaf, §1.10) |',
     '; no datelines. **v3.1:** every paragraph rewritten whole for a reader new to the lore, the lore explained as '
     'the tale meets it, a plain *when* line in place of each dateline, and a note for new readers before the '
     'foreword | done (`wf13/plain_v31.md`, §1.16; v3.0\'s was `wf11/plain_v3.md`, §1.10) |'),
    ('- **Plain Words** is `wf11/plain_v3.md`, the second tab inside the story page.',
     '- **Plain Words** is `wf13/plain_v31.md` (v3.1, §1.16; v3.0\'s was `wf11/plain_v3.md`), the second tab '
     'inside the story page.'),
    ('The Original is owed (§1.11).',
     'The Original is translated, merged and on the story page (§1.15, §1.16).'),
    # section 8: the new row (bold, as the current one is), the v1.1.0 row unbolded, and its 1.15 note (wf12)
    ('| **Book v3.0.0 · Notes v1.1.0** | 2026-10-02 |', HISTORY_ROW + '\n| Book v3.0.0 · Notes v1.1.0 | 2026-10-02 |'),
    ('sections renumbered (the table at the head of this document) |',
     'sections renumbered (the table at the head of this document); §1.15, added 2026-10-03, records the '
     "Original's translation from v3 and its merge |"),
    ('**NOTES v1.1.0 (2026-10-02).**', NOTES_V120 + '\n\n**NOTES v1.1.0 (2026-10-02).**'),
    ('(`count_v3.py`, `plain_check.py`, and R5\'s `style_metrics.py`).',
     '(`count_v3.py`, `plain_check.py`, and R5\'s `style_metrics.py`). §1.15 was added on 2026-10-03 from the '
     "merge report of the Original's translation (`wf12/merge_report.md`)."),
]
# Edits made after the splice, in the added sections themselves (sec_1_15.md stays as wf12 made it).
POST_EDITS = [
    ('The *Original* tab is not yet on the story page. It is built from the merged units next, and until then §5.8 '
     'holds.',
     'The *Original* tab was then built from the merged units, and it is on the story page (§1.16).'),
    (' And the *Original* tab is built from the merged units (§5.8).', ''),      # 1.15's Still to do: done
]
SECTION_ANCHOR = '\n---\n\n## 2 · WHAT V2 CHANGED'      # 1.15 and 1.16 go in before this

# Substrings that name sections of OTHER documents: never auto-linked here.
PROTECT = ['v1.3 §7 and the §9 batteries row', 'MAP §4.1', 'outline §12, call 1', 'R6b §0.1',
           '§0 l.93; §1 l.130; §5.2 l.516', '§7.9 whole', 'Notes v1.0.0 §4']
# A section mark after one of these names another document's section (the 8 characters before it are tested).
OTHER_DOC_SEC = re.compile(r'(doc |its |v1\.3 |v1\.0\.0 |MAP |outline |voice |craft |R6b |spec |\x00 )$')

ADMIRAL_IDS = {'12': 'command-time', '9': 'recognition', '9b': 's9b', '9c': 's9c', '9d': 's9d'}

EXTRA_CSS = r"""
/* — Legends Notes: additions to the house sheet — */
ol{margin:6px 0 12px 22px}
li>ul,li>ol{margin:6px 0 4px 18px}
li>blockquote,li>p{margin-top:8px}
h4{font-family:'Chakra Petch',sans-serif;font-size:.84rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin:22px 0 7px;color:var(--gold)}
h4 .hn{font-family:'Source Sans 3',sans-serif;font-size:.84rem;font-weight:400;letter-spacing:0;text-transform:none;color:var(--dim);margin-left:4px}
h3 .no{color:var(--dim);font-weight:400;margin-right:2px}
p.note{color:var(--dim);font-style:italic;font-size:.84rem}p.note em{font-style:normal;color:var(--dim)}
blockquote{margin:10px 0 14px;padding:2px 0 2px 16px;border-left:2px solid var(--border)}blockquote p{margin-bottom:6px}
.s>:last-child{margin-bottom:0}.s table{margin:10px 0 4px}
.s.law .ct{color:var(--success)}.s.pillar .ct{color:var(--accent)}
.s.jn{border-left-color:var(--gold)}.s.jn .ct{color:var(--gold);text-transform:none;letter-spacing:.3px;font-size:.86rem}
.s.jn p.kq{font-size:.88rem;border-left:2px solid rgba(255,213,79,.35);padding-left:10px;margin:2px 0 10px}
.s.call{border-left-color:var(--purple)}.s.call .ct{color:var(--purple)}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0}.tw table{margin:0}
a.tl{color:inherit;text-decoration:none;border-bottom:1px dotted rgba(79,195,247,.6)}a.tl:hover{color:var(--accent);border-bottom-color:var(--accent)}
a.xr{text-decoration:none;border-bottom:1px dotted rgba(79,195,247,.5)}
.pill.mv{color:var(--warn);border-color:rgba(255,167,38,.45)}.pill.nw{color:var(--success);border-color:rgba(102,187,106,.45)}
.toc{columns:2;column-gap:34px;margin:10px 0 4px}.tg{break-inside:avoid;margin-bottom:10px}
.toc div{font-size:.82rem;line-height:1.5}.toc .t2{font-family:'Chakra Petch',sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:1px;font-size:.74rem;margin-top:8px}
.toc .t2 .n{color:var(--dim);margin-right:8px}.toc a{text-decoration:none}.toc a:hover{text-decoration:underline}
.toc .t3{padding-left:22px;color:var(--dim)}.toc .t3 a{color:var(--text)}
[id]{scroll-margin-top:52px}
tr:target td{background:rgba(255,213,79,.06)}.s:target{box-shadow:0 0 0 1px rgba(255,213,79,.35)}
@media(max-width:768px){.toc{columns:1}.tw table.wide{min-width:680px}.tw table.t4{min-width:520px}}
"""


# ----------------------------------------------------------------------------------------------- inline

def smart_quotes(s):
    out = []
    for i, ch in enumerate(s):
        if ch == '"':
            j = i - 1
            while j >= 0 and s[j] in '*_':
                j -= 1
            prev = s[j] if j >= 0 else ' '
            out.append('“' if (prev.isspace() or prev in '([{—–/·') else '”')
        elif ch == "'":
            prev = s[i - 1] if i else ' '
            nxt = s[i + 1] if i + 1 < len(s) else ' '
            out.append('‘' if (prev.isspace() or prev in '([{“"—–/') and nxt.isalnum() else '’')
        else:
            out.append(ch)
    return ''.join(out)


def roman_ok(r, n):
    return r in TALES and 1 <= int(n) <= TALES[r]


LINK_RE = re.compile(
    r'(?P<adm>admiral doc,? (?:§(?P<admsec>\d+[a-d]?)|T-rule 9))'
    r"|(?P<tladder>Tongues doc[’']s unlock ladder)"
    r'|(?P<tcall>Tongues doc §2\.8 call-out)'
    r'|(?P<admbare>admiral doc)'
    r'|(?P<tongues>Tongues doc)'
    r'|(?P<fight>Fight doc)'
    r'|(?P<orig>The Legends, in Their Own Hands)'
    r'|(?P<plain>The Legends, in Plain Words)'
    r'|(?P<call>§7\.2,? call (?P<calln>\d+))'
    r'|(?P<sec>§(?P<s1>\d)(?!\d)(?:\.(?P<s2>\d+))?)'
    r'|(?<![A-Za-z0-9.§])(?P<count>(?:V\.5,? )?Count (?:VI|IV|V|III|II|I)\b)'
    r'|(?<![A-Za-z0-9.§])(?P<v7>V\.7(?: Part (?:III|II|I)\b| (?:III|II|I)(?![\w.]))?)'
    r'|(?<![A-Za-z0-9.§])(?P<tale>(?P<tr>VI|IV|V|III|II|I)\.(?P<tn>[1-9])(?!\d))'
    r'|(?<![\w])(?P<kn>K(?P<knum>[1-9])(?![\d\w]))'
    r'|(?<![\w])(?P<jn>J(?P<jnum>[1-9]|1\d|2[0-6])(?![\d\w]))'
    r'|(?<![\w])(?P<dn>D(?P<dnum>1[0-2]|[1-9])(?![\d\w]))'
    r'|(?P<epi>\bEpilogue\b)'
    r'|(?P<fore>\b(?:foreword|Of This Book)\b)'
    r'|(?P<inv>\bInvocation\b)'
    r'|(?P<lastnote>\bLast Note\b)'
    r'|(?P<know>\bBook of Knowings\b)'
    r'|(?P<bookn>\bBook (?P<bw>One|Two|Three|Four|Five|Six)\b)'
)

VALID_SECS = set()      # filled from the headings: '1', '1.2', ...


def sec_href(s1, s2):
    key = s1 + ('.' + s2 if s2 else '')
    if key not in VALID_SECS:
        return None
    return '#' + (SEC_IDS[s1] if not s2 else 's%s-%s' % (s1, s2))


def link_text(t):
    """Auto-link tale, section, note and document references in a run of plain (escaped) text."""
    def rep(m):
        g = m.group
        whole = g(0)
        before = m.string[max(0, m.start() - 8):m.start()]
        if g('adm'):
            sec = g('admsec')
            if sec is None:
                return '<a class="xr" href="Rivenkeep_Admiral.html#the-throne-rules">%s</a>' % whole
            aid = ADMIRAL_IDS.get(sec)
            return '<a class="xr" href="Rivenkeep_Admiral.html%s">%s</a>' % ('#' + aid if aid else '', whole)
        if g('tladder'):
            return '<a class="xr" href="Rivenkeep_Tongues.html#ladder">%s</a>' % whole
        if g('tcall'):
            return '<a class="xr" href="Rivenkeep_Tongues.html#a-callout">%s</a>' % whole
        if g('admbare'):
            return '<a class="xr" href="Rivenkeep_Admiral.html">%s</a>' % whole
        if g('tongues'):
            return '<a class="xr" href="Rivenkeep_Tongues.html">%s</a>' % whole
        if g('fight'):
            return '<a class="xr" href="Rivenkeep_Fight.html">%s</a>' % whole
        if g('orig'):
            return '<a class="xr" href="%s">%s</a>' % (ORIGINAL_V1, whole)
        if g('plain'):
            return '<a class="xr" href="%s">%s</a>' % (MODERN_V12, whole)
        if g('call'):
            return '<a href="#call-%s">%s</a>' % (g('calln'), whole)
        if g('sec'):
            if OTHER_DOC_SEC.search(before):
                return whole
            h = sec_href(g('s1'), g('s2'))
            return '<a href="%s">%s</a>' % (h, whole) if h else whole
        if g('count'):
            return '<a class="tl" href="%s#t-V-5">%s</a>' % (BOOK, whole)
        if g('v7'):
            return '<a class="tl" href="%s#t-V-7">%s</a>' % (BOOK, whole)
        if g('tale'):
            # v1.3 numbered two tales differently (its III.2 is VI.2, its VI.1 is VI.3): never link those.
            if re.search(r'(old |was |v1\.3’s )$', before) or not roman_ok(g('tr'), g('tn')):
                return whole
            return '<a class="tl" href="%s#t-%s-%s">%s</a>' % (BOOK, g('tr'), g('tn'), whole)
        if g('kn'):
            return '<a href="#k%s">%s</a>' % (g('knum'), whole)
        if g('jn'):
            return '<a href="#j%s">%s</a>' % (g('jnum'), whole)
        if g('dn'):
            return '<a href="#d%s">%s</a>' % (g('dnum'), whole)
        if g('epi'):
            return '<a class="tl" href="%s#t-epilogue">%s</a>' % (BOOK, whole)
        if g('fore'):
            return '<a class="tl" href="%s#foreword">%s</a>' % (BOOK, whole)
        if g('inv'):
            if before.endswith("v1.3’s "):
                return whole
            return '<a class="tl" href="%s#invocation">%s</a>' % (BOOK, whole)
        if g('lastnote'):
            return '<a class="tl" href="%s#t-last-note">%s</a>' % (BOOK, whole)
        if g('know'):
            return '<a class="tl" href="%s#knowings">%s</a>' % (BOOK, whole)
        if g('bookn'):
            return '<a class="tl" href="%s#book-%d">%s</a>' % (BOOK, BOOKNUM[g('bw')], whole)
        return whole
    return LINK_RE.sub(rep, t)


def link_html(s):
    """Apply link_text to the text runs of an HTML fragment, never inside a tag or an existing <a>."""
    parts = re.split(r'(<[^>]+>)', s)
    depth = 0
    for i, p in enumerate(parts):
        if p.startswith('<'):
            if re.match(r'<a[\s>]', p):
                depth += 1
            elif p.startswith('</a'):
                depth -= 1
            continue
        if depth == 0 and p:
            parts[i] = link_text(p)
    return ''.join(parts)


def inl(text, link=True):
    """Markdown inline -> HTML: code, links, smart quotes, escaping, emphasis, then auto-links."""
    store = []

    def keep(h):
        store.append(h)
        return '\x00%d\x00' % (len(store) - 1)

    t = re.sub(r'`([^`]+)`', lambda m: keep('<code>%s</code>' % html.escape(m.group(1), quote=False)), text)

    def mdlink(m):
        url = m.group(2)
        cls = '' if url.startswith('http') else ' class="xr"'
        return keep('<a%s href="%s">%s</a>' % (cls, html.escape(url), inl(m.group(1), False)))
    t = re.sub(r'\[([^\]]+)\]\(((?:https?://|Research/|Archive/|Rivenkeep_)[^)\s]+)\)', mdlink, t)
    if link:
        for k in PROTECT:
            if k in t:
                t = t.replace(k, keep(html.escape(smart_quotes(k), quote=False)))
    t = smart_quotes(t)
    t = html.escape(t, quote=False)
    t = re.sub(r'\*(\w+)\*s\b', r'<em>\1</em>s', t)                                    # *and*s
    t = re.sub(r'\*\*\*([^*]+)\*([^*]*)\*([^*]+)\*\*\*', r'<strong><em>\1</em>\2<em>\3</em></strong>', t)
    t = re.sub(r'\*\*\*([^*]+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*((?:[^*]|\*[^*\s][^*]*\*)*?)\*([^*\s][^*]*?)\*\*\*', r'<strong>\1<em>\2</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*(?=\S)(.+?)(?<=\S)\*(?![*\w])', r'<em>\1</em>', t)
    t = t.replace('<em>“moved”</em>', '<span class="pill mv">moved</span>').replace(
        '<em>“new”</em>', '<span class="pill nw">new</span>')
    t = t.replace('(<em>new</em>)', '<span class="pill nw">new</span>').replace(
        '<em>(new)</em>', '<span class="pill nw">new</span>')
    if link:
        t = link_html(t)
    t = re.sub('\x00(\\d+)\x00', lambda m: store[int(m.group(1))], t)
    return t


# ----------------------------------------------------------------------------------------------- blocks

LIST_RE = re.compile(r'^(\s*)(-|\d+\.)\s+(.*)$')
INDENTED = re.compile(r'^ {2,}\S')


def parse_quote(qlines):
    """'>' lines -> paragraphs (split at a bare '>'), each a list of lines."""
    paras, cur = [], []
    for q in qlines:
        q = q[1:].strip()
        if not q:
            if cur:
                paras.append(cur)
            cur = []
        else:
            cur.append(q)
    if cur:
        paras.append(cur)
    return paras


def parse(lines):
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i].rstrip('\n')
        if not ln.strip():
            i += 1
            continue
        if ln.startswith('### '):
            m = re.match(r'### (\d+\.\d+) (.*)$', ln)
            blocks.append(('h3', m.group(1), m.group(2)))
            i += 1
        elif ln.startswith('## '):
            m = re.match(r'## (\d+) · (.*)$', ln)
            blocks.append(('h2', m.group(1), m.group(2)) if m else ('h2x', ln[3:]))
            i += 1
        elif ln.startswith('# '):
            blocks.append(('h1', ln[2:]))
            i += 1
        elif ln.strip() == '---':
            blocks.append(('hr',))
            i += 1
        elif ln.startswith('>'):
            buf = []
            while i < n and lines[i].startswith('>'):
                buf.append(lines[i].rstrip('\n'))
                i += 1
            blocks.append(('quote', parse_quote(buf)))
        elif ln.startswith('|'):
            rows = []
            while i < n and lines[i].startswith('|'):
                r = lines[i].strip()
                if not re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', r):        # the separator row (a blank head row stays)
                    rows.append([c.strip() for c in r.strip('|').split('|')])
                i += 1
            blocks.append(('table', rows))
        elif LIST_RE.match(ln):
            items = []
            while i < n:
                cur = lines[i].rstrip('\n')
                m = LIST_RE.match(cur)
                if m:
                    items.append((len(m.group(1)), m.group(2) != '-', m.group(2), m.group(3), []))
                    i += 1
                    continue
                if cur.strip():
                    break
                # a blank line: the list goes on only if indented matter follows (it belongs to the last item)
                j = i
                while j < n and not lines[j].strip():
                    j += 1
                if not (j < n and INDENTED.match(lines[j]) and not LIST_RE.match(lines[j])):
                    break
                # it belongs to the last item it is indented under (past that item's marker), not to a deeper one
                ci = len(lines[j]) - len(lines[j].lstrip(' '))
                owner = next(it for it in reversed(items) if it[0] < ci)
                k = j
                chunk = []
                while k < n and (not lines[k].strip() or INDENTED.match(lines[k])) and not LIST_RE.match(lines[k]):
                    chunk.append(lines[k][ci:] if lines[k][:ci].strip() == '' else lines[k].lstrip())
                    k += 1
                owner[4].extend(parse(chunk))
                i = k
            blocks.append(('list', build_tree(items)))
        else:
            blocks.append(('p', ln.strip()))
            i += 1
    return blocks


def build_tree(items):
    """items: (indent, ordered, marker, text, extra) -> nested {'ordered','start','items':[{'text','children',...}]}."""
    root = {'ordered': items[0][1], 'start': items[0][2], 'items': [], 'indent': items[0][0]}
    stack = [root]
    for ind, ordered, marker, text, extra in items:
        while len(stack) > 1 and ind < stack[-1]['indent']:
            stack.pop()
        top = stack[-1]
        if ind > top['indent'] and top['items']:
            sub = {'ordered': ordered, 'start': marker, 'items': [], 'indent': ind}
            top['items'][-1]['children'].append(sub)
            stack.append(sub)
            top = sub
        top['items'].append({'text': text, 'children': [], 'extra': extra})
    return root


def render_list(lst, link=True):
    tag = 'ol' if lst['ordered'] else 'ul'
    start = ''
    if lst['ordered']:
        s = int(lst['start'].rstrip('.'))
        if s != 1:
            start = ' start="%d"' % s
    out = ['<%s%s>' % (tag, start)]
    for it in lst['items']:
        kids = ''.join(render_list(c, link) for c in it['children'])
        extra = ''.join(render_block(b, None, link) for b in it['extra'])
        out.append('<li>%s%s%s</li>' % (inl(it['text'], link), kids, extra))
    out.append('</%s>' % tag)
    return '\n'.join(out)


def render_quote(paras, link=True):
    return '<blockquote>%s</blockquote>' % ''.join(
        '<p>%s</p>' % '<br>'.join(inl(q, link) for q in para) for para in paras)


def cell_html(c, link):
    m = re.match(r'^\*(moved|new)\* · (.*)$', c)
    if m:
        cls = 'mv' if m.group(1) == 'moved' else 'nw'
        return '<span class="pill %s">%s</span> %s' % (cls, m.group(1), inl(m.group(2), link))
    return inl(c, link)


def render_table(rows, ctx):
    """ctx: the current h3 number ('3.8', ...), a section number, or 'front', for the per-table link rules."""
    ncol = len(rows[0])
    # (not "mid": the house sheet's .mid is a warning colour, which turned every 4-column table orange)
    cls = ' class="wide"' if ncol >= 5 else (' class="t4"' if ncol == 4 else '')
    nolink_cols = set()
    if ctx == 'front':
        nolink_cols = {0}          # Notes v1.0.0's own section numbers
    elif ctx == '5.0':
        nolink_cols = {0, 1}       # v1.3's and Notes v1.0.0's section numbers
    elif ctx == '3.8':
        nolink_cols = {0}          # the death ids themselves
    elif ctx == '8':
        nolink_cols = set(range(ncol))
    out = ['<div class="tw"><table%s>' % cls]
    if any(c for c in rows[0]):
        out.append('<tr>%s</tr>' % ''.join('<th>%s</th>' % inl(c, False) for c in rows[0]))
    for r in rows[1:]:
        rid = ''
        if ctx == '3.8':
            m = re.match(r'\*\*D(\d+)\*\*', r[0])
            if m:
                rid = ' id="d%s"' % m.group(1)
        tds = ''.join('<td>%s</td>' % cell_html(c, k not in nolink_cols) for k, c in enumerate(r))
        out.append('<tr%s>%s</tr>' % (rid, tds))
    out.append('</table></div>')
    return '\n'.join(out)


# Paragraphs that open a call-out box: start of the raw paragraph -> (class, title or None, absorb, mode)
#   title None: the bold lead becomes the title and the rest the body.  mode 'whole': the paragraph is the body;
#   'note': an italic paragraph, the body in the note style; 'colon': the body is what follows the first colon.
BOXES = [
    ('**And the memory theme.**', 'jn', None, 0, 'lead'),
    ('**The rules of the voice**', 'law', None, 1, 'lead'),
    ('**The shape of a tale**', 'law', None, 2, 'lead'),
    ('**The frame, made light**', 'pillar', None, 1, 'lead'),
    ('**The never-list**', 'warn', None, 0, 'lead'),
    ('**The agreement, shown and never stated:**', 'pillar', None, 1, 'lead'),
    ('**Fire that stays, and why each is safe:**', '', None, 0, 'lead'),
    ('**What it keeps exactly:**', 'law', None, 0, 'lead'),
    ('**Declined, with the reasons kept:**', 'warn', None, 1, 'lead'),
    ('**Optional: where the line of keeps stood.**', 'future', None, 0, 'lead'),
    ('**Where the Reckoning was overtaken.**', 'warn', None, 0, 'lead'),
    ('**The laws of the cast**', 'law', None, 1, 'lead'),
    ('**The rites of mourning,**', '', None, 1, 'lead'),
    ('**The strips**', 'pillar', "The strips, which are the art hook's count", 0, 'colon'),
    ('**Others the Book mourns without a name:**', '', None, 0, 'lead'),
    ("**Not Halyna's:**", '', None, 0, 'lead'),
    ('**A half waiting for its other half.**', 'pillar', None, 0, 'lead'),
    ('**What changed in v3.**', 'warn', None, 0, 'lead'),
    ('*Laws 1 to 7 are', 'law', 'The standing laws', 1, 'note'),
    ('**How to read the When column.**', '', None, 1, 'lead'),
    ('**The rule of the wood.**', 'pillar', None, 0, 'lead'),
    ('**How a wood leaf looks**', 'pillar', None, 1, 'lead'),
    ('**The Book is a translation.**', 'pillar', None, 0, 'lead'),
    ('**Where they live.**', '', None, 1, 'lead'),
    ('**The rules.**', 'law', None, 1, 'lead'),
    ('**Dropped or recast in v3.**', 'warn', None, 0, 'lead'),
    ('**The style rules**', 'law', None, 1, 'lead'),
    ("**Jack's lines, kept**", 'pillar', None, 1, 'lead'),
    ('**Cut, or recast.**', 'warn', None, 1, 'lead'),
    ("**The builder's gaps**", 'warn', None, 1, 'lead'),
    ('**Originality.**', 'warn', None, 0, 'lead'),
    ('**Names kept in NOTES only:**', '', None, 0, 'lead'),
    ('**Still to do.**', 'future', None, 0, 'lead'),
    ("**Jack's notes of 2026-10-03, verbatim.**", 'jn', None, 3, 'lead'),     # 1.16: his notes, his reading
]
SPLIT_LEADS = ('**The schedule.**', '**Examples.**', "**Every drawing in the Book's text.**", '**The ripenings**',
               '**Back-translation.**', '**Still open, for Jack.**', '**How it was made.**', '**The counts.**')
LEADS = ('Jack read v2.0 and its Plain Words', 'Each note is quoted from his own words', 'v2.0 (2026-10-01) applied',
         'Nothing below is said in any tale', 'v1.3 closed with', 'All of these run seed before payoff',
         'Stone on the left, wood on the right', 'Every element these lines pointed at',
         'Kept here so that no choice is lost', 'v2.0 gave the coast a custom', 'The Tongues pass that K2 asked for',
         "Jack's notes of 2026-10-03 keep the Book")


def cap(rest):
    """Capitalise a body that now opens a box or follows a sub-head (never a version number: v2.0, v1.3)."""
    if rest and rest[0].islower() and not re.match(r'v\d', rest):
        return rest[0].upper() + rest[1:]
    return rest


def split_lead(p):
    """'**Lead.** rest' -> (lead, paren, rest).  paren is a leading '(…)' of rest, if any."""
    m = re.match(r'^\*\*(.+?)\*\*(.*)$', p)
    if not m:
        return None, None, p
    lead, rest = m.group(1), m.group(2)
    paren = None
    pm = re.match(r'^\s*(\([^)]*\))[.:]?\s*(.*)$', rest)
    if pm:
        paren, rest = pm.group(1), pm.group(2)
    rest = re.sub(r'^[\s,:]+', '', rest)
    lead = lead.rstrip('.:,')
    return lead, paren, cap(rest)


def h4(lead, paren=None, link=True):
    hn = ' <span class="hn">%s</span>' % inl(paren, link) if paren else ''
    return '<h4>%s%s</h4>' % (inl(lead, False), hn)


def render_para(p, ctx, link=True):
    if p.startswith('*') and not p.startswith('**') and p.endswith('*') and not p.endswith('**'):
        return '<p class="note">%s</p>' % inl(p[1:-1], link)
    if p.startswith(LEADS):
        return '<p class="lead">%s</p>' % inl(p, link)
    m = re.match(r'^\*\*(.+?)\*\*(.*)$', p)
    if m and not m.group(1).startswith('*'):
        rest = m.group(2)
        if not rest.strip():
            return h4(m.group(1).rstrip('.:'))
        if re.match(r'^\s*\([^)]*\):?$', rest):
            return h4(m.group(1).rstrip('.:'), rest.strip().rstrip(':'), link)
        if ctx == '4.2' or p.startswith(SPLIT_LEADS):
            lead, paren, body = split_lead(p)
            return h4(lead, paren, link) + '\n<p>%s</p>' % inl(body, link)
    return '<p>%s</p>' % inl(p, link)


def render_block(b, ctx, link=True):
    if b[0] == 'p':
        return render_para(b[1], ctx, link)
    if b[0] == 'list':
        return render_list(b[1], link)
    if b[0] == 'table':
        return render_table(b[1], ctx)
    if b[0] == 'quote':
        return render_quote(b[1], link)
    raise ValueError(b)


J_RE = re.compile(r'^\*\*J(\d+) · (.+?)\*\*(.*)$')
K_RE = re.compile(r'^\*\*K(\d+) · \*(.+)\*\*\*$')


def note_head(b):
    return b[0] == 'p' and (J_RE.match(b[1]) or K_RE.match(b[1]))


def render_body(blocks, ctx_sec):
    """Render the blocks of one numbered section (between its h2 and the next)."""
    out = []
    ctx = ctx_sec
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b[0] == 'hr':
            i += 1
            continue
        if b[0] == 'h3':
            ctx = b[1]
            out.append('<h3 id="s%s"><span class="no">%s ·</span> %s</h3>' % (b[1].replace('.', '-'), b[1], inl(b[2], False)))
            i += 1
            continue
        if b[0] == 'p':
            p = b[1]
            # Jack's notes: K1-K9 of 2026-10-02 and J1-J26 of 2026-09-30, one box each, with what follows them
            km, jm = K_RE.match(p), J_RE.match(p)
            if km or jm:
                inner = []
                if km:
                    nid, head = 'k' + km.group(1), 'K%s · Jack, 2026-10-02' % km.group(1)
                    inner.append('<p class="kq"><em>%s</em></p>' % inl(km.group(2), False))
                else:
                    nid, head = 'j' + jm.group(1), 'J%s · %s' % (jm.group(1), jm.group(2))
                    if jm.group(3).strip():
                        inner.append('<p>%s</p>' % inl(jm.group(3).strip()))
                j = i + 1
                while j < len(blocks) and (blocks[j][0] in ('list', 'table', 'quote') or (
                        blocks[j][0] == 'p' and not blocks[j][1].startswith('**'))):
                    inner.append(render_block(blocks[j], ctx))
                    j += 1
                out.append('<div class="s jn" id="%s"><div class="ct">%s</div>\n%s</div>' % (
                    nid, inl(head, False), '\n'.join(inner)))
                i = j
                continue
            box = next((r for r in BOXES if p.startswith(r[0])), None)
            if box:
                _, cls, title, absorb, mode = box
                if mode == 'lead':
                    lead, paren, rest = split_lead(p)
                    t = title or (lead + (' ' + paren if paren else ''))
                    body = '<p>%s</p>' % inl(rest) if rest else ''
                elif mode == 'colon':
                    t = title
                    body = '<p>%s</p>' % inl(cap(p.split(': ', 1)[1]))
                elif mode == 'note':
                    t = title
                    body = '<p class="note">%s</p>' % inl(p[1:-1])
                else:
                    t = title
                    body = '<p>%s</p>' % inl(p)
                inner = [body] if body else []
                for k in range(absorb):
                    nb = blocks[i + 1 + k]
                    assert nb[0] in ('list', 'table', 'p', 'quote') and not note_head(nb), (p[:40], nb)
                    inner.append(render_block(nb, ctx))
                out.append('<div class="s%s"><div class="ct">%s</div>\n%s</div>' % (
                    (' ' + cls) if cls else '', inl(t, False), '\n'.join(inner)))
                i += 1 + absorb
                continue
        if b[0] == 'list' and ctx == '7.2':
            for k, it in enumerate(b[1]['items'], start=1):
                kids = ''.join(render_list(c) for c in it['children'])
                out.append('<div class="s call" id="call-%d"><div class="ct">Call %d</div>\n<p>%s</p>%s</div>' % (
                    k, k, inl(it['text']), ('\n' + kids) if kids else ''))
            i += 1
            continue
        out.append(render_block(b, ctx))
        i += 1
    return '\n'.join(out)


# ----------------------------------------------------------------------------------------------- page

def house_head():
    src = open(HOUSE, encoding='utf-8').read()
    fonts = re.search(r'<link href="https://fonts\.googleapis\.com[^>]+>', src).group(0)
    fonts = re.sub(r'&(?!amp;)', '&amp;', fonts)     # the same URL, with its ampersands escaped
    style = re.search(r'<style>\n?(.*?)</style>', src, re.S).group(1)
    style, k = re.subn(r'--doc-version:"[^"]*"', '--doc-version:"%s"' % VERSION, style)
    assert k == 1
    return fonts, style.rstrip('\n') + '\n' + EXTRA_CSS.strip('\n') + '\n'


def compose():
    """notes_v3.md, with the pointers of EDITS, and sections 1.15 and 1.16 spliced in before section 2."""
    raw = open(SRC, encoding='utf-8').read()
    for a, b in EDITS:
        assert raw.count(a) == 1, a
        raw = raw.replace(a, b)
    added = '\n\n'.join(open(f, encoding='utf-8').read().strip('\n') for f in ADDED)
    assert raw.count(SECTION_ANCHOR) == 1
    raw = raw.replace(SECTION_ANCHOR, '\n' + added + '\n' + SECTION_ANCHOR)
    for a, b in POST_EDITS:
        assert raw.count(a) == 1, a
        raw = raw.replace(a, b)
    open(COMPOSED, 'w', encoding='utf-8').write(raw)
    return raw


def main():
    raw = compose()
    lines = raw.split('\n')
    blocks = parse(lines)

    # The front matter: everything before "## CONTENTS"; the contents list is rebuilt from the headings.
    ci = next(k for k, b in enumerate(blocks) if b[0] == 'h2x' and b[1] == 'CONTENTS')
    front = blocks[:ci]
    toc_list = blocks[ci + 1]
    assert toc_list[0] == 'list'
    h2_titles = {}
    for it in toc_list[1]['items']:
        h2_titles[str(len(h2_titles))] = it['text']
    rest = blocks[ci + 2:]

    # Sections
    sections = []
    cur = None
    for b in rest:
        if b[0] == 'h2':
            cur = {'num': b[1], 'title': h2_titles[b[1]], 'blocks': [], 'h3': []}
            sections.append(cur)
            VALID_SECS.add(b[1])
        elif cur is not None:
            cur['blocks'].append(b)
            if b[0] == 'h3':
                cur['h3'].append((b[1], b[2]))
                VALID_SECS.add(b[1])
    assert [s['num'] for s in sections] == [str(k) for k in range(9)], [s['num'] for s in sections]

    fonts, style = house_head()
    meta = '*Notes %s · for the Book %s · %s*' % (VERSION, BOOK_VERSION, DATE)
    assert any(b == ('p', meta) for b in front), meta
    paras = [b[1] for b in front if b[0] == 'p' and b[1] != meta]
    quote = [b[1] for b in front if b[0] == 'quote']
    tables = [b[1] for b in front if b[0] == 'table']
    assert len(paras) == 3 and len(quote) == 1 and len(tables) == 1, (paras, quote)
    assert paras[2].startswith('**Where the sections of Notes v1.0.0 went.**')

    o = []
    o.append('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
             '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
             '<title>Rivenkeep — The Legends: Notes</title>\n%s\n<style>\n%s</style>\n</head>\n<body>' % (fonts, style))
    o.append('<header>\n<h1>Rivenkeep — The Legends: Notes</h1>\n'
             '<div class="sub">The Design Companion to The Book of the Riven Stone</div>\n'
             '<div class="meta"><span class="ver"></span> · for <a href="%s">the Book</a> %s · %s · '
             'Owns everything about the Legends that is not the story: how the Book was made, how its pieces fit, '
             'and how it enters the game · Nothing in this doc is Book text, and nothing in it touches the simulation · '
             'Companions: <a href="%s">The Legends</a>, <a href="Rivenkeep_Tongues.html">The Tongues</a>, '
             '<a href="Rivenkeep_Admiral.html">The Admiral</a>, <a href="Rivenkeep_Fight.html">The Fight</a> · '
             'Version history at the bottom of this doc.</div>\n</header>' % (BOOK, BOOK_VERSION, DATE, BOOK))
    o.append('<nav>\n%s\n<a href="%s">The Book &rarr;</a>\n</nav>' % (
        '\n'.join('<a href="#%s">%s</a>' % (a, t) for a, t in NAV), BOOK))
    o.append('<div class="ctn">')

    # This document
    lead = inl(paras[0][1:-1])
    lead = lead.replace('This document sits beside the Book.',
                        'This document sits beside <a href="%s">the Book</a>.' % BOOK, 1)
    assert 'href="%s">the Book</a>' % BOOK in lead
    q = quote[0]
    assert len(q) == 1
    q = re.sub(r'^\*\*How to read the references\.\*\*\s*', '', ' '.join(q[0]))
    wl, _, wrest = split_lead(paras[2])
    moved = '<h3 id="moved">%s</h3>\n<p>%s</p>\n%s' % (inl(wl, False), inl(wrest), render_table(tables[0], 'front'))
    toc = ['<div class="toc">']
    for s in sections:
        sid = SEC_IDS[s['num']]
        toc.append('<div class="tg"><div class="t2"><span class="n">%s</span><a href="#%s">%s</a></div>' % (s['num'], sid, inl(s['title'], False)))
        for n, t in s['h3']:
            toc.append('<div class="t3">%s · <a href="#s%s">%s</a></div>' % (n, n.replace('.', '-'), inl(t, False)))
        toc.append('</div>')
    toc.append('</div>')
    o.append('<section id="about">\n<h2>This Document</h2>\n<p class="lead">%s</p>\n'
             '<div class="s pillar"><div class="ct">What it replaces, and what it gathers</div>\n<p>%s</p></div>\n'
             '<div class="s"><div class="ct">How to read the references</div>\n<p>%s</p></div>\n'
             '%s\n<h3 id="contents">Contents</h3>\n%s\n</section>' % (
                 lead, inl(paras[1][1:-1]), inl(q, False), moved, '\n'.join(toc)))

    for s in sections:
        sid = SEC_IDS[s['num']]
        if sid == 'history':
            body = []
            for b in s['blocks']:
                if b[0] == 'p':
                    body.append(render_para(b[1], '8', link=False))
                elif b[0] == 'table':
                    body.append(render_table(b[1], '8'))
                elif b[0] != 'hr':
                    raise ValueError(b)
            o.append('<section id="history">\n<h2><span class="n">8</span>Version History</h2>\n%s\n</section>' % '\n'.join(body))
        else:
            o.append('<section id="%s">\n<h2><span class="n">%s</span>%s</h2>\n%s\n</section>' % (
                sid, s['num'], inl(s['title'], False), render_body(s['blocks'], s['num'])))

    o.append('</div>')
    o.append('<footer>\nRivenkeep — The Legends: Notes · <span class="ver"></span> · The design companion to '
             '<a href="%s">The Book of the Riven Stone</a> · How it was made, how its pieces fit, how it enters the game · '
             'Nothing here is Book text\n</footer>\n</body>\n</html>\n' % BOOK)
    page = '\n'.join(o)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(page)
    print('wrote', OUT, len(page), 'bytes;', meta)


if __name__ == '__main__':
    main()
