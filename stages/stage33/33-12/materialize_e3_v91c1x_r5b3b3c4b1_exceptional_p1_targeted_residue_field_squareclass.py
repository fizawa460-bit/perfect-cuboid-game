#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1-exceptional-p1-targeted-residue-field-squareclass.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I
UVS = [(0, 1), (1, 0), (1, 1), (-1, 1), (I, 1), (-I, 1)]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x) -> bool:
    return clean(x) == 0


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if not is_zero(x)), None)
    if pivot is None:
        raise SystemExit("zero projective vector")
    return tuple(clean(x / pivot) for x in vals)


def independent_columns(columns):
    out = []
    rank = 0
    for col in columns:
        candidate = sp.Matrix.hstack(*(out + [sp.Matrix(col)]))
        new_rank = candidate.rank()
        if new_rank > rank:
            out.append(sp.Matrix(col))
            rank = new_rank
    return out


def perpendicular_candidates(v):
    x, y, z = list(v)
    return [
        sp.Matrix([y, -x, 0]),
        sp.Matrix([z, 0, -x]),
        sp.Matrix([0, z, -y]),
    ]


def rational_pair(q):
    q = clean(q)
    if q.is_Rational is not True:
        raise SystemExit(f"expected rational coefficient, got {q}")
    return [int(sp.numer(q)), int(sp.denom(q))]


def encode_element(x):
    x = clean(x)
    xc = clean(sp.conjugate(x))
    a = clean((x + xc) / 2)
    b = clean((x - xc) / (2 * I))
    if clean(x - a - b * I) != 0:
        raise SystemExit(f"element escaped Q(i): {x}")
    ar, br = rational_pair(a), rational_pair(b)
    return [ar[0], ar[1], br[0], br[1]]


def encode_vector(v):
    return [encode_element(x) for x in list(v)]


def encode_matrix(m):
    return [[encode_element(m[r, c]) for c in range(m.cols)] for r in range(m.rows)]


def side_metadata(side_index: int):
    j = side_index - 1
    family = j // 8
    r = j % 8
    e1 = [1, -1][r // 4]
    e2 = [1, -1][(r // 2) % 2]
    e3 = [1, -1][r % 2]
    return family, e1, e2, e3


def side_param_and_tangent(side_index: int, parameter_index: int):
    family, e1, e2, e3 = side_metadata(side_index)
    u, v = UVS[parameter_index - 1]
    X, Y, Z = u * u - v * v, 2 * u * v, u * u + v * v
    du, dv = (1, 0) if v != 0 else (0, 1)
    dX = 2 * u * du - 2 * v * dv
    dY = 2 * (du * v + u * dv)
    dZ = 2 * u * du + 2 * v * dv
    if family == 0:
        q = [0, -e1 * X, -e2 * Y, -e3 * Z, Y, X, Z]
        d = [0, -e1 * dX, -e2 * dY, -e3 * dZ, dY, dX, dZ]
    elif family == 1:
        q = [-e2 * Y, 0, -e1 * X, X, -e3 * Z, Y, Z]
        d = [-e2 * dY, 0, -e1 * dX, dX, -e3 * dZ, dY, dZ]
    else:
        q = [-e1 * X, -e2 * Y, 0, Y, X, -e3 * Z, Z]
        d = [-e1 * dX, -e2 * dY, 0, dY, dX, -e3 * dZ, dZ]
    return sp.Matrix([clean(x) for x in q]), sp.Matrix([clean(x) for x in d])


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ])


def jacobian(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        [2 * a1, 2 * a2, 0, 0, 0, -2 * b3, 0],
        [0, 2 * a2, 2 * a3, -2 * b1, 0, 0, 0],
        [2 * a1, 0, 2 * a3, 0, -2 * b2, 0, 0],
        [2 * a1, 2 * a2, 2 * a3, 0, 0, 0, -2 * c],
    ])


def reconstruct_exceptional_model(er: dict) -> dict:
    eid = er["exceptional_id"]
    p = sp.Matrix([atlas.decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
    if any(not is_zero(x) for x in quadrics(p)):
        raise SystemExit(f"node escaped surface: {eid}")
    J = jacobian(p)
    if J.rank() != 3:
        raise SystemExit(f"node Jacobian rank moved: {eid}")
    W = J.nullspace()
    Bcols = independent_columns([p] + W)
    if len(Bcols) != 4 or Bcols[0] != p:
        raise SystemExit(f"radial-first tangent basis moved: {eid}")
    B = sp.Matrix.hstack(*Bcols)

    alpha_space = J.T.nullspace()
    if len(alpha_space) != 1:
        raise SystemExit(f"node quadratic relation moved: {eid}")
    alpha = alpha_space[0]

    def qeval(v):
        return clean((alpha.T * quadrics(v))[0])

    U = B[:, 1:4]
    G = sp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            G[r, c] = clean(
                (qeval(U[:, r] + U[:, c]) - qeval(U[:, r]) - qeval(U[:, c])) / 2
            )
    if G != G.T or is_zero(G.det()):
        raise SystemExit(f"exceptional tangent conic degenerated: {eid}")

    tangent_rows = []
    ys = []
    for cr in er["physical_crossing_tangent_coordinates"]:
        side = int(cr["side_index_1based"])
        z = int(cr["side_parameter_index_1based"])
        q, d = side_param_and_tangent(side, z)
        if projective_normalize(q) != projective_normalize(p):
            raise SystemExit(f"node/side incidence moved: {eid}/{side}/{z}")
        solution, parameters = B.gauss_jordan_solve(d)
        if parameters.rows or B * solution != d:
            raise SystemExit(f"tangent solve failed: {eid}/{side}/{z}")
        y = solution[1:4, 0]
        if y == sp.zeros(3, 1) or not is_zero((y.T * G * y)[0]):
            raise SystemExit(f"side tangent missed exceptional conic: {eid}/{side}/{z}")
        ys.append(y)
        tangent_rows.append((cr, d, y))

    p0 = ys[0]
    forms = independent_columns(
        [x for x in perpendicular_candidates(p0) if x != sp.zeros(3, 1)]
    )
    if len(forms) != 2 or any(not is_zero(f.dot(p0)) for f in forms):
        raise SystemExit(f"projection forms failed: {eid}")
    grad = G * p0
    tangent_kernel = independent_columns(
        [x for x in perpendicular_candidates(grad) if x != sp.zeros(3, 1)]
    )
    w = next(
        (x for x in tangent_kernel if sp.Matrix.hstack(p0, x).rank() == 2),
        None,
    )
    if w is None or not is_zero(grad.dot(w)):
        raise SystemExit(f"projection base tangent failed: {eid}")

    full_crossings = []
    for k, (cr, d, y) in enumerate(tangent_rows):
        source = w if k == 0 else y
        pair = sp.Matrix([clean(forms[0].dot(source)), clean(forms[1].dot(source))])
        if pair == sp.zeros(2, 1):
            raise SystemExit(f"zero P1 coordinate reconstruction: {eid}")
        pair = sp.Matrix(projective_normalize(pair))
        frozen = sp.Matrix([
            atlas.decode_element(x)
            for x in cr["exceptional_P1_homogeneous_coordinate_L_basis"]
        ])
        if projective_normalize(frozen) != projective_normalize(pair):
            raise SystemExit(
                f"frozen exceptional P1 coordinate moved: {eid}/{cr['side_index_1based']}"
            )
        full_crossings.append({
            "side_index_1based": int(cr["side_index_1based"]),
            "side_parameter": cr["side_parameter"],
            "side_parameter_index_1based": int(cr["side_parameter_index_1based"]),
            "ambient_tangent_vector_L_basis": encode_vector(d),
            "exceptional_conic_point_L_basis": encode_vector(y),
            "exceptional_P1_homogeneous_coordinate_L_basis": encode_vector(pair),
        })

    commitment = {
        "node": encode_vector(p),
        "affine_tangent_basis_radial_first": encode_matrix(B),
        "exceptional_conic_gram": encode_matrix(G),
        "projection_forms": encode_matrix(sp.Matrix.hstack(*forms).T),
        "projection_base_tangent": encode_vector(w),
        "full_crossings": sorted(
            full_crossings,
            key=lambda x: (x["side_index_1based"], x["side_parameter_index_1based"]),
        ),
    }
    if csha(commitment) != er["full_tangent_conic_coordinate_model_sha256"]:
        raise SystemExit(f"full frozen tangent model commitment moved: {eid}")

    u, v = sp.symbols("u v")
    f0, f1 = forms
    m = v * f0 - u * f1
    z = sp.Matrix([
        clean(m[1] * p0[2] - m[2] * p0[1]),
        clean(m[2] * p0[0] - m[0] * p0[2]),
        clean(m[0] * p0[1] - m[1] * p0[0]),
    ])
    if z == sp.zeros(3, 1):
        raise SystemExit(f"projection-line direction vanished identically: {eid}")
    A = clean((z.T * G * z)[0])
    Blin = clean((p0.T * G * z)[0])
    yuv = sp.Matrix([clean(A * p0[j] - 2 * Blin * z[j]) for j in range(3)])
    if yuv == sp.zeros(3, 1):
        raise SystemExit(f"P1 conic parametrization vanished identically: {eid}")
    if not is_zero((yuv.T * G * yuv)[0]):
        raise SystemExit(f"P1 parametrization missed conic: {eid}")
    if not is_zero(v * f0.dot(yuv) - u * f1.dot(yuv)):
        raise SystemExit(f"P1 projection ratio relation failed: {eid}")

    return {
        "eid": eid,
        "p": p,
        "U": U,
        "u": u,
        "v": v,
        "yuv": yuv,
        "parametrization_sha256": csha({
            "exceptional_id": eid,
            "p0_Qi": encode_vector(p0),
            "projection_forms_Qi": encode_matrix(sp.Matrix.hstack(*forms).T),
            "yuv_Qi": [atlas.encode_poly(x, [u, v]) for x in yuv],
        }),
    }


def rational_sqrt_if_square(q):
    q = sp.Rational(q)
    if q < 0:
        return None
    n, d = int(sp.numer(q)), int(sp.denom(q))
    sn, sd = math.isqrt(n), math.isqrt(d)
    if sn * sn != n or sd * sd != d:
        return None
    return sp.Rational(sn, sd)


def qi_is_square(z) -> bool:
    z = clean(z)
    zc = clean(sp.conjugate(z))
    a = clean((z + zc) / 2)
    b = clean((z - zc) / (2 * I))
    if a.is_Rational is not True or b.is_Rational is not True:
        raise SystemExit(f"square test escaped Q(i): {z}")
    if z == 0:
        return True
    norm = clean(a * a + b * b)
    r = rational_sqrt_if_square(norm)
    if r is None:
        return False
    x2 = clean((r + a) / 2)
    y2 = clean((r - a) / 2)
    sx = rational_sqrt_if_square(x2)
    sy = rational_sqrt_if_square(y2)
    if sx is None or sy is None:
        return False
    for x in {sx, -sx}:
        for y in {sy, -sy}:
            if clean((x + I * y) ** 2 - z) == 0:
                return True
    return False


def poly_squareclass(expr, t):
    P = sp.Poly(sp.expand(expr), t, extension=I)
    if P.is_zero:
        raise SystemExit("zero residue representative")
    coeff, facs = sp.factor_list(P.as_expr(), t, extension=I)
    odd_factors = []
    for fac, exponent in facs:
        if exponent % 2:
            FP = sp.Poly(fac, t, extension=I)
            terms = FP.terms()
            pivot = sp.sympify(terms[0][1])
            normalized = sp.Poly(sp.expand(FP.as_expr() / pivot), t, extension=I)
            coeff = clean(coeff * pivot ** exponent)
            odd_factors.append({
                "degree": int(normalized.degree()),
                "projective_factor_sha256": csha(
                    [
                        {
                            "exponent": int(mon[0]),
                            "coefficient_Qi": encode_element(sp.sympify(c)),
                        }
                        for mon, c in normalized.terms()
                    ]
                ),
            })
    odd_factors.sort(key=lambda x: (x["degree"], x["projective_factor_sha256"]))
    constant_square = qi_is_square(coeff)
    return {
        "factorization_coefficient_Qi": encode_element(coeff),
        "coefficient_is_square_in_Qi": constant_square,
        "odd_irreducible_factor_count": len(odd_factors),
        "odd_irreducible_factors": odd_factors,
        "square_trivial": constant_square and not odd_factors,
    }


def build_certificate() -> dict:
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    exc = load_locked(EXC, EXC_SHA)

    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    carrier_ids = [r["carrier_id"] for r in inv_rows]
    if len(carrier_ids) != len(set(carrier_ids)):
        raise SystemExit("duplicate carrier id")
    inv = {r["carrier_id"]: r for r in inv_rows}
    coeffs = {
        cid: sp.Matrix([atlas.decode_element(z) for z in inv[cid]["normalized_coefficients_Qi"]])
        for cid in carrier_ids
    }

    c4a_rows = c4a["exceptional_prime_preflight"]["rows"]
    if len(c4a_rows) != 48:
        raise SystemExit("C4A exceptional row count moved")
    c4a_by_eid = {r["exceptional_id"]: r for r in c4a_rows}
    expected_eids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if set(c4a_by_eid) != set(expected_eids):
        raise SystemExit("C4A exceptional inventory moved")
    if c4a["exceptional_prime_preflight"]["zero_formal_linear_factor_parity_exceptional_prime_count"] != 7:
        raise SystemExit("C4A zero-parity count moved")

    exc_rows = exc["exceptional_models"]
    if [r["exceptional_id"] for r in exc_rows] != expected_eids:
        raise SystemExit("frozen exceptional model inventory moved")

    rows = []
    zero_parity = 0
    targeted = 0
    targeted_square = 0
    targeted_nonsquare = 0
    tangent_factor_evaluations = 0
    constant_factor_evaluations = 0

    t = sp.Symbol("t")
    for er in exc_rows:
        model = reconstruct_exceptional_model(er)
        eid = model["eid"]
        crow = c4a_by_eid[eid]
        odd_ids = list(crow["combined_tame_residue_odd_linear_carrier_ids"])
        valuation_support = set(crow["nonzero_carrier_valuation_ids"])

        if not odd_ids:
            zero_parity += 1
            rows.append({
                "exceptional_id": eid,
                "c4a_odd_carrier_ids": [],
                "classification": "SQUARE_TRIVIAL_BY_C4A_ZERO_FORMAL_LINEAR_FACTOR_PARITY",
                "square_trivial_in_Qi_exceptional_function_field": True,
                "frozen_tangent_model_sha256": er["full_tangent_conic_coordinate_model_sha256"],
                "deterministic_p1_parametrization_sha256": model["parametrization_sha256"],
            })
            continue

        targeted += 1
        expr = sp.Integer(1)
        tangent_ids = []
        constant_ids = []
        per_carrier = []
        for cid in odd_ids:
            if cid not in coeffs:
                raise SystemExit(f"C4A odd carrier escaped B3B2 inventory: {eid}/{cid}")
            c = coeffs[cid]
            constant = clean((c.T * model["p"])[0])
            expected_order = 1 if cid in valuation_support else 0
            actual_order = 0 if constant != 0 else 1
            if actual_order != expected_order:
                raise SystemExit(
                    f"C4A/Rees valuation disagreement: {eid}/{cid}: "
                    f"{actual_order} != {expected_order}"
                )
            if actual_order == 0:
                expr = clean(expr * constant)
                constant_ids.append(cid)
                constant_factor_evaluations += 1
                per_carrier.append({
                    "carrier_id": cid,
                    "exceptional_order": 0,
                    "residue_unit_kind": "NODE_CONSTANT",
                    "node_constant_Qi": encode_element(constant),
                })
            else:
                tangent = clean((c.T * model["U"] * model["yuv"])[0])
                if tangent == 0:
                    raise SystemExit(f"carrier tangent leading form vanished on exceptional conic: {eid}/{cid}")
                tangent_t = clean(tangent.subs({model["u"]: t, model["v"]: 1}))
                if tangent_t == 0:
                    raise SystemExit(f"dehomogenized tangent leading form vanished: {eid}/{cid}")
                expr = clean(expr * tangent_t)
                tangent_ids.append(cid)
                tangent_factor_evaluations += 1
                per_carrier.append({
                    "carrier_id": cid,
                    "exceptional_order": 1,
                    "residue_unit_kind": "TANGENT_LINEAR_SECTION_ON_EXCEPTIONAL_CONIC",
                    "dehomogenized_pullback_Qi_t_sha256": csha(atlas.encode_poly(tangent_t, [t])),
                })

        sq = poly_squareclass(expr, t)
        if sq["square_trivial"]:
            targeted_square += 1
            classification = "SQUARE_TRIVIAL_AFTER_EXACT_EXCEPTIONAL_P1_RESIDUE_FIELD_REDUCTION"
        else:
            targeted_nonsquare += 1
            classification = "NONSQUARE_AFTER_EXACT_EXCEPTIONAL_P1_RESIDUE_FIELD_REDUCTION"

        rows.append({
            "exceptional_id": eid,
            "c4a_odd_carrier_ids": odd_ids,
            "odd_carrier_count": len(odd_ids),
            "odd_carrier_exceptional_order_one_ids": tangent_ids,
            "odd_carrier_exceptional_order_zero_ids": constant_ids,
            "per_odd_carrier_residue_units": per_carrier,
            "combined_residue_representative_Qi_t_sha256": csha(atlas.encode_poly(expr, [t])),
            "combined_residue_squareclass": sq,
            "classification": classification,
            "square_trivial_in_Qi_exceptional_function_field": sq["square_trivial"],
            "frozen_tangent_model_sha256": er["full_tangent_conic_coordinate_model_sha256"],
            "deterministic_p1_parametrization_sha256": model["parametrization_sha256"],
        })

    if zero_parity != 7 or targeted != 41:
        raise SystemExit(f"C4A exceptional partition moved: zero={zero_parity} targeted={targeted}")
    if targeted_square + targeted_nonsquare != 41:
        raise SystemExit("targeted exceptional classification incomplete")

    all_square = targeted_nonsquare == 0
    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1.exceptional_p1_targeted_residue_field_squareclass.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1_EXCEPTIONAL_P1_TARGETED_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "role": "EXACT_NONCREDIT_EXCEPTIONAL_DIVISOR_RESIDUE_FIELD_REDUCTION_USING_FROZEN_QI_TANGENT_CONICS_AND_DETERMINISTIC_P1_PARAMETERIZATIONS",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c4a_tame_residue_parity_preflight_sha256": C4A_SHA,
            "frozen_exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
        },
        "method": {
            "field": "Q(i)",
            "exceptional_curve_model": "nonsingular tangent conic with frozen deterministic projection-from-a-point P1 coordinate",
            "valuation_zero_carrier_unit_reduction": "ambient linear carrier evaluated at the normalized node",
            "valuation_one_carrier_unit_reduction": "ambient linear carrier restricted to tangent quotient and then to the exceptional conic",
            "p1_second_intersection_formula": "y=A*p0-2*B*z for z=(v*f0-u*f1)x p0, A=z^T G z, B=p0^T G z",
            "squareclass_test": "dehomogenize u=t,v=1; factor exactly in Q(i)[t]; require even irreducible-factor parity and square scalar in Q(i)",
            "negative_tame_exponents_mod_square": "inverse and direct factor have the same class in K*/K*2",
            "projective_denominator_note": "each tangent linear section pulls back to homogeneous degree 2, so the v-power removed by dehomogenization is even and squareclass-harmless",
        },
        "exceptional_squareclass_reduction": {
            "frozen_exceptional_prime_count": 48,
            "c4a_zero_formal_parity_count": zero_parity,
            "targeted_nonzero_formal_parity_count": targeted,
            "targeted_square_trivial_count": targeted_square,
            "targeted_nonsquare_count": targeted_nonsquare,
            "all_48_exceptional_residues_square_trivial": all_square,
            "tangent_factor_evaluation_count": tangent_factor_evaluations,
            "node_constant_factor_evaluation_count": constant_factor_evaluations,
            "rows": rows,
        },
        "construction_status": {
            "all_48_frozen_exceptional_tangent_models_reconstructed_and_commitment_checked": True,
            "all_41_nonzero_formal_parity_exceptional_rows_reduced_in_exact_Qi_P1_function_fields": True,
            "exceptional_prime_residue_squareclasses_audited": True,
            "strict_prime_repeated_factor_cross_carrier_incidence_materialized": False,
            "strict_prime_residue_field_squareclasses_materialized": False,
            "all_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "exact_consequence": {
            "exceptional_prime_residue_cancellation_verified": all_square,
            "if_targeted_nonsquare_count_is_nonzero_then_current_formal_symbol_candidate_is_ramified_on_those_exceptional_primes": targeted_nonsquare > 0,
            "no_strict_prime_conclusion_is_inferred_from_this_leaf": True,
        },
        "next_missing_object": "REPEATED_C1_FACTOR_CROSS_CARRIER_GEOMETRIC_INCIDENCE_AND_STRICT_PRIME_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "next_exact_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "hostile_audit_credit": False,
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
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != cert:
            raise SystemExit("materialized C4B1 artifact is stale")
    summary = cert["exceptional_squareclass_reduction"]
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3C4B1_EXCEPTIONAL_P1_SQUARECLASS_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "c4a_zero_formal_parity": summary["c4a_zero_formal_parity_count"],
        "targeted_nonzero_formal_parity": summary["targeted_nonzero_formal_parity_count"],
        "targeted_square_trivial": summary["targeted_square_trivial_count"],
        "targeted_nonsquare": summary["targeted_nonsquare_count"],
        "all_48_exceptional_residues_square_trivial": summary["all_48_exceptional_residues_square_trivial"],
        "next_exact_leaf": cert["next_exact_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
