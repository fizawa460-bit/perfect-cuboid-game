#!/usr/bin/env python3
"""Stage14-4bc deterministic audit.

Checks imported theorem flags, split-E support algebra, whole-E edge transfer,
finite projective/root identities, and the exact exponent ledger.
"""

import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FOUR_BB = ROOT / "stages/stage14/14-4bb/result.md"
FOUR_AY = ROOT / "stages/stage14/14-4ay/result.md"
S5C = ROOT / "stages/stage14/14-s5c/result.md"
S5D = ROOT / "stages/stage14/14-s5d/result.md"
S5M = ROOT / "stages/stage14/14-s5m/result.md"
RESULT = ROOT / "stages/stage14/14-4bc/result.md"
SUPPLEMENT = ROOT / "stages/stage14/14-4bc/e-density-completion.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/aux_uniform_e_top_strip_summary.json"


def prime_factors(n: int):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def rad_odd(n: int) -> int:
    r = 1
    for p in prime_factors(n):
        if p != 2:
            r *= p
    return r


def jacobi_odd(a: int, n: int) -> int:
    if n == 1:
        return 1
    assert n > 0 and n % 2 == 1 and gcd(a, n) == 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def dot2(v, w):
    return sum(a * b for a, b in zip(v, w)) % 2


def main() -> None:
    bb = FOUR_BB.read_text()
    ay = FOUR_AY.read_text()
    s5c = S5C.read_text()
    s5d = S5D.read_text()
    s5m = S5M.read_text()
    result = RESULT.read_text()
    supplement = SUPPLEMENT.read_text()

    assert "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200" in bb
    assert "FROZEN_AUXILIARY_MODULUS_DOES_NOT_WORSEN_SLICING_ERROR=true" in ay
    assert "H / 23" in s5c or "H/23" in s5c
    assert "p|H : chi(d1)=+1" in s5d
    assert "MEDIUM_E_LINEAR_DISPERSION_PROVED=true" in s5m
    assert "E_FIXED_ROOT_SHORTEST_VECTOR_BOUND_PROVED=true" in s5m
    assert "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true" in result
    assert "BALANCED_SPLIT_E_TOP_STRIP_DISPERSION_PROVED=false" in result
    assert "F(s)=L(s,chi)L(s,chi*chi4)G(s)" in supplement

    # Exact F2 support algebra: H selected label 23 does not interact with
    # another H selected/unselected prime inside the same E column.
    selected_H = (0, 1, 1)
    unselected_H = (0, 0, 0)
    selected_H_rows = ((0, 1, 1), (1, 0, 0))
    unselected_H_row = (1, 0, 0)
    assert all(dot2(row, selected_H) == 0 for row in selected_H_rows)
    assert all(dot2(row, unselected_H) == 0 for row in selected_H_rows)
    assert dot2(unselected_H_row, selected_H) == 0
    assert dot2(unselected_H_row, unselected_H) == 0

    # Finite exact whole-E divisor identities and split-edge transfer.
    whole_identity_checks = 0
    split_transfer_checks = 0
    e_prime_mod4_checks = 0
    smaller_piece_checks = 0

    for m in range(2, 90):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = m * m + n * n
            e = rad_odd(E)
            for p in prime_factors(e):
                assert p % 4 == 1
                e_prime_mod4_checks += 1

            # Deterministic split of e into two coprime state-piece proxies.
            e23 = 1
            e0 = 1
            for idx, p in enumerate(prime_factors(e)):
                if idx % 2:
                    e0 *= p
                else:
                    e23 *= p
            assert e23 * e0 == e and gcd(e23, e0) == 1
            assert min(e23, e0) <= isqrt(e) + 1
            assert isqrt(e) <= isqrt(E)
            smaller_piece_checks += 1

            forms = {
                "m": m,
                "n": n,
                "m-n": m - n,
                "m+n": m + n,
            }
            for name, value in forms.items():
                for u in prime_factors(value):
                    if u == 2:
                        continue
                    # Odd support disjointness gives coprimality with e.
                    assert gcd(u, e) == 1
                    lhs = jacobi_odd(u, e)
                    expected = 1 if name in ("m", "n") else jacobi_odd(2, u)
                    assert lhs == expected
                    whole_identity_checks += 1
                    # Edge transfer, when both denominators are nontrivial.
                    if e23 > 1 and e0 > 1:
                        assert jacobi_odd(u, e23) == lhs * jacobi_odd(u, e0)
                        assert jacobi_odd(u, e0) == lhs * jacobi_odd(u, e23)
                        split_transfer_checks += 2

    # K5 bulk exponent ledger for eta=1/100.
    eta = Fraction(1, 100)
    long_edge_saving = eta / 2
    very_long_E_saving = eta
    all_short_modulus = 22 * eta
    periodic_first = 1 + 2 * all_short_modulus
    periodic_second = 3 * all_short_modulus
    assert long_edge_saving == Fraction(1, 200)
    assert very_long_E_saving == Fraction(1, 100)
    assert all_short_modulus == Fraction(11, 50)
    assert periodic_first == Fraction(36, 25)
    assert periodic_second == Fraction(33, 50)
    assert periodic_first < 2 and periodic_second < 2

    # Exact top-strip logic for kappa=1/100.
    # On a rational grid containing the boundary, every point outside the
    # declared strip obeys D(a,b)<=2-kappa.
    kappa = Fraction(1, 100)
    top_b = 1 - kappa
    top_a = Fraction(1, 2) - kappa
    max_outside = Fraction(0, 1)
    denominator = 200
    for ai in range(denominator + 1):
        a = Fraction(ai, denominator)
        for bi in range(denominator + 1):
            b = Fraction(bi, denominator)
            kexp = max(a, b / 2)
            dexp = a + b + 1 - kexp
            in_top = b > top_b and a > top_a
            if not in_top:
                max_outside = max(max_outside, dexp)
                assert dexp <= 2 - kappa
    assert max_outside == 2 - kappa

    report = {
        "stage": "14-4bc",
        "classification": "AUXILIARY_UNIFORMITY_CLOSED_AND_SPLIT_E_TOP_STRIP_ISOLATED",
        "imports": {
            "stage14_4bb_k4_graph_saving": "1/200",
            "stage14_4ay_linear_frozen_state_uniformity": True,
            "stage14_s5m_signed_root_E_lattice": True,
            "stage14_s5c_selected_H_label": "23",
            "stage14_s5d_unselected_H_row": "chi(d1)=+1",
        },
        "auxiliary_uniformity": {
            "linear_linear": "imported_from_14-4ay",
            "signed_root_E_auxiliary_lattice_is_sublattice": True,
            "auxiliary_lattice_determinant": "u*v*Q_aux",
            "shortest_vector_not_decreased": True,
            "uniform_E_pointwise": "Delta_aux << B^epsilon*(1+P/K(u,v))",
            "uniform_E_L2": "sum|Delta_aux|^2 << B^epsilon*UV*(1+P^2/K(U,V)^2)",
            "auxiliary_progression_exponent_loss": "0",
        },
        "split_E_structure": {
            "E_is_H_factor": True,
            "selected_label": "23",
            "odd_state_pieces": ["e_23", "e_0"],
            "max_piece_count": 2,
            "internal_E_E_reciprocal_edge": False,
            "whole_kernel_identity": {
                "m": "(u/e)=1",
                "n": "(u/e)=1",
                "m-n": "(u/e)=(2/u)",
                "m+n": "(u/e)=(2/u)",
            },
            "edge_transfer": "(u/e_23)=(u/e)*(u/e_0)",
            "one_reciprocal_active_E_vertex": True,
            "active_E_piece_choice": "min(e_23,e_0)",
            "active_E_piece_scale": "<=M",
        },
        "E_density_completion": {
            "coefficient": "b(n)=mu^2(n)*1_split*prod_{p|n}(2p/(p+1))",
            "dirichlet_factorization": "L(s,chi)*L(s,chi*chi4)*G(s)",
            "G_absolute_half_plane": "Re(s)>1/2+epsilon",
            "partial_sum_bound": "sum_{n<=x}b(n)chi(n) << (xq)^(1/2+epsilon) for x>=q",
            "lambda_E_dyadic_bound": "sum_{n~N}lambda_E(n)chi(n) << N^(-1/2)q^(1/2)(Nq)^epsilon",
        },
        "K5_bulk": {
            "eta": "1/100",
            "long_long_saving": "1/200",
            "very_long_E_threshold": "M^(6/100)",
            "very_long_E_saving": "1/100",
            "all_short_linear_threshold": "M^(4/100)",
            "all_short_E_threshold": "M^(6/100)",
            "all_short_modulus_exponent": "22/100",
            "periodic_first_exponent": "36/25",
            "periodic_second_exponent": "33/50",
            "worst_bulk_saving": "1/200",
        },
        "E_discrepancy": {
            "U": "M^a",
            "V": "M^b",
            "K_exponent": "max(a,b/2)",
            "error_exponent": "a+b+1-max(a,b/2)",
            "kappa": "1/100",
            "closed_outside_top_strip_saving": "1/100",
            "top_strip": {
                "V_lower": "M^(99/100)",
                "U_lower": "M^(49/100)",
                "name": "BALANCED_SPLIT_E_TOP_STRIP_DISPERSION",
            },
        },
        "updated_reciprocal_contract": {
            "old": "min(1/200,delta_aux,delta_E)",
            "new": "min(1/200,delta_top)",
            "closed_M_scale_saving": "1/200",
            "closed_B_scale_saving": "1/400",
            "closed_B_scale_error_exponent": "399/400",
        },
        "decision": {
            "STAGE14_4BC": "AUXILIARY_UNIFORMITY_CLOSED_AND_SPLIT_E_TOP_STRIP_ISOLATED",
            "LINEAR_AUXILIARY_UNIFORMITY_IMPORTED_FROM_4AY": True,
            "E_SIGNED_ROOT_AUXILIARY_SUBLATTICE_THEOREM_PROVED": True,
            "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED": True,
            "AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS": "0",
            "E_COLUMN_IS_H_FACTOR": True,
            "E_ODD_STATE_PIECE_COUNT_MAX": 2,
            "SPLIT_E_INTERNAL_RECIPROCAL_EDGE": False,
            "WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT": True,
            "RECIPROCAL_ACTIVE_E_PIECE_CAN_BE_CHOSEN_LE_M": True,
            "K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED": True,
            "K5_BULK_SAVING_EXPONENT": "1/200",
            "E_DISCREPANCY_OUTSIDE_TOP_STRIP_SAVING_EXPONENT": "1/100",
            "BALANCED_SPLIT_E_TOP_STRIP_DISPERSION_PROVED": False,
            "STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_REDUCED_TO_TOP_STRIP": True,
            "CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA": "min(1/200,delta_top)",
            "CLOSED_RECIPROCAL_B_SCALE_EXPONENT": "1-1/400",
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_COMPLETE_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4bd attack the balanced split-E top strip by a two-copy signed-root determinant/anti-determinant energy estimate, keeping both E state pieces visible; if a fixed saving is obtained, freeze the first complete reciprocal E_rec exponent and then return to the diagonal D_loc/rho_loc assignment",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report

    print(f"e_prime_mod4_checks={e_prime_mod4_checks}")
    print(f"whole_identity_checks={whole_identity_checks}")
    print(f"split_transfer_checks={split_transfer_checks}")
    print(f"smaller_piece_checks={smaller_piece_checks}")
    print(f"max_outside_top_strip_exponent={max_outside}")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
