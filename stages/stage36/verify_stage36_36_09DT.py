#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DT/v4-isogeny-explicit-kernel-source-lock.md'
DS=ROOT/'stages/stage36/36-09DS/fixed-p2-v4-isogeny-2primary-proselmer-transport-preflight.json'

U=frozenset(range(1,9))

def git_hash(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()

def equiv(a,b):
    a=frozenset(a); b=frozenset(b)
    return a==b or a==(U-b)

def add(*subs):
    s=frozenset()
    for x in subs:
        s=s.symmetric_difference(frozenset(x))
    return s

def is_zero(s):
    s=frozenset(s)
    return s==frozenset() or s==U

def conj(s):
    p={1:2,2:1,3:4,4:3,5:6,6:5,7:8,8:7}
    return frozenset(p[x] for x in s)

assert git_hash(CERT)=='362326de8d6ecc0b415ecf29c6eb936134e395ce'
assert git_hash(SOURCE)=='df701b11135d43cd2baaa1c59eb9c289d3abfb72'
assert git_hash(DS)=='8c16b2f2c53f343dc710bf06d55245aab0599a36'
c=json.loads(CERT.read_text())
ds=json.loads(DS.read_text())
assert c['schema']=='STAGE36_36_09DT_FIXED_P2_V4_ISOGENY_PROSELMER_DEFECT_PREFLIGHT_V1'
assert c['status']=='PASS_EXPLICIT_CONSTANT_Z2_CUBED_V4_ISOGENY_KERNEL_PHI_SELMER_LOCAL_CONDITIONS_STILL_MISSING'
assert c['batch_parent']['36_09DS_exact_green_head']=='7cad044d63dace9140c7527390358e19b794298d'
assert c['batch_parent']['36_09DS_exact_head_ci']=='34237708751/102099623747'
assert c['batch_parent']['36_09DS_promotion_replay_head']=='3d36a47b603106aa7fd84511c9da8ecb7697ba51'
assert c['batch_parent']['36_09DS_promotion_replay_ci']=='34238061190/102100815243'
assert ds['degree_and_kernel']['degree_Phi']==8
assert ds['degree_and_kernel']['kernel_Phi_geometric_order']==8
assert ds['degree_and_kernel']['kernel_Phi_killed_by_2'] is True
assert ds['isogeny_maps']['duality']=='Psi=Phi^vee under the canonical principal polarizations'

# Exact orbit partitions from tau:t->-t, sigma:t->1/t, rho:t->-1/t.
orb={
 'tau':[{1,2},{3,4},{5,6},{7,8}],
 'sigma':[{1,4},{2,3},{5,8},{6,7}],
 'rho':[{1,3},{2,4},{5,7},{6,8}],
}
assert c['quotient_orbit_partitions']=={k:[sorted(x) for x in v] for k,v in orb.items()}

alpha={h:frozenset([1,2,3,4]) for h in orb}
beta={
 'tau':frozenset([1,2,5,6]),
 'sigma':frozenset([1,4,5,8]),
 'rho':frozenset([1,3,5,7]),
}

# Each selected class is the union of two quotient orbits, hence is a pulled-back
# quotient 2-torsion class.  Alpha/beta form a nonzero independent pair.
for h in orb:
    unions=[]
    for i in range(4):
        for j in range(i+1,4):
            unions.append(frozenset(orb[h][i]|orb[h][j]))
    assert alpha[h] in unions
    assert beta[h] in unions
    assert not is_zero(alpha[h])
    assert not is_zero(beta[h])
    assert not equiv(alpha[h],beta[h])
    assert not is_zero(add(alpha[h],beta[h]))

# Kernel generators map to zero under Phi by symmetric-difference addition in J[2].
assert is_zero(add(alpha['tau'],alpha['sigma']))
assert is_zero(add(alpha['tau'],alpha['rho']))
assert add(beta['tau'],beta['sigma'],beta['rho'])==U

# Independence in A[2], using (alpha_h,beta_h) as a basis on each elliptic factor.
k1=(1,0, 1,0, 0,0)
k2=(1,0, 0,0, 1,0)
k3=(0,1, 0,1, 0,1)
span=set()
for a in (0,1):
    for b in (0,1):
        for d in (0,1):
            v=tuple((a*k1[i])^(b*k2[i])^(d*k3[i]) for i in range(6))
            span.add(v)
assert len(span)==8
assert c['Phi_kernel_generators']['generated_subgroup_order']==8
assert c['Phi_kernel_generators']['DS_kernel_Phi_geometric_order']==8
assert c['Phi_kernel_generators']['therefore_generated_subgroup_equals_kernel_Phi'] is True

# Galois rationality: complex conjugation fixes each subset class modulo complement.
for s in list(alpha.values())+list(beta.values()):
    assert equiv(conj(s),s)
assert conj(beta['tau'])==beta['tau']
assert conj(beta['sigma'])==U-beta['sigma']
assert conj(beta['rho'])==U-beta['rho']
assert c['Galois_rationality']['all_three_kernel_generators_Q_rational'] is True
assert c['Galois_rationality']['kernel_Phi_constant_Q_group_scheme']=='(Z/2Z)^3'

# Dual-isogeny consequence and cohomological coordinate ceiling.
assert c['dual_kernel']['Psi_equals_Phi_dual'] is True
assert c['dual_kernel']['kernel_Psi_Cartier_dual_to_kernel_Phi'] is True
assert c['dual_kernel']['kernel_Psi_group_scheme']=='mu_2^3'
assert c['dual_kernel']['kernel_Psi_constant_Q_group_scheme']=='(Z/2Z)^3'
assert c['cohomological_coordinate_consequence']['Phi_Selmer_local_condition_map_computed'] is False
assert c['cohomological_coordinate_consequence']['global_Phi_Selmer_group_computed'] is False
assert c['proSelmer_defect_boundary']['proSelmer_cokernel_cardinality_computed'] is False
assert c['proSelmer_defect_boundary']['proSelmer_product_identification_obtained'] is False
assert c['route_result']['next_leaf']=='36-09DU_FIXED_P2_PHI_SELMER_LOCAL_CONDITION_DEFECT_PREFLIGHT'

src=SOURCE.read_text()
assert 'even subsets of the eight ramification points' in src
assert 'Complex conjugation acts by' in src
assert 'kernel of the dual isogeny' in src
for k in ['Phi_Selmer_local_condition_map_computed','global_Phi_Selmer_group_computed','proSelmer_cokernel_size_computed','proSelmer_product_identification_obtained','T2Sel_J_computed','elliptic_quotient_T2Sel_computed','retained_open_curve_proSelmer_intersection_computed','global_2primary_Brauer_set_nonempty','global_2primary_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
    assert c['scope_firewalls'][k] is False,k
print('36-09DT verified: explicit 8-element Q-rational kernel of Phi equals constant (Z/2)^3; dual kernel is split mu_2^3. Phi-Selmer local conditions and all downstream credit remain closed.')
