#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5q.

The analytic statements are proved in result.md.  This script checks the exact
finite interfaces: local Fourier energies, H-row equality, E-Walsh expansion,
critical exponent atlas, signed-root transversality, and the sawtooth count.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import math


def energy(coeffs):
    return sum(c * c for c in coeffs)


def row_coefficients(row, s):
    if row in ("selected_SH", "unselected_SH"):
        return (Fraction(1, 2), Fraction(1, 2))
    if row == "selected_X":
        return (Fraction(1 + s, 4), Fraction(1 + s, 4))
    if row == "unselected_X":
        return (Fraction(3 - s, 4), Fraction(1 + s, 4))
    raise ValueError(row)


def check_row_energies():
    rows = ("selected_SH", "selected_X", "unselected_SH", "unselected_X")
    out = {}
    for row in rows:
        for s in (-1, 1):
            coeffs = row_coefficients(row, s)
            e = energy(coeffs)
            assert e <= 1, (row, s, coeffs, e)
            out[f"{row}_s{s}"] = str(e)

    # Tensor-product coefficient energy is the product of primewise energies.
    tensor_checks = 0
    for choices in product(rows, repeat=4):
        for signs in product((-1, 1), repeat=4):
            e = Fraction(1, 1)
            for row, s in zip(choices, signs):
                e *= energy(row_coefficients(row, s))
            assert e <= 1
            tensor_checks += 1
    return out, tensor_checks


def check_h_row_equality():
    checks = 0
    for a1, a2, a3 in product((-1, 1), repeat=3):
        if a1 * a2 * a3 != 1:
            continue
        selected = (a2 * a3 == 1) and (a1 == 1)
        unselected = a1 == 1
        assert selected == unselected, (a1, a2, a3)
        checks += 1
    return checks


def check_e_walsh():
    checks = 0
    norm_rows = []
    for k in range(1, 7):
        subsets = list(product((0, 1), repeat=k))
        weight = Fraction(1, 2**k)
        l1 = sum(weight for _ in subsets)
        l2sq = sum(weight * weight for _ in subsets)
        assert l1 == 1
        assert l2sq == Fraction(1, 2**k)
        assert l2sq <= 1
        norm_rows.append((k, str(l1), str(l2sq)))

        for xs in product((-1, 1), repeat=k):
            lhs = Fraction(1, 1)
            for x in xs:
                lhs *= Fraction(1 + x, 2)
            rhs = Fraction(0, 1)
            for subset in subsets:
                term = Fraction(1, 1)
                for bit, x in zip(subset, xs):
                    if bit:
                        term *= x
                rhs += weight * term
            assert lhs == rhs, (k, xs, lhs, rhs)
            checks += 1
    return checks, norm_rows


def check_unitary_phase_norm():
    vector = [3.0, -4.0, 5.0, -7.0, 11.0]
    phases = [1.0, -1.0, -1.0, 1.0, -1.0]
    before = sum(x * x for x in vector)
    after = sum((x * p) ** 2 for x, p in zip(vector, phases))
    assert before == after
    return before


def kappa(alpha, beta):
    return max(beta / 2, min(alpha, beta))


def r_e(alpha, beta):
    k = kappa(alpha, beta)
    return alpha + beta + max(Fraction(0), Fraction(1) - k) - 2


def check_exponent_atlas():
    critical = []

    # beta<1, alpha=1.
    for beta in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        val = r_e(Fraction(1), beta)
        assert val == 0, (1, beta, val)
        critical.append((Fraction(1), beta))

    # beta=1, 1/2<=alpha<=1.
    for alpha in (Fraction(1, 2), Fraction(3, 5), Fraction(3, 4), Fraction(1)):
        val = r_e(alpha, Fraction(1))
        assert val == 0, (alpha, 1, val)
        critical.append((alpha, Fraction(1)))

    # beta>1, alpha+beta/2=1 in alpha<beta/2 branch.
    for beta in (Fraction(5, 4), Fraction(3, 2), Fraction(7, 4)):
        alpha = 1 - beta / 2
        assert alpha < beta / 2
        val = r_e(alpha, beta)
        assert val == 0, (alpha, beta, val)
        critical.append((alpha, beta))

    assert r_e(Fraction(2, 5), Fraction(1)) < 0
    assert r_e(Fraction(3, 10), Fraction(6, 5)) < 0
    assert r_e(Fraction(1, 2), Fraction(6, 5)) > 0

    return [(str(a), str(b)) for a, b in critical]


def roots_minus_one(v):
    return [r for r in range(v) if (r * r + 1) % v == 0]


def check_signed_root_charts():
    checks = 0
    for v in (5, 13, 17, 29, 37):
        for r in roots_minus_one(v):
            assert r % v not in (0, 1, v - 1)
            charts = {
                "A": lambda m, n: (m % v, n % v, pow(r, -1, v)),
                "B": lambda m, n: (n % v, m % v, r % v),
                "C": lambda m, n: ((m - n) % v, n % v, pow((r - 1) % v, -1, v)),
                "D": lambda m, n: ((m + n) % v, n % v, pow((r + 1) % v, -1, v)),
            }
            for n in range(v):
                m = (r * n) % v
                for name, chart in charts.items():
                    x, y, c = chart(m, n)
                    assert (y - c * x) % v == 0, (v, r, name, m, n, x, y, c)
                    checks += 1
    return checks


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def psi(x: Fraction) -> Fraction:
    return x - floor_fraction(x) - Fraction(1, 2)


def sawtooth_count(L, R, b, v):
    length_term = Fraction(R - L + 1, v)
    return length_term + psi(Fraction(L - 1 - b, v)) - psi(Fraction(R - b, v))


def check_sawtooth_identity():
    checks = 0
    for v in (3, 5, 7, 11):
        for L in range(-4, 5):
            for R in range(L, L + 9):
                for b in range(v):
                    direct = sum(1 for y in range(L, R + 1) if (y - b) % v == 0)
                    formula = sawtooth_count(L, R, b, v)
                    assert formula.denominator == 1
                    assert formula.numerator == direct, (v, L, R, b, direct, formula)
                    checks += 1
    return checks


def main():
    row_energy, tensor_checks = check_row_energies()
    h_checks = check_h_row_equality()
    walsh_checks, walsh_norms = check_e_walsh()
    unitary_norm = check_unitary_phase_norm()
    critical = check_exponent_atlas()
    chart_checks = check_signed_root_charts()
    saw_checks = check_sawtooth_identity()

    report = {
        "metadata": {
            "stage": "14-s5q",
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_TENSOR_INTERFACE",
        },
        "row_energy": row_energy,
        "tensor_product_energy_checks": tensor_checks,
        "h_row_equality_checks": h_checks,
        "e_walsh_identity_checks": walsh_checks,
        "e_walsh_norms": walsh_norms,
        "unitary_phase_norm_squared": unitary_norm,
        "critical_exponent_points": critical,
        "signed_root_chart_checks": chart_checks,
        "sawtooth_identity_checks": saw_checks,
        "decision": {
            "STAGE14_S5Q": "COMPLETE_FOURIER_ENERGY_TENSOR_CONTRACTION_AND_FINAL_E_TRANSITION_KERNEL",
            "ODD_LOCAL_ROW_FOURIER_L2_ENERGY_LE_1": True,
            "GLOBAL_LOCAL_FOURIER_ENERGY_BOUNDED": True,
            "MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED": True,
            "LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": True,
            "E_SELECTED_UNSELECTED_H_ROW_IDENTICAL": True,
            "E_COLUMN_SINGLE_WALSH_SUBSET_EXACT": True,
            "E_WALSH_L1_NORMALIZED": True,
            "E_WALSH_L2_CONTRACTIVE": True,
            "STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS": False,
            "STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED": True,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_REDUCED_TO_SINGLE_E_LINEAR_EDGE": True,
            "E_LINEAR_TRANSITION_WEDGE_PERSISTS": True,
            "FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT": True,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5r",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5Q=COMPLETE_FOURIER_ENERGY_TENSOR_CONTRACTION_AND_FINAL_E_TRANSITION_KERNEL")
    print("ODD_LOCAL_ROW_FOURIER_L2_ENERGY_LE_1=true")
    print("GLOBAL_LOCAL_FOURIER_ENERGY_BOUNDED=true")
    print("MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true")
    print("LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true")
    print("E_SELECTED_UNSELECTED_H_ROW_IDENTICAL=true")
    print("E_COLUMN_SINGLE_WALSH_SUBSET_EXACT=true")
    print("E_WALSH_L1_NORMALIZED=true")
    print("E_WALSH_L2_CONTRACTIVE=true")
    print("STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS=false")
    print("STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_REDUCED_TO_SINGLE_E_LINEAR_EDGE=true")
    print("E_LINEAR_TRANSITION_WEDGE_PERSISTS=true")
    print("FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5r")


if __name__ == "__main__":
    main()
