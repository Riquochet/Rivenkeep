#!/usr/bin/env python3
"""wf12 merge fix F7: the Book's recurring English rendered once (found by recur.py, the units' own cross-unit tables
and the formula checks).  Each change: (unit, old Orrowen, new Orrowen, the English it stands over, why).  The romanised
line is changed; a *Merge (wf12)* note is set after the Book's English for it; a word-for-word line or unit note that
quotes the old form is mended where given.  Logged to fixes.log and harmonisations.json."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
U = os.path.join(os.path.dirname(HERE), 'units')
LOG = open(os.path.join(HERE, 'fixes.log'), 'a')

# (id, unit, old, new, why, extra [(old, new)] edits of notes in the same unit)
H = [
    ('H1', 'S02', 'Lo hedh orl et movenn, re resk et Stonwrytan', 'Ul hedh orl et movenn, re resk et Stonwrytan',
     '"At dusk on the day of the banner" is *Ul hedh orl et movenn*, as II.1 (S04) says it; *lo hedh* is also read *lo* + S·*cedh*, "at who" (S08\'s collision table), so the Book\'s *at dusk* is *ul hedh* everywhere',
     [('- ***Lo hedh orl et movenn***: a double construct, "at the dusk of the day of the banner" (*lo* softens *hedh*, which does not change).',
       '- ***Ul hedh orl et movenn***: a double construct, "in the dusk of the day of the banner" (*ul* leaves *h* unchanged). *Merge (wf12):* the unit had *Lo hedh*.')]),
    ('H2', 'S01', 'Re hadhom en narl sost um et meskdhrenn hos fedh', 'Re hadhom en narlremull sost um et meskdhrenn hos fedh',
     '"laid mine own palm on the grain" is *en narlremull sost*, "my own palm" (*garlremull*, O0691), as V.1 says it (S07); the unit had *en narl sost*, "my own hand"', []),
    ('H3', 'S10', 'eth re hadha {{Halyna}} en narlath um et tolm.', 'eth re hadha {{Halyna}} en narlath pana um et tolm.',
     '"Halyna laid my two hands on the stone" is I.2\'s line, *en narlath pana*, "my hands, both" (S02), which this line says again', []),
    ('H4', 'S04', 'Um et hald ul gethyl re veskys olna', 'Um et hald ul et kethyl re veskys olna',
     '"on the wall in the holding" is *um et hald ul et kethyl*, the holding as the hour of the siege day (O1124), as I.2 says it (S02)', []),
    ('H5', 'S10', 'Seskym *et bystir sa nath morr ul neld*.', 'Seskym *et bystir sa hess*.',
     '"the stair that goes no more" is the cradle-rhyme\'s own words, *et bystir sa hess* (I.4, S03), as both units asked (the Epilogue quotes the rhyme)',
     [('| *the stair that goes no more* | *et bystir sa nath morr ul neld* | I.4 (the cradle-rhyme) | this unit; the rhyme\'s own line should set it, and this one follow |',
       '| *the stair that goes no more* | *et bystir sa hess* | I.4 (the cradle-rhyme) | the rhyme\'s own line (S03); *merge (wf12)*: the unit\'s *et bystir sa nath morr ul neld* withdrawn, as it asked |')]),
    ('H6', 'S03', 'Doss hulter rytet dem o yaldat, eth nath lusk o yaldat,', 'Doss hulter stinet dem o yaldat, eth nath morr o hyo,',
     'the law of the staff is one saying in I.4 and III.2: *Doss hulter stinet dem o yaldat, eth nath morr o hyo* (O3057, S05): *stin* is the cut of wood (a staff is cut, not lettered), and *orr hy*, "go out of", is "leave"', []),
    ('H7', 'S09', '*Eth lo et vorr ull re dhovv et odh hos hoss um Ebba.*', '*Eth lo et vorr ull re dhovv et odh hoss Ebba.*',
     '"the hearth waited a breath for Ebba" is I.5\'s words, *re dhovv et odh hoss Ebba*, "the hearth waited Ebba\'s breath" (S03), as S03 asked VI.1 to take them, with its own *too*', []),
    ('H8', 'S10', 'ul vodh es vesk nahos pawast so dem mommol et hald', 'ul vodh es vesk nahos pawast so, somm ston et hald',
     '"where no eye will see them again till the wall fall" is II.1\'s and II.3\'s words, *somm ston et hald*, "while the wall stands" (S04, twice), the vow\'s own verb',
     [('| *where no eye will see it again till the wall fall* | *ul vodh es vesk nahos pawast so, dem mommol et hald* | I.4, II.3 |',
       '| *where no eye will see it again till the wall fall* | *ul vodh es vesk nahos pawast so, somm ston et hald* (II.1, II.3: S04; *merge (wf12)*: the unit\'s *dem mommol et hald* withdrawn) | I.4, II.3 |')]),
    ('H9', 'S04', 'ul et taldow withlern, ledh Halvard o um et hald wridlern,', 'ul et taldow bithlernen, ledh Halvard o um et hald bridlernen,',
     '"the north wall" is *et hald bridlernen*, the adjective (O0156), as III.2, V.5 and VI.1 say it (S05, S08, S09); "the south tower", *et taldow bithlernen* (O2972) likewise', []),
    ('H10', 'S09', 'Re vysker gor fedh: hinnar, el hosel trenn dasken um et trenn hemm o.', 'Re vysker gor fedh: hinnar, nayalat veth trenn dasken um et trenn hemm.',
     '"A town is but the last course on the old, we used to say" is III.2\'s saying, *hinnar, nayalat veth trenn dasken um et trenn hemm* (S05)', []),
    ('H11', 'S10', 'Ul et heth dhomast, um ryst helvnynth bynt, hy et myst re rarr sulter lyss myst.', 'Ul et heth dhomast, um ryst helvnynth bynt, re vellor sulter lyss myst hy et myst.',
     '"out of the grey came a small grey boat" is IV.3\'s words, *re vellor sulter lyss myst hy et myst* (S06), which the Epilogue says again', []),
    ('H12', 'S10', 'eth ul lern et kess, eth ul myst.', 'eth ul lern et kess, eth ul et myst.',
     '"Into the wind it went, and against the current, and into the grey" is IV.3\'s words (S06), *eth ul et myst*, the grey with its article as everywhere',
     [('| *Into the wind it went, and against the current, and into the grey* | *Re orr o ul lern et helvhoss, eth ul lern et kess, eth ul myst* | IV.3 (*…, burning*), IV.6 | wf8 S10 |',
       '| *Into the wind it went, and against the current, and into the grey* | *Re orr o ul lern et helvhoss, eth ul lern et kess, eth ul et myst* | IV.3 (*…, burning*), IV.6 | wf8 S10; *merge (wf12)*: *ul et myst*, as IV.3 (S06) |')]),
    ('H13', 'S11', 'sa re haemerent dem varn um stomornel', 'sa re vymment dem varn um vivenn',
     '"the shore laughed at three axemen, home on a spar" is IV.3\'s words (S06), *sa re vymment dem varn um vivenn*, "who came home on a mast", as IV.5 (S07) says Daveth came home; the unit\'s play on *haemer* (the stones hung, the men floated) is given up for the one rendering',
     [('- **One verb, two hangings.** *haemer* is "hang; float": the stones *re haemerent*, "hung", over the fire, and the axemen *sa re haemerent dem varn um stomornel*, "who floated home on a spar".',
       '- *Merge (wf12):* "home on a spar" is now IV.3\'s *sa re vymment dem varn um vivenn* (S06; IV.5 has Daveth *re vymm … dem varn um vivenn*). The unit\'s play, given up for the one rendering: **one verb, two hangings.** *haemer* is "hang; float": the stones *re haemerent*, "hung", over the fire, and the axemen *sa re haemerent dem varn um stomornel*, "who floated home on a spar".')]),
    ('H14', 'S11', 'eth re vorr et greller ryssyth nind dem vimm somm re veskym', 'eth re vorr et greller dem vimm ryssyth nind somm re veskym',
     '"the lamp burned down a finger\'s width" is V.1\'s words and order, *re vorr et greller dem vimm ryssyth nind* (S07)', []),
    ('H15', 'S10', 'Ul vess ull re dhresk et Crenn ryssyth yarl hy saed et covv, eth re yal et saedel bysket um hagess ul susk et ganna.',
     'Vess ull re dhresk et Crenn ryssyth yarl hy saed et covv sa hovv o, eth re wysk o o um hagess, ul susk et ganna.',
     '"That night the Captain cut a hand\'s breadth from his half of the cloak, and bound it on a pike over …" is V.5\'s sentence (S08), *Vess ull re dhresk et Crenn ryssyth yarl hy saed et covv sa hovv o*, with the Book\'s one verb for binding a strip, *bysk* (H31)', []),
    ('H16', 'S09', 'Nath re veskym o. Re vesk Hale o.', 'Nath re veskym o. Re vesk Hale.',
     '"I did not see it. Hale did." is V.5\'s words (S08), *Nath re veskym o. Re vesk Hale.*', []),
    ('H17', 'S11', 'ul vodh re senn et Vorrol', 'ul vodh re senn Vorrol',
     '"where the Burning went out": a Throne\'s name takes no article (§3.2), as VI.1 says it (S09, *ul vodh re senn Vorrol*) and as every other Throne\'s name stands', []),
    ('H18', 'S10', 'Ul surr et Mymmyleth,', 'Ul surr et mymmyleth,',
     '"the year of the homecomings" is a common noun, as VI.1\'s dateline and the Book of Knowings write it (S09, S11); *Mymmyleth* is VI.1\'s title', []),
    ('H19', 'S07', '> Rellorath ul et mesk.', '> Rellorath um et mesk.',
     '"Marks on the wood." is I.3\'s words (S02; O3036), *Rellorath um et mesk*, Hale\'s message, which V.1 quotes',
     [('Word for word: *Signs in the wood.*\n\n- Verbless, as Hale says it. *ul*, "in", for the marks are cut into the wood; *um* would sit next to the feeling idiom (*doss* X *um* Y).',
       'Word for word: *Signs upon the wood.*\n\n- Verbless, as Hale says it. *Merge (wf12):* I.3\'s words, *um*, "upon" (O3036; S02), where the unit had *ul*, "in" (it argued *um* would sit next to the feeling idiom, *doss* X *um* Y, which a verbless line has not).'),
      ('a saying that is its own paragraph stands bare (*Rellorath ul et mesk.*)', 'a saying that is its own paragraph stands bare (*Rellorath um et mesk.*)')]),
    ('H20', 'S10', '> *Eth re lusk et Crenn et biskhovv.*', '> *Eth re hadh et Crenn et biskhovv dem sestow.*',
     '"And the Captain put his hood back." is IV.3\'s close (S06), *Eth re hadh et Crenn et biskhovv dem sestow*, "laid the hood to the back", read back exactly (S06\'s blind reader), against the foreword\'s and I.1\'s *o wiskhovv dem susk*, "his hood up"; this unit\'s *lusk*, "loose", the Captain\'s third call, is given up for the one rendering (the unit asked that the two closes match)',
     [('Word for word: *And the Captain loosed the hood.*\n\n- **"Put his hood back" is *lusk*, "loose"**',
       'Word for word: *And the Captain laid the hood to the back.*\n\n- *Merge (wf12):* IV.3\'s close, word for word (S06), as this unit asked. The unit\'s reasoning for its own *lusk*, kept as a record: **"Put his hood back" is *lusk*, "loose"**'),
      ('| *And the Captain put his hood back.* | *Eth re lusk et Crenn et biskhovv.* | IV.3 | this unit |',
       '| *And the Captain put his hood back.* | *Eth re hadh et Crenn et biskhovv dem sestow.* | IV.3 | IV.3\'s (S06); *merge (wf12)*: the unit\'s *Eth re lusk et Crenn et biskhovv* withdrawn |'),
      ('- **"Put his hood back"** is *lusk*, the Captain\'s own third call ("Hold, or loose"). If IV.3 chooses otherwise, the two closes should match.',
       '- **"Put his hood back"**: *merge (wf12)*: IV.3\'s *Eth re hadh et Crenn et biskhovv dem sestow*; the unit\'s *lusk*, the Captain\'s own third call ("Hold, or loose"), was given up so that the two closes match, as it asked.')]),
    ('H21', 'S10', 'Dhenth et Covv Treskat tul ul susk et hos ledal. Nath re dhunn et wadh tul.', 'Dhenth et Covv Treskat tul ul susk et hos ledal. Nath dunn et wadh tul.',
     '"The sea hath not finished." is Corlen\'s saying as III.1 and V.5 say it (S05, S08; O3053), in the present; the past *nath re dhunn* is III.2\'s "had not finished"',
     [('| *The sea hath not finished.* | *Nath re dhunn et wadh tul.* | III.1, V.5 (Corlen) | this unit |',
       '| *The sea hath not finished.* | *Nath dunn et wadh tul.* | III.1, V.5 (Corlen) | O3053 (S05, S08); *merge (wf12)*: the unit\'s past *Nath re dhunn* withdrawn |')]),
    ('H22', 'S09', 'eth re vysk ey: Doss maver kethyl waegyth um hos.*', 'eth re vysk ey: Doss maver vothol reller um hos.*',
     '"Someone must keep a light." is Hesk\'s saying as III.2 gives it (S05; O3055), *Doss maver vothol reller um hos*, "need of tending a lamp is upon someone", which the fisher-girl says again', []),
    ('H23', 'S10', 'Re yalant et higileth hemm lo wisk et dhysal, eth nath re orrant ul neld.', 'Re yalant et higileth hemm lo wisk et dhysal, eth nath re rarrant mest virr.',
     '"and came no further" is IV.3\'s words for the warden at his door (S06: *nath re rarr o mest virr*, "came no nearer"), which the old ship-masters\' posture echoes (S06\'s table asked for it)', []),
    ('H24', 'S09', 're orr Lymmerd Yendeth dem vimm', 're orr Lymmerd Yendeth Clenn dem vimm',
     '"the Bearer of New Branches" is v3\'s epithet, *Lymmerd Yendeth Clenn* (O3086, S11); *Lymmerd Yendeth* (O2943) is v1.3\'s "the Bearer of Branches"', []),
    ('H25', 'S01', 'doss o ul vimm stelleth rerddhald tevar', 'doss o ul vimm et stelleth rerddhalden tevar',
     '"under the east cairns" is *ul vimm et stelleth rerddhalden*, as V.5 and VI.3 say it (S08, S10)', []),
    ('H26', 'S02', 'um hosk hald et rerddhald,', 'um hosk et hald rerddhalden,',
     '"the parapet of the east wall": *et hald rerddhalden*, "the east wall", as IV.5 and V.5 say it (S07, S08), with the parapet as its capstone (*hosk*)', []),
    ('H27', 'S03', 'Virr gor vess re hadh ey o dholm hosast, hoss ul lern et ullen.', 'Virr gor vess re hadh ey o dholm hosast, hos hoss ul lern et ullen.',
     '"a breath before the rest" is the foreword\'s words (S01), *hos hoss ul lern et ullen*, "one breath before the others"', []),
    ('H28', 'S04', 're yald Tarnel piskur, bysket um wysket,', 're wysk Tarnel piskur, bysket um wysket,',
     '"he knotted a net as he went" is I.2\'s verb (S02), *re wysk … piskur*, "knotted (S·*bysk*) a net", with this leaf\'s own *bysket um wysket*', []),
    ('H29', 'S09', 'hosen re vesk Seren o lo rask et baegyth', 'hosen re vesk Seren o lo et baegyth dasken',
     '"the last of the light" is I.2\'s *et baegyth dasken* (S02)', []),
    ('H30', 'S03', 'eth saed covv um o sestow.', 'eth saed hovv um o sestow.',
     '"his half of a cloak on his back" is I.2\'s words (S02), *saed hovv um o sestow*: the possessor of a construct is softened (§3.2: *covv* > *hovv*)', []),
    ('H31a', 'S08', 'eth re lodh o o um hagess, um stell Yory.', 'eth re wysk o o um hagess, um stell Yory.',
     '"bound (a strip) on a pike" is one verb in the Book, *bysk*, "tie fast; bind" (I.1\'s *bysket um hagess*, I.5, the Epilogue); the unit\'s *lodh*, the bond-word, is given up for the one rendering', []),
    ('H31b', 'S09', 'Hy ull re esk et Crenn saedel hy o hovv um hagess umonta', 'Hy ull re wysk et Crenn saedel hy o hovv um hagess umonta',
     '"the Captain bound a strip on a pike over them": the Book\'s one verb for binding a strip, *bysk* (H31a); *esk* is "cover; close; wrap"', []),
    ('H31c', 'S09', 'eth re esk et Crenn saedel umo.', 'eth re wysk et Crenn saedel umo.',
     'as H31b', []),
    ('H32', 'S03', 'Re wysk et Crenn ryssyth yarl hy o hovv um hagess umoy.', 'Re wysk et Crenn saedel hy o hovv um hagess umoy.',
     '"a strip (of his half-cloak)" is *saedel*, "a small part" of the half, as V.5, V.7 and the Epilogue say it (S08, S09, S10); *ryssyth yarl* stays for the Book\'s *a hand\'s breadth*', []),
    ('H35', 'S09', 'Hy ull re hadh nemm hy et sugornan hos lo ull,', 'Hy ull re hadh nemm sugornan hos lo ull,',
     '"a fisher-girl" is the construct *nemm sugornan*, as VI.3 says it (S10, with *tevath sugornan*, "fisher-children")', []),
]


H2ND = [
    ('H36', 'S10', 'ul molt et tolmath velv, lo sest hebbet et Arra', 'ul molt et tolmath nawrodh, lo sest hebbet et Arra',
     '"the mute stones" is *tolmath nawrodh*, as the foreword, IV.1 and V.1 say it (S01, S06, S07)', []),
]


def main():
    import sys
    todo = H2ND if '--second' in sys.argv else H
    prev = json.load(open(os.path.join(HERE, 'harmonisations.json'))) if '--second' in sys.argv else []
    out = list(prev)
    for hid, u, old, new, why, extra in todo:
        p = os.path.join(U, u + '.md')
        L = open(p, encoding='utf-8').read().split('\n')
        hits = [i for i, l in enumerate(L) if l.startswith('>') and old in l]
        assert len(hits) == 1, (hid, u, old, hits)
        i = hits[0]
        L[i] = L[i].replace(old, new)
        # the English after the blockquote (the first non-blank, non-label line after the bq group)
        j = i
        while j < len(L) and L[j].startswith('>'):
            j += 1
        while j < len(L) and (not L[j].strip() or re.match(r'^\*\((first|second)', L[j])):
            j += 1
        k = j
        while k < len(L) and L[k].strip():
            k += 1
        eng = ' '.join(L[j:k])
        note = '- *Merge (wf12), %s:* %s. (The unit had *%s*.)' % (hid, why, old.lstrip('> ').strip())
        L.insert(k, '')
        L.insert(k + 1, note)
        t = '\n'.join(L)
        t = re.sub(r'\n\n\n(- \*Merge \(wf12\), %s)' % hid, r'\n\n\1', t)
        for a, b in extra:
            assert t.count(a) == 1, (hid, a[:60], t.count(a))
            t = t.replace(a, b)
        open(p, 'w', encoding='utf-8').write(t)
        LOG.write('F7 %s %s: %r -> %r\n' % (hid, u, old, new))
        out.append(dict(id=hid, unit=u, old=old, new=new, english=eng[:300], why=why))
    json.dump(out, open(os.path.join(HERE, 'harmonisations.json'), 'w'), indent=1, ensure_ascii=False)
    print(len(out), 'harmonisations applied')


if __name__ == '__main__':
    main()
