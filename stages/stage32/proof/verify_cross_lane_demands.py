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
BOUND = 157570677819451133507
V41_BOUND = 179119009547804181594
V42_TIGHTENING = 21548331728353048087
EX5_AUDIT_REVIEW = 5242670540


def req(v, m):
    if not v:
        raise SystemExit("FAIL: " + m)


def is_sha1(v):
    return isinstance(v, str) and len(v) == 40 and all(c in "0123456789abcdef" for c in v)


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

    req(st["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V42_HPADJ21_FULL178_BOUND_CONSUMED_REAUDIT_PENDING",
        "MAIN state schema")
    req(st["authority_sync"]["split_authority"]["orchestration_mode"] ==
        "ROOT_NATIVE_STAGE32_MAIN_ONLY", "orchestration mode")
    req(st["authority_sync"]["hpadj21_full178_main_numeric_bound_replacement_consumed"] is True,
        "HPADJ21 consumption flag")
    req(st["authority_sync"]["hpadj21_candidate_hostile_audit_status"] == "PASS" and
        st["authority_sync"]["hpadj21_candidate_hostile_audit_review_id"] == EX5_AUDIT_REVIEW,
        "HPADJ21 producer audit identity")

    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == V41_BOUND,
        "V41 predecessor bound")
    req(f["authoritative_remaining_terminals"] == BOUND, "MAIN numerical authority")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == V42_TIGHTENING,
        "V42 tightening")
    req(f["live_ex5_hpadj21_main_credit_consumed"] is True, "EX5 consumption not recorded")
    req(f["full178_numerical_census_complete"] is False, "FULL178 overclaim")

    req(st["current"]["mainbatch_stop_gate"] ==
        "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "MAIN stop gate")
    req(st["current"]["next_exact_route"] ==
        "HOSTILE_AUDIT_V42_HPADJ21_FULL178_BOUND_REPLACEMENT", "MAIN next route")

    sweep = st["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == st["authority_sync"]["current_repository_main"],
        "repository-main observation drift")

    req(sweep["lane_178_pr"] == 1821 and is_sha1(sweep["lane_178_head"]) and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 live observation")
    req("ZERO_MAIN_CREDIT" in sweep["lane_178_handoff"], "178 credit firewall")
    req(sweep["lane_178_current_head_audit_status"].endswith("HOSTILE_AUDIT_PENDING"),
        "178 audit gate")

    req(sweep["ex5_pr"] == 1818 and
        sweep["ex5_head"] == "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2",
        "EX5 live observation")
    req(sweep["ex5_current_head_audit_status"] ==
        "HOSTILE_AUDITED_PRODUCER_RESULT_PASS__POST_AUDIT_HANDOFF_VERIFIED",
        "EX5 audit gate")
    req(sweep["ex5_handoff"] ==
        "HPADJ21_FULL178_HOSTILE_AUDITED_MAIN_HANDOFF__CONSUMED_BY_V42",
        "EX5 handoff consumption")
    req(sweep["ex5_pending_main_handoff"] == "NONE__CONSUMED_BY_V42",
        "EX5 pending handoff state")

    req(sweep["cut_open_successor"] is False and
        sweep["cut_handoff"] == "NONE" and
        sweep["cut_pending_main_handoff"] == "NONE", "CUT observation")

    req(sweep["mb_pr"] == 1819 and is_sha1(sweep["mb_head"]) and
        sweep["mb_pending_main_handoff"] == "NONE", "MB live observation")
    req("ZERO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")
    req(sweep["mb_current_head_audit_status"] == "PENDING_CURRENT_HEAD_AUDIT",
        "MB audit gate")

    req(sweep["bridge_pr"] == 1813 and is_sha1(sweep["bridge_head"]) and
        sweep["bridge_pending_main_handoff"] == "NONE", "BRIDGE live observation")
    req("ZERO_MAIN_CREDIT" in sweep["bridge_handoff"], "BRIDGE credit firewall")
    req(sweep["bridge_current_head_audit_status"].endswith("HOSTILE_AUDIT_PENDING"),
        "BRIDGE current audit gate")
    req(sweep["bridge_latest_hostile_audit_fail_review_id"] == 5242654911,
        "BRIDGE latest FAIL receipt")

    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "replacement audit firewall not armed")
    for key in ("full178_complete", "effectivity_released", "receiver_credit",
                "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    print("PASS: Stage32 MAIN V42 routes hostile-audited HPADJ21 as a non-additive replacement")
    print("PASS: replacement head is fail-closed pending hostile reaudit; FULL178 remains active incomplete")
    print("PASS: live specialist observation shapes/firewalls verified; remote freshness remains an operator startup obligation")


if __name__ == "__main__":
    main()
