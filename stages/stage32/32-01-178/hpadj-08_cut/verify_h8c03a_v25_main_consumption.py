#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
STATE = REPO / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "H8C-03A-V25-MAIN-CONSUMPTION.json"
REBASE = HERE / "H8C-03A-CURRENT-V24-REBASE.json"
H8C03 = HERE / "H8C-03A-RESULT.json"

PRE_HEAD = "c6284abbb29930255892d56f800da0ea1e34734b"
PRE_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
PRE_STATE_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
STATE_BLOB = "e0c256916815220746b3d53a81044889d8444749"
STATE_CANON = "a818ff8294ec5f2e1b7674b12cd86049b0c41a34dabc9d220d318bb0786aeb74"
RECEIPT_BLOB = "dd55be9ec98345445ced8e86980ec94921d40097"
RECEIPT_CANON = "71976ef4a38d45d1b06374828b16fe9bcf193b99a5c3dcef356f7242d52286a9"
REBASE_BLOB = "0c34d080aa4d067d6cd02436574a14d83d81a5af"
REBASE_CANON = "a3d486a4c5c652e8d31b3abafe81d49f15164dc05253c3ac9fdd28a1db9735fe"
H8C03_BLOB = "37cf76455dc9d29329a730f0facf6f413058712f"
H8C03_CANON = "1e5e0cb7b3ec873c550ca73f3993ab1a06a8da19db745007aa76cc4931cae11a"
REBASE_AUDIT_HEAD = "4392eba5f9d350c4be6dbdd75dd9f320d1f3bc1f"
REBASE_AUDIT_REVIEW = 5207422461
PRE_AUTH = 26876434389242951089388
INCREMENT = 10129121337833359022099
POST_AUTH = 16747313051409592067289


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


def locked(path: Path, b: str, c: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if c is not None:
        req(obj.get("canonical_sha256_without_this_field") == c, f"stored canonical drift {path}")
        req(canon(obj) == c, f"canonical drift {path}")
    return obj


def git_head(root: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve pre-V25 checkout head") from exc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre-v25-root", required=True, type=Path)
    args = ap.parse_args()

    state = locked(STATE, STATE_BLOB, STATE_CANON)
    receipt = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    rebase = locked(REBASE, REBASE_BLOB, REBASE_CANON)
    h8c03 = locked(H8C03, H8C03_BLOB, H8C03_CANON)

    pre = args.pre_v25_root.resolve()
    req(pre.is_dir(), "missing pre-V25 checkout")
    req(git_head(pre) == PRE_HEAD, "pre-V25 exact-head drift")
    pre_state = locked(pre / "stages/stage32/MAIN-STATE.json", PRE_STATE_BLOB, PRE_STATE_CANON)
    pre_verifier = pre / "stages/stage32/verify_main_startup_authority_v24_synced.py"
    req(pre_verifier.is_file(), "missing pre-V25 V24 authority verifier")
    replay = subprocess.run(["python", str(pre_verifier)], cwd=pre, text=True, capture_output=True, timeout=60)
    req(replay.returncode == 0, "pre-V25 V24 startup replay failed: " + (replay.stdout + replay.stderr)[-2000:])
    req("PASS: Stage32 MAIN V24 HPADJ07 hostile-audit sync boundary" in replay.stdout, "pre-V25 V24 replay verdict drift")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_CONSUMED", "V25 schema drift")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "V25 strata drift")
    req(f["authoritative_remaining_terminals"] == POST_AUTH, "V25 terminal authority drift")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V25 authority semantics drift")
    req(f["pre_h8c03a_v24_authoritative_remaining_terminals"] == PRE_AUTH, "pre-H8C03A V24 authority drift")
    req(f["h8c03a_incremental_rejected_terminals_lower_bound"] == INCREMENT, "consumed H8C03A increment drift")
    req(f["h8c03a_main_pruning_credit"] is True, "H8C03A MAIN credit missing")
    req(f["h8c03a_current_authority_overlap_accounted"] is True, "H8C03A overlap accounting missing")
    req(f["h8c03a_double_charge"] is False, "H8C03A double charge")
    req(f["h8c03a_audited_rebase_exact_head"] == REBASE_AUDIT_HEAD, "H8C03A audited rebase head drift")
    req(f["h8c03a_hostile_audit_review_id"] == REBASE_AUDIT_REVIEW, "H8C03A rebase audit review drift")
    req(f["n372_current_authority_witness"] is False and f["n372_current_authority_rebased"] is False, "stale N372 current-authority witness")
    req(f["n372_h8c03a_survival_status"] == "NOT_ESTABLISHED_UNDER_CERTIFIED_UPPER_BOUND_ONLY_CONSUMPTION", "N372 H8C03A status drift")

    req(PRE_AUTH - INCREMENT == POST_AUTH, "V24->V25 subtraction identity drift")
    req(receipt["accounting"]["pre_consumption_authoritative_remaining_terminals_upper_bound"] == PRE_AUTH, "receipt pre-authority drift")
    req(receipt["accounting"]["certified_incremental_rejected_terminals_lower_bound_consumed"] == INCREMENT, "receipt increment drift")
    req(receipt["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"] == POST_AUTH, "receipt post-authority drift")
    req(receipt["accounting"]["current_authority_overlap_accounted"] is True, "receipt overlap accounting drift")
    req(receipt["accounting"]["double_charge"] is False, "receipt double-charge drift")
    req(receipt["accounting"]["exact_current_residual_identity_set_claimed"] is False, "receipt exact-residual overclaim")
    req(receipt["promotion"]["main_pruning_credit_consumed"] is True, "receipt MAIN consumption missing")
    req(receipt["promotion"]["claim_dag_changed"] is False, "unexpected claim DAG mutation")
    req(receipt["promotion"]["replacement_head_hostile_reaudit_required"] is True, "receipt replacement audit gate missing")
    req(receipt["promotion"]["further_main_consumption_before_reaudit_forbidden"] is True, "receipt further-consumption gate missing")

    locks = receipt["source_locks"]
    req(locks["pre_consumption_main"]["exact_head"] == PRE_HEAD, "receipt pre-main head drift")
    req(locks["pre_consumption_main"]["main_state_blob_sha1"] == PRE_STATE_BLOB, "receipt pre-main blob drift")
    req(locks["pre_consumption_main"]["main_state_canonical_sha256"] == PRE_STATE_CANON, "receipt pre-main canonical drift")
    req(locks["current_v24_rebase"]["audited_exact_head"] == REBASE_AUDIT_HEAD, "receipt rebase audit head drift")
    req(locks["current_v24_rebase"]["hostile_audit_review_id"] == REBASE_AUDIT_REVIEW, "receipt rebase audit review drift")
    req(rebase["set_theoretic_rebase"]["current_v24_authoritative_remaining_terminals_upper_bound"] == PRE_AUTH, "rebase V24 authority drift")
    req(rebase["set_theoretic_rebase"]["h8c03a_incremental_lower_bound_vs_hpadj07_candidate"] == INCREMENT, "rebase increment drift")
    req(rebase["set_theoretic_rebase"]["candidate_post_rebase_remaining_terminals_upper_bound"] == POST_AUTH, "rebase post-bound drift")
    req(h8c03["aggregate"]["h8c03a_rejected_terminals"] == 30842390262547542736909, "H8C03A total drift")

    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "V25 stop gate drift")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "V25 re-audit firewall missing")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"V25 firewall unexpectedly true: {key}")

    req(pre_state["current_exact_frontier"]["authoritative_remaining_terminals"] == PRE_AUTH, "pre-V25 checked-out authority mismatch")

    print(json.dumps({
        "status": "PASS_H8C03A_V25_MAIN_CONSUMPTION_PENDING_REPLACEMENT_HEAD_REAUDIT",
        "pre_v25_exact_head": PRE_HEAD,
        "pre_v25_remaining_upper_bound": PRE_AUTH,
        "consumed_incremental_lower_bound": INCREMENT,
        "v25_remaining_upper_bound": POST_AUTH,
        "current_authority_overlap_accounted": True,
        "double_charge": False,
        "claim_dag_changed": False,
        "replacement_head_hostile_reaudit_required": True,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
