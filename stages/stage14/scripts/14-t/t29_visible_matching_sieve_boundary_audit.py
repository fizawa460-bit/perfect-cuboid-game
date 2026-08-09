#!/usr/bin/env python3
"""Stage14-t29: canonical visible-prime matching and sieve-boundary audit."""

from collections import Counter
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T28 = ROOT / "stages/stage14/scripts/14-t/t28_four_linear_cover_packet_audit.py"
T28_DATA = ROOT / "stages/stage14/data/14-t28/four_linear_cover_packet.json"
OUT = ROOT / "stages/stage14/data/14-t29/visible_matching_sieve_boundary.json"


def support_column(a, b, ell):
    cols = []
    vals = {
        "a": a,
        "b": b,
        "difference": b * b - a * a,
        "sum": a * a + b * b,
    }
    for name, value in vals.items():
        if ell > 1 and value % ell == 0:
            cols.append(name)
    assert len(cols) == 1, (a, b, ell, cols)
    return cols[0]


def matching_for_column(column):
    if column in ("a", "b"):
        return {(1, 2), (3, 4)}
    if column == "difference":
        return {(1, 3), (2, 4)}
    if column == "sum":
        return {(1, 4), (2, 3)}
    raise AssertionError(column)


def reduced_biquadrate_tautology(gs, pair, ell):
    g1, g2, g3, g4 = gs
    if pair == (1, 2):
        return (g4 * g4 - g3 * g3) % ell == 0
    if pair == (3, 4):
        return (g2 * g2 - g1 * g1) % ell == 0
    if pair == (1, 3):
        return (g4 * g4 - g2 * g2) % ell == 0
    if pair == (2, 4):
        return (g1 * g1 - g3 * g3) % ell == 0
    if pair == (1, 4):
        return (g2 * g2 + g3 * g3) % ell == 0
    if pair == (2, 3):
        return (g1 * g1 + g4 * g4) % ell == 0
    raise AssertionError(pair)


def audit():
    t28 = runpy.run_path(str(T28))
    ab_direction = t28["ab_direction"]
    largest_odd_prime_factor = t28["largest_odd_prime_factor"]
    squarefree_core = t28["squarefree_core"]
    is_square = t28["is_square"]
    AB_MAX = t28["SYN_AB_MAX"]
    PQ_MAX = t28["SYN_PQ_MAX"]

    totals = Counter()
    matching = Counter()
    visible_columns = Counter()
    visible_pairs = Counter()
    invisible_columns = Counter()

    for b in range(2, AB_MAX + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            eps, r, u, C, D, L, Delta = ab_direction(a, b)
            totals["directions"] += 1

            pstar = max(
                largest_odd_prime_factor(r),
                largest_odd_prime_factor(u),
                largest_odd_prime_factor(C),
                largest_odd_prime_factor(D),
            )
            assert pstar > 1
            assert Delta % pstar == 0
            column = support_column(a, b, pstar)
            allowed = matching_for_column(column)

            for q in range(1, PQ_MAX + 1):
                for p in range(1, PQ_MAX + 1):
                    if gcd(p, q) != 1:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue
                    totals["primitive_interval_tuples"] += 1

                    gs = (
                        b * p - a * q,
                        a * q + b * p,
                        b * q - a * p,
                        b * q + a * p,
                    )
                    assert min(gs) > 0
                    # The weighted-biquadrate identity is intrinsic to the four forms.
                    assert gs[0] * gs[0] + gs[3] * gs[3] == gs[1] * gs[1] + gs[2] * gs[2]

                    divinds = tuple(i + 1 for i, g in enumerate(gs) if g % pstar == 0)
                    if divinds:
                        assert len(divinds) == 2
                        assert divinds in allowed, (a, b, p, q, pstar, column, divinds)
                        totals["canonical_prime_rational_matching_incidence"] += 1
                        matching[f"{column}:{divinds[0]}{divinds[1]}"] += 1
                        assert reduced_biquadrate_tautology(gs, divinds, pstar)
                        totals["reduced_biquadrate_tautology_checks"] += 1
                    else:
                        totals["canonical_prime_no_linear_factor_residual"] += 1

                    prod = gs[0] * gs[1] * gs[2] * gs[3]
                    if not is_square(prod) or p == q:
                        continue

                    totals["non_diagonal_square_cover_hits"] += 1
                    ds = tuple(squarefree_core(g) for g in gs)
                    visible = tuple(i + 1 for i, d in enumerate(ds) if d % pstar == 0)
                    if visible:
                        # Square parity plus the matching theorem forces exactly the same pair.
                        assert divinds
                        assert visible == divinds
                        assert visible in allowed
                        totals["kernel_visible_non_diagonal_hits"] += 1
                        visible_columns[column] += 1
                        visible_pairs[f"{column}:{visible[0]}{visible[1]}"] += 1
                    else:
                        totals["kernel_invisible_non_diagonal_hits"] += 1
                        invisible_columns[column] += 1
                        if divinds:
                            totals["kernel_invisible_rational_even_hits"] += 1
                        else:
                            totals["kernel_invisible_gaussian_dual_residual_hits"] += 1

    assert totals["directions"] == 489
    assert totals["primitive_interval_tuples"] == 239121
    assert totals["canonical_prime_rational_matching_incidence"] == 6371
    assert totals["canonical_prime_no_linear_factor_residual"] == 232750
    assert totals["reduced_biquadrate_tautology_checks"] == 6371

    expected_matching = {
        "sum:14": 2294,
        "sum:23": 2294,
        "difference:13": 587,
        "difference:24": 260,
        "b:12": 466,
        "b:34": 466,
        "a:12": 2,
        "a:34": 2,
    }
    assert dict(matching) == expected_matching

    assert totals["non_diagonal_square_cover_hits"] == 98
    assert totals["kernel_visible_non_diagonal_hits"] == 32
    assert totals["kernel_invisible_non_diagonal_hits"] == 66
    assert totals["kernel_invisible_rational_even_hits"] == 0
    assert totals["kernel_invisible_gaussian_dual_residual_hits"] == 66
    assert dict(visible_columns) == {"sum": 30, "difference": 2}
    assert dict(visible_pairs) == {"sum:23": 15, "sum:14": 15, "difference:13": 2}
    assert dict(invisible_columns) == {"sum": 42, "difference": 16, "b": 8}

    return {
        "totals": dict(totals),
        "matching_incidence_counts": dict(matching),
        "visible_non_diagonal_columns": dict(visible_columns),
        "visible_non_diagonal_pairs": dict(visible_pairs),
        "invisible_non_diagonal_columns": dict(invisible_columns),
    }


def main():
    frozen28 = json.loads(T28_DATA.read_text())
    syn = audit()
    report = {
        "stage": "14-t29",
        "t28_frozen_reference": {
            "candidate_directions_D_le_B2m": frozen28["finite_candidate_universe"]["candidate_directions_D_le_B2m"],
            "candidate_directions_top_shell_B2m": frozen28["finite_candidate_universe"]["candidate_directions_top_shell_B2m"],
        },
        "exact_matching_theorem": {
            "odd_support_columns": "a, b, b^2-a^2, a^2+b^2 are pairwise disjoint at odd primes",
            "matching_ab": "{12,34}",
            "matching_difference": "{13,24}",
            "matching_sum": "{14,23}",
            "kernel_visible_membership": "exactly one matched pair",
            "canonical_prime_role": "large primitive congruence modulus, not an independent square-sieve character gate",
        },
        "synthetic_audit": syn,
        "analytic_boundary": {
            "canonical_visible_prime_reduced_biquadrate_is_tautological": True,
            "canonical_visible_prime_new_character_saving": False,
            "generic_diagonal_quartic_point_count_sufficient": False,
            "kernel_invisible_gaussian_dual_branch_required": True,
            "auxiliary_prime_character_average_still_candidate": True,
        },
        "decision": {
            "STAGE14_T29": "COMPLETE_VISIBLE_LARGEST_PRIME_MATCHING_AND_SIEVE_BOUNDARY",
            "ODD_DIRECTION_SUPPORT_COLUMNS_PAIRWISE_DISJOINT": True,
            "VISIBLE_PRIME_PERFECT_MATCHING_THEOREM": True,
            "VISIBLE_PRIME_EXACTLY_ONE_MATCHED_KERNEL_PAIR": True,
            "VISIBLE_LARGE_PRIME_PRIMITIVE_CONGRUENCE_EXPLICIT": True,
            "VISIBLE_CANONICAL_PRIME_NEW_CHARACTER_GATE": False,
            "VISIBLE_CANONICAL_PRIME_IS_INCIDENCE_MODULUS": True,
            "GENERIC_DIAGONAL_QUARTIC_POINT_COUNT_SUFFICIENT": False,
            "KERNEL_INVISIBLE_GAUSSIAN_DUAL_BRANCH_STILL_REQUIRED": True,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t30 family incidence attack on visible primitive congruence lines, with auxiliary-prime character averaging and the t26 Gaussian/dual residual branch kept separate",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["synthetic_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
