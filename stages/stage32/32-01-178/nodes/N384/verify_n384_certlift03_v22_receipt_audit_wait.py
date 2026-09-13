#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_N383_BLOB = "c2b3d3fa82606cebf261ba4ea4652c1fcad3a867"
EXPECTED_N383_CANONICAL = "f12b8a4696d2e82f8541f89fcb80ee47243443dacc2c26df072a4831ac4b7182"
EXPECTED_N384_CANONICAL = "ce2523230b4e13bb3be270265881e73c5a50bd1f4815e8e6a6380472978b1a6e"
EXPECTED_PRODUCER_STATE_BLOB = "34fb494810906faaee3678294d852b386c65db8b"
EXPECTED_RECEIPT_BLOB = "291bb8b125566bb72c1caae0537dff2625219ffb"
EXPECTED_RECEIPT_CANONICAL = "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858"
EXPECTED_HANDOFF_BLOB = "4c5096e4de8ccee478c8ea10ed1b6858df533583"
EXPECTED_V22_MAIN_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def check_blob(path: Path, expected: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == expected, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", required=True)
    ap.add_argument("--v22-main-root", required=True)
    args = ap.parse_args()

    cert = Path(args.certlift_root)
    v22 = Path(args.v22_main_root)

    n383_path = HERE.parent / "N383" / "STATE.json"
    n384_path = HERE / "STATE.json"
    check_blob(n383_path, EXPECTED_N383_BLOB, "N383 state")
    n383 = load(n383_path)
    req(canonical(n383) == EXPECTED_N383_CANONICAL, "N383 canonical drift")

    n384 = load(n384_path)
    req(canonical(n384) == EXPECTED_N384_CANONICAL, "N384 canonical drift")
    req(n384["canonical_sha256_without_this_field"] == EXPECTED_N384_CANONICAL, "N384 stored canonical drift")
    req(n384["status"] == "CERTLIFT03_V22_ADAPTER_RECEIPT_RETAINED_READY_FOR_HOSTILE_AUDIT_NO_CREDIT", "N384 status drift")

    state_path = cert / "stages/stage32/cut-cert-lift/STATE.json"
    receipt_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json"
    handoff_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-HANDOFF.json"
    audit_pass_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json"
    check_blob(state_path, EXPECTED_PRODUCER_STATE_BLOB, "producer state")
    check_blob(receipt_path, EXPECTED_RECEIPT_BLOB, "V22 receipt")
    check_blob(handoff_path, EXPECTED_HANDOFF_BLOB, "V22 hostile-audit handoff")
    req(not audit_pass_path.exists(), "snapshot unexpectedly contains V22 adapter hostile-audit PASS")

    state = load(state_path)
    receipt = load(receipt_path)
    handoff = load(handoff_path)

    req(state["active_node"] == "CERTLIFT-03_V22_CONSUMPTION_ADAPTER_CANDIDATE_PENDING_HOSTILE_AUDIT", "producer active node drift")
    v22a = state["v22_consumption_adapter"]
    req(v22a["status"] == "PASS_EXACT_HOSTILE_AUDITED_V22_CONSUMPTION_ADAPTER_CANDIDATE_PENDING_HOSTILE_AUDIT", "producer V22 status drift")
    req(v22a["candidate_exact_head"] == "5f6b98f28568e840aee9e639cce6d334c56b49c2", "candidate exact head drift")
    req(v22a["adapter_canonical"] == "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf", "adapter canonical drift")
    req(v22a["candidate_incremental_blocks"] == 1369, "producer incremental block drift")
    req(v22a["candidate_incremental_terminals"] == 154697, "producer incremental terminal drift")
    req(v22a["prior_authority_overlap"]["union_blocks"] == 308, "producer overlap union drift")
    req(v22a["prior_authority_overlap"]["double_charge"] is False, "producer double-charge drift")
    req(v22a["adapter_hostile_audited"] is False, "producer V22 adapter unexpectedly audited")
    req(v22a["main_authority_mutated"] is False and v22a["main_pruning_credit"] is False, "producer credit firewall drift")

    req(receipt["status"] == "V22_ADAPTER_CANDIDATE_PASS_PENDING_HOSTILE_AUDIT", "receipt status drift")
    req(receipt["canonical_sha256_without_this_field"] == EXPECTED_RECEIPT_CANONICAL, "receipt stored canonical drift")
    req(canonical(receipt) == EXPECTED_RECEIPT_CANONICAL, "receipt canonical replay drift")
    req(receipt["adapter_blob_sha1"] == "327aa601acad47bc1e486cccbbac3d3dee7c2681", "receipt adapter blob drift")
    req(receipt["adapter_canonical_sha256"] == "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf", "receipt adapter canonical drift")
    req(receipt["exact_head"] == "5f6b98f28568e840aee9e639cce6d334c56b49c2", "receipt evidence head drift")
    req(receipt["exact_head_ci_run"] == 34728296585 and receipt["exact_head_ci_job"] == 103646309512, "receipt CI source drift")
    req(receipt["population"]["target_blocks"] == 1677, "receipt target drift")
    req(receipt["prior_authority_overlap"]["union_blocks"] == 308, "receipt overlap drift")
    req(receipt["prior_authority_overlap"]["double_charge"] is False, "receipt double-charge drift")
    req(receipt["candidate_increment"]["incremental_blocks"] == 1369, "receipt increment blocks drift")
    req(receipt["candidate_increment"]["incremental_terminals"] == 154697, "receipt increment terminals drift")
    req(receipt["candidate_increment"]["candidate_remaining_terminals_if_later_consumed"] == 47589703313957134649501, "receipt remainder drift")
    req(not any(receipt["firewall"].values()), "receipt firewall regression")

    req(handoff["status"] == "READY_FOR_HOSTILE_AUDIT_NOT_AUDITED", "handoff status drift")
    req(handoff["receipt_blob_sha1"] == EXPECTED_RECEIPT_BLOB, "handoff receipt blob drift")
    req(handoff["receipt_canonical_sha256"] == EXPECTED_RECEIPT_CANONICAL, "handoff receipt canonical drift")
    req(handoff["receipt_replay_enrolled_in_active_auto_ci"] is True, "handoff receipt CI enrollment drift")
    req(handoff["expected_population"]["incremental_blocks"] == 1369, "handoff increment blocks drift")
    req(handoff["expected_population"]["incremental_terminals"] == 154697, "handoff increment terminals drift")
    req(not any(handoff["credit_firewall"].values()), "handoff firewall regression")

    v22_state_path = v22 / "stages/stage32/MAIN-STATE.json"
    check_blob(v22_state_path, EXPECTED_V22_MAIN_BLOB, "V22 MAIN state")
    main_state = load(v22_state_path)
    req(main_state["canonical_sha256_without_this_field"] == "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c", "V22 MAIN canonical drift")
    req(main_state["current_exact_frontier"]["authoritative_remaining_terminals"] == 47589703313957134804198, "V22 MAIN authority drift")
    req(main_state["current_exact_frontier"]["full178_numerical_census_complete"] is False, "V22 FULL178 unexpectedly complete")

    p = n384["promotion_boundary"]
    req(p["receipt_retained"] is True and p["receipt_exact_result_matches_n383_replay"] is True, "N384 receipt promotion drift")
    req(p["hostile_audit_handoff_ready"] is True and p["hostile_audit_pass"] is False, "N384 audit wait drift")
    req(p["v22_increment_consumable_now"] is False and p["subtract_154697_now"] is False, "N384 early consumption regression")
    req(p["main_authority_mutation_allowed_now"] is False, "N384 MAIN mutation regression")
    req(n384["n101_contract"]["remains_stopped"] is True, "N101 stop lost")
    req(not any(n384["anti_loop"].values()), "N384 anti-loop regression")
    req(not any(n384["credit"].values()), "N384 credit firewall regression")

    print(json.dumps({
        "hostile_audit_handoff_ready": True,
        "hostile_audit_pass": False,
        "incremental_blocks": 1369,
        "incremental_terminals": 154697,
        "main_pruning_credit": False,
        "n101_reopened_credit": False,
        "next_gate": n384["next_gate"],
        "receipt_canonical": EXPECTED_RECEIPT_CANONICAL,
        "verdict": "PASS_N384_CERTLIFT03_V22_RECEIPT_RETAINED_HOSTILE_AUDIT_WAIT_BOUNDARY"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
