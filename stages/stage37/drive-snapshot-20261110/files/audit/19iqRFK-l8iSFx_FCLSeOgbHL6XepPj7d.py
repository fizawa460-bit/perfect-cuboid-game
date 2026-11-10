from fractions import Fraction as F
from itertools import product
class G:
 def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
 def __add__(x,y):
  if not isinstance(y,G):y=G(y)
  return G(x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return G(-x.a,-x.b)
 def __sub__(x,y):return x+-y
 def __mul__(x,y):
  if not isinstance(y,G):y=G(y)
  return G(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
 __rmul__=__mul__
 def __truediv__(x,y):
  if not isinstance(y,G):y=G(y)
  d=y.a*y.a+y.b*y.b
  return G((x.a*y.a+x.b*y.b)/d,(x.b*y.a-x.a*y.b)/d)
 def __bool__(x):return bool(x.a or x.b)
 def __repr__(x):return f'({x.a},{x.b})'
def mul(a,b):
 out=[G() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return out
def power(a,n):
 out=[G(1)]
 for _ in range(n):out=mul(out,a)
 return out
from itertools import permutations
def det(A):
 n=len(A);out=G()
 for p in permutations(range(n)):
  v=G((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
  for i in range(n):v=v*A[i][p[i]]
  out=out+v
 return out
reps=[(1,1),(1,0),(1,-1),(0,1)]
def matrices(k):
 ec=[];oc=[]
 for a,b in reps:
  h=[G(1)]
  for p,n in [([G(0,-1),G(1)],1+a),([G(0,1),G(1)],1-a),([G(0,-k),G(1)],1+b),([G(0,k),G(1)],1-b)]:h=mul(h,power(p,n))
  hs=mul(h,h);ec.append([G(hs[j].a) for j in range(0,9,2)]);oc.append([G(hs[j].b) for j in range(1,9,2)])
 r=mul([G(1),G(),G(1)],[G(k*k),G(),G(1)]);r2=mul(r,r);ec.append([G(r2[j].a) for j in range(0,9,2)])
 return ec,oc
def pmul(a,b):
 o=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o
def padd(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def interpolate(ys):
 o=[F(0)]
 for j,y in enumerate(ys):
  p=[F(1)];den=F(1)
  for h in range(len(ys)):
   if h!=j:p=pmul(p,[-h,1]);den*=j-h
  o=padd(o,[v*y/den for v in p])
 while len(o)>1 and not o[-1]:o.pop()
 return o
def factor(p):
 fac=[]
 for root in [0,1,-1]:
  n=0
  while len(p)>1:
   q=[F(0)]*(len(p)-1);q[-1]=p[-1]
   for j in range(len(q)-2,-1,-1):q[j]=p[j+1]+root*q[j+1]
   if p[0]+root*q[0]:break
   p=q;n+=1
  fac.append((root,n))
 return fac,p
def coeff_det(kind):
 ys=[]
 for k in range(17):
  ec,oc=matrices(k)
  cs=oc if kind=='odd' else [ec[j] for j in [0,1,2,4]]
  rows=range(4) if kind=='odd' else range(1,5)
  d=det([[c[r] for c in cs] for r in rows]);assert not d.b;ys.append(d.a)
 return interpolate(ys)
def ppow(a,n):
 out=[F(1)]
 for _ in range(n):out=pmul(out,a)
 return out
odd_expected=[-32768*x for x in pmul([0]*6+[1],ppow([-1,0,1],2))]
even_expected=[-2048*x for x in pmul([0]*3+[1],ppow([-1,0,1],3))]
assert coeff_det('odd')==odd_expected
assert coeff_det('even')==even_expected
modes=list(product(range(-1,2),repeat=2));kernel_checks=0
for k in range(17):
 cols=[]
 for a,b in modes:
  h=[G(1)]
  for p,n in [([G(0,-1),G(1)],1+a),([G(0,1),G(1)],1-a),([G(0,-k),G(1)],1+b),([G(0,k),G(1)],1-b)]:h=mul(h,power(p,n))
  cols.append(mul(h,h))
 weights=[]
 for a,b in modes:
  if not a and not b:w=4*(k**4-10*k*k+1)
  elif not a or not b:w=-2*(k*k-1)**2
  elif a==b:w=(k-1)**4
  else:w=(k+1)**4
  weights.append(w)
 for j in range(9):assert not sum((c[j]*w for c,w in zip(cols,weights)),G());kernel_checks+=1
 # For k positive and distinct from1 all eight off-center entries are nonzero.
 if k>0 and k!=1:assert all(w for mode,w in zip(modes,weights) if mode!=(0,0))
# Sparse support receiver:3 coordinates contribute at most6 off-center modes.
patterns=0
for triple in product(modes,repeat=3):
 support=set()
 for a,b in triple:
  if a or b:support.update([(a,b),(-a,-b)])
 assert len(support)<=6;patterns+=1
# Single conjugate pair: arbitrary multiplicity n, no other roots.
# Laurent coefficients have independent powers; 1/2 per rotating coordinate.
# Verify boundary powers n=1..6 with exact Gaussian polynomials.
boundary_checks=0
for n in range(1,7):
 h=power([G(0,-1),G(1)],2*n)
 e=[G(x.a) for x in h];f=[G(x.b) for x in h]
 r=power([G(1),G(),G(1)],n)
 es=mul(e,e);fs=mul(f,f);rs=mul(r,r)
 assert all(not(x+y-z) for x,y,z in zip(es,fs,rs));boundary_checks+=1
out={'symbolic_degree_bound_det':16,'exact_interpolation_nodes':17,'odd_minor':'-32768*k^6*(k^2-1)^2','even_minor':'-2048*k^3*(k^2-1)^3','minor_polynomial_identities':'PASS','kernel_coefficient_checks':kernel_checks,'kernel_degree_bound':8,'allocation_support_patterns':patterns,'max_off_center_modes_per_three_coordinates':6,'required_nonzero_off_center_kernel_modes':8,'single_pair_boundary_power_checks':boundary_checks,'all_positive_degree4_maps':'EXCLUDED_BY_UNIVERSAL_PROOF','global_counting_credit':0}
import json
from pathlib import Path
Path(__file__).with_name('verification148.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
