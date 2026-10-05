"""Predicted reflexes: what each root would be in the tongue that did not keep it."""
import laws, check, re

def attested_sets():
    roots, rows, bad = check.run()
    o = {}; s = {}
    for t, k, anc, mid, liv, exp, ok in rows:
        if liv:
            (o if t == "O" else s).setdefault(liv.lower(), []).append(k)
    return roots, o, s

BL = set(open("/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf6/lang/blacklist.txt").read().split())

def predict(r, have_o, have_s):
    out = {}
    stem = r.get("stem")
    if not stem:
        return out
    small = r["field"] == "small"
    affix = r["field"] == "affix"
    if not r["o"]:
        w = stem if (small or affix or stem.endswith("ʔ") or stem.endswith("a")) else stem + "s"
        d = laws.derive_o(w, small=small, affix=affix)
        liv = d["living"]
        clash = have_o.get(liv.lower())
        out["o"] = (w, d["hal"], liv, clash)
    if not r["s"]:
        d = laws.derive_s(stem, small=small, affix=affix)
        liv = d["living"]
        clash = have_s.get(liv.lower())
        bl = liv.lower() in BL
        out["s"] = (stem, d["eldest"], liv, clash, bl)
    return out

if __name__ == "__main__":
    roots, have_o, have_s = attested_sets()
    for r in roots:
        p = predict(r, have_o, have_s)
        if p:
            o = p.get("o"); s = p.get("s")
            print(r["key"].ljust(8), r["root"].ljust(14),
                  ("O*" + o[2] + (" CLASH " + ",".join(o[3]) if o[3] else "")) if o else "",
                  ("S*" + s[2] + (" CLASH " + ",".join(s[3]) if s[3] else "") + (" BLACKLIST" if s[4] else "")) if s else "")
