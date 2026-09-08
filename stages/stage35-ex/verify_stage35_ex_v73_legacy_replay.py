#!/usr/bin/env python3
"""Replay persisted V72 authority while V73 Goal4AJ audited claim-sync is live."""
from __future__ import annotations
import hashlib,json,runpy,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V72-e98b06455d34.json'
V73='STAGE35_EX_PESCH_E1_STATE_V73_GOAL4AJ_LITERAL_DEGREE31_SECTIONS_AUDITED_EXPLICIT_F_B_PENDING'
V72='STAGE35_EX_PESCH_E1_STATE_V72_GOAL4AI_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_PROVED_LITERAL_SECTION_COEFFICIENTS_PENDING_AUDIT'
V72_BLOB='0f1bad646ad2b9667431e18519bc5379b70a8631'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z','35g4aa','35g4ab','35g4ac','35g4ad','35g4ae','35g4af','35g4ag','35g4ah','35g4ai'}
if len(sys.argv)!=2 or sys.argv[1] not in OLD: raise SystemExit('usage: verify_stage35_ex_v73_legacy_replay.py target')
target=sys.argv[1]

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

real=json.loads(STATE.read_text())
assert real['schema']==V73
assert real['history_snapshot']['schema']==V72
assert real['history_snapshot']['path']=='stages/stage35-ex/snapshots/MAIN-STATE-V72-e98b06455d34.json'
assert real['history_snapshot']['snapshot_blob_sha1']==V72_BLOB
assert real['history_snapshot']['hostile_audited'] is True
assert real['history_snapshot']['hostile_review_id']==5134464420
assert real['last_audited_authority']['hostile_review_id']==5140644783
assert real['claims']['goal4aj_executed'] is True
assert real['claims']['open_receiver_second_class_degree31_literal_sections_materialized'] is True
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert real['claims']['E1_proved'] is False

assert blob(SNAP)==V72_BLOB
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V72
assert snap['current']['unit']=='35EX-35_GOAL4AI_SECOND_CLASS_QI_CYCLIC_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_AND_LITERAL_SECTION_MATERIALIZATION_PREFLIGHT'
assert snap['claims']['goal4ai_executed'] is True
assert snap['claims']['open_receiver_second_class_degree31_literal_sections_materialized'] is False

orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target=='35g4ai':
            sys.argv=['verify_stage35_ex_35_goal4ai.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4ai.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_v72_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v72_legacy_replay.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V73_PERSISTED_V72_REPLAY_{target}')
