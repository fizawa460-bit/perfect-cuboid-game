import json, math, itertools
from fractions import Fraction as Q
from pathlib import Path

# Exact rational Sturm arithmetic, ascending coefficients. No floating roots.
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def rem(p,d):
    p=p[:]
    while len(p)>=len(d) and any(p):
        c=p[-1]/d[-1]; k=len(p)-len(d)
        for j,v in enumerate(d): p[k+j]-=c*v
        trim(p)
    return p
def ev(p,x):
    v=Q(0)
    for c in reversed(p): v=v*x+c
    return v
def sturm(p):
    s=[p,[i*p[i] for i in range(1,len(p))]]
    while len(s[-1])>1:
        r=[-x for x in rem(s[-2],s[-1])]
        assert any(r)
        s.append(r)
    return s
def sg(x):return 1 if x>0 else -1 if x<0 else 0
def variations(s,x):
    signs=[]
    for p in s:
        v=sg(p[-1])*(-1 if x=='-' and (len(p)-1)%2 else 1) if isinstance(x,str) else sg(ev(p,x))
        if v:signs.append(v)
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def roots_below(s,x):return variations(s,'-')-variations(s,x)
def pattern(s):return ''.join('+' if v>0 else '-' for v in s)

rows=[]; four=two=0
for a in range(-24,25):
  if not a:continue
  for b in range(1,25):
    if math.gcd(a,b)!=1:continue
    N=a*a+b*b; D=2*b*b-25*a*a; u=Q(a,b)
    p=list(map(Q,[-a*a,6*a*b,11*a*a-b*b,-8*a*b,N]))
    s=sturm(p); r=roots_below(s,'+')
    assert r==(4 if D>0 else 2)
    four+=r==4; two+=r==2
    n0=roots_below(s,Q(0)); nu=roots_below(s,u)
    assert (n0,nu)==((1,2) if a>0 else ((3,2) if r==4 else (1,0)))
    assert ev(p,u)==Q(a*a*(a*a+2*b*b)**2,b**4)
    gamma=[1 if min(n0,nu)<=i<max(n0,nu) else -1 for i in range(r)]
    assert math.prod(gamma)==-1
    evals=[tuple([1]*j+[-1]*(r-j)) for j in range(1,r,2)]
    xis={tuple(e[i]*gamma[i] for i in range(r)) for e in evals}
    expected={(-1,-1,1,1),(-1,1,-1,1)} if r==4 else {(-1,-1) if a>0 else (1,1)}
    assert xis==expected
    odd={v for v in itertools.product([-1,1],repeat=r) if math.prod(v)==-1}
    quot=lambda v:min(v,tuple(-x for x in v))
    imageq={quot(e) for e in evals}
    gammaq=quot(tuple(gamma))
    assert (gammaq not in imageq)==(r==4)
    assert len(odd)==(8 if r==4 else 2)
    assert len(imageq)==(2 if r==4 else 1)
    # Norm-sign necessity is strictly weaker than ordered evaluation in r=4.
    assert ev(p,Q(0))<0
    rows.append(dict(a=a,b=b,Delta0=D,real_roots=r,below_zero=n0,below_u=nu,
      gamma=pattern(gamma),evaluation=[pattern(e) for e in evals],
      xi=sorted(pattern(v) for v in xis),gamma_excluded_mod_scalars=r==4))
out=dict(status='PASS',method='exact rational Sturm sequences and complete sign enumeration',
  packets=len(rows),four_real=four,two_real=two,physical_endpoints_enumerated=0,
  S4_Galois_groups_computed=False,class_groups_computed=False,global_counting_credit=0,packets_detail=rows)
Path(__file__).with_name('M3-T11-128-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='packets_detail'}))
