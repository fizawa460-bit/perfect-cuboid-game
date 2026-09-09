#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

import sympy as sp

import materialize_e3_v91c1x_r5b3b3c4b2b2a_f4_pair_multiquadratic_residue_norm_witness as slow


def squareclass_product(norms, x):
    """Exact squareclass of a product, factoring each smaller factor separately."""
    parity = {}
    commits = {}
    scalar = sp.Integer(1)
    for z in norms:
        z = slow.clean(z)
        num, den = sp.fraction(z)
        pn = sp.Poly(num, x, extension=slow.I)
        pd = sp.Poly(den, x, extension=slow.I)
        cn, fn = sp.factor_list(pn.as_expr(), x, extension=slow.I)
        cd, fd = sp.factor_list(pd.as_expr(), x, extension=slow.I)
        scalar = slow.clean(scalar * sp.sympify(cn) / sp.sympify(cd))
        for side, facs in ((1, fn), (-1, fd)):
            for fac, exponent in facs:
                p = sp.Poly(fac, x, extension=slow.I).monic()
                key = slow.csha(slow.poly_commit(p))
                parity[key] = parity.get(key, 0) + side * int(exponent)
                commits[key] = slow.poly_commit(p)

    odd = []
    for key in sorted(parity):
        if parity[key] % 2:
            row = dict(commits[key])
            row["projective_factor_sha256"] = key
            row["signed_exponent_mod_2"] = int(parity[key] % 2)
            odd.append(row)
    scalar_square = slow.qi_is_square(scalar)
    return {
        "scalar_Qi": slow.encode_qi(scalar),
        "scalar_is_square_in_Qi": scalar_square,
        "odd_irreducible_factor_count": len(odd),
        "odd_irreducible_factors": odd,
        "square_trivial_in_Qi_x": scalar_square and not odd,
    }


def carrier_sign_orbit_norm(p, ds, cid, oid):
    n4 = slow.norm_step(p, 4, ds)
    n42 = slow.norm_step(n4, 2, ds)
    n421 = slow.norm_step(n42, 1, ds)
    if any(slow.clean(v) != 0 for v in n421[1:]):
        raise SystemExit(f"per-carrier sign-orbit norm did not land in Q(i)(x): {cid}/{oid}")
    norm = slow.clean(n421[0])
    if norm == 0:
        raise SystemExit(f"zero per-carrier sign-orbit norm: {cid}/{oid}")
    return norm


def build_certificate() -> dict:
    b3b2 = slow.load_locked(slow.B3B2, slow.B3B2_SHA)
    c4a = slow.load_locked(slow.C4A, slow.C4A_SHA)
    b2b2 = slow.load_locked(slow.B2B2, slow.B2B2_SHA)

    inv_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    inv = {r["carrier_id"]: r for r in inv_rows}
    coeffs = {
        cid: [slow.atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]]
        for cid, row in inv.items()
    }

    f4_bucket = next(
        r for r in b2b2["remaining24_partition"]["rows_by_bucket"]
        if r["bucket"] == "F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES"
    )
    if f4_bucket["target_count"] != 2 or f4_bucket["carrier_ids"] != ["LIN_013", "LIN_019"]:
        raise SystemExit("B2B2 F4 bucket moved")
    targets = {r["carrier_id"]: r for r in f4_bucket["rows"]}

    c4rows = {
        (r["carrier_id"], r["c1_normalized_factor_sha256"]): r
        for r in c4a["strict_prime_preflight"]["rows"]
    }

    x = sp.Symbol("x")
    d1 = slow.clean(1 + x * x)
    d2 = slow.clean(-(3 + 4 * x * x) / (4 * d1))
    d3 = slow.clean((4 * x ** 4 - 3) / (4 * d1))
    ds = [d1, d2, d3]
    if slow.clean(d2 - (1 / (4 * d1) - 1)) != 0 or slow.clean(d3 - (x * x + d2)) != 0:
        raise SystemExit("derived multiquadratic radicands failed surface identities")

    rows = []
    nonsquare_count = 0
    inconclusive_count = 0
    for cid, eps in (("LIN_013", -1), ("LIN_019", 1)):
        brow = targets[cid]
        crow = c4rows[(cid, slow.F4_SHA)]
        odd = list(crow["combined_tame_residue_odd_linear_carrier_ids_under_single_carrier_valuation"])
        if odd != brow["combined_tame_residue_odd_linear_carrier_ids"]:
            raise SystemExit(f"C4A/B2B2 odd carrier set mismatch: {cid}")
        if len(odd) != 10:
            raise SystemExit(f"F4 odd carrier count moved: {cid}")

        target_pull = slow.linear_pullback(coeffs[cid], eps, x, d1)
        if any(slow.clean(v) != 0 for v in target_pull):
            raise SystemExit(f"target carrier does not vanish in chart model: {cid}: {target_pull}")

        residue = [sp.Integer(1)] + [sp.Integer(0)] * 7
        per_carrier = []
        carrier_norms = []
        for oid in odd:
            p = slow.linear_pullback(coeffs[oid], eps, x, d1)
            if all(slow.clean(v) == 0 for v in p):
                raise SystemExit(f"odd residue carrier vanished identically: {cid}/{oid}")
            residue = slow.algebra_mul(residue, p, ds)
            carrier_norms.append(carrier_sign_orbit_norm(p, ds, cid, oid))
            per_carrier.append({
                "carrier_id": oid,
                "pullback_nonzero": True,
                "pullback_support_masks": [m for m, v in enumerate(p) if slow.clean(v) != 0],
            })

        residue_commit = slow.csha([sp.srepr(slow.clean(v)) for v in residue])
        norm = sp.Integer(1)
        for carrier_norm in carrier_norms:
            norm = slow.clean(norm * carrier_norm)
        sq = squareclass_product(carrier_norms, x)
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
            "sign_orbit_norm_Qi_x_sha256": slow.csha(sp.srepr(norm)),
            "sign_orbit_norm_squareclass": sq,
            "classification": classification,
            "residue_nonsquare_certified": not sq["square_trivial_in_Qi_x"],
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2a.f4_pair_multiquadratic_residue_norm_witness.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2A_F4_PAIR_MULTIQUEADRATIC_RESIDUE_NORM_WITNESS",
        "role": "EXACT_NONCREDIT_NONSQUARE_WITNESS_ATTEMPT_FOR_THE_TWO_F4_STRICT_PRIME_RESIDUES_USING_AN_EXPLICIT_THREE_SQUARE_ROOT_CHART_AND_SIGN_ORBIT_NORM",
        "entry": {"authority": slow.AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_formal_symbol_inventory_sha256": slow.B3B2_SHA,
            "c4a_tame_residue_preflight_sha256": slow.C4A_SHA,
            "c4b2b2_remaining24_partition_sha256": slow.B2B2_SHA,
        },
        "f4_geometry": {
            "shared_base_factor_sha256": slow.F4_SHA,
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
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = slow.csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        slow.OUT.write_text(text, encoding="utf-8")
        r = cert["residue_norm_reduction"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "nonsquare_by_norm_count": r["nonsquare_by_norm_count"],
            "square_norm_inconclusive_count": r["square_norm_inconclusive_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
            "implementation": "multiplicative_per_carrier_sign_orbit_norm",
        }, sort_keys=True))
        return
    if not slow.OUT.exists():
        raise SystemExit(f"missing materialized certificate: {slow.OUT}")
    if json.loads(slow.OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2A certificate differs from exact multiplicative rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
