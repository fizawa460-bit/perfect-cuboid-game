#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys

ROUTE_ID = "EX5R-ENUM-BTVA-002"
ROW_ID = "g0-d008"
GENUS = 0
DEGREE = 8
LEGACY_E_MIN = 8
LEGACY_E_MAX = 30
REQUIRED_SUPPORT = 6
BLOCKER = "BTVA_G0_D008_EXACT_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_NOT_SOURCE_BOUND"
MATERIALIZER_SOURCE_READY = False
FULL178_RERUN_AUTHORIZED = False
CROSS_ROW_EXPANSION_AUTHORIZED = False

PAIRING_PREFIX_ENGINE = "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
HPERP_ADAPTER = "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
RANK2_BOUND = "stages/stage32/residual-32-01-production/direct_picard_reynolds_rank2_antifixed_coset_bound.py"

def preflight() -> dict:
    return {
        "schema": "STAGE32EX5_EX5R_ENUM_BTVA_002_G0_D008_FAIL_CLOSED_MATERIALIZER_SOURCE_PREFLIGHT_V1",
        "route_id": ROUTE_ID,
        "row_id": ROW_ID,
        "target": {
            "g": GENUS,
            "d": DEGREE,
            "legacy_e_min": LEGACY_E_MIN,
            "legacy_e_max": LEGACY_E_MAX,
            "required_support": REQUIRED_SUPPORT,
            "prune_if": "n(D) < 6",
        },
        "source_capabilities": {
            "pairing_prefix_membership_and_picard_reconstruction_available": True,
            "all140_pairing_reconstruction_available": True,
            "rank2_antifixed_bound_available": True,
            "rank2_antifixed_bound_is_only_a_necessary_pruning_condition": True,
            "source_bound_complete_finite_pairing_coordinate_bounds_available": False,
            "complete_rank61_enumerator_available": False,
            "materializer_source_ready": MATERIALIZER_SOURCE_READY,
        },
        "blocker_code": BLOCKER,
        "firewalls": {
            "heavy_execution_authorized": False,
            "run_key_arm_authorized": False,
            "full178_rerun_authorized": FULL178_RERUN_AUTHORIZED,
            "cross_row_expansion_authorized": CROSS_ROW_EXPANSION_AUTHORIZED,
            "enumeration_complete": False,
            "receiver_credit": False,
            "route_credit": False,
            "stage32_main_credit": False,
            "perfect_cuboid_claim": False,
        },
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    if args.preflight:
        print(json.dumps(preflight(), sort_keys=True))
        return
    raise SystemExit(
        BLOCKER
        + ": refusing enumeration because no exact source-bound finite pairing-prefix "
          "coordinate bounds/backend has been established. Do not arm generation 1."
    )

if __name__ == "__main__":
    main()
