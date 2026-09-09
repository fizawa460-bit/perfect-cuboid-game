#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "ex5r-enum-btva-002-g0-d008-materializer-implementation-preflight.json"
SOURCE = HERE / "run_ex5r_enum_btva_002_g0_d008_rank61.py"
RUNKEY = HERE / "runkeys" / "ex5r-enum-btva-002-g0-d008-rank61.json"

EXPECTED_CANONICAL = "03751e0fc3c50e881b8187338cf1cd47aa4a8f42655449375262cac83e5889f4"
EXPECTED_SOURCE_BLOB = "271c7c67f5fbcbce245950f40423626cfb9e27d2"
EXPECTED_BLOCKER = "BTVA_G0_D008_EXACT_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_NOT_SOURCE_BOUND"

def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main() -> None:
    raw = json.loads(CERT.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_CANONICAL or csha(raw) != EXPECTED_CANONICAL:
        raise SystemExit("canonical certificate regression")

    if raw["authority"] != "SCRATCH_NONAUTHORITATIVE":
        raise SystemExit("authority firewall regression")
    if raw["route_id"] != "EX5R-ENUM-BTVA-002":
        raise SystemExit("route regression")
    if raw["target"] != {
        "d": 8, "g": 0, "legacy_e_max": 30, "legacy_e_min": 8,
        "required_support": 6, "row_id": "g0-d008"
    }:
        raise SystemExit("row contract regression")

    source_bytes = SOURCE.read_bytes()
    if git_blob_sha(source_bytes) != EXPECTED_SOURCE_BLOB:
        raise SystemExit("fail-closed source blob regression")
    source_text = source_bytes.decode()
    required_literals = [
        'MATERIALIZER_SOURCE_READY = False',
        'FULL178_RERUN_AUTHORIZED = False',
        'CROSS_ROW_EXPANSION_AUTHORIZED = False',
        EXPECTED_BLOCKER,
        'Do not arm generation 1.',
    ]
    if any(x not in source_text for x in required_literals):
        raise SystemExit("fail-closed source semantic regression")

    backend = raw["inspected_backend"]
    if not backend["pairing_prefix_engine"]["supports_exact_selected64_pairing_membership"]:
        raise SystemExit("prefix membership regression")
    if not backend["pairing_prefix_engine"]["supports_exact_picard64_reconstruction_from_complete_selected64_pairings"]:
        raise SystemExit("Picard reconstruction regression")
    if backend["pairing_prefix_engine"]["provides_complete_finite_pairing_coordinate_bounds"]:
        raise SystemExit("unsupported finite-bound credit regression")
    if backend["hperp_integral_adapter"]["cap_field_semantics_promoted_here_to_complete_pairing_coordinate_bound"]:
        raise SystemExit("cap semantics promotion regression")
    if not backend["rank2_antifixed_bound"]["supports_exact_necessary_pruning_bound"]:
        raise SystemExit("rank2 bound regression")
    if backend["rank2_antifixed_bound"]["is_complete_rank61_class_enumerator"]:
        raise SystemExit("rank2 completeness overclaim regression")

    dec = raw["route_decision"]
    if dec["blocker_code"] != EXPECTED_BLOCKER:
        raise SystemExit("blocker regression")
    if dec["status"] != "LIVE_AT_FINITE_PREFIX_BOUNDS_ADAPTER_GATE":
        raise SystemExit("route status regression")
    if dec["mathematical_failure"] or not dec["predicate_survives"]:
        raise SystemExit("route semantics regression")
    if dec["materializer_implementation_complete"]:
        raise SystemExit("premature implementation credit")
    if dec["nontrivial_receiver_effect_obtained"] or dec["qualified_independent_route_established"]:
        raise SystemExit("premature receiver/route credit")

    key = json.loads(RUNKEY.read_text())
    if key["generation"] != 0 or key["armed"] is not False:
        raise SystemExit("cold run-key regression")
    if key["source_contract"]["materializer_source_ready"] is not False:
        raise SystemExit("run-key source-ready regression")
    if key["source_contract"]["required_materializer_blob_sha1"] is not None:
        raise SystemExit("run-key must not source-lock fail-closed skeleton as ready materializer")

    if any(raw["credit"].values()):
        raise SystemExit("credit firewall regression")
    if raw["execution"]["heavy_run_performed"] or raw["execution"]["generation1_arm_authorized"]:
        raise SystemExit("execution firewall regression")
    if raw["firewalls"]["g0_d008_closed"] or raw["firewalls"]["full178_completed"]:
        raise SystemExit("closure firewall regression")
    if raw["firewalls"]["perfect_cuboid_claim"] or raw["firewalls"]["merge_authorized"]:
        raise SystemExit("endpoint/merge firewall regression")

    print(json.dumps({
        "status": "PASS_STAGE32EX5_BTVA_G0_D008_MATERIALIZER_IMPLEMENTATION_PREFLIGHT",
        "route": raw["route_id"],
        "blocker": EXPECTED_BLOCKER,
        "next_unit": dec["next_unit"],
        "canonical_sha256": EXPECTED_CANONICAL,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
