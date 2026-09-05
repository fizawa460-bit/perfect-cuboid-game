#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage36/MAIN-STATE.json"
CERT = ROOT / "stages/stage36/36-09/replacement-breadth-gate.json"
CERT_BLOB = "0c6019d70346b531a9b703d6f74e346302273655"
BASE = "dc5898281a7ccea25d8ee0c1ae9953a18941ec08"
PROMO_36_05_MERGE = "99c5f1634dd59d4bc5698cbb775801dd9d000827"
SCHEMA = "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V12_36_09_BREADTH_GATE_PENDING_AUDIT"
FRESHNESS = {"sync_pr":1574,"main_sha":BASE,"merge_commit":"4e0010b26f6b0a59e50234d6f1b35b7a78360fff","scope":"Stage32-only advance via #1570; no Stage36, Stage29 Campedelli/Brauer source, Research OS policy, or Arsenal authority changes"}

SOURCES = {
    "stage36_roadmap": ("stages/stage36/ROADMAP.md", "eeedda0e89e24f851c989b5ec83e7b320e1ad99e"),
    "stage36_36_03_physical_receiver": ("stages/stage36/36-03/physical-open-boundary.json", "fc1947b2de08f7d8a104bdc91902b20e88635349"),
    "stage36_36_05_block": ("stages/stage36/36-05/uniform-ramification-support.json", "193d0165b242d799bc981774783a5160c1ac58dc"),
    "stage29_active_kernel_ledger": ("stages/stage29/29-16/active-kernel-ledger.json", "5d6d4c7709b57064aea5dc0ece672c5170c39550"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_brauer_audit": ("stages/stage29/29-02f/audit.md", "b72f61749bcf0c2535135da11f882560c3a01cce"),
    "stage29_open_algebraic_brauer_adapter": ("stages/stage29/29-02f/open-algebraic-brauer-adapter.md", "2eccbf9bc6848262df7566a7f7eb436dd5b62681"),
    "asset_discovery_policy": ("docs/research-os/policies/repository-asset-discovery.md", "bf001d4ff4375281a901d52c147c35c28643b8a3"),
    "cycle_safety_protocol": ("docs/research-os/policies/cycle-exploration-safety-protocol.md", "4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"),
}
ARSENAL = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S34-WF01": ("docs/arsenal/cards/workflows/S34-WF01.md", "1ebba4ec402e14d536284a06c5ac32625c6b8cec"),
    "S34-W01": ("docs/arsenal/cards/formal/S34-W01.md", "01a8e90e34b4aa46edbfa825803d488e5230e9d0"),
    "S34-W02": ("docs/arsenal/cards/formal/S34-W02.md", "13d41be776fcd2edcd258f11bd28c5a6596de45b"),
    "S34-W03": ("docs/arsenal/cards/formal/S34-W03.md", "1d5275321f42768a6414d4610ac912c63be43f96"),
    "S33-PW07": ("docs/arsenal/cards/provisional/S33-PW07.md", "7f1337858bc6f9006e101d810dd72e67aef534fd"),
    "S33-PW08": ("docs/arsenal/cards/provisional/S33-PW08.md", "c9e13a917811581578f833ea93619d85f717be6d"),
}
EXPECTED_IDS = [
    "B1_DIRECT_UNIFORM_H1_SELMER",
    "B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION",
    "B3_FINITE_CURVE_OR_COVER_DECOMPOSITION",
    "B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION",
    "B5_CAMPEDELLI_BRAUER_ETALE_BRAUER",
    "B6_FIBRATION_TO_CURVE_BASE",
    "B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER",
    "B8_GEOMETRIC_TOPOLOGICAL_CLASSIFICATION",
    "B9_ASYMPTOTIC_OR_SIEVE_SPARSITY",
    "B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER",
]
EXPECTED_STATUS = {
    "B1_DIRECT_UNIFORM_H1_SELMER": "BLOCKED",
    "B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION": "UNTESTED",
    "B3_FINITE_CURVE_OR_COVER_DECOMPOSITION": "UNTESTED",
    "B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION": "UNTESTED",
    "B5_CAMPEDELLI_BRAUER_ETALE_BRAUER": "LIVE",
    "B6_FIBRATION_TO_CURVE_BASE": "UNTESTED",
    "B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER": "UNTESTED",
    "B8_GEOMETRIC_TOPOLOGICAL_CLASSIFICATION": "BLOCKED",
    "B9_ASYMPTOTIC_OR_SIEVE_SPARSITY": "DOMINATED",
    "B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER": "UNTESTED",
}

def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
def req(ok: bool, msg: str) -> None:
    if not ok: raise SystemExit(msg)

def main() -> None:
    req(blob_sha(CERT) == CERT_BLOB, "36-09 certificate blob drift")
    cert = json.loads(CERT.read_text())
    req(cert.get("schema") == "STAGE36_36_09_RECEIVER_MATCHED_REPLACEMENT_BREADTH_GATE_V1", "36-09 schema moved")
    req(cert.get("status") == "BREADTH_GATE_PENDING_HOSTILE_AUDIT", "36-09 status moved")
    req(cert.get("base_main_sha") == BASE, "36-09 base moved")
    req(cert.get("freshness_sync") == FRESHNESS, "36-09 freshness provenance moved")

    for key, (rel, sha) in SOURCES.items():
        req(cert.get("source_locks", {}).get(key) == {"path": rel, "blob_sha": sha}, f"source declaration moved: {key}")
        req(blob_sha(ROOT / rel) == sha, f"source blob drift: {key}")
    for key, (rel, sha) in ARSENAL.items():
        row = cert.get("arsenal_locks", {}).get(key, {})
        req(row.get("path") == rel and row.get("blob_sha") == sha, f"Arsenal declaration moved: {key}")
        req(blob_sha(ROOT / rel) == sha, f"Arsenal blob drift: {key}")

    road = (ROOT / SOURCES["stage36_roadmap"][0]).read_text()
    req("36-09 — RECEIVER-MATCHED REPLACEMENT / BREADTH GATE" in road, "36-09 roadmap heading missing")
    req("EXHAUSTIVE_VIEW_AUDIT" in road and "BLIND_REDISCOVERY" in road, "36-09 roadmap breadth requirements missing")
    cycle = (ROOT / SOURCES["cycle_safety_protocol"][0]).read_text()
    req("the active route would otherwise be parked at an external theorem gate" in cycle, "cycle trigger anchor missing")
    req("Every `EXHAUSTIVE_VIEW_AUDIT` must contain a blind pass" in cycle, "blind-pass policy anchor missing")
    discovery = (ROOT / SOURCES["asset_discovery_policy"][0]).read_text()
    req("Read `docs/arsenal/index.json` as the machine-readable registry" in discovery, "Arsenal discovery route moved")

    phys = json.loads((ROOT / SOURCES["stage36_36_03_physical_receiver"][0]).read_text())
    rr = phys.get("restricted_receiver_preparation", {})
    req(rr.get("exact_restricted_open") == "U_H=q_H(U) for each audited representative", "restricted receiver moved")
    req(rr.get("target_point_image") == "q_H(U(Q)) subset U_H(Q)", "endpoint image inclusion moved")
    req(phys.get("scheme_vs_rational_firewall", {}).get("U_H_Q_equals_q_H_of_U_Q_claimed") is False, "quotient lift equality overclaimed")

    receiver = cert.get("exact_surviving_receiver", {})
    req(receiver.get("representatives") == ["Q6_GEOM8", "Q2_GEOM8", "Q2_GEOM2"], "representative receiver set moved")
    req(receiver.get("restricted_quotient_open") == "U_H := q_H(U) subset C_H", "receiver open moved")
    req(receiver.get("full_C_H_Q_emptiness_required") is False, "receiver target unnecessarily widened")
    req(receiver.get("quotient_point_lifts_automatically") is False, "quotient lift overclaimed")
    req("any one audited Q-defined representative" in receiver.get("sufficient_replacement_target", ""), "replacement quantifier moved")

    ledger = json.loads((ROOT / SOURCES["stage29_active_kernel_ledger"][0]).read_text())
    camp2 = next(x for x in ledger["class3_kernels"] if x["kernel"] == "K16-C3-CAMPEDELLI-UNIFORM-TORSOR")
    req(camp2["children"] == ["R29-CAMP2"] and "replacement arithmetic theorem proving C_H(Q)=empty" in camp2["needed"], "Stage29 CAMP2 receiver moved")
    camp4 = next(x for x in ledger["class2_kernels"] if x["kernel"] == "K16-C2-BRAUER-EXPLICIT-CHAIN")
    req("R29-CAMP4" in camp4["children"] and camp4.get("endpoint_decision_capable") is True, "CAMP4 sibling asset moved")
    req("explicit 2-primary classes and local evaluations" in camp4.get("exact_wall", ""), "CAMP4 live wall moved")

    br = (ROOT / SOURCES["stage29_brauer_audit"][0]).read_text()
    req("No Brauer--Manin obstruction is claimed until local evaluation maps are computed" in br, "Brauer evaluation firewall moved")
    req("R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints" in br, "Brauer evaluation receiver moved")
    oa = (ROOT / SOURCES["stage29_open_algebraic_brauer_adapter"][0]).read_text()
    req("OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false" in oa, "open algebraic Brauer firewall moved")

    wf = (ROOT / ARSENAL["S34-WF01"][0]).read_text()
    req("CLASS3_RECEIVER_REPLACEMENT_THEOREM_PIPELINE" in wf, "S34-WF01 role moved")
    req("exact one-dimensional or finitely decomposable receivers" in wf, "S34-WF01 applicability moved")
    req("replacement theorem must match the exact receiver quantifiers" in wf, "S34-WF01 quantifier firewall moved")
    al = cert.get("arsenal_locks", {})
    req(al["S34-WF01"].get("application") == "APPLIED_AS_BREADTH_AND_REPLACEMENT_ROUTING_WORKFLOW", "S34-WF01 application moved")
    req(al["S34-W01"].get("status") == "BLOCKED_BY_AUDITED_36_05_MOVING_RAMIFICATION_SUPPORT", "S34-W01 block moved")
    req(al["S34-W02"].get("status") == "NOT_TRIGGERED_NO_EXHAUSTIVE_ELLIPTIC_QUOTIENT_FULL_MW_REDUCTION", "S34-W02 activation moved")
    req(al["S34-W03"].get("status") == "PREPARED_RECEIVER_RESTRICTION_BUT_NO_EXACT_BRANCH_INTERSECTION_YET", "S34-W03 activation moved")
    req(al["S33-PW07"].get("maturity") == "PROVISIONAL" and al["S33-PW08"].get("maturity") == "PROVISIONAL", "provisional Stage33 maturity promoted")

    ca = cert.get("cycle_audit", {})
    req(ca.get("EXHAUSTIVE_VIEW_AUDIT") is True and ca.get("BLIND_REDISCOVERY") is True, "breadth/blind audit lost")
    req(ca.get("blind_generation_done_before_arsenal_classification") is True, "blind ordering moved")
    req(ca.get("claim_all_possible_mathematical_views_exhausted") is False, "breadth audit overclaimed exhaustion")
    rows = ca.get("candidate_ledger", [])
    req([x.get("id") for x in rows] == EXPECTED_IDS, "candidate ledger IDs/order moved")
    req({x["id"]: x["status"] for x in rows} == EXPECTED_STATUS, "candidate classifications moved")
    req((ca.get("live_candidate_count"), ca.get("untested_candidate_count"), ca.get("blocked_candidate_count"), ca.get("dominated_candidate_count")) == (1, 6, 2, 1), "candidate counts moved")
    req(ca.get("split_triggered") is False and ca.get("parking_audit_complete") is False, "cycle split/parking status moved")

    sel = cert.get("selected_next_route", {})
    req(sel.get("id") == "36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT", "selected next route moved")
    req(sel.get("candidate") == "B5_CAMPEDELLI_BRAUER_ETALE_BRAUER", "selected candidate moved")
    req(sel.get("executes_brauer_computation_now") is False, "36-09A computation prematurely executed")
    req(sel.get("replacement_theorem_proved") is False and sel.get("receiver_closed") is False, "replacement/receiver credit leaked")
    ce = cert.get("cycle_exit", {})
    req(ce.get("CYCLE_ROUTE_STATUS") == "BLOCKED_NEW_PATTERN_ISOLATED", "cycle route status moved")
    req(ce.get("CYCLE_LIVE_CANDIDATES") == 1 and ce.get("CYCLE_UNTESTED_CANDIDATES") == 6, "cycle exit counts moved")
    req(ce.get("CYCLE_EXHAUSTIVE_VIEW_AUDIT") is True and ce.get("CYCLE_BLIND_REDISCOVERY") is True, "cycle exit audit flags moved")
    req(ce.get("CYCLE_SPLIT_TRIGGERED") is False and ce.get("CYCLE_PARKING_AUDIT_COMPLETE") is False, "cycle exit split/parking moved")

    req(cert.get("pass_condition") == {"RECEIVER_QUANTIFIERS_FROZEN":True,"EXHAUSTIVE_VIEW_AUDIT":True,"BLIND_REDISCOVERY":True,"CANDIDATE_LEDGER_CLASSIFIED":True,"ONE_ACTIVE_ROUTE_SELECTED":True,"SELECTED_NEXT_ROUTE":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED":False}, "36-09 pass condition moved")
    req(all(v is False for v in cert.get("claims", {}).values()), "36-09 certificate leaked higher credit")

    s = json.loads(STATE.read_text())
    req(s.get("schema") == SCHEMA and s.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT", "V12 lifecycle moved")
    req(s.get("base_main_sha") == BASE, "V12 base moved")
    req(s.get("freshness_sync_36_09") == FRESHNESS, "V12 freshness provenance moved")
    promo = s.get("stage36_36_05_promotion", {})
    req(promo.get("pr") == 1573 and promo.get("exact_head") == "741eb0ef6f07ef6551602c84a1b7493977023feb", "36-05 promotion identity moved")
    req(promo.get("exact_head_ci_run") == 33930463014 and promo.get("exact_head_ci_job") == 101207828353, "36-05 promotion CI moved")
    req(promo.get("merged_main_sha") == PROMO_36_05_MERGE and promo.get("NEW_THEOREM_CREDIT") is False, "36-05 promotion provenance moved")
    u = s.get("completed_units", {}).get("36-09", {})
    req(u.get("certificate_blob_sha") == CERT_BLOB and u.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-09 provisional authority moved")
    req(u.get("EXHAUSTIVE_VIEW_AUDIT") is True and u.get("BLIND_REDISCOVERY") is True, "36-09 state breadth flags moved")
    req(u.get("SELECTED_NEXT_ROUTE") == "36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT", "36-09 state route moved")
    req(u.get("RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED") is False and u.get("NEW_THEOREM_CREDIT") is False, "36-09 state credit leaked")
    cur = s.get("current", {})
    req(cur.get("unit") == "36-09" and cur.get("36_06_entry_allowed") is False, "36-06 boundary moved")
    req(cur.get("36_09A_entry_allowed") is False, "36-09A started before hostile audit")
    req(cur.get("provisional_successor_after_hostile_audit") == "36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT", "36-09 successor moved")
    req("36-09A" not in s.get("completed_units", {}), "36-09A executed inside breadth gate")
    g = s.get("promotion_gates", {})
    req(g.get("receiver_matched_replacement_theorem_proved") is False and g.get("R29_CAMP2_closed") is False, "receiver credit leaked")
    req(all(v is False for v in s.get("claims", {}).values()), "Stage36 higher claim leaked")

    print("PASS STAGE36_36_09_RECEIVER_MATCHED_REPLACEMENT_BREADTH_GATE")
    print("receiver=q_H(U(Q)) subset U_H(Q); exhaustive-view + blind rediscovery certified")
    print("candidate ledger=1 LIVE, 6 UNTESTED, 2 BLOCKED, 1 DOMINATED; split=false; parking=false")
    print("selected=36-09A CAMP4 Brauer compatibility preflight; no Brauer/replacement/receiver/endpoint credit")

if __name__ == "__main__": main()
