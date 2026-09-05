#!/usr/bin/env python3
"""Replay Stage35-EX history through hostile-audited merged 35EX-34 against immutable V33 snapshot."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V34='STAGE35_EX_PESCH_E1_STATE_V34_POST_35EX34_HOSTILE_AUDITED_PRIVATE_GCD_PREFLIGHT'
V33='STAGE35_EX_PESCH_E1_STATE_V33_POST_35EX33_HOSTILE_AUDITED_ROUTE_BLOCKER'
SNAPSHOT='c8a876838882c91c078c85da5c88d131b151ac40'
AUDIT_COMMIT='e073c322d52122de10791bb8174c62bd696bf037'
OLD_ALLOWED={'base', *{str(i) for i in range(10,33)}, '32p', '33g1', '33g2', '33'}
ALLOWED=OLD_ALLOWED|{'34'}

if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v34_legacy_replay.py {base|10|...|32|32p|33g1|33g2|33|34}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V34 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['history_snapshot']['commit_sha']==SNAPSHOT
assert real['history_snapshot']['schema']==V33
assert real['history_snapshot']['history_dropped'] is False
assert real['parent_authority']['unit']=='35EX-34'
assert real['parent_authority']['audit_verdict']=='HOSTILE_AUDIT_PASS'
assert real['parent_authority']['hostile_review_id']==5120821124
assert real['parent_authority']['route_status']=='PASS_NEW_GATE_FROM_STRONGER_VIEW'
assert real['current']['unit']=='35EX-35_PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_PREFLIGHT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

snapshot_text=subprocess.check_output(
    ['git','show',f'{SNAPSHOT}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT,text=True,stderr=subprocess.STDOUT,
)
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V33
assert snapshot['current']['unit']=='35EX-34_POST_GAUSSIAN_BLOCK_FRESH_BREADTH_AUDIT'
assert snapshot['current']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'

# #1600 was squash-merged, so its blind/comparison commits are not ancestors of
# the merge commit. The audited 35EX-34 verifier still checks their exact
# ancestor order. Fetch only the comparison commit at depth 2; its direct
# parent is the blind-generation commit, restoring the two immutable objects
# without changing any mathematical or authority content.
if target=='34':
    have=subprocess.run(
        ['git','cat-file','-e',f'{AUDIT_COMMIT}^{{commit}}'], cwd=ROOT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode==0
    if not have:
        subprocess.run(
            ['git','fetch','--no-tags','--depth=2','origin',AUDIT_COMMIT],
            cwd=ROOT,check=True,
        )

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def snapshot_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return snapshot_text
    return original_read_text(self,*args,**kwargs)
Path.read_text=snapshot_read_text
try:
    old_argv=sys.argv[:]
    try:
        if target in OLD_ALLOWED:
            sys.argv=['verify_stage35_ex_v33_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v33_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_34.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_34.py'),run_name='__main__')
    finally:
        sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V34_IMMUTABLE_V33_HISTORY_REPLAY_{target}')
