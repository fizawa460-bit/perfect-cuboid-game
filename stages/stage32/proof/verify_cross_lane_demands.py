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

REGISTRY_BLOB = "e14bea1a62ec287710064a96f80abe57f8b0c3f4"
REGISTRY_CANON = "9a30646b5567adb30f0192b43f89a8d8a01d1464199b2f0a0d19e1138a7d9c74"
MONITOR_BLOB = "53f286f78574cfad59fc397a9d3268d345331594"
MONITOR_CANON = "48a0f92b1325e80507594c25e8d78dd28a0f0bf5d624bc1afd6d9d43be56e32c"
STATE_BLOB = "76bf5e3d9d97297ff5fbee2bf4826a78d125e171"
STATE_CANON = "bfa2441840bcf60ca70ef6cb288f8721310cdcc78e9f0724a197d35e60e79b21"
AUDIT_REVIEW_ID = 5209163478

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

    req(reg["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V5_CUT201_V27_CONSUMED", "registry schema")
    byid = {d["demand_id"]: d for d in reg["demands"]}
    req(byid["S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"]["status"] == "SATISFIED", "CUT192 demand")
    req(byid["S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"]["status"] == "SATISFIED", "HPADJ demand")
    req(byid["S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"]["status"] == "OBSOLETE", "N398 demand")
    req(byid["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]["status"] == "SATISFIED", "N400 demand")
    cut = byid["S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"]
    req(cut["status"] == "SATISFIED", "CUT201 demand")
    sp = cut["source_population_semantics"]
    req(sp["exact_incremental_rejected_terminals"] == 18758 and sp["exact_incremental_blocks"] == 166, "CUT201 increment")
    req(sp["certlift03_overlap_terminals"] == 6780 and sp["other_consumed_route_overlap_terminals"] == 0 and sp["double_charge"] is False, "CUT201 overlap")
    req(sp["producer_lane_main_authority_subtraction_performed"] is False, "producer subtraction")
    req([d["demand_id"] for d in reg["demands"] if d["status"] == "OPEN"] == [], "unexpected OPEN demands")

    req(mon["schema"] == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V4_CUT201_V27_CONSUMED", "monitor schema")
    lanes = {x["lane"]: x for x in mon["active_specialists"]}
    req(set(lanes) == {"32-01-178", "EX5", "CUT", "MB"}, "monitor coverage")
    req(lanes["CUT"]["pending_main_handoff_ids"] == [], "CUT pending handoff not cleared")
    req(mon["credit_firewall"]["duplicate_pruning_credit_authorized"] is False, "monitor duplicate-credit firewall")
    req(mon["credit_firewall"]["merge_authorized"] is False, "monitor merge firewall")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V30_HPADJ08_AUDIT_SYNCED", "V30 state schema")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "V30 stop gate")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 6703403803993210101494, "V30 authority")
    req(state["current_exact_frontier"]["hpadj08_additive_subtraction_against_v28_performed"] is False, "V30 additive double charge")
    req(state["current_exact_frontier"]["hpadj08_v29_replacement_hostile_audited"] is True, "V29 audit not synchronized")
    req(state["current_exact_frontier"]["hpadj08_v29_replacement_hostile_audit_review_id"] == AUDIT_REVIEW_ID, "V29 audit review")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "V30 audit firewall")

    print("PASS: Stage32 cross-lane demand coordination preserved at V30 HPADJ08 audit-synced boundary")
    print("PASS: no OPEN demand; no duplicate N400/CUT201/HPADJ08 subtraction; MAIN stop gate NONE")

if __name__ == "__main__":
    main()
