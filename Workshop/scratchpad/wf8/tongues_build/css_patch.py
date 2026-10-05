# -*- coding: utf-8 -*-
"""Update extra.css for v0.2.0 (generic tab mocks; the font, the first marks, the word-signs, the lexicon). Scratch only."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, 'extra.css')
s = open(p, encoding='utf-8').read()

old_tabs = [
    '#tab-book:checked~.bar label[for=tab-book],#tab-plain:checked~.bar label[for=tab-plain],#tab-orig:checked~.bar label[for=tab-orig]{color:var(--gold);border-bottom-color:var(--gold)}',
    '#tab-book:focus-visible~.bar label[for=tab-book],#tab-plain:focus-visible~.bar label[for=tab-plain],#tab-orig:focus-visible~.bar label[for=tab-orig]{outline:2px solid var(--accent);outline-offset:-2px}',
    '#tab-book:checked~.panes .p-book,#tab-plain:checked~.panes .p-plain,#tab-orig:checked~.panes .p-orig{display:block}',
]
new_tabs = [
    '.tabs .t-book:checked~.bar .l-book,.tabs .t-plain:checked~.bar .l-plain,.tabs .t-orig:checked~.bar .l-orig{color:var(--gold);border-bottom-color:var(--gold)}',
    '.tabs .t-book:focus-visible~.bar .l-book,.tabs .t-plain:focus-visible~.bar .l-plain,.tabs .t-orig:focus-visible~.bar .l-orig{outline:2px solid var(--accent);outline-offset:-2px}',
    '.tabs .t-book:checked~.panes .p-book,.tabs .t-plain:checked~.panes .p-plain,.tabs .t-orig:checked~.panes .p-orig{display:block}',
]
for a, b in zip(old_tabs, new_tabs):
    if a in s:
        s = s.replace(a, b)
    else:
        assert b in s, a

ADD = r'''
/* ---- v0.2.0 ---- */
/* the leaf-hand, set in the Garl Flenn font (embedded above) */
.gf{font-family:'Garl Flenn';font-style:normal;font-weight:400;line-height:1.5;color:var(--stone-ink);letter-spacing:0;text-transform:none;font-size:inherit}
.gf.i2{color:#e3b9a4}
.inkline{font-size:1.7rem;line-height:1.55;margin:6px 0 4px;overflow-wrap:anywhere;text-align:left}
.inkline.big{font-size:2.1rem;text-align:center}
figure.leaf .inkline,.inkline.leaf{text-align:center}
#fig-facing .inkline{font-size:1.55rem;margin-top:14px}
.gtext{background:var(--stone-bg);border:1px solid rgba(236,229,207,.13);border-radius:4px;padding:12px 14px 10px;margin:10px 0}
.gtext .gt-h{font-family:'Chakra Petch',sans-serif;font-size:.74rem;letter-spacing:1px;text-transform:uppercase;color:var(--gold)}
.gtext .gt-h .dim{text-transform:none;letter-spacing:0;font-family:'Source Sans 3',sans-serif}
.gtext .gt-r{font-size:.92rem;margin:2px 0}
.gtext .gt-c{font-family:'IBM Plex Mono',monospace;font-size:.62rem;color:var(--dim);margin:0}
.gfam{font-size:.78rem;color:var(--dim);margin:12px 0 6px}
.ggrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(64px,1fr));gap:8px}
.gcell{background:var(--stone-bg);border:1px solid rgba(236,229,207,.13);border-radius:4px;text-align:center;padding:4px 2px 5px;display:flex;flex-direction:column;align-items:center}
.gcell .gf{font-size:2.3rem;line-height:1.3}
.gcell small{font-family:'IBM Plex Mono',monospace;font-size:.62rem;color:var(--dim)}
table.gforms td{text-align:center;background:var(--stone-bg)}
table.gforms td .gf{font-size:2rem}
td .gf{font-size:1.5rem}
.gsizes .row{display:grid;grid-template-columns:44px 1fr;gap:10px;align-items:baseline;padding:6px 0;border-bottom:1px solid var(--border)}
.gsizes small{font-family:'IBM Plex Mono',monospace;font-size:.62rem;color:var(--dim)}
/* the first marks and their descent */
svg.fm{display:block;width:100%;height:auto;max-width:900px;margin:0 auto;color:var(--stone-ink)}
svg.fm .m polyline,svg.fm .m polygon{fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
svg.fm .m .solid{fill:currentColor;stroke:currentColor}
svg.fm text{fill:currentColor}
svg.fm .sub{fill:var(--dim)}
table.descent{width:auto;margin:0 auto}
table.descent td,table.descent th{border:0;border-bottom:1px solid rgba(236,229,207,.1);vertical-align:middle;text-align:left;background:transparent}
table.descent th{color:var(--dim)}
table.descent .m polyline,table.descent .m polygon{fill:none;stroke:var(--page);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
table.descent .m .solid{fill:var(--page)}
table.descent .nm{font-size:.74rem;color:var(--page)}
table.descent .wd{font-size:.7rem;font-style:italic;color:var(--dim)}
table.descent .cap{font-size:.7rem;color:var(--dim);max-width:220px}
table.descent td.st{color:var(--stone-ink)}
table.descent td.gr{color:var(--wood-ink)}
table.descent .arrow{color:var(--dim);font-size:1.1rem}
table.descent svg{display:block}
/* the word-signs, as centre-lines */
svg.wsg{width:34px;height:42px;display:block;color:var(--stone-ink)}
svg.wsg.big{width:44px;height:55px;display:inline-block;vertical-align:middle}
svg.wsg path{fill:none;stroke:currentColor;stroke-width:.34;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:3}
svg.wsg path.ft{stroke-width:.2;stroke-opacity:.38;stroke-linecap:butt}
table.wsinv td{vertical-align:middle}
table.wsinv td:nth-child(2){background:var(--stone-bg);width:44px}
.wsinline{display:inline-block;background:var(--stone-bg);border-radius:3px;padding:2px 6px;vertical-align:middle}
/* the lexicon, whole */
table.olex td{font-size:.74rem;padding:4px 7px}
table.olex td:first-child{white-space:nowrap}
table.olex td:nth-child(6){font-family:'IBM Plex Mono',monospace;font-size:.62rem;color:var(--dim)}
table.olex td:nth-child(5){color:var(--dim)}
table.olex td:last-child{font-family:'IBM Plex Mono',monospace;font-size:.62rem;color:var(--dim);text-align:center}
table.olex tr.cn td:first-child b,.cnkey{color:var(--gold)}
/* call-outs, figures, facing page */
.s.callout{border-left-color:var(--warn);background:linear-gradient(90deg,rgba(255,167,38,.06),var(--surface) 40%)}
.s.callout .ct{color:var(--warn)}
.s.callout ol li{font-size:.86rem}
figure.leaf.g2hero{padding:10px 6px 12px}
figure.leaf.g2hero>svg{width:100%;max-width:920px}
div.leaf.stone.mini{background:var(--stone-bg);border:1px solid rgba(236,229,207,.13);border-radius:4px;padding:10px 8px;text-align:center;margin:2px 0 6px}
div.leaf.stone.mini svg{max-width:100%;height:auto}
.rows p.gloss,p.gloss{font-family:var(--face-stone);color:var(--page-dim);font-size:1rem}
.tabs .hand.stonehand{background:var(--stone-bg)}
.facing{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:start}
.facing .fl{background:var(--stone-bg);border-radius:4px;padding:8px 10px}
.facing .inkline{font-size:1.35rem}
@media(max-width:640px){
 .facing{grid-template-columns:1fr}
 .inkline{font-size:1.35rem}
 .inkline.big{font-size:1.6rem}
 #fig-facing .inkline{font-size:1.2rem}
 .ggrid{grid-template-columns:repeat(auto-fill,minmax(54px,1fr))}
}
'''
if '/* ---- v0.2.0 ---- */' not in s:
    s = s + ADD
open(p, 'w', encoding='utf-8').write(s)
print('css ok', len(s))
