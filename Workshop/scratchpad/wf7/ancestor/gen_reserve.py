"""Generate original reserve roots for the Book's vocabulary.

Forms are drawn (seeded, deterministic) from the first tongue's own phonotactics, by
texture (hard / soft / plain), then screened:
  * the root, and its Orrowen and Seilrhass reflexes, collide with no attested word
    and with no other reserve root;
  * no reflex is in the Tolkien/franchise blacklist;
  * neither the root nor its reflexes is an English dictionary word (so no reserve
    word reads as English, and none can be a relexed English word);
  * the Seilrhass reflex is legal Seilrhass, the Orrowen reflex legal Orrowen.
"""
import random, re, json, sys
import laws, predict

MEANINGS = [
 # (key, meaning, field, texture, cls)   cls: o broad / i slender
 ("son", "a son", "hearth", "plain", "o"), ("daughter", "a daughter", "hearth", "soft", "i"),
 ("husband", "a husband, the man of a hearth", "hearth", "plain", "o"), ("wife", "a wife, the woman of a hearth", "hearth", "soft", "i"),
 ("brother", "a brother", "hearth", "plain", "o"), ("sister", "a sister", "hearth", "soft", "aʔ"),
 ("grandmother", "a grandmother, an old mother of the hearth", "hearth", "soft", "aʔ"),
 ("forebear", "a forebear; the old line", "hearth", "plain", "o"), ("kin", "kin by blood", "hearth", "plain", "o"),
 ("friend", "a friend, one who stands beside", "hearth", "soft", "i"), ("stranger", "a stranger, one from beyond", "hearth", "hard", "i"),
 ("foe", "a foe, one who comes against", "war", "hard", "o"), ("lord", "a lord, one who holds land", "hearth", "hard", "o"),
 ("trader", "a trader, one who carries goods", "hearth", "plain", "i"), ("clerk", "one who keeps the rolls, a clerk", "speech", "plain", "i"),
 ("gaoler", "one who shuts in, a gaoler", "war", "hard", "o"), ("fisher", "a fisher", "sea", "plain", "i"),
 ("shipmaster", "one who knows the water, a ship-master", "sea", "plain", "o"), ("boatwright", "a worker of wood, a boatwright", "sea", "hard", "i"),
 ("youth", "a youth, one not yet grown", "hearth", "soft", "o"), ("newborn", "a newborn", "hearth", "soft", "o"),
 ("bereft", "one bereft: an orphan, a widow", "hearth", "soft", "o"), ("herald", "one who cries news", "speech", "plain", "o"),
 ("lookout", "a watcher on a height", "war", "hard", "o"), ("troop", "a troop, a band under one leader", "war", "hard", "o"),
 ("council", "a council, those who sit and weigh", "hearth", "plain", "i"), ("boy", "a boy", "hearth", "plain", "o"), ("girl", "a girl", "hearth", "soft", "i"),
 # body
 ("head", "the head", "body", "hard", "o"), ("face", "the face", "body", "soft", "i"), ("hair", "hair", "body", "soft", "o"),
 ("ear", "an ear; to listen", "body", "soft", "o"), ("nose", "the nose; to smell", "body", "plain", "o"), ("tongue", "the tongue", "body", "soft", "o"),
 ("tooth", "a tooth", "body", "hard", "i"), ("lip", "a lip", "body", "soft", "i"), ("skin", "skin, a hide", "body", "plain", "o"),
 ("bone", "a bone", "body", "hard", "o"), ("shoulder", "the shoulder", "body", "plain", "o"), ("knee", "the knee", "body", "hard", "i"),
 ("foot", "the foot", "body", "plain", "o"), ("finger", "a finger", "body", "plain", "i"), ("belly", "the belly, the womb", "body", "soft", "o"),
 ("breast", "the breast", "body", "soft", "i"), ("tear", "a tear; to weep", "body", "soft", "i"), ("sleep", "sleep; to sleep", "body", "soft", "o"),
 ("wake", "wake, be awake", "body", "hard", "i"), ("dream", "a dream", "body", "soft", "o"), ("fever", "a fever, a burning of the body", "body", "hard", "i"),
 ("sickness", "sickness", "body", "plain", "i"), ("strength", "strength", "body", "hard", "o"), ("scar", "a scar, a healed cut", "body", "hard", "o"),
 ("eat", "eat", "body", "plain", "o"), ("drink", "drink", "body", "soft", "i"), ("sweat", "sweat, toil", "body", "plain", "i"),
 # sky, time
 ("sun", "the sun", "sky", "plain", "o"), ("moon", "the moon; a month", "sky", "soft", "o"), ("star", "a star", "sky", "soft", "i"),
 ("cloud", "a cloud", "sky", "soft", "o"), ("shadow", "a shadow", "sky", "soft", "o"), ("dawn", "the first light, dawn", "sky", "soft", "o"),
 ("dusk", "the last light, dusk, evening", "sky", "soft", "i"), ("noon", "the middle of the day, noon", "sky", "plain", "i"),
 ("morning", "the morning", "sky", "plain", "o"), ("spring", "spring, the lengthening", "sky", "soft", "i"), ("summer", "summer", "sky", "plain", "o"),
 ("autumn", "autumn, the gathering-in", "sky", "plain", "o"), ("month", "a month, a moon's turn", "sky", "plain", "i"), ("week", "a week, a turn of days", "sky", "plain", "i"),
 ("now", "now", "small", "plain", ""), ("later", "after, later", "small", "plain", ""), ("early", "early, before the time", "sky", "plain", "o"),
 ("late", "late, after the time", "sky", "plain", "i"), ("age", "an age, a long time", "sky", "soft", "o"), ("never", "never", "small", "plain", ""),
 ("again", "again", "small", "plain", ""), ("yesterday", "yesterday", "sky", "plain", "o"), ("season", "a time, a season", "sky", "soft", "i"),
 # land, water, weather, creatures
 ("moss", "moss", "sea", "soft", "o"), ("fern", "a fern", "sea", "soft", "o"), ("grass", "grass", "sea", "soft", "o"),
 ("flower", "a flower", "sea", "soft", "o"), ("fruit", "fruit", "sea", "soft", "o"), ("stump", "a stump", "sea", "hard", "o"),
 ("shoot", "a shoot from a stump", "sea", "plain", "o"), ("thorn", "a thorn", "sea", "hard", "o"), ("cave", "a hole, a cave", "sea", "plain", "o"),
 ("crag", "a crag", "sea", "hard", "o"), ("cliff", "a cliff", "sea", "hard", "i"), ("pass", "a pass through mountains", "sea", "plain", "o"),
 ("valley", "a valley", "sea", "soft", "o"), ("canyon", "a gorge, a canyon", "sea", "hard", "o"), ("pebble", "a pebble", "sea", "hard", "i"),
 ("shingle", "shingle, the stony beach", "sea", "hard", "i"), ("surf", "surf, breaking water", "sea", "hard", "o"), ("wave", "a wave", "sea", "soft", "o"),
 ("foam", "foam", "sea", "soft", "o"), ("current", "a current in the sea", "sea", "plain", "o"), ("channel", "a channel", "sea", "plain", "o"),
 ("shallows", "shallow water", "sea", "soft", "i"), ("bank", "a bank, a raised edge", "sea", "plain", "o"), ("bay", "a bay, a bend of the shore", "sea", "soft", "i"),
 ("mere", "a lake, a mere", "sea", "soft", "i"), ("pool", "a pool", "sea", "soft", "o"), ("well", "a spring, a well", "sea", "soft", "i"),
 ("mud", "mud", "sea", "plain", "o"), ("salt", "salt", "sea", "hard", "o"), ("smoke", "smoke", "sky", "soft", "o"), ("dust", "dust", "sky", "plain", "o"),
 ("ember", "an ember", "sky", "plain", "i"), ("flame", "a flame", "sky", "soft", "o"), ("spark", "a spark", "sky", "hard", "o"),
 ("hail", "hail", "sky", "hard", "o"), ("lightning", "lightning", "sky", "hard", "i"), ("tempest", "a storm at sea", "sky", "hard", "o"),
 ("calm", "a calm, windless water", "sky", "soft", "o"), ("desert", "a waste of sand", "sea", "plain", "o"), ("bird", "a bird", "sky", "soft", "o"),
 ("fish", "a fish", "sea", "soft", "i"), ("fledgling", "a fledgling", "sky", "soft", "i"), ("beast", "a beast", "sea", "hard", "i"),
 ("feather", "a feather; a wing", "sky", "soft", "i"), ("boulder", "a boulder", "sea", "hard", "o"), ("hollow", "a low place, a hollow", "sea", "soft", "i"),
 ("land", "dry land", "sea", "plain", "i"), ("freeze", "cold; to freeze", "sky", "hard", "i"), ("warm", "warm", "sky", "soft", "o"),
 ("dry", "dry", "quality", "hard", "i"), ("wet", "wet", "quality", "soft", "i"), ("bright", "bright", "quality", "hard", "i"),
 ("dim", "dim", "quality", "soft", "i"), ("pale", "pale", "quality", "soft", "i"), ("brown", "brown", "quality", "plain", "i"),
 # things, building
 ("rope", "a rope", "stone", "plain", "o"), ("chest", "a chest", "stone", "hard", "i"), ("lid", "a lid, a cover", "stone", "plain", "i"),
 ("key", "a key; to lock", "stone", "hard", "i"), ("lamp", "a lamp", "stone", "soft", "o"), ("torch", "a torch", "stone", "hard", "o"),
 ("oil", "oil", "bond", "soft", "o"), ("flask", "a flask", "stone", "plain", "o"), ("cup", "a cup", "hearth", "plain", "o"),
 ("bread", "bread", "hearth", "plain", "o"), ("ale", "ale", "hearth", "soft", "o"), ("bed", "a bed", "hearth", "soft", "i"),
 ("table", "a table", "hearth", "plain", "o"), ("seat", "a seat, a chair", "hearth", "plain", "o"), ("bench", "a bench", "hearth", "plain", "i"),
 ("die", "a die for casting lots", "hearth", "hard", "o"), ("pipe", "a pipe", "hearth", "plain", "i"), ("blanket", "a blanket, a wool cloth", "hearth", "soft", "o"),
 ("pack", "a pack, a bundle", "hearth", "hard", "o"), ("cart", "a cart", "stone", "hard", "o"), ("wheel", "a wheel", "stone", "soft", "i"),
 ("oar", "an oar", "sea", "plain", "o"), ("keel", "a keel", "sea", "hard", "i"), ("rib", "a rib of a hull or a body", "sea", "plain", "i"),
 ("plank", "a plank", "sea", "hard", "o"), ("mast", "a mast", "sea", "hard", "o"), ("strake", "a strake, a line of planking", "sea", "plain", "i"),
 ("seam", "a seam", "sea", "soft", "i"), ("adze", "an adze", "stone", "hard", "o"), ("trowel", "a trowel", "stone", "plain", "o"),
 ("staff", "a staff, a rod", "stone", "plain", "o"), ("pike", "a pike, a long spear", "war", "hard", "i"), ("banner", "a banner, a sign flown", "war", "plain", "o"),
 ("pennant", "a pennant", "war", "soft", "o"), ("coin", "a coin, a struck piece", "stone", "hard", "o"), ("goldmetal", "gold, the metal", "stone", "soft", "o"),
 ("cedar", "cedar", "bond", "plain", "o"), ("myrrh", "myrrh", "bond", "soft", "aʔ"),
 ("granite", "granite, the grained stone", "stone", "hard", "i"), ("powder", "powder", "war", "plain", "o"), ("cloth", "cloth", "hearth", "soft", "i"),
 ("thread", "a thread", "hearth", "soft", "i"), ("needle", "a needle", "hearth", "hard", "i"), ("knife", "a knife, a short blade", "war", "hard", "i"),
 ("spear", "a spear", "war", "hard", "i"), ("bow", "a bow for shooting", "war", "plain", "o"), ("net", "a net", "sea", "plain", "o"),
 ("boat", "a small boat", "sea", "plain", "o"), ("raft", "a raft; to float", "sea", "soft", "o"), ("bridge", "a bridge, a span", "stone", "plain", "i"),
 ("stair", "a stair; to climb", "stone", "plain", "i"), ("step", "a step", "stone", "hard", "o"), ("vault", "a vault, an arched room below", "stone", "plain", "o"),
 ("cellar", "a cellar", "stone", "plain", "i"), ("shaft", "a shaft cut down", "stone", "hard", "o"), ("floor", "a floor", "stone", "plain", "o"),
 ("roof", "a roof", "stone", "plain", "o"), ("beam", "a beam", "stone", "hard", "o"), ("pillar", "a pillar of stone", "stone", "plain", "o"),
 ("buttress", "a buttress, a propping wall", "stone", "hard", "i"), ("arch", "an arch", "stone", "soft", "o"), ("gallery", "a gallery, a way cut in rock", "stone", "plain", "o"),
 ("hall", "a hall", "stone", "plain", "i"), ("room", "a room", "stone", "plain", "o"), ("window", "a window, an eye in a wall", "stone", "soft", "aʔ"),
 ("threshold", "a threshold", "bond", "plain", "o"), ("drain", "a drain", "stone", "plain", "o"), ("crane", "a crane, a lifting-beam", "stone", "hard", "i"),
 ("scaffold", "a scaffold", "stone", "hard", "o"), ("niche", "a niche, a small hollow in a wall", "stone", "soft", "i"), ("grave", "a grave", "bond", "plain", "o"),
 ("holy", "holy, set apart", "bond", "soft", "i"), ("altar", "a raised stone of offering", "bond", "plain", "o"), ("marketplace", "a market", "hearth", "plain", "o"),
 ("town", "a walled town", "stone", "plain", "o"), ("joint", "a joint between stones", "stone", "plain", "o"), ("foundation", "a foundation, the bottom course", "stone", "hard", "o"),
 ("ruin", "a ruin, a thing broken down", "war", "hard", "o"),
 # war, order
 ("siege", "a siege, a sitting-down around", "war", "hard", "o"), ("assault", "an assault, a rushing-on", "war", "hard", "o"), ("battle", "a battle", "war", "hard", "i"),
 ("sortie", "a going-out, a sortie", "war", "plain", "o"), ("breach", "a breach", "war", "hard", "o"), ("volley", "a volley, a shower of shot", "war", "hard", "o"),
 ("flee", "flee", "war", "soft", "o"), ("chase", "chase, drive before one", "war", "hard", "o"), ("ambush", "lie in wait", "war", "plain", "o"),
 ("snare", "a snare, a trap", "war", "plain", "i"), ("lie", "a lie; to lie", "speech", "soft", "o"), ("plan", "a plan, a counsel", "speech", "plain", "i"),
 ("order", "an order; to bid", "war", "hard", "i"), ("obey", "obey, heed an order", "war", "soft", "i"), ("signal", "a sign, a signal", "speech", "plain", "o"),
 ("victory", "a victory", "war", "hard", "i"), ("defeat", "a defeat", "war", "plain", "o"), ("yield", "yield, give oneself up", "war", "soft", "i"),
 ("truce", "a truce, a peace made", "war", "soft", "o"), ("captive", "a captive", "war", "hard", "o"), ("defend", "defend, ward off", "war", "hard", "i"),
 # mind, feeling, faith
 ("think", "think; a thought", "speech", "soft", "o"), ("understand", "understand, grasp", "speech", "plain", "o"), ("believe", "believe, hold true", "bond", "soft", "o"),
 ("doubt", "doubt", "speech", "plain", "o"), ("hope", "hope", "bond", "soft", "o"), ("fear", "fear", "acts", "hard", "o"),
 ("shame", "shame", "bond", "plain", "o"), ("pride", "pride", "bond", "hard", "o"), ("joy", "gladness, joy", "bond", "soft", "o"),
 ("laugh", "laugh", "acts", "soft", "o"), ("mercy", "mercy", "bond", "soft", "i"), ("forgive", "forgive, let a wrong go", "bond", "soft", "o"),
 ("bless", "bless", "bond", "soft", "o"), ("wish", "wish, want", "acts", "soft", "o"), ("choose", "choose", "acts", "plain", "i"),
 ("learn", "learn", "speech", "soft", "i"), ("wonder", "wonder", "speech", "soft", "o"), ("endure", "patience; to endure", "bond", "plain", "o"),
 ("hate", "hatred; to hate", "bond", "hard", "o"), ("courage", "courage", "bond", "hard", "o"), ("wise", "wise", "quality", "soft", "i"),
 ("foolish", "foolish; a fool", "quality", "plain", "o"), ("gentle", "gentle", "quality", "soft", "i"), ("cruel", "cruel, hard of heart", "quality", "hard", "i"),
 ("kind", "kind", "quality", "soft", "i"), ("glad", "glad, content", "quality", "soft", "i"), ("sad", "sad, heavy of heart", "quality", "soft", "o"),
 ("lonely", "alone, lonely", "quality", "soft", "o"), ("soul", "the self within, a soul", "bond", "soft", "o"), ("heaven", "the high dwelling, heaven", "bond", "soft", "o"),
 ("rite", "a rite, a thing done in order", "bond", "plain", "i"), ("anoint", "anoint", "bond", "soft", "i"), ("praise", "praise", "bond", "soft", "o"),
 ("lot", "a lot cast; one's lot", "bond", "plain", "o"), ("mind", "the mind", "speech", "soft", "o"), ("seek", "seek", "acts", "plain", "o"),
 # acts
 ("sit", "sit", "acts", "plain", "i"), ("liedown", "lie down", "acts", "soft", "i"), ("climb", "climb", "acts", "hard", "i"),
 ("haul", "drag, haul", "acts", "hard", "o"), ("pull", "pull", "acts", "plain", "o"), ("push", "push", "acts", "hard", "o"),
 ("lift", "lift", "acts", "plain", "o"), ("lower", "lower", "acts", "soft", "o"), ("throw", "throw", "acts", "hard", "i"),
 ("catch", "catch", "acts", "hard", "o"), ("tie", "tie, knot fast", "acts", "plain", "i"), ("weave", "weave", "acts", "soft", "i"),
 ("sew", "sew", "acts", "soft", "i"), ("dig", "dig", "acts", "hard", "o"), ("bury", "bury, lay in earth", "acts", "soft", "o"),
 ("cover", "cover", "acts", "plain", "o"), ("hide", "hide", "acts", "soft", "o"), ("find", "find", "acts", "plain", "i"),
 ("lose", "lose", "acts", "soft", "o"), ("bring", "bring", "acts", "plain", "i"), ("save", "save, bring through", "acts", "soft", "i"),
 ("spare", "spare", "acts", "soft", "o"), ("spend", "spend", "acts", "plain", "o"), ("buy", "buy, trade for", "hearth", "plain", "o"),
 ("sell", "sell", "hearth", "plain", "i"), ("pay", "pay; a payment", "hearth", "plain", "o"), ("measure", "measure", "stone", "plain", "o"),
 ("cut", "cut", "acts", "hard", "o"), ("hew", "hew", "acts", "hard", "o"), ("polish", "polish, rub smooth", "stone", "soft", "i"),
 ("pour", "pour", "acts", "soft", "o"), ("fill", "fill; full", "acts", "plain", "o"), ("empty", "empty", "quality", "plain", "o"),
 ("kindle", "kindle", "acts", "hard", "o"), ("quench", "quench, put out", "acts", "soft", "o"), ("wash", "wash", "acts", "soft", "o"),
 ("swim", "swim", "acts", "soft", "i"), ("sail", "sail (v.)", "sea", "soft", "o"), ("row", "row", "sea", "plain", "o"),
 ("drown", "drown", "sea", "soft", "o"), ("begin", "begin", "acts", "plain", "o"), ("return", "return, come back", "acts", "plain", "i"),
 ("watch", "watch, keep watch", "acts", "plain", "o"), ("touch", "touch", "acts", "soft", "o"), ("feel", "feel", "acts", "soft", "i"),
 ("say", "say", "speech", "plain", "i"), ("shout", "shout, scream", "speech", "hard", "o"), ("whisper", "whisper", "speech", "soft", "i"),
 ("bowdown", "bow, bend low", "acts", "soft", "o"), ("promise", "promise; a promise", "speech", "plain", "i"), ("lead", "lead", "war", "plain", "o"),
 ("follow", "follow", "war", "soft", "o"), ("sow", "sow seed", "acts", "soft", "o"), ("reap", "reap, gather in", "acts", "hard", "i"),
 ("tend", "tend, care for", "acts", "soft", "i"), ("prune", "prune, cut back to help grow", "acts", "hard", "i"), ("guide", "show the way, guide", "acts", "soft", "o"),
 ("fell", "fell a tree", "acts", "hard", "o"), ("arrive", "come in, arrive", "acts", "plain", "o"), ("rise", "wake up, rise from sleep", "acts", "plain", "i"),
 ("play", "play; a game", "acts", "soft", "o"), ("dance", "dance", "acts", "soft", "i"), ("skip", "skip, leap", "acts", "hard", "i"),
 ("scream", "a scream", "speech", "hard", "i"), ("warn", "warn; a warning", "speech", "plain", "o"), ("trade", "trade, exchange goods", "hearth", "plain", "o"),
 # qualities
 ("high", "high", "quality", "plain", "o"), ("low", "low", "quality", "soft", "o"), ("wide", "wide", "quality", "plain", "i"),
 ("narrow", "narrow", "quality", "hard", "o"), ("near", "near", "quality", "soft", "o"), ("far", "far", "quality", "plain", "i"),
 ("thick", "thick", "quality", "hard", "i"), ("soft", "soft", "quality", "soft", "o"), ("hard", "hard", "quality", "hard", "o"),
 ("strong", "strong", "quality", "hard", "o"), ("weak", "weak", "quality", "soft", "o"), ("slow", "slow", "quality", "soft", "o"),
 ("quick", "quick", "quality", "hard", "i"), ("hot", "hot", "quality", "hard", "i"), ("cold", "cold", "quality", "hard", "o"),
 ("red", "red", "quality", "plain", "o"), ("grey2", "grey (as ash)", "quality", "soft", "o"), ("sweet", "sweet", "quality", "soft", "o"),
 ("bitter", "bitter", "quality", "hard", "i"), ("rich", "rich", "quality", "plain", "i"), ("poor", "poor", "quality", "soft", "o"),
 ("humble", "humble, low-set", "quality", "soft", "o"), ("brave", "brave, bold", "quality", "hard", "o"), ("clean", "clean", "quality", "soft", "i"),
 ("quiet", "quiet", "quality", "soft", "i"), ("loud", "loud", "quality", "hard", "o"), ("wild", "wild", "quality", "hard", "i"),
 ("strange", "strange", "quality", "plain", "i"), ("sure", "sure", "quality", "plain", "i"), ("sharp", "sharp", "quality", "hard", "o"),
 ("blunt", "blunt, dull", "quality", "plain", "o"), ("light", "light (not heavy)", "quality", "soft", "i"), ("broken", "broken", "quality", "hard", "o"),
 ("half", "half", "quality", "plain", "o"), ("few", "few", "quality", "soft", "o"), ("none", "none, no one", "small", "plain", ""),
 ("much", "much, many", "quality", "plain", "o"), ("worn", "old (of things), worn", "quality", "plain", "o"), ("goodwork", "well made, well done", "quality", "plain", "o"),
 ("evil", "evil, ill", "quality", "hard", "o"), ("proud", "proud", "quality", "hard", "o"), ("fair", "fair, lovely to see", "quality", "soft", "i"),
 # small words
 ("here", "here", "small", "plain", ""), ("there", "there", "small", "plain", ""), ("where", "where?", "small", "plain", ""),
 ("why", "why? how?", "small", "plain", ""), ("only", "only", "small", "plain", ""), ("also", "also, likewise", "small", "plain", ""),
 ("thus", "so, thus", "small", "plain", ""), ("because", "because", "small", "plain", ""), ("without", "without", "small", "plain", ""),
 ("among", "with, among", "small", "plain", ""), ("after", "after", "small", "plain", ""), ("before", "before (of time)", "small", "plain", ""),
 ("perhaps", "perhaps", "small", "plain", ""), ("very2", "very, most", "small", "plain", ""), ("almost", "almost", "small", "plain", ""),
]

# distributions shaped on the core roots (the first tongue's own look)
ON = {"hard": ["k", "t", "g", "d", "kr", "tr", "gr", "dr", "sk", "st", "x", "br", "p", "t", "k", "g"],
      "soft": ["l", "m", "n", "s", "w", "f", "h", "th", "dh", "sw", "xw", "l", "m", "n", "s", ""],
      "plain": ["b", "p", "d", "t", "k", "g", "m", "n", "l", "r", "s", "f", "w", "h", "th", "dh", "x", "pr", "pl", "kl", "gl", "bl", "xr", "sp", "st", "t", "l", "r", ""]}
VW = {"hard": ["a", "o", "u", "e", "i", "a", "o", "aʔ", "oʔ", "ai", "eu"],
      "soft": ["e", "i", "a", "o", "u", "ei", "ai", "eʔ", "iʔ", "aʔ", "ui", "e", "i"],
      "plain": ["a", "e", "i", "o", "u", "a", "e", "o", "u", "ai", "ei", "eu", "aʔ", "eʔ", "oʔ", "uʔ"]}
CO = {"hard": ["k", "t", "d", "g", "sk", "st", "rk", "rt", "nd", "rd", "ld", "th", "ss", "rn", "r", "n", "l", "nt", "lt"],
      "soft": ["l", "n", "m", "r", "s", "th", "dh", "ll", "nn", "mm", "rr", "lm", "rn", "lf", "rw", "ŋ", "nth", "lth", "sth", "lw"],
      "plain": ["k", "t", "d", "sk", "st", "rk", "rt", "nd", "rd", "ld", "th", "l", "n", "m", "r", "s", "dh", "ll", "nn", "mm", "rr", "lm", "rn", "nth", "ss"]}
MID = ["l", "r", "n", "m", "s", "th", "dh", "f", "w", "d", "t", "k", "g", "b", "p"]

COMMON = set(open("common_english.txt").read().split())
DICT = set(w.strip().lower() for w in open("/usr/share/dict/words") if len(w.strip()) >= 4)
BL = predict.BL
AVOID = set("""garr denn tross garv lethen lenn wyll sonn cand ethra gelv tol mell ennael leith thil nae naes eneth
orn sil nen hith mith sarn gond ondo galadh eryn taur duin dor ost barad aran ren lin tir mor gil kal
""".split())

O_ON = re.compile(r"^(?:[bcdfghklmnprstv]|th|dh|rh|w|br|bl|dr|tr|cr|cl|gr|gl|pr|pl|sp|st|sc|str|fl|fr|thr)?$")
O_CO = re.compile(r"^(?:[bcdfgklmnprstv]|th|dh|rh|rd|rt|ld|lt|nd|nt|rc|rn|rl|lm|rm|rv|lv|rth|rdh|lth|nth|st|sk|nn|mm|ll|rr|ss)?$")
def legal_o(liv):
    m = re.match(r"^([^aeiouy]*)(.*?)([^aeiouy]*)$", liv)
    if not m:
        return False
    on, mid, co = m.groups()
    if not O_ON.match(on) or not O_CO.match(co):
        return False
    inner = re.findall(r"[^aeiouy]+", mid)
    return all(len(x) <= 3 for x in inner) and not re.search(r"(.)\1\1", liv)

def legal_s(liv):
    return bool(re.fullmatch(r"(?:(?:rh|th|[vslrn])?(?:ae|ea|ei|a|e|i)(?:nth|sth|ss|nn|th|[lnrs])?)+", liv)) and len(liv) >= 2

S_SUFFIX_END = re.compile(r"(en|es|eth|as|ar|ea|ear|ae|ne|e)$")
O_SUFFIX_END = re.compile(r"(at|ard|an|en|el|ol|oth|ath|ast|a|ow)$")
ON_MORE = ["sp", "sk", "st", "tr", "kr", "gr", "br", "dr", "pr", "pl", "kl", "gl", "bl", "xr", "xw", "sw", "thr"]

def gen(seed=23):
    rnd = random.Random(seed)
    roots, have_o, have_s = predict.attested_sets()
    used_o = set(have_o); used_s = set(have_s)
    used_roots = set()
    out = []
    for key, mean, field, tex, cls in MEANINGS:
        got = None
        for attempt in range(30000):
            mono = attempt < 20000
            on = rnd.choice(ON[tex] + (ON_MORE if attempt > 6000 else []))
            v = rnd.choice(VW[tex]); co = rnd.choice(CO[tex])
            if mono or cls in ("", "aʔ"):
                root = on + v + co
            else:
                v2 = rnd.choice(["a", "e", "a", "e", "o", "i"])
                root = on + rnd.choice(["a", "e", "i", "o", "u"]) + rnd.choice(["l", "r", "n", "m", "th", "s", "f", "d", "k"]) + v2 + rnd.choice(["l", "n", "r", "s", "th", "k", "d", "m"])
            if cls == "":
                stem = root
            elif cls == "aʔ":
                stem = root + "-aʔ"
            else:
                stem = root + "-" + cls
            small = (cls == "")
            if root in used_roots or root.replace("ʔ", "") in AVOID or root.replace("ʔ", "") in COMMON:
                continue
            d_o = laws.derive_o(stem if (small or cls == "aʔ") else stem + "s", small=small)
            d_s = laws.derive_s(stem, small=small)
            lo, ls = d_o["living"].lower(), d_s["living"].lower()
            if lo in used_o or ls in used_s or ls in BL or lo in BL or lo in AVOID or ls in AVOID:
                continue
            if lo in COMMON or ls in COMMON or lo in DICT or ls in DICT:
                continue
            if len(lo) > 7 or len(ls) > 7:
                continue
            if re.search(r"(aea|eae|eaa|aee|eie|eia|iae|rh[aei]+rh|th[aei]+th|v[aei]+v)", ls):
                continue
            if not mono and (S_SUFFIX_END.search(ls) or O_SUFFIX_END.search(lo)):
                continue
            if cls not in ("", "aʔ") and len(re.findall(r"(ae|ea|ei|a|e|i)", ls)) == 1 and S_SUFFIX_END.search(ls) and ls.endswith(("ea", "ae")):
                continue
            if not legal_s(ls) or not legal_o(lo) or len(lo) < 2:
                continue
            got = dict(key=key, root=root + ("-" if cls else ""), mean=mean, field=field, stem=stem,
                       o_pred=d_o["living"], hal=d_o["hal"], s_pred=d_s["living"], eldest=d_s["eldest"])
            used_o.add(lo); used_s.add(ls); used_roots.add(root)
            break
        if got:
            out.append(got)
        else:
            print("FAILED", key, file=sys.stderr)
    return out

if __name__ == "__main__":
    out = gen()
    json.dump(out, open("reserve.json", "w"), ensure_ascii=False, indent=0)
    print(len(out), "reserve roots")
    for r in out:
        print(r["key"].ljust(12), ("*" + r["root"]).ljust(10), r["o_pred"].ljust(9), r["s_pred"].ljust(9), r["mean"])
