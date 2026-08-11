#!/usr/bin/env python3

import json
import math
from collections import defaultdict


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def representations(n: int):
    out = set()
    lim = math.isqrt(n)
    for x in range(-lim, lim + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = math.isqrt(y2)
        if y * y == y2:
            out.add((x, y))
            out.add((x, -y))
    return sorted(out)


def oddpart(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    while n % 2 == 0:
        n //= 2
    return n


def split_supported_odd(n: int) -> bool:
    if n % 2 == 0:
        return False
    x = n
    p = 3
    while p * p <= x:
        if x % p == 0:
            if p % 4 != 1:
                return False
            while x % p == 0:
                x //= p
        p += 2
    return x == 1 or x % 4 == 1


def largest_prime_factor(n: int) -> int:
    x = n
    ans = 1
    while x % 2 == 0:
        ans = 2
        x //= 2
    p = 3
    while p * p <= x:
        while x % p == 0:
            ans = p
            x //= p
        p += 2
    if x > 1:
        ans = max(ans, x)
    return ans


def tau(n: int) -> int:
    x = n
    ans = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                e += 1
                x //= p
            ans *= e + 1
        p += 1
    if x > 1:
        ans *= 2
    return ans


def main():
    k0_values = [1, 2, 5, 10, 13, 17, 25]
    h_values = [1, 2, 3, 5]
    ell_values = [p for p in range(5, 600) if is_prime(p) and p % 4 == 1]
    delta0_values = [n for n in range(1, 150, 2) if split_supported_odd(n)]

    weight = defaultdict(int)
    packet_q_checks = 0
    label_checks = 0
    linear_determinant_checks = 0
    max_abs_r = 0
    max_abs_t = 0
    max_q = 0
    max_delta0 = 0
    max_ell = 0

    for h in h_values:
        H = oddpart(h)
        for k0 in k0_values:
            a_reps = representations(k0)
            for delta0 in delta0_values:
                gamma_reps = [
                    g for g in representations(delta0)
                    if math.gcd(abs(g[0]), abs(g[1])) == 1
                ]
                if not gamma_reps:
                    continue

                for ell in ell_values:
                    # Synthetic packets are restricted to the exact t89 strong gap.
                    if ell <= 2 * h * k0 * delta0:
                        continue
                    if not any(x > 0 and y > 0 for x, y in representations(ell)):
                        continue

                    Q = ell * delta0
                    assert largest_prime_factor(Q) == ell
                    packet_q_checks += 1

                    for A, B in a_reps:
                        for u, v in gamma_reps:
                            for sigma in (1, -1):
                                # W_sigma=a*gamma=p-i*sigma*q.
                                p_coord = A * u - B * v
                                imag_w = A * v + B * u
                                q_coord = -sigma * imag_w
                                if p_coord == 0 or q_coord == 0:
                                    continue

                                r = q_coord - p_coord
                                t = q_coord + p_coord

                                # Exact linear-form/norm chart.
                                assert r * r + t * t == 2 * k0 * delta0

                                # Strong gap makes the inherited short-cover bounds automatic.
                                assert r * r < ell
                                assert t * t < ell
                                assert abs(r * t) < k0 * delta0

                                # Upper-envelope angular cofactor (g=1) already satisfies
                                # every t74/t75/t78 archimedean inequality after the
                                # t89 strong gap.  Any physical g>=1 only decreases c.
                                c_upper = H * oddpart(r * t)
                                assert 2 * c_upper < ell
                                assert ell * c_upper < h * k0 * Q
                                assert ell * H * oddpart(r * t) < h * k0 * Q

                                label_checks += 1
                                weight[(h, k0, Q)] += 1
                                max_abs_r = max(max_abs_r, abs(r))
                                max_abs_t = max(max_abs_t, abs(t))
                                max_q = max(max_q, Q)
                                max_delta0 = max(max_delta0, delta0)
                                max_ell = max(max_ell, ell)

    # Independent determinant check for the fixed integral chart.
    for k0 in k0_values:
        for A, B in representations(k0):
            for sigma in (1, -1):
                def rt(u, v):
                    p_coord = A * u - B * v
                    imag_w = A * v + B * u
                    q_coord = -sigma * imag_w
                    return q_coord - p_coord, q_coord + p_coord

                r10, t10 = rt(1, 0)
                r01, t01 = rt(0, 1)
                determinant = r10 * t01 - r01 * t10
                assert abs(determinant) == 2 * k0
                linear_determinant_checks += 1

    max_weight = max(weight.values())
    max_weight_case = max(weight, key=weight.get)
    max_weight_ratio = 0.0

    for (h, k0, Q), count in weight.items():
        ell = largest_prime_factor(Q)
        delta0 = Q // ell
        # r_2(k0) r_2(delta0) times two sigma labels is bounded by
        # 32*tau(k0)*tau(delta0).
        envelope = 32 * tau(k0) * tau(delta0)
        assert count <= envelope
        max_weight_ratio = max(max_weight_ratio, count / envelope)

    result = {
        "stage": "14-t89",
        "k0_values": k0_values,
        "h_values": h_values,
        "ell_values": len(ell_values),
        "delta0_values": len(delta0_values),
        "packet_q_checks": packet_q_checks,
        "label_checks": label_checks,
        "linear_determinant_checks": linear_determinant_checks,
        "weighted_q_packets": len(weight),
        "max_weight": max_weight,
        "max_weight_case": {
            "h": max_weight_case[0],
            "k0": max_weight_case[1],
            "Q": max_weight_case[2],
        },
        "max_weight_over_32_tau_tau": max_weight_ratio,
        "max_abs_r": max_abs_r,
        "max_abs_t": max_abs_t,
        "max_Q": max_q,
        "max_delta0": max_delta0,
        "max_ell": max_ell,
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
