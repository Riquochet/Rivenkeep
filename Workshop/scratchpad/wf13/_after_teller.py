import re,sys
sys.argv=['x']
exec(open('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/_cmp_plain_forms.py').read().split("for uid in a:")[0])
bb = None
h = open(S + '/wf13/out/Rivenkeep_Legends.html', encoding='utf-8').read()
def pane(uid, k):
    i = h.find('id="%s"' % uid) if not uid in ('foreword','invocation') else h.find('<section id="%s"' % uid)
    j = h.find('<div class="pane p-%s"' % k, i); e = h.find('<div class="pane p-', j + 10)
    return h[j:e]
for uid in [u for u in b if not u.endswith(':frame')]:
    for k in ('book', 'plain'):
        p = pane(uid, k)
        m = re.search(r'<p class="teller"[^>]*>.*?</p>\s*(<[a-z0-9]+[^>]*>)', p, re.S)
        print(uid, k, m.group(1)[:60] if m else None)
