"""Exact replay of153's counting ingredients, not a perfect-cuboid search."""
from itertools import product
from math import comb, gcd, isqrt
from fractions import Fraction
from pathlib import Path
import json

def mul(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def conj(z): return z[0],-z[1]
def norm(z): return z[0]*z[0]+z[1]*z[1]
def power(z,n):
    ans=(1,0)
    for _ in range(n): ans=mul(ans,z)
    return ans
def exact_div(z,w):
    num=mul(z,conj(w)); d=norm(w)
    assert num[0]%d==num[1]%d==0
    return num[0]//d,num[1]//d
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def gaussians(m):
    return [(a,b) for a in range(-m,m+1) for b in range(-m,m+1) if a*a+b*b==m*m]
def divisor_weight(m):
    ans=1
    for a in factors(m).values():ans*=2*a+1
    return ans

for a in range(1001):
    assert (2*a+1)**3<=comb(a+26,26)
    assert (2*a+1)**3*(a+27)-(2*a+3)**3*(a+1)==184*a**3+240*a*a+82*a

divisor_checks=[]
for Y in [1,2,5,10,25,100,250]:
    total_d=total_tau=0
    for m in range(1,Y+1):
        t=1
        for a in factors(m).values():t*=comb(a+26,26)
        d=divisor_weight(m)**3
        assert d<=t
        total_d+=d;total_tau+=t
    H=sum((Fraction(1,a) for a in range(1,Y+1)),Fraction(0))
    assert total_d<=total_tau<=Y*H**26
    divisor_checks.append({'Y':Y,'sum_D_cubed':total_d,'sum_tau27':total_tau})

cofactor_checks=[]; examples=[];total_tuples=0
for m in [1,5,13,17,25,29,37,41,65]:
    H=gaussians(m);D=divisor_weight(m)
    assert len(H)==4*D
    assert 3*len(H)**2+len(H)**3<=112*D**3
    sq=[mul(z,z) for z in H];cache={};zeros=valid=0;largest=0
    for r in (2,3):
        for gs in product(sq,repeat=r):
            total_tuples+=1
            C=(sum(z[0] for z in gs),sum(z[1] for z in gs));N=norm(C)
            if N==0:zeros+=1;continue
            valid+=1
            assert N<=r*r*m**4
            if N not in cache:
                cache[N]=[p for p,a in factors(N).items() if a>=2 and p%4==1 and gcd(p,m)==1]
            ps=cache[N];largest=max(largest,len(ps))
            # Exact version of the logarithmic prime budget: distinct p>=5.
            assert 25**len(ps)<=N<=9*m**4
            prod_p2=1
            for p in ps:prod_p2*=p*p
            assert N%prod_p2==0
            if ps and len(examples)<12:examples.append({'m':m,'r':r,'C':C,'norm_C':N,'primes':ps})
    cofactor_checks.append({'m':m,'gaussians':len(H),'nonzero_tuples':valid,'discarded_zero_tuples':zeros,'max_candidate_primes':largest})

roundtrips=0;exponent_checks=0
for p,pi in [(5,(2,1)),(13,(3,2)),(17,(4,1)),(29,(5,2))]:
    assert norm(pi)==p
    for m in [1,5,13,17,25]:
        if gcd(m,p)>1:continue
        for n in range(1,5):
            q=power(conj(pi),2*n);R=m*p**n
            for G in gaussians(m):
                H=mul(q,G)
                assert norm(H)==R*R and H[0]%p!=0
                assert exact_div(H,q)==G
                assert H[0]==conj(H)[0]
                roundtrips+=1
        for B in [10,100,1000,10000]:
            enumerated=[];n=1
            while m*p**n<=B:enumerated.append(n);n+=1
            assert 5**len(enumerated)<=B
            assert enumerated==[n for n in range(1,30) if m*p**n<=B]
            exponent_checks+=1

# Dropping positive-edge/C!=0 is invalid: (0,3,4;R=5) is a boundary tuple.
pi=(2,1);q=power(conj(pi),2)
H2=(3,-4);H3=(4,3)
G2=exact_div(H2,q);G3=exact_div(H3,q)
assert norm(G2)==norm(G3)==1
C2=mul(G2,G2);C3=mul(G3,G3)
assert (C2[0]+C3[0],C2[1]+C3[1])==(0,0)
assert 5*5-3*3-4*4==0

# Exponent/log budget is symbolic arithmetic, not a finite-height asymptotic test.
assert 30-27-1==2
assert Fraction(1,4)<Fraction(1,3)
out={'status':'PASS','scope':'counting-ingredient replay; uniform theorem is the written proof; no cuboid nonexistence inference',
     'local_inequality_checks':1001,'divisor_sum_checks':divisor_checks,
     'cofactor_checks':cofactor_checks,'enumerated_G_tuples':total_tuples,
     'candidate_examples':examples,'orientation_roundtrips':roundtrips,
     'exponent_budget_checks':exponent_checks,'zero_edge_boundary_C_zero_confirmed':True,
     'explicit_log_saving_power':2,'global_gate_closed':False}
dest=Path(__file__).with_name('verification153.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['candidate_examples','divisor_sum_checks','cofactor_checks']},indent=2))
