#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / 'stages/stage35-ex'
ART = HERE / '35ex-35/goal4af-c5-direct-marked-picard-target-span.json'
LOCK = HERE / '35ex-35/goal4af-c5-direct-marked-picard-target-span-source-lock.md'
SNAP = HERE / 'snapshots/MAIN-STATE-V68-00d4c9bf9bb3.json'
DIAG = HERE / 'diagnose_stage35_ex_35_goal4af_c5_target_span.py'
STATE = HERE / 'MAIN-STATE.json'

EXPECTED_ART_BLOB = 'eacc4a127fdf0e111ca8db91bc17418747b3fb01'
EXPECTED_LOCK_BLOB = 'e84ceb08ac156cb7e27713f6e4cfd81c8b29dd0c'
EXPECTED_SNAP_BLOB = '76dcee723c1f7ef465eb9830093dc85910da8aa9'
EXPECTED_DIAG_BLOB = '3a5045f7f3c48a2f93a8116090beca1422bafac3'
EXPECTED_CANON = '08b2efc4d66655858b49cf542138a9ead97a387f070d749b448f8b6f02036845'
EXPECTED_UPSTREAM = '0422b69847f2afb97cb7b3ed02ebef91279f61b1'
V69 = 'STAGE35_EX_PESCH_E1_STATE_V69_GOAL4AF_C5_MARKED_PICARD_ADAPTER_COMPUTED_TARGET_SPAN_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


assert git_blob(ART) == EXPECTED_ART_BLOB
assert git_blob(LOCK) == EXPECTED_LOCK_BLOB
assert git_blob(SNAP) == EXPECTED_SNAP_BLOB
assert git_blob(DIAG) == EXPECTED_DIAG_BLOB

art = json.loads(ART.read_text())
canon = art.pop('canonical_sha256')
assert canon == EXPECTED_CANON == csha(art)
assert art['schema'] == 'STAGE35_EX_GOAL4AF_C5_MARKED_PICARD_TARGET_SPAN_V1'
assert art['parent']['source_head_sha'] == '00d4c9bf9bb37781c81954fb41f22e97d721995b'
assert art['parent']['snapshot_file_commit_sha'] == 'bf16d58cc1d85a930073184a2ac6309e5ff4d095'
assert art['source_locks']['upstream_stoll']['git_blob_sha1'] == EXPECTED_UPSTREAM
assert art['exact_runs']['marked_picard_receiver'] == {
    'head_sha':'5b395e62f83337959297794e93ca1e6facb0828d','workflow_run':34071239834,
    'job':101588889887,'conclusion':'SUCCESS'}
assert art['exact_runs']['target_span'] == {
    'head_sha':'00d4c9bf9bb37781c81954fb41f22e97d721995b','workflow_run':34071619263,
    'job':101589927928,'conclusion':'SUCCESS'}

# Permanent exact replay of the marked rows and target-span calculation.
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(DIAG))
out = ns['out']
summary = ns['summary']
marked64 = [[int(x) for x in r] for r in ns['marked64']]
ma = art['marked_picard_adapter']
assert summary['pair_rows_materialized'] is True and summary['pair_count'] == ma['pair_count'] == 8
assert summary['goal4ac_residual_pair_count'] == ma['goal4ac_residual_pair_count'] == 4
assert len({tuple(r) for r in marked64}) == ma['distinct_residual_marked_picard64_class_count'] == 2
assert set(map(tuple, marked64)) == {tuple(ma['class_A_INDLIST64']), tuple(ma['class_B_INDLIST64'])}
assert all(r['strict_pair_INDLIST64'] == r['total_pullback_pair_INDLIST64'] for r in summary['goal4ac_residual_pairs'])
assert ma['strict_equals_total_for_residual_rows'] is True
assert ma['contracted_exceptional_correction_zero_for_residual_rows'] is True
assert ma['pair_square_or_antipodal_relation_used_as_solver_constraint'] is False

span = art['target_span']
assert out['goal4ab_linear_section_column_count'] == span['base_complete_linear_section_column_count'] == 43
assert out['goal4ab_linear_section_span_rank'] == span['base_span_rank'] == 31
assert out['formal_target_support_count'] == span['formal_target_support_count'] == 69
assert out['c5_residual_embedded_column_rank'] == span['c5_residual_embedded_column_rank'] == 2
assert out['augmented_column_count'] == span['augmented_column_count'] == 47
assert out['augmented_span_rank'] == span['augmented_span_rank'] == 33
assert out['formal_target_in_Q_span_after_adjoining_c5_marked_representatives'] is False
assert span['formal_target_in_Q_span_after_adjoining_c5_marked_representatives'] is False
assert out['actual_C5_support_identified_with_marked_representative'] is False

rr = art['route_result']
assert rr['goal4af_executed'] is True
assert rr['c5_pair_marked_picard_adapter_computed'] is True
assert rr['target_span_with_c5_pairs_computed'] is True
assert rr['general_qi_principal_function_problem'] == 'OPEN'
assert rr['next'] == '35EX-35_GOAL4AG_SECOND_CLASS_QI_CYCLIC_GRADED_COORDINATE_RING_PRINCIPAL_FUNCTION_SYNTHESIS_PREFLIGHT'
fw = art['credit_firewall']
for k in ('hostile_audit_pass','actual_C5_support_materialized_in_140_packet','explicit_F_B_materialized',
          'global_F_B_nonexistence_proved','general_principal_function_problem_closed','full_Br_a_U_computed',
          'local_evaluations_computed','verticality_proved','brauer_manin_obstruction_obtained','theorem_credit',
          'endpoint_credit','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed',
          'perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert fw[k] is False, k

state = json.loads(STATE.read_text())
assert state['schema'] == V69
assert state['current']['unit'] == art['unit']
assert state['claims']['goal4af_executed'] is True
assert state['claims']['open_receiver_second_class_C5_pair_marked_picard_adapter_computed'] is True
assert state['claims']['open_receiver_second_class_C5_distinct_residual_marked_picard_class_count'] == 2
assert state['claims']['open_receiver_second_class_target_span_with_C5_pairs_computed'] is True
assert state['claims']['open_receiver_second_class_target_in_augmented_C5_marked_span'] is False
assert state['claims']['open_receiver_second_class_augmented_C5_marked_span_rank'] == 33
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['open_receiver_second_class_global_F_B_nonexistence_proved'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

print(json.dumps({
    'success': True,
    'goal4af_marked_picard_adapter': 'PASS',
    'residual_pair_count': 4,
    'distinct_marked_picard64_class_count': 2,
    'base_span_rank': 31,
    'augmented_span_rank': 33,
    'target_in_augmented_span': False,
    'explicit_F_B_materialized': False,
    'theorem_credit': False,
    'endpoint_credit': False,
}, sort_keys=True))
