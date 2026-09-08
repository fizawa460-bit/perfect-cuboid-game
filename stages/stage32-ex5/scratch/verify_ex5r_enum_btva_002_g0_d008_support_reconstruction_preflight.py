#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "ex5r-enum-btva-002-g0-d008-support-reconstruction-preflight.json"
EXPECTED_CANONICAL = "22ba931586305b5b0262b0e63cf23a845e1ccc8f1622450c143d9474f63c9f40"
EXPECTED_GATE = "BTVA_G0_D008_REQUIRES_FRESH_RANK61_CLASS_MATERIALIZATION_RUN_KEY"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    raw = json.loads(CERT.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_CANONICAL or csha(raw) != EXPECTED_CANONICAL:
        raise SystemExit("canonical certificate regression")

    if raw["authority"] != "SCRATCH_NONAUTHORITATIVE":
        raise SystemExit("scratch authority firewall regression")
    if raw["route_id"] != "EX5R-ENUM-BTVA-002":
        raise SystemExit("route id regression")

    row = raw["row"]
    if (row["row_id"], row["g"], row["d"], row["legacy_e_min"], row["legacy_e_max"], row["required_support"]) != (
        "g0-d008", 0, 8, 8, 30, 6
    ):
        raise SystemExit("g0-d008 row contract regression")
    if row["legacy_cheap_cut_vacuous_on_row"] is not True:
        raise SystemExit("cheap-cut scope regression")

    sf = raw["structural_findings"]
    if (sf["picard_rank"], sf["compressed_slice_rank"], sf["affine_slice_kernel_rank"], sf["exceptional_component_count"]) != (64, 3, 61, 48):
        raise SystemExit("Picard slice rank regression")
    if sf["legacy_21ad_preserves_individual_exceptional_support"] is not False:
        raise SystemExit("legacy support firewall regression")
    if sf["individual_support_recoverable_from_d_e_a_alone"] is not False:
        raise SystemExit("projection-information firewall regression")
    if sf["complete_support_reconstruction_requires_fresh_integral_class_lifting"] is not True:
        raise SystemExit("fresh lifting gate regression")

    gate = raw["execution_gate"]
    if gate["gate_code"] != EXPECTED_GATE or gate["route_status"] != "LIVE_AT_EXECUTION_GATE":
        raise SystemExit("execution gate regression")
    if gate["heavy_run_performed"] or gate["explicit_run_key_present"] or gate["explicit_storage_policy_present"]:
        raise SystemExit("unauthorized heavy-run credit regression")
    if gate["full178_rerun_authorized"]:
        raise SystemExit("FULL178 authorization firewall regression")

    dec = raw["route_decision"]
    if dec["mathematical_failure"] or not dec["predicate_survives"]:
        raise SystemExit("route-status semantic regression")
    if dec["nontrivial_receiver_effect_obtained"] or dec["qualified_independent_route_established"]:
        raise SystemExit("premature route credit regression")

    if any(raw["credit"].values()):
        raise SystemExit("credit firewall regression")
    fw = raw["firewalls"]
    if fw["g0_d008_closed"] or fw["full178_completed"] or fw["stage32_main_credit"] if "stage32_main_credit" in fw else False:
        raise SystemExit("closure firewall regression")
    if fw["Q602_excluded"] or fw["O210_excluded"] or fw["perfect_cuboid_claim"] or fw["merge_authorized"]:
        raise SystemExit("endpoint firewall regression")

    print(json.dumps({
        "status": "PASS_STAGE32EX5_BTVA_G0_D008_EXECUTION_GATE_PREFLIGHT",
        "route": raw["route_id"],
        "gate": gate["gate_code"],
        "required_support": row["required_support"],
        "canonical_sha256": EXPECTED_CANONICAL,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
