"""compare the Plain Words panes' forms, leaf by leaf, between the v3.0.0 page (wf12) and the v3.1.0 page (wf13)"""
import re, sys, collections
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
sys.path.insert(0, S + '/wf13/book')
def panes(path):
    h = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<(article|div) class="([^"]*\bsw\b[^"]*)"([^>]*)>', h):
        idm = re.search(r'\bid="([^"]+)"', m.group(0))
        uid = idm.group(1) if idm else re.findall(r'<section id="([^"]+)"', h[:m.start()])[-1] + ('' if 'leaf' in m.group(2) else ':frame')
        j = h.find('<div class="pane p-plain"', m.start())
        k = h.find('<div class="pane p-orig"', j)
        out[uid] = h[j:k]
    return out
def forms(p):
    c = collections.Counter()
    for tag, cls in re.findall(r'<(p|h4|div|blockquote|figure|aside|table|tr)\b(?: class="([^"]*)")?', p):
        c['%s.%s' % (tag, cls or '')] += 1
    c['voice a'] = len(re.findall(r'data-voice="a"', p)); c['voice b'] = len(re.findall(r'data-voice="b"', p))
    c['wood'] = len(re.findall(r'class="[^"]*\bwood\b', p)); c['pair'] = p.count('<span class="pair">')
    c['data-m'] = len(re.findall(r'data-m=', p))
    return c
a = panes(S + '/wf12/out/Rivenkeep_Legends.html'); b = panes(S + '/wf13/out/Rivenkeep_Legends.html')
for uid in a:
    fa, fb = forms(a[uid]), forms(b.get(uid, ''))
    d = {k: (fa.get(k, 0), fb.get(k, 0)) for k in set(fa) | set(fb) if fa.get(k, 0) != fb.get(k, 0) and k not in ('p.', 'p.first', 'pair', 'data-m')}
    if d:
        print(uid, sorted(d.items()))

print('--- Book pane vs Plain v3.1 pane (v3.1.0 page)')
def bpanes(path):
    h = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<(article|div) class="([^"]*\bsw\b[^"]*)"([^>]*)>', h):
        idm = re.search(r'\bid="([^"]+)"', m.group(0))
        uid = idm.group(1) if idm else re.findall(r'<section id="([^"]+)"', h[:m.start()])[-1] + ('' if 'leaf' in m.group(2) else ':frame')
        j = h.find('<div class="pane p-book"', m.start())
        k = h.find('<div class="pane p-plain"', j)
        out[uid] = h[j:k]
    return out
bb = bpanes(S + '/wf13/out/Rivenkeep_Legends.html')
for uid in bb:
    fa, fb = forms(bb[uid]), forms(b.get(uid, ''))
    d = {k: (fa.get(k, 0), fb.get(k, 0)) for k in set(fa) | set(fb) if fa.get(k, 0) != fb.get(k, 0) and k not in ('p.', 'p.first', 'pair', 'data-m')}
    if d:
        print(uid, sorted(d.items()))
for uid in ('t-II-2', 't-II-3', 't-III-1', 't-III-2', 't-IV-3', 't-IV-4'):
    print('==', uid)
    for x in re.findall(r'<p class="inscr[^"]*"[^>]*>(.*?)</p>', b[uid]):
        print('   P31', re.sub(r'<[^>]+>', '', x)[:150])
    for x in re.findall(r'<p class="inscr[^"]*"[^>]*>(.*?)</p>', bb[uid]):
        print('   BK ', re.sub(r'<[^>]+>', '', x)[:150])
