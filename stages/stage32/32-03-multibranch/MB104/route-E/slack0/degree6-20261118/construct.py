"""Explicit decomposable slack-0 covers of degree 6: h∘g with (deg g, deg h) = (2,3) or (3,2)."""
import numpy as np, itertools, pickle, os, sys
from common import *
from covers import analyse, polish
def comp(hP,hQ,gP,gQ):
    """homogeneous composition: h(g) where h=(hP,hQ) degree d2 forms (low->high in t0, i.e. coeff m of t0^m t1^(d2-m)), g forms degree d1."""
    d2=len(hP)-1
    outP=0; outQ=0
    for m in range(d2+1):
        term=np.array([1+0j])
        for _ in range(m): term=np.convolve(term,gP)
        for _ in range(d2-m): term=np.convolve(term,gQ)
        outP=outP+hP[m]*term; outQ=outQ+hQ[m]*term
    return outP,outQ
def mob_forms(M):  # Mobius M as degree-1 forms (low->high): P=M00 t + M01 -> [M01,M00]
    return np.array([M[0,1],M[0,0]],complex),np.array([M[1,1],M[1,0]],complex)
def mob_compose_left(M,P,Q): return M[0,0]*P+M[0,1]*Q, M[1,0]*P+M[1,1]*Q
def mob_send(a,b,c):
    """Mobius sending 0->a, inf->b, 1->c (homog points)"""
    a=np.array(a,complex); b=np.array(b,complex); c=np.array(c,complex)
    A=np.array([[b[0],a[0]],[b[1],a[1]]]); lm=np.linalg.solve(A,c)
    return np.array([[b[0]*lm[0],a[0]*lm[1]],[b[1]*lm[0],a[1]*lm[1]]])
def cubics(br):
    """all cubic covers with simple branch values br (4 homog points): list of (P,Q) forms degree 3"""
    out=[]
    N=np.linalg.inv(mob_send(br[0],br[1],br[2]))     # N(br0)=0, N(br1)=inf, N(br2)=1
    w=N@np.array(br[3],complex); z=w[0]/w[1]
    # H_z(k) = k(3k-2)^3 - z(2k-1) = 27k^4 -54k^3+36k^2-8k - 2zk + z
    ks=np.roots([27,-54,36,-8-2*z,z])
    Ni=np.linalg.inv(N)
    for k in ks:
        # F_k = t^2((2k-1)t + 2-3k)/(t-k): P=[0,0,2-3k,2k-1], Q=[-k,1,0,0]
        P=np.array([0,0,2-3*k,2*k-1],complex); Q=np.array([-k,1,0,0],complex)
        out.append(mob_compose_left(Ni,P,Q))
    return out
def preimages(P,Q,y):
    f=(y[1]*P-y[0]*Q)[::-1]; f=np.trim_zeros(np.where(np.abs(f)<1e-12*np.abs(f).max(),0,f),'f')
    r=list(np.roots(f)); n=len(P)-1
    return r+[None]*(n-(len(f)-1))
def crit_points(P,Q):
    n=len(P)-1
    W=np.polysub(np.polymul(np.polyder(P[::-1]),Q[::-1]),np.polymul(P[::-1],np.polyder(Q[::-1])))
    W=np.trim_zeros(np.where(np.abs(W)<1e-11*np.abs(W).max(),0,W),'f')
    cr=[complex(polish(W,c)) for c in np.roots(W)]
    return cr+[None]*(2*n-2-len(cr))
def value_index(P,Q,z):
    n=len(P)-1
    v=(np.polyval(P[::-1],z),np.polyval(Q[::-1],z)) if z is not None else (P[n],Q[n])
    d=[abs(v[0]*BP[y][1]-v[1]*BP[y][0])/(abs(v[0])+abs(v[1])) for y in range(6)]
    k=int(np.argmin(d)); return k if d[k]<1e-6 else None
RT=np.array([[1.1+0.3j,0.27-0.4j],[0.35+0.2j,0.9-0.15j]])
TP,TQ=mob_forms(RT)
def cover_record(P,Q):
    P,Q=comp(P,Q,TP,TQ)
    n=len(P)-1; cr=crit_points(P,Q)
    if any(c is None for c in cr): return None
    ysl=[value_index(P,Q,c) for c in cr]
    if any(y is None for y in ysl): return None
    prof=tuple(ysl.count(y) for y in range(6))
    order=sorted(range(len(cr)),key=lambda k:ysl[k])
    c=np.array([cr[k] for k in order]); ys=[ysl[k] for k in order]
    an=analyse(P,Q,n,prof,c,ys)
    if an is None: return None
    return prof,np.concatenate([P,Q]),c
recs=[]
# deg-3 slack-0 covers h (60): build from all 4-subsets of B as branch values
H3=[]
for S in itertools.combinations(range(6),4):
    for P,Q in cubics([BP[s] for s in S]): H3.append((P,Q))
print('cubics',len(H3))
# (A) f = h∘g, g = M(t^2) with M(0)=v1, M(inf)=v2, v1,v2 odd points of h
for hP,hQ in H3:
    odd=[]; cr=crit_points(hP,hQ)
    for y in range(6):
        for z in set(preimages(hP,hQ,BP[y])) if False else preimages(hP,hQ,BP[y]):
            if z is None:
                if None not in cr: odd.append((1,0))
                continue
            if min([abs(z-c) for c in cr if c is not None]+[9])>1e-4*(1+abs(z)): odd.append((z,1))
    assert len(odd)==10,len(odd)
    for v1,v2 in itertools.combinations(odd,2):
        M=np.array([[v2[0],v1[0]],[v2[1],v1[1]]],complex)
        gP=np.array([M[0,1],0,M[0,0]]); gQ=np.array([M[1,1],0,M[1,0]])
        P,Q=comp(hP,hQ,gP,gQ); r=cover_record(P,Q)
        if r: recs.append(('A',)+r)
print('A',len(recs))
# (B) f = h∘g, h degree 2 (15), g cubic with branch values a 4-subset of S = h^-1(B) minus crit points
nA=len(recs)
for y1,y2 in itertools.combinations(range(6),2):
    M=np.array([[BP[y2][0],BP[y1][0]],[BP[y2][1],BP[y1][1]]],complex)
    hP=np.array([M[0,1],0,M[0,0]]); hQ=np.array([M[1,1],0,M[1,0]])
    S=[]
    for y in range(6):
        if y in (y1,y2): continue
        w=np.linalg.solve(M,np.array(BP[y],complex)); s=np.sqrt(w[0]/w[1]); S+= [(s,1),(-s,1)]
    assert len(S)==8
    # crit points 0, inf map to y1,y2 ; h^-1(y1)={0} only -> S has 8 points (not 10)
    for br in itertools.combinations(S,4):
        for gP,gQ in cubics(list(br)):
            P,Q=comp(hP,hQ,gP,gQ); r=cover_record(P,Q)
            if r: recs.append(('B',)+r)
print('B',len(recs)-nA)
pickle.dump(recs,open('decomp6.pkl','wb'))
from collections import Counter
print(Counter(r[1] for r in recs).most_common(5))
