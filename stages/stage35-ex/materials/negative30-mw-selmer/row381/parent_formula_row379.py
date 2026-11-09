#!/usr/bin/env python3
"""Verify GRH-conditional bounds for the four audited row378 split quotients."""

import argparse
from functools import partial
from hashlib import sha256
import json
from math import ceil, isqrt
from multiprocessing import Pool
from pathlib import Path

from flint import arb, ctx, nmod_poly

HERE = Path(__file__).resolve().parent
N = 105
R1 = 7
DISC = 117981248819779519774066150957208102315271607402605667641283959829993045399028658031316657246104332689903983273746149168969341985775210396795186114853102963382274291541213184
PARENT_SHA = {
    "curve_factors.json":"0eb486cfb6e11c20558d2176909bfb13f67effe1880500abac8508339c32cdc2",
    "row378_exact.json":"f4f616732f3985260959bb9751d6cf50810f46cd52d6ad0fb7b4a8a1991f39b4",
}
BOUND = {
    "both": (32, "0.009"),
    "sum": (16, "0.001"),
    "equal_case": (2, "0.07"),
    "one_zero_case": (2, "0.047"),
}


def parent(name):
    b = (HERE/name).read_bytes()
    assert sha256(b).hexdigest() == PARENT_SHA[name]
    return json.loads(b)


class TestFunction:
    def __init__(self, data):
        self.case = data["case"]
        self.degree = data["excluded_degree"]
        self.T = arb(data["support_twice"])/2
        g = data["weights"]
        assert len(g) > 1 and g == g[::-1] and min(g) >= 0 and max(g) > 0
        self.size = len(g)
        self.h = self.T / self.size
        c = [sum(a*b for a,b in zip(g, g[k:])) for k in range(self.size)] + [0]
        self.values = [arb(x)/c[0] for x in c]
        self.diff = [a-b for a,b in zip(self.values, self.values[1:])]

    def value(self, x):
        if x > self.T:
            return arb(0)
        assert x < self.T and x > 0
        j = int(float(x/self.h))
        assert 0 <= j < self.size and x >= j*self.h and x <= (j+1)*self.h
        return self.values[j] - self.diff[j]*(x/self.h-j)

    def arch_upper(self):
        # W(x)=(1+(r1/n)*(-1)^k)*exp(-(k+1/2)x) summed over k>=0.
        M = 8192
        ratio = arb(R1)/N
        result = arb(0)
        for k in range(M):
            lam = arb(2*k+1)/2
            q = (-lam*self.h).exp()
            poly = arb(0)
            for c in reversed(self.diff):
                poly = c+q*poly
            result += (1+(-1)**k*ratio)*(1-q)*poly/(self.h*lam**2)
        # 0 <= 1-F(x) <= L*x for x>=0 by global Lipschitz continuity.
        L = max(abs(x).upper() for x in self.diff)/self.h
        return result + (1+ratio)*L/(arb(M)-arb(1)/2)

    def prime_weights(self, lognorm):
        odd, even = arb(0), arb(0)
        m = 1
        q = (-lognorm/2).exp()
        inv_power = q
        while m*lognorm < self.T:
            value = self.value(m*lognorm)*inv_power
            if m % 2:
                odd += value
            else:
                even += value
            m += 1
            inv_power *= q
        assert m*lognorm > self.T
        return 2*lognorm*odd/N, 2*lognorm*even/N


def rational_primes(n):
    sieve = bytearray(b"\x01")*(n+1)
    sieve[:2] = b"\x00\x00"
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p::p] = b"\x00"*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]


def degree_one_count(coefficients, p):
    F = nmod_poly(coefficients,p)
    x = nmod_poly([0,1],p)
    return p, int(F.gcd(x.pow_mod(p,F)-x).degree())


def apply_prime(test, lp, degrees, mask):
    term = arb(0)
    for i,f in enumerate(degrees):
        odd, even = test.prime_weights(f*lp)
        if (mask >> i) & 1:
            term += even-odd/(test.degree-1)
        else:
            term += even+odd
    return term


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers",type=int,default=4)
    args = parser.parse_args()
    assert 1 <= args.workers <= 32
    ctx.prec = 128
    coeff = parent("curve_factors.json")["ascending_coefficients"][0]
    rows = parent("row378_exact.json")["prime_tables"]
    fixtures = json.loads((HERE/"test_functions.json").read_text())
    tests = [TestFunction(row) for row in fixtures]
    assert len(tests) == len(BOUND) and {t.case for t in tests} == set(BOUND)
    assert all(t.degree == BOUND[t.case][0] for t in tests)
    limit = ceil(float(max(t.T.exp() for t in tests).upper()))
    assert all(arb(limit)>t.T.exp() for t in tests)
    assert limit < 5003**2
    primes = rational_primes(limit)
    assert [r["p"] for r in rows] == [p for p in primes if 3<=p<=5003 and p!=199]

    # Parent row373 gives the residue degrees at 2. Row378 puts both in all four sets.
    contributions = {t.case: apply_prime(t,arb(2).log(),[7,28],0) for t in tests}
    # At 199 the theta order is maximal locally, but F has repeated roots.
    # Distinct factors give the prime-ideal norms. Use the unrestricted worst sign.
    _, bad = nmod_poly(coeff,199).factor()
    degrees199 = [g.degree() for g,_ in bad]
    assert sum(g.degree()*e for g,e in bad) == N
    for t in tests:
        contributions[t.case] += apply_prime(t,arb(199).log(),degrees199,(1<<len(bad))-1)
    for row in rows:
        p = row["p"]
        factors = row["factors_ascending"]
        _, decomposition = nmod_poly(coeff,p).factor()
        assert sorted(factors) == sorted([list(map(int,g)) for g,e in decomposition if e==1])
        degrees = [len(g)-1 for g in factors]
        assert sum(degrees) == N
        for t in tests:
            mask = row["possible_nonsplit_masks"][t.case]
            assert 0 <= mask < (1<<len(degrees))
            contributions[t.case] += apply_prime(t,arb(p).log(),degrees,mask)

    ps = [p for p in primes if p>5003]
    count = partial(degree_one_count,coeff)
    tail = {t.case: arb(0) for t in tests}
    degree_one = 0
    with Pool(args.workers) as pool:
        for p,r in pool.imap(count,ps,chunksize=96):
            if r==0:
                continue
            degree_one += r
            x = arb(p).log()
            weight = 2*r*x*(-x/2).exp()/N
            for t in tests:
                tail[t.case] -= weight*t.value(x)/(t.degree-1)

    C = arb.const_euler()+(8*arb.pi()).log()+arb(R1)*arb.pi()/(2*N)-arb(DISC).log()/N
    result = {"rational_prime_limit":limit,"tail_rational_primes":len(ps),
              "tail_degree_one_ideals":degree_one,"degrees_at_199":sorted(degrees199),"bounds":{}}
    for t in tests:
        I = t.arch_upper()
        score = C-I+contributions[t.case]+tail[t.case]
        threshold = BOUND[t.case][1]
        assert score > arb(threshold), (t.case,score,threshold)
        result["bounds"][t.case] = {
            "excluded_extension_degree_under_quadratic_Hecke_GRH":t.degree,
            "quotient_2_rank_upper_bound_under_GRH":t.degree.bit_length()-2,
            "certified_score_strictly_greater_than":threshold,
        }
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
