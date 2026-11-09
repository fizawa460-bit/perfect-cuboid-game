#!/usr/bin/env python3
"""Arb certificates for the three inequalities in the row382 zero-window proof."""
import argparse
import csv
import json
from collections import Counter
from fractions import Fraction as Q
from functools import partial
from hashlib import sha256
from math import comb, factorial, isqrt
from multiprocessing import Pool
from pathlib import Path

from flint import acb, arb, ctx, fmpq, nmod_poly

HERE = Path(__file__).resolve().parent
N = 105
DISC = 117981248819779519774066150957208102315271607402605667641283959829993045399028658031316657246104332689903983273746149168969341985775210396795186114853102963382274291541213184
SHA = {
    "curve_C29.json": "04542e2e37a75ce382ca7921d51aae9e3bcc690b6a03d514dcbc0a511205bd74",
    "row378_exact.json": "f4f616732f3985260959bb9751d6cf50810f46cd52d6ad0fb7b4a8a1991f39b4",
    "tail_roots_independent.csv": "572183b2eccf59e0d6327834b5dc957c6bcdffb37aecabf4a637574ac595bee7",
    "mod2_supports382.json": "71f40305ec4aab89384078d9cfb0a5d8c9306b10ac57d18df26eea70ec75b16b",
}
B = 5003
LIMIT = 1623500
A = Q(93, 10)
T = A + 5
LOW_T = Q(1, 4)
HIGH_T = Q(17, 5)
HIGH_TAIL = Q(15, 4)
LOW_U = Q(3, 100)
EPS = Q(17, 500)


def ball(q):
    q = Q(q)
    return arb(fmpq(q.numerator, q.denominator))


def interval(a, b):
    return arb(ball((a + b) / 2), ball((b - a) / 2))


def input_bytes(name):
    data = (HERE / name).read_bytes()
    assert sha256(data).hexdigest() == SHA[name], name
    return data


class Spline:
    def __init__(self):
        self.knots = [
            (a, (-1)**(j+k) * comb(2, j) * comb(10, k))
            for j in range(3) for k in range(11)
            if (a := T - j*A - k) > 0
        ]
        self.s = sum(c*a**11 for a, c in self.knots)
        self.d = -110*sum(c*a**9 for a, c in self.knots)/self.s
        assert self.s > 0 and self.d > 0
        self.norm = self.s / (factorial(11)*A*A)
        self.arb_knots = [(ball(a), c) for a, c in self.knots]
        self.arb_s = ball(self.s)

    def value(self, x):
        total = arb(0)
        for a, c in self.arb_knots:
            y = a-x
            if y > 0:
                total += c*y**11
            else:
                assert y < 0, (a, x)
        return total/self.arb_s

    def archimedean_bound(self, m=1024):
        total = arb(0)
        for k in range(m):
            lam = ball(Q(2*k+1, 2))
            inner = arb(0)
            for a, c in self.arb_knots:
                integral = (1-(-lam*a).exp())/lam
                power = arb(1)
                for degree in range(1, 11):
                    power *= a
                    integral = (power-degree*integral)/lam
                inner += c*integral
            total += ball(1 + Q((-1)**k, 15))*11*inner/(lam*self.arb_s)
        tail = Q(16, 15)*self.d/(2*(m-Q(1, 2))**2)
        return total, ball(tail)


def primes_through(n):
    sieve = bytearray(b"\1")*(n+1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p::p] = b"\0"*((n-p*p)//p+1)
    return [p for p in range(2, n+1) if sieve[p]]


def forced_split():
    rels = [[tuple(p) for p in row] for row in json.loads(input_bytes("mod2_supports382.json"))]
    assert len(rels) == 4140 and all(len(row) == len(set(row)) for row in rels)
    labels = sorted({ideal for row in rels for ideal in row})
    bit = {ideal: 1 << i for i, ideal in enumerate(labels)}
    basis = {}

    def remainder(x):
        while x:
            r = basis.get(x & -x)
            if r is None:
                return x
            x ^= r
        return 0

    for row in rels:
        v = remainder(sum(bit[ideal] for ideal in row))
        if v:
            basis[v & -v] = v
    split = {ideal for ideal in labels if remainder(bit[ideal]) == 0}
    assert len(split) == 2492
    return split, len(basis)


def small_primes(coeff, primes):
    table = json.loads(input_bytes("row378_exact.json"))["prime_tables"]
    assert [r["p"] for r in table] == [p for p in primes if 3 <= p <= B and p != 199]
    out = {2: [7, 28]}
    for row in table:
        p = row["p"]
        _, factors = nmod_poly(coeff, p).factor()
        listed = row["factors_ascending"]
        actual = sorted((list(map(int, g)) for g, e in factors if e == 1),
                        key=lambda cs: (len(cs), cs))
        assert listed == actual and sum(len(g)-1 for g in listed) == N, p
        out[p] = [len(g)-1 for g in listed]
    _, factors199 = nmod_poly(coeff, 199).factor()
    assert sum(g.degree()*e for g, e in factors199) == N
    out[199] = sorted(g.degree() for g, _ in factors199)
    assert out[199] == [1, 27, 76]
    return out


def tail_primes(primes):
    lines = input_bytes("tail_roots_independent.csv").decode("ascii").splitlines()
    tail = [(int(p), int(c)) for p, c in csv.reader(lines) if int(p) <= LIMIT]
    assert [p for p, _ in tail] == [p for p in primes if p > B]
    assert all(0 <= c <= N for _, c in tail)
    return tail


def degree_one_count(coeff, p):
    f = nmod_poly(coeff, p)
    x = nmod_poly([0, 1], p)
    return p, int(f.gcd(x.pow_mod(p, f) - x).degree())


def prime_bounds(spline, degrees, tail, split):
    t = ball(T)
    total = arb(0)
    log_deriv = arb(0)
    tail_split = Counter(p for p, j in split if B < p <= LIMIT)
    tail_degrees = dict(tail)
    assert all(j < tail_degrees[p] for p, j in split if B < p <= LIMIT)
    assert all(j < len(degrees[p]) for p, j in split if p <= B)
    for p, fs in sorted(degrees.items()):
        logp = arb(p).log()
        for j, f in enumerate(fs):
            x = f*logp
            q = p**f
            log_deriv += x/(q*q-1)
            inv_sqrt = 1/arb(q).sqrt()
            weight = inv_sqrt
            m = 1
            while m*x < t:
                sign = 1 if p == 2 or (p, j) in split or m % 2 == 0 else -1
                total += sign*x*weight*spline.value(m*x)
                m += 1
                weight *= inv_sqrt
            assert m*x > t
    for p, c in tail:
        if c:
            logp = arb(p).log()
            total += (2*tail_split[p]-c)*logp/arb(p).sqrt()*spline.value(logp)
    # Above B, all prime ideals together are bounded by N times the
    # decreasing rational-integer sum for log n/(n^2-1).
    log_deriv += N*(arb(B).log()+1)/(B*(1-ball(Q(1, B**2))))
    return 2*total/N, log_deriv


def spectral_bounds(spline):
    eps = ball(EPS)
    one_half = ball(Q(3, 2))
    lengths = [ball(A)]+[arb(1)]*5
    norm = ball(spline.norm)
    assert ball(T)/10 < arb.pi()/2
    c0 = arb(1)
    for ell in lengths:
        c0 *= (2*(ell/4).cosh()/ell)**2
    c0 /= norm
    h = ball(HIGH_TAIL)
    ratio = c0*(4+h*h)/(one_half*h**12)
    assert ratio < eps

    def certified_rectangle(u_max, t_min, t_max):
        pending = [(Q(0), u_max, t_min, t_max, 0)]
        certified = 0
        max_depth = 0
        while pending:
            u0, u1, t0, t1, depth = pending.pop()
            u, t = interval(u0, u1), interval(t0, t1)
            z = acb(u, t)
            product = acb(1)
            for ell in lengths:
                v = ell*z/2
                product *= v.sinh()/v
            phi = (product**2/norm).real
            a, b = one_half-u, one_half+u
            w = (a/(a**2+t**2)+b/(b**2+t**2))/2
            if phi+eps*w > 0:
                certified += 1
                max_depth = max(max_depth, depth)
                continue
            assert depth < 36, (u0, u1, t0, t1, phi, w)
            if u1-u0 >= t1-t0:
                um = (u0+u1)/2
                pending.extend([(u0, um, t0, t1, depth+1), (um, u1, t0, t1, depth+1)])
            else:
                tm = (t0+t1)/2
                pending.extend([(u0, u1, t0, tm, depth+1), (u0, u1, tm, t1, depth+1)])
        return {"u_max": str(u_max), "t_min": str(t_min), "t_max": str(t_max),
                "certified_boxes": certified, "max_depth": max_depth}

    boxes = [
        certified_rectangle(Q(1, 2), Q(1, 10), LOW_T),
        certified_rectangle(LOW_U, LOW_T, HIGH_T),
        certified_rectangle(Q(1, 2), HIGH_T, HIGH_TAIL),
    ]
    return ratio, boxes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recount-tail", type=int, metavar="WORKERS", default=0)
    args = parser.parse_args()
    assert 0 <= args.recount_tail <= 32
    ctx.prec = 192
    assert ball(T).exp() < LIMIT < B**2
    spline = Spline()
    coeff = json.loads(input_bytes("curve_C29.json"))["F_ascending"]
    assert len(coeff) == N+1 and coeff[-1] == 1
    primes = primes_through(LIMIT)
    split, relation_rank = forced_split()
    small = small_primes(coeff, primes)
    tail = tail_primes(primes)
    if args.recount_tail:
        with Pool(args.recount_tail) as pool:
            actual = pool.imap(partial(degree_one_count, coeff), (p for p, _ in tail), chunksize=128)
            for expected, got in zip(tail, actual, strict=True):
                assert expected == got, (expected, got)
    prime_term, log_deriv = prime_bounds(spline, small, tail, split)
    arch_series, arch_tail = spline.archimedean_bound()
    logdisc = arb(DISC).log()
    pi = arb.pi()
    euler = arb.const_euler()
    score_lower_expression = euler+(8*pi).log()+pi/30-logdisc/N-arch_series-arch_tail+prime_term
    moment_upper_expression = logdisc/2+ball(Q(7, 2))*(-euler-pi.log()) + 49*(1-euler-(2*pi).log()) + log_deriv
    assert score_lower_expression > ball(Q(41, 1000)), score_lower_expression
    assert moment_upper_expression < 125, moment_upper_expression
    ratio, boxes = spectral_bounds(spline)
    assert N*Q(41, 1000) > 125*EPS
    print(json.dumps({
        "support_half_width": str(T), "F_raw_at_zero": str(spline.norm),
        "minus_F_second_derivative_at_zero": str(spline.d),
        "split_odd_ideal_count": len(split), "relation_rank": relation_rank,
        "prime_limit": LIMIT, "tail_rational_primes": len(tail),
        "tail_degree_one_ideals": sum(c for _, c in tail),
        "tail_recounted": bool(args.recount_tail),
        "score_lower_expression": str(score_lower_expression),
        "moment_upper_expression": str(moment_upper_expression),
        "score_strict_lower_bound": "41/1000", "moment_strict_upper_bound": 125,
        "tail_ratio_upper_expression": str(ratio), "epsilon": str(EPS),
        "certified_rectangles": boxes,
        "necessary_zero": {"real_part_strictly_above": str(Q(1, 2)+LOW_U),
                           "abs_imaginary_part_strictly_between": [str(LOW_T), str(HIGH_T)]}
    }, indent=2))


if __name__ == "__main__":
    main()
