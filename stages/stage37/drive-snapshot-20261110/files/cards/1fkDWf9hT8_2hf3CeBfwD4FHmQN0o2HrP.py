from fractions import Fraction as Q
from math import gcd,isqrt,lcm
from collections import defaultdict
from pathlib import Path
import json

tri=defaultdict(set)
for m in range(2,150):
 for n in range(1,m):
  R=m*m+n*n
  if R>20000 or gcd(m,n)!=1 or (m-n)%2==0:continue
  a=m*m-n*n;b=2*m*n
  tri[R].update(((a,b),(b,a)))
collision=0;bridge=0;nonunit=0;max_theta=0
def half(R,e1,f1,e2,f2):
 g=gcd(e1,e2);A=e1//g;F=e2//g
 x=Q((R+f1)*(R+f2),g*g);y=-x*Q(f1+f2,g)
 d=isqrt(x.denominator);assert d*d==x.denominator and y.denominator==d**3
 X=x.numerator;Ny=abs(y.numerator)
 D0=2*Ny*d;L=X*X-A*A*F*F*d**4
 L1=X*X-2*A*A*X*d*d+A*A*F*F*d**4
 L2=X*X-2*F*F*X*d*d+A*A*F*F*d**4
 k0=gcd(L,D0)
 assert (L//k0,D0//k0,L1//k0,L2//k0)==(R,g,f1,f2)
 return A,F,Ny,D0,L,L1,L2,k0
def points(R,e1,f1,e2,f2,e3):
 global bridge,nonunit,max_theta
 A,F,Ny,D0,L,L1,L2,k0=half(R,e1,f1,e2,f2)
 assert gcd(gcd(e1,e2),e3)==1
 W=k0*e3;assert W*W==L*L-(A*A+F*F)*D0*D0
 kappa=gcd(e1,R)*gcd(e2,R)
 assert gcd(gcd(e1,R),gcd(e2,R))==1
 for eps1 in (-1,1):
  for eps2 in (-1,1):
   q0=D0*D0*A*F+eps1*eps2*L1*L2
   p0=D0*(eps1*F*L1-eps2*A*L2)
   t0=D0*(eps1*A*L1+eps2*F*L2)
   assert q0*q0-t0*t0==W**4
   G=gcd(q0,p0);assert G%kappa==0
   H=isqrt(G//kappa);assert H*H==G//kappa and L%H==0
   Phi=L//H;q=q0//G;p=p0//G;Theta=kappa*q
   assert R%Phi==0 and Phi>0 and Theta!=0
   Xp=Phi*Phi;Yp=kappa*Phi*p
   Xm=-Q(W,H)**2;Ym=-Q(W*t0,H**3)
   assert Yp*Yp==Xp**3-Theta*Theta*Xp
   assert Ym*Ym==Xm**3-Theta*Theta*Xm
   a=Q(Theta,Phi*Phi);b=Q(Yp,Phi**3);z=Q(W,H*Phi)
   assert a==Q(e1*e2+eps1*eps2*f1*f2,R*R)
   assert b==Q(e2*eps1*f1-e1*eps2*f2,R*R)
   assert z==Q(e3,R)
   assert Q(e1+e2,R)**2==(1+a)*(1-z*z/a)
   assert Q(e1-e2,R)**2==(1-a)*(1+z*z/a)
   assert lcm(Q(e1,R).denominator,Q(e2,R).denominator,z.denominator)==R
   assert abs(Theta)>Phi
   bridge+=1;nonunit+=kappa>1;max_theta=max(max_theta,abs(Theta))
for R,ts in tri.items():
 ts=sorted(ts)
 for i,(e1,f1) in enumerate(ts):
  for e2,f2 in ts[i+1:]:
   A,F,Ny,*_=half(R,e1,f1,e2,f2)
   for eta in (-1,1):
    q=e1*e2+eta*f1*f2;p=f1*e2-eta*e1*f2
    c=R*R//gcd(q,p);s=isqrt(c);assert s*s==c
    d=R//s
    assert gcd(Ny,s)==gcd(abs(A-eta*F),s)
    assert gcd(Ny,d)==gcd(abs(A+eta*F),d)
    collision+=1
   z2=R*R-e1*e1-e2*e2
   if z2>0 and isqrt(z2)**2==z2:points(R,e1,f1,e2,f2,isqrt(z2))
points(697,672,185,153,680,104)
out={'card':'M3-T11-196','signed_unit_pair_ordinate_collision_checks':collision,'integer_W_two_point_bridge_checks':bridge,'nonunit_bridge_checks':nonunit,'max_abs_theta_in_bridge_tests':max_theta,'physical_endpoints':0,'test_scope':'Two-circle/partial-sphere loci, not full endpoints; missing face is retained as a required physical post-filter.','independent_audit':False,'status':'PASS'}
Path('M3-T11-196-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
