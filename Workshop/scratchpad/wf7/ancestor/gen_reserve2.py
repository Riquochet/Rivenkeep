"""Reserve roots, second method: enumerate every monosyllabic root the first tongue
allows, derive both reflexes, score how native each looks, and give each meaning the
best unused candidate of its texture.  Deterministic.

Screens (a candidate is dropped if any fails):
  * its Orrowen reflex is new: no attested word, no other reserve root;
  * its Seilrhass reflex is not an attested word, and is shared by at most one other
    reserve root, of a different field (Seilrhass has seven consonants; it must have
    homophones);
  * neither reflex is in the Tolkien/franchise blacklist, the spec's rejected forms,
    or a list of about 1,600 common English words;
  * both reflexes are legal (the spec's phonotactics).
"""
import re, json, sys, itertools
import laws, predict
from gen_reserve import MEANINGS, COMMON, BL, AVOID, legal_o, legal_s

DICT = set(w.strip().lower() for w in open("/usr/share/dict/words"))
SHORT_DICT = set(w for w in DICT if len(w) <= 3)
ANY_DICT = DICT  # a reserve form that is any English dictionary word is not used
import random

ONSETS = {
 "hard": ["k", "t", "g", "d", "kr", "tr", "gr", "dr", "sk", "st", "br", "p", "x", "sp", "kl", "gl", "b"],
 "soft": ["l", "m", "n", "s", "w", "f", "h", "th", "dh", "sw", "xw", "fl"[:1], "", "r"],
 "plain": ["b", "p", "d", "t", "k", "g", "m", "n", "l", "r", "s", "f", "w", "h", "th", "dh", "x", "pr", "pl", "kl", "bl", "xr", "sp", "st", "br", "gw", ""],
}
NUCLEI = {
 "hard": ["a", "o", "u", "e", "i", "aʔ", "oʔ", "ai", "eu", "au"],
 "soft": ["e", "i", "a", "o", "u", "ei", "ai", "eʔ", "iʔ", "aʔ", "ui", "au"],
 "plain": ["a", "e", "i", "o", "u", "ai", "ei", "eu", "au", "aʔ", "eʔ", "oʔ", "uʔ", "iʔ"],
}
CODAS = {
 "hard": ["k", "t", "d", "g", "sk", "st", "rk", "rt", "nd", "rd", "ld", "th", "ss", "rn", "nt", "lt", "r", "n", "l"],
 "soft": ["l", "n", "m", "r", "s", "th", "dh", "ll", "nn", "mm", "rr", "lm", "rn", "lf", "rw", "ŋ", "nth", "lth", "sth", "lw"],
 "plain": ["k", "t", "d", "sk", "st", "rk", "rt", "nd", "rd", "ld", "th", "l", "n", "m", "r", "s", "dh", "ll", "nn", "mm", "rr", "lm", "rn", "nth", "ss"],
}

def score(root, lo, ls, tex):
    s = 0.0
    s -= abs(len(lo) - 4) * 0.6 + abs(len(ls) - 4) * 0.6
    if lo in DICT: s -= 2.0
    if ls in DICT: s -= 1.5
    if ls.count("rh") > 1 or lo.count("rh") > 1: s -= 2
    if ls.endswith(("ea", "ae")): s -= 1.2          # reads as a suffix -ea or a verb in -e
    if re.search(r"(ae|ea|ei)", ls): s += 0.3        # the diphthongs are the tongue's colour
    if re.search(r"(nth|ss|nn|th)$", ls): s += 0.15
    if re.search(r"(ll|nn|mm|rr|ss|sk|st|rn|rd|ld|lt|rt|nd|nt|rm|lm|lv|rv|nth|rth)$", lo): s += 0.4
    if lo.startswith(("hw", "rhy", "y")): s -= 1
    if "ʔ" in root: s += 0.05                        # the catch is the first tongue's own colour
    return s

def pool():
    roots, have_o, have_s = predict.attested_sets()
    cand = {}
    for tex in ("hard", "soft", "plain"):
        for on, nu, co in itertools.product(ONSETS[tex], NUCLEI[tex], CODAS[tex]):
            root = on + nu + co
            if root in cand or root.replace("ʔ", "") in AVOID or root.replace("ʔ", "") in COMMON:
                continue
            if re.search(r"[aeiou]ʔ[aeiou]", root):
                continue
            for cls in ("o", "i"):
                stem = root + "-" + cls
                d_o = laws.derive_o(stem + "s"); d_s = laws.derive_s(stem)
                lo, ls = d_o["living"].lower(), d_s["living"].lower()
                if lo in have_o or ls in have_s or lo in BL or ls in BL or lo in AVOID or ls in AVOID:
                    continue
                if lo in COMMON or ls in COMMON or lo in ANY_DICT or ls in ANY_DICT:
                    continue
                if not legal_o(lo) or not legal_s(ls) or len(lo) < 3 or len(ls) < 3:
                    continue
                cand.setdefault(root, {})[cls] = dict(root=root, stem=stem, o=d_o["living"], hal=d_o["hal"],
                                                      s=d_s["living"], eldest=d_s["eldest"], tex=tex,
                                                      score=score(root, lo, ls, tex))
    return cand, have_o, have_s

def small_pool(have_o, have_s):
    out = {}
    for on, nu in itertools.product(["", "h", "t", "s", "m", "n", "l", "r", "th", "w", "f", "k", "p", "d", "x", "st"],
                                    ["a", "e", "i", "o", "u", "ai", "ei", "au", "aʔ", "eʔ", "oʔ"]):
        for co in ["", "n", "s", "th", "r", "l", "m", "t", "k", "st", "nth"]:
            root = on + nu + co
            if len(root) < 2:
                continue
            d_o = laws.derive_o(root, small=True); d_s = laws.derive_s(root, small=True)
            lo, ls = d_o["living"].lower(), d_s["living"].lower()
            if lo in have_o or ls in have_s or lo in COMMON or ls in COMMON or lo in BL or ls in BL:
                continue
            if lo in ANY_DICT or ls in ANY_DICT or len(ls) < 2 or len(lo) < 2:
                continue
            if not lo or not ls or not legal_s(ls) or not legal_o(lo):
                continue
            out[root] = dict(root=root, stem=root, o=d_o["living"], hal=d_o["hal"], s=d_s["living"], eldest=d_s["eldest"],
                             tex="plain", score=-abs(len(lo) - 3) - abs(len(ls) - 3))
    return out

S_END_OK = re.compile(r"(al|an|ath|ass|ann|anth|el|er|enn|ess|enth|eir|ein|eis|ael|aen)$")
O_END_OK = re.compile(r"(al|er|or|ul|il|un|ess|enn|arr|ir|ar|us|ur|is|in|um|ur|ull|orn|arn)$")

def di_pool(have_o, have_s):
    out = []
    ons = ["b", "p", "d", "t", "k", "g", "m", "n", "l", "r", "s", "f", "w", "h", "th", "dh", "x", "st", "sk", "tr", "kr", "gr", "br", "pr", "", "sw"]
    v1s = ["a", "e", "i", "o", "u", "ai", "ei", "eu"]
    mids = ["l", "r", "n", "m", "th", "s", "f", "d", "k", "g", "w", "nn", "ll", "rr", "ss", "st", "sk", "nd", "rd", "lt", "rn"]
    v2s = ["a", "e", "o", "u", "i", "aʔ", "ei"]
    ends = ["l", "r", "n", "nn", "ss", "th", "nth", "s", "m", "ll", "rn"]
    for on, v1, mid, v2, en in itertools.product(ons, v1s, mids, v2s, ends):
        root = on + v1 + mid + v2 + en
        for cls in ("o", "i"):
            stem = root + "-" + cls
            d_o = laws.derive_o(stem + "s"); d_s = laws.derive_s(stem)
            lo, ls = d_o["living"].lower(), d_s["living"].lower()
            if lo in have_o or ls in have_s or lo in COMMON or ls in COMMON or lo in BL or ls in BL:
                continue
            if lo in ANY_DICT or ls in ANY_DICT:
                continue
            if not S_END_OK.search(ls) or not O_END_OK.search(lo):
                continue
            if not legal_o(lo) or not legal_s(ls) or len(lo) > 7 or len(ls) > 7:
                continue
            if re.search(r"(rh[aei]+rh|th[aei]+th|v[aei]+v|n[aei]+n|l[aei]+l|r[aei]+r|s[aei]+s)", ls):
                continue
            if re.search(r"(aea|eae|eie|aee)", ls) or re.search(r"(.)\1\1", lo):
                continue
            sc = -abs(len(lo) - 5) - abs(len(ls) - 5) - (1.5 if lo in DICT else 0) - (1 if ls in DICT else 0)
            out.append(dict(root=root, stem=stem, o=d_o["living"], hal=d_o["hal"], s=d_s["living"],
                            eldest=d_s["eldest"], tex="plain", score=sc, cls=cls))
    return out

DROP_SMALL = {"now", "later", "never", "again", "here", "there", "where", "why", "only", "also", "thus", "because",
              "without", "among", "after", "before", "perhaps", "very2", "almost", "none"}
# basic words first (they get the short roots); rarer, specialised words last (they get two syllables)
PRIORITY_FIRST = """son daughter husband wife brother sister kin friend stranger foe boy girl youth newborn
head face hair ear nose tongue tooth lip skin bone shoulder knee foot finger belly breast tear sleep wake dream eat drink
sit liedown climb haul pull push lift lower throw catch tie dig bury cover hide find lose bring save spare cut hew pour fill
wash swim sail row drown begin return watch touch feel say shout whisper bowdown lead follow sow reap tend fell rise play dance
high low wide narrow near far thick soft hard strong weak slow quick hot cold red sweet bitter rich poor brave clean quiet loud
wild strange sure sharp blunt light broken half few much evil proud fair
sun moon star cloud shadow dawn dusk morning spring summer autumn month week season moss grass flower fruit stump shoot thorn
cave crag cliff valley pebble surf wave foam current shallows bank bay mere pool well mud salt smoke dust ember flame spark hail
lightning bird fish beast feather boulder land freeze warm dry wet bright dim pale rope chest lid key lamp torch oil cup bread
ale bed table seat bench pipe pack cart wheel oar keel rib plank mast seam staff pike banner coin net boat raft bridge stair step
floor roof beam pillar arch hall room window grave holy town fear hope shame joy laugh mercy forgive bless wish choose learn
think believe doubt hate courage wise kind glad sad soul heaven mind seek lie plan order obey victory defeat flee chase""".split()

def gen():
    global MEANINGS
    first = {k: i for i, k in enumerate(PRIORITY_FIRST)}
    ms = [m for m in MEANINGS if m[0] not in DROP_SMALL]
    ms.sort(key=lambda m: (0, first[m[0]]) if m[0] in first else (1, 0))
    MEANINGS_ORDER = ms
    cand, have_o, have_s = pool()
    smalls = small_pool(have_o, have_s)
    dis = di_pool(have_o, have_s)
    dis.sort(key=lambda c: (-c["score"], c["root"], c["cls"]))
    used_root, used_o, used_s = set(), set(), set()
    # the would-be reflexes of the inherited roots are taken too
    roots_all, ho_, hs_ = predict.attested_sets()
    for r_ in roots_all:
        p_ = predict.predict(r_, ho_, hs_)
        if "o" in p_: used_o.add(p_["o"][2].lower())
        pass  # the would-be Seilrhass forms stay free: they are only hypothetical
    out, failed = [], []
    # pass 1: monosyllables with a Seilrhass form of their own (the small words first)
    pending = []
    rhyme_count, onset_count = {}, {}
    ordered = MEANINGS_ORDER
    for key, mean, field, tex, cls in ordered:
        if cls == "":
            opts = sorted(smalls.values(), key=lambda c: (-c["score"], c["root"]))
        else:
            want = "o" if cls in ("o", "aʔ") else "i"
            opts = [v[want] for v in cand.values() if want in v and v[want]["tex"] == tex]
            opts.sort(key=lambda c: (-c["score"], c["root"]))
        pick = None
        for c in opts:
            lo, ls = c["o"].lower(), c["s"].lower()
            if c["root"] in used_root or lo in used_o or ls in used_s:
                continue
            rhyme = re.sub(r"^[^aeiou]*", "", c["root"])
            onset = re.match(r"[^aeiou]*", c["root"]).group(0)
            if rhyme_count.get(rhyme, 0) >= 3 or onset_count.get(onset, 0) >= 14:
                continue
            pick = c; break
        if not pick:
            pending.append((key, mean, field, tex, cls)); continue
        rh_ = re.sub(r"^[^aeiou]*", "", pick["root"]); on_ = re.match(r"[^aeiou]*", pick["root"]).group(0)
        rhyme_count[rh_] = rhyme_count.get(rh_, 0) + 1; onset_count[on_] = onset_count.get(on_, 0) + 1
        used_root.add(pick["root"]); used_o.add(pick["o"].lower()); used_s.add(pick["s"].lower())
        if cls == "aʔ":
            stem = pick["root"] + "-aʔ"
            d_o = laws.derive_o(stem); d_s = laws.derive_s(stem)
            pick = dict(pick, stem=stem, o=d_o["living"], hal=d_o["hal"], s=d_s["living"], eldest=d_s["eldest"])
        out.append(dict(key=key, root=pick["root"] + ("-" if cls else ""), mean=mean, field=field, stem=pick["stem"],
                        o_pred=pick["o"], hal=pick["hal"], s_pred=pick["s"], eldest=pick["eldest"], syll=1))
    # pass 2: two-syllable roots for the rest, drawn in a seeded order so the list is not alphabetical,
    # with no onset and no ending used too often
    rnd = random.Random(7)
    good = [c for c in dis if c["score"] >= -3 and c["root"][0] not in "aeiou"]
    rnd.shuffle(good)
    on_count, end_count = {}, {}
    for key, mean, field, tex, cls in pending:
        pick = None
        for c in good:
            onset = re.match(r"[^aeiou]*", c["root"]).group(0)
            ending = c["s"][-3:]
            if on_count.get(onset, 0) >= 7 or end_count.get(ending, 0) >= 10:
                continue
            lo, ls = c["o"].lower(), c["s"].lower()
            if c["root"] in used_root or lo in used_o or ls in used_s:
                continue
            if cls in ("o", "i") and c["cls"] != cls:
                continue
            pick = c; break
        if not pick:
            failed.append(key); continue
        onset = re.match(r"[^aeiou]*", pick["root"]).group(0)
        on_count[onset] = on_count.get(onset, 0) + 1
        end_count[pick["s"][-3:]] = end_count.get(pick["s"][-3:], 0) + 1
        used_root.add(pick["root"]); used_o.add(pick["o"].lower()); used_s.add(pick["s"].lower())
        out.append(dict(key=key, root=pick["root"] + "-", mean=mean, field=field, stem=pick["stem"],
                        o_pred=pick["o"], hal=pick["hal"], s_pred=pick["s"], eldest=pick["eldest"], syll=2))
    # pass 3: a Seilrhass form may be shared by two roots of different fields (a tongue of seven
    # consonants must have homophones); the Orrowen form stays unique
    s_field = {}
    for r in out:
        s_field.setdefault(r["s_pred"].lower(), []).append(r["field"])
    still = []
    fieldof = {m[0]: m[2] for m in MEANINGS}
    for key in failed:
        m = [x for x in MEANINGS if x[0] == key][0]
        k_, mean, field, tex, cls = m
        pick = None
        for c in good:
            lo, ls = c["o"].lower(), c["s"].lower()
            if c["root"] in used_root or lo in used_o:
                continue
            fs = s_field.get(ls, [])
            if len(fs) >= 2 or field in fs:
                continue
            if cls in ("o", "i") and c["cls"] != cls:
                continue
            pick = c; break
        if not pick:
            still.append(key); continue
        used_root.add(pick["root"]); used_o.add(pick["o"].lower()); s_field.setdefault(pick["s"].lower(), []).append(field)
        out.append(dict(key=key, root=pick["root"] + "-", mean=mean, field=field, stem=pick["stem"],
                        o_pred=pick["o"], hal=pick["hal"], s_pred=pick["s"], eldest=pick["eldest"], syll=2))
    by_s = {}
    for r in out:
        by_s.setdefault(r["s_pred"].lower(), []).append(r["key"])
    for r in out:
        r["s_shared"] = [k for k in by_s[r["s_pred"].lower()] if k != r["key"]]
    for k in still:
        print("FAILED", k, file=sys.stderr)
    order = {m[0]: i for i, m in enumerate(MEANINGS)}
    out.sort(key=lambda r: order[r["key"]])
    return out

if __name__ == "__main__":
    out = gen()
    json.dump(out, open("reserve.json", "w"), ensure_ascii=False, indent=0)
    print(len(out), "reserve roots;", sum(1 for r in out if r["syll"] == 2), "of two syllables")
    for r in out:
        print(r["key"].ljust(12), ("*" + r["root"]).ljust(11), r["o_pred"].ljust(9), r["s_pred"].ljust(9), r["mean"],
              ("[S also " + ",".join(r["s_shared"]) + "]") if r.get("s_shared") else "")
