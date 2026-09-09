#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
import sympy as sp

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3

H = Path(__file__).resolve().parent
P = {
    "b3": (H / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json",
           "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"),
    "c2c": (H / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json",
            "01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a"),
    "b2": (H / "e3-v91c1x-r5b3b3c4b2b2-remaining24-strict-prime-squareclass-partition.json",
           "c35b8737bd310935c844b170975617e69f2745b60a932349b3c297dd6909fb27"),
    "b": (H / "e3-v91c1x-r5b3b3c4b2b2b-f14-four-residual-prime-residue-norm-witness.json",
          "6949358e0bd577a9538bc09e662682240c571f7909b0b9feb02eea6efa0c7e08"),
}
OUT = H / "e3-v91c1x-r5b3b3c4b2b2c-unique-degree16-residue-norm-sweep.json"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I
BASE = b3.BASE
VM = {str(v): v for v in BASE}
PRIMES = [13, 17, 29]

def hs(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load(k):
    p, expected = P[k]
    o = json.loads(p.read_text(encoding="utf-8"))
    body = dict(o)
    claimed = body.pop("canonical_sha256", None)
    actual = hs(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"lock moved: {p.name}: claimed={claimed} actual={actual} expected={expected}")
    return o

def z():
    return sp.Poly(0, *BASE, extension=I)

def add(x, y):
    o = dict(x)
    for m, p in y.items():
        q = o.get(m, z()) + p
        if q.is_zero:
            o.pop(m, None)
        else:
            o[m] = q
    return o

def flip(e, bit):
    f = 1 << bit
    return {m: (-p if m & f else p) for m, p in e.items()}

def norm_and_derivatives(enc):
    v = [b3.decode_qi(q) for q in enc]
    e = {}
    q = v[0] * BASE[0] + v[1] * BASE[1] + v[2] * BASE[2]
    if q != 0:
        e[0] = sp.Poly(q, *BASE, extension=I)
    for j, c in enumerate(v[3:]):
        if c != 0:
            e[1 << j] = sp.Poly(c, *BASE, extension=I)
    ds = [{0: sp.Poly(1, *BASE, extension=I)}] + [
        {1 << j: sp.Poly(1, *BASE, extension=I)} for j in range(4)
    ]
    for bit in range(4):
        ef = flip(e, bit)
        ne = b3.elem_mul(e, ef)
        nds = []
        for d in ds:
            nds.append(add(b3.elem_mul(d, ef), b3.elem_mul(e, flip(d, bit))))
        e, ds = ne, nds
    if set(e) != {0} or any(set(d) - {0} for d in ds):
        raise SystemExit("derivative norm retained radicals")
    return e[0], [d.get(0, z()) for d in ds]

def residue_numerator(enc, ds):
    v = [b3.decode_qi(q) for q in enc]
    d0, d1, d2, d3, d4 = ds
    q = ((v[0] * BASE[0] + v[1] * BASE[1] + v[2] * BASE[2]) * d0
         + v[3] * d1 + v[4] * d2 + v[5] * d3 + v[6] * d4)
    return sp.Poly(sp.expand(q.as_expr() if isinstance(q, sp.Poly) else q),
                   *BASE, extension=I)

def i_image(p):
    for r in range(p):
        if (r * r + 1) % p == 0:
            return r
    raise SystemExit(f"prime does not split in Q(i): {p}")

def ratmod(q, p):
    q = sp.Rational(q)
    n, d = int(sp.numer(q)), int(sp.denom(q))
    if d % p == 0:
        raise ValueError("bad reduction denominator")
    return n * pow(d, -1, p) % p

def qimod(c, p, ii):
    c = sp.cancel(sp.sympify(c))
    cc = sp.cancel(sp.conjugate(c))
    re = sp.cancel((c + cc) / 2)
    im = sp.cancel((c - cc) / (2 * I))
    if re.is_Rational is not True or im.is_Rational is not True:
        raise ValueError(f"coefficient escaped Q(i): {c}")
    return (ratmod(re, p) + ii * ratmod(im, p)) % p

def modpoly(expr, vars_, p, ii):
    q = sp.Poly(sp.expand(expr), *vars_, extension=I)
    out = 0
    for mon, c in q.terms():
        t = qimod(c, p, ii)
        for v, e in zip(vars_, mon):
            t *= v ** e
        out += t
    return sp.Poly(out, *vars_, modulus=p)

def odd_sqf_support(poly, x, p):
    q = sp.Poly(poly, x, modulus=p)
    if q.is_zero:
        raise ValueError("zero modular norm")
    _unit, fac = sp.sqf_list(q.as_expr(), x, modulus=p)
    out = []
    for f, e in fac:
        m = sp.Poly(f, x, modulus=p).monic()
        if int(e) % 2 and m.degree() > 0:
            out.append({
                "degree": int(m.degree()),
                "multiplicity_mod_2": 1,
                "squarefree_block_sha256": hs([int(c) % p for c in m.all_coeffs()]),
            })
    return out

def modular_product_norm_witness(f, gs, x, y, p):
    ii = i_image(p)
    fm = modpoly(f, (x, y), p, ii)
    R = sp.GF(p).poly_ring(x)
    fy = sp.Poly(fm.as_expr(), y, domain=R)
    exact_y_degree = int(sp.Poly(f, y).degree())
    if fy.degree() <= 0 or int(fy.degree()) != exact_y_degree:
        raise ValueError("bad reduction: quotient y-degree dropped")
    lc = fy.LC()
    product = sp.Poly(1, x, modulus=p)
    per = []
    for g in gs:
        gm = modpoly(g, (x, y), p, ii)
        gy = sp.Poly(gm.as_expr(), y, domain=R)
        if gy.is_zero:
            raise ValueError("bad reduction: zero residue numerator")
        res = fy.resultant(gy)
        rp = sp.Poly(res, x, modulus=p)
        if rp.is_zero:
            raise ValueError("bad reduction: resultant vanished")
        m = int(gy.degree())
        if m % 2:
            lcp = sp.Poly(lc, x, modulus=p)
            rp *= lcp
        product *= rp
        per.append({
            "g_y_degree_mod_p": m,
            "resultant_x_degree_mod_p": int(sp.Poly(res, x, modulus=p).degree()),
            "leading_coefficient_correction_parity": m % 2,
        })
    support = odd_sqf_support(product.as_expr(), x, p)
    return {
        "rational_prime": p,
        "i_image": ii,
        "i_image_squared_plus_one_zero_mod_p": (ii * ii + 1) % p == 0,
        "per_odd_carrier_norm": per,
        "combined_norm_x_degree_mod_p": int(product.degree()),
        "odd_squarefree_support": support,
        "nonsquare_mod_split_prime": bool(support),
    }

def build():
    B3, C2C, B2, B = load("b3"), load("c2c"), load("b2"), load("b")
    if (B["exact_consequence"]["F14_four_remaining_squareclass_debt_count"] != 0
        or not B["exact_consequence"]["F4_pair_and_F14_four_repeated_factor_debts_all_resolved_as_nonsquare"]
        or B["next_exact_leaf"] != "V91C1X_R5B3B3C4B2B2C_UNIQUE_C1_FACTOR_LOW_COST_RESIDUE_NORM_SWEEP"):
        raise SystemExit("C4B2B2B gate moved")

    inv = {r["carrier_id"]: r for r in B3["finite_linear_carrier_inventory"]["carrier_rows"]}
    reps = {r["carrier_id"]: r for r in C2C["representative_strict_prime_decompositions"]["rows"]}
    bucket = next(r for r in B2["remaining24_partition"]["rows_by_bucket"]
                  if r["bucket"] == "UNIQUE_C1_FACTOR_STRICT_PRIMES")
    rows = list(bucket["rows"])
    d16 = [r for r in rows if int(r["c1_factor_total_degree"]) == 16]
    d1 = [r for r in rows if int(r["c1_factor_total_degree"]) == 1]
    if len(rows) != 18 or len(d16) != 16 or len(d1) != 2:
        raise SystemExit("unique-factor degree partition moved")
    if any(int(r["c1_factor_multiplicity_in_full_sign_norm"]) != 1 for r in d16):
        raise SystemExit("degree-16 multiplicity-one contract moved")
    if any(r["carrier_id"] != "LIN_024" or int(r["c1_factor_multiplicity_in_full_sign_norm"]) != 8
           for r in d1):
        raise SystemExit("LIN_024 degree-one deferred pair moved")
    if set(reps) != {r["carrier_id"] for r in d16}:
        raise SystemExit("C2C representative carrier set no longer equals the 16 unique degree-16 targets")

    out_rows = []
    nonsquare = 0
    for t in sorted(d16, key=lambda r: r["carrier_id"]):
        cid = t["carrier_id"]
        rep = reps[cid]
        if int(rep["strict_prime_count"]) != 1 or list(rep["strict_prime_multiplicities"]) != [1]:
            raise SystemExit(f"C2C strict-prime contract moved for {cid}")
        st = rep["strict_transform_on_resolution"]
        if int(st["irreducible_strict_prime_count"]) != 1 or list(st["strict_transform_multiplicities"]) != [1]:
            raise SystemExit(f"C2C strict-transform contract moved for {cid}")
        mc = rep["modular_norm_irreducibility_certificate"]
        dehom, y, x = VM[mc["dehom"]], VM[mc["polyvar"]], VM[mc["specialized_var"]]
        if {dehom, x, y} != set(BASE):
            raise SystemExit(f"C2C chart variables moved for {cid}")

        N, ds = norm_and_derivatives(inv[cid]["normalized_coefficients_Qi"])
        fsha = t["c1_normalized_factor_sha256"]
        if int(N.total_degree()) != 16 or hs(b3.normalize_norm(N)) != fsha:
            raise SystemExit(f"degree-16 norm/factor reconstruction moved for {cid}")
        f = sp.expand(N.as_expr().subs(dehom, 1))
        ff = sp.Poly(f, y, domain=sp.QQ_I.frac_field(x))
        if ff.degree() <= 0:
            raise SystemExit(f"bad exact quotient chart for {cid}")

        d0 = sp.Poly(ds[0].as_expr().subs(dehom, 1), y,
                     domain=sp.QQ_I.frac_field(x)).rem(ff)
        if d0.is_zero:
            raise SystemExit(f"scalar derivative vanished mod target norm for {cid}")
        target_q = sp.Poly(
            residue_numerator(inv[cid]["normalized_coefficients_Qi"], ds).as_expr().subs(dehom, 1),
            y, domain=sp.QQ_I.frac_field(x)
        ).rem(ff)
        if not target_q.is_zero:
            raise SystemExit(f"derivative adapter target recovery failed for {cid}")

        odd = list(t["combined_tame_residue_odd_linear_carrier_ids"])
        if len(odd) not in (2, 4) or len(odd) % 2:
            raise SystemExit(f"unexpected odd-carrier count for {cid}: {len(odd)}")
        gs, details = [], []
        for oid in odd:
            g = sp.expand(residue_numerator(inv[oid]["normalized_coefficients_Qi"], ds).as_expr().subs(dehom, 1))
            gr = sp.Poly(g, y, domain=sp.QQ_I.frac_field(x)).rem(ff)
            if gr.is_zero:
                raise SystemExit(f"cross-carrier residue unexpectedly zero for {cid}/{oid}")
            gs.append(g)
            details.append({
                "carrier_id": oid,
                "exact_remainder_nonzero_mod_target_norm": True,
                "y_degree_before_reduction": int(sp.Poly(g, y).degree()),
            })

        witnesses = []
        chosen = None
        for p in PRIMES:
            try:
                w = modular_product_norm_witness(f, gs, x, y, p)
            except (ValueError, ZeroDivisionError, sp.PolynomialError) as exc:
                witnesses.append({"rational_prime": p, "usable_good_reduction": False,
                                  "reason": str(exc)[:160]})
                continue
            w["usable_good_reduction"] = True
            witnesses.append(w)
            if w["nonsquare_mod_split_prime"]:
                chosen = w
                break

        ok = chosen is not None
        nonsquare += int(ok)
        out_rows.append({
            "carrier_id": cid,
            "c1_normalized_factor_sha256": fsha,
            "strict_prime_ids": list(t["c4a_strict_prime_ids"]),
            "c2c_irreducible_norm_certificate": {
                "strict_prime_count": 1,
                "strict_prime_multiplicity": 1,
                "norm_irreducible_modular_certificate_bound": True,
                "finite_free_norm_exponent_one_implies_residue_degree_one": True,
            },
            "quotient_chart": {
                "dehomogenized_variable": str(dehom),
                "norm_polynomial_variable": str(y),
                "rational_function_base_variable": str(x),
                "target_norm_total_degree": 16,
                "target_norm_y_degree": int(ff.degree()),
            },
            "derivative_adapter": {
                "scalar_derivative_nonzero_mod_target_norm": True,
                "target_linear_form_recovers_zero_mod_target_norm": True,
                "odd_carrier_denominator_power_even": True,
                "odd_carrier_denominator_is_square_in_combined_squareclass": True,
            },
            "odd_residue_carrier_ids": odd,
            "per_carrier_exact_reduction": details,
            "split_prime_trials": witnesses,
            "residue_nonsquare_certified": ok,
            "classification": ("NONSQUARE_BY_GOOD_SPLIT_PRIME_REDUCTION_OF_DEGREE16_RESIDUE_NORM"
                               if ok else "INCONCLUSIVE_WITH_BOUNDED_SPLIT_PRIME_SWEEP"),
        })

    deferred = [{
        "carrier_id": r["carrier_id"],
        "c1_normalized_factor_sha256": r["c1_normalized_factor_sha256"],
        "strict_prime_ids": list(r["c4a_strict_prime_ids"]),
        "c1_factor_total_degree": 1,
        "c1_factor_multiplicity_in_full_sign_norm": 8,
        "reason": "degree-one base factor has norm multiplicity eight, so the residue-degree-one derivative adapter used for exponent-one irreducible norms is not assumed here",
    } for r in d1]

    inconclusive = 16 - nonsquare
    remaining = inconclusive + 2
    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2c.unique_degree16_residue_norm_sweep.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2C_UNIQUE_C1_FACTOR_LOW_COST_RESIDUE_NORM_SWEEP",
        "role": "EXACT_NONCREDIT_BOUNDED_SPLIT_PRIME_NORM_SWEEP_FOR_THE_16_MULTIPLICITY_ONE_DEGREE16_UNIQUE_C1_STRICT_PRIMES_WITH_THE_TWO_LIN024_DEGREE1_MULTIPLICITY8_TARGETS_EXPLICITLY_DEFERRED",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {k: v[1] for k, v in P.items()},
        "method": {
            "degree16_target_count": 16,
            "finite_free_rank": 16,
            "residue_degree_one_reason": "for each irreducible norm factor occurring with exponent one, the C2C finite-free norm-prime lemma gives one reduced strict prime and determinant length one, hence residue degree one",
            "derivative_adapter": "differentiate the 16-fold sign norm of the target linear carrier; modulo its norm prime this gives the degree-one residue embedding up to one common scalar denominator",
            "squareclass_denominator_control": "every combined tame residue here contains 2 or 4 odd linear carriers, so the common derivative denominator occurs to an even power and is a square",
            "good_reduction_primes_tried": PRIMES,
            "nonsquare_logic": "a square in Q(i)(x) has square reduction at every defined good split prime; an odd squarefree factor in the reduced norm certifies nonsquareness in characteristic zero",
        },
        "degree16_sweep": {
            "target_count": 16,
            "nonsquare_by_norm_count": nonsquare,
            "inconclusive_count": inconclusive,
            "rows": out_rows,
        },
        "lin024_degree1_deferred_pair": {
            "target_count": 2,
            "rows": deferred,
        },
        "exact_consequence": {
            "repeated_factor_F4_and_F14_debts_remaining": 0,
            "unique_degree16_nonsquare_certified_count": nonsquare,
            "unique_degree16_inconclusive_count": inconclusive,
            "lin024_degree1_squareclass_debt_count": 2,
            "remaining_strict_prime_squareclass_debt_count": remaining,
            "current_literal_eight_symbol_candidate_was_already_known_ramified_from_C4B2B1": True,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": (
            "V91C1X_R5B3B3C4B2B2C1_LIN024_TWO_DEGREE1_STRICT_PRIME_SQUARECLASS_TEST"
            if inconclusive == 0
            else "V91C1X_R5B3B3C4B2B2C0_DEGREE16_INCONCLUSIVE_STRONGER_SQUARECLASS_TEST"
        ),
        "credit_firewall": {
            "authority_promotion": False,
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
    cert["canonical_sha256"] = hs(cert)
    return cert

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        r = cert["degree16_sweep"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "nonsquare_by_norm_count": r["nonsquare_by_norm_count"],
            "inconclusive_count": r["inconclusive_count"],
            "lin024_degree1_deferred_count": 2,
            "remaining_strict_prime_squareclass_debt_count": cert["exact_consequence"]["remaining_strict_prime_squareclass_debt_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2C certificate differs from exact rebuild")
    print(cert["canonical_sha256"])

if __name__ == "__main__":
    main()
