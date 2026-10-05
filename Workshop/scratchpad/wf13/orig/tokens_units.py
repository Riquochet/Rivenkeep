#!/usr/bin/env python3
"""tokens.py (unit S01, private scratch; with the back-translation's fix_harmony): romanised Orrowen -> leaf-hand (Garl Flenn) token strings.

Reads each word through the private analyzer copy and the private merged lexicon (wf12: lexicon_orrowen.tsv here links
wf12/lexicon_orrowen_full.tsv, the merge of the Book v3.0.0's units), and writes the
course-hand's underlying form (orrowen_v2 §6.3): base letters, a bite (^S / ^N) under a mutated
consonant (or under the first vowel of a nasalised vowel-initial word), the harmonic letters A and O
for suffix vowels, '=' over a pair-name, and the marks (| perpend, , wedge, #gate, #coping).
Checks every token against the leaf-hand glyph table (wf7/orrowen/leafhand.py, imported read-only)
and counts letters and marks and pen movements with its own counter.

    python3 tokens.py FILE            (lines: ID<TAB>text; prints ID<TAB>tokens<TAB>counts)
    python3 tokens.py --selftest      (the §11 canon texts must come out as the spec's tokens)
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF7 = os.path.join(os.path.dirname(os.path.dirname(HERE)), "wf7")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(WF7, "orrowen"))
import orr_analyze as OA  # noqa: E402  (the private copy)
import leafhand as LH  # noqa: E402  (read-only import)

LEXPATH = os.path.join(HERE, "lexicon_orrowen.tsv")
LEX = OA.Lexicon(LEXPATH)
VOWELS = set("aeiouy")
PAIR_NAMES = {"halyna", "aldwena", "idrenna", "orvenna", "enrella", "wendhessa"}   # wf12: the Book v3.0.0's six (notes_v3 §2.2)
HARM_TOK = {"Ath": ["A", "th"], "Ol": ["O", "l"], "At": ["A", "t"], "Ard": ["A", "r", "d"], "Oth": ["O", "th"],
            "Ast": ["A", "s", "t"], "Om": ["O", "m"], "An": ["A", "n"], "A": ["A"], "Ar": ["A", "r"],
            "Os": ["O", "s"], "Ant": ["A", "n", "t"]}
PLAIN_TOK = {"el": ["e", "l"], "an": ["a", "n"], "en": ["e", "n"], "ow": ["o", "w"], "a": ["a"],
             "ith": ["i", "th"], "imp": ["a"]}
SUFCODE = {}
for c in list(HARM_TOK) + list(PLAIN_TOK):
    SUFCODE[c] = c
for c in ("at", "ath", "ard", "ol", "oth", "ast"):
    SUFCODE["-" + c] = {"at": "At", "ath": "Ath", "ard": "Ard", "ol": "Ol", "oth": "Oth", "ast": "Ast"}[c]
for c in ("an", "el", "en", "ow", "a"):
    SUFCODE["-" + c] = c
for a, b in (("yl", "Ol"), ("et", "At"), ("eth", "Ath"), ("erd", "Ard"), ("yth", "Oth"), ("est", "Ast"),
             ("om", "Om"), ("ym", "Om"), ("ar", "Ar"), ("er", "Ar"), ("ant", "Ant"), ("ent", "Ant"),
             ("os", "Os"), ("ys", "Os"), ("ith", "ith")):
    SUFCODE["-" + a] = b
SUFCODE.update({"1SG": "Om", "2SG": "ith", "1DU": "An", "3DU": "A", "1PL": "Ar", "2PL": "Os", "3PL": "Ant"})
OLD_BROAD = {"tresk", "flenn", "tev"}      # the canon's three old broad stems: full-vowel endings


def letters(s):
    s = s.lower().replace("’", "'")
    out, i = [], 0
    while i < len(s):
        if s[i:i + 2] in ("th", "dh", "rh"):
            out.append(s[i:i + 2]); i += 2; continue
        ch = s[i]
        if ch == "c":
            ch = "k"
        out.append(ch); i += 1
    return out


def bite_first(toks, mut):
    if not mut or not toks:
        return list(toks)
    t = list(toks)
    f = t[0]
    if "^" in f:
        return t
    if mut == "S":
        ok = f in ("p", "b", "m", "t", "d", "k", "g", "rh")
    else:
        ok = f in ("p", "t", "k", "b", "d", "g") or f in VOWELS
        if f == "d" and len(t) > 1 and t[1] == "r":
            ok = False
    if ok:
        t[0] = f + "^" + mut
    return t


def plain(toks):
    return [x.split("^")[0].replace("A", "a").replace("O", "o") for x in toks]


def add_suffix(toks, code, base):
    t = list(toks)
    suf = HARM_TOK.get(code) or PLAIN_TOK.get(code) or []
    if not suf:
        return t
    first_vowel = suf[0] in VOWELS or suf[0] in ("A", "O")
    nv = sum(1 for x in plain(t) if x in VOWELS)
    if first_vowel and t and plain(t)[-1] == "a" and nv > 1 and not "".join(plain(t)).endswith("ow"):
        t = t[:-1]                                   # an old -ā stem drops its -a
    elif first_vowel and t and plain(t)[-1] in VOWELS and not "".join(plain(t)).endswith("ow"):
        t = t + ["w"]                                # the glide: pa > pawast
    if code in HARM_TOK and base in OLD_BROAD:
        suf = [x.lower() if x in ("A", "O") else x for x in suf]
        suf = ["a" if x == "a" else x for x in suf]
    return t + suf


def tok_form(f, surface=None, depth=0):
    """tokens for a formation string (the lexicon's own recipe)"""
    f = f.strip()
    if depth > 6 or not f:
        return letters(surface or f)
    if f.startswith("na-"):
        return ["n", "a"] + bite_first(tok_form(f[3:], None, depth + 1), "S")
    if "+" in f:
        parts = f.split("+")
        base = parts[0]
        toks = tok_word(base, depth + 1)
        for p in parts[1:]:
            if p in SUFCODE:
                toks = add_suffix(toks, SUFCODE[p], base)
            elif p in ("3SG.M", "3SG.F"):
                toks = toks + (["y"] if p.endswith("F") else [])
            else:
                toks = toks + bite_first(tok_word(p, depth + 1), "S")
        return toks
    if "^" in f:
        mod, head = f.split("^", 1)
        return tok_word(mod, depth + 1) + bite_first(tok_form(head, None, depth + 1), "S")
    return tok_word(f, depth + 1)


def tok_word(w, depth=0):
    rows = LEX.get(w.lower())
    if rows:
        return tok_row(rows[0], depth)
    return letters(w)


def tok_row(row, depth=0):
    s = (row.get("orrowen") or "").lower()
    f = (row.get("formation") or "").strip()
    if not f or f.startswith("*") or f in ("loan", "phrase", "grammar") or " " in s or depth > 6:
        return letters(s)
    if "name" in (row.get("pos") or "") and not f.startswith("na-"):
        return letters(s)
    toks = tok_form(f, s, depth)
    if not rebuilds(toks, s):
        return letters(s)                           # the recipe does not rebuild the spelling: trust the spelling
    return fix_harmony(toks, s)


def _resolve(prev):
    vs = re.findall(r"ae|ow|[aeiouy]", "".join(x.split("^")[0] for x in prev if x not in ("A", "O")))
    return "S" if vs and vs[-1] in ("e", "i", "y", "ae") else "B"


def fix_harmony(toks, s):
    """(back-translation S01) a harmonic letter is read from the nearest full vowel before it
    (orrowen_v2 §6.4), so an ending the canon keeps broad on a slender stem (vennoth) must be
    written with its full vowel, as flennath and treskat are: replace any A/O that would read
    otherwise than the spelling"""
    ls = letters(s)
    if any("^" in x for x in toks) or len(ls) != len(toks):
        return toks
    out = list(toks)
    for i, x in enumerate(toks):
        if x in ("A", "O"):
            cls = _resolve(out[:i])
            read = {"A": "a", "O": "o"}[x] if cls == "B" else {"A": "e", "O": "y"}[x]
            if read != ls[i]:
                out[i] = ls[i]
    return out


def rebuilds(toks, s):
    """do the tokens, read aloud (bites applied, A = a/e, O = o/y), give the spelling s?"""
    rx = []
    for i, t in enumerate(toks):
        if t == "A":
            rx.append("[ae]")
        elif t == "O":
            rx.append("[oy]")
        elif "^" in t:
            b, m = t.split("^")
            nxt = toks[i + 1].split("^")[0] if i + 1 < len(toks) else "a"
            nxt = {"A": "a", "O": "o"}.get(nxt, nxt)
            f = OA.soften if m == "S" else OA.nasalise
            w = f(b + nxt).lower()
            out = w[: len(w) - len(nxt)] if w.endswith(nxt) else w
            rx.append("(?:%s)" % re.escape(out.replace("c", "k")))
        else:
            rx.append(re.escape(t))
    return re.fullmatch("".join(rx), s.lower().replace("c", "k")) is not None


def _soft_match(toks, s):
    """does the token list, read aloud (bites applied), give the spelling s?"""
    return read_aloud(toks) == s.replace("c", "k").replace("k", "k")


def read_aloud(toks):
    out = []
    for i, t in enumerate(toks):
        if "^" in t:
            b, m = t.split("^")
            w = "".join(x.split("^")[0] for x in toks[i:i + 2]).replace("A", "a").replace("O", "o")
            if m == "S":
                sw = OA.soften(b + "a").lower()
                out.append(sw[:-1] if sw.endswith("a") else sw)
            else:
                nw = OA.nasalise(b + "a").lower()
                out.append(nw[:-1] if nw.endswith("a") else nw)
        else:
            out.append(t.replace("A", "a").replace("O", "o"))
    return "".join(out).replace("c", "k")


def word_tokens(wd):
    t = wd.tok
    lw = t.lower().replace("’", "'")
    if lw in PAIR_NAMES:
        return ["=" + ".".join(letters(lw))]
    if wd.kind in ("particle", "prep"):
        return [".".join(letters(lw))]
    if wd.kind == "be":
        v = OA.BE_FORMS.get(lw)
        if v is None:
            return [".".join(letters(lw))]
        base, _g, mut = v[0], v[1], v[2]
        if base in ("el", "ew"):
            return [".".join(letters(lw))]
        toks = letters(base)
        if len(v) > 3:
            code = {"1SG": "Om", "2SG": "ith", "1DU": "An", "3DU": "A", "1PL": "Ar", "2PL": "Os", "3PL": "Ant"}[v[3]]
            toks = add_suffix(toks, code, base)
        return [".".join(bite_first(toks, mut or None))]
    p = wd.best
    if p is None:
        return [".".join(letters(lw))]
    # the analyzer's best reading is a gloss; for the hand, take the first reading whose letters, read
    # aloud, give the word as written, preferring a verb stem under a verbal ending (marrol < marr + Ol,
    # not N·arra + Ol) and a plain word over one that needs a compound's dropped rh (ullen, not S·rhullen)
    cands = [p] + [q for q in wd.parses if q is not p]
    def fits(q):
        return q.row is not None and rebuilds(_tokens_of(q, t), lw)
    def verbal_ok(q):
        if not q.layers or q.layers[0] not in ("Ol", "At", "Ard", "Om", "Ar", "Ant", "A", "An", "Os", "ith", "imp"):
            return True
        return "v" in (q.row.get("pos") or "").split(",")
    good = [q for q in cands if fits(q)]
    good = [q for q in good if verbal_ok(q)] or good
    if good:
        p = good[0]
    if p.row and not p.layers and (p.row.get("pos") or "").startswith("v") and (p.row.get("formation") or "").startswith("*"):
        for q in wd.parses:                          # an inflected canon verb row (tessen): write its ending
            if q.layers and q.harmony_ok and q.mut == p.mut and set(q.layers) <= set(HARM_TOK) | {"ith"}:
                p = q
                break
    return [".".join(_tokens_of(p, t))]


def _tokens_of(p, t):
    row = p.row
    if row and "name" in (row.get("pos") or "") and t[:1].isupper() and not p.layers:
        toks = letters(row.get("orrowen") or p.stem)   # a name is said, not meant
    elif row:
        toks = tok_row(row)
    else:
        toks = letters(p.stem)
    base = (row.get("orrowen") or p.stem).lower() if row else p.stem
    for code in p.layers:
        toks = add_suffix(toks, code, base)
    if p.prefix:
        toks = ["n", "a"] + bite_first(toks, "S")
    toks = bite_first(toks, p.mut)
    return toks


MARK = {".": "|", "!": "|", "?": "|", ",": ",", ";": ",", ":": ","}


def line_tokens(text, end=None):
    words = OA.analyse_text(text, LEX)
    out = []
    for j, wd in enumerate(words):
        if wd.kind == "punct" and wd.tok.startswith("!") and 0 < j < len(words) - 1 \
                and words[j + 1].tok.lower() == words[j - 1].tok.lower():
            continue                                  # a repeated cry is one course (the Cry: Talda Talda Talda)
        if wd.kind == "punct":
            m = MARK.get(wd.tok[:1])
            if m and not (out and out[-1] in ("|", ",") and m == ","):
                if out and out[-1] == "," and m == "|":
                    out[-1] = "|"
                elif out and out[-1] == m:
                    pass
                else:
                    out.append(m)
            continue
        out += word_tokens(wd)
    if end:
        if out and out[-1] in ("|", ","):
            out[-1] = end
        else:
            out.append(end)
    return " ".join(out)


def check(tokstr):
    bad = []
    for w in tokstr.split():
        if w in ("|", ",") or w.startswith("#"):
            if w not in LH.G:
                bad.append(w)
            continue
        for part in w.lstrip("=").split("."):
            k = part.split("^")[0]
            if k not in LH.G:
                bad.append(part)
    n_items = sum(len(w.lstrip("=").split(".")) if not (w in ("|", ",") or w.startswith("#")) else 1
                  for w in tokstr.split())          # letters and marks, as orrowen_v2 §11 counts them (bites and lintels aside)
    return bad, n_items, LH.movements(tokstr)


CANON = [
    ("Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan.",
     "u.l t^N.u.m.O.l o.l v.a.r.n , o.l th.e.l.d.A.th , o.l m.a.r.dh , o.l l.u.n.n.A.th , o.l s.o.l.l.a.n |"),
    ("Tumar.", "t.u.m.A.r |"),
    ("Nawrodhat. Nath noss tul kethyl et gunn sy lo Halyna.",
     "n.a.b^S.r.o.dh.A.t | n.a.th d^N.o.s.s t.u.l k.e.th.O.l e.t g.u.n.n s.y l.o =h.a.l.y.n.a |"),
    ("Marr tho dhrun. Kyl tho vedh. Keth, ell lusk.",
     "m.a.r.r th.o t^S.r.u.n | k.y.l th.o p^S.e.dh | k.e.th , e.l.l l.u.s.k |"),
    ("Keth et tolm. Cadh et trenn. Amm cadhat o, es dess et odh.",
     "k.e.th e.t t.o.l.m | k.a.dh e.t t.r.e.n.n | a.m.m k.a.dh.A.t o , e.s t^N.e.s.s e.t o.dh |"),
    ("Grest um hos, grest um vana.", "g.r.e.s.t u.m h.o.s , g.r.e.s.t u.m p^S.a.n.a |"),
    ("Carm et lodh hy et trun. Talda, Stonwrytan! Cadha tolm um dholm. Stona gor hald dem et dask sost, Talda! Talda! Talda!",
     "k.a.r.m e.t l.o.dh h.y e.t t.r.u.n | t.a.l.d.a , s.t.o.n.w.r.y.t.a.n | k.a.dh.a t.o.l.m u.m t^S.o.l.m | s.t.o.n.a g.o.r h.a.l.d d.e.m e.t d.a.s.k s.o.s.t , t.a.l.d.a t.a.l.d.a t.a.l.d.a |"),
    ("Es ston et hald sy. Re hadhan o, eth tessen o, somm el tolm tolm. Ston.",
     "e.s s.t.o.n e.t h.a.l.d s.y | r.e k^S.a.dh.A.n o , e.th t.e.s.s.A.n o , s.o.m.m e.l t.o.l.m t.o.l.m | s.t.o.n |"),
    ("Hebbet sa re yal kethet hos clem", "h.e.b.b.A.t s.a r.e g^S.a.l k.e.th.A.t h.o.s k.l.e.m"),
    ("Re wrodha Halyna o, hos eth ullen, ul ba luth; re hadh Seren o.",
     "r.e b^S.r.o.dh.A =h.a.l.y.n.a o , h.o.s e.th u.l.l.e.n , u.l p^N.a l.u.th , r.e k^S.a.dh s.e.r.e.n o |"),
    ("Amm re yal et mesk cresket, ell re omm et brodhol, doss o rellorat eth nahlennet.",
     "a.m.m r.e g^S.a.l e.t m.e.s.k k.r.e.s.k.A.t , e.l.l r.e o.m.m e.t b.r.o.dh.O.l , d.o.s.s o r.e.l.l.o.r.A.t e.th n.a.k^S.l.e.n.n.A.t |"),
    ("Re yal o lo et lodh um et parow, eth re heth o o hosen re heth ey o, eth ew o sa re hadh et tolm hosast ul et brodhol.",
     "r.e g^S.a.l o l.o e.t l.o.dh u.m e.t p.a.r.o.w , e.th r.e k^S.e.th o o h.o.s.e.n r.e k^S.e.th e.y o , e.th e.w o s.a r.e k^S.a.dh e.t t.o.l.m h.o.s.A.s.t u.l e.t b.r.o.dh.O.l |"),
]


def selftest():
    ok = True
    for text, want in CANON:
        got = line_tokens(text)
        flag = "ok " if got == want else "DIFF"
        if got != want:
            ok = False
        print(flag, text)
        if got != want:
            print("   got :", got)
            print("   want:", want)
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    src = sys.argv[1]
    for line in open(src, encoding="utf-8"):
        line = line.rstrip("\n")
        if "\t" not in line:
            continue
        i, t = line.split("\t", 1)
        if t.isupper():
            continue
        end = "#coping" if i.endswith(".12") and i.startswith("C.") else None
        ts = line_tokens(t, end)
        if i.endswith("S2"):
            ts = ts + " #gate"                          # a vow ends in the gate (§6.7)
        bad, n, mv = check(ts)
        print("%s\t%s\t%d letters and marks, %d pen movements%s" % (i, ts, n, mv, ("\tBAD " + " ".join(bad)) if bad else ""))
