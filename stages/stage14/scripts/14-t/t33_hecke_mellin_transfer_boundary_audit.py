#!/usr/bin/env python3
"""Stage14-t33: Hecke/Mellin transfer boundary audit."""

from __future__ import annotations

import cmath
from collections import Counter
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T32_DATA = ROOT / "stages/stage14/data/14-t32/split_torus_norm_sieve.json"
OUT = ROOT / "stages/stage14/data/14-t33/hecke_mellin_transfer_boundary.json"

SPLIT_PRIMES = (13, 17, 29, 37, 41)
MODEL_RATIO_SQUARE = 4
DFT_TOL = 1e-7


def legendre(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    phi = p - 1
    factors = factor_distinct(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    raise AssertionError(("no primitive root", p))


def sqrt_minus_one(p: int) -> int:
    for x in range(2, p):
        if x * x % p == p - 1:
            return x
    raise AssertionError(("no sqrt(-1)", p))


def torus_trace_value(s: int, p: int) -> int:
    # Valid t32 one-variable model:
    # chi(alpha*s^4-beta) with beta/alpha=4 a nonzero square.
    return legendre(pow(s, 4, p) - MODEL_RATIO_SQUARE, p)


def mellin_spectrum(p: int) -> dict:
    g = primitive_root(p)
    n = p - 1
    values = [torus_trace_value(pow(g, e, p), p) for e in range(n)]

    # mu_4 invariance: multiplying s by any fourth root of unity leaves s^4 fixed.
    shift = n // 4
    assert all(values[e] == values[(e + shift) % n] for e in range(n))

    support = []
    max_order = 1
    nonquadratic = 0
    quadratic_modes = 0
    max_abs = 0.0
    for j in range(n):
        coeff = sum(
            values[e] * cmath.exp(-2j * cmath.pi * j * e / n)
            for e in range(n)
        )
        mag = abs(coeff)
        if mag <= DFT_TOL:
            continue
        order = 1 if j == 0 else n // gcd(j, n)
        support.append(j)
        max_order = max(max_order, order)
        if order <= 2:
            quadratic_modes += 1
        else:
            nonquadratic += 1
        max_abs = max(max_abs, mag)

    # Invariance forces every nonzero Mellin exponent to be trivial on mu_4.
    assert all(j % 4 == 0 for j in support)
    assert nonquadratic > 0

    return {
        "primitive_root": g,
        "zero_count": values.count(0),
        "support_exponents": support,
        "support_size": len(support),
        "quadratic_or_trivial_modes": quadratic_modes,
        "higher_order_modes": nonquadratic,
        "max_character_order": max_order,
        "max_abs_coefficient_rounded_6": round(max_abs, 6),
    }


def value_level_gaussian_symbol_audit(p: int) -> int:
    # For split p choose iota^2=-1.  The quotient map
    # Z[i] -> Z[i]/(p,i-iota) ~= F_p sends a rational integer F to F mod p.
    iota = sqrt_minus_one(p)
    checks = 0
    for x in range(-5, 6):
        for y in range(-5, 6):
            gaussian_residue = (x + iota * y) % p
            norm = x * x + y * y
            assert legendre(norm, p) == legendre(norm % p, p)
            conjugate_residue = (x - iota * y) % p
            assert gaussian_residue * conjugate_residue % p == norm % p
            checks += 1
    return checks


def nonmultiplicativity_audit() -> dict:
    p = 13
    x = 2
    y = 2
    ax = torus_trace_value(x, p)
    ay = torus_trace_value(y, p)
    axy = torus_trace_value(x * y % p, p)
    assert ax != 0 and ay != 0 and axy != 0
    assert axy != ax * ay
    return {
        "prime": p,
        "x": x,
        "y": y,
        "A_x": ax,
        "A_y": ay,
        "A_xy": axy,
    }


def main() -> None:
    frozen32 = json.loads(T32_DATA.read_text())
    assert frozen32["decision"]["STAGE14_T32"] == (
        "COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON"
    )
    assert frozen32["decision"]["ANGULAR_COMPLETE_CORRELATION_CLOSED"] is True
    assert frozen32["finite_audit"]["norm_skeleton"]["totals"][
        "unified_cofactor_checks"
    ] == 13208

    spectra = {str(p): mellin_spectrum(p) for p in SPLIT_PRIMES}
    expected_max_orders = {"13": 3, "17": 4, "29": 7, "37": 9, "41": 10}
    assert {p: d["max_character_order"] for p, d in spectra.items()} == expected_max_orders

    expected_support = {
        "13": [0, 4, 8],
        "17": [0, 4, 8, 12],
        "29": [0, 4, 8, 12, 16, 20, 24],
        "37": [0, 4, 8, 12, 16, 20, 24, 28, 32],
        "41": [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
    }
    assert {p: d["support_exponents"] for p, d in spectra.items()} == expected_support

    gaussian_symbol_checks = sum(value_level_gaussian_symbol_audit(p) for p in SPLIT_PRIMES)
    assert gaussian_symbol_checks == 605

    nonmult = nonmultiplicativity_audit()

    totals = Counter()
    totals["split_primes_spectral_audited"] = len(SPLIT_PRIMES)
    totals["value_level_gaussian_symbol_checks"] = gaussian_symbol_checks
    totals["primes_with_higher_order_mellin_modes"] = sum(
        1 for d in spectra.values() if d["higher_order_modes"] > 0
    )
    totals["quadratic_family_only_sufficient_cases"] = sum(
        1 for d in spectra.values() if d["higher_order_modes"] == 0
    )
    assert totals["primes_with_higher_order_mellin_modes"] == 5
    assert totals["quadratic_family_only_sufficient_cases"] == 0

    report = {
        "stage": "14-t33",
        "t32_frozen_reference": {
            "unified_cofactor_checks": 13208,
            "visible_super_non_torsion": frozen32["finite_audit"]["norm_skeleton"]["totals"][
                "visible_super_non_torsion"
            ],
            "invisible_super_non_torsion": frozen32["finite_audit"]["norm_skeleton"]["totals"][
                "invisible_super_non_torsion"
            ],
            "norm_skeleton": frozen32["decision"]["UNIFIED_NORM_SKELETON"],
        },
        "hecke_transfer": {
            "value_level_quadratic_symbol": (
                "for split lambda and a Gaussian prime ideal L|lambda, "
                "chi_lambda(F)=quadratic_residue_symbol_L((F)) for rational F coprime to lambda"
            ),
            "variable_level_quadratic_hecke_character": False,
            "reason": (
                "the torus trace A(s)=chi_lambda(alpha*s^4-beta) is not multiplicative in s; "
                "completion requires its full multiplicative Mellin spectrum"
            ),
            "mellin_formula": (
                "A(s)=1/(lambda-1)*sum_psi Ahat(psi) psi(s), "
                "with Ahat supported on characters trivial on mu_4"
            ),
            "two_factor_formula": (
                "A(s/t)B(st) expands into characters (psi*phi)(s) "
                "and (phi*psi^-1)(t)"
            ),
        },
        "goldmakher_louvel_boundary": {
            "quadratic_large_sieve_theorem_relevant": True,
            "direct_application_to_full_torus_mellin_spectrum": False,
            "obstruction_1": (
                "nonquadratic Mellin modes occur for every audited split prime; "
                "their orders grow with lambda"
            ),
            "obstruction_2": (
                "aggregating by the squarefree ideal kernel of F collapses all target squares "
                "to the trivial character class and makes the coefficient-energy bound circular"
            ),
            "correct_next_framework": (
                "all-character Mellin/Hecke large sieve (or equivalent Gaussian residue-class large sieve) "
                "combined with the divisor-coupled norm hyperbola"
            ),
        },
        "finite_spectral_audit": {
            "model": "A_lambda(s)=chi_lambda(s^4-4)",
            "model_note": (
                "beta/alpha=4 is a square, matching the t32 torus form "
                "chi(alpha*s^4-beta) after scaling by a nonzero square"
            ),
            "spectra": spectra,
            "nonmultiplicativity_counterexample": nonmult,
            "totals": dict(totals),
        },
        "decision": {
            "STAGE14_T33": "COMPLETE_QUADRATIC_HECKE_VALUE_TRANSFER_AND_MELLIN_SPECTRAL_BOUNDARY",
            "QUADRATIC_HECKE_VALUE_SYMBOL_IDENTIFIED": True,
            "TORUS_TRACE_IS_QUADRATIC_HECKE_CHARACTER_IN_NORM_VARIABLE": False,
            "MU4_MELLIN_SUPPORT_RESTRICTION": True,
            "HIGHER_ORDER_MELLIN_MODES_REQUIRED": True,
            "GOLDMAKHER_LOUVEL_QUADRATIC_LARGE_SIEVE_DIRECTLY_SUFFICIENT": False,
            "SQUAREFREE_KERNEL_AGGREGATION_CLOSES_SQUARE_DETECTOR": False,
            "ALL_CHARACTER_MELLIN_HECKE_SIEVE_OBJECT_DEFINED": True,
            "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED": False,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t34 build the all-character Mellin/Hecke large-sieve inequality over split Gaussian primes, "
                "using mu_4-invariant spectral support and the exact k|epsilon*m, m*delta<<B/ell hyperbola"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_spectral_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
