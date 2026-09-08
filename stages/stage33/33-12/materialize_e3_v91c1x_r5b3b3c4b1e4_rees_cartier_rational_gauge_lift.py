#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d

HERE = Path(__file__).resolve().parent
E2 = HERE / "e3-v91c1x-r5b3b3c4b1e2-hilbert90-swap23-residue-gauge.json"
E3 = HERE / "e3-v91c1x-r5b3b3c4b1e3-hilbert90-divisor-rees-attachment.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"

E2_SHA = "65793b939058c8ebe28cd5829d12c1c3d00bfbc0ca21bfd830513f990a767b9b"
E3_SHA = "cad7a3493b3215a1988058a26ddf00d3da45109212caa19df9f439d9cb5143ea"
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
    return atlas.clean(x)


def affine_tangent_matrix(meta: dict, model: dict) -> sp.Matrix:
    cols = []
    for j in range(3):
        tangent = model["U"][:, j]
        p = meta["point"]
        pivot = int(meta["pivot"])
        pp = clean(p[pivot])
        cols.append(sp.Matrix([
            clean((tangent[k] * pp - p[k] * tangent[pivot]) / (pp * pp))
            for k in meta["nonpivot"]
        ]))
    K = sp.Matrix.hstack(*cols)
    if K.rank() != 3:
        raise SystemExit(f"affine tangent map lost rank at {meta['exceptional_id']}")
    return K


def deterministic_lift_row(K: sp.Matrix, f: sp.Matrix) -> tuple[list[int], sp.Matrix]:
    for rows in itertools.combinations(range(K.rows), 3):
        M = K[list(rows), :]
        if clean(M.det()) == 0:
            continue
        coeff_small = M.T.inv() * f
        coeff = sp.zeros(K.rows, 1)
        for r, value in zip(rows, list(coeff_small)):
            coeff[r] = clean(value)
        if any(clean(x) != 0 for x in K.T * coeff - f):
            raise SystemExit("deterministic tangent projection lift failed")
        return list(rows), coeff
    raise SystemExit("no invertible affine tangent row triple")


def decode_rational(enc: dict, t: sp.Symbol) -> sp.Expr:
    num = atlas.decode_poly(enc["numerator"], [t])
    den = atlas.decode_poly(enc["denominator"], [t])
    if clean(den) == 0:
        raise SystemExit("zero denominator")
    return clean(num / den)


def homogenize_to_degree(poly: sp.Expr, t: sp.Symbol, A: sp.Expr, B: sp.Expr, degree: int) -> sp.Expr:
    P = sp.Poly(sp.expand(poly), t, extension=I)
    if int(P.degree()) > degree:
        raise SystemExit("requested homogeneous degree too small")
    out = sp.Integer(0)
    for mon, coeff in P.terms():
        k = int(mon[0])
        out += sp.sympify(coeff) * A ** k * B ** (degree - k)
    return clean(out)


def encode_rational(expr: sp.Expr, variables: list[sp.Symbol]) -> dict:
    num, den = sp.fraction(sp.cancel(expr))
    return {
        "numerator": atlas.encode_poly(sp.expand(num), variables),
        "denominator": atlas.encode_poly(sp.expand(den), variables),
    }


def decode_poly_vector(rows: list[dict], variables: list[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([atlas.decode_poly(x, variables) for x in rows])


def chart_localize(poly_h: sp.Expr, H: list[sp.Symbol], cp: int) -> tuple[list[sp.Symbol], sp.Expr, dict[int, sp.Symbol]]:
    z = sp.symbols(f"z0:{len(H)-1}")
    sub = {H[cp]: sp.Integer(1)}
    index_to_local = {}
    k = 0
    for j in range(len(H)):
        if j == cp:
            continue
        sub[H[j]] = z[k]
        index_to_local[j] = z[k]
        k += 1
    return list(z), clean(poly_h.subs(sub, simultaneous=True)), index_to_local


def build_certificate() -> dict:
    e2 = load_locked(E2, E2_SHA)
    e3 = load_locked(E3, E3_SHA)
    exc = c4b1d.load_locked(c4b1d.EXC, c4b1d.EXC_SHA)

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    e2_rows = {row["source_exceptional_id"]: row for row in e2["hilbert90_gauge"]["rows"]}
    e3_embed = {row["source_exceptional_id"]: row for row in e3["p1_to_rees_embedding"]["rows"]}
    expected = list(c4b1d.TARGETS)
    if set(e2_rows) != set(expected) or set(e3_embed) != set(expected):
        raise SystemExit("E2/E3 exceptional source inventory moved")

    H = list(sp.symbols("H0:6"))
    t, u, w = sp.symbols("t u w")
    gauge_rows = []
    chart_rows = []
    overlap_rows = []

    for eid in expected:
        er = er_by_eid[eid]
        model = c4b1d.c4b1m.reconstruct_exceptional_model(er)
        meta = atlas.node_meta(er)
        K = affine_tangent_matrix(meta, model)
        f0, f1 = c4b1d.reconstruct_projection_forms(er, model)
        rows0, alpha = deterministic_lift_row(K, f0)
        rows1, beta = deterministic_lift_row(K, f1)
        A = clean(sum(alpha[j] * H[j] for j in range(6)))
        B = clean(sum(beta[j] * H[j] for j in range(6)))

        emb = e3_embed[eid]
        hvec = decode_poly_vector(emb["source_rees_homogeneous_vector_Qi_u_w"], [u, w])
        Ah = clean(A.subs({H[j]: hvec[j] for j in range(6)}, simultaneous=True))
        Bh = clean(B.subs({H[j]: hvec[j] for j in range(6)}, simultaneous=True))
        if clean(w * Ah - u * Bh) != 0:
            raise SystemExit(f"projection ratio failed on E3 P1 embedding for {eid}")
        if Ah == 0 or Bh == 0:
            raise SystemExit(f"degenerate lifted P1 projection for {eid}")

        qenc = e2_rows[eid]["q_source_rational_Qi_t"]
        q_num_t = atlas.decode_poly(qenc["numerator"], [t])
        q_den_t = atlas.decode_poly(qenc["denominator"], [t])
        deg_num = int(sp.Poly(sp.expand(q_num_t), t, extension=I).degree())
        deg_den = int(sp.Poly(sp.expand(q_den_t), t, extension=I).degree())
        degree = max(deg_num, deg_den)
        N = homogenize_to_degree(q_num_t, t, A, B, degree)
        D = homogenize_to_degree(q_den_t, t, A, B, degree)
        if N == 0 or D == 0:
            raise SystemExit(f"zero homogeneous q lift at {eid}")

        subs_h = {H[j]: hvec[j] for j in range(6)}
        q_on_p1 = clean(N.subs(subs_h, simultaneous=True) / D.subs(subs_h, simultaneous=True))
        q_expected = decode_rational(qenc, t).subs({t: u / w}, simultaneous=True)
        if clean(q_on_p1 - q_expected) != 0:
            raise SystemExit(f"homogeneous Rees q lift misses E2 function-field gauge at {eid}")

        active = [int(x) for x in emb["active_source_rees_chart_indices_0based"]]
        if len(active) < 2:
            raise SystemExit(f"insufficient active source Rees charts at {eid}")

        gauge_rows.append({
            "source_exceptional_id": eid,
            "target_exceptional_id": e2_rows[eid]["target_exceptional_id"],
            "projection_u_linear_form_in_rees_H_Qi": atlas.encode_poly(A, H),
            "projection_v_linear_form_in_rees_H_Qi": atlas.encode_poly(B, H),
            "projection_u_deterministic_tangent_row_support_0based": rows0,
            "projection_v_deterministic_tangent_row_support_0based": rows1,
            "homogeneous_q_degree": degree,
            "homogeneous_q_numerator_Qi_H": atlas.encode_poly(N, H),
            "homogeneous_q_denominator_Qi_H": atlas.encode_poly(D, H),
            "homogeneous_q_rational_sha256": csha(encode_rational(clean(N / D), H)),
            "restriction_to_exceptional_p1_equals_e2_q_source_exact": True,
            "active_source_rees_chart_indices_0based": active,
        })

        localized = {}
        for cp in active:
            z, Ncp, idx = chart_localize(N, H, cp)
            _z2, Dcp, _idx2 = chart_localize(D, H, cp)
            if Ncp == 0 or Dcp == 0:
                raise SystemExit(f"localized q equation vanished identically at {eid}/S{cp}")
            localized[cp] = (z, Ncp, Dcp, idx)
            chart_rows.append({
                "source_exceptional_id": eid,
                "source_rees_chart_index_0based": cp,
                "source_rees_chart_id": f"{eid}_GLOBAL_ISOLATING_REES_D{cp}",
                "local_coordinate_names": [str(x) for x in z],
                "local_zero_cartier_equation_Qi": atlas.encode_poly(Ncp, z),
                "local_pole_cartier_equation_Qi": atlas.encode_poly(Dcp, z),
                "local_rational_gauge_Qi": encode_rational(clean(Ncp / Dcp), z),
                "zero_and_pole_equations_are_nonzero_regular_polynomials_on_the_ambient_rees_chart": True,
                "resolved_surface_restriction_cartier_legitimacy_uses_d2_smooth_integral_chart": True,
            })

        for cp, cq in itertools.combinations(active, 2):
            z, _Ncp, _Dcp, idx = localized[cp]
            Hq_in_cp = idx[cq]
            unit = clean(Hq_in_cp ** degree)
            if unit == 0:
                raise SystemExit("zero chart transition unit")
            overlap_rows.append({
                "source_exceptional_id": eid,
                "from_source_rees_chart_index_0based": cp,
                "to_source_rees_chart_index_0based": cq,
                "overlap_condition": f"H{cq}/H{cp} != 0",
                "zero_cartier_equation_transition_unit_in_from_chart_Qi": atlas.encode_poly(unit, z),
                "pole_cartier_equation_transition_unit_in_from_chart_Qi": atlas.encode_poly(unit, z),
                "transition_unit_rule": f"(H{cq}/H{cp})^{degree}",
                "same_transition_unit_for_zero_and_pole_equations": True,
                "rational_q_ratio_transition_is_one_exact_by_equal_homogeneous_degree": True,
                "transition_is_a_regular_gm_unit_on_the_displayed_double_overlap": True,
            })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e4.rees_cartier_rational_gauge_lift.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E4_REES_CARTIER_RATIONAL_HILBERT90_GAUGE_LIFT",
        "role": "EXACT_NONCREDIT_DETERMINISTIC_REES_NEIGHBORHOOD_RATIONAL_LIFT_OF_THE_E2_HILBERT90_GAUGES_WITH_LOCAL_CARTIER_EQUATIONS_AND_CHART_TRANSITION_UNITS",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e2_hilbert90_gauge_sha256": E2_SHA,
            "c4b1e3_divisor_rees_attachment_sha256": E3_SHA,
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
            "r5b2d2_sha256": c4b1d.D2_SHA,
        },
        "rees_rational_gauge_lifts": {
            "row_count": len(gauge_rows),
            "rows": sorted(gauge_rows, key=lambda x: x["source_exceptional_id"]),
        },
        "local_cartier_chart_equations": {
            "row_count": len(chart_rows),
            "rows": sorted(chart_rows, key=lambda x: (x["source_exceptional_id"], x["source_rees_chart_index_0based"])),
        },
        "cartier_double_overlap_transitions": {
            "row_count": len(overlap_rows),
            "rows": sorted(overlap_rows, key=lambda x: (x["source_exceptional_id"], x["from_source_rees_chart_index_0based"], x["to_source_rees_chart_index_0based"])),
        },
        "exact_consequence": {
            "all_four_e2_function_field_gauges_extended_to_deterministic_homogeneous_rational_functions_of_source_rees_directions": True,
            "all_four_rees_rational_lifts_restrict_exactly_to_the_original_e2_q_gauges_on_the_exceptional_p1": True,
            "local_zero_and_pole_cartier_equations_materialized_on_every_active_source_rees_chart": True,
            "zero_and_pole_cartier_equation_double_overlap_transition_units_materialized": True,
            "rational_gauge_is_chart_independent_on_active_rees_double_overlaps": True,
            "off_exceptional_new_height_one_support_inventory_complete": False,
            "same_representative_full_surface_gauge_correction_verified": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "each E2 q gauge has a deterministic rational extension on the active resolved-surface Rees neighborhood, with explicit regular numerator/pole equations on each chart and exact Gm overlap units coming from homogeneous rescaling",
            "what_is_still_missing": "factor/attach the zero and pole equations to actual height-one primes away from the exceptional fiber and recompute the full representative residues there; an arbitrary rational extension that fixes the exceptional residue may create new off-fiber carriers, so it cannot yet be promoted to a full-surface gauge or ell_ij/r_ij data",
            "cartier_transition_units_here_are_for_the_chosen_q_principal_divisor_lift_not_yet_the_full_line_bundle_action_cocycle": True,
        },
        "next_exact_step": "enumerate actual height-one support of the E4 local numerator/denominator equations on the resolved-surface Rees neighborhoods, verify compatibility across overlaps and with the existing strict-transform carrier inventory, then test whether the full-surface representative action difference is killed without creating new uncancelled residues",
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
        raise SystemExit("materialized C4B1E4 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
