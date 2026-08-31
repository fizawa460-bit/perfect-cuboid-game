#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21ap_selected_pairing_integer_fiber import build_relation_interface, solve_selected_integer_fiber
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_SOURCE_SAMPLE_COUNT = 56
EXPECTED_SOURCE_UNSAT_COUNT = 55
EXPECTED_SOURCE_UNKNOWN_COUNT = 1
SCHEMA = "STAGE32_21AQ_SINGLE_UNKNOWN_SELECTED_PAIRING_EXACT_CLOSURE_V1"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=300000)
    args = ap.parse_args()

    frontier = json.loads(args.frontier.read_text())
    claimed = frontier.pop("canonical_sha256_without_this_field")
    if csha(frontier) != claimed or claimed != EXPECTED_FRONTIER_SHA256:
        raise ValueError("21ap UNKNOWN frontier hash regression")
    if frontier["source_canonical_sha256"] != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap source canonical regression")
    if (
        frontier["source_sample_count"] != EXPECTED_SOURCE_SAMPLE_COUNT
        or frontier["source_unsat_count"] != EXPECTED_SOURCE_UNSAT_COUNT
        or frontier["source_unknown_count"] != EXPECTED_SOURCE_UNKNOWN_COUNT
        or len(frontier["frontier"]) != 1
    ):
        raise ValueError("21ap source accounting regression")

    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])
    bundle = load_retained(args.retained, "s32_21aq_picard")
    marking = load_retained(args.marking, "s32_21aq_marking")
    data = reconstruct_translation_data(marking, bundle)
    relif = build_relation_interface(data)

    status, t, pairings, totals = solve_selected_integer_fiber(
        z=z, data=data, relif=relif, timeout_ms=args.solver_timeout_ms
    )
    if tuple(int(v) for v in totals) != tuple(int(v) for v in target["orbit_totals"]):
        raise ValueError("21aq orbit-total regression against source-locked frontier")

    result = {
        "target": {k: target[k] for k in ("row_id", "e", "a", "u", "v", "z")},
        "status": status,
        "orbit_totals": list(totals),
        "translation_witness_sha256": csha(list(t)) if t is not None else None,
        "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
        "all140_pairing_minimum": min(pairings) if pairings is not None else None,
        "all140_pairing_maximum": max(pairings) if pairings is not None else None,
        "combined_representative_sample_sat": 1 if status == "SAT" else 0,
        "combined_representative_sample_unsat": 56 if status == "UNSAT" else 55,
        "combined_representative_sample_unknown": 1 if status == "UNKNOWN" else 0,
    }
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21aq",
        "mode": "SOURCE_LOCKED_SINGLE_21AP_UNKNOWN_RECHECK_WITH_LONG_EXACT_BOUNDED_INTEGER_SOLVE",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "solver_timeout_ms": args.solver_timeout_ms,
        "result": result,
        "interpretation": {
            "unsat_closes_complete_representative_sample_at_56_of_56_unsat": status == "UNSAT",
            "sat_would_be_exact_original_Z59_lift_checked_by_21ap_solver": status == "SAT",
            "unknown_is_not_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": f"STAGE32_21AQ_{status}",
        "status": status,
        "combined_sat": result["combined_representative_sample_sat"],
        "combined_unsat": result["combined_representative_sample_unsat"],
        "combined_unknown": result["combined_representative_sample_unknown"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
