#!/usr/bin/env python3
"""Replay Stage35-EX history through merged 35EX-32 against the immutable V31 snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V32='STAGE35_EX_PESCH_E1_STATE_V32_POST_35EX32_USER_APPROVED_MERGE_ROUTE_SELECTION'
V31='STAGE35_EX_PESCH_E1_STATE_V31_POST_35EX32_ENDPOINT_POPULATION_BREADTH_AUDIT'
SNAPSHOT='3fbcecfb17c8eadde6479ee4c6f55c80be32cf42'
ALLOWED={'base', *{str(i) for i in range(10,33)}}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v32_legacy_replay.py {base|10|...|32}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V32 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['history_snapshot']['commit_sha']==SNAPSHOT
assert real['history_snapshot']['schema']==V31
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-32'
assert real['parent_authority']['hostile_audit_pass'] is False
assert real['parent_authority']['route_selection_authorized_by_user_merge'] is True
assert real['current']['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

try:
    snapshot_text=subprocess.check_output(
        ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
        cwd=ROOT,text=True,stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit('immutable V31 snapshot unavailable in checkout\n'+exc.output) from exc
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V31
assert snapshot['current']['unit']=='35EX-32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    if target=='32':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_32.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v31_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v31_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V32_IMMUTABLE_V31_HISTORY_REPLAY_35EX_{target}')
