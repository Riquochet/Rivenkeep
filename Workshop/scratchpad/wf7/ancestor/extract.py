"""Extract the attested lexicons of Orrowen (shoreland_spec.md) and Seilrhass
(lexicon.tsv) into JSON, so the ancestor's sound laws can be checked against them."""
import re, json, sys
WF6 = "/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf6"
spec = open(WF6 + "/shoreland_spec.md", encoding="utf-8").read()

rows = []
sec = re.search(r"^## 5 · LEXICON(.*?)^## 6 ", spec, re.S | re.M).group(1)
sub = ""
for line in sec.splitlines():
    m = re.match(r"^### (5\.\d+) (.*)", line)
    if m:
        sub = m.group(1); continue
    if not sub or not line.startswith("|") or line.startswith("|---"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if cells[0] in ("Orrowen", "Affix", "", "Column") or cells[0].startswith("**Value"):
        continue
    rows.append({"sub": sub, "cells": cells})

out = []
def strip(s): return re.sub(r"[*]", "", s).strip()
for r in rows:
    c, sub = r["cells"], r["sub"]
    if sub == "5.11":
        # numbers table: pairs of (n, word)
        for i in range(0, len(c) - 1, 2):
            n, w = strip(c[i]), c[i + 1]
            for b in re.findall(r"\*\*\*?([^*]+?)\*\*\*?", w):
                out.append({"form": b.strip(), "sub": sub, "sense": "number " + n, "hal": "", "cls": "", "note": strip(w)})
        continue
    if sub == "5.12":
        out.append({"form": strip(c[0]), "sub": sub, "sense": strip(c[1]), "hal": "", "cls": "", "note": strip(c[2]) if len(c) > 2 else ""})
        continue
    if sub == "5.10":
        out.append({"form": strip(c[0]), "sub": sub, "sense": strip(c[2]) if len(c) > 2 else "", "hal": "", "cls": "", "note": "mut: " + strip(c[1])})
        continue
    if sub in ("5.8", "5.9"):
        out.append({"form": strip(c[0]), "sub": sub, "cls": strip(c[1]), "sense": strip(c[2]), "hal": "", "note": strip(c[3]) if len(c) > 3 else ""})
        continue
    out.append({"form": strip(c[0]), "sub": sub, "hal": strip(c[1]), "cls": strip(c[2]), "sense": strip(c[3]), "note": strip(c[4]) if len(c) > 4 else ""})

# names 4.5
sec = re.search(r"^### 4\.5 The Shoreland names(.*?)^### 4\.6", spec, re.S | re.M).group(1)
for line in sec.splitlines():
    if line.startswith("| **"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        out.append({"form": strip(c[0]), "sub": "4.5", "hal": strip(c[1]), "cls": "", "sense": strip(c[2]), "note": strip(c[3])})
# 4.6 translations + havens
sec = re.search(r"^### 4\.6 (.*?)^## 5 ", spec, re.S | re.M).group(1)
for line in sec.splitlines():
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    if len(c) >= 3 and c[1].startswith("*") and not line.startswith("|---"):
        out.append({"form": strip(c[1]), "sub": "4.6", "hal": "", "cls": "", "sense": strip(c[0]) + " :: " + strip(c[2]), "note": strip(c[3]) if len(c) > 3 else ""})
json.dump(out, open("o_lex_raw.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "O rows")

s = []
for line in open(WF6 + "/lang/lexicon.tsv", encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    f = line.rstrip("\n").split("\t")
    s.append({"form": f[0], "kind": f[1], "sense": f[2], "note": f[3] if len(f) > 3 else ""})
json.dump(s, open("s_lex_raw.json", "w"), ensure_ascii=False, indent=1)
print(len(s), "S rows")
