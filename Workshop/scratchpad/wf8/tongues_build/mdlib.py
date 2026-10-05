"""Small markdown helpers for the Tongues doc builder, v0.2.0 (scratchpad only; never goes into Docs/)."""
import html
import re

SP = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
W = SP + '/wf6'
W7 = SP + '/wf7'


def load(name):
    """Load a markdown file as lines: a bare name is under wf6/, 'w7:name' under wf7/, or an absolute path."""
    if name.startswith('w7:'):
        p = W7 + '/' + name[3:]
    elif name.startswith('/'):
        p = name
    else:
        p = W + '/' + name
    with open(p, encoding='utf-8') as f:
        return f.read().split('\n')


def inline(s):
    """Markdown inline -> HTML: code spans, *** ** *, ~~ ~~, links. Escapes HTML."""
    codes = []

    def keep(m):
        codes.append('<code>' + html.escape(m.group(1), quote=False) + '</code>')
        return '\x00%d\x00' % (len(codes) - 1)
    s = re.sub(r'`([^`]+)`', keep, s)
    s = s.replace('\\*', '\x01')
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.+?)\*([^*]+)\*\*\*', r'<strong>\1<em>\2</em></strong>', s)
    s = re.sub(r'\*\*\*([^*]+?)\*([^*]+?)\*\*', r'<strong><em>\1</em>\2</strong>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*\\])\*(?!\s)(.+?)(?<![\s\\])\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(?<![\w*\\])\*([^*\s]+)\*(?=\w)', r'<em>\1</em>', s)
    s = s.replace('\x01', '*')
    s = re.sub(r'~~(.+?)~~', r'<del>\1</del>', s)
    s = re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m.group(1))], s)
    return s


def split_row(line):
    """Split a markdown table row on | outside backticks (and not on an escaped \\|)."""
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|') and not line.endswith('\\|'):
        line = line[:-1]
    cells, cur, inc = [], '', False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '\\' and i + 1 < len(line) and line[i + 1] == '|':
            cur += '|'
            i += 2
            continue
        if ch == '`':
            inc = not inc
        if ch == '|' and not inc:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def tables_after(lines, start):
    """(header, rows, index) for each table from line index start until the next heading."""
    i = start
    out = []
    while i < len(lines):
        l = lines[i]
        if i > start and re.match(r'^#{1,3} ', l):
            break
        if l.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i + 1]):
            head = split_row(l)
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                if not re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[j]):
                    rows.append(split_row(lines[j]))
                j += 1
            out.append((head, rows, i))
            i = j
            continue
        i += 1
    return out


def find(lines, pat, after=0):
    for i in range(after, len(lines)):
        if re.search(pat, lines[i]):
            return i
    raise KeyError(pat)


def table(lines, heading_pat, n=0, cols=None, fix=None, cls=None, head=None, after=0, rows_filter=None):
    """Render the n-th table under the first line matching heading_pat as HTML."""
    i = find(lines, heading_pat, after)
    ts = tables_after(lines, i)
    h, rows, _ = ts[n]
    if rows_filter:
        rows = [r for r in rows if rows_filter(r)]
    return render(h, rows, cols=cols, fix=fix, cls=cls, head=head)


def post(s):
    """Status tags in the specs, turned into the doc's small tags (after inline())."""
    s = re.sub(r'<strong>\[Jack\]</strong>', '<span class="kv jack">Jack</span>', s)
    s = s.replace('[Jack]', '<span class="kv jack">Jack</span>')
    s = re.sub(r'\s*\[(?:call|rule|canon)[^\]]*\]', '', s)
    s = s.replace('[v1]', '<span class="kv">v1</span>')
    return s


def render(h, rows, cols=None, fix=None, cls=None, head=None):
    if cols is not None:
        h = [h[c] for c in cols]
        rows = [[r[c] if c < len(r) else '' for c in cols] for r in rows]
    if head is not None:
        h = head
    f = fix or (lambda s: s)
    out = ['<div class="tw"><table%s>' % (' class="%s"' % cls if cls else '')]
    out.append('<tr>' + ''.join('<th>%s</th>' % post(inline(f(c))) for c in h) + '</tr>')
    for r in rows:
        out.append('<tr>' + ''.join('<td>%s</td>' % post(inline(f(c))) for c in r) + '</tr>')
    out.append('</table></div>')
    return '\n'.join(out)


def strip_refs(s):
    s = re.sub(r'\s*\((?:see )?§[\d.a-z]+(?:[,;–-]\s*§?[\w.]+)*\)', '', s)
    s = re.sub(r'[:,;]?\s*see §\w+ of the spec', '', s)
    s = re.sub(r'\s*\((?:was Hal [^,)]+), shoreland §[\d.]+\)', lambda m: ' (' + m.group(0).strip()[1:].split(',')[0] + ' in v0.1)', s)
    s = re.sub(r',\s*§[\d.]+[a-z]?(?=\))', '', s)
    s = re.sub(r'\s*\[call §[\d.]+\]', ' [Jack]', s)
    s = re.sub(r'\s*\((?:craft|inventory) §[^)]*\)', '', s)
    return s


# The wf7 specs cite one another and their scratch files; the doc keeps the substance and drops the plumbing.
TOOLS = [
    (r'(?:wf7/)?orr_analyze\.py', 'the analyzer'), (r'(?:wf7/)?grain_validate\.py', 'the grain validator'),
    (r'(?:wf7/)?(?:lex/)?build_lexicon\.py', 'the lexicon builder'), (r'(?:wf7/)?lexicon_orrowen\.tsv', 'the lexicon'),
    (r'(?:wf7/)?render_grain2\.py', 'the grain renderer'), (r'(?:wf7/)?render_chisel\.py', 'the dry-cut renderer'),
    (r'(?:wf6/)?render_shore\.py', 'the course-hand renderer'), (r'(?:wf7/)?to_ink\.py', 'the ink converter'),
    (r'(?:wf7/orrowen/)?leafhand\.py', 'the leaf-hand renderer'), (r'(?:wf7/orrowen/)?wordstones\.py', 'the word-sign builder'),
    (r'(?:wf7/)?coverage/concepts\.tsv', 'the concept register'), (r'(?:wf7/)?coverage/register\.md', 'the concept register'),
    (r'(?:wf7/)?pilot_I1\.md', 'the I.1 pilot'), (r'(?:wf7/)?pilot_IV4\.md', 'the IV.4 pilot'),
    (r'(?:wf7/)?orrowen_v2(?:\.md)?', 'the Orrowen spec'), (r'(?:wf7/)?grain_v2(?:\.md)?', 'the grain v2 spec'),
    (r'(?:wf6/)?mystaeri_spec(?:\.md)?', 'the Seilrhass spec'), (r'(?:wf7/)?ancestor\.md', 'the First Tongue spec'),
    (r'(?:wf6/)?legends_v12\.md', 'the Book'), (r'(?:wf7/)?lexicon_orrowen\.md', 'the lexicon summary'),
    (r'(?:wf7/)?backtrans_I1\.md', 'the I.1 back-translation'), (r'(?:wf7/)?backtrans_IV4\.md', 'the IV.4 back-translation'),
    (r'(?:wf7/)?proto_v3\.py', 'the prototype'), (r'(?:wf7/grain2/)?gn2\.py', 'the notation printer'),
    (r'(?:wf6/)?shoreland_spec(?:\.md)?', 'the Shoreland spec'),
]
EXT = r'(?:md|py|json|tsv|txt|gn2|svg|png|html)'


def strip_files(s):
    for pat, name in TOOLS:
        s = re.sub(r'`' + pat + r'(\s[^`]*)?`', lambda m: name + ((' (`' + m.group(1).strip() + '`)') if m.group(1) else ''), s)
        s = re.sub(r'(?<![\w/])' + pat + r'\b', name, s)
    # a parenthetical that only points at a scratch file or folder
    s = re.sub(r'\s*\([^()]*`[^`]*(?:wf[67]/|/|\.' + EXT + r'\b)[^`]*`[^()]*\)', '', s)
    # any other code span that is a path
    s = re.sub(r'`[^`]*(?:wf[67]/|\.' + EXT + r'\b|/)[^`]*`', '', s)
    s = re.sub(r'\s*\((?:(?:v1|wf6|v2|the (?:Shoreland|Seilrhass|Orrowen|First Tongue|grain v2) spec)\s*)§[\w.,–\- ]+\)', '', s)
    s = re.sub(r'\(\s*\)', '', s)
    s = re.sub(r'[ \t]{2,}', ' ', s)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return s.strip()


def fixall(s):
    return strip_files(strip_refs(s))
