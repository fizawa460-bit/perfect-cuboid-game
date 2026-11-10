import json,math
from fractions import Fraction as Q
from pathlib import Path

def vp_int(n,p):
 if not n:return 99999
 n=abs(n);v=0
 while n%p==0:n//=p;v+=1
 return v

def vp(q,p):
 q=Q(q)
 return vp_int(q.numerator,p)-vp_int(q.denominator,p) if q else 99999

def modq(q,mod):
 q=Q(q);return q.numerator*pow(q.denominator,-1,mod)%mod

def lift(cs,p,x,depth):
 modulus=p
 for j in range(1,depth):
  opts=[x+t*modulus for t in range(p) if sum(c*(x+t*modulus)**i for i,c in enumerate(cs))%(modulus*p)==0]
  assert len(opts)==1
  x=opts[0];modulus*=p
 return x

rows=[]
for p in [5,13,17,29]:
 rho=next(x for x in range(p) if (x*x+1)%p==0)
 for lam in range(1,6):
  for cdepth in range(1,2*lam):
   n=2*lam+cdepth;k=2*lam-cdepth
   u=lift([1,0,1],p,rho,n)
   if vp_int(u*u+1,p)>n:u+=p**n
   assert vp_int(u*u+1,p)==n
   for su in [1,2]:
    S=Q(su,p**k);A=1+u*u;E=4*u*S/A-Q(4*u*u,A);P=4*u*u*S/A
    f=[-P,E,-S,Q(1)];g=[p**(4*lam)*v for v in f]
    assert [vp(v,p) for v in g]==[0,0,n,4*lam]
    fu=sum(f[i]*u**i for i in range(4))
    assert vp(fu,p)==-n
    depth=n+2*lam+4;mod=p**depth
    cs=[modq(v,mod) for v in g]
    assert sum(cs[i]*rho**i for i in range(4))%p==0
    root=lift(cs,p,rho,depth)
    assert vp_int(root-u,p)==k
    normdepth=vp_int(root*root+1,p)
    assert normdepth==k<2*lam
    rows.append(dict(p=p,lambda_=lam,c_p=cdepth,n=n,k=k,S_unit=su,unit_root_modulus=depth,
      unit_root=root,root_minus_u_valuation=k,root_norm_valuation=normdepth,required_depth=2*lam,physical_rootline=False))
#129 nested AP: preservesS4/squareN; p5 interior lambda2,c2 but rootline fails.
examples=[]
for j in range(26):
 r=932+41250*j;a=2*r;b=r*r-1;c=r*r+1;u=Q(a,b);A=1+u*u;q=Q(1,625)
 assert (r-8)%66==0 and math.gcd(a,b)==1 and a*a+b*b==c*c and vp_int(c,5)==3
 S=A*q*q/(8*u*u);z=S/2;E=4*u*S/A-Q(4*u*u,A);P=4*u*u*S/A
 assert (vp(A,5),vp(q,5),vp(S,5),vp(z,5))==(6,-4,-2,-2)
 assert math.isqrt(z.numerator)**2==z.numerator and math.isqrt(z.denominator)**2==z.denominator
 #q-scaled cubic reducesY(Y²+1), with simple roots0,2,3 mod5.
 scaled=[-P/q**3,E/q**2,-S/q,Q(1)]
 assert [modq(v,5) for v in scaled]==[0,1,0,1]
 assert all((3*y*y+1)%5 for y in [0,2,3])
 g=[5**8*v for v in [-P,E,-S,Q(1)]];mod=5**14
 root=lift([modq(v,mod) for v in g],5,modq(u,5),14)
 assert vp_int(root*root+1,5)==2
 F=lambda x:(a*a+b*b)*x**4-8*a*b*x**3+(11*a*a-b*b)*x*x+6*a*b*x-a*a
 residual=-F(z)/Q(a*a+b*b)
 assert vp(residual,5)==-12
 unit=residual*5**12
 assert modq(unit,5) in [1,4]
 examples.append(dict(r=r,a=a,b=b,c=c,z=str(z),q=str(q),residual_Q5_square=True,
  cubic_Q5_split=True,genus3_Q5_lift=True,required_rootline_depth=4,actual_depth=2,physical=False))
out=dict(status='PASS',synthetic_allocations=len(rows),nested_AP_cases=len(examples),
 all_interior_unit_rootlines_failed=True,physical_endpoints_enumerated=0,
 global_counting_credit=0,allocations=rows,AP_examples=examples)
Path(__file__).with_name('M3-T11-130-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['allocations','AP_examples']}))
