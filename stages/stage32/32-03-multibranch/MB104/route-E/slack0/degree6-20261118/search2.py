"""Pair search, large-table version. Index = quadruples of the query covers (degree a, profile reps);
stream over all covers of degree b. Vectorized verification; 40-digit recheck on demand."""
import pickle,sys,time,itertools,numpy as np
from common import *
import hp, mpmath as mp
a,b=int(sys.argv[1]),int(sys.argv[2]); assert a<=b
EPS=float(sys.argv[3]) if len(sys.argv)>3 else 2.5e-6
SH=int(sys.argv[4]) if len(sys.argv)>4 else 0; NSH=int(sys.argv[5]) if len(sys.argv)>5 else 1
import os
A=pickle.load(open(os.environ.get('AF',f'all2_{a}.pkl'),'rb')); Bd=pickle.load(open(os.environ.get('BF',f'all2_{b}.pkl'),'rb')); TAG=os.environ.get('TAG','')
nA,nB=2*a+4,2*b+4; jmin=max(nA,nB)-4; F=nA-jmin+4
def oddlist(an):
    pts=[];lab=[]
    for y in range(6):
        for z in an[y][0]:
            w=np.array((1,0) if z is None else (z,1),complex); w/=np.linalg.norm(w)
            pts.append(w); lab.append(BLAB[y])
    return np.array(pts),np.array(lab)
def wedge(u,v): return u[...,0]*v[...,1]-u[...,1]*v[...,0]
def sph(num,den):
    d=np.abs(num)**2+np.abs(den)**2
    z=2*num*np.conj(den)/d; Z=(np.abs(num)**2-np.abs(den)**2)/d
    return np.stack([z.real,z.imag,Z],-1)
def cross(P):
    z1,z2,z3,z4=P[...,0,:],P[...,1,:],P[...,2,:],P[...,3,:]
    return sph(wedge(z1,z3)*wedge(z2,z4), wedge(z1,z4)*wedge(z2,z3))
W4=np.array([27,9,3,1])
t0=time.time()
Qr=A['reps']; QA=[oddlist(c[2]) for c in Qr]
perm24=np.array(list(itertools.permutations(range(4))))
subs=np.array(list(itertools.combinations(range(F),4)))
ords=subs[:,perm24].reshape(-1,4)          # (C(F,4)*24, 4) indices into f's points
ikey=[];iS=[];ifi=[];iord=[]
for fi,(pts,lab) in enumerate(QA):
    S=cross(pts[ords]); lc=(lab[ords]*W4).sum(1)
    ikey.append(lc*4+S[:,0]+1); iS.append(S); ifi.append(np.full(len(ords),fi,np.int32)); iord.append(np.arange(len(ords),dtype=np.int32))
ikey=np.concatenate(ikey); iS=np.concatenate(iS); ifi=np.concatenate(ifi); iord=np.concatenate(iord)
o=np.argsort(ikey); ikey,iS,ifi,iord=ikey[o],iS[o],ifi[o],iord[o]
QAp=np.array([p for p,_ in QA]); QAl=np.array([l for _,l in QA])
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} F={F} query reps={len(Qr)} index={len(ikey)} table covers={len(Bd["all"])} shard {SH}/{NSH}  {time.time()-t0:.0f}s',flush=True)
quads=[]
for s in itertools.combinations(range(nB),4):
    for rest in itertools.permutations(s[1:]): quads.append((s[0],)+rest)
quads=np.array(quads)
stats=dict(cand=0,acc_max=0.0,rej_min=1.0,amb=0,amb_skipped=0,hp_acc_max=0.0,hp_rej_min=1.0,true_quad_cr_max=0.0)
hist={}; hits=[]
mp.mp.dps=40
HPc={}
HPR={}
for nn,DD in ((a,A),(b,Bd)):
    try: HPR[nn]=pickle.load(open(f'hp_{nn}.pkl','rb'))
    except FileNotFoundError: HPR[nn]=None
def _mp(z): return (mp.mpc(1),mp.mpc(0)) if z is None else (mp.mpc(mp.mpf(z[0]),mp.mpf(z[1])),mp.mpc(1))
def hp_points(side,idx):
    key=(side,idx)
    if key in HPc: return HPc[key]
    if side=='A': ri,perm,nn=idx,None,a
    else:
        c=Bd['all'][idx]; ri,ui,nn=c[4],c[5],b; perm=AUT[ui][1]
    H=HPR[nn]
    D_=A if side=='A' else Bd
    c=D_['reps'][ri]; kk=np.round(np.concatenate([c[0],c[1]]),9).tobytes()
    if H is None or kk not in H:
        p,q,an,aut=c[:4]
        an2,res,co,hpo=hp.refine(p,q,an,len(p)-1,iters=10)
        h={y:[None if z is None else (str(z.real),str(z.imag)) for z in v] for y,v in hpo.items()}
    else: h=H[kk]
    if perm is not None:
        inv={perm[y]:y for y in range(6)}; h={y:h.get(inv[y],[]) for y in range(6)}
    out=[]
    for y in range(6):
        for z in h.get(y,[]): out.append(_mp(z))
    HPc[key]=out; return out
def hpdist(fi,qi,xi,yi):
    X=hp_points('A',fi); Y=hp_points('B',qi)
    def frame(p):
        Mt=mp.matrix([[p[0][0],p[1][0]],[p[0][1],p[1][1]]]); lm=mp.lu_solve(Mt,mp.matrix([p[2][0],p[2][1]]))
        return mp.matrix([[Mt[0,0]*lm[0],Mt[0,1]*lm[1]],[Mt[1,0]*lm[0],Mt[1,1]*lm[1]]])
    M=frame([Y[k] for k in yi[:3]])*mp.inverse(frame([X[k] for k in xi[:3]]))
    D=np.zeros((len(X),len(Y)))
    for i,x in enumerate(X):
        u0=M[0,0]*x[0]+M[0,1]*x[1]; u1=M[1,0]*x[0]+M[1,1]*x[1]; nu=mp.sqrt(abs(u0)**2+abs(u1)**2)
        for j,y in enumerate(Y):
            D[i,j]=float(abs(u0*y[1]-u1*y[0])/(nu*mp.sqrt(abs(y[0])**2+abs(y[1])**2)))
    return D
def omega(close,la,lb):
    # close: (nA,nB) bool, assumed a partial matching
    ii,jj=np.nonzero(close)
    assert len(set(ii))==len(ii) and len(set(jj))==len(jj)
    j=int((la[ii]==lb[jj]).sum()); h=len(ii)-j
    return nA+nB-2*j-h
seen=set()
CH=64
allB=Bd['all']
for c0 in range(SH*CH,len(allB),CH*NSH):
    blk=range(c0,min(c0+CH,len(allB)))
    for qi in blk:
        qp,ql=oddlist(allB[qi][2])
        S=cross(qp[quads]); lc=(ql[quads]*W4).sum(1); k=lc*4+S[:,0]+1
        lo=np.searchsorted(ikey,k-4*EPS); hi=np.searchsorted(ikey,k+4*EPS,'right')
        cnt=hi-lo
        if cnt.sum()==0: continue
        qrow=np.repeat(np.arange(len(k)),cnt)
        ent=np.concatenate([np.arange(l,h) for l,h in zip(lo[cnt>0],hi[cnt>0])])
        d=np.linalg.norm(iS[ent]-S[qrow],axis=1); good=d<4*EPS
        qrow,ent,d=qrow[good],ent[good],d[good]
        if len(ent)==0: continue
        fis=ifi[ent]; xi=ords[iord[ent]]          # (C,4) f point indices
        yi=quads[qrow]                             # (C,4) q point indices
        C=len(ent); stats['cand']+=C
        Xp=QAp[fis]                                # (C,nA,2)
        x3=np.take_along_axis(Xp,xi[:,:3,None],1); y3=qp[yi[:,:3]]
        def frame(p):   # p (C,3,2) -> (C,2,2)
            Mt=np.stack([p[:,0],p[:,1]],2)
            lm=np.linalg.solve(Mt,p[:,2][:,:,None])[:,:,0]
            return Mt*lm[:,None,:]
        M=frame(y3)@np.linalg.inv(frame(x3))
        Mf=M.reshape(C,4); Mn0=Mf/np.take_along_axis(Mf,np.argmax(np.abs(Mf),1)[:,None],1)
        kr=np.round(Mn0,5); keyarr=np.concatenate([fis[:,None].astype(float),kr.real,kr.imag],1)
        _,u0=np.unique(keyarr,axis=0,return_index=True)
        stats['dup_pre']=stats.get('dup_pre',0)+C-len(u0)
        u0=np.sort(u0); fis,xi,yi,d,M,Xp=fis[u0],xi[u0],yi[u0],d[u0],M[u0],Xp[u0]; C=len(u0)
        img=np.einsum('cij,caj->cai',M,Xp); img/=np.linalg.norm(img,axis=2)[:,:,None]
        D=np.abs(wedge(img[:,:,None,:],qp[None,None,:,:]))      # (C,nA,nB) (qp normalized)
        amb=((D>1e-11)&(D<1e-4)).any((1,2))
        lowb=nA+nB-2*(D<1e-4).any(2).sum(1)
        # vectorized stats on clean candidates
        cl=~amb
        if cl.any():
            Dc_=D[cl]; m_=Dc_<1e-11
            if m_.any(): stats['acc_max']=max(stats['acc_max'],float(Dc_[m_].max()))
            stats['rej_min']=min(stats['rej_min'],float(Dc_[~m_].min()))
        far=lowb>4
        hist['>4']=hist.get('>4',0)+int(far.sum()); stats['amb_skipped']+=int((far&amb).sum())
        sel=np.nonzero(~far)[0]
        if len(sel)==0: continue
        Mn=M[sel]/np.take_along_axis(M[sel].reshape(len(sel),4),np.argmax(np.abs(M[sel].reshape(len(sel),4)),1)[:,None],1).reshape(len(sel),1,1)
        kr=np.round(Mn.reshape(len(sel),4),5)
        keyarr=np.concatenate([fis[sel][:,None].astype(float),kr.real,kr.imag],1)
        _,ui=np.unique(keyarr,axis=0,return_index=True)
        for cidx in sel[ui]:
            fi=int(fis[cidx])
            Mn1=M[cidx]/M[cidx].flat[np.argmax(np.abs(M[cidx]))]
            key=(fi,qi,tuple(np.round(Mn1.flatten(),5)))
            if key in seen: continue
            seen.add(key)
            Dc=D[cidx]
            if amb[cidx]:
                stats['amb']+=1
                Dc=hpdist(fi,qi,xi[cidx],yi[cidx])
                acc=Dc[Dc<1e-20]; rej=Dc[Dc>=1e-20]
                if acc.size: stats['hp_acc_max']=max(stats['hp_acc_max'],float(acc.max()))
                stats['hp_rej_min']=min(stats['hp_rej_min'],float(rej.min()))
                close=Dc<1e-20
            else:
                close=Dc<1e-11
            if all(close[xi[cidx][t],yi[cidx][t]] for t in range(4)):
                stats['true_quad_cr_max']=max(stats['true_quad_cr_max'],float(d[cidx]))
            om=omega(close,QAl[fi],ql)
            hist[om]=hist.get(om,0)+1
            if om<=4: hits.append((fi,qi,M[cidx].copy(),om))
    if (c0//CH)%(20*NSH)==SH: print(f'  q {c0}/{len(allB)} cand {stats["cand"]} hits {len(hits)} {time.time()-t0:.0f}s',flush=True)
print('hist',hist); print('stats',stats)
rng=np.random.default_rng(5)
def evalc(p,q,t):
    n=len(p)-1; t0_,t1_=t[...,0],t[...,1]
    P=sum(p[m]*t0_**m*t1_**(n-m) for m in range(n+1)); Qv=sum(q[m]*t0_**m*t1_**(n-m) for m in range(n+1))
    return np.stack([P,Qv],-1)
def chd(u,v): return np.abs(wedge(u,v))/(np.linalg.norm(u,axis=-1)*np.linalg.norm(v,axis=-1))
bir=[]; nonbir=0
for fi,qi,M,om in hits:
    p,q=Qr[fi][0],Qr[fi][1]; pb,qb=allB[qi][0],allB[qi][1]
    isbir=True
    for trial in range(3):
        t=rng.normal(size=2)+1j*rng.normal(size=2); v=evalc(p,q,t)
        r=np.roots((v[1]*p-v[0]*q)[::-1]); fib=np.array([[z,1] for z in r],complex)
        g=evalc(pb,qb,(M@fib.T).T); g0=evalc(pb,qb,M@t)
        if (chd(g,g0[None,:])<1e-7).sum()<2: break
    else: isbir=False
    if isbir: bir.append((fi,qi,om))
    else: nonbir+=1
print(f'|Omega|<=4 hits: {len(hits)}  non-birational: {nonbir}  BIRATIONAL: {len(bir)}')
for x in bir[:20]: print('  BIR',x)
print(f'done {time.time()-t0:.0f}s')
pickle.dump({'hitsM':[(f,q,M,om) for f,q,M,om in hits],'hits':[(f,q,om) for f,q,_,om in hits],'bir':bir,'hist':hist,'stats':stats},open(f'res2_{a}_{b}{TAG}_{SH}of{NSH}.pkl','wb'))
