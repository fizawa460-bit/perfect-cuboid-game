#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CANDIDATE = HERE / "GRF04-V42-HPADJ20-LOW-D-FULL-QA-HYBRID-CANDIDATE.json"
V40 = HERE / "GRF04-V40-HPADJ20-FULL178-MAIN-BOUND-REPLACEMENT.json"
V41 = HERE / "GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json"
PREFLIGHT = HERE / "HPADJ20-FULL-QA-HISTOGRAM-MAIN-PARALLEL-PREFLIGHT.json"
PILOT = HERE / "HPADJ20-FULL-QA-HISTOGRAM-LOW-D-NUMERICAL-PILOT.json"
PILOT_VERIFIER = HERE / "verify_hpadj20_full_qa_histogram_low_d_numerical_pilot.py"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

CANDIDATE_BLOB = "c333040911a8f0fdadc72adc29788590681fe3bf"
CANDIDATE_CANON = "6fa80592291d0dbc99207ece94ef00146127cb6ea7489e236ad57c7d1f3c6a2d"
V40_BLOB = "f9d984f64d2c428481e082be622848e33407baf1"
V40_CANON = "f330348d1d6aee5417df20e119479c3c2b6b045a2ce96f7d6e4e54ac9a88d53d"
V41_BLOB = "ee6639e2b4a4ad5dd48e964d6a6b055f551e7bd1"
V41_CANON = "ac52c7d4598eba4ef165bed05c5ff12931777052a2b8582c65286ff8067400c7"
PREFLIGHT_BLOB = "0eb5672dea0712cbf5044d5376e60fe233e767c3"
PREFLIGHT_CANON = "0191c14b3fc072a762d1b702408746691cd5fe315ce9f4a0a040b75183bd13a8"
PILOT_BLOB = "ae4449029818f7e2c510e745c6572de72d844371"
PILOT_CANON = "ebc454e2805cf737570ccdf2f50f64595f947b9dbaf15ca39cde9e3c5b905406"
PILOT_VERIFIER_BLOB = "0197f7062df96777396bead619bcff4a7ba4063a"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

V41_HEAD = "2a9fa0ca243d7bbe75d7539ab574d632fdc44981"
V41_STATE_BLOB = "dd7dba27eb062e6a6ad4d440094ba26c290900d7"
V41_STATE_CANON = "b9886a12fc479acae53de4bdff84ee452a208dfb641eec3ea199ee876cb6898c"
V41_STARTUP_BLOB = "d12c7d5c86a2a3d5b95fed6c02321d21bbbee2d8"
V41_WRAPPER_BLOB = "302b1819fe3e7e8f6330fb9d02d28ada0acfbbc6"

BASE_BOUND = 179119009547804181594
CANDIDATE_BOUND = 179119009547802604210
DELTA = 1577384
TESTED_HP20 = 112277634
TESTED_FULL = 110700250
UNCHANGED = 179119009547691903960

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

def lock_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj

def current_state() -> dict:
    obj = json.loads(STATE.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(obj) == stored, "current MAIN state canonical drift")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v41-root", type=Path)
    args = ap.parse_args()

    candidate = lock_json(CANDIDATE, CANDIDATE_BLOB, CANDIDATE_CANON, "V42 candidate receipt")
    v40 = lock_json(V40, V40_BLOB, V40_CANON, "V40 replacement receipt")
    v41 = lock_json(V41, V41_BLOB, V41_CANON, "V41 audit-sync receipt")
    preflight = lock_json(PREFLIGHT, PREFLIGHT_BLOB, PREFLIGHT_CANON, "full-qA structural preflight")
    pilot = lock_json(PILOT, PILOT_BLOB, PILOT_CANON, "full-qA low-d pilot")
    req(blob(PILOT_VERIFIER) == PILOT_VERIFIER_BLOB, "full-qA low-d pilot verifier drift")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.v41_root is not None:
        root = args.v41_root
        req((root / "stages/stage32/MAIN-STATE.json").is_file(), "missing exact V41 predecessor state")
        old_state = json.loads((root / "stages/stage32/MAIN-STATE.json").read_text(encoding="utf-8"))
        req(blob(root / "stages/stage32/MAIN-STATE.json") == V41_STATE_BLOB,
            "V41 predecessor state blob drift")
        req(old_state.get("canonical_sha256_without_this_field") == V41_STATE_CANON and
            canon(old_state) == V41_STATE_CANON, "V41 predecessor state canonical drift")
        req(blob(root / "stages/stage32/verify_main_startup.py") == V41_STARTUP_BLOB,
            "V41 startup projection drift")
        req(blob(root / "stages/stage32/verify_main_startup_authority_v41_hpadj20_full178_audit_synced.py")
            == V41_WRAPPER_BLOB, "V41 startup wrapper drift")

    req(candidate["schema"] ==
        "STAGE32_MAIN_GRF04_V42_HPADJ20_LOW_D_FULL_QA_HYBRID_CANDIDATE_V1",
        "candidate schema")
    req(candidate["status"] ==
        "RETAINED_MAIN_PARALLEL_CANDIDATE_HOSTILE_AUDIT_REQUIRED_NO_AUTHORITY_CHANGE",
        "candidate status")
    pred = candidate["predecessor_authority"]
    req(pred["v41_exact_head"] == V41_HEAD, "candidate V41 predecessor head")
    req(pred["authoritative_remaining_terminals"] == BASE_BOUND, "candidate predecessor bound")
    cb = candidate["candidate_bound"]
    req(cb["candidate_upper_bound"] == CANDIDATE_BOUND, "candidate upper bound")
    req(cb["tightening_vs_v41_authority"] == DELTA, "candidate tightening")
    req(cb["candidate_is_current_authority"] is False, "candidate self-promoted")
    req(cb["heavy_compute_required"] is False and
        cb["full178_full_qa_replay_required_for_this_candidate"] is False,
        "candidate unexpectedly requires full heavy replay")
    req(cb["composition_if_audited"] ==
        "DIRECT_SAME_PARTITION_CELLWISE_REFINEMENT__NO_ADDITIVE_SUBTRACTION",
        "candidate composition")

    handoff = v40["consumed_handoff"]
    req(handoff["candidate_upper_bound"] == BASE_BOUND, "V40 bound drift")
    req(handoff["heavy_run_id"] == 35077283028, "V40 heavy run drift")
    req(handoff["heavy_union_canonical_sha256"] ==
        "801999649a71700c369f0c2a32da9f7603b86e077212d3a4865ffbf1773822e7",
        "V40 union identity drift")
    req(handoff["producer_composition_rule"] ==
        "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        "V40 composition drift")
    req(v41["sync"]["authoritative_remaining_terminals"] == BASE_BOUND, "V41 bound drift")
    req(v41["hostile_audit"]["status"] == "PASS", "V41 predecessor audit not PASS")

    dom = preflight["structural_dominance"]
    req(dom["population_preserved_exactly"] is True and dom["same_pre_domain_terminal_mass"] is True,
        "full-qA preflight population identity drift")
    req(dom["same_post_mass_constraint"] is True, "full-qA preflight post-mass drift")
    req(dom["full_histogram_cell_objective_no_larger_than_hpadj20"] is True,
        "full-qA preflight dominance drift")
    req(preflight["next_exact_gate"]["consumption_rule_if_eventually_audited"] ==
        "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        "full-qA preflight composition drift")

    rows = pilot["rows"]
    expected_rows = [
        "g0-d008", "g1-d008", "g0-d010", "g1-d010",
        "g0-d012", "g1-d012", "g0-d014", "g1-d014",
    ]
    req([r["row_id"] for r in rows] == expected_rows, "pilot tested row set/order drift")
    hp20_sum = 0
    full_sum = 0
    strict = []
    for row in rows:
        req(row["hpadj20_replayed_integer_upper"] == row["hpadj20_cell_integer_upper"],
            f"pilot did not exactly replay HPADJ20 cell {row['row_id']}")
        delta = int(row["hpadj20_cell_integer_upper"]) - int(row["full_qa_cell_integer_upper"])
        req(delta == int(row["strict_improvement"]) and delta >= 0,
            f"pilot dominance drift {row['row_id']}")
        hp20_sum += int(row["hpadj20_cell_integer_upper"])
        full_sum += int(row["full_qa_cell_integer_upper"])
        if delta:
            strict.append(row)
    req(hp20_sum == TESTED_HP20 and full_sum == TESTED_FULL, "pilot tested-cell sums drift")
    req(hp20_sum - full_sum == DELTA, "pilot tightening arithmetic drift")
    req(len(strict) == 4 and sorted({int(r["d"]) for r in strict}) == [12, 14],
        "pilot strict cell boundary drift")
    req(pilot["scope"]["full178_replay_run"] is False, "pilot unexpectedly claims FULL178 replay")

    repl = candidate["cellwise_replacement"]
    req(repl["v40_nonzero_post_mass_cells"] == 800, "V40 cell partition count drift")
    req(repl["tested_low_d_cells"] == 8 and repl["strict_low_d_cells"] == 4,
        "candidate tested-cell count drift")
    req(repl["hpadj20_tested_cell_floor_sum"] == hp20_sum, "candidate HPADJ20 tested sum drift")
    req(repl["full_qa_tested_cell_floor_sum"] == full_sum, "candidate full-qA tested sum drift")
    req(repl["strict_tested_cell_tightening"] == DELTA, "candidate tested tightening drift")
    req(repl["unchanged_v40_cell_floor_contribution"] == BASE_BOUND - hp20_sum,
        "candidate unchanged contribution drift")
    req(UNCHANGED == BASE_BOUND - TESTED_HP20, "fixed unchanged arithmetic drift")
    req(CANDIDATE_BOUND == UNCHANGED + TESTED_FULL == BASE_BOUND - DELTA,
        "hybrid candidate arithmetic drift")
    req("NO_ADDITIVE_STACKING" in repl["composition"], "candidate additive-stacking firewall")

    gate = candidate["promotion_gate"]
    req(gate["hostile_audit_required"] is True, "candidate audit gate not armed")
    req(gate["main_authority_mutated"] is False and gate["main_credit_granted"] is False,
        "candidate promoted before hostile audit")
    req(gate["exact_incremental_rejected_identity_set_claimed"] is False and
        gate["additive_subtraction_authorized"] is False, "candidate identity/additive firewall")
    for key, value in candidate["firewalls"].items():
        req(value is False, f"candidate credit firewall opened: {key}")

    state = current_state()
    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V42_HPADJ20_LOW_D_FULL_QA_HYBRID_CANDIDATE_PENDING_AUDIT",
        "state schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "state strata")
    req(f["authoritative_remaining_terminals"] == BASE_BOUND, "state authority changed pre-audit")
    req(f["v42_hybrid_candidate_upper_bound_if_audited"] == CANDIDATE_BOUND,
        "state V42 candidate bound")
    req(f["v42_hybrid_candidate_tightening_if_audited"] == DELTA,
        "state V42 candidate tightening")
    req(f["v42_hybrid_candidate_is_current_authority"] is False,
        "state V42 candidate self-promoted")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "state closure firewall")

    cur = state["current"]
    req(cur["mainbatch_stop_gate"] == "HOSTILE_AUDIT_REQUIRED_FOR_V42_HYBRID_CANDIDATE",
        "state V42 audit stop gate")
    req(cur["next_exact_route"] ==
        "HOSTILE_AUDIT_V42_CANDIDATE_THEN_AUTHORITY_TRANSITION_OR_FULL178",
        "state next route")

    sweep = state["source_locks"]["live_specialist_sweep"]
    req(sweep["observed_repository_main"] == "c6284abbb29930255892d56f800da0ea1e34734b",
        "repository-main observation")
    req(sweep["lane_178_pr"] == 1815 and
        sweep["lane_178_head"] == "bec18f891f1012de21110e71998aa4874edc20b9" and
        sweep["lane_178_pending_main_handoff"] == "NONE", "178 live sweep")
    req(sweep["ex5_pr"] == 1818 and
        sweep["ex5_head"] == "669468c01bbb1f7c3b8bc46b934658765984f0b8" and
        sweep["ex5_pending_main_handoff"] == "NONE", "EX5 live sweep")
    req(sweep["cut_open_successor"] is False and sweep["cut_handoff"] == "NONE",
        "CUT live sweep")
    req(sweep["mb_pr"] == 1819 and
        sweep["mb_head"] == "89e86f93a9fe8b731e15bf5f7254eccc1caae374" and
        sweep["mb_pending_main_handoff"] == "NONE", "MB live sweep")
    req("ZERO_MAIN_CREDIT" in sweep["mb_handoff"], "MB credit firewall")

    for key in ("full178_complete", "effectivity_released", "receiver_credit", "route_credit",
                "theorem_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(state["firewalls"][key] is False, f"state firewall {key}")

    print("PASS: Stage32 V42 low-d full-qA hybrid candidate is a same-partition cellwise refinement")
    print(f"PASS: candidate upper bound {CANDIDATE_BOUND}; tightening {DELTA}; current authority remains {BASE_BOUND}")
    print("PASS: no full178 heavy replay, additive subtraction, identity-set claim, downstream credit, or merge authorization")

if __name__ == "__main__":
    main()
