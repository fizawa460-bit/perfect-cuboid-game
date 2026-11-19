import sys, os, pickle, numpy as np
F = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fast40-20261118'
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(F, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import hp_fast
from covers import BP
sys.argv = _a
import mpmath as mp
n=7
E=pickle.load(open(sys.argv[1],'rb')); prof=tuple(E['prof']); idxs=[int(i) for i in sys.argv[2].split(',')]
for i in idxs:
    u=E['sols'][i]; p,q=u[:n+1],u[n+1:2*n+2]; crit=list(E['fixed'][:3])+list(u[2*n+2:]); ysl=list(E['ys'])
    an={y:([], [c for c,yy in zip(crit,ysl) if yy==y]) for y in range(6)}
    for y in range(6):
        g=(BP[y][1]*p-BP[y][0]*q)[::-1].copy()
        for c in an[y][1]:
            for _ in range(2): g,_r=np.polydiv(g,np.array([1,-c]))
        an[y]=(list(np.roots(g))+[None]*(n-2*prof[y]-(len(g)-1)),an[y][1])
    for dps,it in ((40,12),(60,15),(60,40),(100,40),(100,120)):
        with mp.workdps(dps):
            out,res,com,hpodd,critm,ys,nit=hp_fast.refine_full(p,q,an,n,iters=it,dps=dps)
            cm=sorted(critm,key=lambda z:(float(z.real)))
            dcc=min(abs(a-b) for k,a in enumerate(critm) for b in critm[:k])
            # common-root test: resultant proxy = min over roots of P of |Q|
            P=com[:n+1]; Q=com[n+1:]
            rp=mp.polyroots([c for c in P][::-1],maxsteps=500,extraprec=300)
            mq=min(abs(sum(Q[m]*r**m for m in range(n+1)))/max(abs(v) for v in Q)/(1+abs(r))**n for r in rp)
        print(i,dps,it,'res',mp.nstr(res,3),'min crit-crit',mp.nstr(dcc,3),'min |Q| on roots of P',mp.nstr(mq,3),flush=True)
