import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
G = {
"Reskowath strom sa orrant um wadh":
 ["seats","great","that","they walk","on","sea"],
"Lo dhrenn et surr vranast, cumm eth cumm.":
 ["by","course","the","year","sixth","haven","and","haven"],
"— Nynth. Lesteth, nalelv umor.":
 ["water","houses","heavy","on-us"],
"— Misketh, ul morrol umor. Lilvyl, ul et sedh.":
 ["feet","in","walking","on-us","rot","in","the","fen"],
"— Meskrivullath, ul morrol. Tolm, ul dessyl.":
 ["roots","in","walking","stone","in","answering"],
"— Vorrdhuss. Domm, ul vimm et hal.":
 ["ash","dark","in","low","the","bedrock"],
"— Sulv. Fedh sell ul et sulv.":
 ["white","time","long","in","the","white"],
"— Helv, bemmet. Sirr —":
 ["sky","lifted","glass"],
"— cresket. Vollath, ul vimm gor yalat. Thae — [ ]":
 ["broken","names","in","low","every","thing","Thae"],
"Eth re dhess nahos.":
 ["and","(past)","answered","no one"],
}
head = ["at","seats","great","fallen","every","one","(past)","went in","one","from","Halyna (the two)","into","heart","the","timbers",
 "and","(past)","stood","other","at","edge","at","shoulder","the","soldiers","who","(past)","they refused","going","near",
 "and","(past)","knew","the","one","out-of-it","it","as","(past)","knew","the","one","in-it",
 "is","heart","seat","great","known","in","one","breath","and","the","name","last","and","hard","very"]
# fix stray '(past)|went-in' split handled above
d = json.load(open(S+'/gloss_in/W08.json'))
out=[]; seen=set()
for r in d:
    if r['rom'] in seen: continue
    seen.add(r['rom'])
    words=[w for w,_ in r['draft']]
    g = G.get(r['rom'])
    if g is None: g = head
    assert len(g)==len(words), (r['rom'][:40], len(g), len(words))
    out.append({'rom':r['rom'],'gloss':[[w,e] for w,e in zip(words,g)]})
json.dump(out, open(S+'/gloss/W08.json','w'), ensure_ascii=False, indent=1)
for o in out: print(' · '.join('%s=%s'%(w,e) for w,e in o['gloss']))
