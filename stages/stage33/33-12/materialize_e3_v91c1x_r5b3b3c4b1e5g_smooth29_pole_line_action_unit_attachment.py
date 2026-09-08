#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1e5b_rees_gauge_cross_action_divisor_transport as e5b

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
R5B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
E4 = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"
E5A = HERE / "e3-v91c1x-r5b3b3c4b1e5a-rees-gauge-factor-carrier-binding.json"
E5D = HERE / "e3-v91c1x-r5b3b3c4b1e5d-pole-ideal-constant-gm-action-units.json"
E5F = HERE / "e3-v91c1x-r5b3b3c4b1e5f-whole-cover-action-transport-debt-partition.json"
C2 = HERE / "e3-v91c1x-r5b2c2-jacobian-minor-smooth-cover-node-glue.json"
EXC = HERE.parent / "33-07" / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5g-smooth29-pole-line-action-unit-attachment.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
R5B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
E5A_SHA = "a294f594ab15230f09c8dd3e595f8b343ec88eded5e117600c5fb6181f2eac99"
E5D_SHA = "bd5ebd3bd923433597c7f0f9dc2a07d222df10f9aa118273beca74ad4ff28fd0"
E5F_SHA = "fa982518e59950b4b6e39b7cfa9f454f585c932d61514af23fbd252674ea72cc"
C2_SHA = "8e5b2b38cd38d39c35e908d630a208ac7d84d5dfc8f23e9e59939a1aec6bf8f9"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def clean(x: sp.Expr) -> sp.Expr:
    return atlas.clean(x)


def projective_equal(a: sp.Expr, b: sp.Expr, variables: list[sp.Symbol]) -> bool:
    if a == 0 or b == 0:
        return False
    sa, _ = atlas.projective_poly_signature(a, variables)
    sb, _ = atlas.projective_poly_signature(b, variables)
    return sa == sb


def saturation_basis_by_factor(
    ideal_generators: list[sp.Expr], factor: sp.Expr, variables: list[sp.Symbol], tag: str
) -> list[sp.Expr]:
    y = sp.Symbol(f"sat_{tag}")
    G = sp.groebner(
        list(ideal_generators) + [1 - y * factor],
        y, *variables,
        order="lex",
        extension=I,
    )
    elim = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(y)]
    if not elim:
        raise SystemExit(f"empty saturation elimination basis: {tag}")
    return elim


def ideals_equal(
    lhs: list[sp.Expr], rhs: list[sp.Expr], variables: list[sp.Symbol]
) -> bool:
    Gl = sp.groebner(lhs, *variables, order="grevlex", extension=I)
    Gr = sp.groebner(rhs, *variables, order="grevlex", extension=I)
    return (
        all(clean(Gr.reduce(sp.expand(f))[1]) == 0 for f in lhs)
        and all(clean(Gl.reduce(sp.expand(f))[1]) == 0 for f in rhs)
    )


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    r5b3a = load_locked(R5B3A, R5B3A_SHA)
    e4 = load_locked(E4, E4_SHA)
    e5a = load_locked(E5A, E5A_SHA)
    e5d = load_locked(E5D, E5D_SHA)
    e5f = load_locked(E5F, E5F_SHA)
    c2 = load_locked(C2, C2_SHA)
    exc = load_locked(EXC, EXC_SHA)

    idx = d2["common_refinement_index"]
    if idx["total_piece_count"] != 1757 or idx["smooth_piece_count"] != 29:
        raise SystemExit("R5B2D2 refinement counts moved")
    smooth_rows = d2["smooth_cover_action"]["minor_action_rows"]
    if len(smooth_rows) != 29:
        raise SystemExit("R5B2D2 smooth action inventory moved")
    if not d2["construction_status"]["source_bound_swap23_coordinate_action_materialized"]:
        raise SystemExit("R5B2D2 source-bound swap23 action lost")

    packages = r5b3a["a2_02_source"]["package_rows"]
    if len(packages) != 8:
        raise SystemExit("R5B3A package inventory moved")
    for row in packages:
        pull = row["common_refinement_pullback"]
        if pull["piece_count"] != 1757 or not pull["assignment_is_source_projection_of_317_cover_pullback"]:
            raise SystemExit("R5B3A common-refinement package assignment moved")

    if c2["finite_cover"]["smooth_minor_chart_count"] != 29:
        raise SystemExit("R5B2C2 smooth cover count moved")
    if not c2["smooth_complement_cover"]["smooth_complement_is_union_of_29_principal_minor_opens"]:
        raise SystemExit("R5B2C2 smooth-complement cover statement moved")

    prior = e5f["coverage_accounting"]
    if prior["genuine_exceptional_block_action_unit_piece_count"] != 144:
        raise SystemExit("E5F prior certified action-unit count moved")
    if e5f["next_exact_leaf"] != "V91C1X_R5B3B3C4B1E5G_SMOOTH_29_SAME_REPRESENTATIVE_ACTION_TRANSPORT_PREFLIGHT":
        raise SystemExit("E5F next leaf moved")

    e5d_rows = {
        row["source_exceptional_id"]: row
        for row in e5d["pole_principal_equation_action"]["rows"]
    }
    if set(e5d_rows) != set(TARGETS):
        raise SystemExit("E5D directed source inventory moved")
    if not e5d["exact_consequence"]["all_four_rational_hilbert90_transitions_act_between_the_displayed_pole_principal_equations_with_nonzero_constant_Qi_coefficients"]:
        raise SystemExit("E5D global pole-equation coefficient identity moved")

    e4_rows = {
        row["source_exceptional_id"]: row
        for row in e4["rees_rational_gauge_lifts"]["rows"]
    }
    if set(e4_rows) != set(TARGETS):
        raise SystemExit("E4 source inventory moved")

    pole_rows_by_source: dict[str, list[dict]] = {eid: [] for eid in TARGETS}
    for row in e5a["factorization"]["rows"]:
        if row["equation_kind"] != "pole":
            continue
        if not row["factor_is_linear_rees_direction_hyperplane"]:
            raise SystemExit("E5A pole factor ceased to be linear")
        eid = row["source_exceptional_id"]
        if eid not in pole_rows_by_source:
            raise SystemExit(f"unexpected E5A pole source {eid}")
        pole_rows_by_source[eid].append(row)
    if any(not rows for rows in pole_rows_by_source.values()):
        raise SystemExit("one E5A source lost pole factors")

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    metas = {eid: atlas.node_meta(er_by_eid[eid]) for eid in TARGETS}

    X = list(sp.symbols("a1 a2 a3 b1 b2 b3 c"))
    H = list(sp.symbols("H0:6"))
    surface_ideal = [clean(x) for x in c2.quadrics(sp.Matrix(X))]
    Gsurface = sp.groebner(surface_ideal, *X, order="grevlex", extension=I)

    unique_factors: dict[str, sp.Expr] = {}
    denominator_rows = []
    for eid in TARGETS:
        product = sp.Integer(1)
        local_sigs = []
        for row in pole_rows_by_source[eid]:
            fH = atlas.decode_poly(row["normalized_factor_Qi_H"], H)
            fX = e5b.ambient_lift_from_rees_direction(fH, metas[eid], H, X)
            if sp.Poly(fX, *X, extension=I).total_degree() != 1:
                raise SystemExit(f"ambient pole factor not linear: {eid}")
            sig = atlas.projective_poly_signature(fX, X)[0]
            unique_factors.setdefault(sig, fX)
            exp = int(row["factor_exponent"])
            product = clean(product * fX ** exp)
            local_sigs.append({
                "projective_signature_sha256": sig,
                "exponent": exp,
            })

        D = atlas.decode_poly(e4_rows[eid]["homogeneous_q_denominator_Qi_H"], H)
        Damb = e5b.ambient_lift_from_rees_direction(D, metas[eid], H, X)
        if not projective_equal(Damb, product, X):
            raise SystemExit(f"E4 pole denominator reconstruction moved: {eid}")
        denominator_rows.append({
            "source_exceptional_id": eid,
            "ambient_denominator_projective_signature_sha256": atlas.projective_poly_signature(Damb, X)[0],
            "pole_factor_rows": local_sigs,
            "reconstructed_projectively_from_e5a_factors": True,
        })

    factor_checks = []
    all_nonzerodivisor = True
    for idx, (sig, factor) in enumerate(sorted(unique_factors.items())):
        rem = clean(Gsurface.reduce(sp.expand(factor))[1])
        if rem == 0:
            sat_equal = False
        else:
            sat = saturation_basis_by_factor(surface_ideal, factor, X, f"e5g_{idx}")
            sat_equal = ideals_equal(surface_ideal, sat, X)
        all_nonzerodivisor &= sat_equal
        factor_checks.append({
            "ambient_pole_factor_projective_signature_sha256": sig,
            "linear_over_Qi": True,
            "nonzero_mod_global_surface_ideal": rem != 0,
            "global_surface_ideal_saturation_by_factor_equals_surface_ideal": sat_equal,
            "nonzerodivisor_on_global_surface_coordinate_ring_exact": sat_equal,
            "nonzerodivisor_after_localization_to_each_of_29_jacobian_minor_opens": sat_equal,
        })

    action_units_by_source = {
        eid: e5d_rows[eid]["zero_equation_projective_matching_scalar_Qi"]
        for eid in TARGETS
    }
    piece_rows = []
    for row in smooth_rows:
        piece_rows.append({
            "piece_id": row["common_refinement_piece_id"],
            "source_minor_id": row["source_minor_id_equal_to_pullback_open"],
            "acted_target_minor_id": row["acted_target_minor_id"],
            "minor_pullback_scalar_Qi": row["pullback_scalar_Qi"],
            "all_eight_a2_02_literal_package_pullbacks_available_via_source_projection": True,
            "four_e5d_pole_line_action_units_Qi": action_units_by_source,
            "all_four_pole_line_action_units_are_regular_invertible_on_this_piece": all_nonzerodivisor,
        })

    if len(piece_rows) != 29 or len({r["piece_id"] for r in piece_rows}) != 29:
        raise SystemExit("smooth 29 piece rows do not close")

    promoted_smooth_piece_count = 29 if all_nonzerodivisor else 0
    total_certified = int(prior["genuine_exceptional_block_action_unit_piece_count"]) + promoted_smooth_piece_count
    remaining = 1757 - total_certified
    if all_nonzerodivisor and (total_certified != 173 or remaining != 1584):
        raise SystemExit("E5G expected 173/1584 coverage arithmetic moved")

    if all_nonzerodivisor:
        next_leaf = "V91C1X_R5B3B3C4B1E5H_EXCEPTIONAL_17_SQUARE_TRIVIAL_BLOCK_SAME_REPRESENTATIVE_ACTION_TRANSPORT_PREFLIGHT"
        next_step = (
            "materialize actual source-bound same-representative pole-line action transitions on the 17 square/trivial-residue exceptional blocks; "
            "do not assign unit 1 merely from residue square/triviality; keep the 27 constant-only nonsquare blocks as separate explicit debt"
        )
    else:
        next_leaf = "V91C1X_R5B3B3C4B1E5G1_SMOOTH_29_MINOR_LOCALIZED_POLE_FACTOR_NONZERODIVISOR_REPAIR"
        next_step = (
            "for any failed ambient pole factor, test exact saturation after adjoining/localizing each of the 29 Jacobian minors rather than inferring failure from the global projective-coordinate-ring test"
        )

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5g.smooth29_pole_line_action_unit_attachment.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5G_SMOOTH_29_POLE_LINE_ACTION_UNIT_ATTACHMENT",
        "role": "EXACT_NONCREDIT_SMOOTH_COMPLEMENT_CARTIER_LEGITIMACY_AND_ATTACHMENT_OF_THE_EXISTING_E5D_POLE_LINE_ACTION_UNITS_TO_ALL_29_D2_SMOOTH_COMMON_REFINEMENT_PIECES",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_sha256": D2_SHA,
            "r5b3a_sha256": R5B3A_SHA,
            "c4b1e4_sha256": E4_SHA,
            "c4b1e5a_sha256": E5A_SHA,
            "c4b1e5d_sha256": E5D_SHA,
            "c4b1e5f_sha256": E5F_SHA,
            "r5b2c2_sha256": C2_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "smooth_cover_cartier_legitimacy": {
            "global_surface_quadric_generator_count": len(surface_ideal),
            "unique_ambient_linear_pole_factor_count": len(unique_factors),
            "all_unique_ambient_pole_factors_nonzerodivisors_on_global_surface_coordinate_ring": all_nonzerodivisor,
            "localization_to_29_smooth_principal_opens_preserves_nonzerodivisor": all_nonzerodivisor,
            "factor_checks": factor_checks,
            "denominator_rows": denominator_rows,
        },
        "smooth_piece_attachment": {
            "smooth_piece_count": 29,
            "piece_rows": piece_rows,
            "source_bound_swap23_minor_action_materialized": True,
            "eight_literal_a2_02_package_pullbacks_available_on_each_piece": True,
            "e5d_four_direction_pole_action_coefficients_attached_to_each_piece": True,
            "genuine_pole_line_action_unit_attachment_verified_on_all_29_pieces": all_nonzerodivisor,
        },
        "coverage_accounting": {
            "prior_genuine_exceptional_action_unit_piece_count": int(prior["genuine_exceptional_block_action_unit_piece_count"]),
            "new_genuine_smooth_action_unit_piece_count": promoted_smooth_piece_count,
            "total_genuine_pole_line_action_unit_piece_count": total_certified,
            "coverage_fraction_denominator": 1757,
            "remaining_same_representative_action_transport_piece_count": remaining,
            "remaining_exceptional_block_count": 44,
            "remaining_exceptional_piece_count": 44 * 36,
        },
        "exact_consequence": {
            "smooth_29_domain_action_is_upgraded_to_genuine_pole_line_action_unit_attachment": all_nonzerodivisor,
            "this_does_not_assemble_the_eight_a2_02_packages_into_one_global_kummer_or_cech_representative": True,
            "this_does_not_materialize_cover_wide_line_bundle_gm_1_cocycle_ell_ij": True,
            "this_does_not_materialize_square_root_1_cochain_r_ij": True,
            "this_does_not_materialize_literal_mu2_2_cocycle": True,
            "this_does_not_verify_triple_overlap_action_difference_identity": True,
            "this_does_not_verify_h2_fixedness": True,
            "square_or_trivial_exceptional_residue_is_not_relabelled_as_unit_one": True,
        },
        "diagnostic_boundary": {
            "what_is_now_exact_if_pass": "the already materialized E5D pole-equation action coefficients are genuine regular invertible pole-line action units on every one of the 29 smooth D2 refinement pieces because every E5A ambient pole factor is a global-surface nonzerodivisor and localization preserves that property",
            "what_is_still_missing": "a source-bound single-representative assembly and cover-wide ell_ij/r_ij/mu2/triple-overlap data, plus actual same-representative action transport on the remaining 44 exceptional blocks",
            "pole_line_action_unit_attachment_is_not_full_line_bundle_or_h2_glue": True,
        },
        "next_exact_leaf": next_leaf,
        "next_exact_step": next_step,
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "source_bound_single_representative_credit": False,
            "whole_cover_ell_ij_credit": False,
            "whole_cover_r_ij_credit": False,
            "literal_mu2_2_cocycle_credit": False,
            "exceptional_cancellation_credit": False,
            "unramifiedness_credit": False,
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "smooth_pass": cert["smooth_piece_attachment"]["genuine_pole_line_action_unit_attachment_verified_on_all_29_pieces"],
            "total_action_unit_pieces": cert["coverage_accounting"]["total_genuine_pole_line_action_unit_piece_count"],
            "remaining_pieces": cert["coverage_accounting"]["remaining_same_representative_action_transport_piece_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5G certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
