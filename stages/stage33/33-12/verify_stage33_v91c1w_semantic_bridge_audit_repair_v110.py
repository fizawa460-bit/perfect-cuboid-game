#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

D=Path(__file__).resolve().parent
S33=D.parent
STATE=S33/'MAIN-STATE.json'
W=D/'e3-v91c1w-a2-02-all8-picard64-reduction.json'
AUTH=D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'
CTL=S33/'controller.json'

STATE_SHA='6991e41d18c9e06f4d2d4bedffc8f6ac4fbfd209e93012d7f5a7989d5e599241'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
NEXT='V91C1X_R1_MATERIALIZE_CHAIN_LEVEL_CECH_GM_COCHAIN_WITNESS_FOR_SWAP23_ACTION_DIFFERENCE_OR_KEEP_SEMANTIC_BRIDGE_BLOCKED'
BLOCKER='CHAIN_LEVEL_CECH_GM_COCHAIN_WITNESS_IDENTIFYING_SWAP23_SEED_ACTION_DIFFERENCE_WITH_THE_KUMMER_BOUNDARY_OF_THE_COMPUTED_CARTIER_CLASS'
FAIL_HEAD='3d96e40705995e6355c9570c2fe9e6eeddad8353'
FAIL_REVIEW=5127167940

def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(p,h):
    o=json.loads(p.read_text())
    b=dict(o)
    q=b.pop('canonical_sha256')
    assert q==h==csha(b), p
    return o

s=load(STATE,STATE_SHA)
w=load(W,W_SHA)
au=load(AUTH,AUTH_SHA)
ctl=json.loads(CTL.read_text())
cb=dict(ctl)
q=cb.pop('projection_canonical_sha256')
assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False

assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V48_V91C1W_RETAINED_SEMANTIC_ACTION_DIFFERENCE_BRIDGE_BLOCKER'
assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
assert s['authority_sync']['branch_candidate_frontier']=='V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO'
assert s['branch_exact_frontier_candidate']==str(W.relative_to(Path.cwd()))

cg=s['candidate_audit_gate']
assert cg['hostile_audit_verdict']=='FAIL'
assert cg['hostile_audit_review']==FAIL_REVIEW
assert cg['exact_audited_head']==FAIL_HEAD
assert cg['candidate_certificate_sha256']==W_SHA
assert cg['retained_subclaim']=='V91C1W_BOUNDED_PICARD64_AND_COMPLETE_SWAP23_PIC2_ZERO'
assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False

assert w['anti_inference']['zero_pic2_divisor_difference_promoted_to_h2_seed_fixedness'] is False
assert w['anti_inference']['zero_pic2_divisor_difference_promoted_to_marked_brauer_image'] is False
assert w['exact_result']['strict_scheme_count']==8
assert w['exact_result']['all_eight_exact_decomposition_or_source_bound_relation'] is True
assert w['exact_result']['complete_swap23_difference_zero_mod2'] is True
assert w['exact_result']['complete_swap23_difference_mod2_support_one_based']==[]
assert w['exact_consequence']['a2_02_swap23_seed_fixed_mod_pic2_promoted'] is False
assert w['exact_consequence']['a2_02_marked_brauer_image_excluded_from_mask20'] is False

f=s['current_exact_frontier']
assert f['a2_02_swap23_complete_difference_zero_in_retained_picard_mod2'] is True
for k in [
    'a2_02_swap23_seed_fixed_mod_pic2',
    'a2_02_sign_b1_seed_fixed_mod_pic2',
    'a2_02_sign_a2_seed_fixed_mod_pic2',
    'a2_02_marked_brauer_image_must_be_swap23_fixed',
    'a2_02_marked_brauer_image_must_be_sign_b1_fixed',
    'a2_02_marked_brauer_image_must_be_sign_a2_fixed',
    'a2_02_marked_brauer_image_excluded_from_mask20',
    'a2_02_semantic_action_difference_chain_witness_materialized',
    'a2_02_source_bound_stabilizer_fixed_subspace_materialized']:
    assert f[k] is False, k
assert f['a2_02_semantic_action_difference_verified_automorphisms']==[]
assert f['a2_02_semantic_action_difference_blocked_automorphisms']==['swap23','sign_b1','sign_a2']
assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2'] is None
assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality'] is None
assert f['a2_02_minimal_source_bound_discriminator_positions_one_based']==[]
assert f['a2_02_marked_brauer_image_computed'] is False
assert f['source_bound_proper14_evaluation_bits_materialized']==0

assert s['current']['active_missing_interface']==BLOCKER
assert s['current']['next_exact_leaf']==NEXT
assert s['execution_gate']['advance_allowed'] is True
assert s['execution_gate']['next_expected_command']=='STAGE33_MAIN_BATCH_V91C1X_R1_CHAIN_LEVEL_ACTION_DIFFERENCE_BRIDGE'
assert s['stage33_progress']=='6/11'
assert s['firewalls']['merge_allowed'] is False
assert au['canonical_sha256']==AUTH_SHA

print(json.dumps({
    'success':True,
    'marker':'V110_V91C1W_RETAINED_SEMANTIC_ACTION_DIFFERENCE_BRIDGE_BLOCKER',
    'state_sha256':STATE_SHA,
    'candidate_sha256':W_SHA,
    'hostile_audit_review':FAIL_REVIEW,
    'next_exact_leaf':NEXT,
    'credit':False,
    'stage33_progress':'6/11'
},sort_keys=True))
