"""The sound laws from the first tongue (Ulvrae... name fixed in roots.py) to
Orrowen (via the Hal) and to Seilrhass (via the Eldest speech).

Every law is a named, ordered function.  derive_o() and derive_s() return the
stages and a trace of which laws fired, so the tables in ancestor.md are
computed, not typed.

Ancestral romanisation (input):
  p b t d k g   m n ŋ   f th dh s x h   w r l y   ʔ (the catch)
  vowels a e i o u.  '-' marks a suffix seam, '+' a compound seam.
Stress is on the first syllable, in the ancestor and in both daughters.
"""
import re

VOW = set("aeiou")
# ---------------------------------------------------------------- tokens
def tok(s):
    """ancestral romanisation -> list of segment codes"""
    out, i = [], 0
    while i < len(s):
        two = s[i:i + 2]
        if two == "th":
            out.append("T"); i += 2; continue
        if two == "dh":
            out.append("D"); i += 2; continue
        c = s[i]
        out.append({"ŋ": "N", "ʔ": "Q"}.get(c, c))
        i += 1
    return out

SHOW_ANC = {"T": "th", "D": "dh", "N": "ŋ", "Q": "ʔ"}
def show_anc(segs):
    return "".join(SHOW_ANC.get(c, c) for c in segs)

def is_v(c):
    return c in VOW or c in ("A", "E", "I", "O", "U", "Y", "ü", "ɛ")

def strip_b(segs):
    return [c for c in segs if c not in "-+"]

# ================================================================ ORROWEN
# Stage 1: the first tongue -> the Hal (the first builders' speech)
#   O1  the catch: before l r m n s it doubles the consonant; before any other
#       consonant, or at the end of a word, it lengthens the vowel; between
#       vowels, or at the start, it is lost.
#   O2  the old diphthongs close: ai, ei, oi > ē ; au, ou > ū ; eu > iu ; ui > y
#   O3  i-colouring (umlaut): a stressed a, o > e and u > y when the next
#       syllable holds i.  This is the birth of the slender class.
#   O4  f > v everywhere; w > v before a vowel (not in wr-, not after g);
#       gw > w; sw- > s-; x > h before r, w and a front vowel (the Hal's hr,
#       hw, and the h of hya)
#   O5  three like consonants in a row keep two (lld > ld, rrn > rn)

LONG = {"a": "A", "e": "E", "i": "I", "o": "O", "u": "U", "ü": "Y"}

def O1_catch(w):
    w = list(w); out = []
    i = 0
    while i < len(w):
        c = w[i]
        if c == "Q":
            prev = out[-1] if out else None
            # next real segment (skip seams)
            j = i + 1
            while j < len(w) and w[j] in "-+":
                j += 1
            nxt = w[j] if j < len(w) else None
            if prev and prev in LONG:
                if nxt is None:
                    out[-1] = LONG[prev]
                elif nxt in "lrmns":
                    # double the consonant (if not already doubled)
                    seam = w[i + 1:j]
                    out.extend(seam)
                    if not (j + 1 < len(w) and w[j + 1] == nxt):
                        out.append(nxt)
                    i = j
                    continue
                elif is_v(nxt):
                    pass  # lost between vowels
                else:
                    out[-1] = LONG[prev]
            # word-initial or after a consonant: lost
            i += 1
            continue
        out.append(c)
        i += 1
    return out

def O2_diph(w):
    s = "".join(w)
    s = s.replace("ai", "E").replace("ei", "E").replace("oi", "E")
    s = s.replace("au", "U").replace("ou", "U").replace("eu", "iu").replace("ui", "ü")
    return list(s)

def O2b_shorten(w):
    """a long vowel before two consonants is shortened (weinnis > vennis)"""
    w = list(w); out = list(w)
    for i, c in enumerate(w):
        if c in "AEIOUY":
            nxt = [x for x in w[i + 1:i + 4] if x not in "-+"]
            if len(nxt) >= 2 and not is_v(nxt[0]) and not is_v(nxt[1]):
                out[i] = {"A": "a", "E": "e", "I": "i", "O": "o", "U": "u", "Y": "ü"}[c]
    return out

def _vowel_positions(w):
    return [i for i, c in enumerate(w) if is_v(c)]

def O3_umlaut(w):
    w = list(w)
    vp = _vowel_positions(w)
    if len(vp) < 2:
        return w
    a, b = vp[0], vp[1]
    # iu counts as one nucleus: skip
    if w[a] == "i" and b == a + 1:
        return w
    between = w[a + 1:b]
    if "+" in between:           # never across a compound seam
        return w
    if not any(c not in "-+" for c in between):
        return w                 # hiatus: no umlaut
    if w[b] in ("i", "I"):
        w[a] = {"a": "ɛ", "o": "e", "u": "ü"}.get(w[a], w[a])
    return w

def O4_cons(w):
    s = "".join(w)
    s = s.replace("f", "v")
    s = re.sub(r"^sw", "s", s)
    s = s.replace("xr", "R")                     # Hal hr (the rough r)
    s = s.replace("xw", "F")                     # Hal hw
    s = s.replace("gw", "W")                     # the new w
    s = re.sub(r"w(?=[aeiouAEIOUüYɛ])", "v", s)  # w > v before a vowel
    s = s.replace("W", "w")
    s = re.sub(r"x(?=[iIüYj])", "h", s)
    return list(s)

def O5_clusters(w):
    s = "".join(w)
    s = re.sub(r"([lrmns])\1(?=[^aeiouAEIOUüY\-+]|$)", lambda m: m.group(1), s) if False else s
    s = s.replace("lld", "ld").replace("rrn", "rn").replace("nnt", "nt").replace("rrd", "rd")
    s = s.replace("TT", "T").replace("DD", "D").replace("ssk", "sk").replace("sst", "st")
    s = re.sub(r"([lrmns])\1(?=[bcdfgkmnprstTDvwxlhFR])", lambda m: m.group(1), s)
    return list(s)

HAL_SHOW = {"T": "th", "D": "dh", "N": "ŋ", "A": "ā", "E": "ē", "I": "ī", "O": "ō", "U": "ū",
            "ü": "y", "Y": "ȳ", "R": "hr", "F": "hw", "j": "y"}
def show_hal(w):
    s = "".join(c for c in w if c not in "-+")
    return ck("".join(HAL_SHOW.get(c, c) for c in s).replace("ɛ", "ɛ")).replace("ɛ", "e")

def ck(s):
    """the Book's c/k: k before e i y ae and in -sk-; c elsewhere and in sc-;
    and c before an e that the i-colouring made out of a (cemm, cedh)"""
    out = []
    for i, ch in enumerate(s):
        if ch == "k":
            nxt = s[i + 1:i + 3]
            prev = s[i - 1] if i else ""
            if nxt[:1] == "ɛ":
                out.append("c")
            elif nxt[:1] in ("e", "i", "y", "ē", "ī", "ȳ") or nxt[:2] == "ae":
                out.append("k")
            elif prev == "s" and i > 1:
                out.append("k")
            elif i == len(s) - 1 and prev in ("e", "i", "y", "ɛ"):
                out.append("k")
            else:
                out.append("c")
        else:
            out.append(ch)
    s = "".join(out)
    s = re.sub(r"^sk", "sc", s)
    return s

# Stage 2: the Hal -> living Orrowen (the laws of shoreland_spec §4.2, made exact)
#   H1  the -n of the small words falls (ulan > ula)
#   H2  the fall of the endings: final -os, -is, -as after a consonant, and any
#       final short vowel, are lost in words of two or more syllables.  A final
#       long -ā survives as -a where it is still a living ending (the dual, the
#       feminine); a final -ū survives as -ow.
#   H3  the long vowels shift: ā > o, ē > ae, ī > i, ō > u, ū > ow; an unstressed
#       long vowel inside a word is first shortened (tevāthi > tevath)
#   H4  the three mergers and the loss of w: x > h, ŋm > mm, ŋ > n, hw > f,
#       hr > rh, wr- > r-, iu > y
#   H5  the wearing at a compound seam: after the seam p b m t d k g > v w v dh r h y
#       (only in compounds spelled as said: Halvard)

def H1_particle_n(w, small):
    if small and w and w[-1] == "n" and len(w) >= 2 and is_v(w[-2]):
        return w[:-1]
    return w

def H2_endings(w, keep_long_a=True):
    w = list(w)
    real = "".join(c for c in w if c not in "-+").replace("iu", "Ü")
    nv = len([c for c in real if is_v(c) or c == "Ü"])
    if nv < 2 or real.endswith("Ü"):
        return w
    # -os -is -as after a consonant
    s = "".join(w)
    m = re.search(r"([^aeiouAEIOUüY\-+])-?([oia])s$", s)
    if m:
        s = s[:m.start(2)].rstrip("-") if s[m.start(2) - 1] == "-" else s[:m.start(2)]
        return list(s.rstrip("-"))
    # final short vowel (after consonant or vowel)
    if w[-1] in "aeiou":
        return list("".join(w[:-1]).rstrip("-"))
    if w[-1] == "A" and not keep_long_a:
        return list("".join(w[:-1]).rstrip("-"))
    return w

def H3_long(w):
    w = list(w)
    vp = _vowel_positions(w)
    out = []
    for k, c in enumerate(w):
        if c in "AEIOUY":
            final = (k == len(w) - 1) or all(x in "-+" for x in w[k + 1:])
            first = vp and k == vp[0]
            if final:
                out.append({"A": "a", "E": "ae", "I": "i", "O": "u", "U": "ow", "Y": "y"}[c])
            elif not first:
                out.append({"A": "a", "E": "e", "I": "i", "O": "o", "U": "u", "Y": "ü"}[c])
            else:
                out.append({"A": "o", "E": "ae", "I": "i", "O": "u", "U": "ow", "Y": "i"}[c])
        else:
            out.append(c)
    return list("".join(out))

def H4_merge(w, keep_wr=False):
    s = "".join(w)
    s = s.replace("Nm", "mm").replace("N", "n")
    s = s.replace("x", "h").replace("F", "f").replace("R", "Ṙ")
    if not keep_wr:
        s = re.sub(r"(^|[+\-])wr", lambda m: m.group(1) + "r", s)
    s = s.replace("iu", "ü")
    return list(s)

SOFT = {"p": "v", "b": "w", "m": "v", "t": "D", "d": "r", "k": "h", "g": "j"}
def H5_seam(w):
    w = list(w)
    for i, c in enumerate(w):
        if c == "+" and i + 1 < len(w) and w[i + 1] in SOFT:
            w[i + 1] = SOFT[w[i + 1]]
    return w

def romanise_o(w):
    """living Orrowen in the Book's spelling (§2.4): c/k, th, dh, rh, y, ae, ow"""
    s = "".join(c for c in w if c not in "-+")
    s = s.replace("T", "th").replace("D", "dh").replace("Ṙ", "rh").replace("ü", "y").replace("j", "y")
    return ck(s).replace("ɛ", "e")

def harmony(w):
    """H6 (the spec's law 7): a suffix vowel a or o after a slender stem becomes e or y"""
    s = "".join(w)
    m = re.match(r"^(.*?[eiüɛ][^aeiouüɛAEIOUY]+)([ao])([^aeiouüɛ]*)$", s)
    if m:
        s = m.group(1) + {"a": "e", "o": "ü"}[m.group(2)] + m.group(3)
    return list(s)

def derive_o(anc, small=False, compound=False, keep_long_a=True, keep_wr=False, hal_only=False, affix=False, harm=False):
    """anc: ancestral romanisation (the whole word, with its Hal ending).
    Returns dict with 'hal', 'living', 'trace'."""
    trace = []
    w = [c for c in tok(anc) if c != "-"]
    steps = [("anc", show_anc(w))]
    pre = "-" if affix else ""
    for name, fn in (("O1", O1_catch), ("O2", O2_diph), ("O2", O2b_shorten), ("O3", (lambda x: x) if affix else O3_umlaut), ("O4", O4_cons), ("O5", O5_clusters)):
        nw = fn(w)
        if strip_b(nw) != strip_b(w):
            if not trace or trace[-1] != name:
                trace.append(name)
            steps.append((name, show_hal(nw)))
        w = nw
    hal = pre + show_hal(w)
    if hal_only:
        return {"hal": hal, "living": None, "trace": trace, "steps": steps}
    for name, fn in (("H1", lambda x: H1_particle_n(x, small)),
                     ("H2", (lambda x: x) if affix else (lambda x: H2_endings(x, keep_long_a))),
                     ("H2", (lambda x: list("".join(x)[:-1]) if affix and "".join(x)[-1:] in "aeiou" and len([c for c in x if is_v(c)]) > 1 else x)),
                     ("H3", (lambda x: H3_long(["b"] + x)[1:]) if affix else H3_long),
                     ("H4", lambda x: H4_merge(x, keep_wr)),
                     ("H5", H5_seam if compound else (lambda x: x)),
                     ("H6", harmony if harm else (lambda x: x))):
        nw = fn(w)
        if strip_b(nw) != strip_b(w):
            trace.append(name)
            steps.append((name, show_mid(nw)))
        w = nw
    return {"hal": hal, "living": pre + romanise_o(w), "trace": trace, "steps": steps}

def show_mid(w):
    """an in-between Orrowen form: the Hal's letters for what has not yet merged"""
    s = "".join(c for c in w if c not in "-+")
    m = {"T": "th", "D": "dh", "N": "ŋ", "A": "ā", "E": "ē", "I": "ī", "O": "ō", "U": "ū", "Y": "ȳ",
         "ü": "y", "R": "hr", "F": "hw", "Ṙ": "rh", "j": "y"}
    return ck("".join(m.get(c, c) for c in s)).replace("ɛ", "e")

# ================================================================ SEILRHASS
# Seilrhass is built on the ancestral STEM (no case ending): the wood-folk kept
# the bare stem that the first tongue used for calling and naming.
# Stage 1: the parting (the first tongue -> the Eldest speech)
#   S1  the catch and the old diphthongs break in the first syllable:
#       aʔ oʔ ai oi au > ae ; eʔ > ea ; iʔ > i ; uʔ ei > ei ; eu > e ; ui > i.
#       A w after the first vowel and before another vowel melts into it
#       (aw > ae, ew > ea, iw > ei).  Elsewhere aʔ > ae, eʔ > ea, and the
#       catch is otherwise lost.
#   S2  the brightening: in the first syllable o > ae; i and u > ei in an open
#       syllable, > i in a closed one; a and e stay.
#   S3  the thinning of the later syllables: o, u, i > e; a > e in an open
#       syllable that is not the last; an unstressed old diphthong gives a
#       long e (E) that will not fall.
#   S4  the lips and the throat go soft: p b f w > v; m ŋ > n; h y > nothing;
#       d > t; g x > k  (the Eldest speech has only the stops t and k)
#   S5  the clusters: at the start tr- > t-, kr- gr- xr- xwr- > k-,
#       pr- br- fr- wr- mr- > r-, stop or fricative + l > l-, st- sk- sp- sw- > s-;
#       after a vowel sk > ss, st > s(s), s+th > sth, nt nd n+th > nth,
#       mb > nn, lt ld > l, rt rd rn rm > r, lm > l, rs ls ns ks ts > ss,
#       kt pt > t, tt > t, ll > l, rr > r; a final k or v is lost
# Stage 2: the Eldest speech -> living Seilrhass (mystaeri_spec §2.4)
#   S6  the old stops were lost: t > th, k > rh (a stop after the first
#       syllable left the knock, which then spread to every word of two
#       syllables or more)
#   S7  final vowels fell after a consonant (and after a vowel), except the
#       long E of an old diphthong and a final -a or -ae
#   S8  -aer > -ear (by analogy with -ea), except in Esthaer

S_DIPH1 = [("aQ", "Æ"), ("oQ", "Æ"), ("ai", "Æ"), ("oi", "Æ"), ("au", "Æ"),
           ("eQ", "Ë"), ("iQ", "ı"), ("uQ", "Ï"), ("ei", "Ï"), ("eu", "e"), ("ui", "ı")]
# Æ = ae, Ë = ea, Ï = ei (single nuclei)
SV = set("aeiouÆËÏEı")

def _first_vowel(w):
    for i, c in enumerate(w):
        if c in SV:
            return i
    return None

def S1_break(w):
    s = "".join(w)
    fv = _first_vowel(list(s))
    if fv is None:
        return list(s)
    # w melting after the first vowel before another vowel
    m = re.match(r"^([^aeiou]*)([aeiou])w(?=[-+]?[aeiou])", s)
    if m:
        v = m.group(2)
        rep = {"a": "Æ", "e": "Ë", "i": "Ï", "o": "Æ", "u": "Ï"}[v]
        s = m.group(1) + rep + s[m.end():]
    else:
        for a, b in S_DIPH1:
            if s[fv:fv + 2] == a:
                s = s[:fv] + b + s[fv + 2:]
                break
    # elsewhere
    s = s.replace("aQ", "Æ").replace("eQ", "Ë").replace("ai", "E").replace("ei", "E")
    s = s.replace("Q", "")
    # vowel + vowel across a seam after melting
    return list(s)

def _closed(w, i):
    """is the vowel at i in a closed syllable (ancestral count)?"""
    j = i + 1
    cons = 0
    while j < len(w) and w[j] not in SV:
        if w[j] not in "-+":
            cons += 1
        j += 1
    if j >= len(w):           # no vowel after: word-final consonant(s)
        return cons >= 1
    return cons >= 2

def S2_bright(w):
    w = list(w)
    fv = _first_vowel(w)
    if fv is None:
        return w
    c = w[fv]
    if c == "o":
        w[fv] = "Æ"
    elif c in ("i", "u"):
        w[fv] = "i" if _closed(w, fv) else "Ï"
    return w

def S3_thin(w):
    w = list(w)
    fv = _first_vowel(w)
    vs = [i for i, c in enumerate(w) if c in SV]
    for k, i in enumerate(vs):
        if i == fv:
            continue
        c = w[i]
        last = (k == len(vs) - 1)
        if c in ("o", "u", "i"):
            w[i] = "e"
        elif c == "a" and not last and not _closed(w, i):
            w[i] = "e"
    return w

def S4_soft(w):
    s = "".join(w)
    s = re.sub(r"^gw", "w", s)
    s = s.replace("nd", "nn").replace("mb", "nn")
    s = re.sub(r"[pbfw]", "v", s)
    s = re.sub(r"[mN]", "n", s)
    s = re.sub(r"[hy]", "", s)
    s = s.replace("d", "t").replace("D", "T")
    s = re.sub(r"[gx]", "k", s)
    return list(s)

def S5_clusters(w):
    s = "".join(w)
    # onsets
    s = re.sub(r"^s[tkv]r", "s", s)
    s = re.sub(r"^tr", "t", s); s = re.sub(r"^Tr", "t", s)
    s = re.sub(r"^kvr", "k", s); s = re.sub(r"^kr", "k", s)
    s = re.sub(r"^kvl", "l", s)
    s = re.sub(r"^vr", "r", s); s = re.sub(r"^nr", "r", s)
    s = re.sub(r"^[tTkv]l", "l", s)
    s = re.sub(r"^s[tkv]", "s", s)
    s = re.sub(r"^kv", "k", s)
    # after a vowel
    V = "aeiouÆËÏE"
    s = re.sub(r"sk(?=[-+]?[%s])" % V, "ss", s)
    s = re.sub(r"sk", "ss", s)
    s = re.sub(r"sT", "S", s)                       # s + th, kept (esth)
    s = s.replace("st", "s")
    s = re.sub(r"n[tT]", "N", s)                    # nth
    s = s.replace("nd", "nn").replace("nt", "N")
    s = s.replace("vv", "v")
    s = re.sub(r"l[tT]", "l", s)
    s = re.sub(r"r[tTnm]", "r", s)
    s = s.replace("rn", "r").replace("ln", "l")
    s = s.replace("ln", "l")
    s = re.sub(r"ln|lm", "l", s)
    s = re.sub(r"[rlnkt]s", "ss", s)
    s = re.sub(r"k[tT]", "t", s)
    s = re.sub(r"v[tT]", "t", s)
    s = s.replace("tt", "t").replace("TT", "T").replace("tT", "T")
    s = s.replace("ll", "l").replace("rr", "r").replace("kk", "k")
    s = s.replace("nn", "M")                        # protect nn
    s = re.sub(r"[kv]$", "", s)
    s = re.sub(r"[kv](?=[-+][^%s])" % V, "", s)
    s = s.replace("M", "nn").replace("N", "nT").replace("S", "sT")
    # any other pair of consonants left at the end of the word keeps its first
    s = re.sub(r"(rl|lr|rs|lv|rv|lk|rk|lp|rp|lm|rm|ln|rn|nl|nr)$", lambda m: m.group(1)[0], s)
    return list(s)

def show_eldest(w):
    s = "".join(c for c in w if c not in "-+")
    s = s.replace("D", "dh").replace("N", "ŋ").replace("Q", "ʔ")
    return s.replace("ı", "i").replace("T", "th").replace("Æ", "ae").replace("Ë", "ea").replace("Ï", "ei").replace("E", "e")

def S6_stops(w):
    s = "".join(w)
    s = s.replace("t", "T").replace("k", "K")
    return list(s)

S_CODA_OK = ("nT", "sT", "ss", "nn")
def S7_final(w):
    w = [c for c in w]
    # strip trailing seams
    while w and w[-1] in "-+":
        w.pop()
    nv = len([c for c in w if c in SV])
    if nv >= 2 and w[-1] == "e":
        w.pop()
        # the new last syllable may end in a pair the tongue does not allow:
        # it keeps the first of them (rharle > rharl > rhar)
        s = "".join(w)
        tail = re.search(r"([^aeiouÆËÏEı]{2,})$", s)
        if tail and tail.group(1) not in S_CODA_OK and not tail.group(1) in ("TK",):
            t = tail.group(1)
            keep = t[0] if t[0] in "lnrsT" else ""
            s = s[:tail.start(1)] + keep
        # a stop or the rough r cannot end a word
        s = re.sub(r"[tkKv]$", "", s)
        w = list(s)
    return w

def romanise_s(w):
    s = "".join(c for c in w if c not in "-+")
    s = s.replace("T", "th").replace("K", "rh").replace("ı", "i")
    s = s.replace("Æ", "ae").replace("Ë", "ea").replace("Ï", "ei").replace("E", "e")
    # vowel sequences created by loss
    s = s.replace("aea", "aea")
    return s

def derive_s(stem, relic_aer=False, small=False, affix=False):
    trace = []
    pre = "-" if (affix or stem.startswith("-")) else ""
    affix = affix or stem.startswith("-")
    w = [c for c in tok(stem) if c != "-"]
    steps = [("anc", show_anc(w))]
    for name, fn in (("S1", (lambda x: x) if affix else S1_break) if not affix else ("S1", S1_affix),
                     ("S2", (lambda x: x) if (small or affix) else S2_bright),
                     ("S3", S3_thin_all if affix else S3_thin), ("S4", S4_soft), ("S5", S5_clusters)):
        nw = fn(w)
        if strip_b(nw) != strip_b(w):
            trace.append(name)
            steps.append((name, show_eldest(nw)))
        w = nw
    eldest = show_eldest(w)
    for name, fn in (("S6", S6_stops), ("S7", S7_final)):
        nw = fn(w)
        if strip_b(nw) != strip_b(w):
            trace.append(name)
            steps.append((name, romanise_s(nw)))
        w = nw
    liv = romanise_s(w)
    if not relic_aer and liv.endswith("aer") and len(liv) >= 3:
        liv = liv[:-3] + "ear"; trace.append("S8"); steps.append(("S8", liv))
    return {"eldest": pre + eldest, "living": pre + liv, "trace": trace, "steps": steps}

def S1_affix(w):
    s = "".join(w)
    s = s.replace("aQ", "Æ").replace("eQ", "Ë").replace("ai", "E").replace("ei", "E").replace("Q", "")
    return list(s)

def S3_thin_all(w):
    w = list(w)
    vs = [i for i, c in enumerate(w) if c in SV]
    for k, i in enumerate(vs):
        c = w[i]
        last = (k == len(vs) - 1)
        if c in ("o", "u", "i"):
            w[i] = "e"
        elif c == "a" and not last and not _closed(w, i):
            w[i] = "e"
    return w

def knock(liv):
    """the spoken form: a knock after the first syllable of any word of 2+ syllables"""
    nuc = re.compile(r"(ae|ea|ei|a|e|i)")
    ms = list(nuc.finditer(liv))
    if len(ms) < 2:
        return liv
    # the consonants between nucleus 1 and 2: the last one begins syllable 2
    a_end = ms[0].end(); b = ms[1].start()
    mid = liv[a_end:b]
    # onset of syllable 2: rh / th if they end mid, else last letter
    if mid.endswith("rh") or mid.endswith("th"):
        cut = b - 2
    elif mid == "":
        cut = a_end
    else:
        cut = b - 1
    # double letters split (ss, nn, ll, rr): keep one each side
    return liv[:cut] + "'" + liv[cut:]

if __name__ == "__main__":
    tests_o = [("trosk-is", "tresk"), ("krask-is", "cresk"), ("ol-on", "ol"), ("pa-naʔ", "pana"),
               ("taʔl-d-uʔ", "taldow"), ("xreun-aʔ", "rhyna"), ("sweren-", None), ("waʔr-n-os", "varn"),
               ("weʔs-is", "vess"), ("kail-os", "kael"), ("xwren-n-os", "frenn"), ("aŋ-ma", "amm"),
               ("xui-a", "hy"), ("tum-ol-a", "tumol"), ("taw-is", "tev")]
    for a, e in tests_o:
        r = derive_o(a, small=a in ("ol-on", "xui-a"))
        print("O", a, "->", r["hal"], "->", r["living"], r["trace"], "" if e is None or r["living"] == e else "  <<< want " + e)
    tests_s = [("trosk-i", "thaess"), ("krask-i", "rhass"), ("ol", "ael"), ("pann-i", "vann"),
               ("taʔl-i", "thael"), ("xreun-i", "rhen"), ("waʔr-ai", "vaere"), ("weʔs-i", "veas"),
               ("weʔth-i", "veath"), ("ston-i", "saen"), ("skedh-i", "seth"), ("tum-i", "thein"),
               ("par-ane", "varen"), ("aŋ-thi", "anth"), ("taw-i", "thae"), ("lew-i", "lea"),
               ("kul-i", "rheil"), ("iʔl-aʔ", "ilae"), ("es-th-a", None), ("brant-i", "ranth"), ("xwrel-i", "rhel"),
               ("xwlel-i", "lel"), ("kritth-i", "rhith"), ("musi", "neis"), ("weinn-i", "veinn")]
    for a, e in tests_s:
        r = derive_s(a)
        print("S", a, "->", r["eldest"], "->", r["living"], knock(r["living"]), r["trace"], "" if e is None or r["living"] == e else "  <<< want " + e)
