#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers against immutable V30 state at #1583 merge."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V31='STAGE35_EX_PESCH_E1_STATE_V31_POST_35EX32_ENDPOINT_POPULATION_BREADTH_AUDIT'
V30='STAGE35_EX_PESCH_E1_STATE_V30_POST_35EX31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE'
BASE_MAIN='c3a90a8c5ccda8a649131430b92366e5f8a4cee0'
V30_COMMIT='8211bb0ef80de61ecf39c3b97743c58f1193187a'
ALLOWED={'base', *{str(i) for i in range(10,32)}}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v31_legacy_replay.py {base|10|...|31}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V31 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==BASE_MAIN
hs=real['history_snapshot']
assert hs['commit_sha']==V30_COMMIT and hs['schema']==V30
assert hs['role']=='IMMUTABLE_COMPLETE_V30_HISTORY_THROUGH_35EX31_PROVISIONAL'
assert hs['history_dropped'] is False
parent=real['parent_authority']
assert parent['unit']=='35EX-31'
assert parent['hostile_audit_verdict']=='PASS_USER_APPROVED'
assert parent['final_exact_head_sha']=='9f1d3d73f41377bddb1296a3e6fc95b5e2fd8dd7'
assert parent['final_exact_head_ci_run']==33953462420 and parent['final_exact_head_ci_job']==101272407623
assert parent['merged_main_sha']==V30_COMMIT
assert real['completed_units_delta']['35EX-31']['status']=='AUDITED_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_E1_CREDIT'
assert real['completed_units_delta']['35EX-32']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['current']['unit']=='35EX-32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

try:
    snapshot_text=subprocess.check_output(
        ['git','show',f'{V30_COMMIT}:stages/stage35-ex/MAIN-STATE.json'],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit(
        'immutable V30 snapshot commit is not available in checkout; '
        'workflow must fetch enough history to include '+V30_COMMIT+'\n'+exc.output
    ) from exc
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V30
assert snapshot['base_main_sha']=='125504622b46e462bd5fe8d7016f18d59717d696'
assert snapshot['current']['unit']=='35EX-31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE_OR_ENDPOINT_SCALE_BLOCKER'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert snapshot['completed_units_delta']['35EX-31']['status']=='PROVISIONAL_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_CREDIT'

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    if target=='31':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_31.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v30_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v30_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V31_IMMUTABLE_V30_HISTORY_REPLAY_35EX_{target}')
