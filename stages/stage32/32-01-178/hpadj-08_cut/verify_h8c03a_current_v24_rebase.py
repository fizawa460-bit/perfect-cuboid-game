#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

REBASE = HERE / "H8C-03A-CURRENT-V24-REBASE.json"
H8C03 = HERE / "H8C-03A-RESULT.json"
H8C02 = HERE / "H8C-02-RESULT.json"
MAIN_STATE_REL = Path("stages/stage32/MAIN-STATE.json")
HPADJ_CORRECTION = REPO / "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json"
HPADJ_V23_REBASE = REPO / "stages/stage32/management/hpadj-07/proof-chain/CURRENT-V23-CONSERVATIVE-REBASE.json"
HPADJ_CONSUMPTION = REPO / "stages/stage32/management/hpadj-07/HPADJ07-V23-MAIN-CONSUMPTION.json"

REBASE_BLOB = "0c34d080aa4d067d6cd02436574a14d83d81a5af"
REBASE_CANONICAL = "a3d486a4c5c652e8d31b3abafe81d49f15164dc05253c3ac9fdd28a1db9735fe"
H8C03_BLOB = "37cf76455dc9d29329a730f0facf6f413058712f"
H8C03_CANONICAL = "1e5e0cb7b3ec873c550ca73f3993ab1a06a8da19db745007aa76cc4931cae11a"
H8C02_BLOB = "81cfcbe8f9cb9c1c9750be3187e15f61ade3ea9d"
MAIN_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
HPADJ_CORRECTION_BLOB = "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e"
HPADJ_V23_REBASE_BLOB = "8883cfc59a6d48e34d7e256fad15e69714dc02d1"
HPADJ_CONSUMPTION_BLOB = "e942711b67ebc43b39a73ab55bc10862654059f8"

EXPECTED_MAIN_HEAD = "c6284abbb29930255892d56f800da0ea1e34734b"
EXPECTED_H8C03_AUDITED_HEAD = "c656d49fbd210f530d927d19a543d944fbe6b003"
EXPECTED_H8C03_REVIEW = 5207037037


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_locked(path: Path, blob: str) -> dict:
    req(path.is_file(), f"missing source {path}")
    req(git_blob(path) == blob, f"source-lock drift: {path}")
    return json.loads(path.read_text())


def check_canonical(obj: dict, expected: str, label: str) -> None:
    payload = dict(obj)
    stored = payload.pop("canonical_sha256_without_this_field", None)
    req(stored == expected, f"{label} stored canonical drift")
    actual = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    req(actual == expected, f"{label} canonical replay drift")


def exact_head(root: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve pre-V25 MAIN checkout head: " + exc.output.strip()) from exc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre-v25-root", type=Path, default=REPO)
    args = ap.parse_args()

    main_root = args.pre_v25_root.resolve()
    req(main_root.is_dir(), "missing pre-V25 MAIN checkout")
    req(exact_head(main_root) == EXPECTED_MAIN_HEAD, "pre-V25 MAIN exact-head drift")
    main_state_path = main_root / MAIN_STATE_REL

    rebase = load_locked(REBASE, REBASE_BLOB)
    h8c03 = load_locked(H8C03, H8C03_BLOB)
    h8c02 = load_locked(H8C02, H8C02_BLOB)
    main_state = load_locked(main_state_path, MAIN_STATE_BLOB)
    corr = load_locked(HPADJ_CORRECTION, HPADJ_CORRECTION_BLOB)
    old_rebase = load_locked(HPADJ_V23_REBASE, HPADJ_V23_REBASE_BLOB)
    consumption = load_locked(HPADJ_CONSUMPTION, HPADJ_CONSUMPTION_BLOB)

    check_canonical(rebase, REBASE_CANONICAL, "H8C-03A current-V24 rebase")
    check_canonical(h8c03, H8C03_CANONICAL, "H8C-03A RESULT")
    check_canonical(main_state, "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d", "pre-V25 MAIN V24 state")
    check_canonical(corr, "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa", "HPADJ07 correction")
    check_canonical(old_rebase, "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01", "HPADJ07 V23 rebase")
    check_canonical(consumption, "6fc1800b84de587e2218c372966e1424186405e57477586e8a284961f575f417", "HPADJ07 V23 consumption")

    locks = rebase["source_locks"]
    req(locks["current_main"]["exact_head"] == EXPECTED_MAIN_HEAD, "recorded current-main exact head drift")
    req(locks["h8c03a"]["audited_exact_head"] == EXPECTED_H8C03_AUDITED_HEAD, "H8C-03A audited head drift")
    req(locks["h8c03a"]["hostile_audit_review_id"] == EXPECTED_H8C03_REVIEW, "H8C-03A hostile-audit review drift")

    mf = main_state["current_exact_frontier"]
    req(mf["authoritative_remaining_strata"] == 17128, "pre-V25 MAIN stratum authority drift")
    req(mf["authoritative_remaining_terminals"] == 26876434389242951089388, "pre-V25 MAIN terminal upper-bound drift")
    req(mf["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "MAIN terminal semantics drift")
    req(mf["hpadj07_main_pruning_credit"] is True, "HPADJ07 MAIN consumption missing")
    req(main_state["firewalls"]["full178_complete"] is False, "FULL178 unexpectedly complete")

    h = corr["corrected_v22_conservative_replay"]["candidate_rejected_terminals_lower_bound"]
    req(h == 20713268924714183714810, "corrected HPADJ07 V22 lower-bound drift")
    req(h8c02["population_replay"]["hpadj07_rejected_terminals"] == h, "H8C-02 HPADJ07 replay identity drift")
    req(h8c02["mathematics"]["dominates_hpadj07_group_cauchy"] is True, "H8C-02 dominance firewall drift")

    k = h8c03["aggregate"]["h8c03a_rejected_terminals"]
    req(k == 30842390262547542736909, "H8C-03A candidate total drift")
    req(k >= h8c03["aggregate"]["h8c02_rejected_terminals"] >= h, "H8C-03A/H8C-02/HPADJ07 nesting count order drift")
    req(h8c03["aggregate"]["incremental_vs_hpadj07"] == k - h, "H8C-03A increment-vs-HPADJ07 identity drift")

    s = rebase["set_theoretic_rebase"]
    v22 = s["v22_authoritative_remaining_terminals_upper_bound"]
    cert = s["v22_to_v23_certlift03_removed_terminals"]
    v23 = s["v23_pre_hpadj07_authoritative_remaining_terminals_upper_bound"]
    hcons = s["hpadj07_v23_consumed_lower_bound"]
    v24 = s["current_v24_authoritative_remaining_terminals_upper_bound"]
    inc = s["h8c03a_incremental_lower_bound_vs_hpadj07_candidate"]
    post = s["candidate_post_rebase_remaining_terminals_upper_bound"]

    req(v22 == old_rebase["source_locks"]["predecessor_v22"]["authoritative_remaining_terminals"], "V22 authority source drift")
    req(cert == old_rebase["set_theoretic_rebase"]["v22_to_v23_total_removed"] == 154697, "CERTLIFT03 overlap budget drift")
    req(v23 == old_rebase["source_locks"]["current_main_state"]["authoritative_remaining_terminals"], "V23 authority source drift")
    req(hcons == consumption["accounting"]["certified_hpadj07_rejected_terminals_lower_bound_consumed"], "consumed HPADJ07 lower-bound drift")
    req(v24 == consumption["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"], "V24 authority consumption identity drift")
    req(v24 == mf["authoritative_remaining_terminals"], "V24 rebase != pre-V25 MAIN authority")
    req(s["corrected_hpadj07_v22_rejected_lower_bound"] == h, "rebase HPADJ07 V22 lower-bound drift")
    req(s["h8c03a_v22_rejected_lower_bound_candidate"] == k, "rebase H8C-03A V22 lower-bound drift")

    req(v23 == v22 - cert, "V22->V23 subtraction identity drift")
    req(hcons == h - cert, "HPADJ07 conservative overlap subtraction identity drift")
    req(v24 == v23 - hcons, "V23->V24 consumption identity drift")
    req(v24 == v22 - h, "V24 != V22-HPADJ07 algebraic rebase identity")
    req(inc == k - h, "H8C-03A incremental lower-bound identity drift")
    req(post == v24 - inc, "candidate post-rebase subtraction identity drift")
    req(post == v22 - k, "candidate post-rebase != V22-H8C03A identity")
    req(post >= 0, "candidate post-rebase upper bound negative")

    req(s["exact_current_residual_identity_set_claimed"] is False, "exact residual identity-set claim firewall drift")
    req(s["stratum_count_change_claimed"] is False, "stratum-count firewall drift")
    req(s["requires_main_consumption_before_authority_mutation"] is True, "MAIN consumption gate drift")

    audit = rebase["audit_boundary"]
    req(audit["current_authority_overlap_accounted_candidate"] is True, "overlap accounting candidate flag drift")
    req(audit["double_charge_accounted_candidate"] is True, "double-charge accounting candidate flag drift")
    req(audit["main_pruning_credit"] is False, "premature candidate MAIN credit")
    req(audit["hostile_audit_required_before_main_credit"] is True, "hostile-audit gate drift")
    req(audit["claim_sync_required_if_promoted"] is True, "claim-sync gate drift")

    fw = rebase["firewalls"]
    for key in ("main_authority_mutated", "main_pruning_credit", "full178_complete", "effectivity_credit", "receiver_credit", "theorem_credit", "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized"):
        req(fw[key] is False, f"candidate firewall drift: {key}")

    print(json.dumps({
        "status": "PASS_H8C03A_CURRENT_V24_CONSERVATIVE_REBASE_CANDIDATE",
        "pre_v25_main_exact_head_locked": EXPECTED_MAIN_HEAD,
        "h8c03a_hostile_audit_review_id": EXPECTED_H8C03_REVIEW,
        "current_v24_remaining_upper_bound": v24,
        "h8c03a_incremental_lower_bound_vs_consumed_hpadj07_candidate": inc,
        "candidate_post_rebase_remaining_upper_bound": post,
        "current_authority_overlap_accounted_candidate": True,
        "double_charge_accounted_candidate": True,
        "main_pruning_credit": False,
        "hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
