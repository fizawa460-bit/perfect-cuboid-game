"""(H) pairs built as quotients of cyclic 2^k-isogenies onto E': y^2 = x(x+1)(x+i).  double precision, tol 1e-8."""
import numpy as np, itertools, cmath, sys, time
from collections import Counter
def k1(x): return 1j/x
def k2(x): return (-x-1j)/(x+1)
def chain(steps, choice):
    """returns list of (shift_out, a, b, shift_in): X = (x-sin) + a + b/(x-sin) + sout ; built downward-list from top."""
    roots=[0,-1,-1j]; ker=0   # dual-kernel point on current curve (start: T'=(0,0) on E')
    maps=[]
    for st in range(steps):
        others=[r-ker for r in roots if abs(r-ker)>1e-12]
        a=(others[0]+others[1])/2; b=((others[0]-others[1])/4)**2
        # domain curve y^2 = x(x^2+a x+b); map X = x + a + b/x, then add ker to return to current coords
        maps.append((ker,a,b))
        disc=cmath.sqrt(a*a-4*b); rp=(-a+disc)/2; rm=(-a-disc)/2
        roots=[0,rp,rm]; ker=[rp,rm][choice[st] if st<len(choice) else 0]   # next dual kernel: not (0,0)
    return maps, roots
def pre(maps, vals):
    pts=list(vals)
    for ker,a,b in maps:
        new=[]
        for X in pts:
            c=X-ker-a   # x + b/x = c
            d=cmath.sqrt(c*c-4*b); new+=[(c+d)/2,(c-d)/2]
        pts=new
    return pts
def search(O1,O2,L1,L2,tol=1e-8):
    O1=np.array(O1);O2=np.array(O2); n1,n2=len(O1),len(O2)
    def m(z):
        z1,z2,z3=z; return np.array([[z2-z3,-z1*(z2-z3)],[z2-z1,-z3*(z2-z1)]])
    den2=np.sqrt(1+abs(O2)**2)
    def mind(P):
        d=np.abs(P[:,None]-P[None,:])/np.sqrt((1+abs(P[:,None])**2)*(1+abs(P[None,:])**2)); d[np.diag_indices(len(P))]=9
        return d.min()
    print('  smallest chordal distance inside O1, O2: %.2e %.2e'%(mind(O1),mind(O2)))
    uniq={}
    inv=[ (img,np.linalg.inv(m(O2[list(img)]))) for img in itertools.permutations(range(n2),3)]
    for tri in itertools.combinations(range(n1),3):
        mz=m(O1[list(tri)])
        for img,mi in inv:
            M=mi@mz
            if abs(np.linalg.det(M))<1e-7*(abs(M)**2).sum(): continue   # degenerate map
            w=(M[0,0]*O1+M[0,1])/(M[1,0]*O1+M[1,1])
            d=np.abs(w[:,None]-O2[None,:])/(np.sqrt(1+abs(w[:,None])**2)*den2[None,:])
            hit=np.argwhere(d<tol)
            if len(hit)>=4 and len(set(hit[:,0]))==len(hit)==len(set(hit[:,1])): uniq[tuple(sorted(map(tuple,hit)))]=1
    res=Counter()
    for key in uniq:
        j=sum(L1[a]==L2[b] for a,b in key); res[(len(key),j,len(key)-j)]+=1
    return dict(sorted(res.items()))
steps=int(sys.argv[1]); choice=[int(c) for c in (sys.argv[2] if len(sys.argv)>2 else '')]
maps,top=chain(steps,choice)
U=[t for t in top]   # finite 2-torsion x-values of E1; infinity omitted -> move by a Moebius below
c1,c2=k2(1),k2(1j)
A=pre(maps,[1]); Bp=pre(maps,[1j]); C1=pre(maps,[c1]); C2=pre(maps,[c2])
# coordinates: send the 2-torsion x-values U[0], U[1], infinity to -1, 1, 0 (spreads the points)
u0,u1=U[0],U[1]
mv=lambda z: (u1-u0)/(2*z-u0-u1)
Uall=[mv(t) for t in U]+[0j]      # last entry: image of infinity
# labels of U under p_s: Phi(U) = {O, T'} -> x = inf, 0 ; p_O = Phi: labels e,e ; p_{t2} = k2 o Phi: k2(inf)=-1 (b), k2(0)=-i (a)
# which U points go to inf / 0 under Phi: evaluate
def Phi(t):
    x=t
    for ker,a,b in reversed(maps):
        x=(x)+a+b/x+ker if abs(x)>1e-14 else np.inf
        if x==np.inf: return np.inf
    return x
def lab(v):
    if v==np.inf or abs(v)>1e8 or abs(v)<1e-8: return 'e'
    if abs(v-1)<1e-7 or abs(v+1)<1e-7: return 'b'
    if abs(v-1j)<1e-7 or abs(v+1j)<1e-7: return 'a'
    return '?'
PhU=[Phi(t) for t in U]+[np.inf]
LU0=[lab(v) for v in PhU]
LU2=[lab(k2(v)) if v!=np.inf and abs(v)>1e-8 else ('b' if v==np.inf or abs(v)>1e8 else 'a') for v in PhU]
n=2**steps
O_O=[mv(t) for t in A+Bp]+Uall; L_O=['b']*n+['a']*n+LU0          # p_O = Phi
O_2=[mv(t) for t in C1+C2]+Uall; L_2=['b']*n+['a']*n+LU2         # p_{t2} = k2 o Phi
print('degree',n,'|O|',len(O_O),'labels U:',LU0,LU2)
t0=time.time()
print(' (H) pair  p_O vs k2.p_O : (c,j,h) ->',search(O_2,O_O,L_2,L_O))
print(' time %.0fs'%(time.time()-t0))
