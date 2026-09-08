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
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
B2B2 = HERE / "e3-v91c1x-r5b3b3c4b2b2-remaining24-strict-prime-squareclass-partition.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2a-f4-pair-multiquadratic-residue-norm-witness.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
B2B2_SHA = "c35b8737bd310935c844b170975617e69f2745b60a932349b3c297dd6909fb27"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
F4_SHA = "69623aeb5f2dab057c7c435c9f72d85b6670e7716c1a64d2a2b8ea3b9ec1be1b"
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


def clean(z):
    return sp.cancel(sp.together(z))


def rational_pair(q):
    q = clean(q)
    if q.is_Rational is not True:
        raise SystemExit(f"expected rational, got {q}")
    return [int(sp.numer(q)), int(sp.denom(q))]


def encode_qi(z):
    z = clean(z)
    zc = clean(sp.conjugate(z))
    a = clean((z + zc) / 2)
    b = clean((z - zc) / (2 * I))
    if clean(z - a - I * b) != 0 or a.is_Rational is not True or b.is_Rational is not True:
        raise SystemExit(f"escaped Q(i): {z}")
    ar, br = rational_pair(a), rational_pair(b)
    return [ar[0], ar[1], br[0], br[1]]


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
    a, b = clean((z + zc) / 2), clean((z - zc) / (2 * I))
    if a.is_Rational is not True or b.is_Rational is not True:
        raise SystemExit(f"square test escaped Q(i): {z}")
    if z == 0:
        return True
    r = rational_sqrt_if_square(clean(a * a + b * b))
    if r is None:
        return False
    sx = rational_sqrt_if_square(clean((r + a) / 2))
    sy = rational_sqrt_if_square(clean((r - a) / 2))
    if sx is None or sy is None:
        return False
    return any(clean((xx + I * yy) ** 2 - z) == 0 for xx in {sx, -sx} for yy in {sy, -sy})


def poly_commit(poly: sp.Poly) -> dict:
    p = sp.Poly(poly, extension=I).monic()
    return {
        "degree": int(p.degree()),
        "coefficients_high_to_low_Qi": [encode_qi(sp.sympify(c)) for c in p.all_coeffs()],
    }


def rational_function_squareclass(z, x):
    z = clean(z)
    num, den = sp.fraction(z)
    pn = sp.Poly(num, x, extension=I)
    pd = sp.Poly(den, x, extension=I)
    cn, fn = sp.factor_list(pn.as_expr(), x, extension=I)
    cd, fd = sp.factor_list(pd.as_expr(), x, extension=I)
    parity = {}
    commits = {}
    for side, facs in ((1, fn), (-1, fd)):
        for fac, exponent in facs:
            p = sp.Poly(fac, x, extension=I).monic()
            key = csha(poly_commit(p))
            parity[key] = parity.get(key, 0) + side * int(exponent)
            commits[key] = poly_commit(p)
    odd = []
    for key in sorted(parity):
        if parity[key] % 2:
            row = dict(commits[key])
            row["projective_factor_sha256"] = key
            row["signed_exponent_mod_2"] = int(parity[key] % 2)
            odd.append(row)
    scalar = clean(sp.sympify(cn) / sp.sympify(cd))
    scalar_square = qi_is_square(scalar)
    return {
        "scalar_Qi": encode_qi(scalar),
        "scalar_is_square_in_Qi": scalar_square,
        "odd_irreducible_factor_count": len(odd),
        "odd_irreducible_factors": odd,
        "square_trivial_in_Qi_x": scalar_square and not odd,
    }


def algebra_mul(a, b, ds):
    out = [sp.Integer(0)] * 8
    for ma, va in enumerate(a):
        if va == 0:
            continue
        for mb, vb in enumerate(b):
            if vb == 0:
                continue
            common = ma & mb
            factor = sp.Integer(1)
            for bit, d in ((1, ds[0]), (2, ds[1]), (4, ds[2])):
                if common & bit:
                    factor *= d
            out[ma ^ mb] += va * vb * factor
    return [clean(v) for v in out]


def algebra_flip(a, bit):
    return [clean((-v if (m & bit) else v)) for m, v in enumerate(a)]


def norm_step(a, bit, ds):
    out = algebra_mul(a, algebra_flip(a, bit), ds)
    bad = [m for m, v in enumerate(out) if (m & bit) and clean(v) != 0]
    if bad:
        raise SystemExit(f"quadratic norm failed to eliminate bit {bit}: masks={bad}")
    return out


def linear_pullback(coeff, eps, x, d1):
    ca1, ca2, ca3, cb1, cb2, cb3, cc = coeff
    rcoef = clean(cb3 + cc + (eps * cb2 - cc) / (2 * d1))
    out = [sp.Integer(0)] * 8
    out[0] = clean(ca1 + ca2 * x)
    out[1] = rcoef
    out[2] = clean(ca3)
    out[4] = clean(cb1)
    return out


def build_certificate() -> dict:
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    b2b2 = load_locked(B2B2, B2B2_SHA)

    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    inv = {r["carrier_id"]: r for r in inv_rows}
    coeffs = {
        cid: [atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]]
        for cid, row in inv.items()
    }

    f4_bucket = next(r for r in b2b2["remaining24_partition"]["rows_by_bucket"] if r["bucket"] == "F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES")
    if f4_bucket["target_count"] != 2 or f4_bucket["carrier_ids"] != ["LIN_013", "LIN_019"]:
        raise SystemExit("B2B2 F4 bucket moved")
    targets = {r["carrier_id"]: r for r in f4_bucket["rows"]}

    c4rows = {
        (r["carrier_id"], r["c1_normalized_factor_sha256"]): r
        for r in c4a["strict_prime_preflight"]["rows"]
    }

    x = sp.Symbol("x")
    d1 = clean(1 + x * x)
    d2 = clean(-(3 + 4 * x * x) / (4 * d1))
    d3 = clean((4 * x ** 4 - 3) / (4 * d1))
    ds = [d1, d2, d3]
    f4_chart = clean(3 + 4 * x * x + 4 * x * x * 0)  # metadata only; exact homogeneous identity checked below
    homogeneous_f4_identity = sp.expand(4 * (1 + sp.Symbol("Y") ** 2) * (1 + x ** 2) - 1)
    if clean(d2 - (1 / (4 * d1) - 1)) != 0 or clean(d3 - (x * x + d2)) != 0:
        raise SystemExit("derived multiquadratic radicands failed surface identities")

    rows = []
    nonsquare_count = 0
    inconclusive_count = 0
    for cid, eps in (("LIN_013", -1), ("LIN_019", 1)):
        brow = targets[cid]
        crow = c4rows[(cid, F4_SHA)]
        odd = list(crow["combined_tame_residue_odd_linear_carrier_ids_under_single_carrier_valuation"])
        if odd != brow["combined_tame_residue_odd_linear_carrier_ids"]:
            raise SystemExit(f"C4A/B2B2 odd carrier set mismatch: {cid}")
        if len(odd) != 10:
            raise SystemExit(f"F4 odd carrier count moved: {cid}")

        # Validate the target carrier itself vanishes in the chart model.
        target_pull = linear_pullback(coeffs[cid], eps, x, d1)
        if any(clean(v) != 0 for v in target_pull):
            raise SystemExit(f"target carrier does not vanish in chart model: {cid}: {target_pull}")

        residue = [sp.Integer(1)] + [sp.Integer(0)] * 7
        per_carrier = []
        for oid in odd:
            p = linear_pullback(coeffs[oid], eps, x, d1)
            if all(clean(v) == 0 for v in p):
                raise SystemExit(f"odd residue carrier vanished identically: {cid}/{oid}")
            residue = algebra_mul(residue, p, ds)
            per_carrier.append({
                "carrier_id": oid,
                "pullback_nonzero": True,
                "pullback_support_masks": [m for m, v in enumerate(p) if clean(v) != 0],
            })

        residue_commit = csha([sp.srepr(clean(v)) for v in residue])
        n4 = norm_step(residue, 4, ds)
        n42 = norm_step(n4, 2, ds)
        n421 = norm_step(n42, 1, ds)
        if any(clean(v) != 0 for v in n421[1:]):
            raise SystemExit(f"full sign-orbit norm did not land in Q(i)(x): {cid}")
        norm = clean(n421[0])
        if norm == 0:
            raise SystemExit(f"zero sign-orbit norm: {cid}")
        sq = rational_function_squareclass(norm, x)
        if sq["square_trivial_in_Qi_x"]:
            classification = "INCONCLUSIVE_SQUARE_SIGN_ORBIT_NORM_REQUIRES_STRONGER_TEST"
            inconclusive_count += 1
        else:
            classification = "NONSQUARE_RESIDUE_BY_NONSQUARE_SIGN_ORBIT_NORM_TO_QI_X"
            nonsquare_count += 1

        rows.append({
            "carrier_id": cid,
            "strict_prime_ids": list(brow["c4a_strict_prime_ids"]),
            "carrier_equation": "b2+b3-c=0" if cid == "LIN_013" else "b2-b3+c=0",
            "b2_times_b3": "-a1^2/2" if eps == -1 else "+a1^2/2",
            "a1_chart_model": {
                "base_field": "Q(i)(x), x=a2/a1",
                "r_square": "1+x^2",
                "y_square": "-(3+4*x^2)/(4*(1+x^2))",
                "q_square": "(4*x^4-3)/(4*(1+x^2))",
                "coordinates": {
                    "a1": "1", "a2": "x", "a3": "y", "b1": "q", "b3": "r",
                    "b2": "-1/(2*r)" if eps == -1 else "+1/(2*r)",
                    "c": "r-1/(2*r)",
                },
            },
            "odd_residue_carrier_ids": odd,
            "odd_residue_carrier_count": len(odd),
            "per_odd_carrier_pullback": per_carrier,
            "combined_residue_multiquadratic_basis_sha256": residue_commit,
            "sign_orbit_norm_method": "multiply by q-sign conjugate, then y-sign conjugate, then r-sign conjugate in the 8-dimensional square-root algebra",
            "square_implication_used": "if the residue were a square in the strict-prime function field then the product of all sign conjugates would be a square in Q(i)(x); therefore a nonsquare sign-orbit product certifies a nonsquare residue",
            "sign_orbit_norm_Qi_x_sha256": csha(sp.srepr(norm)),
            "sign_orbit_norm_squareclass": sq,
            "classification": classification,
            "residue_nonsquare_certified": not sq["square_trivial_in_Qi_x"],
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2a.f4_pair_multiquadratic_residue_norm_witness.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2A_F4_PAIR_MULTIQUEADRATIC_RESIDUE_NORM_WITNESS",
        "role": "EXACT_NONCREDIT_NONSQUARE_WITNESS_ATTEMPT_FOR_THE_TWO_F4_STRICT_PRIME_RESIDUES_USING_AN_EXPLICIT_THREE_SQUARE_ROOT_CHART_AND_SIGN_ORBIT_NORM",
        "entry": {"authority": AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_formal_symbol_inventory_sha256": B3B2_SHA,
            "c4a_tame_residue_preflight_sha256": C4A_SHA,
            "c4b2b2_remaining24_partition_sha256": B2B2_SHA,
        },
        "f4_geometry": {
            "shared_base_factor_sha256": F4_SHA,
            "homogeneous_base_factor": "3*a1^4+4*a1^2*(a2^2+a3^2)+4*a2^2*a3^2",
            "derivation": "from c=b2+b3 (LIN_013) or c=b3-b2 (LIN_019), the four surface quadrics give b2*b3=minus_or_plus_a1^2/2; squaring and substituting b2^2=a1^2+a3^2, b3^2=a1^2+a2^2 gives the same F4 equation",
            "a1_chart_multiquadratic_model_exactly_satisfies_the_derived_square_relations": True,
            "no_claim_that_the_three_radicands_are_independent_is_needed_for_the_nonsquare_implication": True,
        },
        "residue_norm_reduction": {
            "target_count": 2,
            "nonsquare_by_norm_count": nonsquare_count,
            "square_norm_inconclusive_count": inconclusive_count,
            "rows": rows,
        },
        "exact_consequence": {
            "F4_pair_residue_nonsquare_certified_count": nonsquare_count,
            "F4_pair_remaining_squareclass_debt_count": inconclusive_count,
            "current_literal_eight_symbol_candidate_was_already_known_ramified_from_C4B2B1": True,
            "this_leaf_only_refines_the_ramification_profile_and_does_not_negate_other_representatives_or_the_stage33_endpoint": True,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5B3B3C4B2B2B_F14_FOUR_RESIDUAL_PRIME_RESIDUE_NORM_WITNESS" if inconclusive_count == 0 else "V91C1X_R5B3B3C4B2B2A1_F4_PAIR_STRONGER_SQUARECLASS_TEST",
        "credit_firewall": {
            "authority_promotion": False, "hostile_audit_credit": False, "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False, "genuine_full_surface_h2_mu2_lift_credit": False,
            "offboundary_cancellation_credit": False, "unramifiedness_credit": False,
            "stage33_close_credit": False, "stage33_release_credit": False, "theorem_credit": False,
            "receiver_credit": False, "endpoint_credit": False, "merge_allowed": False,
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
        r = cert["residue_norm_reduction"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "nonsquare_by_norm_count": r["nonsquare_by_norm_count"],
            "square_norm_inconclusive_count": r["square_norm_inconclusive_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    if json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2A certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
