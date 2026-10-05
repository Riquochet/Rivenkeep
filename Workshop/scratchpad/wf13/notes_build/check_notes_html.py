#!/usr/bin/env python3
"""check_notes_html.py - structural checks on wf13/out/Rivenkeep_Legends_Notes.html (Notes v1.2.0; wf13 scratch).

    python3 check_notes_html.py [--doc-version "v1.2.0"]

Against the composed markdown the builder wrote (notes_build/notes_v3_composed.md: wf11/notes_v3.md with sections
1.15 and 1.16 and their pointers).  The story page's anchors are checked against wf13/out/Rivenkeep_Legends.html
(the v3.1.0 page) when it is there.  Exit 1 on any problem.
"""
import argparse
import collections
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(HERE)
PAGE = os.path.join(W, 'out', 'Rivenkeep_Legends_Notes.html')
SRC = os.path.join(HERE, 'notes_v3_composed.md')
PANES = os.path.join(W, 'orig', 'panes.json')          # the v3 story page's anchors, as its builder keys them
DOCS = '/Users/riquochet/code/Rivenkeep/Docs'
_ap = argparse.ArgumentParser()
_ap.add_argument('--doc-version', default='v1.2.0')
VERSION = _ap.parse_args().doc_version
VOID = {'meta', 'link', 'br', 'hr', 'img', 'input', 'col', 'area', 'base', 'wbr', 'source'}
# what each block may directly contain (a light content-model check)
NO_BLOCK_IN = {'p', 'h1', 'h2', 'h3', 'h4', 'th', 'a', 'strong', 'em', 'code', 'span'}
BLOCKS = {'div', 'p', 'ul', 'ol', 'table', 'section', 'h2', 'h3', 'h4', 'header', 'nav', 'footer', 'blockquote'}

problems = []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.hrefs, self.text, self.code = [], [], [], [], []
        self.tags = collections.Counter()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] += 1
        if tag == 'script':
            problems.append('script tag')
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'a':
            self.hrefs.append(a.get('href', ''))
            if 'a' in self.stack:
                problems.append('nested <a> at %s' % (self.getpos(),))
        if tag in BLOCKS and self.stack and self.stack[-1] in NO_BLOCK_IN:
            problems.append('block <%s> inside <%s> at %s' % (tag, self.stack[-1], self.getpos()))
        if tag == 'li' and self.stack and self.stack[-1] not in ('ul', 'ol'):
            problems.append('li outside list at %s' % (self.getpos(),))
        if tag in ('tr',) and self.stack and self.stack[-1] != 'table':
            problems.append('tr outside table')
        if tag in BLOCKS or tag in ('li', 'td', 'th', 'br', 'tr'):
            self.text.append(' ')
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            problems.append('mismatched </%s> (open: %s) at %s' % (tag, self.stack[-3:], self.getpos()))
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                self.stack.pop()
            return
        self.stack.pop()

    def handle_data(self, d):
        if self.stack and self.stack[-1] in ('style', 'title'):
            return
        if 'code' in self.stack:
            self.code.append(d)
            d = ' CODE '
        self.text.append(d)


s = open(PAGE, encoding='utf-8').read()
md = open(SRC, encoding='utf-8').read()
p = P()
p.feed(s)
p.close()
if p.stack:
    problems.append('unclosed: %s' % p.stack)
dups = [k for k, v in collections.Counter(p.ids).items() if v > 1]
if dups:
    problems.append('duplicate ids: %s' % dups)
ids = set(p.ids)
internal = [h for h in p.hrefs if h.startswith('#')]
bad = sorted({h for h in internal if h[1:] not in ids})
if bad:
    problems.append('unresolved internal anchors: %s' % bad)

# the house sheet, at this version
if s.count('--doc-version:"%s"' % VERSION) != 1 or s.count('--doc-version:"') != 1:
    problems.append('doc-version is not %s' % VERSION)

# every heading, note, death and call of the markdown has its id
want = {'about', 'contents', 'glance', 'changed-v3', 'changed-v2', 'reckoning', 'puzzle', 'game', 'names', 'calls',
        'history'}
want |= {'s' + n.replace('.', '-') for n in re.findall(r'^### (\d+\.\d+) ', md, re.M)}
want |= {'k%d' % k for k in range(1, 10)} | {'j%d' % k for k in range(1, 27)} | {'d%d' % k for k in range(1, 13)}
calls = re.search(r'^### 7\.2 .*?\n(.*?)^### 7\.3', md, re.M | re.S).group(1)
ncalls = len(re.findall(r'^(\d+)\. ', calls, re.M))
want |= {'call-%d' % k for k in range(1, ncalls + 1)}
missing = sorted(want - ids)
if missing:
    problems.append('ids missing: %s' % missing)
n_h3_md = len(re.findall(r'^### ', md, re.M))
n_h3 = len(re.findall(r'<h3 id="s\d', s))
if n_h3 != n_h3_md:
    problems.append('sub-sections: md %d, page %d' % (n_h3_md, n_h3))
n_tab_md = len(re.findall(r'(?:^|\n\n)\|', md))
n_tab = p.tags['table']
if n_tab != n_tab_md:
    problems.append('tables: md %d, page %d' % (n_tab_md, n_tab))
n_bq_md = len(re.findall(r'(?:^|\n\n) *>', md)) - 1          # the front's references note is a box, not a quote
if p.tags['blockquote'] != n_bq_md:
    problems.append('block quotes: md %d, page %d' % (n_bq_md, p.tags['blockquote']))

text = ''.join(p.text)
for pat, what in [(r'\*\*', '** left'), (r'(?<![\w])\*(?=\w)', '* left'), (r'`', 'backtick left'),
                  (r'\]\(', 'md link left'), (r'\{\{', '{{ left'), (r'/private/|/tmp/|scratchpad', 'scratch path'),
                  (r'"', 'straight double quote'), (r"'", 'straight apostrophe'), (r'(?:^|\s)>\s', 'quote marker left'),
                  (r'\x00', 'placeholder left')]:
    hits = re.findall(r'.{0,30}' + pat + r'.{0,30}', text)
    if hits:
        problems.append('%s x%d, e.g. %r' % (what, len(hits), hits[:3]))
if re.search(r'<table class="(?:mid|red|full|dim)"', s):
    problems.append('a table carries a house colour class (mid, red, full, dim)')
if '<script' in s.lower():
    problems.append('script')

# no section mark of another document links into this one (voice §4, craft §2.1, its §12.2, a file's §4 ...)
for m in re.finditer(r'(voice|craft|R6b|outline|MAP|its|v1\.3|v1\.0\.0|</code>) <a href="#[^"]+">§', s):
    problems.append('another document\'s section linked here: %r' % s[m.start():m.end() + 12])

# external links: other docs and their anchors
ext = collections.Counter(h for h in p.hrefs if not h.startswith('#'))
docs_ok = {}
for h in sorted(ext):
    if h.startswith('http'):
        continue
    f, _, frag = h.partition('#')
    if f == 'Rivenkeep_Legends.html':
        continue          # the story page is built beside this one; its anchors are checked below
    path = os.path.join(DOCS, f)
    if not os.path.exists(path):
        problems.append('missing doc %s' % f)
        continue
    if frag:
        body = docs_ok.setdefault(f, open(path, encoding='utf-8').read())
        if 'id="%s"' % frag not in body:
            problems.append('anchor %s not in %s' % (frag, f))

book = collections.Counter(h.partition('#')[2] for h in p.hrefs if h.startswith('Rivenkeep_Legends.html'))
story = os.path.join(W, 'out', 'Rivenkeep_Legends.html')
if os.path.exists(story):
    sb = open(story, encoding='utf-8').read()
    missing = [a for a in book if a and 'id="%s"' % a not in sb]
    if missing:
        problems.append('story-page anchors not found in out/Rivenkeep_Legends.html: %s' % missing)
    print('checked story anchors against', story)
else:
    anchors = set(json.load(open(PANES, encoding='utf-8')))
    missing = [a for a in book if a and a not in anchors]
    if missing:
        problems.append('story-page anchors not among the v3 anchors (panes.json): %s' % missing)
    print('story page not built in wf13/out; anchors checked against the v3 anchor set in', PANES)

print('links into the Book by anchor:', dict(sorted(book.items())))
print('other links:', {k: v for k, v in sorted(ext.items()) if not k.startswith('Rivenkeep_Legends.html')})
print('ids:', len(ids), ' internal hrefs:', len(internal), ' calls:', ncalls, ' h3:', n_h3, ' tables:', n_tab,
      ' quotes:', p.tags['blockquote'], ' boxes:', len(re.findall(r'<div class="s[ "]', s)))

# word parity: every word of the markdown (minus markup) appears in the page text, roughly as often
md_words = re.findall(r"[A-Za-z][A-Za-z’'-]+", md.replace("'", '’'))
pg_words = re.findall(r"[A-Za-z][A-Za-z’'-]+", text)
c_md, c_pg = collections.Counter(md_words), collections.Counter(pg_words)
lost = {w: c_md[w] - c_pg[w] for w in c_md if c_md[w] > c_pg[w]}
print('words: md %d page %d; words short in page: %s' % (len(md_words), len(pg_words),
                                                        dict(sorted(lost.items(), key=lambda x: -x[1])[:25])))
print('PROBLEMS:' if problems else 'OK: no problems', *problems, sep='\n  ')
sys.exit(1 if problems else 0)
