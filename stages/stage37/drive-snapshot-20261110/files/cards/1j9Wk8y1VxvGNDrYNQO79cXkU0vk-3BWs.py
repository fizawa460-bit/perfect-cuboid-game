from fractions import Fraction as Q
from math import gcd,isqrt
from collections import defaultdict
from pathlib import Path
import json

finite=0;maps=0
for p in (17,41,73):
 roots=defaultdict(list)
 for v in range(1,p):roots[v*v%p].append(v)
 for e in range(1,p):
  for f in range(1,p):
   z2=(1-e*e-f*f)%p
   if z2 not in roots or (1-e*e)%p not in roots or (1-f*f)%p not in roots:continue
   for z in roots[z2]:
    if (1-z*z)%p not in roots:continue
    for fi in roots[(1-e*e)%p]:
     for fj in roots[(1-f*f)%p]:
      a=(e*f+fi*fj)%p;b=(fi*f-e*fj)%p
      if a in (0,1,p-1) or b==0:continue
      S=(e+f)%p;D=(e-f)%p
      if S==0 or D==0:continue
      ai=pow(a,-1,p);bi=pow(b,-1,p)
      for t in roots[(1-z*z)%p]:
       V=a*bi*S*D%p;Y=V*t%p;T=(e*fi+f*fj)%p
       assert (V+T)%p==0
       x=z*z%p
       # Three character-pair elliptic quotients.
       assert ((z*V)**2-((-x)**3-a*a*(-x)))%p==0
       assert ((z*S*t)**2-(1+a)*ai*x*(a-x)*(1-x))%p==0
       assert ((z*D*t)**2-(1-a)*ai*x*(a+x)*(1-x))%p==0
       # Two elliptic quotients of the even genus-two character.
       assert (Y*Y-(a*a-x*x)*(1-x))%p==0
       u=pow(x,-1,p);v=Y*pow(z**3,-1,p)%p
       assert (v*v-(a*a*u*u-1)*(u-1))%p==0
       finite+=1;maps+=5

tri=defaultdict(set)
for m in range(2,150):
 for n in range(1,m):
  R=m*m+n*n
  if R>20000 or gcd(m,n)!=1 or (m-n)%2==0:continue
  a=m*m-n*n;b=2*m*n;tri[R].update(((a,b),(b,a)))
partial=0;receiver=0;third_pass=0
def square(q):return q>=0 and isqrt(q.numerator)**2==q.numerator and isqrt(q.denominator)**2==q.denominator
def check(R,e1,f1,e2,f2,e3):
 global partial,receiver,third_pass
 g=gcd(e1,e2);A=e1//g;F=e2//g;kappa=gcd(e1,R)*gcd(e2,R)
 for ep in (-1,1):
  for eq in (-1,1):
   QQ=e1*e2+ep*eq*f1*f2;PP=ep*f1*e2-eq*f2*e1;T=ep*e1*f1+eq*e2*f2
   if not QQ or not PP or not T:continue
   G0=gcd(QQ,PP);c=R*R//G0;u=isqrt(c//kappa);assert kappa*u*u==c
   Phi=kappa*u;Theta=kappa*(QQ//G0);U=Q(Phi*e3,R)**2
   v2=(U*U-Theta*Theta)*(U-Phi*Phi)
   assert v2==Q(Phi**6*T*T*(R*R-e3*e3),R**6)
   assert square(v2)==(isqrt(R*R-e3*e3)**2==R*R-e3*e3)
   assert square(v2/(Theta*Theta-U*U))==square(Q(Phi*Phi)-U)
   partial+=1;third_pass+=square(v2)
   for k0 in (1,2,7):
    L=k0*R;W=k0*e3;D0=k0*g;BT=k0*k0*T;H=Q(L,Phi)
    assert v2==Q(BT*BT*D0*D0*(A*A+F*F))/H**6
    receiver+=1
for R,ts in tri.items():
 ts=sorted(ts)
 for i,(e1,f1) in enumerate(ts):
  for e2,f2 in ts[i+1:]:
   v=R*R-e1*e1-e2*e2
   if v>0 and isqrt(v)**2==v:check(R,e1,f1,e2,f2,isqrt(v))
check(697,672,185,153,680,104)
# Independent sign characters for three elliptic differentials and two triple-character forms.
characters=[(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
for i,a in enumerate(characters):
 for j,b in enumerate(characters):
  total=sum((-1)**sum((a[k]+b[k])*((mask>>k)&1) for k in range(3)) for mask in range(8))
  assert total==(8 if i==j else 0)
out={'card':'M3-T11-197','finite_field_full_cover_points':finite,'five_elliptic_map_checks':maps,'rational_partial_sphere_third_face_equivalence_checks':partial,'scaled_integer_receiver_identity_checks':receiver,'partial_locus_third_face_pass':third_pass,'differential_character_orthogonality':'PASS; triple-character forms 1,z are independent functions','physical_endpoints':0,'independent_audit':False,'status':'PASS'}
Path('M3-T11-197-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
