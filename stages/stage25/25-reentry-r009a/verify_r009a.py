#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
def text(p):
    q=ROOT/p; assert q.exists(),p; return q.read_text(encoding='utf-8')
def data(p): return json.loads(text(p))
ctrl=data('stages/stage25/25-reentry-controller.json')
audit=text('stages/stage25/25-reentry-r009a/audit.md')
res=text('stages/stage25/25-reentry-r009a/result.md')
s17=text('stages/stage17/post-stage25-r009a.md')
s23=text('stages/stage23/post-stage25-r009a.md')
assert 'AUDIT_VERDICT=PASS' in audit
assert ctrl['phase30_submission']['pr']==1005
assert ctrl['phase30_submission']['merge_commit']=='daf84757c185df6973936d2970a6307ab0bff62b'
r9=ctrl['r009a_submission']
assert r9['route_id']=='Stage25-um-r009a'
assert r9['audit_status']=='PASS'
closed=ctrl['status']=='CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY'
assert ctrl['stage26_gate']['stage26_allowed'] is closed
if closed:
    assert ctrl['current_phase']==70
    assert ctrl['phase70_submission']['audit_status']=='PASS'
    assert ctrl['phase70_submission']['merge_commit']=='be5f7d8360b3bac2b9060cd88ede596a4fb218dc'
    assert ctrl['next_expected_command']=='Stage26-main-batch'
if ctrl['current_phase']==30:
    assert r9['status']=='AUDITED_PASS_AWAITING_MERGE'
    assert ctrl['phases']['40']['status']=='BLOCKED_UNTIL_R009A_AUDIT_PASS_MERGE'
else:
    assert ctrl['current_phase'] in (40,50,60,70)
    assert r9['status']=='AUDITED_PASS_MERGED'
    assert r9['pr']==1006
    assert r9['merge_commit']=='4eb3349ee8ec02dcabb71bd1be3a48234356606b'
    assert not any(x['route_id']=='Stage25-um-r009a' and x['blocks_next_phase'] for x in ctrl['propagation_queue'])
for m in ('N_{2,a}=A_{ab,ac}-A_3','N_{2,b}=A_{ab,bc}-A_3','N_{2,c}=A_{ac,bc}-A_3'):
    assert m in res or m in s17 or m in s23
assert 'LITERAL_SURVIVAL_INTERPRETATION=false' in res
assert 'A3_QUARTER_POWER_CONTROL=false' in res
assert 'PERFECT_CUBOID_CONCLUSION=NONE' in res
print('STAGE25_REENTRY_R009A=PASS')
print('STAGE25_REENTRY_R009A_LIFECYCLE=PASS')
print('STAGE26_GATE=LIFECYCLE_VALID')
