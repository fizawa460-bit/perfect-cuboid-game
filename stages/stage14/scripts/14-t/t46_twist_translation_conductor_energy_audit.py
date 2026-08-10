#!/usr/bin/env python3
"""Stage14-t46: collapse the t45 moving-conductor family to a twist-translation of squareclasses."""

from __future__ import annotations

from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T45_DATA = ROOT / "stages/stage14/data/14-t45/two_canonical_character.json"
OUT = ROOT / "stages/stage14/data/14-t46/twist_translation_conductor_energy.json"

B = 10_000
HEAVY_THRESHOLD = 20
TOP_TARGET_COUNT = 8


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def squarefree_product(a: int, b: int) -> int:
    g = gcd(a, b)
    return (a // g) * (b // g)


def fundamental_discriminant_from_squarefree(d: int) -> int:
    assert d > 0
    return d if d % 4 == 1 else 4 * d


def main():
    t45 = json.loads(T45_DATA.read_text())
    assert t45["decision"]["STAGE14_T45"] == "COMPLETE_TWO_CANONICAL_LOCAL_CHARACTER_AND_MANY_CONDUCTOR_BARRIER"
    assert t45["decision"]["FIXED_PARTNER_QUADRATIC_CHARACTER_CERTIFIED"] is True
    assert t45["decision"]["MANY_CONDUCTOR_AGGREGATION_REQUIRED"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    states = t36["build_frozen_states"]()
    reps = t42["reciprocal_quotient"](states)
    cross_kernel = t42["cross_kernel"]
    assert len(reps) == 560

    kernel_hist = Counter(s["kernel"] for s in reps)
    ell_hist = Counter(s["ell"] for s in reps)
    H = len(reps)
    A1 = sum(m * m for m in kernel_hist.values())
    E_ell = sum(m * m for m in ell_hist.values())
    assert len(kernel_hist) == 544
    assert A1 == 592

    conv = Counter()
    kernels_by_state = [s["kernel"] for s in reps]
    for kx in kernels_by_state:
        for ky in kernels_by_state:
            conv[cross_kernel(kx, ky)] += 1
    assert conv[1] == A1
    heavy = [(tau, mult) for tau, mult in conv.items() if tau != 1 and mult > HEAVY_THRESHOLD]
    heavy.sort(key=lambda kv: (-kv[1], kv[0]))
    assert len(heavy) == 72
    targets = [tau for tau, _mult in heavy[:TOP_TARGET_COUNT]]

    # Base conductor family: for odd test primes, chi_{D(k)}(ell)=(k/ell).
    base_D = {k: fundamental_discriminant_from_squarefree(k) for k in kernel_hist}
    base_max_D = max(base_D.values())
    base_max_k = max(kernel_hist)

    target_rows = []
    translation_involution_checks = 0
    character_factorization_checks = 0
    for tau in targets:
        translated_hist = Counter()
        translated_kernel_hist = Counter()
        for y in reps:
            kt = squarefree_product(tau, y["kernel"])
            Dt = fundamental_discriminant_from_squarefree(kt)
            translated_kernel_hist[kt] += 1
            translated_hist[Dt] += 1
            assert squarefree_product(tau, kt) == y["kernel"]
            translation_involution_checks += 1

        # Multiplication by tau is an involution of the positive squareclass group, and D(k)
        # is injective on positive squarefree k. Hence the multiplicity profile is unchanged.
        assert sorted(translated_hist.values()) == sorted(kernel_hist.values())
        assert len(translated_hist) == len(kernel_hist)
        assert sum(m * m for m in translated_hist.values()) == A1
        assert max(translated_hist.values()) == max(kernel_hist.values())
        assert translated_hist.get(1, 0) == kernel_hist.get(tau, 0)

        tau_bad_ells = sorted(ell for ell in ell_hist if tau % ell == 0)
        # t44's safe support ledger: a fixed twist can expose only O(1) super-sqrt canonical primes.
        assert len(tau_bad_ells) <= 16

        # The apparently tau-dependent many-conductor matrix is just a row-sign twist of the
        # base squareclass character matrix on good rows:
        #   chi_{D(tau*k)}(ell) = (tau*k/ell) = (tau/ell)(k/ell).
        for ell in ell_hist:
            if tau % ell == 0:
                continue
            for k in kernel_hist:
                if k % ell == 0:
                    continue
                kt = squarefree_product(tau, k)
                Dt = fundamental_discriminant_from_squarefree(kt)
                lhs = legendre(Dt, ell)
                rhs = legendre(tau, ell) * legendre(k, ell)
                assert lhs == rhs
                character_factorization_checks += 1

        target_rows.append({
            "tau": tau,
            "global_cross_kernel_multiplicity": conv[tau],
            "translated_distinct_conductors": len(translated_hist),
            "translated_conductor_energy": sum(m * m for m in translated_hist.values()),
            "translated_max_multiplicity": max(translated_hist.values()),
            "principal_conductor_multiplicity": translated_hist.get(1, 0),
            "expected_principal_slice_r_tau": kernel_hist.get(tau, 0),
            "tau_bad_canonical_ells": tau_bad_ells,
            "max_translated_fundamental_discriminant": max(translated_hist),
        })

    # Exact finite base-character Gram ledger on distinct canonical primes versus distinct
    # squareclasses. This is diagnostic only; no asymptotic spectral theorem is inferred.
    ells = sorted(ell_hist)
    kernels = sorted(kernel_hist)
    row_vectors = {}
    for ell in ells:
        row_vectors[ell] = [legendre(k, ell) for k in kernels]
    max_offdiag_abs_correlation = 0
    max_offdiag_pair = None
    diagonal_min = None
    diagonal_max = None
    for i, ell1 in enumerate(ells):
        r1 = row_vectors[ell1]
        diag = sum(v * v for v in r1)
        diagonal_min = diag if diagonal_min is None else min(diagonal_min, diag)
        diagonal_max = diag if diagonal_max is None else max(diagonal_max, diag)
        for ell2 in ells[i + 1:]:
            r2 = row_vectors[ell2]
            corr = sum(a * b for a, b in zip(r1, r2))
            if abs(corr) > max_offdiag_abs_correlation:
                max_offdiag_abs_correlation = abs(corr)
                max_offdiag_pair = [ell1, ell2, corr]

    # Safe asymptotic size ledger. A single state has |F|<=256 B^4 (t40), so its squareclass
    # kappa<=256 B^4 and D(kappa)<=2^10 B^4. The t46 factorization removes the extra tau from
    # the moving conductor, reducing the naive translated-conductor exponent back to 4.
    safe_base_conductor_bound = 2**10 * B**4
    assert base_max_D <= safe_base_conductor_bound
    Q_frozen = max(ells)
    R_kernel = len(kernels)
    L_ell = len(ells)

    # Unit-weight compressed coefficient energies. For arbitrary coefficients these become
    # E_kappa=sum_k |sum_{y:kappa_y=k} b_y|^2 and
    # E_ell=sum_ell |sum_{x:ell_x=ell} a_x|^2.
    # Classical quadratic-large-sieve interface (schematic, theorem supplied externally):
    # |S_tau|^2 << E_kappa * (K+Q) * E_ell * (KQ)^eps.
    # The elementary Frobenius/cardinality bound is
    # |S_tau|^2 <= (R_kernel*L_ell) * E_kappa * E_ell.
    large_sieve_unit_core = A1 * (base_max_D + Q_frozen) * E_ell
    frobenius_unit_core = R_kernel * L_ell * A1 * E_ell

    report = {
        "stage": "14-t46",
        "squareclass_translation": {
            "states": H,
            "distinct_squareclasses": len(kernel_hist),
            "squareclass_energy_A1": A1,
            "max_squareclass_multiplicity": max(kernel_hist.values()),
            "translation_involution_checks": translation_involution_checks,
            "identity": "kappa_{tau,y}=tau*kappa_y in Q^x/Q^{x2}; multiplication by tau is an involution",
            "principal_slice": "D_{tau,y}=1 iff kappa_y=tau",
        },
        "twist_independent_character_operator": {
            "identity": "chi_{D(tau*kappa)}(ell)=chi_tau(ell)*chi_{D(kappa)}(ell) on ell not dividing 2*tau*kappa",
            "character_factorization_checks": character_factorization_checks,
            "base_distinct_conductors": len(base_D),
            "base_max_squarefree_kernel": base_max_k,
            "base_max_fundamental_discriminant": base_max_D,
            "safe_asymptotic_base_conductor_bound": "2^10*B^4",
            "naive_translated_conductor_exponent_removed": True,
            "all_twists_share_same_base_operator_up_to_row_signs": True,
        },
        "canonical_prime_side": {
            "distinct_canonical_ells": len(ell_hist),
            "canonical_ell_energy_unit_weights": E_ell,
            "max_states_per_canonical_ell": max(ell_hist.values()),
            "max_frozen_canonical_ell": Q_frozen,
        },
        "top_heavy_twists": target_rows,
        "base_character_gram_diagnostic": {
            "rows_distinct_ell": L_ell,
            "columns_distinct_squareclass": R_kernel,
            "row_squared_norm_min": diagonal_min,
            "row_squared_norm_max": diagonal_max,
            "max_offdiagonal_abs_correlation": max_offdiag_abs_correlation,
            "max_offdiagonal_pair": max_offdiag_pair,
            "asymptotic_claim": False,
        },
        "large_sieve_interface": {
            "compressed_form": "S_tau=sum_ell A_ell*chi_tau(ell)*sum_kappa B_kappa*chi_kappa(ell)",
            "weighted_squareclass_energy": "E_kappa=sum_kappa |B_kappa|^2; for unit state weights E_kappa=A1",
            "weighted_canonical_energy": "E_ell=sum_ell |A_ell|^2",
            "quadratic_large_sieve_schematic": "|S_tau|^2 << E_kappa*(K+Q)*E_ell*(KQ)^eps",
            "elementary_sparse_frobenius": "|S_tau|^2 <= (#kappa)*(#ell)*E_kappa*E_ell",
            "frozen_unit_large_sieve_rhs_core_without_eps": large_sieve_unit_core,
            "frozen_unit_frobenius_rhs": frobenius_unit_core,
            "critical_Q": "B^(1/2+o(1))",
            "safe_K": "B^(4+o(1))",
            "standard_max_range_large_sieve_has_B2_square_root_cost": True,
            "sparse_support_cardinality_not_used_by_standard_max_range_bound": True,
        },
        "detector_boundary": {
            "two_endogenous_local_tests_constant_term": "1/4",
            "operator_cancellation_alone_removes_constant_term": False,
            "growing_test_family_or_centered_dispersion_still_required": True,
        },
        "th13": {
            "needed": True,
            "updated_task": "exploit t46 twist-translation: build a twist-uniform sparse squareclass quadratic-character operator receiver using E_kappa rather than arbitrary conductor count; compare max-range quadratic large sieve with cardinality/energy-sensitive sparse alternatives, retain canonical selector and tau-bad O(1) slices, and give the critical exponent ledger",
        },
        "decision": {
            "STAGE14_T46": "COMPLETE_TWIST_TRANSLATION_CONDUCTOR_ENERGY_AND_BASE_OPERATOR_REDUCTION",
            "MOVING_CONDUCTOR_FAMILY_IS_TWIST_TRANSLATED_SQUARECLASS_SPECTRUM": True,
            "TRANSLATED_CONDUCTOR_MULTIPLICITY_ENERGY_EQUALS_A1": True,
            "PRINCIPAL_CONDUCTOR_SLICE_EQUALS_R_TAU": True,
            "TWIST_DEPENDENCE_FACTORS_AS_ROW_CHARACTER": True,
            "ALL_TWISTS_SHARE_BASE_QUADRATIC_CHARACTER_OPERATOR": True,
            "SAFE_BASE_CONDUCTOR_BOUND": "2^10*B^4",
            "STANDARD_QUADRATIC_LARGE_SIEVE_INTERFACE_VALID": True,
            "STANDARD_MAX_RANGE_LARGE_SIEVE_CLOSES_CRITICAL_STRIP": False,
            "SPARSE_CARDINALITY_ENERGY_LARGE_SIEVE_PROVED": False,
            "TWO_LOCAL_FILTER_CONSTANT_TERM_REMOVED": False,
            "GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH13_NEEDED": True,
            "NEXT": "Stage14-t47 attack the twist-independent sparse squareclass character operator and the 1/4 detector baseline; use tH13 if available for a cardinality/energy-sensitive adapter",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
