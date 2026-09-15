#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "32-01-178/hpadj-08_cut/H8C-03A-V25-MAIN-CONSUMPTION.json"
REBASE = HERE / "32-01-178/hpadj-08_cut/H8C-03A-CURRENT-V24-REBASE.json"
H8C03 = HERE / "32-01-178/hpadj-08_cut/H8C-03A-RESULT.json"
CLAIM_REGISTRY = HERE / "proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "e0c256916815220746b3d53a81044889d8444749"
STATE_CANON = "a818ff8294ec5f2e1b7674b12cd86049b0c41a34dabc9d220d318bb0786aeb74"
RECEIPT_BLOB = "dd55be9ec98345445ced8e86980ec94921d40097"
RECEIPT_CANON = "71976ef4a38d45d1b06374828b16fe9bcf193b99a5c3dcef356f7242d52286a9"
REBASE_BLOB = "0c34d080aa4d067d6cd02436574a14d83d81a5af"
REBASE_CANON = "a3d486a4c5c652e8d31b3abafe81d49f15164dc05253c3ac9fdd28a1db9735fe"
H8C03_BLOB = "37cf76455dc9d29329a730f0facf6f413058712f"
H8C03_CANON = "1e5e0cb7b3ec873c550ca73f3993ab1a06a8da19db745007aa76cc4931cae11a"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LIVE_LANE_ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
REBASE_AUDITED_HEAD = "4392eba5f9d350c4be6dbdd75dd9f320d1f3bc1f"
REBASE_AUDIT_REVIEW = 5207422461
AUTH = 16747313051409592067289
INCREMENT = 10129121337833359022099


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
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    rebase = locked_json(REBASE, REBASE_BLOB, REBASE_CANON)
    h8c03 = locked_json(H8C03, H8C03_BLOB, H8C03_CANON)
    locked_json(CLAIM_REGISTRY, CLAIM_REGISTRY_BLOB)
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    locked_json(LANE_ADAPTERS, LIVE_LANE_ADAPTERS_BLOB)

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_CONSUMED", "schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority")
    req(f["authoritative_remaining_terminals"] == AUTH, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["h8c03a_main_pruning_credit"] is True, "H8C03A consumed credit")
    req(f["h8c03a_incremental_rejected_terminals_lower_bound"] == INCREMENT, "H8C03A increment")
    req(f["h8c03a_current_authority_overlap_accounted"] is True, "H8C03A overlap accounting")
    req(f["h8c03a_double_charge"] is False, "H8C03A double charge")
    req(f["h8c03a_audited_rebase_exact_head"] == REBASE_AUDITED_HEAD, "rebase audit head")
    req(f["h8c03a_hostile_audit_review_id"] == REBASE_AUDIT_REVIEW, "rebase audit review")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    req(f["n372_current_authority_witness"] is False, "stale N372 authority witness")
    req(f["n372_h8c03a_survival_status"] == "NOT_ESTABLISHED_UNDER_CERTIFIED_UPPER_BOUND_ONLY_CONSUMPTION", "N372 status")

    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "replacement-head audit stop gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "re-audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    a = receipt["accounting"]
    req(a["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH, "receipt post authority")
    req(a["certified_incremental_rejected_terminals_lower_bound_consumed"] == INCREMENT, "receipt increment")
    req(a["current_authority_overlap_accounted"] is True and a["double_charge"] is False, "receipt overlap/double-charge")
    req(receipt["promotion"]["main_pruning_credit_consumed"] is True, "receipt promotion")
    req(receipt["promotion"]["claim_dag_changed"] is False, "claim DAG mutation")
    req(receipt["promotion"]["replacement_head_hostile_reaudit_required"] is True, "receipt audit gate")

    s = rebase["set_theoretic_rebase"]
    req(s["h8c03a_incremental_lower_bound_vs_hpadj07_candidate"] == INCREMENT, "rebase increment")
    req(s["candidate_post_rebase_remaining_terminals_upper_bound"] == AUTH, "rebase post authority")
    req(rebase["audit_boundary"]["current_authority_overlap_accounted_candidate"] is True, "rebase overlap candidate")
    req(rebase["audit_boundary"]["double_charge_accounted_candidate"] is True, "rebase double-charge candidate")
    req(h8c03["aggregate"]["h8c03a_rejected_terminals"] == 30842390262547542736909, "H8C03A total")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None and full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier promotion")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit promotion")

    expected_working = [
        "stages/stage32/32-01-178/hpadj-08_cut/H8C-03A-V25-MAIN-CONSUMPTION.json",
        "stages/stage32/32-01-178/hpadj-08_cut/verify_h8c03a_v25_main_consumption.py",
        "stages/stage32/verify_main_startup_authority_v25_h8c03a_consumed.py",
        "stages/stage32/proof/verify_cross_lane_demands.py",
    ]
    req(state["current_leaf_working_set"] == expected_working, "V25 working-set drift")

    print("PASS: Stage32 MAIN V25 H8C-03A consumption boundary")
    print(f"remaining_strata=17128 remaining_terminals_upper_bound={AUTH}")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED heavy_compute_authorized=false merge_authorized=false")


if __name__ == "__main__":
    main()
