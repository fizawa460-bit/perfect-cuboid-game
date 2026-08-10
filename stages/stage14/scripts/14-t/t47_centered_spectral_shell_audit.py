#!/usr/bin/env python3
"""Stage14-t47: plug t46 into tH13 shell ledger and center the square detector."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import log, sqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T46_DATA = ROOT / "stages/stage14/data/14-t46/twist_translation_conductor_energy.json"
TH13_DATA = ROOT / "stages/stage14/data/tH13/sparse_many_conductor_adapter_summary.json"
OUT = ROOT / "stages/stage14/data/14-t47/centered_spectral_shell.json"

B = 10_000


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def fundamental_discriminant_from_squarefree(d: int) -> int:
    assert d > 0
    return d if d % 4 == 1 else 4 * d


def dyadic_Q(D: int) -> int:
    """Return Q with Q < D <= 2Q for integer D>1, Q a power of two."""
    assert D > 1
    j = (D - 1).bit_length() - 1
    return 1 << j


def exponent_proxy(x: int | float) -> float:
    assert x > 0
    return log(x) / log(B)


def matvec(M, v):
    return [sum(a * b for a, b in zip(row, v)) for row in M]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def power_iteration_psd(G, iters=160):
    n = len(G)
    v = [1.0 / sqrt(n)] * n
    lam = 0.0
    for _ in range(iters):
        w = matvec(G, v)
        nw = sqrt(dot(w, w))
        if nw == 0:
            return 0.0
        v = [x / nw for x in w]
        Gv = matvec(G, v)
        lam = dot(v, Gv)
    return lam


def main():
    t46 = json.loads(T46_DATA.read_text())
    th13 = json.loads(TH13_DATA.read_text())
    assert t46["decision"]["STAGE14_T46"] == "COMPLETE_TWIST_TRANSLATION_CONDUCTOR_ENERGY_AND_BASE_OPERATOR_REDUCTION"
    assert t46["decision"]["ALL_TWISTS_SHARE_BASE_QUADRATIC_CHARACTER_OPERATOR"] is True
    assert th13["status"] == "COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER"
    assert th13["proof_boundary"]["same_modulus_dispersion_receiver_proved"] is True
    assert th13["proof_boundary"]["critical_sqrt_ell_exponent_ledger_proved"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    states = t36["build_frozen_states"]()
    reps = t42["reciprocal_quotient"](states)
    assert len(reps) == 560

    kernel_hist = Counter(s["kernel"] for s in reps)
    ell_hist = Counter(s["ell"] for s in reps)
    kernels = sorted(kernel_hist)
    ells = sorted(ell_hist)
    H = len(reps)
    P = len(ells)
    A1 = sum(r * r for r in kernel_hist.values())
    E_ell = sum(r * r for r in ell_hist.values())
    assert len(kernels) == 544
    assert A1 == 592
    assert P == 87
    assert E_ell == 7184

    base_D = {k: fundamental_discriminant_from_squarefree(k) for k in kernels}
    max_D = max(base_D.values())
    L_numeric = max(ells)

    # tH13 dyadic conductor-shell census on the t46 base family. This is finite
    # diagnostic data only: the common-refinement aggregation theorem is not inferred.
    shell_members = defaultdict(list)
    principal_state_mass = kernel_hist.get(1, 0)
    for k in kernels:
        D = base_D[k]
        if D == 1:
            continue
        shell_members[dyadic_Q(D)].append(k)

    p_proxy = exponent_proxy(P)
    shell_rows = []
    positive_proxy_energy = 0
    negative_proxy_energy = 0
    weighted_conductor_energy = 0
    for Q in sorted(shell_members):
        ks = shell_members[Q]
        K = len(ks)
        state_mass = sum(kernel_hist[k] for k in ks)
        energy = sum(kernel_hist[k] ** 2 for k in ks)
        D_min = min(base_D[k] for k in ks)
        D_max = max(base_D[k] for k in ks)
        weighted = sum((L_numeric + base_D[k]) * kernel_hist[k] ** 2 for k in ks)
        weighted_conductor_energy += weighted
        k_proxy = exponent_proxy(K)
        q_proxy = exponent_proxy(2 * Q)
        margin = p_proxy + k_proxy - max(0.5, q_proxy)
        if margin > 0:
            positive_proxy_energy += energy
        else:
            negative_proxy_energy += energy
        qls_core = E_ell * energy * (L_numeric + 2 * Q)
        hs_core = E_ell * energy * (P * K)
        shell_rows.append({
            "Q": Q,
            "D_interval": f"({Q},{2*Q}]",
            "distinct_squareclasses": K,
            "state_mass": state_mass,
            "squareclass_energy": energy,
            "D_min": D_min,
            "D_max": D_max,
            "weighted_conductor_energy": weighted,
            "finite_B_exponent_proxy": {
                "p": p_proxy,
                "k": k_proxy,
                "q": q_proxy,
                "positive_gain_margin": margin,
                "positive_gain_proxy": margin > 0,
                "asymptotic_claim": False,
            },
            "unit_receiver_core": {
                "quadratic_large_sieve": qls_core,
                "hilbert_schmidt": hs_core,
                "best": min(qls_core, hs_core),
                "best_route": "QLS" if qls_core <= hs_core else "HS",
            },
        })

    max_envelope_weighted = (L_numeric + max_D) * A1

    # Weighted base character matrix W_{ell,k}=sqrt(r_k)*chi_k(ell).
    # Its row Gram G=W W^T has exact entries
    # G(ell,ell')=sum_k r_k chi_k(ell)chi_k(ell').
    G = []
    max_offdiag = 0
    max_offdiag_pair = None
    diag_min = None
    diag_max = None
    row_abs_sums = []
    for i, ell1 in enumerate(ells):
        row = []
        for j, ell2 in enumerate(ells):
            val = sum(
                kernel_hist[k] * legendre(k, ell1) * legendre(k, ell2)
                for k in kernels
            )
            row.append(val)
            if i == j:
                diag_min = val if diag_min is None else min(diag_min, val)
                diag_max = val if diag_max is None else max(diag_max, val)
            elif abs(val) > max_offdiag:
                max_offdiag = abs(val)
                max_offdiag_pair = [ell1, ell2, val]
        G.append(row)
        row_abs_sums.append(sum(abs(x) for x in row))

    schur_lambda_upper = max(row_abs_sums)
    lambda_power = power_iteration_psd(G)
    centered_r1_schur_upper = schur_lambda_upper / P
    centered_r1_power_diagnostic = lambda_power / P
    diagonal_baseline = H / P
    actual_r1 = kernel_hist.get(1, 0)

    # Pair-squareclass distribution has Gram G_pair = G o G, because summing over
    # ordered state pairs factorizes. Its target at twist 1 is c(1)=A1.
    G_pair = [[x * x for x in row] for row in G]
    pair_row_sums = [sum(row) for row in G_pair]
    pair_schur_lambda_upper = max(pair_row_sums)
    pair_lambda_power = power_iteration_psd(G_pair)
    centered_A1_schur_upper = pair_schur_lambda_upper / P
    centered_A1_power_diagnostic = pair_lambda_power / P

    # Exact centered detector theorem:
    # if k=1, every row character equals 1, so
    # r(1) P^2 <= ||W^T 1||^2 <= P ||W||_op^2.
    # Schur on G then gives the explicit row-correlation receiver.
    # For the pair distribution, replace G by G o G.
    single_offdiag_l1_max = max(
        sum(abs(G[i][j]) for j in range(P) if j != i) for i in range(P)
    )
    pair_offdiag_l2sq_max = max(
        sum(G[i][j] ** 2 for j in range(P) if j != i) for i in range(P)
    )

    report = {
        "stage": "14-t47",
        "imports": {
            "t46_base_operator": True,
            "tH13_adapter": True,
            "tH13_common_refinement_still_required_for_asymptotic_aggregation": True,
        },
        "base_population": {
            "states": H,
            "distinct_squareclasses": len(kernels),
            "A1": A1,
            "actual_squareclass_1_multiplicity": actual_r1,
            "distinct_canonical_test_primes": P,
            "canonical_prime_energy": E_ell,
            "max_test_prime": L_numeric,
            "max_base_fundamental_discriminant": max_D,
        },
        "conductor_shell_ledger": {
            "shell_count": len(shell_rows),
            "principal_state_mass": principal_state_mass,
            "nonprincipal_weighted_conductor_energy": weighted_conductor_energy,
            "max_range_weighted_envelope": max_envelope_weighted,
            "weighted_to_max_envelope_ratio": weighted_conductor_energy / max_envelope_weighted,
            "finite_proxy_positive_gain_energy": positive_proxy_energy,
            "finite_proxy_nonpositive_gain_energy": negative_proxy_energy,
            "finite_proxy_is_not_asymptotic_proof": True,
            "shells": shell_rows,
        },
        "centered_single_state_detector": {
            "weighted_matrix": "W_{p,kappa}=sqrt(r_kappa)*chi_kappa(p)",
            "gram": "G_{p,q}=sum_kappa r_kappa*chi_kappa(p)*chi_kappa(q)",
            "exact_identity": "r(1)*P^2 <= ||W^T 1||^2 <= P*lambda_max(G)",
            "spectral_receiver": "r(1) <= lambda_max(G)/P",
            "schur_receiver": "r(1) <= H/P + max_p sum_{q!=p}|G_pq|/P",
            "constant_term_one_quarter_present": False,
            "diagonal_baseline_H_over_P": diagonal_baseline,
            "gram_diagonal_min": diag_min,
            "gram_diagonal_max": diag_max,
            "max_offdiagonal_abs_correlation": max_offdiag,
            "max_offdiagonal_pair": max_offdiag_pair,
            "max_offdiagonal_l1_row_sum": single_offdiag_l1_max,
            "schur_lambda_upper": schur_lambda_upper,
            "power_iteration_lambda_diagnostic": lambda_power,
            "finite_schur_r1_upper": centered_r1_schur_upper,
            "finite_power_iteration_r1_diagnostic": centered_r1_power_diagnostic,
            "asymptotic_spectral_bound_proved": False,
        },
        "centered_pair_detector": {
            "pair_gram_identity": "G_pair = G hadamard-square G for ordered state pairs",
            "target_at_twist_1": "c(1)=A1",
            "spectral_receiver": "A1 <= lambda_max(G_pair)/P",
            "schur_receiver": "A1 <= H^2/P + max_p sum_{q!=p}|G_pq|^2/P",
            "max_offdiagonal_squared_row_sum": pair_offdiag_l2sq_max,
            "schur_lambda_upper": pair_schur_lambda_upper,
            "power_iteration_lambda_diagnostic": pair_lambda_power,
            "finite_schur_A1_upper": centered_A1_schur_upper,
            "finite_power_iteration_A1_diagnostic": centered_A1_power_diagnostic,
            "asymptotic_pair_spectral_bound_proved": False,
        },
        "tH13_instantiation": {
            "max_range_QLS_remains_insufficient": True,
            "conductor_energy_refinement_instantiated_on_frozen_base_family": True,
            "centered_detector_routes_to_same_modulus_product_kernel_dispersion": True,
            "missing_uniform_input": "physical row-correlation/spectral estimate for G over a growing test-prime family, together with tH12 common-refinement aggregation",
            "sufficient_single_state_condition": "P>=B^rho and max_p sum_{q!=p}|G_pq| <= H*P*B^{-delta} gives r(1) <= H*B^{-rho}+H*B^{-delta}",
            "sufficient_pair_energy_condition": "P>=B^rho and max_p sum_{q!=p}|G_pq|^2 <= H^2*P*B^{-delta} gives A1 <= H^2*B^{-rho}+H^2*B^{-delta}",
        },
        "tH_decision": {
            "additional_tH_stage_needed_now": False,
            "reason": "tH13 already supplies the exact same-modulus/product-kernel dispersion receiver; t47 specializes it to the physical Gram matrix, so the next task is a live arithmetic bound rather than another adapter",
            "reopen_trigger": "reopen tH only if t48 produces a new concrete row-correlation structure requiring a receiver not covered by tH13",
        },
        "decision": {
            "STAGE14_T47": "COMPLETE_TH13_SHELL_INSTANTIATION_AND_CENTERED_SPECTRAL_DETECTOR_REDUCTION",
            "TH13_USED_DIRECTLY": True,
            "BASE_CONDUCTOR_SHELL_LEDGER_FROZEN": True,
            "CONDUCTOR_ENERGY_REFINEMENT_INSTANTIATED": True,
            "CENTERED_DETECTOR_REMOVES_ONE_QUARTER_CONSTANT_TERM": True,
            "SINGLE_STATE_TARGET_REDUCES_TO_BASE_OPERATOR_SPECTRAL_NORM": True,
            "PAIR_PRINCIPAL_ENERGY_REDUCES_TO_HADAMARD_GRAM_SPECTRAL_NORM": True,
            "CENTERED_DISPERSION_IS_TH13_PRODUCT_KERNEL_RECEIVER": True,
            "UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED": False,
            "TWO_LOCAL_FILTER_CONSTANT_TERM_REMOVED": True,
            "GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_NEEDED": False,
            "NEXT": "Stage14-t48 prove a uniform physical row-correlation/spectral estimate for the t46 squareclass character matrix (or identify its exceptional coherent rows), using the common-core/canonical-prime geometry rather than another generic large-sieve adapter",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
