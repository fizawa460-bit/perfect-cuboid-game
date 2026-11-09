#!/usr/bin/env python3
"""Exact ±30 Ward factor, curve, rank-lower-bound, and local-gate replay."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from json import dumps
from math import gcd
from pathlib import Path

from flint import fmpz_poly, nmod_poly
import sympy as sp


Z = sp.Symbol("z")
T = sp.Symbol("t")
HERE = Path(__file__).resolve().parent


@lru_cache(None)
def ward(n):
    if n < 5:
        values = [0, 1, -2, (1-Z)*(3+Z), -4*(1-3*Z-5*Z**2-Z**3)]
        return sp.Poly(values[n], Z)
    k = n//2
    if n % 2:
        return ward(k+2)*ward(k)**3 - ward(k-1)*ward(k+1)**3
    return (ward(k)*(ward(k+2)*ward(k-1)**2 - ward(k-2)*ward(k+1)**2)).exquo(ward(2))


def reflected_factors(j):
    sign, pair = ward(j).factor_list()
    assert sign == (1 if j == 29 else -1)
    expected = 105 if j == 29 else 120
    assert all(g.is_monic and e == 1 and g.degree() == expected for g, e in pair)
    assert len(pair) == 2
    factor_list = []
    for g, _ in pair:
        substituted = sp.Poly.from_dict({(2*k[0],): c for k, c in g.terms()}, T)
        scale, factors = substituted.factor_list()
        assert scale == 1 and all(h.is_monic and e == 1 for h, e in factors)
        factor_list.extend(fmpz_poly([int(c) for c in h.all_coeffs()]) for h, _ in factors)
    negative, = [h for h in factor_list if h[1] < 0]
    positive, = [h for h in factor_list if h[1] > 0]
    even, = [h for h in factor_list if h[1] == 0]
    assert negative.degree() == positive.degree() == expected
    assert even.degree() == 2*expected
    x = fmpz_poly([0, 1])
    assert positive == negative(-x) and even == even(-x)
    assert all(h[0] == 1 and h.gcd(h.derivative()).degree() == 0
               for h in (negative, positive, even))
    assert [int(h.leading_coefficient()) for h in (negative, positive, even)] == (
        [1, -1, -29] if j == 29 else [1, 1, -31]
    )
    assert int(negative[1]) == (-7 if j == 29 else -8)
    reciprocal = fmpz_poly([int(c)//int(sign) for c in ward(j).all_coeffs()])
    assert negative*positive*even == reciprocal(x*x)
    return int(sign), [g for g, _ in pair], [negative, positive, even]


def homogeneous(f, d, b2, modulus=None):
    result, power = int(f.leading_coefficient()), 1
    for c in reversed(list(f)[:-1]):
        power *= b2
        result = result*d + int(c)*power
        if modulus is not None:
            result %= modulus
            power %= modulus
    return result


def primitive_slopes(p, polynomials):
    squares = {i*i % p for i in range(p)}
    survivors = []
    for u, v in [(i, 1) for i in range(p)] + [(1, 0)]:
        a, b, c = 2*u*v % p, (u*u-v*v) % p, (u*u+v*v) % p
        d = a*c % p
        values = [homogeneous(f, d, b*b % p, p) for f in polynomials]
        if all(x in squares for x in values):
            survivors.append([u, v, a, b, c, values])
    return survivors


def f_p(f, p):
    return nmod_poly([int(c) for c in f], p)


def factors_at(f, p):
    reduced = f_p(f, p)
    scalar, factors = reduced.factor()
    out = [g for g, e in factors if e == 1]
    assert len(out) == len(factors) and sum(g.degree() for g in out) == f.degree()
    product = nmod_poly([int(scalar)], p)
    for g in out:
        product *= g
    assert product == reduced
    return sorted(out, key=lambda g: (g.degree(), list(map(int, g))))


def degrees_of_subproducts(degrees):
    possible = {0}
    for d in degrees:
        possible |= {k+d for k in possible}
    return possible


def mod_power(x, n, mod, p):
    result = nmod_poly([1], p)
    x %= mod
    while n:
        if n % 2:
            result = (result*x) % mod
        n //= 2
        x = (x*x) % mod
    return result


def gf2_rank(rows):
    basis = {}
    for row in rows:
        mask = sum(bit << i for i, bit in enumerate(row))
        while mask:
            h = mask.bit_length()
            if h not in basis:
                basis[h] = mask
                break
            mask ^= basis[h]
    return len(basis)


def real_bands(polys):
    roots = []
    for i, f in enumerate(polys):
        expr = sp.Poly.from_list([int(c) for c in reversed(list(f))], T)
        for (a, b), multiplicity in expr.intervals(eps=sp.Rational(1, 10**8), inf=0):
            assert multiplicity == 1 and a > 0
            roots.append((a, b, i))
    roots.sort()
    assert all(b < c for (_, b, _), (c, _, _) in zip(roots, roots[1:]))
    assert len(roots) == 29
    signs = set()
    bands = []
    last = (0, 0, -1)
    for entry in roots:
        if not signs:
            bands.append([last, entry])
        i = entry[2]
        signs.symmetric_difference_update({i})
        last = entry
    assert signs and len(bands) == 4
    return [[[str(a), str(b), i] for a, b, i in band] for band in bands]


def signed_real_witness(u, v, polys):
    a, b, c = 2*u*v, u*u-v*v, u*u+v*v
    d, V = a*c, b**4
    d2 = d*d
    assert gcd(u, v) == 1 and (u-v) % 2 == 1
    assert all(homogeneous(f, d, b*b) > 0 for f in polys)
    small = [0, 1, -2*d**3, d**4*(d2-V)*(3*d2+V),
             -4*d**9*(d2**3-3*V*d2**2-5*V*V*d2-V**3)]

    @lru_cache(None)
    def W(n):
        if n < 5:
            return small[n]
        k = n//2
        if n % 2:
            return W(k+2)*W(k)**3-W(k-1)*W(k+1)**3
        q, r = divmod(W(k)*(W(k+2)*W(k-1)**2-W(k-2)*W(k+1)**2), W(2))
        assert r == 0
        return q

    assert W(29) > 0 and W(31) < 0 and W(30) != 0 and W(60) != 0
    return {"u":u,"v":v,"s":str(Fraction(d,b*b)),"W60_sign":1 if W(60)>0 else -1}


def main():
    raw = {j: reflected_factors(j) for j in (29, 31)}
    polynomials = raw[29][2] + raw[31][2]
    expected = [7385,14770,8400,8400,16800,14770,8400,8400,16800,
                16800,16800,33600,9640,19280,19280]
    results = {}
    for (i, k), power in zip(combinations(range(6), 2), expected):
        assert abs(int(polynomials[i].resultant(polynomials[k]))) == 2**power
        results[f"{i}/{k}"] = power
    assert [abs(int(raw[j][1][0].resultant(raw[j][1][1]))) for j in (29,31)] == [2**14770,2**19280]

    primes = [3, 7, 11, 19, 31]
    slopes = {p: primitive_slopes(p, polynomials) for p in primes}
    assert all([[r[0],r[1]] for r in table] == [[0,1],[1,0]] for table in slopes.values())
    assert all(homogeneous(f,4,1,8) == c for f,c in zip(polynomials,[5,5,1,1,1,1]))
    assert all(homogeneous(f,0,1,8) == 1 for f in polynomials)

    x = fmpz_poly([0, 1])
    F = polynomials[0]
    factorization = F(-x*x).factor()[1]
    assert sorted((g.degree(),m) for g,m in factorization) == [(105,1),(105,1)]
    G = factorization[0][0]
    if G[0] < 0:
        G = -G
    assert G(x)*G(-x) == F(-x*x)
    A = fmpz_poly([(-1)**i*G[2*i] for i in range(53)])
    B = fmpz_poly([(-1)**i*G[2*i+1] for i in range(53)])
    if B.leading_coefficient() < 0:
        B = -B
    assert A[0] == 1 and abs(B[0]) == 1
    assert A.degree() == B.degree() == 52 and B.leading_coefficient() == 1
    assert F == A*A + x*B*B and A.gcd(B).degree() == 0
    assert F(1) == F(-1) == 2**70

    good = {p: factors_at(F,p) for p in (3,17,31)}
    degs = {p: [g.degree() for g in ff] for p, ff in good.items()}
    assert degs == {3:[6,33,66],17:[4,8,14,16,63],31:[4,5,48,48]}
    assert degrees_of_subproducts(degs[3]) & degrees_of_subproducts(degs[31]) == {0,105}
    classes = []
    norms = []
    for a in (B, 1-x, -1-x):
        U = f_p(a,17)
        row, raw_norm = [], []
        for g in good[17]:
            chi = mod_power(U,(17**g.degree()-1)//2,g,17)
            assert chi in (nmod_poly([1],17), nmod_poly([16],17))
            raw_norm.append(int(g.resultant(U)) % 17)
            row.append(0 if chi[0] == 1 else 1)
        assert [int(pow(r,8,17) != 1) for r in raw_norm] == row
        classes.append(row)
        norms.append(raw_norm)
    assert classes == [[0,0,0,1,1],[1,1,1,0,1],[1,1,0,1,1]]
    assert gf2_rank(classes) == 3
    bands = real_bands(polynomials)
    witnesses = [signed_real_witness(u,v,polynomials) for u,v in ((7,2),(18,1))]
    assert [r["W60_sign"] for r in witnesses] == [-1,1]

    data = {
        "status":"AUTHOR_EXACT_REPLAY_PASS_NO_SIGNED_INDEX_EXCLUSION",
        "factor_order":["F29(s)","F29(-s)","E29(s)","F31(s)","F31(-s)","E31(s)"],
        "ascending_coefficients":[[int(c) for c in f] for f in polynomials],
        "z_factors_ascending":{j:[[int(g.nth(k)) for k in range(g.degree()+1)] for g in row[1]]
                               for j,row in raw.items()},
        "resultant_abs_2_exponents":results,
        "primitive_projective_survivors":slopes,
        "common_positive_bands_with_isolations":bands,
        "real_sign_witnesses":witnesses,
        "A_star_ascending":[int(c) for c in A],
        "B_star_ascending":[int(c) for c in B],
        "factor_degrees_mod_p":degs,
        "finite_field_factors_ascending":{p:[list(map(int,g)) for g in ff] for p,ff in good.items()},
        "p17_Kummer_norms":norms, "p17_Kummer_classes":classes,
        "p17_Kummer_rank":3, "rank_lower_bound":3,
        "new_excluded_abs":[],"remaining_abs":[12,30,42,60,72,102,108,138,150],
        "remaining_signed_count":17,
    }
    (HERE/"row370_exact.json").write_text(dumps(data,indent=2)+"\n",encoding="utf-8")
    print(dumps({"status":data["status"],"degrees":[f.degree() for f in polynomials],
                "pairwise_resultants":len(results),"positive_bands":len(bands),
                "forced_odd_A_primes":primes,"rank_lower_bound":3,"remaining":[9,17]}))


if __name__ == "__main__":
    main()
