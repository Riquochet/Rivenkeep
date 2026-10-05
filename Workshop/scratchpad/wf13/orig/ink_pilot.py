#!/usr/bin/env python3
"""ink_pilot.py (the pilots' ink.py, kept for comparison) -- romanised Orrowen (as the Book spells it) -> the leaf-hand's token string -> Garl Flenn markup,
reading the MERGED tier-3 lexicon (wf8 copy: its orr_analyze.py and lexicon_orrowen.tsv are private copies,
the lexicon being wf8/lexicon_orrowen_full.tsv; never goes into Docs/).

to_ink.py reads the wf6 lexicon through render_shore.py and so spells the tier-3 words by sound (the pilot's
note, pilot_I1.md §5 "The hands").  This does what that note asks: it takes every word's parse from
orr_analyze.py (lexicon_orrowen.tsv), and writes the UNDERLYING form the course-hand writes (orrowen_v2 §6.3):

  * a mutated word: its base letter with the bite under it (dumol -> t^N.u.m.O.l; rik -> g^S.r.i.k; hull -> rh^S.u.l.l);
    after the prefix na- the softened stem likewise (nawrodhat -> n.a.b^S.r.o.dh.A.t);
  * every harmonic suffix (-Ath -Ol -At -Ard -Oth -Ast and the person endings) with its harmonic letter A or O;
  * the sealing lintel over a pair-name (=h.a.l.y.n.a); Seren's own name and every other name without one;
  * the Book's punctuation as the marks: . ! ? the perpend, , ; : the wedge; a one-word sentence Ston. that
    closes an oath takes the gate (#gate); the end of a tale the coping (#coping, D10).

Then wf7/to_ink.py turns the token string into the font's markup (bites as combining marks, ZWNJ where a t/d/r
and an h are two letters).

    python3 orig/ink.py "Re hadh Crennel Kael, Kael Nydherd."          # tokens, then markup
    python3 orig/ink.py --test                                          # the pilots' own token strings
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W7 = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'wf7')
sys.path.insert(0, W7)
sys.path.insert(0, HERE)        # the private analyzer copy, reading the merged lexicon (wf8/lexicon_orrowen_full.tsv)
import orr_analyze as OA   # noqa: E402
import to_ink as TI        # noqa: E402

LEX = OA.Lexicon()
PAIR_NAMES = {"halyna", "aldwena", "idrenna"}          # the Bonded pairs' names carry the sealing lintel
HARM_LETTER = {"Ath": "A", "At": "A", "Ard": "A", "Ast": "A", "An": "A", "A": "A", "Ar": "A", "Ant": "A",
               "Ol": "O", "Oth": "O", "Om": "O", "Os": "O"}
DIGRAPHS = ("th", "dh", "rh")


def letters(w):
    """a spelled word -> its letters (th dh rh one letter each; c and k one letter; hw one letter)"""
    w = w.lower()
    out, i = [], 0
    while i < len(w):
        two = w[i:i + 2]
        if two in DIGRAPHS or two == "hw":
            out.append(two)
            i += 2
            continue
        ch = w[i]
        out.append("k" if ch == "c" else ch)
        i += 1
    return out


def base_of(surface, mut, stem):
    """the word with its first letter restored, and the base letter (the one that takes the bite)"""
    lw = surface.lower()
    cands = OA.unsoften(lw) if mut == "S" else OA.unnasalise(lw)
    st = OA.nk(stem)
    best = None
    for b, m in cands:
        if OA.nk(b)[:max(1, min(3, len(st)))] == st[:max(1, min(3, len(st)))]:
            best = b
            break
    if best is None and cands:
        best = cands[0][0]
    return best


def harm_mark(lets, layers):
    """replace the vowel of every harmonic suffix by its harmonic letter, from the end inward"""
    j = len(lets)
    for code in reversed(layers):
        if code in OA.HARMONIC:
            forms = OA.HARMONIC[code]
            done = False
            for f in forms:
                fl = letters(f)
                if lets[j - len(fl):j] == fl:
                    # the suffix's vowel: its first vowel letter
                    for q in range(j - len(fl), j):
                        if lets[q] in "aeiouy":
                            lets[q] = HARM_LETTER[code]
                            break
                    j -= len(fl)
                    done = True
                    break
            if not done:
                return lets, False
        else:
            f = "a" if code == "imp" else OA.PLAIN.get(code, "")
            fl = letters(f)
            if f and lets[j - len(fl):j] == fl:
                j -= len(fl)
            else:
                return lets, False
    return lets, True


VERB_CODES = {"Om", "ith", "An", "A", "Ar", "Os", "Ant", "imp"}
BE_TAG = {"1SG": "Om", "2SG": "ith", "1DU": "An", "3DU": "A", "1PL": "Ar", "2PL": "Os", "3PL": "Ant"}
FORM_CODE = {"At": "At", "at": "At", "et": "At", "Ol": "Ol", "ol": "Ol", "yl": "Ol", "Ath": "Ath", "ath": "Ath",
             "eth": "Ath", "Ard": "Ard", "ard": "Ard", "erd": "Ard", "Oth": "Oth", "oth": "Oth", "yth": "Oth",
             "Ast": "Ast", "ast": "Ast", "est": "Ast", "Ar": "Ar", "ar": "Ar", "er": "Ar", "el": "el", "en": "en",
             "ow": "ow"}


def derived_parse(wd, p):
    """a word the lexicon holds whole (hebbet, tumar, nawrodhat) is still written with its harmonic letters
    and bites (the course-hand writes the underlying form, §6.3): its row's formation says how it was made,
    so take the analyser's layered parse that agrees with it"""
    row = p.row or {}
    form = (row.get("formation") or "").strip()
    if not form or ("+" not in form and not form.startswith("na-") and "-" not in form):
        return p
    head = re.split(r"[+]", form.replace("na-", "").lstrip("*"), maxsplit=1)[0]
    head = head.split("-")[0].strip()
    want_prefix = form.startswith("na-")
    pos = row.get("pos", "")
    alts = [q for q in OA.analyse_word(wd.tok.lower(), LEX)
            if q.layers and q.harmony_ok and bool(q.prefix) == want_prefix and q.mut == p.mut]
    if not alts:
        # the analyser will not strip it (galat: the suppletive gal takes no participle in its parses),
        # but the row's own formation names the suffix: take it from there
        m = re.search(r"\+\s*-?([A-Za-z]+)\s*$", form)
        if m and not want_prefix:
            suf = m.group(1)
            isverb = pos.startswith("v") or ",v" in pos
            code = FORM_CODE.get(suf) or FORM_CODE.get(suf.lower())
            if suf.lower() == "an":
                code = "An" if isverb else "an"
            if code:
                return OA.Parse(p.row, head, [code], p.mut)
        return p
    head_k = OA.nk(head)

    def fits(q):
        st = OA.nk(q.stem)
        return st == head_k or head_k.startswith(st) or st.startswith(head_k)
    alts = [q for q in alts if fits(q)] or []
    if not alts:
        return p
    isverb = pos.startswith("v") or ",v" in pos
    alts.sort(key=lambda q: (0 if (q.layers[-1] in VERB_CODES) == isverb else 1, len(q.layers), q.score()))
    return alts[0]


def word_tokens(wd):
    """one analysed word -> its letter tokens, or None (with a reason) where the analysis cannot place it"""
    t = wd.tok
    lw = t.lower().replace("’", "'")
    if "'" in lw:
        return ".".join(letters(lw.replace("'", ""))), None
    p = wd.best
    if p is None:
        return ".".join(letters(lw)), "no parse"
    if wd.kind == "be" and lw in OA.BE_FORMS:
        # the two "be" verbs (§3.4): the base under its bite (noss = N·doss, yal = S·gal) and the person
        # ending with its harmonic letter (yalant = S·gal + -Ant)
        v = OA.BE_FORMS[lw]
        lemma, mut = v[0], v[2]
        surf_stem = {"doss": "doss", "noss": "doss", "yal": "gal", "gal": "gal"}.get(lw[:4] if lw[:4] in ("doss", "noss") else lw[:3], lemma)
        if lemma in ("doss", "gal") and lw[:len(surf_stem)] != surf_stem:
            word = surf_stem + lw[len(surf_stem):]
        else:
            word = lw
        lets = letters(word)
        layers = [BE_TAG[v[3]]] if len(v) > 3 else []
        lets, ok = harm_mark(lets, layers)
        if mut in ("S", "N") and lets:
            lets[0] += "^" + mut
        return ".".join(lets), (None if ok else "suffix letters not found")
    if not p.layers and wd.kind not in ("particle", "prep", "be"):
        q = derived_parse(wd, p)
        if not q.layers:
            # na- + a stem the lexicon holds whole (nayalat = na- + galat): the stem's own formation
            # gives the suffix, and the stem's first letter takes the prefix's softening
            form = ((p.row or {}).get("formation") or "")
            cands = [p] if p.prefix else ([x for x in OA.analyse_word(lw, LEX) if x.prefix and not x.layers]
                                          if form.startswith("na-") else [])
            for x in cands:
                inner = OA.Word(x.stem)
                OA.analyse_living(inner, LEX)
                if inner.best is not None:
                    r = derived_parse(inner, inner.best)
                    if r.layers:
                        q = OA.Parse(x.row, r.stem, list(r.layers), x.mut, prefix=True)
                        break
        p = q
    word = lw
    bite_at = None
    if p.mut in ("S", "N") and wd.kind not in ("particle", "prep"):
        b = base_of(lw, p.mut, p.stem)
        if b:
            word = b
            bite_at = (0, p.mut)
    lets = letters(word)
    if p.prefix and lets[:2] == ["n", "a"]:
        rest = "".join(lets[2:])
        st = OA.nk(p.stem)
        if OA.nk(rest)[:2] != st[:2]:
            for b, m in OA.unsoften(rest):
                if OA.nk(b)[:2] == st[:2]:
                    lets = ["n", "a"] + letters(b)
                    bite_at = (2, "S")
                    break
    lets, ok = harm_mark(lets, p.layers)
    toks = []
    for i, L in enumerate(lets):
        s = L
        if bite_at and i == bite_at[0]:
            s += "^" + bite_at[1]
        toks.append(s)
    out = ".".join(toks)
    if lw in PAIR_NAMES:
        out = "=" + out
    return out, (None if ok else "suffix letters not found for %s" % "+".join(p.layers))


def line_tokens(text, end=None, report=None):
    """a line of romanised Orrowen -> the course-hand token string. end: None, 'coping'"""
    words = OA.analyse_text(text, LEX)
    out = []
    sentence_words = []
    for i, wd in enumerate(words):
        if wd.kind == "punct":
            for ch in wd.tok:
                if ch in ".!?":
                    nxt = next((w for w in words[i + 1:] if w.kind != "punct"), None)
                    if ch == "!" and nxt is not None and sentence_words and nxt.tok.lower() == sentence_words[-1].lower():
                        continue           # a cry repeated is one cry (§7.2)
                    out.append("|")
                    # a one-word sentence Ston. closing an oath takes the gate (§3.9, §6.7)
                    if len(sentence_words) == 1 and sentence_words[0].lower() == "ston":
                        out.append("#gate")
                    sentence_words = []
                elif ch in ",;:—-":
                    out.append(",")
                # "…" and others: left open
            continue
        sentence_words.append(wd.tok)
        tk, why = word_tokens(wd)
        if (why or wd.status != "OK") and report is not None:
            report.append((wd.tok, wd.status, why, OA.gloss_of(wd.best) if wd.best else ""))
        out.append(tk)
    if end == "coping":
        if out and out[-1] == "|":
            out.pop()                      # the coping closes the tale in the perpend's place (D10)
        out.append("#coping")
    return " ".join(out)


def markup(text, end=None, report=None):
    tok = line_tokens(text, end, report)
    return TI.tokens_to_markup(tok), tok


def _norm_tokens(s):
    return " ".join(s.replace(" |", " |").split())


def selftest():
    bad = 0
    # the IV.4 pilot's frame: its romanised lines and its hand-checked token strings
    rom = open(os.path.join(W7, "pilot_IV4", "headnote.txt"), encoding="utf-8").read().strip().split("\n")
    tok = open(os.path.join(W7, "pilot_IV4", "headnote.tokens"), encoding="utf-8").read().strip().split("\n")
    pairs = list(zip(rom, tok))
    # the canon's own (orrowen_v2 §11, via to_ink.SAMPLES)
    pairs += [(r, t) for k, r, t in TI.SAMPLES]
    for r, t in pairs:
        end = "coping" if t.rstrip().endswith("#coping") else None
        got = line_tokens(r, end)
        # the pilot writes the title with no closing perpend
        want = _norm_tokens(t)
        g = _norm_tokens(got)
        if g.endswith(" |") and not want.endswith("|") and not want.endswith("#coping") and not want.endswith("#gate"):
            g = g[:-2]
        ok = g == want
        bad += not ok
        print(("ok   " if ok else "DIFF ") + r[:70])
        if not ok:
            print("   want:", want)
            print("   got: ", g)
    print("%d differences" % bad)
    return bad


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        sys.exit(1 if selftest() else 0)
    rep = []
    m, t = markup(" ".join(a), report=rep)
    print(t)
    print(m)
    for r in rep:
        print("  !", r)
