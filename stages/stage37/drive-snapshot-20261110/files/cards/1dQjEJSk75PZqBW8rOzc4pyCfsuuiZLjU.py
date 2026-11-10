import itertools,random,json,math
from pathlib import Path

def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(p,q):
 z=[0]*max(len(p),len(q))
 for i,x in enumerate(p):z[i]+=x
 for i,x in enumerate(q):z[i]+=x
 return trim(z)
def neg(p):return [-x for x in p]
def sub(p,q):return add(p,neg(q))
def mul(p,q):
 z=[0]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):z[i+j]+=x*y
 return trim(z)
def scale(p,c):return trim([c*x for x in p])
def sq(p):return mul(p,p)
def power(p,k):
 z=[1]
 for _ in range(k):z=mul(z,p)
 return z
def ev(p,n):
 z=0
 for c in reversed(p):z=z*n+c
 return z
def zero(p):return p==[0]
def data(R,A):
 Z=sq(R);q=[sub(scale(Z,2),sq(a)) for a in A];Q=[mul(sq(a),v) for a,v in zip(A,q)]
 D=power(Z,4)
 for v in Q:D=add(D,sq(v));D=sub(D,scale(mul(sq(Z),v),2))
 for i,j in itertools.combinations(range(3),2):D=sub(D,scale(mul(Q[i],Q[j]),2))
 P=sub(sq(D),scale(mul(sq(Z),mul(mul(Q[0],Q[1]),Q[2])),64))
 return q,P
def radical_mul(f,g,q):
 out={}
 for m,p in f.items():
  for n,v in g.items():
   z=mul(p,v)
   for i in range(3):
    if (m&n)&(1<<i):z=mul(z,q[i])
   key=m^n;out[key]=add(out.get(key,[0]),z)
 return {m:p for m,p in out.items() if not zero(p)}
def norm(R,A,q):
 f={0:[1]}
 for signs in itertools.product((-1,1),repeat=3):
  g={0:sq(R)}
  for i,(a,s) in enumerate(zip(A,signs)):g[1<<i]=scale(a,s)
  f=radical_mul(f,g,q)
 return f
def classification(R,A):
 s,r=(R+[0,0])[:2]
 ks=[r*(a+[0,0])[0]-s*(a+[0,0])[1] for a in A]
 radial=all(k==0 for k in ks)
 boundary=any(zero(sub(sq(A[i]),sq(R))) and zero(sub(sq(A[j]),sq(A[k])))
              for i,j,k in ((0,1,2),(1,0,2),(2,0,1)))
 return radial,boundary

# Exhaustive coefficient grid for R=n and constant R=1.
vecs=[[b,a] for a,b in itertools.product(range(-2,3),repeat=2) if (a,b)!=(0,0)]
counts={'packets':0,'nonradial_identity':0,'radial_identity':0,'nonidentity':0,'max_degree':0}
for R in ([0,1],[1,0]):
 for A in itertools.product(vecs,repeat=3):
  q,P=data(R,A);radial,boundary=classification(R,A)
  counts['packets']+=1
  assert len(P)-1<=16
  counts['max_degree']=max(counts['max_degree'],len(P)-1)
  if zero(P):
   assert radial or boundary,(R,A)
   counts['radial_identity' if radial else 'nonradial_identity']+=1
  else:counts['nonidentity']+=1

# Exact sign-product identity on random affine families, no floating radicals.
rng=random.Random(145);norm_tests=200
for _ in range(norm_tests):
 R=[rng.randint(-5,5),rng.randint(-5,5)]
 A=[[rng.randint(-5,5),rng.randint(-5,5)] for _ in range(3)]
 q,P=data(R,A);f=norm(R,A,q)
 assert f==({0:P} if not zero(P) else {})
 for n in (-3,0,2):
  aa=[ev(a,n) for a in A];rr=ev(R,n)
  for i,j in itertools.combinations(range(3),2):
   qi=2*rr*rr-aa[i]*aa[i];qj=2*rr*rr-aa[j]*aa[j]
   assert aa[i]**2*qi-aa[j]**2*qj==(aa[i]**2-aa[j]**2)*(2*rr*rr-aa[i]**2-aa[j]**2)

# Boundary samples genuinely satisfy full signed equations; positivity fails.
boundary_samples=0
for R in range(1,80):
 for A in range(-math.isqrt(2*R*R),math.isqrt(2*R*R)+1):
  q=2*R*R-A*A
  if q<0 or math.isqrt(q)**2!=q:continue
  y=math.isqrt(q);aa=(A,A,R);yy=(y,-y,-R)
  assert all(a*a+b*b==2*R*R for a,b in zip(aa,yy))
  assert sum(a*b for a,b in zip(aa,yy))==-R*R
  assert aa[2]+yy[2]==0
  assert sum((a+b)**2 for a,b in zip(aa,yy))==4*R*R
  boundary_samples+=1

# 142 must meet the nonidentity polynomial, not a contained physical line.
q,P=data([0,17],[[5,6],[3,6],[4,3]])
assert not zero(P)
assert all(ev(P,241+8670*k)!=0 for k in range(100))
out={'status':'PASS',**counts,'exact_radical_norm_replays':norm_tests,
 'signed_zero_edge_boundary_samples':boundary_samples,'142_nonzero_P_samples':100,
 'physical_endpoints_enumerated':0,'global_counting_credit':0,
 'audit':'within-session; not external'}
Path(__file__).with_name('verification145.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
