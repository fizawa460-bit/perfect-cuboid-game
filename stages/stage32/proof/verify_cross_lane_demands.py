#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"

REGISTRY_BLOB = "68a02f31431ad658b42ad695f9553c67fd6cff01"
REGISTRY_CANON = "aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB = "2d245205d2c4e597284fcefc6b5f6b43f8df7a2a"
MONITOR_CANON = "f5b2403a76546db1c7aea61bfb3eb5b62b3141063969e819758e6911f3a54e6e"
BOUND = 179119009547804181594
V39_BOUND = 195414091250828468192
V40_TIGHTENING = 16295081703024286598
V40_AUDIT_REVIEW = 5231559824


def req(v, m):
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p):
    b = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canon(o):
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def lock(p, b, c):
    req(blob(p) == b, f"blob drift {p}")
    o = json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field") == c and canon(o) == c,
        f"canonical drift {p}")
    return o


def current_state():
    o = json.loads(STATE.read_text(encoding="utf-8"))
    stored = o.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(o) == stored, "current MAIN state canonical drift")
    return o


def main():
    reg = lock(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    mon = lock(MONITOR, MONITOR_BLOB, MONITOR_CANON)
    st = current_state()

    req([d["demand_id"] for d in reg["demands"] if d["status"] == "OPEN"] == [],
        "unexpected OPEN demand")
    req(mon["startup_rule"]["refresh_live_on_every_stage32mainbatch"] is True,
        "live sweep startup rule disabled")
    req(mon["authority"]["this_contract_is_a_snapshot_of_live_heads"] is False,
        "monitor contract treated as live snapshot")
    req(mon["credit_firewall"]["monitor_observation_is_mathematical_credit"] is False,
        "monitor observation credit firewall")

    req(st["schema"] == "STAGE32_MAIN_COMPACT_STATE_V41_HPADJ20_FULL178_BOUND_AUDIT_SYNCED",
        "MAIN state schema")
    req(st["authority_sync"]["split_authority"]["orchestration_mode"] ==
        "ROOT_NATIVE_STAGE32_MAIN_ONLY", "orchestration mode")

    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v39_authoritative_remaining_terminals"] == V39_BOUND,
        "V39 predecessor bound")
    req(f["authoritative_remaining_terminals"] == BOUND, "MAIN numerical authority")
    req(f["v40_hpadj20_certified_numeric_bound_tightening_vs_v39"] == V40_TIGHTENING,
        "V40 tightening")
    req(f["v40_replacement_head_hostile_audited"] is True,
        "V40 replacement audit not synchronized")
    req(f["v40_replacement_head_hostile_audit_review_id"] == V40_AUDIT_REVIEW,
        "V40 replacement audit review")
    req(f["v41_audit_sync_additional_pruning"] == 0, "V41 added pruning")
    req(f["full178_numerical_census_complete"] is False, "FULL178 overclaim")

    req(st["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(st["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "MAIN next route")

    sweep = st["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == st["authority_sync"]["current_repository_main"],
        "repository-main observation drift")
    req(sweep["lane_178_pr"] == 1821 and
        sweep["lane_178_head"] == "59c229bf10020d1d103916329b0262d7b4930f7c" and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 live observation")
    req(sweep["lane_178_current_head_audit_status"] ==
        "PENDING_FRESH_EXACT_HEAD_REPLAY_AUDIT", "178 audit gate")
    req(sweep["ex5_pr"] == 1818 and
        sweep["ex5_head"] == "3d4b9e190aa6d9feba596e60c8a6cecfa325b5d0" and
        sweep["ex5_pending_main_handoff"] == "NONE", "EX5 live observation")
    req("ZERO_MAIN_CREDIT" in sweep["ex5_handoff"], "EX5 credit firewall")
    req(sweep["ex5_current_head_audit_status"] ==
        "FULL178_HEAVY_REPLAY_QUEUED__HOSTILE_AUDIT_PENDING", "EX5 audit gate")
    req(sweep["cut_open_successor"] is False and
        sweep["cut_handoff"] == "NONE" and
        sweep["cut_pending_main_handoff"] == "NONE", "CUT observation")
    req(sweep["mb_pr"] == 1819 and
        sweep["mb_head"] == "ef09e1dfb69ab9fbe9198b9fa22d3c01c03a4de6" and
        sweep["mb_pending_main_handoff"] == "NONE", "MB live observation")
    req("ZERO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")
    req(sweep["mb_current_head_audit_status"] == "PENDING_CURRENT_HEAD_AUDIT",
        "MB audit gate")

    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "replacement audit firewall still armed")
    for key in ("full178_complete", "effectivity_released", "receiver_credit",
                "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    print("PASS: Stage32 MAIN V41 synchronizes V40 hostile-audit PASS and resumes FULL178 routing")
    print("PASS: live 178/EX5/MB/CUT observations refreshed with no new MAIN handoff or credit")


if __name__ == "__main__":
    main()
