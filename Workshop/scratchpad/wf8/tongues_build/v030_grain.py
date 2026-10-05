"""The grain's v3 page cut for Rivenkeep_Tongues.html v0.3.0 (scratch only; never goes into Docs/).

The drawings are the v3 renderer's own output: wf8/render_grain3.py was re-run on wf8/grain3/texts/IV-6.gn2 and
IV-4.gn2 into g3render/ (byte-identical to wf8/grain3/svg/grain3_IV-*.svg, the sheet's sources). The v2 IV.6 is
the round v0.2 printed at the head of §9 (identical to wf7's render_grain2.py output).

On the page:
  * the §9 hero becomes the v3 IV.6 (its ids unchanged);
  * §9.18 prints the v2 IV.6 beside it (ids prefixed 'v2'; its 143 sign symbols, byte-identical to the hero's,
    are not repeated: its <use>s point at the hero's), the v3 IV.4 whole, and reading-scale crops drawn as
    <svg viewBox=crop><use href="#<round>-all"/></svg> (the crops of the sheet, grain_v2_v3.png);
  * the renderer notes v3, and the decode check.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mdlib import inline, post, fixall  # noqa: E402

WF8 = os.path.dirname(HERE)
V3_IV6 = open(HERE + '/g3render/IV-6.svg', encoding='utf-8').read().strip()
V3_IV4 = open(HERE + '/g3render/IV-4.svg', encoding='utf-8').read().strip()
assert V3_IV6 == open(WF8 + '/grain3/svg/grain3_IV-6.svg', encoding='utf-8').read().strip()
assert V3_IV4 == open(WF8 + '/grain3/svg/grain3_IV-4.svg', encoding='utf-8').read().strip()
NOTES = open(WF8 + '/grain_render_v3.md', encoding='utf-8').read()
DECODE = open(WF8 + '/grain3/sheet/decode_table.html', encoding='utf-8').read()


def with_group_id(svg, gid):
    assert svg.count('<g fill="currentColor">') == 1
    return svg.replace('<g fill="currentColor">', '<g id="%s" fill="currentColor">' % gid, 1)


def hero_v3():
    return with_group_id(V3_IV6, 'g65e9475-all')


def v2_deduped(v2):
    """The v2 IV.6, its ids prefixed 'v2', its sign symbols dropped (the hero's identical ones are used)."""
    syms = dict(re.findall(r'<symbol id="([^"]+)"(.*?</symbol>)', v2, re.S))
    hero_syms = dict(re.findall(r'<symbol id="([^"]+)"(.*?</symbol>)', V3_IV6, re.S))
    assert syms and all(hero_syms.get(k) == v for k, v in syms.items()), 'symbols differ'
    s = re.sub(r'<symbol id="[^"]+".*?</symbol>', '', v2, flags=re.S)
    ids = set(re.findall(r'\bid="([^"]+)"', s))

    def ren(i):
        return ('v2' + i) if i in ids else i
    s = re.sub(r'\bid="([^"]+)"', lambda m: 'id="%s"' % ren(m.group(1)), s)
    s = re.sub(r'href="#([^"]+)"', lambda m: 'href="#%s"' % ren(m.group(1)), s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: 'url(#%s)' % ren(m.group(1)), s)
    s = re.sub(r'aria-labelledby="([^"]+)"', lambda m: 'aria-labelledby="%s"' % ' '.join(ren(x) for x in m.group(1).split()), s)
    s = s.replace('<title id="v2g65e9475-t">The Voyage of the Aelvaren (IV.6), whole.</title>',
                  '<title id="v2g65e9475-t">The Voyage of the Aelvaren (IV.6), whole, as the v2 renderer cut it.</title>')
    assert 'as the v2 renderer cut it' in s
    s = with_group_id(s, 'v2g65e9475-all')
    return s


def use_svg(gid, vb, label, w=None):
    x, y, ww, hh = vb
    return ('<svg xmlns="http://www.w3.org/2000/svg" class="wood-ink" viewBox="%g %g %g %g" width="%d" height="%d" '
            'role="img" aria-label="%s"><use href="#%s"/></svg>'
            % (x, y, ww, hh, w or 360, round((w or 360) * hh / ww), html.escape(label), gid))


# the sheet's crops (sheet_v2_v3.py), in the rounds' own units
CROPS_IV6 = [
    ('IV.6, ring 7: the braid <i>abab!</i> (fire and grey, by turns, until the grey)', (-706, -58, 76, 76),
     'The over-strands read p, q, p, q, and the last crossing splinters; in v3 each strand lies in its dark groove, so the over-strand is lifted.'),
    ('IV.6, ring 5: our turning <i>breaks</i> the current (e1 ⊳ f1)', (-100, 455, 60, 60),
     'A break crosses square, once. In v3 the under-strand’s gap is wider and its ends splinter, so a break and a pass tell apart at page size.'),
    ('IV.6, the heart ring: the root HOLD', (-110, -165, 220, 220),
     'What does not change: the heart stays a plain anchor. No figure, wake, knot-eye or ring-split, and a runner there keeps v2’s knife; only the dark margin round each cut is wider.'),
]
CROPS_IV4 = [
    ('IV.4, rings 9–15, files 12–3: the busy sapwood', (0, -1000, 700, 700),
     'The outer rings at reading size: runners in their grooves, the wake of grain along them, the knot-eyes round the marks, and the flecked figure between the rings.'),
    ('IV.4, ring 9: the bind K1 (i6 and i7 hooked through each other) and its out-runner', (572, -476, 50, 50),
     'Two lock crossings, the eye, and one out-runner.'),
]


def crops_html():
    out = ['<figure class="leaf wood cv crops" id="fig-v3-crops">']
    for t, vb, note in CROPS_IV6:
        lab = re.sub('<[^>]+>', '', t)
        out.append('<div class="ct3">%s</div><div class="rounds pair">'
                   '<div>%s<div class="cap">v2</div></div><div>%s<div class="cap">v3</div></div></div>'
                   '<div class="cn3">%s</div>'
                   % (t, use_svg('v2g65e9475-all', vb, lab + ', v2'), use_svg('g65e9475-all', vb, lab + ', v3'), note))
    out.append('<div class="rounds pair" style="margin-top:14px;align-items:flex-start">')
    for t, vb, note in CROPS_IV4:
        lab = re.sub('<[^>]+>', '', t)
        out.append('<div><div class="ct3">%s</div>%s<div class="cap">v3</div><div class="cn3">%s</div></div>'
                   % (t, use_svg('g0bcfbef-all', vb, lab + ', v3'), note))
    out.append('</div>')
    out.append('<figcaption>The same crops as the before-and-after sheet, at reading scale, each a window on the whole round '
               'above (nothing here is redrawn). The v2 cut of IV.4 is not printed in this doc, for its weight, so its two crops '
               'show v3 alone; the decode check below compared both.</figcaption></figure>')
    return '\n'.join(out)


# ---------------------------------------------------------------- the renderer notes v3, as HTML
def notes_md():
    a = NOTES.index('## Renderer notes v3')
    b = NOTES.index('## The mini decode check')
    t = NOTES[a:b].split('\n', 1)[1].strip().rstrip('-').strip()
    reps = [
        (' (checked by `wf8/grain3/work/equiv.py`)', ', checked by code'),
        ('which keeps the intent of call §19.2(a)', 'which keeps the intent of the recommended call on the runners’ tone \x02'),
        ('(grain_v2 §15)', '(the grain v2 bans)'),
        ('Drawn as continuous lines, the figure read as the rejected vinyl look (grain_v2 §1.2).',
         'Drawn as continuous lines, the figure read as the rejected vinyl look \x03.'),
        (' (grain_v2 §4.6)', ''), ('(grain_v2 §11.5)', '\x04'), (' (§6.1)', ''), (' (grain_v2 §11.6)', ' for a leaf'),
        ('The whole-round `--check` is deterministic', 'The whole-round check is deterministic'),
        ('The §4.6 check (no two lines within 4 units) still passes', 'The spec’s check that no two ring lines come within 4 units still passes'),
    ]
    for x, y in reps:
        assert x in t, x
        t = t.replace(x, y)
    return t


def md_blocks(t):
    """A small markdown-to-HTML for the notes: ### headings, paragraphs, nested - and 1. lists, tables."""
    lines = t.split('\n')
    out = []
    i = 0

    def inl(s):
        s = post(inline(fixall(s) if 'wf' in s else s))
        s = s.replace('\x02', '(<a href="#g2-jack">§9.17</a>, call 2)')
        s = s.replace('\x03', '(<a href="#g2-ask">§9.1</a>)')
        s = s.replace('\x04', '(<a href="#g2-leaf">§9.11</a>)')
        return s

    def parse_list(i, indent):
        items = []
        kind = None
        while i < len(lines):
            l = lines[i]
            if not l.strip():
                # a blank line ends the list unless the next line continues it at this indent or deeper
                j = i + 1
                if j < len(lines) and re.match(r'^\s{%d,}(?:- |\d+\. )' % indent, lines[j]):
                    i = j
                    continue
                break
            m = re.match(r'^(\s*)(- |\d+\. )(.*)$', l)
            if not m:
                break
            ind = len(m.group(1))
            if ind < indent:
                break
            if ind > indent:
                sub, i = parse_list(i, ind)
                if items:
                    items[-1] += sub
                continue
            kind = kind or ('ol' if m.group(2)[0].isdigit() else 'ul')
            items.append(inl(m.group(3)))
            i += 1
        return '<%s>%s</%s>' % (kind, ''.join('<li>%s</li>' % x for x in items), kind), i

    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == '---':
            i += 1
            continue
        if l.startswith('### '):
            out.append('<h5>%s</h5>' % inl(l[4:]))
            i += 1
            continue
        if re.match(r'^\s*(- |\d+\. )', l):
            h, i = parse_list(i, len(re.match(r'^(\s*)', l).group(1)))
            out.append(h)
            continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                if not re.match(r'^\|[\s:|-]+\|$', lines[i]):
                    rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            h = '<tr>' + ''.join('<th>%s</th>' % inl(c) for c in rows[0]) + '</tr>'
            b = ''.join('<tr>' + ''.join('<td>%s</td>' % inl(c) for c in r) + '</tr>' for r in rows[1:])
            out.append('<div class="tw"><table>%s%s</table></div>' % (h, b))
            continue
        para = [l]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(\s*(- |\d+\. )|\||### )', lines[i]):
            para.append(lines[i])
            i += 1
        out.append('<p>%s</p>' % inl(' '.join(x.strip() for x in para)))
    return '\n'.join(out)


def notes_html():
    h = md_blocks(notes_md())
    assert 'wf8' not in h and 'wf7' not in h and '.py' not in h, re.findall(r'.{40}(?:wf8|wf7|\.py).{40}', h)[:3]
    return h


def decode_html():
    t = re.search(r'<table>.*</table>', DECODE, re.S).group(0)
    t = t.replace(' class="ok"', '').replace('<i>', '<em>').replace('</i>', '</em>')
    t = t.replace('(a router watch item, &sect;15)', '(a watch item for the router: the circuit-board look the grain v2 bans)')
    assert '&sect;' not in t
    return '<div class="tw">%s</div>' % t


# ---------------------------------------------------------------- §9.18
def section_html(v2_hero):
    v2 = v2_deduped(v2_hero)
    iv4 = with_group_id(V3_IV4, 'g0bcfbef-all')
    use_v3 = ('<svg xmlns="http://www.w3.org/2000/svg" class="wood-ink" viewBox="-1003 -1043 2022 1966" width="1213" '
              'height="1180" role="img" aria-label="The Voyage of the Aelvaren (IV.6), whole, as the v3 renderer cuts it: '
              'the round at the head of this section."><use href="#g65e9475-all"/></svg>')
    return '''<h3 id="g2-v3">9.18 · The page cut, v3: the same carving, cut to be seen</h3>
<p>Jack’s note 7 asked for the grain to be <em>“more intricate and more intertwined”</em>, with the anchor kept. The v2 rules made the carving so. But at page size, about 700 px wide, a whole leaf still read as <strong>sparse and faint</strong>: small scattered marks and pale lines, not a carving. v2 cut every round with one knife, sized for reading scale. On IV.6, whose radius is about 1,000 units, one unit is about a third of a pixel on the page, so a runner 2.7 units wide became a sub-pixel hairline, and its crossings, gaps of about 3 units, disappeared. The structure was all there. It was drawn too finely to see.</p>
<p><strong>The v3 renderer changes only how a whole round is cut for the page.</strong> The Grain Notation, every rule of the grain v2 spec, the packing, the router and the signs are unchanged. Checked by code on IV.6, IV.4, the gift’s sentence and E4-01, the v2 and v3 drawings have the same marks, the same runner courses, the same crossings (over, under and kind), the same runner ends and the same validator warnings. A whole round is cut at a <strong>page weight</strong>, <em>pw = R / 400</em>, between 1 and 2.8, where R is the radius of its outermost ring. At that weight the runners are heavier and lie in dark grooves, and the gaps where one passes under another are wider. A dark knot-eye surrounds every mark. The ring lines yield further round the marks and are dragged where runners cross, with a wake of grain along every runner. The ring lines split into finer strands where the carving disturbs them, and a flecked figure of grain runs between the rings. All of it follows <strong>the Law of the Rings</strong>: nothing in the heart ring, a little in band I, and the most outward. So the anchor stays plain and the detail is outward, as Jack asked.</p>
<figure class="leaf wood" id="fig-v2v3-iv6"><div class="rounds pair">
<div>{v2}<div class="cap">IV.6 · v2</div></div>
<div>{use_v3}<div class="cap">IV.6 · v3 (pw 2.34)</div></div>
</div>
<figcaption><strong>IV.6, <em>The Voyage of the Aelvaren</em>, whole: v2 and v3.</strong> The same notation, the same packing, routes and crossings. Only the cut changed. The v3 round is the one at the head of this section.</figcaption></figure>
<figure class="leaf wood g2hero" id="fig-iv4-v3">
{iv4}
<figcaption><strong>IV.4, <em>The Gift Held an Hour</em>, carved whole, cut by v3</strong> (pw 2.80). This is the wood pilot’s round (<a href="#t3-iv4">§11.9</a>), printed whole here for the first time: 16 rings, 63 knowings, 110 runners, two breaks, a bind, a blind, eight pockets. The root in the heart is GIFT, plain. The rings of its middle band stay open wood on the lower half, because the telling carves little on those files; v3 adds texture there, not marks.</figcaption></figure>
<h4>At reading scale</h4>
{crops}
<h4>What does not change</h4>
<ul>
<li><strong>Young and small carvings, the ring plates and the chips</strong> render byte-identical to v2. That includes the Hasty seven (E1-01 to E1-07), <em>Burn</em>, VI.1, <em>Naelear</em> and E4-01 (pw 1), the chip, and every ring plate: IV.6’s plates 5, 7 and 9, IV.4’s plates 5 and 12 and the gift’s plate 2. So E1-01 and <em>Burn</em> in <a href="#g2-compare">§9.13</a>, E4-01 in <a href="#x-e4">§10.16</a> and IV.4’s ring 9 in <a href="#t3-iv4">§11.9</a> are already the v3 drawings. The plates are the reading surface (<a href="#g2-leaf">§9.11</a>), and they keep v2’s exact cut.</li>
<li><strong>Rounds of three rings or fewer, and stage-0 rounds, are never page-weighted.</strong> Young carvings stay simple, as the Law of the Rings wants.</li>
<li><strong>Nothing leaves the rim, and nothing is ink that was not.</strong> The wake, the figure and the splits are masked to rings 2 and beyond. The knot-eye is a knock-out, darker wood. There is no spiral, no tendril, no smoke, no closed circle besides the growth rings and no interlace off a crossing, so none of the looks the grain v2 bans comes back.</li>
<li><strong>The runners’ tone.</strong> At page weight, runners are cut in one tone at 88%, and the marks stay the brightest thing in the round at 97%. That keeps the intent of the recommended call on the runners’ tone (<a href="#g2-jack">§9.17</a>, call 2).</li>
<li><strong>The Texts’ drawings</strong> (<a href="#texts">§10</a>) are unchanged in this version. Their young and small rounds are already the v3 drawings, byte for byte; the larger ones, the gift’s sentence among them (pw 1.46), would be cut somewhat heavier by v3.</li>
</ul>
<h4>The decode check</h4>
<p>Both whole rounds were re-rendered by v3 with their titles, descriptions and labels stripped, cut into v2 and v3 crop pairs at reading scale (IV.6 51 crops, IV.4 70) and read by eye against the grain’s reading rules, then compared with the model’s own list of what each crop holds.</p>
{decode}
<p><strong>The weight.</strong> IV.6 whole is 344.7 KB in v3 (306.8 KB in v2), inside the 350 KB budget for a leaf. IV.4 whole is 479.2 KB (429.1 KB in v2, already over). Every sign is still one symbol placed by reference. The new cost is the figure, the stroked runner steps that the wake reuses, the knot-eyes and the year-line slivers. The whole-round check is deterministic: two runs are byte-identical.</p>
<details class="lex" id="g2-v3-notes"><summary>Renderer notes v3 <span class="n">v3.0–v3.12, whole</span></summary><div class="dn">
{notes}
</div></details>
<p><strong>The call is Jack’s:</strong> cut whole rounds for the page by v3, or keep v2’s one knife. The notation, the rules and every reading are the same either way <span class="kv jack">Jack</span>.</p>
'''.format(v2=v2, use_v3=use_v3, iv4=iv4, crops=crops_html(), decode=decode_html(), notes=notes_html())


CSS = '''
/* v0.3.0: the grain's page cut (v3), and the whole Book */
.crops .ct3{font-family:'Source Sans 3',sans-serif;font-size:.78rem;color:var(--page);text-align:left;margin:14px 0 5px}
.crops .ct3:first-child{margin-top:2px}
.crops .cn3{font-family:'Source Sans 3',sans-serif;font-size:.72rem;color:var(--dim);text-align:left;margin:4px 0 2px;line-height:1.5}
.crops svg{background:#0c0f0a;border-radius:2px}
.cv{content-visibility:auto;contain-intrinsic-size:auto 1400px}
details.lex>.dn{padding:2px 16px 12px}
.dn h5{font-family:'Chakra Petch',sans-serif;font-size:.74rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin:16px 0 5px;color:var(--gold)}
.dn p,.dn li{font-size:.84rem}
.dn .tw table td,.dn .tw table th{font-size:.76rem}
'''


if __name__ == '__main__':
    print(len(notes_html()), len(decode_html()), len(crops_html()))
    print(notes_html()[:4000])
