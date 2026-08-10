#!/usr/bin/env python3
"""Stage14-tH13 deterministic audit for the sparse many-conductor adapter."""

from __future__ import annotations

from collections import defaultdict
from math import isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T44 = ROOT / "stages/stage14/data/14-t44/canonical_prime_twist_support.json"
T45 = ROOT / "stages/stage14/data/14-t45/two_canonical_character.json"
TH12 = ROOT / "stages/stage14/data/tH12/ld2_kummer_incidence_receiver_summary.json"
SUMMARY = ROOT / "stages/stage14/data/tH13/sparse_many_conductor_adapter_summary.json"


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def funddisc_from_squarefree(d: int) -> int:
    assert d > 0
    return d if d % 4 == 1 else 4 * d


def predecessor_contract_audit() -> dict:
    t44 = json.loads(T44.read_text())
    t45 = json.loads(T45.read_text())
    th12 = json.loads(TH12.read_text())

    assert t44["decision"]["NONPRINCIPAL_CROSS_BAD_PRIME_ROUTES_INTO_TWIST"] is True
    assert t44["decision"]["FIXED_TWIST_SUPER_SQRT_EXPOSED_CANONICAL_PRIMES"] == "O(1)"
    assert t44["support_ledger"]["super_sqrt_prime_support_bound"] == "omega_{p>2sqrt(B)}(tau)<=16+o(1)"

    assert t45["decision"]["FIXED_PARTNER_QUADRATIC_CHARACTER_CERTIFIED"] is True
    assert t45["decision"]["TH13_REOPEN_TRIGGER"] is True
    assert t45["decision"]["CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED"] is False
    rows = t45["generic_cross_good"]["top_heavy_targets"]
    assert len(rows) == 8
    assert all(r["distinct_fixed_partner_conductors"] == 544 for r in rows)
    assert max(r["max_pairs_sharing_one_partner_conductor"] for r in rows) == 1114

    assert th12["status"] == "COMPLETE_LD2_KUMMER_CANONICAL_PRIME_COMMON_CORE_RECEIVER"
    assert th12["proof_boundary"]["canonical_prime_selector_cancellation_proved"] is False

    return {
        "t44_bad_prime_route": True,
        "t45_character_trigger": True,
        "top_heavy_targets": len(rows),
        "distinct_conductors_each": 544,
        "max_same_conductor_candidate_multiplicity": 1114,
        "tH12_common_refinement_imported": True,
    }


def selector_and_same_modulus_collapse_audit() -> dict:
    # Exact toy rectangular family.  Repeated ell and repeated D are deliberately present.
    x_rows = [
        {"ell": 5, "a": 2, "w": 1},
        {"ell": 5, "a": -1, "w": 1},
        {"ell": 13, "a": 3, "w": 2},
    ]
    y_rows = [
        {"D": 17, "b": 1, "v": 1},
        {"D": 17, "b": 2, "v": -1},
        {"D": 29, "b": -1, "v": 2},
    ]

    direct = 0
    for x in x_rows:
        for y in y_rows:
            direct += x["a"] * x["w"] * y["b"] * y["v"] * legendre(y["D"], x["ell"])

    A = defaultdict(int)
    B = defaultdict(int)
    for x in x_rows:
        A[x["ell"]] += x["a"] * x["w"]
    for y in y_rows:
        B[y["D"]] += y["b"] * y["v"]

    collapsed = sum(B[D] * A[ell] * legendre(D, ell) for D in B for ell in A)
    assert direct == collapsed

    E_ell = sum(v * v for v in A.values())
    E_D = sum(v * v for v in B.values())
    assert E_ell > 0 and E_D > 0

    return {
        "direct_bilinear": direct,
        "collapsed_bilinear": collapsed,
        "prime_cells": len(A),
        "conductor_cells": len(B),
        "E_ell": E_ell,
        "E_D": E_D,
        "selector_preserved_exactly": True,
        "same_modulus_collapsed_exactly": True,
    }


def principal_slice_audit() -> dict:
    A = {5: 2, 13: -3, 17: 4}
    B1 = 7
    direct = sum(B1 * a * legendre(1, ell) for ell, a in A.items())
    separated = B1 * sum(A.values())
    assert direct == separated
    return {"principal_value": direct, "separate_formula_exact": True}


def dispersion_identity_audit() -> dict:
    # Distinct positive fundamental discriminants, all coprime to the prime support.
    primes = [5, 13, 37]
    beta = {17: 2, 29: -1, 41: 3}

    lhs = sum(sum(b * legendre(D, ell) for D, b in beta.items()) ** 2 for ell in primes)
    E_D = sum(b * b for b in beta.values())
    diagonal = len(primes) * E_D

    gamma = defaultdict(int)
    for D, b in beta.items():
        for Dp, bp in beta.items():
            if D == Dp:
                continue
            kappa = funddisc_from_squarefree(squarefree_kernel(D * Dp))
            gamma[kappa] += b * bp

    offdiag = 0
    for kappa, coeff in gamma.items():
        S = sum(legendre(kappa, ell) for ell in primes)
        offdiag += coeff * S

    assert lhs == diagonal + offdiag
    return {
        "prime_support": len(primes),
        "conductor_support": len(beta),
        "product_kernel_support": len(gamma),
        "second_moment": lhs,
        "diagonal": diagonal,
        "offdiagonal": offdiag,
        "dispersion_identity_exact": True,
    }


def sparse_cardinality_countermodel_audit() -> dict:
    support = [3, 5, 7, 11]
    M = 8
    for p in support:
        M *= p
    assert M == 9240

    # Explicit primes q == 1 mod M.  They are fundamental discriminants because q == 1 mod 4.
    conductors = [9241, 18481, 55441, 92401, 101641, 110881, 120121, 129361]
    for q in conductors:
        assert q % M == 1
        assert is_prime(q)
        assert q % 4 == 1
        for p in support:
            assert legendre(q, p) == 1

    P = len(support)
    K = len(conductors)
    all_ones_operator_norm_squared = P * K
    cardinality_only_additive_cost = P + K
    assert all_ones_operator_norm_squared > cardinality_only_additive_cost

    return {
        "P": P,
        "K": K,
        "modulus_M": M,
        "all_character_entries_plus_one": True,
        "operator_norm_squared": all_ones_operator_norm_squared,
        "P_plus_K": cardinality_only_additive_cost,
        "cardinality_only_additive_large_sieve_fails": True,
    }


def critical_exponent_ledger_audit() -> dict:
    def qls_exp(e_ell: float, e_D: float, q: float) -> float:
        return (e_ell + e_D + max(0.5, q)) / 2.0

    def hs_exp(e_ell: float, e_D: float, p: float, k: float) -> float:
        return (e_ell + e_D + p + k) / 2.0

    def unit_gain(p: float, k: float, q: float) -> float:
        return max(0.0, (p + k - max(0.5, q)) / 2.0)

    assert unit_gain(0.5, 0.0, 0.5) == 0.0
    assert unit_gain(0.5, 0.0, 1.0) == 0.0
    assert unit_gain(0.5, 0.25, 0.5) == 0.125
    assert qls_exp(0.5, 0.25, 0.5) == 0.625
    assert hs_exp(0.5, 0.25, 0.5, 0.25) == 0.75

    return {
        "critical_L_exponent": 0.5,
        "sparse_k0_full_prime_p_half_gain": unit_gain(0.5, 0.0, 0.5),
        "example_positive_gain": unit_gain(0.5, 0.25, 0.5),
        "ledger_formula_checked": True,
    }


def summary_contract_audit() -> dict:
    s = json.loads(SUMMARY.read_text())
    assert s["status"] == "COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER"
    pb = s["proof_boundary"]
    assert pb["adapter_theorem_proved"] is True
    assert pb["canonical_prime_selector_weight_preserved"] is True
    assert pb["t44_bad_prime_routing_included"] is True
    assert pb["principal_conductor_separated"] is True
    assert pb["conductor_energy_refinement_available"] is True
    assert pb["sparse_cardinality_replaces_conductor_range"] is False
    assert pb["sparse_cardinality_countermodel_recorded"] is True
    assert pb["critical_sqrt_ell_exponent_ledger_proved"] is True
    assert pb["t45_power_saving_assumed"] is False
    assert pb["critical_sqrt_ell_strip_power_saving_proved"] is False
    assert pb["generic_cross_good_global_power_saving_proved"] is False
    return {
        "summary_status_locked": True,
        "no_t45_power_saving_assumption": True,
        "no_false_global_power_saving_claim": True,
    }


def main() -> None:
    report = {
        "predecessors": predecessor_contract_audit(),
        "coefficient_collapse": selector_and_same_modulus_collapse_audit(),
        "principal": principal_slice_audit(),
        "dispersion": dispersion_identity_audit(),
        "countermodel": sparse_cardinality_countermodel_audit(),
        "critical_ledger": critical_exponent_ledger_audit(),
        "contract": summary_contract_audit(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH13 sparse many-conductor adapter audit: PASS")


if __name__ == "__main__":
    main()
