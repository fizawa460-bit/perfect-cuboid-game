from fractions import Fraction as F
from math import gcd,isqrt,lcm
from collections import defaultdict
from pathlib import Path
import json

def add(P,Q,n):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and y==-v:return None
 m=(3*x*x-n*n)/(2*y) if P==Q else (v-y)/(u-x)
 z=m*m-x-u;return z,-y+m*(x-z)
def neg(P):return None if P is None else (P[0],-P[1])
def mul(k,P,n):
 Q=None
 while k:
  if k&1:Q=add(Q,P,n)
  P=add(P,P,n);k//=2
 return Q
def root(q):
 assert q>=0
 a=isqrt(q.numerator);b=isqrt(q.denominator)
 assert a*a==q.numerator and b*b==q.denominator
 return F(a,b)
def square(q):return q>=0 and isqrt(q.numerator)**2==q.numerator and isqrt(q.denominator)**2==q.denominator
def half(P,n):
 if P is None:return None
 x,y=P;r=[root(x),root(x-n),root(x+n)]
 if r[0]*r[1]*r[2]!=-y:r[2]=-r[2]
 assert r[0]*r[1]*r[2]==-y
 t=r[0]*r[1]+r[0]*r[2]+r[1]*r[2]
 Q=(x+t,-y-sum(r)*t)
 assert add(Q,Q,n)==P
 return Q
checks=0;nonunit=0
def check(R,e1,f1,e2,f2,e3):
 global checks,nonunit
 kappa=gcd(R,e1)*gcd(R,e2)
 for ep in (-1,1):
  for eq in (-1,1):
   Q0=e1*e2+ep*eq*f1*f2;P0=ep*f1*e2-eq*f2*e1;T=ep*e1*f1+eq*e2*f2
   if not Q0 or not P0:continue
   G=gcd(Q0,P0);c=R*R//G;u=isqrt(c//kappa);assert kappa*u*u==c
   Phi=kappa*u;n=kappa*(Q0//G)
   plus=(F(Phi*Phi),F(kappa*Phi*(P0//G)))
   minus=(-F(Phi*e3,R)**2,-F(Phi**3*e3*T,R**3));tors=(F(0),F(0))
   diff=add(add(minus,neg(plus),n),tors,n)
   H=half(diff,n)
   assert add(add(plus,tors,n),mul(2,H,n),n)==minus
   # The remaining doubling-graph square is exactly the third face.
   remaining=F(Phi*Phi)+minus[0]
   assert square(remaining)==square(F(R*R-e3*e3))
   checks+=1;nonunit+=kappa>1
tri=defaultdict(set)
for m in range(2,150):
 for n in range(1,m):
  R=m*m+n*n
  if R>20000 or gcd(m,n)!=1 or (m-n)%2==0:continue
  a=m*m-n*n;b=2*m*n;tri[R].update(((a,b),(b,a)))
for R,ts in tri.items():
 ts=sorted(ts)
 for i,(e1,f1) in enumerate(ts):
  for e2,f2 in ts[i+1:]:
   z2=R*R-e1*e1-e2*e2
   if z2>0 and isqrt(z2)**2==z2:check(R,e1,f1,e2,f2,isqrt(z2))
check(697,672,185,153,680,104)

# Exact cyclic-subgroup witness: all pre-third-face conditions, but not an endpoint.
a=F(5,13);b=F(12,13);P=(F(1),b);tors=(F(0),F(0));Q=mul(2,P,a)
N=add(mul(5,P,a),tors,a)
assert add(add(P,tors,a),mul(2,Q,a),a)==N
z=root(-N[0]);S=root((1+a)*(1-z*z/a));D=root((1-a)*(1+z*z/a))
assert S>D>0
x1=(S+D)/2;x2=(S-D)/2;v2=(a*x2-x1)/b;v1=b*x2+a*v2
assert x1*x1+x2*x2+z*z==1 and x1*x1+v1*v1==1 and x2*x2+v2*v2==1
assert not square(1-z*z)
R=lcm(x1.denominator,x2.denominator,z.denominator)
edges=[int(R*x1),int(R*x2),int(R*z)];faces=[int(R*v1),int(R*v2)]
assert gcd(gcd(edges[0],edges[1]),edges[2])==1
witness={'a':str(a),'b':str(b),'Q':'2*P','Pminus':'5*P+(0,0)','R':R,'edges':edges,'signed_two_faces':faces,'third_face_square':False,'physical_endpoint':False,'scope':'Cyclic-subgroup membership proves no rank-independence obstruction on the pre-third-face relaxation; no full-mask counterexample.'}
finite=0
for p in (17,41,73):
 roots=defaultdict(list)
 for y in range(p):roots[y*y%p].append(y)
 def padd(P,Q,a):
  if P is None:return Q
  if Q is None:return P
  x,y=P;u,v=Q
  if x==u and (y+v)%p==0:return None
  m=((3*x*x-a*a)*pow(2*y,-1,p) if P==Q else (v-y)*pow(u-x,-1,p))%p
  z=(m*m-x-u)%p;return z,(-y+m*(x-z))%p
 cache={}
 for e in range(1,p):
  for f in range(1,p):
   for z in roots[(1-e*e-f*f)%p]:
    if z==0:continue
    for fi in roots[(1-e*e)%p]:
     for fj in roots[(1-f*f)%p]:
      a=(e*f+fi*fj)%p;b=(fi*f-e*fj)%p
      if a in (0,1,p-1) or b==0 or (e+f)%p==0 or (e-f)%p==0:continue
      if a not in cache:
       pts=[None]+[(x,y) for x in range(p) for y in roots[(x**3-a*a*x)%p]]
       cache[a]={padd(P,P,a) for P in pts}
      T=(e*fi+f*fj)%p;N=(-z*z%p,-z*T%p)
      diff=padd(padd(N,(1,-b%p),a),(0,0),a)
      assert diff in cache[a]
      finite+=1
out={'card':'M3-T11-198','rational_coset_and_explicit_halving_checks':checks,'nonunit_checks':nonunit,'finite_field_exhaustive_double_image_membership_checks':finite,'cyclic_subgroup_partial_sphere_witness':witness,'physical_endpoints':0,'independent_audit':False,'status':'PASS'}
Path('M3-T11-198-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='cyclic_subgroup_partial_sphere_witness'}));print('witness primitive R digits',len(str(R)))
