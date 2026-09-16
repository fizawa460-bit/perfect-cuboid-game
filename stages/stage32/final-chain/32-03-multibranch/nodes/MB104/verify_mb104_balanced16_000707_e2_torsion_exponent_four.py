#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-TORSION-EXPONENT-FOUR-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-TORSION-EXPONENT-FOUR.md",
        "1f7e9ddd426c6df61c1aff30fb7ef42d12ea3a3b",
    ),
    "SOURCE_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FINITE-QUOTIENT-TORSION-EXPONENT-FOUR-SOURCE-NOTE.md",
        "d0c2b5b374b048c558b9cb74911cfee75c5bb8cc",
    ),
    "IRREGULARITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-IRREGULARITY-TORSION-REFINEMENT-CERTIFICATE.json",
        "4f0e8872ad03427348b0f16d1cdd14711e67d4b1",
    ),
    "INTERMEDIATE_H": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md",
        "d2e3056137360a9e15ae7c820088d2977a5eb137",
    ),
    "HURWITZ_CAPACITY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY.md",
        "c91f97b738faa66a49a068824f9b8c3739d4a8fa",
    ),
    "ANTIINVARIANT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION-CERTIFICATE.json",
        "727e332aa551313f7fb127c77145dc24535b6080",
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


def main():
    rr = root()
    req(CERT.is_file(), "missing certificate")
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_TORSION_EXPONENT_FOUR_V1", "schema")
    req(cert["active_leaf"] == ACTIVE, "active leaf")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob(p) == want, f"SOURCE_LOCK_FAIL {key}")

    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    geom = cert["quotient_geometry"]
    req(geom["H_order"] == 4, "H order")
    req(geom["H_generators"] == ["s1", "s2"], "H generators")
    req(geom["s1_fixed_points_on_C8"] == 8, "s1 fixed points")
    req(geom["s2_fixed_points_on_C8"] == 8, "s2 fixed points")
    req(geom["fixed_sets_disjoint"] is True, "fixed sets disjoint")
    req(geom["product_s1s2_fixed_point_free"] is True, "product involution free")
    req(geom["X_H_singularities"] == "A1 only", "A1 quotient singularities")

    desc = cert["descent"]
    req(desc["torsion_formal_A1_fibre_trivial"] is True, "formal fibre torsion")
    req(desc["rational_singularity_descent_applied"] is True, "descent")
    req(desc["torsion_birationally_preserved_for_smooth_surfaces"] is True, "birational torsion")

    pic = cert["picard_norm"]
    req(pic["H1_product_H_invariant_dimension"] == 0, "H1 invariant")
    req(pic["torsion_pullback_lies_in_Pic0_P"] is True, "pullback Pic0")
    req(pic["H_norm_zero_on_Pic0"] is True, "norm zero")
    req(pic["quotient_pullback_injective"] is True, "pullback injective")
    req(pic["torsion_exponent_divides"] == 4, "exponent four")

    rel = cert["active_remainder"]
    req(rel["w"] == "(C_1-C_2)+sum_j(d_j/2)F_j", "w formula")
    req(rel["four_w_linearly_trivial"] is True, "4w trivial")
    req(rel["linear_equivalence"] == "4(C_1-C_2) ~ -2*sum_j d_j F_j", "4w relation")
    req(rel["two_w_linearly_trivial_claimed"] is False, "no 2w overclaim")
    req(rel["w_linearly_trivial_claimed"] is False, "no w overclaim")

    route = cert["routing_consequence"]
    req(route["finite_torsion_ambiguity_remaining"] is True, "torsion still possible")
    req(route["individual_conductor_pair_map_materialized"] is False, "conductor open")
    req(route["active_leaf_unchanged"] is True, "leaf unchanged")
    req(route["e2_closed"] is False, "e2 open")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_TORSION_EXPONENT_FOUR_V1")
    print("Pic^tau(Y) torsion exponent divides 4; 4w~0; conductor transition open; credit 0")


if __name__ == "__main__":
    main()
