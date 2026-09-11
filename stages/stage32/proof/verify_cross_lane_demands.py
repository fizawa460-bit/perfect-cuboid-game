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

EXPECTED_REGISTRY_CANONICAL = "49a9c51c3d428afb97eade9b996f3e5b52337a565048a1cdd9a8e6bcf4294848"
EXPECTED_EX5_STATE_CANONICAL = "39bb944f978dbc6a63e77ccac35a5ea51414ac8ba8a13a1b220f05613047a90d"
EXPECTED_CUT_STATE_CANONICAL = "2f9e88e64aa6cf14e9b212ded549dd943844aa771d53e182c78573408082b360"
REQUIRED_LANES = {"MAIN","EX1","EX2","EX3","EX4","EX5","EX6","CUT","32-01-178","MB"}
DEMAND_ID = "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
PRIORITY = {"P0_BLOCKING_DOWNSTREAM":0,"P1_HIGH":1,"P2_NORMAL":2,"P3_LOW":3}


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


def verify_satisfied_artifact(demand: dict) -> None:
    sat = demand["satisfying_artifact"]
    req(all(sat[k] for k in ("path","blob_sha1","canonical_sha256")),
        f"SATISFIED demand missing artifact identity: {demand['demand_id']}")
    path = REPO / sat["path"]
    req(path.is_file(), f"SATISFIED artifact path missing: {path}")
    req(git_blob_sha(path) == sat["blob_sha1"],
        f"SATISFIED artifact blob drift: {demand['demand_id']}")
    try:
        artifact = load(path)
    except Exception as exc:
        raise SystemExit(f"FAIL: SATISFIED canonical artifact is not JSON: {demand['demand_id']}: {exc}")
    req(artifact.get("canonical_sha256_without_this_field") == sat["canonical_sha256"],
        f"SATISFIED artifact stored canonical drift: {demand['demand_id']}")
    req(csha(artifact) == sat["canonical_sha256"],
        f"SATISFIED artifact recomputed canonical drift: {demand['demand_id']}")


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
    req(d["status"] == "OPEN", "CUT192 demand unexpectedly not OPEN")
    req(d["producer_lane"] == "EX5" and d["consumer_lane"] == "CUT", "CUT192 producer/consumer drift")
    req(d["priority"] == "P0_BLOCKING_DOWNSTREAM", "CUT192 priority drift")
    req(DEMAND_ID in lane_rows["EX5"]["open_demand_refs"], "EX5 lane adapter lacks CUT192 demand")
    req(DEMAND_ID in lane_rows["CUT"]["open_demand_refs"], "CUT lane adapter lacks CUT192 demand")
    pop = d["source_population_semantics"]
    req(pop["must_be_current_main_surviving"] is True and pop["must_be_disjoint_from_cut191_first_block"] is True, "CUT192 source population semantics weakened")
    req(pop["consumed_cut191_first_block_rank_range"] == [0,112], "CUT191 first-block identity drift")
    req(pop["authoritative_remaining_terminals"] == 65396964990500233636101, "post-CUT191 authority drift")

    main_state = load(MAIN_STATE)
    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == pop["authoritative_remaining_strata"],
        "demand source strata do not match live MAIN-STATE")
    req(frontier["authoritative_remaining_terminals"] == pop["authoritative_remaining_terminals"],
        "demand source terminals do not match live MAIN-STATE")
    req(frontier["cut191_main_pruning_credit"] is True,
        "CUT191 is not consumed in live MAIN-STATE")
    req(frontier["cut191_incremental_rejected_terminals"] == 113,
        "CUT191 live MAIN-STATE credit drift")
    req(frontier["cut191_remaining_terminals"] == pop["authoritative_remaining_terminals"],
        "CUT191 live post-consumption count disagrees with demand population")

    ex5 = load(REPO / reg["lane_coordination_state_paths"]["EX5"])
    req(ex5["canonical_sha256_without_this_field"] == EXPECTED_EX5_STATE_CANONICAL and csha(ex5) == EXPECTED_EX5_STATE_CANONICAL, "EX5 coordination state canonical drift")
    req(DEMAND_ID in ex5["open_producer_demands"], "EX5 did not acknowledge OPEN producer demand")
    req(ex5["highest_priority_open_demand"] == DEMAND_ID, "EX5 highest-priority demand drift")
    req(ex5["producer_acknowledged"] is True, "EX5 producer acknowledgement missing")
    req(ex5["local_route_deferred_while_demand_open"] is True, "EX5 still prioritizes local route over P0 demand")
    req(PRIORITY[ex5["coordination_priority"]] < PRIORITY[ex5["local_route_priority"]], "EX5 demand priority does not dominate local route")

    cut = load(REPO / reg["lane_coordination_state_paths"]["CUT"])
    req(cut["canonical_sha256_without_this_field"] == EXPECTED_CUT_STATE_CANONICAL and csha(cut) == EXPECTED_CUT_STATE_CANONICAL, "CUT coordination state canonical drift")
    req(DEMAND_ID in cut["waiting_on"], "CUT waiting edge missing")
    req(cut["must_not_rebuild_producer_interface"] is True, "CUT may duplicate producer work")
    req(cut["reentry_on_satisfied"] is True, "CUT re-entry rule missing")
    req(cut["cut191_main_consumed"] is True and cut["cut191_consumption_is_not_blocked"] is True, "CUT191 incorrectly blocked by CUT192 demand")

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
        "cut192_waits_on_ex5":True,
        "ex5_priority_override":True,
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
