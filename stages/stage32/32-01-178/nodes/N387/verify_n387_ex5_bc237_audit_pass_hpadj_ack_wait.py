#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]

EXPECTED_N386_BLOB = "d8f092cfac4a32c95ded9f2208126ac8c2d354b9"
EXPECTED_N386_CANONICAL = "66f100b8bcfb8008afd3f59817268ff3d2293001b8746035ac75ffb25b871885"
EXPECTED_N387_CANONICAL = "609a5cf44445a269f201ff1ba2fb0d52b4d4b86677e430fd3ac151811e9fbbca"

MAIN_COORD_HEAD = "68a5220927c60e7bf3fdbe9f1ff937c4b43a25c1"
DEMAND_ID = "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
DEMAND_REGISTRY_PATH = "stages/stage32/proof/CROSS-LANE-DEMANDS.json"
DEMAND_REGISTRY_BLOB = "75982b910ae1f149bc55b766f22ddea77db1f49e"
DEMAND_REGISTRY_CANONICAL = "470168bccfd4130b7de28002f40277002fcf6eda7f8d917b2df57f88879d0668"
MONITOR_PATH = "stages/stage32/management/hpadj-04/PRODUCER-MONITOR.json"
MONITOR_BLOB = "927ba2d2858ebfb3b54c299c6650836d10a6b97e"
MONITOR_CANONICAL = "929c6815ba13236362b9fb233f6aa1148a5253a757b347123a31f76c9640b0cd"

EX5_HEAD = "9852fcec959962607da3290100291a60185e7104"
EX5_AUDIT_REVIEW = 5189412496
EX5_MAIN_STATE_PATH = "stages/stage32-ex5/MAIN-STATE.json"
EX5_MAIN_STATE_BLOB = "93cd25eb0798facfd0eb9d342b681dc8aeaeb020"
EX5_CROSS_LANE_PATH = "stages/stage32-ex5/CROSS-LANE-STATE.json"
EX5_CROSS_LANE_BLOB = "0c15a31d8085b50d5ab54a92c5ff7fa96e7535e0"
EX5_CROSS_LANE_CANONICAL = "7d3e06425e8672cb31a1c39c871b2e11964a662cffa29d0157623b8808710a9a"


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
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def checked_local(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing local file: {path}")
    raw = path.read_bytes()
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
    subprocess.run(
        ["git", "-C", str(REPO), "cat-file", "-e", f"{sha}^{{commit}}"],
        check=True,
    )


def show_bytes(sha: str, path: str) -> bytes:
    ensure_commit(sha)
    return subprocess.check_output(["git", "-C", str(REPO), "show", f"{sha}:{path}"])


def checked_remote(sha: str, path: str, expected_blob: str, expected_canonical: str | None = None) -> dict:
    raw = show_bytes(sha, path)
    req(git_blob_bytes(raw) == expected_blob, f"remote blob drift: {sha}:{path}")
    obj = load_bytes(raw)
    if expected_canonical is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canonical, f"remote stored canonical drift: {sha}:{path}")
        req(canonical(obj) == expected_canonical, f"remote canonical drift: {sha}:{path}")
    return obj


def main() -> None:
    n386 = checked_local(
        HERE.parent / "N386" / "STATE.json",
        EXPECTED_N386_BLOB,
        EXPECTED_N386_CANONICAL,
    )
    req(
        n386["status"]
        == "HPADJ01_EXPLICITLY_EXCLUDES_N372_G1D008_E8_FROM_CHARGED_LOWER_BOUND_NO_TRANSFER_NO_CREDIT",
        "N386 parent status drift",
    )
    req(n386["routing"]["duplicate_ex5_hpadj_terminal_to_picard64_producer_work"] is False, "N386 producer-duplication firewall drift")

    n387_path = HERE / "STATE.json"
    n387 = load_bytes(n387_path.read_bytes())
    req(n387.get("canonical_sha256_without_this_field") == EXPECTED_N387_CANONICAL, "N387 stored canonical drift")
    req(canonical(n387) == EXPECTED_N387_CANONICAL, "N387 canonical drift")

    registry = checked_remote(
        MAIN_COORD_HEAD,
        DEMAND_REGISTRY_PATH,
        DEMAND_REGISTRY_BLOB,
        DEMAND_REGISTRY_CANONICAL,
    )
    monitor = checked_remote(
        MAIN_COORD_HEAD,
        MONITOR_PATH,
        MONITOR_BLOB,
        MONITOR_CANONICAL,
    )
    ex5_cross = checked_remote(
        EX5_HEAD,
        EX5_CROSS_LANE_PATH,
        EX5_CROSS_LANE_BLOB,
        EX5_CROSS_LANE_CANONICAL,
    )
    ex5_main = checked_remote(
        EX5_HEAD,
        EX5_MAIN_STATE_PATH,
        EX5_MAIN_STATE_BLOB,
    )

    demands = [d for d in registry["demands"] if d["demand_id"] == DEMAND_ID]
    req(len(demands) == 1, "HPADJ demand cardinality drift")
    demand = demands[0]
    req(demand["producer_lane"] == "EX5", "HPADJ producer lane drift")
    req(demand["consumer_lane"] == "MAIN", "HPADJ consumer lane drift")
    req(demand["priority"] == "P0_BLOCKING_DOWNSTREAM", "HPADJ demand priority drift")
    req(demand["status"] == "OPEN", "HPADJ demand no longer OPEN at source-locked coordinator head")
    req(demand["satisfying_artifact"] is None, "HPADJ demand unexpectedly has satisfying artifact")
    req(demand["routing"]["producer_acknowledgement_required"] is True, "HPADJ producer acknowledgement no longer required")
    req(demand["routing"]["consumer_waits_without_rebuilding_producer_interface"] is True, "HPADJ consumer wait firewall drift")
    req(demand["main_promotion_requirement"]["demand_satisfaction_auto_promotes_to_main"] is False, "HPADJ demand satisfaction auto-promotion drift")

    req(monitor["status"] == "WAITING_FOR_EX5_PRODUCER_SYNC_NO_DUPLICATION", "HPADJ-04 monitor status drift")
    req(monitor["main_observation"]["demand_id"] == DEMAND_ID, "HPADJ-04 monitor demand drift")
    req(monitor["main_observation"]["demand_status"] == "OPEN", "HPADJ-04 monitor demand status drift")
    req(monitor["main_observation"]["demand_priority"] == "P0_BLOCKING_DOWNSTREAM", "HPADJ-04 monitor priority drift")
    req(monitor["main_observation"]["main_consumer_wait_required"] is True, "HPADJ-04 MAIN wait drift")
    req(monitor["main_observation"]["main_must_not_rebuild_producer_interface"] is True, "HPADJ-04 no-duplication drift")
    req(monitor["producer_observation"]["observed_exact_head"] == EX5_HEAD, "HPADJ-04 producer head drift")
    req(monitor["producer_observation"]["observed_registry_contains_hpadj_demand"] is False, "HPADJ-04 producer registry observation drift")
    req(monitor["producer_observation"]["observed_open_producer_demands"] == [], "HPADJ-04 producer open-demand observation drift")
    req(monitor["producer_observation"]["producer_acknowledged_current_hpadj_demand"] is False, "HPADJ-04 producer acknowledgement observation drift")
    req(monitor["next_gate"]["stage32ex5_audit_is_immediate_producer_command"] is True, "HPADJ-04 audit-gate observation drift")
    req(monitor["next_gate"]["stage32ex5_mainbatch_is_next_after_audit"] is True, "HPADJ-04 post-audit producer route drift")
    for key, value in monitor["firewalls"].items():
        req(value is False, f"HPADJ-04 monitor firewall unexpectedly opened: {key}")

    req(ex5_cross["schema"] == "STAGE32_EX5_CROSS_LANE_COORDINATION_STATE_V2_SATISFIED", "EX5 cross-lane schema drift")
    req(ex5_cross["open_producer_demands"] == [], "EX5 frozen pre-ack state unexpectedly has open demand")
    req(DEMAND_ID not in ex5_cross["satisfied_producer_demands"], "HPADJ demand unexpectedly satisfied at frozen EX5 head")
    req(ex5_cross["satisfied_producer_demands"] == ["S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"], "EX5 frozen satisfied-demand set drift")
    req(ex5_cross["credit_firewall"]["demand_satisfaction_grants_math_credit"] is False, "EX5 demand credit firewall drift")
    req(ex5_cross["credit_firewall"]["merge_authorized"] is False, "EX5 merge firewall drift")

    req(ex5_main["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V28_BC2_37_TARGETED_REPLAY_AUDIT_BOUNDARY", "EX5 BC2-37 schema drift")
    req(ex5_main["current"]["status"] == "BC2_37_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "EX5 BC2-37 frozen status drift")
    req(ex5_main["current"]["next_route"] == "HOSTILE_AUDIT_BC2_37_TARGETED_REPLAY", "EX5 BC2-37 frozen next-route drift")
    req(ex5_main["cross_lane_routing"]["open_ex5_producer_demand_count"] == 0, "EX5 frozen demand count drift")
    req(ex5_main["frontier"]["e8_bc2_37_audited"] is False, "EX5 frozen pre-review audit flag drift")
    req(ex5_main["frontier"]["e8_bc2_37_new_parent_unsat_count"] == 7, "EX5 BC2-37 UNSAT count drift")
    req(ex5_main["frontier"]["e8_bc2_37_remaining_unknown_count"] == 34, "EX5 BC2-37 UNKNOWN count drift")
    req(ex5_main["frontier"]["e8_bc2_37_candidate_known_parent_unsat_count_lower_bound"] == 7302, "EX5 BC2-37 lower-bound drift")
    req(ex5_main["intermediate_audit_boundary"]["freeze_active"] is True, "EX5 audit freeze drift")
    req(ex5_main["intermediate_audit_boundary"]["re_audit_required"] is True, "EX5 pre-review re-audit flag drift")
    req(ex5_main["next_step"]["bc2_38_blocked_until_bc2_37_hostile_audit_pass"] is True, "EX5 BC2-38 block drift")
    req(ex5_main["next_step"]["main_promotion_authorized"] is False, "EX5 premature MAIN promotion")
    req(ex5_main["next_step"]["merge_authorized"] is False, "EX5 premature merge authorization")

    req(
        n387["status"]
        == "BC2_37_HOSTILE_AUDIT_PASS_OBSERVED_HPADJ_P0_DEMAND_STILL_UNACKNOWLEDGED_WAIT_FOR_EX5_MAINBATCH_NO_CREDIT",
        "N387 status drift",
    )
    req(n387["main_coordination"]["exact_head"] == MAIN_COORD_HEAD, "N387 coordinator head drift")
    req(n387["main_coordination"]["demand_id"] == DEMAND_ID, "N387 demand id drift")
    req(n387["main_coordination"]["demand_status"] == "OPEN", "N387 demand status drift")
    req(n387["producer_audit"]["audited_exact_head"] == EX5_HEAD, "N387 producer head drift")
    req(n387["producer_audit"]["hostile_audit_review_id"] == EX5_AUDIT_REVIEW, "N387 external hostile-audit review drift")
    req(n387["producer_audit"]["hostile_audit_status"] == "PASS", "N387 external hostile-audit status drift")
    req(n387["producer_audit"]["known_parent_unsat_lower_bound_after_audit"] == 7302, "N387 producer lower-bound drift")
    req(n387["producer_audit"]["remaining_unknown_count"] == 34, "N387 producer UNKNOWN-count drift")
    req(n387["producer_pre_ack_state"]["producer_acknowledged_hpadj_demand"] is False, "N387 illegally acknowledges HPADJ demand")
    req(n387["routing"]["stage32ex5_audit_gate_resolved"] is True, "N387 failed to recognize BC2-37 audit PASS")
    req(n387["routing"]["next_required_external_command"] == "stage32ex5-mainbatch", "N387 next external command drift")
    req(n387["routing"]["178_duplicates_ex5_producer_work"] is False, "N387 duplicates EX5 producer work")
    req(n387["routing"]["178_may_treat_demand_as_satisfied_now"] is False, "N387 prematurely satisfies HPADJ demand")
    req(n387["routing"]["178_may_promote_hpadj01_now"] is False, "N387 prematurely promotes HPADJ-01")
    req(n387["routing"]["n101_remains_stopped"] is True, "N387 illegally reopens N101")
    req(n387["routing"]["heavy_compute_authorized"] is False, "N387 heavy-compute firewall drift")
    for key, value in n387["credit"].items():
        req(value is False, f"N387 credit unexpectedly opened: {key}")

    print(json.dumps({
        "verdict": "PASS_N387_BC2_37_AUDIT_PASS_HPADJ_P0_ACK_WAIT",
        "main_coordination_head": MAIN_COORD_HEAD,
        "hpadj_demand_id": DEMAND_ID,
        "hpadj_demand_status": "OPEN",
        "hpadj_demand_priority": "P0_BLOCKING_DOWNSTREAM",
        "producer_pr": 1776,
        "producer_audited_exact_head": EX5_HEAD,
        "producer_hostile_audit_review": EX5_AUDIT_REVIEW,
        "producer_bc2_37_known_parent_unsat_lower_bound": 7302,
        "producer_bc2_37_remaining_unknown": 34,
        "producer_acknowledged_hpadj_demand": False,
        "next_required_external_command": "stage32ex5-mainbatch",
        "n387_additional_pruning_terminals": 0,
        "n101_reopened": False,
        "full178_complete": False,
        "stage32_closed": False,
        "merge_authorized": False,
        "next_gate": n387["next_gate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
