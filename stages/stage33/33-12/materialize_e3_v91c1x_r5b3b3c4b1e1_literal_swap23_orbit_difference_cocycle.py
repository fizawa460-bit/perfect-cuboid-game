#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d

HERE = Path(__file__).resolve().parent
C4B1D = HERE / "e3-v91c1x-r5b3b3c4b1d-swap23-tangent-pullback-comparison.json"
C4B1E = HERE / "e3-v91c1x-r5b3b3c4b1e-1757-refinement-unit-or-cech-cochain-preflight.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e1-literal-swap23-orbit-difference-cocycle.json"

C4B1D_SHA = "0b63663ce9e4eda381e7665dbf7722969898ebf931806b5eec3687579882c11e"
C4B1E_SHA = "6a2da8f33ba78a9c385733c8f05c5b8b50c046300d423288c5a4d631b3114a60"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def reconstruct_exact_data():
    d2 = c4b1d.load_locked(c4b1d.D2, c4b1d.D2_SHA)
    b3b2 = c4b1d.load_locked(c4b1d.B3B2, c4b1d.B3B2_SHA)
    c4a = c4b1d.load_locked(c4b1d.C4A, c4b1d.C4A_SHA)
    c4b1 = c4b1d.load_locked(c4b1d.C4B1, c4b1d.C4B1_SHA)
    c4b1c = c4b1d.load_locked(c4b1d.C4B1C, c4b1d.C4B1C_SHA)
    exc = c4b1d.load_locked(c4b1d.EXC, c4b1d.EXC_SHA)

    node_map = {
        row["source_node"]: row["acted_target_node"]
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    expected_map = {
        row["exceptional_id"]: row["swap23_target_exceptional_id"]
        for row in c4b1c["nonconstant_exceptional_targets"]["rows"]
    }
    if set(expected_map) != set(c4b1d.TARGETS):
        raise SystemExit("C4B1C target set moved")
    if any(node_map[eid] != expected_map[eid] for eid in c4b1d.TARGETS):
        raise SystemExit("C4B1C/D2 swap23 target map disagreement")

    er_by_eid = {
        row["exceptional_id"]: row
        for row in exc["exceptional_models"]
    }
    models = {
        eid: c4b1d.c4b1m.reconstruct_exceptional_model(er_by_eid[eid])
        for eid in c4b1d.TARGETS
    }
    c4b1_by_eid = {
        row["exceptional_id"]: row
        for row in c4b1["exceptional_squareclass_reduction"]["rows"]
    }
    c4a_by_eid = {
        row["exceptional_id"]: row
        for row in c4a["exceptional_prime_preflight"]["rows"]
    }
    coeffs = {
        row["carrier_id"]: sp.Matrix(
            [c4b1d.atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]]
        )
        for row in b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    }
    residues = {
        eid: c4b1d.reconstruct_residue_expr(
            eid,
            models[eid],
            coeffs,
            c4a_by_eid,
            c4b1_by_eid,
        )
        for eid in c4b1d.TARGETS
    }
    directed_maps = {}
    for eid in c4b1d.TARGETS:
        tid = expected_map[eid]
        directed_maps[(eid, tid)] = c4b1d.pgl2_tangent_map(
            er_by_eid[eid],
            models[eid],
            er_by_eid[tid],
            models[tid],
        )
    return expected_map, residues, directed_maps


def ratio_for(source: str, target: str, residues: dict, directed_maps: dict):
    t = sp.Symbol("t")
    row_map = directed_maps[(source, target)]
    M = row_map["_matrix"]
    lu = c4b1d.clean(M[0, 0] * t + M[0, 1])
    lv = c4b1d.clean(M[1, 0] * t + M[1, 1])
    target_parameter = c4b1d.clean(lu / lv)
    target_pullback = c4b1d.clean(
        residues[target].subs({t: target_parameter}, simultaneous=True)
    )
    ratio = c4b1d.clean(residues[source] / target_pullback)
    return t, target_parameter, target_pullback, ratio


def build_certificate() -> dict:
    c4 = load_locked(C4B1D, C4B1D_SHA)
    pre = load_locked(C4B1E, C4B1E_SHA)
    expected_map, residues, directed_maps = reconstruct_exact_data()

    comparison_by_source = {}
    for orbit in c4["swap23_nonconstant_orbit_comparison"]["orbits"]:
        for row in orbit["directed_comparisons"]:
            comparison_by_source[row["source_exceptional_id"]] = row
    if set(comparison_by_source) != set(c4b1d.TARGETS):
        raise SystemExit("C4B1D comparison source set moved")

    literal_rows = []
    literal_ratio_by_source = {}
    target_parameter_by_source = {}
    for source in c4b1d.TARGETS:
        target = expected_map[source]
        t, target_parameter, target_pullback, ratio = ratio_for(
            source, target, residues, directed_maps
        )
        encoded_target_pullback = c4b1d.atlas.encode_rational(target_pullback, [t])
        encoded_ratio = c4b1d.atlas.encode_rational(ratio, [t])
        expected = comparison_by_source[source]
        if csha(encoded_target_pullback) != expected["target_pullback_rational_Qi_t_sha256"]:
            raise SystemExit(f"C4B1D target pullback reconstruction moved for {source}")
        if csha(encoded_ratio) != expected["source_over_pulled_target_rational_Qi_t_sha256"]:
            raise SystemExit(f"C4B1D literal difference reconstruction moved for {source}")
        sq = c4b1d.rational_squareclass(ratio, t)
        if sq != expected["squareclass_difference"]:
            raise SystemExit(f"C4B1D squareclass replay moved for {source}")

        num, den = sp.fraction(c4b1d.clean(ratio))
        literal_ratio_by_source[source] = ratio
        target_parameter_by_source[source] = target_parameter
        literal_rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "source_bound_target_parameter_Qi_t": c4b1d.atlas.encode_rational(target_parameter, [t]),
            "literal_difference_rational_Qi_t": encoded_ratio,
            "literal_difference_rational_Qi_t_sha256": csha(encoded_ratio),
            "numerator_total_degree": int(sp.Poly(sp.expand(num), t, extension=sp.I).degree()),
            "denominator_total_degree": int(sp.Poly(sp.expand(den), t, extension=sp.I).degree()),
            "squareclass_difference": sq,
        })

    orbit_identity_rows = []
    seen = set()
    t = sp.Symbol("t")
    for source in c4b1d.TARGETS:
        target = expected_map[source]
        key = tuple(sorted((source, target)))
        if key in seen:
            continue
        seen.add(key)
        forward = literal_ratio_by_source[source]
        reverse = literal_ratio_by_source[target]
        forward_target_parameter = target_parameter_by_source[source]
        pulled_reverse = c4b1d.clean(
            reverse.subs({t: forward_target_parameter}, simultaneous=True)
        )
        product = c4b1d.clean(forward * pulled_reverse)
        if product != 1:
            raise SystemExit(
                f"swap23 orbit-difference rational 1-cocycle identity failed: {source}<->{target}: {product}"
            )
        orbit_identity_rows.append({
            "orbit_members": list(key),
            "forward_source": source,
            "reverse_source": target,
            "forward_times_pullback_reverse_equals_one": True,
            "identity_rational_Qi_t": c4b1d.atlas.encode_rational(product, [t]),
        })

    if len(orbit_identity_rows) != 2:
        raise SystemExit("expected exactly two nonconstant swap23 orbits")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e1.literal_swap23_orbit_difference_cocycle.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E1_LITERAL_SWAP23_ORBIT_DIFFERENCE_RATIONAL_COCYCLE",
        "role": "EXACT_NONCREDIT_LITERAL_RECONSTRUCTION_OF_THE_FOUR_C4B1D_NONSQUARE_RATIONAL_DIFFERENCES_AND_THEIR_SWAP23_ORBIT_COCYCLE_IDENTITY",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1d_sha256": C4B1D_SHA,
            "c4b1e_refinement_attachment_preflight_sha256": C4B1E_SHA,
            "r5b2d2_sha256": c4b1d.D2_SHA,
            "r5b3b2_sha256": c4b1d.B3B2_SHA,
            "r5b3b3c4a_sha256": c4b1d.C4A_SHA,
            "r5b3b3c4b1_sha256": c4b1d.C4B1_SHA,
            "r5b3b3c4b1c_sha256": c4b1d.C4B1C_SHA,
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
        },
        "literal_orbit_difference": {
            "directed_row_count": len(literal_rows),
            "rows": sorted(literal_rows, key=lambda row: row["source_exceptional_id"]),
            "orbit_identity_rows": sorted(orbit_identity_rows, key=lambda row: row["orbit_members"]),
        },
        "exact_consequence": {
            "all_four_c4b1d_difference_rational_functions_reconstructed_literally": True,
            "all_four_literal_reconstructions_match_c4b1d_hashes_and_squareclasses": True,
            "swap23_orbit_difference_rational_group_1_cocycle_identity_verified_on_both_nonconstant_orbits": True,
            "this_group_action_rational_cocycle_is_not_the_required_cover_indexed_cech_square_root_1_cochain": True,
            "literal_per_piece_d2_pullback_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "refinement_attachment_preflight_consistency": {
            "attached_directed_count": pre["preflight_counts"]["directed_orbit_difference_count"],
            "attached_exceptional_piece_slots": pre["preflight_counts"]["exceptional_common_refinement_piece_slots_attached"],
            "global_common_refinement_piece_count": pre["preflight_counts"]["global_common_refinement_piece_count"],
        },
        "next_exact_step": "pull each literal difference rational function into the corresponding four D2 36-piece exceptional refinement blocks, expose the literal piece localizers/projection coordinates, and classify whether the required ell_ij/r_ij equations are solvable without further refinement",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E1 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
