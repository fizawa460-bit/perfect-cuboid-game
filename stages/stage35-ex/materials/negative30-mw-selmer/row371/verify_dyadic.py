#!/usr/bin/env python3
"""Verify the exact Newton polygon and residual certificates at 2."""

import json
from pathlib import Path

from flint import fmpz_poly, nmod_poly


def v2(n):
    return (n & -n).bit_length() - 1


def support(poly):
    return [i for i, c in enumerate(poly) if c]


def from_support(exponents):
    return nmod_poly([int(i in exponents) for i in range(max(exponents) + 1)], 2)


def verify_irreducible(poly, degree, prime_divisors):
    x = nmod_poly([0, 1], 2)
    assert poly.degree() == degree
    assert x.pow_mod(2**degree, poly) == x
    for prime in prime_divisors:
        assert poly.gcd(x.pow_mod(2**(degree // prime), poly) - x) == 1


def main():
    root = Path(__file__).resolve().parent
    curve = json.loads((root / "curve_C29.json").read_text())
    f = fmpz_poly(curve["F_ascending"])
    a = fmpz_poly(curve["A_star_ascending"])
    b = fmpz_poly(curve["B_star_ascending"])
    x = fmpz_poly([0, 1])
    g = a(-x*x) + x*b(-x*x)
    assert g.degree() == 105 and g[105] == 1
    assert g*g(-x) == f(-x*x)

    shifted = g(x + 1)
    assert shifted.degree() == 105 and v2(int(shifted[0])) == 35
    for i, coefficient in enumerate(shifted):
        c = int(coefficient)
        if c:
            assert 3*v2(c) + i >= 105

    coefficients = []
    for i in range(36):
        q, remainder = divmod(int(shifted[3*i]), 2**(35-i))
        assert remainder == 0
        coefficients.append(q % 2)
    residual = nmod_poly(coefficients, 2)
    r7 = from_support([0, 1, 7])
    r28 = from_support([0, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 20, 21, 22, 24, 28])
    assert residual == r7*r28 and residual[0] == 1
    verify_irreducible(r7, 7, [7])
    verify_irreducible(r28, 28, [2, 7])
    assert residual.gcd(residual.derivative()) == 1

    z = nmod_poly([0, 1], 2)
    assert (2**7-1) % 3 != 0
    assert z.pow_mod((2**28-1)//3, r28) == 1

    degrees = [(3, 7), (3, 28)]
    field_disc_v2 = sum((e-1)*f for e, f in degrees)
    norm_kernel_dimension = sum(e*f + 2 for e, f in degrees) - 3
    jacobian_kummer_dimension = 52 + (len(degrees)-1)
    assert (field_disc_v2, norm_kernel_dimension, jacobian_kummer_dimension) == (70, 106, 53)

    print("G monic of degree 105, F(-x^2) = G(x)G(-x)")
    print("one Newton side (0,35)--(105,0)")
    print("residual exponents", support(residual))
    print("irreducible residual factors", support(r7), support(r28))
    print("dyadic (e,f)", degrees, "v2(field discriminant)", field_disc_v2)
    print("both residue classes are cubes: local fields U_f(2^(1/3))")
    print("norm kernel dimension", norm_kernel_dimension, "Jacobian Kummer dimension", jacobian_kummer_dimension)
    result = {
        "newton_endpoints": [[0, 35], [105, 0]],
        "residual_support": support(residual),
        "rabin_verified_factors": [support(r7), support(r28)],
        "local_ef": degrees,
        "residue_root_is_cube": [True, True],
        "field_discriminant_v2": field_disc_v2,
        "norm_kernel_dimension": norm_kernel_dimension,
        "jacobian_kummer_dimension": jacobian_kummer_dimension,
    }
    (root / "dyadic_local.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
