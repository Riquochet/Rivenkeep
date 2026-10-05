"""Build the tier-3 Orrowen lexicon (scratch tool, wf7/lex).

    python3 build_lexicon.py            -> ../lexicon_orrowen.tsv, coverage_en.tsv, stats.json

Inputs: base.py (canon + reserve + word-signs, all read-only), en_map/*.txt (the Book's English
lemmas and the Orrowen recipe for each), lemmas.tsv / names.tsv / compounds.tsv (extract_lemmas.py).
The morphology is orr_analyze.py's, so the words are made by the same rules the analyzer undoes.
"""
import os, re, sys, json, csv, glob
from collections import OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WF7 = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, WF7)
import base                     # noqa: E402
import orr_analyze as M         # noqa: E402

OUT_TSV = os.path.join(WF7, "lexicon_orrowen.tsv")
COLS = ["id", "orrowen", "hal", "pos", "class", "meanings", "canon_sense", "derivation", "root", "formation",
        "logogram", "dry_cut", "source", "book_lemmas"]

SIGNS = base.signs()
RESERVE = base.reserve()
V2 = base.v2_tables()

BANNED_END = re.compile(r"(ion|iel|dor)$")
BANNED_LET = re.compile(r"[zxqj]")

COMPLEMENT = {"Ath": "A.th", "Ol": "O.l", "At": "A.t", "Ard": "A.r.d", "Oth": "O.th", "Ast": "A.s.t",
              "el": "e.l", "an": "a.n", "en": "e.n", "ow": "o.w", "a": "a"}
NUMERAL = {"hos": "h", "pa": "p", "sull": "s", "gemm": "g", "lesk": "l", "vran": "v", "dhom": "dh",
           "thell": "th", "rost": "r", "noth": "n", "delv": "d", "murr": "m", "bost": "b"}
TURNED = {"nath", "na", "nel", "new", "na-"}
NUMERAL_KEYS = {"hos": "h", "pa": "p", "sull": "s", "gemm": "g", "lesk": "l", "vran": "v", "dhom": "dh",
                "thell": "th", "rost": "r", "noth": "n", "delv": "d", "murr": "m", "bost": "b"}
COMPOUND_NUMERALS = {"hosnoth": "nh", "sullnoth": "ns", "gemmnoth": "ng", "lesknoth": "nl", "vrannoth": "nv",
                     "dhomnoth": "ndh", "thellnoth": "nth", "rostnoth": "nr"}


class E:
    def __init__(self, form, pos="", cls=None, source="", hal=""):
        self.form = form
        self.key = M.nk(form)
        self.hal = hal
        self.pos = []
        self.add_pos(pos)
        self.cls = cls or M.word_class(form)
        self.canon = ""
        self.senses = []
        self.derivation = ""
        self.roots = []
        self.formation = ""
        self.source = source
        self.lemmas = []
        self.sign = None          # the word-sign of this very word
        self.base = None          # the entry it is derived from (for the dry cut)
        self.codes = []           # suffix codes on the base
        self.neg = False
        self.parts = []           # compound parts (entries)
        self.phrase = False
        self.flag = ""
        self.harm_letters = []    # suffix codes whose vowel is harmonic (for letters)
        self.pos_senses = defaultdict(list)   # the tier-3 senses, by part of speech

    def add_pos(self, p):
        for x in re.split(r"[,/ ]+", p or ""):
            x = x.strip()
            if x and x not in self.pos:
                self.pos.append(x)

    def add_sense(self, s):
        s = s.strip().replace('"', "'")
        if not s:
            return
        low = s.lower()
        allsense = (self.canon + "; " + "; ".join(self.senses)).lower()
        # A sense is already said when its words stand whole, outside brackets, in a sense the entry has. One seen
        # only inside another sense's brackets, or only as part of a longer word, is not: "water" is not said by
        # "a spring (of water)", nor "cap" by "capstone" (the IV.4 back-translation, wf7/backtrans_IV4.md).
        bare = re.sub(r"\([^)]*\)", "", allsense)

        def said(x):
            return bool(x) and re.search(r"(?<![a-z'])" + re.escape(x) + r"(?![a-z'])", bare) is not None
        if said(low):
            return
        low_bare = re.sub(r"\([^)]*\)", "", low).strip(" ;,")
        if low_bare != low and said(low_bare) and all(b in allsense for b in re.findall(r"\([^)]*\)", low)):
            return
        head = re.split(r"[;(]", low)[0].strip()
        if head and any(x.strip().startswith(head) for x in re.split(r";", allsense) if x.strip()):
            rest = low[len(head):].strip(" ;")
            if not rest or rest in allsense:
                return
        self.senses.append(s)

    def meanings(self):
        out = [self.canon] if self.canon else []
        out += self.senses
        return "; ".join(x for x in out if x)


ENTRIES = OrderedDict()
ERRORS = []


def put(e):
    if e.key in ENTRIES:
        raise KeyError(e.key)
    ENTRIES[e.key] = e
    return e


def get(form):
    return ENTRIES.get(M.nk(form))


# ======================================================================= 1. the base inventory
POS_CANON = {
    # canon words whose part of speech the tables give only in prose
    "tolm": "n", "hal": "n", "hald": "n", "lodh": "n", "trenn": "n", "cadh": "v", "ston": "v", "gald": "v",
    "gal": "v", "clenn": "adj,v", "stann": "v", "bresk": "n", "drunn": "n", "gann": "n", "ganna": "n",
    "hosk": "n,v", "gorn": "n", "keth": "v", "kethow": "n", "tresk": "n,v", "lest": "n", "cumm": "n",
    "stell": "n", "pell": "n", "ryt": "n,v", "prass": "n", "hemm": "adj,n", "hemma": "n", "mardh": "name",
    "ammel": "v", "ammad": "v", "tev": "n", "voll": "n", "tunn": "adj", "grest": "n", "par": "v,n",
    "pard": "n", "odh": "n", "odha": "n", "theld": "n", "varn": "n", "gedh": "n", "uld": "n", "essa": "n",
    "lunt": "n", "orr": "v", "orrow": "n,name", "arra": "n", "gebb": "n", "lumm": "v", "vall": "v",
    "osk": "v,n", "tesk": "n", "sost": "pron,adv", "crenn": "n", "hesp": "n", "kest": "n", "bramm": "n",
    "hask": "v", "gomm": "n", "carm": "n,v", "pedh": "n", "trun": "n", "marr": "v", "kyl": "v", "lusk": "v",
    "bosk": "v", "hurr": "v", "gorr": "v", "covv": "n", "sceth": "n", "wemm": "n", "wadh": "n",
    "myst": "n,adj", "mesk": "n", "lurr": "n", "helv": "n", "hyll": "n", "rhull": "n", "sedh": "n",
    "nell": "n", "tav": "v", "tavow": "n", "sorth": "n", "brunn": "n", "grull": "n", "sirr": "n",
    "crest": "n", "frenn": "n", "sulv": "n,adj", "grem": "n", "vorr": "n", "orl": "n", "vess": "n",
    "clem": "n", "surr": "n", "cemm": "v,n", "garl": "n", "molt": "n", "hoss": "n", "lorr": "n,adj",
    "senn": "v", "hess": "v", "lomm": "n", "sol": "v", "sollan": "n", "lunn": "n", "tum": "v", "tumol": "n",
    "brod": "n", "brodh": "v", "vesk": "v", "flenn": "n", "luth": "n", "brenth": "n", "vell": "n",
    "sesk": "v", "nydh": "v", "kael": "n,name", "pess": "v", "tess": "v", "tessen": "v", "doss": "v",
    "el": "v", "ew": "v", "darr": "v", "hunn": "v", "hebb": "v", "tovv": "v", "omm": "v", "cresk": "v",
    "ser": "v", "rhyn": "v", "strom": "adj", "lyss": "adj", "gell": "adj", "venn": "adj", "gunn": "adj,n",
    "sell": "adj", "domm": "adj", "bell": "adj,n", "lenn": "adj,n", "taldow": "n", "tald": "v",
    "et": "art", "ul": "prep", "hy": "prep", "um": "prep", "lo": "prep", "dem": "prep", "eth": "conj",
    "ell": "conj", "veth": "conj", "na": "pref", "nath": "part", "re": "part", "es": "part", "ho": "part",
    "sa": "pron", "somm": "conj", "amm": "conj", "cedh": "pron", "vodh": "pron", "sy": "det", "ull": "det",
    "gor": "det", "tul": "adv", "dask": "n", "en": "pron", "tho": "pron", "o": "pron", "ey": "pron",
    "ol": "pron", "olna": "pron", "va": "pron", "so": "pron", "sona": "pron", "hos": "num", "pa": "num",
    "pana": "det", "rost": "num", "sull": "num", "gemm": "num", "lesk": "num", "vran": "num",
    "dhom": "num", "thell": "num", "noth": "num", "delv": "num", "murr": "num", "bost": "num",
}
POS_RESERVE = {
    "fear": "n,v", "freeze": "adj,v", "tear": "n,v", "sleep": "n,v", "key": "n,v", "ear": "n,v",
    "nose": "n,v", "raft": "n,v", "stair": "n,v", "promise": "n,v", "order": "n,v", "lie": "n,v",
    "think": "v,n", "doubt": "v,n", "hope": "n,v", "shame": "n", "pride": "n", "joy": "n", "mercy": "n",
    "forgive": "v", "bless": "v", "endure": "n,v", "hate": "n,v", "courage": "n", "anoint": "v",
    "praise": "n,v", "lot": "n", "mind": "n", "believe": "v", "understand": "v", "learn": "v",
    "wonder": "v,n", "say": "v", "shout": "v", "whisper": "v", "warn": "v,n", "scream": "n,v",
    "plan": "n", "obey": "v", "signal": "n", "yield": "v", "defend": "v", "wish": "v,n", "choose": "v",
    "seek": "v", "pay": "v,n", "buy": "v", "sell": "v", "trade": "v,n", "measure": "v", "polish": "v",
    "sail": "v", "row": "v", "wake": "v", "eat": "v", "drink": "v", "sweat": "n", "flee": "v", "chase": "v",
    "ambush": "v", "fill": "v,adj", "empty": "adj", "play": "v,n", "lead": "v", "follow": "v",
    "tend": "v", "guide": "v", "rise": "v", "lower": "v", "cut": "v", "hew": "v", "wash": "v",
    "swim": "v", "drown": "v", "begin": "v", "return": "v", "watch": "v", "touch": "v", "feel": "v",
    "bowdown": "v", "sow": "v", "reap": "v", "prune": "v", "fell": "v", "arrive": "v", "dance": "v",
    "skip": "v", "catch": "v", "tie": "v", "weave": "v", "sew": "v", "dig": "v", "bury": "v",
    "cover": "v", "hide": "v", "find": "v", "lose": "v", "bring": "v", "save": "v", "spare": "v",
    "spend": "v", "cut ": "v", "pour": "v", "kindle": "v", "quench": "v", "liedown": "v", "climb": "v",
    "haul": "v", "pull": "v", "push": "v", "lift": "v", "throw": "v", "sit": "v", "laugh": "v",
    "wake ": "v",
}


def reserve_pos(r):
    k = r["key"]
    if k in POS_RESERVE:
        return POS_RESERVE[k]
    m = r["mean"]
    if r["field"] == "quality":
        return "adj"
    if r["field"] == "acts":
        return "v"
    if re.match(r"(a|an|the|one) ", m) or r["field"] in ("stone", "sea", "sky", "body", "hearth", "war"):
        if "; to " in m:
            return "n,v"
        return "n"
    return "n"


def clean_md(s):
    return re.sub(r"\*+", "", s or "").strip()


CANON_SENSES = defaultdict(list)
FORMATION_PARTS = {}
SUFCODE = {"-ath": "Ath", "-ol": "Ol", "-at": "At", "-ard": "Ard", "-oth": "Oth", "-el": "el", "-an": "an",
           "-en": "en", "-ow": "ow", "-ast": "Ast", "-a": "a", "-ar": None, "-aer": None, "-i": None}


def link_formations():
    """a canon formation's parts, as entries: its base and suffixes, its prefix, or its compound parts"""
    for k, parts in FORMATION_PARTS.items():
        e = ENTRIES[k]
        if e.phrase:
            continue
        if parts[0] == "na-" or parts[0] == "na":
            e.neg = True
            parts = parts[1:]
        words = [p for p in parts if not p.startswith("-")]
        sufs = [p for p in parts if p.startswith("-")]
        if len(words) == 1 and all(SUFCODE.get(s) for s in sufs):
            b = get(words[0])
            if b is not None and b is not e:
                e.base = b
                e.codes = [SUFCODE[s] for s in sufs]
                e.harm_letters = [c for c in e.codes if c in M.HARMONIC]
        elif len(words) > 1 and not sufs:
            ps = [get(w) for w in words]
            if all(p is not None for p in ps):
                e.parts = ps


def canon_add(key, s):
    s = clean_md(s).replace('"', "'")
    norm = lambda x: re.sub(r"^\((?:v|n|adj|adv)\.\)\s*", "", x.lower()).strip()
    for part in [x.strip() for x in re.split(r";\s*", s) if x.strip()]:
        have = [norm(x) for x in CANON_SENSES[key]]
        if norm(part) in have:
            # keep the marked form ((v.) ...) where the tables give one
            if part.startswith("(") and not CANON_SENSES[key][have.index(norm(part))].startswith("("):
                CANON_SENSES[key][have.index(norm(part))] = part
            continue
        CANON_SENSES[key].append(part)


def v2_split():
    """orrowen_v2 §5 rows, one per form: a row of several forms (Hemm · Hemma) gives each its sense"""
    out = defaultdict(list)
    for head, r in V2.items():
        forms = [x.strip() for x in head.split("·") if x.strip()]
        senses = [x.strip() for x in r["sense"].split("·")]
        for i, f in enumerate(forms):
            s = senses[i] if len(senses) == len(forms) else r["sense"]
            out[M.nk(f)].append((f, s, r))
    return out


# canon names of things (orrowen_v2 §1, §3.10, §4.7): phrases the canon gives
CANON_PHRASES = {
    "Garl Dhrenn": ("name", "the course-hand ('the hand of the course'): the script"),
    "Garl Flenn": ("name", "the leaf-hand: the scribes' running hand, the one the Book is written in"),
    "Garl Hal": ("name", "the bedrock hand: the first builders' hand"),
    "garl brenth": ("n", "the coal hand: the Captain's hand, the Title only"),
    "ryt broc": ("n", "the dry cut ('dry cutting'): the chisel register"),
    "brodath lodh": ("n", "the mortar words ('the words of mortar'): the small words the dry cut leaves out"),
    "rellor wrod": ("n", "a word-sign ('a sign of a word'); pl. rellorath wrod"),
    "lodh gunn": ("n", "the footing ('the deep mortar'): the second mortar line under every word-sign"),
    "tolm kylet": ("n", "the turned stone: the NOT mark of the dry cut"),
    "brodhen Orrow": ("n", "the speech of the Shore: the formal name of Orrowen"),
    "Orrowen Hal": ("name", "the Hal, the old register ('the bedrock speech')"),
    "cadh trenn": ("v", "lay a course; lay a tale (a scribe lays a line as a mason lays a course)"),
    "Seren Pa Luth": ("name", "Seren Two-Inks"),
    "Rhyna Yanna Ulvenn": ("name", "Rhyna of the Inner Gate"),
    "Halvard Tolmvard": ("name", "Halvard Stone-Warden"),
    "Voss sa re vess": ("name", "Voss who asked"),
    "ganna ulvenn": ("n", "the inner gate"),
    "lest Vardh": ("n", "a temple ('a house of God')"),
    "Tolm Vardh": ("n", "a Theolith ('a stone of God'); pl. Tolmath Vardh"),
    "Grest um hos, grest um vana": ("phr", "harm to one is harm to both: the old masters' saying, and the meaning of the Aelthar"),
}
FORM_SENSE = {
    "hosast": "first", "pawast": "second",
    "tevath": "children: the plural of tev (irregular: from old tevāthi, an old ā-plural)",
    "tolmath vardh": "the Theoliths ('stones of God')", "tunnoth": "wholeness", "odh sell": "the Long Hearth",
    "drunnard": "a smith", "drunnow": "a smithy, a forge", "scethel": "one hull of a fleet",
    "covv treskat": "the Torn Cloak", "nydherd": "a counter: Kael Nydherd", "brodhat": "told",
    "nawrodhat": "untold", "kethyl": "holding; (of the wood) a knowing", "sennyl": "dying, death",
    "tumar": "we remember: the hearth's answer, and Orrowen's 'yes'", "tolmvard": "Stone-Warden: Halvard's epithet",
    "cadhat": "laid", "lodhan": "the Bonded ('those of the mortar'): et Lodhan",
    "halyna": "Halyna: the pair-name of Halvard and Rhyna, the Bonded of the Keep",
    "aldwena": "Aldwena: the pair-name of Aldun and Bena, the first builders who laid the old capstone",
    "idrenna": "Idrenna: the pair-name of Idlan and Denna, the Theoliths who taught Halyna",
    "kael nydherd": "Kael the Counter", "tavow hemm": "Eldhythe ('the old landing')",
    "cemm hyll": "Tidesmeet ('the meeting of the tide')", "sedhnell": "Fenholm ('fen-islet')",
    "lurrvard": "Holtward ('forest-ward')", "kethow stellath": "Carnhold ('the hold of the cairns')",
    "tavow vorr": "Emberhythe ('the landing of fire')", "grullsorth": "Sandreach ('sand-ridge')",
    "frennvar": "Rimewatch ('frost-guard')", "taldow helv": "Highreach ('the high place of the sky')",
    "sirrvell": "Glasspire ('glass-spire')", "kethow dhresk": "Rivenkeep ('the holding-place of the cleft')",
    "et hosk": "the Title ('the lintel')", "hosnoth": "eleven ('one-ten')", "sullnoth": "thirteen",
    "pa relv": "twenty-four ('two twelves', the guild's way)", "pa vurr": "forty ('two twenties')",
    "lesk murr": "a hundred ('five twenties')", "delvoth": "twelvefold", "et delv": "the Twelve: the True Men",
    "nel": "is not (the copula, negative)", "new": "was not (the copula, negative, past)",
    "yal": "was, were (re yal-: the suppletive past of doss, from old gal-)",
    "mystaeri": "the Mystaeri (a hybrid exonym: myst + the Seilrhass -aer + the loan-plural -i)",
    "mystow": "the Mystlands ('the place of the grey')", "ketherd": "the Commander ('the holder')",
}


def build_base():
    v2 = v2_split()
    # the canon: inherited words and names
    for it in base.canon_inherited():
        form = it["form"]
        if it["affix"]:
            continue
        name = it["name"]
        disp = form[:1].upper() + form[1:] if (name and form != "kael") or form in ("mardh", "orrow") else form
        e = get(disp)
        if e is None:
            e = put(E(disp, POS_CANON.get(form, "name" if name else "n"), source="canon", hal=it["hal"]))
        canon_add(e.key, it["gloss"])
        for f, s, r in v2.get(M.nk(form), []):
            canon_add(e.key, s)
        if form == "kael":
            canon_add(e.key, "Kael (a name: Kael the Counter)")
            e.add_pos("name")
        if form == "seren":
            e.roots.append("*reŋ-")
        if it["root"] != "—":
            e.roots.append("*" + it["root"].split(" / ")[0].strip())
        laws = ",".join(x for x in it["trace"])
        e.derivation = "*%s > %s > %s%s" % (it["anc"], ("Hal " + it["hal"]) if it["hal"] else "Hal", form,
                                            (" (%s)" % laws) if laws else "")
        if name and form not in ("seren", "halvard", "rhyna", "stannard", "pellow", "garvel", "tarnel", "kael"):
            e.derivation += "; a name: names are names (no sense given)"
        if form == "seren":
            e.derivation = ("*swe- 'one's own; one alone, single' + *reŋ- 'a sorrow that is carried and does not "
                            "break the one who carries it' + the nominative *-o-s: *swe-reŋ-o-s > Hal SEREŊOS "
                            "(O4 sw- > s-) > sereŋ (H2) > seren (H4 ŋ > n); Jack's note 6")
        e.formation = "*" + it["anc"]
        if it["root"] != "—":
            e.derivation = "*%s '%s': " % (it["root"], short(it["root_mean"])) + e.derivation
    # the affixes, as entries of their own
    for code, disp, sense in (("Ath", "-Ath", "plural (-ath broad, -eth slender)"),
                              ("Ol", "-Ol", "verbal noun (-ol, -yl)"), ("At", "-At", "participle: done, made (-at, -et)"),
                              ("Ard", "-Ard", "agent: one who does (-ard, -erd)"), ("Oth", "-Oth", "abstract quality (-oth, -yth)"),
                              ("el", "-el", "singulative; 'little, dear'"), ("an", "-an", "'the folk of', a collective"),
                              ("en", "-en", "'of, belonging to'; an old name-ending"), ("ow", "-ow", "place of"),
                              ("Ast", "-Ast", "ordinal (-ast, -est)"), ("a", "-a", "the old dual; feminine names; the pair-name lintel"),
                              ("na", "-na", "dual of a pronoun"),
                              ("Om", "-Om", "1sg (-om, -ym)"), ("ith", "-ith", "2sg"), ("An", "-An", "1du, we two (-an, -en)"),
                              ("A", "-A", "3du, they two (-a, -e)"), ("Ar", "-Ar", "1pl, we (-ar, -er)"),
                              ("Os", "-Os", "2pl, you (-os, -ys)"), ("Ant", "-Ant", "3pl, they (-ant, -ent)")):
        e = E(disp, "suf", source="canon")
        e.key = "suffix:" + disp
        anc = {"Ath": "*-aθi", "Ol": "*-ol-a", "At": "*-at", "Ard": "*-ard", "Oth": "*-oθ", "el": "*-el",
               "an": "*-an", "en": "*-en", "ow": "*-uʔ", "Ast": "*-ast", "a": "*-aʔ", "na": "*-naʔ",
               "Om": "*-om", "ith": "*-iθ", "An": "*-ana", "A": "*-aʔ", "Ar": "*-ar", "Os": "*-us",
               "Ant": "*-ant"}[code]
        e.roots.append(anc)
        e.derivation = "%s > the living suffix %s (harmony: §3.2)" % (anc, disp)
        e.formation = anc
        ENTRIES[e.key] = e
        canon_add(e.key, sense)
    # canon formations (the daughter's grammar)
    for f in base.canon_formations():
        form = f["form"]
        disp = FORM_DISPLAY.get(form, form)
        e = get(disp)
        if e is None:
            e = put(E(disp, "", source="canon"))
        if form in FORM_SENSE:
            canon_add(e.key, FORM_SENSE[form])
        for ff, s, r in v2.get(M.nk(disp), []) + (v2.get(M.nk(form), []) if M.nk(form) != M.nk(disp) else []):
            canon_add(e.key, s)
        if not CANON_SENSES[e.key]:
            ERRORS.append("canon formation with no sense: %s" % form)
        e.formation = "+".join(f["parts"])
        e.derivation = "canon formation: " + " + ".join(f["parts"]) + " (" + f["how"] + ")"
        e.phrase = " " in disp
        if not e.pos:
            e.add_pos(FORM_POS.get(form, "n"))
        FORMATION_PARTS[e.key] = f["parts"]
    # canon phrases (orrowen_v2 §1, §3.10)
    for form, (pos, sense) in CANON_PHRASES.items():
        e = get(form)
        if e is None:
            e = put(E(form, pos, source="canon"))
            e.phrase = " " in form
            e.formation = "phrase"
            e.derivation = "canon (orrowen_v2)"
        canon_add(e.key, sense)
    # orrowen_v2 §5 rows not yet in
    for k, lst in v2.items():
        for f, s, r in lst:
            if f in ("na-",):
                continue
            if get(f) is None:
                e = put(E(f, "", source="canon"))
                e.derivation = "orrowen_v2 §%s: %s" % (r["sub"], clean_md(r["note"]))
                e.phrase = " " in f
                e.add_pos("phr" if e.phrase else "n")
            canon_add(M.nk(f), s)
    # the reserve roots
    for r in RESERVE:
        form = r["o_pred"]
        e = get(form)
        if e is not None:
            ERRORS.append("reserve form clashes with a canon word: %s" % form)
            continue
        e = put(E(form, reserve_pos(r), source="reserve", hal=r["hal"]))
        canon_add(e.key, r["mean"])
        e.roots.append("*" + r["root"])
        e.derivation = "*%s '%s' (reserve, ancestor §3.3): Hal %s > %s" % (r["root"], short(r["mean"]), r["hal"], form)
        e.formation = "*" + r["root"]
        e.field = r["field"]
        if BANNED_END.search(form):
            e.flag = "banned ending -dor (§2.5): the reserve root owes a re-draw; not used in tier-3 text"
    # the two word-sign terms of §1
    canon_add("bisk", "(of a word-sign) its head: the mark a word-sign stands on")
    canon_add("hosk", "(of a word-sign) a crown: the small mark set over a head")
    # the canon senses, set
    for k, e in ENTRIES.items():
        if CANON_SENSES.get(k):
            e.canon = "; ".join(CANON_SENSES[k])
    # word-signs
    for reading, s in SIGNS.items():
        e = get(reading)
        if e is None:
            ERRORS.append("word-sign reading not in the lexicon: %s" % reading)
            continue
        e.sign = s


FORM_DISPLAY = {"stonwryt": "Stonwryt", "stonwrytan": "Stonwrytan", "halyna": "Halyna", "aldwena": "Aldwena",
                "idrenna": "Idrenna", "kael nydherd": "Kael Nydherd", "tavow hemm": "Tavow Hemm",
                "cemm hyll": "Cemm Hyll", "sedhnell": "Sedhnell", "lurrvard": "Lurrvard",
                "kethow stellath": "Kethow Stellath", "tavow vorr": "Tavow Vorr", "grullsorth": "Grullsorth",
                "frennvar": "Frennvar", "taldow helv": "Taldow Helv", "sirrvell": "Sirrvell",
                "kethow dhresk": "Kethow Dhresk", "et hosk": "et Hosk", "et delv": "et Delv",
                "mystow": "Mystow", "mystaeri": "Mystaeri", "mesk myst": "Mesk Myst", "tolm myst": "Tolm Myst",
                "gannath myst": "Gannath Myst", "crenn myst": "Crenn Myst", "orrowan": "Orrowan",
                "orrowen": "Orrowen", "treskan": "Treskan", "ketherd": "Ketherd", "hosk lunn": "Hosk Lunn",
                "covv treskat": "Covv Treskat", "tolm vardh": "Tolm Vardh", "tolmath vardh": "Tolmath Vardh",
                "ryt dhunnoth": "Ryt Dhunnoth", "lodh helv": "Lodh Helv", "odh sell": "Odh Sell",
                "tolmvard": "Tolmvard", "lodhan": "Lodhan"}
FORM_POS = {"nayald": "v", "stannow": "n", "gorndholm": "n", "trenndholm": "n", "halflenn": "n",
            "stonwryt": "n", "stonwrytan": "n", "stonwrytel": "n", "prassel": "n", "vennoth": "n",
            "lodhat": "adj", "nalodhat": "adj", "lodhan": "n", "sullast": "num", "hosast": "num,n",
            "pawast": "num", "veskerd": "n", "tevow": "n", "tevath": "n", "tevel": "adj", "hoskol": "n",
            "hoskvoll": "n", "tunnoth": "n", "orrowan": "name", "orrowen": "name", "brodhen": "n",
            "treskan": "name", "ketherd": "n", "vennuld": "n", "hesperd": "n", "bramman": "n", "haskard": "n",
            "drunnard": "n", "drunnow": "n", "scethan": "n", "scethel": "n", "treskat": "adj", "mystow": "name",
            "mystaeri": "name", "lurrel": "adj", "tumol": "n", "nadhum": "v", "flennath": "n", "nydherd": "n",
            "brodhat": "adj", "nawrodhat": "adj", "kethyl": "n", "sennyl": "n", "tumar": "v", "ulvenn": "adj",
            "tolmvard": "name", "cadhat": "adj", "halyna": "name", "aldwena": "name", "idrenna": "name",
            "hosnoth": "num", "sullnoth": "num", "delvoth": "adj", "nel": "v", "new": "v", "yal": "v",
            "sedhnell": "name", "lurrvard": "name", "grullsorth": "name", "frennvar": "name",
            "sirrvell": "name"}


def short(s):
    s = re.sub(r"^\([^)]*\)\s*", "", s.strip())
    return re.split(r"[;:(]", s)[0].strip()[:48]


def M_trace(stem, hal, living):
    return "Hal %s > %s" % (hal, living)


# ======================================================================= 2. recipes
SUFS = ["Ath", "Ol", "At", "Ard", "Oth", "Ast", "el", "an", "en", "ow", "a"]


class Built:
    def __init__(self, form, cls, deriv, roots, formation, base_e=None, codes=(), neg=False, parts=(),
                 harm=()):
        self.form, self.cls, self.deriv, self.roots, self.formation = form, cls, deriv, roots, formation
        self.base_e, self.codes, self.neg, self.parts, self.harm = base_e, list(codes), neg, list(parts), list(harm)


def build_part(p):
    """word(+SUF)* -> Built"""
    bits = p.split("+")
    w = bits[0]
    e = get(w)
    if e is None:
        raise ValueError("no base word '%s'" % w)
    form = e.form
    cls = e.cls
    deriv = "%s '%s'" % (e.form, short(e.canon or (e.senses[0] if e.senses else "")))
    roots = list(e.roots)
    codes = []
    harm = []
    for s in bits[1:]:
        if s not in SUFS:
            raise ValueError("unknown suffix %s" % s)
        stem_cls = irreg_cls(M.nk(form), s, cls)
        new = M.attach(form if form[:1].islower() or s else form, s, stem_cls if s in M.HARMONIC else None)
        if s in M.HARMONIC:
            harm.append(s)
            # the harmonic suffix keeps the stem's class
        else:
            cls = M.word_class(M.PLAIN[s])
        deriv += " + " + ("-" + s) + " (" + M.SUF_NAME[s] + ")"
        codes.append(s)
        form = new
        if e.form[:1].isupper() and not e.form.isupper() and "name" not in e.pos:
            form = form[:1].lower() + form[1:]
    return Built(form, cls, deriv, roots, p, base_e=e, codes=codes, harm=harm)


IRREG_CLASS = {"tresk": "B", "flenn": "B", "tev": "B"}   # the canon's old broad stems (treskat, flennath, tevath)
IRREG_CODES = {"tresk": None, "flenn": {"Ath"}, "tev": {"Ath"}}  # None: every harmonic suffix; else only these


def irreg_cls(key, code, default):
    if key in IRREG_CLASS and (IRREG_CODES[key] is None or code in IRREG_CODES[key]):
        return IRREG_CLASS[key]
    return default


def build_recipe(rec):
    neg = False
    r = rec
    if r.startswith("na-"):
        neg = True
        r = r[3:]
    parts = r.split("^")
    built = [build_part(p) for p in parts]
    if len(built) == 1:
        b = built[0]
    else:
        form = built[0].form
        deriv = built[0].deriv
        roots = list(built[0].roots)
        for nb in built[1:]:
            if M.seam_misreads(form, nb.form):
                raise ValueError("the seam of %s + %s would be misread (a letter pair read as one sound)" % (form, nb.form))
            form = M.seam(form, nb.form)
            deriv += " + S " + nb.deriv + " (compound: the head softened, §3.10)"
            roots += nb.roots
        cls = built[-1].cls
        if form[:1].isupper() and built[0].base_e is not None and "name" in built[0].base_e.pos and \
                built[0].base_e.form in ("Orrow",):
            form = form[:1].lower() + form[1:]
        b = Built(form, cls, deriv, roots, rec, parts=built, harm=built[-1].harm)
        b.codes = []
    if neg:
        b.form = M.negate(b.form)
        b.deriv = "na- 'un-' (+S) + " + b.deriv
        b.neg = True
    b.formation = rec
    return b


def check_form(form):
    probs = []
    for w in form.split():
        lw = w.lower()
        if BANNED_LET.search(lw):
            probs.append("banned letter")
        if BANNED_END.search(lw):
            probs.append("banned ending")
    return probs


def load_recipes():
    rows = []
    for fn in sorted(glob.glob(os.path.join(HERE, "en_map", "*.txt"))):
        for i, ln in enumerate(open(fn, encoding="utf-8"), 1):
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            cells = [c.strip() for c in ln.split(" | ")]
            while len(cells) < 4:
                cells.append("")
            rows.append(dict(lemma=cells[0], recipe=cells[1], pos=cells[2], gloss=cells[3],
                             where="%s:%d" % (os.path.basename(fn), i)))
    return rows


COVER = defaultdict(list)     # english lemma -> [(orrowen or note, id-key)]


def apply_recipes():
    for r in load_recipes():
        lem, rec, pos, gloss = r["lemma"], r["recipe"], r["pos"], r["gloss"] or r["lemma"]
        try:
            if rec.startswith("@"):
                COVER[lem].append(("(grammar) " + gloss, None))
                continue
            if rec.startswith("="):
                form = rec[1:]
                e = get(form)
                if e is None:
                    e = put(E(form, pos or "loan", source="tier3"))
                    e.derivation = ("a Mystaeri word, borrowed by sound (orrowen_v2 §6.14 D7: loan words and "
                                    "Mystaeri names are spelled by sound, the knock as a wedge inside the word)")
                    e.formation = "loan"
                    e.roots.append("(Seilrhass)")
                e.add_sense(gloss)
                note_lemma(e, lem)
                continue
            if rec.startswith("~"):
                form = rec[1:]
                e = get(form)
                if e is None:
                    e = put(E(form, pos or "phr", source="tier3"))
                    e.phrase = " " in form
                    e.formation = "phrase"
                elif e.phrase or " " in form:
                    e.add_pos(pos)
                e.add_sense(gloss)
                note_lemma(e, lem)
                continue
            b = build_recipe(rec)
            probs = check_form(b.form)
            if probs:
                ERRORS.append("%s: %s -> %s: %s" % (r["where"], rec, b.form, probs))
            disp = b.form
            e = get(disp)
            if e is None:
                e = put(E(disp, pos, cls=b.cls, source="tier3"))
                e.derivation = b.deriv
                e.roots = [x for x in b.roots if x]
                e.formation = b.formation
                e.base = b.base_e
                e.codes = b.codes
                e.neg = b.neg
                e.parts = [p.base_e if not p.codes else p for p in b.parts]
                e.harm_letters = b.harm
                e.built = b
            else:
                e.add_pos(pos)
            e.add_sense(gloss)
            for p in (pos or "").split(","):
                e.pos_senses[p.strip()].append(gloss)
            note_lemma(e, lem)
        except Exception as ex:  # noqa
            ERRORS.append("%s: %s | %s: %s" % (r["where"], lem, rec, ex))


def note_lemma(e, lem):
    if lem in ("@phrase", "-"):
        return
    if lem not in e.lemmas:
        e.lemmas.append(lem)
    COVER[lem].append((e.form, e.key))


# ======================================================================= 3. the systematic derivations
EN_PP = {"hold": "held", "keep": "kept", "know": "known", "stand": "stood", "build": "built", "lay": "laid",
         "tell": "told", "speak": "spoken", "see": "seen", "read": "read", "give": "given", "come": "come",
         "go": "gone", "run": "run", "fall": "fallen", "break": "broken", "cut": "cut", "sit": "sat",
         "lie": "lain", "fight": "fought", "hear": "heard", "find": "found", "lose": "lost", "bring": "brought",
         "teach": "taught", "think": "thought", "catch": "caught", "seek": "sought", "sell": "sold",
         "buy": "bought", "say": "said", "sleep": "slept", "feel": "felt", "swim": "swum", "drink": "drunk",
         "eat": "eaten", "sow": "sown", "hew": "hewn", "sew": "sewn", "throw": "thrown", "grow": "grown",
         "bind": "bound", "spend": "spent", "lead": "led", "meet": "met", "kneel": "knelt", "rise": "risen",
         "forgive": "forgiven", "understand": "understood", "hide": "hidden", "begin": "begun",
         "choose": "chosen", "strike": "struck", "swear": "sworn", "tear": "torn", "weave": "woven",
         "wake": "woken", "dig": "dug", "shut": "shut", "put": "put", "set": "set", "let": "let",
         "cast": "cast", "do": "done", "make": "made", "bear": "borne", "fly": "flown", "freeze": "frozen",
         "forget": "forgotten", "sing": "sung", "sink": "sunk", "draw": "drawn", "light": "lit",
         "pay": "paid", "mean": "meant", "leave": "left", "slay": "slain", "weep": "wept", "write": "written",
         "ride": "ridden", "shake": "shaken", "speed": "sped", "flee": "fled", "tread": "trodden",
         "bite": "bitten", "fling": "flung", "hang": "hung", "shoot": "shot", "stick": "stuck", "win": "won",
         "send": "sent", "bend": "bent", "leap": "leapt", "sweep": "swept", "creep": "crept", "lend": "lent",
         "wind": "wound", "hit": "hit", "burst": "burst", "spill": "spilled", "dream": "dreamt",
         "wear": "worn", "hurt": "hurt", "split": "split", "spread": "spread", "shed": "shed", "cost": "cost",
         "quit": "quit", "outlive": "outlived", "forbid": "forbidden", "swell": "swollen", "undo": "undone"}
EN_GER = {"begin": "beginning", "forget": "forgetting", "forbid": "forbidding", "open": "opening",
          "remember": "remembering", "offer": "offering", "wonder": "wondering", "answer": "answering",
          "gather": "gathering", "enter": "entering", "wither": "withering", "murmur": "murmuring",
          "listen": "listening", "happen": "happening", "travel": "travelling", "quarrel": "quarrelling"}
NO_DERIV = {"doss", "el", "ew", "gal", "yal", "nel", "new", "tumar", "tessen", "ser", "nayald", "nadhum"}
import sys_curated as SC   # noqa: E402


def sense_for(e, p):
    """the English sense of an entry for one part of speech: the canon's own segment for it first,
    then a tier-3 sense given for it"""
    segs = [x.strip() for x in (e.canon or "").split(";") if x.strip()]
    mark = {"v": "(v.)", "adj": "(adj.)", "n": "(n.)"}[p]
    for s in segs:
        if s.startswith(mark):
            return s[len(mark):].strip()
    canon_pos = CANON_POS.get(e.key, e.pos[:1])
    for s in segs:
        if s.startswith("("):
            continue
        is_n = bool(re.match(r"(a|an|the|one) ", s))
        if p == "n" and is_n:
            return s
        if p != "n" and not is_n and canon_pos and canon_pos[0] == p:
            return s
    if e.pos_senses.get(p):
        return e.pos_senses[p][0]
    if e.senses and e.pos and e.pos[0] == p:
        return e.senses[0]
    return ""


CANON_POS = {}


def en_verbs(e):
    m = sense_for(e, "v")
    m = re.sub(r"\(.*?\)", "", m)
    first = re.split(r"[;:]", m)[0]
    vs = [x.strip() for x in first.split(",") if x.strip()]
    vs = [re.sub(r"^to ", "", v) for v in vs]
    vs = [v for v in vs if v and not re.match(r"^(a|an|the) ", v)]
    return vs[:2]


def gerund(v):
    words = v.split(" ")
    h = words[0]
    if h in EN_GER:
        g = EN_GER[h]
    elif h in ("be",):
        g = "being"
    elif h.endswith("ie"):
        g = h[:-2] + "ying"
    elif h.endswith("e") and not h.endswith(("ee", "ye", "oe")):
        g = h[:-1] + "ing"
    elif re.match(r"^[^aeiou]*[aeiou][^aeiouwxy]$", h):
        g = h + h[-1] + "ing"
    else:
        g = h + "ing"
    return " ".join([g] + words[1:])


def pp(v):
    words = v.split(" ")
    h = words[0]
    if h in EN_PP:
        g = EN_PP[h]
    elif h.endswith("e"):
        g = h + "d"
    elif h.endswith("y") and h[-2:-1] not in "aeiou":
        g = h[:-1] + "ied"
    elif re.match(r"^[^aeiou]*[aeiou][^aeiouwxy]$", h):
        g = h + h[-1] + "ed"
    else:
        g = h + "ed"
    return " ".join([g] + words[1:])


def s3(v):
    words = v.split(" ")
    h = words[0]
    if h.endswith(("s", "sh", "ch", "x", "o")):
        g = h + "es"
    elif h.endswith("y") and h[-2:-1] not in "aeiou":
        g = h[:-1] + "ies"
    else:
        g = h + "s"
    return " ".join([g] + words[1:])


def en_nouns(e):
    m = sense_for(e, "n")
    m = re.sub(r"\(.*?\)", "", m)
    first = re.split(r"[;:]", m)[0]
    ns = [x.strip() for x in first.split(",") if x.strip()]
    return [re.sub(r"^(a|an|the|one's) ", "", n) for n in ns[:2]]


def en_adjs(e):
    m = sense_for(e, "adj")
    m = re.sub(r"\(.*?\)", "", m)
    first = re.split(r"[;:]", m)[0]
    return [x.strip() for x in first.split(",") if x.strip()][:2]


def is_root_word(e):
    return (e.formation.startswith("*") and e.source in ("canon", "reserve") and not e.phrase
            and "name" not in e.pos and "loan" not in e.pos and e.form not in NO_DERIV and not e.flag
            and re.fullmatch(r"[a-z]+", e.form) is not None)


def systematic():
    made = 0
    for k, e in list(ENTRIES.items()):
        CANON_POS[k] = list(e.pos)
    bases = [e for e in list(ENTRIES.values()) if is_root_word(e)]
    small = {"part", "prep", "pron", "det", "conj", "art", "pref"}
    for e in bases:
        pos = set(e.pos)
        if pos & small and e.form not in ("tul", "somm", "amm"):
            continue
        if "v" in pos:
            vs = en_verbs(e) or []
            if vs:
                made += derive(e, "Ol", "; ".join(gerund(v) for v in vs) + "; the act of " + gerund(vs[0]), "n")
                made += derive(e, "At", ", ".join(pp(v) for v in vs) + " (the participle)", "adj")
                made += derive(e, "Ard", "one who " + " or ".join(s3(v) for v in vs), "n")
            if e.form in SC.OW_VERBS:
                made += derive(e, "ow", SC.OW_VERBS[e.form], "n")
            if e.form in SC.NA_PTCP:
                pt = get(M.attach(e.form, "At", irreg_cls(e.key, "At", None)))
                if pt is not None:
                    made += derive_neg(pt, SC.NA_PTCP[e.form] + " (un- + the participle)", "adj")
        if "adj" in pos:
            adjs = en_adjs(e) or []
            if adjs:
                a0 = adjs[0]
                if " " in a0 or e.form in ("bell", "lenn", "styvil"):
                    made += derive(e, "Oth", "the quality of being " + a0, "n")
                else:
                    made += derive(e, "Oth", (a0[:-1] + "iness" if a0.endswith("y") else a0 + "ness")
                                   + "; the quality of being " + a0, "n")
                made += derive_neg(e, "not " + a0 + "; un-" + a0, "adj")
            if e.form in SC.EL_ADJ:
                made += derive(e, "el", SC.EL_ADJ[e.form], "adj")
        if "n" in pos:
            ns = en_nouns(e)
            if not ns:
                continue
            n0 = ns[0]
            person = e.form in SC.AN_PEOPLE or n0.startswith("one ")
            if e.form in SC.COLLECTIVE_EL:
                if SC.COLLECTIVE_EL[e.form]:
                    made += derive(e, "el", SC.COLLECTIVE_EL[e.form] + " (the singulative)", "n")
            elif e.form not in SC.MASS_TIME and "v" not in pos and "adj" not in pos:
                made += derive(e, "el", ("little %s, dear %s" % (n0, n0)) if person else "a small %s; a single %s" % (n0, n0), "n")
            if e.form in SC.MASS_EN:
                made += derive(e, "en", SC.MASS_EN[e.form], "adj")
            elif e.form not in SC.MASS_TIME and not person and "v" not in pos:
                made += derive(e, "en", "of %s; %s-like" % (plural_en(n0), n0), "adj")
            if SC.OW_NOUNS.get(e.form):
                made += derive(e, "ow", SC.OW_NOUNS[e.form], "n")
            if e.form in SC.AN_PEOPLE:
                made += derive(e, "an", SC.AN_PEOPLE[e.form], "n")
            if SC.AN_THINGS.get(e.form):
                made += derive(e, "an", SC.AN_THINGS[e.form], "n")
            if SC.OCCUPATIONS.get(e.form):
                made += derive(e, "Ard", SC.OCCUPATIONS[e.form] + " ('the one of the %s')" % n0, "n")
            if SC.NOUN_OTH.get(e.form):
                made += derive(e, "Oth", SC.NOUN_OTH[e.form], "n")
        if "v" in pos and SC.REVERSATIVE.get(e.form):
            made += derive_neg(e, SC.REVERSATIVE[e.form] + " (na-, the reversative)", "v")
        if e.form in SC.MASS_EN and "n" not in pos:
            made += derive(e, "en", SC.MASS_EN[e.form], "adj")
        if "num" in pos and e.form in NUMERAL and e.form not in ("hos", "pa", "sull"):
            made += derive(e, "Ast", "%s (the ordinal)" % ORDINAL_EN.get(e.form, e.form), "num")
    # the derived verbs (reversatives, compound verbs, na- verbs): their verbal noun, participle, agent
    for e in list(ENTRIES.values()):
        if e.source not in ("tier3", "tier3-sys", "canon") or e.phrase or " " in e.form:
            continue
        if "v" not in e.pos or e.form in NO_DERIV - {"nayald", "nadhum"} or e.key in M.PREP_FORMS:
            continue
        if e.formation.startswith("*") or re.fullmatch(r"[a-z]+", e.form) is None:
            continue
        if e.key in M.BE_FORMS or e.form in M.PARTICLES:
            continue
        vs = en_verbs(e) or []
        if not vs:
            continue
        v0 = re.sub(r"\s*\(.*$", "", vs[0])
        vs = [re.sub(r"\s*\(.*$", "", v) for v in vs]
        made += derive(e, "Ol", "; ".join(gerund(v) for v in vs) + "; the act of " + gerund(v0), "n", derived=True)
        made += derive(e, "At", ", ".join(pp(v) for v in vs) + " (the participle)", "adj", derived=True)
        made += derive(e, "Ard", "one who " + " or ".join(s3(v) for v in vs), "n", derived=True)
    for f, sense in SC.NOUN_AT.items():
        e = get(f)
        if e is not None:
            made += derive(e, "At", sense + " ('provided with X': -At on a noun)", "adj")
    for f, sense in SC.DERIVED_OTH.items():
        e = get(f)
        if e is not None:
            made += derive(e, "Oth", sense, "n")
    for table, code, pos in ((SC.ADJ_ARD, "Ard", "n"), (SC.ADJ_AN, "an", "n"), (SC.ADJ_OW, "ow", "n")):
        for f, sense in table.items():
            e = get(f)
            if e is not None:
                made += derive(e, code, sense, pos)
    for f, sense in SC.AN_PLACES.items():
        e = get(f)
        if e is not None:
            made += derive(e, "an", sense, "n")
    for f, sense in SC.PLURAL_SENSES.items():
        e = get(f)
        if e is not None:
            made += derive(e, "Ath", sense + " (a plural with a sense of its own)", "n")
    made += numbers()
    made += grammar_forms()
    return made


def numbers():
    made = 0
    teens = (("gemm", "fourteen"), ("lesk", "fifteen"), ("vran", "sixteen"), ("dhom", "seventeen"),
             ("thell", "eighteen"), ("rost", "nineteen"))
    for unit, en in teens:
        made += make_compound("%s^noth" % unit, en, "num", "the teens: unit + ten, as hosnoth, sullnoth")
    tens = (("~murr eth noth", "thirty (twenty and ten)"), ("~pa vurr eth noth", "fifty (two twenties and ten)"),
            ("~sull murr", "sixty (three twenties)"), ("~sull murr eth noth", "seventy"),
            ("~gemm murr", "eighty (four twenties)"), ("~gemm murr eth noth", "ninety"),
            ("~noth murr", "two hundred (ten twenties)"), ("~pa wost", "eight hundred (two four-hundreds)"),
            ("~pa wost eth noth murr", "a thousand (two four-hundreds and ten twenties)"),
            ("~lesk bost", "two thousand ('five four-hundreds')"))
    for form, en in tens:
        f = form[1:]
        if get(f) is None:
            ne = put(E(f, "num", source="tier3-sys"))
            ne.phrase = True
            ne.formation = "phrase"
            ne.derivation = "the numbers count in twenties (§5.11): " + en
            ne.add_sense(en)
            made += 1
    return made


def make_compound(rec, sense, pos, how):
    b = build_recipe(rec)
    if get(b.form) is not None:
        return 0
    ne = put(E(b.form, pos, cls=b.cls, source="tier3-sys"))
    ne.derivation = b.deriv + " (" + how + ")"
    ne.roots = [x for x in b.roots if x]
    ne.formation = rec
    ne.parts = [p.base_e for p in b.parts]
    ne.add_sense(sense)
    return 1


def grammar_forms():
    """the conjugated prepositions (§3.6) and the two 'be' verbs (§3.4): forms the lexicon lists"""
    made = 0
    PERS = {"1SG": "me", "2SG": "you (one)", "3SG.M": "him, it", "3SG.F": "her", "1DU": "us two",
            "1PL": "us", "2PL": "you (many)", "3PL": "them", "3DU": "them two"}
    for form, (p, g, per) in sorted(M.PREP_FORMS.items()):
        if get(form) is not None:
            continue
        src = "canon" if p in ("lo", "um") else "tier3-sys"
        ne = put(E(form, "prep", cls=M.word_class(form), source=src))
        ne.derivation = "%s '%s' + the %s ending (§3.6, conjugated prepositions%s)" % (
            p, g, per, "" if src == "canon" else ": 'the other prepositions follow the same pattern'")
        ne.formation = "%s+%s" % (p, per)
        sense = "%s %s" % (g, PERS[per])
        SUBJ = {"1SG": "I have", "2SG": "you have", "3SG.M": "he has", "3SG.F": "she has", "1DU": "we two have",
                "1PL": "we have", "2PL": "you have", "3PL": "they have", "3DU": "they two have"}
        FEEL = {"1SG": "I feel", "2SG": "you feel", "3SG.M": "he feels", "3SG.F": "she feels", "1DU": "we two feel",
                "1PL": "we feel", "2PL": "you feel", "3PL": "they feel", "3DU": "they two feel"}
        if p == "lo":
            sense += " (having: Doss X %s, '%s X')" % (form, SUBJ[per])
        if p == "um":
            sense += " (feeling: Doss X %s, '%s X')" % (form, FEEL[per])
        if src == "canon":
            canon_add(ne.key, sense)
            ne.canon = "; ".join(CANON_SENSES[ne.key])
        else:
            ne.add_sense(sense)
        base = get(p)
        ne.base = base
        ne.roots = list(base.roots) if base else []
        made += 1
    for form, v in sorted(M.BE_FORMS.items()):
        if get(form) is not None:
            continue
        per = v[3] if len(v) > 3 else "3SG"
        ne = put(E(form, "v", cls=M.word_class(form), source="canon"))
        ne.derivation = "the state verb doss (§3.4): %s%s" % (
            {"": "", "N": "nasalised (after nath, es): ", "S": "softened (after re): "}[v[2]], per)
        ne.formation = "%s+%s" % (v[0], per)
        what = {"doss": "am, is, are (state, place)", "noss": "(after nath/es) be", "yal": "was, were"}
        stem = "doss" if form.startswith("doss") else ("noss" if form.startswith("noss") else "yal")
        canon_add(ne.key, "%s, %s" % (what[stem], per))
        ne.canon = "; ".join(CANON_SENSES[ne.key])
        ne.base = get("doss")
        ne.roots = list(get("doss").roots)
        made += 1
    return made


ORDINAL_EN = {"gemm": "fourth", "lesk": "fifth", "vran": "sixth", "dhom": "seventh", "thell": "eighth",
              "rost": "ninth", "noth": "tenth", "delv": "twelfth", "murr": "twentieth", "bost": "four-hundredth"}


def plural_en(n):
    n = n.strip()
    if n.endswith(("s", "sh", "ch", "x")):
        return n + "es"
    if n.endswith("y") and n[-2:-1] not in "aeiou":
        return n[:-1] + "ies"
    if n.endswith("f"):
        return n[:-1] + "ves"
    return n + "s"


def derive(e, code, sense, pos, derived=False):
    stem_cls = irreg_cls(e.key, code, e.cls)
    form = M.attach(e.form, code, stem_cls if code in M.HARMONIC else None)
    if e.form[:1].isupper():
        form = form[:1].lower() + form[1:]
    if check_form(form):
        return 0
    k = M.nk(form)
    if k in ENTRIES:
        ex = ENTRIES[k]
        if ex.base is e and ex.codes == [code]:
            ex.add_sense(sense)
            ex.add_pos(pos)
        return 0
    ne = put(E(form, pos, cls=(e.cls if code in M.HARMONIC else M.word_class(M.PLAIN[code])), source="tier3-sys"))
    ne.derivation = "%s '%s' + -%s (%s)" % (e.form, short(e.canon or (e.senses[0] if e.senses else "")),
                                            code, M.SUF_NAME[code])
    ne.roots = list(e.roots)
    ne.formation = "%s+%s" % (e.form, code)
    ne.base = e
    ne.codes = [code]
    ne.harm_letters = [code] if code in M.HARMONIC else []
    ne.add_sense(sense)
    return 1


def derive_neg(e, sense, pos):
    form = M.negate(e.form)
    if check_form(form):
        return 0
    k = M.nk(form)
    if k in ENTRIES:
        return 0
    # a negative must not read as na + another word softened (nahemm "not old" beside cemm)
    for x in M.unsoften(form[2:]) + [(form[2:], None)]:
        if M.nk(x[0]) != e.key and M.nk(x[0]) in ENTRIES:
            return 0
    ne = put(E(form, pos, cls=e.cls, source="tier3-sys"))
    ne.derivation = "na- 'un-' (+S) + %s '%s'" % (e.form, short(e.canon or (e.senses[0] if e.senses else "")))
    ne.roots = list(e.roots)
    ne.formation = "na-%s" % e.form
    ne.base = e
    ne.neg = True
    ne.add_sense(sense)
    return 1


# ======================================================================= 4. the dry cut and the logogram
def sign_label(s):
    return "%s (%d)" % (base.sign_name(s), s["n"])


def letters(form, harm_codes=()):
    """course-hand letters as drycut.py tokens (§6.3): th dh rh single; c/k one letter; ae = a e;
    ow = o w; a harmonic suffix vowel is A or O"""
    f = form.lower()
    toks = []
    i = 0
    while i < len(f):
        two = f[i:i + 2]
        if two in ("th", "dh", "rh"):
            toks.append(two)
            i += 2
            continue
        c = f[i]
        if c == "c":
            c = "k"
        if c == "'":
            toks.append(",")
            i += 1
            continue
        if c.isalpha():
            toks.append(c)
        i += 1
    # the harmonic vowels of the suffixes: from the end of the word inward
    n = len(toks)
    pos = n
    for code in reversed(list(harm_codes)):
        surf = M.HARMONIC[code][0]
        L = len(surf.replace("th", "T").replace("dh", "D"))
        # find the suffix's vowel: the first vowel of the last L tokens
        seg = list(range(pos - L, pos))
        for j in seg:
            if 0 <= j < n and toks[j] in "aeoy":
                toks[j] = "A" if code in ("Ath", "At", "Ard", "Ast", "An", "A", "Ar", "Ant") else "O"
                break
        pos -= L
    return ".".join(toks)


def dry_cut(e):
    """(logogram, dry-cut token string)"""
    lw = e.form.lower()
    if e.key.startswith("suffix:"):
        return "", "letters, after the sign (D5)"
    if lw in TURNED:
        return "the turned stone (NOT)", "!"
    if lw in M.MORTAR or lw in ("cedh", "vodh", "noss", "yal"):
        return "", "left out (a mortar word, D2)"
    if e.sign is not None:
        return sign_label(e.sign), "@" + lw
    if lw in NUMERAL:
        return "", "%" + NUMERAL[lw]
    if lw in COMPOUND_NUMERALS:
        return "", "%" + COMPOUND_NUMERALS[lw]
    if "name" in e.pos and not e.phrase:
        pair = lw in ("halyna", "aldwena", "idrenna")
        return "", ("=" if pair else "") + letters(e.form)
    if "loan" in e.pos:
        return "", letters(e.form)
    if e.phrase:
        words = M.analyse_text(e.form, LEXPROXY) if LEXPROXY else []
        if not e.derivation or e.derivation == "canon (orrowen_v2)":
            parts = []
            for wd in words:
                if wd.kind == "punct" or wd.best is None:
                    continue
                parts.append("%s %s" % (wd.tok, wd.gloss))
                te = ENTRIES.get(M.nk(wd.best.stem))
                if te is not None and te is not e:
                    for r0 in te.roots:
                        if r0 and r0 not in e.roots:
                            e.roots.append(r0)
            pre = e.derivation + ": " if e.derivation else "a phrase: "
            e.derivation = pre + " + ".join(parts)
        out, logs = [], []
        numeral = ""
        for wd in words:
            if wd.kind == "punct":
                if numeral:
                    out.append("%" + numeral)
                    numeral = ""
                out.append({",": ",", ".": "|"}.get(wd.tok, ""))
                continue
            tl = wd.tok.lower()
            stem = M.nk(wd.best.stem) if wd.best is not None else None
            if stem in NUMERAL_KEYS or (stem and stem in COMPOUND_NUMERALS):
                numeral += NUMERAL_KEYS.get(stem) or COMPOUND_NUMERALS[stem]
                continue
            if tl == "eth" and numeral:
                continue
            if numeral:
                out.append("%" + numeral)
                numeral = ""
            if tl in TURNED:
                out.append("!")
                continue
            if tl in M.MORTAR or wd.kind in ("particle", "prep", "be"):
                continue
            te = ENTRIES.get(stem) if stem else None
            if te is None or te is e or te.phrase:
                out.append(letters(wd.tok))
                continue
            lg, dc = dry_cut(te)
            if dc.startswith("left out"):
                continue
            cs = [c for c in wd.best.layers if c in COMPLEMENT]
            if cs and dc.startswith("@") and "+" not in dc:
                dc = dc + "+" + ".".join(COMPLEMENT[c] for c in cs)
            if wd.best.prefix and not dc.startswith("!"):
                dc = "!" + dc
            out.append(dc)
            if lg:
                logs.append(lg)
        if numeral:
            out.append("%" + numeral)
        out = [x for x in out if x]
        while out and out[-1] in (",",):
            out.pop()
        return " · ".join(logs), " ".join(out) if out else "left out (mortar words only)"
    # derived from a base with a sign
    if e.base is not None:
        lg, dc = dry_cut(e.base)
        if e.neg and not e.codes:
            return ("the turned stone + " + lg) if lg else "", "!" + dc if dc.startswith(("@", "!")) else "letters: " + letters(e.form)
        if dc.startswith("@") and e.codes:
            comp = []
            regular = e.base.form
            for c in e.codes:
                regular = M.attach(regular, c, e.base.cls if c in M.HARMONIC else None)
            irregular = M.nk(regular) != M.nk(e.form)
            for c in e.codes:
                if irregular and c in M.HARMONIC:
                    # an irregular ending is cut in full vowels (D5): the vowel the word really has
                    b0 = M.HARMONIC[c]
                    surf = b0[0] if M.nk(e.form).endswith(M.nk(b0[0])) else b0[1]
                    comp.append(".".join(t for t in re.findall(r"th|dh|.", surf)))
                else:
                    comp.append(COMPLEMENT[c])
            dcx = dc + "+" + ".".join(comp)
            lgx = lg + " + " + " ".join(x.replace(".", " ") for x in comp)
            if e.neg:
                return "the turned stone + " + lgx, "!" + dcx
            return lgx, dcx
        return "", "letters: " + letters(e.form, e.harm_letters)
    if e.parts:
        signs, labels = [], []
        for p in e.parts:
            pe = p if isinstance(p, E) else getattr(p, "base_e", None)
            if pe is None or pe.sign is None or (not isinstance(p, E) and p.codes):
                return "", "letters: " + letters(e.form, e.harm_letters)
            signs.append("@" + pe.form.lower())
            labels.append(sign_label(pe.sign))
        dc = "".join(signs)
        if e.neg:
            return "the turned stone + " + " · ".join(labels), "!" + dc
        return " · ".join(labels), dc
    return "", "letters: " + letters(e.form, e.harm_letters)


LEXPROXY = None


class LexProxy:
    """the analyzer's lexicon interface, over the entries being built"""
    def __init__(self):
        self.by_key = defaultdict(list)
        for k, e in ENTRIES.items():
            if " " in e.form or k.startswith("suffix:"):
                continue
            self.by_key[M.nk(e.form)].append(row_of(e))
        self.keys = sorted(self.by_key)

    def get(self, form):
        return self.by_key.get(M.nk(form), [])


def row_of(e):
    return {"orrowen": e.form, "pos": ",".join(e.pos), "class": e.cls, "meanings": e.meanings(),
            "source": e.source, "hal": e.hal}


# ======================================================================= 5. write
def main():
    global LEXPROXY
    build_base()
    link_formations()
    apply_recipes()
    nsys = systematic()
    LEXPROXY = LexProxy()
    # rows
    lem_counts = {}
    for ln in open(os.path.join(HERE, "lemmas.tsv"), encoding="utf-8").read().split("\n")[1:]:
        if ln.strip():
            c = ln.split("\t")
            lem_counts[c[0]] = int(c[1])
    rows = []
    order = sorted(ENTRIES.values(), key=sort_key)
    for e in order:
        e._dc = dry_cut(e)
    for i, e in enumerate(order, 1):
        lg, dc = e._dc
        pos = ",".join(e.pos) or "n"
        rows.append(OrderedDict(
            id="O%04d" % i, orrowen=e.form, hal=e.hal or "", pos=pos, **{"class": e.cls},
            meanings=e.meanings(), canon_sense=e.canon if e.source == "canon" or e.source == "reserve" else "",
            derivation=e.derivation + ((" [" + e.flag + "]") if e.flag else ""),
            root=", ".join(dict.fromkeys(x for x in e.roots if x)), formation=e.formation, logogram=lg,
            dry_cut=dc, source=e.source, book_lemmas=", ".join(e.lemmas)))
        e.id = "O%04d" % i
    with open(OUT_TSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE,
                           escapechar="\\")
        rows = [OrderedDict((k, for_tsv(v)) for k, v in r.items()) for r in rows]
        w.writeheader()
        for r in rows:
            w.writerow(r)
    # coverage of the Book's lemmas
    cov_rows, gaps = [], []
    for ln in open(os.path.join(HERE, "lemmas.tsv"), encoding="utf-8").read().split("\n")[1:]:
        if not ln.strip():
            continue
        lem, cnt = ln.split("\t")[:2]
        got = COVER.get(lem)
        if not got:
            gaps.append(lem)
        cov_rows.append((lem, cnt, "word", got))
    for fn, kind in (("names.tsv", "name"), ("compounds.tsv", "compound")):
        for ln in open(os.path.join(HERE, fn), encoding="utf-8").read().split("\n"):
            if not ln.strip():
                continue
            nm, cnt = ln.split("\t")[:2]
            nm0 = re.sub(r"'s$", "", nm)
            got = COVER.get(nm0) or COVER.get(nm0.lower())
            if not got:
                gaps.append(nm0)
            cov_rows.append((nm0, cnt, kind, got))
    with open(os.path.join(HERE, "coverage_en.tsv"), "w", encoding="utf-8") as f:
        f.write("english\tcount\tkind\torrowen\tids\n")
        for lem, cnt, kind, got in cov_rows:
            forms = "; ".join(dict.fromkeys(g[0] for g in (got or [])))
            ids = ", ".join(dict.fromkeys(ENTRIES[g[1]].id for g in (got or []) if g[1] in ENTRIES))
            f.write("%s\t%s\t%s\t%s\t%s\n" % (lem, cnt, kind, forms or "(GAP)", ids))
    stats = dict(entries=len(rows), systematic=nsys,
                 by_source=count_by(rows, "source"), by_pos=count_by(rows, "pos"),
                 with_sign=sum(1 for r in rows if r["dry_cut"].startswith("@") and "+" not in r["dry_cut"]),
                 with_sign_complement=sum(1 for r in rows if r["dry_cut"].startswith(("@", "!@")) and "+" in r["dry_cut"]),
                 lemmas=len([c for c in cov_rows if c[2] == "word"]), gaps=gaps, errors=ERRORS)
    json.dump(stats, open(os.path.join(HERE, "stats.json"), "w"), indent=1, ensure_ascii=False)
    print("entries", len(rows), "| systematic", nsys, "| gaps", len(gaps), "| errors", len(ERRORS))
    for x in ERRORS[:80]:
        print("  ERR", x)
    if gaps:
        print("  GAPS:", " ".join(gaps[:200]))


def for_tsv(s):
    s = re.sub(r"[\t\n]+", " ", s or "")
    return s.replace('"', "'").replace("\\", "/")


def count_by(rows, col):
    d = defaultdict(int)
    for r in rows:
        d[r[col]] += 1
    return dict(sorted(d.items(), key=lambda x: -x[1]))


def sort_key(e):
    f = e.form.lower().lstrip("-")
    return (1 if e.key.startswith("suffix:") else 0, re.sub(r"[^a-z ]", "", f), f)


if __name__ == "__main__":
    main()
