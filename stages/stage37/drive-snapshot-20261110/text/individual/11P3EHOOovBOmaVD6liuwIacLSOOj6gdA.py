import random,json
from collections import Counter
from pathlib import Path

def val(a,p):
 if a==0:return 100000
 k=0
 while a%p==0:a//=p;k+=1
 return k
def sqrt_unit(a,p,n):
 roots=[r for r in range(1,p) if r*r%p==a%p]
 if not roots:return None
 r=roots[0];m=p
 for _ in range(1,n):
  r+=(((a-r*r)//m)*pow(2*r,-1,p)%p)*m;m*=p
 assert (r*r-a)%m==0
 return r
def sqrt_any(a,p,n):
 v=val(a,p)
 if v>=n:return None
 if v%2:return None
 r=sqrt_unit(a//p**v,p,n-v)
 return None if r is None else p**(v//2)*r

rng=random.Random(186);counts=Counter();deficits=Counter();cases=0
for p in (5,13,17,29):
 for lam in (1,2,3):
  n=12*lam+12;mod=p**n;R=p**lam
  for nu in range(1,3*lam+3):
   kap=min(nu,lam)
   for _ in range(12):
    e1=rng.randrange(1,mod)
    while e1%p==0:e1=rng.randrange(1,mod)
    unit=rng.randrange(1,mod//p**nu)
    while unit%p==0:unit=rng.randrange(1,mod//p**nu)
    if nu==lam:
     q=p*unit;smallmod=p**(n-lam)
     x=((1-q*q)*pow(1+q*q,-1,smallmod))%smallmod
     e3=p**lam*x
    else:e3=p**nu*unit
    e2=sqrt_any((R*R-e1*e1-e3*e3)%mod,p,n)
    assert e2 is not None and e2%p
    ee=(e1,e2,e3)
    fs=[sqrt_any((R*R-e*e)%mod,p,n) for e in ee]
    assert all(f is not None for f in fs)
    for mask in range(8):
     ff=[(-f if mask>>i&1 else f)%mod for i,f in enumerate(fs)]
     tn=sum(e*f for e,f in zip(ee,ff))%mod
     yn=(ff[0]*e2*e3+ff[1]*e1*e3+ff[2]*e1*e2-ff[0]*ff[1]*ff[2])%mod
     assert (tn*yn-2*e1*e2*e3*R*R)%mod==0
     vt,vy=val(tn,p),val(yn,p)
     assert vt<n and vy<n
     cd=max(0,3*lam-vy);td=max(0,2*lam-vt)
     deficit=3*lam-kap-cd-td
     assert deficit==0
     assert td%2==0
     assert cd-(lam-kap)==2*lam-td>=0
     if kap<lam:
      assert (cd,td) in ((3*lam-kap,0),(lam+kap,2*(lam-kap)),(lam-kap,2*lam))
      assert deficit==0
     else:
      assert cd in (0,2*lam)
      assert (cd,td) in ((2*lam,0),(0,2*lam))
     counts[f'p={p},lambda={lam},kappa={kap},nu={nu},c={cd},t={td}']+=1
     deficits[str(deficit)]+=1;cases+=1
out={'status':'PASS','seed':186,'synthetic_content_prime_power_cases':cases,'strata':len(counts),'deficit_distribution':dict(deficits),'claims':['partial-content exact 3-case denominator table','saturated content exact (c,t)=(2lambda,0) or (0,2lambda)','depth(c)+depth(t)=3lambda-kappa in every case','all S denominator depths even'],'scope':'p-adic six-square/sphere witnesses, not positive rational physical endpoints','physical_endpoints_enumerated':0,'independent_hostile_audit':'NOT_RUN'}
Path('M3-T11-186-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
