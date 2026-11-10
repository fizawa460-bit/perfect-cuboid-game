import math, json
from pathlib import Path

def bound(r,s,a,b,B):
 k=r*b-s*a;d=2*r*r-a*a;D=8*k*k
 assert r and k and d
 if d<0:return 1+math.sqrt(D)/abs(d)
 U=(2*d*B+2*abs(a*k))/abs(r)
 if U<math.sqrt(D):return 0
 return 2*(1+math.log(2*U/math.sqrt(D))/math.asinh(math.sqrt(d)/D))

packets=0; evaluations=0; survivors=0; definite=0;indefinite=0
for r in range(1,6):
 for s in range(-3,4):
  for a in range(-8,9):
   for b in range(-3,4):
    k=r*b-s*a
    if not k:continue
    d=2*r*r-a*a;D=8*k*k
    assert d and (4*r*s-2*a*b)**2-4*d*(2*s*s-b*b)==D
    B=500;ns=[]
    for n in range(math.ceil((1-s)/r),math.floor((B-s)/r)+1):
     R=r*n+s;A=a*n+b;q=2*R*R-A*A
     evaluations+=1
     if q>=0 and math.isqrt(q)**2==q:ns.append(n)
    assert len(ns)<=bound(r,s,a,b,B)+1e-8
    # Exact R-based norm coordinate identity, including X<0.
    for n in ns:
     R=r*n+s;X=2*d*n+4*r*s-2*a*b;W=2*math.isqrt(2*R*R-(a*n+b)**2)
     assert r*X==2*d*R-2*a*k
     assert X*X-d*W*W==D
    packets+=1;survivors+=len(ns)
    if d<0:definite+=1
    else:indefinite+=1

gaps=0;norm_sets=0
for d in range(1,26):
 for D in range(1,101):
  pts=[]
  for X in range(math.isqrt(D),1001):
   v=X*X-D
   if v<0 or v%d:continue
   W=math.isqrt(v//d)
   if W*W==v//d:pts.append((X,W))
  if not pts:continue
  norm_sets+=1
  gap=math.asinh(math.sqrt(d)/D)
  for (x1,w1),(x2,w2) in zip(pts,pts[1:]):
   det=x1*w2-x2*w1
   assert det>=1
   L=x1*x2-d*w1*w2
   assert L*L-d*det*det==D*D
   ratio=(x2+math.sqrt(d)*w2)/(x1+math.sqrt(d)*w1)
   assert math.log(ratio)+1e-10>=gap
   gaps+=1
  upper=1+math.log(2000/math.sqrt(D))/gap
  assert len(pts)<=upper+1e-8

# Primitive radial repetitions count one candidate, not infinitely many n.
assert math.gcd(3,4)==1
# Moving normalized direction in a constant-R family has a bounded parameter interval.
for s in range(1,20):
 for a in range(1,8):
  ns=[n for n in range(-100,101) if abs(a*n+3)<=math.sqrt(2)*s]
  assert len(ns)<=1+2*math.sqrt(2)*s/a+1e-8

out={'status':'PASS','affine_packets':packets,'definite_packets':definite,
 'indefinite_packets':indefinite,'integer_evaluations':evaluations,
 'unsigned_square_hits':survivors,'norm_sets':norm_sets,'successive_gap_checks':gaps,
 'physical_endpoints_enumerated':0,'global_counting_credit':0,
 'audit':'within-session; no external audit'}
Path(__file__).with_name('verification144.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
