import sys, os, pickle, numpy as np
F = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fast40-20261118'
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(F, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import hp_fast
from covers import BP
sys.argv = _a
import mpmath as mp
n=7; rows=[]
def prep(p,q,crit,ysl,prof):
    an={y:([], [c for c,yy in zip(crit,ysl) if yy==y]) for y in range(6)}
    for y in range(6):
        g=(BP[y][1]*p-BP[y][0]*q)[::-1].copy()
        for c in an[y][1]:
            for _ in range(2): g,_r=np.polydiv(g,np.array([1,-c]))
        an[y]=(list(np.roots(g))+[None]*(n-2*prof[y]-(len(g)-1)),an[y][1])
    return an
def dcc(critm): return min(abs(a-b) for k,a in enumerate(critm) for b in critm[:k])
for fn in sys.argv[1:]:
    E=pickle.load(open(fn,'rb')); prof=tuple(E['prof'])
    for i,u in enumerate(E['sols']):
        p,q=u[:n+1],u[n+1:2*n+2]; crit=list(E['fixed'][:3])+list(u[2*n+2:]); ysl=list(E['ys'])
        an=prep(p,q,crit,ysl,prof); r=[]
        for dps,it in ((40,12),(80,60)):
            with mp.workdps(dps):
                out,res,com,hpodd,critm,ys,nit=hp_fast.refine_full(p,q,an,n,iters=it,dps=dps); r.append((float(res),float(dcc(critm))))
        d0=float(dcc([mp.mpc(c) for c in crit]))
        rows.append((fn,i,d0,r[0],r[1])); 
        flag = r[1][1] < 0.1*r[0][1] or r[1][0] > 1e-60
        if flag: print('DRIFT',fn,i,'double',f'{d0:.1e}',r,flush=True)
    print(fn,'done',len(E['sols']),flush=True)
pickle.dump(rows,open('drift_rows.pkl','wb'))
