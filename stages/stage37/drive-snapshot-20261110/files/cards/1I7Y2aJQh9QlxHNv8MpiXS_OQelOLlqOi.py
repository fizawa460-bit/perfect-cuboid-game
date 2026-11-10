from fractions import Fraction as Q
from math import gcd,isqrt
from collections import defaultdict
from pathlib import Path
import json

def recover(A,F,R,f1,f2,g):
 x=Q((R+f1)*(R+f2),g*g);y=-x*Q(f1+f2,g)
 d=isqrt(x.denominator);assert d*d==x.denominator and y.denominator==d**3
 X=x.numerator;Ny=abs(y.numerator)
 js=(X,X-A*A*d*d,X-F*F*d*d)
 assert min(js)>0 and js[0]*js[1]*js[2]==Ny*Ny
 ad=isqrt(js[0]-js[1]);fd=isqrt(js[0]-js[2]);dr=gcd(ad,fd)
 assert (dr,ad//dr,fd//dr)==(d,A,F)
 L=X*X-A*A*F*F*d**4;D0=2*Ny*d;k=gcd(L,D0)
 assert (D0//k,L//k)==(g,R)
 L1=X*X-2*A*A*X*d*d+A*A*F*F*d**4
 L2=X*X-2*F*F*X*d*d+A*A*F*F*d**4
 assert (L1//k,L2//k)==(f1,f2) and L1%k==L2%k==0
 return d,X,Ny,L,D0,k
tri=defaultdict(list)
for m in range(2,150):
 for j in range(1,m):
  R=m*m+j*j
  if R>20000 or gcd(m,j)!=1 or (m-j)%2==0:continue
  a=m*m-j*j;b=2*m*j
  tri[R].extend(((a,b),(b,a)))
pairs=0
for R,ts in tri.items():
 for i,(ea,fa) in enumerate(ts):
  for eb,fb in ts[i+1:]:
   e1,f1,e2,f2=ea,fa,eb,fb;g=gcd(e1,e2);A=e1//g;F=e2//g
   if A%2==0:A,F=F,A;f1,f2=f2,f1
   if A%2==0 or F%2:continue
   recover(A,F,R,f1,f2,g);pairs+=1
# Non-unit individual contents: a larger two-triangle locus, still no full endpoint claim.
alltri=defaultdict(set)
for m in range(2,46):
 for j in range(1,m):
  D=m*m+j*j
  if D>2000 or gcd(m,j)!=1 or (m-j)%2==0:continue
  a=m*m-j*j;b=2*m*j
  for sc in range(1,2000//D+1):
   alltri[D*sc].update(((sc*a,sc*b),(sc*b,sc*a)))
nonunit=0
for R,ts0 in alltri.items():
 ts=sorted(ts0)
 for i,(ea,fa) in enumerate(ts):
  for eb,fb in ts[i+1:]:
   if gcd(R,ea)==gcd(R,eb)==1:continue
   g=gcd(ea,eb);A=ea//g;F=eb//g;f1=fa;f2=fb
   if gcd(R,g)!=1:continue
   if A%2==0:A,F=F,A;f1,f2=f2,f1
   if A%2==0 or F%2:continue
   recover(A,F,R,f1,f2,g);nonunit+=1
boundary=0;gcdchecks=0
for m in range(2,101):
 for j in range(1,m):
  if gcd(m,j)!=1 or (m-j)%2==0:continue
  A=m*m-j*j;F=2*m*j;n=m*m+j*j
  d,X,Ny,L,D0,k=recover(A,F,n,F,A,1)
  assert L*L-n*n*D0*D0==0
  assert Ny>n**3*d**3 and Ny<8*n**3*d**3
  assert gcd(0,D0)==k
  boundary+=1
  # Scaled integer right-triangle relation, not an endpoint.
  for scale in (1,2,7,20):
   for g in (1,F):
    ni=F//g;Li=scale*n;Wi=scale*A;Di=scale*g
    assert Li*Li-Wi*Wi==ni*ni*Di*Di
    assert gcd(Li,Di)==gcd(Wi,Di)==scale
    gcdchecks+=1
out=dict(card='M3-T11-192',status='PASS',two_primitive_space_triangle_factor_and_inverse_checks=pairs,nonunit_content_two_space_triangle_checks=nonunit,primitive_face_zero_edge_boundary_full_receiver_checks=boundary,scaled_integer_gcd_identity_checks=gcdchecks,physical_endpoints_enumerated=0,scope='Exact divisor-factor and inverse reconstruction; full receiver checked on zero-edge boundaries only. Two-triangle/scaled triples are over-cover tests, not positive endpoints. No independent audit or moving occupancy theorem.')
Path('M3-T11-192-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
