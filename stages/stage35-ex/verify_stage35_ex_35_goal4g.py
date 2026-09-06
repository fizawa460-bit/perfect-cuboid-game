#!/usr/bin/env python3
"""Verify Goal4G: natural pairwise Hilbert reciprocity gives no finite branch pruning."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4g-joint-local-hilbert-reciprocity-profile.json'
state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())

V44 = 'STAGE35_EX_PESCH_E1_STATE_V44_GOAL4G_NATURAL_HILBERT_RECIPROCITY_PROFILE_PENDING_LATER_AUDIT'
assert state['schema'] == V44
assert art['schema'] == 'STAGE35_EX_35_GOAL4G_JOINT_LOCAL_HILBERT_RECIPROCITY_PROFILE_V1'
assert art['stacked_on_pr'] == 1637
assert art['last_audited_authority']['pr'] == 1633
assert art['last_audited_authority']['hostile_review_id'] == 5123284301
assert art['provisional_parent_goal4f']['snapshot_commit'] == '1ec7218615a3e45949d5b4dd8c21f59824a45112'
assert art['provisional_parent_goal4f']['hostile_audited'] is False

# Equation-generated norm Hilbert symbols have a square second argument, hence are trivial.
norms = art['equation_generated_norm_symbols']
assert norms['status'] == 'IDENTICALLY_TRIVIAL_AT_EVERY_PLACE'
assert norms['branch_pruning_obtained'] is False
assert len(norms['symbols']) == 4

# Legendre symbol for nonzero residues.
def legendre(a: int, p: int) -> int:
    a %= p
    assert a != 0
    v = pow(a, (p-1)//2, p)
    assert v in (1,p-1)
    return 1 if v == 1 else -1

def is_prime(n: int) -> bool:
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n%d == 0: return n == d
        d += 1
    return True

# Exact Pythagorean identity behind the local family:
# (2t)^2 + (t^2-1)^2 = (t^2+1)^2.
for t in range(-25,26):
    B = 2*t
    C = t*t-1
    D = t*t+1
    assert B*B + C*C == D*D

# Counting proof encoded in the certificate:
# each prescribed character class for 2t has (q-1)/2 elements; the excluded set
# {+/-1} plus roots of t^2+1 has at most four. At q>=11, (q-1)/2 >= 5.
assert (11-1)//2 == 5
assert art['coordinate_pair_local_sign_flexibility']['construction']['existence_count'].startswith('each prescribed quadratic-character class')

# Exhaustively replay the local sign-surjectivity construction for many odd primes.
# This is a regression check for the uniform counting argument, not the proof cutoff itself.
for q in [p for p in range(11,300) if is_prime(p)]:
    seen = set()
    for t in range(1,q):
        if t in (1,q-1):
            continue
        if (t*t+1) % q == 0:
            continue
        B = (2*t) % q
        C = (t*t-1) % q
        D = (t*t+1) % q
        assert B and C and D
        # For A=q^m with m>0, all four local square conditions reduce mod q
        # to B^2, C^2, D^2 respectively and hence are nonzero square units.
        assert legendre(B*B,q) == 1
        assert legendre(C*C,q) == 1
        assert legendre(D*D,q) == 1
        # Odd-prime Hilbert formula with A=q^m, m odd: (A,B)_q=(B/q).
        seen.add(legendre(B,q))
    assert seen == {-1,1}, (q,seen)

profile = art['reciprocity_profile_result']
assert profile['forced_prime_receiver_alone_determines_global_hilbert_product'] is False
assert profile['product_formula_itself'] == 'UNIVERSAL_IDENTITY_NOT_NEW_ENDPOINT_CREDIT'
assert profile['certified_branch_pruning_from_natural_pairwise_hilbert_symbols'] is False
assert profile['natural_pairwise_hilbert_route_closed'] is True

assert state['current']['unit'] == '35EX-35_GOAL4G_JOINT_LOCAL_HILBERT_RECIPROCITY_PROFILE_TEST'
assert state['current']['status'] == 'PROVISIONAL_STACKED_PENDING_LATER_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['goal4f_hostile_audit_pass'] is False
assert state['claims']['goal4g_executed'] is True
assert state['claims']['natural_pairwise_hilbert_route_closed'] is True
assert state['claims']['cross_prime_branch_pruning_obtained'] is False
assert state['claims']['nonobvious_vertical_brauer_route_closed'] is False
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

print('PASS STAGE35_EX_35_GOAL4G_NATURAL_HILBERT_RECIPROCITY_NO_BRANCH_PRUNING')
