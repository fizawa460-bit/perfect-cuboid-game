import json,math
from fractions import Fraction as Q
from pathlib import Path

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

cases=[]
for m in range(1,41):
 for n in range(1,21):
  if math.gcd(m,n)!=1:continue
  r=Q(m,n);u=(r*r-2)/(2*r);w=(r*r+2)/(2*r);A=1+u*u
  roots=[2*u/A,(-2*u+2*u*w)/A,(-2*u-2*u*w)/A]
  S=sum(roots);E=sum(roots[i]*roots[j] for i,j in [(0,1),(0,2),(1,2)]);P=math.prod(roots)
  assert S==-2*u/A and E==4*u*(S-u)/A and P==4*u*u*S/A
  a,b=u.numerator,u.denominator;s,t=S.numerator,S.denominator;N=a*a+b*b
  Bs=[v.denominator for v in roots];As=[v.numerator for v in roots];D=math.prod(Bs)
  H=2*b*s-a*t;Wp=math.prod(a*Bi+b*Ai for Ai,Bi in zip(As,Bs))
  assert a*a*D*(4*b*b*H+N*(b*s+a*t))==N*t*Wp
  assert all(v*v<=8 for v in roots) and s*s<=72*t*t
  assert H and H*H<=289*t*t*N
  assert (D*math.gcd(4,N))%N==0 and math.lcm(*Bs)%t==0
  cases.append(dict(u=str(u),S=str(S),H=H,N=N,t=t,D=D,exact_product_identity=True,range_bound=True,physical_endpoint=False))

locals_=[]
for p in [5,13,17,29,41]:
 for lam in range(1,5):
  L=2*lam;n=2*L;rho=next(i for i in range(p) if (i*i+1)%p==0)
  u=lift([1,0,1],p,rho,n)
  if vp(u*u+1,p)>n:u+=p**n
  A=1+u*u;assert vp(A,p)==2*L
  for h in range(1,3*L+1):
   S=Q(u,2)+p**h;K=u*(4-A)-S*(A+8)
   H=(2*S-u).numerator
   f=[-4*u*u*S/A,4*u*(S-u)/A,-S,Q(1)]
   assert 4*(2*S-u)+A*(S+u)==-A*sum(f[i]*(-u)**i for i in range(4))/(u*u)
   depth=6*L+8;mod=p**depth;g=[p**(2*L)*v for v in f]
   V=lift([mq(v,mod) for v in g],p,(-u)%p,depth)
   assert vp(V+u,p)==vp(K,p)
   assert min(vp(H,p),2*L)==min(vp(V+u,p),2*L)
   assert (vp(H,p)>=L)==(vp(V+u,p)>=L)
   locals_.append(dict(p=p,lambda_=lam,h=h,H_depth=vp(H,p),target_plus_u_depth=vp(V+u,p),same_threshold=True,physical_endpoint=False))

out=dict(status='PASS',rational_split_enlargement_cases=len(cases),local_gaussian_cases=len(locals_),
 exact_pullback_identity=True,height_bound_17=True,physical_endpoints_enumerated=0,global_counting_credit=0,
 rational_cases=cases,local_cases=locals_)
Path(__file__).with_name('M3-T11-132-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['rational_cases','local_cases']}))
