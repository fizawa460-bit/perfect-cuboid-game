#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STATE = HERE / "MAIN-STATE.json"
NORMALMASS = HERE / "management/btva-compressed-lift/run_btva_static7_normalmass_bounded_panel.py"
RELAXED = HERE / "management/btva-compressed-lift/run_btva_static7_bounded_panel.py"

CURRENT_MAIN = "83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49"
V43_AUDITED_HEAD = "1dfea81c06f9e3f52b99e4c88e7da7e78c872cc2"
BOUND = 157570677819451133507
V41_BOUND = 179119009547804181594
TIGHTENING = 21548331728353048087
NORMALMASS_BLOB = "971cf6bab500eefd04bbef870807f1badc8b07c4"
RELAXED_BLOB = "e44bec7ad9c0b7a4d8d7d87a455f181a681035c6"


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


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    stored = state.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(state) == stored,
        "current MAIN state canonical drift")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V43_HPADJ21_FULL178_BOUND_AUDIT_SYNCED",
        "authority schema drift")
    auth = state["authority_sync"]
    req(auth["current_repository_main"] == CURRENT_MAIN, "live repository main drift")
    req(auth["v42_replacement_hostile_audit_status"] == "PASS", "V42 audit lost")
    req(auth["v43_audit_sync_additional_pruning"] == 0, "V43 pruning drift")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority drift")
    req(f["authoritative_remaining_terminals"] == BOUND, "numerical authority drift")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == V41_BOUND,
        "V41 predecessor drift")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == TIGHTENING,
        "V42 tightening drift")
    req(f["v42_replacement_head_hostile_audited"] is True, "V42 audit flag lost")
    req(f["full178_numerical_census_complete"] is False, "FULL178 overclaim")
    req(f["stage32_closed"] is False, "Stage32 closure overclaim")

    cur = state["current"]
    req(cur["latest_main_native_research"] ==
        "V44_BTVA_BASE4_FULL343_V3_DIAGNOSTIC_RECOVERY__ZERO_MAIN_CREDIT",
        "V44 research successor routing drift")
    req(cur["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(cur["next_exact_route"] ==
        "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS",
        "MAIN next route drift")

    req(blob(NORMALMASS) == NORMALMASS_BLOB, "normalmass successor blob drift")
    req(blob(RELAXED) == RELAXED_BLOB, "relaxed predecessor blob drift")
    req("stages/stage32/management/btva-compressed-lift/run_btva_static7_normalmass_bounded_panel.py" in state["current_leaf_working_set"],
        "normalmass successor missing from working set")
    req("stages/stage32/management/btva-compressed-lift/run_btva_base4_full343_shard.py" in state["current_leaf_working_set"],
        "full343 recovery worker missing from working set")
    req("stages/stage32/management/btva-compressed-lift/BTVA-BASE4-FULL343-SCALEOUT-PREFLIGHT-V3.json" in state["current_leaf_working_set"],
        "full343 V3 preflight missing from working set")

    sweep = state["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == CURRENT_MAIN, "live main observation drift")
    req(sweep["lane_178_pr"] == 1821 and sweep["lane_178_head"] ==
        "bf5173ff96b97f266e810ebd7747d14de6a28727" and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 live observation")
    req(sweep["ex5_pr"] == 1818 and sweep["ex5_head"] ==
        "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2" and
        sweep["ex5_pending_main_handoff"] == "NONE__CONSUMED_BY_V42", "EX5 observation")
    req(sweep["mb_pr"] == 1819 and sweep["mb_head"] ==
        "6d5d6c77fd2d347dc8e43aaa183b794075201fcd" and
        sweep["mb_pending_main_handoff"] == "NONE", "MB observation")
    req(sweep["bridge_pr"] == 1813 and sweep["bridge_head"] ==
        "74d49b08b1924c2edcfbd7d0fa26f308e23c3ba4" and
        sweep["bridge_audited_doorstep_head"] == "48bf75ea1fe79afe08d4349799bc699da651ce04" and
        sweep["bridge_audited_doorstep_review_id"] == 5243659462 and
        sweep["bridge_runkey_generation"] == 0 and
        sweep["bridge_runkey_armed"] is False and
        sweep["bridge_pending_main_handoff"] == "NONE", "BRIDGE observation")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT observation")

    for key in ("full178_complete", "effectivity_released", "receiver_credit",
                "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(state["firewalls"][key] is False, "firewall " + key)

    req(V41_BOUND - BOUND == TIGHTENING, "authority arithmetic")
    print("PASS: merged hostile-audited V43 authority is preserved on V44 successor")
    print("PASS: V44 BTVA static7 normal-mass unit is zero-credit and source-locked")
    print("PASS: live 178/EX5/MB/BRIDGE/CUT observations are refreshed")


if __name__ == "__main__":
    main()
