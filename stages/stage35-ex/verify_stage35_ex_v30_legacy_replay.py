#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers against the immutable V29 state snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V30='STAGE35_EX_PESCH_E1_STATE_V30_POST_35EX31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE'
V29='STAGE35_EX_PESCH_E1_STATE_V29_POST_35EX30_ENDPOINT_GAUGE_RETURN_FIREWALL'
BASE_MAIN='05c229420a7c73886fedbece2d746b36ed3d91d5'
V29_COMMIT='3d63864b0a10a53549f64a9e0dc3acf6f59ef9c0'
ALLOWED={'base', *{str(i) for i in range(10,31)}}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v30_legacy_replay.py {base|10|...|30}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V30 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==BASE_MAIN
hs=real['history_snapshot']
assert hs['commit_sha']==V29_COMMIT and hs['schema']==V29
assert hs['role']=='IMMUTABLE_COMPLETE_V29_HISTORY_AND_AUTHORITY_SNAPSHOT'
assert hs['history_dropped'] is False
parent=real['parent_authority']
assert parent['unit']=='35EX-30'
assert parent['hostile_audit_verdict']=='PASS'
assert parent['hostile_audit_review_node_id']=='PRR_kwDOTr52Y88AAAABMS_hqA'
assert parent['audited_head_sha']=='00d6199c0df611b0606b15b8a46897629363cb10'
assert parent['exact_head_ci_run']==33950151293 and parent['exact_head_ci_job']==101263267837
assert parent['merged_main_sha']==V29_COMMIT
assert real['completed_units_delta']['35EX-30']['status']=='AUDITED_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'
assert real['completed_units_delta']['35EX-31']['status']=='PROVISIONAL_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_CREDIT'
assert real['current']['unit']=='35EX-31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE_OR_ENDPOINT_SCALE_BLOCKER'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

try:
    snapshot_text=subprocess.check_output(
        ['git','show',f'{V29_COMMIT}:stages/stage35-ex/MAIN-STATE.json'],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit(
        'immutable V29 snapshot commit is not available in checkout; '
        'workflow must fetch enough history to include '+V29_COMMIT+'\n'+exc.output
    ) from exc
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V29
assert snapshot['base_main_sha']=='38434ea3c4124efd1cc04a228e85b2fd207f2c14'
assert snapshot['current']['unit']=='35EX-30_ENDPOINT_GAUGE_RETURN_FIREWALL'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert snapshot['completed_units_delta']['35EX-29B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert snapshot['completed_units_delta']['35EX-30']['status']=='PROVISIONAL_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    if target=='30':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_30.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v29_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v29_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V30_IMMUTABLE_V29_HISTORY_REPLAY_35EX_{target}')
