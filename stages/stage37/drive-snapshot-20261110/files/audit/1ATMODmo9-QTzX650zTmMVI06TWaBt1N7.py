import math,json,itertools
from fractions import Fraction as Q
from pathlib import Path

def sq(q):
 q=Q(q)
 return q>=0 and math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator
def surf(v):
 S=sum(v);E=sum(v[i]*v[j] for i,j in [(0,1),(0,2),(1,2)]);P=math.prod(v)
 return (S*E+P)**2-S*S*P*(4*S-P)
def elim(v):
 S=sum(v);d=[(S-x)/2 for x in v];q=[1-x*x for x in d]
 return (1+sum(x*x for x in q)-2*sum(q)-2*sum(q[i]*q[j] for i,j in [(0,1),(0,2),(1,2)]))**2-64*math.prod(q)
def vp(q,p):
 q=Q(q)
 if not q:return 99999
 def val(n):
  n=abs(n);a=0
  while n%p==0:n//=p;a+=1
  return a
 return val(q.numerator)-val(q.denominator)
def mq(q,m):
 q=Q(q);return q.numerator*pow(q.denominator,-1,m)%m
def lift(cs,p,r,d):
 mod=p
 for j in range(1,d):
  rr=[r+k*mod for k in range(p) if sum(c*(r+k*mod)**i for i,c in enumerate(cs))%(p*mod)==0]
  assert len(rr)==1;r=rr[0];mod*=p
 return r
def chi(x,p):
 x%=p;return 0 if not x else (1 if pow(x,(p-1)//2,p)==1 else -1)

generic=[]
for a in range(-5,6):
 for b in range(-5,6):
  for c in range(-5,6):
   v=[Q(a,3),Q(b,4),Q(c,5)]
   assert elim(v)==surf(v)
   generic.append(dict(v=list(map(str,v)),identity=True))

phases=[]
for m in range(2,32):
 for n in range(1,m):
  if math.gcd(m,n)>1:continue
  x=Q(m*m-n*n,m*m+n*n);y=Q(2*m*n,m*m+n*n);D=x.denominator;d=2*x*y
  assert y.denominator==D and d.denominator==D*D and D%2==1
  assert (1+d).denominator==D*D==(1-d).denominator
  assert sq(1+d) and sq(1-d)
  phases.append(dict(x=str(x),y=str(y),D=D,denominator_square=True))

# Unit-circle triples verify the eliminant/sign equivalence OFF the sphere too.
torus=[]
sample=[(Q(q['x']),Q(q['y'])) for q in phases[:10]]
for xyz in itertools.product(sample,repeat=3):
 d=[2*x*y for x,y in xyz];S=sum(d);v=[S-2*a for a in d];delta=[x*x-y*y for x,y in xyz]
 branches=[e for e in itertools.product([-1,1],repeat=3) if 1+sum(e[i]*delta[i] for i in range(3))==0]
 pol=math.prod(1+sum(e[i]*delta[i] for i in range(3)) for e in itertools.product([-1,1],repeat=3))
 assert pol==surf(v)==elim(v)
 assert bool(branches)==(surf(v)==0)
 if branches:assert len(branches)==1
 torus.append(dict(on_surface=(surf(v)==0),signed_branches=len(branches),physical_endpoint=False))

boundary=[]
for row in phases:
 x=Q(row['x']);y=Q(row['y']);xs=[x,y,Q(0)];ys=[y,x,Q(1)]
 d=[2*xs[i]*ys[i] for i in range(3)];S=sum(d);v=[S-2*z for z in d]
 assert surf(v)==0 and elim(v)==0
 qs=[math.isqrt(z.denominator) for z in d];R=math.lcm(*qs)
 assert all(qs[i]**2==d[i].denominator for i in range(3))
 e=[int(R*z) for z in xs];h=[math.gcd(R,z) for z in e];tau=math.gcd(*qs)
 assert R==row['D'] and R%2==1 and sum(z*z for z in e)==R*R
 assert qs==[R//z for z in h] and math.prod(qs)==tau*R*R
 assert tau==Q(math.prod(qs),R*R) and R==math.prod(h)*tau
 assert all(math.gcd(h[i],h[j])==1 for i,j in [(0,1),(0,2),(1,2)])
 delta=[xs[i]**2-ys[i]**2 for i in range(3)]
 count=sum(1+sum(eps[i]*delta[i] for i in range(3))==0 for eps in itertools.product([-1,1],repeat=3))
 assert count>1 # zero-edge mask is material; no uniqueness claim here.
 boundary.append(dict(R=R,D=qs,content=h,tau=tau,zero_edge=True,signed_branches=count,physical_endpoint=False))

# Old G local cubic/rootline data can survive, but equal-tau physical denominators cannot.
local=[]
for p in [17,41,73,89,97,113]:
 for rho in [r for r in range(p) if (r*r+1)%p==0]:
  for lam in range(1,5):
   L=2*lam;n=2*L;depth=6*L+6;mod=p**depth
   root=lift([1,0,1],p,rho,n)
   u=next(root+k*p**n for k in range(p) if vp(1+(root+k*p**n)**2,p)==n and chi(((1+(root+k*p**n)**2)//p**n)%p,p)==1)
   A=1+u*u
   for hdepth in [L,L+1,2*L]:
    S=Q(u,2)+p**hdepth;E=4*u*(S-u)/A;P=4*u*u*S/A
    g=[p**n*z for z in [-P,E,-S,Q(1)]]
    V=lift([mq(z,mod) for z in g],p,(-u)%p,depth)
    assert vp(V+u,p)>=L and vp(V*V+1,p)>=L
    pole=[-P*p**(3*L),E*p**(2*L),-S*p**L,Q(1)]
    roots=[r for r in range(1,p) if sum(mq(z,p)*r**i for i,z in enumerate(pole))%p==0]
    assert len(roots)==2
    vs=[V]+[Q(lift([mq(z,mod) for z in pole],p,r,depth),p**L) for r in roots]
    ds=[(S-v)/2 for v in vs]
    val=[vp(z,p) for z in ds];assert val==[0,-L,-L]
    inferred_D_depth=[max(0,-z)//2 for z in val]
    assert inferred_D_depth==[0,lam,lam] and inferred_D_depth!=[lam]*3
    local.append(dict(p=p,lambda_=lam,old_G_rootline=True,pole_split=True,norm_unit_square=True,d_valuations=val,inferred_hypotenuse_depths=inferred_D_depth,required_fresh_depths=[lam]*3,equal_tau_physical_compatible=False,physical_endpoint=False))

out=dict(status='PASS',generic_eliminant_cases=len(generic),primitive_unit_circle_denominator_cases=len(phases),rational_torus_sign_cases=len(torus),zero_edge_boundary_cases=len(boundary),old_G_local_impostor_cases=len(local),physical_endpoints_enumerated=0,global_counting_credit=0,generic_cases=generic,phase_cases=phases,torus_cases=torus,boundary_cases=boundary,local_cases=local)
Path(__file__).with_name('M3-T11-134-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,list)}))
