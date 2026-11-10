import json, math, random
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import itertools
def padd(x,y):
    z=x.copy()
    for k,v in y.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def pscale(x,c):return {k:v*c for k,v in x.items() if v*c}
def pmul(x,y):
    z={}
    for (i,j),v in x.items():
        for (k,l),w in y.items():z[i+k,j+l]=z.get((i+k,j+l),0)+v*w
    return {k:v for k,v in z.items() if v}
aa={(2,0):1,(0,0):-1}; ab={(1,0):4}; ac=pscale(aa,-1)
ba={(0,2):1,(0,0):-1}; bb={(0,1):4}; bc=pscale(ba,-1)
matrix=[[aa,ab,ac,{}],[{},aa,ab,ac],[ba,bb,bc,{}],[{},ba,bb,bc]]
res={}
for perm in itertools.permutations(range(4)):
    sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    v={(0,0):sign}
    for i in range(4):v=pmul(v,matrix[i][perm[i]])
    res=padd(res,v)
aminusb={(1,0):1,(0,1):-1}; aplusb={(1,1):1,(0,0):1}
expected=pscale(pmul(pmul(aminusb,aminusb),pmul(aplusb,aplusb)),-16)
assert res==expected

def factorint(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def divisors(n):
    ds=[1]
    for p,e in factorint(n).items():ds=[d*p**k for d in ds for k in range(e+1)]
    return ds

def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cj(x): return (x[0],-x[1])
def phase(x,y): return (F(x*x-y*y,x*x+y*y),F(2*x*y,x*x+y*y))
rng=random.Random(171)
identity_checks=0
for _ in range(2000):
    rr=[phase(rng.randint(1,100),rng.randint(-100,100)) for _ in range(3)]
    A=[sum(mul(r,r)[k] for r in rr) for k in range(2)]
    traces=[2*mul(rr[i],cj(rr[j]))[0] for i,j in [(0,1),(0,2),(1,2)]]
    assert A[0]*A[0]+A[1]*A[1]-1==math.prod(traces)
    identity_checks+=1

phase_reps=defaultdict(list)
for x in range(1,142):
    for y in range(-141,142):
        if x*x+y*y<=20000 and math.gcd(x,y)==1:
            phase_reps[phase(x,y)].append((x,y))
assert max(map(len,phase_reps.values()))==1

sigma_checks=0
primes=[5,13,17,29,37,41,53,61,73,89]
for _ in range(10000):
    ns=[1]*4
    for p in primes:
        if rng.randrange(3)==0: ns[rng.randrange(4)]*=p**rng.randint(1,3)
    hs=[rng.choice([1,5,13,17]) for _ in range(3)]
    H=math.prod(hs); tau=math.prod(ns); R=H*tau
    j=max(range(1,4),key=lambda k:(ns[k],-k))
    mu=math.prod(ns[k] for k in range(1,4) if k!=j)
    sigma=H*mu
    assert R==sigma*ns[0]*ns[j] and R%sigma==0
    assert mu**3<=math.prod(ns[1:])**2
    assert sigma**3<=H*R*R
    sorted_rel=sorted(ns[1:])
    assert sorted_rel[1]**2>=mu and sorted_rel[2]**2>=mu
    sigma_checks+=1

def tuple_count(n,k):
    if k==1:return 1
    return sum(tuple_count(n//d,k-1) for d in divisors(n))
tuple_checks=0
for n in range(1,301):
    expected=math.prod(math.comb(e+4,4) for e in factorint(n).values())
    assert tuple_count(n,5)==expected
    tuple_checks+=1

# Logical countermodel only: multiplicity log(B) is subpolynomial.
# A support of B^(1/3)/log(B) is little-o, but weighted count is asymptotic B^(1/3).
counter=[]
for k in [12,18,24,30]:
    B=10**k; m=math.ceil(math.log(B)); root=10**(k//3)
    support=root//m
    counter.append({'B':str(B),'support':support,'multiplicity':m,'endpoint_over_B_one_third':F(m*support,root).__str__()})

result={'status':'PASS','scope':'finite algebra and packet combinatorics; not a physical endpoint census; not proof of uniform elliptic input',
        'resultant':'-16*(a-b)^2*(a*b+1)^2; exact integer polynomial determinant verified','trace_identity_checks':identity_checks,
        'primitive_gaussian_phase_checks':sum(map(len,phase_reps.values())),
        'synthetic_norm_bundle_checks':sigma_checks,'ordered_five_factor_checks':tuple_checks,
        'little_o_countermodel':counter,'physical_endpoints_enumerated':0}
Path('M3-T11-171-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
