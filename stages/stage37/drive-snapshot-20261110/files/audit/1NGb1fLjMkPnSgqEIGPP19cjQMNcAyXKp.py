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

# Exact sparse-power multiplicity certificate at a nonzero argument.
# Euler derivatives (w d/dw)^j of w^e equal e^j w^e.
# Up to three distinct powers have a Vandermonde determinant.
from itertools import combinations
vandermonde_checks=0
for r in [1,2,3]:
 for exponents in combinations(range(-12,13,2),r):
  M=[[G(e**j) for e in exponents] for j in range(r)]
  expected=1
  for i in range(r):
   for j in range(i+1,r):expected*=exponents[j]-exponents[i]
  got=det(M);assert got.a==expected and not got.b and got
  vandermonde_checks+=1

# Every3x3 allocation matrix for a square-free degree6 lift: entries -1/0/1.
# Each root pair needs at least2 active coordinates, by common-factor and pole tests.
patterns=0
for flat in product([-1,0,1],repeat=9):
 if all(sum(flat[3*i+j]!=0 for i in range(3))>=2 for j in range(3)):
  patterns+=1
assert patterns==8000

def conj(x):return G(x.a,-x.b)
def allocation(roots,mode):
 h=[G(1)]
 for root,a in zip(roots,mode):
  h=mul(h,power([-root,G(1)],1+a))
  h=mul(h,power([-conj(root),G(1)],1-a))
 return h
def rank(cols):
 rows=len(cols[0]);M=[[c[i] for c in cols] for i in range(rows)];r=0
 for j in range(len(cols)):
  p=next((i for i in range(r,rows) if M[i][j]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];v=M[r][j];M[r]=[x/v for x in M[r]]
  for i in range(rows):
   if i!=r:
    v=M[i][j];M[i]=[x-v*y for x,y in zip(M[i],M[r])]
  r+=1
  if r==rows:break
 return r

sample_ranks=[];circle_checks=0;phase_receiver_checks=0
phases=[G(1),G(0,1),G(F(3,5),F(4,5))]
for roots in [[G(0,1),G(0,2),G(1,1)],[G(0,1),G(0,3),G(2,1)]]:
 modes=list(product([-1,0,1],repeat=3));hs=[allocation(roots,a) for a in modes]
 r=allocation(roots,(0,0,0));r2=mul(r,r)
 cs=[mul(h,h) for h in hs]
 sample_ranks.append(rank(cs))
 for h,c in zip(hs,cs):
  assert all(not(x-y) for x,y in zip(mul(h,[conj(x) for x in h]),r2));circle_checks+=1
  for phase in phases:
   ph=[phase*x for x in h];E=[G(x.a) for x in ph];Esq=mul(E,E)
   lam=phase*phase
   # 2 E^2 = Re(lambda H^2) + R^2 coefficientwise.
   assert all(not(2*x-G((lam*y).a)-z) for x,y,z in zip(Esq,c,r2))
   phase_receiver_checks+=1
assert sample_ranks==[13,13]

# Valid boundary maps with two distinct pairs, multiple arbitrary multiplicities.
boundary_checks=0
for n,m in [(2,1),(3,1),(2,2),(4,3)]:
 h=mul(power([G(0,-1),G(1)],2*n),power([G(0,-2),G(1)],2*m))
 r=mul(power([G(1),G(),G(1)],n),power([G(4),G(),G(1)],m))
 e=[G(x.a) for x in h];f=[G(x.b) for x in h]
 assert all(not(x+y-z) for x,y,z in zip(mul(e,e),mul(f,f),mul(r,r)))
 boundary_checks+=1
import json
from pathlib import Path
out={'sparse_power_vandermonde_checks':vandermonde_checks,'squarefree_degree6_local_allocation_patterns':patterns,'sample_27column_squared_allocation_ranks':sample_ranks,'sample_kernel_dimensions':[27-x for x in sample_ranks],'allocation_circle_checks':circle_checks,'exact_phase_receiver_checks':phase_receiver_checks,'two_pair_boundary_checks':boundary_checks,'universal_two_pair_result':'ZERO_EDGE_FOR_NONCONSTANT_BASEPOINT_FREE_SIGNED_LIFTS','squarefree_degree6':'OPEN','sample_scope':'fixed rational Gaussian roots only; rank samples not universal exclusion','global_counting_credit':0}
Path(__file__).with_name('verification149.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
