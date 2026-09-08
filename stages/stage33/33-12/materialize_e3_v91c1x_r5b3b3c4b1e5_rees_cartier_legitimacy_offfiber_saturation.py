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
C1 = HERE / "e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json"
EXC = HERE.parent / "33-07" / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5-rees-cartier-legitimacy-offfiber-saturation.json"

E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
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
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def clean(x):
    return sp.cancel(sp.expand(x))


def ideals_equal(gens_a: list[sp.Expr], gens_b: list[sp.Expr], variables: list[sp.Symbol]) -> bool:
    GA = sp.groebner(gens_a, *variables, order="grevlex", extension=I)
    GB = sp.groebner(gens_b, *variables, order="grevlex", extension=I)
    return (
        all(clean(GB.reduce(sp.expand(f))[1]) == 0 for f in gens_a)
        and all(clean(GA.reduce(sp.expand(f))[1]) == 0 for f in gens_b)
    )


def saturation_by_function(gens: list[sp.Expr], f: sp.Expr, variables: list[sp.Symbol], tag: str) -> list[sp.Expr]:
    y = sp.Symbol(f"sat_{tag}")
    G = sp.groebner(list(gens) + [1 - y * f], y, *variables, order="lex", extension=I)
    elim = [g.as_expr() for g in G.polys if not g.as_expr().has(y)]
    if not elim:
        raise SystemExit(f"empty saturation elimination basis: {tag}")
    return [clean(x) for x in elim]


def localization_zero_locus_nonempty(gens: list[sp.Expr], f: sp.Expr, e: sp.Symbol, variables: list[sp.Symbol], tag: str) -> bool:
    y = sp.Symbol(f"loc_{tag}")
    G = sp.groebner(list(gens) + [f, 1 - y * e], y, *variables, order="grevlex", extension=I)
    rem = G.reduce(sp.Integer(1))[1]
    return clean(rem) != 0


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
    return e, u, strict


def build_certificate() -> dict:
    e4 = load_locked(E4, E4_SHA)
    c1cert = load_locked(C1, C1_SHA)
    exc = load_locked(EXC, EXC_SHA)

    c1_rows = {row["exceptional_id"]: row for row in c1cert["node_rows"]}
    points = {
        row["exceptional_id"]: sp.Matrix([c1.decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
        for row in exc["exceptional_models"]
    }
    chart_source = {
        (row["source_exceptional_id"], int(row["source_rees_chart_index_0based"])): row
        for row in e4["local_cartier_chart_equations"]["rows"]
    }
    if len(chart_source) != e4["local_cartier_chart_equations"]["row_count"]:
        raise SystemExit("duplicate E4 chart rows")

    rows = []
    nonzerodivisor_pass = 0
    off_fiber_nonempty = 0
    equation_checks = 0

    z = list(sp.symbols("z0:5"))
    for (eid, cp), erow in sorted(chart_source.items()):
        e, u, strict = reconstruct_locked_chart(eid, points[eid], cp, c1_rows[eid])
        variables = [e, *u]
        sub_z = {z[j]: u[j] for j in range(5)}
        for kind, field in (
            ("zero", "local_zero_cartier_equation_Qi"),
            ("pole", "local_pole_cartier_equation_Qi"),
        ):
            Pz = atlas.decode_poly(erow[field], z)
            P = clean(Pz.subs(sub_z, simultaneous=True))
            if P == 0:
                raise SystemExit(f"E4 local {kind} equation became zero {eid}/D{cp}")
            GI = sp.groebner(strict, *variables, order="grevlex", extension=I)
            remainder = clean(GI.reduce(sp.expand(P))[1])
            if remainder == 0:
                equation_zero_in_surface = True
                sat_equal = False
                off_nonempty = False
            else:
                equation_zero_in_surface = False
                sat = saturation_by_function(strict, P, variables, f"{eid}_{cp}_{kind}")
                sat_equal = ideals_equal(strict, sat, variables)
                if sat_equal:
                    nonzerodivisor_pass += 1
                off_nonempty = localization_zero_locus_nonempty(
                    strict, P, e, variables, f"{eid}_{cp}_{kind}"
                )
                if off_nonempty:
                    off_fiber_nonempty += 1
            equation_checks += 1
            rows.append({
                "source_exceptional_id": eid,
                "source_rees_chart_index_0based": cp,
                "equation_kind": kind,
                "c1_strict_chart_commitment_replayed_exact": True,
                "equation_zero_in_strict_transform_coordinate_ring": equation_zero_in_surface,
                "saturation_of_strict_ideal_by_equation_equals_strict_ideal": sat_equal,
                "equation_is_nonzerodivisor_modulo_strict_ideal_by_saturation_test": sat_equal,
                "zero_locus_meets_e_nonzero_blowdown_region": off_nonempty,
                "off_exceptional_height_one_support_requires_inventory": off_nonempty,
            })

    all_nzd = nonzerodivisor_pass == equation_checks
    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5.rees_cartier_legitimacy_offfiber_saturation.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5_REES_CARTIER_LEGITIMACY_AND_OFFFIBER_SATURATION",
        "role": "EXACT_NONCREDIT_SATURATION_REPLAY_OF_E4_LOCAL_GAUGE_EQUATIONS_AGAINST_THE_SOURCE_BOUND_C1_STRICT_TRANSFORM_IDEALS",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e4_rees_cartier_rational_gauge_lift_sha256": E4_SHA,
            "r5b2c1_all_48_node_rees_neighborhoods_sha256": C1_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "saturation_audit": {
            "local_equation_check_count": equation_checks,
            "nonzerodivisor_saturation_pass_count": nonzerodivisor_pass,
            "all_e4_local_zero_and_pole_equations_are_nonzerodivisors_modulo_the_locked_strict_transform_ideals": all_nzd,
            "off_exceptional_nonempty_zero_locus_check_count": off_fiber_nonempty,
            "rows": rows,
        },
        "exact_consequence": {
            "e4_cartier_wording_legitimate_on_the_checked_source_rees_charts": all_nzd,
            "e4_local_equations_replayed_against_exact_c1_strict_transform_chart_commitments": True,
            "off_exceptional_support_is_present_for_at_least_one_e4_local_zero_or_pole_equation": off_fiber_nonempty > 0,
            "off_exceptional_height_one_support_inventory_complete": False,
            "same_representative_full_surface_gauge_correction_verified": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "if_all_nonzerodivisor_tests_pass": "E4's local zero/pole equations are legitimate local effective-Cartier equations on the locked strict-transform charts in the exact saturation sense; this still does not show the chosen q extension is harmless away from the exceptional fiber",
            "if_offfiber_support_is_nonempty": "the deterministic E4 rational extension creates genuine support in the e!=0 blowdown region, so the next leaf must identify those height-one carriers and recompute their residue contribution instead of treating the exceptional Hilbert90 gauge as a full-surface correction",
        },
        "next_exact_step": "factor and source-bind the off-exceptional E4 zero/pole support against the B3B2 finite linear carrier inventory and any residual nonlinear factors, then compute the induced tame-residue change on every resulting height-one prime",
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
        raise SystemExit("materialized C4B1E5 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
