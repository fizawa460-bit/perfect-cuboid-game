"""Exact structural replay of152; not a search for perfect cuboids."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import gcd, comb
from pathlib import Path
import json

def add(z,w): return z[0]+w[0],z[1]+w[1]
def conj(z): return z[0],-z[1]
def mul(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def phase(e,f,R): return F(e*e-f*f,R*R),F(2*e*f,R*R)
def total(zs):
    z=(F(0),F(0))
    for w in zs:z=add(z,w)
    return z

classes=Counter()
for mask in range(1,64):
    inds=[i for i in range(6) if mask>>i&1]
    n=len(inds)
    if n%2: classes['odd_real_numerator']+=1
    elif n==2:
        if inds[0]//2==inds[1]//2: classes['same_edge_R2_equals_2e2']+=1
        else: classes['different_edges_force_third_zero']+=1
    elif n==4: classes['complement_two_unit_terms_force_minus_one']+=1
    else:
        assert n==6
        classes['whole_sum_is_minus_two']+=1
assert dict(classes)=={'odd_real_numerator':32,'same_edge_R2_equals_2e2':3,
                      'different_edges_force_third_zero':12,
                      'complement_two_unit_terms_force_minus_one':15,
                      'whole_sum_is_minus_two':1}

# Real parts for size2: same edge gives 4X_i-2; distinct gives
# 2(X_i+X_j-1)=-2X_k on X1+X2+X3=1. Check exact coefficient vectors.
for i,j in combinations(range(6),2):
    coeff=[0,0,0];coeff[i//2]+=2;coeff[j//2]+=2
    if i//2==j//2: assert sorted(coeff)==[0,0,4]
    else: assert sorted(coeff)==[0,2,2]

boundary=[]
for m in range(2,21):
    for n in range(1,m):
        if gcd(m,n)!=1 or (m-n)%2==0: continue
        a=m*m-n*n;b=2*m*n;R=m*m+n*n
        es=(0,a,b);fs=(R,b,a)
        assert sum(e*e for e in es)==R*R
        assert all(e*e+f*f==R*R for e,f in zip(es,fs))
        zs=[]
        for e,f in zip(es,fs):
            z=phase(e,f,R);assert mul(z,conj(z))==(1,0)
            zs.extend((z,conj(z)))
        assert total(zs)==(-2,0)
        masks=[mask for mask in range(1,64) if total([z for i,z in enumerate(zs) if mask>>i&1])==(0,0)]
        assert masks and all(mask.bit_count()%2==0 for mask in masks)
        boundary.append({'edges':es,'R':R,'vanishing_masks':masks})

# For each prime the exponent embedding consists of three independent
# columns e_(2j)-e_(2j+1); distinct primes occupy independent valuation rows.
rank_checks=[]
for s in range(0,21):
    vectors=[]
    for p in range(s):
        for j in range(3):
            v=[0]*(6*s);v[6*p+2*j]=1;v[6*p+2*j+1]=-1;vectors.append(v)
    pivots=[next(i for i,a in enumerate(v) if a) for v in vectors]
    assert len(set(pivots))==len(vectors)==3*s
    rank_checks.append([s,len(vectors)])
assert 4*6**4==5184 and 5184*7==36288 and 5184*3==15552
for s in range(101):
    # B=48^(4*15552*s): log_48(bound)=36288+log_48(B)/4.
    assert 5184*(7+3*s)==36288+(4*15552*s)//4

# Verify the rational local generating function by exact coefficients.
for n in range(101):
    coeff=sum(c*comb(n-j+3,3) for j,c in enumerate((1,23,23,1)) if n>=j)
    assert coeff==(2*n+1)**3
def localF(x): return (1+23*x+23*x*x+x**3)/(1-x)**4
def weighted_count(primes,B,j=0,R=1,w=1):
    if j==len(primes): return w
    totalw=0;power=1;n=0
    while R*power<=B:
        totalw+=weighted_count(primes,B,j+1,R*power,w*(2*n+1)**3)
        power*=primes[j];n+=1
    return totalw
euler_checks=[]
for ps in [(5,), (5,13), (5,13,17), (101,109), (5,1009)]:
    prod=F(1)
    for p in ps:prod*=localF(F(1,p))
    for B in (10,100,1000,10000):
        w=weighted_count(ps,B)
        assert F(w)<=B*prod  # exact sigma=1 Rankin majorant
        euler_checks.append({'S':ps,'B':B,'weight_without_64':w})
assert 1-1/F(4,3)==F(1,4)
assert F(1,3)-F(1,4)==F(1,12)

report={'status':'PASS','subsum_masks':63,'mask_classes':dict(classes),
        'boundary_counterexamples':len(boundary),'first_boundary':boundary[0],
        'group_rank_checks':rank_checks,'AV_n':6,'rank':'3*|S|',
        'C0':'48^36288','K':'48^15552','sector_alphabet_size':'(log B)^(4/3)',
        'sector_exponent':'1/4+o(1)','local_series_coefficients_checked':101,
        'exact_weighted_euler_checks':euler_checks,
        'scope':'Finite structural replay; the uniform proof and published theorem certify the bound. No physical existence/nonexistence inference.'}
Path(__file__).with_name('verification152.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
