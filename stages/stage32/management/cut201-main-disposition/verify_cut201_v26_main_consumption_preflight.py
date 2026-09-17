#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "CUT201-V27-MAIN-CONSUMPTION.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
REGISTRY = ROOT / "stages/stage32/proof/CROSS-LANE-DEMANDS.json"
CLAIM_REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"
RECEIPT_BLOB = "cdd766cae064430bb1aa901f1d023fcb48b39877"
RECEIPT_CANON = "aa9a40c0514412444a15db8a59d54de4866de39345ff4a0dbd531c14eaced9f6"
STATE_BLOB = "399221dc91733b3a9a2d79ae3473ea2365e409a3"
STATE_CANON = "e25d3c2d3381193462af28577c6ddd0c6c5fc597192a640d7534034213b86d1b"
REGISTRY_BLOB = "e14bea1a62ec287710064a96f80abe57f8b0c3f4"
REGISTRY_CANON = "9a30646b5567adb30f0192b43f89a8d8a01d1464199b2f0a0d19e1138a7d9c74"
CLAIM_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUTH_BEFORE = 26876434389242951083886
CREDIT = 18758
AUTH_AFTER = 26876434389242951065128
DEMAND_ID = "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"

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
    r = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    s = locked_json(STATE, STATE_BLOB, STATE_CANON)
    reg = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    req(blob(CLAIM_REGISTRY) == CLAIM_BLOB, "claim registry drift")
    req(blob(ACTIVE_FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(LANE_ADAPTERS) == LANE_BLOB, "lane adapters drift")
    a = r["accounting"]
    req(a["pre_consumption_certified_remaining_terminals_upper_bound"] == AUTH_BEFORE, "authority before")
    req(a["credited_incremental_rejected_terminals"] == CREDIT, "credit")
    req(a["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH_AFTER, "authority after")
    req(a["source_candidate_terminals"] == 25538 and a["certlift03_exact_overlap_terminals"] == 6780, "partition counts")
    req(a["other_consumed_route_overlap_terminals"] == 0 and a["double_charge"] is False, "no-double-charge")
    req(a["consume_exactly_once"] is True, "consume exactly once")
    req(a["producer_lane_authority_subtraction_performed"] is False and a["main_consumer_authority_subtraction_performed"] is True, "lane ownership")
    f = s["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata")
    req(f["authoritative_remaining_terminals"] == AUTH_AFTER, "MAIN authority")
    req(f["cut201_incremental_rejected_terminals"] == CREDIT and f["cut201_main_pruning_credit"] is True, "MAIN CUT201 credit")
    req(f["cut201_double_charge"] is False, "MAIN double charge")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement re-audit gate")
    req(s["current"]["mainbatch_stop_gate"] == "HOSTILE_REAUDIT_REQUIRED_BEFORE_FURTHER_MAIN_CONSUMPTION", "stop gate")
    byid = {d["demand_id"]: d for d in reg["demands"]}
    req(byid[DEMAND_ID]["status"] == "SATISFIED", "CUT201 demand not satisfied")
    sat = byid[DEMAND_ID]["satisfying_artifact"]
    req(sat["audited_exact_head"] == "9b485b4e643b7ed041629547fdb4a867e31c00cd" and sat["audit_review_id"] == 5206283218, "demand audit identity")
    consumed = [x for x in reg["audited_result_consumption"] if x.get("demand_id") == DEMAND_ID]
    req(len(consumed) == 1 and consumed[0]["credited_incremental_rejected_terminals"] == CREDIT, "CUT201 consumption ledger cardinality")
    req(consumed[0]["main_consumed"] is True and consumed[0]["double_charge"] is False, "CUT201 ledger")
    for k in ("effectivity_credit","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","stage32_closed","theorem_credit"):
        req(r["firewalls"][k] is False, f"receipt firewall {k}")
    print("PASS: CUT201 V26 audited adapter consumed exactly once by MAIN V27; 18,758 terminals credited; replacement head frozen for hostile re-audit")
if __name__ == "__main__":
    main()
