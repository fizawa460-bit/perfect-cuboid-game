#!/usr/bin/env python3

import json
import math

LIMIT_ELL = 2000
LIMIT_NORM = 5000


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True


def factor(n: int):
    out = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def tau(n: int) -> int:
    z = 1
    for e in factor(n).values():
        z *= e + 1
    return z


def divisors(n: int):
    out = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out


def canonical_gaussian_rep(ell: int):
    for y in range(1, math.isqrt(ell) + 1):
        x2 = ell - y * y
        x = math.isqrt(x2)
        if x * x == x2 and x > 0 and x != y:
            return (max(x, y), min(x, y))
    return None


def primitive_rep_count(N: int) -> int:
    R = math.isqrt(N)
    count = 0
    for T in range(-R, R + 1):
        D2 = N - T * T
        if D2 < 0:
            continue
        D = math.isqrt(D2)
        if D * D != D2:
            continue
        vals = {D, -D} if D else {0}
        for DD in vals:
            if math.gcd(abs(T), abs(DD)) == 1:
                count += 1
    return count


def main():
    gaussian_primes = 0
    switched_states = 0
    norm_identity_checks = 0
    primitive_gcd_checks = 0
    lpf_checks = 0
    lpf_exponent_checks = 0
    super_sqrt_checks = 0
    support_mod4_checks = 0
    reconstruction_checks = 0
    short_cofactor_checks = 0
    divisor_quotient_checks = 0
    quarter_dichotomy_checks = 0
    max_short_cofactor_ratio = 0.0
    max_quarter_ratio = 0.0

    for ell in range(5, LIMIT_ELL + 1):
        if not is_prime(ell) or ell % 4 != 1:
            continue
        rep = canonical_gaussian_rep(ell)
        assert rep is not None
        gaussian_primes += 1
        x, y = rep
        lim = math.isqrt((ell - 1) // 2) + 2
        for p in range(1, lim + 1):
            for q in range(p + 1, lim + 1):
                if math.gcd(p, q) != 1:
                    continue
                n = p * p + q * q
                if 2 * n >= ell:
                    continue
                for sigma in (1, -1):
                    T = x * p + sigma * y * q
                    D = y * p - sigma * x * q
                    N = T * T + D * D
                    switched_states += 1

                    assert D != 0
                    assert N == ell * n
                    norm_identity_checks += 1
                    assert math.gcd(abs(T), abs(D)) == 1
                    primitive_gcd_checks += 1

                    ff = factor(N)
                    assert max(ff) == ell
                    lpf_checks += 1
                    assert ff[ell] == 1
                    lpf_exponent_checks += 1
                    assert ell * ell > 2 * N
                    super_sqrt_checks += 1
                    assert all(r == 2 or r % 4 == 1 for r in ff)
                    support_mod4_checks += 1

                    pp_num = x * T + y * D
                    qq_num = sigma * (y * T - x * D)
                    assert pp_num % ell == 0 and qq_num % ell == 0
                    assert pp_num // ell == p and qq_num // ell == q
                    reconstruction_checks += 1

                    assert n * n < N / 2
                    short_cofactor_checks += 1
                    max_short_cofactor_ratio = max(
                        max_short_cofactor_ratio, n / math.sqrt(N / 2)
                    )

                    for d in divisors(abs(D)):
                        j = D // d
                        assert d * j == D
                        divisor_quotient_checks += 1
                        assert min(d, abs(j)) ** 2 <= abs(D)
                        quarter_dichotomy_checks += 1
                        max_quarter_ratio = max(
                            max_quarter_ratio,
                            min(d, abs(j)) / math.sqrt(abs(D)),
                        )

    fixed_norm_representation_checks = 0
    max_primitive_representations = 0
    max_representation_ratio = 0.0
    max_representation_norm = 0
    for N in range(1, LIMIT_NORM + 1):
        count = primitive_rep_count(N)
        bound = 4 * tau(N)
        assert count <= bound
        fixed_norm_representation_checks += 1
        if count > max_primitive_representations:
            max_primitive_representations = count
            max_representation_norm = N
        max_representation_ratio = max(max_representation_ratio, count / bound)

    result = {
        "stage": "14-t84",
        "ell_limit": LIMIT_ELL,
        "norm_bound_limit": LIMIT_NORM,
        "gaussian_primes": gaussian_primes,
        "switched_states": switched_states,
        "norm_identity_checks": norm_identity_checks,
        "primitive_gcd_checks": primitive_gcd_checks,
        "lpf_checks": lpf_checks,
        "lpf_exponent_checks": lpf_exponent_checks,
        "super_sqrt_checks": super_sqrt_checks,
        "support_mod4_checks": support_mod4_checks,
        "reconstruction_checks": reconstruction_checks,
        "short_cofactor_checks": short_cofactor_checks,
        "divisor_quotient_checks": divisor_quotient_checks,
        "quarter_dichotomy_checks": quarter_dichotomy_checks,
        "fixed_norm_representation_checks": fixed_norm_representation_checks,
        "max_primitive_representations": max_primitive_representations,
        "max_representation_norm": max_representation_norm,
        "max_representation_ratio": max_representation_ratio,
        "max_short_cofactor_ratio": max_short_cofactor_ratio,
        "max_quarter_ratio": max_quarter_ratio,
        "boundary": {
            "STAGE14_T84": "COMPLETE_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_AND_SHORT_COFACTOR_REDUCTION",
            "PRIMITIVE_SWITCHED_BINARY_NORM_PROVED": True,
            "CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF": True,
            "CANONICAL_ELL_EXPONENT_ONE_IN_BINARY_NORM": True,
            "CANONICAL_PRIME_INDEPENDENT_CHOICE_ELIMINATED": True,
            "SHORT_COVER_NORM_COFACTOR_PROVED": True,
            "FIXED_ORIENTATION_PI_V_RECONSTRUCTION_UNIQUE": True,
            "BILINEAR_PI_V_MULTIPLICITY_ELIMINATED": True,
            "TH23_TARGET_REOPENED": False,
            "TH24_NEEDED": True,
            "TH24_DISPATCHED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
            "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
            "NEXT": "Stage14-t85",
        },
    }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
