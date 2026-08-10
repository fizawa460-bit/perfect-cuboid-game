#!/usr/bin/env python3
"""Stage14-t61: Kummer polar Schatten/leverage obstruction audit."""

from __future__ import annotations

from pathlib import Path
import json
import math
import runpy

ROOT = Path(__file__).resolve().parents[4]
T57_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t57_rank1_kummer_mellin_audit.py"
T60_RESULT = ROOT / "stages/stage14/14-t60/result.md"
TH4_RESULT = ROOT / "stages/stage14/14-tH4/result.md"
OUT = ROOT / "stages/stage14/data/14-t61/polar_schatten_obstruction.json"

SPLIT_PRIMES = (13, 17, 29, 37, 53, 61, 73)


def resonant(t: int, u: int, p: int) -> bool:
    inv = pow(t, p - 2, p)
    if u % p in {t % p, (-t) % p, inv, (-inv) % p}:
        return True
    # Rows with t^4=1 are themselves square-valued off their zero sets.
    # Any two such exceptional rows can therefore correlate at full scale.
    return pow(t, 4, p) == 1 and pow(u, 4, p) == 1


def row_correlation(t: int, u: int, p: int, K) -> int:
    return sum(K(t, x, p) * K(u, x, p) for x in range(1, p))


def audit_prime(p: int, K) -> dict:
    assert p % 4 == 1
    n = p - 1
    weil_envelope = 7 * math.sqrt(p) + 8

    min_nonzero_row = n
    max_resonant_rows = 0
    max_resonant_correlation = 0
    max_nonresonant_correlation = 0
    nonresonant_checks = 0

    for t in range(1, p):
        nonzero = sum(1 for x in range(1, p) if K(t, x, p) != 0)
        assert nonzero >= n - 4
        min_nonzero_row = min(min_nonzero_row, nonzero)

        resonant_rows = 0
        for u in range(1, p):
            c = abs(row_correlation(t, u, p, K))
            if resonant(t, u, p):
                resonant_rows += 1
                max_resonant_correlation = max(max_resonant_correlation, c)
                assert c <= n
            else:
                nonresonant_checks += 1
                max_nonresonant_correlation = max(max_nonresonant_correlation, c)
                assert c <= weil_envelope + 1e-9
        assert resonant_rows <= 4
        max_resonant_rows = max(max_resonant_rows, resonant_rows)

    # Schur/Gershgorin bound for K K*: row sum <= n(7 sqrt(p)+12).
    gram_row_sum_upper = n * (7 * math.sqrt(p) + 12)
    K_op_upper = math.sqrt(gram_row_sum_upper)
    C_op_upper = K_op_upper / n

    # Parseval row energy >= (n-4)/n.  Since CC* <= ||C||op |C|,
    # the polar leverage of every evaluation vector is at least q/op.
    row_quadratic_lower = (n - 4) / n
    polar_leverage_lower = row_quadratic_lower / C_op_upper
    asymptotic_scale_ratio = polar_leverage_lower / (p ** 0.25)

    assert polar_leverage_lower > 0

    return {
        "p": p,
        "n": n,
        "min_nonzero_row_entries": min_nonzero_row,
        "max_resonant_rows_per_t": max_resonant_rows,
        "max_resonant_correlation": max_resonant_correlation,
        "max_nonresonant_correlation": max_nonresonant_correlation,
        "weil_safe_envelope": weil_envelope,
        "nonresonant_checks": nonresonant_checks,
        "gram_row_sum_upper": gram_row_sum_upper,
        "K_operator_norm_upper": K_op_upper,
        "C_operator_norm_upper": C_op_upper,
        "row_quadratic_energy_lower": row_quadratic_lower,
        "polar_leverage_lower": polar_leverage_lower,
        "polar_leverage_over_p_quarter": asymptotic_scale_ratio,
    }


def main() -> None:
    t60 = T60_RESULT.read_text()
    th4 = TH4_RESULT.read_text()
    assert "STAGE14_T60=COMPLETE_POLAR_KUMMER_ONE_SIDE_FOURTH_MOMENT_REDUCTION" in t60
    assert "POLAR_KUMMER_HALF_PACKET_FACTORIZATION_PROVED=true" in t60
    assert "CANONICAL_PRIME_POLAR_KUMMER_FOURTH_MOMENT_PROVED=false" in t60
    assert "PRIMITIVE_COVER_POLAR_KUMMER_FOURTH_MOMENT_PROVED=false" in t60
    assert "WEIGHTED_ONE_VARIABLE_LARGE_SIEVE_TRANSFER_PROVED=true" in th4
    assert "SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false" in th4

    t57 = runpy.run_path(str(T57_SCRIPT), run_name="stage14_t57_import")
    K = t57["K"]

    rows = [audit_prime(p, K) for p in SPLIT_PRIMES]

    pair_rows = []
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            # |C_p tensor C_q| = |C_p| tensor |C_q|, so leverage multiplies.
            leverage = a["polar_leverage_lower"] * b["polar_leverage_lower"]
            squared = leverage * leverage
            pair_rows.append({
                "p": a["p"],
                "q": b["p"],
                "two_prime_polar_leverage_lower": leverage,
                "two_prime_squared_polar_loss_lower": squared,
                "sqrt_pq": math.sqrt(a["p"] * b["p"]),
                "squared_loss_over_sqrt_pq": squared / math.sqrt(a["p"] * b["p"]),
            })

    report = {
        "stage": "14-t61",
        "split_primes": list(SPLIT_PRIMES),
        "prime_rows": rows,
        "two_prime_pairs": pair_rows,
        "totals": {
            "prime_count": len(rows),
            "two_prime_pair_count": len(pair_rows),
            "max_resonant_rows_per_t": max(r["max_resonant_rows_per_t"] for r in rows),
            "max_nonresonant_correlation": max(r["max_nonresonant_correlation"] for r in rows),
            "min_polar_leverage_over_p_quarter": min(r["polar_leverage_over_p_quarter"] for r in rows),
            "min_two_prime_squared_loss_over_sqrt_pq": min(r["squared_loss_over_sqrt_pq"] for r in pair_rows),
        },
        "exact_lemmas": {
            "fourier_equivalence": "K_r=(r-1) U_r C_r U_r^T",
            "row_resonance": "full-scale resonance only inside {+/-t,+/-t^-1}, plus the common t^4=1 exceptional class; <=4 rows total",
            "nonresonant_weil": "|R_r(t,t')| <= 7 sqrt(r)+8",
            "operator_bound": "||C_r||op <= sqrt((7 sqrt(r)+12)/(r-1)) = O(r^-1/4)",
            "row_parseval": "a_t^* C_r C_r^* a_t >= (r-5)/(r-1)",
            "polar_leverage": "a_t^* |C_r| a_t >= (r-5)/(sqrt(r-1)*sqrt(7 sqrt(r)+12)) = Omega(r^1/4)",
            "two_prime_tensor": "D_pq(t)=D_p(t)D_q(t), hence D_pq(t)^2=Omega(sqrt(pq))",
        },
        "decision": {
            "STAGE14_T61": "COMPLETE_POLAR_SCHATTEN_OBSTRUCTION_AND_SIGNED_RECTANGLE_REOPENING",
            "ONE_PRIME_KUMMER_MATRIX_FOURIER_EQUIVALENCE_PROVED": True,
            "ONE_PRIME_NONRESONANT_ROW_CORRELATION_WEIL_BOUND": True,
            "ONE_PRIME_KUMMER_OPERATOR_NORM_UPPER": "O(r^(-1/4))",
            "ONE_PRIME_POLAR_EVALUATION_LEVERAGE_LOWER": "Omega(r^(1/4))",
            "ONE_PRIME_KUMMER_SCHATTEN1_LOWER": "Omega(r^(1/4))",
            "TWO_PRIME_POLAR_EVALUATION_LEVERAGE_LOWER": "Omega((p*q)^(1/4))",
            "AUXILIARY_SCALE_L_POLAR_SQUARED_LOSS": "Omega(L)",
            "ARBITRARY_SUPPORT_POLAR_FOURTH_MOMENT_TARGET_VALID": False,
            "T60_ONE_SIDE_FOURTH_MOMENTS_REQUIRE_PHYSICAL_SUPPORT_STRUCTURE": True,
            "TH4_DIRECTLY_PROVES_CANONICAL_PRIME_POLAR_FOURTH_MOMENT": False,
            "TH4_DIRECTLY_PROVES_PRIMITIVE_COVER_POLAR_FOURTH_MOMENT": False,
            "T36_T38_DIRECTLY_CONTROL_POLAR_OPERATOR": False,
            "POLAR_ZERO_LOSS_SHORTCUT_VALID": False,
            "SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED": False,
            "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED": False,
            "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH17_NEEDED": True,
            "TH17_REQUESTED_OBJECT": "SignedOrthogonalRectangleKummerBilinearLargeSieve",
            "T_ROUTE_BLOCKED_WAITING_FOR_TH17": False,
            "NEXT": "Stage14-t62 attack the signed orthogonal-rectangle Kummer bilinear large sieve directly; run Stage14-tH17 in parallel",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
