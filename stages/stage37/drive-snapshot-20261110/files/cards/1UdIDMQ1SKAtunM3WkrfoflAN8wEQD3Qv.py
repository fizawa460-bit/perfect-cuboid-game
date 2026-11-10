from fractions import Fraction as Q
from math import gcd,isqrt
from collections import defaultdict
from pathlib import Path
import json

def factors(n):
 r={};p=2
 while p*p<=n:
  while n%p==0:r[p]=r.get(p,0)+1;n//=p
  p+=1
 if n>1:r[n]=1
 return r

def vp(n,p):
 v=0
 while n%p==0:n//=p;v+=1
 return v
tri=defaultdict(list)
for m in range(2,150):
 for k in range(1,m):
  R=m*m+k*k
  if R>20000 or gcd(m,k)!=1 or (m-k)%2==0:continue
  a=m*m-k*k;b=2*m*k
  tri[R].extend(((a,b),(b,a)))
checks=0;cases=defaultdict(int);examples={}
for R,pairs in tri.items():
 for i,(edge1,diag1) in enumerate(pairs):
  for edge2,diag2 in pairs[i+1:]:
   e1,f1,e2,f2=edge1,diag1,edge2,diag2
   g=gcd(e1,e2);A=e1//g;F=e2//g
   if A%2==0:A,F=F,A;e1,e2=e2,e1;f1,f2=f2,f1
   if A%2==0 or F%2 or gcd(g,R)!=1:continue
   x=Q((R+f1)*(R+f2),g*g)
   y=-Q((R+f1)*(R+f2)*(f1+f2),g**3)
   assert y*y==x*(x-A*A)*(x-F*F)
   d=isqrt(x.denominator);assert d*d==x.denominator
   pred=1
   for p,v in factors(g).items():
    if p==2:
     s1=vp(R+f1,2);s2=vp(R+f2,2)
     assert s1 in (1,2*v-1) and s2 in (1,2*(v+vp(F,2))-1)
     if s1==s2==1:pred*=2**(v-1)
    elif (R+f1)%p and (R+f2)%p:pred*=p**v
   assert pred==d and g%d==0 and y.denominator==d**3
   assert R*R*Q(d*d,g*g)<x.numerator<4*R*R*Q(d*d,g*g)
   z=-Q(x*x-A*A*F*F,2*y);assert z==Q(R,g)
   assert (2*y.numerator)% (g//d)==0
   key='g_even' if g%2==0 else 'g_odd';cases[key]+=1
   if d<g:cases['cancellation']+=1
   if 1<d<g:cases['partial_cancellation']+=1
   if d==1:cases['integral_halfpoint']+=1
   examples.setdefault(key,dict(R=R,e1=e1,e2=e2,f1=f1,f2=f2,g=g,d=d))
   checks+=1
out=dict(card='M3-T11-191',status='PASS',primitive_two_space_triangle_pairs=checks,cases=dict(cases),examples=examples,physical_endpoints_enumerated=0,scope='Exact Fraction denominator, parity, height and inverse checks on two primitive space triangles; the third face/full cuboid lift is not asserted. General theorem is deductive; no global occupancy saving or independent audit.')
Path('M3-T11-191-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
