#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
CERT_PATH = ROOT / "stages/stage36/36-01/source-authority-certificate.json"
BASE = "62c26297ebeb159e9cdd1e6b9c2129dff6a4acdc"

SOURCES = {
    "stage29_active_kernel_ledger": ("stages/stage29/29-16/active-kernel-ledger.json", "5d6d4c7709b57064aea5dc0ece672c5170c39550"),
    "stage29_endpoint_hub_graph": ("stages/stage29/29-06/endpoint-hub-graph.json", "7ea59474767f81fbaa4837c8cbc94b535560617b"),
    "stage29_campedelli_route_contract": ("stages/stage29/29-02hb/route-contract.json", "75045d8f15786836e8a7383fc07ef95161fa86e7"),
    "stage29_campedelli_arithmetic_routing": ("stages/stage29/29-02hb/arithmetic-routing.md", "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_source_lock": ("stages/stage29/29-02hb/source-lock.md", "713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d"),
}
ARSENAL = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S30-WF02": ("docs/arsenal/cards/workflows/S30-WF02.md", "38e4625155eb079bbe3d50d663c6256559319886"),
    "S30-WF03": ("docs/arsenal/cards/workflows/S30-WF03.md", "12740198aba19ade18302819f8e890dbda4eb701"),
}


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def lock_dict() -> dict:
    return {k: {"path": p, "blob_sha": s} for k, (p, s) in SOURCES.items()}


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    cert = json.loads(CERT_PATH.read_text())

    # S30-WF02: immutable mathematical inputs, independently replay cheap structure.
    expected = lock_dict()
    require(cert.get("immutable_stage29_sources") == expected, "certificate source-lock set moved")
    require(state.get("source_locks") == expected, "MAIN-STATE source-lock set moved")
    for key, (rel, sha) in SOURCES.items():
        require(blob_sha(ROOT / rel) == sha, f"source blob drift: {key}")

    aw = cert.get("arsenal_workflow_locks", {})
    for key, (rel, sha) in ARSENAL.items():
        require(aw.get(key, {}).get("path") == rel, f"Arsenal path moved: {key}")
        require(aw.get(key, {}).get("blob_sha") == sha, f"Arsenal lock moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"Arsenal blob drift: {key}")
    require("IMMUTABLE_LAYERED_CERTIFICATE_REPLAY" in (ROOT / ARSENAL["S30-WF02"][0]).read_text(), "S30-WF02 role moved")
    require("ADAPTER_CREDIT_LAYER_FIREWALL" in (ROOT / ARSENAL["S30-WF03"][0]).read_text(), "S30-WF03 role moved")

    ledger = json.loads((ROOT / SOURCES["stage29_active_kernel_ledger"][0]).read_text())
    rows = [r for r in ledger.get("class3_kernels", []) if r.get("kernel") == "K16-C3-CAMPEDELLI-UNIFORM-TORSOR"]
    require(len(rows) == 1, "Campedelli Class-3 kernel missing/duplicated")
    k = rows[0]
    require(k.get("execution_class") == 3, "execution class moved")
    require(k.get("children") == ["R29-CAMP2"], "receiver moved")
    require(k.get("parent_routes") == ["Q11-CAMPEDELLI"], "parent route moved")
    require(k.get("endpoint_decision_capable") is True, "endpoint capability moved")

    route = json.loads((ROOT / SOURCES["stage29_campedelli_route_contract"][0]).read_text())
    enum = route.get("exact_kernel_enumeration", {})
    require(enum.get("distinct_rank3_kernels") == 10, "ten-kernel count moved")
    require(enum.get("geometric_Qi_kernel_orbit_sizes") == [8, 2], "Q(i) split moved")
    require(enum.get("certified_Q_kernel_orbit_sizes") == [6, 2, 2], "Q split moved")
    require(enum.get("exact_Q_isomorphism_class_count_proved") is False, "Q-isomorphism firewall moved")
    require(route.get("open_receivers", {}).get("R29-CAMP2") == "ArithmeticHTorsorDescentForThreeCertifiedQSymmetryRepresentatives", "R29-CAMP2 identity moved")
    qf = route.get("q_form_firewall", {})
    require(qf.get("each_kernel_and_quotient_Q_defined") is True, "Q-defined quotient fact moved")
    require(qf.get("external_arithmetic_transfers_without_Q_form_adapter") is False, "Q-form firewall moved")
    require(route.get("rational_point_transfer") == "ONE_WAY_ENDPOINT_TO_QUOTIENT", "point-transfer direction moved")
    require(route.get("quotient_Q_point_nonexistence_would_kill_endpoint") is True, "quotient emptiness implication moved")
    require(route.get("quotient_Q_point_existence_implies_endpoint_Q_point") is False, "forbidden converse moved")

    hub = json.loads((ROOT / SOURCES["stage29_endpoint_hub_graph"][0]).read_text())
    nodes = {r["id"]: r for r in hub.get("nodes", [])}
    require(nodes.get("CAMPEDELLI_BAR_H", {}).get("base_field") == "Q", "canonical quotient Q-form moved")
    require(nodes.get("CAMPEDELLI_H", {}).get("base_field") == "Q", "resolved quotient Q-form moved")
    edges = {r["id"]: r for r in hub.get("edges", [])}
    e15 = edges.get("E15", {})
    require(e15.get("relation") == "FINITE_ETALE_QUOTIENT_BY_H", "E15 relation moved")
    require(e15.get("degree") == 8 and e15.get("field") == "Q", "E15 degree/field moved")
    require(e15.get("rational_point_pushforward") is True, "E15 pushforward moved")
    require(e15.get("rational_point_lift") == "requires H-torsor descent", "E15 lift firewall moved")
    e15r = edges.get("E15R", {})
    require(e15r.get("relation") == "FINITE_ETALE_RESOLVED_QUOTIENT", "E15R relation moved")
    require(e15r.get("degree") == 8 and e15r.get("field") == "Q", "E15R degree/field moved")
    require(e15r.get("rational_point_lift") == "requires H-torsor descent", "E15R lift firewall moved")

    arithmetic = (ROOT / SOURCES["stage29_campedelli_arithmetic_routing"][0]).read_text()
    for needle in [
        "U_endpoint(Q) -> C_H(Q)",
        "three certified Q-symmetry representatives",
        "H ~= (Z/2)^3",
        "H^1(Q,H)",
        "Without ramification conditions this set is infinite.",
        "rational quotient point need not lift rationally upstairs",
    ]:
        require(needle in arithmetic, f"arithmetic-routing anchor missing: {needle}")

    adapter = (ROOT / SOURCES["stage29_campedelli_quotient_adapter"][0]).read_text()
    for needle in [
        "Cbar_H := Sbar/H",
        "Sbar -> Cbar_H",
        "finite etale `H`-torsor",
        "S  --etale degree 8-->  C_H",
        "U_endpoint(Q) -> C_H(Q)",
        "C_H(Q)=empty  =>  U_endpoint(Q)=empty",
        "No converse is asserted.",
    ]:
        require(needle in adapter, f"quotient-adapter anchor missing: {needle}")

    src = (ROOT / SOURCES["stage29_campedelli_source_lock"][0]).read_text()
    for needle in [
        "SAME_GLOBAL_MAP_PROVED_IN_REPO=true",
        "SOURCE_GEOMETRY_TO_Q_ARITHMETIC_AUTOMATIC=false",
        "Q_FORM_ADAPTER_REQUIRED_FOR_EXTERNAL_ARITHMETIC=true",
    ]:
        require(needle in src, f"source-lock firewall missing: {needle}")

    require(cert.get("schema") == "STAGE36_36_01_SOURCE_AUTHORITY_LOCK_V1", "certificate schema moved")
    require(cert.get("base_main_sha") == BASE, "certificate base moved")
    ids = cert.get("locked_identities", {})
    require(ids.get("ROOT_KERNEL") == "K16-C3-CAMPEDELLI-UNIFORM-TORSOR", "root identity moved")
    require(ids.get("SOURCE_RECEIVER") == "R29-CAMP2", "receiver identity moved")
    require(ids.get("PARENT_ROUTE") == "Q11-CAMPEDELLI", "parent identity moved")
    require(cert.get("locked_frontier") == {
        "TEN_Q_DEFINED_KERNELS": True,
        "DISTINCT_RANK3_KERNEL_COUNT": 10,
        "CANONICAL_QUOTIENT_DEGREE": 8,
        "RESOLVED_ETALE_QUOTIENT_DEGREE": 8,
        "H_GROUP": "(Z/2)^3",
        "CERTIFIED_Q_SYMMETRY_SPLIT": [6, 2, 2],
        "GEOMETRIC_QI_SPLIT": [8, 2],
        "EXECUTION_REPRESENTATIVES": 3,
        "EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED": False,
        "ENDPOINT_Q_POINT_PUSHES_TO_EVERY_AUDITED_C_H": True,
        "QUOTIENT_Q_POINT_IMPLIES_ENDPOINT_Q_POINT": False,
        "UNRESTRICTED_H1_Q_H_FINITE": False,
    }, "certificate frontier moved")
    require(cert.get("pass_condition") == {"STAGE36_SOURCE_FRONTIER_LOCKED": True, "NEW_THEOREM_CREDIT": False}, "pass condition moved")
    require(cert.get("promotion", {}).get("hostile_audit_required") is True, "hostile-audit gate missing")
    require(cert.get("promotion", {}).get("promoted_to_audited_authority") is False, "premature promotion")
    require(cert.get("promotion", {}).get("next_leaf_before_audit_allowed") is False, "premature 36-02")
    require(all(v is False for v in cert.get("claims", {}).values()), "certificate leaked higher credit")

    require(state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V2_36_01_PENDING_AUDIT", "state schema moved")
    require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT", "state audit status moved")
    require(state.get("base_main_sha") == BASE, "state base moved")
    unit = state.get("completed_units", {}).get("36-01", {})
    require(unit.get("status") == "EXACT_SOURCE_FRONTIER_LOCK_PENDING_HOSTILE_AUDIT", "36-01 status moved")
    require(unit.get("STAGE36_SOURCE_FRONTIER_LOCKED") is True, "36-01 result missing")
    require(unit.get("NEW_THEOREM_CREDIT") is False, "36-01 theorem credit leaked")
    require(unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-01 promotion status moved")
    current = state.get("current", {})
    require(current.get("unit") == "36-01", "current unit advanced")
    require(current.get("next_exact_leaf") == "36-01_SOURCE_AUTHORITY_LOCK", "next leaf advanced before audit")
    require(current.get("provisional_successor_after_hostile_audit") == "36-02_THREE_Q_REPRESENTATIVE_INVENTORY", "successor moved")
    require(all(v is False for v in state.get("promotion_gates", {}).values()), "promotion gate flipped before audit")
    require(all(v is False for v in state.get("claims", {}).values()), "state leaked higher credit")
    sib = state.get("sibling_interfaces", {}).get("K16-C2-BRAUER-EXPLICIT-CHAIN", {})
    require(sib.get("receiver") == "R29-CAMP4", "CAMP4 sibling moved")
    require(sib.get("relationship") == "SIBLING_ASSET_PROVIDER_ONLY", "CAMP4 relation moved")
    require(sib.get("automatic_authority_merge") is False, "CAMP4 auto-merge enabled")
    require(sib.get("automatic_R29_CAMP2_closure") is False, "CAMP4 auto-close enabled")

    print("PASS STAGE36_36_01_SOURCE_AUTHORITY_LOCK_V1")
    print("immutable_stage29_sources=6; arsenal=S30-WF02,S30-WF03")
    print("frontier=10 kernels; Q symmetry 6+2+2; H=(Z/2)^3; degree=8; endpoint->quotient only")
    print("36-01 provisional exact result; hostile audit required; 36-02 not started")


if __name__ == "__main__":
    main()
