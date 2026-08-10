#!/usr/bin/env python3
"""Stage14-t48: physical row-correlation / exceptional-coherence audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T47_DATA = ROOT / "stages/stage14/data/14-t47/centered_spectral_shell.json"
OUT = ROOT / "stages/stage14/data/14-t48/physical_row_correlation.json"

TOP_PAIRS = 12


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def reduced_physical_F(s) -> int:
    """Remove the canonical even ell^2 factor on the visible branch."""
    F = s["F"]
    ell = s["ell"]
    if s["branch"] == "visible":
        assert F % (ell * ell) == 0
        F //= ell * ell
    return F


def cover_key(s):
    return (min(s["p"], s["q"]), max(s["p"], s["q"]))


def relation_key(s, lam, mu):
    if s["ell"] == lam:
        return "state_ell=left_test"
    if s["ell"] == mu:
        return "state_ell=right_test"
    return "state_ell=other"


def partition_summary(reps, values, keyfun):
    cells = defaultdict(int)
    for s, v in zip(reps, values):
        cells[keyfun(s)] += v
    vals = sorted((abs(v), str(k), v) for k, v in cells.items())
    top_abs, top_key, top_signed = vals[-1]
    l2 = sum(v * v for v in cells.values())
    return {
        "cells": len(cells),
        "max_abs_cell": top_abs,
        "max_abs_cell_key": top_key,
        "max_abs_cell_signed": top_signed,
        "cell_l2_energy": l2,
    }


def main():
    t47 = json.loads(T47_DATA.read_text())
    assert t47["decision"]["STAGE14_T47"] == "COMPLETE_TH13_SHELL_INSTANTIATION_AND_CENTERED_SPECTRAL_DETECTOR_REDUCTION"
    assert t47["decision"]["PAIR_PRINCIPAL_ENERGY_REDUCES_TO_HADAMARD_GRAM_SPECTRAL_NORM"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    common_packet_key = t42["common_packet_key"]
    assert len(reps) == 560

    ells = sorted({s["ell"] for s in reps})
    directions = sorted({(s["a"], s["b"]) for s in reps})
    common_packets = sorted({common_packet_key(s) for s in reps})
    assert len(ells) == 87
    assert len(directions) == 137
    assert all(ell % 4 == 1 for ell in ells)

    # After reciprocal quotient every fixed direction has distinct squareclasses (t36's
    # only within-direction collisions were p<->q reciprocal duplicates).
    by_direction = defaultdict(list)
    for s in reps:
        by_direction[(s["a"], s["b"])].append(s)
    for fiber in by_direction.values():
        assert len({s["kernel"] for s in fiber}) == len(fiber)

    # Canonical even valuation is removed before evaluating the physical quartic at its
    # own canonical prime. This is the exact bridge from t47 squareclass characters to
    # t32's canonical-square-normalized four-linear symbol.
    reduced = [reduced_physical_F(s) for s in reps]
    canonical_normalization_checks = 0
    for s, Fr in zip(reps, reduced):
        assert Fr % s["ell"] != 0
        assert legendre(Fr, s["ell"]) == legendre(s["kernel"], s["ell"])
        canonical_normalization_checks += 1

    # Character rows indexed by the physical canonical split primes.
    rows = {ell: [legendre(s["kernel"], ell) for s in reps] for ell in ells}
    G = {}
    product_character_checks = 0
    for i, lam in enumerate(ells):
        for mu in ells[i:]:
            total = 0
            for idx, s in enumerate(reps):
                v = rows[lam][idx] * rows[mu][idx]
                total += v
                # Exact physical realization after removing only the state's own even
                # canonical square. For a foreign super-sqrt test prime, any divisibility
                # is odd (t44 routing), so zero behavior is preserved.
                rhs = legendre(reduced[idx], lam) * legendre(reduced[idx], mu)
                assert v == rhs
                product_character_checks += 1
            G[(lam, mu)] = total
            G[(mu, lam)] = total

    offdiag = []
    for i, lam in enumerate(ells):
        for mu in ells[i + 1:]:
            offdiag.append((abs(G[(lam, mu)]), lam, mu, G[(lam, mu)]))
    offdiag.sort(reverse=True)

    top_pairs = []
    for absG, lam, mu, signedG in offdiag[:TOP_PAIRS]:
        vals = [a * b for a, b in zip(rows[lam], rows[mu])]
        rel = Counter()
        for s, v in zip(reps, vals):
            rel[relation_key(s, lam, mu)] += v
        zero_left = sum(v == 0 for v in rows[lam])
        zero_right = sum(v == 0 for v in rows[mu])
        both_nonzero = sum(a != 0 and b != 0 for a, b in zip(rows[lam], rows[mu]))
        top_pairs.append({
            "left": lam,
            "right": mu,
            "G": signedG,
            "abs_G": absG,
            "zero_left": zero_left,
            "zero_right": zero_right,
            "both_nonzero": both_nonzero,
            "endpoint_canonical_contribution": dict(sorted(rel.items())),
            "branch_partition": partition_summary(reps, vals, lambda s: s["branch"]),
            "direction_partition": partition_summary(reps, vals, lambda s: (s["a"], s["b"])),
            "common_packet_partition": partition_summary(reps, vals, common_packet_key),
            "cover_partition": partition_summary(reps, vals, cover_key),
        })

    # Row L2 target from t47 and exact partition-Cauchy ledgers. These show whether a
    # local fixed-direction/common-packet estimate can be promoted without paying the
    # number of active cells.
    row_ledgers = []
    for lam in ells:
        actual = sum(G[(lam, mu)] ** 2 for mu in ells if mu != lam)

        dir_local = 0
        for d, fiber in by_direction.items():
            idxs = [i for i, s in enumerate(reps) if (s["a"], s["b"]) == d]
            for mu in ells:
                if mu == lam:
                    continue
                gd = sum(rows[lam][i] * rows[mu][i] for i in idxs)
                dir_local += gd * gd

        packet_groups = defaultdict(list)
        for i, s in enumerate(reps):
            packet_groups[common_packet_key(s)].append(i)
        packet_local = 0
        for idxs in packet_groups.values():
            for mu in ells:
                if mu == lam:
                    continue
                gp = sum(rows[lam][i] * rows[mu][i] for i in idxs)
                packet_local += gp * gp

        row_ledgers.append({
            "prime": lam,
            "actual_offdiag_l2": actual,
            "direction_local_l2_sum": dir_local,
            "direction_cauchy_upper": len(directions) * dir_local,
            "common_packet_local_l2_sum": packet_local,
            "common_packet_cauchy_upper": len(common_packets) * packet_local,
        })
    row_ledgers.sort(key=lambda r: (-r["actual_offdiag_l2"], r["prime"]))
    worst = row_ledgers[0]
    assert worst["actual_offdiag_l2"] == t47["centered_pair_detector"]["max_offdiagonal_squared_row_sum"]

    # Finite coherence census: large pair correlations are not explained by the state
    # canonical prime endpoints or one direction/common-core packet alone.
    endpoint_max = max(
        abs(row["endpoint_canonical_contribution"].get("state_ell=left_test", 0))
        + abs(row["endpoint_canonical_contribution"].get("state_ell=right_test", 0))
        for row in top_pairs
    )
    max_direction_cell = max(row["direction_partition"]["max_abs_cell"] for row in top_pairs)
    max_packet_cell = max(row["common_packet_partition"]["max_abs_cell"] for row in top_pairs)

    report = {
        "stage": "14-t48",
        "physical_character_bridge": {
            "test_primes": len(ells),
            "all_test_primes_split_mod4": True,
            "canonical_square_normalization_checks": canonical_normalization_checks,
            "product_character_checks": product_character_checks,
            "identity": "G_{lambda,mu}=sum_s chi_{kappa_s}(lambda)chi_{kappa_s}(mu)=sum_s chi_{lambda*mu}(F_s/ell_s^2 on visible; F_s on invisible)",
            "t32_connection": "the normalized physical symbol is the same four-linear squareclass character whose split two-prime angular completion was bounded in t32",
        },
        "fixed_direction_structure": {
            "directions": len(directions),
            "reciprocal_quotient_fixed_direction_squareclass_injective": True,
            "reason": "t36 within-direction multiplicity two is exactly the reciprocal p<->q duplication removed by t42",
        },
        "top_offdiagonal_pairs": top_pairs,
        "row_l2": {
            "worst": worst,
            "top8": row_ledgers[:8],
            "direction_partition_cells": len(directions),
            "common_packet_partition_cells": len(common_packets),
            "exact_global_vs_local_warning": "G=sum_R G_R, hence |G|^2<=#R sum_R|G_R|^2; local cancellation alone pays the number of cells unless signed aggregation is retained",
        },
        "finite_coherence": {
            "top_pair_count": len(top_pairs),
            "max_abs_endpoint_canonical_contribution_sum": endpoint_max,
            "max_abs_single_direction_cell_on_top_pairs": max_direction_cell,
            "max_abs_single_common_packet_cell_on_top_pairs": max_packet_cell,
            "largest_abs_global_G": offdiag[0][0],
            "largest_abs_global_pair": [offdiag[0][1], offdiag[0][2], offdiag[0][3]],
            "diagnosis": "large frozen correlations are diffuse across physical cells; no single endpoint-canonical, direction, or common-packet cell explains the top rows",
            "asymptotic_claim": False,
        },
        "proof_contract": {
            "t32_split_torus_angular_complete_bound_reusable": True,
            "tH13_same_modulus_product_kernel_receiver_reusable": True,
            "remaining_live_sum": "signed aggregation over divisor-coupled norm-index/common-refinement cells after the t32 angular completion",
            "sufficient_t47_target": "uniform max_lambda sum_{mu!=lambda}|G_{lambda,mu}|^2 <= H^2*P*B^-delta",
            "local_cell_bounds_without_signed_aggregation_sufficient": False,
        },
        "tH_decision": {
            "additional_tH_needed": False,
            "reason": "t48 identifies the live obstruction as the same signed common-refinement/norm-index aggregation already covered by tH12+tH13; no new adapter object appears",
            "reopen_trigger": "only if the next live arithmetic step exposes a new structured coherent-row family not representable by the existing product-kernel/common-refinement receiver",
        },
        "decision": {
            "STAGE14_T48": "COMPLETE_PHYSICAL_ROW_CORRELATION_BRIDGE_AND_DIFFUSE_COHERENCE_AUDIT",
            "T47_GRAM_IS_NORMALIZED_PHYSICAL_FOUR_LINEAR_CHARACTER_SUM": True,
            "ALL_CANONICAL_TEST_PRIMES_SPLIT": True,
            "T32_TWO_PRIME_ANGULAR_COMPLETION_REUSED": True,
            "FIXED_DIRECTION_KERNEL_INJECTIVITY_AFTER_RECIPROCAL_QUOTIENT": True,
            "TOP_FROZEN_ROW_CORRELATIONS_SINGLE_CELL_EXCEPTIONAL": False,
            "SIGNED_COMMON_REFINEMENT_AGGREGATION_REQUIRED": True,
            "UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_NEEDED": False,
            "NEXT": "Stage14-t49 keep the signed common-refinement aggregation and attack the divisor-coupled norm-index row second moment directly, using the t32 split-torus completion plus tH12/tH13 hyperbola/product-kernel machinery; do not Cauchy over direction/common-packet cells first",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
