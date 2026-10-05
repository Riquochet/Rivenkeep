"""to_ink.py (wf12 private copy) -- the leaf-hand's token string -> Garl Flenn markup, and the canon's own token strings.

RECONSTRUCTED 2026-10-03 for the wf12 merge, because the scratch cleaner removed wf7/to_ink.py (its symlinks in wf8 and in
the Rivenkeep_Workshop backup point at nothing), as it removed wf7/orrowen/leafhand.py, which was rebuilt from
leafhand.json.  It does only what ink.py and build_original.py ask of it:

  * tokens_to_markup(tok): the font's markup, as GarlFlenn.fea reads it: a word's letters run together (the font's
    LIG lookup joins t+h, d+h, r+h itself, so a ZWNJ is set where t, d or r and h are two letters); a bite after its
    letter as a combining mark (^S U+032C, ^N U+033A, the font's biteS / biteN); the harmonic letters A and O kept in
    capitals (the font's Acap / Ocap, HARM lookup); '=' for the sealing lintel; the perpend '|' as a full stop and the
    wedge ',' as a comma, each set on its word; '#gate' as ' #', '#coping' as ' ¶' in place of the last perpend.
    Checked against the wf8 build: the 326 ink lines of wf8/out/Rivenkeep_Legends_Original.html, each re-tokenised
    from its romanisation by ink.py, come out of this function character for character (wf12/merge/inkre/).
  * SAMPLES: [(key, romanisation, tokens)], the canon's own written lines, read from orrowen_v2.md §11.1-§11.10 (the
    living tongue's blockquote and the first token block under it).  Read only.
"""
import os
import re

BITE = {'S': '̬', 'N': '̺'}
ZWNJ = '‌'


def word_markup(w):
    lint = w.startswith('=')
    s, prev = '', None
    for p in w.lstrip('=').split('.'):
        if not p:
            continue
        base, _, bite = p.partition('^')
        if prev in ('t', 'd', 'r') and base == 'h':
            s += ZWNJ
        s += base
        if bite:
            s += BITE[bite[0]]
        prev = base
    return ('=' if lint else '') + s


def tokens_to_markup(tok):
    out = ''
    for w in tok.split():
        if w == '|':
            if not out.endswith('.'):
                out += '.'
            continue
        if w == ',':
            out += ','
            continue
        if w == '#gate':
            out += ' #'
            continue
        if w == '#coping':
            out = out.rstrip('.') + ' ¶'
            continue
        out += (' ' if out else '') + word_markup(w)
    return out


def _samples():
    here = os.path.dirname(os.path.abspath(__file__))
    spec = os.path.join(os.path.dirname(os.path.dirname(here)), 'wf7', 'orrowen_v2.md')
    try:
        L = open(spec, encoding='utf-8').read().split('\n')
    except OSError:
        return []
    out = []
    a = next(i for i, l in enumerate(L) if l.startswith('## 11 '))
    b = next(i for i, l in enumerate(L) if l.startswith('### 11.11'))
    key, roms, i = None, [], a
    while i < b:
        l = L[i]
        m = re.match(r'^### (11\.\d+)', l)
        if m:
            key, roms = m.group(1), []
        elif l.startswith('> **') and key:
            t = l[2:]
            parts = re.findall(r'\*\*([^*]+)\*\*', t)
            if parts and re.search(r'[A-Z]{4,} [A-Z]{3,}', parts[0]):     # the Hal, in capitals: not the living tongue
                i += 1
                continue
            roms.append(' '.join(parts))
        elif l.startswith('```') and key and roms:
            j = i + 1
            body = []
            while not L[j].startswith('```'):
                body.append(L[j])
                j += 1
            if body and '@' not in body[0]:
                rom = ' '.join(roms).replace(' · ', ' ').strip()
                rom = re.sub(r'\s+', ' ', rom)
                out.append((key, rom, ' '.join(' '.join(body).split())))
                roms = []
            i = j
        i += 1
    return out


SAMPLES = _samples()
