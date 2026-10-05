"""web_copy.py - the private web copy of the story page for claude.ai (wf12, 2026-10-03), from the same build.

The host's page contract:
  * no <!doctype>, <html>, <head> or <body> tags (the host wraps the file); the first thing in the file is
    <title>The Legends of Rivenkeep</title>, then the Google Fonts <link>, then one <style>
  * every colour a token on :root; the page deliberately single-theme dark (color-scheme: dark on :root) with an
    explicit body background from a token; no literal colours in component rules
  * the leaf-hand font inline (base64 @font-face, from panes.css); outside loads only from Google Fonts
  * the sticky bar at top: env(safe-area-inset-top, 0px); a side gutter of at least 16px at every width
  * no links to other repo files; no print rules (the copy is for the screen)

make(css, body, fonts, version) -> the file's text. tokenize(css) -> (css, {token: literal}) is the colour pass:
every colour literal outside :root (hex, rgb[a](), hsl[a](), a named colour, transparent) becomes var(--token),
a token that already holds that literal on :root where there is one, else a new one named for its value; every
top-level :root rule is merged into one, first.
"""
import re

NAMED = set('''aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond blue blueviolet brown
burlywood cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod
darkgray darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen
darkslateblue darkslategray darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue
firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod gray green greenyellow grey honeydew
hotpink indianred indigo ivory khaki lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan
lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon lightseagreen lightskyblue lightslategray
lightslategrey lightsteelblue lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue mediumorchid
mediumpurple mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred midnightblue mintcream
mistyrose moccasin navajowhite navy oldlace olive olivedrab orange orangered orchid palegoldenrod palegreen
paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue purple rebeccapurple red rosybrown
royalblue saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue slateblue slategray slategrey snow
springgreen steelblue tan teal thistle tomato turquoise violet wheat white whitesmoke yellow yellowgreen
transparent'''.split())
LIT = re.compile(r'(?<![\w-])#[0-9a-fA-F]{3,8}(?![\w-])|(?<![\w-])(?:rgba?|hsla?)\([^()]*\)|(?<![\w-])[a-zA-Z]+(?![\w(-])')


def protect(css):
    keep = []

    def k(m):
        keep.append(m.group(0))
        return '\x02%d\x02' % (len(keep) - 1)
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)          # the copy carries no comments
    css = re.sub(r'url\([^)]*\)|"[^"\n]*"|\'[^\'\n]*\'', k, css, flags=re.S)
    return css, keep


def restore(css, keep):
    return re.sub(r'\x02(\d+)\x02', lambda m: keep[int(m.group(1))], css)


def blocks(css):
    """top-level statements: [(prelude, body or None)], brace-aware"""
    out = []
    i, n = 0, len(css)
    while i < n:
        j = i
        while j < n and css[j] not in '{;':
            j += 1
        if j >= n:
            if css[i:].strip():
                out.append((css[i:], None))
            break
        if css[j] == ';':
            out.append((css[i:j + 1], None))
            i = j + 1
            continue
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{':
                depth += 1
            elif css[k] == '}':
                depth -= 1
            k += 1
        out.append((css[i:j], css[j + 1:k - 1]))
        i = k
    return out


def norm(lit):
    return re.sub(r'\s+', '', lit.lower())


def tok_name(lit):
    v = norm(lit)
    if v.startswith('#'):
        return '--c-' + v[1:]
    m = re.match(r'(rgba?|hsla?)\((.*)\)', v)
    if m:
        parts = [p for p in re.split(r'[,/\s]+', m.group(2)) if p]
        if m.group(1).startswith('rgb') and len(parts) >= 3:
            h = ''.join('%02x' % int(round(float(p.rstrip('%')) * (2.55 if p.endswith('%') else 1)))
                        for p in parts[:3])
            a = parts[3] if len(parts) > 3 else ''
            return '--c-' + h + (('-a' + a.replace('.', '').replace('%', '')) if a else '')
        return '--c-' + re.sub(r'[^0-9a-z]+', '-', v).strip('-')
    return '--c-' + v


def tokenize(css):
    css, keep = protect(css)
    root_decls = []
    rest = []
    for pre, body in blocks(css):
        if body is not None and pre.strip() == ':root':
            root_decls.append(body.strip().rstrip(';'))
        else:
            rest.append((pre, body))
    # the existing tokens, by the literal they hold
    by_lit = {}
    decls = []
    for d in ';'.join(root_decls).split(';'):
        d = d.strip()
        if not d:
            continue
        decls.append(d)
        m = re.match(r'(--[\w-]+)\s*:\s*(.+)$', d, re.S)
        if m and LIT.fullmatch(m.group(2).strip()) and is_colour(m.group(2).strip()):
            by_lit.setdefault(norm(m.group(2)), m.group(1))
    new = {}

    def swap_value(v):
        def one(m):
            s = m.group(0)
            if not is_colour(s):
                return s
            key = norm(s)
            name = by_lit.get(key)
            if not name:
                name = tok_name(s)
                while name in new and new[name] != key:
                    name += 'x'
                new[name] = key
                by_lit[key] = name
            return 'var(%s)' % name
        return LIT.sub(one, v)

    def swap_body(body):
        # declarations (and, inside @media/@supports, nested rules)
        if '{' in body:
            return ''.join(emit(p, b) for p, b in blocks(body))
        out = []
        for d in body.split(';'):
            if ':' in d:
                prop, val = d.split(':', 1)
                out.append(prop + ':' + swap_value(val))
            else:
                out.append(d)
        return ';'.join(out)

    def emit(pre, body):
        if body is None:
            return pre
        p = pre.strip()
        if p.startswith('@media') and ('print' in p or 'prefers-color-scheme' in p):
            return ''                       # a screen copy, one theme
        return '%s{%s}' % (pre.rstrip(), swap_body(body))

    out = ''.join(emit(p, b) for p, b in rest)
    root = ':root{color-scheme:dark;%s;%s}\n' % (';'.join(decls), ';'.join('%s:%s' % (k, v) for k, v in sorted(new.items())))
    css = root + out
    return restore(css, keep), new


def is_colour(s):
    s = s.strip()
    if s.startswith('#'):
        return bool(re.fullmatch(r'#[0-9a-fA-F]{3,8}', s)) and len(s) in (4, 5, 7, 9)
    if re.match(r'(rgba?|hsla?)\(', s, re.I):
        return True
    return s.lower() in NAMED


def make(css, body, fonts, version):
    css, new = tokenize(css)
    # the body: an explicit background from a token, under the host's own body too
    css += '\nhtml,body{background:var(--bg);color:var(--text)}\n'
    body = body.strip() + '\n'
    assert not re.search(r'<(?:!doctype|html|head|body)[\s>]', body, re.I)
    page = ('<title>The Legends of Rivenkeep</title>\n<link href="%s" rel="stylesheet">\n<style>\n'
            '/* The Legends of Rivenkeep, %s: the private web copy. One theme, deliberately dark: every colour a token on :root. */\n'
            '%s</style>\n%s' % (fonts.replace('&', '&amp;'), version, css, body))
    return page
