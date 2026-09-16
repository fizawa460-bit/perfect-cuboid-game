#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md",
        "aa9a7215467428b55b18ef296ced91b63ec4bf07",
    ),
    "BOUNDARY_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-SATAKE-BOUNDARY-SOURCE-NOTE.md",
        "bea35571b1b8ad8fc14c9a5a9a7342e63fe2c398",
    ),
    "HURWITZ_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY-CERTIFICATE.json",
        "76b458d2f21af7113764447e1a8064e957b025e7",
    ),
    "TWO_QUARTIC_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json",
        "658516458e0af20bbcac28f5f778eeeb361cd468",
    ),
    "PIC0_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json",
        "1a92336433816883757fee844b736181e6848813",
    ),
    "EQUALITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json",
        "62a2d01447016731001d35cc5915880daa2bfada",
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


def load_locked(key):
    rel, _ = LOCKS[key]
    return json.loads((root() / rel).read_text())


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_BALANCED16_000707_BOUNDARY_FIBER_SATURATION_V1", "schema")
    preflight(cert)

    h = load_locked("HURWITZ_CERT")
    tq = load_locked("TWO_QUARTIC_CERT")
    p0 = load_locked("PIC0_CERT")
    eq = load_locked("EQUALITY_CERT")

    # Exact upstream scope.
    req(h["support"]["mask"] == "000707000f0f", "support mask")
    req(h["support"]["node_type_counts"] == [7, 7, 0], "two used node types")
    req(h["support"]["branches_per_supported_node"] == "8*l", "8l branches per node")
    req(h["support"]["supported_branches_total"] == "112*l", "112l total branches")
    req(h["scope_firewall"]["e2_closed"] is False and h["scope_firewall"]["e4_closed"] is False, "e2/e4 upstream open")

    req(eq["uniform_F1_P5"]["g"] == 1, "genus one equality input")
    req(eq["uniform_F1_P5"]["d"] == "112*l", "degree 112l")
    req(eq["equality_consequence"]["both_projections_etale"] is True, "product projections etale")

    # Zero quartics and seven-of-eight support geometry.
    q = tq["zero_quartics"]
    req(q["Q0"] == ["b1=0", "i*a2-a3=0", "a1-c=0"], "Q0 equations")
    req(q["Q1"] == ["b2=0", "i*a3+a1=0", "a2-c=0"], "Q1 equations")
    profile = p0["balanced_profiles"]["000707000f0f"]
    req(profile["zero_quartics"] == 2, "two zero quartics")
    req(profile["supported_nodes_per_zero_quartic"] == 7, "seven supported nodes per quartic")
    req(p0["geometry"]["box_nodes_per_quartic"] == 8, "eight box nodes per quartic")

    zq = cert["zero_quartics"]
    req(zq["satake_boundary_components"] is True, "boundary-component adapter")
    req(zq["fixed_factor_H_orbit_values_per_quartic"] == 2, "two H-orbit values")
    req(zq["orientation_between_Q0_Q1_claimed"] is False, "orientation firewall")

    # Common rank-two quotient geometry.
    rs = cert["rank_two_subgroup"]
    req(rs["order"] == 4, "H order")
    req(rs["e2"]["B_equals_E"] is True and rs["e2"]["genus_B"] == 1, "e2 genus-one quotient")
    req(rs["e4"]["B_to_E_degree"] == 2 and rs["e4"]["B_to_E_etale"] is True, "e4 residual etale double cover")
    req(rs["e4"]["genus_B"] == 1, "e4 genus-one quotient")

    # Arithmetic is coefficientwise in l>0.
    # e=2: 7 nodes * 8l = 56l supported points; two fibers of degree 28l have length 56l.
    e2_supported = 7 * 8
    e2_degree = 28
    req(e2_supported == 2 * e2_degree == 56, "e2 two-fiber saturation arithmetic")

    # e=4: B->E is etale degree two, so the same 56l points lift to 112l;
    # two fibers of degree 56l have total length 112l.
    e4_supported = 2 * 7 * 8
    e4_degree = 56
    req(e4_supported == 2 * e4_degree == 112, "e4 two-fiber saturation arithmetic")

    fs = cert["fiber_saturation"]
    req(fs["e2"]["supported_points_from_one_zero_quartic"] == "56*l", "e2 supported count")
    req(fs["e2"]["two_fiber_total_scheme_length"] == "56*l", "e2 fiber length")
    req(fs["e2"]["points_unramified_for_fixed_factor_projection"] is True, "e2 unramified")
    req(fs["e2"]["each_fiber_reduced_cardinality"] == "28*l", "e2 each fiber full")
    req(fs["e2"]["global_two_value_split"] == "28*l + 28*l", "e2 half split")

    req(fs["e4"]["supported_downstairs_points_from_one_zero_quartic"] == "56*l", "e4 downstairs count")
    req(fs["e4"]["lifts_to_B_per_downstairs_point"] == 2, "e4 lift multiplicity")
    req(fs["e4"]["supported_points_on_B_from_one_zero_quartic"] == "112*l", "e4 B count")
    req(fs["e4"]["two_fiber_total_scheme_length"] == "112*l", "e4 fiber length")
    req(fs["e4"]["points_unramified_for_fixed_factor_projection"] is True, "e4 unramified")
    req(fs["e4"]["each_fiber_reduced_cardinality"] == "56*l", "e4 each fiber full")

    # Do not silently promote the reduction into a closure claim.
    mi = cert["new_missing_invariant"]
    req(mi["coarse_hurwitz_capacity_exhausted"] is True, "coarse capacity exhausted")
    req(mi["per_node_branch_value_concentration_known"] is False, "no per-node concentration")
    req(mi["branchwise_binary_H_orbit_assignment_known_e2"] is False, "binary sheet assignment still missing")

    fw = cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False, "e cases remain open")
    req(fw["orbit_000707_closed"] is False, "orbit remains open")
    req(fw["geometric_uniform_ray_support_population"] == 864, "geometric frontier firewall")
    req(fw["mb104_equality_packet_support_population"] == 768, "equality frontier firewall")
    req(fw["MB104_complete"] is False and fw["span5_closed"] is False, "MB104/span5 firewall")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False, "credit firewall")
    req(fw["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_BOUNDARY_FIBER_SATURATION_V1")
    print("e=2: each zero quartic saturates two specific degree-28l fibers with 28l+28l unramified supported points")
    print("e=4: each zero quartic saturates two specific degree-56l fibers with 56l+56l unramified supported points on B=Z/H")
    print("firewall: no per-node q+/q- concentration; e=2 and e=4 remain open")


if __name__ == "__main__":
    main()
