"""leafhand.py -- the leaf-hand (Garl Flenn) glyph table and pen-movement counter.

RECONSTRUCTED 2026-10-02 from leafhand.json (the table the original module wrote) after the scratch
cleaner removed the original. G is the glyph table (letters and marks, keyed by token); BITES the two
bites; movements(tokstr) counts, as orrowen_v2 §8.9 says, one for every stroke that does not begin where
the pen already is, and one for every bite, lintel and mark."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(HERE, 'leafhand.json'), encoding='utf-8'))
METRICS = _D['metrics']
LETTERS = _D['letters']
MARKS = _D['marks']
BITES = _D['bites']
G = dict(LETTERS)
G.update(MARKS)
EPS = 0.02


def _word_moves(parts):
    """pen movements for one written word: its letters joined where a stroke begins where the pen is"""
    moves, pen, x = 0, None, 0.0
    for p in parts:
        k = p.split('^')[0]
        g = LETTERS.get(k)
        if g is None:
            moves += 1
            continue
        for st in g['strokes']:
            x0, y0 = st['pts'][0]
            start = (x + x0, y0)
            if pen is None or abs(pen[0] - start[0]) > EPS or abs(pen[1] - start[1]) > EPS:
                moves += 1
            x1, y1 = st['pts'][-1]
            pen = (x + x1, y1)
        x += g['adv']
        if '^' in p:
            moves += 1          # the bite
    return moves


def movements(tokstr):
    n = 0
    for w in tokstr.split():
        if w in MARKS or w.startswith('#'):
            n += 1
            continue
        if w.startswith('='):
            n += 1              # the lintel
            w = w.lstrip('=')
        n += _word_moves(w.split('.'))
    return n
