import json,math
from fractions import Fraction as Q
from pathlib import Path

def square(q):
 q=Q(q)
 return q>=0 and math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator
def vp(q,p):
 q=Q(q)
 if not q:return 99999
 def v(n):
  n=abs(n);z=0
  while n%p==0:n//=p;z+=1
  return z
 return v(q.numerator)-v(q.denominator)
def mq(q,m):
 q=Q(q);return q.numerator*pow(q.denominator,-1,m)%m
def lift(cs,p,r,d):
 mod=p
 for j in range(1,d):
  rr=[r+h*mod for h in range(p) if sum(c*(r+h*mod)**i for i,c in enumerate(cs))%(p*mod)==0]
  assert len(rr)==1;r=rr[0];mod*=p
 return r
def chi(a,p):
 a%=p
 return 0 if not a else (1 if pow(a,(p-1)//2,p)==1 else -1)

finite=[]
for p in range(5,1000,4):
 if any(p%d==0 for d in range(2,math.isqrt(p)+1)):continue
 for rho in range(p):
  if (rho*rho+1)%p:continue
  plus=(1+3*rho*pow(4,-1,p))%p;minus=(1-3*rho*pow(4,-1,p))%p
  assert ((3+rho)**2-8*plus)%p==0 and ((3-rho)**2-8*minus)%p==0
  ch=[chi(plus,p),chi(minus,p)]
  if p%8==5:assert -1 in ch
  else:assert ch==[1,1]
  finite.append(dict(p=p,rho=rho,classes=ch,rejected=(p%8==5)))

local=[]
for p in [5,13,17,29,37,41,53,73,89,97]:
 for rho in [i for i in range(p) if (i*i+1)%p==0]:
  for lam in [1,2,3]:
   L=2*lam;n=2*L;mod=p**(6*L+6)
   base=lift([1,0,1],p,rho,n)
   u=next(base+k*p**n for k in range(p) if vp(1+(base+k*p**n)**2,p)==n and chi(-2*pow(((1+(base+k*p**n)**2)//p**n)%p,-1,p),p)==1)
   A=1+u*u;A0=Q(A,p**n)
   for h in [L,L+1,2*L]:
    S=Q(u,2)+p**h;E=4*u*(S-u)/A;P=4*u*u*S/A
    g=[p**n*c for c in [-P,E,-S,Q(1)]]
    V=lift([mq(c,mod) for c in g],p,(-u)%p,6*L+6)
    assert vp(V+u,p)>=L and vp(V*V+1,p)>=L
    pole=[-P*p**(3*L),E*p**(2*L),-S*p**L,Q(1)]
    rs=[j for j in range(p) if sum(mq(c,p)*j**i for i,c in enumerate(pole))%p==0]
    assert len(rs)==3
    for j in rs:lift([mq(c,mod) for c in pole],p,j,4*L+4)
    d=(S-V)/2;ch=[chi(mq(1+d,p),p),chi(mq(1-d,p),p)]
    if p%8==5:assert -1 in ch
    else:assert ch==[1,1]
    local.append(dict(p=p,rho=rho,lambda_=lam,H_depth=h,pole_split=True,old_rootline=True,target_square_classes=ch,new_exclusion=(p%8==5),physical_endpoint=False))

enlargement=[]
for m in range(1,41):
 for n in range(1,21):
  if math.gcd(m,n)!=1:continue
  r=Q(m,n);u=(r*r-2)/(2*r);w=(r*r+2)/(2*r);A=1+u*u
  vv=[2*u/A,(-2*u+2*u*w)/A,(-2*u-2*u*w)/A];S=sum(vv)
  tests=[1+sgn*(S-v)/2 for v in vv for sgn in [1,-1]]
  assert math.prod(tests[::2])==(2+S+S*u)**2/(4*A)
  assert math.prod(tests[1::2])==(2-S+S*u)**2/(4*A)
  assert (2+S+S*u) or (2-S+S*u)
  if all(map(square,tests)):assert square(A)
  s,t=S.numerator,S.denominator
  for v in vv:
   ai,bi=v.numerator,v.denominator
   for sign in [1,-1]:
    J=2*t*bi*(2*t*bi+sign*(s*bi-t*ai))
    assert square(J)==square(1+sign*(S-v)/2)
  enlargement.append(dict(u=str(u),norm_square=square(A),all_six_squares=all(map(square,tests)),physical_endpoint=False))

# Exact rational boundary spheres: verify forward/reverse lift and primitive R.
# One edge is zero, so these are deliberately NOT positive physical endpoints.
boundary=[]
for m in range(2,31):
 for n in range(1,m):
  if math.gcd(m,n)!=1:continue
  x=[Q(m*m-n*n,m*m+n*n),Q(2*m*n,m*m+n*n),Q(0)]
  y=[x[1],x[0],Q(1)]
  h=[x[i]*y[i] for i in range(3)];v=[2*sum(h)-4*hi for hi in h];S=sum(v)
  lp=[x[i]+y[i] for i in range(3)];lm=[x[i]-y[i] for i in range(3)]
  assert all(lp[i]**2==1+(S-v[i])/2 and lm[i]**2==1-(S-v[i])/2 for i in range(3))
  assert sum(lp[i]*lm[i] for i in range(3))==-1
  assert [(lp[i]+lm[i])/2 for i in range(3)]==x
  R=math.lcm(*(q.denominator for q in x));edges=[int(q*R) for q in x]
  assert sum(e*e for e in edges)==R*R and math.gcd(R,*edges)==1
  assert all((q*R).denominator==1 for q in y)
  boundary.append(dict(R=R,edges=edges,positive=False))

out=dict(status='PASS',finite_field_cases=len(finite),split_local_gaussian_cases=len(local),rational_split_enlargement_cases=len(enlargement),boundary_reconstruction_cases=len(boundary),global_norm_square_product_identities=True,gaussian_5mod8_excluded_without_assuming_squareN=True,physical_endpoints_enumerated=0,global_counting_credit=0,finite_cases=finite,local_cases=local,enlargement_cases=enlargement,boundary_cases=boundary)
Path(__file__).with_name('M3-T11-133-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,list)}))
