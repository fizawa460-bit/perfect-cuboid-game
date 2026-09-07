#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BQ/relative-factor-squareclass-branch-exhaustiveness-preflight.json'
BP=ROOT/'stages/stage36/36-09BP/full-cover-global-descent-router-preflight.json'
BPV=ROOT/'stages/stage36/verify_stage36_36_09BP.py'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
AF=ROOT/'stages/stage36/36-09AF/variable-prime-jacobi-matrix-realizability-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
AY=ROOT/'stages/stage36/36-09AY/universal-boundary-tunnell-survivor-preflight.json'
BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
W01=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='727b3f34c4d850e868aff64483aeb99861b13c7c'
BP_HEAD='1ff60da12b83e92daa40b90ce2e5ca756a089212'
BP_CI='34113049979/101713444698'
CERT_BLOB='22847973ab424f8a35b49bd3c7a7f32086ba846a'
LOCKS={
 BP:'fa29295bcc1072c9ed9608bc79be82993b2b657c', BPV:'4b7f1f0f2ea735d945b9bb14ab16b43d8a5e470e',
 AD:'9d0388845955efee71d1a761ae4ee943d8b565d5', AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
 AF:'be5a65e3fcfb182998ccb02ec42f8114b50b0a7d', AW:'c1970a020803275ba87b249229e319367fa8f811',
 AY:'add18004debf95a218a6393f6c2f18f2bd4f7e10', BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',
 BB:'e4b63fd500d05ff5dc704e0c08409edee5895053', W01:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BP_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bp=json.loads(BP.read_text()); ad=json.loads(AD.read_text()); ae=json.loads(AE.read_text()); af=json.loads(AF.read_text()); aw=json.loads(AW.read_text()); ay=json.loads(AY.read_text()); ba=json.loads(BA.read_text()); bb=json.loads(BB.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1693,'36_09BP_exact_head':BP_HEAD,'36_09BP_exact_head_ci':BP_CI}
    assert bp['route_result']['next_leaf']=='36-09BQ_RELATIVE_FACTOR_SQUARECLASS_BRANCH_EXHAUSTIVENESS_PREFLIGHT'

    ex=c['existing_exact_branch_adapter']
    assert ad['aggregate_odd_squareclasses']['finite_directional_slot_count']==10
    assert ad['coupled_squareclass_reconstruction']['existence_statement'].startswith('there exist positive rationals/integer-square representatives')
    assert ae['finite_mod8_skeleton']['survivor_count_after_reciprocity_and_UV_2adic_compatibility']==128
    assert ae['interpretation']['finite_exhaustive_Q_squareclass_family'] is False
    enum=aw['fixed_p_outer_enumerator']; rule=aw['fixed_p_exclusion_rule']
    assert enum['outer_superset'] is True
    assert rule['unconditional'] is True
    assert rule['converse'] is False
    assert ex['AW_outer_superset'] is True and ex['AW_fixed_p_zero_survivor_exclusion_unconditional'] is True

    pop=c['AY_population_adapter']
    assert ay['universal_construction']['AW_membership'].startswith('this support-compatible branch satisfies')
    assert ba['AY_branch']['squareclasses']=='A=B=D=1, C=odd_sf(D0), eta=sign(D0), f=1, e=(1+v2(D0)) mod2'
    assert ba['receiver_intersection_firewall']['auxiliary_C_AY_open_point_implies_top_receiver'] is False
    assert bb['route_result']['receiver_restricted_intersection_exact'] is True
    assert 'lambda*t is a Q-point of C_kappa' in bb['receiver_restricted_intersection']['equivalent_description']
    assert pop['AY_certificate_states_AW_membership'] is True
    assert pop['AY_auxiliary_point_is_receiver_automatically'] is False
    assert pop['BB_restores_original_joint_receiver_conditions'] is True

    u=c['uniformity_boundary']; res=c['S34_W01_resolution']; nxt=c['next_weapon_preflight']; rr=c['route_result']
    assert af['conclusion']['actual_variable_prime_identity_load_bearing'] is True
    assert af['conclusion']['finite_exhaustive_Q_squareclass_family'] is False
    assert u['fixed_p_finite_exhaustive_outer_branch_family'] is True
    assert u['all_p_single_fixed_finite_Q_squareclass_family'] is False
    assert u['all_p_single_fixed_finite_H1_twist_family'] is False
    assert res['every_receiver_point_enters_fixed_p_outer_enumerator'] is True
    assert res['fixed_p_exhaustive_outer_coverage_requirement_met'] is True
    assert res['uniform_fixed_Q_squareclass_family_requirement_met'] is False
    assert res['full_uniform_S34_W01_output_obtained'] is False
    w02=W02.read_text()
    assert '| Role | `GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION` |' in w02
    assert 'proved full MW basis/generator and complete torsion subgroup' in w02
    assert ba['positive_rank_and_infinitude']['rank_E_n_Q_at_least']==1
    assert nxt['S34_W02_applicability_proved'] is False
    assert rr['fixed_p_exhaustive_outer_branch_family'] is True
    assert rr['uniform_finite_Q_squareclass_family'] is False
    assert rr['uniform_finite_H1_twist_family'] is False
    assert rr['next_leaf']=='36-09BR_AY_MORDELL_WEIL_CONGRUENCE_APPLICABILITY_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V106_36_09BQ_FIXED_P_OUTER_EXHAUSTIVENESS'
    bq=st['authority_frontier']['36-09BQ']
    assert bq['certificate_blob_sha']==CERT_BLOB
    assert bq['FIXED_P_EXHAUSTIVE_OUTER_BRANCH_FAMILY'] is True
    assert bq['UNIFORM_FINITE_Q_SQUARECLASS_FAMILY'] is False
    assert bq['UNIFORM_FINITE_H1_TWIST_FAMILY'] is False
    assert bq['S34_W02_APPLICABILITY_PROVED'] is False
    assert st['current']['unit']=='36-09BQ'
    assert st['current']['next_exact_leaf']=='36-09BR_AY_MORDELL_WEIL_CONGRUENCE_APPLICABILITY_PREFLIGHT'
    assert st['current']['36_09BR_entry_allowed'] is True
    assert st['cycle_ledger']['B4_BAD_PRIME_LOCAL']=='LIVE_PARAMETER_ELIMINATION_UNTESTED_UNIFORMLY_RETAINS_RECEIVER_POINT_GATES'
    for key in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BQ verified: AW already gives a finite exhaustive outer branch family for each fixed p, and AY is an explicit AW-compatible branch with BB restoring the joint receiver condition. Uniform fixed Q-squareclass/H1 finiteness remains false; S34-W02 full-MW applicability is selected next.')

if __name__=='__main__': main()
