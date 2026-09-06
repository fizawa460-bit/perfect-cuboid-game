#!/usr/bin/env python3
"""Replay immutable in-PR V45 Goal4H snapshot while V46 Goal4I is stacked provisionally."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
V46 = 'STAGE35_EX_PESCH_E1_STATE_V46_GOAL4I_V2_SELF_MAP_PREFLIGHT_PENDING_LATER_AUDIT'
V45 = 'STAGE35_EX_PESCH_E1_STATE_V45_GOAL4H_VERTICAL_BRAUER_ADAPTER_PREFLIGHT_PENDING_LATER_AUDIT'
SNAPSHOT = 'ec4d078984bf1ce6b5b8707615c1690eaa62e512'
OLD_ALLOWED = {'base', *{str(i) for i in range(10,33)}, '32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g'}
ALLOWED = OLD_ALLOWED | {'35g4h'}
if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v46_legacy_replay.py {base|10|...|35g4h}')
target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real['schema'] == V46
assert real['history_snapshot']['commit_sha'] == SNAPSHOT
assert real['history_snapshot']['schema'] == V45
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr'] == 1633
assert real['current']['unit'] == '35EX-35_GOAL4I_GENUINE_V2_INFINITE_DESCENT_SELF_MAP_PREFLIGHT'
assert real['claims']['goal4i_executed'] is True
assert real['claims']['E1_proved'] is False

snapshot_text = subprocess.check_output(
    ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'], cwd=ROOT, text=True, stderr=subprocess.STDOUT
)
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V45
assert snapshot['current']['unit'] == '35EX-35_GOAL4H_NONOBVIOUS_VERTICAL_BRAUER_ENDPOINT_FIBRATION_SOURCE_LOCK_PREFLIGHT'
assert snapshot['claims']['goal4h_executed'] is True
assert snapshot['claims']['S33_PW07_direct_transfer_applicable'] is False
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
            sys.argv = ['verify_stage35_ex_v45_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v45_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4h.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4h.py'),run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text
print(f'PASS V46_IMMUTABLE_IN_PR_V45_REPLAY_{target}')
