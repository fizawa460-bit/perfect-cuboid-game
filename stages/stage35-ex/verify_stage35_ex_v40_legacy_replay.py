#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged Goal4B while V40 Goal4C is provisional."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V40 = 'STAGE35_EX_PESCH_E1_STATE_V40_GOAL4C_MOD7_PRIVATE_GCD_SUPPORT_RECEIVER_PENDING_AUDIT'
V38 = 'STAGE35_EX_PESCH_E1_STATE_V38_GOAL4B_MOD7_LOCAL_RESTRICTION_PENDING_AUDIT'
SNAPSHOT = 'cc27e6d6146e93e1928b467cda3464845350b7c1'
LIVE_BASE = '0bc325f9b9db817193bc271121d19cb04970c5b9'
OLD_ALLOWED = {'base', *{str(i) for i in range(10, 33)}, '32p', '33g1', '33g2', '33', '34', '35', '35g4a'}
ALLOWED = OLD_ALLOWED | {'35g4b'}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v40_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35|35g4a|35g4b}')
target = sys.argv[1]

real = json.loads(STATE.read_text())
assert real['schema'] == V40 and real['stage'] == '35-EX' and real['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha'] == LIVE_BASE
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V38
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit'] == '35EX-35_GOAL4B_MOD7_ODD_PRIME_LOCAL_RESTRICTION'
assert real['parent_authority']['audit_verdict'] == 'HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id'] == 5123108516
assert real['parent_authority']['prior_fail_freshness_review_id'] == 5121493238
assert real['parent_authority']['pr'] == 1622
assert real['parent_authority']['exact_head_sha'] == '2fabc151417a021a6f164c62264c86be34ed7082'
assert real['parent_authority']['exact_head_ci_run'] == 33971211075
assert real['parent_authority']['exact_head_ci_job'] == 101319941910
assert real['parent_authority']['merge_sha'] == SNAPSHOT
assert real['current']['unit'] == '35EX-35_GOAL4C_PRIVATE_GCD_LIFT_OF_MOD7_BRANCH_AND_FINITE_RECEIVER_TEST'
assert real['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert real['claims']['goal4b_hostile_audit_pass'] is True
assert real['claims']['goal4c_executed'] is True
assert real['claims']['private_gcd_mod7_lift_completed'] is True
assert real['claims']['finite_mod7_source_support_receiver_obtained'] is True
assert real['claims']['finite_squareclass_receiver_obtained'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text = subprocess.check_output(
    ['git', 'show', f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT, text=True, stderr=subprocess.STDOUT,
)
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V38
assert snapshot['current']['unit'] == '35EX-35_GOAL4B_MOD7_ODD_PRIME_LOCAL_RESTRICTION'
assert snapshot['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert snapshot['claims']['goal4b_mod7_test_completed'] is True
assert snapshot['claims']['odd_prime_local_restriction_p7_obtained'] is True
assert snapshot['claims']['finite_squareclass_receiver_obtained'] is False
assert snapshot['claims']['private_gcd_mod7_lift_completed'] is False

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
            sys.argv = ['verify_stage35_ex_v38_legacy_replay.py', target]
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_v38_legacy_replay.py'), run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4b.py']
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_35_goal4b.py'), run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text

print(f'PASS V40_IMMUTABLE_V38_HISTORY_REPLAY_{target}')
