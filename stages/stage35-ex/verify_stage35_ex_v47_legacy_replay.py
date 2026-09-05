#!/usr/bin/env python3
"""Replay persisted in-PR V46 Goal4I snapshot while V47 Goal4J is stacked provisionally."""
from __future__ import annotations
import json, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAPFILE = ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V46-9675711189fa.json'
V47 = 'STAGE35_EX_PESCH_E1_STATE_V47_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_PREFLIGHT_PENDING_LATER_AUDIT'
V46 = 'STAGE35_EX_PESCH_E1_STATE_V46_GOAL4I_V2_SELF_MAP_PREFLIGHT_PENDING_LATER_AUDIT'
SOURCE_HEAD = '9675711189fa91e0d7f0ef6d8404845015a6688b'
OLD_ALLOWED = {'base', *{str(i) for i in range(10,33)}, '32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h'}
ALLOWED = OLD_ALLOWED | {'35g4i'}
if len(sys.argv) != 2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v47_legacy_replay.py {base|10|...|35g4i}')
target = sys.argv[1]
real = json.loads(STATE.read_text())
assert real['schema'] == V47
assert real['history_snapshot']['commit_sha'] == SOURCE_HEAD
assert real['history_snapshot']['schema'] == V46
assert real['history_snapshot']['path'] == 'stages/stage35-ex/snapshots/MAIN-STATE-V46-9675711189fa.json'
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr'] == 1633
assert real['current']['unit'] == '35EX-35_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_COUPLING_PREFLIGHT'
assert real['claims']['goal4j_executed'] is True
assert real['claims']['cross_twist_selmer_pruning_obtained'] is False
assert real['claims']['E1_proved'] is False

snapshot_text = SNAPFILE.read_text()
snapshot = json.loads(snapshot_text)
assert snapshot['schema'] == V46
assert snapshot['current']['unit'] == '35EX-35_GOAL4I_GENUINE_V2_INFINITE_DESCENT_SELF_MAP_PREFLIGHT'
assert snapshot['claims']['goal4i_executed'] is True
assert snapshot['claims']['minimum_v2_scalar_descent_route_closed'] is True
assert snapshot['claims']['E1_proved'] is False

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
            sys.argv = ['verify_stage35_ex_v46_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v46_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv = ['verify_stage35_ex_35_goal4i.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4i.py'),run_name='__main__')
    finally:
        sys.argv = old_argv
finally:
    Path.read_text = original_read_text
print(f'PASS V47_PERSISTED_IN_PR_V46_REPLAY_{target}')
