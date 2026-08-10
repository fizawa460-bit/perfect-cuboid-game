#!/usr/bin/env python3
"""Stage14-t60: aggregated Kummer coefficient matrix / polar fourth-moment audit."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import cmath
import json
import math
import runpy

ROOT = Path(__file__).resolve().parents[4]
T57_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t57_rank1_kummer_mellin_audit.py"
T59_RESULT = ROOT / "stages/stage14/14-t59/result.md"
TH16_RESULT = ROOT / "stages/stage14/14-tH16/result.md"
OUT = ROOT / "stages/stage14/data/14-t60/polar_kummer_fourth_moment.json"

SPLIT_PRIMES = (5, 13, 17, 29)
TOL = 2e-8


def char_value(index: int, log_value: int, n: int) -> complex:
    return cmath.exp(2j * math.pi * index * log_value / n)


def aggregated_matrix(p: int, t57: dict):
    coeffs, logs = t57["mellin_coefficients"](p)
    n = p - 1

    C = [[0j for _ in range(n)] for _ in range(n)]
    fibers = Counter()
    original_energy = 0.0

    for j in range(n):
        for k in range(n):
            c = coeffs[j] * coeffs[k] / (n * n)
            a = (k - j) % n
            b = (j + k) % n
            C[a][b] += c
            fibers[(a, b)] += 1
            original_energy += abs(c) ** 2

    # The linear map (j,k)->(k-j,j+k) has kernel {(0,0),(n/2,n/2)}.
    assert max(fibers.values()) == 2
    assert set(fibers.values()) == {2}

    expected_original = ((p - 3) / (p - 1)) ** 2
    assert abs(original_energy - expected_original) < 1e-7

    aggregated_energy = sum(abs(z) ** 2 for row in C for z in row)
    assert aggregated_energy <= 2 * original_energy + 1e-7
    assert aggregated_energy <= 2 + 1e-7

    reconstruction_checks = 0
    max_error = 0.0
    for t in range(1, p):
        et = logs[t]
        for x in range(1, p):
            ex = logs[x]
            total = 0j
            for a in range(n):
                ca = char_value(a, et, n)
                for b in range(n):
                    if abs(C[a][b]) < 1e-14:
                        continue
                    total += C[a][b] * ca * char_value(b, ex, n)
            target = t57["K"](t, x, p)
            err = abs(total - target)
            max_error = max(max_error, err)
            assert err < TOL
            reconstruction_checks += 1

    return {
        "p": p,
        "mode_map_fiber_max": max(fibers.values()),
        "original_mode_energy": original_energy,
        "aggregated_matrix_hs2": aggregated_energy,
        "two_times_original_energy": 2 * original_energy,
        "reconstruction_checks": reconstruction_checks,
        "reconstruction_max_error": max_error,
    }


def main() -> None:
    t59 = T59_RESULT.read_text()
    th16 = TH16_RESULT.read_text()
    assert "STAGE14_T59=COMPLETE_EXACT_TWO_COMPARATOR_ORTHOGONAL_RECTANGLE_REDUCTION" in t59
    assert "BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2=true" in t59
    assert "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false" in t59
    assert "STAGE14_TH16=COMPLETE_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_APPLICABILITY_AUDIT" in th16
    assert "NAIVE_SAME_MODULUS_MELLIN_CAUCHY_CLOSES_TARGET=false" in th16
    assert "QUADRATIC_LARGE_SIEVE_CLOSES_T58_TARGET=false" in th16
    assert "SAME_MODULUS_TOROIDAL_KUMMER_LARGE_SIEVE_PROVED=false" in th16

    t57 = runpy.run_path(str(T57_SCRIPT), run_name="stage14_t57_import")
    rows = [aggregated_matrix(p, t57) for p in SPLIT_PRIMES]

    # Two-prime coefficient matrix is C_p tensor C_q, so HS^2 multiplies.
    pair_rows = []
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            hs2 = a["aggregated_matrix_hs2"] * b["aggregated_matrix_hs2"]
            assert hs2 <= 4 + 1e-6
            pair_rows.append({"p": a["p"], "q": b["p"], "tensor_hs2": hs2})

    report = {
        "stage": "14-t60",
        "split_primes": list(SPLIT_PRIMES),
        "prime_rows": rows,
        "two_prime_pairs": pair_rows,
        "totals": {
            "one_prime_reconstruction_checks": sum(r["reconstruction_checks"] for r in rows),
            "two_prime_tensor_pairs": len(pair_rows),
            "max_mode_map_fiber": max(r["mode_map_fiber_max"] for r in rows),
            "max_aggregated_matrix_hs2": max(r["aggregated_matrix_hs2"] for r in rows),
            "max_two_prime_tensor_hs2": max(r["tensor_hs2"] for r in pair_rows),
        },
        "exact_reduction": {
            "one_prime_matrix": "C_r(alpha,beta)=sum_{xi eta^-1=alpha, eta xi=beta} Ahat(eta)Ahat(xi)/(r-1)^2",
            "two_prime_matrix": "C_pq=C_p tensor C_q",
            "polar_factorization": "C_pq=L_pq R_pq^* with L=U Sigma^(1/2), R=V Sigma^(1/2)",
            "rectangle_trace": "T=sum_{j,h} Xhalf_{j,h} Yhalf_{j,h}",
            "outer_cauchy": "sum_pq |T|^2 <= sqrt(sum E_A^2 * sum E_B^2)",
            "t59_energy_bridge": "sqrt((sum |A_j|^2)(sum |B_j|^2)) <= sqrt(2) sum |A_j||B_j|",
        },
        "decision": {
            "STAGE14_T60": "COMPLETE_POLAR_KUMMER_ONE_SIDE_FOURTH_MOMENT_REDUCTION",
            "ONE_PRIME_AGGREGATED_MELLIN_COEFFICIENT_MATRIX_DEFINED": True,
            "ONE_PRIME_MODE_MAP_FIBER_MAX": 2,
            "ONE_PRIME_AGGREGATED_MATRIX_HS2_LE_2": True,
            "TWO_PRIME_COEFFICIENT_MATRIX_TENSOR_IDENTITY": True,
            "TWO_PRIME_AGGREGATED_MATRIX_HS2_LE_4": True,
            "POLAR_KUMMER_HALF_PACKET_FACTORIZATION_PROVED": True,
            "SAME_AUXILIARY_PAIR_OUTER_AVERAGE_PRESERVED": True,
            "INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED": False,
            "CANONICAL_PRIME_POLAR_KUMMER_FOURTH_MOMENT_PROVED": False,
            "PRIMITIVE_COVER_POLAR_KUMMER_FOURTH_MOMENT_PROVED": False,
            "POLAR_ONE_SIDE_FOURTH_MOMENT_PAIR_IMPLIES_T59_RECEIVER": True,
            "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED": False,
            "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "TH16_CONSUMED": True,
            "TH17_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH": False,
            "NEXT": "Stage14-t61 attack CanonicalPrimePolarKummerFourthMoment and PrimitiveCoverPolarKummerFourthMoment; first test tH4-compatible one-variable large-sieve/fourth-moment upgrades",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
