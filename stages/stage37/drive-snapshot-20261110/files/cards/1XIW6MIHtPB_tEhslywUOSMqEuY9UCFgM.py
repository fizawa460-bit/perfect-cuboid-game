import math,json,collections
from pathlib import Path
# Arithmetic checks, not an enumeration of positive physical endpoints.
limit=20000
triples=set()
for m in range(2,math.isqrt(limit)+1):
 for n in range(1,m):
  c=m*m+n*n
  if c>limit or math.gcd(m,n)!=1 or (m-n)%2==0: continue
  x,y=sorted((m*m-n*n,2*m*n)); triples.add((x,y,c))
by=collections.defaultdict(set)
for ell,beta,c in triples:
 assert (c-beta)*(c+beta)==ell*ell
 assert 2*c<=ell*ell+1
 by[ell].add((beta,c))
reconstructed=0
for ell,expected in by.items():
 actual=set()
 for d in range(1,ell+1):
  if ell*ell%d:continue
  t=ell*ell//d
  if (d+t)%2:continue
  c=(d+t)//2; beta=(t-d)//2
  if c<=limit and beta>=ell and math.gcd(ell,beta)==1:
   actual.add((beta,c))
 assert actual==expected
 reconstructed+=len(actual)
field_counts={}
for p in (41,73,89):
 roots=collections.defaultdict(list)
 for y in range(1,p):roots[y*y%p].append(y)
 count=0
 for e1 in range(1,p):
  for e2 in range(1,p):
   for e3 in roots[(1-e1*e1-e2*e2)%p]:
    for f1 in roots[(1-e1*e1)%p]:
     for f2 in roots[(1-e2*e2)%p]:
      for f3 in roots[(1-e3*e3)%p]:
       N=(e1*f1+e2*f2+e3*f3)%p
       U=(e1*e2*e3-e1*f2*f3-e2*f1*f3-e3*f1*f2)%p
       V=(f1*e2*e3+f2*e1*e3+f3*e1*e2-f1*f2*f3)%p
       assert (U*U+V*V)%p==1
       assert (N*V-2*e1*e2*e3)%p==0
       count+=1
 field_counts[str(p)]=count
out={'card':'M3-T11-187','status':'PASS','primitive_phase_triples_c_le':limit,'primitive_phase_triples_checked':len(triples),'fixed_short_leg_classes':len(by),'divisor_reconstructions':reconstructed,'finite_field_algebra_checks':field_counts,'finite_field_algebra_total':sum(field_counts.values()),'physical_endpoints_enumerated':0,'scope':'Conic inverse/bound and finite-field identities only; no asymptotic or physical occupancy verification.'}
Path('M3-T11-187-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
