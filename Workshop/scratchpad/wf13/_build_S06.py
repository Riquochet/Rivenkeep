import json
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
need = json.load(open(S + '/gloss_in/S06.json'))

P = '(past)'
F = '(future)'
Q = '(question)'
HAL = 'Halyna (the two)'
WEN = 'Wendhessa (the two)'

G = {}
G[0] = ['Felling', 'the', 'Pillars', 'Black']
G[1] = ['the', 'spring', 'second', 'in', 'Tide', 'Second']
G[2] = [P, 'laid', 'Seren', 'Two', 'Inks', 'from', 'rolls', 'the', 'guild', 'about', 'the', 'Harvest',
        P, 'they two read', HAL, 'them', 'to-me', 'in', 'nights', 'and', P, 'I wrote', 'from-them-two', 'fast', 'very',
        P, 'they leaned', 'my', 'letters', 'like', 'grass', 'in', 'wind']
G[3] = ['hold!', 'the', 'stone', 'Seren']
G[4] = [P, 'we read', 'one', 'year', 'when', 'in', 'night', 'that', P, 'went soft', 'the', 'ice', P, 'we came', 'to',
        'bottom', 'chest', 'archive',
        P, 'was', 'rope', 'the', 'roll', 'old', 'very', 'rotted', 'and', P, 'broke', 'it', 'at', 'fingers', 'Rhyna',
        'not', P, 'they two read', HAL, 'one', 'line', 'in-it', 'to-me', 'yet', 'first', P, 'I wrote', 'this']
G[5] = ['not', P, 'we two lived', 'it']
G[6] = ['but', P, 'they lived', 'fathers', 'our', 'fathers', 'it', P, 'they wrote', 'it', 'and', 'not', P, 'they read',
        'ever', 'thing', 'that', P, 'they wrote']
G[7] = ['in', 'roll', 'old', 'very', 'is', 'the', 'grey', 'written', 'like', 'veil', 'blackish', 'in', 'edge', 'the',
        'sea', 'and', 'nothing', 'other',
        'from', 'that', 'is', 'question', 'it', 'which', P, 'they asked', 'in', 'night-watches', 'and', 'which', P,
        'answered', 'no one', 'ever', 'what', 'was', 'it', 'and', 'who', P, 'breathed', 'it',
        'when', P, 'came', 'the', 'answer', 'not', P, 'was', 'it', 'written', 'in', 'our', 'hand']
G[8] = ['from', 'that', P, 'came', 'heart', 'summer', 'when', P, 'was', 'pride', 'upon', 'the', 'havens',
        P, 'they went', 'the', 'ships', 'to', 'far', 'in', 'what', 'not', P, 'they dared', 'their', 'fathers', 'and',
        'in', 'edge', 'the', 'grey', P, 'they found', 'the', 'pillars', 'black', 'in', 'their', 'ranks', 'plumb', 'as',
        'plumb-line',
        P, 'they named', 'the', 'ship-masters', 'them', 'Posts', 'Grey', 'from', 'what', P, 'they held', 'the', 'grey',
        'to', 'high', 'as', P, 'they seemed', 'as', 'they hold', 'posts', 'roof',
        P, 'was', 'the', 'wood', 'black', 'hard', 'than', 'oak', 'and', 'light', 'than', 'iron', 'and', P,
        'warded off', 'it', 'rot']
G[9] = ['by', 'course', 'two', 'generations', P, 'sent', 'Council', 'Trade', 'the', 'axes', 'to', 'far',
        'they keep', 'the', 'rolls', 'the', 'count', 'cargo', 'and', 'cargo',
        'hear!', 'it', 'when', 'this', 'and', 'hold!', 'it', 'from', 'what', 'is', 'it', 'at-us']
G[10] = ['wood', 'black', 'for', 'buttresses', 'and', 'bridges',
         'wood', 'black', 'for', 'three', 'spans', 'in', 'Meeting', 'Tide', 'and', 'for', 'pilings', 'Fenholm',
         'wood', 'black', 'for', 'roof-trees', 'Holtward', 'and', 'for', 'cranes', 'Tower', 'Sky',
         'wood', 'black', 'for', 'galleries', 'Sandreach', 'and', 'for', 'hall', 'on', 'the', 'ice', 'at', 'Rimewatch',
         'wood', 'black', 'burned', 'slow', 'in', 'forges', 'Harbour', 'Fire',
         'and', 'in', 'Hold', 'Cairns', P, 'they were', 'the', 'axes', 'hammered', 'and', P, 'they went back', 'to',
         'edge', 'for', 'cutting', 'more']
G[11] = ['from', 'that', 'the', 'things', 'that', 'not', P, 'they needed', 'thing', 'like', 'that']
G[12] = ['wood', 'black', 'for', 'floor', 'dancing-hall', 'lord', 'Harbour', 'Old']
G[13] = ['wood', 'black', 'for', 'trade-tables', 'the', 'harbour-houses', 'and', 'their', 'dice-boards']
G[14] = ['at', 'this', 'is', 'the', 'roll', 'stained', 'and', 'are', 'three', 'lines', 'lost']
G[15] = ['at', 'end', 'very', P, 'hewed', 'merchant', 'in', 'Meeting', 'Tide', 'one', 'pillar', 'into', 'one', 'bed']
G[16] = [P, 'slept', 'he', 'in-it', 'and', P, 'was', 'pride', 'on-him']
G[17] = [P, 'turned', 'Halvard', 'the', 'leaf', 'and', P, 'went back', 'he', 'to', 'it']
G[18] = ['they keep', 'the', 'rolls', 'count', 'another', 'at', 'shoulder', 'that', 'strange', 'than-it',
         'in', 'what', P, 'was', 'pillar', 'felled', P, 'rose', 'new growth', 'from', 'the', 'stump', 'plumb', 'and',
         'black',
         P, 'they went back', 'the', 'axemen', 'to', 'cutting', 'it', 'from', 'what', P, 'they came', 'poles', 'good',
         'from-it', 'and', P, 'bought', 'the', 'guild', 'them', 'for', 'scaffold']
G[19] = [P, 'they cut', 'it', 'and', P, 'grew', 'it',
         P, 'they cut', 'it', 'and', P, 'grew', 'it',
         P, 'they cut', 'it']
G[20] = ['in', 'low', 'count', 'poles', P, 'stopped', 'finger', 'Rhyna',
         P, 'wrote', 'clerk', 'one', 'line', 'more', 'small', 'very', 'two', 'times', P, 'I bent', 'the', 'lamp', 'to',
         'it', 'and', 'from', 'that', P, 'read', 'she', 'it']
G[21] = ['by', 'course', 'the', 'edge', 'whole', P, 'rose', 'nothing', 'from', 'the', 'stumps']
G[22] = [P, 'wrote', 'no one', 'from', 'what', 'and', P, 'asked', 'no one',
         'not', P, 'said', 'the', 'roll', 'who', 'was', 'the', 'hand',
         'if', P, 'said', 'it', F, 'I will keep', 'name', 'the', 'hand']
G[23] = ['time', 'and', 'time', P, 'thinned', 'the', 'grey', 'and', P, 'named', 'the', 'Council', 'it', 'fortune',
         P, 'I tried', 'the', 'word', 'that', 'in', 'low', 'my', 'tongue', 'and', 'not', P, 'held', 'it', 'like',
         'sand', 'from', 'mortar', 'old']
G[24] = [P, 'warned', 'the', 'Stonewrights', 'the', 'Council',
         'is', 'it', 'in', 'our', 'hand', 'own', 'on', 'leaf', 'that', 'not', P, 'was', 'dark', 'from', 'fingers',
         'ever']
G[25] = ['they grow', 'the', 'trees', 'these', 'in', 'soil', 'strange',
         'they bear', 'the', 'carvings', 'that', 'we find', 'at', 'their', 'shoulder', 'tongue', 'that', 'not', 'is',
         'reading', 'at-us',
         'in', 'what', 'absent', 'wisdom', 'restraint', 'our', 'guide']
G[26] = ['but', 'already', P, 'sat', 'trade', 'in', 'seat', 'great', 'and', P, 'was', 'our', 'counsel', 'like',
         'thing', 'that', 'they say', 'grandmothers', 'by', 'the', 'fire',
         'one', 'time', P, 'was', 'the', 'warning', 'read', 'in', 'voice', 'in', 'council-hall', 'Harbour', 'Old',
         'from', 'that', P, 'they laid', 'it', 'on', 'shelf']
G[27] = ['from', 'what', P, 'were', 'carvings',
         'at', 'feet', 'the', 'pillars', P, 'they found', 'the', 'axemen', 'stones', 'laid', 'plumb', 'cut', 'in',
         'signs', 'curled', 'beautiful', 'as', 'frost', 'on', 'window',
         P, 'was', 'reading', 'at', 'no one']
G[28] = [P, 'they hung', 'some', 'in', 'harbour-houses', 'turned', 'to', 'ornament',
         P, 'they drank', 'men', 'in', 'low', 'the', 'stones', 'and', P, 'they reckoned',
         P, 'locked', 'the', 'guild', 'the', 'rest', 'in', 'archives', 'and', 'the', 'warning', 'own', 'with-them']
G[29] = ['they lie', 'some', 'from-them', 'at', 'knee', 'in', 'the', 'chest', 'that', P, 'I carried', 'to', 'high',
         'the', 'mountain',
         P, 'they two laid', HAL, 'four', 'hands', 'on-them', 'and', P, 'they gave', 'nothing', 'to-them-two',
         'not', 'is', 'translating', 'at', 'stone']
G[30] = ['in', 'heart', 'counts', 'one', 'summer', 'late', P, 'found', 'Halvard', 'letter', 'from', 'the', 'outpost',
         'outer', 'very',
         P, 'wrote', 'clerk', 'it', 'in', 'mortar', 'count', 'poles', 'and', 'count', 'oars', 'in', 'one', 'tending',
         P, 'read', 'Halvard', 'it', 'as', P, 'read', 'he', 'the', 'oars']
G[31] = ['stranger', 'unknown', 'intent', 'hostile', 'stopped', 'vessel', 'burned', 'and', 'loosed']
G[32] = ['at', 'its', 'foot', 'is', 'name', 'cut',
         P, 'laid', 'Rhyna', 'her', 'finger', 'on', 'the', 'blot', 'and', P, 'took', 'she', 'it', 'from-it']
G[33] = ['on', 'the', 'leaf', 'next', 'are', 'two', 'boats', 'the', 'wood', 'black', 'cut', 'from', 'list', 'cargo',
         'and', 'at', 'their', 'shoulder', 'in', 'one', 'hand', 'lost', 'in', 'edge']
G[34] = [P, 'I wrote', 'it', 'as', P, 'wrote', 'the', 'clerk', 'it', 'in', 'mortar', 'the', 'poles', 'and', 'the',
         'oars']
G[35] = ['not', P, 'I knew', 'what', P, 'I held']
G[36] = ['was not', 'wisdom', 'that', P, 'stopped', 'the', 'Harvest', 'but', 'fickleness', 'men',
         P, 'they were', 'the', 'pillars', 'near', 'scarce', 'and', P, 'they gave', 'hills', 'the', 'north', 'wood',
         'more', 'cheap',
         'from', 'year', 'the', 'boat', 'that', 'burns', 'not', P, 'wanted', 'one', 'crew', 'rowing', 'in', 'sight',
         'the', 'grey', 'and', 'not', P, 'they said', 'the', 'rolls', 'from', 'what',
         'from', 'that', P, 'they stopped', 'the', 'axes',
         P, 'decided', 'no one', 'it']
G[37] = ['from', 'that', P, 'they forgot', 'the', 'havens',
         'in', 'high', 'the', 'ale', 'and', 'the', 'dice', P, 'they hung', 'the', 'stones', 'still', 'and', P,
         'they asked', 'children', 'what', 'they say', 'they', 'and', P, 'was', 'said', 'to-them', 'nothing',
         'were', 'the', 'children', 'those', 'some', 'from-you', 'who', 'you sit', 'at', 'the', 'fire', 'this']
G[38] = ['late', 'late', 'very', P, 'turned', 'wheel', 'pride',
         P, 'they were', 'houses', 'God', 'mended', 'and', P, 'they climbed', 'men', 'our', 'steps', 'worn', 'again',
         'for', 'asking', 'counsel', 'glad', 'as', 'men', 'who', 'they mend', 'wall', 'sea', 'in', 'calm',
         P, 'asked', 'no one', 'about', 'the', 'stones', 'and', P, 'we said', 'nothing',
         'was', 'we', 'who', P, 'we turned', 'the', 'key',
         'is', 'our', 'share', 'that']
G[39] = ['but', P, 'came', 'humility', 'late']
G[40] = [P, 'they were', 'the', 'sails', 'dark', 'first', 'already', 'on', 'the', 'sea']
G[41] = ['I lay', 'it', 'as', P, 'was', 'laid', 'at-me']
G[42] = ['and', P, 'said', 'the', 'hearth', 'we-remember']
G[43] = ['Door', 'the', 'Warden']
G[44] = ['the', 'winter', 'third', 'in', 'Tide', 'Remembering']
G[45] = ['words', 'Brenn', 'outpost', 'as', P, 'they two took', WEN, 'them', 'from', 'his', 'mouth', 'in', 'old age',
         'pair', 'the', 'guild', 'in', 'Harbour', 'Old',
         P, 'they two read', HAL, 'them', 'at', 'the', 'hearth', 'this', 'and', P, 'I laid', 'inscription', 'year',
         'in', 'their', 'back']
G[46] = ['mark', WEN, 'two', 'archivists', 'Harbour', 'Old', 'on', 'seal', 'bundle', 'Brenn', 'as', P, 'broke', 'it']
G[47] = ['we two hold', 'the', 'stone']
G[48] = ['but', 'not', 'are', 'the', 'words', 'at-us-two', 'as', P, 'they were', 'written', 'like', 'this',
         'we two read', 'them']
G[49] = [P, 'were', 'nineteen', 'years', 'at-me',
         P, 'we were', 'twelve', 'and', 'the', 'warden', 'in', 'outpost', 'last', 'the', 'land', 'in', 'what', 'runs',
         'the', 'rock', 'to', 'the', 'grey',
         P, 'was', 'Tobe', 'old', 'fisherman', 'at', 'the', 'edge', 'ten', 'and', 'twenty', 'years',
         'was', 'the', 'runner', 'I', P, 'I swore', 'when', P, 'were', 'fifteen', 'years', 'at-me', 'my', 'hand',
         'flat', 'on', 'stone', 'the', 'runners',
         'thing', 'that', P, 'I saw', 'I carry', 'it', 'not', 'I carry', 'thing', 'other', 'it stands']
G[50] = [P, 'laid', 'the', 'wood', 'black', 'in', 'the', 'outpost', 'whole', 'in', 'posts', 'the', 'door', 'in', 'his',
         'table', 'in', 'frame', 'the', 'bed',
         P, 'held', 'he', 'the', 'outpost', 'by', 'name', 'his', 'father', 'in', 'Council', 'Trade', 'and', 'was not',
         'more', 'old', 'than', 'the', 'runner', 'he',
         'from', 'what', 'was', 'hot', 'his', 'temper', P, 'they sent', 'him', 'to', 'edge', 'in', 'what', 'not', P,
         'fell', 'it', 'but', 'on-us', 'the', 'twelve',
         P, 'knew', 'he', 'battle', 'never', P, 'knew', 'he', 'patience', 'never']
G[51] = ['one', 'morning', 'at', 'end', 'summer', P, 'came in', 'boat', 'small', 'grey', 'from', 'the', 'grey',
         'not', P, 'was', 'wind', 'but', P, 'came in', 'the', 'boat']
G[52] = [P, 'beached', 'the', 'stranger', 'it', 'and', P, 'walked', 'he', 'to', 'high', 'to', 'door', 'the', 'warden',
         P, 'stood', 'in', 'the', 'house', 'and', 'not', P, 'came', 'he', 'more', 'near', 'to', 'the', 'door',
         'was', 'tall', 'the', 'stranger', 'and', 'pale', 'and', 'clad', 'in', 'mist-cloth', 'that', P, 'moved',
         'when', 'not', P, 'moved', 'he',
         'not', P, 'I saw', 'weapon', 'on-him']
G[53] = [P, 'spoke', 'he', 'first', 'in', 'his', 'tongue', 'own', 'loud', 'like', 'wind', 'storm', 'in', 'forest',
         'old', 'and', P, 'was', 'fear', 'on-us',
         'not', P, 'we knew', 'like', 'this', 'they speak', 'they', 'and', 'nothing', 'other',
         'from', 'that', P, 'said', 'he', 'three', 'words', 'Shoreland', 'carefully', 'as', 'lays', 'man', 'thing',
         'that', 'breaks', 'might']
G[54] = ['stop', 'sky', 'dying']
G[55] = ['were', 'words', 'true', 'they', 'spoken', 'true', 'I know', 'it', 'when', 'this',
         'but', 'are', 'sounds', 'alone', 'words', 'that', 'not', 'is', 'sentence', 'at-them', 'and', 'not', P,
         'we heard', 'but', 'sounds']
G[56] = ['from', 'that', P, 'knelt', 'he', 'on', 'threshold', 'and', P, 'laid', 'he', 'in', 'face', 'the', 'warden',
         'stone', 'dark', 'great', 'as', 'two', 'fists',
         P, 'laid', 'he', 'it', 'as', F, 'you will lay', 'bread', 'in', 'face', 'guest',
         'not', P, 'moved', 'one', 'from-us',
         'in', 'his', 'back', P, 'came', 'seabird', 'to', 'low', 'and', P, 'walked', 'it', 'in', 'heart', 'the',
         'stones']
G[57] = [P, 'kicked', 'it', 'at', 'shoulder']
G[58] = [P, 'went', 'it', 'into', 'the', 'dust', 'by', 'the', 'wall',
         'from', 'that', P, 'they laughed', 'men', 'the', 'warden',
         P, 'I stood', 'at', 'their', 'shoulder', 'and', 'I hear', 'the', 'laughing', 'that', 'yet']
G[59] = [P, 'rose', 'the', 'stranger',
         P, 'laid', 'he', 'his', 'hand', 'right', 'on', 'back', 'neck', 'the', 'warden', 'gently', 'as', P, 'did',
         'mother', 'to-me', 'when', P, 'was', 'fever', 'on-me',
         P, 'drew', 'he', 'their', 'heads', 'together', 'until', 'touching', 'the', 'foreheads', 'and', P, 'was',
         'he', 'in', 'silence',
         P, 'stood', 'and', P, 'let', 'he', 'him', 'in', 'touching',
         'I think', 'if', P, 'stopped', 'it', 'at', 'that', F, 'will go', 'our', 'life', 'other']
G[60] = ['from', 'that', P, 'took', 'the', 'stranger', 'blade', 'small', 'in', 'his', 'hand', 'other', 'and', P,
         'touched', 'he', 'it', 'on', 'arm', 'right', 'the', 'warden']
G[61] = [P, 'tore', 'from-him',
         'not', P, 'came', 'blood', 'from-him', 'ever', 'in', 'his', 'life',
         'in', 'tearing', P, 'went', 'deep', 'the', 'cut', 'that', P, 'was', 'meant', 'shallow', 'and', P, 'came',
         'the', 'blood']
G[62] = ['seize!', 'him', P, 'screamed', 'he']
G[63] = [P, 'they seized', 'him', 'not', P, 'fought', 'he',
         P, 'was', 'the', 'blade', 'yet', 'in', 'his', 'hand', 'turned', 'to', 'his', 'arm', 'own',
         'in', 'mortar', 'their', 'hands', 'again', P, 'knelt', 'he', 'in', 'what', P, 'knelt', 'he', 'at', 'his',
         'gift',
         'not', P, 'I understood', 'it']
G[64] = ['kill!', 'him', P, 'screamed']
G[65] = [P, 'they took', 'thing', 'that', P, 'was', 'at', 'hand', 'staves', 'and', 'stones', 'the', 'shingle', 'and',
         'poles', 'the', 'boats',
         P, 'took', 'one', 'from-them', 'my', 'pole', 'the', 'pole', 'that', P, 'I pushed', 'the', 'boats', 'with']
G[66] = ['not', P, 'lifted', 'he', 'his', 'hand',
         'if', P, 'cried out', 'he', P, 'was', 'it', 'in', 'his', 'tongue', 'own', 'and', P, 'I heard', 'it', 'like',
         'wind',
         P, 'I counted', 'the', 'blows', 'I count', 'them', 'yet',
         'when', P, 'lay still', 'he', P, 'went on', 'in', 'screaming', 'and', P, 'they went on', 'some',
         P, 'they broke', 'two', 'arms', 'the', 'stranger', 'the', 'one', 'that', P, 'held', 'neck', 'the', 'warden',
         'gently', 'so', 'and', 'the', 'one', 'that', P, 'held', 'the', 'blade']
G[67] = [P, 'they obeyed', 'men', 'the', 'warden']
G[68] = [P, 'we obeyed']
G[69] = ['I say', 'we', 'from', 'what', 'was', 'one', 'thing', 'the', 'outpost', 'day', 'that', 'and', P, 'I was',
         'in-it',
         'not', P, 'I laid', 'hand', 'on-him', 'not', P, 'I stopped', 'them', 'was', 'boy', 'I', 'in', 'heart', 'men']
G[70] = ['from', 'that', P, 'was', 'silence', 'and', P, 'went', 'the', 'seabird']
G[71] = [P, 'they drew', 'him', 'by', 'his', 'feet', 'over', 'the', 'shingle', 'to', 'the', 'sea', 'and', P, 'touched',
         'his', 'head', 'every', 'stone',
         P, 'they threw', 'him', 'into', 'his', 'boat', 'own', 'as', 'throws', 'fisherman', 'net', 'torn', 'into',
         'bottom', 'boat']
G[72] = [P, 'held', 'his', 'arm', 'and', 'not', P, 'looked at', 'he', 'the', 'boat']
G[73] = ['burn!', 'it', P, 'said', 'he', 'and', 'shove!', 'it', 'to', 'far', 'and', 'give!', 'it', 'to', 'tide',
         'leave!', 'nothing', 'that', 'gives', 'sight']
G[74] = [P, 'they laid', 'it', 'in', 'fire', 'and', 'not', P, 'burned', 'it', 'as', 'burns', 'wood',
         P, 'was', 'screaming', 'in-it', P, 'was', 'the', 'stranger', 'dead',
         'was not', 'man', 'that', P, 'screamed', 'was', 'the', 'wood', 'itself']
G[75] = [P, 'they shoved', 'it', 'to', 'far', 'with', 'the', 'poles', 'very',
         P, 'went', 'Tobe', 'old', 'into', 'the', 'sea', 'to', 'his', 'knees', 'and', P, 'washed', 'he', 'the',
         'poles',
         P, 'we stood', 'the', 'rest', 'on', 'the', 'shingle', 'and', 'not', P, 'we wanted', 'seeing', 'and', P,
         'we looked']
G[76] = ['in', 'far', P, 'turned', 'the', 'boat',
         P, 'went', 'it', 'in', 'face', 'the', 'wind', 'and', 'in', 'face', 'the', 'current', 'and', 'into', 'the',
         'grey', 'in', 'fire']
G[77] = ['day', 'that', 'very', P, 'called', 'to', 'clerk', 'and', P, 'wrote', 'the', 'clerk', 'to', 'the', 'Council',
         P, 'I was', 'at', 'shoulder', 'and', 'is', 'its', 'saying', 'at-me', 'from', 'heart']
G[78] = G[31]
G[79] = ['not', 'is', 'word', 'about', 'the', 'gift', 'not', 'is', 'word', 'about', 'the', 'kneeling']
G[80] = ['in', 'morning', 'next', 'when', P, 'slept', 'every', 'one', 'still', P, 'I picked up', 'the', 'stone', 'from',
         'the', 'dust',
         'not', 'I know', 'from', 'what', P, 'I did', 'it',
         'at', 'his', 'door', P, 'gave', 'the', 'letter', 'to-me',
         'like', 'this', P, 'they went', 'the', 'gift', 'and', 'the', 'lie', 'into', 'one', 'pack', 'and', P,
         'I ran', 'it']
G[81] = [P, 'I ran', 'one', 'day', 'and', 'one', 'night', 'and', 'four hundred', 'paces', 'and', 'four hundred',
         'paces', P, 'I said', 'the', 'oath', 'again']
G[82] = ['in', 'Harbour', 'Old', P, 'read', 'clerk', 'old', 'the', 'Council', 'it', 'ink', 'on', 'his', 'fingers',
         'and', P, 'looked', 'he', 'to', 'high', 'at-me']
G[83] = [Q, 'is', 'it', 'like', 'this']
G[84] = ['not', P, 'I said', 'is', 'it', 'like', 'this', P, 'I said', 'is', 'it', 'written',
         'two', 'twenties', 'years', P, 'I weighed', 'the', 'cleverness', 'small', 'that']
G[85] = [P, 'I carried', 'the', 'lie', 'in', 'one', 'day', 'and', 'one', 'night',
         P, 'I carried', 'the', 'truth', 'two', 'twenties', 'years', 'and', P, 'I gave', 'it', 'to', 'no one']
G[86] = ['autumn', 'that', P, 'laughed', 'the', 'Shore', 'on', 'three', 'axemen', 'who', P, 'they came back', 'to',
         'home', 'on', 'mast', 'and', 'who', P, 'they swore', 'upon', 'boat', 'that', 'burns', 'from', 'the', 'grey',
         'not', P, 'I laughed', 'from', 'what', P, 'I saw', 'it', 'in', 'turning',
         'but', P, 'I said', 'nothing', P, 'was', 'it', 'written', 'at', 'the', 'Council']
G[87] = [P, 'wore', 'sleeves', 'long', 'until', 'death', 'by', 'course', 'summers', 'hot', 'in', 'Harbour', 'Old',
         'and', 'I know', 'from', 'what',
         'winter', 'that', P, 'went', P, 'died', 'he', 'in', 'bed', 'the', 'wood', 'black',
         'I am', 'alone', 'yet', 'from', 'the', 'twelve']
G[88] = ['two', 'twenties', 'years', P, 'lay', 'the', 'stone', 'in', 'bottom', 'my', 'pack', 'and', 'not', P,
         'I held', 'it', 'one', 'time',
         'I give', 'it', 'when', 'this', 'with', 'the', 'words', 'these', 'and', 'I ask', 'forgiving', 'to', 'God',
         'from', 'what', 'not', 'is', 'one', 'at-me', 'for', 'asking', 'but', 'God']
G[89] = ['until', 'this', 'words', 'Brenn', 'blot', 'and', 'blot', P, 'they two were', HAL, 'mute']
G[90] = [P, 'bore', 'arm', 'the', 'warden', 'one', 'mark', 'half', 'thing', 'riven', 'in', 'middle',
         P, 'kept', 'the', 'Council', 'the', 'letter']
G[91] = [P, 'died', 'Brenn', 'as', 'lays', 'man', 'load',
         P, 'buried', 'the', 'guild', 'him', 'in', 'low', 'his', 'name',
         P, 'cut', 'it', 'name', 'the', 'warden', 'to', 'far']
G[92] = [P, 'they two sealed', WEN, 'his', 'words', 'and', P, 'they two told', 'them', 'to', 'no one',
         'in', 'the', 'Fall', P, 'they two carried', 'they two', 'the', 'chest', 'from', 'the', 'haven', 'his', 'hand',
         'on', 'one', 'handle', 'and', 'her', 'hand', 'on', 'the', 'other',
         'on', 'the', 'Road', P, 'they failed', 'their (two)', 'arms',
         P, 'they said', 'the', 'masons', 'not', 'is', 'thing', 'rich', 'in-it', 'and', P, 'they gave', 'it', 'to',
         'two', 'young', 'very', 'to', 'Tarnel', 'and', 'to-me',
         'with', 'his', 'hand', 'loosed', P, 'knotted', 'Tarnel', 'his', 'net',
         P, 'I looked at', 'the', 'knots']
G[93] = ['in', 'night', 'the', 'pass', P, 'they two lay down', WEN, 'and', 'not', P, 'they two rose',
         'by', 'the', 'chest', P, 'we two slept', 'Tarnel', 'and', 'I', 'his', 'hand', 'on', 'one', 'handle', 'and',
         'my', 'hand', 'on', 'the', 'other',
         'in', 'morning', P, 'was', 'frost', 'on', 'both']
G[94] = ['not', P, 'woke', 'Tarnel']
G[95] = ['at', 'that', P, 'I stopped', 'night', 'this', 'my', 'hands', 'on', 'the', 'stone',
         'from', 'that', P, 'they two laid', HAL, 'their (two)', 'hands', 'at', 'their', 'shoulder']
G[96] = [P, 'carried', 'she', 'it', 'every', 'step']
G[97] = ['and', 'from', 'the', 'passes', P, 'carried', 'she', 'it', 'alone']
G[98] = ['not', 'is', 'law', 'old', 'than', 'this', 'in', 'heart', 'the', 'peoples', 'man', 'who', 'kneels', 'at',
         'your', 'door', 'in', 'low', 'your', 'roof',
         'were', 'people', 'doors', 'we']
G[99] = ['we two lay', 'it', 'as', P, 'was', 'laid', 'at-us-two']
G[100] = G[42]
G[101] = ['not', P, 'said', 'the', 'hearth', 'this', 'it', 'ever', 'over', 'killing', 'that', P, 'did', 'our',
          'people', 'own',
          P, 'laid', 'Ebba', 'old', 'the', 'stone', 'first', 'and', P, 'were', 'the', 'rest', 'slow', 'to',
          'following',
          'but', P, 'they followed']
G[102] = ['and', P, 'put', 'the', 'Captain', 'the', 'hood', 'to', 'back']
G[103] = ['in', 'morning', P, 'they swore', 'the', 'runners', 'the', 'oath', 'again', 'and', P, 'they added', 'four',
          'words', 'on-it', 'is not', 'as', 'carrying', 'Brenn',
          P, 'swore', 'Wick', 'the', 'young', 'very', 'it', 'loud', 'very']

out, seen, errs = [], {}, []
for i, r in enumerate(need):
    words = [w for w, _ in r['draft']]
    g = G.get(i)
    if g is None:
        errs.append((i, 'missing')); continue
    if len(g) != len(words):
        errs.append((i, 'len', len(g), len(words)))
        for k in range(max(len(g), len(words))):
            a = words[k] if k < len(words) else '--'
            b = g[k] if k < len(g) else '--'
            print('   ', i, k, a, '=', b)
        continue
    pairs = [[w, e] for w, e in zip(words, g)]
    if r['rom'] in seen:
        if seen[r['rom']] != pairs:
            errs.append((i, 'dup differs'))
        continue
    seen[r['rom']] = pairs
    out.append({'rom': r['rom'], 'gloss': pairs})
print('errors:', errs)
if not errs:
    json.dump(out, open(S + '/gloss/S06.json', 'w'), ensure_ascii=False, indent=1)
    print('wrote', len(out), 'rows')
