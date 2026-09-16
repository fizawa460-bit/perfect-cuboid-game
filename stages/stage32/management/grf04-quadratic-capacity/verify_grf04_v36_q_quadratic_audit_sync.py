#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
SYNC = HERE / "GRF04-V36-Q-QUADRATIC-AUDIT-SYNC.json"
V35_RECEIPT = HERE / "GRF04-V35-Q-QUADRATIC-MAIN-BOUND-REPLACEMENT.json"
V35_VERIFIER = HERE / "verify_grf04_v35_q_quadratic_main_bound_replacement.py"
CANDIDATE = HERE / "GRF04-MAIN-INDEPENDENT-QUADRATIC-CAPACITY-LP-CANDIDATE.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

STATE_BLOB = "e5e490192706a4efcf5fb5e1300a9e7662c6e0b4"
STATE_CANON = "c77ae807e3892303cff7e055cde2ad872eaf55c55d15c8b744cb4f7b76a33614"
SYNC_BLOB = "c5418f9ed2813f0a38b2342fd31e4f3ce23a017a"
SYNC_CANON = "b30400705423b2c3c060f58ae9085d9442fc07c88dddad10ffa27e1f41c0ff59"
V35_RECEIPT_BLOB = "b24731409f33a8e76d3924ee2f651fbfba86b044"
V35_RECEIPT_CANON = "c04bf60efdd92f7af245e307167fffffd1d0d4a087a676ded5b01e5110298748"
V35_VERIFIER_BLOB = "769ec6c3d3b6c53f06aa94a492971c0ea83c2bc9"
CANDIDATE_BLOB = "1d669114e930951b9d5f9f82a6abb2b59cd43884"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

V35_HEAD = "872e30bbdf089f39223031efc7a2daa4600aa5da"
V35_STATE_BLOB = "9b460df0b49e70513a13e0ab09aecb8fab375f90"
V35_STATE_CANON = "987e6d33b86170c78a3c9de3bfb0b39875314afb1f129160c8a2dfd97e3eabaa"
AUDIT_REVIEW = 5217772644
BOUND = 195603649074545538415


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked_json(path: Path, blob_sha1: str, canonical_sha256: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob_sha1, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == canonical_sha256,
        f"{label} stored canonical drift")
    req(canonical(obj) == canonical_sha256, f"{label} canonical drift")
    return obj


def main() -> None:
    # Lock every load-bearing live artifact before interpreting its semantics.
    state = locked_json(STATE, STATE_BLOB, STATE_CANON, "V36 MAIN state")
    sync = locked_json(SYNC, SYNC_BLOB, SYNC_CANON, "V36 audit-sync receipt")
    v35 = locked_json(V35_RECEIPT, V35_RECEIPT_BLOB, V35_RECEIPT_CANON, "V35 replacement receipt")
    req(git_blob(V35_VERIFIER) == V35_VERIFIER_BLOB, "V35 replacement verifier drift")
    req(git_blob(CANDIDATE) == CANDIDATE_BLOB, "q-quadratic candidate drift")
    req(git_blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(git_blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(git_blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    req(sync["status"] == "V35_REPLACEMENT_HOSTILE_AUDIT_PASS_SYNCED__ZERO_NEW_PRUNING",
        "sync status")
    audit = sync["hostile_audit"]
    req(audit["status"] == "PASS", "replacement audit status")
    req(audit["audited_exact_head"] == V35_HEAD, "replacement audited head")
    req(audit["review_id"] == AUDIT_REVIEW, "replacement audit review")
    req(audit["merge_ready_freshness"] == "CLEAR", "replacement audit freshness")
    pred = sync["predecessor_v35"]
    req(pred["exact_head"] == V35_HEAD, "predecessor exact head")
    req(pred["state_blob_sha1"] == V35_STATE_BLOB, "predecessor state blob")
    req(pred["state_canonical_sha256"] == V35_STATE_CANON, "predecessor state canonical")
    req(pred["replacement_receipt_blob_sha1"] == V35_RECEIPT_BLOB, "predecessor receipt blob")
    req(pred["replacement_verifier_blob_sha1"] == V35_VERIFIER_BLOB, "predecessor verifier blob")

    s = sync["sync"]
    req(s["authority_version"] == "V36_PROCESS_SYNC_ONLY", "sync authority version")
    req(s["authoritative_remaining_strata"] == 17128, "sync strata")
    req(s["authoritative_remaining_terminals"] == BOUND, "sync bound")
    req(s["additional_pruning"] == 0, "sync added pruning")
    req(s["numeric_authority_changed"] is False, "numeric authority changed")
    req(s["logical_claim_statement_changed"] is False, "logical claim changed")
    req(s["claim_registry_mutated"] is False and
        s["active_frontier_mutated"] is False and
        s["lane_adapters_mutated"] is False, "claim/frontier routing mutation")
    req(s["replacement_head_hostile_reaudit_required_after_sync"] is False, "audit gate not cleared")
    req(s["full178_resumes"] is True, "FULL178 did not resume")
    req(s["retained_v36_t_stratified_candidate_consumed"] is False,
        "unrelated retained V36 candidate silently consumed")

    req(v35["replacement"]["authoritative_remaining_terminals"] == BOUND,
        "V35 predecessor authority")
    req(v35["replacement"]["additive_subtraction_performed"] is False, "V35 additive subtraction")
    req(v35["replacement"]["double_charge"] is False, "V35 double charge")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V36_Q_QUADRATIC_AUDIT_SYNCED_FULL178_REENTRY",
        "state schema")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "state strata")
    req(f["authoritative_remaining_terminals"] == BOUND, "state bound")
    req(f["v35_replacement_head_hostile_audited"] is True, "state audit flag")
    req(f["v35_replacement_head_audited_exact_head"] == V35_HEAD, "state audit head")
    req(f["v35_replacement_head_hostile_audit_review_id"] == AUDIT_REVIEW, "state audit review")
    req(f["v36_audit_sync_additional_pruning"] == 0, "state sync added pruning")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "closure firewall")

    fw = state["firewalls"]
    req(fw["replacement_head_hostile_reaudit_required"] is False, "replacement audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(fw[key] is False, f"firewall {key}")

    sweep = state["source_locks"]["live_specialist_sweep"]
    req(sweep["lane_178_head"] == "23e53bfd145b722640481e34458fb689326e486a",
        "178 live head")
    req("NO_MAIN_CREDIT" in sweep["lane_178_handoff"], "178 credit firewall")
    req(sweep["ex5_head"] == "dbd3a191bfdd33c3413a2abc41331feb651f0830",
        "EX5 live head")
    req("NO_MAIN_CREDIT" in sweep["ex5_handoff"], "EX5 credit firewall")
    req(sweep["cut_handoff"] == "NONE" and sweep["mb_handoff"] == "NONE",
        "CUT/MB handoff firewall")

    print("PASS: Stage32 V36 synchronizes hostile-audit PASS for V35 q-quadratic authority with zero new pruning")
    print("PASS: replacement reaudit gate cleared; FULL178 reentry resumes; specialist successors remain zero-credit")


if __name__ == "__main__":
    main()
