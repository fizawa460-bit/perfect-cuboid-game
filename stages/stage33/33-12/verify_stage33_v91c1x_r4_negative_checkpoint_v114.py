#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
STATE_SHA='46115ccafb577bdec61a3ce379d903fc0121f6dd083a502a1b889bc87179c102'
R4_SHA='cead57f641b02e8defb8cb614ee1b1acdca1ee6d1e9f7c04514ccfffef5577e0'
CAND='V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_DATA_INSUFFICIENT_FOR_COVER_INDEXED_A2_02_H2_REPRESENTATIVE'
MISSING='NEW_SOURCE_BOUND_A2_02_FINITE_COVER_WITH_LITERAL_LOCAL_EQUATIONS_UNIFORMIZERS_OVERLAP_TRANSITIONS_AND_SWAP23_COMMON_REFINEMENT_SUFFICIENT_TO_MATERIALIZE_Z_IJK_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_IDENTITY'
NEXT='V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE'
AUDIT='HOSTILE_AUDIT_PR_1682_V91C1X_R4_NEGATIVE_CHECKPOINT_EXACT_HEAD'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

s=load(S33/'MAIN-STATE.json',STATE_SHA)
r4=load(HERE/'e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json',R4_SHA)
assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V53_V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_CHECKPOINT'
assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
assert s['authority_audit_gate']['hostile_audit_verdict']=='PASS' and s['authority_audit_gate']['merged'] is True
r3a=s['continuation_provenance']['x_r3_grouped_hostile_audit']
assert r3a['pr']==1678 and r3a['verdict']=='PASS' and r3a['merged'] is True and r3a['authority_unchanged'] is True
assert s['candidate_audit_gate']['candidate']==CAND and s['candidate_audit_gate']['candidate_certificate_sha256']==R4_SHA
assert s['candidate_audit_gate']['pr']==1682 and s['candidate_audit_gate']['status']=='PENDING_GROUPED_HOSTILE_AUDIT_R4_NEGATIVE_CHECKPOINT'
assert s['candidate_audit_gate']['audit_pass_credit'] is False and s['candidate_audit_gate']['mathematical_authority_promoted'] is False
assert r4['candidate']==CAND and r4['credit']=='NONCREDIT_CONSTRUCTION_BLOCKER'
assert r4['exact_consequence']=='THE_INSPECTED_RETAINED_BOUNDARY_RESOLUTION_CHAIN_IS_INSUFFICIENT_TO_MATERIALIZE_THE_R2_ACCEPTED_COVER_INDEXED_A2_02_H2_REPRESENTATIVE'
assert r4['next_missing_object']==MISSING and r4['next_exact_leaf_after_audit']==NEXT
for k in ['repository_wide_search_claim','repository_wide_absence_claim','mathematical_nonexistence_claim','route_mathematically_impossible_claim']:
    assert r4['bounded_scope'][k] is False,k
for k in ['finite_cover_materialized','overlap_indices_materialized','component_uniformizers_materialized','literal_local_equations_materialized','overlap_transitions_materialized','equivalent_unimodular_cech_glue_materialized','literal_mu2_2_cocycle_materialized','swap23_common_refinement_materialized','line_bundle_gm_1_cocycle_ell_ij_materialized','square_root_1_cochain_r_ij_materialized','triple_overlap_identity_verified']:
    assert r4['bounded_findings'][k] is False,k
for k in ['accepted_source_h2_representative_credit','h2_fixedness_credit','mask20_credit','sign_b1_h2_fixedness_credit','sign_a2_h2_fixedness_credit','source_bound_dim5_credit','marked_brauer_image_credit','stage33_close_credit','stage33_release_credit','theorem_credit','receiver_credit','endpoint_credit','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim','merge_allowed']:
    assert r4['credit_firewall'][k] is False,k
assert s['current']['active_missing_interface']==MISSING and s['current']['next_exact_leaf']==NEXT
assert s['execution_gate']['advance_allowed'] is False and s['execution_gate']['next_expected_command']==AUDIT
assert s['firewalls']['stage33_12_closed_exact'] is False and s['firewalls']['stage33_13_released'] is False and s['firewalls']['merge_allowed'] is False
assert s['stage33_progress']=='6/11'
subprocess.run([sys.executable,str(S33/'sync_main_state.py'),'--check'],check=True)
print(json.dumps({'success':True,'marker':'V114_V91C1X_R4_NEGATIVE_CHECKPOINT_CURRENT_STARTUP','state_sha256':STATE_SHA,'candidate_sha256':R4_SHA,'next_expected_command':AUDIT,'stage33_progress':'6/11'},sort_keys=True))
