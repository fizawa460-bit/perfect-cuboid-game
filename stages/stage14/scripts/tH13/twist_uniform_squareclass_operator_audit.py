#!/usr/bin/env python3
"""Stage14-tH13 R2 deterministic audit for the t46 twist-uniform squareclass operator receiver."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T46_DATA = ROOT / "stages/stage14/data/14-t46/twist_translation_conductor_energy.json"
TH13_R1_DATA = ROOT / "stages/stage14/data/tH13/sparse_many_conductor_adapter_summary.json"
SUMMARY = ROOT / "stages/stage14/data/tH13/twist_uniform_squareclass_operator_summary.json"


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def squarefree_product(a: int, b: int) -> int:
    from math import gcd
    g = gcd(a, b)
    return (a // g) * (b // g)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def primes_one_mod(modulus: int, count: int) -> list[int]:
    out = []
    m = 1
    while len(out) < count:
        q = 1 + m * modulus
        if is_prime(q):
            out.append(q)
        m += 1
    return out


def matmul_column_gram(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    return [
        [sum(matrix[i][j] * matrix[i][k] for i in range(rows)) for k in range(cols)]
        for j in range(cols)
    ]


def frozen_input_audit() -> dict[str, int | bool]:
    t46 = json.loads(T46_DATA.read_text())
    r1 = json.loads(TH13_R1_DATA.read_text())

    assert t46["decision"]["STAGE14_T46"] == "COMPLETE_TWIST_TRANSLATION_CONDUCTOR_ENERGY_AND_BASE_OPERATOR_REDUCTION"
    assert t46["decision"]["MOVING_CONDUCTOR_FAMILY_IS_TWIST_TRANSLATED_SQUARECLASS_SPECTRUM"] is True
    assert t46["decision"]["TRANSLATED_CONDUCTOR_MULTIPLICITY_ENERGY_EQUALS_A1"] is True
    assert t46["decision"]["PRINCIPAL_CONDUCTOR_SLICE_EQUALS_R_TAU"] is True
    assert t46["decision"]["ALL_TWISTS_SHARE_BASE_QUADRATIC_CHARACTER_OPERATOR"] is True
    assert t46["decision"]["STANDARD_MAX_RANGE_LARGE_SIEVE_CLOSES_CRITICAL_STRIP"] is False
    assert t46["decision"]["TWO_LOCAL_FILTER_CONSTANT_TERM_REMOVED"] is False

    sq = t46["squareclass_translation"]
    ep = t46["canonical_prime_side"]
    gram = t46["base_character_gram_diagnostic"]
    assert (sq["states"], sq["distinct_squareclasses"], sq["squareclass_energy_A1"]) == (560, 544, 592)
    assert sq["max_squareclass_multiplicity"] == 2
    assert (ep["distinct_canonical_ells"], ep["canonical_ell_energy_unit_weights"]) == (87, 7184)
    assert gram["max_offdiagonal_abs_correlation"] == 81
    assert (gram["row_squared_norm_min"], gram["row_squared_norm_max"]) == (540, 544)
    assert gram["asymptotic_claim"] is False

    assert r1["status"] == "COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER"
    assert r1["proof_boundary"]["t45_power_saving_assumed"] is False

    for row in t46["top_heavy_twists"]:
        assert row["translated_distinct_conductors"] == 544
        assert row["translated_conductor_energy"] == 592
        assert row["translated_max_multiplicity"] == 2
        assert row["principal_conductor_multiplicity"] == row["expected_principal_slice_r_tau"]
        assert len(row["tau_bad_canonical_ells"]) <= 16

    return {
        "states": 560,
        "N_kappa": 544,
        "E_kappa": 592,
        "N_ell": 87,
        "E_ell": 7184,
        "max_frozen_row_correlation": 81,
        "t46_power_saving_assumed": False,
    }


def twist_uniform_operator_audit() -> dict[str, int | bool]:
    # Small exact model with no tau-bad rows.  D(k) differs from k by at most the
    # square factor 4 for odd evaluation primes, so chi_D(k)(ell)=chi_k(ell).
    ells = [13, 17, 29, 37]
    kappas = [1, 3, 5, 7, 11, 19]
    tau = 3
    assert all(ell % tau for ell in ells)
    assert all(all(k % ell for k in kappas) for ell in ells)

    base = [[legendre(k, ell) for k in kappas] for ell in ells]
    signs = [legendre(tau, ell) for ell in ells]
    twisted = [[signs[i] * base[i][j] for j in range(len(kappas))] for i in range(len(ells))]

    factorization_checks = 0
    for i, ell in enumerate(ells):
        for j, k in enumerate(kappas):
            kt = squarefree_product(tau, k)
            lhs = legendre(kt, ell)
            rhs = signs[i] * legendre(k, ell)
            assert lhs == rhs == twisted[i][j]
            factorization_checks += 1

    # Diagonal row signs are unitary: M^T M is unchanged.
    assert matmul_column_gram(base) == matmul_column_gram(twisted)

    # The translated principal conductor kappa=tau is the all-ones column after
    # the row sign is applied: chi_tau(ell)^2=1 on good rows.
    tau_col = kappas.index(tau)
    assert all(twisted[i][tau_col] == 1 for i in range(len(ells)))

    # Exact row-Gram identity G(ell,ell') = sum_k chi_k(ell*ell').
    gram_checks = 0
    for i, ell1 in enumerate(ells):
        for j, ell2 in enumerate(ells):
            lhs = sum(base[i][c] * base[j][c] for c in range(len(kappas)))
            if i == j:
                rhs = sum(legendre(k, ell1) ** 2 for k in kappas)
            else:
                rhs = sum(legendre(k, ell1) * legendre(k, ell2) for k in kappas)
            assert lhs == rhs
            gram_checks += 1

    return {
        "rows": len(ells),
        "columns": len(kappas),
        "factorization_checks": factorization_checks,
        "row_gram_checks": gram_checks,
        "column_gram_preserved_by_twist_sign": True,
        "translated_principal_column_is_constant_one": True,
    }


def sparse_countermodel_audit() -> dict[str, int | bool]:
    rows = [3, 5, 7]
    modulus = 8
    for p in rows:
        modulus *= p
    kappas = primes_one_mod(modulus, 5)

    assert len(set(kappas)) == 5
    assert all(q % 4 == 1 for q in kappas)
    assert all(is_prime(q) for q in kappas)

    matrix = []
    for p in rows:
        row = [legendre(q, p) for q in kappas]
        assert row == [1] * len(kappas)
        matrix.append(row)

    N_ell = len(rows)
    N_kappa = len(kappas)
    E_kappa_unit = N_kappa
    # All-ones matrix: the normalized all-ones input gives ||M||^2=N_ell*N_kappa,
    # while Hilbert-Schmidt gives the matching upper bound.
    operator_sq = N_ell * N_kappa
    hs_sq = sum(v * v for row in matrix for v in row)
    assert operator_sq == hs_sq
    assert E_kappa_unit == N_kappa

    return {
        "row_primes": N_ell,
        "prime_squareclasses": N_kappa,
        "unit_squareclass_energy": E_kappa_unit,
        "operator_norm_squared": operator_sq,
        "hilbert_schmidt_squared": hs_sq,
        "all_entries_one": True,
        "cardinality_plus_minimal_energy_forces_cancellation": False,
    }


def spectral_frozen_ledger_audit() -> dict[str, int | bool]:
    N_ell = 87
    N_kappa = 544
    max_corr = 81
    gershgorin = N_kappa + (N_ell - 1) * max_corr
    hs = N_ell * N_kappa
    assert gershgorin == 7510
    assert hs == 47328
    assert gershgorin < hs
    return {
        "gershgorin_operator_squared_upper": gershgorin,
        "hilbert_schmidt_operator_squared_upper": hs,
        "finite_diagnostic_only": True,
    }


def critical_exponent_audit() -> dict[str, str | bool]:
    q = Fraction(1, 2)
    k = Fraction(4, 1)
    standard_op_sq = max(q, k)
    standard_amp = standard_op_sq / 2
    assert standard_op_sq == 4
    assert standard_amp == 2

    # Optimistic Baier sparse-additive route after Gauss/Cauchy:
    # K*X_AP*(sqrt(Q)+N_kappa), with X_AP=B^o(1) and beta=0.
    baier_best = k + max(q / 2, Fraction(0, 1))
    assert baier_best == Fraction(17, 4)
    assert baier_best > standard_op_sq

    # Near-orthogonality would improve HS by min(alpha,beta)/2 in amplitude.
    alpha = Fraction(2, 5)
    beta = Fraction(1, 3)
    hs_op_sq = alpha + beta
    near_op_sq = max(alpha, beta)
    gain = (hs_op_sq - near_op_sq) / 2
    assert gain == min(alpha, beta) / 2 == Fraction(1, 6)

    return {
        "critical_Q_exponent": str(q),
        "safe_K_exponent": str(k),
        "standard_operator_squared_exponent": str(standard_op_sq),
        "standard_amplitude_cost_exponent": str(standard_amp),
        "optimistic_sparse_additive_operator_squared_exponent_beta0": str(baier_best),
        "known_sparse_additive_route_beats_standard_at_endpoint": False,
        "near_orthogonality_sample_amplitude_gain": str(gain),
    }


def summary_contract_audit() -> dict[str, bool]:
    s = json.loads(SUMMARY.read_text())
    assert s["status"] == "COMPLETE_TWIST_UNIFORM_SPARSE_SQUARECLASS_OPERATOR_RECEIVER"
    pb = s["proof_boundary"]
    assert pb["arbitrary_544_conductor_model_superseded"] is True
    assert pb["all_twists_share_one_base_operator"] is True
    assert pb["canonical_prime_selector_weight_preserved"] is True
    assert pb["squareclass_energy_E_kappa_explicit"] is True
    assert pb["canonical_prime_energy_E_ell_explicit"] is True
    assert pb["spectral_R1_R2_receiver"] is True
    assert pb["weighted_product_character_dispersion_receiver"] is True
    assert pb["cardinality_plus_E_kappa_alone_gives_cancellation"] is False
    assert pb["simple_factor_structure_alone_gives_cancellation"] is False
    assert pb["two_local_filter_constant_term_removed"] is False
    assert pb["t46_power_saving_assumed"] is False
    assert pb["critical_sqrt_ell_strip_power_saving_proved"] is False
    assert pb["generic_cross_good_global_power_saving_proved"] is False
    return {
        "summary_locked": True,
        "no_t46_power_saving_assumed": True,
        "no_critical_strip_power_saving_claim": True,
        "two_local_constant_boundary_locked": True,
    }


def main() -> None:
    report = {
        "frozen": frozen_input_audit(),
        "twist_uniform_operator": twist_uniform_operator_audit(),
        "sparse_countermodel": sparse_countermodel_audit(),
        "spectral_frozen_ledger": spectral_frozen_ledger_audit(),
        "critical_exponents": critical_exponent_audit(),
        "contract": summary_contract_audit(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH13 R2 twist-uniform squareclass operator audit: PASS")


if __name__ == "__main__":
    main()
