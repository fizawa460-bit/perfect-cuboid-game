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
RECEIPT = HERE / "HPADJ07-V23-MAIN-CONSUMPTION.json"

PRE_HEAD = "8d8f1116d82f873d2cddafdd4d3619fb8649891b"
PRE_STATE_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
PRE_STATE_CANON = "460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
AUDIT_REVIEW = 5191822227
RECEIPT_BLOB = "e942711b67ebc43b39a73ab55bc10862654059f8"
RECEIPT_CANON = "6fc1800b84de587e2218c372966e1424186405e57477586e8a284961f575f417"
STATE_BLOB = "c7fac09b774d8fc75ba3daa1b9320dbb66b81a6d"
STATE_CANON = "22e2ae97041b175bc5901572d2490f6d14ad1dd34cf96687f955679be92e4d12"

PRE = 47589703313957134649501
CREDIT = 20713268924714183560113
POST = 26876434389242951089388
STRATA = 17128

LOCKS = {
    "correction": ("stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json", "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e", "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa"),
    "direction": ("stages/stage32/management/hpadj-07/proof-chain/PRUNING-DIRECTION-CONTRACT-REVIEW.json", "bd1beddf25b505c9f6c7e163606e6156dca10346", "3c6ace29e475f781e6db5a5859578b88b91179a46637c97551391782e85d3e87"),
    "rebase": ("stages/stage32/management/hpadj-07/proof-chain/CURRENT-V23-CONSERVATIVE-REBASE.json", "8883cfc59a6d48e34d7e256fad15e69714dc02d1", "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01"),
    "wall": ("stages/stage32/management/hpadj-07/CARRIER-REALIZATION-WALL.json", "e4a35aa9bdd174ac64162839ec391cd57f7d9315", "79598cf3649be2d86771ea9f90d748a51028d348c672dc258424db025a39b303"),
}

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

def head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-v23-root", required=True, type=Path)
    a = ap.parse_args()
    pred = a.audited_v23_root.resolve()

    req(pred.is_dir(), "missing hostile-audited V23 checkout")
    req(head(pred) == PRE_HEAD, "hostile-audited V23 exact head drift")

    pstate = locked_json(pred / "stages/stage32/MAIN-STATE.json", PRE_STATE_BLOB, PRE_STATE_CANON)
    pf = pstate["current_exact_frontier"]
    req(pstate["schema"] == "STAGE32_MAIN_COMPACT_STATE_V23_CERTLIFT03_CONSUMED", "predecessor V23 schema")
    req(pf["authoritative_remaining_strata"] == STRATA, "predecessor strata")
    req(pf["authoritative_remaining_terminals"] == PRE, "predecessor terminal authority")
    req(pf["certlift03_main_pruning_credit"] is True, "predecessor CERTLIFT03 credit")
    req(pf["full178_numerical_census_complete"] is False and pf["stage32_closed"] is False, "predecessor closure drift")

    locked = {}
    for name, (rel, b, c) in LOCKS.items():
        locked[name] = locked_json(pred / rel, b, c)

    rebase = locked["rebase"]["set_theoretic_rebase"]
    req(rebase["therefore_current_v23_hpadj_rejected_lower_bound"] == CREDIT, "audited HPADJ V23 lower bound")
    req(rebase["candidate_remaining_upper_bound_if_corrected_hpadj_promoted"] == POST, "audited HPADJ candidate remainder")
    req(rebase["requires_exact_overlap_for_exact_increment"] is False, "audited overlap contract")
    req(rebase["sufficient_for_safe_lower_bound_credit_after_audit"] is True, "audited safe-credit contract")
    req(locked["correction"]["firewalls"]["main_pruning_credit"] is False, "predecessor correction was prematurely credited")
    req(locked["direction"]["firewalls"]["main_pruning_credit"] is False, "predecessor direction was prematurely credited")
    req(locked["wall"]["promotion_gate"]["explicit_main_consumption_required"] is True, "predecessor consumption gate missing")
    req(locked["wall"]["promotion_gate"]["main_authority_mutation_allowed_now"] is False, "predecessor wall already mutated authority")

    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    req(receipt["hostile_audit_source"]["audited_exact_head"] == PRE_HEAD, "receipt predecessor head")
    req(receipt["hostile_audit_source"]["hostile_audit_review_id"] == AUDIT_REVIEW, "receipt audit review")
    req(receipt["hostile_audit_source"]["hostile_audit_status"] == "PASS", "receipt audit status")
    acct = receipt["accounting"]
    req(acct["pre_v23_authoritative_remaining_terminals"] == PRE, "receipt pre authority")
    req(acct["certified_hpadj07_rejected_terminals_lower_bound_consumed"] == CREDIT, "receipt credit")
    req(acct["post_consumption_certified_remaining_terminals_upper_bound"] == POST, "receipt post authority")
    req(PRE - CREDIT == POST, "arithmetic identity")
    req(acct["double_charge"] is False, "receipt double charge")
    req(acct["exact_v23_hpadj_overlap_required"] is False, "receipt exact-overlap contract")
    req(acct["remaining_terminal_authority_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "receipt authority semantics")
    req(receipt["promotion"]["main_pruning_credit_consumed"] is True, "receipt MAIN credit not consumed")
    req(receipt["promotion"]["replacement_head_hostile_reaudit_required"] is True, "receipt re-audit gate")
    req(all(v is False for v in receipt["firewalls"].values()), "receipt broad-credit firewall")

    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_LOWER_BOUND_CONSUMED", "V24 schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "V24 strata")
    req(f["authoritative_remaining_terminals"] == POST, "V24 terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V24 authority semantics")
    req(f["pre_hpadj07_v23_authoritative_remaining_terminals"] == PRE, "V24 predecessor terminal authority")
    req(f["hpadj07_certified_rejected_terminals_lower_bound"] == CREDIT, "V24 HPADJ credit")
    req(f["hpadj07_main_pruning_credit"] is True, "V24 HPADJ MAIN credit")
    req(f["hpadj07_double_charge"] is False and f["hpadj07_exact_overlap_required"] is False, "V24 accounting firewall")
    req(f["hpadj07_hostile_audit_review_id"] == AUDIT_REVIEW and f["hpadj07_audited_exact_head"] == PRE_HEAD, "V24 audit provenance")
    req(f["n372_survives_hpadj07"] is True, "N372 preservation")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "V24 closure overclaim")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "V24 re-audit firewall")
    req(state["firewalls"]["merge_authorized"] is False, "V24 merge firewall")

    sl = state["source_locks"]["hpadj07_v23_consumption"]
    req(sl["predecessor_exact_head"] == PRE_HEAD, "state predecessor head lock")
    req(sl["predecessor_main_state_blob_sha1"] == PRE_STATE_BLOB, "state predecessor blob lock")
    req(sl["hostile_audit_review_id"] == AUDIT_REVIEW, "state audit review lock")
    req(sl["consumption_receipt_blob_sha1"] == RECEIPT_BLOB, "state receipt blob lock")
    req(sl["consumption_receipt_canonical_sha256"] == RECEIPT_CANON, "state receipt canonical lock")

    print(json.dumps({"verdict":"PASS_HPADJ07_V23_LOWER_BOUND_MAIN_CONSUMPTION_CANDIDATE","pre":PRE,"consumed_lower_bound":CREDIT,"post_certified_upper_bound":POST,"remaining_strata":STRATA,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
