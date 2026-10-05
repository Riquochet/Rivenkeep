"""shoot3.py - headless Chrome shots of grain SVGs on the dark page (wf8 scratch helper).

    python3 shoot3.py one OUT.png SVG WIDTH            # one svg, scaled to WIDTH px wide
    python3 shoot3.py crop OUT.png SVG x y w h [px]    # a zoom into its viewBox
    python3 shoot3.py grid OUT.png WIDTH COLS a.svg b.svg ...
"""
import os, re, subprocess, sys
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BG, INK = '#15120e', '#dccaa3'


def chrome(html_path, png, w, h, scale=1):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--screenshot=' + os.path.abspath(png),
                    '--window-size=%d,%d' % (w, h), '--force-device-scale-factor=%s' % scale,
                    'file://' + os.path.abspath(html_path)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=240)


def page(body):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:%s;font:13px Georgia,serif;color:#8a7f6a}'
            '.wood-ink{color:%s}svg{display:block}</style></head><body>%s</body></html>' % (BG, INK, body))


def one(out, svg, W):
    s = open(svg, encoding='utf-8').read()
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', s)
    vw, vh = float(m.group(3)), float(m.group(4))
    H = int(round(W * vh / vw))
    s = re.sub(r'(<svg [^>]*?) width="\d+" height="\d+"', r'\1 width="%d" height="%d"' % (W, H), s, count=1)
    hp = out + '.html'
    open(hp, 'w', encoding='utf-8').write(page(s))
    chrome(hp, out, W, H)


def crop(out, svg, x, y, w, h, px=900):
    s = open(svg, encoding='utf-8').read()
    s = re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"', 'viewBox="%g %g %g %g" width="%d" height="%d"' % (x, y, w, h, px, int(px * h / w)), s, count=1)
    hp = out + '.html'
    open(hp, 'w', encoding='utf-8').write(page(s))
    chrome(hp, out, px, int(px * h / w))


def grid(out, W, cols, svgs):
    cw = W // cols
    cells = []
    for p in svgs:
        s = open(p, encoding='utf-8').read()
        s = re.sub(r'(<svg [^>]*?) width="\d+" height="\d+"', r'\1 width="%d" height="%d"' % (cw - 8, cw - 8), s, count=1)
        cells.append('<div style="padding:4px">%s<div style="text-align:center">%s</div></div>' % (s, os.path.basename(p)))
    rows = (len(svgs) + cols - 1) // cols
    body = '<div style="display:grid;grid-template-columns:repeat(%d,%dpx)">%s</div>' % (cols, cw, ''.join(cells))
    hp = out + '.html'
    open(hp, 'w', encoding='utf-8').write(page(body))
    chrome(hp, out, W, rows * (cw + 24) + 10)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'one':
        one(a[1], a[2], int(a[3]))
    elif a[0] == 'crop':
        crop(a[1], a[2], *[float(v) for v in a[3:7]], px=int(a[7]) if len(a) > 7 else 900)
    else:
        grid(a[1], int(a[2]), int(a[3]), a[4:])
    print(a[1])


def one2(out, svg, W, scale=2):
    s = open(svg, encoding='utf-8').read()
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', s)
    vw, vh = float(m.group(3)), float(m.group(4))
    H = int(round(W * vh / vw))
    s = re.sub(r'(<svg [^>]*?) width="\d+" height="\d+"', r'\1 width="%d" height="%d"' % (W, H), s, count=1)
    open(out + '.html', 'w', encoding='utf-8').write(page(s))
    chrome(out + '.html', out, W, H, scale)
