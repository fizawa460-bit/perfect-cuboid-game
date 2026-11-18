import sys,pickle,time,closure
from covers import *
n=int(sys.argv[1]); prof=tuple(int(x) for x in sys.argv[2].split(','))
target=float(sys.argv[4]); batch=int(sys.argv[5]) if len(sys.argv)>5 else 2000
ys=[y for y in range(6) for _ in range(prof[y])]
import os
seed=int(sys.argv[3])
fixed=np.array([0.31+0.17j,-0.52+0.44j,0.13-0.61j]) if seed==7 else np.random.default_rng(seed).normal(size=3)+1j*np.random.default_rng(seed+1).normal(size=3)
outfn=f'cov_{n}_{"".join(map(str,prof))}.pkl' if seed==7 else f'seed/cov_{n}_{"".join(map(str,prof))}_{seed}.pkl'
if seed!=7: os.makedirs('seed',exist_ok=True)
found={}; t0=time.time(); tries=0
INV=[]
def isnew(an):
    v=invariant(an)
    for u in INV:
        if np.abs(u-v).max()<1e-6*(1+np.abs(v).max()): return False
    INV.append(v); return True
while True:
    x,c,res=newton_batch(n,ys,batch,fixed)
    tries+=batch
    for i in np.nonzero(res<1e-10)[0]:
        an=analyse(x[i,:n+1],x[i,n+1:],n,prof,c[i],ys)
        if an is None: continue
        fp,aut=fingerprint(an)
        if isnew(an):
            found[len(found)]=(x[i].copy(),aut)
            if seed!=7:
                stack=[(x[i].copy(),an)]
                while stack:
                    xx,aa=stack.pop()
                    for x2,an2 in closure.images(xx,aa,n,prof):
                        if isnew(an2): found[len(found)]=(x2,aut); stack.append((x2,an2))
    w=sum(1/a for _,a in found.values())
    print(f'tries {tries} found {len(found)} weighted {w} target {target} t={time.time()-t0:.0f}s',flush=True)
    if abs(w-target)<1e-9 or w>target or tries>=int(sys.argv[6] if len(sys.argv)>6 else 10**6): break
    if seed!=7: pickle.dump({'n':n,'prof':prof,'covers':[v for v in found.values()]},open(outfn,'wb'))
pickle.dump({'n':n,'prof':prof,'covers':[v for v in found.values()]},open(outfn,'wb'))
