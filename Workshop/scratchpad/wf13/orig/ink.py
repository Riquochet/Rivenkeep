#!/usr/bin/env python3
"""ink.py (wf8, set up for wf12: the Book v3.0.0) -- romanised Orrowen -> the leaf-hand's token string -> Garl Flenn markup, for the whole Book.

Two token writers came out of tier 3: the pilots' (wf7/orig/ink.py, kept here as ink_pilot.py) and the units'
(tokens_units.py, the merge's copy of wf8/tmp/mergetok/tokens.py, with the back-translations' fixes: `ullen` not
S·rhullen, `marrol` not N·arra+Ol, the old broad stems' full vowels `flennath treskat tevath`, both harmonic letters
of a stacked ending `galdArdAth`, na- with its softened stem `nat^SumAr`).  This writer takes the units' tokens and
applies the merge's one rule on top (merge_report §5.2 #16, orrowen_v2 §6.5): a LEXICALISED COMPOUND is written as
said, with no bite inside it (kaelirvesk, meskdhrenn, brenthromm, rellordholm, stannowvardath ...).  So a bite is
kept only on a word's first letter, or on the stem after the prefix na-; any other bite is written as the letters
said, the harmonic letters of the ending kept.  A word the units' writer cannot place falls back to the pilots'.
Both read the merged lexicon (the private copy orr_analyze.py + lexicon_orrowen.tsv, which links wf12/lexicon_orrowen_full.tsv).

    python3 ink.py "Re hadh Crennel Kael, Kael Nydherd."     # tokens, then markup
    python3 ink.py --test                                    # the canon's and the pilots' own token strings
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W7 = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'wf7')
sys.path.insert(0, W7)
sys.path.insert(0, HERE)
import orr_analyze as OA          # noqa: E402  (private copy)
import to_ink as TI               # noqa: E402  (wf7, read only)
import tokens_units as TU         # noqa: E402
import ink_pilot as IP            # noqa: E402

LEX = TU.LEX
VOW = set('aeiouy')


def _plain(t):
    return t.split('^')[0].replace('A', 'a').replace('O', 'o')


def _same(t, s):
    """does token t (A/O allowed) stand for surface letter s?"""
    if t == 'A':
        return s in ('a', 'e')
    if t == 'O':
        return s in ('o', 'y')
    return _plain(t) == s


def as_said(toks, surface):
    """re-spell a word whose tokens carry a bite inside it: letters as said, harmonic letters and the first
    letter's (or the na- stem's) bite kept. None if the tokens and the spelling cannot be lined up."""
    S = TU.letters(surface)
    keep_first = '^' in toks[0]
    na = len(toks) > 2 and toks[0] == 'n' and toks[1] == 'a' and '^' in toks[2] and surface.lower().startswith('na')
    inner = [i for i, t in enumerate(toks) if '^' in t and not (i == 0) and not (na and i == 2)]
    if not inner:
        return toks
    j = max(inner)
    tail = toks[j + 1:]
    if len(tail) > len(S) or not all(_same(t, s) for t, s in zip(tail, S[len(S) - len(tail):])):
        return None
    j0 = min(inner)
    head = toks[:j0]
    # the head: its letters as the surface has them, but for a bitten first letter (or na- stem)
    if keep_first or na:
        lead = 3 if na else 1
        rest = head[lead:]
        for a in range(0, len(S) - len(tail) - len(rest) + 1):
            if all(_same(t, s) for t, s in zip(rest, S[a:a + len(rest)])) and (a >= (2 if na else 0)):
                mid = S[a + len(rest):len(S) - len(tail)]
                return head[:lead] + rest + mid + tail
        return None
    if not all(_same(t, s) for t, s in zip(head, S[:len(head)])):
        return None
    return head + S[len(head):len(S) - len(tail)] + tail


def reharmonise(toks):
    """the units' writer spells every ending of the three old broad stems (tev, flenn, tresk) with its full vowel,
    which is right where the canon keeps the ending broad on the slender stem (flennath, treskat, tevath: the harmonic
    letter would read e) but not where the ending's vowel is the one the harmonic letter reads (tevet, `tevAt`, as
    the IV.4 pilot and the wood units write it)"""
    base = [t.split('^')[0] for t in toks]
    for st in (('t', 'e', 'v'), ('f', 'l', 'e', 'n', 'n'), ('t', 'r', 'e', 's', 'k')):
        if tuple(base[:len(st)]) == st and len(toks) > len(st) and toks[len(st)] in ('e', 'y'):
            i = len(st)
            cls = TU._resolve(toks[:i])
            if cls == 'S':
                toks = toks[:i] + [{'e': 'A', 'y': 'O'}[toks[i]]] + toks[i + 1:]
    return toks


FINITE_BEFORE = ('re', 'es', 'nath')


def word_tokens(wd, prev=None):
    lw = wd.tok.lower().replace('’', "'")
    if "'" in lw:
        # a name with the knock (Ael'thar): written as the pilots write it, its letters whole
        return '.'.join(TU.letters(lw.replace("'", '')))
    if prev and prev.lower() in FINITE_BEFORE and wd.best is not None and wd.best.layers == ['imp']:
        # after a tense particle a verb is finite, never the imperative: -a is the dual (nath re luska sona)
        du = [q for q in wd.parses if q.layers == ['A'] and q.row is wd.best.row]
        if du:
            wd.best = du[0]
    try:
        w = TU.word_tokens(wd)[0]
    except Exception:  # noqa: BLE001
        w = None
    if w is not None:
        lint = w.startswith('=')
        toks = w.lstrip('=').split('.')
        bad = any(t in ('', '^') or t.startswith('^') for t in toks)
        if not bad:
            said = as_said(toks, wd.tok.lower().replace('’', "'"))
            if said is not None:
                return ('=' if lint else '') + '.'.join(reharmonise(said))
    tk, _why = IP.word_tokens(wd)
    return tk


MARK = {".": "|", "!": "|", "?": "|", ",": ",", ";": ",", ":": ","}


def line_tokens(text, end=None, report=None):
    """a line of romanised Orrowen -> the course-hand token string. end: None or 'coping'"""
    words = OA.analyse_text(text, LEX)
    out = []
    sent = []
    for j, wd in enumerate(words):
        if wd.kind == 'punct' and wd.tok.startswith('!') and 0 < j < len(words) - 1 \
                and words[j + 1].tok.lower() == words[j - 1].tok.lower():
            continue                                  # a repeated cry is one course (the Cry: Talda Talda Talda)
        if wd.kind == 'punct':
            m = MARK.get(wd.tok[:1])
            if wd.tok[:1] == '…':
                # wf12: an ellipsis (a broken-off word: the Guest's three words, the readings' fragments) is the wedge
                # between words and no mark at the end of the line (orrowen_v2 §11.8: h.e.s.s , h.e.l.v , s.e.n.n.O.l)
                m = ',' if any(w.kind != 'punct' for w in words[j + 1:]) else None
            if m and not (out and out[-1] in ('|', ',') and m == ','):
                if out and out[-1] == ',' and m == '|':
                    out[-1] = '|'
                elif out and out[-1] == m:
                    pass
                else:
                    out.append(m)
            if m == '|':
                # a one-word sentence Ston. that closes an oath takes the gate (§3.9, §6.7)
                if len(sent) == 1 and sent[0].lower() == 'ston':
                    out.append('#gate')
                sent = []
            continue
        sent.append(wd.tok)
        if report is not None and wd.status != 'OK':
            report.append((wd.tok, wd.status, OA.gloss_of(wd.best) if wd.best else ''))
        prev = next((w.tok for w in reversed(words[:j]) if w.kind != 'punct'), None)
        out.append(word_tokens(wd, prev))
    if end:
        e = '#' + end if not end.startswith('#') else end
        if out and out[-1] in ('|', ','):
            out[-1] = e
        else:
            out.append(e)
    return ' '.join(out)


def markup(text, end=None, report=None):
    tok = line_tokens(text, end, report)
    return TI.tokens_to_markup(tok), tok


def selftest():
    bad = 0
    pairs = [(r, t) for r, t in TU.CANON]
    rom = open(os.path.join(W7, 'pilot_IV4', 'headnote.txt'), encoding='utf-8').read().strip().split('\n')
    tok = open(os.path.join(W7, 'pilot_IV4', 'headnote.tokens'), encoding='utf-8').read().strip().split('\n')
    pairs += list(zip(rom, tok))
    spec = [(r, t) for k, r, t in TI.SAMPLES]
    # the canon's own strings (orrowen_v2 §11, via to_ink.SAMPLES) win where the units' list gives the same line
    # without its gate (the units' writer adds a vow's gate by line id)
    pairs = [(r, t) for r, t in pairs if r.strip().rstrip('.') not in {x.strip().rstrip('.') for x, _ in spec}] + spec
    for r, t in pairs:
        want = ' '.join(t.split())
        end = 'coping' if want.endswith('#coping') else None
        got = line_tokens(r, end)
        if not want.endswith(('|', '#coping', '#gate')) and got.endswith(' |'):
            got = got[:-2]
        ok = got == want
        bad += not ok
        print(('ok   ' if ok else 'DIFF ') + r[:70])
        if not ok:
            print('   want:', want)
            print('   got: ', got)
    print('%d differences' % bad)
    return bad


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--test' in a:
        sys.exit(1 if selftest() else 0)
    rep = []
    m, t = markup(' '.join(a), report=rep)
    print(t)
    print(m)
    for r in rep:
        print('  !', r)
