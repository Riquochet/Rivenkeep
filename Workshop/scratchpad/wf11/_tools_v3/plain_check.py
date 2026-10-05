#!/usr/bin/env python3
"""Plain Words checker (voice_v3.md §11).

Usage:
  python3 plain_check.py <book_leaf.md> <plain_leaf.md>
  python3 plain_check.py <combined.md>        (Book leaf, then '<!-- PLAIN WORDS ... -->', then the Plain)

A Book leaf file that also carries an old Plain twin is cut at '<!-- PLAIN WORDS'.
Reports length ratio, sentence shape, contractions, Flesch-Kincaid, overlap with the Book,
an archaism and inversion scan, and whether the fixed matter, markers, {{pair-names}} and the warden's blots carried over.
The scans flag lines for a human look; they do not judge."""
import os, re, sys, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from count_v3 import proper_parts, sentences, words, grams, fk  # noqa: E402

FIXED_LINES = [
    'In memory of our home, our families, our God, our freedoms, our peace.',
    'IN MEMORY OF OUR HOME, OUR FAMILIES, OUR GOD, OUR FREEDOMS, OUR PEACE.',
    'The mortar cries out from the ground. Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end.',
    'Rise! Rise! Rise!',
    'We remember our home too.',
    'We remember.',
    'But war is for the short-minded and the angry young.',
    'When the left hand dies, does not the right one die too?',
    'Stop… Sky… Dying…',
    'Unknown intruder. Hostile intent. Neutralized. Vessel burned and released.',
    'What I saw, I carry. I carry nothing else.',
    'Not as Brenn carried.',
    'This is held in the grain.',
]
# Paragraphs that are fixed matter (left out of the prose-only measures).
FIXED_STARTS = ('>', '**IN MEMORY', '*Then ', 'This is held in the grain.', '*And no one answered', 'And no one answered',
                "That's all he came to say", 'That is all he came to say', '*And the hearth said', '*And everyone at the hearth said',
                'This I lay', 'This we lay', 'I have laid', 'We have laid', '*—', '— ')

ARCHAIC = r"""\b(thou|thee|thy|thine|ye|hath|doth|dost|saith|art|wast|wert|ere|naught|aught|wist|spake|sware|bade|forgat|
kneeled|whoso|whosoever|bide|bides|feign|feigned|morrow|nigh|oft|lest|yonder|hither|thither|whither|wherefore|whence|
upon|unto|amongst|whilst|ween|peradventure|eft|methinks|forsooth|prithee|mayhap|perchance|anon|alas|lo|verily|
twain|nay|aye|yea|beseech|betwixt)\b"""
ETH = r"\b(?!teeth\b|beth\b)[a-z]+eth\b"
NOT_AFTER_VERB = r"\b(?:know|knew|go|went|come|came|see|saw|say|said|spoke|take|took|give|gave|stop|stopped|fear|feared|care|cared|doubt|doubted|look|looked|hear|heard|answer|answered|move|moved|wept|laugh|laughed|fight|fought|struck|tell|told|ask|asked|want|wanted|think|thought|believe|believed|understand|understood|remember|remembered|forget|forgot|rose|fell|held|hold|let|seek|sought|wist)\s+not\b"
INVERSION = r"(?:^|[.!?]\s+|\"|“)(Then|Now|Down|Up|Out|In|Into|Over|So|Thus|Never|Long|Last|First|Little|Well|Twice|Alone|Gone)\s+(came|went|ran|rode|was|were|stood|lay|sat|spake|spoke|said|laughed|fell|rose|did|had|have|is|are|knew|saw|heard|cried|began|stopped)\s+(?!up\b|out\b|down\b|back\b|on\b|off\b|away\b)"
BANNED = r"\b(Picture a|Think of|Imagine)\b"
TELLTALE_FOR = r",\s+for\s+(?!a |an |the |ever|good|now|once|years|days|nights|a month|a moment|him|her|them|us|me|you|it|what|that|this|those|these|each|every|all|one|two|three|four|five|six|seven|eight|nine|ten|twelve|forty)"


def split_inputs(argv):
    if len(argv) == 2:
        raw = open(argv[1], encoding='utf-8').read()
        if '<!-- PLAIN WORDS' not in raw:
            sys.exit('one file given but it has no <!-- PLAIN WORDS --> marker')
        book, plain = raw.split('<!-- PLAIN WORDS', 1)
        return book, plain.split('-->', 1)[1]
    book = open(argv[1], encoding='utf-8').read().split('<!-- PLAIN WORDS', 1)[0]
    plain = open(argv[2], encoding='utf-8').read()
    if '<!-- PLAIN WORDS' in plain:
        plain = plain.split('<!-- PLAIN WORDS', 1)[1].split('-->', 1)[1]
    return book, plain


def nwords(ps):
    return sum(len(words(p)) for p in ps)


def prose(ps):
    return [p for p in ps if not p.startswith(FIXED_STARTS)]


def shape(ps):
    ss = sentences(ps)
    ls = [len(words(s)) for s in ss]
    return ss, ls


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    book_raw, plain_raw = split_inputs(sys.argv)
    bh, bp = proper_parts(book_raw, True)
    ph, pp = proper_parts(plain_raw, False)
    bw, pw = nwords(bp), nwords(pp)
    bpr, ppr = prose(bp), prose(pp)
    bpw, ppw = nwords(bpr), nwords(ppr)
    ss, ls = shape(ppr)   # prose only: no songs, liturgy, Title or reading lines
    body = ' '.join(pp)
    contr = len(re.findall(r"\b(?:\w+n['’]t|\w+['’](?:ll|re|ve|d|m)|(?:it|that|he|she|there|what|who|here|let|where)['’]s)\b", body, flags=re.I))
    bg = set(grams(bp)); pg = grams(pp)
    bg2 = set(grams(bpr)); pg2 = grams(ppr)
    ov = 100 * sum(g in bg for g in pg) / max(1, len(pg))
    ov2 = 100 * sum(g in bg2 for g in pg2) / max(1, len(pg2))

    def mark(ok):
        return 'ok ' if ok else 'FIX'
    r = pw / bw
    r2 = ppw / max(1, bpw)
    print(f"LENGTH   {mark(0.70 <= r <= 0.85)} tale proper: Book {bw} · Plain {pw} = {100*r:.1f}% (band 70-85%; most leaves land 75-85%)")
    print(f"         (info) prose only, fixed matter out: Book {bpw} · Plain {ppw} = {100*r2:.0f}%")
    print(f"PARAS    {mark(len(pp) <= 0.85 * len(bp))} paragraphs: Book {len(bp)} · Plain {len(pp)} (its own paragraphing: about a quarter fewer)")
    print(f"HEADNOTE {mark(len(words(ph)) <= 45)} {len(words(ph))} words (45 at most; one or two sentences)")
    mean = statistics.mean(ls)
    short = 100 * sum(l < 10 for l in ls) / len(ls)
    over = [l for l in ls if l > 25]
    print(f"SENTENCE {mark(10 <= mean <= 14)} mean {mean:.1f} (10-14) · median {statistics.median(ls)}")
    print(f"         {mark(short <= 40)} under 10 words {short:.0f}% (about a third; 40% at most for a curt teller)")
    print(f"         {mark(not [l for l in ls if l > 30])} over 25 words: {len(over)} {over} (none over 30; over 25 only for a plain list)")
    print(f"         {mark(body.count(';') == 0)} semicolons {body.count(';')}")
    print(f"WORDS    {mark(10 <= 1000*contr/pw <= 35)} contractions {contr} ({1000*contr/pw:.1f}/1k; 10-35)")
    print(f"         {mark(fk(ss) <= 4.5)} Flesch-Kincaid grade {fk(ss):.1f} (4 or under; 4.5 hard stop)")
    print(f"OVERLAP  {mark(ov <= 20 and ov2 <= 15)} 4-word runs in the Book: {ov:.1f}% all · {ov2:.1f}% prose (20% / 15% at most)")

    scan = [(n, s) for n, s in enumerate(ss)]
    hits = []
    for n, s in scan:
        for lab, pat, fl in (('archaic', ARCHAIC, re.I | re.X), ('-eth', ETH, re.I), ('verb+not', NOT_AFTER_VERB, re.I),
                             ('inversion?', INVERSION, 0), ('banned', BANNED, 0), (', for (because?)', TELLTALE_FOR, re.I)):
            m = re.search(pat, s, fl)
            if m:
                hits.append(f"  [{lab}] «{m.group(0).strip()}» in: {s[:90]}")
    print(f"SCAN     {mark(not hits)} {len(hits)} line(s) to look at" + ('' if hits else ''))
    for h in hits:
        print(h)

    # fixed matter carried over
    bfull, pfull = re.sub(r'\s+', ' ', book_raw), re.sub(r'\s+', ' ', plain_raw)
    missing = [f for f in FIXED_LINES if f in bfull and f not in pfull]
    print(f"FIXED    {mark(not missing)} fixed lines in the Book missing from the Plain: {missing or 'none'}")
    bn = sorted(set(re.findall(r'\{\{[^}]+\}\}', book_raw))); pn = sorted(set(re.findall(r'\{\{[^}]+\}\}', plain_raw)))
    print(f"PAIRS    {mark(set(bn) <= set(pn))} {{{{names}}}} Book {bn} · Plain {pn}")
    bb, pb = book_raw.count('▒▒▒▒'), plain_raw.count('▒▒▒▒')
    print(f"WARDEN   {mark((bb == 0) == (pb == 0))} ▒▒▒▒ blots: Book {bb} · Plain {pb}")
    mk = lambda t: sorted(set(re.findall(r'<!-- (PROLOGUE EXCERPT BEGIN|PROLOGUE EXCERPT END|HALYNA END|HALYNA|READING|RING|FACING LEAF)', t)))
    print(f"MARKERS  {mark(mk(book_raw) == mk(plain_raw))} Book {mk(book_raw)} · Plain {mk(plain_raw)}")
    nb = len(re.findall(r'^\s*>?\s*::: native', book_raw, flags=re.M)); npl = len(re.findall(r'^\s*>?\s*::: native', plain_raw, flags=re.M))
    print(f"NATIVE   {mark(nb == npl)} native blocks: Book {nb} · Plain {npl}")


if __name__ == '__main__':
    main()
