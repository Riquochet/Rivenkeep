import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
need=json.load(open(S+'/gloss_in/S09.json'))
G={}
def g(i,*parts):
    out=[]
    for p in parts: out+= [w.strip() for w in p.split('|')]
    G[i]=out
g(0,"Mirror|in|Grain")
g(1,"summer|fourth|spring|fifth|and|winter|sixth")
g(2,"(past)|I laid|it|Seren|Two|Inks|in|three|courses|each|course|in|the|night|that|(past)|was|the|carving|known",
    "in|the|three|(past)|I held|the|lamp|on|the|shingle|and|is|the|lamp|this|it")
g(3,"Course|First|Three|Roads|One|Hour")
g(4,"hold!|the|stone|Seren")
g(5,"by|course|the|night|short|that|(past)|they knocked|the|drums|in|the|grey|like|mallets|in|quarry|far",
    "by|its|course|(past)|they two sat|Enno|and|Della|in|their (two)|house|one|door",
    "(past)|rested|mark|Enrella (the two)|in|low|its|stone|first",
    "(past)|set|Enno|the|chisel|and|(past)|struck|Della",
    "(past)|stood|it|one|course|high|high|than|that|never")
g(6,"hand|in|hand|(past)|they two came in|they two|into|the|courtyard|that|in|what|(past)|I came in|alone")
g(7,"in|the|dawn|(past)|came|the|fleet|by|three|roads|in|one|hour|and|(past)|broke|it|the|wall|at|east|and|at|north",
    "(past)|was|every|pair|bonded|in|breach|and|(past)|were|breaches|still",
    "Orvenna (the two)|master-pair|the|wall|who|not|they two cry out|ever",
    "(past)|they two built|they two|mute|something|that|not|(past)|they built|masters|ever|before")
g(8,"(past)|they two sent|Orvenna (the two)|pair|from|other")
g(9,"(past)|gave|Ormund|the|breach|eastern|to|Enno|and|(past)|gave|Penna|the|north|to|Della",
    "at|head|the|stair|(past)|called|Enno|over|his|shoulder|it is|like|one|man",
    "and|(past)|threw|Della|the|rest|to-him|in|running|with|four|hands|and|none|other|for|blaming")
g(10,"are|the|Bonded|from|other|few|times|and|far|never|is|far|four hundred|paces|wall")
g(11,"in|east|(past)|took|shot|the|wall|and|Enno|with-it|not|(past)|I saw|it|(past)|saw|Hale")
g(12,"at|north|(past)|I was|at|shoulder|Della|and|the|mortar|with-me",
     "(past)|turned|she|the|stone|last|for|cutting|the|mark|in|its|low",
     "(past)|set|she|herself|the|chisel|and|(past)|struck|she|and|not|(past)|shook|the|hand")
g(13,"from|that|(past)|stopped|the|mallet|in|the|air|in|the|hand")
g(14,"(past)|looked|she|to|east|from|that|(past)|bent|she|again|and|(past)|cut|she|the|stroke|last",
     "and|(past)|laid|she|the|chisel|at|shoulder|the|mark|and|(past)|lay down|she|face|on|stone")
g(15,"(past)|I put|the|finger|great|on|the|mortar|as|they lay|masons|not|(past)|set|it|yet")
g(16,"(past)|went out|she")
g(17,"(past)|came|Hale|in|running|and|the|word|from|east|with-him|and|not|(past)|said|he|it",
     "not|(past)|came|runner|late|ever")
g(18,"in|inscriptions|year|not|is|mark|other|that|(past)|finished|one|hand|it",
     "in|dusk|(past)|I sought|time|long|the|stroke|that|(past)|cut|Della|alone")
g(19,"mark|Enrella (the two)|whole|on|underside|the|stone|northern|as|(past)|saw|Seren|it|by|the|light|last")
g(20,"not|is|knowing|at-you")
g(21,"at|nightfall|(past)|carried|Stannard|Enno|four hundred|paces|whole|and|(past)|laid|he|him|at|her|shoulder",
     "with|their (two)|four|hands|own|(past)|they two laid|Orvenna (the two)|the|stone|northern|over-them-two|the|mark|to|low",
     "(past)|they two prayed|Idrenna (the two)|who|(past)|they two sealed|Enrella (the two)|over-it|in|two|halves")
g(22,"God|(past)|you bonded|both|into|one|while|not|(past)|they two breathed|they two|yet")
g(23,"(past)|was|one|cradle|at-them-two|from-you|and|one|stone|from-us|and|not|you part|them two")
g(24,"over|the|stone|(past)|laid|Ormund|the|stone|first|in|the|jest|old|and|(past)|laid|Penna|the|capstone|on-it",
     "from|that|(past)|bound|the|Captain|piece|from|his|cloak|on|pike|over-them-two|the|first|to|Stonewrights",
     "and|were|his|company|they two",
     "(past)|stood|Kael|at|shoulder|and|(past)|counted|he|them two")
g(25,"one|(past)|said|he")
g(26,"at|turning|the|tide|(past)|came in|plank|the|standard-bearer",
     "(past)|went|Rhyna|to|low|to-it|and|(past)|I went|at|her|shoulder|and|the|lamp|with-me",
     "on|the|wall|in|high|in|what|(past)|knelt|Enno|(past)|mended|Halvard|the|breach|while|(past)|they sang|the|masons|Two|at|Gate",
     "(past)|took|no one|the|voice|first|in|front|the|comma|or|in|far",
     "at|the|line|second|(past)|came in|the|rest|as|if|(past)|was|the|first|sung")
g(27,"(past)|laid|Rhyna|hand|on|the|grain|and|(past)|went pale|she",
     "in|high|(past)|went pale|Halvard|in|one|breath|and|the|trowel|in|his|hand",
     "(past)|came|he|to|low|and|(past)|they two told|they two|it|order|the|fleet|whole|ship|bonded|to|ship")
g(28,"time|long|(past)|they two were|silent|(past)|I asked|what|(past)|was|harm|on-them-two|but|I think|(past)|I knew|it")
g(29,"like|this|we build|wall")
g(30,"waits|the|one|for|stroke|the|other|and|not|is|need|telling|on-him")
g(31,"(past)|named|the|carving|the|Tide|that|Aelthae|night|that|(past)|I knew|the|half|first",
     "Ael|(past)|I wrote|it|one|time|in|the|Ael'thar|(past)|I wrote|the|name|and|not|I write|what|(past)|I thought")
g(32,"on|trowel|Halvard|(past)|was|the|mortar|in|setting")
g(33,"I lay|it|as|(past)|was|laid|to-me")
g(34,"and|(past)|said|the|hearth|we-remember")
g(35,"Course|Second|What|(past)|We Taught|To-Them")
g(36,"in|spring|in|morning|grey|(past)|ran|fleet|on|the|wall|in|the|way|old|every|ship|alone|and|loud|and|true",
     "from|that|(past)|laughed|the|wall|whole|and|(past)|spoke|every|gun|on-it|battery|Pellow|in|heart|the|rest")
g(37,"Pellow|spire|the|young|very|(past)|were|two|words|at-him|for|men|the|wall|every|one")
g(38,"look!|near")
g(39,"what|(past)|came|from|that|is|it|at-me|from|Hale",
     "when|(past)|they spoke|his|guns|(past)|carried|Pellow|the|glass|to|high|and|(past)|went pale|sail|in-it",
     "from|that|the|second|from|that|the|third")
g(40,"are not|green|they")
g(41,"(past)|ran|Hale|it",
     "in|his|back|(past)|turned|Pellow|his|guns|to|the|grey|unbidden|and|(past)|stood|he|on|the|capstone|wall|and|the|glass|with-him")
g(42,"(past)|went|the|Captain|by|course|the|wall|and|at|shoulder|True Man|every|one|(past)|called|he|shift!|your|ground",
     "not|(past)|hurried|he|as|not|hurries|kindler|or|dies|the|fire")
g(43,"out of|the|grey|(past)|they came|the|hunters|to|the|guns|that|(past)|they spoke|every|one|and|not|(past)|they went|from-them",
     "(past)|lived|every|battery|that|(past)|arrived|he|to-it|is|slow|one|and|one")
g(44,"was|the|far|very|from-him|battery|Pellow|and|the|near|very|to|the|grey",
     "to-it|(past)|they came|first|and|(past)|stood|it|in|their|face|alone|not|(past)|hurried|the|Captain")
g(45,"(past)|lay|Pellow|dead|at|the|capstone|wall")
g(46,"(past)|lay|the|glass|by|his|hand|and|was|whole|it")
g(47,"at|turning|the|tide|(past)|they two laid|Halyna (the two)|hand|on|plank|the|fleet|that")
g(48,"in|its|low|(past)|was|carved")
g(49,"not|is|lying|at|the|wood|(past)|I said|and|from|that|(past)|I saw|it",
     "not|lies|the|wood",
     "(past)|was|it|commanded|to|laying|lie|in|our|mind|and|(past)|obeyed|it")
g(50,"(past)|they learned|it|from-us")
g(51,"(past)|we taught|it|to-them|with|the|guns|silent|every|one")
g(52,"not|(past)|was|word|for|lie|at-them",
     "(past)|we gave|one|to-them",
     "in|the|carving|that|(past)|was|their|word|for-us|carved|small|Rhenear|the|stone-deaf")
g(53,"in|dusk|(past)|we raised|cairn|Pellow|and|(past)|bound|the|Captain|piece|over-it",
     "from|that|(past)|gave|he|the|glass|to|Hale|and|the|battery|with-it")
g(54,"am not|True Man|I|(past)|said|Hale|I run")
g(55,"from|that|(past)|they went|to|Ruan|spire|his|corporal|and|(past)|raised|the|Captain|True Man|from-him",
     "(past)|put|he|the|glass|to|the|eye|and|(past)|looked|he|in|far|the|cairn")
g(56,"look!|near|(past)|said|he")
g(59,"Course|Third|Plan|That|(past)|Carved|Defeat|On-It|Itself")
g(60,"in|snow|to|the|knee|(past)|came|standard-bearer|and|morrow|whole|carved|in|its|heart",
     "(past)|we sank|it|in|front|noon|and|(past)|brought|the|tide|the|heart|to|the|shingle")
g(61,"was|knowing|long|very|it|that|(past)|they two held|Halyna (the two)|ever",
     "two|times|(past)|I filled|the|lamp|while|not|(past)|they two told|they two|it|whole|yet|and|in|its|end|(past)|was|thing|this")
g(62,"(past)|they carved|defeat|on-them|themselves|in|the|plan")
g(63,"there is|one|hand|in|the|carving|that|whole|and|is not|hand|council|it")
g(64,"and|is|young|the|hand")
g(65,"but|was|the|two|words|last|that|(past)|held|us",
     "not|(past)|knew|the|wood|young|home|but|as|the|place|in|what|runs|thing|hurt",
     "in|this|(past)|was|it|carved|as|(past)|was|meant")
g(66,"(past)|we looked|we|three|one|on|other|across|the|lamp|as|looks|wife|to|high|when|asks|husband|in|fever|long|his|boots")
g(67,"they carve|morrow|when|this|as|we carve")
g(68,"from|that|(future)|we will build|morrow|that|not|(past)|they carved|for-it")
g(69,"(past)|went out|the|lamp|on|the|shingle|and|not|(past)|I filled|it|time|third")
g(72,"Homecomings")
g(73,"year|the|homecomings|at|ten|fires")
g(74,"(past)|they laid|the|True Men|it|at|the|fire|in|each|one|from|the|havens|in|the|night|that|(past)|fell|the|Seat|Great|in-it",
     "(past)|I set|each|one|at|its|shoulder",
     "(past)|laid|Kael|the|words|first|and|the|words|last|at|the|hearth|this|when|(past)|was|the|tenth|in|home",
     "and|(past)|counted|he|the|Book|that|(past)|I wrote|in|front|his|stone|first")
g(75,"give!|the|stone|to-me|not|I sit|(future)|I will stand")
g(76,"at|end|the|winter|(past)|we went|to|low|by|course|the|roads|old|over|the|mountains",
     "the|True Men|and|their|troops|in|front|the|masons|in|back",
     "by|course|the|road|whole|(past)|ran|water|the|snow|at|our|shoulder",
     "in|every|one|from|the|havens|(past)|sat|Seat|Great|in|heart|the|walls|fallen|and|(past)|waited|it")
g(77,"at|the|hearth|this|(past)|swore|each|one|from-us|upon|the|haven|that|(past)|was|at-him",
     "am|oath-keeper|I|and|(past)|I held|the|ten|whole",
     "in|what|(past)|was|man|fallen|(past)|spoke|another|at|his|seat")
g(78,"when|this|hear!|names|the|havens|and|hold!|them|from|what|they are|at-us|again")
g(79,"Harbour|Old")
g(80,"Voss|at|seat|Corlen")
g(81,"at|this|(past)|were|walls|first|the|havens|laid|and|at|this|they stand|again",
     "(past)|sank|Heart|Tide|into|the|sea|that|(past)|came|it|from-it|and|not|(past)|rose|it",
     "who|is|need|on-him|bringing|the|boat|first|to|home",
     "on|Corlen",
     "lies|he|in|low|the|cairns|eastern",
     "from|that|(past)|came|the|boat|into|my|hand")
g(82,"(past)|I held|finger|wet|to|high|as|(past)|held|he|but|(past)|told|the|wind|nothing|to-me",
     "(past)|I brought|it|to|harbour|at|tide|the|evening|slow",
     "from|that|(past)|I waited|as|(future)|will wait|he|until|finishing|the|sea")
g(83,"on|the|quay|(past)|stood|house|my|grandmother|and|not|(past)|was|roof|at-it",
     "in|high|the|hearth|cold|(past)|were|the|three|stones|flat|grey|in|the|wall|still",
     "and|the|stone|low|very|marked|in|what|(past)|they knocked|the|ship-masters|pipes",
     "they are|in|my|pack|night|this",
     "(past)|they hung|time|enough|in|high|fire|dead")
g(84,"and|(past)|said|the|hearth|we-remember")
g(85,"Meeting|Tide")
g(86,"Tamm|three|spans")
g(87,"(past)|were|three|heads|at-it|and|(past)|we struck|the|three|in|the|one|holding|and|(past)|came back|none",
     "in|what|(past)|stood|the|span|in|middle|the|three|(past)|went|Bearer|Branches|New|to|low",
     "on|the|bank|(past)|I set|the|three|stones|at-me|in|line|as|at|shoulder|my|blanket|every|night|the|war",
     "is|plank|one|span|is|city|three")
g(89,"Fenholm")
g(90,"Marl|fen-born")
g(91,"(past)|we said|every|time|town|nothing|but|course|last|on|the|course|old",
     "night|this|(past)|we said|again|and|(past)|we laughed",
     "like|log|rotted|(past)|went|Grain|That|Rots|to|low|into|the|fen|and|(past)|went|the|rot|out of|our|mortar",
     "(past)|carried|my|grandmother|course|last|our|house|out of|the|fen|on|her|back|and|(past)|died|she|and|not|(past)|was|it|in|home|yet",
     "(past)|I laid|the|stone|at-her|on|the|course|old|as|(past)|bade|she|to-me",
     "if|(past)|you asked|her|(question)|(future)|will stand|it|(future)|will answer|she|perhaps")
g(92,"not|(past)|sank|it")
g(93,"and|at|the|fire|that|(past)|waited|the|hearth|breath|Ebba")
g(95,"Holtward")
g(96,"Aske|roof|forest")
g(97,"in|heart|the|trees|(past)|we found|Heart|Root|in|standing|still",
     "(past)|laid|it|its|roots|and|not|(past)|it rose",
     "were|trees|they|one|time|(past)|I said|to|my|troop",
     "hold!|your|hand",
     "not|(past)|was|axe|raised",
     "(past)|we left|it|in|standing",
     "(past)|came back|it|to|home")
g(99,"Hold|Cairns")
g(100,"Garvel|smithies")
g(101,"(past)|was|Hold|Cairns|that|(past)|rang|all|day|quiet",
      "stone|into|stone|(past)|crumbled|Grain|Stone|and|(past)|they took|cairns|the|quarrymen|first|it",
      "in|smithy|cold|(past)|I struck|the|anvil|one|time|for|its|hearing",
      "(past)|rang|the|anvil|true",
      "is not|gun|the|thing|first|that|(future)|I will make|on-it")
g(103,"Harbour|Fire")
g(104,"Harl|Shore|that|burns")
g(105,"(past)|went|our|mason|to|low|to|the|crust|black|in|what|(past)|went out|Burning|like|smithy|untended",
      "on-it|(past)|laid|he|his|plank|charred|the|plank|that|(past)|said|burn!")
g(106,"not|(past)|I burned|it")
g(108,"Sandreach")
g(109,"Ulden|galleries")
g(110,"one|hour|(past)|shook|the|canyon|when|(past)|burst|Deep|in|low|to|high|in|low|the|keep|eastern|and|(past)|broke|it|itself",
      "when|(past)|was|it|still|(past)|I went|to|low|to|the|gallery|low|very|and|(past)|I laid|ear|on|the|ground",
      "(past)|I heard|nothing",
      "night|this|I sleep|in|low|my|roof|of stone|own")
g(112,"Rimewatch")
g(113,"Kael|at|seat|Hesk")
g(114,"city|man|other|not|I lay|it|city|this|is|need|on-me")
g(115,"by|course|the|morning|that|(past)|lay|the|mere|white|and|in|the|white|(past)|waited|Winter|Long")
g(116,"(past)|stood|Hesk|on|the|shore|and|lamp|his|mother|lit|in|his|hand|at|light|the|day",
      "six|winters|(past)|lit|he|it|in|dusk|on|our|wall|northern|and|(past)|guided|it|the|night-watch")
g(117,"in|front|noon|(past)|went|he|alone|on|the|ice",
      "from|the|shore|(past)|I counted|steps|Hesk",
      "at|ten|twenties|and|twelve|(past)|stopped|he|in|what|(past)|stood|the|hall|great",
      "(past)|spoke|the|ice|in|his|low|as|(past)|spoke|it|in|the|night|that|(past)|carried|he|the|lamp|that|out of|Rimewatch")
g(118,"night|that|(past)|held|it")
g(119,"in|noon|(past)|rose|the|white|and|(past)|took|the|ice|Winter|Long|to|low")
g(120,"and|(past)|took|the|ice|Hesk")
g(121,"in|dusk|(past)|we went|by|course|the|crack|and|ropes|with-us|and|(past)|we found|his|lamp|on|the|ice|in|burning",
      "I swear|upon|that|it stands")
g(122,"(past)|came back|Hesk|to|home")
g(124,"laid|in|hand|Seren|at|the|Keep|night|that|not|(past)|burned|lamp|on|the|wall|northern",
      "from|that|(past)|set|girl|fisher-folk|one|at|that|and|(past)|lit|she|it|and|(past)|said|she|is|need|tending|lamp|on|someone")
g(125,"Tower|Sky")
g(126,"Lanner|crags")
g(127,"(past)|went|Blood|Sky|to|low|out of|its|cloud|and|not|(past)|went|it|to|high|again",
      "from|that|(past)|I climbed|the|crag|high|as|(past)|I said|and|(past)|I whistled|to|the|wind",
      "(past)|came|the|wind|not|(past)|brought|it|one|sail")
g(129,"Glasspire")
g(130,"Ruan|at|seat|Pellow")
g(131,"in|dark|the|cellars|(past)|broke|Silvered|like|mirror|and|(past)|we saw|in|every|piece|from-it|the|lamps|that|(past)|we brought|we|ourselves",
      "(future)|will see|Pellow|it|first",
      "is|glass|Pellow|at-me",
      "(past)|I looked|near|and|(past)|I sought|him")
g(133,"from|that|(past)|laid|Kael|his|hands|on|the|stone|time|second")
g(134,"night|this|in|the|ward|(past)|I called|the|names",
      "fourteen|names|and|eleven|for|answering",
      "at|name|Corlen|(past)|was|the|ward|quiet|one|breath|and|at|name|Pellow",
      "at|name|Hesk|(past)|was|lamp|lit|on|the|wall|northern|and|not|(past)|came|answer|to|low")
g(135,"not|is|haven|at-me|from|what|(past)|found|the|Captain|me|by|road",
      "year|this|(past)|I sat|at|ten|fires",
      "at|fire|every|one|when|(past)|came|the|answer|was|the|hearth|this|that|(past)|I heard",
      "every|one|from|the|havens|is|Keep|Riven|it|I swear|upon|that|it stands")
g(136,"ten|havens|(past)|I counted|them|two|times|and|was not|long")

out=[];seen={};errs=0
for i,r in enumerate(need):
    words=[w for w,_ in r['draft']]
    if r['rom'] in seen:
        j=seen[r['rom']]
        if i in G and G[i]!=G[j]: print('DUP MISMATCH',i,j)
        continue
    if i not in G:
        print('MISSING',i,r['rom'][:60]); errs+=1; continue
    gl=G[i]
    if len(gl)!=len(words):
        print('LEN',i,len(gl),len(words))
        for k in range(max(len(gl),len(words))):
            print('   ',words[k] if k<len(words) else '--', '=', gl[k] if k<len(gl) else '--')
        errs+=1; continue
    seen[r['rom']]=i
    out.append({'rom':r['rom'],'gloss':[[w,e] for w,e in zip(words,gl)]})
extra=set(G)-set(range(len(need)))
if extra: print('EXTRA',extra)
json.dump(out,open(S+'/gloss/S09.json','w'),ensure_ascii=False,indent=1)
print('rows',len(out),'errs',errs)
