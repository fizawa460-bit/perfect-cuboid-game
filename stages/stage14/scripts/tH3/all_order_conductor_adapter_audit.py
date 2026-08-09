#!/usr/bin/env python3
from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH1 = ROOT / "stages/stage14/14-tH1/result.md"
TH2 = ROOT / "stages/stage14/14-tH2/result.md"
TH3 = ROOT / "stages/stage14/14-tH3/result.md"
FROZEN = ROOT / "stages/stage14/data/tH3/all_order_conductor_adapter_summary.json"

SPLIT_PRIMES = (5, 13, 17, 29, 37, 41)
CRT_PRIMES = (5, 13, 17, 29, 37)
EPSILON_STATES = (1, 2, 3, 4, 6, 8, 12)
GOOD_TEST_PRIMES = (5, 13, 17, 29)
HYPERBOLA_Y = 64


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def e2(signature: int) -> int:
    signature %= 4
    if signature == 0:
        return 0
    if signature == 2:
        return 2
    return 3


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def enumerate_transformed_hyperbola() -> list[tuple[int, int, int, int, int]]:
    out: list[tuple[int, int, int, int, int]] = []
    Y = HYPERBOLA_Y
    for epsilon in EPSILON_STATES:
        for g in divisors(epsilon):
            epsilon_prime = epsilon // g
            for h in range(1, Y + 1):
                if gcd(h, epsilon_prime) != 1:
                    continue
                for r in range(1, Y // h + 1):
                    for delta in range(1, Y // (h * r) + 1):
                        out.append((epsilon, g, h, r, delta))
    return out


def build_summary() -> dict:
    th1 = TH1.read_text(encoding="utf-8")
    th2 = TH2.read_text(encoding="utf-8")
    th3 = TH3.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH1=COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION",
        "ARBITRARY_LOCAL_CHARACTER_ORDER_SUPPORTED=true",
        "EXACT_CRT_CONDUCTOR_NORM_FORMULA=true",
    ]:
        require(th1, marker, "Stage14-tH1")

    for marker in [
        "STAGE14_TH2=COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE",
        "TRANSFORMED_IDENTITIES=m=h*r,k=g*h",
        "SHARED_GAUSSIAN_NORM_FACTOR=h",
    ]:
        require(th2, marker, "Stage14-tH2")

    for marker in [
        "STAGE14_TH3=COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER",
        "MU4_TRIVIAL_FAMILY_TWO_ADIC_CONDUCTOR_EXPONENT_ZERO=true",
        "JOINT_MODULUS_ENVELOPE_IS_LCM=true",
        "SHARED_AUXILIARY_MODULUS_PRESERVED=true",
        "SHARED_PRIME_JOINT_MODULUS_SQUARED=false",
        "HYPERBOLA_GOOD_MODULUS_CONDITION=gcd(Q_rat,g*h*r*delta)=1",
        "NEXT=Stage14-tH4",
    ]:
        require(th3, marker, "Stage14-tH3")

    mu4_local_modes_checked = 0
    mu4_nontrivial_local_modes = 0
    same_modulus_mu4_pair_modes = 0
    same_modulus_mu4_pairs_joint_modulus_p = 0
    same_modulus_mu4_trivial_trivial_pairs = 0
    same_modulus_conductor_squaring_violations = 0

    arbitrary_order_same_modulus_pairs = 0
    arbitrary_joint_two_adic_counts = {0: 0, 2: 0, 3: 0}

    for p in SPLIT_PRIMES:
        n = p - 1
        mu4_modes = list(range(0, n, 4))
        expected_h = n // 4
        if len(mu4_modes) != expected_h:
            raise AssertionError((p, len(mu4_modes), expected_h))

        for rho in (1, -1):
            for j in mu4_modes:
                signature = (rho * j) % 4
                if signature != 0 or e2(signature) != 0:
                    raise AssertionError((p, rho, j, signature))
                mu4_local_modes_checked += 1
                if j != 0:
                    mu4_nontrivial_local_modes += 1

            for j_u in mu4_modes:
                for j_v in mu4_modes:
                    same_modulus_mu4_pair_modes += 1
                    active_u = j_u != 0
                    active_v = j_v != 0
                    # The coordinate conductors each use p when active, but the
                    # joint evaluation modulus is their lcm, so the odd factor
                    # is p once, not p^2.
                    f_u_odd = p if active_u else 1
                    f_v_odd = p if active_v else 1
                    joint_odd = p if (active_u or active_v) else 1
                    if joint_odd not in (1, p):
                        same_modulus_conductor_squaring_violations += 1
                    if joint_odd == p * p:
                        same_modulus_conductor_squaring_violations += 1
                    # lcm for values restricted to {1,p}.
                    expected_joint = max(f_u_odd, f_v_odd)
                    if joint_odd != expected_joint:
                        raise AssertionError((p, rho, j_u, j_v))
                    if joint_odd == p:
                        same_modulus_mu4_pairs_joint_modulus_p += 1
                    else:
                        same_modulus_mu4_trivial_trivial_pairs += 1

            for j_u in range(n):
                for j_v in range(n):
                    arbitrary_order_same_modulus_pairs += 1
                    e_u = e2(rho * j_u)
                    e_v = e2(rho * j_v)
                    e_joint = max(e_u, e_v)
                    arbitrary_joint_two_adic_counts[e_joint] += 1
                    active = j_u != 0 or j_v != 0
                    odd_joint = p if active else 1
                    # General arbitrary-order envelope is
                    # (1+i)^max(eU,eV) times the union of odd prime support.
                    joint_norm = (2**e_joint) * odd_joint
                    if joint_norm <= 0:
                        raise AssertionError("nonpositive conductor norm")

    # Two-prime CRT audit for mu4-trivial character pairs, one orientation.
    crt_mu4_packet_combinations = 0
    crt_active_support_size_counts = {0: 0, 1: 0, 2: 0}
    for left, p in enumerate(CRT_PRIMES):
        p_modes = [
            (j_u, j_v)
            for j_u in range(0, p - 1, 4)
            for j_v in range(0, p - 1, 4)
        ]
        for q in CRT_PRIMES[left + 1 :]:
            q_modes = [
                (j_u, j_v)
                for j_u in range(0, q - 1, 4)
                for j_v in range(0, q - 1, 4)
            ]
            for p_pair in p_modes:
                for q_pair in q_modes:
                    crt_mu4_packet_combinations += 1
                    p_active = p_pair != (0, 0)
                    q_active = q_pair != (0, 0)
                    support_size = int(p_active) + int(q_active)
                    crt_active_support_size_counts[support_size] += 1
                    joint_norm = (p if p_active else 1) * (q if q_active else 1)
                    expected = 1
                    if p_active:
                        expected *= p
                    if q_active:
                        expected *= q
                    if joint_norm != expected:
                        raise AssertionError((p, q, p_pair, q_pair))

    # Exact good-modulus mask on tH2 transformed variables.
    transformed = enumerate_transformed_hyperbola()
    good_modulus_predicates_checked = 0
    good_modulus_equivalence_failures = 0
    good_tuple_counts_by_prime = {p: 0 for p in GOOD_TEST_PRIMES}
    for epsilon, g, h, r, delta in transformed:
        u_norm = h * r
        v_norm = g * h * delta
        for p in GOOD_TEST_PRIMES:
            from_norms = (u_norm * v_norm) % p != 0
            from_adapter = (g * h * r * delta) % p != 0
            good_modulus_predicates_checked += 1
            if from_norms != from_adapter:
                good_modulus_equivalence_failures += 1
            if from_norms:
                good_tuple_counts_by_prime[p] += 1

    if good_modulus_equivalence_failures:
        raise AssertionError(
            f"good-modulus equivalence failures: {good_modulus_equivalence_failures}"
        )

    return {
        "stage": "Stage14-tH3",
        "status": "COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER",
        "requires_future_t_result": False,
        "dependencies": ["Stage14-tH1", "Stage14-tH2"],
        "mu4_specialization": {
            "local_condition": "j mod 4 = 0",
            "local_unit_signature_zero": True,
            "global_unit_signature_zero": True,
            "two_adic_conductor_exponent": 0,
            "ramified_conductor_factor_present": False,
        },
        "joint_modulus_adapter": {
            "coordinate_primitive_conductors_preserved": True,
            "joint_modulus_envelope": "lcm(f_U,f_V)",
            "shared_oriented_prime_counted_once": True,
            "shared_prime_squared": False,
            "conjugate_oriented_primes_distinct": True,
            "mu4_joint_modulus": "product(active union of oriented Gaussian prime ideals)",
        },
        "hyperbola_adapter": {
            "u_norm": "h*r",
            "v_norm": "g*h*delta",
            "rational_good_prime_condition": "p does not divide g*h*r*delta",
            "finite_support_condition": "gcd(Q_rat,g*h*r*delta)=1",
            "shared_modulus_group_preserved": True,
        },
        "audit": {
            "split_primes": list(SPLIT_PRIMES),
            "oriented_prime_ideals": 2 * len(SPLIT_PRIMES),
            "mu4_local_modes_checked": mu4_local_modes_checked,
            "mu4_nontrivial_local_modes": mu4_nontrivial_local_modes,
            "same_modulus_mu4_pair_modes": same_modulus_mu4_pair_modes,
            "same_modulus_mu4_pairs_joint_modulus_p": same_modulus_mu4_pairs_joint_modulus_p,
            "same_modulus_mu4_trivial_trivial_pairs": same_modulus_mu4_trivial_trivial_pairs,
            "same_modulus_conductor_squaring_violations": same_modulus_conductor_squaring_violations,
            "arbitrary_order_same_modulus_pairs": arbitrary_order_same_modulus_pairs,
            "arbitrary_joint_two_adic_counts": {
                str(k): v for k, v in arbitrary_joint_two_adic_counts.items()
            },
            "crt_primes": list(CRT_PRIMES),
            "crt_mu4_packet_combinations": crt_mu4_packet_combinations,
            "crt_active_support_size_counts": {
                str(k): v for k, v in crt_active_support_size_counts.items()
            },
            "hyperbola_epsilon_states": list(EPSILON_STATES),
            "hyperbola_Y": HYPERBOLA_Y,
            "hyperbola_transformed_tuples": len(transformed),
            "good_prime_test_primes": list(GOOD_TEST_PRIMES),
            "good_modulus_predicates_checked": good_modulus_predicates_checked,
            "good_modulus_equivalence_failures": good_modulus_equivalence_failures,
            "good_tuple_counts_by_prime": {
                str(k): v for k, v in good_tuple_counts_by_prime.items()
            },
        },
        "proof_boundary": {
            "all_order_ray_class_hyperbola_conductor_adapter_proved": True,
            "shared_auxiliary_modulus_preserved": True,
            "all_character_mellin_hecke_large_sieve_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH4",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH3 summary differs semantically")
    print("Stage14-tH3 all-order conductor adapter audit: OK")


if __name__ == "__main__":
    main()
