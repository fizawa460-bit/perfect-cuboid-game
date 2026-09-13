#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]

EXPECTED_N387_BLOB = "3bff027f7fccc50dadd91514a8f143fba6316f47"
EXPECTED_N387_CANONICAL = "609a5cf44445a269f201ff1ba2fb0d52b4d4b86677e430fd3ac151811e9fbbca"
EXPECTED_N388_CANONICAL = "becb1434075922d957569a17c3cb59ac3629946fbf3c78e6a648956acb5e1e5d"

MAIN_COORD_HEAD = "7bd57f5f2013089f0cba34513a7be5e9fee78c7a"
MAIN_CROSS_PATH = "stages/stage32-ex5/CROSS-LANE-STATE.json"
MAIN_CROSS_BLOB = "0006aa15d3971d993eee4b3c33fc3a15004ce891"
MAIN_CROSS_CANONICAL = "4afb71a75c11647fe5dd0b27f080e4bdc90e970a33d45db46e0fa25a24b95f47"
MONITOR_PATH = "stages/stage32/management/hpadj-04/PRODUCER-MONITOR.json"
MONITOR_BLOB = "1b3e2bb96058a4e03dc522a16ca9a6ed8b80cab8"
MONITOR_CANONICAL = "d28370cb9af18ee5afd427e3445ae1a0765d6bd52e30aa2177c2f999ceafc123"

EX5_HEAD = "d26a27e8564458f3d575ec58601b2226fc23944f"
EX5_MAIN_PATH = "stages/stage32-ex5/MAIN-STATE.json"
EX5_MAIN_BLOB = "ef688b0a2101ec60a48db25567aa386471ab0ea7"
EX5_CROSS_PATH = "stages/stage32-ex5/CROSS-LANE-STATE.json"
EX5_CROSS_BLOB = "0c15a31d8085b50d5ab54a92c5ff7fa96e7535e0"
EX5_CROSS_CANONICAL = "7d3e06425e8672cb31a1c39c871b2e11964a662cffa29d0157623b8808710a9a"

DEMAND_ID = "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_bytes(raw: bytes) -> dict:
    return json.loads(raw.decode("utf-8"))


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked_local(path: Path, expected_blob: str | None, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing local file: {path}")
    raw = path.read_bytes()
    if expected_blob is not None:
        req(git_blob_bytes(raw) == expected_blob, f"local blob drift: {path}")
    obj = load_bytes(raw)
    req(obj.get("canonical_sha256_without_this_field") == expected_canonical, f"stored canonical drift: {path}")
    req(canonical(obj) == expected_canonical, f"canonical drift: {path}")
    return obj


def ensure_commit(sha: str) -> None:
    probe = subprocess.run(
        ["git", "-C", str(REPO), "cat-file", "-e", f"{sha}^{{commit}}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if probe.returncode == 0:
        return
    subprocess.run(
        ["git", "-C", str(REPO), "fetch", "--no-tags", "--depth=1", "origin", sha],
        check=True,
    )
    subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", f"{sha}^{{commit}}"], check=True)


def checked_remote(sha: str, path: str, expected_blob: str, expected_canonical: str | None = None) -> dict:
    ensure_commit(sha)
    raw = subprocess.check_output(["git", "-C", str(REPO), "show", f"{sha}:{path}"])
    req(git_blob_bytes(raw) == expected_blob, f"remote blob drift: {sha}:{path}")
    obj = load_bytes(raw)
    if expected_canonical is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canonical, f"remote stored canonical drift: {sha}:{path}")
        req(canonical(obj) == expected_canonical, f"remote canonical drift: {sha}:{path}")
    return obj


def main() -> None:
    n387 = checked_local(HERE.parent / "N387" / "STATE.json", EXPECTED_N387_BLOB, EXPECTED_N387_CANONICAL)
    req(
        n387["status"] == "BC2_37_HOSTILE_AUDIT_PASS_OBSERVED_HPADJ_P0_DEMAND_STILL_UNACKNOWLEDGED_WAIT_FOR_EX5_MAINBATCH_NO_CREDIT",
        "N387 parent status drift",
    )
    req(n387["routing"]["next_required_external_command"] == "stage32ex5-mainbatch", "N387 producer route drift")
    req(n387["routing"]["178_may_promote_hpadj01_now"] is False, "N387 HPADJ firewall drift")

    n388 = checked_local(HERE / "STATE.json", None, EXPECTED_N388_CANONICAL)

    main_cross = checked_remote(MAIN_COORD_HEAD, MAIN_CROSS_PATH, MAIN_CROSS_BLOB, MAIN_CROSS_CANONICAL)
    monitor = checked_remote(MAIN_COORD_HEAD, MONITOR_PATH, MONITOR_BLOB, MONITOR_CANONICAL)
    ex5_main = checked_remote(EX5_HEAD, EX5_MAIN_PATH, EX5_MAIN_BLOB)
    ex5_cross = checked_remote(EX5_HEAD, EX5_CROSS_PATH, EX5_CROSS_BLOB, EX5_CROSS_CANONICAL)

    req(main_cross["schema"] == "STAGE32_EX5_CROSS_LANE_COORDINATION_STATE_V5_HPADJ_OPEN_PRODUCER_DIVERSION_DETECTED", "MAIN synchronized EX5 cross-lane schema drift")
    req(main_cross["status"] == "OPEN_P0_HPADJ_FULL178_PICARD64_HANDOFF_PRODUCER_DIVERSION_BLOCKED", "MAIN synchronized EX5 cross-lane status drift")
    req(main_cross["open_producer_demands"] == [DEMAND_ID], "MAIN synchronized open-demand set drift")
    req(main_cross["highest_priority_open_demand"] == DEMAND_ID, "MAIN synchronized highest-priority demand drift")
    req(main_cross["coordination_priority"] == "P0_BLOCKING_DOWNSTREAM", "MAIN coordination priority drift")
    req(main_cross["local_route_priority"] == "P2_NORMAL", "MAIN observed local-route priority drift")
    req(main_cross["producer_acknowledged"] is False, "producer unexpectedly acknowledged P0")
    req(main_cross["producer_sync_required"] is True, "producer sync requirement drift")
    req(main_cross["producer_diversion_detected"] is True, "producer diversion detection drift")
    obs = main_cross["producer_observation"]
    req(obs["observed_exact_head"] == EX5_HEAD, "observed EX5 head drift")
    req(obs["observed_registry_contains_hpadj_demand"] is False, "stale producer registry observation drift")
    req(obs["observed_open_producer_demands"] == [], "stale producer open-demand observation drift")
    req(obs["bc2_37_hostile_audit_consumed"] is True, "BC2-37 audit consumption observation drift")
    req(obs["bc2_38_execution_authorized"] is True, "BC2-38 stale-state authorization observation drift")
    req(obs["bc2_38_workflow_run"] == 34742297972, "BC2-38 workflow identity drift")
    req(obs["bc2_38_compute_job"] == 103683975497, "BC2-38 compute job identity drift")
    req(obs["post_demand_new_lower_priority_research_detected"] is True, "lower-priority diversion observation drift")
    req(obs["classification"] == "P0_PREEMPTION_VIOLATION_EX5_STARTED_BC2_38_WITH_STALE_CROSS_LANE_REGISTRY", "diversion classification drift")
    repair = main_cross["required_repair"]
    req(repair["stop_new_p2_research"] is True, "P2 stop requirement drift")
    req(repair["do_not_promote_bc2_38_to_main"] is True, "BC2-38 promotion firewall drift")
    req(repair["synchronize_current_cross_lane_registry"] is True, "registry sync requirement drift")
    req(repair["acknowledge_hpadj_p0_before_next_local_research"] is True, "P0 acknowledgement requirement drift")
    req(repair["next_producer_command"] == "stage32ex5-mainbatch", "repair command drift")
    req(main_cross["credit_firewall"]["bc2_38_main_credit"] is False, "MAIN cross-lane BC2-38 credit unexpectedly open")
    req(main_cross["credit_firewall"]["merge_authorized"] is False, "MAIN cross-lane merge firewall drift")

    req(monitor["schema"] == "STAGE32_MAIN_HPADJ04_EX5_PRODUCER_SYNC_MONITOR_V3_P0_PREEMPTION_VIOLATION", "producer monitor schema drift")
    req(monitor["status"] == "EX5_P0_PREEMPTION_VIOLATION_MAIN_FAIL_CLOSED_WAIT", "producer monitor status drift")
    req(monitor["main_observation"]["demand_id"] == DEMAND_ID, "monitor demand id drift")
    req(monitor["main_observation"]["demand_status"] == "OPEN", "monitor demand status drift")
    req(monitor["main_observation"]["demand_priority"] == "P0_BLOCKING_DOWNSTREAM", "monitor demand priority drift")
    req(monitor["producer_observation"]["observed_exact_head"] == EX5_HEAD, "monitor EX5 head drift")
    req(monitor["producer_observation"]["producer_cross_lane_sync_performed"] is False, "monitor producer sync drift")
    req(monitor["violation"]["producer_diversion_violation_asserted"] is True, "monitor violation assertion drift")
    req(monitor["violation"]["new_lower_priority_research_after_demand_detected"] is True, "monitor post-demand research observation drift")
    req(monitor["violation"]["local_route_priority"] == "P2_NORMAL", "monitor local priority drift")
    req(monitor["violation"]["blocking_route_priority"] == "P0_BLOCKING_DOWNSTREAM", "monitor blocking priority drift")
    req(monitor["violation"]["bc2_38_must_not_be_promoted_to_main"] is True, "monitor BC2-38 promotion firewall drift")
    req(monitor["violation"]["bc2_38_result_does_not_satisfy_hpadj_demand"] is True, "monitor HPADJ satisfaction firewall drift")
    req(monitor["observed_ci"]["producer_head_main_startup_conclusion"] == "FAILURE", "producer startup failure observation drift")
    req(monitor["observed_ci"]["producer_head_claim_frontier_conclusion"] == "FAILURE", "producer claim-frontier failure observation drift")
    req(monitor["next_gate"]["next_producer_command"] == "stage32ex5-mainbatch", "monitor next producer command drift")
    req(monitor["next_gate"]["main_remains_blocked"] is True, "monitor MAIN block drift")
    for key, value in monitor["firewalls"].items():
        req(value is False, f"monitor firewall unexpectedly opened: {key}")

    req(ex5_cross["schema"] == "STAGE32_EX5_CROSS_LANE_COORDINATION_STATE_V2_SATISFIED", "EX5 stale cross-lane schema drift")
    req(ex5_cross["open_producer_demands"] == [], "EX5 stale cross-lane unexpectedly sees current P0")
    req(DEMAND_ID not in ex5_cross["satisfied_producer_demands"], "EX5 stale cross-lane unexpectedly satisfies current P0")
    req(ex5_cross["credit_firewall"]["merge_authorized"] is False, "EX5 stale cross-lane merge firewall drift")

    req(ex5_main["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V29_BC2_37_AUDIT_CONSUMED_BC2_38_EXECUTION", "EX5 current main-state schema drift")
    req(ex5_main["cross_lane_routing"]["registry_blob_sha"] == "bbf4fc2460bad22c65359bc17aa89f8717e259a2", "EX5 stale registry blob drift")
    req(ex5_main["cross_lane_routing"]["open_ex5_producer_demand_count"] == 0, "EX5 stale demand count drift")
    req(ex5_main["cross_lane_routing"]["local_bc2_38_execution_may_continue"] is True, "EX5 stale BC2-38 route drift")
    req(ex5_main["current"]["leaf"] == "BC2_38_REFINE_REMAINING_FRESH_UNKNOWN_SET", "EX5 BC2-38 leaf drift")
    req(ex5_main["current"]["status"] == "BC2_38_TARGETED_REPLAY_EXECUTION_AUTHORIZED", "EX5 BC2-38 stale authorization drift")
    req(ex5_main["frontier"]["e8_bc2_37_audited"] is True, "EX5 BC2-37 audited flag drift")
    req(ex5_main["frontier"]["e8_bc2_37_remaining_unknown_count"] == 34, "EX5 BC2-37 remaining count drift")
    req(ex5_main["frontier"]["e8_known_parent_unsat_count_lower_bound"] == 7302, "EX5 lower bound drift")
    req(ex5_main["intermediate_audit_boundary"]["bc2_38_execution_authorized"] is True, "EX5 BC2-38 execution authorization drift")
    req(ex5_main["next_step"]["main_promotion_authorized"] is False, "EX5 premature MAIN promotion")
    req(ex5_main["next_step"]["merge_authorized"] is False, "EX5 premature merge authorization")

    req(n388["status"] == "EX5_BC2_38_LOWER_PRIORITY_ROUTE_STARTED_WITH_STALE_REGISTRY_WHILE_HPADJ_P0_OPEN_FAIL_CLOSED_DISARM_AND_ACK_REQUIRED_NO_CREDIT", "N388 status drift")
    req(n388["main_coordination"]["exact_head"] == MAIN_COORD_HEAD, "N388 MAIN coordination head drift")
    req(n388["main_coordination"]["demand_id"] == DEMAND_ID, "N388 demand drift")
    req(n388["main_coordination"]["producer_acknowledged"] is False, "N388 producer acknowledgement drift")
    req(n388["main_coordination"]["producer_diversion_detected"] is True, "N388 diversion flag drift")
    req(n388["producer_diversion"]["observed_exact_head"] == EX5_HEAD, "N388 producer head drift")
    req(n388["producer_diversion"]["classification"] == obs["classification"], "N388 diversion classification mismatch")
    req(n388["firewall"]["bc2_38_execution_authorized_under_current_coordination"] is False, "N388 current-coordination authorization firewall drift")
    req(n388["firewall"]["bc2_38_output_may_be_promoted_to_main_now"] is False, "N388 BC2-38 promotion firewall drift")
    req(n388["firewall"]["bc2_38_output_satisfies_hpadj_demand"] is False, "N388 HPADJ satisfaction firewall drift")
    req(n388["firewall"]["bc2_38_output_may_grant_178_pruning_credit"] is False, "N388 pruning firewall drift")
    req(n388["firewall"]["178_must_not_duplicate_ex5_producer_work"] is True, "N388 no-duplication firewall drift")
    req(n388["firewall"]["178_heavy_compute_authorized"] is False, "N388 heavy-compute firewall drift")
    req(n388["firewall"]["n101_remains_stopped"] is True, "N388 illegally reopens N101")
    req(n388["required_repair"]["next_external_command"] == "stage32ex5-mainbatch", "N388 repair command drift")
    req(n388["required_repair"]["disarm_or_retire_bc2_38_run_authorization"] is True, "N388 disarm requirement drift")
    req(n388["required_repair"]["acknowledge_hpadj_p0_before_next_local_research"] is True, "N388 P0 acknowledgement requirement drift")
    for key, value in n388["credit"].items():
        req(value is False, f"N388 credit unexpectedly opened: {key}")

    print(json.dumps({
        "verdict": "PASS_N388_EX5_BC2_38_P0_PREEMPTION_VIOLATION_FIREWALL",
        "main_coordination_head": MAIN_COORD_HEAD,
        "producer_head": EX5_HEAD,
        "hpadj_demand": DEMAND_ID,
        "demand_status": "OPEN",
        "demand_priority": "P0_BLOCKING_DOWNSTREAM",
        "producer_acknowledged": False,
        "producer_diversion_detected": True,
        "bc2_38_current_coordination_authorized": False,
        "bc2_38_main_credit": False,
        "n388_additional_pruning_terminals": 0,
        "next_external_command": "stage32ex5-mainbatch",
        "n101_reopened": False,
        "full178_complete": False,
        "stage32_closed": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
