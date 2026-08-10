#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH2 = ROOT / "stages/stage14/14-tH2/result.md"
TH3 = ROOT / "stages/stage14/14-tH3/result.md"
TH4 = ROOT / "stages/stage14/14-tH4/result.md"
TH5 = ROOT / "stages/stage14/14-tH5/result.md"
FROZEN = ROOT / "stages/stage14/data/tH5/gaussian_pair_collision_energy_summary.json"

EPSILON_STATES = (1, 2, 3, 4, 6, 8, 12)
Y = 128


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def tau(n: int) -> int:
    return len(divisors(n))


def r2(n: int) -> int:
    d1 = 0
    d3 = 0
    for d in divisors(n):
        if d % 4 == 1:
            d1 += 1
        elif d % 4 == 3:
            d3 += 1
    return 4 * (d1 - d3)


def enumerate_source() -> list[tuple[int, int, int, int, int, int, int]]:
    out: list[tuple[int, int, int, int, int, int, int]] = []
    for epsilon in EPSILON_STATES:
        for g in divisors(epsilon):
            c = epsilon // g
            for h in range(1, Y + 1):
                if gcd(h, c) != 1:
                    continue
                for r in range(1, Y // h + 1):
                    for delta in range(1, Y // (h * r) + 1):
                        m = h * r
                        n = g * h * delta
                        out.append((epsilon, g, h, r, delta, m, n))
    return out


def exact_formula_count(epsilon: int, g: int, m: int, n: int) -> int:
    if n % g:
        return 0
    c = epsilon // g
    d0 = gcd(m, n // g)
    count = 0
    for h in divisors(d0):
        if gcd(h, c) != 1:
            continue
        if m * n <= g * h * Y:
            count += 1
    return count


def build_summary() -> dict:
    th2 = TH2.read_text(encoding="utf-8")
    th3 = TH3.read_text(encoding="utf-8")
    th4 = TH4.read_text(encoding="utf-8")
    th5 = TH5.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH2=COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE",
        "TRANSFORMED_IDENTITIES=m=h*r,k=g*h",
    ]:
        require(th2, marker, "Stage14-tH2")

    for marker in [
        "STAGE14_TH3=COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER",
        "SHARED_AUXILIARY_MODULUS_PRESERVED=true",
    ]:
        require(th3, marker, "Stage14-tH3")

    for marker in [
        "STAGE14_TH4=COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX",
        "DIVISOR_LIFT_FIXED_POWER_LOSS=false",
        "FULL_COEFFICIENT_COLLISION_ENERGY_PROVED=false",
    ]:
        require(th4, marker, "Stage14-tH4")

    for marker in [
        "STAGE14_TH5=COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY",
        "EXACT_SHARED_H_FIBER_FORMULA_PROVED=true",
        "FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true",
        "PAIR_RETENTION_ESSENTIAL=true",
        "SAME_MODULUS_RESIDUE_COLLISION_ENERGY_PROVED=false",
        "NEXT=Stage14-tH6",
    ]:
        require(th5, marker, "Stage14-tH5")

    source = enumerate_source()
    fibers: Counter[tuple[int, int, int, int]] = Counter(
        (epsilon, g, m, n)
        for epsilon, g, h, r, delta, m, n in source
    )

    formula_failures = 0
    for (epsilon, g, m, n), observed in fibers.items():
        exact = exact_formula_count(epsilon, g, m, n)
        if exact != observed:
            formula_failures += 1
    if formula_failures:
        raise AssertionError(f"exact fiber formula failures: {formula_failures}")

    tau_max_y = max(tau(n) for n in range(1, Y + 1))
    max_fiber = max(fibers.values())
    if max_fiber > tau_max_y:
        raise AssertionError((max_fiber, tau_max_y))

    histogram = Counter(fibers.values())
    exact_norm_pair_collision_energy = sum(v * v for v in fibers.values())
    if exact_norm_pair_collision_energy > tau_max_y * len(source):
        raise AssertionError("norm-pair collision energy exceeds tau_max source mass")

    gaussian_source_lifts = 0
    distinct_gaussian_pairs = 0
    gaussian_collision_energy = 0
    for (epsilon, g, m, n), multiplicity in fibers.items():
        rep_pairs = r2(m) * r2(n)
        gaussian_source_lifts += multiplicity * rep_pairs
        distinct_gaussian_pairs += rep_pairs
        gaussian_collision_energy += multiplicity * multiplicity * rep_pairs

    if gaussian_collision_energy > tau_max_y * gaussian_source_lifts:
        raise AssertionError("Gaussian exact-pair collision energy exceeds tau_max bound")

    # Deterministic signed source weights collapsed to retained (epsilon,g,m,n).
    collapsed: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    fiber_source_energy: defaultdict[tuple[int, int, int, int], int] = defaultdict(int)
    weighted_source_energy = 0
    for epsilon, g, h, r, delta, m, n in source:
        weight = ((-1) ** (h + r + delta)) * (
            1 + ((h + 2 * r + 3 * delta + epsilon + g) % 5)
        )
        key = (epsilon, g, m, n)
        collapsed[key] += weight
        fiber_source_energy[key] += weight * weight
        weighted_source_energy += weight * weight

    weighted_collapsed_energy = sum(value * value for value in collapsed.values())
    weighted_violations = 0
    for key, value in collapsed.items():
        if value * value > fibers[key] * fiber_source_energy[key]:
            weighted_violations += 1
    if weighted_violations:
        raise AssertionError(f"weighted fiber Cauchy violations: {weighted_violations}")
    if weighted_collapsed_energy > tau_max_y * weighted_source_energy:
        raise AssertionError("weighted collapsed energy exceeds tau_max bound")

    return {
        "stage": "Stage14-tH5",
        "status": "COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY",
        "requires_future_t_result": False,
        "dependencies": ["Stage14-tH2", "Stage14-tH3", "Stage14-tH4"],
        "exact_fiber_formula": {
            "fixed_state": "epsilon,g",
            "c": "epsilon/g",
            "m": "h*r",
            "n": "g*h*delta",
            "shared_h_condition": "h divides gcd(m,n/g)",
            "coprimality": "gcd(h,epsilon/g)=1",
            "physical_budget": "m*n <= g*h*Y",
            "multiplicity_upper_bound": "tau(gcd(m,n/g)) <= tau_max(Y)",
        },
        "energy_theorem": {
            "exact_gaussian_pair_collision_multiplicity_divisor_bounded": True,
            "full_exact_gaussian_pair_coefficient_collision_energy_proved": True,
            "exact_pair_collapse_fixed_power_loss": False,
            "exact_pair_collision_energy": "source_mass*Y^o(1)",
            "unit_orbit_expansion_cost_at_most": 16,
            "pair_retention_essential": True,
            "one_coordinate_projection_collision_energy_proved": False,
            "same_modulus_residue_collision_energy_proved": False,
            "same_modulus_joint_second_moment_theorem_proved": False,
        },
        "audit": {
            "epsilon_states": list(EPSILON_STATES),
            "Y": Y,
            "source_transformed_tuples": len(source),
            "retained_state_norm_pair_fibers": len(fibers),
            "maximum_exact_fiber_multiplicity": max_fiber,
            "tau_max_Y": tau_max_y,
            "exact_fiber_formula_failures": formula_failures,
            "fiber_multiplicity_histogram": {
                str(k): histogram[k] for k in sorted(histogram)
            },
            "exact_norm_pair_collision_energy": exact_norm_pair_collision_energy,
            "gaussian_source_lifts": gaussian_source_lifts,
            "distinct_exact_gaussian_pair_labels": distinct_gaussian_pairs,
            "exact_gaussian_pair_collision_energy": gaussian_collision_energy,
            "gaussian_collision_source_ratio": gaussian_collision_energy / gaussian_source_lifts,
            "weighted_source_l2_energy": weighted_source_energy,
            "weighted_collapsed_pair_l2_energy": weighted_collapsed_energy,
            "weighted_energy_ratio": weighted_collapsed_energy / weighted_source_energy,
            "weighted_fiber_cauchy_violations": weighted_violations,
        },
        "proof_boundary": {
            "exact_shared_h_fiber_formula_proved": True,
            "exact_paired_norm_collision_multiplicity_le_tau_max": True,
            "full_exact_gaussian_pair_coefficient_collision_energy_proved": True,
            "same_modulus_residue_collision_energy_proved": False,
            "same_modulus_joint_second_moment_theorem_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH6",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH5 summary differs semantically")
    print("Stage14-tH5 exact Gaussian-pair collision-energy audit: OK")


if __name__ == "__main__":
    main()
