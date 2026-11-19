import sys,pickle,numpy as np
sys.path.insert(0,'/home/user/work'); sys.path.insert(0,'/home/user/work7')
from common import AUT
import md_hp, monodromy as md
def images(p,q,prof):
    out=[]
    for M,perm in AUT:
        if not all(prof[perm[y]]==prof[y] for y in range(6)): continue
        p2=M[0,0]*p+M[0,1]*q; q2=M[1,0]*p+M[1,1]*q
        out.append((p2,q2)); out.append((np.conj(p2),np.conj(q2)))
    return out
def close(p,q,prof,TUP):
    new={}
    for p2,q2 in images(p,q,prof):
        try: t=md_hp.tuple1(p2,q2)
        except Exception as e: print('  hp label failed',e,flush=True); continue
        if not md.check(t,prof): print('  invalid tuple',flush=True); continue
        cf,au=md.canon(t)
        if cf not in TUP and cf not in new: new[cf]=(p2,q2,au)
    return new
if __name__=='__main__':
    profs=sys.argv[1]; prof=tuple(int(c) for c in profs); n=7
    import os
    C=pickle.load(open(sys.argv[2],'rb')); TUP=set(C['TUP'])
    HA=f'hardall_{profs}.pkl'; HALL=pickle.load(open(HA,'rb')) if os.path.exists(HA) else {}
    TUP|=set(HALL)
    R=pickle.load(open(sys.argv[3],'rb'))
    allnew={}
    for cf,(k,au) in R['new'].items():
        u=R['fail'][k]; nw=close(u[:n+1],u[n+1:2*n+2],prof,TUP|set(allnew)); allnew.update(nw)
        print('from hard cover',k,'new images',len(nw),flush=True)
    print('total new',len(allnew),'weighted',sum(1/v[2] for v in allnew.values()),'W before',C['W'],'after',C['W']+sum(1/v[2] for v in allnew.values()))
    HALL.update(allnew); pickle.dump(HALL,open(HA,'wb')); print('hardall',len(HALL),'weighted',sum(1/v[2] for v in HALL.values()),'W total',C['W']+sum(1/v[2] for v in HALL.values()))
