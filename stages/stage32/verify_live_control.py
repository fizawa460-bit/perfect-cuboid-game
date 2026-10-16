#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CURRENT = HERE / "CURRENT.json"
DETAIL = HERE / "MAIN-STATE.json"
FORMAL_ROADMAP = HERE / "ROADMAP.md"
LIVE_02 = HERE / "final-chain/32-02-effectivity/LIVE.json"
LIVE_03 = HERE / "final-chain/32-03-multibranch/LIVE.json"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    cur = load(CURRENT)
    detail = load(DETAIL)
    u2 = load(LIVE_02)
    u3 = load(LIVE_03)
    roadmap = FORMAL_ROADMAP.read_text(encoding="utf-8")

    req(cur["schema"] == "STAGE32_LIVE_CONTROL_V1" and cur["stage"] == 32, "live control schema")
    req(cur["operator_entrypoint"] == "stage32mainbatch", "operator entrypoint")
    req(cur["detail_authority"] == "stages/stage32/MAIN-STATE.json", "detail authority pointer")
    req(cur["formal_roadmap"] == "stages/stage32/ROADMAP.md", "formal roadmap pointer")
    req(cur["routing_policy"] == "stages/stage32/MAIN-START-HERE.md", "routing policy pointer")
    req(cur["detail_files_are_on_demand"] is True, "detail files must be on-demand")
    req(not (HERE / "LIVE-ROADMAP.md").exists(), "duplicate LIVE-ROADMAP resurrected")

    target = detail["current_target"]
    frontier = detail["current_exact_frontier"]
    fire = detail["firewalls"]

    req(cur["status"]["32-01"] == "AUDITED_COMPLETE", "32-01 status")
    req(target["full178_numerical_census_complete"] is True, "detail 32-01 completion")
    req(cur["status"]["32-02"] == "ACTIVE_PRIMARY" and target["primary_incomplete_id"] == "32-02", "32-02 routing")
    req(cur["status"]["32-03"] == "ACTIVE_PARALLEL" and target["parallel_incomplete_id"] == "32-03", "32-03 routing")
    req(cur["status"]["32-04"] == "BLOCKED_ON_32_02_AND_32_03", "32-04 status")
    req(cur["status"]["32-05"] == "EXTERNAL_AUDIT_ONLY", "32-05 status")

    cf = cur["current_frontier"]
    req(int(cf["certified_upper_bound"]) == int(frontier["authoritative_remaining_terminals"]), "upper bound drift")
    req(cf["remaining_strata"] == frontier["authoritative_remaining_strata"], "strata drift")
    req(cf["full178_numerical_census_complete"] is frontier["full178_numerical_census_complete"], "census drift")
    req(cf["upper_bound_is_exact_residual_identity_set"] is False, "upper-bound semantics strengthened")

    for key in (
        "effectivity_released", "receiver_credit", "route_credit", "theorem_credit",
        "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ):
        req(cur["firewalls"][key] is fire[key] is False, f"firewall drift: {key}")

    req("dispatch" not in cur, "CURRENT duplicated dispatch policy")
    req(cur["unit_pointers"]["32-02"] == "stages/stage32/final-chain/32-02-effectivity/LIVE.json", "32-02 live pointer")
    req(cur["unit_pointers"]["32-03"] == "stages/stage32/final-chain/32-03-multibranch/LIVE.json", "32-03 live pointer")
    req(set(cur["unit_pointers"]) == {"32-02", "32-03"}, "unexpected live unit pointer")
    req(set(cur["parked"]) == {"32-01-178", "CUT", "BRIDGE"}, "parked surface drift")

    req(u2["schema"] == "STAGE32_32_02_LIVE_V1" and u2["status"] == "ACTIVE_PRIMARY_INCOMPLETE", "32-02 live schema/status")
    req(u2["internal_helper"]["surface"] == "EX5" and u2["internal_helper"]["read_only_when_needed"] is True, "32-02 helper routing")
    req(u2["internal_helper"]["routing_authority"] is False, "EX5 routing authority leak")
    req(all(v is False for v in u2["credit"].values()), "32-02 credit leak")
    req("close_criterion" not in u2, "32-02 live pointer duplicated formal close criterion")
    req(u2["formal_spec"] == "stages/stage32/ROADMAP.md", "32-02 formal spec pointer")
    req(u2["formal_spec_role"] == "SOLE_OWNER_OF_UNIT_DEFINITION_AND_CLOSE_CRITERION", "32-02 formal ownership")

    req(u3["schema"] == "STAGE32_32_03_LIVE_V1" and u3["status"] == "ACTIVE_PARALLEL_INCOMPLETE_ZERO_CREDIT", "32-03 live schema/status")
    req(u3["internal_surface"] == "MB", "32-03 MB routing")
    req(u3["auxiliary"]["surface"] == "MB-FIB" and u3["auxiliary"]["read_only_when_mb_selects_it"] is True, "MB-FIB preload leak")
    req(all(v is False for v in u3["credit"].values()), "32-03 credit leak")
    req("close_criterion" not in u3, "32-03 live pointer duplicated formal close criterion")
    req(u3["formal_spec"] == "stages/stage32/ROADMAP.md", "32-03 formal spec pointer")
    req(u3["formal_spec_role"] == "SOLE_OWNER_OF_UNIT_DEFINITION_AND_CLOSE_CRITERION", "32-03 formal ownership")

    for token in (
        "### 32-02-L — rigorous effectivity certification",
        "UNKNOWN_EFFECTIVITY_SURVIVOR_COUNT=0",
        "R29_LG2_EFF=DISCHARGED",
        "### 32-03-L — multibranch-at-node carrier ledger",
        "MULTIBRANCH_LOW_GENUS_LEDGER_COMPLETE=true",
        "R29_LG2_MB=DISCHARGED",
        "### 32-04-M — low-genus carrier synthesis and final certificate",
        "### 32-05 — final hostile audit and close",
        "PERFECT_CUBOID_EXISTENCE_CLAIM=false",
        "PERFECT_CUBOID_NONEXISTENCE_CLAIM=false",
    ):
        req(token in roadmap, f"formal roadmap missing load-bearing token: {token}")

    print("PASS: Stage32 compact live control matches retained detailed authority")
    print("PASS: ordinary startup may avoid MAIN-STATE/detail layers until load-bearing")


if __name__ == "__main__":
    main()
