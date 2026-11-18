import pickle,sys,numpy as np,hp
from covers import *
fn=sys.argv[1]; d=pickle.load(open(fn,'rb')); n=d['n']; prof=d['prof']
keep=[];res_=[];INV=[]
for (x,a),an in zip(d['covers'],d['ans']):
    an2,res,co,hpo=hp.refine(x[:n+1],x[n+1:],an,n,iters=12)
    pts=[z for y in range(6) for t in (0,1) for z in an2[y][t]]
    P=np.array([[1,0] if z is None else [z,1] for z in pts],complex)
    D=np.abs(P[:,None,0]*P[None,:,1]-P[:,None,1]*P[None,:,0])/(np.abs(P).sum(1)[:,None]*np.abs(P).sum(1)[None,:]); np.fill_diagonal(D,9)
    moved=max(abs(z1-z2) for y in range(6) for z1,z2 in zip(an[y][0],an2[y][0]) if z1 is not None and z2 is not None)
    ok=res<1e-25 and D.min()>1e-5 and moved<1e-6
    res_.append((res,D.min(),moved,ok))
    if ok:
        a=autcount(an2); v=invariant(an2)
        if all(np.abs(u-v).max()>=1e-7*(1+np.abs(v).max()) for u in INV): INV.append(v); keep.append(((x,a),an2))
print(fn,len(d["covers"]),"valid distinct",len(keep),sum(1/a for (x,a),an in keep))
bad=[r for r in res_ if not r[3]]; print('invalid examples',bad[:5])
if len(sys.argv)>2: d['covers']=[k[0] for k in keep]; d['ans']=[k[1] for k in keep]; pickle.dump(d,open(fn,'wb'))
