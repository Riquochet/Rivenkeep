import json,re,sys
d=json.load(open('panes.json'))
def skel(h):
    h=re.sub(r'<details class="([^"]*)"><summary>(.*?)</summary>.*?</details>',lambda m:'[fold %s: %s]'%(m.group(1),re.sub('<[^>]+>','',m.group(2))),h,flags=re.S)
    h=re.sub(r'<span class="svg-slot" data-(svg3|native)="([^"]+)"[^>]*></span>',r'[\1:\2]',h)
    h=re.sub(r'<p class="(ink[^"]*)"[^>]*>(.*?)</p>',lambda m:'[%s: %s]'%(m.group(1),re.sub('<[^>]+>','',m.group(2))[:50]),h,flags=re.S)
    h=re.sub(r'<figure class="([^"]*)">',r'<fig \1>',h)
    h=re.sub(r'</?(div|figcaption|span)[^>]*>','',h)
    h=re.sub(r'<span class="cap">','',h)
    return h
anchors=sys.argv[1].split(',')
kinds=sys.argv[2].split(',') if len(sys.argv)>2 else None
for a in anchors:
    for i,b in enumerate(d[a]):
        if kinds and b['kind'] not in kinds and not ('role' in b and 'role' in kinds): continue
        print('%s %d %s %s %s %s %s | %s'%(a,i,b['kind'],b.get('src'),b.get('wrap') or '',b.get('voice') or '',b.get('role') or '',b['book'][:60].replace('\n',' / ')))
        print('    '+skel(b['html'])[:600])
