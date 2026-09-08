#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex5-06-executable-route-contracts.json"

EXPECTED_ROUTES = ["EX5R-XSTAGE-001", "EX5R-EFC-001", "EX5R-EHS-001"]
EXPECTED_SHAPE = ["input", "exact_adapter", "bounded_unit", "expected_observable", "success_predicate", "failure_predicate", "next_route"]


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    data = json.loads(ART.read_text())
    digest = data.pop("canonical_sha256_without_this_field")
    req(csha(data) == digest, "canonical SHA mismatch")
    req(digest == "09f838b088437aea6c8005083503b435c9b0f215e10a5252a8aff98e94676b6f", "unexpected canonical SHA")
    req(data["schema"] == "STAGE32EX5_EX5_06_EXECUTABLE_ROUTE_CONTRACTS_V1", "schema drift")
    req(data["status"] == "EX5_06_EXECUTABLE_ROUTE_CONTRACTS_COMPLETE_UNAUDITED_RETAINED", "status drift")
    req(data["contract_shape"] == EXPECTED_SHAPE, "contract shape drift")
    req(data["stable_route_order"] == EXPECTED_ROUTES, "route order drift")

    for lock in data["source_locks"]:
        p = ROOT / lock["path"]
        req(p.is_file(), f"missing source {lock['path']}")
        req(blob_sha1(p) == lock["blob_sha1"], f"source blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(p.read_text())
            stored = obj.pop("canonical_sha256_without_this_field")
            req(stored == lock["canonical_sha256"], f"stored canonical drift {lock['path']}")
            req(csha(obj) == stored, f"recomputed canonical drift {lock['path']}")

    ledger = json.loads((HERE / "ex5-01-exact-receiver-ledger.json").read_text())
    rows = {r["ledger_row_id"]: r for r in ledger["receiver_rows"]}
    req(rows["R29-LG2-MB::MULTIBRANCH_AT_NODE"]["field_model_ref"] == "FM-GEO-S-MB", "MB field model drift")
    req(rows["R29-LG2-EFF::ALL_NUMERICAL_SURVIVORS"]["field_model_ref"] == "FM-GEO-S", "EFF field model drift")

    card = (ROOT / "docs/arsenal/cards/formal/S34-W03.md").read_text()
    for marker in ["Maturity | **FORMAL**", "B(Q) intersect K(Q) = empty", "receiver branch closed = allowed", "factor cover Q-pointset complete = not implied"]:
        req(marker in card, f"S34-W03 contract marker missing: {marker}")

    contracts = data["execution_contracts"]
    req([c["route_id"] for c in contracts] == EXPECTED_ROUTES, "contracts must cover primary + two backups exactly")
    for c in contracts:
        for field in EXPECTED_SHAPE:
            req(field in c, f"{c['route_id']} missing {field}")
        req(c["bounded_unit"]["heavy_workflow_required"] is False, f"{c['route_id']} first unit must be light")
        req(c["exact_adapter"]["adapter_complete_at_EX5_06"] is False, f"{c['route_id']} adapter precredited")

    x = contracts[0]
    req(x["selection_role"] == "PRIMARY", "XSTAGE must remain primary")
    req(x["bounded_unit"]["unit_id"] == "XSTAGE-PREFLIGHT-01", "XSTAGE unit drift")
    req("B(Q) intersect K(Q)" in x["exact_adapter"]["known_open_issue"], "XSTAGE must expose rational/geometric scope gate")
    req(x["next_route"]["on_failure"] == "EX5R-EFC-001", "XSTAGE failure must move to EFC")

    e = contracts[1]
    req(e["selection_role"] == "BACKUP_1" and e["next_route"]["on_failure"] == "EX5R-EHS-001", "EFC backup chain drift")
    h = contracts[2]
    req(h["selection_role"] == "BACKUP_2", "EHS backup role drift")

    policy = data["execution_policy"]
    req(policy["execute_in_EX5_06"] is False, "EX5-06 must not execute diagnostics")
    req(policy["heavy_compute_authorized"] is False, "heavy compute cannot be authorized")
    req(policy["first_executed_unit"] == "XSTAGE-PREFLIGHT-01", "first future unit drift")
    req(policy["route_failure_is_stage_exhaustion"] is False, "route failure cannot exhaust stage")

    ex5 = data["ex5_contract"]
    req(ex5["executable_route_contracts_complete"] is True, "contract completion missing")
    req(ex5["next_leaf"] == "EX5-07_PRIMARY_ROUTE_MICRODIAGNOSTIC", "successor drift")
    for key in ["primary_microdiagnostic_complete", "nontrivial_receiver_effect_obtained", "qualified_independent_route_established"]:
        req(ex5[key] is False, f"future credit pregranted: {key}")
    for key, value in data["firewalls"].items():
        req(value is False, f"firewall must remain false: {key}")

    print("PASS: Stage32EX5 EX5-06 executable route contracts; XSTAGE Q/geometric gate explicit")


if __name__ == "__main__":
    main()
