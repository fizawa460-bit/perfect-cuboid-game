#!/usr/bin/env python3
"""Fail-closed compact verifier for the MB104 e=2 half-hyperplane factorization."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_HALF_HYPERPLANE_FACTORIZATION_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION.md",
        "ba7ea7a7e21f0e4ca5d8b96c3dac1dbafbbddff6",
    ),
    "CARTIER_REFINEMENT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-PARITY-CARTIER-REFINEMENT-CERTIFICATE.json",
        "e380c99ef818f6064d6da77615337eeee1cb4863",
    ),
    "PICARD_PARITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json",
        "7621932b87a7558d473bc99a09b46bcb04a433a0",
    ),
    "AMBIENT_H1_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-H1-TORSION-KILL-CERTIFICATE.json",
        "480f452b75afed9d0f33dbb3e931feaca496d922",
    ),
    "ANTIINVARIANT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION-CERTIFICATE.json",
        "727e332aa551313f7fb127c77145dc24535b6080",
    ),
    "ABSENT_HALF_FIBER_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD-CERTIFICATE.json",
        "5fdae0e985be1875417442203835879a206312a8",
    ),
    "BOUNDARY_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md",
        "aa9a7215467428b55b18ef296ced91b63ec4bf07",
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
    req(cert["schema"] == "STAGE32_MB104_000707_E2_HALF_HYPERPLANE_FACTORIZATION_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    cartier = load_json(rr, "CARTIER_REFINEMENT_CERT")
    parity = load_json(rr, "PICARD_PARITY_CERT")
    h1 = load_json(rr, "AMBIENT_H1_CERT")
    anti = load_json(rr, "ANTIINVARIANT_CERT")
    half = load_json(rr, "ABSENT_HALF_FIBER_CERT")
    boundary = (rr / LOCKS["BOUNDARY_NOTE"][0]).read_text(encoding="utf-8")

    support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    req(parity["variables"]["order"] == support, "support order")
    req(parity["interpretation"]["canonical_conditions"] == "x_j = 0 mod 2 for every supported node j", "all-even input")
    req(cartier["exact_parity_refinement"]["d_j_divisible_by_4"] is True, "d in 4Z input")
    req(cartier["exact_cartier_consequence"]["Gamma_globally_Cartier_on_X_H"] is True, "Cartier upstream")

    req(anti["exact_numerical_decomposition"]["supported_exceptional_preimage"] == "E_j^+ disjoint_union E_j^-", "split exceptionals")
    req(anti["exact_numerical_decomposition"]["centered_variable"] == "d_j=2*x_j-8*l", "centered variable")
    req(h1["active_remainder"]["linear_equivalence"] == "(C_1-C_2) ~ -sum_j(d_j/2)F_j", "candidate linear relation")
    req(h1["resolution_and_picard"]["Pic_tau_Y_trivial"] is True, "Pic torsion kill")
    req(h1["evidence"]["hostile_audit_passed"] is False, "candidate-status firewall")
    req(half["carrier_restriction"]["integral_carrier_disjoint_from_absent_exceptionals"] is True, "absent branch disjointness")
    req("D_l=7lH-4l sum_(p in Sigma)E_p" in boundary, "carrier class source")

    # Exact coefficient algebra for the two effective conjugate divisors.
    # G1-G2 has coefficient 2y-4l=d/2 on E+ and its negative on E-;
    # G1+G2 has coefficient 4l on each lift, independently of y.
    for l in range(1, 7):
        for y in range(0, 4*l + 1):
            x = 2*y
            d = 2*x - 8*l
            req(2*y - 4*l == d//2, "difference coefficient")
            req(y + (4*l-y) == 4*l, "allocation-free sum coefficient")
            req(y >= 0 and 4*l-y >= 0, "effectivity coefficients")

    eff = cert["effective_conjugate_divisors"]
    req(eff["G2_equals_tau_G1"] is True, "deck conjugacy")
    req(eff["difference"] == "G1-G2=(C1-C2)+sum_j(d_j/2)F_j", "difference formula")
    req(eff["linearly_equivalent_conditional"] is True and eff["both_effective"] is True, "effective equivalent pair")

    sm = cert["allocation_free_sum"]
    req(sm["carrier_class"] == "D_l=7*l*H-4*l*sum_supported E_j", "carrier class")
    req(sm["sum"] == "G1+G2~pi^*(7*l*H)", "allocation-free sum")
    req(sm["half_hyperplane"] == "2*G1~2*G2~pi^*(7*l*H)", "half-hyperplane identity")
    req(sm["allocation_disappears_from_doubled_class"] is True, "allocation elimination")

    uniq = cert["uniqueness"]
    req(uniq["PicY_two_torsion_trivial_conditional"] is True, "2-torsion uniqueness input")
    req(uniq["half_hyperplane_square_root_unique"] is True, "unique root")
    req(uniq["allocation_changes_effective_representative_not_line_bundle_class"] is True, "fixed line class")

    even = cert["even_l"]
    req(even["pure_pullback"] == "Lambda_(2m)~=pi^*O_S(7*m*H)", "even-l pure pullback")
    req(even["G1_G2_distinct_effective_members"] is True, "distinct even-l members")
    req(even["defining_section_not_pure_deck_eigenvector"] is True, "both eigenspaces needed")
    req(even["antiinvariant_eigenspace_vanishing_claimed"] is False, "no effectivity overclaim")

    # Bezout normalization for odd l is coefficientwise exact.
    for l in range(1, 12, 2):
        u = 1
        v = (1-l)//2
        req(u*l + 2*v == 1, "odd-l Bezout")
        # 2*(u Lambda_l + 7v H) = 7*(u*l+2v) H = 7H.
        req(7*(u*l + 2*v) == 7, "primitive half coefficient")
    odd = cert["odd_l"]
    req(odd["primitive_half_relation"] == "2*Lambda_*=7*pi^*H", "primitive half")
    req(odd["scaling"] == "Lambda_l=l*Lambda_*", "odd scaling")
    req(odd["effectivity_of_primitive_half_claimed"] is False, "odd effectivity firewall")

    route = cert["routing_consequence"]
    req(route["individual_conductor_pair_map_materialized"] is False, "conductor map open")
    req(route["weighted_cut_upper_bound_proved"] is False, "no cut upper bound")
    req(route["balanced_allocation_excluded"] is False, "balanced survives")
    req(route["e2_closed"] is False and route["active_leaf_unchanged"] is True, "route firewall")
    req(all(v is False for v in cert["credit_firewall"].values()), "credit firewall")

    print(PASS)
    print("G1,G2 effective conjugates; G1+G2=pi^*(7lH); conditional 2G1=pi^*(7lH); even-l pure pullback; e2_closed=false")


if __name__ == "__main__":
    main()
