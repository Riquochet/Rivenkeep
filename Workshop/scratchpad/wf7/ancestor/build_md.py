"""Build ancestor.md from ancestor_template.md and the engine. Every table of forms is computed."""
import json, re, sys
import laws, check, predict, formations
import first_marks as FM

OUT = "/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf7/ancestor.md"
SIGNS = json.load(open("/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf6/grain/signs.json"))

FIELD_NAMES = [("stone", "Stone, wood and building"), ("bond", "Faith, bond and kin"), ("hearth", "Hearth and people"),
               ("war", "The wall, the war, the sea-road"), ("sea", "Sea, land and growing things"), ("sky", "Sky, weather, fire and time"),
               ("body", "Body, life and feeling"), ("speech", "Speech, writing and mind"), ("acts", "Other acts"),
               ("quality", "Qualities"), ("number", "Numbers"), ("small", "Small words"), ("affix", "Affixes"), ("name", "Names")]

def esc(s):
    """raw text: escape the table pipe and markdown's asterisk"""
    return s.replace("|", "\\|").replace("*", "\\*")

def pipe(s):
    """a composed cell: escape only the table pipe"""
    return s.replace("|", "\\|")

def q(g):
    """a gloss in single quotes, unless it is quoted already"""
    g = esc(g)
    return g if g.startswith("'") else "'%s'" % g

def gl(g, n=60):
    m = re.match(r"^([A-Z][a-z]+), '([^']+)'", g)
    if m:
        return "'%s'" % m.group(2)
    g = g.split(";")[0].strip()
    if len(g) > n:
        cut = g[:n]
        k = max(cut.rfind(", "), cut.rfind(": "), cut.rfind(" ("))
        if k < n // 2:
            k = cut.rfind(" ")
        g = cut[:k].rstrip(" ,:") + "…"
    if g.count("(") > g.count(")"):
        g += ")"
    return g

def anc(a):
    return "*\\*" + a + "*"

roots, rows, bad = check.run()
roots_p, have_o, have_s = predict.attested_sets()
mo, ms, no, ns = check.coverage()
reserve = json.load(open("reserve.json"))
BL = predict.BL

def o_of(anc_, opt):
    return laws.derive_o(anc_, small=opt.get("small", False), compound=opt.get("compound", False),
                         keep_long_a=opt.get("keep_long_a", True), keep_wr=opt.get("keep_wr", False),
                         affix=anc_.startswith("-"), harm=opt.get("harm", False))

def s_of(stem, opt, r):
    return laws.derive_s(stem, relic_aer=opt.get("relic_aer", False), small=opt.get("small", False),
                         affix=(stem.startswith("-") or r["field"] == "affix"))

key_of_o = {}
key_of_s = {}
for r in roots:
    for a, e, g, opt in r["o"]:
        key_of_o.setdefault(e.lower(), (r["key"], g))
    for a, e, g, opt in r["s"]:
        key_of_s.setdefault(e.lower(), (r["key"], g))

def pred_cell(r, side):
    p = predict.predict(r, have_o, have_s)
    if side not in p:
        return ""
    if side == "o":
        w, hal, liv, clash = p["o"]
        if clash:
            k = clash[0]; other = key_of_o.get(liv.lower(), (k, ""))[1]
            return "*would be* %s: falls together with %s %s" % (liv, liv, q(gl(other, 30)))
        return "*would be* %s (Hal *%s*)" % (liv, hal)
    stem, eld, liv, clash, bl = p["s"]
    if bl:
        return "*would be* %s: a lift (on the blacklist), not usable" % liv
    if clash:
        k = clash[0]; other = key_of_s.get(liv.lower(), (k, ""))[1]
        return "*would be* %s: falls together with %s %s" % (liv, liv, q(gl(other, 30)))
    return "*would be* %s" % liv

def cell_o(r):
    if not r["o"]:
        return pred_cell(r, "o") if r["field"] not in ("affix",) else "—"
    parts = []
    for a, e, g, opt in r["o"]:
        d = o_of(a, opt)
        w = d["living"]
        if opt.get("name"):
            w = w[:1].upper() + w[1:]
        h = d["hal"]
        parts.append("**%s** %s%s" % (w, q(gl(g, 48)), (" (Hal *%s*)" % h) if h.lower().strip("-") != d["living"].lower().strip("-") else ""))
    return " · ".join(parts)

def cell_s(r):
    if not r["s"]:
        return pred_cell(r, "s") if r["field"] not in ("affix", "name") else "—"
    parts = []
    for a, e, g, opt in r["s"]:
        d = s_of(a, opt, r)
        w = d["living"]
        if opt.get("name"):
            w = w[:1].upper() + w[1:]
        parts.append("**%s** %s (Eldest *%s*)" % (w, q(gl(g, 48)), d["eldest"]))
    return " · ".join(parts)

def t_core():
    out = []
    for f, title in FIELD_NAMES:
        rs = [r for r in roots if r["field"] == f]
        if not rs:
            continue
        out.append("**%s** (%d)\n" % (title, len(rs)))
        out.append("| First tongue | Meaning | Orrowen | Seilrhass |")
        out.append("|---|---|---|---|")
        for r in rs:
            star = "★ " if (r["o"] and r["s"] and f != "affix") else ""
            rootd = r["root"] if r["root"] != "—" else "—"
            out.append("| %s%s | %s | %s | %s |" % (star, ("*\\*%s*" % rootd) if rootd != "—" else "—", esc(r["mean"]), pipe(cell_o(r)), pipe(cell_s(r))))
        out.append("")
    return "\n".join(out)

def t_reserve():
    out = []
    by_s = {}
    for r in reserve:
        by_s.setdefault(r["s_pred"].lower(), []).append(r["mean"])
    for f, title in FIELD_NAMES:
        rs = [r for r in reserve if r["field"] == f]
        if not rs:
            continue
        out.append("**%s** (%d)\n" % (title, len(rs)))
        out.append("| First tongue | Meaning | Orrowen (Hal) | Seilrhass (spoken) |")
        out.append("|---|---|---|---|")
        for r in rs:
            sh = [m for m in by_s[r["s_pred"].lower()] if m != r["mean"]]
            kn = laws.knock(r["s_pred"])
            s_cell = r["s_pred"] + ((" (%s)" % kn) if kn != r["s_pred"] else "")
            if sh:
                s_cell += "; also %s" % q(gl(sh[0], 30))
            hal = r["hal"]
            out.append("| *\\*%s* | %s | %s (*%s*) | %s |" % (r["root"], esc(r["mean"]), r["o_pred"], hal, pipe(s_cell)))
        out.append("")
    return "\n".join(out)

def steps_o(d, start):
    st = d["steps"]
    s = "*\\*%s*" % start
    halstage = [x for x in st if x[0].startswith("O")]
    for law, form in st[1:]:
        if law.startswith("O"):
            s += " >%s *%s*" % (law, form)
    s += " = Hal *%s*" % d["hal"] if halstage else " = Hal *%s* (unchanged)" % d["hal"]
    for law, form in st[1:]:
        if law.startswith("H"):
            s += " >%s *%s*" % (law, form)
    return s

def t_oderiv():
    out = ["| Orrowen | Sense | How it falls out |", "|---|---|---|"]
    n = 0
    for r in roots:
        for a, e, g, opt in r["o"]:
            d = o_of(a, opt)
            w = d["living"]
            if opt.get("name"):
                w = w[:1].upper() + w[1:]
            how = steps_o(d, a)
            if opt.get("irr"):
                how += ". *%s*" % esc(opt["irr"])
            out.append("| **%s** | %s | %s |" % (w, esc(gl(g, 70)), pipe(how)))
            n += 1
    return "\n".join(out), n

def t_form(forms, side):
    out = ["| Word | Built from | How |", "|---|---|---|"]
    for w, (parts, how) in forms.items():
        out.append("| **%s** | %s | %s |" % (w, esc(" + ".join(parts)), esc(how)))
    return "\n".join(out)

def steps_s(d, start):
    st = d["steps"]
    s = "*\\*%s*" % start
    for law, form in st[1:]:
        if law in ("S1", "S2", "S3", "S4", "S5"):
            s += " >%s *%s*" % (law, form)
    s += " = Eldest *%s*" % d["eldest"]
    for law, form in st[1:]:
        if law in ("S6", "S7", "S8"):
            s += " >%s *%s*" % (law, form)
    return s

def t_sderiv():
    out = ["| Seilrhass | Spoken | Sense | How it falls out |", "|---|---|---|---|"]
    n = 0
    for r in roots:
        for a, e, g, opt in r["s"]:
            d = s_of(a, opt, r)
            w = d["living"]
            if opt.get("name"):
                w = w[:1].upper() + w[1:]
            how = steps_s(d, a)
            if opt.get("irr"):
                how += ". *%s*" % esc(opt["irr"])
            out.append("| **%s** | %s | %s | %s |" % (w, laws.knock(w) if not w.startswith("-") else w, esc(gl(g, 60)), pipe(how)))
            n += 1
    return "\n".join(out), n

def t_cognates():
    order = ["TOL", "XREUN", "TUM", "OL", "PA", "TROSK", "KRASK", "STON", "SKETH", "MOLT", "MUS", "WAQR", "WAQL", "SENN", "FEQ",
             "PAR", "ODH", "TRENN", "LENN", "WEINN", "KUL", "GREST", "KREN", "TAW", "ET", "RE", "ES", "XUI", "NA", "ANG", "ROS",
             "XWRE", "XWLE", "BRO", "TAN", "LO", "SA", "-EN"]
    byk = {r["key"]: r for r in roots}
    out = ["| First tongue | Orrowen | Seilrhass | Where it touches the Book |", "|---|---|---|---|"]
    n = 0
    for k in order:
        r = byk[k]
        ow = " · ".join("*%s* %s" % ((o_of(a, opt)["living"].capitalize() if opt.get("name") else o_of(a, opt)["living"]), esc(gl(g, 40))) for a, e, g, opt in r["o"])
        sw = " · ".join("*%s* %s" % (s_of(a, opt, r)["living"], esc(gl(g, 40))) for a, e, g, opt in r["s"])
        out.append("| *\\*%s* %s | %s | %s | %s |" % (r["root"], esc(gl(r["mean"], 44)), ow, sw, esc(r["note"] or "")))
        n += 1
    return "\n".join(out), n

def sentence(words, side):
    """words: list of (ancestral, expected living, gloss, opts)"""
    rows_ = []
    for a, exp, g, opt in words:
        if side == "o":
            d = laws.derive_o(a, small=opt.get("small", False), compound=opt.get("compound", False), harm=opt.get("harm", False))
            liv = d["living"]; mid = d["hal"].upper()
        else:
            d = laws.derive_s(a, small=opt.get("small", False)); liv = d["living"]; mid = d["eldest"]
        want = opt.get("surface", exp)
        assert liv.lower() == exp.lower(), (a, liv, exp)
        rows_.append((a, mid, liv, want, g))
    return rows_

def t_sent(rows_, side, title):
    head = "| First tongue | %s | living | as the line says it | gloss |" % ("Hal" if side == "o" else "Eldest")
    out = ["*%s*" % title, "", head, "|---|---|---|---|---|"]
    for a, mid, liv, want, g in rows_:
        out.append("| *\\*%s* | %s | %s | **%s** | %s |" % (a, mid, liv, want, g))
    return "\n".join(out)

def t_title():
    o = sentence([("ul-an", "ul", "in (+N)", dict(small=True, surface="Ul")),
                  ("tum-ol-a", "tumol", "memory", dict(surface="dumol (N after ul)")),
                  ("ol-on", "ol", "our (+N)", dict(small=True)),
                  ("waʔr-n-o-s", "varn", "home", {}),
                  ("ol-on", "ol", "our", dict(small=True)),
                  ("thald-athi", "thaldath", "families", dict(surface="theldeth (rebuilt on theld-)")),
                  ("ol-on", "ol", "our", dict(small=True)),
                  ("mardh-o-s", "mardh", "God", dict(surface="Mardh")),
                  ("ol-on", "ol", "our", dict(small=True)),
                  ("lunn-athi", "lunnath", "freedoms", {}),
                  ("ol-on", "ol", "our", dict(small=True)),
                  ("soʔl-an-o-s", "sollan", "peace", {})], "o")
    h = sentence([("tum-ar", "tumar", "hold-1PL: we remember", dict(surface="Tumar"))], "o")
    s = sentence([("be", "ve", "we", dict(small=True, surface="Ve")),
                  ("itt-o", "ith", "own", {}),
                  ("molt-o", "nael", "breath (+ enn: home)", dict(surface="naelenn (nael + enn)")),
                  ("enn-o", "enn", "within", dict(surface="(in naelenn)")),
                  ("ol", "ael", "too, together", {}),
                  ("ral-o", "ral", "root (+ thein: remember)", dict(surface="raltheine (ral + thein + -e)")),
                  ("tum-i", "thein", "hold", dict(surface="(in raltheine)")),
                  ("e", "e", "now: the present", dict(surface="(-e)"))], "s")
    return "\n\n".join([t_sent(o, "o", "The Title: Ul dumol ol varn, ol theldeth, ol Mardh, ol lunnath, ol sollan."),
                        t_sent(h, "o", "The hearth's answer: Tumar."),
                        t_sent(s, "s", "The sliver: Ve ith naelenn ael raltheine.")])

def t_proverb():
    o = sentence([("grest-o-s", "grest", "harm", dict(surface="Grest")), ("um-o", "um", "upon (+S)", dict(small=True)),
                  ("hos-o-s", "hos", "one", {}), ("grest-o-s", "grest", "harm", {}), ("um-o", "um", "upon (+S)", dict(small=True)),
                  ("pa-naʔ", "pana", "both", dict(surface="vana (S after um)"))], "o")
    s = sentence([("itt-o", "ith", "one", dict(surface="Ith")), ("li", "li", "at", dict(small=True)),
                  ("trosk-i", "thaess", "a wound (O tresk, riven)", {}), ("pann-i", "vann", "two (O pana, both)", {}),
                  ("li", "li", "at", dict(small=True)), ("trosk-i", "thaess", "a wound", {})], "s")
    return "\n\n".join([t_sent(o, "o", "Orrowen: Grest um hos, grest um vana. (Hal GRESTOS UMO HOSOS GRESTOS UMO PANĀ, exactly.)"),
                        t_sent(s, "s", "Seilrhass: Ith li thaess, vann li thaess.")])

def t_stonwryt():
    w = [("es-an", "es", "FUT (+N)", dict(small=True, surface="Es")), ("ston-o-s", "ston", "stand-3SG", {}),
         ("et-as", "et", "the", dict(small=True)), ("xal-d-o-s", "hald", "wall", {}), ("siu", "sy", "this", dict(small=True)),
         ("re", "re", "PST (+S)", dict(small=True, surface="Re")), ("kadh-ana", "cadhan", "lay-1DU", dict(surface="hadhan (S after re)")),
         ("o-a", "o", "it", dict(small=True)), ("eth-as", "eth", "and", dict(small=True)),
         ("tess-ana", "tessen", "answer-1DU", dict(harm=True)), ("o-a", "o", "it", dict(small=True)),
         ("soŋ-ma-s", "somm", "while", dict(small=True)), ("el-i-s", "el", "is", {}), ("tolm-o-s", "tolm", "stone", {}),
         ("tolm-o-s", "tolm", "stone", {}), ("ston-o-s", "ston", "it stands", dict(surface="Ston."))]
    o = sentence(w, "o")
    return t_sent(o, "o", "ESAN STONOS ETAS XALDOS SIU · RE CADHANA OA ETHAS TESSANA OA SOŊMAS ELIS TOLMOS TOLMOS · STONOS: each Hal word is also the first tongue's")

def t_guest():
    o = sentence([("hess-i-s", "hess", "stop", dict(surface="Hess…")), ("half-i-s", "helv", "the upper air, sky", dict(surface="Helv…")),
                  ("senn-i-s", "senn", "go down: die (+ -Ol, dying)", dict(surface="Sennyl…"))], "o")
    s = sentence([("kul-i", "rheil", "stop (O kyl, change)", {}), ("molt-o", "nael", "sky, breath (O molt, heart)", {}),
                  ("feʔs-i", "veas", "die (O vess, night)", dict(surface="vease")), ("senn-i", "senn", "beneath (O senn, die)", {})], "s")
    return "\n\n".join([t_sent(o, "o", "What he said, in the shore's tongue: Hess… Helv… Sennyl…"),
                        t_sent(s, "s", "What his own tongue says for the same, and the word at the end of the gift's sentence")])

def t_seren():
    d = laws.derive_o("swe-reŋ-o-s")
    assert d["living"] == "seren" and d["hal"] == "sereŋos"
    lines = ["| Stage | Form | Law |", "|---|---|---|", "| the first tongue | *\\*swe-reŋ-o-s* | single + a sorrow that overcomes + the nominative |"]
    for law, form in d["steps"][1:]:
        what = {"O4": "*sw-* > *s-* (O4): the Hal's **SEREŊOS**", "H2": "the ending falls (H2)", "H4": "*ŋ* > *n* (H4): living **Seren**"}.get(law, law)
        lines.append("| %s | *%s* | %s |" % ("the Hal" if law.startswith("O") else "living Orrowen", form, what))
    s = laws.derive_s("swe-reŋ-o")
    # the wood's laws, as the engine fires them (the bare stem *swe-reŋ-o: S3 thins the -o, S7 drops it)
    what_s = {"S3": "S3 *-o* > *-e*", "S4": "S4 *ŋ* > *n*", "S5": "S5 *sw-* > *s-*", "S7": "S7 the final *-e* falls"}
    assert s["trace"] == ["S3", "S4", "S5", "S7"], s["trace"]
    lines.append("| (in the wood's tongue) | *%s* | from the bare stem *\\*swe-reŋ-o*: %s; spoken *%s* |" % (
        s["living"], ", ".join(what_s[t] for t in s["trace"]), laws.knock(s["living"])))
    return "\n".join(lines)

def t_marks():
    out = ["| # | Mark | First-tongue word | Meaning | On stone | In wood |", "|---|---|---|---|---|---|"]
    for i, (k, m) in enumerate(FM.MARKS.items(), 1):
        out.append("| %d | **%s** | *\\*%s* | %s | %s | %s |" % (i, m["name"], m["word"], esc(m["mean"]), esc(m["stone"]), esc(m["wood"])))
    return "\n".join(out)

def t_laws(L):
    out = ["| Law | | What happens |", "|---|---|---|"]
    for k, t, d in L:
        out.append("| **%s** | %s | %s |" % (k, t, esc(d)))
    return "\n".join(out)

def t_letters():
    out = ["| Letter | Upright (place) | Laid stones (manner) | Note |", "|---|---|---|---|"]
    for L_, place, man, note in FM.LETTERS:
        up = FM.UPRIGHT[place]; desc, src = FM.MANNER[man]
        upn = FM.MARKS[up]["name"]
        mans = esc(desc) + ((" (from %s, *\\*%s*)" % (FM.MARKS[src]["name"], FM.MARKS[src]["word"])) if src else "")
        out.append("| **%s** | the %s (from %s, *\\*%s*) | %s | %s |" % (L_, place, upn, FM.MARKS[up]["word"], pipe(mans), esc(note)))
    return "\n".join(out)

def t_vowels():
    out = ["| Vowel | From | How |", "|---|---|---|"]
    for v, src, how in FM.VOWELS:
        out.append("| **%s** | %s (*\\*%s*) | %s |" % (v, FM.MARKS[src]["name"], FM.MARKS[src]["word"], esc(how)))
    return "\n".join(out)

def t_stonemarks():
    out = ["| Mark | From | How |", "|---|---|---|"]
    for mk, src, how in FM.MARKS_STONE:
        srcs = " + ".join(FM.MARKS[x.strip()]["name"] for x in src.split("+"))
        out.append("| **%s** | %s | %s |" % (mk, srcs, esc(how)))
    return "\n".join(out)

def t_grain():
    out = ["| Sign | Soft reading | From the first marks | Laws | How |", "|---|---|---|---|---|"]
    for k, (marks, lw, how) in FM.GRAIN.items():
        soft = SIGNS[k]["soft"]
        ms_ = " + ".join(FM.MARKS[m]["name"] for m in marks)
        out.append("| **%s** | *%s* | %s | %s | %s |" % (k, soft, ms_, lw, esc(how)))
    return "\n".join(out)

def t_bands():
    out = ["| Band | From | How |", "|---|---|---|"]
    for k, (marks, lw, how) in FM.BANDS.items():
        out.append("| **%s** | %s | %s |" % (k, " + ".join(FM.MARKS[m]["name"] for m in marks), esc(how)))
    return "\n".join(out)

def t_devices():
    out = ["| Device | Where it comes from | Laws |", "|---|---|---|"]
    for k, how, lw in FM.DEVICES:
        out.append("| **%s** | %s | %s |" % (k, esc(how), lw))
    return "\n".join(out)

def main():
    tpl = open("ancestor_template.md").read()
    oder, n_o = t_oderiv()
    sder, n_s = t_sderiv()
    cog, n_cog = t_cognates()
    n_core = len(roots)
    n_res = len(reserve)
    bad_s = "%d" % len(bad)
    check_txt = "\n".join([
        "- **%d derivations** from **%d inherited roots**, run by `check.py`: **%d mismatches**. Every Hal form the shoreland spec gives comes out exactly (three are emended first, §4.3), and so does every Eldest form the mystaeri spec gives (*\\*thaele* as a stage of *thael*, *\\*senne*)." % (len(rows), n_core, len(bad)),
        "- **Coverage:** %d of %d Orrowen lexicon entries (every entry of shoreland spec §4.5, §4.6 and §5, split at its ·) and %d of %d Seilrhass entries (all of `wf6/lang/lexicon.tsv`) are derived, directly or as a formation whose every part is derived." % (no - len(mo), no, ns - len(ms), ns),
        "- **The canon Hal texts** (the Stonwryt, the proverb) are reproduced word for word (§1.6), and so are the Title, the hearth's answer, the sliver's sentence and the Guest's words.",
        "- **Reserve:** %d roots; every one derives in both tongues by the same laws, and none collides with an existing word." % n_res,
        "- **What the check cannot do:** it cannot judge beauty or originality. The reserve forms were screened against the Tolkien and franchise blacklist, the spec's rejected forms and the whole English dictionary (about 236,000 words), but a dictionary pass against Welsh, Irish and the Tolkien lexicons (shoreland spec §9c) is still owed for any reserve word before it ships.",
    ])
    rep = {
        "{{N_ROOTS}}": str(n_core + n_res), "{{N_CORE}}": str(n_core), "{{N_RESERVE}}": str(n_res),
        "{{N_COG}}": str(n_cog), "{{COV_O}}": "%d of %d" % (no - len(mo), no), "{{COV_S}}": "%d of %d" % (ns - len(ms), ns),
        "{{N_BAD}}": bad_s, "{{N_DERIV}}": str(len(rows)), "{{N_MARKS}}": str(len(FM.MARKS)),
        "{{T_COGNATES}}": cog, "{{T_CORE}}": t_core(), "{{T_RESERVE}}": t_reserve(),
        "{{T_ODERIV}}": oder, "{{T_OFORM}}": t_form(formations.O_FORM, "o"), "{{T_SDERIV}}": sder, "{{T_SFORM}}": t_form(formations.S_FORM, "s"),
        "{{T_TITLE}}": t_title(), "{{T_PROVERB}}": t_proverb(), "{{T_STONWRYT}}": t_stonwryt(), "{{T_GUEST}}": t_guest(), "{{T_SEREN}}": t_seren(),
        "{{T_MARKS}}": t_marks(), "{{T_STONELAWS}}": t_laws(FM.STONE_LAWS), "{{T_WOODLAWS}}": t_laws(FM.WOOD_LAWS),
        "{{T_LETTERS}}": t_letters(), "{{T_VOWELS}}": t_vowels(), "{{T_STONEMARKS}}": t_stonemarks(),
        "{{T_GRAIN}}": t_grain(), "{{T_BANDS}}": t_bands(), "{{T_DEVICES}}": t_devices(), "{{CHECK}}": check_txt,
    }
    for k, v in rep.items():
        tpl = tpl.replace(k, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", tpl)
    assert not left, left
    open(OUT, "w").write(tpl)
    print("wrote", OUT, len(tpl), "chars;", tpl.count("\n"), "lines; O rows", n_o, "S rows", n_s, "cognates", n_cog)

if __name__ == "__main__":
    main()
