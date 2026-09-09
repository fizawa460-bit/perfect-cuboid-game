#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C4B2B2C1 = HERE / "e3-v91c1x-r5b3b3c4b2b2c1-inherited-direct-support-primality-recheck.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2c2-lin024-actual-four-component-prime-incidence.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C4B2B2C1_SHA = "64e25e200f4f0188731a6c85e1e69e6eae85a759403ac0d984309b3dca881b39"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved: {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def pstr(expr: sp.Expr) -> str:
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def canonical_groebner(gens: list[sp.Expr], variables: tuple[sp.Symbol, ...]) -> tuple[str, list[str], sp.GroebnerBasis]:
    gb = sp.groebner(gens, *variables, order="grevlex", extension=I)
    basis = [sp.srepr(sp.expand(poly.as_expr())) for poly in gb.polys]
    return csha(basis), basis, gb


def linear_expr(encoded: list, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    if len(encoded) != 7:
        raise SystemExit(f"unexpected carrier coefficient length: {len(encoded)}")
    return sp.expand(sum(b3.decode_qi(q) * v for q, v in zip(encoded, variables)))


def build_member_exponents(carrier_rows: list[dict], components: list[str]):
    pi = {d: defaultdict(int) for d in components}
    ff = {d: defaultdict(int) for d in components}
    for row in carrier_rows:
        cid = row["carrier_id"]
        for app in row["appearances"]:
            d = app["symbol_component"]
            if d not in pi:
                raise SystemExit(f"unexpected formal symbol component: {d}")
            target = pi if app["member"] == "pi_D" else ff if app["member"] == "f_D" else None
            if target is None:
                raise SystemExit(f"unexpected symbol member: {app['member']}")
            target[d][cid] += int(app["exponent"])
    return pi, ff


def residue_parity_for_valuation_vector(carrier_ids, components, pi, ff, valuation):
    odd = defaultdict(int)
    vpi_by_component = {}
    vf_by_component = {}
    sign_parity = 0
    for d in components:
        vpi = sum(int(pi[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        vf = sum(int(ff[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        vpi_by_component[d] = vpi
        vf_by_component[d] = vf
        sign_parity ^= (vpi * vf) & 1
        for cid in carrier_ids:
            e = int(pi[d].get(cid, 0)) * vf - int(ff[d].get(cid, 0)) * vpi
            odd[cid] ^= e & 1
    return sorted(cid for cid in carrier_ids if odd[cid]), sign_parity, vpi_by_component, vf_by_component


def factor_signature(poly: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[dict]:
    unit, facs = sp.factor_list(sp.expand(poly), *variables, extension=I)
    rows = []
    for f, e in facs:
        q = sp.Poly(f, *variables, extension=I)
        rows.append({
            "degree": int(q.total_degree()),
            "exponent": int(e),
            "factor_sha256": csha(sp.srepr(sp.expand(q.as_expr()))),
        })
    return sorted(rows, key=lambda r: (r["degree"], r["factor_sha256"])), pstr(sp.sympify(unit))


def build() -> dict:
    b3b2 = load(B3B2, B3B2_SHA)
    c4a = load(C4A, C4A_SHA)
    c1 = load(C4B2B2C1, C4B2B2C1_SHA)
    if not c1["lin024_exact_boundary"]["the_two_C3_ids_are_not_prime_exact_residue_field_targets"]:
        raise SystemExit("C4B2B2C1 LIN024 primality boundary moved")
    if c1["next_exact_leaf"] != "V91C1X_R5B3B3C4B2B2C2_LIN024_EXACT_FOUR_COMPONENT_PRIME_REFINEMENT_AND_COMPONENTWISE_RESIDUE_SQUARECLASS":
        raise SystemExit("C4B2B2C1 next-leaf gate moved")

    formal = b3b2["formal_tame_symbol_sum"]
    components = list(formal["component_ids_in_source_order"])
    carrier_rows = list(b3b2["finite_linear_carrier_inventory"]["carrier_rows"])
    carrier_ids = [r["carrier_id"] for r in carrier_rows]
    if carrier_ids != list(c4a["formal_symbol_input"]["carrier_ids"]):
        raise SystemExit("C4A/B3B2 formal carrier ordering moved")
    if len(carrier_ids) != len(set(carrier_ids)):
        raise SystemExit("duplicate formal carrier id")
    inv = {r["carrier_id"]: r for r in carrier_rows}
    if "LIN_024" not in inv:
        raise SystemExit("LIN_024 escaped formal carrier inventory")
    pi, ff = build_member_exponents(carrier_rows, components)

    a1, a2, a3, b1, b2, b3v, cv = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    Q = [
        a1**2 + a2**2 - b3v**2,
        a2**2 + a3**2 - b1**2,
        a1**2 + a3**2 - b2**2,
        a1**2 + a2**2 + a3**2 - cv**2,
    ]
    carrier_expr = {cid: linear_expr(inv[cid]["normalized_coefficients_Qi"], variables) for cid in carrier_ids}
    lin024 = sp.Poly(carrier_expr["LIN_024"], *variables, extension=I)
    terms = lin024.terms()
    if len(terms) != 1 or terms[0][0] != (0, 0, 0, 0, 1, 0, 0):
        raise SystemExit(f"LIN_024 is no longer the b2 axis carrier: {carrier_expr['LIN_024']}")

    # Global quotient after b2=0, a1=+-i*a3 and c=+-a2 is
    # Q(i)[a2,a3,b1,b3]/(b1^2-(a2^2+a3^2), b3^2-(a2^2-a3^2)).
    # The two radicands have disjoint odd linear factor support over Q(i), hence
    # independent squareclasses.  Sequential quadratic extension therefore gives a domain.
    R = sp.expand(a2**2 + a3**2)
    S = sp.expand(a2**2 - a3**2)
    rf, ru = factor_signature(R, (a2, a3))
    sf, su = factor_signature(S, (a2, a3))
    rsf, rsu = factor_signature(sp.expand(R*S), (a2, a3))
    if len(rf) != 2 or len(sf) != 2 or len(rsf) != 4:
        raise SystemExit("LIN024 component radicand factor pattern moved")
    if any(r["degree"] != 1 or r["exponent"] != 1 for r in rf + sf + rsf):
        raise SystemExit("LIN024 component radicand odd-factor proof moved")
    if sp.gcd(sp.Poly(R, a2, a3, extension=I), sp.Poly(S, a2, a3, extension=I)).total_degree() != 0:
        raise SystemExit("LIN024 component radicands lost coprimality")
    common_domain_proof = {
        "quotient_presentation": "Q(i)[a2,a3,b1,b3]/(b1^2-(a2^2+a3^2), b3^2-(a2^2-a3^2))",
        "first_radicand_factor_signature": rf,
        "second_radicand_factor_signature": sf,
        "product_radicand_factor_signature": rsf,
        "radicands_coprime_over_Qi": True,
        "first_radicand_nonsquare": True,
        "second_radicand_nonsquare": True,
        "second_over_first_squareclass_nonsquare": True,
        "squareclass_rank_two": True,
        "sequential_quadratic_extension_is_domain": True,
        "actual_component_ideal_is_prime": True,
    }

    support_specs = [
        {"support": "a1+i*a3", "support_expr": a1 + I*a3, "old_support_id": "537ee4d04a103c9082958b087b663f1a1fa319ecd2c0ad7fbfface8a5cbe6767", "c1_factor_sha256": "72eb2cb8280203a24bc841d55bdea12b0f2920a9fa4bb3dda4555e5150396513"},
        {"support": "a1-i*a3", "support_expr": a1 - I*a3, "old_support_id": "914b682af4aa0f52d029122538b95c9961e86eb738c567495947efbe21166c11", "c1_factor_sha256": "3c29ee732fe64c83d9b7523c352d2a14c6eaa1fceb4dca6fd041c407c96153e7"},
    ]

    out_rows = []
    extra_incidence_components = 0
    single_carrier_components = 0
    distinct_prime_ids = set()
    for spec in support_specs:
        for csign in (1, -1):
            c_rel = sp.expand(cv - csign*a2)
            gens = Q + [b2, spec["support_expr"], c_rel]
            prime_id, basis, gb = canonical_groebner(gens, variables)
            distinct_prime_ids.add(prime_id)
            containing = []
            remainder_hashes = {}
            for cid in carrier_ids:
                rem = sp.expand(gb.reduce(carrier_expr[cid])[1])
                remainder_hashes[cid] = csha(sp.srepr(rem))
                if rem == 0:
                    containing.append(cid)
            if "LIN_024" not in containing:
                raise SystemExit(f"actual LIN024 component lost LIN_024 carrier: {spec['support']}/{csign}")
            # Every contained formal carrier is linear and belongs to the degree-one part
            # of this homogeneous prime ideal, so its DVR order is exactly one; it cannot
            # lie in P^2, whose nonzero homogeneous elements have degree >=2.
            valuation = {cid: (1 if cid in containing else 0) for cid in carrier_ids}
            odd, sign, vpi, vf = residue_parity_for_valuation_vector(carrier_ids, components, pi, ff, valuation)
            extras = sorted(cid for cid in containing if cid != "LIN_024")
            if extras:
                extra_incidence_components += 1
            else:
                single_carrier_components += 1
            out_rows.append({
                "old_support_id": spec["old_support_id"],
                "c1_factor_sha256": spec["c1_factor_sha256"],
                "base_support": spec["support"],
                "c_branch": "c=a2" if csign == 1 else "c=-a2",
                "actual_prime_id": prime_id,
                "actual_prime_generators": [pstr(g) for g in gens],
                "canonical_groebner_basis_sha256": csha(basis),
                "quotient_domain_proof": common_domain_proof,
                "formal_carrier_incidence": {
                    "containing_carrier_ids": sorted(containing),
                    "containing_carrier_count": len(containing),
                    "extra_carrier_ids_beyond_LIN024": extras,
                    "single_carrier_valuation_model_survives": not extras,
                    "all_containing_linear_carrier_DVR_orders": 1,
                    "full_remainder_vector_sha256": csha(remainder_hashes),
                },
                "generalized_tame_residue_parity": {
                    "valuation_nonzero_carrier_ids": sorted(containing),
                    "odd_linear_carrier_ids": odd,
                    "odd_linear_carrier_count": len(odd),
                    "formal_linear_factor_parity_zero": not odd,
                    "tame_sign_parity": sign,
                    "minus_one_square_over_Qi": True,
                    "v_pi_by_symbol_component": vpi,
                    "v_f_by_symbol_component": vf,
                },
            })

    if len(distinct_prime_ids) != 4 or len(out_rows) != 4:
        raise SystemExit(f"LIN024 actual component prime count moved: {len(distinct_prime_ids)}")
    if extra_incidence_components:
        next_leaf = "V91C1X_R5B3B3C4B2B2C3_LIN024_ACTUAL_COMPONENT_LOCAL_UNIT_RATIO_TAME_RESIDUE_RECONSTRUCTION"
        consequence = "EXTRA_FORMAL_CARRIER_INCIDENCE_REQUIRES_LOCAL_UNIT_RATIO_RECONSTRUCTION_BEFORE_RESIDUE_SQUARECLASS_TEST"
    else:
        next_leaf = "V91C1X_R5B3B3C4B2B2C3_LIN024_FOUR_COMPONENT_BIQUADRATIC_RESIDUE_NORM_TEST"
        consequence = "SINGLE_CARRIER_VALUATION_SURVIVES_ON_ALL_FOUR_COMPONENTS_READY_FOR_BIQUADRATIC_RESIDUE_NORM_TEST"

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2c2.lin024_actual_four_component_prime_incidence.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2C2_LIN024_ACTUAL_FOUR_COMPONENT_PRIME_INCIDENCE",
        "role": "EXACT_NONCREDIT_REFINEMENT_OF_THE_TWO_NONPRIME_LIN024_BASE_SUPPORT_LABELS_TO_FOUR_ACTUAL_HEIGHT_ONE_COMPONENT_PRIMES_WITH_FULL_FORMAL_CARRIER_INCIDENCE_AND_GENERALIZED_TAME_PARITY_REPLAY",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "c4a_tame_residue_preflight_sha256": C4A_SHA,
            "c4b2b2c1_direct_support_primality_recheck_sha256": C4B2B2C1_SHA,
        },
        "component_refinement": {
            "old_support_label_count": 2,
            "actual_height_one_prime_count": 4,
            "all_four_actual_component_ideals_prime": True,
            "common_domain_proof": common_domain_proof,
            "rows": out_rows,
        },
        "incidence_summary": {
            "component_count": 4,
            "components_with_extra_formal_carrier_incidence": extra_incidence_components,
            "components_with_only_LIN024_formal_carrier": single_carrier_components,
            "old_two_support_ids_are_replaced_by_four_actual_prime_ids_for_residue_field_arithmetic": True,
        },
        "exact_consequence": {
            "degree16_F4_F14_nonsquare_results_unchanged": True,
            "lin024_actual_prime_refinement_complete": True,
            "lin024_component_incidence_replayed_against_all_formal_carriers": True,
            "lin024_generalized_tame_parity_recomputed_on_all_four_actual_primes": True,
            "next_branch_reason": consequence,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": next_leaf,
        "credit_firewall": {
            "authority_promotion": False,
            "authority_demotion_claim": False,
            "hostile_audit_credit": False,
            "marked_brauer_image_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "actual_height_one_prime_count": cert["component_refinement"]["actual_height_one_prime_count"],
            "components_with_extra_formal_carrier_incidence": cert["incidence_summary"]["components_with_extra_formal_carrier_incidence"],
            "next_exact_leaf": cert["next_exact_leaf"],
            "certificate_sha256": cert["canonical_sha256"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    if json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2C2 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
