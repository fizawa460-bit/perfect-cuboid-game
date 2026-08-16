#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel; assert p.exists(), rel; return p.read_text(encoding='utf-8')
def data(rel): return json.loads(text(rel))

reg=data('stages/stage25/25-reentry-r010a/backflow-registry.json')
res=text('stages/stage25/25-reentry-r010a/result.md')
s18=text('stages/stage18/post-stage25-r010a.md')
s20=text('stages/stage20/post-stage25-r010a.md')
s22=text('stages/stage22/post-stage25-r010a.md')
p40audit=text('stages/stage25/25-reentry-40/audit.md')
ctrl=data('stages/stage25/25-reentry-controller.json')

assert 'AUDIT_VERDICT=PASS' in p40audit
assert reg['route_id']=='Stage25-um-r010a'
assert reg['parent_pr']==1007
assert reg['parent_merge_commit']=='eebe4cd59caef804be76508f3773f2af6c7d47f2'
assert reg['affected_stages']==[18,20,22]
for j in ('a','b','c'):
    assert reg['directional_identities'][j]==f'P_{j}=M2,{j}+M3'
assert reg['directional_asymptotics']['third_face_ratio'].endswith("(log B)^(-eta)->0")
assert reg['directional_asymptotics']['postfilter'].endswith("->1")
assert reg['fine_mechanism']['directional_robustness_proved'] is True
assert reg['fine_mechanism']['averaging_artifact_excluded'] is True
assert reg['fine_mechanism']['third_face_postfilter_as_leading_cause_excluded'] is True
assert reg['fine_mechanism']['four_independent_log_factors_proved'] is False
assert reg['fine_mechanism']['status']=='OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM'
for marker in ('G22_LOG4_FINE_MECHANISM=OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM','FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false','PERFECT_CUBOID_CONCLUSION=NONE'):
    assert marker in res
assert 'DIRECTIONAL_THIRD_FACE_POSTFILTER_TO_ONE=true' in s18
assert 'M3_LOWER_ORDER_IN_EACH_M2_DIRECTION=true' in s20
assert 'LIVE_FINE_MECHANISM_LOCUS=ONE_FACE_VS_SHARED_EDGE_DOUBLE_PYTHAGOREAN_RANK6_TORIC_INTERNAL_COUNTING' in s22
assert 'DIRECTIONAL_STAGE22_CONSTANTS_SYNCED=true' in s22

r10=ctrl['r010a_submission']
assert r10['route_id']=='Stage25-um-r010a'
assert r10['parent_pr']==1007
assert r10['parent_merge_commit']=='eebe4cd59caef804be76508f3773f2af6c7d47f2'
assert ctrl['stage26_gate']['stage26_allowed'] is False

if ctrl['current_phase']==40:
    assert ctrl['phases']['50']['status']=='BLOCKED_UNTIL_R010A_AUDIT_PASS_MERGE'
    assert ctrl['propagation_queue'][-1]['route_id']=='Stage25-um-r010a'
    if reg['audit_status']=='PENDING':
        assert r10['audit_status']=='PENDING'
        assert r10['advance_allowed'] is False
        assert r10['merge_allowed'] is False
    elif reg['audit_status']=='PASS':
        assert r10['audit_status']=='PASS'
        assert r10['status']=='AUDITED_PASS_AWAITING_MERGE'
        assert r10['advance_allowed'] is True
        assert r10['merge_allowed'] is True
    else:
        raise AssertionError(f"unexpected registry audit state: {reg['audit_status']}")
else:
    # Immutable r010a theorem/receiver audit after its PR has merged and later phases are active.
    assert ctrl['current_phase']>=50
    assert r10['audit_status']=='PASS'
    assert r10['status']=='AUDITED_PASS_MERGED'
    assert r10['pr']==1008
    assert r10['merge_commit']=='9d2e767697a33195e756af6b366cb6f0548494d3'
    q=[x for x in ctrl['propagation_queue'] if x['route_id']=='Stage25-um-r010a']
    assert len(q)==1
    assert q[0]['status']=='AUDITED_PASS_MERGED'
    assert q[0]['blocks_next_phase'] is False

print('STAGE25_REENTRY_R010A_PARENT_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_R010A_RECEIVER_SYNC=PASS')
print('STAGE25_REENTRY_R010A_FINE_MECHANISM_BOUNDARY=PASS')
print('STAGE25_REENTRY_R010A_LIFECYCLE=PASS')
print('STAGE26_GATE=BLOCKED_VALID')
