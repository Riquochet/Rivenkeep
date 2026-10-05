#!/usr/bin/env python3
"""grain_validate.py - Grain Notation v2 validator and reader (wf7; Python standard library only).

Parses Grain Notation v2 (grain_v2.md section 13, with the Additions of section 21), checks it
against the sign table and the composition rules, and prints a plain English reading of the round:
the knowing as a shore-mind would tell it.

The sign table is read from the specs themselves, so the specs stay the one source of truth:
  - wf6/mystaeri_spec.md section 3.5, the JSON block "The inventory as data" (the 70 v1 signs);
  - wf7/grain_v2.md section 9.3, the JSON block (the 47 v2 signs);
  - any ```json block in grain_v2.md section 21 holding {"signs": {...}} or {"compounds": {...}}.
If a spec cannot be read, the validator falls back to wf6/grain/signs.json and wf7/grain2/signs_new.json.

What it checks is notation: everything that can be decided from the GN text alone. Geometry (gates,
crossing angles, the router, the round trip through a drawing) belongs to the renderer's validator
(grain_v2.md section 14.2, items 3-5 and 9). The checks and their codes are listed by --rules.

Usage
  python3 grain_validate.py FILE.gn2 [FILE ...]      check each file, then print its plain reading
  python3 grain_validate.py --literal FILE           the literal reading of section 13.5 instead
  python3 grain_validate.py --canon FILE             print the canonical GN v2 (section 13.4)
  python3 grain_validate.py --check-only FILE ...    findings only
  python3 grain_validate.py --json FILE              findings and the parsed round as JSON
  python3 grain_validate.py --kind order|telling|chip FILE    override the inferred kind of round
  python3 grain_validate.py --expr "TRUE+HOLD →that pocket said{ CARVE{all}+MOUTH }"
                                                     check a grain fragment (signs, ligatures, devices)
  python3 grain_validate.py --md FILE.md             check every GN block (a ``` block whose first line
                                                     starts "round ") found in a markdown file
  python3 grain_validate.py --rules                  list the checks
  python3 grain_validate.py --selftest               run the built-in tests
Files may hold several rounds; each starts with a line "round ...". Lines starting with # are comments;
"# file 12: we (the Aelvaren)" comments name a file's referent for the reading ("# file 5 from r6: ..."
names it from ring 6 on). A trailing "(...)" after two spaces is a comment, as in the v1 samples.

Knowing form (grain_v2 §21, A8): a round may be written knowing by knowing, in the telling's order, with ring
lines "r5·3" (the 3rd knowing of ring 5) and addresses "12.r5·3" or "12.2.r5·3" (the 2nd mark on file 12 in that
knowing). It is packed into years and cells by grain_v2 §4.3 before it is checked; --canon prints the result.

The test corpus is wf7/coverage/tests/*.gn2; run it with wf7/coverage/run_tests.py.

Exit status: 0 when no round has an error, 1 when one does, 2 on a usage problem.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ------------------------------------------------------------------------------------------------
# 1 · Constants of the notation
# ------------------------------------------------------------------------------------------------

BANDS = ('MIST', 'WHITE', 'DREAD', 'WATER', 'STILL', 'DARK')
BAND_PHRASE = {'MIST': 'in the grey', 'WHITE': 'in the white', 'DREAD': 'in the dread',
               'WATER': 'on the water', 'STILL': 'in the stillness', 'DARK': 'in the dark'}
BAND_THING = {'MIST': 'the grey (the breath, the sky)', 'WHITE': 'the white (open sky, snow, hard light)',
              'DREAD': 'the dread', 'WATER': 'the water (the sea)', 'STILL': 'still water (silence, peace)',
              'DARK': 'the dark (night)'}
ARROWS = {'→': 'to', '⇒': 'then', '→in': 'in', '→with': 'with', '→for': 'for', '→bc': 'bc',
          '→as': 'as', '→thru': 'thru', '→that': 'that'}
ROLE_ARROW = {v: k for k, v in ARROWS.items()}
ROLE_READ = {'to': 'to', 'then': 'then / from this', 'in': 'in', 'with': 'with', 'for': 'for, so that',
             'bc': 'because', 'as': 'as', 'thru': 'through', 'that': 'that', 'blind': 'why, the wood does not hold'}
FRINGE = {'all': 'cw', 'few': 'cw', 'half': 'cw', 'only': 'ccw', 'more': 'ccw', 'most': 'ccw',
          'again': 'foot', 'still': 'foot', 'last': 'foot', 'slow': 'foot', 'gently': 'foot'}
FRINGE_LIFE = {'again', 'still', 'last'}          # the time fringe (a shore-man's life, section 3)
PARTS = {  # grain_v2 section 5.2, and DOOR:post from section 18 [Additions A11]
    ('US', 'crown'): 'a head', ('STONEFOLK', 'crown'): "a shore-man's brow",
    ('US', 'stem'): 'a neck', ('STONEFOLK', 'stem'): "a shore-man's neck",
    ('US', 'foot'): 'a foot', ('STONEFOLK', 'foot'): "a shore-man's foot",
    ('HAND', 'stem'): 'an arm', ('HAND', 'palm'): 'a palm',
    ('TREE', 'trunk'): 'a trunk', ('TREE', 'boughs'): 'a crown of boughs',
    ('SAIL', 'mast'): 'a mast', ('SAIL', 'cloth'): "a sail's cloth",
    ('BEARER', 'keel'): 'the keel', ('BEARER', 'hull'): "a hull's shell",
    ('NEW', 'stump'): 'a stump', ('NEW', 'shoot'): 'a shoot', ('DOOR', 'post'): 'a door-post'}
LINE_ROOTS = ('WAVE', 'LONE', 'BARB', 'SPARK', 'SQUARE', 'MOUTHS', 'STERN', 'BREATH', 'KNOT', 'SMOOTH', 'BURN')
WOODS = ('green', 'forty', 'life', 'long', 'eldest', 'stone', 'plain')
AGE = {'green': 0, 'forty': 1, 'life': 2, 'long': 3, 'eldest': 4, 'stone': 4, 'plain': 4}
AGE_NAME = {0: 'green wood', 1: 'wood of forty summers', 2: "a shore-man's life", 3: 'a long life', 4: 'the eldest'}
GRAIN_ARC = ('GRAIN', 'grain-arc')        # the grain-arc: in names only (mystaeri_spec section 3.14)
BEARING = {0: 'ahead (the shore)', 2: 'the right-ahead diagonal', 4: 'the right hand', 6: 'the right-behind diagonal',
           8: 'behind (home, the other side)', 10: 'the left-behind diagonal', 12: 'the left hand',
           14: 'the left-ahead diagonal'}
NUMW = {1: 'once', 2: 'twice', 3: 'thrice', 4: 'four times'}
CARD = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
ORDW = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}

RULES_DOC = [
    ('P', 'parse', 'every line is GN v2 (section 13.2, with Additions A1-A3), a v1 form (section 13.7), or a comment'),
    ('H', 'header', 'wood, pith, rings <= 24, rules after, cells (1-4, ring 1 has 1, never shrinking outward), kind'),
    ('S', 'structure', 'rings in order and within the header count; years contiguous; bands I/II/III where the rules put them'),
    ('M', 'marks', 'known sign; valid part; fringe values, one per station; counts and ordinals 1-4; a ligature of at most '
                   'two signs; files 0-15; cells 1-4, written only when a file holds two marks, never above the ring\'s cells'),
    ('M', 'root', 'one root per pith, in ring 1, year 1, on file 0; ring 1 files 15, 0 and 1 are the root\'s; an order '
                  'cuts nothing else in ring 1; an order\'s root should be one of the ten line roots or Burn'),
    ('M', 'packing', 'a file fills its cells and years in order (section 4.3), except where a pocket took a year'),
    ('K', 'pockets', 'said or cut; at most six files and eight items; depth <= 2; nothing else cut on its files in its '
                     'year; exactly one "that" runner; runners among its items stay inside it'),
    ('R', 'runners', 'unique ids; source and target resolve; the role fits the target (that -> pocket, blind -> '
                     'nothing, @f -> to or in, bind -> to or then); never inward across rings; across rings only then '
                     'or to; no duplicate; splits have at most three shoots; @f needs a free cell'),
    ('X', 'crossings', 'laps name two runners that can meet; braids have 2-3 strands, a pattern of those letters, '
                       'length <= 9, all in one ring; binds have 2-3 strands that end on the bind, one out-runner at most'),
    ('A', 'age and place', 'section 3: in orders, each device only in wood old enough for it; in every round, the heart '
                           'ring takes no fringe, pocket, braid, bind or break, and in a telling band I takes no pocket, '
                           'braid, bind or break and at most two cells'),
    ('C', 'canonical order', 'marks by year, file, cell; runners by source (ring, year, file, cell), then target, then id; '
                             'then laps, braids, binds (section 13.4, with Addition A7 for non-mark targets)'),
    ('D', 'v1 devices', 'ties become runners (section 13.7); rays join marks on one file; memory rays leave a mark; '
                        'forks and chains name known signs'),
]

# ------------------------------------------------------------------------------------------------
# 2 · Short glosses for the reading (the spec's Meaning columns, cut to a word or two)
#     kind: n = thing (sg|pl), v = act (base|ing|causative), a = quality (adj|as a thing)
# ------------------------------------------------------------------------------------------------

G = {
    # the ten roots and Burn, as marks (their own readings as roots are in ROOT_READ)
    'WAVE': 'v:go to the shore, all at once|going to the shore, all at once|send to the shore',
    'LONE': 'n:one alone, ahead of the rest|ones alone', 'BARB': 'n:a screen before|screens before',
    'SPARK': 'v:strike where it flashed|striking where it flashed|', 'SQUARE': 'n:stone (a wall)|stones',
    'MOUTHS': 'n:two mouths, one loud, one landing|', 'STERN': 'v:turn the stern for home|turning for home|send home',
    'BREATH': 'n:the gap between|gaps', 'KNOT': 'v:wait|waiting|make wait', 'SMOOTH': 'v:go veiled|going veiled|veil',
    'BURN': 'v:burn|burning|kindle',
    # acts
    'GO': 'v:go|going|send', 'STRIKE': 'v:strike|striking|', 'BREAK': 'v:break|breaking|',
    'WOUND': 'v:be struck|struck|wound', 'TURN': 'v:turn aside|turning|turn', 'HOLD': 'v:hold|holding|teach',
    'OPEN': 'v:open|opening|lay open', 'CLOSE': 'v:close|closing|', 'MOUTH': 'v:speak|speaking|goad',
    'FALL': 'v:fall|falling|fell', 'RISE': 'v:rise|rising|raise', 'GROW': 'v:grow|growing|grow',
    'LIVE': 'v:live|living|keep alive', 'DYING': 'v:die|dying|kill', 'KNEEL': 'v:kneel|kneeling|',
    'GIFT': 'v:give|giving|', 'BOND': 'v:bind|binding|bind', 'STOP': 'v:stop|stopping|silence',
    'MEND': 'v:mend|mending|', 'ROT': 'v:rot|rotting|rot', 'AXE': 'v:fell with iron|felling|',
    'CARVE': 'v:carve|carving|', 'LEAN': 'v:lean toward|leaning|', 'BEND': 'v:bend|bending|',
    'BENEATH': 'v:go beneath|going beneath|put beneath',
    'HEAR': 'v:hear|hearing|', 'SING': 'v:sing|singing|', 'CRY': 'v:cry out|crying out|', 'LAUGH': 'v:laugh|laughing|',
    'EAT': 'v:drink|drinking|feed', 'WEEP': 'v:weep|weeping|', 'FIND': 'v:find|finding|', 'TAKE': 'v:take|taking|',
    'LOSE': 'v:lose|losing|', 'TEND': 'v:tend|tending|', 'CARRY': 'v:carry|carrying|', 'SIT': 'v:sit|sitting|seat',
    'LIE': 'v:lie down|lying|lay down', 'GUIDE': 'v:guide|guiding|', 'CHOOSE': 'v:choose|choosing|',
    'FOLLOW': 'v:follow|following|draw on', 'OVER': 'a:over, above|what is above',
    # things
    'HULL': 'n:hull|hulls', 'BEARER': 'n:bearer|bearers', 'THIN': 'n:thin one (thin wood)|thin hulls', 'SPENT': 'n:spent hull|worthless wood',
    'GREAT': 'n:great hull|crowns', 'EYE': 'n:eye|eyes', 'HUNTER': 'n:hunter|hunters', 'SWIFT': 'n:swift one|the swift',
    'BREAKER': 'n:stone-breaker|stone-breakers', 'RAM': 'n:ram|rams', 'ROOT': 'n:root|roots', 'SEED': 'n:winged seed|seed',
    'TREE': 'n:tree|trees', 'PILLAR': 'n:black pillar|black pillars', 'SAPLING': 'n:sapling (a child)|children',
    'HEART': 'n:heart|hearts', 'US': 'n:one of us|the long-lived', 'STONEFOLK': 'n:shore-man|shore-men',
    'HOME': 'n:home|homes', 'HOMESTONE': 'n:home of stone|homes of stone', 'SHORE': 'n:shore|shores',
    'ROAD': 'n:road|roads', 'EDGE': 'n:edge|edges', 'GUN': 'n:gun|guns', 'CASTLE': 'n:the house behind the stone|castles',
    'DOOR': 'n:door|doors', 'FLASH': 'n:flash (hard light)|flashes', 'BLOOD': 'n:blood|kin', 'GRIEF': 'n:grief|griefs',
    'SAIL': 'n:sail|sails', 'HAND': 'n:hand|hands', 'TIDE': 'n:tide (a growing)|tides', 'DEEP': 'a:old|the deep',
    'AELTHAR': 'n:the Aelthar|', 'WOOD': 'n:wood|woods', 'BARK': 'n:bark|barks', 'LEAF': 'n:leaf|leaves', 'SAP': 'n:sap|',
    'EARTH': 'n:earth|lands', 'SAND': 'n:sand|sands', 'DUST': 'n:dust|', 'MOSS': 'n:moss|', 'RAIN': 'n:rain|',
    'WIND': 'n:wind|winds', 'SILVERBARK': 'n:silverbark|the council', 'SOFTLIGHT': 'n:soft light|lamps',
    'MORNING': 'n:morning|mornings', 'DUSK': 'n:dusk|', 'SUMMER': 'n:summer|summers', 'MORROW': 'n:the morrow|morrows',
    'NAME': 'n:name|names', 'BONE': 'n:bone|bones', 'BEAST': 'n:beast|beasts', 'MIND': 'n:mind|minds', 'WORD': 'n:word|words',
    'HOUSE': 'n:house|houses', 'CHEST': 'n:chest|chests', 'BRIDGE': 'n:bridge|bridges', 'ANGER': 'n:anger (heat)|',
    'SHAME': 'n:shame|', 'GLAD': 'a:glad|gladness', 'HOLY': 'a:holy|what is holy', 'NEW': 'a:new|what is new',
    'TRUE': 'a:true|what is so',
    'GRAIN': 'n:the grain|',
}
MOTION = {'GO', 'FALL', 'RISE', 'TURN', 'LEAN', 'FOLLOW', 'WAVE', 'STERN', 'KNEEL', 'BENEATH', 'SMOOTH', 'LONE'}
SPECIAL_PLURAL = {'SILVERBARK': 'the council (the silverbarks)', 'TREE': 'the trees (a grove)', 'US': 'the long-lived',
                  'STONEFOLK': 'the shore-men', 'HULL': 'the host (many hulls)', 'ROOT': 'the root-men (roots)',
                  'SAPLING': 'children', 'BLOOD': 'kin', 'SEED': 'the seed (the sky falling)', 'GREAT': 'crowns (heads)',
                  'BONE': 'ribs (bones)'}
KIND_ARC = {'US': 'the long-lived as a people (Naelear)', 'STONEFOLK': 'the shore-folk as a people (Aethear)',
            'ROOT': 'forebears (mothers and fathers)'}
ROOT_READ = {  # (lasting signature, the young-wood order, Seren's one word) - mystaeri_spec section 3.5
    'WAVE': ('to the shore: all at once, by the straightest water, none waiting on another',
             'To shore. As root to water, go. Wait on no bough.', 'shore'),
    'LONE': ('one goes ahead of the rest', 'Go until struck. Where bark splits, turn aside.', 'go'),
    'BARB': ('a screen before the bearer', 'Before bearer, thin wood. Thin wood falls; bearer keeps pace.', 'before'),
    'SPARK': ('where the stone flashed, strike there', 'Where it flashed, strike. Last flash, only flash.', 'flash'),
    'SQUARE': ('stone; the wall; the mute thing', 'Break wall. First stone, only stone. Strike till it opens or wood is ash.', 'wall'),
    'MOUTHS': ('loud in one place; the landing in another', None, 'two mouths'),
    'STERN': ('turn the stern for home', 'Home when wounded. One bough falls; all turn, each by its own water.', 'home'),
    'BREATH': ('between their blows: go in the gap', None, 'breath'),
    'KNOT': ('wait in the grey; come when the shore is still', 'Wait in grey, as seed waits out frost. When stone is still, come.', 'grey'),
    'SMOOTH': ('hidden in the grey: go veiled', None, 'hidden'),
    'BURN': ('burn', 'Burn.', 'burn'),
}
COMPOUNDS = {  # modifier+head -> reading. Keys ignore every decoration but a part and x3 (see lig_key).
    'AXE+WOOD': 'n:timber', 'NEW+HOLD': 'v:learn|learning|teach', 'TRUE+HOLD': 'v:believe|believing|make believe',
    'MORROW+HOLD': 'v:hope|hoping|', 'BOND+HOLD': 'v:trust|trusting|', 'HEART+HOLD': 'v:love|loving|',
    'BOND+US': 'n:the Guest|guests', 'DOOR+STONEFOLK': 'n:the host (the master of the house)|hosts',
    'SQUARE+CARVE': 'n:a lie|lies', 'TRUE+CARVE': 'n:a law|laws', 'DEEP+CARVE': 'n:a judgement|judgements',
    'BOND+BEARER': 'n:the Aelvaren (the Bearer of the Binding)|', 'BOND+SQUARE': 'n:Aelrhen (bond-to-stone)|',
    'BOND+TIDE': 'n:Aelthae (the Joined Tide)|', 'CARVE+BEARER': 'n:the Standard-Bearer (Sethvaren)|Standard-Bearers',
    'HEART+GRAIN': 'n:the Heartwood (Saenvael)|', 'BOND+ROOT×3': 'n:the bond of roots (Aelralen)|',
    'SAPLING+TIDE': 'n:Leathae (the Hasty Tide)|', 'GRAIN+TIDE': 'n:Vaelthae (the Second Tide)|',
    'ROOT×3+TIDE': 'n:Ralenthae (the Tide of Remembering)|', 'SQUARE+TIDE': 'n:Rhenthae (the Tide that Learned Deceit)|',
    'DEEP+TIDE': 'n:Eirthae (the Last Tide)|', 'TIDE+HEART': 'n:Thaesaen (the tide-heart)|',
    'SAPLING+BEARER': 'n:Leavaren (bearer of new branches)|', 'GRAIN+ROT': 'n:Vaelress (the grain that rots)|',
    'ROOT×3+HEART': 'n:Ralensaen (root-heart)|', 'SQUARE+GRAIN': 'n:Rhenvael (stone-grain)|',
    'BENEATH+DEEP': 'n:Senneir (the deep-beneath)|', 'DEEP+KNOT': 'n:the long wait (Eirlenth, in the white)|',
    'HEART+TREE': 'n:Heartoak|', 'AXE+BARK': 'n:Ironbark|', 'DEEP+TREE': 'n:Yew (the old tree)|',
    'TURN+HULL': 'n:Twistbough|', 'BEND+TREE': 'n:Willow|', 'BURN+TREE': 'n:Ashwood|',
    'GREAT+BEAST': 'n:the great beast (the Leviathan)|', 'US:crown×3+BEAST': 'n:the many-headed beast (the Hydra)|',
    'ROT+MOUTH': 'n:the rot-speaker (the Plague Herald)|', 'TREE+BEAST': 'n:the tree-beast (the Ancient Treant)|',
    'GREAT+STONEFOLK': 'n:the great one of stone (the Colossus)|', 'BURN+GREAT': 'n:the burning great one (the Magma Titan)|',
    'SAND+BEAST': 'n:the sand-beast (the Sandworm)|', 'BREAK+GREAT': 'n:the storm-great one (the Storm King)|',
    'DYING+HEART': 'n:the dying heart (the Crystal Lich, in the stillness)|',
    'SHORE+CASTLE': 'n:a haven|havens', 'SQUARE+RISE': 'v:build|building|', 'SQUARE+EYE': 'n:the reach|reaches',
    'HAND+OPEN': 'n:hunger (need)|', 'HAND+CLOSE': 'n:the kept hand|', 'THIN+BEARER': 'n:the prize|prizes',
    'DEEP+SQUARE': 'n:the mountain|mountains', 'BOND+MOUTH': 'n:a promise|promises', 'TRUE+MOUTH': 'n:a tongue of truth|',
    'CARVE+GROW': 'v:prune|pruning|', 'HOLY+KNEEL': 'n:a rite|rites', 'BURN+HOMESTONE': 'n:a hearth|hearths',
    'PILLAR+HULL': 'n:a throne|thrones', 'GIFT+TAKE': 'n:trade|', 'BURN+HOUSE': 'n:a forge|forges',
    'GREAT+HOUSE': 'n:a hall|halls', 'BENEATH+HOUSE': 'n:a cellar|cellars', 'ROAD+BENEATH': 'n:a gallery|galleries',
    'BENEATH+SQUARE': 'n:a canyon|canyons', 'SQUARE+PILLAR': 'n:a tower|towers', 'EYE+OPEN': 'v:wake|waking|wake',
    'NEW+SUMMER': 'n:spring|', 'CLOSE+BOND': 'n:a leash|', 'WIND+SING': 'n:windsong|', 'SEED+GROW': 'v:ripen|ripening|',
    'SIT+WOOD': 'n:a bench|benches', 'HOLD+CARVE': 'v:count|counting|', 'ROOT+HOLD': 'v:remember|remembering|',
    'LONE+NAME': 'n:our own name|own names', 'CARVE+WORD×3': 'n:words cut (more than a word)|', 'HOUSE+OVER': 'n:a roof|roofs', 'TAKE+SAIL:cloth': 'n:a net|nets',
    'BURN+DUST': 'n:ash|', 'EARTH+OPEN': 'v:dig|digging|', 'EARTH+RISE': 'n:a hill|hills', 'CARVE+US': 'n:a carver|carvers',
    'BLOOD+SQUARE': 'n:a sister stone|sister stones', 'SWIFT+FOLLOW': 'v:chase|chasing|', 'SWIFT+GO': 'v:run|running|',
    'HULL+CARRY': 'n:the hull that brings it|', 'NAME+GLAD': 'a:proud of the name|pride', 'GRIEF+ANGER': 'v:rage in grief|raging in grief|',
    'SHORE+HOUSE': 'n:a harbour-house|harbour-houses', 'SHORE+SAND': 'n:the shingle|', 'THIN+MIND': 'n:the short-minded|',
    'STONEFOLK+LIVE': "n:a shore-man's life|shore-men's lives", 'DEEP+LIVE': 'n:a long life|long lives',
    'NEW+WOOD': 'n:green wood|', 'DEEP+WOOD': 'n:the old wood|', 'AXE+PILLAR': 'n:the felling of the pillars|',
    'AXE+PILLAR×3': 'n:the felling of the pillars|', 'BOND+WORD×3': 'n:a sentence|', 'HEART+MIST': 'n:a mist-heart|',
    'HAND+GIFT': 'v:help|helping|', 'WOOD+CRY': 'v:scream as wood screams|screaming|',
    'SUMMER×3+WOOD': 'n:wood of many summers|', 'US+CARVE': 'n:a carver|carvers', 'NEW+STUMP': 'n:a stump|',
    'TRUE+PILLAR': 'n:a straight pillar|', 'BURN+SQUARE': 'n:burning rock (magma)|', 'SAPLING+CARVE': 'n:a sign cut in young wood|',
}

# ------------------------------------------------------------------------------------------------
# 3 · The sign table, read from the specs
# ------------------------------------------------------------------------------------------------


def _json_blocks(text):
    out = []
    for m in re.finditer(r'```json\s*\n(.*?)\n```', text, re.S):
        out.append((m.start(), m.group(1)))
    return out


def load_signs(root=ROOT):
    """Return (signs, sources, compounds): signs = {ID: {'cls','soft','els','gloss','src'}}."""
    signs, sources, extra_compounds = {}, [], {}
    v1 = os.path.join(root, 'wf6', 'mystaeri_spec.md')
    v2 = os.path.join(root, 'wf7', 'grain_v2.md')
    ok1 = ok2 = False
    try:
        t = open(v1, encoding='utf-8').read()
        i = t.index('**The inventory as data.**')
        blk = [b for (p, b) in _json_blocks(t) if p > i][0]
        for k, v in json.loads(blk).items():
            v = dict(v)
            v['src'] = 'v1'
            signs[k] = v
        ok1 = True
        sources.append('wf6/mystaeri_spec.md §3.5 (%d signs)' % len(signs))
    except Exception as e:  # pragma: no cover
        sources.append('mystaeri_spec.md unreadable (%s); fell back to wf6/grain/signs.json' % e)
    try:
        t = open(v2, encoding='utf-8').read()
        i = t.index('### 9.3')
        blocks = _json_blocks(t)
        blk = [b for (p, b) in blocks if p > i][0]
        n0 = len(signs)
        for k, v in json.loads(blk).items():
            v = dict(v)
            v['src'] = 'v2'
            signs[k] = v
        ok2 = True
        sources.append('wf7/grain_v2.md §9.3 (%d signs)' % (len(signs) - n0))
        j = t.find('\n## 21 ')
        if j > 0:
            for (p, b) in blocks:
                if p > j:
                    try:
                        d = json.loads(b)
                    except ValueError:
                        continue
                    if isinstance(d, dict) and 'signs' in d:
                        for k, v in d['signs'].items():
                            v = dict(v)
                            v['src'] = 'v2-add'
                            signs[k] = v
                        sources.append('wf7/grain_v2.md §21 (%d added signs)' % len(d['signs']))
                    if isinstance(d, dict) and 'compounds' in d:
                        extra_compounds.update(d['compounds'])
                        sources.append('wf7/grain_v2.md §21 (%d compounds)' % len(d['compounds']))
    except Exception as e:  # pragma: no cover
        sources.append('grain_v2.md unreadable (%s); fell back to wf7/grain2/signs_new.json' % e)
    # glosses (and the fallbacks)
    for path, tag, ok in ((os.path.join(root, 'wf6', 'grain', 'signs.json'), 'v1', ok1),
                          (os.path.join(root, 'wf7', 'grain2', 'signs_new.json'), 'v2', ok2)):
        try:
            d = json.load(open(path, encoding='utf-8'))
        except Exception:
            continue
        for k, v in d.items():
            if not isinstance(v, dict):
                continue
            if k not in signs and not ok:
                v = dict(v)
                v['src'] = tag
                signs[k] = v
            if k in signs and v.get('gloss'):
                signs[k].setdefault('gloss', v['gloss'])
    return signs, sources, extra_compounds


SIGNS, SIGN_SOURCES, EXTRA_COMPOUNDS = load_signs()
for _k, _v in EXTRA_COMPOUNDS.items():
    COMPOUNDS.setdefault(_k, _v)


def sign_class(sid):
    if sid in GRAIN_ARC:
        return 'thing'
    g = G.get(sid)
    if g:
        return {'n': 'thing', 'v': 'act', 'a': 'quality'}[g[0]]
    s = SIGNS.get(sid, {})
    c = s.get('cls', 'thing')
    return {'root': 'act', 'ligature': 'thing'}.get(c, c)


# ------------------------------------------------------------------------------------------------
# 4 · Findings
# ------------------------------------------------------------------------------------------------

class Findings:
    def __init__(self):
        self.items = []
        self.current = None

    def add(self, level, code, where, msg, ref=''):
        self.items.append({'level': level, 'code': code, 'where': where, 'msg': msg, 'ref': ref, 'round': self.current})

    def count_round(self, level, rid):
        return sum(1 for i in self.items if i['level'] == level and i['round'] == rid)

    def err(self, code, where, msg, ref=''):
        self.add('ERROR', code, where, msg, ref)

    def warn(self, code, where, msg, ref=''):
        self.add('WARN', code, where, msg, ref)

    def note(self, code, where, msg, ref=''):
        self.add('NOTE', code, where, msg, ref)

    def count(self, level):
        return sum(1 for i in self.items if i['level'] == level)


# ------------------------------------------------------------------------------------------------
# 5 · Tokens and ligatures
# ------------------------------------------------------------------------------------------------

SUF_RE = re.compile(r'(×3|x3|‿|½|\?|\*|/|\\|#\d+|@\d+|\^r\d+(?:/\d+)?)')


class Token:
    def __init__(self):
        self.pre = ''
        self.sign = None
        self.part = None
        self.plural = False
        self.kind = False
        self.half = False
        self.q = False
        self.root = False
        self.lean = None
        self.count = None
        self.ord = None
        self.span = None
        self.fringe = []
        self.fork = None      # (x_lig, y_lig) raw strings
        self.pair = None      # (Token, Token): the v1 pair (A=B)
        self.fold = None      # v1 fold [X within Y]: (inner, host)
        self.raw = ''

    @property
    def neg(self):
        return '!' in self.pre

    @property
    def hollow(self):
        return '~' in self.pre

    @property
    def smooth(self):
        return '_' in self.pre

    @property
    def caus(self):
        return '>' in self.pre

    def key(self):
        if self.pair:
            return '(%s=%s)' % (self.pair[0].key(), self.pair[1].key())
        k = self.sign + (':' + self.part if self.part else '')
        if self.plural:
            k += '×3'
        return k

    def canon(self):
        if self.pair:
            s = '(%s=%s)' % (self.pair[0].canon(), self.pair[1].canon())
        else:
            s = self.sign + (':' + self.part if self.part else '')
        pre = ''.join(c for c in '!~_>' if c in self.pre)
        suf = ''
        if self.plural:
            suf += '×3'
        if self.kind:
            suf += '‿'
        if self.half:
            suf += '½'
        if self.count:
            suf += '#%d' % self.count
        if self.ord:
            suf += '@%d' % self.ord
        if self.span:
            suf += '^r%d' % self.span[0] + ('/%d' % self.span[1] if self.span[1] else '')
        if self.q:
            suf += '?'
        if self.lean:
            suf += self.lean
        fr = '{%s}' % ','.join(self.fringe) if self.fringe else ''
        fk = '<%s|%s>' % self.fork if self.fork else ''
        fo = '[%s within %s]' % self.fold if self.fold else ''
        return pre + s + suf + fr + fk + fo + ('*' if self.root else '')


class Lig:
    def __init__(self):
        self.tokens = []
        self.band = None       # an item's own condition band: EARTH[MIST] (Addition A1)
        self.band_only = False  # [MIST]: the band alone, as a thing (Addition A1)
        self.raw = ''
        self.held_root = False  # v1: HOLD cupped round the pith at a root's foot

    @property
    def is_root(self):
        return any(t.root for t in self.tokens) or any(t.pair and (t.pair[0].root or t.pair[1].root) for t in self.tokens)

    @property
    def head(self):
        return self.tokens[-1] if self.tokens else None

    def signs(self):
        out = []
        for t in self.tokens:
            if t.pair:
                out += [t.pair[0].sign, t.pair[1].sign]
            elif t.sign:
                out.append(t.sign)
        return out

    def key(self):
        return '+'.join(t.key() for t in self.tokens)

    def canon(self):
        if self.band_only:
            return '[%s]' % self.band
        s = '+'.join(t.canon() for t in self.tokens)
        if self.band:
            s += '[%s]' % self.band
        return s


def _depth_step(ch, depth, angle, nxt=' '):
    """Bracket depth for scanning marks: ( [ { always nest; < > nest only as a fork (a > before a sign is the causative)."""
    if ch in '([{':
        depth += 1
    elif ch in ')]}':
        depth -= 1
    elif ch == '<':
        angle += 1
    elif ch == '>' and angle > 0 and not re.match(r'[A-Z!~_>(]', nxt):
        angle -= 1
    return depth, angle


def _split_plus(s):
    parts, depth, angle, cur = [], 0, 0, ''
    for k, ch in enumerate(s):
        depth, angle = _depth_step(ch, depth, angle, s[k + 1:k + 2] or ' ')
        if ch == '+' and depth == 0 and angle == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += ch
    parts.append(cur)
    return parts


def parse_token(s, F, where, ctx):
    t = Token()
    t.raw = s
    s = s.strip()
    m = re.match(r'([!~_>]*)', s)
    t.pre = m.group(1)
    rest = s[m.end():]
    if len(set(t.pre)) != len(t.pre):
        F.warn('M09', where, 'a flag is repeated in "%s"' % s)
    if rest.startswith('('):  # the v1 pair (A=B)
        depth, j = 0, 0
        for j, ch in enumerate(rest):
            depth += ch == '('
            depth -= ch == ')'
            if depth == 0:
                break
        inner = rest[1:j]
        if '=' not in inner:
            F.err('P10', where, 'a bracket in "%s" is neither a pair (A=B) nor a comment' % s)
            return None
        a, b = inner.split('=', 1)
        ta = parse_token(a.strip(), F, where, ctx)
        tb = parse_token(b.strip(), F, where, ctx)
        if not ta or not tb:
            return None
        t.pair = (ta, tb)
        t.sign = ta.sign
        rest = rest[j + 1:]
        ctx.setdefault('devices', set()).add('pair')
    else:
        m = re.match(r'([A-Z][A-Z0-9]*|grain-arc)(?::([a-z]+))?', rest)
        if not m:
            F.err('P11', where, 'no sign in "%s"' % s)
            return None
        t.sign = 'GRAIN' if m.group(1) == 'grain-arc' else m.group(1)
        t.part = m.group(2)
        rest = rest[m.end():]
    # suffixes, fringe, fork, fold (any order the v1 samples used)
    while rest:
        m = SUF_RE.match(rest)
        if m:
            x = m.group(1)
            if x in ('×3', 'x3'):
                if x == 'x3':
                    F.warn('P12', where, 'write ×3, not x3, in "%s"' % s)
                t.plural = True
            elif x == '‿':
                t.kind = True
            elif x == '½':
                t.half = True
            elif x == '?':
                t.q = True
            elif x == '*':
                t.root = True
            elif x in ('/', '\\'):
                t.lean = x
            elif x[0] == '#':
                t.count = int(x[1:])
            elif x[0] == '@':
                t.ord = int(x[1:])
            else:
                mm = re.match(r'\^r(\d+)(?:/(\d+))?', x)
                t.span = (int(mm.group(1)), int(mm.group(2)) if mm.group(2) else None)
            rest = rest[m.end():]
            continue
        if rest.startswith('{'):
            j = rest.find('}')
            if j < 0:
                F.err('P13', where, 'unclosed fringe in "%s"' % s)
                return None
            t.fringe += [x.strip() for x in rest[1:j].split(',') if x.strip()]
            rest = rest[j + 1:]
            continue
        if rest.startswith('<'):
            depth, j = 0, 0
            for j, ch in enumerate(rest):
                if ch == '<':
                    depth += 1
                elif ch == '>' and not re.match(r'[A-Z!~_>(]', rest[j + 1:j + 2] or ' '):
                    depth -= 1        # a '>' before a sign is the causative, not the fork's close
                if depth == 0:
                    break
            inner = rest[1:j]
            if '|' not in inner:
                F.err('P14', where, 'a fork needs two branches, <X|Y>, in "%s"' % s)
                return None
            x, y = inner.split('|', 1)
            t.fork = (x.strip(), y.strip())
            rest = rest[j + 1:]
            continue
        m = re.match(r'\[([A-Z0-9×‿½]+)\s+within\s+([A-Z]+)\]', rest)
        if m:
            t.fold = (m.group(1), m.group(2))
            rest = rest[m.end():]
            continue
        break
    if rest.strip():
        F.err('P15', where, 'unread text "%s" in "%s"' % (rest, s))
        return None
    return t


def check_token(t, F, where, ctx):
    """Sign-table and device checks on one token."""
    if t.pair:
        check_token(t.pair[0], F, where, ctx)
        check_token(t.pair[1], F, where, ctx)
        return
    if t.sign in GRAIN_ARC:
        if not ctx.get('name_ok'):
            F.err('M10', where, 'the grain-arc is cut only in names (in the bark, or a name in a pocket)',
                  'mystaeri_spec §3.14')
    elif t.sign not in SIGNS:
        near = [k for k in SIGNS if k.startswith(t.sign[:3])][:4]
        F.err('M01', where, 'unknown sign %s%s' % (t.sign, (' (nearest: %s)' % ', '.join(near)) if near else ''), '§9, v1 §3.5')
    if t.part:
        if (t.sign, t.part) not in PARTS:
            ok = sorted(p for (s, p) in PARTS if s == t.sign)
            F.err('M02', where, 'no part "%s" of %s%s' % (t.part, t.sign, (' (parts: %s)' % ', '.join(ok)) if ok else ' (it has no parts)'), '§5.2')
        ctx.setdefault('devices', set()).add('part')
    st = {}
    for fr in t.fringe:
        if fr not in FRINGE:
            F.err('M03', where, 'unknown fringe mark "%s" (one of %s)' % (fr, ', '.join(FRINGE)), '§5.4')
            continue
        if FRINGE[fr] in st:
            F.err('M04', where, 'two fringe marks on one station (%s and %s): at most one per station' % (st[FRINGE[fr]], fr), '§5.4')
        st[FRINGE[fr]] = fr
        ctx.setdefault('fringe', set()).add(fr)
    for n, nm in ((t.count, 'count'), (t.ord, 'ordinal')):
        if n is not None and not 1 <= n <= 4:
            F.err('M05', where, 'a %s is 1-4 bites (a count above four is a hand: X+HAND, X+HAND#n)' % nm, 'v1 §3.7, Addition A3')
    if t.count:
        ctx.setdefault('devices', set()).add('count')
    if t.ord:
        ctx.setdefault('devices', set()).add('ordinal')
    if t.kind and not t.plural:
        F.err('M06', where, 'the kind-arc ‿ follows ×3', '§5.3')
    if t.kind:
        ctx.setdefault('devices', set()).add('kind-arc')
    for flag, dev in (('~', 'hollow'), ('_', 'smoothed')):
        if flag in t.pre:
            ctx.setdefault('devices', set()).add(dev)
    if t.q:
        ctx.setdefault('devices', set()).add('question')
    if t.half:
        ctx.setdefault('devices', set()).add('half')
    if t.lean:
        ctx.setdefault('devices', set()).add('lean')
    if t.span:
        ctx.setdefault('devices', set()).add('span')
    if t.fork:
        ctx.setdefault('devices', set()).add('fork')
        for br in t.fork:
            if br.strip() in ('', '…', '...'):
                continue
            sub = parse_ligature(br.strip(), F, where + ' (fork branch)', ctx)
            if sub:
                for tk in sub.tokens:
                    if tk.half and tk.sign in LINE_ROOTS:
                        ctx.setdefault('devices', set()).add('chain')
    if t.fold:
        ctx.setdefault('devices', set()).add('fold')


def parse_ligature(s, F, where, ctx=None, item=False):
    """Parse a mark or pocket item; returns Lig or None. ctx collects devices used."""
    if ctx is None:
        ctx = {}
    L = Lig()
    L.raw = s
    s = s.strip()
    if not s:
        F.err('P16', where, 'an empty mark')
        return None
    m = re.match(r'^\[([A-Z]+)\]$', s)
    if m:
        if m.group(1) not in BANDS:
            F.err('M07', where, 'unknown band %s' % m.group(1), 'v1 §3.6')
            return None
        if not item:
            F.err('K10', where, 'a band alone, [%s], stands only as a pocket item or a grain fragment' % m.group(1), 'Addition A1')
        L.band_only, L.band = True, m.group(1)
        return L
    m = re.match(r'^(.*?)\[([A-Z]+)\]$', s)
    if m and m.group(2) in BANDS:
        s, L.band = m.group(1), m.group(2)
        if not item:
            F.err('K10', where, 'X[%s] (a band on one item) is written only inside a pocket; in a year, write "band %s files a–b"' % (L.band, L.band), 'Addition A1')
    parts = _split_plus(s)
    for p in parts:
        fm = re.match(r'^\s*\[([A-Z0-9×‿½]+)\s+within\s+([A-Z]+)\](\*?)\s*$', p)
        if fm and L.tokens:          # v1: the fold [X within Y] rides on the sign before it (the sliver, VI-1)
            L.tokens[-1].fold = (fm.group(1), fm.group(2))
            if fm.group(3):
                L.tokens[-1].root = True
            ctx.setdefault('devices', set()).add('fold')
            continue
        t = parse_token(p, F, where, ctx)
        if t is None:
            return None
        L.tokens.append(t)
    for t in L.tokens:
        check_token(t, F, where, ctx)
    n = len(L.tokens)
    # v1: HOLD cupped round the pith at the root's foot is a device, not a ligature part (mystaeri_spec §3.7)
    if n >= 2 and L.tokens[0].sign == 'HOLD' and L.is_root and not L.tokens[0].pre:
        L.held_root = True
        n -= 1
        ctx.setdefault('devices', set()).add('held-at-root')
    if n > 2:
        F.err('M08', where, '"%s" is a ligature of %d signs: a mark is one sign or a ligature of two; cut the rest '
              'as its own mark and join it by a runner' % (s, n), '§10.2')
    if len(L.tokens) > 1:
        ctx.setdefault('devices', set()).add('ligature')
    return L


# ------------------------------------------------------------------------------------------------
# 6 · The round model and the line parser
# ------------------------------------------------------------------------------------------------

class Mark:
    def __init__(self, pith, file, cell, ring, year, lig, line):
        self.pith, self.file, self.cell, self.ring, self.year = pith, file, cell, ring, year
        self.lig, self.line = lig, line
        self.cell_written = cell is not None
        self.conds = []

    def addr(self):
        p = 'p%d·' % self.pith if self.pith is not None else ''
        return '%s%d%s.r%d/%d' % (p, self.file, ('.%d' % self.cell) if self.cell_written else '', self.ring, self.year)

    def pos(self):
        return (self.ring, self.year, -1 if self.pith is None else self.pith, self.file, self.cell or 1)


class Pocket:
    def __init__(self, pid, kind, s0, s1, items, ring, year, line, parent=None):
        self.pid, self.kind, self.s0, self.s1, self.items = pid, kind, s0, s1, items
        self.ring, self.year, self.line, self.parent = ring, year, line, parent

    def files(self):
        n = (self.s1 - self.s0) % 16 + 1
        return [(self.s0 + i) % 16 for i in range(n)]

    def pos(self):
        return (self.ring, self.year, -1, self.s0, 0)


class Runner:
    def __init__(self, rid, src, role, targets, flags, line, split=False):
        self.rid, self.src, self.role, self.targets = rid, src, role, targets
        self.flags, self.line, self.split = flags, line, split
        self.hidden = '_' in flags
        self.seeming = '~' in flags


class Round:
    def __init__(self, rid, header_line):
        self.id = rid
        self.header_line = header_line
        self.attrs = {}
        self.wood = None
        self.pith = 'round'
        self.npith = 1
        self.K = None
        self.rules = []
        self.cells = None
        self.axis = None
        self.kind = None
        self.kind_why = ''
        self.marks = []
        self.pockets = {}
        self.conds = []          # (ring, year, band, s0, s1, line)
        self.empty = set()
        self.ring_band = {}      # ring -> declared band
        self.rule_lines = []     # rings after which a band-rule line stood
        self.bark = []           # (file, Lig, line)
        self.pale = 0
        self.runners = []
        self.laps = []           # (over, under, line)
        self.braids = []         # (bid, strands, pattern, line)
        self.binds = []          # (kid, strands, out (arrow, addr) or None, line)
        self.rays = []           # (file, (r,y), (r,y), line)
        self.mems = []           # (file, (r,y), line)
        self.grafts = []
        self.labels = []         # (file, from_ring, label)
        self.order_log = []      # the written order, for the canonical check
        self.lines = []


def _ints(s):
    return int(s)


def _strip_comment(line):
    s = line.rstrip('\n')
    if s.strip().startswith('#'):
        return ''
    s = re.sub(r'\s#\s.*$', '', s)
    return s


def parse_text(text, F, srcname='<text>'):
    """Parse one or more rounds; returns [Round]."""
    rounds = []
    R = None
    section = None
    band = None
    lines = text.split('\n')
    for ln, raw in enumerate(lines, start=1):
        where = '%s:%d' % (srcname, ln)
        st = raw.strip()
        if not st:
            continue
        lab = re.match(r'#\s*file\s+(\d+)(?:\s+from\s+r(\d+))?\s*[:=]\s*(.+)$', st)
        if lab and R is not None:
            R.labels.append((int(lab.group(1)), int(lab.group(2) or 1), lab.group(3).strip()))
            continue
        if st.startswith('#') or st.startswith('```'):
            continue
        s = _strip_comment(raw)
        if not s.strip():
            continue
        st = s.strip()
        if st.startswith('round '):
            R = Round(None, ln)
            rounds.append(R)
            section, band = 'body', None
            F.current = None
            parse_header(R, st, F, where)
            F.current = R.id
            for it in F.items:
                if it['round'] is None and it['where'] == where:
                    it['round'] = R.id
            continue
        if R is None:
            F.err('P01', where, 'text before the first "round" line: "%s"' % st[:60])
            continue
        R.lines.append((ln, raw))
        # remove trailing comments "(…)" after two spaces (v1 samples), but keep pairs (A=B)
        st = re.sub(r'(?:\s{2,}|^)\((?![^)]*=)[^)]*\)\s*$', '', st).strip()
        if not st:
            continue
        if st in ('I', 'II', 'III'):
            band = st
            section = 'body'
            continue
        if st.startswith('‖'):
            prev = max([m.ring for m in R.marks] + [p.ring for p in R.pockets.values()] + list(R.empty) + [0])
            R.rule_lines.append((prev, '¦' in st, ln))
            continue
        if st == 'bark':
            section = 'bark'
            continue
        if st == 'runners' or st == 'devices':
            section = 'devices'
            continue
        m = re.match(r'^r(\d+)(?:([/·])(\d+))?(?=\s|$)(.*)$', st)
        if m and section in ('body', None):
            ring, year = int(m.group(1)), int(m.group(3) or 1)
            if m.group(2) == '·':
                R.knowing_form = True
            m = re.match(r'^r(\d+)(?:[/·](\d+))?(?=\s|$)(.*)$', st)
            if m.group(2) is None and R.attrs.get('_v2'):
                pass
            if band:
                R.ring_band.setdefault(ring, (band, ln))
            parse_yearline(R, ring, year, m.group(3), F, where, ln)
            continue
        if st.startswith('bark ') and re.match(r'bark\s+\d+\s*:', st):
            mm = re.match(r'bark\s+(\d+)\s*:\s*(.+)$', st)
            ctx = {'name_ok': True}
            lig = parse_ligature(mm.group(2).strip(), F, where, ctx, item=True)
            if lig:
                R.bark.append((int(mm.group(1)), lig, ln))
            continue
        if re.match(r'pale\s+\d+$', st):
            R.pale = int(st.split()[1])
            continue
        # device lines (possibly several, separated by ·)
        parse_devices(R, st, F, where, ln)
    for R in rounds:
        F.current = R.id
        if getattr(R, 'knowing_form', False):
            pack_round(R, F, srcname)
        finish_round(R, F, srcname)
    F.current = None
    return rounds


def pack_round(R, F, src):
    """Section 4.3: knowings in telling order; each mark takes the next free cell of its file, cell by cell, then the
    next year; a pocket takes a whole year across its files, above the highest cursor among them. Rewrites years,
    cells and the runners' knowing addresses (file[.n].rK·i) into canonical addresses."""
    R.packed_from = {}
    rings = sorted(set([mk.ring for mk in R.marks] + [P.ring for P in R.pockets.values()] + [c[0] for c in R.conds]))
    kmap = {}   # (ring, knowing, file, nth) -> mark
    orig = {id(mk): mk.year for mk in R.marks}          # the knowing each mark was written in
    porig = {P.pid: P.year for P in R.pockets.values()}
    corig = list(R.conds)
    for k in rings:
        c = cells_of(R, k) or (1 if k == 1 else 1)
        cursor = {}
        knowings = sorted(set([orig[id(mk)] for mk in R.marks if mk.ring == k] + [porig[P.pid] for P in R.pockets.values() if P.ring == k and not P.parent]
                              + [cd[1] for cd in corig if cd[0] == k]))
        row_of = {}
        for i in knowings:
            pk = [P for P in R.pockets.values() if P.ring == k and porig[P.pid] == i and not P.parent]
            pfiles = [f for P in pk for f in P.files()]
            if pfiles:
                row = max([cursor.get(f, (0, 0))[0] + (1 if cursor.get(f, (0, 0))[1] else 0) for f in pfiles] + [0])
                for f in pfiles:
                    cursor[f] = (row + 1, 0)
                for P in pk:
                    P.year = row + 1
                row_of[i] = row
            nth = {}
            for mk in [m for m in R.marks if m.ring == k and orig[id(m)] == i]:
                key = (mk.pith, mk.file)
                rw, cl = cursor.get(key, (0, 0))
                nth[key] = nth.get(key, 0) + 1
                kmap[(k, i, mk.pith, mk.file, nth[key])] = mk
                mk.year, mk.cell = rw + 1, cl + 1
                row_of.setdefault(i, rw)
                cl += 1
                if cl >= c:
                    rw, cl = rw + 1, 0
                cursor[key] = (rw, cl)
            row_of.setdefault(i, 0)
        R.conds = [((kk, row_of.get(y0, 0) + 1, b, s0, s1, ln) if kk == k else cur)
                   for (kk, y0, b, s0, s1, ln), cur in zip(corig, R.conds)]
    for P in R.pockets.values():
        if P.parent and P.parent in R.pockets:
            P.year = R.pockets[P.parent].year
    # cells are written where a file holds more than one mark in a year
    groups = {}
    for mk in R.marks:
        groups.setdefault((mk.ring, mk.year, mk.pith, mk.file), []).append(mk)
    for g_ in groups.values():
        for mk in g_:
            mk.cell_written = len(g_) > 1

    def conv(a, rid):
        a = a.strip()
        m = re.match(r'^(?:p(\d+)·)?(\d+)(?:\.(\d+))?\.r(\d+)·(\d+)$', a)
        if not m:
            return a
        p = int(m.group(1)) if m.group(1) is not None else None
        mk = kmap.get((int(m.group(4)), int(m.group(5)), p, int(m.group(2)), int(m.group(3) or 1)))
        if not mk:
            F.err('R04', '%s:%d' % (src, R.header_line), 'runner %s: no mark %s in that knowing' % (rid, a))
            return a
        return mk.addr()
    for rn in R.runners:
        rn.src = conv(rn.src, rn.rid)
        rn.targets = [conv(t, rn.rid) if not t.startswith(('@', 'bind ')) else re.sub(r'\.r(\d+)·(\d+)', lambda m_: '.r%s/%d' % (
            m_.group(1), (min([mm.year for mm in R.marks if mm.ring == int(m_.group(1))] or [1]))), t) for t in rn.targets]
    for i, (kid, st, o, ln) in enumerate(R.binds):
        if o:
            R.binds[i] = (kid, st, (o[0], conv(o[1], kid)), ln)
    R.order_log = [x for x in R.order_log if x[0] == 'runner']


def parse_header(R, st, F, where):
    m = re.match(r'round\s+(\S+)\s*(\([^)]*\))?\s*\{(.*)\}\s*$', st)
    if not m:
        F.err('H01', where, 'a header is "round ID {wood: …; pith: …; rings: K; rules after: […]}"', '§13.2')
        m2 = re.match(r'round\s+(\S+)', st)
        R.id = m2.group(1) if m2 else '?'
        return
    R.id = m.group(1)
    comment = (m.group(2) or '').lower()
    body = m.group(3)
    # split on ';' outside brackets
    attrs, depth, cur = [], 0, ''
    for ch in body:
        depth += ch in '(['
        depth -= ch in ')]'
        if ch == ';' and depth == 0:
            attrs.append(cur)
            cur = ''
        else:
            cur += ch
    attrs.append(cur)
    for a in attrs:
        a = re.sub(r'\([^)]*\)', '', a).strip()
        if not a:
            continue
        if a.startswith('axis'):
            mm = re.match(r'axis\s*:?\s*(-?\d+)', a)
            R.axis = int(mm.group(1)) if mm else None
            continue
        if ':' not in a:
            F.err('H02', where, 'unreadable header attribute "%s"' % a)
            continue
        k, v = [x.strip() for x in a.split(':', 1)]
        R.attrs[k] = v
        if k == 'wood':
            if v not in WOODS:
                F.err('H03', where, 'wood "%s" is not one of %s' % (v, ', '.join(WOODS)), '§13.2')
            R.wood = v
        elif k == 'pith':
            mm = re.match(r'(round|war)(?:\s*×\s*(\d+))?$', v)
            if not mm:
                F.err('H04', where, 'pith is "round" or "war", with "×n" for joined piths', '§13.2')
            else:
                R.pith = mm.group(1)
                R.npith = int(mm.group(2) or 1)
        elif k == 'rings':
            mm = re.match(r'(\d+)', v)
            R.K = int(mm.group(1)) if mm else None
            if R.K is None or R.K > 24:
                F.err('H05', where, 'rings is a number, at most 24', 'v1 §3.2')
        elif k == 'rules after':
            R.rules = [int(x) for x in re.findall(r'\d+', v)]
        elif k == 'cells':
            R.cells = [int(x) for x in re.findall(r'\d+', v)]
        elif k == 'kind':
            if v not in ('telling', 'order', 'chip'):
                F.err('H06', where, 'kind is telling, order or chip', 'Addition A10')
            R.kind, R.kind_why = v, 'declared in the header'
        else:
            F.warn('H07', where, 'unknown header attribute "%s"' % k)
    if 'chip' in comment:
        R.kind, R.kind_why = 'chip', 'the header calls it a chip'
    if R.wood is None:
        F.err('H08', where, 'the header gives no wood')


def _addr_parse(s):
    m = re.match(r'^(?:p(\d+)·)?(\d+)(?:\.(\d+))?\.r(\d+)(?:/(\d+))?$', s)
    if not m:
        return None
    return (int(m.group(1)) if m.group(1) is not None else None, int(m.group(2)),
            int(m.group(3)) if m.group(3) else None, int(m.group(4)), int(m.group(5) or 1))


def _brace_end(s, i):
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return j
    return -1


def _pocket_from(R, s, F, where, ring, year, ln, parent=None, depth=1):
    """s starts with 'pocket'. Returns (Pocket, consumed) or (None, consumed)."""
    m = re.match(r'pocket\s+(\S+)\s+(said|cut)\s+(\d+)\s*[–-]\s*(\d+)\s*\{', s)
    if not m:
        F.err('P20', where, 'a pocket is "pocket P said|cut s0–s1 { item  item … }"', '§13.2')
        j = s.find('}')
        return None, (j + 1 if j >= 0 else len(s))
    j = _brace_end(s, m.end() - 1)
    if j < 0:
        F.err('P21', where, 'a pocket\'s braces do not close')
        return None, len(s)
    inner = s[m.end():j]
    pid = m.group(1)
    P = Pocket(pid, m.group(2), int(m.group(3)), int(m.group(4)), [], ring, year, ln, parent)
    if pid in R.pockets:
        F.err('K01', where, 'pocket id %s is used twice' % pid)
    R.pockets[pid] = P
    if depth > 2:
        F.err('K02', where, 'a pocket may hold one pocket: depth 2 at most', '§8')
    # items: separated by two spaces (or a semicolon, Addition A2); nested pockets by braces
    k = 0
    inner_s = inner
    while k < len(inner_s):
        while k < len(inner_s) and inner_s[k] in ' ;':
            k += 1
        if k >= len(inner_s):
            break
        if inner_s.startswith('pocket', k):
            sub, used = _pocket_from(R, inner_s[k:], F, where, ring, year, ln, parent=pid, depth=depth + 1)
            if sub:
                P.items.append(('pocket', sub.pid))
            k += used
            continue
        # one item runs to two spaces or a ';' outside brackets
        depth_b, ang, e = 0, 0, k
        while e < len(inner_s):
            ch = inner_s[e]
            depth_b, ang = _depth_step(ch, depth_b, ang, inner_s[e + 1:e + 2] or ' ')
            if depth_b == 0 and ang == 0 and (inner_s.startswith('  ', e) or ch == ';'):
                break
            e += 1
        tok = inner_s[k:e].strip()
        if tok:
            ctx = {'name_ok': True}
            lig = parse_ligature(tok, F, where + ' (pocket %s)' % pid, ctx, item=True)
            if lig:
                P.items.append(('lig', lig))
                R._ctx_devices.update(ctx.get('devices', set()))
                R._ctx_fringe.update(ctx.get('fringe', set()))
        k = e
    return P, j + 1


def parse_yearline(R, ring, year, rest, F, where, ln):
    if not hasattr(R, '_ctx_devices'):
        R._ctx_devices, R._ctx_fringe = set(), set()
    s = rest
    i = 0
    got = 0
    while i < len(s):
        while i < len(s) and s[i] in ' \t·':
            i += 1
        if i >= len(s):
            break
        sub = s[i:]
        if sub.startswith('pocket'):
            P, used = _pocket_from(R, sub, F, where, ring, year, ln)
            if P:
                R.order_log.append(('pocket', P, ln))
                got += 1
            i += used
            continue
        m = re.match(r'band\s+([A-Z]+)(?:\s+r(\d+)(?:\s*[–-]\s*r?(\d+))?)?\s+(?:(all\s+files)|(?:files?|slots?)\s+(-?\d+)(?:\s*[–-]\s*(-?\d+))?)', sub)
        if m:
            b = m.group(1)
            if b not in BANDS:
                F.err('M07', where, 'unknown band %s' % b, 'v1 §3.6')
            r0 = int(m.group(2)) if m.group(2) else ring
            if m.group(2) and int(m.group(2)) != ring:
                F.warn('S08', where, 'band written in ring %d carries "r%s"' % (ring, m.group(2)))
            if m.group(4):
                s0, s1 = 0, 15
            else:
                s0 = int(m.group(5)) % 16
                s1 = int(m.group(6)) % 16 if m.group(6) is not None else s0
            R.conds.append((r0, year, b, s0, s1, ln))
            i += m.end()
            continue
        m = re.match(r'mem\s+(?:file\s+|slot\s+)?(\d+)\s*:\s*r(\d+)(?:/(\d+))?\s*→\s*pith', sub)
        if m:
            R.mems.append((int(m.group(1)), (int(m.group(2)), int(m.group(3) or 1)), ln))
            i += m.end()
            continue
        m = re.match(r'graft\(([^)]*)\)', sub)
        if m:
            R.grafts.append((ring, m.group(1), ln))
            R._ctx_devices.add('graft')
            i += m.end()
            continue
        m = re.match(r'(?:p(\d+)·\s*)?(\d+)(?:\.(\d+))?\s*:\s*', sub)
        if m:
            j = m.end()
            depth, ang, e = 0, 0, j
            while e < len(sub):
                ch = sub[e]
                depth, ang = _depth_step(ch, depth, ang, sub[e + 1:e + 2] or ' ')
                if depth == 0 and ang == 0 and sub.startswith('  ', e):
                    break
                e += 1
            ligs = sub[j:e].strip()
            ctx = {}
            lig = parse_ligature(ligs, F, where, ctx)
            if lig:
                mk = Mark(int(m.group(1)) if m.group(1) is not None else None, int(m.group(2)),
                          int(m.group(3)) if m.group(3) else None, ring, year, lig, ln)
                mk.devices = ctx.get('devices', set())
                mk.fringe = ctx.get('fringe', set())
                R.marks.append(mk)
                R.order_log.append(('mark', mk, ln))
                got += 1
            i += e
            continue
        if sub.startswith('('):
            j = sub.find(')')
            i += (j + 1) if j >= 0 else len(sub)
            continue
        F.err('P02', where, 'unreadable "%s"' % sub[:50].strip())
        break
    if got == 0 and not any(c[0] == ring and c[1] == year for c in R.conds):
        R.empty.add(ring)


def parse_devices(R, st, F, where, ln):
    pieces = [p.strip() for p in re.split(r'\s+·\s+', st) if p.strip()]
    last_kw = None
    for p in pieces:
        p = re.sub(r'\s*\((?:does it to|when|because|when/because)[^)]*\)\s*$', '', p).strip()
        if not re.match(r'(run|lap|braid|bind|ray|mem|tie|band)\b', p) and last_kw == 'tie' and '→' in p:
            p = 'tie ' + p
        kw = p.split()[0]
        last_kw = kw
        if kw == 'run':
            parse_runner(R, p, F, where, ln)
        elif kw == 'lap':
            m = re.match(r'lap\s+(\S+)\s*⊳\s*(\S+)$', p)
            if not m:
                F.err('P30', where, 'a lap is "lap A ⊳ B" (A thwarts B)', '§7.1')
            else:
                R.laps.append((m.group(1), m.group(2), ln))
        elif kw == 'braid':
            m = re.match(r'braid\s+(\S+)\s+(.+?)\s*:\s*([abc]+!?)$', p)
            if not m:
                F.err('P31', where, 'a braid is "braid B r1 r2 [r3] : abab[!]"', '§7.2')
            else:
                R.braids.append((m.group(1), m.group(2).split(), m.group(3), ln))
        elif kw == 'bind':
            m = re.match(r'bind\s+(\S+)\s+(.+?)(?:\s+(→|⇒)\s+(\S+))?$', p)
            if not m:
                F.err('P32', where, 'a bind is "bind K r1 r2 [r3] [→|⇒ addr]"', '§7.3')
            else:
                R.binds.append((m.group(1), m.group(2).split(), (m.group(3), m.group(4)) if m.group(3) else None, ln))
        elif kw == 'ray':
            m = re.match(r'ray\s+(?:file\s+|slot\s+)?(\d+)\s*:\s*r(\d+)(?:/(\d+))?\s*[–-]\s*r(\d+)(?:/(\d+))?', p)
            if not m:
                F.err('P33', where, 'a ray is "ray s: ri–rj"', 'v1 §3.7')
            else:
                R.rays.append((int(m.group(1)), (int(m.group(2)), int(m.group(3) or 1)),
                               (int(m.group(4)), int(m.group(5) or 1)), ln))
        elif kw == 'mem':
            m = re.match(r'mem\s+(?:file\s+|slot\s+)?(\d+)\s*:\s*r(\d+)(?:/(\d+))?\s*→\s*pith', p)
            if not m:
                F.err('P34', where, 'a memory ray is "mem s: rk → pith"', 'v1 §3.7')
            else:
                R.mems.append((int(m.group(1)), (int(m.group(2)), int(m.group(3) or 1)), ln))
        elif kw == 'tie':
            m = re.match(r'tie\s+(\S+)\s*→\s*(\S+)', p)
            if not m:
                F.err('P35', where, 'a v1 tie is "tie a.ri → b.rj"', '§13.7')
                continue
            a, b = _addr_parse(m.group(1)), _addr_parse(m.group(2))
            if not a or not b:
                F.err('P35', where, 'a v1 tie joins two addresses, "file.rK"')
                continue
            role = 'to' if a[3] == b[3] else 'then'
            rid = 't%d' % (len([r for r in R.runners if r.rid.startswith('t')]) + 1)
            R.runners.append(Runner(rid, m.group(1), role, [m.group(2)], '', ln))
            R.runners[-1].from_tie = True
        elif kw == 'band':
            m = re.match(r'band\s+([A-Z]+)\s+r(\d+)(?:\s*[–-]\s*r?(\d+))?\s+(?:(all\s+files)|(?:files?|slots?)\s+(-?\d+)(?:\s*[–-]\s*(-?\d+))?)', p)
            if not m:
                F.err('P36', where, 'a band line is "band X rK files a–b"')
                continue
            r0 = int(m.group(2))
            r1 = int(m.group(3)) if m.group(3) else r0
            if m.group(4):
                s0, s1 = 0, 15
            else:
                s0 = int(m.group(5)) % 16
                s1 = int(m.group(6)) % 16 if m.group(6) is not None else s0
            for r in range(r0, r1 + 1):
                R.conds.append((r, 1, m.group(1), s0, s1, ln))
        else:
            F.err('P03', where, 'unreadable line "%s"' % p[:60])


def parse_runner(R, p, F, where, ln):
    m = re.match(r'run\s+(\S+)\s+(\S+)\s+(→in|→with|→for|→bc|→as|→thru|→that|→|⇒)\s+(.+?)\s*$', p)
    if not m:
        F.err('P40', where, 'a runner is "run ID SOURCE ROLE TARGET [_|~]"', '§13.2')
        return
    rid, src, arrow, tgt = m.group(1), m.group(2), m.group(3), m.group(4)
    flags = ''
    mm = re.match(r'^(.*?)\s+([_~]+)$', tgt)
    if mm:
        tgt, flags = mm.group(1), mm.group(2)
    role = ARROWS[arrow]
    split = False
    if tgt.startswith('{'):
        split = True
        targets = [x.strip() for x in tgt.strip('{}').split(',') if x.strip()]
    elif tgt.startswith('bind '):
        targets = [tgt]
    else:
        targets = [tgt]
    if role == 'bc' and targets == ['∅']:
        role = 'blind'
    R.runners.append(Runner(rid, src, role, targets, flags, ln, split))
    R.order_log.append(('runner', R.runners[-1], ln))


# ------------------------------------------------------------------------------------------------
# 7 · Checks on a parsed round
# ------------------------------------------------------------------------------------------------

def band_of(R, k):
    rules = R.rules or []
    if not rules or k <= rules[0]:
        return 'I'
    if len(rules) < 2 or k <= rules[1]:
        return 'II'
    return 'III'


def cells_of(R, k):
    if R.cells and 1 <= k <= len(R.cells):
        return R.cells[k - 1]
    return None


def finish_round(R, F, srcname):
    where0 = '%s:%d' % (srcname, R.header_line)
    if not hasattr(R, '_ctx_devices'):
        R._ctx_devices, R._ctx_fringe = set(), set()
    # resolve cells: a mark without a written cell is cell 1
    for mk in R.marks:
        if mk.cell is None:
            mk.cell = 1
    infer_kind(R, F, where0)
    check_structure(R, F, srcname)
    check_marks(R, F, srcname)
    check_pockets(R, F, srcname)
    check_runners(R, F, srcname)
    check_crossings(R, F, srcname)
    check_v1_devices(R, F, srcname)
    check_gating(R, F, srcname)
    check_canonical(R, F, srcname)


def infer_kind(R, F, where):
    if R.kind:
        return
    roots = [mk for mk in R.marks if mk.lig.is_root]
    seal = any(f == 0 and lig.tokens and lig.tokens[0].sign == 'HOLD' and len(lig.tokens) == 1 for (f, lig, _) in R.bark)
    if R.wood == 'plain' or not roots:
        R.kind, R.kind_why = 'chip', ('wood: plain' if R.wood == 'plain' else 'it has no root')
    elif seal:
        R.kind, R.kind_why = 'telling', 'the seal (bark 0: HOLD) stands in its bark'
    elif all(r.lig.head.sign in LINE_ROOTS for r in roots):
        R.kind, R.kind_why = 'order', 'its root is a line root and it has no seal'
    else:
        R.kind, R.kind_why = 'telling', 'its root %s is not a line root' % roots[0].lig.head.sign
    F.note('H10', where, 'read as %s (%s); override with "kind:" in the header or --kind' % (R.kind, R.kind_why), 'Addition A10')


def check_structure(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    rings = sorted(set([mk.ring for mk in R.marks] + [p.ring for p in R.pockets.values()] + list(R.empty)
                       + [c[0] for c in R.conds]))
    K = R.K
    if K is None:
        K = max(rings) if rings else 0
        R.K = K
    for k in rings:
        if k > K:
            F.err('S01', w(R.header_line), 'ring %d is cut, but the header gives %d rings' % (k, K), '§13.2')
    if R.kind != 'chip':
        missing = [k for k in range(1, K + 1) if k not in rings]
        if missing:
            F.note('S02', w(R.header_line), 'ring%s %s not written: read as empty (a morrow passes); write "r%d ·" to say so'
                   % ('s' if len(missing) > 1 else '', ', '.join(map(str, missing)), missing[0]), 'v1 §3.7')
    # years contiguous
    for k in rings:
        ys = sorted(set([mk.year for mk in R.marks if mk.ring == k] + [p.year for p in R.pockets.values() if p.ring == k and not p.parent]
                        + [c[1] for c in R.conds if c[0] == k]))
        if ys and ys != list(range(1, ys[-1] + 1)):
            F.warn('S03', w(R.header_line), 'ring %d: years %s are not 1…n' % (k, ys), '§4.2')
    # header cells
    if R.cells is not None:
        if len(R.cells) != K:
            F.err('H09', w(R.header_line), 'cells lists %d rings, the round has %d' % (len(R.cells), K), '§13.2')
        if R.cells and R.cells[0] != 1:
            F.err('H09', w(R.header_line), 'ring 1 always has one cell per slot', '§4.4')
        for a, b in zip(R.cells, R.cells[1:]):
            if b < a:
                F.warn('H09', w(R.header_line), 'cells shrink outward (%s): outer rings have more girth, never fewer cells' % R.cells, '§4.4')
                break
        if any(not 1 <= c <= 4 for c in R.cells):
            F.err('H09', w(R.header_line), 'a ring has 1–4 cells per slot', '§4.4')
    # bands and rules
    if len(R.rules) > 2:
        F.err('S04', w(R.header_line), 'at most two band-rules', 'v1 §3.3')
    for a, b in zip(R.rules, R.rules[1:]):
        if b <= a:
            F.err('S04', w(R.header_line), 'band-rules must stand in order')
    for k, (b, ln) in sorted(R.ring_band.items()):
        want = band_of(R, k)
        if b != want:
            F.err('S05', w(ln), 'ring %d stands under band %s, but "rules after: %s" puts it in band %s' % (k, b, R.rules, want), 'v1 §3.3')
    written = [r for (r, _, _) in R.rule_lines]
    v1form = not any(re.match(r'\s*r\d+/\d+', raw) for (_, raw) in R.lines)
    for r in R.rules:
        if r not in written:
            F.add('NOTE' if v1form else 'WARN', 'S06', w(R.header_line), 'no band-rule line (‖) after ring %d, where "rules after" puts one' % r, '§13.2')
    for (r, _, ln) in R.rule_lines:
        if r not in R.rules:
            F.err('S07', w(ln), 'a band-rule line after ring %d, which "rules after" does not name' % r)


def _marks_at(R, ring, year, file, pith=None):
    return [mk for mk in R.marks if mk.ring == ring and mk.year == year and mk.file == file and mk.pith == pith]


def check_marks(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    # cells: written only when needed; contiguous; within the ring's count
    groups = {}
    for mk in R.marks:
        groups.setdefault((mk.ring, mk.year, mk.pith, mk.file), []).append(mk)
        if not 0 <= mk.file <= 15:
            F.err('M11', w(mk.line), 'file %d: files are 0–15' % mk.file, 'v1 §3.3')
        if mk.cell_written and not 1 <= mk.cell <= 4:
            F.err('M12', w(mk.line), 'cell %d: cells are 1–4' % mk.cell, '§4.4')
    for (k, y, p, f), ms in groups.items():
        cs = sorted(m.cell for m in ms)
        if len(ms) > 1 and any(not m.cell_written for m in ms):
            F.err('M13', w(ms[0].line), 'file %d holds %d marks in r%d/%d: write each one\'s cell (%d.1, %d.2 …)' % (f, len(ms), k, y, f, f), '§13.2')
        if len(ms) == 1 and ms[0].cell_written:
            F.warn('M14', w(ms[0].line), 'the cell is written only when a file holds more than one mark in a year (%s)' % ms[0].addr(), '§13.2')
        if len(set(cs)) != len(cs):
            F.err('M15', w(ms[0].line), 'two marks in one cell (file %d, r%d/%d): one mark per cell' % (f, k, y), '§10.2')
        elif cs and cs != list(range(1, len(cs) + 1)):
            F.warn('M16', w(ms[0].line), 'cells on file %d in r%d/%d are %s, not 1…n: marks take the next free cell' % (f, k, y, cs), '§4.3')
        c = cells_of(R, k)
        if c is not None and max(cs) > c:
            F.err('M17', w(ms[0].line), 'file %d in r%d/%d uses cell %d, but ring %d has %d cell%s per slot' % (f, k, y, max(cs), k, c, '' if c == 1 else 's'), '§4.4')
    # packing: a file fills its year before the next, unless a pocket took a year across it
    if R.cells:
        for k in sorted(set(mk.ring for mk in R.marks)):
            c = cells_of(R, k) or 1
            byf = {}
            for mk in R.marks:
                if mk.ring == k:
                    byf.setdefault((mk.pith, mk.file), {}).setdefault(mk.year, 0)
                    byf[(mk.pith, mk.file)][mk.year] += 1
            for (p, f), ys in byf.items():
                yl = sorted(ys)
                for a, b in zip(yl, yl[1:]):
                    if ys[a] < c:
                        pk = [P for P in R.pockets.values() if P.ring == k and not P.parent and a < P.year < b + 1 and f in P.files()]
                        if not pk:
                            F.warn('M18', '%s:ring %d' % (src, k), 'file %d has a free cell in r%d/%d but cuts again in r%d/%d: '
                                   'each mark takes the next free cell of its file (a pocket between would explain it)' % (f, k, a, k, b), '§4.3')
                            break
    # roots
    roots = [mk for mk in R.marks if mk.lig.is_root]
    if R.kind != 'chip':
        piths = list(range(R.npith)) if R.npith > 1 else [None]
        for p in piths:
            rs = [mk for mk in roots if mk.pith == p]
            label = ('pith %d' % p) if p is not None else 'the round'
            if not rs:
                F.err('M20', '%s:%d' % (src, R.header_line), '%s has no root (a mark ending in *)' % label, '§10.1')
            elif len(rs) > 1:
                F.err('M21', w(rs[1].line), '%s has %d roots: one root per round (per pith when joined)' % (label, len(rs)), '§10.1')
        for mk in roots:
            if mk.ring != 1 or mk.year != 1 or mk.file != 0:
                F.err('M22', w(mk.line), 'the root is cut in ring 1, year 1, on file 0 (it is at %s)' % mk.addr(), '§10.1')
            if R.npith > 1 and mk.pith is None:
                F.err('M23', w(mk.line), 'in a joined round every root stands on its own pith (pN·0)', 'v1 §3.3')
            if R.kind == 'order' and mk.lig.head.sign not in LINE_ROOTS:
                F.warn('M24', w(mk.line), 'an order\'s root is one of the ten line roots or Burn (%s is not; the council\'s own carving is the one exception)' % mk.lig.head.sign, 'v1 §3.5')
        for mk in R.marks:
            if mk.ring == 1 and not mk.lig.is_root:
                if R.kind == 'order':
                    F.err('M25', w(mk.line), 'an order cuts nothing in ring 1 but its root (%s)' % mk.addr(), 'v1 §3.8.1')
                elif mk.file in (15, 0, 1) and (mk.pith is None or R.npith > 1):
                    F.err('M26', w(mk.line), 'files 15, 0 and 1 of every year of ring 1 are the root\'s (%s)' % mk.addr(), '§10.1')
    # spans and questions
    for mk in R.marks:
        for t in mk.lig.tokens:
            if t.span:
                if t.span[0] <= mk.ring:
                    F.err('M27', w(mk.line), 'a span runs outward: ^r%d from ring %d' % (t.span[0], mk.ring), 'v1 §3.7')
                elif R.K and t.span[0] > R.K:
                    F.err('M27', w(mk.line), 'a span to ring %d, beyond the round\'s %d rings' % (t.span[0], R.K))
    # conditions
    for (k, y, b, s0, s1, ln) in R.conds:
        if b not in BANDS:
            continue
        if not (0 <= s0 <= 15 and 0 <= s1 <= 15):
            F.err('M28', w(ln), 'a band spans files 0–15')
    # bark
    for (f, lig, ln) in R.bark:
        if f != 0:
            F.warn('M29', w(ln), 'names and the seal stand in the bark on file 0', 'v1 §3.7')


def check_pockets(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    that = {}
    for rn in R.runners:
        if rn.role == 'that':
            for t in rn.targets:
                that.setdefault(t, []).append(rn.rid)
    for pid, P in R.pockets.items():
        n = len(P.files())
        if n > 6:
            F.err('K03', w(P.line), 'pocket %s spans %d files (%d–%d): a pocket spans at most six' % (pid, n, P.s0, P.s1), '§8')
        if len(P.items) > 8:
            F.err('K04', w(P.line), 'pocket %s holds %d items: at most eight' % (pid, len(P.items)), '§8')
        if not P.items:
            F.err('K05', w(P.line), 'pocket %s is empty' % pid)
        if not P.parent:
            clash = [mk for mk in R.marks if mk.ring == P.ring and mk.year == P.year and mk.file in P.files()]
            if clash:
                F.err('K06', w(P.line), 'pocket %s takes its year across files %d–%d, but %s is cut there too'
                      % (pid, P.s0, P.s1, ', '.join(m.addr() for m in clash)), '§4.3, §8')
            for Q in R.pockets.values():
                if Q is not P and not Q.parent and Q.ring == P.ring and Q.year == P.year and set(Q.files()) & set(P.files()) and Q.pid > P.pid:
                    F.err('K07', w(P.line), 'pockets %s and %s overlap in r%d/%d' % (P.pid, Q.pid, P.ring, P.year))
        rs = that.get(pid, [])
        if len(rs) != 1:
            F.err('K08', w(P.line), 'pocket %s has %d "that" runners: exactly one' % (pid, len(rs)), '§8')
        if P.ring == 1:
            F.err('A01', w(P.line), 'the heart ring takes no pocket', '§3')
        if P.kind == 'said':
            R._ctx_devices.add('said-pocket')
        else:
            R._ctx_devices.add('cut-pocket')


def _resolve(R, a, F, where, rid):
    """An address string to ('mark', Mark) | ('item', (Pocket, i)) | ('file', f) | ('pocket', P) | ('none',) | ('bind', kid)."""
    a = a.strip()
    if a == '∅':
        return ('none', None)
    if a.startswith('@'):
        mm = re.match(r'@(\d+)(?:\.r(\d+)(?:/(\d+))?)?$', a)
        if not mm or not 0 <= int(mm.group(1)) <= 15:
            F.err('R02', where, 'runner %s: "%s" is not a file referent @0…@15 (or @f.rK/Y)' % (rid, a), '§6.1, Addition A4')
            return None
        if mm.group(2):
            return ('file', int(mm.group(1)), (int(mm.group(2)), int(mm.group(3) or 1)))
        return ('file', int(mm.group(1)), None)
    if a.startswith('bind '):
        return ('bind', a.split()[1])
    mm = re.match(r'^([A-Za-z]\w*)\.(\d+)$', a)
    if mm and mm.group(1) in R.pockets:
        P = R.pockets[mm.group(1)]
        i = int(mm.group(2))
        if not 1 <= i <= len(P.items):
            F.err('R03', where, 'runner %s: pocket %s has no item %d' % (rid, P.pid, i), 'Addition A2')
            return None
        return ('item', (P, i))
    if a in R.pockets:
        return ('pocket', R.pockets[a])
    ad = _addr_parse(a)
    if not ad:
        F.err('R02', where, 'runner %s: cannot read the address "%s"' % (rid, a), '§13.2')
        return None
    p, f, c, k, y = ad
    ms = _marks_at(R, k, y, f, p)
    if not ms:
        F.err('R04', where, 'runner %s: nothing is cut at %s' % (rid, a))
        return None
    if c is None:
        if len(ms) > 1:
            F.err('R05', where, 'runner %s: %s holds %d marks: give the cell' % (rid, a, len(ms)), '§13.2')
            return None
        return ('mark', ms[0])
    hit = [m for m in ms if m.cell == c]
    if not hit:
        F.err('R04', where, 'runner %s: no cell %d at %s' % (rid, c, a))
        return None
    if len(ms) == 1:
        F.warn('M14', where, 'runner %s: %s writes a cell for a file that holds one mark' % (rid, a), '§13.2')
    return ('mark', hit[0])


def _ring_of(R, node, src_node=None):
    if node is None:
        return None
    if node[0] == 'mark':
        return (node[1].ring, node[1].year)
    if node[0] == 'item':
        return (node[1][0].ring, node[1][0].year)
    if node[0] == 'pocket':
        return (node[1].ring, node[1].year)
    if node[0] == 'file' and len(node) > 2 and node[2]:
        return node[2]
    return None


def check_runners(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    seen = {}
    R.rnode = {}
    for rn in R.runners:
        where = w(rn.line)
        if getattr(rn, 'from_tie', False):       # v1: a tie that ends where nothing is cut ties to that file's bearing
            ad = _addr_parse(rn.targets[0])
            if ad and not _marks_at(R, ad[3], ad[4], ad[1], ad[0]):
                rn.targets = ['@%d' % ad[1]]
                F.note('D06', where, 'v1 tie %s ends where nothing is cut: read as the file referent @%d (its bearing)' % (rn.rid, ad[1]), '§13.7')
        if rn.rid in seen:
            F.err('R01', where, 'runner id %s is used twice' % rn.rid)
        seen[rn.rid] = rn
        s = _resolve(R, rn.src, F, where, rn.rid)
        if s and s[0] not in ('mark', 'item'):
            F.err('R06', where, 'runner %s springs from %s: a runner springs from a mark\'s head' % (rn.rid, rn.src), '§6.1')
            s = None
        ts = [_resolve(R, t, F, where, rn.rid) for t in rn.targets]
        R.rnode[rn.rid] = (s, ts)
        if rn.split:
            R._ctx_devices.add('split')
            if len(rn.targets) > 3:
                F.err('R07', where, 'runner %s forks into %d shoots: at most three' % (rn.rid, len(rn.targets)), '§6.3')
            if len(rn.targets) < 2:
                F.warn('R07', where, 'runner %s is written as a split with one shoot' % rn.rid)
        if rn.hidden or rn.seeming:
            R._ctx_devices.add('hollow runner' if rn.seeming else 'smoothed runner')
        if s is None:
            continue
        sring = _ring_of(R, s)
        for t, traw in zip(ts, rn.targets):
            if t is None:
                continue
            kind = t[0]
            # role fits target
            if rn.role == 'that' and kind != 'pocket':
                F.err('R10', where, 'runner %s: a "that" runner ends in a pocket\'s mouth, not %s' % (rn.rid, traw), '§6.1, §8')
            if kind == 'pocket' and rn.role != 'that':
                F.err('R11', where, 'runner %s ends on pocket %s: only a "that" runner enters a pocket\'s mouth' % (rn.rid, traw), '§6.3.4')
            if kind == 'none' and rn.role not in ('blind', 'to'):
                F.err('R12', where, 'runner %s: ∅ (empty wood) ends only the blind, "→bc ∅" (why), or "→ ∅" (whither)' % rn.rid, '§6.1, Addition A5')
            if kind == 'none' and rn.role == 'to':
                R._ctx_devices.add('blind')
            if rn.role == 'blind':
                R._ctx_devices.add('blind')
            if kind == 'file':
                R._ctx_devices.add('file referent')
                if rn.role not in ('to', 'in'):
                    F.err('R13', where, 'runner %s: a file referent @f takes a runner of role to or in, not %s' % (rn.rid, rn.role), '§6.1')
                if s[0] == 'item':
                    F.err('R14', where, 'runner %s: inside a pocket there are no files to point at' % rn.rid, 'Addition A2')
                elif s[0] == 'mark':
                    mk = s[1]
                    tr, ty = (t[2] if t[2] else (mk.ring, mk.year))
                    c = cells_of(R, tr)
                    here = _marks_at(R, tr, ty, t[1], mk.pith)
                    n = len(here)
                    if c is not None and n >= c and not (t[1] == mk.file and (tr, ty) == (mk.ring, mk.year)):
                        F.warn('R15', where, 'runner %s → @%d: file %d has no free cell in r%d/%d for the terminal; '
                               'its referent is cut there (%s), so run to that mark instead' % (rn.rid, t[1], t[1], tr, ty, here[0].addr()), '§6.1, §10.11')
                    if tr == 1 and t[1] in (15, 0, 1) and R.kind != 'chip':
                        F.err('R19', where, 'runner %s → @%d in the heart ring: files 15, 0 and 1 of ring 1 are the root\'s, and a terminal '
                              'cannot stand in the root; point at the file in a later ring (@%d.rK/Y)' % (rn.rid, t[1], t[1]), '§10.1, Addition A4')
                    if any(P.ring == tr and P.year == ty and not P.parent and t[1] in P.files() for P in R.pockets.values()):
                        F.err('R16', where, 'runner %s → @%d: a pocket fills file %d in that year' % (rn.rid, t[1], t[1]), '§6.3.4')
            if kind == 'bind' and rn.role not in ('to', 'then'):
                F.err('R17', where, 'runner %s: a bind\'s strand is a runner of role to or then' % rn.rid, '§7.3')
            # items: runners stay inside their pocket
            if s[0] == 'item' or kind == 'item':
                sp = s[1][0].pid if s[0] == 'item' else None
                tp = t[1][0].pid if kind == 'item' else (t[1].parent if kind == 'pocket' else None)
                if s[0] == 'item' and kind == 'pocket':
                    tp = t[1].parent
                if sp != tp:
                    F.err('R18', where, 'runner %s crosses a pocket\'s border (%s → %s): runners among items stay in their pocket' % (rn.rid, rn.src, traw), '§6.3.4, Addition A2')
            # direction
            tring = _ring_of(R, t)
            if tring is None and kind == 'file':
                tring = sring
            if tring and sring:
                if tring[0] < sring[0]:
                    F.err('R20', where, 'runner %s runs inward, ring %d to ring %d: only memory runs inward' % (rn.rid, sring[0], tring[0]), '§6.2.4')
                elif tring[0] > sring[0] and rn.role not in ('then', 'to', 'that'):
                    F.err('R21', where, 'runner %s crosses rings %d→%d as "%s": across rings a runner is then (or to)' % (rn.rid, sring[0], tring[0], rn.role), '§6.3.2')
                elif tring[0] > sring[0] and rn.role == 'that':
                    F.warn('R21', where, 'runner %s ("that") crosses rings to its pocket' % rn.rid)
            if kind == 'mark' and s[0] == 'mark' and t[1] is s[1]:
                F.err('R22', where, 'runner %s ends on its own source' % rn.rid)
        if rn.role not in ('to', 'then'):
            R._ctx_devices.add('role ' + rn.role)
    # duplicates (same source, role, target)
    sig = {}
    for rn in R.runners:
        for t in rn.targets:
            k = (rn.src, rn.role, t)
            if k in sig:
                F.err('R23', w(rn.line), 'runners %s and %s have one source, one role and one target: they are one runner' % (sig[k], rn.rid), '§6.3.3')
            sig[k] = rn.rid
    if any(rn.role != 'blind' for rn in R.runners):
        R._ctx_devices.add('runner')


def check_crossings(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    ids = {rn.rid: rn for rn in R.runners}

    def span(rid):
        s, ts = R.rnode.get(rid, (None, []))
        rings = []
        for n in [s] + ts:
            r = _ring_of(R, n)
            if r:
                rings.append(r[0])
        return (min(rings), max(rings)) if rings else None

    under_count = {}
    for (a, b, ln) in R.laps:
        R._ctx_devices.add('break')
        for x in (a, b):
            if x not in ids:
                F.err('X01', w(ln), 'lap names runner %s, which is not written' % x, '§7.1')
        if a == b:
            F.err('X02', w(ln), 'a runner cannot thwart itself')
        if a in ids and b in ids:
            sa, sb = span(a), span(b)
            if sa and sb and (sa[1] < sb[0] or sb[1] < sa[0]):
                F.err('X03', w(ln), 'lap %s ⊳ %s: the two runners share no ring, so they cannot cross' % (a, b), '§7.1')
        under_count[b] = under_count.get(b, 0) + 1
    in_braid = {}
    for (bid, strands, pat, ln) in R.braids:
        R._ctx_devices.add('braid')
        if not 2 <= len(strands) <= 3:
            F.err('X10', w(ln), 'braid %s has %d strands: two or three' % (bid, len(strands)), '§7.2')
        letters = set(pat.rstrip('!'))
        allowed = set('abc'[:len(strands)])
        if not letters <= allowed:
            F.err('X11', w(ln), 'braid %s: pattern "%s" names strands it does not have' % (bid, pat), '§7.2')
        if len(pat.rstrip('!')) > 9:
            F.err('X12', w(ln), 'braid %s: a pattern is at most nine crossings' % bid, '§13.2')
        if len(strands) == 3 and pat.rstrip('!')[:3] != 'abc' and len(set(pat.rstrip('!'))) == 3:
            F.note('X13', w(ln), 'braid %s: the standard plait of three reads "abcabc…"' % bid, '§7.2')
        rings = set()
        for x in strands:
            if x not in ids:
                F.err('X14', w(ln), 'braid %s names runner %s, which is not written' % (bid, x))
                continue
            if x in in_braid:
                F.err('X15', w(ln), 'runner %s is in braids %s and %s' % (x, in_braid[x], bid))
            in_braid[x] = bid
            sp = span(x)
            if sp:
                rings |= set(range(sp[0], sp[1] + 1))
        spans = [span(x) for x in strands if x in ids]
        if spans and all(spans) and len(set(sp for sp in spans)) > 1 and not set.intersection(*[set(range(a, b + 1)) for a, b in spans]):
            F.err('X16', w(ln), 'braid %s: its strands share no ring; a braid runs along one ring' % bid, '§7.2, §15')
    for (kid, strands, out, ln) in R.binds:
        R._ctx_devices.add('bind')
        if not 2 <= len(strands) <= 3:
            F.err('X20', w(ln), 'bind %s has %d strands: two, or three as two locks' % (kid, len(strands)), '§7.3')
        for x in strands:
            if x not in ids:
                F.err('X21', w(ln), 'bind %s names runner %s, which is not written' % (kid, x))
            elif not any(t.strip() == 'bind ' + kid for t in ids[x].targets):
                F.err('X22', w(ln), 'bind %s: strand %s does not end on the bind (write "run %s … → bind %s")' % (kid, x, x, kid), '§7.3')
        for rn in R.runners:
            if any(t.strip() == 'bind ' + kid for t in rn.targets) and rn.rid not in strands:
                F.err('X23', w(rn.line), 'runner %s ends on bind %s but is not one of its strands' % (rn.rid, kid))
        if out:
            node = _resolve(R, out[1], F, w(ln), 'bind ' + kid)
            if node and node[0] != 'mark':
                F.err('X24', w(ln), 'bind %s: its out-runner goes to a mark' % kid, '§7.3')
    for rn in R.runners:
        for t in rn.targets:
            if t.startswith('bind ') and t.split()[1] not in [b[0] for b in R.binds]:
                F.err('X25', w(rn.line), 'runner %s ends on bind %s, which is not written' % (rn.rid, t.split()[1]))


def check_v1_devices(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    for (f, (ri, yi), (rj, yj), ln) in R.rays:
        R._ctx_devices.add('ray')
        if rj <= ri:
            F.err('D01', w(ln), 'a ray runs outward, from an inner ring to an outer one')
        for (r, y) in ((ri, yi), (rj, yj)):
            banded = any(c[0] == r and f in [(c[3] + i) % 16 for i in range((c[4] - c[3]) % 16 + 1)] for c in R.conds)
            if not banded and not any(mk.file == f and mk.ring == r for mk in R.marks):
                F.warn('D02', w(ln), 'ray %d: r%d–r%d: nothing is cut on file %d in ring %d' % (f, ri, rj, f, r), 'v1 §3.8.7')
    for (f, (r, y), ln) in R.mems:
        R._ctx_devices.add('memory ray')
        if not any(mk.file == f and mk.ring == r for mk in R.marks):
            F.warn('D03', w(ln), 'memory ray on file %d from ring %d: no mark there to remember' % (f, r))
    for rn in R.runners:
        if getattr(rn, 'from_tie', False):
            F.note('D04', w(rn.line), 'v1 tie read as runner %s %s %s (%s)' % (rn.src, ROLE_ARROW[rn.role], rn.targets[0], rn.role), '§13.7')
    if R.npith > 1:
        R._ctx_devices.add('joined piths')
    for (f, lig, ln) in R.bark:
        if not (lig.tokens and lig.tokens[0].sign == 'HOLD' and len(lig.tokens) == 1):
            R._ctx_devices.add('name')
    if R.pale:
        R._ctx_devices.add('pale ring')
        if not 1 <= R.pale <= 3:
            F.err('D05', w(R.header_line), 'a Throne closes 1–3 pale rings', 'v1 §3.7')
    for mk in R.marks:
        R._ctx_devices.update(mk.devices)
        R._ctx_fringe.update(mk.fringe)
        if mk.cell > 1:
            R._ctx_devices.add('cells')
        if mk.year > 1:
            R._ctx_devices.add('years')


# the devices each age of wood may carry (section 3; cumulative); names of devices as collected above
DEVICE_AGE = {
    'runner': 1, 'ligature': 1, 'count': 2, 'ordinal': 2, 'memory ray': 2, 'fork': 2, 'question': 2, 'cut-pocket': 2,
    'blind': 2, 'ray': 1, 'span': 1, 'role in': 3, 'role with': 3, 'role for': 3, 'role bc': 3, 'role as': 3,
    'role thru': 3, 'role that': 2, 'file referent': 3, 'break': 3, 'braid': 3, 'bind': 3, 'hollow': 3, 'smoothed': 3,
    'hollow runner': 3, 'smoothed runner': 3, 'part': 3, 'kind-arc': 3, 'cells': 3, 'joined piths': 3, 'pair': 3,
    'half': 3, 'chain': 3, 'split': 3, 'graft': 3, 'said-pocket': 4, 'name': 3, 'pale ring': 4, 'lean': 3, 'years': 2,
    'held-at-root': 0, 'fold': 0,
}


def check_gating(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    devs = set(R._ctx_devices)
    fr = set(R._ctx_fringe)
    # position (every round): the heart ring and, in a telling, band I
    for mk in R.marks:
        if mk.ring == 1 and mk.fringe:
            F.err('A02', w(mk.line), 'the heart ring takes no fringe (%s at %s)' % (', '.join(sorted(mk.fringe)), mk.addr()), '§3')
    rule1 = R.rules[0] if R.rules else (R.K or 0)
    for rn in R.runners:
        s, ts = R.rnode.get(rn.rid, (None, []))
        r = _ring_of(R, s)
        if not r:
            continue
        for coll, label in ((R.laps, 'break'), (R.braids, 'braid'), (R.binds, 'bind')):
            for item in coll:
                names = (item[0], item[1]) if label == 'break' else item[1]
                if rn.rid in names:
                    if r[0] == 1:
                        F.err('A03', w(rn.line), 'the heart ring takes no %s (runner %s)' % (label, rn.rid), '§3')
                    elif R.kind == 'telling' and r[0] <= rule1 and R.rules:
                        F.err('A04', w(rn.line), 'in a telling, band I takes runners and the fringe but no %s (runner %s, ring %d); '
                              'the fine devices grow beyond band-rule 1' % (label, rn.rid, r[0]), '§3, Addition A9')
    if R.kind == 'telling' and R.rules:
        for P in R.pockets.values():
            if P.ring <= rule1 and P.ring != 1:
                F.err('A04', w(P.line), 'in a telling, band I takes no pocket (%s in ring %d)' % (P.pid, P.ring), '§3, Addition A9')
        for mk in R.marks:
            if mk.ring <= rule1 and mk.cell > 2:
                F.err('A05', w(mk.line), 'band I takes at most two cells (%s)' % mk.addr(), '§3')
    # age (orders only: a telling, and the eldest, may carry everything)
    if R.kind != 'order':
        return
    age = AGE.get(R.wood, 4)
    for d in sorted(devs):
        need = DEVICE_AGE.get(d, 0)
        if need > age:
            F.err('A10', w(R.header_line), '%s is carried by %s and older; this order is %s' % (d, AGE_NAME[need], AGE_NAME[age]), '§3')
    for f in sorted(fr):
        need = 2 if f in FRINGE_LIFE else 4
        if need > age:
            F.err('A11', w(R.header_line), 'the fringe mark "%s" is carried by %s and older; this order is %s' % (f, AGE_NAME[need], AGE_NAME[age]), '§3')
    marked = sorted(set(mk.ring for mk in R.marks))
    if age == 0:
        extra = [mk for mk in R.marks if not mk.lig.is_root]
        if extra or R.runners or (R.K or 1) > 1:
            F.err('A12', w(R.header_line), 'green wood holds one sign, from the pith: nothing else', '§3')
    if age == 1:
        if len([r for r in R.runners]) > 1:
            F.err('A13', w(R.header_line), 'wood of forty summers holds one runner ("a word, and waits for its brother")', '§3')
        for rn in R.runners:
            if rn.role not in ('to', 'then'):
                F.err('A13', w(rn.line), 'wood of forty summers holds only a then or to runner')
        if len(marked) > 2:
            F.err('A14', w(R.header_line), 'wood of forty summers has two marked rings (and empty ones)', '§3')
    ymax = max([mk.year for mk in R.marks] + [1])
    if age == 2 and ymax > 2:
        F.err('A15', w(R.header_line), 'a shore-man\'s life has at most two years a ring', '§3')
    if age == 3 and ymax > 4:
        F.err('A15', w(R.header_line), 'a long life has at most four years a ring', '§3')
    K = R.K or 0
    lim = {1: (2, 99), 2: (3, 6), 3: (4, 9)}.get(age)
    if lim and not lim[0] <= K <= lim[1]:
        F.warn('A16', w(R.header_line), '%s grows %d–%d rings; this order has %d' % (AGE_NAME[age], lim[0], lim[1] if lim[1] < 99 else 2, K), 'v1 §3.9')
    if R.bark and age < 3:
        F.warn('A17', w(R.header_line), 'a name in the bark: §3 gives names to the eldest; E4-01 (a long life) has one', '§3, Addition A10')


def _run_sort_key(R, rn):
    s, ts = R.rnode.get(rn.rid, (None, []))

    def key(n, src_pos=None):
        if n is None:
            return (99, 99, 99, 99, 99)
        if n[0] == 'mark':
            m = n[1]
            return (m.ring, m.year, -1 if m.pith is None else m.pith, m.file, m.cell)
        if n[0] == 'item':
            P, i = n[1]
            return (P.ring, P.year, -1, P.s0, 10 + i)
        if n[0] == 'pocket':
            P = n[1]
            return (P.ring, P.year, -1, P.s0, 9)
        if n[0] == 'file':   # Addition A7: @f sorts at file f, in the source's ring and year, after its cells
            base = src_pos or (0, 0, -1, 0, 0)
            return (base[0], base[1], -1, n[1], 5)
        if n[0] == 'none':
            base = src_pos or (0, 0, -1, 0, 0)
            return (base[0], base[1], 98, 98, 98)
        if n[0] == 'bind':
            return (99, 0, 0, 0, 0)
        return (99, 99, 99, 99, 99)
    sp = key(s)
    tk = key(ts[0], sp) if ts else (99,)
    return (sp, tk, rn.rid)


def check_canonical(R, F, src):
    w = lambda ln: '%s:%d' % (src, ln)
    # marks and pockets within a ring line: by year, then pith, file, cell
    lastpos = None
    lastname = None
    for kind, obj, ln in R.order_log:
        if kind == 'runner':
            continue
        pos = obj.pos()
        name = obj.addr() if kind == 'mark' else 'pocket ' + obj.pid
        if lastpos is not None and pos < lastpos and not (kind == 'pocket'):
            F.warn('C01', w(ln), '%s is written after %s: marks go year by year, file by file clockwise from 0, cell by cell'
                   % (name, lastname), '§13.4')
        lastpos, lastname = pos, name
    rs = [rn for rn in R.runners if not getattr(rn, 'from_tie', False)]
    keys = [_run_sort_key(R, rn) for rn in rs]
    bad = [(rs[i], rs[i + 1]) for i in range(len(rs) - 1) if keys[i + 1] < keys[i]]
    for a, b in bad:
        F.add('NOTE' if getattr(R, 'knowing_form', False) else 'WARN', 'C02', w(b.line), 'runner %s is written after %s: runners go by source (ring, year, file, cell), then '
               'target, then id; a pass reads its over-strand by this order' % (b.rid, a.rid), '§13.4, Addition A7')
    R.canon_runner_order = [rn.rid for _, rn in sorted(zip(keys, rs), key=lambda x: x[0])]


# ------------------------------------------------------------------------------------------------
# 8 · Canonical GN
# ------------------------------------------------------------------------------------------------

def canon_gn(R):
    out = []
    attrs = ['wood: %s' % R.wood, 'pith: %s%s' % (R.pith, (' ×%d' % R.npith) if R.npith > 1 else ''),
             'rings: %d' % (R.K or 0), 'rules after: [%s]' % ', '.join(map(str, R.rules))]
    if R.cells:
        attrs.append('cells: [%s]' % ', '.join(map(str, R.cells)))
    if R.axis is not None:
        attrs.append('axis %d' % R.axis)
    out.append('round %s {%s}' % (R.id, '; '.join(attrs)))
    rings = sorted(set([mk.ring for mk in R.marks] + [p.ring for p in R.pockets.values() if not p.parent]
                       + [c[0] for c in R.conds] + list(R.empty)))
    cur = None
    for k in range(1, (R.K or 0) + 1):
        b = band_of(R, k)
        if b != cur:
            if cur is not None:
                out.append('  ‖')
            out.append('  ' + b)
            cur = b
        has = any(mk.ring == k for mk in R.marks) or any(P.ring == k for P in R.pockets.values()) or any(c[0] == k for c in R.conds)
        if k not in rings or not has:
            out.append('    r%d ·' % k)
            continue
        years = sorted(set([mk.year for mk in R.marks if mk.ring == k] + [p.year for p in R.pockets.values() if p.ring == k and not p.parent]
                           + [c[1] for c in R.conds if c[0] == k]))
        multi = len(years) > 1 or any(y > 1 for y in years)
        for y in years:
            items = []
            for mk in R.marks:
                if mk.ring == k and mk.year == y:
                    items.append((mk.pos(), 'm', mk))
            for P in R.pockets.values():
                if P.ring == k and P.year == y and not P.parent:
                    items.append((P.pos(), 'p', P))
            items.sort(key=lambda t: t[0])
            cells = []
            for _, kind, o in items:
                if kind == 'm':
                    many = len(_marks_at(R, k, y, o.file, o.pith)) > 1
                    pre = ('p%d·' % o.pith) if o.pith is not None else ''
                    cells.append('%s%d%s: %s' % (pre, o.file, ('.%d' % o.cell) if many else '', o.lig.canon()))
                else:
                    cells.append(_pocket_canon(R, o))
            conds = ['band %s files %d–%d' % (b_, s0, s1) for (kk, yy, b_, s0, s1, _) in R.conds if kk == k and yy == y]
            line = '    r%-4s ' % (('%d/%d' % (k, y)) if multi or True else str(k)) + '    '.join(cells)
            if conds:
                line += '      ' + '  '.join(conds)
            out.append(line.rstrip())
        if k in R.rules and k != (R.K or 0) and band_of(R, k + 1) != band_of(R, k):
            pass
    if R.bark or R.pale:
        out.append('  bark')
        for (f, lig, _) in R.bark:
            out.append('    bark %d: %s' % (f, lig.canon()))
        if R.pale:
            out.append('    pale %d' % R.pale)
    rs = [rn for rn in R.runners]
    if rs:
        out.append('  runners')
        keyed = sorted(rs, key=lambda rn: _run_sort_key(R, rn))
        for rn in keyed:
            if rn.split:
                tgt = '{%s}' % ', '.join(rn.targets)
            else:
                tgt = rn.targets[0]
            arrow = '→bc' if rn.role == 'blind' else ROLE_ARROW[rn.role]
            src = rn.src
            s = R.rnode.get(rn.rid, (None, []))[0]
            if s and s[0] == 'mark':
                src = s[1].addr()
            fl = (' _' if rn.hidden else '') + (' ~' if rn.seeming else '')
            out.append('    run %-4s %-13s %-6s %s%s' % (rn.rid, src, arrow, tgt, fl))
    for (a, b, _) in R.laps:
        out.append('  lap  %s ⊳ %s' % (a, b))
    for (bid, st, pat, _) in R.braids:
        out.append('  braid %s %s : %s' % (bid, ' '.join(st), pat))
    for (kid, st, o, _) in R.binds:
        out.append('  bind %s %s%s' % (kid, ' '.join(st), (' %s %s' % o) if o else ''))
    for (f, a, b, _) in R.rays:
        out.append('  ray %d: r%d/%d–r%d/%d' % (f, a[0], a[1], b[0], b[1]))
    for (f, a, _) in R.mems:
        out.append('  mem %d: r%d/%d → pith' % (f, a[0], a[1]))
    return '\n'.join(out)


def _pocket_canon(R, P):
    items = []
    for kind, it in P.items:
        if kind == 'pocket':
            items.append(_pocket_canon(R, R.pockets[it]))
        else:
            items.append(it.canon())
    return 'pocket %s %s %d–%d { %s }' % (P.pid, P.kind, P.s0, P.s1, '  '.join(items))


# ------------------------------------------------------------------------------------------------
# 9 · Reading
# ------------------------------------------------------------------------------------------------

def _g(sid):
    if sid in GRAIN_ARC:
        sid = 'GRAIN'
    g = G.get(sid)
    if g:
        k, rest = g.split(':', 1)
        parts = rest.split('|') + ['', '']
        return k, parts[0], parts[1], parts[2]
    s = SIGNS.get(sid, {})
    gl = (s.get('gloss') or sid.lower()).split(';')[0].strip()
    c = sign_class(sid)
    return ({'act': 'v', 'quality': 'a'}.get(c, 'n'), gl, gl, '')


ARTS = ('a ', 'an ', 'the ', 'one ')
QUANT = {'all': 'all', 'few': 'few', 'half': 'half', 'more': 'more', 'most': 'most', 'only': 'only'}
ADVB = {'again': 'again', 'still': 'still', 'last': 'at the last', 'slow': 'slowly', 'gently': 'gently'}
MOD_ADJ = {'DEEP': 'old', 'NEW': 'new', 'TRUE': 'true', 'GREAT': 'great', 'THIN': 'thin', 'HOLY': 'holy',
           'GLAD': 'glad', 'OVER': 'high', 'SPENT': 'spent', 'SWIFT': 'swift', 'ANGER': 'hot', 'SHAME': 'shamed',
           'DYING': 'dying', 'LIVE': 'living', 'BURN': 'burning', 'SAPLING': 'young', 'US': "the long-lived's",
           'STONEFOLK': "the shore-men's", 'AXE': 'iron', 'SQUARE': 'stone', 'WOOD': 'wooden', 'DARK': 'dark',
           'LONE': 'own', 'SILVERBARK': 'silver', 'HOLY': 'holy', 'GRIEF': 'grieving', 'SAND': 'sand'}


def _strip_art(s):
    for a in ARTS:
        if s.startswith(a):
            return s[len(a):]
    return s


def _a(s):
    """Fix a/an."""
    return re.sub(r'\ba ([aeiouAEIOU])', r'an \1', re.sub(r'\ban ([^aeiouAEIOU\W])', r'a \1', s))


def _with_mod(adj, np):
    if np.startswith('many '):
        return 'many ' + adj + ' ' + np[5:]
    for a in ARTS:
        if np.startswith(a):
            return _a(a + adj + ' ' + np[len(a):])
    return adj + ' ' + np


def _ingw(w):
    irr = {'be': 'being', 'lie': 'lying', 'die': 'dying', 'see': 'seeing', 'flee': 'fleeing'}
    if w in irr:
        return irr[w]
    if w.endswith('ie'):
        return w[:-2] + 'ying'
    if w.endswith('e') and not w.endswith('ee'):
        return w[:-1] + 'ing'
    if re.search(r'[^aeiou][aeiou][bdgmnprt]$', w) and len(w) <= 4:
        return w + w[-1] + 'ing'
    return w + 'ing'


def _3sgw(w):
    irr = {'go': 'goes', 'do': 'does', 'have': 'has', 'be': 'is'}
    if w in irr:
        return irr[w]
    if re.search(r'(s|sh|ch|x|z|o)$', w):
        return w + 'es'
    if re.search(r'[^aeiou]y$', w):
        return w[:-1] + 'ies'
    return w + 's'


def _map_verbs(vp, fn):
    """Apply fn to the first word of the phrase and to the first word after each ' and '."""
    parts = vp.split(' and ')
    out = []
    for p in parts:
        ws = p.split(' ')
        if ws and ws[0] and ws[0] not in ('not', 'many', 'seem', 'make', 'no'):
            m = re.match(r"([A-Za-z'-]+)(.*)$", ws[0])
            if m:
                ws[0] = fn(m.group(1)) + m.group(2)
        out.append(' '.join(ws))
    return ' and '.join(out)


def conj(vp, plural):
    if vp.startswith('not '):
        return ('do not ' if plural else 'does not ') + vp[4:]
    if vp.startswith('seem to '):
        return ('seem to ' if plural else 'seems to ') + vp[8:]
    if vp.startswith('many '):
        return vp
    if vp.startswith('make '):
        return ('make ' if plural else 'makes ') + vp[5:]
    if plural:
        return vp.replace('be struck', 'are struck')
    return _map_verbs(vp, _3sgw)


def gerund(vp):
    if vp.startswith('not '):
        return 'not ' + _map_verbs(vp[4:], _ingw)
    if vp.startswith('make '):
        return 'making ' + vp[5:]
    return _map_verbs(vp, _ingw)


def token_phrase(t, as_mod=False):
    """(pos, phrase) for one token; pos is n / v / a. Verb phrases are in the base form."""
    if t.pair:
        a = token_phrase(t.pair[0])[1]
        b = token_phrase(t.pair[1])[1]
        return 'n', '%s and %s, grown from one foot, bound' % (a, b)
    k, sg, pl, caus = _g(t.sign)
    if t.part and (t.sign, t.part) in PARTS:
        k, sg = 'n', PARTS[(t.sign, t.part)]
        pl = {'a head': 'heads', 'a foot': 'feet', 'an arm': 'arms', 'a neck': 'necks', 'the keel': 'keels',
              "a shore-man's brow": "shore-men's brows"}.get(sg, _strip_art(sg) + 's')
    if t.half and t.sign in ROOT_READ:
        return 'n', 'a carving of the %s line ("%s"), cited by its root cut small' % (
            {'WAVE': 'Wave', 'LONE': 'Lone Stroke', 'BARB': 'Bar Before', 'SPARK': 'Spark', 'SQUARE': 'Mute Square',
             'MOUTHS': 'Two Mouths', 'STERN': 'Turned Stern', 'BREATH': 'Breath', 'KNOT': 'Knot', 'SMOOTH': 'Smoothed Cut',
             'BURN': 'Burn'}[t.sign], ROOT_READ[t.sign][2])
    if k == 'n':
        if t.plural and t.kind and t.sign in KIND_ARC:
            ph = KIND_ARC[t.sign]
        elif t.plural and t.kind:
            ph = 'the %s, as a whole kind' % (pl or sg)
        elif t.plural:
            ph = (None if (t.part or as_mod) else SPECIAL_PLURAL.get(t.sign)) or ('many ' + (pl or sg))
        else:
            ph = sg
        if t.count:
            ph = ('%s %s' % (CARD.get(t.count, t.count), pl or sg)) if t.count > 1 else 'one ' + _strip_art(sg)
        if t.ord:
            ph = 'the %s %s' % (ORDW.get(t.ord, str(t.ord)), _strip_art(sg))
        if t.half:
            if t.plural and not t.kind:
                ph = 'many small ' + (pl or sg)
            else:
                ph = _with_mod('small', ph if _strip_art(ph) != ph else 'a ' + ph)
        if t.caus:
            ph = 'the making of ' + ph
        if t.neg:
            ph = 'no ' + _strip_art(ph)
        if t.hollow:
            ph = _a('a seeming ' + _strip_art(ph)) + ' (shown, not meant)'
        if t.smooth:
            ph = 'a hidden ' + _strip_art(ph)
    elif k == 'a':
        ph = sg
        if t.neg:
            ph = 'not ' + ph
        if t.hollow:
            ph = 'seeming ' + ph
        if t.smooth:
            ph = 'hidden ' + ph
        if t.half:
            ph = 'a little ' + ph
    else:
        base = caus if (t.caus and caus) else (('make ' + sg + ' happen') if t.caus else sg)
        ph = base
        if t.plural:
            ph = 'many ' + gerund(ph)
        if t.count:
            ph = '%s %s' % (ph, NUMW.get(t.count, '%d times' % t.count))
        if t.ord:
            ph = '%s, the %s time' % (ph, ORDW.get(t.ord, str(t.ord)))
        if t.half:
            ph = ph + ' a little'
        if t.neg:
            ph = 'not ' + ph
        if t.hollow:
            ph = 'seem to ' + ph + ' (shown, not meant)'
        if t.smooth:
            ph = ph + ' unseen'
    q = [QUANT[f] for f in t.fringe if f in QUANT]
    adv = [ADVB[f] for f in t.fringe if f in ADVB]
    if q and k == 'a':
        ph = '%s %s' % (' '.join(q), ph)
        q = []
    if q:
        if k == 'n':
            core = ph if ph.startswith('the ') and t.plural else _strip_art(ph)
            if core.startswith('many '):
                core = core[5:]
            ph = '%s %s' % (' '.join(q), core)
        else:
            ph = '%s, %s' % (ph, ' '.join('wholly' if x == 'all' else ('the most' if x == 'most' else x) for x in q))
    if adv:
        ph = '%s %s' % (ph, ', '.join(adv))
    if t.span:
        ph += ', until ring %d' % t.span[0]
    if t.q:
        ph += '?'
    if t.lean:
        ph += ' (leaning %s)' % ('clockwise' if t.lean == '/' else 'counter-clockwise')
    if t.fork:
        ph += ' (if: %s; if not: %s)' % (lig_phrase_str(t.fork[0]), lig_phrase_str(t.fork[1]))
    if t.fold:
        ph += ' (folded in its %s: %s)' % (t.fold[1].lower(), lig_phrase_str(t.fold[0]))
    return k, ph


def lig_phrase_str(s):
    F = Findings()
    if s.strip() in ('…', '...', ''):
        return '…'
    L = parse_ligature(s, F, 'fork', {}, item=True)
    return lig_phrase(L)[1] if L else s


def lig_phrase(L, root_mode=None):
    """(pos, phrase) of a whole mark or item."""
    if L is None:
        return 'n', '?'
    if L.band_only:
        return 'n', BAND_THING[L.band]
    toks = L.tokens[1:] if L.held_root else L.tokens
    pre = 'held at the root, remembered: ' if L.held_root else ''
    band = (' ' + BAND_PHRASE[L.band]) if L.band else ''
    if root_mode and len(toks) == 1 and toks[0].sign in ROOT_READ and not toks[0].half:
        sig, young, word = ROOT_READ[toks[0].sign]
        return 'n', pre + '"%s"' % (young if (root_mode == 'green' and young) else sig)
    k0 = '+'.join(t.key() for t in toks)
    comp = COMPOUNDS.get(k0) or COMPOUNDS.get('+'.join(t.sign + (':' + t.part if t.part else '') for t in toks))
    if comp and len(toks) >= 2 or (comp and len(toks) == 1):
        kind, rest = comp.split(':', 1)
        sg = rest.split('|')[0]
        pl = (rest.split('|') + [''])[1]
        caus = (rest.split('|') + ['', ''])[2]
        flags = ''.join(t.pre for t in toks)
        ph = sg
        if toks[-1].plural and pl and '×3' not in k0.split('+')[0]:
            ph = pl
        if '>' in flags and kind == 'v':
            ph = caus or ('make ' + ph + ' happen')
        if '!' in flags:
            ph = ('not ' if kind == 'v' else 'no ') + _strip_art(ph)
        if '~' in flags:
            ph = ('seem to ' + ph if kind == 'v' else _a('a seeming ' + _strip_art(ph))) + ' (shown, not meant)'
        if '_' in flags:
            ph = (ph + ' unseen') if kind == 'v' else 'a hidden ' + _strip_art(ph)
        extras = []
        for t in toks:
            extras += [QUANT.get(f) or ADVB.get(f) for f in t.fringe]
            if t.count:
                extras.append(NUMW.get(t.count, '') if kind == 'v' else '(%s of them)' % CARD.get(t.count, t.count))
            if t.ord:
                extras.append('(the %s)' % ORDW.get(t.ord, t.ord))
            if t.half:
                extras.append('(small)')
            if t.q:
                extras.append('?')
            if t.lean:
                extras.append('(leaning %s)' % ('clockwise' if t.lean == '/' else 'counter-clockwise'))
            if t.span:
                extras.append(', until ring %d' % t.span[0])
        if extras:
            ph += ' ' + ' '.join(x for x in extras if x)
        return kind, pre + ph + band
    parts = [token_phrase(t, as_mod=(i < len(toks) - 1)) for i, t in enumerate(toks)]
    if len(parts) == 1:
        return parts[0][0], pre + parts[0][1] + band
    (k1, p1), (k2, p2) = parts[0], parts[-1]
    m, h = toks[0], toks[-1]
    if h.sign == 'HAND' and k1 == 'n' and not h.part:
        n = 5 * (h.count or 1)
        return 'n', pre + '%s (%d of them; or their hands)' % (p1, n) + band
    if k2 == 'v':
        if k1 == 'v':
            return 'v', pre + '%s and %s' % (p1, p2) + band
        if k1 == 'a':
            return 'v', pre + '%s, %s' % (p2, p1) + band
        return 'v', pre + '%s: %s' % (p2, p1) + band          # the doer as modifier: "send: many shore-men"
    if m.sign == 'BENEATH' and k2 == 'n':
        return 'n', pre + 'below ' + (p2 if p2.startswith('the ') else 'the ' + _strip_art(p2)) + band
    if m.sign in MOD_ADJ and not (m.part or m.neg or m.hollow or m.smooth or m.caus or m.count or m.ord or m.fringe) and k2 == 'n':
        adj = MOD_ADJ[m.sign]
        if m.plural and m.sign in ('US', 'STONEFOLK'):
            adj = adj
        elif m.sign in ('US', 'STONEFOLK'):
            adj = {'US': "one of us's", 'STONEFOLK': "a shore-man's"}[m.sign]
        if adj.endswith("'s"):
            return 'n', pre + adj + ' ' + _strip_art(p2) + band
        return 'n', pre + _with_mod(adj, p2 if (_strip_art(p2) != p2 or p2.startswith('many ')) else 'a ' + p2) + band
    if k1 == 'v':
        return 'n', pre + '%s %s' % (gerund(p1), _strip_art(p2)) + band
    if k1 == 'a':
        return 'n', pre + _with_mod(p1, p2 if _strip_art(p2) != p2 else 'a ' + p2) + band
    if m.part:
        return 'n', pre + '%s, and %s' % (p1, _strip_art(p2) if p2.startswith(('a ', 'an ')) else p2) + band
    return 'n', pre + '%s %s' % (_strip_art(p1), _strip_art(p2)) + band


TRANS = {'HOLD', 'TAKE', 'STRIKE', 'BREAK', 'CARRY', 'FIND', 'LOSE', 'TEND', 'GUIDE', 'CHOOSE', 'FOLLOW', 'EAT', 'HEAR',
         'OPEN', 'CLOSE', 'MEND', 'CARVE', 'GIFT', 'BOND', 'AXE', 'STOP', 'NAME', 'SING', 'BURN'}


def lig_parts(L, root_mode=None):
    """(kind, doer, phrase, transitive): a thing+act ligature gives its doer (STONEFOLK×3+>GO: the shore-men send)."""
    toks = L.tokens[1:] if (L and L.held_root) else (L.tokens if L else [])
    if L and not L.band_only and len(toks) == 2 and not L.held_root:
        k0 = '+'.join(t.key() for t in toks)
        comp = COMPOUNDS.get(k0) or COMPOUNDS.get('+'.join(t.sign for t in toks))
        a, b = toks
        if not comp and a.sign == 'LONE' and sign_class(b.sign) == 'act' and not a.pre:
            vk, vp = token_phrase(b)
            return 'v', None, vp + ', only', (b.sign in TRANS or b.caus)
        if not comp and (sign_class(a.sign) == 'thing' or a.sign in DOER_NOUN) and sign_class(b.sign) == 'act':
            doer = DOER_NOUN.get(a.sign) if (a.sign in DOER_NOUN and not (a.pre or a.plural or a.fringe)) else token_phrase(a)[1]
            vk, vp = token_phrase(b)
            if L.band:
                vp += ' ' + BAND_PHRASE[L.band]
            return 'v', doer, vp, (b.sign in TRANS or b.caus)
    kind, ph = lig_phrase(L, root_mode)
    head = toks[-1] if toks else None
    trans = bool(head) and (head.sign in TRANS or head.caus)
    if head and len(toks) == 2:
        key = '+'.join(t.sign for t in toks)
        trans = trans or key in TRANS_COMPOUNDS
    if kind == 'a' and not (L and L.band_only):
        return 'q', None, ph, False
    return kind, None, ph, trans


def verbify(mk_parts, L):
    """A thing-sign that is also an act (EYE, NAME, HAND) reads as its act when it sends a runner."""
    kind, doer, ph, tr = mk_parts
    toks = L.tokens[1:] if L.held_root else L.tokens
    if (kind == 'n' and toks and toks[-1].sign in DUAL_VERB and not toks[-1].plural and not toks[-1].part
            and (len(toks) == 1 or sign_class(toks[0].sign) != 'thing')):
        base = DUAL_VERB[toks[-1].sign]
        if toks[-1].caus:
            base = {'EYE': 'show', 'NAME': 'make name', 'HAND': 'make lay a hand on', 'GIFT': 'make give'}[toks[-1].sign]
        mod = ''
        if len(toks) == 2:
            mod = ' (' + token_phrase(toks[0], as_mod=True)[1] + ')'
        t = toks[-1]
        if t.neg:
            base = 'not ' + base
        extras = [QUANT.get(f) or ADVB.get(f) for f in t.fringe]
        if t.ord:
            extras.append('the %s time' % ORDW.get(t.ord, t.ord))
        if t.q:
            extras.append('?')
        return 'v', doer, base + mod + ((' ' + ' '.join(x for x in extras if x)) if extras else ''), True
    return mk_parts


DOER_NOUN = {'AXE': 'the iron'}
DUAL_VERB = {'EYE': 'look at', 'NAME': 'name', 'HAND': 'lay a hand on', 'GIFT': 'give'}
TRANS_COMPOUNDS = {'SQUARE+RISE', 'NEW+HOLD', 'TRUE+HOLD', 'BOND+HOLD', 'HEART+HOLD', 'MORROW+HOLD', 'CARVE+GROW',
                   'SWIFT+FOLLOW', 'EARTH+OPEN', 'HAND+GIFT', 'SEED+GROW'}


PLURAL_HEADS = ('the long-lived', 'the shore-men', 'many ', 'all ', 'children', 'kin', 'the root-men', 'we', 'they', 'you')


def forms(label):
    """(subject, object, possessive, plural) of a referent's label."""
    L = label.strip()
    for pro, obj, poss in (('we', 'us', 'our'), ('they', 'them', 'their'), ('you', 'you', 'your')):
        if L == pro or L.startswith(pro + ' '):
            rest = L[len(pro):]
            return L, obj + rest, poss, True
    core = re.split(r' of | \(|,', L)[0].strip()
    last = core.split(' ')[-1] if core else ''
    heads = r'^(?:the )?(?:long-lived|shore-men|many|all|children|kin|root-men|we|they|you)\b'
    plural = (bool(re.match(heads, L))
              or last in ('children', 'men', 'kin', 'people', 'folk', 'dead', 'young', 'long-lived', 'shore-men')
              or (core.endswith('s') and not core.endswith(('ss', 'us', "'s"))))
    base = re.sub(r'\s*\([^)]*\)', '', L)
    return L, L, (base + "'" if base.endswith('s') else base + "'s"), plural


# grain_v2 section 21.8, A16: a belonging stands on its owner's file (section 10.3) and never introduces a referent there.
BELONGINGS = {'MIND', 'WORD', 'NAME', 'BREATH', 'HAND', 'EYE', 'BONE', 'DUST'}   # and BLOOD, one's blood (not BLOOD×3, kin)
PLACE_PARTS = {'CASTLE': {'DOOR', 'SQUARE'}, 'HOUSE': {'DOOR', 'SQUARE'}}        # a built place's doors, walls, stones


def is_belonging(lig, owner_head):
    """True when a thing-mark standing first on a file is a belonging of the file's referent, not a new referent:
    a part (SIGN:part, unless the ligature is a named compound such as TAKE+SAIL:cloth, a net), a person's mind, word
    or words (a sentence, BOND+WORD×3), name, breath, hand, eye, bones or blood, the dust at a place, or a built
    place's doors and stones."""
    t = lig.tokens[-1]
    if t.part:
        key = '+'.join(x.sign + (':' + x.part if x.part else '') for x in lig.tokens)
        return key not in COMPOUNDS
    if t.sign in BELONGINGS or (t.sign == 'BLOOD' and not t.plural):
        return True
    return t.sign in PLACE_PARTS.get(owner_head, ())


class Reader:
    def __init__(self, R):
        self.R = R

    # --- referents -------------------------------------------------------------------------
    def label(self, f, ring, pith=None):
        R = self.R
        best = None
        for (ff, fr, lab) in R.labels:
            if ff == f and fr <= ring and (best is None or fr >= best[0]):
                best = (fr, lab)
        if best:
            return best[1]
        intro = None  # the first thing-sign standing first on the file introduces its referent (section 11.2)
        intro_head = None  # ... unless it is a belonging of the referent already there (section 21.8, A16)
        for k in range(1, min(ring, (R.K or 0)) + 1):
            ms = sorted([mk for mk in R.marks if mk.ring == k and mk.file == f and mk.pith == pith], key=lambda m: (m.year, m.cell))
            if (ms and not ms[0].lig.is_root and sign_class(ms[0].lig.tokens[-1].sign) == 'thing'
                    and not (intro and is_belonging(ms[0].lig, intro_head))):
                intro = lig_phrase(ms[0].lig)[1]
                intro_head = ms[0].lig.tokens[-1].sign
        if intro:
            return intro
        if R.kind == 'order' and f == 8 and band_of(R, min(ring, R.K or ring)) == 'III':
            return 'the aim (Cut against)'
        return BEARING.get(f, 'the one on file %d' % f)

    def conds_at(self, mk):
        out = []
        for (k, y, b, s0, s1, _) in self.R.conds:
            if k == mk.ring and y == mk.year and mk.file in [(s0 + i) % 16 for i in range((s1 - s0) % 16 + 1)]:
                out.append(BAND_PHRASE[b])
        return out

    def parts(self, mk):
        root_mode = None
        if mk.lig.is_root:
            root_mode = 'green' if self.R.wood == 'green' else 'sig'
        return lig_parts(mk.lig, root_mode)

    def raw(self, mk):
        kind, doer, ph, tr = self.parts(mk)
        if doer:
            ph = '%s: %s' % (ph, doer)
        c = self.conds_at(mk)
        return kind, ph + ((' ' + ', '.join(c)) if c else '')

    def is_intro(self, mk):
        """True when mk is the first mark on its file in its ring (it names the file's referent there)."""
        first = min([m for m in self.R.marks if m.ring == mk.ring and m.file == mk.file and m.pith == mk.pith],
                    key=lambda m: (m.year, m.cell))
        return first is mk

    def has_label(self, f, ring):
        return any(ff == f and fr <= ring for (ff, fr, _) in self.R.labels)

    def subject_clause(self, mk, conds=True, as_act=False):
        """The mark as a clause with its doer: 'the current takes', 'the shore-men send', 'the Guest: blood'."""
        kind, doer, ph, tr = self.parts(mk)
        c = self.conds_at(mk) if conds else []
        tail = (', ' + ', '.join(c)) if c else ''
        if mk.lig.is_root:
            return 'The root: %s%s' % (ph, tail)
        lab = self.label(mk.file, mk.ring, mk.pith)
        if as_act:
            kind, doer, ph, tr = verbify((kind, doer, ph, tr), mk.lig)
        subj, obj, poss, pl = forms(doer or lab)
        aim = self.R.kind == 'order' and band_of(self.R, mk.ring) == 'III' and mk.file == 8
        if kind == 'q':
            s = '%s %s %s' % (subj, 'are' if pl else 'is', ph)
        elif kind == 'v':
            s = '%s %s' % (subj, conj(ph, pl))
        elif lab == ph or _strip_art(lab) == _strip_art(ph):
            s = ph
        else:
            s = '%s: %s' % (subj, ph)
        return ('Cut against: ' + s + tail) if aim else s + tail

    def object_phrase(self, node, src=None):
        """The target of a runner, as an object."""
        if node is None:
            return '?'
        k = node[0]
        if k == 'mark':
            mk = node[1]
            kind, doer, ph, tr = self.parts(mk)
            lab = self.label(mk.file, mk.ring, mk.pith)
            subj, obj, poss, pl = forms(lab)
            c = self.conds_at(mk)
            if c:
                ph = ph + ' ' + ', '.join(c)
            if mk.lig.is_root:
                return 'the root (%s)' % ph
            if kind == 'v':
                if doer:
                    return '%s %s' % (doer, gerund(ph))
                return '%s %s' % (poss, gerund(ph))
            if kind == 'q':
                return '%s, %s' % (obj, ph)
            if lab == ph or _strip_art(lab) == _strip_art(ph):
                return ph
            if self.is_intro(mk):
                return ('%s (%s)' % (obj, ph)) if self.has_label(mk.file, mk.ring) else ph
            return '%s %s' % (poss, _strip_art(ph))
        if k == 'file':
            ring = node[2][0] if len(node) > 2 and node[2] else 99
            if src is not None and src[0] == 'mark' and src[1].file == node[1] and not (len(node) > 2 and node[2]):
                subj, obj, poss, pl = forms(self.label(node[1], src[1].ring))
                refl = {'us': 'ourselves', 'them': 'themselves', 'you': 'yourselves'}.get(obj.split(' ')[0], 'themselves' if pl else 'itself')
                return '%s (file %d)' % (refl, node[1])
            if src is not None and src[0] == 'mark':
                ring = src[1].ring if ring == 99 else ring
            return forms(self.label(node[1], ring))[1] + ' (file %d)' % node[1]
        if k == 'none':
            return ''
        if k == 'pocket':
            return self.pocket_phrase(node[1])
        if k == 'item':
            P, i = node[1]
            kind, it = P.items[i - 1]
            return lig_phrase(it)[1] if kind == 'lig' else self.pocket_phrase(self.R.pockets[it])
        if k == 'bind':
            return 'the bind %s' % node[1]
        return '?'

    def pocket_phrase(self, P):
        items = []
        for kind, it in P.items:
            if kind == 'lig' and P.kind == 'cut' and len(it.tokens) == 1 and it.tokens[0].half and it.tokens[0].sign not in ROOT_READ:
                t0 = it.tokens[0]
                items.append('the carving whose root is "%s", cited by its root cut small' % _g(t0.sign)[1])
                continue
            items.append(self.pocket_phrase(self.R.pockets[it]) if kind == 'pocket' else lig_phrase(it)[1])
        rel = [rn for rn in self.R.runners if self.R.rnode.get(rn.rid, (None,))[0] and
               self.R.rnode[rn.rid][0][0] == 'item' and self.R.rnode[rn.rid][0][1][0] is P]
        rtxt = ''
        if rel:
            bits = []
            for rn in rel:
                s, ts = self.R.rnode[rn.rid]
                a = self.object_phrase(s)
                b = self.object_phrase(ts[0]) if ts and ts[0] else ''
                bits.append('%s %s %s' % (a, {'to': '→', 'then': ', then'}.get(rn.role, ROLE_READ[rn.role]), b))
            rtxt = ' — ' + '; '.join(bits)
        tag = 'said' if P.kind == 'said' else 'an older carving, cited'
        return '[%s: %s%s]' % (tag, '; '.join(items), rtxt)

    def runner_name(self, rid):
        """A short name for a runner in braids and breaks: 'the fire's not burning'."""
        s, ts = self.R.rnode.get(rid, (None, []))
        if not s or s[0] != 'mark':
            return rid
        mk = s[1]
        kind, doer, ph, tr = self.parts(mk)
        lab = self.label(mk.file, mk.ring, mk.pith)
        subj, obj, poss, pl = forms(lab)
        if kind == 'v':
            return ('%s %s' % (doer, gerund(ph))) if doer else '%s %s' % (poss, gerund(ph))
        if lab == ph or (self.is_intro(mk) and not self.has_label(mk.file, mk.ring)):
            return ph
        return '%s %s' % (poss, _strip_art(ph))

    # --- the plain reading --------------------------------------------------------------------
    def sentence(self, rn):
        R = self.R
        s, ts = R.rnode[rn.rid]
        src = s[1]
        kind, doer, _, trans = verbify(self.parts(src), src.lig)
        head = self.subject_clause(src, conds=False, as_act=True)
        c = self.conds_at(src)
        objs = []
        for t in ts:
            if t is None:
                continue
            if t[0] == 'mark' and t[1].ring != src.ring:
                objs.append('(in ring %d) %s' % (t[1].ring, self.object_phrase(t, s)))
            else:
                objs.append(self.object_phrase(t, s))
        tgt = ' and '.join(o for o in objs if o)
        c = [x for x in c if x not in tgt]
        role = rn.role
        if ts and ts[0] and ts[0][0] == 'bind':
            body = '%s — a strand of the bind %s' % (head, ts[0][1])
            body = body[0].upper() + body[1:]
            return body + '. [%s]' % rn.rid
        if role == 'blind':
            body = '%s, and why, the wood does not hold' % head
        elif role == 'to' and ts and ts[0] and ts[0][0] == 'none':
            body = '%s, and whither, the wood does not hold' % head
        elif role == 'to':
            body = '%s %s%s' % (head, '' if (kind == 'v' and trans) else 'to ', tgt)
        elif role == 'then':
            body = '%s; then %s' % (head, tgt)
        elif role == 'that':
            body = '%s that: %s' % (head, tgt)
        else:
            body = '%s, %s %s' % (head, {'in': 'in', 'with': 'with', 'for': 'for', 'bc': 'because of',
                                        'as': 'as', 'thru': 'through'}[role], tgt)
        if c:
            body += ', ' + ', '.join(c)
        if rn.hidden:
            body += ' (hidden)'
        if rn.seeming:
            body += ' (a seeming)'
        for (a, b, _) in R.laps:
            if a == rn.rid:
                body += '; and this broke %s' % self.runner_name(b)
            if b == rn.rid:
                body += ' (but %s broke it)' % self.runner_name(a)
        body = body[0].upper() + body[1:]
        return body + ('' if body.endswith(('?', '.')) else '.') + ' [%s]' % rn.rid

    def ring_sentences(self, k):
        R = self.R
        ms = sorted([mk for mk in R.marks if mk.ring == k], key=lambda m: m.pos())
        order = {rid: i for i, rid in enumerate(getattr(R, 'canon_runner_order', []))}
        runners = [rn for rn in R.runners if R.rnode.get(rn.rid, (None,))[0] and R.rnode[rn.rid][0][0] == 'mark'
                   and R.rnode[rn.rid][0][1].ring == k]
        runners.sort(key=lambda rn: order.get(rn.rid, 0))
        touched = set()
        for rn in runners:
            s, ts = R.rnode[rn.rid]
            touched.add(id(s[1]))
            for t in ts:
                if t and t[0] == 'mark':
                    touched.add(id(t[1]))
        out = []
        for mk in ms:
            if id(mk) not in touched:
                c = self.subject_clause(mk)
                c = c[0].upper() + c[1:]
                out.append(c + ('' if c.endswith(('?', '.')) else '.'))
        braided = {x for (_, st, _, _) in R.braids for x in st}
        for rn in runners:
            if rn.rid in braided:
                continue
            out.append(self.sentence(rn))
        for (bid, st, pat, _) in R.braids:
            if not any(x in [rn.rid for rn in runners] for x in st):
                continue
            names = [self.runner_name(x) for x in st]
            seq = [names['abc'.index(c)] for c in pat.rstrip('!') if 'abc'.index(c) < len(names)]
            if len(st) == 2:
                txt = 'By turns, each to the other: %s and %s (%s: over at each turn, %s)' % (names[0], names[1], bid, ', '.join(seq))
            else:
                txt = 'These three, each holding the others: %s (%s: %s)' % (', '.join(names), bid, ', '.join(seq))
            if pat.endswith('!'):
                txt += '; until at the last %s prevailed' % seq[-1]
            out.append(txt[0].upper() + txt[1:] + '. [%s]' % ','.join(st))
        for (kid, st, o, _) in R.binds:
            rs = [R.rnode.get(x, (None, []))[0] for x in st]
            if not any(r and r[0] == 'mark' and r[1].ring == k for r in rs):
                continue
            txt = 'Bound, each only with the other: %s' % ' and '.join(self.runner_name(x) for x in st)
            if o:
                node = _resolve(R, o[1], Findings(), '', kid)
                txt += '; and, bound, %s %s' % ('then' if o[0] == '⇒' else 'to', self.object_phrase(node))
            out.append(txt + '. [%s]' % kid)
        for (b_k, y, b, s0, s1, _) in R.conds:
            if b_k == k:
                files = [(s0 + i) % 16 for i in range((s1 - s0) % 16 + 1)]
                if not any(mk.ring == k and mk.year == y and mk.file in files for mk in R.marks):
                    out.append('%s lies over files %d–%d.' % (BAND_THING[b][0].upper() + BAND_THING[b][1:], s0, s1))
        for (f, a, b, _) in R.rays:
            if a[0] == k:
                out.append('(A ray on file %d: what is cut there in ring %d is the same one as in ring %d.)' % (f, a[0], b[0]))
        for (f, a, _) in R.mems:
            if a[0] == k:
                out.append('(A memory ray from file %d: remembered, carried back to the heart%s.)' % (f, '; always' if k > 1 else ''))
        return out

    def plain(self):
        R = self.R
        out = ['%s · %s · %s wood · %d ring%s%s' % (R.id, R.kind, R.wood, R.K or 0, '' if R.K == 1 else 's',
                                                   (' · %d piths' % R.npith) if R.npith > 1 else '')]
        seal = [lig for (f, lig, _) in R.bark if lig.tokens and lig.tokens[0].sign == 'HOLD' and len(lig.tokens) == 1]
        names = [lig for (f, lig, _) in R.bark if not (lig.tokens and lig.tokens[0].sign == 'HOLD' and len(lig.tokens) == 1)]
        if seal:
            out.append('  This is held in the grain.')
        for k in range(1, (R.K or 0) + 1):
            ms = [mk for mk in R.marks if mk.ring == k]
            Ps = [P for P in R.pockets.values() if P.ring == k and not P.parent]
            cs = [c for c in R.conds if c[0] == k]
            if not ms and not Ps and not cs:
                out.append('  Ring %d: a morrow passes.' % k)
                continue
            yrs = sorted(set([m.year for m in ms] + [P.year for P in Ps]))
            out.append('  Ring %d (band %s%s):' % (k, band_of(R, k), (', %d years' % len(yrs)) if len(yrs) > 1 else ''))
            out += ['    ' + s for s in self.ring_sentences(k)]
        if names:
            out.append('  In the bark: %s.' % '; '.join(lig_phrase(n)[1] for n in names))
        if R.pale:
            out.append('  In the bark, %d pale ring%s: its groans.' % (R.pale, '' if R.pale == 1 else 's'))
        if seal:
            out.append('  …and the grain holds it still.')
        return '\n'.join(out)

    # --- the literal reading (section 13.5) ----------------------------------------------------
    def literal(self):
        R = self.R
        out = ['%s — literal reading (§13.5)' % R.id]
        for k in range(1, (R.K or 0) + 1):
            ms = sorted([mk for mk in R.marks if mk.ring == k], key=lambda m: (m.pith if m.pith is not None else -1, m.file, m.year, m.cell))
            Ps = [P for P in R.pockets.values() if P.ring == k and not P.parent]
            if not ms and not Ps:
                out.append('r%d: (empty: a morrow passes)' % k)
                continue
            out.append('r%d:' % k)
            byf = {}
            for mk in ms:
                byf.setdefault((mk.pith, mk.file), []).append(mk)
            for (p, f), lst in sorted(byf.items(), key=lambda x: ((x[0][0] if x[0][0] is not None else -1), x[0][1])):
                multi = len(set(m.year for m in lst)) > 1
                bits = [('y%d ' % mk.year if multi else '') + self.raw(mk)[1] for mk in lst]
                out.append('  %s%d [%s]: %s' % (('p%d·' % p) if p is not None else '', f, self.label(f, k, p), '; '.join(bits)))
            for P in Ps:
                out.append('  pocket %s (%s, files %d–%d, r%d/%d): %s' % (P.pid, P.kind, P.s0, P.s1, P.ring, P.year, self.pocket_phrase(P)))
            for rn in R.runners:
                s, ts = R.rnode.get(rn.rid, (None, []))
                if s and s[0] == 'mark' and s[1].ring == k:
                    tg = ', '.join(self.object_phrase(t, s) for t in ts if t)
                    role = 'why, the wood does not hold' if rn.role == 'blind' else ROLE_READ[rn.role]
                    out.append('  %s: [%s] —%s→ [%s]' % (rn.rid, self.raw(s[1])[1], role, tg))
        for (a, b, _) in R.laps:
            out.append('lap %s ⊳ %s: and %s broke %s' % (a, b, self.runner_name(a), self.runner_name(b)))
        for (bid, st, pat, _) in R.braids:
            out.append('braid %s (%s): %s' % (bid, pat, 'by turns' if len(st) == 2 else 'each holding the others') +
                       (', until at the last %s' % st['abc'.index(pat.rstrip('!')[-1])] if pat.endswith('!') else ''))
        for (kid, st, o, _) in R.binds:
            out.append('bind %s: %s bound, each only with the other%s' % (kid, ' + '.join(st), ('; out: %s %s' % o) if o else ''))
        for (f, lig, _) in R.bark:
            out.append('bark %d: %s' % (f, 'the seal: this is held in the grain' if (lig.tokens[0].sign == 'HOLD' and len(lig.tokens) == 1) else lig_phrase(lig)[1]))
        return '\n'.join(out)


# ------------------------------------------------------------------------------------------------
# 10 · Fragments (for coverage tables): check every sign-like token in a grain expression
# ------------------------------------------------------------------------------------------------

FRAG_TOKEN = re.compile(r"(?<![A-Za-z])((?:[!~_>]*)(?:\([^()]*=[^()]*\)|[A-Z][A-Z0-9]+)(?::[a-z]+)?"
                        r"(?:×3|‿|½|\?|\*|/|\\|#\d+|@\d+|\^r\d+(?:/\d+)?|\{[a-z, ]*\}|<[^<>]*>|\[[A-Z]+\])*"
                        r"(?:\+(?:[!~_>]*)(?:[A-Z][A-Z0-9]+|grain-arc)(?::[a-z]+)?"
                        r"(?:×3|‿|½|\?|\*|/|\\|#\d+|@\d+|\^r\d+(?:/\d+)?|\{[a-z, ]*\}|<[^<>]*>|\[[A-Z]+\])*)*)")
DEVICE_WORDS = {'braid', 'bind', 'lap', 'pocket', 'said', 'cut', 'mem', 'ray', 'fork', 'chain', 'span', 'twin', 'pair',
                'lean', 'seal', 'grain-arc', 'file', 'ring', 'year', 'cell', 'empty', 'band', 'blind', 'aim', 'root',
                'name', 'hollow', 'smoothed', 'plural', 'kind-arc', 'part', 'fringe', 'count', 'ordinal', 'split'}


def check_fragment(expr, F, where='expr'):
    """Validate every sign-like token of a grain expression; return (signs used, devices)."""
    used, devs = set(), set()
    s = expr
    for m in re.finditer(r'\[([A-Z]+)\]', s):
        if m.group(1) not in BANDS:
            F.err('M07', where, 'unknown band [%s]' % m.group(1))
    for m in re.finditer(r'\b(MIST|WHITE|DREAD|WATER|STILL|DARK)\b', s):
        devs.add('band')
    scrub = re.sub(r'(?:(?<=^)|(?<=[\s;,(]))\[(MIST|WHITE|DREAD|WATER|STILL|DARK)\]', ' ', s)   # a band alone
    scrub = re.sub(r'\b(MIST|WHITE|DREAD|WATER|STILL|DARK)\b(?!\])', ' ', scrub)
    for m in FRAG_TOKEN.finditer(scrub):
        tok = m.group(1)
        if re.fullmatch(r'[A-Z]', tok):
            continue
        if tok in ('GN', 'IV', 'II', 'III', 'VI', 'RING', 'OK'):
            continue
        ctx = {'name_ok': True}
        lig = parse_ligature(tok, F, where, ctx, item=True)
        if lig:
            used.update(lig.signs())
            devs.update(ctx.get('devices', set()))
    for a in re.findall(r'→in|→with|→for|→bc|→as|→thru|→that|→|⇒', s):
        devs.add('runner ' + ARROWS.get(a, a))
    if '∅' in s:
        devs.add('blind')
    if re.search(r'@\d+|@f', s):
        devs.add('file referent')
    return used, devs


# ------------------------------------------------------------------------------------------------
# 11 · Driver
# ------------------------------------------------------------------------------------------------

def validate_text(text, name='<text>', kind=None):
    F = Findings()
    if kind:
        text = re.sub(r'^(round\s+\S+(?:\s*\([^)]*\))?\s*\{)', r'\1kind: %s; ' % kind, text, flags=re.M)
    rounds = parse_text(text, F, name)
    return rounds, F


def print_findings(F, stream=sys.stdout, quiet_notes=False):
    for it in F.items:
        if quiet_notes and it['level'] == 'NOTE':
            continue
        ref = ('  [%s]' % it['ref']) if it['ref'] else ''
        stream.write('%-5s %s %s: %s%s\n' % (it['level'], it['code'], it['where'], it['msg'], ref))


def md_blocks(path):
    t = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'```[a-z0-9]*\s*\n(.*?)\n```', t, re.S):
        body = m.group(1)
        if re.match(r'\s*round\s+[\w.·-]+\s*(\([^)]*\)\s*)?\{', body):
            ln = t[:m.start()].count('\n') + 2
            out.append((ln, body))
    return out


SELFTEST = r'''
round T-ok {wood: long; pith: war; rings: 3; rules after: [1, 2]; cells: [1, 2, 2]}
  I
    r1/1  0: KNOT*
  ‖
  II
    r2/1  4.1: GO    4.2: SWIFT+FOLLOW{again}    12: HULL×3
  ‖
  III
    r3/1  8: STONEFOLK×3+HOLD      band MIST files 7–9
  runners
    run a  4.1.r2/1    →      @0
    run b  12.r2/1     ⇒      8.r3/1
'''
SELFTEST_BAD = r'''
round T-bad {wood: forty; pith: war; rings: 2; rules after: [1]; cells: [1, 1]}
  I
    r1/1  0: WAVE*    5: HULL{all}
  ‖
  II
    r2/1  4: EDGE+BREAKER+GUN    6: TAKE:palm    7: NOPE    9: GO{all,few}
  runners
    run t1  0.r1/1   →in    4.r2/1
    run t2  4.r2/1   →      0.r1/1
'''


def selftest():
    ok = True
    rs, F = validate_text(SELFTEST, 'selftest-ok')
    errs = [i for i in F.items if i['level'] == 'ERROR']
    if errs:
        ok = False
        print('selftest: the good round has errors:')
        print_findings(F)
    rs, F = validate_text(SELFTEST_BAD, 'selftest-bad')
    codes = set(i['code'] for i in F.items if i['level'] == 'ERROR')
    want = {'M08', 'M02', 'M01', 'M04', 'M25', 'A02', 'R20', 'A10', 'A13'}
    miss = want - codes
    if miss:
        ok = False
        print('selftest: the bad round should raise %s; it raised %s' % (sorted(miss), sorted(codes)))
    F2 = Findings()
    check_fragment('TRUE+HOLD →that pocket said{ CARVE{all}+MOUTH } ; SAPLING+TRUE+HOLD ; EARTH[MIST]', F2)
    if not any(i['code'] == 'M08' for i in F2.items):
        ok = False
        print('selftest: the fragment checker missed a three-sign ligature')
    print('selftest: %s (%d signs loaded from %s)' % ('ok' if ok else 'FAILED', len(SIGNS), '; '.join(SIGN_SOURCES)))
    return ok


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description='Grain Notation v2 validator and reader.')
    ap.add_argument('files', nargs='*')
    ap.add_argument('--literal', action='store_true')
    ap.add_argument('--canon', action='store_true')
    ap.add_argument('--check-only', action='store_true')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--kind', choices=('order', 'telling', 'chip'))
    ap.add_argument('--expr', action='append')
    ap.add_argument('--md', action='append')
    ap.add_argument('--rules', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--no-notes', action='store_true')
    a = ap.parse_args(argv)
    if a.rules:
        for code, name, text in RULES_DOC:
            print('%s  %-16s %s' % (code, name, text))
        print('\nSigns: %d, from %s' % (len(SIGNS), '; '.join(SIGN_SOURCES)))
        return 0
    if a.selftest:
        return 0 if selftest() else 1
    bad = 0
    for e in a.expr or []:
        F = Findings()
        used, devs = check_fragment(e, F)
        print('expr: %s' % e)
        print_findings(F)
        print('  signs: %s' % ', '.join(sorted(used)))
        print('  devices: %s' % ', '.join(sorted(devs)))
        bad |= F.count('ERROR') > 0
    for md in a.md or []:
        for ln, body in md_blocks(md):
            rs, F = validate_text(body, '%s@%d' % (os.path.basename(md), ln), a.kind)
            for R in rs:
                print('== %s (%s, line %d): %d errors, %d warnings' % (R.id, os.path.basename(md), ln, F.count_round('ERROR', R.id), F.count_round('WARN', R.id)))
            print_findings(F, quiet_notes=a.no_notes)
            bad |= F.count('ERROR') > 0
    if not a.files and not a.expr and not a.md:
        ap.print_help()
        return 2
    for path in a.files:
        text = open(path, encoding='utf-8').read()
        rs, F = validate_text(text, os.path.basename(path), a.kind)
        bad |= F.count('ERROR') > 0
        if a.json:
            print(json.dumps({'file': path, 'rounds': [R.id for R in rs], 'findings': F.items}, ensure_ascii=False, indent=1))
            continue
        for R in rs:
            print('== %s: %s, %s wood, %d rings; %d errors, %d warnings' % (R.id, R.kind, R.wood, R.K or 0,
                                                                         F.count_round('ERROR', R.id), F.count_round('WARN', R.id)))
        print_findings(F, quiet_notes=a.no_notes)
        if a.check_only:
            continue
        for R in rs:
            print()
            if a.canon:
                print(canon_gn(R))
            elif a.literal:
                print(Reader(R).literal())
            else:
                print(Reader(R).plain())
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
