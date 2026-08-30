#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

from sympy import Matrix

from direct_picard_reynolds_lattice_diagnostic import GROUP_ORDER, PICARD_RANK, csha, load_retained
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound
from direct_picard_reynolds_rank2_integer_qp import quad

EXPECTED_AA_SHA256 = "f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238"
EXPECTED_AB_SHA256 = "07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4"
EXPECTED_AC_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_PROJECTION_CLASS_COUNT = 16384
EXPECTED_FREE_SUBGROUP_ORDER = 128
EXPECTED_COSET_COUNT = 128
EXPECTED_POSITIVE_COSETS = 127
EXPECTED_MIN_POSITIVE = Fraction(1, 572)


def add_mod(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % GROUP_ORDER for x, y in zip(a, b))


def scale_mod(k: int, a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((k * x) % GROUP_ORDER for x in a)


def independent_generated_subgroup(generators: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    subgroup: set[tuple[int, ...]] = {(0,) * PICARD_RANK}
    for generator in generators:
        multiples = tuple(scale_mod(k, generator) for k in range(GROUP_ORDER))
        subgroup = {add_mod(h, m) for h in subgroup for m in multiples}
    return subgroup


def independent_penalty(residue: tuple[int, ...], dual_norms: tuple[Fraction, ...]) -> Fraction:
    best = Fraction(0, 1)
    for raw, dual_norm in zip(residue, dual_norms):
        distance = min(int(raw), GROUP_ORDER - int(raw))
        if not distance:
            continue
        if dual_norm <= 0:
            raise ValueError("nonpositive dual norm on fractional coordinate")
        best = max(best, Fraction(distance * distance, GROUP_ORDER * GROUP_ORDER) / dual_norm)
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
    if (aa_sha, ab_sha, ac_sha) != (EXPECTED_AA_SHA256, EXPECTED_AB_SHA256, EXPECTED_AC_SHA256):
        raise ValueError(f"locked certificate drift: {(aa_sha, ab_sha, ac_sha)}")

    B = Matrix(aa.fixed_image_basis)
    T = Matrix(rank2.smith_right)
    direct_map = (B * T).applyfunc(lambda z: int(z) % GROUP_ORDER)
    smith_columns = tuple(tuple(int(direct_map[i, j]) for i in range(PICARD_RANK)) for j in range(5))
    if smith_columns != mapping.map_columns:
        raise ValueError("independent B*T mod64 map mismatch")

    basis_columns = tuple(
        tuple(int(B[i, j]) % GROUP_ORDER for i in range(PICARD_RANK)) for j in range(5)
    )
    basis_image = independent_generated_subgroup(basis_columns)
    smith_image = independent_generated_subgroup(smith_columns)
    claimed_image = set(mapping.sorted_projection_residues)
    if basis_image != smith_image or smith_image != claimed_image:
        raise ValueError("independent full projection-image mismatch")
    if len(claimed_image) != EXPECTED_PROJECTION_CLASS_COUNT:
        raise ValueError("projection class count drift")

    free_subgroup = independent_generated_subgroup((smith_columns[3], smith_columns[4]))
    if free_subgroup != set(mapping.free_subgroup) or len(free_subgroup) != EXPECTED_FREE_SUBGROUP_ORDER:
        raise ValueError("independent free-subgroup mismatch")

    remaining = set(claimed_image)
    cosets: list[tuple[tuple[int, ...], set[tuple[int, ...]]]] = []
    while remaining:
        seed = min(remaining)
        coset = {add_mod(seed, h) for h in free_subgroup}
        if len(coset) != EXPECTED_FREE_SUBGROUP_ORDER or not coset <= claimed_image:
            raise ValueError("free-coset partition regression")
        cosets.append((min(coset), coset))
        remaining.difference_update(coset)
    cosets.sort(key=lambda x: x[0])
    if len(cosets) != EXPECTED_COSET_COUNT:
        raise ValueError("free quotient coset count drift")
    if tuple(rep for rep, _ in cosets) != mapping.coset_representatives:
        raise ValueError("canonical coset representative mismatch")
    independent_residue_to_coset = {
        residue: coset_id
        for coset_id, (_, coset) in enumerate(cosets)
        for residue in coset
    }
    if independent_residue_to_coset != mapping.residue_to_coset_id:
        raise ValueError("residue-to-coset table mismatch")

    penalties = {
        residue: independent_penalty(residue, aa.coordinate_dual_norms)
        for residue in mapping.sorted_projection_residues
    }
    for residue, value in penalties.items():
        if value != aa.lower_bound_from_residue(residue):
            raise ValueError("independent 32-21aa penalty mismatch")
    coset_lbs = tuple(min(penalties[r] for r in coset) for _, coset in cosets)
    if coset_lbs != ac.coset_lower_bounds:
        raise ValueError("independent 32-21ac coset-bound table mismatch")
    if any(coset_lbs[mapping.residue_to_coset_id[r]] > penalties[r] for r in penalties):
        raise ValueError("coset lower bound is not memberwise safe")
    zero_cosets = sum(value == 0 for value in coset_lbs)
    positive = tuple(value for value in coset_lbs if value > 0)
    if zero_cosets != 1 or len(positive) != EXPECTED_POSITIVE_COSETS or min(positive) != EXPECTED_MIN_POSITIVE:
        raise ValueError("coset lower-bound population/value drift")

    # Fresh implementation panel from synthetic locked Smith coordinates.
    S = Matrix(rank2.smith_left)
    Sinv = S.inv()
    D3 = Matrix.diag(*rank2.smith_diagonal_signed)
    panel_cases = 0
    old_true_new_false = 0
    witness_checks = 0
    zero_coset_equivalence = 0
    for locked in itertools.product((-1, 0, 1), repeat=3):
        tvec = Sinv * D3 * Matrix(locked)
        if any(value.q != 1 for value in tvec):
            raise ValueError("synthetic Smith target nonintegral")
        d, e, a = (int(tvec[i, 0]) for i in range(3))
        for lower in (-1, 0, 1):
            panel_cases += 1
            old_ok, _, _, old_witness = rank2.can_reach_selfsq(d, e, a, lower)
            new_ok, _, _, new_witness, lambda_coset = ac.can_reach_selfsq(d, e, a, lower)
            if not old_ok and new_ok:
                raise ValueError("strengthened predicate revived an old rank2 prune")
            if old_ok and not new_ok:
                old_true_new_false += 1
            if lambda_coset is None:
                if new_ok:
                    raise ValueError("survivor missing coset lower bound")
                continue
            if lambda_coset == 0:
                zero_coset_equivalence += 1
                if old_ok != new_ok:
                    raise ValueError("zero-penalty coset differs from old rank2 decision")
            if new_ok:
                if new_witness is None:
                    raise ValueError("new survivor missing witness")
                u, v = new_witness
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("new witness missing affine origin")
                k0, k1 = rank2.kernel_columns
                z = tuple(z0[i] + u * k0[i] + v * k1[i] for i in range(5))
                if any(sum(row[j] * z[j] for j in range(5)) < 0 for row in rank2.fixed_halfspace_rows):
                    raise ValueError("new witness violates fixed halfspace")
                projected = Fraction(quad(rank2.hessian, z), rank2.certificate["objective_denominator"])
                if projected - lambda_coset < lower:
                    raise ValueError("new witness fails direct raised-threshold check")
                witness_checks += 1
            if old_ok and old_witness is None:
                raise ValueError("old rank2 survivor missing witness")
    if zero_coset_equivalence == 0:
        raise ValueError("panel did not exercise zero-penalty coset")

    cert = {
        "schema": "STAGE32_21AA_AC_BOUNDARY_AUDIT_V2",
        "verdict": "PASS_STAGE32_21AA_AC_FRESH_BOUNDARY_AUDIT",
        "scope": "32-21aa anti-fixed penalty -> 32-21ab exact Smith quotient map -> 32-21ac cheap exact coset pruning predicate",
        "locked_certificates": {"32-21aa": aa_sha, "32-21ab": ab_sha, "32-21ac": ac_sha},
        "independent_rederivation": {
            "B_times_T_mod_64_rebuilt": True,
            "basis_image_equals_smith_image": True,
            "projection_class_count": len(claimed_image),
            "free_subgroup_order": len(free_subgroup),
            "free_quotient_coset_count": len(cosets),
            "all_16384_penalties_recomputed": True,
            "all_coset_minima_recomputed": True,
            "zero_minimum_coset_count": zero_cosets,
            "positive_minimum_coset_count": len(positive),
            "minimum_positive_coset_lower_bound": [min(positive).numerator, min(positive).denominator],
            "coset_lower_bound_stream_sha256": fraction_stream_sha256(coset_lbs),
        },
        "implementation_panel": {
            "case_count": panel_cases,
            "old_rank2_false_new_true_count": 0,
            "old_true_new_false_count": old_true_new_false,
            "surviving_witness_direct_checks": witness_checks,
            "zero_coset_equivalence_checks": zero_coset_equivalence,
        },
        "proof_chain": {
            "aa": "lambda(r)<=-q^2 for every exact Reynolds projection residue",
            "ab": "r=(B*T*y) mod64 and integer u,v move inside one exact 128-element subgroup coset",
            "ac": "lambda_C=min_C lambda(r), so x^2<=p^2-lambda_C; the exact rank2 integer QP is solved against lower+lambda_C after integer scaling",
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
            "32-21ad_may_be_planned_after_checkpoint_merge": True,
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
        "free_quotient_coset_count": len(cosets),
        "positive_minimum_coset_count": len(positive),
        "panel_cases": panel_cases,
        "old_true_new_false_count": old_true_new_false,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
