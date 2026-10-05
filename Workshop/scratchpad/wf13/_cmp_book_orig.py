"""v3.1.0 vs v3.0.0: the Book panes byte for byte; the Original panes byte for byte once the romanisation folds'
lines are read back to their v3.0.0 form (<p><em>line</em></p>); the frame outside the panes"""
import re, html
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
a = open(S + '/wf12/out/Rivenkeep_Legends.html', encoding='utf-8').read()
b = open(S + '/wf13/out/Rivenkeep_Legends.html', encoding='utf-8').read()
def split(h):
    out = []
    for m in re.finditer(r'<div class="pane p-(book|plain|orig)"[^>]*>', h):
        out.append((m.group(1), m.start()))
    return out
def element(s, start):
    depth = 0
    for m in re.compile(r'<(/?)div\b[^>]*?>').finditer(s, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return s[start:m.end()]
def panes(h):
    return [(k, element(h, i)) for k, i in split(h)]
pa, pb = panes(a), panes(b)
assert [k for k, _ in pa] == [k for k, _ in pb]
def unil(x):
    def one(m):
        inner = m.group(1)
        inner = re.sub(r' <span class="sr">.*?</span>$', '', inner)
        inner = re.sub(r'<small aria-hidden="true">.*?</small>', '', inner)
        inner = re.sub(r'</?i>', '', inner)
        return '<p><em>%s</em></p>' % inner
    return re.sub(r'<p class="il">(.*?)</p>', one, x)
diff = {'book': 0, 'orig': 0}
for (k, x), (_, y) in zip(pa, pb):
    if k == 'book' and x != y:
        diff['book'] += 1
    if k == 'orig' and x != unil(y):
        diff['orig'] += 1
        if diff['orig'] < 3:
            import difflib
            sm = difflib.SequenceMatcher(None, x, unil(y), autojunk=False)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op != 'equal':
                    print(op, repr(x[i1-80:i2+80]), '\n   ', repr(unil(y)[j1-80:j2+80])); break
print('panes', len(pa), 'differ:', diff)
# outside the panes
def strip_panes(h):
    out, pos = [], 0
    for k, i in split(h):
        e = element(h, i)
        out.append(h[pos:i]); pos = i + len(e)
    out.append(h[pos:])
    return ''.join(out)
oa, ob = strip_panes(a), strip_panes(b)
la = re.split(r'(?<=>)', oa); lb = re.split(r'(?<=>)', ob)
import difflib
n = 0
for l in difflib.unified_diff(la, lb, n=0, lineterm=''):
    if l.startswith(('---', '+++', '@@')): continue
    n += 1
    if n <= 40: print('FRAME', l[:240].replace('\n', ' '))
print('frame diff lines', n)
