#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged Goal4E while V43 Goal4F is provisional."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V43 = 'STAGE35_EX_PESCH_E1_STATE_V43_GOAL4F_FORCED_PRIME_SQUARECLASS_PARITY_LIFT_PENDING_AUDIT'
V42 = 'STAGE35_EX_PESCH_E1_STATE_V42_GOAL4E_ALL_ODD_PRIME_ZERO_SUPPORT_CLASSIFICATION_PENDING_AUDIT'
SNAPSHOT = '6fa39f76be24b55153f118812b1bd7f41c43e399'
LIVE_BASE = 'cf5389b857ee52225ed44543ff7ac8d05387583a'
OLD_ALLOWED = {'base', *{str(i) for i in range(10,33)}, '32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d'}
ALLOWED = OLD_ALLOWED | {'35g4e'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v43_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35|35g4a|35g4b|35g4c|35g4d|35g4e}')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V43 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==LIVE_BASE
assert real['history_snapshot']['commit_sha']==SNAPSHOT and real['history_snapshot']['schema']==V42 and real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-35_GOAL4E_ODD_PRIME_LOCAL_BREADTH_AND_FINITE_GLOBAL_RECEIVER_TEST'
assert real['parent_authority']['audit_verdict']=='HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id']==5123284301 and real['parent_authority']['pr']==1633
assert real['parent_authority']['exact_head_sha']=='fcedffa7f2d768ee8b1bc78b04611e1f0a401e77'
assert real['parent_authority']['exact_head_ci_run']==33996269618 and real['parent_authority']['exact_head_ci_job']==101387257990
assert real['parent_authority']['merge_sha']==SNAPSHOT
assert real['current']['unit']=='35EX-35_GOAL4F_FORCED_PRIME_SUPPORT_656_ORBITS_SQUARECLASS_PARITY_LIFT_TEST'
assert real['current']['status']=='PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert real['claims']['goal4e_hostile_audit_pass'] is True and real['claims']['goal4f_executed'] is True
assert real['claims']['finite_squareclass_receiver_obtained'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False
snapshot_text=subprocess.check_output(['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],cwd=ROOT,text=True,stderr=subprocess.STDOUT)
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V42
assert snapshot['current']['unit']=='35EX-35_GOAL4E_ODD_PRIME_LOCAL_BREADTH_AND_FINITE_GLOBAL_RECEIVER_TEST'
assert snapshot['claims']['goal4e_executed'] is True
assert snapshot['claims']['forced_odd_prime_set']==[3,5,7,11,19]
assert snapshot['claims']['finite_global_forced_prime_support_S3_orbits']==656
assert snapshot['claims']['finite_squareclass_receiver_obtained'] is False
original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved: return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    old_argv=sys.argv[:]
    try:
        if target in OLD_ALLOWED:
            sys.argv=['verify_stage35_ex_v42_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v42_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4e.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4e.py'),run_name='__main__')
    finally:
        sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V43_IMMUTABLE_V42_HISTORY_REPLAY_{target}')
