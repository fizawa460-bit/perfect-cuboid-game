#!/usr/bin/env python3
"""Rigorous modulated Poitou certificate for three class characters."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import partial
from itertools import product
from math import comb, factorial, prod
from multiprocessing import Pool
from pathlib import Path
import argparse
import csv
import json

from flint import acb, acb_series, arb, ctx

from row382_inputs import B, DISC, N, ball, forced_split, input_bytes
from row382_inputs import degree_one_count, interval, primes_through, small_primes

HERE = Path(__file__).resolve().parent
LIMIT = 1982760


class TestFunction:
    def __init__(self, fixture):
        lengths = list(map(Q, fixture["lengths"]))
        self.support = sum(lengths)
        self.degree = 2*len(lengths)-1
        self.lengths = list(map(ball, lengths))
        self.widths = [
            (ball(a/2), 2*k, [ball((a/2)**j/factorial(j)) for j in range(8)])
            for a, k in Counter(lengths).items()
        ]
        self.shifts = [(Q(a), Q(b)) for a, b in fixture["cosine_weights"]]
        assert sum(b for _, b in self.shifts) == 1
        assert self.shifts[0][0] == 0 and all(a > 0 for a, _ in self.shifts[1:])
        assert self.shifts[0][1] > sum(abs(b) for _, b in self.shifts[1:])
        self.modulation = [(ball(a), ball(b)) for a, b in self.shifts]
        self.modulation_size = ball(sum(abs(b) for _, b in self.shifts))

        knot_coeff = defaultdict(int)
        ranges = [
            [(j*a, (-1)**j*comb(2*k, j)) for j in range(2*k+1)]
            for a, k in Counter(lengths).items()
        ]
        for items in product(*ranges):
            a = self.support - sum(x for x, _ in items)
            if a > 0:
                knot_coeff[a] += prod(c for _, c in items)
        knots = [(a, c) for a, c in sorted(knot_coeff.items()) if c]
        sums = [sum(c*a**j for a, c in knots) for j in range(self.degree+1)]
        d = self.degree
        s = sums[d]
        norm = s/(factorial(d)*prod(a*a for a in lengths))
        assert s > 0 and norm > 0
        self.norm = ball(norm)
        self.s = ball(s)
        self.knots = [(ball(a), c) for a, c in knots]
        self.d_upper = ball(-d*(d-1)*sums[d-2]/s + sum(abs(b)*a*a for a, b in self.shifts))
        assert self.d_upper > 0
        self.arch_poly = [ball((-1)**j * factorial(d-1)//factorial(d-1-j) * sums[d-1-j])
                          for j in range(d)]

    def value(self, x):
        f = arb(0)
        for a, c in self.knots:
            y = a-x
            if y > 0:
                f += c*y**self.degree
            else:
                assert y < 0, (a, x)
        return f/self.s*sum(b*(a*x).cos() for a, b in self.modulation)

    def arch_upper(self, m=1024):
        total = arb(0)
        d = self.degree
        fact = factorial(d-1)
        phase = [
            [c*acb(0, a*v).exp() for a, c in self.knots]
            for v, _ in self.modulation
        ]
        steps = [(-a).exp() for a, _ in self.knots]
        decays = [(-a/2).exp() for a, _ in self.knots]
        for k in range(m):
            lam = ball(Q(2*k+1, 2))
            row = arb(0)
            for (v, b), phases in zip(self.modulation, phase, strict=True):
                inv = 1/acb(lam, -v)
                q = acb(0)
                for a in reversed(self.arch_poly):
                    q = q*inv+a
                e = sum(x*y for x, y in zip(phases, decays, strict=True))
                j = d*inv**2/self.s*(q-fact*inv**(d-1)*e)
                row += b*(1/lam - (inv-j).real)
            total += ball(1+Q((-1)**k, 15))*row
            decays = [x*y for x, y in zip(decays, steps, strict=True)]
        tail = ball(Q(16, 15)/(2*(m-Q(1,2))**2))*self.d_upper
        return total+tail, tail

    def phi0(self, z):
        val = acb(1)
        for ell in self.lengths:
            v = z*ell/2
            val *= acb(-v.imag, v.real).sinc()
        return val**2/self.norm

    def phi0_series(self, z):
        out = acb_series([1])
        for a, count, powers in self.widths:
            w = a*z
            sin, cos = w.sinh(), w.cosh()
            numerator = acb_series([k*(cos if j%2 else sin) for j,k in enumerate(powers)])
            out *= (numerator/acb_series([w,a]))**count
        return out/acb(self.norm)

    def transform_series(self, u, t):
        total = self.phi0_series(acb(u,t))*acb(self.modulation[0][1])
        for a, b in self.modulation[1:]:
            total += (self.phi0_series(acb(u,t+a))+self.phi0_series(acb(u,t-a)))*acb(b/2)
        return total

    def tail_constant(self):
        return prod((2*(ell/4).cosh()/ell)**2 for ell in self.lengths)/self.norm


def load_primes(recount_workers):
    coeff = json.loads(input_bytes("curve_C29.json"))["F_ascending"]
    primes = primes_through(LIMIT)
    split, rank = forced_split()
    small = small_primes(coeff, primes)
    tail = [(int(p), int(c)) for p,c in csv.reader(input_bytes("tail_roots_independent.csv").decode().splitlines())]
    assert [p for p, _ in tail] == [p for p in primes if p > B]
    assert len(tail) == 147058 and sum(c for _, c in tail) == 147527
    if recount_workers:
        with Pool(recount_workers) as pool:
            recount = pool.imap(partial(degree_one_count, coeff), (p for p,_ in tail), chunksize=128)
            for a,b in zip(tail,recount,strict=True):
                assert a == b, (a,b)
    counts = dict(tail)
    assert all(j < counts[p] for p, j in split if B < p <= LIMIT)
    assert all(j < len(small[p]) for p, j in split if p <= B)
    tail_splits = Counter(p for p, j in split if B < p <= LIMIT)
    return small, tail, split, tail_splits, rank


def prime_bounds(f, sigma, data, character_count):
    small, tail, split, tail_splits, _ = data
    t = ball(f.support)
    assert t.exp() < LIMIT < B**2
    unknown_odd = -arb(1)/character_count
    score_prime = arb(0)
    log_deriv = arb(0)
    for p, fs in sorted(small.items()):
        logp = arb(p).log()
        for j, d in enumerate(fs):
            x = d*logp
            forced = p == 2 or (p,j) in split
            q = (sigma*x).exp()
            log_deriv += -x/(q-1) if forced else x/(q+1)
            half = (-x/2).exp()
            w = half
            m = 1
            while m*x < t:
                sign = 1 if forced or m%2 == 0 else unknown_odd
                score_prime += sign*x*w*f.value(m*x)
                w *= half
                m += 1
            assert m*x > t

    for p, c in tail:
        if c == 0:
            continue
        x = arb(p).log()
        q = (sigma*x).exp()
        known = tail_splits[p]
        log_deriv += x*((c-known)/(q+1)-known/(q-1))
        if x < t:
            score_prime += (known+(c-known)*unknown_odd)*x/arb(p).sqrt()*f.value(x)
        else:
            assert x > t

    # Degree >=2 at rational p>B, using sum of residue degrees <= N
    # and the decreasing integral of log(x)/x^(2*sigma).
    s2 = 2*sigma-1
    log_b = arb(B).log()
    assert log_b > 1/(2*sigma)
    log_deriv += N*(log_b/s2+1/s2**2)*(-s2*log_b).exp()/(1-(-2*sigma*log_b).exp())
    # Degree 1 for p>LIMIT: Chebyshev theta(y) <= log(4)*y.
    l = arb(LIMIT).log()
    log_deriv += N*arb(4).log()*sigma/(sigma-1)*((1-sigma)*l).exp()/(1-(-sigma*l).exp())
    return 2*score_prime/N, log_deriv


def check_exterior(f, fixture):
    sigma = Q(fixture["hadamard_real_abscissa"])
    eps = ball(Q(fixture["epsilon"]))
    bands = [[Q(a), Q(b), Q(c)] for a,b,c in fixture["height_bands_and_u_max"]]
    high = Q(fixture["tail_height"])
    assert Q(1,10) < bands[0][0] and bands[-1][1] < high
    assert all(a<b and 0<c<Q(1,2) for a,b,c in bands)
    assert all(bands[j][1]<bands[j+1][0] for j in range(len(bands)-1))
    assert ball(f.support)/10 < arb.pi()/2
    assert high > max(a for a, _ in f.shifts)
    h = ball(high)
    ratio = f.tail_constant()*(ball(sigma)**2+h*h)/ball(sigma-Q(1,2))*sum(
        ball(abs(b)/(high-a)**(len(f.lengths)*2)) for a,b in f.shifts
    )
    assert ratio < eps, ratio
    centers = ball(sigma-Q(1,2))

    def check_rectangle(u_max, t_min, t_max):
        pending = [(Q(0), u_max, t_min, t_max, 0)]
        completed, max_depth = 0, 0
        while pending:
            u0, u1, t0, t1, depth = pending.pop()
            u, t = interval(u0,u1), interval(t0,t1)
            a, b = centers-u, centers+u
            w = (a/(a**2+t**2)+b/(b**2+t**2))/2
            du, dt = ball((u1-u0)/2), ball((t1-t0)/2)
            r = (du**2+dt**2).sqrt()
            if r < ball(Q(1, 10)):
                um, tm = ball((u0+u1)/2), ball((t0+t1)/2)
                series = f.transform_series(um,tm)
                variation = abs(series[1].real)*du+abs(series[1].imag)*dt
                variation += sum(abs(series[k])*r**k for k in range(2,8))
                outer = f.phi0(acb(um+ball(Q(1,2)))).real*f.modulation_size
                variation += outer*(2*r)**8/(1-2*r)
                g = series[0].real+eps*w-variation
                if g > 0:
                    completed += 1
                    max_depth = max(depth,max_depth)
                    continue
            assert depth < 42, (u0, u1, t0, t1)
            if u1-u0 >= t1-t0:
                mid = (u0+u1)/2
                pending.extend([(u0,mid,t0,t1,depth+1),(mid,u1,t0,t1,depth+1)])
            else:
                mid = (t0+t1)/2
                pending.extend([(u0,u1,t0,mid,depth+1),(u0,u1,mid,t1,depth+1)])
        return {"u_max":str(u_max),"t_min":str(t_min),"t_max":str(t_max),
                "boxes":completed,"max_depth":max_depth}

    gaps = list(zip([Q(1,10)]+[b for _,b,_ in bands], [a for a,_,_ in bands]+[high], strict=True))
    checked = [check_rectangle(Q(1,2),a,b) for a,b in gaps]
    checked += [check_rectangle(c,a,b) for a,b,c in bands]
    return str(ratio), checked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recount-tail", type=int, default=0, metavar="WORKERS")
    args = parser.parse_args()
    assert 0 <= args.recount_tail <= 32
    ctx.prec = 192
    ctx.cap = 8
    fixture = json.loads((HERE/"fixture384.json").read_text())
    sigma = ball(Q(fixture["hadamard_real_abscissa"]))
    f = TestFunction(fixture)
    data = load_primes(args.recount_tail)
    character_count = fixture["number_of_nontrivial_characters_in_average"]
    assert character_count == 3
    prime, deriv = prime_bounds(f,sigma,data,character_count)
    arch, tail = f.arch_upper()
    pi, gamma, logdisc = arb.pi(), arb.const_euler(), arb(DISC).log()
    score = gamma+(8*pi).log()+pi/30-logdisc/N-arch+prime
    moment = logdisc/2 + ball(Q(7,2))*((sigma/2).digamma()-pi.log()) + 49*(sigma.digamma()-(2*pi).log()) + deriv
    low_score = Q(fixture["score_threshold"])
    upper_moment = Q(fixture["moment_threshold"])
    eps = Q(fixture["epsilon"])
    assert score > ball(low_score), score
    assert moment < ball(upper_moment), moment
    assert N*low_score > eps*upper_moment
    result = {
        "prime_term_lower_expression":str(prime),"arch_upper_expression":str(arch),
        "arch_series_tail_upper":str(tail),"log_derivative_upper_expression":str(deriv),
        "average_score_lower_expression":str(score),"moment_upper_expression":str(moment),
        "uniform_odd_splits":len(data[2]),"principal_relation_rank":data[4],
        "tail_recounted":bool(args.recount_tail),
        "number_of_nontrivial_characters_in_average":character_count,
        "score_threshold":str(low_score),"moment_threshold":str(upper_moment),
        "contradiction_gap":str(N*low_score-eps*upper_moment)
    }
    ratio, boxes = check_exterior(f,fixture)
    result.update(tail_ratio_upper_expression=ratio, certified_rectangles=boxes,
                  necessary_bands=[{"abs_imaginary_part_in":[a,b],"real_part_gt":str(Q(1,2)+Q(c))}
                                   for a,b,c in fixture["height_bands_and_u_max"]])
    print(json.dumps(result,indent=2),flush=True)


if __name__ == "__main__":
    main()
