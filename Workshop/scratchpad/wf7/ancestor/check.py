"""Run every derivation, compare with the attested forms, and report."""
import json, sys, re, importlib
import laws
sys.path.insert(0, ".")

def load_roots():
    import roots_core
    importlib.reload(roots_core)
    if "formations" in sys.modules:
        importlib.reload(sys.modules["formations"])
    else:
        import formations
    roots = list(roots_core.ROOTS)
    try:
        import roots_reserve
        importlib.reload(roots_reserve)
        roots += roots_reserve.ROOTS
    except ImportError:
        pass
    return roots

def norm(x):
    return (x or "").lower().replace("ȳ", "ȳ")

def run(verbose=False):
    roots = load_roots()
    bad = []
    rows = []
    for r in roots:
        for anc, exp, gloss, opt in r["o"]:
            o = laws.derive_o(anc, small=opt.get("small", False), compound=opt.get("compound", False),
                              keep_long_a=opt.get("keep_long_a", True), keep_wr=opt.get("keep_wr", False),
                              affix=anc.startswith("-"), harm=opt.get("harm", False))
            ok = (exp is None) or (norm(o["living"]) == norm(exp))
            hok = ("hal" not in opt) or (norm(o["hal"]) == norm(opt["hal"]))
            rows.append(("O", r["key"], anc, o["hal"], o["living"], exp, ok and hok))
            if not ok or not hok:
                bad.append(("O", r["key"], anc, "hal", o["hal"], "want", opt.get("hal"), "living", o["living"], "want", exp))
        for stem, exp, gloss, opt in r["s"]:
            s_ = laws.derive_s(stem, relic_aer=opt.get("relic_aer", False), small=opt.get("small", False),
                               affix=(stem.startswith("-") or r["field"] == "affix"))
            liv = s_["living"]
            ok = (exp is None) or norm(liv) == norm(exp)
            eok = ("eldest" not in opt) or (norm(s_["eldest"]) == norm(opt["eldest"]))
            rows.append(("S", r["key"], stem, s_["eldest"], liv, exp, ok and eok))
            if not ok or not eok:
                bad.append(("S", r["key"], stem, "eldest", s_["eldest"], "want", opt.get("eldest"), "living", liv, "want", exp))
    return roots, rows, bad

if __name__ == "__main__":
    roots, rows, bad = run()
    print(len(roots), "roots;", len(rows), "derivations;", len(bad), "mismatches")
    for b in bad:
        print("  ", b)


# ------------------------------------------------------------------ coverage
def attested():
    o = json.load(open("o_lex_raw.json")); s = json.load(open("s_lex_raw.json"))
    ow, sw = [], []
    for r in o:
        f = r["form"]
        f = re.sub(r"\(.*?\)", "", f)
        for part in f.split("·"):
            part = part.strip().strip("*").strip()
            if not part:
                continue
            ow.append((part, r["sub"], r["sense"]))
    for r in s:
        sw.append((r["form"], r["kind"], r["sense"]))
    return ow, sw

def coverage():
    import formations
    roots, rows, bad = run()
    have_o = {}
    have_s = {}
    for t, k, anc, mid, liv, exp, ok in rows:
        if liv is None:
            continue
        (have_o if t == "O" else have_s)[liv.lower()] = k
    OF = {k.lower(): v for k, v in formations.O_FORM.items()}
    SF = {k.lower(): v for k, v in formations.S_FORM.items()}
    extra_o = {"-i", "-aer"}
    def ok_o(w, depth=0):
        w = w.lower().strip()
        if w.startswith("et ") and w[3:] in have_o or w in ("et " + x for x in have_o):
            return True
        if w in have_o or w in extra_o or w.strip("-") in have_o:
            return True
        if w in OF:
            return all(ok_o(p, depth + 1) or ok_s(p) for p in OF[w][0])
        if " " in w:
            return all(ok_o(x, depth + 1) for x in w.split())
        return False
    def ok_s(w, depth=0):
        w = w.lower().strip()
        if w in have_s or w.strip("-") in have_s:
            return True
        if w in SF:
            return all(ok_s(p, depth + 1) for p in SF[w][0])
        return False
    ow, sw = attested()
    miss_o = [(w, sub) for w, sub, sense in ow if not ok_o(w)]
    miss_s = [(w, k) for w, k, sense in sw if not ok_s(w)]
    return miss_o, miss_s, len(ow), len(sw)

if __name__ == "__main__":
    mo, ms, no, ns = coverage()
    print("coverage: O", no - len(mo), "/", no, "; S", ns - len(ms), "/", ns)
    for m in mo: print("  O missing:", m)
    for m in ms: print("  S missing:", m)
