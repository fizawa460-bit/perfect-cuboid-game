#!/usr/bin/env python3
"""Verify the finite-field and discriminant inputs to the signed group proof."""
from math import gcd, lcm
import json

from flint import fmpz_poly, nmod_poly

from row382_inputs import DISC, N, input_bytes


def subset_sums(values):
    sums = {0}
    for d in values:
        sums |= {s+d for s in sums}
    return sums


def irreducible(g, p):
    d = g.degree()
    x = nmod_poly([0,1],p)
    roots = x % g
    for k in range(1,d+1):
        roots = roots.pow_mod(p,g)
        if k <= d//2 and d%k == 0 and (roots-x).gcd(g).degree() != 0:
            return False
    return (roots-x) % g == nmod_poly([],p)


def main():
    coefficients = json.loads(input_bytes("curve_C29.json"))["F_ascending"]
    F = fmpz_poly(coefficients)
    assert F.degree()==N and F.leading_coefficient()==1
    disc = int(F.discriminant())
    assert disc == -DISC * 2**7210
    decompositions = {}
    for p in (3,31,43,199):
        polynomial = nmod_poly(coefficients,p)
        c, factors = polynomial.factor()
        reconstructed = nmod_poly([int(c)],p)
        for f, e in factors:
            assert f.leading_coefficient()==1 and irreducible(f,p)
            reconstructed *= f**e
        assert reconstructed==polynomial
        decompositions[p]=sorted((f.degree(),e) for f,e in factors)
    assert decompositions[3] == [(6,1),(33,1),(66,1)]
    assert decompositions[31] == [(4,1),(5,1),(48,1),(48,1)]
    possible=subset_sums([d for d,e in decompositions[3]]) & subset_sums([d for d,e in decompositions[31]])
    assert possible=={0,N}
    assert decompositions[43] == [(2,1),(2,1),(9,1),(10,1),(11,1),(71,1)]
    power=lcm(*(d for d,e in decompositions[43] if d!=71))
    assert gcd(power,71)==1
    block_sizes=[d for d in range(2,N) if N%d==0]
    assert max(block_sizes)<71 and max(N//d for d in block_sizes)<71
    assert decompositions[199] == [(1,2),(27,1),(76,1)]
    assert disc%199==0 and disc%199**2!=0
    print(json.dumps({
        "factor_degrees_and_multiplicities":decompositions,
        "common_factor_degrees":sorted(possible),
        "frobenius_power_is_71_cycle":power,
        "proper_nontrivial_block_sizes":block_sizes,
        "discriminant_exponent_at_199":1,
        "unramified_residue_degrees_at_199":[27,76],
        "ramified_residue_degree_at_199":1,
        "ramification_index_at_199":2
    },indent=2))


if __name__=="__main__":
    main()
