#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage35-ex/35ex-11/reciprocity-routing-certificate.json"
BREADTH = ROOT / "stages/stage35-ex/35ex-11/post-three-reservoir-breadth-audit.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"


def v2(n: int) -> int:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def factor(n: int):
    n = abs(n)
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def legendre(a: int, ell: int) -> int:
    a %= ell
    assert a != 0
    z = pow(a, (ell - 1) // 2, ell)
    return 1 if z == 1 else -1


cert = json.loads(CERT.read_text())
breadth = json.loads(BREADTH.read_text())
state = json.loads(STATE.read_text())

# 35EX-11 mathematics is unchanged by the hostile-audit repair.
assert cert["unit"] == "35EX-11_RECIPROCITY_COUPLING_OR_BAD_SPLIT_PRIME_EXISTENCE"
assert cert["routing_consequence"]["inert_primes_source_oriented"] is True
assert cert["routing_consequence"]["bad_split_primes_impossible_under_counterexample"] is True
assert cert["routing_consequence"]["locally_good_split_primes_retain_binary_edge_choice"] is True
assert cert["routing_consequence"]["reservoir_choices_primewise_independent_at_current_squareclass_layer"] is True
assert cert["route_decision"]["universal_source_only_bad_split_prime_existence"] is False
assert cert["route_decision"]["current_three_reservoir_local_symbol_layer_global_contradiction"] is False
assert cert["route_decision"]["stronger_reciprocity_relation_ruled_out_in_principle"] is False
assert cert["route_decision"]["next_exact_leaf"] == "35EX-12_SUNIT_THUE_ADAPTER_OR_DYNAMIC_SUPPORT_BLOCKER"

for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert cert["credit"][key] is False

# Hostile-audit repair: a fresh Cycle Exploration Safety Protocol breadth audit
# must intervene between the post-35EX-09 route freezes and theorem-species change.
assert breadth["unit"] == "35EX-11B_FRESH_BREADTH_AUDIT"
assert breadth["trigger"]["material_receiver_change"] == "35EX-09_COMPLETE_THREE_RESERVOIR_SQUARECLASS_GRAPH"
assert breadth["trigger"]["old_35ex01_snapshot_sufficient"] is False
assert len(breadth["trigger"]["routes_frozen_since_prior_breadth_audit"]) >= 4
protocol = breadth["cycle_protocol"]
assert protocol["EXHAUSTIVE_VIEW_AUDIT"] is True
assert protocol["BLIND_REDISCOVERY"] is True
assert protocol["ARSENAL_COMPARISON_AFTER_BLIND_PASS"] is True
assert protocol["HISTORICAL_BLOCK_LEDGER_COMPARISON"] is True
assert protocol["SPLIT_TRIGGERED"] is False

snapshot = breadth["receiver_snapshot"]
assert snapshot["factorwise_support_complete_conditionally"] is True
assert snapshot["e_divides_c"] is True
assert snapshot["fixed_finite_support_over_all_master_hits"] is False
assert snapshot["global_E1_proved"] is False

blind = {row["id"]: row for row in breadth["blind_pass"]["candidates"]}
for candidate in (
    "E1-SUNIT-THUE-DYNAMIC-SUPPORT",
    "E1-ALTERNATE-NORM-SYMMETRY",
    "E1-NONNAIVE-DESCENT",
    "E1-GLOBAL-RECIPROCITY-BEYOND-LOCAL-GRAPH",
    "E1-RECEIVER-RESTRICTED-JOINT-LOCAL",
):
    assert blind[candidate]["status"] == "UNTESTED"
assert blind["E1-UNIFORM-ELLIPTIC-HEIGHT"]["status"] == "BLOCKED"
assert blind["E1-FIXED-FIBER-TORSION"]["status"] == "BLOCKED"

historical = {row["id"]: row for row in breadth["historical_route_reclassification"]}
assert historical["E1-GCD-SPLIT"]["status"] == "DOMINATED"
assert historical["E1-DOUBLE-PRIMITIVE-PYTH"]["status"] == "DOMINATED"
assert historical["E1-GAUSSIAN-DOUBLE-SQUARE"]["status"] == "DOMINATED"
assert historical["E1-LOCAL-VALUATION"]["status"] == "DOMINATED"
assert historical["E1-INFINITE-DESCENT"]["status"] == "UNTESTED"
assert historical["E1-SUNIT-THUE"]["status"] == "UNTESTED"
assert historical["E1-ELLIPTIC-HEIGHT"]["status"] == "BLOCKED"
assert historical["E1-FIXED-FIBER-TORSION"]["status"] == "BLOCKED"

arsenal = {row["id"]: row for row in breadth["arsenal_comparison"]["matches"]}
assert arsenal["S34-W01"]["status"] == "NOT_CURRENTLY_APPLICABLE_TO_FINITE_ENUMERATION"
assert arsenal["S34-W03"]["status"] == "UNTESTED_ADAPTER_CANDIDATE"
assert breadth["arsenal_comparison"]["matching_sunit_thue_card_found"] is False
assert breadth["arsenal_comparison"]["stage34_concrete_branch_counts_or_local_primes_transfer_allowed"] is False
assert breadth["block_ledger_comparison"]["no_block_promoted_to_impossibility"] is True

selection = breadth["selection"]
assert selection["selected_next_unit"] == "35EX-12_SUNIT_THUE_ADAPTER_OR_DYNAMIC_SUPPORT_BLOCKER"
assert selection["status"] == "RESELECTED_AFTER_FRESH_BREADTH_AUDIT"
assert selection["selection_is_theorem_credit"] is False
assert selection["finite_enumeration_authorized"] is False
assert set(selection["other_untested_candidates_preserved"]) == {
    "E1-ALTERNATE-NORM-SYMMETRY",
    "E1-NONNAIVE-DESCENT",
    "E1-GLOBAL-RECIPROCITY-BEYOND-LOCAL-GRAPH",
    "E1-RECEIVER-RESTRICTED-JOINT-LOCAL",
}
for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert breadth["credit"][key] is False

# Exact source witness: a genuine Master-Hit with no odd split prime in either
# source-known Branch-L reservoir. This refutes universal source-only split-prime
# existence; it is explicitly not an E1-counterexample witness.
a, b, m, n = (4, 3, 16, 5)
assert gcd(a, b) == gcd(m, n) == 1
assert (a-b) % 2 == (m-n) % 2 == 1
U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
assert (U1, V1, W1) == (7, 24, 25)
assert (U2, V2, W2) == (231, 160, 281)
master_norm = (V1*U2)**2 + (U1*V2)**2
assert isqrt(master_norm)**2 == master_norm

c = gcd(U1, U2)
p = gcd(W1, V2)
q = gcd(V1, V2)
D = U1 // c
T = U2 // c
K = (W1 // p) * (V1 // q)
assert (c,p,q,D,T,K) == (7,5,8,1,33,15)
assert v2(V1) < v2(V2)
t = D * V2 // (2*p*q)
assert t == 2
assert [ell for ell in factor(t) if ell % 4 == 1] == []
assert [ell for ell in factor(T) if ell % 4 == 1] == []

# The two inert T-primes are source-oriented exactly as the 35EX-11 proof says.
pq = p*q
assert legendre(-1, 3) == -1
assert legendre(-1, 11) == -1
assert legendre(pq, 3) == 1       # 3 -> T23
assert legendre(pq, 11) == -1     # 11 -> T14

# e divides c, while every odd prime of e must be 1 mod4. Since c=7, this source
# witness forces e=1 under any hypothetical counterexample based on this hit.
assert factor(c) == {7: 1}
assert 7 % 4 == 3

# Blind alternate-norm candidate starts from an exact identity, but remains
# explicitly UNTESTED beyond that identity.
assert (W1*U2)**2 + (U1*V2)**2 == (U1*W2)**2 + (V1*U2)**2

# Primewise routing truth-table sanity.
for ell in (3, 7, 11, 19, 23, 31):
    assert ell % 4 == 3
    assert legendre(-1, ell) == -1
for ell in (5, 13, 17, 29, 37, 41):
    assert ell % 4 == 1
    assert legendre(-1, ell) == 1

assert state["stage"] == "35-EX"
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

print("PASS STAGE35_EX_11_RECIPROCITY_AND_FRESH_BREADTH_AUDIT_V2")
