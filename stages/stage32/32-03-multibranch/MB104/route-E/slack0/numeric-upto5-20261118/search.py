import pickle,sys,time,itertools,numpy as np
from common import *
a,b=int(sys.argv[1]),int(sys.argv[2]); assert a<=b
EPS=float(sys.argv[3]) if len(sys.argv)>3 else 1e-9
TOL=float(sys.argv[4]) if len(sys.argv)>4 else 1e-6
A=pickle.load(open(f'all_{a}.pkl','rb')); Bd=pickle.load(open(f'all_{b}.pkl','rb'))
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
nA,nB=2*a+4,2*b+4; jmin=max(nA,nB)-4; F=nA-jmin+4
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} F={F} query covers={len(A["reps"])} table covers={len(Bd["all"])}',flush=True)
t0=time.time()
# ---- table
Q=[oddlist(c[2]) for c in Bd['all']]
quads=[]
for s in itertools.combinations(range(nB),4):
    for rest in itertools.permutations(s[1:]): quads.append((s[0],)+rest)
quads=np.array(quads)        # (Nq,4)
keys=[];qid=[];qix=[]
for i,(pts,lab,ys) in enumerate(Q):
    S=cross(pts[quads]); lc=(lab[quads]*np.array([27,9,3,1])).sum(1)
    keys.append(lc*4+S[:,0]+1); qid.append(np.full(len(quads),i,np.int32))
keys=np.concatenate(keys); qid=np.concatenate(qid); qq=np.tile(np.arange(len(quads),dtype=np.int32),len(Q))
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
for fi,(p,q,an,aut) in enumerate(A['reps']):
    if fi%NSH!=SH: continue
    pts,lab,ys=oddlist(an)
    seen=set()
    for s in itertools.combinations(range(F),4):
        X=pts[np.array(s)][perm24]                      # 24,4,2
        S=cross(X); lc=(lab[np.array(s)][perm24]*np.array([27,9,3,1])).sum(1)
        k=lc*4+S[:,0]+1
        lo=np.searchsorted(keys,k-EPS*4); hi=np.searchsorted(keys,k+EPS*4,'right')
        for r in range(24):
            for e in range(lo[r],hi[r]):
                qi=qid[e]; qp,ql,qy=Q[qi]; yq=quads[qq[e]]
                Sy=cross(qp[yq]); d=np.linalg.norm(Sy-S[r])
                if d>EPS*4: continue
                stats['cand']+=1
                xs=X[r]; M=mob3(xs[:3],qp[yq[:3]])
                Mn=M/M.flat[np.argmax(np.abs(M))]
                key=(int(qi),tuple(np.round(Mn.flatten(),6)))
                if key in seen: stats['dup_skipped']=stats.get('dup_skipped',0)+1; continue
                img=(M@pts.T).T; img/=np.linalg.norm(img,axis=1)[:,None]
                D=chdist(img[:,None,:],qp[None,:,:])
                amb=(D>1e-11)&(D<1e-4)
                if amb.any() and nA+nB-2*int((D<1e-4).any(1).sum())>4:
                    stats['amb_skipped']=stats.get('amb_skipped',0)+1
                    close=D<1e-11
                    hist['>4(skipped)']=hist.get('>4(skipped)',0)+1
                    continue
                if amb.any():
                    stats['amb']=stats.get('amb',0)+1
                    D=hpdist(fi,int(qi),s,perm24[r],yq)
                    stats['hp_acc_max']=max(stats.get('hp_acc_max',0),float(D[D<1e-20].max()) if (D<1e-20).any() else 0)
                    stats['hp_rej_min']=min(stats.get('hp_rej_min',1),float(D[D>=1e-20].min()))
                    close=D<1e-20
                else:
                    close=D<1e-11
                acc=D[close]; rej=D[~close]
                if acc.size: stats['acc_max']=max(stats['acc_max'],acc.max())
                stats['rej_min']=min(stats['rej_min'],rej.min())
                stats['cr_acc_max']=max(stats['cr_acc_max'],d)
                ii,jj=np.nonzero(close)
                qd=[int(x) for x in np.array(s)[perm24[r]]]
                if all(close[qd[k],yq[k]] for k in range(4)):
                    stats['true_quad_cr_max']=max(stats.get('true_quad_cr_max',0),float(d))
                assert len(set(ii))==len(ii) and len(set(jj))==len(jj)
                j=int((lab[ii]==ql[jj]).sum()); h=len(ii)-j
                om=nA+nB-2*j-h
                seen.add(key)
                hist[om]=hist.get(om,0)+1
                if om<=4: hits.append((fi,int(qi),M,om,j,h))
    if fi%20==0: print(f'  f {fi}/{len(A["reps"])} cand {stats["cand"]} hits {len(hits)} {time.time()-t0:.0f}s',flush=True)
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
pickle.dump({'hits':hits,'bir':bir,'hist':hist,'stats':stats},open(f'res_{a}_{b}_{SH}of{NSH}.pkl','wb'))
