#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_04_x4_innermost_block_compression_preflight as b

SCHEMA = "STAGE32EX5_BC2_05_SYMBOLIC_X4_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT_V1"
EXPECTED_BLOCK_CHECKPOINT_CANONICAL = "1be08f0d9bbd1449f33422202d1ba4fd78ed8f501e3a4490721475951595ad74"
EXPECTED_LEDGER_CANONICAL = "fb4a5d1a61e1e1260636ec093f8b355991befa2c2e432cfb5e45ad5b5012f3ac"
EXPECTED_BC2_04_EVIDENCE_CANONICAL = "5da62963fdaf6e3fec6e52c6c7fca4c269e154c553f62c962ba8bf23dd8d247b"
EXPECTED_PARENT_COUNT = 210
EXPECTED_RETAINED_UNSAT = 158
EXPECTED_UNKNOWN_PARENTS = 52
EXPECTED_REFINED_SUBCASES = 376
EXPECTED_UNKNOWN_MASS_COUNTS = {"0": 34, "1": 18}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def verify_canonical_field(payload: dict, expected: str, name: str) -> None:
    got_field = payload.get("canonical_sha256_without_this_field")
    if got_field != expected:
        raise ValueError(f"{name} canonical field regression")
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    got = csha(body)
    if got != expected:
        raise ValueError(f"{name} canonical replay regression")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--rank0-checkpoint", type=Path, required=True)
    ap.add_argument("--rank1-checkpoint", type=Path, required=True)
    ap.add_argument("--block-checkpoint", type=Path, required=True)
    ap.add_argument("--unknown-parent-ledger", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--refine-timeout-ms", type=int, default=1500)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.refine_timeout_ms <= 0:
        raise ValueError("refine timeout must be positive")

    g = b.g
    v1 = g.v1

    block_cp = load_json(args.block_checkpoint)
    ledger = load_json(args.unknown_parent_ledger)
    verify_canonical_field(block_cp, EXPECTED_BLOCK_CHECKPOINT_CANONICAL, "BC2-04 checkpoint")
    verify_canonical_field(ledger, EXPECTED_LEDGER_CANONICAL, "BC2-04 unknown-parent ledger")
    if block_cp["exact_result"]["evidence_canonical_sha256"] != EXPECTED_BC2_04_EVIDENCE_CANONICAL:
        raise ValueError("BC2-04 evidence canonical regression")
    if block_cp["next_exact_unit"]["id"] != "BC2_05_SYMBOLIC_X4_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT":
        raise ValueError("BC2-04 next-unit routing regression")
    if block_cp["proof_partition"]["parent_exact_unsat_count"] != EXPECTED_RETAINED_UNSAT:
        raise ValueError("retained BC2-04 exact-UNSAT parent count regression")
    if block_cp["proof_partition"]["parent_unknown_count"] != EXPECTED_UNKNOWN_PARENTS:
        raise ValueError("BC2-04 UNKNOWN parent count regression")
    if block_cp["proof_partition"]["required_full_exceptional_refinement_subcases"] != EXPECTED_REFINED_SUBCASES:
        raise ValueError("BC2-04 required refinement count regression")
    if ledger["source_evidence_canonical_sha256"] != EXPECTED_BC2_04_EVIDENCE_CANONICAL:
        raise ValueError("unknown-parent ledger source evidence regression")
    if ledger["parent_partition_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("unknown-parent ledger parent count regression")
    if ledger["retained_exact_unsat_parent_count"] != EXPECTED_RETAINED_UNSAT:
        raise ValueError("unknown-parent ledger retained UNSAT regression")
    if ledger["unknown_parent_count"] != EXPECTED_UNKNOWN_PARENTS:
        raise ValueError("unknown-parent ledger UNKNOWN count regression")
    if ledger["expected_full_exceptional_refinement_subcase_count"] != EXPECTED_REFINED_SUBCASES:
        raise ValueError("unknown-parent ledger refinement count regression")
    if ledger["unknown_parent_unselected_mass_counts"] != EXPECTED_UNKNOWN_MASS_COUNTS:
        raise ValueError("unknown-parent ledger mass-count regression")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    rank0, rank0_canonical = v1.load_canonical_json(args.rank0_checkpoint)
    rank1 = load_json(args.rank1_checkpoint)

    if rank0_canonical != g.RANK0_CHECKPOINT_CANONICAL:
        raise ValueError("rank0 checkpoint canonical regression")
    if rank1.get("exact_result", {}).get("rank1_terminal_exact_unsat_authorized") is not True:
        raise ValueError("rank1 exact-UNSAT authority regression")
    locks = rank0["source_locks"]
    for got, expected, name in (
        (manifest_canonical, locks["manifest_canonical_sha256"], "manifest"),
        (prefix_canonical, locks["prefix_checkpoint_canonical_sha256"], "prefix"),
        (preflight_canonical, locks["adapter_preflight_canonical_sha256"], "adapter preflight"),
    ):
        if got != expected:
            raise ValueError(f"{name} source-lock regression")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or v1.ROW_ID not in rows:
        raise ValueError("FULL178 manifest row population regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment-order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    if indexer.normal_budget != b.EXPECTED_NORMAL_BUDGET:
        raise ValueError("normal budget regression")
    block_width = indexer.normal_budget + 1
    if block_width != b.EXPECTED_BLOCK_WIDTH:
        raise ValueError("block width regression")
    base_terminal = tuple(int(q) for q in indexer.unrank(0))
    base_exceptional_signature = base_terminal[:4] + base_terminal[5:]
    for x4_value in range(block_width):
        term = tuple(int(q) for q in indexer.unrank(x4_value))
        if term[4] != x4_value:
            raise ValueError("x4 innermost rank regression")
        if term[:4] + term[5:] != base_exceptional_signature:
            raise ValueError("exceptional signature changed within symbolic block")
        if indexer.rank(term) != x4_value:
            raise ValueError("rank/unrank regression within symbolic block")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_05_x4_refine_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_05_x4_refine_marking")
    if bundle["canonical_sha256"] != locks["retained_bundle_canonical_sha256"]:
        raise ValueError("retained bundle source-lock regression")
    if marking["canonical_sha256"] != locks["retained_marking_canonical_sha256"]:
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
    if den != locks["selected64_inverse_denominator"]:
        raise ValueError("selected64 inverse denominator regression")
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix(
        [[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)]
    )
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-coordinate map became nonintegral")
    Anum = Matrix(
        [[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)]
    )

    terminal_by_label = {
        int(label): int(value)
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, base_terminal)
    }
    selected_exceptional_labels = [label for label in selected_labels if label > b.NORMAL_COUNT]
    terminal_exceptional_labels = sorted(
        label for label in terminal_by_label if label > b.NORMAL_COUNT
    )
    fixed_exceptional_mass = sum(terminal_by_label[label] for label in terminal_exceptional_labels)
    residual_exceptional_mass = v1.EXCEPTIONAL_MASS - fixed_exceptional_mass
    if residual_exceptional_mass != 2:
        raise ValueError("symbolic block residual exceptional mass regression")

    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    if len(remaining_selected_exceptional_labels) != 19:
        raise ValueError("remaining selected exceptional count regression")
    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [
        selected_pos[label] for label in remaining_selected_exceptional_labels
    ]
    unselected_exceptional_labels = [
        label
        for label in range(b.NORMAL_COUNT + 1, b.NORMAL_COUNT + b.EXCEPTIONAL_COUNT + 1)
        if label not in selected_exceptional_labels
    ]
    if len(unselected_exceptional_labels) != 19:
        raise ValueError("unselected exceptional count regression")

    parent_assignments = list(
        g.at_most_weak_compositions(
            residual_exceptional_mass, len(remaining_selected_exceptional_labels)
        )
    )
    if len(parent_assignments) != EXPECTED_PARENT_COUNT:
        raise ValueError("canonical parent partition count regression")

    unknown_ids = [int(q) for q in ledger["unknown_parent_ids"]]
    if len(unknown_ids) != len(set(unknown_ids)) or len(unknown_ids) != EXPECTED_UNKNOWN_PARENTS:
        raise ValueError("unknown parent IDs are not a 52-element set")
    if min(unknown_ids) < 0 or max(unknown_ids) >= EXPECTED_PARENT_COUNT:
        raise ValueError("unknown parent ID outside canonical parent partition")
    if csha(unknown_ids) != ledger["unknown_parent_id_stream_sha256"]:
        raise ValueError("unknown parent ID stream hash regression")

    reconstructed_unknown_records = []
    reconstructed_mass_counts = {"0": 0, "1": 0}
    reconstructed_refinement_total = 0
    for parent_id in unknown_ids:
        assignment = parent_assignments[parent_id]
        selected_mass = int(sum(assignment))
        unselected_mass = residual_exceptional_mass - selected_mass
        if unselected_mass not in (0, 1):
            raise ValueError("BC2-04 UNKNOWN parent has unexpected residual mass")
        count = math.comb(
            unselected_mass + len(unselected_exceptional_labels) - 1,
            len(unselected_exceptional_labels) - 1,
        )
        reconstructed_mass_counts[str(unselected_mass)] += 1
        reconstructed_refinement_total += count
        reconstructed_unknown_records.append({
            "parent_branch_id": int(parent_id),
            "selected_residual_mass": selected_mass,
            "selected_assignment_sparse_labels_1based": g.sparse_labels(
                remaining_selected_exceptional_labels, assignment
            ),
            "unselected_residual_mass": int(unselected_mass),
            "exact_full_exceptional_refinement_subcase_count": int(count),
            "reason_unknown": "canceled",
        })
    if reconstructed_mass_counts != EXPECTED_UNKNOWN_MASS_COUNTS:
        raise ValueError("reconstructed UNKNOWN mass-count regression")
    if reconstructed_refinement_total != EXPECTED_REFINED_SUBCASES:
        raise ValueError("reconstructed refinement total regression")
    if csha(reconstructed_unknown_records) != ledger["unknown_parent_records_sha256"]:
        raise ValueError("reconstructed UNKNOWN record stream does not match BC2-04 artifact")

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
        solver.add(
            den * p[i]
            == sum(int(Anum[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        )
    for i in range(v1.PICARD_RANK):
        numerator = sum(
            int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK)
        )
        solver.add(numerator % den == 0)
    solver.add(sum(p[:b.NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[b.NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)
    for label, value in terminal_by_label.items():
        if label == b.EXPECTED_LABEL49:
            continue
        solver.add(p[label - 1] == value)
    x4 = p[b.EXPECTED_LABEL49 - 1]
    solver.add(x4 >= 0, x4 <= normal_mass)

    status_stream = []
    exact_unsat_count = 0
    unknown_subcases = []
    sat_record = None
    sat_model = None
    tested = 0

    stop = False
    for parent_id in unknown_ids:
        parent_assignment = parent_assignments[parent_id]
        selected_mass = int(sum(parent_assignment))
        unselected_mass = residual_exceptional_mass - selected_mass
        refine_assignments = list(
            g.exact_weak_compositions(unselected_mass, len(unselected_exceptional_labels))
        )
        expected_here = math.comb(
            unselected_mass + len(unselected_exceptional_labels) - 1,
            len(unselected_exceptional_labels) - 1,
        )
        if len(refine_assignments) != expected_here:
            raise ValueError("full-exceptional refinement coverage regression")

        for refine_id, unselected_assignment in enumerate(refine_assignments):
            solver.push()
            try:
                for pos, value in zip(remaining_selected_positions, parent_assignment):
                    solver.add(y[pos] == int(value))
                for label, value in zip(
                    unselected_exceptional_labels, unselected_assignment
                ):
                    solver.add(p[label - 1] == int(value))
                result = solver.check()
                tested += 1
                if result == sat:
                    status_stream.append([int(parent_id), int(refine_id), "SAT"])
                    sat_model = solver.model()
                    sat_x4 = int(sat_model.eval(x4, model_completion=True).as_long())
                    sat_record = {
                        "parent_branch_id": int(parent_id),
                        "refined_subcase_id": int(refine_id),
                        "selected_assignment_sparse_labels_1based": g.sparse_labels(
                            remaining_selected_exceptional_labels, parent_assignment
                        ),
                        "unselected_assignment_sparse_labels_1based": g.sparse_labels(
                            unselected_exceptional_labels, unselected_assignment
                        ),
                        "x4": sat_x4,
                        "terminal_rank": sat_x4,
                    }
                    stop = True
                elif result == unsat:
                    status_stream.append([int(parent_id), int(refine_id), "UNSAT"])
                    exact_unsat_count += 1
                elif result == unknown:
                    reason = solver.reason_unknown()
                    status_stream.append([int(parent_id), int(refine_id), "UNKNOWN"])
                    unknown_subcases.append({
                        "parent_branch_id": int(parent_id),
                        "refined_subcase_id": int(refine_id),
                        "reason_unknown": reason,
                    })
                else:
                    raise ValueError(f"unexpected solver result: {result}")
            finally:
                solver.pop()
            if stop:
                break
        if stop:
            break

    if sat_record is not None:
        aggregate = "SAT"
    elif tested == EXPECTED_REFINED_SUBCASES and exact_unsat_count == EXPECTED_REFINED_SUBCASES and not unknown_subcases:
        aggregate = "UNSAT"
    else:
        aggregate = "UNKNOWN"

    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank_block": [0, 132],
        "x4_range": [0, normal_mass],
    }
    completion = None
    witness_r_reduced = None
    if aggregate == "SAT":
        if sat_model is None or sat_record is None:
            raise ValueError("SAT refinement missing model")
        target_extra, witness_r_reduced, completion = g.reconstruct_sat(
            model=sat_model,
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
        target["terminal_rank"] = int(sat_record["terminal_rank"])
        target["terminal_pairings"] = list(indexer.unrank(target["terminal_rank"]))
        if target["terminal_pairings"][4] != sat_record["x4"]:
            raise ValueError("SAT x4 terminal-rank replay regression")

    whole_block_unsat = (
        aggregate == "UNSAT"
        and tested == EXPECTED_REFINED_SUBCASES
        and exact_unsat_count == EXPECTED_REFINED_SUBCASES
        and len(unknown_subcases) == 0
        and block_cp["proof_partition"]["parent_exact_unsat_count"] == EXPECTED_RETAINED_UNSAT
    )

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-05",
        "unit": "BC2_05_SYMBOLIC_X4_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT",
        "status": (
            "PASS_WHOLE_RANK0_TO_132_BLOCK_EXACT_UNSAT"
            if whole_block_unsat
            else "PASS_SYMBOLIC_BLOCK_EXACT_COMPLETION_FOUND"
            if aggregate == "SAT"
            else "PASS_REFINEMENT_INCOMPLETE_UNKNOWN_REMAINS"
        ),
        "source_locks": {
            "block_checkpoint_canonical_sha256": EXPECTED_BLOCK_CHECKPOINT_CANONICAL,
            "unknown_parent_ledger_canonical_sha256": EXPECTED_LEDGER_CANONICAL,
            "bc2_04_evidence_canonical_sha256": EXPECTED_BC2_04_EVIDENCE_CANONICAL,
            "unknown_parent_id_stream_sha256": ledger["unknown_parent_id_stream_sha256"],
            "unknown_parent_records_sha256": ledger["unknown_parent_records_sha256"],
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "selected64_inverse_denominator": den,
        },
        "retained_parent_partition": {
            "parent_branch_count": EXPECTED_PARENT_COUNT,
            "exact_unsat_parents_retained_without_rerun": EXPECTED_RETAINED_UNSAT,
            "unknown_parents_refined_only": EXPECTED_UNKNOWN_PARENTS,
            "bc2_04_parent_partition_recomputed_for_credit": False,
            "unknown_parent_assignments_reconstructed_from_canonical_partition": True,
        },
        "full_exceptional_refinement": {
            "expected_subcase_count": EXPECTED_REFINED_SUBCASES,
            "tested_subcase_count": tested,
            "exact_unsat_subcase_count": exact_unsat_count,
            "unknown_subcase_count": len(unknown_subcases),
            "sat_subcase_found": sat_record is not None,
            "status_stream_sha256": csha(status_stream),
            "unknown_subcases": unknown_subcases,
            "all_48_exceptional_pairings_fixed_in_each_tested_subcase": True,
            "x4_kept_symbolic_over_full_range": True,
            "x4_range": [0, normal_mass],
            "new_mathematical_condition_added": False,
        },
        "exact_result": {
            "aggregate_result": aggregate,
            "whole_rank_0_to_132_block_exact_unsat_authorized": whole_block_unsat,
            "retained_158_plus_refined_376_partition_complete": whole_block_unsat,
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
                "BC2_06_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT"
                if whole_block_unsat
                else "BC2_05_UNKNOWN_SUBCASE_REFINEMENT"
                if aggregate == "UNKNOWN"
                else "BC2_05_SAT_NODE_SUPPORT_CONSUMPTION"
            ),
            "heavy_scaleout_authorized": False,
            "new_parallel_lane_required": False,
        },
        "firewalls": {
            "whole_rank_0_to_132_block_closed": whole_block_unsat,
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
        "z3_version": get_version_string(),
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "aggregate_result": aggregate,
        "tested": tested,
        "exact_unsat": exact_unsat_count,
        "unknown": len(unknown_subcases),
        "sat_subcase": sat_record,
        "whole_block_unsat": whole_block_unsat,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
