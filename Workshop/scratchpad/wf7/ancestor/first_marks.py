"""The first marks: the ancestral sign-set, and what each became on stone and in wood.

MARKS: id -> dict(name (English), word (ancestral), mean, draw (list of primitives), stone, wood)
Primitives, in a 10 x 10 box with y up:
  ("l", [(x,y),...])  a stroke (polyline)       ("c", cx, cy, r, a0, a1)  an arc (degrees, ccw from +x)
  ("lens", cx, cy, len, w, rot)                   ("sq", cx, cy, s)
  ("drop", cx, cy, len, w)                        ("dot", cx, cy, r)       ("fill", [(x,y),...]) a solid shape
Drawn as a first hand: one even stroke, round caps, no taper and no facets (neither chisel nor knife).
"""
import math, json

MARKS = {}
def M(id_, name, word, mean, draw, stone, wood):
    MARKS[id_] = dict(id=id_, name=name, word=word, mean=mean, draw=draw, stone=stone, wood=wood)

M("STEM", "the Stem", "tolm-", "a standing thing: a stone set up, a trunk", [("l", [(5, 0.5), (5, 9.5)])],
  "every consonant's upright; a letter is still called a tolm", "the cut itself: GO; the trunk of TREE and RISE (thael)")
M("BAR", "the Bar", "hosk-", "a stone laid across; a cap", [("l", [(1, 5), (9, 5)])],
  "the laid stones; the sealing lintel; the long-stone", "the bar and the ring-arc that lie along a ring")
M("FORE", "the Fore", "re-il", "the one before; first", [("l", [(5, 0.5), (5, 9.5)]), ("l", [(2, 7.2), (8, 7.2)])],
  "kept whole as the foremark (proposed: the mark on the black chest, the head of the lintel column); its right arm and foot give r", "kept whole: the Bar Before (reil)")
M("END", "the End", "kul-", "leave off; stop", [("l", [(5, 0.5), (5, 8.6)]), ("l", [(2, 9.2), (8, 9.2)])],
  "the perpend (the stopping bar stood on the bed)", "STOP (rheil); laid along the whole ring, the band-rule")
M("POST", "the Post", "gann-", "a post, an upright", [("l", [(5, 0.5), (5, 5.2)])],
  "the pin of b d g r rh (a letter 'with its post')", "the posts of DOOR")
M("DOOR", "the Door", "gann-aʔ", "the two posts; a gate", [("l", [(2.5, 0.5), (2.5, 7.8)]), ("l", [(7.5, 0.5), (7.5, 7.8)]), ("l", [(1.4, 8.6), (8.6, 8.6)])],
  "kept whole: the gate mark (end of an oath); capped, the coping (end of a tale)", "kept whole: DOOR (veth)")
M("CURL", "the Curl", "oð-", "the rim where one comes to rest", [("l", [(4, 0.5), (4, 6.5)]), ("c", 5.9, 6.5, 1.9, 180, -30)],
  "the broad vowels a and o (the curl laid over a short pin as a capstone)", "the Wave (aeth); SHORE, the Turned Stern, HOME, FALL")
M("LONE", "the Lone Mark", "itt-", "this very one; one", [("l", [(4.2, 0.5), (4.2, 6.2)]), ("l", [(6.2, 7.6), (6.2, 9.6)])],
  "the slender vowels i and e (a tall pin and a low stone)", "the Lone Stroke (ith)")
M("UPON", "the Upon", "um-", "upon; (seen from below) beneath", [("l", [(3.2, 0.5), (3.2, 5)]), ("l", [(6.8, 0.5), (6.8, 5)]), ("l", [(2, 7), (8, 7)])],
  "the vowel u (two pins and a keystone raised clear)", "BENEATH (senn): the two strokes grown into one")
M("SPLIT", "the Split", "krask-", "crack, break", [("l", [(5, 0.5), (5, 5.4)]), ("l", [(5, 5.4), (3.8, 7.4), (3.2, 9.6)]), ("l", [(5, 5.4), (7.4, 8.4)])],
  "the shore (the back-leaning upright of k g h); k", "BREAK (rhass); the check of WOUND, SPENT, GRIEF; the fork (if, if not)")
M("COURSE", "the Course", "trenn-", "a running line: a course, a stream", [("l", [(3, 0.5), (3, 4.8), (7, 4.8), (7, 9.5)])],
  "the offset (the stepped upright of t d n th dh s l r rh); t; the hand's own name, Garl Dhrenn", "the WATER band; ROAD (two running lines); the ray")
M("BEARER", "the Bearer", "par-", "bear up, hold up", [("l", [(2.6, 0.5), (5.6, 8.4)]), ("l", [(4.6, 9), (9.2, 9)])],
  "the prop (the forward-leaning upright of p b m f v w); p", "BEARER (varen): the load grown round the stroke into a laden hull")
M("BOUGH", "the Bough", "sul-", "a bough; to bend", [("lens", 5, 5, 8.6, 3.2, 90)],
  "the sibilant stones of s (the lens cut straight: one stone free above, one joined below)", "HULL and BEND (seil); every curved closed shape (of wood)")
M("SQUARE", "the Square", "xreun-", "the hard thing, the set-fast; stone", [("sq", 5, 5, 6.4)],
  "rh (Hal hr): the square stood on its bed and opened", "the Mute Square (rhen); every straight closed shape (of stone); the war-pith")
M("WITHIN", "the Breath Within", "molt-", "the living middle; the heart's breath", [("l", [(5, 0.5), (5, 9.5)]), ("l", [(1.0 + 0.4 * k, 5 + 0.9 * __import__("math").sin(k * 0.785)) for k in range(21)])],
  "the nasal stone (the middle stone of m n ŋ)", "the MIST band (a pale band through the middle of the ring)")
M("BREATHING", "the Breathing", "hoss-", "breath going out", [("l", [(4.4, 0.5), (4.4, 9.5)]), ("l", [(4.4, 3.2), (7.8, 4.6)])],
  "the fricative stone (the low stone of f th h)", "LIVE (ilae): a leaf on a short stalk")
M("SAIL", "the Sail", "gwemm-", "a cloth that fills", [("l", [(3.6, 0.5), (3.6, 9.6)]), ("l", [(3.6, 9.6), (7.2, 9.6), (8.6, 8.2), (8.8, 6.6), (8.0, 5.2), (6.4, 4.4)])],
  "the approximant stones of w and l (a short top stone and a free low one)", "SAIL (reaslel)")
M("BED", "the Bed", "loð-", "the wet bed a thing is set in", [("l", [(5, 1.4), (5, 9.5)]), ("l", [(1.5, 0.6), (8.5, 0.6)])],
  "the mortar line under every word (lodh)", "DEEP (eir): a cut standing on a floor-bar")
M("ROOTS", "the Roots", "ral-", "a root; what feeds from below", [("l", [(5, 9.5), (5, 4)]), ("l", [(5, 4), (2.6, 0.8)]), ("l", [(5, 4), (4.6, 0.5)]), ("l", [(5, 4), (7.8, 1.2)])],
  "lost: the chisel set every mark on its bed instead", "ROOT, the feet of US and STONEFOLK, the memory ray's root-hairs")
M("GAP", "the Gap", "onn-", "the between", [("l", [(5, 0.5), (5, 3.8)]), ("l", [(5, 6.2), (5, 9.5)])],
  "the head-joint: the break in the bed between two word-stones", "the Breath (aenn)")
M("CUP", "the Cup", "tum-", "hold, keep", [("c", 5.6, 5, 3.2, 125, 235), ("c", 4.4, 5, 3.2, -55, 55)],
  "lost: the stone kept the word (tum, remember) and let the mark go", "HOLD (thein), OPEN, CLOSE, the palm of HAND; the seal in the bark")
M("DROP", "the Drop", "θar-", "blood", [("drop", 5, 5, 7, 4)],
  "lost", "BLOOD (thar); the Aelthar's two drops")
M("STAR", "the Star", "kris-", "a hard glint", [("l", [(5, 5), (5, 9.4)]), ("l", [(5, 5), (9.2, 6.4)]), ("l", [(5, 5), (7.6, 1.4)]), ("l", [(5, 5), (2.4, 1.4)]), ("l", [(5, 5), (0.8, 6.4)])],
  "lost", "FLASH (rheis); the star of SPARK, HUNTER and GUN")
M("WEDGE", "the Wedge", "tass-", "a blow", [("fill", [(3, 9.4), (7, 9.4), (5, 3.4)]), ("l", [(5, 3.4), (5, 0.5)])],
  "the wedge mark (a pause: the blow's base kept as a free laid stone)", "STRIKE (thass); the wedge of RAM; the causative chevron")
M("KNOT", "the Knot", "lanθ-", "hold one's place, wait", [("l", [(5, 0.5), (5, 5)]), ("lens", 5, 7, 3.6, 3, 0)],
  "lost", "the Knot (lanth)")
M("SCAR", "the Scar", "esθ-", "burn", [("fill", [(2, 9.5), (8, 9.5), (5, 0.8)])],
  "lost", "BURN (esth): a fire scar")
M("CARVE", "the Cut", "skeθ-", "hew, cut into wood", [("l", [(2.2, 9.5), (5, 0.8), (7.8, 9.5)])],
  "late: the V of the softening bite", "CARVE (seth); the Smoothed Cut")
M("LEAN", "the Lean", "iʔl-en-", "lean toward", [("l", [(2.6, 0.8), (7.4, 9.2)])],
  "the vowel y (e's pin set leaning)", "LEAN (ilen); the lean and the pair")
M("MOUTH", "the Mouth", "brenn-", "a mouth; to speak", [("l", [(5, 0.8), (3.4, 2.8), (2.5, 5.6), (2.3, 9.2)]), ("l", [(5, 0.8), (6.6, 2.8), (7.5, 5.6), (7.7, 9.2)])],
  "lost", "MOUTH (renn); the Two Mouths")
M("HAND", "the Hand", "wind-", "the whole hand", [("l", [(5, 0.5), (5, 5.2)]), ("c", 5, 7.4, 2.2, 180, 360)],
  "lost", "HAND (vinn); five")
M("EYE", "the Eye", "neʔs-", "the eye; to look", [("lens", 5, 5, 4.6, 3, 90), ("l", [(5, 0.5), (5, 2.7)]), ("l", [(5, 7.3), (5, 9.5)])],
  "lost", "EYE (neas)")
M("SEED", "the Seed", "wus-", "a seed", [("lens", 5, 7.2, 3.6, 2.8, 90), ("l", [(5, 5.4), (2.6, 1.2)]), ("l", [(5, 5.4), (7.4, 1.2)])],
  "lost", "SEED (veis)")
M("SPROUT", "the Sprout", "taw-", "sprout, grow", [("l", [(5, 0.5), (5, 9.5)]), ("l", [(5, 3), (7.4, 5)]), ("l", [(5, 5), (2.6, 7)]), ("l", [(5, 7), (7.2, 8.8)])],
  "lost (the stone kept the word, tev, a child)", "GROW and TIDE (thae); SAPLING")
M("KNEEL", "the Kneel", "roθ-", "fold the knee", [("l", [(3.4, 9.5), (3.4, 4.2), (6.6, 2.4), (6.6, 0.6), (9.2, 0.6)])],
  "lost", "KNEEL (raeth); in the Stone, 'the one they kneel to'")
M("BOND", "the Bond", "ol", "together, one with another", [("l", [(1.4, 9.6), (2.6, 7.2), (4.0, 5.2), (5, 4.2)]), ("l", [(7.8, 8.0), (6.8, 6.2), (5.8, 4.9), (5, 4.2)]), ("l", [(5, 4.2), (5, 0.5)])],
  "lost (the stone binds with mortar: lodh)", "BOND (ael); the Aelthar's joined stems; the tie")
M("STILL", "the Still", "waʔr-", "stillness", [("l", [(1.2, 4), (8.8, 4)]), ("l", [(1.2, 6.4), (8.8, 6.4)])],
  "lost", "the STILL band (vaere)")
M("FADE", "the Fade", "feʔ-", "fade, go dark", [("l", [(5, 0.5), (5, 4.4)]), ("l", [(5, 5.4), (5, 7.2)]), ("l", [(5, 8.0), (5, 8.8)]), ("dot", 5, 9.5, 0.25)],
  "lost", "DYING (veas); crumbled, ROT; laid along the ring, the DARK band")
M("PALE", "the Pale", "lenn-", "pale-bright", [("l", [(1.8, 4.0), (1.8, 5.6)]), ("l", [(3.9, 5.2), (3.9, 6.8)]), ("l", [(6.1, 4.0), (6.1, 5.6)]), ("l", [(8.2, 5.2), (8.2, 6.8)])],
  "lost", "the WHITE band (a frost ring of short ticks)")
M("EDGE", "the Rim", "enθ-", "a rim, an edge", [("l", [(5, 0.5), (5, 6.4)]), ("c", 5, 5.0, 3.6, 30, 150)],
  "lost", "EDGE (enth); the ring-arc under TIDE")
M("TALLY", "the Tally", "kail-", "a notch cut to keep a count", [("l", [(4, 0.5), (4, 9.5)]), ("l", [(4.3, 7.9), (5.4, 7.3), (4.3, 6.7)]), ("l", [(4.3, 5.7), (5.4, 5.1), (4.3, 4.5)])],
  "the numeral cap; and Kael's name", "the count and ordinal bites")
M("GIFT", "the Gift", "wi", "give; a thing set down before", [("l", [(1.6, 3), (8.4, 3)]), ("lens", 5, 6.2, 4.4, 3.4, 0)],
  "lost", "GIFT (vei)")
M("WHOLE", "the Whole", "weinn-", "sound, true, made whole", [("l", [(5, 0.5), (5, 3.8)]), ("sq", 5, 5, 1.8), ("l", [(5, 6.2), (5, 9.5)])],
  "lost (the stone kept the word, venn, true, plumb)", "MEND (veinn)")
M("TURN", "the Turn", "neθ-", "turn aside", [("l", [(4, 0.5), (4, 6), (7.6, 9.2)])],
  "lost", "TURN (neth)")
M("EDGE2", "the Blade", "kriθθ-", "a hard cutting edge", [("l", [(4, 0.5), (4, 9.5)]), ("fill", [(4.2, 9.2), (8.4, 9.2), (4.2, 5.4)])],
  "lost", "AXE (rhith)")
M("THREE", "the Three", "ros-", "three; many", [("l", [(3, 1), (3, 9)]), ("l", [(5, 1), (5, 9)]), ("l", [(7, 1), (7, 9)])],
  "lost (the stone counts with letters)", "the plural: three copies abreast")

# ---------------------------------------------------------------- the laws of form
STONE_LAWS = [
 ("C1", "The chisel straightens.", "A curve becomes a straight stroke or a corner; a closed curve opens into strokes; a solid is cut as its outline's base."),
 ("C2", "Everything stands on a bed.", "A mark is stood on the mortar line; its roots are replaced by the bed; a mark that hung or floated is set down."),
 ("C3", "Stones are laid to the right.", "An arm on the left of a stem is cut away; what is kept runs to the right, as a mason lays each stone against the last."),
 ("C4", "Three leans.", "Every upright leans forward, steps, or leans back, and nothing else."),
 ("C5", "The first sound.", "A mark is read for the first sound of its name (acrophony). Stone writes what is said."),
 ("C6", "The laying of the letters (the reform).", "The first builders' scribes made the letter of each sound out of two parts: the upright of its place, taken from the three oldest letters p, t and k; and the laid stones of its manner, taken from the mark whose name began with that kind of sound. Everything else about the old marks was let go. Like the reformed Egyptian that note 1 names, it is an economy: few strokes, laid by rule."),
 ("C7", "Small marks become pinnings.", "The marks read for a vowel become small loose stones set low between the ashlars, in mirrored pairs."),
 ("C8", "Marks of ending and binding stay marks.", "What closed or bound a line in the old hand stays outside the alphabet as punctuation: the end, the door, the bar, the tally."),
]
WOOD_LAWS = [
 ("G1", "The mark goes on a file.", "Its stem runs from the heart outward; whatever lay across the stem now lies along the ring; a line laid along the whole ring is a condition or a rule."),
 ("G2", "The knife and the growing.", "Strokes bow and taper at both ends; corners round; a closed shape stays straight only when it names a thing of stone."),
 ("G3", "Meaning, not sound.", "A mark is known by what it means. Its soft reading is the living word for that meaning, not the mark's old name. Wood writes what is meant."),
 ("G4", "Signs grow new signs.", "Marks join on one file (modifier inward) and grow parts: a lens for a thing of wood, a square for a thing of stone, a star for a flash, a wedge for a blow, a check for a hurt."),
 ("G5", "Time and place.", "What comes first is cut nearer the heart (a ring is an hour); who and where are files; a pause is an empty ring."),
 ("G6", "The mirror.", "The first tongue's 'not' was a mark turned to face the other way. The grain kept it as negation, and gave every symmetrical sign the entry-nick so that it has a mirror."),
 ("G7", "The two line-qualities.", "The Square and the Bough became the classifier: straight for what is of stone, curved for what is of wood."),
]

# ---------------------------------------------------------------- the course-hand, letter by letter
UPRIGHT = {"prop": "BEARER", "offset": "COURSE", "shore": "SPLIT"}
MANNER = {"stop": ("a top stone: the old letter's own laid stone", None),
          "vstop": ("the stop + the pin", "POST"), "nasal": ("the middle stone", "WITHIN"), "fric": ("the low stone", "BREATHING"),
          "vfric": ("the stop's top stone, shortened, + the fricative's low stone (built by the reform)", None),
          "approx": ("a short top stone + a free low stone", "SAIL"), "sib": ("a free top stone + a joined low stone", "BOUGH"),
          "rhot": ("a short middle stone + the pin", "FORE"), "rrhot": ("the middle stone + the pin + a free top stone", "SQUARE")}
LETTERS = [
 # (letter, place, manner, note)
 ("p", "prop", "stop", "the Bearer itself: a prop under its load (*par-, 'bear up')"),
 ("b", "prop", "vstop", ""), ("m", "prop", "nasal", "*molt-: the Breath Within gives the nasal stone, and m is its own first sound"),
 ("f", "prop", "fric", "made when Hal hw became f: hw without its free top stone"), ("v", "prop", "vfric", ""),
 ("w", "prop", "approx", "*gwemm-: the Sail gives the approximant stones, and w is its own first sound"),
 ("t", "offset", "stop", "the Course itself: a line that runs and steps (*trenn-); the hand is named for it, Garl Dhrenn"),
 ("d", "offset", "vstop", ""), ("n", "offset", "nasal", ""), ("th", "offset", "fric", ""), ("dh", "offset", "vfric", ""),
 ("s", "offset", "sib", "*sul-: the Bough gives the sibilant stones, and s is its own first sound"),
 ("l", "offset", "approx", "l shares its stones with w (both let the breath past)"),
 ("r", "offset", "rhot", "*re-il: the Fore's right arm and foot; r is its first sound. The Fore itself stays whole outside the alphabet"),
 ("rh", "offset", "rrhot", "*xreun-: the Square opened; Hal hr, its first sound (Rhyna's own root)"),
 ("k", "shore", "stop", "the Split itself (*krask-, 'crack')"), ("g", "shore", "vstop", "*gann-: the Post gives the pin, and g is its own first sound"),
 ("h", "shore", "fric", "*hoss-: the Breathing gives the low stone, and h is its own first sound"),
 ("ŋ (Hal)", "shore", "nasal", "the shore nasal; its letter died with the sound, and Seren's name keeps it (Hal SEREŊOS)"),
 ("hw (Hal)", "prop", "sib", "the lip-sibilant; living f"), ("x (Hal)", "shore", "approx", "the back approximant; living h"),
]
VOWELS = [
 ("a", "CURL", "the Curl's head laid flat as a capstone over a short pin on the left (C1, C7)"),
 ("o", "CURL", "the same, pin on the right: the Curl's own first sound, *oð-"),
 ("u", "UPON", "two short pins and a keystone raised clear of them: the Upon, *um-, its first sound"),
 ("e", "LONE", "a tall pin on the left and a low stone: the Lone Mark mirrored by the reform"),
 ("i", "LONE", "a tall pin on the right and a low stone: the Lone Mark, *itt-, its first sound"),
 ("y", "LEAN", "e's pin set leaning: made by the reform when the i-colouring gave the Hal its y"),
 ("A · O", "CURL", "a and o with the capstone broken: the reform's empty vowel, which takes the colour of its stem"),
]
MARKS_STONE = [
 ("perpend", "END", "the End's stopping bar stood on the bed (C2)"), ("wedge (pause)", "WEDGE", "the blow's base kept as a free laid stone (C1)"),
 ("gate (end of an oath)", "DOOR", "kept whole (C8)"), ("coping (end of a tale)", "DOOR + BAR", "the gate capped: a course laid over it"),
 ("sealing lintel", "BAR", "*hosk-, the lintel: a pair-name under one laid stone"), ("long-stone (Hal)", "BAR", "a short laid stone over an old long vowel"),
 ("numeral cap", "TALLY", "the tally-notch set over the letter it counts (C2, C8)"), ("the bed band", "BED", "*loð-, the mortar line: the stone-folk's roots"),
 ("the head-joint", "GAP", "the break in the bed between two word-stones"), ("softening bite (V)", "CARVE", "late: the living hand's own, the V of a cut"),
 ("nasalising bite (square)", "SQUARE", "late: a socket cut into the bed"), ("the foremark (proposed)", "FORE", "kept whole: the first builders' mark"),
]

def svg_mark(m, x0, y0, size, stroke=1.1):
    """draw one mark at (x0, y0) (top-left) in a size x size box"""
    s = size / 10.0
    def P(x, y):
        return (x0 + x * s, y0 + (10 - y) * s)
    out = []
    for pr in m["draw"]:
        t = pr[0]
        if t == "l":
            pts = " ".join("%.1f,%.1f" % P(x, y) for x, y in pr[1])
            out.append('<polyline points="%s"/>' % pts)
        elif t == "c":
            _, cx, cy, r, a0, a1 = pr
            n = 24
            pts = []
            for k in range(n + 1):
                a = math.radians(a0 + (a1 - a0) * k / n)
                pts.append(P(cx + r * math.cos(a), cy + r * math.sin(a)))
            out.append('<polyline points="%s"/>' % " ".join("%.1f,%.1f" % p for p in pts))
        elif t == "lens":
            _, cx, cy, ln, w, rot = pr
            # a vesica along the axis rot (degrees from +x); built from two arcs
            n = 20; pts = []
            half = ln / 2.0
            for side in (1, -1):
                for k in range(n + 1):
                    u = -half + ln * k / n if side == 1 else half - ln * k / n
                    v = side * (w / 2.0) * (1 - (u / half) ** 2)
                    a = math.radians(rot)
                    x = cx + u * math.cos(a) - v * math.sin(a)
                    y = cy + u * math.sin(a) + v * math.cos(a)
                    pts.append(P(x, y))
            out.append('<polygon points="%s"/>' % " ".join("%.1f,%.1f" % p for p in pts))
        elif t == "sq":
            _, cx, cy, sz = pr
            h = sz / 2.0
            pts = [P(cx - h, cy - h), P(cx + h, cy - h), P(cx + h, cy + h), P(cx - h, cy + h)]
            out.append('<polygon points="%s"/>' % " ".join("%.1f,%.1f" % p for p in pts))
        elif t == "drop":
            _, cx, cy, ln, w = pr
            n = 24; pts = []
            for k in range(n + 1):
                a = 2 * math.pi * k / n
                u = math.cos(a); v = math.sin(a)
                x = cx + (w / 2.0) * v * (1 - u) * 0.62
                y = cy + (ln / 2.0) * u
                pts.append(P(x, y))
            out.append('<polygon points="%s"/>' % " ".join("%.1f,%.1f" % p for p in pts))
        elif t == "dot":
            _, cx, cy, r = pr
            X, Y = P(cx, cy)
            out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" class="solid"/>' % (X, Y, r * s))
        elif t == "fill":
            pts = " ".join("%.1f,%.1f" % P(x, y) for x, y in pr[1])
            out.append('<polygon points="%s" class="solid"/>' % pts)
    return "\n".join(out)

def sheet(path):
    ids = list(MARKS)
    cols = 8
    cell = 118
    box = 64
    rows = (len(ids) + cols - 1) // cols
    W = cols * cell + 40
    H = rows * (cell + 30) + 90
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Georgia, serif">' % (W, H, W, H),
           '<style>:root{--ink:#2d2618;--paper:#f3ecdc;--sub:#6b5d45}@media (prefers-color-scheme: dark){:root{--ink:#eadfc6;--paper:#1c1812;--sub:#a8987a}}'
           'svg{background:var(--paper)} .m polyline,.m polygon{fill:none;stroke:var(--ink);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}'
           '.m .solid{fill:var(--ink);stroke:var(--ink)} text{fill:var(--ink)} .sub{fill:var(--sub)}</style>',
           '<text x="20" y="34" font-size="22">The first marks</text>',
           '<text x="20" y="56" font-size="13" class="sub">the sign-set of the first tongue, drawn in no hand of either people: one even stroke, no chisel-foot, no knife-taper</text>']
    for k, id_ in enumerate(ids):
        m = MARKS[id_]
        c, r = k % cols, k // cols
        x = 20 + c * cell; y = 80 + r * (cell + 30)
        out.append('<g class="m">%s</g>' % svg_mark(m, x + (cell - box) / 2 - 6, y, box))
        out.append('<text x="%d" y="%d" font-size="12.5" text-anchor="middle">%s</text>' % (x + cell / 2 - 6, y + box + 22, m["name"]))
        out.append('<text x="%d" y="%d" font-size="11.5" text-anchor="middle" font-style="italic" class="sub">*%s</text>' % (x + cell / 2 - 6, y + box + 38, m["word"]))
    out.append('</svg>')
    open(path, "w").write("\n".join(out))

if __name__ == "__main__":
    sheet("first_marks.svg")
    json.dump(MARKS, open("first_marks.json", "w"), ensure_ascii=False, indent=1)
    print(len(MARKS), "marks")

# ---------------------------------------------------------------- the grain, sign by sign
# sign: (marks, laws, how)
GRAIN = {
 # the eleven that open a carving
 "WAVE": (["CURL"], "G1 G2", "the Curl on its file; its head bows over and breaks forward, as a crest"),
 "LONE": (["LONE"], "G1 G2", "kept: a long cut and a short one set aside"),
 "BARB": (["FORE"], "G1", "kept whole: the Fore, its bar laid along the ring"),
 "SPARK": (["STEM", "STAR"], "G4", "a cut that ends in the Star"),
 "SQUARE": (["SQUARE"], "G7", "kept whole; the one straight closed shape among the roots"),
 "MOUTHS": (["MOUTH", "MOUTH"], "G2 G4 · hollow", "two mouths grown to two parallel cuts, one cut hollow: one voice is a seeming"),
 "STERN": (["CURL"], "G4", "the Curl hooked back on itself and run home beside its own stroke"),
 "BREATH": (["GAP"], "G1", "the Gap on its file: two cuts and the between"),
 "KNOT": (["KNOT"], "G1 G2", "kept; the rings bow round it as grain flows round a branch"),
 "SMOOTH": (["CARVE"], "G2 · smoothed", "a bowed cut filled and smoothed: felt, not seen"),
 "BURN": (["SCAR"], "G2", "the Scar as a charred wedge, lipped with callus where the wood grew back"),
 # acts
 "GO": (["STEM"], "G1 G3", "the Stem on a file: a cut from the heart outward is a going"),
 "STRIKE": (["STEM", "WEDGE"], "G4", "a cut ending in the Wedge: the blow landing"),
 "BREAK": (["SPLIT"], "G2", "the Split: the head opens"),
 "WOUND": (["SPLIT"], "G2", "the Split grown as a check, widest toward the bark"),
 "TURN": (["TURN"], "G2", "kept: a cut with a kink"),
 "HOLD": (["CUP"], "G1", "kept: the Cup cupped round the file"),
 "OPEN": (["CUP"], "G4", "the Cup turned outward"),
 "CLOSE": (["CUP", "BAR"], "G4", "the Cup with a bar across its head"),
 "MOUTH": (["MOUTH"], "G2", "kept: an open lens, joined at the foot"),
 "FALL": (["CURL"], "G4", "the Curl at the foot: the head points down into the wood"),
 "RISE": (["STEM", "BOUGH"], "G4", "a cut ending in a bud (a small Bough)"),
 "GROW": (["SPROUT"], "G2", "kept: leaves springing alternately up the stem"),
 "LIVE": (["BREATHING"], "G2 G3", "the Breathing: one leaf on a short stalk; breath is life"),
 "DYING": (["FADE"], "G2", "kept: a cut breaking into shorter and shorter pieces"),
 "KNEEL": (["KNEEL"], "G2", "kept: the fold that comes to rest on the ground"),
 "GIFT": (["GIFT"], "G1", "kept: a lens set down on a bar"),
 "BOND": (["BOND"], "G2", "kept: two cuts that bow in and grow into one"),
 "STOP": (["END"], "G1", "the End: a cut against a bar that lies along the ring"),
 "MEND": (["WHOLE"], "G1", "kept: a line made whole with a small stone in its gap"),
 "ROT": (["FADE"], "G4", "the Fade crumbled into five pieces, offset"),
 "AXE": (["EDGE2"], "G2", "the Blade: a haft running the whole space, the blade on its clockwise side"),
 "CARVE": (["CARVE"], "G1 G2", "kept: the V of a knife-cut"),
 "LEAN": (["LEAN"], "G1", "kept: one cut set obliquely across the ring"),
 "BEND": (["BOUGH"], "G2", "the Bough as a single stroke, deeply bowed: bending as a bough bends"),
 "BENEATH": (["UPON"], "G2 G3", "the Upon read from below: a bar at the head, a cut under it that does not reach it"),
 # things
 "HULL": (["BOUGH"], "G1", "kept: the Bough is a hull"),
 "BEARER": (["BEARER", "BOUGH"], "G2 G4", "the Bearer's load grown round the bearing stroke: a hull with a cut inside"),
 "THIN": (["BOUGH"], "G4", "a narrow Bough"),
 "SPENT": (["BOUGH", "SPLIT"], "G4", "a Bough split by a check"),
 "GREAT": (["BOUGH", "BAR"], "G4", "a broad Bough with a rib across it"),
 "EYE": (["EYE"], "G1", "kept: a short lens with tails"),
 "HUNTER": (["BOUGH", "STAR"], "G4", "a Bough with a star at its fore tip"),
 "SWIFT": (["BOUGH", "COURSE", "COURSE"], "G4", "a short Bough with two running lines behind it: the wake"),
 "BREAKER": (["BOUGH", "SQUARE"], "G4", "a Bough with a small Square at its fore tip"),
 "RAM": (["BOUGH", "WEDGE"], "G4", "a Bough with a Wedge at its fore tip"),
 "ROOT": (["STEM", "ROOTS"], "G4", "a cut ending in the Roots, reaching forward"),
 "SEED": (["SEED"], "G2", "kept: a small lens with two swept wings"),
 "TREE": (["STEM", "BOUGH", "BOUGH"], "G4", "the Stem with two boughs at two heights: *tolm-, the standing thing, is thael, the tree"),
 "PILLAR": (["STEM", "BOUGH", "BOUGH"], "G4", "the tree with its trunk cut solid"),
 "SAPLING": (["STEM", "BOUGH", "BOUGH"], "G4", "a small tree in the outer half of its space"),
 "HEART": (["BOUGH"], "G4", "a small Bough cut solid"),
 "US": (["ROOTS", "STEM", "BOUGH"], "G4 G7", "one who stands rooted, crowned with a Bough: of wood"),
 "STONEFOLK": (["ROOTS", "STEM", "SQUARE"], "G4 G7", "one who stands rooted, crowned with a Square: of stone"),
 "HOME": (["CURL"], "G4", "the Curl closed round on itself: the Turned Stern made whole"),
 "HOMESTONE": (["CURL", "SQUARE"], "G4 G7", "Home drawn straight and square: a home of stone"),
 "SHORE": (["BAR", "CURL"], "G1 G4", "a bar along the ring with a small Curl at its end"),
 "ROAD": (["COURSE", "COURSE"], "G1 G4", "two running lines: a lane"),
 "EDGE": (["EDGE"], "G1", "the Rim, its arc following the ring at the head of its space"),
 "GUN": (["SQUARE", "STAR"], "G4", "a Square with a Star at its head: a speaking stone"),
 "CASTLE": (["SQUARE", "SQUARE"], "G4", "a large Square with a small one behind it, joined"),
 "DOOR": (["DOOR"], "G2", "kept whole; its posts battered in as old jambs lean"),
 "FLASH": (["STAR"], "G1", "kept: the Star alone"),
 "BLOOD": (["DROP"], "G1", "kept: a drop, point toward the heart"),
 "GRIEF": (["SPLIT"], "G4", "the Split as a check, its head closed over by callus: a wound the wood has grown around"),
 "SAIL": (["SAIL"], "G2", "kept: a mast under a cloth bellied by the wind"),
 "HAND": (["HAND"], "G1", "kept: a stem ending in an open palm"),
 "TIDE": (["EDGE", "SPROUT"], "G4", "an arc along the ring with a shoot rising from it"),
 "DEEP": (["BED"], "G1", "the Bed: a cut standing on a floor-bar"),
 "AELTHAR": (["DROP", "DROP", "BOND"], "G4", "two Drops whose stems grow together: two bloods made one"),
}
BANDS = {
 "MIST": (["WITHIN"], "G1", "the Breath Within laid along the ring: a pale band through its middle"),
 "WHITE": (["PALE"], "G1", "the Pale laid along the ring: a frost ring of short ticks"),
 "DREAD": (["SPLIT"], "G1", "the Split laid along the ring: a ring shake"),
 "WATER": (["COURSE"], "G1", "the Course laid along the ring: a single waving hairline"),
 "STILL": (["STILL"], "G1", "kept: two level lines, concentric"),
 "DARK": (["FADE"], "G1", "the Fade laid along the ring: a stain"),
}
DEVICES = [
 ("file", "the first hand cut its marks round a standing thing (*tolm-); where a mark stood round the trunk said who and where", "G1 G5"),
 ("ring", "the tree grew over the marks: what was cut first lies nearest the heart; a ring is an hour", "G5"),
 ("span", "a Stem stretched across rings: until", "G5"),
 ("empty ring", "a pause in the telling became a pause in time: a morrow passes", "G5"),
 ("ligature", "two marks on one file, modifier inward, as in the first tongue's own compounds", "G4"),
 ("plural ×3", "the Three: three copies abreast", "G4"),
 ("pair", "the Bond: two from one foot", "G4"),
 ("lean", "the Lean", "G1"),
 ("twin", "the same mark on the opposite file: likewise, on the other side", "G5"),
 ("negation", "the first tongue's 'not' was a mark turned to face the other way", "G6"),
 ("entry-nick", "added so that every symmetrical sign has a mirror", "G6"),
 ("hollow", "the first tongue's 'seeming' was a mark cut in outline only (*iθ-, eith)", "—"),
 ("smoothed", "the Cut filled and smoothed", "G2"),
 ("count, ordinal", "the Tally: notches on one side count, on the other side order", "G4"),
 ("five", "the Hand after a thing", "G4"),
 ("causative", "a small Wedge at the foot: the push that makes it do", "G4"),
 ("half size", "a mark cut small: the lesser", "G4"),
 ("question", "the first tongue's asking mark was a stroke left unfinished; it runs into the ring line and stops", "G2"),
 ("ray", "the Course along one file: the same one", "G1"),
 ("memory ray", "the Course running back to the heart and ending in the Roots: carried back through the roots", "G4 G5"),
 ("held at the root", "the Cup cupped round the pith itself", "G4"),
 ("ties", "the Bond thinned to a hairline: this one to that one; when this, then that", "G4"),
 ("fork", "the Split: if, and if not", "G4"),
 ("chain", "a fork ending in an older root, cut small", "G4"),
 ("band-rule", "the End laid along the whole ring: a movement ends", "G1"),
 ("war-pith", "the Square at the heart: the council's carving", "G7"),
 ("seal", "the Cup (HOLD) in the bark: this is held in the grain", "G4"),
 ("grain-arc", "the grain line itself, *waʔl- (vael): a short hairline along the ring, in names only", "G1"),
 ("included bark, graft, joined piths, pale ring", "not marks but growth: what a tree does, which the grain reads", "—"),
]
