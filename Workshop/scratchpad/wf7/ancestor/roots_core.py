"""The roots of the first tongue that the two living tongues continue.

R(key, root, meaning, field, o=[...], s=[...], note, stem)
  o entry: (ancestral word with its Hal ending, living Orrowen, gloss, {opts})
  s entry: (ancestral stem, living Seilrhass, gloss, {opts})
  opts:  hal=expected Hal form · small=True (a small word: its -n falls)
         compound=True (a lexicalised compound: the seam wears) · keep_long_a=False
         keep_wr=True · eldest=expected Eldest form · relic_aer=True · irr="note"
  stem:  the plain stem, used to predict the reflex in a tongue that did not keep the root.
Fields: stone, bond, hearth, war, sea, sky, body, speech, acts, quality, small, number, affix, name
"""

ROOTS = []
def R(key, root, mean, field, o=(), s=(), note="", stem=None):
    ROOTS.append(dict(key=key, root=root, mean=mean, field=field, o=list(o), s=list(s), note=note,
                      stem=stem))

# ------------------------------------------------------------------ STONE, WOOD, BUILDING
R("TOL", "tol- / tal-", "rise, stand up tall; (o-grade) a standing thing, a stone set up or a trunk", "stone",
  o=[("tolm-o-s", "tolm", "a stone; a letter of the course-hand", dict(hal="tolmos")),
     ("tal-d-o-s", "tald", "rise, stand up (v.)", {}),
     ("tal-d-uʔ", "taldow", "a tower, a high place", dict(hal="taldū"))],
  s=[("tolm-i", "thael", "a tree; a living trunk; to rise, to stand", dict(eldest="taele")),
     ("tal-o", "thal", "the neck, where life goes up into thought", {})],
  note="The one word for the standing thing split between the peoples: the stone-folk kept it for stone, the wood-folk for the tree. The mystaeri spec's analysis of thael as thae + *-l is replaced.")
R("XAL", "xal-", "the living rock, what lies under everything", "stone",
  o=[("xal-o-s", "hal", "bedrock, the living rock of the ridge", dict(hal="xalos")),
     ("xal-d-o-s", "hald", "a wall ('rock made to stand')", dict(hal="xaldos"))], stem="xal-o")
R("LODH", "loð-", "set in a wet bed; bind (as mortar binds)", "stone",
  o=[("lodh-o-s", "lodh", "mortar; the mortar line; the bond", dict(hal="lodhos"))], stem="lodh-o")
R("TRENN", "trenn-", "a running line: a course of stones, a line of writing, a stream", "stone",
  o=[("trenn-o-s", "trenn", "a course of stones; a line of writing; a tale laid in one night", dict(hal="trennos"))],
  s=[("trenn-o", "thenn", "water; the sea", dict(eldest="tenne"))],
  note="A course of stone and a course of water: the stone-folk laid tales in it, the wood-folk heard the sea in it.")
R("KADH", "kað-", "set down in its place, lay", "stone",
  o=[("kadh-o-s", "cadh", "lay (a stone, a course, a tale)", {})], stem="kadh-o")
R("STON", "ston-", "stand firm, hold one's place; the standing core of a thing", "stone",
  o=[("ston-o-s", "ston", "stand (of a wall), make stand, hold firm", dict(hal="stonos"))],
  s=[("ston-i", "saen", "heartwood; the heart of a tree; the middle", {})],
  note="The Stonwryt ('the standing cutting') and the Saenvael ('heart-grain') are one word at the root: the vow at the core of a wall, the order at the core of a hull.")
R("GAL", "gal-", "set up, raise; (of a thing) stand made, be", "stone",
  o=[("gal-d-o-s", "gald", "build, raise a work", {}),
     ("gal-o-s", "gal", "(old) was: the suppletive past of doss, re yal-", {})], stem="gal-o")
R("KLENN", "klenn-", "fresh, not yet worn", "stone",
  o=[("klenn-i-s", "clenn", "new; make new, mend", {})], stem="klenn-i")
R("STANN", "stann-", "cut out of its bed", "stone",
  o=[("stann-o-s", "stann", "quarry, cut stone from the bed", {}),
     ("stann-ard-o-s", "stannard", "Stannard, 'quarrier' (a name)", dict(hal="stannardos", name=True))], stem="stann-o")
R("BRASK", "brask-", "a biting edge", "stone",
  o=[("brask-i-s", "bresk", "a chisel", dict(hal="breskis"))], stem="brask-i")
R("DRUNN", "drunn-", "a heavy blow", "stone",
  o=[("drunn-o-s", "drunn", "a mallet, a hammer", dict(hal="drunnos"))], stem="drunn-o")
R("GANN", "gann-", "a post, an upright; (dual) the two posts", "stone",
  o=[("gann-o-s", "gann", "a post, an upright", dict(hal="gannos")),
     ("gann-aʔ", "ganna", "a gate ('the two posts')", dict(hal="gannā"))], stem="gann-o")
R("HOSK", "hosk-", "a stone laid across; to cap", "stone",
  o=[("hosk-o-s", "hosk", "a lintel; a capstone; lay the lintel, seal", dict(hal="hoskos"))], stem="hosk-o")
R("GORN", "gorn-", "a turn of a wall, a corner", "stone",
  o=[("gorn-o-s", "gorn", "a corner, a quoin", {})], stem="gorn-o")
R("KETH", "keθ-", "hold in the hand, keep", "stone",
  o=[("keth-i-s", "keth", "hold, keep; (of the wood) know", {}),
     ("keth-uʔ", "kethow", "a keep, a hold", dict(hal="kethū"))], stem="keth-i")
R("TROSK", "trosk-", "split, cleave; a split", "stone",
  o=[("trosk-i-s", "tresk", "a cleft, a split; cleave, rive, tear", dict(hal="treskis"))],
  s=[("trosk-i", "thaess", "to split; a wound; to be struck", {})],
  note="The Riven Stone and the Torn Cloak (O tresk) and the wound of the proverb (S thaess) are one word.")
R("LAST", "last-", "a roofed room", "stone",
  o=[("last-i-s", "lest", "a house", dict(hal="lestis"))], stem="last-i")
R("KUMM", "kumm-", "a sheltered hollow", "stone",
  o=[("kumm-o-s", "cumm", "a haven: any walled place of shelter", dict(hal="cummos"))], stem="kumm-o")
R("STELL", "stell-", "a heap of stones", "stone",
  o=[("stell-i-s", "stell", "a cairn", dict(hal="stellis"))], stem="stell-i")
R("PELL", "pell-", "a tall point", "stone",
  o=[("pell-i-s", "pell", "a spire, a tall point", dict(hal="pellis")),
     ("pell-uʔ", "pellow", "Pellow, 'of the spire' (a name)", dict(hal="pellū", name=True))], stem="pell-i")
R("WRUT", "wrut-", "cut into; a cut made to last", "stone",
  o=[("wrut-i-s", "ryt", "a cut vow, an oath; an inscription; cut letters, write, swear", dict(hal="wrytis"))], stem="wrut-i")
R("PRASS", "prass-", "one who knows the work through", "stone",
  o=[("prass-o-s", "prass", "a master of the craft", dict(hal="prassos"))], stem="prass-o")

# ------------------------------------------------------------------ FAITH, BOND, KIN
R("HEMM", "hemm-", "old, of many years", "bond",
  o=[("hemm-o-s", "hemm", "old; Elder", dict(hal="hemmos")),
     ("hemm-aʔ", "hemma", "Elderess", dict(hal="hemmā"))], stem="hemm-o")
R("MARDH", "marð-", "the Maker; the one who is knelt to", "bond",
  o=[("mardh-o-s", "mardh", "God (used of nothing else)", dict(hal="mardhos"))], stem="mardh-o",
  note="The wood kept no word from this root. Its grain names Him by an act: 'the one they kneel to' (KNEEL).")
R("AMM", "amm-", "lift the voice to one above: to call upon, to teach", "bond",
  o=[("amm-el-i-s", "ammel", "pray", {}), ("amm-ad-o-s", "ammad", "teach", {})], stem="amm-o")
R("TAW", "taw-", "sprout, grow", "bond",
  o=[("taw-i-s", "tev", "a child", dict(hal="tevis"))],
  s=[("taw-i", "thae", "tide; a growing; to grow", {})],
  note="A child is a sprouting; a Tide is a growing. tevow (Hal tevū) and tevel are built in the Hal on tev-, after the i-colouring.")
R("WOLL", "woll-", "a calling, a name", "bond",
  o=[("woll-o-s", "voll", "a name", dict(hal="vollos"))], stem="woll-o")
R("TAN", "tann- / tunn-", "shut in; (u-grade) shut round, whole", "bond",
  o=[("tunn-o-s", "tunn", "whole, complete", {})],
  s=[("tann-i", "thann", "to close; closed", {})])
R("GREST", "grest-", "a burning smart, a hurt", "bond",
  o=[("grest-o-s", "grest", "harm, hurt", dict(hal="grestos"))],
  s=[("grest-i", "rhes", "anger; hot", {})],
  note="Harm (the stone's word) and anger (the wood's) are the same heat.")
R("PAR", "par-", "bear up, hold up; keep safe", "bond",
  o=[("par-o-s", "par", "guard, protect; a watch", {}),
     ("par-d-o-s", "pard", "a warden, a keeper", dict(hal="pardos")),
     ("xal+par-d-o-s", "halvard", "Halvard, 'bedrock-warden' (a name)", dict(hal="xalpardos", compound=True, name=True))],
  s=[("par", "var", "to bear, to carry", {}),
     ("par-ane", "varen", "a bearer; a laden hull", dict(irr="keeps the old agent ending *-ane"))],
  note="Halvard's -vard and the Aelvaren's -varen are one root.")
R("ODH", "oð-", "the rim where one stops and gathers: the fireside, the waterside", "bond",
  o=[("odh-o-s", "odh", "a hearth", dict(hal="odhos")),
     ("odh-aʔ", "odha", "a mother ('she of the hearth')", dict(hal="odhā"))],
  s=[("odh-i", "aeth", "a shore; the edge where water ends", {})],
  note="The first word the wood ever gave Halyna, shore, is the hearth's own word in the first tongue.")
R("THALD", "θald-", "those of one hearth", "bond",
  o=[("thald-i-s", "theld", "a family, a household", dict(hal="theldis"))], stem="thald-i")
R("WAQR", "waʔr-", "stillness; a still place", "bond",
  o=[("waʔr-n-o-s", "varn", "home", dict(hal="varnos"))],
  s=[("waʔr-ai", "vaere", "still water; its face; a reflection; (postp.) like, as", dict(irr="the final -e is the long e of the old *-ai, which did not fall"))],
  note="The Title's 'home' and the Stone's 'peace' (STILL) are one word in the first tongue.")
R("GADH", "gað-", "a father", "bond",
  o=[("gadh-i-s", "gedh", "a father", dict(hal="gedhis"))], stem="gadh-i")
R("ULD", "uld-", "grown", "bond",
  o=[("uld-o-s", "uld", "a man; a grown person", dict(hal="uldos"))], stem="uld-o")
R("ESS", "ess-", "a woman", "bond",
  o=[("ess-aʔ", "essa", "a woman", dict(hal="essā"))], stem="ess-aʔ")
R("LUNT", "lunt-", "those of one speech", "bond",
  o=[("lunt-o-s", "lunt", "a people, a nation", dict(hal="luntos"))], stem="lunt-o")
R("ORR", "orr-", "go along; the edge one goes along", "bond",
  o=[("orr-o-s", "orr", "go, walk", {}), ("orr-uʔ", "orrow", "the Shore; the Shorelands", dict(hal="orrū"))], stem="orr-o")
R("ARR", "arr-aʔ", "(dual) the two at a threshold, the guest and the host", "bond",
  o=[("arr-aʔ", "arra", "a guest", dict(hal="arrā", irr="keeps the dual -a: a guest is half of a pair"))], stem="arr-aʔ")
R("GEBB", "gebb-", "a leaf that swings; a door", "bond",
  o=[("gebb-i-s", "gebb", "a door", dict(hal="gebbis"))], stem="gebb-i")
R("LUMM", "lumm-", "bow down", "bond",
  o=[("lumm-o-s", "lumm", "kneel", {})], stem="lumm-o")
R("WAQL", "waʔl-", "the inward bent of a thing: its grain, what it leans to", "bond",
  o=[("waʔl-o-s", "vall", "love", {})],
  s=[("waʔl-i", "vael", "grain; temper; the carved knowing", {})],
  note="Love is the heart's grain.")
R("OSK", "osk-", "rest one's weight on", "bond",
  o=[("osk-o-s", "osk", "trust (v. and n.)", {})], stem="osk-o")
R("TESK", "tesk-", "a layer, a laying-down", "bond",
  o=[("tesk-i-s", "tesk", "a generation", dict(hal="teskis"))], stem="tesk-i")
R("SWE", "swe- / swo-", "one's own; one alone, single", "bond",
  o=[("swo-st-o-s", "sost", "self, very", {}),
     ("swe-reŋ-o-s", "seren", "Seren, 'a single sorrow that overcomes' (a name)", dict(hal="sereŋos", name=True))],
  stem="swe-o", note="See REŊ. The spec's Hal Serenos becomes SEREŊOS.")
R("RENG", "reŋ-", "a sorrow that is carried and does not break the one who carries it; a grief that overcomes", "bond",
  o=[], s=[], stem="reŋ-o", note="Kept only in Seren's name.")

# ------------------------------------------------------------------ THE WALL, WAR
R("KREN", "krenn- / krann-", "weighty; the one who bears the weight, the head", "war",
  o=[("krenn-o-s", "crenn", "a captain; the Captain", dict(hal="crennos"))],
  s=[("krann-i", "rhann", "heavy, great", {})])
R("HESP", "hesp-", "a long blade", "war", o=[("hesp-i-s", "hesp", "a sword", dict(hal="hespis"))], stem="hesp-i")
R("KEST", "kest-", "a band that goes together", "war", o=[("kest-i-s", "kest", "a company of soldiers", dict(hal="kestis"))], stem="kest-i")
R("BRAMM", "bramm-", "a roar; to roar", "war", o=[("bramm-o-s", "bramm", "a gun ('the roarer')", dict(hal="brammos"))], stem="bramm-o")
R("HASK", "hask-", "run", "war", o=[("hask-o-s", "hask", "run", {})], stem="hask-o")
R("GOMM", "gomm-", "a horn", "war", o=[("gomm-o-s", "gomm", "a horn", dict(hal="gommos"))], stem="gomm-o")
R("KARM", "karm-", "cry out", "war", o=[("karm-o-s", "carm", "a call, a cry; cry out, call", {})], stem="karm-o")
R("PEDH", "peð-", "a thing thrown", "war", o=[("pedh-i-s", "pedh", "a shot: what a gun throws", dict(hal="pedhis"))], stem="pedh-i")
R("TRUN", "trun-", "the ground under one", "war", o=[("trun-o-s", "trun", "ground; the water a battery watches", dict(hal="trunos"))], stem="trun-o")
R("MARR", "marr-", "shift over", "war", o=[("marr-o-s", "marr", "shift, move to another place", {})], stem="marr-o")
R("KUL", "kul-", "leave off; turn from one thing", "war",
  o=[("kul-i-s", "kyl", "change", {})],
  s=[("kul-i", "rheil", "to stop, to cease", {})],
  note="The Captain's 'Change your shot' and the Guest's plea 'Stop' are one verb.")
R("LUSK", "lusk-", "let go", "war", o=[("lusk-o-s", "lusk", "loose, let go, set free", {})], stem="lusk-o")
R("BOSK", "bosk-", "fall upon", "war", o=[("bosk-o-s", "bosk", "attack", {})], stem="bosk-o")
R("HURR", "hurr-", "strike down", "war", o=[("hurr-o-s", "hurr", "kill", {})], stem="hurr-o")
R("GORR", "gorr-", "fight", "war", o=[("gorr-o-s", "gorr", "fight", {})], stem="gorr-o")
R("KOFF", "koff-", "a wrap", "war", o=[("koff-o-s", "covv", "a cloak", dict(hal="covvos"))], stem="koff-o")
R("SKETH", "skeθ-", "hew, cut into wood", "war",
  o=[("sketh-i-s", "sceth", "a ship, a hull (a trunk hewn out)", dict(hal="scethis"))],
  s=[("sketh-i", "seth", "a carving; an order cut in living wood; to carve", {})],
  note="The stone-folk's word for a ship is the wood-folk's word for a carving: the Sethvaren is, at the root, 'the hull that bears the hewing'.")
R("GWEMM", "gwemm-", "a cloth that fills", "war", o=[("gwemm-i-s", "wemm", "a sail", dict(hal="wemmis"))], stem="gwemm-i")

# ------------------------------------------------------------------ SEA, LAND, WEATHER, TIME
R("GWADH", "gwað-", "the great water", "sea", o=[("gwadh-o-s", "wadh", "the sea", dict(hal="wadhos"))], stem="gwadh-o")
R("MUS", "mus-", "the dim light; fog-light", "sea",
  o=[("mus-t-i-s", "myst", "sea-fog; the grey; (adj.) grey", dict(hal="mystis"))],
  s=[("mus-i", "neis", "soft light; to shine softly", {})],
  note="The Rivenmen's grey (myst, in Mystaeri and the Mystlands) is the wood's between-light.")
R("MOSK", "mosk-", "a tree and its wood", "sea", o=[("mosk-i-s", "mesk", "a tree; wood", dict(hal="meskis"))], stem="mosk-i")
R("LURR", "lurr-", "thick-grown", "sea", o=[("lurr-o-s", "lurr", "a forest", dict(hal="lurros"))], stem="lurr-o")
R("HALF", "half-", "the upper air", "sky", o=[("half-i-s", "helv", "the sky, the upper air", dict(hal="helvis"))], stem="half-i")
R("HULL", "hull-", "a swelling of water", "sea", o=[("hull-i-s", "hyll", "a tide", dict(hal="hyllis"))], stem="hull-i")
R("XRULL", "xrull-", "a rushing water", "sea", o=[("xrull-o-s", "rhull", "a river", dict(hal="hrullos"))], stem="xrull-o")
R("SEDH", "seð-", "soft wet ground", "sea", o=[("sedh-i-s", "sedh", "a fen", dict(hal="sedhis"))], stem="sedh-i")
R("NALL", "nall-", "a small land in water", "sea", o=[("nall-i-s", "nell", "an islet", dict(hal="nellis"))], stem="nall-i")
R("TAF", "taf-", "come to land", "sea",
  o=[("taf-o-s", "tav", "come ashore, land a boat", {}), ("taf-uʔ", "tavow", "a harbour, a landing", dict(hal="tavū"))], stem="taf-o")
R("SORTH", "sorθ-", "a back of land", "sea", o=[("sorth-o-s", "sorth", "a ridge", dict(hal="sorthos"))], stem="sorth-o")
R("BRUNN", "brunn-", "a great height of land", "sea", o=[("brunn-o-s", "brunn", "a mountain", dict(hal="brunnos"))], stem="brunn-o")
R("GRULL", "grull-", "grit", "sea", o=[("grull-o-s", "grull", "sand", dict(hal="grullos"))], stem="grull-o")
R("SIRR", "sirr-", "a clear hard thing", "sea", o=[("sirr-i-s", "sirr", "glass", dict(hal="sirris"))], stem="sirr-i")
R("KREST", "krest-", "hard water, ice", "sea", o=[("krest-i-s", "crest", "ice", dict(hal="crestis"))], stem="krest-i")
R("XWRE", "xwre-", "rime, frost", "sky",
  o=[("xwren-n-o-s", "frenn", "frost, rime", dict(hal="hwrennos"))],
  s=[("xwrel-i", "rhel", "frost; to cool", {})],
  note="A root of the cold. The stone built it with *-n-, the wood with *-l-.")
R("SULF", "sulf-", "snow", "sky", o=[("sulf-o-s", "sulv", "snow; (adj.) white", dict(hal="sulvos"))], stem="sulf-o")
R("GREM", "grem-", "the hard season", "sky", o=[("grem-i-s", "grem", "winter", dict(hal="gremis"))], stem="grem-i")
R("FORR", "forr-", "fire", "sky", o=[("forr-o-s", "vorr", "fire", dict(hal="vorros"))], stem="forr-o")
R("ORL", "orl-", "the light of one day", "sky", o=[("orl-o-s", "orl", "a day", dict(hal="orlos"))], stem="orl-o")
R("FEQ", "feʔ-", "fade, go dark", "sky",
  o=[("feʔs-i-s", "vess", "a night", dict(hal="vessis"))],
  s=[("feʔs-i", "veas", "to die; dying; death", {}),
     ("feʔth-i", "veath", "night; the dark", {})],
  note="Chiasmus with SENN: the stone's night is the wood's dying, and the stone's dying is the wood's 'beneath'.")
R("KLEM", "klem-", "a stroke of time", "sky", o=[("klem-i-s", "clem", "an hour", dict(hal="clemis"))], stem="klem-i")
R("SURR", "surr-", "a turn of the seasons", "sky", o=[("surr-o-s", "surr", "a year", dict(hal="surros"))], stem="surr-o")
R("KAMM", "kamm-", "come together", "sky", o=[("kamm-i-s", "cemm", "meet; a meeting", {})], stem="kamm-i")

# ------------------------------------------------------------------ BODY, LIFE, FEELING
R("GARL", "garl-", "a hand", "body", o=[("garl-o-s", "garl", "a hand; a hand of writing", dict(hal="garlos"))], stem="garl-o")
R("MOLT", "molt-", "the breath within; the living middle", "body",
  o=[("molt-o-s", "molt", "a heart", dict(hal="moltos"))],
  s=[("molt-o", "nael", "mist; the veil; the breath of the trees; the sky it made", {})],
  note="What the stone-folk call the heart, the wood-folk call the breath. Naelear, 'those of the breath', is in the first tongue 'those of the heart'.")
R("HOSS", "hoss-", "breath going out", "body", o=[("hoss-o-s", "hoss", "breath", dict(hal="hossos"))], stem="hoss-o")
R("LORR", "lorr-", "red blood", "body", o=[("lorr-o-s", "lorr", "blood; (adj.) crimson", dict(hal="lorros"))], stem="lorr-o")
R("SENN", "senn-", "down, below; go down (as a fire in peace, as the sun)", "body",
  o=[("senn-i-s", "senn", "die: go out, as a fire in peace", {})],
  s=[("senn-i", "senn", "beneath, under; the deep below", dict(eldest="senne"))])
R("HESS", "hess-", "halt, stay", "body", o=[("hess-i-s", "hess", "stop", {})], stem="hess-i")
R("LOMM", "lomm-", "the weight of a loss", "body", o=[("lomm-o-s", "lomm", "grief", dict(hal="lommos"))], stem="lomm-o")
R("SOL", "sol- / soʔl-", "lie still; (catch-grade) the deep rest", "body",
  o=[("sol-o-s", "sol", "rest, lie still", {}), ("soʔl-an-o-s", "sollan", "peace ('the rest after the work')", dict(hal="sollanos"))], stem="sol-o")
R("LUNN", "lunn-", "an open space, room to move", "body", o=[("lunn-o-s", "lunn", "freedom", dict(hal="lunnos"))], stem="lunn-o")

# ------------------------------------------------------------------ SPEECH, WRITING, MEMORY
R("TUM", "tum-", "hold, keep (in the hand and in the mind)", "speech",
  o=[("tum-o-s", "tum", "remember", {}), ("tum-ol-a", "tumol", "remembering; memory", dict(hal="tumola"))],
  s=[("tum-i", "thein", "to hold; to know by touch; a knowing", {})],
  note="The hearth's yes, Tumar 'we remember', is in the first tongue 'we hold'. The Knowing (theinas) is the same holding.")
R("BRO", "bro- / bra- / bre-", "utter", "speech",
  o=[("brod-o-s", "brod", "a word", dict(hal="brodos")), ("brodh-o-s", "brodh", "put into words, tell, speak", {}),
     ("brenn-o-s", "brenn", "Brenn: a name. Names are names; by the laws alone it would be 'mouth'", dict(name=True))],
  s=[("brant-i", "ranth", "a word (a spoken thing, which can break)", {}),
     ("brenn-i", "renn", "a mouth; to speak, to sound aloud", {})])
R("WESK", "wesk-", "look at closely", "speech", o=[("wesk-i-s", "vesk", "see; read (letters, or a cradle)", {})], stem="wesk-i")
R("XWLE", "xwle-", "a thin sheet: a leaf", "speech",
  o=[("xwlen-naʔ", "flenn", "a leaf of a book or of slate; a sheet", dict(hal="hwlennā", keep_long_a=False,
      irr="the -ā fell, because it was not the dual or the feminine but a stem vowel"))],
  s=[("xwlel-i", "lel", "a leaf", {})])
R("LUTH", "luθ-", "a dark wetness", "speech", o=[("luth-o-s", "luth", "ink", dict(hal="luthos"))], stem="luth-o")
R("BRANTH", "branθ-", "an ember", "speech", o=[("branth-i-s", "brenth", "coal", dict(hal="brenthis"))], stem="branth-i")
R("FELL", "fell-", "a song", "speech", o=[("fell-i-s", "vell", "a song", dict(hal="vellis"))], stem="fell-i")
R("SESK", "sesk-", "know (a thing that is so)", "speech", o=[("sesk-i-s", "sesk", "know a fact", {})], stem="sesk-i")
R("NUDH", "nuð-", "count", "speech", o=[("nudh-i-s", "nydh", "count", {})], stem="nudh-i")
R("KAIL", "kail-", "a notch cut to keep a count", "speech",
  o=[("kail-o-s", "kael", "a tally-notch; Kael (a name)", dict(hal="kēlos"))], stem="kail-o")
R("PESS", "pess-", "ask", "speech", o=[("pess-i-s", "pess", "ask", {})], stem="pess-i")
R("TESS", "tess-", "give back an answer; stand for", "speech",
  o=[("tess-i-s", "tess", "answer; stand surety for", {}), ("tess-ana", "tessen", "we two answer (1du)", dict(hal="tessana", harm=True))], stem="tess-i")

# ------------------------------------------------------------------ OTHER VERBS
R("DOSS", "doss-", "be (in a place, in a state)", "acts", o=[("doss-o-s", "doss", "be (state, place)", {})], stem="doss-o")
R("EL", "el- / egw-", "be such; (egw-) was", "acts",
  o=[("el-i-s", "el", "is (the copula)", dict(hal="elis")), ("egw-as", "ew", "was", {})], stem="el-i",
  note="nel 'is not' and new 'was not' are the Hal's own contractions of na + el, na + ew.")
R("DARR", "darr-", "come near", "acts", o=[("darr-o-s", "darr", "come", {})], stem="darr-o")
R("HUNN", "hunn-", "hear", "acts", o=[("hunn-o-s", "hunn", "hear", {})], stem="hunn-o")
R("HABB", "habb-", "hold out, give", "acts", o=[("habb-i-s", "hebb", "give", {})], stem="habb-i")
R("TOFF", "toff-", "stay where one is", "acts", o=[("toff-o-s", "tovv", "wait", {})], stem="toff-o")
R("OMM", "omm-", "drop", "acts", o=[("omm-o-s", "omm", "fall", {})], stem="omm-o")
R("KRASK", "krask-", "crack, break", "acts",
  o=[("krask-i-s", "cresk", "break", {})],
  s=[("krask-i", "rhass", "storm; thunder; a crack; to crack, to break", {})],
  note="Seilrhass, 'bough-thunder', is at the root 'the breaking of the boughs'.")
R("SER", "ser-", "go on, carry forward", "acts", o=[("ser-i-s", "ser", "go on, carry forward", {})], stem="ser-i",
  note="No longer the root of Seren (see SWE, REŊ); the guild hears it in her name all the same.")
R("XREUN", "xreun-", "set hard, harden; the hard thing", "acts",
  o=[("xreun-i-s", "rhyn", "set fast (of mortar), take hold", {}),
     ("xreun-aʔ", "rhyna", "Rhyna, 'she who sets fast' (a name)", dict(hal="hriunā", name=True))],
  s=[("xreun-i", "rhen", "stone, the mute thing; a wall", {})],
  note="Rhyna's name and the wood's word for stone are one. The Guest's errand-name Aelrhen, 'bond-to-stone', is at the root *ol-xreun: 'together, set fast'.")

# ------------------------------------------------------------------ QUALITIES
R("STROM", "strom-", "wide, great", "quality", o=[("strom-o-s", "strom", "great", {})], stem="strom-o")
R("LUSS", "luss-", "small", "quality", o=[("luss-i-s", "lyss", "small", {})], stem="luss-i")
R("GELL", "gell-", "fitting, good", "quality", o=[("gell-i-s", "gell", "good", {})], stem="gell-i")
R("WEINN", "weinn-", "sound, whole, true (as a plumb wall)", "quality",
  o=[("weinn-i-s", "venn", "true; plumb; faithful", {})],
  s=[("weinn-i", "veinn", "to mend, to make whole", {})],
  note="A True Man (vennuld) is, at the root, a whole man; the grain's MEND is 'make true'.")
R("GUNN", "gunn-", "deep", "quality", o=[("gunn-o-s", "gunn", "deep; the deep", {})], stem="gunn-o")
R("SELL", "sell-", "long", "quality", o=[("sell-i-s", "sell", "long", {})], stem="sell-i")
R("DOMM", "domm-", "black", "quality", o=[("domm-o-s", "domm", "black", {})], stem="domm-o")
R("BELL", "bell-", "golden", "quality", o=[("bell-i-s", "bell", "gold, golden", {})], stem="bell-i")
R("LENN", "lenn-", "pale-bright", "quality",
  o=[("lenn-i-s", "lenn", "silver", {})],
  s=[("lenn-i", "lenn", "white; bleached; the white", {})])

# ------------------------------------------------------------------ SMALL WORDS
R("ET", "et- / itt-", "this very one, the same", "small",
  o=[("et-as", "et", "the (the article)", dict(hal="etas", small=True))],
  s=[("itt-o", "ith", "one; alone; the same; own", {})],
  note="The stone's article and the wood's 'one' are one word: 'the' is 'that one'.")
R("UL", "ul-", "in, within", "small", o=[("ul-an", "ul", "in (+N)", dict(hal="ulan", small=True))], stem="ul")
R("XUI", "xui", "out of, from", "small",
  o=[("xui-a", "hy", "from, out of (+S)", dict(hal="hya", small=True))],
  s=[("xui", "rhi", "from, out of", dict(small=True))])
R("UM", "um-", "upon", "small", o=[("um-o", "um", "upon, on (+S)", dict(hal="umo", small=True))], stem="um")
R("LO", "lo- / li-", "at, by", "small",
  o=[("lo-a", "lo", "at, by, with (+S)", dict(hal="loa", small=True))],
  s=[("li", "li", "in, at, on (place)", dict(small=True))])
R("DEM", "dem-", "up to, as far as", "small", o=[("dem-en", "dem", "until, as far as (+N)", dict(hal="demen", small=True))], stem="dem")
R("ETH", "eθ-", "and, also", "small", o=[("eth-as", "eth", "and", dict(hal="ethas", small=True))], stem="eth")
R("ELL", "ell-", "or, else", "small", o=[("ell-o", "ell", "or", dict(small=True))], stem="ell")
R("WETH", "weθ-", "on the other side, rather", "small", o=[("weth-o", "veth", "but, rather", dict(small=True))], stem="weth")
R("NA", "na- / ni", "not", "small",
  o=[("na", "na", "un- (prefix, +S)", dict(small=True)), ("nath-an", "nath", "not (before a verb, +N)", dict(hal="nathan", small=True))],
  s=[("ni", "ni", "not (before the verb)", dict(small=True))])
R("RE", "re", "yonder, that; then, at that time", "small",
  o=[("re", "re", "past particle (+S)", dict(hal="re", small=True, irr="the spec's §4.3 gives Hal rea; the Stonwryt itself cuts RE, and RE is right: a vowel-final word, so it softens"))],
  s=[("re", "re", "that; the other one", dict(small=True)), ("re-il", "reil", "fore, front; before; first", dict(irr="soft reading of the Bar Before"))],
  note="A 'that' became the stone's past ('then') and the wood's fore ('the one before').")
R("ES", "es", "at another time, not now", "small",
  o=[("es-an", "es", "future particle (+N)", dict(hal="esan", small=True))],
  s=[("es", "es", "-es, the past of a verb (a particle fused after the final vowels fell)", {})],
  note="The stone looked forward with it and the wood looked back.")
R("HO", "ho-", "is it?", "small", o=[("ho-a", "ho", "question particle (+S)", dict(hal="hoa", small=True))], stem="ho")
R("SA", "sa / se", "that one, the one by you", "small",
  o=[("sa-e", "sa", "who, which, that (relative, +S)", dict(hal="sae", small=True))],
  s=[("sa", "sa", "you (one)", dict(small=True)), ("se", "se", "you (more than one)", dict(small=True))])
R("SONG", "soŋ-", "the length of a thing", "small", o=[("soŋ-ma-s", "somm", "while, as long as", dict(hal="soŋmas", small=True))], stem="soŋ-o")
R("ANG", "aŋ-", "at the hour", "small",
  o=[("aŋ-ma", "amm", "when (conj.)", dict(small=True))],
  s=[("aŋ-thi", "anth", "an hour; (clause-final) when", {})])
R("KA", "ka-, wo- + -ð-", "which one? (ka- of a person, wo- of a thing, with the asking suffix *-ð-)", "small",
  o=[("ka-dh-i", "cedh", "who?", dict(small=True)), ("wo-dh-o", "vodh", "what?", dict(small=True))], stem="ka-dh-i")
R("SIU", "siu", "this, here", "small", o=[("siu", "sy", "this (after the noun)", dict(hal="siu", small=True))], stem="siu")
R("ULL", "ull-", "that, there", "small", o=[("ull-o", "ull", "that (after the noun)", dict(small=True))], stem="ull")
R("GOR", "gor-", "all, each one", "small", o=[("gor-a", "gor", "every, all (+S)", dict(hal="gora", small=True))], stem="gor")
R("TUL", "tul-", "still, as yet", "small", o=[("tul-o", "tul", "yet, still", dict(small=True))], stem="tul")
R("DASK", "dask-", "the last of a thing", "small", o=[("dask-o-s", "dask", "the end", {})], stem="dask-o")
R("EN", "en-", "I, this one here", "small", o=[("en-an", "en", "I; my (+N)", dict(hal="enan", small=True))], stem="en")
R("THO", "θo-", "you (one)", "small", o=[("tho-e", "tho", "you; your (sg., +S)", dict(hal="thoe", small=True))], stem="tho")
R("O", "o-", "he, it", "small", o=[("o-a", "o", "he, it; his, its (+S)", dict(hal="oa", small=True))], stem="o")
R("EY", "ey-", "she", "small", o=[("ey-as", "ey", "she; her", dict(hal="eyas", small=True))], stem="ey")
R("OL", "ol", "together, one with another; we (all)", "small",
  o=[("ol-on", "ol", "we; our (+N)", dict(hal="olon", small=True)), ("ol-naʔ", "olna", "we two (+S)", dict(hal="olnā", small=True))],
  s=[("ol", "ael", "bond, joining; to bind; (adv.) together, too, likewise", {})],
  note="The Title says ol five times ('our home, our families...'); the Aelthar and the sliver's 'too' are the same word.")
R("WA", "wa-", "you (many)", "small", o=[("wa-n", "va", "you; your (pl., +N)", dict(hal="van", small=True, irr="the spec's Hal vanan is emended to van: vanan would give *van"))], stem="wa")
R("SO", "so-", "they", "small",
  o=[("so-a", "so", "they; their (+S)", dict(hal="soa", small=True)), ("so-naʔ", "sona", "they two (+S)", dict(hal="sonā", small=True))], stem="so")
R("BA", "ba / be", "I / we (the speaker's side)", "small", s=[("ba", "va", "I", dict(small=True)), ("be", "ve", "we", dict(small=True))], stem="ba")
R("LA", "la / le", "he, she (a living thing) / they", "small", s=[("la", "la", "he, she; it (a living thing)", dict(small=True)), ("le", "le", "they (living)", dict(small=True))], stem="la")
R("XA", "xa / xe", "it (a thing that does not answer) / they", "small", s=[("xa", "rha", "it (a mute thing: stone, iron, the dead)", dict(small=True)), ("xe", "rhe", "they (mute)", dict(small=True))], stem="xa")
R("RA", "ra", "this, the one in hand", "small", s=[("ra", "ra", "this; the held one", dict(small=True))], stem="ra")
R("NGA", "ŋa", "toward", "small", s=[("ŋa", "na", "to, toward", dict(small=True))], stem="ŋa")
R("TI", "ti", "through, past", "small", s=[("ti", "thi", "through, past, by way of", dict(small=True))], stem="ti")
R("LOQS", "loʔs", "above", "small", s=[("loʔs", "laes", "above, over", dict(small=True))], stem="loʔs")
R("SI", "si", "with; given that", "small",
  s=[("si", "si", "with", dict(small=True)), ("si", "sei", "if (closes a clause)", dict(irr="the stressed twin of si: a clause-final word took the knock's stress"))], stem="si")
R("RI", "ri", "go toward; against", "small",
  s=[("ri", "ri", "against, upon", dict(small=True)), ("ri", "rei", "to go", dict(irr="the stressed twin: the verb"))], stem="ri")
R("WI", "wi", "give; for (the sake of)", "small",
  s=[("wi", "vi", "for, for the sake of; so that", dict(small=True)), ("wi", "vei", "to give; a gift", dict(irr="the stressed twin: the verb"))], stem="wi")
R("EI", "ei", "and, and also", "small", s=[("ei", "ei", "and", dict(small=True))], stem="ei")
R("TES", "tes-", "after that", "small", s=[("tes", "thes", "then, after that", dict(small=True))], stem="tes")
R("LOQ", "loʔ", "is it so? ask", "small", s=[("loʔ", "lae", "(closes a question); to ask", dict(small=True))], stem="loʔ")

# ------------------------------------------------------------------ NUMBERS
R("HOS", "hos-", "one", "number", o=[("hos-o-s", "hos", "one", dict(hal="hosos"))], stem="hos-o")
R("PA", "pa-", "two", "number",
  o=[("paʔ", "pa", "two (+S)", dict(hal="pā")), ("pa-naʔ", "pana", "both", dict(hal="panā"))],
  s=[("pann-i", "vann", "two", {})],
  note="The proverb's last word is this root in both tongues: grest um vana / vann li thaess.")
R("ROS", "ros-", "three", "number",
  o=[("ros-t-o-s", "rost", "nine ('thrice three')", {})],
  s=[("ros-i", "raes", "three; (in the grain) many", {})],
  note="The stone kept the old three only in nine; its living three, sull, is new.")
R("SULL", "sull-", "a set of three", "number", o=[("sull-o-s", "sull", "three", {})], stem="sull-o")
R("GEMM", "gemm-", "four", "number", o=[("gemm-i-s", "gemm", "four", {})], stem="gemm-i")
R("NAL", "nal-", "the four fingers, a hand without its thumb", "number", s=[("nal-o", "nal", "four", {})], stem="nal-o")
R("LESK", "lesk-", "five", "number", o=[("lesk-i-s", "lesk", "five", {})], stem="lesk-i")
R("WIND", "wind-", "the whole hand", "number", s=[("wind-o", "vinn", "hand; five", {})], stem="wind-o")
R("FRAN", "fran-", "six", "number", o=[("fran-o-s", "vran", "six", {})], stem="fran-o")
R("DHOM", "ðom-", "seven", "number", o=[("dhom-o-s", "dhom", "seven", {})], stem="dhom-o")
R("THELL", "θell-", "eight", "number", o=[("thell-i-s", "thell", "eight", {})], stem="thell-i")
R("NOTH", "noθ-", "ten", "number", o=[("noth-o-s", "noth", "ten", {})], stem="noth-o")
R("DELF", "delf-", "a full course", "number", o=[("delf-i-s", "delv", "twelve", {})], stem="delf-i")
R("MURR", "murr-", "a score", "number", o=[("murr-o-s", "murr", "twenty", {})], stem="murr-o")
R("BOST", "bost-", "a great heap", "number", o=[("bost-o-s", "bost", "four hundred", {})], stem="bost-o")

# ------------------------------------------------------------------ AFFIXES
R("-ATHI", "-aθi", "many (the plural)", "affix", o=[("-athi", "-ath", "plural -Ath", dict(hal="-athi"))], stem="-athi")
R("-OLA", "-ol-a", "the doing (a verbal noun)", "affix", o=[("-ola", "-ol", "verbal noun -Ol", dict(hal="-ola"))], stem="-ola")
R("-AT", "-at", "done, made", "affix", o=[("-at", "-at", "participle -At", {})], stem="-at")
R("-ARD", "-ard", "one who does", "affix", o=[("-ard", "-ard", "agent -Ard", {})], stem="-ard")
R("-OTH", "-oθ", "the quality of", "affix", o=[("-oth", "-oth", "abstract -Oth", {})], stem="-oth")
R("-EL", "-el", "one, a small one", "affix", o=[("-el", "-el", "singulative; 'little, dear' (names)", {})], stem="-el")
R("-AN", "-an", "the folk of", "affix", o=[("-an", "-an", "collective 'the folk of'", {})], stem="-an")
R("-EN", "-en", "belonging to; (as a noun) those belonging", "affix",
  o=[("-en", "-en", "'of, belonging to'; an old name-ending", {})],
  s=[("-en", "-en", "plural", {})])
R("-UQ", "-uʔ", "at, the place of", "affix", o=[("-uʔ", "-ow", "place of -ow", dict(hal="-ū"))], stem="-uʔ")
R("-AST", "-ast", "the n-th", "affix", o=[("-ast", "-ast", "ordinal -Ast", {})], stem="-ast")
R("-AQ", "-aʔ", "the pair; she", "affix", o=[("-aʔ", "-a", "the old dual; feminine names; the pair-name lintel", dict(hal="-ā"))], stem="-aʔ")
R("-NAQ", "-naʔ", "the two of", "affix", o=[("-naʔ", "-na", "dual of a pronoun", dict(hal="-nā"))], stem="-naʔ")
R("-EQ", "-eʔ", "one of, one who", "affix", s=[("-eʔ", "-ea", "one of; one who; the n-th", {})], stem="-eʔ")
R("-AQR", "-aʔr", "all of a kind, those of", "affix",
  s=[("-aʔr", "-ear", "those of (a whole people or kind)", {}), ("-aʔr", "-aer", "the relic, kept in Esthaer and borrowed in Mystaeri", dict(relic_aer=True))], stem="-aʔr")
R("-AS", "-as", "the doing, the thing done", "affix", s=[("-as", "-as", "verbal noun", {})], stem="-as")
R("-ETH", "-eθ", "make (one) do", "affix", s=[("-eth", "-eth", "causative", {})], stem="-eth")
R("-E", "e", "now, here (a particle)", "affix", s=[("e", "-e", "verb: it does, it is doing (fused late)", {})], stem="e")
R("-AR", "ar", "toward (a goal)", "affix", s=[("ar", "-ar", "verb: it shall, it is meant to (fused late)", {})], stem="ar")
R("-ANE", "-ane", "one who bears or does (old)", "affix", s=[("-ane", "-en", "the old agent, merged with the plural; frozen in varen", {})], stem="-ane")
R("PERS", "-om, -ith, -os, -ana, -aʔ, -ar, -us, -ant", "the person endings of the verb", "affix",
  o=[("-om", "-om", "1sg -Om", {}), ("-ith", "-ith", "2sg -ith", {}), ("-ana", "-an", "1du -An (Hal -ana)", dict(hal="-ana")),
     ("-aʔ", "-a", "3du -A", {}), ("-ar", "-ar", "1pl -Ar: tum-ar 'we remember' < *tum-ar 'we hold'", {}),
     ("-us", "-us", "2pl -Os (Hal -us, reduced to the harmonic O)", {}), ("-ant", "-ant", "3pl -Ant", {})], stem="-ar",
  note="3sg *-os fell with the other endings, which is why the living 3sg is the bare stem (Hal stonos > ston).")

# ------------------------------------------------------------------ SEILRHASS ROOTS THE STONE DID NOT KEEP
R("THAR", "θar-", "blood", "body", s=[("thar-o", "thar", "blood; to bleed", {})], stem="thar-o")
R("LEW", "lew-", "green, fresh", "sea", s=[("lew-i", "lea", "green, young; new growth; new", {})], stem="lew-i")
R("RAL", "ral-", "a root", "sea", s=[("ral-o", "ral", "a root; a hull sent first", {})], stem="ral-o")
R("IR", "ir-", "far down, far back", "quality", s=[("ir-i", "eir", "deep; old; long; last; still; until", {})], stem="ir-i")
R("NIW", "niw-", "the gleam of a still surface", "quality", s=[("niw-i", "nei", "silver", {})], stem="niw-i")
R("RESS", "ress-", "go soft, rot", "acts", s=[("ress-i", "ress", "rot, the soft death of wood; to rot", {})], stem="ress-i")
R("LANTH", "lanθ- / lenθ-", "hold one's place, wait; (e-grade) the season of waiting", "acts",
  s=[("lanth-i", "lanth", "a knot in the grain; to wait, to hold one's place", {}),
     ("lenth-i", "lenth", "winter; the white season", dict(irr="the e-grade, 'the season of': the spec's own analysis"))], stem="lanth-i")
R("ESTH", "esθ-", "burn", "sky",
  s=[("esth-o", "esth", "fire; to burn", {}), ("esth-aʔr", "esthaer", "Esthaer, 'that of fire' (the Burning)", dict(relic_aer=True, name=True))],
  stem="esth-o")
R("WATH", "waθ-", "an outer skin", "sea", s=[("wath-o", "vath", "bark", {})], stem="wath-o")
R("ROSS", "ross-", "a slow inner flowing", "sea", s=[("ross-i", "raess", "sap", {})], stem="ross-i")
R("IL", "il-", "a round, a going-round", "sea", s=[("il-o", "eil", "a growth ring; a time (once, twice); to count", {})], stem="il-o")
R("WUR", "wur-", "living wood", "sea", s=[("wur-i", "veir", "wood, the living stuff", {})], stem="wur-i")
R("WUS", "wus-", "a seed", "sea", s=[("wus-i", "veis", "seed; the winged seed", {})], stem="wus-i")
R("SUL", "sul-", "a bough; to bend", "sea", s=[("sul-i", "seil", "bough, branch; a hull; to bend as a bough bends", {})], stem="sul-i")
R("KRITH", "kriθθ-", "a hard cutting edge; (later) iron, the axe", "war", s=[("kriththi", "rhith", "iron; the axe; the felling; to fell", {})], stem="kriththi")
R("NIR", "nir-", "sing", "speech", s=[("nir-a", "neira", "to sing; a song", {})], stem="nir-a")
R("KRIS", "kris-", "a hard glint", "sky", s=[("kris-i", "rheis", "hard light; the open sun; a flash (of a gun)", {})], stem="kris-i")
R("LIS", "lis-", "what comes next", "sky", s=[("lis-i", "leis", "the morrow; the next coming", {})], stem="lis-i")
R("RETH", "reθ-", "the earth underfoot", "sea", s=[("reth-o", "reth", "ground, earth", {})], stem="reth-o")
R("REQS", "reʔs-", "moving air", "sky", s=[("reʔs-o", "reas", "wind", {})], stem="reʔs-o")
R("NITH", "niθθ-", "falling water", "sky", s=[("niththi", "nith", "rain", {})], stem="niththi")
R("ENTH", "enθ-", "a rim, an edge", "sea", s=[("enth-o", "enth", "edge, rim, margin", {})], stem="enth-o")
R("GWES", "gwes-", "a way", "sea", s=[("gwes-o", "ves", "a road; a way over water", {})], stem="gwes-o")
R("LANN", "lann-", "an arm", "body", s=[("lann-o", "lann", "arm", {})], stem="lann-o")
R("LIN", "lin-", "the brow", "body", s=[("lin-o", "lein", "brow, forehead", {})], stem="lin-o")
R("NEQS", "neʔs-", "the eye; to look", "body", s=[("neʔs-o", "neas", "eye; to see, to look", {})], stem="neʔs-o")
R("IS", "is-", "a name, a calling-out", "speech", s=[("is-o", "eis", "name; to name", {})], stem="is-o")
R("ENN", "enn-", "within; the one from within", "body",
  s=[("enn-o", "enn", "within, inside", {}), ("enn-a", "enna", "a child", {})], stem="enn-o")
R("GWETH", "gweθ-", "a way in", "bond", s=[("gweth-o", "veth", "door; the way in", {})], stem="gweth-o")
R("SATH", "saθ-", "the back", "body", s=[("sath-o", "sath", "back, stern; behind", {})], stem="sath-o")
R("AFEN", "afen-", "the other", "quality", s=[("afen-o", "aven", "other; another", {})], stem="afen-o")
R("ONN", "onn-", "a gap, the between", "acts", s=[("onn-o", "aenn", "open; a gap; between; to open", {})], stem="onn-o")
R("GRISS", "griss-", "seize", "acts", s=[("griss-i", "rhiss", "to take, to seize", {})], stem="griss-i")
R("ROTH", "roθ-", "fold the knee", "acts", s=[("roth-i", "raeth", "to kneel", {})], stem="roth-i")
R("IQLA", "iʔl-", "breathe, live", "acts",
  s=[("iʔl-aʔ", "ilae", "to live; to breathe; life", {}), ("iʔl-en-o", "ilen", "to lean, to incline toward (as one leans to breathe)", {})], stem="iʔl-aʔ")
R("NENN", "nenn-", "sink", "acts", s=[("nenn-o", "nenn", "to fall, to sink", {})], stem="nenn-o")
R("SOQ", "soʔ", "come", "acts", s=[("soʔ", "sae", "to come", {})], stem="soʔ")
R("NETH", "neθ-", "turn aside", "acts", s=[("neth-i", "neth", "to turn, to turn aside", {})], stem="neth-i")
R("TASS", "tass-", "strike", "acts", s=[("tass-o", "thass", "to strike; a blow", {})], stem="tass-o")
R("SEINN", "seinn-", "listen, heed", "acts", s=[("seinn-i", "seinn", "to hear; to heed", {})], stem="seinn-i")
R("TAFALL", "tafall-", "go after", "acts", s=[("tafall-o", "thaval", "to hunt, to go for", {})], stem="tafall-o")
R("SOSS", "soss-", "hunger", "acts", s=[("soss-i", "saess", "hunger; to hunger", {})], stem="soss-i")
R("SENTH", "senθ-", "dread", "acts", s=[("senth-o", "senth", "dread, fear; the dread", {})], stem="senth-o")
R("ITH", "iθ-", "hollow, a seeming", "quality", s=[("ith-o", "eith", "hollow, empty; a seeming", {})], stem="ith-o")
R("ISS", "iss-", "thin", "quality", s=[("iss-o", "iss", "thin, slight", {})], stem="iss-o")
R("LEQS", "leʔs-", "swift", "quality", s=[("leʔs-o", "leas", "swift; to run", {})], stem="leʔs-o")
R("EISS", "eiss-", "so, as it is", "quality", s=[("eiss-o", "eiss", "so; true; what is (the copula)", {})], stem="eiss-o")
