from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

def add(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))
def scale(a,c): return tuple(c*x for x in a)
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return tuple(out)
def eq(a,b): return all(x==0 for x in add(a,scale(b,-1)))
R=(F(1),F(0),F(1)); U=(F(-1),F(0),F(1)); V=(F(0),F(2),F(0))
phases={(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))}
for a,b in [(F(3,5),F(4,5)),(F(4,5),F(3,5))]:
    for x,y in product([-1,1],repeat=2): phases.add((x*a,y*b))
coords=[]
for a,b in sorted(phases):
    assert a*a+b*b==1
    coords.append(('fixed',scale(R,a),scale(R,b),a,b))
    coords.append(('rotating',add(scale(U,a),scale(V,-b)),add(scale(U,b),scale(V,a)),a,b))
for _,e,f,_,_ in coords: assert eq(add(mul(e,e),mul(f,f)),mul(R,R))
counts={str(i):0 for i in range(4)}; examined=0
for triple in product(coords,repeat=3):
    examined+=1
    sq=(F(0),)
    for _,e,_,_,_ in triple: sq=add(sq,mul(e,e))
    if not eq(sq,mul(R,R)): continue
    m=sum(c[0]=='rotating' for c in triple); counts[str(m)]+=1
    assert m in [0,2]
    if m==2:
        fixed=[c for c in triple if c[0]=='fixed'][0]
        assert all(x==0 for x in fixed[1])
        rotating=[c for c in triple if c[0]=='rotating']
        assert sum((c[3]**2-c[4]**2 for c in rotating),F(0))==0
        assert sum((2*c[3]*c[4] for c in rotating),F(0))==0
E=[U,V,(F(0),F(0),F(0))]; G=[V,scale(U,-1),R]
assert eq(add(add(mul(E[0],E[0]),mul(E[1],E[1])),mul(E[2],E[2])),mul(R,R))
A=[add(e,f) for e,f in zip(E,G)]; Y=[add(e,scale(f,-1)) for e,f in zip(E,G)]
for a,y in zip(A,Y): assert eq(add(mul(a,a),mul(y,y)),scale(mul(R,R),2))
assert eq(sum_poly:=add(add(mul(A[0],Y[0]),mul(A[1],Y[1])),mul(A[2],Y[2])),scale(mul(R,R),-1))
odd_checks=0
for d in [1,3,5,7]:
    for s,t in product(range(-3,4),repeat=2):
        p=sum(F(k+1)*s**k*t**(d-k) for k in range(d+1))
        n=sum(F(k+1)*(-s)**k*(-t)**(d-k) for k in range(d+1))
        assert n==-p; odd_checks+=1
out={'coordinate_phase_count':len(phases),'individual_circle_checks':len(coords),'triples_examined':examined,'sphere_identities_by_rotating_count':counts,'odd_antipodal_checks':odd_checks,'boundary_plus_lift_verified':True,'positive_nonconstant_degree2_examples':0,'proof_method':'factor allocation and Laurent coefficients; finite enumeration is supporting verification only','global_counting_credit':0}
Path(__file__).with_name('verification147.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
