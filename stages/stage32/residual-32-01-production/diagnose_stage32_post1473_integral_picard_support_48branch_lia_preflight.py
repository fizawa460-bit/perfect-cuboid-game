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
from diagnose_stage32_21ak_affine_2adic_membership import (
    EXPECTED_SMITH_FACTORS,
    reconstruct_translation_data,
)
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
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound

V3_CANONICAL_SHA256 = "d4c49ec32c680f6f0e7c92cd6809e3a7e9edca3ca6e061f794bec28adcd07737"


def max_abs_matrix(a: Matrix) -> int:
    return max((abs(int(v)) for v in a), default=0)


def reconstruct_witness(data, y0, S, q, model, required_support: int) -> dict:
    rank = len(q)
    qv = Matrix([int(model.eval(v, model_completion=True).as_long()) for v in q])
    uq = data["Uf"] * qv
    smith_coordinates = []
    for i in range(rank):
        diag = int(data["Df"][i, i])
        value = int(uq[i, 0])
        if value % diag:
            raise ValueError("SAT witness violates Smith image divisibility")
        smith_coordinates.append(value // diag)
    tw = data["Vf"] * Matrix(smith_coordinates)
    if data["F"] * tw != qv:
        raise ValueError("SAT witness does not reconstruct an original translation")
    if data["M"] * tw != S * qv:
        raise ValueError("SAT witness pairing translation reconstruction regression")

    pairings = tuple(
        int(y0[i, 0]) + sum(int(S[i, j]) * int(qv[j, 0]) for j in range(rank))
        for i in range(EXPECTED_ALL140_COUNT)
    )
    exceptional = pairings[-EXPECTED_EXCEPTIONAL_COUNT:]
    support = sum(1 for v in exceptional if v > 0)
    if min(pairings) < 0 or support < required_support:
        raise ValueError("SAT witness violates exact support/nonnegative preflight")
    return {
        "saturated_translation_sha256": csha([int(v) for v in qv]),
        "original_translation_sha256": csha([int(v) for v in tw]),
        "all140_pairings_sha256": csha(list(pairings)),
        "minimum_pairing": min(pairings),
        "maximum_pairing": max(pairings),
        "positive_exceptional_support": support,
        "zero_exceptional_indices": [i for i, v in enumerate(exceptional) if v == 0],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--node-preflight", type=Path, required=True)
    ap.add_argument("--picard-adapter", type=Path, required=True)
    ap.add_argument("--node-support-audit", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--branch-timeout-ms", type=int, default=8000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.branch_timeout_ms <= 0:
        raise ValueError("branch timeout must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest canonical regression")

    node_preflight = load_preflight(args.node_preflight)
    if node_preflight["canonical_sha256_without_this_field"] != EXPECTED_PREFLIGHT_SHA256:
        raise ValueError("node-support preflight regression")
    adapter_evidence = load_canonical(args.picard_adapter, EXPECTED_PICARD_ADAPTER_CANONICAL, "post-21bl Picard adapter")
    node_audit = load_canonical(args.node_support_audit, EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL, "node-support fresh audit")

    target = adapter_evidence["target"]
    for key, expected in EXPECTED_TARGET.items():
        if target.get(key) != expected:
            raise ValueError(f"representative target regression at {key}: {target.get(key)} != {expected}")
    if node_audit["verdict"]["bijective_normalization_genus1_curve_in_representative_class"] is not False:
        raise ValueError("representative node-support exclusion audit regression")

    g, d, e = int(target["genus"]), int(target["degree"]), int(target["e"])
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
    if csha(list(tuple(data["constraint_rows"]))) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak affine constraint-row regression")
    if tuple(int(v) for v in data["factors"]) != EXPECTED_SMITH_FACTORS:
        raise ValueError("21ak Smith-factor regression")
    if data["Sfinal"] * data["F"] != data["M"]:
        raise ValueError("saturated pairing-coordinate reconstruction regression")
    if data["Uf"] * data["F"] * data["Vf"] != data["Df"]:
        raise ValueError("Smith reconstruction regression")

    z = tuple(int(v) for v in target["z"])
    picard = Matrix([int(v) for v in adapter_evidence["reconstruction"]["picard_coordinates"]])
    if picard.rows != 64 or picard.cols != 1:
        raise ValueError("persisted Picard64 coordinate shape regression")
    if tuple(int(v) for v in (data["C"] * picard)) != z:
        raise ValueError("persisted Picard class does not map to locked z")

    x0 = data["x0_map"] * Matrix(z)
    translation, params = data["K"].gauss_jordan_solve(picard - x0)
    if params.rows != 0 or any(sympy.denom(v) != 1 for v in translation):
        raise ValueError("persisted Picard class lacks unique integral 21ak translation")
    translation = Matrix([int(v) for v in translation])
    if data["K"] * translation != picard - x0:
        raise ValueError("21ak affine translation reconstruction regression")

    persisted_all140 = tuple(int(v) for v in adapter_evidence["all140"]["pairings"])
    if tuple(int(v) for v in (data["adapter"].pairing_matrix * picard)) != persisted_all140:
        raise ValueError("persisted all140 pairing replay regression")
    if len(persisted_all140) != EXPECTED_ALL140_COUNT or min(persisted_all140) < 0:
        raise ValueError("known representative all140 nonnegative regression")
    known_exceptional = persisted_all140[-EXPECTED_EXCEPTIONAL_COUNT:]
    known_support = sum(v > 0 for v in known_exceptional)
    known_zero_indices = [i for i, v in enumerate(known_exceptional) if v == 0]
    if known_support != EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT or len(known_zero_indices) <= 1:
        raise ValueError("known representative exceptional support regression")

    rank = int(data["F"].cols)
    q = [Int(f"q_{j}") for j in range(rank)]
    solver = Solver()
    solver.set(timeout=args.branch_timeout_ms)

    divisibility_count = 0
    for i in range(rank):
        diag = int(data["Df"][i, i])
        if abs(diag) == 1:
            continue
        r = Int(f"smith_div_{i}")
        lhs = sum(int(data["Uf"][i, j]) * q[j] for j in range(rank))
        solver.add(lhs == diag * r)
        divisibility_count += 1
    if divisibility_count != 14:
        raise ValueError(f"expected 14 nonunit Smith divisibility constraints, got {divisibility_count}")

    y0 = data["pairing_x0_map"] * Matrix(z)
    S = data["Sfinal"]
    pairing_exprs = []
    for i in range(EXPECTED_ALL140_COUNT):
        expr = int(y0[i, 0]) + sum(int(S[i, j]) * q[j] for j in range(rank))
        pairing_exprs.append(expr)
        solver.add(expr >= 0)
    exceptional_exprs = pairing_exprs[-EXPECTED_EXCEPTIONAL_COUNT:]

    # Exact union decomposition. Under nonnegative integer pairings,
    # support >= 47 of 48 iff there exists an omitted j for which every
    # exceptional coordinate except j is >= 1. All-positive solutions are
    # included in every branch; a one-zero solution is included in its branch.
    branch_order = known_zero_indices + [i for i in range(EXPECTED_EXCEPTIONAL_COUNT) if i not in known_zero_indices]
    branch_results = []
    aggregate_status = "UNSAT"
    aggregate_witness = None
    sat_branch = None
    for omitted in branch_order:
        solver.push()
        for i, expr in enumerate(exceptional_exprs):
            if i != omitted:
                solver.add(expr >= 1)
        result = solver.check()
        record = {"omitted_exceptional_index": omitted}
        if result == sat:
            aggregate_status = "SAT"
            sat_branch = omitted
            aggregate_witness = reconstruct_witness(data, y0, S, q, solver.model(), required_support)
            record["status"] = "SAT"
            branch_results.append(record)
            solver.pop()
            break
        if result == unsat:
            record["status"] = "UNSAT"
        elif result == unknown:
            record["status"] = "UNKNOWN"
            record["reason"] = solver.reason_unknown()
            aggregate_status = "UNKNOWN"
        else:
            solver.pop()
            raise ValueError(f"unexpected solver status: {result}")
        branch_results.append(record)
        solver.pop()

    tested = len(branch_results)
    sat_count = sum(r["status"] == "SAT" for r in branch_results)
    unsat_count = sum(r["status"] == "UNSAT" for r in branch_results)
    unknown_count = sum(r["status"] == "UNKNOWN" for r in branch_results)
    if aggregate_status == "UNSAT" and (tested != EXPECTED_EXCEPTIONAL_COUNT or unsat_count != EXPECTED_EXCEPTIONAL_COUNT):
        raise ValueError("UNSAT aggregate requires all 48 branches proved UNSAT")
    if aggregate_status == "SAT" and sat_count != 1:
        raise ValueError("SAT aggregate requires a recorded SAT branch")
    if aggregate_status == "UNKNOWN" and sat_count != 0:
        raise ValueError("UNKNOWN aggregate cannot contain SAT")

    nonunit_factors = [int(v) for v in data["factors"] if int(v) != 1]
    payload = {
        "schema": "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_48_BRANCH_SATURATED_LIA_PREFLIGHT_V4",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_EXACT_LINEAR_SUPPORT_FEASIBILITY",
        "mode": "ONE_LOCKED_PROJECTION_EXACT_21AK_SATURATED_PAIRING_LATTICE_PLUS_48_OMITTED_ZERO_LINEAR_BRANCHES",
        "source_locks": {
            "main_merge_base": "4a08b3636b342b682d2a257aa157e146e86ba302",
            "v3_unknown_canonical_sha256": V3_CANONICAL_SHA256,
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
            "known_exact_picard_zero_exceptional_indices": known_zero_indices,
            "known_exact_picard_class_excluded_by_refined_support_bound": True,
            "known_exact_picard_21ak_translation_sha256": csha([int(v) for v in translation]),
        },
        "saturated_pairing_lattice": {
            "integer_rank": rank,
            "exact_identity_M_equals_Sfinal_times_F": True,
            "smith_factor_multiplicities": {
                "1": list(data["factors"]).count(1),
                "2": list(data["factors"]).count(2),
                "4": list(data["factors"]).count(4),
                "8": list(data["factors"]).count(8),
            },
            "nonunit_divisibility_constraint_count": divisibility_count,
            "maximum_nonunit_modulus": max(nonunit_factors),
            "original_M_max_abs_coefficient": max_abs_matrix(data["M"]),
            "saturated_Sfinal_max_abs_coefficient": max_abs_matrix(S),
            "exact_same_integer_fiber": True,
        },
        "exact_48_branch_linearization": {
            "all_exceptional_pairings_nonnegative_integer": True,
            "required_positive_exceptional_support": required_support,
            "equivalence": "support>=47_of_48 iff union_j(all_exceptional_i_except_j>=1, exceptional_j>=0)",
            "branch_count": EXPECTED_EXCEPTIONAL_COUNT,
            "positive_constraints_per_branch": EXPECTED_EXCEPTIONAL_COUNT - 1,
            "all_positive_case_included": True,
            "boolean_cardinality_removed": True,
            "pairwise_1128_constraints_removed": True,
        },
        "branch_preflight": {
            "aggregate_status": aggregate_status,
            "z3_version": get_version_string(),
            "branch_timeout_ms": args.branch_timeout_ms,
            "branch_order": branch_order,
            "branches_tested": tested,
            "sat_count": sat_count,
            "unsat_count": unsat_count,
            "unknown_count": unknown_count,
            "sat_branch_omitted_exceptional_index": sat_branch,
            "results": branch_results,
            "witness": aggregate_witness,
            "self_intersection_threshold_enforced": False,
            "sat_is_only_necessary_condition_survival": True,
            "unsat_would_reject_only_this_fixed_z_for_bijective_normalization_branch": True,
        },
        "firewalls": {
            "representative_known_class_exclusion_remains_audited": True,
            "fixed_z_affine_fiber_closed": aggregate_status == "UNSAT",
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
        "verdict": "PASS_STAGE32_POST1473_FIXED_Z_48_BRANCH_LINEAR_SUPPORT_PREFLIGHT",
        "aggregate_status": aggregate_status,
        "branches_tested": tested,
        "sat_count": sat_count,
        "unsat_count": unsat_count,
        "unknown_count": unknown_count,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
