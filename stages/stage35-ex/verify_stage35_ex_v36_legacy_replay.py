#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited Goal4-ready V35 snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V36 = 'STAGE35_EX_PESCH_E1_STATE_V36_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_PENDING_AUDIT'
V35 = 'STAGE35_EX_PESCH_E1_STATE_V35_POST_35EX35_HOSTILE_AUDITED_GOAL4_READY'
SNAPSHOT = '5a79ace1a48bcff04e48b021afee75af3a40b8c1'
LIVE_BASE = '29ba60e69549a89eba7fab936516d17fa517dd2c'
OLD_ALLOWED = {'base', *{str(i) for i in range(10, 33)}, '32p', '33g1', '33g2', '33', '34', '35'}

if len(sys.argv) != 2 or sys.argv[1] not in OLD_ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v36_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35}')
target = sys.argv[1]

real = json.loads(STATE.read_text())
assert real['schema'] == V36 and real['stage'] == '35-EX' and real['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha'] == LIVE_BASE
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V35
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit'] == '35EX-35_GOALS_1_TO_3_AUTHORITY_PROMOTION'
assert real['parent_authority']['hostile_reaudit_review_id'] == 5121283524
assert real['parent_authority']['exact_head_sha'] == 'ea7dffd56ed85e9d8511e04e6aa5b13acfc9f6d3'
assert real['parent_authority']['merge_sha'] == SNAPSHOT
assert real['current']['unit'] == '35EX-35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_TEST'
assert real['claims']['goal4a_two_adic_test_completed'] is True
assert real['claims']['goal4_full_test_completed'] is False
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text = subprocess.check_output(
    ['git', 'show', f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT, text=True, stderr=subprocess.STDOUT,
)
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V35
assert snapshot['current']['unit'] == '35EX-35_GOAL4_FOURTH_SQUARE_RESTRICTION_TEST'
assert snapshot['current']['status'] == 'READY_AFTER_HOSTILE_AUDITED_GOALS_1_TO_3_NO_E1_CREDIT'
assert snapshot['claims']['goal4_fourth_square_restriction_test_completed'] is False

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
        sys.argv = ['verify_stage35_ex_v35_legacy_replay.py', target]
        runpy.run_path(str(ROOT / 'stages/stage35-ex/verify_stage35_ex_v35_legacy_replay.py'), run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text

print(f'PASS V36_IMMUTABLE_V35_HISTORY_REPLAY_{target}')
