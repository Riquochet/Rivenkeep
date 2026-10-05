# -*- coding: utf-8 -*-
"""Second round of builder fixes (ids, stray spec references, emphasis). Scratch only."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def patch(fn, pairs):
    p = os.path.join(HERE, fn)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (fn, a[:80])
        s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf-8').write(s)


patch('mdlib.py', [
    ("""    s = re.sub(r'\\*\\*([^*]+?)\\*([^*]+?)\\*\\*\\*', r'<strong>\\1<em>\\2</em></strong>', s)""",
     """    s = re.sub(r'\\*\\*(.+?)\\*([^*]+)\\*\\*\\*', r'<strong>\\1<em>\\2</em></strong>', s)"""),
    ("""def strip_refs(s):
    s = re.sub(r'\\s*\\((?:see )?§[\\d.a-z]+(?:[,;–-]\\s*§?[\\d.a-z]+)*\\)', '', s)""",
     """def strip_refs(s):
    s = re.sub(r'\\s*\\((?:see )?§[\\d.a-z]+(?:[,;–-]\\s*§?[\\w.]+)*\\)', '', s)
    s = re.sub(r'\\s*\\(see §\\w+ of the spec\\)', '', s)
    s = re.sub(r'\\s*\\((?:was Hal [^,)]+), shoreland §[\\d.]+\\)', lambda m: ' (' + m.group(0).strip()[1:].split(',')[0] + ' in v0.1)', s)"""),
])

patch('build.py', [
    # unique prefixes for repeated dry-cut drawings
    ("""def dry(key):
    tok, measure, title = DRY[key]
    s, st = RC.render(tok, measure=measure, title=title, desc='Dry cut tokens: ' + tok, pfx='d' + key[:3])""",
     """DRYN = [0]


def dry(key):
    tok, measure, title = DRY[key]
    DRYN[0] += 1
    s, st = RC.render(tok, measure=measure, title=title, desc='Dry cut tokens: ' + tok, pfx='d%d%s' % (DRYN[0], key[:3]))"""),
    # the descent sheet repeats a grain sign's ids when two rows show one sign
    ("""    def plain(m):
        sv = m.group(0)
        if 'class="stone-ink"' in sv or '<defs>' in sv:
            return sv""",
     """    def plain(m):
        sv = m.group(0)
        k[0] += 1
        if '<defs>' in sv or 'id="' in sv:
            return uniq_ids(sv, 'ds%d-' % k[0])
        if 'class="stone-ink"' in sv:
            return sv"""),
    # the whole lexicon: drop the specs' own section numbers and file names from its cells
    ("""        d = re.sub(r'\\s*\\(reserve, ancestor §3\\.3\\)', ' (reserve)', d)""",
     """        d = re.sub(r'\\s*\\(reserve, ancestor §3\\.3\\)', ' (reserve)', d)
        d = fixall(d)
        d = re.sub(r',?\\s*§[\\d.]+[a-z]?', '', d)
        d = re.sub(r'\\(\\s*\\)', '', d)"""),
    ("""                           html.escape(r['pos']), html.escape(r['class']), inline(r['meanings']),""",
     """                           html.escape(r['pos']), html.escape(r['class']), inline(re.sub(r'\\s*\\(§[\\d.]+\\)', '', r['meanings'])),"""),
])


# the tables' fixers: known references to the specs' own sections, said in words
patch('build.py', [
    ("""def fixS(s):
    s = strip_refs(s)""",
     """SPEC_WORDS = [
    ('the word is in §7.7', 'the word is in the inventory'),
    ('the First Tongue spec §3.2 and §4.4', 'the First Tongue’s roots and derivations'),
    ('their Hal forms are in the First Tongue spec §3.2', 'their Hal forms are in the First Tongue’s roots'),
    ('the First Tongue spec §1.7 (1)', 'the lore call-out, item 1'),
    ('ancestor.md` §1.7 (1)', 'the lore call-out, item 1'),
    ('§14a', ''),
    ('A15 in the new §21.8', 'A15, a new rule'),
    ('A16 in §21.8', 'A16, a new rule'),
    ('§21.8', 'the rules'),
    ('see §3', 'see the collisions above'),
]


def spec_words(s):
    for a, b in SPEC_WORDS:
        s = s.replace(a, b)
    return s


def fixS(s):
    s = spec_words(s)
    s = strip_refs(s)"""),
    ("""def fixA(s):
    s = strip_refs(s)""",
     """def fixA(s):
    s = spec_words(s)
    s = strip_refs(s)"""),
    ("""def fixG(s):
    s = strip_refs(s)""",
     """def fixG(s):
    s = spec_words(s)
    s = re.sub(r'^§[\\d.]+\\s+', '', s)
    s = re.sub(r'^§10\\.9$', 'a likeness', s)
    s = re.sub(r'^§9\\.2$', 'no new sign', s)
    s = re.sub(r'^§[\\d.]+$', '', s)
    s = strip_refs(s)"""),
    ("""def fixL(s):
    s = strip_refs(s)""",
     """def fixL(s):
    s = spec_words(s)
    s = re.sub(r'^§[\\d.]+$', '', s)
    s = strip_refs(s)"""),
])
print('fix2 ok')
