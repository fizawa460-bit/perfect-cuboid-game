"""Pair search with S4-invariant (j-invariant) keys and split subsets (see cost.py).
usage: python3 search2.py a b EPS [Fa|-] [shard nshards] [dirA] [dirB]"""
import os; sys_path_fix=__import__("sys").path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../numeric-upto5-20261118"))
import pickle,sys,time,itertools,numpy as np
from common import *
a,b=int(sys.argv[1]),int(sys.argv[2]); assert a<=b
EPS=float(sys.argv[3]) if len(sys.argv)>3 else 1e-9
FA=int(sys.argv[4]) if len(sys.argv)>4 and sys.argv[4]!='-' else None
DA=sys.argv[7] if len(sys.argv)>7 else '.'; DB=sys.argv[8] if len(sys.argv)>8 else DA
A=pickle.load(open(f'{DA}/all_{a}.pkl','rb')); Bd=pickle.load(open(f'{DB}/all_{b}.pkl','rb'))
def oddlist(an):
    pts=[];lab=[];ys=[]
    for y in range(6):
        for z in an[y][0]:
            w=np.array((1,0) if z is None else (z,1),complex); w/=np.linalg.norm(w)
            pts.append(w); lab.append(BLAB[y]); ys.append(y)
    return np.array(pts),np.array(lab),np.array(ys)
def wedge(u,v): return u[...,0]*v[...,1]-u[...,1]*v[...,0]
def sph(num,den):
    d=np.abs(num)**2+np.abs(den)**2
    z=2*num*np.conj(den)/d; Z=(np.abs(num)**2-np.abs(den)**2)/d
    return np.stack([z.real,z.imag,Z],-1)
def cross(P):  # P[...,4,2]
    z1,z2,z3,z4=P[...,0,:],P[...,1,:],P[...,2,:],P[...,3,:]
    return sph(wedge(z1,z3)*wedge(z2,z4), wedge(z1,z4)*wedge(z2,z3))
nA,nB=2*a+4,2*b+4; jmin=max(nA,nB)-4
need=nA+nB-jmin+4                      # Fa+Fb >= need guarantees 4 matched pairs inside both subsets
if FA is None: FA=nA
Fa=FA; Fb=need-Fa; assert 4<=Fa<=nA and 4<=Fb<=nB, (Fa,Fb)
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} Fa={Fa} Fb={Fb} query covers={len(A["reps"])} table covers={len(Bd["all"])}',flush=True)
t0=time.time()
def jkey(P):  # P[...,4,2] -> S4-invariant: chordal point of the j-invariant
    z1,z2,z3,z4=P[...,0,:],P[...,1,:],P[...,2,:],P[...,3,:]
    num=wedge(z1,z3)*wedge(z2,z4); den=wedge(z1,z4)*wedge(z2,z3)
    Aj=(num**2-num*den+den**2)**3; Bj=(num*den*(num-den))**2
    s=np.sqrt(np.abs(Aj)**2+np.abs(Bj)**2); return sph(Aj/s,Bj/s)
def lcode(L):  # sorted label multiset of 4 labels in 0..2 -> small int
    Ls=np.sort(L,-1); return (Ls*np.array([27,9,3,1])).sum(-1)
# ---- table: unordered 4-subsets of the first Fb odd points of every table cover
Q=[oddlist(c[2]) for c in Bd['all']]
subB=np.array(list(itertools.combinations(range(Fb),4)))
keys=[];qid=[]
for i,(pts,lab,ys) in enumerate(Q):
    S=jkey(pts[subB]); keys.append(lcode(lab[subB])*4+S[:,0]+1); qid.append(np.full(len(subB),i,np.int32))
keys=np.concatenate(keys); qid=np.concatenate(qid); qq=np.tile(np.arange(len(subB),dtype=np.int32),len(Q))
o=np.argsort(keys); keys=keys[o]; qid=qid[o]; qq=qq[o]
print(f'table {len(keys)} entries, {time.time()-t0:.0f}s',flush=True)
def mob3(x,y):
    # Mobius M with M x_k ~ y_k, k=0..2 (homog). M = Ny * diag * Nx^{-1}
    def frame(p):
        Mt=np.array([p[0],p[1]]).T   # columns
        lm=np.linalg.solve(Mt,p[2]); return Mt*lm
    return frame(y)@np.linalg.inv(frame(x))
def chdist(u,v):
    return np.abs(wedge(u,v))/(np.linalg.norm(u,axis=-1)*np.linalg.norm(v,axis=-1))
import mpmath as mp
mp.mp.dps=40
def hplist(an):
    out=[]
    for y in range(6):
        for z in an['hp'].get(y,[]):
            out.append((mp.mpc(1),mp.mpc(0)) if z is None else (z,mp.mpc(1)))
    return out
HA={}; HB={}
def hpdist(fi,qi,s,pr,yq):
    if fi not in HA: HA[fi]=hplist(A['reps'][fi][2])
    if qi not in HB: HB[qi]=hplist(Bd['all'][qi][2])
    X=HA[fi]; Y=HB[qi]
    xs=[X[s[pr[k]]] for k in range(3)]; ys_=[Y[yq[k]] for k in range(3)]
    def frame(p):
        Mt=mp.matrix([[p[0][0],p[1][0]],[p[0][1],p[1][1]]]); lm=mp.lu_solve(Mt,mp.matrix([p[2][0],p[2][1]]))
        return mp.matrix([[Mt[0,0]*lm[0],Mt[0,1]*lm[1]],[Mt[1,0]*lm[0],Mt[1,1]*lm[1]]])
    M=frame(ys_)*mp.inverse(frame(xs))
    D=np.zeros((len(X),len(Y)))
    for i,x in enumerate(X):
        u0=M[0,0]*x[0]+M[0,1]*x[1]; u1=M[1,0]*x[0]+M[1,1]*x[1]
        nu=mp.sqrt(abs(u0)**2+abs(u1)**2)
        for j,y in enumerate(Y):
            D[i,j]=float(abs(u0*y[1]-u1*y[0])/(nu*mp.sqrt(abs(y[0])**2+abs(y[1])**2)))
    return D
perm24=np.array(list(itertools.permutations(range(4))))
stats={'cand':0,'acc_max':0.0,'rej_min':1.0,'cr_acc_max':0.0}
hist={}; hits=[]
SH=int(sys.argv[5]) if len(sys.argv)>5 else 0; NSH=int(sys.argv[6]) if len(sys.argv)>6 else 1
SH=int(sys.argv[5]) if len(sys.argv)>5 else 0; NSH=int(sys.argv[6]) if len(sys.argv)>6 else 1
subA=np.array(list(itertools.combinations(range(Fa),4)))
QP=np.array([x[0] for x in Q]); QL=np.array([x[1] for x in Q])          # (Ncov,nB,2), (Ncov,nB)
TS=jkey(QP[qid[:,None],subB[qq]])   # (Nent,3) j-key of every table entry
def mob3v(x,y):  # batched: M x_k ~ y_k for k=0..2 ; x,y (C,3,2)
    def frame(p):
        Mt=np.stack([p[:,0],p[:,1]],-1)                      # columns p0,p1
        lm=np.linalg.solve(Mt,p[:,2][:,:,None])[:,:,0]
        return Mt*lm[:,None,:]
    return frame(y)@np.linalg.inv(frame(x))
stats['dup_skipped']=0; stats['amb_skipped']=0; stats['amb']=0
for fi,(p,q,an,aut) in enumerate(A['reps']):
    if fi%NSH!=SH: continue
    pts,lab,ys=oddlist(an)
    SA=jkey(pts[subA]); kA=lcode(lab[subA])*4+SA[:,0]+1
    lo=np.searchsorted(keys,kA-EPS*4); hi=np.searchsorted(keys,kA+EPS*4,'right')
    cnt=hi-lo
    if cnt.sum()==0: continue
    R_=np.repeat(np.arange(len(kA)),cnt); E_=np.repeat(lo,cnt)+(np.arange(cnt.sum())-np.repeat(np.cumsum(cnt)-cnt,cnt))
    ok=np.linalg.norm(TS[E_]-SA[R_],axis=1)<=EPS*4; R_=R_[ok]; E_=E_[ok]
    if len(R_)==0: continue
    QI=qid[E_]; T_=subB[qq[E_]]                                  # (C,4)
    YQ=T_[:,perm24]                                              # (C,24,4)
    labok=(QL[QI[:,None,None],YQ]==lab[subA[R_]][:,None,:]).all(-1)
    c_,p_=np.nonzero(labok)
    R2=R_[c_]; QI2=QI[c_]; YQ2=YQ[c_,p_]
    X=pts[subA[R2]]; Y=QP[QI2[:,None],YQ2]
    d=np.linalg.norm(cross(Y)-cross(X),axis=1); ok=d<=EPS*4
    R2,QI2,YQ2,X,Y,d=R2[ok],QI2[ok],YQ2[ok],X[ok],Y[ok],d[ok]
    if len(R2)==0: continue
    stats['cand']+=len(R2)
    M=mob3v(X[:,:3],Y[:,:3])
    Mf=M.reshape(len(M),4); Mn=Mf/Mf[np.arange(len(Mf)),np.argmax(np.abs(Mf),1)][:,None]
    kk=np.concatenate([QI2[:,None].astype(float),np.round(Mn.real,6),np.round(Mn.imag,6)],1)
    _,ui=np.unique(kk,axis=0,return_index=True); stats['dup_skipped']+=len(R2)-len(ui)
    R2,QI2,YQ2,M,d=R2[ui],QI2[ui],YQ2[ui],M[ui],d[ui]
    img=np.einsum('cij,nj->cni',M,pts); img/=np.linalg.norm(img,axis=2)[:,:,None]
    D=chdist(img[:,:,None,:],QP[QI2][:,None,:,:])               # (U,nA,nB)
    amb=((D>1e-11)&(D<1e-4)).any((1,2))
    nclose=(D<1e-4).any(2).sum(1)
    skip=amb&(nA+nB-2*nclose>4)
    stats['amb_skipped']+=int(skip.sum()); hist['>4(skipped)']=hist.get('>4(skipped)',0)+int(skip.sum())
    for u in np.nonzero(~skip)[0]:
        qi=int(QI2[u]); yq=YQ2[u]; s=subA[R2[u]]; Du=D[u]; ql=QL[qi]
        if amb[u]:
            stats['amb']+=1
            Du=hpdist(fi,qi,s,np.arange(4),yq)
            stats['hp_acc_max']=max(stats.get('hp_acc_max',0),float(Du[Du<1e-20].max()) if (Du<1e-20).any() else 0)
            stats['hp_rej_min']=min(stats.get('hp_rej_min',1),float(Du[Du>=1e-20].min()))
            close=Du<1e-20
        else: close=Du<1e-11
        acc=Du[close]; rej=Du[~close]
        if acc.size: stats['acc_max']=max(stats['acc_max'],acc.max())
        stats['rej_min']=min(stats['rej_min'],rej.min())
        stats['cr_acc_max']=max(stats['cr_acc_max'],float(d[u]))
        if all(close[s[k],yq[k]] for k in range(4)): stats['true_quad_cr_max']=max(stats.get('true_quad_cr_max',0),float(d[u]))
        ii,jj=np.nonzero(close)
        assert len(set(ii))==len(ii) and len(set(jj))==len(jj)
        j=int((lab[ii]==ql[jj]).sum()); h=len(ii)-j; om=nA+nB-2*j-h
        hist[om]=hist.get(om,0)+1
        if om<=4: hits.append((fi,qi,M[u],om,j,h))
print('hist (distinct (f,q,M) found via quadruples)',hist)
print('stats',stats)
# ---- birationality test
rng=np.random.default_rng(5)
def evalc(p,q,t):  # t homog array (...,2); p,q coeff low->high of degree n
    n=len(p)-1; t0,t1=t[...,0],t[...,1]
    P=sum(p[m]*t0**m*t1**(n-m) for m in range(n+1)); Qv=sum(q[m]*t0**m*t1**(n-m) for m in range(n+1))
    return np.stack([P,Qv],-1)
nonbir=0; bir=[]
for fi,qi,M,om,j,h in hits:
    p,q,_,_=A['reps'][fi]; pb,qb,_,_=Bd['all'][qi]
    isbir=True
    for trial in range(3):
        t=rng.normal(size=2)+1j*rng.normal(size=2)
        v=evalc(p,q,t)
        # fibre of f over v: roots of v1 P - v0 Q
        poly=(v[1]*p-v[0]*q)[::-1]; r=np.roots(poly)
        fib=np.array([[z,1] for z in r],complex)
        g=evalc(pb,qb,(M@fib.T).T); g0=evalc(pb,qb,M@t)
        dd=chdist(g,g0[None,:])
        if (dd<1e-7).sum()<2: break   # only t itself -> injective here
    else: isbir=False
    if isbir: bir.append((fi,qi,om,j,h))
    else: nonbir+=1
print(f'|Omega|<=4 hits: {len(hits)}  non-birational: {nonbir}  BIRATIONAL: {len(bir)}')
for x in bir[:20]: print('  BIR',x)
print(f'done {time.time()-t0:.0f}s')
pickle.dump({'hits':hits,'bir':bir,'hist':hist,'stats':stats},open(f'res2_{a}_{b}_{SH}of{NSH}.pkl','wb'))
