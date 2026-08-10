#!/usr/bin/env python3
"""Stage14-tH9: squareclass cross-ratio/autocorrelation atlas audit."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T40_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t40_cross_kernel_hecke_dispersion_audit.py"
T40_DATA = ROOT / "stages/stage14/data/14-t40/cross_kernel_hecke_dispersion.json"
SUMMARY = ROOT / "stages/stage14/data/tH9/squareclass_crossratio_atlas_summary.json"
RESULT = ROOT / "stages/stage14/14-tH9/result.md"


def class_autocorrelation(weights, cross_kernel):
    out = Counter()
    items = sorted((int(s), int(w)) for s, w in weights.items() if w != 0)
    for s, ws in items:
        for t, wt in items:
            out[cross_kernel(s, t)] += ws * wt
    return out


def structural_group_audit(classes, cross_kernel):
    classes = sorted(classes)
    sample = classes[:40]

    identity_checks = 0
    self_inverse_checks = 0
    commutativity_checks = 0
    associativity_checks = 0
    triangle_checks = 0

    for s in classes:
        assert cross_kernel(s, 1) == s
        assert cross_kernel(s, s) == 1
        identity_checks += 1
        self_inverse_checks += 1

    for i, s in enumerate(sample):
        for t in sample:
            assert cross_kernel(s, t) == cross_kernel(t, s)
            commutativity_checks += 1
        for j, t in enumerate(sample):
            for u in sample:
                lhs = cross_kernel(cross_kernel(s, t), u)
                rhs = cross_kernel(s, cross_kernel(t, u))
                assert lhs == rhs
                associativity_checks += 1

                # kappa_st xor kappa_tu = kappa_su
                assert cross_kernel(cross_kernel(s, t), cross_kernel(t, u)) == cross_kernel(s, u)
                triangle_checks += 1

    # Every pair kernel is recoverable from one basepoint label.
    base = classes[0]
    labels = {s: cross_kernel(s, base) for s in classes}
    basepoint_checks = 0
    for s in classes:
        for t in classes:
            assert cross_kernel(labels[s], labels[t]) == cross_kernel(s, t)
            basepoint_checks += 1

    return {
        "identity_checks": identity_checks,
        "self_inverse_checks": self_inverse_checks,
        "commutativity_checks": commutativity_checks,
        "associativity_checks": associativity_checks,
        "triangle_checks": triangle_checks,
        "basepoint_recovery_checks": basepoint_checks,
    }


def cross_ratio_audit(states, cross_kernel):
    n = len(states)
    checks = 0
    four_cycle_checks = 0
    for q in range(50_000):
        i = (17 * q + 3) % n
        j = (31 * q + 7) % n
        k = (43 * q + 11) % n
        l = (59 * q + 13) % n
        si = int(states[i]["kernel"])
        sj = int(states[j]["kernel"])
        sk = int(states[k]["kernel"])
        sl = int(states[l]["kernel"])

        kij = cross_kernel(si, sj)
        kkl = cross_kernel(sk, sl)
        rho = cross_kernel(kij, kkl)
        assert (rho == 1) == (kij == kkl)
        checks += 1

        kjk = cross_kernel(sj, sk)
        kkl2 = cross_kernel(sk, sl)
        kli = cross_kernel(sl, si)
        cycle = cross_kernel(cross_kernel(kij, kjk), cross_kernel(kkl2, kli))
        assert cycle == 1
        four_cycle_checks += 1

    return {
        "cross_ratio_collision_checks": checks,
        "four_cycle_checks": four_cycle_checks,
    }


def weighted_autocorrelation_audit(states, cross_kernel):
    # Deterministic signed weights: deliberately include zeros and cancellations.
    weights = [((37 * i + 11) % 13) - 6 for i in range(len(states))]
    class_weights = Counter()
    for state, w in zip(states, weights):
        class_weights[int(state["kernel"])] += w

    compressed = class_autocorrelation(class_weights, cross_kernel)

    direct = Counter()
    pair_checks = 0
    for i, a in enumerate(states):
        wa = weights[i]
        if wa == 0:
            continue
        sa = int(a["kernel"])
        for j, b in enumerate(states):
            wb = weights[j]
            if wb == 0:
                continue
            sb = int(b["kernel"])
            direct[cross_kernel(sa, sb)] += wa * wb
            pair_checks += 1

    # Drop exact-zero coefficients before comparing sparse Counters.
    direct = Counter({k: v for k, v in direct.items() if v != 0})
    compressed = Counter({k: v for k, v in compressed.items() if v != 0})
    assert direct == compressed

    principal = sum(v * v for v in class_weights.values())
    assert direct.get(1, 0) == principal

    weighted_energy = sum(v * v for v in direct.values())
    assert weighted_energy >= principal * principal

    return {
        "nonzero_state_weights": sum(w != 0 for w in weights),
        "direct_nonzero_pair_checks": pair_checks,
        "compressed_nonzero_class_weights": sum(v != 0 for v in class_weights.values()),
        "weighted_principal_coefficient": principal,
        "weighted_fourth_energy": weighted_energy,
    }


def route_b_value_character_audit(states, t40):
    legendre = t40["legendre"]
    jacobi = t40["jacobi"]
    primes = t40["AUX_PRIMES"][:5]
    checks = 0
    zero_cases = 0
    for state in states[:80]:
        f = int(state["F"])
        for i, p in enumerate(primes):
            for q in primes[i + 1 :]:
                lhs = legendre(f, p) * legendre(f, q)
                rhs = jacobi(f, p * q)
                assert lhs == rhs
                checks += 1
                if lhs == 0:
                    zero_cases += 1
    return {
        "route_b_value_level_character_checks": checks,
        "route_b_zero_cases": zero_cases,
        "packet_multiplicative_parameterization_proved": False,
    }


def main():
    summary = json.loads(SUMMARY.read_text())
    frozen40 = json.loads(T40_DATA.read_text())
    t40 = runpy.run_path(str(T40_SCRIPT), run_name="stage14_t40_import")
    t36 = runpy.run_path(str(t40["T36_SCRIPT"]), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()

    assert summary["stage"] == "Stage14-tH9"
    assert summary["status"] == "COMPLETE_SQUARECLASS_CROSS_RATIO_AND_AUTOCORRELATION_ATLAS"
    assert summary["requires_future_t_result"] is False
    assert frozen40["decision"]["STAGE14_T40"] == (
        "COMPLETE_ONE_CAUCHY_QUADRATIC_HECKE_CROSS_KERNEL_AND_ENERGY_BOUNDARY"
    )
    assert frozen40["decision"]["CROSS_KERNEL_IS_NORM_INDUCED_QUADRATIC_HECKE_CHARACTER_OVER_QI"] is True
    assert len(states) == 1120

    cross_kernel = t40["cross_kernel"]
    fundamental_discriminant = t40["fundamental_discriminant"]

    # Reproduce the exact t40 unweighted population and energy.
    energies, single, cross = t40["kernel_energy"](states)
    expected = summary["t40_frozen_regression"]
    assert energies["states"] == expected["states"]
    assert energies["distinct_single_squareclasses"] == expected["distinct_single_squareclasses"]
    assert energies["max_single_squareclass_multiplicity"] == expected["max_single_squareclass_multiplicity"]
    assert energies["global_second_squareclass_energy"] == expected["global_second_squareclass_energy_A1"]
    assert energies["ordered_cross_pairs"] == expected["ordered_cross_pairs"]
    assert energies["distinct_cross_kernels"] == expected["distinct_cross_kernels"]
    assert energies["cross_kernel_fourth_energy"] == expected["cross_kernel_fourth_energy_E4"]
    assert energies["global_second_squareclass_energy"] ** 2 == expected["principal_energy_A1_squared"]
    assert energies["cross_kernel_fourth_energy"] - energies["global_second_squareclass_energy"] ** 2 == expected["off_principal_E4"]

    # Unweighted pair counts are exactly the class autocorrelation.
    corr = class_autocorrelation(single, cross_kernel)
    assert corr == cross
    assert corr[1] == energies["global_second_squareclass_energy"]
    assert sum(v * v for v in corr.values()) == energies["cross_kernel_fourth_energy"]

    # D(kappa) is a lossless reindexing of positive squarefree kernels.
    discriminants = {k: fundamental_discriminant(k) for k in cross}
    assert len(set(discriminants.values())) == len(discriminants)

    group = structural_group_audit(single.keys(), cross_kernel)
    ratio = cross_ratio_audit(states, cross_kernel)
    weighted = weighted_autocorrelation_audit(states, cross_kernel)

    # Re-run t40's exact auxiliary Hecke/Dirichlet regression.
    reciprocity = t40["reciprocity_audit"](states)
    norm_pullback = t40["norm_induced_multiplicativity_audit"](cross)
    assert reciprocity["good_pair_prime_checks"] == expected["good_pair_prime_checks"]
    assert norm_pullback["norm_pullback_multiplicativity_checks"] == expected["norm_pullback_multiplicativity_checks"]

    route_b = route_b_value_character_audit(states, t40)

    # Locked prose/boundary markers.
    text = RESULT.read_text()
    required_markers = (
        "STAGE14_TH9=COMPLETE_SQUARECLASS_CROSS_RATIO_AND_AUTOCORRELATION_ATLAS",
        "PAIR_KERNEL_IS_SQUARECLASS_DIFFERENCE=true",
        "PAIR_COEFFICIENT_IS_SQUARECLASS_AUTOCORRELATION=true",
        "FOURTH_ENERGY_IS_SQUARECLASS_ADDITIVE_ENERGY=true",
        "AUXILIARY_ROUTE_QUADRATIC_HECKE_CERTIFICATE_PROVED=true",
        "PHYSICAL_ROUTE_HECKE_PACKET_CERTIFICATE_PROVED=false",
        "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-tH10",
    )
    for marker in required_markers:
        assert marker in text, marker

    report = {
        "unweighted": {
            "states": energies["states"],
            "classes": energies["distinct_single_squareclasses"],
            "A1": energies["global_second_squareclass_energy"],
            "cross_kernels": energies["distinct_cross_kernels"],
            "E4": energies["cross_kernel_fourth_energy"],
            "off_principal_E4": expected["off_principal_E4"],
        },
        "group": group,
        "cross_ratio": ratio,
        "weighted": weighted,
        "route_a": {
            **reciprocity,
            **norm_pullback,
            "quadratic_hecke_certificate": True,
        },
        "route_b": route_b,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH9 audit: PASS")


if __name__ == "__main__":
    main()
