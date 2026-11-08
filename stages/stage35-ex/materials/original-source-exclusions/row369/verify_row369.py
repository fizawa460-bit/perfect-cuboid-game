#!/usr/bin/env python3
"""Replay the exact arithmetic of the Stage35EX LOW Ward-7 transfer.

Python 3.10+ and SymPy. The proof uses the accepted Ward inputs and the
C35-12 rational-point classification (which this replay does not recompute).
"""
from fractions import Fraction
from functools import lru_cache
from json import dumps, loads
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
Z = sp.Symbol("z")
U = sp.Symbol("u")

P7 = sp.Poly(Z**6 + 2*Z**5 - 33*Z**4 - 116*Z**3 - 65*Z**2 - 46*Z + 1, Z)
Q7 = sp.Poly(Z**6 + 10*Z**5 + 55*Z**4 + 156*Z**3 + 111*Z**2 - 70*Z - 7, Z)
P3 = sp.Poly(U**6 - 5*U**5 - 8*U**4 - 5*U**3 - 8*U**2 - 5*U - 1, U)
REFLECTION = sp.Poly(P3.as_expr().subs(U, -1-U), U)
TARGETS = {48: (49, 7), 78: (77, 11), 90: (91, 13), 120: (119, 17), 132: (133, 19)}


def ward_mod(modulus=None):
    initial = [sp.Poly(g, Z) for g in (0, 1, -2, (1-Z)*(3+Z), -4*(1-3*Z-5*Z**2-Z**3))]

    @lru_cache(None)
    def ward(n):
        if n < len(initial):
            value = initial[n]
        else:
            k = n//2
            if n % 2:
                value = ward(k+2)*ward(k)**3 - ward(k-1)*ward(k+1)**3
            else:
                product = ward(k)*(ward(k+2)*ward(k-1)**2 - ward(k-2)*ward(k+1)**2)
                value = product.exquo(sp.Poly(-2, Z))
        return value.rem(modulus) if modulus is not None else value

    return ward


def pow_mod(base, exponent, modulus):
    result = sp.Poly(1, Z)
    base = base.rem(modulus)
    while exponent:
        if exponent % 2:
            result = (result*base).rem(modulus)
        base = (base*base).rem(modulus)
        exponent //= 2
    return result


def norm_resultant(f, g):
    x = f.gen
    columns = [(g*sp.Poly(x**i, x)).rem(f) for i in range(f.degree())]
    norm = sp.Matrix([[c.nth(i) for c in columns] for i in range(f.degree())]).det()
    assert norm == f.resultant(g)
    return int(norm)


def source_slopes(p, a_even):
    for s, t in [(i, 1) for i in range(p)] + [(1, 0)]:
        a, b, c = 2*s*t % p, (s*s-t*t) % p, (s*s+t*t) % p
        if not a_even:
            a, b = b, a
        yield s, t, a, b, c


def source_roots(p, a_even):
    records = {"H1": [], "H2": []}
    for s, t, a, b, c in source_slopes(p, a_even):
        d = a*c % p
        if not d:
            assert b != 0
            continue
        z = pow(b, 4, p)*pow(d, -2, p) % p
        for label, poly in [("H1", P7), ("H2", Q7)]:
            if int(poly.eval(z)) % p == 0:
                records[label].append([s, t, z, b])
    return records


def signed_twists_mod8(support, residue):
    products = [1]
    for p in support:
        products += [p*d for d in products]
    return sorted(sign*d for sign in [-1, 1] for d in products if sign*d % 8 == residue)


def main():
    baseline = loads((HERE/"ROW368_BASELINE.json").read_text())
    remaining_signed = baseline["remaining_signed"]
    remaining_abs = baseline["remaining_abs"]
    remaining_B_even_abs = baseline["remaining_B_even_abs"]
    assert len(remaining_abs) == 14 and len(remaining_signed) == 27
    assert 12 not in remaining_signed and -12 in remaining_signed
    assert remaining_B_even_abs == [48, 72, 120]
    assert {n for n in remaining_abs if (n-1)*(n+1) % 7 == 0} == set(TARGETS)

    w = ward_mod()
    w7 = w(7)
    assert w7 == -P7*Q7
    phi7 = w7**2 - w(6)*w(8)
    res = {
        "P7_Q7": norm_resultant(P7, Q7),
        "P7_phi7": norm_resultant(P7, phi7),
        "Q7_phi7": norm_resultant(Q7, phi7),
        "P3_reflection": norm_resultant(P3, REFLECTION),
    }
    assert res == {"P7_Q7": -2**52, "P7_phi7": 2**196,
                   "Q7_phi7": 2**196, "P3_reflection": -2**24*13}
    split = sum(P7.nth(i)*(U*(U+1))**(6-i) for i in range(7))
    assert sp.Poly(split, U) == P3*REFLECTION
    common = sp.gcd(sp.Poly(P3.as_expr(), U, modulus=13),
                    sp.Poly(REFLECTION.as_expr(), U, modulus=13))
    assert common == sp.Poly(U-6, U, modulus=13)
    assert pow(6, 6, 13) == 12

    ward_quotient = ward_mod(w7**2)
    target_table = {}
    for n, (j, m) in TARGETS.items():
        assert j in (n-1, n+1) and j == 7*m and sp.isprime(m)
        assert ward_quotient(j).exquo(w7) == m*pow_mod(phi7, (m*m-1)//2, w7)
        roots = {label: [z for z in range(m) if int(poly.eval(z)) % m == 0]
                 for label, poly in [("H1", P7), ("H2", Q7)]}
        by_label = {label: source_roots(m, a_even)
                    for label, a_even in [("A_even", True), ("B_even", False)]}
        for rows in by_label.values():
            assert rows["H1"] == []
            if m == 7:
                assert len(rows["H2"]) == 2
                assert all(z == 0 and b == 0 for _, _, z, b in rows["H2"])
            else:
                assert rows["H2"] == []
        assert signed_twists_mod8([], 1) == [1]
        h2_twists = signed_twists_mod8([m] if m == 7 else [], 1)
        assert h2_twists == ([-7, 1] if m == 7 else [1])
        target_table[n] = {"j": j, "m": m, "field_roots": roots, "source_roots": by_label,
                           "H1_twist": [1], "H2_twists": h2_twists,
                           "B_even_allowed": n in remaining_B_even_abs}

    assert P3.eval(0) == REFLECTION.eval(0) == -1
    assert P3.LC() == REFLECTION.LC() == 1
    positive_bound = sum(Fraction(int(Q7.nth(i)), 30**i) for i in range(2, 7))
    assert positive_bound < 1 and Q7.nth(1) == -70 and Q7.nth(0) == -7
    assert all(not (a and b and c)
               for a_even in (True, False) for _, _, a, b, c in source_slopes(5, a_even))
    w47_at_0 = int(ward_mod(sp.Poly(Z, Z))(47).eval(0))
    assert w47_at_0 == 47 and (47**2-1) % 2 == 0
    nonsquares = sorted({47 % 5, -47 % 5, -7 % 5})
    assert nonsquares == [2, 3] and all(pow(x, 2, 5) == 4 for x in nonsquares)

    removed_signed = sorted(n for n in remaining_signed if abs(n) in TARGETS)
    after_signed = sorted(set(remaining_signed) - set(removed_signed))
    after_abs = sorted({abs(n) for n in after_signed})
    after_B_even = sorted(set(remaining_B_even_abs) - set(TARGETS))
    assert len(removed_signed) == 10
    assert after_abs == [12, 30, 42, 60, 72, 102, 108, 138, 150]
    assert len(after_signed) == 17 and after_B_even == [72]
    assert all(sp.isprime(n-1) and sp.isprime(n+1) for n in after_abs)

    result = {
        "run": "STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER",
        "scope": "Original indexed P23 R3-07 LOW; both signed indices, all allowed labels",
        "status": "AUTHOR_EXACT_ARITHMETIC_REPLAY_PASS_C35_12_INHERITED",
        "resultants": res,
        "P3_reflection_gcd_mod13": str(common.as_expr()),
        "ward7_checks": target_table,
        "Q7_small_z_positive_terms_bound": str(positive_bound),
        "w47_at_zero": w47_at_0,
        "mod5_nonsquare_residues": nonsquares,
        "removed_abs": sorted(TARGETS),
        "removed_signed": removed_signed,
        "removed_allowed_label_slots": len(removed_signed)+2*len(set(remaining_B_even_abs)&set(TARGETS)),
        "remaining_abs": after_abs,
        "remaining_signed": after_signed,
        "remaining_B_even_abs": after_B_even,
        "remaining_adjacent_twin_primes": {n: [n-1, n+1] for n in after_abs},
    }
    (HERE/"row369_exact.json").write_text(dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(dumps({"status": result["status"], "parent": [len(remaining_abs), len(remaining_signed)],
                 "removed": [len(TARGETS), len(removed_signed)],
                 "remaining": [len(after_abs), len(after_signed)],
                 "remaining_abs": after_abs, "remaining_B_even": after_B_even},
                ensure_ascii=False))


if __name__ == "__main__":
    main()
