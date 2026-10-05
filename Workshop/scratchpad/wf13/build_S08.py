import json, sys
S = '/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
need = json.load(open(S + '/gloss_in/S08.json'))
HY = 'Halyna (the two)'
G = {}
def g(i, s):
    G[i] = [w.strip() for w in s.split('|')]

g(0, "Night | Naming")
g(1, "late | in | the | summer | second")
g(2, "(past) | I held | the | lamp | night | that | and | (past) | I laid | this | at | the | hearth | in | evening | the | morrow | "
     "they lie | the | planks | that | I tell | about-them | in | the | vault | low | very | yet | "
     "goes | anyone | to | low | when | he wishes | and | lays | one | his | hand | on-them")
g(3, "hold! | the | stone | Seren")
g(4, "at | course | the | winter | first | that | (past) | laughed | the | fire | this | upon | the | sails | grey | "
     "(past) | said | Kael | (past) | they chose | the | keep | wrong | and | (past) | I laughed | like | the | rest")
g(5, "in | night | late | in | Tide | Second | (past) | they two went | HY | to | low | to | the | vault | old | very | in | low | the | hall | this | in | what | (past) | was | the | Rite | found | "
     "(past) | I followed | them two | and | the | ink | and | the | lamps | at-me | "
     "is | it | cold | in | the | summer | as | in | the | winter | "
     "(past) | they lay | the | courses | grey | upon | grey | like | field | turned | that | (past) | gave | stones")
g(6, "(past) | were | at | that | two | twenties | and | thirteen | planks | the | winter | first | and | every | one | carved | "
     "(past) | they carried | the | runners | them | to | home | two | runners | to | one | plank | from | in | what | (past) | gave | the | sea | them | and | the | salt | in | pouring | upon | their | arms | "
     "(past) | was | the | rest | at | fires | the | soldiers | and | at | the | tide | "
     "(past) | named | the | wall | them | the | tablets | "
     "were | only | planks | they")
g(7, "every | one | from-them | but | one | (past) | gave | it | one | word | to | HY | and | (past) | I wrote | the | words | one | word | to | leaf | "
     "(past) | gave | the | one | nothing | but | (past) | was | it | carved | well | as | every | one | "
     "weeks | in | back | the | first | (past) | brought | the | sea | it")
g(8, "(past) | they bore | planks | Tide | Second | two | signs | every | one | cut | close | as | they cut | names | close | upon | lintel | old | "
     "on | the | shingle | (past) | they two learned | HY | holding | both | together | and | (past) | was | gap | in | the | telling | every | time | "
     "not | (past) | I mended | them | with | guesses | "
     "until | night | that | (past) | went | no one | to | low | for | asking | the | two | twenties | and | thirteen | (question) | is | much")
g(9, "was | short | the | night | and | were | long | the | courses | from | that | (past) | they two laid | the | stone | first | in | the | two | ends | Rhyna | at | the | stair | and | Halvard | at | the | wall | far | "
     "(past) | I saw | HY | never | in | holding | from | other | until | night | that | "
     "and | not | (past) | they two were | far | from | other | length | the | vault")
g(10, "(past) | took | Rhyna | the | plank | first | very | the | wave | that | (past) | said | shore | and | one | edge | long | riven | at-it | "
      "(past) | took | Halvard | the | one | mute | and | (past) | was | edge | long | riven | at-it | as | at | the | first")
g(11, "(past) | I stood | in | mortar | HY | and | the | lamp | at-me | "
      "not | comes | wind | as far as | the | deep | this | and | (past) | rose | the | flame | true | in | my | hand")
g(12, "(past) | lifted | Rhyna | her | plank | at | the | wall | far | (past) | lifted | Halvard | his | plank | "
      "like | this | they rise | the | knots | far | together | and | the | knots | near | from | what | is | one | net | whole | it")
g(13, "in | one | moment | (past) | they two changed | the | two | faces")
g(14, "from | that | (past) | spoke | Rhyna | and | was not | word | it | was | order | whole | it")
g(15, "to | shore | as | root | to | water | go! | not | wait! | on | bough")
g(16, "from | the | end | far | and | the | plank | mute | at-him | (past) | said | Halvard | it | together | word | upon | word")
g(17, "from | that | (past) | spoke | every | plank | "
      "(past) | we laid | them | in | course | as | (past) | gave | the | sea | them | and | night | that | (past) | gave | every | one | its | course | own | "
      "the | night | whole | (past) | they two went | HY | at | line | the | courses | Rhyna | to | Halvard | and | Halvard | to | Rhyna | and | (past) | I went | in | mortar | and | (past) | I wrote | "
      "in | middle | the | courses | (past) | was | hurt | upon | my | hand | to | the | joint | and | not | (past) | I stopped | "
      "they are | at | this | the | others | as | (past) | I wrote | them")
g(18, "break! | wall | stone | first | stone | only | strike! | until | opening | or | until | your | ash | "
      "was | that | the | square | whole | like | this | they cut | they | the | thing | mute | stone | "
      "(past) | they hammered | the | hulls | that | one | wall | until | sinking | and | (past) | we named | them | wild")
g(19, "go! | until | blow | in | what | splits | skin | turn! | at | shoulder | "
      "(past) | swerved | the | one | that | and | (past) | followed | none | it | "
      "(past) | we named | it | un-brave")
g(20, "in | face | bearer | wood | thin | falls | wood | thin | goes on | bearer | "
      "the | hulls | at | head | the | line | (past) | was | commanded | to-them | die! | first | and | (past) | they died | first")
g(21, "in | what | (past) | flashed | it | strike! | flash | last | flash | only | "
      "the | gun | that | (past) | spoke | last | (past) | they turned | to | it | "
      "(past) | we named | it | want")
g(22, "wait! | in | grey | as | seed | in | frost | when | is still | stone | come! | "
      "(past) | they came | when | (past) | we stopped | looking")
g(23, "to | home | when | wounded | falls | one | bough | turns | every | one | in | its | water | own | "
      "at | loss | first | (past) | they scattered | and | (past) | shouted | the | wall | in | gladness")
g(24, "(past) | they took | the | soldiers | head | the | order | for | name | one | and | one | in | the | words | plain | "
      "to | the | shore | break! | the | wall | wait! | in | grey")
g(25, "when | (past) | they two met | HY | in | middle | (past) | was | grey | the | morning | in | going | to | low | upon | the | stair | "
      "(past) | lay | one | plank | other | at | end | the | course | last | alone | "
      "(past) | carried | mason | Harbour | Fire | it | to | high | the | mountain | in | back | the | Fall | charred | black | at | one | end | "
      "not | (past) | endured | he | bringing | nothing | from | his | city | and | not | (past) | knew | he | what | was | it")
g(26, "(past) | they two held | HY | it | at | end | hand | and | hand | on | the | grain | while | (past) | they paled | the | lamps")
g(27, "(past) | said | it | burn!")
g(28, "(past) | spoke | no one | and | at | course | time | long | not | (past) | I wrote | "
      "from | that | (past) | laid | Halvard | it | in | its | place | at | end | the | course | last | alone")
g(29, "was | that | every | thing | that | (past) | knew | the | wood | young | one | word | to | hull | and | in-it | one | order | "
      "(past) | said | every | hull | its | word | at | our | wall | and | (past) | said | again | and | (past) | said | until | drowning")
g(30, "not | (past) | they chose | anything")
g(31, "(past) | they were | sent")
g(32, "when | (past) | rose | the | day | (past) | I took | the | plank | first | and | the | one | mute | "
      "the | night | whole | (past) | they returned | my | eyes | to | their | edge | "
      "(past) | I laid | them | shoulder | at | shoulder | edge | riven | at | edge | riven")
g(33, "(past) | met | the | grain | broken")
g(34, "(past) | met | it | as | they two meet | two | halves | the | wood | riven | "
      "not | (past) | I asked | HY | what | means | it | and | not | (past) | they two told | it | to-me")
g(35, "from | that | (past) | we sat | in | middle | the | planks | we | three | "
      "(past) | they burned | the | lamps | still | and | (past) | stopped | no one | them | "
      "at | end | (past) | I said | this | and | (past) | they two let | HY | it | in | standing")
g(36, "I think | the | hulls | that | were | the | wood | young | very | they | sent | first | from | what | grow | the | young | quick | very | "
      "the | bad | very | from | the | wood | not | (past) | came | it | yet | "
      "is | it | in | growing | still")
g(37, "I lay | it | as | (past) | was | laid | to-me")
g(38, "and | (past) | said | the | hearth | we-remember")
# V.5
g(39, "Tides | that | (past) | Counted | the | Wall")
g(40, "at | end | Tide | and | Tide | at | course | six | winters")
g(41, "(past) | laid | Kael | Counter | who | not | (past) | laid | Tide | but | when | (past) | was | it | whole | "
      "in | the | winter | sixth | (past) | bade | he | to-me | mending | the | six | as | (past) | I mended | his | tale | first | "
      "(past) | I lessened | my | mending | on-them")
g(42, "give! | the | stone | to-me | not | I sit | (future) | I will stand")
g(43, "one | Tide | Hasty")
g(44, "I count | am | counter | I")
g(45, "eight | sails | the | morning | first | and | (past) | kept | none | place | at | shoulder | another | "
      "(past) | hammered | every | hull | the | wall | first | that | (past) | touched | it | until | sinking")
g(46, "(past) | stood | no one | on | the | decks | from | the | transports | (past) | they came | the | men | root | like | kindling | poured | "
      "are | treelings | they | to | the | wall | as | if | (future) | will lessen | name | them")
g(47, "at | noon | (past) | was | fire | the | fleet | in | lessening | and | (past) | we learned | saying | is | fire | the | fleet | spent")
g(48, "(past) | fell | breach | on | face | southern | the | wall | outward | as | (past) | said | slates | the | chest | black | "
      "and | (past) | lived | every | one | at | its | back | I swear | upon | that | it stands")
g(49, "at | course | the | winter | that | (past) | I said | at | the | fire | this | (past) | they chose | the | sails | grey | the | keep | wrong | "
      "every | night | (past) | went | it | at | line | the | benches | together | and | the | cup | and | (past) | drank | every | man | to | it | "
      "(past) | we laughed | forgive! | us | God | (past) | we laughed")
g(50, "Jory | Harbour | Old | who | (past) | whistled | on | the | wall | eastern | (past) | laughed | he | loudly | very | "
      "is | name | Jory | first | in | low | the | cairns | eastern")
g(51, "(past) | took | fire-ship | him | "
      "night | that | (past) | tore | the | Captain | breadth | hand | from | half | the | cloak | that | wears | he | and | (past) | bound | he | it | on | pike | over | cairn | Jory")
g(52, "was | the | piece | first | it")
g(53, "laid | in | hand | Seren | was not | the | last | it")
g(54, "two | Tide | Second")
g(55, "the | count | second | and | hard | than | the | first")
g(56, "two | and | two | (past) | they came | the | one | in | front | (past) | took | it | the | shot | and | the | one | in | back | (past) | took | it | the | ground")
g(57, "at | the | point | northern | (past) | caught | hull | shot | "
      "four hundred | paces | to | the | south | (past) | paled | sail | hull | other | grey | and | green | to | white | like | face | man | and | (past) | turned | it")
g(58, "not | (past) | saw | it | (past) | knew | it")
g(59, "from | that | (past) | they came | the | crown-hulls | and | the | seed | winged | in | what | (past) | they were | the | guns | at-us | quiet")
g(60, "when | (past) | we sank | bearer | (past) | took | another | the | standard | and | (past) | took | the | fleet | heart | the | bearer | new | "
      "I say | it | yet | to | the | gunners | young | choose! | the | heart | which | you leave | to-them")
g(61, "(past) | held | Corlen | harbour | old | very | the | Twelve | finger | wet | to | the | wind | in | face | the | holding | every | time | "
      "(past) | said | he | wait! | not | finishes | the | sea | yet")
g(62, "in | falling | seed | (past) | came | hull | slow | on | his | water | "
      "by | his | judgement | own | (past) | held | he | his | battery | quiet | until | coming | the | hull | near | "
      "(past) | looked | Corlen | upon | the | water | and | upon | nothing | in | his | back")
g(63, "(past) | came | the | seed | over | the | wall | in | what | (past) | they were | the | guns | quiet")
g(64, "his | guns")
g(65, "(past) | died | he | at | the | capstone | wall | in | looking | the | water | and | three | from | his | gun-crew | together | "
      "night | that | (past) | tore | the | Captain | the | piece | second")
g(66, "(past) | held | Corlen | as | (future) | will hold | the | Captain | in | his | place | "
      "is | every | thing | True Man | that | "
      "and | (past) | killed | that | him")
g(67, "(past) | took | Voss | his | battery | and | (past) | rose | he | True Man | "
      "at | the | holding | next | (past) | held | he | finger | wet | to | the | wind | as | (past) | held | Corlen | "
      "(past) | looked | the | Captain | at | his | shoulder | to | high | and | is not | to | the | sea")
g(68, "change! | your | shot")
g(69, "three | Tide | Remembering")
g(70, "(past) | you knew | Wick | (past) | ran | he | from | place | to | place | and | to | the | hearth | this | even | "
      "and | (past) | sat | he | at | the | front | in | what | they sit | the | children | his | knee | to | his | mouth | "
      "(past) | was | running | the | wall-walk | at-him | while | (past) | said | one | the | Title | two | times | "
      "not | (past) | wanted | he | but | running | word | to | the | Captain")
g(71, "by | night | (past) | moved | the | Captain | the | gun | southern | two | twenties | paces | "
      "at | morning | grey | (past) | stood | Wick | at | place | old | the | gun | to | looking | the | water | "
      "on | the | wall | northern | (past) | burned | lamp | Hesk | still")
g(72, "(past) | came | one | hull | alone | and | slow | in | sounding | water | "
      "is not | to | the | wall | to | the | place | in | what | (past) | was | the | gun | "
      "(past) | fired | it | at | that | to | seeing | whether | answers | the | gun")
g(73, "(past) | took | the | shot | the | capstone | wall | and | (past) | fell | Wick | with-it")
g(74, "not | (past) | I saw | it | (past) | saw | Hale | (past) | gave | Wick | three | words | to-him")
g(75, "they are | in | looking")
g(76, "(past) | came | his | word | to | the | Captain | as | (past) | wanted | he | every | day | the | war")
g(77, "(past) | ran | Hale | it")
g(78, "night | that | (past) | tore | the | Captain | piece | Wick | like | this | (past) | died | youth | from | gun | that | not | (past) | was | at | that")
g(79, "(past) | we thought | are | beasts | they | that | they learn | by | stick | "
      "they look | first | and | from | that | they trust | "
      "(past) | they knew | our | walls | our | Captain | never | "
      "from | that | (past) | we moved | the | guns | by | night | and | was | war | quiet | from | that | and | (past) | I liked | it | little | than | the | war | loud")
g(80, "four | Tide | Joined")
g(81, "the | night | whole | (past) | they were | the | drums | in | knocking | in | grey | from | hull | to | hull | "
      "at | dawn | (past) | they came | the | sails | on | three | roads | together | north | and | east | and | south | "
      "three | roads | one | hour")
g(82, "(past) | whistled | Lanner | crags | for | the | wind | as | they whistle | men | crags | "
      "(past) | stood | the | Captain | at | his | shoulder | and | (past) | was still | he | "
      "(past) | stopped | Lanner | whistling")
g(83, "loose!")
g(84, "one | hour | in | back | the | dawn | (past) | sank | battery | Lanner | their | bearer")
g(85, "not | (past) | fell | the | fleet | "
      "in | the | hour | that | (past) | cut | the | heart | dead | (past) | they turned | on | the | road | eastern | into | water | empty | (past) | paled | one | sail | and | from | that | the | next | one | breath | in | spacing | "
      "(past) | they kept | hour | mind | dead | "
      "were | hulls | bearer | own | alone | that | (past) | they turned | into | wild")
g(86, "in | face | the | dusk | (past) | I went | at | line | the | wall | for | counting | "
      "(past) | I found | Enno | guild | in | the | breach | eastern | and | four hundred | paces | from-him | in | the | north | Della")
g(87, "five | Tide | that | (past) | Learned | Deceit")
g(88, "the | count | fifth | and | not | I like | it")
g(89, "(past) | they came | as | (past) | came | the | wood | young | loud | and | alone | and | straight | and | (past) | we laughed | as | (past) | we laughed | in | the | winter | first | "
      "(past) | spoke | every | gun | and | (past) | they came | the | hunters | to | the | guns | that | (past) | they spoke | every | one | "
      "(past) | they sent | straw | upon | road | new | every | day | hulls | that | were not | hulls | and | upon | the | road | in | what | not | (past) | woke | gun | the | men | root")
g(90, "but | look! | close | as | (past) | said | Pellow | "
      "(past) | rode | straw | high | and | not | (past) | left | wreck | and | not | (past) | flinched | at | shot | "
      "(past) | kept | rout | false | its | courses | and | green hull | that | (past) | paled | was not | green hull | it")
g(91, "not | (past) | they looked | some | from-us | and | they are | in | low | the | cairns | eastern")
g(92, "(past) | looked | Pellow | every | thing | in | his | glass | and | (past) | you laughed | upon-him | and | (past) | I laughed | I | myself | "
      "(past) | polished | he | our | glasses | sight | far | from | glass | his | city")
g(93, "(past) | looked | Pellow | and | is | he | in | low | the | cairns | like | them")
g(94, "(past) | kept | looking | no one | alive | (past) | kept | it | the | wall")
g(95, "six | Tide | Last")
g(96, "in | the | winter | this | when | (past) | lost | fleet | its | bearer | and | the | second | (past) | went | it | to | home | was not | scattered | (past) | it went")
g(97, "in | Tide | Joined | (past) | they two told | HY | to-me")
g(98, "not | is | calling | the | fleet | to | home")
g(99, "from | what | obeys | the | wood | the | wood")
g(100, "(past) | I answered | to-them-two | (future) | we will send | it | to | home | and | not | (past) | I knew | what | (past) | I meant | "
       "not | is | its | calling | to | home | but | is | its | sending | to | home")
g(101, "is | fearing | at | the | wood")
g(102, "at | end | the | winter | this | (past) | came | ten | hulls | great | that | were not | fleet | and | (past) | they sat | in | our | havens | "
       "(past) | named | the | wall | them | Captains | Mist | and | the | soldiers | Seats | Great | "
       "they sit | at | that | night | this")
g(103, "at | course | six | winters | (past) | I counted | the | sails | grey | I know | the | number | and | not | I lay | it | at | the | hearth | this")
g(104, "but | (future) | I will lay | the | number | at-us")
g(105, "is not | count | count | until | naming | "
       "night | this | in | the | ward | (past) | I called | names | the | True Men | fourteen | names | and | twelve | who | answer")
g(106, "when | (past) | I called | Corlen | harbour | (past) | was | quiet | the | ward | "
       "(past) | I let | it | quiet | at | time | one | breath | and | (past) | I called | the | name | next | "
       "when | (past) | I called | Hesk | mere | (past) | came | the | answer | to | low | from | the | wall | northern | in | what | (past) | was | his | lamp | lit | "
       "when | (past) | I called | Pellow | spire | (past) | was | quiet | the | ward")
g(107, "when | this | hear! | dead | the | wall | and | hold! | them | from | what | they are | at-us | "
       "Jory | who | (past) | whistled | Corlen | who | (past) | waited | on | the | sea | Wick | who | (past) | ran | from | place | to | place | "
       "Enno | and | Della | Enrella (the two) | hand | in | hand | Pellow | who | (past) | looked | every | thing | in | his | glass | "
       "(past) | tore | the | Captain | breadth | hand | to-them | one | and | one | as | tear | the | poor | the | bread | last | and | they keep | the | share | thin | very")
g(108, "the | cairns | eastern | other | (past) | I named | them | in | dusk | in | middle | the | stones | every | name | two | times | "
       "at | the | last | from-them | not | (past) | stood | my | voice | and | not | I lie | about-it")
g(109, "in | the | winter | first | (past) | hung | half | the | cloak | that | wears | he | to | his | knee")
g(110, "night | this | not | reaches | it | to | his | belly")
g(111, "is | he | in | sitting | at | that | when | this | at | end | the | bench")
g(112, "I lay | it | as | (past) | was | laid | to-me")
g(113, "and | (past) | said | the | hearth | we-remember")

out = []
bad = 0
for i, r in enumerate(need):
    words = [w for w, _ in r['draft']]
    gl = [HY if x == 'HY' else x for x in G[i]]
    if len(gl) != len(words):
        bad += 1
        print('LEN MISMATCH line', i, len(gl), len(words))
        for k in range(max(len(gl), len(words))):
            print('   ', k, words[k] if k < len(words) else '---', '=', gl[k] if k < len(gl) else '---')
        continue
    for w, e in zip(words, gl):
        if w in ('Halyna',) and e != HY:
            print('WARN halyna', i)
    out.append({'rom': r['rom'], 'gloss': [[w, e] for w, e in zip(words, gl)]})
if bad:
    sys.exit(1)
json.dump(out, open(S + '/gloss/S08.json', 'w'), ensure_ascii=False, indent=1)
if '--show' in sys.argv:
    for i, o in enumerate(out):
        print('##', i, ' '.join('%s[%s]' % (w, e) for w, e in o['gloss']))
print('wrote', len(out))
