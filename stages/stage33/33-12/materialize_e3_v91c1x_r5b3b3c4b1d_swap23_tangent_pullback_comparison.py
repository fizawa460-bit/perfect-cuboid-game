#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1_exceptional_p1_targeted_residue_field_squareclass as c4b1m

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C4B1 = HERE / "e3-v91c1x-r5b3b3c4b1-exceptional-p1-targeted-residue-field-squareclass.json"
C4B1C = HERE / "e3-v91c1x-r5b3b3c4b1c-nonconstant-exceptional-swap23-correction-preflight.json"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1d-swap23-tangent-pullback-comparison.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C4B1_SHA = "f14d9ca73ad0f0cbcf052c4512603bcc0942fb9263f97535023e8050ffcdced4"
C4B1C_SHA = "07c1865506e93d3fa71d6bb8b8435b4e944f2558ec8e042770b8659cba1736d8"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
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


def clean(x):
    return sp.cancel(sp.expand(x))


def encode_matrix(m: sp.Matrix) -> list:
    return [
        [atlas.encode_element(m[r, c]) for c in range(m.cols)]
        for r in range(m.rows)
    ]


def projective_normalize_matrix(m: sp.Matrix) -> sp.Matrix:
    pivot = next((clean(x) for x in list(m) if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit("zero projective matrix")
    return sp.Matrix(m.rows, m.cols, [clean(x / pivot) for x in list(m)])


def reconstruct_projection_forms(er: dict, model: dict) -> tuple[sp.Matrix, sp.Matrix]:
    B = sp.Matrix.hstack(model["p"], model["U"])
    first = er["physical_crossing_tangent_coordinates"][0]
    _q, d = c4b1m.side_param_and_tangent(
        int(first["side_index_1based"]),
        int(first["side_parameter_index_1based"]),
    )
    solution, parameters = B.gauss_jordan_solve(d)
    if parameters.rows or B * solution != d:
        raise SystemExit(f"first tangent solve failed: {er['exceptional_id']}")
    p0 = solution[1:4, 0]
    forms = c4b1m.independent_columns(
        [x for x in c4b1m.perpendicular_candidates(p0) if x != sp.zeros(3, 1)]
    )
    if len(forms) != 2:
        raise SystemExit(f"projection forms moved: {er['exceptional_id']}")
    if any(clean(f.dot(p0)) != 0 for f in forms):
        raise SystemExit(f"projection forms no longer vanish at base point: {er['exceptional_id']}")
    return forms[0], forms[1]


def pgl2_tangent_map(source_er: dict, source_model: dict, target_er: dict, target_model: dict) -> dict:
    su, sv = sp.symbols("su sv")
    source_y = sp.Matrix([
        clean(x.subs({source_model["u"]: su, source_model["v"]: sv}, simultaneous=True))
        for x in source_model["yuv"]
    ])
    source_ambient_tangent = source_model["U"] * source_y
    acted_ambient_tangent = atlas.tau_vec(source_ambient_tangent)

    target_B = sp.Matrix.hstack(target_model["p"], target_model["U"])
    solution, parameters = target_B.gauss_jordan_solve(acted_ambient_tangent)
    if parameters.rows or clean(target_B * solution - acted_ambient_tangent) != sp.zeros(7, 1):
        raise SystemExit(
            f"source-bound tangent transport failed: {source_er['exceptional_id']}->{target_er['exceptional_id']}"
        )
    target_y = sp.Matrix([clean(x) for x in solution[1:4, 0]])
    f0, f1 = reconstruct_projection_forms(target_er, target_model)
    raw_u = clean(f0.dot(target_y))
    raw_v = clean(f1.dot(target_y))
    if raw_u == 0 or raw_v == 0:
        raise SystemExit(
            f"degenerate raw target P1 coordinate: {source_er['exceptional_id']}->{target_er['exceptional_id']}"
        )

    PU = sp.Poly(sp.expand(raw_u), su, sv, extension=I)
    PV = sp.Poly(sp.expand(raw_v), su, sv, extension=I)
    common = sp.gcd(PU, PV)
    common_expr = sp.expand(common.as_expr())
    lin_u = clean(raw_u / common_expr)
    lin_v = clean(raw_v / common_expr)
    check_u = sp.Poly(sp.expand(lin_u), su, sv, extension=I)
    check_v = sp.Poly(sp.expand(lin_v), su, sv, extension=I)
    if check_u.total_degree() != 1 or check_v.total_degree() != 1:
        raise SystemExit(
            f"target P1 pullback did not reduce to linear forms: {source_er['exceptional_id']}->{target_er['exceptional_id']}"
        )
    if check_u.coeff_monomial(1) != 0 or check_v.coeff_monomial(1) != 0:
        raise SystemExit("P1 pullback unexpectedly acquired constant term")

    a = clean(check_u.coeff_monomial(su))
    b = clean(check_u.coeff_monomial(sv))
    c = clean(check_v.coeff_monomial(su))
    d = clean(check_v.coeff_monomial(sv))
    M = sp.Matrix([[a, b], [c, d]])
    if clean(M.det()) == 0:
        raise SystemExit(
            f"source-bound P1 map is singular: {source_er['exceptional_id']}->{target_er['exceptional_id']}"
        )
    Mnorm = projective_normalize_matrix(M)

    target_param = sp.Matrix([
        clean(
            x.subs(
                {target_model["u"]: lin_u, target_model["v"]: lin_v},
                simultaneous=True,
            )
        )
        for x in target_model["yuv"]
    ])
    for r in range(3):
        for s in range(r + 1, 3):
            if clean(target_y[r] * target_param[s] - target_y[s] * target_param[r]) != 0:
                raise SystemExit(
                    f"P1 map missed transported target conic point: {source_er['exceptional_id']}->{target_er['exceptional_id']}"
                )

    return {
        "source_exceptional_id": source_er["exceptional_id"],
        "target_exceptional_id": target_er["exceptional_id"],
        "common_factor_Qi_su_sv_sha256": csha(atlas.encode_poly(common_expr, [su, sv])),
        "pgl2_matrix_Qi_projectively_normalized": encode_matrix(Mnorm),
        "pgl2_matrix_sha256": csha(encode_matrix(Mnorm)),
        "determinant_Qi": atlas.encode_element(clean(Mnorm.det())),
        "linear_u_Qi_su_sv": atlas.encode_poly(clean(Mnorm[0, 0] * su + Mnorm[0, 1] * sv), [su, sv]),
        "linear_v_Qi_su_sv": atlas.encode_poly(clean(Mnorm[1, 0] * su + Mnorm[1, 1] * sv), [su, sv]),
        "_matrix": Mnorm,
    }


def reconstruct_residue_expr(
    eid: str,
    model: dict,
    coeffs: dict[str, sp.Matrix],
    c4a_by_eid: dict[str, dict],
    c4b1_by_eid: dict[str, dict],
) -> sp.Expr:
    t = sp.Symbol("t")
    crow = c4a_by_eid[eid]
    odd_ids = list(crow["combined_tame_residue_odd_linear_carrier_ids"])
    valuation_support = set(crow["nonzero_carrier_valuation_ids"])
    expr = sp.Integer(1)
    for cid in odd_ids:
        c = coeffs[cid]
        constant = clean((c.T * model["p"])[0])
        if cid not in valuation_support:
            if constant == 0:
                raise SystemExit(f"unexpected zero order-zero carrier: {eid}/{cid}")
            expr = clean(expr * constant)
        else:
            if constant != 0:
                raise SystemExit(f"unexpected nonzero order-one carrier: {eid}/{cid}")
            tangent = clean((c.T * model["U"] * model["yuv"])[0])
            tangent_t = clean(
                tangent.subs({model["u"]: t, model["v"]: 1}, simultaneous=True)
            )
            if tangent_t == 0:
                raise SystemExit(f"vanishing exceptional tangent residue: {eid}/{cid}")
            expr = clean(expr * tangent_t)
    expected_hash = c4b1_by_eid[eid]["combined_residue_representative_Qi_t_sha256"]
    actual_hash = csha(atlas.encode_poly(expr, [t]))
    if actual_hash != expected_hash:
        raise SystemExit(
            f"C4B1 residue reconstruction moved: {eid}: {actual_hash} != {expected_hash}"
        )
    return expr


def normalized_factor_signature(fac: sp.Expr, t: sp.Symbol) -> tuple[str, sp.Expr, sp.Expr]:
    P = sp.Poly(sp.expand(fac), t, extension=I)
    lc = clean(P.LC())
    monic = sp.Poly(sp.expand(P.as_expr() / lc), t, extension=I)
    encoded = atlas.encode_poly(monic.as_expr(), [t])
    return csha(encoded), monic.as_expr(), lc


def rational_squareclass(expr: sp.Expr, t: sp.Symbol) -> dict:
    expr = clean(expr)
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    den = sp.expand(den)
    if num == 0 or den == 0:
        raise SystemExit("invalid zero rational squareclass representative")
    cn, nf = sp.factor_list(num, t, extension=I)
    cd, df = sp.factor_list(den, t, extension=I)
    scalar = clean(cn / cd)
    parity: dict[str, dict] = {}

    def add_side(factors, denominator: bool):
        nonlocal scalar
        for fac, exponent in factors:
            sig, monic, lc = normalized_factor_signature(fac, t)
            if denominator:
                scalar = clean(scalar / (lc ** exponent))
            else:
                scalar = clean(scalar * (lc ** exponent))
            if exponent % 2:
                if sig in parity:
                    parity.pop(sig)
                else:
                    parity[sig] = {
                        "degree": int(sp.Poly(monic, t, extension=I).degree()),
                        "projective_factor_sha256": sig,
                    }

    add_side(nf, False)
    add_side(df, True)
    odd = sorted(parity.values(), key=lambda x: (x["degree"], x["projective_factor_sha256"]))
    scalar_square = c4b1m.qi_is_square(scalar)
    return {
        "factorization_scalar_Qi": atlas.encode_element(scalar),
        "coefficient_is_square_in_Qi": scalar_square,
        "odd_irreducible_factor_count": len(odd),
        "odd_irreducible_factors": odd,
        "square_trivial": scalar_square and not odd,
    }


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    c4b1 = load_locked(C4B1, C4B1_SHA)
    c4b1c = load_locked(C4B1C, C4B1C_SHA)
    exc = load_locked(EXC, EXC_SHA)

    node_map = {
        row["source_node"]: row["acted_target_node"]
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    expected_map = {
        row["exceptional_id"]: row["swap23_target_exceptional_id"]
        for row in c4b1c["nonconstant_exceptional_targets"]["rows"]
    }
    if set(expected_map) != set(TARGETS):
        raise SystemExit("C4B1C nonconstant target set moved")
    if any(node_map[eid] != expected_map[eid] for eid in TARGETS):
        raise SystemExit("C4B1C/D2 exceptional swap23 map disagreement")

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    models = {eid: c4b1m.reconstruct_exceptional_model(er_by_eid[eid]) for eid in TARGETS}
    c4b1_by_eid = {
        row["exceptional_id"]: row
        for row in c4b1["exceptional_squareclass_reduction"]["rows"]
    }
    c4a_by_eid = {
        row["exceptional_id"]: row
        for row in c4a["exceptional_prime_preflight"]["rows"]
    }
    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    coeffs = {
        row["carrier_id"]: sp.Matrix(
            [atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]]
        )
        for row in inv_rows
    }
    residues = {
        eid: reconstruct_residue_expr(eid, models[eid], coeffs, c4a_by_eid, c4b1_by_eid)
        for eid in TARGETS
    }

    directed_maps = {}
    for eid in TARGETS:
        tid = expected_map[eid]
        directed_maps[(eid, tid)] = pgl2_tangent_map(
            er_by_eid[eid], models[eid], er_by_eid[tid], models[tid]
        )

    orbit_rows = []
    compared_directed = 0
    same_directed = 0
    mismatch_directed = 0
    for orbit in c4b1c["swap23_orbit_reduction"]["orbits"]:
        members = list(orbit["orbit_members"])
        if len(members) != 2:
            raise SystemExit("C4B1C nonconstant orbit ceased to have size 2")
        a, b = members
        Mab = directed_maps[(a, b)]["_matrix"]
        Mba = directed_maps[(b, a)]["_matrix"]
        comp = projective_normalize_matrix(Mba * Mab)
        if comp != sp.eye(2):
            raise SystemExit(f"source-bound P1 maps failed involution check on orbit {members}: {comp}")

        directed_rows = []
        for source, target in [(a, b), (b, a)]:
            row_map = directed_maps[(source, target)]
            M = row_map["_matrix"]
            t = sp.Symbol("t")
            lu = clean(M[0, 0] * t + M[0, 1])
            lv = clean(M[1, 0] * t + M[1, 1])
            target_pullback = clean(residues[target].subs({t: clean(lu / lv)}, simultaneous=True))
            ratio = clean(residues[source] / target_pullback)
            sq = rational_squareclass(ratio, t)
            compared_directed += 1
            if sq["square_trivial"]:
                same_directed += 1
                classification = "SAME_SQUARECLASS_AFTER_SOURCE_BOUND_SWAP23_TANGENT_PULLBACK"
            else:
                mismatch_directed += 1
                classification = "NONSQUARE_SQUARECLASS_DIFFERENCE_AFTER_SOURCE_BOUND_SWAP23_TANGENT_PULLBACK"
            directed_rows.append({
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "source_residue_Qi_t_sha256": c4b1_by_eid[source]["combined_residue_representative_Qi_t_sha256"],
                "target_residue_Qi_t_sha256": c4b1_by_eid[target]["combined_residue_representative_Qi_t_sha256"],
                "pgl2_matrix_Qi_projectively_normalized": row_map["pgl2_matrix_Qi_projectively_normalized"],
                "pgl2_matrix_sha256": row_map["pgl2_matrix_sha256"],
                "pgl2_determinant_Qi": row_map["determinant_Qi"],
                "target_pullback_rational_Qi_t_sha256": csha(atlas.encode_rational(target_pullback, [t])),
                "source_over_pulled_target_rational_Qi_t_sha256": csha(atlas.encode_rational(ratio, [t])),
                "squareclass_difference": sq,
                "classification": classification,
            })
        orbit_rows.append({
            "orbit_members": members,
            "source_bound_p1_involution_verified": True,
            "directed_comparisons": directed_rows,
            "same_squareclass_in_both_directions": all(
                r["squareclass_difference"]["square_trivial"] for r in directed_rows
            ),
        })

    for row in directed_maps.values():
        row.pop("_matrix", None)

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1d.swap23_tangent_pullback_comparison.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1D_SWAP23_TANGENT_PULLBACK_COMPARISON_OF_FOUR_NONCONSTANT_EXCEPTIONAL_RESIDUES",
        "role": "EXACT_NONCREDIT_SOURCE_BOUND_SWAP23_TANGENT_P1_PULLBACK_AND_SQUARECLASS_COMPARISON_FOR_THE_FOUR_NONCONSTANT_EXCEPTIONAL_OBSTRUCTIONS",
        "entry": {
            "pr": 1695,
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "r5b2d2_swap23_common_refinement_sha256": D2_SHA,
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c4a_tame_residue_parity_preflight_sha256": C4A_SHA,
            "r5b3b3c4b1_exceptional_squareclass_sha256": C4B1_SHA,
            "r5b3b3c4b1c_nonconstant_swap23_preflight_sha256": C4B1C_SHA,
            "frozen_exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "method": {
            "source_bound_action": "global swap23 coordinate permutation from R5B2D2, restricted to each frozen tangent quotient",
            "target_p1_coordinate_reconstruction": "apply the exact target deterministic projection forms used by C4B1 to the transported tangent-conic point, cancel the common homogeneous factor, and require an invertible PGL2 linear pair",
            "residue_reconstruction": "replay the exact C4B1 ambient-linear carrier evaluation from B3B2/C4A and verify every C4B1 residue hash before comparison",
            "squareclass_comparison": "pull the target Q(i)(t) residue through the source-bound PGL2 map and test source/pullback(target) exactly in Q(i)(t)^*/Q(i)(t)^{*2}",
        },
        "swap23_nonconstant_orbit_comparison": {
            "target_count": 4,
            "orbit_count": 2,
            "directed_comparison_count": compared_directed,
            "same_squareclass_directed_count": same_directed,
            "nonsquare_difference_directed_count": mismatch_directed,
            "orbits": orbit_rows,
        },
        "exact_consequence": {
            "source_bound_swap23_p1_maps_materialized_for_all_four_nonconstant_targets": True,
            "source_bound_swap23_p1_maps_verified_involutive_on_both_orbits": True,
            "four_current_nonconstant_residue_squareclasses_compared_on_common_function_fields": True,
            "all_four_current_residue_classes_swap23_compatible": mismatch_directed == 0,
            "a_nonsquare_difference_if_present_is_only_the_required_local_correction_squareclass_not_an_allowed_global_correction": True,
            "source_bound_cech_or_refinement_unit_correction_materialized": False,
            "exceptional_residue_cancellation_verified": False,
            "all_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "missing_source_bound_correction_data": c4b1c["missing_source_bound_correction_data"],
        "next_exact_leaf_if_any_nonsquare_difference": "V91C1X_R5B3B3C4B1E_SOURCE_BOUND_1757_REFINEMENT_UNIT_OR_CECH_COCHAIN_REALIZATION_FOR_SWAP23_ORBIT_DIFFERENCES",
        "next_exact_leaf_if_all_swap23_compatible": "V91C1X_R5B3B3C4B1E_SOURCE_BOUND_GLOBAL_CECH_REPRESENTATIVE_ASSEMBLY_PREFLIGHT",
        "parallel_outstanding_leaf": c4b1c["parallel_outstanding_leaf"],
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "exceptional_cancellation_credit": False,
            "unramifiedness_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "merge_allowed": False,
        },
    }
    return cert


def materialize(write: bool) -> dict:
    cert = build_certificate()
    cert["canonical_sha256"] = csha(cert)
    if write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        if not OUT.exists():
            raise SystemExit(f"missing materialized artifact: {OUT}")
        existing = json.loads(OUT.read_text(encoding="utf-8"))
        if existing != cert:
            raise SystemExit("materialized C4B1D artifact does not match exact rebuild")
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = materialize(args.write)
    print(cert["canonical_sha256"])
    summary = cert["swap23_nonconstant_orbit_comparison"]
    print(
        f"directed={summary['directed_comparison_count']} "
        f"same={summary['same_squareclass_directed_count']} "
        f"mismatch={summary['nonsquare_difference_directed_count']}"
    )


if __name__ == "__main__":
    main()
