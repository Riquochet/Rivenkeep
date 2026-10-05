"""Independent check of the web copy against the host's page contract."""
import re, sys, os, collections
P = sys.argv[1]
raw = open(P, 'rb').read(); w = raw.decode('utf-8')
out = []
def ok(c, msg): out.append(('PASS' if c else 'FAIL') + '  ' + msg)
ok(w.lstrip().startswith('<title>'), 'title first: %r' % w[:45])
tags = re.findall(r'<(!doctype|html|head|body)\b|</(html|head|body)>', w, re.I)
ok(not tags, 'no doctype/html/head/body tags (%d found)' % len(tags))
styles = re.findall(r'<style\b[^>]*>(.*?)</style>', w, re.S)
ok(len(styles) == 1, 'one <style> element (%d)' % len(styles))
css = '\n'.join(styles)
css_nc = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
roots = [m for m in re.finditer(r'(^|[}\s,])(:root)\s*\{', css_nc)]
ok(len(roots) == 1, 'one :root rule in the CSS (%d)' % len(roots))
m = re.search(r':root\s*\{([^}]*)\}', css_nc)
root = m.group(1) if m else ''
ok('color-scheme:dark' in root.replace(' ', ''), ':root carries color-scheme: dark')
ntok = len(re.findall(r'--[\w-]+\s*:', root))
ok(ntok > 10, ':root holds %d tokens' % ntok)
rest = css_nc[:m.start()] + css_nc[m.end():] if m else css_nc
# strip font-face src (base64), strings and urls before scanning for colours
rest2 = re.sub(r'url\([^)]*\)', 'url()', rest)
rest2 = re.sub(r'"[^"]*"|\'[^\']*\'', '""', rest2)
LIT = re.compile(r'(?<![\w-])#[0-9a-fA-F]{3,8}(?![\w-])|(?<![\w-])(?:rgba?|hsla?)\([^()]*\)')
NAMED = re.compile(r':\s*[^;{}]*?(?<![\w-])(white|black|red|green|blue|gray|grey|silver|gold|orange|yellow|purple|transparent)(?![\w-])', re.I)
lits = LIT.findall(rest2)
named = [x for x in NAMED.findall(rest2)]
ok(not lits and not named, 'no literal colours in the CSS outside :root (%d hex/rgb, %d named: %s)' % (len(lits), len(named), (lits + named)[:6]))
body_bg = re.search(r'(^|[}\s])body\s*\{[^}]*background(?:-color)?\s*:\s*([^;}]+)', rest)
ok(bool(body_bg) and body_bg.group(2).strip().startswith('var(--'), 'body background from a token: %s' % (body_bg.group(2).strip() if body_bg else None))
# colours in markup outside the style: style="" attributes and svg presentation attributes
html_part = w.replace(styles[0], '') if styles else w
attr_cols = re.findall(r'\b(fill|stroke|stop-color|color|flood-color|lighting-color)\s*=\s*"([^"]*)"', html_part)
attr_lit = collections.Counter(v for a, v in attr_cols if LIT.fullmatch(v.strip()) or v.strip().lower() in ('white', 'black', 'red', 'green', 'blue', 'gray', 'grey'))
ok(not attr_lit, 'no literal colours in markup presentation attributes (%s)' % dict(list(attr_lit.items())[:6]))
st_attr = re.findall(r'\sstyle="([^"]*)"', html_part)
st_lit = [s for s in st_attr if LIT.search(s)]
ok(not st_lit, 'no literal colours in style="" attributes (%d style attrs, %d with a colour: %s)' % (len(st_attr), len(st_lit), st_lit[:3]))
# outside loads
urls = set(re.findall(r'(?:href|src)\s*=\s*"(https?:[^"]*)"', w)) | set(re.findall(r'url\(\s*[\'"]?(https?:[^)\'"]*)', w)) | set(re.findall(r'@import\s+[\'"]?(https?:[^\'";]*)', w))
bad = [u for u in urls if not re.match(r'https://fonts\.(googleapis|gstatic)\.com', u)]
ok(not bad, 'outside loads Google Fonts only: %s' % sorted(urls)[:3] + ('; bad: %s' % bad if bad else ''))
links = [h for h in re.findall(r'<link\b[^>]*>', w)]
ok(all('fonts.googleapis.com' in l or 'fonts.gstatic.com' in l for l in links), '%d <link> elements, all Google Fonts' % len(links))
scripts = re.findall(r'<script\b([^>]*)>', w)
ok(all('src=' not in s for s in scripts), '%d <script> elements, none external' % len(scripts))
rel = [h for h in re.findall(r'\shref="([^"#][^"]*)"', w) if not h.startswith('https://fonts.')]
ok(not rel, 'no links to other files (%s)' % rel[:3])
size = len(raw)
ok(size < 15.5 * 1024 * 1024, 'size %d bytes = %.2f MiB < 15.5 MB' % (size, size / 1048576))
fontface = re.findall(r'@font-face\s*\{[^}]*\}', css)
ok(all('data:' in f or 'fonts.gstatic' in f for f in fontface), '%d @font-face, inline base64' % len(fontface))
ok('env(safe-area-inset-top' in css, 'the sticky bars at env(safe-area-inset-top)')
print('\n'.join(out))
print('FAILS', sum(1 for o in out if o.startswith('FAIL')))
