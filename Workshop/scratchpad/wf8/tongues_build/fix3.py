# -*- coding: utf-8 -*-
"""Third round: the specs' own section numbers, said in words; mask ids in the descent sheet. Scratch only."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def patch(fn, pairs):
    p = os.path.join(HERE, fn)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (fn, a[:80])
        s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf-8').write(s)


patch('build.py', [
    ("""    ('see §3', 'see the collisions above'),
]""",
     """    ('see §3', 'see the collisions above'),
    ('the First Tongue spec §3.3', 'the First Tongue’s reserve'),
    ('the Orrowen spec §5.12', 'the Orrowen suffixes'),
    ('the Orrowen spec §11.4', 'the spec'),
    ('Rewritten in v2 as a joined running hand: §8.', 'Rewritten in v2 as a joined running hand.'),
    ('(An originality law, after the runes: §13.)', '(An originality law, after the runes.)'),
    ('a word not in §7.7', 'a word not in the inventory'),
    ('the §6.6 end rule', 'the end rule'),
    ('the §6.5 bites', 'the bites'),
    ('wf6 §9c\\'s list', 'v0.1’s near-call list'),
    ("wf6 §9c's list", 'v0.1’s near-call list'),
    ('(wf6 §11b: tresket by the rule)', '(by the rule, tresket)'),
    ("the spec's §4.3 gives Hal rea", 'v0.1 gave Hal rea'),
    ('(lexicon §8.3 left it open)', '(the lexicon left it open)'),
    (', lexicon §4.3)', ', the lexicon’s seam rule)'),
    ("which §3.6's conjugated prepositions make natural", 'which the conjugated prepositions make natural'),
    ('§3.6 never said', 'the spec never said'),
    ('§3.5 never said', 'the spec never said'),
    ('Same §3.5 gap', 'The same gap'),
    ("the pilot's own §3 collision note", "the pilot's own collision note"),
    ('§6.1 does not allow that', 'the runner rules do not allow that'),
    ("(the part's own gloss, §5.2, which I did not use)", "(the part's own gloss, which I did not use)"),
    ("(§7.3's gloss)", "(the bind's gloss)"),
    ('§11.2 ("a new thing-sign', 'The layout rule ("a new thing-sign'),
    ('clashes with §10.3 ("a thing', 'clashes with the composition rule ("a thing'),
    ('The validator applies §11.2 alone.', 'The validator applied the first alone.'),
    ('§6.1 makes a split one act', 'The runner rules make a split one act'),
    ('§21.8 states the rule', 'The additions state the rule'),
    ("The pilot's §3 findings", "The pilot's findings"),
    ('decode report §4', 'the decode report'),
    ('new · §10.9', 'new · a likeness'),
    ('§10.9', 'a likeness'),
    ('§11.7', 'the saying both peoples share'),
]"""),
    ("""def fixS(s):
    s = spec_words(s)
    s = strip_refs(s)""",
     """def fixS(s):
    s = spec_words(s)
    s = re.sub(r'\\(?§3\\.11 (D\\d+)\\)?', lambda m: ('(' if m.group(0).startswith('(') else '') + m.group(1) + (')' if m.group(0).endswith(')') else ''), s)
    s = re.sub(r'^§6\\.7$', 'the punctuation', s)
    s = re.sub(r'\\(§[\\d.]+: ', '(', s)
    s = strip_refs(s)"""),
    ("""    s = s.replace('For the Shoreland designer', "A Shoreland word: its Orrowen parts are in the Book's translations (§2.5)")
    return fixall(s)""",
     """    s = s.replace('For the Shoreland designer', "A Shoreland word: its Orrowen parts are in the Book's translations (§2.5)")
    return spec_words(fixall(s))"""),
    ("""TABS['g_changes'] = TG(r'^### 2\\.2 What v2 changes', 0)""",
     """TABS['g_changes'] = TG(r'^### 2\\.2 What v2 changes', 0, cols=[0, 1])"""),
    ("""TABS['g_tokens'] = TG(r'^### 13\\.3 Tokens, at a glance', 0)""",
     """TABS['g_tokens'] = TG(r'^### 13\\.3 Tokens, at a glance', 0, cols=[0, 1])"""),
    ("""    def plain(m):
        sv = m.group(0)
        k[0] += 1
        if '<defs>' in sv or 'id="' in sv:
            return uniq_ids(sv, 'ds%d-' % k[0])""",
     """    def plain(m):
        sv = m.group(0)
        k[0] += 1
        if '<defs>' in sv or 'id="' in sv:
            return uniq_ids(fix_mask_ids(sv), 'ds%d-' % k[0])"""),
])

# every fixer ends by saying the known references in words
p = os.path.join(HERE, 'build.py')
s = open(p, encoding='utf-8').read()
for name in ('fixS', 'fixA', 'fixG', 'fixL'):
    i = s.index('def %s(s):' % name)
    j = s.index('    return fixall(s)', i)
    s = s[:j] + '    return spec_words(fixall(s))' + s[j + len('    return fixall(s)'):]
s = s.replace("""    s = re.sub(r'\\s*\\(see §\\w+ of the spec\\)', '', s)""", """    s = re.sub(r'[:,;]?\\s*see §\\w+ of the spec', '', s)""")
open(p, 'w', encoding='utf-8').write(s)

p = os.path.join(HERE, 'mdlib.py')
s = open(p, encoding='utf-8').read()
a = """    s = re.sub(r'\\s*\\(see §\\w+ of the spec\\)', '', s)"""
assert a in s
s = s.replace(a, """    s = re.sub(r'[:,;]?\\s*see §\\w+ of the spec', '', s)""")
open(p, 'w', encoding='utf-8').write(s)

patch('p1.html', [
    ('a reader who had only the rules in §2–§3,', 'a reader who had only the rules of the Orrowen and course-hand chapters,'),
])
patch('p4.html', [
    ('<strong>The First Tongue</strong> (new §2)', '<strong>The First Tongue</strong> (new <a href="#first-tongue">§2</a>)'),
    ('<strong>The dry cut</strong> (new §5)', '<strong>The dry cut</strong> (new <a href="#dry-cut">§5</a>)'),
    ('<strong>The leaf-hand</strong> (new §6)', '<strong>The leaf-hand</strong> (new <a href="#leaf-hand">§6</a>)'),
    ('<strong>The grain v2</strong> (new §9)', '<strong>The grain v2</strong> (new <a href="#grain2">§9</a>)'),
    ('<strong>Tier 3</strong> (new §11, note 5)', '<strong>Tier 3</strong> (new <a href="#tier3">§11</a>, note 5)'),
])
print('fix3 ok')
