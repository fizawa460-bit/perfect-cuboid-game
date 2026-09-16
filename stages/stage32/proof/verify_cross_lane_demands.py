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
BOUND = 195414091250828468192
PREDECESSOR_BOUND = 195603649074545538415
FULL178_AUDIT_REVIEW = 5218209619
V38_AUDIT_REVIEW = 5218756566
TIGHTENING = 189557823717070223

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

    req(st["authority_sync"]["split_authority"]["orchestration_mode"] ==
        "ROOT_NATIVE_STAGE32_MAIN_ONLY", "orchestration mode")
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v37_authoritative_remaining_terminals"] == PREDECESSOR_BOUND,
        "V37 predecessor bound")
    req(f["authoritative_remaining_terminals"] == BOUND, "MAIN numerical authority")
    req(f["v38_td02_full178_certified_numeric_bound_tightening_vs_v37"] == TIGHTENING,
        "V38 tightening")
    req(f["live_178_td02_full178_capacity_hostile_audited"] is True,
        "178 FULL178 PASS missing")
    req(f["live_178_td02_full178_capacity_audit_review_id"] == FULL178_AUDIT_REVIEW,
        "178 FULL178 audit review")
    req(f["live_178_td02_main_credit_consumed"] is True,
        "178 consumption boundary")
    req(f["v38_replacement_head_hostile_audited"] is True,
        "V38 replacement audit not synced")
    req(f["v38_replacement_head_hostile_audit_review_id"] == V38_AUDIT_REVIEW,
        "V38 replacement audit review")
    req(f["v39_audit_sync_additional_pruning"] == 0,
        "V39 audit-sync added pruning")
    req(f["full178_numerical_census_complete"] is False,
        "FULL178 numerical census overclaim")

    req(st["current"]["mainbatch_stop_gate"] == "NONE",
        "MAIN stop gate not cleared")
    req(st["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS",
        "MAIN next route")

    sweep = st["source_locks"]["live_specialist_sweep"]
    required = (
        "observed_repository_main", "lane_178_pr", "lane_178_head", "lane_178_handoff",
        "lane_178_full178_audit_review_id", "lane_178_postsync_replay_head",
        "ex5_pr", "ex5_head", "ex5_handoff", "cut_open_successor", "cut_handoff",
        "mb_pr", "mb_head", "mb_handoff",
    )
    for key in required:
        req(key in sweep, f"missing live sweep field {key}")
    req(sweep["observed_repository_main"] == st["authority_sync"]["current_repository_main"],
        "repository-main observation drift")
    req(sweep["lane_178_pr"] == 1815 and
        sweep["lane_178_full178_audit_review_id"] == FULL178_AUDIT_REVIEW,
        "178 live observation")
    req("MAIN_BOUND_CONSUMED_V38" in sweep["lane_178_handoff"] and
        "V38_REPLACEMENT_AUDIT_PASS_SYNCED" in sweep["lane_178_handoff"],
        "178 audit-sync semantics")
    req(sweep["ex5_head"] == "626285adecb3f0b195515b39d1a5e11c82b75cad",
        "EX5 live observation stale")
    req("NO_MAIN_CREDIT" in sweep["ex5_handoff"], "EX5 credit firewall")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT observation")
    req(sweep["mb_head"] == "c034cd52c8dc30842733b5aa0ca002b10c3a7732",
        "MB live observation stale")
    req("NO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")

    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "replacement reaudit firewall not cleared")
    for key in ("full178_complete", "effectivity_released", "receiver_credit",
                "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    print("PASS: Stage32 MAIN V39 has synchronized the hostile-audit PASS for V38 with zero new pruning")
    print("PASS: current specialist observations are refreshed; FULL178/final-milestone route may resume")

if __name__ == "__main__":
    main()
