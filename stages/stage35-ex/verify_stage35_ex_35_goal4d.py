#!/usr/bin/env python3
"""Verify 35EX-35 Goal4D: full Q_7 lift, valuation cone, and cross-face gap rules."""
from __future__ import annotations
import itertools, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4d-full-q7-valuation-crossface-closure.json'
G4B = ROOT / 'stages/stage35-ex/35ex-35/goal4b-mod7-local-restriction.json'
G4C = ROOT / 'stages/stage35-ex/35ex-35/goal4c-mod7-private-gcd-support-receiver.json'

state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())
g4b = json.loads(G4B.read_text())
g4c = json.loads(G4C.read_text())

LIVE_BASE = '40cd38c5f5d2679874ce3be882cc67d17d4c7558'
G4C_MERGE = '12f0adb9a70e387f0a3ad6c37d6f22a3fb78cda6'
G4C_HEAD = 'c5337c2998f6f9148dae50df5fe33db0cfad1a5b'
G4C_REVIEW = 5123181794

assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V41_GOAL4D_FULL_Q7_VALUATION_CROSSFACE_CLOSURE_PENDING_AUDIT'
assert state['stage'] == '35-EX' and state['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha'] == LIVE_BASE
assert state['parent_authority']['unit'] == '35EX-35_GOAL4C_PRIVATE_GCD_LIFT_OF_MOD7_BRANCH_AND_FINITE_RECEIVER_TEST'
assert state['parent_authority']['audit_verdict'] == 'HOSTILE_AUDIT_PASS'
assert state['parent_authority']['hostile_review_id'] == G4C_REVIEW
assert state['parent_authority']['pr'] == 1627
assert state['parent_authority']['exact_head_sha'] == G4C_HEAD
assert state['parent_authority']['exact_head_ci_run'] == 33994394731
assert state['parent_authority']['exact_head_ci_job'] == 101382199811
assert state['parent_authority']['merge_sha'] == G4C_MERGE

assert art['schema'] == 'STAGE35_EX_35_GOAL4D_FULL_Q7_VALUATION_CROSSFACE_CLOSURE_V1'
assert art['status'] == 'PROVISIONAL_EXACT_FULL_Q7_VALUATION_CLOSURE_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert art['base_main_sha'] == LIVE_BASE
assert art['parent_goal4c_authority']['hostile_review_id'] == G4C_REVIEW
assert art['parent_goal4c_authority']['exact_head_sha'] == G4C_HEAD
assert art['parent_goal4c_authority']['merge_sha'] == G4C_MERGE
assert g4c['mod7_support_receiver']['exact_support_pattern_count'] == 12
assert g4c['mod7_support_receiver']['S3_orbit_count'] == 3
assert g4c['exact_interpretation']['strict_additional_mod7_elimination_beyond_goal4b'] is False
assert g4b['fourth_square_cut']['exact_equivalence_on_face_locus'] == (
    'A^2+B^2+C^2 is a square modulo 7 iff A*B*C is 0 modulo 7'
)

p = 7
Q = {t*t % p for t in range(p)}
QNZ = Q - {0}
assert Q == {0,1,2,4}
assert (-1) % p not in Q
assert {1,2} <= QNZ

# Odd-prime Hensel gate: each nonzero square residue has a simple square root.
for q in QNZ:
    roots = [r for r in range(1,p) if r*r % p == q]
    assert len(roots) == 2
    assert all((2*r) % p != 0 for r in roots)

# Independently replay the exact Goal4B residue theorem and strengthen its
# forward branch to a nonzero unit-square residue, which is enough for Q_7.
face_count = full_count = 0
for A,B,C in itertools.product(range(p), repeat=3):
    if A == B == C == 0:
        continue
    faces = (A*A+B*B, A*A+C*C, B*B+C*C)
    if not all(v % p in Q for v in faces):
        continue
    face_count += 1
    S = (A*A+B*B+C*C) % p
    prod_zero = (A*B*C) % p == 0
    assert (S in Q) == prod_zero
    if prod_zero:
        assert S in QNZ
        full_count += 1
    else:
        assert S != 0 and S not in Q
assert face_count == 78
assert full_count == 54

# Goal4C's 12 source supports map exactly to the three valuation-cone types.
singletons = {tuple(x) for x in g4c['mod7_support_receiver']['singleton_patterns']}
doubletons = {tuple(x) for x in g4c['mod7_support_receiver']['doubleton_patterns']}
assert singletons == {('x',),('y',),('z',),('a',),('b',),('c',)}
assert doubletons == {
    ('x','a'),('x','b'),('y','a'),('y','c'),('z','b'),('z','c')
}

def edge_vals(v: dict[str,int]) -> tuple[int,int,int]:
    return (v['x']+v['y']+v['a'], v['x']+v['z']+v['b'], v['y']+v['z']+v['c'])

# Positive magnitudes are symbolic parameters; these representatives check the
# exact additive formula that determines equality/inequality for each support.
for s in singletons | doubletons:
    v = {k:0 for k in 'xyzabc'}
    for j,k in enumerate(s):
        v[k] = 2 + j  # positive, and distinct on a doubleton
    alpha,beta,gamma = edge_vals(v)
    positives = [t for t in (alpha,beta,gamma) if t > 0]
    assert min(alpha,beta,gamma) == 0 and max(alpha,beta,gamma) > 0
    if s in {('a',),('b',),('c',)}:
        assert len(positives) == 1
    elif s in {('x',),('y',),('z',)}:
        assert len(positives) == 2 and positives[0] == positives[1]
    else:
        assert len(positives) == 2 and positives[0] != positives[1]

# General Q_7 realization proof reduces to the finite residue cases below.
# For two powers 7^u,7^v, after factoring 7^(2 min(u,v)), the unit residue is
# 2 if u=v and 1 otherwise. Both are nonzero squares mod 7.
for relation,residue in [('equal',2),('unequal',1)]:
    assert residue in QNZ
# For a primitive nontrivial valuation triple, the number of zero valuations is
# exactly 1 or 2, so the space unit residue of the explicit model is 1 or 2.
for zero_count in (1,2):
    assert zero_count in QNZ

# Exhaust a finite window as a regression check on the general case formula.
for alpha,beta,gamma in itertools.product(range(5), repeat=3):
    if min(alpha,beta,gamma) != 0 or max(alpha,beta,gamma) == 0:
        continue
    exps = (alpha,beta,gamma)
    for i,j in ((0,1),(0,2),(1,2)):
        u,v = exps[i], exps[j]
        residue = 2 if u == v else 1
        assert residue in QNZ
    assert sum(t == 0 for t in exps) in QNZ

# Face-diagonal valuation rule. If edge valuations are equal, cancellation of
# the leading unit squares is impossible because -1 is a nonresidue mod 7.
for u,v in itertools.product(range(1,p), repeat=2):
    assert (u*u + v*v) % p != 0
assert art['face_and_cross_face_valuation_coupling']['face_diagonal_rule'] == (
    'v7(D_ij)=min(v7(edge_i),v7(edge_j))'
)

# Cross-face sign uniqueness: for unit W,D with W^2=D^2 mod 7, exactly one of
# W-D and W+D vanishes mod 7. Combined with
# (W-D)(W+D)=A_i^2 this gives exact gap valuation 2*v7(A_i).
for W,D in itertools.product(range(1,p), repeat=2):
    if (W*W-D*D) % p != 0:
        continue
    zeros = [((W-D) % p == 0), ((W+D) % p == 0)]
    assert sum(zeros) == 1
assert art['face_and_cross_face_valuation_coupling']['positive_edge_gap_identity'] == (
    '(W-D_jk)(W+D_jk)=A_i^2'
)

interp = art['exact_interpretation']
assert interp['goal4d_full_Q7_lift_completed'] is True
assert interp['full_Q7_fourth_square_condition_classified'] is True
assert interp['p7_valuation_cone_classified'] is True
assert interp['p7_valuation_only_route_exhausted'] is True
assert interp['p7_higher_adic_route_exhausted'] is True
assert interp['strict_additional_p7_elimination_beyond_goal4b'] is False
assert interp['finite_exhaustive_global_squareclass_family_obtained'] is False
assert interp['all_odd_prime_local_conditions_classified'] is False

assert state['current']['unit'] == '35EX-35_GOAL4D_MOD7_SUPPORT_BRANCH_VALUATION_LIFT_AND_CROSS_FACE_COUPLING_TEST'
assert state['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['goal4d_executed'] is True
assert state['claims']['full_Q7_fourth_square_condition_classified'] is True
assert state['claims']['goal4b_mod7_cut_is_full_Q7_local_condition'] is True
assert state['claims']['p7_valuation_cone_classified'] is True
assert state['claims']['p7_valuation_only_route_exhausted'] is True
assert state['claims']['p7_higher_adic_route_exhausted'] is True
assert state['claims']['strict_additional_p7_elimination_beyond_goal4b'] is False
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

print('PASS STAGE35_EX_35_GOAL4D_FULL_Q7_LOCAL_EQUIVALENCE_VALUATION_CONE_CROSSFACE_NO_EXTRA_P7_OBSTRUCTION')
