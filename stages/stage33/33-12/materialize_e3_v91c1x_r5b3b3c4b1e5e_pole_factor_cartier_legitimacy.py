#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2c1_all_48_node_isolating_rees_neighborhoods as c1
import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
E4 = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"
E5A = HERE / "e3-v91c1x-r5b3b3c4b1e5a-rees-gauge-factor-carrier-binding.json"
E5D = HERE / "e3-v91c1x-r5b3b3c4b1e5d-pole-ideal-constant-gm-action-units.json"
C1 = HERE / "e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json"
EXC = HERE.parent / "33-07" / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5e-pole-factor-cartier-legitimacy.json"

E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
E5A_SHA = "a294f594ab15230f09c8dd3e595f8b343ec88eded5e117600c5fb6181f2eac99"
E5D_SHA = "bd5ebd3bd923433597c7f0f9dc2a07d222df10f9aa118273beca74ad4ff28fd0"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
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


def reconstruct_locked_chart(eid: str, point: sp.Matrix, cp: int, c1_row: dict):
    germ = c1.adapted_local_germ(eid, point)
    d = germ["d"]
    e = sp.Symbol("e")
    u = list(sp.symbols("u0:5"))
    nonp = [j for j in range(6) if j != cp]
    sub = {d[cp]: e}
    for k, j in enumerate(nonp):
        sub[d[j]] = e * u[k]
    pullbacks = [clean(g.subs(sub)) for g in germ["gens"]]
    strict = [clean(gp / (e ** o)) for gp, o in zip(pullbacks, germ["orders"])]
    exceptional = [clean(g.subs(e, 0)) for g in strict]
    commitment = {
        "chart_id": f"{eid}_GLOBAL_ISOLATING_REES_D{cp}",
        "node_open": f"D_+(Lambda_{eid})",
        "pivot_displacement_index_0based": cp,
        "nonpivot_displacement_indices_in_u_order": nonp,
        "strict_transform_division_orders": germ["orders"],
        "strict_transform_generators_Qi": [c1.encode_poly(g, [e, *u]) for g in strict],
        "exceptional_fiber_generators_Qi": [c1.encode_poly(g, u) for g in exceptional],
        "exceptional_uniformizer": "e",
        "pullback_ideal_t_saturation_equals_strict_transform_ideal": True,
    }
    expected = c1_row["standard_rees_chart_commitment_sha256s"][cp]
    actual = csha(commitment)
    if actual != expected:
        raise SystemExit(f"C1 strict chart commitment moved {eid}/D{cp}: {actual} != {expected}")
    return e, u, nonp, strict


def saturation_basis_by_linear_factor(
    strict: list[sp.Expr], factor: sp.Expr, variables: list[sp.Symbol], tag: str
) -> list[sp.Expr]:
    y = sp.Symbol(f"sat_{tag}")
    G = sp.groebner(list(strict) + [1 - y * factor], y, *variables, order="lex", extension=I)
    elim = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(y)]
    if not elim:
        raise SystemExit(f"empty saturation elimination basis: {tag}")
    return elim


def saturation_equals_strict(
    strict: list[sp.Expr], sat: list[sp.Expr], variables: list[sp.Symbol], Gstrict: sp.GroebnerBasis
) -> bool:
    Gsat = sp.groebner(sat, *variables, order="grevlex", extension=I)
    return (
        all(clean(Gsat.reduce(sp.expand(f))[1]) == 0 for f in strict)
        and all(clean(Gstrict.reduce(sp.expand(f))[1]) == 0 for f in sat)
    )


def projective_equal(a: sp.Expr, b: sp.Expr, variables: list[sp.Symbol]) -> bool:
    if a == 0 or b == 0:
        return False
    sa, _pa = atlas.projective_poly_signature(a, variables)
    sb, _pb = atlas.projective_poly_signature(b, variables)
    return sa == sb


def build_certificate() -> dict:
    e4 = load_locked(E4, E4_SHA)
    e5a = load_locked(E5A, E5A_SHA)
    e5d = load_locked(E5D, E5D_SHA)
    c1cert = load_locked(C1, C1_SHA)
    exc = load_locked(EXC, EXC_SHA)

    if not e5d["exact_consequence"]["constant_gm_action_coefficients_materialized_on_all_144_attached_exceptional_d2_pieces"]:
        raise SystemExit("E5D 144-piece constant-unit boundary moved")
    if e5d["pole_principal_equation_action"]["attached_d2_piece_count"] != 144:
        raise SystemExit("E5D attached D2 piece count moved")

    e4_rows = {
        row["source_exceptional_id"]: row
        for row in e4["rees_rational_gauge_lifts"]["rows"]
    }
    if set(e4_rows) != set(TARGETS):
        raise SystemExit("E4 four-source inventory moved")

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
        raise SystemExit("one E5A source lost all pole factors")

    c1_rows = {row["exceptional_id"]: row for row in c1cert["node_rows"]}
    points = {
        row["exceptional_id"]: sp.Matrix([c1.decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
        for row in exc["exceptional_models"]
    }

    H = list(sp.symbols("H0:6"))
    source_rows = []
    chart_rows = []
    factor_rows = []
    nonconstant_factor_checks = 0
    nonconstant_factor_passes = 0
    constant_unit_localizations = 0
    full_pole_equation_chart_count = 0

    for eid in TARGETS:
        erow = e4_rows[eid]
        D = atlas.decode_poly(erow["homogeneous_q_denominator_Qi_H"], H)
        factor_data = []
        product = sp.Integer(1)
        for frow in pole_rows_by_source[eid]:
            f = atlas.decode_poly(frow["normalized_factor_Qi_H"], H)
            exp = int(frow["factor_exponent"])
            if sp.Poly(f, *H, extension=I).total_degree() != 1:
                raise SystemExit(f"nonlinear pole factor replayed at {eid}")
            product = clean(product * f ** exp)
            factor_data.append((frow, f, exp))
        if not projective_equal(D, product, H):
            raise SystemExit(f"E5A pole factor product no longer reconstructs E4 denominator at {eid}")

        source_nonconstant = 0
        source_passes = 0
        source_constant = 0
        for cp in range(6):
            e, u, nonp, strict = reconstruct_locked_chart(eid, points[eid], cp, c1_rows[eid])
            variables = [e, *u]
            Gstrict = sp.groebner(strict, *variables, order="grevlex", extension=I)
            subH = {H[cp]: sp.Integer(1)}
            for k, j in enumerate(nonp):
                subH[H[j]] = u[k]

            local_product = sp.Integer(1)
            local_factor_count = 0
            local_nonconstant = 0
            local_passes = 0
            local_constants = 0
            for frow, f, exp in factor_data:
                floc = clean(f.subs(subH, simultaneous=True))
                if floc == 0:
                    raise SystemExit(f"pole factor vanished identically after chart localization {eid}/D{cp}")
                local_product = clean(local_product * floc ** exp)
                local_factor_count += 1
                degree = sp.Poly(floc, *u, extension=I).total_degree()
                if degree == 0:
                    if floc.free_symbols:
                        raise SystemExit("degree-zero pole localization retained symbols")
                    local_constants += 1
                    source_constant += 1
                    constant_unit_localizations += 1
                    factor_rows.append({
                        "source_exceptional_id": eid,
                        "source_rees_chart_index_0based": cp,
                        "ambient_projective_hyperplane_signature_sha256": frow["ambient_projective_hyperplane_signature_sha256"],
                        "factor_exponent": exp,
                        "localization_kind": "NONZERO_CONSTANT_UNIT",
                        "localized_factor_Qi_u": c1.encode_poly(floc, u),
                        "nonzerodivisor_exact": True,
                        "saturation_required": False,
                    })
                    continue
                if degree != 1:
                    raise SystemExit(f"localized pole factor is not linear {eid}/D{cp}: degree={degree}")
                rem = clean(Gstrict.reduce(sp.expand(floc))[1])
                if rem == 0:
                    raise SystemExit(f"linear pole factor is zero in strict-transform ring {eid}/D{cp}")
                tag = f"{eid}_{cp}_{frow['ambient_projective_hyperplane_signature_sha256'][:12]}"
                sat = saturation_basis_by_linear_factor(strict, floc, variables, tag)
                sat_equal = saturation_equals_strict(strict, sat, variables, Gstrict)
                nonconstant_factor_checks += 1
                source_nonconstant += 1
                local_nonconstant += 1
                if sat_equal:
                    nonconstant_factor_passes += 1
                    source_passes += 1
                    local_passes += 1
                factor_rows.append({
                    "source_exceptional_id": eid,
                    "source_rees_chart_index_0based": cp,
                    "ambient_projective_hyperplane_signature_sha256": frow["ambient_projective_hyperplane_signature_sha256"],
                    "factor_exponent": exp,
                    "localization_kind": "NONCONSTANT_LINEAR_FACTOR",
                    "localized_factor_Qi_u": c1.encode_poly(floc, u),
                    "nonzero_mod_locked_strict_transform_ideal": True,
                    "saturation_of_locked_strict_ideal_by_factor_equals_locked_strict_ideal": sat_equal,
                    "nonzerodivisor_exact": sat_equal,
                    "saturation_required": True,
                })

            Dloc = clean(D.subs(subH, simultaneous=True))
            if not projective_equal(Dloc, local_product, u):
                raise SystemExit(f"localized E4 denominator factor product mismatch {eid}/D{cp}")
            full_pole_equation_chart_count += 1
            chart_rows.append({
                "source_exceptional_id": eid,
                "source_rees_chart_index_0based": cp,
                "c1_strict_chart_commitment_replayed_exact": True,
                "pole_factor_localization_count": local_factor_count,
                "nonconstant_linear_factor_count": local_nonconstant,
                "nonconstant_linear_factor_nonzerodivisor_pass_count": local_passes,
                "nonzero_constant_unit_factor_count": local_constants,
                "localized_e4_pole_equation_reconstructed_projectively_from_e5a_factors": True,
                "full_pole_equation_is_nonzerodivisor_as_product_of_nonzerodivisors": local_passes == local_nonconstant,
                "localization_to_each_d2_principal_open_preserves_nonzerodivisor": local_passes == local_nonconstant,
            })

        source_rows.append({
            "source_exceptional_id": eid,
            "homogeneous_pole_factor_count": len(factor_data),
            "homogeneous_pole_factor_exponent_sum": sum(exp for _r, _f, exp in factor_data),
            "all_six_source_rees_charts_checked": True,
            "nonconstant_linear_factor_saturation_check_count": source_nonconstant,
            "nonconstant_linear_factor_saturation_pass_count": source_passes,
            "constant_unit_localization_count": source_constant,
            "all_pole_factors_nonzerodivisors_on_all_six_locked_source_rees_charts": source_nonconstant == source_passes,
        })

    all_pass = nonconstant_factor_checks == nonconstant_factor_passes
    all_chart_poles = all(row["full_pole_equation_is_nonzerodivisor_as_product_of_nonzerodivisors"] for row in chart_rows)
    if len(chart_rows) != 4 * 6 or full_pole_equation_chart_count != 24:
        raise SystemExit("expected four sources times six Rees charts")
    if not all_pass or not all_chart_poles:
        raise SystemExit(
            f"pole-factor Cartier legitimacy failed: {nonconstant_factor_passes}/{nonconstant_factor_checks} factor saturations"
        )

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5e.pole_factor_cartier_legitimacy.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5E_POLE_FACTOR_CARTIER_LEGITIMACY",
        "role": "EXACT_NONCREDIT_POLE_ONLY_LINEAR_FACTOR_SATURATION_PROOF_FOR_THE_E4_DENOMINATOR_CARTIER_EQUATIONS_ON_ALL_24_LOCKED_SOURCE_REES_CHARTS_SUPPORTING_THE_E5D_144_PIECE_CONSTANT_GM_ACTION_UNITS",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e4_sha256": E4_SHA,
            "c4b1e5a_sha256": E5A_SHA,
            "c4b1e5d_sha256": E5D_SHA,
            "r5b2c1_sha256": C1_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "pole_cartier_legitimacy": {
            "source_count": len(source_rows),
            "source_rees_chart_check_count": len(chart_rows),
            "nonconstant_linear_factor_saturation_check_count": nonconstant_factor_checks,
            "nonconstant_linear_factor_saturation_pass_count": nonconstant_factor_passes,
            "nonzero_constant_unit_localization_count": constant_unit_localizations,
            "all_nonconstant_linear_pole_factors_are_nonzerodivisors_modulo_locked_c1_strict_transform_ideals": all_pass,
            "all_24_localized_e4_pole_equations_are_nonzerodivisors": all_chart_poles,
            "source_rows": source_rows,
            "chart_rows": chart_rows,
            "factor_rows": factor_rows,
        },
        "exact_consequence": {
            "timed_out_e5_zero_side_and_nonlinear_support_not_replayed": True,
            "all_e4_pole_factors_are_linear_over_Qi": True,
            "all_e4_pole_principal_equations_are_legitimate_cartier_nonzerodivisors_on_all_six_locked_rees_charts_at_each_of_the_four_sources": True,
            "cartier_legitimacy_persists_on_all_144_attached_d2_exceptional_refinement_pieces_by_localization": True,
            "e5d_constant_gm_coefficients_are_genuine_exceptional_block_pole_line_action_units": True,
            "exceptional_block_line_bundle_action_unit_materialized": True,
            "whole_1757_cover_line_bundle_gm_1_cocycle_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "the denominator side needed by E5D is Cartier on all six locked source Rees charts for each of EXC_003, EXC_004, EXC_011, EXC_012; therefore the 144 constant coefficients are genuine regular invertible action coefficients between localized pole principal ideals on the attached exceptional common-refinement blocks",
            "what_is_still_missing": "this certifies only the four exceptional action blocks. A cover-wide line-bundle Gm action cocycle still requires the same-representative action data on the remaining common-refinement pieces and compatibility on their overlaps before any square-root or H2-fixedness test",
            "pole_only_cartier_legitimacy_does_not_claim_zero_divisor_support_inventory_complete": True,
            "exceptional_block_action_units_are_not_yet_the_whole_1757_cover_ell_ij": True,
        },
        "next_exact_step": "source-bind the same A2_02 representative on the 29 smooth common-refinement pieces and the exceptional blocks outside the four corrected sources, then compare its action transitions with these 144 genuine exceptional-block units to materialize or refute a cover-wide Gm 1-cocycle before attempting square roots",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
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
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5E certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
