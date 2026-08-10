#!/usr/bin/env python3
"""Stage14-t50: external Frobenius mean-square / selector-sensitive two-modulus boundary."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T49 = ROOT / "stages/stage14/data/14-t49/frobenius_amplifier_frozen.json"
TH4 = ROOT / "stages/stage14/data/tH4/weighted_large_sieve_toolbox_summary.json"
TH5 = ROOT / "stages/stage14/data/tH5/gaussian_pair_collision_energy_summary.json"
TH8 = ROOT / "stages/stage14/data/tH8/external_auxiliary_spin_dispersion_summary.json"
TH11 = ROOT / "stages/stage14/data/tH11/cycle2_stress_park_summary.json"
OUT = ROOT / "stages/stage14/data/14-t50/selector_sensitive_two_modulus.json"


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def selector_countermodel() -> dict:
    # Complete character cancellation does not imply cancellation after a sparse selector.
    p = 13
    full = sum(legendre(x, p) for x in range(1, p))
    selected = [x for x in range(1, p) if legendre(x, p) == 1]
    selected_sum = sum(legendre(x, p) for x in selected)
    assert full == 0
    assert len(selected) == 6
    assert selected_sum == 6
    return {
        "prime": p,
        "complete_nonzero_sum": full,
        "selected_points": len(selected),
        "selected_sum": selected_sum,
        "logical_conclusion": "complete finite-field cancellation alone does not control an arbitrary sparse selector; physical Gaussian selector distribution needs its own mean-square theorem",
    }


def bad_prime_lemma_audit(t49: dict) -> dict:
    # The proof is asymptotic/algebraic.  The frozen sample provides a consistency check.
    H = t49["external"]["H"]
    P = t49["external"]["P"]
    assert H == 560 and P == 128
    assert t49["external"]["max_bad"] == 0
    assert t49["endogenous"]["max_bad"] == 2

    # If B_p is the number of states bad at auxiliary p and every state is bad at
    # at most C_rho=O_rho(1) primes p~B^rho, then
    # sum B_p <= C_rho H, sum B_p^2 <= H sum B_p, and
    # sum_{p!=q}(B_p+B_q)^2 <= 4(P-1) sum B_p^2.
    # Hence R_bad << C_rho H^2 P, which is <= H P^2 B^o once P>=H B^-o.
    return {
        "bad_datum": "M_s=ell_s*Delta_s*m_s*n_s*Ftilde_s (up to bounded fixed factors)",
        "polynomial_size": "|M_s|<=B^C0 for an absolute C0 on the physical family",
        "amplifier_scale": "p~L=B^rho, rho>0 fixed",
        "bad_primes_per_state": "omega_{p~L}(M_s)<=C0/rho+o(1)=O_rho(1)",
        "incidence_sum": "sum_p B_p=O_rho(H)",
        "incidence_l2": "sum_p B_p^2<=H*sum_p B_p=O_rho(H^2)",
        "bad_pair_error": "sum_{p!=q}|E_pq|^2<=4(P-1)*sum_p B_p^2=O_rho(H^2*P)",
        "absorbed_at_t49_scale": "if P>=H*B^-o(1), then R_bad<=H*P^2*B^o(1)",
        "frozen_external_max_bad": t49["external"]["max_bad"],
        "frozen_endogenous_max_bad": t49["endogenous"]["max_bad"],
        "aggregate_bound_proved": True,
    }


def main() -> None:
    t49 = json.loads(T49.read_text())
    th4 = json.loads(TH4.read_text())
    th5 = json.loads(TH5.read_text())
    th8 = json.loads(TH8.read_text())
    th11 = json.loads(TH11.read_text())

    assert t49["boundary"] == "COMPLETE_EXTERNAL_SPLIT_PRIME_FROBENIUS_AMPLIFIER_AND_NONCIRCULAR_MEAN_SQUARE_REDUCTION"
    assert th4["status"] == "COMPLETE_WEIGHTED_MELLIN_HECKE_LARGE_SIEVE_TRANSFER_TOOLBOX"
    assert th5["status"] == "COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY"
    assert th8["status"] == "COMPLETE_EXTERNAL_AUXILIARY_GAUSSIAN_SPIN_DISPERSION_ADAPTER"
    assert th11["status"] == "COMPLETE_SECOND_CYCLE_STRESS_GATE_AND_PARK"

    assert th4["same_modulus_policy"]["same_modulus_joint_second_moment_theorem_proved"] is False
    assert th5["energy_theorem"]["same_modulus_residue_collision_energy_proved"] is False
    assert th5["energy_theorem"]["same_modulus_joint_second_moment_theorem_proved"] is False
    assert th8["adapter"]["physical_packet_cauchy_dispersion_identity_proved"] is True
    assert "genuinely multi-modulus post-dispersion packet" in th11["reopen_triggers"]

    bad = bad_prime_lemma_audit(t49)
    selector = selector_countermodel()

    report = {
        "stage": "14-t50",
        "t49_target": {
            "target": "R_off=sum_{p!=q}|G_pq|^2 <= H*P^2*B^o(1)",
            "frozen_external_ratio": t49["external"]["offdiag_random_scale_ratio"],
            "frozen_external_R_off": t49["external"]["offdiagonal_frobenius"],
            "frozen_H": t49["external"]["H"],
            "frozen_P": t49["external"]["P"],
        },
        "bad_auxiliary": bad,
        "route_b_identification": {
            "tH8_route_b_available": True,
            "identity": "H_X(p,q)=sum_x chi_p(P_x)chi_q(P_x) is exactly the t49/t50 Gram kernel G_pq after canonical-square normalization",
            "two_auxiliary_moduli_simultaneously_present": True,
            "tH11_reopen_trigger_hit": "genuinely multi-modulus post-dispersion packet",
        },
        "t32_to_physical_selector_gap": {
            "t32_input": "for fixed good split p,q and fixed norm indices, complete angular torus correlation has square-root cancellation",
            "physical_input": "only the sparse integral Gaussian representations satisfying the divisor-coupled hyperbola, canonical selector, interval/reconstruction and branch masks are retained",
            "countermodel": selector,
            "complete_sum_bound_alone_sufficient": False,
            "missing_object": "selector-sensitive same-modulus/two-auxiliary Gaussian norm-index second moment",
        },
        "roadworks_contract": {
            "tH4_weight_masks_transfer_without_fixed_power_once_base_second_moment_exists": th4["transfer_contract"]["weighted_one_variable_large_sieve_transfer_proved"],
            "tH4_same_modulus_joint_second_moment_already_proved": th4["same_modulus_policy"]["same_modulus_joint_second_moment_theorem_proved"],
            "tH5_exact_gaussian_pair_collision_energy_near_linear": th5["energy_theorem"]["full_exact_gaussian_pair_coefficient_collision_energy_proved"],
            "tH5_same_modulus_residue_collision_energy_already_proved": th5["energy_theorem"]["same_modulus_residue_collision_energy_proved"],
            "no_new_divisor_or_weight_overhead_needed": True,
        },
        "missing_theorem_contract": {
            "name": "SelectorSensitiveTwoAuxiliaryGaussianSecondMoment",
            "block_sum": "S_R(p,q)=sum_{xi in X_R} w_R(xi)*chi_{pq}(Ftilde(xi))",
            "required_global_bound": "sum_{p!=q in P}|sum_R S_R(p,q)|^2 <= P^2*(sum_R ||w_R||_2^2)*B^o(1)",
            "physical_unweighted_specialization": "R_good<=H*P^2*B^o(1)",
            "must_preserve": [
                "signed aggregation across common-refinement blocks",
                "shared U/V modulus group",
                "divisor-coupled hyperbola cutoff",
                "canonical-prime selector and physical reconstruction masks",
                "two distinct split auxiliary primes p,q",
            ],
            "forbidden_shortcut": "do not collapse state pairs to cross-kernel coefficients before physical/norm-index cancellation, since that imports E4",
            "proved": False,
        },
        "tH_decision": {
            "additional_tH_needed": True,
            "stage": "Stage14-tH14",
            "reason": "t50 hits tH11's explicit multi-modulus post-dispersion reopen trigger and the exact same-modulus joint second-moment gap left by tH4/tH5",
        },
        "decision": {
            "STAGE14_T50": "COMPLETE_BAD_AUXILIARY_BOUND_AND_SELECTOR_SENSITIVE_TWO_MODULUS_BOUNDARY",
            "EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED": True,
            "TH8_PHYSICAL_ROUTE_B_EQUALS_T49_FROBENIUS_KERNEL": True,
            "TH11_MULTI_MODULUS_REOPEN_TRIGGER_HIT": True,
            "T32_COMPLETE_ANGULAR_BOUND_DIRECTLY_CONTROLS_SPARSE_PHYSICAL_SELECTOR": False,
            "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED": True,
            "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED": False,
            "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_NEEDED": True,
            "NEXT": "Stage14-t51 attack SelectorSensitiveTwoAuxiliaryGaussianSecondMoment on the critical family; consume Stage14-tH14 if available, while keeping t32 completion before pair collapse",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
