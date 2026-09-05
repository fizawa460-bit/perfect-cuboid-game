#!/usr/bin/env python3
"""Verify 35EX-35 Goal4C: exact finite mod-7 six-variable support receiver."""
from __future__ import annotations
import itertools, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4c-mod7-private-gcd-support-receiver.json'
DECOMP = ROOT / 'stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json'
G4B = ROOT / 'stages/stage35-ex/35ex-35/goal4b-mod7-local-restriction.json'

state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())
decomp = json.loads(DECOMP.read_text())
g4b = json.loads(G4B.read_text())

LIVE_BASE = '0bc325f9b9db817193bc271121d19cb04970c5b9'
GOAL4B_MERGE = 'cc27e6d6146e93e1928b467cda3464845350b7c1'
HEAD4B = '2fabc151417a021a6f164c62264c86be34ed7082'
assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V40_GOAL4C_MOD7_PRIVATE_GCD_SUPPORT_RECEIVER_PENDING_AUDIT'
assert state['stage'] == '35-EX' and state['status'] == 'ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha'] == LIVE_BASE
assert state['history_snapshot']['commit_sha'] == GOAL4B_MERGE
assert state['parent_authority']['pr'] == 1622
assert state['parent_authority']['hostile_review_id'] == 5123108516
assert state['parent_authority']['prior_fail_freshness_review_id'] == 5121493238
assert state['parent_authority']['exact_head_sha'] == HEAD4B
assert state['parent_authority']['exact_head_ci_run'] == 33971211075
assert state['parent_authority']['exact_head_ci_job'] == 101319941910
assert state['parent_authority']['merge_sha'] == GOAL4B_MERGE

assert art['schema'] == 'STAGE35_EX_35_GOAL4C_MOD7_PRIVATE_GCD_SUPPORT_RECEIVER_V1'
assert art['status'] == 'PROVISIONAL_EXACT_MOD7_FINITE_SUPPORT_RECEIVER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert art['base_main_sha'] == LIVE_BASE
assert art['parent_goal4b_authority']['hostile_review_id'] == 5123108516
assert art['parent_goal4b_authority']['exact_head_sha'] == HEAD4B
assert art['parent_goal4b_authority']['merge_sha'] == GOAL4B_MERGE

assert decomp['definitions'] == {
    'x': 'gcd(A,B)', 'y': 'gcd(A,C)', 'z': 'gcd(B,C)',
    'a': 'A/(x*y)', 'b': 'B/(x*z)', 'c': 'C/(y*z)'
}
assert decomp['goal1_exact_decomposition']['reconstruction'] == ['A=x*y*a','B=x*z*b','C=y*z*c']
assert set(decomp['goal1_exact_decomposition']['pairwise_gcds']) == {
    'gcd(x,y)=1','gcd(x,z)=1','gcd(y,z)=1'
}
assert set(decomp['goal2_primitive_parity_coprimality_dictionary']['derived_coprimalities']) == {
    'gcd(a,b)=gcd(a,c)=gcd(b,c)=1', 'gcd(a,z)=1', 'gcd(b,y)=1', 'gcd(c,x)=1'
}
assert set(decomp['goal2_primitive_parity_coprimality_dictionary']['not_claimed_coprimalities']) == {
    'gcd(a,x)=1','gcd(a,y)=1','gcd(b,x)=1','gcd(b,z)=1','gcd(c,y)=1','gcd(c,z)=1'
}
assert g4b['fourth_square_cut']['exact_equivalence_on_face_locus'] == (
    'A^2+B^2+C^2 is a square modulo 7 iff A*B*C is 0 modulo 7'
)

p = 7
Q = {t*t % p for t in range(p)}
VARS = ('x','y','z','a','b','c')
FORBIDDEN = {
    frozenset(q) for q in (
        ('x','y'),('x','z'),('y','z'),
        ('a','b'),('a','c'),('b','c'),
        ('a','z'),('b','y'),('c','x'),
    )
}
assert {frozenset(q) for q in art['mod7_support_receiver']['forbidden_pairs_from_exact_coprimality']} == FORBIDDEN

def edges(d: dict[str,int]) -> tuple[int,int,int]:
    return (
        d['x']*d['y']*d['a'] % p,
        d['x']*d['z']*d['b'] % p,
        d['y']*d['z']*d['c'] % p,
    )

def square_system(A: int, B: int, C: int) -> bool:
    return all(v % p in Q for v in (
        A*A+B*B, A*A+C*C, B*B+C*C, A*A+B*B+C*C,
    ))

def support(d: dict[str,int]) -> tuple[str,...]:
    return tuple(v for v in VARS if d[v] == 0)

def respects_exact_zero_coprimality(d: dict[str,int]) -> bool:
    return all(not (d[u] == 0 and d[v] == 0) for u,v in (tuple(q) for q in FORBIDDEN))

counts: Counter[tuple[str,...]] = Counter()
edge_zero_counts: Counter[tuple[str,...]] = Counter()
for values in itertools.product(range(p), repeat=6):
    d = dict(zip(VARS, values))
    if not respects_exact_zero_coprimality(d):
        continue
    A,B,C = edges(d)
    if A == B == C == 0 or not square_system(A,B,C):
        continue
    counts[support(d)] += 1
    edge_zero_counts[tuple(e for e,t in zip(('A','B','C'),(A,B,C)) if t == 0)] += 1

EXPECTED = {
    ('x',): 7776, ('y',): 7776, ('z',): 7776,
    ('a',): 2592, ('b',): 2592, ('c',): 2592,
    ('x','a'): 1296, ('x','b'): 1296,
    ('y','a'): 1296, ('y','c'): 1296,
    ('z','b'): 1296, ('z','c'): 1296,
}
assert counts == Counter(EXPECTED)
assert sum(counts.values()) == 38880
assert edge_zero_counts == Counter({
    ('A','B'): 10368, ('A','C'): 10368, ('B','C'): 10368,
    ('A',): 2592, ('B',): 2592, ('C',): 2592,
})

receiver = art['mod7_support_receiver']
assert receiver['max_support_size'] == 2
assert receiver['exact_support_pattern_count'] == 12
assert {tuple(x) for x in receiver['singleton_patterns']} == {k for k in EXPECTED if len(k) == 1}
assert {tuple(x) for x in receiver['doubleton_patterns']} == {k for k in EXPECTED if len(k) == 2}
assert receiver['S3_orbit_count'] == 3
assert {(o['name'], tuple(o['representative']), o['orbit_size']) for o in receiver['S3_orbit_types']} == {
    ('PRIVATE_GCD_SINGLETON', ('x',), 3),
    ('COFACTOR_SINGLETON', ('a',), 3),
    ('INCIDENT_PRIVATE_GCD_COFACTOR_DOUBLETON', ('x','a'), 6),
}
byedge = {k:{tuple(v) for v in vals} for k,vals in receiver['by_edge_zero_pattern'].items()}
assert byedge == {
    'A_only': {('a',)}, 'B_only': {('b',)}, 'C_only': {('c',)},
    'A_B': {('x',),('x','a'),('x','b')},
    'A_C': {('y',),('y','a'),('y','c')},
    'B_C': {('z',),('z','b'),('z','c')},
}

# Single-edge branch representative: support {a} forces only A=0, and
# B^2=C^2 gives xb=+/-yc after cancelling the unit z.
for values in itertools.product(range(p), repeat=6):
    d = dict(zip(VARS, values))
    if not respects_exact_zero_coprimality(d):
        continue
    A,B,C = edges(d)
    if A == B == C == 0 or not square_system(A,B,C):
        continue
    if support(d) == ('a',):
        xb = d['x']*d['b'] % p
        yc = d['y']*d['c'] % p
        assert A == 0 and B != 0 and C != 0
        assert (xb-yc) % p == 0 or (xb+yc) % p == 0

interp = art['exact_interpretation']
assert set(counts) == set(EXPECTED)
assert interp['finite_mod7_source_support_receiver_obtained'] is True
assert interp['strict_additional_mod7_elimination_beyond_goal4b'] is False
assert interp['finite_exhaustive_global_squareclass_family_obtained'] is False

assert state['current']['unit'] == '35EX-35_GOAL4C_PRIVATE_GCD_LIFT_OF_MOD7_BRANCH_AND_FINITE_RECEIVER_TEST'
assert state['current']['status'] == 'PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['goal4c_executed'] is True
assert state['claims']['private_gcd_mod7_lift_completed'] is True
assert state['claims']['finite_mod7_source_support_receiver_obtained'] is True
assert state['claims']['strict_additional_mod7_elimination_beyond_goal4b'] is False
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['goal4_full_test_completed'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

print('PASS STAGE35_EX_35_GOAL4C_EXACT_MOD7_PRIVATE_GCD_SUPPORT_RECEIVER_12_PATTERNS_3_S3_ORBITS')
