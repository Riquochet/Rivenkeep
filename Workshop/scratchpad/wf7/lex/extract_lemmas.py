"""Extract every distinct English lemma of the Book's STONE text (scratch tool, wf7/lex).

The stone text of wf6/legends_v12.md is:
  - the front matter (title, subtitle, CONTENTS, OF THIS BOOK, THE INVOCATION);
  - every book heading and its italic line, and every tale heading;
  - every stone leaf, whole, except the passages its markers give to the wood:
      <!-- W -->                 the next paragraph or verse
      <!-- W (inline): ...seven paragraphs, and *Burn* below -->  the leading <em> of the next 7
                                   paragraphs, and the *Burn* after them
      <!-- W (inline): the italic line in the next paragraph -->  that paragraph's <em> parts
      <!-- W (by line): ... line 3 ... -->  that line of the next verse
  - on a wood leaf (headnote begins "*As the Mystwood remembers"): the title, Seren's headnote,
    and Seren's frames after the wood's telling ("*And no one answered.*", the facing-leaf note);
  - the Epilogue (its MIXED inscription is stone letters);
  - the Appendix's own prose and its table, except the column "The carvings, youngest to eldest"
    (the wood's words).
Left out: the editor's note, HTML comments, ::: native / ::: note blocks (surface captions and
Translation folds for the builder), {TOKENS}, ⟦drawings⟧, and everything from
"# HOW THE LEGENDS ENTER THE GAME" on.

Writes lex/stone_text.txt (the text kept, one paragraph a line, with its tale) and
lex/lemmas.tsv (lemma, count, first tale, forms seen, class: word|name|compound-part).
"""
import os, re, sys, json
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
WF6 = os.path.join(HERE, "..", "..", "wf6")
SRC = os.path.join(WF6, "legends_v12.md")


def stone_paragraphs():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    out = []            # (tale, text)
    tale = "front"
    kind = "stone"      # of the current leaf
    in_comment = False
    in_native = False
    in_editor = False
    w_block = False
    w_lead = 0
    w_burn = False
    w_all = False
    w_line = None
    wood_body = False   # inside a wood leaf's telling
    headnote_pending = False
    verse = []
    table_wood_col = None

    def flush_verse():
        nonlocal verse, w_block, w_line
        if verse:
            keep = []
            for n, v in enumerate(verse, 1):
                if w_block:
                    continue
                if w_line is not None and n == w_line:
                    continue
                keep.append(v)
            if keep:
                out.append((tale, " / ".join(keep)))
            verse = []
            w_block = False
            w_line = None

    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        s = raw.strip()
        if s.startswith("# HOW THE LEGENDS ENTER THE GAME"):
            break
        if "HOW THE LEGENDS ENTER THE GAME" in s:
            continue   # the CONTENTS line for the builder's section: not the Book
        # html comments (may span lines)
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            body = s
            if "-->" not in s:
                in_comment = True
            if body.startswith("<!-- W -->"):
                w_block = True
            elif body.startswith("<!-- W (inline): the italic carving"):
                w_lead = 7; w_burn = True
            elif body.startswith("<!-- W (inline): the italic line"):
                w_all = True
            elif body.startswith("<!-- W (by line)"):
                m = re.search(r"line (\d+)", body)
                w_line = int(m.group(1)) if m else None
            continue
        # strip inline comments
        s = re.sub(r"<!--.*?-->", "", s)
        # editor's note blockquote at the top
        if s.startswith("> **Editor's note"):
            in_editor = True
        if in_editor:
            if s == "---":
                in_editor = False
            continue
        # native / note blocks (also inside blockquotes)
        t = s[1:].strip() if s.startswith(">") else s
        if t.startswith("::: native") or t == "::: note":
            in_native = True
            continue
        if in_native:
            if t == ":::":
                in_native = False
            continue
        if s == "---":
            flush_verse(); continue
        # headings
        if s.startswith("#"):
            flush_verse()
            h = s.lstrip("#").strip()
            if s.startswith("### "):
                tale = h.split("·")[0].strip() if "·" in h else h
                headnote_pending = True
                wood_body = False
                kind = "stone"
            elif s.startswith("## "):
                if h.startswith("BOOK") or h.startswith("EPILOGUE") or h.startswith("APPENDIX"):
                    tale = h.split("·")[0].strip()
                elif h in ("CONTENTS", "OF THIS BOOK", "THE INVOCATION"):
                    tale = h
                headnote_pending = h.startswith("OF THIS BOOK") or h.startswith("APPENDIX")
                wood_body = False
            out.append((tale, h))
            continue
        if not s:
            flush_verse(); continue
        # verse lines (blockquote with trailing double space, or "> *...*")
        if s.startswith(">"):
            q = s[1:].strip()
            if not q:
                continue
            if wood_body:
                continue
            verse.append(q)
            continue
        flush_verse()
        # a wood leaf is keyed on its headnote
        if headnote_pending and s.startswith("*"):
            headnote_pending = False
            if s.startswith("*As the Mystwood remembers"):
                kind = "wood"
                out.append((tale, s))
                wood_body = True
                continue
            out.append((tale, s))
            continue
        headnote_pending = False
        if wood_body:
            if s.startswith("*And no one answered"):
                wood_body = False
                out.append((tale, s))
            continue
        # tables
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            if "The carvings, youngest to eldest" in cells:
                table_wood_col = cells.index("The carvings, youngest to eldest")
            if table_wood_col is not None and table_wood_col < len(cells):
                cells = [c for k, c in enumerate(cells) if k != table_wood_col]
            if tale == "APPENDIX" and len(cells) >= 3:
                cells[-1] = re.sub(r"\*[^*]+\*", "", cells[-1])
            out.append((tale, " | ".join(cells)))
            continue
        table_wood_col = None
        if w_block:
            w_block = False
            continue
        if w_lead > 0:
            s = re.sub(r"^\*[^*]+\*", "", s)
            w_lead -= 1
        elif w_burn and "*Burn*" in s:
            s = s.replace("*Burn*", "")
            w_burn = False
        if w_all:
            s = re.sub(r"\*[^*]+\*", "", s)
            w_all = False
        out.append((tale, s))
    flush_verse()
    return out


def clean(s):
    s = re.sub(r"\{[A-Z_]+\}", " ", s)
    s = re.sub(r"\b[IVX]+\.\d\b", " ", s)
    s = re.sub(r"^\**[IVX]+ ·", " ", s)
    s = re.sub(r"\b(Part|BOOK) [IVX]+\b", r"\1", s)
    s = re.sub(r"\[?⟦[^⟧]*⟧\]?", " ", s)
    s = s.replace("**", "").replace("*", "")
    s = re.sub(r"`[^`]*`", " ", s)
    return s


# ---------------------------------------------------------------- lemmatiser
DICT = set(w.strip() for w in open("/usr/share/dict/words", encoding="utf-8"))
DICT_LOWER = set(w for w in DICT if w.islower())

BRIT = {"harbour": "harbor", "colour": "color", "honour": "honor", "labour": "labor", "armour": "armor",
        "neighbour": "neighbor", "favour": "favor", "rumour": "rumor", "valour": "valor", "vapour": "vapor",
        "grey": "gray", "plough": "plow", "chequered": "checkered", "counselled": "counseled",
        "traveller": "traveler", "neutralized": "neutralize", "defence": "defense", "centre": "center",
        "metre": "meter", "sceptre": "scepter", "splendour": "splendor", "odour": "odor",
        "behaviour": "behavior", "endeavour": "endeavor", "clamour": "clamor", "ardour": "ardor",
        "mould": "mold", "smoulder": "smolder", "saviour": "savior", "fervour": "fervor",
        "vigour": "vigor", "rigour": "rigor", "harbourhouse": "harborhouse"}

IRR = {
 # be, have, do
 "is": "be", "are": "be", "am": "be", "was": "be", "were": "be", "been": "be", "being": "be", "be": "be",
 "has": "have", "had": "have", "having": "have", "does": "do", "did": "do", "done": "do", "doing": "do",
 # pronouns and determiners kept as their own lemma families
 "me": "i", "my": "i", "mine": "i", "myself": "i", "us": "we", "our": "we", "ours": "we", "ourselves": "we",
 "him": "he", "his": "he", "himself": "he", "her": "she", "hers": "she", "herself": "she",
 "them": "they", "their": "they", "theirs": "they", "themselves": "they", "its": "it", "itself": "it",
 "your": "you", "yours": "you", "yourself": "you", "yourselves": "you", "an": "a", "these": "this",
 "those": "that", "whom": "who", "whose": "who",
 # irregular verbs
 "went": "go", "gone": "go", "goes": "go", "came": "come", "saw": "see", "seen": "see", "took": "take",
 "taken": "take", "gave": "give", "given": "give", "knew": "know", "known": "know", "found": "find",
 "told": "tell", "held": "hold", "laid": "lay", "sat": "sit", "stood": "stand", "felt": "feel",
 "left": "leave", "lost": "lose", "made": "make", "meant": "mean", "met": "meet", "ran": "run",
 "rose": "rise", "risen": "rise", "said": "say", "sang": "sing", "sung": "sing", "sank": "sink",
 "sunk": "sink", "sent": "send", "shook": "shake", "slept": "sleep", "spoke": "speak", "spoken": "speak",
 "spent": "spend", "struck": "strike", "swore": "swear", "sworn": "swear", "taught": "teach",
 "thought": "think", "threw": "throw", "thrown": "throw", "tore": "tear", "torn": "tear",
 "understood": "understand", "wept": "weep", "woke": "wake", "woken": "wake", "wore": "wear",
 "worn": "wear", "wrote": "write", "written": "write", "bore": "bear", "borne": "bear", "began": "begin",
 "begun": "begin", "bent": "bend", "bound": "bind", "brought": "bring", "built": "build",
 "bought": "buy", "caught": "catch", "chose": "choose", "chosen": "choose", "crept": "creep",
 "drank": "drink", "drew": "draw", "drawn": "draw", "drove": "drive", "driven": "drive", "dug": "dig",
 "ate": "eat", "eaten": "eat", "fed": "feed", "fled": "flee", "flew": "fly", "flung": "fling",
 "forgot": "forget", "forgotten": "forget", "forgave": "forgive", "forgiven": "forgive", "froze": "freeze",
 "frozen": "freeze", "got": "get", "grew": "grow", "grown": "grow", "hung": "hang", "heard": "hear",
 "hid": "hide", "hidden": "hide", "kept": "keep", "knelt": "kneel", "leapt": "leap", "led": "lead",
 "lit": "light", "paid": "pay", "rang": "ring", "rode": "ride", "ridden": "ride", "sawn": "saw",
 "shone": "shine", "shot": "shoot", "slain": "slay", "slew": "slay", "slid": "slide", "sought": "seek",
 "sped": "speed", "spilt": "spill", "sprang": "spring", "stole": "steal", "stolen": "steal",
 "stuck": "stick", "strode": "stride", "swam": "swim", "swept": "sweep", "swung": "swing",
 "trod": "tread", "trodden": "tread", "wove": "weave", "woven": "weave", "won": "win", "clad": "clad",
 "lain": "lie", "dealt": "deal", "fought": "fight", "fell": "fall", "fallen": "fall", "wed": "wed",
 "outlive": "outlive", "withheld": "withhold", "overcame": "overcome", "undid": "undo", "arose": "arise",
 "forbade": "forbid", "forbidden": "forbid", "blew": "blow", "blown": "blow", "broke": "break",
 "broken": "break", "shaken": "shake", "stricken": "strike", "sewn": "sew", "sown": "sow",
 "hewn": "hew", "mown": "mow", "swollen": "swell", "burnt": "burn", "learnt": "learn", "dreamt": "dream",
 "spun": "spin", "wound": "wound", "ground": "ground", "felled": "fell", "lay": "lay", "lying": "lie",
 "lies": "lie", "lied": "lie", "dying": "die", "died": "die", "dies": "die", "tying": "tie",
 "saying": "say", "says": "say",
 # nouns
 "men": "man", "women": "woman", "children": "child", "feet": "foot", "teeth": "tooth", "lives": "life",
 "wives": "wife", "knives": "knife", "halves": "half", "selves": "self", "wolves": "wolf",
 "shelves": "shelf", "thieves": "thief", "mice": "mouse", "geese": "goose", "oxen": "ox",
 "leaves": "leaf", "people": "people", "dice": "die", "fishermen": "fisherman", "axemen": "axeman",
 "quarrymen": "quarryman", "noblemen": "nobleman", "noblemen's": "nobleman", "sons": "son",
 "boughs": "bough", "news": "news", "glasses": "glass",
 # adjectives, adverbs
 "better": "good", "best": "good", "worse": "bad", "worst": "bad", "further": "far", "furthest": "far",
 "farther": "far", "less": "little", "least": "little", "more": "much", "most": "much",
 "elder": "elder", "eldest": "old", "older": "old", "oldest": "old",
}
KEEP = {"news", "always", "towards", "whereas", "various", "alms", "thus", "yes", "perhaps", "is",
        "was", "has", "this", "its", "us", "his", "hers", "ours", "yours", "theirs", "less", "unless",
        "across", "princess", "series", "species", "christmas", "moss", "grass", "glass", "pass", "mass",
        "brass", "cross", "loss", "boss", "hiss", "kiss", "miss", "bliss", "bless", "dress", "press",
        "stress", "chess", "mess", "guess", "ness", "less", "ashes", "nevertheless", "canvas", "atlas",
        "bus", "plus", "thus", "virus", "chaos", "crisis", "basis", "gas", "alias", "bias",
        "iris", "tennis", "fetus", "abyss", "compass", "harness", "fortress", "mistress", "wilderness",
        "witness", "business", "darkness", "goodness", "kindness", "business", "stillness", "wholeness",
        "sickness", "weakness", "readiness", "hardness", "rightness", "whiteness", "blindness",
        "gladness", "fairness", "boldness", "loneliness", "harshness", "fickleness", "greatness",
        "sadness", "emptiness", "quietness", "swiftness", "bitterness", "happiness", "forgiveness",
        "holiness", "politics", "tidings", "annals", "trappings", "means", "savings", "winnings",
        "odds", "thanks", "arms_", "wits", "outskirts", "surroundings", "whereabouts", "ruins", "riches",
        "always", "sometimes", "afterwards", "backwards", "forwards", "upwards", "downwards",
        "inwards", "outwards", "sideways", "nowadays", "hers", "besides", "else", "upstairs",
        "downstairs", "overseas", "whilst", "amongst", "betwixt", "yes"}


def in_dict(w):
    return w in DICT_LOWER or BRIT.get(w, "") in DICT_LOWER


def lemma(w):
    """a lowercase word form -> its lemma (rule-based, dictionary-checked)"""
    if w in OVERRIDE:
        return OVERRIDE[w]
    if w in IRR:
        return IRR[w]
    if w in KEEP:
        return w
    if w.endswith("'s"):
        w = w[:-2]
        if w in IRR:
            return IRR[w]
    if w.endswith("s'"):
        w = w[:-1]
    cands = []
    # plurals / 3sg
    if w.endswith("ies") and len(w) > 4:
        cands.append(w[:-3] + "y")
    if w.endswith("ves") and len(w) > 4:
        cands += [w[:-3] + "f", w[:-3] + "fe"]
    if w.endswith("es") and len(w) > 3:
        cands.append(w[:-2])
    if w.endswith("s") and not w.endswith("ss") and len(w) > 2:
        cands.append(w[:-1])
    # past / participle
    if w.endswith("ied") and len(w) > 4:
        cands.append(w[:-3] + "y")
    if w.endswith("ed") and len(w) > 3:
        b = w[:-2]
        cands += [b + "e", b] if not in_dict(b) else [b, b + "e"]
        if len(b) > 2 and b[-1] == b[-2] and b[-1] not in "ls":
            cands.insert(0, b[:-1])
        if len(b) > 2 and b[-1] == b[-2]:
            cands.append(b[:-1])
    if w.endswith("ing") and len(w) > 4:
        b = w[:-3]
        if len(b) > 2 and b[-1] == b[-2] and b[-1] not in "ls":
            cands.append(b[:-1])
        cands += [b, b + "e"] if in_dict(b) else [b + "e", b]
        if len(b) > 2 and b[-1] == b[-2]:
            cands.append(b[:-1])
        if b.endswith("y"):
            cands.append(b[:-1] + "ie")
    # comparatives of adjectives
    for suf in ("iest", "ier"):
        if w.endswith(suf):
            cands.append(w[:-len(suf)] + "y")
    for suf in ("est", "er"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            b = w[:-len(suf)]
            if len(b) > 2 and b[-1] == b[-2]:
                cands.append(b[:-1])
            cands += [b, b + "e"]
    # prefer a candidate the Book itself uses as a bare word, then a dictionary word
    cands = [c for c in cands if len(c) >= 2]
    booked = [c for c in cands if c in BOOK_FORMS]
    if booked:
        cands = booked + [c for c in cands if c not in booked]
    for c in cands:
        if (c in BOOK_FORMS or in_dict(c)) and len(c) >= 2:
            # an -er noun (singer, runner) is a word of its own: keep the form when it is itself a word
            if (w.endswith("er") or w.endswith("est")) and in_dict(w) and not w.endswith("ier"):
                return w
            if w.endswith("ing") and in_dict(w) and w in NOUN_ING:
                return w
            if w.endswith("ed") and in_dict(w) and w in ADJ_ED:
                return w
            return c
    return w


# -ing and -ed forms that the Book uses as nouns or adjectives in their own right
NOUN_ING = {"building", "evening", "morning", "meaning", "beginning", "ending", "feeling", "warning",
            "ceiling", "offering", "carving", "telling", "knowing", "holding", "laying", "hauling",
            "sealing", "felling", "growing", "naming", "cutting", "kindling", "sapling", "seedling",
            "fledgling", "dwelling", "gathering", "reckoning", "blessing", "wedding", "sitting",
            "shilling", "piling", "landing", "sounding", "turning", "gallery", "sibling", "wing",
            "string", "thing", "king", "ring", "spring", "nothing", "something", "anything",
            "everything", "during", "bring", "sing", "sting", "swing", "cling", "fling", "sling",
            "wring", "ding", "ping", "bling", "hireling", "treeling", "yearling", "darling",
            "harvesting", "forgetting", "going", "coming", "keeping", "killing", "standing",
            "understanding", "shingle"}
ADJ_ED = {"hundred", "sacred", "wicked", "naked", "rugged", "ragged", "crooked", "beloved",
          "learned", "aged", "bed", "red", "shed", "need", "seed", "deed", "feed", "speed", "weed",
          "bleed", "breed", "creed", "greed", "reed", "steed", "tweed", "wed", "sled", "fled", "led",
          "shred", "bred", "sped", "embed", "kindred", "hatred", "wretched", "dogged", "blessed",
          "cursed", "winged", "wounded", "orphaned", "bonded", "unbonded", "silvered", "charred",
          "laden", "feigned", "untold", "unknown", "unbroken", "unwelcome"}


BOOK_FORMS = set()
# names that are also English words (Hale, Marl ...): a capitalised use is always the name
NAME_FORCE = {"Hale", "Harl", "Marl", "Lanner", "Voss", "Tamm", "Aske", "Kael", "Brenn", "Seren", "Corlen",
              "Garvel", "Ulden", "Hesk", "Pellow", "Stannard", "Tarnel", "Rivenkeep", "RIVENKEEP", "Halyna",
              "Halvard", "Rhyna", "Aldwena", "Idrenna"}
OVERRIDE = {}

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ'’]+(?:-[A-Za-zÀ-ÿ'’]+)*")


def main():
    paras = stone_paragraphs()
    whole = open(SRC, encoding="utf-8").read().split("# HOW THE LEGENDS ENTER THE GAME")[0]
    for m in WORD_RE.finditer(clean(whole)):
        for p in m.group(0).lower().replace("’", "'").split("-"):
            BOOK_FORMS.add(p.strip("'"))
    ov = os.path.join(HERE, "lemma_overrides.tsv")
    if os.path.exists(ov):
        for ln in open(ov, encoding="utf-8"):
            if ln.strip() and not ln.startswith("#"):
                a, b = ln.rstrip("\n").split("\t")[:2]
                OVERRIDE[a] = b
    with open(os.path.join(HERE, "stone_text.txt"), "w", encoding="utf-8") as f:
        for tale, t in paras:
            f.write("%s\t%s\n" % (tale, t))
    count = Counter()
    first = {}
    forms = defaultdict(set)
    compounds = Counter()
    names = Counter()
    ntok = 0
    for tale, t in paras:
        t = clean(t)
        # sentence starts: a capital after . ! ? : " or at the start
        for m in WORD_RE.finditer(t):
            tokn = m.group(0).replace("’", "'").strip("'")
            if not tokn:
                continue
            start = m.start()
            pre = t[:start].rstrip()
            sent_start = (not pre) or pre[-1] in '.!?:;"“(—|/…' or pre.endswith("·")
            parts = tokn.split("-")
            if len(parts) > 1:
                compounds[tokn.lower()] += 1
            for k, p in enumerate(parts):
                if not p:
                    continue
                ntok += 1
                low = p.lower()
                bare = re.sub(r"'s$", "", p)
                if bare in NAME_FORCE:
                    names[bare] += 1
                    continue
                if p[0].isupper() and not p.isupper():
                    lem = lemma(low)
                    # a capitalised word that is not a dictionary word (in any case) is a name
                    if not (sent_start and k == 0) or not (in_dict(lem) or in_dict(low) or low in IRR):
                        if not in_dict(lem) and not in_dict(low) and low not in IRR:
                            names[p] += 1
                            continue
                        # a capital inside a sentence on a dictionary word: a proper use (the Keep,
                        # the Captain, the Stonewrights) still counts as the word
                elif p.isupper() and len(p) > 1:
                    low = p.lower()
                lem = lemma(low)
                count[lem] += 1
                forms[lem].add(low)
                first.setdefault(lem, tale)
    with open(os.path.join(HERE, "lemmas.tsv"), "w", encoding="utf-8") as f:
        f.write("lemma\tcount\tfirst\tforms\tin_dict\n")
        for lem, c in sorted(count.items(), key=lambda x: (-x[1], x[0])):
            f.write("%s\t%d\t%s\t%s\t%s\n" % (lem, c, first[lem], ",".join(sorted(forms[lem])),
                                              "y" if in_dict(lem) else "n"))
    with open(os.path.join(HERE, "names.tsv"), "w", encoding="utf-8") as f:
        for n, c in names.most_common():
            f.write("%s\t%d\n" % (n, c))
    with open(os.path.join(HERE, "compounds.tsv"), "w", encoding="utf-8") as f:
        for n, c in compounds.most_common():
            f.write("%s\t%d\n" % (n, c))
    print("paragraphs", len(paras), "tokens", ntok, "lemmas", len(count), "names", len(names),
          "hyphenated", len(compounds), "not-in-dict", sum(1 for l in count if not in_dict(l)))


if __name__ == "__main__":
    main()
