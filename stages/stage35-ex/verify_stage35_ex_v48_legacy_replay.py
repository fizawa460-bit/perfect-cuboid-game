#!/usr/bin/env python3
"""Replay persisted in-PR V47 Goal4J snapshot while V48 Goal4K is stacked provisionally."""
from __future__ import annotations
import json, runpy, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAPFILE=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V47-bc51012fc327.json'
V48='STAGE35_EX_PESCH_E1_STATE_V48_GOAL4K_RATIO_DISCRIMINANT_GENUS_ONE_QUOTIENT_PENDING_LATER_AUDIT'
V47='STAGE35_EX_PESCH_E1_STATE_V47_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_PREFLIGHT_PENDING_LATER_AUDIT'
SOURCE='bc51012fc3273e893445f01f8ac7098a2dd5c480'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i'}
ALLOWED=OLD|{'35g4j'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v48_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V48
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V47
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4k_executed'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAPFILE.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V47
assert snap['claims']['goal4j_executed'] is True
assert snap['claims']['cross_twist_selmer_pruning_obtained'] is False
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v47_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v47_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4j.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4j.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V48_PERSISTED_IN_PR_V47_REPLAY_{target}')
