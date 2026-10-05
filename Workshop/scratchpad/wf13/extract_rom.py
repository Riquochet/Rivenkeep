"""extract_rom.py (wf13) -- every romanised Orrowen line on the story page's Original tab, grouped by unit, with the
analyzer's mechanical word gloss as a draft for the gloss writers.  -> gloss_in/<UNIT>.json"""
import json, re, os, sys, html, collections
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
sys.path.insert(0, S + '/wf12/orig')
import orr_analyze as OA
LEX = OA.Lexicon(S + '/wf12/orig/lexicon_orrowen.tsv') if os.path.exists(S + '/wf12/orig/lexicon_orrowen.tsv') else OA.Lexicon(S + '/wf12/lexicon_orrowen_full.tsv')
panes = json.load(open(S + '/wf12/orig/panes.json'))
LEAF_UNIT = {'front': 'S11', 'contents': 'S11', 'foreword': 'S01', 'invocation': 'S01', 't-I-1': 'S01'}
DET = re.compile(r'<details class="tr rom[^"]*"><summary>(.*?)</summary><div class="tr-body">(.*?)</div></details>', re.S)
def text(h):
    return html.unescape(re.sub(r'<[^>]+>', '', h)).strip()
def words(line):
    return [w for w in line.split() if re.search(r"[A-Za-zÀ-ž']", w)]
def draft(w):
    core = re.sub(r"^[^\w']+|[^\w']+$", '', w)
    try:
        r = OA.analyze_line(core, LEX) if hasattr(OA, 'analyze_line') else None
    except Exception:
        r = None
    return core, r
out = collections.defaultdict(list)
seen = set()
for leaf, blocks in panes.items():
    for b in blocks:
        unit = (b.get('src') or '').split(':')[0] or LEAF_UNIT.get(leaf, '?')
        for m in DET.finditer(b.get('html', '')):
            label = text(m.group(1))
            for p in re.findall(r'<p[^>]*>(.*?)</p>', m.group(2), re.S):
                line = text(p)
                if not line or not words(line):
                    continue
                key = line
                out[unit].append({'leaf': leaf, 'para_index': b.get('para_index'), 'label': label, 'rom': line,
                                  'english': b.get('book', ''), 'dup': key in seen})
                seen.add(key)
os.makedirs(S + '/wf13/gloss_in', exist_ok=True)
for u, rows in out.items():
    json.dump(rows, open(S + '/wf13/gloss_in/%s.json' % u, 'w'), ensure_ascii=False, indent=1)
print({u: (len(r), sum(len(words(x['rom'])) for x in r)) for u, r in sorted(out.items())})
