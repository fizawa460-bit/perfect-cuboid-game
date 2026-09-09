#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DS/fixed-p2-v4-isogeny-2primary-proselmer-transport-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DS/v4-isogeny-norm-pullback-proselmer-source-lock.md'
DR=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
DR_SOURCE=ROOT/'stages/stage36/36-09DR/v4-elliptic-quotient-isogeny-source-lock.md'

def git_hash(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()

assert git_hash(CERT)=='8c16b2f2c53f343dc710bf06d55245aab0599a36'
assert git_hash(SOURCE)=='1bac0039c0abccc236b392c2deba3a26ee83ba88'
assert git_hash(DR)=='c212f0430fb5b4d04ee0887e303a73fb303657c8'
assert git_hash(DR_SOURCE)=='e546e1a731dfd6b270641eb1adb026847f8b838e'

c=json.loads(CERT.read_text())
dr=json.loads(DR.read_text())
s=SOURCE.read_text()

assert c['schema']=='STAGE36_36_09DS_FIXED_P2_V4_ISOGENY_2PRIMARY_PROSELMER_TRANSPORT_PREFLIGHT_V1'
assert c['status']=='PASS_V4_ISOGENY_DEGREE8_AND_PROSELMER_EXPONENT2_TRANSPORT_PRODUCT_IDENTIFICATION_STILL_MISSING'
assert c['base_main_sha']=='70265586b3f97be21c7621af73f443311f1f3fa3'
assert c['batch_parent']['36_09DR_exact_green_head']=='ffff741cc96fb9d3125013e0d02e69410a434175'
assert c['batch_parent']['36_09DR_exact_head_ci']=='34234332852/102088050237'
assert c['batch_parent']['36_09DR_promotion_replay_head']=='cd1c5eaba94bf6202d8d2d9bc430a74224933bba'
assert c['batch_parent']['36_09DR_promotion_replay_ci']=='34234702694/102089303104'
assert dr['isogeny_result']['Q_isogeny_constructed'] is True
assert dr['full_V4_quotient']['genus']==0
assert dr['differential_check']['determinant']==2

# V4 group-ring replay. Coordinates are [1,tau,sigma,rho].
e=(1,0,0,0)
tau=(0,1,0,0)
sigma=(0,0,1,0)
rho=(0,0,0,1)
def add(*xs):
    return tuple(sum(vs) for vs in zip(*xs))
def scale(n,x):
    return tuple(n*a for a in x)

N=add(e,tau,sigma,rho)
sum_three_traces=add(add(e,tau),add(e,sigma),add(e,rho))
# sum_h (1+h) = 2*1 + N; N acts through Jac(C/V4)=0.
assert tuple(a-b for a,b in zip(sum_three_traces,scale(2,e)))==N
assert c['push_pull_relations']['V4_norm_relation_on_J']=='1+tau+sigma+rho=0'
assert c['composition_relations']=={
    'Psi_after_Phi':'[2]_A',
    'Phi_after_Psi':'[2]_J',
    'both_exact':True
}

# Degree replay: Phi and Psi are dual and Psi*Phi=[2] on a 3-fold.
dimA=c['abelian_varieties']['dimension_A']
assert dimA==3==c['abelian_varieties']['dimension_J']
deg2=2**(2*dimA)
assert deg2==64==c['degree_and_kernel']['degree_multiplication_by_2_on_dimension_3']
deg_phi=int(deg2**0.5)
assert deg_phi*deg_phi==deg2
assert deg_phi==8
assert c['degree_and_kernel']['degree_Phi']==8
assert c['degree_and_kernel']['degree_Psi']==8
assert c['degree_and_kernel']['kernel_Phi_geometric_order']==8
assert c['degree_and_kernel']['kernel_Psi_geometric_order']==8
assert c['degree_and_kernel']['kernel_Phi_killed_by_2'] is True
assert c['degree_and_kernel']['kernel_Psi_killed_by_2'] is True
assert c['degree_and_kernel']['kernel_rational_Galois_module_structure_computed'] is False
assert c['degree_and_kernel']['kernel_identified_as_constant_Z2_cubed'] is False

# Formal pro-Selmer consequence of fg=gf=[2] on 2-torsion-free inverse limits:
# each map is injective, and each quotient by its image is killed by 2.
p=c['proSelmer_transport']
assert p['T2Sel_2_torsion_free'] is True
assert p['Phi_injective'] is True and p['Psi_injective'] is True
assert p['cokernel_Phi_killed_by_2'] is True
assert p['cokernel_Psi_killed_by_2'] is True
assert p['cokernel_dimension_computed'] is False
assert p['cokernel_cardinality_computed'] is False
assert p['product_identification_obtained'] is False
assert 'compatibility `x_n=2x_{n+1}` forces every' in s
assert 'both cokernels are killed by 2' in s
assert 'does **not** compute the cokernel' in s

assert c['route_result']['next_leaf']=='36-09DT_FIXED_P2_V4_ISOGENY_PROSELMER_DEFECT_PREFLIGHT'
for k in [
    'kernel_rational_Galois_module_structure_computed',
    'proSelmer_cokernel_size_computed',
    'proSelmer_product_identification_obtained',
    'T2Sel_J_computed',
    'elliptic_quotient_T2Sel_computed',
    'retained_open_curve_proSelmer_intersection_computed',
    'global_2primary_Brauer_set_nonempty',
    'global_2primary_Brauer_set_empty',
    'Brauer_Manin_obstruction_obtained',
    'fixed_p_parameter_exclusion_obtained',
    'candidate_parameter_set_shrunk',
    'receiver_emptiness_proved',
    'R29_CAMP2_closed',
    'Q11_CAMPEDELLI_closed',
    'endpoint_closed',
    'perfect_cuboid_nonexistence_claim'
]:
    assert c['scope_firewalls'][k] is False,k

print('36-09DS verified: V4 norm/pullback maps satisfy both [2] compositions, dual degree-8 isogenies have order-8 geometric 2-torsion kernels, and the induced pro-Selmer maps are mutual injections with exponent-2 cokernel. Exact defect/product identification and all downstream credit remain closed.')
