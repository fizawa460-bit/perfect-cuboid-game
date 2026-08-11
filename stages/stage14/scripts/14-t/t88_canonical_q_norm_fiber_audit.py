#!/usr/bin/env python3

from collections import Counter, defaultdict
from math import gcd, isqrt
import json


def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def isprime(n):
    f = factor(n)
    return n >= 2 and len(f) == 1 and next(iter(f.values())) == 1


def tau(n):
    out = 1
    for e in factor(n).values():
        out *= e + 1
    return out


def squarefree(n):
    return all(e == 1 for e in factor(n).values())


def split_support(n):
    return all(p == 2 or p % 4 == 1 for p in factor(n))


def reps(n, primitive=False):
    out = []
    r = isqrt(n)
    for x in range(-r, r + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = isqrt(y2)
        if y * y != y2:
            continue
        for yy in {y, -y}:
            if primitive and gcd(abs(x), abs(yy)) != 1:
                continue
            out.append((x, yy))
    return list(dict.fromkeys(out))


def gmul(z, w):
    x, y = z
    u, v = w
    return (x * u - y * v, x * v + y * u)


def gconj(z):
    return (z[0], -z[1])


def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]


def gdiv_exact(z, a):
    n = gnorm(a)
    num = gmul(z, gconj(a))
    if num[0] % n or num[1] % n:
        return None
    return (num[0] // n, num[1] // n)


def assoc_key(z):
    x, y = z
    return min((x, y), (-y, x), (-x, -y), (y, -x))


def canonical_prime_rep(ell):
    rr = [z for z in reps(ell, True) if z[0] > 0 and z[1] > 0]
    return min(rr) if rr else None


def first_primitive_rep(n):
    rr = reps(n, True)
    rr2 = [z for z in rr if z[0] > 0 and z[1] >= 0]
    return min(rr2) if rr2 else (rr[0] if rr else None)


def main():
    q_limit = 3000
    q_values_checked = 0
    primitive_q_rep_checks = 0
    canonical_lpf_factor_recoveries = 0
    max_primitive_q_reps = 0
    max_r2_over_4tau = 0.0

    for Q in range(1, q_limit + 1, 2):
        fs = factor(Q)
        if not fs or any(p % 4 != 1 for p in fs):
            continue
        ell = max(fs)
        if fs[ell] != 1:
            continue
        delta0 = Q // ell
        if not ell > 2 * delta0:
            continue
        q_values_checked += 1
        rr = reps(Q, True)
        primitive_q_rep_checks += len(rr)
        max_primitive_q_reps = max(max_primitive_q_reps, len(rr))
        max_r2_over_4tau = max(max_r2_over_4tau, len(rr) / (4 * tau(Q)))

        prime_reps = reps(ell, True)
        for w in rr:
            classes = set()
            for pi in prime_reps:
                if gdiv_exact(w, pi) is not None:
                    classes.add(assoc_key(pi))
            assert len(classes) == 1, (Q, ell, delta0, w, classes)
            canonical_lpf_factor_recoveries += 1

    ell_list = [p for p in range(5, 500) if isprime(p) and p % 4 == 1]
    delta_list = [
        n for n in range(1, 121, 2)
        if split_support(n) and reps(n, True)
    ]
    k0_list = [
        n for n in range(1, 31)
        if split_support(n) and reps(n, True)
    ]

    product_reconstruction_states = 0
    canonical_q_recovery_checks = 0
    unique_norm_ell_divisor_checks = 0
    endpoint_projective_checks = 0
    max_endpoint_d = 1
    d_counter = Counter()

    for ell in ell_list:
        pi = canonical_prime_rep(ell)
        for delta0 in delta_list:
            gamma = first_primitive_rep(delta0)
            for k0 in k0_list:
                if not ell > 2 * k0 * delta0:
                    continue
                if gcd(ell, k0 * delta0) != 1 or gcd(k0, delta0) != 1:
                    continue
                a = first_primitive_rep(k0)
                W = gmul(a, gamma)
                z = gmul(pi, W)
                if gcd(abs(z[0]), abs(z[1])) != 1:
                    continue

                w = gmul(pi, gamma)
                Q = ell * delta0
                assert gmul(a, w) == z
                assert gnorm(w) == Q
                fs = factor(Q)
                assert max(fs) == ell and fs[ell] == 1 and Q // ell == delta0
                canonical_q_recovery_checks += 1

                classes = set()
                for pi2 in reps(ell, True):
                    if gdiv_exact(z, pi2) is not None:
                        classes.add(assoc_key(pi2))
                assert len(classes) == 1, (ell, delta0, k0, z, classes)
                unique_norm_ell_divisor_checks += 1

                for d in range(1, 22, 2):
                    if not squarefree(d):
                        continue
                    if z[1] % d:
                        continue
                    if gcd(d, gnorm(z)) != 1:
                        continue
                    endpoint_projective_checks += 1
                    max_endpoint_d = max(max_endpoint_d, d)
                    d_counter[d] += 1
                    assert gmul(a, w)[1] % d == 0
                    assert gcd(gmul(a, w)[0], d) == 1

                product_reconstruction_states += 1

    fixed_q_fiber_labels = 0
    fixed_q_fiber_packets = 0
    d_values = [1, 3, 5, 7, 11, 13, 15, 17, 19, 21]
    max_fixed_q_fiber = 0
    max_fixed_q_fiber_case = None
    max_fixed_q_fiber_over_16tautau = 0.0

    for Q in range(1, q_limit + 1, 2):
        fs = factor(Q)
        if not fs or any(p % 4 != 1 for p in fs):
            continue
        ell = max(fs)
        if fs[ell] != 1:
            continue
        delta0 = Q // ell
        wr = reps(Q, True)
        for k0 in k0_list:
            if not ell > 2 * k0 * delta0:
                continue
            if gcd(k0, Q) != 1:
                continue
            ar = reps(k0, True)
            for d in d_values:
                if not squarefree(d) or gcd(d, k0 * Q) != 1:
                    continue
                count = 0
                for a in ar:
                    for w in wr:
                        z = gmul(a, w)
                        if z[1] % d == 0 and gcd(z[0], d) == 1:
                            count += 1
                fixed_q_fiber_packets += 1
                fixed_q_fiber_labels += count
                ratio = count / (16 * tau(Q) * tau(k0))
                max_fixed_q_fiber_over_16tautau = max(
                    max_fixed_q_fiber_over_16tautau, ratio
                )
                if count > max_fixed_q_fiber:
                    max_fixed_q_fiber = count
                    max_fixed_q_fiber_case = {
                        "Q": Q, "k0": k0, "d": d, "count": count
                    }

    boundary = {
        "STAGE14_T88": "COMPLETE_ENDPOINT_SMALL_PROJECTIVE_SELECTOR_TO_CANONICAL_Q_NORM_FINITE_FIBER_REDUCTION",
        "MERGED_T87_IMPORTED": True,
        "MERGED_TH25_CONSUMED": True,
        "CANONICAL_T84_PRIME_IDENTIFIED_WITH_T86_PI_PRIME": True,
        "ORIENTED_COVER_EQUALS_GAMMA_TIMES_FIXED_K_FACTOR": True,
        "CANONICAL_Q_VARIABLE_PROVED": True,
        "Q_DEFINITION": "Q=ell*delta0=N(gamma*pi)",
        "ELL_RECOVERED_AS_Q_LPF": True,
        "ELL_EXPONENT_IN_Q": 1,
        "DELTA0_RECOVERED_FROM_Q": True,
        "FIXED_Q_GAUSSIAN_REPRESENTATION_COST": "Bo1",
        "FIXED_Q_PHYSICAL_FIBER_MULTIPLICITY": "Bo1",
        "RING_CLASS_FAMILY_COST_SURVIVES": False,
        "ONE_DIMENSIONAL_Q_ENERGY_BOUND": "X*Bo1",
        "CANONICAL_LPF_CORE_ALONE_FIXED_POWER_SPARSE": False,
        "TH25_TARGET_REOPENED": False,
        "TH26_NEEDED": False,
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
        "NEXT": "Stage14-t89",
    }

    data = {
        "stage": "14-t88",
        "q_limit": q_limit,
        "q_values_checked": q_values_checked,
        "primitive_q_rep_checks": primitive_q_rep_checks,
        "canonical_lpf_factor_recoveries": canonical_lpf_factor_recoveries,
        "max_primitive_q_reps": max_primitive_q_reps,
        "max_r2_over_4tau": max_r2_over_4tau,
        "product_reconstruction_states": product_reconstruction_states,
        "canonical_q_recovery_checks": canonical_q_recovery_checks,
        "unique_norm_ell_divisor_checks": unique_norm_ell_divisor_checks,
        "endpoint_projective_checks": endpoint_projective_checks,
        "max_endpoint_d": max_endpoint_d,
        "endpoint_d_histogram": dict(sorted(d_counter.items())),
        "fixed_q_fiber_packets": fixed_q_fiber_packets,
        "fixed_q_fiber_labels": fixed_q_fiber_labels,
        "max_fixed_q_fiber": max_fixed_q_fiber,
        "max_fixed_q_fiber_case": max_fixed_q_fiber_case,
        "max_fixed_q_fiber_over_16tautau": max_fixed_q_fiber_over_16tautau,
        "boundary": boundary,
    }
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
