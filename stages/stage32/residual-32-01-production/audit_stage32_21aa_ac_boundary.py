#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

from sympy import Matrix

from direct_picard_reynolds_lattice_diagnostic import (
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    load_retained,
)
from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)

EXPECTED_AA_SHA256 = "f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238"
EXPECTED_AB_SHA256 = "07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4"
EXPECTED_AC_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_PROJECTION_CLASS_COUNT = 16384
EXPECTED_FREE_SUBGROUP_ORDER = 128
EXPECTED_COSET_COUNT = 128
EXPECTED_POSITIVE_COSETS = 127
EXPECTED_ZERO_COSETS = 1
EXPECTED_MIN_POSITIVE = Fraction(1, 572)


def add_mod(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % GROUP_ORDER for x, y in zip(a, b))


def scale_mod(k: int, a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((int(k) * x) % GROUP_ORDER for x in a)


def independent_generated_subgroup(
    generators: tuple[tuple[int, ...], ...]
) -> set[tuple[int, ...]]:
    """Independent finite closure: adjoin all 0..63 multiples of each generator."""
    subgroup: set[tuple[int, ...]] = {(0,) * PICARD_RANK}
    for generator in generators:
        multiples = tuple(scale_mod(k, generator) for k in range(GROUP_ORDER))
        subgroup = {add_mod(h, multiple) for h in subgroup for multiple in multiples}
    return subgroup


def independent_penalty(
    residue: tuple[int, ...], dual_norms: tuple[Fraction, ...]
) -> Fraction:
    best = Fraction(0, 1)
    for raw, dual_norm in zip(residue, dual_norms):
        r = int(raw)
        distance = min(r, GROUP_ORDER - r)
        if distance == 0:
            continue
        if dual_norm <= 0:
            raise ValueError("positive fractional coordinate has nonpositive dual norm")
        candidate = Fraction(distance * distance, GROUP_ORDER * GROUP_ORDER) / dual_norm
        if candidate > best:
            best = candidate
    return best


def fraction_stream_sha256(values: tuple[Fraction, ...]) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{value.numerator}/{value.denominator}\n".encode())
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21aa_ac_audit_picard")
    marking = load_retained(args.marking, "s32_21aa_ac_audit_marking")
    ac = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    mapping = ac.mapping
    rank2 = mapping.rank2
    aa = mapping.penalty

    aa_sha = aa.certificate["canonical_sha256_without_this_field"]
    ab_sha = mapping.certificate["canonical_sha256_without_this_field"]
    ac_sha = ac.certificate["canonical_sha256_without_this_field"]
    if aa_sha != EXPECTED_AA_SHA256:
        raise ValueError(f"32-21aa certificate drift: {aa_sha}")
    if ab_sha != EXPECTED_AB_SHA256:
        raise ValueError(f"32-21ab certificate drift: {ab_sha}")
    if ac_sha != EXPECTED_AC_SHA256:
        raise ValueError(f"32-21ac certificate drift: {ac_sha}")

    B = Matrix(aa.fixed_image_basis)
    T = Matrix(rank2.smith_right)
    direct_map = (B * T).applyfunc(lambda z: int(z) % GROUP_ORDER)
    claimed_columns = tuple(mapping.map_columns)
    independent_columns = tuple(
        tuple(int(direct_map[i, j]) for i in range(PICARD_RANK))
        for j in range(5)
    )
    if claimed_columns != independent_columns:
        raise ValueError("independent B*T quotient-map reconstruction mismatch")

    basis_generators = tuple(
        tuple(int(B[i, j]) % GROUP_ORDER for i in range(PICARD_RANK))
        for j in range(5)
    )
    image_from_basis = independent_generated_subgroup(basis_generators)
    image_from_smith = independent_generated_subgroup(independent_columns)
    claimed_image = set(mapping.sorted_projection_residues)
    if image_from_basis != image_from_smith or image_from_smith != claimed_image:
        raise ValueError("independent full projection-image reconstruction mismatch")
    if len(claimed_image) != EXPECTED_PROJECTION_CLASS_COUNT:
        raise ValueError("projection class count drift in boundary audit")

    free_subgroup = independent_generated_subgroup(
        (independent_columns[3], independent_columns[4])
    )
    if free_subgroup != set(mapping.free_subgroup):
        raise ValueError("independent rank2 free-subgroup reconstruction mismatch")
    if len(free_subgroup) != EXPECTED_FREE_SUBGROUP_ORDER:
        raise ValueError(f"free subgroup order drift: {len(free_subgroup)}")

    remaining = set(claimed_image)
    independent_cosets: list[tuple[tuple[int, ...], set[tuple[int, ...]]]] = []
    independent_residue_to_coset: dict[tuple[int, ...], int] = {}
    while remaining:
        seed = min(remaining)
        coset = {add_mod(seed, h) for h in free_subgroup}
        if len(coset) != EXPECTED_FREE_SUBGROUP_ORDER or not coset <= claimed_image:
            raise ValueError("independent free-coset partition regression")
        canonical = min(coset)
        independent_cosets.append((canonical, coset))
        remaining.difference_update(coset)
    independent_cosets.sort(key=lambda item: item[0])
    if len(independent_cosets) != EXPECTED_COSET_COUNT:
        raise ValueError(f"free quotient coset count drift: {len(independent_cosets)}")
    if tuple(rep for rep, _ in independent_cosets) != mapping.coset_representatives:
        raise ValueError("canonical free-coset representative convention mismatch")
    for coset_id, (_, coset) in enumerate(independent_cosets):
        for residue in coset:
            independent_residue_to_coset[residue] = coset_id
    if independent_residue_to_coset != mapping.residue_to_coset_id:
        raise ValueError("residue-to-coset-id table mismatch")

    dual_norms = aa.coordinate_dual_norms
    independent_penalties = {
        residue: independent_penalty(residue, dual_norms)
        for residue in mapping.sorted_projection_residues
    }
    for residue, value in independent_penalties.items():
        if value != aa.lower_bound_from_residue(residue):
            raise ValueError("independent 32-21aa penalty formula mismatch")

    independent_coset_lbs: list[Fraction] = []
    for _, coset in independent_cosets:
        lb = min(independent_penalties[residue] for residue in coset)
        independent_coset_lbs.append(lb)
        if any(lb > independent_penalties[residue] for residue in coset):
            raise ValueError("coset minimum is not a safe memberwise lower bound")
    independent_coset_lbs_tuple = tuple(independent_coset_lbs)
    if independent_coset_lbs_tuple != ac.coset_lower_bounds:
        raise ValueError("independent coset lower-bound table mismatch")

    zero_cosets = sum(1 for value in independent_coset_lbs_tuple if value == 0)
    positive_values = tuple(value for value in independent_coset_lbs_tuple if value > 0)
    if zero_cosets != EXPECTED_ZERO_COSETS:
        raise ValueError(f"zero coset count drift: {zero_cosets}")
    if len(positive_values) != EXPECTED_POSITIVE_COSETS:
        raise ValueError(f"positive coset count drift: {len(positive_values)}")
    if min(positive_values) != EXPECTED_MIN_POSITIVE:
        raise ValueError(f"minimum positive coset bound drift: {min(positive_values)}")

    # Fresh implementation-level panel. Construct integer targets from locked
    # Smith y-coordinates via t=S^{-1}*D*y. This avoids relying on physical-row
    # enumeration while exercising the exact affine adapter. The strengthened
    # predicate may prune more, but it must never revive a slice already pruned
    # by the old exact rank2 predicate. Every returned witness is checked
    # directly against halfspaces and the rational raised threshold.
    S = Matrix(rank2.smith_left)
    Sinv = S.inv()
    D3 = Matrix.diag(*rank2.smith_diagonal_signed)
    panel_cases = 0
    strengthened_only_prunes = 0
    surviving_witness_checks = 0
    zero_coset_equivalence_checks = 0
    for locked in itertools.product((-1, 0, 1), repeat=3):
        tvec = Sinv * D3 * Matrix(locked)
        if any(value.q != 1 for value in tvec):
            raise ValueError("Smith synthetic target unexpectedly nonintegral")
        d, e, a = (int(tvec[i, 0]) for i in range(3))
        for lower in (-1, 0, 1):
            panel_cases += 1
            old_ok, _, _, old_witness = rank2.can_reach_selfsq(d, e, a, lower)
            new_ok, _, _, new_witness, lambda_coset = ac.can_reach_selfsq(
                d, e, a, lower
            )
            if not old_ok and new_ok:
                raise ValueError("strengthened anti-fixed predicate revived an old rank2 prune")
            if old_ok and not new_ok:
                strengthened_only_prunes += 1
            if lambda_coset is None:
                if new_ok:
                    raise ValueError("survivor missing quotient coset lower bound")
                continue
            if lambda_coset == 0:
                zero_coset_equivalence_checks += 1
                if old_ok != new_ok:
                    raise ValueError("zero-penalty coset did not reduce exactly to old rank2 decision")
            if new_ok:
                if new_witness is None:
                    raise ValueError("strengthened survivor missing witness")
                u, v = new_witness
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("strengthened witness has no affine origin")
                k0, k1 = rank2.kernel_columns
                z = tuple(z0[i] + u * k0[i] + v * k1[i] for i in range(5))
                if any(sum(row[j] * z[j] for j in range(5)) < 0 for row in rank2.fixed_halfspace_rows):
                    raise ValueError("strengthened witness violates a fixed halfspace")
                projected = Fraction(quad(rank2.hessian, z), rank2.certificate["objective_denominator"])
                if projected - lambda_coset < int(lower):
                    raise ValueError("strengthened witness fails direct rational threshold check")
                surviving_witness_checks += 1
            if old_ok and old_witness is None:
                raise ValueError("old rank2 survivor missing witness on audit panel")

    if zero_coset_equivalence_checks == 0:
        raise ValueError("audit panel failed to exercise zero-penalty coset equivalence")

    cert = {
        "schema": "STAGE32_21AA_AC_BOUNDARY_AUDIT_V1",
        "verdict": "PASS_STAGE32_21AA_AC_FRESH_BOUNDARY_AUDIT",
        "scope": "32-21aa anti-fixed penalty -> 32-21ab exact Smith quotient map -> 32-21ac cheap exact coset pruning predicate",
        "locked_certificates": {
            "32-21aa": aa_sha,
            "32-21ab": ab_sha,
            "32-21ac": ac_sha,
        },
        "independent_rederivation": {
            "B_times_T_mod_64_rebuilt": True,
            "basis_image_equals_smith_image": True,
            "projection_class_count": len(claimed_image),
            "free_subgroup_order": len(free_subgroup),
            "free_quotient_coset_count": len(independent_cosets),
            "all_projection_classes_partitioned_once": True,
            "all_16384_penalties_recomputed_from_dual_norm_formula": True,
            "all_coset_minima_recomputed": True,
            "zero_minimum_coset_count": zero_cosets,
            "positive_minimum_coset_count": len(positive_values),
            "minimum_positive_coset_lower_bound": [
                min(positive_values).numerator,
                min(positive_values).denominator,
            ],
            "coset_lower_bound_stream_sha256": fraction_stream_sha256(
                independent_coset_lbs_tuple
            ),
        },
        "implementation_panel": {
            "smith_locked_coordinate_values": [-1, 0, 1],
            "lower_values": [-1, 0, 1],
            "case_count": panel_cases,
            "old_rank2_false_new_true_count": 0,
            "old_true_new_false_count": strengthened_only_prunes,
            "surviving_witness_direct_checks": surviving_witness_checks,
            "zero_coset_equivalence_checks": zero_coset_equivalence_checks,
        },
        "proof_chain": {
            "aa_interface": "lambda(r) <= -q^2 for each exact Reynolds projection residue r",
            "ab_adapter": "rank2 Smith y maps exactly by r=(B*T*y) mod 64; integer u,v move r inside one 128-element subgroup coset",
            "ac_adapter": "lambda_C=min_{r in C} lambda(r), hence lambda_C<=-q^2 for every lift in the slice and x^2<=p^2-lambda_C",
            "decision": "old exact rank2 concave integer-QP exhaustion is reused with the rational threshold lower+lambda_C scaled to exact integers",
        },
        "firewalls": {
            "full178_census_run": False,
            "legacy_prefix_dfs_rearmed": False,
            "anti_fixed_59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "unknown_is_unsat": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "release": {
            "32-21aa_ac_package_audited": True,
            "32-21ad_full178_census_may_be_planned_after_checkpoint_merge": True,
            "32-21ad_armed_by_this_audit": False,
            "automatic_merge_authorized": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": cert["verdict"],
        "projection_class_count": len(claimed_image),
        "free_subgroup_order": len(free_subgroup),
        "free_quotient_coset_count": len(independent_cosets),
        "positive_minimum_coset_count": len(positive_values),
        "panel_cases": panel_cases,
        "old_true_new_false_count": strengthened_only_prunes,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
