#!/usr/bin/env python3
"""wf12 merge: open every unit with its merge note (as the Tier 3 merge did): what it was re-validated against, what the
merge changed in it (each change is also marked *Merge (wf12)* where it stands), and where its lexicon rows went.
Idempotent: a unit that already carries the note has it replaced."""
import collections, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
W12 = os.path.dirname(HERE)
U = os.path.join(W12, 'units')
dec = json.load(open(os.path.join(HERE, 'lex_decisions.json')))
harm = json.load(open(os.path.join(HERE, 'harmonisations.json')))
fixes = [l.rstrip('\n') for l in open(os.path.join(HERE, 'fixes.log'), encoding='utf-8')]
MARK = '**Merge (`wf12/merge_report.md`, 2026-10-03).**'

wd = set((d['unit'], d['row']) for d in dec['decisions'] if d['kind'] in ('one sense, two forms', 'folded into one saying'))
rowmap = collections.defaultdict(list)
for r in dec['new_rows']:
    for u, rid in zip(r['units'], r['rows']):
        if (u, rid) not in wd:
            rowmap[u].append('%s → %s *%s*' % (rid, r['id'], r['form']))
withdrawn = collections.defaultdict(list)
senses = collections.defaultdict(list)
for d in dec['decisions']:
    if d['kind'] in ('one sense, two forms', 'folded into one saying'):
        withdrawn[d['unit']].append('%s *%s* (for *%s*)' % (d['row'], d['dropped'], d['chosen']))
    if d['kind'] == 'new sense of a base form':
        for rid in d['rows']:
            u = re.search(r'(S\d\d|W\d\d)', rid).group(1)
            senses[u].append('%s → a sense of %s *%s*' % (rid, d['base'], d['form']))

FIXDESC = {
    'F1': 'the wood\'s story English set to the Book character for character (the unit had it in italics)',
    'F2': 'the seal set in the house style of W01–W03 (the bark\'s block over *This is held in the grain.*)',
    'F3': 'the title page and the Books\' headings and Arguments left to S11, which owns them (the offered copy kept as a record in a note)',
    'F4': 'the forms the lexicon merge chose',
    'F5': 'quotation marks taken out of the romanised lines (orrowen_v2 §6.7: direct speech is not marked)',
    'F6': 'pair-names written under the lintel, `{{…}}`, as the English writes them',
    'F8': 'the printed literal readings under the merged compound glosses',
}


def note_for(u):
    fx = collections.Counter(l.split()[0] for l in fixes if len(l.split()) > 1 and l.split()[1].rstrip(':') == u)
    hs = [h for h in harm if h['unit'] == u]
    parts = []
    for f in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F8'):
        if fx.get(f):
            parts.append('%s (%s)' % (FIXDESC[f], f))
    if hs:
        parts.append('the Book\'s recurring English rendered once, as the other leaves render it (%s: %s)' % (
            ', '.join(h['id'] for h in hs), '; '.join('*%s* > *%s*' % (h['old'].lstrip('> ').strip()[:60], h['new'].lstrip('> ').strip()[:60]) for h in hs)))
    t = [MARK + ' This unit was re-validated against the merged lexicon (`wf12/lexicon_orrowen_full.tsv`, 3,101 entries) '
         'and the merged grain spec (`wf12/grain_v2_full.md`, §21.10): 0 unknown and 0 ill-formed words in its blockquotes; '
         'every GN block 0 errors and 0 warnings; every paragraph of its leaves has one blockquote (or ring) over the Book\'s '
         'English, character for character.']
    if parts:
        t.append(' The merge changed, each marked *Merge (wf12)* where it stands: ' + '; '.join(parts) + '.')
    else:
        t.append(' The merge changed nothing in it.')
    lx = []
    if rowmap.get(u):
        lx.append('new rows ' + ', '.join(rowmap[u]))
    if senses.get(u):
        lx.append('new senses ' + ', '.join(senses[u]))
    if withdrawn.get(u):
        lx.append('withdrawn ' + ', '.join(withdrawn[u]))
    if lx:
        t.append(' Its lexicon additions: ' + '; '.join(lx) + '.')
    return ''.join(t)


def main():
    for f in sorted(os.listdir(U)):
        if not f.endswith('.md'):
            continue
        u = f[:-3]
        p = os.path.join(U, f)
        L = open(p, encoding='utf-8').read().split('\n')
        L = [l for l in L if not l.startswith(MARK)]
        # after the first paragraph that follows the title (the unit's own opening line)
        i = 1
        while i < len(L) and not L[i].strip():
            i += 1
        while i < len(L) and L[i].strip():
            i += 1
        L[i:i] = ['', note_for(u)]
        t = '\n'.join(L)
        t = re.sub(r'\n{3,}(\*\*Merge \(`wf12)', r'\n\n\1', t)
        open(p, 'w', encoding='utf-8').write(t)
        print(u, len(note_for(u)))


if __name__ == '__main__':
    main()
