#!/usr/bin/env python3
"""Replay persisted V73 authority while V74 Goal4AK audited claim-sync is live."""
from __future__ import annotations
import hashlib,json,runpy,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V73-84a9906500e2.json'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'
V73='STAGE35_EX_PESCH_E1_STATE_V73_GOAL4AJ_LITERAL_DEGREE31_SECTIONS_AUDITED_EXPLICIT_F_B_PENDING'
V73_BLOB='9dfb9f44b1c84ae774f80ce5021193a5d6cd8807'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z','35g4aa','35g4ab','35g4ac','35g4ad','35g4ae','35g4af','35g4ag','35g4ah','35g4ai'}
ALLOWED=OLD|{'35g4aj','35g4ak'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v74_legacy_replay.py target')
target=sys.argv[1]

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

real=json.loads(STATE.read_text())
assert real['schema']==V74
assert real['history_snapshot']['schema']==V73
assert real['history_snapshot']['path']=='stages/stage35-ex/snapshots/MAIN-STATE-V73-84a9906500e2.json'
assert real['history_snapshot']['snapshot_blob_sha1']==V73_BLOB
assert real['history_snapshot']['hostile_audited'] is True
assert real['history_snapshot']['hostile_review_id']==5142248509
assert real['last_audited_authority']['unit']=='35EX-35_GOAL4AK_SECOND_CLASS_QI_CYCLIC_EXPLICIT_F_B_ASSEMBLY'
assert real['last_audited_authority']['hostile_review_id']==5142248509
assert real['claims']['goal4ak_executed'] is True
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is True
assert real['claims']['open_receiver_second_class_local_evaluation_released'] is True
assert real['claims']['open_receiver_local_evaluations_computed'] is False
assert real['claims']['E1_proved'] is False

assert blob(SNAP)==V73_BLOB
snapbytes=SNAP.read_bytes(); snaptext=snapbytes.decode(); snap=json.loads(snaptext)
assert snap['schema']==V73
assert snap['current']['unit']=='35EX-35_GOAL4AJ_SECOND_CLASS_QI_CYCLIC_DEGREE31_LITERAL_SECTION_COEFFICIENT_EXTRACTION'
assert snap['claims']['goal4aj_executed'] is True
assert snap['claims']['open_receiver_second_class_explicit_F_B_computed'] is False

orig_text=Path.read_text; orig_bytes=Path.read_bytes; sr=STATE.resolve()
def patched_text(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig_text(self,*a,**k)
def patched_bytes(self:Path,*a,**k):
    if self.resolve()==sr:return snapbytes
    return orig_bytes(self,*a,**k)
Path.read_text=patched_text
Path.read_bytes=patched_bytes
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v73_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v73_legacy_replay.py'),run_name='__main__')
        elif target=='35g4aj':
            # The Goal4AJ verifier has an explicit V74 compatibility mode. Let it
            # see the real live V74 state, so any subprocess it launches uses the
            # V74 -> persisted-V73 adapter rather than mistaking V74 for V73.
            Path.read_text=orig_text
            Path.read_bytes=orig_bytes
            try:
                sys.argv=['verify_stage35_ex_35_goal4aj_audited_claim_sync.py']
                runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aj_audited_claim_sync.py'),run_name='__main__')
            finally:
                Path.read_text=patched_text
                Path.read_bytes=patched_bytes
        else:
            sys.argv=['verify_stage35_ex_35_goal4ak_explicit_fb.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4ak_explicit_fb.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally:
    Path.read_text=orig_text
    Path.read_bytes=orig_bytes
print(f'PASS V74_PERSISTED_V73_REPLAY_{target}')
