#!/usr/bin/env python3
"""wf12 merge: the Book's standing terms against the Orrowen of every paragraph that uses them (a term in the English
whose expected Orrowen is not in the paragraph's blockquote is listed, for reading)."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pairs as P
T = [
 ('Long Hearth', r'Odh Sell|Odh Hell'), ('inner gate', r'[gy]anna ulvenn|Yanna Ulvenn'), ('torn cloak', r'[chg]ovv treskat|Covv Treskat'),
 ('grey sails', r'wemmeth myst'), ('young wood', r'mesk tevel'), ('black pillars', r'[gy]annath domm'),
 ('mute stones', r'[td]h?olmath nawrodh'), ('archive chest', r'vestul rytow'), ('True Men?', r'vennuld'),
 ('Stonewrights?', r'[Ss]tonwryt'), ('wreck-wood', r'kaelirvesk'), ('Mystarchs?', r'Crenn(eth)? Myst'),
 ('Thrones?', r'[Rr]eskow(ath)? [Ss]trom'), ('harbour-house', r'[dt]h?avowlest'), ('east cairns', r'stelleth rerddhalden'),
 ('the Fall', r'Ommol'), ('the Twelve', r'Delv'), ('wall-walk', r'haldorrol'), ('the Rite', r'[Tt]ernil'),
 ('the Captain', r'[CcHh]renn'), ('half-cloak|half of the cloak|half of a cloak', r'saed'), ('the Bonded', r'Lodhan'),
 ('Shorelanders|Shorelands', r'Orrow'), ('the Guest', r'arra|Arra'), ('Tide of Remembering', r'Hyll Dhumol'),
 ('Hasty Tide', r'Hyll Pynt'), ('Second Tide', r'Hyll Pawast'), ('Joined Tide', r'Hyll Lodhat'), ('Last Tide', r'Hyll Dasken'),
 ('Tide that Learned Deceit', r'Hyll sa re rystull nycul'), ('the grey\b', r'myst'), ('the warden', r'▒▒▒▒|pard'),
]
res = P.all_items()
out = []
for term, rx in T:
    bad = []
    tot = 0
    for u, its in res.items():
        for it in its:
            if it['kind'] != 'bq' or not it['eng']:
                continue
            if re.search(r'\b(' + term + r')\b', it['eng']):
                tot += 1
                if not re.search(rx, re.sub(r'[*{}]', '', it['orr'])):
                    bad.append((u, it['line'], it['orr'][:150].replace('\n', ' '), it['eng'][:110].replace('\n', ' ')))
    print('%-34s %3d paragraphs, %d without %s' % (term, tot, len(bad), rx))
    for b in bad:
        print('      [%s L%d] %s\n            EN: %s' % b)
