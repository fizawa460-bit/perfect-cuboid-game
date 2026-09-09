#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09EF/fixed-p2-physical-receiver-adapter-preflight.json'
SRC=ROOT/'stages/stage36/36-09EF/fixed-p2-physical-receiver-adapter-source-lock.md'
O=ROOT/'stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
EE=ROOT/'stages/stage36/36-09EE/fixed-p2-q2-rho-retained-open-exclusion-preflight.json'
RECEIPT=ROOT/'stages/stage36/36-09EE/hostile-audit-pass-receipt.json'
LOCKS={
 CERT:'14422b916552ba88562c2ed773a2c8a1fd2953e9',
 SRC:'7b616319f58cb466fa6840446ee71c2078f162e1',
 O:'6a2678ebedba40e13277100441361039ee47ca28',
 AW:'c1970a020803275ba87b249229e319367fa8f811',
 EE:'683d52e7cba9e2bd683cc06577fb6913532feb77',
 RECEIPT:'91a047fbffd05ecac51236a94e9d7582347051e2',
}
def gh(p):
    return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items():
    got=gh(p); assert got==h,(p,got,h)

c=json.loads(CERT.read_text()); o=json.loads(O.read_text()); aw=json.loads(AW.read_text()); ee=json.loads(EE.read_text()); rr=json.loads(RECEIPT.read_text()); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09EF_FIXED_P2_PHYSICAL_RECEIVER_ADAPTER_PREFLIGHT_V1'
assert c['status']=='PASS_FIXED_P2_PHYSICAL_RECEIVER_SECTOR_EXCLUDED_HOSTILE_AUDIT_GATED'
assert c['base_main_sha']=='09cc1687e74ef0372e4f7f1ebd8b0cddacc52dd6'
for name,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(name,gh(p),item['blob_sha'])

# Entry authority is the already-consumed EE hostile PASS.
assert c['entry_authority']['36_09EF_entry_allowed'] is True
assert c['entry_authority']['36_09EE_pass_consumed'] is True
assert rr['audit']['review_id']==5149991589
assert rr['audit']['result']=='PASS'
assert rr['audit']['audited_exact_head']=='6ae4fde45a9665f7a81173e0790006722f9bb1da'
assert rr['merged_checkpoint']['merge_commit']=='4d7f50af95ffc00340d14ec9830f619273278a81'

# 36-09O is the exact physical top genus-3 cover, not a later outer branch.
ns=o['notation_separation']; top=o['top_genus3_exact_factorization']
assert ns['base_parameter']=='p'
assert set(ns['physical_exclusions'])=={'p=0','p=1','p=-1','t=0','t=1','t=-1','t=infinity'}
assert top['normalized_model']=='C3_p: y^2=(t^2+p^2)*(t^2+p^(-2))*(t^2+c^2)*(t^2+c^(-2))'
assert top['genus']==3
assert o['middle_elliptic_physical_square_lift']['top_square_coordinate']=='x=t^2=(V+rho*U)/(V-rho*U)'
assert o['middle_elliptic_physical_square_lift']['physical_lift_condition']=='(V+rho*U)/(V-rho*U) is a nonzero rational square'
# Hostile-audited O authority is explicitly frozen in the EF cert/source.
pa=c['physical_adapter_authority']
assert pa['36_09O_pr']==1642 and pa['36_09O_hostile_review']==5123512777
assert pa['36_09O_audited_exact_head']=='be979251c6e3d7a2431fb56537520afd2596c7d9'
assert pa['36_09O_exact_head_ci']=='34000052247/101397173180'
assert pa['physical_square_lift_adapter_audited'] is True
assert 'review `5123512777`' in src

# AW confirms the fixed-p terminology means a rational physical base parameter.
assert aw['fixed_p_outer_enumerator']['input']=='primitive p=a/b on the retained physical open'
assert 'retained Stage36 receiver over that fixed p is empty' in aw['fixed_p_exclusion_rule']['statement']

# Replay p=2 specialization exactly with rational arithmetic.
p=Fraction(2,1)
h=p-1/p
cc=(p+1)/(p-1)
assert h==Fraction(3,2) and cc==3
vals=[p*p,1/(p*p),cc*cc,1/(cc*cc)]
assert vals==[Fraction(4),Fraction(1,4),Fraction(9),Fraction(1,9)]
fp=c['fixed_parameter']; sp=c['top_cover_specialization']
assert fp=={'p':'2','physical_base_allowed':True,'p_not_zero_or_plusminus_one':True,'h':'3/2','c':'3'}
assert [sp['p_squared'],sp['p_inverse_squared'],sp['c_squared'],sp['c_inverse_squared']]==['4','1/4','9','1/9']
assert sp['specialized_model']=='C3_2: y^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)'
assert sp['normalization_factor_h_nonzero'] is True
assert sp['specialization_exactly_matches_36_09EE_curve'] is True
for k in ['quadratic_twist_inserted','scalar_extension_inserted','extra_squareclass_branch_inserted']:
    assert sp[k] is False,k

# The specialized equation is literally the audited EE fixed curve.
assert ee['fixed_curve']['curve']=='C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)'
# z/y is only an ordinate letter; the RHS and retained t-open are identical.
ra=c['retained_open_adapter']
assert set(ra['physical_top_boundary'])=={'t=0','t=1','t=-1','t=infinity'}
assert set(ra['EE_retained_top_boundary'])==set(ra['physical_top_boundary'])
assert set(ee['reference_and_boundary']['retained_open_boundary_contains'])==set(ra['physical_top_boundary'])
assert ra['boundary_sets_match'] is True
assert ra['forward_implication_exact'] is True
assert ra['reverse_implication_claimed'] is False

# Consume only the hostile-audited EE ceiling.
abi=c['audited_brauer_input']
assert abi['36_09EE_external_review']==5149991589
assert abi['36_09EE_pass_consumed'] is True
assert ee['Q2_intersection_exclusion']['global_retained_open_proSelmer_intersection_empty'] is True
assert ee['brauer_manin_consequence']['full_global_2primary_Brauer_set_on_retained_open_empty'] is True
assert ee['brauer_manin_consequence']['two_primary_Brauer_Manin_obstruction_obtained'] is True
assert abi['U_ret_C3_2_adelic_Br2primary_empty'] is True
assert abi['two_primary_Brauer_Manin_obstruction'] is True

# Logical transfer ceiling: diagonal Q-points are Brauer-orthogonal, so empty BM set => no retained Q-point.
rpc=c['rational_point_consequence']; pc=c['physical_receiver_consequence']
assert rpc['diagonal_rational_points_are_Brauer_orthogonal'] is True
assert rpc['U_ret_C3_2_Q_empty'] is True
assert pc['fixed_p2_retained_receiver_sector_empty'] is True
assert pc['fixed_p_parameter_exclusion_obtained'] is True
assert pc['excluded_parameter']=='p=2'
# Crucial firewalls.
assert pc['candidate_parameter_set_shrunk'] is False
assert pc['full_receiver_emptiness_proved'] is False
assert pc['R29_CAMP2_closed'] is False
assert c['route_result']['hostile_audit_required_before_next_promotion'] is True
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():
    assert v is False,(k,v)

print('36-09EF verified: hostile-audited 36-09O specializes the exact physical top cover at p=2 to the audited EE curve C3_2 with the same retained boundary. EE emptiness of the full 2-primary Brauer set therefore excludes the retained physical receiver sector at p=2. No candidate-set, full-R29, Q11, endpoint, or Perfect Cuboid credit is granted.')
