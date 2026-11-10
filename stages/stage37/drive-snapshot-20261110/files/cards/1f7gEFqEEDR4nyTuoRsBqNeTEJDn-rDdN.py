import json, math
from pathlib import Path
class P:
 def __init__(self,d): self.d={k:v for k,v in d.items() if v}
 def co(x): return x if isinstance(x,P) else P({(0,)*6:x})
 def __add__(self,x):
  x=P.co(x);d=self.d.copy()
  for k,v in x.d.items():d[k]=d.get(k,0)+v
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,x):return self+-P.co(x)
 def __rsub__(self,x):return P.co(x)+-self
 def __mul__(self,x):
  d={}
  for k,v in self.d.items():
   for l,w in P.co(x).d.items():
    m=tuple(ki+li for ki,li in zip(k,l));d[m]=d.get(m,0)+v*w
  return P(d)
 __rmul__=__mul__
 def __pow__(self,k):
  z=P.co(1)
  for _ in range(k):z=z*self
  return z
n,r,t,a,b,y=[P({tuple(int(i==j) for i in range(6)):1}) for j in range(6)]
Q=2*(r*n+t)**2-(a*n+b)**2
aa=2*r*r-a*a;bb=4*r*t-2*a*b;cc=2*t*t-b*b
disc=bb*bb-4*aa*cc
assert not (disc-8*(r*b-t*a)**2).d
assert not ((2*aa*n+bb)**2-aa*(2*y)**2-disc-4*aa*(Q-y*y)).d
count=0
for rr in range(1,8):
 for tt in range(-3,4):
  for ai in range(-8,9):
   for bi in range(-3,4):
    A=2*rr*rr-ai*ai; B=4*rr*tt-2*ai*bi; C=2*tt*tt-bi*bi
    assert B*B-4*A*C==8*(rr*bi-tt*ai)**2
    for nn in (-2,0,1,5):
     q=2*(rr*nn+tt)**2-(ai*nn+bi)**2
     yy=math.isqrt(q) if q>=0 else 0
     assert (2*A*nn+B)**2-A*(2*yy)**2-(B*B-4*A*C)==4*A*(q-yy*yy)
    count+=1
# 142 remains nonphysical; its normalized Pell coefficients are exact.
assert not ((2*(17*n)**2-(6*n+3)**2)-(542*n*n-36*n-9)).d
assert 36**2+4*542*9==20808==8*51**2
for k in range(1000):
 nn=241+8670*k
 assert (542*nn*nn-36*nn-9)%3==2
# A radial boundary lift passes the unsigned polynomial-square cover but fails signed sum.
assert not (3*n*n-(-n*n)-4*n*n).d
out={'status':'PASS','abstract_affine_packets':count,'integer_checks':count*4,
 '142_AP_nonphysical':1000,'symbolic_discriminant':'8*(r*b-t*a)^2',
 'symbolic_Pell_identity':'0','positive_physical_endpoints_enumerated':0,
 'audit':'within-session, not external','global_counting_credit':0}
Path(__file__).with_name('verification143.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
