#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
CERT_PATH = ROOT / "stages/stage36/36-03/physical-open-boundary.json"
INVENTORY_PATH = ROOT / "stages/stage36/36-02/representative-inventory.json"
BASE = "bdd707e52ded061014bfbb6158762e8b997e7a38"
PROMOTION_MERGE = "26fb608cb2551ab2102ae36ad3b57c063959df58"
AUDITED_36_02_INVENTORY_BLOB = "88130b9380a677a191f91c24df87618e65be0a2f"

SOURCES = {
    "stage36_roadmap": ("stages/stage36/ROADMAP.md", "eeedda0e89e24f851c989b5ec83e7b320e1ad99e"),
    "stage29_endpoint_hub_graph": ("stages/stage29/29-06/endpoint-hub-graph.json", "7ea59474767f81fbaa4837c8cbc94b535560617b"),
    "stage29_endpoint_source_crosswalk": ("stages/stage29/29-06/source-crosswalk.md", "30fe24229f14070f10234801b6a57a9ea6129052"),
    "stage29_physical_open_audit": ("stages/stage29/29-02f/audit.md", "b72f61749bcf0c2535135da11f882560c3a01cce"),
    "stage29_exact_sign_cover_model": ("stages/stage29/29-02ha/exact-sign-cover-model.md", "fc2d5284a259750f45d2d756a952002671e3bccc"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_arithmetic_routing": ("stages/stage29/29-02hb/arithmetic-routing.md", "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
}
ARSENAL = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S30-WF02": ("docs/arsenal/cards/workflows/S30-WF02.md", "38e4625155eb079bbe3d50d663c6256559319886"),
    "S30-WF03": ("docs/arsenal/cards/workflows/S30-WF03.md", "12740198aba19ade18302819f8e890dbda4eb701"),
    "S34-W03": ("docs/arsenal/cards/formal/S34-W03.md", "1d5275321f42768a6414d4610ac912c63be43f96"),
}
EXPECTED_REPS = ["Q6_GEOM8", "Q2_GEOM8", "Q2_GEOM2"]
LINES = {
    "A1": (1, 0, 0), "A2": (0, 1, 0), "A3": (0, 0, 1),
    "B3": (1, 1, 0), "B2": (1, 0, 1), "B1": (0, 1, 1), "C": (1, 1, 1),
}
TRIPLES = {
    ((0, 0, 1), ("A1", "A2", "B3")),
    ((0, 1, 0), ("A1", "A3", "B2")),
    ((1, 0, 0), ("A2", "A3", "B1")),
    ((0, 1, -1), ("A1", "B1", "C")),
    ((1, 0, -1), ("A2", "B2", "C")),
    ((1, -1, 0), ("A3", "B3", "C")),
}
DOUBLES = {
    ((1, -1, -1), ("B2", "B3")),
    ((1, -1, 1), ("B1", "B3")),
    ((1, 1, -1), ("B1", "B2")),
}


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def canonical_point(p):
    g = 0
    for x in p:
        g = gcd(g, abs(x))
    require(g > 0, "duplicate projective lines")
    p = tuple(x // g for x in p)
    for x in p:
        if x:
            return tuple(-y for y in p) if x < 0 else p
    raise SystemExit("zero projective point")


def reconstruct_arrangement(lines):
    pts = {}
    for left, right in itertools.combinations(lines, 2):
        p = canonical_point(cross(lines[left], lines[right]))
        incidence = tuple(sorted(name for name, c in lines.items() if sum(c[i]*p[i] for i in range(3)) == 0))
        pts[p] = incidence
    require(all(len(v) <= 3 for v in pts.values()), "fourfold concurrence appeared")
    return ({(p, v) for p, v in pts.items() if len(v) == 3}, {(p, v) for p, v in pts.items() if len(v) == 2})


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    state = json.loads(STATE_PATH.read_text())

    require(cert.get("schema") == "STAGE36_36_03_PHYSICAL_OPEN_PUSH_BOUNDARY_V1", "36-03 certificate schema moved")
    require(cert.get("status") == "EXACT_PHYSICAL_OPEN_PUSH_BOUNDARY_PENDING_HOSTILE_AUDIT", "36-03 certificate status moved")
    require(cert.get("base_main_sha") == BASE, "36-03 certificate base moved")
    require(cert.get("freshness_sync") == {
        "sync_pr": 1554,
        "main_sha": BASE,
        "merge_commit": "a741d573da4045cdee984a0541d71a55a9d7c0a9",
        "scope": "Stage32-only advance via #1550; no Stage36, Stage29 Campedelli/physical-open source, or Arsenal authority changes",
    }, "36-03 freshness sync moved")

    # Bind the hostile-audited 36-02 mathematical inventory byte-for-byte.
    require(blob_sha(INVENTORY_PATH) == AUDITED_36_02_INVENTORY_BLOB, "audited 36-02 inventory blob drift")
    inventory = json.loads(INVENTORY_PATH.read_text())
    require(list(inventory.get("representatives", {}).keys()) == EXPECTED_REPS, "audited representative order/set moved")
    require(cert.get("audited_Q_representatives") == EXPECTED_REPS, "36-03 representative scope moved")
    auth = cert.get("source_authority", {})
    require(auth.get("stage36_36_02_hostile_audit_review") == 5113379283, "36-02 audit review moved")
    require(auth.get("stage36_36_02_audited_head") == "3a78f9ff156b53f509625d353df48d1b3e02b836", "36-02 audited head moved")
    require(auth.get("stage36_36_02_merge") == "4c93ccb79e95cbcd9e2416ad3b6a3f4788d6f586", "36-02 audited PR merge moved")
    require(auth.get("stage36_36_02_promotion_merge") == PROMOTION_MERGE, "36-02 promotion merge moved")
    require(auth.get("stage36_36_02_inventory") == {"path": "stages/stage36/36-02/representative-inventory.json", "blob_sha": AUDITED_36_02_INVENTORY_BLOB}, "36-02 inventory authority moved")

    declared_sources = cert.get("source_locks", {})
    for key, (rel, sha) in SOURCES.items():
        require(declared_sources.get(key) == {"path": rel, "blob_sha": sha}, f"source declaration moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"source blob drift: {key}")
    declared_arsenal = cert.get("arsenal_locks", {})
    for key, (rel, sha) in ARSENAL.items():
        row = declared_arsenal.get(key, {})
        require(row.get("path") == rel and row.get("blob_sha") == sha, f"Arsenal declaration moved: {key}")
        require(blob_sha(ROOT / rel) == sha, f"Arsenal blob drift: {key}")
    require("IMMUTABLE_LAYERED_CERTIFICATE_REPLAY" in (ROOT / ARSENAL["S30-WF02"][0]).read_text(), "S30-WF02 role moved")
    require("ADAPTER_CREDIT_LAYER_FIREWALL" in (ROOT / ARSENAL["S30-WF03"][0]).read_text(), "S30-WF03 role moved")
    require("RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in (ROOT / ARSENAL["S34-W03"][0]).read_text(), "S34-W03 role moved")
    require(declared_arsenal["S34-W03"].get("executed") is False, "S34-W03 executed prematurely")

    roadmap = (ROOT / SOURCES["stage36_roadmap"][0]).read_text()
    for needle in ["36-03 — PHYSICAL_OPEN_PUSH_AND_BOUNDARY", "free-action locus", "six A1 quotient points", "canonical/resolution distinction", "branch/deleted boundary", "ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT=true", "CONVERSE_LIFT_CLAIM=false"]:
        require(needle in roadmap, f"roadmap anchor missing: {needle}")

    hub = json.loads((ROOT / SOURCES["stage29_endpoint_hub_graph"][0]).read_text())
    nodes = {r["id"]: r for r in hub.get("nodes", [])}
    edges = {r["id"]: r for r in hub.get("edges", [])}
    require(nodes.get("U_PHYS", {}).get("base_field") == "Q", "U_PHYS field moved")
    require("a1*a2*a3 != 0" in nodes.get("U_PHYS", {}).get("data", ""), "U_PHYS definition moved")
    require("resolution is an isomorphism here" in nodes.get("U_PHYS", {}).get("data", ""), "U_PHYS resolution scope moved")
    require(nodes.get("CAMPEDELLI_BAR_H", {}).get("data", "").startswith("Cbar_H=Sbar/H; six A1 points"), "canonical quotient node moved")
    require(nodes.get("CAMPEDELLI_H", {}).get("base_field") == "Q", "resolved quotient Q-form moved")
    e03, e15, e15r, e16r = (edges.get(k, {}) for k in ("E03", "E15", "E15R", "E16R"))
    require(e03.get("rational_point_lift") == "isomorphism on U_PHYS; not inverse on the A1 locus as a morphism", "E03 open scope moved")
    require(e15.get("relation") == "FINITE_ETALE_QUOTIENT_BY_H" and e15.get("degree") == 8 and e15.get("field") == "Q", "E15 moved")
    require(e15.get("proof_status") == "AUDITED_EXACT_FOR_ALL_TEN_KERNELS", "E15 scope moved")
    require(e15.get("rational_point_pushforward") is True and e15.get("rational_point_lift") == "requires H-torsor descent", "E15 transfer moved")
    require(e15r.get("relation") == "FINITE_ETALE_RESOLVED_QUOTIENT" and e15r.get("degree") == 8 and e15r.get("field") == "Q", "E15R moved")
    require(e15r.get("rational_point_lift") == "requires H-torsor descent", "E15R lift moved")
    require(e16r.get("rational_point_lift") == "isomorphism off six A1 points", "E16R A1 scope moved")

    crosswalk = (ROOT / SOURCES["stage29_endpoint_source_crosswalk"][0]).read_text()
    require("U=Sbar∩D_+(a1a2a3)" in crosswalk and "smooth and resolution-isomorphic" in crosswalk, "source crosswalk open scope moved")
    physical_audit = (ROOT / SOURCES["stage29_physical_open_audit"][0]).read_text()
    for needle in ["Ubar=Sbar intersect D_+(a1*a2*a3)", "24 Q-defined side conics", "48 exceptional curves", "72 geometric irreducible components", "PHYSICAL_OPEN_AUDIT=PASS", "BOUNDARY_72_COMPONENT_LEDGER_AUDIT=PASS"]:
        require(needle in physical_audit, f"physical-open audit anchor missing: {needle}")

    sign_model = (ROOT / SOURCES["stage29_exact_sign_cover_model"][0]).read_text()
    for needle in ["[x:y:z]=[a_1^2:a_2^2:a_3^2]", "L_{a1}=x", "L_{a2}=y", "L_{a3}=z", "L_{b3}=x+y", "L_{b2}=x+z", "L_{b1}=y+z", "L_c=x+y+z", "A=\\mathbf P^2\\setminus D"]:
        require(needle in sign_model, f"sign-cover anchor missing: {needle}")
    adapter = (ROOT / SOURCES["stage29_campedelli_quotient_adapter"][0]).read_text()
    for needle in ["H ∩ I_x = 0", "H`-action on the entire singular canonical model `Sbar` is free", "finite etale `H`-torsor, even at the rational-double-point locus", "There are exactly six such `A1` points.", "S  --etale degree 8-->  C_H", "On the physical endpoint open, all seven branch forms are nonzero", "U_endpoint(Q) -> C_H(Q)", "No converse is asserted."]:
        require(needle in adapter, f"Campedelli adapter anchor missing: {needle}")
    routing = (ROOT / SOURCES["stage29_campedelli_arithmetic_routing"][0]).read_text()
    for needle in ["U_endpoint(Q) -> C_H(Q)", "rational quotient point need not lift rationally upstairs", "exact physical-open image and deleted boundary", "three certified Q-symmetry representatives"]:
        require(needle in routing, f"arithmetic-routing anchor missing: {needle}")

    declared_lines = {name: tuple(v) for name, v in cert.get("seven_line_base", {}).get("line_coefficients", {}).items()}
    require(declared_lines == LINES, "seven-line coefficient system moved")
    triples, doubles = reconstruct_arrangement(declared_lines)
    require(triples == TRIPLES and doubles == DOUBLES, "seven-line intersection reconstruction mismatch")
    require(all(0 in p for p, _ in triples), "a triple point entered xyz!=0")
    require(all(all(x != 0 for x in p) for p, _ in doubles), "a remaining double point left xyz!=0")
    declared_triples = {(tuple(r["point"]), tuple(sorted(r["lines"]))) for r in cert["seven_line_base"]["triple_points"]}
    declared_doubles = {(tuple(r["point"]), tuple(sorted(r["lines"]))) for r in cert["seven_line_base"]["remaining_double_points"]}
    require(declared_triples == TRIPLES and declared_doubles == DOUBLES, "certificate intersection ledger moved")

    physical = cert.get("physical_open", {})
    require(physical.get("smooth") is True and physical.get("resolution_isomorphism_on_open") is True, "physical-open smoothness/resolution moved")
    require(physical.get("boundary_on_S_Qbar") == {"Q_defined_side_conics": 24, "exceptional_curves": 48, "geometric_irreducible_components": 72}, "physical boundary ledger moved")
    chain = cert.get("global_quotient_chain", {})
    require(chain.get("H_group") == "(Z/2)^3" and chain.get("H_torsor_degree") == 8 and chain.get("Q_defined") is True, "H quotient identity moved")
    require(chain.get("H_action_free_on_all_Sbar") is True and chain.get("canonical_H_torsor_finite_etale") is True and chain.get("resolved_H_torsor_finite_etale") is True, "global H-torsor scope moved")
    require(chain.get("rational_point_pushforward") is True and chain.get("rational_point_lift_requires_H_torsor_descent") is True, "H rational transfer moved")

    boundary = cert.get("canonical_resolution_boundary", {})
    require(boundary.get("Cbar_H_A1_count") == 6 and boundary.get("all_Cbar_H_A1_points_outside_physical_side_nonzero_open") is True, "quotient A1 boundary moved")
    require(boundary.get("Sbar_A1_count") == 48 and boundary.get("Sbar_A1_points_over_each_triple_point") == 8 and boundary.get("all_48_Sbar_A1_points_outside_Ubar") is True, "Sbar A1 ledger moved")
    require(boundary.get("C_H_exceptional_minus2_curves_over_A1_count") == 6 and boundary.get("physical_image_avoids_C_H_exceptional_curves") is True, "resolved quotient exceptional boundary moved")
    require(boundary.get("canonical_and_resolved_targets_identical_on_physical_image") is True, "canonical/resolved physical image moved")

    image = cert.get("physical_rational_image", {})
    require(image.get("all_seven_line_values_nonzero_for_Q_points") is True, "physical Q image branch-free fact moved")
    require(image.get("endpoint_Q_point_to_each_representative_C_H_Q") is True, "endpoint quotient push moved")
    require(image.get("endpoint_Q_point_to_each_representative_branch_free_quotient_open_Q") is True, "endpoint branch-free image moved")
    require(image.get("converse_lift_claim") is False, "converse lift overclaim")
    firewall = cert.get("scheme_vs_rational_firewall", {})
    require(firewall.get("Ubar_Qbar_subset_of_pi_inverse_A") is False, "scheme/rational firewall lost")
    require(firewall.get("q_H_inverse_U_H_equals_U") is True, "restricted quotient open saturation moved")
    require(firewall.get("U_H_Q_equals_q_H_of_U_Q_claimed") is False, "rational quotient-image equality overclaim")

    behavior = cert.get("torsor_and_branch_behavior", {})
    require(behavior.get("H_torsor_degenerates_on_boundary") is False and behavior.get("H_torsor_is_global_etale_even_at_RDP") is True, "H-torsor boundary behavior moved")
    require(behavior.get("beta_H_to_P2_branched_on_D7") is True and behavior.get("radical_squareclass_chart_requires_nonzero_line_values") is True, "radical branch chart moved")
    require(behavior.get("radical_zero_branch_cases_require_separate_treatment") is True and behavior.get("physical_rational_endpoint_image_avoids_those_zero_cases") is True, "zero/branch handling moved")
    require(behavior.get("global_C_H_Q_points_on_branch_are_not_ruled_out") is True and behavior.get("global_C_H_Q_emptiness_claim") is False, "global quotient overclaim")
    restricted = cert.get("restricted_receiver_preparation", {})
    require(restricted.get("S34_W03_prepared") is True and restricted.get("receiver_intersection_exclusion_executed") is False and restricted.get("receiver_closed") is False, "S34-W03 preparation/credit moved")
    require("no quotient component-count claim" in restricted.get("deleted_boundary", ""), "quotient boundary count firewall missing")

    require(cert.get("pass_condition") == {"ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT": True, "CONVERSE_LIFT_CLAIM": False}, "36-03 pass condition moved")
    promotion = cert.get("promotion", {})
    require(promotion.get("hostile_audit_required") is True and promotion.get("promoted_to_audited_authority") is False and promotion.get("next_leaf_before_audit_allowed") is False, "36-03 promotion gate moved")
    require(promotion.get("provisional_successor_after_audit") == "36-04_EXPLICIT_H_TORSOR_AND_LIFT_CLASS", "36-04 successor moved")
    require(all(v is False for v in cert.get("claims", {}).values()), "36-03 certificate leaked higher credit")

    require(state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V6_36_03_PENDING_AUDIT", "Stage36 V6 state schema moved")
    require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT" and state.get("base_main_sha") == BASE, "Stage36 36-03 state lifecycle moved")
    require(state.get("freshness_sync_36_03") == {
        "sync_pr": 1554,
        "main_sha": BASE,
        "merge_commit": "a741d573da4045cdee984a0541d71a55a9d7c0a9",
        "scope": "Stage32-only advance via #1550; no Stage36, Stage29 Campedelli/physical-open source, or Arsenal authority changes",
    }, "36-03 state freshness moved")
    gates = state.get("promotion_gates", {})
    require(gates.get("source_authority_lock_complete") is True and gates.get("three_Q_representatives_exact") is True, "audited predecessor gates lost")
    for key, value in gates.items():
        if key not in {"source_authority_lock_complete", "three_Q_representatives_exact"}:
            require(value is False, f"later gate prematurely promoted: {key}")
    unit = state.get("completed_units", {}).get("36-03", {})
    require(unit.get("status") == "EXACT_PHYSICAL_OPEN_PUSH_BOUNDARY_PENDING_HOSTILE_AUDIT", "36-03 provisional status moved")
    require(unit.get("ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT") is True and unit.get("CONVERSE_LIFT_CLAIM") is False and unit.get("NEW_THEOREM_CREDIT") is False, "36-03 provisional credit moved")
    require(unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-03 prematurely promoted")
    current = state.get("current", {})
    require(current.get("unit") == "36-03" and current.get("next_exact_leaf") == "36-03_PHYSICAL_OPEN_PUSH_AND_BOUNDARY", "36-04 started before audit")
    require(current.get("provisional_successor_after_hostile_audit") == "36-04_EXPLICIT_H_TORSOR_AND_LIFT_CLASS", "36-04 successor moved")
    require(all(v is False for v in state.get("claims", {}).values()), "Stage36 state leaked higher credit")

    print("PASS STAGE36_36_03_PHYSICAL_OPEN_PUSH_BOUNDARY_V1")
    print("physical_boundary_on_S=24 side conics + 48 exceptional = 72 geometric components")
    print("seven_line_arrangement=6 triple(xyz=0)+3 double(xyz!=0); six quotient A1 points outside physical side-open")
    print("H-torsor=global etale degree8; beta_H radical chart branches on D7; physical Q-image is branch-free")
    print("arsenal=S30-WF02,S30-WF03,S34-W03(prepared_not_executed)")
    print("36-03 provisional exact result; hostile audit required; 36-04 not started")


if __name__ == "__main__":
    main()