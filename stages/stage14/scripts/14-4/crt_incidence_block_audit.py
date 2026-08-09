#!/usr/bin/env python3
"""Stage14-4av: audit the bare CRT Euclid-incidence block reduction."""

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AU = ROOT / "stages/stage14/data/14-4/local_indicator_obstruction_summary.json"
S5H = ROOT / "stages/stage14/14-s5h/result.md"
OUT = ROOT / "stages/stage14/data/14-4/crt_incidence_block_summary.json"

FORMS = {
    "m": (1, 0),
    "n": (0, 1),
    "m-n": (1, -1),
    "m+n": (1, 1),
}


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def lin(form, m, n):
    a, b = FORMS[form]
    return a * m + b * n


def incidence_count(form_i, form_j, M, N, u, v):
    total = 0
    for m in range(M + 1, 2 * M + 1):
        for n in range(N + 1, 2 * N + 1):
            if (m - n) % 2 == 0:
                continue
            if lin(form_i, m, n) % u == 0 and lin(form_j, m, n) % v == 0:
                total += 1
    return total


def frac_str(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)


def main():
    au = json.loads(AU.read_text())
    s5h = S5H.read_text()

    assert au["decision"]["RECIPROCAL_DIVISOR_BILINEAR_BOUND_PROVED"] is False
    assert "FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_PROVED=true" in s5h
    assert "EUCLID_INCIDENCE_SEPARABILITY_PROVED=false" in s5h
    assert "WHOLE_KERNEL_GENUINE_RECIPROCAL_EDGE_COUNT=6" in s5h

    names = list(FORMS)
    pairs = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            d = abs(det(FORMS[names[i]], FORMS[names[j]]))
            assert d in (1, 2)
            pairs.append({"edge": f"{names[i]}--{names[j]}", "abs_determinant": d})
    assert len(pairs) == 6

    # Finite consistency check for the elementary lattice-count asymptotic.
    # The theorem uses an absolute O-constant; the numerical test uses a very
    # generous constant and is not the proof.
    samples = []
    for M, N in [(18, 22), (25, 19), (31, 29)]:
        for u, v in [(3, 5), (5, 7), (7, 11), (9, 5), (15, 7)]:
            if math.gcd(u, v) != 1 or u % 2 == 0 or v % 2 == 0:
                continue
            for p in pairs:
                fi, fj = p["edge"].split("--")
                actual = incidence_count(fi, fj, M, N, u, v)
                main_term = M * N / (2 * u * v)
                scale = (M + N) * (1 / u + 1 / v) + 1
                normalized_error = abs(actual - main_term) / scale
                assert normalized_error <= 20
                samples.append(normalized_error)

    kappas = [Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 4), Fraction(1, 3)]
    exponent_rows = []
    for kappa in kappas:
        exponent_rows.append(
            {
                "kappa": frac_str(kappa),
                "main_X_exponent": frac_str(Fraction(2, 1) - kappa / 2),
                "boundary_X_exponent": frac_str(Fraction(2, 1) - kappa),
                "UV_X_exponent": frac_str(Fraction(2, 1) - 2 * kappa),
                "uniform_saving_in_X": frac_str(kappa / 2),
            }
        )

    report = {
        "stage": "14-4av",
        "classification": "BARE_LINEAR_EDGE_CRT_FACTORIZATION_AND_INTERIOR_POWER_SAVING",
        "imported_s5h": {
            "separable_dyadic_bilinear_bound_proved": True,
            "separable_bound": "|sum alpha_u beta_v (u/v)| <<_eps (UV)^eps sqrt(U+V)||alpha||_2||beta||_2",
            "full_euclid_incidence_separability_proved_in_s5h": False,
        },
        "linear_edge_geometry": {
            "forms": FORMS,
            "genuine_whole_kernel_linear_edges": 6,
            "edges": pairs,
            "odd_moduli": True,
            "opposite_parity_density": "1/2",
            "bare_incidence_asymptotic": "C_ij(u,v;M,N)=MN/(2uv)+O((M+N)(1/u+1/v)+1) for coprime odd u,v",
            "proof_mechanism": "solve the two primitive linear congruences sequentially / CRT; odd moduli are independent of the fixed parity split",
        },
        "bare_reciprocal_block": {
            "definition": "B_ij^bare=sum_{u~U}^* sum_{v~V}^* (u/v) C_ij(u,v;M,N)",
            "bound": "<<_eps MN(UV)^eps sqrt(U+V)/sqrt(UV) + (M+N)(U+V) + UV",
            "main_term_input": "s5h separable quadratic-large-sieve bound with alpha_u=1/u, beta_v=1/v",
            "boundary_treatment": "triangle inequality applied only to the elementary CRT lattice-count remainder",
        },
        "balanced_box_interior_range": {
            "assumption": "M~N~X and X^kappa <= U,V <= X^(1-kappa), fixed 0<kappa<1/2",
            "conclusion": "B_ij^bare <<_eps X^(2-kappa/2+eps)",
            "saving_vs_trivial_X2": "X^(-kappa/2+eps)",
            "exponent_table": exponent_rows,
        },
        "finite_consistency": {
            "sample_count": len(samples),
            "max_normalized_lattice_error": max(samples),
            "proof_status": "diagnostic only; theorem is elementary CRT/lattice counting plus the imported s5h bilinear theorem",
        },
        "remaining_full_indicator_obstruction": {
            "name": "GROWING_AUXILIARY_STATE_INCIDENCE_COUPLING",
            "bare_linear_incidence_is_now_factorized": True,
            "still_uncontrolled": [
                "complementary divisor/state pieces that vary with u and v",
                "primitive gcd/Mobius coupling after state splitting",
                "state-split interactions involving pieces of m^2+n^2",
                "small-side, large-side, and strongly unbalanced dyadic endpoint blocks",
            ],
            "fixed_auxiliary_modulus_extension": "CRT factorization persists for finitely many frozen residue conditions coprime to 2uv; the obstruction is that the actual auxiliary modulus grows and is summed over",
        },
        "ci_repair": {
            "stage14_4au_failure_root_cause": "committed JSON used compact five_factors formatting while audit rewrote json.dumps(indent=2)",
            "mathematical_failure": False,
            "summary_format_repaired_on_4av_branch": True,
        },
        "decision": {
            "STAGE14_4AV": "BARE_LINEAR_EDGE_CRT_FACTORIZATION_AND_INTERIOR_POWER_SAVING_PROVED",
            "S5H_SEPARABLE_BILINEAR_BOUND_IMPORTED": True,
            "SIX_LINEAR_WHOLE_KERNEL_EDGES_CRT_FACTORIZED": True,
            "BARE_OPPOSITE_PARITY_INCIDENCE_ASYMPTOTIC_PROVED": True,
            "BARE_RECIPROCAL_BLOCK_BOUND_PROVED": True,
            "INTERIOR_DYADIC_POWER_SAVING_PROVED": True,
            "FULL_AUXILIARY_STATE_WEIGHT_SEPARABILITY_PROVED": False,
            "ENDPOINT_DYADIC_BLOCKS_CONTROLLED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4aw lift the bare CRT block estimate to the growing auxiliary state weight via modulus freezing/dispersion and primitive Mobius bookkeeping, while isolating and summing the dyadic endpoint ranges",
        },
    }

    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
