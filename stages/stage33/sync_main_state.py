#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'

STATE_SHA='9c436458001fafc4c036aeeb99e610abbdc2d0554f34bf7fde9ba4c144d84191'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
R1_SHA='b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
CAND='V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_PREFLIGHT_BLOCKED'
NEXT='V91C1X_R2_MATERIALIZE_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_THEN_COMPARE_SWAP23_ACTION_DIFFERENCE'
MISSING='SOURCE_BOUND_LITERAL_A2_02_MU2_2_COCYCLE_OR_EQUIVALENT_UNIMODULAR_CECH_GLUE_DATUM_WITH_SWAP23_ACTION_AND_GM_1_COCHAIN_COMPARISON'


def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(p,h):
    o=json.loads(p.read_text())
    b=dict(o); q=b.pop('canonical_sha256')
    assert q==h==csha(b),p
    return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    s=load(OUT,STATE_SHA)
    au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA)
    w=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',W_SHA)
    r1=load(D/'e3-v91c1x-r1-chain-level-action-difference-preflight.json',R1_SHA)
    ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256')
    assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False

    assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V49_V91C1X_R1_CHAIN_LEVEL_PREFLIGHT_BLOCKED_R2_LITERAL_MU2_GLUE'
    assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
    assert s['authority_sync']['branch_candidate_frontier']==CAND
    assert s['branch_exact_frontier_candidate']=='stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json'
    ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS' and ag['merged'] is True
    prior=s['prior_failed_candidate_gate']; assert prior['pr']==1671 and prior['hostile_audit_review']==5127167940 and prior['hostile_audit_verdict']=='FAIL'
    assert prior['candidate_certificate_sha256']==W_SHA and prior['retained_subclaim']=='V91C1W_BOUNDED_PICARD64_AND_COMPLETE_SWAP23_PIC2_ZERO'
    cg=s['candidate_audit_gate']; assert cg['candidate']==CAND and cg['candidate_certificate_sha256']==R1_SHA and cg['pr']==1678
    assert cg['status']=='EXACT_NONCREDIT_NEGATIVE_PREFLIGHT_CONTINUATION_ALLOWED' and cg['audit_pass_credit'] is False and cg['merge_allowed'] is False

    assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA and r1['canonical_sha256']==R1_SHA
    p=r1['swap23_package_level']
    assert p['package_level_literal_closure'] is False
    assert p['every_acted_package_has_original_a2_02_divisor_candidate'] is False
    assert p['every_acted_package_has_unique_original_a2_02_divisor_candidate'] is False
    assert p['all_candidate_function_scalar_ratios_one'] is False
    assert p['literal_package_action_is_permutation_of_same_eight'] is False
    h=r1['chain_level_h2_interface']
    assert h['d_cech_cartier_seed_assembly_materialized'] is True
    assert h['d_genuine_full_surface_h2_mu2_lift_for_e3'] is False
    assert h['full_surface_kummer_extension_class_missing'] is True
    assert h['locked_interface_exposes_literal_mu2_2_cocycle'] is False
    assert h['locked_interface_exposes_equivalent_unimodular_cech_glue'] is False
    assert h['actual_swap23_gm_1_cochain_comparison_materialized'] is False
    assert h['chain_level_identity_g_seed_minus_seed_equals_delta_Lg_verifiable'] is False
    assert r1['semantic_bridge']['next_missing_object']==MISSING and r1['semantic_bridge']['next_exact_leaf']==NEXT

    f=s['current_exact_frontier']
    assert f['a2_02_swap23_complete_difference_zero_in_retained_picard_mod2'] is True
    assert f['a2_02_swap23_package_level_literal_closure'] is False
    assert f['a2_02_swap23_every_component_has_original_package_candidate'] is False
    assert f['a2_02_swap23_all_candidate_function_scalar_ratios_one'] is False
    for k in ['a2_02_literal_mu2_2_cocycle_materialized','a2_02_equivalent_unimodular_cech_glue_materialized','a2_02_actual_swap23_gm_1_cochain_comparison_materialized','a2_02_semantic_action_difference_chain_witness_materialized','a2_02_swap23_seed_fixed_mod_pic2','a2_02_marked_brauer_image_excluded_from_mask20','a2_02_source_bound_stabilizer_fixed_subspace_materialized']:
        assert f[k] is False,k
    assert f['a2_02_semantic_action_difference_verified_automorphisms']==[]
    assert f['a2_02_semantic_action_difference_blocked_automorphisms']==['swap23','sign_b1','sign_a2']
    assert f['a2_02_marked_brauer_image_computed'] is False and f['source_bound_proper14_evaluation_bits_materialized']==0
    assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2'] is None and f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality'] is None

    assert s['current']['active_missing_interface']==MISSING and s['current']['next_exact_leaf']==NEXT
    assert s['execution_gate']['advance_allowed'] is True
    assert s['execution_gate']['advance_scope']=='V91C1X_R2_LITERAL_MU2_2_COCYCLE_OR_EQUIVALENT_CECH_GLUE_ONLY_NO_H2_FIXEDNESS_MASK20_OR_DIM5_CREDIT'
    assert s['execution_gate']['next_expected_command']=='STAGE33_MAIN_BATCH_V91C1X_R2_LITERAL_MU2_COCYCLE_GLUE'
    assert s['stage33_progress']=='6/11' and s['firewalls']['merge_allowed'] is False
    if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
    if a.check or not a.write:
        print(json.dumps({'success':True,'marker':'V111_V91C1X_R1_NEGATIVE_CHAIN_PREFLIGHT_R2_LITERAL_MU2_GLUE','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':R1_SHA,'next_exact_leaf':NEXT,'stage33_progress':'6/11'},sort_keys=True))
if __name__=='__main__': main()
