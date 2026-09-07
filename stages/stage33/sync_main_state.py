#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'

STATE_SHA='bf00eda9927064a14562a91df106af999b292d42f6c2d5305225d8a6542a9528'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
R1_SHA='b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb'
R2_SHA='912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1'
R3_SHA='e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
CAND='V91C1X_R3_COVER_INDEXED_A2_02_REPRESENTATIVE_BOUNDED_PREFLIGHT'
NEXT='V91C1X_R4_CONSTRUCT_NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA'
MISSING='NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_OR_EQUIVALENT_GLUE_BUILT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA_WITH_EXPLICIT_SWAP23_COMMON_REFINEMENT'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    s=load(OUT,STATE_SHA)
    au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA)
    w=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',W_SHA)
    r1=load(D/'e3-v91c1x-r1-chain-level-action-difference-preflight.json',R1_SHA)
    r2=load(D/'e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json',R2_SHA)
    r3=load(D/'e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',R3_SHA)
    ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb)

    assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V51_V91C1X_R3_BOUNDED_H2_REPRESENTATIVE_PREFLIGHT_GROUPED_AUDIT_CHECKPOINT'
    assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
    assert s['authority_sync']['branch_candidate_frontier']==CAND
    assert s['branch_exact_frontier_candidate']=='stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json'
    ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS' and ag['merged'] is True
    cg=s['candidate_audit_gate']; assert cg['candidate']==CAND and cg['candidate_certificate_sha256']==R3_SHA and cg['status']=='PENDING_GROUPED_HOSTILE_AUDIT_R1_R2_R3'
    assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False and cg['pr']==1678

    assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA
    assert r1['canonical_sha256']==R1_SHA and r2['canonical_sha256']==R2_SHA and r3['canonical_sha256']==R3_SHA
    assert r1['swap23_package_level']['package_level_literal_closure'] is False
    assert r1['chain_level_h2_interface']['chain_level_identity_g_seed_minus_seed_equals_delta_Lg_verifiable'] is False
    assert r2['accepted_source_representative']['materialized'] is False
    assert r2['swap23_chain_level_requirements']['triple_overlap_identity_verified'] is False
    ex=r3['exact_bounded_consequence']
    for k in ['current_named_locked_assets_materialize_accepted_a2_02_literal_mu2_2_cocycle','current_named_locked_assets_materialize_accepted_equivalent_unimodular_cech_glue','current_named_locked_assets_materialize_kummer_square_root_1_cochain','current_named_locked_assets_materialize_swap23_cover_action_or_common_refinement','current_named_locked_assets_verify_triple_overlap_action_difference_identity','repository_wide_absence_claim','route_mathematically_impossible']:
        assert ex[k] is False,k
    assert r3['audit_checkpoint']['mathematically_substantial_checkpoint'] is True
    assert r3['audit_checkpoint']['hostile_audit_required_before_any_h2_fixedness_mask20_or_dim5_credit'] is True
    assert r3['next_construction']['next_exact_leaf']==NEXT and r3['next_construction']['missing_object']==MISSING

    f=s['current_exact_frontier']
    assert f['a2_02_r3_named_locked_asset_preflight_materialized'] is True
    assert f['a2_02_swap23_complete_difference_zero_in_retained_picard_mod2'] is True
    for k in ['a2_02_literal_mu2_2_cocycle_materialized','a2_02_equivalent_unimodular_cech_glue_materialized','a2_02_actual_swap23_gm_1_cochain_comparison_materialized','a2_02_semantic_action_difference_chain_witness_materialized','a2_02_swap23_seed_fixed_mod_pic2','a2_02_marked_brauer_image_excluded_from_mask20','a2_02_source_bound_stabilizer_fixed_subspace_materialized']:
        assert f[k] is False,k
    assert f['a2_02_semantic_action_difference_verified_automorphisms']==[]
    assert f['a2_02_marked_brauer_image_computed'] is False and f['source_bound_proper14_evaluation_bits_materialized']==0
    assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2'] is None
    assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality'] is None

    assert s['current']['active_missing_interface']==MISSING and s['current']['next_exact_leaf']==NEXT
    gate=s['execution_gate']; assert gate['advance_allowed'] is False
    assert gate['advance_scope']=='GROUPED_HOSTILE_AUDIT_PR_1678_V91C1X_R1_R2_R3'
    assert gate['next_expected_command']=='HOSTILE_AUDIT_PR_1678_GROUPED_V91C1X_R1_R2_R3_EXACT_HEAD'
    assert s['stage33_progress']=='6/11'
    for k in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']:
        assert s['firewalls'][k] is False,k
    if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
    if a.check or not a.write:
        print(json.dumps({'success':True,'marker':'V113_V91C1X_R3_GROUPED_AUDIT_CHECKPOINT','state_sha256':STATE_SHA,'candidate_sha256':R3_SHA,'next_exact_leaf':NEXT,'next_expected_command':gate['next_expected_command'],'stage33_progress':'6/11'},sort_keys=True))
if __name__=='__main__': main()
