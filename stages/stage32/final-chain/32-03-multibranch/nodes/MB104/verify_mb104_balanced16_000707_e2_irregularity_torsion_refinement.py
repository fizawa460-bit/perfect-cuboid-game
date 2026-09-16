#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-IRREGULARITY-TORSION-REFINEMENT-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-IRREGULARITY-TORSION-REFINEMENT.md",
        "fab8808df91a6e3b61776cf1023ae62564dcadcb",
    ),
    "SOURCE_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FINITE-QUOTIENT-IRREGULARITY-TORSION-SOURCE-NOTE.md",
        "5862aa62f0337e85b4dc802234e9d38507108b2e",
    ),
    "INTERMEDIATE_H": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md",
        "d2e3056137360a9e15ae7c820088d2977a5eb137",
    ),
    "EXPLICIT_RESIDUAL_KUMMER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE.md",
        "5017d7c137f6d4994a34cb1edac28aadcd832a2a",
    ),
    "AMBIENT_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md",
        "2bdb46e79be8a745880622c9c0643eb13ef20b26",
    ),
    "HALF_BRANCH": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md",
        "e22de5a6f4be163268e699cde03d37e1e564d43b",
    ),
    "ANTIINVARIANT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION-CERTIFICATE.json",
        "727e332aa551313f7fb127c77145dc24535b6080",
    ),
    "HURWITZ_CAPACITY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY.md",
        "c91f97b738faa66a49a068824f9b8c3739d4a8fa",
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
    req(cert["schema"] == "STAGE32_MB104_000707_E2_IRREGULARITY_TORSION_REFINEMENT_V1", "schema")
    req(cert["active_leaf"] == ACTIVE, "active leaf")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob(p) == want, f"SOURCE_LOCK_FAIL {key}")

    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    field = cert["function_field_bridge"]
    req(field["X_H_extension"] == "k(B)(r), r^2=2*f_t", "X_H field")
    req(field["Y_extension"] == "k(S)(sqrt(f_t)) up to inversion and nonzero square scalar", "Y field")
    req(field["kS_equals_kB"] is True, "resolution function field")
    req(field["over_C_two_is_square"] is True, "2 square over C")
    req(field["inversion_preserves_quadratic_square_class"] is True, "inversion square class")
    req(field["same_function_field"] is True, "same function field")
    req(field["birational_only_not_isomorphic"] is True, "birational firewall")

    q = cert["irregularity"]
    req(q["factor_quotient"] == "C8/H ~= P1", "factor quotient")
    req(q["H1_C8_H_invariant_dimension"] == 0, "factor invariant H1")
    # Kunneth: two copies of the same zero-dimensional invariant space.
    req(q["H1_product_Hdiag_invariant_dimension"] == 0 + 0, "product invariant H1")
    req(q["H1_X_H_dimension"] == 0, "quotient H1")
    req(q["finite_quotient_surface_singularities_rational_over_C"] is True, "rational quotient singularities")
    req(q["H1_resolution_dimension"] == 0, "resolution H1")
    req(q["q_Y"] == 0, "q(Y)")
    req(q["Pic0_Y_trivial"] is True, "Pic0(Y)")

    tor = cert["torsion_refinement"]
    req(tor["numerical_remainder"] == "w=(C_1-C_2)+sum_j(d_j/2)F_j == 0 numerically", "remainder")
    req(tor["Pic_tau_Y_finite"] is True, "Pic tau finite")
    req(tor["fixed_exponent_exists"] is True, "fixed exponent")
    req(tor["fixed_exponent_independent_of_l"] is True, "uniform exponent")
    req(tor["linear_equivalence_after_fixed_exponent"] == "N_Y*(C_1-C_2) ~ -N_Y*sum_j(d_j/2)F_j", "torsion linear relation")
    req(tor["N_Y_value_computed"] is False, "no torsion exponent guess")
    req(tor["w_linearly_trivial_claimed"] is False, "no w~0 overclaim")

    route = cert["routing_consequence"]
    req(route["continuous_Pic0_ambiguity_remaining"] is False, "Pic0 ambiguity removed")
    req(route["finite_torsion_ambiguity_remaining"] is True, "torsion remains")
    req(route["individual_conductor_pair_map_materialized"] is False, "no conductor map")
    req(route["active_leaf_unchanged"] is True, "leaf unchanged")
    req(route["e2_closed"] is False, "e2 open")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_IRREGULARITY_TORSION_REFINEMENT_V1")
    print("q(Y)=0; Pic^0(Y)=0; numerical anti-invariant remainder is fixed finite torsion; conductor sign open; credit 0")


if __name__ == "__main__":
    main()
