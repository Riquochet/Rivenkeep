#!/usr/bin/env python3
"""Build wf8/concepts_full.tsv = wf7/coverage/concepts.tsv with the register corrections of grain_v2_full.md §21.9.5
applied in place (the old form kept in the note), and a row for every compound of §21.9.2 and every reading of §21.9.3
(kind `add`). Every grain cell is checked with the private validator's fragment check (as coverage/check_coverage.py
does); a reading whose examples are prose keeps only the fragments that parse, and its prose goes in the note."""
import importlib.util, json, os, re, sys
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('gv', os.path.join(HERE, 'groot', 'wf7', 'grain_validate.py'))
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
sys.path.insert(0, HERE)
import gen_grain_full as G

SRC = S + '/wf7/coverage/concepts.tsv'
OUT = S + '/wf8/concepts_full.tsv'

# (lemma cell as it stands) -> (new grain, new kind or None, note to append)
CORRECT = {
    'mistake': ('~HOLD ; !TURN+HOLD', 'add', "wf8 merge (A17): \"must not be mistaken\" is !TURN+HOLD (was !~HOLD, which the drawing cannot tell from ~!HOLD)"),
    'shard': ('BREAK+SQUARE{only}[STILL]', 'add', "wf8 merge (W02, A22): was SQUARE½{only}[STILL], which reads as the Mute Square cited"),
    'jar': ('~BREAK+HOLD', 'add', "wf8 merge: BREAK+HOLD is now a glossed compound, a cracked cup (W06)"),
    'strength': ('LIVE+GO', 'add', "wf8 merge (W06): life going out; was LIVE"),
    'bank': ('HOLD →as ~ROOT', 'cmp', "wf8 merge (W03 #1): ~ROOT → ~EARTH beside it; was →as ~ROOT+HOLD → ~EARTH, which reads \"seem to remember\""),
    'leave': ('GO → @8 ; !GO → @8 ; RISE{still}', None, "wf8 merge (A15): !GO → @8 is not go away, will not leave (IV.2 r13)"),
    'away': ('GO → @8 ; !GO → @8', None, "wf8 merge (A15): !GO → @8, not go home, carried away from home (IV.6 r4)"),
    'grain': ('[grain-arc in names] ; CARVE ; WOOD', None, "wf8 merge (W03 #5): the kind of a heart's wood (\"that is our grain\") is WOOD on the teller's file, NAME to it and to the said-pocket of the grain's name; CARVE stays for the shape of a knowing"),
    'play, trick': ('~ ; ~GO#1{only}', None, "wf8 merge (A17): \"never plays one trick twice\" is ~GO#1{only} with a memory ray (was !~GO#2, which the drawing cannot tell from ~!GO#2)"),
    'matter, empty': ('~ ; !SPENT', None, "wf8 merge (W05, A17): \"silent and not empty\" is SQUARE+!MOUTH →with !SPENT (was !~, which reads backwards)"),
}


def frag_ok(fr):
    F = g.Findings()
    try:
        g.check_fragment(fr, F, 'x')
    except Exception:
        return False
    return not [x for x in F.items if x['level'] == 'ERROR']


def main():
    out, fixed = [], []
    for ln in open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('#') or not ln.strip():
            out.append(ln)
            continue
        c = ln.split('\t') + [''] * 4
        lem = c[0].strip()
        if lem in CORRECT:
            gr, kind, note = CORRECT[lem]
            assert frag_ok(gr), gr
            old = c[1]
            c[1] = gr
            if kind:
                c[2] = kind
            c[3] = (c[3] + '; ' if c[3] else '') + note + ('' if old == gr else ' [was: %s]' % old)
            fixed.append(lem)
            out.append('\t'.join(c[:4]))
        else:
            out.append(ln)
    assert set(fixed) == set(CORRECT), set(CORRECT) - set(fixed)
    out.append('# ---- wf8 merge, 2026-09-28: the compounds of grain_v2_full.md §21.9.2 and the readings of §21.9.3 ----')
    n_c = n_r = n_skip = 0
    for k, c in G.compounds().items():
        eng = c['gloss'].split(':', 1)[1].split('|')[0]
        lem = re.sub(r'\s*\(.*?\)', '', eng).strip()
        assert frag_ok(k), k
        out.append('\t'.join([lem, k, 'add', 'wf8 %s; §21.9.2; %s' % (', '.join(c['units']), eng)]))
        n_c += 1
    for e, gr, w in G.A15:
        frags = [f for f in re.findall(r'`([^`]+)`', gr) if frag_ok(f)]
        if not frags:
            n_skip += 1
            continue
        lem = re.sub(r'\s*\(.*?\)', '', e).replace('*', '').strip()
        out.append('\t'.join([lem, ' ; '.join(dict.fromkeys(frags)), 'add', 'wf8 §21.9.3 (A15); %s; %s' % (w, re.sub(r'\s+', ' ', gr.replace('|', '/')))]))
        n_r += 1
    open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(corrected=sorted(fixed), compounds=n_c, readings=n_r, readings_without_fragment=n_skip),
              open(os.path.join(HERE, 'concepts_stats.json'), 'w'), indent=1)
    print('wrote %s: %d rows corrected, %d compound rows, %d reading rows (%d readings had no checkable fragment)' % (
        OUT, len(fixed), n_c, n_r, n_skip))


if __name__ == '__main__':
    main()
