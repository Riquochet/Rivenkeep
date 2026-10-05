"""heuristic sweep: is each on-page gloss supported by the lexicon rows the analyzer finds for its word?"""
import sys, json, os, re, collections
sys.path.insert(0,'/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/orig')
import orr_analyze as OA
W13='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf13'
lex=OA.Lexicon(OA.LEX)
IRR=dict(x.split('>') for x in '''held>hold laid>lay went>go came>come knew>know drew>draw spoke>speak said>say wrote>write grew>grow took>take fell>fall kept>keep told>tell found>find bore>bear brought>bring began>begin broke>break stood>stand sat>sit gave>give made>make saw>see ran>run rose>rise sang>sing slept>sleep fought>fight left>leave set>set burnt>burn built>build thought>think heard>hear felt>feel met>meet led>lead sent>send struck>strike swore>swear threw>throw wore>wear won>win woke>wake ate>eat drank>drink flew>fly forgot>forget hid>hide meant>mean paid>pay sold>sell shook>shake sought>seek taught>teach tore>tear understood>understand wept>weep bound>bind bled>bleed dug>dig fed>feed fled>flee hung>hang knelt>kneel lit>light lost>lose rode>ride shone>shine shot>shoot slew>slay stole>steal swam>swim sank>sink spun>spin strove>strive chose>choose froze>freeze drove>drive did>do had>have men>man women>woman children>child feet>foot teeth>tooth were>was are>is be>is been>is am>is spake>speak sware>swear died>die dead>die broken>break given>give known>know taken>take fallen>fall born>bear risen>rise sung>sing woven>weave wove>weave held>hold dwelt>dwell sprang>spring bade>bid gone>go done>do worn>wear torn>tear shorn>shear hewn>hew sown>sow grown>grow drawn>draw'''.split())
STOP=set('i we you he she it they two me him her us them my our your his its their the a an of past future question is was not one to'.split())
SELF={'itself','themselves','myself','yourself','herself','himself','ourselves','yourselves'}
def stem(w):
    w=w.lower().strip("'’")
    if w in SELF: return 'self'
    w=IRR.get(w,w)
    if w.endswith('ied') or w.endswith('ies'):
        return w[:-3]+'y'
    if w.endswith('ves') and len(w)>4: return w[:-3]+'f'
    for suf in ('ings','ing','ed','es','s','ly','er','est','ers','ard','ardath','eth','ath'):
        if w.endswith(suf) and len(w)-len(suf)>=3:
            w=w[:-len(suf)]
            if len(w)>3 and w[-1]==w[-2] and w[-1] not in 'lsz': w=w[:-1]
            if w.endswith('e') and len(w)>3: w=w[:-1]
            return w
    if w.endswith('e') and len(w)>3: w=w[:-1]
    return w
def toks(s):
    return [t for t in re.findall(r"[a-zA-Z']+", s.lower())]
def support(wd):
    txt=[wd.gloss]
    rows=[]
    if wd.best is not None and wd.best.row is not None: rows.append(wd.best.row)
    for p in wd.parses:
        if p.row is not None: rows.append(p.row)
    rows+=lex.get(wd.tok)
    for r in rows: txt+= [r.get('meanings') or '', r.get('canon_sense') or '', r.get('book_lemmas') or '', r.get('orrowen') or '', r.get('derivation') or '']
    # phrase rows that contain this word
    return ' '.join(txt)
pairs=collections.Counter(); unsup=collections.defaultdict(list); total=0; mismatch_lines=[]
for f in sorted(os.listdir(W13+'/gloss')):
    for r in json.load(open(W13+'/gloss/'+f)):
        words=[w for w in OA.analyse_text(r['rom'], lex) if w.kind!='punct']
        if len(words)!=len(r['gloss']):
            mismatch_lines.append((f, r['rom'][:80], len(words), len(r['gloss']))); continue
        hints=' '.join(m for _,m in OA.phrase_hints(OA.analyse_text(r['rom'], lex), lex))
        for wd,(w,g) in zip(words, r['gloss']):
            total+=1
            content=[t for t in toks(g) if t not in STOP]
            if not content: continue
            sup=set(stem(t) for t in toks(support(wd)+' '+hints))
            if any(stem(t) in sup for t in content): continue
            unsup[(w.lower(), g)].append((f, r['rom']))
print('boxes', total, 'lines with a different token count', len(mismatch_lines))
for m in mismatch_lines[:20]: print('  ', m)
print('distinct (word, gloss) pairs without lexical support:', len(unsup), ' boxes:', sum(len(v) for v in unsup.values()))
for (w,g),v in sorted(unsup.items(), key=lambda x:(-len(x[1]), x[0])):
    print('%4d  %-16s -> %-26s  e.g. [%s] %s' % (len(v), w, g, v[0][0], v[0][1][:90]))
print('\n=== review table')
for (w,g),v in sorted(unsup.items(), key=lambda x:(-len(x[1]), x[0])):
    f,rom=v[0]
    words=[x for x in OA.analyse_text(rom, lex) if x.kind!='punct']
    wd=[x for x in words if x.tok.lower()==w][0]
    rows=[]
    if wd.best is not None and wd.best.row is not None: rows.append(wd.best.row)
    for p in wd.parses:
        if p.row is not None and p.row not in rows: rows.append(p.row)
    m=' | '.join('%s: %s' % (r.get('orrowen'), (r.get('meanings') or '')[:70]) for r in rows[:3])
    print('%-14s %-22s an=%-22s %s' % (w, g, wd.gloss, m[:170]))
