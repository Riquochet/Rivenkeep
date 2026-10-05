#!/usr/bin/env python3
"""orr_analyze.py: check romanised Orrowen against the tier-3 lexicon (wf7, scratch; standard library only).

    python3 orr_analyze.py "Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan."
    python3 orr_analyze.py --gloss "Carm et lodh hy et trun."
    python3 orr_analyze.py --gloss --hal "GRESTOS UMO HOSOS GRESTOS UMO PANĀ"
    python3 orr_analyze.py --file text.txt            (one sentence or line per line)
    python3 orr_analyze.py --test                      (every sample of orrowen_v2.md)

What it does, word by word (the grammar is orrowen_v2.md §3):
  1. tokenises (words, the Mystaeri knock ' inside a loan, and the punctuation);
  2. undoes the two initial mutations (§3.3), softening (S) and nasalising (N), with the repair
     rules (a softened g before a consonant drops; a softened rh after a consonant drops);
  3. undoes the inflections and the derivational suffixes (§3.2, §3.4, §5.12): -Ath, -Ol, -At, -Ard,
     -Oth, -el, -an, -en, -ow, -Ast, -a, the person endings, the imperative plural, the prefix na-,
     the conjugated prepositions (§3.6) and the two "be" verbs (§3.4);
  4. checks each stem against the lexicon (lexicon_orrowen.tsv), and the harmony of every
     harmonic suffix (A: a/e, O: o/y) against the stem's class;
  5. checks each mutation against the word before it (the triggers of §3.3): a trigger with no
     mutation after it, or a mutation with no trigger (outside a construct), is reported;
  6. reports UNKNOWN or ILL-FORMED words with suggestions (the right mutation, the right harmony,
     and the nearest lexicon words); --gloss prints a word-by-word gloss instead.
The --hal switch (or an all-capitals line) reads the old register, the Hal, against the lexicon's
Hal forms and the Hal's own endings.
"""
import os, re, sys, csv, difflib, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "lexicon_orrowen.tsv")

# ======================================================================= phonology and spelling
VOW = "aeiouy"
SLENDER_V = ("e", "i", "y", "ae")


def nk(w):
    """a lookup key: lower case, c and k are one sound (the c/k split is a spelling rule, §2.4)"""
    w = w.lower().replace("’", "'")
    return w.replace("c", "k")


def full_vowels(w):
    return re.findall(r"ae|ow|[aeiouy]", w.lower())


def word_class(w):
    """harmony class (§2.2): the class of the last full vowel; a o u ow broad, e i y ae slender"""
    vs = full_vowels(w)
    if not vs:
        return "B"
    return "S" if vs[-1] in SLENDER_V else "B"


def ck_join(stem, suffix):
    """respell a stem-final c/k before a suffix vowel: k before e i y ae, and in -sk; c before a o u"""
    if stem and stem[-1] in "ck" and suffix:
        if len(stem) > 1 and stem[-2] == "s":
            return stem[:-1] + "k" + suffix
        if suffix[0] in "eiy" or suffix.startswith("ae"):
            return stem[:-1] + "k" + suffix
        if suffix[0] in "aou":
            return stem[:-1] + "c" + suffix
    return stem + suffix


def recase(src, out):
    return out[:1].upper() + out[1:] if src[:1].isupper() else out


# ======================================================================= the two mutations (§3.3)
def soften(w):
    """S, the wearing: p b m t d c/k g rh > v w v dh r h y h; a softened g before a consonant drops"""
    lw = w.lower()
    if not lw:
        return w
    if lw.startswith("rh"):
        out = "h" + lw[2:]
    elif lw.startswith(("th", "dh", "sc", "sk")):
        out = lw
    elif lw[0] == "p":
        out = "v" + lw[1:]
    elif lw[0] == "b":
        out = "w" + lw[1:]
    elif lw[0] == "m":
        out = "v" + lw[1:]
    elif lw[0] == "t":
        out = "dh" + lw[1:]
    elif lw[0] == "d":
        out = "r" + lw[1:]
        if out.startswith("rr"):
            out = out[1:]                     # dr- > r- (a doubled r cannot begin a word)
    elif lw[0] in "ck":
        out = "h" + lw[1:]
    elif lw[0] == "g":
        out = ("y" + lw[1:]) if len(lw) > 1 and lw[1] in VOW else lw[1:]
    else:
        out = lw
    return recase(w, out)


def nasalise(w):
    """N, the bedding: p t c/k b d g > b d g m n n; a vowel takes m- (broad) or n- (slender);
    a nasalised d before r stays d"""
    lw = w.lower()
    if not lw:
        return w
    if lw.startswith(("th", "dh", "rh", "sc", "sk")):
        out = lw
    elif lw[0] == "p":
        out = "b" + lw[1:]
    elif lw[0] == "t":
        out = "d" + lw[1:]
    elif lw[0] in "ck":
        out = "g" + lw[1:]
    elif lw[0] == "b":
        out = "m" + lw[1:]
    elif lw[0] == "d":
        out = lw if lw[1:2] == "r" else "n" + lw[1:]
    elif lw[0] == "g":
        out = "n" + lw[1:]
    elif lw[0] in "aeiou" or (lw[0] == "y" and (len(lw) == 1 or lw[1] not in VOW)):
        first = full_vowels(lw)[0] if full_vowels(lw) else "a"
        out = ("n" if first in SLENDER_V else "m") + lw
    else:
        out = lw
    return recase(w, out)


def unsoften(w):
    """candidate base forms of a word that may be softened: [(base, 'S'), ...]"""
    lw = w.lower()
    out = []
    if lw.startswith("dh"):
        out.append(("t" + lw[2:], "S"))
    elif lw.startswith("v"):
        out += [("p" + lw[1:], "S"), ("m" + lw[1:], "S")]
    elif lw.startswith("w"):
        out.append(("b" + lw[1:], "S"))
    elif lw.startswith("r") and not lw.startswith("rh"):
        out.append(("d" + lw[1:], "S"))
        out.append(("d" + lw, "S"))          # dr- > r- (drunn > runn)
        out.append(("g" + lw, "S"))          # g dropped before a consonant (gorr > re yorr; grest > rest)
    elif lw.startswith("h"):
        out += [("k" + lw[1:], "S"), ("rh" + lw[1:], "S")]
    elif lw.startswith("y") and len(lw) > 1 and lw[1] in VOW:
        out.append(("g" + lw[1:], "S"))
    if lw[:1] == "l":
        out.append(("g" + lw, "S"))          # gl- > l-
    if lw[:1] in VOW and not lw.startswith("y"):
        out.append(("rh" + lw, "S"))          # a softened rh lost after a consonant (in a compound)
    return out


def unnasalise(w):
    lw = w.lower()
    out = []
    if lw.startswith("b"):
        out.append(("p" + lw[1:], "N"))
    elif lw.startswith("d") and not lw.startswith("dh"):
        out.append(("t" + lw[1:], "N"))
    elif lw.startswith("g"):
        out.append(("k" + lw[1:], "N"))
    elif lw.startswith("m"):
        out.append(("b" + lw[1:], "N"))
        if lw[1:2] and lw[1] in "aou":
            out.append((lw[1:], "N"))
    elif lw.startswith("n"):
        out += [("d" + lw[1:], "N"), ("g" + lw[1:], "N")]
        if lw[1:2] and (lw[1] in "eiy" or lw[1:3] == "ae"):
            out.append((lw[1:], "N"))
    return out


# ======================================================================= word-building (§3.2, §5.12)
HARMONIC = {  # suffix code: (broad, slender)
    "Ath": ("ath", "eth"), "Ol": ("ol", "yl"), "At": ("at", "et"), "Ard": ("ard", "erd"),
    "Oth": ("oth", "yth"), "Ast": ("ast", "est"),
    "Om": ("om", "ym"), "An": ("an", "en"), "A": ("a", "e"), "Ar": ("ar", "er"), "Os": ("os", "ys"),
    "Ant": ("ant", "ent"),
}
PLAIN = {"el": "el", "an": "an", "en": "en", "ow": "ow", "a": "a", "ith": "ith"}
SUF_TAG = {"Ath": "PL", "Ol": "VN", "At": "PTCP", "Ard": "AG", "Oth": "ABST", "Ast": "ORD",
           "el": "SGV", "an": "COLL", "en": "OF", "ow": "PLACE", "a": "DU",
           "Om": "1SG", "ith": "2SG", "An": "1DU", "A": "3DU", "Ar": "1PL", "Os": "2PL", "Ant": "3PL",
           "imp": "IMP.PL"}
SUF_NAME = {"Ath": "plural", "Ol": "verbal noun", "At": "participle", "Ard": "agent", "Oth": "abstract",
            "Ast": "ordinal", "el": "singulative, 'little'", "an": "collective, 'the folk of'",
            "en": "'of, belonging to'", "ow": "place", "a": "the old dual / feminine"}


def attach(stem, code, cls=None):
    """stem + suffix, with harmony (by the stem's class, or a given one) and the vowel-final rules"""
    if code in HARMONIC:
        c = cls or word_class(stem)
        suf = HARMONIC[code][0 if c == "B" else 1]
    else:
        suf = PLAIN[code]
    s = stem
    lw = s.lower()
    if lw.endswith("ow"):
        pass
    elif lw[-1:] == "a" and len(full_vowels(lw)) > 1:
        # an old -ā stem (the dual, the feminine) drops its -a before a vowel suffix; broad
        s = s[:-1]
        if code in HARMONIC:
            suf = HARMONIC[code][0]
    elif lw[-1:] in "aeiouy" and suf[:1] in "aeiouy":
        s = s + "w"                           # pa + -ast > pawast
    return ck_join(s, suf)


def seam(mod, head):
    """a compound: modifier + softened head (§3.10, H5); a softened rh is lost after a consonant;
    three like consonants keep two (O5)"""
    h = soften(head).lower()
    m = mod
    if head.lower().startswith("rh") and m[-1:].lower() not in VOW:
        h = h[1:]
    w = m + h
    w = re.sub(r"(.)\1\1", r"\1\1", w)
    return w


def seam_misreads(mod, head):
    """a compound whose seam makes a letter pair the Book reads as one sound (t+h > th, d+h > dh,
    r+h > rh, a+e > ae, o+w > ow) would be misread: such a compound is not made"""
    h = soften(head).lower()
    a, b = mod[-1:].lower(), h[:1]
    return (a + b) in ("th", "dh", "rh", "ae", "ow")


def negate(w):
    """the prefix na- (+S)"""
    return "na" + soften(w).lower()


# ======================================================================= the grammar's small words
PARTICLES = {  # form: (gloss, mutation it causes)
    "et": ("the", None), "ul": ("in", "N"), "hy": ("from", "S"), "um": ("upon", "S"), "lo": ("at", "S"),
    "dem": ("until", "N"), "eth": ("and", None), "ell": ("or", None), "veth": ("but", None),
    "nath": ("NEG", "N"), "re": ("PST", "S"), "es": ("FUT", "N"), "ho": ("Q", "S"), "sa": ("REL", "S"),
    "somm": ("while", None), "amm": ("when", None), "cedh": ("who?", None), "vodh": ("what", None),
    "sy": ("this", None), "ull": ("that", None), "gor": ("every", "S"), "sost": ("self", None),
    "tul": ("yet", None), "pa": ("two", "S"),
    "en": ("my/I", "N"), "tho": ("your/you", "S"), "o": ("his/it", "S"), "ey": ("her/she", None),
    "olna": ("our two", "S"), "ol": ("our/we", "N"), "va": ("your(pl)", "N"), "sona": ("their two", "S"),
    "so": ("their/they", "S"),
    "el": ("is", None), "ew": ("was", None), "nel": ("is.not", None), "new": ("was.not", None),
}
POSSESSIVES = {"en", "tho", "o", "ey", "olna", "ol", "va", "sona", "so"}
MORTAR = {"et", "ul", "hy", "um", "lo", "dem", "eth", "ell", "veth", "re", "es", "ho", "sa", "sy", "ull",
          "gor", "sost", "en", "tho", "o", "ey", "olna", "ol", "va", "sona", "so", "el", "ew", "doss", "noss"}
# the conjugated prepositions (§3.6)
PREP_PERSON = {"m": "1SG", "th": "2SG", "": "3SG.M", "y": "3SG.F", "na": "1DU", "r": "1PL", "s": "2PL",
               "nt": "3PL", "nta": "3DU"}
PREP_FORMS = {}
for _p, _g in (("lo", "at"),):
    for _e, _t in PREP_PERSON.items():
        PREP_FORMS[_p + _e] = (_p, _g, _t)
for _p, _g in (("um", "upon"), ("ul", "in"), ("dem", "until"), ("hy", "from")):
    for _e, _t in (("om", "1SG"), ("oth", "2SG"), ("o", "3SG.M"), ("oy", "3SG.F"), ("ona", "1DU"),
                   ("or", "1PL"), ("os", "2PL"), ("ont", "3PL"), ("onta", "3DU")):
        PREP_FORMS[_p + _e] = (_p, _g, _t)
# the two "be" verbs (§3.4): irregular forms
BE_FORMS = {
    "doss": ("doss", "be", ""), "noss": ("doss", "be", "N"), "yal": ("gal", "be.PST", "S"),
    "gal": ("gal", "be.PST", ""),
    "el": ("el", "is", ""), "ew": ("ew", "was", ""), "nel": ("el", "is.not", ""), "new": ("ew", "was.not", ""),
}
for _e, _t in (("om", "1SG"), ("ith", "2SG"), ("an", "1DU"), ("a", "3DU"), ("ar", "1PL"), ("os", "2PL"),
               ("ant", "3PL")):
    BE_FORMS["doss" + _e] = ("doss", "be", "", _t)
    BE_FORMS["noss" + _e] = ("doss", "be", "N", _t)
    BE_FORMS["yal" + _e] = ("gal", "be.PST", "S", _t)

S_TRIGGERS = {k for k, v in PARTICLES.items() if v[1] == "S"} | {"na-"}
N_TRIGGERS = {k for k, v in PARTICLES.items() if v[1] == "N"}
PARTICLE_GLOSS = {
    "et": "the", "ul": "in(+N)", "hy": "from(+S)", "um": "upon(+S)", "lo": "at(+S)", "dem": "until(+N)",
    "eth": "and", "ell": "or", "veth": "but", "nath": "NEG(+N)", "re": "PST(+S)", "es": "FUT(+N)",
    "ho": "Q(+S)", "sa": "REL(+S)", "somm": "while", "amm": "when", "cedh": "who?", "vodh": "what",
    "sy": "this", "ull": "that", "gor": "every(+S)", "sost": "self", "tul": "yet", "pa": "two(+S)",
    "en": "my(+N)", "tho": "your(+S)", "o": "his/it(+S)", "ey": "her", "olna": "our.two(+S)",
    "ol": "our(+N)", "va": "your.PL(+N)", "sona": "their.two(+S)", "so": "their(+S)",
    "el": "is", "ew": "was", "nel": "is.not", "new": "was.not",
}


# ======================================================================= the lexicon
class Lexicon:
    def __init__(self, path=LEX):
        self.rows = []
        self.by_key = {}
        self.by_hal = {}
        self.hal_stems = {}
        if not os.path.exists(path):
            return
        with open(path, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar="\\")
            for r in rd:
                self.rows.append(r)
                form = r["orrowen"]
                if " " in form:
                    continue
                self.by_key.setdefault(nk(form), []).append(r)
                hal = (r.get("hal") or "").strip()
                if hal and " " not in hal:
                    hk = hal_key(hal)
                    self.by_hal.setdefault(hk, []).append(r)
                    st = hal_stem(hk)
                    if st:
                        self.hal_stems.setdefault(st, []).append(r)
        self.keys = sorted(self.by_key)

    def get(self, form):
        return self.by_key.get(nk(form), [])

    def is_pos(self, form, pos):
        return any(pos in (r["pos"] or "").split(",") or (r["pos"] or "").startswith(pos)
                   for r in self.get(form))


def hal_key(h):
    h = unicodedata.normalize("NFC", h.lower())
    return h.replace("c", "k")


def hal_stem(hk):
    for end in ("os", "is", "as", "ā", "a", "ū", "o", "e"):
        if hk.endswith(end) and len(hk) > len(end) + 1:
            return hk[: -len(end)]
    return None


def short_gloss(r):
    form = r.get("orrowen", "")
    if form.lower() in PARTICLE_GLOSS:
        return PARTICLE_GLOSS[form.lower()]
    pos = (r.get("pos") or "").split(",")
    if ("name" in pos or "loan" in pos) and "n" not in pos and form[:1].isupper():
        return form
    m = r.get("meanings") or ""
    m = re.sub(r"^\((?:v|n|adj|adv)\.\)\s*", "", m.strip())
    g = re.split(r"[;,:(]", m)[0].strip()
    g = re.sub(r"^(a|an|the|to) (?=\S)", "", g)
    g = re.sub(r"['\"]", "", g).strip()
    return g.replace(" ", ".") or form


# ======================================================================= analysis of one word
class Parse:
    def __init__(self, stem_row, stem, layers, mut, prefix=False, note="", harmony_ok=True, fixed=None):
        self.row = stem_row          # the lexicon row of the stem (or of the whole word)
        self.stem = stem
        self.layers = layers         # suffix codes, innermost first
        self.mut = mut               # None, 'S' or 'N'
        self.prefix = prefix         # the na- prefix
        self.note = note
        self.harmony_ok = harmony_ok
        self.fixed = fixed           # a suggested correct spelling (harmony)

    def score(self):
        s = len(self.layers) * 2 + (1 if self.mut else 0) + (2.5 if self.prefix else 0)
        s += 0 if self.harmony_ok else 5
        if self.row and self.row.get("source", "").startswith("canon"):
            s -= 0.5
        return s


SUFFIX_FORMS = []  # (surface, code, class or None)
for _c, (_b, _s) in HARMONIC.items():
    SUFFIX_FORMS.append((_b, _c, "B"))
    SUFFIX_FORMS.append((_s, _c, "S"))
for _c, _f in PLAIN.items():
    SUFFIX_FORMS.append((_f, _c, None))
SUFFIX_FORMS.append(("a", "imp", None))
SUFFIX_FORMS.sort(key=lambda x: -len(x[0]))

VERB_ENDINGS = {"Om", "ith", "An", "A", "Ar", "Os", "Ant", "imp"}
DERIV_OK = {"Ath", "Ol", "At", "Ard", "Oth", "Ast", "el", "an", "en", "ow", "a"}


def restore_stem(s):
    """a stripped stem back to a lexicon spelling: the dropped -a of an old ā-stem (essath < essa);
    the glide w after a vowel (pawast < pa)"""
    out = [s, s + "a"]
    if s.endswith("w") and s[-2:-1] in "aeiouy":
        out.append(s[:-1])
    return out


CANON_SLIPS = {
    # form: (stem, layers, mutation, note) -- the spec's own harmony slips, kept as canon (§15 item 12)
    "stellath": ("stell", ["Ath"], None, "the canon's broad -ath (Kethow Stellath), by the rule stelleth"),
    "glennol": ("clenn", ["Ol"], "N", "the canon's broad -ol (ul glennol), by the rule glennyl"),
    "rytom": ("ryt", ["Om"], None, "the canon's broad -om (Rytom um ...), by the rule rytym"),
}


def analyse_word(tok, lex, depth=0):
    """all parses of one word (mutation undone, suffixes undone); best first"""
    w = tok.lower().replace("’", "'")
    parses = []
    bases = [(w, None)] + unsoften(w) + unnasalise(w)
    seen = set()
    for base, mut in bases:
        if (base, mut) in seen:
            continue
        seen.add((base, mut))
        parses += strip_all(base, mut, lex, depth)
    parses.sort(key=lambda p: p.score())
    return parses


def strip_all(base, mut, lex, depth):
    out = []
    # 1. the whole word is in the lexicon
    for r in lex.get(base):
        out.append(Parse(r, base, [], mut))
    # 2. one or two suffix layers
    out += strip_layers(base, mut, lex, [], 0)
    # 3. the prefix na- (+S)
    if base.startswith("na") and len(base) > 3 and depth == 0:
        rest = base[2:]
        cands = [(rest, None)] + unsoften(rest)
        for b2, m2 in cands:
            for r in lex.get(b2):
                out.append(Parse(r, b2, [], mut, prefix=True))
            for p in strip_layers(b2, mut, lex, [], 0):
                p.prefix = True
                out.append(p)
    return out


def strip_layers(word, mut, lex, layers, level):
    out = []
    if level >= 3:
        return out
    for surf, code, cls in SUFFIX_FORMS:
        if not word.endswith(surf) or len(word) - len(surf) < 2:
            continue
        stem = word[: -len(surf)]
        new_layers = [code] + layers
        for st in restore_stem(stem):
            rows = lex.get(st)
            for r in rows:
                ok, fixed = harmony_check(st, r, code, cls, surf)
                if not layer_fits(r, code, layers):
                    continue
                out.append(Parse(r, st, new_layers, mut, harmony_ok=ok, fixed=fixed))
        # deeper: the stem itself derived (haskardath, kethyleth); only the stem as it stands
        if code in ("Ath", "Om", "ith", "An", "A", "Ar", "Os", "Ant", "a", "el", "an", "en", "Oth",
                    "At", "Ol", "Ard", "ow"):
            out += strip_layers(stem, mut, lex, new_layers, level + 1)
    return out


SUPPLETIVE = {"yal", "gal"}   # the suppletive past of doss (§3.4): person endings only, no participle or noun
SUPPLETIVE_FORMS = {"yala", "yalan", "yalant", "yalar", "yalith", "yalom", "yalos"}   # already inflected: no layer


def layer_fits(row, code, outer):
    pos = row.get("pos", "")
    orr = (row.get("orrowen") or "").lower()
    if orr in SUPPLETIVE_FORMS or (orr in SUPPLETIVE and (code not in VERB_ENDINGS or code == "imp" or outer)):
        return False                          # backtrans I.1: *yalatath* is S·galat-PL 'things', not 'was-PTCP-PL'
    if code in VERB_ENDINGS and "v" not in pos.split(",") and not pos.startswith("v"):
        return False
    if code == "a" and not any(p in pos.split(",") for p in ("n", "name")):
        return False                          # the old dual / feminine -a is a noun's
    if code in ("Om", "ith", "An", "A", "Ar", "Os", "Ant", "imp") and outer:
        return False
    return True


def harmony_check(stem, row, code, cls, surf):
    """a harmonic suffix must take the class of the stem (§3.2); the lexicon's own class wins"""
    if code not in HARMONIC:
        return True, None
    want = (row.get("class") or word_class(stem)).strip() or word_class(stem)
    if cls == want:
        return True, None
    right = HARMONIC[code][0 if want == "B" else 1]
    return False, stem + right


# ======================================================================= tokenising and the sentence
TOKEN_RE = re.compile(r"[A-Za-zÀ-ÿĀ-žŊŋ]+(?:['’][A-Za-zÀ-ÿĀ-žŊŋ]+)*|[.,;:!?…|—-]+")


def tokenise(text):
    return TOKEN_RE.findall(text)


class Word:
    def __init__(self, tok):
        self.tok = tok
        self.parses = []
        self.status = "OK"
        self.msgs = []
        self.sugg = []
        self.gloss = ""
        self.best = None
        self.kind = "word"


def analyse_text(text, lex, hal=False):
    toks = tokenise(text)
    if not hal and toks and all(t.isupper() or not t.isalpha() for t in toks if len(t) > 1) \
            and any(t.isalpha() and len(t) > 2 for t in toks):
        hal = True
    words = []
    for t in toks:
        wd = Word(t)
        if not t[0].isalpha():
            wd.kind = "punct"
            wd.gloss = t
            words.append(wd)
            continue
        if hal:
            analyse_hal(wd, lex)
        else:
            analyse_living(wd, lex)
        words.append(wd)
    if not hal:
        context_check(words, lex)
    return words


def analyse_living(wd, lex):
    t = wd.tok
    lw = t.lower().replace("’", "'")
    # the small words first: they are fixed forms
    if lw in PARTICLES and lex.get(lw):
        wd.kind = "particle"
        wd.best = Parse(lex.get(lw)[0], lw, [], None)
        wd.gloss = PARTICLE_GLOSS.get(lw, lw)
        return
    if lw in PREP_FORMS:
        p, g, per = PREP_FORMS[lw]
        wd.kind = "prep"
        wd.gloss = "%s-%s" % (g, per)
        wd.best = Parse(lex.get(p)[0] if lex.get(p) else None, p, [], None)
        return
    if lw in BE_FORMS or (lw[:1] in "dnyg" and lw in BE_FORMS):
        v = BE_FORMS[lw]
        wd.kind = "be"
        tag = ("-" + v[3]) if len(v) > 3 else ""
        wd.gloss = ("%s·" % v[2] if v[2] else "") + v[1] + tag
        wd.best = Parse(lex.get(v[0])[0] if lex.get(v[0]) else None, v[0], [], v[2] or None)
        return
    if "'" in lw:
        rows = lex.get(lw) or lex.get(lw.replace("'", ""))
        if rows:
            wd.best = Parse(rows[0], lw, [], None)
            wd.kind = "loan"
            wd.gloss = short_gloss(rows[0])
            return
    if lw in CANON_SLIPS and lex.get(CANON_SLIPS[lw][0]):
        st, lay, mut, note = CANON_SLIPS[lw]
        p = Parse(lex.get(st)[0], st, lay, mut)
        wd.parses = [p]
        wd.best = p
        wd.gloss = gloss_of(p)
        wd.msgs.append("a harmony slip the canon keeps: " + note)
        return
    ps = analyse_word(lw, lex)
    wd.parses = ps
    if not ps:
        wd.status = "UNKNOWN"
        bad = re.findall(r"[zxqj]", lw)
        if bad:
            wd.status = "ILL-FORMED"
            wd.msgs.append("not an Orrowen word: the tongue has no %s (§2.5)" % ", ".join(sorted(set(bad))))
        elif re.search(r"(ion|iel|dor)$", lw):
            wd.status = "ILL-FORMED"
            wd.msgs.append("not an Orrowen word: the endings -ion, -iel, -dor are banned (§2.5)")
        wd.sugg = suggest(lw, lex)
        wd.gloss = "?" + t
        return
    good = [p for p in ps if p.harmony_ok]
    wd.best = good[0] if good else ps[0]
    if not good:
        wd.status = "ILL-FORMED"
        p = ps[0]
        wd.msgs.append("harmony: the suffix does not take the class of the stem %s (%s)" %
                       (p.stem, p.row.get("class") or word_class(p.stem)))
        if p.fixed:
            wd.sugg.append(recase(t, rebuild_fixed(p)))
    wd.gloss = gloss_of(wd.best)


def rebuild_fixed(p):
    w = p.stem
    cls = (p.row.get("class") or word_class(p.stem)).strip() or word_class(p.stem)
    for code in p.layers:
        if code == "imp":
            w = w + "a"
        else:
            w = attach(w, code, cls if code in HARMONIC else None)
    if p.prefix:
        w = negate(w)
    if p.mut == "S":
        w = soften(w)
    elif p.mut == "N":
        w = nasalise(w)
    return w


def gloss_of(p):
    if p is None:
        return "?"
    g = short_gloss(p.row) if p.row else p.stem
    tags = []
    for code in p.layers:
        tags.append(SUF_TAG.get(code, code))
    out = g + "".join("-" + t for t in tags)
    if p.prefix:
        out = "un-" + out
    if p.mut:
        out = p.mut + "·" + out
    return out


def context_check(words, lex):
    """the mutation a word shows must be the one the word before it asks for (§3.3)"""
    prev = None
    prevprev = None
    for i, wd in enumerate(words):
        if wd.kind == "punct":
            prev, prevprev = None, None
            continue
        if wd.status == "UNKNOWN" or wd.best is None:
            prevprev, prev = prev, wd
            continue
        want = None
        trig = None
        if prev is not None and prev.kind in ("particle",):
            pl = prev.tok.lower()
            want = PARTICLES.get(pl, (None, None))[1]
            trig = pl
        if want and wd.kind == "word":
            # the readings the trigger allows: the mutation it asks for, or no mutation on a letter it
            # cannot change; after a verbal particle a verb is preferred, after a nominal one a noun
            def ok_after(p):
                if not p.harmony_ok:
                    return False
                if p.mut == want:
                    return True
                first = "na" if p.prefix else p.stem
                return p.mut is None and (soften(first) if want == "S" else nasalise(first)).lower() == first.lower()
            cands = [p for p in wd.parses if ok_after(p)]
            if cands:
                if trig in VERBAL_TRIGGERS:
                    pref = [p for p in cands if row_has(p, ("v",))]
                else:
                    pref = [p for p in cands if row_has(p, ("n", "adj", "name", "num", "pron", "loan"))]
                # when both readings fit, the one that shows the asked-for mutation wins: a base form that
                # sounds like a mutated word is the accident, the trigger is the grammar (nath mosk < bosk)
                pick = min(pref or cands, key=lambda p: (0 if p.mut == want else 1, p.score()))
                if pick is not wd.best:
                    wd.best = pick
                    wd.gloss = gloss_of(pick)
        got = wd.best.mut if wd.kind not in ("particle",) else None
        first = "na" if wd.best.prefix else wd.best.stem
        if want:
            changed = (soften(first) if want == "S" else nasalise(first)).lower() != first.lower()
        else:
            changed = False
        base_initial_mutable = changed
        if wd.kind == "be" and wd.best.mut:
            got = wd.best.mut
            base_initial_mutable = True
        if want and got != want and base_initial_mutable and wd.kind not in ("particle", "prep"):
            if trig in ("o", "en", "ol", "va", "so", "tho", "ey") and is_verbish(wd, lex):
                pass  # a pronoun after a verb, then a new clause: no mutation is asked
            elif got is None:
                right = soften(wd.tok) if want == "S" else nasalise(wd.tok)
                wd.status = "ILL-FORMED" if wd.status == "OK" else wd.status
                wd.msgs.append("'%s' asks for %s after it (%s); expected '%s'" %
                               (trig, "softening (S)" if want == "S" else "nasalising (N)", trig, right))
                wd.sugg.insert(0, right)
            else:
                # a different mutation: look for a parse with the wanted one
                alt = [p for p in wd.parses if p.mut == want and p.harmony_ok]
                if alt:
                    wd.best = alt[0]
                    wd.gloss = gloss_of(alt[0])
                else:
                    wd.status = "ILL-FORMED" if wd.status == "OK" else wd.status
                    wd.msgs.append("'%s' asks for %s, but the word shows %s" % (trig, want, got))
        elif got and not want:
            # a mutation with no trigger: fine in a construct (a noun before it), a compound, a
            # vocative, or after a dual; otherwise prefer an unmutated parse, or flag it
            unmut = [p for p in wd.parses if p.mut is None and p.harmony_ok]
            if unmut:
                wd.best = unmut[0]
                wd.gloss = gloss_of(unmut[0])
            elif got == "S" and prev is not None and prev.kind == "word" and prevprev is not None \
                    and prevprev.tok.lower() == "pa":
                wd.msgs.append("softened after a dual (§3.3)")
            elif prev is not None and prev.kind in ("word", "loan") and is_nounish(prev, lex):
                wd.msgs.append("softened as a possessor (the construct, §3.2)" if got == "S" else
                               "nasalised with no trigger before it")
                if got == "N":
                    wd.status = "ILL-FORMED" if wd.status == "OK" else wd.status
            elif got == "S" and (prev is None or prev.kind == "punct"):
                wd.msgs.append("softened with no trigger (a vocative?)")
            else:
                wd.status = "ILL-FORMED" if wd.status == "OK" else wd.status
                wd.msgs.append("%s with no trigger before it" % ("softened" if got == "S" else "nasalised"))
                wd.sugg.insert(0, recase(wd.tok, wd.best.stem))
        # an epithet after a name is a construct (§3.10): when the plain reading wins, name the softened
        # possessor's reading too, which a homophone can hide (backtrans I.1: Pellow Vell, S·pell 'spire',
        # not vell 'song')
        if prev is not None and prev.best is not None and prev.best.row is not None \
                and "name" in (prev.best.row.get("pos") or "").split(",") and wd.tok[:1].isupper() \
                and wd.best.mut is None and not want:
            alt = [p for p in wd.parses if p.mut == "S" and p.harmony_ok and p.row is not None
                   and p.stem != wd.best.stem]
            if alt:
                wd.msgs.append("or, as an epithet construct after a name, S·%s '%s' (the possessor softened, "
                               "§3.10)" % (alt[0].stem, short_gloss(alt[0].row)))
        # the Last Carver's error: an article on the head of a construct (§3.2, §11.9)
        prevprev, prev = prev, wd
    # -a on a broad verb: the 3du has a subject after it; with none, it is the imperative plural (§3.4)
    for i, wd in enumerate(words):
        if wd.best is not None and wd.best.layers[-1:] in (["A"], ["imp"]) and wd.kind == "word":
            nxt = words[i + 1] if i + 1 < len(words) else None
            subj = nxt is not None and nxt.kind in ("word", "loan") and nxt.tok[:1].isupper() and \
                nxt.best is not None and nxt.best.row is not None and "name" in (nxt.best.row.get("pos") or "")
            want = "A" if subj else "imp"
            if wd.best.layers[-1] != want:
                alt = [p for p in wd.parses if p.layers[-1:] == [want] and p.stem == wd.best.stem]
                if alt:
                    wd.best = alt[0]
                    wd.gloss = gloss_of(alt[0])
    for i in range(len(words) - 3):
        a, b, c, d = words[i:i + 4]
        if a.tok.lower() == "et" and b.kind == "word" and c.kind == "particle" and c.tok.lower() in POSSESSIVES \
                and d.kind == "word":
            b.msgs.append("the article on the head of a construct: '%s %s' is the foreigner's error "
                          "(the Last Carver's word too many, §11.9); say '%s %s %s'" %
                          (a.tok, b.tok, b.tok, c.tok, d.tok))
            if b.status == "OK":
                b.status = "ILL-FORMED"


VERBAL_TRIGGERS = {"re", "es", "nath", "ho", "sa"}


def row_has(p, poss):
    if p.row is None:
        return False
    rp = (p.row.get("pos") or "").split(",")
    if p.layers and p.layers[-1] in ("Ol", "Ard", "Oth", "Ath", "el", "an", "ow"):
        rp = ["n"]
    elif p.layers and p.layers[-1] in ("At", "en"):
        rp = ["adj"]
    elif p.layers and p.layers[-1] in ("Om", "ith", "An", "A", "Ar", "Os", "Ant", "imp"):
        rp = ["v"]
    return any(x in rp for x in poss)


def is_verbish(wd, lex):
    return wd.best is not None and wd.best.row is not None and "v" in (wd.best.row.get("pos") or "").split(",")


def is_nounish(wd, lex):
    if wd.best is None or wd.best.row is None:
        return wd.kind == "loan"
    pos = (wd.best.row.get("pos") or "")
    return any(x in pos.split(",") for x in ("n", "name", "loan")) or wd.best.layers[-1:] in (["Ol"], ["Ath"])


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def suggest(w, lex, n=4):
    out = []
    for base, mut in [(w, None)] + unsoften(w) + unnasalise(w):
        if lex.get(base):
            out.append(base)
    k = nk(w)
    close = difflib.get_close_matches(k, lex.keys, n=12, cutoff=0.6)
    close.sort(key=lambda c: (lev(k, c), abs(len(c) - len(k)), -difflib.SequenceMatcher(None, k, c).ratio()))
    for c in close:
        r = lex.by_key[c][0]
        out.append(r["orrowen"])
    seen, res = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            res.append(s)
    return res[:n]


# ======================================================================= the Hal
HAL_END = [("athi", "PL"), ("ola", "VN"), ("ana", "1DU"), ("ant", "3PL"), ("om", "1SG"), ("ith", "2SG"),
           ("ar", "1PL"), ("us", "2PL"), ("os", "NOM/3SG"), ("is", "NOM/3SG"), ("ā", "DU"), ("a", ""),
           ("ū", "PLACE")]


def analyse_hal(wd, lex):
    hk = hal_key(wd.tok)
    rows = lex.by_hal.get(hk)
    if rows:
        wd.best = Parse(rows[0], hk, [], None)
        wd.gloss = short_gloss(rows[0]) + hal_tag(hk, rows[0])
        wd.kind = "hal"
        return
    for end, tag in HAL_END:
        if hk.endswith(end) and len(hk) > len(end) + 1:
            st = hk[: -len(end)]
            rows = lex.hal_stems.get(st)
            if rows:
                wd.best = Parse(rows[0], st, [], None)
                wd.gloss = short_gloss(rows[0]) + ("-" + tag if tag else "")
                wd.kind = "hal"
                return
    wd.status = "UNKNOWN"
    wd.gloss = "?" + wd.tok
    close = difflib.get_close_matches(hk, list(lex.by_hal), n=3, cutoff=0.7)
    wd.sugg = [lex.by_hal[c][0]["hal"] for c in close]


def hal_tag(hk, row):
    pos = row.get("pos") or ""
    if hk.endswith(("os", "is")) and "v" in pos.split(","):
        return "-3SG"
    if hk.endswith(("os", "is")) and "n" in pos.split(","):
        return "-NOM"
    return ""


# ======================================================================= set phrases (--gloss)
PHRASE_EQUIV = {"doss": {"doss", "gal", "yal", "noss"}}   # the state verb, in its past and its negative


def word_keys(wd):
    """every form a word may stand for in a set phrase: as written, its stem, its lexicon row"""
    ks = {nk(wd.tok)}
    b = wd.best
    if b is not None:
        if b.stem:
            ks.add(nk(b.stem))
        if b.row is not None and b.row.get("orrowen"):
            ks.add(nk(b.row["orrowen"]))
    return ks


def phrase_hints(words, lex):
    """The lexicon's set phrases (its entries of two or more words) found in a line, as (form, meanings).
    A two-word phrase must stand together; a longer one may have at most two words in each gap, which are an idiom's
    slots (re yal maver o wrodhol um Halyna is doss maver um, "must"). A phrase never runs across punctuation.
    Added by the IV.4 back-translation (wf7/backtrans_IV4.md): the gloss showed only single words, and a reader
    took maver for "wish" where the idiom says "must"."""
    if not hasattr(lex, "_phrases"):
        lex._phrases = [(tuple(nk(x) for x in r["orrowen"].split()), r) for r in lex.rows
                        if " " in (r.get("orrowen") or "").strip()]
    segs, cur = [], []
    for wd in words:
        if wd.kind == "punct":
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append(word_keys(wd))
    if cur:
        segs.append(cur)

    def fits(w, ks):
        return w in ks or bool(ks & PHRASE_EQUIV.get(w, set()))

    def match(seg, ph, i, j, gap):
        if j == len(ph):
            return True
        for k in range(i, min(len(seg), i + gap + 1)):
            if fits(ph[j], seg[k]) and match(seg, ph, k + 1, j + 1, gap):
                return True
        return False

    out, seen = [], set()
    for ph, r in lex._phrases:
        gap = 0 if len(ph) == 2 else 2
        for seg in segs:
            if any(fits(ph[0], seg[s]) and match(seg, ph, s + 1, 1, gap) for s in range(len(seg))):
                if r["orrowen"] not in seen:
                    seen.add(r["orrowen"])
                    out.append((r["orrowen"], r["meanings"]))
                break
    return out


# ======================================================================= output
def report(words, out=sys.stdout):
    bad = 0
    for wd in words:
        if wd.kind == "punct":
            continue
        line = "  %-14s %-10s %s" % (wd.tok, wd.status, wd.gloss)
        if wd.best is not None and wd.best.row is not None and wd.status != "UNKNOWN":
            line += "   [%s]" % wd.best.row.get("orrowen", "")
        out.write(line + "\n")
        for m in wd.msgs:
            out.write("      - %s\n" % m)
        if wd.sugg:
            out.write("      suggest: %s\n" % ", ".join(wd.sugg))
        if wd.status != "OK":
            bad += 1
    return bad


def gloss_lines(words):
    toks, gls = [], []
    for wd in words:
        if wd.kind == "punct":
            if toks:
                toks[-1] += wd.tok
                gls[-1] += wd.tok if wd.tok not in (",",) else ""
            continue
        g = wd.gloss + ("" if wd.status == "OK" else "{%s}" % wd.status.lower())
        w = max(len(wd.tok), len(g))
        toks.append(wd.tok.ljust(w))
        gls.append(g.ljust(w))
    return "  ".join(toks).rstrip(), "  ".join(gls).rstrip()


# ======================================================================= the samples of orrowen_v2.md
def v2_samples():
    """every sample text of orrowen_v2.md: §11's quoted texts (living and Hal), the phrasebook,
    the §3 grammar examples, §3.7's idiom table and §14a's plea"""
    path = os.path.join(HERE, "orrowen_v2.md")
    txt = open(path, encoding="utf-8").read()
    out = []
    s11 = txt.split("## 11 · SAMPLE TEXTS")[1].split("## 12 ·")[0]
    for m in re.finditer(r"^> \*\*(.+?)\*\*", s11, re.M):
        line = m.group(1)
        line = re.sub(r"\(Hal:.*?\)", "", line).strip()
        line = re.sub(r"⟨.*?⟩", "", line).strip()
        out.append(("§11 " + line[:40], line, line.isupper() or line.split()[0].isupper() and len(line.split()[0]) > 2))
    for m in re.finditer(r"\(Hal: \*(.+?)\*", s11):
        out.append(("§11 Hal", m.group(1), True))
    # the phrasebook (§11.11), first column
    pb = s11.split("### 11.11")[1]
    for m in re.finditer(r"^\| \*(.+?)\*(?: · \*(.+?)\*)? \|", pb, re.M):
        for g in m.groups():
            if g:
                out.append(("§11.11", g, False))
    # §3 examples: the interlinear-ready italics that are whole Orrowen phrases
    s3 = txt.split("## 3 · GRAMMAR")[1].split("## 4 ·")[0]
    for ex in GRAMMAR_EXAMPLES:
        if ex in s3:
            out.append(("§3", ex, False))
        else:
            out.append(("§3 (not found!)", ex, False))
    s14 = txt.split("## 14 · CONTACT POINTS")[1]
    m = re.search(r"\*\*\*(Hess\. .+?)\*\*\*", s14)
    if m:
        out.append(("§14a", m.group(1), False))
    return out


GRAMMAR_EXAMPLES = [
    "Keth et tolm", "Carm et lodh hy et trun", "et gunn sy", "hosk et ganna", "sull carm", "delv vennuld",
    "El et tolm sa heth", "pa yarl", "pa dholm", "tolmath", "theldeth", "Hosk et ganna", "garl Dhrenn",
    "lest Vardh", "Kethow Dhresk", "tumol ol varn", "pa yarl dhevel", "tumar", "re dhumar", "re heth",
    "es dumar", "es geth", "nath dumar", "nath geth", "ho dhumos?", "ho heth?", "tum!", "tuma!", "keth!",
    "ketha!", "tumol", "kethyl", "tumat", "kethet", "tumard", "Ketherd", "Ho dhumos?", "Tumar",
    "Nath dumar", "Doss et hald ul glennol", "re yal", "re yalar", "es noss", "nath noss",
    "El tolm et hald", "Somm el tolm tolm", "Tumar ol", "Re hadhan o", "Doss tolm lom.",
    "Doss kethyl et tolm lom.", "Doss lomm umom.", "Re hethe Halyna et mesk.", "nath geth", "nawrodhat",
    "nadhum", "nayald", "nalodhat", "et tolm sa heth", "Voss sa re vess", "Tuma Halyna", "Rytom um hosk",
    "Ston.", "Stonos", "Rhyna Yanna Ulvenn", "Kael Nydherd", "Halvard Tolmvard", "Halyna", "Aldwena",
    "Idrenna",
]


EXPECTED_ERRORS = {"Ul et dumol ol varn, ol theldeth…": "the Last Carver's inscription: the article on a construct "
                   "head, and the Title's nasal bite copied after it (§11.9, §6.13: his tells)"}


def run_tests(lex):
    total = bad = 0
    seen = set()
    for where, text, hal in v2_samples():
        if text in seen:
            continue
        seen.add(text)
        words = analyse_text(text, lex, hal=hal)
        t, g = gloss_lines(words)
        nbad = sum(1 for w in words if w.kind != "punct" and w.status != "OK")
        mark = "ok " if nbad == 0 else "!! "
        print("%s[%s] %s" % (mark, where, text))
        print("      %s\n      %s" % (t, g))
        for wd in words:
            for m in wd.msgs:
                print("      - %s: %s" % (wd.tok, m))
            if wd.status != "OK" and wd.sugg:
                print("      - %s: suggest %s" % (wd.tok, ", ".join(wd.sugg)))
        total += 1
        if nbad and text in EXPECTED_ERRORS:
            print("      (expected: %s)" % EXPECTED_ERRORS[text])
        elif nbad:
            bad += 1
    return total, bad


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description="Check and gloss romanised Orrowen against the tier-3 lexicon.")
    ap.add_argument("text", nargs="*", help="Orrowen text (or use --file)")
    ap.add_argument("--gloss", action="store_true", help="print a word-by-word gloss")
    ap.add_argument("--hal", action="store_true", help="read the old register (the Hal)")
    ap.add_argument("--file", help="read the text from a file, one line at a time")
    ap.add_argument("--lexicon", default=LEX, help="the lexicon TSV (default: lexicon_orrowen.tsv)")
    ap.add_argument("--test", action="store_true", help="analyse every sample of orrowen_v2.md")
    a = ap.parse_args(argv)
    lex = Lexicon(a.lexicon)
    if not lex.rows:
        print("no lexicon at %s" % a.lexicon)
        return 2
    if a.test:
        total, bad = run_tests(lex)
        print("\n%d samples, %d with a word reported (besides the expected ones)" % (total, bad))
        return 0 if bad == 0 else 1
    lines = []
    if a.file:
        lines = [l.rstrip("\n") for l in open(a.file, encoding="utf-8") if l.strip()]
    if a.text:
        lines.append(" ".join(a.text))
    if not lines:
        lines = [l.rstrip("\n") for l in sys.stdin if l.strip()]
    nbad = 0
    for line in lines:
        words = analyse_text(line, lex, hal=a.hal)
        if a.gloss:
            t, g = gloss_lines(words)
            print(t)
            print(g)
            for form, mean in phrase_hints(words, lex):
                print("  = %s: %s" % (form, mean))
            for wd in words:
                for m in wd.msgs:
                    print("  - %s: %s" % (wd.tok, m))
                if wd.status != "OK" and wd.sugg:
                    print("  - %s: suggest %s" % (wd.tok, ", ".join(wd.sugg)))
            print()
        else:
            print(line)
            nbad += report(words)
    return 0 if nbad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
