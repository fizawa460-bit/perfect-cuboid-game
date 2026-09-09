#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]

FILES = {
    "csc": HERE / "ex5r-csc-002-nonv6-adapter-preflight.json",
    "btva": HERE / "ex5r-enum-btva-002-support-predicate-preflight.json",
    "btva_impl": HERE / "ex5r-enum-btva-002-g0-d008-materializer-implementation-preflight.json",
    "ledger": HERE / "post1728-cycle2-candidate-ledger-v2.json",
}

def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")

def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def load_canonical(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    stored = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == stored, f"canonical drift: {path.name}")
    data["canonical_sha256_without_this_field"] = stored
    return data

csc = load_canonical(FILES["csc"])
btva = load_canonical(FILES["btva"])
btva_impl = load_canonical(FILES["btva_impl"])
ledger = load_canonical(FILES["ledger"])

for obj in (csc, btva):
    for lock in obj["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock: {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift: {lock['path']}")
        if "canonical_sha256" in lock:
            raw = json.loads(path.read_text(encoding="utf-8"))
            require(
                raw.get("canonical_sha256_without_this_field") == lock["canonical_sha256"],
                f"stored source canonical drift: {lock['path']}",
            )

require(csc["status"] == "ROUTE_BLOCKED_BY_NAMED_MISSING_ADAPTER", "CSC status drift")
require(
    csc["route_decision"]["blocker_code"]
    == "CSC_MISSING_GENERAL_RECEIVER_TO_UPSTAIRS_CORRESPONDENCE_ADAPTER",
    "CSC blocker drift",
)
require(csc["credit"]["nontrivial_receiver_effect_obtained"] is False, "CSC credit leak")

require(
    btva["status"] == "ROUTE_SURVIVES_PREFLIGHT_WITH_EXACT_NEW_PREDICATE",
    "BTVA status drift",
)
require(btva["predicate"]["support"] == "n(D)=#{j: p_j(D)>0}", "BTVA support definition drift")
w = btva["preflight_results"]["strictness_witness"]
require((w["g"], w["d"], w["e"], w["support"], w["required_support"]) == (1, 186, 266, 44, 47), "strictness witness drift")
require(w["aggregate_e_cut_passes"] is True and w["strong_support_predicate_fails"] is True, "strictness relation drift")
require(btva["credit"]["nontrivial_receiver_effect_obtained"] is False, "BTVA receiver-effect credit leak")
require(btva["execution_policy"]["selected_first_open_row"] == "g0-d008", "BTVA next row drift")
require(btva["execution_policy"]["heavy_full178_run_authorized"] is False, "heavy authorization leak")

require(
    btva_impl["route_decision"]["status"] == "LIVE_AT_FINITE_PREFIX_BOUNDS_ADAPTER_GATE",
    "BTVA implementation-gate status drift",
)
require(
    btva_impl["route_decision"]["blocker_code"]
    == "BTVA_G0_D008_EXACT_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_NOT_SOURCE_BOUND",
    "BTVA implementation blocker drift",
)
require(btva_impl["route_decision"]["mathematical_failure"] is False, "BTVA false mathematical failure")
require(btva_impl["route_decision"]["predicate_survives"] is True, "BTVA predicate survival drift")
require(btva_impl["execution"]["run_key_generation"] == 0, "BTVA run-key generation drift")
require(btva_impl["execution"]["run_key_armed"] is False, "BTVA run-key arm leak")
require(btva_impl["credit"]["receiver_credit"] is False, "BTVA implementation receiver credit leak")

records = {x["candidate_id"]: x for x in ledger["candidate_records"]}
require(set(records) == {"EX5R-CSC-002", "EX5R-ENUM-BTVA-002"}, "cycle2 candidate set drift")
require(records["EX5R-CSC-002"]["status"] == "BLOCKED", "ledger CSC status drift")
brec = records["EX5R-ENUM-BTVA-002"]
require(brec["status"] == "LIVE_AT_FINITE_PREFIX_BOUNDS_ADAPTER_GATE", "ledger BTVA status drift")
require(
    brec["blocker_code"] == "BTVA_G0_D008_EXACT_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_NOT_SOURCE_BOUND",
    "ledger BTVA blocker drift",
)
require(
    brec["evidence"] == "stages/stage32-ex5/scratch/ex5r-enum-btva-002-g0-d008-materializer-implementation-preflight.json",
    "ledger BTVA evidence drift",
)
require(
    brec["next_unit"] == "BTVA_G0_D008_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_DISCOVERY",
    "ledger BTVA next-unit drift",
)
require(ledger["cycle"]["active_route"] == "EX5R-ENUM-BTVA-002", "active route drift")
require(ledger["cycle"]["route_status"] == "LIVE_AT_FINITE_PREFIX_BOUNDS_ADAPTER_GATE", "cycle route status drift")
require(ledger["authority_breadth_cycle_opened"] is False, "scratch breadth authority leak")
require(ledger["credit"]["qualified_independent_route_established"] is False, "qualification credit leak")
require(ledger["firewalls"]["main_state_rewritten"] is False, "MAIN state firewall drift")

print("PASS_STAGE32EX5_POST1728_CYCLE2_CSC_BLOCK_BTVA_FINITE_PREFIX_GATE")
