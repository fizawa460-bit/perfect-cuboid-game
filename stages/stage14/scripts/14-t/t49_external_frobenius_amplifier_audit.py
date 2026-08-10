#!/usr/bin/env python3
"""Stage14-t49: external split-prime Frobenius amplifier / mean-square audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T48_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t48_physical_row_correlation_audit.py"
T48_DATA = ROOT / "stages/stage14/data/14-t48/physical_row_correlation.json"
TH12 = ROOT / "stages/stage14/data/tH12/ld2_kummer_incidence_receiver_summary.json"
TH13 = ROOT / "stages/stage14/data/tH13/sparse_many_conductor_adapter_summary.json"
OUT = ROOT / "stages/stage14/data/14-t49/external_frobenius_amplifier.json"

EXTERNAL_SPLIT_PRIME_COUNT = 128
EXTERNAL_SPLIT_PRIME_START = 2000


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def external_split_primes(start: int, count: int):
    out = []
    n = max(5, start | 1)
    while len(out) < count:
        if n % 4 == 1 and is_prime(n):
            out.append(n)
        n += 2
    return out


def cross_kernel(a: int, b: int) -> int:
    g = gcd(a, b)
    return (a // g) * (b // g)


def gram_stats(reps, primes, label: str):
    H = len(reps)
    P = len(primes)
    r = Counter(s["kernel"] for s in reps)
    A1 = sum(v * v for v in r.values())

    rows = {p: [legendre(s["kernel"], p) for s in reps] for p in primes}
    G = {}
    row_l2 = {}
    for p in primes:
        for q in primes:
            G[(p, q)] = sum(a * b for a, b in zip(rows[p], rows[q]))
    for p in primes:
        row_l2[p] = sum(G[(p, q)] ** 2 for q in primes if q != p)

    diag = sum(G[(p, p)] ** 2 for p in primes)
    offdiag = sum(G[(p, q)] ** 2 for p in primes for q in primes if p != q)
    full = diag + offdiag

    bad_counts = {k: sum(k % p == 0 for p in primes) for k in r}
    max_bad = max(bad_counts.values())
    min_good = P - max_bad
    principal_exact = sum(r[k] ** 2 * (P - bad_counts[k]) ** 2 for k in r)
    assert principal_exact <= full
    assert min_good > 0

    exact_receiver_upper = full / (min_good * min_good)
    coarse_receiver_upper = (P * H * H + offdiag) / (min_good * min_good)
    assert exact_receiver_upper <= coarse_receiver_upper + 1e-12

    return {
        "label": label,
        "H": H,
        "P": P,
        "A1": A1,
        "min_test_prime": min(primes),
        "max_test_prime": max(primes),
        "max_bad_test_primes_per_squareclass": max_bad,
        "principal_exact_frobenius_contribution": principal_exact,
        "full_frobenius": full,
        "diagonal_frobenius": diag,
        "offdiagonal_frobenius": offdiag,
        "max_offdiagonal_row_l2": max(row_l2.values()),
        "average_offdiagonal_row_l2": offdiag / P,
        "max_to_average_row_l2_ratio": max(row_l2.values()) / (offdiag / P),
        "offdiag_to_random_scale_H_P_Pminus1": offdiag / (H * P * (P - 1)),
        "exact_A1_receiver_upper": exact_receiver_upper,
        "coarse_A1_receiver_upper": coarse_receiver_upper,
    }, rows, G


def product_kernel_frobenius_audit(r, primes, expected_full: int):
    # For squarefree a,b and g=gcd(a,b),
    # chi_a(p)chi_b(p)=1_{p not|g} chi_{sqf(ab)}(p).
    # Grouping by (cross-kernel, shared test-prime support) is therefore exact.
    groups = Counter()
    tau_mass = Counter()
    for a, ra in r.items():
        for b, rb in r.items():
            w = ra * rb
            tau = cross_kernel(a, b)
            g = gcd(a, b)
            shared = tuple(p for p in primes if g % p == 0)
            groups[(tau, shared)] += w
            tau_mass[tau] += w

    reconstructed = 0
    principal = 0
    nonempty_shared_mass = 0
    for (tau, shared), mult in groups.items():
        shared_set = set(shared)
        S = sum(legendre(tau, p) for p in primes if p not in shared_set)
        term = mult * S * S
        reconstructed += term
        if tau == 1:
            principal += term
        if shared:
            nonempty_shared_mass += mult
    assert reconstructed == expected_full

    H2 = sum(groups.values())
    E4 = sum(v * v for v in tau_mass.values())
    nonprincipal_E4 = E4 - tau_mass[1] ** 2
    assert tau_mass[1] == 592
    assert E4 == 1_324_576

    return {
        "exact_identity": "||G||_F^2=sum_(tau,J) c(tau,J)*|sum_{p in P\\J} chi_tau(p)|^2",
        "refinement_groups": len(groups),
        "cross_kernel_support": len(tau_mass),
        "total_pair_mass_sum_c": H2,
        "max_cross_kernel_multiplicity": max(tau_mass.values()),
        "max_nonprincipal_cross_kernel_multiplicity": max(v for k, v in tau_mass.items() if k != 1),
        "principal_cross_kernel_mass": tau_mass[1],
        "principal_frobenius_contribution": principal,
        "pair_mass_with_nonempty_shared_test_prime_support": nonempty_shared_mass,
        "naive_pair_coefficient_energy_sum_c_squared": E4,
        "naive_nonprincipal_pair_coefficient_energy": nonprincipal_E4,
        "reconstructed_full_frobenius": reconstructed,
        "warning": "collapsing ordered state pairs to coefficients c(tau) before physical/norm-index cancellation imports E4 as coefficient energy; keep the signed physical aggregate before this collapse",
    }


def main():
    t48 = json.loads(T48_DATA.read_text())
    th12 = json.loads(TH12.read_text())
    th13 = json.loads(TH13.read_text())
    assert t48["decision"]["STAGE14_T48"] == "COMPLETE_PHYSICAL_ROW_CORRELATION_BRIDGE_AND_DIFFUSE_COHERENCE_AUDIT"
    assert t48["decision"]["SIGNED_COMMON_REFINEMENT_AGGREGATION_REQUIRED"] is True
    assert th12["status"] == "COMPLETE_LD2_KUMMER_CANONICAL_PRIME_COMMON_CORE_RECEIVER"
    assert th13["status"] == "COMPLETE_SPARSE_MANY_CONDUCTOR_LARGE_SIEVE_DISPERSION_ADAPTER"

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    t48mod = runpy.run_path(str(T48_SCRIPT), run_name="stage14_t48_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    reduced_physical_F = t48mod["reduced_physical_F"]
    assert len(reps) == 560

    canonical_primes = sorted({s["ell"] for s in reps})
    external_primes = external_split_primes(EXTERNAL_SPLIT_PRIME_START, EXTERNAL_SPLIT_PRIME_COUNT)
    assert len(canonical_primes) == 87
    assert all(p % 4 == 1 for p in canonical_primes)
    assert all(p % 4 == 1 for p in external_primes)

    canonical, _, _ = gram_stats(reps, canonical_primes, "frozen_endogenous_canonical_split_primes")
    external, _, _ = gram_stats(reps, external_primes, "external_split_prime_amplifier")

    # The character bridge is not canonical-prime-specific: any odd split auxiliary
    # prime sees the same squareclass after removing the state's even canonical square.
    external_physical_checks = 0
    for s in reps:
        Fr = reduced_physical_F(s)
        for p in external_primes:
            assert legendre(s["kernel"], p) == legendre(Fr, p)
            external_physical_checks += 1

    r = Counter(s["kernel"] for s in reps)
    pk = product_kernel_frobenius_audit(r, canonical_primes, canonical["full_frobenius"])

    report = {
        "stage": "14-t49",
        "external_split_prime_amplifier": {
            "identity": "for any split auxiliary p=1 mod4, chi_kappa(p)=(Ftilde/p); the centered Gram detector does not require p to be a state's canonical prime",
            "external_physical_character_checks": external_physical_checks,
            "finite_external_prime_count": len(external_primes),
            "finite_external_prime_start": EXTERNAL_SPLIT_PRIME_START,
            "bad_prime_policy": "zeros are retained exactly in the Gram matrix; asymptotically primes dividing the polynomial-size physical discriminant/norm data form B^o(1) incidences per state and must be charged separately before t32 good-prime completion",
        },
        "frobenius_receiver": {
            "principal_lower": "A1*(P-b)^2 <= ||G||_F^2, where b=max_kappa #{p in P:p|kappa}",
            "diagonal_upper": "sum_p G_pp^2 <= P*H^2",
            "exact_receiver": "A1 <= (P*H^2 + R_off)/(P-b)^2, R_off=sum_{p!=q}|G_pq|^2",
            "near_linear_sufficient": "if b=o(P), P>=H*B^-o(1), and R_off<=H*P^2*B^o(1), then A1<=H*B^o(1)",
            "uniform_worst_row_required": False,
            "remaining_mean_square": "R_off=sum_{p!=q in external split amplifier}|sum_s (Ftilde_s/p)(Ftilde_s/q)|^2",
            "t32_native_interface": "each offdiagonal p,q summand is exactly the split two-prime physical four-linear character object whose angular completion is bounded in t32 on good norm-index cells",
        },
        "frozen_endogenous": canonical,
        "frozen_external_amplifier": external,
        "product_kernel_order_of_operations": pk,
        "proof_contract": {
            "t32_split_torus_completion_must_precede_pair_coefficient_collapse": True,
            "tH12_common_refinement_must_remain_signed": True,
            "tH13_same_modulus_dispersion_is_compatible_after_signed_norm_index_aggregation": True,
            "naive_pair_collapse_is_circular_because_energy_is_E4": True,
            "global_external_two_prime_mean_square_power_saving_proved": False,
            "external_bad_auxiliary_aggregate_bound_proved": False,
        },
        "tH_decision": {
            "additional_tH_needed": False,
            "reason": "the new Frobenius amplifier is an exact reordering of the same t32+tH12+tH13 objects; the missing input is the live signed norm-index mean square, not a new adapter",
            "reopen_trigger": "only if t50 exposes a repeated-character/selector obstruction not representable by the existing common-refinement and same-modulus dispersion receivers",
        },
        "decision": {
            "STAGE14_T49": "COMPLETE_EXTERNAL_SPLIT_PRIME_FROBENIUS_AMPLIFIER_AND_NONCIRCULAR_MEAN_SQUARE_REDUCTION",
            "EXTERNAL_SPLIT_PRIME_AMPLIFIER_VALID": True,
            "PRINCIPAL_COLLISION_FROBENIUS_LOWER_BOUND": True,
            "UNIFORM_WORST_ROW_BOUND_REQUIRED": False,
            "AVERAGED_TWO_PRIME_MEAN_SQUARE_SUFFICIENT_FOR_A1_NEAR_LINEAR": True,
            "T32_TWO_PRIME_PHYSICAL_INTERFACE_NATIVE": True,
            "NAIVE_PRODUCT_KERNEL_PAIR_COEFFICIENT_ENERGY_EQUALS_E4": True,
            "PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_IS_CIRCULAR": True,
            "SIGNED_NORM_INDEX_AGGREGATION_BEFORE_PAIR_COLLAPSE_REQUIRED": True,
            "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED": False,
            "EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_NEEDED": False,
            "NEXT": "Stage14-t50 prove the external split-prime offdiagonal Frobenius mean square R_off<=H*P^2*B^o(1) on the critical family by applying t32 angular completion before Cauchy/pair collapse and retaining the tH12/tH13 signed divisor-coupled norm-index aggregation; separately charge auxiliary bad-prime incidences",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
