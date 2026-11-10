"""Exact local checks, not global physical endpoints. Python standard library."""
import json
from itertools import product
from fractions import Fraction

def lift_sqrt(a,p,k,seed):
    x=seed; mod=p
    for _ in range(1,k):
        x += ((a-x*x)//mod * pow(2*x,-1,p) % p)*mod
        mod *= p
    assert (x*x-a)%mod==0
    return x

checks=0; same=0; relative=0
for p in (5,13,17,29,41):
  for beta in (1,2):
    k=4*beta; modulus=p**k; R=p**beta
    root=lift_sqrt(-1,p,k,next(x for x in range(1,p) if (x*x+1)%p==0))
    for e1,e2 in product(range(1,min(p,7)),repeat=2):
      a=(R*R-e1*e1-e2*e2)%modulus
      seeds=[x for x in range(1,p) if (x*x-a)%p==0]
      if not seeds: continue
      es=(e1,e2,lift_sqrt(a,p,k,seeds[0]))
      for signs in product((-1,1),repeat=3):
        fs=[lift_sqrt((R*R-e*e)%modulus,p,k,s*root*e%p) for e,s in zip(es,signs)]
        N=sum(e*f for e,f in zip(es,fs))%modulus
        As=[(N-2*e*f)%modulus for e,f in zip(es,fs)]
        if len(set(signs))==1:
          assert (2*N+signs[0]*root*R*R)%modulus==0
          same+=1
        else:
          i=next(i for i in range(3) if signs.count(signs[i])==1)
          assert N%p!=0
          assert (2*As[i]-signs[i]*root*R*R)%modulus==0
          assert As[i]%(p**(2*beta))==0 and As[i]%(p**(2*beta+1))!=0
          assert all(As[j]%p!=0 for j in range(3) if j!=i)
          relative+=1
        assert (sum(As)-N)%modulus==0
        checks+=1

# Exact exponent/ratio cancellation behind the cofactor product identity.
ratio_checks=0
for HQ,HS,tQ,tB,tC,tF,n,b in product((1,3),(1,5),(1,17),(1,7),(1,11),(1,13),(1,-2),(1,19)):
    q=HQ*tQ; R=q*HS*tB*tC*tF
    c=tB*tC*tF*HQ**2*tQ**3; N=q*q*n
    lhs=Fraction(N*R**4*b*b,c*c*tF*tF)
    rhs=n*(HQ*HS**2*tB*tC*b)**2
    assert lhs==rhs
    ratio_checks+=1

result={"status":"PASS","modular_sphere_and_signed_face_states":checks,
        "fresh_relative_trace_allocations":relative,"all_same_control_states":same,
        "exact_cofactor_ratio_checks":ratio_checks,
        "physical_endpoints":0,"independent_audit":"NOT RUN",
        "scope":"Modular sphere+three signed face roots and exact integer ratios; not a global endpoint census or occupancy bound."}
with open('M3-T11-219-verification.json','w') as f: json.dump(result,f,indent=2)
print(json.dumps(result))
