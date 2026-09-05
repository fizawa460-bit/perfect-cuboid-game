#!/usr/bin/env python3
"""Replay Stage35-EX history through user-approved merged 35EX-33 against immutable V32 snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V33='STAGE35_EX_PESCH_E1_STATE_V33_POST_35EX33_USER_APPROVED_ROUTE_BLOCKER'
V32='STAGE35_EX_PESCH_E1_STATE_V32_POST_35EX32_USER_APPROVED_MERGE_ROUTE_SELECTION'
SNAPSHOT='e21378e59f7f1076a7ad71d34cee1fd0ac3a5cb3'
ALLOWED={'base', *{str(i) for i in range(10,33)}, '32p', '33g1', '33g2', '33'}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v33_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V33 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['history_snapshot']['commit_sha']==SNAPSHOT
assert real['history_snapshot']['schema']==V32
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-33'
assert real['parent_authority']['audit_verdict']=='PASS_USER_APPROVED'
assert real['parent_authority']['route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
assert real['current']['unit']=='35EX-34_POST_GAUSSIAN_BLOCK_FRESH_BREADTH_AUDIT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text=subprocess.check_output(
    ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT,text=True,stderr=subprocess.STDOUT,
)
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V32
assert snapshot['current']['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert snapshot['current']['status']=='PROVISIONAL_EXACT_ROUTE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    if target in {'base', *{str(i) for i in range(10,33)}}:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v32_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v32_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
    elif target=='32p':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_32_merged_promotion.py'),run_name='__main__')
    elif target=='33g1':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_33_goal1.py'),run_name='__main__')
    elif target=='33g2':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_33_goal2.py'),run_name='__main__')
    elif target=='33':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_33_blocker.py'),run_name='__main__')
finally:
    Path.read_text=original_read_text
print(f'PASS V33_IMMUTABLE_V32_HISTORY_REPLAY_{target}')
