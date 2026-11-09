#!/usr/bin/env python3
"""Exact real condition, discriminants, and integral order for C29."""

import json
from pathlib import Path

from flint import fmpq, fmpq_poly, fmpz_poly


def variations(signs):
    nonzero = [s for s in signs if s]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def sign(value):
    return int(value > 0)-int(value < 0)


def sturm_chain(f):
    a, b = fmpq_poly(f), fmpq_poly(f.derivative())
    chain = [a, b]
    while b.degree() > 0:
        remainder = -(a % b)
        assert remainder
        a, b = b, remainder/abs(remainder[remainder.degree()])
        chain.append(b)
    return chain


def main():
    root = Path(__file__).resolve().parent
    data = json.loads((root/"curve_C29.json").read_text())
    f, a, b = (fmpz_poly(data[key]) for key in
               ("F_ascending", "A_star_ascending", "B_star_ascending"))
    x = fmpz_poly([0, 1])
    g = a(-x*x)+x*b(-x*x)
    assert g.degree() == f.degree() == 105 and g[105] == f[105] == 1
    assert f(-x*x) == g*g(-x)
    disc_f, disc_g = int(f.discriminant()), int(g.discriminant())
    assert disc_f == 2**3640*disc_g
    odd_part, remainder = divmod(-disc_g, 2**3640)
    assert not remainder and odd_part % 2 == 1
    cofactor, remainder = divmod(odd_part, 199)
    assert not remainder and cofactor % 199 != 0

    shifted = g(x+1)
    relation = [[], [], []]
    for i, c in enumerate(shifted):
        q, r = divmod(i, 3)
        coeff, remainder = divmod(int(c), 2**(35-q))
        assert not remainder
        relation[r].append(coeff)
    assert relation[0][35] == 1
    assert abs(int(shifted[0])) == 2**35
    basis_index_exp = sum(i//3 for i in range(105))
    order_disc, remainder = divmod(disc_g, 2**(2*basis_index_exp))
    assert not remainder and order_disc == -2**70*199*cofactor

    chain = sturm_chain(f)
    at_minus_inf = variations(sign(q[q.degree()])*(-1)**q.degree() for q in chain)
    at_plus_inf = variations(sign(q[q.degree()]) for q in chain)
    assert (at_minus_inf, at_plus_inf) == (56, 49)
    bounds = [(-123,-122), (-14,-13), (-5,-4), (-3,-2), (fmpq(-3,2),-1),
              (fmpq(-7,10),fmpq(-3,5)), (fmpq(-2,5),fmpq(-1,5))]
    signs = []
    for i, (lo, hi) in enumerate(bounds):
        assert fmpq_poly(f)(lo) != 0 and fmpq_poly(f)(hi) != 0
        before = variations(sign(q(lo)) for q in chain)
        after = variations(sign(q(hi)) for q in chain)
        assert (before, after) == (56-i, 55-i)
        signs.append([str(lo),str(hi),before,after])
    real_dim = (len(bounds)-1)//2
    assert real_dim == 3
    out = {
        "real_signature": [7, 49],
        "sturm_infinity_variations": [56, 49],
        "real_root_intervals_ascending": signs,
        "real_sign_condition": "First sign positive, signs equal in pairs (2,3), (4,5), (6,7), 1-based.",
        "real_kummer_dimension": real_dim,
        "disc_F_v2": 7280,
        "disc_G_v2": 3640,
        "Z_rho_over_Z_theta_index_v2": 1820,
        "two_maximal_order_over_Z_rho_index_v2": basis_index_exp,
        "order_discriminant": str(order_disc),
        "odd_cofactor_after_199": str(cofactor),
        "relation_coefficients_of_t_powers": relation,
    }
    (root/"global_preflight.json").write_text(json.dumps(out, indent=2)+"\n")
    print("exact Sturm signature (7,49), seven isolating intervals, real Kummer dimension 3")
    print("disc F / disc G = 2^3640, v199 = 1")
    print("2-maximal order basis t^r beta^q, (r,q) in {0,1,2} x {0,...,34}")
    print("order discriminant -2^70*199*M, remaining cofactor digits",len(str(cofactor)))


if __name__ == "__main__":
    main()
