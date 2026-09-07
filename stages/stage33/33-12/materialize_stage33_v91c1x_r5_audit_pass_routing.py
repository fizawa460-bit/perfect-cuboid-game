#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
STATE = S33 / 'MAIN-STATE.json'
R4 = HERE / 'e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json'

OLD_STATE_SHA = '46115ccafb577bdec61a3ce379d903fc0121f6dd083a502a1b889bc87179c102'
R4_SHA = 'cead57f641b02e8defb8cb614ee1b1acdca1ee6d1e9f7c04514ccfffef5577e0'
AUDITED_HEAD = '4dd839ec21ece8ef08c25cb385e28050720dda77'
AUDIT_REVIEW = 5128292956
AUDIT_REVIEW_NODE = 'PRR_kwDOTr52Y88AAAABMauKXA'
AUDIT_SUBMITTED_AT = '2026-09-07T05:21:36Z'
MERGE_COMMIT = '726198a3d8ca4834e45c2ef275a75266b0f752b4'
NEXT = 'V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE'
MISSING = 'NEW_SOURCE_BOUND_A2_02_FINITE_COVER_WITH_LITERAL_LOCAL_EQUATIONS_UNIFORMIZERS_OVERLAP_TRANSITIONS_AND_SWAP23_COMMON_REFINEMENT_SUFFICIENT_TO_MATERIALIZE_Z_IJK_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_IDENTITY'


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding='utf-8'))
    body = dict(obj)
    claimed = body.pop('canonical_sha256')
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f'canonical lock moved for {path}: claimed={claimed} actual={actual} expected={expected}')
    return obj


s = load_locked(STATE, OLD_STATE_SHA)
r4 = load_locked(R4, R4_SHA)
if r4['next_exact_leaf_after_audit'] != NEXT or r4['next_missing_object'] != MISSING:
    raise SystemExit('R4 next-leaf contract moved')
if r4['credit'] != 'NONCREDIT_CONSTRUCTION_BLOCKER':
    raise SystemExit('R4 credit boundary moved')

s['schema'] = 'STAGE33_MAIN_COMPACT_STATE_V54_V91C1X_R4_HOSTILE_PASS_R5_ACTIVE'
s['authority_sync']['status'] = 'V91C1V_AUTHORITY_R4_HOSTILE_PASS_R5_CONSTRUCTION_ACTIVE'

cg = s['candidate_audit_gate']
cg.update({
    'status': 'HOSTILE_AUDIT_PASS_MERGED_NONCREDIT_R4_CHECKPOINT',
    'audit_pass_credit': True,
    'exact_audited_head': AUDITED_HEAD,
    'hostile_audit_review': AUDIT_REVIEW,
    'hostile_audit_review_node': AUDIT_REVIEW_NODE,
    'hostile_audit_submitted_at': AUDIT_SUBMITTED_AT,
    'hostile_audit_verdict': 'PASS',
    'mathematical_authority_promoted': False,
    'merge_allowed': False,
    'merged': True,
    'merge_commit': MERGE_COMMIT,
})

cp = s['continuation_provenance']
cp['hostile_audit_pass_claimed'] = True
pol = cp['grouped_hostile_audit_policy']
pol['current_stop_reason'] = 'R4_GROUPED_HOSTILE_AUDIT_PASS_R5_CONSTRUCTION_ACTIVE'
pol['hostile_audit_still_required_before_authority_credit_or_merge'] = False
pol['stop_when'] = []
cp['x_r4_grouped_hostile_audit'] = {
    'pr': 1682,
    'review': AUDIT_REVIEW,
    'review_node': AUDIT_REVIEW_NODE,
    'submitted_at': AUDIT_SUBMITTED_AT,
    'exact_audited_head': AUDITED_HEAD,
    'verdict': 'PASS',
    'checkpoint_credit': 'NONCREDIT_CONSTRUCTION_BLOCKER_ONLY',
    'authority_unchanged': True,
    'stage33_progress_unchanged': True,
    'merge_commit': MERGE_COMMIT,
    'merged': True,
    'next_exact_leaf': NEXT,
}

s['current']['substep'] = 'E3_V91C1X_R5_SOURCE_BOUND_COVER_GLUE_PACKAGE_ACTIVE'
s['current']['active_missing_interface'] = MISSING
s['current']['next_exact_leaf'] = NEXT
s['execution_gate'] = {
    'advance_allowed': True,
    'advance_scope': 'V91C1X_R5_SOURCE_BOUND_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE_ONLY',
    'next_expected_command': 'STAGE33_MAIN_BATCH_V91C1X_R5_COVER_GLUE_PACKAGE',
    'stop_semantics': 'ADVANCE_R5_ONLY_NO_H2_FIXEDNESS_MASK20_DIM5_OR_DOWNSTREAM_CREDIT',
}

s['resolved_investigations']['e3_v91c1x_r4_retained_boundary_resolution_insufficiency'] = (
    'HOSTILE_AUDIT_PASS_MERGED_BOUNDED_NONCREDIT_CONSTRUCTION_BLOCKER_'
    'INSPECTED_RETAINED_CHAIN_INSUFFICIENT_NO_REPOSITORY_WIDE_ABSENCE_OR_IMPOSSIBILITY_CLAIM'
)
s['work_checkpoint']['status'] = 'V91C1X_R4_HOSTILE_PASS_MERGED_R5_CONSTRUCTION_ACTIVE'

# Keep startup focused on the exact R5 inputs.  These paths already exist at
# the audited/merged R4 checkpoint and are sufficient for Arsenal-first search
# plus a fresh source-bound construction attempt.
s['current_leaf_working_set'] = [
    'docs/research-os/policies/repository-asset-discovery.md',
    'docs/arsenal/index.json',
    'docs/arsenal/cards/provisional/S33-PW04.md',
    'docs/arsenal/cards/provisional/S33-PW07.md',
    'docs/arsenal/cards/provisional/S33-PW08.md',
    'stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json',
    'stages/stage33/33-12/e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json',
    'stages/stage33/33-12/e3-v91c1x-r4-a2-02-local-chart-inventory.json',
    'stages/stage33/33-12/diagnose_e3_v91c1x_r4_exceptional_chart_selector.py',
    'stages/stage33/33-07/materialize_mixed_order_side_ambient_function_lifts.py',
    'stages/stage33/33-07/materialize_mixed_order_exceptional_ambient_tangent_function_lifts.py',
]

# No mathematical authority/credit promotion.
for key in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']:
    if s['firewalls'][key] is not False:
        raise SystemExit(f'firewall unexpectedly true before R5: {key}')
if s['stage33_progress'] != '6/11':
    raise SystemExit('Stage33 progress moved unexpectedly')
if s['authority_sync']['frontier_authority'] != 'V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT':
    raise SystemExit('mathematical authority moved unexpectedly')

body = dict(s)
body.pop('canonical_sha256', None)
s['canonical_sha256'] = csha(body)
STATE.write_text(json.dumps(s, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
print(json.dumps({
    'success': True,
    'marker': 'V91C1X_R5_R4_HOSTILE_PASS_ROUTING_MATERIALIZED',
    'state_sha256': s['canonical_sha256'],
    'r4_sha256': R4_SHA,
    'audit_review': AUDIT_REVIEW,
    'audit_review_node': AUDIT_REVIEW_NODE,
    'audited_head': AUDITED_HEAD,
    'merge_commit': MERGE_COMMIT,
    'next_exact_leaf': NEXT,
    'stage33_progress': '6/11',
}, sort_keys=True))
