#!/usr/bin/env python3
"""Exact stdlib replay: old unit12 lattice has a proper index-13 extension
and theta is a fourth power but not an eighth power in the fixed K=Q(theta).
Does not compute class groups, full units, true Selmer or MW upper.
"""
import json,hashlib,subprocess,sys
from pathlib import Path
F=Path(__file__).resolve().parent
C=json.loads((F/'unit_index13_theta4_certificate.json').read_text())
for name,checksum in C['parent_SHA256'].items():
    assert hashlib.sha256((F/name).read_bytes()).hexdigest()==checksum,(name,'SHA256 NOT MATCH')
old=subprocess.run([sys.executable,str(F/'verify_unit12_stdlib.py')],text=True,capture_output=True,timeout=120)
assert old.returncode==0,(old.stdout[-1800:],old.stderr[-1800:])
assert 'PASS 13x14 GF2 matrix rank13' in old.stdout
print('PASS old 12 independent unit group source SHA-locked and full replay verified')
D=json.loads((F/'unit12_certificate.json').read_text())
Q={u['name']:u for u in D['unit_definitions']}
h=D['h2_coefficients_ascending'];n=len(h)-1
assert n==36 and h[0]==1 and h[-1]==1
assert h==C['h2_coefficients_ascending']
assert D['expected_GF2_rank']==13
assert [u['name'] for u in D['unit_definitions']]==['epsilon','eta','sigma','alpha','rho','beta4','beta9','gamma8','gamma6','gamma12','tau3','upsilon3']
q2=Q['rho']['q'];q4=Q['beta4']['q'];q9=Q['beta9']['q'];a8=Q['gamma8']['q']
assert C['q_poly_ASC']=={'Q2_rho':q2,'Q4_beta4':q4,'Q9_beta9':q9,'A8_gamma8':a8}

def product(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):z[i+j]+=c*d
    return z

def modh(v):
    v=v[:]
    # independent coefficient indexing, monic order-36 relation
    while len(v)>n:
        c=v.pop()
        if c:
            offset=len(v)-n
            for i in range(n):v[offset+i]-=c*h[i]
    return v+[0]*(n-len(v))

def powerpoly(a,e):
    assert e>=0
    z=[1];b=a[:]
    while e:
        if e&1:z=modh(product(z,b))
        e//=2
        if e:b=modh(product(b,b))
    return modh(z)

lhs=[0,1]
lhs=powerpoly(lhs,13)
for q,e in [([1,1],8),(q2,8),(q4,8),(a8,68)]:
    lhs=modh(product(lhs,powerpoly(q,e)))
lhs=[(2**56)*z for z in lhs]
rhs=modh(product(powerpoly([1,3],60),powerpoly(q9,60)))
assert lhs==rhs,'FAILED exact 36-dimensional integer polynomial algebra identity'
check=hashlib.sha256(json.dumps(lhs,separators=(',',':')).encode()).hexdigest()
assert check==C['exact_mod_h2_poly_remainder_SHA256']
print('PASS exact integer identity modulo h2: θ^13=U^4; SHA256',check)
# Parent units epsilon, eta, alpha, rho, beta4, beta9, gamma8 are certified
# integral global units in old replay. theta is integral with norm h2(0)=1,
# so theta and U and V=U/theta^3 are global integral units.
exponents={'epsilon':5,'eta':15,'alpha':-2,'rho':-2,'beta4':-2,'beta9':15,'gamma8':-17}
assert exponents==C['unit_U_exponents_old'] and exponents['epsilon']%13!=0
# Basic algebra in the commutative unit group:
# theta^13=U^4, V=U theta^-3, hence
# V^4=U^4 theta^-12=theta, V^13=U^13 theta^-39=U.
# Old twelve units are multiplicatively Z-independent; therefore the
# coordinates of U are NOT all divisible by13. If V belonged to Gamma_0,
# U=V^13 would force every coordinate divisible by13. This contradiction
# and V^13 in Gamma_0 prove exactly [Gamma_0+<V>:Gamma_0]=13.
assert C['relative_index_<Gamma0,V>_over_Gamma0']==13
print('PASS index-13 superlattice, V^13=U, V^4=theta by exact group identities')
# Non-eighth-power certificate at p=61 and its degree-one prime theta -> 47.
p=61;t=47
assert sum(c*pow(t,i,p) for i,c in enumerate(h))%p==0
assert sum(i*c*pow(t,i-1,p) for i,c in enumerate(h) if i)%p==49
# 61 is unramified in K since p not among exact disc factors.
# V expressed via old units, denominator nonzero mod 61.
def evaluate(a):return sum(int(z)*pow(t,i,p) for i,z in enumerate(a))%p
N=(pow(3*t+1,15,p)*pow(evaluate(q9),15,p))%p
E=(pow(2,14,p)*pow(t,3,p)*pow(t+1,2,p)*pow(evaluate(q2),2,p)*pow(evaluate(q4),2,p)*pow(evaluate(a8),17,p))%p
assert (N,E)==(1,21)
v=N*pow(E,-1,p)%p
assert v==32 and pow(v,4,p)==t and pow(v,(p-1)//2,p)==p-1
assert pow((-v)%p,(p-1)//2,p)==p-1
assert C['prime61']['V_modp']==v
# If theta=w^8 in K, then V^4=w^8 implies V/w^2 in μ_4(K).
# K admits real embeddings, so μ_4(K)={+1,-1}. But neither ±V
# is a square in K by the p=61 reduction above => contradiction.
assert C['theta_in_K_fourth_power'] and C['theta_not_K_eighth_power']
print('PASS at p61: theta->47, hprime=49, V->32, ±V both quadratic nonresidues')
print('THEOREM: theta ∈ K^4 but theta ∉ K^8, unit sublattice Gamma0 has a certified index-13 extension.')
print('STRICT: no Cl(K)[2], Cl_S[2], full rank-19 ordinary unit group, full rank-40 S-unit group, true Sel2 upper, MW rank upper, p163 fullMW Coleman or original source exclusion proven.')
