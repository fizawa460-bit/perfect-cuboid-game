#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
REPO = STAGE.parents[1]
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
LANES = HERE / "LANE-ADAPTERS.json"
MAIN_STATE = STAGE / "MAIN-STATE.json"

EXPECTED_REGISTRY_CANONICAL = "ae916d01b2690b2f86f06c754c83d396f947d4d2ed5df0b3adbdc42d10c2e62a"
EXPECTED_EX5_STATE_CANONICAL = "7d3e06425e8672cb31a1c39c871b2e11964a662cffa29d0157623b8808710a9a"
EXPECTED_CUT_STATE_CANONICAL = "fb19ce30a734a611390b05a08d774e9d4b3215a7b962eb1fb9a12edd03b48de7"
EXPECTED_RECEIPT_PATH = "stages/stage32/proof/CUT192-EX5-E8-HANDOFF-SATISFIED.json"
EXPECTED_RECEIPT_BLOB = "b8ff5a4b962c24a6e4f4bca5621cbdb79f6d4781"
EXPECTED_RECEIPT_CANONICAL = "011265b32e83f269c8a46d9556982bbe7da3377fa15d3ffbf019eb11d1f16e42"
REQUIRED_LANES = {"MAIN","EX1","EX2","EX3","EX4","EX5","EX6","CUT","32-01-178","MB"}
DEMAND_ID = "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
PRIORITY = {"P0_BLOCKING_DOWNSTREAM":0,"P1_HIGH":1,"P2_NORMAL":2,"P3_LOW":3}
CUT194_INCREMENT = 26442
POST_CUT194_REMAINING = 65396964990500233609659

EXPECTED_INTERFACE_LOCKS = {
    "stages/stage32-ex5/cut-handoff/e8-terminal-population-preflight.json": "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py": "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    "stages/stage32-ex5/cut-handoff/verify_e8_terminal_population_adapter.py": "8fe802444ca8c92a80058555eaf431f0c1a52c76",
    "stages/stage32-ex5/runkeys/e8-cut-handoff-wave.json": "3d1796fc09eabf507b8293bdad7421e05dff5723",
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def csha(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def detect_cycle(edges: dict[str, set[str]]) -> None:
    visiting: set[str] = set()
    done: set[str] = set()
    def dfs(v: str) -> None:
        if v in visiting:
            raise SystemExit(f"FAIL: cyclic cross-lane wait detected at {v}")
        if v in done:
            return
        visiting.add(v)
        for w in edges.get(v, set()):
            dfs(w)
        visiting.remove(v)
        done.add(v)
    for v in edges:
        dfs(v)


def verify_satisfied_artifact(demand: dict) -> dict:
    sat = demand["satisfying_artifact"]
    req(all(sat.get(k) for k in ("path","blob_sha1","canonical_sha256")), f"SATISFIED demand missing artifact identity: {demand['demand_id']}")
    path = REPO / sat["path"]
    req(path.is_file(), f"SATISFIED artifact path missing: {path}")
    req(git_blob_sha(path) == sat["blob_sha1"], f"SATISFIED artifact blob drift: {demand['demand_id']}")
    artifact = load(path)
    req(artifact.get("canonical_sha256_without_this_field") == sat["canonical_sha256"], f"SATISFIED artifact stored canonical drift: {demand['demand_id']}")
    req(csha(artifact) == sat["canonical_sha256"], f"SATISFIED artifact recomputed canonical drift: {demand['demand_id']}")
    return artifact


def verify_cut192_receipt(receipt: dict) -> None:
    req(receipt["schema"] == "STAGE32_CUT192_EX5_E8_HANDOFF_SATISFIED_RECEIPT_V1", "CUT192 receipt schema drift")
    req(receipt["demand_id"] == DEMAND_ID and receipt["status"] == "SATISFIED", "CUT192 receipt demand/status drift")
    req(receipt["producer_lane"] == "EX5" and receipt["consumer_lane"] == "CUT", "CUT192 receipt lane drift")

    prod = receipt["producer"]
    req(prod["pr"] == 1776, "CUT192 producer PR drift")
    req(prod["exact_head"] == "fd00531181228c9f367a49eb61ddc3af6ab84ab3", "CUT192 producer exact head drift")
    req(prod["exact_head_ci_run"] == 34598945799 and prod["ci_conclusion"] == "SUCCESS", "CUT192 producer exact-head CI drift")
    req(prod["adapter_verifier_step_conclusion"] == "SUCCESS" and prod["handoff_job_conclusion"] == "SUCCESS", "CUT192 producer handoff checks not successful")

    locks = {row["path"]: row["blob_sha1"] for row in receipt["interface_source_locks"]}
    req(locks == EXPECTED_INTERFACE_LOCKS, "CUT192 interface source-lock set drift")

    sem = receipt["interface_semantics"]
    req(sem["artifact_type"] == "SOURCE_LOCKED_EXACT_TERMINAL_TO_PICARD64_COMPLETION_INTERFACE", "CUT192 interface type drift")
    req(sem["handoff_universe_blocks"] == 7596 and sem["handoff_universe_terminals"] == 858348, "CUT192 handoff universe drift")
    req(sem["random_access_by_exceptional_rank"] is True and sem["terminal_block_width"] == 113, "CUT192 rank/unrank semantics drift")
    req(sem["preferred_wave_survivor_offset_range"] == [1,255] and sem["preferred_wave_block_count"] == 255 and sem["preferred_wave_terminal_count"] == 28815, "CUT192 first wave semantics drift")
    req(sem["preferred_wave_block_index_stream_sha256"] == "68ca7b27ffeceb52c35942449ca47105fd4a74757575544033454c3c9be514ea", "CUT192 wave block stream drift")

    art = receipt["producer_wave_artifact"]
    req(art["artifact_id"] == 10263148684, "CUT192 producer artifact id drift")
    req(art["digest"] == "sha256:df48610fbf8d6cd11640f8f3feb534256b307e6ea803688267a33cb972cfba7f", "CUT192 producer artifact digest drift")
    req(art["canonical_sha256"] == "7344a7c23ed83b66046d4a72a27a0679ab12fdc05cb41d8f6cdcacec6adcaa01", "CUT192 producer artifact canonical drift")

    bridge = receipt["current_main_bridge"]
    req(bridge["authority_exact_head"] == "6d63d798adb50dd4efc5f0d5abc553b3dfa23060" and bridge["authority_hostile_reaudit_review_id"] == 5178420739, "CUT192 MAIN authority receipt drift")
    req(bridge["authoritative_remaining_strata"] == 17128 and bridge["authoritative_remaining_terminals"] == 65396964990500233636101, "CUT192 MAIN population receipt drift")
    req(bridge["n356_preserves_handoff_population"] is True and bridge["preferred_wave_disjoint_from_cut191"] is True and bridge["preferred_wave_first_source_block_index"] == 1, "CUT192 current-MAIN/disjoint bridge drift")

    reentry = receipt["consumer_reentry"]
    req(reentry["pr"] == 1786 and reentry["head_at_satisfaction_sync"] == "702ed10b85948c562ee87ad7cc26c6554d1ef4f8" and reentry["node"] == "CUT193" and reentry["status"] == "REENTERED_CONSUMING_SATISFIED_INTERFACE" and reentry["stage32_main_credit"] is False, "CUT193 re-entry receipt drift")

    fw = receipt["audit_and_credit_firewall"]
    req(fw["demand_satisfaction_is_hostile_audit"] is False and fw["demand_satisfaction_grants_mathematical_credit"] is False and fw["producer_interface_requires_hostile_audit_before_mathematical_credit"] is True and fw["cut193_candidate_requires_own_hostile_audit"] is True and fw["cut193_requires_separate_main_consumption_for_main_credit"] is True and fw["cut191_main_credit_remains_consumed"] is True and fw["full178_complete"] is False and fw["stage32_closed"] is False and fw["merge_authorized"] is False, "CUT192/CUT193 credit firewall drift")


def main() -> None:
    reg = load(REGISTRY)
    req(reg["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V1", "registry schema drift")
    req(reg["canonical_sha256_without_this_field"] == EXPECTED_REGISTRY_CANONICAL, "registry stored canonical drift")
    req(csha(reg) == EXPECTED_REGISTRY_CANONICAL, "registry recomputed canonical drift")
    req(reg["contract"]["claim_dag_separation"] is True, "claim/demand DAG separation lost")
    req(reg["contract"]["satisfaction_does_not_grant_credit"] is True, "demand satisfaction credit firewall lost")

    lanes = load(LANES)
    lane_rows = {x["lane"]: x for x in lanes["lanes"]}
    req(REQUIRED_LANES == set(lane_rows), f"lane enrollment drift: got {sorted(lane_rows)}")
    req(lanes["contract"]["cross_lane_demand_registry"] == "stages/stage32/proof/CROSS-LANE-DEMANDS.json", "lane registry demand pointer drift")
    req(lanes["contract"]["cross_lane_separation_rule"].startswith("The claim DAG and cross-lane demand DAG are independent"), "lane registry separation rule drift")
    req(lane_rows["MAIN"]["demand_role"] == "GLOBAL_MONITOR", "MAIN demand monitor role missing")
    req(lane_rows["EX5"]["demand_role"] == "PRODUCER", "EX5 producer role missing")
    req(lane_rows["CUT"]["demand_role"] == "CONSUMER", "CUT consumer role missing")
    req(lane_rows["32-01-178"]["startup_path"] == "stages/stage32/32-01-178/MAIN-START-HERE.md", "178 demand-aware startup path drift")

    for p in (HERE / "CLAIM-REGISTRY.json", HERE / "ACTIVE-FRONTIER.json"):
        req("S32.DEMAND." not in p.read_text(encoding="utf-8"), f"demand ID leaked into claim DAG: {p.name}")

    demands = reg["demands"]
    ids = [d["demand_id"] for d in demands]
    req(len(ids) == len(set(ids)), "duplicate demand_id")
    edges: dict[str, set[str]] = {}
    by_id = {d["demand_id"]: d for d in demands}
    for d in demands:
        req(d["status"] in {"OPEN","SATISFIED","OBSOLETE"}, f"bad demand status {d['demand_id']}")
        req(d["priority"] in PRIORITY, f"bad priority {d['demand_id']}")
        prod, cons = d["producer_lane"], d["consumer_lane"]
        req(prod in lane_rows, f"orphan producer {prod}")
        req(cons in lane_rows, f"orphan consumer {cons}")
        req(prod != cons, f"self-demand forbidden {d['demand_id']}")
        if d["status"] == "OPEN":
            edges.setdefault(cons, set()).add(prod)
            sat = d["satisfying_artifact"]
            req(all(sat[k] is None for k in ("path","blob_sha1","canonical_sha256","audited_exact_head","audit_review_id")), "OPEN demand has fake satisfying artifact")
        elif d["status"] == "SATISFIED":
            verify_satisfied_artifact(d)
    detect_cycle(edges)

    d = by_id[DEMAND_ID]
    req(d["status"] == "SATISFIED", "CUT192 demand is not synchronized SATISFIED")
    req(d["producer_lane"] == "EX5" and d["consumer_lane"] == "CUT", "CUT192 producer/consumer drift")
    req(d["priority"] == "P0_BLOCKING_DOWNSTREAM", "CUT192 priority drift")
    req(DEMAND_ID not in lane_rows["EX5"].get("open_demand_refs", []), "EX5 lane adapter retains stale OPEN demand ref")
    req(DEMAND_ID not in lane_rows["CUT"].get("open_demand_refs", []), "CUT lane adapter retains stale OPEN demand ref")
    req(DEMAND_ID in lane_rows["EX5"].get("satisfied_demand_refs", []), "EX5 lane adapter lacks SATISFIED demand ref")
    req(DEMAND_ID in lane_rows["CUT"].get("satisfied_demand_refs", []), "CUT lane adapter lacks SATISFIED demand ref")

    sat = d["satisfying_artifact"]
    req(sat["path"] == EXPECTED_RECEIPT_PATH and sat["blob_sha1"] == EXPECTED_RECEIPT_BLOB and sat["canonical_sha256"] == EXPECTED_RECEIPT_CANONICAL, "CUT192 satisfaction receipt identity drift")
    req(sat["producer_exact_head"] == "fd00531181228c9f367a49eb61ddc3af6ab84ab3" and sat["producer_ci_run"] == 34598945799, "CUT192 producer identity drift")
    req(sat["consumer_reentry_pr"] == 1786 and sat["consumer_reentry_head"] == "702ed10b85948c562ee87ad7cc26c6554d1ef4f8", "CUT192 consumer re-entry identity drift")
    req(sat["audited_exact_head"] is None and sat["audit_review_id"] is None, "operational satisfaction must not masquerade as hostile audit")

    receipt_path = REPO / EXPECTED_RECEIPT_PATH
    req(git_blob_sha(receipt_path) == EXPECTED_RECEIPT_BLOB, "CUT192 receipt blob drift")
    receipt = load(receipt_path)
    req(receipt["canonical_sha256_without_this_field"] == EXPECTED_RECEIPT_CANONICAL and csha(receipt) == EXPECTED_RECEIPT_CANONICAL, "CUT192 receipt canonical drift")
    verify_cut192_receipt(receipt)

    pop = d["source_population_semantics"]
    req(pop["must_be_current_main_surviving"] is True and pop["must_be_disjoint_from_cut191_first_block"] is True, "CUT192 source population semantics weakened")
    req(pop["consumed_cut191_first_block_rank_range"] == [0,112], "CUT191 first-block identity drift")
    req(pop["authoritative_remaining_terminals"] == 65396964990500233636101, "post-CUT191 authority drift")

    main_state = load(MAIN_STATE)
    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == pop["authoritative_remaining_strata"], "demand source strata do not match live MAIN-STATE")
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 is not consumed in live MAIN-STATE")
    req(frontier["cut191_incremental_rejected_terminals"] == 113, "CUT191 live MAIN-STATE credit drift")
    req(frontier["cut191_remaining_terminals"] == pop["authoritative_remaining_terminals"], "CUT191 live post-consumption count disagrees with demand population")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 is not consumed in live MAIN-STATE")
    req(frontier["cut194_incremental_rejected_terminals"] == CUT194_INCREMENT, "CUT194 live MAIN-STATE credit drift")
    req(frontier["authoritative_remaining_terminals"] == POST_CUT194_REMAINING, "post-CUT194 live MAIN-STATE count drift")
    req(pop["authoritative_remaining_terminals"] - frontier["authoritative_remaining_terminals"] == CUT194_INCREMENT, "live MAIN delta is not exactly CUT194")
    req(frontier["cut194_remaining_terminals"] == frontier["authoritative_remaining_terminals"], "CUT194 remaining count disagrees with live MAIN authority")

    cut194_lock = main_state["source_locks"]["cut194"]
    cut194_path = REPO / cut194_lock["result_path"]
    req(cut194_path.is_file(), "CUT194 source-locked result missing")
    req(git_blob_sha(cut194_path) == cut194_lock["result_blob_sha1"], "CUT194 source-locked result blob drift")
    cut194 = load(cut194_path)
    req(csha(cut194) == cut194_lock["result_canonical_sha256"], "CUT194 source-locked result canonical drift")
    preferred_wave = receipt["interface_semantics"]["preferred_wave_survivor_offset_range"]
    cut194_wave = cut194["target"]["survivor_offset_range"]
    req(preferred_wave == [1,255] and cut194_wave == [256,510], "CUT192/CUT194 wave identity drift")
    req(preferred_wave[1] < cut194_wave[0], "CUT194 overlaps the satisfied CUT192 preferred wave")
    req(cut194["target"]["cut193_wave1_disjoint"] is True, "CUT194 producer did not certify CUT193/CUT192-wave disjointness")

    ex5 = load(REPO / reg["lane_coordination_state_paths"]["EX5"])
    req(ex5["canonical_sha256_without_this_field"] == EXPECTED_EX5_STATE_CANONICAL and csha(ex5) == EXPECTED_EX5_STATE_CANONICAL, "EX5 coordination state canonical drift")
    req(ex5["status"] == "SATISFIED_HANDOFF_COMPLETE", "EX5 satisfaction state drift")
    req(ex5["open_producer_demands"] == [] and DEMAND_ID in ex5["satisfied_producer_demands"], "EX5 producer demand transition drift")
    req(ex5["highest_priority_open_demand"] is None, "EX5 stale highest-priority OPEN demand")
    req(ex5["local_route_deferred_while_demand_open"] is False, "EX5 remains artificially deferred after satisfaction")
    req(ex5["producer_acknowledged"] is True, "EX5 producer acknowledgement missing")
    ex5r = ex5["handoff_receipt"]
    req(ex5r["path"] == EXPECTED_RECEIPT_PATH and ex5r["blob_sha1"] == EXPECTED_RECEIPT_BLOB and ex5r["canonical_sha256"] == EXPECTED_RECEIPT_CANONICAL, "EX5 handoff receipt identity drift")

    cut = load(REPO / reg["lane_coordination_state_paths"]["CUT"])
    req(cut["canonical_sha256_without_this_field"] == EXPECTED_CUT_STATE_CANONICAL and csha(cut) == EXPECTED_CUT_STATE_CANONICAL, "CUT coordination state canonical drift")
    req(cut["status"] == "REENTERED_CONSUMING_SATISFIED_DEMAND", "CUT re-entry state drift")
    req(cut["waiting_on"] == [] and DEMAND_ID in cut["consuming_satisfied_demands"], "CUT stale wait / missing satisfied consumption")
    req(cut["must_not_rebuild_producer_interface"] is True, "CUT may duplicate producer work")
    req(cut["reentry_on_satisfied"] is True and cut["reentry_consumed"] is True, "CUT re-entry transition missing")
    req(cut["current_node"] == "CUT193", "CUT did not re-enter at CUT193")
    req(cut["satisfying_artifact"]["path"] == EXPECTED_RECEIPT_PATH and cut["satisfying_artifact"]["blob_sha1"] == EXPECTED_RECEIPT_BLOB and cut["satisfying_artifact"]["canonical_sha256"] == EXPECTED_RECEIPT_CANONICAL, "CUT satisfying artifact identity drift")
    req(cut["cut191_main_consumed"] is True and cut["cut191_consumption_is_not_blocked"] is True, "CUT191 incorrectly coupled to CUT192/CUT193")

    startup_paths = {
        "MAIN":"stages/stage32/MAIN-START-HERE.md",
        "EX1":"stages/stage32-ex1/MAIN-START-HERE.md",
        "EX2":"stages/stage32-ex2/MAIN-START-HERE.md",
        "EX3":"stages/stage32-ex3/MAIN-START-HERE.md",
        "EX4":"stages/stage32-ex4/MAIN-START-HERE.md",
        "EX5":"stages/stage32-ex5/MAIN-START-HERE.md",
        "EX6":"stages/stage32-ex6/MAIN-START-HERE.md",
        "32-01-178":"stages/stage32/32-01-178/MAIN-START-HERE.md",
        "CUT":"stages/stage32/full178-cut/MAIN-START-HERE.md",
        "MB":"stages/stage32/final-chain/32-03-multibranch/MAIN-START-HERE.md",
    }
    for lane, rel in startup_paths.items():
        t = (REPO / rel).read_text(encoding="utf-8")
        req(lane_rows[lane]["startup_path"] == rel, f"{lane} lane-adapter startup path drift")
        req("stages/stage32/proof/CROSS-LANE-DEMANDS.json" in t, f"{lane} startup missing demand registry")
        req("OPEN demand" in t, f"{lane} startup missing OPEN producer rule")
        req("SATISFIED" in t, f"{lane} startup missing SATISFIED consumer re-entry rule")
        req("does not grant mathematical credit" in t.lower() or "does not grant math credit" in t.lower(), f"{lane} startup missing demand/credit separation")

    for r in reg["audited_result_consumption"]:
        if r["audit_status"] == "PASS" and r["main_consumption_required"]:
            req(r["main_consumed"] is True, f"audited result awaiting MAIN consumption: {r['result_id']}")
    cut191 = reg["audited_result_consumption"][0]
    req(cut191["result_id"] == "S32.CUT191.FIRST_BLOCK.113_TERMINAL_PRUNING.V1", "CUT191 consumption record missing")
    req(cut191["credited_incremental_rejected_terminals"] == 113, "CUT191 credit drift")
    req(cut191["authoritative_remaining_terminals_after_consumption"] == 65396964990500233636101, "CUT191 post-consumption count drift")
    req(cut191["main_synchronized_reaudit_review_id"] == 5178420739, "CUT191 synchronized-head audit identity drift")

    fw = reg["credit_firewall"]
    req(all(v is False for v in fw.values()), "cross-lane registry grants forbidden credit/merge")

    print(json.dumps({
        "verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION",
        "open_demands":[d["demand_id"] for d in demands if d["status"] == "OPEN"],
        "satisfied_demands":[d["demand_id"] for d in demands if d["status"] == "SATISFIED"],
        "cut192_satisfied":True,
        "cut193_reentered":True,
        "cut194_consumed_disjoint_from_cut192_wave":True,
        "ex5_handoff_complete":True,
        "cut191_main_consumed":True,
        "main_population_cross_checked":True,
        "satisfied_artifact_canonical_fail_closed":True,
        "cyclic_wait":False,
        "orphan_demand":False,
        "producer_diversion":False,
        "audited_result_unconsumed":False,
        "demand_status_grants_mathematical_credit":False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
