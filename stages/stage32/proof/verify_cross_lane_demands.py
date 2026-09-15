#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"

REGISTRY_BLOB = "68a02f31431ad658b42ad695f9553c67fd6cff01"
REGISTRY_CANON = "aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB = "aad65b1d7e13ff31d3fc0124ddcba0f0a9125c68"
MONITOR_CANON = "5c0c07cd7e38d2a40e6855b8020e34dc2b8dc371108b48886d51f7214090fbf5"
STATE_BLOB = "a7f58ca7cccee3f0e3ae538288d3298cf5571bb6"
STATE_CANON = "0da2f2bc76d0a27b12277bbcf3f823293465f7e937afb80e75940db7f8aed31e"

TD01_DEMAND = "S32.DEMAND.TD01.178.MAIN.AUDITED_BOUND_HANDOFF.V1"
HPADJ10_DEMAND = "S32.DEMAND.HPADJ10.EX5.MAIN.AUDITED_POPULATION_HANDOFF.V1"
CHARACTER_KEY = "PICARD64_X0_X4_X8_X10_PARITY_V1"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def locked_json(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift {path}")
    req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj

def main() -> None:
    reg = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    mon = locked_json(MONITOR, MONITOR_BLOB, MONITOR_CANON)
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)

    req(reg["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V7_TD01_V31_CONSUMED_HPADJ10_RETAINED", "registry schema")
    byid = {d["demand_id"]: d for d in reg["demands"]}
    req([d["demand_id"] for d in reg["demands"] if d["status"] == "OPEN"] == [], "unexpected OPEN demand")
    req(byid["S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"]["status"] == "SATISFIED", "CUT192 demand")
    req(byid["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]["status"] == "SATISFIED", "N400 demand")
    req(byid["S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"]["status"] == "SATISFIED", "CUT201 demand")

    td = byid[TD01_DEMAND]
    req(td["status"] == "SATISFIED", "TD01 demand")
    req(td["producer_surface"]["audit_status"] == "HOSTILE_AUDIT_PASS", "TD01 producer audit")
    req(td["producer_surface"]["audit_review_id"] == 5214778974, "TD01 review")
    req(td["producer_surface"]["observed_exact_head"] == "54945927416a94a67533c7b06c59c5a24e50c4f1", "TD01 head")
    req(td["candidate"]["same_completion_character_key"] == CHARACTER_KEY, "TD01 character")
    req(td["candidate"]["certified_upper_bound_candidate"] == 3453268626299532038131, "TD01 bound")
    req(td["candidate"]["additive_stacking_authorized"] is False, "TD01 additive stacking")
    req(td["satisfying_artifact"]["main_consumption_rule"] == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "TD01 composition")

    hp = byid[HPADJ10_DEMAND]
    req(hp["status"] == "SATISFIED", "HPADJ10 demand")
    req(hp["producer_surface"]["audit_status"] == "HOSTILE_AUDIT_PASS", "HPADJ10 audit")
    req(hp["producer_surface"]["audit_review_id"] == 5211248190, "HPADJ10 review")
    req(hp["scope"]["same_completion_character_key"] == CHARACTER_KEY, "HPADJ10 character")
    req(hp["scope"]["additive_stacking_with_td01_authorized"] is False, "HPADJ10 stacking")
    req(hp["satisfying_artifact"]["additional_main_credit"] == 0, "HPADJ10 duplicate credit")

    consumed = [x for x in reg["audited_result_consumption"] if x["result_id"] == "S32.TD01.V31.CERTIFIED_UPPER_BOUND_REPLACEMENT.V1"]
    req(len(consumed) == 1, "TD01 consumption cardinality")
    c = consumed[0]
    req(c["authoritative_remaining_terminals_before_consumption"] == 6703403803993210101494, "TD01 predecessor bound")
    req(c["authoritative_remaining_terminals_after_consumption"] == 3453268626299532038131, "TD01 post bound")
    req(c["certified_tightening"] == 3250135177693678063363, "TD01 tightening")
    req(c["exact_incremental_rejected_set_claimed"] is False and c["additive_subtraction_performed"] is False and c["double_charge"] is False, "TD01 no-double-charge")

    req(mon["schema"] == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V6_TD01_V31_CONSUMED", "monitor schema")
    lanes = {x["lane"]: x for x in mon["active_specialists"]}
    req(set(lanes) == {"32-01-178", "EX5", "CUT", "MB"}, "monitor lanes")
    req(lanes["32-01-178"]["pending_main_handoff_ids"] == [], "178 handoff not cleared")
    req(lanes["EX5"]["pending_main_handoff_ids"] == [], "EX5 handoff not cleared")
    req(mon["credit_firewall"]["same_character_double_charge_authorized"] is False, "monitor same-character firewall")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V31_TD01_BOUND_CONSUMED_PENDING_REAUDIT", "V31 state schema")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "V31 stop gate")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 3453268626299532038131, "V31 authority")
    req(state["current_exact_frontier"]["td01_additive_subtraction_against_v30_performed"] is False, "V31 additive subtraction")
    req(state["current_exact_frontier"]["td01_double_charge"] is False, "V31 double charge")
    req(state["current_exact_frontier"]["hpadj10_main_additive_credit"] == 0, "HPADJ10 credit")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "V31 replacement audit gate")
    req(state["firewalls"]["full178_complete"] is False and state["firewalls"]["merge_authorized"] is False, "V31 firewalls")

    print("PASS: Stage32 V31 consumes hostile-audited TD01 once by min-composition; no OPEN demand remains")
    print("PASS: HPADJ10 same-character result retained with zero additional MAIN credit; replacement head requires hostile re-audit")

if __name__ == "__main__":
    main()
