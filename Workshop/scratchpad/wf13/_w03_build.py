import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
G = {
"Hebbet sa re yal kethet hos clem":
 "gift|that|(past)|was|held|one|hour",
"Et heth sullast, ul Hyll Dhumol.":
 "the|spring|third|in|Tide|Remembering",
"Ul vess veskyl wrodath Wrenn re vess tev vodh re hebb et arra. Heth sy re heth Rhyna o hos clem, eth re rarr o uloy niss, hosen nynth um dholm; nath re femm Halvard o, um et parow lo et lodh, eth ew o sa re hadh et tolm hosast ul et brodhol.":
 "in|night|reading|words|Brenn|(past)|asked|child|what|(past)|gave|the|Guest|"
 "spring|this|(past)|held|Rhyna|it|one|hour|and|(past)|came|it|into-her|slow|as|water|over|stone|"
 "not|(past)|touched|Halvard|it|across|the|ward|at|the|mortar|and|was|he|who|(past)|laid|the|stone|first|in|the|telling",
"— Hemm. Domm, eth hemm. Tolm — nel. Nel tolm. Ew mesk.":
 "old|dark|and|old|stone|is not|is not|stone|was|tree",
"— Garlath, dhaedh, fedh sell. Flenneth. Nel — brodath, hosen flenneth. Hos, eth hos, eth hos.":
 "hands|warm|time|long|leaves|is not|words|like|leaves|one|and|one|and|one",
"— Sull. Sull brod ulo —":
 "three|three|words|in-him",
"— eth nayalat ul so lodh. Doss o lona.":
 "and|nothing|in|their|mortar|is|it|at-us-two",
"— Gebb. Ol — lonn et mesk, ul et gannath. Dannat. Nath dessent.":
 "door|our|kin|the|wood|in|the|posts|hewn|not|they answer",
"— Lummol. Cadhat. O yell sost. Misk.":
 "kneeling|laid|his|good|very|foot",
"— Tuss. Dhyvullol, lo dhrenn et tuss.":
 "dust|laughter|by|course|the|dust",
"— Biskyann, kethet. Pa wisklern, hos —":
 "neck|held|two|brows|one",
"— et preller — [ ]":
 "the|blade",
"Eth re dhess nahos.":
 "and|(past)|answered|no one",
}
need = json.load(open(S+'/gloss_in/W03.json'))
out=[]; seen=set()
for r in need:
    if r['rom'] in seen: continue
    seen.add(r['rom'])
    eng = G[r['rom']].split('|')
    words=[w for w,_ in r['draft']]
    assert len(eng)==len(words), (r['rom'], len(eng), len(words))
    out.append({'rom': r['rom'], 'gloss': [[w,e] for w,e in zip(words,eng)]})
json.dump(out, open(S+'/gloss/W03.json','w'), ensure_ascii=False, indent=1)
for o in out:
    print(' · '.join('%s=%s'%(w,e) for w,e in o['gloss']))
