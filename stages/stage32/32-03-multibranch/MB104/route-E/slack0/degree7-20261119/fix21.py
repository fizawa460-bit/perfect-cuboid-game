import sys,os,pickle,numpy as np
sys.path.insert(0,'/home/user/work'); sys.path.insert(0,'/home/user/work7')
from common import AUT
import md_hp, monodromy as md
n=7; E=pickle.load(open('extra_7_112323.pkl','rb')); prof=tuple(E['prof'])
target=md.canon(E['tuples'][21])[0]
conjy={0:0,1:1,2:2,3:3,4:5,5:4}
for k in [int(a) for a in sys.argv[1:]]:
    u=E['sols'][k]; p,q=u[:n+1],u[n+1:2*n+2]; c=list(E['fixed'][:3])+list(u[2*n+2:]); ysl=list(E['ys'])
    for ui,(M,perm) in enumerate(AUT):
        if not all(prof[perm[y]]==prof[y] for y in range(6)): continue
        p2=M[0,0]*p+M[0,1]*q; q2=M[1,0]*p+M[1,1]*q; y2=[perm[y] for y in ysl]
        for cj in (0,1):
            pp,qq,cc,yy=(p2,q2,c,y2) if not cj else (np.conj(p2),np.conj(q2),list(np.conj(c)),[conjy[y] for y in y2])
            try: t=md_hp.tuple1(pp,qq)
            except Exception as e: print(k,ui,cj,'fail',e,flush=True); continue
            cf,au=md.canon(t)
            print(k,ui,cj,'match' if cf==target else '-',flush=True)
            if cf==target: pickle.dump((pp,qq,cc,yy,au),open('fix21.pkl','wb')); sys.exit()
