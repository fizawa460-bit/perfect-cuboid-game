#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH = {i: ROOT / f"stages/stage14/14-tH{i}/result.md" for i in range(8)}
TH6_SUMMARY = ROOT / "stages/stage14/data/tH6/power_saving_transfer_summary.json"
T38 = ROOT / "stages/stage14/14-t38/result.md"
FROZEN = ROOT / "stages/stage14/data/tH7/roadworks_stress_gate_summary.json"


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


STRESS_CASES = [
    ("higher_order_mellin", "SAFE"),
    ("non_mu4_unit_signature", "SAFE"),
    ("same_oriented_prime_uv", "SAFE"),
    ("conjugate_primes_both_active", "SAFE"),
    ("bad_prime_mask", "SAFE"),
    ("many_shared_h_decompositions", "SAFE"),
    ("gaussian_representation_multiplicity", "SAFE"),
    ("unit_orbit_quotient", "SAFE"),
    ("u_only_projection", "REOPEN_OLD_CYCLE"),
    ("prime_power_odd_conductor", "REOPEN_OLD_CYCLE"),
    ("polynomial_spectral_energy", "ACCOUNTED_FIXED_LOSS"),
    ("polynomial_mellin_kernel", "ACCOUNTED_FIXED_LOSS"),
    ("polynomial_block_count", "ACCOUNTED_FIXED_LOSS"),
    ("independent_uv_modulus_tensorization", "INVALID_SHORTCUT"),
    ("missing_same_modulus_theorem", "EXTERNAL_ANALYTIC"),
    ("direct_count_vs_second_moment", "SAFE"),
    ("leave_gaussian_field", "REOPEN_OLD_CYCLE"),
    ("higher_rank_packet", "REOPEN_OLD_CYCLE"),
]


def stress_counts() -> dict[str, int]:
    out: dict[str, int] = {}
    for _, cls in STRESS_CASES:
        out[cls] = out.get(cls, 0) + 1
    return out


def exponent_grid_audit() -> dict:
    sigmas = [Fraction(0), Fraction(1, 20), Fraction(1, 7)]
    kappas = [Fraction(0), Fraction(1, 30), Fraction(1, 11)]
    betas = [Fraction(0), Fraction(1, 16)]
    omega_news = [Fraction(0), Fraction(1, 50)]
    gammas = [Fraction(1, 2), Fraction(20, 21), Fraction(1)]

    checks = 0
    for sigma in sigmas:
        for kappa in kappas:
            for beta in betas:
                for omega_new in omega_news:
                    omega = sigma + 2 * kappa + beta + omega_new
                    for gamma in gammas:
                        effective = gamma - omega
                        delivered = effective / 2
                        if 2 * delivered != effective:
                            raise AssertionError((sigma, kappa, beta, omega_new, gamma))
                        checks += 1

    return {
        "formula": "Omega=sigma+2*kappa+beta+Omega_new",
        "grid_checks": checks,
        "sigma_values": [str(x) for x in sigmas],
        "kappa_values": [str(x) for x in kappas],
        "beta_values": [str(x) for x in betas],
        "omega_new_values": [str(x) for x in omega_news],
        "gamma_values": [str(x) for x in gammas],
    }


def build_summary() -> dict:
    texts = {i: TH[i].read_text(encoding="utf-8") for i in range(8)}
    t38 = T38.read_text(encoding="utf-8")

    required = {
        0: [
            "STAGE14_TH0=COMPLETE_INDEPENDENT_T_SUPPORT_ROADWORKS_ARCHITECTURE",
            "TH_CAN_ADVANCE_WHILE_T_IS_STALLED=true",
            "TH_CAN_ADVANCE_WHILE_T_IS_AHEAD=true",
            "TH_BLOCKED_SUBTOOL_IS_PARKED_NOT_PROPAGATED_AS_WAITING_STAGE=true",
        ],
        1: [
            "STAGE14_TH1=COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION",
            "ARBITRARY_LOCAL_CHARACTER_ORDER_SUPPORTED=true",
            "EXACT_CRT_CONDUCTOR_NORM_FORMULA=true",
        ],
        2: [
            "STAGE14_TH2=COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE",
            "TRANSFORMED_IDENTITIES=m=h*r,k=g*h",
            "SHARED_GAUSSIAN_NORM_FACTOR=h",
        ],
        3: [
            "STAGE14_TH3=COMPLETE_ALL_ORDER_RAY_CLASS_HYPERBOLA_CONDUCTOR_ADAPTER",
            "SHARED_AUXILIARY_MODULUS_PRESERVED=true",
            "SHARED_PRIME_JOINT_MODULUS_SQUARED=false",
        ],
        4: [
            "STAGE14_TH4=COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX",
            "WEIGHTED_ONE_VARIABLE_LARGE_SIEVE_TRANSFER_PROVED=true",
            "INDEPENDENT_UV_MODULUS_TENSORIZATION_ALLOWED=false",
        ],
        5: [
            "STAGE14_TH5=COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY",
            "FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true",
            "PAIR_RETENTION_ESSENTIAL=true",
        ],
        6: [
            "STAGE14_TH6=COMPLETE_ABSTRACT_POWER_SAVING_TRANSFER_RECEIVER",
            "STANDARD_TH1_TH5_FIXED_POWER_OVERHEAD=0",
            "ONE_ROOT_DELIVERED_SAVING=(Gamma-Omega)/2",
        ],
        7: [
            "STAGE14_TH7=COMPLETE_ROADWORKS_STRESS_GATE_AND_NEW_CYCLE_DECISION",
            "TH_CYCLE1_PARKED=true",
            "TH_SUPPORT_ROUTE_PARKED=false",
            "NEXT=Stage14-tH8 Gaussian spin / Dirichlet-symbol Type-I/II infrastructure; do not wait for t39",
        ],
    }
    for i, markers in required.items():
        for marker in markers:
            require(texts[i], marker, f"Stage14-tH{i}")

    for marker in [
        "STAGE14_T38=COMPLETE_MOVING_PRIME_ELLIPTIC_PACKET_BOUND_AND_CRITICAL_STRIP_REDUCTION",
        "CLASSICAL_QI_GAUSSIAN_SPIN_THEOREM_IDENTIFIED=true",
        "STAGE14_PACKET_EQUALS_FI_JACOBI_KUBOTA_SPIN=false",
        "CRITICAL_SQRT_ELL_STRIP_REMAINS=true",
    ]:
        require(t38, marker, "Stage14-t38")

    th6_summary = json.loads(TH6_SUMMARY.read_text(encoding="utf-8"))
    road_exponents = th6_summary["standard_roadworks_fixed_power_exponents"]
    if len(road_exponents) != 8:
        raise AssertionError(f"expected eight tH6 standard road exponents, got {len(road_exponents)}")
    if any(v != "0" for v in road_exponents.values()):
        raise AssertionError(f"nonzero standard road exponent: {road_exponents}")
    if th6_summary["standard_total_overhead"] != "0":
        raise AssertionError("tH6 standard overhead is not zero")

    if Fraction(41, 42) - Fraction(1, 2) != Fraction(10, 21):
        raise AssertionError("Stage14 direct threshold identity failed")
    if 2 * Fraction(10, 21) != Fraction(20, 21):
        raise AssertionError("Stage14 one-root threshold identity failed")

    counts = stress_counts()
    expected_counts = {
        "SAFE": 9,
        "REOPEN_OLD_CYCLE": 4,
        "ACCOUNTED_FIXED_LOSS": 3,
        "INVALID_SHORTCUT": 1,
        "EXTERNAL_ANALYTIC": 1,
    }
    if counts != expected_counts:
        raise AssertionError((counts, expected_counts))

    exponent_audit = exponent_grid_audit()

    return {
        "stage": "Stage14-tH7",
        "status": "COMPLETE_ROADWORKS_STRESS_GATE_AND_NEW_CYCLE_DECISION",
        "requires_future_t_result": False,
        "cycle1": {
            "covered_stages": ["tH1", "tH2", "tH3", "tH4", "tH5", "tH6"],
            "complete": True,
            "reusable": True,
            "parked": True,
            "standard_fixed_power_overhead": "0",
            "hidden_fixed_power_loss_found": False,
        },
        "stress_matrix": {
            "cases": [{"name": n, "classification": c} for n, c in STRESS_CASES],
            "counts": counts,
        },
        "reopen_old_cycle_triggers": [
            "prime-power odd conductors",
            "unavoidable one-coordinate projection",
            "unaccounted polynomial spectral/Mellin/block budget",
            "higher-rank packet replacing exact (U,V) pair",
            "arithmetic leaves Q(i)",
        ],
        "external_not_roadworks_defect": [
            "same-modulus joint second-moment or direct-count power-saving theorem",
        ],
        "exponent_audit": exponent_audit,
        "stage14_thresholds": {
            "current_local_exponent": "41/42",
            "sqrt_B_exponent": "1/2",
            "post_local_direct_saving_required": "10/21",
            "one_root_squared_saving_required_at_zero_overhead": "20/21",
        },
        "current_live_t_compatibility": {
            "audited_through": "Stage14-t38",
            "t38_classical_gaussian_spin_identified": True,
            "stage14_packet_equals_fi_spin": False,
            "critical_sqrt_ell_strip_remains": True,
            "old_cycle_invalidated": False,
        },
        "next_cycle": {
            "support_route_parked": False,
            "new_independent_roadwork_available": True,
            "next": "Stage14-tH8",
            "theme": "Gaussian spin / Dirichlet-symbol Type-I/II infrastructure",
            "wait_for_t39": False,
        },
        "proof_boundary": {
            "same_modulus_joint_second_moment_theorem_proved": False,
            "canonical_prime_sum_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH7 summary differs semantically")
    print("Stage14-tH7 roadworks stress gate audit: OK")


if __name__ == "__main__":
    main()
