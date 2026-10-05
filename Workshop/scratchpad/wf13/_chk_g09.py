import re, sys, collections, difflib
sys.path.insert(0, 'wf11')
from _assemble_plain_v3 import cut, strip_header
COMMENT = re.compile(r'<!--.*?-->')
BLOCK = re.compile(r'^(?:> ?)*:::.*$')
CHIP = re.compile(r'\[⟦[^⟧]*⟧\]|⟦[^⟧]*⟧')
PAIR = re.compile(r'\{\{[^}]*\}\}')
TOKEN = re.compile(r'\{[A-Z_]+\}')
def marks(body):
    out=[]
    for ln in body:
        s=ln.strip()
        if BLOCK.match(s): out.append(s)
        out += COMMENT.findall(ln) + CHIP.findall(ln)
    return out
def nb(body):  # native blocks whole
    out=[];inb=False
    for ln in body:
        if ln.startswith(':::'):
            inb = not inb if ln.strip()==':::' or inb else True
            out.append(ln); continue
        if inb: out.append(ln)
    return out
def bold(body): return [l for l in body if l.startswith('**')]
new = dict(cut(strip_header(open('wf13/plain/g09.md').read())))
old = dict(cut(open('wf11/plain_v3.md').read()))
book = dict(cut(open('wf11/book_v3.md').read()))
for k in new:
    if k in (None,'---'): continue
    print('==',k)
    for name,f in (('marks',marks),('native',nb),('bold',bold)):
        a,b=f(old[k]),f(new[k])
        print('  ',name,'same' if a==b else 'DIFF')
        if a!=b:
            for d in difflib.unified_diff(a,b,lineterm='',n=0): print('     ',d)
    print('   pairs book',sorted(set(PAIR.findall('\n'.join(book[k])))),'new',sorted(set(PAIR.findall('\n'.join(new[k])))))
    bw=len([w for l in book[k] if not l.startswith('<!--') for w in l.split()])
    nw=len([w for l in new[k] if not l.startswith('<!--') for w in l.split()])
    print('   words book',bw,'new',nw, f'{nw/bw*100:.0f}%')
