import sys,pickle,time,os,numpy as np
from covers import *
import closure, track, hp
n=int(sys.argv[1]); prof=tuple(int(v) for v in sys.argv[2].split(',')); seed=int(sys.argv[3]); target=float(sys.argv[4])
maxtime=float(sys.argv[5]) if len(sys.argv)>5 else 3600
rng2=np.random.default_rng(seed+1000)
ys=[y for y in range(6) for _ in range(prof[y])]; K=len(ys)
fixed=np.array([0.31+0.17j,-0.52+0.44j,0.13-0.61j])
outfn=f'mono/cov_{n}_{"".join(map(str,prof))}.pkl'; os.makedirs('mono',exist_ok=True)
MS=np.array([[1,0.37+1.21j],[1,-2.3+0.71j]],complex); MSi=np.linalg.inv(MS)
W=np.array([(MS[0]@np.array(BP[y],complex))/(MS[1]@np.array(BP[y],complex)) for y in range(6)])
found=[]; INV=[]; t0=time.time()
def isnew(an):
    v=invariant(an)
    for u in INV:
        if np.abs(u-v).max()<1e-5*(1+np.abs(v).max()): return False
    INV.append(v); return True
def add(x,c,ysl=None,seedmode=False):
    """x,c original coords; returns True if new"""
    yl=ys if ysl is None else ysl
    Lc=np.ones(2*n+2); xx=x/(x@Lc)
    Y0=np.array([[BP[y][0] for y in yl]],complex); Y1=np.array([[BP[y][1] for y in yl]],complex)
    R,J,_,_=track.system(xx[None],np.asarray(c)[None],Y0,Y1,Lc,n,len(yl))
    an=analyse(x[:n+1],x[n+1:],n,prof,c,yl)
    if an is None: return False
    if seedmode:
        pts=[z for y in range(6) for t in (0,1) for z in an[y][t]]
        PP=np.array([[1,0] if z is None else [z,1] for z in pts],complex)
        DD=np.abs(PP[:,None,0]*PP[None,:,1]-PP[:,None,1]*PP[None,:,0])/(np.abs(PP).sum(1)[:,None]*np.abs(PP).sum(1)[None,:]); np.fill_diagonal(DD,9)
        if DD.min()<3e-6: return False
    v=invariant(an)
    for u in INV:
        if np.abs(u-v).max()<1e-6*(1+np.abs(v).max()): return False
    try: an2,res,co,hpo=hp.refine(x[:n+1],x[n+1:],an,n,iters=12)
    except Exception: return False
    moved=max([abs(z1-z2) for y in range(6) for z1,z2 in zip(an[y][0]+an[y][1],an2[y][0]+an2[y][1]) if z1 is not None and z2 is not None]+[0])
    if not (res<1e-28 and moved<1e-6): return False
    an=an2
    if not isnew(an): return False
    aut=autcount(an); found.append((x.copy(),aut,an,c.copy()))
    stack=[(x.copy(),an)]
    while stack:
        xx,aa=stack.pop()
        for x2,an2 in closure.images(xx,aa,n,prof):
            if isnew(an2):
                # crit list in ys order for the image cover
                c2=np.array([z for y in range(6) for z in an2[y][1]])
                found.append((x2,aut,an2,None)); stack.append((x2,an2))
    return True
def weighted(): return sum(1/a for _,a,_,_ in found)
def save(): pickle.dump({'n':n,'prof':prof,'covers':[(x,a) for x,a,_,_ in found],'ans':[an for _,_,an,_ in found]},open(outfn,'wb'))
if os.path.exists(outfn):
    d=pickle.load(open(outfn,'rb'))
    for (x,a),an in zip(d['covers'],d['ans']):
        INV.append(invariant(an)); found.append((x,a,an,None))
    print('resumed',len(found),flush=True)
sfn=f'seeds{n}/'+''.join(map(str,prof))+'.pkl'
if os.path.exists(sfn):
    k0=len(found)
    for x,c in pickle.load(open(sfn,'rb')):
        try: add(x,c)
        except Exception as e: pass
    print('decomposable seeds added',len(found)-k0,flush=True)
# 1. seed with random Newton
for b in range(3 if weighted()<target else 0):
    x,c,res=newton_batch(n,ys,2000,fixed)
    for i in np.nonzero(res<1e-7)[0]: add(x[i],c[i],seedmode=True)
    print(f'newton batch {b}: {len(found)} weighted {weighted()} / {target}  {time.time()-t0:.0f}s',flush=True)
    if abs(weighted()-target)<1e-9: break
# 2. monodromy loops
L=rng2.normal(size=2*(n+1))+1j*rng2.normal(size=2*(n+1))
def to_S(x): p,q=x[:n+1],x[n+1:]; y=np.concatenate([MS[0,0]*p+MS[0,1]*q,MS[1,0]*p+MS[1,1]*q]); return y/(y@L)
def from_S(x): p,q=x[:n+1],x[n+1:]; return np.concatenate([MSi[0,0]*p+MSi[0,1]*q,MSi[1,0]*p+MSi[1,1]*q])
def loop(i,j,steps=240):
    wi,wj=W[i],W[j]; others=[W[k] for k in range(6) if k!=j]
    r=0.4*min(abs(wj-o) for o in others)
    d=(wi-wj)/abs(wi-wj); a=wj+r*d
    seg1=[wi+(a-wi)*t for t in np.linspace(0,1,steps//3)]
    ang=np.angle(d); circ=[wj+r*np.exp(1j*(ang+2*np.pi*t)) for t in np.linspace(0,1,steps//3)]
    seg2=seg1[::-1]
    path=np.array(seg1+circ[1:]+seg2[1:])
    P=np.tile(W,(len(path),1)); P[:,i]=path
    return P
it=0; stall=0
def wordpath(w,steps):
    at=list(range(6))   # at[label]=position index
    segs=[]
    for (u,v) in w:     # swap the labels sitting at positions u and v
        lu=at.index(u); lv=at.index(v)
        m=(W[u]+W[v])/2; r=(W[u]-m); ts=np.linspace(0,1,steps)
        P=np.array([[W[at[l]] for l in range(6)]]*steps)
        P[:,lu]=m+r*np.exp(1j*np.pi*ts); P[:,lv]=m-r*np.exp(1j*np.pi*ts)
        segs.append(P if not segs else P[1:])
        at[lu],at[lv]=v,u
    return np.concatenate(segs),at
def swappath(i,j,steps=240):
    m=(W[i]+W[j])/2; r=(W[i]-m)
    ts=np.linspace(0,1,steps)
    P=np.tile(W,(steps,1)); P[:,i]=m+r*np.exp(1j*np.pi*ts); P[:,j]=m-r*np.exp(1j*np.pi*ts)
    return P
while abs(weighted()-target)>1e-9 and time.time()-t0<maxtime:
    it+=1
    act=[y for y in range(6) if prof[y]>0]
    i,j=rng2.choice(act,2,replace=False)
    pairs=[(u,v) for u in act for v in act if u<v and prof[u]==prof[v]]
    swap = bool(pairs) and rng2.random()<0.3
    if swap: i,j=pairs[rng2.integers(len(pairs))]
    word=None
    if not swap and rng2.random()<0.5:
        # random word of half twists whose total permutation preserves the profile
        for _try in range(1000):
            L_=rng2.integers(2,6); w=[tuple(rng2.choice(6,2,replace=False)) for _ in range(L_)]
            perm=list(range(6))
            for (u,v) in w:
                perm=[v if q==u else u if q==v else q for q in perm]
            _,at=wordpath(w,2)
            if all(prof[at[p]]==prof[p] for p in range(6)) and at!=list(range(6)): word=(w,at); break
    if stall>=3:
        nn=0
        for _r in range(3):
            x,c,res=newton_batch(n,ys,2000,fixed)
            nn+=sum(1 for ii in np.nonzero(res<1e-7)[0] if add(x[ii],c[ii],seedmode=True))
        print(f'  newton refill: new {nn}',flush=True); stall=0
    # only loops of points with crits matter, but any loop is valid
    starts=[(x,c) for x,a,an,c in found if c is not None]
    # solutions from closure have c=None: compute crit list in ys order from an
    starts=[]
    for x,a,an,c in found:
        cc=np.array([z for y in range(6) for z in an[y][1]],complex)
        if any(z is None for y in range(6) for z in an[y][1]): continue
        # need first 3 crits == fixed for the tracker's normalization -> renormalize source
        starts.append((x,cc))
    # source-normalize each start so that its first three crits sit at 'fixed'
    fixedL=(rng2.normal(size=3)+1j*rng2.normal(size=3))*0.6
    X=[];C=[]
    for x,cc in starts:
        a3=[np.array([z,1]) for z in cc[:3]]; b3=[np.array([z,1]) for z in fixedL]
        def frame(p):
            Mt=np.array([p[0],p[1]]).T; lm=np.linalg.solve(Mt,p[2]); return Mt*lm
        T=frame(a3)@np.linalg.inv(frame(b3))   # T(fixed_k)=cc_k ; new cover f∘T
        # compose binary forms: P(T(t))
        p,q=x[:n+1],x[n+1:]
        def comp(poly):
            out=np.zeros(n+1,complex)
            A=np.array([T[0,1],T[0,0]]); B=np.array([T[1,1],T[1,0]])   # low->high linear forms in t
            for m,cm in enumerate(poly):
                term=np.array([1+0j])
                for _ in range(m): term=np.convolve(term,A)
                for _ in range(n-m): term=np.convolve(term,B)
                out[:len(term)]+=cm*term
            return out
        xn=np.concatenate([comp(p),comp(q)])
        Ti=np.linalg.inv(T)
        cn=np.array([(Ti[0,0]*z+Ti[0,1])/(Ti[1,0]*z+Ti[1,1]) for z in cc])
        X.append(to_S(xn)); C.append(cn)
    if not X: stall=6; continue
    X=np.array(X); C=np.array(C)
    if word is not None:
        mk=lambda st: wordpath(word[0],st)[0]
    else:
        mk=(lambda st: swappath(i,j,st)) if swap else (lambda st: loop(i,j,st))
    P=mk(240)
    xs,cs,ok=track.track(X,C,P,None,L,n,ys)
    if (~ok).any():
        bad=np.nonzero(~ok)[0]
        x2,c2,ok2=track.track(X[bad],C[bad],mk(1200),None,L,n,ys)
        xs[bad[ok2]]=x2[ok2]; cs[bad[ok2]]=c2[ok2]; ok[bad[ok2]]=True
    new=0
    for k in np.nonzero(ok)[0]:
        ysl=[ (j if y==i else i if y==j else y) for y in ys] if swap else ([word[1][y] for y in ys] if word is not None else ys)
        if add(from_S(xs[k]),cs[k],ysl): new+=1
    stall=stall+1 if new==0 else 0
    print(f'loop {it} ({i},{j}{" swap" if swap else ""}{" word"+str(word[0]) if word is not None else ""}): tracked {ok.sum()}/{len(X)} new {new} -> {len(found)} weighted {weighted():.2f} / {target}  {time.time()-t0:.0f}s',flush=True)
    save()
save()
print('DONE' if abs(weighted()-target)<1e-9 else 'INCOMPLETE', weighted(), target)
