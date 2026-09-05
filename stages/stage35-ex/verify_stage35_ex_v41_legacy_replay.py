#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged Goal4C while V41 Goal4D is provisional."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V41 = 'STAGE35_EX_PESCH_E1_STATE_V41_GOAL4D_FULL_Q7_VALUATION_CROSSFACE_CLOSURE_PENDING_AUDIT'
V40 = 'STAGE35_EX_PESCH_E1_STATE_V40_GOAL4C_MOD7_PRIVATE_GCD_SUPPORT_RECEIVER_PENDING_AUDIT'
SNAPSHOT = '12f0adb9a70e387f0a3ad6c37d6f22a3fb78cda6'
LIVE_BASE = 'f91c045796cba859ec1dd172cf7871fcac5f6d8a'
OLD_ALLOWED = {'base', *{str(i) for i in range(10, 33)}, '32p', '33g1', '33g2', '33', '34', '35', '35g4a', '35g4b'}
ALLOWED = OLD_ALLOWED | {'35g4c'}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v41_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35|35g4a|35g4b|35g4c}')
target = sys.argv[1]

real = json.loads(STATE.read_text())
assert real['schema'] == V41 and real['stage'] == '35-EX' and real['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha'] == LIVE_BASE
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V40
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit'] == '35EX-35_GOAL4C_PRIVATE_GCD_LIFT_OF_MOD7_BRANCH_AND_FINITE_RECEIVER_TEST'
assert real['parent_authority']['audit_verdict'] == 'HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id'] == 5123181794
assert real['parent_authority']['pr'] == 1627
assert real['parent_authority']['exact_head_sha'] == 'c5337c2998f6f9148dae50df5fe33db0cfad1a5b'
assert real['parent_authority']['exact_head_ci_run'] == 33994394731
assert real['parent_authority']['exact_head_ci_job'] == 101382199811
assert real['parent_authority']['merge_sha'] == SNAPSHOT
assert real['parent_authority']['exact_support_pattern_count'] == 12
assert real['parent_authority']['S3_orbit_count'] == 3
assert real['current']['unit'] == '35EX-35_GOAL4D_MOD7_SUPPORT_BRANCH_VALUATION_LIFT_AND_CROSS_FACE_COUPLING_TEST'
assert real['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert real['claims']['goal4c_hostile_audit_pass'] is True
assert real['claims']['goal4d_executed'] is True
assert real['claims']['full_Q7_fourth_square_condition_classified'] is True
assert real['claims']['finite_squareclass_receiver_obtained'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text = subprocess.check_output(
    ['git', 'show', f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT, text=True, stderr=subprocess.STDOUT,
)
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V40
assert snapshot['current']['unit'] == '35EX-35_GOAL4C_PRIVATE_GCD_LIFT_OF_MOD7_BRANCH_AND_FINITE_RECEIVER_TEST'
assert snapshot['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert snapshot['claims']['goal4c_executed'] is True
assert snapshot['claims']['private_gcd_mod7_lift_completed'] is True
assert snapshot['claims']['finite_mod7_source_support_receiver_obtained'] is True
assert snapshot['claims']['strict_additional_mod7_elimination_beyond_goal4b'] is False
assert snapshot['claims']['finite_squareclass_receiver_obtained'] is False

original_read_text = Path.read_text
state_resolved = STATE.resolve()
def snapshot_read_text(self: Path, *args, **kwargs):
    if self.resolve() == state_resolved:
        return snapshot_text
    return original_read_text(self, *args, **kwargs)

Path.read_text = snapshot_read_text
try:
    old_argv = sys.argv[:]
    try:
        if target in OLD_ALLOWED:
            sys.argv = ['verify_stage35_ex_v40_legacy_replay.py', target]
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_v40_legacy_replay.py'), run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4c.py']
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_35_goal4c.py'), run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text

print(f'PASS V41_IMMUTABLE_V40_HISTORY_REPLAY_{target}')
