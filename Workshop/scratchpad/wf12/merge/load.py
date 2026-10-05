import csv, glob, os, sys
S='/private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad'
def read_tsv(p):
    rows=[]
    with open(p,encoding='utf-8') as f:
        lines=f.read().split('\n')
    hdr=lines[0].split('\t')
    for ln in lines[1:]:
        if not ln.strip(): continue
        parts=ln.split('\t')
        rows.append(dict(zip(hdr,parts+['']*(len(hdr)-len(parts)))) | {'_ncols':len(parts)})
    return hdr,rows
def shared():
    return read_tsv(S+'/wf7/lexicon_orrowen.tsv')
def additions():
    out=[]
    for p in sorted(glob.glob(S+'/wf8/additions/*.tsv')):
        u=os.path.basename(p)[:-4]
        h,rs=read_tsv(p)
        for r in rs:
            r['_unit']=u; r['_hdr']=h
            out.append(r)
    return out
