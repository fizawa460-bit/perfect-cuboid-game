#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'

STATE_SHA='0db30ac3b6c9bfa33339edab1f22537886b1e8341fd84d4e89d2e27a8d3abf7d'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
R1_SHA='b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb'
R2_SHA='912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1'
R3_SHA='e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e'
R4_SHA='cead57f641b02e8defb8cb614ee1b1acdca1ee6d1e9f7c04514ccfffef5577e0'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
CAND='V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_DATA_INSUFFICIENT_FOR_COVER_INDEXED_A2_02_H2_REPRESENTATIVE'
MISSING='NEW_SOURCE_BOUND_A2_02_FINITE_COVER_WITH_LITERAL_LOCAL_EQUATIONS_UNIFORMIZERS_OVERLAP_TRANSITIONS_AND_SWAP23_COMMON_REFINEMENT_SUFFICIENT_TO_MATERIALIZE_Z_IJK_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_IDENTITY'
NEXT='V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE'
AUDITED_HEAD='4dd839ec21ece8ef08c25cb385e28050720dda77'
AUDIT_REVIEW=5128292956
AUDIT_NODE='PRR_kwDOTr52Y88AAAABMauKXA'
AUDIT_AT='2026-09-07T05:21:36Z'
MERGE_COMMIT='726198a3d8ca4834e45c2ef275a75266b0f752b4'
R5_COMMAND='STAGE33_MAIN_BATCH_V91C1X_R5_COVER_GLUE_PACKAGE'
R5_SCOPE='V91C1X_R5_SOURCE_BOUND_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE_ONLY'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    s=load(OUT,STATE_SHA)
    au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA)
    w=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',W_SHA)
    r1=load(D/'e3-v91c1x-r1-chain-level-action-difference-preflight.json',R1_SHA)
    r2=load(D/'e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json',R2_SHA)
    r3=load(D/'e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',R3_SHA)
    r4=load(D/'e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json',R4_SHA)
    ctl=json.loads(CTL.read_text(encoding='utf-8')); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb)

    assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA
    assert r1['canonical_sha256']==R1_SHA and r2['canonical_sha256']==R2_SHA and r3['canonical_sha256']==R3_SHA and r4['canonical_sha256']==R4_SHA
    assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V54_V91C1X_R4_HOSTILE_PASS_R5_ACTIVE'
    assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
    assert s['authority_sync']['branch_candidate_frontier']==CAND
    assert s['authority_sync']['status']=='V91C1V_AUTHORITY_R4_HOSTILE_PASS_R5_CONSTRUCTION_ACTIVE'
    assert s['branch_exact_frontier_candidate']=='stages/stage33/33-12/e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json'

    ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS' and ag['merged'] is True
    r3a=s['continuation_provenance']['x_r3_grouped_hostile_audit']; assert r3a['pr']==1678 and r3a['verdict']=='PASS' and r3a['merged'] is True
    cg=s['candidate_audit_gate']
    assert cg['candidate']==CAND and cg['candidate_certificate_sha256']==R4_SHA and cg['pr']==1682
    assert cg['status']=='HOSTILE_AUDIT_PASS_MERGED_NONCREDIT_R4_CHECKPOINT'
    assert cg['audit_pass_credit'] is True and cg['mathematical_authority_promoted'] is False and cg['merge_allowed'] is False and cg['merged'] is True
    assert cg['exact_audited_head']==AUDITED_HEAD and cg['hostile_audit_review']==AUDIT_REVIEW and cg['hostile_audit_review_node']==AUDIT_NODE
    assert cg['hostile_audit_submitted_at']==AUDIT_AT and cg['hostile_audit_verdict']=='PASS' and cg['merge_commit']==MERGE_COMMIT
    r4a=s['continuation_provenance']['x_r4_grouped_hostile_audit']
    assert r4a['pr']==1682 and r4a['review']==AUDIT_REVIEW and r4a['review_node']==AUDIT_NODE and r4a['submitted_at']==AUDIT_AT
    assert r4a['exact_audited_head']==AUDITED_HEAD and r4a['verdict']=='PASS' and r4a['checkpoint_credit']=='NONCREDIT_CONSTRUCTION_BLOCKER_ONLY'
    assert r4a['authority_unchanged'] is True and r4a['stage33_progress_unchanged'] is True and r4a['merged'] is True and r4a['merge_commit']==MERGE_COMMIT and r4a['next_exact_leaf']==NEXT

    assert r4['candidate']==CAND and r4['credit']=='NONCREDIT_CONSTRUCTION_BLOCKER'
    assert r4['next_missing_object']==MISSING and r4['next_exact_leaf_after_audit']==NEXT
    for k in ['repository_wide_search_claim','repository_wide_absence_claim','mathematical_nonexistence_claim','route_mathematically_impossible_claim']:
        assert r4['bounded_scope'][k] is False,k
    for k in ['finite_cover_materialized','overlap_indices_materialized','component_uniformizers_materialized','literal_local_equations_materialized','overlap_transitions_materialized','equivalent_unimodular_cech_glue_materialized','literal_mu2_2_cocycle_materialized','swap23_common_refinement_materialized','line_bundle_gm_1_cocycle_ell_ij_materialized','square_root_1_cochain_r_ij_materialized','triple_overlap_identity_verified']:
        assert r4['bounded_findings'][k] is False,k

    assert s['current']['substep']=='E3_V91C1X_R5_SOURCE_BOUND_COVER_GLUE_PACKAGE_ACTIVE'
    assert s['current']['active_missing_interface']==MISSING and s['current']['next_exact_leaf']==NEXT
    gate=s['execution_gate']; assert gate['advance_allowed'] is True and gate['advance_scope']==R5_SCOPE and gate['next_expected_command']==R5_COMMAND
    assert gate['stop_semantics']=='ADVANCE_R5_ONLY_NO_H2_FIXEDNESS_MASK20_DIM5_OR_DOWNSTREAM_CREDIT'
    f=s['current_exact_frontier']
    assert f['a2_02_r4_retained_boundary_resolution_insufficiency_materialized'] is True
    for k in ['a2_02_r4_finite_cover_materialized','a2_02_r4_overlap_indices_materialized','a2_02_r4_component_uniformizers_materialized','a2_02_r4_literal_local_equations_materialized','a2_02_r4_overlap_transitions_materialized','a2_02_literal_mu2_2_cocycle_materialized','a2_02_equivalent_unimodular_cech_glue_materialized','a2_02_actual_swap23_gm_1_cochain_comparison_materialized','a2_02_semantic_action_difference_chain_witness_materialized','a2_02_swap23_seed_fixed_mod_pic2','a2_02_marked_brauer_image_excluded_from_mask20','a2_02_source_bound_stabilizer_fixed_subspace_materialized','a2_02_marked_brauer_image_computed']:
        assert f[k] is False,k
    assert f['a2_02_semantic_action_difference_verified_automorphisms']==[] and f['source_bound_proper14_evaluation_bits_materialized']==0
    assert s['stage33_progress']=='6/11'
    for k in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']:
        assert s['firewalls'][k] is False,k
    if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    if a.check or not a.write:
        print(json.dumps({'success':True,'marker':'V115_V91C1X_R4_HOSTILE_PASS_R5_ACTIVE','state_sha256':STATE_SHA,'r4_sha256':R4_SHA,'audit_review':AUDIT_REVIEW,'next_exact_leaf':NEXT,'next_expected_command':R5_COMMAND,'stage33_progress':'6/11'},sort_keys=True))
if __name__=='__main__': main()
