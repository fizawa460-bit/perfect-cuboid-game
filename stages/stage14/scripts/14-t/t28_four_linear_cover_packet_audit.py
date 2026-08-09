#!/usr/bin/env python3
"""Stage14-t28: four-linear cover packet and torsion-diagonal audit."""

from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t28/four_linear_cover_packet.json"
MAX_B = 2_000_000
SYN_AB_MAX = 40
SYN_PQ_MAX = 40


def is_square(n):
    if n < 0:
        return False
    s = isqrt(n)
    return s * s == n


def squarefree_core(n):
    n = abs(n)
    if n == 0:
        return 0
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def largest_odd_prime_factor(n):
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    ans = 1
    p = 3
    while p * p <= n:
        while n % p == 0:
            ans = p
            n //= p
        p += 2
    if n > 1:
        ans = max(ans, n)
    return ans


def ab_direction(a, b):
    assert 0 < a < b and gcd(a, b) == 1
    eps = 1 if (a & 1 and b & 1) else 2
    if eps == 1:
        r = (b - a) // 2
        u = (b + a) // 2
    else:
        r = b - a
        u = b + a
    C = eps * a * b
    D = eps * (a * a + b * b) // 2
    L = eps * (b * b - a * a) // 2
    h = 2 if eps == 1 else 1

    assert gcd(r, u) == 1 and u > r > 0
    assert h == (1 if (r & 1 and u & 1) else 2)
    assert D == h * (r * r + u * u) // 2
    assert C == h * (u * u - r * r) // 2
    assert L == h * r * u
    assert D * D - C * C == L * L
    assert D - L == eps * a * a
    assert D + L == eps * b * b
    assert C == eps * a * b

    Delta = 2 * a * b * (b * b - a * a) * (a * a + b * b)
    if eps == 1:
        assert Delta == 16 * r * u * C * D
    else:
        assert Delta == r * u * C * D
    return eps, r, u, C, D, L, Delta


def count_candidate_directions():
    total = 0
    top = 0
    max_b = isqrt(2 * MAX_B) + 2
    for b in range(2, max_b + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            eps = 1 if (a & 1 and b & 1) else 2
            D = eps * (a * a + b * b) // 2
            if D > MAX_B:
                continue
            ab_direction(a, b)
            total += 1
            if D > MAX_B // 2:
                top += 1
    assert total == 636640
    assert top == 318362
    return total, top


def synthetic_cover_audit():
    directions = 0
    interval_tuples = 0
    square_cover_hits = 0
    torsion_diagonal_hits = 0
    non_torsion_cover_hits = 0
    kernel_support_checks = 0
    diagonal_biquadrate_checks = 0
    largest_prime_kernel_visible = 0
    largest_prime_kernel_invisible = 0

    for b in range(2, SYN_AB_MAX + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            eps, r, u, C, D, L, Delta = ab_direction(a, b)
            directions += 1

            # Universal p=q=1 point: x=-C^2, y=2 C^2 L.
            x4 = -C * C
            y4 = 2 * C * C * L
            curve_rhs = x4 * (
                x4 * x4 + (4 * D * D - 2 * C * C) * x4 + C**4
            )
            assert y4 * y4 == curve_rhs
            # Duplication on y^2=x(x^2+A x+C^4):
            # x(2P)=(x^2-C^4)^2/(4y^2), hence x(2P4)=0.
            assert x4 * x4 == C**4 and y4 != 0

            pstar = max(
                largest_odd_prime_factor(r),
                largest_odd_prime_factor(u),
                largest_odd_prime_factor(C),
                largest_odd_prime_factor(D),
            )

            for q in range(1, SYN_PQ_MAX + 1):
                for p in range(1, SYN_PQ_MAX + 1):
                    if gcd(p, q) != 1:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue
                    interval_tuples += 1

                    g1 = b * p - a * q
                    g2 = a * q + b * p
                    g3 = b * q - a * p
                    g4 = b * q + a * p
                    assert min(g1, g2, g3, g4) > 0

                    W2 = (4 * D * D - 2 * C * C) * p * p * q * q \
                        - C * C * (p**4 + q**4)
                    prod = g1 * g2 * g3 * g4
                    assert W2 == eps * eps * prod

                    # Pairwise gcd support is controlled by the six determinants.
                    gs = (g1, g2, g3, g4)
                    dets = (
                        2 * a * b,
                        b * b - a * a,
                        a * a + b * b,
                        a * a + b * b,
                        b * b - a * a,
                        2 * a * b,
                    )
                    pairs = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
                    for (i, j), det in zip(pairs, dets):
                        assert det % gcd(gs[i], gs[j]) == 0

                    if not is_square(prod):
                        continue
                    square_cover_hits += 1
                    W = eps * isqrt(prod)
                    assert W * W == W2

                    ds = tuple(squarefree_core(z) for z in gs)
                    zs = tuple(isqrt(z // d) for z, d in zip(gs, ds))
                    assert all(d * z * z == g for d, z, g in zip(ds, zs, gs))
                    assert all(Delta % d == 0 for d in ds)
                    dprod = ds[0] * ds[1] * ds[2] * ds[3]
                    assert is_square(dprod)
                    kernel_support_checks += 1

                    lhs = ds[0]**2 * zs[0]**4 + ds[3]**2 * zs[3]**4
                    rhs = ds[1]**2 * zs[1]**4 + ds[2]**2 * zs[2]**4
                    assert lhs == rhs
                    diagonal_biquadrate_checks += 1

                    if p == q:
                        assert p == 1
                        assert g1 == g3 and g2 == g4
                        torsion_diagonal_hits += 1
                    else:
                        assert not (g1 == g3 and g2 == g4)
                        non_torsion_cover_hits += 1
                        if pstar > 1 and any(d % pstar == 0 for d in ds):
                            largest_prime_kernel_visible += 1
                        else:
                            largest_prime_kernel_invisible += 1

    assert directions == 489
    assert interval_tuples == 239121
    assert square_cover_hits == 587
    assert torsion_diagonal_hits == 489
    assert non_torsion_cover_hits == 98
    assert kernel_support_checks == square_cover_hits
    assert diagonal_biquadrate_checks == square_cover_hits
    assert largest_prime_kernel_visible == 32
    assert largest_prime_kernel_invisible == 66

    return {
        "a_b_directions": directions,
        "physical_interval_primitive_pq_tuples": interval_tuples,
        "square_cover_hits": square_cover_hits,
        "universal_p_eq_q_order4_hits": torsion_diagonal_hits,
        "non_torsion_cover_hits": non_torsion_cover_hits,
        "kernel_support_checks": kernel_support_checks,
        "diagonal_biquadrate_checks": diagonal_biquadrate_checks,
        "non_torsion_largest_prime_kernel_visible": largest_prime_kernel_visible,
        "non_torsion_largest_prime_kernel_invisible": largest_prime_kernel_invisible,
    }


def main():
    total, top = count_candidate_directions()
    synthetic = synthetic_cover_audit()

    report = {
        "stage": "14-t28",
        "exact_reparametrization": {
            "epsilon_rule": "epsilon=1 for a,b odd; epsilon=2 for opposite parity",
            "D_minus_L": "epsilon*a^2",
            "D_plus_L": "epsilon*b^2",
            "C": "epsilon*a*b",
            "D": "epsilon*(a^2+b^2)/2",
            "L": "epsilon*(b^2-a^2)/2",
            "direction_bad_gcd_support": "Delta=2ab(b^2-a^2)(a^2+b^2)",
            "Delta_vs_ruCD": "Delta=16*r*u*C*D if epsilon=1, else Delta=r*u*C*D",
        },
        "four_linear_cover": {
            "physical_interval": "a/b < p/q < b/a",
            "g1": "b*p-a*q",
            "g2": "a*q+b*p",
            "g3": "b*q-a*p",
            "g4": "b*q+a*p",
            "identity": "W^2=epsilon^2*g1*g2*g3*g4",
            "universal_order4_diagonal": "p=q=1",
            "kernel_decomposition": "g_i=d_i*z_i^2, d_i squarefree, d_i|rad(Delta), product d_i square",
            "kernel_state_loss": "at most 8^omega(Delta)=X^o(1)",
            "weighted_biquadrate": "d1^2*z1^4+d4^2*z4^4=d2^2*z2^4+d3^2*z3^4",
            "non_torsion_condition": "not (g1=g3 and g2=g4), equivalently p!=q",
        },
        "analytic_boundary": {
            "canonical_largest_prime_kernel_visibility_guaranteed": False,
            "reason": "a large prime in ruCD can be absent from all four squarefree kernels; t26 Gaussian/dual routing remains necessary for that branch",
            "cover_only_count_without_torsion_removal_valid": False,
            "bonolis_browning_odd_degree_surface_theorem_directly_applicable": False,
            "reason_bonolis_browning": "the relevant fibre is an even quartic and has a universal rational 4-torsion section",
        },
        "finite_candidate_universe": {
            "max_B": MAX_B,
            "candidate_directions_D_le_B2m": total,
            "candidate_directions_top_shell_B2m": top,
        },
        "synthetic_cover_audit": synthetic,
        "decision": {
            "STAGE14_T28": "COMPLETE_FOUR_LINEAR_COVER_PACKET_AND_TORSION_DIAGONAL_REMOVAL",
            "TRIVIAL_KERNEL_COVER_FULL_2_TORSION": True,
            "UNIVERSAL_P_EQ_Q_POINT_EXACT_ORDER4": True,
            "FOUR_LINEAR_COVER_FACTORISATION": True,
            "PAIRWISE_GCD_SUPPORT_EQUALS_DIRECTION_ODD_SUPPORT": True,
            "FOUR_FACTOR_SQUAREFREE_KERNEL_PACKET": True,
            "FOUR_FACTOR_KERNEL_STATE_LOSS": "X^o(1)",
            "WEIGHTED_DIAGONAL_BIQUADRATE_REDUCTION": True,
            "CANONICAL_LARGE_PRIME_ALWAYS_KERNEL_VISIBLE": False,
            "COVER_ONLY_COUNTING_WITHOUT_TORSION_REMOVAL_VALID": False,
            "ROUTED_LARGE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t29 split non-torsion packets into largest-prime kernel-visible versus Gaussian/dual-invisible states and test square/polynomial-sieve incidence on the visible weighted biquadrate family",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_candidate_universe"], indent=2, sort_keys=True))
    print(json.dumps(report["synthetic_cover_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
