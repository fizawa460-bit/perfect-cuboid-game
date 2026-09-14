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
TMP_VERIFIER = HERE / ".verify_cross_lane_demands_v24_pre_ex5_startup_collapse.py"
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
SYNTHESIS = HERE / "PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json"
EX5_STATE = ROOT / "stages/stage32-ex5/CROSS-LANE-STATE.json"
ARCH_EX5_STATE = ROOT / "stages/stage32-ex5/archive/startup-surface-20260914/CROSS-LANE-STATE.json"

ARCH_VERIFIER_BLOB = "add0e8d511295c6aeca1364f3901cda930407307"
ARCH_REGISTRY_BLOB = "e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd"
ARCH_EX5_STATE_BLOB = "99151c6b5402e2ed12dfe268bd497935d5be1b3c"
CURRENT_REGISTRY_CANON = "0ba500be9566fbda6e24c87a5ed8f83f481498b67d99f4498e9e9fc8cfc4d777"
SYNTHESIS_CANON = "02e654b76702ddc33595b6c41995af26de7ad4981296f4dbf4b2353659dc6925"
N398_DEMAND = "S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"
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
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_json(path: Path) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def demand_by_id(registry: dict, demand_id: str) -> dict:
    hits = [d for d in registry.get("demands", []) if d.get("demand_id") == demand_id]
    req(len(hits) == 1, f"demand identity drift {demand_id}")
    return hits[0]


def verify_current_wiring() -> None:
    registry = load_json(REGISTRY)
    req(registry.get("schema") == "STAGE32_CROSS_LANE_DEMANDS_V2_ACTIVE_SPECIALIST_HANDOFF",
        "current registry schema drift")
    req(registry.get("canonical_sha256_without_this_field") == CURRENT_REGISTRY_CANON,
        "current registry stored canonical drift")
    req(canon(registry) == CURRENT_REGISTRY_CANON, "current registry canonical drift")
    req(registry.get("credit_firewall", {}).get("demand_satisfied_is_mathematical_credit") is False,
        "demand status promoted to mathematical credit")
    req(registry.get("credit_firewall", {}).get("merge_authorized") is False,
        "cross-lane registry merge firewall opened")

    old_cut = demand_by_id(registry, "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1")
    old_hpadj = demand_by_id(registry, "S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1")
    req(old_cut.get("status") == "SATISFIED", "CUT192/EX5 historical demand drift")
    req(old_hpadj.get("status") == "SATISFIED", "HPADJ/EX5 historical demand drift")

    n398 = demand_by_id(registry, N398_DEMAND)
    req(n398.get("status") == "OPEN", "N398 handoff must remain OPEN before hostile audit PASS")
    req(n398.get("priority") == "P0_BLOCKING_DOWNSTREAM", "N398 handoff priority drift")
    req(n398.get("producer_lane") == "32-01-178" and n398.get("consumer_lane") == "MAIN",
        "N398 handoff producer/consumer drift")
    req(n398.get("satisfying_artifact") is None, "N398 handoff falsely satisfied")
    ar = n398.get("audit_requirement", {})
    req(ar.get("hostile_audit_required_before_demand_satisfaction") is True,
        "N398 handoff audit-before-satisfaction firewall missing")
    req(ar.get("producer_may_not_self_grant_audit_credit") is True,
        "N398 producer self-audit firewall missing")
    sp = n398.get("source_population_semantics", {})
    req(sp.get("producer_pr") == 1797, "N398 producer PR drift")
    req(sp.get("candidate_branch_head") == "71f078a7521b265e300a450ab129370f077ef6a1",
        "N398 frozen candidate head drift")
    req(sp.get("candidate_state_canonical_sha256") ==
        "f1146a2fda26d4d747e710b90ab829dd27b09118471a4d385046a1cb1215fcd1",
        "N398 state identity drift")
    req(sp.get("candidate_result_canonical_sha256") ==
        "611632cedd9ff3515bb374a608020dd06079240db5224bb15f90845c7b90cad7",
        "N398 result identity drift")
    req(sp.get("retained_block_count") == 97 and sp.get("terminal_identity_count") == 10961,
        "N398 retained population drift")
    req(sp.get("current_main_residual_subset_identity_proved") is False,
        "N398 current-MAIN residual identity overclaim")

    monitor = load_json(MONITOR)
    req(monitor.get("schema") == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V1",
        "active-specialist monitor schema drift")
    req(monitor.get("startup_rule", {}).get("refresh_live_on_every_stage32mainbatch") is True,
        "live specialist refresh not mandatory")
    lanes = monitor.get("active_specialists", [])
    lane_ids = {x.get("lane") for x in lanes}
    req(lane_ids == ACTIVE_SPECIALISTS,
        f"active specialist monitor coverage drift: {sorted(lane_ids)}")
    required_fields = set(monitor.get("startup_rule", {}).get("required_observation_fields", []))
    req(required_fields == {
        "live_pr_or_active_surface",
        "live_head",
        "current_state_or_retained_boundary",
        "latest_retained_result",
        "audit_gate",
        "pending_handoff_or_none",
        "main_freshness",
        "semantic_leaf",
    }, "active specialist observation field drift")
    by_lane = {x["lane"]: x for x in lanes}
    req(by_lane["32-01-178"].get("expected_open_pr") == 1797, "178 monitor PR drift")
    req(N398_DEMAND in by_lane["32-01-178"].get("pending_main_handoff_ids", []),
        "N398 handoff missing from 178 monitor")
    req(by_lane["EX5"].get("expected_open_pr") == 1776, "EX5 monitor PR drift")
    req(by_lane["CUT"].get("expected_open_pr") == 1806, "CUT monitor PR drift")
    req(by_lane["MB"].get("expected_open_pr") == 1791, "MB monitor PR drift")
    fw = monitor.get("credit_firewall", {})
    req(all(fw.get(k) is False for k in (
        "monitor_observation_is_mathematical_credit",
        "audit_pending_candidate_is_main_credit",
        "demand_status_is_main_credit",
        "duplicate_pruning_credit_authorized",
        "merge_authorized",
    )), "active specialist monitor credit firewall opened")

    synthesis = load_json(SYNTHESIS)
    req(synthesis.get("schema") == "STAGE32_PICARD64_PARITY_CROSS_LANE_SYNTHESIS_V1",
        "parity synthesis schema drift")
    req(synthesis.get("canonical_sha256_without_this_field") == SYNTHESIS_CANON,
        "parity synthesis stored canonical drift")
    req(canon(synthesis) == SYNTHESIS_CANON, "parity synthesis canonical drift")
    req(synthesis.get("status") == "OPEN_SYNTHESIS_NO_CREDIT", "parity synthesis status drift")
    sources = synthesis.get("sources", {})
    req(set(sources) == {"n398_178", "grf09_main", "ex5_picard64"},
        "parity synthesis source set drift")
    req(sources["n398_178"].get("producer_pr") == 1797 and
        sources["n398_178"].get("audit_status") == "PENDING",
        "N398 synthesis source drift")
    req(sources["grf09_main"].get("producer_pr") == 1808 and
        sources["grf09_main"].get("current_main_residual_subset_identity_proved") is False,
        "GRF-09 synthesis source drift")
    req(sources["ex5_picard64"].get("producer_pr") == 1776 and
        sources["ex5_picard64"].get("hostile_audit_review_id") == 5193423203,
        "EX5 synthesis source drift")
    comparisons = synthesis.get("required_comparisons", [])
    req({x.get("id") for x in comparisons} == {
        "POPULATION_IDENTITY",
        "COORDINATE_LABEL_ADAPTER",
        "AFFINE_RELATION_SPACE",
        "EX5_STRUCTURAL_ORIGIN",
    }, "parity synthesis comparison set drift")
    req(all(x.get("status") == "NOT_PROVED" for x in comparisons),
        "parity synthesis silently promoted an unresolved comparison")
    sfw = synthesis.get("credit_firewall", {})
    req(all(sfw.get(k) is False for k in (
        "n398_main_pruning_credit",
        "grf09_main_pruning_credit",
        "ex5_main_credit",
        "population_equivalence_proved",
        "coordinate_equivalence_proved",
        "shared_parity_theorem_proved",
        "full178_complete",
        "effectivity_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "merge_authorized",
    )), "parity synthesis credit firewall opened")


def replay_historical_v24_boundary() -> None:
    req(not EX5_STATE.exists(), "retired EX5 CROSS-LANE-STATE leaked into live root")
    req(ARCH_VERIFIER.is_file() and blob(ARCH_VERIFIER) == ARCH_VERIFIER_BLOB,
        "archived V24 cross-lane verifier drift")
    req(ARCH_REGISTRY.is_file() and blob(ARCH_REGISTRY) == ARCH_REGISTRY_BLOB,
        "archived pre-N398 cross-lane registry drift")
    req(ARCH_EX5_STATE.is_file() and blob(ARCH_EX5_STATE) == ARCH_EX5_STATE_BLOB,
        "archived EX5 coordination snapshot drift")

    current_registry = REGISTRY.read_bytes()
    old_state = EX5_STATE.read_bytes() if EX5_STATE.exists() else None
    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    try:
        REGISTRY.write_bytes(ARCH_REGISTRY.read_bytes())
        EX5_STATE.write_bytes(ARCH_EX5_STATE.read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        REGISTRY.write_bytes(current_registry)
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

    req(REGISTRY.read_bytes() == current_registry, "current cross-lane registry restore failed")
    req(not EX5_STATE.exists() if old_state is None else EX5_STATE.read_bytes() == old_state,
        "EX5 coordination snapshot leaked after historical replay")


def main() -> None:
    verify_current_wiring()
    replay_historical_v24_boundary()
    verify_current_wiring()
    print("PASS: live Stage32 specialist monitor and N398 parity handoff wiring verified")
    print("PASS: N398/GRF-09/EX5 Picard64 synthesis remains explicit NO-CREDIT pending adapters/audit")
    print("PASS: historical V24 cross-lane authority replay preserved")


if __name__ == "__main__":
    main()
