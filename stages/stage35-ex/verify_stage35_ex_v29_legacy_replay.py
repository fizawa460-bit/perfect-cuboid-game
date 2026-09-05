#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers against the immutable V28 state snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V29='STAGE35_EX_PESCH_E1_STATE_V29_POST_35EX30_ENDPOINT_GAUGE_RETURN_FIREWALL'
V28='STAGE35_EX_PESCH_E1_STATE_V28_POST_35EX29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION'
V28_COMMIT='38434ea3c4124efd1cc04a228e85b2fd207f2c14'
ALLOWED={'base', *{str(i) for i in range(10,30)}}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v29_legacy_replay.py {base|10|...|29}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V29 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==V28_COMMIT
hs=real['history_snapshot']
assert hs['commit_sha']==V28_COMMIT and hs['schema']==V28
assert hs['role']=='IMMUTABLE_COMPLETE_V28_HISTORY_AND_AUTHORITY_SNAPSHOT'
assert hs['history_dropped'] is False
parent=real['parent_authority']
assert parent['unit']=='35EX-29'
assert parent['hostile_audit_verdict']=='PASS'
assert parent['hostile_audit_review_node_id']=='PRR_kwDOTr52Y88AAAABMS3Ipg'
assert parent['audited_head_sha']=='21ce592d3f30fd10b421ed0d3be68a702c26c65a'
assert parent['exact_head_ci_run']==33946860829 and parent['exact_head_ci_job']==101254427135
assert parent['merged_main_sha']==V28_COMMIT
assert real['completed_units_delta']['35EX-29']['status']=='AUDITED_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'
assert real['completed_units_delta']['35EX-30']['status']=='PROVISIONAL_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'
assert real['current']['unit']=='35EX-30_ENDPOINT_GAUGE_RETURN_FIREWALL'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

try:
    snapshot_text=subprocess.check_output(
        ['git','show',f'{V28_COMMIT}:stages/stage35-ex/MAIN-STATE.json'],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit(
        'immutable V28 snapshot commit is not available in checkout; '
        'workflow must fetch enough history to include '+V28_COMMIT+'\n'+exc.output
    ) from exc
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V28
assert snapshot['base_main_sha']=='5fa33e600b81fc34f4be9b22761c8079b31d7806'
assert snapshot['current']['unit']=='35EX-29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_OR_JOINT_LOCAL_FIREWALL'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert snapshot['completed_units']['35EX-28B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert snapshot['completed_units']['35EX-29']['status']=='PROVISIONAL_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    if target=='29':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_29.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v28_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v28_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V29_IMMUTABLE_V28_HISTORY_REPLAY_35EX_{target}')
