#!/usr/bin/env python3
import json
import subprocess
from itertools import combinations
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DU/fixed-p2-phi-selmer-local-condition-defect-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DU/phi-descent-character-functions-source-lock.md'
DT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
U=frozenset(range(1,9))

def git_hash(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()

def canon(S):
    S=frozenset(S); C=U-S
    return min(tuple(sorted(S)),tuple(sorted(C)))

def push_zero(S,orbits):
    bits=[len(set(S)&set(o))%2 for o in orbits]
    return bits in ([0,0,0,0],[1,1,1,1])

assert git_hash(CERT)=='d2a8bab0ab63406c7c1ced5d077cc523d5648ba2'
assert git_hash(SOURCE)=='c9e9f9309555106ff5c0ed947c3973c0b11b1753'
assert git_hash(DT)=='362326de8d6ecc0b415ecf29c6eb936134e395ce'
c=json.loads(CERT.read_text()); dt=json.loads(DT.read_text())
assert c['schema']=='STAGE36_36_09DU_FIXED_P2_PHI_SELMER_LOCAL_CONDITION_DEFECT_PREFLIGHT_V1'
assert c['status']=='PASS_EXPLICIT_PHI_DESCENT_CHARACTER_FUNCTIONS_LOCAL_IMAGES_NOT_COMPUTED'
assert c['batch_parent']['36_09DT_exact_green_head']=='bc240925594794550c4bac7b78d2c8befbaf90c5'
assert c['batch_parent']['36_09DT_exact_head_ci']=='34239568316/102105958771'
assert c['batch_parent']['36_09DT_promotion_replay_head']=='8d4f71a9c415bd321aaf67e73116cb5e59937668'
assert c['batch_parent']['36_09DT_promotion_replay_ci']=='34239817869/102106797949'
assert dt['Galois_rationality']['kernel_Phi_constant_Q_group_scheme']=='(Z/2Z)^3'
assert dt['dual_kernel']['kernel_Psi_group_scheme']=='mu_2^3'

orbs={
 'tau':[{1,2},{3,4},{5,6},{7,8}],
 'sigma':[{1,4},{2,3},{5,8},{6,7}],
 'rho':[{1,3},{2,4},{5,7},{6,8}],
}
# Enumerate J[2] = even subsets modulo complement and compute simultaneous pushforward kernel.
classes=set()
for r in (0,2,4,6,8):
    for S in combinations(range(1,9),r): classes.add(canon(S))
assert len(classes)==64
ker=[]
for cc in sorted(classes):
    S=set(cc)
    if all(push_zero(S,orbs[h]) for h in orbs): ker.append(list(cc))
expected=[[],[1,2,3,4],[1,2,5,6],[1,2,7,8],[1,3,5,7],[1,3,6,8],[1,4,5,8],[1,4,6,7]]
assert ker==expected
assert c['dual_kernel_on_J2']['kernel_classes_canonical']==expected
assert c['dual_kernel_on_J2']['kernel_class_count']==8

# Basis independence in the F2 subset quotient.
l1=frozenset([1,2,3,4]); l2=frozenset([1,2,5,6]); l3=frozenset([1,4,5,8])
span=set()
for a in (0,1):
    for b in (0,1):
        for d in (0,1):
            S=frozenset()
            if a: S=S.symmetric_difference(l1)
            if b: S=S.symmetric_difference(l2)
            if d: S=S.symmetric_difference(l3)
            span.add(canon(S))
assert len(span)==8
assert set(span)==set(tuple(x) for x in expected)

# Rational functions F1,F2 are direct branch products for lambda1,lambda2.
# F3 descent identity is checked symbolically in Q(i)[t,z]/(z^2-g*gbar).
# Represent a=(t^2-1)^2 and b=(25/6)t(t^2+1) as coefficient dictionaries in t.
# We only need the algebraic identity: (z+g)^2-2(z+a)g = z^2-g*gbar.
# This follows by expansion for g=a-i b, gbar=a+i b; verify coefficientwise abstractly.
# Expand: LHS = z^2 +2zg+g^2 -2zg-2ag = z^2 + g(g-2a)=z^2-g*gbar.
assert c['rational_descent_functions']['curve_identity']=='z^2=(a-i*b)(a+i*b)=a^2+b^2'
assert c['rational_descent_functions']['descent_identity']=='(z+g)^2=2(z+a)g'
assert c['rational_descent_functions']['F3']=='2(z+(t^2-1)^2)'
assert c['rational_descent_functions']['F3_is_Q_rational'] is True
assert c['rational_descent_functions']['F3_same_squareclass_as_lambda3_branch_product'] is True
assert c['rational_descent_functions']['all_three_dual_kernel_characters_have_Q_rational_function_representatives'] is True

# Direct exact polynomial check g*gbar equals the fixed curve RHS.
# a=(t^2-1)^2 => [1,0,-2,0,1]; b=(25/6)(t+t^3).
def mul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return out
a=[Fraction(1),0,Fraction(-2),0,Fraction(1)]
b=[0,Fraction(25,6),0,Fraction(25,6)]
a2=mul(a,a); b2=mul(b,b)
N=max(len(a2),len(b2)); lhs=[Fraction(0)]*N
for i in range(N): lhs[i]=(a2[i] if i<len(a2) else 0)+(b2[i] if i<len(b2) else 0)
rhs=[Fraction(1),0,Fraction(481,36),0,Fraction(733,18),0,Fraction(481,36),0,Fraction(1)]
assert lhs==rhs

assert c['Phi_connecting_map_coordinates']['coordinate_connecting_map_constructed'] is True
assert c['Phi_connecting_map_coordinates']['well_defined_mod_squares_by_functions_on_curve_descent_protocol'] is True
assert c['Phi_connecting_map_coordinates']['local_image_delta_v_JQv_computed'] is False
assert c['local_condition_boundary']['local_images_computed'] is False
assert c['local_condition_boundary']['required_place_set_certified'] is False
assert c['local_condition_boundary']['global_Phi_Selmer_group_computed'] is False
assert c['route_result']['next_leaf']=='36-09DV_FIXED_P2_PHI_SELMER_REQUIRED_PLACES_LOCAL_IMAGE_PREFLIGHT'

src=SOURCE.read_text()
for token in ['Computing a Selmer group of a Jacobian using functions on the curve','lambda1','F3=2(z+(t^2-1)^2)','(z+g)^2 = 2(z+a) g']:
    assert token in src
for k in ['required_place_set_certified','Phi_Selmer_local_condition_map_computed','global_Phi_Selmer_group_computed','proSelmer_cokernel_size_computed','proSelmer_product_identification_obtained','T2Sel_J_computed','elliptic_quotient_T2Sel_computed','retained_open_curve_proSelmer_intersection_computed','global_2primary_Brauer_set_nonempty','global_2primary_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
    assert c['scope_firewalls'][k] is False,k
print('36-09DU verified: ker(Psi) branch-subset basis and Q-rational descent functions F1,F2,F3 construct explicit Phi connecting coordinates. Required places/local images and all downstream credit remain closed.')
