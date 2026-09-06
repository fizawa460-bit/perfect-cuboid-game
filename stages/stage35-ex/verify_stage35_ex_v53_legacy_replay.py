#!/usr/bin/env python3
"""Replay persisted in-PR V52 Goal4O snapshot while V53 Goal4P is stacked provisionally."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V52-25cc99b9faca.json'
V53='STAGE35_EX_PESCH_E1_STATE_V53_GOAL4P_BRAUER_FROM_SCRATCH_INTERFACE_LOCALIZED_PENDING_LATER_AUDIT'
V52='STAGE35_EX_PESCH_E1_STATE_V52_GOAL4O_TERNARY_SPINOR_TAUTOLOGY_FAILCLOSE_PENDING_LATER_AUDIT'
SOURCE='25cc99b9facae0abeb6ce08405dd1e3b81523eb5'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n'}
ALLOWED=OLD|{'35g4o'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v53_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V53
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V52
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4p_executed'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V52
assert snap['current']['unit']=='35EX-35_GOAL4O_SPINOR_NORM_TERNARY_FORM_PREFLIGHT'
assert snap['claims']['goal4o_executed'] is True
assert snap['claims']['E1_proved'] is False
orig=Path.read_text;sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v52_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v52_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4o.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4o.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V53_PERSISTED_IN_PR_V52_REPLAY_{target}')
