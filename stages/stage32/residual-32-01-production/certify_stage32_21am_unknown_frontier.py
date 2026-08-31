#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
import diagnose_stage32_21am_quotient_dp as qdp
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "63eb839d65b4cbd52258cc739749370f86356f63fca8783910cdebb4a7f75490"
EXPECTED_UNKNOWN_EXAMPLES_SHA256 = "e2799772d2cf008f0f0a881d06967f04232742ef7197f8340f4f4f6be9145a7c"
EXPECTED_SOURCE_CANONICAL_SHA256 = "7928a76837c2225505a4dbfe2b0794455b0c5f0410a52afdcf95647ecade45c3"
EXPECTED_SOURCE_SAT = 42
EXPECTED_SOURCE_UNSAT = 0
EXPECTED_SOURCE_UNKNOWN = 14
EXPECTED_SAMPLE_TOTAL = 56
SCHEMA = "STAGE32_21AM_UNKNOWN_FRONTIER_EXACT_SAT_CLOSURE_V1"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    frontier = json.loads(args.frontier.read_text())
    claimed = frontier.pop("canonical_sha256_without_this_field")
    if csha(frontier) != claimed or claimed != EXPECTED_FRONTIER_SHA256:
        raise ValueError("21al UNKNOWN frontier canonical hash regression")
    if csha(frontier["unknown_examples"]) != EXPECTED_UNKNOWN_EXAMPLES_SHA256:
        raise ValueError("21al UNKNOWN example stream hash regression")
    if frontier["source_canonical_sha256"] != EXPECTED_SOURCE_CANONICAL_SHA256:
        raise ValueError("21al source canonical hash regression")
    if (
        frontier["source_sat"] != EXPECTED_SOURCE_SAT
        or frontier["source_unsat"] != EXPECTED_SOURCE_UNSAT
        or frontier["source_unknown"] != EXPECTED_SOURCE_UNKNOWN
        or frontier["sampled_states"] != EXPECTED_SAMPLE_TOTAL
        or len(frontier["unknown_examples"]) != EXPECTED_SOURCE_UNKNOWN
        or not frontier["unknown_frontier_complete"]
    ):
        raise ValueError("21al source/frontier accounting regression")

    bundle = load_retained(args.retained, "s32_21am_frontier_picard")
    marking = load_retained(args.marking, "s32_21am_frontier_marking")
    data = reconstruct_translation_data(marking, bundle)
    constraint_rows = tuple(data["constraint_rows"])
    selected_curve_indices = tuple(int(v) for v in data["pivot_rows"])
    selected_orbit_ids = tuple(int(v) for v in data["selected_orbit_ids"])
    orbits = tuple(tuple(int(v) for v in orbit) for orbit in data["orbits"])
    orbit_sizes = tuple(len(orbit) for orbit in orbits)

    qdp._PROOF_ROWS.clear()
    closure_rows = []
    for item in frontier["unknown_examples"]:
        status, witness = qdp.solve_quotient_dp(
            z=tuple(int(v) for v in item["z"]),
            orbit_totals=tuple(int(v) for v in item["orbit_totals"]),
            selected_curve_indices=selected_curve_indices,
            selected_orbit_ids=selected_orbit_ids,
            orbit_sizes=orbit_sizes,
            constraint_rows=constraint_rows,
            timeout_ms=1,
        )
        if status != "SAT" or witness is None:
            raise ValueError(
                f"21am frontier state did not close SAT: {item['row_id']} e={item['e']} a={item['a']} status={status}"
            )
        closure_rows.append(
            {
                "row_id": item["row_id"],
                "e": int(item["e"]),
                "a": int(item["a"]),
                "u": int(item["u"]),
                "v": int(item["v"]),
                "z": [int(v) for v in item["z"]],
                "orbit_totals": [int(v) for v in item["orbit_totals"]],
                "selected_residue_witness_sha256": csha(list(witness)),
            }
        )

    if len(qdp._PROOF_ROWS) != EXPECTED_SOURCE_UNKNOWN:
        raise ValueError("21am structural proof-row count regression")
    if any(row["status"] != "SAT" for row in qdp._PROOF_ROWS):
        raise ValueError("21am structural proof stream contains non-SAT row")

    max_residual_quotient_order = max(
        int(row["residual_quotient_order"]) for row in qdp._PROOF_ROWS
    )
    final_sat = EXPECTED_SOURCE_SAT + len(closure_rows)
    final_unsat = EXPECTED_SOURCE_UNSAT
    final_unknown = 0
    if final_sat + final_unsat + final_unknown != EXPECTED_SAMPLE_TOTAL:
        raise ValueError("21am closed representative accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21am",
        "mode": "SOURCE_LOCKED_42_SAT_PLUS_EXACT_SMITH_DP_CLOSURE_OF_COMPLETE_14_UNKNOWN_FRONTIER",
        "source_21al": {
            "run_id": frontier["source_run_id"],
            "job_id": frontier["source_job_id"],
            "artifact_id": frontier["source_artifact_id"],
            "artifact_zip_sha256": frontier["source_artifact_zip_sha256"],
            "canonical_sha256": EXPECTED_SOURCE_CANONICAL_SHA256,
            "sampled_states": EXPECTED_SAMPLE_TOTAL,
            "sat": EXPECTED_SOURCE_SAT,
            "unsat": EXPECTED_SOURCE_UNSAT,
            "unknown": EXPECTED_SOURCE_UNKNOWN,
        },
        "unknown_frontier": {
            "canonical_sha256": EXPECTED_FRONTIER_SHA256,
            "unknown_examples_sha256": EXPECTED_UNKNOWN_EXAMPLES_SHA256,
            "complete": True,
            "state_count": EXPECTED_SOURCE_UNKNOWN,
        },
        "exact_closure": {
            "closed_state_count": len(closure_rows),
            "all_closed_sat": True,
            "maximum_residual_quotient_order": max_residual_quotient_order,
            "generic_smt_used": False,
            "timeout_or_unknown_possible": False,
            "closure_rows_sha256": csha(closure_rows),
            "structural_proof_rows_sha256": csha(qdp._PROOF_ROWS),
            "closure_rows": closure_rows,
            "structural_proof_rows": qdp._PROOF_ROWS,
        },
        "representative_result": {
            "sampled_states": EXPECTED_SAMPLE_TOTAL,
            "sat": final_sat,
            "unsat": final_unsat,
            "unknown": final_unknown,
            "pure_2adic_plus_orbit_total_filter_zero_unsat_on_representative_sample": True,
        },
        "interpretation": {
            "pure_2adic_plus_orbit_total_filter_observed_pruning_opportunity": False,
            "this_is_not_full178_numerical_credit": True,
            "this_is_not_slice_prune_credit": True,
            "next_leaf": (
                "32-21an: add the 67 independent rational affine-pairing relations beyond the 14 orbit sums, "
                "then enforce all 140 nonnegative pairings before any norm search"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "terminal_family_materialization_run": False,
            "59d_cvp_run": False,
            "full_59d_affine_integer_solver_run": False,
            "representative_sample_only": True,
            "unknown_is_not_unsat": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AM_UNKNOWN_FRONTIER_EXACT_SAT_CLOSURE",
        "sampled": EXPECTED_SAMPLE_TOTAL,
        "sat": final_sat,
        "unsat": final_unsat,
        "unknown": final_unknown,
        "max_residual_quotient_order": max_residual_quotient_order,
        "canonical_sha256": payload["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
