#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH3 = ROOT / "stages/stage14/14-tH3/result.md"
TH4 = ROOT / "stages/stage14/14-tH4/result.md"
FROZEN = ROOT / "stages/stage14/data/tH4/weighted_large_sieve_toolbox_summary.json"

Y = 512
C_STATES = (1, 2, 3, 4, 6, 8, 12)
SPLIT_PRIMES = (5, 13, 17, 29, 37, 41, 53, 61)


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


def divisor_lift_audit() -> dict:
    source_pairs = 0
    source_energy_total = 0
    collapsed_energy_total = 0
    max_fiber_multiplicity = 0
    fiber_cauchy_violations = 0
    max_ratio = Fraction(0, 1)
    per_state: dict[str, dict] = {}

    for c in C_STATES:
        coeff: dict[int, int] = {}
        fiber_count: dict[int, int] = {}
        fiber_energy: dict[int, int] = {}
        source_energy = 0
        state_pairs = 0

        for h in range(1, Y + 1):
            if gcd(h, c) != 1:
                continue
            for r in range(1, Y // h + 1):
                n = h * r
                w = ((-1) ** (h + r)) * (1 + ((h + 2 * r) % 3))
                source_energy += w * w
                state_pairs += 1
                coeff[n] = coeff.get(n, 0) + w
                fiber_count[n] = fiber_count.get(n, 0) + 1
                fiber_energy[n] = fiber_energy.get(n, 0) + w * w

        collapsed_energy = sum(v * v for v in coeff.values())
        local_max = max(fiber_count.values())
        for n, value in coeff.items():
            if value * value > fiber_count[n] * fiber_energy[n]:
                fiber_cauchy_violations += 1

        if collapsed_energy > local_max * source_energy:
            raise AssertionError((c, collapsed_energy, local_max, source_energy))

        ratio = Fraction(collapsed_energy, source_energy)
        max_ratio = max(max_ratio, ratio)
        source_pairs += state_pairs
        source_energy_total += source_energy
        collapsed_energy_total += collapsed_energy
        max_fiber_multiplicity = max(max_fiber_multiplicity, local_max)
        per_state[str(c)] = {
            "source_pairs": state_pairs,
            "source_l2_energy": source_energy,
            "collapsed_norm_l2_energy": collapsed_energy,
            "max_fiber_multiplicity": local_max,
        }

    return {
        "Y": Y,
        "c_states": list(C_STATES),
        "source_pairs": source_pairs,
        "source_l2_energy": source_energy_total,
        "collapsed_norm_l2_energy": collapsed_energy_total,
        "max_divisor_fiber_multiplicity": max_fiber_multiplicity,
        "fiber_cauchy_violations": fiber_cauchy_violations,
        "max_observed_lift_source_energy_ratio": float(max_ratio),
        "per_state": per_state,
    }


def bounded_weight_audit() -> dict:
    coeff = [((7 * n + 3) % 17) - 8 for n in range(1, Y + 1)]
    unweighted = sum(a * a for a in coeff)

    # Weight = 1_{(n,30)=1} * ((n mod 7)+1)/8 * (-1)^n.
    # Record the weighted energy numerator over the common denominator 64.
    numerator = 0
    for n, a in enumerate(coeff, start=1):
        if gcd(n, 30) != 1:
            continue
        smooth_num = (n % 7) + 1
        phase = -1 if n % 2 else 1
        weighted_num = a * smooth_num * phase
        numerator += weighted_num * weighted_num

    violations = 0 if numerator <= 64 * unweighted else 1
    if violations:
        raise AssertionError((unweighted, numerator))

    return {
        "length": Y,
        "unweighted_l2_energy": unweighted,
        "weighted_energy_numerator": numerator,
        "weighted_energy_denominator": 64,
        "l2_monotonicity_violations": violations,
    }


def spectral_cauchy_audit() -> dict:
    one_coordinate_modes = 0
    same_modulus_pairs = 0
    max_h = 0
    violations = 0
    one_c_energy = 0
    one_m_energy = 0
    one_output_square = 0

    for p in SPLIT_PRIMES:
        h_p = (p - 1) // 4
        max_h = max(max_h, h_p)

        c = [((-1) ** k) * (k + 1) for k in range(h_p)]
        m = [((3 * k + 2) % 11) - 5 for k in range(h_p)]
        ec = sum(x * x for x in c)
        em = sum(x * x for x in m)
        s = sum(x * y for x, y in zip(c, m))
        if s * s > ec * em:
            violations += 1
        one_coordinate_modes += h_p
        one_c_energy += ec
        one_m_energy += em
        one_output_square += s * s

        cc: list[int] = []
        mm: list[int] = []
        for a in range(h_p):
            for b in range(h_p):
                cc.append(((-1) ** (a + b)) * (1 + ((a + 2 * b) % 5)))
                mm.append(((2 * a + 3 * b + 1) % 13) - 6)
        ec2 = sum(x * x for x in cc)
        em2 = sum(x * x for x in mm)
        s2 = sum(x * y for x, y in zip(cc, mm))
        if s2 * s2 > ec2 * em2:
            violations += 1
        same_modulus_pairs += h_p * h_p

    if violations:
        raise AssertionError(f"spectral Cauchy violations: {violations}")

    return {
        "split_primes": list(SPLIT_PRIMES),
        "one_coordinate_modes_checked": one_coordinate_modes,
        "same_modulus_ordered_mode_pairs_checked": same_modulus_pairs,
        "maximum_local_H_p": max_h,
        "spectral_cauchy_violations": violations,
        "one_coordinate_c_energy_total": one_c_energy,
        "one_coordinate_m_energy_total": one_m_energy,
        "one_coordinate_output_square_total": one_output_square,
    }


def assembly_audit() -> dict:
    powers: list[int] = []
    value = 1
    while value <= Y:
        powers.append(value)
        value *= 2

    raw_blocks = 0
    for h in powers:
        for r in powers:
            for d in powers:
                if h * r * d <= Y:
                    raw_blocks += 1

    conductor_qmax = 4096
    conductor_bands = 0
    q = 1
    while q <= conductor_qmax:
        conductor_bands += 1
        q *= 2

    return {
        "Y": Y,
        "dyadic_scales": len(powers),
        "raw_HRD_blocks_with_product_le_Y": raw_blocks,
        "sample_conductor_Qmax": conductor_qmax,
        "sample_dyadic_conductor_bands": conductor_bands,
    }


def build_summary() -> dict:
    th3 = TH3.read_text(encoding="utf-8")
    th4 = TH4.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH3=COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER",
        "SHARED_AUXILIARY_MODULUS_PRESERVED=true",
        "HYPERBOLA_GOOD_MODULUS_CONDITION=gcd(Q_rat,g*h*r*delta)=1",
    ]:
        require(th3, marker, "Stage14-tH3")

    for marker in [
        "STAGE14_TH4=COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX",
        "WEIGHTED_ONE_VARIABLE_LARGE_SIEVE_TRANSFER_PROVED=true",
        "DIVISOR_LIFT_FIXED_POWER_LOSS=false",
        "INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false",
        "SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false",
        "NEXT=Stage14-tH5",
    ]:
        require(th4, marker, "Stage14-tH4")

    divisor = divisor_lift_audit()
    bounded = bounded_weight_audit()
    spectral = spectral_cauchy_audit()
    assembly = assembly_audit()

    return {
        "stage": "Stage14-tH4",
        "status": "COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX",
        "requires_future_t_result": False,
        "dependencies": ["Stage14-tH3"],
        "transfer_contract": {
            "coefficient_masks_l2_safe": True,
            "bounded_smooth_weights_l2_safe": True,
            "unit_modulus_phases_l2_safe": True,
            "spectral_packet_cost": "exact L2 energy",
            "divisor_lift_l2_cost": "tau_max(Y)",
            "divisor_lift_fixed_power_loss": False,
            "gaussian_representation_fixed_power_loss": False,
            "conductor_band_count": "polylogarithmic",
            "hyperbola_block_count": "polylogarithmic",
            "mellin_kernel_cost": "K_W^2",
            "weighted_one_variable_large_sieve_transfer_proved": True,
            "base_large_sieve_reproved": False,
        },
        "same_modulus_policy": {
            "shared_modulus_packet_cauchy_preserves_group": True,
            "independent_uv_modulus_tensorization_allowed": False,
            "same_modulus_joint_second_moment_theorem_proved": False,
        },
        "audit": {
            "divisor_lift": divisor,
            "bounded_weight_layer": bounded,
            "spectral_cauchy": spectral,
            "assembly": assembly,
        },
        "proof_boundary": {
            "weighted_transfer_toolbox_proved": True,
            "full_coefficient_collision_energy_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH5",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH4 summary differs semantically")
    print("Stage14-tH4 weighted large-sieve transfer toolbox audit: OK")


if __name__ == "__main__":
    main()
