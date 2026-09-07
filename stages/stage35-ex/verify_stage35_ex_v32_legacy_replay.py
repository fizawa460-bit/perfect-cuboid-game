#!/usr/bin/env python3
"""Replay Stage35-EX history through merged 35EX-32 against the immutable V31 snapshot.

The original 35EX-32 breadth audit exact-locked the then-current Arsenal index.
That registry is intentionally mutable.  Historical replay therefore supplies
an immutable byte-for-byte snapshot of the exact locked index only while the
35EX-32 verifier runs; the live Arsenal registry is not rewritten or treated as
historical mathematical identity.
"""
from __future__ import annotations
import hashlib, json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
ARSENAL=ROOT/'docs/arsenal/index.json'
ARSENAL_SNAPSHOT=ROOT/'stages/stage35-ex/snapshots/arsenal-index-35ex32-aa45d19c.json'
ARSENAL_BLOB='aa45d19c2f1d8970c7f142bf744c5c17e75abe5a'
V32='STAGE35_EX_PESCH_E1_STATE_V32_POST_35EX32_USER_APPROVED_MERGE_ROUTE_SELECTION'
V31='STAGE35_EX_PESCH_E1_STATE_V31_POST_35EX32_ENDPOINT_POPULATION_BREADTH_AUDIT'
SNAPSHOT='3fbcecfb17c8eadde6479ee4c6f55c80be32cf42'
ALLOWED={'base', *{str(i) for i in range(10,33)}}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v32_legacy_replay.py {base|10|...|32}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V32 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['history_snapshot']['commit_sha']==SNAPSHOT
assert real['history_snapshot']['schema']==V31
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-32'
assert real['parent_authority']['hostile_audit_pass'] is False
assert real['parent_authority']['route_selection_authorized_by_user_merge'] is True
assert real['current']['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

try:
    snapshot_text=subprocess.check_output(
        ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
        cwd=ROOT,text=True,stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit('immutable V31 snapshot unavailable in checkout\n'+exc.output) from exc
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V31
assert snapshot['current']['unit']=='35EX-32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'

original_read_text=Path.read_text
original_read_bytes=Path.read_bytes
state_resolved=STATE.resolve()
arsenal_resolved=ARSENAL.resolve()
arsenal_snapshot_bytes=original_read_bytes(ARSENAL_SNAPSHOT)
assert hashlib.sha1(b'blob '+str(len(arsenal_snapshot_bytes)).encode()+b'\0'+arsenal_snapshot_bytes).hexdigest()==ARSENAL_BLOB
arsenal_snapshot=json.loads(arsenal_snapshot_bytes)
assert arsenal_snapshot['registry_contract']['canonical_machine_registry'] is True
assert arsenal_snapshot['active_stage_snapshot_policy']['live_head_must_be_refetched_at_card_use'] is True
assert {x['id'] for x in arsenal_snapshot['formal_router_weapons']}.issuperset({'S34-W01','S34-W02','S34-W03','S31-W01'})

def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)

def snapshot_read_bytes(self:Path,*args,**kwargs):
    if target=='32' and self.resolve()==arsenal_resolved:
        return arsenal_snapshot_bytes
    return original_read_bytes(self,*args,**kwargs)

Path.read_text=snapshot_read_text
Path.read_bytes=snapshot_read_bytes
try:
    if target=='32':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_32.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v31_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v31_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
    Path.read_bytes=original_read_bytes
print(f'PASS V32_IMMUTABLE_V31_HISTORY_REPLAY_35EX_{target}')
