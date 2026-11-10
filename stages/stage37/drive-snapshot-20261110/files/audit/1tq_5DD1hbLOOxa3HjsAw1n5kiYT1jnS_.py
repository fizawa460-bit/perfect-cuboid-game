from math import gcd
from itertools import product
from pathlib import Path
import json
def forms(a):
 s=sum(x*x for x in a);return [s]+[s-2*x*x for x in a]
def surface(v):
 S=sum(v);E=sum(v[i]*v[j] for i in range(3) for j in range(i));P=v[0]*v[1]*v[2]
 return (S*E+P)**2-S*S*P*(4*S-P)
counts={'odd_plus_parity':0,'unit_unique_prime_factor':0,'signed_boundary_scope':0,'boundary_saturation_counterexamples':0,'zero_root_surface':0}
for a in product(range(-19,20,2),repeat=3):
 f=forms(a);assert [x%8 for x in f]==[3,1,1,1] and all(f)
 counts['odd_plus_parity']+=1
for p in (3,5,7,13,17,29):
 for a in product(range(1,min(p,12)),repeat=3):
  f=forms(a);assert sum(x%p==0 for x in f)<=1
  counts['unit_unique_prime_factor']+=1
for a in range(-20,21):
 for b in range(-20,21):
  assert surface([0,a,b])==((a+b)*a*b)**2
  assert surface([a,b,-a-b])==(a*b*(-a-b))**2
  counts['zero_root_surface']+=1
for m in range(2,31):
 for n in range(1,m):
  if gcd(m,n)!=1 or (m-n)%2==0:continue
  e=[m*m-n*n,2*m*n,0];R=m*m+n*n
  for signs in product((-1,1),repeat=3):
   f=[signs[0]*e[1],signs[1]*e[0],signs[2]*R]
   a=[x+y for x,y in zip(e,f)];F=forms(a)
   assert [x%8 for x in F]==[3,1,1,1]
   counts['signed_boundary_scope']+=1
   counts['boundary_saturation_counterexamples']+=any(x%(R*R)==0 for x in F)
assert counts['boundary_saturation_counterexamples']>0
assert [k for k in range(0,6) if k%8==3]==[3]
assert [k for k in range(-2,5) if k%8==1]==[1]
out={'card':'M3-T11-140','status':'PASS','counts':counts,'positive_physical_endpoints_enumerated':0,'boundary_samples_are_endpoints':False,'external_audit':False,'global_counting_credit':0,'support_power_bound_proved':False}
Path('M3-T11-140-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
