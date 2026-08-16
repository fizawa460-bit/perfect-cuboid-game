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
assert ctrl['r009a_submission']['route_id']=='Stage25-um-r009a'
assert ctrl['r009a_submission']['audit_status']=='PASS'
assert ctrl['r009a_submission']['status']=='AUDITED_PASS_AWAITING_MERGE'
assert ctrl['phases']['40']['status']=='BLOCKED_UNTIL_R009A_AUDIT_PASS_MERGE'
assert ctrl['stage26_gate']['stage26_allowed'] is False
for m in ('N_{2,a}=A_{ab,ac}-A_3','N_{2,b}=A_{ab,bc}-A_3','N_{2,c}=A_{ac,bc}-A_3'):
    assert m in res or m in s17 or m in s23
assert 'LITERAL_SURVIVAL_INTERPRETATION=false' in res
assert 'A3_QUARTER_POWER_CONTROL=false' in res
assert 'PERFECT_CUBOID_CONCLUSION=NONE' in res
print('STAGE25_REENTRY_R009A=PASS')
print('STAGE25_REENTRY_R009A_LIFECYCLE=PASS')
print('STAGE26_GATE=BLOCKED_VALID')
