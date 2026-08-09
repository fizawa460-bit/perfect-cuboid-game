#!/usr/bin/env python3
"""Stage14-t37: common-core orientation packets / fixed-ell saving audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd, sqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T36_DATA = ROOT / "stages/stage14/data/14-t36/fixed_direction_squareclass_energy.json"
OUT = ROOT / "stages/stage14/data/14-t37/common_core_fixed_ell_saving.json"


def primitive_gaussian_norm_admissible(n: int) -> bool:
    """Primitive x^2+y^2 norms have v2<=1 and no 3 mod 4 prime divisor."""
    assert n > 0
    v2 = 0
    while n % 2 == 0:
        n //= 2
        v2 += 1
    if v2 > 1:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            if p % 4 == 3:
                return False
            while n % p == 0:
                n //= p
        p += 2
    return n == 1 or n % 4 == 1


def common_core_audit(states):
    delta_hist = Counter()
    h_hist = Counter()
    a0_hist = Counter()
    b0_hist = Counter()
    t_hist = Counter()
    packets = set()
    primitive_checks = 0

    for s in states:
        m = s["m"]
        n = s["n"]
        eps = s["eps"]
        delta = s["delta"]
        ell = s["ell"]

        k = gcd(n, eps * m)
        assert n == k * delta
        h = eps * m // k
        assert gcd(delta, h) == 1

        g = gcd(eps, h)
        A0 = eps * delta // g
        B0 = h // g
        assert gcd(A0, B0) == 1
        assert m % B0 == 0
        t = m // B0
        assert n == A0 * t
        assert m == B0 * t

        # From B_min<=B and ell^2>4B in the t36 frozen population.
        assert ell > 2 * eps * m * delta
        assert ell > 2 * m
        assert ell > 2 * n

        assert primitive_gaussian_norm_admissible(m)
        assert primitive_gaussian_norm_admissible(n)
        primitive_checks += 2

        delta_hist[delta] += 1
        h_hist[h] += 1
        a0_hist[A0] += 1
        b0_hist[B0] += 1
        t_hist[t] += 1
        packets.add((eps, delta, h, A0, B0))

    assert len(states) == 1120
    assert primitive_checks == 2240
    assert len(packets) == 31
    assert dict(sorted(delta_hist.items())) == {
        1: 232, 5: 456, 13: 176, 17: 116,
        25: 64, 29: 44, 37: 20, 41: 12,
    }
    assert dict(sorted(h_hist.items())) == {1: 398, 2: 676, 5: 24, 10: 22}
    assert dict(sorted(b0_hist.items())) == {1: 790, 2: 284, 5: 46}
    assert dict(sorted(t_hist.items())) == {1: 882, 2: 130, 5: 108}

    return {
        "states_checked": len(states),
        "primitive_gaussian_norm_checks": primitive_checks,
        "unique_packets": len(packets),
        "delta_histogram": dict(sorted(delta_hist.items())),
        "h_histogram": dict(sorted(h_hist.items())),
        "A0_histogram": dict(sorted(a0_hist.items())),
        "B0_histogram": dict(sorted(b0_hist.items())),
        "t_histogram": dict(sorted(t_hist.items())),
        "all_common_core_identities": True,
        "all_super_sqrt_separation_checks": True,
    }


def reverse_squareclass_audit(states):
    fibers = defaultdict(list)
    for s in states:
        fibers[(s["p"], s["q"])].append(s)

    energy = 0
    max_mult = 0
    duplicate_pairs = 0
    multiplicity_hist = Counter()

    for fiber in fibers.values():
        classes = Counter(s["kernel"] for s in fiber)
        energy += sum(v * v for v in classes.values())
        max_mult = max(max_mult, max(classes.values()))
        for v in classes.values():
            multiplicity_hist[v] += 1
            duplicate_pairs += v * (v - 1) // 2

    assert len(fibers) == 216
    assert max(len(v) for v in fibers.values()) == 110
    assert energy == 1132
    assert max_mult == 2
    assert duplicate_pairs == 6
    assert dict(sorted(multiplicity_hist.items())) == {1: 1108, 2: 6}

    return {
        "ordered_cover_slope_fibers": len(fibers),
        "max_reverse_fiber": max(len(v) for v in fibers.values()),
        "reverse_squareclass_collision_energy": energy,
        "max_reverse_squareclass_multiplicity": max_mult,
        "duplicate_unordered_pairs": duplicate_pairs,
        "multiplicity_histogram": dict(sorted(multiplicity_hist.items())),
    }


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cbar(z):
    return (z[0], -z[1])


def cnorm(z):
    return z[0] * z[0] + z[1] * z[1]


def phi(c, z):
    zz = cmul(z, z)
    czz = cmul(c, zz)
    return czz[0] * czz[1]


def universal_form(a: int, b: int, p: int, q: int) -> int:
    return (b * b * p * p - a * a * q * q) * (b * b * q * q - a * a * p * p)


def orientation_factorization_audit():
    # (pi, alpha, beta, R, S).  The identity is algebraic and does not
    # require the synthetic samples to satisfy the physical positivity interval.
    samples = (
        ((2, 3), (1, 2), (2, 1), (1, 1), (2, 1)),
        ((4, 1), (2, 1), (1, 2), (2, 1), (1, 2)),
        ((5, 2), (1, 2), (3, 2), (1, 2), (2, 3)),
        ((6, 1), (2, 3), (1, 2), (2, 1), (3, 2)),
    )
    modes = ("visible_same", "visible_opposite", "invisible")
    checks = 0
    phi_factor_checks = 0

    for pi, alpha, beta, R, S in samples:
        U = cmul(beta, cmul(R, S))
        V = cmul(alpha, cmul(R, cbar(S)))
        for mode in modes:
            if mode == "visible_same":
                eta = pi
            elif mode == "visible_opposite":
                eta = cbar(pi)
            else:
                eta = (1, 0)

            A = cmul(pi, U)
            P = cmul(eta, V)
            F = universal_form(A[0], A[1], P[0], P[1])

            cS = cmul(cmul(cmul(pi, cbar(eta)), beta), cbar(alpha))
            cR = cmul(cmul(cmul(pi, eta), beta), alpha)
            t = cnorm(R) * cnorm(S)
            rhs = -(t * t) * phi(cR, R) * phi(cS, S)
            assert F == rhs
            checks += 1

            # Phi_c(x+iy) is exactly the product of two rational quadratics.
            for c, z in ((cR, R), (cS, S)):
                u, v = c
                x, y = z
                q1 = u * (x * x - y * y) - 2 * v * x * y
                q2 = v * (x * x - y * y) + 2 * u * x * y
                assert phi(c, z) == q1 * q2
                assert 4 * (u * u + v * v) > 0  # discriminant of both slope quadratics
                phi_factor_checks += 1

    assert checks == 12
    assert phi_factor_checks == 24
    return {
        "exact_common_core_squareclass_factorization_checks": checks,
        "phi_two_quadratic_factorization_checks": phi_factor_checks,
        "orientation_modes_checked": list(modes),
    }


def exponent_optimization_audit():
    rows = []
    for N in (64, 729, 4096, 15625):
        worst = -1.0
        worst_M = None
        for M in range(1, N + 1):
            forward = sqrt(M * N)
            packet = N * (M ** (-0.25))
            combined = min(forward, packet)
            if combined > worst:
                worst = combined
                worst_M = M
        target = N ** (5 / 6)
        assert worst <= target * (1 + 1e-12)
        rows.append({
            "N": N,
            "worst_M": worst_M,
            "worst_combined_bound": round(worst, 6),
            "N_5_6": round(target, 6),
            "ratio": round(worst / target, 6),
        })

    expected = [
        {"N": 64, "worst_M": 16, "worst_combined_bound": 32.0, "N_5_6": 32.0, "ratio": 1.0},
        {"N": 729, "worst_M": 81, "worst_combined_bound": 243.0, "N_5_6": 243.0, "ratio": 1.0},
        {"N": 4096, "worst_M": 256, "worst_combined_bound": 1024.0, "N_5_6": 1024.0, "ratio": 1.0},
        {"N": 15625, "worst_M": 625, "worst_combined_bound": 3125.0, "N_5_6": 3125.0, "ratio": 1.0},
    ]
    assert rows == expected
    return rows


def main():
    frozen36 = json.loads(T36_DATA.read_text())
    assert frozen36["decision"]["STAGE14_T36"] == (
        "COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_AND_FIBER_SQRT_SAVING"
    )
    assert frozen36["decision"]["LONG_FIBER_POWER_SAVING_PROVED"] is True
    assert frozen36["decision"]["SHORT_FIBER_ENDPOINT_POWER_SAVING_PROVED"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()

    common = common_core_audit(states)
    reverse = reverse_squareclass_audit(states)
    orientation = orientation_factorization_audit()
    optimization = exponent_optimization_audit()

    report = {
        "stage": "14-t37",
        "t36_frozen_reference": {
            "states": frozen36["finite_audit"]["total_states"],
            "forward_squareclass_collision_energy": frozen36["finite_audit"]["squareclass_collision_energy"],
            "signed_fixed_direction_cancellation": True,
        },
        "common_core": {
            "h_definition": "h=epsilon*m/k, k=gcd(n,epsilon*m)",
            "coprimality": "gcd(delta,h)=1",
            "reduced_ratio": "g=gcd(epsilon,h), A0=epsilon*delta/g, B0=h/g",
            "common_norm_core": "m=B0*t, n=A0*t",
            "super_sqrt_separation": "ell>2*epsilon*m*delta, hence ell>2m and ell>2n",
        },
        "reverse_squareclass": {
            "quartic": "g_pq(y)=(p^2-y^2*q^2)(q^2-y^2*p^2)",
            "branch_points": ["p/q", "-p/q", "q/p", "-q/p"],
            "energy": "E_V^rev<=K_V*B^o(1)",
            "target_bound": "R_V<=sqrt(K_V)*B^o(1)",
        },
        "orientation_packet": {
            "equal_norm_decomposition": "Z1=R*S, Z2=R*bar(S), N(R)N(S)=t up to units",
            "phi": "Phi_c(z)=Re(c*z^2)*Im(c*z^2)",
            "squareclass_factorization": "[F]=[-Phi_cR(R)*Phi_cS(S)]",
            "one_variable_collision": "B^o(1) by rational quadratic factorization + t22 bounded-height mechanism",
            "fixed_delta_h_target": "sqrt(M/h)*B^o(1)",
        },
        "shell_bound": {
            "N": "B/ell",
            "physical_delta_count": "O(N/M)",
            "small_h": "N*sqrt(H/M)*B^o(1)",
            "large_h": "N/sqrt(H)*B^o(1)",
            "balanced_H": "sqrt(M)",
            "packet_bound": "N*M^(-1/4)*B^o(1)",
            "t36_forward_bound": "N*sqrt(M/N)*B^o(1)",
            "combined": "N*min(sqrt(M/N),M^(-1/4))*B^o(1)",
            "worst_shell": "M=N^(2/3)",
            "uniform_fixed_ell_shell": "N^(5/6)*B^o(1)",
            "uniform_fixed_ell_total": "(B/ell)^(5/6)*B^o(1)",
        },
        "remaining_boundary": {
            "moving_canonical_prime": True,
            "large_ell_tiny_cofactor_endpoint": "N=B/ell=O(1)",
            "next_object": "Gaussian-prime spin/bilinear average over ell; fixed-ell analysis is already power-saving",
            "general_degree_ge_3_spin_theorem_directly_applies_to_Qi": False,
        },
        "finite_audit": {
            "common_core": common,
            "reverse_squareclass": reverse,
            "orientation_factorization": orientation,
            "optimization": optimization,
        },
        "decision": {
            "STAGE14_T37": "COMPLETE_COMMON_CORE_SPIN_FACTORIZATION_AND_FIXED_ELL_POWER_SAVING",
            "REVERSE_FIXED_COVER_SQUARECLASS_ENERGY": "K*B^o(1)",
            "DELTA_H_COMMON_CORE_IDENTITY": True,
            "SUPER_SQRT_ELL_SEPARATES_COFACTOR_NORMS": True,
            "EQUAL_NORM_GAUSSIAN_ORIENTATION_DECOMPOSITION": True,
            "COMMON_CORE_SQUARECLASS_FACTORIZATION": True,
            "ONE_VARIABLE_SPIN_SQUARECLASS_COLLISION": "B^o(1)",
            "SMALL_H_PACKET_BOUND": "N*sqrt(H/M)*B^o(1)",
            "LARGE_H_REVERSE_BOUND": "N/sqrt(H)*B^o(1)",
            "PACKET_OPTIMIZED_BOUND": "N*M^(-1/4)*B^o(1)",
            "FIXED_ELL_SHELL_COMBINED_BOUND": "N*min(sqrt(M/N),M^(-1/4))*B^o(1)",
            "FIXED_ELL_SHELL_UNIFORM_BOUND": "N^(5/6)*B^o(1)",
            "FIXED_ELL_NORM_INDEX_POWER_SAVING_PROVED": True,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t38 average the common-core Gaussian spin packets over the moving canonical prime ell, "
                "with special attention to N=B/ell=O(1); identify a Gaussian-prime bilinear/spin estimate "
                "that is actually valid in the degree-two Q(i) setting"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
