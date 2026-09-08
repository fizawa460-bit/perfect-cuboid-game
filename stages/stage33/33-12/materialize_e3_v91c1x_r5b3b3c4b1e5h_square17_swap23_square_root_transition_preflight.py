#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1_exceptional_p1_targeted_residue_field_squareclass as c4b1m
import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C4B1 = HERE / "e3-v91c1x-r5b3b3c4b1-exceptional-p1-targeted-residue-field-squareclass.json"
E5F = HERE / "e3-v91c1x-r5b3b3c4b1e5f-whole-cover-action-transport-debt-partition.json"
E5G = HERE / "e3-v91c1x-r5b3b3c4b1e5g-smooth29-pole-line-action-unit-attachment.json"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5h-square17-swap23-square-root-transition-preflight.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C4B1_SHA = "f14d9ca73ad0f0cbcf052c4512603bcc0942fb9263f97535023e8050ffcdced4"
E5F_SHA = "fa982518e59950b4b6e39b7cfa9f454f585c932d61514af23fbd252674ea72cc"
E5G_SHA = "be6641c291e7a07d00d085c72e9deeed48a7ca88c16dd2035adf121849b2f017"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


def clean(x: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(x))


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


def rational_sqrt_if_square(q: sp.Expr) -> sp.Expr | None:
    q = sp.Rational(q)
    if q < 0:
        return None
    n, d = int(sp.numer(q)), int(sp.denom(q))
    sn, sd = int(sp.sqrt(n)), int(sp.sqrt(d))
    if sn * sn != n or sd * sd != d:
        return None
    return sp.Rational(sn, sd)


def qi_square_root(z: sp.Expr) -> sp.Expr | None:
    z = clean(z)
    if z == 0:
        return sp.Integer(0)
    zc = clean(sp.conjugate(z))
    a = clean((z + zc) / 2)
    b = clean((z - zc) / (2 * I))
    if a.is_Rational is not True or b.is_Rational is not True:
        raise SystemExit(f"square-root coefficient escaped Q(i): {z}")
    norm = clean(a * a + b * b)
    r = rational_sqrt_if_square(norm)
    if r is None:
        return None
    x2 = clean((r + a) / 2)
    y2 = clean((r - a) / 2)
    sx = rational_sqrt_if_square(x2)
    sy = rational_sqrt_if_square(y2)
    if sx is None or sy is None:
        return None
    for x in (sx, -sx):
        for y in (sy, -sy):
            root = clean(x + I * y)
            if clean(root * root - z) == 0:
                return root
    return None


def exact_poly_square_root(expr: sp.Expr, t: sp.Symbol) -> sp.Expr:
    expr = clean(expr)
    P = sp.Poly(sp.expand(expr), t, extension=I)
    if P.is_zero:
        raise SystemExit("zero squareclass representative is invalid")
    coeff, facs = sp.factor_list(P.as_expr(), t, extension=I)
    root_coeff = qi_square_root(coeff)
    if root_coeff is None:
        raise SystemExit(f"square representative coefficient has no Q(i) root: {coeff}")
    root = root_coeff
    for fac, exponent in facs:
        if exponent % 2:
            raise SystemExit(f"square representative retained odd factor exponent {exponent}: {fac}")
        root = clean(root * fac ** (exponent // 2))
    if clean(root * root - expr) != 0:
        raise SystemExit("exact polynomial square root reconstruction failed")
    return root


def canonical_residue_expr(
    eid: str,
    model: dict,
    coeffs: dict[str, sp.Matrix],
    c4a_by_eid: dict[str, dict],
    c4b1_by_eid: dict[str, dict],
) -> tuple[sp.Expr, str]:
    odd_ids = list(c4a_by_eid[eid]["combined_tame_residue_odd_linear_carrier_ids"])
    if not odd_ids:
        row = c4b1_by_eid[eid]
        if row["classification"] != "SQUARE_TRIVIAL_BY_C4A_ZERO_FORMAL_LINEAR_FACTOR_PARITY":
            raise SystemExit(f"zero odd-support row classification moved: {eid}")
        return sp.Integer(1), "CANONICAL_MOD_SQUARE_REPRESENTATIVE_ONE_FROM_ZERO_ODD_CARRIER_PARITY"
    expr = c4b1d.reconstruct_residue_expr(eid, model, coeffs, c4a_by_eid, c4b1_by_eid)
    return expr, "EXACT_C4B1_ODD_CARRIER_REPRESENTATIVE"


def pulled_rational(expr: sp.Expr, M: sp.Matrix, t: sp.Symbol) -> sp.Expr:
    lu = clean(M[0, 0] * t + M[0, 1])
    lv = clean(M[1, 0] * t + M[1, 1])
    if lv == 0:
        raise SystemExit("PGL2 affine denominator vanished identically")
    return clean(expr.subs({t: clean(lu / lv)}, simultaneous=True))


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    c4b1 = load_locked(C4B1, C4B1_SHA)
    e5f = load_locked(E5F, E5F_SHA)
    e5g = load_locked(E5G, E5G_SHA)
    exc = load_locked(EXC, EXC_SHA)

    square_ids = list(e5f["whole_cover_partition"]["exceptional_square_or_trivial_residue_blocks"]["exceptional_ids"])
    if len(square_ids) != 17:
        raise SystemExit("E5F square/trivial block count moved")
    square_set = set(square_ids)
    if e5g["coverage_accounting"]["total_genuine_pole_line_action_unit_piece_count"] != 173:
        raise SystemExit("E5G 173-piece coverage boundary moved")

    d2_rows = {
        row["source_node"]: row
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    if len(d2_rows) != 48:
        raise SystemExit("D2 node action inventory moved")
    node_map = {eid: d2_rows[eid]["acted_target_node"] for eid in d2_rows}
    for eid, target in node_map.items():
        if node_map.get(target) != eid:
            raise SystemExit(f"D2 node action ceased to be involutive at {eid}")

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    c4a_by_eid = {
        row["exceptional_id"]: row
        for row in c4a["exceptional_prime_preflight"]["rows"]
    }
    c4b1_by_eid = {
        row["exceptional_id"]: row
        for row in c4b1["exceptional_squareclass_reduction"]["rows"]
    }
    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    coeffs = {
        row["carrier_id"]: sp.Matrix([atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]])
        for row in inv_rows
    }

    needed_ids = sorted(square_set | {node_map[eid] for eid in square_set})
    models = {eid: c4b1m.reconstruct_exceptional_model(er_by_eid[eid]) for eid in needed_ids}
    t = sp.Symbol("t")

    residue_expr: dict[str, sp.Expr] = {}
    residue_kind: dict[str, str] = {}
    square_roots: dict[str, sp.Expr] = {}
    for eid in needed_ids:
        if eid in square_set:
            expr, kind = canonical_residue_expr(eid, models[eid], coeffs, c4a_by_eid, c4b1_by_eid)
            if not c4b1_by_eid[eid]["square_trivial_in_Qi_exceptional_function_field"]:
                raise SystemExit(f"E5F square source no longer square in C4B1: {eid}")
            root = exact_poly_square_root(expr, t)
            residue_expr[eid] = expr
            residue_kind[eid] = kind
            square_roots[eid] = root
        else:
            expr = c4b1d.reconstruct_residue_expr(eid, models[eid], coeffs, c4a_by_eid, c4b1_by_eid)
            residue_expr[eid] = expr
            residue_kind[eid] = "EXACT_C4B1_NONSQUARE_ODD_CARRIER_REPRESENTATIVE"

    maps: dict[tuple[str, str], dict] = {}
    for source in square_ids:
        target = node_map[source]
        maps[(source, target)] = c4b1d.pgl2_tangent_map(
            er_by_eid[source], models[source], er_by_eid[target], models[target]
        )

    rows = []
    stable_sources = []
    cross_sources = []
    for source in square_ids:
        target = node_map[source]
        M = maps[(source, target)]["_matrix"]
        target_pull = pulled_rational(residue_expr[target], M, t)
        ratio = clean(residue_expr[source] / target_pull)
        ratio_sq = c4b1d.rational_squareclass(ratio, t)
        target_is_square = target in square_set

        base = {
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "source_canonical_representative_kind": residue_kind[source],
            "source_canonical_representative_Qi_t_sha256": csha(atlas.encode_rational(residue_expr[source], [t])),
            "source_square_root_Qi_t": atlas.encode_rational(square_roots[source], [t]),
            "source_square_root_Qi_t_sha256": csha(atlas.encode_rational(square_roots[source], [t])),
            "pgl2_matrix_Qi_projectively_normalized": maps[(source, target)]["pgl2_matrix_Qi_projectively_normalized"],
            "pgl2_matrix_sha256": maps[(source, target)]["pgl2_matrix_sha256"],
            "target_is_in_square_or_trivial_17_set": target_is_square,
            "source_over_pulled_target_squareclass": ratio_sq,
            "d2_piece_count": int(d2_rows[source]["common_refinement_piece_count"]),
            "d2_36_piece_descriptors_sha256": d2_rows[source]["36_piece_descriptors_sha256"],
        }

        if target_is_square:
            root_target_pull = pulled_rational(square_roots[target], M, t)
            transition = clean(square_roots[source] / root_target_pull)
            if clean(transition * transition - ratio) != 0:
                raise SystemExit(f"square-root transition failed to square to residue ratio: {source}->{target}")
            if not ratio_sq["square_trivial"]:
                raise SystemExit(f"square-square source/target ratio became nonsquare: {source}->{target}")
            stable_sources.append(source)
            base.update({
                "classification": "SQUARE17_TARGET_STAYS_IN_SQUARE17_AND_EXPLICIT_SQUARE_ROOT_TRANSITION_EXISTS",
                "target_canonical_representative_kind": residue_kind[target],
                "target_canonical_representative_Qi_t_sha256": csha(atlas.encode_rational(residue_expr[target], [t])),
                "target_square_root_Qi_t_sha256": csha(atlas.encode_rational(square_roots[target], [t])),
                "explicit_square_root_transition_Qi_t": atlas.encode_rational(transition, [t]),
                "explicit_square_root_transition_Qi_t_sha256": csha(atlas.encode_rational(transition, [t])),
                "transition_square_equals_source_over_pulled_target_exact": True,
                "same_representative_function_field_square_root_transition_materialized": True,
                "regular_invertible_on_all_36_d2_pieces_verified": False,
            })
        else:
            if ratio_sq["square_trivial"]:
                raise SystemExit(
                    f"cross-class source unexpectedly has square ratio despite nonsquare target classification: {source}->{target}"
                )
            cross_sources.append(source)
            base.update({
                "classification": "SQUARE17_SOURCE_MAPS_TO_CURRENT_NONSQUARE_TARGET_AND_NO_SQUARE_ROOT_TRANSITION_EXISTS_FOR_CURRENT_CANONICAL_LOCAL_REPRESENTATIVES",
                "target_canonical_representative_kind": residue_kind[target],
                "target_c4b1_classification": c4b1_by_eid[target]["classification"],
                "same_representative_function_field_square_root_transition_materialized": False,
                "obstruction_is_for_current_canonical_local_representatives_not_global_nonexistence": True,
            })
        rows.append(base)

    stable_set = set(stable_sources)
    stable_orbits = []
    seen = set()
    for source in stable_sources:
        target = node_map[source]
        orbit = tuple(sorted((source, target)))
        if orbit in seen:
            continue
        seen.add(orbit)
        if target not in stable_set:
            raise SystemExit(f"stable source set is not orbit-closed: {source}->{target}")
        Mst = maps[(source, target)]["_matrix"]
        if (target, source) not in maps:
            maps[(target, source)] = c4b1d.pgl2_tangent_map(
                er_by_eid[target], models[target], er_by_eid[source], models[source]
            )
        Mts = maps[(target, source)]["_matrix"]
        comp = c4b1d.projective_normalize_matrix(Mts * Mst)
        if comp != sp.eye(2):
            raise SystemExit(f"stable square orbit PGL2 involution failed: {orbit}")
        rs = next(r for r in rows if r["source_exceptional_id"] == source)
        rt = next(r for r in rows if r["source_exceptional_id"] == target)
        ms = atlas.decode_poly(rs["explicit_square_root_transition_Qi_t"]["numerator"], [t]) / atlas.decode_poly(rs["explicit_square_root_transition_Qi_t"]["denominator"], [t])
        mt = atlas.decode_poly(rt["explicit_square_root_transition_Qi_t"]["numerator"], [t]) / atlas.decode_poly(rt["explicit_square_root_transition_Qi_t"]["denominator"], [t])
        mt_pull = pulled_rational(clean(mt), Mst, t)
        if clean(ms * mt_pull - 1) != 0:
            raise SystemExit(f"square-root transition involution identity failed: {orbit}")
        stable_orbits.append({
            "orbit_members": list(orbit),
            "pgl2_involution_verified": True,
            "forward_times_pulled_reverse_transition_equals_one_exact": True,
        })

    stable_piece_count = len(stable_sources) * 36
    unresolved_square_source_piece_count = len(cross_sources) * 36
    if stable_piece_count + unresolved_square_source_piece_count != 17 * 36:
        raise SystemExit("square17 source piece accounting does not close")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5h.square17_swap23_square_root_transition_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5H_SQUARE17_SWAP23_SQUARE_ROOT_TRANSITION_PREFLIGHT",
        "role": "EXACT_NONCREDIT_SOURCE_BOUND_SWAP23_FUNCTION_FIELD_PREFLIGHT_FOR_THE_17_E5F_SQUARE_OR_TRIVIAL_EXCEPTIONAL_SOURCE_BLOCKS_USING_EXPLICIT_CANONICAL_MOD_SQUARE_REPRESENTATIVES_AND_EXACT_SQUARE_ROOT_GAUGES",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_sha256": D2_SHA,
            "r5b3b2_sha256": B3B2_SHA,
            "c4a_sha256": C4A_SHA,
            "c4b1_sha256": C4B1_SHA,
            "c4b1e5f_sha256": E5F_SHA,
            "c4b1e5g_sha256": E5G_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "square17_transition_preflight": {
            "source_block_count": 17,
            "source_piece_count": 17 * 36,
            "rows": sorted(rows, key=lambda r: r["source_exceptional_id"]),
            "source_blocks_whose_swap23_target_is_also_square_or_trivial": len(stable_sources),
            "source_blocks_whose_swap23_target_is_currently_nonsquare": len(cross_sources),
            "stable_square_orbit_count": len(stable_orbits),
            "stable_square_orbits": sorted(stable_orbits, key=lambda r: r["orbit_members"]),
            "function_field_square_root_transition_materialized_source_block_count": len(stable_sources),
            "function_field_square_root_transition_materialized_piece_count_before_cartier_attachment": stable_piece_count,
            "current_cross_class_source_block_count": len(cross_sources),
            "current_cross_class_source_piece_count": unresolved_square_source_piece_count,
        },
        "exact_consequence": {
            "all_17_square_or_trivial_sources_were_tested_against_the_actual_D2_swap23_target": True,
            "unit_one_was_not_assigned_merely_from_square_or_trivial_residue_classification": True,
            "every_square_source_used_an_explicit_canonical_mod_square_representative_and_exact_Qi_t_square_root": True,
            "stable_square_target_sources_have_explicit_function_field_square_root_transitions": len(stable_sources) > 0,
            "cross_class_sources_do_not_have_a_square_root_transition_for_the_current_canonical_local_representatives": len(cross_sources) > 0,
            "cross_class_failure_is_not_a_global_nonexistence_proof_for_all_source_bound_corrected_representatives": True,
            "regular_invertibility_on_the_D2_Rees_pieces_verified": False,
            "whole_1757_cover_line_bundle_gm_1_cocycle_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "coverage_accounting": {
            "prior_genuine_pole_line_action_unit_piece_count": 173,
            "new_function_field_transition_piece_count_not_yet_cartier_attached": stable_piece_count,
            "genuine_pole_line_action_unit_piece_count_remains": 173,
            "remaining_exceptional_source_piece_debt_before_any_E5H_cartier_attachment": 44 * 36,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "the 17 square/trivial E5F source blocks are no longer treated as one undifferentiated class: each is compared to its actual source-bound D2 swap23 target, with an explicit canonical local representative and exact Q(i)(t) square root; only the target-stable subset has an explicit function-field square-root transition",
            "what_is_still_missing": "lift the target-stable square-root transition rational functions to the relevant Rees charts and prove regular invertibility/Cartier legitimacy on their 36-piece blocks; cross-class source blocks require a different source-bound representative/correction mechanism rather than residue-class relabelling",
        },
        "next_exact_leaf": "V91C1X_R5B3B3C4B1E5H1_STABLE_SQUARE_ORBIT_REES_CARTIER_ACTION_UNIT_ATTACHMENT",
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
        s = cert["square17_transition_preflight"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "stable_square_source_blocks": s["source_blocks_whose_swap23_target_is_also_square_or_trivial"],
            "cross_class_source_blocks": s["source_blocks_whose_swap23_target_is_currently_nonsquare"],
            "stable_square_orbits": s["stable_square_orbit_count"],
            "function_field_transition_pieces": s["function_field_square_root_transition_materialized_piece_count_before_cartier_attachment"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5H certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
