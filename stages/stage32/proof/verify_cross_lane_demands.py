#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCH = HERE / "historical-routing-blobs"
ARCH_VERIFIER = ARCH / "VERIFY-CROSS-LANE-DEMANDS-V24-PRE-EX5-STARTUP-COLLAPSE.py"
ARCH_REGISTRY = ARCH / "CROSS-LANE-DEMANDS-V24-PRE-N398-HANDOFF.json"
ARCH_MAIN_STATE = ARCH / "b8df16056625db5fbb1947f1e927593de258f1ff.json"
TMP_VERIFIER = HERE / ".verify_cross_lane_demands_v24_pre_ex5_startup_collapse.py"
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
MONITOR = HERE / "ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
SYNTHESIS = HERE / "PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json"
EX5_STATE = ROOT / "stages/stage32-ex5/CROSS-LANE-STATE.json"
ARCH_EX5_STATE = ROOT / "stages/stage32-ex5/archive/startup-surface-20260914/CROSS-LANE-STATE.json"
CUT201_DISP = ROOT / "stages/stage32/management/cut201-main-disposition/CUT201-G11-V26-MAIN-DISPOSITION.json"
CUT201_DISP_VERIFIER = ROOT / "stages/stage32/management/cut201-main-disposition/verify_cut201_g11_v26_main_disposition.py"

ARCH_VERIFIER_BLOB = "add0e8d511295c6aeca1364f3901cda930407307"
ARCH_REGISTRY_BLOB = "e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd"
ARCH_MAIN_STATE_BLOB = "b8df16056625db5fbb19456a6854a39cb3aec87a"
ARCH_EX5_STATE_BLOB = "99151c6b5402e2ed12dfe268bd497935d5be1b3c"
CURRENT_REGISTRY_CANON = "9ace76a55e717dec9f39151e694e78a00250fa08a0a804373faded45196ab7e4"
SYNTHESIS_CANON = "20defc105e39fedaaf5243de55bf0c496ffa997566fec582595847da5a02c2ca"
CUT201_DISP_BLOB = "50707eaee4df3a71927967b7ba325939c3030c2f"
CUT201_DISP_VERIFIER_BLOB = "185f2a33a561dd7bd5d2261d7be7d45a279bc2d1"
CUT201_DISP_CANON = "946ec777f824eaae75aa14d9c3ab5f348bfea38da020e72ede9750c914f86381"
N398_DEMAND = "S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"
N400_DEMAND = "S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"
CUT201_DEMAND = "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"
ACTIVE_SPECIALISTS = {"32-01-178", "EX5", "CUT", "MB"}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_json(path: Path) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def demand_by_id(registry: dict, demand_id: str) -> dict:
    hits = [d for d in registry.get("demands", []) if d.get("demand_id") == demand_id]
    req(len(hits) == 1, f"demand identity drift {demand_id}")
    return hits[0]


def verify_current_wiring() -> None:
    registry = load_json(REGISTRY)
    req(registry.get("schema") == "STAGE32_CROSS_LANE_DEMANDS_V4_CUT201_V26_ADAPTER_OPEN", "current registry schema drift")
    req(registry.get("canonical_sha256_without_this_field") == CURRENT_REGISTRY_CANON, "current registry stored canonical drift")
    req(canon(registry) == CURRENT_REGISTRY_CANON, "current registry canonical drift")
    req(registry.get("credit_firewall", {}).get("demand_satisfied_is_mathematical_credit") is False, "demand status promoted to credit")
    req(registry.get("credit_firewall", {}).get("merge_authorized") is False, "merge firewall opened")

    req(demand_by_id(registry, "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1").get("status") == "SATISFIED", "CUT192 demand drift")
    req(demand_by_id(registry, "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1").get("status") == "SATISFIED", "HPADJ demand drift")
    n398 = demand_by_id(registry, N398_DEMAND)
    req(n398.get("status") == "OBSOLETE", "N398 demand must be superseded")
    req(n398.get("satisfying_artifact") is None, "obsolete N398 demand should not fabricate direct artifact")
    n400 = demand_by_id(registry, N400_DEMAND)
    req(n400.get("status") == "SATISFIED", "N400 demand not satisfied")
    sat = n400.get("satisfying_artifact", {})
    req(sat.get("producer_pr") == 1797, "N400 producer PR")
    req(sat.get("audited_exact_head") == "b1a950cbc6edf3cb85e1ea79473105c6f1f67b03", "N400 audited head")
    req(sat.get("audit_review_id") == 5203374607 and sat.get("audit_status") == "PASS", "N400 audit receipt")
    req(sat.get("result_blob_sha1") == "485c9a0380788bedd25cde5a47204e2c8c62472e", "N400 result blob")
    req(sat.get("verifier_blob_sha1") == "6898ea22458d2156944569dc598eb5b7ebb0048e", "N400 verifier blob")
    sp = n400.get("source_population_semantics", {})
    req(sp.get("terminal_identity_count") == 10961 and sp.get("rejected_terminal_count") == 5502, "N400 population/count")
    req(sp.get("prior_consumed_v24_overlap_terminal_count") == 0 and sp.get("double_charge") is False, "N400 double charge")
    req(sp.get("producer_lane_main_authority_subtraction_performed") is False, "178 producer subtraction")

    consumed = [x for x in registry.get("audited_result_consumption", []) if x.get("result_id") == "S32.N400.N396_REJECTED_5502.COMPACT_MAIN_CONSUMPTION.V1"]
    req(len(consumed) == 1, "N400 consumption ledger must be exactly once")
    req(consumed[0].get("credited_incremental_rejected_terminals") == 5502, "N400 consumed credit")
    req(consumed[0].get("double_charge") is False and consumed[0].get("prior_consumed_overlap_terminals") == 0, "N400 ledger overlap")
    req(consumed[0].get("producer_lane_subtraction_performed") is False, "N400 producer subtraction ledger")

    c201 = demand_by_id(registry, CUT201_DEMAND)
    req(c201.get("status") == "OPEN", "CUT201 V26 adapter demand must remain OPEN")
    req(c201.get("priority") == "P0_BLOCKING_DOWNSTREAM", "CUT201 demand priority")
    req(c201.get("producer_lane") == "CUT" and c201.get("consumer_lane") == "MAIN", "CUT201 demand routing")
    req(c201.get("satisfying_artifact") is None, "CUT201 demand prematurely satisfied")
    csp = c201.get("source_population_semantics", {})
    req(csp.get("producer_pr") == 1806, "CUT201 producer PR")
    req(csp.get("audited_exact_head") == "8eed1449b325c3b990f90b61471bf7ecec0d89bc", "CUT201 audited head")
    req(csp.get("hostile_audit_review_id") == 5204865930 and csp.get("audit_status") == "PASS", "CUT201 audit receipt")
    req(csp.get("cut201_result_blob_sha1") == "ebdf1f741365f7403050f22b478eeea5a7a1d653", "CUT201 result blob")
    req(csp.get("cut201_result_canonical_sha256") == "8f9ccc51046b9559d15ee5d64ef72be35f798a740a78a85df92d865286dbd467", "CUT201 result canonical")
    req(csp.get("cut201_verifier_blob_sha1") == "1aad3b1ffb54b1d3be8e4095091904826fbdfa43", "CUT201 verifier blob")
    req(csp.get("candidate_closed_block_count") == 226 and csp.get("candidate_pruned_terminal_count") == 25538, "CUT201 candidate counts")
    req(csp.get("source_main_authority_version") == "V12", "CUT201 source authority")
    req(csp.get("current_main_projection_schema") == "STAGE32_MAIN_COMPACT_STATE_V26_N400_AUDIT_SYNCED", "CUT201 current authority target")
    req(csp.get("current_v26_subset_identity_proved") is False and csp.get("current_v26_overlap_accounting_proved") is False, "CUT201 current-authority adapter prematurely promoted")
    req(csp.get("credited_incremental_rejected_terminals") == 0, "CUT201 premature MAIN credit")
    req(csp.get("main_disposition_canonical_sha256") == CUT201_DISP_CANON, "CUT201 disposition canonical link")

    req(CUT201_DISP.is_file() and blob(CUT201_DISP) == CUT201_DISP_BLOB, "CUT201 MAIN disposition blob drift")
    req(CUT201_DISP_VERIFIER.is_file() and blob(CUT201_DISP_VERIFIER) == CUT201_DISP_VERIFIER_BLOB, "CUT201 MAIN disposition verifier drift")
    disp = load_json(CUT201_DISP)
    req(disp.get("canonical_sha256_without_this_field") == CUT201_DISP_CANON and canon(disp) == CUT201_DISP_CANON, "CUT201 disposition canonical")
    runpy.run_path(str(CUT201_DISP_VERIFIER), run_name="__main__")

    open_demands = [d.get("demand_id") for d in registry.get("demands", []) if d.get("status") == "OPEN"]
    req(open_demands == [CUT201_DEMAND], "unexpected OPEN demand set")

    monitor = load_json(MONITOR)
    req(monitor.get("schema") == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V3_CUT201_V26_ADAPTER_PENDING", "monitor schema")
    req(monitor.get("startup_rule", {}).get("refresh_live_on_every_stage32mainbatch") is True, "monitor refresh")
    lanes = monitor.get("active_specialists", [])
    req({x.get("lane") for x in lanes} == ACTIVE_SPECIALISTS, "monitor coverage")
    by_lane = {x["lane"]: x for x in lanes}
    req(by_lane["32-01-178"].get("expected_open_pr") == 1797, "178 monitor PR")
    req(by_lane["32-01-178"].get("pending_main_handoff_ids") == [], "178 pending handoff not cleared")
    req(by_lane["EX5"].get("expected_open_pr") == 1776 and by_lane["EX5"].get("pending_main_handoff_ids") == [], "EX5 monitor state")
    req(by_lane["CUT"].get("expected_open_pr") == 1806, "CUT monitor PR")
    req(by_lane["CUT"].get("pending_main_handoff_ids") == [CUT201_DEMAND], "CUT201 pending handoff missing")
    req(by_lane["MB"].get("expected_open_pr") == 1791 and by_lane["MB"].get("pending_main_handoff_ids") == [], "MB monitor state")
    fw = monitor.get("credit_firewall", {})
    req(all(fw.get(k) is False for k in ("monitor_observation_is_mathematical_credit", "audit_pending_candidate_is_main_credit", "demand_status_is_main_credit", "duplicate_pruning_credit_authorized", "merge_authorized")), "monitor firewall")

    synthesis = load_json(SYNTHESIS)
    req(synthesis.get("schema") == "STAGE32_PICARD64_PARITY_CROSS_LANE_SYNTHESIS_V2_SUPERSEDED_BY_N400", "synthesis schema")
    req(synthesis.get("canonical_sha256_without_this_field") == SYNTHESIS_CANON and canon(synthesis) == SYNTHESIS_CANON, "synthesis canonical")
    req(synthesis.get("status") == "SUPERSEDED_BY_AUDITED_N400_MAIN_CONSUMPTION", "synthesis status")
    req(all(x.get("status") == "NOT_PROVED" for x in synthesis.get("required_comparisons", [])), "unresolved synthesis promoted")
    req(synthesis.get("sources", {}).get("n400_178", {}).get("hostile_audit_review_id") == 5203374607, "N400 synthesis audit")
    sfw = synthesis.get("credit_firewall", {})
    req(all(sfw.get(k) is False for k in ("n398_main_pruning_credit", "grf09_main_pruning_credit", "ex5_main_credit", "population_equivalence_proved", "coordinate_equivalence_proved", "shared_parity_theorem_proved", "full178_complete", "effectivity_credit", "theorem_credit", "endpoint_credit", "stage32_closed", "merge_authorized")), "synthesis firewall")


def replay_historical_v24_boundary() -> None:
    req(not EX5_STATE.exists(), "retired EX5 CROSS-LANE-STATE leaked into live root")
    req(ARCH_VERIFIER.is_file() and blob(ARCH_VERIFIER) == ARCH_VERIFIER_BLOB, "archived verifier drift")
    req(ARCH_REGISTRY.is_file() and blob(ARCH_REGISTRY) == ARCH_REGISTRY_BLOB, "archived registry drift")
    req(ARCH_MAIN_STATE.is_file() and blob(ARCH_MAIN_STATE) == ARCH_MAIN_STATE_BLOB, "archived V24 MAIN-STATE drift")
    req(ARCH_EX5_STATE.is_file() and blob(ARCH_EX5_STATE) == ARCH_EX5_STATE_BLOB, "archived EX5 state drift")
    current_registry = REGISTRY.read_bytes()
    current_main_state = MAIN_STATE.read_bytes()
    old_state = EX5_STATE.read_bytes() if EX5_STATE.exists() else None
    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    try:
        REGISTRY.write_bytes(ARCH_REGISTRY.read_bytes())
        MAIN_STATE.write_bytes(ARCH_MAIN_STATE.read_bytes())
        EX5_STATE.write_bytes(ARCH_EX5_STATE.read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        REGISTRY.write_bytes(current_registry)
        MAIN_STATE.write_bytes(current_main_state)
        if old_state is None:
            if EX5_STATE.exists():
                EX5_STATE.unlink()
        else:
            EX5_STATE.write_bytes(old_state)
        if old_tmp is None:
            if TMP_VERIFIER.exists():
                TMP_VERIFIER.unlink()
        else:
            TMP_VERIFIER.write_bytes(old_tmp)
    req(REGISTRY.read_bytes() == current_registry, "registry restore failed")
    req(MAIN_STATE.read_bytes() == current_main_state, "MAIN-STATE restore failed")


def main() -> None:
    verify_current_wiring()
    replay_historical_v24_boundary()
    verify_current_wiring()
    print("PASS: live Stage32 specialist monitor and N400 MAIN-consumption coordination verified")
    print("PASS: CUT201 G11 is dispositioned at zero current-V26 MAIN credit with one P0 adapter demand OPEN")
    print("PASS: historical V24 cross-lane authority replay preserved")


if __name__ == "__main__":
    main()
