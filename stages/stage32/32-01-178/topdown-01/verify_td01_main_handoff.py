#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "TD01-HOSTILE-AUDIT-PASS.json"
HANDOFF = HERE / "MAIN-HANDOFF.json"
STATE = HERE / "STATE.json"
AUDIT_HANDOFF = HERE / "AUDIT-HANDOFF.json"
PACKET = HERE / "EXACT-X4-ENVELOPE-BOUND.json"

RECEIPT_BLOB = "cf00fb61435d198a1f033306190647331f9884f7"
RECEIPT_CANON = "9ae9e53c93c761aff3144443a9e63ee82dab71a9767eaaae1f5e3256220da41c"
HANDOFF_BLOB = "19d0ba1005ee149b405e87b97c10a42409e0998a"
HANDOFF_CANON = "09b1bb55b8bdfbe844258d8ad7d112d78c25c4397f08675c9c4c3b1f4a000469"
STATE_BLOB = "26f55629483a843bc41d0be9b27a074908b4b8d2"
STATE_CANON = "5175a23ee481c145171d50ac794e4e9c191c51b2695cafad7cc5d7cbe06a2108"
AUDIT_HANDOFF_BLOB = "f0195a7fc6a682a09979869f7d9ba515e55d30af"
AUDIT_HANDOFF_CANON = "fc20d86b534e1a49f30d7896137bd8657df837c28fc07d97219a97e08667f5b5"
PACKET_BLOB = "51271c11078459ad9171138c4fb6121d7a665c39"
PACKET_CANON = "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d"

AUDITED_HEAD = "54945927416a94a67533c7b06c59c5a24e50c4f1"
AUDIT_REVIEW_ID = 5214778974
CI_RUN_ID = 34979035686
CI_JOB_ID = 104414192160
DEMAND_ID = "S32.DEMAND.TD01.178.MAIN.AUDITED_BOUND_HANDOFF.V1"
CANDIDATE = 3453268626299532038131
ENVELOPE = 6703403803993209250491
TIGHTENING = 3250135177693678063363
RULE = "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj


def main() -> None:
    receipt = locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "TD01 audit PASS receipt")
    handoff = locked(HANDOFF, HANDOFF_BLOB, HANDOFF_CANON, "TD01 MAIN handoff")
    state = locked(STATE, STATE_BLOB, STATE_CANON, "TD01 state")
    audit_handoff = locked(AUDIT_HANDOFF, AUDIT_HANDOFF_BLOB, AUDIT_HANDOFF_CANON, "TD01 audit handoff")
    packet = locked(PACKET, PACKET_BLOB, PACKET_CANON, "TD01 exact bound packet")

    ha = receipt["hostile_audit"]
    req(receipt["status"] == "HOSTILE_AUDIT_PASS", "audit receipt status")
    req(ha["audited_exact_head"] == AUDITED_HEAD, "audited head drift")
    req(ha["review_id"] == AUDIT_REVIEW_ID, "audit review drift")
    req(ha["merge_ready_freshness"] == "CLEAR", "audit freshness drift")
    ci = receipt["exact_head_ci"]
    req(ci["run_id"] == CI_RUN_ID and ci["job_id"] == CI_JOB_ID and ci["conclusion"] == "SUCCESS", "exact-head CI identity")
    req(ci["exact_head_checkout"] is True, "exact-head checkout not certified")
    req(ci["hpadj09_grf02_historical_replay"] is True, "character historical replay not certified")
    req(ci["td01_x4_envelope_historical_replay"] is True, "TD01 historical replay not certified")

    c = receipt["candidate"]
    req(c["exact_hpadj08_survivor_envelope"] == ENVELOPE, "receipt envelope")
    req(c["certified_upper_bound_candidate"] == CANDIDATE, "receipt candidate")
    req(c["potential_tightening_vs_current_main"] == TIGHTENING, "receipt tightening")
    req(c["composition_rule"] == RULE, "receipt composition")
    req(c["additive_stacking_authorized"] is False, "receipt additive stacking")

    hb = handoff["audited_boundary"]
    req(handoff["status"] == "HOSTILE_AUDITED_PRODUCER_CANDIDATE_READY_FOR_MAIN_DISPOSITION", "handoff status")
    req(hb["audited_exact_head"] == AUDITED_HEAD and hb["hostile_audit_status"] == "PASS", "handoff audit identity")
    req(hb["audit_review_id"] == AUDIT_REVIEW_ID, "handoff review id")
    req(hb["audit_pass_receipt_blob_sha1"] == RECEIPT_BLOB, "handoff receipt blob")
    req(hb["audit_pass_receipt_canonical_sha256"] == RECEIPT_CANON, "handoff receipt canonical")
    hc = handoff["candidate"]
    req(hc["exact_hpadj08_survivor_envelope"] == ENVELOPE, "handoff envelope")
    req(hc["certified_upper_bound_candidate"] == CANDIDATE, "handoff candidate")
    req(hc["potential_tightening_vs_v30_main"] == TIGHTENING, "handoff tightening")
    req(hc["composition_rule"] == RULE and hc["additive_stacking_authorized"] is False, "handoff composition")
    cc = handoff["consumer_contract"]
    req(cc["demand_id"] == DEMAND_ID, "handoff demand id")
    req(cc["demand_may_now_be_satisfied_from_this_artifact"] is True, "handoff demand not satisfiable")
    req(cc["explicit_main_consumption_still_required"] is True, "handoff bypasses MAIN consumption")
    req(cc["producer_subtraction_performed"] is False, "producer subtraction performed")

    req(state["status"] == "HOSTILE_AUDIT_PASS_MAIN_HANDOFF_READY_NO_MAIN_CREDIT", "state status")
    req(state["routing"]["audit_required"] is False, "state still audit-pending")
    req(state["routing"]["main_handoff_ready"] is True, "state handoff not ready")
    req(state["routing"]["main_credit_allowed"] is False, "state self-grants MAIN credit")
    req(state["hostile_audit_pass"]["review_id"] == AUDIT_REVIEW_ID, "state review id")
    req(state["exact_nonheavy_bound"]["candidate_td01_upper_bound"] == CANDIDATE, "state candidate")
    req(state["exact_nonheavy_bound"]["composition_rule"] == RULE, "state composition")
    req(state["anti_duplication"]["hpadj09_and_td01_additively_stacked"] is False, "state double stack")

    req(audit_handoff["status"] == "HOSTILE_AUDIT_PASS_RECORDED_MAIN_HANDOFF_READY_NO_MAIN_CREDIT", "audit handoff status")
    req(audit_handoff["consumer_contract"]["demand_id"] == DEMAND_ID, "audit handoff demand")
    req(audit_handoff["consumer_contract"]["producer_ready_for_consumer_reentry"] is True, "consumer re-entry not released")
    req(audit_handoff["consumer_contract"]["explicit_main_consumption_required"] is True, "audit handoff bypasses MAIN consumption")

    req(packet["main_composition_candidate"]["candidate_td01_upper_bound"] == CANDIDATE, "packet candidate")
    req(packet["main_composition_candidate"]["rule"] == RULE, "packet composition")
    req(packet["main_composition_candidate"]["main_authority_mutated"] is False, "packet MAIN mutation")

    for surface in (receipt, handoff, state, audit_handoff):
        fw = surface.get("credit_firewall", surface.get("firewalls", {}))
        req(fw.get("merge_authorized") is False, "merge firewall")
        if "main_pruning_credit" in fw:
            req(fw["main_pruning_credit"] is False, "MAIN credit firewall")

    print(json.dumps({
        "status": "PASS_TD01_HOSTILE_AUDITED_MAIN_HANDOFF_READY",
        "audited_exact_head": AUDITED_HEAD,
        "audit_review_id": AUDIT_REVIEW_ID,
        "consumer_demand_id": DEMAND_ID,
        "candidate_td01_upper_bound": CANDIDATE,
        "main_handoff_ready": True,
        "main_credit": False,
        "merge_authorized": False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
