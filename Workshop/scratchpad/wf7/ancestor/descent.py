"""The descent of the marks: first mark -> course-hand letter (stone) -> grain sign (wood).
Uses wf6's two renderers read-only, so the letters and signs are drawn exactly as the Book draws them."""
import sys, math
WF6 = "/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf6"
sys.path.insert(0, WF6)
sys.argv = ["x"]
import render_shore as RS
import render_grain as RG
from first_marks import MARKS, svg_mark

ROWS = [
 # (mark, course-hand tokens or None, stone caption, grain sign or ('cond', X), wood caption)
 ("FORE", "{r}", "r: the Fore's right arm and foot; the Fore itself stays whole as the foremark", "BARB", "the Bar Before: kept whole"),
 ("SQUARE", "{rh}", "rh: the Square stood on its bed and opened", "SQUARE", "the Mute Square"),
 ("COURSE", "{t}", "t: the Course is the offset upright", ("cond", "WATER"), "the WATER band: the running line laid along the ring"),
 ("BEARER", "{p}", "p: a prop under its load", "BEARER", "a laden hull: the load grown round the bearer"),
 ("SPLIT", "{k}", "k: the stem and back tine are the shore; the other tine is laid flat", "BREAK", "BREAK: the head opens into a split"),
 ("CURL", "{o}", "o (and a): the curl laid over a short pin", "WAVE", "the Wave"),
 ("LONE", "{i}", "i (and e): a tall pin and a low stone", "LONE", "the Lone Stroke"),
 ("UPON", "{u}", "u: two pins and a raised keystone", "BENEATH", "BENEATH: the same picture read from below"),
 ("WITHIN", "{m}", "m: the Breath Within gives the middle stone", ("cond", "MIST"), "the MIST band: through the middle of the ring"),
 ("SAIL", "{w}", "w: the Sail gives a short top stone and a free low one", "SAIL", "SAIL"),
 ("BOUGH", "{s}", "s: the lens cut straight into two stones", "HULL", "HULL: a bough, a hull"),
 ("DOOR", "{s.t.o.n | #gate}", "the gate mark, after Ston: kept whole", "DOOR", "DOOR: kept whole, its posts battered"),
 ("CUP", None, "lost: the stone kept the word tum, remember", "HOLD", "HOLD: the cup"),
 ("STEM", "tolm", "every upright; a letter is a tolm", "TREE", "TREE (thael): the same word, *tolm-"),
]

_n = [0]
def stone_svg(tokens):
    _n[0] += 1
    svg, _t, _d = RS.render(text=tokens, title="", px_per_u=7.0, pfx="dsc%d" % _n[0])
    return svg

def grain_svg(sign, key):
    cell = 176
    if isinstance(sign, tuple):
        defs, body = RG.chip_svg(None, 0, 0, cell, "desc/" + key, cond=sign[1])
    else:
        defs, body = RG.chip_svg(sign, 0, 0, cell, "desc/" + key)
    x0, y0, x1, y1 = RG.CHIP_BOX[0]
    x0, y0, x1, y1 = math.floor(x0 - 4), math.floor(y0 - 4), math.ceil(x1 + 4), math.ceil(y1 + 4)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" width="%d" height="%d">' % (x0, y0, x1 - x0, y1 - y0, round((x1 - x0) * 0.5), round((y1 - y0) * 0.5))
            + '<defs>' + ''.join(defs) + '</defs><g fill="currentColor">' + ''.join(body) + '</g></svg>')

def mark_svg(key):
    m = MARKS[key]
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 70" width="70" height="70"><g class="m">%s</g></svg>'
            % svg_mark(m, 3, 3, 64))

def page():
    rows = []
    for key, tok, sc, sign, wc in ROWS:
        m = MARKS[key]
        stone = stone_svg(tok) if tok else '<div class="none">—</div>'
        rows.append('<tr><td class="mk">%s<div class="nm">%s</div><div class="wd">*%s</div></td>'
                    '<td class="arrow">→</td><td class="st">%s<div class="cap">%s</div></td>'
                    '<td class="arrow">→</td><td class="gr">%s<div class="cap">%s</div></td></tr>'
                    % (mark_svg(key), m["name"], m["word"], stone, sc, grain_svg(sign, key), wc))
    return """<!doctype html><html><head><meta charset="utf-8"><title>The descent of the marks</title><style>
:root{--ink:#2d2618;--paper:#f3ecdc;--sub:#6b5d45;--stone:#3d3326;--wood:#344a2c}
@media (prefers-color-scheme: dark){:root{--ink:#eadfc6;--paper:#1c1812;--sub:#a8987a;--stone:#e4dbc2;--wood:#c9dcb4}}
body{background:var(--paper);color:var(--ink);font-family:Georgia,serif;margin:24px}
h1{font-weight:normal;font-size:22px;margin:0 0 4px} p.sub{color:var(--sub);font-style:italic;margin:0 0 16px;font-size:14px}
table{border-collapse:collapse} td{vertical-align:middle;padding:6px 10px;border-bottom:1px solid rgba(128,110,80,.25)}
th{font-weight:normal;text-align:left;color:var(--sub);font-size:13px;letter-spacing:1.5px;text-transform:uppercase;padding:4px 10px}
.m polyline,.m polygon{fill:none;stroke:var(--ink);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}.m .solid{fill:var(--ink)}
.nm{font-size:13px}.wd{font-size:12px;font-style:italic;color:var(--sub)}.cap{font-size:12px;color:var(--sub);max-width:250px}
.st{color:var(--stone)} .gr{color:var(--wood)} .arrow{color:var(--sub);font-size:20px} .none{font-size:30px;color:var(--sub);padding:14px}
.stone-ink{color:var(--stone)}
</style></head><body><h1>The descent of the marks</h1><p class="sub">first mark &nbsp;→&nbsp; stone: the course-hand (chisel wear, the first sound, the reform) &nbsp;→&nbsp; wood: the grain (the file, the knife, the meaning). Letters and signs drawn by the Book's own renderers.</p>
<table><tr><th>the first mark</th><th></th><th>on stone</th><th></th><th>in wood</th></tr>%s</table></body></html>""" % "".join(rows)

if __name__ == "__main__":
    open("descent.html", "w").write(page())
    print("descent.html written")
