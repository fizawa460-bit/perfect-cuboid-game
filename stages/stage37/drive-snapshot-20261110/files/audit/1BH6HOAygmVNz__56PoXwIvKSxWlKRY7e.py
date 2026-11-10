from itertools import product,combinations
from math import gcd,prod
from pathlib import Path
import json
def forms(a):
 s=sum(x*x for x in a);return [s]+[s-2*x*x for x in a]
def fac(n):
 out=[];p=3
 while p*p<=n:
  if n%p==0:
   k=0
   while n%p==0:n//=p;k+=1
   out.append((p,k))
  p+=2
 if n>1:out.append((n,1))
 return out
def vp(n,p):
 k=0
 while n%p==0:n//=p;k+=1
 return k
counts={'primitive_triple_gcd':0,'abstract_divisor_cover':0,'content_supported_cases':0,'content_with_tau_cases':0,'signed_boundary_adapter':0}
def check(a,R):
 f=forms(a);assert all(f) and prod(f)%(R*R)==0
 h=[gcd(abs(x),R) for x in a]
 assert all(gcd(h[i],h[j])==1 for i in range(3) for j in range(i))
 H=prod(h);assert R%H==0
 for i in range(3):
  j,k=[x for x in range(3) if x!=i]
  assert h[i]**2%gcd(gcd(abs(f[0]),abs(f[i+1])),R*R)==0
  assert h[i]**2%gcd(gcd(abs(f[j+1]),abs(f[k+1])),R*R)==0
 ns=[1]*4
 for p,l in fac(R):
  kap=max(vp(x,p) for x in h)
  if l==kap:continue
  depths=[vp(x,p) for x in f]
  selected=max(range(4),key=lambda j:(depths[j],-j))
  assert depths[selected]>=2*(l-kap)
  ns[selected]*=p**(l-kap)
 assert prod(ns)==R//H and all(f[j]%(ns[j]**2)==0 for j in range(4))
 assert all(gcd(ns[i],ns[j])==1 for i in range(4) for j in range(i))
 return H,R//H
for a in product(range(1,32,2),repeat=3):
 if gcd(gcd(*a[:2]),a[2])!=1:continue
 f=forms(a)
 for inds in combinations(range(4),3):assert gcd(gcd(abs(f[inds[0]]),abs(f[inds[1]])),abs(f[inds[2]]))==1
 counts['primitive_triple_gcd']+=1
 C=prod(f)
 for R in range(3,100,2):
  if C%(R*R):continue
  H,t=check(a,R);counts['abstract_divisor_cover']+=1
  counts['content_supported_cases']+=H>1
  counts['content_with_tau_cases']+=H>1 and t>1
for m in range(2,31):
 for n in range(1,m):
  if gcd(m,n)!=1 or (m-n)%2==0:continue
  e=[m*m-n*n,2*m*n,0];R=m*m+n*n
  for signs in product((-1,1),repeat=3):
   f=[signs[0]*e[1],signs[1]*e[0],signs[2]*R]
   a=[x+y for x,y in zip(e,f)];check(a,R)
   counts['signed_boundary_adapter']+=1
assert counts['content_with_tau_cases']>0
out={'card':'M3-T11-141','status':'PASS','counts':counts,'abstract_samples_are_endpoints':False,'boundary_samples_are_endpoints':False,'positive_physical_endpoints_enumerated':0,'external_audit':False,'global_counting_credit':0,'support_power_bound_proved':False}
Path('M3-T11-141-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
