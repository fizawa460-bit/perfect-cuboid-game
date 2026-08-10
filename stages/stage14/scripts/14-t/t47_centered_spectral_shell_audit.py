#!/usr/bin/env python3
"""Stage14-t47: tH13 shell instantiation and centered spectral detector."""

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


def funddisc(d: int) -> int:
    return d if d % 4 == 1 else 4 * d


def dyadic_Q(D: int) -> int:
    assert D > 1
    return 1 << ((D - 1).bit_length() - 1)


def blog(x: int | float) -> float:
    return log(x) / log(B)


def matvec(M, v):
    return [sum(a * b for a, b in zip(row, v)) for row in M]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def power_iteration(G, iters=160):
    n = len(G)
    v = [1.0 / sqrt(n)] * n
    lam = 0.0
    for _ in range(iters):
        w = matvec(G, v)
        nw = sqrt(dot(w, w))
        if not nw:
            return 0.0
        v = [x / nw for x in w]
        lam = dot(v, matvec(G, v))
    return lam


def main():
    t46 = json.loads(T46_DATA.read_text())
    th13 = json.loads(TH13_DATA.read_text())
    assert t46["decision"]["ALL_TWISTS_SHARE_BASE_QUADRATIC_CHARACTER_OPERATOR"] is True
    assert th13["status"] == "COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER"
    assert th13["proof_boundary"]["same_modulus_dispersion_receiver_proved"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    kh = Counter(s["kernel"] for s in reps)
    eh = Counter(s["ell"] for s in reps)
    kernels = sorted(kh)
    ells = sorted(eh)
    H, P = len(reps), len(ells)
    A1 = sum(v * v for v in kh.values())
    Eell = sum(v * v for v in eh.values())
    assert (len(kernels), P, A1, Eell) == (544, 87, 592, 7184)

    D = {k: funddisc(k) for k in kernels}
    maxD, L = max(D.values()), max(ells)

    # tH13 shell ledger, compacted for frozen output.
    shells = defaultdict(list)
    for k in kernels:
        if D[k] != 1:
            shells[dyadic_Q(D[k])].append(k)
    p = blog(P)
    shell_summary = []
    pos_energy = 0
    nonpos_energy = 0
    weighted = 0
    weighted_rows = []
    for Q in sorted(shells):
        ks = shells[Q]
        K = len(ks)
        E = sum(kh[k] ** 2 for k in ks)
        W = sum((L + D[k]) * kh[k] ** 2 for k in ks)
        weighted += W
        margin = p + blog(K) - max(0.5, blog(2 * Q))
        if margin > 0:
            pos_energy += E
        else:
            nonpos_energy += E
        shell_summary.append([Q, K, E, round(margin, 6)])
        weighted_rows.append((W, Q, K, E, max(D[k] for k in ks)))
    weighted_rows.sort(reverse=True)
    max_envelope = (L + maxD) * A1

    # Weighted state-squareclass character Gram.
    G = []
    max_offdiag = 0
    max_pair = None
    dmin = None
    dmax = None
    for i, p1 in enumerate(ells):
        row = []
        for j, p2 in enumerate(ells):
            val = sum(kh[k] * legendre(k, p1) * legendre(k, p2) for k in kernels)
            row.append(val)
            if i == j:
                dmin = val if dmin is None else min(dmin, val)
                dmax = val if dmax is None else max(dmax, val)
            elif abs(val) > max_offdiag:
                max_offdiag = abs(val)
                max_pair = [p1, p2, val]
        G.append(row)

    row_abs = [sum(abs(x) for x in row) for row in G]
    single_off_l1 = max(sum(abs(G[i][j]) for j in range(P) if j != i) for i in range(P))
    single_schur = max(row_abs)
    single_power = power_iteration(G)

    # Ordered-pair squareclass Gram is the Hadamard square G o G.
    G2 = [[x * x for x in row] for row in G]
    pair_off_l2 = max(sum(G[i][j] ** 2 for j in range(P) if j != i) for i in range(P))
    pair_schur = max(sum(row) for row in G2)
    pair_power = power_iteration(G2)

    report = {
        "stage": "14-t47",
        "base": {
            "states": H,
            "distinct_squareclasses": len(kernels),
            "A1": A1,
            "r1": kh.get(1, 0),
            "test_prime_count": P,
            "canonical_prime_energy": Eell,
            "max_test_prime": L,
            "max_base_fundamental_discriminant": maxD,
        },
        "tH13_shell_instantiation": {
            "shell_count": len(shell_summary),
            "shell_summary_Q_K_E_margin": shell_summary,
            "finite_positive_gain_energy": pos_energy,
            "finite_nonpositive_gain_energy": nonpos_energy,
            "weighted_conductor_energy": weighted,
            "max_range_weighted_envelope": max_envelope,
            "weighted_to_max_envelope_ratio": weighted / max_envelope,
            "top5_weighted_shells_W_Q_K_E_Dmax": [list(x) for x in weighted_rows[:5]],
            "finite_proxy_is_not_asymptotic_proof": True,
        },
        "centered_single_state_detector": {
            "identity": "r(1)*P^2 <= ||W^T1||^2 <= P*lambda_max(G)",
            "spectral_receiver": "r(1)<=lambda_max(G)/P",
            "schur_receiver": "r(1)<=H/P+max_p sum_{q!=p}|G_pq|/P",
            "one_quarter_constant_removed": True,
            "diagonal_H_over_P": H / P,
            "gram_diagonal_min": dmin,
            "gram_diagonal_max": dmax,
            "max_offdiagonal_abs": max_offdiag,
            "max_offdiagonal_pair": max_pair,
            "max_offdiagonal_l1_row_sum": single_off_l1,
            "schur_lambda_upper": single_schur,
            "power_iteration_lambda_diagnostic": single_power,
            "finite_schur_r1_upper": single_schur / P,
            "finite_power_r1_diagnostic": single_power / P,
            "asymptotic_bound_proved": False,
        },
        "centered_pair_detector": {
            "identity": "G_pair=G hadamard-square G; c(1)=A1",
            "spectral_receiver": "A1<=lambda_max(G_pair)/P",
            "schur_receiver": "A1<=H^2/P+max_p sum_{q!=p}|G_pq|^2/P",
            "max_offdiagonal_squared_row_sum": pair_off_l2,
            "schur_lambda_upper": pair_schur,
            "power_iteration_lambda_diagnostic": pair_power,
            "finite_schur_A1_upper": pair_schur / P,
            "finite_power_A1_diagnostic": pair_power / P,
            "asymptotic_bound_proved": False,
        },
        "proof_contract": {
            "centered_detector_is_tH13_product_kernel_dispersion": True,
            "missing_uniform_input": "physical row-correlation/spectral estimate over a growing test-prime family plus tH12 common-refinement aggregation",
            "single_sufficient": "P>=B^rho and max_p sum_{q!=p}|G_pq|<=H*P*B^-delta => r1<=H*B^-rho+H*B^-delta",
            "pair_sufficient": "P>=B^rho and max_p sum_{q!=p}|G_pq|^2<=H^2*P*B^-delta => A1<=H^2*B^-rho+H^2*B^-delta",
        },
        "tH_decision": {
            "additional_tH_needed": False,
            "reason": "tH13 already contains the product-kernel/same-modulus dispersion receiver; the next missing input is live arithmetic correlation, not a new adapter",
            "reopen_trigger": "only if t48 exposes a new correlation structure not covered by tH13",
        },
        "decision": {
            "STAGE14_T47": "COMPLETE_TH13_SHELL_INSTANTIATION_AND_CENTERED_SPECTRAL_DETECTOR_REDUCTION",
            "TH13_USED_DIRECTLY": True,
            "CONDUCTOR_ENERGY_REFINEMENT_INSTANTIATED": True,
            "CENTERED_DETECTOR_REMOVES_ONE_QUARTER_CONSTANT_TERM": True,
            "SINGLE_STATE_TARGET_REDUCES_TO_BASE_OPERATOR_SPECTRAL_NORM": True,
            "PAIR_PRINCIPAL_ENERGY_REDUCES_TO_HADAMARD_GRAM_SPECTRAL_NORM": True,
            "CENTERED_DISPERSION_IS_TH13_PRODUCT_KERNEL_RECEIVER": True,
            "UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_NEEDED": False,
            "NEXT": "Stage14-t48 prove a uniform physical row-correlation/spectral estimate for the squareclass character Gram matrix, or classify exceptional coherent rows using common-core/canonical-prime geometry",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
