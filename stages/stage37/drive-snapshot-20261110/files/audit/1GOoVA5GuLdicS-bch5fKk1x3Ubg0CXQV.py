from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def scale(a,k):return [x*k for x in a]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def ev(a,k):return sum(x*k**i for i,x in enumerate(a))
def poly(r):
 q=[[F(0),2*x*x,-x**4] for x in r]
 z=[F(1)]
 for a in q:z=add(z,add(mul(a,a),scale(a,-2)))
 for i in range(3):
  for j in range(i):z=add(z,scale(mul(q[i],q[j]),-2))
 return add(mul(z,z),scale(mul(mul(q[0],q[1]),q[2]),-64))
def symmetric(r,k):
 d=[k*x*x-1 for x in r];s=sum(d);v=[s-2*x for x in d]
 e=sum(v[i]*v[j] for i in range(3) for j in range(i));p=v[0]*v[1]*v[2]
 return (s*e+p)**2-s*s*p*(4*s-p)
counts={'generic_polynomials':0,'global_ratio_identities':0,'boundary_height_and_primitive':0}
for n in range(1,1001):
 r=[F(n%31+1,n%17+1),F(n%23+1,n%19+1),F(1)]
 p=poly(r);assert len(p)<=9 and p[0]==1
 k=F(n%13+1,n%11+1)
 assert ev(p,k)==symmetric(r,k)
 counts['generic_polynomials']+=1
 t=[r[1],1/r[0],r[0]/r[1]];assert t[0]*t[1]*t[2]==1
 z=[x+1/x for x in t];f=[x*x/4 for x in z]
 assert sum(x*x for x in z)-z[0]*z[1]*z[2]==4
 assert (sum(f)-1)**2==4*f[0]*f[1]*f[2]
 assert all(x>=1 for x in f)
 counts['global_ratio_identities']+=1
for m in range(2,31):
 for n in range(1,m):
  if gcd(m,n)!=1 or (m-n)%2==0:continue
  e=[m*m-n*n,2*m*n,0];R=m*m+n*n
  for mask in range(8):
   f=[e[1],e[0],R];f=[(-x if mask&(1<<i) else x) for i,x in enumerate(f)]
   a=[x+y for x,y in zip(e,f)]
   assert gcd(gcd(abs(a[0]),abs(a[1])),abs(a[2]))==1
   h=[gcd(R,x) for x in e]
   assert all(gcd(abs(a[i]),R)==h[i] for i in range(3))
   H=max(map(abs,a));assert 25*H*H>=R*R and H*H<=2*R*R
   t=[F(a[1],a[2]),F(a[2],a[0]),F(a[0],a[1])]
   assert all(max(abs(x.numerator),x.denominator)<=H for x in t)
   r=[F(a[0],a[2]),F(a[1],a[2]),F(1)]
   assert ev(poly(r),F(a[2]*a[2],R*R))==0
   counts['boundary_height_and_primitive']+=1
out={'card':'M3-T11-138','status':'PASS','counts':counts,'symbolic':[8,1,0,0],
 'positive_physical_endpoints_enumerated':0,'boundary_samples_are_endpoints':False,
 'global_counting_credit':0,'independent_external_audit':False,
 'realized_support_power_bound_proved':False}
Path('M3-T11-138-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
