import json
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
need=json.load(open(S+'/gloss_in/W02.json'))
G = [
 ['Axe','in','Grain'],
 ['the','winter','third','in','Tide','Remembering'],
 ['(past)','took up','Rhyna','the','heart','this','on','the','shingle','and','(past)','was','the','shape','only','at','Halyna (the two)',
  'winter','this','(past)','came','it','whole','into','Halvard','in','the','vault','and','into-her','in','middle','the','children',
  'was','three','nights','the','telling','from','what','(past)','was','it','in-them-two','like','wound','and','not','(past)','was','like','tale'],
 ['courses','tall','skin','dark','holding','the','breath','to','low'],
 ['oars','oars','many','from','that','iron','in','the','skin'],
 ['one','and'],
 ['strokes','counted','every','stroke','counted'],
 ['(past)','fell','every','one','and','(past)','opened','the','sky','pale'],
 ['and','pale','and','hard','shoots','cut','and','cut','again'],
 ['signs','soft','on','the','thing','mute'],
 ['and','not','(past)'],
 ['two','marks','shape','the','wood','that','(past)','was','sight','at','Halyna (the two)','and','not','(past)','was','yet','telling','at-them-two'],
 ['the','first','the','posts','many','and','memory','cut','at','their','course','to','the','heart',
  'thing','that','(past)','held','one','pillar','(past)','held','every','course','it','from','root','to','root',
  'the','second','the','mouth','turned','and','bonded','across','the','rings','to','plea','carved','on','the','stone',
  'not','(past)','answered','it'],
 ['and','(past)','answered','no one'],
]
out=[]
for r,g in zip(need,G):
    words=[w for w,_ in r['draft']]
    assert len(words)==len(g),(r['rom'][:40],len(words),len(g))
    out.append({'rom':r['rom'],'gloss':[[w,e] for w,e in zip(words,g)]})
json.dump(out,open(S+'/gloss/W02.json','w'),ensure_ascii=False,indent=1)
for o in out:
    print(' · '.join('%s=%s'%(w,e) for w,e in o['gloss']))
