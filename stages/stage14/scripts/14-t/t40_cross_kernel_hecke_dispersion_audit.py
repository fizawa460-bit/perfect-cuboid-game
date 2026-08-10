#!/usr/bin/env python3
"""Stage14-t40: one-Cauchy cross-kernel / norm-induced Hecke dispersion audit."""

from __future__ import annotations

from collections import Counter
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T39_DATA = ROOT / "stages/stage14/data/14-t39/fi_transfer_obstruction.json"
OUT = ROOT / "stages/stage14/data/14-t40/cross_kernel_hecke_dispersion.json"

AUX_PRIMES = (13, 17, 29, 37, 41, 53, 61, 73, 89, 97)
PAIR_SAMPLE = 96
B_FROZEN = 10_000


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def jacobi(a: int, n: int) -> int:
    assert n > 0 and n % 2 == 1
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                out = -out
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            out = -out
        a %= n
    return out if n == 1 else 0


def cross_kernel(s: int, t: int) -> int:
    """Squarefree kernel of the product of two positive squarefree kernels."""
    g = gcd(s, t)
    return (s // g) * (t // g)


def fundamental_discriminant(k: int) -> int:
    assert k > 0
    return k if k % 4 == 1 else 4 * k


def kernel_energy(states):
    single = Counter(int(s["kernel"]) for s in states)
    assert sum(single.values()) == len(states)

    second_energy = sum(v * v for v in single.values())
    cross = Counter()
    items = sorted(single.items())
    for s, rs in items:
        for t, rt in items:
            cross[cross_kernel(s, t)] += rs * rt

    assert sum(cross.values()) == len(states) ** 2
    assert cross[1] == second_energy

    fourth_energy = sum(v * v for v in cross.values())
    max_cross_kernel, max_cross_mult = max(cross.items(), key=lambda kv: kv[1])
    max_disc = max(fundamental_discriminant(k) for k in cross)

    return {
        "states": len(states),
        "distinct_single_squareclasses": len(single),
        "max_single_squareclass_multiplicity": max(single.values()),
        "global_second_squareclass_energy": second_energy,
        "ordered_cross_pairs": len(states) ** 2,
        "distinct_cross_kernels": len(cross),
        "principal_cross_kernel_pairs": cross[1],
        "max_cross_kernel": max_cross_kernel,
        "max_cross_kernel_multiplicity": max_cross_mult,
        "cross_kernel_fourth_energy": fourth_energy,
        "max_fundamental_discriminant_frozen": max_disc,
    }, single, cross


def reciprocity_audit(states):
    checks = 0
    bad_skips = 0
    sampled = states[:PAIR_SAMPLE]
    for a in sampled:
        for b in sampled:
            ka = int(a["kernel"])
            kb = int(b["kernel"])
            k = cross_kernel(ka, kb)
            D = fundamental_discriminant(k)
            for lam in AUX_PRIMES:
                # Pairwise good-auxiliary condition.  If lam divides a square
                # factor of F it is not visible in k, so use the actual values.
                if int(a["F"]) % lam == 0 or int(b["F"]) % lam == 0:
                    bad_skips += 1
                    continue
                lhs = legendre((int(a["F"]) % lam) * (int(b["F"]) % lam), lam)
                rhs_kernel = legendre(k, lam)
                rhs_disc = legendre(D, lam)
                assert lhs == rhs_kernel == rhs_disc
                checks += 1
    assert checks > 50_000
    return {"good_pair_prime_checks": checks, "bad_pair_prime_skips": bad_skips}


def norm_induced_multiplicativity_audit(cross):
    # For an odd Gaussian norm N(z), eta_D(z)=chi_D(N(z)) is multiplicative.
    gaussian_samples = ((1, 2), (2, 3), (1, 4), (2, 5), (4, 5), (2, 7))
    norms = [x * x + y * y for x, y in gaussian_samples]
    assert all(n % 2 == 1 for n in norms)

    checks = 0
    nonprincipal = [k for k in sorted(cross) if k != 1][:40]
    for k in nonprincipal:
        D = fundamental_discriminant(k)
        for n1 in norms:
            for n2 in norms:
                if gcd(D, n1 * n2) != 1:
                    continue
                e1 = jacobi(D, n1)
                e2 = jacobi(D, n2)
                e12 = jacobi(D, n1 * n2)
                assert e12 == e1 * e2
                checks += 1
    assert checks > 500
    return {"norm_pullback_multiplicativity_checks": checks}


def size_bound_audit(states, cross_stats):
    # t30 gives p^2+q^2<=2B.  In the super-sqrt (1,1) branch,
    # a^2+b^2=ell*m<=2B.  Hence |a|,|b|,|p|,|q|<=sqrt(2B),
    # each |g_i|<=4B, |F|<=256 B^4, and a pair kernel has
    # fundamental discriminant <=4*(256 B^4)^2=2^18 B^8.
    per_state_bound = 256 * (B_FROZEN ** 4)
    cross_disc_bound = (2 ** 18) * (B_FROZEN ** 8)
    max_f = max(int(s["F"]) for s in states)
    assert max_f <= per_state_bound
    assert cross_stats["max_fundamental_discriminant_frozen"] <= cross_disc_bound
    return {
        "max_F_frozen": max_f,
        "proved_per_state_bound": "|F|<=256*B^4",
        "proved_cross_fundamental_discriminant_bound": "|D_cross|<=2^18*B^8",
    }


def main():
    frozen39 = json.loads(T39_DATA.read_text())
    assert frozen39["decision"]["STAGE14_T39"] == (
        "COMPLETE_FI_TRANSFER_AUDIT_AND_EXTERNAL_AUXILIARY_TRILINEAR_BOUNDARY"
    )
    assert frozen39["decision"]["EXTERNAL_AUXILIARY_THIRD_VARIABLE_ESSENTIAL"] is True
    assert frozen39["decision"]["DIRECT_TWO_VARIABLE_FI_TRANSFER_VALID"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()
    assert len(states) == 1120

    energies, single, cross = kernel_energy(states)
    reciprocity = reciprocity_audit(states)
    norm_pullback = norm_induced_multiplicativity_audit(cross)
    sizes = size_bound_audit(states, energies)

    report = {
        "stage": "14-t40",
        "one_cauchy_dispersion": {
            "trilinear_form": "T=sum_lambda a_lambda sum_j d_j chi_lambda(F_j), j=(pi,gamma)",
            "cauchy_identity": (
                "|T|^2 <= P * sum_{j,j'} d_j*conj(d_j') K_Lambda(j,j'), "
                "K_Lambda=sum_lambda chi_lambda(F_j*F_j')"
            ),
            "cross_squarefree_kernel": "kappa_jj'=sqfree(F_j*F_j')",
            "fundamental_discriminant": "D(k)=k if k=1 mod 4, otherwise 4k",
            "good_auxiliary_identity": "chi_lambda(F_j*F_j')=chi_D(kappa_jj')(lambda)",
            "gaussian_pullback": "eta_D(z)=chi_D(N(z)) is a quadratic norm-induced Hecke character on Q(i)",
        },
        "quadratic_large_sieve_interface": {
            "available_theorem": (
                "Goldmakher-Louvel quadratic Hecke large sieve; in this norm-induced subfamily "
                "the classical rational quadratic large sieve already controls the auxiliary variable"
            ),
            "pair_coefficients": "A_D=sum_{j,j':D_jj'=D} d_j*conj(d_j')",
            "principal_coefficient": "A_1 is the global squareclass collision energy",
            "fourth_energy": "E4=sum_D |A_D|^2",
            "off_principal_bound": (
                "sum_{D!=1} A_D S_D << E4^(1/2)*(K+Q)^(1/2)*P^(1/2)*(KQ)^epsilon"
            ),
            "dispersion_bound": (
                "|T|^2 << P^2*A_1 + P^(3/2)*(K+Q)^(1/2)*E4^(1/2)*(KQ)^epsilon + bad_auxiliary_error"
            ),
        },
        "bad_auxiliary": {
            "issue": "if lambda divides F_j*F_j', Legendre is zero and kernel-only reciprocity need not equal the trace",
            "control": "each polynomial-size F has only B^o(1) prime divisors; remove/charge these pairwise bad incidences",
        },
        "frozen_audit": {
            "kernel_energy": energies,
            "reciprocity": reciprocity,
            "norm_pullback": norm_pullback,
            "size_bounds": sizes,
        },
        "remaining_boundary": {
            "principal_kernel": (
                "kappa_jj'=1 iff F_j and F_j' have the same rational squareclass; "
                "this is the global collision term and contains all target-target pairs"
            ),
            "nonprincipal_kernel": (
                "one Cauchy makes the auxiliary dependence genuinely quadratic-Hecke, but a direct "
                "large-sieve estimate pays the cross-kernel conductor height and the fourth-order energy E4"
            ),
            "local_energy_not_global": (
                "t36/t37 control collisions after freezing one side; t40 needs global collisions with both pi and gamma moving"
            ),
            "safe_conductor_height": "|D_cross|<=2^18*B^8 from the physical coordinate bounds",
        },
        "decision": {
            "STAGE14_T40": "COMPLETE_ONE_CAUCHY_QUADRATIC_HECKE_CROSS_KERNEL_AND_ENERGY_BOUNDARY",
            "ONE_CAUCHY_REMOVES_EXTERNAL_TRACE_NONMULTIPLICATIVITY": True,
            "CROSS_KERNEL_IS_QUADRATIC_DIRICHLET_CHARACTER_IN_AUXILIARY_NORM": True,
            "CROSS_KERNEL_IS_NORM_INDUCED_QUADRATIC_HECKE_CHARACTER_OVER_QI": True,
            "QUADRATIC_HECKE_LARGE_SIEVE_INTERFACE_VALID": True,
            "PRINCIPAL_CROSS_KERNEL_EQUALS_GLOBAL_SQUARECLASS_COLLISION": True,
            "FOURTH_ORDER_CROSS_KERNEL_ENERGY_REQUIRED": True,
            "SAFE_CROSS_CONDUCTOR_BOUND": "2^18*B^8",
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t41 analyze the principal and fourth-order cross-kernel energies globally. "
                "Exploit the t38 genus-one moving-prime fibers and t37 reverse fibers simultaneously; "
                "test whether a two-sided incidence/energy decomposition gives A_1 and E4 below the sqrt-B barrier"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["frozen_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
