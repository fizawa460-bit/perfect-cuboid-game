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
BOUND = 138652739800650593494
V43_BOUND = 157570677819451133507
V44_TIGHTENING = 18917938018800540013
V41_BOUND = 179119009547804181594
V42_TIGHTENING = 21548331728353048087


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


def main():
    reg = lock(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    mon = lock(MONITOR, MONITOR_BLOB, MONITOR_CANON)
    st = json.loads(STATE.read_text(encoding="utf-8"))
    stored = st.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(st) == stored, "current MAIN state canonical drift")

    req([d["demand_id"] for d in reg["demands"] if d["status"] == "OPEN"] == [],
        "unexpected OPEN demand")
    req(mon["startup_rule"]["refresh_live_on_every_stage32mainbatch"] is True,
        "live sweep startup rule disabled")
    req(mon["authority"]["this_contract_is_a_snapshot_of_live_heads"] is False,
        "monitor contract treated as live snapshot")
    req(mon["credit_firewall"]["monitor_observation_is_mathematical_credit"] is False,
        "monitor observation credit firewall")

    req(st["schema"] == "STAGE32_MAIN_COMPACT_STATE_V45_HPADJ22_FULL178_BOUND_AUDIT_SYNCED",
        "MAIN state schema")
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["authoritative_remaining_terminals"] == BOUND, "MAIN numerical authority")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == V41_BOUND,
        "V41 predecessor bound")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == V42_TIGHTENING,
        "V42 tightening")
    req(f["v42_replacement_head_hostile_audited"] is True, "V42 hostile audit not synced")
    req(f["v43_audit_sync_additional_pruning"] == 0, "V43 added pruning")
    req(f["predecessor_v43_authoritative_remaining_terminals"] == V43_BOUND, "V43 predecessor authority")
    req(f["v44_hpadj22_main_numeric_bound_replacement_consumed"] is True, "V44 replacement not consumed")
    req(f["v44_hpadj22_candidate_main_credit"] is True, "V44 MAIN credit")
    req(f["v44_hpadj22_candidate_tightening_vs_hpadj21"] == str(V44_TIGHTENING), "V44 tightening")
    req(f["v44_replacement_head_hostile_audited"] is True, "V44 replacement audit not synced")
    req(f["v44_replacement_head_audited_exact_head"] == "142b50757b345971218c953db6a15ddd09974172", "V44 audited head")
    req(f["v44_replacement_head_hostile_audit_review_id"] == 5254793258, "V44 audit review")
    req(f["v45_audit_sync_additional_pruning"] == 0, "V45 added pruning")
    req(f["full178_numerical_census_complete"] is False, "FULL178 overclaim")

    req(st["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(st["current"]["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "MAIN next route")
    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is False,
        "replacement hostile re-audit gate still armed")

    sweep = st["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == "83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49",
        "repository main observation")
    req(sweep["lane_178_pr"] == 1821 and sweep["lane_178_head"] ==
        "fd8ffe03ff4b90f811e317a43e76a95f31c30464" and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 observation")
    req(sweep["ex5_pr"] == 1823 and sweep["ex5_head"] ==
        "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2" and
        sweep["ex5_pending_main_handoff"] == "NONE", "EX5 observation")
    req(sweep["mb_pr"] == 1825 and sweep["mb_head"] ==
        "81ac5f243c08fb7c16a2b7cb2f09653fff78f65e" and
        sweep["mb_pending_main_handoff"] == "NONE", "MB observation")
    req(sweep["mb_latest_audited_exact_head"] ==
        "b28adadc95776762754e1415a0ecab0da1d4cd8e" and
        sweep["mb_latest_audit_review_id"] == 5254494158,
        "MB audited predecessor observation")
    req(sweep["bridge_pr"] == 1813 and sweep["bridge_head"] ==
        "ee755bbfd46f405ca83e4930b354ee63459ad362" and
        sweep["bridge_runkey_generation"] == 1 and sweep["bridge_runkey_armed"] is True and
        sweep["bridge_pending_main_handoff"] == "NONE", "BRIDGE observation")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT observation")

    for key in ("full178_complete", "effectivity_released", "receiver_credit",
                "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    print("PASS: Stage32 MAIN V45 audit-sync records hostile-audited V44 HPADJ22 authority with zero new pruning")
    print("PASS: live 178/EX5/MB/BRIDGE/CUT observations include current MB P6B head with zero MAIN credit")
    print("PASS: FULL178 remains active incomplete; downstream and merge credit remain blocked")


if __name__ == "__main__":
    main()
