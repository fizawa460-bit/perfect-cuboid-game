from fractions import Fraction as F
from math import gcd,isqrt,lcm
from collections import defaultdict
from pathlib import Path
import json

tri=defaultdict(set)
for m in range(2,150):
 for n in range(1,m):
  d=m*m+n*n
  if d>20000 or gcd(m,n)!=1 or (m-n)%2==0:continue
  x=m*m-n*n;y=2*m*n
  tri[d].update(((x,y),(y,x)))
unit_checks=0; rational_checks=0; nonunit_checks=0; examples=[]
def check(R,e1,f1,e2,f2,e3):
 global rational_checks,nonunit_checks
 for t1 in (-1,1):
  for t2 in (-1,1):
   v1=t1*f1;v2=t2*f2
   Q=e1*e2+v1*v2;P=v1*e2-e1*v2;T=e1*v1+e2*v2
   assert Q*Q+P*P==R**4 and Q*Q-T*T==e3**4
   assert P*T==Q*(e2*e2-e1*e1)
   if not Q or not P:continue
   a=F(Q,R*R);b=F(P,R*R);z=F(e3,R)
   X=-z*z;Y=-z*F(T,R*R)
   assert Y*Y==X**3-a*a*X
   S=F(e1+e2,R);D=F(e1-e2,R)
   assert S*S==(1+a)*(1-z*z/a)
   assert D*D==(1-a)*(1+z*z/a)
   assert F(v2,R)==(a*F(e2,R)-F(e1,R))/b
   assert F(v1,R)==b*F(e2,R)+a*F(v2,R)
   g=gcd(gcd(e1,e2),e3)
   assert lcm(F(e1,R).denominator,F(e2,R).denominator,z.denominator)==R//gcd(R,g)
   if g==1:assert lcm(F(e1,R).denominator,F(e2,R).denominator,z.denominator)==R
   rational_checks+=1
   if gcd(R,e1)>1 or gcd(R,e2)>1:nonunit_checks+=1
for R,ts in tri.items():
 ts=sorted(ts)
 for i,(e1,f1) in enumerate(ts):
  for e2,f2 in ts[i+1:]:
   for t in (-1,1):
    Q=e1*e2+t*f1*f2;P=f1*e2-t*e1*f2
    c=R*R//gcd(Q,P);s=isqrt(c)
    assert s*s==c and R%s==0 and gcd(s,R//s)==1
    unit_checks+=1
   u=R*R-e1*e1-e2*e2
   if u>0 and isqrt(u)**2==u:check(R,e1,f1,e2,f2,isqrt(u))
# This partial cuboid has integral space diagonal and two faces, but its third face is absent.
check(697,672,185,153,680,104)
examples.append({'R':697,'edges':[672,153,104],'two_faces':[185,680],'third_face_integral':False})
# Full circle/sphere algebra over finite fields; these are not rational endpoints.
finite=0
for p in (17,41,73):
 roots=defaultdict(list)
 for x in range(1,p):roots[x*x%p].append(x)
 for x in range(1,p):
  for y in range(1,p):
   z2=(1-x*x-y*y)%p
   if z2 not in roots:continue
   if (1-x*x)%p not in roots or (1-y*y)%p not in roots:continue
   for z in roots[z2]:
    if (1-z*z)%p not in roots:continue
    for f in roots[(1-x*x)%p]:
     for g in roots[(1-y*y)%p]:
      a=(x*y+f*g)%p;b=(f*y-x*g)%p;T=(x*f+y*g)%p
      if a==0 or b==0:continue
      X=-z*z%p;Y=-z*T%p
      assert (Y*Y-X**3+a*a*X)%p==0
      ai=pow(a,-1,p)
      assert ((x+y)**2-(1+a)*(1-z*z*ai))%p==0
      assert ((x-y)**2-(1-a)*(1+z*z*ai))%p==0
      finite+=1
out={'card':'M3-T11-194','unit_pair_square_denominator_checks':unit_checks,'rational_partial_sphere_map_checks':rational_checks,'nonunit_partial_sphere_map_checks':nonunit_checks,'finite_field_full_circle_sphere_checks':finite,'partial_examples':examples,'physical_endpoints':0,'independent_audit':False,'status':'PASS'}
Path('M3-T11-194-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
