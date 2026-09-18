#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
SYNC = HERE / "GRF04-V43-HPADJ21-FULL178-AUDIT-SYNC.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

SYNC_BLOB = "0ce17ea71e723a69581e613e36c03445f99963ea"
SYNC_CANON = "838ec4f617ffb986e7939aff61e437870b68be43ee3a159f50bdeb0b9c163f60"
V42_HEAD = "e4311c4ec31d5768c57308681ae60679987e2ced"
V42_STATE_BLOB = "07d71175268085fd608443bdfef0c126ed4894c3"
V42_STATE_CANON = "1fe41b66c97c81f3fc72154728600284b1256c71204b9e1841b0bc7955d6a836"
V42_RECEIPT_BLOB = "3072d84981eaec239ba55a5e5e25a3481d37406b"
V42_RECEIPT_CANON = "06be0bdf846364622af9c555e6f7e64be50b58c1d369d6db66c2f0b21d644831"
V42_VERIFIER_BLOB = "e7c88c208739ebe30b5f21a4c5b8be625442c02d"
V42_WRAPPER_BLOB = "52940cf924cc239584a7d1cb39b55fdc9c9d9289"
V42_STARTUP_BLOB = "7f2d8f1c84db40a33afaea43326a38395491715c"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUDIT_REVIEW_NODE = "PRR_kwDOTr52Y88AAAABOILpPw"
CURRENT_REPO_MAIN = "37bb811b95399d73cc46fe899badcfa8eb5fca7d"
BOUND = 157570677819451133507
V41_BOUND = 179119009547804181594
TIGHTENING = 21548331728353048087


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
    ap.add_argument("--v42-root", type=Path)
    args = ap.parse_args()

    state = current_state()
    sync = lock_json(SYNC, SYNC_BLOB, SYNC_CANON, "V43 audit-sync receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.v42_root is not None:
        root = args.v42_root
        lock_json(root / "stages/stage32/MAIN-STATE.json", V42_STATE_BLOB, V42_STATE_CANON,
                  "V42 predecessor state")
        lock_json(root / "stages/stage32/management/grf04-quadratic-capacity/GRF04-V42-HPADJ21-FULL178-MAIN-BOUND-REPLACEMENT.json",
                  V42_RECEIPT_BLOB, V42_RECEIPT_CANON, "V42 replacement receipt")
        req(blob(root / "stages/stage32/management/grf04-quadratic-capacity/verify_grf04_v42_hpadj21_full178_main_bound_replacement.py") == V42_VERIFIER_BLOB,
            "V42 replacement verifier drift")
        req(blob(root / "stages/stage32/verify_main_startup_authority_v42_hpadj21_full178_bound_consumed.py") == V42_WRAPPER_BLOB,
            "V42 startup wrapper drift")
        req(blob(root / "stages/stage32/verify_main_startup.py") == V42_STARTUP_BLOB,
            "V42 startup projection drift")

    req(sync["status"] == "V42_REPLACEMENT_HOSTILE_AUDIT_PASS_SYNCED__ZERO_NEW_PRUNING",
        "sync status")
    pred = sync["predecessor_v42"]
    req(pred["exact_head"] == V42_HEAD, "V42 predecessor head")
    req(pred["state_blob_sha1"] == V42_STATE_BLOB and
        pred["state_canonical_sha256"] == V42_STATE_CANON, "V42 predecessor state identity")
    req(pred["replacement_receipt_blob_sha1"] == V42_RECEIPT_BLOB and
        pred["replacement_receipt_canonical_sha256"] == V42_RECEIPT_CANON,
        "V42 receipt identity")
    req(pred["replacement_verifier_blob_sha1"] == V42_VERIFIER_BLOB,
        "V42 verifier identity")

    audit = sync["hostile_audit"]
    req(audit["status"] == "PASS", "V42 audit status")
    req(audit["audited_exact_head"] == V42_HEAD, "V42 audited head")
    req(audit["review_node_id"] == AUDIT_REVIEW_NODE, "V42 audit review node")
    req(audit["current_main_at_audit"] == CURRENT_REPO_MAIN, "V42 audit main")
    req(audit["merge_ready_freshness"] == "CLEAR", "V42 audit freshness")
    req(audit["stage36_failure_is_independent"] is True, "Stage36 separation record")

    s = sync["sync"]
    req(s["authority_version"] == "V43_PROCESS_SYNC_ONLY", "sync authority version")
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

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V43_HPADJ21_FULL178_BOUND_AUDIT_SYNCED",
        "state schema")
    a = state["authority_sync"]
    req(a["current_repository_main"] == CURRENT_REPO_MAIN, "state repository main")
    req(a["predecessor_process_head"] == V42_HEAD, "state predecessor head")
    req(a["v42_replacement_hostile_audit_status"] == "PASS", "state V42 audit status")
    req(a["v42_replacement_hostile_audit_review_node_id"] == AUDIT_REVIEW_NODE,
        "state V42 audit review")
    req(a["v43_audit_sync_additional_pruning"] == 0, "V43 added pruning")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "state strata")
    req(f["authoritative_remaining_terminals"] == BOUND, "state bound")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == V41_BOUND,
        "V41 bound")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == TIGHTENING,
        "V42 tightening")
    req(f["v42_replacement_head_hostile_audited"] is True, "V42 audit flag")
    req(f["v43_audit_sync_additional_pruning"] == 0, "V43 state pruning")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "closure firewall")

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
    req(sweep["lane_178_pr"] == 1821 and sweep["lane_178_head"] ==
        "e60f03cf5105bc6e26cb4615acabd6fe0c07625c", "178 live sweep")
    req(sweep["ex5_pr"] == 1818 and sweep["ex5_head"] ==
        "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2", "EX5 live sweep")
    req(sweep["mb_pr"] == 1819 and sweep["mb_head"] ==
        "ebbbeacd73500866569f93e94983912a52e18c70", "MB live sweep")
    req(sweep["bridge_pr"] == 1813 and sweep["bridge_head"] ==
        "b5d687711d74cbfe8a0c5135dae8162988a40f9a", "BRIDGE live sweep")
    req(sweep["bridge_runkey_generation"] == 1 and sweep["bridge_runkey_armed"] is True,
        "BRIDGE generation-1 arm observation")

    sl = state["source_locks"]["v43_audit_sync_receipt"]
    req(sl["blob_sha1"] == SYNC_BLOB and sl["canonical_sha256"] == SYNC_CANON,
        "state V43 sync receipt source lock")

    req(V41_BOUND - BOUND == TIGHTENING, "V42 authority arithmetic")
    print("PASS: Stage32 V43 synchronizes the hostile-audited V42 HPADJ21 numerical authority with zero new pruning")
    print("PASS: V42 audit gate cleared; FULL178 research resumes with downstream/merge firewalls unchanged")
    print("PASS: live specialist sweep refreshed through MB and BRIDGE current heads")


if __name__ == "__main__":
    main()
