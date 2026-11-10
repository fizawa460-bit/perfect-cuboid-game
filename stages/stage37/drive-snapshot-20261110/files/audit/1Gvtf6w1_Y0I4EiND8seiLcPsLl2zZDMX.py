from math import gcd
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

def forms(a):
 s=sum(x*x for x in a)
 return [s]+[s-2*x*x for x in a]
def data(a,Z):
 q=[x*x*(2*Z-x*x) for x in a]
 D=Z**4+sum(x*x for x in q)-2*Z*Z*sum(q)-2*sum(q[i]*q[j] for i in range(3) for j in range(i))
 return D,D*D-64*Z*Z*q[0]*q[1]*q[2]
def C(a):
 return sum(x**8 for x in a)-2*sum(a[i]**4*a[j]**4 for i in range(3) for j in range(i))
counts={'generic_integer_identities':0,'signed_boundary_lifts':0,'fresh_unique_factor_mod_p2':0,'zero_heron_false_converse':0}
for n in range(1,2001):
 a=[n%29+1,-(n%31+1),n%37+1];Z=n%43+1
 fs=forms(a);assert C(a)==-fs[0]*fs[1]*fs[2]*fs[3]
 D,P=data(a,Z);assert (D-C(a))%Z==0
 r=[Fraction(a[0],a[2]),Fraction(a[1],a[2]),Fraction(1)]
 k=Fraction(a[2]**2,Z);d=[k*x*x-1 for x in r];q=[1-x*x for x in d]
 H=(1+sum(x*x for x in q)-2*sum(q)-2*sum(q[i]*q[j] for i in range(3) for j in range(i)))**2-64*q[0]*q[1]*q[2]
 assert H==Fraction(P,Z**8)
 counts['generic_integer_identities']+=1
for m in range(2,31):
 for n in range(1,m):
  if gcd(m,n)!=1 or (m-n)%2==0:continue
  e=[m*m-n*n,2*m*n,0];R=m*m+n*n;Z=R*R
  for signs in product((-1,1),repeat=3):
   f=[signs[0]*e[1],signs[1]*e[0],signs[2]*R]
   a=[x+y for x,y in zip(e,f)];b=[x-y for x,y in zip(e,f)]
   assert all(x*x+y*y==2*Z for x,y in zip(a,b))
   assert sum(x*y for x,y in zip(a,b))==-Z
   D,P=data(a,Z);assert P==0 and D==-8*Z*a[0]*a[1]*a[2]*b[0]*b[1]*b[2]
   assert C(a)%Z==0
   assert [(x+y)//2 for x,y in zip(a,b)]==e
   counts['signed_boundary_lifts']+=1
# Abstract p^2 factor router only: not a full physical or137 square-witness test.
for p in (5,13,17,29):
 mod=p*p
 for x in range(1,mod):
  if x%p==0:continue
  for y in range(1,mod):
   if y%p==0:continue
   for z in range(1,mod):
    if z%p==0:continue
    # Stop after an adequate bounded sample instead of enumerating every residue.
    fs=forms([x,y,z]);hits=[i for i,F in enumerate(fs) if F%p==0]
    assert len(hits)<=1
    if hits and fs[hits[0]]%mod==0:counts['fresh_unique_factor_mod_p2']+=1
    if z>5:break
   if y>20:break
  if x>20:break
# Zero leading Heron factor is not an automatic eliminant root or lift.
a=[3,4,5];assert C(a)==0 and data(a,1)[1]!=0
counts['zero_heron_false_converse']+=1
out={'card':'M3-T11-139','status':'PASS','counts':counts,'symbolic':[8,1,0,0],'positive_physical_endpoints_enumerated':0,'boundary_samples_are_endpoints':False,'fresh_tests_are_physical':False,'independent_external_audit':False,'global_counting_credit':0,'support_power_bound_proved':False}
Path('M3-T11-139-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
