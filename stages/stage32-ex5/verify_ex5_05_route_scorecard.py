#!/usr/bin/env python3
"""Replay Stage32EX5 EX5-05 route typing/scorecard.

This verifier checks only the frozen five-candidate scorecard, deterministic
selection, source locks, and credit firewalls. It grants no mathematical route,
receiver, theorem, endpoint, or Stage32 MAIN credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex5-05-route-scorecard.json"
EX504 = HERE / "ex5-04-repository-asset-dedup.json"

EXPECTED = {
    "EX5R-XSTAGE-001",
    "EX5R-EFC-001",
    "EX5R-EHS-001",
    "EX5R-LGS-001",
    "EX5R-MOD-001",
}
MANDATORY = {
    "receiver_coverage_breadth",
    "object_identity",
    "field_model_compatibility",
    "quantifier_compatibility",
    "existence_effectivity_assumptions",
    "reverse_adapter_length",
    "genuinely_new_information",
    "proof_burden",
    "computational_cost_storage_risk",
    "dependence_on_unproved_actual_carrier_existence",
    "overlap_with_MAIN_EX1_EX4",
    "expected_terminal_effect_if_successful",
}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    data = json.loads(ART.read_text(encoding="utf-8"))
    expected_digest = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == expected_digest, "EX5-05 canonical SHA256 mismatch")
    require(expected_digest == "846c398a3ac2d0143a444eaa925ffb9d91e0f8a4d5b605adf54756d329545951",
            "unexpected EX5-05 canonical SHA256")
    require(data["schema"] == "STAGE32EX5_EX5_05_ROUTE_SCORECARD_V1", "wrong schema")
    require(data["status"] == "EX5_05_ROUTE_TYPING_SCORECARD_COMPLETE_UNAUDITED_RETAINED", "wrong status")

    for lock in data["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(path.read_text(encoding="utf-8"))
            stored = obj.pop("canonical_sha256_without_this_field")
            require(stored == lock["canonical_sha256"], f"stored canonical drift {lock['path']}")
            require(csha(obj) == stored, f"recomputed canonical drift {lock['path']}")

    dedup = json.loads(EX504.read_text(encoding="utf-8"))
    retained = set(dedup["dedup_contract"]["deduplicated_executable_candidate_ids"])
    require(retained == EXPECTED, "EX5-04 retained candidate set drift")

    contract = data["score_contract"]
    require(set(contract["mandatory_dimensions"]) == MANDATORY, "mandatory scorecard dimensions drift")
    require(contract["selection_creates_mathematical_credit"] is False, "score selection cannot grant credit")

    cards = {r["route_id"]: r for r in data["route_scorecards"]}
    require(set(cards) == EXPECTED and len(cards) == 5, "scorecard must cover exactly five retained candidates")
    for rid, record in cards.items():
        for field in MANDATORY:
            require(field in record, f"{rid} missing scorecard field {field}")
        require(record["dependence_on_unproved_actual_carrier_existence"] is False,
                f"{rid} cannot rely on unproved actual-carrier existence")
        for field in ("source_input_readiness","receiver_adapter_readiness","bounded_execution_cost_readiness","independence_readiness"):
            require(record[field] in {0,1,2,3}, f"{rid} invalid readiness value {field}")

    require(cards["EX5R-XSTAGE-001"]["source_input_readiness"] == 3, "XSTAGE source readiness drift")
    require(cards["EX5R-XSTAGE-001"]["selection_status"] == "PRIMARY", "XSTAGE must be primary")
    require(cards["EX5R-EFC-001"]["selection_status"] == "BACKUP_1", "EFC backup drift")
    require(cards["EX5R-EHS-001"]["selection_status"] == "BACKUP_2", "EHS backup drift")
    require(cards["EX5R-LGS-001"]["selection_status"] == "RESERVE_1", "LGS reserve drift")
    require(cards["EX5R-MOD-001"]["selection_status"] == "RESERVE_2", "MOD reserve drift")

    selection = data["selection"]
    require(selection["primary_route_id"] == "EX5R-XSTAGE-001", "primary route drift")
    require(selection["backup_route_ids"] == ["EX5R-EFC-001","EX5R-EHS-001"], "backup route drift")
    require(selection["reserve_route_ids"] == ["EX5R-LGS-001","EX5R-MOD-001"], "reserve route drift")
    require(selection["selection_is_route_qualification"] is False, "selection cannot qualify route")
    require(selection["selection_is_nontrivial_receiver_effect"] is False, "selection cannot grant receiver effect")

    ex5 = data["ex5_contract"]
    require(ex5["route_scorecard_complete"] is True and ex5["primary_route_selected"] is True,
            "EX5-05 completion flags missing")
    require(ex5["backup_route_count"] == 2, "backup count drift")
    require(ex5["next_leaf"] == "EX5-06_EXECUTABLE_ROUTE_CONTRACTS", "wrong EX5-05 successor")
    for key in ("primary_microdiagnostic_complete","nontrivial_receiver_effect_obtained",
                "qualified_independent_route_established","route_credit_granted"):
        require(ex5[key] is False, f"EX5-05 pre-credits future state: {key}")

    for key, value in data["firewalls"].items():
        require(value is False, f"firewall must remain false: {key}")

    print("PASS: Stage32EX5 EX5-05 route typing/scorecard (primary XSTAGE; backups EFC/EHS)")


if __name__ == "__main__":
    main()
