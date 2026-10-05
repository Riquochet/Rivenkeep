"""Static check of every romanised line (p.il) on a built page: each word an <i> with a non-empty <small> gloss,
no bare letters outside the word boxes, the screen-reader list matching the words."""
import re, sys, html, collections
P = sys.argv[1]
s = open(P, encoding='utf-8').read()
s = re.sub(r'<svg.*?</svg>', '<svg/>', s, flags=re.S)
lines = re.findall(r'<p class="il">(.*?)</p>', s, re.S)
print('p.il lines', len(lines))
st = collections.Counter(); bad = []
WORD = re.compile(r"[A-Za-zÀ-ÿĀ-žḀ-ỿ]")
for L in lines:
    ws = re.findall(r'<i(?: class="blot")?>(.*?)<small aria-hidden="true">(.*?)</small></i>', L, re.S)
    st['words'] += len(ws)
    st['blot boxes'] += len(re.findall(r'<i class="blot">', L))
    st['marks in span.m'] += len(re.findall(r'<span class="m">', L))
    n_i = len(re.findall(r'<i(?: class="blot")?>', L))
    if n_i != len(ws):
        bad.append(('i without small', L[:160]))
    for w, g in ws:
        if not html.unescape(re.sub('<[^>]+>', '', g)).strip():
            bad.append(('empty gloss', w))
        if not WORD.search(html.unescape(re.sub('<[^>]+>', '', w))):
            st['word-box without letters (the blots)'] += 1
    rest = re.sub(r'<i(?: class="blot")?>.*?</small></i>', ' ', L, flags=re.S)
    rest = re.sub(r'<span class="sr">.*?</span>', ' ', rest, flags=re.S)
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', rest))
    if WORD.search(txt):
        bad.append(('bare letters outside a word box', txt.strip()[:120], L[:200]))
    sr = re.search(r'<span class="sr">Word by word: (.*?)\.</span>', L, re.S)
    if ws:
        if not sr:
            bad.append(('no sr list', L[:120]))
        else:
            # glosses may contain commas? compare joined text instead
            joined = ', '.join('a name blotted out' if g == '(name blotted out)' else html.unescape(g) for _, g in ws)
            if html.unescape(sr.group(1)) != joined:
                bad.append(('sr list differs', sr.group(1)[:100], joined[:100]))
    else:
        st['lines without words'] += 1
        bad.append(('line without words', html.unescape(re.sub('<[^>]+>', '', L))[:120]))
print(dict(st))
for b in bad[:40]:
    print(b)
print('problems', len(bad))
# glosses: distribution of lengths, longest ones
gl = collections.Counter()
for L in lines:
    for w, g in re.findall(r'<i>(.*?)<small aria-hidden="true">(.*?)</small></i>', L, re.S):
        gl[html.unescape(g)] += 1
longest = sorted(gl, key=len, reverse=True)[:15]
print('longest glosses', longest)
print('distinct glosses', len(gl))
odd = [g for g in gl if re.search(r'[?<>{}\[\]_]|\bTODO\b|\?\?', g)]
print('odd glosses', odd[:30])
