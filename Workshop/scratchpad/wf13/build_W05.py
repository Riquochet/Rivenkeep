import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
G = {
"Kaelir sa re vymm dem varn": ['wreck','that','(past)','went back','to','home'],
"Ul nunn et grem sullast.": ['in','deep','the','winter','third'],
"Re yalant garlath Halvard um et sceth sy; nath re femm Rhyna o, eth stinel dhant lunnat ul ey garlremullath, veth re heth ey o hosen re heth o o, hosen keth lonn lonn.":
 ['(past)','they were','hands','Halvard','on','the','hull','this',
  'not','(past)','touched','Rhyna','it',
  'and','stroke','salt','open','in','her','palms',
  'but','(past)','knew','she','it','as','(past)','knew','he','it',
  'as','knows','kin','kin'],
"— Tant. Tant ul grynir eth crynir. Brid, fedh sell.": ['salt','salt','in','board','and','board','cold','time','long'],
"— Tolm, ul drodol. Dusstyvil, vimm, ulo eth hyo. Et wadh ulo.": ['stone','in','flashing','iron','low','into-it','and','out-of-it','the','sea','in-it'],
"— Dem varn, amm grestet. Dem varn, niss. Brodhol dem lonn.": ['to','home','when','wounded','to','home','slow','telling','to','kin'],
"— Vesk hosast —": ['look!','first'],
"— eth hy ull osk.": ['and','from','that','trust!'],
"— Pawast. Et wadh ull sost. Hosel, eth niss.": ['again','the','sea','that','very','alone','and','slow'],
"— Hos vorr, driget. Ul vodh re omm o — [ ]": ['one','fire','thrown','in','what','(past)','fell','it'],
"— Tolm, ul drodol. Dusstyvil, vimm, ulo eth —": ['stone','in','flashing','iron','low','into-it','and'],
"Eth re dhess nahos.": ['and','(past)','answered','no one'],
}
need = json.load(open(S+'/gloss_in/W05.json'))
out=[]; seen=set()
for r in need:
    if r['rom'] in seen: continue
    seen.add(r['rom'])
    words=[w for w,_ in r['draft']]
    g=G[r['rom']]
    assert len(g)==len(words),(r['rom'],len(g),len(words))
    out.append({'rom':r['rom'],'gloss':[[w,e] for w,e in zip(words,g)]})
json.dump(out,open(S+'/gloss/W05.json','w'),ensure_ascii=False,indent=1)
for o in out:
    print(o['rom']); print('   '+' · '.join('%s=%s'%(w,e) for w,e in o['gloss']))
