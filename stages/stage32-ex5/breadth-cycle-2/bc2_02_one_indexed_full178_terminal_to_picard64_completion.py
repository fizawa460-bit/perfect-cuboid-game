#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_indexer import CompressedTerminalIndexer
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from run_full178_prefix_work_unit import KNOWN_LABEL_ORDER

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_V1"
ROW_ID = "g1-d008"
GENUS = 1
DEGREE = 8
EXCEPTIONAL_MASS = 4
TERMINAL_RANK = 0
PICARD_RANK = 64
ALL140_COUNT = 140
ANTI_RANK = 59
EXPECTED_ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_canonical_json(path: Path) -> tuple[dict, str]:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    if not isinstance(claimed, str):
        raise ValueError(f"missing canonical hash: {path}")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    if csha(body) != claimed:
        raise ValueError(f"canonical hash regression: {path}")
    return raw, claimed


def parse_manifest_rows(manifest: dict) -> set[str]:
    rows: set[str] = set()
    for ids in manifest.get("m_class_rows", {}).values():
        rows.update(str(v) for v in ids)
    return rows


def linear_expr(coeffs, variables):
    return sum(int(coeffs[j]) * variables[j] for j in range(len(variables)))


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=60000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest, manifest_canonical = load_canonical_json(args.manifest)
    rows = parse_manifest_rows(manifest)
    if ROW_ID not in rows or len(rows) != 178:
        raise ValueError("FULL178 manifest row population regression")

    checkpoint, checkpoint_canonical = load_canonical_json(args.prefix_checkpoint)
    indexed = checkpoint["indexed_reparameterization"]
    if indexed["random_access_unrank"] is not True or indexed["inverse_rank"] is not True:
        raise ValueError("compressed terminal random-access contract regression")
    if indexed["full_terminal_materialization_required"] is not False:
        raise ValueError("compressed terminal materialization firewall regression")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")
    if list(KNOWN_LABEL_ORDER) != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("runtime pairing-prefix label-order regression")

    adapter_preflight, adapter_preflight_canonical = load_canonical_json(args.adapter_preflight)
    if adapter_preflight["next_exact_unit"]["id"] != "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE":
        raise ValueError("BC2-02 preflight next-unit regression")
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct terminal-index to z shortcut became authorized")

    emin = 8 if GENUS == 0 else 4
    emax = (19 * DEGREE) // 5
    if not emin <= EXCEPTIONAL_MASS <= emax:
        raise ValueError("representative stratum outside audited FULL178 e range")

    indexer = CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    if indexer.terminal_count <= TERMINAL_RANK:
        raise ValueError("representative compressed terminal rank outside family")
    terminal = tuple(int(v) for v in indexer.unrank(TERMINAL_RANK))
    if indexer.rank(terminal) != TERMINAL_RANK:
        raise ValueError("compressed terminal rank/unrank replay regression")

    bundle = load_retained(args.retained, "s32ex5_bc2_02_indexed_picard")
    marking = load_retained(args.marking, "s32ex5_bc2_02_indexed_marking")
    data = reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    if adapter.pairing_matrix.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")
    if data["C"].shape != (5, PICARD_RANK) or data["K"].shape != (PICARD_RANK, ANTI_RANK):
        raise ValueError("Reynolds projection/kernel shape regression")

    # Exact generic completion interface.  This deliberately uses only the
    # source-locked FULL178 terminal values, the exact (d,e) Picard slice and
    # all-140 nonnegativity.  No 21az r50/r55/r27 prism or later chain band is
    # imported here.
    xvars = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)
    pairing_exprs = []
    for i in range(ALL140_COUNT):
        expr = linear_expr(adapter.pairing_matrix.row(i), xvars)
        pairing_exprs.append(expr)
        solver.add(expr >= 0)

    degree_expr = linear_expr(bridge.degree_functional, xvars)
    exceptional_mass_expr = linear_expr(bridge.exceptional_mass_functional, xvars)
    solver.add(degree_expr == DEGREE)
    solver.add(exceptional_mass_expr == EXCEPTIONAL_MASS)

    terminal_constraints = []
    for label, value in zip(EXPECTED_ASSIGNMENT_ORDER, terminal):
        all140_index = int(label) - 1
        solver.add(pairing_exprs[all140_index] == int(value))
        terminal_constraints.append({
            "known_label_1based": int(label),
            "all140_index_0based": all140_index,
            "pairing": int(value),
        })

    result = solver.check()
    result_status = "UNKNOWN"
    witness_r_reduced = None
    completion = None
    target = {
        "row_id": ROW_ID,
        "genus": GENUS,
        "degree": DEGREE,
        "e": EXCEPTIONAL_MASS,
        "terminal_rank": TERMINAL_RANK,
        "terminal_pairings": list(terminal),
    }

    if result == sat:
        result_status = "SAT"
        model = solver.model()
        x = Matrix([int(model.eval(v, model_completion=True).as_long()) for v in xvars])
        if x.shape != (PICARD_RANK, 1):
            raise ValueError("Picard64 witness shape regression")
        pairings = adapter.pairing_matrix * x
        pairing_values = vector_int(pairings)
        if min(pairing_values) < 0:
            raise ValueError("SAT witness violates all140 nonnegativity")
        for item in terminal_constraints:
            if pairing_values[item["all140_index_0based"]] != item["pairing"]:
                raise ValueError("SAT witness violates indexed terminal pairing")

        d_actual = int(Matrix([bridge.degree_functional]) * x)[0]
        e_actual = int(Matrix([bridge.exceptional_mass_functional]) * x)[0]
        a_actual = int(Matrix([bridge.first_normal_half_functional]) * x)[0]
        if (d_actual, e_actual) != (DEGREE, EXCEPTIONAL_MASS):
            raise ValueError("SAT witness violates exact d/e slice")
        if sum(pairing_values[92:140]) != EXCEPTIONAL_MASS:
            raise ValueError("SAT witness exceptional-mass replay regression")

        z = data["C"] * x
        z_values = vector_int(z)
        if data["C"] * x != z:
            raise ValueError("rank-5 projection replay regression")
        x0 = data["x0_map"] * z
        delta = x - x0
        original_t, params = data["K"].gauss_jordan_solve(delta)
        if params.rows != 0:
            raise ValueError("anti-fixed translation unexpectedly non-unique")
        if any(sympy.denom(v) != 1 for v in original_t):
            raise ValueError("Picard64 completion does not have integral 59D translation")
        original_t = Matrix([int(v) for v in original_t])
        if data["K"] * original_t != delta:
            raise ValueError("59D translation reconstruction regression")

        M = data["M"]
        pivots = tuple(int(v) for v in data["pivot_rows"])
        selected_M = M.extract(list(pivots), list(range(ANTI_RANK)))
        reduced_rows, Trow = selected_M.T.lll_transform()
        if reduced_rows != Trow * selected_M.T:
            raise ValueError("LLL reduced-coordinate transform regression")
        U = Trow.T
        if abs(int(U.det())) != 1:
            raise ValueError("reduced-coordinate transform is not unimodular")
        reduced_t = U.inv() * original_t
        if any(sympy.denom(v) != 1 for v in reduced_t):
            raise ValueError("unimodular reduced translation became nonintegral")
        reduced_t = Matrix([int(v) for v in reduced_t])
        witness_r_reduced = vector_int(reduced_t)
        if len(witness_r_reduced) != ANTI_RANK:
            raise ValueError("reduced 59D witness length regression")
        if x0 + data["K"] * U * reduced_t != x:
            raise ValueError("reduced 59D witness does not reconstruct Picard64 completion")

        gram = Matrix(bundle["picard_gram_64x64"])
        raw_selfsq = (x.T * gram * x)[0, 0]
        if sympy.denom(raw_selfsq) != 1:
            raise ValueError("Picard self-intersection became nonintegral")
        selfsq = int(raw_selfsq)
        lower = -DEGREE - 2 + 2 * GENUS
        selfsq_pass = selfsq >= lower
        required_support = math.ceil((DEGREE - 16 * GENUS + 16) / 4)
        exceptional_support = sum(1 for value in pairing_values[92:140] if value > 0)

        target.update({"a": a_actual, "z": z_values})
        completion = {
            "picard_coordinates": vector_int(x),
            "picard_coordinates_sha256": csha(vector_int(x)),
            "all140_pairings": pairing_values,
            "all140_pairings_sha256": csha(pairing_values),
            "all140_nonnegative": True,
            "degree": d_actual,
            "exceptional_mass": e_actual,
            "first_normal_half_a": a_actual,
            "projection_z": z_values,
            "projection_z_equals_C_times_picard": True,
            "original_59d_translation_sha256": csha(vector_int(original_t)),
            "reduced_59d_translation_sha256": csha(witness_r_reduced),
            "reduced_59d_reconstructs_same_picard64": True,
            "self_intersection": selfsq,
            "project_native_self_intersection_lower_formula": "-d-2+2g",
            "project_native_self_intersection_lower_bound": lower,
            "passes_project_native_self_intersection_lower_bound": selfsq_pass,
            "positive_exceptional_support": exceptional_support,
            "bijective_node_support_required_lower_bound": required_support,
            "passes_bijective_node_support_lower_bound": exceptional_support >= required_support,
        }
    elif result == unsat:
        result_status = "UNSAT"
    elif result == unknown:
        result_status = "UNKNOWN"
    else:
        raise ValueError(f"unexpected Z3 status: {result}")

    historical_preflight = RESIDUAL / "diagnose_stage32_post1473_integral_picard_support_preflight.py"
    historical_selfsq = RESIDUAL / "diagnose_stage32_post1473_integral_picard_support_selfsq_preflight.py"
    source_locks = {
        "manifest": str(args.manifest),
        "manifest_canonical_sha256": manifest_canonical,
        "prefix_checkpoint": str(args.prefix_checkpoint),
        "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
        "adapter_preflight": str(args.adapter_preflight),
        "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
        "compressed_terminal_indexer_raw_sha256": raw_sha256(RESIDUAL / "compressed_terminal_indexer.py"),
        "historical_integral_picard_support_preflight_raw_sha256": raw_sha256(historical_preflight),
        "historical_self_intersection_preflight_raw_sha256": raw_sha256(historical_selfsq),
        "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
        "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
    }

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE",
        "status": (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
            if result_status == "SAT"
            else f"PASS_BOUNDED_PROTOTYPE_{result_status}_NO_COMPLETION_CREDIT"
        ),
        "source_locks": source_locks,
        "indexed_terminal": {
            "row_id": ROW_ID,
            "genus": GENUS,
            "degree": DEGREE,
            "e": EXCEPTIONAL_MASS,
            "terminal_rank": TERMINAL_RANK,
            "terminal_count_in_stratum": int(indexer.terminal_count),
            "rank_unrank_replay_exact": True,
            "assignment_order_known_labels_1based": EXPECTED_ASSIGNMENT_ORDER,
            "pairings": list(terminal),
            "constraints": terminal_constraints,
        },
        "exact_completion_problem": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "picard_integer_variable_count": PICARD_RANK,
            "all140_pairing_nonnegativity_enforced": True,
            "degree_equality_enforced": True,
            "exceptional_mass_equality_enforced": True,
            "indexed_11_pairing_equalities_enforced": True,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
            "self_intersection_used_to_authorize_solver_sat": False,
            "result": result_status,
            "reason_unknown": solver.reason_unknown() if result_status == "UNKNOWN" else None,
        },
        "target": target,
        "result": {
            "status": result_status,
            "witness_r_reduced": witness_r_reduced,
            "completion": completion,
        },
        "semantics": {
            "indexed_terminal_is_not_assumed_to_determine_z": True,
            "z_is_computed_only_after_exact_picard64_completion": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "self_intersection_is_exactly_evaluated_on_the_same_witness_but_not_part_of_the_LIA_sat_claim": True,
            "one_terminal_result_is_not_full178_completion": True,
        },
        "firewalls": {
            "heavy_scaleout_authorized": False,
            "FULL178_complete": False,
            "receiver_credit": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "solver_result": result_status,
        "row_id": ROW_ID,
        "e": EXCEPTIONAL_MASS,
        "terminal_rank": TERMINAL_RANK,
        "terminal_count": int(indexer.terminal_count),
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "self_intersection_pass": completion.get("passes_project_native_self_intersection_lower_bound") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
