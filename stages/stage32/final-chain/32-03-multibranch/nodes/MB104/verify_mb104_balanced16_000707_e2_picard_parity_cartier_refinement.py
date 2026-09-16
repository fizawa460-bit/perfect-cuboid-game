#!/usr/bin/env python3
"""Fail-closed verifier for the MB104 Picard-parity Cartier refinement.

This verifier deliberately consumes only compact retained certificates/notes.  It
never imports or expands the Stage33 Picard64 retained payload.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-PARITY-CARTIER-REFINEMENT-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_PICARD_PARITY_CARTIER_REFINEMENT_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-PARITY-CARTIER-REFINEMENT.md",
        "5e37a08cdc7dbb2636fed104d6104230451dbbd7",
    ),
    "PICARD_PARITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json",
        "7621932b87a7558d473bc99a09b46bcb04a433a0",
    ),
    "A1_ENERGY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY-CERTIFICATE.json",
        "0cec993c9d22e31fcf982985b37f0ae82c8cbce7",
    ),
    "AMBIENT_H1_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-H1-TORSION-KILL-CERTIFICATE.json",
        "480f452b75afed9d0f33dbb3e931feaca496d922",
    ),
    "PRODUCT_LINEARIZATION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION-CERTIFICATE.json",
        "ea8bd879093a5ec2054f560807fa05806f96a553",
    ),
    "SHEET_AJ_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SHEET-SELECTED-FIBER-ABEL-JACOBI.md",
        "76ef6c5638b9a601fd01ca28bb01531d7279c180",
    ),
}


def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_json(rr, key):
    rel, _ = LOCKS[key]
    return json.loads((rr / rel).read_text(encoding="utf-8"))


def main():
    rr = root()
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    req(cert["schema"] == "STAGE32_MB104_000707_E2_PICARD_PARITY_CARTIER_REFINEMENT_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    parity = load_json(rr, "PICARD_PARITY_CERT")
    energy = load_json(rr, "A1_ENERGY_CERT")
    h1 = load_json(rr, "AMBIENT_H1_CERT")
    prod = load_json(rr, "PRODUCT_LINEARIZATION_CERT")
    aj_text = (rr / LOCKS["SHEET_AJ_NOTE"][0]).read_text(encoding="utf-8")

    support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    req(parity["variables"]["order"] == support, "support order")
    expected_eqs = [[0] + [int(k == j) for k in range(14)] for j in range(14)]
    req(parity["exact_result"]["equation_rows_l_then_support"] == expected_eqs, "all-even Picard equations")
    req(parity["interpretation"]["canonical_conditions"] == "x_j = 0 mod 2 for every supported node j", "all-even interpretation")
    req(parity["exact_result"]["remaining_parity_classes"] == 1, "unique parity class")
    req(parity["exact_result"]["e2_closed"] is False, "parity does not close e2")

    eid = energy["exact_identity"]
    req(eid["support_nodes"] == support, "A1 support")
    req(eid["branches_per_supported_node_coefficient"] == 8, "8l branches")
    req(eid["a1_exceptional_self_intersection"] == -2, "A1 exceptional square")
    req(eid["centered_variable"] == "d_j=2*x_j-8*l", "centered variable")
    req(eid["centered_y_formula"] == "168*l^2+(1/4)*sum_j d_j^2", "energy y formula")
    req(eid["weighted_cut_formula"] == "84*l^2+(1/8)*sum_j d_j^2", "weighted-cut formula")
    req(eid["same_sheet_formula"] == "84*l^2+56*l-(1/8)*sum_j d_j^2", "same-sheet formula")

    # Coefficientwise parity algebra: x=2y and b=y-2l imply d=4b.
    # The complementary local multiplicity is 8l-x=2(4l-y), also even.
    for l in range(1, 5):
        for y in range(0, 4*l + 1):
            x = 2*y
            b = y - 2*l
            d = 2*x - 8*l
            req(d == 4*b, "d=4b identity")
            req(x % 2 == 0 and (8*l-x) % 2 == 0, "both A1 multiplicities even")
            req((168*l*l + d*d//4) == (168*l*l + 4*b*b), "one-coordinate energy substitution")

    # Exact saturation identities used to remove the constant terms.
    req("x8+x9+x10+x11+x32+x33+x34=28l" in aj_text, "Q1 saturation source")
    req("x0-x1+x2-x3-x24+x25-x26=-4l" in aj_text, "Q0 saturation source")

    resolution = h1["resolution_and_picard"]
    req(resolution["quotient_singularities"] == "isolated A1 rational double points", "only isolated A1 singularities")
    req(h1["active_remainder"]["linear_equivalence"] == "(C_1-C_2) ~ -sum_j(d_j/2)F_j", "ambient linearization")
    req(h1["evidence"]["hostile_audit_passed"] is False, "candidate H1 firewall")

    lin = prod["linearization"]
    req(prod["scope"]["depends_on_candidate_ambient_h1_torsion_kill"] is True, "pencil dependency firewall")
    req(lin["normal_quotient_relation"] == "Gamma ~ tau Gamma on X_H", "Gamma translate linearization")
    req(prod["intersection_and_genus"]["Gamma_self_intersection"] == "392*l^2", "Gamma self intersection")

    exact = cert["exact_parity_refinement"]
    req(exact["support_nodes"] == support, "certificate support")
    req(exact["all_x_j_even"] is True and exact["d_j_divisible_by_4"] is True, "certificate divisibility")
    req(exact["Q1_b_equation"] == "b8+b9+b10+b11+b32+b33+b34=0", "Q1 b equation")
    req(exact["Q0_b_equation"] == "b0-b1+b2-b3-b24+b25-b26=0", "Q0 b equation")
    req(exact["weighted_cut_formula"] == "84*l^2+2*sum_j b_j^2", "two-step cut")
    req(exact["balanced_b_zero_survives"] is True, "balanced firewall")

    cart = cert["exact_cartier_consequence"]
    req(cart["A1_local_class_group"] == "Z/2", "A1 class group")
    req(cart["supported_local_Cartier"] is True, "supported Cartier")
    req(cart["Gamma_globally_Cartier_on_X_H"] is True, "Gamma Cartier")
    req(cart["tauGamma_globally_Cartier_on_X_H"] is True, "tauGamma Cartier")

    pencil = cert["conditional_pencil_consequence"]
    req(pencil["depends_on_candidate_ambient_H1_linearization"] is True, "conditional pencil firewall")
    req(pencil["Gamma_linearly_equivalent_tauGamma"] is True, "pencil linear equivalence")
    req(pencil["h0_lower_bound"] == 2 and pencil["honest_pencil_exists"] is True, "honest pencil")
    req(pencil["base_point_free_claimed"] is False, "no base-point-free overclaim")
    req(pencil["invariant_multiplier_evaluated"] is False, "Kummer multiplier remains open")

    wall = cert["mod4_route_wall"]
    req(wall["same_descent_implies_new_x_mod4_condition"] is False, "no fake mod4 condition")
    req(wall["valid_future_2adic_input_requires_new_geometry"] is True, "future 2-adic firewall")

    route = cert["routing_consequence"]
    req(route["individual_conductor_pair_map_materialized"] is False, "conductor map still open")
    req(route["weighted_cut_upper_bound_proved"] is False, "no cut upper bound")
    req(route["e2_closed"] is False and route["active_leaf_unchanged"] is True, "route firewall")
    req(all(v is False for v in cert["credit_firewall"].values()), "credit firewall")

    print(PASS)
    print("x_even=>d_in_4Z; Gamma,tauGamma Cartier on X_H; conditional honest pencil; repeated descent gives no new mod4 condition; e2_closed=false")


if __name__ == "__main__":
    main()
