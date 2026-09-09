#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_07_outer_rank1_symbolic_x4_parent_preflight as b

SCHEMA = "STAGE32EX5_BC2_08_OUTER_RANK1_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT_V1"
EXPECTED_BC2_07_EVIDENCE_CANONICAL = "c40f658608019cdc3094d96e153ed9974937828b686660151f2904cda1893efe"
EXPECTED_UNKNOWN_PARENT_ID = 7
EXPECTED_RETAINED_PARENT_UNSAT = 19
EXPECTED_REFINEMENT_SUBCASES = 1
EXPECTED_ARTIFACT_UNKNOWN_SPARSE = [[121, 1]]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def verify_canonical(payload: dict, expected: str, name: str) -> None:
    if payload.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"{name} canonical field regression")
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    if b.g.csha(body) != expected:
        raise ValueError(f"{name} canonical replay regression")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--bc2-06-checkpoint", type=Path, required=True)
    ap.add_argument("--bc2-07-evidence", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--refine-timeout-ms", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.refine_timeout_ms <= 0:
        raise ValueError("refinement timeout must be positive")

    g = b.g
    v1 = g.v1

    evidence = load_json(args.bc2_07_evidence)
    verify_canonical(evidence, EXPECTED_BC2_07_EVIDENCE_CANONICAL, "BC2-07 evidence")
    if evidence.get("schema") != b.SCHEMA:
        raise ValueError("BC2-07 evidence schema regression")
    if evidence["parent_result"]["aggregate_result"] != "UNKNOWN":
        raise ValueError("BC2-07 predecessor is not UNKNOWN")
    if evidence["parent_result"]["exact_unsat_parent_branches"] != EXPECTED_RETAINED_PARENT_UNSAT:
        raise ValueError("BC2-07 retained exact-UNSAT parent count regression")
    if evidence["parent_result"]["unknown_parent_branches"] != 1:
        raise ValueError("BC2-07 UNKNOWN parent count regression")
    if evidence["parent_result"]["exact_full_exceptional_refinement_subcase_count_if_needed"] != EXPECTED_REFINEMENT_SUBCASES:
        raise ValueError("BC2-07 refinement count regression")
    if evidence["next_exact_unit"]["id"] != "BC2_08_OUTER_RANK1_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT":
        raise ValueError("BC2-07 next-unit routing regression")
    if evidence["firewalls"]["rank_133_to_265_block_picard64_closed"] is not False:
        raise ValueError("BC2-07 block firewall regression")

    unknowns = evidence["unknown_parents"]
    if len(unknowns) != 1:
        raise ValueError("BC2-07 UNKNOWN record population regression")
    unknown_record = unknowns[0]
    if int(unknown_record["parent_branch_id"]) != EXPECTED_UNKNOWN_PARENT_ID:
        raise ValueError("BC2-07 UNKNOWN parent ID regression")
    if int(unknown_record["selected_residual_mass"]) != 1:
        raise ValueError("BC2-07 selected residual mass regression")
    if int(unknown_record["unselected_residual_mass"]) != 0:
        raise ValueError("BC2-07 unselected residual mass regression")
    if unknown_record["selected_assignment_sparse_labels_1based"] != EXPECTED_ARTIFACT_UNKNOWN_SPARSE:
        raise ValueError("BC2-07 UNKNOWN sparse assignment regression")
    if int(unknown_record["exact_full_exceptional_refinement_subcase_count"]) != 1:
        raise ValueError("BC2-07 UNKNOWN subcase count regression")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    bc2_06, bc2_06_canonical = v1.load_canonical_json(args.bc2_06_checkpoint)
    source_locks = evidence["source_locks"]
    for got, expected, name in (
        (manifest_canonical, source_locks["manifest_canonical_sha256"], "manifest"),
        (prefix_canonical, source_locks["prefix_checkpoint_canonical_sha256"], "prefix"),
        (preflight_canonical, source_locks["adapter_preflight_canonical_sha256"], "adapter preflight"),
        (bc2_06_canonical, source_locks["bc2_06_checkpoint_canonical_sha256"], "BC2-06 checkpoint"),
    ):
        if got != expected:
            raise ValueError(f"{name} source-lock regression")

    replay = bc2_06["exact_replay"]
    if replay["replay_stream_sha256"] != source_locks["bc2_06_replay_stream_sha256"]:
        raise ValueError("BC2-06 replay-stream lock regression")
    if replay["terminal_rank_start"] != b.BLOCK_START or replay["terminal_rank_end"] != b.BLOCK_END:
        raise ValueError("BC2-06 block regression")
    if tuple(replay["base_terminal_x4_zero"]) != b.EXPECTED_BASE_TERMINAL:
        raise ValueError("BC2-06 base terminal regression")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or v1.ROW_ID not in rows:
        raise ValueError("FULL178 manifest row population regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    if indexer.normal_budget != b.EXPECTED_NORMAL_BUDGET:
        raise ValueError("normal budget regression")
    base_terminal = tuple(int(q) for q in indexer.unrank(b.BLOCK_START))
    if base_terminal != b.EXPECTED_BASE_TERMINAL:
        raise ValueError("outer-rank1 base terminal changed")
    base_signature = base_terminal[:4] + base_terminal[5:]
    if base_signature != b.EXPECTED_EXCEPTIONAL_SIGNATURE:
        raise ValueError("outer-rank1 exceptional signature changed")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_08_outer_rank1_refine_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_08_outer_rank1_refine_marking")
    if bundle["canonical_sha256"] != source_locks["retained_bundle_canonical_sha256"]:
        raise ValueError("retained bundle source-lock regression")
    if marking["canonical_sha256"] != source_locks["retained_marking_canonical_sha256"]:
        raise ValueError("retained marking source-lock regression")

    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(label) for label in g.INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = g.lcm_denominator(Pinv)
    if den != source_locks["selected64_inverse_denominator"]:
        raise ValueError("selected64 inverse denominator regression")
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-coordinate map became nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])

    terminal_by_label = {
        int(label): int(value)
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, base_terminal)
    }
    selected_exceptional_labels = [label for label in selected_labels if label > b.NORMAL_COUNT]
    terminal_exceptional_labels = sorted(label for label in terminal_by_label if label > b.NORMAL_COUNT)
    if any(label not in selected_exceptional_labels for label in terminal_exceptional_labels):
        raise ValueError("terminal exceptional label left selected64 set")
    fixed_exceptional_mass = sum(terminal_by_label[label] for label in terminal_exceptional_labels)
    residual_exceptional_mass = v1.EXCEPTIONAL_MASS - fixed_exceptional_mass
    if fixed_exceptional_mass != 3 or residual_exceptional_mass != 1:
        raise ValueError("outer-rank1 exceptional mass split regression")

    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    if len(remaining_selected_exceptional_labels) != 19:
        raise ValueError("remaining selected exceptional count regression")
    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [selected_pos[label] for label in remaining_selected_exceptional_labels]
    unselected_exceptional_labels = [
        label
        for label in range(b.NORMAL_COUNT + 1, b.NORMAL_COUNT + b.EXCEPTIONAL_COUNT + 1)
        if label not in selected_exceptional_labels
    ]
    if len(unselected_exceptional_labels) != 19:
        raise ValueError("unselected exceptional count regression")

    parent_assignments = list(g.at_most_weak_compositions(residual_exceptional_mass, len(remaining_selected_exceptional_labels)))
    if len(parent_assignments) != 20:
        raise ValueError("canonical 20-parent partition regression")
    parent_assignment = parent_assignments[EXPECTED_UNKNOWN_PARENT_ID]
    selected_sparse = g.sparse_labels(remaining_selected_exceptional_labels, parent_assignment)
    if selected_sparse != EXPECTED_ARTIFACT_UNKNOWN_SPARSE:
        raise ValueError("canonical parent-id reconstruction disagrees with artifact")
    if sum(parent_assignment) != 1:
        raise ValueError("unknown parent selected mass regression")

    unselected_assignment = tuple(0 for _ in unselected_exceptional_labels)
    if sum(unselected_assignment) != 0:
        raise AssertionError("unselected zero assignment construction regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != b.EXPECTED_NORMAL_BUDGET:
        raise ValueError("normal mass regression")

    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.refine_timeout_ms)

    for j, label in enumerate(selected_labels):
        ub = v1.EXCEPTIONAL_MASS if label > b.NORMAL_COUNT else normal_mass
        solver.add(y[j] >= 0, y[j] <= ub)
        solver.add(p[label - 1] == y[j])
    for i in range(v1.ALL140_COUNT):
        ub = normal_mass if i < b.NORMAL_COUNT else v1.EXCEPTIONAL_MASS
        solver.add(p[i] >= 0, p[i] <= ub)
        solver.add(den * p[i] == sum(int(Anum[i, j]) * y[j] for j in range(v1.PICARD_RANK)))
    for i in range(v1.PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        solver.add(numerator % den == 0)
    solver.add(sum(p[:b.NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[b.NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)
    for label, value in terminal_by_label.items():
        if label == b.EXPECTED_LABEL49:
            continue
        solver.add(p[label - 1] == value)
    x4 = p[b.EXPECTED_LABEL49 - 1]
    solver.add(x4 >= 0, x4 <= normal_mass)

    for pos, value in zip(remaining_selected_positions, parent_assignment):
        solver.add(y[pos] == int(value))
    for label, value in zip(unselected_exceptional_labels, unselected_assignment):
        solver.add(p[label - 1] == int(value))

    result = solver.check()
    if result == sat:
        aggregate = "SAT"
    elif result == unsat:
        aggregate = "UNSAT"
    elif result == unknown:
        aggregate = "UNKNOWN"
    else:
        raise ValueError(f"unexpected solver result: {result}")

    sat_record = None
    completion = None
    witness_r_reduced = None
    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank_block": [b.BLOCK_START, b.BLOCK_END],
        "outer_exceptional_rank": b.BLOCK_EXCEPTIONAL_RANK,
        "x4_range": [0, normal_mass],
        "base_terminal_x4_zero": list(base_terminal),
        "exceptional_signature": list(base_signature),
    }
    if aggregate == "SAT":
        model = solver.model()
        sat_x4 = int(model.eval(x4, model_completion=True).as_long())
        sat_record = {
            "parent_branch_id": EXPECTED_UNKNOWN_PARENT_ID,
            "refined_subcase_id": 0,
            "selected_assignment_sparse_labels_1based": selected_sparse,
            "unselected_assignment_sparse_labels_1based": [],
            "x4": sat_x4,
            "terminal_rank": b.BLOCK_START + sat_x4,
        }
        target_extra, witness_r_reduced, completion = g.reconstruct_sat(
            model=model,
            y=y,
            p=p,
            Binv=Binv,
            den=den,
            P=P,
            normal_mass=normal_mass,
            bridge=bridge,
            data=data,
            bundle=bundle,
        )
        target.update(target_extra)
        target["terminal_rank"] = sat_record["terminal_rank"]
        target["terminal_pairings"] = list(indexer.unrank(target["terminal_rank"]))
        if target["terminal_pairings"][4] != sat_x4:
            raise ValueError("SAT x4/rank replay regression")
        if tuple(target["terminal_pairings"][:4] + target["terminal_pairings"][5:]) != base_signature:
            raise ValueError("SAT terminal escaped outer-rank1 signature")

    whole_block_unsat = (
        aggregate == "UNSAT"
        and evidence["parent_result"]["exact_unsat_parent_branches"] == EXPECTED_RETAINED_PARENT_UNSAT
        and evidence["parent_result"]["unknown_parent_branches"] == 1
    )

    status_stream = [[EXPECTED_UNKNOWN_PARENT_ID, 0, aggregate]]
    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-08",
        "unit": "BC2_08_OUTER_RANK1_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT",
        "status": (
            "PASS_WHOLE_RANK133_TO_265_BLOCK_EXACT_UNSAT"
            if whole_block_unsat
            else "PASS_OUTER_RANK1_EXACT_COMPLETION_FOUND"
            if aggregate == "SAT"
            else "PASS_OUTER_RANK1_SINGLE_REFINEMENT_UNKNOWN"
        ),
        "source_locks": {
            "bc2_07_evidence_canonical_sha256": EXPECTED_BC2_07_EVIDENCE_CANONICAL,
            "bc2_07_parent_status_stream_sha256": evidence["parent_result"]["parent_status_stream_sha256"],
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "bc2_06_checkpoint_canonical_sha256": bc2_06_canonical,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "selected64_inverse_denominator": den,
        },
        "retained_parent_partition": {
            "parent_branch_count": 20,
            "exact_unsat_parents_retained_without_rerun": EXPECTED_RETAINED_PARENT_UNSAT,
            "unknown_parents_refined_only": 1,
            "bc2_07_parent_partition_recomputed_for_credit": False,
            "unknown_parent_assignment_reconstructed_from_canonical_partition": True,
            "unknown_parent_id": EXPECTED_UNKNOWN_PARENT_ID,
            "selected_assignment_sparse_labels_1based": selected_sparse,
        },
        "full_exceptional_refinement": {
            "expected_subcase_count": 1,
            "tested_subcase_count": 1,
            "exact_unsat_subcase_count": 1 if aggregate == "UNSAT" else 0,
            "unknown_subcase_count": 1 if aggregate == "UNKNOWN" else 0,
            "sat_subcase_count": 1 if aggregate == "SAT" else 0,
            "status_stream_sha256": g.csha(status_stream),
            "all_48_exceptional_pairings_fixed_in_tested_subcase": True,
            "unselected_exceptional_pairings_all_zero": True,
            "x4_kept_symbolic_over_full_range": True,
            "x4_range": [0, normal_mass],
            "new_mathematical_condition_added": False,
            "refine_timeout_ms": args.refine_timeout_ms,
            "z3_version": get_version_string(),
        },
        "exact_result": {
            "aggregate_result": aggregate,
            "rank_133_to_265_block_exact_unsat_authorized": whole_block_unsat,
            "retained_19_plus_refined_1_partition_complete": whole_block_unsat,
        },
        "target": target,
        "result": {
            "status": aggregate,
            "witness_r_reduced": witness_r_reduced,
            "completion": completion,
        },
        "sat_subcase": sat_record,
        "next_exact_unit": {
            "id": (
                "BC2_09_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
                if whole_block_unsat
                else "BC2_08_SINGLE_SUBCASE_EXACT_SOLVER_REFINEMENT"
                if aggregate == "UNKNOWN"
                else "BC2_08_SAT_NODE_SUPPORT_CONSUMPTION"
            ),
            "heavy_scaleout_authorized": False,
            "new_parallel_lane_required": False,
        },
        "firewalls": {
            "rank_0_to_132_block_exact_unsat_retained": True,
            "rank_133_to_265_block_picard64_closed": whole_block_unsat,
            "whole_g1_d008_e4_stratum_closed": False,
            "FULL178_complete": False,
            "stage32_main_credit": False,
            "receiver_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = g.csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "aggregate_result": aggregate,
        "parent_id": EXPECTED_UNKNOWN_PARENT_ID,
        "selected_assignment": selected_sparse,
        "unselected_mass": 0,
        "tested": 1,
        "whole_block_unsat": whole_block_unsat,
        "sat_subcase": sat_record,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
