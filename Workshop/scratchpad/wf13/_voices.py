import re
h = open('/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13/out/Rivenkeep_Legends.html', encoding='utf-8').read()
def pane(uid, k):
    i = h.find('id="%s"' % uid)
    j = h.find('<div class="pane p-%s"' % k, i); e = h.find('<div class="pane p-', j + 10)
    return h[j:e]
for uid in ('t-IV-1', 't-epilogue'):
    for k in ('book', 'plain'):
        p = pane(uid, k)
        ps = re.findall(r'<p\b([^>]*)>(.*?)</p>', p, re.S)
        for i, (a, t) in enumerate(ps):
            if 'data-voice' in a:
                for j in range(max(0, i-1), i+1):
                    print(uid, k, ps[j][0].strip()[:50], '|', re.sub(r'<[^>]+>', '', ps[j][1])[:150])
