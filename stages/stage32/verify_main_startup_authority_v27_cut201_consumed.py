#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/cut201-main-disposition/CUT201-V27-MAIN-CONSUMPTION.json"
REGISTRY = HERE / "proof/CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
CLAIM_REGISTRY = HERE / "proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"
STATE_BLOB = "399221dc91733b3a9a2d79ae3473ea2365e409a3"
STATE_CANON = "e25d3c2d3381193462af28577c6ddd0c6c5fc597192a640d7534034213b86d1b"
RECEIPT_BLOB = "cdd766cae064430bb1aa901f1d023fcb48b39877"
RECEIPT_CANON = "aa9a40c0514412444a15db8a59d54de4866de39345ff4a0dbd531c14eaced9f6"
REGISTRY_BLOB = "e14bea1a62ec287710064a96f80abe57f8b0c3f4"
REGISTRY_CANON = "9a30646b5567adb30f0192b43f89a8d8a01d1464199b2f0a0d19e1138a7d9c74"
MONITOR_BLOB = "53f286f78574cfad59fc397a9d3268d345331594"
MONITOR_CANON = "48a0f92b1325e80507594c25e8d78dd28a0f0bf5d624bc1afd6d9d43be56e32c"
CLAIM_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUTH = 26876434389242951065128
STRATA = 17128

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

def locked_json(path: Path, expected_blob: str | None = None, expected_canon: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    if expected_blob is not None:
        req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift {path}")
        req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj

def main() -> None:
    s = locked_json(STATE, STATE_BLOB, STATE_CANON)
    r = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    reg = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    mon = locked_json(MONITOR, MONITOR_BLOB, MONITOR_CANON)
    req(blob(CLAIM_REGISTRY) == CLAIM_BLOB, "claim registry drift")
    req(blob(ACTIVE_FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(LANE_ADAPTERS) == LANE_BLOB, "lane adapters drift")
    req(s["schema"] == "STAGE32_MAIN_COMPACT_STATE_V27_CUT201_CONSUMED_PENDING_REAUDIT", "schema")
    f=s["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA and f["authoritative_remaining_terminals"] == AUTH, "authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["cut201_incremental_rejected_terminals"] == 18758 and f["cut201_incremental_blocks"] == 166, "CUT201 credit")
    req(f["cut201_certlift03_overlap_terminals"] == 6780 and f["cut201_other_consumed_route_overlap_terminals"] == 0, "CUT201 overlap")
    req(f["cut201_double_charge"] is False and f["cut201_main_pruning_credit"] is True, "CUT201 credit firewall")
    req(s["current"]["mainbatch_stop_gate"] == "HOSTILE_REAUDIT_REQUIRED_BEFORE_FURTHER_MAIN_CONSUMPTION", "stop gate")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "re-audit flag")
    for k in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(s["firewalls"][k] is False, f"firewall unexpectedly true: {k}")
    req(r["status"] == "CONSUMED_ON_V27_REPLACEMENT_MAIN_HEAD_PENDING_HOSTILE_REAUDIT", "receipt status")
    req(r["producer_audit"]["audited_exact_head"] == "9b485b4e643b7ed041629547fdb4a867e31c00cd" and r["producer_audit"]["hostile_audit_review_id"] == 5206283218, "adapter audit")
    req(r["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH, "receipt authority")
    byid={d["demand_id"]:d for d in reg["demands"]}
    req(byid["S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"]["status"] == "SATISFIED", "CUT201 demand")
    lanes={x["lane"]:x for x in mon["active_specialists"]}
    req(lanes["CUT"]["pending_main_handoff_ids"] == [], "CUT handoff")
    print("PASS: Stage32 MAIN V27 CUT201 consumption authority; replacement head pending hostile re-audit")
    print(f"remaining_strata={STRATA} remaining_terminals_upper_bound={AUTH}")
    print("CUT201=18758 consumed_once double_charge=false producer_subtraction=false")
    print("FULL178=ACTIVE_INCOMPLETE further_MAIN_consumption=FROZEN merge_authorized=false")
if __name__ == "__main__":
    main()
