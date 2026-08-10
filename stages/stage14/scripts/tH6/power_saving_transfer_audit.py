#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH4 = ROOT / "stages/stage14/14-tH4/result.md"
TH5 = ROOT / "stages/stage14/14-tH5/result.md"
TH6 = ROOT / "stages/stage14/14-tH6/result.md"
FROZEN = ROOT / "stages/stage14/data/tH6/power_saving_transfer_summary.json"


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def frac_text(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def margin_class(x: Fraction) -> str:
    if x > 0:
        return "POSITIVE"
    if x == 0:
        return "CRITICAL"
    return "FAIL"


def squared_case(name: str, gamma: Fraction, omega: Fraction) -> dict:
    effective = gamma - omega
    delivered = effective / 2
    return {
        "name": name,
        "gamma": frac_text(gamma),
        "omega": frac_text(omega),
        "effective_squared_saving": frac_text(effective),
        "delivered_after_one_root": frac_text(delivered),
        "classification": margin_class(effective),
    }


def direct_case(name: str, delta: Fraction, omega: Fraction) -> dict:
    effective = delta - omega
    return {
        "name": name,
        "delta": frac_text(delta),
        "omega_count": frac_text(omega),
        "effective_count_saving": frac_text(effective),
        "classification": margin_class(effective),
    }


def build_summary() -> dict:
    th4 = TH4.read_text(encoding="utf-8")
    th5 = TH5.read_text(encoding="utf-8")
    th6 = TH6.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH4=COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX",
        "DIVISOR_LIFT_FIXED_POWER_LOSS=false",
        "GAUSSIAN_REPRESENTATION_LIFT_FIXED_POWER_LOSS=false",
        "INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false",
    ]:
        require(th4, marker, "Stage14-tH4")

    for marker in [
        "STAGE14_TH5=COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY",
        "FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true",
        "EXACT_PAIR_COLLAPSE_FIXED_POWER_LOSS=false",
        "PAIR_RETENTION_ESSENTIAL=true",
    ]:
        require(th5, marker, "Stage14-tH5")

    for marker in [
        "STAGE14_TH6=COMPLETE_ABSTRACT_POWER_SAVING_TRANSFER_RECEIVER",
        "STANDARD_TH1_TH5_FIXED_POWER_OVERHEAD=0",
        "SQUARED_SECOND_MOMENT_EFFECTIVE_SAVING=Gamma-Omega",
        "ONE_ROOT_DELIVERED_SAVING=(Gamma-Omega)/2",
        "DIRECT_COUNT_EFFECTIVE_SAVING=Delta-Omega_count",
        "POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21",
        "ONE_ROOT_SQUARED_SAVING_REQUIRED_FOR_SQRT_B=20/21+Omega",
        "NEXT=Stage14-tH7",
    ]:
        require(th6, marker, "Stage14-tH6")

    road_components = {
        "gaussian_normalization": Fraction(0),
        "finite_state_sum": Fraction(0),
        "divisor_hyperbola_lift": Fraction(0),
        "conductor_adapter": Fraction(0),
        "spectral_energy_under_declared_subpolynomial_budget": Fraction(0),
        "mellin_kernel_under_declared_subpolynomial_budget": Fraction(0),
        "dyadic_assembly": Fraction(0),
        "exact_pair_collision": Fraction(0),
    }
    road_total = sum(road_components.values(), Fraction(0))
    if road_total != 0:
        raise AssertionError(road_total)

    squared = [
        squared_case("positive_basic", Fraction(1, 3), Fraction(0)),
        squared_case("sqrt_threshold_exact", Fraction(20, 21), Fraction(0)),
        squared_case("overhead_threshold_exact", Fraction(1), Fraction(1, 21)),
        squared_case("positive_with_overhead", Fraction(1, 2), Fraction(1, 6)),
        squared_case("critical", Fraction(1, 4), Fraction(1, 4)),
        squared_case("fail", Fraction(1, 5), Fraction(1, 4)),
    ]

    direct = [
        direct_case("positive_basic", Fraction(1, 5), Fraction(0)),
        direct_case("sqrt_threshold_exact", Fraction(10, 21), Fraction(0)),
        direct_case("overhead_threshold_exact", Fraction(1, 2), Fraction(1, 42)),
        direct_case("critical", Fraction(1, 4), Fraction(1, 4)),
    ]

    expected_squared = {
        "positive_basic": ("1/3", "1/6", "POSITIVE"),
        "sqrt_threshold_exact": ("20/21", "10/21", "POSITIVE"),
        "overhead_threshold_exact": ("20/21", "10/21", "POSITIVE"),
        "positive_with_overhead": ("1/3", "1/6", "POSITIVE"),
        "critical": ("0", "0", "CRITICAL"),
        "fail": ("-1/20", "-1/40", "FAIL"),
    }
    for row in squared:
        exp = expected_squared[row["name"]]
        got = (
            row["effective_squared_saving"],
            row["delivered_after_one_root"],
            row["classification"],
        )
        if got != exp:
            raise AssertionError((row["name"], got, exp))

    expected_direct = {
        "positive_basic": ("1/5", "POSITIVE"),
        "sqrt_threshold_exact": ("10/21", "POSITIVE"),
        "overhead_threshold_exact": ("10/21", "POSITIVE"),
        "critical": ("0", "CRITICAL"),
    }
    for row in direct:
        exp = expected_direct[row["name"]]
        got = (row["effective_count_saving"], row["classification"])
        if got != exp:
            raise AssertionError((row["name"], got, exp))

    local = Fraction(41, 42)
    sqrt_exp = Fraction(1, 2)
    post_required = local - sqrt_exp
    squared_required_one_root = 2 * post_required
    if post_required != Fraction(10, 21):
        raise AssertionError(post_required)
    if squared_required_one_root != Fraction(20, 21):
        raise AssertionError(squared_required_one_root)

    # Verify the generic identity for a grid of exact rational budgets.
    grid_checks = 0
    for gamma_num in range(0, 9):
        gamma = Fraction(gamma_num, 8)
        for omega_num in range(0, 9):
            omega = Fraction(omega_num, 16)
            eff = gamma - omega
            delivered = eff / 2
            if 2 * delivered != eff:
                raise AssertionError((gamma, omega))
            if (eff > 0) != (gamma > omega):
                raise AssertionError((gamma, omega, eff))
            grid_checks += 1

    return {
        "stage": "Stage14-tH6",
        "status": "COMPLETE_ABSTRACT_POWER_SAVING_TRANSFER_RECEIVER",
        "requires_future_t_result": False,
        "dependencies": ["Stage14-tH4", "Stage14-tH5"],
        "standard_roadworks_fixed_power_exponents": {
            key: frac_text(value) for key, value in road_components.items()
        },
        "standard_total_overhead": frac_text(road_total),
        "transfer_formulas": {
            "squared_effective": "Gamma-Omega",
            "one_root_delivered": "(Gamma-Omega)/2",
            "direct_count_effective": "Delta-Omega_count",
            "positive_squared_survival_condition": "Gamma>Omega",
            "positive_direct_survival_condition": "Delta>Omega_count",
        },
        "stage14_thresholds": {
            "current_local_exponent": "41/42",
            "sqrt_B_exponent": "1/2",
            "post_local_direct_saving_required": frac_text(post_required),
            "one_root_squared_saving_required_at_zero_overhead": frac_text(
                squared_required_one_root
            ),
            "general_one_root_condition": "Gamma-Omega>=20/21",
        },
        "audit": {
            "squared_second_moment_cases": squared,
            "direct_count_cases": direct,
            "exact_fraction_grid_checks": grid_checks,
        },
        "proof_boundary": {
            "abstract_power_saving_transfer_receiver_proved": True,
            "standard_th1_th5_fixed_power_overhead_zero": True,
            "same_modulus_joint_second_moment_theorem_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH7",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if summary != frozen:
        raise AssertionError("frozen tH6 summary differs semantically")
    print("Stage14-tH6 power-saving transfer audit: OK")


if __name__ == "__main__":
    main()
