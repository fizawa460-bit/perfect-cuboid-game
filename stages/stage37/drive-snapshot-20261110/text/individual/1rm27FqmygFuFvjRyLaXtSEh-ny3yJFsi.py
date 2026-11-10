import random, json
from collections import Counter
from pathlib import Path

def root_unit(a,p,n):
    roots=[r for r in range(1,p) if r*r%p==a%p]
    if not roots:return None
    r=roots[0];mod=p
    for _ in range(1,n):
        digit=((a-r*r)//mod)*pow(2*r,-1,p)%p
        r+=digit*mod;mod*=p
    assert (r*r-a)%mod==0
    return r

def val(a,p):
    if a==0:return 10000
    n=0
    while a%p==0:a//=p;n+=1
    return n

rng=random.Random(185)
counts=Counter();total=0
for p in (13,17,29,37):
 for lam in (1,2,3):
  n=6*lam+3;mod=p**n;R=p**lam;accepted=0
  for attempt in range(20000):
   e=[rng.randrange(1,mod),rng.randrange(1,mod)]
   if any(a%p==0 for a in e):continue
   third=root_unit((R*R-e[0]**2-e[1]**2)%mod,p,n)
   if third is None:continue
   e.append(third)
   f=[root_unit((R*R-a*a)%mod,p,n) for a in e]
   assert all(a is not None for a in f)
   for mask in range(8):
    ff=[(-a if mask>>i&1 else a)%mod for i,a in enumerate(f)]
    Tnum=sum(a*b for a,b in zip(e,ff))%mod
    Ynum=(ff[0]*e[1]*e[2]+ff[1]*e[0]*e[2]+ff[2]*e[0]*e[1]-ff[0]*ff[1]*ff[2])%mod
    assert (Tnum*Ynum-2*e[0]*e[1]*e[2]*R*R)%mod==0
    ty,yy=val(Tnum,p),val(Ynum,p)
    assert (ty,yy) in ((2*lam,0),(0,2*lam))
    cdepth=3*lam-yy;tdepth=max(0,2*lam-ty)
    assert (cdepth,tdepth) in ((3*lam,0),(lam,2*lam))
    assert cdepth+tdepth==3*lam
    counts[f'p={p},lambda={lam},c={cdepth},t={tdepth}']+=1;total+=1
   accepted+=1
   if accepted==80:break
  assert accepted==80

result={'status':'PASS','seed':185,'local_unit_content_prime_power_cases':total,'counts':dict(counts),'scope':'synthetic p-adic sphere/space-triangle witnesses; not positive rational physical endpoints','physical_endpoints_enumerated':0,'claims_verified':['Tnum*Ynum=2e1e2e3R^2 modulo p^N','fresh product-phase vs S denominator depth (3lambda,0) or (lambda,2lambda)','fresh depth(c)+depth(t)=3lambda'],'independent_hostile_audit':'NOT_RUN'}
Path('M3-T11-185-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','cases':total,'strata':len(counts)}))
