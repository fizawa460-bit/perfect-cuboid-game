#!/usr/bin/env python3
"""Verify Goal4F: forced-prime valuation-parity lift and global squareclass gate failure."""
from __future__ import annotations
import itertools, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4f-forced-prime-squareclass-parity-lift.json'
state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())

BASE = 'cf5389b857ee52225ed44543ff7ac8d05387583a'
PARENT_MERGE = '6fa39f76be24b55153f118812b1bd7f41c43e399'
HEAD4E = 'fcedffa7f2d768ee8b1bc78b04611e1f0a401e77'
REVIEW4E = 5123284301
assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V43_GOAL4F_FORCED_PRIME_SQUARECLASS_PARITY_LIFT_PENDING_AUDIT'
assert state['base_main_sha'] == BASE
assert state['parent_authority']['pr'] == 1633
assert state['parent_authority']['hostile_review_id'] == REVIEW4E
assert state['parent_authority']['exact_head_sha'] == HEAD4E
assert state['parent_authority']['exact_head_ci_run'] == 33996269618
assert state['parent_authority']['exact_head_ci_job'] == 101387257990
assert state['parent_authority']['merge_sha'] == PARENT_MERGE
assert art['base_main_sha'] == BASE
assert art['parent_goal4e_authority']['hostile_review_id'] == REVIEW4E
assert art['parent_goal4e_authority']['exact_head_sha'] == HEAD4E
assert art['parent_goal4e_authority']['merge_sha'] == PARENT_MERGE

def qr(p: int, a: int) -> bool:
    a %= p
    return a != 0 and pow(a, (p-1)//2, p) == 1

assert qr(5,9) and qr(5,16) and qr(5,1)
assert qr(7,1) and qr(7,2)
for p in (11,19): assert qr(p,1) and qr(p,4) and qr(p,5)
for p in (3,5,7,11,19): assert qr(p,1)
parity_pair_reps = {('E','E'):(2,4),('E','O'):(2,1),('O','E'):(1,2),('O','O'):(1,3)}
for par,(m,n) in parity_pair_reps.items():
    assert m>=1 and n>=1 and m!=n
    assert ('E' if m%2==0 else 'O')==par[0]
    assert ('E' if n%2==0 else 'O')==par[1]
assert {2%2,3%2}=={0,1} and {1%2,2%2}=={0,1}

states3=[v for v in itertools.product((0,1,2),repeat=3) if sum(x!=0 for x in v)==2]
states_other=[v for v in itertools.product((0,1,2),repeat=3) if sum(x!=0 for x in v) in (1,2)]
assert len(states3)==12 and len(states_other)==18
perms=list(itertools.permutations(range(3)))
def act(v,p): return tuple(v[p[i]] for i in range(3))
fix3=[sum(act(v,p)==v for v in states3) for p in perms]
fixo=[sum(act(v,p)==v for v in states_other) for p in perms]
identity=len(states3)*len(states_other)**4
joint_fix=[fix3[i]*fixo[i]**4 for i in range(6)]
assert identity==1259712
assert sorted(joint_fix)==[0,0,512,512,512,1259712]
assert sum(joint_fix)//6==210208
recv=art['joint_forced_prime_parity_receiver']
assert recv['labeled_states']==1259712 and recv['S3_orbits']==210208

for q in (7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97):
    assert q not in (2,3,5)
    assert qr(q,9) and qr(q,16) and qr(q,25)
assert art['arbitrary_nonforced_prime_injection']['global_existence_not_claimed'] is True
boundary=art['exact_boundary']
assert boundary['forced_prime_valuation_parity_classified'] is True
assert boundary['forced_prime_parity_pruning_obtained'] is False
assert boundary['finite_forced_prime_parity_receiver_obtained'] is True
assert boundary['finite_forced_prime_parity_S3_orbits']==210208
assert boundary['arbitrary_nonforced_prime_local_odd_valuation_injection_obtained'] is True
assert boundary['finite_exhaustive_global_squareclass_family_obtained'] is False
assert state['current']['unit']=='35EX-35_GOAL4F_FORCED_PRIME_SUPPORT_656_ORBITS_SQUARECLASS_PARITY_LIFT_TEST'
assert state['claims']['goal4f_executed'] is True
assert state['claims']['forced_prime_parity_S3_orbits']==210208
assert state['claims']['forced_prime_parity_pruning_obtained'] is False
assert state['claims']['arbitrary_nonforced_prime_local_odd_valuation_injection_obtained'] is True
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4F_PARITY_1259712_TO_210208_NO_FORCED_PRIME_PARITY_PRUNING_ARBITRARY_Q_INJECTION')
