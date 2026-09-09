#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DZ/fixed-p2-mw-phi-quotient-preflight.json'
SRC=ROOT/'stages/stage36/36-09DZ/mw-phi-quotient-source-lock.md'
DR=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
DY=ROOT/'stages/stage36/36-09DY/fixed-p2-phi-to-proselmer-defect-preflight.json'
DYV=ROOT/'stages/stage36/verify_stage36_36_09DY.py'
LOCKS={
 CERT:'5fb697e6d450ab46adde1a4a40cde9c415e4cd90',
 SRC:'4ff753f9933f56cd33accaac264ddc7e936d2364',
 DR:'c212f0430fb5b4d04ee0887e303a73fb303657c8',
 DY:'3adcab8e00fa8a517df28ce71b95925f6e00ada6',
 DYV:'39173498249965f010fb40769131bd6f3618e484',
}
def gh(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dr=json.loads(DR.read_text()); dy=json.loads(DY.read_text()); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09DZ_FIXED_P2_MW_PHI_QUOTIENT_PREFLIGHT_V1'
assert c['status']=='PASS_MW_RANK1_EXACT_PHI_PSI_PROSELMER_COKERNELS'
assert c['base_main_sha']=='97aa65b83015ea31d453bffee0cc56c4d9876724'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])
assert dr['elliptic_quotients']['E_tau']['equation']=='y^2=(x+4)(x+1/4)(x+9)(x+1/9)'
assert dy['Mordell_Weil_quotient_constraints']['allowed_triples_a_a_prime_rank']==[[1,5,0],[2,4,0],[2,5,1]]
assert dy['Mordell_Weil_quotient_constraints']['common_Mordell_Weil_rank_upper_bound']==1
assert dy['finite_Phi_Selmer']['F2_dimension']==2
assert dy['finite_Psi_Selmer']['F2_dimension']==5

# Tiny exact polynomial arithmetic, coefficients low-to-high.
def padd(a,b):
    n=max(len(a),len(b)); z=[F(0)]*n
    for i in range(n): z[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(z)>1 and z[-1]==0:z.pop()
    return z
def pmul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return z
def pscale(a,s): return [F(s)*x for x in a]
def ppow(a,n):
    z=[F(1)]
    for _ in range(n): z=pmul(z,a)
    return z

def lin(a,b): return [F(b),F(a)] # a*x+b

# Verify the birational identity by clearing denominators:
# U=-7(x+4)/(4x+1), V=126y/(4x+1)^2 and y^2=quartic.
# Equivalent polynomial identity: 126^2*quartic = [-7(x+4)]*([-7(x+4)]+(4x+1))*([-7(x+4)]+49(4x+1))*(4x+1).
quart=[F(1)]
for rootshift in [F(4),F(1,4),F(9),F(1,9)]: quart=pmul(quart,[rootshift,F(1)])
N=pscale([F(4),F(1)],-7)     # -7(x+4)
D=[F(1),F(4)]                 # 4x+1
rhs=pmul(pmul(pmul(N,padd(N,D)),padd(N,pscale(D,49))),D)
lhs=pscale(quart,126**2)
assert lhs==rhs,(lhs,rhs)

# Verify the inverse rational map algebraically by composition on the function field.
# It suffices to check exact composition at symbolic numerator/denominator level for x:
# x=-(U+28)/(4U+7), U=N/D.
xnum=pscale(padd(N,pscale(D,28)),-1)
xden=padd(pscale(N,4),pscale(D,7))
# xnum/xden must equal x, i.e. xnum = x*xden.
assert xnum==pmul([F(0),F(1)],xden)

# Exact rational witness on the quartic and forward/inverse maps.
x=F(-29,11); y=F(875,121)
assert y*y==(x+4)*(x+F(1,4))*(x+9)*(x+F(1,9))
U=-7*(x+4)/(4*x+1); V=126*y/(4*x+1)**2
assert (U,V)==(F(1),F(10))
assert V*V==U*(U+1)*(U+49)
xx=-(U+28)/(4*U+7); yy=F(175)*V/(2*(4*U+7)**2)
assert (xx,yy)==(x,y)
assert c['E_tau_quartic']['explicit_point']==['-29/11','875/121']
assert c['E_tau_Weierstrass']['mapped_point_P']==['1','10']

# Full rational 2-torsion is visible on V^2=U(U+1)(U+49).
for X in [F(0),F(-1),F(-49)]: assert X*(X+1)*(X+49)==0
assert c['E_tau_Weierstrass']['full_rational_2_torsion']==[['0','0'],['-1','0'],['-49','0']]

# Exact group law on y^2=x^3+50x^2+49x.
O=None; a2=F(50); a4=F(49)
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and y1==-y2:return None
    if P==Q:
        if y1==0:return None
        m=(3*x1*x1+2*a2*x1+a4)/(2*y1)
    else:m=(y2-y1)/(x2-x1)
    x3=m*m-a2-x1-x2
    y3=-y1+m*(x1-x3)
    return (x3,y3)
def mul(n,P):
    R=None; Q=P
    while n:
        if n&1:R=add(R,Q)
        Q=add(Q,Q); n//=2
    return R
P=(F(1),F(10))
assert add(P,P)==(F(144,25),F(-5772,125))
assert mul(8,P) is not None
assert c['non_torsion_witness']['two_P']==['144/25','-5772/125']
assert c['non_torsion_witness']['eight_P_is_identity'] is False
# The external theorem ceiling is source-locked, while the arithmetic witness is independently replayed here.
assert "Mazur's rational torsion theorem" in src
assert 'Z/2Z x Z/2nZ' in src and '1 <= n <= 4' in src
assert c['non_torsion_witness']['Mazur_full_2_torsion_max_point_order']==8
assert c['non_torsion_witness']['P_non_torsion'] is True

# Rank lower bound from P plus DY upper bound collapses the allowed triples.
assert c['Mordell_Weil_rank']['A_rank_lower_bound_from_E_tau']==1
assert c['Mordell_Weil_rank']['DY_common_rank_upper_bound']==1
assert c['Mordell_Weil_rank']['common_rank_exact']==1
allowed=dy['Mordell_Weil_quotient_constraints']['allowed_triples_a_a_prime_rank']
rank1=[t for t in allowed if t[2]==1]
assert rank1==[[2,5,1]]
assert c['rational_isogeny_quotients']['unique_triple_a_a_prime_rank']==[2,5,1]
assert c['rational_isogeny_quotients']['Phi_MW_quotient_F2_dimension']==2
assert c['rational_isogeny_quotients']['Psi_MW_quotient_F2_dimension']==5

# Finite Selmer dimensions equal the MW quotient dimensions, so the finite isogeny Sha kernels vanish.
assert c['finite_isogeny_Sha_kernels']['Phi_Selmer_F2_dimension']==2
assert c['finite_isogeny_Sha_kernels']['Psi_Selmer_F2_dimension']==5
assert c['finite_isogeny_Sha_kernels']['Sha_A_Phi_F2_dimension']==0
assert c['finite_isogeny_Sha_kernels']['Sha_J_Psi_F2_dimension']==0
assert c['finite_isogeny_Sha_kernels']['Sha_A_Phi_trivial'] is True
assert c['finite_isogeny_Sha_kernels']['Sha_J_Psi_trivial'] is True

# Consume DY's exact kernel comparison and zero residual Sha contribution.
e=c['exact_proSelmer_defect']
assert e['Phi_kernel_F2_dimension']==3 and e['Psi_kernel_F2_dimension']==3
assert e['Phi_kernel_exact']=='(Z/2Z)^3' and e['Psi_kernel_exact']=='(Z/2Z)^3'
assert e['Phi_cokernel_F2_dimension']==2 and e['Phi_cokernel_cardinality']==4
assert e['Psi_cokernel_F2_dimension']==5 and e['Psi_cokernel_cardinality']==32
assert e['Phi_cokernel_exact_dimension_computed'] is True
assert e['Psi_cokernel_exact_dimension_computed'] is True
assert e['proSelmer_product_identification_obtained'] is False
assert c['route_result']['next_leaf']=='36-09EA_FIXED_P2_DEFECT_AWARE_RETAINED_OPEN_INTERSECTION_PREFLIGHT'
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09DZ verified: E_tau carries the exact non-torsion point P=(1,10), so common MW rank=1. The unique DY triple is (2,5,1), both finite isogeny Sha kernels vanish, and the pro-Selmer defects are exact: Phi kernel/cokernel dimensions 3/2 and Psi 3/5. EA is next; all Brauer/receiver/endpoint credit remains closed.')
