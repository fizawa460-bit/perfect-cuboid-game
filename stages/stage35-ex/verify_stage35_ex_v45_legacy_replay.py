#!/usr/bin/env python3
"""Replay immutable in-PR V44 Goal4G snapshot while V45 Goal4H is stacked provisionally."""
from __future__ import annotations
import json, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
SNAPSHOT_FILE = ROOT / 'stages/stage35-ex/snapshots/MAIN-STATE-V44-8c96c43a3e39.json'
V45 = 'STAGE35_EX_PESCH_E1_STATE_V45_GOAL4H_VERTICAL_BRAUER_ADAPTER_PREFLIGHT_PENDING_LATER_AUDIT'
V44 = 'STAGE35_EX_PESCH_E1_STATE_V44_GOAL4G_NATURAL_HILBERT_RECIPROCITY_PROFILE_PENDING_LATER_AUDIT'
SNAPSHOT = '8c96c43a3e39732f2c93cfa871855ccc96ff534e'
OLD_ALLOWED = {'base', *{str(i) for i in range(10,33)}, '32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f'}
ALLOWED = OLD_ALLOWED | {'35g4g'}
if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v45_legacy_replay.py {base|10|...|35g4g}')
target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real['schema'] == V45
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V44
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr'] == 1633
assert real['current']['unit'] == '35EX-35_GOAL4H_NONOBVIOUS_VERTICAL_BRAUER_ENDPOINT_FIBRATION_SOURCE_LOCK_PREFLIGHT'
assert real['claims']['goal4f_hostile_audit_pass'] is False
assert real['claims']['goal4h_executed'] is True
assert real['claims']['E1_proved'] is False

# Exact blob copy of MAIN-STATE.json from source commit SNAPSHOT.  This avoids
# dependence on dangling in-PR commit objects after #1637 was squash-merged.
snapshot_text = SNAPSHOT_FILE.read_text()
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V44
assert snapshot['current']['unit'] == '35EX-35_GOAL4G_JOINT_LOCAL_HILBERT_RECIPROCITY_PROFILE_TEST'
assert snapshot['claims']['goal4g_executed'] is True
assert snapshot['claims']['natural_pairwise_hilbert_route_closed'] is True
assert snapshot['claims']['goal4f_hostile_audit_pass'] is False

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
            sys.argv = ['verify_stage35_ex_v44_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v44_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4g.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4g.py'),run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text
print(f'PASS V45_IMMUTABLE_IN_PR_V44_REPLAY_{target}')
