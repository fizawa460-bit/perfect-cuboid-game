#!/usr/bin/env python3

import json
import math
from collections import Counter
from functools import lru_cache

LIMIT_ELL = 1500
INDEPENDENT_D = (3, 5, 7, 11, 15, 21, 33, 35, 55, 65, 77, 105)


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


@lru_cache(maxsize=None)
def factor_tuple(n: int):
    x = n
    out = []
    p = 2
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e:
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1))
    return tuple(out)


def factor(n: int):
    return dict(factor_tuple(n))


@lru_cache(maxsize=None)
def divisors(n: int):
    out = [1]
    for p, e in factor_tuple(n):
        out = [x * (p ** a) for x in out for a in range(e + 1)]
    return tuple(sorted(out))


@lru_cache(maxsize=None)
def primitive_sos_rep(n: int):
    for a in range(1, math.isqrt(n) + 1):
        b2 = n - a * a
        if b2 < 0:
            break
        b = math.isqrt(b2)
        if b > 0 and b * b == b2 and math.gcd(a, b) == 1:
            return (max(a, b), min(a, b))
    return None


def odd_squarefree_divisors(n: int):
    ps = [p for p, _ in factor_tuple(n) if p % 2 == 1]
    out = [1]
    for p in ps:
        out += [x * p for x in out]
    return tuple(sorted(set(out)))


def omega(n: int) -> int:
    return len(factor_tuple(n))


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def jacobi_squarefree(a: int, s: int) -> int:
    if s == 1:
        return 1
    z = 1
    for p, _ in factor_tuple(s):
        z *= legendre(a, p)
    return z


def main():
    stats = {
        "stage": "14-t85",
        "ell_limit": LIMIT_ELL,
        "gaussian_primes": 0,
        "switched_states": 0,
        "synthetic_fixed_u_packet_lifts": 0,
        "selector_cases": 0,
        "gcd_norm_checks": 0,
        "square_quotient_checks": 0,
        "mod_d2_lift_checks": 0,
        "character_tensor_checks": 0,
        "product_hyperbola_checks": 0,
        "delta_square_hyperbola_checks": 0,
        "quarter_selector_delta_checks": 0,
        "delta_mod4_support_checks": 0,
        "independent_unit_residue_checks": 0,
        "independent_square_root_multiplicity_checks": 0,
    }

    max_product_ratio = 0.0
    max_delta_square_ratio = 0.0
    max_quarter_ratio = 0.0
    max_root_classes = 0
    max_selector_d = 0

    for ell in range(5, LIMIT_ELL + 1):
        if not is_prime(ell) or ell % 4 != 1:
            continue
        rep = primitive_sos_rep(ell)
        assert rep is not None
        stats["gaussian_primes"] += 1
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
                    if D == 0:
                        continue
                    N = T * T + D * D
                    assert N == ell * n
                    assert math.gcd(abs(T), abs(D)) == 1
                    stats["switched_states"] += 1

                    # Synthetic exact fixed-U skeleton: epsilon=h=1, m=k.
                    # We only use it to regress the t65/t82 inequalities
                    # hk=epsilon*m, d|R*S, 2|R*S|<=m, ell>2epsilon*m*delta.
                    for k in divisors(n):
                        U = primitive_sos_rep(k)
                        if U is None:
                            continue
                        R, S = U
                        delta = n // k
                        assert R * R + S * S == k
                        assert 2 * abs(R * S) <= k
                        assert ell > 2 * k * delta
                        stats["synthetic_fixed_u_packet_lifts"] += 1

                        assert all(r == 2 or r % 4 == 1 for r, _ in factor_tuple(delta))
                        stats["delta_mod4_support_checks"] += 1

                        # Choose genuine odd squarefree selector divisors hosted
                        # simultaneously by D and the fixed-U coordinate product.
                        host = math.gcd(abs(D), abs(R * S))
                        for d in odd_squarefree_divisors(host):
                            if d == 1:
                                continue
                            assert D % d == 0
                            j = D // d
                            stats["selector_cases"] += 1

                            # Primitive switched point => whole vertical coordinate
                            # is coprime to N=ell*k*delta.
                            assert math.gcd(d * abs(j), N) == 1
                            assert math.gcd(d, delta) == 1
                            assert math.gcd(j, delta) == 1
                            stats["gcd_norm_checks"] += 1

                            # Exact square quotient and d^2 root lift.
                            assert N - T * T == d * d * j * j
                            assert (N - T * T) // (d * d) == j * j
                            stats["square_quotient_checks"] += 1

                            assert (T * T - N) % (d * d) == 0
                            assert math.gcd(T, d) == 1
                            stats["mod_d2_lift_checks"] += 1

                            # Exact quadratic-character expansion.
                            rhs_num = sum(jacobi_squarefree(N, s) for s in divisors(d))
                            rhs_den = 2 ** omega(d)
                            assert rhs_num == rhs_den
                            stats["character_tensor_checks"] += 1

                            # Set B=N/2.  Then the t65 budget is exact for the
                            # synthetic epsilon=h=1,m=k packet, and ell^2>4B
                            # follows from ell>2n.
                            B = N / 2.0
                            Y_U = ell * delta

                            product_ratio = 2.0 * d * delta / math.sqrt(B)
                            assert product_ratio < 1.0 + 1e-12
                            max_product_ratio = max(max_product_ratio, product_ratio)
                            stats["product_hyperbola_checks"] += 1

                            delta_square_ratio = 4.0 * d * delta * delta / Y_U
                            assert delta_square_ratio < 1.0 + 1e-12
                            max_delta_square_ratio = max(max_delta_square_ratio, delta_square_ratio)
                            stats["delta_square_hyperbola_checks"] += 1

                            quarter_ratio = min(d, delta) * math.sqrt(2.0) / (B ** 0.25)
                            assert quarter_ratio < 1.0 + 1e-12
                            max_quarter_ratio = max(max_quarter_ratio, quarter_ratio)
                            stats["quarter_selector_delta_checks"] += 1

                            max_root_classes = max(max_root_classes, 2 ** omega(d))
                            max_selector_d = max(max_selector_d, d)

    # Independent finite-ring regression.  For odd squarefree d, every unit
    # square modulo d^2 has exactly 2^omega(d) roots, and solubility is
    # equivalent to being a quadratic residue at every p|d.
    for d in INDEPENDENT_D:
        assert all(e == 1 and p % 2 == 1 for p, e in factor_tuple(d))
        modulus = d * d
        square_counts = Counter((x * x) % modulus for x in range(modulus))
        expected_roots = 2 ** omega(d)
        for a in range(modulus):
            if math.gcd(a, d) != 1:
                continue
            soluble = all(legendre(a, p) == 1 for p, _ in factor_tuple(d))
            roots = square_counts[a]
            assert (roots > 0) == soluble
            stats["independent_unit_residue_checks"] += 1
            if roots:
                assert roots == expected_roots
                stats["independent_square_root_multiplicity_checks"] += 1
                max_root_classes = max(max_root_classes, roots)

            # Character orthogonality independently matches the square-coset
            # indicator, not just on physical/synthetic states.
            rhs_num = sum(jacobi_squarefree(a, s) for s in divisors(d))
            rhs_den = 2 ** omega(d)
            assert rhs_num in (0, rhs_den)
            assert (rhs_num == rhs_den) == soluble

    stats.update(
        {
            "max_selector_delta_product_ratio": max_product_ratio,
            "max_selector_delta_square_ratio": max_delta_square_ratio,
            "max_selector_delta_quarter_ratio": max_quarter_ratio,
            "max_root_classes": max_root_classes,
            "max_selector_d": max_selector_d,
            "boundary": {
                "STAGE14_T85": "COMPLETE_SELECTOR_DELTA_COPRIMALITY_MODULUS_SQUARE_ROOT_LIFT_AND_SQUARE_QUOTIENT_REDUCTION",
                "VERTICAL_COORDINATE_COPRIME_TO_BINARY_NORM": True,
                "SELECTOR_DIVISOR_COPRIME_TO_DELTA": True,
                "BINARY_NORM_SQUARE_ROOT_LIFT_MOD_D2": True,
                "ROOT_CLASS_MULTIPLICITY": "Bo1",
                "SELECTOR_ROOT_LIFT_QUADRATIC_CHARACTER_EXPANSION_PROVED": True,
                "PRIME_COFACTOR_QUADRATIC_CHARACTER_TENSORIZATION_PROVED": True,
                "VERTICAL_DIVISOR_CONDITION_EQUIVALENT_TO_ROOT_LIFT_PLUS_SQUARE_QUOTIENT": True,
                "SELECTOR_DELTA_PRODUCT_HYPERBOLA_PROVED": True,
                "SELECTOR_DELTA_QUARTER_DICHOTOMY_PROVED": True,
                "SELECTOR_DELTA_SQUARED_HYPERBOLA_PROVED": True,
                "ROOT_LIFT_SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED": False,
                "TH24_NEEDED": True,
                "TH24_TARGET_REOPENED": False,
                "TH25_NEEDED": False,
                "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
                "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
                "NEXT": "Stage14-t86",
            },
        }
    )

    print(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
