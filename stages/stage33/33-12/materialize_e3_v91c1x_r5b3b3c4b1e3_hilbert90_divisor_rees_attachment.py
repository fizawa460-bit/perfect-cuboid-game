#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d
import materialize_e3_v91c1x_r5b3b3c4b1e1_literal_swap23_orbit_difference_cocycle as e1

HERE = Path(__file__).resolve().parent
E2 = HERE / "e3-v91c1x-r5b3b3c4b1e2-hilbert90-swap23-residue-gauge.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e3-hilbert90-divisor-rees-attachment.json"

E2_SHA = "65793b939058c8ebe28cd5829d12c1c3d00bfbc0ca21bfd830513f990a767b9b"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


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


def affine_tangent_h(meta: dict, tangent: sp.Matrix) -> sp.Matrix:
    p = meta["point"]
    pivot = int(meta["pivot"])
    pp = atlas.clean(p[pivot])
    if pp == 0:
        raise SystemExit(f"zero affine pivot for {meta['exceptional_id']}")
    return sp.Matrix([
        atlas.clean((tangent[j] * pp - p[j] * tangent[pivot]) / (pp * pp))
        for j in meta["nonpivot"]
    ])


def acted_affine_tangent_h(source_meta: dict, target_meta: dict, tangent: sp.Matrix) -> sp.Matrix:
    acted_p = atlas.tau_vec(source_meta["point"])
    acted_tangent = atlas.tau_vec(tangent)
    pivot = int(target_meta["pivot"])
    pp = atlas.clean(acted_p[pivot])
    if pp == 0:
        raise SystemExit(
            f"acted target affine pivot vanished for {source_meta['exceptional_id']}->{target_meta['exceptional_id']}"
        )
    return sp.Matrix([
        atlas.clean((acted_tangent[j] * pp - acted_p[j] * acted_tangent[pivot]) / (pp * pp))
        for j in target_meta["nonpivot"]
    ])


def vector_common_gcd(v: sp.Matrix, u: sp.Symbol, w: sp.Symbol) -> sp.Expr:
    g = None
    for x in list(v):
        x = atlas.clean(x)
        if x == 0:
            continue
        p = sp.Poly(sp.expand(x), u, w, extension=I)
        g = p if g is None else sp.gcd(g, p)
    if g is None:
        raise SystemExit("zero Rees homogeneous tangent vector")
    return sp.Poly(g, u, w, extension=I).monic().as_expr()


def remove_common_gcd(v: sp.Matrix, u: sp.Symbol, w: sp.Symbol) -> tuple[sp.Matrix, sp.Expr]:
    g = vector_common_gcd(v, u, w)
    out = sp.Matrix([atlas.clean(x / g) for x in list(v)])
    if vector_common_gcd(out, u, w) != 1:
        raise SystemExit("Rees tangent vector common-gcd removal failed")
    return out, g


def projectively_equal(a: sp.Matrix, b: sp.Matrix) -> bool:
    if len(a) != len(b):
        return False
    if all(atlas.clean(x) == 0 for x in list(a)) or all(atlas.clean(x) == 0 for x in list(b)):
        return False
    for r in range(len(a)):
        for s in range(r + 1, len(a)):
            if atlas.clean(a[r] * b[s] - a[s] * b[r]) != 0:
                return False
    return True


def homogenize_univariate(encoded: dict, t: sp.Symbol, u: sp.Symbol, w: sp.Symbol) -> sp.Expr:
    f = atlas.decode_poly(encoded, [t])
    p = sp.Poly(sp.expand(f), t, extension=I)
    degree = int(p.degree())
    out = sp.Integer(0)
    for mon, coeff in p.terms():
        k = int(mon[0])
        out += sp.sympify(coeff) * u ** k * w ** (degree - k)
    return atlas.clean(out)


def finite_prime_chart_indices(
    hvec: sp.Matrix,
    factor_t: sp.Expr,
    t: sp.Symbol,
    u: sp.Symbol,
    w: sp.Symbol,
) -> list[int]:
    f = sp.Poly(sp.expand(factor_t), t, extension=I)
    out = []
    for idx, h in enumerate(list(hvec)):
        ht = atlas.clean(h.subs({u: t, w: 1}, simultaneous=True))
        if ht == 0:
            continue
        hp = sp.Poly(sp.expand(ht), t, extension=I)
        _q, rem = sp.div(hp, f)
        if not rem.is_zero:
            out.append(idx)
    return out


def infinity_chart_indices(hvec: sp.Matrix, u: sp.Symbol, w: sp.Symbol) -> list[int]:
    return [
        idx
        for idx, h in enumerate(list(hvec))
        if atlas.clean(h.subs({u: 1, w: 0}, simultaneous=True)) != 0
    ]


def encode_poly_vector(v: sp.Matrix, variables: list[sp.Symbol]) -> list[dict]:
    return [atlas.encode_poly(atlas.clean(x), variables) for x in list(v)]


def build_certificate() -> dict:
    e2 = load_locked(E2, E2_SHA)
    exc = c4b1d.load_locked(c4b1d.EXC, c4b1d.EXC_SHA)
    d2 = c4b1d.load_locked(c4b1d.D2, c4b1d.D2_SHA)
    expected_map, _residues, directed_maps = e1.reconstruct_exact_data()

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    models = {
        eid: c4b1d.c4b1m.reconstruct_exceptional_model(er_by_eid[eid])
        for eid in c4b1d.TARGETS
    }
    metas = {eid: atlas.node_meta(er_by_eid[eid]) for eid in c4b1d.TARGETS}
    d2_rows = {
        row["source_node"]: row
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    e2_rows = {
        row["source_exceptional_id"]: row
        for row in e2["hilbert90_gauge"]["rows"]
    }
    if set(e2_rows) != set(c4b1d.TARGETS):
        raise SystemExit("C4B1E2 source set moved")

    u, w, t = sp.symbols("u w t")
    embedding_rows = []
    support_rows = []
    support_piece_incidence_count = 0
    unique_support_keys = set()

    for source in c4b1d.TARGETS:
        target = expected_map[source]
        if d2_rows[source]["acted_target_node"] != target:
            raise SystemExit(f"D2 target moved for {source}")
        source_model = models[source]
        target_model = models[target]
        source_meta = metas[source]
        target_meta = metas[target]

        source_tangent = sp.Matrix([
            atlas.clean(x.subs({source_model["u"]: u, source_model["v"]: w}, simultaneous=True))
            for x in source_model["U"] * source_model["yuv"]
        ])
        h_source_raw = affine_tangent_h(source_meta, source_tangent)
        h_source, source_common = remove_common_gcd(h_source_raw, u, w)

        J0, det = atlas.derivative_matrix(source_meta, target_meta)
        h_target_from_derivative_raw = sp.Matrix([
            atlas.clean(x) for x in J0 * h_source_raw
        ])
        h_target_direct_raw = acted_affine_tangent_h(source_meta, target_meta, source_tangent)
        if any(
            atlas.clean(a - b) != 0
            for a, b in zip(list(h_target_from_derivative_raw), list(h_target_direct_raw))
        ):
            raise SystemExit(f"D2 derivative/acted tangent mismatch for {source}->{target}")
        h_target, target_common = remove_common_gcd(h_target_direct_raw, u, w)

        maprow = directed_maps[(source, target)]
        M = maprow["_matrix"]
        tu = atlas.clean(M[0, 0] * u + M[0, 1] * w)
        tv = atlas.clean(M[1, 0] * u + M[1, 1] * w)
        target_tangent_model = sp.Matrix([
            atlas.clean(
                x.subs(
                    {target_model["u"]: tu, target_model["v"]: tv},
                    simultaneous=True,
                )
            )
            for x in target_model["U"] * target_model["yuv"]
        ])
        h_target_model_raw = affine_tangent_h(target_meta, target_tangent_model)
        if not projectively_equal(h_target_direct_raw, h_target_model_raw):
            raise SystemExit(f"C4B1D P1/D2 Rees tangent map mismatch for {source}->{target}")

        active_source = [idx for idx, x in enumerate(list(h_source)) if atlas.clean(x) != 0]
        active_target = [idx for idx, x in enumerate(list(h_target)) if atlas.clean(x) != 0]
        if not active_source or not active_target:
            raise SystemExit(f"empty induced Rees chart cover for {source}->{target}")

        embedding_rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "source_p1_parameter": "[u:w]",
            "source_rees_homogeneous_vector_Qi_u_w": encode_poly_vector(h_source, [u, w]),
            "source_rees_homogeneous_vector_sha256": csha(encode_poly_vector(h_source, [u, w])),
            "source_removed_common_factor_Qi_u_w": atlas.encode_poly(source_common, [u, w]),
            "acted_target_rees_homogeneous_vector_Qi_u_w": encode_poly_vector(h_target, [u, w]),
            "acted_target_rees_homogeneous_vector_sha256": csha(encode_poly_vector(h_target, [u, w])),
            "acted_target_removed_common_factor_Qi_u_w": atlas.encode_poly(target_common, [u, w]),
            "active_source_rees_chart_indices_0based": active_source,
            "active_target_rees_chart_indices_0based": active_target,
            "d2_tangent_derivative_determinant_Qi": atlas.encode_element(det),
            "d2_derivative_equals_direct_global_swap23_tangent_transport": True,
            "c4b1d_pgl2_target_parametrization_projectively_equals_d2_acted_rees_tangent_transport": True,
            "source_rees_vector_basepoint_free_on_p1_by_common_gcd_one": True,
            "acted_target_rees_vector_basepoint_free_on_p1_by_common_gcd_one": True,
        })

        div = e2_rows[source]["q_source_principal_divisor"]
        for dr in div["finite_rows"]:
            factor_t = atlas.decode_poly(dr["monic_factor_Qi_t"], [t])
            factor_hom = homogenize_univariate(dr["monic_factor_Qi_t"], t, u, w)
            src_charts = finite_prime_chart_indices(h_source, factor_t, t, u, w)
            tgt_charts = finite_prime_chart_indices(h_target, factor_t, t, u, w)
            if not src_charts or not tgt_charts:
                raise SystemExit(
                    f"q divisor prime escaped one side of the D2 induced cover: {source}/{dr['projective_factor_sha256']}"
                )
            pieces = [f"REF_{source}_S{s}_T{r}" for s in src_charts for r in tgt_charts]
            support_piece_incidence_count += len(pieces)
            key = (source, dr["kind"], dr["projective_factor_sha256"], int(dr["order"]))
            unique_support_keys.add(key)
            support_rows.append({
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "support_kind": dr["kind"],
                "support_order": int(dr["order"]),
                "support_degree": int(dr["degree"]),
                "support_projective_factor_sha256": dr["projective_factor_sha256"],
                "homogenized_support_Qi_u_w": atlas.encode_poly(factor_hom, [u, w]),
                "source_rees_chart_indices_covering_generic_support_point_0based": src_charts,
                "acted_target_rees_chart_indices_covering_generic_support_point_0based": tgt_charts,
                "d2_refinement_piece_ids_meeting_generic_support_point": pieces,
                "d2_refinement_piece_incidence_count": len(pieces),
            })

        infinity_order = int(div["infinity_order"])
        if infinity_order:
            src_charts = infinity_chart_indices(h_source, u, w)
            tgt_charts = infinity_chart_indices(h_target, u, w)
            if not src_charts or not tgt_charts:
                raise SystemExit(f"q infinity divisor escaped D2 induced cover for {source}")
            pieces = [f"REF_{source}_S{s}_T{r}" for s in src_charts for r in tgt_charts]
            support_piece_incidence_count += len(pieces)
            unique_support_keys.add((source, "infinity", "INFINITY", infinity_order))
            support_rows.append({
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "support_kind": "infinity",
                "support_order": infinity_order,
                "support_degree": 1,
                "support_projective_factor_sha256": "INFINITY_V_EQUALS_ZERO",
                "homogenized_support_Qi_u_w": atlas.encode_poly(w, [u, w]),
                "source_rees_chart_indices_covering_generic_support_point_0based": src_charts,
                "acted_target_rees_chart_indices_covering_generic_support_point_0based": tgt_charts,
                "d2_refinement_piece_ids_meeting_generic_support_point": pieces,
                "d2_refinement_piece_incidence_count": len(pieces),
            })

    if len(embedding_rows) != 4:
        raise SystemExit("expected four P1/Rees embedding rows")
    if not support_rows:
        raise SystemExit("Hilbert90 gauge divisor support unexpectedly empty")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e3.hilbert90_divisor_rees_attachment.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E3_HILBERT90_GAUGE_DIVISOR_TO_D2_REES_ATTACHMENT",
        "role": "EXACT_NONCREDIT_ATTACHMENT_OF_THE_EXPLICIT_HILBERT90_GAUGE_PRINCIPAL_DIVISORS_TO_THE_SOURCE_BOUND_D2_EXCEPTIONAL_REES_COMMON_REFINEMENT",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e2_hilbert90_gauge_sha256": E2_SHA,
            "r5b2d2_sha256": c4b1d.D2_SHA,
            "c4b1d_sha256": "0b63663ce9e4eda381e7665dbf7722969898ebf931806b5eec3687579882c11e",
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
        },
        "p1_to_rees_embedding": {
            "row_count": len(embedding_rows),
            "rows": sorted(embedding_rows, key=lambda row: row["source_exceptional_id"]),
        },
        "q_divisor_rees_attachment": {
            "directed_support_row_count": len(support_rows),
            "directed_support_key_count": len(unique_support_keys),
            "total_d2_piece_incidence_count_with_multiplicity": support_piece_incidence_count,
            "rows": sorted(
                support_rows,
                key=lambda row: (
                    row["source_exceptional_id"],
                    row["support_kind"],
                    row["support_projective_factor_sha256"],
                ),
            ),
        },
        "exact_consequence": {
            "all_four_exceptional_p1s_embedded_explicitly_into_their_six_source_rees_homogeneous_coordinates": True,
            "all_four_swap23_p1_maps_verified_compatible_with_the_d2_rees_tangent_derivative": True,
            "all_hilbert90_q_principal_divisor_support_rows_attached_to_nonempty_d2_refinement_piece_incidence": True,
            "q_divisor_support_attached_to_the_1757_rees_cover": True,
            "literal_local_cartier_equations_extending_each_support_off_the_exceptional_p1_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "the nonconstant q=1+d Hilbert90 gauges have explicit principal-divisor support on the four exceptional P1 function fields, and every such support prime is attached to concrete source/acted-target D2 Rees refinement pieces through an exact P1-to-Rees tangent embedding",
            "what_is_still_missing": "lift each exceptional support equation from the P1 fiber to a local Cartier equation in the resolved-surface Rees neighborhood, compare those equations on overlaps to obtain actual Gm transition units, then solve/test the required square-root cochain and triple-overlap identity",
            "fiber_divisor_attachment_is_not_yet_a_resolved_surface_cartier_divisor": True,
            "rees_piece_incidence_is_not_itself_a_cech_transition_function": True,
        },
        "next_exact_step": "for each attached q divisor prime choose a deterministic covering Rees chart, lift the homogenized P1 support equation to a local Cartier equation in that Rees neighborhood, and materialize overlap ratios as candidate ell_ij transition units before attempting r_ij square roots",
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
        raise SystemExit("materialized C4B1E3 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
