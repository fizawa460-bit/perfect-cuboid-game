#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNKEY = HERE / "runkeys" / "ex5r-enum-btva-002-g0-d008-rank61.json"
STORAGE = HERE / "ex5r-enum-btva-002-g0-d008-storage-output-contract.json"
CERT = HERE / "ex5r-enum-btva-002-g0-d008-runkey-storage-preflight.json"
LEDGER = HERE / "post1728-cycle2-candidate-ledger-v2.json"

EXPECTED = {
    RUNKEY: "18d4caef49b50c89fbfa671dd5ff244c217873f98008c2d6f2e4ed92679e70dc",
    STORAGE: "a4aedf220533462612d7252c21a6cd54345d6edf7427abe248a7a3992e6c01c2",
    CERT: "c3be5e8e54acfc5a61b3206c4f0c0c1fbf3b0fead4aa3299e7781f6070f60ca7",
    LEDGER: "436f472a41690fa93574d49b05723c019072407b84c9cdcb2499c8f91b295a2f",
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    expected = EXPECTED[path]
    if claimed != expected or csha(raw) != expected:
        raise SystemExit(f"canonical regression: {path.name}")
    raw["canonical_sha256_without_this_field"] = claimed
    return raw


def main() -> None:
    runkey = load_checked(RUNKEY)
    storage = load_checked(STORAGE)
    cert = load_checked(CERT)
    ledger = load_checked(LEDGER)

    if runkey["authority"] != "SCRATCH_NONAUTHORITATIVE":
        raise SystemExit("run-key authority firewall regression")
    if runkey["route_id"] != "EX5R-ENUM-BTVA-002":
        raise SystemExit("run-key route regression")
    if runkey["generation"] != 0 or runkey["armed"] is not False:
        raise SystemExit("cold run-key regression")
    auth = runkey["authorization"]
    if auth["heavy_execution_authorized"] or not auth["arm_requires_distinct_followup_commit"]:
        raise SystemExit("heavy authorization firewall regression")
    if auth["next_valid_arm_generation"] != 1:
        raise SystemExit("next generation regression")
    scope = runkey["scope"]
    if (scope["row_id"], scope["g"], scope["d"], scope["required_support"]) != ("g0-d008", 0, 8, 6):
        raise SystemExit("one-row scope regression")
    if scope["planned_jobs"] != 1 or scope["planned_shards"] != 1 or scope["effective_heavy_concurrency"] != 1:
        raise SystemExit("bounded execution-shape regression")
    if scope["full178_rerun_authorized"] or scope["cross_row_expansion_authorized"]:
        raise SystemExit("FULL178/cross-row firewall regression")
    source = runkey["source_contract"]
    if source["materializer_source_ready"] or source["required_materializer_blob_sha1"] is not None:
        raise SystemExit("premature materializer-source credit regression")

    shape = storage["execution_shape"]
    if (shape["planned_jobs"], shape["planned_shards"], shape["effective_heavy_concurrency"]) != (1, 1, 1):
        raise SystemExit("storage execution shape regression")
    if shape["full178_rerun_authorized"] or shape["cross_row_expansion_authorized"] or shape["raw_class_records_uploaded"]:
        raise SystemExit("storage scope firewall regression")
    pre = storage["storage_preflight"]
    if pre["projected_peak_simultaneous_artifact_mb"] > storage["policy_lock"]["operating_budget_mb"]:
        raise SystemExit("storage budget regression")
    if pre["largest_plausible_uploaded_artifact_mb"] > 1.0 or pre["final_output_max_mb"] > 1.0:
        raise SystemExit("compact artifact cap regression")
    if pre["final_output_retention_days"] != 3:
        raise SystemExit("retention regression")
    out = storage["compact_output_contract"]
    if out["max_bytes"] != 1048576:
        raise SystemExit("compact output byte cap regression")
    if out["enumeration_status_allowed"] != ["COMPLETE", "RESOURCE_WALL", "ERROR"]:
        raise SystemExit("completion status regression")
    if out["resource_wall_semantics"].startswith("execution-resource wall only") is False:
        raise SystemExit("resource-wall semantic regression")
    if storage["execution_readiness"]["heavy_execution_ready"]:
        raise SystemExit("premature heavy-execution readiness regression")

    pf = cert["preflight_result"]
    if not pf["run_key_present"] or pf["run_key_armed"] or pf["run_key_generation"] != 0:
        raise SystemExit("certificate run-key regression")
    if not pf["storage_output_contract_present"] or pf["heavy_execution_ready"] or pf["materializer_source_ready"]:
        raise SystemExit("certificate execution gate regression")
    dec = cert["route_decision"]
    if dec["status"] != "LIVE_RUNKEY_STORAGE_CONTRACT_READY_MATERIALIZER_PENDING":
        raise SystemExit("route status regression")
    if dec["blocker_code"] != "BTVA_G0_D008_MATERIALIZER_SOURCE_NOT_YET_IMPLEMENTED":
        raise SystemExit("materializer blocker regression")
    if dec["mathematical_failure"] or not dec["predicate_survives"]:
        raise SystemExit("route semantic regression")
    if dec["nontrivial_receiver_effect_obtained"] or dec["qualified_independent_route_established"]:
        raise SystemExit("premature route credit regression")

    rec = next(x for x in ledger["candidate_records"] if x["candidate_id"] == "EX5R-ENUM-BTVA-002")
    if rec["status"] != dec["status"] or rec["blocker_code"] != dec["blocker_code"]:
        raise SystemExit("ledger/certificate route mismatch")
    if rec["next_unit"] != "BTVA_G0_D008_RANK61_MATERIALIZER_IMPLEMENTATION_PREFLIGHT":
        raise SystemExit("next-unit regression")
    if ledger["cycle"]["route_status"] != "LIVE_AT_MATERIALIZER_IMPLEMENTATION_GATE":
        raise SystemExit("ledger cycle status regression")

    for obj in (runkey, storage, cert):
        if any(obj["credit"].values()):
            raise SystemExit("credit firewall regression")
    if any(cert["firewalls"].values()):
        raise SystemExit("certificate firewall regression")
    if any(ledger["credit"].values()):
        raise SystemExit("ledger credit firewall regression")

    print(json.dumps({
        "status": "PASS_STAGE32EX5_BTVA_G0_D008_RUNKEY_STORAGE_PREFLIGHT",
        "route": "EX5R-ENUM-BTVA-002",
        "run_key_generation": 0,
        "armed": False,
        "next_unit": rec["next_unit"],
        "canonical_sha256": EXPECTED[CERT],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
