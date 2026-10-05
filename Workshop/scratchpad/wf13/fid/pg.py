"""fidelity helpers: split a story page into its panes (independent of the builder/checker)."""
import re, html as H

V30 = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/out/Rivenkeep_Legends.html'
V31 = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/out/Rivenkeep_Legends.html'
TAG = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>')
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr'}

def element(s, start):
    """end index of the element whose start tag begins at s[start] (same-name nesting; skips <script>/<style> bodies)"""
    m = TAG.match(s, start)
    name = m.group(2).lower()
    depth = 0
    pos = start
    rx = re.compile(r'<(/?)%s\b[^>]*?(/?)>' % name, re.I)
    for mm in rx.finditer(s, start):
        if mm.group(1):
            depth -= 1
        elif not mm.group(2):
            depth += 1
        if depth == 0:
            return mm.end()
    raise ValueError('unclosed %s at %d' % (name, start))

def panes(h):
    """[(kind, start, end, html)] for every div.pane in page order"""
    out = []
    for m in re.finditer(r'<div class="pane p-(book|plain|orig)"', h):
        e = element(h, m.start())
        out.append((m.group(1), m.start(), e, h[m.start():e]))
    return out

def strip_panes(h, kinds=('plain', 'orig')):
    """the page with the panes of the given kinds cut out (left as a marker)"""
    ps = [p for p in panes(h) if p[0] in kinds]
    out, last = [], 0
    for k, s, e, _ in ps:
        out.append(h[last:s]); out.append('<!--PANE %s-->' % k); last = e
    out.append(h[last:])
    return ''.join(out)

def text(fr):
    fr = re.sub(r'<(script|style)\b.*?</\1>', ' ', fr, flags=re.S)
    fr = re.sub(r'<svg\b.*?</svg>', ' ', fr, flags=re.S)
    fr = re.sub(r'<[^>]+>', ' ', fr)
    return re.sub(r'\s+', ' ', H.unescape(fr)).strip()
