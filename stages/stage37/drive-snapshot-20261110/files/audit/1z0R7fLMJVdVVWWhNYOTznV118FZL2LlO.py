"""Exact replay of gluing and squarefree CRT equivalence, not asymptotic counting."""
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json

def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def conj(z): return z[0],-z[1]
def norm(z): return z[0]**2+z[1]**2
def div(z,w):
    a=mul(z,conj(w)); n=norm(w)
    return (a[0]//n,a[1]//n) if a[0]%n==a[1]%n==0 else None
def circle(R):
    out=set()
    for a in range(-R,R+1):
        b=isqrt(R*R-a*a)
        if a*a+b*b==R*R: out.update([(a,b),(a,-b)])
    return out
def pi(p):
    return next((a,isqrt(p-a*a)) for a in range(1,isqrt(p)+1) if a*a+isqrt(p-a*a)**2==p)

glue=[]
for p,q in [(5,13),(5,17),(13,17)]:
    P=mul(conj(pi(p)),conj(pi(p))); Q=mul(conj(pi(q)),conj(pi(q)))
    for h in [1,29]:
        A=circle(q*h); D=circle(p*h)
        pairs=[(g,k) for g,k in product(A,D) if mul(P,g)==mul(Q,k) or mul(P,g)==conj(mul(Q,k))]
        predicted=set()
        for K in circle(h):
            predicted.add((mul(Q,K),mul(P,K)))
            predicted.add((mul(conj(Q),K),mul(conj(P),conj(K))))
        assert set(pairs)==predicted and len(pairs)==2*len(circle(h))
        pos=[x for x in pairs if mul(P,x[0])[0]>0]
        assert len(pos)==len(circle(h))
        glue.append({'p':p,'q':q,'h':h,'signed_pairs':len(pairs),'positive_pairs':len(pos)})

checks=0; branches={'r2':0,'r3':0}; examples=[]
for R,ps in [(5,[5]),(13,[13]),(65,[5,13]),(85,[5,17]),(221,[13,17]),(1105,[5,13,17])]:
    H=sorted(z for z in circle(R) if z[0]>0 and z[1]>0)
    for hs in product(H,repeat=3):
        es=[z[0] for z in hs]
        if gcd(gcd(es[0],es[1]),es[2])!=1 or sum(e%2 for e in es)!=1: continue
        S=sum(e*e for e in es); F=4*(S-R*R)
        all_local=True
        for p in ps:
            P=mul(conj(pi(p)),conj(pi(p)))
            I=[i for i,e in enumerate(es) if e%p]
            oriented=[]
            for i in I:
                z=hs[i]; G=div(z,P)
                if G is None: G=div(conj(z),P)
                assert G is not None and norm(G)==(R//p)**2
                oriented.append(G)
            C=(sum(mul(g,g)[0] for g in oriented),sum(mul(g,g)[1] for g in oriented))
            local=div(C,mul(pi(p),pi(p))) is not None
            assert local==(F%(p*p)==0)
            if len(I) in [2,3]: branches['r'+str(len(I))]+=1
            all_local &= local
        assert all_local==(S==R*R)
        checks+=1
    examples.append({'R':R,'positive_circle_points':len(H)})
out={'status':'PASS','gluing_cases':glue,'squarefree_triple_checks':checks,'witness_branch_checks':branches,'circle_domains':examples,'scope':'finite replay supplements uniform proofs; no asymptotic saving or universal cuboid nonexistence inferred','GLOBAL_COUNTING_CREDIT':0}
Path(__file__).with_name('verification155.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
