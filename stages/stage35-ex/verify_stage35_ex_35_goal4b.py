#!/usr/bin/env python3
"""Verify 35EX-35 Goal4B: genuine mod-7 fourth-square local restriction."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4b-mod7-local-restriction.json'

state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())

assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V38_GOAL4B_MOD7_LOCAL_RESTRICTION_PENDING_AUDIT'
assert state['stage'] == '35-EX' and state['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha'] == 'd761baa2d2d5e69479ef191041c5e2f017a50283'
assert state['parent_authority']['unit'] == '35EX-35_GOAL4A_AUTHORITY_PROMOTION'
assert state['parent_authority']['hostile_review_id'] == 5121443297
assert state['parent_authority']['pr'] == 1618
assert state['parent_authority']['exact_head_sha'] == '8a84f61e5b0cdc54430ca77e6d2e00e9ef682798'
assert state['parent_authority']['exact_head_ci_run'] == 33969337207
assert state['parent_authority']['exact_head_ci_job'] == 101314947704
assert state['parent_authority']['merge_sha'] == '7ce9edb2652a044fd6140e0f45b87026eefcf319'

assert art['schema'] == 'STAGE35_EX_35_GOAL4B_MOD7_ODD_PRIME_LOCAL_RESTRICTION_V1'
assert art['status'] == 'PROVISIONAL_EXACT_MOD7_LOCAL_RESTRICTION_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert art['base_main_sha'] == state['base_main_sha']
assert art['parent_goal4a_authority']['hostile_review_id'] == 5121443297
assert art['parent_goal4a_authority']['merge_sha'] == state['parent_authority']['merge_sha']

p = 7
Q = {x * x % p for x in range(p)}
Qstar = Q - {0}
assert Q == {0, 1, 2, 4}
assert Qstar == {1, 2, 4}

# Exact nonzero-square pair-sum lemma.
for u in Qstar:
    for v in Qstar:
        assert (((u + v) % p in Q) == (u == v))

# Direct exhaustive residue audit on (A,B,C) modulo 7, excluding the
# projectively invalid all-zero triple.  The three face-square predicates
# are checked before the fourth (space) square predicate.
def face_ok(A: int, B: int, C: int) -> bool:
    return (
        (A*A + B*B) % p in Q
        and (A*A + C*C) % p in Q
        and (B*B + C*C) % p in Q
    )

def full_ok(A: int, B: int, C: int) -> bool:
    return face_ok(A, B, C) and (A*A + B*B + C*C) % p in Q

def projective_normalize(t: tuple[int, int, int]) -> tuple[int, int, int]:
    for x in t:
        if x % p:
            inv = pow(x, -1, p)
            return tuple((inv * y) % p for y in t)
    raise AssertionError('all-zero triple has no projective normalization')

vectors = [
    (A, B, C)
    for A in range(p)
    for B in range(p)
    for C in range(p)
    if (A, B, C) != (0, 0, 0)
]
face = [t for t in vectors if face_ok(*t)]
full = [t for t in vectors if full_ok(*t)]
rejected = [t for t in face if t not in set(full)]

assert len(face) == 78
assert len(full) == 54
assert len(rejected) == 24

faceP = {projective_normalize(t) for t in face}
fullP = {projective_normalize(t) for t in full}
rejectedP = faceP - fullP
assert len(faceP) == 13
assert len(fullP) == 9
assert len(rejectedP) == 4
assert rejectedP == {
    (1, 1, 1),
    (1, 1, 6),
    (1, 6, 1),
    (1, 6, 6),
}

# Face-locus support decomposition: 3 axes, 6 two-coordinate classes,
# and exactly the four all-nonzero classes above.
support_hist: dict[int, int] = {}
for t in faceP:
    support = sum(x != 0 for x in t)
    support_hist[support] = support_hist.get(support, 0) + 1
assert support_hist == {1: 3, 2: 6, 3: 4}

# Strong exact equivalence on the three-face-square residue locus:
# the space residue is square iff at least one edge is 0 modulo 7.
for A, B, C in face:
    assert (full_ok(A, B, C) == ((A * B * C) % p == 0))

# Genuine-new-condition witness: all face squares survive but the space
# square fails.  Thus 7|ABC is not already implied by the face conditions.
assert face_ok(1, 1, 1)
assert not full_ok(1, 1, 1)
assert (1 + 1) % p in Q
assert (1 + 1 + 1) % p not in Q

cut = art['fourth_square_cut']
assert cut['full_projective_classes'] == len(fullP)
assert cut['rejected_projective_classes'] == len(rejectedP)
assert cut['full_nonzero_vector_residues'] == len(full)
assert cut['rejected_nonzero_vector_residues'] == len(rejected)
assert {tuple(x) for x in cut['rejected_projective_representatives']} == rejectedP
assert cut['exact_equivalence_on_face_locus'] == 'A^2+B^2+C^2 is a square modulo 7 iff A*B*C is 0 modulo 7'

assert state['current']['unit'] == '35EX-35_GOAL4B_MOD7_ODD_PRIME_LOCAL_RESTRICTION'
assert state['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['goal4b_mod7_test_completed'] is True
assert state['claims']['odd_prime_local_restriction_p7_obtained'] is True
assert state['claims']['new_fourth_square_restriction_obtained'] is True
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['goal4_full_test_completed'] is False
assert state['claims']['E1_proved'] is False
assert state['claims']['stage35_closed'] is False
assert state['claims']['perfect_cuboid_nonexistence_claim'] is False

fire = art['credit_firewall']
assert fire['receiver_branch_7_not_divide_ABC_locally_closed'] is True
assert fire['finite_squareclass_receiver_obtained'] is False
assert fire['E1_proved'] is False and fire['stage35_closed'] is False

print('PASS STAGE35_EX_35_GOAL4B_MOD7_GENUINE_LOCAL_RESTRICTION')
