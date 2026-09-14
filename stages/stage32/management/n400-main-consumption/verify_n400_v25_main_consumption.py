#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "N400-V25-MAIN-CONSUMPTION.json"
AUDIT_RECEIPT = HERE / "N400-HOSTILE-AUDIT-PASS-RECEIPT.json"
REGISTRY = ROOT / "stages/stage32/proof/CROSS-LANE-DEMANDS.json"
MONITOR = ROOT / "stages/stage32/proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
SYNTHESIS = ROOT / "stages/stage32/proof/PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json"
CLAIM_REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
CLAIM_SYNC = ROOT / "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"

PRE_HEAD = "23a6512e0e14b98439e4c04d0c4367fb779359a5"
PRE_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
PRE_STATE_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
N400_HEAD = "b1a950cbc6edf3cb85e1ea79473105c6f1f67b03"
N400_REVIEW = 5203374607
N400_RESULT_BLOB = "485c9a0380788bedd25cde5a47204e2c8c62472e"
N400_RESULT_CANON = "8459cd213cca964718b36c4bce7006439c85a2527943441ede1f286a7eb56dcb"
N400_STATE_BLOB = "c6fb6f55e026be9c87f5e825a18d114ce0dd3d23"
N400_STATE_CANON = "eabea6689d7fc92542eb5a417e1467dba4bf3ce7cb69613fd6dff4d5e52fd342"
N400_VERIFIER_BLOB = "6898ea22458d2156944569dc598eb5b7ebb0048e"
AUDIT_RECEIPT_BLOB = "c43a50a417cb62228860c0c230a27110939ed6e7"
AUDIT_RECEIPT_CANON = "201422333dd02f1e15c8fc9bb59b332651905f8b21c2d4cd9fa8c67005f1ccbb"
RECEIPT_BLOB = "e0eb8e7d0364dc11df0568d7bbd820488cd44678"
RECEIPT_CANON = "2b6d8d3c3f6eec99def1ee29d65e9a53d610c2c4696de4301d16ec37241ff205"
STATE_BLOB = "c6debd246e0a7f5bac2f5cce6c1d3cf80de3918c"
STATE_CANON = "82a0835b40910b1b3460f55da9d8d19e6252a919b43096772d54d62a41353cd2"
REGISTRY_BLOB = "454eca60149ae5c3121f79567d6b4a782d373369"
REGISTRY_CANON = "600e877e1d0764c4ac0687282d2836707e06b55d6248cf7a0c6fe5b845842161"
MONITOR_BLOB = "344aeaccb0c655f2e1def290eb68dab834aa5105"
SYNTHESIS_BLOB = "e41ee562f8a940ad5041d2d5e64228f2ada7a207"
SYNTHESIS_CANON = "20defc105e39fedaaf5243de55bf0c496ffa997566fec582595847da5a02c2ca"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
CLAIM_SYNC_BLOB = "bbab1b565afbd2e767fc6cc4325c5167d42919b4"
PRE = 26876434389242951089388
CREDIT = 5502
POST = 26876434389242951083886
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

def locked_json(path: Path, b: str, c: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if c is not None:
        req(obj.get("canonical_sha256_without_this_field") == c, f"stored canonical drift {path}")
        req(canon(obj) == c, f"canonical drift {path}")
    return obj

def head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def find_claim(node, claim_id: str):
    if isinstance(node, dict):
        if node.get("claim_id") == claim_id:
            return node
        for value in node.values():
            found = find_claim(value, claim_id)
            if found is not None:
                return found
    elif isinstance(node, list):
        for value in node:
            found = find_claim(value, claim_id)
            if found is not None:
                return found
    return None

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--predecessor-main-root", required=True, type=Path)
    ap.add_argument("--n400-audited-root", required=True, type=Path)
    args = ap.parse_args()

    pred = args.predecessor_main_root.resolve()
    prod = args.n400_audited_root.resolve()
    req(head(pred) == PRE_HEAD, "predecessor MAIN exact head drift")
    req(head(prod) == N400_HEAD, "N400 audited exact head drift")
    pstate = locked_json(pred / "stages/stage32/MAIN-STATE.json", PRE_STATE_BLOB, PRE_STATE_CANON)
    req(pstate["current_exact_frontier"]["authoritative_remaining_terminals"] == PRE, "predecessor terminal authority")
    req(pstate["current_exact_frontier"]["authoritative_remaining_strata"] == STRATA, "predecessor strata")
    req(pstate["firewalls"]["merge_authorized"] is False, "predecessor merge firewall")

    presult = locked_json(prod / "stages/stage32/32-01-178/nodes/N400/RESULT.json", N400_RESULT_BLOB, N400_RESULT_CANON)
    pnode = locked_json(prod / "stages/stage32/32-01-178/nodes/N400/STATE.json", N400_STATE_BLOB, N400_STATE_CANON)
    req(blob(prod / "stages/stage32/32-01-178/nodes/N400/verify_n400_n399_compact_main_consumption_handoff.py") == N400_VERIFIER_BLOB, "N400 verifier blob drift")
    cert = presult["certificate"]
    req(cert["source_terminal_count"] == 10961, "N400 source population")
    req(cert["rejected_terminal_count"] == CREDIT, "N400 rejected count")
    req(cert["rejected_terminal_rank_stream_sha256"] == "6648c3a246b71f74dec275012f0218d8a44477cd756229e6e3bc3eda965ca262", "N400 rejected stream")
    req(cert["prior_consumed_v24_overlap_terminal_count"] == 0, "N400 prior overlap")
    req(cert["double_charge"] is False and cert["eligible_for_separate_main_consumption"] is True, "N400 no-double-charge eligibility")
    req(presult["route_control"]["main_authority_subtraction_performed"] is False, "178 producer performed subtraction")
    req(pnode["result_summary"]["main_authority_subtraction_performed"] is False, "178 state performed subtraction")

    ar = locked_json(AUDIT_RECEIPT, AUDIT_RECEIPT_BLOB, AUDIT_RECEIPT_CANON)
    req(ar["audit"]["status"] == "PASS" and ar["audit"]["review_id"] == N400_REVIEW, "retained N400 audit receipt")
    req(ar["audit"]["audited_exact_head"] == N400_HEAD, "retained N400 audited head")

    registry = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    demands = {d["demand_id"]: d for d in registry["demands"]}
    req(demands["S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"]["status"] == "OBSOLETE", "N398 demand not superseded")
    n400d = demands["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]
    req(n400d["status"] == "SATISFIED", "N400 demand not satisfied")
    req(n400d["satisfying_artifact"]["audit_review_id"] == N400_REVIEW, "N400 demand audit review")
    req(n400d["source_population_semantics"]["double_charge"] is False, "N400 demand double charge")
    consumed = [x for x in registry["audited_result_consumption"] if x.get("result_id") == "S32.N400.N396_REJECTED_5502.COMPACT_MAIN_CONSUMPTION.V1"]
    req(len(consumed) == 1, "N400 must appear exactly once in consumption ledger")
    req(consumed[0]["credited_incremental_rejected_terminals"] == CREDIT, "N400 ledger credit")
    req(consumed[0]["producer_lane_subtraction_performed"] is False, "producer-lane subtraction in ledger")

    req(blob(MONITOR) == MONITOR_BLOB, "active specialist monitor drift")
    synthesis = locked_json(SYNTHESIS, SYNTHESIS_BLOB, SYNTHESIS_CANON)
    req(synthesis["status"] == "SUPERSEDED_BY_AUDITED_N400_MAIN_CONSUMPTION", "parity synthesis supersession drift")
    req(all(x["status"] == "NOT_PROVED" for x in synthesis["required_comparisons"]), "unresolved cross-population comparison promoted")

    req(blob(CLAIM_REGISTRY) == CLAIM_REGISTRY_BLOB, "claim registry drift")
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    req(blob(CLAIM_SYNC) == CLAIM_SYNC_BLOB, "claim sync contract drift")
    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None and full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 claim status overpromotion")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 goal audit overpromotion")

    rec = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    acct = rec["accounting"]
    req(acct["pre_consumption_certified_remaining_terminals_upper_bound"] == PRE, "receipt pre authority")
    req(acct["credited_incremental_rejected_terminals"] == CREDIT, "receipt credit")
    req(acct["post_consumption_certified_remaining_terminals_upper_bound"] == POST, "receipt post authority")
    req(PRE - CREDIT == POST, "exact subtraction arithmetic")
    req(acct["prior_consumed_v24_overlap_terminal_count"] == 0 and acct["double_charge"] is False, "receipt double-charge")
    req(acct["consume_exactly_once"] is True, "receipt consume-once")
    req(acct["producer_lane_authority_subtraction_performed"] is False, "producer subtraction receipt")
    req(acct["main_consumer_authority_subtraction_performed"] is True, "MAIN consumer subtraction missing")
    req(rec["claim_sync"]["claim_semantics_changed"] is False and rec["claim_sync"]["claim_status_changed"] is False, "claim core/status should remain unchanged")
    req(rec["claim_sync"]["frontier_status_after"] == "ACTIVE_INCOMPLETE", "claim frontier status")

    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_N400_CONSUMED_AUDIT_REQUIRED", "V25 schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "V25 strata")
    req(f["authoritative_remaining_terminals"] == POST, "V25 terminal authority")
    req(f["n400_incremental_rejected_terminals"] == CREDIT and f["n400_main_pruning_credit"] is True, "V25 N400 credit")
    req(f["n400_prior_consumed_v24_overlap_terminal_count"] == 0 and f["n400_double_charge"] is False, "V25 N400 accounting")
    req(f["n400_producer_lane_subtraction_performed"] is False and f["n400_main_consumer_subtraction_performed"] is True, "V25 lane ownership")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "V25 closure overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "HOSTILE_AUDIT_V25_N400_MAIN_CONSUMPTION", "replacement head not frozen")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement hostile audit gate")
    for key in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(state["firewalls"][key] is False, f"broad firewall opened: {key}")

    print(json.dumps({"verdict":"PASS_N400_V25_MAIN_CONSUMPTION","pre":PRE,"consumed":CREDIT,"post":POST,"remaining_strata":STRATA,"double_charge":False,"producer_subtraction":False,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
