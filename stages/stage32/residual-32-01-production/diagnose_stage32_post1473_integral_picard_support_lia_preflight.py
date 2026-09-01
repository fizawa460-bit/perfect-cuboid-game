#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, Solver, get_version_string, sat, unknown, unsat

from build_stage32_post21bl_full178_node_mass_census import (
    EXPECTED_AC_CERTIFICATE_SHA256,
    EXPECTED_MANIFEST_SHA256,
    EXPECTED_PREFLIGHT_SHA256,
    ceil_div,
    load_module_payload,
    load_preflight,
)
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_post1473_integral_picard_support_preflight import (
    EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
    EXPECTED_ALL140_COUNT,
    EXPECTED_EXCEPTIONAL_COUNT,
    EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT,
    EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
    EXPECTED_PICARD_ADAPTER_CANONICAL,
    EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT,
    EXPECTED_TARGET,
    load_canonical,
)
from direct_picard_reynolds_lattice_diagnostic import csha
from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--node-preflight", type=Path, required=True)
    ap.add_argument("--picard-adapter", type=Path, required=True)
    ap.add_argument("--node-support-audit", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=30000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest canonical regression")

    node_preflight = load_preflight(args.node_preflight)
    if node_preflight["canonical_sha256_without_this_field"] != EXPECTED_PREFLIGHT_SHA256:
        raise ValueError("node-support preflight regression")

    adapter_evidence = load_canonical(
        args.picard_adapter,
        EXPECTED_PICARD_ADAPTER_CANONICAL,
        "post-21bl Picard adapter",
    )
    node_audit = load_canonical(
        args.node_support_audit,
        EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
        "node-support fresh audit",
    )

    target = adapter_evidence["target"]
    for key, expected in EXPECTED_TARGET.items():
        if target.get(key) != expected:
            raise ValueError(f"representative target regression at {key}: {target.get(key)} != {expected}")
    if node_audit["verdict"]["bijective_normalization_genus1_curve_in_representative_class"] is not False:
        raise ValueError("representative node-support exclusion audit regression")

    g = int(target["genus"])
    d = int(target["degree"])
    e = int(target["e"])
    required_support = ceil_div(d - 16 * g + 16, 4)
    if required_support != EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT:
        raise ValueError("required exceptional support regression")
    if e < required_support:
        raise ValueError("known representative unexpectedly fails the cheap e lower bound")

    bundle = load_module_payload(args.retained, "stage32_post1473_support_picard")
    marking = load_module_payload(args.marking, "stage32_post1473_support_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("audited 32-21ac evaluator certificate regression")

    data = reconstruct_translation_data(marking, bundle)
    constraint_rows = tuple(data["constraint_rows"])
    if csha(list(constraint_rows)) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak affine constraint-row regression")

    z = tuple(int(v) for v in target["z"])
    picard = Matrix([int(v) for v in adapter_evidence["reconstruction"]["picard_coordinates"]])
    if picard.rows != 64 or picard.cols != 1:
        raise ValueError("persisted Picard64 coordinate shape regression")

    C = data["C"]
    if tuple(int(v) for v in (C * picard)) != z:
        raise ValueError("persisted Picard class does not map to the locked 5D projection z")

    x0 = data["x0_map"] * Matrix(z)
    delta = picard - x0
    translation, params = data["K"].gauss_jordan_solve(delta)
    if params.rows != 0:
        raise ValueError("fixed-projection translation unexpectedly non-unique")
    if any(sympy.denom(v) != 1 for v in translation):
        raise ValueError("persisted Picard class requires nonintegral 21ak translation coordinates")
    translation = Matrix([int(v) for v in translation])
    if data["K"] * translation != delta:
        raise ValueError("21ak affine translation reconstruction regression")

    persisted_all140 = tuple(int(v) for v in adapter_evidence["all140"]["pairings"])
    all140 = data["adapter"].pairing_matrix * picard
    if tuple(int(v) for v in all140) != persisted_all140:
        raise ValueError("persisted all140 pairing replay regression")
    if len(persisted_all140) != EXPECTED_ALL140_COUNT or min(persisted_all140) < 0:
        raise ValueError("known representative all140 nonnegative regression")

    exceptional = persisted_all140[-EXPECTED_EXCEPTIONAL_COUNT:]
    known_support = sum(1 for v in exceptional if v > 0)
    known_zero_count = sum(1 for v in exceptional if v == 0)
    if known_support != EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT:
        raise ValueError("known representative exceptional support regression")
    if known_support >= required_support or known_zero_count <= 1:
        raise ValueError("known representative no longer violates refined node-support bound")

    selected_curve_indices = tuple(int(v) for v in data["pivot_rows"])
    selected_pairings = tuple(persisted_all140[i] for i in selected_curve_indices)
    for row in constraint_rows:
        modulus = int(row["modulus"])
        lhs = sum(
            int(row["selected_pairing_coefficients"][j]) * selected_pairings[j]
            for j in range(len(selected_pairings))
        )
        offset = sum(
            int(row["projection_z_offset_coefficients"][k]) * z[k]
            for k in range(len(z))
        )
        if (lhs - offset) % modulus:
            raise ValueError("known exact Picard class violates published 21ak affine congruence")

    # Exact pure-LIA linearization.  Because all exceptional pairings are constrained
    # to be nonnegative integers, requiring at least 47 of 48 to be positive is
    # exactly equivalent to allowing at most one zero.  The latter is equivalent
    # to y_i + y_j >= 1 for every distinct exceptional pair.  This removes the
    # previous Boolean/cardinality If layer without changing the feasible set.
    t = [Int(f"t_{j}") for j in range(data["K"].cols)]
    y0 = data["pairing_x0_map"] * Matrix(z)
    M = data["M"]
    solver = Solver()
    solver.set(timeout=args.solver_timeout_ms)
    pairing_exprs = []
    for i in range(EXPECTED_ALL140_COUNT):
        expr = int(y0[i, 0]) + sum(int(M[i, j]) * t[j] for j in range(M.cols))
        pairing_exprs.append(expr)
        solver.add(expr >= 0)

    exceptional_exprs = pairing_exprs[-EXPECTED_EXCEPTIONAL_COUNT:]
    pairwise_constraint_count = 0
    for i in range(EXPECTED_EXCEPTIONAL_COUNT):
        for j in range(i + 1, EXPECTED_EXCEPTIONAL_COUNT):
            solver.add(exceptional_exprs[i] + exceptional_exprs[j] >= 1)
            pairwise_constraint_count += 1
    expected_pairwise_count = EXPECTED_EXCEPTIONAL_COUNT * (EXPECTED_EXCEPTIONAL_COUNT - 1) // 2
    if pairwise_constraint_count != expected_pairwise_count:
        raise ValueError("pairwise support linearization count regression")

    result = solver.check()
    fiber_status = "UNKNOWN"
    fiber_witness = None
    unknown_reason = None
    if result == sat:
        fiber_status = "SAT"
        m = solver.model()
        tw = tuple(int(m.eval(v, model_completion=True).as_long()) for v in t)
        pairings = tuple(
            int(y0[i, 0]) + sum(int(M[i, j]) * tw[j] for j in range(M.cols))
            for i in range(EXPECTED_ALL140_COUNT)
        )
        support = sum(1 for v in pairings[-EXPECTED_EXCEPTIONAL_COUNT:] if v > 0)
        if min(pairings) < 0 or support < required_support:
            raise ValueError("SAT witness violates exact support/nonnegative preflight")
        fiber_witness = {
            "translation_sha256": csha(list(tw)),
            "all140_pairings_sha256": csha(list(pairings)),
            "minimum_pairing": min(pairings),
            "maximum_pairing": max(pairings),
            "positive_exceptional_support": support,
        }
    elif result == unsat:
        fiber_status = "UNSAT"
    elif result == unknown:
        fiber_status = "UNKNOWN"
        unknown_reason = solver.reason_unknown()
    else:
        raise ValueError(f"unexpected solver status: {result}")

    payload = {
        "schema": "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_LIA_PREFLIGHT_V2",
        "stage": 32,
        "leaf": "POST1473_INTEGRAL_PICARD_SUPPORT_LIA_PREFLIGHT",
        "mode": "ONE_LOCKED_PROJECTION_EXACT_21AK_AFFINE_FIBER_PLUS_ALL140_NONNEGATIVITY_PLUS_EXACT_PAIRWISE_LIA_SUPPORT_LINEARIZATION",
        "source_locks": {
            "main_merge_base": "4a08b3636b342b682d2a257aa157e146e86ba302",
            "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
            "node_support_preflight_canonical_sha256": EXPECTED_PREFLIGHT_SHA256,
            "picard_adapter_canonical_sha256": EXPECTED_PICARD_ADAPTER_CANONICAL,
            "node_support_audit_canonical_sha256": EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
            "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
            "affine_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        },
        "locked_projection": {
            **EXPECTED_TARGET,
            "node_mass_cheap_required_support_lower_bound": required_support,
            "known_exact_picard_positive_exceptional_support": known_support,
            "known_exact_picard_zero_exceptional_count": known_zero_count,
            "known_exact_picard_class_excluded_by_refined_support_bound": True,
            "known_exact_picard_maps_to_21ak_projection": True,
            "known_exact_picard_has_integral_21ak_translation": True,
            "known_exact_picard_21ak_translation_sha256": csha([int(v) for v in translation]),
        },
        "exact_support_linearization": {
            "all_exceptional_pairings_nonnegative_integer": True,
            "required_positive_exceptional_support": required_support,
            "equivalence": "support>=47_of_48 iff at_most_one_zero iff every_distinct_pair_sum>=1",
            "boolean_cardinality_removed": True,
            "pairwise_linear_constraint_count": pairwise_constraint_count,
        },
        "affine_fiber_support_preflight": {
            "status": fiber_status,
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "solver_unknown_reason": unknown_reason,
            "integer_translation_rank": int(data["K"].cols),
            "all140_nonnegative_enforced": True,
            "exceptional_pairing_count": EXPECTED_EXCEPTIONAL_COUNT,
            "required_positive_exceptional_support": required_support,
            "positive_means_integer_pairing_at_least_one": True,
            "self_intersection_threshold_enforced": False,
            "fiber_sat_is_only_necessary_condition_survival": True,
            "fiber_unsat_would_reject_this_fixed_z_for_bijective_normalization_branch": True,
            "witness": fiber_witness,
        },
        "firewalls": {
            "representative_known_class_exclusion_remains_audited": True,
            "fixed_z_affine_fiber_closed": fiber_status == "UNSAT",
            "full178_integral_picard_closed": False,
            "full178_geometric_closed": False,
            "multibranch_closed": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "unknown_is_not_unsat": True,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_LIA_PREFLIGHT",
        "known_class_support": known_support,
        "required_support": required_support,
        "fixed_z_affine_fiber_status": fiber_status,
        "pairwise_linear_constraint_count": pairwise_constraint_count,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
