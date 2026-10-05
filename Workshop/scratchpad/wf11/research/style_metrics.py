#!/usr/bin/env python3
"""Style metrics for the Legends of Rivenkeep: v1.3 Book, v2.0 Book, Modern v1.2 (old Plain Words), Plain v2.0.

Usage: python3 style_metrics.py            -> prints corpus tables + per-tale tables
Writes: style_metrics_out.txt and style_metrics.json next to this script.
"""
import re, html, json, statistics, os, sys
from collections import Counter, defaultdict

SP = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
SRC = {
    'v1.3 Book': SP + '/wf7/book/legends_v13.md',
    'v2.0 Book': SP + '/wf10/book_v2.md',
    'Modern v1.2': '/Users/riquochet/code/Rivenkeep/Docs/Archive/Rivenkeep_Legends_Modern_v1.2.html',
    'Plain v2.0': SP + '/wf10/plain_v2.md',
}
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- parsing
def clean_inline(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'\{\{([^}]+)\}\}', r'\1', t)
    t = t.replace('**', '').replace('*', '')
    t = t.replace('’', "'").replace('‘', "'")
    t = t.replace('“', '"').replace('”', '"')
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def norm_title(t):
    t = clean_inline(t).lower()
    t = re.sub(r'^(of )', '', t)
    return t.strip()

def parse_md(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    # strip multi-line HTML comments
    txt = '\n'.join(lines)
    txt = re.sub(r'<!--.*?-->', '', txt, flags=re.S)
    lines = txt.split('\n')
    tales = []
    cur = None
    i = 0
    stop_at = re.compile(r'^(# |## |### )')
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'^### (?:([IVX]+\.\d+) · )?(.*)$', ln)
        if m and (m.group(1) or 'Stone out of the Grey' in ln):
            if cur: tales.append(cur)
            cur = {'id': m.group(1) or 'Epi', 'title': m.group(2).strip(), 'paras': []}
            i += 1
            continue
        if cur and stop_at.match(ln) and not ln.startswith('### '):
            tales.append(cur); cur = None
            # stop collecting after appendix / game sections
            i += 1
            continue
        if cur and ln.startswith('### '):
            tales.append(cur); cur = None
            i += 1
            continue
        if cur is None:
            i += 1; continue
        # gather paragraph blocks
        if ln.strip() == '' or ln.strip() == '---':
            i += 1; continue
        if ln.lstrip('> ').startswith('::: native'):
            # skip native block
            i += 1
            while i < len(lines) and lines[i].lstrip('> ').strip() != ':::':
                i += 1
            i += 1
            continue
        block = [ln]
        i += 1
        while i < len(lines) and lines[i].strip() != '' and not lines[i].lstrip('> ').startswith('::: native') and not stop_at.match(lines[i]):
            if lines[i].startswith('>') != ln.startswith('>'):
                break
            block.append(lines[i]); i += 1
        raw = '\n'.join(block)
        if raw.startswith('>'):
            inner = re.sub(r'^> ?', '', raw, flags=re.M).strip()
            kind = 'song' if inner.startswith('*') and inner.count('\n') >= 1 else 'blockquote'
            cur['paras'].append((kind, raw))
            continue
        s = raw.strip()
        if s.startswith('**Part') or s.startswith('**') and s.endswith('**') and len(s) < 80:
            cur['paras'].append(('subhead', raw)); continue
        if s.startswith('*') and s.endswith('*') and not s.startswith('**'):
            cur['paras'].append(('italic', raw)); continue
        if s.startswith('***'):
            cur['paras'].append(('italic', raw)); continue
        cur['paras'].append(('prose', raw))
    if cur: tales.append(cur)
    # classify leading italics as headnote
    for t in tales:
        head, body, frame, songs = [], [], [], []
        seen_prose = False
        for kind, raw in t['paras']:
            if kind == 'italic' and not seen_prose:
                head.append(raw)
            elif kind == 'prose':
                seen_prose = True
                c = clean_inline(raw)
                if c.startswith('IN MEMORY OF OUR HOME'):
                    frame.append(raw)
                else:
                    body.append(raw)
            elif kind == 'song':
                songs.append(raw)
            else:
                frame.append(raw)
        t['head'] = [clean_inline(h) for h in head]
        t['body'] = [clean_inline(b) for b in body]
        t['frame'] = [clean_inline(f) for f in frame]
        t['songs'] = songs
    return [t for t in tales if t['body']]

def parse_html(path):
    s = open(path, encoding='utf-8').read()
    tales = []
    for am in re.finditer(r'<article class="tale[^"]*" id="([^"]+)"[^>]*>(.*?)</article>', s, flags=re.S):
        aid, inner = am.group(1), am.group(2)
        tm = re.search(r'<span class="tt">(.*?)</span>', inner)
        title = html.unescape(re.sub(r'<[^>]+>', '', tm.group(1))) if tm else aid
        inner2 = re.sub(r'<figure.*?</figure>', '', inner, flags=re.S)
        inner2 = re.sub(r'<blockquote class="grain">.*?</blockquote>', '', inner2, flags=re.S)
        inner2 = re.sub(r'<svg.*?</svg>', '', inner2, flags=re.S)
        head, body, frame, songs = [], [], [], []
        for pm in re.finditer(r'<p( class="([^"]*)")?[^>]*>(.*?)</p>', inner2, flags=re.S):
            cls = pm.group(2) or ''
            txt = clean_inline(html.unescape(re.sub(r'<[^>]+>', '', pm.group(3))))
            if not txt: continue
            if 'teller' in cls: head.append(txt)
            elif cls in ('', 'first', 'laid', 'marked', 'marked first', 'gloss'): body.append(txt)
            else: frame.append(txt)
        for vm in re.finditer(r'<div class="verse">(.*?)</div>', inner2, flags=re.S):
            songs.append(vm.group(1))
        tid = aid.replace('t-', '').replace('-', '.') if aid != 't-epilogue' else 'Epi'
        tales.append({'id': tid, 'title': title, 'head': head, 'body': body, 'frame': frame, 'songs': songs})
    return tales

# ---------------------------------------------------------------- metrics
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")

def words(t):
    return WORD.findall(t)

def sentences(t):
    t = t.replace('…', ',')  # ellipses inside Guest's speech are not sentence ends
    t = re.sub(r'\s+', ' ', t)
    parts = re.split(r'(?<=[.!?])["\')\]]?\s+(?=["\'(]?[A-Z0-9▒])', t)
    out = []
    for p in parts:
        if len(words(p)) > 0:
            out.append(p)
    return out

ARCHAIC = set('''ere upon unto thee thou thy thine ye hath doth dost shalt wilt nay aye yea whence whither thence
hither thither wherein whereof whereon whereby therein thereof thereto thereon hereafter naught nought betwixt amid amidst
anon morrow oft lest wont verily forsooth bade bidden spake twain yonder alas kine hearken hark beseech wrought nigh
mayhap perchance ofttimes erelong forthwith withal methinks thereafter whereupon howbeit fain sooth wist'''.split())
# grammar-level archaisms (do-less negation, subjunctive be, inversion with nor)
DOLESS = re.compile(r"\b(knew|know|saw|see|came|come|went|go|said|say|spoke|speak|heard|hear|fear|feared|looked|wanted|cared|doubt|stood|gave|took|mended|changed|waited|understood|understand|tell|told|move|moved|answer|answered|think|thought|let|ask|asked|stop|stopped|weep|wept|hurry|hurried|need|needed|lift|lifted|turn|turned|sleep|slept|forget|forgot|remember|remembered|find|found) not\b", re.I)
SUBJ_BE = re.compile(r"\b(if|though|whether|till|until|lest|unless|ere) ([a-z]+ ){0,3}be\b", re.I)
NOR_INV = re.compile(r"\bnor (did|was|were|had|would|could|will|is|are|do|does|shall|can) \b", re.I)
FRONT_INV = re.compile(r"(^|[.;:] )(Then|So|Thus|Long|Deep|Up|Down|Into|Out of|Over|Under|Through|Of all|Never|Not once|Nor|Well out|Far|Higher|After them|First)\b[^.;:]{0,40}?\b(came|went|stood|lay|answered|did|was|were|had|is|are|goes|go|come|rose|fell|sat|ran)\b (the|a|an|his|her|their|our|my|he|she|they|we|I|it)\b")
# v2.0 tics
TICS = {
    'one-said/other-finished': re.compile(r'one of them (said|began)[^.]{0,30}the other (finished|ended)', re.I),
    'he and she': re.compile(r'\bhe and she\b', re.I),
    'the two of them': re.compile(r'\bthe two of them\b', re.I),
    'his ... and hers': re.compile(r"\bhis [a-z]+ and hers\b|\bhis voice and hers\b|\bhis hand and hers\b|\bhis fingers and hers\b", re.I),
    'epic simile (As when / As a ...: so)': re.compile(r'\bAs when\b|\bAs (a|an) [^.]{20,400}?: so\b'),
    'Picture/Think of (plain simile)': re.compile(r'\b(Picture|Think of|Imagine) (a|an|the|masons|it)\b'),
    'day of the banner': re.compile(r'\bday of the banner\b', re.I),
    'causal ", for "': re.compile(r'[,;] for (?!a while|the first|the last|all|each|every|ever|one|two|three|him|her|them|us|me|you|it\b|this|that\b|good)', re.I),
    'ere': re.compile(r'\bere\b', re.I),
    'rubric opening (Hear how / This is how / Now hear)': re.compile(r'\b(Hear (now )?how|This is how|Now hear|Hear now)\b'),
    'time anchor (nth season/night, years before/after)': re.compile(r'\b(first|second|third|fourth|fifth|sixth|seventh|tenth|fourteenth|fifteenth|twentieth|twenty-\w+)\s+(winter|summer|spring|autumn|month|year|night|day|tide)s?\b|\b(years|winters|nights|days|months) (before|after|ago)\b|\bday of the banner\b', re.I),
    'numbers spelled (counts/dates)': re.compile(r'\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|hundred|hundreds|thousand)\b', re.I),
    'upon': re.compile(r'\bupon\b', re.I),
}
CONTRACTION = re.compile(r"\b\w+'(t|ll|re|ve|d|m)\b|\b(it|that|he|she|there|what|who|here|where|let)'s\b", re.I)

def syllables(w):
    w = w.lower().strip("'-")
    if len(w) <= 3: return 1
    w = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', w)
    w = re.sub(r'^y', '', w)
    n = len(re.findall(r'[aeiouy]{1,2}', w))
    return max(1, n)

def quote_words(paras):
    n = 0
    for p in paras:
        for q in re.findall(r'"([^"]+)"', p):
            n += len(words(q))
    return n

def ngrams(ws, n):
    ws = [w.lower() for w in ws]
    return [tuple(ws[i:i+n]) for i in range(len(ws)-n+1)]

def metrics_for(paras):
    text = ' '.join(paras)
    ws = words(text)
    nW = len(ws)
    sents = [s for p in paras for s in sentences(p)]
    sl = [len(words(s)) for s in sents]
    nS = len(sl) or 1
    pw = [len(words(p)) for p in paras]
    lw = [w.lower() for w in ws]
    arch = sum(1 for w in lw if w in ARCHAIC)
    eth = sum(1 for w in lw if re.match(r"^[a-z]+eth$", w) and w not in ('teeth', 'beneath', 'seth', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth', 'hundredth'))
    gram = len(DOLESS.findall(text)) + len(SUBJ_BE.findall(text)) + len(NOR_INV.findall(text)) + len(FRONT_INV.findall(text))
    syl = sum(syllables(w) for w in ws)
    poly = sum(1 for w in ws if syllables(w) >= 3)
    fk = 0.39 * (nW / nS) + 11.8 * (syl / max(nW, 1)) - 15.59
    m = {
        'words': nW, 'sentences': len(sl), 'paragraphs': len(paras),
        'sent_mean': round(statistics.mean(sl), 1) if sl else 0,
        'sent_median': statistics.median(sl) if sl else 0,
        'sent_p90': sorted(sl)[int(0.9 * (len(sl) - 1))] if sl else 0,
        'sent_max': max(sl) if sl else 0,
        'pct_over30': round(100 * sum(1 for x in sl if x > 30) / nS, 1),
        'pct_over45': round(100 * sum(1 for x in sl if x > 45) / nS, 1),
        'pct_under10': round(100 * sum(1 for x in sl if x < 10) / nS, 1),
        'words_per_para': round(statistics.mean(pw), 1) if pw else 0,
        'semicolons_per_sent': round(text.count(';') / nS, 2),
        'commas_per_sent': round(text.count(',') / nS, 2),
        'and_per_sent': round(sum(1 for w in lw if w == 'and') / nS, 2),
        'archaic_lex_per_1k': round(1000 * (arch + eth) / max(nW, 1), 1),
        'archaic_gram_per_1k': round(1000 * gram / max(nW, 1), 1),
        'contractions_per_1k': round(1000 * len(CONTRACTION.findall(text)) / max(nW, 1), 1),
        'dialogue_share_pct': round(100 * quote_words(paras) / max(nW, 1), 1),
        'fk_grade': round(fk, 1),
        'pct_polysyllabic': round(100 * poly / max(nW, 1), 1),
    }
    for k, rx in TICS.items():
        m['tic:' + k] = round(1000 * len(rx.findall(text)) / max(nW, 1), 2)
    return m, sl

def overlap(book_paras, plain_paras, n=4):
    b = set(ngrams(words(' '.join(book_paras)), n))
    p = ngrams(words(' '.join(plain_paras)), n)
    if not p: return 0.0
    return round(100 * sum(1 for g in p if g in b) / len(p), 1)

# ---------------------------------------------------------------- run
def main():
    data = {}
    for name, path in SRC.items():
        data[name] = parse_html(path) if path.endswith('.html') else parse_md(path)
    out = []
    def P(*a):
        out.append(' '.join(str(x) for x in a))

    P('# Corpus metrics (tale bodies only: no headnotes, songs, native blocks, hearth-answer frames)')
    keys = None
    corpus = {}
    for name, tales in data.items():
        paras = [p for t in tales for p in t['body']]
        m, sl = metrics_for(paras)
        hw = [len(words(' '.join(t['head']))) for t in tales]
        m['tales'] = len(tales)
        m['words_per_tale_mean'] = round(statistics.mean([len(words(' '.join(t['body']))) for t in tales]), 0)
        m['headnote_words_mean'] = round(statistics.mean(hw), 1)
        m['headnote_words_max'] = max(hw)
        m['headnote_share_pct'] = round(100 * sum(hw) / (sum(hw) + m['words']), 1)
        corpus[name] = m
        keys = list(m.keys())
    P('| metric | ' + ' | '.join(corpus.keys()) + ' |')
    P('|---|' + '---|' * len(corpus))
    for k in keys:
        P('| ' + k + ' | ' + ' | '.join(str(corpus[n][k]) for n in corpus) + ' |')

    # sentence-length histogram
    P('\n# Sentence-length distribution (% of sentences per band)')
    bands = [(1, 5), (6, 10), (11, 15), (16, 20), (21, 30), (31, 45), (46, 60), (61, 999)]
    P('| band | ' + ' | '.join(data.keys()) + ' |')
    P('|---|' + '---|' * len(data))
    hists = {}
    for name, tales in data.items():
        paras = [p for t in tales for p in t['body']]
        sl = [len(words(s)) for p in paras for s in sentences(p)]
        hists[name] = [round(100 * sum(1 for x in sl if a <= x <= b) / len(sl), 1) for a, b in bands]
    for i, (a, b) in enumerate(bands):
        P(f'| {a}-{b if b < 999 else "+"} | ' + ' | '.join(str(hists[n][i]) for n in data) + ' |')

    # per-tale
    P('\n# Per-tale: body words / headnote words / mean sentence / %>30 / semicolons per sentence / dialogue %')
    def key(t):
        return norm_title(t['title'])
    bytitle = {n: {key(t): t for t in ts} for n, ts in data.items()}
    order = [key(t) for t in data['v2.0 Book']]
    for k in [key(t) for t in data['v1.3 Book']]:
        if k not in order: order.append(k)
    P('| tale | ' + ' | '.join(data.keys()) + ' |')
    P('|---|' + '---|' * len(data))
    pertale = {}
    for k in order:
        row = []
        for n in data:
            t = bytitle[n].get(k)
            if not t:
                row.append('—'); continue
            m, _ = metrics_for(t['body'])
            hw = len(words(' '.join(t['head'])))
            pertale.setdefault(k, {})[n] = {'id': t['id'], 'body': m['words'], 'head': hw, 'mean': m['sent_mean'], 'o30': m['pct_over30'], 'semi': m['semicolons_per_sent'], 'dlg': m['dialogue_share_pct']}
            row.append(f"{t['id']}: {m['words']} / {hw} / {m['sent_mean']} / {m['pct_over30']}% / {m['semicolons_per_sent']} / {m['dialogue_share_pct']}%")
        P(f'| {k} | ' + ' | '.join(row) + ' |')

    # Book→Plain overlap (how much of the plain retelling is lifted verbatim)
    P('\n# Plain-from-Book verbatim overlap: % of Plain 4-grams found in the paired Book tale (lower = more of a real retelling)')
    P('| tale | Modern v1.2 vs v1.3 | Plain v2.0 vs v2.0 | sentence ratio M1.2/v1.3 | sentence ratio P2/v2.0 |')
    P('|---|---|---|---|---|')
    tot = {'a': [], 'b': []}
    for k in order:
        a = b = ra = rb = '—'
        if k in bytitle['v1.3 Book'] and k in bytitle['Modern v1.2']:
            a = overlap(bytitle['v1.3 Book'][k]['body'], bytitle['Modern v1.2'][k]['body']); tot['a'].append(a)
            ra = round(len([s for p in bytitle['Modern v1.2'][k]['body'] for s in sentences(p)]) / max(1, len([s for p in bytitle['v1.3 Book'][k]['body'] for s in sentences(p)])), 2)
        if k in bytitle['v2.0 Book'] and k in bytitle['Plain v2.0']:
            b = overlap(bytitle['v2.0 Book'][k]['body'], bytitle['Plain v2.0'][k]['body']); tot['b'].append(b)
            rb = round(len([s for p in bytitle['Plain v2.0'][k]['body'] for s in sentences(p)]) / max(1, len([s for p in bytitle['v2.0 Book'][k]['body'] for s in sentences(p)])), 2)
        P(f'| {k} | {a} | {b} | {ra} | {rb} |')
    P(f"| MEAN | {round(statistics.mean(tot['a']),1)} | {round(statistics.mean(tot['b']),1)} | | |")

    # focus tales: longest sentences in v2.0 sample tales
    P('\n# Longest sentences, focus tales')
    for k in ['the torn cloak', 'the cry of the bonded', "the warden's door", 'the gift held an hour', 'the knowing of the green wood']:
        for n in ['v1.3 Book', 'v2.0 Book']:
            t = bytitle[n].get(k)
            if not t: continue
            ss = sorted([s for p in t['body'] for s in sentences(p)], key=lambda s: -len(words(s)))[:2]
            for s in ss:
                P(f'- [{n} {t["id"]}] ({len(words(s))}w) {s[:400]}')

    # headnotes of the focus tales
    P('\n# Headnotes, focus tales (words)')
    for k in ['the torn cloak', 'the cry of the bonded', "the warden's door", 'the gift held an hour', 'the knowing of the green wood']:
        for n in data:
            t = bytitle[n].get(k)
            if t:
                P(f'- [{n} {t["id"]}] {len(words(" ".join(t["head"])))}w: ' + ' || '.join(h[:220] for h in t['head']))

    txt = '\n'.join(out)
    print(txt)
    open(os.path.join(OUT_DIR, 'style_metrics_out.txt'), 'w').write(txt)
    json.dump({'corpus': corpus, 'hist': hists, 'pertale': pertale}, open(os.path.join(OUT_DIR, 'style_metrics.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
