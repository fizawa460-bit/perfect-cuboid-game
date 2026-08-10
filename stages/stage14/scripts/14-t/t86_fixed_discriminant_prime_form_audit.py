#!/usr/bin/env python3

import json
import math

LIMIT_ELL = 900
ROOT_ENUM_LIMIT = 200
GAUSS_EXTRACTION_NORM_LIMIT = 220


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def factor(n: int):
    n = abs(n)
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int):
    out = [1]
    for p, e in factor(n).items():
        base = list(out)
        pe = 1
        for _ in range(e):
            pe *= p
            out += [d * pe for d in base]
    return sorted(out)


def odd_squarefree_divisors(n: int):
    out = [1]
    for p in factor(n):
        if p % 2 == 0:
            continue
        out += [d * p for d in list(out)]
    return sorted(out)


def v2(n: int) -> int:
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def canonical_gaussian_rep(ell: int):
    for y in range(1, math.isqrt(ell) + 1):
        x2 = ell - y * y
        x = math.isqrt(x2)
        if x * x == x2 and x > 0 and x != y:
            return max(x, y), min(x, y)
    return None


def roots_minus_one(q: int):
    if q == 1:
        return [0]
    return [r for r in range(q) if (r * r + 1) % q == 0]


def root_count_formula(q: int) -> int:
    if q == 1:
        return 1
    return 2 ** len(factor(q))


def gaussian_norm(z):
    return z[0] * z[0] + z[1] * z[1]


def gaussian_reps_of_norm(n: int):
    out = []
    radius = math.isqrt(n)
    for a in range(-radius, radius + 1):
        b2 = n - a * a
        if b2 < 0:
            continue
        b = math.isqrt(b2)
        if b * b != b2:
            continue
        out.append((a, b))
        if b:
            out.append((a, -b))
    return out


def gaussian_divide_exact(z, g):
    ng = gaussian_norm(g)
    re_num = z[0] * g[0] + z[1] * g[1]
    im_num = z[1] * g[0] - z[0] * g[1]
    if re_num % ng or im_num % ng:
        return None
    return re_num // ng, im_num // ng


def find_gaussian_divisor_of_norm(z, target_norm: int):
    for g in gaussian_reps_of_norm(target_norm):
        quotient = gaussian_divide_exact(z, g)
        if quotient is not None:
            return g, quotient
    return None, None


def main():
    counts = {
        "gaussian_primes": 0,
        "switched_states": 0,
        "two_adic_absorption_checks": 0,
        "delta_root_orientation_checks": 0,
        "delta_root_multiplicity_enumerations": 0,
        "gaussian_delta_divisor_extractions": 0,
        "fixed_k_gaussian_peels": 0,
        "quotient_form_cases": 0,
        "quotient_form_identity_checks": 0,
        "fixed_discriminant_checks": 0,
        "primitive_form_checks": 0,
        "primitive_transformed_coordinate_checks": 0,
        "fixed_cofactor_prime_value_checks": 0,
        "independent_form_regressions": 0,
    }

    max_root_classes = 0
    max_delta0 = 0
    max_k0 = 0
    max_d = 0
    max_abs_s = 0
    max_form_coefficient = 0
    max_delta_gaussian_representation_count = 0

    for ell in range(5, LIMIT_ELL + 1):
        if not is_prime(ell) or ell % 4 != 1:
            continue
        rep = canonical_gaussian_rep(ell)
        assert rep is not None
        counts["gaussian_primes"] += 1
        x, y = rep

        lim = math.isqrt((ell - 1) // 2) + 1
        for p in range(1, lim + 1):
            for q in range(p + 1, lim + 1):
                if math.gcd(p, q) != 1:
                    continue
                n = p * p + q * q
                if 2 * n >= ell:
                    continue
                assert v2(n) <= 1

                for sigma in (1, -1):
                    T = x * p + sigma * y * q
                    D = y * p - sigma * x * q
                    if D == 0:
                        continue
                    assert T * T + D * D == ell * n
                    assert math.gcd(abs(T), abs(D)) == 1
                    counts["switched_states"] += 1

                    for delta in divisors(n):
                        k = n // delta
                        eta = 1 << v2(delta)
                        assert eta in (1, 2)
                        delta0 = delta // eta
                        k0 = eta * k
                        assert k0 * delta0 == n
                        assert math.gcd(abs(T), delta0) == 1
                        assert math.gcd(abs(D), delta0) == 1
                        counts["two_adic_absorption_checks"] += 1

                        if delta0 == 1:
                            rho0 = 0
                        else:
                            rho0 = (T * pow(D % delta0, -1, delta0)) % delta0
                            assert (rho0 * rho0 + 1) % delta0 == 0
                        counts["delta_root_orientation_checks"] += 1

                        root_count = root_count_formula(delta0)
                        max_root_classes = max(max_root_classes, root_count)
                        if delta0 <= ROOT_ENUM_LIMIT:
                            roots = roots_minus_one(delta0)
                            assert len(roots) == root_count
                            assert rho0 in roots
                            counts["delta_root_multiplicity_enumerations"] += 1

                        # Independent numerical verification of the Gaussian ideal
                        # interpretation in the small audit range.
                        if (
                            delta0 <= GAUSS_EXTRACTION_NORM_LIMIT
                            and k0 <= GAUSS_EXTRACTION_NORM_LIMIT
                        ):
                            gamma, w = find_gaussian_divisor_of_norm((T, D), delta0)
                            assert gamma is not None and w is not None
                            assert gaussian_norm(gamma) == delta0
                            assert gaussian_norm(w) == ell * k0
                            counts["gaussian_delta_divisor_extractions"] += 1

                            a, pi_q = find_gaussian_divisor_of_norm(w, k0)
                            assert a is not None and pi_q is not None
                            assert gaussian_norm(a) == k0
                            assert gaussian_norm(pi_q) == ell
                            assert is_prime(gaussian_norm(pi_q))
                            counts["fixed_k_gaussian_peels"] += 1
                            max_delta_gaussian_representation_count = max(
                                max_delta_gaussian_representation_count,
                                len(gaussian_reps_of_norm(delta0)),
                            )

                        for d in odd_squarefree_divisors(abs(D)):
                            j = D // d
                            assert math.gcd(abs(d * j), ell * k * delta) == 1
                            assert math.gcd(d, delta0) == 1
                            counts["quotient_form_cases"] += 1

                            rho = rho0
                            c = (rho * rho + 1) // delta0
                            assert rho * rho + 1 == c * delta0
                            assert (T - rho * d * j) % delta0 == 0
                            s = (T - rho * d * j) // delta0

                            F = (
                                delta0 * s * s
                                + 2 * rho * d * s * j
                                + c * d * d * j * j
                            )
                            assert F == ell * k0
                            counts["quotient_form_identity_checks"] += 1

                            disc = (2 * rho * d) ** 2 - 4 * delta0 * (c * d * d)
                            assert disc == -4 * d * d
                            counts["fixed_discriminant_checks"] += 1

                            assert math.gcd(
                                delta0,
                                math.gcd(abs(2 * rho * d), abs(c * d * d)),
                            ) == 1
                            counts["primitive_form_checks"] += 1

                            assert math.gcd(abs(s), abs(d * j)) == 1
                            counts["primitive_transformed_coordinate_checks"] += 1

                            ff = factor(F)
                            assert max(ff) == ell
                            assert ff[ell] == 1
                            assert F // ell == k0
                            assert math.gcd(ell, k0) == 1
                            assert ell > 2 * k0 * delta0
                            assert ell * ell > 2 * delta0 * F
                            counts["fixed_cofactor_prime_value_checks"] += 1

                            max_delta0 = max(max_delta0, delta0)
                            max_k0 = max(max_k0, k0)
                            max_d = max(max_d, d)
                            max_abs_s = max(max_abs_s, abs(s))
                            max_form_coefficient = max(
                                max_form_coefficient,
                                delta0,
                                abs(2 * rho * d),
                                abs(c * d * d),
                            )

    # Separate algebraic regression: arbitrary primitive transformed points in
    # several fixed-discriminant families.  These do not use primality.
    for d in (1, 3, 5, 7, 11, 15, 21):
        for delta0 in (1, 5, 13, 17, 25, 29, 37, 41, 65, 85):
            if math.gcd(d, delta0) != 1:
                continue
            for rho in roots_minus_one(delta0):
                c = (rho * rho + 1) // delta0
                for s in range(-4, 5):
                    for j in range(-4, 5):
                        if j == 0 or math.gcd(abs(s), abs(d * j)) != 1:
                            continue
                        T = rho * d * j + delta0 * s
                        D = d * j
                        F = (
                            delta0 * s * s
                            + 2 * rho * d * s * j
                            + c * d * d * j * j
                        )
                        assert T * T + D * D == delta0 * F
                        assert (2 * rho * d) ** 2 - 4 * delta0 * (c * d * d) == -4 * d * d
                        counts["independent_form_regressions"] += 1

    result = {
        "stage": "14-t86",
        "ell_limit": LIMIT_ELL,
        "root_enum_limit": ROOT_ENUM_LIMIT,
        "gauss_extraction_norm_limit": GAUSS_EXTRACTION_NORM_LIMIT,
        **counts,
        "max_root_classes": max_root_classes,
        "max_delta0": max_delta0,
        "max_k0": max_k0,
        "max_d": max_d,
        "max_abs_s": max_abs_s,
        "max_form_coefficient": max_form_coefficient,
        "max_delta_gaussian_representation_count": max_delta_gaussian_representation_count,
        "boundary": {
            "STAGE14_T86": "COMPLETE_COFACTOR_ROOT_LINE_TO_FIXED_DISCRIMINANT_FIXED_COFACTOR_PRIME_VALUE_FORM",
            "DELTA_ROOT_OF_MINUS_ONE_PROVED": True,
            "COFACTOR_ROOT_LINE_QUOTIENT_FORM_PROVED": True,
            "SQUARE_QUOTIENT_NONLINEARITY_ELIMINATED": True,
            "FIXED_DISCRIMINANT_REDUCTION_PROVED": True,
            "FORM_DISCRIMINANT": "-4*d^2",
            "PRIMITIVE_POSITIVE_DEFINITE_FORM_PROVED": True,
            "FIXED_COFACTOR_PRIME_VALUE_FORM_PROVED": True,
            "DELTA_GAUSSIAN_IDEAL_EXTRACTION_PROVED": True,
            "FIXED_K_GAUSSIAN_FACTOR_PEEL_PROVED": True,
            "TH24_CONSUMED": True,
            "TH24_TARGET_REOPENED": False,
            "TH25_NEEDED": True,
            "TH25_DISPATCHED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
            "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
            "NEXT": "Stage14-t87",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
