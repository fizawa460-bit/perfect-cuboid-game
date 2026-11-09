#!/usr/bin/env python3
"""Replay the integer real-sign and finite-field certificates for row376."""

from functools import cache
from itertools import combinations
import json
from math import isqrt, prod
from pathlib import Path

from flint import fmpz_poly, nmod_poly


HERE = Path(__file__).resolve().parent
X = fmpz_poly([0, 1])
WARD_INITIAL = tuple(map(fmpz_poly, ([0], [1], [-2], [3, -2, -1], [-4, 12, 20, 4])))


@cache
def ward(n):
    if n < len(WARD_INITIAL):
        return WARD_INITIAL[n]
    k = n // 2
    if n % 2:
        return ward(k + 2) * ward(k)**3 - ward(k - 1) * ward(k + 1)**3
    numerator = ward(k) * (ward(k + 2) * ward(k - 1)**2 - ward(k - 2) * ward(k + 1)**2)
    assert all(c % 2 == 0 for c in numerator)
    return fmpz_poly([int(c) // -2 for c in numerator])


def reverse_even(f):
    """Return x^(2*deg(f)) f(1/x^2)."""
    coefficients = [0] * (2 * f.degree() + 1)
    coefficients[::2] = list(reversed(list(f)))
    return fmpz_poly(coefficients)


def homogenized(f, a, b):
    """Return b^deg(f) f(a/b), including b=0."""
    coefficients = list(f)
    value = coefficients[-1]
    b_power = 1
    for c in reversed(coefficients[:-1]):
        b_power *= b
        value = a * value + c * b_power
    return value


def check_model(factors, a_star, b_star):
    f, f_reflected, e, h, h_reflected, e_next = factors
    assert [p.degree() for p in factors] == [105, 105, 210, 120, 120, 240]
    assert [p.leading_coefficient() for p in factors] == [1, -1, -29, 1, 1, -31]
    assert all(p[0] == 1 for p in factors)
    assert f_reflected == f(-X) and h_reflected == h(-X)
    assert f * f_reflected * e == reverse_even(ward(29))
    assert h * h_reflected * e_next == -reverse_even(ward(31))
    assert [abs(p.resultant(q)) for p, q in combinations(factors, 2)] == [
        2**k for k in (7385, 14770, 8400, 8400, 16800, 14770, 8400, 8400, 16800,
                       16800, 16800, 33600, 9640, 19280, 19280)
    ]
    assert [p(4) % 8 for p in factors] == [5, 5, 1, 1, 1, 1]
    assert f == a_star**2 + X * b_star**2
    g = a_star(-X**2) + X * b_star(-X**2)
    assert g.degree() == 105 and g[0] == 1 and g.leading_coefficient() == 1
    assert g * g(-X) == f(-X**2)


def check_real_signs(f, h):
    assert homogenized(f, -3, 10) < 0 < homogenized(f, -29, 100)
    assert h[0] > 0 > homogenized(h, 3, 10)
    assert homogenized(h, 643, 5538) > 0 > homogenized(h, 2133, 18371)
    transformed = homogenized(h, 3 * X, 10 * (1 + X))
    signs = [1 if c > 0 else -1 for c in transformed if c]
    changes = sum(x != y for x, y in zip(signs, signs[1:]))
    assert changes == 1
    bound_gap = 18371**2 - 74 * 2133**2
    assert bound_gap == 816655
    w60_shifted = ward(60)(74 + X)
    assert w60_shifted.degree() == 899 and w60_shifted.leading_coefficient() == 60
    assert len(w60_shifted) == 900 and min(w60_shifted) == 60
    return {
        "F29_negative_root_bracket": ["-3/10", "-29/100"],
        "F31_descartes_sign_changes": changes,
        "F31_first_positive_root_bracket": ["643/5538", "2133/18371"],
        "z_lower_bound_gap": bound_gap,
        "w60_at_74_plus_X_degree": w60_shifted.degree(),
        "w60_at_74_plus_X_positive_coefficients": len(w60_shifted),
        "w60_at_74_plus_X_smallest_coefficient": int(min(w60_shifted)),
    }


def slopes(p, factors):
    squares = {x*x % p for x in range(p)}
    polynomials = [nmod_poly([int(c) for c in f], p) for f in factors]
    square_arguments = {x for x in range(p) if all(int(f(x)) in squares for f in polynomials)}
    survivors = []
    for u, v in [(1, 0)] + [(u, 1) for u in range(p)]:
        a, b, c = 2*u*v % p, (u*u - v*v) % p, (u*u + v*v) % p
        d = a*c % p
        if b:
            allowed = d * pow(b, -2, p) % p in square_arguments
        else:
            allowed = all(int(f.leading_coefficient()) * pow(d, f.degree(), p) % p in squares
                          for f in factors)
        if allowed:
            survivors.append([u, v, a, b, c])
    assert [1, 0, 0, 1, 1] in survivors and [0, 1, 0, p-1, 1] in survivors
    return polynomials[0], survivors


def subset_degrees(degrees):
    sums = {0}
    for d in degrees:
        sums |= {n + d for n in sums}
    return sums


def check_splitting_primes(factors):
    forced_abc = []
    forced_a = []
    for p in range(3, 258, 2):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        f_mod_p, survivors = slopes(p, factors)
        if all(a*b*c % p == 0 for _, _, a, b, c in survivors):
            unit, decomposition = f_mod_p.factor()
            assert unit == 1 and all(e == 1 for _, e in decomposition)
            product = nmod_poly([1], p)
            for g, _ in decomposition:
                product *= g
            assert product == f_mod_p
            degrees = sorted(g.degree() for g, _ in decomposition)
            forced_abc.append({"p": p, "survivors": survivors, "residue_degrees": degrees})
        if all(a == 0 for _, _, a, _, _ in survivors):
            forced_a.append(p)
    assert [r["p"] for r in forced_abc] == [
        3, 5, 7, 11, 13, 19, 31, 41, 43, 47, 53, 59, 67, 71, 79, 103, 107, 137, 139, 167, 227,
    ]
    assert forced_a == [3, 7, 11, 19, 31, 43, 47, 59, 67, 71, 79, 103, 107, 139, 167, 227]
    degrees = {r["p"]: r["residue_degrees"] for r in forced_abc}
    assert subset_degrees(degrees[3]) & subset_degrees(degrees[31]) == {0, 105}
    odd_ideal_count = sum(len(ds) for ds in degrees.values())
    assert odd_ideal_count == 98
    modulus = 8 * prod(forced_a)
    assert modulus == 2832526362265305430752577704
    return {
        "odd_prime_limit": 257,
        "forced_abc": forced_abc,
        "forced_a": forced_a,
        "A_modulus": modulus,
        "S0_odd_prime_ideals": odd_ideal_count,
        "S0_dyadic_prime_ideals_from_row373": 2,
        "S0_cardinality": odd_ideal_count + 2,
    }


def main():
    model = json.loads((HERE / "curve_factors.json").read_text(encoding="utf-8"))
    assert model["factor_order"] == ["F29(s)", "F29(-s)", "E29(s)", "F31(s)", "F31(-s)", "E31(s)"]
    factors = [fmpz_poly(c) for c in model["ascending_coefficients"]]
    a_star, b_star = (fmpz_poly(model[key]) for key in ("A_star_ascending", "B_star_ascending"))
    check_model(factors, a_star, b_star)
    result = check_real_signs(factors[0], factors[3]) | check_splitting_primes(factors)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
