#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD.md",
        "b7221c44a7c9c4d8c16bb4045ed4cfff379699bc",
    ),
    "FIBRATION_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md",
        "b71225ac859eef5afefeebd019a97c403ed27655",
    ),
    "RESIDUAL_CHARACTER_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER-CERTIFICATE.json",
        "5e12d24f85d1fe27e53edab337bbacc45fb34cdb",
    ),
    "PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "SECTION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json",
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL missing {key}: {rel}")
        got = blob(p)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL {key}: expected {expected}, got {got}")


def load(key):
    return json.loads((root() / LOCKS[key][0]).read_text())


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_000707_ABSENT_HALF_FIBER_PICARD_V1", "schema")
    preflight(cert)

    rc = load("RESIDUAL_CHARACTER_CERT")
    p0 = load("PIC0_CERT")
    sec = load("SECTION_CERT")

    # Exact upstream residual-character scope.
    req(rc["scope"]["mask"] == "000707000f0f", "residual mask")
    req(rc["scope"]["node_type_counts"] == [7, 7, 0], "absent node type")
    req(rc["scope"]["allowed_e"] == [2, 4], "remaining e cases")
    req(rc["half_fiber"]["eta"] == "O_E(A-B)", "upstream eta")
    req(rc["case_classification"]["e2_eta_zero"] is True and rc["case_classification"]["e4_eta_nonzero"] is True, "upstream eta classification")

    # G2 retained geometry.
    req(p0["geometry"]["elliptic_quartic_count"] == 12, "12 G2 elliptic quartics")
    req(p0["geometry"]["box_nodes_per_quartic"] == 8, "8 box nodes per G2")
    req(sec["incidence16_size3"]["section"] == "4 smooth elliptic quartics", "b_j=0 four-quartic section")
    req(sec["incidence16_size3"]["node_component_incidence"] == "each of 16 section nodes lies on exactly two quartics", "b_j node incidence")

    g2 = cert["g2_fibration"]
    req(g2["two_complementary_product_fibrations"] is True, "two product fibrations")
    req(g2["bad_fibers_per_fibration"] == 6, "six bad fibers")
    req(g2["bad_reduced_component_family"] == "G2", "G2 bad components")
    req(g2["bad_reduced_component_degree"] == 4 and g2["bad_reduced_component_genus"] == 1, "quartic genus-one")
    req(g2["bad_reduced_component_self_square"] == -4, "Q square")
    req(g2["box_nodes_per_G2"] == 8, "G2 node count")
    req(g2["canonical_intersection_per_G2"] == 4, "K.Q")

    # A1 resolution fiber arithmetic: F=2Q+sum_8 E.
    Q2 = -4
    QE = 1
    E2 = -2
    n = 8
    F2 = 4 * Q2 + 4 * n * QE + n * E2
    KF = 2 * 4
    req(F2 == 0, "fiber self-square zero")
    req(KF == 8, "K.F=8 genus-five fiber")

    rf = cert["resolution_fiber"]
    req(rf["formula"] == "F_Q=2*Q+sum_(p in T_Q)E_p", "fiber formula")
    req(rf["T_Q_size"] == 8 and rf["Q_dot_E_p"] == 1 and rf["E_p_square"] == -2, "local A1 coefficients")
    req(rf["F_Q_square"] == 0 and rf["K_dot_F_Q"] == 8, "certificate fiber numerics")

    hf = cert["half_fiber_relation"]
    req(hf["same_fibration"] is True, "same fibration")
    req(hf["formula"] == "2*(Q_a-Q_b) ~ sum_(p in T_b)E_p - sum_(p in T_a)E_p", "half-fiber relation")
    req(hf["surface_difference_torsion_claimed"] is False, "no surface torsion overclaim")

    # Uniform-ray intersection with an absent G2 curve: 7l*4 - 0 = 28l.
    cr = cert["carrier_restriction"]
    req(cr["absent_exceptional_coefficient_in_D_l"] == 0, "absent coefficient zero")
    req(cr["D_l_dot_absent_E"] == 0, "D.E absent zero")
    req(cr["integral_carrier_disjoint_from_absent_exceptionals"] is True, "carrier avoids absent exceptionals")
    req(7 * 4 == 28, "D_l.Q coefficient")
    req(cr["D_l_dot_Q_a"] == "28*l" and cr["D_l_dot_Q_b"] == "28*l", "half-fiber degrees")
    req(cr["deg_A"] == "28*l" and cr["deg_B"] == "28*l", "A/B degree")
    req(cr["eta_surface_restriction"] == "O_E((Q_a-Q_b)|_E)", "eta surface restriction")
    req(cr["eta_two_torsion"] is True, "eta two-torsion")

    tf = cert["two_factor_classes"]
    req(tf["required_eta_1_equals_eta_2"] is True, "joint eta equality")
    req(tf["required_difference_restriction_trivial"] == "O_E((Delta_1-Delta_2)|_E)=O_E", "difference restriction")

    tors = cert["torsion_firewall"]
    req(tors["Pic_S_torsion_free"] is True, "Pic torsion-free source fact")
    req(tors["Pic_S_torsion_free_closes_e4"] is False, "torsion-free does not close e4")

    fw = cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False, "e cases open")
    req(fw["orbit_000707_closed"] is False, "orbit open")
    req(fw["geometric_uniform_ray_support_population"] == 864, "geometric frontier")
    req(fw["mb104_equality_packet_support_population"] == 768, "packet frontier")
    req(fw["MB104_complete"] is False and fw["span5_closed"] is False, "MB104/span5 firewall")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False, "credit firewall")
    req(fw["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_ABSENT_HALF_FIBER_PICARD_V1")
    print("bad fiber on S: F_Q=2Q+sum_8 E; F_Q^2=0, K.F_Q=8")
    print("eta=O_E((Q_a-Q_b)|_E); two factors give explicit Delta_1,Delta_2 in Pic(S)")
    print("firewall: Pic(S) torsion-free does not force eta=0; e=2,e=4 remain open")


if __name__ == "__main__":
    main()
