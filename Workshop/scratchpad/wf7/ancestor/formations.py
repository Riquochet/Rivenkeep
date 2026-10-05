"""Names, and the words each living tongue built for itself out of inherited parts.

A formation is not a sound change: it is the daughter's own grammar at work
(compounding, suffixes, mutation).  Each part must itself be an inherited word
(roots_core / names below) or another formation.
"""
from roots_core import R, ROOTS

# ------------------------------------------------------------------ NAMES
# "Sometimes a name is just a name."  These names are regular Orrowen and have an
# ancestral shape, but no sense is given for most of them.
NAMES = [
    ("tarn-el-o-s", "tarnel", "Tarnel, 'little net' (*tarn- 'a net' + *-el)", dict(hal="tarnelos", name=True)),
    ("garf-el-o-s", "garvel", "Garvel, 'little smith' (*garf- 'forge', a Hal word lost from the living tongue)", dict(hal="garvelos", name=True)),
    ("korlen-o-s", "corlen", "Corlen (a cradle-name; no sense)", dict(name=True)),
    ("woss-o-s", "voss", "Voss", dict(name=True)),
    ("xaleʔa", "hale", "Hale", dict(name=True)),
    ("marl-o-s", "marl", "Marl", dict(name=True)),
    ("tamm-o-s", "tamm", "Tamm", dict(name=True)),
    ("askeʔa", "aske", "Aske", dict(name=True)),
    ("xarl-o-s", "harl", "Harl", dict(name=True)),
    ("uld-en-o-s", "ulden", "Ulden", dict(name=True)),
    ("hesk-o-s", "hesk", "Hesk", dict(name=True)),
    ("lann-er-o-s", "lanner", "Lanner", dict(name=True)),
    ("ald-un-o-s", "aldun", "Aldun (the first builder of Aldwena)", dict(name=True)),
    ("ben-aʔ", "bena", "Bena (the first builder of Aldwena)", dict(name=True)),
    ("id-lan-o-s", "idlan", "Idlan (of Idrenna)", dict(name=True)),
    ("denn-aʔ", "denna", "Denna (of Idrenna)", dict(name=True)),
]
R("NAMES", "—", "Shoreland cradle-names (names are names)", "name", o=NAMES, s=[], stem="tamm-o")

# ------------------------------------------------------------------ ORROWEN FORMATIONS
# word: (parts, how)
O_FORM = {
    # stone
    "nayald": (["na-", "gald"], "na- + S gald (g > y)"),
    "stannow": (["stann", "-ow"], "place -ow"),
    "gorndholm": (["gorn", "tolm"], "compound: second element softened (t > dh)"),
    "trenndholm": (["trenn", "tolm"], "compound, softened"),
    "halflenn": (["hal", "flenn"], "compound 'rock-leaf'"),
    "stonwryt": (["ston", "ryt"], "Hal compound stonwryta, built on the Hal stems ston- and wryt- (hence its y); the guild keeps the w in spelling"),
    "stonwrytan": (["stonwryt", "-an"], "collective"),
    "stonwrytel": (["stonwryt", "-el"], "singulative"),
    "prassel": (["prass", "-el"], "'little master'"),
    # faith, bond
    "vennoth": (["venn", "-oth"], "abstract (the spec's slip: by harmony vennyth)"),
    "lodhat": (["lodh", "-at"], "participle"),
    "nalodhat": (["na-", "lodhat"], "un-"),
    "lodhan": (["lodh", "-an"], "collective: et Lodhan, the Bonded"),
    "sullast": (["sull", "-ast"], "ordinal"),
    "hosast": (["hos", "-ast"], "ordinal"),
    "pawast": (["pa", "-ast"], "ordinal (w between the vowels)"),
    "veskerd": (["vesk", "-ard"], "agent, slender"),
    "tevow": (["tev", "-ow"], "Hal tevū, built on tev- after the i-colouring"),
    "tevath": (["tev", "-ath"], "Hal tevāthi: the broad plural of an old ā-plural"),
    "tevel": (["tev", "-el"], "'young'"),
    "hoskol": (["hosk", "-ol"], "the sealing"),
    "hoskvoll": (["hosk", "voll"], "compound, softened"),
    "tolm vardh": (["tolm", "mardh"], "construct, possessor softened (m > v)"),
    "tolmath vardh": (["tolm", "-ath", "mardh"], "plural"),
    "tunnoth": (["tunn", "-oth"], "wholeness"),
    "ryt dhunnoth": (["ryt", "tunnoth"], "construct, softened (t > dh)"),
    "lodh helv": (["lodh", "helv"], "construct"),
    "odh sell": (["odh", "sell"], "the Long Hearth"),
    # hearth, people
    "orrowan": (["orrow", "-an"], "the shore-folk"),
    "orrowen": (["orrow", "-en"], "'of the Shore'"),
    "brodhen": (["brodh", "-en"], "a speech, a tongue"),
    "treskan": (["tresk", "-an"], "the cleft-folk (broad: the spec keeps tresk's old broad suffixes, as in treskat)"),
    # war
    "ketherd": (["keth", "-ard"], "the holder: the Commander"),
    "vennuld": (["venn", "uld"], "compound: a True Man"),
    "hesperd": (["hesp", "-ard"], "'sword-one'"),
    "bramman": (["bramm", "-an"], "a battery"),
    "haskard": (["hask", "-ard"], "a runner"),
    "drunnard": (["drunn", "-ard"], "a smith"),
    "drunnow": (["drunn", "-ow"], "a smithy"),
    "hosk lunn": (["hosk", "lunn"], "the Title of Liberty"),
    "scethan": (["sceth", "-an"], "a fleet"),
    "scethel": (["sceth", "-el"], "one hull of it"),
    "treskat": (["tresk", "-at"], "riven, torn (an old broad suffix: see §11b of the spec)"),
    "covv treskat": (["covv", "treskat"], "the Torn Cloak"),
    # sea, grey
    "mystow": (["myst", "-ow"], "the Mystlands"),
    "mystaeri": (["myst", "-aer", "-i"], "hybrid: Orrowen myst + the Eldest Seilrhass -aer (before -aer > -ear) + an Orrowen loan-plural -i"),
    "mesk myst": (["mesk", "myst"], "Mystwood"), "tolm myst": (["tolm", "myst"], "Myststone"),
    "gannath myst": (["gann", "-ath", "myst"], "the Mystholders"), "crenn myst": (["crenn", "myst"], "a Mystarch"),
    "lurrel": (["lurr", "-el"], "green, 'forest-coloured'"),
    # body, speech
    "tumol": (["tum", "-ol"], "memory (also inherited whole: *tum-ol-a)"),
    "nadhum": (["na-", "tum"], "forget, un-remember (t > dh)"),
    "flennath": (["flenn", "-ath"], "the Book: broad, as an old ā-stem (see tevath)"),
    "nydherd": (["nydh", "-ard"], "a counter: Kael Nydherd"),
    "brodhat": (["brodh", "-at"], "told"), "nawrodhat": (["na-", "brodhat"], "untold (b > w)"),
    "kethyl": (["keth", "-ol"], "holding (slender -yl)"), "sennyl": (["senn", "-ol"], "dying, death"),
    "tumar": (["tum", "-ar"], "we remember: the hearth's answer, and Orrowen's 'yes'"),
    "ulvenn": (["ul", "venn"], "inner: 'true-in'"),
    "tolmvard": (["tolm", "pard"], "Stone-Warden, Halvard's epithet"),
    "cadhat": (["cadh", "-at"], "laid"),
    # names, pair-names
    "halyna": (["hal", "rhyna", "-a"], "pair-name: Hal- + softened Rhyn- (rh > h, lost after a consonant) + the lintel -a"),
    "aldwena": (["aldun", "bena", "-a"], "pair-name: Ald- + softened Ben- (b > w) + -a"),
    "idrenna": (["idlan", "denna", "-a"], "pair-name: Id- + softened Denn- (d > r) + -a"),
    "kael nydherd": (["kael", "nydherd"], "Kael the Counter"),
    # the havens
    "tavow hemm": (["tavow", "hemm"], "Eldhythe"), "cemm hyll": (["cemm", "hyll"], "Tidesmeet"),
    "sedhnell": (["sedh", "nell"], "Fenholm"), "lurrvard": (["lurr", "pard"], "Holtward (p > v)"),
    "kethow stellath": (["kethow", "stell", "-ath"], "Carnhold (the spec's broad -ath)"),
    "tavow vorr": (["tavow", "vorr"], "Emberhythe"), "grullsorth": (["grull", "sorth"], "Sandreach"),
    "frennvar": (["frenn", "par"], "Rimewatch (p > v)"), "taldow helv": (["taldow", "helv"], "Highreach"),
    "sirrvell": (["sirr", "pell"], "Glasspire (p > v)"),
    "kethow dhresk": (["kethow", "tresk"], "Rivenkeep (t > dh)"),
    "et hosk": (["et", "hosk"], "the Title"),
    # numbers
    "hosnoth": (["hos", "noth"], "eleven"), "sullnoth": (["sull", "noth"], "thirteen"),
    "pa relv": (["pa", "delv"], "twenty-four, 'two twelves' (d > r)"), "pa vurr": (["pa", "murr"], "forty (m > v)"),
    "lesk murr": (["lesk", "murr"], "a hundred"), "delvoth": (["delv", "-oth"], "twelvefold"),
    "et delv": (["et", "delv"], "the Twelve"),
    # small-word forms the tables give
    "nel": (["na", "el"], "is not: the Hal's contraction"), "new": (["na", "ew"], "was not"),
    "yal": (["gal"], "was: re + S gal (g > y)"),
}

# ------------------------------------------------------------------ SEILRHASS FORMATIONS
S_FORM = {
    "ralen": (["ral", "-en"], "roots; the root-bond"),
    "sethen": (["seth", "-en"], "carvings"), "thaen": (["thae", "-en"], "tides (after a vowel -n)"),
    "ennan": (["enna", "-en"], "children (-n after a vowel)"),
    "aelthar": (["ael", "thar"], "bond-blood: the rite"), "aelvaren": (["ael", "varen"], "the Bearer of the Binding"),
    "aelrhen": (["ael", "rhen"], "bond-to-stone, a who-is name"), "naelear": (["nael", "-ear"], "those of the breath"),
    "naelsaen": (["nael", "saen"], "mist-hearts"), "rhenear": (["rhen", "-ear"], "those of stone"),
    "saenvael": (["saen", "vael"], "heart-grain: the Heartwood"), "sethvaren": (["seth", "varen"], "the Standard-Bearer"),
    "aelralen": (["ael", "ralen"], "the root-bond"), "leathae": (["lea", "thae"], "the Hasty Tide"),
    "vaelthae": (["vael", "thae"], "the Second Tide"), "ralenthae": (["ralen", "thae"], "the Tide of Remembering"),
    "aelthae": (["ael", "thae"], "the Joined Tide"), "rhenthae": (["rhen", "thae"], "the Tide that Learned Deceit"),
    "eirthae": (["eir", "thae"], "the Last Tide"), "thaesaen": (["thae", "saen"], "tide-heart"),
    "leavaren": (["lea", "varen"], "bearer of new branches"), "vaelress": (["vael", "ress"], "the grain that rots"),
    "ralensaen": (["ralen", "saen"], "root-heart"), "rhenvael": (["rhen", "vael"], "stone-grain"),
    "senneir": (["senn", "eir"], "the deep-beneath"), "eirlenth": (["eir", "lenth"], "the long winter"),
    "naelthar": (["nael", "thar"], "blood of the sky"), "neivaere": (["nei", "vaere"], "the silvered"),
    "seilrhass": (["seil", "rhass"], "bough-thunder: the spoken tongue"), "eilseth": (["eil", "seth"], "ring-carving: the grain"),
    "theinas": (["thein", "-as"], "a knowing"), "naelenn": (["nael", "enn"], "home"), "naelea": (["nael", "-ea"], "a Mystaeri"),
    "aethea": (["aeth", "-ea"], "a shore-man"), "aethear": (["aeth", "-ear"], "the shore-men"), "rhenea": (["rhen", "-ea"], "one of stone"),
    "ralthein": (["ral", "thein"], "to remember, 'root-hold'"), "raltheinas": (["ralthein", "-as"], "a memory"),
    "aelthein": (["ael", "thein"], "to trust"), "leathein": (["lea", "thein"], "to learn"), "theineth": (["thein", "-eth"], "to teach"),
    "reith": (["rei", "-eth"], "to send"), "neaseth": (["neas", "-eth"], "to show"), "renneth": (["renn", "-eth"], "to goad"),
    "rheileth": (["rheil", "-eth"], "to silence"), "veaseth": (["veas", "-eth"], "to kill"), "aelress": (["ael", "ress"], "grief"),
    "rhenseth": (["rhen", "seth"], "a lie"), "rennrhen": (["renn", "rhen"], "a gun"), "rhenneas": (["rhen", "neas"], "the reach"),
    "rhenrhass": (["rhen", "rhass"], "a stone-breaker"), "ennas": (["enn", "-as"], "a dwelling"), "rhenennas": (["rhen", "ennas"], "a castle"),
    "eithseil": (["eith", "seil"], "straw"), "ressveir": (["ress", "veir"], "worthless wood"), "isseil": (["iss", "seil"], "thin wood"),
    "rhannseil": (["rhann", "seil"], "the great hull"), "thannvinn": (["thann", "vinn"], "the kept hand"),
    "issralen": (["iss", "ralen"], "root-men"), "rhasseil": (["rhass", "seil"], "the ram"), "leasen": (["leas", "-en"], "the swift"),
    "thavalen": (["thaval", "-en"], "the hunters"), "thavalea": (["thaval", "-ea"], "a hunter"), "seilen": (["seil", "-en"], "the host"),
    "neivath": (["nei", "vath"], "silverbark"), "neivathen": (["neivath", "-en"], "the council"), "thaelen": (["thael", "-en"], "a grove"),
    "leathael": (["lea", "thael"], "a sapling"), "naelneis": (["nael", "neis"], "the between-light"), "eirrhen": (["eir", "rhen"], "the mountain"),
    "esthas": (["esth", "-as"], "ash"), "rhithveir": (["rhith", "veir"], "timber"), "rhithas": (["rhith", "-as"], "the felling"),
    "tharear": (["thar", "-ear"], "kin"), "ralear": (["ral", "-ear"], "forebears"), "eirea": (["eir", "-ea"], "an elder"),
    "aelea": (["ael", "-ea"], "a guest"), "vethea": (["veth", "-ea"], "a host"), "rhesea": (["rhes", "-ea"], "an enemy"),
    "rhesear": (["rhes", "-ear"], "enemies"), "sethea": (["seth", "-ea"], "a carver"), "eirsethea": (["eir", "sethea"], "the Last Carver"),
    "leisthein": (["leis", "thein"], "to hope"), "lelneis": (["lel", "neis"], "blossom"), "eirveir": (["eir", "veir"], "Myststone"),
    "leaveir": (["lea", "veir"], "green wood"), "eilen": (["eil", "-en"], "all; always"), "rheissae": (["rheis", "sae"], "east"),
    "rheisnenn": (["rheis", "nenn"], "west"), "lennves": (["lenn", "ves"], "north"), "rhesves": (["rhes", "ves"], "south"),
    "vannrenn": (["vann", "renn"], "a feint"), "sathneth": (["sath", "neth"], "a turning for home"), "reaslel": (["reas", "lel"], "a sail"),
    "naelseth": (["nael", "seth"], "a hidden thing"), "eisranth": (["eis", "ranth"], "a soft reading"),
    "rhelranth": (["rhel", "ranth"], "the soft letters"), "vannea": (["vann", "-ea"], "the second"),
    "naelsaenen": (["naelsaen", "-en"], "the pillars"),
    "raltheine": (["ralthein", "-e"], "remembers: Ve raltheine, 'we remember'"),
    "eisse": (["eiss", "-e"], "is (so)"),
}
