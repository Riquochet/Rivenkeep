"""The merged lexicon for Rivenkeep_Tongues.html v0.3.0 (scratch only; never goes into Docs/).

Reads wf8/lexicon_orrowen_full.tsv (the merge's 3,015 rows) read-only, groups it by field exactly as the v0.2
builder did (build.py olex(): the First Tongue root's field, a compound with its head), and renders
  * the per-field counts,
  * a representative selection of each field (stratified by source, evenly spaced through the alphabet,
    preferring words the Book uses),
  * every entry added in translation (the pilots' 23 and the merge's 135), whole.
"""
import csv
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mdlib import W7, inline, fixall  # noqa: E402

WF8 = os.path.dirname(HERE)
LEX = WF8 + '/lexicon_orrowen_full.tsv'
sys.path.insert(0, W7 + '/ancestor')
import roots_core as RCORE  # noqa: E402  (read-only)

FIELDS = [('stone', 'Stone, wood and building'), ('bond', 'Faith, bond and kin'), ('hearth', 'Hearth and people'),
          ('war', 'The wall, the war, the sea-road'), ('sea', 'Sea, land and growing things'),
          ('sky', 'Sky, weather, fire and time'), ('body', 'Body, life and feeling'),
          ('speech', 'Speech, writing and mind'), ('acts', 'Other acts'), ('quality', 'Qualities'),
          ('number', 'Numbers'), ('small', 'Small words and set phrases'), ('affix', 'Affixes'),
          ('names', 'Names, places and loans')]
SRCMARK = {'canon': 'C', 'reserve': 'R', 'tier3': 'T', 'tier3-sys': '·'}
SRC_ORDER = ['canon', 'reserve', 'tier3', 'tier3-sys']

ROWS = list(csv.DictReader(open(LEX, encoding='utf-8'), delimiter='\t'))
assert len(ROWS) == 3015 and ROWS[-1]['id'] == 'O3015', (len(ROWS), ROWS[-1]['id'])


def num(r):
    return int(r['id'][1:])


def _field_map():
    F = {}
    for r in RCORE.ROOTS:
        for part in r['root'].split('/'):
            F[part.strip().strip('*').strip()] = r['field']
        F[r['root']] = r['field']
    for r in json.load(open(W7 + '/ancestor/reserve.json', encoding='utf-8')):
        F[r['root'].strip('*')] = r['field']
    return F


def group_rows(rows):
    """The v0.2 builder's grouping, verbatim in its logic."""
    F = _field_map()
    byword = {}
    groups = {k: [] for k, _ in FIELDS}

    def field_of(r):
        pos = r['pos']
        if 'name' in pos or 'loan' in pos or r['root'].startswith('(Seilrhass)'):
            return 'names'
        if pos.startswith('suf') or pos == 'pref':
            return 'affix'
        if pos.split(',')[0] == 'num':
            return 'number'
        roots = [x.strip().lstrip('*') for x in r['root'].split(',') if x.strip()]
        fs = [F.get(x) for x in roots]
        if '^' in r['formation'] and len(fs) >= 2 and fs[-1]:
            return fs[-1]
        good = [f for f in fs if f and f not in ('small', 'affix')]
        if good:
            return good[0]
        if fs and fs[0]:
            return fs[0]
        base = re.split(r'[+^ ]', r['formation'])[0].strip('-') if r['formation'] else ''
        return byword.get(base, 'small')
    for r in rows:
        f = field_of(r)
        if f == 'affix' and not r['pos'].startswith('suf'):
            f = 'small'
        byword.setdefault(r['orrowen'], f)
        groups.setdefault(f, []).append(r)
    return groups


GROUPS = group_rows(ROWS)
# the v0.2 doc's own grouping of its 2,880 rows, to check the logic reproduces it
_G0 = group_rows([r for r in ROWS if num(r) <= 2880])
V02_FIELD_COUNTS = {'stone': 409, 'bond': 245, 'hearth': 154, 'war': 241, 'sea': 291, 'sky': 151, 'body': 170,
                    'speech': 167, 'acts': 372, 'quality': 336, 'number': 63, 'small': 115, 'affix': 19, 'names': 147}
assert {k: len(v) for k, v in _G0.items() if v} == V02_FIELD_COUNTS, {k: len(v) for k, v in _G0.items()}


def _rowid_forms():
    """The merge report's own map (its section 2.3): each additions row id -> the entry it became."""
    from mdlib import load, tables_after, find
    R = load(WF8 + '/merge_report.md')
    h, rows, _ = tables_after(R, find(R, r'^### 2\.3'))[0]
    m = {}
    for r in rows:
        form = r[1].strip('*')
        for rid in re.findall(r'\(((?:O-)?[SW]\d\d-\d\d)\)', r[2]):
            m[rid] = form
    return m


ROWID = _rowid_forms()


def _rowid(mm):
    rid = mm.group(0)
    if rid in ROWID:
        return '*%s*' % ROWID[rid]
    return re.match(r'(?:O-)?([SW]\d\d)', rid).group(1) + '’s additions'


def clean_deriv(r):
    """The v0.2 builder's cell_from, plus the merge's unit notes made readable (no scratch paths)."""
    d = r['derivation']
    if r['source'] == 'tier3-sys':
        d = re.sub(r" '[^']*'", '', d)
        d = re.sub(r" \(('[^)]*'|[^)]*)\)$", '', d)
    d = re.sub(r'\s*\(reserve, ancestor §3\.3\)', ' (reserve)', d)
    # the merge's notes: "[wf8 units S02, S03]" -> "(units S02, S03)"; "[wf8: …]" -> "(…)"
    d = re.sub(r'\[wf8 (units? [^\]]+)\]', r'(\1)', d)
    d = re.sub(r'\[wf8:\s*([^\]]+)\]', r'(\1)', d)
    d = d.replace('legends_v13', 'the Book')
    d = d.replace('backtrans I.1', 'the I.1 back-translation')
    d = d.replace('a phrase, the dual of the Orrowen spec:', 'a phrase, the dual:')
    d = re.sub(r'\b(?:O-)?[SW]\d\d-\d\d\b', _rowid, d)
    d = fixall(d)
    d = re.sub(r',?\s*§[\d.]+[a-z]?(?: item \d+)?', '', d)
    d = re.sub(r'\(\s*\)', '', d)
    d = re.sub(r'\s*\(?(?:ancestor|orrowen_v2|lexicon_orrowen)[^;)]*§[\d.]+\)?', '', d)
    d = re.sub(r'\s*\((?:the )?(?:Orrowen spec|lexicon summary|First Tongue spec)\)', '', d)
    d = d.replace('; pilot I.1', ' (I.1 pilot)').replace('pilot I.1', 'I.1 pilot')
    d = re.sub(r'[ \t]{2,}', ' ', d)
    d = re.sub(r'\s+([,.;:])', r'\1', d)
    assert 'wf8' not in d and 'wf7' not in d, d
    return d.strip()


def row_html(r):
    mark = SRCMARK.get(r['source'], '')
    hal = ('<i>%s</i>' % html.escape(r['hal'])) if r['hal'] else ''
    dc = r['dry_cut']
    if r['logogram']:
        logo = html.escape(r['logogram'])
    elif dc.startswith('left out'):
        logo = '<span class="dim">left out</span>'
    elif dc.startswith('(not cut'):
        logo = '<span class="dim">not cut</span>'
    else:
        logo = '<span class="dim">letters</span>'
    sense = inline(re.sub(r'\s*\(§[\d.]+\)', '', r['meanings']))
    return ('<tr%s><td><b>%s</b></td><td>%s</td><td>%s · %s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            % (' class="cn"' if r['source'] == 'canon' else '', html.escape(r['orrowen']), hal,
               html.escape(r['pos']), html.escape(r['class']), sense, inline(clean_deriv(r)), logo, mark))


HEAD = ('<div class="tw"><table class="olex"><tr><th>Orrowen</th><th>Hal</th><th>pos · cl.</th><th>Sense</th>'
        '<th>From</th><th>Dry cut</th><th></th></tr>')


def pick(rows, n):
    """n rows, stratified by source (at least one of each source present), evenly spaced alphabetically;
    among the rules-made rows, words the Book uses first."""
    if len(rows) <= n:
        return list(rows)
    by = {s: [r for r in rows if r['source'] == s] for s in SRC_ORDER}
    by = {s: v for s, v in by.items() if v}
    quota = {s: max(1, round(n * len(v) / len(rows))) for s, v in by.items()}
    while sum(quota.values()) > n:
        s = max(quota, key=lambda k: quota[k])
        quota[s] -= 1
    while sum(quota.values()) < n:
        s = max(by, key=lambda k: len(by[k]) - quota[k])
        quota[s] += 1
    out = []
    for s, v in by.items():
        pool = v
        if s in ('tier3-sys', 'tier3'):
            used = [r for r in v if r['book_lemmas'].strip()]
            if len(used) >= quota[s]:
                pool = used
        k = quota[s]
        idx = sorted(set(int(round((i + 0.5) * len(pool) / k - 0.5)) for i in range(k)))
        out.extend(pool[i] for i in idx)
    key = {id(r): i for i, r in enumerate(rows)}
    return sorted(out, key=lambda r: key[id(r)])


def src_counts(rows):
    c = {s: 0 for s in SRC_ORDER}
    for r in rows:
        c[r['source']] = c.get(r['source'], 0) + 1
    return c


def fmt(n):
    return '{:,}'.format(n)


# ---------------------------------------------------------------- the numbers
N = len(ROWS)
SRC = src_counts(ROWS)
LOGO = sum(1 for r in ROWS if r['logogram'])
LOGO_V02 = sum(1 for r in ROWS if r['logogram'] and num(r) <= 2880)
PILOT = [r for r in ROWS if 2857 < num(r) <= 2880]
MERGE = [r for r in ROWS if num(r) > 2880]
ADDED = PILOT + MERGE
assert len(PILOT) == 23 and len(MERGE) == 135 and LOGO_V02 == 1767

# entries touched at the merge (new senses, regular plurals), by their derivation notes
TOUCHED = [r for r in ROWS if num(r) <= 2880 and 'wf8' in r['derivation']]


def kind_of_added(r):
    f = r['formation']
    if f == 'phrase' or ' ' in r['orrowen']:
        return 'phrase'
    if '^' in f:
        return 'compound'
    if f.startswith('na-'):
        return 'na-'
    return 'suffixed'


ADDED_KINDS = {}
for r in ADDED:
    ADDED_KINDS[kind_of_added(r)] = ADDED_KINDS.get(kind_of_added(r), 0) + 1
assert ADDED_KINDS == {'phrase': 154, 'na-': 1, 'suffixed': 2, 'compound': 1}, ADDED_KINDS

# the v0.2 table "How the words are made" counted the builder's 2,857 rows; the added 158 go by kind
KINDS_V02 = [('inherited root word', 212), ('reserve root', 371), ('suffixed', 1548), ('na-', 178),
             ('compound', 219), ('construct or set phrase', 225), ('grammar form', 65), ('suffix', 19),
             ('loan', 17), ('other', 3)]
assert sum(v for _, v in KINDS_V02) == 2857
KINDS = dict(KINDS_V02)
KINDS['suffixed'] += ADDED_KINDS['suffixed']
KINDS['na-'] += ADDED_KINDS['na-']
KINDS['compound'] += ADDED_KINDS['compound']
KINDS['construct or set phrase'] += ADDED_KINDS['phrase']
assert sum(KINDS.values()) == N


def dry_of_added(r):
    d = r['dry_cut']
    if d.startswith('(not cut') or d.startswith('left out'):
        return 'not cut'
    toks = [t for t in re.split(r'[\s,|]+', d) if t and t != 'letters:']
    signs = [t for t in toks if '@' in t]
    nums = [t for t in toks if t.startswith('%')]
    if d.strip() == '!':
        return 'turned stone'
    if not signs and not nums:
        return 'letters'
    if not signs:
        return 'numeral letters'
    if len(toks) == 1:
        return 'one sign'
    return 'stones'


ADDED_DRY = {}
for r in ADDED:
    k = dry_of_added(r)
    ADDED_DRY[k] = ADDED_DRY.get(k, 0) + 1


# ---------------------------------------------------------------- HTML
def field_table():
    out = ['<div class="tw"><table><tr><th>Field</th><th>Entries</th><th>Canon</th><th>Reserve</th>'
           '<th>Made for the Book</th><th>Made by rule</th><th>Shown below</th></tr>']
    tot = {s: 0 for s in SRC_ORDER}
    shown_tot = 0
    for k, lab in FIELDS:
        rs = GROUPS.get(k, [])
        c = src_counts(rs)
        for s in SRC_ORDER:
            tot[s] += c[s]
        sh = len(SELECTION[k])
        shown_tot += sh
        out.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                   % (html.escape(lab), fmt(len(rs)), fmt(c['canon']), fmt(c['reserve']), fmt(c['tier3']),
                      fmt(c['tier3-sys']), sh))
    out.append('<tr><td><strong>all</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td>'
               '<td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td>'
               '<td><strong>%s</strong></td></tr>'
               % (fmt(N), fmt(tot['canon']), fmt(tot['reserve']), fmt(tot['tier3']), fmt(tot['tier3-sys']), fmt(shown_tot)))
    out.append('</table></div>')
    assert sum(len(v) for v in GROUPS.values()) == N
    return '\n'.join(out)


def per_field_n(k, rows):
    if k == 'affix':
        return len(rows)
    return min(len(rows), max(12, round(len(rows) * 0.07)))


SELECTION = {k: pick(GROUPS.get(k, []), per_field_n(k, GROUPS.get(k, []))) for k, _ in FIELDS}


def selection_html():
    out = []
    for k, lab in FIELDS:
        rs = GROUPS.get(k, [])
        sel = SELECTION[k]
        body = [HEAD] + [row_html(r) for r in sel] + ['</table></div>']
        out.append('<details class="lex"><summary>%s <span class="n">%d of %s</span></summary>%s</details>'
                   % (html.escape(lab), len(sel), fmt(len(rs)), '\n'.join(body)))
    return '\n'.join(out)


def added_html():
    body = [HEAD] + [row_html(r) for r in ADDED] + ['</table></div>']
    return ('<details class="lex" id="t3-added"><summary>Added in translation: the pilots’ 23 and the merge’s 135 '
            '<span class="n">%d, whole</span></summary>%s</details>' % (len(ADDED), '\n'.join(body)))


if __name__ == '__main__':
    print('N', N, SRC, 'logo', LOGO, 'v02 logo', LOGO_V02)
    print('fields', {k: len(v) for k, v in GROUPS.items()})
    print('selection', {k: len(v) for k, v in SELECTION.items()}, sum(len(v) for v in SELECTION.values()))
    print('added kinds', ADDED_KINDS, 'dry', ADDED_DRY)
    print('touched', len(TOUCHED), [r['orrowen'] for r in TOUCHED])
    h = field_table() + selection_html() + added_html()
    print('html bytes', len(h.encode('utf-8')))
    for r in ADDED[:3] + MERGE[10:13]:
        print(clean_deriv(r))
