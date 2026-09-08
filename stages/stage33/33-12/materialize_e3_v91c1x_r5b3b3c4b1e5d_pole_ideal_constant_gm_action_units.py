#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d
import materialize_e3_v91c1x_r5b3b3c4b1e5b_rees_gauge_cross_action_divisor_transport as e5b

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
E4 = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"
E5B = HERE / "e3-v91c1x-r5b3b3c4b1e5b-rees-gauge-cross-action-divisor-transport.json"
E5C = HERE / "e3-v91c1x-r5b3b3c4b1e5c-rees-gauge-hilbert90-transition-match.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5d-pole-ideal-constant-gm-action-units.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
E5B_SHA = "5d60f94503a863800d4ca67265728a9e3b55cdd9d8d08f5203b8734316a9616d"
E5C_SHA = "5da47187cc8a6a054ac70f18d533cb190921aa5fc41a52c9b85477ab94894a4f"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
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


def encode_rational(expr: sp.Expr, variables: list[sp.Symbol]) -> dict:
    num, den = sp.fraction(sp.cancel(expr))
    return {
        "numerator": atlas.encode_poly(sp.expand(num), variables),
        "denominator": atlas.encode_poly(sp.expand(den), variables),
    }


def scalar_projective_match(a: sp.Expr, b: sp.Expr, X: list[sp.Symbol]) -> sp.Expr:
    sa, pa = atlas.projective_poly_signature(a, X)
    sb, pb = atlas.projective_poly_signature(b, X)
    if sa != sb:
        raise SystemExit("expected projectively equal zero equations")
    scalar = clean(pa / pb)
    if clean(a - scalar * b) != 0:
        raise SystemExit("projective scalar reconstruction failed")
    if scalar == 0:
        raise SystemExit("zero projective matching scalar")
    return scalar


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    e4 = load_locked(E4, E4_SHA)
    e5b_cert = load_locked(E5B, E5B_SHA)
    e5c = load_locked(E5C, E5C_SHA)
    exc = c4b1d.load_locked(c4b1d.EXC, c4b1d.EXC_SHA)

    targets = list(c4b1d.TARGETS)
    e4_rows = {
        row["source_exceptional_id"]: row
        for row in e4["rees_rational_gauge_lifts"]["rows"]
    }
    c_rows = {
        row["source_exceptional_id"]: row
        for row in e5c["transition_match"]["rows"]
    }
    d2_rows = {
        row["source_node"]: row
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    metas = {eid: atlas.node_meta(er_by_eid[eid]) for eid in targets}
    if not (set(e4_rows) == set(c_rows) == set(targets)):
        raise SystemExit("E4/E5C target inventory mismatch")

    zero_transport = {
        row["source_exceptional_id"]: bool(row["total_zero_or_pole_divisor_equation_transports_projectively_exact"])
        for row in e5b_cert["whole_zero_pole_divisor_transport"]["rows"]
        if row["equation_kind"] == "zero"
    }
    if set(zero_transport) != set(targets) or not all(zero_transport.values()):
        raise SystemExit("E5B zero transport is no longer exact on all four directions")

    X = list(sp.symbols("a1 a2 a3 b1 b2 b3 c"))
    H = list(sp.symbols("H0:6"))

    ambient = {}
    for source in targets:
        row = e4_rows[source]
        N = atlas.decode_poly(row["homogeneous_q_numerator_Qi_H"], H)
        D = atlas.decode_poly(row["homogeneous_q_denominator_Qi_H"], H)
        Namb = e5b.ambient_lift_from_rees_direction(N, metas[source], H, X)
        Damb = e5b.ambient_lift_from_rees_direction(D, metas[source], H, X)
        ambient[source] = (Namb, Damb)

    directed_rows = []
    piece_rows = []
    scalar_by_source = {}
    total_piece_count = 0

    for source in targets:
        target = c_rows[source]["target_exceptional_id"]
        if d2_rows[source]["acted_target_node"] != target:
            raise SystemExit(f"D2 target moved for {source}")
        if d2_rows[source]["common_refinement_piece_count"] != 36:
            raise SystemExit(f"D2 piece count moved for {source}")

        Ns, Ds = ambient[source]
        Nt, Dt = ambient[target]
        Nt_pull = e5b.pullback_tau(Nt, X)
        Dt_pull = e5b.pullback_tau(Dt, X)
        zero_scalar = scalar_projective_match(Ns, Nt_pull, X)
        scalar_by_source[source] = zero_scalar

        Qs = clean(Ns / Ds)
        Qt_pull = clean(Nt_pull / Dt_pull)
        m = clean(Qs / Qt_pull)
        local_action_unit = clean(m * Ds / Dt_pull)
        if clean(local_action_unit - zero_scalar) != 0:
            raise SystemExit(f"pole-ideal action coefficient failed to collapse to zero scalar at {source}")
        if local_action_unit.free_symbols:
            raise SystemExit(f"pole-ideal action coefficient is not constant at {source}")

        piece_ids = [
            f"REF_{source}_S{cs}_T{ct}"
            for cs in range(6)
            for ct in range(6)
        ]
        total_piece_count += len(piece_ids)
        directed_rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "zero_equation_projective_matching_scalar_Qi": atlas.encode_element(zero_scalar),
            "identity": "m_source * D_source / swap23^*(D_target) = zero_matching_scalar",
            "identity_verified_as_global_rational_function": True,
            "coefficient_is_nonzero_constant_Qi_gm_unit": True,
            "d2_piece_count": len(piece_ids),
            "d2_36_piece_descriptors_sha256": d2_rows[source]["36_piece_descriptors_sha256"],
            "constant_unit_restricts_to_every_d2_piece": True,
        })
        for pid in piece_ids:
            piece_rows.append({
                "piece_id": pid,
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "constant_action_unit_Qi": atlas.encode_element(zero_scalar),
                "unit_is_regular_and_invertible_on_piece_because_it_is_nonzero_constant": True,
                "unit_represents_the_coefficient_of_m_between_the_two_displayed_pole_principal_equations": True,
            })

    involution_rows = []
    seen = set()
    for source in targets:
        target = c_rows[source]["target_exceptional_id"]
        orbit = tuple(sorted((source, target)))
        if orbit in seen:
            continue
        seen.add(orbit)
        product = clean(scalar_by_source[source] * scalar_by_source[target])
        if clean(product - 1) != 0:
            raise SystemExit(f"constant Gm action units fail involution on orbit {orbit}")
        involution_rows.append({
            "orbit_members": list(orbit),
            "forward_unit_Qi": atlas.encode_element(scalar_by_source[source]),
            "reverse_unit_Qi": atlas.encode_element(scalar_by_source[target]),
            "forward_times_reverse_equals_one_exact": True,
        })

    if total_piece_count != 4 * 36:
        raise SystemExit("four exceptional D2 block piece count moved")
    if len(involution_rows) != 2:
        raise SystemExit("expected two two-point swap23 orbits")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5d.pole_ideal_constant_gm_action_units.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5D_POLE_PRINCIPAL_IDEAL_CONSTANT_GM_ACTION_UNITS",
        "role": "EXACT_NONCREDIT_EXTRACTION_OF_NONZERO_CONSTANT_GM_COEFFICIENTS_FOR_THE_E5C_RATIONAL_TRANSITION_BETWEEN_SOURCE_AND_SWAP23_PULLED_POLE_PRINCIPAL_EQUATIONS_ON_ALL_144_ATTACHED_D2_EXCEPTIONAL_REFINEMENT_PIECES",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_sha256": D2_SHA,
            "c4b1e4_sha256": E4_SHA,
            "c4b1e5b_sha256": E5B_SHA,
            "c4b1e5c_sha256": E5C_SHA,
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
        },
        "pole_principal_equation_action": {
            "directed_row_count": len(directed_rows),
            "rows": sorted(directed_rows, key=lambda row: row["source_exceptional_id"]),
            "attached_d2_piece_count": total_piece_count,
            "piece_rows": sorted(piece_rows, key=lambda row: row["piece_id"]),
        },
        "swap23_involution": {
            "orbit_count": len(involution_rows),
            "rows": sorted(involution_rows, key=lambda row: row["orbit_members"]),
        },
        "exact_consequence": {
            "all_four_rational_hilbert90_transitions_act_between_the_displayed_pole_principal_equations_with_nonzero_constant_Qi_coefficients": True,
            "constant_gm_action_coefficients_materialized_on_all_144_attached_exceptional_d2_pieces": True,
            "both_two_point_orbits_satisfy_forward_reverse_gm_unit_product_one": True,
            "piecewise_regular_gm_unit_candidate_for_pole_principal_ideal_action_materialized": True,
            "pole_principal_equations_verified_cartier_nonzerodivisors_on_all_resolved_surface_charts": False,
            "whole_1757_cover_line_bundle_gm_1_cocycle_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "after expressing the E5C rational transition relative to the source and swap23-pulled pole equations, the coefficient is a nonzero Q(i) constant on every one of the 144 attached exceptional D2 pieces and the two orbitwise forward/reverse products are 1",
            "what_is_still_missing": "certify that the displayed pole equations define legitimate Cartier principal ideals on the resolved-surface charts (the heavy all-zero/pole E5 saturation timed out), extend/compare this action data with the remaining 1757-cover charts needed by the same representative, and only then identify a genuine cover-wide ell_ij and test square roots",
            "constant_unit_between_ambient_principal_equations_is_not_by_itself_full_line_bundle_glue": True,
        },
        "next_exact_step": "replace the timed-out 24-equation E5 saturation by a pole-only orbit-reduced Cartier legitimacy check for the finitely many linear pole factors from E5A; if that passes, promote the 144 constant coefficients to genuine exceptional-block line-bundle action units before adjoining the smooth-cover data",
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
        raise SystemExit("materialized C4B1E5D certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
