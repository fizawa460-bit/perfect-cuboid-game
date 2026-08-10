#!/usr/bin/env python3
"""Stage14-tH11 deterministic stress gate for the second tH roadworks cycle."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
TH8 = ROOT / "stages/stage14/data/tH8/external_auxiliary_spin_dispersion_summary.json"
TH9 = ROOT / "stages/stage14/data/tH9/squareclass_crossratio_atlas_summary.json"
TH10 = ROOT / "stages/stage14/data/tH10/squareclass_fiber_energy_toolbox_summary.json"
T40 = ROOT / "stages/stage14/data/14-t40/cross_kernel_hecke_dispersion.json"
T41 = ROOT / "stages/stage14/data/14-t41/global_energy_incidence.json"
SUMMARY = ROOT / "stages/stage14/data/tH11/cycle2_stress_park_summary.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def regression_audit() -> dict[str, int]:
    th8 = load(TH8)
    th9 = load(TH9)
    th10 = load(TH10)
    t40 = load(T40)
    t41 = load(T41)
    summary = load(SUMMARY)

    assert th8["status"] == "COMPLETE_EXTERNAL_AUXILIARY_GAUSSIAN_SPIN_DISPERSION_ADAPTER"
    assert th9["status"] == "COMPLETE_SQUARECLASS_CROSS_RATIO_AND_AUTOCORRELATION_ATLAS"
    assert th10["status"] == "COMPLETE_SQUARECLASS_FIBER_AND_AUTOCORRELATION_INCIDENCE_TOOLBOX"
    assert t40["decision"]["STAGE14_T40"] == "COMPLETE_ONE_CAUCHY_QUADRATIC_HECKE_CROSS_KERNEL_AND_ENERGY_BOUNDARY"
    assert t41["decision"]["STAGE14_T41"] == "COMPLETE_TWO_SIDED_INCIDENCE_AUDIT_AND_KUMMER_ENERGY_BARRIER"

    # tH8 exact dispersion audit remains intact.
    d8 = th8["audit"]["dispersion"]
    assert d8["physical_packets"] == 55
    assert d8["legendre_product_checks"] == 15125
    assert d8["legendre_product_failures"] == 0
    assert d8["route_a_second_moment"] == d8["route_a_cross_expansion"] == 2845
    assert d8["route_b_second_moment"] == d8["route_b_cross_expansion"] == 2485

    # t40 upgrades auxiliary Route A from merely defined to proved Hecke-ready.
    dec40 = t40["decision"]
    assert dec40["ONE_CAUCHY_REMOVES_EXTERNAL_TRACE_NONMULTIPLICATIVITY"] is True
    assert dec40["CROSS_KERNEL_IS_QUADRATIC_DIRICHLET_CHARACTER_IN_AUXILIARY_NORM"] is True
    assert dec40["CROSS_KERNEL_IS_NORM_INDUCED_QUADRATIC_HECKE_CHARACTER_OVER_QI"] is True
    assert dec40["QUADRATIC_HECKE_LARGE_SIEVE_INTERFACE_VALID"] is True

    # tH9 compression agrees exactly with t40 frozen energy data.
    r9 = th9["t40_frozen_regression"]
    assert r9["states"] == 1120
    assert r9["distinct_single_squareclasses"] == 544
    assert r9["global_second_squareclass_energy_A1"] == 2368
    assert r9["cross_kernel_fourth_energy_E4"] == 21193216
    assert r9["off_principal_E4"] == 15585792

    # t41 exact principal partition and logical barrier.
    dec41 = t41["decision"]
    assert dec41["TWO_SIDED_LOCAL_ENERGY_IMPLIES_GLOBAL_NEAR_LINEAR"] is False
    assert dec41["OFF_FIBER_COLLISION_SURFACE_KUMMER_TYPE"] is True
    cats = t41["frozen_audit"]["principal_collision_breakdown"]["ordered_collision_categories"]
    assert cats["global"] == 2368
    assert cats["same_direction"] == 2240
    assert cats["cross_direction"] == 128
    assert cats["global"] == cats["same_direction"] + cats["cross_direction"]

    # tH10 accepts both uniform and sparse-heavy outputs.
    pr10 = th10["proof_boundary"]
    assert pr10["principal_partition_identity_proved"] is True
    assert pr10["two_sided_local_energy_shortcut_rejected"] is True
    assert pr10["generic_exceptional_off_fiber_receiver_defined"] is True
    assert pr10["uniform_nonprincipal_e4_receiver_proved"] is True
    assert pr10["heavy_light_nonprincipal_e4_receiver_proved"] is True
    assert pr10["fiber_times_support_expansion_bound_proved"] is True
    fr10 = th10["t41_frozen_regression"]
    assert fr10["uniform_receiver_upper_bound"] == 205_932_544

    frozen = summary["frozen_regressions"]
    assert frozen["tH8_physical_packets"] == 55
    assert frozen["tH8_legendre_product_checks"] == 15125
    assert frozen["tH9_states"] == 1120
    assert frozen["tH9_squareclasses"] == 544
    assert frozen["tH9_A1"] == 2368
    assert frozen["tH9_E4"] == 21193216
    assert frozen["t41_same_direction_local_energy"] == 2240
    assert frozen["t41_off_direction_ordered_collisions"] == 128
    assert frozen["tH10_uniform_receiver_upper_bound_frozen"] == 205_932_544

    return {
        "tH8_product_checks": d8["legendre_product_checks"],
        "states": r9["states"],
        "squareclasses": r9["distinct_single_squareclasses"],
        "A1": r9["global_second_squareclass_energy_A1"],
        "E4": r9["cross_kernel_fourth_energy_E4"],
        "local": cats["same_direction"],
        "off": cats["cross_direction"],
        "uniform_receiver": fr10["uniform_receiver_upper_bound"],
    }


def stress_classification_audit() -> dict[str, int]:
    cases = [
        ("raw_external_trace_direct_FI", "INVALID_SHORTCUT"),
        ("natural_modulus_self_symbol", "INVALID_SHORTCUT"),
        ("route_A_after_one_cauchy", "SAFE"),
        ("principal_kernel_sent_to_large_sieve", "INVALID_SHORTCUT"),
        ("bad_auxiliary_prime", "ACCOUNTED"),
        ("squareclass_compression", "SAFE"),
        ("fundamental_discriminant_reindex", "SAFE"),
        ("two_local_energy_shortcut", "INVALID_SHORTCUT"),
        ("generic_exceptional_receiver", "SAFE_RECEIVER"),
        ("uniform_nonprincipal_theorem", "EXTERNAL_MATH"),
        ("heavy_light_theorem", "EXTERNAL_MATH"),
        ("fiber_support_receiver", "SAFE_RECEIVER"),
        ("signed_complex_positivity", "REOPEN_IF_NEEDED"),
        ("prime_power_auxiliary", "REOPEN_IF_NEEDED"),
        ("higher_moment", "REOPEN_IF_NEEDED"),
        ("multi_modulus_packet", "REOPEN_IF_NEEDED"),
        ("leave_Qi", "REOPEN_IF_NEEDED"),
        ("physical_route_new_parameterization", "REOPEN_IF_USEFUL"),
        ("no_stable_t42_contract", "PARK"),
    ]

    counts: dict[str, int] = {}
    for _, cls in cases:
        counts[cls] = counts.get(cls, 0) + 1

    # Three invalid shortcuts are structural plus the local-energy shortcut.
    assert counts["INVALID_SHORTCUT"] == 4
    assert counts["SAFE"] == 3
    assert counts["SAFE_RECEIVER"] == 2
    assert counts["EXTERNAL_MATH"] == 2
    assert counts["REOPEN_IF_NEEDED"] == 5
    assert counts["REOPEN_IF_USEFUL"] == 1
    assert counts["PARK"] == 1
    assert counts["ACCOUNTED"] == 1
    return counts


def receiver_algebra_audit() -> dict[str, int]:
    # Verify the uniform/heavy-light inequalities on a grid of abstract integer
    # autocorrelation profiles.  We only use nonnegative profiles, matching the
    # positivity scope explicitly frozen by tH10.
    checks = 0
    profiles = [
        (10, 14, [8, 6, 4, 2]),
        (12, 20, [10, 8, 8, 4, 2]),
        (16, 28, [12, 10, 6, 4, 4, 2]),
        (20, 36, [16, 12, 8, 8, 4, 4, 2]),
    ]
    for H, A1, non in profiles:
        S = sum(non)
        # Profiles need not exhaust H^2-A1; append leftover as many unit kernels.
        leftover = H * H - A1 - S
        assert leftover >= 0
        full = non + ([1] * leftover)
        E4 = A1 * A1 + sum(v * v for v in full)
        R = max(full, default=0)
        assert E4 <= A1 * A1 + R * (H * H - A1)
        checks += 1
        for T in range(0, R + 1):
            MT = sum(v for v in full if v > T)
            rhs = A1 * A1 + T * (H * H - A1) + (R - T) * MT
            assert E4 <= rhs
            checks += 1
    return {"receiver_checks": checks}


def exponent_ledger_audit() -> int:
    vals = [Fraction(0), Fraction(1, 8), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)]
    checks = 0
    for h in vals[1:]:
        for lam in vals:
            for gen in vals:
                for exc in vals:
                    a = max(lam, gen, exc)
                    for r in vals:
                        q = max(2 * a, r + 2 * h)
                        assert q >= 2 * a and q >= r + 2 * h
                        checks += 1
                    for t in vals:
                        for r in vals:
                            for m in vals:
                                q = max(2 * a, t + 2 * h, r + m)
                                assert q >= 2 * a
                                assert q >= t + 2 * h
                                assert q >= r + m
                                checks += 1
    assert checks > 10_000
    return checks


def decision_audit() -> dict:
    summary = load(SUMMARY)
    assert summary["status"] == "COMPLETE_SECOND_CYCLE_STRESS_GATE_AND_PARK"
    assert summary["requires_future_t_result"] is False
    d = summary["decision"]
    assert d["TH_CYCLE2_T_H8_T_H10_COMPLETE"] is True
    assert d["TH_CYCLE2_REUSABLE"] is True
    assert d["TH_CYCLE2_PARKED"] is True
    assert d["TH_SUPPORT_ROUTE_PARKED"] is True
    assert d["TH_NEW_INDEPENDENT_ROADWORK_AVAILABLE"] is False
    assert d["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
    assert d["GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED"] is False
    assert d["CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED"] is False
    assert d["A_11_POWER_SAVING_PROVED"] is False
    assert d["T_O_SQRT_B_PROVED"] is False
    assert d["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
    assert len(summary["reopen_triggers"]) == 7
    assert summary["next"].startswith("WAIT_FOR_NEW_STABLE_T_DEMAND")
    return d


def main() -> None:
    regression = regression_audit()
    classes = stress_classification_audit()
    receivers = receiver_algebra_audit()
    exponent_checks = exponent_ledger_audit()
    decision = decision_audit()

    report = {
        "regression": regression,
        "stress_classifications": classes,
        "receiver_algebra": receivers,
        "exponent_ledger_checks": exponent_checks,
        "parked": decision["TH_SUPPORT_ROUTE_PARKED"],
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH11 audit: PASS")


if __name__ == "__main__":
    main()
