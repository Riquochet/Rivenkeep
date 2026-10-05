"""The base inventory of Orrowen words, before any new derivation (scratch tool, wf7/lex).

Four sources, all read-only:
  1. ancestor/roots_core.py + formations.py: every inherited Orrowen word with its ancestral
     form, and the words Orrowen built for itself (canon);
  2. orrowen_v2.md §5: the lexicon tables (the canon senses, notes and dry-cut column);
  3. ancestor/reserve.json: the 371 reserve roots, each with its computed Orrowen and Hal form;
  4. orrowen/wordstones.json: the 328 word-signs of the dry cut (their readings, heads, crowns).
Every form is re-derived by the ancestor's engine (ancestor/laws.py) where an ancestral form
is known, and the build stops if a derivation does not give the form the sources give.
"""
import os, re, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
WF7 = os.path.normpath(os.path.join(HERE, ".."))
ANC = os.path.join(WF7, "ancestor")
sys.path.insert(0, ANC)
import laws            # noqa: E402
import roots_core      # noqa: E402
import formations      # noqa: E402

BROAD, SLENDER = "B", "S"


def last_full_vowel_class(form):
    """harmony class: the class of the last full vowel (a o u ow broad; e i y ae slender)"""
    s = form.lower()
    vs = re.findall(r"ae|ow|[aeiouy]", s)
    if not vs:
        return BROAD
    v = vs[-1]
    return SLENDER if v in ("e", "i", "y", "ae") else BROAD


def root_of(key):
    for r in roots_core.ROOTS:
        if r["key"] == key:
            return r
    return None


def canon_inherited():
    """every Orrowen word of roots_core (inherited and names), re-derived"""
    out = []
    for r in roots_core.ROOTS:
        for anc, exp, gloss, opt in r["o"]:
            o = laws.derive_o(anc, small=opt.get("small", False), compound=opt.get("compound", False),
                              keep_long_a=opt.get("keep_long_a", True), keep_wr=opt.get("keep_wr", False),
                              affix=anc.startswith("-"), harm=opt.get("harm", False))
            if exp is not None and o["living"].lower() != exp.lower():
                raise SystemExit("derivation mismatch: %s %s %s" % (anc, o["living"], exp))
            out.append(dict(form=exp, anc=anc, hal=opt.get("hal") or o["hal"], gloss=gloss,
                            root=r["root"], root_mean=r["mean"], field=r["field"], key=r["key"],
                            name=bool(opt.get("name")) or r["field"] == "name",
                            affix=anc.startswith("-"), trace=o["trace"], src="canon"))
    return out


def canon_formations():
    out = []
    for w, (parts, how) in formations.O_FORM.items():
        out.append(dict(form=w, parts=parts, how=how, src="canon"))
    return out


def v2_tables():
    """orrowen_v2 §5: form -> (hal, cls, sense, note, drycut)"""
    txt = open(os.path.join(WF7, "orrowen_v2.md"), encoding="utf-8").read()
    sec = txt.split("## 5 · LEXICON")[1].split("## 6 ·")[0]
    rows = {}
    sub = None
    for ln in sec.split("\n"):
        m = re.match(r"### (5\.\d+) ", ln)
        if m:
            sub = m.group(1)
            continue
        if not ln.startswith("| **"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        forms = re.findall(r"\*\*([^*]+)\*\*", cells[0])
        head = cells[0]
        if sub in ("5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7"):
            hal, cls, sense, note, dry = cells[1], cells[2], cells[3], cells[4], cells[5]
        elif sub in ("5.8", "5.9"):
            hal, cls, sense, note, dry = "", cells[1], cells[2], cells[3], cells[4]
        elif sub == "5.10":
            hal, cls, sense, note, dry = "", "", cells[2], "mutation after: " + cells[1], cells[3]
        elif sub == "5.11":
            continue
        elif sub == "5.12":
            continue
        else:
            continue
        for f in forms:
            rows[f.strip()] = dict(sub=sub, head=head, hal=hal.strip("*"), cls=cls, sense=sense, note=note,
                                   dry=dry)
    return rows


def reserve():
    return json.load(open(os.path.join(ANC, "reserve.json"), encoding="utf-8"))


def signs():
    d = json.load(open(os.path.join(WF7, "orrowen", "wordstones.json"), encoding="utf-8"))
    return {k: dict(n=v["n"], head=v["head"], crown=v["crown"], cls=v["cls"], pos=v["pos"], gloss=v["gloss"],
                    src=v["src"], why=v.get("why", "")) for k, v in d.items()}


def sign_name(s):
    return s["head"] + ("+" + s["crown"] if s["crown"] else "")


if __name__ == "__main__":
    inh = canon_inherited()
    fm = canon_formations()
    v2 = v2_tables()
    rs = reserve()
    sg = signs()
    print("inherited", len(inh), "formations", len(fm), "v2 rows", len(v2), "reserve", len(rs), "signs", len(sg))
    if "dump" in sys.argv:
        for e in inh:
            print("I\t%s\t%s\t%s\t%s" % (e["form"], e["hal"], e["gloss"][:70], e["root"]))
        for e in fm:
            print("F\t%s\t%s\t%s" % (e["form"], "+".join(e["parts"]), e["how"][:60]))
        for e in rs:
            print("R\t%s\t%s\t%s\t%s" % (e["o_pred"], e["hal"], e["mean"][:60], e["field"]))
    if "v2" in sys.argv:
        for f, r in v2.items():
            print(f, "|", r["sense"][:60], "|", r["dry"])
