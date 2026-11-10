from math import gcd,isqrt
from itertools import product
from collections import Counter
from pathlib import Path
import json

def root(a,p,k):
 mod=p**k;a%=mod
 r=next((v for v in range(1,p) if v*v%p==a%p),None)
 if r is None:return None
 pk=p
 for j in range(1,k):
  r+=(-((r*r-a)//pk)*pow(2*r,-1,p)%p)*pk;pk*=p
 return r%mod
counts=Counter();collisions=Counter()
for p in (5,13,17,29,41,73):
 for lam in (1,2,3):
  k=3*lam+2;mod=p**k;R=p**lam
  for A in range(1,9):
   if A%p==0:continue
   candidates=set(range(1,p))
   for a in range(1,lam+1):
    candidates.update((A+p**a,-A+p**a))
   for F in candidates:
    if F%p==0:continue
    e3=root(R*R-A*A-F*F,p,k)
    if e3 is None:continue
    roots=[root(R*R-e*e,p,k) for e in (A,F,e3)]
    assert all(r is not None for r in roots)
    for a1,a2 in product((1,-1),repeat=2):
     rr=[a1*roots[0]%mod,a2*roots[1]%mod,roots[2]]
     r1,r2,r3=rr;M=r1+r2;Delta=A*A-F*F
     common=gcd(M,R)
     assert gcd(Delta,R)%common==0
     if common>1:
      assert p%8==1
      collisions[str(p)]+=1
     for eps in product((1,-1),repeat=3):
      sig=[eps[i]*rr[i]*pow(e,-1,p)%p for i,e in enumerate((A,F,e3))]
      same=sig[0]==sig[1]==sig[2]
      if same:
       assert gcd(M,R)==gcd(eps[0]*A+eps[1]*F,R)
       counts['all_same_gcd_checks']+=1
      else:counts['relative_cases']+=1
      counts['signed_local_cases']+=1
# Content/face coprimality on exact zero-third-edge boundary points.
boundary=0
for m in range(2,101):
 for j in range(1,m):
  if gcd(m,j)!=1 or (m-j)%2==0:continue
  A=m*m-j*j;F=2*m*j;n=m*m+j*j
  Ny=(n+A)*(n+F)*(A+F)
  assert gcd(Ny,n)==1
  boundary+=1
cube=[]
for Z in (100,1000,5000,25000):
 maxd=int(round(Z**(1/3)))+2
 for D in range(1,maxd+1):
  ds=[d for d in range(D,maxd+1) if d**3<=Z]
  labels=set(c for d in ds for c in range(d**3,Z+1,d**3))
  pairs=sum(Z//(d**3) for d in ds)
  assert len(labels)<=pairs and pairs*D*D<=2*Z
  if D**3>Z:assert len(labels)==0
  cube.append(dict(Z=Z,D=D,distinct_c=len(labels),pair_envelope=pairs))
out=dict(card='M3-T11-193',status='PASS',signed_padic_local_tests=dict(counts),ordinate_R_collision_cases_by_prime=dict(collisions),zero_edge_boundary_content_coprimality_checks=boundary,cubic_divisor_envelope_cells=len(cube),physical_endpoints_enumerated=0,independent_audit='NOT_RUN',scope='Synthetic local square lifts and zero-edge boundaries, plus exact integer divisor enumeration. No positive rational endpoint or global occupied support count is inferred.')
Path('M3-T11-193-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
