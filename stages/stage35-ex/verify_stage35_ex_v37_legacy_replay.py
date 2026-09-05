#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged Goal4A snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V37 = 'STAGE35_EX_PESCH_E1_STATE_V37_POST_GOAL4A_HOSTILE_AUDITED_GOAL4B_READY'
V36 = 'STAGE35_EX_PESCH_E1_STATE_V36_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_PENDING_AUDIT'
SNAPSHOT = '2365d4bce49faf2822be2a3ff7d841af9a14820c'
LIVE_BASE = 'af2bcbe67f8ea71238829877c04a054d49ba2f11'
OLD_ALLOWED = {'base', *{str(i) for i in range(10, 33)}, '32p', '33g1', '33g2', '33', '34', '35'}
ALLOWED = OLD_ALLOWED | {'35g4a'}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v37_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35|35g4a}')
target = sys.argv[1]

real = json.loads(STATE.read_text())
assert real['schema'] == V37 and real['stage'] == '35-EX' and real['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha'] == LIVE_BASE
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V36
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit'] == '35EX-35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_TEST'
assert real['parent_authority']['audit_verdict'] == 'HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id'] == 5121404951
assert real['parent_authority']['pr'] == 1615
assert real['parent_authority']['exact_head_sha'] == 'df72152df049b765d42bb9aecc1d5637e3fb0b68'
assert real['parent_authority']['exact_head_ci_run'] == 33968754649
assert real['parent_authority']['exact_head_ci_job'] == 101313405862
assert real['parent_authority']['merge_sha'] == SNAPSHOT
assert real['current']['unit'] == '35EX-35_GOAL4B_ODD_PRIME_OR_FINITE_SQUARECLASS_RECEIVER_TEST'
assert real['current']['status'] == 'READY_AFTER_HOSTILE_AUDITED_GOAL4A_NO_E1_CREDIT'
assert real['claims']['goal4a_hostile_audit_pass'] is True
assert real['claims']['goal4_full_test_completed'] is False
assert real['claims']['odd_prime_local_conditions_tested'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text = subprocess.check_output(
    ['git', 'show', f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT, text=True, stderr=subprocess.STDOUT,
)
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V36
assert snapshot['current']['unit'] == '35EX-35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_TEST'
assert snapshot['current']['status'] == 'PROVISIONAL_GOAL4A_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert snapshot['claims']['goal4a_two_adic_test_completed'] is True
assert snapshot['claims']['goal4_full_test_completed'] is False

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
            sys.argv = ['verify_stage35_ex_v36_legacy_replay.py', target]
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_v36_legacy_replay.py'), run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4a.py']
            runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_35_goal4a.py'), run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text

print(f'PASS V37_IMMUTABLE_V36_HISTORY_REPLAY_{target}')
