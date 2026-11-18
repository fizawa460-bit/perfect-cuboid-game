"""Build full cover lists from per-profile pickles that store 'ans' (mono.py) or from older pickles via allcovers.
   Output all2_n.pkl: reps=[(p,q,an,aut)], all=[(p,q,an,aut,rep_index,U_index)] (no 40-digit refinement here)."""
import glob,pickle,sys,numpy as np
from covers import *
import allcovers
def load(n):
    reps=[]
    files=sorted(glob.glob(f'mono/cov_{n}_*.pkl'))
    if not files:
        r,_=allcovers.load_reps(n); return [(p,q,{y:an[y] for y in range(6)},aut) for p,q,an,aut in r]
    for fn in files:
        d=pickle.load(open(fn,'rb'))
        for (x,aut),an in zip(d['covers'],d['ans']): reps.append((x[:n+1],x[n+1:],an,aut))
    return reps
def build(n):
    reps=allcovers.dedupe(load(n)) if n>2 else load(n)
    allc=[]
    for ri,(p,q,an,aut) in enumerate(reps):
        for ui,(M,perm) in enumerate(AUT):
            p2=M[0,0]*p+M[0,1]*q; q2=M[1,0]*p+M[1,1]*q
            allc.append((p2,q2,{perm[y]:an[y] for y in range(6)},aut,ri,ui))
    allc=allcovers.dedupe(allc)
    return reps,allc
if __name__=='__main__':
    for n in map(int,sys.argv[1:]):
        reps,allc=build(n)
        print(n,'reps',len(reps),'weighted reps',sum(1/c[3] for c in reps),'all',len(allc),'weighted',sum(1/c[3] for c in allc),flush=True)
        pickle.dump({'reps':reps,'all':allc},open(f'all2_{n}.pkl','wb'))
