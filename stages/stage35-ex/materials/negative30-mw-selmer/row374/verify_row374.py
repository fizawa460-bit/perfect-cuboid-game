#!/usr/bin/env python3
"""Exact odd discriminant and 17 dyadic obstructions on global units."""

import json
from math import gcd, isqrt, prod
from pathlib import Path

from flint import fmpz_mod_poly_ctx, fmpz_poly, nmod_mat

import row373_local_arithmetic as local


def ec_add(left, right, a, n):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u:
        if (y+v) % n == 0:
            return None
        assert y == v
        numerator, denominator = 3*x*x+a, 2*y
    else:
        numerator, denominator = v-y, u-x
    assert gcd(denominator,n) == 1
    slope = numerator*pow(denominator,-1,n) % n
    w = (slope*slope-x-u) % n
    return w, (slope*(x-w)-y) % n


def ec_mul(k, point, a, n):
    result = None
    for bit in bin(k)[2:]:
        result = ec_add(result,result,a,n)
        if bit == "1":
            result = ec_add(result,point,a,n)
    return result


def verify_primes(certificates):
    proved = set()

    def lucas(n):
        if n in proved:
            return
        assert n >= 2
        if n <= 1000:
            assert all(n % q for q in range(2,isqrt(n)+1))
        else:
            rows = certificates["lucas"][str(n)]
            assert len({q for q,_,_ in rows}) == len(rows)
            assert all(2 <= q < n and e >= 1 for q,e,_ in rows)
            assert prod(q**e for q,e,_ in rows) == n-1
            for q,_,a in rows:
                lucas(q)
                assert pow(a,n-1,n) == 1
                assert gcd(pow(a,(n-1)//q,n)-1,n) == 1
        proved.add(n)

    primes = certificates["odd_primes"]
    assert len(primes) == len(set(primes)) == 6 and all(p % 2 for p in primes)
    ec_steps = 0
    for n in primes:
        chain = certificates["ecpp"].get(str(n))
        if chain is None:
            lucas(n)
            continue
        expected = n
        for N,trace,s,a,point in chain:
            assert N == expected and N > 3 and N % 2
            assert trace**2 < 4*N and s > 0
            q,r = divmod(N+1-trace,s)
            assert r == 0 and (isqrt(isqrt(N))+2)**2 < q < N
            x,y = (c % N for c in point)
            b = (y*y-x*x*x-a*x) % N
            assert gcd(4*a**3+27*b*b,N) == 1
            nonzero = ec_mul(s,(x,y),a,N)
            assert nonzero is not None
            u,v = nonzero
            assert (v*v-u*u*u-a*u-b) % N == 0
            assert ec_mul(q,nonzero,a,N) is None
            expected = q
            ec_steps += 1
        lucas(expected)
    assert ec_steps == 9 and set(map(int,certificates["lucas"])) <= proved
    return primes, ec_steps


def verify_node(f, modulus):
    ring = fmpz_mod_poly_ctx(modulus)
    ff = ring(list(map(int,f)))
    fp = ff.derivative()
    a,b = ff,fp
    A,B = (ring([1]),ring([])), (ring([]),ring([1]))
    steps = 0
    while b:
        assert gcd(int(b.leading_coefficient()),modulus) == 1
        q,r = divmod(a,b)
        a,b = b,r
        A,B = B,(A[0]-q*B[0],A[1]-q*B[1])
        steps += 1
    assert a.degree() == 1
    inv = pow(int(a.leading_coefficient()),-1,modulus)
    g = a*inv
    assert g[1] == 1 and inv*(A[0]*ff+A[1]*fp) == g
    root = -int(g[0]) % modulus
    assert ff(root) == fp(root) == 0
    assert gcd(int(fp.derivative()(root)),modulus) == 1
    return {"modulus":str(modulus),"root":str(root),"unit_divisions":steps}


def scaled_g(g_shift, ring):
    poly = []
    for i,c in enumerate(g_shift):
        c = int(c)
        if not c:
            poly.append(ring.zero)
            continue
        v = local.v2(c)
        k = 3*v+i-105
        assert k >= 0
        poly.append((c>>v)*ring.pi_powers[k] if k < local.PRECISION else ring.zero)
    return poly


def verify_units(root, f, g):
    x = fmpz_poly([0,1])
    thetas = local.local_roots(f(x-1))
    wvals = []
    for theta in thetas:
        ring = theta.ring
        w0 = ring.sqrt_residue(theta.digit(0))
        w = ring.hensel(scaled_g(g(x+1),ring),ring.zero,w0)
        assert theta == -w*w-ring.pi**2*w and w.valuation() == 0
        wvals.append(w)

    local_image = json.loads((root/"row373_kummer2_membership.json").read_text())
    masks = [int(v,16) for v in local_image["parity_equations"]]
    basis = [int(v,16) for v in local_image["basis"]]
    assert len(masks) == 54 and len(basis) == 53
    assert all((b&m).bit_count() % 2 == 0 for b in basis for m in masks)

    t_norm = -int(g(1))
    assert t_norm == 2**35
    rows = json.loads((root/"unit_witnesses.json").read_text())
    obstruction = []
    for witness in rows:
        h = fmpz_poly(witness["polynomial"])
        m, sign = witness["m"], witness["sign"]
        assert m >= 0 and sign in (-1,1)
        assert int(f.resultant(h)) == sign*t_norm**m
        shifted = h(x-1)
        digits = []
        for theta,w in zip(thetas,wvals):
            ring = theta.ring
            numerator = local.evaluate(ring.scaled_polynomial(shifted,m),theta)
            assert numerator.valuation() == 0
            unit = sign*numerator*ring.inverse(w)**m
            digits.append(ring.coordinate(unit))
        assert digits == witness["coordinates"]
        code = local.combine(digits)
        image = sum(((code&mask).bit_count() % 2)<<i for i,mask in enumerate(masks))
        assert image == int(witness["obs"],16)
        obstruction.append(image)

    span = local.Span()
    pivots = [span.add(v) for v in obstruction]
    assert len(pivots) == 17 and all(i is not None for i in pivots)
    matrix = nmod_mat([[(v>>i)&1 for i in sorted(pivots)] for v in obstruction],2)
    assert matrix.det() == 1
    return {"rank":17,"pivot_columns_zero_based":sorted(pivots),
            "minor_determinant_mod_2":int(matrix.det())}


def main():
    root = Path(__file__).resolve().parent
    source = json.loads((root/"curve_C29.json").read_text())
    f,a,b = (fmpz_poly(source[key]) for key in
             ("F_ascending","A_star_ascending","B_star_ascending"))
    x = fmpz_poly([0,1])
    g = a(-x*x)+x*b(-x*x)
    assert f == a*a+x*b*b
    assert f.degree() == g.degree() == 105 and f[105] == g[105] == 1
    assert f(-x*x) == g*g(-x)

    primes, ec_steps = verify_primes(json.loads((root/"prime_certificates.json").read_text()))
    assert primes[0] == 199
    odd = prod(primes)
    assert int(g.discriminant()) == -2**3640*odd
    assert int(f.discriminant()) == -2**7280*odd
    index = sum(i//3 for i in range(105))
    assert index == 1785
    order_disc = int(g.discriminant()) // 2**(2*index)
    assert order_disc == -2**70*odd
    nodes = [verify_node(f,modulus) for modulus in (199,odd//199)]
    units = verify_units(root,f,g)

    result = {
        "odd_discriminant_primes_all_exponent_one":primes,
        "elliptic_primality_steps":ec_steps,
        "field_discriminant":str(order_disc),
        "maximal_order_basis_in_rho":"(rho-1)^i / 2^floor(i/3), 0<=i<=104",
        "odd_nodal_certificates":nodes,
        "exceptional_odd_valuation_support":[],
        "dyadic_global_unit_obstructions":units,
    }
    (root/"row374_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print("six distinct odd primes proved, including nine exact elliptic steps")
    print("integer discriminants verified, all odd valuations of disc(F) at most one")
    print("two Euclidean certificates prove a unique double root at every odd bad prime")
    print("17 norm-one units, rank 17 of dyadic obstructions, minor determinant 1")
    print("unit candidate dimension <= 38, Selmer dimension <= 38 + dim Cl(K)[2]")


if __name__ == "__main__":
    main()
