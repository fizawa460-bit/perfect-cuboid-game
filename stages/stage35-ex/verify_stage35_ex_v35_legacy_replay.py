#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged 35EX-35 against immutable V34 snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V35='STAGE35_EX_PESCH_E1_STATE_V35_POST_35EX35_HOSTILE_AUDITED_GOAL4_READY'
V34='STAGE35_EX_PESCH_E1_STATE_V34_POST_35EX34_HOSTILE_AUDITED_PRIVATE_GCD_PREFLIGHT'
LIVE_BASE='2f708b8f0b36483eb7ce19fbb4f7dcc6b9d9d0bc'
SNAPSHOT='17c53d659e8d5d49b6e2bfca5c65c38a8658ac0d'
OLD_ALLOWED={'base', *{str(i) for i in range(10,33)}, '32p', '33g1', '33g2', '33', '34'}
ALLOWED=OLD_ALLOWED|{'35'}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v35_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V35 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==LIVE_BASE
assert real['history_snapshot']['commit_sha']==SNAPSHOT
assert real['history_snapshot']['schema']==V34
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-35_GOALS_1_TO_3'
assert real['parent_authority']['audit_verdict']=='HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id']==5120979784
assert real['parent_authority']['pr']==1603
assert real['parent_authority']['exact_head_sha']=='51ae29a044d0e2524285e56237cf0e32269a54cf'
assert real['parent_authority']['exact_head_ci_run']==33961134707
assert real['parent_authority']['exact_head_ci_job']==101293098839
assert real['parent_authority']['merged_main_sha']==SNAPSHOT
assert real['current']['unit']=='35EX-35_GOAL4_FOURTH_SQUARE_RESTRICTION_TEST'
assert real['current']['status']=='READY_AFTER_HOSTILE_AUDITED_GOALS_1_TO_3_NO_E1_CREDIT'
assert real['claims']['35ex35_goals_1_to_3_hostile_audit_pass'] is True
assert real['claims']['goal4_fourth_square_restriction_test_completed'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text=subprocess.check_output(
    ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT,text=True,stderr=subprocess.STDOUT,
)
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V34
assert snapshot['current']['unit']=='35EX-35_PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_PREFLIGHT'
assert snapshot['current']['status']=='PROVISIONAL_EXACT_GOALS_1_TO_3_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert snapshot['claims']['goal4_fourth_square_restriction_test_completed'] is False

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    old_argv=sys.argv[:]
    try:
        if target in OLD_ALLOWED:
            sys.argv=['verify_stage35_ex_v34_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v34_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35.py'),run_name='__main__')
    finally:
        sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V35_IMMUTABLE_V34_HISTORY_REPLAY_{target}')
