#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
SYNC = HERE / "GRF04-V39-TD02-FULL178-INTEGER-LATTICE-AUDIT-SYNC.json"
V38_RECEIPT = HERE / "GRF04-V38-TD02-FULL178-INTEGER-LATTICE-MAIN-BOUND-REPLACEMENT.json"
V38_VERIFIER = HERE / "verify_grf04_v38_td02_full178_integer_lattice_main_bound_replacement.py"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

SYNC_BLOB = "1524215fd43e22c3e3cc31f98c5f912754b7b487"
SYNC_CANON = "2b55387f83dcf377dba0c98c8bc614f99d155353d01521e29768303703d0b89a"
V38_RECEIPT_BLOB = "f959b922129354f58c2fd0e1b182d723bfa174e2"
V38_RECEIPT_CANON = "8adf31a03c6c1fd6538e25c50deb059b843d34cfaf174bc2993f078b4657a08b"
V38_VERIFIER_BLOB = "db25e786156906c1d2c51c39771e83329261ab32"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

V38_HEAD = "2d675a9a89ddd15531f0ab0f891c1c9398f94779"
V38_STATE_BLOB = "d965cb5c5e1d17e56acbbf5d5fede2569f217a91"
V38_STATE_CANON = "e3d5039665c4920733488ac2934c32741cacdd7c77bb8bb5ecd033aeaa604d18"
AUDIT_REVIEW = 5218756566
BOUND = 195414091250828468192

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
    req(STATE.is_file(), "missing current MAIN state")
    obj = json.loads(STATE.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(obj) == stored, "current MAIN state canonical drift")
    return obj

def main() -> None:
    state = current_state()
    sync = lock_json(SYNC, SYNC_BLOB, SYNC_CANON, "V39 audit-sync receipt")
    v38 = lock_json(V38_RECEIPT, V38_RECEIPT_BLOB, V38_RECEIPT_CANON, "V38 replacement receipt")
    req(blob(V38_VERIFIER) == V38_VERIFIER_BLOB, "V38 replacement verifier drift")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    req(sync["status"] == "V38_REPLACEMENT_HOSTILE_AUDIT_PASS_SYNCED__ZERO_NEW_PRUNING",
        "sync status")
    pred = sync["predecessor_v38"]
    req(pred["exact_head"] == V38_HEAD, "V38 predecessor head")
    req(pred["state_blob_sha1"] == V38_STATE_BLOB, "V38 predecessor state blob")
    req(pred["state_canonical_sha256"] == V38_STATE_CANON, "V38 predecessor state canonical")
    req(pred["replacement_receipt_blob_sha1"] == V38_RECEIPT_BLOB,
        "V38 predecessor receipt blob")
    req(pred["replacement_verifier_blob_sha1"] == V38_VERIFIER_BLOB,
        "V38 predecessor verifier blob")

    audit = sync["hostile_audit"]
    req(audit["status"] == "PASS", "V38 audit status")
    req(audit["audited_exact_head"] == V38_HEAD, "V38 audited head")
    req(audit["review_id"] == AUDIT_REVIEW, "V38 audit review")
    req(audit["merge_ready_freshness"] == "CLEAR", "V38 audit freshness")

    s = sync["sync"]
    req(s["authority_version"] == "V39_PROCESS_SYNC_ONLY", "sync authority version")
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

    req(v38["replacement"]["authoritative_remaining_terminals"] == BOUND,
        "V38 predecessor authority")
    req(v38["replacement"]["additive_subtraction_performed"] is False and
        v38["replacement"]["double_charge"] is False, "V38 credit firewall")

    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V39_FULL178_INTEGER_LATTICE_BOUND_AUDIT_SYNCED",
        "state schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "state strata")
    req(f["authoritative_remaining_terminals"] == BOUND, "state bound")
    req(f["v38_replacement_head_hostile_audited"] is True, "V38 audit flag")
    req(f["v38_replacement_head_audited_exact_head"] == V38_HEAD, "V38 state audit head")
    req(f["v38_replacement_head_hostile_audit_review_id"] == AUDIT_REVIEW,
        "V38 state audit review")
    req(f["v39_audit_sync_additional_pruning"] == 0, "V39 added pruning")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "closure firewall")

    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(state["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS",
        "MAIN next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "replacement audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete",
                "merge_authorized", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "receiver_credit",
                "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    sweep = state["source_locks"]["live_specialist_sweep"]
    req(sweep["lane_178_head"] == "df3b29d20ef0f7da1e34fa92beada6418ad3a4ea",
        "178 live head")
    req("V38_REPLACEMENT_AUDIT_PASS_SYNCED" in sweep["lane_178_handoff"],
        "178 audit-sync semantics")
    req(sweep["ex5_head"] == "bd1beaa5d91cf71f8a028527efd00aeb3558347d",
        "EX5 live head")
    req("HPADJ20" in sweep["ex5_handoff"] and "NO_MAIN_CREDIT" in sweep["ex5_handoff"],
        "EX5 credit firewall")
    req(sweep["mb_head"] == "c034cd52c8dc30842733b5aa0ca002b10c3a7732",
        "MB live head")
    req("NO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT observation")

    sl = state["source_locks"]["v39_audit_sync_receipt"]
    req(sl["blob_sha1"] == SYNC_BLOB and sl["canonical_sha256"] == SYNC_CANON,
        "state V39 sync receipt source lock")

    print("PASS: Stage32 V39 synchronizes hostile-audit PASS for V38 with zero new pruning")
    print("PASS: replacement audit gate cleared; FULL178/final-milestone route resumes")
    print("PASS: EX5 HPADJ20 and MB successors remain observational zero-credit inputs")

if __name__ == "__main__":
    main()
