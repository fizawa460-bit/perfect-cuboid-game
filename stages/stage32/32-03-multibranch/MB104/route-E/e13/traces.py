# exact arithmetic in Q_B over Z[sqrt2]; enumerate Gamma_0 = PQ^1(P^2) elements, involutions, traces of products.
import math, itertools, sys
sys.dont_write_bytecode = True
from collections import Counter
R2=math.sqrt(2)
class K:
    __slots__=("x","y")
    def __init__(s,x=0,y=0): s.x=x; s.y=y
    def __add__(s,o): return K(s.x+o.x,s.y+o.y)
    def __sub__(s,o): return K(s.x-o.x,s.y-o.y)
    def __mul__(s,o): return K(s.x*o.x+2*s.y*o.y, s.x*o.y+s.y*o.x)
    def __neg__(s): return K(-s.x,-s.y)
    def key(s): return (s.x,s.y)
    def val(s): return s.x+s.y*R2
    def conj(s): return s.x-s.y*R2
Z=K(); O=K(1); S=K(0,1)
def V(*c):
    c=list(c)+[Z]*(4-len(c)); return tuple(c)
T={(0,0):V(O),(0,1):V(Z,O),(0,2):V(Z,Z,O),(0,3):V(Z,Z,Z,O),(1,0):V(Z,O),(2,0):V(Z,Z,O),(3,0):V(Z,Z,Z,O),
 (1,1):V(-O,O),(1,2):V(Z,Z,Z,O),(1,3):V(Z,Z,-O,O),
 (2,1):V(K(-1,-1),O,O,-O),(2,2):V(-O,Z,O),(2,3):V(-O,O,-S,Z),
 (3,1):V(-O,-S,O,Z),(3,2):V(Z,-O,Z,O),(3,3):V(-O,Z,Z,-S)}
def mul(u,v):
    r=[Z,Z,Z,Z]
    for i in range(4):
        if u[i].x==0 and u[i].y==0: continue
        for j in range(4):
            if v[j].x==0 and v[j].y==0: continue
            k=u[i]*v[j]; t=T[(i,j)]
            for m in range(4): r[m]=r[m]+k*t[m]
    return tuple(r)
def key(u): return tuple(c.key() for c in u)
def neg(u): return tuple(-c for c in u)
def pkey(u):
    k=key(u); k2=key(neg(u)); return min(k,k2)
one=V(O); a=V(Z,O); b=V(Z,Z,O)
B=[one,a,b,V(Z,Z,Z,O)]
assert all(key(mul(mul(x,y),z))==key(mul(x,mul(y,z))) for x in B for y in B for z in B)
def tr(u): return u[0]+u[0]+u[1]+u[2]-S*u[3]
# inverses of alpha, beta: alpha^{-1} = 1 - alpha (alpha^2-alpha+1=0)
ai=V(O,-O); bi=V(O,Z,-O)
assert key(mul(a,ai))==key(one) and key(mul(b,bi))==key(one)
def mod2(u): return tuple((c.x%2,c.y%2) for c in u)
# level>=2 residues: computed from filt.py logic: x-1 in J^2.  Recompute J^2 quickly via import
import importlib.util
import os
spec=importlib.util.spec_from_file_location("filt",os.path.join(os.path.dirname(os.path.abspath(__file__)),"filt.py"))
import io,contextlib
f=io.StringIO()
with contextlib.redirect_stdout(f):
    F=importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
L2=set(F.L2); L3=set(F.L3)
gens=[a,ai,b,bi]
seen={pkey(one):one}; fr=[one]; DEPTH=int(sys.argv[1])
for d in range(DEPTH):
    n=[]
    for x in fr:
        for g in gens:
            y=mul(x,g); k=pkey(y)
            if k not in seen: seen[k]=y; n.append(y)
    fr=n
els=list(seen.values()); print("elements of PQ^1 found:",len(els))
G0=[x for x in els if mod2(x) in L2]
print("in Gamma_0:",len(G0))
bad=0; trs=set()
for x in G0:
    t=tr(x)
    if abs(t.conj())>2+1e-9: bad+=1
    trs.add((abs(t.val())))
print("conjugate trace >2:",bad)
invs=[x for x in G0 if tr(x).x==0 and tr(x).y==0]
print("involutions (elliptic order 2) in Gamma_0 found:",len(invs))
print("their levels mod 2:",Counter(F.lvl(mod2(x)) for x in invs))
# traces of products of two involutions
pt=Counter()
for x,y in itertools.combinations(invs,2):
    t=tr(mul(x,y)); pt[round(abs(t.val()),9)]+=1
vals=sorted(pt)
print("smallest |tr| of products of two involutions:",vals[:14])
hyp=sorted(v for v in trs if v>2+1e-9)
print("smallest hyperbolic |tr| in Gamma_0:",[round(v,6) for v in hyp[:12]])
gaps=sorted({round(hyp[i+1]-hyp[i],9) for i in range(min(len(hyp)-1,400))})
print("smallest gaps between distinct traces (first 400):",gaps[:5])
