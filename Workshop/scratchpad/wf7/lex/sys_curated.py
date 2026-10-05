"""The curated side of the systematic derivations (scratch, wf7/lex).

The builder derives freely where a suffix's meaning is regular (every verb has its verbal noun,
participle and agent; every quality its abstract and its 'not'). Where the meaning is not regular
(a place of X, the folk of X, un-done, X-ish, a little X), only the words listed here are derived,
each with the sense a speaker would give it.
"""

# -ow, "place of": nouns, with the sense of the place
OW_NOUNS = {
    "tolm": "a stone-yard, where dressed stone is stacked", "mesk": "a wood-lot, a stand of timber",
    "grull": "the sands, a sandy shore", "linth": "a meadow, a grassy place", "feth": "a mossy place, a moss",
    "sinth": "a flower-bed, a place of flowers", "nanth": "an orchard", "stell": "a field of cairns",
    "ledal": "a graveyard", "nas": "a rookery, a place of birds", "ses": "a fishing-ground",
    "kynt": "a lair, a den of beasts", "sulter": "a boat-yard, a boat-strand", "sceth": "a shipyard",
    "serull": "a treasury, a place of coins", "blenth": "a bakehouse", "braemur": "an alehouse",
    "lodull": "a sleeping-room, a dormitory", "vestul": "a store-room of chests", "havul": "a storehouse",
    "hagess": "an armoury of pikes", "hesp": "an armoury", "bramm": "a gun-emplacement, a gun-pit",
    "pedh": "a shot-store, a magazine", "kest": "a barracks", "crest": "an ice-field",
    "sulv": "a snowfield", "frenn": "a frost-land, a rime-field", "spenn": "a mudflat",
    "tant": "a salt-pan", "bront": "a boulder-field", "tynt": "a pebble-beach", "brint": "a thicket of thorns",
    "brynt": "a stump-field, a felled place", "gend": "a coppice, a place of young shoots",
    "vorr": "a fire-place, a hearth-pit", "tuss": "a dusty place, a waste", "dhidh": "a smoke-hole, a chimney",
    "luth": "an ink-room, a scriptorium", "flenn": "a library, a place of leaves",
    "rellor": "a signal-post", "movenn": "a standard-post", "stomorn": "a timber-yard",
    "crynir": "a plank-store", "greller": "a lamp-room", "nunth": "a buttery, a place of cups",
    "roval": "a cloth-store", "piskur": "a net-loft", "nestull": "an oar-store", "breller": "a slipway",
    "saenul": "a colonnade, a place of pillars", "stinal": "a holy place of offering-stones",
    "lorr": "a place of slaughter", "derd": "an ossuary, a bone-house", "rivull": "a foundation-pit",
    "heskal": "a bridgehead", "bystir": "a stairwell", "gylorn": "a market-square", "hinnar": "a townland",
    "gebb": "a porch, a doorway", "genth": "a refectory, a place of tables", "prenth": "a bench-row, a court",
    "sirr": "a glass-house", "kyvil": "a granite-quarry", "styvil": "a gold-working", "govul": "a powder-store",
    "nuless": "a gaming-room, a dicing-place", "mygur": "a smoking-room",
}
# -ow, "a place for V-ing": verbs
OW_VERBS = {
    "resk": "a place, a seat (where one sits)", "aedh": "a sleeping-place, a bed-chamber",
    "nask": "an eating-place, a hall of meals", "fimm": "a drinking-place, a watering-place",
    "vilv": "a dancing-floor", "ammel": "a place of prayer, a chapel", "lamm": "a burial-ground",
    "pask": "a dig, a diggings", "nend": "a watch-post, a lookout", "cemm": "a meeting-place",
    "ridh": "a washing-place", "felv": "a bathing-pool", "sodh": "a playing-field, a game-ground",
    "serdul": "a trading-post", "hynal": "a selling-place, a stall", "pyskorn": "a workshop",
    "gorr": "a fighting-ground, a lists", "rystull": "a school, a place of learning",
    "ammad": "a teaching-house", "sol": "a resting-place", "tovv": "a waiting-place, an anchorage",
    "lumm": "a kneeling-place, a shrine", "farr": "a sea-lane, a sailing-ground", "tav": "a landing-place",
    "gald": "a building-site, a works", "vell": "a singing-place, a choir", "ryt": "an archive, a place of writings",
    "firr": "a lying-place, a lair", "derr": "a reaping-field", "fymm": "a sown field",
    "hurr": "a killing-ground", "comull": "a weaving-shed", "cald": "a hauling-way, a slipway",
    "nydh": "a counting-house", "hess": "a stopping-place, a halt", "cadh": "a laying-course, a building-bed",
    "par": "a ward, a courtyard (the guarded place)", "mymm": "a returning-place, a home port",
    "lusk": "a place of release", "haemer": "a raft-landing", "gyst": "a climbing-place, a scaling-point",
    "hollar": "a refuge", "sevess": "an ambush-place", "hydull": "a place of patience, a waiting-room",
}
# -an, "the folk of": people nouns, with the sense of the whole
AN_PEOPLE = {
    "hass": "the sons (of a house)", "henn": "the daughters (of a house)", "vost": "a brotherhood",
    "lalva": "a sisterhood", "memm": "a fellowship, one's friends", "besk": "the strangers, the foreign folk",
    "bynd": "the enemy host", "pithul": "the lords, the nobility", "vaskorn": "the traders, the merchants' guild",
    "saevul": "the clerks, the chancery", "higil": "the ship-masters", "pynull": "the boatwrights",
    "rall": "the youth, the young folk", "luld": "the boys", "nemm": "the girls", "vadull": "the forebears, the old line",
    "dhaker": "the bereft, the orphans and widows", "begorn": "the lookouts", "uld": "mankind, the menfolk",
    "essa": "womankind, the women", "gedh": "the fathers", "odha": "the mothers", "arra": "the guests",
    "prass": "the masters (of the guild)", "pard": "the wardens", "crenn": "the captains",
    "humm": "the husbands", "verr": "the wives", "scaelur": "the grandmothers", "remm": "the newborns",
    "tev": "the children's folk, the young of a hearth",
    "sugorn": "the fisher-folk", "heness": "the captives", "gennar": "the fools",
    "kynt": "the beasts, the herd", "nas": "a flock of birds", "ses": "a shoal of fish",
}
# na- on the participle: "un-V-ed"
NA_PTCP = {
    "cresk": "unbroken", "sesk": "unknown", "vesk": "unread, unseen", "voth": "untended", "hunn": "unheard",
    "gald": "unbuilt", "cadh": "unlaid", "hosk": "unsealed", "ryt": "uncut, unwritten", "stann": "unquarried",
    "keth": "unheld, unkept", "tum": "unremembered", "lodh": "unmortared", "tunn": "unfinished",
    "clenn": "unmended", "voll": "unnamed", "nydh": "uncounted", "tess": "unanswered", "hebb": "ungiven",
    "lusk": "unloosed, unreleased", "peskul": "unblessed", "haeril": "unforgiven", "lamm": "unburied",
    "wesk": "unfound", "renn": "unsaved", "stin": "uncut", "dann": "unhewn", "dasor": "unpolished",
    "esk": "uncovered", "lemm": "unhidden", "bysk": "untied", "tragul": "unpromised", "pess": "unasked",
    "hyrril": "not understood", "daevar": "unbelieved", "par": "unguarded", "pemess": "undefended",
    "gost": "unfelled", "derr": "unreaped", "fymm": "unsown", "cald": "unhauled", "bemm": "unlifted",
    "syndal": "unkindled", "raltar": "unquenched", "ridh": "unwashed", "losk": "unfilled",
    "grik": "uncaught", "drunn": "unstruck", "brodh": "untold", "carm": "uncalled", "ammad": "untaught",
    "rystull": "unlearned", "nesk": "unled", "fenn": "unfollowed", "lestir": "unguided", "comull": "unwoven",
    "lyrnenn": "unsewn", "pask": "undug", "nethil": "unpaid", "hynal": "unsold", "lenull": "unbought",
    "haral": "unbidden", "lynir": "unheeded", "stathul": "unpraised", "buthar": "unanointed",
    "hurr": "unslain", "mamm": "unlost", "haemer": "unfloated", "vall": "unloved", "osk": "untrusted",
}
# -el on a quality: "somewhat X, X-ish"
EL_ADJ = {
    "domm": "blackish, darkish", "lenn": "silvery", "bell": "goldish, pale gold", "sulv": "whitish",
    "unth": "reddish", "terril": "greyish", "vaenal": "brownish", "stacorn": "palish, wan",
    "lorr": "reddish, blood-tinged", "myst": "hazy, greyish", "baeg": "brightish, gleaming",
    "dustal": "dimmish, dusky", "brid": "coolish, chill", "bith": "warmish", "crent": "chilly",
    "dhaedh": "lukewarm", "broc": "dryish", "thenth": "dampish, damp", "lilv": "softish",
    "duss": "hardish", "niss": "slowish", "pynt": "quickish, brisk", "rimm": "sweetish",
    "scid": "bitterish, sharp", "velv": "quietish, hushed", "bont": "loudish", "dyss": "odd, a little strange",
    "sell": "longish", "lyss": "tiny, very small", "strom": "largish, sizeable", "susk": "highish",
    "vimm": "lowish", "ryss": "broadish", "bynt": "slender", "deld": "farish, distant",
    "virr": "near at hand", "gesk": "sturdy", "mirr": "weakly, frail", "hemm": "oldish, elderly",
    "clenn": "newish, fresh", "gunn": "deepish", "dind": "thickish", "lelv": "lightish, slight",
}
# nouns that are not counted things: no -el (a little X) and no -en for them
MASS_TIME = {
    "blenth", "feth", "styvil", "sast", "grull", "tant", "spenn", "tuss", "dhidh", "fidh", "drid", "sulv", "crest",
    "sirr", "lernul", "braemur", "roval", "govul", "lorr", "luth", "brenth", "linth", "nynth", "hedh", "dhess",
    "sorenn", "ryst", "heth", "syst", "bremm", "grem", "orl", "vess", "clem", "surr", "dynd", "bress", "selm",
    "begess", "fedh", "gordal", "lomm", "sollan", "lunn", "vennoth", "tumol", "hoss", "aedh", "cathal",
    "mylenn", "suress", "pyskorn", "lyrness", "kaemul", "hylenn", "teltor", "hydull", "tevir", "syllorn",
    "saemal", "ludal", "myrral", "grumar", "pussal", "prener", "wadh", "helv", "myst", "hal", "lodh", "frenn",
    "trun", "gaed", "vonul", "nerdess", "ressur", "maress", "styvess", "kyvil", "bell", "lenn", "grest",
    "stykil", "bethir", "kaever", "niltenn", "haral", "haethil", "sannal", "lernil", "kiser", "stemir",
    "tynur", "sevir", "ranner", "nycul", "tragul", "peltir", "sodh", "serdul", "nethil", "semm", "filv",
}

# -el on a collective: the singulative, one member (canon: scethel, stonwrytel)
COLLECTIVE_EL = {
    "redul": "a councillor, one of the council", "lonn": "a kinsman, a kinswoman", "lunt": "one of a people, a countryman",
    "cryrull": "a trooper, one of a troop", "theld": "one of a household", "lurr": None, "tesk": None,
    "stell": "one stone of a cairn", "trenn": "one stone of a course", "flenn": None,
}
# -Ard on a noun: "the one of the X" (canon: hesperd 'sword-one', drunnard 'hammer-one', a smith)
OCCUPATIONS = {
    "mesk": "a woodsman, a forester", "sceth": "a shipman, a hull-hand", "gomm": "a hornblower",
    "hagess": "a pikeman", "sivur": "a spearman", "raenorn": "a bowman", "piskur": "a netman, a fisherman",
    "sulter": "a boatman", "luth": "an inker, a copyist", "flenn": "a bookman, a keeper of leaves",
    "bramm": "a gunner", "pedh": "a shot-carrier", "wemm": "a sailmaker", "nestull": "an oarsman",
    "roval": "a clothier", "greller": "a lamplighter", "tymorn": "a torch-bearer", "bunth": "a ropemaker",
    "vestul": "a chest-keeper, a steward", "serull": "a moneyer", "gylorn": "a market-man, a hawker",
    "braemur": "an alewife, a brewer", "blenth": "a baker", "roskur": "a key-keeper, a turnkey",
    "birnenn": "a trowel-man, a layer", "movenn": "a standard-bearer", "gever": "a pennant-bearer",
    "kest": "a corporal, the leader of a file", "cumm": "a haven-man", "tavow": "a harbourmaster",
    "stell": "a cairn-builder", "ledal": "a gravedigger", "nas": "a fowler", "ses": "a fisherman",
    "kynt": "a herdsman", "heskal": "a bridge-keeper", "gebb": "a doorkeeper, a porter",
    "hellur": "a hall-keeper", "odh": "a host, a keeper of the hearth", "redul": "a politician, a councilman",
    "prynur": "a scaffolder", "stendor": None, "lodh": "a mortar-man, a mixer", "tolm": "a mason",
    "wadh": "a seafarer", "gorn": "a quoin-setter", "hosk": "a capstone-layer, the sealer of a work",
}
# -Oth on a noun: the state of being one (-hood, -ship)
NOUN_OTH = {
    "uld": "manhood", "tev": "childhood", "memm": "friendship", "vost": "brotherhood (the bond of brothers)",
    "lalva": "sisterhood", "pithul": "lordship", "crenn": "captaincy, command", "prass": "mastery",
    "arra": "guesthood, the guest's right", "odha": "motherhood", "gedh": "fatherhood",
    "humm": "husbandhood, the bond of the husband", "verr": "wifehood", "pard": "wardenship",
    "hemm": "old age; eldership", "rall": "youth, the years before the growing", "bynd": "enmity",
    "besk": "strangeness, the state of a stranger", "heness": "captivity", "dhaker": "bereavement",
    "gennar": "folly", "lonn": "kinship", "theld": "the bond of a household", "lunt": "nationhood",
    "sceth": None, "tesk": None,
}
# na- on a verb: the reversative (canon: nadhum 'forget', nayald 'destroy')
REVERSATIVE = {
    "cadh": "unlay, take down (a course)", "bysk": "untie, undo a knot", "hosk": "unseal, lift a capstone",
    "lodh": "unbind, rake out the mortar", "roskur": "unlock", "daevar": "disbelieve", "lynir": "disobey",
    "peskul": "curse ('unbless')", "stathul": "blame, dispraise", "comull": "unweave, unravel",
    "lyrnenn": "unpick a seam", "lamm": "unbury, exhume", "tragul": "break a promise, forswear",
    "sesk": "not know, be ignorant of", "ammad": "mislead, unteach", "rystull": "unlearn",
    "clenn": "wear out, make old", "tunn": "undo, leave unfinished", "keth": "let slip, lose hold of",
    "par": "leave unguarded, betray a watch", "osk": None, "vall": "stop loving, turn from",
    "hebb": None, "tess": "leave unanswered", "rhyn": "loosen (of mortar: fail to set)",
    "ston": "fall from standing, give way", "tald": "sink down, stoop", "voll": "unname, strike a name out",
    "ryt": "unswear, break a vow", "lymm": "take away", "renn": "abandon, leave unsaved",
    "gyst": "climb down", "bemm": "set down, unload", "haral": "countermand",
}
# -an on things: the collective, the whole set (canon: scethan 'a fleet', bramman 'a battery')
AN_THINGS = {
    "gann": "a palisade, a row of posts", "tolm": "a heap of dressed stone, the stones of a work",
    "wemm": "a spread of sails", "fodh": "the breakers, a run of waves", "elth": "a constellation",
    "henth": "a bank of cloud", "hesp": "a band of swords", "hagess": "a hedge of pikes",
    "gomm": "a sounding of horns", "stell": "a field of cairns", "trenn": "the courses of a wall",
    "crynir": "a planking, a deck of planks", "stomorn": "a frame of beams, a roofing",
    "saenul": "a colonnade", "disker": "a row of windows", "lusul": "a flight of steps",
    "sivur": "a thicket of spears", "raenorn": "a line of bows", "greller": "a string of lamps",
    "tymorn": "a torchlit line, a procession", "flenn": None, "rellor": "a code of signals",
    "vell": "a song-cycle", "brod": "a speech, a set of words", "gend": "a coppice, the new growth",
    "sinth": "a garland", "nynth": "the springs, the wells of a place", "rhull": "a river-system",
    "nell": "an archipelago", "gynt": "the crags", "gint": "a range of cliffs", "brunn": "a range of mountains",
    "sorth": "the ridges", "misk": "a footing of men, a file", "garl": "a crew of hands",
    "bisk": "a head-count, a muster",
}
# -en on a thing that is not counted: the adjective of a material or a time
MASS_EN = {
    "blenth": "of bread", "styvil": "of gold (the metal)", "sast": "of hide, leathern", "grull": "sandy",
    "tant": "salty, of salt", "spenn": "muddy", "tuss": "dusty", "dhidh": "smoky", "fidh": "foamy",
    "crest": "icy", "sulv": "snowy", "sirr": "of glass, glassy", "lernul": "oily", "roval": "of cloth",
    "lorr": "bloody, of blood", "luth": "inky", "brenth": "of coal", "linth": "grassy", "nynth": "watery",
    "maress": "of cedar", "kyvil": "of granite", "wadh": "of the sea, sea-going", "helv": "of the sky, airy",
    "myst": "misty, of the grey", "hal": "of the bedrock, rock-born", "lodh": "of mortar",
    "frenn": "frosty", "trun": "earthen, of the ground", "gaed": "of dry land", "orl": "daily, of the day",
    "vess": "nightly, of the night", "surr": "yearly", "grem": "wintry", "syst": "of summer",
    "heth": "of spring", "bremm": "autumnal", "ryst": "of the morning", "hedh": "of evening",
    "dhess": "of dawn", "clem": "hourly", "fedh": "timely, seasonable", "begess": "age-old",
    "feth": "mossy", "govul": "powdery", "braemur": "of ale", "styvess": "of myrrh", "vorr": "fiery",
    "lomm": "grievous", "sollan": "peaceful", "lunn": "free", "hoss": "breathing, of breath",
    "aedh": "sleepy", "cathal": "sickly", "mylenn": "strong, of strength", "ludal": "fearful",
    "kaemul": "shameful", "lyrness": "prideful", "hylenn": "joyful", "teltor": "merciful",
    "saemal": "hopeful", "tevir": "hateful", "syllorn": "courageous", "myrral": "of the soul, soulful",
    "grumar": "heavenly", "prener": "of the mind", "pussal": "fated",
}
# -an on a place: its folk (canon: Orrowan 'the shore-folk', Treskan 'the cleft-folk')
AN_PLACES = {
    "cumm": "the haven-folk", "hinnar": "the townsfolk", "lurr": "the forest-folk", "brunn": "the mountain-folk",
    "sedh": "the fen-folk", "nell": "the islanders", "sorth": "the ridge-folk", "wadh": "the sea-folk",
    "tavow": "the harbour-folk", "kethow": "the keep-folk, the garrison", "gaed": "the landsfolk",
    "myst": "the mist-folk, the folk of the grey (Seren's gloss of Mystaeri)", "gylorn": "the market-folk",
    "stannow": "the quarry-folk", "drunnow": "the smithy-folk", "odh": "the hearth-folk, those who sit at a hearth",
}
# lexicalised plurals: a plural with a sense of its own (canon: flennath 'the Book', tevath 'children')
PLURAL_SENSES = {
    "tolm": "stonework, masonry ('the stones')", "trenn": "the courses of a wall; the tales of a night",
    "surr": "age, the years of a life", "orl": "days, a lifetime", "brod": "words; a speech",
    "hesp": "arms, weapons ('swords')", "tesk": "the generations, the old line", "wemm": "sails; a fleet under sail",
    "gann": "posts; a palisade", "rellor": "signs; a code", "stell": "cairns; a burial-field",
}
# -At on a noun: "provided with X, X-ed" (canon: lodhat 'mortared, bonded', treskat 'riven')
NOUN_AT = {
    "crest": "iced over", "sulv": "snowed over, snow-covered", "frenn": "rimed, frosted", "tuss": "dusted, dusty",
    "spenn": "muddied", "tant": "salted", "lorr": "bloodied", "myst": "fogged, lost in the grey",
    "dhidh": "smoked, smoke-blackened", "henth": "clouded, overcast", "feth": "mossed, moss-grown",
    "linth": "grassed over", "crisur": "roofed", "hald": "walled", "pressir": "floored", "trenn": "coursed, laid in courses",
    "gebb": "doored", "disker": "windowed", "stomorn": "beamed", "crynir": "planked", "bunth": "roped",
    "wemm": "rigged, under sail", "lernul": "oiled, anointed with oil", "bell": "gilded", "sirr": "glazed",
    "dhenth": "feathered", "bisk": "headed, crowned", "misk": "footed", "gann": "posted, fenced with posts",
    "hesp": "sworded, armed", "movenn": "bannered", "roval": "clothed", "naeval": "blanketed",
    "stell": "cairned, marked with a cairn", "ryt": "inscribed", "rellor": "signed, marked",
}
# -Oth on a derived quality
DERIVED_OTH = {"navenn": "falsehood, untruth", "nasell": "shortness", "nalelv": "heaviness, weight",
               "naryll": "cheapness, worthlessness", "nahunn": "deafness", "nawrodh": "muteness, dumbness",
               "nayess": "doubt, uncertainty", "naross": "absence", "hossen": "life, liveliness",
               "hyvenn": "outwardness", "ulvenn": "inwardness, the inner life", "tevel": "youth, youngness",
               "lurrel": "greenness"}
OW_NOUNS.update({"lorr": None} if False else {})
OW_NOUNS.update({
    "gorn": "a nook, a corner-place", "ganna": None, "trun": "a plot of ground, a field", "hyll": "a tidal flat",
    "odh": None, "fodh": "a surf-beach, where the waves break", "kess": "a race, a place of currents",
    "nynth": "a spring-head, a watering-place", "lynth": "a lake-land", "gint": "a cliff-land", "gynt": "a crag-land",
    "nenth": "a vale-land", "vem": "a burning-place, a pyre", "semm": None, "hass": None,
    "sast": "a tannery, a place of hides", "derd": "an ossuary, a bone-house",
})
AN_THINGS.update({
    "pedh": "a volley of shot (the shot of one discharge)", "sceth": None, "bramm": None, "fodh": "the breakers, a run of waves",
    "nas": "a flock of birds", "ses": "a shoal of fish", "tev": None,
})
# -Ard on a quality: "one who is X" (the agent of a state)
ADJ_ARD = {
    "berd": "a brave one, a hero", "podul": "a wise one, a sage", "deth": "a proud one, a boaster",
    "rirn": "a poor man", "dyll": "a rich man", "dath": "an evildoer", "gell": "a good man",
    "pryssal": "a kind soul", "ruthar": "a cruel one, a tyrant", "dagorn": "a gentle one",
    "nestorn": "a humble one", "sumess": "a glad one", "prumul": "a sad one, a mourner", "hyvul": "a loner",
    "dend": "a wild one, an outlaw", "dyss": "an odd one, a stranger in his ways", "mirr": "a weakling",
    "gesk": "a strong man", "niss": "a laggard, a slow one", "bont": "a loud one, a brawler",
    "velv": "a quiet one", "pynt": "a quick one", "crystil": "a worn old thing, a veteran",
}
# -an on a quality: "the X ones" (the folk who are X)
ADJ_AN = {"rirn": "the poor", "dyll": "the rich", "hemm": "the elders, the old", "gell": "the good",
          "dath": "the wicked", "berd": "the brave", "podul": "the wise", "nestorn": "the humble",
          "prumul": "the mourners", "dend": "the wild folk"}
# -ow on a quality: "a place of X"
ADJ_OW = {"susk": "a height, a high place", "vimm": "a low place, a bottom", "deld": "a far place, the distance",
          "gunn": "a deep place, the depths", "broc": "a dry place, a desert", "thenth": "a wet place, a marsh",
          "bith": "a hot place", "brid": "a cold place", "dend": "a wild place, a wilderness",
          "velv": "a quiet place, a retreat", "peness": "a holy place, a sanctuary", "dustal": "a dim place, a shade",
          "baeg": "a bright place, a clearing", "rerr": "a fair place, a pleasance"}
