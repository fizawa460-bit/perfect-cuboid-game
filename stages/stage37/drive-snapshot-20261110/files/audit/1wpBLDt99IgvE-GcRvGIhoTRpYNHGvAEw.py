import json
from fractions import Fraction as Q
from pathlib import Path

def val(q,p):
 q=Q(q)
 if not q:return 99999
 def v(n):
  n=abs(n);s=0
  while n%p==0:s+=1;n//=p
  return s
 return v(q.numerator)-v(q.denominator)

def mq(q,m):
 q=Q(q);return q.numerator*pow(q.denominator,-1,m)%m

def lift(cs,p,r,depth):
 power=p
 for j in range(1,depth):
  opts=[r+t*power for t in range(p) if sum(c*(r+t*power)**i for i,c in enumerate(cs))%(power*p)==0]
  assert len(opts)==1,(p,j,r)
  r=opts[0];power*=p
 return r

def choose_u(p,n,unit_square):
 rho=next(x for x in range(p) if (x*x+1)%p==0)
 r=lift([1,0,1],p,rho,n)
 for t in range(p):
  u=r+t*p**n;A=1+u*u
  if val(A,p)==n and (pow((A//p**n)%p,(p-1)//2,p)==1)==unit_square:return u
 raise AssertionError()

def cubic(u,S):
 A=1+u*u;E=4*u*S/A-Q(4*u*u,A);P=4*u*u*S/A
 return [-P,E,-S,Q(1)]

rows=[];D=[];G=[]
for p in [5,13,17,29,41]:
 for lam in range(1,5):
  L=2*lam;depth=4*L+6;mod=p**depth
  for square_unit in [False,True]:
   u=choose_u(p,L,square_unit);A=1+u*u
   for su in range(1,p):
    S=Q(su,p**L);f=cubic(u,S);g=[p**(2*L)*c for c in f]
    assert [val(c,p) for c in g]==[0,0,L,2*L]
    root=lift([mq(c,mod) for c in g],p,u%p,depth)
    assert val(root-u,p)>=L and val(root*root+1,p)>=L
    # Pole scaling; simple nonzero roots lift iff its discriminant is a nonzero square.
    scaled=[p**(3*L-i*L)*f[i] for i in range(4)]
    red=[mq(c,p) for c in scaled];assert red[0]==0 and red[3]==1
    roots=[x for x in range(1,p) if sum(red[i]*x**i for i in range(4))%p==0]
    discr=(red[2]**2-4*red[1])%p
    assert (len(roots)==2)==(discr!=0 and pow(discr,(p-1)//2,p)==1)
    D.append(dict(p=p,lambda_=lam,A_unit_square=square_unit,S_unit=su,unit_rootline=True,orientation='plus_u',simple_pole_roots=len(roots)))
   u=choose_u(p,2*L,square_unit);A=1+u*u;A0=mq(Q(A,p**(2*L)),p)
   for h in range(L+2):
    S=Q(u,2)+p**h
    if val(S,p)!=0 or val(S-u,p)!=0:continue
    f=cubic(u,S);g=[p**(2*L)*c for c in f]
    assert [val(c,p) for c in g]==[0,0,2*L,2*L]
    r0=mq(Q(u)*S/(S-u),p)
    root=lift([mq(c,mod) for c in g],p,r0,depth)
    passes=val(root*root+1,p)>=L
    congr=val(2*S-u,p)>=L
    assert passes==congr
    if congr:
     assert val(root+u,p)>=L
     scaled=[p**(3*L-i*L)*f[i] for i in range(4)]
     red=[mq(c,p) for c in scaled]
     assert red==[0,mq(Q(2,A0),p),0,1]
     poles=[r for r in range(1,p) if sum(red[i]*r**i for i in range(4))%p==0]
     assert (len(poles)==2)==(pow(mq(Q(-2,A0),p),(p-1)//2,p)==1)
     for r in poles:
      rr=lift([mq(c,mod) for c in scaled],p,r,depth)
      assert val(Q(rr,p**L),p)==-L
    G.append(dict(p=p,lambda_=lam,A_unit_square=square_unit,perturbation_depth=h,rootline=passes,congruence=congr))
   S=Q(u,2);f=cubic(u,S)
   scaled=[p**(3*L-i*L)*f[i] for i in range(4)]
   red=[mq(c,p) for c in scaled]
   assert red==[0,mq(Q(2,A0),p),0,1]
   roots=[r for r in range(p) if sum(red[i]*r**i for i in range(4))%p==0]
   split=pow(mq(Q(-2,A0),p),(p-1)//2,p)==1
   assert (len(roots)==3)==split
   if square_unit:assert split==(p%8==1)
   if split:
    cs=[mq(c,mod) for c in scaled]
    lifted=[lift(cs,p,r,depth) for r in roots]
    assert sorted(val(Q(r,p**L),p) for r in lifted)==[-L,-L,0]
    unit=next(Q(r,p**L) for r in lifted if val(Q(r,p**L),p)==0)
    assert val(unit*unit+1,p)>=L
   rows.append(dict(p=p,lambda_=lam,A_unit_square=square_unit,S='u/2',pole_split=split,
    square_unit_pmod8_rule=(not square_unit or split==(p%8==1)),physical_endpoint=False))

out=dict(status='PASS',denominator_cases=len(D),gaussian_congruence_cases=len(G),
 gaussian_pole_cases=len(rows),denominator_rootline_automatic=True,gaussian_rootline_iff_2S_eq_u=True,
 squareN_gaussian_fresh_primes_require_p1mod8=True,physical_endpoints_enumerated=0,global_counting_credit=0,
 denominator=D,gaussian_congruence=G,gaussian_poles=rows)
Path(__file__).with_name('M3-T11-131-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['denominator','gaussian_congruence','gaussian_poles']}))
