#!/usr/bin/env python3
"""Replay immutable in-PR V43 Goal4F snapshot while V44 Goal4G is stacked provisionally."""
from __future__ import annotations
import json, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
SNAPSHOT_FILE = ROOT / 'stages/stage35-ex/snapshots/MAIN-STATE-V43-1ec7218615a3.json'
V44 = 'STAGE35_EX_PESCH_E1_STATE_V44_GOAL4G_NATURAL_HILBERT_RECIPROCITY_PROFILE_PENDING_LATER_AUDIT'
V43 = 'STAGE35_EX_PESCH_E1_STATE_V43_GOAL4F_FORCED_PRIME_SQUARECLASS_PARITY_LIFT_PENDING_AUDIT'
SNAPSHOT = '1ec7218615a3e45949d5b4dd8c21f59824a45112'
OLD_ALLOWED = {'base', *{str(i) for i in range(10,33)}, '32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e'}
ALLOWED = OLD_ALLOWED | {'35g4f'}

if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v44_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34|35|35g4a|35g4b|35g4c|35g4d|35g4e|35g4f}')
target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real['schema'] == V44
assert real['stage'] == '35-EX' and real['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V43
assert real['history_snapshot']['hostile_audited'] is False
assert real['history_snapshot']['history_dropped'] is False
assert real['last_audited_authority']['pr'] == 1633
assert real['last_audited_authority']['hostile_review_id'] == 5123284301
assert real['current']['unit'] == '35EX-35_GOAL4G_JOINT_LOCAL_HILBERT_RECIPROCITY_PROFILE_TEST'
assert real['claims']['goal4f_hostile_audit_pass'] is False
assert real['claims']['goal4g_executed'] is True
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

# Persisted exact copy of MAIN-STATE.json from source commit SNAPSHOT.
# This avoids shallow-checkout ancestry dependence after freshness rebases while keeping the source commit id explicit.
snapshot_text = SNAPSHOT_FILE.read_text()
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V43
assert snapshot['current']['unit'] == '35EX-35_GOAL4F_FORCED_PRIME_SUPPORT_656_ORBITS_SQUARECLASS_PARITY_LIFT_TEST'
assert snapshot['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert snapshot['claims']['goal4f_executed'] is True
assert snapshot['claims']['forced_prime_parity_S3_orbits'] == 210208
assert snapshot['completed_units_delta']['35EX-35-GOAL4F']['status'].startswith('PROVISIONAL_')
assert snapshot['claims']['finite_squareclass_receiver_obtained'] is False

original_read_text = Path.read_text
state_resolved = STATE.resolve()
def snapshot_read_text(self: Path,*args,**kwargs):
    if self.resolve() == state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text = snapshot_read_text
try:
    old_argv = sys.argv[:]
    try:
        if target in OLD_ALLOWED:
            sys.argv = ['verify_stage35_ex_v43_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v43_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4f.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4f.py'),run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text
print(f'PASS V44_IMMUTABLE_IN_PR_V43_REPLAY_{target}')
