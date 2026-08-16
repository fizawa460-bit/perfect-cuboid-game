#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

reg = data('stages/stage25/25-reentry-r010a/backflow-registry.json')
res = text('stages/stage25/25-reentry-r010a/result.md')
s18 = text('stages/stage18/post-stage25-r010a.md')
s20 = text('stages/stage20/post-stage25-r010a.md')
s22 = text('stages/stage22/post-stage25-r010a.md')
p40audit = text('stages/stage25/25-reentry-40/audit.md')
ctrl = data('stages/stage25/25-reentry-controller.json')

assert 'AUDIT_VERDICT=PASS' in p40audit
assert reg['route_id'] == 'Stage25-um-r010a'
assert reg['parent_pr'] == 1007
assert reg['parent_merge_commit'] == 'eebe4cd59caef804be76508f3773f2af6c7d47f2'
assert reg['affected_stages'] == [18,20,22]

for j in ('a','b','c'):
    assert reg['directional_identities'][j] == f'P_{j}=M2,{j}+M3'
assert reg['directional_asymptotics']['third_face_ratio'].endswith("(log B)^(-eta)->0")
assert reg['directional_asymptotics']['postfilter'].endswith("->1")
assert reg['fine_mechanism']['directional_robustness_proved'] is True
assert reg['fine_mechanism']['averaging_artifact_excluded'] is True
assert reg['fine_mechanism']['third_face_postfilter_as_leading_cause_excluded'] is True
assert reg['fine_mechanism']['four_independent_log_factors_proved'] is False
assert reg['fine_mechanism']['status'] == 'OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM'

for marker in (
    'G22_LOG4_FINE_MECHANISM=OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM',
    'FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
):
    assert marker in res
assert 'DIRECTIONAL_THIRD_FACE_POSTFILTER_TO_ONE=true' in s18
assert 'M3_LOWER_ORDER_IN_EACH_M2_DIRECTION=true' in s20
assert 'LIVE_FINE_MECHANISM_LOCUS=ONE_FACE_VS_SHARED_EDGE_DOUBLE_PYTHAGOREAN_RANK6_TORIC_INTERNAL_COUNTING' in s22
assert 'DIRECTIONAL_STAGE22_CONSTANTS_SYNCED=true' in s22

r10 = ctrl['r010a_submission']
assert r10['route_id'] == 'Stage25-um-r010a'
assert r10['parent_pr'] == 1007
assert r10['parent_merge_commit'] == 'eebe4cd59caef804be76508f3773f2af6c7d47f2'
assert r10['audit_status'] == 'PENDING'
assert r10['advance_allowed'] is False
assert r10['merge_allowed'] is False
assert ctrl['current_phase'] == 40
assert ctrl['phases']['40']['status'] == 'AUDITED_PASS_MERGED_BACKFLOW_SUBMITTED_PENDING_AUDIT'
assert ctrl['phases']['50']['status'] == 'BLOCKED_UNTIL_R010A_AUDIT_PASS_MERGE'
assert ctrl['propagation_queue'][-1]['route_id'] == 'Stage25-um-r010a'
assert ctrl['propagation_queue'][-1]['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert ctrl['stage26_gate']['stage26_allowed'] is False
assert ctrl['next_expected_command'] == 'Stage25-reentry-audit'

print('STAGE25_REENTRY_R010A_PARENT_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_R010A_RECEIVER_SYNC=PASS')
print('STAGE25_REENTRY_R010A_FINE_MECHANISM_BOUNDARY=PASS')
print('STAGE25_REENTRY_R010A_PHASE50_GATE=BLOCKED_VALID')
print('STAGE26_GATE=BLOCKED_VALID')
