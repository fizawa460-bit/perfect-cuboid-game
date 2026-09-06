#!/usr/bin/env python3
import itertools,json,math
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4t-full-picard-rank-gap-hodge-cap.json'
Q=ROOT/'stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json'
S=ROOT/'stages/stage35-ex/35ex-35/goal4s-picard-overlattice-discriminant-2primary.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text());q4=json.loads(Q.read_text());s4=json.loads(S.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4T_FULL_PICARD_RANK_GAP_HODGE_CAP_V1'
assert q4['projective_closure']['complete_intersection_type']=='(2,2,2,2)'
assert q4['projective_closure']['degree']==16
assert q4['singular_locus']['geometric_node_count']==48
assert q4['singular_locus']['all_nodes_type']=='A1_ordinary_double_point'
assert s4['visible_numerical_lattice']['rank']==53
assert s4['smith_normal_form']['discriminant_absolute']=='2^45'

# Complete-intersection canonical and Euler-characteristic calculation.
ambient_n=6
degs=[2,2,2,2]
degree=math.prod(degs)
K_coeff=sum(degs)-(ambient_n+1)
assert degree==16 and K_coeff==1
K2=K_coeff*K_coeff*degree
assert K2==16

# Koszul Euler characteristic for O_X0 on P^6.  chi(P^6,O(m)) is the
# Hilbert polynomial binomial(m+6,6), valid at negative m as Euler characteristic.
def chi_P6(m): return sp.binomial(m+6,6)
chi=sum((-1)**j*math.comb(4,j)*chi_P6(-2*j) for j in range(5))
assert int(chi)==8

# A1 singularities are rational double points: the minimal resolution is crepant
# and preserves H^i(O).  Adjunction gives omega_X0=O_X0(1); the four quadrics
# contain no linear equation, hence h0(O_X0(1))=7.
pg=7
q=1+pg-int(chi)
assert q==0
c2=12*int(chi)-K2
assert c2==80
b2=c2-2+4*q
assert b2==78
h11=b2-2*pg
assert h11==64
visible=53
assert h11-visible==11

assert a['canonical_complete_intersection_data']['minimal_resolution_crepant'] is True
assert a['holomorphic_invariants']=={
    'K_squared':16,'chi_O':8,'p_g':7,'q':0,
    'derivation':a['holomorphic_invariants']['derivation']}
assert a['topological_hodge_invariants']['c2']==80
assert a['topological_hodge_invariants']['b2']==78
assert a['topological_hodge_invariants']['h11']==64
assert a['picard_rank_gate']['exact_interval']=='53 <= rho(Xbar) <= 64'
assert a['picard_rank_gate']['missing_rank_upper_bound']==11
assert a['picard_rank_gate']['visible_rank_already_forces_full_rank'] is False
assert a['credit_boundary']['full_geometric_picard_group_computed'] is False
assert a['credit_boundary']['E1_proved'] is False

st=json.loads(STATE.read_text())
assert st['schema'].startswith('STAGE35_EX_PESCH_E1_STATE_V57_')
assert st['current']['unit']=='35EX-35_GOAL4T_FULL_PICARD_RANK_GAP_AND_HODGE_CAP_PREFLIGHT'
assert st['claims']['geometric_picard_rank_upper_bound_64_obtained'] is True
assert st['claims']['missing_picard_rank_upper_bound_11_obtained'] is True
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4T: 53 <= rho(Xbar) <= 64, missing Picard rank at most 11')
