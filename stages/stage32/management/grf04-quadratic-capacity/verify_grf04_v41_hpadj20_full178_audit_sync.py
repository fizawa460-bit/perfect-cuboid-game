#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
SYNC = HERE / "GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

SYNC_BLOB = "ee6639e2b4a4ad5dd48e964d6a6b055f551e7bd1"
SYNC_CANON = "ac52c7d4598eba4ef165bed05c5ff12931777052a2b8582c65286ff8067400c7"
V40_HEAD = "dc4dfdf7bea41116aa63d69a5bbd17fa053e741c"
V40_STATE_BLOB = "a22cb78a4b8a495f1abb93b20d4a8048dbd98df4"
V40_STATE_CANON = "10eb99bcf609dc9e8c65707398a0a57b0f7f1f48c631dc666d93cb7dcad4e817"
V40_RECEIPT_BLOB = "f9d984f64d2c428481e082be622848e33407baf1"
V40_RECEIPT_CANON = "f330348d1d6aee5417df20e119479c3c2b6b045a2ce96f7d6e4e54ac9a88d53d"
V40_VERIFIER_BLOB = "dd3073cd83ab8079d1fa16dd506e453a2d632ff7"
V40_WRAPPER_BLOB = "b519b1d5df79ebc784337ac72cee4494fdc9d003"
V40_STARTUP_BLOB = "adc9c0ba91547504bea1a2121af595a94581bcbd"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUDIT_REVIEW = 5231559824
MAIN_AT_AUDIT = "c6284abbb29930255892d56f800da0ea1e34734b"
CURRENT_REPO_MAIN = "37bb811b95399d73cc46fe899badcfa8eb5fca7d"
BOUND = 179119009547804181594
V39_BOUND = 195414091250828468192
TIGHTENING = 16295081703024286598

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def lock_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj

def current_state() -> dict:
    obj = json.loads(STATE.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(obj) == stored, "current MAIN state canonical drift")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v40-root", type=Path)
    args = ap.parse_args()

    state = current_state()
    sync = lock_json(SYNC, SYNC_BLOB, SYNC_CANON, "V41 audit-sync receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.v40_root is not None:
        root = args.v40_root
        lock_json(root / "stages/stage32/MAIN-STATE.json", V40_STATE_BLOB, V40_STATE_CANON,
                  "V40 predecessor state")
        lock_json(root / "stages/stage32/management/grf04-quadratic-capacity/GRF04-V40-HPADJ20-FULL178-MAIN-BOUND-REPLACEMENT.json",
                  V40_RECEIPT_BLOB, V40_RECEIPT_CANON, "V40 replacement receipt")
        req(blob(root / "stages/stage32/management/grf04-quadratic-capacity/verify_grf04_v40_hpadj20_full178_main_bound_replacement.py") == V40_VERIFIER_BLOB,
            "V40 replacement verifier drift")
        req(blob(root / "stages/stage32/verify_main_startup_authority_v40_hpadj20_full178_bound_consumed.py") == V40_WRAPPER_BLOB,
            "V40 startup wrapper drift")
        req(blob(root / "stages/stage32/verify_main_startup.py") == V40_STARTUP_BLOB,
            "V40 startup projection drift")

    req(sync["status"] == "V40_REPLACEMENT_HOSTILE_AUDIT_PASS_SYNCED__ZERO_NEW_PRUNING",
        "sync status")
    pred = sync["predecessor_v40"]
    req(pred["exact_head"] == V40_HEAD, "V40 predecessor head")
    req(pred["state_blob_sha1"] == V40_STATE_BLOB and
        pred["state_canonical_sha256"] == V40_STATE_CANON, "V40 predecessor state identity")
    req(pred["replacement_receipt_blob_sha1"] == V40_RECEIPT_BLOB and
        pred["replacement_receipt_canonical_sha256"] == V40_RECEIPT_CANON,
        "V40 receipt identity")
    req(pred["replacement_verifier_blob_sha1"] == V40_VERIFIER_BLOB,
        "V40 verifier identity")

    audit = sync["hostile_audit"]
    req(audit["status"] == "PASS", "V40 audit status")
    req(audit["audited_exact_head"] == V40_HEAD, "V40 audited head")
    req(audit["review_id"] == AUDIT_REVIEW, "V40 audit review")
    req(audit["current_main_at_audit"] == MAIN_AT_AUDIT, "V40 audit main")
    req(audit["merge_ready_freshness"] == "CLEAR", "V40 audit freshness")
    req(audit["stage36_failure_is_independent"] is True, "Stage36 separation record")

    s = sync["sync"]
    req(s["authority_version"] == "V41_PROCESS_SYNC_ONLY", "sync authority version")
    req(s["authoritative_remaining_strata"] == 17128, "sync strata")
    req(s["authoritative_remaining_terminals"] == BOUND, "sync bound")
    req(s["additional_pruning"] == 0 and s["numeric_authority_changed"] is False,
        "audit sync changed numerical authority")
    req(s["logical_claim_statement_changed"] is False, "logical claim changed")
    req(s["claim_registry_mutated"] is False and
        s["active_frontier_mutated"] is False and
        s["lane_adapters_mutated"] is False, "claim DAG unexpectedly mutated")
    req(s["replacement_head_hostile_reaudit_required_after_sync"] is False,
        "replacement audit gate not cleared")
    req(s["full178_resumes"] is True, "FULL178 did not resume")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V41_HPADJ20_FULL178_BOUND_AUDIT_SYNCED",
        "state schema")
    a = state["authority_sync"]
    req(a["current_repository_main"] == CURRENT_REPO_MAIN, "state current repository main")
    req(a["predecessor_process_head"] == V40_HEAD, "state predecessor head")
    req(a["v40_replacement_hostile_audit_status"] == "PASS", "state V40 audit status")
    req(a["v40_replacement_hostile_audit_review_id"] == AUDIT_REVIEW, "state V40 audit review")
    req(a["v41_audit_sync_additional_pruning"] == 0, "V41 added pruning")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "state strata")
    req(f["authoritative_remaining_terminals"] == BOUND, "state bound")
    req(f["predecessor_v39_authoritative_remaining_terminals"] == V39_BOUND, "V39 bound")
    req(f["v40_hpadj20_certified_numeric_bound_tightening_vs_v39"] == TIGHTENING,
        "V40 tightening")
    req(f["v40_replacement_head_hostile_audited"] is True, "V40 audit flag")
    req(f["v40_replacement_head_audited_exact_head"] == V40_HEAD, "V40 state audit head")
    req(f["v40_replacement_head_hostile_audit_review_id"] == AUDIT_REVIEW,
        "V40 state audit review")
    req(f["v41_audit_sync_additional_pruning"] == 0, "V41 state pruning")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "closure firewall")
    req("CANDIDATE_BOUND_177806468459973221208__ZERO_MAIN_CREDIT" in
        f["main_hpadj21_known_strict_subset_candidate_status"], "HPADJ21 preflight status")

    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(state["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "MAIN next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "replacement audit firewall")
    for key in ("full178_complete", "effectivity_released", "receiver_credit", "route_credit",
                "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    sweep = state["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == CURRENT_REPO_MAIN, "repository-main observation")
    req(sweep["lane_178_pr"] == 1821 and
        sweep["lane_178_head"] == "24bd91cfdd741db57d80a2763f123e80b5f1b492" and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 live sweep")
    req(sweep["lane_178_current_head_audit_status"] ==
        "PENDING_FRESH_EXACT_HEAD_REPLAY_AUDIT", "178 audit gate")
    req(sweep["ex5_pr"] == 1818 and
        sweep["ex5_head"] == "3d4b9e190aa6d9feba596e60c8a6cecfa325b5d0" and
        sweep["ex5_pending_main_handoff"] == "NONE", "EX5 successor live sweep")
    req("ZERO_MAIN_CREDIT" in sweep["ex5_handoff"], "EX5 credit firewall")
    req(sweep["ex5_current_head_audit_status"] ==
        "FULL178_HEAVY_REPLAY_QUEUED__HOSTILE_AUDIT_PENDING", "EX5 audit gate")
    req(sweep["ex5_representative_result"] ==
        "G1_D190_QA_FLOOR_IMPROVEMENT_1312541087822068106__REPRESENTATIVE_ONLY",
        "EX5 representative result")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT live sweep")
    req(sweep["mb_pr"] == 1819 and
        sweep["mb_head"] == "12ad04f57a6dcb0fd1587673ff83282a4033fd49" and
        sweep["mb_pending_main_handoff"] == "NONE", "MB live sweep")
    req("ZERO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")
    req(sweep["mb_current_head_audit_status"] == "PENDING_CURRENT_HEAD_AUDIT",
        "MB audit gate")
    req(sweep["bridge_pr"] == 1813 and
        sweep["bridge_head"] == "a182e95544cd8381a385ce360c9211240acd3741" and
        sweep["bridge_pending_main_handoff"] == "NONE", "BRIDGE live sweep")
    req("ZERO_MAIN_CREDIT" in sweep["bridge_handoff"], "BRIDGE credit firewall")
    req(sweep["bridge_current_head_audit_status"] == "CURRENT_HEAD_NOT_HOSTILE_AUDITED",
        "BRIDGE audit gate")
    req(sweep["bridge_latest_hostile_audit_pass_head"] ==
        "c780c05fb6ae8405dd609ba4a2331d4565331510" and
        sweep["bridge_latest_hostile_audit_review_id"] == 5231786735,
        "BRIDGE retained audited boundary")

    sl = state["source_locks"]["v41_audit_sync_receipt"]
    req(sl["blob_sha1"] == SYNC_BLOB and sl["canonical_sha256"] == SYNC_CANON,
        "state V41 sync receipt source lock")

    req(V39_BOUND - BOUND == TIGHTENING, "V40 authority arithmetic")
    print("PASS: Stage32 V41 synchronizes the hostile-audited V40 numerical authority with zero new pruning")
    print("PASS: V40 audit gate cleared; FULL178 resumes with downstream/merge firewalls unchanged")
    print("PASS: live 178/EX5/CUT/MB plus BRIDGE observations refreshed; HPADJ21 strict-subset preflight retained at zero credit")

if __name__ == "__main__":
    main()
