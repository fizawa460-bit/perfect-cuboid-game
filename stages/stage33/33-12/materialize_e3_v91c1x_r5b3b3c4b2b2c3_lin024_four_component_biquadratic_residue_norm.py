#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3c4b1e_1757_refinement_unit_or_cech_cochain_preflight as _unused_guard  # noqa: F401
import materialize_e3_v91c1x_r5b3b3c4a_tame_residue_parity_and_cross_carrier_preflight as c4a_mod
import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C2 = HERE / "e3-v91c1x-r5b3b3c4b2b2c2-lin024-actual-four-component-prime-incidence.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2c3-lin024-four-component-biquadratic-residue-norm.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C2_SHA = "68d1be09543e79e210dc3e1e13d9f3e9cee3eb08d1b576238b5889e2a995e59f"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I
SPLIT_PRIMES = [5, 13, 17, 29, 37, 41, 53, 61]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def pstr(expr: sp.Expr) -> str:
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def linear_expr(encoded: list, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    return sp.expand(sum(b3.decode_qi(q) * v for q, v in zip(encoded, variables)))


def mul(z, w, R, S):
    A, B, C, D = z
    a, b, c, d = w
    return tuple(sp.expand(v) for v in (
        A*a + B*b*R + C*c*S + D*d*R*S,
        A*b + B*a + C*d*S + D*c*S,
        A*c + C*a + B*d*R + D*b*R,
        A*d + D*a + B*c + C*b,
    ))


def linear_to_basis(expr: sp.Expr, r: sp.Symbol, s: sp.Symbol):
    expr = sp.expand(expr)
    A = sp.expand(expr.subs({r: 0, s: 0}))
    B = sp.expand(sp.diff(expr, r).subs({r: 0, s: 0}))
    C = sp.expand(sp.diff(expr, s).subs({r: 0, s: 0}))
    D = sp.expand(sp.diff(sp.diff(expr, r), s).subs({r: 0, s: 0}))
    recon = sp.expand(A + B*r + C*s + D*r*s)
    if sp.expand(expr - recon) != 0:
        raise SystemExit(f"restriction escaped biquadratic basis: {expr}")
    return A, B, C, D


def gaussian_den_lcm(poly: sp.Poly) -> int:
    den = 1
    for coeff in poly.all_coeffs():
        re, im = sp.expand(coeff).as_real_imag(deep=True)
        if not (re.is_Rational and im.is_Rational):
            raise SystemExit(f"non-Gaussian-rational norm coefficient: {coeff}")
        den = int(sp.ilcm(den, int(sp.denom(re)), int(sp.denom(im))))
    return den


def i_root_mod_p(p: int) -> int:
    for q in range(1, p):
        if (q*q + 1) % p == 0:
            return q
    raise SystemExit(f"prime is not split in Q(i): {p}")


def monic_factor_record(f, x, p: int, exponent: int):
    q = sp.Poly(f, x, modulus=p).monic()
    coeffs = [int(c) % p for c in q.all_coeffs()]
    return {
        "degree": int(q.degree()),
        "exponent": int(exponent),
        "exponent_mod_2": int(exponent) & 1,
        "monic_coefficients_mod_p": coeffs,
        "monic_factor_sha256": csha(coeffs),
    }


def reduction_witness(norm_expr: sp.Expr, x: sp.Symbol):
    q0 = sp.Poly(sp.expand(norm_expr), x, extension=I)
    degree0 = int(q0.degree())
    den = gaussian_den_lcm(q0)
    scaled = sp.expand(norm_expr * den)
    trials = []
    for p in SPLIT_PRIMES:
        if den % p == 0:
            trials.append({"rational_prime": p, "usable_good_reduction": False, "reason": "denominator clearing scalar divisible by p"})
            continue
        ii = i_root_mod_p(p)
        reduced_expr = sp.expand(scaled.subs(I, ii))
        q = sp.Poly(reduced_expr, x, modulus=p)
        if q.is_zero or int(q.degree()) != degree0:
            trials.append({"rational_prime": p, "i_image": ii, "usable_good_reduction": False, "reason": "norm degree dropped or reduction vanished"})
            continue
        _unit, facs = sp.factor_list(q.as_expr(), modulus=p)
        rows = [monic_factor_record(f, x, p, e) for f, e in facs]
        odd_positive = [r for r in rows if r["degree"] > 0 and r["exponent_mod_2"] == 1]
        trial = {
            "rational_prime": p,
            "i_image": ii,
            "i_image_squared_plus_one_zero_mod_p": (ii*ii + 1) % p == 0,
            "usable_good_reduction": True,
            "norm_degree_mod_p": int(q.degree()),
            "factorization": rows,
            "odd_positive_degree_factor_count": len(odd_positive),
            "nonsquare_mod_split_prime_by_odd_factor": bool(odd_positive),
        }
        trials.append(trial)
        if odd_positive:
            return True, trials, den, degree0
    return False, trials, den, degree0


def build() -> dict:
    b3b2 = load(B3B2, B3B2_SHA)
    c4a = load(C4A, C4A_SHA)
    c2 = load(C2, C2_SHA)
    if c2["next_exact_leaf"] != "V91C1X_R5B3B3C4B2B2C3_LIN024_FOUR_COMPONENT_BIQUADRATIC_RESIDUE_NORM_TEST":
        raise SystemExit(f"C2 next-leaf gate moved: {c2['next_exact_leaf']}")
    if c2["incidence_summary"]["components_with_extra_formal_carrier_incidence"] != 0:
        raise SystemExit("LIN024 no longer has single-formal-carrier incidence on every component")
    if c2["component_refinement"]["actual_height_one_prime_count"] != 4:
        raise SystemExit("LIN024 actual component count moved")
    if not c2["component_refinement"]["all_four_actual_component_ideals_prime"]:
        raise SystemExit("LIN024 actual component primality gate lost")

    carrier_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    inv = {r["carrier_id"]: r for r in carrier_rows}
    carrier_ids = [r["carrier_id"] for r in carrier_rows]
    if carrier_ids != list(c4a["formal_symbol_input"]["carrier_ids"]):
        raise SystemExit("B3B2/C4A formal carrier inventory moved")

    a1, a2, a3, b1, b2, b3v, cv = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    x, r, s = sp.symbols("x r s")
    carrier_expr = {cid: linear_expr(inv[cid]["normalized_coefficients_Qi"], variables) for cid in carrier_ids}
    R = x**2 + 1
    S = x**2 - 1

    rows = []
    nonsquare_count = 0
    for comp in c2["component_refinement"]["rows"]:
        incidence = comp["formal_carrier_incidence"]
        parity = comp["generalized_tame_residue_parity"]
        if incidence["containing_carrier_ids"] != ["LIN_024"] or incidence["extra_carrier_ids_beyond_LIN024"]:
            raise SystemExit(f"component incidence escaped single-carrier model: {comp['actual_prime_id']}")
        odd_ids = list(parity["odd_linear_carrier_ids"])
        if len(odd_ids) != 10 or "LIN_024" in odd_ids:
            raise SystemExit(f"LIN024 odd residue carrier pattern moved: {odd_ids}")
        if parity["valuation_nonzero_carrier_ids"] != ["LIN_024"]:
            raise SystemExit("LIN024 valuation vector moved")

        if comp["base_support"] == "a1+i*a3":
            a1_value = -I
        elif comp["base_support"] == "a1-i*a3":
            a1_value = I
        else:
            raise SystemExit(f"unexpected LIN024 support: {comp['base_support']}")
        if comp["c_branch"] == "c=a2":
            csign = 1
        elif comp["c_branch"] == "c=-a2":
            csign = -1
        else:
            raise SystemExit(f"unexpected LIN024 c branch: {comp['c_branch']}")

        subs = {a1: a1_value, a2: x, a3: 1, b1: r, b2: 0, b3v: s, cv: csign*x}
        z = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
        factor_rows = []
        for cid in odd_ids:
            restricted = sp.expand(carrier_expr[cid].subs(subs))
            basis = linear_to_basis(restricted, r, s)
            if all(v == 0 for v in basis):
                raise SystemExit(f"odd residue carrier vanished identically on component: {comp['actual_prime_id']}/{cid}")
            z = mul(z, basis, R, S)
            factor_rows.append({
                "carrier_id": cid,
                "restricted_linear_form": pstr(restricted),
                "basis_coefficients_sha256": csha([pstr(v) for v in basis]),
            })

        rconj = (z[0], -z[1], z[2], -z[3])
        nr = mul(z, rconj, R, S)
        if sp.expand(nr[1]) != 0 or sp.expand(nr[3]) != 0:
            raise SystemExit("first quadratic norm retained r or r*s term")
        U, V = sp.expand(nr[0]), sp.expand(nr[2])
        total_norm = sp.expand(U**2 - V**2*S)
        if total_norm == 0:
            raise SystemExit("biquadratic residue norm vanished")
        nonsquare, trials, den, degree0 = reduction_witness(total_norm, x)
        nonsquare_count += int(nonsquare)
        rows.append({
            "actual_prime_id": comp["actual_prime_id"],
            "old_support_id": comp["old_support_id"],
            "base_support": comp["base_support"],
            "c_branch": comp["c_branch"],
            "residue_field_chart": {
                "dehomogenized": "a3=1",
                "base_variable": "x=a2",
                "first_radical": "r=b1, r^2=x^2+1",
                "second_radical": "s=b3, s^2=x^2-1",
                "biquadratic_basis": ["1", "r", "s", "r*s"],
            },
            "single_formal_carrier_valuation": {
                "only_nonzero_formal_carrier": "LIN_024",
                "valuation_of_LIN024": 1,
                "old_C4A_tame_parity_formula_applies_componentwise": True,
                "odd_residue_carrier_ids": odd_ids,
            },
            "odd_residue_factor_rows": factor_rows,
            "residue_element_basis_sha256": csha([pstr(v) for v in z]),
            "first_norm_U_plus_Vs_sha256": csha([pstr(U), pstr(V)]),
            "total_biquadratic_norm_sha256": csha(pstr(total_norm)),
            "total_biquadratic_norm_degree": degree0,
            "denominator_clearing_scalar": den,
            "split_prime_trials": trials,
            "residue_nonsquare_certified": nonsquare,
            "classification": "NONSQUARE_BY_GOOD_SPLIT_PRIME_REDUCTION_OF_BIQUADRATIC_TOTAL_NORM" if nonsquare else "INCONCLUSIVE_BY_CONFIGURED_SPLIT_PRIMES",
            "logical_witness": "if the residue element were a square in the biquadratic function field, its field norm to Q(i)(x) would be a square; an odd positive-degree factor after defined good split-prime reduction contradicts this",
        })

    inconclusive = 4 - nonsquare_count
    if inconclusive == 0:
        next_leaf = "V91C1X_R5B3B3C4B2B2D_OFFBOUNDARY_RESIDUE_CLASSIFICATION_RECONCILIATION_AND_DIRECT_SUPPORT_REPAIR_SCOPE"
    else:
        next_leaf = "V91C1X_R5B3B3C4B2B2C4_LIN024_INCONCLUSIVE_COMPONENT_RESIDUE_EXACT_SQUARECLASS_FALLBACK"

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2c3.lin024_four_component_biquadratic_residue_norm.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2C3_LIN024_FOUR_COMPONENT_BIQUADRATIC_RESIDUE_NORM_TEST",
        "role": "EXACT_NONCREDIT_COMPONENTWISE_SQUARECLASS_TEST_FOR_THE_FOUR_ACTUAL_LIN024_HEIGHT_ONE_PRIMES_REPLACING_THE_TWO_NONPRIME_DIRECT_SUPPORT_LABELS",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "c4a_tame_residue_preflight_sha256": C4A_SHA,
            "c4b2b2c2_lin024_actual_prime_incidence_sha256": C2_SHA,
        },
        "componentwise_result": {
            "actual_prime_count": 4,
            "nonsquare_certified_count": nonsquare_count,
            "inconclusive_count": inconclusive,
            "rows": rows,
        },
        "exact_consequence": {
            "lin024_old_two_support_label_squareclass_debt_retired": True,
            "lin024_actual_four_prime_squareclass_tests_materialized": True,
            "lin024_all_four_actual_prime_residues_nonsquare": inconclusive == 0,
            "f4_f14_degree16_nonsquare_results_unchanged": True,
            "current_literal_eight_symbol_candidate_unramifiedness_verified": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "stage33_11e_direct_support_prime_inventory_replay_still_required": True,
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
            "actual_prime_count": cert["componentwise_result"]["actual_prime_count"],
            "nonsquare_certified_count": cert["componentwise_result"]["nonsquare_certified_count"],
            "inconclusive_count": cert["componentwise_result"]["inconclusive_count"],
            "next_exact_leaf": cert["next_exact_leaf"],
            "certificate_sha256": cert["canonical_sha256"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    if json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2C3 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
