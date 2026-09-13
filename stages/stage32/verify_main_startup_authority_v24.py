#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/hpadj-07/HPADJ07-V23-MAIN-CONSUMPTION.json"

STATE_BLOB = "c7fac09b774d8fc75ba3daa1b9320dbb66b81a6d"
STATE_CANON = "22e2ae97041b175bc5901572d2490f6d14ad1dd34cf96687f955679be92e4d12"
RECEIPT_BLOB = "e942711b67ebc43b39a73ab55bc10862654059f8"
RECEIPT_CANON = "6fc1800b84de587e2218c372966e1424186405e57477586e8a284961f575f417"
PRE_HEAD = "8d8f1116d82f873d2cddafdd4d3619fb8649891b"
AUDIT_REVIEW = 5191822227
PRE = 47589703313957134649501
CREDIT = 20713268924714183560113
POST = 26876434389242951089388

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

def locked(path: Path, b: str, c: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == c, f"stored canonical drift {path}")
    req(canon(obj) == c, f"canonical drift {path}")
    return obj

def main() -> None:
    s = locked(STATE, STATE_BLOB, STATE_CANON)
    r = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)

    req(s["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_LOWER_BOUND_CONSUMED", "schema")
    f = s["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority")
    req(f["authoritative_remaining_terminals"] == POST, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "terminal authority semantics")
    req(f["pre_hpadj07_v23_authoritative_remaining_terminals"] == PRE, "predecessor authority")
    req(f["hpadj07_certified_rejected_terminals_lower_bound"] == CREDIT, "HPADJ07 lower bound")
    req(f["hpadj07_main_pruning_credit"] is True, "HPADJ07 MAIN credit")
    req(f["hpadj07_double_charge"] is False, "HPADJ07 double charge")
    req(f["hpadj07_exact_overlap_required"] is False, "HPADJ07 overlap contract")
    req(f["hpadj07_stratum_count_change_claimed"] is False, "stratum overclaim")
    req(f["hpadj07_audited_exact_head"] == PRE_HEAD, "HPADJ07 predecessor audit head")
    req(f["hpadj07_hostile_audit_review_id"] == AUDIT_REVIEW, "HPADJ07 audit review")
    req(f["n372_survives_hpadj07"] is True and f["n372_main_pruning_credit"] is False, "N372 firewall")
    req(f["certlift03_main_pruning_credit"] is True and f["certlift03_incremental_rejected_terminals"] == 154697, "CERTLIFT03 retained credit")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    req(s["current"]["mainbatch_stop_gate"] == "V24_HPADJ07_REPLACEMENT_HEAD_HOSTILE_REAUDIT", "stop gate")
    req(s["current"]["next_exact_route"] == "STAGE32AUDIT_V24_HPADJ07_LOWER_BOUND_CONSUMPTION", "next route")
    req(s["authority_sync"]["predecessor_v23_exact_head"] == PRE_HEAD, "predecessor head")
    req(s["authority_sync"]["predecessor_v23_hostile_audit_review_id"] == AUDIT_REVIEW, "audit review")
    req(s["authority_sync"]["hpadj07_main_pruning_credit_consumed"] is True, "authority sync HPADJ credit")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "re-audit firewall")
    for key in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(s["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    acct = r["accounting"]
    req(r["hostile_audit_source"]["audited_exact_head"] == PRE_HEAD, "receipt audit head")
    req(r["hostile_audit_source"]["hostile_audit_review_id"] == AUDIT_REVIEW, "receipt audit review")
    req(acct["pre_v23_authoritative_remaining_terminals"] == PRE, "receipt pre")
    req(acct["certified_hpadj07_rejected_terminals_lower_bound_consumed"] == CREDIT, "receipt credit")
    req(acct["post_consumption_certified_remaining_terminals_upper_bound"] == POST, "receipt post")
    req(PRE - CREDIT == POST, "receipt arithmetic")
    req(acct["double_charge"] is False, "receipt double charge")
    req(r["promotion"]["main_pruning_credit_consumed"] is True, "receipt promotion")
    req(r["promotion"]["replacement_head_hostile_reaudit_required"] is True, "receipt re-audit gate")
    req(all(v is False for v in r["firewalls"].values()), "receipt broad-credit firewall")

    print("PASS: Stage32 MAIN V24 HPADJ07 lower-bound consumption authority")
    print(f"remaining_strata=17128 remaining_terminals_upper_bound={POST} consumed_hpadj07_lower_bound={CREDIT}")
    print("FULL178=false Stage32_closed=false replacement_head_hostile_reaudit_required=true merge_authorized=false")

if __name__ == "__main__":
    main()
